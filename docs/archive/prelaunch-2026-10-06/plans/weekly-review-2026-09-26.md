> ARCHIVED on 6 October 2026. Historical context only; do not execute this plan. The [current roadmap](../../../../roadmap.md) supersedes its scheduling, gates, and scope.

# Weekly planning review: 26 September 2026

> Historical planning snapshot. Current accepted E0/E1/E2 status and native measurements are in the [27 September record](../../../validation/e1-e2-native-readiness-2026-09-27.md); the original 0/6 planning denominator below is retained as history.

Status: completed planning pass; no implementation or new runtime campaign. This review changes future priorities, not historical outcomes. The [root roadmap](../roadmap.md) owns current order. Next scheduled planning review: 3 October 2026; this is a written cadence, not an automated task.

## Where we are

The original local-runner MVP is delivered. The subsequent engineering batch is recorded complete through R6-V: suites, offline reports, exact-version installation, fresh workspaces, corpus depth and a published qualified prerelease. We are past the prototype stage. We have not established competitive leadership, independent usability, retention or commercial demand.

| Dimension | Evidence as reviewed | Remaining boundary |
| --- | --- | --- |
| Original MVP, Sprints 0–4 | Implemented and published as stable v0.1.0 | Preserve its contract; stable does not contain all newer capabilities |
| Later batch, Sprints 5–14/R6 | Accepted scope complete through public verification of v0.4.0-rc.1 | S10, S12-B and S6 software branches were deferred, not implemented; newer stable promotion remains a separate decision |
| Application depth | 15 manifest projects and 120 workflow JSON files; dated qualification records their execution | Full depth is Windows-runner evidence, including 16 WSL-target workflows; only ten selected workflows have three-host repetition |
| Focused coverage | 300 risk-map rows, mapping to 41 distinct reference strings in the current file | Not proof of 300 independently executed test functions; audit subcases, duplicated risks and actual test events in E0 |
| Repetition | Dated R6-Q record: ten workflows × 100 attempts × three hosts; zero non-pass first attempts in that campaign | Does not estimate reliability across arbitrary workflows; separate full-depth CV-02/Posting transients remain in history |
| Defect detection | 15 known-bad controls/recoveries in R6-Q; three source mutations in the competitive fixtures | Audit what each control changes; baseline/spec mutations do not prove detection of target bugs |
| Comparison | Four tools, three small owned targets, Linux amd64, 360 fresh executions | All detected selected defects; Playtestr slower; no independent authoring or diagnosis comparison |
| Installation/release | Public-byte/action/upgrade verification on Windows amd64, Linux amd64, macOS arm64 | v0.4.0-rc.1 is a prerelease; new bytes need new qualification |
| Presentation | Deployed route/browser sweep recorded; offline report checks recorded | Interactive human screen-reader session still open |
| Adoption | Cohort records five previously posted invitations, zero responses/consents/qualifying projects | Further outreach held by this review; no independent retention or CI evidence |
| Business | Discovery instruments exist | No demand, payment or unit-economics evidence |

No overall completion percentage is defensible: the previous batch is complete at its accepted boundary, while the newly planned readiness phase has **0/6 milestones complete**. Counting deferred features as delivered or equating 3,000 repetitions with 3,000 different scenarios would mislead.

## What this pass actually checked

Reviewed roadmap, sprint/release plans, qualification/publication/comparison records, compatibility contracts, cohort, manifest, risk map and source wait/cleanup paths. The working tree started clean at `c0f2b72`. Read-only inventory counted 15 projects, 120 workflow JSON files, 300 risk rows and 41 unique reference strings. These counts corroborate repository structure, not fresh execution.

Read current project-owned documentation for the principal alternatives and testing practices; findings and sources are in the [research refresh](../../../research/competitive-refresh-2026-09-26.md). This pass did not install competitors, rerun performance tests, independently re-download historical CI artifacts or recertify public release bytes. Historical execution claims remain attributed to their dated records. E0 explicitly checks evidence retrievability before stronger claims.

Key evidence: [comparison](../../../validation/sprint-13-c-competitive-2026-09-22.md), [frozen qualification](../../../validation/sprint-11-c-r6-q-2026-09-25.md), [public verification](../../../validation/r6-publication-and-blocker-2026-09-25.md), [exact compatibility](../../../qualified-compatibility-v0.4.0-rc.1.md), [cohort](../../../trials/cohort.md).

## Decisions this week

