# Candidate operator rehearsal

These source recipes are for the unpublished engineering candidate. Public
archives still install their named published version. No candidate download
URL or independent human first-use timing is claimed.

Use a source checkout and Go 1.26.0, Git, Python 3.12, Node 24.7.0, and the
reviewed corpus target tools. Linux/macOS preparation is documented and executed
by `python scripts/readiness/setup-native.py`: it pins sources, builds targets
and independent state oracles, checks the create-vite package hash and prepares
the reviewed target-code negatives. Windows uses the installed pinned corpus
tools from the corpus admission recipes; inspect their hashes before reusing
them. Target installation is a prerequisite, separate from runner installation.

From the repository root on Windows:

```powershell
go build -trimpath -o bin/playtestr.exe ./cmd/playtestr
python scripts/readiness/e4-prepare.py
python scripts/readiness/e4-walkthroughs.py --runner bin/playtestr.exe
```

On Unix use `bin/playtestr` instead of `bin/playtestr.exe`. Use a fresh checkout
or fresh evidence directory for every rehearsal; scripts refuse overwriting
attempt ledgers. These commands do not execute GitUI or television holdouts.

The four generated directories are selector (`fzf`), stateful wizard
(`create-vite`), editor (`micro`) and repository tool (`lazygit`). Each includes
copied reviewed fixtures, the original good and bad spec, two separately labeled
synthetic maintenance changes, first unmodified-spec failures, repaired specs,
state-sensitive defect checks and unchanged-spec recoveries. Run any generated
spec directly using the candidate binary and
`test --artifacts-dir evidence --report results.json SPEC` from its directory.
No test requires launching the target manually or guessing a readiness delay.

For a reviewed screen baseline, run the generated `baseline.json` with
`test --update`, inspect `snapshots/e4-reviewed.txt`, then rerun without
`--update`. Baseline updates happen only in the disposable walkthrough directory;
the original corpus baselines remain unchanged. This operator-reviewed synthetic
baseline rehearsal does not claim a real upstream upgrade or blinded usability.

Keep evidence references relative: absolute artifact directories intentionally
cannot be exported by the offline renderer. From the same invocation directory,
run `playtestr report --input results.json --evidence-root . --output report.html`.

Inspect failure category, first failed step, actual screen/diff, independent
oracle marker and cleanup separately. A correctly detected injected target defect
still has a nonzero product result. The walkthrough ledger records tool wall time
and helper/fixture identities; human authoring and diagnosis minutes are unknown.
