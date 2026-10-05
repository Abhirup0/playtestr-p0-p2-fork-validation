# Adoption and PR workflow preparation — 5 October 2026

Status: implementation, material preparation, authorized source push and hosted validation complete. Website deployment and outreach remain pending. This record describes the current task, not completion of independent adoption or commercial validation. The user explicitly requested execution of the [adoption prompt](../plans/adoption-and-pr-workflow-execution-prompt.md), then authorized committing and pushing the prepared package.

## Baseline and scope

Source checkout began at `326650d` with existing user changes to AGENTS.md and the planning index, and three untracked execution prompts. Those changes are preserved. Read-only GitHub release checks confirmed latest stable `v0.1.0` and newest published prerelease `v0.4.0-rc.3`; the trial uses rc.3 for suites/reports/workspaces. No runner source, compiler/dependency pin, schema, release asset, setup Action or tag was changed. New functionality is a separate standard-library Python summary helper and an adopter workflow.

Existing assets reused: the mission-control demo and its build-time `diagnosticsSuffix`, committed menu specs/snapshot, report v1/v2, offline renderer, checksum-verified setup Action, website templates/test tools, release qualification and wide-character investigation. The article describes that historical repair; it is not a new fidelity or performance experiment.

## Implementation and outcomes

- `scripts/ci/report_summary.py` reads at most 8 MiB, accepts 1–1000 results and at most 10,000 aggregate steps, validates the metadata/counts it consumes, and renders at most 100 problem rows. It bounds appended output to 256 KiB, escapes metadata, excludes failure prose/screens, checks evidence presence only within the resolved evidence root, and never launches targets. It is not a full JSON Schema validator.
- `.github/workflows/terminal-pr-example.yml` uses a named Linux host, read-only permissions, pinned action commits and the actual Go demo. Its test step has no failure suppression. Later HTML, summary and upload steps run after failures where the platform permits; hard cancellation may prevent them. Fork execution needs no secrets or write token. No PR comment publisher or GitHub App exists.
- `scripts/ci/capture_demo.py` executes the actual published Windows rc.3 binary through normal target, deliberately seeded output defect and unchanged recovery. Final capture: exits 0/1/0, defect `snapshot_mismatch`, cleanup confirmed in each case, unchanged spec/baseline hashes, HTML and Markdown generated for each.
- Trial kit, article, current tool-choice note, launch drafts, four-week plan and sustainability recommendation are linked from [the review index](../adoption/README.md). Five individualized candidate drafts and route-policy uncertainties are in an ignored private packet. No invitations or posts were sent.
- Read-only reconciliation of five old invitation threads found four with no comments and one explicit refusal. The private ledger now marks no further contact for that recipient. The public cohort records only the aggregate response/decline, with zero consents and qualifying participants. The September zero-response statements remain dated history.

## Provenance

Previously downloaded public archive `playtestr_0.4.0-rc.3_windows_amd64.zip` was rehashed as `b159cd8f638f231c278b485565663dfe8fe323f97e3edf0c86fe7077239a406f`, matching `site/data/prerelease.toml`. Final capture executable SHA-256: `531804dcb5f29bdcc9d9e2650b1be86e083eedd34c4545ebff1654f05d33f16a`. It is the published Go 1.26.0 runner, not a newly built runner. Demo target builds used local Go 1.27.0 on Windows amd64.

Final capture lives in ignored `artifacts/adoption-demo-final/`: `capture.json`, `transcript.txt`, per-case logs, reports, screens/diff, HTML and Markdown. Spec hash `c828d38077bd4123196eac294638dc89907e58833d4e0640bc27b02835a7b6d3` and baseline hash `96bbce2386a3ab5e113225d126bbedbd674e1bcc28f33c657c4d621604aa3eb4` remained identical across all three cases. The recovered target binary hash equals the initial good target hash. These are three operator executions, not repeat independent adoption. The captured runner also matched the executable bytes read directly from the checksum-verified archive. An unedited Chrome screenshot of the actual failed HTML is included at `site/static/images/adoption/seeded-defect-report.png`, SHA-256 `0e44c23370f578dea5770e870e50d7c8d4cfcd5a7eab4c704c0bb0d8f1e5ad2d`. The draft article is 993 words.

