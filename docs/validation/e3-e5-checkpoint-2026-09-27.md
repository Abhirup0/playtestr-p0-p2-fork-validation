# E3–E5 execution checkpoint — 27 September 2026

Status: executing, not accepted or qualified. User invoked the complete execution
prompt, including testing-branch pushes and final push; publication remains excluded.

Baseline: main `b736ca355ab37e563ff6abd6b8f32a681209ac67`, remote HEAD matched.
The existing AGENTS.md user edit and execution prompt are preserved. No holdout
has been executed during this phase. Historical GitUI/television corpus presence
limits holdout independence.

Active behavior: investigate MICRO-08 wide Snow/stale-cell rendering, with exact
UTF-8 input and independently reviewed cell expectations. Acceptance: native
Linux amd64/macOS arm64 reproduction, encoding check, reduced cell/cursor case,
fzf wide/combining/repeated-resize companion, and either a regression-proven
repair or an explicit investigated unsupported boundary. Basic café/λ remains
a separate positive control. No new Unicode support is implied.

Public contracts touched initially: none. Owner/reviewer: Codex engineering and
self-review; no independent human usability review. Native hosts: standard
Ubuntu 24.04, macOS 15 arm64; local Windows amd64 supplementary checks.
Prerequisites: authenticated GitHub available with command-specific network
permission, Go, pinned micro/fzf sources. Published runner bytes unchanged.
Candidate binary identities will be captured when built, rather than guessed.

Effort estimate: prompt's E3 2–3 focused days, E4 3–4, E5 2–3 plus queues;
actual elapsed tool/engineering intervals recorded separately. Human effort
unknown. Exploratory forecast follows two pilots, bounded at six native hours
and 1 GiB compressed. No paid capacity, tag, release, deployment or outreach.

E4 remains pending four documented walkthroughs, eight maintenance changes,
six diagnosis classes, installation and presentation checks. E5 remains pending
entry acceptance, frozen holdouts, final bytes and all R6 qualification gates.
