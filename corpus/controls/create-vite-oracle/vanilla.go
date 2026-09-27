package main

import (
	"bytes"
	"embed"
	"encoding/json"
	"fmt"
	"io"
	"io/fs"
	"os"
	"path/filepath"
	"sort"
	"strings"
)

// Reviewed before E1 execution from the pinned create-vite 9.2.1 template.
// These are MIT-licensed Vite template assets, not captured generated output.
//
//go:embed all:vanilla-golden
var vanillaGolden embed.FS

func verifyVanillaTree(directory, name string) error {
	expected := map[string][]byte{}
	expectedDirs := map[string]bool{".": true}
	err := fs.WalkDir(vanillaGolden, "vanilla-golden", func(path string, entry fs.DirEntry, err error) error {
		if err != nil {
			return err
		}
		if entry.IsDir() {
			if path != "vanilla-golden" {
				expectedDirs[strings.TrimPrefix(path, "vanilla-golden/")] = true
			}
			return nil
		}
		key := strings.TrimPrefix(path, "vanilla-golden/")
		if key == "_gitignore" {
			key = ".gitignore"
		}
		data, err := vanillaGolden.ReadFile(path)
		if err != nil {
			return err
		}
		if key == "index.html" {
			data = bytes.Replace(data, []byte("<title>Vite + JS</title>"), []byte("<title>"+name+"</title>"), 1)
		}
		if key == "package.json" {
			var value map[string]any
			if err := json.Unmarshal(data, &value); err != nil {
				return err
			}
			value["name"] = name
			data, err = json.Marshal(value)
			if err != nil {
				return err
			}
		}
		expected[key] = data
		return nil
	})
	if err != nil {
		return fmt.Errorf("reviewed vanilla input: %w", err)
	}
	var actualNames []string
	err = filepath.WalkDir(directory, func(path string, entry fs.DirEntry, err error) error {
		if err != nil {
			return err
		}
		rel, err := filepath.Rel(directory, path)
		if err != nil {
			return err
		}
		key := filepath.ToSlash(rel)
		if entry.IsDir() {
			if !expectedDirs[key] {
				return fmt.Errorf("unexpected scaffold directory %s", key)
			}
			return nil
		}
		want, ok := expected[key]
		if !ok {
			return fmt.Errorf("unexpected scaffold file %s", key)
		}
		info, err := entry.Info()
		if err != nil {
			return err
		}
		if !info.Mode().IsRegular() || info.Size() > int64(len(want)+65536) {
			return fmt.Errorf("unsafe or oversized scaffold file %s", key)
		}
		file, err := os.Open(path)
		if err != nil {
			return err
		}
		got, readErr := io.ReadAll(io.LimitReader(file, int64(len(want)+65537)))
		closeErr := file.Close()
		if readErr != nil {
			return fmt.Errorf("read scaffold %s: %w", key, readErr)
		}
		if closeErr != nil {
			return fmt.Errorf("close scaffold %s: %w", key, closeErr)
		}
		if len(got) > len(want)+65536 {
			return fmt.Errorf("scaffold file grew beyond bound: %s", key)
		}
		if key == "package.json" {
			var value map[string]any
			if err := json.Unmarshal(got, &value); err != nil {
				return fmt.Errorf("decode scaffold package: %w", err)
			}
			got, err = json.Marshal(value)
			if err != nil {
				return err
			}
		}
		if !bytes.Equal(got, want) {
			return fmt.Errorf("exact scaffold bytes/fields differ: %s", key)
		}
		actualNames = append(actualNames, key)
		return nil
	})
	if err != nil {
		return err
	}
	if len(actualNames) != len(expected) {
		sort.Strings(actualNames)
		return fmt.Errorf("scaffold file set has %d files, want %d: %v", len(actualNames), len(expected), actualNames)
	}
	return nil
}
