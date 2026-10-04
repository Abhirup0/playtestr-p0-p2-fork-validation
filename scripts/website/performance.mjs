import lighthouse from 'lighthouse';
import {chromium} from '@playwright/test';
import {spawn} from 'node:child_process';
import {mkdirSync, writeFileSync} from 'node:fs';
import {resolve} from 'node:path';
const base = process.env.SITE_URL || 'http://127.0.0.1:4173/playtestr/';
const out = resolve(process.env.PERFORMANCE_OUT || '../../artifacts/website-performance'); mkdirSync(out,{recursive:true});
const local = process.env.SITE_URL ? undefined : spawn(process.execPath,['scripts/website/serve.mjs'],{cwd:resolve('../..'),stdio:'ignore'});
const port = 9245;
const browser = await chromium.launch({headless:true,args:[`--remote-debugging-port=${port}`]});
const results=[];
try {
  for(let i=0;i<40;i++){try{if((await fetch(base)).ok)break;}catch{}await new Promise(r=>setTimeout(r,100));}
  for(const route of ['', 'docs/ci-installation/']) for(let attempt=1;attempt<=3;attempt++) {
    const result=await lighthouse(new URL(route,base).href,{port,output:'json',onlyCategories:['performance','accessibility','best-practices','seo'],logLevel:'error',maxWaitForLoad:20000});
    const report=result.lhr;const label=route?'docs':'home';
    writeFileSync(resolve(out,`${label}-${attempt}.json`),result.report);
    results.push({page:label,attempt,performance:report.categories.performance.score*100,accessibility:report.categories.accessibility.score*100,seo:report.categories.seo.score*100,lcp_ms:report.audits['largest-contentful-paint'].numericValue,cls:report.audits['cumulative-layout-shift'].numericValue,total_bytes:report.audits['total-byte-weight'].numericValue,tool:report.lighthouseVersion,scope:'Mobile Lighthouse lab, simulated throttling; not field INP or p75'});
  }
  writeFileSync(resolve(out,'summary.json'),JSON.stringify(results,null,2));console.log(JSON.stringify(results,null,2));
  for(const page of ['home','docs']) {const runs=results.filter(x=>x.page===page);const median=runs.map(x=>x.performance).sort((a,b)=>a-b)[1];if(median<95||runs.some(x=>x.lcp_ms>2500||x.cls>0.1))throw new Error(`${page} exceeds the mobile lab performance budget`);}
} finally {await browser.close();if(local){local.kill();await new Promise(r=>{if(local.exitCode!==null)r();else{local.once('exit',r);setTimeout(r,3000);}});}}
