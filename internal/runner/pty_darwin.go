package runner

import (
	"errors"
	"os"
	"sync"

	"github.com/charmbracelet/x/xpty"
	"golang.org/x/sys/unix"
)

type darwinTerminalPty struct {
	*xpty.UnixPty
	mu     sync.Mutex
	closed bool
	fd     int
}

// macOS can discard unread output when the last slave descriptor closes. Keep
// the parent's slave until ordinary bounded session cleanup. Linux's EOF
// optimization is intentionally separate; a delayed-reader regression exercises
// both paths without relying on goroutine scheduling.
func newTerminalPty(width, height int) (xpty.Pty, error) {
	p, err := xpty.NewUnixPty(width, height)
	if err != nil {
		return nil, err
	}
	fd := int(p.Master().Fd())
	if err := unix.SetNonblock(fd, true); err != nil {
		_ = p.Close()
		return nil, err
	}
	return &darwinTerminalPty{UnixPty: p, fd: fd}, nil
}

func (p *darwinTerminalPty) Read(buffer []byte) (int, error) {
	// A blocking Darwin tty read may keep os.File.Close waiting even after
	// process exit. Poll nonblocking reads with a bounded lock interval so
	// cleanup can close both descriptors and the reader observes shutdown.
	for {
		p.mu.Lock()
		if p.closed {
			p.mu.Unlock()
			return 0, os.ErrClosed
		}
		fd := p.fd
		events := []unix.PollFd{{Fd: int32(fd), Events: unix.POLLIN}}
		ready, err := unix.Poll(events, 25)
		if err == nil && ready > 0 {
			var n int
			n, err = unix.Read(fd, buffer)
			p.mu.Unlock()
			if err == unix.EAGAIN || err == unix.EINTR {
				continue
			}
			return n, err
		}
		p.mu.Unlock()
		if err != nil && err != unix.EINTR {
			return 0, err
		}
	}
}

func (p *darwinTerminalPty) Close() error {
	p.mu.Lock()
	defer p.mu.Unlock()
	if p.closed {
		return nil
	}
	p.closed = true
	// Release the slave before closing the master: an in-flight master read
	// must wake before os.File.Close waits for that read to finish.
	return errors.Join(p.Slave().Close(), p.Master().Close())
}
