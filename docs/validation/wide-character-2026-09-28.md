# Selected wide-character development repair

28 September 2026. The user requested the
[three-step execution prompt](../archive/prelaunch-2026-10-06/plans/wide-character-next-steps-prompt.md)
and its implementation. Outreach and marketing remain prohibited.

## Outcome and scope

Development source `c87e477e4c96b8402b5719149759029bfa9e4c1a` corrects
two-column East Asian Wide/Fullwidth glyphs behind the existing screen adapter.
The unchanged MICRO-08 Snow insertion, resize, save and independent saved-byte
oracle passes on native Windows amd64, Linux amd64 and macOS arm64.
[The ADR](../wide-character-decision.md) records the local fork, rejected
replacement, licensing, dependencies, limits and migration.

This is development validation. Published v0.4.0-rc.2 assets/tags and their
qualification remain unchanged. It is not a new release, an all-framework
claim, a universal Unicode claim, or independent adoption. Combining clusters,
emoji/ZWJ sequences, terminal-specific ambiguous widths and target-visible
terminal-query round trips remain unsupported.

## Reproduction and implementation

The copied original vt10x failed 14 of 15 independently specified reduced
cases. The first output is retained in `before-tests.txt`; the historical
cell probe also retains wrong wide/combining cursor positions.
The repaired cases cover cursor advancement/addressing, paired overwrite and
erasure, right-edge wrap, fullwidth text, insert/delete cells, leading spaces
and clipped narrow/no-wrap viewports. Adapter regressions cover byte-split
UTF-8/escapes, redraw, cropping/expansion of both screens and discarded queries.
A separate combining test retains the explicit unsupported boundary.

An alternative pinned x/vt emulator lost Snow in the four-column `abc雪X`
wrap pilot (`abc\nX`). Its pilot is retained; its dependency tree was removed.
The internal vt10x copy retains the original MIT license and upstream tests.
It adds fixed-size continuation flags and pinned `golang.org/x/text/width`.
No scrollback, goroutine, reply reader or new shutdown path is added.

The first dependency audit found module-only GO-2026-5970 in x/text v0.35.0's
normalization package, which the renderer does not use. We nevertheless pinned
the fixed v0.39.0. The final `govulncheck v1.1.4 -show verbose ./...` reported
no vulnerabilities; `go mod verify` passed. These are dated scan results, not
a security guarantee. Go 1.25 remains the declared floor.

## Native checks

[Initial native run 36350175057](https://github.com/Wyrcan-io/playtestr/actions/runs/36350175057)
passed eight jobs at `1859c6b`. After the dependency correction and wide-output
cap regression, [final native run 36350415225](https://github.com/Wyrcan-io/playtestr/actions/runs/36350415225)
passed all eight jobs at `c87e477`:

| Host | Source checks | Real fidelity cases | Existing native journeys |
| --- | --- | --- | --- |
| Linux amd64, ubuntu-24.04 | Full tests, vet, race, required installer/lifecycle events, manual examples: 15/15 command/check rows | 5/5 including unchanged MICRO-08 and fzf wide/resize/combining companions | Six admitted journeys, 48/48 good/defect/recovery attempts |
| macOS arm64, macos-15 | Same 15/15 command/check rows | Same 5/5 | Same 48/48 |
| Windows amd64, windows-latest | Same 15/15 command/check rows | Same 5/5 | Full local corpus below; not an extra hosted six-journey claim |

All source hosts used Go 1.26.0, real PTYs and native C compilers for race
coverage. Required focused events passed; workflow configuration alone was not
counted. Real cases confirm process exit and workspace cleanup. The combining
companion checks selected bytes, not general combining-cell rendering.
The persistence-only derived probe remains separate from unchanged MICRO-08.

Native fidelity executable SHA-256 at `c87e477`, built with `-trimpath`:

| Host | SHA-256 |
| --- | --- |
| Linux amd64 | `3bf9d9157770c46d8a7d19bc2d66a01a88ab258d5645ed89ec0066d876558f5d` |
| macOS arm64 | `79fa5e40a8fe4c515e57d21f622b65d315b2c92f37f9e159a5a93f26a02f888c` |
| Windows amd64 | `59a46d7ee396fae4b7de2aafb16ee4467adc8802fd866a7e4b30ccb11b37bf80` |

[Terminal tests 36350415210](https://github.com/Wyrcan-io/playtestr/actions/runs/36350415210)
also passed all three native hosts using the declared Go version. The earlier
local Windows dirty-source full tests/vet/race/focused/manual run passed; it is
preliminary evidence, not the final clean native source identity above.
The prescribed local menu/menu-exit manual suite passed 2/2 on the final
development binary.

## Corpus, first failures and reviewed migration

The first Windows development corpus run preserves all 150 outcomes:
144 accepted, six unexpected. MICRO-08 passed without changing its assertion.
Three television snapshots (TV-03/05/06) encoded old wrong CJK widths and,
for TV-03/06, a stale `雪.xxt` filename. Each affected row was edited explicitly:
Snow uses two cells, the viewport border is at column 80, and the fixture's
filename is `gamma-unicode-雪.txt`. Each independently edited baseline then
matched the captured screen exactly. Five rows across three snapshots changed;
no bulk snapshot update was used. Old text and old/new hashes are retained in
`snapshot-review` and Git history. Historical rc.2 qualification is unchanged.

The other first failures were FZF-06 selected-line order, IPM-01 startup timeout
and POST-05 startup timeout. Three alternating old/repaired diagnostics per
case passed 18/18 with unchanged specs. The old binary was checksum-verified
against published rc.2. These failures were not reproduced and no deterministic
cause was established; they are not relabeled as passes or claimed fixed.

The final development corpus uses the fixed dependency and the three reviewed
baselines. Its runner is Go 1.27.0 Windows amd64, `-trimpath`, SHA-256
`938e01dab2d8542204d3a5f2ffdd5c5cadc48a2ac369db5f13823da5ec7fbd78`.
The ledger preserves each attempt and its classification. The campaign covers
120 existing workflows, 15 intended negatives and 15 recoveries; 12 controls
are executable-code defects and three are fixture/input controls. TIG and
taskwarrior targets remain Linux-under-WSL evidence, not native Windows apps.
The final campaign accepted 150/150 outcomes with no changed input during
execution. The earlier 144/150 campaign remains a separate retained result.

## Cost, evidence and next boundary

The four recorded hosted runs used 0.926 runner-hours in aggregate (22 jobs),
below the six-hour exploration cap. Both native real-case scripts forecast
after two pilots and retain all first attempts. Initial Windows microbenchmarks
used three 100 ms samples: write allocations stayed 384 B/36 allocations for
the selected ASCII sequence and 184 B/16 for the wide sequence. Timing samples
were noisy and do not establish a speed improvement. Per-cell storage is
unchanged; real wide-output flood tests enforce the existing byte cap.

The [machine packet](wide-character-2026-09-28.json) records identities, native
gates, corpus outcomes and snapshot review. Raw evidence lives under
`artifacts/wide-character-2026-09-28` and is preserved in a private ZIP with
member hashes and CRC verification. Later documentation/snapshot commits do
not change the renderer code at `c87e477`; their post-push tests remain separate
from those runner identities.

The requested three steps are complete at the scoped development boundary.
Any release requires an unused candidate version, separately frozen builds,
affected qualification and exact-byte publication verification. No release,
website deployment, outreach, issue, PR or discussion mutation occurred here.
