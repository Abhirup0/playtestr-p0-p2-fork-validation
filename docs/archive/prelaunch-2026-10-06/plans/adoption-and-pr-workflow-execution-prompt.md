> ARCHIVED on 6 October 2026. Historical context only; do not execute this plan. The [current roadmap](../../../../roadmap.md) supersedes its scheduling, gates, and scope.

# Playtestr: adoption preparation and PR workflow execution prompt

Prepared 5 October 2026. This is a reusable execution prompt, not a record of completed work. Paste the prompt below into a coding-agent session with this repository available, or ask the agent to execute this file.

## Prompt begins

You are working in the Playtestr repository. Execute the following finite project through implementation, local verification and a concrete review packet. Do not stop after proposing a plan or generating a collection of placeholders.

### Objective and owner preferences

Help Playtestr become a respected, useful open-source project with a small number of real users. Reputation, technical credibility and limited maintainer time matter more than revenue. The next experiment is independent adoption, not another broad feature campaign.

Produce a usable PR testing workflow, one reproducible launch demonstration, one technically substantive article, a compact trial kit, tailored outreach drafts, and a practical four-week operating plan. Reuse existing implementation and evidence wherever possible.

AI can research, implement, execute tests, reproduce examples, draft material and organize evidence. It cannot supply independent human preference, participant consent, voluntary repeat use, endorsements or willingness to pay. Keep those outcomes explicitly unobserved until actual evidence arrives. Agent role-play or another agent reviewing the work is not independent adoption.

### Authorization and scope

Invoking this prompt authorizes the local preparation and implementation described here, including local website content changes for preview, ordinary necessary validation and read-only public research. It does not authorize external publication or communication.

- Read and follow AGENTS.md, applicable nested instructions and existing session authorization.
- Preserve existing uncommitted changes. Start with git status and identify overlapping files before editing. Do not discard, reset or absorb unrelated work.
- Do not push, publish a release, deploy the site, open or modify a PR/issue/discussion, send invitations/replies, or enable sponsorship/payment accounts without the relevant explicit authorization. Local git commits also require an instruction to commit for this task.
- Prepare exact reviewable changes and exact message drafts before requesting a final external action. Do not ask permission for routine local work already authorized here. Finish unaffected work while an external step is pending.
- A research shortlist is not permission to contact its members. Approval of one invitation is not approval for other recipients or later follow-ups.
- Standard GitHub-hosted native validation is the repository's preferred remote validation path. Prepare necessary workflow changes. Use existing authorized dispatch paths if available; a new push still needs explicit push authorization. If blocked, report the exact unverified hosts and required action; do not ask the user to obtain hardware or SSH access.
- No paid services, ads, runners, purchases, hosted infrastructure, billing, automatic scheduled messages or new accounts.
- No fake hiring posts, fake users, purchased engagement, invented endorsements, undisclosed affiliation, mass messaging or manufactured urgency. Use the maintainer's actual identity and relationship to the project.
- Do not implement a hosted GitHub App, arbitrary-code execution service, autonomous test generator, AI reviewer, dashboard or cloud history.
- Do not rewrite the runner, expand terminal compatibility, change public formats or promote a prerelease to stable as part of this task. Reduce concrete defects found during execution; repair only a narrow blocker within this task's acceptance boundary, with regression coverage. Surface larger work separately.

### 1. Inspect the current state and choose a narrow slice

Read the current versions of these documents, following relevant links rather than reading every historical file indiscriminately:

- AGENTS.md, README.md, roadmap.md, docs/sprints.md and docs/language-decision.md.
- docs/plans/README.md and the latest dated weekly review.
- docs/plans/release/07-maintainer-adoption.md and 08-commercial-discovery.md.
- docs/trials/cohort.md, existing trial templates and the private-kit guide.
- docs/ci-installation.md, docs/ci-failure-handoff.md, docs/failure-reports.md and the current report contracts.
- docs/demo-gallery.md, release/stories, existing demo assets, recipe pages and announcement drafts.
- Current release, qualification, compatibility and website validation records.
- Existing competitive research and the later E1/E2 measurements that supersede older performance conclusions.

Inspect the relevant code, test infrastructure, setup Action and workflows. Use the repository's existing website and tooling conventions.

