# Engineering readiness before renewed outreach

Planned 26 September 2026; complete E3–E5 execution was subsequently authorized, including testing-branch and final pushes. **E0–E4 accepted on 27 September: 5/6 milestones complete; E5 qualifying.** The [E1/E2 record](../validation/e1-e2-native-readiness-2026-09-27.md), [E3 boundary](../validation/e3-fidelity-boundary-2026-09-27.md) and [E4 record](../validation/e4-operator-readiness-2026-09-27.md) preserve first failures, repairs and exclusions. E3 uses an investigated fidelity deferral; E4 is familiar-operator evidence with human accessibility and timing limits. Publication and outreach remain unauthorized. Final changed bytes need E5 qualification. The [roadmap](../../roadmap.md) owns sequence; the [weekly review](weekly-review-2026-09-26.md) preserves the original planning pass.

## Outcome and boundary

Earn technical preference for deterministic keyboard-driven CLI/TUI regression testing: accurate state and screen checks, maintained real workflows, competitive total effort, bounded execution, useful evidence and reproducible installation. Strive to lead every relevant dimension and record losses honestly. Universal superiority across SDKs, graphics, agent automation and framework unit testing is neither our product scope nor a measurable release condition.

Owner: project maintainer. The implementing engineer records results; the maintainer reviews expected behavior and claim wording. If the same person does both, label self-review and operator familiarity. Native-host availability and human accessibility testing are dependencies, not presumed resources. No new paid infrastructure budget is assumed.

At most one implementation behavior is active at a time. Allow one selected terminal-compatibility family and one conditional authoring/CI convenience family in this phase. Existing-contract correctness repairs take priority. Any extra family needs a revised plan, concrete blocked task and displaced work. Stop after each accepted checkpoint for testing/feedback unless further execution was explicitly authorized.

## Scorecard: baseline, target and proof

Targets below are proposed engineering decision thresholds, not results, SLAs or population estimates. E0 freezes definitions before measured work; changing a target later needs a dated explanation retaining the original.

| Dimension | Current evidence / gap | Proposed exit target | Proof owner/checkpoint |
| --- | --- | --- | --- |
| Correct outcomes | Selected controls pass; screen-only false-pass lesson exists | Every admitted target defect detected for the intended reason; zero unexplained false passes, wrong exits or state corruption | E1, E5; independent state oracles |
| Real-world usefulness | Deep pinned corpus, little upgrade/maintenance evidence | Six primary and two held-out journeys pass/defect/recover; at least three primary journeys include a target-version or realistic UI-change maintenance exercise | E1, E4 |
| Reliability | 3,000 selected first attempts; other host transients recorded | Zero unresolved failures in claimed support; every original failure retained/classified; selected final-byte qualification under existing policy | E1/E5; no retry substitution |
| Terminal fidelity | Complex cell widths unsupported | Close one demonstrated valuable blocker or explicitly narrow the support claim after probes; no wrong advertised rendering accepted | E3; no universal Unicode label |
| Runtime | Short fixture medians 295–305 ms, about 5.6–6.0× fastest alternative | Investigate ≥30% reduction against matched current baseline; aim within 20% **or 50 ms** of fastest comparable median per short task; no real-suite regression beyond 10% **and** 100 ms without diagnosis | E2; ambition and release gates distinguished below |
| Resources | Partial RSS data, no qualified process-tree memory baseline | Establish process-tree CPU/RSS and suite drift; no unexplained sustained growth or managed survivor; compare matched tools without a universal memory target | E2/E5 |
| Installation | Three-host public binary/action checks | All advertised paths work; cold download/extraction and target/runtime setup timed separately; broken paths block readiness | E4/E5 |
| Authoring | Recipes/operator evidence only | Complete four journeys without undocumented steps; record all helpers and two maintenance changes per selected journey; compare total effort | E4; independent 4/5 target remains A1 |
| Diagnosis | Offline evidence shipped; independent timing unknown | Correctly classify six different failure classes, retain exact step/state/cleanup evidence, target ≤2 minutes each in operator rehearsal | E4; label familiarity |
| Accessibility | Browser/tree checks, human screen-reader path open | Complete keyboard and one interactive screen-reader walkthrough of install → report → next action, or block broad accessibility claim and explicitly scope readiness | E4 |
| Competitive advantage | Equal selected detection, speed loss, different feature breadth | All task-level wins/ties/losses/unknowns recorded; demonstrate at least one meaningful advantage on two primary real journeys without correctness loss | E2/E4/E5 |
| User preference / retention | Zero independent adoption recorded | Remains unknown until A1; ≥2 voluntary later uses is an A1 target | A1, never operator substitute |

