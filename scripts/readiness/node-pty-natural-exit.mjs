// Reduced native Windows cleanup diagnostic, not an alternative benchmark.
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import { resolve } from 'node:path';
import assert from 'node:assert/strict';
const root = fileURLToPath(new URL('../../', import.meta.url));
const require = createRequire(resolve(root, '.trial-private/readiness-termless/package.json'));
const pty = require('node-pty');
const killAfterExit = process.argv.includes('--kill-after-exit');
const child = pty.spawn(resolve(root, 'bin/demo.exe'), [], {
  name: 'xterm-256color', cols: 64, rows: 16, cwd: root, env: process.env,
});
let observed = '';
let requestedExit = false;
// An exited target can still leave adapter handles alive. Preserve that as a
// diagnostic failure instead of letting this reduced experiment hang.
const finalDeadline = setTimeout(() => {
  console.error(JSON.stringify({ diagnostic: 'adapter did not terminate within 10 seconds', active_handle_types: process._getActiveHandles().map(handle => handle.constructor.name) }));
  process.exit(2);
}, 10000);
finalDeadline.unref();
const deadline = setTimeout(() => {
  console.error('bounded natural-exit deadline exceeded');
  child.kill();
  process.exitCode = 1;
}, 5000);
child.onData(data => {
  observed += data;
  if (observed.length > 65536) { child.kill(); throw new Error('bounded diagnostic output exceeded'); }
  if (!requestedExit && observed.includes('Deploy preview')) {
    requestedExit = true;
    child.write('q');
  }
});
child.onExit(({ exitCode }) => {
  clearTimeout(deadline);
  assert.equal(requestedExit, true);
  assert.equal(exitCode, 0);
  console.log(JSON.stringify({ scope: 'node-pty reduced natural-exit diagnostic', exit_code: exitCode, kill_after_exit: killAfterExit }));
  if (killAfterExit) child.kill();
});
