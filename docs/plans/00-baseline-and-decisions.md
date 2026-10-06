# 00 — Baseline and direction decisions

Status: planning, 6 October 2026. Repository-document audit, not fresh execution or remote release verification. [Roadmap](../../roadmap.md).

## User constraints translated into decisions

| Constraint | Decision | Consequence |
| --- | --- | --- |
| Position before marketing | Terminal regression checks for PRs, authored locally | One message across docs, examples and checkout |
| Keep everything AI-free | Deterministic recording, assertions and review | Human selects scenarios and accepts expectations |
| Avoid typing every keypress into JSON | Guided recording with explicit checkpoints | Recorder is launch scope; timing playback is insufficient |
| Minimize operating work | Managed metadata backend; customer-owned execution/evidence | No VM fleet or mandatory analytics dashboard |
| Pay after revenue | Prove free-tier feasibility and bounded usage | Not a guarantee every backend fits a free tier |
| Complete engineering before marketing | Commercial loop, 100-project campaign, launch decision | No hidden recruitment prerequisite |
| 100 independent real projects | 100 distinct upstream codebases in operator validation | Not 100 customers, installs or independent human testers |
| Plans only now | Documentation replacement | No implementation or activation |

## Reuse inventory

| Asset | Reference | Treatment |
| --- | --- | --- |
| Go runner and PTY lifecycle | [README](../../README.md), [language ADR](../language-decision.md), [platform evidence](../platform-support.md) | Preserve boundaries; no rewrite |
| Strict specs/reports | [v1](../spec-v1.md), [v2](../spec-v2.md), [report v2](../report-v2.md) | Additions need explicit migration/version decisions |
| Snapshots and updates | [Snapshots](../snapshots.md) | Reuse transactional update behavior |
| Suites and workspaces | [Suites](../suites.md), [workspaces](../workspaces.md) | Reuse; never imply sandboxing |
| HTML reports and summary helper | [Reports](../failure-reports.md), [5 October record](../validation/adoption-preparation-2026-10-05.md) | Reuse evidence; minimize new metadata |
| Setup Action and PR example | [CI guide](../ci-installation.md), [workflow](../../.github/workflows/terminal-pr-example.yml) | Extend complete journey; keep builds explicit |
| Releases | [v0.1.0](../releases/v0.1.0.md), [rc.3](../releases/v0.4.0-rc.3.md) | Published identities immutable |
| 15-project corpus | [Corpus](../../corpus/README.md), [qualification](../qualified-compatibility-v0.4.0-rc.1.md) | Re-admit; no automatic new campaign credit |
| Research and comparisons | [Tool choice](../research/tool-choice-2026-10-05.md), [native E1/E2](../validation/e1-e2-native-readiness-2026-09-27.md) | Keep dated losses and unknowns |
| Website/docs | [Website record](../website.md) | Future repositioning; no future-feature claims now |

## New scope

Guided setup/recording; meaningful readiness authoring; fixture reuse; generated CI setup; least-privilege App; result provenance; review of baseline/spec/policy changes tied to revisions; small account/repository settings surface; hosted checkout/portal; entitlements; deletion; cost/operations instrumentation; 100-project validation and final qualification.

A tiny authenticated page for installation, billing, selected repositories and review is allowed. A general analytics dashboard or hosted terminal environment is not required.

## Retained limits

- Existing terminal exclusions include combining/emoji/ZWJ and target-query behavior; use exact release docs. Repair a concrete blocked need, not every terminal feature.
- Screen success may conceal incorrect saved state. File/Git/database checks need a bounded oracle with the correct workspace lifecycle.
- PTYs execute with host permissions. Fork code needs restricted ephemeral CI.
- Scheduling varies; deterministic inputs/expectations do not prove universal absence of flakes.
- Actions evidence is not proof against a malicious repository administrator. The App's trust model is explicit in 04/07.
- Historical invitations/refusals remain history. No prior outreach permission carries forward automatically.

Selected direction: PR-first, free local utility, commercial review automation, managed backend, customer compute, AI-free, 100-project prelaunch gate.

Provisional: Workers/D1, one $49 tier, merchant-of-record fallback, numerical quotas, integration language and final version. [12](12-risks-and-decisions.md) assigns owners and gates.

Unknown: demand, conversion, retention, independent usability, provider eligibility, measured unit cost, support effort and results on the 100 projects. A plan cannot establish these facts.