1. Replace immediate recruitment with a finite E0–E5 engineering-readiness phase, as requested. This explicitly supersedes the former instruction to proceed straight from R6 to A1. It does not reopen completed sprints.
2. Aim to lead the complete deterministic regression workflow. Track every important competitive dimension separately; no universal winner score. An honest tie or loss is a result, not a reason to manipulate tasks.
3. Prioritize evidence integrity, real target defects, suite maintenance and the measured speed deficit. More repetitions alone are low value until these gaps are addressed.
4. Investigate terminal fidelity proactively using realistic multilingual/stateful tasks. Previous ASCII-heavy successes do not settle wide-cell correctness. A selected compatibility change still needs a reduced failing task.
5. Keep Go, standalone execution, real PTYs, strict contracts, serial suites and local offline reports. No language rewrite, cloud, agent platform, automatic retries or universal feature parity program.
6. Hold new outreach, follow-ups and marketing. Preserve the five recorded invitations as history. E5 provides a concrete readiness decision to the user; it never authorizes contact or publication by itself.
7. Preserve historical failed attempts, exclusions and release records. Repair stale active planning summaries and add explicit supersession notes rather than rewriting history.

## What “better” means

We want correct defect detection, reliable cleanup, useful terminal fidelity, quick setup, maintainable tests, fast enough real suites, good resource behavior, clear diagnosis and trustworthy installation. We cannot credibly beat framework unit tests at their own in-process job or claim every terminal protocol. The [readiness scorecard](engineering-readiness.md) defines targets and evidence for the selected product job.

Engineering can establish technical readiness before outreach. It cannot establish independent preference or retention without users. E5 therefore distinguishes “ready to ask for trials” from “demonstrated user preference.” If the user still requires universal leadership before outreach, A1 stays held and the unprovable parts stay explicitly unknown; no fabricated finish line.

## Next week: 27 September–3 October

This is a proposed allocation if execution is separately requested, not work started by this planning pass. Assume one maintainer with about 20 focused hours; change the calendar if capacity differs.

| Work | Budget | Checkpoint result |
| --- | ---: | --- |
| E0 evidence inventory, raw-artifact availability and risk-map audit | 6 h | Reconciled evidence ledger; supported counts; list of missing records |
| Select and preregister E1 real scenarios and holdouts | 5 h | Named tasks, exact candidate pins, independent outcomes and defect provenance |
| E2 measurement design and baseline setup planning | 4 h | Comparable acquisition paths, measured-phase definitions, cost limits |
| Close stale documentation inventory; E4 walkthrough checklist | 2 h | Version/installation/claim mismatch list with owners |
| Weekly review and contingency | 3 h | Re-estimate and choose one next executable slice |

Do not promise all runtime comparisons next week. Native availability, target builds and evidence recovery can consume the allocation. Missing evidence is a reported gap, not a failed maintainer.

## Weekly review procedure

Owner: project maintainer. Use one 45–60 minute review each week; archive a dated Markdown note and update the root roadmap once.

1. State the active checkpoint and exact user outcome. Record completed, failed, blocked and deferred work separately.
2. Review first-attempt failures, false passes, cleanup defects and newly lost support before feature requests.
3. Review one real workflow end to end: setup, useful assertion, bug detection, diagnosis, recovery, upgrade and maintenance cost.
4. Update the scorecard with numerator/denominator, host/version scope and evidence link; unknown stays unknown.
5. Check competitor changes only for relevant workflow impact. Documentation changes trigger evaluation, not automatic parity work.
6. Review actual engineering hours, native job time, artifacts and maintenance burden against budget. Drop optional breadth before weakening correctness.
7. Choose at most one implementation behavior and one supporting validation activity for the next week. Every addition displaces named work.
8. Record decisions, owner, next review date, exit evidence and permissions still needed. Never infer permission from a plan checkbox.

Weekly note template: date; checkpoint; hypothesis; baseline; work completed with evidence; failed/blocked attempts; scorecard deltas; real-scenario lesson; hours/cost; decision and alternatives; next slice and acceptance cases; outreach/release status. A milestone closes only with its exit record, not when the allocated week ends.

## Planning cleanup completed

Root roadmap now separates completed history from the next phase. Product focus and planning index no longer describe S8/S9 native verification as pending. The old comparison is explicitly fixture evidence. Historical catalogs/protocols retain their original intent with current-status pointers. A1 and the cohort preserve existing invitations while holding further contact. Decision D21 records the user-directed sequencing change. Public product code, schemas, workflows and benchmarks are unchanged.

Planning validation: 23 changed/new Markdown files; 248 local links and one heading target checked successfully; `git diff --check` clean. Only Markdown files changed. Runtime tests were not run because this pass changes plans and status documentation, not execution behavior. External research pages were read as sources; this is not an audit that every historical external link or CI artifact remains available.
