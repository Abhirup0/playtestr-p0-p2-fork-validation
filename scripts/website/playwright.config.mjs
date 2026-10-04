import {defineConfig, devices} from '@playwright/test';
const site = process.env.SITE_URL || 'http://127.0.0.1:4173/playtestr/';
export default defineConfig({
  testDir: '.', testMatch: 'site.spec.mjs', timeout: 90000, expect: {timeout:10000},
  retries: 0, workers: 2, fullyParallel: true,
  outputDir: '../../artifacts/website-browser-results',
  reporter: [['list'], ['json', {outputFile:'../../artifacts/website-browser-results.json'}]],
  use: {baseURL:site, trace:'retain-on-failure', screenshot:'only-on-failure'},
  projects: [
    {name:'chromium',use:{...devices['Desktop Chrome']}},
    {name:'firefox',use:{...devices['Desktop Firefox']}},
    {name:'webkit',use:{...devices['Desktop Safari']}}
  ],
  webServer: process.env.SITE_URL ? undefined : {
    command:'node scripts/website/serve.mjs', cwd:'../..',
    url:site, timeout:15000, reuseExistingServer:!process.env.CI
  }
});