Performance thresholds are decision targets, not permission to weaken readiness waits, output capture, final drain or cleanup. Missing a speed target keeps the competitive gap open. E5 may recommend a qualified scoped trial despite an explained tradeoff, but only the user can accept that recommendation and authorize outreach. An unresolved correctness failure in advertised scope cannot be waived for speed or schedule. A tie on every competitive task does not satisfy the proposed differentiation target; record the result and revisit positioning.

## E0 — reconcile evidence and freeze the next questions

User outcome: a maintainer can inspect what is actually supported and reproduce the basis for a claim.

Entry: this plan, existing release hashes, corpus and comparison records. Budget: 1–2 focused maintainer days.

1. Inventory every major claim: source/runner/target identities, exact host, spec/oracle, attempt denominator, record location and raw evidence availability. Check artifact expiry; preserve a bounded sanitized copy where authorized, or mark unavailable and schedule only the necessary rerun. Historical summaries remain attributed evidence if raw artifacts cannot be recovered.
2. Audit 300 risk rows against their 41 unique references: map to real test/subcase names and observed test events; distinguish one test exercising multiple risks from duplicated accounting. Report unit, PTY, integration and mapped-risk counts separately. Do not invent extra tests to reach 300.
3. Audit each of the 15 negative controls: target code mutation, altered input, missing dependency, spec change, or baseline change. State which defects it can prove. Identify at least six real target-code or historical bug cases for E1.
4. Freeze scenario selection, held-out tasks, competitor versions/documentation, oracle review, metrics, native cells, resource ceilings and non-goals before optimization. Keep both the older comparator pins and a separately labeled refreshed baseline if versions change.
5. Triage CV-02/Posting resource transients and installer regression history into reproducible hypotheses; do not erase them because the later campaign passed.

Exit: one reviewable evidence ledger with accessible/missing/invalidated distinctions, corrected count wording, scenario admission table and ranked hypotheses. Missing evidence blocks the affected claim, not unrelated design. No implementation until the first user-visible repair/investigation is selected.

## E1 — prove useful real workflows and defect sensitivity

User outcome: tests protect actual user tasks, including persisted state and recovery, rather than merely displaying expected text.

Entry: E0; follow the [real-world scenario protocol](real-world-scenarios.md). Budget: 4–6 days, including native setup and triage.

Deliver six primary journeys plus two held-out journeys across at least four projects and three implementation ecosystems. Reuse existing targets, fixtures and oracles first. Run each primary on two actually supported native hosts, covering all three advertised runner hosts overall; record unsupported/native-unavailable cells before execution. WSL remains a separate lane. Full 15×8×3 multiplication is not required.

Each admitted journey needs a human-readable expected outcome, known-good target, a real defect in target behavior, intended detection and unchanged-spec recovery. Include exact Git/file/database/request state where meaningful. At least two cases must render plausible success while persisting wrong state. Include one historical bug replay where a safe reproducible buggy/fixed pair exists; if unavailable, explicitly substitute a reviewed target patch and do not call it historical coverage.

Run five first-attempt good executions and one intended-negative/recovery pair per admitted primary-host cell for discovery. Then exercise scheduled variation and upgrades from the scenario protocol. Counts are development sampling, not a reliability percentage. A changed spec or oracle invalidates that cell's result and requires fresh controls. Keep real resource/service outages separate from runner defects without deleting them.

Exit: all six primary journeys have accepted task outcomes and negative controls on the admitted cells; every boundary failure has a disposition; two held-out definitions are frozen; at least three maintenance exercises completed. A correctness blocker goes to the smallest repair before expansion. Unmet cardinality is an explicit checkpoint shortfall, not silent exclusion.

