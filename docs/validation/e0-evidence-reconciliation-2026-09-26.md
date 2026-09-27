# E0 evidence reconciliation — 26 September 2026

Status: E0 audit and experiment freeze complete, with affected claims explicitly
limited below. E1/E2 are authorized but not accepted. This is operator self-review.
Starting HEAD: `c0f2b7237e70cd90103b1941b37863f0dbae2b7e`; pre-existing planning
edits are preserved. No historical run is relabeled as a fresh run.

## Evidence ledger

| Claim | Identity / host / denominator | Accessible evidence audited now | Limitation / correction |
| --- | --- | --- | --- |
| Release qualification | `f6ffeb76a7ec3b826052690ab53071dcdf0e565f`; three native hosts; ten workflows × 100 each | Three retained `attempts.jsonl` files in `artifacts/qualification-final-36106092065`; independently counted 1,000 unique host/attempt IDs per host, zero non-pass dispositions, ten cold-first labels per host; file hashes in [audit](e0-risk-audit-2026-09-26.json) | Historical evidence inspection, not 3,000 new executions. First attempt is not proof of cold acquisition/cache state. Survivor fields are runner confirmation, not a new external process census |
| Exact runner bytes | Windows `7a73b598613d34e8a05831d12f2ab26d4abae3e6ce05e63c7d80c316bcc80fc2`; Linux `2ed5c7f06d9117a4450079312ffd00001205f893bbca36fbc0ab551338171d0b`; macOS `a2a662c53d948795cae12ee931d3d4e761a4baf9e54d7ddfe76ae2cd1fa524f8` | Match ledger identities to [freeze](r6-f-candidate-freeze-2026-09-25.md) and [candidate manifest](../../release/candidate-manifest.json); matching Windows file found under `artifacts/qualified candidate extracted` | Similarly named `final qualification extracted candidate` contains different bytes (`2cb92180…`); never select an executable by directory name alone |
| CI artifact availability | Run `36106092065`, three qualification bundles | Fresh read-only `gh api repos/Wyrcan-io/playtestr/actions/runs/36106092065/artifacts`: all `expired=false`, sizes 47,601 / 43,622 / 45,798; digests match dated record | Metadata verified; did not independently redownload ZIP bytes in this audit. Local extracted ledgers are accessible; remote retention is temporary |
| Full depth | 15 projects / 120 workflow files; Windows runner, 104 native target workflows and 16 WSL target workflows | Fifteen `corpus/results/*-windows-amd64.json` records, specs, fixtures, controls, original reports under `.trial-private` and `artifacts/r6q-*`; identities retained by audit | These are recorded results. E0 does not recertify all 120 outcomes. No Linux/macOS full-depth inference |
| Risk inventory | 300 rows / 60 risk descriptions / five repeated layer labels | All 41 references resolve: 40 Go test function anchors and one BT-08 workflow. Fresh uncached Windows `go test -json` observed all 40 parent test passes, 51 distinct named subcase terminal events (one skipped) | 300 mappings are not 300 tests or subcases. Parent and child events are separate counts. Native labels are not execution evidence. BT-08 has no fresh execution in this audit and is not the three-host BT-06 repetition |
| Competitive results | `f1ab948f13937bed9c67d8e27da4eb5e26ed67cc`; Linux amd64; Atago 0.23.0, tui-test beta.5, Termlens 0.11.2 | Local `competitive-success-35750618644` contains `versions.txt`, attempt/control/install/adversarial ledgers; hashes in audit | Historical 360 attempts / 36 controls; not refreshed comparator timings. Mixed source-build/acquisition work prevents a binary-install ranking |
| Installation repair | Action `1c03904075512e67f53b0c94a13daa17f0383f1d`; failed `36168381776`, successful `36172240134` and `36173075209` | Source integration tests and [publication record](r6-publication-and-blocker-2026-09-25.md) | Original three-host 404 remains a failure. This audit did not redownload every release or inspect every historical remote job log |
| Public presentation and adoption | Website record `36222050575`; five invitations, zero recorded consents | Dated presentation and cohort records | Attributed record only; no fresh screen-reader, deployed-site, independent adoption or retention evidence |

Audit reproduction:

```powershell
go test -count=1 -json ./... > artifacts/readiness-2026-09-26/go-test.jsonl
# Windows PowerShell redirects as UTF-16: convert this file to UTF-8 before audit.
go run ./scripts/readiness/audit.go -events artifacts/readiness-2026-09-26/go-test.jsonl -out docs/validation/e0-risk-audit-2026-09-26.json
gh api repos/Wyrcan-io/playtestr/actions/runs/36106092065/artifacts
```

The JSON groups every original row ID, mapped risk, layer, source anchor,
literal subcase name and observed Windows event. Dynamic table names are counted
only from execution. It deliberately does not assign a native-host pass to each
mapping. Source-anchor existence is weaker than semantic coverage: rendering
references cover basic split UTF-8/CSI, carriage return, erase and alternate
screens, not general wide/grapheme support; `supported Unicode width` must be
read within the existing one-rune-per-cell exclusion. Layer labels for a pure
validation test do not make it a PTY test. Workspace and installer tests mix
pure and real-process subcases; their exact event names are the evidence.

Source review of the **40 mapped parent functions**, not all repository tests:
9 pure logic/filesystem tests, 27 real-PTY integration tests, 2 runner rejection
tests that deliberately prevent launch, and 2 installer subprocess integration
tests. These classifications describe test bodies; they do not multiply by five
layer labels or turn parent/child events into additional independent tests.

Known semantic mapping exceptions remain visible rather than counting the
reference's pass as proof of the risk:

