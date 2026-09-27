# Decisions, unresolved questions and scope control

Updated 26 September 2026. The [root roadmap](../../roadmap.md) fixes order; this register makes choices and revisit triggers visible. A proposed feature is not approved merely because it has a row.

Current execution status updated 27 September: E0–E5 accepted within recorded boundaries; v0.4.0-rc.2 qualified privately. Publication and outreach remain held. The dated decisions below retain the earlier partial states.

28 September override: the user authorized exact-byte download publication and
public verification, now complete. Outreach and marketing are explicitly
prohibited; A1/A2 remain unstarted even after technical readiness.

## Current sequencing override

D21 supersedes D01's immediate R6-to-A1 scheduling and the old fixed stop at Sprint 14, at the user's explicit request on 26 September. Completed engineering and evidence-backed deferrals stay complete. E0-E5 are a finite new phase, not an indefinite parity campaign. Further outreach is held; recorded prior invitations remain history.

## Decisions made for the previous batch

| ID | Decision | Reason and consequence |
| --- | --- | --- |
| D01 | Complete finite engineering batch and R6 before A1 recruitment | Explicit user preference; compensate with public research, operator pilots and a fixed stop at Sprint 14 |
| D02 | Verify existing S8/S9 native behavior early at 13-A0 | Platform/lifecycle risk should surface before new features amplify it |
| D03 | Five pilots before implementing full corpus | Broad 120-case inventory is useful; building every case before reducing blockers wastes work |
| D04 | Freeze executable/version before 3,000 repeats | Expensive results must apply to final candidate bytes; avoid a circular “finish campaign before freeze” gate |
| D05 | State checks have an explicit lifecycle contract | Successful workspace deletion prevents naive post-run inspection; use proven external resource/adapter/owned-cwd approaches |
| D06 | Existing report-v2 HTML is verification work | Source and S9 evidence already contain implementation; avoid speculative duplicate work |
| D07 | At most one compatibility family plus one conditional input/assertion family | A finite feature budget keeps breadth in tests rather than API surface |
| D08 | Manifest/reproduce commands conditional on failed manual handoff | Existing spec/report/fixture/version instructions may solve the task; no new replay system by default |
| D09 | Runner remains serial; corpus CI may shard independent jobs | Large validation volume does not justify a user-facing parallel scheduler |
| D10 | Native application claims are version/workflow/host-specific | Language diversity, framework examples and WSL do not prove all-platform compatibility |
| D11 | No version per sprint; no forced v1.0 | Releases express qualified coherent behavior and contract policy, not number of tasks completed |
| D12 | Documentation-only audit does not rerun PTY test suite | Check links, provenance, feasibility and consistency; later implementation must execute relevant tests |
| D13 | Defer Sprint 10 without a qualifying pilot blocker | All five admitted pilots complete their intended current flows; BT-06 redraw passes and no reduced application case demonstrates wrong terminal cells/protocol behavior. Reopen only with the evidence in the Sprint 10 decision record. |
| D14 | Defer both Sprint 12-B extension candidates | No two admitted workflows share a missing input family or unavoidable dynamic-text blocker after fixture/state control. Keep strict formats unchanged; reopen only with two named reduced failures. |
| D15 | Defer the Sprint 6 reproduction manifest | A clean-directory `GUM-01` failure, corrected pass and missing-target control were fully classified from ordinary pinned inputs and existing evidence. Add software only after a repeated safe context omission survives the written handoff. |
| D16 | Setup action reports both archive and executable SHA-256 and rejects non-native target overrides | The immutable action identity and selected runner release remain independent. Successful outputs are transactionally published only after native mapping, extraction, version and staged/final executable identity checks all pass; a publication failure rolls back the fresh install and output files. |
| D17 | Keep the Sprint 13-C comparison factual, task-specific and Linux-only | All four tools detected the three reviewed mutations in 360/360 fresh attempts, while Playtestr was slower on these short tasks. Only Playtestr supplied the exercised raw-output cap; alternatives retain finite-drain labels instead of artificial failures. No universal winner or cross-host claim follows. |
| D18 | Close Sprint 11-B at depth while retaining host exclusions | The corpus now has 15 exact projects, 120 distinct workflows, 300 focused risk cells, 15 intended defect detections/recoveries and two reviewed boundary workflows per project. Thirteen targets are native Windows; TIG and taskwarrior-tui are Linux-under-WSL evidence only. Native application breadth is deferred honestly to candidate qualification rather than inferred. |
| D19 | Select and qualify `v0.4.0-rc.1` without stable relabeling | Exact-version setup plus opt-in workspace/report v2 is a coherent minor prerelease. V1 remains the downgrade boundary; changing the embedded version changes bytes and requires qualification. |
| D20 | Close R6-Q with exact hash evidence and retain transient failures | The 120-workflow matrix, 15 intended negatives/recoveries and 3,000 unique first attempts passed. CV-02 and Posting host transients remain recorded; WSL target rows are not native app claims. |

