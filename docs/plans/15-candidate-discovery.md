# 15 — Candidate discovery and campaign preparation

Status: research plan and historical leads. **No new project is admitted or counted as tested here.** The controlling protocol is [08](08-real-project-validation.md).

## Seed leads already represented in repository evidence

These URLs come from the existing [corpus manifest](../../corpus/manifest.json). They identify candidates for re-admission, not current-version or new-product compatibility. Inspect original records before reusing a fixture.

| Candidate | Potential useful task to investigate | Main admission concern |
| --- | --- | --- |
| [Charm Gum](https://github.com/charmbracelet/gum) | Select/confirm/input outcome | Count one project, not each Gum command |
| [Lazygit](https://github.com/jesseduffield/lazygit) | Stage/commit local fixture changes | Verify actual Git state, not status text alone |
| [fzf](https://github.com/junegunn/fzf) | Select the expected item | Distinguish interactive flow from a filter-only command |
| [Posting](https://github.com/darrenburns/posting) | Compose request to a local test endpoint | Control service and query-related terminal behavior |
| [litecli](https://github.com/dbcli/litecli) | Query/update a synthetic SQLite database | Verify exact database state |
| [mitmproxy/mitmconsole](https://github.com/mitmproxy/mitmproxy) | Inspect a locally generated request flow | Disposable network fixture; no real traffic or credentials |
| [bottom](https://github.com/ClementTsang/bottom) | Navigate/configure a monitor | Dynamic metrics cannot become arbitrary snapshot masks |
| [GitUI](https://github.com/extrawurst/gitui) | Navigate/change a disposable Git repository | Native input/state oracle; prior holdout status is historical |
| [television](https://github.com/alexpasmantier/television) | Search/select a local candidate | Stable data and emitted selection |
| [npkill](https://github.com/voidcosmos/npkill) | Select/remove synthetic directories | Strict owned-path deletion safety |
| [create-vite](https://github.com/vitejs/vite) | Choose options and create a fixture project | Count Vite once; avoid live dependency drift |
| [ipm-cli](https://github.com/inkdropapp/ipm-cli) | Local interactive command | Verify useful offline workflow and actual runtime prerequisites |
| [micro](https://github.com/zyedidia/micro) | Edit/save/reopen a synthetic file | Unicode/resize/terminal-query scope |
| [tig](https://github.com/jonas/tig) | Inspect/navigate fixture Git history | Existing WSL evidence is not native Linux/macOS proof |
| [taskwarrior-tui](https://github.com/kdheepak/taskwarrior-tui) | Change synthetic task state | Control external task tool/database/version |

Do not assume these 15 all qualify for the new three-workflow, recorder, mutation, PR and paid-review requirements. Their eventual count is determined by fresh evidence.

## Find the remaining candidates

Use primary project repositories and release docs. Search separately for interactive scaffolding/configuration, fuzzy selection/navigation, Git/developer workflows, terminal editors/file managers, local data clients, and task/monitoring utilities. Search across Go, Rust, Python, JavaScript/TypeScript, C/C++ and other runtimes rather than fill the corpus with one ecosystem.

For each lead, first confirm an actual interactive task in documentation/source, independent upstream ownership, license, maintainable pin, synthetic fixture strategy and plausible target mutation. Popularity/stars are neither admission nor compatibility evidence. Avoid lists padded with framework demos or apps whose only task is printing help.

Produce a 130–150-row screening registry during V0/V1, including at least 20 reserved late candidates plus replacements. It is intentionally not prefilled with 100 unverified names in this plan. Assign canonical IDs and the 08 category allocation before implementation invests in the full set.

## Screening disposition

`lead → screened → admitted for attempt → authored → controlled defect caught → complete integration → qualified`.

Other terminal states: duplicate, unsuitable, dependency blocked, unsupported terminal behavior, unsafe fixture, resource exceeded, abandoned with reason. Only qualified rows count toward 100. Record the date/pin because project capabilities can change.

Before running unfamiliar source, review the intended build and runtime behavior, use isolated disposable execution appropriate to the risk, and enforce bounds. Testing a public repository is not permission to modify or contact it. Synthetic PR tests belong in explicitly authorized owner-controlled repositories, without implication of upstream endorsement.
