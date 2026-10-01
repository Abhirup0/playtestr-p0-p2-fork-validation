"""Verify an explicitly selected native candidate and extract only admitted members."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tarfile
import zipfile

p = argparse.ArgumentParser()
p.add_argument('--candidate', default='candidate')
p.add_argument('--source', required=True)
p.add_argument('--version', required=True)
p.add_argument('--out', default='frozen candidate')
a = p.parse_args()
assert re.fullmatch(r'[0-9a-f]{40}', a.source)
assert re.fullmatch(r'v\d+\.\d+\.\d+-rc\.\d+', a.version)
root = Path(a.candidate)
records = list(root.rglob('candidate-evidence-*.json'))
assert len(records) == 1, records
r = json.loads(records[0].read_text())
assert r['source_commit'] == a.source and r['version'] == a.version
archive = root / r['archive']
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
assert sha(archive) == r['archive_sha256']
base = archive.name.removesuffix('.tar.gz').removesuffix('.zip')
executable = 'playtestr.exe' if archive.suffix == '.zip' else 'playtestr'
expected = sorted(base + '/' + name for name in ['LICENSE', 'README.md', 'THIRD_PARTY_NOTICES.md', executable])
assert sorted(r['archive_members']) == expected
destination = Path(a.out).resolve()
destination.mkdir(parents=True, exist_ok=False)
if archive.suffix == '.zip':
    with zipfile.ZipFile(archive) as z:
        assert sorted(z.namelist()) == expected
        z.extractall(destination)
else:
    with tarfile.open(archive) as t:
        assert sorted(t.getnames()) == expected
        assert all(m.isfile() for m in t.getmembers())
        t.extractall(destination, filter='data')
binary = destination / base / executable
assert sha(binary) == r['executable_sha256']
assert subprocess.check_output([str(binary), 'version'], text=True).strip() == 'playtestr ' + a.version
installer = json.loads((root / 'artifacts/private-install-identity.json').read_text(encoding='utf-8-sig'))
assert installer['binary_sha256'] == r['executable_sha256']
assert installer['archive_sha256'] == r['archive_sha256']
(destination / 'verified-identity.json').write_text(json.dumps(r, indent=2) + '\n')
if 'GITHUB_ENV' in os.environ:
    with open(os.environ['GITHUB_ENV'], 'a') as env:
        env.write('FROZEN_RUNNER=' + str(binary) + '\n')
        env.write('FROZEN_RUNNER_SHA256=' + r['executable_sha256'] + '\n')
print(json.dumps(dict(source=a.source, version=a.version, executable_sha256=sha(binary), archive_sha256=sha(archive))))
