"""Retain compact E5 identities/results; never infer a pass from configuration."""
import argparse
from collections import Counter
from datetime import datetime
import hashlib
import json
from pathlib import Path
import statistics

ROOT=Path(__file__).resolve().parents[2]
p=argparse.ArgumentParser(); p.add_argument('--complete',action='store_true'); args=p.parse_args()
def read(path):
    data=path.read_bytes(); return json.loads(data.decode('utf-16' if data[:2] in [b'\xff\xfe',b'\xfe\xff'] else 'utf-8-sig'))
def lines(path): return [json.loads(line) for line in path.read_text(encoding='utf-8-sig').splitlines() if line.startswith('{')]
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
packet=dict(schema_version=1,status='pending',source_commit='ae97c62022966cde9699b26169b4dc6ef0a12439',
    version='v0.4.0-rc.2',candidate=read(ROOT/'release/e5-candidate-manifest.json'),native_source=[])
source=ROOT/'artifacts/e5-native-source-36329981123'
for directory in sorted(source.glob('e4-native-source-*')):
    events=lines(directory/'full-tests.log')
    terminal=[r for r in events if r.get('Test') and r['Action'] in ['pass','fail','skip']]
    top={(r['Package'],r['Test']) for r in terminal if r['Action']=='pass' and '/' not in r['Test']}
    sub={(r['Package'],r['Test']) for r in terminal if r['Action']=='pass' and '/' in r['Test']}
    scaffolding=[list(x) for x in sorted(top) if x[1]=='TestHelperProcess']
    packet['native_source'].append(dict(host=directory.name,commands=read(directory/'commands.json'),focused=read(directory/'focused/summary.json'),
        passed_top_level_events=len(top),passed_subcases=len(sub),helper_scaffolding_events=scaffolding,
        passed_top_level_behavior_tests=len(top)-len(scaffolding),skips=[r for r in terminal if r['Action']=='skip'],
        failures=[r for r in terminal if r['Action']=='fail'],test_event_log_sha256=sha(directory/'full-tests.log')))
audit=read(ROOT/'artifacts/e5-source-local/risk-audit.json')
packet['risk_mapping']=dict(mapped_rows=300,distinct_anchors=41,test_function_anchors=40,corpus_spec_anchors=1,
    observed_windows_test_anchors=sum(bool(r.get('observed_windows_events')) for r in audit['mapping_audit']),
    corpus_anchor='corpus/workflows/bottom/bottom-08.json',policy='Mappings are not distinct test executions; BT-08 actual frozen-byte result is in the corpus ledger.')
packet['corpus']=dict(summary=read(ROOT/'artifacts/e5-corpus/summary.json'),
    claims=dict(executed_good_workflows=120,supported_claim_workflows=119,excluded_diagnostic_cell='MICRO-08 wide-cell rendering is unreliable even on Windows'),
    attempts=[{k:r[k] for k in ['id','spec','phase','exit','actual_category','accepted','start_utc','end_utc','wall_ms','runner_sha256']} |
              dict(cleanup=r['result']['cleanup'],workspace=r['result'].get('workspace'),failure=r['result'].get('failure'))
              for r in lines(ROOT/'artifacts/e5-corpus/attempts.jsonl')],ledger_sha256=sha(ROOT/'artifacts/e5-corpus/attempts.jsonl'))
packet['holdouts']=[dict(label=name,summary=read(ROOT/'artifacts'/name/'summary.json'),freeze=read(ROOT/'artifacts'/name/'freeze.json'),
    attempts=[{k:r[k] for k in ['attempt_id','definition','start_utc','end_utc','whole_command_ms','exit','expected_exit','expected_category','accepted','runner_sha256']} for r in read(ROOT/'artifacts'/name/'attempts.json')])
    for name in ['e5-holdouts','e5-holdouts-exact','e5-holdouts-frozen']]
