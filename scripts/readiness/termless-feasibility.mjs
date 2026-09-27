// Real-PTY feasibility only: this is neither a benchmark nor a support matrix.
import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { createHash } from 'node:crypto';
import assert from 'node:assert/strict';
const root = fileURLToPath(new URL('../../', import.meta.url));
const packages = resolve(root, '.trial-private/readiness-termless');
const output = resolve(root, process.argv[2] ?? 'artifacts/readiness-2026-09-26/termless-first.json');
if (existsSync(output)) throw new Error('Use a fresh evidence filename');
const hash = (path) => createHash('sha256').update(readFileSync(path)).digest('hex');
const result = {
  host: `${process.platform}_${process.arch}`, node: process.version,
  core: '0.9.1', xtermjs: '0.9.1', node_pty: '1.1.0',
  package_lock_sha256: hash(resolve(packages, 'package-lock.json')),
  target_sha256: hash(resolve(root, 'bin/demo.exe')),
  scope: 'real interactive menu, rendered readiness, input, natural exit; no process-tree coverage or speed ranking',
};
let term;
const start = performance.now();
try {
  const { createTerminal } = await import(pathToFileURL(resolve(packages, 'node_modules/@termless/core/dist/index.mjs')));
  const { createXtermBackend } = await import(pathToFileURL(resolve(packages, 'node_modules/@termless/xtermjs/dist/index.mjs')));
  term = createTerminal({ backend: createXtermBackend(), cols: 64, rows: 16 });
  await term.spawn([resolve(root, 'bin/demo.exe')], { cwd: root });
  await term.waitFor('> Deploy preview', 3000);
  term.press('ArrowDown');
  await term.waitFor('> Run diagnostics', 3000);
  term.press('Enter');
  await term.waitFor('Diagnostics: all systems healthy.', 3000);
  result.screen = term.screen.getText();
  term.type('q');
  const deadline = performance.now() + 3000;
  while (term.alive && performance.now() < deadline) await new Promise(r => setTimeout(r, 10));
  assert.equal(term.alive, false, 'target must exit within budget');
  assert.equal(term.exitInfo, 'exit=0');
  result.exit_info = term.exitInfo;
  result.status = 'task_passed_cleanup_unverified';
} catch (error) {
  result.status = 'failed';
  result.error = String(error);
  process.exitCode = 1;
} finally {
  if (term) await term.close();
  result.whole_attempt_ms = performance.now() - start;
  mkdirSync(dirname(output), { recursive: true });
  writeFileSync(output, JSON.stringify(result, null, 2) + '\n');
  console.log(JSON.stringify(result));
}
