# When one character occupies two terminal columns

Draft for maintainer review, 5 October 2026. This describes a recorded Playtestr repair shipped in v0.4.0-rc.3. It is not a new benchmark or a claim of complete Unicode support.

A terminal test can enter the right text, save the right bytes, and still compare the wrong screen. Playtestr encountered that distinction in a micro editor interaction: insert `雪 `, resize the viewport, save, and check the rendered result. An independent file check confirmed the intended bytes. The terminal emulator nevertheless left stale text after redraw. The application state and the testing tool's picture of that state disagreed.

That matters because Playtestr asserts the screen after terminal control sequences have been interpreted. Raw output cannot explain the final picture by itself: programs move the cursor, erase cells, redraw a region and switch screens. A wrong emulator can manufacture a regression that the target does not have. Changing the expected snapshot would make the test green while preserving the faulty observation.

The [development record](../validation/wide-character-2026-09-28.md) retains the original failed interaction and the reduced cases. The useful question was narrower than “does Unicode work?” It was whether selected East Asian Wide and Fullwidth characters occupy the correct two columns during cursor movement and redraw.

## Reduce the problem to cells

The original renderer advanced one column for each rune. That rule works for ordinary ASCII, but a rune and a terminal column are different units. Consider this short input:

```text
雪X
```

Under the selected two-column contract, `雪` occupies columns 1 and 2. `X` occupies column 3. The next cursor position is column 4, or zero-based x=3. Advancing once per rune places the cursor at zero-based x=2 instead.

Cursor addressing makes the mistake visible without a full editor. This is the actual reduced input represented with Go escapes:

```go
"雪 X\x1b[1;4HZ"
```

The escape addresses row 1, column 4. Correctly counting terminal columns means `Z` replaces `X`, leaving `雪 Z`. A renderer that counted `雪` as one column puts the old `X` elsewhere and leaves `雪 XZ`. The expected result comes from the stated column contract, rather than accepting whichever picture a second emulator happens to produce.

These cases live in [TestWideCells](../../internal/terminal/vt10x/wide_test.go). They inspect both serialized text and cursor coordinates. A text-only check would miss some cursor mistakes; a cursor-only check would miss stale glyphs. The original copied implementation failed 14 of the 15 selected reduced cases in the recorded investigation.

## Width belongs in the screen model

Padding a snapshot string would be too late. Cursor advancement, overwrite and erasure have already happened by the time the emulator serializes its screen. The fix therefore represents the two cells inside the emulator itself.

The maintained vt10x copy uses its existing glyph attributes to mark a wide head and a continuation cell. The width lookup uses the pinned `golang.org/x/text/width` table for East Asian Wide and Fullwidth properties. Other characters retain the explicitly documented one-column behavior, including ambiguous-width characters.

That representation has consequences beyond printing. Overwriting either half of a wide glyph must clear the pair, or the screen can contain a dangling half. Erasing from its second column must also remove its head. Insert/delete operations and resize cropping must preserve valid pairs or clear a pair cut at the boundary. [breakWide and sanitizeWide](../../internal/terminal/vt10x/state.go) implement those operations. Serialization emits the head once and skips the continuation; it does not insert an extra space into the displayed text.

Wrapping is another useful test. In a four-column viewport, `abc雪X` must put the two-column glyph on the next row because only one column remains after `abc`. A glyph that cannot fit in a one-column viewport is clipped under the chosen contract. Resize crops or expands the fixed viewport; it does not reflow existing text. These are deliberate behavioral choices that need tests, not accidental consequences of a string representation.

## Evaluate the replacement before choosing it

The investigation also piloted a pinned alternative emulator. It handled selected addressed overwrite cases but lost `雪` in the four-column wrapping probe, producing `abc\nX`. That result did not establish that the alternative was generally unsuitable. It showed that the replacement did not satisfy the chosen case without further work.

The [decision record](../wide-character-decision.md) explains the smaller repair: retain the original vt10x attribution and tests, maintain an internal copy behind Playtestr's adapter, and change the selected cell behavior. This creates a maintenance responsibility. Future parser updates must review the copy and run the affected tests. A local fork is not automatically safer or more accurate because its diff is small.

The repair added no reply reader or new goroutine. Existing output limits still bound raw terminal output before parsing. Terminal query responses remain discarded. It also left the public spec and machine-report formats unchanged, so users could keep their interaction definitions while reviewing affected snapshots individually.

## Verify the interaction again

The reduced tests were necessary, but they were not the end of verification. The unchanged micro insertion, resize, save and saved-byte oracle ran on the recorded native Windows, Linux and macOS paths. Companion tests covered split UTF-8, addressed redraws, cropping, alternate screens and the existing output limit. The [release record](../validation/wide-character-release-2026-10-01.md) separately records qualification and verification of the published rc.3 bytes.

Those results support the selected repair. They do not establish correct combining clusters, variation selectors, emoji/ZWJ sequences, terminal-specific ambiguous widths or query-dependent applications. Passing a companion that preserves selected bytes is also not proof that every combining character rendered correctly.

The practical lesson is to test the observer as well as the application. When a screen assertion fails, inspect the saved state, cursor operations and final rendered cells before accepting a new baseline. A respected testing tool needs to make its observation errors reproducible too.

Playtestr is an open-source standalone runner for trusted interactive CLIs and TUIs. To try one keyboard interaction, use the [exact rc.3 installation guide](https://wyrcan-io.github.io/playtestr/docs/prerelease-installation/) and the [writing-tests guide](https://wyrcan-io.github.io/playtestr/docs/writing-tests/). A useful report is a small reproduction with the runner version, target pin, viewport and observed difference.
