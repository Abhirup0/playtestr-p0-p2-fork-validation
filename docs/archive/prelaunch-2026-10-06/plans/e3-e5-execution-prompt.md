> ARCHIVED on 6 October 2026. Historical context only; do not execute this plan. The [current roadmap](../../../../roadmap.md) supersedes its scheduling, gates, and scope.

# Comprehensive E3–E5 execution prompt

Prepared 27 September 2026. This is a prompt for the user to invoke; writing this
document does not itself authorize or start E3–E5. Copy the text below into the
next execution request.

---

Complete E3, E4 and E5 in the Playtestr repository. Implement and verify the
necessary changes, preserve all evidence, prepare the final readiness decision,
and commit and push the completed work. Continue through these milestones without
stopping at a plan or asking me to reconfirm routine authorized actions. Do not
claim completion until their declared acceptance boundaries are supported by
actual results. An honest investigated deferral or qualified recommendation is
valid where the plan permits it; missing mandatory checks are not passes.

## Authorization and boundaries

I authorize local implementation, fixture/oracle/test/documentation changes,
candidate builds and packaging, testing-branch creation and pushes, GitHub
Actions workflow creation/updates/dispatches, monitoring, log and artifact
retrieval, diagnostic revisions, necessary fixes, and the final verified commit
and push. Use standard GitHub-hosted Linux amd64, macOS arm64 and Windows amd64
runners for native evidence. I do not have Linux/macOS devices or SSH endpoints;
use Actions rather than asking me to acquire them. Local Windows checks remain
useful, and native hosted Windows is available when needed.

Use included/free standard Actions capacity for meaningful work. The previous
usage screenshot is historical, not a current quota meter. Do not purchase paid
runners, change budgets, enable paid overages, or assume an account reset has
occurred. After two pilot cells, forecast duration and compressed artifact size.
Keep each exploratory campaign within six native runner-hours and 1 GiB of
retained compressed evidence, following the existing plan. Forecast final
qualification separately using its existing policy. Do not spend the allowance
on duplicate campaigns or discard failures to meet a budget.

This authorizes engineering and an unpublished qualification candidate. It does
not authorize creating/publishing tags or releases, replacing public assets,
deploying the website, repository-setting changes, contacting anybody, or
creating/editing/commenting on PRs, issues or discussions. Prepare concrete
release/claim/outreach proposals for later review. A1/A2 are not this task.

Preserve unrelated user changes, including the newly saved Actions preference in
AGENTS.md. Inspect the actual branch, worktree and remote before changing them.
Do not force-push, reset user work or overwrite historical evidence. Progress
autonomously within this boundary; ask only for a genuinely missing decision or
external prerequisite that affects mandatory work. Complete independent work
while a dependency is unavailable. Report any automatic approval rejection with
the exact action and reason if no safe authorized route remains.

## Read first and establish the baseline

Read AGENTS.md, README.md, roadmap.md and these current sources:

- docs/plans/engineering-readiness.md
- docs/plans/execution-contract.md
- docs/plans/real-world-scenarios.md
- docs/plans/operational-checklists.md
- docs/plans/product-focus.md and decision-register.md
- docs/plans/release/06-qualified-release.md
- docs/validation/e0-experiment-freeze-2026-09-26.md
- docs/validation/e0-evidence-reconciliation-2026-09-26.md
- docs/validation/e1-e2-native-readiness-2026-09-27.md and its linked ledgers
- docs/validation/e2-unix-eof-candidate-2026-09-27.md
- The existing R6 qualification record, source scripts and workflow definitions.

Resolve current status from the actual checkout and root roadmap. E0–E2 were
accepted and pushed to main at b736ca355ab37e563ff6abd6b8f32a681209ac67; all
post-push native checks passed. This is provenance, not permission to assume the
checkout has never changed. Published v0.4.0-rc.1 is unchanged. The later Unix
PTY ownership repair is an unpublished engineering candidate, not final-byte
qualified. Do not reopen accepted E0–E2 wholesale; rerun checks invalidated by
new changes.

Preserve these known limits: micro's wide Snow/stale-cell probe failed on native
Linux/macOS; the basic café/λ probe does not replace it. Posting query-edit
semantics remain unisolated. The selected Lazygit comparison still loses on
runtime, with a long first-positive-assertion wait whose cause is not isolated;
create-vite approximately ties Atago on the measured route. Termless's Windows
menu PTY works but cleanup is unqualified; Linux/macOS feasibility is unknown.
Human authoring/diagnosis effort and interactive screen-reader usability are
not established by existing automated timings. Do not turn these into passes.

GitUI 0.28.1 and television 0.15.9 are the frozen, operator-designed holdouts.
Read definitions to check admission, but do not execute or use fresh outcomes
to tune E3/E4. Their historical corpus presence limits independence; say so.

