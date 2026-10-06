# Execute P0, P1 and P2 to full acceptance

Prepared 7 October 2026. **Reusable execution prompt:** this file authorizes nothing merely by existing. Its instructions and bounded action permissions apply when the user explicitly sends/invokes it as the implementation task. Creating this file is documentation work only.

---

Implement the complete **P0 → P1 → P2** batch in this Playtestr repository. I am going AFK. Make routine decisions autonomously, maintain progress and evidence, and **do not stop at the end of P0, P1, a small prototype, a passing local demo, or a configured CI workflow**. Continue until all three phases satisfy their full acceptance criteria, with implementation, tests, documentation and real applicable hosted evidence.

The outcome is:

> A developer records a trusted CLI/TUI interaction, chooses meaningful checkpoints, reviews and exports an ordinary test, replays it from fresh state, commits it, runs it on a real pull request, catches a deliberate target regression, diagnoses the captured evidence locally, and recovers without weakening the test.

This instruction explicitly authorizes implementation of P0–P2 and continuation across their phase/sprint boundaries. Earlier statements that the roadmap was “plans only” describe the previous planning task; they do not prohibit this implementation. Archived plans are history and must not control the work.

## 1. Read the controlling files and establish the baseline

Read repository/nested `AGENTS.md` instructions, [the roadmap](../../roadmap.md), and [the planning index](README.md), then these plans:

| File | Required use in this batch |
| --- | --- |
| [00 — baseline](00-baseline-and-decisions.md) | Reuse inventory, limits and new-scope boundaries |
| [01 — product](01-product-and-positioning.md) | PR-first promise, free/paid separation, AI-free constraints |
| [02 — journeys](02-customer-journeys.md) | Complete J1/J2/J3; design implications of later journeys only |
| [03 — authoring](03-deterministic-authoring.md) | Entire P1 recorder/export/readiness/fixture acceptance |
| [04 — GitHub](04-github-execution-and-review.md) | P0 trust decisions and P2 free execution; paid sections are design only |
| [05 — infrastructure](05-managed-infrastructure.md) | P0 backend/free-tier feasibility, not production service construction |
| [06 — commerce](06-commercial-model.md) | P0 first-sale/eligibility/fee analysis, not checkout implementation |
| [07 — security](07-security-and-data.md) | Recording, local execution, generated workflow and fork trust boundaries |
| [08 — campaign](08-real-project-validation.md) | Future count rules; this batch does not execute the 100-project campaign |
| [09 — milestones](09-delivery-milestones.md) | Every P0.1–P0.6, P1.1–P1.5 and P2.1–P2.4 slice |
| [10 — quality](10-quality-and-release.md) | Relevant native/format/lifecycle/CI checks and evidence invalidation |
| [11 — launch](11-launch-and-operations.md) | Preserve marketing/release boundaries and self-service design |
| [12 — decisions](12-risks-and-decisions.md) | Resolve batch-relevant questions and record remaining later gates |
| [13 — sources](13-source-register.md) | Refresh unstable provider/platform facts from primary sources |
| [14 — templates](14-execution-templates.md) | Record actual slice and acceptance evidence |
| [15 — discovery](15-candidate-discovery.md) | Choose a few suitable development examples; no admission inflation |

Also read current usage/contracts: [README](../../README.md), [development](../development.md), [spec v1](../spec-v1.md), [spec v2](../spec-v2.md), [report v1](../report-v1.md), [report v2](../report-v2.md), [snapshots](../snapshots.md), [workspaces](../workspaces.md), [suites](../suites.md), [terminal compatibility](../terminal-compatibility.md), [CI installation](../ci-installation.md), [failure handoff](../ci-failure-handoff.md), and [failure reports](../failure-reports.md).

