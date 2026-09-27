"""Package bounded synthetic private evidence only after the complete E5 gate."""
import hashlib,json,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
packet=json.loads((ROOT/'docs/validation/e5-observations-2026-09-27.json').read_text())
assert packet['status'].startswith('complete'), 'Do not package a pending checkpoint as complete'
destination=ROOT/'.trial-private/e5-readiness-kit'; destination.mkdir(exist_ok=False)
directories=['e3-native-36305941244','e3-local','e4 walkthroughs','e4-walkthroughs-r2','e4 diagnosis','e4-setup','e4-setup-r2',
 'e4-native-36329364021','e4-native-36307315138','e4-public-36307330579','macos-output-36307693286','macos-output-36329115446',
 'macos-output-36329407653','macos-output-286279a','e5-candidate-36329978517','e5-native-source-36329981123',
 'e5-preflight-36330142857','e5-stories-36330145384','e5-native-bytes-36330943126','e5-qualification-36330814511',
 'e5-corpus','e5-holdouts','e5-holdouts-exact','e5-holdouts-frozen','e5-compatibility','e5-source-local',
 'e5-windows-tree','e5-windows-plain','e5-windows-supported-tree','e5-windows-supported-plain','e5-supported-serial',
 'e4-frozen-walkthroughs','e5-ci-index','e5-native-real-36333011585']
allowed={'.json','.jsonl','.log','.txt','.md','.html','.control','.oracle','.sha256'}
files=set()
for name in directories:
    folder=ROOT/'artifacts'/name
    for path in folder.rglob('*'):
        if path.is_file() and not path.is_symlink() and (path.suffix.lower() in allowed or
              (name=='e5-candidate-36329978517' and (path.name.endswith('.zip') or path.name.endswith('.tar.gz')))):
            files.add(path)
for path in (ROOT/'docs/validation').glob('e[345]*2026-09-27.*'): files.add(path)
for name in ['release/e5-candidate-config.json','release/e5-candidate-manifest.json','release/checksums-v0.4.0-rc.2.txt',
 'release/e5-release-notes.md','docs/trials/e5-private-kit.md','docs/migration-v0.4.0-rc.2.md','docs/e4-operator-walkthroughs.md',
 'artifacts/e5-site-status.json','artifacts/e5-site-status-r2.json','artifacts/e5-site-check.log','artifacts/e5-site-check-r2.log',
 'artifacts/e5-qualification-forecast.json','artifacts/e5-native-gates-first-failure.log']:
    files.add(ROOT/name)
for name in ['artifacts/e5-site-final.log','artifacts/e5-site-final-exit.txt','artifacts/e5-post-push.json']:
    path=ROOT/name
    if path.exists(): files.add(path)
assert sum(path.stat().st_size for path in files)<256*1024*1024,'Private evidence exceeds admitted bound'
entries=[dict(path=str(path.relative_to(ROOT)).replace('\\','/'),bytes=path.stat().st_size,sha256=hashlib.sha256(path.read_bytes()).hexdigest()) for path in sorted(files)]
manifest=dict(schema_version=1,status=packet['status'],source_commit=packet['source_commit'],version=packet['version'],
    contents=entries,privacy='Synthetic fixtures and explicit tool identities only; no browser profile, environment dump, user execution prompt, target runtime installation or development executable.',
    publication='Unauthorized; private package is not a release asset')
manifest_bytes=(json.dumps(manifest,indent=2)+'\n').encode()
archive=destination/'playtestr-e5-private-evidence.zip'
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for entry in entries:
        info=zipfile.ZipInfo(entry['path'],date_time=(2026,9,27,0,0,0)); info.compress_type=zipfile.ZIP_DEFLATED
        z.writestr(info,(ROOT/entry['path']).read_bytes())
    info=zipfile.ZipInfo('private-evidence-manifest.json',date_time=(2026,9,27,0,0,0)); info.compress_type=zipfile.ZIP_DEFLATED
    z.writestr(info,manifest_bytes)
identity=dict(schema_version=1,path=str(archive.relative_to(ROOT)),bytes=archive.stat().st_size,
              sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),files=len(entries),uncompressed_bytes=sum(x['bytes'] for x in entries),publication='private only')
(ROOT/'artifacts/e5-private-kit-identity.json').write_text(json.dumps(identity,indent=2)+'\n')
print(json.dumps(identity,indent=2))
