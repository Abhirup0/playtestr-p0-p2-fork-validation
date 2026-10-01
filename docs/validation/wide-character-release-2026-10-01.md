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

Native source, exact-byte fidelity/lifecycle, corpus, repeat, compatibility,
regression holdouts and public installation gates are pending. Publication has not
occurred. Operator review cannot close independent adoption or human accessibility.
The [machine record](wide-character-release-2026-10-01.json) will record final outcomes.
