# 07 — Security, privacy and data lifecycle

Status: requirements to implement and prove. [PR contract](04-github-execution-and-review.md) · [Infrastructure](05-managed-infrastructure.md).

## Trust boundaries

| Boundary | Threat | Required control |
| --- | --- | --- |
| Developer → target process | Trusted target hangs, floods or leaves children | Existing time/output bounds and explicit cleanup evidence; no sandbox claim |
| Fork author → Actions | PR code tries to access secrets or persistent host state | Restricted ephemeral jobs, no App/payment credentials, least permissions |
| Actions/artifact → backend | Fabricated fields, traversal, oversized payload, false provenance | Verify run through GitHub; strict bounded data-only parsing; context binding |
| GitHub/billing → webhook | Forged/replayed/reordered event | Verify raw-body signatures; deduplicate; reconcile upstream state |
| Account A → account B | ID guessing or stale repository ownership | Authorize every request using stable tenant/install/repo IDs |
| Reviewer → approval | Unauthorized or stale approval | Verify role and exact revision/policy; invalidate on relevant change |
| Internet → service | Request floods and cost exhaustion | Pre-processing limits, bounded work, circuit breakers and monitored reserves |
| Maintainer → production | Bad migration, leaked key or compromised dependency | Narrow deployment access, staged releases, rotation, rollback and audit |

The service must not execute downloaded artifacts, evaluate code in reports, follow supplied URLs freely, render raw HTML, or accept a result's own claim of tenant/PR identity as authority. A public repository is not proof its content is harmless.

## Proposed minimum GitHub permissions

Installation metadata; checks read/write; actions read for result/run metadata; pull requests read for changed-contract inventory and review state; contents read only where needed for trusted configuration and relevant small blobs. Exact permission names and endpoints must be verified in P0. Avoid contents write, workflow write, administration write and broad personal tokens.

Default publication uses checks. If a PR comment feature adds write permissions, it needs a concrete benefit and a revised review. Organization-membership access is conditional on a team-review feature that needs it. Permissions should be visible before install, and permission expansion requires reauthorization rather than silently broadening access.

Installation tokens are short-lived, scoped and never passed to test jobs. App signing key and webhook/payment secrets remain provider-managed secrets, outside code/artifacts/logs. Rotation supports overlap where the upstream service permits it, with an exercised revocation path.

## Data inventory and retention

| Data | Location | Proposed retention / deletion |
| --- | --- | --- |
| Specs, fixtures and reviewed snapshots | Customer repository | Customer-controlled Git history |
| Raw terminal output, diffs and offline HTML | Customer GitHub artifacts | Customer-selected bounded Actions retention |
| Installation/account/repository IDs and selected policy | D1 | Active account; remove within 30 days of verified deletion/uninstall unless needed for a stated billing reconciliation |
| Review outcomes, revision IDs and actor IDs | D1 | Rolling 30 days; export available |
| Webhook/job diagnostics | D1/provider logs | Seven days of sanitized IDs/status only |
| Retry work | D1 | Delete payload references after completion/expiry; retain only bounded diagnostics |
| Payment method, invoice and legally retained transaction records | Billing provider | Provider/legal retention; disclose separately from service deletion |
| Encrypted backups/exports | Managed provider storage | Selected plan's bounded schedule, documented expiry after live deletion |

No environment values, typed input, target command arguments, raw event bodies or screen text in service logs. The small result envelope should contain outcome categories and safe step indices, not arbitrary target-written error prose. GitHub artifact URLs may expire; do not copy private artifacts to a public CDN to improve convenience.

A target can print secrets. Local authoring uses synthetic data, previews exports and explains this risk. No automatic masking claim guarantees secrecy. Security controls must detect accidental propagation of deliberately planted test secrets through recorder drafts, reports, HTTP logs, metrics and error messages.

## Identity and account changes

Use GitHub-issued identity/session verification, CSRF protection, secure cookies where sessions exist, short expiration and safe return URLs. Billing portal creation requires current account authorization. Do not trust query-string account IDs or client-supplied subscription state.

Repository rename preserves identity; transfer requires owner/installation/entitlement revalidation and may stop evaluation. Removing a repository from an installation revokes service access immediately. Account deletion and App uninstall have distinct billing effects; the UI explains cancellation, and reconciliation prevents a forgotten subscription from remaining invisible.

Deletion requests must be verifiable, idempotent and automatic. Track deadline and retries without retaining deleted sensitive data in a permanent tombstone. Explain backup expiry and provider-retained invoices. Restore procedures must reapply deletion tombstones before serving restored data.

## Required abuse and fault tests

Cross-tenant read/write/export/delete attempts; guessed run/PR IDs; duplicate signature-valid events; wrong secret; stale timestamps where supported; incorrect media type; oversized and compressed payloads; pathological JSON depth/counts; unexpected schema; path traversal; artifact URL redirection/SSRF; hostile Markdown/HTML; repository transfer; revoked token; unauthorized reviewer; stale policy; secret strings; request bursts; hot-tenant contention; deletion during retries; restore after deletion; key rotation during in-flight jobs.

Treat fixtures and third-party project source as untrusted when building the 100-project campaign. Use disposable native hosted workers, no production secrets, bounded storage and explicit build commands. Downloading/testing a project does not authorize upstream changes or contact.

## Incident and disclosure gate

Have an owner, contact route, revoke/disable procedure, dependency inventory and minimal incident record. A detected tenant escape, false successful policy result, leaked credential or unauthorized charge blocks launch. Document a response procedure without promising continuous on-call coverage that the owner cannot supply.

Before publication, review privacy terms against actual stored data, provider locations/subprocessors and retention. Check legal/provider requirements with appropriate expertise when necessary; a Markdown plan is not evidence of compliance certification.
