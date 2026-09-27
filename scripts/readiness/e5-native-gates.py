"""Exercise frozen bytes against bounded native lifecycle and sampled suites."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import time

p=argparse.ArgumentParser(); p.add_argument('--runner',required=True); p.add_argument('--fixture',required=True); p.add_argument('--out',required=True)
args=p.parse_args(); runner=Path(args.runner).resolve(); fixture=Path(args.fixture).resolve(); out=Path(args.out).resolve()
out.mkdir(parents=True,exist_ok=False)
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
freeze=dict(runner_sha256=sha(runner),fixture_sha256=sha(fixture),version=subprocess.check_output([str(runner),'version'],text=True).strip(),
            source=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),host=os.uname().sysname if os.name!='nt' else 'Windows')
(out/'freeze.json').write_text(json.dumps(freeze,indent=2)+'\n')
cases=[('hang','hang',[{'expect':'fixture ready; waiting forever'},{'expect':'never arrives'}],500,2000,'assertion_timeout'),
       ('run-deadline','hang',[{'expect':'fixture ready; waiting forever'},{'expect':'never arrives'}],2000,500,'run_timeout'),
       ('flood','flood',[{'expect':'never arrives'}],2000,3000,'output_limit'),
       ('descendant','child',[{'expect':'started child'},{'exit':0}],500,2000,'assertion_timeout')]
rows=[]
for name,mode,steps,step_ms,run_ms,category in cases:
    spec=out/(name+'.json'); report=out/(name+'-report.json')
    spec.write_text(json.dumps(dict(version=1,name=name,command=[str(fixture),mode],timeout_ms=step_ms,run_timeout_ms=run_ms,
                                   max_output_bytes=4096 if name=='flood' else 100000,steps=steps)))
    tick=time.monotonic()
    with (out/(name+'.log')).open('wb') as log:
        result=subprocess.run([str(runner),'test','--report',str(report),'--artifacts-dir',str(out/(name+'-evidence')),str(spec)],stdout=log,stderr=subprocess.STDOUT,timeout=15)
    captured=json.loads(report.read_text())['results'][0]
    accepted=result.returncode==1 and captured['failure']['category']==category and captured['cleanup']['confirmed_exited']
    rows.append(dict(id=name,expected_category=category,exit=result.returncode,result=captured,accepted=accepted,wall_ms=(time.monotonic()-tick)*1000))
    print(name,accepted,flush=True)
# The full native cancellation gate already ran during archive extraction.
# These resource cells are one sample each, not statistical or real-app speed claims.
seed=out/'fixture'; seed.mkdir(); (seed/'seed.txt').write_text('reviewed\n')
for size in [1,10,50]:
    specs=[]
    for number in range(size):
        spec=out/f'suite-{size}-{number}.json'
        spec.write_text(json.dumps(dict(version=2,name=f'native fixture {size}/{number}',command=[str(fixture),'workspace'],
            workspace=dict(fixture='fixture',cwd='.',home='temporary',temp='temporary'),width=72,height=12,timeout_ms=3000,run_timeout_ms=10000,
            steps=[dict(expect='fresh workspace seed=reviewed home=true temp=true'),dict(exit=0)])))
        specs.append(str(spec))
    report=out/f'suite-{size}-report.json'; tick=time.monotonic(); started=datetime.now(timezone.utc).isoformat()
    peak=0; sampled_cpu=0; samples=0; observed=set(); rss_series=[]
    with (out/f'suite-{size}.log').open('wb') as log:
        process=subprocess.Popen([str(runner),'test','--report',str(report),'--artifacts-dir',str(out/f'suite-{size}-evidence')]+specs,stdout=log,stderr=subprocess.STDOUT)
        while process.poll() is None:
            if time.monotonic()-tick>15*size+15:
                process.kill(); process.wait(timeout=10); raise RuntimeError('bounded suite harness deadline')
            if os.name!='nt':
                # No environment or command lines are retained. Coarse ps CPU
                # and 100ms RSS samples miss short-lived descendants.
                output=subprocess.check_output(['ps','-axo','pid=,ppid=,rss=,time='],text=True)
                inventory=[]
                for line in output.splitlines():
                    pid,parent,rss,cpu=line.split(); inventory.append((int(pid),int(parent),int(rss),cpu))
                reachable={process.pid}
                for _ in range(len(inventory)):
                    children={pid for pid,parent,_,_ in inventory if parent in reachable}
                    if children<=reachable: break
                    reachable |= children
                live=[r for r in inventory if r[0] in reachable]; observed |= reachable
                peak=max(peak,sum(r[2]*1024 for r in live)); samples+=1
                if len(rss_series)<5000: rss_series.append(sum(r[2]*1024 for r in live))
                total=0
                for _,_,_,cpu in live:
                    pieces=cpu.split(':'); seconds=0.0
                    for piece in pieces: seconds=seconds*60+float(piece)
                    total+=seconds*1000
                sampled_cpu=max(sampled_cpu,total)
            time.sleep(.1)
        process.wait(timeout=10)
    captured=json.loads(report.read_text())
    survivors=None
    if os.name!='nt':
        live_pids={int(line) for line in subprocess.check_output(['ps','-axo','pid='],text=True).splitlines()}
        survivors=sorted(observed & live_pids)
    accepted=process.returncode==0 and captured['summary']['passed']==size and all(r['cleanup']['confirmed_exited'] and r['workspace']['cleaned'] for r in captured['results'])
    evidence_bytes=report.stat().st_size+sum(f.stat().st_size for f in (out/f'suite-{size}-evidence').rglob('*') if f.is_file())
    rows.append(dict(id=f'suite-{size}',size=size,replications=1,exit=process.returncode,accepted=accepted,start_utc=started,
        wall_ms=(time.monotonic()-tick)*1000,artifact_bytes=evidence_bytes,sample_count=samples,sampled_tree_peak_rss_bytes=peak if samples else None,
        sampled_tree_cpu_ms=sampled_cpu if samples else None,observed_pids=sorted(observed),observed_survivor_pids=survivors,sampled_tree_rss_series_bytes=rss_series,
        limitation='Synthetic native fixture, n=1 per size; coarse sampled CPU/RSS lower bounds; short-lived descendants and PID reuse remain limitations. Windows real-task tree measurements are separate.'))
    print('suite',size,accepted,flush=True)
(out/'observations.json').write_text(json.dumps(dict(freeze=freeze,attempts=rows),indent=2)+'\n')
raise SystemExit(0 if all(r['accepted'] for r in rows) else 1)