## E2 — investigate latency and total cost

User outcome: real local and CI suites return accurate results promptly without growing resource or cleanup cost.

Entry: E0 baseline plus at least two valid E1 journeys. Budget: 3–5 days; E1 need not be fully complete to begin measurement design. Keep one active code change.

First reproduce the earlier C1–C3 direction using pinned comparable routes. Measure binary download/extraction separately from source builds and dependency installation. Record whole command wall time plus, where instrumentable, launch, target readiness, assertion/settlement, evidence generation and cleanup. Do not subtract nested or overlapping spans to invent “runner overhead.” Validate instrumentation overhead using uninstrumented controls.

Profile wait/drain/polling and artifact paths; investigate the 150 ms allowances without assuming they explain the loss. Include natural exit, last-moment output, continuously redrawing screens, slow input, hang, cancellation, output flood and descendant cleanup. No lower timeout or earlier snapshot simply to meet the benchmark target.

Compare current and candidate Playtestr on the same host/toolchain/targets with counterbalanced order. Initial cells use 30 fresh attempts; report median, range, all failures and uncertainty. Use at least 100 observations per selected cell before presenting p95 as descriptive data, still with sample size and no population guarantee. Compare at least two E1 real journeys against the strongest applicable alternative, counting oracle and cleanup glue. Evaluate Termless PTY feasibility for at most one day; blocked setup is visible, not an assumed loss.

Run serial suite sizes 1, 10 and 50 from existing valid workflows, preserving task composition and first results; repeated tasks remain repeats. Observe process-tree RSS/CPU, artifact size, total time and memory trend under a bounded longer suite. If resource instrumentation is unavailable, label unknown. A faster microtask with a slower or less correct real suite is not a successful optimization.

Exit: measured cause or bounded inconclusive diagnosis, before/after task table, real-suite effect, resource evidence and regression controls. If the latency target cannot be met safely, retain current semantics, document the loss and proceed to E5 with the gap. No automatic scheduler, rewrite or feature expansion.

## E3 — close the most valuable fidelity gap

User outcome: a specified real interaction renders and accepts input correctly on its claimed hosts.

Entry: E1 probes and an independently justified failing task. Budget: 2–3 days investigation, plus at most 3–5 days for one selected family; otherwise re-estimate explicitly.

Probe multilingual filenames, wide text beside a selection/cursor, combining marks, paste into an editor/wizard, repeated shrink/grow and terminal queries on appropriate real targets. Freeze width/locale assumptions. Compare captures with a reference terminal or authoritative expected cells; disagreement between emulators is a question to resolve, not a majority vote.

If a blocker qualifies, choose among a local fix, a bounded dependency change behind the session interface, or an explicit unsupported boundary. A dependency change needs an ADR evaluating license, release maintenance, security history, Go/standalone compatibility, memory/output bounds, three-host behavior and migration. Do not promise complete emoji/grapheme support from one fix. Keyboard additions require exact encoding and lifecycle tests; styles/mouse remain conditional on valuable inaccessible tasks.

Exit: one previously failing real task plus negative/recovery controls, applicable native terminal/lifecycle/race checks and updated contract, or an evidence-backed deferral with exact exclusions. The old S10 deferral remains historically valid; E3 is a new investigation. Scope reduction cannot hide a regression of existing support.

## E4 — author, diagnose, maintain and install

User outcome: someone following the docs can create a meaningful test, understand failures and keep it useful after change.

Entry: stable E1 scenarios and relevant E2/E3 fixes. Budget: 3–4 days. Prefer docs and smaller repairs over new commands.

Rehearse selector, stateful wizard, editor and repository-tool journeys from clean directories using the exact intended binary. Time prerequisites, install, first correct test, intended defect, diagnosis and recovery separately. Count edits, commands, helper files, unsuccessful attempts and operator hints. Rehearse baseline review and target upgrade; two real maintenance changes per chosen walkthrough. Where practical, delay diagnosis or conceal the injected variant from the operator; otherwise explicitly label prior knowledge.

