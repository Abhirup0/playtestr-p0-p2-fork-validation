"""Matched before/after controls; source regression must fail before the fix."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import time

ROOT = Path(__file__).resolve().parents[2]
out = ROOT / 'artifacts/readiness-native/candidate'
out.mkdir(parents=True, exist_ok=False)
baseline = ROOT / '.trial-private/readiness-baseline-source'
subprocess.run(['git', 'worktree', 'add', '--detach', str(baseline), 'adee5bf6554ffceb3eeed78752a708a5e8e052ea'], cwd=ROOT, check=True, timeout=30)
shutil.copyfile(ROOT / 'internal/runner/pty_unix_test.go', baseline / 'internal/runner/pty_unix_test.go')
with (out / 'before-regression.log').open('wb') as log:
    regression = subprocess.run(['go', 'test', '-count=1', './internal/runner', '-run', '^TestNaturalExitReachesTerminalEOF$'], cwd=baseline, stdout=log, stderr=subprocess.STDOUT, timeout=90)
if regression.returncode == 0 or 'terminal reader did not reach EOF after natural exit' not in (out / 'before-regression.log').read_text():
    raise SystemExit('Baseline did not reproduce the intended EOF regression')
with (out / 'after-regression.log').open('wb') as log:
    subprocess.run(['go', 'test', '-count=1', './internal/runner', '-run', '^TestNaturalExitReachesTerminalEOF$'], cwd=ROOT, stdout=log, stderr=subprocess.STDOUT, check=True, timeout=90)
binaries = {}
for mode, source in [('before', baseline), ('after', ROOT)]:
    binary = out / (mode + '-playtestr')
    subprocess.run(['go', 'build', '-trimpath', '-o', str(binary), './cmd/playtestr'], cwd=source, check=True, timeout=180)
    binaries[mode] = binary
(out / 'identities.json').write_text(json.dumps({'baseline_commit': 'adee5bf6554ffceb3eeed78752a708a5e8e052ea', 'candidate_commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(), 'go': subprocess.check_output(['go', 'version'], text=True).strip(), 'binaries': {mode: hashlib.sha256(binary.read_bytes()).hexdigest() for mode, binary in binaries.items()}}, indent=2) + '\n')
rows = []
if os.environ.get('READINESS_REGRESSION_ONLY') == '1':
    raise SystemExit(0)
for sample in range(1, 31):
    for task, expected in [('c1', 'Beta'), ('c2', 'port=4242'), ('c3', None)]:
        for mode in (['before', 'after'] if sample % 2 else ['after', 'before']):
            identity = f'{task}-{sample}-{mode}'
            state = out / (identity + '-state.txt')
            env = os.environ.copy()
            env['C1_RESULT_PATH' if task == 'c1' else 'C2_CONFIG_PATH'] = str(state)
            report = out / (identity + '-report.json')
            started = time.monotonic()
            with (out / (identity + '.log')).open('wb') as log:
                result = subprocess.run([str(binaries[mode]), 'test', '--report', str(report), '--artifacts-dir', str(out / (identity + '-artifacts')), str(ROOT / f'benchmarks/competitive/{task}/playtestr.json')], cwd=ROOT, env=env, stdout=log, stderr=subprocess.STDOUT, timeout=20)
            wall = (time.monotonic() - started) * 1000
            product = json.loads(report.read_text()) if report.exists() else {'results': []}
            results = product['results']
            observed = state.read_text().strip() if state.exists() else None
            accepted = result.returncode == 0 and len(results) == 1 and results[0]['status'] == 'passed' and results[0]['cleanup']['confirmed_exited'] and observed == expected
            row = dict(task=task, sample=sample, mode=mode, wall_ms=wall, exit=result.returncode, state=observed, accepted=accepted)
            rows.append(row)
            with (out / 'observations.jsonl').open('a') as ledger:
                ledger.write(json.dumps(row) + '\n')
            print(identity, 'accepted', accepted, 'wall_ms', round(wall), flush=True)
raise SystemExit(0 if all(row['accepted'] for row in rows) else 1)
