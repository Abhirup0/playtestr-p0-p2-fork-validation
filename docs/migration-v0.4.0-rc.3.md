# v0.4.0-rc.3 migration and rollback

Status: qualified, published and public-download verified on all three native hosts. See the
[release record](validation/wide-character-release-2026-10-01.md).

Spec/report v1 stay the default; v2 workspaces and mixed reports remain opt-in.
Existing compatible v1 fixtures and baseline files must stay unchanged through
installation and upgrade. Install beside the existing binary, verify the matching
archive checksum and exact version, then change PATH. Keep the older executable.

The selected East Asian Wide/Fullwidth repair counts wide glyphs as two columns.
CJK snapshots that encoded the old incorrect cursor positions may differ.
The three television snapshots were individually reviewed using target filenames
and terminal columns; their old/new hashes remain in the development evidence and
Git history. Inspect the actual screen and independent target state before an
explicit selected baseline update. Do not bulk accept or automatically migrate.

Rollback restores the prior binary/PATH entry, never a release asset/tag or
baseline rewrite. rc.2 still has the old wide-cell gap. Combining clusters,
emoji/ZWJ sequences, ambiguous-width settings and target-visible queries remain
outside this repair. No schema or report-version change is required.

The immutable setup action revision remains
`ae97c62022966cde9699b26169b4dc6ef0a12439`; its version input independently selects
`v0.4.0-rc.3`. Native source installation includes corrupt/partial/stalled-download
checks. Actual public download/action and genuine old-to-new upgrade checks passed
on all three native hosts; baseline hashes stayed unchanged. Earlier rc.2 checks are historical old-byte evidence.
