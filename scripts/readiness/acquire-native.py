"""Acquire pinned public runner bytes with separately timed phases."""
import argparse
import hashlib
import json
from pathlib import Path
import tarfile
import time
import urllib.request

p=argparse.ArgumentParser();p.add_argument('--target',required=True);p.add_argument('--sha256',required=True);a=p.parse_args()
if a.target not in ('linux_amd64','darwin_arm64'):raise SystemExit('invalid native target')
out=Path('artifacts/readiness-native/runner');out.mkdir(parents=True,exist_ok=True)
archive=out/'candidate.tar.gz'
url=f'https://github.com/Wyrcan-io/playtestr/releases/download/v0.4.0-rc.1/playtestr_0.4.0-rc.1_{a.target}.tar.gz'
started=time.monotonic()
with urllib.request.urlopen(url,timeout=60) as response,archive.open('wb') as target:
    count=0
    while chunk:=response.read(65536):
        count+=len(chunk)
        if count>50*1024*1024:raise RuntimeError('archive byte bound exceeded')
        target.write(chunk)
acquisition=(time.monotonic()-started)*1000
started=time.monotonic();observed=hashlib.sha256(archive.read_bytes()).hexdigest();assert observed==a.sha256
verification=(time.monotonic()-started)*1000
started=time.monotonic()
with tarfile.open(archive) as bundle:
    for member in bundle.getmembers():
        path=(out/member.name).resolve()
        if not path.is_relative_to(out.resolve()) or not (member.isfile() or member.isdir()):raise RuntimeError('invalid archive member')
    bundle.extractall(out,filter='data')
extraction=(time.monotonic()-started)*1000
(out/'archive-sha256.txt').write_text(observed+'\n')
(out/'acquisition.json').write_text(json.dumps(dict(target=a.target,url=url,archive_sha256=observed,archive_bytes=count,acquisition_ms=acquisition,verification_ms=verification,extraction_ms=extraction),indent=2)+'\n')