Record a short baseline: current stable and prerelease versions, recommended version for this trial, source/published-byte distinction, existing assets worth reusing, current independent adoption evidence, and worktree constraints. Verify versions from available authoritative sources; do not assume the versions in this prompt remain latest.

Historical starting context: stable v0.1.0 and verified prerelease v0.4.0-rc.3 existed at preparation time; the repo documented extensive internal validation but no established independent adoption. Five earlier invitations were recorded. Do not reset that history or assume those people have still not replied without checking an authorized source.

State the user-visible behavior for this implementation slice:

> A maintainer adds a documented workflow, runs committed terminal tests on a PR, and gets an accurate failing check plus a readable summary and downloadable failure evidence.

Finish this behavior before optional presentation work expands. Keep progress updates concise. Avoid another extensive planning framework.

### 2. Build the minimum PR integration

Reuse the setup-only Action and the existing runner. Keep installation and execution separate. Prefer a small report-to-Markdown helper and a complete adopter workflow over a new service or a new composite Action unless existing structure makes the latter clearly simpler.

Required behavior:

1. A copyable workflow triggers on pull requests and appropriate pushes, installs an exact release through a pinned setup Action, builds/prepares a concrete target, and runs committed specs.
2. Target preparation is explicit. Do not publish an apparently runnable example that references a nonexistent executable or undeclared prerequisites.
3. The test job uses minimal permissions, a bounded job duration and the established runner budgets. Prefer a named hosted Linux image for the initial documented example; keep other-host claims limited to executed paths.
4. A genuine runner failure remains a failed check. Summary creation or evidence upload must not turn it green.
5. Generate an Actions job summary from the existing versioned machine report, naming outcomes, failed specs, available failure categories and where to find evidence. GitHub summaries are workflow summaries, not PR comments.
6. Preserve JSON, screens/diffs and the existing offline HTML report where available. Upload on test failure as well as success where appropriate, with explicit retention.
7. Handle a missing/malformed/unsupported report, installation failure, cancellation, renderer failure and missing artifacts honestly. Never infer all tests passed from an absent report or zero parsed results.
8. Keep report parsing bounded. Treat report strings, paths and terminal output as untrusted data. Escape Markdown/HTML and control characters appropriately; do not interpolate report fields into shell commands, evaluate them, or emit workflow commands from them.
9. Respect the existing evidence-root/path boundaries and privacy policy. Prefer counts, categories and artifact links in summaries; do not automatically post raw screens, typed input or command/environment values. Targets can print secrets even if the machine report excludes them.
10. Fork PRs must not require secrets or write tokens for test execution. Do not execute PR-head code in a privileged pull_request_target workflow. If a comment publisher is later needed, record it as a separate design with validated run/commit provenance, least privilege and untrusted-artifact handling; do not implement it now.
11. Keep baseline changes deliberate. Never automatically accept snapshots or push commits to a contributor branch.

Check current official GitHub documentation for workflow permissions, summaries, artifacts and fork behavior. Pin external actions according to repository policy and verify revisions rather than inventing hashes. Keep the core in Go; use existing scripting infrastructure for glue only where it is justified. Do not add a runtime or production dependency solely to format a summary.

Validation must include a real passing target, an intended failing target or snapshot, unchanged recovery, missing/malformed report handling, and relevant limits/escaping tests. Verify both output content and exit-code propagation. Local runs can validate the helper and command chain; only actual Actions execution validates Actions behavior. If remote execution is unavailable under current authorization, label that boundary and prepare the exact next run.

Update the CI guide with a complete example, prerequisites, artifact retrieval instructions, expected pass/failure behavior, release pin and uninstall/removal instructions. Avoid changing the setup-only Action's contract. Give the operator a straightforward way to remove the workflow and specs.

### 3. Produce one authentic demonstration

Select the strongest existing release story or recipe. Prefer an interaction that makes the regression obvious without understanding Playtestr internals. Reuse the current demo system and recording tooling; do not build a recorder.

The demonstration must show:

- The exact runner version and small test definition.
- A successful keyboard-driven interaction.
- A clearly labeled injected defect or controlled regression.
- The actual failing result and readable evidence.
- Recovery with the same test after removing the defect.

Capture actual output from the executed commands. Keep reproduction scripts, relevant pins and hashes with the evidence. Do not make screenshots or output using an image generator. If a UI animation replays a recorded transcript, label it as a replay rather than live execution.

