# 01 — Product, positioning and launch scope

Status: proposed product contract. [Roadmap](../../roadmap.md) · [Journeys](02-customer-journeys.md).

## Customer and job

Primary customer: a developer or small team shipping an interactive CLI/TUI, with a GitHub repository, a repeatable build, and a few important user flows currently checked manually or through custom scripts. Initial buying hypothesis: teams responsible for developer tools, setup wizards, repository tools, local editors and internal terminal applications will pay to reduce review and baseline-maintenance work.

Solo developers use the same engine locally and in CI. Large repository owners use selected repositories, existing Actions and native review permissions. Repository popularity is not evidence of budget. Open-source maintainers are legitimate free users, not a mandatory revenue source.

Job: after changing code, discover whether a protected terminal interaction broke; understand the difference; deliberately accept an intended change; merge with the reviewed expectations preserved.

## Message hierarchy

| Surface | Planned wording / meaning |
| --- | --- |
| Category | Terminal regression checks for pull requests |
| Headline | Record once. Check every PR. Review terminal changes. |
| Explanation | Record important CLI/TUI workflows, approve expected results, and replay those tests locally and in GitHub Actions without AI |
| Paid reason | Review and govern test/baseline changes across a team, with revision-bound approvals and a compact audit trail |
| Proof | Reproducible pass → real target defect → useful failure → recovery; project/host/version-specific evidence |

“Record once” means reuse a recorded workflow until intentional behavior or fixtures change. It does not mean tests never need maintenance. “Every PR” means configured workflow events under GitHub's permission, fork and quota rules. “Automatic” applies to execution and evidence, not comprehensive discovery of intended behavior.

The product is a GitHub-centered regression workflow with a local engine. “GitHub bot” may explain delivery, but is insufficient as the value proposition. Existing competitors offer PTY testing and snapshots; avoid first/only/best claims without narrow evidence. See [historical research](../research/tool-choice-2026-10-05.md).

## Free and paid boundary

| Capability | Free | Paid launch tier |
| --- | --- | --- |
| Standalone runner and recorder | Yes, accountless | Same engine |
| Specs, assertions, fixtures and local snapshots | Yes | Same formats |
| GitHub Actions test job, summary and downloadable report | Yes | Same execution |
| Basic manual baseline review through Git | Yes | Same source of truth |
| App-rendered PR review summary and changed-contract inventory | — | Yes |
| Enforced reviewer policy for baseline/spec/workflow changes | — | Yes, exact scope in 04 |
| Revision-bound approval with stale-result invalidation | — | Yes |
| Compact review/outcome history and repository settings | — | Yes, bounded metadata |
| Billing portal, self-service cancellation and deletion | — | Yes |
| Hosted execution, dedicated support, custom integrations | — | Outside launch |

Keep the existing Apache-licensed local core useful. Do not attempt to retroactively charge for existing released behavior. Any separately licensed service code and third-party notices need an explicit licensing decision before publication. The server owns paid entitlements; a local secret or unsigned flag cannot establish payment.

## Why the paid tier could earn its fee

The test can fail freely today. The hypothesis is that teams also need to distinguish a genuine reviewed behavior change from a PR that silently changes snapshots or disables tests. The App should make that review explicit, bind it to exact revisions, and avoid repeated manual bookkeeping.

Test this hypothesis with scenarios: changed snapshots pass tests but await review; changed test selection needs review; an approval becomes stale after new commits; a canceled run cannot satisfy policy; an unauthorized commenter cannot approve; intended changes are accepted without repeated manual baseline hunting.

If the complete paid workflow is only a prettier red/green comment, reject the commercial launch gate. Do not manufacture demand by removing free functionality. After launch, measure actual paid use, retention and support burden before expanding tiers.

## Launch feature boundary

Must have: trusted local recording; explicit assertions/checkpoints; generated editable specs; repeatable fixture guidance; same local/CI semantics; exact runner pinning; accessible evidence; App installation/repository selection; review policy; safe fork treatment; automatic commercial lifecycle; documented limitations; 100-project qualification.

Exclude: AI, autonomous traversal, general fuzzing, game exploration, hosted customer binaries, browser/desktop testing, full styling/pixel snapshots, generalized mouse/protocol parity, custom enterprise deployment, multiple SCM providers, arbitrary dashboards, test-discovery by source analysis, general-purpose SDKs, consulting, and unlimited SLAs.

Seeded input generation/model-based exploration may be future work when a developer supplies the state model and invariants. It is not required to pretend that a terminal screen contains a machine-readable application contract.

## Success measures and falsification

- Engineering: correct failures, reliable generated workflows, inspectable expectations, exact PR provenance, no routine intervention.
- Adoption: independent retained tests and later reuse, recorded only after actual users supply evidence.
- Commercial: paid conversions, cancellations, net collections, per-customer service cost and support time. No target is an achieved metric.
- Operational: target at most two routine maintenance hours per week at the first 100 paid accounts, excluding feature development; incidents tracked separately, never hidden from the total.
- Falsifiers: generated tests need extensive manual repair; baseline policy is too intrusive; frequent unknown terminal behavior; free checks solve all paid needs; support costs exceed the tier's margin.

A failed hypothesis narrows the product before launch or triggers a postlaunch decision. It does not justify silently changing the marketing story halfway through implementation.
