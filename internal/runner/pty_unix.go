//go:build !windows

package runner

import (
	"errors"
	"fmt"
	"os/exec"

	"github.com/charmbracelet/x/xpty"
)

// unixTerminalPty releases the parent's slave after the child inherits it.
// Keeping that duplicate open prevents the master reader from reaching EOF
// when the target and its descendants finish, forcing a full drain timeout.
type unixTerminalPty struct {
	*xpty.UnixPty
	slaveReleased bool
	releaseErr    error
}

func newTerminalPty(width, height int) (xpty.Pty, error) {
	p, err := xpty.NewUnixPty(width, height)
	if err != nil {
		return nil, err
	}
	return &unixTerminalPty{UnixPty: p}, nil
}

func (p *unixTerminalPty) Start(cmd *exec.Cmd) error {
	if err := p.UnixPty.Start(cmd); err != nil {
		return err
	}
	p.slaveReleased = true
	if err := p.Slave().Close(); err != nil {
		// The child has started: retain a cleanup error rather than returning
		// a start failure that would bypass process observation and shutdown.
		p.releaseErr = fmt.Errorf("release parent terminal slave: %w", err)
	}
	return nil
}

func (p *unixTerminalPty) Close() error {
	if !p.slaveReleased {
		return p.UnixPty.Close()
	}
	// Slave was already closed after successful start. Closing it twice
	// would create a spurious cleanup failure; the master remains owned here.
	return errors.Join(p.Master().Close(), p.releaseErr)
}
