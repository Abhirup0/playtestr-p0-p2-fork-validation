package main

import (
	"os"
	"path/filepath"
	"testing"
)

// This exercises the independent persisted-state reader with the real pinned
// interpreter. A success-looking UI cannot rescue a corrupt or missing file.
func TestSavedRequestState(t *testing.T) {
	oracle, err := filepath.Abs("../../../.trial-private/corpus-tools/posting-oracle")
	if err != nil {
		t.Fatal(err)
	}
	python := postingExecutable(oracle, "python")
	if _, err := os.Stat(python); err != nil {
		t.Skip("pinned Posting interpreter unavailable")
	}
	for _, tc := range []struct {
		name, content string
		missing, pass bool
	}{
		{"reviewed", "name: Reviewed Saved Request\nmethod: GET\nurl: http://127.0.0.1:28741/saved\noptions: {follow_redirects: false, timeout: 3.0}\n", false, true},
		{"serializer defaults", "name: Reviewed Saved Request\nurl: http://127.0.0.1:28741/saved\n", false, true},
		{"wrong URL", "name: Reviewed Saved Request\nurl: http://127.0.0.1:28741/stale\n", false, false},
		{"wrong name", "name: Other\nurl: http://127.0.0.1:28741/saved\n", false, false},
		{"missing", "", true, false},
	} {
		t.Run(tc.name, func(t *testing.T) {
			path := filepath.Join(t.TempDir(), "reviewed-name.posting.yaml")
			if !tc.missing {
				if err := os.WriteFile(path, []byte(tc.content), 0600); err != nil {
					t.Fatal(err)
				}
			}
			err := verifySavedRequest(python, path, "http://127.0.0.1:28741/saved")
			if (err == nil) != tc.pass {
				t.Fatalf("pass=%v error=%v", tc.pass, err)
			}
		})
	}
}
