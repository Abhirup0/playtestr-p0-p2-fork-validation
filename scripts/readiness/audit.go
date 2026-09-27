// Command audit inventories E0 evidence without equating mappings with executions.
package main

import (
	"bufio"
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"flag"
	"fmt"
	"go/ast"
	"go/parser"
	"go/token"
	"os"
	"path/filepath"
	"sort"
	"strings"
)

type mapping struct {
	Reference       string            `json:"reference"`
	Rows            []string          `json:"mapped_rows"`
	Risks           []string          `json:"mapped_risks"`
	Layers          []string          `json:"labels_not_execution"`
	Found           bool              `json:"source_anchor_found"`
	LiteralSubcases []string          `json:"literal_subcase_names_not_exhaustive"`
	Observed        map[string]string `json:"observed_windows_events,omitempty"`
}

func must(err error) {
	if err != nil {
		panic(err)
	}
}
func main() {
	out := flag.String("out", "", "output JSON")
	events := flag.String("events", "", "optional go test -json output from this host")
	flag.Parse()
	if *out == "" {
		panic("-out is required")
	}
	data, err := os.ReadFile("corpus/risk-map.json")
	must(err)
	var inventory struct {
		Cases []struct{ ID, Risk, Layer, Reference string }
	}
	must(json.Unmarshal(data, &inventory))
	groups := map[string]*mapping{}
	for _, row := range inventory.Cases {
		m := groups[row.Reference]
		if m == nil {
			m = &mapping{Reference: row.Reference}
			groups[row.Reference] = m
		}
		m.Rows = append(m.Rows, row.ID)
		m.Risks = appendUnique(m.Risks, row.Risk)
		m.Layers = appendUnique(m.Layers, row.Layer)
	}
	var result []*mapping
	functions, workflows := 0, 0
	for ref, m := range groups {
		parts := strings.SplitN(ref, "#", 2)
		if len(parts) == 1 {
			_, err := os.Stat(ref)
			m.Found = err == nil
			workflows++
		} else {
			functions++
			file, err := parser.ParseFile(token.NewFileSet(), parts[0], nil, 0)
			must(err)
			for _, decl := range file.Decls {
				f, ok := decl.(*ast.FuncDecl)
				if !ok || f.Name.Name != parts[1] {
					continue
				}
				m.Found = true
				ast.Inspect(f.Body, func(n ast.Node) bool {
					call, ok := n.(*ast.CallExpr)
					if !ok {
						return true
					}
					sel, ok := call.Fun.(*ast.SelectorExpr)
					if !ok || sel.Sel.Name != "Run" || len(call.Args) == 0 {
						return true
					}
					if name, ok := call.Args[0].(*ast.BasicLit); ok && name.Kind == token.STRING {
						m.LiteralSubcases = append(m.LiteralSubcases, name.Value)
					}
					return true
				})
			}
		}
		result = append(result, m)
	}
	sort.Slice(result, func(i, j int) bool { return result[i].Reference < result[j].Reference })
	if *events != "" {
		f, err := os.Open(*events)
		must(err)
		defer f.Close()
		s := bufio.NewScanner(f)
		s.Buffer(make([]byte, 4096), 2<<20)
		for s.Scan() {
			var event struct{ Action, Package, Test string }
			if json.Unmarshal(s.Bytes(), &event) != nil || event.Test == "" {
				continue
			}
			if event.Action != "pass" && event.Action != "fail" && event.Action != "skip" {
				continue
			}
			for ref, m := range groups {
				parts := strings.SplitN(ref, "#", 2)
				if len(parts) != 2 {
					continue
				}
				if !strings.HasSuffix(event.Package, filepath.ToSlash(filepath.Dir(parts[0]))) {
					continue
				}
				if event.Test == parts[1] || strings.HasPrefix(event.Test, parts[1]+"/") {
					if m.Observed == nil {
						m.Observed = map[string]string{}
					}
					m.Observed[event.Test] = event.Action
				}
			}
		}
		must(s.Err())
	}
	identities := map[string]string{}
	for _, pattern := range []string{"corpus/results/*.json", "artifacts/qualification-final-36106092065/*/attempts.jsonl", ".trial-private/competitive-success-35750618644/*.jsonl", ".trial-private/competitive-success-35750618644/versions.txt"} {
		paths, err := filepath.Glob(pattern)
		must(err)
		for _, path := range paths {
			data, err := os.ReadFile(path)
			must(err)
			sum := sha256.Sum256(data)
			identities[filepath.ToSlash(path)] = hex.EncodeToString(sum[:])
		}
	}
	document := map[string]any{"mapped_rows": len(inventory.Cases), "distinct_reference_strings": len(groups), "test_function_anchors": functions, "workflow_anchors": workflows, "mapping_audit": result, "accessible_historical_files_sha256": identities, "subcase_policy": "Literal names are only source inventory. Distinct runtime subcases are observed full test names; table-driven/dynamic cases are counted only from events. Parent events are not additional subcases. Windows events prove only this native path; no row automatically gains a native execution from its label."}
	encoded, err := json.MarshalIndent(document, "", "  ")
	must(err)
	must(os.MkdirAll(filepath.Dir(*out), 0755))
	must(os.WriteFile(*out, append(encoded, '\n'), 0644))
	fmt.Printf("%d mapped rows; %d references (%d test anchors, %d workflow anchors)\n", len(inventory.Cases), len(groups), functions, workflows)
}
func appendUnique(values []string, value string) []string {
	for _, v := range values {
		if v == value {
			return values
		}
	}
	return append(values, value)
}
