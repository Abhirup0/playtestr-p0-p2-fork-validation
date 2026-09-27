// Command workspace-launch supplies identical fixture, oracle and cleanup glue
// to E2 real-task adapters. It is experiment infrastructure, not runner code.
package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"io"
	"os"
	"os/exec"
	"path/filepath"
)

func main() { os.Exit(run()) }

func run() int {
	journey := flag.String("journey", "", "RW1 or RW3")
	variant := flag.String("variant", "good", "good or defect")
	output := flag.String("output", "", "absolute independent result file")
	flag.Parse()
	if (*journey != "RW1" && *journey != "RW3") || (*variant != "good" && *variant != "defect") || !filepath.IsAbs(*output) {
		fmt.Fprintln(os.Stderr, "invalid experiment arguments")
		return 2
	}
	root, err := os.Getwd()
	if err != nil {
		return 2
	}
	project, profile := "lazygit", "stage-neighbor"
	if *journey == "RW3" {
		project, profile = "create-vite", "corrected"
	}
	workspace, err := os.MkdirTemp("", "playtestr-e2-common-")
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		return 2
	}
	// Final cleanup happens before the independent result and success marker.
	code := 0
	err = copyFixture(filepath.Join(root, "corpus", "workflows", project, "fixture"), workspace)
	if err == nil {
		for _, name := range []string{".managed-home", ".managed-temp"} {
			if err = os.Mkdir(filepath.Join(workspace, name), 0700); err != nil {
				break
			}
		}
	}
	if err == nil {
		args := []string{profile}
		if *journey == "RW3" {
			args = append(args, "Bad Name", "--interactive")
		}
		cmd := exec.Command(filepath.Join(root, ".trial-private", "corpus-tools", project+"-oracle"), args...)
		cmd.Dir = workspace
		cmd.Stdin, cmd.Stdout, cmd.Stderr = os.Stdin, os.Stdout, os.Stderr
		cmd.Env = append(os.Environ(), "HOME="+filepath.Join(workspace, ".managed-home"), "TMPDIR="+filepath.Join(workspace, ".managed-temp"), "PLAYTESTR_LAZYGIT_MUTATION=0", "PLAYTESTR_CREATE_VITE_RUNTIME=create-vite-runtime")
		if *variant == "defect" {
			if *journey == "RW1" {
				cmd.Env = append(cmd.Env, "PLAYTESTR_LAZYGIT_MUTATION=1")
			} else {
				cmd.Env = append(cmd.Env, "PLAYTESTR_CREATE_VITE_RUNTIME=create-vite-code-mutated-runtime")
			}
		}
		err = cmd.Run()
		if exit, ok := err.(*exec.ExitError); ok {
			code = exit.ExitCode()
		}
	}
	if err != nil && code == 0 {
		code = 1
	}
	cleanErr := os.RemoveAll(workspace)
	if cleanErr != nil {
		fmt.Fprintf(os.Stderr, "common workspace cleanup: %v\n", cleanErr)
		code = 1
	}
	record := struct {
		Journey string `json:"journey"`
		Variant string `json:"variant"`
		Exit    int    `json:"exit"`
		Cleaned bool   `json:"cleaned"`
	}{*journey, *variant, code, cleanErr == nil}
	data, _ := json.Marshal(record)
	if err := os.WriteFile(*output, append(data, '\n'), 0600); err != nil {
		fmt.Fprintln(os.Stderr, err)
		return 1
	}
	if err != nil {
		fmt.Fprintf(os.Stderr, "independent state oracle: %v\n", err)
	}
	if code == 0 {
		fmt.Printf("PLAYTESTR-E2-%s-WRAPPER-OK\n", *journey)
	}
	return code
}

func copyFixture(source, destination string) error {
	count := 0
	return filepath.WalkDir(source, func(path string, entry os.DirEntry, walkErr error) error {
		if walkErr != nil {
			return walkErr
		}
		rel, err := filepath.Rel(source, path)
		if err != nil {
			return err
		}
		to := filepath.Join(destination, rel)
		if entry.IsDir() {
			return os.MkdirAll(to, 0700)
		}
		count++
		if count > 200 {
			return fmt.Errorf("fixture exceeds file bound")
		}
		info, err := entry.Info()
		if err != nil {
			return err
		}
		if !info.Mode().IsRegular() || info.Size() > 1<<20 {
			return fmt.Errorf("invalid fixture file %s", rel)
		}
		input, err := os.Open(path)
		if err != nil {
			return err
		}
		data, readErr := io.ReadAll(io.LimitReader(input, (1<<20)+1))
		closeErr := input.Close()
		if readErr != nil {
			return readErr
		}
		if closeErr != nil {
			return closeErr
		}
		if len(data) > 1<<20 {
			return fmt.Errorf("fixture grew beyond bound")
		}
		return os.WriteFile(to, data, 0600)
	})
}
