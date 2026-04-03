#!/usr/bin/env node
// svg-to-mp4.js <input.svg> <output-dir> [fps] [duration_s]
// Renders an animated SVG to PNG frames using Puppeteer,
// then FFmpeg stitches them into mp4.

const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');
const { execSync } = require('child_process');

const args = process.argv.slice(2);
if (args.length < 2) {
  console.error('Usage: node svg-to-mp4.js <input.svg> <output-dir> [fps] [duration_s]');
  process.exit(1);
}

const svgPath = path.resolve(args[0]);
const outputDir = path.resolve(args[1]);
const fps = parseInt(args[2] || '10');
const durationS = parseFloat(args[3] || '0');

// Find ffmpeg
const ffmpegPaths = [
  'ffmpeg',
  'C:/Users/giodl/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-8.1-full_build/bin/ffmpeg.exe'
];
let ffmpeg = ffmpegPaths.find(p => {
  try { execSync(`"${p}" -version`, { stdio: 'ignore' }); return true; } catch { return false; }
});
if (!ffmpeg) { console.error('FFmpeg not found'); process.exit(1); }

async function main() {
  fs.mkdirSync(path.join(outputDir, 'frames'), { recursive: true });

  const svgContent = fs.readFileSync(svgPath, 'utf8');

  // Extract duration from SVG animation
  const durMatch = svgContent.match(/dur="([\d.]+)s"/);
  const svgDuration = durMatch ? parseFloat(durMatch[1]) : 10;
  const totalDuration = durationS > 0 ? durationS : svgDuration;
  const totalFrames = Math.ceil(totalDuration * fps);

  console.log(`SVG duration: ${svgDuration}s, rendering ${totalFrames} frames at ${fps}fps`);

  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.setViewport({ width: 1400, height: 800 });

  // Load SVG in a simple HTML page
  const html = `<!DOCTYPE html>
<html><head><style>
  body { margin: 0; padding: 0; background: #1e1e2e; display: flex; align-items: center; justify-content: center; height: 100vh; }
  svg { max-width: 100%; max-height: 100%; }
</style></head><body>${svgContent}</body></html>`;

  await page.setContent(html, { waitUntil: 'networkidle0' });

  // Capture frames
  const frameInterval = 1000 / fps;
  for (let i = 0; i < totalFrames; i++) {
    const framePath = path.join(outputDir, 'frames', `frame-${String(i).padStart(5, '0')}.png`);
    await page.screenshot({ path: framePath });

    // Advance SVG animation by manipulating time
    await page.evaluate((ms) => {
      document.querySelectorAll('animate, animateTransform, set').forEach(el => {
        if (el.parentElement && el.parentElement.style) {
          // SVG CSS animations - advance via Web Animations API if available
        }
      });
    }, i * frameInterval);

    await new Promise(r => setTimeout(r, frameInterval));

    if ((i + 1) % 10 === 0) {
      process.stdout.write(`\r  Frames: ${i + 1}/${totalFrames}`);
    }
  }
  console.log(`\r  Frames: ${totalFrames}/${totalFrames} - done`);

  await browser.close();

  // FFmpeg: frames -> mp4
  const framesPattern = path.join(outputDir, 'frames', 'frame-%05d.png');
  const outputMp4 = path.join(outputDir, 'output.mp4');

  const cmd = `"${ffmpeg}" -y -framerate ${fps} -i "${framesPattern}" -c:v libx264 -pix_fmt yuv420p -r 30 "${outputMp4}"`;
  console.log('  Encoding mp4...');
  execSync(cmd, { stdio: 'inherit' });

  console.log(`\nOutput: ${outputMp4}`);
}

main().catch(err => { console.error(err); process.exit(1); });
