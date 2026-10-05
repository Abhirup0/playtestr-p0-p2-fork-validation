# Choosing a terminal testing tool

Draft guidance, researched 5 October 2026. This compares current project-owned documentation and separate historical measurements. It is not a fresh execution of competitors, a package-version guarantee or independent user-preference research.

| Choice | Authoring and installation | Assertions and evidence described by its docs | Good reason to choose it |
| --- | --- | --- | --- |
| Playtestr v0.4.0-rc.3 | Standalone exact-version native binary; JSON interactions. Optional Python helper for Actions summaries; target prerequisites are separate. | Rendered text, exact exits, reviewed snapshots, bounded runs, suites, temporary workspaces, JSON reports and offline HTML. | A small keyboard-driven regression suite kept outside the application's language tooling. |
| [Microsoft tui-test](https://github.com/microsoft/tui-test) | CLI installation and Rust/Python/JavaScript APIs. | Text/style locators, keyboard/mouse actions, screenshots, snapshots and trace artifacts. | Rich terminal automation or programmatic tests needing more input and inspection choices. |
| [Atago](https://github.com/nao1215/atago) | Declarative YAML tests; documented binary/Go installation routes and recording. | Commands, files, snapshots, interactive PTY flows and CI report formats including JUnit. | A CLI product whose tests need terminal interaction together with generated-file or broader command checks. |
| [Termlens](https://github.com/vyncint/termlens) | Rust integration using the actual target binary and Cargo dev dependencies. | Rendered screen/style assertions, input modes, snapshots and deadline-bounded waits with failure screens. | Rust projects that want end-to-end tests integrated with their normal test code. |
| Existing [Pexpect](https://pexpect.readthedocs.io/en/stable/overview.html) scripts | Python code with existing process-matching logic. | Pattern matching, input, timeouts and EOF handling; rendered-screen comparison requires additional work. | An existing reliable script already checks the meaningful behavior, or stream/exit matching is sufficient. |
| Framework tests | Existing application framework and test runner. | For example, [Textual's Pilot](https://textual.textualize.io/guide/testing/) and [Ratatui snapshot testing](https://ratatui.rs/recipes/testing/snapshots/) cover framework-level behavior. | Fast widget/unit feedback; keep this layer even when adding real-binary terminal tests. |

The documented feature rows are selection guidance, not measurements of correctness or maintenance cost. Playtestr's real PTY, snapshots and language-independent target execution are shared capabilities, not exclusive inventions. Color/style comparisons, mouse, bracketed paste, general grapheme layout and target-visible queries are outside its current tested contract. Read [terminal compatibility](../terminal-compatibility.md) before choosing it for a particular application.

## What the existing measurements establish

The repository's [27 September matched Linux campaign](../validation/e1-e2-native-readiness-2026-09-27.md) used a Playtestr candidate later shipped in rc.2, Atago 0.23.0 and Termlens 0.11.2. Its selected create-vite task medians were approximately 114 ms for both Playtestr and Atago, and 164 ms for the selected Termlens route. On the selected Lazygit task, Playtestr was approximately 1,117 ms, Atago 164 ms and Termlens 215 ms. Selected defect detection tied. These are two tasks, 30 observations per task/tool, on one host and particular adapters; they do not rank current releases universally.

Older fixtures also included tui-test 0.1.0-beta.5. The later short-task repair removed measured overhead, but the original loss remains recorded. The optimized 50-test suite observation improved from about 126.8 to 113.5 seconds; this was a particular composition, not an independent adoption result or a broad throughput guarantee. No fresh competitive execution was performed for this note.

## The adoption question

Playtestr's proposed position is: “Catch keyboard-driven CLI regressions with a standalone runner, small JSON tests and readable failure evidence.” Lower total effort is a hypothesis. Test it by asking a maintainer to protect one flow, diagnose a known failure, review a change and decide whether to retain the test. Record installation time and assistance separately, and ask why their existing method may be preferable. No independent authoring-effort advantage or willingness to pay has been established.
