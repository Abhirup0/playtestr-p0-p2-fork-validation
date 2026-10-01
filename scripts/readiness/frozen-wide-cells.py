"""Independent ANSI/column expectations exercised through a frozen runner's real PTY."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

# Explicit expected strings are column-counted, never obtained from the renderer.
CASES = [
    ('advance', '雪X\x1b[1;4HZ', '雪XZ', 8),
    ('address', '雪 X\x1b[1;4HZ', '雪 Z', 8),
    ('overwrite-head', '雪X\x1b[1;1HZ', 'Z X', 8),
    ('overwrite-tail', '雪X\x1b[1;2HZ', ' ZX', 8),
    ('erase-tail', '雪X\x1b[1;2H\x1b[K', '', 8),
    ('wrap-before', 'abc雪X', 'abc\n雪X', 4),
    ('wrap-after', 'ab雪X', 'ab雪\nX', 4),
    ('fullwidth', 'ＡX\x1b[1;4HZ', 'ＡXZ', 8),
    ('insert-before', '雪XY\x1b[1;1H\x1b[@', ' 雪XY', 8),
    ('insert-tail', '雪XY\x1b[1;2H\x1b[@', '   XY', 8),
    ('delete-half', '雪XY\x1b[1;1H\x1b[P', ' XY', 8),
    ('delete-pair', '雪XY\x1b[1;1H\x1b[2P', 'XY', 8),
    ('leading-spaces', '  雪X', '  雪X', 8),
    ('nowrap-clip', 'abc\x1b[?7l雪', 'abc', 4),
    ('split-utf8', '雪 X\x1b[1;4HZ', '雪 Z', 8),
    ('alternate', '雪X\x1b[?1049hＡY\x1b[?1049l', '雪X', 8),
    ('resize-main', 'abc雪X', 'abc', 8),
    ('resize-alternate', '\x1b[?1049habc雪X', 'abc', 8),
]

if len(sys.argv) == 3 and sys.argv[1] == '--target':
    if os.name == 'nt':
        import ctypes
        assert ctypes.windll.kernel32.SetConsoleOutputCP(65001)
        assert ctypes.windll.kernel32.SetConsoleCP(65001)
    name, sequence, _, _ = next(c for c in CASES if c[0] == sys.argv[2])
    # Reset the shell's inherited cursor and clear both visible state and scroll position.
    data = ('\x1b[2J\x1b[H' + sequence).encode('utf-8')
    if name == 'split-utf8':
        for byte in data:
            os.write(1, bytes([byte]))
            time.sleep(.015)
    else:
        os.write(1, data)
    if name.startswith('resize-'):
        sys.stdin.readline()
        # Input echo after resize is cleared; the target deliberately preserves row one.
        os.write(1, b'\x1b[2;1H\x1b[J')
    time.sleep(.2)
    raise SystemExit(0)

p = argparse.ArgumentParser()
p.add_argument('--runner', required=True)
p.add_argument('--out', required=True)
a = p.parse_args()
runner = Path(a.runner).resolve()
out = Path(a.out).resolve()
out.mkdir(parents=True, exist_ok=False)
(out / 'snapshots').mkdir()
digest = hashlib.sha256(runner.read_bytes()).hexdigest()
rows = []
for name, sequence, expected, width in CASES:
    baseline = out / 'snapshots' / (name + '.txt')
    baseline.write_text(expected + '\n', encoding='utf-8')
    steps = []
    if name.startswith('resize-'):
        steps = [dict(expect='abc雪X'), dict(resize=dict(width=4, height=3)),
                 dict(key='Enter')]
    steps += [dict(exit=0), dict(snapshot=baseline.name)]
    spec = out / (name + '.json')
    spec.write_text(json.dumps(dict(version=1, command=[sys.executable, '-u', str(Path(__file__).resolve()), '--target', name],
                                   width=width, height=3, timeout_ms=3000, run_timeout_ms=10000, steps=steps)))
    report = out / (name + '-result.json')
    started = time.monotonic()
    with (out / (name + '.log')).open('wb') as log:
        result = subprocess.run([str(runner), 'test', '--report', str(report), '--artifacts-dir', str(out / (name + '-evidence')), str(spec)],
                                stdout=log, stderr=subprocess.STDOUT, timeout=15)
    captured = json.loads(report.read_text())['results'][0]
    accepted = result.returncode == 0 and captured['cleanup']['confirmed_exited']
    rows.append(dict(id=name, expected_screen=expected, ansi_utf8_hex=sequence.encode('utf-8').hex(),
                     runner_sha256=digest, exit=result.returncode, accepted=accepted, result=captured,
                     wall_ms=(time.monotonic()-started)*1000))
    (out / 'attempts.json').write_text(json.dumps(rows, indent=2) + '\n')
    print(name, accepted, flush=True)
(out / 'summary.json').write_text(json.dumps(dict(attempts=len(rows), accepted=sum(r['accepted'] for r in rows),
                                                 runner_sha256=digest), indent=2) + '\n')
raise SystemExit(0 if all(r['accepted'] for r in rows) else 1)
