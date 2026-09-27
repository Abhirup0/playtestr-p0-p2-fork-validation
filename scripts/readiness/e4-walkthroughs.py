"""Four clean-directory operator rehearsals, with all attempts retained.

Prerequisite: reviewed corpus target tools are installed. This does not measure
a human's first use, or pretend synthetic changes are upstream upgrades.
"""
import argparse
import copy
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import time

ROOT=Path(__file__).resolve().parents[2]
parser=argparse.ArgumentParser()
parser.add_argument('--runner',required=True)
parser.add_argument('--out',default='artifacts/e4 walkthroughs')
parser.add_argument('--projects',default='fzf,micro,create-vite,lazygit')
parser.add_argument('--revision',default='initial')
args=parser.parse_args()
runner=Path(args.runner).resolve()
out=(ROOT/args.out).resolve()
out.mkdir(parents=True,exist_ok=False)
tools=ROOT/'.trial-private/corpus-tools'
suffix='.exe' if os.name=='nt' else ''
rows=[]

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def now(): return datetime.now(timezone.utc).isoformat()
def write(p,data): p.write_text(json.dumps(data,ensure_ascii=True,indent=2)+'\n',encoding='utf-8')
def attempt(name,specpath,expected,category=None,update=False):
    report=out/(name+'.json'); tick=time.monotonic(); start=now()
    # HTML intentionally rejects absolute/traversing evidence references. Keep
    # evidence relative to the spec's invocation directory for offline export.
    argv=[str(runner),'test','--report',str(report),'--artifacts-dir',name+' evidence']
    if update: argv+=['--update']
    argv+=[str(specpath)]
    with (out/(name+'.log')).open('wb') as log:
        process=subprocess.run(argv,cwd=specpath.parent,stdout=log,stderr=subprocess.STDOUT,timeout=75)
    data=json.loads(report.read_text()) if report.exists() else {}
    result=data.get('results',[{}])[0]
    actual=result.get('failure',{}).get('category')
    clean=result.get('cleanup',{}).get('confirmed_exited')
    accepted=process.returncode==expected and (category is None or actual==category)
    if result and result.get('status')!='not-run': accepted=accepted and clean is True
    row=dict(case=name,start_utc=start,end_utc=now(),whole_command_ms=(time.monotonic()-tick)*1000,
        exit=process.returncode,expected_exit=expected,expected_category=category,accepted=accepted,
        runner_sha256=sha(runner),spec_sha256=sha(specpath),result=result,
        report=str(report.relative_to(ROOT)),cwd=str(specpath.parent.relative_to(ROOT)),
        operator='Codex familiar with injections; automated evidence inspection',human_minutes=None)
    rows.append(row); write(out/'attempts.json',rows)
    print(name,process.returncode,actual,'accepted',accepted,flush=True)
    return row

def import_spec(project,source,name):
    directory=out/project
    directory.mkdir(exist_ok=True)
    origin=ROOT/'corpus/workflows'/project/source
    spec=json.loads(origin.read_text(encoding='utf-8-sig'))
    fixture=origin.parent/spec['workspace']['fixture']
    destination=directory/spec['workspace']['fixture']
    if not destination.exists(): shutil.copytree(fixture,destination)
    if (origin.parent/'snapshots').exists() and not (directory/'snapshots').exists():
        shutil.copytree(origin.parent/'snapshots',directory/'snapshots')
    executable=(origin.parent/spec['command'][0]).resolve()
    if os.name=='nt' and executable.suffix!='.exe': executable=Path(str(executable)+'.exe')
    assert executable.exists(),str(executable)
    spec['command'][0]=str(executable)
    if os.name!='nt': spec['command']=[s.replace('reload(type candidates.txt)','reload(cat candidates.txt)') for s in spec['command']]
    path=directory/(name+'.json'); write(path,spec)
    return path,spec

journeys=[('fzf','fzf-01.json','fzf-01-known-bad.control'),
    ('micro','micro-01.json','micro-01-known-bad.control'),
    ('create-vite','create-vite-04.json','rw3-invalid-correction-code-defect.control'),
    ('lazygit','rw1-neighbor.control','rw1-neighbor-defect.control')]

# Freeze synthetic maintenance changes before any walkthrough execution.
# Selector: two invocation-level prompt changes; editor: two filename changes;
# wizard: framework and variant prompt changes independently; repository: two
# application labels independently. All retain the original state oracles.
maintenance=[('fzf','Find: ','Choose: '),('fzf','Find: ','Filter: '),
    ('micro','document.txt','draft notes.txt'),('micro','document.txt','draft review.txt'),
    ('create-vite','Select a framework:','Choose a framework:'),
    ('create-vite','Select a variant:','Choose a variant:'),
    ('lazygit','Staged changes','Indexed changes'),('lazygit','alpha.txt','aardvark.txt')]
write(out/'maintenance-freeze.json',[dict(project=p,old=a,new=b,kind='reviewed synthetic UI/fixture change; not an upstream upgrade') for p,a,b in maintenance])