Start with a short checkpoint record: user-visible behavior, exact source and
binary identities, acceptance cases, public contracts touched, native hosts,
prerequisites, exclusions, expected effort and reviewer/self-review status.
Only one implementation behavior may be active at a time. This phase permits
one selected terminal-compatibility family and, conditionally, one authoring/CI
convenience family. Correctness repairs take priority; no speculative rewrite,
parallel orchestration feature, cloud dependency or Gametestr expansion.

## E3 — investigate and close one valuable terminal fidelity boundary

Begin with the retained MICRO-08 wide Snow/stale-cell failure. Reproduce on native
Linux and macOS with the pinned micro target, exact input bytes, fixed geometry,
UTF-8 locale, configuration and hashes. Preserve the original failure and any
new first attempt. Check fixture/input encoding before blaming rendering.

Establish independently justified expected cells and cursor positions using
authoritative terminal semantics, a reference terminal capture or a reduced
target with explicitly reviewed behavior. Emulator disagreement alone does not
identify a defect; do not majority-vote implementations or normalize away the
wrong cell. Separate application behavior, terminal-emulator behavior, encoding,
locale, capture timing, fixture errors and unsupported contract assumptions.

Use the frozen fzf wide/combining/repeated-resize companion and appropriate
primary applications to probe multilingual filenames, wide text beside cursor
or selection, combining marks, repeated shrink/grow, paste into editor/wizard,
and terminal queries. Pin versions and expected behavior before execution.
These are investigations, not automatic promises of new key/mouse/style support.

Reduce one demonstrated valuable failure. Choose the smallest justified option:
a local fix; a bounded dependency change behind the session interface; or an
explicit evidence-backed unsupported boundary. A dependency change needs an ADR
covering license/notices, maintenance, security history, Go/standalone behavior,
resource/output bounds, all three native hosts, migration and alternatives.
Do not claim universal Unicode, emoji or grapheme support from one repair.

For a fix, prove the relevant externally observable regression fails before and
passes after, then run the real interaction with meaningful negative and
unchanged-spec recovery controls. Check rendered screen, cursor, input encoding,
resize, alternate screen and process lifecycle where affected. Keyboard changes
need exact encoded-byte and lifecycle evidence. Preserve existing supported
behavior; narrowing scope cannot silently hide a regression.

Run appropriate real PTY/native integration, Go tests/vet and race checks after
concurrency/lifecycle changes, plus the manual example. Check natural exit,
last-moment output, redraw, timeout, cancellation, flood and descendants where
affected. Keep product timeouts, final drain, output limits and cleanup intact.
Update the terminal contract, support table, examples/migration notes and evidence.

Budget: 2–3 focused days of investigation, optionally 3–5 for one justified
family. If two days do not reduce the blocker, document the hypothesis and
choose a bounded next step or evidence-backed deferral rather than broadening
the implementation indefinitely. Record actual effort; do not invent time.

E3 exits with one repaired real failing task and its controls/native checks, or
a documented investigated deferral specifying exclusions, workaround, impact,
owner and revisit trigger. Explicitly distinguish accepted investigation from
implemented support. Then continue to E4 under this authorization.

## E4 — reproduce authoring, maintenance, diagnosis and installation

Using the intended candidate binary, complete four clean-directory walkthroughs:
selector, stateful wizard, editor and repository tool. Prefer the accepted fzf,
create-vite, micro and Lazygit journeys and reuse their independent state
oracles. Follow documented commands rather than hidden agent knowledge. Record
every undocumented prerequisite or hint and repair the docs or smallest cause.

Measure prerequisites, installation, first meaningful test, intended defect,
diagnosis and recovery separately. Count edits, commands, helper files/lines,
unsuccessful attempts, baseline changes and operator hints. Distinguish automated
wall time, tool execution, active engineering effort and human walkthrough time.
Do not label model execution time as human first-use effort or reconstruct
missing historical authoring minutes from guesses.

For each walkthrough, rehearse reviewed baseline changes and two real maintenance
changes, using actual pinned target upgrades when practical or separately labeled
reviewed synthetic UI/behavior changes. Preserve the first unmodified-spec result,
show the legitimate repair, and recheck meaningful defect detection/recovery.
Count all oracle, fixture, adapter, helper and cleanup work, not only spec lines.
Unchanged expected state must remain independently checked. Existing E1 synthetic
maintenance evidence may inform design but does not magically supply a second
change, human time or actual upstream upgrade evidence.