Action revisions were resolved through public GitHub tag APIs: checkout v6 `d23441a48e516b6c34aea4fa41551a30e30af803`; setup-python v6 `ece7cb06caefa5fff74198d8649806c4678c61a1`; setup-go v7 `b7ad1dad31e06c5925ef5d2fc7ad053ef454303e`; upload-artifact v6 `b7c566a772e6b6bfb58ed0dc250532a479d7789f`. The existing setup Action commit `ae97c62022966cde9699b26169b4dc6ef0a12439` was confirmed. Tag/API checks prove identities, not successful execution of the new workflow.

## Checks and retained failures

| Check | Actual result |
| --- | --- |
| `python -m unittest discover -s scripts/ci -p 'test_*.py' -v` | Eight top-level tests pass, covering versions/statuses, missing/malformed/empty reports, contradictory pass/counts, injection/privacy, evidence-root/missing files, row/input/append bounds and CLI alias/URL rejection. |
| `.tools/actionlint-1.7.12/actionlint.exe .github/workflows/terminal-pr-example.yml .github/workflows/test.yml` | Passed with no diagnostics. This is workflow lint, not native Actions execution. |
| `go test ./...` with project-local `.cache/go-build` | Passed all packages on Windows. No Go source changed. |
| `go vet ./...` with the same cache | Passed. |
| Published rc.3 + `capture_demo.py`, fresh `artifacts/adoption-demo-final` | Pass/seeded failure/recovery and all three HTML/summary renders passed. |
| Published rc.3, normal demo, `examples/menu.json examples/menu-exit.json` | Both specs passed, 12/12 steps; offline HTML and summary generated under `artifacts/adoption-workflow-local`. |
| Website build/static | Passed: 40 HTML pages, required links/assets/schema checks; final build includes the new walkthrough and unedited report screenshot. |
| Browser checks | Chromium 9/9 and WebKit 9/9 passed in the installed-browser run; Firefox 9/9 passed in the separate run outside the command sandbox. All ran locally on Windows, not native macOS/Linux browser hosts. |

The first Go check could not access an entry in the shared build cache; switching GOCACHE to a project-local directory resolved it. A later demo build emitted a shared module-cache stat warning but returned success; the capture separately checks every build's exit and target hash.

Two initial demo captures retained their failure at seeded HTML rendering. Their absolute Windows evidence paths were rejected as URI-like references by the existing renderer. The capture was corrected to pass invocation-relative artifact/report paths, matching the example workflow. No release bytes were patched or report evidence rewritten to hide the failure. The failed directories `artifacts/adoption-demo/` and `artifacts/adoption-demo-verified/` remain intact.

The first website-browser attempt lacked the pinned browser executables. They were downloaded into ignored `.tools/playwright-browsers`, then Chromium and WebKit passed 18 checks. Firefox reproduced a page-creation TypeError even in an about:blank probe inside the command sandbox; its nine checks then passed outside the sandbox without changing tests or site code. The final Firefox JSON is retained in `artifacts/adoption-browser-firefox-final.json`. The mixed-run JSON is retained in `artifacts/adoption-browser-first-installed.json`. An initial PowerShell call to npm was blocked by the host script policy; using npm.cmd resolved that invocation issue. An intermediate website check failed because the review index referred to this record before it was created. Final link checks include the completed record. Network access to public release APIs required command-specific sandbox escalation; all actions were read-only. No automatic approval rejection occurred.

## Remaining boundaries

The new workflow and native helper results are recorded below. Existing release qualification remains separate historical evidence. No concurrency or process-lifecycle code changed, so an additional race campaign was not required for this slice.

The source package was committed and pushed after explicit authorization; the article is now publicly accessible as a repository draft. No site deployment, blog publication, invitations, comments, PR/issue/discussion mutations, sponsorship setup or service spend occurred. New website routes must not be announced as deployed. Human trial consent, unaided first use, diagnosis effort, voluntary return and paid demand remain unobserved. HN's current generated-text prohibition is recorded; no HN-ready AI draft was prepared.