## Decisions from the 26 September review

| ID | Decision | Reason and consequence |
| --- | --- | --- |
| D21 | Add finite E0-E5 readiness before further outreach | User requested deeper R&D and real-scenario competitive improvement; [plan](engineering-readiness.md) defines scope, budget, evidence and stop decision. No implementation authorized by this planning pass. |
| D22 | Audit risk rows and mutation provenance before enlarging campaigns | 300 rows reference 41 distinct strings; no inference of 300 independent tests. Real target defects must be distinguished from mismatched baselines/specs. |
| D23 | Retain task-level wins, ties, losses and unknowns | Speed cannot compensate for false passes; operator success cannot establish independent preference; universal superiority is not claimed. |
| D24 | Accept E0 audit; keep E1/E2 partial | [E0 ledger](../validation/e0-evidence-reconciliation-2026-09-26.md) separates 300 mappings, 40 test anchors and one workflow, fixes timing interpretations and distinguishes executable patches from template/input controls. Missing evidence stays missing. |
| D25 | Repair state oracles and readiness before optimization | [Local execution](../validation/e1-e2-local-readiness-2026-09-26.md) adds exact Git/SQLite/request/scaffold state and save/reopen controls. Preserve first harness failures, stale readiness and input-transition failure. No runner safeguard reduction or unsupported performance win. |
| D26 | Do not infer native acceptance or competitor cleanup from local task passes | Required Linux/macOS lanes and matched resource/comparator cells remain open. Termless menu task works, but its console-helper stderr leaves cleanup unqualified. E3-E5 and outreach remain unstarted. |
| D27 | Continue local diagnostics; hold conditional push until E0-E2 acceptance | User confirms no native endpoint is available. Fresh Windows sampled-resource and reduced node-pty cleanup findings improve evidence but cannot replace required native cells or matched comparisons. Preserve instrumentation/operator failures and keep E1/E2 unaccepted. |

## Decisions from 27 September execution

| ID | Decision | Reason and consequence |
| --- | --- | --- |
| D28 | Use standard GitHub-hosted native runners under explicit authorization | No physical devices or SSH hosts are needed. Actual Linux/macOS execution, artifact retrieval and testing-branch pushes are authorized; configured workflows alone remain insufficient proof. No paid runners, publication or outreach. |
| D29 | Accept E1's admitted six-journey native scope | Five-good/source-defect/recovery on all three hosts, scheduled variations and three synthetic maintenance cases pass. Preserve wide-cell failure and unisolated Posting query editing; synthetic changes and unknown human minutes are not upstream-upgrade or independent-effort claims. |
| D30 | Accept E2's measured Unix parent-slave ownership repair and honest tradeoffs | Same-source regression fails before/pass after on Linux; macOS baseline already reaches EOF. Matched short/real-task and paired 1/10/50 suites preserve exact state, output and cleanup. Source safeguards remain fixed. Create-vite ties Atago; Lazygit still loses with an unisolated first-assertion wait. New bytes remain unpublished and require E5 qualification. |
| D31 | Accept E3 investigated deferral across all hosts | Reduced one-rune/one-cell behavior explains unreliable wide/combining layout; retain original failures and exact-state/basic-character workarounds, maintainer owns revisit. |
| D32 | Accept E4 scoped operator evidence and necessary correctness repairs | Four walkthroughs, eight synthetic changes, six diagnoses, bounded installer reads and macOS final-output regression/native gates; human timing/accessibility excluded, no new convenience family. |
| D33 | Qualify unused private v0.4.0-rc.2 and recommend scoped trial | Exact native archives, 3,000 first attempts, holdout controls, compatibility and resources accepted. Differentiation unmet; public availability, release, deployment and outreach remain held. |

