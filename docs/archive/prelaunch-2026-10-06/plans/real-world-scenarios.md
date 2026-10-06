> ARCHIVED on 6 October 2026. Historical context only; do not execute this plan. The [current roadmap](../../../../roadmap.md) supersedes its scheduling, gates, and scope.

# Real-world scenario and maintenance protocol

Planned 26 September 2026 for E1–E5. No rows below are new support claims or executed results. Existing [corpus](../../../../corpus/README.md) and [qualified host table](../../../qualified-compatibility-v0.4.0-rc.1.md) remain the baseline. This protocol adds realistic depth and change over time instead of replacing the corpus with a leaderboard.

## Admission and independent expected results

A journey represents a useful maintainer task with multiple interactions, a persisted result where applicable, a failure and recovery story, and a reason it needs real PTY coverage. Record exact app/runtime/runner pins, geometry, locale, fixture hashes, safe working directory, expected state, public/private evidence boundary, cleanup and host prerequisites.

Review the expected outcome before recording the baseline. Do not derive the oracle by copying the tool's own screen output. File bytes, Git index/tree, database queries and local server request logs should be checked independently at the right lifecycle point, before a successful temporary workspace is deleted. Retain evidence outside the owned workspace. A wrong oracle must itself fail a control.

Use trusted disposable targets only. Local requests and synthetic fixtures replace real accounts, credentials, cloud clusters and destructive administration. Do not weaken a meaningful task solely to fit Playtestr's current input surface: record inaccessible actions as gaps.

## Six primary journeys

Candidate versions start with existing admitted corpus pins; E0 records the actual tested pins and availability. Each journey needs two supported native hosts, and the admitted set must include Windows amd64, Linux amd64 and macOS arm64. This is a selection target, not a portability assumption.

| ID | Candidate real task | Independent proof and intended defect | Variation / practical value |
| --- | --- | --- | --- |
| RW1 | Lazygit: stage one of several files, inspect diff, commit or cancel | Exact index/tree and commit content; mutation displays selected file but stages the wrong file | Distracting neighboring changes, resize, upgrade; catches costly screen/state disagreement |
| RW2 | micro: edit UTF-8 file, save, reopen and undo/cancel another edit | Exact saved bytes and untouched neighbor; mutation reports save but drops/reorders data | Spaces/multilingual names, narrow viewport, delayed writes; preserves actual user work |
| RW3 | create-vite: invalid name, correct choice, scaffold, refuse overwrite | Exact package fields/file tree and untouched existing marker; mutation reports success with wrong template/config | Fresh home/temp, existing directory, changed prompt wording; realistic onboarding/maintenance |
| RW4 | fzf: filter similarly named records, move selection, accept/cancel | Exact chosen record and status; mutation selects a plausible wrong record | Wide/combining text, empty result, geometry and locale; probes input/fidelity beyond ASCII |
| RW5 | litecli: modify disposable SQLite state, inspect, rollback/correct | Independent database query and transaction invariants; mutation displays success without correct persistence | Existing history, validation error, longer output and upgrade; no remote database |
| RW6 | Posting: edit/save request and send to local deterministic server | Exact request method/path/body and saved collection; mutation retains old field despite edited display | Repeated edit, modal/resize and slow local response; no external network dependency |

These mutations are experiment designs, not claims that upstream has those bugs. First prefer a pinned historical buggy/fixed pair; otherwise use a small reviewed target-source patch in a disposable fork/build. Keep licenses and patch provenance. If target mutation cost is excessive, substitute a distinct accessible task before optimization and explain why. Replacing a baseline or deliberately invalidating a spec is useful harness validation but does not satisfy target-defect coverage.

Keep useful existing BT-06 redraw/cancellation, Gum and process-lifecycle cases as regression controls. The six journeys need not create 48 new specs; reuse a spec where its actual user task and oracle match. Counts reflect distinct tasks, not hosts, data variations or repeats.

## Two held-out journeys

At E0 freeze HO1 GitUI stage/unstage with independent Git state and HO2 television filter/select with exact selected-record output, or documented substitutes if unavailable. Keep their scenarios, expected outcomes and mutation definitions reviewable, but do not use their runtime results to tune E2/E3 changes. They are held out from optimization, not new projects claimed as independent users.

