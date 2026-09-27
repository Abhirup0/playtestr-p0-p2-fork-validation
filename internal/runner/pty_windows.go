package runner

import "github.com/charmbracelet/x/xpty"

func newTerminalPty(width, height int) (xpty.Pty, error) {
	return xpty.NewPty(width, height)
}
