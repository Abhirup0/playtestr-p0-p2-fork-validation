# Locally maintained terminal cell repair

Copied from github.com/hinshun/vt10x at
v0.0.0-20220301184237-5011da428d02 (commit 5011da428d02), including
its tests and MIT LICENSE. Original copyrights are preserved.

Playtestr owns the changes in state.go and parse.go: Unicode Wide/Fullwidth
two-cell glyphs, continuation cells, paired overwrite/erase, wrap and clipping,
and sanitization after cell insertion/deletion or viewport cropping.
wide_test.go supplies the independently specified cell regressions.

Width properties come from the pinned golang.org/x/text/width tables.
Ambiguous characters remain narrow. Combining clusters, emoji sequences,
insert mode and terminal query round trips are not newly supported.
No scrollback, goroutine, subprocess or query reader is added.

Keep upstream updates explicit and review local changes against the original
commit; do not blindly replace this directory from a newer dependency version.
