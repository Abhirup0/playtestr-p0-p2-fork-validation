# Playtestr roadmap

Updated 1 October 2026 after rc.3 qualification, publication and native public-download verification. **This file is the authoritative status and execution order.** Detailed plans live in [docs/plans](docs/plans/README.md). Historical evidence remains in its original dated records.

Product goal: a developer installs one runner, writes a short terminal interaction, catches a meaningful regression, and understands the failure quickly. Protect correctness and simplicity while increasing real-project depth. E0-E5 are accepted within their recorded boundaries: audited claims, native real tasks, measured cost, investigated fidelity deferral and operator walkthroughs. The macOS last-output and bounded installer repairs passed native gates. E5 qualified exact private v0.4.0-rc.2 bytes and recommends a scoped trial; publication subsequently completed with verified downloads; outreach and marketing remain held. [Execution checkpoint](docs/validation/e3-e5-checkpoint-2026-09-27.md).

## Read the status correctly

The later [wide-character task](docs/plans/wide-character-next-steps-prompt.md)
is complete and now ships in verified v0.4.0-rc.3;
[release evidence](docs/validation/wide-character-release-2026-10-01.md) preserves exact-byte results and remaining limits. The older rc.2 bytes remain unchanged.

| Label | Meaning |
| --- | --- |
| Implemented | Behavior exists in source; says nothing by itself about other hosts or released binaries |
| Locally verified | Exact local checks are recorded; native evidence applies only to the named host |
| Natively verified | Exact OS/architecture path ran; a workflow configuration or cross-compile is insufficient |
| Published and verified | Versioned public assets were downloaded and checked; see their own evidence |
| Adopted | Independent maintainer ran/reviewed the flow, with later reuse recorded separately |
| Planned / conditional | Not implemented by this planning work; conditional work may be explicitly deferred |

Engineering completion, publication and adoption are separate dimensions. An unchecked human gate does not undo a completed release; a successful local test does not close a missing native/public-asset gate. No independent adoption is established in the reviewed records.

## Published runner releases

