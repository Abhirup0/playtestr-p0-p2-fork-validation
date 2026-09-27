"""Side-by-side private upgrade preparation; preserve reviewed v1 snapshots."""
import hashlib
import json
from pathlib import Path
import subprocess
ROOT=Path(__file__).resolve().parents[2]
out=ROOT/'artifacts/e5-compatibility'; out.mkdir(parents=True,exist_ok=False)
new=ROOT/'artifacts/e5 frozen candidate extracted/playtestr_0.4.0-rc.2_windows_amd64/playtestr.exe'
old=ROOT/'artifacts/upgrade previous extracted/playtestr_0.3.0-rc.1_windows_amd64/playtestr.exe'
public=ROOT/'artifacts/qualified candidate extracted/playtestr_0.4.0-rc.1_windows_amd64/playtestr.exe'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
baseline=ROOT/'examples/snapshots/diagnostics.txt'; original=sha(baseline)
rows=[]
def run(name,binary,spec,expected,report_version,category=None):
    report=out/(name+'.json'); evidence=out/(name+'-evidence')
    with (out/(name+'.log')).open('wb') as log:
        process=subprocess.run([str(binary),'test','--report',str(report.relative_to(ROOT)),'--artifacts-dir',str(evidence.relative_to(ROOT)),spec],
                               cwd=ROOT,stdout=log,stderr=subprocess.STDOUT,timeout=30)
    result=json.loads(report.read_text()); first=result['results'][0]
    accepted=process.returncode==expected and result['report_version']==report_version
    if category: accepted=accepted and first.get('failure',{}).get('category')==category
    if category!='invalid_spec': accepted=accepted and first['cleanup']['confirmed_exited']
    rows.append(dict(id=name,runner_sha256=sha(binary),version=subprocess.check_output([str(binary),'version'],text=True).strip(),
                     exit=process.returncode,accepted=accepted,result=result))
for label,binary in [('old-v03',old),('public-v04rc1',public),('private-v04rc2',new)]:
    run(label+'-pass',binary,'examples/menu.json',0,1)
    run(label+'-failure',binary,'examples/snapshot-mismatch.json',1,1,'snapshot_mismatch')
    run(label+'-recovery',binary,'examples/menu.json',0,1)
run('old-v03-rejects-v2',old,'examples/workspace.json',1,1,'invalid_spec')
run('public-v04rc1-v2',public,'examples/workspace.json',0,2)
run('private-v04rc2-v2',new,'examples/workspace.json',0,2)
v1=out/'old-v03-failure.json'
v2=out/'private-v04rc2-v2.json'
for name,reader,input_file,expected in [('new-reader-old-v1',new,v1,0),('new-reader-v2',new,v2,0),('old-reader-rejects-v2',old,v2,1)]:
    with (out/(name+'.log')).open('wb') as log:
        process=subprocess.run([str(reader),'report','--input',str(input_file.relative_to(ROOT)),
                               '--evidence-root','artifacts','--output',str((out/(name+'.html')).relative_to(ROOT))],cwd=ROOT,stdout=log,stderr=subprocess.STDOUT,timeout=15)
    rows.append(dict(id=name,runner_sha256=sha(reader),exit=process.returncode,expected_exit=expected,accepted=process.returncode==expected))
assert sha(baseline)==original
(out/'observations.json').write_text(json.dumps(dict(attempts=rows,baseline_sha256=original,baseline_preserved=True,
    route='Private source upgrade preparation alongside retained public binaries; candidate is not publicly downloadable'),indent=2)+'\n')
print(json.dumps([(r['id'],r['accepted']) for r in rows]))
raise SystemExit(0 if all(r['accepted'] for r in rows) else 1)