| Rows | Current mapping limitation | Corrective reference / claim boundary |
| --- | --- | --- |
| WSP-026…030 | `TestWorkingDirectoryAndExplicitEnvironment` checks launch configuration, not managed-home conflict rejection | `TestWorkspaceSpecValidation/managed_env_conflict` and `/managed_inherit_conflict` are the observed rejection subcases |
| WSP-031…035 | `TestWorkspaceCancellationCleansAfterTarget` cancels after launch, not during setup | Fixture-copy `/cancelled` subcase proves cancelled copy; do not equate it with every setup stage |
| ART-011…015 | Unsafe-reference rejection is not the same as correctly displaying missing legitimate evidence | `TestRenderHTMLMixedSuiteIsOfflineEscapedAndComplete` asserts the missing-file label |
| REN-041…045 | BT-08 workflow is copied across five layer labels | Historical Windows workflow evidence only here; BT-06 repetition is a different workflow |
| REN-056…060 | Rendered string tests do not certify cell width/graphemes | Basic Unicode content only; exact wide/grapheme cell expectations are not proved |

The historical risk map is retained as the dated mapping input; the ledger is
the corrected interpretation. All affected row IDs and source events remain
auditable, without manufacturing replacement tests or execution events.

## All fifteen negative controls

Classification comes from control diffs, source/oracle inspection and the
dated per-project records. Synthetic patches are not upstream bug reports.

| Project | Classification | What it proves / does not prove |
| --- | --- | --- |
| GUM | Changed input (spec omits ArrowDown) | Unchanged Beta baseline detects selecting Alpha; no target-code defect |
| LG | Target-code mutation: StageFiles skips git add | External Git index oracle rejects screen interaction without staging |
| FZF | Target-code mutation: wrong selected record | Exact final result snapshot rejects alpha instead of beta |
| POST | Target-code mutation: response marker changed | Detects response rendering defect; does not prove saved request integrity |
| LITE | Target-code mutation: affected-row status changed | Detects status rendering defect; not transaction persistence corruption |
| MITM | Target-code mutation: filtered view loses flow | Detects missing expected flow after positive filter |
| BT | Target-code mutation: Processes → BROCESSES | Detects widget title regression |
| GUI | Target-code mutation: staging removed | External Git oracle rejects unstaged result; reserved from new tuning |
| TV | Target-code mutation: wrong selected record | Exact result mismatch; reserved from new tuning |
| NPK | Target-code mutation: DELETED → WRONG-DELETED | Detects dry-run status regression; first unrelated startup timeout is rejected control evidence |
| CV | Changed input: bundled target template package type module → commonjs | Wizard says Done while independent package oracle rejects persisted state; executable target code unchanged |
| IPM | Changed input: bundled target theme template value false | Success message while independent config oracle rejects persisted state; executable target code unchanged |
| MICRO | Target-code mutation: save corrupts bytes | Saved message while exact file-byte oracle rejects saved document |
| TIG | Target-code mutation: Enter binding removed | Detects missing opened diff; WSL target only |
| TASK | Target-code mutation: d binding → D | Detects missing completion prompt; WSL target only |

Total: 12 recorded executable target-code controls, three changed-input controls
(one keyboard sequence and two bundled template inputs); zero
dependency-only, baseline-only or expectation-only controls in this roster.
The bundled templates are target-owned source assets, but this audit does not
count template-data edits as executable code defects. E1 adds a genuine
create-vite JavaScript mutation separately. The patched controls use changed launch selection/configuration to choose the patch, but that
does not make them expectation mutations. Baseline mismatches prove target
defects only when the target behavior itself changed, as in FZF/TV. Historical
controls are not automatically accepted E1 controls for the richer tasks.

## Corrections and ranked investigations

1. **Correctness / real-task impact:** Posting `verify("save", …)` only checks
   no HTTP requests. It does not read a persisted file, despite POST-05 metadata
   saying it does. Strengthen the oracle and run a save corruption control before
   admitting that claim. Likewise LG-01's current setup only modifies alpha;
   the dated statement that beta remains unstaged overstates a distracting-change
   task. E1 must introduce and independently check that neighboring change.
2. **Cleanup:** CV-02 historical cleanup timeout remains unresolved causally.
   The 20 recovery reports are retained. Nine entries/no survivor is reported
   context, not proof of host-resource causation. Hypotheses: deletion deadline,
   delayed file release, scheduling/antivirus/OneDrive contention. Preserve the
   failure; do not shorten cleanup budgets or add automatic retries.
3. **Real-task availability:** Posting historical startup/timeouts after a long
   suite may be host contention, fixed-port availability or target/runtime
   startup. Recovery does not isolate cause. Keep serial order, first reports,
   port/listener state and resource observations in E1.
4. **Installation correctness:** checksum contract mismatch is a reproduced,
   repaired historical defect. Keep both manifest formats and safe failure
   publication regression tests; do not mutate released assets.
5. **Measurement correctness:** `reportMetrics` assigns first-step duration to
   `target_startup_ms` and `max(0, wall-report)` to `runner_overhead_ms`.
   Interpret them as **first-step wait** and **outside-reported-run residual**.
   Neither isolates startup or runner overhead. `wait_for_redraw` duration is a
   synchronization window, not necessarily an intentional fixed sleep. Retain
   old raw field names/values as history, but withdraw the causal interpretation.
6. **Maintenance / performance:** no target-upgrade evidence establishes the new
   E1 boundary. Existing Linux speed loss remains 295–305 ms vs 49–54 ms on
   owned short tasks. Profile only after valid controls; quiet/grace/drain/polling
   explanations are hypotheses.

Missing native access and independently recovered remote logs limit affected
claims, not this audit's completion. The [frozen experiment](e0-experiment-freeze-2026-09-26.md)
sets the next executable scope. E3–E5, outreach, releases and remote mutations
remain outside this authorization.
