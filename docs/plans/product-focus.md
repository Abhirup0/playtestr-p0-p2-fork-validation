# Product focus

Decision update: 26 September 2026. The root [roadmap](../../roadmap.md) owns sequence; the [research refresh](../research/competitive-refresh-2026-09-26.md) records evidence and uncertainty.

## User and job

Start with maintainers of keyboard-driven CLIs/TUIs who want important interactions protected through their real executable in CI. They already have unit tests or manual checks, care about reviewable changes, and cannot spend days assembling PTY scripts. Prioritize selectors, setup wizards, local editors, and repository tools with deterministic data.

Promise: **Press the keys. Catch the bug. Understand the failure.** Install one binary, review a short test, see the intended regression fail, and recover without learning terminal internals. Keep fast framework tests alongside the small E2E layer.

Live production administration, remote infrastructure, autonomous exploration, graphical terminals, and universal protocol coverage are outside this batch. A workflow requiring unsupported semantics should receive clear limits and an appropriate alternative.

## Earn preference through the complete workflow

Real PTYs, declarative specs, snapshots, binaries, and HTML evidence overlap with competitors. Our differentiation hypothesis is the complete low-maintenance experience: explicit readiness, bounded outcomes, reviewed baselines, exact installation, portable evidence, and reproducible recipes across languages.

Invest in three assets that improve without growing the API:

1. Versioned real-project recipes with independent postconditions and known-bad cases.
2. Reports that explain the evidence and its limits in one file.
3. Demos viewers can reproduce as the same good/bad/recovered flow.

These are execution opportunities, not claims of invention. Reliability, usability, and preference require comparison and independent use.

## Priorities

| Priority | Gap | Response |
| --- | --- | --- |
| P0 | False passes, state corruption, unbounded execution, cleanup or data loss | Smallest evidence-backed repair; cannot be traded for speed |
| P1 | Claims, mapped counts and raw evidence need reconciliation | E0 audit; no extra test-count target |
| P1 | Real target defects, variation and upgrade maintenance underrepresented | E1 primary journeys and E5 holdouts |
| P1 | Measured short-task latency deficit and incomplete resource data | E2 profiling and real-suite comparisons |
| P1 | Wide cells/input may block valuable real tasks | E3 proactive probes, one reduced task before implementation |
| P2 | Independent usability unknown; operator journey still needs hard cases | E4 installation, authoring, diagnosis and maintenance rehearsal |
| P2 | Changed bytes need trustworthy distribution | E5 qualification using existing R6 rules |
| Later | Preference, retention and willingness to pay | A1/A2 after readiness review and explicit outreach authorization |

## Feature budget

The new E0-E5 phase permits at most one selected terminal-compatibility family and one conditional authoring/CI convenience family. The earlier S10/S12-B/manifest deferrals remain historical decisions; new implementation needs fresh evidence and a narrow checkpoint. Existing-contract fixes, tests, docs, packaging, and report integration still need small acceptance boundaries.

Every addition needs a failed workflow, evidence that current features or a recipe cannot solve it, a minimal contract, failure tests, migration cost, and maintenance owner. A competitor checkbox alone is insufficient.

Keep serial execution, JSON specs, text snapshots, one setup action plus archives, and offline reports. Defer generic scripting, multiple SDKs, AI auto-healing, retries that hide flakes, hosted dashboards, billing, recorder engines, image/style assertions, broad mouse protocols, many package channels, and parallel scheduling. External recording tools may produce marketing assets. Autonomous game behavior stays in Gametestr.

JUnit requires a named CI consumer whose ingestion need is unmet. Parallelism requires measured unacceptable runtime after profiling and proven resource separation. Region/masking features require unavoidable dynamic data and proof that meaningful regressions remain visible.

## Demo acceptance

Show a real pass, a controlled target defect, the captured failure and recovery with the same spec and unchanged reviewed baseline. A viewer must understand the caught bug and be able to run the same example. Label recordings and editorial annotations; provide static and keyboard-accessible alternatives. [Sprint 14](sprints/14-demos-and-release-kit.md) owns the three stories, reproducible assets, browser checks and release kit. Independent comprehension and timing measurements follow in A1.

## Outcome targets

These are proposed targets, not achieved metrics. Record all attempts and assistance.

| Outcome | Engineering proof target in E0-E5 | Independent proof later in A1 |
| --- | --- | --- |
| First value | Fresh-machine installation and three recipes without undocumented setup | 4 of 5 participants reach pass/failure/recovery within 10 minutes after prerequisites; installation timed separately |
| Diagnosis | Correct category, step, screen/diff, and cleanup for seeded defects | 4 of 5 identify the seeded problem within 2 minutes from the report |
| Trust | Every admitted known-bad case fails for its intended reason | Users distinguish application, test, setup, and runner failures |
| Reliability | Native repeated-run and lifecycle campaign | Participant-owned repeated CI use; unexplained failures investigated |
| Maintenance | Pinned recipes, bounded costs, preserved baselines | At least 2 projects voluntarily reuse in a later session |

The [readiness scorecard](engineering-readiness.md) sets measurable goals across relevant dimensions. Aim for leadership, disclose losses, and distinguish engineering evidence from independent preference. The user chose to hold further outreach until a readiness review; optimizing without users remains a risk, so E0-E5 have a finite scope, budget and decision point. No universal-best claim or automatic recruitment follows.
