// Desktop CPU probe complements workerd local wall timings, not provider metering.
import { webcrypto as crypto } from 'node:crypto';
import { performance } from 'node:perf_hooks';
const payload=JSON.stringify({version:1,results:Array.from({length:1000},(_,id)=>({id,status:'passed',head:'a'.repeat(40),padding:'p'.repeat(100)}))});
const data=new TextEncoder().encode(payload);
const key=await crypto.subtle.importKey('raw',new Uint8Array(32).fill(7),{name:'HMAC',hash:'SHA-256'},false,['sign','verify']);
const rsa=await crypto.subtle.generateKey({name:'RSASSA-PKCS1-v1_5',modulusLength:2048,publicExponent:new Uint8Array([1,0,1]),hash:'SHA-256'},false,['sign','verify']);
const measurements=[];
for(let i=0;i<100;i++){
  const cpu=process.cpuUsage(),start=performance.now();
  const sig=await crypto.subtle.sign('HMAC',key,data);
  if(!await crypto.subtle.verify('HMAC',key,sig,data))throw new Error('signature');
  const parsed=JSON.parse(payload);if(parsed.results.length!==1000)throw new Error('parser');
  await crypto.subtle.sign('RSASSA-PKCS1-v1_5',rsa.privateKey,new TextEncoder().encode('synthetic.jwt'));
  const used=process.cpuUsage(cpu);
  measurements.push({cpu_ms:(used.user+used.system)/1000,wall_ms:performance.now()-start});
}
const sorted=measurements.map(m=>m.cpu_ms).sort((a,b)=>a-b);
console.log(JSON.stringify({desktop_only:true,provider_cpu_metering:false,payload_bytes:data.byteLength,iterations:100,cpu_p50_ms:sorted[49],cpu_p95_ms:sorted[94],cpu_max_ms:sorted.at(-1),rss_bytes:process.memoryUsage().rss,measurements},null,2));