## Decisions to make at explicit checkpoints

| ID | Question | Owner / deadline | Evidence needed / default |
| --- | --- | --- | --- |
| Q01 | Which terminal family blocks the most valuable pilot? | **Closed 2026-09-21: none qualifies; Sprint 10 deferred** | [Decision record](../validation/sprint-10-decision-2026-09-21.md); reopen only with a reduced failing real case and independent expectation |
| Q02 | Extra input or focused region? | **Closed 2026-09-21: neither qualifies; 12-B deferred** | [Decision record](../validation/sprint-12-b-decision-2026-09-21.md); reopen only with two distinct named blocked workflows and failed fixture/state-control workarounds |
| Q03 | Does CI handoff need new software? | **Closed 2026-09-21: no; Sprint 6 manifest deferred** | [Experiment](../validation/sprint-6-handoff-2026-09-21.md); reopen only for a repeated context omission the ordinary handoff cannot safely prevent |
| Q04 | Which candidate projects cannot meet host/task depth? | **Closed 2026-09-24 for task depth** | All 15 pins reached eight workflows and a defect control; TIG and taskwarrior-tui retain explicit native-host exclusions for qualification. |
| Q05 | What next version and compatible migration? | **Closed 2026-09-25: `v0.4.0-rc.1`** | V1 remains compatible; v2 workspace/mixed reports need the new reader. Remote novelty checked; migration/rollback is documented. |
| Q06 | How to retain reproducible evidence affordably? | **Closed 2026-09-24 for discovery depth** | Checked-in corpus metadata is 384,243 bytes; screen artifacts and raw reports remain ignored/private, while compact result records preserve hashes, outcomes, costs and exclusions. R6-Q defines its own bounded attempt ledger. |
| Q07 | Is a comparison task fairly supported by all chosen tools? | **Closed 2026-09-22 for C1-C3 on Linux amd64** | [Measurement record](../validation/sprint-13-c-competitive-2026-09-22.md); raw-output limiting and cancellation models remain explicitly non-equivalent |
| Q08 | Can genuine installer upgrade be shown in this batch? | **Closed 2026-09-26 at R6-V** | Same immutable action verified public v0.3-to-v0.4 upgrades on all three hosts; [record](../validation/r6-publication-and-blocker-2026-09-25.md). Future release upgrades need their own evidence. |
| Q09 | How do strict formats interact with patch-addition wording? | **Closed 2026-09-25** | New reader accepts old v1 documents; old strict readers may reject v2/new documents. V2 is opt-in and not silently downgraded. |

Do not silently pick a new format version during implementation. Document alternatives and cost at the relevant checkpoint; the maintainer reviews the concrete contract before it is presented as stable. Routine implementation choices within accepted scope do not need repeated permission requests.

## New phase checkpoint questions

| ID | Question | Owner / deadline | Evidence / default |
| --- | --- | --- | --- |
| Q10 | Which claims retain reproducible raw evidence and distinct test execution? | **Closed at E0 audit boundary** | [Ledger](../validation/e0-evidence-reconciliation-2026-09-26.md); missing historical evidence remains missing |
| Q11 | What causes the speed gap and can it be reduced safely? | **Closed at E2 investigation boundary** | [Native record](../validation/e1-e2-native-readiness-2026-09-27.md): Linux final drain explained and repaired; remaining RW1 readiness cost and human-effort comparison remain explicit gaps |
| Q12 | Which fidelity family blocks a useful real task? | **Closed at E3 investigated deferral** | [Native MICRO-08 and reduced cells](../validation/e3-fidelity-boundary-2026-09-27.md); wide/combining cursor layout and query-dependent flows excluded |
| Q13 | Does total authoring/maintenance effort beat an applicable alternative? | **Closed as unmet/unknown at E4** | [Four walkthroughs and task scorecard](../validation/e4-operator-readiness-2026-09-27.md); human total effort unknown, two meaningful advantages not demonstrated |
| Q14 | Is evidence sufficient to resume a scoped trial? | **Technical boundary closed at E5; user decision held** | [Qualified private recommendation](../validation/e5-qualified-readiness-2026-09-27.md); differentiation unmet, independent demand unknown. Publication and specific outreach still require separate authorization |

