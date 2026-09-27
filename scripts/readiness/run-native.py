"""Native discovery ledger: real runner, unchanged evidence, no retries."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import signal
import subprocess
import time

ROOT=Path(__file__).resolve().parents[2]
parser=argparse.ArgumentParser()
parser.add_argument('--runner',required=True)
parser.add_argument('--out',default='artifacts/readiness-native/tasks')
args=parser.parse_args()
runner=Path(args.runner).resolve()
out=ROOT/args.out
out.mkdir(parents=True,exist_ok=False)
host=platform.system().lower()+'_'+platform.machine()
runner_sha=hashlib.sha256(runner.read_bytes()).hexdigest()
rows=[]

def adapt(source):
    original=ROOT/source
    spec=json.loads(original.read_text(encoding='utf-8-sig'))
    spec['command']=[x.replace('reload(type candidates.txt)','reload(cat candidates.txt)') for x in spec['command']]
    # Keep fixture/snapshot resolution at the reviewed source directory.
    native=original.with_name('native-'+original.stem+'.control')
    native.write_text(json.dumps(spec,indent=2)+'\n')
    return native

def attempt(identity,source,expected,categories=('unexpected_exit','snapshot_mismatch')):
    spec=adapt(source)
    report=out/(identity+'.json')
    log=out/(identity+'.log')
    started=time.monotonic()
    timed_out=False
    with log.open('wb') as stream:
        process=subprocess.Popen([str(runner),'test','--report',str(report),'--artifacts-dir',str(out/(identity+'-artifacts')),str(spec)],cwd=ROOT,stdout=stream,stderr=subprocess.STDOUT,start_new_session=True)
        try:
            exitcode=process.wait(timeout=90)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid,signal.SIGKILL)
            exitcode=process.wait(timeout=5)
            timed_out=True
    result=json.loads(report.read_text())['results'][0] if report.exists() else {}
    cleanup=result.get('cleanup',{})
    workspace=result.get('workspace',{})
    failure=result.get('failure',{}).get('category')
    expected_failure=failure in categories if expected else failure is None
    # On native Linux the staging mutation omits the Staged changes section;
    # the unchanged readiness assertion detects it before the Git oracle. Admit
    # this exact failure only, retaining the original narrower classification.
    early_stage_failure=(identity=='RW1-defect' and failure=='assertion_timeout'
        and any(x.get('number')==7 and x.get('status')=='failed' for x in result.get('steps',[]))
        and result.get('target',{}).get('exit_code')==1)
    expected_failure=expected_failure or early_stage_failure
    valid=exitcode==expected and not timed_out and expected_failure and cleanup.get('confirmed_exited') is True and workspace.get('cleaned') is True
    row=dict(attempt_id=identity,source_spec=source,adapted_spec=str(spec.relative_to(ROOT)),spec_sha256=hashlib.sha256(spec.read_bytes()).hexdigest(),runner_sha256=runner_sha,host=host,exit=exitcode,expected_exit=expected,whole_command_ms=(time.monotonic()-started)*1000,harness_timeout=timed_out,accepted=valid,detection='missing staged section before Git oracle' if early_stage_failure else 'reviewed assertion/state oracle',report=str(report.relative_to(ROOT)),result=result)
    rows.append(row)
    with (out/'attempts.jsonl').open('a') as ledger: ledger.write(json.dumps(row)+'\n')
    print(identity,'exit',exitcode,'accepted',valid,flush=True)
    return valid

journeys=[
 ('RW1','lazygit/rw1-neighbor.control','lazygit/rw1-neighbor-defect.control'),
 ('RW2','micro/rw2-reopen.control','micro/rw2-reopen-defect.control'),
 ('RW3','create-vite/create-vite-04.json','create-vite/rw3-invalid-correction-code-defect.control'),
 ('RW4','fzf/fzf-01.json','fzf/fzf-01-known-bad.control'),
 ('RW5','litecli/rw5-transaction.control','litecli/rw5-transaction-defect.control'),
 ('RW6','posting/rw6-edit-save-send.control','posting/rw6-edit-save-send-defect.control')]
pilot=[]
for ident,good,bad in journeys:
    pilot.append(attempt(ident+'-pilot','corpus/workflows/'+good,0))
if all(pilot):
    for ident,good,bad in journeys:
        for i in range(1,6): attempt(ident+'-good-'+str(i),'corpus/workflows/'+good,0)
        attempt(ident+'-defect','corpus/workflows/'+bad,1)
        attempt(ident+'-recovery','corpus/workflows/'+good,0)
    variations=[
        'lazygit/rw1-resize.control','micro/rw2-ui-maintained.control',
        'micro/micro-05.json','micro/micro-08.json','micro/rw2-realistic.control',
        'create-vite/create-vite-04.json','create-vite/create-vite-05.json',
        'fzf/fzf-03.json','fzf/fzf-04.json','fzf/rw4-combining.control',
        'litecli/rw5-transaction.control','posting/rw6-slow-response.control',
        'posting/posting-07.json']
    for number,source in enumerate(variations,1):
        attempt('variation-'+str(number),'corpus/workflows/'+source,0)
    # Synthetic UI maintenance: original expectation must fail for readiness;
    # maintained target must pass and retain state-defect sensitivity.
    for ident,project in [('rw2','micro'),('rw3','create-vite'),('rw6','posting')]:
        for phase,variant,exitcode in [('unmaintained','unmaintained',1),('maintained','maintained',0),('defect','defect',1),('recovery','maintained',0)]:
            source=f'corpus/workflows/{project}/{ident}-ui-{variant}.control'
            # A deliberate wording change is expected to time out, not a target defect.
            if phase=='unmaintained':
                attempt(ident+'-maintenance-'+phase,source,exitcode,('assertion_timeout',))
            else: attempt(ident+'-maintenance-'+phase,source,exitcode)
else:
    print('Pilot failures retained; discovery campaign deferred until diagnostic revision',flush=True)
summary=dict(host=host,runner_sha256=runner_sha,attempts=len(rows),accepted=sum(x['accepted'] for x in rows),pilot_accepted=all(pilot),e1_complete=False,scope='native task cells; variation and wider acceptance gates classified separately')
(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
raise SystemExit(0 if all(x['accepted'] for x in rows) else 1)
