#!/usr/bin/env node
// render-title-card.js <text> <output.png> [width] [height]
// Renders text onto a dark background as a PNG using Puppeteer.

const puppeteer = require('puppeteer');
const path = require('path');

const args = process.argv.slice(2);
if (args.length < 2) {
  console.error('Usage: node render-title-card.js <text> <output.png> [width] [height]');
  process.exit(1);
}

const text = args[0];
const outputPath = path.resolve(args[1]);
const width = parseInt(args[2] || '1400');
const height = parseInt(args[3] || '800');

async function main() {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.setViewport({ width, height });

  // Escape HTML entities
  const escaped = text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');

  const html = `<!DOCTYPE html>
<html><head><style>
  body {
    margin: 0; padding: 40px;
    background: #1e1e2e;
    display: flex; align-items: center; justify-content: center;
    height: calc(100vh - 80px);
    font-family: 'Segoe UI', 'Consolas', monospace;
  }
  pre {
    color: #cdd6f4;
    font-size: 26px;
    line-height: 1.6;
    text-align: center;
    white-space: pre-wrap;
  }
</style></head><body><pre>${escaped}</pre></body></html>`;

  await page.setContent(html);
  await page.screenshot({ path: outputPath });
  await browser.close();
}

main().catch(err => { console.error(err); process.exit(1); });
