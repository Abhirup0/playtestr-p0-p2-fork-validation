"""Temporary source instrumentation with matched overhead controls, Linux only."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import time

ROOT=Path(__file__).resolve().parents[2]
out=ROOT/'artifacts/readiness-native/profile'
out.mkdir(parents=True,exist_ok=False)
scratch=ROOT/'.trial-private/readiness-profile-source'
scratch.mkdir(exist_ok=False)
for name in ['go.mod','go.sum']:shutil.copyfile(ROOT/name,scratch/name)
for name in ['internal','cmd/playtestr']:shutil.copytree(ROOT/name,scratch/name)
patches=[('internal/runner/runner.go','func executeStep(',''),('internal/runner/session.go','func (s *terminalSession) drainFinal(',''),('internal/runner/session.go','func (s *terminalSession) stop(','')]
for relative,anchor,_ in patches:
    path=scratch/relative
    text=path.read_text()
    if relative.endswith('session.go') and '"os"' not in text:
        text=text.replace('"os/exec"','"os/exec"\n\t"os"')
    assert text.count(anchor)==1
    beginning=text.index('{',text.index(anchor))+1
    label='executeStep' if 'executeStep' in anchor else ('drainFinal' if 'drainFinal' in anchor else 'stop')
    statement='\n if os.Getenv("READINESS_PROFILE") == "1" { started := time.Now(); defer func(){ fmt.Fprintf(os.Stderr,"READINESS_PHASE '+label+' %f\\n",float64(time.Since(started))/float64(time.Millisecond)) }() }\n'
    text=text[:beginning]+statement+text[beginning:]
    path.write_text(text)
subprocess.run(['gofmt','-w',str(scratch/'internal/runner/runner.go'),str(scratch/'internal/runner/session.go')],check=True)
binary=out/'instrumented-playtestr'
subprocess.run(['go','build','-trimpath','-o',str(binary),'./cmd/playtestr'],cwd=scratch,check=True,timeout=180)
normal=ROOT/'artifacts/competitive/bin/playtestr'
selector=ROOT/'artifacts/competitive/bin/selector'
subprocess.run(['go','build','-trimpath','-o',str(normal),'./cmd/playtestr'],cwd=ROOT,check=True)
if not selector.exists():raise SystemExit('Pinned C1 target preparation required')
rows=[]
for sample in range(1,31):
    order=['normal','instrumented'] if sample%2 else ['instrumented','normal']
    for mode in order:
        ident=f'{sample}-{mode}'
        env=os.environ.copy();env['C1_RESULT_PATH']=str(out/(ident+'-state.txt'))
        if mode=='instrumented':env['READINESS_PROFILE']='1'
        else:env.pop('READINESS_PROFILE',None)
        started=time.monotonic()
        with (out/(ident+'.log')).open('wb') as log:
            result=subprocess.run([str(normal if mode=='normal' else binary),'test',str(ROOT/'benchmarks/competitive/c1/playtestr.json')],cwd=ROOT,env=env,stdout=log,stderr=subprocess.STDOUT,timeout=15)
        state=Path(env['C1_RESULT_PATH']).read_text().strip() if Path(env['C1_RESULT_PATH']).exists() else None
        row=dict(sample=sample,mode=mode,elapsed_ms=(time.monotonic()-started)*1000,exit=result.returncode,state=state,accepted=result.returncode==0 and state=='Beta')
        rows.append(row)
        with (out/'observations.jsonl').open('a') as ledger:ledger.write(json.dumps(row)+'\n')
(out/'identities.json').write_text(json.dumps([{'path':str(p.relative_to(ROOT if p.is_relative_to(ROOT) else scratch)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [normal,binary,scratch/'internal/runner/runner.go',scratch/'internal/runner/session.go']],indent=2)+'\n')
raise SystemExit(0 if all(x['accepted'] for x in rows) else 1)
