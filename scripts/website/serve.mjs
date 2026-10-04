import {createServer} from 'node:http';
import {readFileSync, statSync} from 'node:fs';
import {resolve, extname, sep} from 'node:path';
import {gzipSync} from 'node:zlib';
const root = resolve(process.env.WEB_ROOT || 'artifacts/website-redesign-preview');
const types = {'.html':'text/html; charset=utf-8','.css':'text/css','.js':'text/javascript','.json':'application/json','.xml':'application/xml','.svg':'image/svg+xml','.png':'image/png','.txt':'text/plain'};
const server = createServer((request, response) => {
  try {
    const url = new URL(request.url, 'http://localhost');
    if (!url.pathname.startsWith('/playtestr/')) throw new Error('not a project route');
    const path = resolve(root, decodeURIComponent(url.pathname.slice('/playtestr/'.length)));
    if (path !== root && !path.startsWith(root + sep)) throw new Error('unsafe path');
    const file = statSync(path).isDirectory() ? resolve(path, 'index.html') : path;
    if (statSync(file).size > 4 * 1024 * 1024) throw new Error('oversized file');
    let body = readFileSync(file);
    response.setHeader('Content-Type', types[extname(file)] || 'application/octet-stream');
    response.setHeader('Cache-Control', 'no-store');
    if (/gzip/.test(request.headers['accept-encoding'] || '') && !['.png'].includes(extname(file))) {
      body = gzipSync(body); response.setHeader('Content-Encoding','gzip');
    }
    response.setHeader('Content-Length',body.length);
    response.end(body);
  } catch {
    response.writeHead(404, {'Content-Type':'text/html; charset=utf-8'});
    response.end(readFileSync(resolve(root,'404.html')));
  }
});
server.listen(Number(process.env.PORT || 4173), '127.0.0.1');
for (const signal of ['SIGINT','SIGTERM']) process.on(signal, () => server.close(() => process.exit(0)));
