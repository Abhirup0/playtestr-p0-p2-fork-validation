// Local synthetic P0 probe only. No App, billing, network API or production routes.
interface Env { DB: D1Database }

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    if (new URL(request.url).pathname === "/seed") {
      await env.DB.exec("CREATE TABLE IF NOT EXISTS jobs (id TEXT PRIMARY KEY, tenant INTEGER NOT NULL, due INTEGER NOT NULL, lease INTEGER NOT NULL DEFAULT 0, attempts INTEGER NOT NULL DEFAULT 0); CREATE INDEX IF NOT EXISTS jobs_due ON jobs(due,lease); CREATE INDEX IF NOT EXISTS jobs_tenant ON jobs(tenant,id);");
      await env.DB.batch(Array.from({length: 100}, (_, i) => env.DB.prepare("INSERT OR IGNORE INTO jobs(id,tenant,due) VALUES(?,?,?)").bind(`synthetic-${i}`, i % 3, 0)));
      return Response.json({synthetic_rows:100});
    }
    const payload = JSON.stringify({version:1, results:Array.from({length:1000},(_,i)=>({id:i,status:"passed",head:"a".repeat(40),padding:"p".repeat(100)}))});
    const data = new TextEncoder().encode(payload);
    if (data.byteLength > 256*1024) throw new Error("probe payload exceeded contract");
    const key = await crypto.subtle.importKey("raw", new Uint8Array(32).fill(7), {name:"HMAC",hash:"SHA-256"},false,["sign","verify"]);
    const rsa = await crypto.subtle.generateKey({name:"RSASSA-PKCS1-v1_5",modulusLength:2048,publicExponent:new Uint8Array([1,0,1]),hash:"SHA-256"},false,["sign","verify"]);
    const start = performance.now();
    const signature = await crypto.subtle.sign("HMAC",key,data);
    const valid = await crypto.subtle.verify("HMAC",key,signature,data);
    const decoded = JSON.parse(payload);
    if (!valid || decoded.results.length!==1000) throw new Error("probe verification failed");
    const signatureParseWallMs = performance.now()-start;
    const signingStart = performance.now();
    const jwtSignature = await crypto.subtle.sign("RSASSA-PKCS1-v1_5",rsa.privateKey,new TextEncoder().encode("synthetic.jwt"));
    const rsaSignWallMs = performance.now()-signingStart;
    const queriesStart = performance.now();
    // Each claimant atomically selects and leases one job. Duplicate delivery IDs
    // insert once; expired leases are reclaimable; attempts bounded in the query.
    const claims = await Promise.all(Array.from({length:8},()=>env.DB.prepare("UPDATE jobs SET lease=?,attempts=attempts+1 WHERE id=(SELECT id FROM jobs WHERE due<=? AND lease<? AND attempts<5 ORDER BY due,id LIMIT 1) RETURNING id,attempts").bind(10000,1,1).all()));
    const ids=claims.flatMap(c=>c.results.map((r:any)=>r.id));
    if(new Set(ids).size!==ids.length) throw new Error("duplicate atomic lease");
    const rows=await env.DB.prepare("SELECT id,attempts FROM jobs WHERE tenant=? ORDER BY id LIMIT 20").bind(1).all();
    const plan=await env.DB.prepare("EXPLAIN QUERY PLAN SELECT id FROM jobs WHERE tenant=? ORDER BY id LIMIT 20").bind(1).all();
    return Response.json({local_workerd_only:true,provider_cpu_metering:false,payload_bytes:data.byteLength,signature_parse_wall_ms:signatureParseWallMs,rsa_sign_wall_ms:rsaSignWallMs,rsa_signature_bytes:jwtSignature.byteLength,d1_wall_ms:performance.now()-queriesStart,unique_claims:ids.length,tenant_rows:rows.results.length,index_plan:plan.results});
  }
};