Inspect the actual code rather than implementing from prose alone: `cmd/playtestr`, `internal/runner`, `internal/terminal`, `internal/discovery`, `internal/report`, `schema`, `setup-playtestr`, `cmd/demo`, `cmd/fixture`, `scripts/ci`, existing examples, and `.github/workflows`. Locate existing seams for sessions, inputs, state, snapshots, fixture setup and cleanup.

Record current branch/commit, worktree changes and available tools. Preserve unrelated user edits, staged changes, private trial data and historical evidence. Never reset/clean the workspace or rewrite published tags/assets. Use an isolated implementation branch/worktree if necessary. Do not force-add ignored private artifacts or compiler caches.

## 2. Autonomy, action permissions and boundaries

When I invoke this prompt, local P0–P2 edits, tests, small necessary dependencies/ADRs, fixtures, documentation, bounded research and acceptance tooling are authorized. Select sensible implementation details and record rationale; do not repeatedly ask me to choose flag names, package layouts or routine techniques.

For **this batch's validation only**, invocation also explicitly authorizes the following concrete remote actions, after verifying ownership/access and first preparing the local changes for review:

- Make scoped commits and push the P0–P2 implementation to a new non-default branch `work/p0-p2-implementation` in **`Wyrcan-io/playtestr`**. If that branch already contains unrelated work, use a new uniquely suffixed branch and record the choice. Push only intended files/changes; preserve unrelated local edits. No force push, merge or default-branch push.
- Push a dedicated acceptance base branch `validation/p0-p2-base` containing the scoped candidate and workflows, and a dedicated head branch `validation/p0-p2-journey`, in that same repository. Use new uniquely suffixed names if the specified names already belong to unrelated work.
- Create **one draft synthetic acceptance PR** from that journey branch to that validation base branch, titled `P0–P2 acceptance: record, PR regression and recovery`. Its body must state that it is a temporary internal test, link the candidate identities, and request no reviewer. Update its head branch through pass → deliberate target defect → recovery → intentional reviewed baseline update. This authorizes that test PR's necessary title/body corrections and its closure after evidence is captured; do not merge it or add comments/reviews to unrelated PRs.
- For restricted-fork validation, reuse a verified fork owned by my authenticated account, or create **one fork of `Wyrcan-io/playtestr` in that account** named `playtestr-p0-p2-fork-validation` if needed. Push one dedicated acceptance branch there and create **one draft fork acceptance PR** against the same validation base branch, titled `P0–P2 acceptance: restricted fork workflow`. This authorizes updating that fork branch for the bounded pass/defect/recovery cases and closing that specific test PR afterward. No reviewer requests, unrelated comments or upstream contact. Retain the fork/branches unless deletion is separately authorized.
- Update/execute the relevant validation workflows on these branches; approve execution of these own synthetic fork runs if GitHub requires it; use **standard GitHub-hosted** Linux/macOS/Windows runners; monitor actual runs and retrieve bounded artifacts/logs. Existing public-repository standard-runner validation may proceed. Do not enable paid runners, change budgets or run on a billable private-repository route without separate permission.

These permissions are for internal acceptance, not maintainer outreach or an implementation-review PR. Do not open an additional PR to merge the product, modify any unrelated issue/Discussion/PR, send invitations, or publish marketing.

Do not publish a release/tag, change stable/prerelease channels, deploy the website or a production service, register/subscribe to a payment provider, incur new service costs, enter personal/business verification data, take a live payment, change production branch protections, or launch P3/P4. P0 can create local feasibility probes and design artifacts; it cannot silently become an App/backend/billing build.

If actual remote ownership/credentials/policies prevent the specifically authorized tests, explain the precise blocker, prepare all affected changes locally, and continue every unaffected slice. Do not invent remote success. Request only information or permission genuinely absent from this instruction, with the exact action and rule explained.

## 3. Finish every P0 slice

**P0.1 — baseline audit:** map existing functionality to reuse points; identify minimum changes; reconcile instructions and record why recorder/PR work is now in scope. Avoid rebuilding suites, report rendering, workspaces or the installer.

