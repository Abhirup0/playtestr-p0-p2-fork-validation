//go:build !windows

package runner

import (
	"context"
	"os"
	"strings"
	"testing"
	"time"
)

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