packet['holdout_independence']='Only two operator-designed historical holdout definitions; 20 final-byte executions. Preliminary/exact developmental repetitions are not independent holdouts.'
packet['compatibility']=read(ROOT/'artifacts/e5-compatibility/observations.json')
packet['browser']=dict(first='connection refused after old disposable browser exited; retained',
    accepted=read(ROOT/'artifacts/e5-compatibility/browser-r2-exit.txt')==0,log_sha256=sha(ROOT/'artifacts/e5-compatibility/browser-r2.log'),human_screen_reader='unknown; broad accessibility excluded')
packet['resources']={name:lines(ROOT/'artifacts'/name/'observations.jsonl') for name in ['e5-windows-tree','e5-windows-plain','e5-windows-supported-tree','e5-windows-supported-plain']}
packet['supported_resource_admission']=read(ROOT/'artifacts/e5-supported-serial/admission.json')
packet['native_bytes']=[read(path) for path in sorted((ROOT/'artifacts/e5-native-bytes-36330943126').rglob('observations.json'))]
packet['native_real']=[]
for path in sorted((ROOT/'artifacts/e5-native-real-36333011585').rglob('summary.json')):
    rows=lines(path.parent/'attempts.jsonl')
    packet['native_real'].append(dict(summary=read(path),attempts=rows,runtime_identities=read(path.parent/'runtime-identities.json'),ledger_sha256=sha(path.parent/'attempts.jsonl')))
frozen_walk=ROOT/'artifacts/e4-frozen-walkthroughs/attempts.json'
packet['frozen_walkthroughs']=read(frozen_walk) if frozen_walk.exists() else None
packet['qualification']=[]
for directory in sorted((ROOT/'artifacts/e5-qualification-36330814511').glob('qualification-*-100')):
    rows=lines(directory/'attempts.jsonl'); workflows=[]
    for ident in sorted({r['workflow_id'] for r in rows}):
        selected=[r for r in rows if r['workflow_id']==ident]; values=[r['total_wall_ms'] for r in selected]
        workflows.append(dict(id=ident,attempts=len(selected),median_wall_ms=statistics.median(values),min_wall_ms=min(values),max_wall_ms=max(values),
            descriptive_p95_wall_ms=statistics.quantiles(values,n=20,method='inclusive')[18] if len(values)>=100 else None,
            total_cpu_ms=sum(r.get('runner_cpu_user_ms',0)+r.get('runner_cpu_system_ms',0) for r in selected),artifact_bytes=sum(r['artifact_bytes'] for r in selected),
            failures=[r['attempt_id'] for r in selected if r['exit_code']!=0 or r['disposition']!='pass']))
    packet['qualification'].append(dict(host=directory.name,summary=read(directory/'summary.json'),workflows=workflows,
        ledger_sha256=sha(directory/'attempts.jsonl'),actual_ledger_rows=len(rows),targets_sha256=sha(directory/'qualification-targets.txt'),
        observed_runner_hashes=sorted({r['runner_sha256'] for r in rows}),
        unique_attempt_ids=len({r['attempt_id'] for r in rows}),
        unconfirmed_cleanup=[r['attempt_id'] for r in rows if r['survivor_check']!='confirmed_exited' or 'workspace_cleaned=false' in r['cleanup']] ))
packet['measurement_interpretation']='Raw target_startup_ms is first-step wait; runner_overhead_ms is outside-reported-run residual. Neither isolates startup or runner overhead. Samples are observations, not population reliability or speed guarantees.'
packet['actual_local_target_inventory']=read(ROOT/'artifacts/e5-corpus/actual-target-inventory.json')
packet['ci_runs']=read(ROOT/'artifacts/e5-ci-index/runs.json')
packet['runner_job_seconds']={}; packet['job_metadata']=[]
for path in sorted((ROOT/'artifacts/e5-ci-index').glob('jobs-*.json')):
    ident=int(path.stem.split('-')[-1]); run=next((r for r in packet['ci_runs'] if r['databaseId']==ident),{})
    seconds=0
    for job in read(path)['jobs']:
        if job['started_at'] and job['completed_at']:
            seconds+=(datetime.fromisoformat(job['completed_at'].replace('Z','+00:00'))-datetime.fromisoformat(job['started_at'].replace('Z','+00:00'))).total_seconds()
    packet['runner_job_seconds'][str(ident)]=dict(workflow=run.get('workflowName'),seconds=seconds,status=run.get('status'),conclusion=run.get('conclusion'))
    packet['job_metadata'].append(dict(path=str(path.relative_to(ROOT)),sha256=sha(path)))