Compare total documented effort with the strongest applicable pinned alternatives
on at least two primary journeys. Use equivalent tasks, state oracles and cleanup
semantics, counting all glue. Record task-level wins, ties, losses and unknowns.
Demonstrate a meaningful advantage on two primary real journeys if the evidence
supports it; otherwise leave the differentiation gate explicitly unmet. Do not
invent a scoring scheme after seeing results or hide the Lazygit speed loss.

Exercise six diagnosis classes: target logic defect, bad spec, missing target or
runtime, assertion timeout, wrong exit, and cleanup/artifact failure. Define the
expected root cause before injection. Preserve product exit/category/step,
independent state, final useful screen and separate primary/cleanup errors.
Target correct diagnosis within two minutes per operator rehearsal; a fast wrong
answer fails. Delay diagnosis or conceal the injected variant where practical;
otherwise state familiarity and prior knowledge. An automated evidence inspection
is useful but is not a blinded human timing result.

Test offline report viewing and keyboard navigation; paths with spaces; failed
install; rollback; stale PATH; interrupted upgrade; archive extraction/version/
hash/layout; and documented source/archive/action routes on their claimed native
hosts. Check required test-level events and skips, not aggregate exit zero.
Inventory exact test names at the current revision. Ensure PowerShell exists
where installer checks require it. A local source setup-action check does not
prove an immutable external consumer action. New unpublished bytes cannot be
claimed to work via a public release URL.

Audit README, docs, examples, trial entry points and copy-paste commands for stale
version/action claims and source-only features. Keep qualified public release
instructions distinct from candidate instructions. Use existing installed-byte,
schema/report and installation failure gates rather than adding another public
format or installer channel.

Complete keyboard checks and, if an appropriate human/operator and environment
are available, an actual interactive screen-reader walkthrough from installation
through report to next action. Browser accessibility trees or scripted inspection
alone cannot close human screen-reader usability. If unavailable, finish other
work, retain the gap with owner and exact follow-up, and explicitly exclude broad
accessibility claims in E5. Do not manufacture a participant or purchase devices.

Add one authoring/CI convenience family only after two repeated real workflow
failures or one documented necessary ingestion consumer justify it. Prefer small
template/doc assistance or a narrow exporter; otherwise explicitly choose no
new family. No recorder/orchestrator/masking expansion without the stated trigger.

Budget: 3–4 focused days. E4 exits with four reproducible walkthroughs, six
correctly classified failure classes, two maintenance changes per chosen
walkthrough, honest effort comparisons, installation/documentation evidence and
presentation gaps disposed of under the permitted scoped boundary. Independent
first-use/adoption remains A1. Continue to E5 when entry gates are met.

## E5 — holdouts, immutable final bytes and readiness decision

Do not run the final expensive campaign during ordinary development. Enter with
accepted E0–E4 records and no unresolved correctness blocker in advertised scope.
First run HO1 GitUI stage/unstage with exact index/worktree bytes and HO2 television
filter/select with exact selected-record output, using their frozen definitions.
Run each on at least one actually supported native host: five fresh good attempts
plus a meaningful target-code defect and unchanged-spec recovery. State whether
a pilot is separate from the five-good denominator. Preserve the first result
without tuning in advance.

If a holdout reveals a defect, retain it, reduce/fix the cause and label subsequent
use contaminated. The protocol permits at most one replacement cycle; freeze
any justified substitute before execution. Do not shop for indefinitely passing
tasks. Operator-designed holdouts do not prove independent customer adoption.

Before freezing, settle all code, dependencies, build inputs and contract choices.
Select and justify an explicit unused candidate version under the repository's
version policy; inspect local/remote identities rather than using the release
workflow's v0.1.0 default. Record the embedded version before qualification.
Creating or publishing a tag/release remains unauthorized. If a maintainer
decision is genuinely needed, present the concrete audited recommendation.

Freeze a clean immutable commit, toolchain, dependencies/locks, build flags,
embedded version, target manifest, specs, fixtures, oracles, baselines and support
matrix. Build once per advertised native host and retain those exact executables;
record SHA-256 and package those same bytes with README/license/notices. Record
archive hashes and exact members. Extract into paths with spaces and prove
executable hash/version equality. No rebuild during qualification or promotion.

Reuse evidence only under the execution-contract invalidation table. New runner
code, dependencies, compiler, flags or embedded version means new executable
identities and required qualification. Identical executable hashes permit reuse
only for the original tested boundary; changed packaging still needs its gates.
Documentation-only changes need relevant link/command checks, not automatically
another 3,000 attempts. Do not attach old RC evidence to rebuilt stable bytes.

Apply R6-F/R6-Q/R6-K to the unpublished candidate, not R6-P/publication. Execute:

- Native source tests/vet, required race checks, real PTY lifecycle and manual
  examples; test-level event/skip inventory and honest mapped-risk counts.
