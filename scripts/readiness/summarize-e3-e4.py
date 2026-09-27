"""Keep compact synthetic observations and retained file identities."""
import hashlib
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
packet={}; native=ROOT/'artifacts/e3-native-36305941244'
for name in ['run','artifacts']: packet['e3_'+name]=json.loads((native/(name+'.json')).read_text(encoding='utf-16'))
packet['e3_attempts']=[]
for d in sorted(native.glob('e3-fidelity-*')): packet['e3_attempts']+=json.loads((d/'attempts.json').read_text())
packet['e3_cells']=json.loads((ROOT/'artifacts/e3-local/cells-with-query.json').read_text(encoding='utf-16'))
packet['e4_attempts']=[]
for d in ['e4 walkthroughs','e4-walkthroughs-r2']: packet['e4_attempts']+=json.loads((ROOT/'artifacts'/d/'attempts.json').read_text())
packet['e4_diagnosis']=json.loads((ROOT/'artifacts/e4 diagnosis/attempts.json').read_text())
packet['e4_preparation']=[json.loads((ROOT/'artifacts'/d/'setup.json').read_text()) for d in ['e4-setup','e4-setup-r2']]
packet['retained_files']=[]
for directory in [native]+[ROOT/'artifacts'/d for d in ['e3-local','e4 walkthroughs','e4-walkthroughs-r2','e4 diagnosis','e4-setup','e4-setup-r2']]:
    for p in sorted(directory.rglob('*')):
        if p.is_file() and p.suffix.lower() not in ('.exe','.pyc'):
            packet['retained_files'].append(dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
(ROOT/'docs/validation/e3-e4-observations-2026-09-27.json').write_text(json.dumps(packet,ensure_ascii=True,indent=2)+'\n')