**P0.2 — authoring contract:** define the actual launch/setup, controls, checkpoints, cancellation, review, export and editing behavior. Produce a complete fixture-backed wizard example with generated spec, readiness and candidate snapshots. Resolve recorder hotkey collisions and the way a user sends the control key literally. Determine whether existing strict v1/v2 can express the generated result; choose/version a separate draft format only if necessary.

**P0.3 — PR contract:** freeze the head/base/tested-merge identity rules, expected workflow/report context, bounded evidence and test selection. Define future baseline/spec/policy-change review and approval invalidation precisely enough for P3 to implement later. Pick the small review surface and minimal permissions; do not implement the paid App now. Explicitly retain the limitation that customer-controlled CI is not malicious-admin-proof attestation.

**P0.4 — managed-backend feasibility:** build only local bounded probes needed to evaluate signature/crypto work, result parsing, indexed metadata queries, durable retry/atomic job design and worst allowed inputs. Use the provider's supported local runtime where available. Record measured local CPU/resource data and how it compares to current official free-tier limits; do not equate a desktop stopwatch with provider metering. Choose/justify the integration language in an ADR. If actual platform proof requires deployment, leave that correctly scheduled before P5 rather than claim deployed evidence. Resolve feasibility or document a concrete viable alternative.

**P0.5 — commerce feasibility:** refresh primary-source requirements for Marketplace, candidate merchant-of-record eligibility, fees, payout delays, cancellation/portal/refund support and no-monthly-minimum options. Separate documented plausibility from actual seller/account approval, which is a later external gate. Do not infer eligibility from timezone or invent unavailable business facts. Select a reasoned provisional first-sale path and cost model; do not block local recording on a future production verification form.

**P0.6 — freeze decisions:** write the bounded ADRs/contracts, update batch-relevant register entries, record remaining later gates with owners, and revise estimates using evidence. Explain the proposed paid value beyond a red/green comment without pretending demand has been validated. P0 completion means its scoped audit/design/feasibility decisions are supported; it does not mean production eligibility or infrastructure is already verified.

Then proceed immediately to P1. Do not end the task merely to hand back a design summary.

## 4. Implement the complete P1 recorder experience

Implement all P1 slices from 09 and the full acceptance in 03. Keep the local recorder/core in Go, accountless and offline. Reuse the session/terminal engine and lifecycle protections.

Required behavior:

- Guided setup selects explicit executable/arguments, cwd, viewport, fixture/home/temp behavior, environment allowlist and bounds. Do not guess or silently run a build command. Show resolved target/path information.
- Capture supported typing/paste/named keys and resizing through a real PTY; maintain bounded ordered events and a coherent rendered screen. Unsupported input is actionable, not silently dropped.
- Let the author mark meaningful text appearance/disappearance, expected exact exit and named snapshot checkpoints. Keep control UI distinct from target input and rendering.
- Use positive readiness evidence after relevant input/resize. Existing settling supplements it; wall-clock pauses, stale prompts or quiet output cannot become the sole readiness criterion.
- Review candidate steps/baselines, edit/remove/reorder or rerecord the supported selected portion as the decided contract permits, and reject unresolved invalid states before approved export. Provide a practical maintenance path; one raw capture prototype is not full P1.
- Replay from fresh synthetic state with the same test runner; preserve the first failed attempt and diagnose it. Validate relevant saved/file/Git state using the existing bounded harness or a justified minimal extension with a documented lifecycle.
- Export readable editable ordinary tests and reviewed snapshots transactionally. No partially accepted export on cancellation/failure, silent overwrite or automatic refresh of all existing baselines.
- Restore operator terminal modes/cursor/screen as appropriate on success, error, cancellation and forced shutdown. Every background worker has a bounded shutdown path.
- Keep capture memory bounded and avoid automatic secret-bearing draft/raw-log persistence. Preview exported text; do not claim that a target cannot print secrets.
- Preserve existing manual authoring and strict contracts. New schema/action semantics require validation, reader/writer/examples/docs/migration changes together; no unknown fields added casually.

