# Website redesign validation - 4 October 2026

Publication is pending. The implementation follows the [reviewed website prompt](../plans/website-redesign-execution-prompt.md). The machine-readable record is [website-redesign-2026-10-04.json](website-redesign-2026-10-04.json).

The original design uses white/cool gray surfaces, navy type, blue links, fine dividers, system fonts and actual captured terminal evidence. Homepage, downloads, documentation, releases, examples, support and 404 share the same restrained components. Stable v0.1.0 and verified prerelease v0.4.0-rc.3 have separate download identities. Current installation, migration and CI paths are explicit; trial recruitment remains held.

## Acceptance

- Static validation passed for 39 HTML pages: internal links and anchors, all public schemas, exact route canonicals, social metadata, sitemap, release archive identities and content budgets.
- All 27 local browser tests passed in Chromium, Firefox and WebKit. Responsive templates were checked at 320, 375, 390, 768, 1024 and 1440 CSS pixels.
- Axe reported no WCAG 2.2 AA rule violations on seven representative templates in all three engines. Keyboard menus, no-JavaScript navigation/TOC, reduced motion, copy feedback, search results and unavailable-index recovery were exercised.
- Windows onboarding used the actual SHA-256-verified published rc.3 archive and the Markdown commands, then the linked greeting recipe: pass 0, deliberate failure 1, recovery 0. The same install/pass/failure/recovery checks passed on native Linux amd64, macOS arm64 and Windows amd64 in [Terminal tests 37194251994](https://github.com/Wyrcan-io/playtestr/actions/runs/37194251994).
- Lighthouse 13.5.0 used simulated mobile throttling with the same local gzip server for three homepage and three CI-guide runs before and after. Median performance remained 100; current accessibility and SEO scored 100. Homepage median LCP was about 1.21 seconds, CI guide about 0.96 seconds, and current CLS was zero in all six runs. Full individual metrics are retained in JSON. These are lab results, not field metrics.

Initial failures were retained: unfocusable terminal scroll regions, code-copy focus movement and a no-script test using a page with too few headings for a TOC. Cross-engine checks additionally found an unfocusable rendered screen. Performance caught a 0.136 menu layout shift, fixed by setting progressive-enhancement state before the first paint. Executing installation commands caught the nested archive directory missing from binary paths. Native CI also exposed a test-harness shell mismatch: starting Windows PowerShell from PowerShell 7 inherited an incompatible module path. The harness now uses the available PowerShell host. Final keyboard review found that the skip link scrolled without transferring focus; the main target now accepts focus, the link declares its tab stop for WebKit, and a regression test covers both home and docs at desktop and mobile widths. None of these findings was suppressed to obtain a pass.

## Evidence and limits

Before/after desktop and mobile screenshots are in ignored `artifacts/website-screenshots-before/` and `artifacts/website-screenshots/`. Browser results, traces and initial failed measurements stay in bounded ignored artifacts; CI uploads the browser evidence separately. The existing demo retains its source provenance rather than fabricating live terminal execution. No core runner, release asset or tag was changed; no outreach or campaign was performed.

No human screen-reader, physical phone, field INP, search ranking, independent adoption or universal terminal compatibility claim is made. Effective host-root robots behavior will be verified after deployment; a project-path robots file cannot control the root host.

## Publication

Await the scoped commit, successful CI, explicit Pages deployment and production acceptance before marking this record complete.
