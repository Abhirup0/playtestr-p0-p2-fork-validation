> ARCHIVED on 6 October 2026. Historical context only; do not execute this plan. The [current roadmap](../../../../roadmap.md) supersedes its scheduling, gates, and scope.

# Execute the next qualified Playtestr release

Prepared 1 October 2026. Creating this document does not start execution.
When the user explicitly instructs you to execute this prompt, the requested
scope includes implementation, necessary source pushes to main, standard
GitHub-hosted validation, publishing the qualified prerelease, and verifying
its public downloads. Outreach and marketing are prohibited throughout.

## Objective and starting point

Make the completed wide-character repair available in a new, verified
download for Windows amd64, Linux amd64 and macOS arm64. Finish the complete
release cycle, including checking the actual public files after publication.

The repair is on main at `07b304bb32aab9d064e7109733c244ab91766899`, including
the website evidence-link repair. Native terminal and integrated hardening
checks passed. The downloadable v0.4.0-rc.2 does not contain this repair.
Development test results do not qualify a newly versioned executable.

Read AGENTS.md, README.md, roadmap.md, docs/plans/execution-contract.md,
docs/plans/release/06-qualified-release.md, docs/plans/operational-checklists.md,
docs/wide-character-decision.md, docs/validation/wide-character-2026-09-28.md,
and the previous rc.2 qualification/publication records before acting.
Inspect the current branch, remote state and working tree; preserve user changes,
including AGENTS.md and docs/plans/e3-e5-execution-prompt.md. If the repository
has advanced, audit the differences before selecting the frozen source.

## 1. Prepare and freeze the candidate

- Review release scope, contracts, notices, dependencies, installation examples
  and the selected CJK snapshot migration. Retain v1/v2 compatibility and the
  remaining combining-cluster, emoji/ZWJ and terminal-query exclusions.
- Prefer `v0.4.0-rc.3` only if remote tags and releases confirm it is unused.
  Otherwise select the next unused coherent prerelease. Verify novelty again
  immediately before publication. Keep existing stable and prerelease assets
  and tags immutable; do not promote the new candidate to stable.
- Audit existing release/readiness workflows and scripts. Reuse their qualified
  mechanisms, removing candidate-specific hardcoded identities where necessary
  without weakening their checks. Never dispatch a workflow that publishes
  automatically before qualification has completed.
- Freeze a clean immutable source commit, chosen embedded version, pinned
  toolchain, dependencies, build flags, target versions, fixtures, independent
  oracles, reviewed snapshots and support scope before the long campaign.
  Use Go 1.26.0 if still appropriate to the audited build inputs; record any
  justified change and apply the evidence invalidation rules.
- Build once on each advertised native host. Record executable hashes, package
  those exact binaries with the required docs/licenses/notices, and record
  archive hashes and members. Extract into paths with spaces and verify hash,
  version and lightweight installed behavior. Preserve these candidate bytes.

## 2. Qualify the exact frozen files

- Run required native source tests, vet, relevant race checks, manual examples,
  lifecycle/output-cap/cleanup and installer gates. Inspect individual required
  test events and skips, not just command exit status.
- Exercise extracted candidate binaries through the admitted 120-workflow host
  coverage, 15 classified negative controls and recovery, affected terminal
  families, representative unchanged families, report v1/v2 and offline HTML.
  Preserve actual host distinctions; do not invent a 120-by-three native matrix.
- Independently verify the original MICRO-08 saved-file result and selected
  wide-cell cursor, overwrite, erase, wrapping, split UTF-8, resize and alternate
  screen behavior. Apply existing reviewed snapshots; any additional migration
  needs independent justification and preserved old/new evidence.
- Execute the required 3,000-repeat campaign on the new exact executable hashes,
  retaining every first attempt, timeout, mismatch, oracle and cleanup outcome.
  Follow the existing frozen scenario/host distribution and holdout protocol.
  State when previously used holdouts are regression cases rather than newly
  unseen evidence. Do not invent replacement holdouts to inflate claims.
- Check exact-version source-action installation, corrupt/interrupted download
  behavior, native archives, upgrade preparation, baseline preservation and
  installed pass/intended-failure/recovery. Reuse identical-byte evidence only
  where the execution contract permits it.
- Forecast campaign cost and evidence size before launching. Use ordinary
  GitHub-hosted runners; no paid runners, billing changes or new service spend.
  Reuse existing bounded retention and timeouts. Record actual cost and limits;
  never silently reduce required coverage to fit a budget.

If a gate fails, retain the failure, identify whether it is a target defect,
runner defect or harness problem, reduce and repair it, then refreeze and rerun
the affected gates. Do not retry away first failures, automatically overwrite
snapshots, weaken assertions, or waive false passes, leaks, unsafe cleanup,
unbounded behavior or broken advertised installation. Native coverage requires
actual successful runs, not cross-compilation or configured workflows.

## 3. Publish and verify the downloadable release

- Prepare concrete release notes, checksums, evidence index, installation and
  upgrade instructions, migration notes and scoped limitations. Update the
  roadmap and relevant docs to distinguish source, qualified and published
  status accurately. Reuse existing demonstrations where appropriate.
- Commit/push necessary reviewed work and verify required post-push checks.
  Documentation-only changes must not accidentally rebuild qualified binaries;
  changed executable inputs require new qualification.
- Publish the new immutable prerelease using the exact qualified archives and
  checksum files. Confirm source/tag provenance and the independently pinned
  setup-action revision. Do not rebuild or substitute assets during promotion.
- Download the actual public archives/checksums on all three advertised native
  hosts and prove equality to the qualified files. Extract into paths with
  spaces; check executable identity/version and representative real-app
  pass/intended-failure/recovery, invalid input, cleanup/cancellation and report
  generation. Verify the immutable public setup action and a genuine old-to-new
  version upgrade without changing existing baselines.
- Treat any public-byte mismatch or broken installation as an unresolved release
  failure. Repair through a new version if necessary; never replace published
  bytes or rewrite tags. Preserve original failed publication attempts.
- Check documentation/download links and the website build. Website deployment
  is outside this prompt; prepare any relevant updates in the repository.

## Boundaries and completion

Do not contact anyone, post announcements, do marketing, mutate issues/PRs/
discussions, deploy the website, start adoption/commercial discovery, add cloud
services, or expand terminal features beyond an evidence-required release fix.
Independent adoption and human accessibility evidence must remain honestly
open; operator or automated runs cannot substitute for them.

Continue through all authorized steps until downloads are published and verified.
If an external approval or service failure genuinely blocks an action, complete
unaffected work and report the exact pending action and reason. Never bypass an
approval rejection. Do not claim the release complete while mandatory checks
or public-byte verification remain unresolved.

Completion requires a dated Markdown record and machine-readable evidence with
the frozen identities, native run links, archive/executable hashes, first-attempt
results, controls/recoveries, failures, exclusions, costs and verified public
downloads. Update roadmap.md to reflect the final outcome while retaining all
historical evidence. Give the user a short plain-language result: what they can
download, what changed, what passed, what remains limited and the next decision.
