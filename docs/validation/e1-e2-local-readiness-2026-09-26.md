# E1 local correctness and E2 diagnostic work — 26 September 2026

Status: **E1 partial; E2 partial and not accepted.** E0 is complete at its audit
boundary. Six Windows core tasks have discovery controls; required second native
hosts, remaining variation/maintenance measurements and matched comparisons are
still missing. No E3–E5 execution, publication, push or outreach occurred.

This is operator self-review, not independent use. The unchanged qualified
Windows runner hash is `7a73b598613d34e8a05831d12f2ab26d4abae3e6ce05e63c7d80c316bcc80fc2`.
Changed **test helpers, fixtures and specs** do not change that runner binary,
but do invalidate reuse of the old task/oracle controls. Current-source tests
use Go 1.27.0 Windows amd64 separately. The runner itself was not optimized.

## What changed and why

- Lazygit now has a `stage-neighbor` oracle: alpha's exact staged bytes, beta's
  exact unstaged bytes, unchanged HEAD and exact index/worktree path lists.
- litecli has a transaction journey with rollback and commit. An independent
  SQLite connection checks all final rows. The new synthetic target-source patch
  preserves row-count/status success while writing `wrong` instead of `three`.
- Posting independently reads bounded persisted YAML before workspace deletion,
  checks request name/method/URL/options and the collection's request-file set,
  and also checks the local server's exact method/path/body. A real target-source
  patch writes a stale URL while retaining successful save/send feedback.
- POST-05 waits for **Request saved**, replacing a stale **Saved** match in the
  existing request name. Five independent-reader tests cover correct state,
  serializer defaults, wrong name, wrong URL and missing file.
- Reproducible audit/discovery/maintenance/serial/Termless scripts retain initial
  reports and refuse to overwrite campaign directories. New `.control` files
  do not inflate the 120-workflow corpus denominator.

The new state mutations are synthetic, not upstream defects. Exact source
anchors and before/after hashes are enforced by
[`prepare-state-mutations.ps1`](../../scripts/readiness/prepare-state-mutations.ps1).
Posting collection source: `54130864af979db95c1d1af18133ca3a437fe2f7e60d3375630d9b878cab9bbb`
→ `2d5aa43f09bdd86b286cc9a23a3ecb00bd3750fbd57861bf8b723c445da45a41`.
litecli executor: `649d63bda90ffa7844410cf267302f20c9fb1b204f036497b6e255c0b11826ce`
→ `f18d7cad34cea9cf90d285b38085b846503b8e872d952f4598eedbe4194c9fee`.

## Six Windows core task outcomes

The final executable-code cohort combines 35 non-RW3 attempts from
`discovery-final-local` with seven RW3 attempts from `discovery-rw3-exact-final`.
The latter rebuilt the oracle after the final bounded-read/directory-set change.
It recorded five fresh good attempts, one target defect
and one unchanged-step/oracle recovery per task: **30 good + 6 intended negative
+ 6 recovered**. All 42 returned the intended exit; all reported process exit
and cleaned workspaces. No selected-image PID appeared in its immediate post-run
census. This census covers named target images, not every possible descendant.

| Task | Useful result / independent proof | Good / defect / recovery |
| --- | --- | --- |
| RW1 Lazygit | Explicitly select alpha among two changes; exact staged alpha and unstaged beta bytes | 5 pass / `unexpected_exit` at oracle, target wrapper 1 / pass |
| RW2 micro | Save, reopen, discard a second edit and verify exact document/neighbor bytes; synthetic save corruption | 5 pass / `unexpected_exit`, oracle 90 / pass |
| RW3 create-vite | Correct invalid package name, choose vanilla JavaScript, decline install; exact reviewed 11-file tree, directory set and every JSON field; executable JavaScript writes wrong package type | 5 pass / `unexpected_exit`, oracle 90 / pass |
| RW4 fzf | Filter similar records and accept exact reviewed final output; source returns wrong record | 5 pass / `snapshot_mismatch` / pass |
| RW5 litecli | Roll back one insert, commit another, verify all independent database rows; synthetic wrong persisted value | 5 pass / `unexpected_exit`, oracle 90 / pass |
| RW6 Posting | Edit URL path, save, send; exact local request and independently saved YAML; synthetic stale saved URL | 5 pass / `unexpected_exit`, oracle 90 / pass |

