// Package console provides bounded native operator input, independent of target PTYs.
package console

import (
	"context"
	"fmt"
	"os"
	"time"

	"golang.org/x/term"
)

// Input owns restoration of the operator terminal. Read polls so cancellation
// does not leave a blocked reader goroutine or require closing the user's stdin.
type Input struct {
	file  *os.File
	state *term.State
}

// Open enters raw mode only for a real console; redirected input stays readable.
func Open(file *os.File) (*Input, error) {
	i := &Input{file: file}
	if term.IsTerminal(int(file.Fd())) {
		state, err := term.MakeRaw(int(file.Fd()))
		if err != nil {
			return nil, fmt.Errorf("enter operator raw mode: %w", err)
		}
		i.state = state
	}
	return i, nil
}

// Close restores terminal modes and is idempotent.
func (i *Input) Close() error {
	if i.state == nil {
		return nil
	}
	state := i.state
	i.state = nil
	return term.Restore(int(i.file.Fd()), state)
}

// Read returns available bytes or a bounded idle interval. No background reader.
func (i *Input) Read(ctx context.Context) ([]byte, error) {
	if err := ctx.Err(); err != nil {
		return nil, err
	}
	data, err := readNative(i.file, i.state != nil)
	if len(data) == 0 && err == nil {
		timer := time.NewTimer(20 * time.Millisecond)
		defer timer.Stop()
		select {
		case <-ctx.Done():
			return nil, ctx.Err()
		case <-timer.C:
		}
	}
	return data, err
}
