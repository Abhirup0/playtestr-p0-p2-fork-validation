# 02 — Complete customer journeys

Status: planned experience, not existing CLI/API documentation. All command names below are illustrative until P0/P1 finalize them. [Product](01-product-and-positioning.md).

## J1: solo developer reaches a useful local test

Prerequisite: the developer can build and run the target with synthetic data. Playtestr does not guess a universal build command from a repository.

1. Install a pinned runner and read supported host/input limits.
2. Guided setup asks for executable/arguments, working directory, fixture strategy, viewport and expected completion. Detect common project metadata only to suggest editable choices; never execute an inferred build without selection.
3. Start recording, for example `playtestr record --output tests/terminal/create.json -- ./bin/my-cli create` (proposed syntax).
4. Interact normally. Use a separate recorder control to mark a text expectation, screen checkpoint or expected exit; recorder controls must not leak into target input.
5. Review generated steps and snapshots, including recorded text that could be sensitive. Candidate expectations are unapproved until the author confirms them.
6. Replay from fresh state. Explain failures using the step and captured evidence. Show unresolved readiness or dynamic content explicitly.
7. Commit the reviewed spec, synthetic fixture, snapshots and pinned tool configuration. Run locally with the existing test command.

Completion: the same declared workflow passes from fresh state and detects a seeded target defect without editing the test or baseline. First-value target: at most 15 minutes after the target builds, for admitted simple workflows. Record build/install time, author time and assistance separately. Operator speed is not independent usability evidence.

## J2: maintain or debug an existing test

Run the suite; open the offline report; reproduce the exact failed spec with the recorded runner/target/fixture identities. If the target is wrong, fix it and rerun with unchanged expectations. If behavior intentionally changed, regenerate only selected candidate snapshots, review the diff and commit the update. Never refresh all snapshots merely to clear failures.

A new feature requires a new workflow or assertion. A changed implementation covered by existing tests normally requires no test authoring. An untested path remains untested; a clean suite must say how many selected workflows ran, not “application verified.”

When dependencies or project versions change, capture the old/new pins and classify intentional change, target defect, flaky environment, unsupported behavior or Playtestr defect. A removed test is a coverage change, not a harmless cleanup.

## J3: enable ordinary PR checks

1. Maintainer selects a generated workflow template and enters their build/setup/test commands.
2. Review the exact workflow before committing it. The setup Action installs a runner; it does not hide the application build.
3. Select supported OS lanes and explicitly opt into any additional cost. Linux is a reasonable initial example, not a mandatory target for Windows-only software.
4. Run a passing PR, a deliberate application regression, and a recovery in an authorized test repository.
5. Configure the test check as required using repository controls when desired.

Each PR open/update rebuilds and runs committed specs. Results show selected/executed/skipped counts, exact revision, failed assertion, cleanup status, and links to evidence. A test selection of zero is a configuration error for a required suite. Hard cancellation may prevent artifact upload; display “evidence unavailable,” never success.

The workflow and GitHub project settings remain inspectable. Installation does not open a PR or mutate the repository unless that exact action is authorized. Template download/copy is the default onboarding path.

## J4: install the paid App

1. Explain paid value and show a real baseline-review example before checkout.
2. GitHub account/organization admin installs the App for selected repositories using least privileges.
3. The setup page verifies installation ownership and lists repository readiness: no workflow, no tests, unsupported report, missing permission, ready.
4. The buyer chooses the launch plan through an eligible hosted checkout. If Marketplace is unavailable, disclose the external merchant/payment route before purchase.
5. Verified payment event grants entitlement; browser redirection alone does not. Show pending confirmation with an automatic retry/reconciliation path.
6. Bind selected stable repository IDs to the entitlement. Configure reviewers and the baseline/spec/policy path set from the trusted default branch.
7. Demonstrate one passing review and one changed-baseline approval. Customer chooses required-check settings.

Acceptance: no founder-issued license, hand-entered database row, per-customer deployment, or manual invoice is needed. Unauthorized organization members cannot purchase on another account's behalf or select repositories they do not administer.

## J5: review a regression on a PR

Two outcomes are visible: **tests** and **review policy**. Tests may pass because the PR changes its own expected snapshot, while policy awaits an authorized review of that change.

Review screen: repository/PR, head and base identities, tested merge identity if applicable, suite selection, runner version, test result, changed test/baseline files, diff/artifact links, prior relevant approval and current reason for waiting. Raw terminal data stays in GitHub artifacts; private evidence links retain GitHub access checks.

Reviewer approves a defined change set at exact revisions. New head commits, base changes affecting evaluation, relevant settings changes or deleted evidence invalidate approval/results as specified in 04. The App does not auto-commit snapshots, auto-merge PRs or turn a failed test green. A self-approval policy for solo accounts is explicit and visibly weaker than independent review.

Large repos can require a distinct reviewer/team. If their membership/permissions cannot be verified with the chosen permissions, the feature is unavailable until the contract is resolved; do not silently allow everyone.

## J6: quota, outage and payment trouble

| Event | Customer sees | Automatic behavior |
| --- | --- | --- |
| Results quota reached | Usage and reset time; paid review unavailable for additional runs | Free tests continue; paid check cannot pass without evaluation |
| Missing/inaccessible artifact | Exact missing evidence and rerun instruction | Retry boundedly; then actionable failure |
| GitHub/API outage | Pending/integration-unavailable status when publication is possible | Durable retries and later reconciliation; never stale success |
| Payment confirmation delayed | Pending activation and provider portal link | Reconcile verified purchase event |
| Renewal fails | Past-due state, end of documented grace, payment portal | Dunning handled by provider; entitlement changes by verified state |
| App permission revoked | Which installation permission needs repair | Stop relevant access; recover after reauthorization |
| Service down after required-check setup | GitHub may retain pending status | Tests still run; owner can deliberately change required-check settings |

## J7: cancel, remove, export and return

Hosted portal cancels renewal with access through the paid term. Removal of the App stops GitHub access immediately; uninstall alone is not assumed to cancel provider billing, so onboarding and removal docs explain the direct cancellation path and automated reminder where permitted. Prefer linking uninstall state to a clear self-service cancellation workflow rather than silently continuing an unwanted subscription.

Export compact account/review metadata. Delete service data on the defined schedule after verified request/uninstall, while retaining only required billing records through the provider. Tests, baselines and artifacts in the customer's repository remain theirs. Reinstall uses the account/repository identities, reconciles an existing subscription and never creates a duplicate charge. Access to a transferred repository must be reauthorized for the new owner.

## Journey acceptance matrix

Every journey needs success, expected failure, timeout/cancellation where relevant, recovery, permission-denied, and unsupported-input cases. Validate private/public repos, organization/personal ownership, fork PRs, renamed/transferred repos, branch updates, deleted artifacts and loss of credentials. Accessibility includes keyboard-only recorder controls and setup/review pages, useful labels, contrast, focus order and an actual screen-reader review before claiming that path.