Run at E5 on at least one native supported host each, good/defect/recovery plus five fresh good attempts. The same maintainer designing them limits independence; state that explicitly. If used to diagnose a fix, retain the failed first result and label the journey no longer held out. At most one replacement cycle prevents unlimited shopping for passing tasks.

## Variation without a combinatorial explosion

Baseline all primary-host cells first. Then select one risk-driven variation per primary journey, plus a second variation for RW1 and RW2. Freeze the eight assignments before running; report separate cells and first outcomes. Avoid an unexplained all-pairs matrix.

| Variation | Controlled experiment | Acceptance |
| --- | --- | --- |
| Fresh and reused environment | New workspace/home/temp versus a reviewed harmless existing configuration | Same intended state or explicitly different expected behavior; no host contamination |
| Slow target / busy host | Bounded deliberate target delay or recorded CPU contention | Condition waits remain correct; finite timeout category and cleanup if budget exceeded |
| Data and locale | Distracting entries, spaces, basic/wide/combining text with fixed locale | Correct selection/state; unsupported cell layout surfaced rather than silently normalized |
| Resize and redraw | Repeated shrink/grow, modal dismissal, output between input events | Correct final state and meaningful fresh readiness |
| Failure after partial progress | Cancel, wrong exit, local service interruption or save failure | Original and partial state accounted for; cleanup and evidence accurate |
| Long serial work | Mix short/stateful/redraw journeys in a 50-spec suite | No survivor/state leakage, unexplained memory trend or loss of failure evidence |

An intentionally induced target timeout is a successful harness control only when Playtestr records the expected non-pass result. Never rewrite the original product report as passed. Repeat diagnostic attempts are labeled separately and cannot replace the first failure.

## Maintenance and upgrades

For at least three primary journeys, freeze spec, fixture, baseline and oracle, then try a later available target version. Keep runner fixed to isolate target change. Separately change runner with target fixed when testing a runner upgrade. Do not change both and guess which caused a failure.

Record whether the original test passes, detects a real regression, needs a legitimate reviewed expectation change, or breaks due to selectors/format/timing. Measure human minutes, changed lines/files, baseline churn, helpers and required knowledge. Use a behavior-preserving label/layout change and a behavior-changing defect as separate controls: reducing maintenance must not hide the latter. “No newer package available” stays unavailable; a synthetic change is not a real version upgrade.

Before claiming supported target upgrades, run good/defect/recovery at the new pin and update the host table. One app's successful upgrade does not qualify a framework or future release family. Two weeks of internally scheduled reruns may expose drift but still do not count as user retention.

## Comparative use

After correctness controls, compare at least RW1 and one of RW3/RW6 with the strongest applicable alternative using the [comparison protocol](competitive-benchmark.md). Freeze task, geometry, state, defect and oracle. Permit idiomatic assertions and helpers for every tool; count installation, runtime, cleanup, diagnosis and maintenance work. Do not require identical syntax or impose our report format on competitors.

Unsupported is a visible suitability result, not a fast runtime or invented failure. A different process/session model must include the resources needed to finish the same user job. Document a framework-native unit test as a complementary control when possible, separately from real-process timing. One useful extra regression caught by E2E matters more than winning against an irrelevant baseline.

## Evidence and decision sheet

For every journey/cell record: user task; reason PTY is needed; identities; host; baseline/fixture/oracle review; exact command; first-attempt result; defect provenance; intended versus observed failure step/category; state before/after; cleanup/survivor proof; wall/CPU/memory where measurable; setup/authoring/maintenance/diagnosis effort; artifact location; exclusions; reviewer; next decision.

Classify tool defects, target defects, bad test/oracle, setup failure and external-host failure separately. Any unclassified result remains open. Summarize real task success, intended bug detection, false passes, false failures, unsupported cells and maintenance burden with denominators. Do not compress them into a weighted score that allows speed to cancel out a false pass.

E1 closes only on the admitted primary scope; E5 includes held-out results and the final bytes. An attractive benchmark with an unexplained failure on these real tasks does not pass readiness.
