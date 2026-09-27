package main

import (
	"context"
	"fmt"
	"io"
	"net"
	"net/http"
	"os"
	"os/exec"
	"path/filepath"
	"runtime"
	"strings"
	"sync"
	"time"
)

type observation struct{ method, uri, body, header string }

func main() {
	if len(os.Args) != 2 {
		fail("usage: posting-oracle PROFILE")
	}
	profile := os.Args[1]
	var mu sync.Mutex
	var seen []observation
	var server *http.Server
	if profile == "failure" {
		listener, err := net.Listen("tcp", "127.0.0.1:28742")
		if err != nil {
			fail("listen failure endpoint: %v", err)
		}
		defer listener.Close()
		go func() {
			connection, err := listener.Accept()
			if err == nil {
				mu.Lock()
				seen = append(seen, observation{method: "CONNECT_ATTEMPT"})
				mu.Unlock()
				fmt.Println("PLAYTESTR-POST-FAILURE-CONNECTED")
				connection.Close()
			}
		}()
	} else {
		listener, err := net.Listen("tcp", "127.0.0.1:28741")
		if err != nil {
			fail("listen: %v", err)
		}
		server = &http.Server{Handler: http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			if os.Getenv("PLAYTESTR_POSTING_SLOW_RESPONSE") == "1" {
				time.Sleep(200 * time.Millisecond)
			}
			body, _ := io.ReadAll(io.LimitReader(r.Body, 4096))
			mu.Lock()
			seen = append(seen, observation{r.Method, r.URL.RequestURI(), string(body), r.Header.Get("X-Playtestr")})
			mu.Unlock()
			w.Header().Set("Content-Type", "application/json")
			fmt.Fprintf(w, `{"marker":"PLAYTESTR-POST-%s","path":%q}`, strings.ToUpper(profile), r.URL.RequestURI())
		})}
		go server.Serve(listener)
		defer server.Close()
	}
	exe, err := os.Executable()
	if err != nil {
		fail("locate oracle: %v", err)
	}
	target := postingExecutable(exe, "posting")
	cwd, err := os.Getwd()
	if err != nil {
		fail("cwd: %v", err)
	}
	collectionProfile := profile
	if profile == "save-send" {
		collectionProfile = "save"
	}
	command := exec.Command(target, "default", "--collection", filepath.Join(cwd, "collection", collectionProfile))
	command.Stdin, command.Stdout, command.Stderr = os.Stdin, os.Stdout, os.Stderr
	command.Env = append(os.Environ(), "POSTING_CONFIG_FILE="+filepath.Join(cwd, "posting.yaml"), "XDG_CONFIG_HOME="+filepath.Join(cwd, "config"), "XDG_DATA_HOME="+filepath.Join(cwd, "data"))
	if os.Getenv("PLAYTESTR_POSTING_MUTATION") == "1" {
		command.Env = append(command.Env, "PYTHONPATH="+filepath.Join(filepath.Dir(exe), "posting-mutated"))
	}
	if os.Getenv("PLAYTESTR_POSTING_SAVE_MUTATION") == "1" {
		command.Env = append(command.Env, "PYTHONPATH="+filepath.Join(filepath.Dir(exe), "posting-save-mutated"))
	}
	if os.Getenv("PLAYTESTR_POSTING_UI_CHANGE") == "1" {
		variant := "posting-ui-changed"
		if os.Getenv("PLAYTESTR_POSTING_SAVE_MUTATION") == "1" {
			variant = "posting-ui-save-mutated"
		}
		command.Env = append(command.Env, "PYTHONPATH="+filepath.Join(filepath.Dir(exe), variant))
	}
	if err := command.Run(); err != nil {
		if e, ok := err.(*exec.ExitError); ok {
			os.Exit(e.ExitCode())
		}
		fail("run posting: %v", err)
	}
	mu.Lock()
	observations := append([]observation(nil), seen...)
	mu.Unlock()
	if err := verify(profile, observations); err != nil {
		fail("profile %s: %v", profile, err)
	}
	fmt.Printf("PLAYTESTR-POST-ORACLE %s OK\n", profile)
}

