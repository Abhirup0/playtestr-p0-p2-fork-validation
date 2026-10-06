# 11 — Launch preparation and low-maintenance operation

Status: plan only. Outreach and marketing remain held until the product and validation gates close and exact external actions are authorized.

## Launch packet

Prepare one reviewable packet containing:

- Exact runner/Action/service versions, hashes, deployment configuration and rollback instructions.
- Product message and free/paid feature table consistent with delivered behavior.
- Complete local and PR onboarding, supported hosts, installation/removal, fixture guidance and known limitations.
- A reproducible recording → PR regression → reviewed intentional update → recovery demo using synthetic data and captured evidence.
- 100-project ledger with attempted/excluded denominator, actual native cells, defects, recovery, costs and artifact availability.
- Security/privacy/retention/permissions summary, accessibility evidence and unresolved lower-severity findings.
- Actual billing-provider eligibility, checkout/portal/cancel/refund behavior, price/limits, fees and payout timing.
- Measured service-cost model, budget protections, unattended rehearsal and intervention log.
- Support boundaries, incident route, dependency update process and named owner.
- Exact proposed release, deployment and marketing actions, separately reviewable under repository policy.

Before launch, update website/README/docs drafts together so “recorder” and paid features are described only where shipped/qualified. Do not erase the existing stable/prerelease distinctions or present historical users as paying customers. Verify current competitor positioning using primary sources; no “nothing like this exists” claim.

## Publication sequence

P7 produces readiness and the packet. Owner review selects go, hold for a named defect, or revise a specified scope. P8 requires explicit authorization for exact release/deployment actions. Verify public downloads and the live purchase path after publication. Marketing starts only after the live product passes its post-publication checks.

GitHub Marketplace eligibility may come later than the first commercial launch. The external checkout route must be clearly disclosed, working and approved. Marketplace billing is not a reason to fabricate 100 installs or to label the engineering corpus as users.

Marketing preparation can include drafts and a channel-specific plan after the technical gates. Sending invitations, posts, issue/PR/discussion mutations or follow-ups always requires the specific authorization in AGENTS.md. The planning task sends nothing. Preserve no-contact/refusal history; no automated outreach bot is part of the product.

## Support designed for self-service

Document solutions for failed build, zero tests, readiness/timeout, snapshot mismatch, unsupported input, expired artifact, missing permission, stale approval, quota, payment state and uninstall. Show the correct next action at the point of failure, with a versioned error code and safe diagnostic bundle.

Diagnostic export excludes secrets/screens by default, previews optional evidence and includes identities necessary to reproduce. Users can file a bug using existing support channels; paid access does not imply bespoke test writing or unlimited assistance. Do not promise a response time until actual capacity supports it.

Normal billing, renewals, cancellation, usage reset, event retry, retention and deletion must be automatic. Use the provider's portal for payment details and invoices. Do not create a separate invoice-management system.

## Operational acceptance and cadence

Prelaunch: 14-day rehearsal from 05, zero routine manual account/job corrections, exercised rollback/restore/key rotation, bounded alerts and recorded exceptional interventions. P7 decides whether observed work fits the desired operating model.

After launch, target no more than two routine operating hours/week at the first 100 paid accounts. This is an internal goal, not a passive-income promise. Measure incident hours, product-development hours and customer-support hours separately and show their total. A large incident cannot disappear from the workload metric because it was “exceptional.”

| Cadence | Automated work | Human responsibility |
| --- | --- | --- |
| Continuous | Bounded event processing/retry, usage controls, health checks | Respond to actionable severe failures |
| Daily | Billing/install reconciliation, deletion/retention, aggregated anomaly report | Review only actionable exceptions |
| Weekly | Usage/cost/support summary, dependency advisory collection | Short health review, prioritize demonstrated defects |
| Monthly | Revenue/fees/refunds and retention report | Check actual margins and maintenance budget |
| Before dependency/platform updates | Compatibility tests and staged deployment | Review material changes and release when qualified |

Provider-managed infrastructure removes provisioning/patching of our own servers. It does not update our GitHub integration, fix our bugs or resolve business disputes automatically. If routine effort exceeds budget for two review periods, prioritize automation/scope reduction over acquiring more customers.

## Commercial learning after launch

At 30/60/90 days examine actual paid activation, repeated use of paid review, cancellation reasons, refunds, median/p95 support effort, net collections and unit costs. Distinguish paying accounts from active repos, installed Apps, test runs and the external-project corpus.

No paid demand: keep the free tool useful, inspect the proposed paid benefit and pricing, and choose a bounded revision or stop commercial expansion. Heavy support: fix onboarding/common faults or narrow advertised scope. Strong repeat use with measured healthy margins: consider Marketplace expansion or an additional tier. Do not add hosted execution by default.

## Exit and shutdown

Have a documented ability to stop new sales, cancel future renewals, provide required refunds/notice through the provider, export metadata and remove service data. Customers retain local tests and GitHub evidence. A service shutdown should not disable the free runner or strand customer-owned baselines.
