# Execute conditional roadmap branches when their evidence qualifies

Prepared 2 October 2026. Use under an instruction to execute roadmap work;
this document supplies acceptance criteria, not publication or contact permission.

Review the current source and recorded evidence for each branch:

| Branch | Entry evidence | Smallest permitted implementation |
| --- | --- | --- |
| S10 terminal fidelity | Reduced failing useful application task with an expectation independent of Playtestr; original selected CJK repair already ships in rc.3 | One demonstrated terminal family, isolated behind the terminal boundary |
| S12-B authoring | Two distinct blocked admitted workflows sharing one missing input family, or unavoidable dynamic text after fixture/state control | One finite input family or one bounded region mechanism |
| S6 handoff | Repeated safe context omission surviving the ordinary pinned-input handoff guide | Minimal evidence-backed handoff change; software only if the guide cannot solve it |

Existing exclusions for combining clusters, emoji/ZWJ, ambiguous width and
terminal queries are limitations; they are not automatically qualifying tasks.
Read the original decision records before changing a gate:
[S10](../validation/sprint-10-decision-2026-09-21.md),
[S12-B](../validation/sprint-12-b-decision-2026-09-21.md),
[S6](../validation/sprint-6-handoff-2026-09-21.md).

For each branch, record triggering workflow IDs, actual first failure,
expectation/oracle, tried workarounds and disposition. If no new entry evidence
is present, record deferred with reason and revisit trigger, then continue.
Do not run an unchanged expensive campaign merely to restate an accepted result.

If admitted, write a regression that fails before the fix, make the smallest
coherent repair, verify success, known-bad detection, timeout/cancellation and
cleanup as applicable. Terminal/lifecycle changes require real PTYs and actual
native Linux/macOS/Windows results for claimed hosts; use standard hosted
runners under session authorization. Preserve first failures and race evidence.
Schema changes require an explicit opt-in version/migration decision, matching
validation/examples/docs and old-reader behavior. Never weaken baselines,
assertions or safety limits to pass. Only a necessary new candidate enters the
separate exact-byte release cycle.

Finish with dated evidence and roadmap status. No outreach, marketing,
deployment, hosted services, paid runners, automatic retries or new language
for the runner.
