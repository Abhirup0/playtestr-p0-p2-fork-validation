# Playtestr website: researched redesign and publication prompt

Prepared 4 October 2026. Planning artifact only; no website implementation or deployment was performed while preparing this file.

## How to use this in a new chat

Send: **Read `docs/plans/website-redesign-execution-prompt.md` and execute it completely, including its website-scoped commits, pushes, GitHub Pages deployment and live verification. No outreach or marketing campaigns.**

Reading this file for review is not an instruction to execute it. When explicitly instructed to execute it, follow the complete scope below without stopping after a design proposal or local build. The execution instruction authorizes website-scoped commits, necessary source pushes and deployment to the existing GitHub Pages site. It does not authorize a new runner release, paid services, changes to DNS, outreach, or issue/PR/discussion mutations.

## 1. Outcome and quality bar

Update Playtestr's existing website into a complete, polished developer-product website. It should have the clarity and execution quality associated with an established professional software company: deliberate design, useful documentation, accurate information, fast pages and reliable interactions.

The user's priorities are minimal, professional, responsive, technically credible, strong SEO and GEO, proper pages and links, and no broken essential journeys. They explicitly reject generic AI-looking design, extravagance, bloat and lag. "Multimillion-dollar company quality" describes execution quality; it does not license fabricated company size, funding, customers, revenue or enterprise offerings.

Take design liberties within that brief. Make routine decisions independently. Finish implementation, checks, commit/push, deployment and verification of the actual public site. Preserve failed attempts and report concrete external blockers honestly. Never bypass an approval rejection.

## 2. Research findings that should shape the work

These findings are starting evidence, not a substitute for checking the repository and live site when execution begins.

### Reference: Graphify

