# Wide-character release execution — 1 October 2026

Status: **complete; published and native public downloads verified**. The user authorized the complete
release cycle, including necessary main pushes and publication after qualification.
Outreach, marketing, issue/PR/discussion mutations and website deployment remain prohibited.

The candidate is `v0.4.0-rc.3`, shipping source
`07b304bb32aab9d064e7109733c244ab91766899`, Go 1.26.0, `-trimpath` and
`-s -w -X github.com/Wyrcan-io/playtestr/internal/buildinfo.Version=v0.4.0-rc.3`.
Remote main matched this source and remote tags/releases showed rc.3 unused before build.
[Native build](https://github.com/Wyrcan-io/playtestr/actions/runs/36862893790)
passed all three hosts, building once per host and preserving those exact binaries.
Each archive contains the binary, README, Apache license and third-party notices;
source installation, spaced-path extraction, version, installed examples, intended
failure, cancellation and offline report smokes ran on each native host.
[Manifest](../../release/wide-character-candidate-manifest.json) preserves the hashes.

The [repair decision](../wide-character-decision.md) and historical
[development record](wide-character-2026-09-28.md) define the selected two-column
East Asian Wide/Fullwidth behavior and reviewed television migration. Spec/report
v1 and opt-in v2 remain unchanged. Combining clusters, emoji/ZWJ sequences,
terminal-specific ambiguous widths and target-visible terminal queries remain excluded.
Existing stable/prerelease bytes and historical failed attempts remain immutable.

Qualification uses the existing 120-workflow host distribution, 15 classified controls
and recoveries, six native Linux/macOS journeys, and ten frozen workflows repeated
100 times on each of three native runner hosts. This is one 3,000-attempt campaign,
not a 120-by-three matrix. Previously used GitUI/television holdouts are regression
cases, not newly unseen evidence. The two-host real journeys remain distinct from
the Windows corpus and its admitted WSL target lanes.

Before the long campaign, historical rc.2 actual cost is 1.74 runner-hours and
6.47 MB scaled evidence. A fresh 30-cell preflight is running to update the forecast.
The 90-minute campaign jobs, six-hour exploration allowance, per-attempt 64 MiB and
per-job 1 GiB bounds and 14-day hosted retention remain unchanged. No paid runner,
billing change or new service spend is authorized. Actual billed dollars remain unknown.
First attempts and unexpected results will be retained individually.

Native source gates passed 15/15 command/check rows per host with required events
present. Full-test events include 263 passes on each Unix host and 262 on Windows
(counting subcases); only the platform-inapplicable Windows-path/Unix-permission
cases skipped. Source wide-cell and adapter regressions passed on each host.
Exact-byte fidelity passed 5/5 per host, lifecycle/resource gates passed per host,
and release stories accepted ten declared command outcomes per host. Native Linux
and macOS primary journeys accepted 48/48 each. The Windows corpus accepted
150/150 expectations (120 workflows, 15 negatives, 15 recoveries); no original
input changed and all 56 retained target inventory files matched prior hashes.

Compatibility accepted 15/15; previously used GitUI/television regression definitions
accepted 20/20. Independently specified ANSI/cell baselines accepted 18/18 on each
native host (54 total), including addressed cursor proof, overwrite/erase/wrap,
split UTF-8, crop resize and alternate screen. Offline report browser validation
passed at 375/1440px with keyboard/no-script/layout/contrast/accessibility-name
checks and zero external requests; this is not human screen-reader evidence.

The first new Windows ANSI harness run put its independently written baseline files
in the wrong directory. The second retained run corrected that path but exposed the
Python target's default Windows console code page interpreting raw UTF-8 incorrectly.
Explicit UTF-8 console code pages fixed the target; expected baseline strings were
unchanged. All first reports remain retained. The first browser attempt connected
before browser startup completed; its connection refusal and separate successful
attempt are both retained. No runner rebuild, assertion weakening or baseline
acceptance was used.

Fresh preflight accepted 30/30 and forecasts 1.537 runner-hours plus setup and
6,471,700 bytes. The exact 3,000-attempt campaign passed at
[36864122786](https://github.com/Wyrcan-io/playtestr/actions/runs/36864122786).
All 3,000/3,000 first attempts passed, with zero first-attempt or managed-cleanup failures. Each host ledger contains ten workflows with exactly 100 unique attempts each, the expected frozen executable hash on every row, and confirmed cleanup. Raw reports/oracles and ledgers remain retained. Public installation and upgrade verification subsequently passed; see the dated publication section below. Operator review cannot close independent adoption or human accessibility.
The [machine record](wide-character-release-2026-10-01.json) will record final outcomes.

The manifest/configuration files preserve their original build-time pending fields as
historical freeze evidence. The derived qualification section in the machine packet
records final acceptance. Implementing engineer self-review is the review boundary;
independent adoption and human accessibility remain open.

## Publication and actual public installation

[v0.4.0-rc.3](https://github.com/Wyrcan-io/playtestr/releases/tag/v0.4.0-rc.3) was published at 2026-10-01T13:49:27Z (1 October in Asia/Calcutta). The immutable tag resolves to `07b304bb32aab9d064e7109733c244ab91766899`; all seven public assets matched the qualified files locally and through native public routes. No binary was rebuilt or substituted. Stable v0.1.0 remains latest stable; all prior tags/assets are unchanged.

| Host | Executable SHA-256 | Archive SHA-256 |
| --- | --- | --- |
| macOS ARM64 | `05ad8911ddaa4a5ad73ca0a218b357d850a1cf93b6d610e1c691f0fc80c36b79` | `494731020f663eca67340ba8969d5475c0f52525ebdd12cc0975fbbc8246c181` |
| Linux X64 | `6317f37b59946c30e50a7f34c627c9be6fdd957fe370a8d9cde4697fc5d04425` | `8ebd5390e0e76cd2c34e141e66cb4dda2d0c8488f18ef4319fd9c17bf4a6ed16` |
| Windows X64 | `531804dcb5f29bdcc9d9e2650b1be86e083eedd34c4545ebff1654f05d33f16a` | `b159cd8f638f231c278b485565663dfe8fe323f97e3edf0c86fe7077239a406f` |

[Native public distribution/upgrade 36871693872](https://github.com/Wyrcan-io/playtestr/actions/runs/36871693872) passed three public lanes, three genuine old-to-new upgrade lanes and its identity job. [Binary-only native installation 36871699556](https://github.com/Wyrcan-io/playtestr/actions/runs/36871699556) passed all three hosts without a Go setup/invocation prerequisite. The retained audit inspected 83 distribution/upgrade result rows and 14 binary-only rows (97 total), preserving intended failed product reports. Every launched reported target confirmed managed cleanup; invalid inputs were rejected before launch, and cancellation and workspace cleanup passed. All downloaded archives/checksums returned HTTP 200, matched frozen hashes, extracted into spaced paths and reported rc.3. Reviewed upgrade baselines stayed unchanged.

The actual external immutable setup action remains `Wyrcan-io/playtestr/setup-playtestr@ae97c62022966cde9699b26169b4dc6ef0a12439`, independently pinned from the runner version. Its source implementation is identical at frozen source and passed native corrupt/interrupted/network gates. Genuine upgrades installed existing v0.3.0-rc.1 and rc.3 into separate paths with the same action pin, exercised v1 pass/intended-failure/recovery on both and v2 only on the new version. Public Gum pass/wrong-input-negative/recovery and offline HTML passed on all three hosts; the negative is explicitly an input control, not a code defect. Automated browser checks also passed against the actual Windows public-binary HTML.

The prepublication aggregate-checksum guard caught local Windows CRLF conversion and stopped before creating a release. Original bytes and old/new hashes are retained; publication used the exact LF Git blob, leaving archives and native adjacent checksums unchanged. Two evidence summarizer mistakes are also retained: absent optional CPU fields are now explicitly counted rather than inferred, and the public auditor uses committed checksum bytes because an intermediate expected file was not uploaded. Neither changed product outcomes or public files. No failed publication, target failure or runner failure was retried away.

## Cost, retention and completion

- final qualification: 6292 actual runner-job seconds (1.748 runner-hours).
- preflight: 679 actual runner-job seconds (0.189 runner-hours).
- engineering validation: 1904 actual runner-job seconds (0.529 runner-hours).
- public verification: 424 actual runner-job seconds (0.118 runner-hours).
- binary-only installation: 55 actual runner-job seconds (0.015 runner-hours).

Engineering validation remains below the six-hour exploration allowance; required final qualification and ordinary CI are separately attributed. Native artifact sizes/digests, source/target/runtime/spec/oracle hashes, every first-attempt ledger and descriptive timing/resource limits are retained in the machine packet and private evidence archive. Hosted artifact retention is 14 days; local ZIP members are hash/CRC verified. Billed dollars and human effort remain unknown; no paid runners or billing changes were used.

Documentation-only follow-ups leave executable inputs and qualified bytes unchanged. Website build/link checks ran; website deployment is excluded. The user’s pre-existing documentation edits are preserved. No outreach, marketing, issues, PRs or discussions were mutated. Human accessibility, independent adoption and differentiation remain honestly open. Next decision: use the verified prerelease locally; any stable promotion or specific independent outreach/trial needs a later instruction and its own applicable gates.

The final website rehearsal caught six missing route mappings for new release,
migration and evidence links. The original failed log is retained; explicit
mappings corrected them and the 36-page build/link check passed without deployment.

Ordinary CI through the qualified-record push passed 18 runs and used 5657 runner-job seconds (1.571 runner-hours), separately attributed from final qualification. Final documentation-push checks and the private evidence ZIP digest/CRC/member closure are retained in `artifacts/rc3-completion-seal.json`. The ZIP is `.trial-private/playtestr-wide-character-release-evidence-2026-10-01.zip`; it is not a release asset.