| Release | What it delivered | Recorded verification | Remaining limitations / use |
| --- | --- | --- | --- |
| [v0.1.0-rc.1](docs/releases/v0.1.0-rc.1.md) | First packaged MVP: spec/report v1, PTY actions, assertions, snapshots, bounded execution | Three native package paths and later downloaded-asset checks; source `1dde372` | Historical Linux `/dev/tty` defect; not a recommended basis for new full-screen coverage |
| [v0.1.0-rc.2](docs/releases/v0.1.0-rc.2.md) | Controlling-terminal fix, improved disappearance/redraw synchronization and failure capture | Three native package/public-install paths; source `583352a`; separate real-app evidence | Exact workflow exclusions remain in trial records |
| [v0.1.0](docs/releases/v0.1.0.md) | First stable MVP, published 12 September | Three native package/public-install paths; source `4ed8884`; nine-app refresh separately scoped | Latest stable in reviewed records; no directory-suite, HTML-report or workspace promise from this version |
| [v0.2.0-rc.1](docs/validation/sprint-5-engineering-2026-09-15.md) | Sprint 5 directory suites, preview, summaries and isolated evidence | Source `ea2e77f`; release run `35096743871`; public-install run `35120830130`; three native hosts | Prerelease, not stable v0.2.0; participant acceptance pending |
| [v0.3.0-rc.1](docs/releases/v0.3.0-rc.1.md) | Sprint 7 offline HTML reports plus prior suite work, published 18 September | Source `7cf64af`; release run `35288218202`; public-install run `35288555826`; three native hosts | Historical prerelease; does not contain later spec-v2 workspaces |
| [v0.4.0-rc.1](docs/releases/v0.4.0-rc.1.md) | Opt-in workspaces, report v2, setup action and release stories, published 25 September | Frozen source `f6ffeb7`; qualified archive hashes match public assets; immutable action `1c03904`; six-lane public verification [36173075209](https://github.com/Wyrcan-io/playtestr/actions/runs/36173075209) | Verified prerelease on Windows amd64, Linux amd64 and macOS arm64; not the stable channel |
| [v0.4.0-rc.2](docs/releases/v0.4.0-rc.2.md) | Bounded installer reads, Linux EOF optimization, macOS final-output preservation | Frozen source `ae97c62`; exact archives promoted unchanged; public distribution/upgrade and binary-only checks passed on three native hosts | Prerelease; wide-cell/query and human-accessibility exclusions retained; no outreach |

Exact hashes and run links belong to the cited records. Local tags corroborate identities but do not themselves prove publication. The annotated v0.1.0 tag object differs from its peeled source commit; use the source commit above for code provenance. No stable v0.2.0/v0.3.0/v0.4.0 is claimed; released workspaces are available in v0.4.0-rc.1.

## All sprints: completed, existing and planned

| Sprint | Delivered behavior | Status and evidence | Still to do |
| --- | --- | --- | --- |
| 0 | Baseline, repository/language decisions, menu proof | Implemented; [delivery history](docs/sprints.md), [Go decision](docs/language-decision.md) | No restart or rewrite |
| 1 | Exact process outcomes, unexpected exit detection | Implemented; incorporated into MVP releases; [history](docs/sprints.md) | Maintain regression coverage |
| 2 | Budgets, cancellation, output caps, managed tree cleanup, explicit environment | Implemented; incorporated into MVP releases; [history](docs/sprints.md) | Preserve documented process-escape boundaries |
| 3 | Rendered text snapshots, diffs, transactional updates and terminal fixtures | Implemented; incorporated into MVP releases; [history](docs/sprints.md) | Selected cell-width/protocol limits remain |
| 4 | Formats, packaging, native matrix, Gum trial, licensing | Implemented and published; [platform evidence](docs/platform-support.md) | New releases must requalify their own bytes |
| 5 | Serial suites, deterministic listing and useful evidence layout | Implemented, natively/publicly verified in v0.2.0-rc.1; [record](docs/validation/sprint-5-engineering-2026-09-15.md) | Independent CI adoption in A1 |
| 6 | CI-to-local failure handoff | **Ordinary handoff documented; manifest deferred**; [experiment](docs/validation/sprint-6-handoff-2026-09-21.md), [guide](docs/ci-failure-handoff.md) | Reopen software only for a repeated safe context omission the guide cannot resolve |
| 7 | Offline failure diagnosis | Implemented, natively/publicly verified in v0.3.0-rc.1; [record](docs/validation/sprint-7-engineering-2026-09-18.md) | Independent diagnosis timing in A1 |
| 8 | Setup-only exact-version GitHub Action | Implemented, source-qualified, repaired for both checksum contracts, and publicly verified on three native hosts; [record](docs/validation/r6-publication-and-blocker-2026-09-25.md) | Independent participant CI use in A1 |
| 9 | Fresh bounded workspaces, spec/report v2, v2 HTML rendering | Implemented, qualified and publicly verified in frozen bytes on three native hosts; [record](docs/validation/sprint-9-engineering-2026-09-19.md), [R6-V](docs/validation/r6-publication-and-blocker-2026-09-25.md) | Independent participant use in A1 |
| 10 | One evidence-selected terminal compatibility improvement | Original deferral reopened for the reduced MICRO-08 CJK failure; selected two-column repair natively verified in development; [record](docs/validation/wide-character-2026-09-28.md) | Fresh release qualification; combining clusters/query round trips remain excluded |
| 11 | Deep real-project validation corpus | **A0/A1/B/C and R6-V complete**; [checkpoint](corpus/README.md), [B evidence](docs/validation/sprint-11-b-corpus-depth-2026-09-24.md), [R6-V](docs/validation/r6-publication-and-blocker-2026-09-25.md) | Independent adoption remains A1 |
| 12 | Easier first-test authoring | **A complete; B deferred at its evidence gate**; [A record](docs/validation/sprint-12-a-authoring-2026-09-21.md), [B decision](docs/validation/sprint-12-b-decision-2026-09-21.md) | Reopen B only for two reduced workflow failures with the same missing input/assertion family |
| 13 | Native evidence, integrated hardening and fair comparison | **A0/A1/B/C/D and R6 complete**; [A0](docs/validation/sprint-13-a0-native-gaps-2026-09-20.md), [A1](docs/validation/sprint-13-a1-integrated-hardening-2026-09-21.md), [B](docs/validation/sprint-13-b-setup-action-2026-09-21.md), [C](docs/validation/sprint-13-c-competitive-2026-09-22.md), [D](docs/validation/sprint-13-d-rehearsal-2026-09-24.md), [R6-V](docs/validation/r6-publication-and-blocker-2026-09-25.md) | Preserve regressions through E0-E5; A1 is held |
| 14 | Reproducible demos and release kit | **Complete; v0.4.0-rc.1 published and publicly verified**; [plan](docs/plans/sprints/14-demos-and-release-kit.md), [R6-K record](docs/validation/sprint-14-r6-k-2026-09-25.md), [R6-V](docs/validation/r6-publication-and-blocker-2026-09-25.md) | Manual interactive screen-reader session remains open |

Sprint numbers are durable identifiers, not chronology: 7 shipped before 6, and 11 discovery precedes 10 selection. Do not rebuild implemented suites, HTML reports, the setup action or report-v2 rendering.

## Completed release and presentation milestones

| Milestone | What is complete | What is open |
| --- | --- | --- |
| [R1](docs/plans/release/01-release-candidate.md) | First native candidate packaging/publication | Historical defects remain documented, not erased |
| [R2](docs/plans/release/02-installation-walkthrough.md) | Automated public-asset installation checks | Independent unassisted walkthrough moves to A1 |
| [R3 technical campaign](docs/plans/release/03a-windows-linux-project-trials.md) | Lazygit/Lazydocker/K9s operator testing and discovered defects | Not maintainer adoption; host/release distinctions preserved |
| [R3b](docs/plans/release/03b-trial-findings-and-candidate-readiness.md) | Candidate repairs and rc.2 technical closure | Historical exclusions remain visible |
| [R3c](docs/plans/release/03c-cross-stack-validation.md) | Nine-app Python/Rust/Node campaign; 18 intended Windows/WSL cells, 54 frozen primary attempts | Not 54 distinct workflows, native macOS app coverage or nine adopters |
| [R4](docs/plans/release/04-stable-release.md) | v0.1.0 stable publication and technical verification | Human post-publication handoff now belongs to A1 |
| [R5](docs/plans/release/05-public-presentation.md) | Website/docs implementation and local browser/build checks; [validation](docs/validation/public-presentation-2026-09-12.md) | R6-V records deployed browser/route checks; interactive human screen-reader work remains open for E4. Historical gaps require their own evidence |
| [R3 independent trials](docs/plans/release/03-real-project-trials.md) | Protocol and templates only | Deferred to A1; no qualifying independent use claimed |

## How much is done?

The original MVP and the accepted subsequent engineering batch are complete through **R6-V**. S12-B and the S6 manifest remain evidence-backed deferrals. S10 was later reopened for the selected CJK failure and its development repair passed native checks. Engineering readiness is **6/6 milestones complete within explicit acceptance boundaries**. Independent adoption and commercial validation remain unproven; an overall product-completion percentage would hide those differences.

Recorded depth is 15 projects / 120 workflows; 3,000 repetitions cover ten selected workflows on three hosts. Full application depth is not a 120-workflow three-host matrix. The 300 focused risk-map rows point to 41 distinct references and are not automatically 300 independent executed tests. See the [weekly audit](docs/plans/weekly-review-2026-09-26.md) and [exact host coverage](docs/qualified-compatibility-v0.4.0-rc.1.md).

The historical Linux comparison found equal selected detection and a Playtestr speed deficit; that record remains intact. The E2 candidate, subsequently published as v0.4.0-rc.2, removes a measured Linux final-drain cost, improves matched short-task whole-command medians about 80%, and reduces the observed 50-test suite from 126.8 to 113.5 seconds. Create-vite now effectively ties Atago on the selected task; Lazygit remains substantially slower. [Native acceptance and measured tradeoffs](docs/validation/e1-e2-native-readiness-2026-09-27.md) retain every loss and sampling limitation; no universal ranking follows.

## Execute next, in this order

Subsequent user instructions authorized E0-E5 execution, native hosted validation, source pushes and exact rc.2 publication. The later [wide-character prompt](docs/plans/wide-character-next-steps-prompt.md) authorizes a scoped development repair and verification. Outreach, marketing and PR/issue/discussion mutations remain held. Completed sprint IDs remain historical; do not rebuild shipped capabilities.

| Checkpoint | Concrete outcome | Acceptance / dependency | Status |
| --- | --- | --- | --- |
| E0: evidence reconciliation | Auditable claims, counts, artifact availability and frozen experiment questions | Map risk rows to actual tests; classify controls; select scenarios, hosts and comparison pins | **Complete with scoped evidence gaps**; [ledger](docs/validation/e0-evidence-reconciliation-2026-09-26.md), [freeze](docs/validation/e0-experiment-freeze-2026-09-26.md) |
| E1: real-world effectiveness | Six useful primary journeys with state checks, target defects and maintenance exercises | E0; good/defect/recovery on two native hosts per primary journey, all three runner hosts represented; two holdouts reserved | **Complete at admitted scope**: six journeys on all three hosts, scheduled variations and three synthetic maintenance exercises; human authoring time remains unknown; [record](docs/validation/e1-e2-native-readiness-2026-09-27.md) |
| E2: runtime and resource cost | Explain and safely reduce measured overhead; compare real suites and total effort | E0 plus two valid E1 journeys; matched before/after, real-task comparison and lifecycle controls | **Complete at engineering boundary**: causal EOF proof, matched short/real tasks, paired 1/10/50 resource suites and lifecycle/race controls; remaining runtime/effort losses explicit; [record](docs/validation/e1-e2-native-readiness-2026-09-27.md) |
| E3: targeted terminal fidelity | Original native investigation; later selected CJK repair | [Original exclusions](docs/validation/e3-fidelity-boundary-2026-09-27.md), [development repair](docs/validation/wide-character-2026-09-28.md) | Historical deferral retained; selected wide-cell repair qualified and published in verified rc.3 |
| E4: authoring, diagnosis and maintenance | Four walkthroughs, eight maintenance changes, six diagnoses and native correctness repairs | [Operator and accessibility boundaries](docs/validation/e4-operator-readiness-2026-09-27.md) | Accepted |
| E5: final qualification and readiness decision | Exact-byte evidence, two held-out definitions, honest competitive scorecard | [Qualified private v0.4.0-rc.2](docs/validation/e5-qualified-readiness-2026-09-27.md); 3,000 first attempts on three native hosts, support/accessibility exclusions | **Complete; published downloads verified; outreach held** |
| A1: independent adoption | Consenting maintainer first use, participant CI and voluntary later use | E5 readiness review plus explicit permission for each outreach action | **Held** |
| A2: commercial discovery | Evidence about paid value and support cost, or a no-build decision | Independent repeat use; no cloud/accounts/billing assumption | Preparation only; gate closed |

Six admitted primary journeys are Lazygit, micro, create-vite, fzf, litecli and Posting; GitUI and television remain frozen holdouts. Evidence applies to the exact tested pins/workflows/hosts, not broader application or framework compatibility. Runtime benchmarks support the decision; real-task correctness, maintenance and cleanup are required separately.

## Outreach and marketing boundary

The [cohort record](docs/trials/cohort.md) says five invitations were posted before this review, with zero recorded responses or consents. Preserve that history. Further invitations, follow-ups and marketing are held under the user's new direction. Nothing in this plan authorizes external mutations, contact or removal of prior posts.

E5 produces a concrete recommendation for the user. Technical readiness can be established before outreach; independent preference cannot. Aim to lead each important dimension, keep every win/tie/loss/unknown visible, and never claim universal superiority. The user decides whether the evidence is sufficient to resume specific outreach. A1 measures independent value and retention; operator campaigns cannot close it.

## Release strategy

Stable v0.1.0 remains the stable channel; v0.4.0-rc.3 is the newest published, verified prerelease. Earlier rc.2 [publication evidence](docs/validation/e5-publication-2026-09-28.md) remains historical. Keep published tags/assets immutable. A necessary correctness hotfix may interrupt planned work with narrow acceptance and its own qualification.

Any runner source, version, compiler/dependency or build-flag change creates new bytes and requires affected native and final qualification. Unchanged-byte evidence may be reused under the [invalidation policy](docs/plans/execution-contract.md). A new stable version is not qualified by relabeling prerelease results. Publication and downloaded-byte verification remain separate explicit actions under [R6](docs/plans/release/06-qualified-release.md).

## Weekly cadence and scope

The [26 September review](docs/plans/weekly-review-2026-09-26.md) owns this week's findings, proposed 20-hour allocation and review template. Next planning review: 3 October 2026. The phase estimate is roughly 6-12 weeks at that capacity, subject to E0 re-estimation and native/human-test availability; it is not a delivery commitment.

Keep one implementation behavior active, with one supporting validation activity. Reuse the 120-workflow corpus; do not inflate counts or automatically expand to every host/tool permutation. Allow one evidence-selected terminal family and one conditional authoring/CI family. Correctness repairs outrank optional breadth. No language rewrite, autonomous game behavior, hosted platform, automatic retries or parallel runner by default.

Every checkpoint ends with exact evidence, retained failures, exclusions, actual cost and a next decision. Missed speed/usability targets stay visible; false passes, destructive cleanup and unbounded behavior cannot be waved through. A good benchmark cannot compensate for a broken real workflow.

## Immediate next decision

**E0–E5 complete at their scoped boundaries.** Review the
[private readiness decision and kit](docs/validation/e5-qualified-readiness-2026-09-27.md).
Publication and native download/install verification completed under the later user instruction.
**No outreach or marketing now:** A1/A2 remain held until a later explicit instruction.
Use the verified download and existing examples locally. The requested
[three-step wide-character task](docs/plans/wide-character-next-steps-prompt.md)
is complete as a scoped development repair. The authorized [wide-character release cycle](docs/validation/wide-character-release-2026-10-01.md)
is complete: `v0.4.0-rc.3` passed its 3,000-attempt exact-byte campaign, native
gates, public-download/action and genuine upgrade checks. Stable v0.1.0 remains
unchanged. No outreach, marketing or website deployment occurred. Next decision:
use the verified prerelease locally; stable promotion or specific independent
trial/outreach requires a later instruction. Human accessibility/adoption remain open.

**E3's original investigated deferral remains historical evidence.** Later development corrects the selected MICRO-08 wide-cell gap on all three native hosts; [the repair record](docs/validation/wide-character-2026-09-28.md) preserves first failures and reviewed snapshot migration. Combining clusters and query-dependent flows remain excluded. The published rc.2 runner retains its original boundary; rc.3 separately qualifies the selected repair.

GitHub-hosted native jobs resolved the missing-device dependency. E0-E2 acceptance
and the completed push preserve first failures, source/runner/target hashes,
unknown human effort and the remaining Lazygit readiness cost. The published
v0.4.0-rc.1 assets are unchanged. Held-out tasks and exact changed-byte qualification
are complete within the E5 record; no release or outreach follows automatically.