[Graphify](https://graphify.com/) was inspected through its public page and 1440-pixel-wide browser captures while scrolling through the homepage. Beyond the textured hero, the observed sections include paired explanation/visuals, a modular feature layout, a comparison table, a concise trust row, a split FAQ and a grouped footer.

**Design judgment for Playtestr:** selectively adapt structure and clarity. The user specifically asked us to inspect below the fold and does not want everything brought over. Do not reject useful modular layouts just because generic templates overuse them; choose components for their content and keep them compact. Do not import the oversized hero, dense commercial navigation, proof counters or unsupported social proof. A reference is not a template or endorsement of its claims.

Research screenshots, if still available: `artifacts/website-prompt-research-2026-10-04/graphify-desktop.png` and `graphify-section-{0,3,4,5,6,8}.png` in the same directory. These capture the desktop opening and lower sections, not a complete mobile or accessibility audit. The browser was closed after research. Reinspect only as needed.

Translate the research into these Playtestr-specific options, selecting only the ones that improve the final page:

| Pattern to consider | Original adaptation for Playtestr |
| --- | --- |
| Explanation beside a visual | Pair a short spec with the resulting rendered screen and failure diff. If controls change the example, all states must remain readable and keyboard accessible. Prefer a static pairing when interaction adds little. |
| Compact modular feature previews | Use a few real artifacts: a snapshot diff, a suite summary and an offline report. Unequal panel sizes are acceptable when content warrants them. Avoid a wall of identical icon cards or abstract decoration. |
| Comparison table | An optional small "where it fits" table can clarify terminal end-to-end tests versus complementary testing methods. State limits and retain unit tests' role. Named competitor claims require current primary evidence and fair scope; omit unsupported rankings. |
| Concise trust information | Present verified license, standalone operation, readable evidence and trusted-target boundaries with relevant links. Do not copy certifications or assume a target application never uses the network. |
| Split FAQ | A short introduction beside approximately five genuine questions: need for Go, supported hosts, stable/prerelease choice, real PTY versus sandbox, and snapshot review. Native disclosure elements are sufficient. |
| Grouped footer | Use a compact Product / Documentation / Project arrangement, limited to real destinations. No oversized decorative wordmark, empty corporate sections or provider-branded "ask AI" buttons. |

These options are a design palette, not six mandatory extra homepage sections. Fold them into the existing story, combine overlaps and omit anything that lengthens the page without helping a visitor. The user's reference should inform more than the hero while the resulting identity remains distinctly Playtestr.

### SEO and GEO

Google's [AI features guidance](https://developers.google.com/search/docs/appearance/ai-features) says ordinary SEO fundamentals apply to its AI search experiences; special AI files or special structured data are not required. Eligibility does not guarantee indexing or appearance. Therefore, this task prioritizes accessible substantive content, internal discovery, precise explanations and attributable claims, without promising AI citations. Also consult the [official generative-AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide).

There is an important hosting detail: [robots.txt belongs at the host root](https://developers.google.com/crawling/docs/robots-txt/create-robots-txt). A generated `/playtestr/robots.txt` is not the authoritative crawl policy for `wyrcan-io.github.io`. Inspect the real host-root policy and describe any ownership limitation; do not edit another repository or claim project-subdirectory robots rules control the host. Public content can still be crawlable without a project-controlled root robots file.

### Accessibility and performance

WCAG 2.2 [target-size minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum) is 24 by 24 CSS pixels with defined exceptions. Prefer approximately 44-pixel main controls for comfortable use, while treating that larger size as a design choice rather than misquoting the AA minimum.

[Core Web Vitals](https://web.dev/articles/vitals) use LCP, INP and CLS, with field assessment at the 75th percentile. Lab runs are useful for regressions but do not establish field performance. Keep lab measurements, simulated interactions, Lighthouse scores and real-user data distinct.

### Existing implementation and known gaps

The current site is Hugo with small CSS/JavaScript assets. It already has canonical/social metadata, fingerprinted CSS, static content, a documentation sidebar, search, code-copy controls and a prepared terminal demonstration. Improve these rather than replacing everything to appear busy.

Known 4 October audit findings:

| Area | Observation | Required response |
| --- | --- | --- |
| Live downloads/releases | Still listed rc.1; live rc.3 release route returned 404 | Correct content, deploy, then check actual public responses |
| Repository release pages | Rc.3 page and current-prerelease summary already exist | Preserve correct material and complete publication |
| `site/content/trials.md` | Recommends rc.1 and its older action pin | Align status and versions without launching recruitment |
| `docs/ci-installation.md` | Current-status paragraph still describes rc.2 verification | Reconcile with rc.3 evidence; preserve dated historical results |
| `site/layouts/home.html` | Hardcoded stable v0.1.0 CTA and v1-only fact strip | Make channel/version boundaries intentional and data-driven |
| `site/data/release.toml` | Existing stable download data | Add a coherent stable/prerelease source of truth without changing stable's identity |
| `site/assets/site.js` | Basic mobile toggle; table of contents generated by JS | Review keyboard/focus behavior; render substantive structure in HTML where practical |
| `scripts/browser-check.mjs` | Existing Chromium/CDP-based browser checks | Preserve useful coverage; bound waits and add missing behaviors/browser coverage |
| `.github/workflows/pages.yml` | Deployment occurs only on dispatch with `publish: true` | A push/build alone does not update the public site |

The local site build passed 36 HTML-page checks during the audit. That did not prove live freshness, comprehensive accessibility, visual polish or every external link. Local audit files may exist under `artifacts/live-site-audit-2026-10-04/` and `artifacts/site-audit-2026-10-04/`; recheck rather than assume availability.

## 3. Repository, scope and baseline

Repository: `C:\Users\abhir\OneDrive\Documents\playtestr`.

Production site: `https://wyrcan-io.github.io/playtestr/`.

Read `AGENTS.md`, README, `roadmap.md`, platform/terminal compatibility docs, current release and migration records, the website workflow, and the files referenced above. Inspect `site/content/`, `site/layouts/`, `site/assets/`, `site/data/`, `site/hugo.toml` and the existing check scripts.

At preparation time HEAD was `63c9968e42385ea600882f401ae0518baa6aaaa5`. Original user changes remained in `AGENTS.md`, `docs/plans/README.md` and two untracked execution prompts. Reinspect and preserve all unrelated changes, including any added since then. Do not automatically stage everything or overwrite planning files to get a clean tree.

Before edits, produce a compact route/content inventory, baseline screenshots of representative pages, measured page weights and an issue list with priorities. Record the last deployed commit and current local/remote relationship. Distinguish observed bugs from design proposals.

Website implementation, documentation updates, synthetic examples, static assets and relevant validation tooling are in scope. Runner/terminal code, spec schemas, published binaries, release tags, pricing, accounts, commercial infrastructure and new product features are not scope fillers.

Use existing Hugo and GitHub Pages. Do not migrate to React/Next.js, a CMS, a site generator service or a new host. Avoid runtime frameworks and production dependencies unless a specific necessary behavior cannot be implemented simply. Test-only browser/accessibility tools may be added with pinned versions and bounded execution.

## 4. Design specification

Choose one coherent visual direction and apply it across the entire site. Recommended starting direction: a quiet technical editorial layout, light neutral canvas, dark ink, one restrained accent, fine dividers, a confident sans-serif and readable monospace for actual code. You may refine colors and proportions after inspecting real content.

Use a consistent spacing scale, type scale, reading width, content grid, border treatment and control sizing. Prefer a maximum general content width around 1120-1200 pixels and comfortable prose lines around 60-75 characters. These are starting constraints, not reasons to force content into awkward shapes. Body text should remain readable on phones; avoid tiny muted labels everywhere.

Build a small shared set of components: header/navigation, buttons/links, release labels, code blocks, terminal evidence, callouts, tables, documentation navigation, page contents, search results, breadcrumbs where helpful, and footer. Define tokens centrally. Avoid a giant CSS patchwork or a new component for every section.

The homepage should show a concise product explanation and real product proof early. Avoid a mostly empty first viewport. Documentation should feel like part of the same product, with less decoration and stronger reading ergonomics.

Do not use gradient blobs, glow, glass panels, decorative particles, scrolling marquees, gratuitous bento grids, generic feature-card walls, stock AI illustrations, fake dashboards, animated counters, parallax, scroll hijacking, custom cursors or decorative WebGL. Avoid oversized pill shapes and large-radius containers everywhere. No animation library for simple transitions. Respect reduced motion; no essential meaning depends on animation.

Do not fabricate logos, testimonials, adoption statistics or compliance badges. Do not introduce an unnecessary theme switcher. Use the existing logo/wordmark thoughtfully; any refinement must remain legible at small sizes and as a favicon.

Review the homepage, a long documentation page and the download page together at desktop and mobile sizes early. Correct the shared design before expanding it to every template. Visual inspection is mandatory; a successful build cannot judge design.

## 5. Pages and user journeys

Retain useful existing URLs and content. Merge duplication where useful; do not create thin pages merely to increase page count. Keep navigation concise: documentation, examples, releases, source repository and a clearly labelled download action are sufficient unless another item earns its place.

### Homepage

Explain what Playtestr tests, who uses it, how it drives a terminal, what it asserts and what a failure produces. Show one real short test and corresponding evidence with a clear route to reproduce it. Keep useful content within roughly five to seven purposeful sections, not an arbitrary full-page marketing template.

Use one primary action and one secondary action. Make stable versus prerelease explicit wherever choosing a channel matters. Current features must not appear to ship in older stable binaries without version labels.

The browser demo must be labelled as a prepared demonstration if it does not execute a real PTY. Do not invent a shell transcript to make the product look successful. Use sanitized, reproducible product examples with prerequisites available beside them.

### Downloads and releases

Present stable and current prerelease separately. Provide exact platform/architecture names, direct archives, checksums, version strings, installation guidance, release notes, migration/rollback and evidence links. Do not hide download links behind scripts or automatically redirect based on guessed architecture.

Centralize current release/channel data, including runner version and independently pinned setup-action SHA. Keep historical release documents fixed to their own versions; never replace all version strings globally. Ensure relevant rc.2 history remains discoverable, even if linked to its existing repository record rather than adding another thin website page.

### Documentation

Organize by reader task: get started, author tests, run in CI, diagnose failures, then references. Cover installation, meaningful first pass/failure/recovery, keys/text/readiness/assertions, reviewed snapshots, suites, workspaces, reports, CI installation, local handoff, examples, troubleshooting, schemas, compatibility and migration.

Retain a single source for content rendered from repository docs. Audit Markdown-to-site link mapping so internal documentation links open useful website pages where available; intentional repository references must be clearly labelled. Do not fork technical documentation into contradictory copies.

Give version-dependent features visible minimum-version guidance. Windows PowerShell and Unix shell instructions must be correct for their named host; tabbed examples must remain accessible and useful without JavaScript. Explain target prerequisites. Do not require Go for a binary-only first test when Go is unnecessary.

Use build-rendered page contents, stable heading anchors, accurate sidebar active states and appropriate previous/next navigation. Keep technical tables and code horizontally scrollable inside their own containers. Search should load its index on demand, be keyboard usable, handle special characters safely and show understandable no-results/loading/failure states.

### Support and supporting pages

Keep security reporting, support boundaries, license and source links easy to find. Do not invent a sales team, enterprise package, SLA or legal policy. State actual data practices if a privacy explanation is useful. Avoid adding analytics, advertising, trackers, cookie banners or external embeds by default.

Retain any existing trial route with accurate status, or provide a clear migration path if its purpose changes. No new recruiting forms, invitations, marketing copy campaigns or external contact. Correct old version advice without representing independent adoption as established.

Provide a useful 404 page, clear current/historical release organization and complete footer destinations. A link is preferable to a decorative disabled button pretending a feature exists.

## 6. Product truth and version rules

At preparation time stable was `v0.1.0`; the newer verified prerelease was `v0.4.0-rc.3`. Rc.3's setup-action pin was `ae97c62022966cde9699b26169b4dc6ef0a12439`. Release targets were Windows amd64, Linux amd64 and macOS arm64. Reverify these using authoritative records and actual releases before publication.

Read `docs/releases/v0.4.0-rc.3.md`, `docs/migration-v0.4.0-rc.3.md`, `docs/validation/wide-character-release-2026-10-01.md` and `docs/terminal-compatibility.md`. Rc.3 includes the selected CJK/fullwidth two-column repair. Remaining combining-cluster, emoji/ZWJ, ambiguous-width and terminal-query boundaries must match the contract.

Distinguish v1/v2 format support, stable/prerelease, source/released bytes, exact tested tasks/broad compatibility, and operator/independent results. Playtestr runs explicitly trusted targets with user permissions; a subprocess or PTY is not sandbox isolation.

Counts and benchmarks need scope and evidence. Do not call repeated attempts distinct scenarios, corpus projects customers, or task-specific speed results universal superiority. Do not claim full accessibility, zero flakiness, broad Unicode support or independent adoption from automated tests.

Use concrete copy without inflated adjectives. Reconcile active descriptions while retaining historical failures and dated evidence. Published tags and binary assets remain immutable.

## 7. SEO, GEO and metadata

Inventory metadata before adding it: canonicals, descriptions, social tags and fingerprinted assets already exist. Fix inconsistent values and omissions rather than duplicating tags.

Implement unique useful titles/descriptions, sensible headings, descriptive links, stable URLs, page-specific social descriptions, valid image dimensions, favicons and canonical production URLs. Improve the homepage title beyond the bare brand name while keeping it concise. Verify all generated URLs respect `/playtestr/` and never point at localhost or an unrelated root path.

Maintain a valid sitemap with intended canonical public pages. Exclude error/search-state/duplicate generated pages where appropriate. Use truthful substantive modification dates; do not stamp every page with build time. Preserve old URLs, or implement the best supported alias/redirect behavior and label its real HTTP behavior. Do not claim Hugo static aliases provide server-side 301s without checking.

Inspect the actual host-root robots policy. Do not treat a project-path robots file as authoritative or modify the organization's root-site repository without separate scope. Use supported page-level indexing controls where appropriate; never claim robots rules protect private data. Do not publish private artifacts in the first place.

Use structured data only for supported visible facts, such as website/software/source-code identity and breadcrumbs. Validate JSON-LD syntax and references. Do not fabricate ratings, reviews, prices or corporate details to satisfy a rich-result template. Schema validity does not guarantee a search enhancement.

For GEO, provide a consistent concise product definition, useful task explanations, exact version/platform information, visible limitations and source-backed answers. Keep substantive content in crawlable HTML. A short FAQ belongs only where it answers actual reader questions; do not create a keyword-stuffed FAQ farm.

An `llms.txt` directory is optional and low priority. If added, keep it concise and generated or checked against canonical docs. No ranking or citation promises, special hidden AI text, doorway pages, fake locality pages or gratuitous SEO blog. The research above is guidance for Google; do not generalize unsupported requirements to every answer engine.

Search Console verification/submission is not a prerequisite for finishing the site if account access is absent. Prepare the sitemap and record account-dependent follow-up without inventing traffic/indexing evidence or creating new accounts.

## 8. Responsive behavior and accessibility

Test 320, 375, 390, 768, 1024 and 1440 CSS-pixel widths plus intermediate resizing, landscape and zoom. Require no unintended whole-page horizontal scrolling, clipped navigation, overlapping headings, unreadable code or inaccessible sidebar controls.

Core content, navigation, download links and documentation must work with JavaScript disabled. Search/demo/copy controls may progressively enhance usable HTML. In particular, a mobile menu must not hide every navigation destination when its toggle script fails.

Use semantic landmarks, skip navigation, logical heading order, appropriate names/labels, visible focus, readable contrast and meaningful image alternatives. Aim at WCAG 2.2 AA within the tested scope; do not claim certification. Support text enlargement and reflow, keyboard-only operation, reduced motion and forced-colors where applicable.

For ordinary disclosure navigation, do not add a focus trap unnecessarily. For a genuinely modal mobile drawer, manage focus and background interaction correctly. Support Escape, return focus appropriately, maintain expanded state and keep focused controls visible beneath sticky UI. No hover-only functionality.

Main controls should be comfortably touchable. Copy buttons need accessible feedback and a usable failure path. Diff meaning must not rely on red/green alone. Tables require proper headers. Code copy must copy the intended command without stray prompts or decorative line numbers.

Run automated accessibility checks and manual keyboard checks on each template. Preserve the distinction from an actual human screen-reader session; missing independent human evidence stays open without pretending the website was never technically checked.

## 9. Performance budgets and measurement

Keep Hugo/static HTML, modest CSS and small progressive JavaScript. No SPA, heavy animation library, unnecessary third-party scripts or backend. Prefer system fonts; if a self-hosted font materially improves the result, limit families/weights, document licensing and measure its cost.

These are project targets, not claims copied from a universal standard:

| Metric | Target |
| --- | --- |
| Initial compressed JS on ordinary pages | At most 35 KiB |
| Shared compressed CSS | At most 40 KiB |
| Initial homepage transferred resources | At most about 350 KiB, including initially loaded images/fonts |
| Ordinary documentation page | Lighter than the homepage; no eager full search-index download |
| Mobile lab LCP / CLS | At most 2.5 seconds / 0.1 under a documented repeatable profile |
| Mobile Lighthouse performance | Aim for median 95+ across three comparable cold-load runs |

Record baseline and final results on the same profile, including browser/tool versions, throttling, page, transfer sizes and first-load behavior. Lab INP cannot be inferred from a navigation-only Lighthouse run. If real-user data exists, report it separately; otherwise field values are unknown. Scores alone do not replace interaction testing.

Optimize and document any justified budget exception; do not quietly lower targets. Prioritize actual slow resources or long tasks over chasing a noisy score. Bound test timeouts and evidence retention.

Give images explicit dimensions and appropriate formats, prioritize actual above-fold content and lazy-load suitable lower-page media. Avoid lazy-loading the LCP element. Fingerprint assets and keep cache behavior compatible with Pages. Optional demos should pause when hidden and should not occupy a continuous render loop merely for decoration.

## 10. Validation and definition of done

Extend existing checks for actual missed risks. Do not delete valuable checks just because redesigned markup makes them fail; update assertions to test the intended user behavior. A static assertion of a version string alone does not prove the download link, channel or page is correct.

Create a route/link manifest from actual public content, checking every internal destination, fragment, asset, schema, sitemap and canonical. Check critical external release/checksum/source links with bounded concurrency and retries. Classify blocked/transient external responses honestly rather than calling all of them broken or successful.

Test these complete journeys on desktop and mobile:

1. Homepage to a clearly chosen channel, correct archive/checksum instructions and first meaningful pass/failure/recovery.
2. Example to its documented prerequisites and reproducible spec.
3. CI instructions to independently pinned action and runner version.
4. Failure report to diagnosis and recovery guidance.
5. Release notes to migration and exact compatibility limitations.
6. Search to useful results, plus no-results and failed-index behavior.
7. Keyboard/mobile menu, heading navigation, code copy and no-JavaScript access.

Run Chromium, Firefox and WebKit coverage using available local tools or ordinary GitHub-hosted runners. A WebKit engine run is not an actual iPhone/Safari device claim. Record exact coverage; avoid claiming unsupported physical-device validation.

Inspect responsive screenshots visually on the homepage, downloads, documentation home, long reference, release notes, search and 404. Check console errors, failed assets, redirects, focus behavior and overflow. Use bounded browser sessions with explicit shutdown; never kill a user's ordinary browser.

Validate changed executable examples with their named released binary and prerequisites. Do not rerun the unchanged 3,000-attempt runner qualification campaign for a website redesign. Run source tests only where relevant executable/helper behavior changes, and retain the repository's required CI checks for pushed changes.

Known build/check entry points, to adapt after inspecting the environment:

```powershell
.tools/hugo-0.164.0/hugo.exe --source . --config site/hugo.toml --destination artifacts/website-redesign-preview --minify
New-Item -ItemType Directory -Force artifacts/website-redesign-preview/schema | Out-Null
Copy-Item schema/*.json artifacts/website-redesign-preview/schema
node scripts/check-site.mjs artifacts/website-redesign-preview
git diff --check
```

Use the repository-pinned Hugo toolchain at execution time. Serve previews under the real project base path. `scripts/browser-check.mjs` currently expects an existing CDP endpoint; inspect its invocation and lifecycle instead of assuming it launches a browser. On Windows start background helpers hidden, write text explicitly as UTF-8, and keep all cleanup within checked task-owned paths.

## 11. Execution sequence, commits and deployment

Proceed through these checkpoints without repeatedly requesting routine design approval:

1. **Audit:** confirm repo/remote/live state, content and route inventory, baseline measurements, issues and current release identities.
2. **Design:** settle the shared system using homepage, documentation and downloads; inspect desktop/mobile together.
3. **Implementation:** apply all templates, navigation, accurate copy, release data, docs, metadata and progressive interactions.
4. **Acceptance:** fix failures from links, actual user journeys, browser/accessibility checks and performance measurement; retain evidence.
5. **Publication:** commit only scoped work, push under the explicit execution authorization, await actual required CI and deploy the reviewed commit using the existing Pages workflow.
6. **Production acceptance:** verify the real public site and close the evidence record.

No force pushes or rewriting published assets. Handle an advanced remote by reviewing differences; preserve other work. Website builds must not trigger a new runner release. The current workflow deploys through `workflow_dispatch` with `publish: true`; inspect the latest workflow and dispatch against the intended committed revision. Correlate its checked-out SHA, build, deploy job and public content. Do not mistake an ordinary green push build for publication.

After deployment, fetch all intended routes with bounded requests and verify the current release page returns 200, stale channel text is gone, essential links work, and generated assets/canonicals/sitemap reference production correctly. Verify genuinely missing URLs return appropriate error behavior rather than a misleading success page. Repeat representative browser/mobile/keyboard checks against production. Cache refresh waits must be bounded; record what was actually observed.

If a deployment regression occurs, restore a known-good site through the existing non-destructive deployment process when possible, preserve the failed attempt and repair before declaring completion. A service outage or denied permission is an explicit blocker, not permission to bypass controls or label publication complete.

## 12. Deliverables and completion report

Deliver the implemented site, reusable design tokens/components, coherent current release data, corrected documentation, useful regression checks, and dated Markdown plus machine-readable validation evidence. Keep bulky screenshots and browser traces in bounded ignored artifacts; link their identities from a compact record. Never publish private evidence archives or browser profiles.

Include before/after representative screenshots, page-weight/performance measurements, route/metadata results, tested browser/device scope, actual CI/deployment links and the deployed commit. Preserve historical product evidence rather than rewriting it for presentation.

Acceptance requires a polished coherent design across all templates, working essential journeys, accurate current-release content, no known critical internal-link/interaction failures, documented accessibility and performance results, and actual verified publication. Search ranking, external adoption and human screen-reader evidence cannot be fabricated to satisfy this checklist.

Finish with the public URL, commit, deployment outcome, key changes and any concrete remaining limitation. Do not report "everything is perfect" from a passing build or stop at a mockup. No outreach, marketing campaigns, new paid services or invented product claims.