func verify(profile string, seen []observation) error {
	if profile == "failure" {
		if len(seen) != 1 || seen[0].method != "CONNECT_ATTEMPT" {
			return fmt.Errorf("connection attempts=%v", seen)
		}
		return nil
	}
	if profile == "cancel" || profile == "save" {
		if len(seen) != 0 {
			return fmt.Errorf("unexpected requests: %v", seen)
		}
		if profile == "save" {
			exe, err := os.Executable()
			if err != nil {
				return fmt.Errorf("locate saved-state oracle: %w", err)
			}
			python := postingExecutable(exe, "python")
			return verifySavedRequest(python, filepath.Join("collection", "save", "reviewed-name.posting.yaml"), "http://127.0.0.1:28741/saved")
		}
		return nil
	}
	if len(seen) != 1 {
		return fmt.Errorf("requests=%d, want 1", len(seen))
	}
	o := seen[0]
	switch profile {
	case "save-send":
		if o.method != "GET" || o.uri != "/saved-edited" || o.body != "" {
			return fmt.Errorf("edited request differs: %+v", o)
		}
		exe, err := os.Executable()
		if err != nil {
			return fmt.Errorf("locate saved-state oracle: %w", err)
		}
		python := postingExecutable(exe, "python")
		return verifySavedRequest(python, filepath.Join("collection", "save", "reviewed-name.posting.yaml"), "http://127.0.0.1:28741/saved-edited")
	case "get", "reopen":
		if o.method != "GET" || o.uri != "/marker" {
			return fmt.Errorf("got %s %s", o.method, o.uri)
		}
	case "query":
		if o.method != "GET" || o.uri != "/query?alpha=one&space=two" {
			return fmt.Errorf("got %s %s", o.method, o.uri)
		}
	case "body":
		if o.method != "POST" || o.uri != "/body" || o.body != `{"value":"PLAYTESTR-BODY"}` {
			return fmt.Errorf("got %+v", o)
		}
	case "header":
		if o.method != "GET" || o.uri != "/header" || o.header != "synthetic-value" {
			return fmt.Errorf("got %+v", o)
		}
	default:
		return fmt.Errorf("unknown profile")
	}
	return nil
}

func postingExecutable(oracle, name string) string {
	if runtime.GOOS == "windows" {
		return filepath.Clean(filepath.Join(filepath.Dir(oracle), "..", "r3c", "windows", "py-01-posting", "venv", "Scripts", name+".exe"))
	}
	return filepath.Clean(filepath.Join(filepath.Dir(oracle), "..", "r3c", runtime.GOOS, "py-01-posting", "venv", "bin", name))
}

// Read persisted YAML independently of Posting's request model and screen.
// Defaults omitted by the target serializer have their reviewed values here.
const savedRequestOracle = `import pathlib,sys,yaml
p=pathlib.Path(sys.argv[1])
if p.stat().st_size>65536: raise ValueError('saved request exceeds oracle bound')
d=yaml.safe_load(p.read_text(encoding='utf-8'))
assert d.get('name')=='Reviewed Saved Request', 'wrong saved name'
assert d.get('method','GET')=='GET', 'wrong saved method'
assert d.get('url')==sys.argv[2], 'wrong saved URL'
assert d.get('options',{}).get('follow_redirects',False)==False, 'wrong redirect option'
assert d.get('options',{}).get('timeout',3.0)==3.0, 'wrong timeout'
assert sorted(x.name for x in p.parent.glob('*.posting.yaml'))==[p.name], 'unexpected saved request files'
`

func verifySavedRequest(python, path, expectedURL string) error {
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()
	command := exec.CommandContext(ctx, python, "-c", savedRequestOracle, path, expectedURL)
	if output, err := command.CombinedOutput(); err != nil {
		return fmt.Errorf("saved request state: %w: %s", err, output)
	}
	return nil
}

func fail(format string, values ...any) {
	fmt.Fprintf(os.Stderr, "PLAYTESTR-POST-ORACLE FAIL: "+format+"\n", values...)
	os.Exit(90)
}
