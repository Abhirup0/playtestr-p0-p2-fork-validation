//go:build !windows

package runner

import (
	"context"
	"os"
	"os/exec"
	"strings"
	"testing"
	"time"
)

// Starting a reader after a tiny target exits is a valid scheduling outcome.
// Retain final bytes even when the target's last slave descriptor is closed.
func TestTerminalPreservesOutputBeforeReaderStarts(t *testing.T) {
	p, err := newTerminalPty(40, 8)
	if err != nil {
		t.Fatal(err)
	}
	t.Cleanup(func() { _ = p.Close() })
	ctx, cancel := context.WithTimeout(context.Background(), 3*time.Second)
	defer cancel()
	cmd := exec.CommandContext(ctx, os.Args[0], "-test.run=TestHelperProcess", "--", "exit-zero")
	cmd.Env = targetEnvironment(Spec{Version: SpecVersion, Env: map[string]string{"PLAYTESTR_HELPER_PROCESS": "1"}})
	configureProcess(cmd)
	if err := p.Start(cmd); err != nil {
		t.Fatal(err)
	}
	if err := cmd.Wait(); err != nil {
		t.Fatal(err)
	}
	type readResult struct {
		data string
		err  error
	}
	read := make(chan readResult, 1)
	go func() {
		buffer := make([]byte, 4096)
		n, err := p.Read(buffer)
		read <- readResult{string(buffer[:n]), err}
	}()
	select {
	case result := <-read:
		if !strings.Contains(result.data, "finished cleanly") {
			t.Fatalf("final output missing after exit: %q, read error: %v", result.data, result.err)
		}
	case <-ctx.Done():
		_ = p.Close()
		select {
		case <-read:
		case <-time.After(time.Second):
			t.Error("reader did not stop after master close")
		}
		t.Fatal("final output read timed out")
	}
}

// The child's final bytes must be readable to EOF without closing the master
// or waiting for the final-drain deadline. A parent-held slave prevents EOF.
func TestNaturalExitReachesTerminalEOF(t *testing.T) {
	session, err := startTerminalSession(sessionConfig{
		command: []string{os.Args[0], "-test.run=TestHelperProcess", "--", "exit-zero"},
		env:     targetEnvironment(Spec{Version: SpecVersion, Env: map[string]string{"PLAYTESTR_HELPER_PROCESS": "1"}}),
		width:   40, height: 8, maxOutputBytes: 100000,
	})
	if err != nil {
		t.Fatal(err)
	}
	t.Cleanup(func() {
		ctx, cancel := context.WithTimeout(context.Background(), 3*time.Second)
		defer cancel()
		if result := session.stop(ctx); result.err != nil {
			t.Errorf("cleanup: %v", result.err)
		}
	})
	ctx, cancel := context.WithTimeout(context.Background(), 3*time.Second)
	defer cancel()
	code, err, exited := session.outcome.wait(ctx)
	if !exited || err != nil || code != 0 {
		t.Fatalf("natural exit: code=%d exited=%v error=%v", code, exited, err)
	}
	select {
	case <-session.readerDone:
	case <-ctx.Done():
		t.Fatal("terminal reader did not reach EOF after natural exit")
	}
	if screen := session.observe().screen; !strings.Contains(screen, "finished cleanly") {
		t.Fatalf("final output missing: %q", screen)
	}
}
