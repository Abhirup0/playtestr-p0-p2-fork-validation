# 04 — GitHub execution, review and provenance

Status: planned contract. [Existing CI guide](../ci-installation.md) · [Security](07-security-and-data.md).

## Two checks, two questions

1. **Playtestr tests:** did the selected committed workflows pass against the tested build?
2. **Playtestr review:** were relevant test-contract/baseline changes explicitly approved under the configured policy for these revisions?

The App never overrides a failed test check. Baseline approval does not make an assertion mismatch pass. PRs can change their own tests, so passing test output alone cannot answer the second question.

GitHub Actions runs builds/tests on customer-owned capacity. The backend handles installation, result metadata and review state. The App has no facility to execute a submitted command or clone/build a customer's repository.

## Free execution workflow

- Trigger configured PR events and pushes as documented; cancel superseded runs using repository/PR-scoped concurrency when appropriate.
- Pin setup Action and runner identities separately. Customer explicitly owns application dependency installation/build commands.
- Use the selected PR head/merge strategy consistently and record both head/base and actual tested commit. Default to GitHub's merge commit for PR testing, while displaying that distinction.
- Select the suite before launch; empty required selection, invalid specs and missing baselines fail visibly.
- Run tests with bounded time/output; preserve original exit status through summary/report/upload steps.
- Upload only bounded admitted evidence. Reports remain GitHub artifacts with documented retention; an expired artifact is unavailable, not a cached success.
- Never use automatic retries to convert unexplained test failures into a clean first-attempt result.

The initial template does not include merge queues, reusable-workflow matrices or self-hosted runner support unless separately qualified. Required-check users need an explicit supported event list; document merge-queue limitations before enabling enforcement.

## Paid result ingestion

Preferred P0 prototype: GitHub App receives signed installation/PR/workflow events and obtains authoritative run/repository/commit metadata through GitHub's API. Fetch only a small versioned result manifest from the allowlisted completed workflow. Avoid customer-stored App secrets and avoid a privileged postprocessor executing fork artifacts.

Publish that manifest as a separate bounded artifact so the backend never downloads a large screen/report archive to find it. Enforce compressed and decompressed byte limits, member count, file-name allowlist and redirect destinations before parsing. Raw failure evidence remains a separate customer artifact linked for review.

Treat all result data as untrusted. Bind a result to stable installation/account/repository IDs, workflow identity, event type, PR number, head/base SHA, tested SHA, run ID, attempt number, artifact identity/digest, runner version and suite/contract digest. Repository names and branch strings are display labels, not tenant keys.

The service verifies repository ownership, selected-repository entitlement, run completion/conclusion, approved workflow path/configuration and consistency with current PR state. Validate schema, counts, bounded fields and known status values. A forged or mismatched manifest produces an integration error, never success.

A successful GitHub job is still customer-controlled execution, not cryptographic proof of application correctness. A malicious repo administrator can alter code/policies or remove required checks. Even untrusted target code can interfere within its job. The launch App provides regression workflow integrity within a documented repository trust model; do not market it as adversarial supply-chain attestation.

## Contract-change inventory

P0 defines a trusted configuration containing spec/fixture/baseline paths, suite selection, workflow/build configuration and policy version. Start with explicit path sets rather than guessing dependency graphs.

Compare the relevant trusted base state with the PR's proposed state. Detect additions, removals, renames, widened exclusions, changed snapshot data, changed assertion/input actions, altered fixture content, workflow changes and modified selection. Explain which changed files require review. A deleted test or removed snapshot is not automatically exempt.

No relevant changes + a complete valid current test result may satisfy review policy automatically. Relevant changes need explicit approval. If the policy file itself changes, evaluate that change using the prior trusted policy; a PR cannot approve itself by weakening its policy.

## Approval contract

Approval identifies reviewer GitHub ID, verified role, repository/PR, head/base/tested identities, policy version and digest of the reviewed change set. Default team policy excludes the PR author. A personal-account mode can permit explicit self-approval but labels it accurately. No claim of independent review in that mode.

Choose between an authenticated minimal App review page and a narrowly defined GitHub-native review event during P0. Commands hidden in arbitrary comments are not accepted as approvals by default. Role membership is checked at approval and when applying the result; a revoked reviewer cannot supply new approvals.

Changes that invalidate evaluation: head update; base update affecting the tested merge/contract; relevant configuration/policy change; selected suite change; result/artifact identity change; run attempt supersession; reviewer permission change where policy requires it. Conservatively require reevaluation when uncertain. Do not reuse approval merely because the PR number is unchanged.

Approving proposed baselines does not write repository content. Developer commits the reviewed update, reruns tests and obtains an approval valid for that final change set. UI must explain why a previous approval became stale.

## State machine

| State | Entry | Allowed transition / displayed action |
| --- | --- | --- |
| Awaiting run | Eligible current PR, no matching completion | Await CI; never publish success |
| Evaluating | Matching run and bounded manifest available | Verify context and changed-contract inventory |
| Tests failed | Valid run reports failure | Link exact evidence; fix target/test intentionally |
| Awaiting review | Tests pass; relevant changes need approval | Show changed files and authorized review action |
| Satisfied | Current valid tests and required approval | Success for exact evaluated revision |
| Superseded | New head/base/attempt/policy | Invalidate prior success and evaluate current context |
| Unavailable | Missing artifact, API outage, bad schema, quota or entitlement issue | Pending then actionable non-success after deadline |
| Removed | Uninstall/repository removed | Stop access/publication; explain required-check cleanup |

Bound evaluation to a planned 15-minute retry window after workflow completion. Distinguish a run that has not completed from a service attempt that timed out. A full backend outage may prevent publishing an updated check; GitHub can retain pending/stale visible information, so consumers must bind required checks to the current revision.

## Fork and privilege boundary

Run untrusted PR code in restricted ephemeral `pull_request` jobs without service secrets. Keep App credentials exclusively in the backend. Do not switch to privileged `pull_request_target` and then execute fork code to gain comment permissions. A trusted publisher may read artifacts as data only. See the [GitHub primary source](https://docs.github.com/en/actions/reference/security/securely-using-pull_request_target).

The App fetches metadata using its own installation context after checking the event/run relationship. Never accept artifact-provided URLs, commands or repository IDs as authority. If a required fork relationship cannot be proven by the supported API path, show unsupported/pending with a clear reason rather than weakening access rules.

## Acceptance scenarios

Pass, application regression, intended snapshot change, deleted assertion, zero tests, malformed/truncated manifest, artifact expiration, duplicate and reordered events, force-push, PR close/reopen, base change, run rerun/cancel, missing privileges, uninstallation, repository rename/transfer, unauthorized approval, author self-approval, stale reviewer membership, quota exhaustion, billing lapse, GitHub throttling and backend recovery.

For all cases assert which revision gets which check and whether a write occurs. Instrument idempotency: duplicate deliveries create one logical result/check update, not an expanding comment trail. The launch default is checks plus one stable summary; comment spam is not a feature.
