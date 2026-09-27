"""Qualify the admitted 120 cells and 15 attributed controls on frozen bytes."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parents[2]
p = argparse.ArgumentParser()
p.add_argument('--runner', required=True)
p.add_argument('--sha256', required=True)
p.add_argument('--out', default='artifacts/e5-corpus')
args = p.parse_args()
runner = Path(args.runner).resolve()
out = ROOT / args.out
out.mkdir(parents=True, exist_ok=False)
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
assert sha(runner) == args.sha256
records = [json.loads(f.read_text(encoding='utf-8')) for f in sorted((ROOT/'corpus/results').glob('*-windows-amd64.json'))]
assert len(records) == 15
plans = []
for record in records:
    for flow in record['workflows']:
        plans.append(dict(id=flow['id'], spec=flow['spec'], expected_exit=0, category=None, phase='good'))
assert len(plans) == 120
for record in records:
    control = record['control']
    plans.append(dict(id=record['project']['id']+'-control', spec=control['known_bad_spec'], expected_exit=1,
                      category=control['observed_category'], phase='control'))
    plans.append(dict(id=record['project']['id']+'-recovery', spec=control['recovery_spec'], expected_exit=0, category=None, phase='recovery'))
inputs = [dict(path=str(f.relative_to(ROOT)), sha256=sha(f)) for f in sorted((ROOT/'corpus/workflows').rglob('*')) if f.is_file()]
targets = [dict(path=str(f.relative_to(ROOT)), sha256=sha(f)) for f in sorted((ROOT/'.trial-private/corpus-tools').glob('*')) if f.is_file()]
freeze = dict(source=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),runner_sha256=args.sha256,
              runner_version=subprocess.check_output([str(runner),'version'],text=True).strip(),plans=plans,inputs=inputs,targets=targets,
              admission='Windows amd64 runner; tig/taskwarrior targets use the separately admitted WSL lane',
              classification='12 executable-code defects; 3 changed-input/fixture controls, per E0')
(out/'freeze.json').write_text(json.dumps(freeze,indent=2)+'\n',encoding='utf-8')
rows=[]
for plan in plans:
    name=plan['id']; report=out/(name+'.json'); started=datetime.now(timezone.utc).isoformat(); tick=time.monotonic()
    with (out/(name+'.log')).open('wb') as log:
        result=subprocess.run([str(runner),'test','--report',str(report),'--artifacts-dir',str(out/(name+'-evidence')),plan['spec']],
                              cwd=ROOT,stdout=log,stderr=subprocess.STDOUT,timeout=65)
    captured=json.loads(report.read_text(encoding='utf-8'))['results'][0]
    category=captured.get('failure',{}).get('category')
    accepted=result.returncode==plan['expected_exit'] and captured['cleanup']['confirmed_exited'] is True
    if plan['category']: accepted=accepted and category==plan['category']
    if captured.get('workspace'): accepted=accepted and captured['workspace']['cleaned'] is True
    row=dict(**plan,exit=result.returncode,actual_category=category,accepted=accepted,result=captured,
             start_utc=started,end_utc=datetime.now(timezone.utc).isoformat(),wall_ms=(time.monotonic()-tick)*1000,runner_sha256=args.sha256)
    rows.append(row)
    with (out/'attempts.jsonl').open('a',encoding='utf-8') as ledger: ledger.write(json.dumps(row)+'\n')
    print(name,result.returncode,category,accepted,flush=True)
changed=[item['path'] for item in inputs if sha(ROOT/item['path'])!=item['sha256']]
summary=dict(attempts=len(rows),good=120,controls=15,recoveries=15,accepted=sum(r['accepted'] for r in rows),
             unexpected=[r['id'] for r in rows if not r['accepted']],changed_original_inputs=changed,runner_sha256=args.sha256)
(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
raise SystemExit(0 if all(r['accepted'] for r in rows) and not changed else 1)
