package console

import (
	"context"
	"io"
	"os"
	"testing"
	"time"
)

func TestDecodeSplitUnicodeKeysAndUnsupportedInput(t *testing.T) {
	events, rest, err := Decode([]byte("a\x1b["), false)
	if err != nil || len(events) != 1 || len(rest) != 2 {
		t.Fatalf("%v %q %v", events, rest, err)
	}
	events, rest, err = Decode(append(rest, 'B'), false)
	if err != nil || len(rest) != 0 || events[0].Key != "ArrowDown" {
		t.Fatal(events, err)
	}
	_, rest, err = Decode([]byte{0xc3}, false)
	if err != nil || len(rest) != 1 {
		t.Fatal(err)
	}
	events, _, err = Decode(append(rest, 0xa9), false)
	if err != nil || events[0].Text != "é" {
		t.Fatal(events, err)
	}
	for _, bad := range [][]byte{{255}, []byte("\x1b[99~"), {1}} {
		if _, _, err := Decode(bad, true); err == nil {
			t.Fatalf("silently accepted %q", bad)
		}
	}
	events, _, err = Decode([]byte{27}, true)
	if err != nil || events[0].Key != "Escape" {
		t.Fatal(events, err)
	}
}

func TestNativeRedirectedInputAndIdleCancellation(t *testing.T) {
	read, write, err := os.Pipe()
	if err != nil {
		t.Fatal(err)
	}
	defer read.Close()
	defer write.Close()
	input, err := Open(read)
	if err != nil {
		t.Fatal(err)
	}
	defer input.Close()
	ctx, cancel := context.WithTimeout(context.Background(), 50*time.Millisecond)
	defer cancel()
	for {
		_, err = input.Read(ctx)
		if err != nil {
			break
		}
	}
	if err != context.DeadlineExceeded {
		t.Fatal(err)
	}
	if _, err := write.Write([]byte("native input")); err != nil {
		t.Fatal(err)
	}
	data, err := input.Read(context.Background())
	if err != nil || string(data) != "native input" {
		t.Fatalf("%q %v", data, err)
	}
	write.Close()
	_, err = input.Read(context.Background())
	if err != io.EOF {
		t.Fatalf("EOF: %v", err)
	}
}