Prove the recorder using wizard, selector, full-screen, resize and stateful examples. They may overlap where one app supplies several useful behaviors, but show each distinct capability. Include at least one independently maintained pinned external application, with a real useful interaction and synthetic fixtures, alongside deterministic internal helpers. This is limited development evidence, not the later 100-project campaign or maintainer adoption.

For each selected example demonstrate reviewed generated test → fresh pass → deliberate target behavior defect detected with unchanged test/baseline → recovery. Run at least ten fresh replay attempts with delay variation, preserve initial failures, and prove manual edit/rerun without the recorder.

Required failure coverage: unsupported keys/encoding, oversized paste/events/output, invalid dimensions/path, duplicate snapshot names, unready/ambiguous checkpoint, stale anchor, dynamic output, dirty fixture, unexpected exit, expected nonzero exit, hang, flood, cancellation, interrupted export, blocked input, descendant cleanup, terminal restoration and cleanup failure preservation. Test relevant native input behavior rather than proving it only with mocks.

Then proceed immediately to P2. Do not stop after a working wizard or local tests.

## 5. Implement the complete P2 free GitHub workflow

Implement P2.1–P2.4 and J3, using existing setup Action, summary helper, reports and failure handoff where suitable.

- Provide a practical generator/guided setup for a reviewable workflow based on explicit build, target prerequisite, suite and OS choices. Finalize command names during P0; do not present illustrative syntax as already supported. Do not hide application installation/build inside the setup Action.
- Pin Action and runner identities independently; verify the selected install. Since the new recorder is not in an old published release, distinguish new candidate-source validation from existing published-runner compatibility. Test the actual changed candidate; do not obtain green results by running only rc.3. Use a documented pinned source/candidate-build path on validation branches without publishing a new release or promising an unreleased downloadable version.
- Run declared PR events with consistent head/base/tested identity. Record runner, target, fixture and suite identities needed for reproduction. Avoid unsanitized GitHub expressions in shell commands.
- Preserve the test's nonzero result through HTML/summary/upload work. Bound metadata/artifacts and retain useful screen/diff/cleanup evidence. Zero selected tests, malformed specs, missing snapshots and setup failures cannot become green tests.
- Show an accessible summary with selected/executed/skipped counts, exact revision, failed step/category, cleanup state, artifact links and ordinary local rerun instructions. Label evidence missing after hard cancellation/expiry rather than manufacture a report.
- Keep fork execution restricted to ephemeral `pull_request` jobs with read-only permissions and no App/payment credentials. No privileged `pull_request_target` execution of fork code, no secret-bearing self-hosted route and no paid App/comments needed for basic evidence.
- Handle superseded runs, cancellation, absent report/helper/target dependencies, invalid workflow inputs and no-artifact cases accurately. No retry policy hides an initial regression.
- Document supported events, OS choices, tool/build prerequisites, Actions billing separation, artifact retention/access/expiry, required-check configuration and complete removal. Make limitations such as merge-queue support explicit.

Using the authorized test branches/PRs, execute and capture:

1. A passing recorded workflow in a real PR.
2. A source/configuration defect in the target that produces a real red check and preserved failure evidence, with unchanged test/baseline hashes.
3. Retrieval of that exact failure context and successful local reproduction.
4. Recovery by fixing/reverting the target defect while retaining the test/baseline.
5. An intentional behavior change followed by selected, visibly reviewed baseline maintenance and passing replay/CI. P2 proves ordinary human Git review; paid policy enforcement belongs to P3.
6. A passing and deliberately failing restricted fork run demonstrating the absence of service secrets/write-token requirements.

