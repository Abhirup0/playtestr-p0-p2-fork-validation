# 13 — Provider sources and assumptions

Read-only planning research checked **6 October 2026**. Provider facts can change. Recheck at P0 and before production billing/deployment. Links support provider facts, not Playtestr's measured feasibility. No accounts, purchases or deployments were created.

| Source | Planning-relevant fact | Required follow-through |
| --- | --- | --- |
| [GitHub Marketplace listing requirements](https://docs.github.com/en/apps/github-marketplace/creating-apps-for-github-marketplace/requirements-for-listing-an-app) | Paid Apps require verified organizational publishing; the document lists a minimum of 100 GitHub App installations. Apps process purchase lifecycle events and support monthly/annual paid billing. | Verify actual eligibility and current listing approval; external project tests are not installations |
| [GitHub App hosting](https://docs.github.com/en/enterprise-cloud@latest/apps/creating-github-apps/about-creating-github-apps/about-creating-github-apps) | The developer supplies the application's hosting. | Marketplace subscriptions do not provision a backend |
| [GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions) | Standard public-repository hosted execution is free; private allowances/overages and runner types differ. | Customer chooses/pays for its execution; measure campaign spend separately |
| [GitHub workflow artifacts](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts) | GitHub can retain generated reports as artifacts. | Configure retention/access and test expiry; do not promise permanent evidence |
| [GitHub privileged PR guidance](https://docs.github.com/en/actions/reference/security/securely-using-pull_request_target) | Executing fork code with privileged credentials creates a security boundary violation. | Restrict execution; publish through a separate authenticated data-only path |
| [Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/) | Free tier exists; paid Workers starts at a $5 monthly minimum with usage pricing. | No claim that $5 covers all service components or unlimited usage |
| [Workers limits](https://developers.cloudflare.com/workers/platform/limits/) | Free HTTP allowance includes 100,000 requests/day and 10 ms CPU/request. | Measure cryptography/parsing/database work; request volume alone is insufficient |
| [D1 pricing](https://developers.cloudflare.com/d1/platform/pricing/) | Free allowances include 5 million rows read/day, 100,000 written/day and 5 GB total storage; query scans matter. | Use indexes, test contention and retention; verify per-database/plan limits separately |
| [Paddle pricing](https://www.paddle.com/pricing) | Candidate merchant of record advertises no monthly fee and standard 5% + $0.50 per checkout transaction. | Seller/product eligibility, actual agreement, payouts, geography, refunds and additional applicable costs remain unverified |

The suggested Cloudflare architecture and modeled cost envelopes are engineering/business inferences from these capabilities. They are not a provider guarantee, measured bill, account approval or recommendation to spend now. The previous conversation's $40–$100 infrastructure example is not a mandatory starting configuration.

## Competitor and product evidence

Use [5 October tool-choice research](../research/tool-choice-2026-10-05.md), [26 September research](../research/competitive-refresh-2026-09-26.md), and their primary links as dated context. Terminal testing, snapshots and recording already have alternatives. At P0 refresh relevant shipped versions and compare complete authoring/review workflows, not marketing feature counts.

Existing Playtestr releases and exact runtime comparisons remain in repository evidence. No new competitive benchmark, market-size estimate, revenue evidence, customer interview or current competitor installation was produced by this planning task.

## Facts still to verify

Marketplace financial terms and payout schedule; payment-provider eligibility and production account approval; current GitHub endpoint permissions/rate limits; serverless scheduled-job and transaction semantics; selected-plan backup/restore/deletion behavior; budget enforcement versus alerts; supported geographic/data-handling requirements; exact provider deployment rollback behavior. These are explicit P0/P7 work items, not silently assumed capabilities.