Aim for a 30–60 second presentation using existing tooling. Provide a text transcript, a static useful fallback and captions or accessible labels. If video tooling is unavailable, complete a reproducible text/static demonstration and explain the single missing export step; do not spend a day building media infrastructure.

Clearly identify seeded defects as seeded. Do not imply an upstream project endorsed Playtestr or that a synthetic mutation was a real upstream bug. Keep old-version evidence labeled instead of attributing it to a newer release.

### 4. Write one substantial engineering article and improve the entry path

Choose one actual investigation, such as macOS final-output preservation or selected two-column character rendering. Review source diffs, regression tests and dated evidence before drafting.

Write approximately 800–1,200 words, shorter if the story warrants it, covering:

1. The observable failure and why a developer would care.
2. A minimal reproduction or precise recorded reproduction.
3. The mechanism supported by code and evidence.
4. The fix and the regression test.
5. Remaining limitations and what was not proved.
6. One modest invitation to try the relevant workflow.

Use a descriptive technical title. Separate measured facts from inference. Use real excerpts with links, not fabricated quotations, benchmark charts or debugging anecdotes. Do not write in the maintainer's first person about feelings or work they did not personally report. A draft is not published content.

Prepare a small local website/README improvement only where needed to connect: what the tool does → one demo → exact-version first test → CI → feedback route. Make stable versus prerelease requirements explicit. Reuse the recently completed website design; do not redesign it again. Avoid expanding the README into a release-history or validation ledger. Verify local links and commands.

### 5. Refresh a compact, fair comparison

Read current project-owned documentation for Microsoft tui-test, Atago and Termlens. Include existing scripts/framework tests as an alternative when relevant. Date the comparison and cite exact sources. Do not use AI-generated summaries or search snippets as final technical evidence.

Produce a concise comparison focused on who should choose which tool: authoring style, installation needs, rendered assertions, evidence, integration fit and documented limitations. Include reasons to choose alternatives.

Distinguish current documented features from version-pinned executed benchmarks. Preserve the original measurement versions and conditions; never extrapolate old measurements to current releases. Do not rerun the full competitive benchmark campaign. Record unknowns honestly. Do not claim that real PTYs, snapshots, cross-language execution or readable diagnostics are unique to Playtestr.

Use a positioning hypothesis such as: “Catch keyboard-driven CLI regressions with a standalone runner, small JSON tests and readable failure evidence.” Claims of lower effort require independent observations and must remain hypotheses until obtained.

### 6. Prepare recruitment materials without sending them

Reuse the existing adoption protocol and templates. Prepare:

- A one-page participant guide: suitable targets, prerequisites, exact install, one useful flow, pass/defect/recovery, evidence retrieval, optional CI integration, known limits and removal.
- Five brief feedback questions about the last relevant regression, current method, first obstacle, usefulness of diagnosis and reason to keep or reject the test.
- A factual observation template distinguishing unaided work, agent/maintainer assistance, actual elapsed time, failures, abandonment, CI completion and later voluntary reuse.
- A respectful follow-up draft, usable only with separate authorization and appropriate consent.

Do not burden a first participant with the entire internal qualification protocol. Start with one valuable interaction and record what actually happens. Keep existing formal A1 thresholds intact; a smaller exploratory experiment does not silently mark A1 complete.

Research at most five prospective projects using public project information. Select active interactive CLIs/TUIs with a specific plausible testable flow. For each record the project URL, evidence for fit, likely existing alternative, proposed interaction, a suitable public contact route and that route's contribution/promotion rules. Use “unknown” where necessary. No personal-email harvesting or personal profiling.

Check existing outreach history before suggesting another invitation to the same project. Use the private ledger only if available and appropriate; do not expose it in public artifacts. If inaccessible, flag deduplication as pending. Keep candidate identities and exact proposed messages in an ignored local review packet unless already authorized for public inclusion. First verify the chosen private directory is ignored; never rely on its name alone.

Draft no more than five individualized messages, roughly 60–100 words each. State affiliation, mention the concrete flow, link the relevant demo, and ask whether trying it would be useful. Avoid praise templates, performance promises, pressure, requests for stars, or implying consent.

