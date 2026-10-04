# Repository website

The Playtestr website is a static Hugo site published at <https://wyrcan-io.github.io/playtestr/>. It has dedicated documentation, download, examples, release, support, and project-trial pages. It uses no application backend, analytics, remote fonts, external search service, or runtime GitHub API request.

## Design contract

The design keeps Playtestr's white and cool gray surfaces, navy ink, blue links, fine rules, and dark terminal colors. Pages use solid surfaces, fine borders, readable type, and product evidence as the main visual material. Do not introduce frosted glass, backdrop blur, decorative gradients, neon glow, floating ornaments, or generic marketing-card grids.

The interactive terminal is a browser presentation of finite, reviewed repository fixture states. It does not execute arbitrary commands or claim to be a live PTY. The provenance record is published with its data at `site/static/demos/README.txt`.

## Source layout

- `site/hugo.toml` pins site behavior and the public `/playtestr/` base path.
- `site/layouts/` contains the shared page shell and page-type templates.
- `site/assets/` contains the shared CSS and small JavaScript enhancements.
- `site/content/` defines public routes. Reference wrappers point to a canonical repository document through their `source` front-matter field.
- `site/data/release.toml` and `site/data/prerelease.toml` separately hold reviewed stable and prerelease archive identities.
- `site/static/` contains the favicon, social preview, and bounded demonstration data.
- `docs/` remains the canonical source for technical prose shared with GitHub and release archives.
- `scripts/check-site.mjs` checks required routes, local links, fragments, metadata, search terms, demo evidence, fixed colors, prohibited effects, and asset budgets.

Only pages represented under `site/content/` are published. Internal plans, operator trial notes, and outreach drafts are not added to website navigation automatically.

## Pinned build

The website uses Hugo `v0.164.0`. CI downloads the official Linux amd64 archive and verifies SHA-256 `d9c8b17285ea4ec004d9f814273ea910f2051ce02c284993fd1f91ba455ae50d` before extraction.

On Windows, place the official verified `hugo.exe` at `.tools/hugo-0.164.0/hugo.exe`, then run:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\site.ps1 build
```

Preview locally:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\site.ps1 serve
```

On Unix with the same Hugo version on `PATH`:

```sh
sh scripts/site.sh build
sh scripts/site.sh serve
```

The build writes only to ignored `public/`. Build mode copies the four canonical v1/v2 schemas to `public/schema/` and runs the Node-based validation. Serve mode uses Hugo's development server and renders drafts without changing repository content.

Install the pinned test tools with `npm ci --prefix scripts/website --ignore-scripts`, then run `npx playwright install chromium firefox webkit` from `scripts/website`. Build the preview under `artifacts/website-redesign-preview`, including public schemas, then run `npm test --prefix scripts/website`. Set `WEB_ROOT=public` to test the normal build or `SITE_URL=https://wyrcan-io.github.io/playtestr/` to test production. The harness owns and closes its local server and browser sessions.

The tests visit every route, check six viewport widths from 320 to 1440, run axe WCAG 2.2 AA rules on representative templates, exercise search failure paths, keyboard menus, reduced motion, no-script access, code copying, release identities and genuine 404s. Screenshots and traces stay in ignored `artifacts/`. `npm run performance --prefix scripts/website` performs three mobile Lighthouse lab runs each on the homepage and CI guide. These are lab measurements, not field INP or human accessibility certification.

## Adding or changing documentation

1. Edit the canonical Markdown file under `docs/`.
2. If it is a new public page, add a small route wrapper under `site/content/` with a title, description, and `source` path.
3. Add the route to documentation navigation only when it is part of the stable user journey.
4. Add any repository-relative link mapping needed by the rendered website to `site/layouts/_default/_markup/render-link.html`.
5. Build and run `scripts/check-site.mjs` through the site script.
6. Check GitHub-rendered Markdown when the canonical file is also read outside the website.

Do not copy and independently edit reference prose under `site/`. Page-specific introductions and product navigation may live in `site/content/`.

## Updating a stable release

Update `site/data/release.toml` only from a published, verified release record. Check the exact version, all archive and checksum URLs, architectures, hashes, published date, evidence page, and installation guide. Then update the README, release record, support wording, and website together. Published assets are never replaced under an existing version.

## GitHub repository presentation

Keep the repository settings aligned with the reviewed site when an owner applies them:

- Description: `End-to-end testing for interactive CLIs and TUIs.`
- Website: `https://wyrcan-io.github.io/playtestr/`
- Topics: `cli`, `tui`, `testing`, `terminal`, `e2e-testing`, `go`
- Social preview: `site/static/images/social-preview.png`

These are prepared settings, not evidence that the external repository settings have been changed. Verify them directly after an authorized update.

## Demonstration capture

Use only the trusted repository demo and sanitized specs. Record the source revision, runner label, native host, exact command, ordered screen states, final output, exit status, expected baseline, actual screen, and diff. Verify the passing and deliberately failing commands manually. Update `site/static/demos/README.txt` with provenance.

The demonstration JSON is website data, not report v1 and not a runner replay format. Keep it bounded. UI explanations and line highlights must be distinguishable from runner output. When authentic intermediate screen evidence is unavailable, show the verified final state rather than inventing a frame.

## Deployment workflow

`.github/workflows/pages.yml` builds and validates website changes on pull requests without deploying. Pushes to `main` build and run browser checks without deploying. Dispatch the Website workflow on the reviewed revision with `publish: true` to build, validate, upload and deploy its Pages artifact. The workflow continues to publish the canonical versioned JSON schemas at `/playtestr/schema/`.

A configured or green build is not evidence that the public site works. After deployment, check direct entry to nested routes, downloads and checksums, schemas, search, the terminal controls, social-preview assets, mobile layout, keyboard navigation, and the 404 page at the configured Pages address.

## Release recovery

If a website deployment is broken, identify the last commit whose deployed site was verified. Re-run its Website workflow or prepare a narrow forward fix, then repeat the live checks. Do not rewrite a release tag or replace release assets to repair documentation.

## Validation record

Record website verification in a dated file under `docs/validation/`. Include the source commit, Hugo version, preview or deployed URL, browser/viewport combinations, automated link and metadata result, keyboard and screen-reader observations, transfer sizes, performance setup/result, demonstration provenance, native onboarding results, and unresolved limitations. Lab performance results are not real-user metrics.