packet['retained_artifact_metadata']=[]
for path in sorted((ROOT/'artifacts').glob('e*-*/digests.json')):
    if 'e5-' in str(path) or 'e4-native-' in str(path) or 'e4-public-' in str(path):
        packet['retained_artifact_metadata'].append(dict(path=str(path.relative_to(ROOT)),record=read(path)))
packet['local_checks']=dict(go_version='go1.27.0 windows/amd64; supplementary to native frozen Go 1.26.0 gates',
    status=read(ROOT/'artifacts/e5-source-local/status.json'),race_exit=read(ROOT/'artifacts/e5-source-local/race-exit.txt'),
    final_manual_exit=read(ROOT/'artifacts/e5-source-local/final-manual-exit.txt'),human_engineering_effort='unknown; wall time and queues are not focused human days')
packet['cost_totals_seconds']=dict(ordinary_ci=0,final_qualification=0,preflight=0,engineering_validation=0)
for ident,run in packet['runner_job_seconds'].items():
    group='ordinary_ci' if run['workflow']=='Terminal tests' else 'final_qualification' if ident=='36330814511' else 'preflight' if ident=='36330142857' else 'engineering_validation'
    packet['cost_totals_seconds'][group]+=run['seconds']
packet['cost_interpretation']='Actual unweighted job elapsed seconds, including setup and failed/cancelled runs. Final qualification, pilot preflight and ordinary CI are separate from engineering validation. Not billed dollars or human effort; partial running jobs contribute only after completion.'
if args.complete:
    assert len(packet['qualification'])==3
    assert sum(r['actual_ledger_rows'] for r in packet['qualification'])==3000
    assert all(r['summary']['first_attempt_failures']==0 and r['summary']['managed_cleanup_failures']==0 for r in packet['qualification'])
    identities={r['executable_sha256'] for r in packet['candidate']}
    assert all(r['actual_ledger_rows']==1000 and len(r['workflows'])==10 and
        all(w['attempts']==100 and not w['failures'] for w in r['workflows']) and
        r['summary']['runner_sha256'] in identities and r['unique_attempt_ids']==1000 and
        not r['unconfirmed_cleanup'] and r['observed_runner_hashes']==[r['summary']['runner_sha256']] for r in packet['qualification'])
    assert len(packet['native_real'])==2 and all(len(r['attempts'])==48 and
        all(a['accepted'] and a['runner_sha256']==r['summary']['runner_sha256'] and
            a['result']['cleanup']['confirmed_exited'] for a in r['attempts']) and
        r['summary']['runner_sha256'] in identities for r in packet['native_real'])
    assert all(r['accepted'] for r in packet['frozen_walkthroughs']) and len(packet['frozen_walkthroughs'])==52
    assert all(r['exit']==0 and r['cleanup_unconfirmed']==0 for name in ['e5-windows-supported-tree','e5-windows-supported-plain'] for r in packet['resources'][name])
    assert all(r['accepted'] for host in packet['native_bytes'] for r in host['attempts'])
    assert all(not host['failures'] and all(r['exit_status']==r['expected_exit_status'] for r in host['commands']) for host in packet['native_source'])
    assert all(r['accepted'] for r in packet['compatibility']['attempts']) and packet['browser']['accepted']
    packet['status']='complete within explicit support and accessibility boundaries; unpublished'
(ROOT/'docs/validation/e5-observations-2026-09-27.json').write_text(json.dumps(packet,indent=2,ensure_ascii=True)+'\n',encoding='utf-8')
print(packet['status'],len(packet['qualification']),'qualification hosts')
