"""Verify retained native manifests; execute only the native Windows extraction."""
import hashlib
import json
from pathlib import Path
import subprocess
import tarfile
import zipfile
ROOT=Path(__file__).resolve().parents[2]
source=ROOT/'artifacts/e5-candidate-36329978517'
out=ROOT/'artifacts/e5 frozen candidate extracted'
out.mkdir(parents=True,exist_ok=False)
records=[]
for folder in sorted(source.glob('playtestr-*')):
    manifest=json.loads(next(folder.rglob('candidate-evidence-*.json')).read_text(encoding='utf-8'))
    archive=folder/manifest['archive']
    assert hashlib.sha256(archive.read_bytes()).hexdigest()==manifest['archive_sha256']
    assert manifest['source_commit']=='ae97c62022966cde9699b26169b4dc6ef0a12439'
    assert manifest['version']=='v0.4.0-rc.2'
    if archive.suffix=='.zip':
        with zipfile.ZipFile(archive) as z:
            assert sorted(z.namelist())==sorted(manifest['archive_members'])
            # Members were admitted by the exact four-file manifest, including
            # the original native archive's single relative package prefix.
            z.extractall(out)
        binary=next(out.rglob('playtestr.exe'))
        assert hashlib.sha256(binary.read_bytes()).hexdigest()==manifest['executable_sha256']
        assert subprocess.check_output([str(binary),'version'],text=True).strip()==manifest['version_output']
    else:
        with tarfile.open(archive) as t:
            assert sorted(t.getnames())==sorted(manifest['archive_members'])
            binary=next(m for m in t.getmembers() if m.name.endswith('/playtestr'))
            assert hashlib.sha256(t.extractfile(binary).read()).hexdigest()==manifest['executable_sha256']
    installer=json.loads((folder/'artifacts/private-install-identity.json').read_text(encoding='utf-8-sig'))
    assert installer['binary_sha256']==manifest['executable_sha256']
    assert installer['archive_sha256']==manifest['archive_sha256']
    records.append(dict(**manifest,local_retained_archive_verified=True,source_installer=installer))
(ROOT/'release/e5-candidate-manifest.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
(ROOT/'release/checksums-v0.4.0-rc.2.txt').write_text(''.join(r['archive_sha256']+'  '+Path(r['archive']).name+'\n' for r in records),encoding='utf-8')
print(json.dumps([dict(host=r['host'],binary=r['executable_sha256'],archive=r['archive_sha256']) for r in records],indent=2))
