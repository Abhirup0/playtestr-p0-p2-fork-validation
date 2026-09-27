"""Counterbalanced E2 RW1/RW3 comparison with identical workspace glue."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shlex
import signal
import subprocess
import time
import yaml

ROOT=Path(__file__).resolve().parents[2]
p=argparse.ArgumentParser()
p.add_argument('--runner',required=True)
p.add_argument('--atago',required=True)
p.add_argument('--samples',type=int,default=30)
p.add_argument('--out',default='artifacts/readiness-native/real-comparison')
a=p.parse_args()
if not 1<=a.samples<=100: raise SystemExit('bounded samples required')
out=ROOT/a.out;out.mkdir(parents=True,exist_ok=False)
launcher=ROOT/'.trial-private/corpus-tools/workspace-launch'
subprocess.run(['go','build','-trimpath','-o',str(launcher),'./scripts/readiness/workspace-launch'],cwd=ROOT,check=True)
pins=[Path(a.runner).resolve(),Path(a.atago).resolve(),launcher]
(out/'adapter-pins.json').write_text(json.dumps([{'path':str(x),'sha256':hashlib.sha256(x.read_bytes()).hexdigest()} for x in pins],indent=2)+'\n')
rows=[]
manifest=ROOT/'benchmarks/competitive/c1/termlens/Cargo.toml'
cargo_env=os.environ.copy();cargo_env['CARGO_TARGET_DIR']=str(ROOT/'artifacts/competitive/cargo-target')
subprocess.run(['cargo','+1.85.0','test','--offline','--locked','--no-run','--manifest-path',str(manifest),'--test','real'],cwd=ROOT,env=cargo_env,check=True,timeout=180)

def attempt(journey,tool,phase,number,variant):
    identity=f'{journey}-{phase}-{number}-{tool}'
    result=out/(identity+'-state.json')
    marker=f'PLAYTESTR-E2-{journey}-WRAPPER-OK'
    command=[str(launcher),'-journey',journey,'-root',str(ROOT),'-variant',variant,'-output',str(result)]
    original=ROOT/('corpus/workflows/lazygit/rw1-neighbor.control' if journey=='RW1' else 'corpus/workflows/create-vite/create-vite-04.json')
    source=json.loads(original.read_text())
    # The same reviewed keyboard/readiness steps precede the common result marker.
    steps=source['steps'][:-2]+[{'expect':marker},{'exit':0}]
    if journey=='RW1':
        # Both adapters rely on the exact post-exit Git oracle, including the
        # unchanged neighbor, rather than the transient staged-pane heading.
        steps=[step for step in steps if step.get('expect')!='Staged changes']
    evidence=out/(identity+'-evidence')
    if tool=='playtestr':
        spec={k:v for k,v in source.items() if k not in ('workspace','env','command')}
        spec.update(version=1,command=command,steps=steps)
        definition=out/(identity+'.json');definition.write_text(json.dumps(spec,indent=2)+'\n')
        argv=[a.runner,'test','--report',str(out/(identity+'-report.json')),'--artifacts-dir',str(evidence),str(definition)]
    elif tool=='atago':
        actions=[]
        keys={'ArrowDown':'down','ArrowRight':'right','Enter':'enter'}
        for step in steps[:-2]:
            if 'expect' in step: actions.append({'expect_screen':{'contains':step['expect']}})
            elif 'text' in step: actions.append({'send':step['text']})
            elif 'key' in step: actions.append({'send':{'key':keys[step['key']]}})
        actions.append({'expect':marker})
        spec={'version':'1','suite':{'name':identity},'scenarios':[{'name':journey,'steps':[{'pty':{'command':shlex.join(command),'rows':source['height'],'cols':source['width'],'timeout':'30s','session':actions}},{'assert':{'exit_code':0,'stdout':{'contains':marker}}}]}]}
        definition=out/(identity+'.yaml');definition.write_text(yaml.safe_dump(spec,sort_keys=False))
        argv=[a.atago,'run','--ci','--parallel','1','--artifacts-dir',str(evidence),str(definition)]
    else:
        definition=manifest.parent/'tests/real.rs'
        argv=['cargo','+1.85.0','test','--offline','--locked','--manifest-path',str(manifest),'--test','real','--','real_'+journey.lower(),'--exact','--nocapture']
    env=cargo_env.copy()
    env.update(RWX_LAUNCHER=str(launcher),RWX_ROOT=str(ROOT),RWX_VARIANT=variant,RWX_RESULT=str(result))
    started=time.monotonic()
    with (out/(identity+'.log')).open('wb') as log:
        process=subprocess.Popen(argv,cwd=ROOT,env=env,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
        timeout=False
        try: exitcode=process.wait(timeout=45)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid,signal.SIGKILL);exitcode=process.wait(timeout=5);timeout=True
    state=json.loads(result.read_text()) if result.exists() else None
    expected=1 if variant=='defect' else 0
    accepted=not timeout and (exitcode!=0 if expected else exitcode==0) and state is not None and state['cleaned'] and state.get('target_started') and (state['exit']!=0 and state.get('independent_state_defect') if expected else state['exit']==0)
    row=dict(identity=identity,journey=journey,tool=tool,phase=phase,sample=number,exit=exitcode,expected_status='nonzero' if expected else 'zero',harness_timeout=timeout,whole_command_ms=(time.monotonic()-started)*1000,state=state,accepted=accepted,adapter_sha256=hashlib.sha256(definition.read_bytes()).hexdigest())
    rows.append(row)
    with (out/'attempts.jsonl').open('a') as ledger:ledger.write(json.dumps(row)+'\n')
    print(identity,'exit',exitcode,'accepted',accepted,flush=True)
    return accepted

controls=[]
for journey in ['RW1','RW3']:
    for tool in ['playtestr','atago','termlens']:
        for phase,variant in [('pilot','good'),('defect','defect'),('recovery','good')]: controls.append(attempt(journey,tool,phase,0,variant))
if all(controls):
    for number in range(1,a.samples+1):
        orders=[['playtestr','atago','termlens'],['termlens','atago','playtestr'],['atago','playtestr','termlens'],['termlens','playtestr','atago'],['atago','termlens','playtestr'],['playtestr','termlens','atago']]
        order=orders[(number-1)%len(orders)]
        for journey in ['RW1','RW3']:
            for tool in order:attempt(journey,tool,'measurement',number,'good')
else:print('Invalid comparator controls: retain failures, defer measurement',flush=True)
(out/'summary.json').write_text(json.dumps(dict(controls_accepted=all(controls),attempts=len(rows),accepted=sum(x['accepted'] for x in rows),scope='matched common fixture/oracle/cleanup glue; no universal tree-cleanup or effort superiority claim'),indent=2)+'\n')
raise SystemExit(0 if all(x['accepted'] for x in rows) else 1)
