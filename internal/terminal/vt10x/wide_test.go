package vt10x

import (
	legacy "github.com/hinshun/vt10x"
	"strings"
	"testing"
)

// Expectations count terminal columns, independently of the implementation:
// East Asian Wide/Fullwidth glyphs occupy two cells; CUP is one-based.
func TestWideCells(t *testing.T) {
	for _, tc := range []struct {
		name, input, want string
		cols, x, y        int
	}{
		{"advance", "雪X", "雪X", 8, 3, 0},
		{"address", "雪 X\x1b[1;4HZ", "雪 Z", 8, 4, 0},
		{"overwrite_head", "雪X\x1b[1;1HZ", "Z X", 8, 1, 0},
		{"overwrite_tail", "雪X\x1b[1;2HZ", " ZX", 8, 2, 0},
		{"erase_tail", "雪X\x1b[1;2H\x1b[K", "", 8, 1, 0},
		{"wrap_before_wide", "abc雪X", "abc\n雪X", 4, 3, 1},
		{"wrap_after_wide", "ab雪X", "ab雪\nX", 4, 1, 1},
		{"fullwidth", "ＡX", "ＡX", 8, 3, 0},
		{"insert_before", "雪XY\x1b[1;1H\x1b[@", " 雪XY", 8, 0, 0},
		{"insert_tail", "雪XY\x1b[1;2H\x1b[@", "   XY", 8, 1, 0},
		{"delete_half", "雪XY\x1b[1;1H\x1b[P", " XY", 8, 0, 0},
		{"delete_pair", "雪XY\x1b[1;1H\x1b[2P", "XY", 8, 0, 0},
		{"leading_spaces", "  雪X", "  雪X", 8, 5, 0},
		{"nowrap_clip", "abc\x1b[?7l雪", "abc", 4, 3, 0},
		{"one_column_clip", "雪X", "\nX", 1, 0, 1},
	} {
		t.Run(tc.name, func(t *testing.T) {
			v := New(WithSize(tc.cols, 3))
			for _, b := range []rune(tc.input) {
				_, _ = v.Write([]byte(string(b)))
			}
			rows := strings.Split(strings.TrimSuffix(v.String(), "\n"), "\n")
			for i := range rows {
				rows[i] = strings.TrimRight(rows[i], " \x00")
			}
			got := strings.TrimRight(strings.Join(rows, "\n"), "\n")
			if got != tc.want {
				t.Errorf("screen = %q; want %q", got, tc.want)
			}
			if c := v.Cursor(); c.X != tc.x || c.Y != tc.y {
				t.Errorf("cursor = (%d,%d); want (%d,%d)", c.X, c.Y, tc.x, tc.y)
			}
		})
	}
}

func BenchmarkCellWrites(b *testing.B) {
	for _, input := range []string{"ascii status\r\x1b[K", "雪X\r\x1b[K"} {
		b.Run(input, func(b *testing.B) {
			for _, tc := range []struct {
				name     string
				terminal interface{ Write([]byte) (int, error) }
			}{
				{"baseline", legacy.New(legacy.WithSize(80, 24))},
				{"repaired", New(WithSize(80, 24))},
			} {
				b.Run(tc.name, func(b *testing.B) {
					data := []byte(input)
					b.ReportAllocs()
					b.SetBytes(int64(len(data)))
					b.ResetTimer()
					for i := 0; i < b.N; i++ {
						_, _ = tc.terminal.Write(data)
					}
				})
			}
		})
	}
}