Earlier CV template-data negatives remain changed-input evidence and are excluded
from the executable-code cohort. The new CV patch changes `dist/index.js` from
`cb74cb790239b5ec7c07e91ba04ed1ef41a4eb130eb12cdd040179e5ed55838a` to
`23ca944a09883a99b5ea3006621a08c626eb8e85719896b5e3fbb0a6307db1f0`.
Six scaffold-oracle regression cases cover reviewed output, missing asset, extra
file, extra empty directory, corrupt counter and wrong preview configuration.

MICRO/CV/LITE/POST demonstrate plausible success with incorrect persisted state,
not baseline or expectation mutations. FZF's reviewed final-output snapshot is
the selected-result check; a separate redirected-result file oracle is still a
stronger follow-up. No safe historical buggy/fixed pair was admitted; reviewed
synthetic patches substitute and are labeled throughout.

The durable [attempt ledger](e1-local-attempts-2026-09-26.json) preserves earlier
discovery phases too; the 42-row state-oracle revision is separate from the
42-row preliminary corpus revision. They are not 84 distinct tasks. Raw reports,
screens, logs and source/fixture/binary pins remain under
`artifacts/readiness-2026-09-26`; [identity hashes](e1-e2-input-identities-2026-09-26.json)
pin the principal raw inputs. Ignored raw evidence is local, not a committed
portable artifact archive. Missing files after checkout remain missing prerequisites.

## First failures retained and disposition

| First observation | Disposition / evidence |
| --- | --- |
| Discovery stopped on expected LG defect stderr | PowerShell `ErrorActionPreference=Stop` aborted ledger writing. Product failure report remains under `discovery/RW1-defect.json`; five preceding good attempts remain. Corrected harness records expected stderr; new campaign is labeled `discovery-harness-repaired`, not a replaced first run |
| Two-change LG spec staged alpha and beta | Bad selection spec: Space acted on root row. Git oracle rejected both staged paths. `rw1-neighbor-first.json` retained; explicit ArrowDown to alpha passes. This is not a runner fix |
| POST save-source defect first passed | Old `Saved` readiness matched request name before target save; the mutation never reached serialization. `post05-save-defect.json` retained. Fresh `Request saved` readiness reaches the write and the independent oracle rejects stale URL |
| POST query edit looked changed but server saw `/saved` | `rw6-edit-save-send-first.json` retained. Query-table/input commit semantics not isolated; do not call this a confirmed runner/upstream bug. Path edit is a documented useful-task substitution and succeeds. Query editing stays an open reduced-task investigation |
| Maintenance POST “defect” passed | Generated spec omitted `PLAYTESTR_POSTING_SAVE_MUTATION` because a PowerShell hashtable note property was not serialized. This was a good-target run, invalid mutation evidence. Original ledger remains; corrected spec fails at oracle and subsequent unchanged maintained recovery passes |
| Preliminary selected-image census saw transient PIDs in three attempts | PIDs 38916, 32440, 41072, 13200, 37576, 46968 were absent in the later diagnostic census. Ownership and duration were not established, so neither managed-survivor nor guaranteed-zero-survivor claim follows. State-oracle revision had zero sampled new selected-image PIDs; runner Job Object cleanup was confirmed |

Historical CV-02 workspace cleanup deadline failure and Posting startup/resource
timeouts remain separately open causal investigations; this run does not erase
them or prove host-resource causation.

## Variations and maintenance

The ten-spec variation suite passed **10/10**: neighboring-file resize/stage,
spaced micro filename, unsaved close cancellation, basic Unicode save/resize,
create-vite invalid package-name correction and occupied-directory refusal,
fzf Unicode-candidate selection and exact cancel exit 130, SQLite rollback/commit,
and Posting with a bounded 200 ms local response delay. Each state oracle ran
before deletion. Wide-cell/grapheme layout is still outside the advertised contract.

