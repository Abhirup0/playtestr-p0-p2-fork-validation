package main

import (
	"bytes"
	"io/fs"
	"os"
	"path/filepath"
	"strings"
	"testing"
)

func TestVanillaScaffoldRequiresExactState(t *testing.T) {
	for _, tc := range []struct {
		name, path  string
		remove      bool
		directory   bool
		replacement []byte
	}{
		{name: "reviewed"},
		{name: "missing asset", path: "src/assets/hero.png", remove: true},
		{name: "extra file", path: "unexpected.txt", replacement: []byte("unexpected")},
		{name: "extra empty directory", path: "unexpected", directory: true},
		{name: "corrupt counter", path: "src/counter.js", replacement: []byte("wrong behavior")},
		{name: "wrong preview script", path: "package.json", replacement: []byte(`{"name":"cv-vanilla","version":"0.0.0","private":true,"type":"module","scripts":{"dev":"vite","build":"vite build","preview":"wrong"},"devDependencies":{"vite":"^8.3.0"}}`)},
	} {
		t.Run(tc.name, func(t *testing.T) {
			t.Chdir(t.TempDir())
			err := fs.WalkDir(vanillaGolden, "vanilla-golden", func(path string, entry fs.DirEntry, err error) error {
				if err != nil {
					return err
				}
				if entry.IsDir() {
					return nil
				}
				name := strings.TrimPrefix(path, "vanilla-golden/")
				if name == "_gitignore" {
					name = ".gitignore"
				}
				data, err := vanillaGolden.ReadFile(path)
				if err != nil {
					return err
				}
				if name == "package.json" {
					data = bytes.Replace(data, []byte("vite-starter"), []byte("cv-vanilla"), 1)
				}
				if name == "index.html" {
					data = bytes.Replace(data, []byte("Vite + JS"), []byte("cv-vanilla"), 1)
				}
				dest := filepath.Join("cv-vanilla", filepath.FromSlash(name))
				if err := os.MkdirAll(filepath.Dir(dest), 0755); err != nil {
					return err
				}
				return os.WriteFile(dest, data, 0600)
			})
			if err != nil {
				t.Fatal(err)
			}
			if tc.path != "" {
				path := filepath.Join("cv-vanilla", filepath.FromSlash(tc.path))
				if tc.directory {
					err = os.Mkdir(path, 0755)
				} else if tc.remove {
					err = os.Remove(path)
				} else {
					err = os.WriteFile(path, tc.replacement, 0600)
				}
				if err != nil {
					t.Fatal(err)
				}
			}
			err = verify("vanilla")
			if (err == nil) != (tc.name == "reviewed") {
				t.Fatalf("exact state result: %v", err)
			}
		})
	}
}
