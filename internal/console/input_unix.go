//go:build !windows

package console

import (
	"golang.org/x/sys/unix"
	"io"
	"os"
)

func readNative(file *os.File, raw bool) ([]byte, error) {
	poll := []unix.PollFd{{Fd: int32(file.Fd()), Events: unix.POLLIN}}
	_, err := unix.Poll(poll, 0)
	if err != nil {
		if err == unix.EINTR {
			return nil, nil
		}
		return nil, err
	}
	if poll[0].Revents == 0 {
		return nil, nil
	}
	buffer := make([]byte, 4096)
	n, err := unix.Read(int(file.Fd()), buffer)
	if n == 0 && err == nil {
		return nil, io.EOF
	}
	return buffer[:max(n, 0)], err
}