Supplementary variations passed **3/3**: a multilingual filename with reviewed
existing editor configuration, fixed-locale combining-text selection and local
HTTP connection interruption. A later `settings.seed` bootstrap revision passed
separately. The final micro journey saves, reopens and discards a second edit.
Its first reopen attempt timed out when input reached the exiting child's buffer;
a positive acknowledgement barrier and cleared-marker assertion repaired the
transition. Initial and repaired reports remain. Reviewed configuration seeding
does not prove arbitrary retained user homes. Wider terminal-cell probes, fresh
native lanes and active human effort measurements remain open.

Three **synthetic realistic UI changes**, not real upstream version upgrades:

| Journey | Change and first unchanged-expectation result | Maintenance edits | Meaningful defect retained? |
| --- | --- | --- | --- |
| micro | `document.txt` → `draft notes.txt`; old Saved assertion timed out | Target argument, Saved expectation, fixture filename and six oracle path-key updates; helper algorithm unchanged | Yes, corrupt saved bytes rejected; recovery pass |
| create-vite | Select → Choose in two prompts; old readiness timed out | Two expectation strings; clone good/bad runtimes and keep exact state oracle | Yes, template-data commonjs change rejected; recovery pass (executable-code discovery separate) |
| Posting | Request saved → Request stored toast; old readiness timed out | One expectation string plus helper variant selection and separate good/state-bad source copies | Corrected diagnostic detects stale persisted URL; recovery pass; first invalid negative retained |

No snapshot baseline changed in these exercises. Good/bad target behavior remains
separate from changed UI wording. Authored `.control` files and helpers are all
countable in source. **Active human minutes were not instrumented** and remain
unknown; execution durations in the ledger are not authoring times. Fixture-driven
filename/status changes and source wording patches do not prove future upgrades.

## Serial suite correctness and resources

One first attempt per size, with repeated valid tasks from RW1 resize, micro
Unicode save, CV invalid-name correction, SQLite transaction and Posting delay:

| Size | Outcome | Whole command | Report/evidence bytes | Cleanup unconfirmed |
| --- | --- | ---: | ---: | ---: |
| 1 | 1/1 pass | 2,641 ms | 2,997 | 0 |
| 10 | 10/10 pass | 22,969 ms | 31,222 | 0 |
| 50 | 50/50 pass | 112,991 ms | 155,276 | 0 |

These are **single E1 correctness observations**, not the required 30-observation
E2 performance cells. Repeated tasks are not new workflows. Independent state
checks and successful workspace deletion found no task-state leakage. No
process-tree CPU/RSS sampling or memory trend was instrumented; those are unknown.
Size 1 uses only the first composition member, so no naive scaling comparison is
made. No descriptive p95 or performance improvement is reported.

## E2 diagnostic findings and remaining gate

Current-source native Windows trace command:

```powershell
go test -count=1 -run '^(TestSnapshotBaselineAndReadableMismatch|TestSnapshotSettlesAfterExplicitReadiness|TestChildProcessCleanup)$' -trace artifacts/readiness-2026-09-26/runner.trace ./internal/runner
go tool trace -pprof=sync artifacts/readiness-2026-09-26/runner.trace
```

The traced tests passed in 8.625 s. The synchronization profile shows cumulative
blocked spans in `executeStep`, process wait, final drain and stop. Its **41.76 s
sum overlaps across goroutines**, exceeds whole-test wall time, and includes
testing/runtime instrumentation. It is not a phase decomposition or runner
overhead. Final drain contributes 0.74 s and stop 0.30 s cumulatively across this
selected test set; neither is a per-command tax or proof of the historical
Linux speed gap. Instrumentation overhead has not been qualified. The cause of
the comparable runtime deficit remains inconclusive; no safeguard was shortened
and no candidate optimization or before/after win is claimed.

