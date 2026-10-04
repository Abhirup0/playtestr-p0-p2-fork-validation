import {test, expect} from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';
import {readdirSync, mkdirSync} from 'node:fs';
import {resolve, relative} from 'node:path';
const root = resolve('../..', process.env.WEB_ROOT || 'artifacts/website-redesign-preview');
const walk = dir => readdirSync(dir,{withFileTypes:true}).flatMap(x=>x.isDirectory()?walk(resolve(dir,x.name)):[resolve(dir,x.name)]);
const routes = walk(root).filter(x=>x.endsWith('.html')&&!x.endsWith('404.html')).map(x=>relative(root,x).replaceAll('\\','/').replace(/index\.html$/,''));
const examples = ['', 'download/', 'docs/', 'docs/spec-v2/', 'releases/v0.4.0-rc.3/', 'examples/', 'docs/prerelease-installation/'];
test('every built route has a title, one main heading and no missing first-party assets',async({page,baseURL})=>{
  const errors=[]; page.on('pageerror',e=>errors.push(e.message));
  page.on('response',r=>{if(r.url().startsWith(baseURL)&&r.status()>=400) errors.push(r.url());});
  for(const route of routes){const response=await page.goto(route); expect(response.status()).toBe(200); await expect(page.locator('h1')).toHaveCount(1); await expect(page.locator('main')).toHaveCount(1); expect(await page.title()).toContain('Playtestr');}
  expect(errors).toEqual([]);
});
test('responsive layouts and representative screenshots',async({page},info)=>{
  mkdirSync(resolve('../../artifacts/website-screenshots'),{recursive:true});
  for(const width of [320,375,390,768,1024,1440]){
    await page.setViewportSize({width,height:900});
    for(const route of examples){await page.goto(route); expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),`${route} at ${width}px`).toBe(true);
      if(info.project.name==='chromium'&&[390,1440].includes(width)) await page.screenshot({path:resolve(`../../artifacts/website-screenshots/${route.replaceAll('/','-')||'home'}-${width}.png`),fullPage:true});
    }
  }
});
test('representative templates pass WCAG 2.2 AA automated checks',async({page})=>{
  for(const route of examples){await page.goto(route);const result=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa','wcag22aa']).analyze();expect(result.violations.map(x=>({id:x.id,nodes:x.nodes.map(n=>n.target)})),route).toEqual([]);}
});
test('mobile menu keyboard disclosure and no-script access',async({page,browser,baseURL})=>{
  await page.setViewportSize({width:375,height:812}); await page.goto('');
  const toggle=page.getByRole('button',{name:'Menu',exact:true}); await toggle.focus();await page.keyboard.press('Enter');await expect(toggle).toHaveAttribute('aria-expanded','true');await expect(page.locator('#site-nav a').first()).toBeFocused();await page.keyboard.press('Escape');await expect(toggle).toBeFocused();await expect(toggle).toHaveAttribute('aria-expanded','false');
  const context=await browser.newContext({javaScriptEnabled:false,viewport:{width:320,height:812}});
  try{const plain=await context.newPage();await plain.goto(baseURL);await expect(plain.locator('#site-nav').getByRole('link',{name:'Docs',exact:true})).toBeVisible();await plain.goto(new URL('docs/ci-installation/',baseURL).href);await expect(plain.locator('.page-toc')).toBeVisible();await plain.goto(new URL('examples/',baseURL).href);await expect(plain.locator('[data-demo-screen]')).toContainText('mission control');await expect(plain.locator('.noscript-note')).toBeVisible();}finally{await context.close();}
});
test('search handles results, empty queries, no results and unavailable index',async({page})=>{
  await page.goto('docs/'); const input=page.locator('#docs-search'); await input.fill('expect_not');await page.getByRole('button',{name:'Search',exact:true}).click();await expect(page.locator('.search-results li').first()).toBeVisible();await page.getByRole('button',{name:'Clear',exact:true}).click();await expect(input).toBeFocused();await input.fill('<nonexistent-xyz>');await page.getByRole('button',{name:'Search',exact:true}).click();await expect(page.locator('[data-search-status]')).toContainText('No documentation');await input.fill('a');await page.getByRole('button',{name:'Search',exact:true}).click();await expect(page.locator('[data-search-status]')).toContainText('at least two');
  await page.reload();await page.route('**/index.json',route=>route.abort());await input.fill('snapshots');await page.getByRole('button',{name:'Search',exact:true}).click();await expect(page.locator('[data-search-status]')).toContainText('unavailable');
});
test('channels, exact checksums and pinned CI instructions',async({page})=>{
  await page.goto('download/');await expect(page.locator('#prerelease-title')).toHaveText('v0.4.0-rc.3');await expect(page.locator('#stable-title')).toHaveText('v0.1.0');await expect(page.locator('a[href*="/download/v0.4.0-rc.3/"]')).toHaveCount(6);await expect(page.locator('a[href*="/download/v0.1.0/"]')).toHaveCount(6);await page.goto('docs/ci-installation/');await expect(page.locator('main')).toContainText('ae97c62022966cde9699b26169b4dc6ef0a12439');await expect(page.locator('main')).toContainText('PLAYTESTR_VERSION: v0.4.0-rc.3');
});
test('demo sensitivity, reduced motion and copy feedback',async({page})=>{
  await page.emulateMedia({reducedMotion:'reduce'}); await page.goto('');await expect(page.locator('[data-demo-provenance]')).not.toContainText('loading');await page.locator('[data-scenario="failure"]').click();await page.locator('[data-demo-action="play"]').click();await expect(page.locator('[data-evidence-panel]')).toBeVisible();await page.locator('[data-evidence="diff"]').click();await expect(page.locator('[data-evidence-output]')).toContainText('Preview deployed successfully.');await page.goto('docs/ci-installation/');await page.getByRole('button',{name:'Copy code'}).first().click();await expect(page.locator('pre [role="status"]').first()).toContainText(/Code copied|Copy unavailable/);
});
test('missing routes are genuine 404s',async({page})=>{const response=await page.goto('does-not-exist-website-check/');expect(response.status()).toBe(404);await expect(page.getByRole('heading',{level:1})).toContainText("isn't here");});

test('skip navigation transfers keyboard focus into the content',async({page})=>{
  for(const width of [375,1440]) for(const route of ['', 'docs/']) {
    await page.setViewportSize({width,height:900});await page.goto(route);
    await page.keyboard.press('Tab');await expect(page.getByRole('link',{name:'Skip to content'})).toBeFocused();
    await page.keyboard.press('Enter');await expect(page.locator('main')).toBeFocused();
  }
});