- Contract compatibility: preserved v1, opt-in v2, CLI/schema/docs/report agreement,
  minimum versions and bounded rejection by unsupported/strict readers.
- Exact archive layout, integrity, native extraction and installed-byte identity.
- The existing admitted 120-workflow host matrix, independent postconditions,
  intended negatives and recovery using the extracted frozen binaries.
- The final 3,000 selected first-attempt executions under the existing R6 policy,
  exact executable hashes and complete ledger. Do not count this twice as both
  11-C and R6-Q, or inflate repeats into distinct workflows.
- Existing 15 project controls, retaining E0's classification of executable-code
  defects versus changed-input/fixture controls. Never relabel all 15 as genuine
  code bugs. Keep new real-target controls separately counted and attributed.
- Installer source success, invalid/corrupt/interrupted failure paths, stale PATH
  and upgrade preparation; compatible old/public v1 behavior versus candidate
  v1/v2, reviewed baseline preservation and bounded failure.
- Cancellation, final output, hangs/floods, descendants and managed cleanup;
  report v1/v2/offline behavior, primary versus cleanup failures, safe paths,
  bounded evidence and privacy limits.
- Relevant suite wall time, artifact bytes, sampled CPU/RSS and drift/survivors,
  preserving E2 sampling limitations and distinguishing n=1 large-suite cells
  from statistically replicated claims.

Inspect logs and actual artifacts for every required host. A configured workflow,
green job with mandatory skipped tests, cross-compilation or WSL is not equivalent
native runtime proof. Retain every unexpected first failure, classify infrastructure
versus target/harness/runner faults, fix the smallest cause, and refreeze/rerun
invalidated evidence. Never retry until green and discard the original result.
No unresolved false pass, wrong advertised result, destructive cleanup, unbounded
execution/output, managed leak or broken advertised install can be waived.

New public-download and immutable published-action candidate checks remain
pending until a separately authorized release exists. Test the currently public
version's route where relevant without claiming it installs the new candidate.
Prepare exact publication and post-download verification commands and checksums,
but do not dispatch workflows that publish/deploy as a side effect.

Budget: 2–3 focused engineering days plus native queue/campaign time. Close E5
with a private evidence packet and one clear recommendation: technically ready
for a scoped trial; one named blocking repair; or a narrower/repositioned product.
A qualified unpublished candidate is ready for a release decision, not verified
public availability. Mark differentiation unmet if two meaningful real-task
advantages were not demonstrated; do not claim universal superiority or reopen
endless benchmarking. Independent demand, comprehension and retention remain
unknown pending separately authorized A1.

## Evidence, verification and final handoff

Use dated Markdown records and bounded machine-readable attempt ledgers. Each
required cell records source/dirty or patch identity, executable/archive hashes,
embedded version, toolchain/flags, exact target/runtime/package pin, native image/
OS/architecture, locale/dimensions, spec/fixture/oracle/baseline identities, UTC
start/end, expected category/step/state/cleanup, actual results, attempt denominator,
artifact references and disposition. Keep skips, exclusions, unavailable evidence
and first failures visible. Seeded product failures remain nonzero in their
reports even when their intended detection passes the campaign expectation.

Use synthetic fixtures and sanitize retained evidence. Do not upload secrets,
ambient environment values or private target state. Bound retention, preserve
useful final evidence, and record artifact digests before expiry. Do not equate
zero observed survivors or sampled RSS with proof about every possible process.

Format changed Go files. Run appropriate repository checks, including go test
./..., go vet ./..., native race checks and the Windows scripts/test-race.ps1
with its actual compiler prerequisite. Build the demo and execute the menu and
menu-exit examples when execution changes. Capture exit codes and required tests
actually run. Verify changed public contracts, docs, schemas, examples and
migration together. Never shorten product deadlines to pass instrumentation.

Update roadmap, engineering-readiness status, decision register, support/claim
tables and evidence index as each checkpoint is genuinely accepted. Preserve
historical snapshots and existing E0–E2 acceptance. Measure actual effort against
estimates where available; label unknown human time rather than fabricating it.
Keep progress updates concise and regular during implementation and CI waits.

At the final push, inspect the diff, confirm all intended changes and preserved
user edits, and verify no release/deployment side effects. Monitor post-push
ordinary CI and fix actual failures. Do not create a PR or publish a release.

Finish with: E3/E4/E5 status and exact acceptance boundaries; what changed and why;
source and per-host final executable/archive identities; qualification denominators
and CI/artifact links; task-level wins/ties/losses/unknowns; correctness, cleanup,
installation and accessibility limits; actual costs; final commit/branch and clean
or remaining-worktree status; and the concrete release/claim/outreach proposals
for the user's later decision. If a mandatory gate remains blocked, say exactly
which one and why instead of declaring all milestones complete.
