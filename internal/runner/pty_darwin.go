package runner

import (
	"errors"

	"github.com/charmbracelet/x/xpty"
)

type darwinTerminalPty struct{ *xpty.UnixPty }

// macOS can discard unread output when the last slave descriptor closes. Keep
// the parent's slave until ordinary bounded session cleanup. Linux's EOF
// optimization is intentionally separate; a delayed-reader regression exercises
// both paths without relying on goroutine scheduling.
func newTerminalPty(width, height int) (xpty.Pty, error) {
	p, err := xpty.NewUnixPty(width, height)
	if err != nil {
		return nil, err
	}
	return &darwinTerminalPty{p}, nil
}

func (p *darwinTerminalPty) Close() error {
	// Release the slave before closing the master: an in-flight master read
	// must wake before os.File.Close waits for that read to finish.
	return errors.Join(p.Slave().Close(), p.Master().Close())
}
