# Frozen E1/E2 experiment revision 1 — 26 September 2026

Frozen before E1 runs and optimization; owner/reviewer: same operator (self-review).
Runner for local correctness: qualified Windows `v0.4.0-rc.1`, executable SHA-256
`7a73b598613d34e8a05831d12f2ab26d4abae3e6ce05e63c7d80c316bcc80fc2`,
under `artifacts/qualified candidate extracted`. Keep this runner fixed for
target/harness maintenance. Current-source Go 1.27.0 Windows tests are separate.
Targets start with corpus manifest/result pins. Exact local binaries, specs,
fixtures and changed source hashes must be recorded for every campaign revision.

## Admission and host cells

| ID | Task, candidate and existing input | Oracle / defect | Native cells |
| --- | --- | --- | --- |
| RW1 | Lazygit 0.65.0 `c07f4d381b90419583b7ce04f87379654d983ebc`; LG-01 selection/staging | Index path and exact staged bytes; changed beta remains unstaged; synthetic StageFiles skips add | Windows available; Linux required/unavailable |
| RW2 | micro 2.0.14 `04c577049ca898f097cd6a2dae69af0b4d4493e1`; MICRO-01 edit/save plus reopen/cancel | Exact document/neighbor bytes; existing synthetic save corruption | Windows available; macOS required/unavailable |
| RW3 | create-vite 9.2.1, tarball `4dd92d0e734e96e88ec8afd8c0153f6a9446156205460a995b978b63b49b4eb8`; CV-01 with invalid/overwrite boundary companions | Package fields, tree, unchanged marker; synthetic module type corruption | Windows available; Linux required/unavailable |
| RW4 | fzf 0.74.4 `a140afeb4d733cad3c96a56bf6db7e26853b6757`; FZF-01 filter/select | Exact selected record/status captured independently of selection UI; synthetic wrong record | Windows available; Linux required/unavailable |
| RW5 | litecli 1.17.1; insert with transaction/rollback companion | Independent SQLite connection checks all rows; existing status mutation is preliminary only; persistence defect required | Windows available; Linux required/unavailable |
| RW6 | Posting 2.10.0; edit/save/send local request | Exact YAML state and local server method/path/body; existing response mutation preliminary only; persistence defect required | Windows available; macOS required/unavailable |

Availability is not admission. No lane is accepted until five fresh good attempts
and intended defect/recovery reach the reviewed state oracle and cleanup. No WSL
substitution for native cells. This environment exposes Windows only; no native
Linux/macOS execution endpoint is configured. Historic qualification is reusable
only for its original task/bytes, not these changed journeys.

Expected state is reviewed from fixture bytes and oracle source before snapshots.
All state checks run after target exit and before successful workspace deletion.
No screen-only persistence proof. Wrong expected-state controls must fail too.
Target patches are synthetic; no safe historical buggy/fixed pair is admitted
yet. Six target defects required, including at least two plausible screen successes
with wrong persisted state. Existing MICRO/CV patches meet that design; POST/LITE
need state-specific controls. Changes invalidate the affected cell's controls.

## Holdouts

HO1: GitUI 0.28.1, GUI stage/unstage with exact index/worktree bytes; synthetic
staging patch. HO2: television 0.15.9, TV filter/select exact candidate output;
synthetic wrong selection. Freeze corpus inputs as definitions only. No fresh
holdout execution, oracle result or comparison outcome may tune E1/E2. Their
historical presence is acknowledged; operator-designed holdouts are not blind
independent validation. First new holdout execution is E5, outside current scope.

## Eight variation assignments

RW1: distracting beta change; resize/help then stage. RW2: UTF-8/spaced filename;
unsaved second edit/cancel. RW3: pre-existing occupied directory/refuse overwrite.
RW4: similar names plus fixed Unicode/locale candidates. RW5: explicit transaction
rollback after partial progress. RW6: second edit plus bounded local response delay.
All suites also compare fresh versus reviewed reused state and serial order;
do not multiply counts into new workflows. Record inaccessible input or cell-width
behavior without normalizing it away. Budgets retain existing 8–15 s step,
30 s run and 1–10 MB output limits; one bounded failure remains failure.

Maintenance assignments: micro behavior-preserving file/status label change;
create-vite prompt change; Posting saved request name/path change. Prefer later
real pinned versions when available; label synthetic UI changes separately.
Freeze runner and original tests first; report first attempt, edited files/lines,
helpers, baseline churn and active engineering minutes. Do not invent time.
Each maintenance case still requires unchanged meaningful defect detection.

## E2 comparison and measurement freeze

Historical C1–C3 pins remain Atago 0.23.0, tui-test 0.1.0-beta.5, Termlens 0.11.2,
Rust 1.85.0, Playtestr `f1ab948`. Refresh is a separate revision, not a rolling
latest comparison. Reproduce direction on native Linux with the committed
idiomatic adapters. RW1 and RW3 are primary real comparisons with Atago first;
evaluate whether Termlens is stronger on the exact task, keeping its full glue.
Termless real-PTY feasibility: one maintainer day maximum; package/docs pin must
be frozen before execution. In-memory timings cannot enter the E2E ranking.

Measurements: monotonic whole-command wall time; acquisition, extraction,
dependency setup and target setup timed separately; startup/readiness/evidence/
cleanup phases only with non-overlapping instrumentation. First-step waits and
outside-run residuals are labeled literally. Profile the measured bottleneck;
validate instrumentation against uninstrumented runs. No overhead subtraction
without a defensible phase boundary. No candidate until evidence supports a change.

Thirty fresh observations per exploratory cell, counterbalanced baseline/candidate
order on identical host/toolchain/targets/fixtures. Report median/min/max, outliers
and every failure; p95 only with at least 100 observations per selected cell.
Serial suites 1/10/50 use valid repeated primary workflows and record artifact
bytes, exact state, survivors, CPU/RSS and memory trends where measurable.
Unknown resource data remains unknown. Target ≥30% improvement; aim within 20%
or 50 ms of fastest comparable short-task median; investigate real-suite losses
exceeding both 10% and 100 ms. Safeguards and semantics remain fixed.

Compute ceiling: six native runner-hours and 1 GiB compressed retained evidence
per exploratory campaign after two pilot cells. Missing hosts block affected
experiments; complete local independent work. No paid service or workflow dispatch
is implied, and no push/release/issue/PR/contact is authorized.

## Dated local execution revision

On 26 September, local tasks gained a micro reopen acknowledgement barrier,
an exact reviewed create-vite scaffold tree and a genuine JavaScript code defect.
These replace incomplete or ambiguous local controls before any optimization.
Earlier reports remain separate revisions, including the template-data negative.
Supplementary reviewed-config, combining-locale and service-interruption probes
were recorded separately. No performance threshold or native requirement changed.
