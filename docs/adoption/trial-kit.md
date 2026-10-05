# One useful terminal test

Draft participant guide, 5 October 2026. Optional trial; no participant is enrolled by this document. Use published `v0.4.0-rc.3` for these suites, reports and workspace instructions. Stable v0.1.0 supports a smaller feature set.

## Try the runner

Use the [exact-version installation guide](https://wyrcan-io.github.io/playtestr/docs/prerelease-installation/) for your host. It names the archive, SHA-256 verification and extraction commands for Windows amd64, Linux amd64 or Apple silicon macOS. Put the extracted binary on your chosen PATH or invoke its absolute path. Confirm `playtestr --version` prints `playtestr v0.4.0-rc.3`. Your target and its runtime must be installed separately. Test only explicitly trusted targets; PTY execution is not a sandbox.

For a complete first interaction, clone the Playtestr checkout containing this kit and install Go for the repository-owned demo. From its root:

```sh
go build -o bin/demo ./cmd/demo
playtestr test --artifacts-dir artifacts/trial/screens --report artifacts/trial/results.json examples/menu.json examples/menu-exit.json
playtestr report --input artifacts/trial/results.json --evidence-root artifacts/trial --output artifacts/trial/report.html
```

On Windows, build with `go build -o bin/demo.exe ./cmd/demo`; the menu spec resolves that native executable. Open `artifacts/trial/report.html` offline. A controlled demo failure uses `go build -ldflags '-X main.diagnosticsSuffix=REGRESSION' -o bin/demo ./cmd/demo` (use `bin/demo.exe` on Windows), then the same test command. Expect runner exit 1 and a screen diff. Restore the normal build and rerun the unchanged test to recover exit 0. Do not run `--update` to hide the defect. Each invocation keeps its own screen directory; use separate report filenames if retaining every outcome.

## Protect your own interaction

Choose one local keyboard flow you already care about: selecting an item, dismissing a modal, saving an edit or correcting a wizard input. Use a small disposable fixture and an explicit target pin. Keep production accounts, real databases and personal files out of the trial.

Adapt a [selector, stateful wizard or full-screen recipe](https://wyrcan-io.github.io/playtestr/docs/recipes/) to your actual executable, viewport and meaningful readiness text. Specs invoke commands directly; shell syntax is not interpreted. After each input or resize, wait for evidence of the new state before taking a snapshot. Record prerequisites and installation separately from authoring time.

First get a good case. Then introduce a reviewed, reversible defect or known incorrect fixture that should fail, retain the report, and recover with the same test. If the valuable result is a saved file or database update, verify that state independently; plausible screen text alone cannot prove persistence. The existing stateful recipes show adapter/oracle approaches. Treat a missing dependency as a setup failure, not a caught product regression.

Keep your faster unit/widget tests. Add [CI](https://github.com/Wyrcan-io/playtestr/blob/main/docs/ci-installation.md) only if this terminal test is useful. The PR summary workflow passed hosted normal/failure/recovery verification; it is a separate source addition, not included inside the downloaded rc.3 binary. Use this source guide until the updated website documentation is deployed.

## Limits, feedback and removal

Snapshots compare text, not colors or styles. Combining clusters, emoji/ZWJ sequences, bracketed paste and target-visible terminal queries remain outside the supported contract. Query-dependent tasks or unsupported keys may make a chosen flow unsuitable. Report the blocked flow; there is no obligation to keep using the tool.

Use the [support route](https://wyrcan-io.github.io/playtestr/support/) to provide a small sanitized reproduction. Share runner/target versions, host, viewport, spec and expected versus observed outcome; review screens before sharing. Screens can contain data printed by the target. Consent to a trial does not permit publishing your name, quote, screenshot or project outcome. Ask for separate permission for each.

Remove the installed binary and any PATH entry you added when finished. Delete copied trial specs/workflow/helper files you no longer want. There is no account or subscription. Retained local workspaces/artifacts need explicit removal; shared CI artifacts follow their configured retention policy.

## Five feedback questions

1. What was the last relevant terminal regression, and how did you find or reproduce it?
2. What do you currently use to test this interaction, and what does that method do better?
3. Where did installation or the first test become confusing or fail? Did you stop or need help?
4. Could you explain the deliberate failure from its evidence? What information was missing?
5. Would you retain this particular test or voluntarily use the tool again? Why or why not?

## Private observation template

Copy this table into an ignored private trial record. Do not commit identities or raw feedback without permission. Blank outcomes mean unobserved, never passed.

| Field | Record |
| --- | --- |
| Opaque trial ID and permission reference | |
| Date, target/runner pins, host and valuable flow | |
| Current alternative and reason to retain it | |
| Prerequisite/install elapsed time; measurement basis | |
| Unaided first attempt; authoring elapsed time | |
| Failures, abandoned attempts and reason | |
| Maintainer/agent assistance: exactly what was done | |
| Good, deliberate bad and unchanged recovery evidence | |
| Diagnosis: participant explanation and observed time | |
| Baseline review and changes needed | |
| Participant-owned CI result, actual run link | |
| Later separate voluntary use: date and evidence | |
| Consent for contact, quotation, name, screenshot | |
| Decline/opt-out; further contact prohibited | |

A completed operator demonstration does not fill participant rows. The formal [A1 protocol](../plans/release/07-maintainer-adoption.md) retains its own thresholds.
