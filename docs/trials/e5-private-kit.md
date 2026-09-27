# Private E5 trial and release-decision kit

Status: **qualified private v0.4.0-rc.2; technically ready for a scoped trial**.
All 3,000 first attempts passed on the three native hosts. See the
[readiness decision](../validation/e5-qualified-readiness-2026-09-27.md) and
[evidence index](../validation/e3-e5-evidence-index-2026-09-27.md).
This kit does not authorize publication, a deployment, or contact with anyone.

Proposed trial version: `v0.4.0-rc.2`, exact source
`ae97c62022966cde9699b26169b4dc6ef0a12439`, Go 1.26.0, native Linux amd64,
macOS arm64 and Windows amd64. Retain the [manifest](../../release/e5-candidate-manifest.json)
and [checksums](../../release/checksums-v0.4.0-rc.2.txt). The private archives are
the original [native build 36329978517](https://github.com/Wyrcan-io/playtestr/actions/runs/36329978517)
artifacts. A new source build, embedded version or stable relabel needs new
qualification; these bytes must be promoted without rebuilding.

Follow the [four operator recipes](../e4-operator-walkthroughs.md). Install the
exact native archive into a path with spaces, verify the manifest hash and
`playtestr version`, install the separately pinned target/runtime prerequisites,
then run a good spec, its attributed defect and unchanged recovery. Review
baseline text before accepting any update. Export reports using relative
evidence paths. Candidate v1 and opt-in v2 contracts match the existing
[v0.4 migration rules](../migration-v0.4.0-rc.1.md).

Claims proposed for review: deterministic screen/exit and exact-state checks on
the admitted pinned cells, real native PTYs, bounded execution/evidence and
confirmed managed process/workspace cleanup in the observed cases. Exclude
wide/combining cursor layout, terminal-query-dependent flows, universal framework
support, isolation/sandboxing, universal speed or total-effort superiority and
broad accessibility. MICRO-08 has an intermittent Windows wide-cell failure in
addition to the native Unix failures; its 120-cell first pass is diagnostic,
not a reliable support claim. Human screen-reader work is owned by the maintainer.

Historical matched E2 tasks: RW1 speed loss, RW3 tie with Atago and speed win
against Termlens; selected correctness ties, complete human effort unknown.
Those measurements remain attributed to their original binaries/toolchains.
Two meaningful real-task advantages were not demonstrated: differentiation is
unmet. No independent demand, comprehension, retained use or purchase evidence
is inferred from these operator campaigns.

After a separate publication decision, the following is the exact proposed
asset preparation and prerelease command. It has **not** been executed:

```powershell
gh run download 36329978517 --dir 'artifacts/e5 promotion download'
New-Item -ItemType Directory -Path 'artifacts/e5 promotion assets'
Get-ChildItem 'artifacts/e5 promotion download' -Recurse -File | Where-Object { $_.Name -like 'playtestr_*.zip*' -or $_.Name -like 'playtestr_*.tar.gz*' } | Copy-Item -Destination 'artifacts/e5 promotion assets'
Copy-Item release/checksums-v0.4.0-rc.2.txt 'artifacts/e5 promotion assets'
# Verify all archive hashes against the checked-in manifest before publication.
gh release create v0.4.0-rc.2 'artifacts/e5 promotion assets/playtestr_0.4.0-rc.2_linux_amd64.tar.gz' 'artifacts/e5 promotion assets/playtestr_0.4.0-rc.2_linux_amd64.tar.gz.sha256' 'artifacts/e5 promotion assets/playtestr_0.4.0-rc.2_darwin_arm64.tar.gz' 'artifacts/e5 promotion assets/playtestr_0.4.0-rc.2_darwin_arm64.tar.gz.sha256' 'artifacts/e5 promotion assets/playtestr_0.4.0-rc.2_windows_amd64.zip' 'artifacts/e5 promotion assets/playtestr_0.4.0-rc.2_windows_amd64.zip.sha256' 'artifacts/e5 promotion assets/checksums-v0.4.0-rc.2.txt' --target ae97c62022966cde9699b26169b4dc6ef0a12439 --prerelease --title 'Playtestr v0.4.0-rc.2' --notes-file release/e5-release-notes.md
gh workflow run e5-public-verification.yml --ref readiness/e3-e5
```

The last command executes the prepared native public-origin and immutable
setup-action checks; it must succeed on all three hosts, and downloaded hashes
must match the private manifest, before a public candidate recommendation.
The proposed action is `Wyrcan-io/playtestr/setup-playtestr@ae97c62022966cde9699b26169b4dc6ef0a12439`
with `version: v0.4.0-rc.2`. Existing v0.4.0-rc.1 public routes remain old-byte
evidence. No website deployment is part of this proposal.

Outreach proposal for a later decision: invite consenting maintainers to one
scoped target workflow, collect first-use/diagnosis time and participant CI,
then observe voluntary reuse. Request permission for each specific recipient
and message before sending anything. A1's comprehension and retention targets
remain independent-use questions; the operator must not substitute these
engineering walkthroughs for participant results.
