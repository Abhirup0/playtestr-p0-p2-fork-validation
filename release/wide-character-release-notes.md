# Playtestr v0.4.0-rc.3

Release-note draft; qualification and publication are pending.

This prerelease adds the selected East Asian Wide/Fullwidth two-column repair:
correct cursor advancement, addressed overwrite/erase, wrapping, split UTF-8,
resize cropping and alternate-screen behavior. MICRO-08 now verifies the original
wide-text interaction and independently saved file. Three television baselines
were explicitly reviewed; no bulk snapshot update or automatic migration occurs.

Spec/report v1 and opt-in v2 remain compatible. Suites, offline reports,
workspaces, bounded installation, macOS final-output preservation and Linux EOF
behavior are retained. Stable v0.1.0 and previous prerelease tags/assets stay unchanged.

Targets are Linux amd64, Apple silicon macOS arm64 and Windows amd64, with
native evidence scoped to the exact recorded host images and application pins.
Go is not required to run the standalone download. Targets and their runtimes
remain the user's responsibility; trusted-target execution is not a sandbox.

Install the matching archive beside your current binary, verify its adjacent
SHA-256 and `playtestr version` (`playtestr v0.4.0-rc.3`), then change PATH.
Retain your previous binary for rollback. Keep existing reviewed baselines;
review CJK alignment changes individually against terminal columns and target
state. rc.2 retains its old wide-cell behavior, so switching back may restore
its old snapshot mismatches. No schema migration is required.

The independently pinned setup action remains
`Wyrcan-io/playtestr/setup-playtestr@ae97c62022966cde9699b26169b4dc6ef0a12439`,
with runner version `v0.4.0-rc.3` selected separately. Its implementation is
unchanged from the verified action, and current native installer source/failure
checks passed. Public action and public-download checks will run after publication.

Combining clusters, variation selectors, emoji/ZWJ sequences, terminal-specific
ambiguous widths and target-visible terminal queries remain excluded. Cleanup
applies to the documented process-group/Job Object boundary, with existing escape
limits. Exact workflow evidence is not universal framework/Unicode compatibility.
Independent adoption, human screen-reader usability, human effort and differentiation
remain open. No website deployment, outreach or marketing accompanies this release.
