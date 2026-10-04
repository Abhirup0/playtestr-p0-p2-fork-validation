# Website redesign validation - 4 October 2026

Publication and production acceptance are complete. The implementation follows the [reviewed website prompt](../plans/website-redesign-execution-prompt.md). The machine-readable record is [website-redesign-2026-10-04.json](website-redesign-2026-10-04.json).

The original design uses white/cool gray surfaces, navy type, blue links, fine dividers, system fonts and actual captured terminal evidence. Homepage, downloads, documentation, releases, examples, support and 404 share the same restrained components. Stable v0.1.0 and verified prerelease v0.4.0-rc.3 have separate download identities. Current installation, migration and CI paths are explicit; trial recruitment remains held.

## Acceptance

- Static validation passed for 39 HTML pages: internal links and anchors, all public schemas, exact route canonicals, social metadata, sitemap, release archive identities and content budgets.
- All 27 local browser tests passed in Chromium, Firefox and WebKit. Responsive templates were checked at 320, 375, 390, 768, 1024 and 1440 CSS pixels.
- Axe reported no WCAG 2.2 AA rule violations on seven representative templates in all three engines. Keyboard menus, no-JavaScript navigation/TOC, reduced motion, copy feedback, search results and unavailable-index recovery were exercised.
- Windows onboarding used the actual SHA-256-verified published rc.3 archive and the Markdown commands, then the linked greeting recipe: pass 0, deliberate failure 1, recovery 0. The same install/pass/failure/recovery checks passed on native Linux amd64, macOS arm64 and Windows amd64 in [Terminal tests 37194251994](https://github.com/Wyrcan-io/playtestr/actions/runs/37194251994).
- Lighthouse 13.5.0 used simulated mobile throttling with the same local gzip server for three homepage and three CI-guide runs before and after. Median performance remained 100; current accessibility and SEO scored 100. Homepage median LCP was about 1.22 seconds, CI guide about 0.91 seconds, and current CLS was zero in all six runs. Full individual metrics are retained in JSON. These are lab results, not field metrics.

Initial failures were retained: unfocusable terminal scroll regions, code-copy focus movement and a no-script test using a page with too few headings for a TOC. Cross-engine checks additionally found an unfocusable rendered screen. Performance caught a 0.136 menu layout shift, fixed by setting progressive-enhancement state before the first paint. Executing installation commands caught the nested archive directory missing from binary paths. Native CI also exposed a test-harness shell mismatch: starting Windows PowerShell from PowerShell 7 inherited an incompatible module path. The harness now uses the available PowerShell host. Final keyboard review found that the skip link scrolled without transferring focus; the main target now accepts focus, the link declares its tab stop for WebKit, and a regression test covers both home and docs at desktop and mobile widths. None of these findings was suppressed to obtain a pass.

## Evidence and limits

Before/after desktop and mobile screenshots are in ignored `artifacts/website-screenshots-before/` and `artifacts/website-screenshots/`. Browser results, traces and initial failed measurements stay in bounded ignored artifacts; CI uploads the browser evidence separately. The existing demo retains its source provenance rather than fabricating live terminal execution. No core runner, release asset or tag was changed; no outreach or campaign was performed.

No human screen-reader, physical phone, field INP, search ranking, independent adoption or universal terminal compatibility claim is made. The actual host-root `/robots.txt` returned 404 during production verification; no host-root policy file was available. The project-path robots file is informational and cannot set the root-host crawl policy. No other repository was modified.

## Publication

The reviewed site commit is `d01793685eee6082ba9e0d7fecf1316811619ab3`.

- [Website CI 37194684874](https://github.com/Wyrcan-io/playtestr/actions/runs/37194684874): 27 passes, zero skipped, failed or flaky cases.
- [Terminal tests 37194684872](https://github.com/Wyrcan-io/playtestr/actions/runs/37194684872): all three native jobs passed, including public-binary onboarding.
- [Native gap checks 37194684867](https://github.com/Wyrcan-io/playtestr/actions/runs/37194684867): all three native jobs passed.
- [Pages deployment 37194969977](https://github.com/Wyrcan-io/playtestr/actions/runs/37194969977): build and deploy succeeded for the exact reviewed SHA; its additional 27 browser checks passed.
- [Public website](https://wyrcan-io.github.io/playtestr/): 54 HTTP checks passed for intended routes and assets, genuine missing-route 404 and observed root-robots 404. All 27 browser acceptance cases then passed against production across Chromium, Firefox and WebKit.

The final lab build used the deployed source: all six performance, accessibility and SEO scores were 100, all six CLS measurements were zero. Median homepage LCP was 1.22 seconds and CI guide LCP 0.91 seconds. Homepage total transfer was 14,420 bytes; CI guide was 11,965 bytes with the test server's gzip. Production transport can differ. These numbers describe the stated lab setup, not field performance.

This evidence closure is a subsequent documentation-only commit. It changes no rendered site content; the public deployment identity remains the reviewed SHA above. Unrelated user changes to AGENTS.md and roadmap planning files were preserved. Screenshot SHA-256 identities and full measurement results are included in the JSON record; bulk evidence remains in ignored artifacts and the linked CI uploads.