The [machine-readable local record](adoption-preparation-2026-10-05.json) retains capture outcomes, runtime identities, final file hashes and browser-result counts. No costs or human hours have been measured. Browser dependencies were downloaded locally; no service or paid runner was purchased. Private candidate drafts and refusal data remain ignored.

The original missing-browser run completed after the task-owned preview server was terminated; its 27 prerequisite failures are retained in `artifacts/adoption-browser-missing-prerequisites.json`. The final accepted browser evidence remains the separate installed-browser and Firefox runs above. Preview termination was confirmed by the process API. The final summary-helper code was also run successfully on all three captured reports, writing `summary-final.md` without rerunning the targets or changing evidence.

## Hosted validation after authorized push

The owner explicitly approved committing and pushing the prepared package. Commit `30edcc34e44cb66e4e0cfce29a006e37f0031df8` was pushed to `main`; existing edits to AGENTS.md, the planning index and the two unrelated execution prompts were excluded. The Website workflow was inspected before pushing: deployment requires an explicit `workflow_dispatch` with `publish=true`, so the push only built and checked the site.

| Hosted check at that source commit | Actual result |
| --- | --- |
| [Normal PR-example run](https://github.com/Wyrcan-io/playtestr/actions/runs/37328072239) | Passed on Ubuntu 24.04; published rc.3, two specs, 12 passing steps, confirmed cleanup. HTML, job summary and artifact upload steps succeeded. |
| [Seeded regression](https://github.com/Wyrcan-io/playtestr/actions/runs/37328099210) | Expected failed check. The menu snapshot failed with `snapshot_mismatch`; the exit spec passed. HTML, job summary and artifact upload still succeeded. Downloaded actual screen/diff and HTML contain `Diagnostics: all systems healthy.REGRESSION`; cleanup confirmed for both results. |
| [Unchanged recovery](https://github.com/Wyrcan-io/playtestr/actions/runs/37328210937) | Passed after dispatching with defect injection disabled, at the same source commit and with unchanged specs/baseline. Two specs and all 12 steps passed; cleanup, HTML, summary and upload succeeded. |
| [Native terminal tests](https://github.com/Wyrcan-io/playtestr/actions/runs/37328072077) | All three jobs passed: ubuntu-latest, macos-latest and windows-latest. Each actually executed the new summary failure-control tests, Go tests/vet, real terminal acceptance and expected-failure checks. |
| [Native gap checks](https://github.com/Wyrcan-io/playtestr/actions/runs/37328072333) | All focused integrated-hardening jobs passed: Linux amd64, macOS arm64 and Windows amd64. This existing workflow also ran automatically on the push. |
| [Website](https://github.com/Wyrcan-io/playtestr/actions/runs/37328072029) | Hosted Linux build/static checks and all 27 browser checks passed, zero skipped/unexpected failures. Downloaded browser JSON confirms the count. Deploy job was skipped. |

Commands: `git commit` and `git push origin main`; normal example/native/site checks were push-triggered. `gh workflow run terminal-pr-example.yml --ref main -f inject_regression=true` supplied the expected failure; the same dispatch with `false` supplied recovery. `gh run view --json status,conclusion,jobs` verified completed job/step outcomes; `gh run download` retrieved all three example artifacts and website browser evidence. Ignored `artifacts/adoption-hosted/` retains reports, failed screen/diff, HTML, run metadata and browser JSON. Report hashes and run IDs are in the machine-readable record. Job-summary step success is verified from job metadata; summary text is not part of the downloaded evidence artifact.

These checks establish the repository-owned demo workflow and helper tests on the named hosts. They do not establish external fork-PR execution, third-party adoption, unrestricted terminal compatibility or paid demand. Source publication and hosted validation were the authorized external actions; no invitations, PR/issue/discussion mutations or website deployment occurred.

The documentation follow-up initially used a relative link to this validation record from the demo page. The site check caught that the record has no generated website route; the link was corrected to its repository URL and the final build/static check passed.
