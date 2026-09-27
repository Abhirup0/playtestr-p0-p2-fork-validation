"""Execute frozen operator-designed holdouts once at E5, without retries."""
import argparse
from datetime import datetime,timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time
ROOT=Path(__file__).resolve().parents[2]
p=argparse.ArgumentParser(); p.add_argument('--runner',required=True); p.add_argument('--out',default='artifacts/e5-holdouts')
args=p.parse_args(); runner=Path(args.runner).resolve(); out=ROOT/args.out; out.mkdir(parents=True,exist_ok=False)
assert os.name=='nt','This frozen admission uses native Windows pinned targets'
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
plans=[('HO1-stage','gitui/gui-01.json'),('HO1-unstage','gitui/gui-02.json'),('HO2','television/television-01.json')]
definitions={}
for ident,source in plans:
    original=ROOT/'corpus/workflows'/source; spec=json.loads(original.read_text())
    # Match the frozen negative route: persisted index is the independent
    # positive staging proof. Do not rely on a UI label that implies success.
    if ident=='HO1-stage': spec['steps']=[s for s in spec['steps'] if s.get('expect')!='Unstage']
    path=original.with_name('e5-'+ident+'.control'); path.write_text(json.dumps(spec,indent=2)+'\n')
    definitions[ident]=dict(path=str(path.relative_to(ROOT)),original_sha256=sha(original),spec_sha256=sha(path))
negative=ROOT/'corpus/workflows/gitui/e5-HO1-defect.control'
spec=json.loads((ROOT/definitions['HO1-stage']['path']).read_text()); spec['env']={'PLAYTESTR_GITUI_MUTATION':'1'}
negative.write_text(json.dumps(spec,indent=2)+'\n'); definitions['HO1-defect']=dict(path=str(negative.relative_to(ROOT)),spec_sha256=sha(negative))
definitions['HO2-defect']=dict(path='corpus/workflows/television/television-01-known-bad.control',spec_sha256=sha(ROOT/'corpus/workflows/television/television-01-known-bad.control'))
freeze=dict(source=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),runner_sha256=sha(runner),
    targets=[dict(path=str(t.relative_to(ROOT)),sha256=sha(t)) for t in
        [ROOT/'.trial-private/r3c/windows/rs-02-gitui/bin/gitui.exe']+
        [ROOT/'.trial-private/corpus-tools'/x for x in ['gitui-mutated.exe','gitui-oracle.exe','tv.exe','tv-mutated.exe']]],
    definitions=definitions,pilot='none; first execution is good attempt 1 of 5',independence='operator designed; historical corpus presence limits independence')
(out/'freeze.json').write_text(json.dumps(freeze,indent=2)+'\n')
rows=[]
def attempt(ident,definition,expected,category=None):
    report=out/(ident+'.json'); tick=time.monotonic(); start=datetime.now(timezone.utc).isoformat()
    with (out/(ident+'.log')).open('wb') as log:
        process=subprocess.run([str(runner),'test','--report',str(report),'--artifacts-dir',str(out/(ident+'-evidence')),definitions[definition]['path']],
            cwd=ROOT,stdout=log,stderr=subprocess.STDOUT,timeout=60)
    result=json.loads(report.read_text())['results'][0]
    failure=result.get('failure',{}).get('category'); accepted=process.returncode==expected and result['cleanup']['confirmed_exited'] is True
    if category: accepted=accepted and failure==category
    if result.get('workspace'): accepted=accepted and result['workspace']['cleaned'] is True
    rows.append(dict(attempt_id=ident,definition=definition,start_utc=start,end_utc=datetime.now(timezone.utc).isoformat(),
        whole_command_ms=(time.monotonic()-tick)*1000,exit=process.returncode,expected_exit=expected,expected_category=category,
        result=result,accepted=accepted,runner_sha256=freeze['runner_sha256']))
    (out/'attempts.json').write_text(json.dumps(rows,indent=2)+'\n'); print(ident,process.returncode,failure,accepted,flush=True)
    return accepted
for journey,steps in [('HO1',['HO1-stage','HO1-unstage']),('HO2',['HO2'])]:
    for number in range(1,6):
        for definition in steps: attempt(f'{journey}-good-{number}-{definition}',definition,0)
    attempt(journey+'-defect',journey+'-defect',1,'unexpected_exit' if journey=='HO1' else 'snapshot_mismatch')
    for definition in steps: attempt(journey+'-recovery-'+definition,definition,0)
(out/'summary.json').write_text(json.dumps(dict(attempts=len(rows),accepted=sum(r['accepted'] for r in rows),
    holdout_good_attempts={'HO1':5,'HO2':5},pilot_separate=False),indent=2)+'\n')
raise SystemExit(0 if all(r['accepted'] for r in rows) else 1)
