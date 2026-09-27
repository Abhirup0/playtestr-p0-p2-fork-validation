"""Bounded E3 first-attempt investigation; never executes holdouts."""
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import time
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'artifacts/e3-fidelity'
TOOLS = ROOT / '.trial-private/corpus-tools'
OUT.mkdir(parents=True, exist_ok=False)
TOOLS.mkdir(parents=True, exist_ok=True)
suffix = '.exe' if os.name == 'nt' else ''

def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def run(argv, cwd=ROOT, timeout=600):
    subprocess.run([str(x) for x in argv], cwd=cwd, check=True, timeout=timeout)

for name, repo, commit, binary, package in [
    ('micro', 'zyedidia/micro', '04c577049ca898f097cd6a2dae69af0b4d4493e1', 'micro.exe', './cmd/micro'),
    ('fzf', 'junegunn/fzf', 'a140afeb4d733cad3c96a56bf6db7e26853b6757', 'fzf'+suffix, '.')]:
    source = ROOT / '.trial-private' / ('e3-'+name)
    run(['git', 'init', '-q', source])
    run(['git', 'remote', 'add', 'origin', 'https://github.com/'+repo+'.git'], source)
    run(['git', 'fetch', '--depth', '1', 'origin', commit], source)
    run(['git', 'checkout', '--detach', 'FETCH_HEAD'], source)
    assert subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=source, text=True).strip() == commit
    run(['go', 'build', '-trimpath', '-o', TOOLS/binary, package], source)
run(['go', 'build', '-trimpath', '-o', TOOLS/('micro-oracle'+suffix), '.'], ROOT/'corpus/controls/micro-oracle')
runner = OUT/('playtestr'+suffix)
run(['go', 'build', '-trimpath', '-o', runner, './cmd/playtestr'])
identity = dict(source=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
    runner_sha256=sha(runner), toolchain=subprocess.check_output(['go','version'],text=True).strip(),
    host=platform.platform(), architecture=platform.machine(), flags=['-trimpath'],
    targets={p.name:sha(p) for p in [TOOLS/'micro.exe', TOOLS/('fzf'+suffix), TOOLS/('micro-oracle'+suffix)]})
(OUT/'identities.json').write_text(json.dumps(identity,indent=2)+'\n')
cases = [
    ('micro-wide-original', 'micro/micro-08.json', False),
    ('micro-basic-control', 'micro/rw2-basic-unicode.control', False),
    ('fzf-wide-resize', 'fzf/fzf-08.json', True),
    ('fzf-combining', 'fzf/rw4-combining.control', False),
    ('micro-wide-persistence', 'micro/micro-08.json', True),
]
rows=[]
for name, rel, derived in cases:
    original=ROOT/'corpus/workflows'/rel
    spec=json.loads(original.read_text(encoding='utf-8-sig'))
    for step in spec['steps']:
        if 'text' in step:
            assert step['text'].encode('utf-8').decode('utf-8') == step['text']
    spec['env']={**spec.get('env',{}),'LANG':'C.UTF-8','LC_ALL':'C.UTF-8'}
    if os.name != 'nt':
        spec['command']=[x.replace('reload(type candidates.txt)','reload(cat candidates.txt)') for x in spec['command']]
    if name=='fzf-wide-resize':
        at=next(i for i,s in enumerate(spec['steps']) if 'resize' in s)
        spec['steps'][at:at]=[{'resize':{'width':45,'height':12}},{'wait_for_redraw':True},{'expect':'Find: gamma'},
            {'resize':{'width':60,'height':16}},{'wait_for_redraw':True},{'expect':'Find: gamma'}]
        # Final selected bytes still compare the original reviewed snapshot.
    if name=='micro-wide-persistence':
        # Separate file/input probe: do not credit this as a rendered-wide pass.
        for step in spec['steps']:
            if step.get('expect')=='雪 alpha marker': step['expect']='alpha marker'
    path=original.with_name('e3-'+name+'.control')
    path.write_text(json.dumps(spec,ensure_ascii=True,indent=2)+'\n',encoding='utf-8')
    start=datetime.now(timezone.utc).isoformat(); tick=time.monotonic()
    report=OUT/(name+'.json')
    with (OUT/(name+'.log')).open('wb') as log:
        process=subprocess.run([str(runner),'test','--report',str(report),'--artifacts-dir',str(OUT/name),str(path)],
            cwd=ROOT,stdout=log,stderr=subprocess.STDOUT,timeout=60)
    result=json.loads(report.read_text())['results'][0]
    row=dict(case=name,derived=derived,start_utc=start,end_utc=datetime.now(timezone.utc).isoformat(),
        elapsed_ms=(time.monotonic()-tick)*1000,exit=process.returncode,result=result,
        original_spec_sha256=sha(original),executed_spec_sha256=sha(path),
        input_hex=[s['text'].encode('utf-8').hex() for s in spec['steps'] if 'text' in s],**identity)
    rows.append(row)
    (OUT/'attempts.json').write_text(json.dumps(rows,indent=2)+'\n')
    print(name,process.returncode,result.get('failure',{}),flush=True)
    if len(rows)==2:
        forecast=dict(pilot_cells=2,pilot_ms=sum(r['elapsed_ms'] for r in rows),
            projected_task_ms=sum(r['elapsed_ms'] for r in rows)/2*len(cases),
            raw_evidence_bytes=sum(p.stat().st_size for p in OUT.rglob('*') if p.is_file()),
            runner_hour_cap=6,compressed_byte_cap=1073741824,
            note='Two native jobs, five cells each; target setup measured by Actions separately. No repeats.')
        (OUT/'forecast.json').write_text(json.dumps(forecast,indent=2)+'\n')