Use six diagnosis classes: target logic defect, bad spec, missing target/runtime, assertion timeout, wrong exit and cleanup/artifact failure. Reports must distinguish primary and cleanup failure and preserve useful final evidence. A fast wrong diagnosis fails. Check a report offline, keyboard navigation, paths with spaces, failed installation, rollback, stale PATH and interrupted upgrade using existing gates.

Audit README/docs/trial entry points for stale release/action claims and copy-paste commands. Complete the outstanding interactive screen-reader path with an available human/operator and appropriate environment; accessible-tree checks alone cannot close it. If unavailable, name the limitation and owner at E5.

Consider one authoring/CI extension only after two repeated real workflow failures or one documented necessary CI ingestion consumer: template assistance before recorder, narrow exporter before orchestration, bounded assertion before masking. Otherwise ship no new family. Exit: four reproducible walkthroughs, six correctly diagnosed classes, maintenance/cost comparison, presentation gaps disposition and no undocumented installation step. Independent first-use timing remains A1.

## E5 — qualify and decide readiness

User outcome: the downloadable bytes support the exact story and claims being proposed.

Entry: E0–E4 accepted records, no unresolved correctness blocker in advertised scope. Budget: 2–3 days engineering plus native queue time. Owner reviews a private evidence packet before any external action.

1. Run the two held-out journeys without tuning first; preserve failure results. If a failure requires a fix, replay it and record contamination; use one replacement holdout for generalization, capped at one replacement cycle before a scope review.
2. Freeze final source, embedded version, toolchain, dependency/build flags and hashes. Reuse unchanged-byte evidence only under the existing [invalidation rules](execution-contract.md). If runner bytes changed, use [R6 qualification](release/06-qualified-release.md) including its final 3,000 selected attempts; do not run that expensive campaign after every edit.
3. Recheck affected native support, exact package contents, install/upgrade, public-contract/schema compatibility, cancellation, descendants, output flood and report/privacy limits. Public-asset checks remain pending until a separately authorized publication actually happens. Stable relabeling requires new bytes and qualification; no new version is chosen in this plan.
4. Review a task-level scorecard with all losses, unsupported cases, confidence and artifacts; measure actual effort against the phase estimate. Show at least one meaningful workflow advantage on two real tasks or explicitly mark the differentiation gate unmet.
5. Decide: technically ready for a scoped trial; one named blocking repair; or narrow/reposition the product. No endless benchmark expansion. Provide the user exact release/claim/outreach proposals for any later approval.

Separate E5 technical qualification from public availability: a qualified unpublished candidate is ready for a release decision, not a verified public-download recommendation. If trials will use new bytes, authorized publication and successful public-asset verification must finish before those bytes enter the trial kit. If unchanged v0.4.0-rc.1 remains the trial version, state which later experiments do not apply to that version.

E5 does not itself prove independent adoption. Renewed contact stays held until the user accepts the readiness boundary and explicitly authorizes specific outreach. Marketing claims must cite the exact task/version/host evidence and preserve tradeoffs. A1 subsequently tests independent comprehension, useful CI and voluntary reuse; A2 waits for repeat use and buying evidence.

## Capacity and stop rules

Estimate 15–23 focused maintainer days plus the optional 3–5 day E3 repair and native/interactive-test availability. Using eight focused hours per maintainer day, at 20 focused hours/week this is roughly 6–12 calendar weeks, not a delivery promise. Re-estimate after E0; do not book all weeks as mandatory feature development. A failed hypothesis can close with an honest no-change decision.

Provisional compute budget: after two pilot cells, extrapolate planned attempts × observed duration and artifact size; cap each exploratory campaign at six native runner-hours and 1 GiB retained compressed evidence. If forecast exceeds this, reduce optional cells or submit a costed revision before launching; never stop recording failures to fit. Qualification uses the existing budget and evidence policy. No additional spend is implied.

Stop expansion when a known task lacks a valid oracle, comparison semantics differ materially, a target requires unsafe/production resources, or engineering spends two days without reducing a blocker. Record the problem and choose a smaller task or a reviewed support boundary. Correctness failures are fixed or excluded explicitly; ambitious speed, breadth and usability targets remain visible if unmet. A larger campaign is never the default answer to weak evidence.