Record real run IDs, PR identities, commit associations, artifact hashes, actual outcomes and cleanup. Workflow YAML, mocked events, a dispatch-only run and an old unrelated green run cannot substitute for the required PR evidence.

## 6. Validation and acceptance gates

Run relevant checks after coherent changes; fix findings rather than weakening assertions or excluding failures. At minimum, where applicable:

```powershell
go test ./...
go vet ./...
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\test-race.ps1
go build -o bin/demo.exe ./cmd/demo
go run ./cmd/playtestr test examples/menu.json examples/menu-exit.json
```

Format changed Go files. Run existing/new Python helper tests and relevant workflow validation if those files change. Add meaningful tests for recorder logic and lifecycle, export transactions, compatibility and generator/summary behavior. Mocks are suitable for pure policy/protocol logic, not substitutes for real PTY execution.

Obtain actual native Windows amd64, Linux amd64 and macOS arm64 evidence for the changed recorder/lifecycle paths using standard hosted runners where needed. Missing local devices/SSH hosts are not blockers. If a race compiler is absent, use a supported native validation route; record any still missing check honestly. Test-only deadlines can accommodate instrumentation; product deadlines cannot be loosened just to make CI green.

Review concurrency, terminal restoration, process-tree handling, hostile paths, stale state, privacy and sensitive-data propagation. Keep first failures, unsupported behavior and corrected harness errors in the record. Compare relevant hashes before/after mutation/recovery. Validate docs/schema/example parity and local links.

P0–P2 are complete only when all of these are true:

| Gate | Required evidence |
| --- | --- |
| P0 decisions | Every P0 slice has a supported conclusion; later account/deployment/demand gates explicitly separated |
| P1 whole journey | Setup/capture/checkpoints/review/fresh replay/export/maintenance all work as documented |
| P1 coverage | Wizard/selector/full-screen/resize/state and relevant adverse paths proven; external example and repeated replay evidence |
| Native/lifecycle | Exact changed paths actually pass supported native checks, bounded cleanup and race checks where required |
| P2 generation | Explicit choices produce a reviewable working workflow with exact candidate/install semantics |
| P2 real execution | Main acceptance PR and restricted-fork pass/defect/recovery evidence; no secret/write-token dependence |
| P2 diagnosis | Actual failed CI evidence is retrieved and reproduced locally; recovery does not weaken expectations |
| Maintenance/docs | Selected intentional updates, migration/limitations/removal instructions and public behavior parity |
| Scope/evidence | No P3/P4 build, release, marketing, unsupported compatibility or adoption claims |

No mandatory gate becomes “done” because a plan describes it or because it is inconvenient to run. Do not claim all three complete while real PR/native proof is missing.

## 7. Persistence, progress and handoff

Keep a concise live phase/slice checklist and dated evidence record under `docs/validation/`; update the roadmap and decisions with actual statuses. Distinguish implemented, locally tested, natively verified and hosted PR verified. Keep provisional versus final-campaign project counts intact.

Send concise progress updates during long work. Context compaction, an intermediate passing test, nominal sprint boundaries, earlier planning estimates and an opportunity to ask “shall I continue?” are not reasons to stop. Continue through the complete P0–P2 batch and fix regressions discovered in integration.

If a real external blocker remains after reasonable alternatives, continue independent work, document exact failed attempts and the minimum missing input/action. Do not claim completion or create permanent polling loops. Respect system limits and explicit user stop instructions. Preserve a precise resumable checkpoint if execution must be interrupted for those reasons.

Once all gates pass, provide one self-contained final report: delivered commands/workflow, actual example, files/ADRs, native/race/PR evidence links, original defect/recovery evidence, remaining documented limits, P0 later external gates, scoped commit/branch identities and the next phase. Do not launch P3 or marketing. The preferred final state is **P0 accepted, P1 accepted, P2 accepted**, each backed by its own proof.

Start with the baseline audit now, then continue until the batch is fully accepted.