Also prepare one concise LinkedIn post and one community post suited to a researched channel's current rules. Share a technical finding and an actual demonstration. Do not post to hiring channels or bypass self-promotion rules. These are optional alternative channels, not instructions for a simultaneous blast.

For each proposed external action, prepare a review row containing destination, exact content, links/assets, purpose and required authorization. Nothing gets sent merely because the draft exists.

### 7. Prepare a small sustainability decision

Write a one-page recommendation, using the existing commercial plan rather than starting a business plan:

- Keep the standalone runner open-source and useful without an account.
- Optional sponsorship is a future low-obligation route, not forecast revenue. Verify platform requirements if recommending a concrete service. Do not activate accounts or invent eligibility.
- Fixed-scope onboarding or compatibility work may be considered if someone has an actual need and the maintainer wants the commitment. Prepare an example scope with deliverables, exclusions and a support-hour cap, not a fabricated customer or approved price.
- A hosted PR service remains deferred. Explain why a free workflow already supplies much of the immediate value and what recurring paid problem would justify operating a service.
- Retain the existing independent-repeat-use and paid-pilot gates. Interest, praise and hypothetical willingness to pay are different from payment.

Do not add billing, accounts, SLAs, a pricing page, sponsorship tiers with ongoing obligations, or payment links as part of this task.

### 8. Design the four-week experiment

Prepare a schedule capped at roughly three maintainer hours per week. This is a proposed allocation, not a claim about time already spent. Start the recruitment clock only after the owner actually authorizes and begins outreach.

- Week 1: approve/select the prepared demonstration and article; choose a small number of invitations.
- Week 2: observe willing first attempts; record help and failures; fix at most one recurring adoption blocker.
- Week 3: support a useful retained test or participant-owned CI integration; publish a factual learning only with necessary permissions.
- Week 4: review completed attempts, voluntary return, maintenance burden and the reasons people declined.

Use two independent useful first tests and one voluntary later reuse as provisional small-experiment signals, not formal A1 completion or proof of product-market fit. Record installation, attempt, useful result, retention and CI separately. Stars and impressions are secondary observations, not adoption.

Define three possible decisions: continue modest maintenance and one focused fix; revise positioning/onboarding based on a named obstacle; or stop active promotion and maintain the project at a low cadence. No response does not prove the tool is useless, but it does not justify endless new features either.

Do not create scheduled tasks or automatic follow-ups. Do not wait weeks pretending to complete the independent-use portion in this execution session.

### 9. Validate and deliver

Run checks appropriate to actual changes. Format Go changes and run relevant tests/vet. For lifecycle/concurrency changes run the required race checks; do not claim success if their compiler prerequisite is unavailable. Execute the affected manual example. Use existing site build/link/browser checks for site changes; do not rerun the entire release qualification campaign for article edits.

Maintain a small dated completion record with exact commands/results, release/source identities, generated artifacts, failed attempts, current unknowns and external steps not performed. Label historical checks as historical. Do not overwrite past evidence, adoption counts or authorization status.

Expected deliverables, reusing existing files where sensible:

1. Minimal tested report-summary implementation and runnable adopter workflow/example.
2. Updated CI/first-use documentation for the selected version.
3. One reproduced demo with actual evidence and accessible fallback.
4. One technically sourced article draft and only necessary local presentation edits.
5. A short dated comparison with fair choice guidance.
6. One compact trial kit and an ignored private recipient/message review packet.
7. A short sustainability recommendation and four-week operating plan.
8. One completion record and one concise review index linking the above.

Prefer a few coherent documents over a separate file for every bullet. Do not add another sprawling roadmap. Leave roadmap adoption/commercial gates open unless actual evidence closes them. Clearly mark all unpublished material.

Before finishing, inspect the final diff and worktree status. Confirm private drafts are ignored, examples use available commands, version claims are consistent, failure propagation is correct, and no external actions occurred accidentally.

The final response should lead with what now works, link the concrete artifacts, summarize checks and limitations, and identify the smallest remaining owner decisions. If publication, push or contact is pending, request only a specific action on a fully prepared result and explain that AGENTS.md requires specific authorization. Link the applicable instructions. Do not ask “shall I continue?” while authorized local deliverables remain unfinished.

Success for this execution is a useful, tested local PR integration and an honest, ready-to-review adoption package. Real adoption and paid demand remain outcomes to observe afterward.

## Prompt ends
