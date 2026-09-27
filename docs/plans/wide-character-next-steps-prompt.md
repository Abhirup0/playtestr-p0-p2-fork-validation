# Next engineering steps: correct wide-character rendering

The user asked to write and execute these steps on 28 September 2026.
Outreach and marketing remain prohibited.

1. Preserve the published v0.4.0-rc.2 baseline and reproduce the original
   MICRO-08 Snow/stale-cell failure. Add independently justified reduced
   regressions for two-column CJK text, cursor addressing, erasure/overwrite,
   right-edge wrapping, split UTF-8, redraw, alternate screen and resize.
   Test combining marks separately; do not promise universal grapheme/emoji
   behavior or terminal queries from a passing wide-character case.
2. Evaluate a small fix or one pinned Go emulator replacement behind the
   internal screen adapter. Prefer a real cell model over inserted padding.
   Record an ADR covering licenses/notices, maintenance/security evidence,
   alternative choices, parser/output/memory limits, synchronous query replies,
   shutdown, performance and compatibility. Preserve normalization, leading
   spaces, schemas, keyboard encoding, deadlines, output caps and managed cleanup.
   Prove a regression fails before and passes after; preserve all first failures.
3. Verify the unchanged real micro interaction, independently checked saved
   bytes, meaningful defect/recovery and fzf multilingual/resize companions.
   Run full tests/vet/race, manual examples and required lifecycle/install
   checks on actual native Windows amd64, Linux amd64 and macOS arm64 using
   standard hosted runners. Recheck affected existing real tasks/corpus and
   snapshot compatibility. Document precise supported cases, migration and
   any remaining unsupported boundaries; do not normalize failures away.

Continue until these steps have an evidence-backed outcome: a validated scoped
repair, or a concrete investigated blocker if the candidate cannot preserve
existing correctness/resource bounds. Do not leave a speculative replacement
installed or claim native support from cross-compilation. Commit/push accepted
work and verify post-push CI, preserving the user's AGENTS.md edit and earlier
execution prompt. Keep exploratory campaigns within six native runner-hours
and 1 GiB compressed evidence, forecasting after pilots.

Published assets/tags stay unchanged. Development/native validation is not a
new release qualification. Any later release needs a separately frozen unused
version, exact builds, full affected qualification and publication authorization.
Do not create a new release, deploy the website, contact anyone, post marketing,
or mutate issues/PRs/discussions during these steps.