for project,good,bad in journeys:
    if project not in args.projects.split(','): continue
    goodpath,spec=import_spec(project,good,'good')
    badpath,badspec=import_spec(project,bad,'defect')
    attempt(project+'-first',goodpath,0)
    # Reviewed baseline rehearsal occurs only in this clean disposable directory.
    # Snapshot adoption is explicit; persisted state is still independently checked.
    snapshot='e4-reviewed.txt'
    with_snapshot=copy.deepcopy(spec)
    # Wizard completion prints its random managed directory. Capture the stable
    # initial prompt after positive readiness, before any input, without masking.
    if project=='create-vite': with_snapshot['steps'].insert(1,{'snapshot':snapshot})
    else: with_snapshot['steps'].append({'snapshot':snapshot})
    baselinepath=goodpath.with_name('baseline.json'); write(baselinepath,with_snapshot)
    attempt(project+'-baseline-adopt',baselinepath,0,update=True)
    baseline=goodpath.parent/'snapshots'/snapshot
    before=sha(baseline)
    attempt(project+'-baseline-review',baselinepath,0)
    defectrow=attempt(project+'-defect',badpath,1)
    attempt(project+'-recovery',goodpath,0)
    assert before==sha(baseline),'Unexpected baseline modification'
    for number,(_,old,new) in enumerate([m for m in maintenance if m[0]==project],1):
        changed=copy.deepcopy(spec); changed_bad=copy.deepcopy(badspec)
        changed['steps']=[s for s in changed['steps'] if 'snapshot' not in s]
        changed_bad['steps']=[s for s in changed_bad['steps'] if 'snapshot' not in s]
        directory=goodpath.parent
        if project=='fzf':
            for data in (changed,changed_bad): data['command']=[s.replace(old,new) for s in data['command']]
            # Keep exact selected-record snapshot: prompt is removed when fzf exits.
            changed['steps'].append({'snapshot':'fzf-01.txt'})
            changed_bad['steps'].append({'snapshot':'fzf-01.txt'})
        elif project=='micro':
            fixture=directory/('maintenance-'+str(number)); shutil.copytree(directory/'fixture',fixture)
            (fixture/old).rename(fixture/new)
            for oracle in fixture.glob('*.oracle'):
                data=json.loads(oracle.read_text()); data['files']={new if k==old else k:v for k,v in data['files'].items()}; write(oracle,data)
            for data in (changed,changed_bad):
                data['workspace']['fixture']=fixture.name
                data['command']=[new if s==old else s for s in data['command']]
        elif project=='create-vite':
            for data,original,label in [(changed,'create-vite-runtime','good'),(changed_bad,'create-vite-code-mutated-runtime','bad')]:
                destination=tools/f'e4-vite-{args.revision}-{number}-{label}'
                shutil.copytree(tools/original,destination)
                js=destination/'node_modules/create-vite/dist/index.js'; text=js.read_text(encoding='utf-8'); assert text.count(old)==1
                js.write_text(text.replace(old,new),encoding='utf-8')
                data['env']={**data.get('env',{}),'PLAYTESTR_CREATE_VITE_RUNTIME':destination.name}
        else:
            # Prepared pinned target/oracle variants live beside their supporting
            # binaries; their reviewed source patches and hashes are in setup.json.
            for data,label in [(changed,'good'),(changed_bad,'bad')]:
                data['command'][0]=str(tools/f'e4-lazygit-{number}-{label}'/('lazygit-oracle'+suffix))
                data['env']={}
        unmodified=directory/f'm{number}-unmodified.json'; write(unmodified,changed)
        attempt(f'{project}-m{number}-first-unmodified',unmodified,1,'assertion_timeout')
        def repair(data):
            for step in data['steps']:
                if 'expect' in step: step['expect']=step['expect'].replace(old,new)
        repair(changed); repair(changed_bad)
        repaired=directory/f'm{number}-repaired.json'; negative=directory/f'm{number}-defect.json'
        write(repaired,changed); write(negative,changed_bad)
        attempt(f'{project}-m{number}-repair',repaired,0)
        attempt(f'{project}-m{number}-defect',negative,1)
        attempt(f'{project}-m{number}-recovery',repaired,0)
        write(directory/f'm{number}-cost.json',dict(old=old,new=new,
            changed_spec_lines=sum(1 for a,b in zip(json.dumps(spec,indent=2).splitlines(),json.dumps(changed,indent=2).splitlines()) if a!=b),
            helper_and_fixture_files=[{'path':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size} for p in directory.rglob('*') if p.is_file()],
            human_minutes=None,baseline_changed=False,maintenance_kind='synthetic'))
write(out/'summary.json',dict(attempts=len(rows),accepted=sum(r['accepted'] for r in rows),
    runner_sha256=sha(runner),host=platform.platform(),human_first_use='not measured',
    source=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
    total_helper_lines=sum(len(p.read_text(encoding='utf-8').splitlines()) for p in (ROOT/'corpus/controls').rglob('*.go'))))
raise SystemExit(0 if all(r['accepted'] for r in rows) else 1)
