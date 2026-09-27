"""Linux /proc lower-bound resource samples and uninstrumented controls."""
import argparse
import json
import os
from pathlib import Path
import signal
import subprocess
import time

ROOT=Path(__file__).resolve().parents[2]
p=argparse.ArgumentParser();p.add_argument('--runner',required=True);p.add_argument('--candidate');p.add_argument('--out',default='artifacts/readiness-native/resources');a=p.parse_args()
out=ROOT/a.out;out.mkdir(parents=True,exist_ok=False)
sources=['lazygit/rw1-resize.control','micro/rw2-basic-unicode.control','create-vite/create-vite-04.json','litecli/rw5-transaction.control','posting/rw6-slow-response.control']
tick=os.sysconf('SC_CLK_TCK');page=os.sysconf('SC_PAGE_SIZE')
inputs=[]
for number,source in enumerate(sources):
    original=ROOT/'corpus/workflows'/source
    data=json.loads(original.read_text());data['command'][0]=str((original.parent/data['command'][0]).resolve())
    data['workspace']['fixture']=str((original.parent/data['workspace']['fixture']).resolve())
    # Public contract forbids absolute fixtures: keep definition beside source.
    data['workspace']['fixture']=json.loads(original.read_text())['workspace']['fixture']
    path=original.with_name('resource-'+str(number)+'.control');path.write_text(json.dumps(data,indent=2)+'\n');inputs.append(path)

def inventory():
    records={}
    for path in Path('/proc').iterdir():
        if not path.name.isdigit():continue
        try:
            fields=(path/'stat').read_text().rsplit(') ',1)[1].split()
            records[int(path.name)]={'ppid':int(fields[1]),'born':int(fields[19]),'cpu_ms':(int(fields[11])+int(fields[12]))*1000/tick,'rss_bytes':int(fields[21])*page}
        except (OSError,ValueError,IndexError):pass
    return records

rows=[]
def attempt(size,sample,instrumented,mode='baseline'):
    identity=f'{mode}-size-{size}-{sample}-'+('sampled' if instrumented else 'plain')
    aliases=[]
    for i in range(size):
        source=inputs[i%len(inputs)];data=json.loads(source.read_text())
        path=source.with_name(identity+'-'+str(i)+'.control');path.write_text(json.dumps(data,indent=2)+'\n');aliases.append(path)
    report=out/(identity+'.json');evidence=out/(identity+'-artifacts')
    owned={};peak=0;samples=[];timed_out=False
    started=time.monotonic()
    with (out/(identity+'.log')).open('wb') as log:
        proc=subprocess.Popen([a.candidate if mode=='candidate' else a.runner,'test','--report',str(report),'--artifacts-dir',str(evidence),*[str(x) for x in aliases]],cwd=ROOT,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
        while proc.poll() is None:
            if time.monotonic()-started>size*35+10:
                os.killpg(proc.pid,signal.SIGKILL);proc.wait(timeout=5);timed_out=True;break
            if instrumented:
                records=inventory();reachable={proc.pid:records[proc.pid]['born']} if proc.pid in records else {}
                added=True
                while added:
                    added=False
                    for pid,item in records.items():
                        if pid not in reachable and item['ppid'] in reachable and item['born']>=reachable[item['ppid']]:reachable[pid]=item['born'];added=True
                resident=0
                for pid,born in reachable.items():
                    item=records[pid];key=f'{pid}:{born}'
                    owned[key]=dict(pid=pid,born=born,cpu_ms=max(item['cpu_ms'],owned.get(key,{}).get('cpu_ms',0)))
                    resident+=item['rss_bytes']
                peak=max(peak,resident);samples.append(dict(elapsed_ms=(time.monotonic()-started)*1000,rss_bytes=resident))
            time.sleep(.02)
        exitcode=proc.wait(timeout=5)
    wall=(time.monotonic()-started)*1000
    product=json.loads(report.read_text()) if report.exists() else {'results':[]}
    results=product['results']
    after=inventory() if instrumented else {}
    survivors=[x for x in owned.values() if x['pid'] in after and after[x['pid']]['born']==x['born']]
    row=dict(identity=identity,mode=mode,size=size,sample=sample,instrumented=instrumented,wall_ms=wall,exit=exitcode,harness_timeout=timed_out,passed=sum(x['status']=='passed' for x in results),cleanup_unconfirmed=sum(not x.get('cleanup',{}).get('confirmed_exited') or not x.get('workspace',{}).get('cleaned') for x in results),sampled_cpu_ms=sum(x['cpu_ms'] for x in owned.values()) if instrumented else None,sampled_peak_rss_bytes=peak if instrumented else None,observed_survivors=survivors,resource_samples=samples,artifact_bytes=sum(x.stat().st_size for x in evidence.rglob('*') if x.is_file())+(report.stat().st_size if report.exists() else 0),scope='Linux proc samples miss short-lived/reparented children; aggregate CPU/RSS lower bounds; no complete survivor guarantee')
    row['accepted']=exitcode==0 and not timed_out and row['passed']==size and row['cleanup_unconfirmed']==0 and not survivors
    rows.append(row)
    with (out/'observations.jsonl').open('a') as ledger:ledger.write(json.dumps(row)+'\n')
    print(identity,'passed',row['passed'],'wall_ms',round(wall),'accepted',row['accepted'],flush=True)
for sample in range(1,31):
    for instrumented in ([False,True] if sample%2 else [True,False]):
        for mode in (['baseline','candidate'] if sample%2 else ['candidate','baseline']) if a.candidate else ['baseline']:
            attempt(1,sample,instrumented,mode)
for size in [10,50]:
    for instrumented in [False,True]:
        for mode in (['baseline','candidate'] if size==10 else ['candidate','baseline']) if a.candidate else ['baseline']:
            attempt(size,1,instrumented,mode)
(out/'summary.json').write_text(json.dumps(dict(attempts=len(rows),accepted=sum(x['accepted'] for x in rows),scope='30 matched instrumentation controls for size 1; single larger suites and within-suite drift'),indent=2)+'\n')
raise SystemExit(0 if all(x['accepted'] for x in rows) else 1)
