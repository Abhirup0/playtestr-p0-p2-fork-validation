# 14 — Templates for future execution evidence

Templates only. Empty entries mean unknown/not run, never passed. Store completed future records under a dated validation/campaign location; do not mark this planning set as executed.

## Slice record

| Field | Value to record |
| --- | --- |
| Phase/slice ID and date | |
| Source base and existing working-tree changes | |
| User-visible acceptance statement | |
| Dependencies/decisions closed | |
| Implementation/format/docs changes | |
| Success, expected failure, timeout and cleanup commands | |
| Native OS/architecture and tool identities | |
| Actual outcomes, first failures and artifact links/hashes | |
| Manual example and observed result | |
| Risks, exclusions, cost and next decision | |
| Status | planned / in progress / accepted / blocked / deferred |

## Project admission and result record

| Field | Value to record |
| --- | --- |
| Project ID, canonical upstream URL, distinctness rationale | |
| License, pin, integrity, dependency/build instructions | |
| Primary category, language/framework, full-screen/prompt/state dimensions | |
| Host cells and evidence status per cell | |
| Fixture, environment, viewport, external resource/disposal policy | |
| Three workflows and meaningful expected outcomes | |
| Recorder-generated output, manual edits and authoring effort | |
| Independent state oracle and negative oracle check | |
| Target mutation or historical good/bad pair, patch/hash and symptom | |
| Unchanged spec/baseline hashes for defect/recovery | |
| CI/App identities, actual PR event and reviewer-policy proof | |
| Ten fresh attempts per workflow/cell; first failures retained | |
| Artifact paths/hashes and availability deadline | |
| Build/run/operator cost and resource totals | |
| Exclusions, fixes, retests and final admission decision | |

## Attempt ledger shape

Proposed future record fields (not an implemented schema): `attempt_id`, `project_id`, `workflow_id`, `host`, `runner_hash`, `target_hash`, `fixture_hash`, `spec_hash`, `baseline_hash`, `service_version`, `action_revision`, `policy_version`, `run_id`, `run_attempt`, `head_sha`, `base_sha`, `tested_sha`, `mutation_id`, `expected_outcome`, `observed_outcome`, `first_attempt`, `duration_ms`, `resources`, `cleanup`, `artifact_hashes`, `classification`, `supersedes`.

Use a new campaign schema/version when implemented. Do not mutate old corpus schema/counts to make it appear the new campaign already ran. Exclude environment values, credentials and raw terminal strings from shared metadata.

## Batch review

- Candidate IDs: screened / attempted / accepted / excluded / failed / pending, with reasons.
- Canonical uniqueness check and separate development-accepted / final-qualified totals out of 100.
- Category/framework/host distribution and deviations from frozen allocation.
- First-attempt counts, defect controls, recoveries, unexplained failures and fixes.
- Reserved holdouts untouched / consumed / replacement disposition.
- Planned versus actual operator hours, CI minutes by OS, bytes and provider cost.
- Recurring friction and next single implementation repair, if needed.
- Evidence invalidated by changes; exact required reruns.
- Next batch/go/hold decision, owner and rationale.

## Commercial/provider rehearsal

Record provider/test mode, authorized account identities (sanitized), checkout reference, signature validation, event sequence including duplicates/reordering, database/entitlement transitions, effective term/grace, portal/cancel/refund results, run/check behavior during outage, reconciliation result, fees and payout observation. Production and sandbox rows must be distinct.

## Launch decision record

List all ten roadmap gates with evidence and pass/hold disposition. Include exact bytes/deployments, supported host/cell scope, price/limits, provider eligibility, unresolved issues, actual costs/interventions, first-sale path, public claim audit, rollback/shutdown and artifact-retention verification. Name exact proposed external actions. Record the owner's decision separately from engineering recommendation.

## Operations review

Period; paid accounts/selected repos/evaluations; collected revenue/fees/refunds; provider resources/cost; errors/retries/queue lag; retention/deletion success; support tickets/minutes; routine maintenance hours; incident hours; feature-development hours; actions taken; next capacity threshold; next price/scope decision. Avoid vanity metrics and averages that conceal a single expensive account.
