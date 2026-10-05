# Adoption package review

Local preparation dated 5 October 2026. No release, site deployment, push, invitation or public post is authorized by this index. The core runner and published assets are unchanged. Independent adoption/commercial gates remain open.

| Ready-to-review result | Location |
| --- | --- |
| Runnable PR workflow with failure-preserving summary/evidence steps | [.github/workflows/terminal-pr-example.yml](../../.github/workflows/terminal-pr-example.yml) |
| Standalone bounded report v1/v2 summary helper and failure tests | [scripts/ci/report_summary.py](../../scripts/ci/report_summary.py), [tests](../../scripts/ci/test_report_summary.py) |
| Complete CI example, prerequisites, artifact retrieval and removal | [CI installation](../ci-installation.md) |
| Actual published-runner pass/seeded failure/recovery and 45-second presentation script | [Demonstration](../adoption-demo.md), [capture script](../../scripts/ci/capture_demo.py) |
| Engineering article draft | [Two columns, one character](../articles/two-columns-one-character.md) |
| Current fair tool-selection guidance with historical measurement boundaries | [Tool choice](../research/tool-choice-2026-10-05.md) |
| Participant guide, feedback questions and private observation template | [Trial kit](trial-kit.md) |
| LinkedIn/community post drafts and optional follow-up | [Launch drafts](launch-drafts.md) |
| Four-week time allocation and sustainability decision | [Operating plan](operating-plan.md) |
| Actual checks, failed attempts, provenance and remaining boundaries | [Validation record](../validation/adoption-preparation-2026-10-05.md) |

The ignored `.trial-private/adoption-review-2026-10-05/messages.md` contains five researched candidates, proposed routes, exact invitation drafts and external-action review rows. Identities and the earlier refusal stay private. The private packet is excluded by the repository's existing ignore rule; do not force-add it. It records route uncertainty rather than treating an open discussion category as permission to promote.

## Smallest next decisions

1. Review the source diff, approve a scoped commit/push and hosted runs if desired: default pass, seeded red check with retained evidence, unchanged recovery. Actual new-workflow hosted results are still required.
2. Approve publication of the reviewed demo/CI documentation and, separately, decide where the article should live. An article in `docs/articles` is a draft, not automatically a public blog route.
3. Select at most two private invitation drafts or one public-post draft. Approval must name the destination and exact text; existing AGENTS.md requires permission for each external communication/mutation.
4. Record real first use and later voluntary reuse before any commercial discovery. The operating plan starts from actual recruitment, not this file's creation date.

These decisions do not require buying a service or operating a hosted bot. The current source workflow supplies the useful PR-test behavior through normal GitHub Actions.