## Backlog admission table

| Idea | Current disposition | Revisit trigger / smallest possible response |
| --- | --- | --- |
| JUnit | Deferred | A named CI consumer cannot ingest current evidence; one bounded exporter, no CI orchestration |
| Parallel runner | Deferred | Measured user suites exceed accepted duration after profiling; resource separation proven |
| Broad mouse input | Deferred | Two important keyboard-inaccessible adopter flows; selected protocol only |
| Styled snapshots | Deferred | Text cannot detect a real visual regression users need; reviewed representation and compatibility policy |
| Recorder/code generator | Deferred | A1 shows manual authoring causes repeated abandonment despite recipes; start with small template assistance |
| New SDK/language DSL | Deferred | Repeated retained users cannot express necessary deterministic flow in current contract |
| Failure minimization | Deferred | Stable reproducible failure identity and repeated manual shrinking burden |
| More installer channels | Deferred | Measured requested channel plus maintenance owner; archives/action remain useful |
| AI/MCP sessions | Outside batch | Separate product decision supported by actual user job; no autonomous game exploration |
| Hosted evidence/history | Deferred to A2 | Independent repeat use, repeated collaborative need and one paid pilot |
| Billing/accounts/PR bots | Deferred | Paid value and privacy/operating economics established; never a local-run prerequisite |

Every new accepted item needs task, evidence, minimum solution, regression proof, cost, owner and a displaced priority or later slot. A competitor release alone is not a trigger. Do not append optional work beyond E0-E5 for these ideas without a revised scope decision and displaced priority.

## Main risks and early warning signals

| Risk | Early signal | Mitigation / stop condition |
| --- | --- | --- |
| Demand assumptions outlive engineering | E0-E5 grows without stronger real-task evidence | Fixed phase budget and E5 decision; independent preference remains unknown until authorized A1 |
| Test count inflation | Same flow renamed for hosts/viewports | Stable IDs, distinct-task review, separate repeat counters |
| Oracle validates the wrong state | Screen green but Git/file state differs | Independent exact state checks and failing-oracle controls |
| Adapter invalidates real-process coverage | Signals/input differ from direct launch | Native parity checks or use owned-cwd harness alternative |
| Dynamic data causes noisy snapshots | Baselines change without target defect | Control data, choose meaningful assertions, isolate limited region only if justified |
| Scope masking | Bad cell removed to get all-green report | Keep denominator and issue; previously promised correctness blocks promotion |
| CI cost/maintenance growth | Campaign exceeds measured estimate or artifacts explode | Pilot cost model, shard fixed work, preserve compact ledger, never weaken assertions to save time |
| Late freeze invalidates effort | Rebuilding runner/version after long campaign | R6-F precedes repeat campaign; hashes enforce evidence reuse |
| Overstated competitor win | Different target/host or tuned versus naive recipes | Matched protocol, unsupported states and losses published |
| Platform claim creep | Windows/WSL result described as three-host coverage | Native per-cell ledger; same release hashes as advertised |
| Release promises exceed staffing | SLA/support promises before an owner exists | Explicit maintenance boundary; commercial promises require costed paid pilot |

## Decision record form

Record ID/date, task/evidence, alternatives considered, selected smallest scope, exclusions, affected format/version, maintenance cost, acceptance proof, owner, and revisit trigger. Link it from the checkpoint and root roadmap. An unresolved question stays unresolved until evidence or an explicit scoped decision closes it.
