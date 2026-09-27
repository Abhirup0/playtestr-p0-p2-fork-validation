"""Prepare a separately attributed suite after the retained unsupported wide-cell failure."""
import hashlib,json,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
old=ROOT/'artifacts/readiness-2026-09-26/serial'; new=ROOT/'artifacts/e5-supported-serial'
new.mkdir(exist_ok=False)
shutil.copytree(old/'fixtures',new/'fixtures')
shutil.copytree(ROOT/'corpus/workflows/micro/supported-unicode-fixture',new/'fixtures/basic-unicode')
basic=json.loads((ROOT/'corpus/workflows/micro/rw2-basic-unicode.control').read_text(encoding='utf-8'))
basic['command'][0]=str(ROOT/'.trial-private/corpus-tools/micro-oracle.exe')
basic['workspace']['fixture']='fixtures/basic-unicode'
pins=[]
for original in sorted(old.glob('size-*-repeat-*.json')):
    spec=json.loads(original.read_text(encoding='utf-8-sig')); replaced='MICRO-08' in spec['name']
    if replaced:
        name=spec['name']; spec=json.loads(json.dumps(basic)); spec['name']=name+'; separately scoped basic-character route'
    path=new/original.name; path.write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
    pins.append(dict(path=str(path.relative_to(ROOT)),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
        original_path=str(original.relative_to(ROOT)),original_sha256=hashlib.sha256(original.read_bytes()).hexdigest(),replaced_unsupported_wide_route=replaced))
(new/'admission.json').write_text(json.dumps(dict(reason='Retained first size-50 instrumented MICRO-08 stale wide-cell failure; basic cafe/lambda route is separately qualified, not a repaired wide rendering claim.',
    original_failed_attempt='artifacts/e5-windows-tree/size-50-sample-1.json',inputs=pins),indent=2)+'\n')
print(len(pins),'inputs; original files unchanged')
