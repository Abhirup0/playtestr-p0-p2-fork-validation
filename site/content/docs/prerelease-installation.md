---
title: "Install the current prerelease"
description: "Verify and install Playtestr v0.4.0-rc.3 on Windows amd64, Linux amd64 or macOS arm64, then run a meaningful test."
---

This guide installs **v0.4.0-rc.3**. Stable v0.1.0 has a separate [binary-only first-test walkthrough](/playtestr/docs/installation/). Your target application still needs its own runtime. The Playtestr binary does not require Go.

## Download and verify

Choose the exact host archive and its adjacent `.sha256` file on the [downloads page](/playtestr/download/). Save both into the same directory. These examples assume the files have already been downloaded.

### Windows amd64 (PowerShell)

```powershell
$archive = 'playtestr_0.4.0-rc.3_windows_amd64.zip'
$expectedHash = (Get-Content ($archive + '.sha256')).Split(' ')[0]
if ((Get-FileHash $archive -Algorithm SHA256).Hash -ne $expectedHash) { throw 'Checksum mismatch' }
Expand-Archive -LiteralPath $archive -DestinationPath './playtestr rc3' -ErrorAction Stop
& './playtestr rc3/playtestr_0.4.0-rc.3_windows_amd64/playtestr.exe' --version
```

### Linux amd64 (shell)

```sh
sha256sum --check playtestr_0.4.0-rc.3_linux_amd64.tar.gz.sha256
mkdir 'playtestr rc3'
tar -xzf playtestr_0.4.0-rc.3_linux_amd64.tar.gz -C 'playtestr rc3'
'./playtestr rc3/playtestr_0.4.0-rc.3_linux_amd64/playtestr' --version
```

### macOS arm64 (shell)

```sh
shasum -a 256 --check playtestr_0.4.0-rc.3_darwin_arm64.tar.gz.sha256
mkdir 'playtestr rc3'
tar -xzf playtestr_0.4.0-rc.3_darwin_arm64.tar.gz -C 'playtestr rc3'
'./playtestr rc3/playtestr_0.4.0-rc.3_darwin_arm64/playtestr' --version
```

Stop if checksum verification fails. Confirm the executable reports `playtestr v0.4.0-rc.3` before adding its directory to PATH. Extraction examples deliberately use a directory containing a space. Keep downloaded versions in separate directories.

## Prove the test can fail

Follow the [first-test walkthrough](/playtestr/docs/installation/) with your verified rc.3 executable path in place of the stable executable. Its v1 greeting spec remains compatible: run a passing test, make the documented intentional assertion change, confirm a nonzero failure and restore the correct assertion. Do not overwrite a baseline merely to make a run pass.

The [authoring recipes](/playtestr/docs/recipes/) offer useful interactive targets with explicit prerequisites. [Suites](/playtestr/docs/suites/), [offline HTML reports](/playtestr/docs/failure-reports/) and [workspaces](/playtestr/docs/workspaces/) document the newer capabilities separately.

## Use in CI

Pin the setup action and runner version independently using the [GitHub Actions guide](/playtestr/docs/ci-installation/). The action verifies release identity; target setup, test execution and artifact upload remain explicit workflow steps.

## Upgrade, remove and understand limits

Read [migration and rollback](/playtestr/docs/upgrade/) before adopting v2. Remove the version's directory and any PATH entry you added to uninstall; baseline and test files remain your project data. Do not run recursive cleanup against guessed paths.

Rc.3 includes selected two-column CJK/fullwidth behavior, not universal Unicode layout. Combining clusters, emoji/ZWJ, ambiguous-width settings and terminal queries remain limited. Read [terminal compatibility](/playtestr/docs/terminal-compatibility/). Only run explicitly trusted targets: this backend is not a sandbox.
