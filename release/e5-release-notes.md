# Playtestr v0.4.0-rc.2 â€” prerelease

This candidate preserves the v1 contract and opt-in v2 managed-workspace/report
behavior. It repairs bounded installer body reads, preserves unread macOS final
terminal output with bounded session cleanup, and retains Linux's natural-exit
EOF optimization. No new test/report format or target-framework dependency.

Scope: explicitly trusted keyboard-driven CLI/TUI regression targets and the
pinned workflows in the accompanying qualification record. The PTY runner is
not a sandbox. Basic exercised text does not imply complete Unicode layout.
Wide/combining cursor layout and terminal-query-dependent flows remain excluded;
MICRO-08 wide rendering is unreliable even where an individual Windows run
passes. macOS retains the bounded final-drain cost to preserve correctness.

Private qualification accepted 3,000 first attempts on three native hosts,
with zero first-attempt or managed-cleanup failures. The corpus has 119
supported cells plus one excluded wide-rendering diagnostic. Publication
was authorized on 28 September 2026; public-download and immutable-action verification
must pass after publication before a public recommendation. Independent first use, human
screen-reader navigation, preference and retention remain unmeasured.

Install an approved archive beside the current binary, verify SHA-256 and version,
then change PATH explicitly. Keep reviewed v1 baselines for old-runner interchange;
older strict readers can reject v2. The candidate binary and setup-action commit
are separate pins. The immutable setup-action pin is
`ae97c62022966cde9699b26169b4dc6ef0a12439`.

Downloads: choose the archive matching your host, verify its adjacent SHA-256 file, extract it and run `playtestr version`. Linux amd64, Apple silicon macOS arm64 and Windows amd64 archives are attached. Stable v0.1.0 remains unchanged. No Go installation is required to run the binary; target runtimes remain your responsibility.
