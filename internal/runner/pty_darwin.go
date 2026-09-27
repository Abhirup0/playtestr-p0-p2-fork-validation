package runner

import "github.com/charmbracelet/x/xpty"

// macOS can discard unread output when the last slave descriptor closes. Keep
// the parent's slave until ordinary bounded session cleanup. Linux's EOF
// optimization is intentionally separate; a delayed-reader regression exercises
// both paths without relying on goroutine scheduling.
func newTerminalPty(width, height int) (xpty.Pty, error) {
	return xpty.NewUnixPty(width, height)
}
