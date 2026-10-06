# 06 — Subscription, first sale and unit economics

Status: hypotheses and implementation requirements, not a price announcement, provider account or revenue forecast. [Sources](13-source-register.md).

## Initial offer

One launch tier: **Playtestr Review — $49/month or $490/year per GitHub personal account or organization**, covering three selected repositories, 1,000 review evaluations/month and 30-day compact history. Local runner/recording/basic CI remain free. Limits have one source in [05](05-managed-infrastructure.md).

Annual payments do not create an unlimited evaluation pool: monthly usage resets on the documented subscription anchor. No seat charge, execution-minute resale, automatic overage, custom SLA, bespoke setup or separate enterprise tier at launch. The $149 tier discussed earlier is deferred until real demand/cost evidence warrants it. A lower price is a later experiment, not a second untested launch offer.

The fee buys review-policy automation and history. GitHub execution/storage fees remain the customer's separate responsibility. Explain that public/private runner allowances vary, with a link to current GitHub pricing. Never present $49 as covering arbitrary cross-platform compute.

## First-sale route and Marketplace sequence

1. P0 checks seller-country/business/product eligibility, verification documents, payout method/timing, customer geography, supported checkout, cancellation/refund handling and sandbox access.
2. Prefer GitHub Marketplace when approved and eligible. GitHub's documented paid-app installation/verification prerequisites mean this cannot be assumed for the first customer. **100 tested codebases do not equal 100 App installations.**
3. If unavailable, prefer a hosted merchant-of-record checkout with no monthly minimum, subject to actual approval. Paddle is a candidate with published transaction pricing; it is not a selected or approved account. Keep a second eligible hosted provider as fallback only if the first fails a concrete criterion.
4. Install the GitHub App through GitHub and buy through the clearly identified external portal. Link verified buyer identity to the installed account through an authenticated session; never match solely by email text.
5. Once Marketplace eligibility is reached, implement its approved billing adapter and verification. Recheck requirements then. Do not manufacture installs or migrate existing customers into double billing.

Complete one working billing route before launch. Marketplace availability is not allowed to postpone the entire product indefinitely when a compliant self-service fallback exists. If no eligible route works, paid launch is blocked; report that finding rather than collecting money manually.

Merchant-of-record handling of transaction taxes does not eliminate the owner's business registration, income-tax, payout or accounting obligations. Resolve relevant provider/professional requirements at the business gate; do not invent legal eligibility from this plan.

## Entitlement state machine

| State | Entry | Product behavior |
| --- | --- | --- |
| Unsubscribed | No verified active purchase | Free local/CI; paid review unavailable |
| Pending | Checkout initiated, not verified | No paid activation from browser redirect |
| Active | Verified purchase/renewal, eligible account | Paid features within limits |
| Past due | Provider confirms failed renewal | Proposed 7-day grace for existing entitlement; show portal and exact end |
| Cancel at term | Verified cancellation request | Keep access until paid period end; no future renewal |
| Expired | Term/grace ended | Stop new paid evaluations; no false successful policy checks |
| Refunded/revoked | Verified provider action | Apply documented effective date; reconcile access and audit |
| Suspended/uninstalled | App access removed or abuse | No GitHub access; expose provider cancellation route |

Use one logical subscription per GitHub account/product. Unique provider subscription/customer IDs plus a selected billing-provider field prevent parallel adapters granting duplicate charges. Out-of-order events reconcile to authoritative provider state. Deduplicate deliveries; make database update/publication retry-safe. Grace policy must be supported by the chosen provider and reflected in terms before checkout.

Required tests: pending payment, success, failed payment, delayed/duplicate/reordered webhook, signature failure, renewal, annual reset, cancellation/end-of-term, refund, dispute, reinstall, account transfer, portal access loss, provider outage, double checkout and old-provider migration. Sandbox proof is necessary; a small authorized production transaction/refund is a separate launch qualification task, never claimed from sandbox alone.

## Unit economics model

Monthly contribution before founder time and business taxes:

`collected subscription revenue - processor/platform fees - allocated managed-service cost - refunds/chargebacks - other direct service costs`

Economic contribution also subtracts support/maintenance hours at an explicitly selected hourly value. Revenue is not profit; prepaid annual cash is not twelve months of already earned monthly revenue. Cash available for hosting depends on payout schedules and reserves, not checkout completion alone.

Illustrative model using a **5% + $0.50 transaction fee** candidate, before additional applicable charges, taxes/refunds and founder time. Provider pricing is sourced in 13. Infrastructure values below are deliberately assumed planning envelopes, not measured forecasts.

| Monthly customers | Gross at $49 | Modeled transaction fees | Assumed total monthly infrastructure | Contribution before excluded costs |
| ---: | ---: | ---: | ---: | ---: |
| 0 | $0 | $0 | $0 target | $0, excluding development effort |
| 1 | $49 | $2.95 | $0–$5 | $41.05–$46.05 |
| 10 | $490 | $29.50 | $5–$15 | $445.50–$455.50 |
| 100 | $4,900 | $295 | $15–$75 | $4,530–$4,590 |
| 1,000 | $49,000 | $2,950 | $75–$500 | $45,550–$45,975 |

The 1,000-customer row is arithmetic sensitivity, not evidence that one database or current quotas can support it. Validate storage, concurrency, billing reconciliation and GitHub API capacity before that scale. Marketplace fees require their own current agreement; do not apply the candidate processor fee to Marketplace revenue.

At an illustrative founder time value of $30/hour, one support hour on a $49 account costs $30 economically. At $60/hour it exceeds most of that account's contribution. The product must therefore minimize recurring support rather than depend on bespoke onboarding revenue.

## Cost measurement and commercial gates

Before launch, benchmark representative paid evaluations (unchanged, changed baseline, failed run, large metadata, duplicates and throttling). Record resource units and cost at 1/10/100/1,000 modeled accounts using measured per-evaluation data and realistic monthly activity. Stress the worst allowed account, not only the average. Include free installs, malicious traffic, payment callbacks, backups, monitoring and deletion.

Targets: service infrastructure at or below 10% of collected revenue once at least ten paid accounts are modeled; nonnegative first-customer direct contribution; no mandatory recurring infrastructure spend at zero customers; no manual normal billing steps. These targets are not guarantees of profitability or capacity.

Default launch support is asynchronous documented bug support with no guaranteed response SLA. Do not promise custom test authoring or unlimited debugging. State refund/cancellation terms clearly and verify their consistency with the chosen provider before selling.

After launch assess real paid conversion, repeated review use, churn reasons, refunds and support minutes at 30/60/90 days. If customers use only free features or no paid benefit survives comparison, reconsider pricing/value. One hundred successful project tests cannot settle willingness to pay.
