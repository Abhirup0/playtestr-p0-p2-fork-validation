# Two-column terminal cells

28 September 2026; development repair, not a new release qualification.

The original MICRO-08 interaction sends UTF-8 `雪 ` and then redraws after a
70×16 to 84×22 resize. The target saves the intended bytes, but the original
vt10x advances every rune by one cell. Addressed redraws therefore leave stale
text (`雪l alpha marker`). The reduced `雪X` cursor is column 2 instead of 3;
`雪 X` followed by CUP column 4 and `Z` renders `雪 XZ` instead of `雪 Z`.
The first failing reduced test output is retained in the development evidence.

## Decision

Maintain a small internal copy of vt10x at its existing pinned commit
5011da428d02, retaining its MIT license and upstream tests. Add two-cell heads
and continuation flags to its existing fixed-size Glyph representation.
Use `golang.org/x/text/width v0.39.0` for East Asian Wide/Fullwidth properties.
Ambiguous characters remain one column. This dependency is Go's maintained
Unicode table package under the same BSD license as the existing x packages;
it adds no transitive production dependency. Go 1.25 remains the module floor.

The first audit of v0.35.0 reported the module-only
[GO-2026-5970](https://pkg.go.dev/vuln/GO-2026-5970) finding in Unicode
normalization, which this renderer does not import or call. The dependency
was upgraded to the fixed v0.39.0 anyway; the original scan is retained.

This is a local maintenance responsibility. Future updates must review the
copied parser and cell operations explicitly, retain attribution, and run
native regressions. Neither repository age nor a vulnerability scanner proves
that a parser is safe. This backend still runs explicitly trusted targets.

The adapter now uses that internal copy; the original external module remains
only for the historical cell-probe baseline. No exported spec/report contract,
input encoding or process lifecycle changes. Two-column cells participate in
cursor advancement, addressed overwrite, erasure, automatic wrap, insert/delete
cell operations and resize cropping on both screens. Cropping or overwriting
either half clears the pair; resize does not reflow text. A wide glyph with no
room under disabled wrap, or in a one-column viewport, is clipped to blank.
String serialization emits the head once and skips the continuation; it does
not manufacture a padding space. Actual leading and intervening spaces remain.

## Alternatives examined

Padding the string would leave the parser's cursor wrong. Changing MICRO-08's
assertion would conceal the application failure. Replacing the whole emulator
with `github.com/charmbracelet/x/vt` at
`v0.0.0-20260927004216-9c77d672503d` was piloted: cursor addressing and paired
overwrite passed, but a four-column viewport receiving `abc雪X` lost the Snow
character on wrap (observed `abc\nX`, expected `abc\n雪X`). The pilot is retained.
That module also describes its API as experimental, adds a larger dependency
tree and defaults to scrollback and a synchronous reply pipe. It was removed
from go.mod/go.sum; no speculative replacement ships.

## Bounds and remaining contract

The existing output cap applies before parsing. The parser keeps its existing
256-rune string buffer and fixed CSI argument storage; viewport allocation
remains proportional to the two bounded screens. Continuation flags use the
existing int16 attribute field, so per-cell storage does not grow. Each glyph
does constant bounded pair work, and resize/insert/delete remain bounded by
the viewport. The width lookup is table based. No scrollback, query reader,
new goroutine or shutdown path is added. The writer still discards responses,
so device/cursor queries do not become target-visible and cannot wait on a
new synchronous reply pipe.

Zero-width combining clusters, variation selectors, emoji/ZWJ sequences,
terminal-specific ambiguous-width settings and query round trips remain
unsupported. A passing combining-selection companion only checks selected
bytes, not correct general combining-cell rendering. Insert-mode support is
unchanged; CSI insert/delete cells have dedicated wide-pair regression tests.

## Validation and migration

See the linked development validation record for actual native results,
first failures, target identities, full tests/vet/race, existing corpus and
defect/recovery evidence. Published rc.2 assets and qualification records
remain immutable. This change must be separately frozen and qualified before
any later release.

ASCII and existing single-column snapshots should remain identical. Snapshots
that depended on the old wrong CJK cursor positions can change. Inspect the
captured screen and target behavior, then explicitly review each affected
baseline; do not bulk accept snapshots or rewrite old evidence. No new schema
or automatic baseline migration is introduced.
