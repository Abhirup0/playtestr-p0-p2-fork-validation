"""Retain compact, reproducible CI observations without binaries or secrets."""
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
p = argparse.ArgumentParser()
p.add_argument('--runs', nargs='+', type=int, required=True)
p.add_argument('--output', required=True)
a = p.parse_args()

def read(path):
    if path.stat().st_size > 32 * 1024 * 1024:
        raise SystemExit('Evidence input exceeds 32 MiB bound: ' + str(path))
    raw = path.read_bytes()
    return raw.decode('utf-8-sig'), hashlib.sha256(raw).hexdigest()

records = []
for run in a.runs:
    folder = ROOT / f'artifacts/readiness-ci-{run}'
    for path in sorted(folder.rglob('*.jsonl')):
        text, digest = read(path)
        rows = [json.loads(line) for line in text.splitlines()]
        for row in rows:
            if path.parent.name == 'comparison' and row.get('tool') in {'baseline', 'playtestr'} and row.get('phase') == 'measurement':
                report = path.parent / (row['identity'] + '-report.json')
                if report.exists():
                    report_text, report_digest = read(report)
                    product = json.loads(report_text)['results'][0]
                    row['first_positive_assertion_duration_ms'] = product['steps'][0]['duration_ms']
                    row['report_sha256'] = report_digest
            if isinstance(row.get('result'), dict) and 'steps' in row['result']:
                steps = row['result'].pop('steps')
                row['result']['step_count'] = len(steps)
                row['result']['failed_steps'] = [step for step in steps if step.get('status') != 'passed']
            if 'resource_samples' in row:
                samples = row.pop('resource_samples')
                row['resource_sample_count'] = len(samples)
                row['rss_ten_time_interval_maxima'] = []
                for index in range(10):
                    values = [x['rss_bytes'] for x in samples if index * row['wall_ms'] / 10 <= x['elapsed_ms'] < (index + 1) * row['wall_ms'] / 10]
                    row['rss_ten_time_interval_maxima'].append(max(values) if values else None)
        records.append(dict(run=run, file=path.relative_to(folder).as_posix(), sha256=digest, rows=rows))
    for path in sorted(folder.rglob('*.json')):
        if path.name not in {'summary.json', 'acquisition.json', 'identities.json', 'adapter-pins.json', 'setup-operations.json', 'target-pins.json'}:
            continue
        text, digest = read(path)
        value = json.loads(text)
        if path.name == 'target-pins.json':
            # Full manifest remains in native artifacts. Retain executable and
            # target package identities here; its digest covers all other inputs.
            selected = [x for x in value if x['path'].startswith('.trial-private/corpus-tools/') and '/' not in x['path'][len('.trial-private/corpus-tools/'):]]
            value = {'input_count': len(value), 'top_level_tools': selected}
        records.append(dict(run=run, file=path.relative_to(folder).as_posix(), sha256=digest, value=value))
    for path in sorted(folder.rglob('*-regression.log')):
        text, digest = read(path)
        records.append(dict(run=run, file=path.relative_to(folder).as_posix(), sha256=digest, text=text))
    for path in sorted(folder.rglob('versions.txt')):
        text, digest = read(path)
        records.append(dict(run=run, file=path.relative_to(folder).as_posix(), sha256=digest, text=text))
    for path in sorted(folder.glob('*/profile/*-instrumented.log')):
        text, digest = read(path)
        phases = [{'phase': label, 'nested_ms': float(value)} for label, value in re.findall(r'READINESS_PHASE (\w+) ([0-9.]+)', text)]
        records.append(dict(run=run, file=path.relative_to(folder).as_posix(), sha256=digest, phases=phases))
result = dict(schema_version=1, scope='original attempt records; changed harness revisions stay separate; resource traces reduced to ten equal-time maxima with original-file digest', runs=a.runs, records=records)
(ROOT / a.output).write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('Retained', len(records), 'evidence files;', (ROOT / a.output).stat().st_size, 'bytes')
