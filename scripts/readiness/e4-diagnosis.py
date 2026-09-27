"""Six predeclared diagnosis classes; familiar automated operator, no human timing."""
import argparse
import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parents[2]
p=argparse.ArgumentParser(); p.add_argument('--runner',required=True); p.add_argument('--out',default='artifacts/e4 diagnosis')
args=p.parse_args(); runner=Path(args.runner).resolve(); out=ROOT/args.out; out.mkdir(parents=True,exist_ok=False)
target=out/'target.py'
target.write_text('''import pathlib,sys,time
mode=sys.argv[1]
print("diagnosis target ready",flush=True)
if mode=="hang": time.sleep(60)
elif mode=="wrong-exit": sys.exit(7)
elif mode=="defect":
 pathlib.Path("saved.txt").write_bytes(b"wrong\\n")
 print("Saved successfully",flush=True)
 if pathlib.Path("saved.txt").read_bytes()!=b"reviewed\\n":
  print("INDEPENDENT_STATE_ORACLE failed",flush=True)
  sys.exit(9)
else: print("reviewed state",flush=True)
''')
base=dict(version=1,command=[sys.executable,str(target),'good'],width=60,height=12,
    timeout_ms=750,run_timeout_ms=5000,max_output_bytes=100000,
    steps=[{'expect':'diagnosis target ready'},{'expect':'reviewed state'},{'exit':0}])
cases=[('target-logic-defect','wrong persisted bytes despite Saved successfully','unexpected_exit',2),
    ('bad-spec','unsupported spec version','invalid_spec',None),
    ('missing-runtime','missing executable','launch_failure',None),
    ('assertion-timeout','live target never renders reviewed state','assertion_timeout',2),
    ('wrong-exit','target exits seven, spec requires zero','unexpected_exit',2),
    ('artifact-failure','evidence directory path is a regular file',None,None)]
(out/'expected.json').write_text(json.dumps(cases,indent=2)+'\n')
rows=[]
for name,cause,category,step in cases:
    spec=copy.deepcopy(base)
    if name=='target-logic-defect':
        spec['command'][-1]='defect'; spec['steps'][1]={'expect':'INDEPENDENT_STATE_ORACLE passed'}
    if name=='bad-spec': spec['version']=999
    if name=='missing-runtime': spec['command']=[str(out/'absent-runtime')]
    if name=='assertion-timeout': spec['command'][-1]='hang'
    if name=='wrong-exit': spec['command'][-1]='wrong-exit'; spec['steps']=[spec['steps'][0],{'exit':0}]
    specpath=out/(name+'.json'); specpath.write_text(json.dumps(spec,indent=2)+'\n')
    report=out/(name+'-report.json'); evidence=out/(name+' evidence')
    if name=='artifact-failure': evidence.write_bytes(b'blocked path\n')
    start=datetime.now(timezone.utc).isoformat(); tick=time.monotonic()
    process=subprocess.run([str(runner),'test','--report',str(report),'--artifacts-dir',str(evidence),str(specpath)],cwd=out,
        stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=15)
    (out/(name+'.log')).write_bytes(process.stdout)
    result=json.loads(report.read_text())['results'][0] if report.exists() else {}
    actual=result.get('failure',{}).get('category')
    failed=next((s['number'] for s in result.get('steps',[]) if s['status']=='failed'),None)
    accepted=process.returncode!=0 and (actual==category if category else b'artifact' in process.stdout.lower()) and failed==step
    if name not in ('bad-spec','missing-runtime','artifact-failure'): accepted=accepted and result.get('cleanup',{}).get('confirmed_exited') is True
    rows.append(dict(case=name,expected_root_cause=cause,expected_category=category,expected_step=step,exit=process.returncode,
        actual_category=actual,actual_step=failed,accepted=accepted,result=result,
        start_utc=start,end_utc=datetime.now(timezone.utc).isoformat(),whole_command_ms=(time.monotonic()-tick)*1000,
        diagnosis='automated inspection of predeclared variant; familiar operator',human_diagnosis_minutes=None,
        independent_state_hex=(out/'saved.txt').read_bytes().hex() if name=='target-logic-defect' else None,
        runner_sha256=hashlib.sha256(runner.read_bytes()).hexdigest()))
    (out/'attempts.json').write_text(json.dumps(rows,indent=2)+'\n')
    print(name,process.returncode,actual,failed,accepted,flush=True)
raise SystemExit(0 if all(r['accepted'] for r in rows) else 1)
