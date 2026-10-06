# Reviewed recorder examples

These ordinary strict v1/v2 specs were produced with the source recorder, reviewed and freshly replayed before export. They are development examples, not three independent campaign projects.

Build `bin/playtestr`, `bin/demo` and `bin/fixture` from this source (`.exe` on Windows). Install the pinned external selector with `GOBIN` pointing at `.tools/external`: `go install github.com/charmbracelet/gum@v0.17.0`. Set `PLAYTESTR_GUM` to the absolute resulting executable path. The target wrapper reads only the synthetic `fixtures/selector/choices.txt`; it drives actual Charm Gum. `PLAYTESTR_DELAY_MS` is an explicit optional inherited synthetic redraw delay.

Run from repository root:

```sh
playtestr test examples/recorded/wizard.json examples/recorded/selector.json examples/recorded/fullscreen.json
```

Wizard covers typing, resized dimensions, fresh fixture/home/temp and a saved-file verification before workspace cleanup. Selector chooses Beta in independently maintained Gum v0.17.0. Full-screen navigates mission control and snapshots diagnostics. [Recorder guide](../../docs/recording.md) explains how to produce/maintain these tests and distinguish intended updates from regressions.

`python scripts/acceptance/recorded_journey.py` records fresh copies, runs ten delay-varied replays per example, mutates actual target behavior/configuration with unchanged tests/baselines, preserves a failing report, restores and replays, then proves a manual JSON edit. It writes only synthetic development evidence under ignored `artifacts/p0-p2-recorded` and fresh private drafts under `.cache/p0-p2`. `--export-examples` creates these committed examples only when their output files do not already exist; it never overwrites their baselines.
