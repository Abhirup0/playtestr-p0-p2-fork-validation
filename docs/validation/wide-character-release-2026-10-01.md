# Wide-character release execution — 1 October 2026

Status: **qualification in progress; unpublished**. The user authorized the complete
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
6,471,700 bytes. The exact 3,000-attempt campaign is running at
[36864122786](https://github.com/Wyrcan-io/playtestr/actions/runs/36864122786).
Repeat qualification and public installation gates remain pending. Publication has not
occurred. Operator review cannot close independent adoption or human accessibility.
The [machine record](wide-character-release-2026-10-01.json) will record final outcomes.