Termless feasibility used Node 24.7.0, npm 11.5.1, `@termless/core`/`xtermjs`
0.9.1 and `node-pty` 1.1.0. Package-lock SHA-256 is
`aef02bc4f7c09a60dac3b68da4d9b722c17c3050399436106cf3efb7a34261cb`.
The [project-owned README](https://github.com/beorn/termless/blob/main/README.md)
documents the real-process API and Node PTY prerequisite; the installed package
types/source were read to match the actual release API. Current remote main
`46e84504317f6cedaae20831bb4da2945ca0abcc` is context, not the npm distribution hash.

Initial setup without a local npm manifest selected an ancestor project and
failed on an unrelated missing local tarball. Initial `--omit=optional` install
then failed import on `ghostty-web`; neither is scored as a competitor runtime
loss. Explicit local project initialization and the normal optional dependencies
repaired setup. No browser binary or paid service was installed.

The real menu spawned through Termless/node-pty, rendered fresh readiness,
accepted ArrowDown/Enter, showed diagnostics and exited `exit=0`. After the
adapter's result and `close`, node-pty's console helper emitted **AttachConsole
failed** from `conpty_console_list_agent.js:13`. Overall Node exit was 0, but
cleanup is not qualified. Preserve that stderr independently of the adapter's
task-pass JSON. This is feasibility evidence only, not a performance ranking,
tree-cleanup pass or invented unsupported-tool failure. It needs a bounded
cleanup diagnostic before admission to a matched comparison.

Historical Linux loss remains 295–305 ms vs 49–54 ms on C1–C3. No refreshed
direction, binary acquisition/extraction parity, 30-attempt counterbalanced
baseline/candidate data, two real-task alternative comparisons or process-tree
resource baseline has been completed. Those acceptance gates remain open.

## Reproduction and verification

Existing exact corpus targets and the qualified extracted Windows binary are
prerequisites; hash-check them before use. New mutation preparations reject a
changed source/existing output. The recorded runner is not a new release build.

```powershell
$env:GOCACHE = Join-Path (Get-Location) '.cache/readiness-go'
go build -C corpus/controls/lazygit-oracle -o ../../../.trial-private/corpus-tools/lazygit-oracle.exe .
go build -C corpus/controls/micro-oracle -o ../../../.trial-private/corpus-tools/micro-oracle.exe .
go build -C corpus/controls/create-vite-oracle -o ../../../.trial-private/corpus-tools/create-vite-oracle.exe .
go build -C corpus/controls/litecli-oracle -o ../../../.trial-private/corpus-tools/litecli-oracle.exe .
go build -C corpus/controls/posting-oracle -o ../../../.trial-private/corpus-tools/posting-oracle.exe .
powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts/readiness/prepare-state-mutations.ps1
powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts/readiness/prepare-ui-variants.ps1
powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts/readiness/run-discovery.ps1 -Output artifacts/readiness-reproduction/discovery
powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts/readiness/run-maintenance.ps1 -Output artifacts/readiness-reproduction/maintenance
powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts/readiness/run-serial.ps1 -Output artifacts/readiness-reproduction/serial
```

Termless installation must start in an initialized private local directory:

```powershell
# In .trial-private/readiness-termless, create package.json with private:true.
Copy-Item ../../scripts/readiness/termless-package-lock.json package-lock.json
# package.json must match the lock root package and pinned dependencies.
npm.cmd ci --prefix . --no-audit --no-fund
# From repository root:
go build -o bin/demo.exe ./cmd/demo
node scripts/readiness/termless-feasibility.mjs artifacts/readiness-reproduction/termless.json
```

Verification: changed Go formatted; root uncached tests and vet; separate nested
oracle tests/vet (root `./...` does not traverse their modules); root Windows race
script using project-local GCC and nested Posting oracle race tests; manual menu
and menu-exit **2/2 specs, 12/12 steps**. Race-built micro and Posting
helpers passed real reopen and delayed-HTTP journeys **2/2** in
`helper-race-integration-diagnostic.json`. The first build placed `-C` after
`-race`, which Go rejects; resulting missing-binary setup failures remain in
`helper-race-integration.json` as operator prerequisite errors. Corrected builds
put `-C` first. This is separate from the root race check. Root lifecycle tests cover unexpected
exit, timeout, cancellation, flood, final output and descendant cleanup using
real PTYs. E0's JSON records skipped Windows symlink/unreadable-directory cases;
they are not passes. A default-cache Go access-denied attempt was retained and
repaired with project-local GOCACHE. A later build printed a module stat-cache
write warning; command results do not imply that external cache was writable.

## Acceptance decision and exact next work

E1: six local core task cells controlled; **6/12 required native discovery cells**
represented, zero fresh Linux/macOS cells. Historical native results do not close
the changed journeys. Maintenance timing, arbitrary retained user homes and broader probes
remain explicit shortfalls. GitUI and television have not been freshly run.

E2: frozen measurement design, selected trace and Termless feasibility only.
No accepted optimization, matched comparison or resource trend. Finish E1 native
lanes, reduce Posting query semantics, then execute pinned native Linux C1–C3 and
RW1/RW3 comparisons with complete setup/oracle/cleanup glue and 30 fresh attempts.
No configured native execution endpoint is available here, and remote runtime
mutations are outside the read-only remote authorization.

The exact later **E3 task**, after E1/E2 gates, is to probe fixed-locale fzf
wide/combining filenames beside selection and repeated shrink/grow, compare
independently justified terminal cells and exact selected output, and reduce
one valuable failing family before choosing a fix or explicit support boundary.
E3 is not started by this record.

## Continuation after conditional push authorization

The user requested continued E0-E2 work and a push only after completion, then
confirmed that no native SSH/execution endpoint is available. E1's six missing
native cells therefore remain externally blocked. Neither WSL nor containers
substitute for the frozen native-host requirement. No push was performed.

A new bounded Windows measurement harness retains the process handle for exact
exit codes, samples the observed parent/descendant chain through process IDs and
creation timestamps, and stores CPU/RSS counters without command lines or
environment values. Short-lived children can escape sampling: CPU and peak RSS
are lower bounds, and zero observed survivors is not a complete tree guarantee.
The 100 ms field is a requested sleep between reads; CIM inventory and counter
reads add variable time. Instrumentation overhead remains unqualified.

Thirty handle-corrected size-1 observations all passed with exact runner exit 0 and
confirmed cleanup. The initial 30-record harness lost exit codes after process
termination; those observations are retained but excluded from exit-qualified
measurement. A tree pilot also exposed a PowerShell dictionary aggregation error,
which was corrected before the campaign. A stale parent PID then attributed
a pre-existing ASUS utility to the runner in one sample; this is a harness
ownership error, not runner-survivor evidence. A child-creation-after-parent guard
was added and a separate fresh 30-observation revision retained. The affected
original tree statistics are excluded. Size-10/50 resource diagnostics
remain single observations, not 30-sample suite cells. See [continuation measurements](e2-windows-continuation-2026-09-26.json) for exact medians and ranges. Host activity was not isolated, so these are
instrumented diagnostics rather than an accepted performance comparison.

A reduced node-pty experiment distinguishes natural target exit from adapter
termination. The first no-kill experiment left Node alive and was explicitly
stopped by identified process tree. The bounded revision returned diagnostic
exit 2 at 10 seconds with Socket/MessagePort handles. Calling kill after the same
positive natural exit returned Node exit 0 but reproduced AttachConsole failed.
Installed Termless 0.9.1 close calls closePty, whose node-pty implementation calls
destroy/kill after exit; node-pty 1.1.0 then queries the exited console. This
source path plus reduced reproduction supports a redundant post-exit cleanup explanation,
but does not prove safe cleanup for arbitrary child trees or justify suppressing
stderr. No competitor sources were patched and no upstream issue was published.

Reproduction:

```powershell
# Windows process inventory access is required. Use a fresh output directory.
& scripts/readiness/run-windows-measurements.ps1 -Output artifacts/readiness-reproduction/windows-short -Samples 30 -Sizes @(1) -ObserveTree
& scripts/readiness/run-windows-measurements.ps1 -Output artifacts/readiness-reproduction/windows-suites -Samples 1 -Sizes @(10,50) -ObserveTree
node scripts/readiness/node-pty-natural-exit.mjs
node scripts/readiness/node-pty-natural-exit.mjs --kill-after-exit
```

E0 remains complete. E1 and E2 remain unaccepted: missing native cells, active
human maintenance times, matched alternatives/setup parity, instrumentation
qualification, repeated larger-suite resources and a justified optimization or
accepted causal explanation still prevent completion. Conditional authorization
to push does not waive these gates. E3-E5 remain unstarted.
