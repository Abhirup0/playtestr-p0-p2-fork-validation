# Competitive research refresh: 26 September 2026

> Historical research freeze. Later [native E2 measurements](../validation/e1-e2-native-readiness-2026-09-27.md) preserve the original speed losses and separately measure the unpublished candidate; this research snapshot is not rewritten as new execution.

Method: project-owned documentation read on this date, plus the repository's existing executed comparison. This supplements the [19 September survey](competitive-user-survey-2026-09-19.md); it is not a customer survey, market-size estimate or new runtime experiment. Live branch documentation can differ from released packages. Future comparisons must pin matching docs and binaries. Access dates are not release dates.

## What the existing data says

The [22 September experiment](../validation/sprint-13-c-competitive-2026-09-22.md) used Playtestr `f1ab948`, Atago v0.23.0, tui-test 0.1.0-beta.5 and Termlens 0.11.2 on Linux amd64. Its C1–C3 targets are repository-owned deterministic fixtures, not three independent projects. All four tools detected the selected mutations; 360 fresh attempts and 36 controls passed the harness's expected outcomes.

| Task | Playtestr median | Atago | tui-test | Termlens | Interpretation |
| --- | ---: | ---: | ---: | ---: | --- |
| Selector | 295 ms | 49 ms | 137 ms | 49 ms | Playtestr about 6.0× the fastest observed median |
| Stateful configuration | 296 ms | 51 ms | 143 ms | 50 ms | About 5.9× |
| Modal/resize | 305 ms | 106 ms | 150 ms | 54 ms | About 5.6× |

These are 30-sample exploratory cells, not tail-latency guarantees. Peak RSS was lower than Atago/Termlens and higher than tui-test. Installation compared different acquisition work, including builds; its raw times are useful history but not a clean binary-install ranking. The configurable raw-output cap was exercised only for Playtestr; finite output drain and target/session cancellation in alternatives were explicitly different contracts.

The source contains a 150 ms snapshot quiet period, a 150 ms graceful-stop allowance, polling and final-output drain behavior. These are **profiling hypotheses**, not measured explanations of the gap. Preserve final output, readiness and cleanup while investigating. Neither disabling safeguards nor rewriting Go is an evidence-based response yet.

## Refreshed competitive map

Each row distinguishes documented capability from our proposed response. Documentation is not independent proof of performance or reliability.

