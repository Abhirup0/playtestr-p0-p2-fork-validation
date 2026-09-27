// cell-probe records a reduced, explicitly reviewed terminal-width boundary.
// It is evidence tooling, not a second product terminal implementation.
package main

import (
	"bytes"
	"encoding/hex"
	"encoding/json"
	"os"
	"strings"

	"github.com/hinshun/vt10x"
)

func main() {
	// Tailored contract: Snow occupies columns 0–1, ASCII X occupies column 2,
	// and the cursor is at column 3. CUP 1;4 must overwrite the space after X.
	// This is a selected fixed-cell contract, not a claim about every grapheme.
	rows := []map[string]any{}
	for _, probe := range []struct {
		name, input, expected string
		x                     int
	}{
		{"wide-cursor", "\u96eaX", "\u96eaX", 3},
		{"wide-addressed-redraw", "\u96ea X\x1b[1;4HZ", "\u96ea Z", 4},
		{"combining-cursor", "e\u0301X", "e\u0301X", 2},
		{"ascii-control", "abX", "abX", 3},
	} {
		terminal := vt10x.New(vt10x.WithSize(12, 3))
		_, _ = terminal.Write([]byte(probe.input))
		cursor := terminal.Cursor()
		screen := strings.TrimRight(strings.Split(terminal.String(), "\n")[0], " ")
		rows = append(rows, map[string]any{"case": probe.name, "input_hex": hex.EncodeToString([]byte(probe.input)),
			"expected_text": probe.expected, "expected_cursor_x": probe.x, "expected_cursor_y": 0,
			"observed_text": screen, "observed_cursor_x": cursor.X, "observed_cursor_y": cursor.Y,
			"contract_matches": screen == probe.expected && cursor.X == probe.x && cursor.Y == 0})
	}
	var replies bytes.Buffer
	queryTerminal := vt10x.New(vt10x.WithSize(12, 3), vt10x.WithWriter(&replies))
	_, _ = queryTerminal.Write([]byte("\x1b[6n"))
	rows = append(rows, map[string]any{"case": "cursor-position-query", "input_hex": "1b5b366e",
		"expected_response_hex": "1b5b313b3152", "observed_response_hex": hex.EncodeToString(replies.Bytes()),
		"contract_matches": bytes.Equal(replies.Bytes(), []byte("\x1b[1;1R"))})
	encoder := json.NewEncoder(os.Stdout)
	encoder.SetIndent("", "  ")
	if err := encoder.Encode(rows); err != nil {
		panic(err)
	}
}
