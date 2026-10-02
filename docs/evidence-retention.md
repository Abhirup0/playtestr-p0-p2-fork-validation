# Verify retained release evidence

CI artifacts have finite retention. The 1 October rc.3 release retained a
private ZIP of synthetic reports, ledgers, qualified/public archives and dated
records. Its completion seal is separate so the archive can have a trusted
digest without referring to its own hash. Keep both in approved private
storage; this repository does not upload or publish that archive.

From the repository root, using Python 3.10 or newer:

```powershell
python scripts/readiness/verify-evidence.py .trial-private/playtestr-wide-character-release-evidence-2026-10-01.zip --sha256 8fcdb231a5ce89e65d09e3765e8801ff41f62b4a212f723d673d5f08986abda9
```

Supply the trusted digest from the separate completion seal, rather than
calculating a fresh digest of an untrusted archive and treating it as proof.
The verifier reads without extraction or target execution. It checks the
archive digest, member CRCs, index coverage, sizes and every indexed SHA-256.
It rejects duplicate/unsafe paths, links, encrypted members and malformed
indexes. Bounds are 64 MiB compressed, 1 GiB expanded, 10,000 members and a
4 MiB index. The current tool reads the rc.3 member-index format; a different
packet format needs an explicit tooling change.

Success prints a compact JSON result and exits zero. Invalid, missing,
corrupt or oversized evidence exits nonzero with a generic message that does
not print private member data. The tool proves integrity against the supplied
digest. It does not rerun targets, extend host coverage, prove reported results
or create independent adoption evidence.

Run the failure controls:

```powershell
python -m unittest discover -s scripts/readiness -p test_verify_evidence.py -v
```

See [release evidence](validation/wide-character-release-2026-10-01.md) for
qualified identities and results, and [continuation evidence](validation/roadmap-continuation-2026-10-02.md)
for the initial retained-archive verification and conditional decisions.