| Alternative / source | Documented strengths relevant to this product | R&D consequence |
| --- | --- | --- |
| [Microsoft tui-test](https://github.com/microsoft/tui-test) | CLI plus language APIs, text/style locators, keyboard/mouse actions, screenshots and trace artifacts | Direct rival in authoring and diagnosis. Compare normal emitted failure evidence and real PTY journeys; do not claim our reports or waits are unique |
| [Atago](https://github.com/nao1215/atago) | Declarative real-command/PTY tests, file checks, recording, multiple CI report formats and installation routes | Closest declarative rival. Compare stateful tasks including external-oracle glue; investigate JUnit only against a named CI workflow |
| [Termlens](https://github.com/vyncint/termlens) | Rust real-binary PTY tests, rendered cells/styles, deadline-bounded waits, input modes and documented per-platform differences | Strong Rust integration and fidelity reference. Compare actual job and maintenance effort; do not make “framework agnostic” a claim that Rust authors must prefer us |
| [Termless](https://raw.githubusercontent.com/beorn/termless/main/README.md) | Vitest matchers, regions/styles, multiple emulator backends and a real-process PTY route | Add one bounded PTY feasibility comparison. Its advertised sub-millisecond in-memory tests cannot enter an E2E speed ranking |
| [VHS](https://github.com/charmbracelet/vhs) | Scripted terminal recording, screen waits and testing-related workflows | Presentation/usability reference; use existing recording tools before designing our own engine |
| [Pexpect](https://pexpect.readthedocs.io/en/stable/overview.html) | Flexible process input/output matching, timeout and EOF handling | Existing scripts are a legitimate baseline. Measure glue and result interpretation rather than assuming users need rendered snapshots for every command |
| [Textual testing](https://textual.textualize.io/guide/testing/) and [Ratatui snapshots](https://ratatui.rs/recipes/testing/snapshots/) | Framework-level testing and snapshot guidance; complementary integration boundaries | Keep unit/widget tests as fast controls. Demonstrate the additional defect caught by the real executable path |

The Termless GitHub HTML view did not expose its README; the linked project-owned raw README was readable. No missing page was interpreted as a missing feature. Other alternatives in the prior survey—Bats, Snapbox, Tuistory, Ink testing library, Teatest and pytest-textual-snapshot—remain relevant substitutes; they were not all re-evaluated at runtime or refreshed in this pass. There is no exhaustive “all competitors” claim.

## Research implications

**Correctness and maintenance are the opportunity.** Existing contenders already offer real PTYs, snapshots and useful diagnostics. Our defensible hypothesis is that a maintainer can install, write, maintain and diagnose a small cross-language regression suite with low total effort and accurate outcomes. This needs E1/E4 measurement and later independent A1 use.

**Terminal fidelity is a concrete weakness.** Our [contract](../terminal-compatibility.md) documents one rune per cell and incomplete wide/grapheme layout. New probes should include multilingual filenames, combining text and selection adjacent to wide cells in real apps. Differential emulators can reveal disagreement; they cannot alone decide which behavior is correct. E3 requires an independently justified expectation and exact host scope.

**Real-world variation matters more than another large green total.** Existing corpus depth mostly uses pinned inputs and one runner host. Add target upgrades, meaningful state changes, fresh user directories, constrained hosts and multi-step maintenance exercises. Keep service state local and disposable. A benchmark improvement that breaks these tasks fails the milestone.

**Usability is still unknown.** Operator-authored tests do not measure beginner comprehension. Before outreach, perform disciplined clean-room operator rehearsals and label their bias. After authorized outreach, test independent first use and voluntary return. Do not claim that private engineering validates preference.

Design references reinforce this approach: [Playwright guidance](https://playwright.dev/docs/best-practices) emphasizes user-visible behavior, isolation and condition-based assertions; [pytest's flake guidance](https://docs.pytest.org/en/stable/explanation/flaky.html) discusses state/timing dependencies. Our inference is to control fixtures, retain every initial result and investigate causes rather than retry failures into green status.

## Hypotheses and falsification

| Hypothesis | Experiment | Result that rejects or narrows it |
| --- | --- | --- |
| Excess runner waiting explains short-task loss | Phase timings plus matched before/after on fixtures and real apps | Target/session semantics explain most cost, or reduction loses output/cleanup correctness |
| Standalone JSON reduces total work | Same real stateful job, count setup, helpers, edits and diagnosis | Alternative needs less total work or avoids external-oracle glue |
| Existing terminal dependency is enough for the chosen audience | Multilingual editor/selector and resize probes with cell expectations | Wrong selection/cursor/layout on a valuable task; evaluate replacement behind the existing interface |
| Existing reports make diagnosis quick | Blinded or delayed review of mixed failure classes | Operator cannot distinguish target, setup, runner and cleanup failures; later confirm independently |
| Existing corpus predicts upgrades | Freeze specs, try a later target version, classify every change | Frequent unexplained breaks or baseline churn without target regressions |

Public issue reports in the earlier survey remain qualitative historical signals, not votes or current unresolved defects. Future research should find concrete reproducible tasks, not accumulate feature requests. The [readiness plan](../archive/prelaunch-2026-10-06/plans/engineering-readiness.md) turns these hypotheses into bounded milestones, and the [scenario protocol](../archive/prelaunch-2026-10-06/plans/real-world-scenarios.md) prevents benchmark-only optimization.
