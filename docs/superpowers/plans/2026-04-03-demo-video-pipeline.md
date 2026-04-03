# Demo Video Pipeline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an automated pipeline that renders professional demo videos from three text inputs (scenario file, narration script, title card text) with one shell command.

**Architecture:** A bash orchestrator (`render-demo.sh`) coordinates four stages: (1) terminal-demo renders a scenario to .cast, (2) svg-term converts .cast to animated SVG, (3) Puppeteer + FFmpeg renders SVG to terminal mp4, (4) FFmpeg composites terminal video + ElevenLabs narration audio + subtitles + title cards into a final mp4 and a 30-second clip. Narration duration is the master clock.

**Tech Stack:** terminal-demo + svg-term-cli + Puppeteer (terminal rendering), FFmpeg (compositing), ElevenLabs API (TTS), bash + jq (orchestration)

**Spec:** `docs/superpowers/specs/2026-04-03-demo-video-pipeline-design.md`

**Verified on:** Windows 11 Enterprise 10.0.26100, Node.js v24.14.0, FFmpeg 8.1. No WSL2 or Docker required.

**What already exists (from prototype session):**
- `demos/lib/svg-to-mp4.js` -- Puppeteer SVG renderer (working)
- `demos/lib/package.json` -- Puppeteer dependency (installed)
- `demos/tapes/test-scenario.txt` -- test scenario (verified)
- `demos/.gitignore` -- ignores raw/, audio/, final/, node_modules
- Tools installed: terminal-demo, svg-term-cli, FFmpeg 8.1

---

## File Structure

```
demos/
  render-demo.sh              # Main orchestrator (Task 5)
  lib/
    svg-to-mp4.js              # Puppeteer SVG renderer (EXISTS)
    cast-to-mp4.sh             # .cast -> SVG -> mp4 wrapper (Task 1)
    parse-narration.sh         # Markdown -> section JSON (Task 2)
    generate-audio.sh          # ElevenLabs TTS per section (Task 3)
    generate-srt.sh            # Subtitle generation (Task 2)
    generate-title-card.sh     # Title card video generation (Task 2)
    composite-video.sh         # FFmpeg final assembly (Task 4)
    extract-clip.sh            # 30-second clip extraction (Task 4)
    package.json               # Node deps - Puppeteer (EXISTS)
  config.env.example           # Template for API keys (Task 1)
  scenarios/
    demo-0-install.txt         # Demo 0 scenario (Task 6)
    demo-3-persona.txt         # Demo 3 scenario (Task 7)
  narration/
    demo-0-install.md          # Demo 0 narration (Task 6)
    demo-3-persona.md          # Demo 3 narration (Task 7)
  titles/
    endorsement.txt            # Endorsement card (Task 6)
    demo-0-install-opening.txt # "You got a link..." (Task 6)
    demo-3-persona-opening.txt # "You wrote a spec..." (Task 7)
    demo-3-persona-prev.txt    # "Previously gathered" (Task 7)
  raw/                         # Intermediate files (git-ignored)
  audio/                       # Generated voiceover (git-ignored)
  final/                       # Finished mp4s and clips (git-ignored)
```

---

## Task 1: Scaffold and Cast-to-MP4 Wrapper

Build the shell wrapper around the existing svg-to-mp4.js prototype. Create config template.

**Files:**
- Create: `demos/config.env.example`
- Create: `demos/lib/cast-to-mp4.sh`
- Modify: `demos/lib/svg-to-mp4.js` (improve frame timing)

- [ ] **Step 1: Create directory structure**

```bash
cd /c/src/signals
mkdir -p demos/{scenarios,narration,titles,raw,audio,final}
```

- [ ] **Step 2: Create config.env.example**

Create `demos/config.env.example`:
```bash
# Demo Video Pipeline Configuration
# Copy to config.env and fill in values

# ElevenLabs TTS
ELEVENLABS_API_KEY="your-key-here"
ELEVENLABS_VOICE_ID="pNInz6obpgDQGcFmaJgB"  # "Adam" - professional male
ELEVENLABS_MODEL_ID="eleven_monolingual_v1"

# Video settings
VIDEO_WIDTH=1400
VIDEO_HEIGHT=800
VIDEO_FPS=10
VIDEO_THEME="Catppuccin Mocha"

# Tool paths (auto-detected if blank)
FFMPEG_BIN=""
```

- [ ] **Step 3: Create cast-to-mp4.sh wrapper**

This wraps the three-step conversion: scenario.txt -> .cast -> .svg -> .mp4

Create `demos/lib/cast-to-mp4.sh`:
```bash
#!/usr/bin/env bash
# cast-to-mp4.sh <scenario.txt> <output.mp4> [speed]
# Converts a terminal-demo scenario to mp4 via .cast -> .svg -> Puppeteer+FFmpeg
#
# Requires: terminal-demo, svg-term, node, ffmpeg

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DEMO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

SCENARIO="$1"
OUTPUT="$2"
SPEED="${3:-1}"

# Load config for video settings
CONFIG="$DEMO_DIR/config.env"
if [[ -f "$CONFIG" ]]; then source "$CONFIG"; fi
FPS="${VIDEO_FPS:-10}"

# Temp working directory
WORK=$(mktemp -d)
trap "rm -rf $WORK" EXIT

SCENARIO_NAME=$(basename "$SCENARIO" .txt)

echo "  [cast-to-mp4] Scenario: $SCENARIO"

# Step 1: scenario -> .cast
echo "  [1/3] Recording scenario to .cast..."
echo "" | terminal-demo play "$SCENARIO" \
  --record "$WORK/${SCENARIO_NAME}.cast" \
  --speed "$SPEED" \
  2>/dev/null

# Step 2: .cast -> .svg
echo "  [2/3] Converting .cast to animated SVG..."
cat "$WORK/${SCENARIO_NAME}.cast" | svg-term \
  --out "$WORK/${SCENARIO_NAME}.svg" \
  --window \
  2>/dev/null

# Step 3: .svg -> .mp4 via Puppeteer + FFmpeg
echo "  [3/3] Rendering SVG to mp4..."
node "$SCRIPT_DIR/svg-to-mp4.js" \
  "$WORK/${SCENARIO_NAME}.svg" \
  "$WORK/video" \
  "$FPS" \
  2>/dev/null

# Move final output
cp "$WORK/video/output.mp4" "$OUTPUT"

DURATION=$(ffprobe -v quiet -show_entries format=duration -of csv=p=0 "$OUTPUT" 2>/dev/null || echo "unknown")
SIZE=$(du -h "$OUTPUT" | cut -f1)
echo "  [cast-to-mp4] Done: ${DURATION}s, ${SIZE}"
```

- [ ] **Step 4: Improve svg-to-mp4.js frame timing**

The prototype captures frames in real-time (waits between frames). For a curated scenario where we control timing, we should capture all frames as fast as possible using CSS animation scrubbing. Update `demos/lib/svg-to-mp4.js`:

```javascript
#!/usr/bin/env node
// svg-to-mp4.js <input.svg> <output-dir> [fps]
// Renders an animated SVG to PNG frames, then FFmpeg encodes to mp4.

const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');
const { execSync } = require('child_process');

const args = process.argv.slice(2);
if (args.length < 2) {
  console.error('Usage: node svg-to-mp4.js <input.svg> <output-dir> [fps]');
  process.exit(1);
}

const svgPath = path.resolve(args[0]);
const outputDir = path.resolve(args[1]);
const fps = parseInt(args[2] || '10');

// Find ffmpeg
const ffmpegPaths = [
  'ffmpeg',
  path.join(process.env.LOCALAPPDATA || '', 'Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-8.1-full_build/bin/ffmpeg.exe')
];
let ffmpeg = ffmpegPaths.find(p => {
  try { execSync(`"${p}" -version`, { stdio: 'ignore' }); return true; } catch { return false; }
});
if (!ffmpeg) { console.error('FFmpeg not found'); process.exit(1); }

async function main() {
  const framesDir = path.join(outputDir, 'frames');
  fs.mkdirSync(framesDir, { recursive: true });

  const svgContent = fs.readFileSync(svgPath, 'utf8');

  // Extract total animation duration from SVG
  const durMatches = [...svgContent.matchAll(/dur="([\d.]+)s"/g)];
  const maxDur = durMatches.reduce((max, m) => Math.max(max, parseFloat(m[1])), 10);
  const totalFrames = Math.ceil(maxDur * fps);

  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.setViewport({ width: 1400, height: 800 });

  const html = `<!DOCTYPE html>
<html><head><style>
  body { margin: 0; padding: 0; background: #1e1e2e; overflow: hidden; }
  svg { width: 100%; height: 100%; }
</style></head><body>${svgContent}</body></html>`;

  await page.setContent(html, { waitUntil: 'networkidle0' });

  // Capture frames with real-time pacing
  const frameInterval = 1000 / fps;
  for (let i = 0; i < totalFrames; i++) {
    const framePath = path.join(framesDir, `frame-${String(i).padStart(5, '0')}.png`);
    await page.screenshot({ path: framePath });
    await new Promise(r => setTimeout(r, frameInterval));
  }

  await browser.close();

  // FFmpeg: frames -> mp4
  const framesPattern = path.join(framesDir, 'frame-%05d.png').replace(/\\/g, '/');
  const outputMp4 = path.join(outputDir, 'output.mp4').replace(/\\/g, '/');

  execSync(`"${ffmpeg}" -y -framerate ${fps} -i "${framesPattern}" -c:v libx264 -pix_fmt yuv420p -r 30 "${outputMp4}"`, { stdio: 'pipe' });
}

main().catch(err => { console.error(err); process.exit(1); });
```

- [ ] **Step 5: Test the wrapper end-to-end**

```bash
chmod +x demos/lib/cast-to-mp4.sh
bash demos/lib/cast-to-mp4.sh demos/tapes/test-scenario.txt demos/raw/test-wrapped.mp4 2
```

Expected: `demos/raw/test-wrapped.mp4` exists, plays correctly, slower than the prototype test (speed=2 instead of 10).

- [ ] **Step 6: Commit**

```bash
git add demos/config.env.example demos/lib/cast-to-mp4.sh demos/lib/svg-to-mp4.js
git commit -m "feat(demos): cast-to-mp4 wrapper and config template"
```

---

## Task 2: Narration Parser, Subtitle Generator, Title Card Generator

Three utility scripts that prepare assets for compositing.

**Files:**
- Create: `demos/lib/parse-narration.sh`
- Create: `demos/lib/generate-srt.sh`
- Create: `demos/lib/generate-title-card.sh`

- [ ] **Step 1: Write the narration parser**

Create `demos/lib/parse-narration.sh`:
```bash
#!/usr/bin/env bash
# parse-narration.sh <narration.md>
# Parses narration markdown into JSON sections.
# Output: JSON array to stdout
#   [{"name":"intro","text":"This is the intro..."},...]
#
# Format: ## section-name followed by narration text.

set -euo pipefail

INPUT="$1"

if [[ ! -f "$INPUT" ]]; then
  echo "ERROR: narration file not found: $INPUT" >&2
  exit 1
fi

awk '
BEGIN { printf "["; first = 1; name = ""; text = "" }
/^## / {
  if (name != "") {
    gsub(/^ +| +$/, "", text)
    gsub(/"/, "\\\"", text)
    gsub(/\n+$/, "", text)
    if (!first) printf ","
    printf "{\"name\":\"%s\",\"text\":\"%s\"}", name, text
    first = 0
  }
  name = substr($0, 4)
  gsub(/^ +| +$/, "", name)
  text = ""
  next
}
name != "" && /[^ ]/ {
  if (text != "") text = text " "
  line = $0
  gsub(/^ +| +$/, "", line)
  text = text line
}
END {
  if (name != "") {
    gsub(/^ +| +$/, "", text)
    gsub(/"/, "\\\"", text)
    gsub(/\n+$/, "", text)
    if (!first) printf ","
    printf "{\"name\":\"%s\",\"text\":\"%s\"}", name, text
  }
  printf "]"
}
' "$INPUT"
```

- [ ] **Step 2: Write a test narration file**

Create `demos/narration/test.md`:
```markdown
## intro
This is the introduction. It sets the scene.

## middle
This is the middle section where the action happens.

## outro
This is the conclusion. Short and direct.
```

- [ ] **Step 3: Test the parser**

```bash
chmod +x demos/lib/parse-narration.sh
bash demos/lib/parse-narration.sh demos/narration/test.md | jq .
```

Expected:
```json
[
  {"name": "intro", "text": "This is the introduction. It sets the scene."},
  {"name": "middle", "text": "This is the middle section where the action happens."},
  {"name": "outro", "text": "This is the conclusion. Short and direct."}
]
```

- [ ] **Step 4: Write the SRT subtitle generator**

Create `demos/lib/generate-srt.sh`:
```bash
#!/usr/bin/env bash
# generate-srt.sh <durations.json> <narration.md> <output.srt>
# Generates SRT subtitles timed to audio durations.
# Splits text into ~10-word chunks.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DURATIONS="$1"
NARRATION="$2"
OUTPUT="$3"

SECTIONS=$("$SCRIPT_DIR/parse-narration.sh" "$NARRATION")
COUNT=$(echo "$SECTIONS" | jq length)

format_ts() {
  local total_ms=$(echo "$1 * 1000" | bc | cut -d. -f1)
  local ms=$((total_ms % 1000))
  local total_s=$((total_ms / 1000))
  local s=$((total_s % 60))
  local m=$(((total_s / 60) % 60))
  local h=$((total_s / 3600))
  printf "%02d:%02d:%02d,%03d" "$h" "$m" "$s" "$ms"
}

SUBTITLE_NUM=1
CURRENT_TIME=0
> "$OUTPUT"

for i in $(seq 0 $((COUNT - 1))); do
  TEXT=$(echo "$SECTIONS" | jq -r ".[$i].text")
  DURATION=$(jq -r ".[$i].duration_s" "$DURATIONS")

  WORDS=($TEXT)
  TOTAL_WORDS=${#WORDS[@]}
  CHUNK_SIZE=10
  NUM_CHUNKS=$(( (TOTAL_WORDS + CHUNK_SIZE - 1) / CHUNK_SIZE ))
  [[ $NUM_CHUNKS -eq 0 ]] && NUM_CHUNKS=1

  CHUNK_DURATION=$(echo "$DURATION / $NUM_CHUNKS" | bc -l)

  for c in $(seq 0 $((NUM_CHUNKS - 1))); do
    START_WORD=$((c * CHUNK_SIZE))
    CHUNK_WORDS=("${WORDS[@]:$START_WORD:$CHUNK_SIZE}")
    CHUNK_TEXT="${CHUNK_WORDS[*]}"

    START_TS=$(format_ts "$CURRENT_TIME")
    CURRENT_TIME=$(echo "$CURRENT_TIME + $CHUNK_DURATION" | bc -l)
    END_TS=$(format_ts "$CURRENT_TIME")

    echo "$SUBTITLE_NUM" >> "$OUTPUT"
    echo "$START_TS --> $END_TS" >> "$OUTPUT"
    echo "$CHUNK_TEXT" >> "$OUTPUT"
    echo "" >> "$OUTPUT"

    SUBTITLE_NUM=$((SUBTITLE_NUM + 1))
  done
done

echo "Subtitles: $OUTPUT ($((SUBTITLE_NUM - 1)) entries)"
```

- [ ] **Step 5: Write the title card generator**

Create `demos/lib/generate-title-card.sh`:
```bash
#!/usr/bin/env bash
# generate-title-card.sh <text-file> <output.mp4> [duration_s]
# Renders text onto a dark background as a short mp4 clip.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DEMO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

TEXT_FILE="$1"
OUTPUT="$2"
DURATION="${3:-5}"

CONFIG="$DEMO_DIR/config.env"
if [[ -f "$CONFIG" ]]; then source "$CONFIG"; fi
WIDTH="${VIDEO_WIDTH:-1400}"
HEIGHT="${VIDEO_HEIGHT:-800}"

# Find ffmpeg
FFMPEG="${FFMPEG_BIN:-ffmpeg}"
if ! command -v "$FFMPEG" &>/dev/null; then
  FFMPEG="$(find /c/Users/*/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/ffmpeg-*/bin/ffmpeg.exe 2>/dev/null | head -1)"
fi

TEXT=$(cat "$TEXT_FILE" | sed "s/'/\\\\'/g" | sed ':a;N;$!ba;s/\n/\\n/g')

"$FFMPEG" -y -f lavfi \
  -i "color=c=#1e1e2e:s=${WIDTH}x${HEIGHT}:d=${DURATION}:r=30" \
  -vf "drawtext=text='${TEXT}':fontsize=28:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2:line_spacing=12" \
  -c:v libx264 -pix_fmt yuv420p \
  "$OUTPUT" \
  2>/dev/null

echo "Title card: $OUTPUT (${DURATION}s)"
```

- [ ] **Step 6: Test title card generator**

Create `demos/titles/test-card.txt`:
```
Signals gathered so far:

  discover-hypothesis: claim stated
  discover-competitors: 4 alternatives mapped

Now: validate the spec with 5 personas.
```

```bash
chmod +x demos/lib/generate-title-card.sh
bash demos/lib/generate-title-card.sh demos/titles/test-card.txt demos/raw/test-card.mp4
```

Expected: 5-second dark background mp4 with white centered text.

- [ ] **Step 7: Commit**

```bash
chmod +x demos/lib/parse-narration.sh demos/lib/generate-srt.sh demos/lib/generate-title-card.sh
git add demos/lib/parse-narration.sh demos/lib/generate-srt.sh demos/lib/generate-title-card.sh
git add demos/narration/test.md demos/titles/test-card.txt
git commit -m "feat(demos): narration parser, subtitle generator, title card generator"
```

---

## Task 3: ElevenLabs TTS Integration

Generate mp3 audio per narration section. Output durations.json for the sync contract.

**Files:**
- Create: `demos/lib/generate-audio.sh`

- [ ] **Step 1: Write the audio generator**

Create `demos/lib/generate-audio.sh`:
```bash
#!/usr/bin/env bash
# generate-audio.sh <narration.md> <output-dir>
# Generates one mp3 per narration section via ElevenLabs API.
# Writes durations.json with per-section timing.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
NARRATION="$1"
OUTPUT_DIR="$2"

CONFIG="$(cd "$SCRIPT_DIR/.." && pwd)/config.env"
if [[ ! -f "$CONFIG" ]]; then
  echo "ERROR: config.env not found. Copy config.env.example and add your API key." >&2
  exit 1
fi
source "$CONFIG"

if [[ -z "${ELEVENLABS_API_KEY:-}" || "$ELEVENLABS_API_KEY" == "your-key-here" ]]; then
  echo "ERROR: ELEVENLABS_API_KEY not set in config.env" >&2
  exit 1
fi

# Find ffprobe
FFPROBE="ffprobe"
if ! command -v "$FFPROBE" &>/dev/null; then
  FFPROBE="$(find /c/Users/*/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/ffmpeg-*/bin/ffprobe.exe 2>/dev/null | head -1)"
fi

mkdir -p "$OUTPUT_DIR"

SECTIONS=$("$SCRIPT_DIR/parse-narration.sh" "$NARRATION")
COUNT=$(echo "$SECTIONS" | jq length)

echo "  Generating audio for $COUNT sections..."

DURATIONS="["
FIRST=true

for i in $(seq 0 $((COUNT - 1))); do
  NAME=$(echo "$SECTIONS" | jq -r ".[$i].name")
  TEXT=$(echo "$SECTIONS" | jq -r ".[$i].text")
  OUTFILE="$OUTPUT_DIR/${NAME}.mp3"

  echo "    [$((i+1))/$COUNT] $NAME..."

  HTTP_CODE=$(curl -s -o "$OUTFILE" -w "%{http_code}" \
    -X POST \
    "https://api.elevenlabs.io/v1/text-to-speech/${ELEVENLABS_VOICE_ID}" \
    -H "xi-api-key: ${ELEVENLABS_API_KEY}" \
    -H "Content-Type: application/json" \
    -d "$(jq -n \
      --arg text "$TEXT" \
      --arg model "${ELEVENLABS_MODEL_ID:-eleven_monolingual_v1}" \
      '{text: $text, model_id: $model, voice_settings: {stability: 0.5, similarity_boost: 0.75}}'
    )")

  if [[ "$HTTP_CODE" != "200" ]]; then
    echo "ERROR: ElevenLabs returned HTTP $HTTP_CODE for '$NAME'" >&2
    cat "$OUTFILE" >&2
    exit 1
  fi

  DURATION=$("$FFPROBE" -v quiet -show_entries format=duration -of csv=p=0 "$OUTFILE")

  [[ "$FIRST" == "true" ]] && FIRST=false || DURATIONS="${DURATIONS},"
  DURATIONS="${DURATIONS}{\"name\":\"${NAME}\",\"file\":\"${NAME}.mp3\",\"duration_s\":${DURATION}}"
done

DURATIONS="${DURATIONS}]"
echo "$DURATIONS" | jq . > "$OUTPUT_DIR/durations.json"

echo "  Audio complete. Total: $(echo "$DURATIONS" | jq '[.[].duration_s] | add')s"
```

- [ ] **Step 2: Test with test narration (requires API key)**

```bash
cp demos/config.env.example demos/config.env
# Edit demos/config.env: add ELEVENLABS_API_KEY

chmod +x demos/lib/generate-audio.sh
bash demos/lib/generate-audio.sh demos/narration/test.md demos/audio/test
```

Expected: `demos/audio/test/` contains `intro.mp3`, `middle.mp3`, `outro.mp3`, `durations.json`.

- [ ] **Step 3: Commit**

```bash
git add demos/lib/generate-audio.sh
git commit -m "feat(demos): ElevenLabs TTS audio generation"
```

---

## Task 4: Video Compositor and Clip Extractor

Assembles all layers into the final video: title cards + terminal video + narration audio + subtitles. Also extracts 30-second clips.

**Files:**
- Create: `demos/lib/composite-video.sh`
- Create: `demos/lib/extract-clip.sh`

- [ ] **Step 1: Write the compositor**

Create `demos/lib/composite-video.sh`:
```bash
#!/usr/bin/env bash
# composite-video.sh <demo-name> <terminal.mp4> <audio-dir> <narration.md> <output.mp4>
# Composites terminal video + narration audio + subtitles + title cards.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DEMO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

DEMO_NAME="$1"
TERMINAL_VIDEO="$2"
AUDIO_DIR="$3"
NARRATION="$4"
OUTPUT="$5"

DURATIONS="$AUDIO_DIR/durations.json"

CONFIG="$DEMO_DIR/config.env"
if [[ -f "$CONFIG" ]]; then source "$CONFIG"; fi
WIDTH="${VIDEO_WIDTH:-1400}"
HEIGHT="${VIDEO_HEIGHT:-800}"

# Find ffmpeg/ffprobe
FFMPEG="${FFMPEG_BIN:-ffmpeg}"
FFPROBE="ffprobe"
if ! command -v "$FFMPEG" &>/dev/null; then
  FFMPEG="$(find /c/Users/*/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/ffmpeg-*/bin/ffmpeg.exe 2>/dev/null | head -1)"
  FFPROBE="$(find /c/Users/*/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/ffmpeg-*/bin/ffprobe.exe 2>/dev/null | head -1)"
fi

WORK=$(mktemp -d)

# --- Total narration duration (master clock) ---
TOTAL_NARRATION=$(jq '[.[].duration_s] | add' "$DURATIONS")
SECTION_COUNT=$(jq 'length' "$DURATIONS")
echo "  Narration: ${TOTAL_NARRATION}s across $SECTION_COUNT sections"

# --- Terminal video duration ---
RAW_DURATION=$("$FFPROBE" -v quiet -show_entries format=duration -of csv=p=0 "$TERMINAL_VIDEO")
echo "  Terminal video: ${RAW_DURATION}s"

# --- Speed factor ---
SPEED_FACTOR=$(echo "$RAW_DURATION / $TOTAL_NARRATION" | bc -l)
echo "  Speed factor: ${SPEED_FACTOR}x"

# --- Concatenate audio sections ---
AUDIO_LIST="$WORK/audio-concat.txt"
> "$AUDIO_LIST"
for i in $(seq 0 $((SECTION_COUNT - 1))); do
  FILE=$(jq -r ".[$i].file" "$DURATIONS")
  echo "file '$(cd "$AUDIO_DIR" && pwd)/${FILE}'" >> "$AUDIO_LIST"
done
COMBINED_AUDIO="$WORK/combined.mp3"
"$FFMPEG" -y -f concat -safe 0 -i "$AUDIO_LIST" -c copy "$COMBINED_AUDIO" 2>/dev/null

# --- Subtitles ---
SRT_FILE="$WORK/subtitles.srt"
bash "$SCRIPT_DIR/generate-srt.sh" "$DURATIONS" "$NARRATION" "$SRT_FILE" 2>/dev/null

# --- Title cards ---
TITLE_CONCAT="$WORK/title-concat.txt"
> "$TITLE_CONCAT"
TITLE_DURATION=0

for CARD_FILE in \
  "$DEMO_DIR/titles/endorsement.txt" \
  "$DEMO_DIR/titles/${DEMO_NAME}-opening.txt" \
  "$DEMO_DIR/titles/${DEMO_NAME}-prev.txt"; do

  if [[ -f "$CARD_FILE" ]]; then
    CARD_NAME=$(basename "$CARD_FILE" .txt)
    CARD_VIDEO="$WORK/${CARD_NAME}.mp4"
    bash "$SCRIPT_DIR/generate-title-card.sh" "$CARD_FILE" "$CARD_VIDEO" 5
    echo "file '$CARD_VIDEO'" >> "$TITLE_CONCAT"
    TITLE_DURATION=$((TITLE_DURATION + 5))
  fi
done

# --- Speed-adjust terminal video ---
SPEED_VIDEO="$WORK/speed-adjusted.mp4"
"$FFMPEG" -y -i "$TERMINAL_VIDEO" \
  -filter:v "setpts=PTS/${SPEED_FACTOR}" \
  -an -c:v libx264 -pix_fmt yuv420p -r 30 \
  "$SPEED_VIDEO" 2>/dev/null
echo "  Speed-adjusted terminal video"

# --- Concatenate: title cards + terminal ---
FINAL_CONCAT="$WORK/final-concat.txt"
> "$FINAL_CONCAT"
if [[ -s "$TITLE_CONCAT" ]]; then
  cat "$TITLE_CONCAT" >> "$FINAL_CONCAT"
fi
echo "file '$SPEED_VIDEO'" >> "$FINAL_CONCAT"

CONCAT_VIDEO="$WORK/concat.mp4"
"$FFMPEG" -y -f concat -safe 0 -i "$FINAL_CONCAT" \
  -c:v libx264 -pix_fmt yuv420p -r 30 \
  "$CONCAT_VIDEO" 2>/dev/null

# --- Final: video + audio + subtitles ---
"$FFMPEG" -y \
  -i "$CONCAT_VIDEO" \
  -i "$COMBINED_AUDIO" \
  -c:v libx264 -pix_fmt yuv420p \
  -c:a aac -b:a 192k \
  -vf "subtitles=${SRT_FILE}:force_style='FontSize=20,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,Outline=2,MarginV=40'" \
  -map 0:v -map 1:a \
  -shortest \
  "$OUTPUT" 2>/dev/null

FINAL_DURATION=$("$FFPROBE" -v quiet -show_entries format=duration -of csv=p=0 "$OUTPUT")
FINAL_SIZE=$(du -h "$OUTPUT" | cut -f1)
echo "  Output: $OUTPUT (${FINAL_DURATION}s, ${FINAL_SIZE})"

rm -rf "$WORK"
```

- [ ] **Step 2: Write the clip extractor**

Create `demos/lib/extract-clip.sh`:
```bash
#!/usr/bin/env bash
# extract-clip.sh <full-video.mp4> <output-clip.mp4> [start_s] [duration_s]
# Extracts a clip. Default: 30 seconds starting at 60% through.

set -euo pipefail

INPUT="$1"
OUTPUT="$2"
DURATION="${4:-30}"

FFMPEG="${FFMPEG_BIN:-ffmpeg}"
FFPROBE="ffprobe"
if ! command -v "$FFMPEG" &>/dev/null; then
  FFMPEG="$(find /c/Users/*/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/ffmpeg-*/bin/ffmpeg.exe 2>/dev/null | head -1)"
  FFPROBE="$(find /c/Users/*/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/ffmpeg-*/bin/ffprobe.exe 2>/dev/null | head -1)"
fi

TOTAL=$("$FFPROBE" -v quiet -show_entries format=duration -of csv=p=0 "$INPUT")

if [[ -z "${3:-}" ]]; then
  START=$(echo "$TOTAL * 0.6" | bc -l)
else
  START="$3"
fi

MAX_START=$(echo "$TOTAL - $DURATION" | bc -l)
if (( $(echo "$START > $MAX_START" | bc -l) )); then
  START="$MAX_START"
fi
# Don't go negative
if (( $(echo "$START < 0" | bc -l) )); then
  START=0
fi

"$FFMPEG" -y -ss "$START" -i "$INPUT" \
  -t "$DURATION" \
  -c:v libx264 -pix_fmt yuv420p \
  -c:a aac -b:a 192k \
  "$OUTPUT" 2>/dev/null

CLIP_SIZE=$(du -h "$OUTPUT" | cut -f1)
echo "  Clip: $OUTPUT (${DURATION}s from ${START}s, ${CLIP_SIZE})"
```

- [ ] **Step 3: Commit**

```bash
chmod +x demos/lib/composite-video.sh demos/lib/extract-clip.sh
git add demos/lib/composite-video.sh demos/lib/extract-clip.sh
git commit -m "feat(demos): video compositor and clip extractor"
```

---

## Task 5: Main Orchestrator (render-demo.sh)

The one command that does everything.

**Files:**
- Create: `demos/render-demo.sh`

- [ ] **Step 1: Write the orchestrator**

Create `demos/render-demo.sh`:
```bash
#!/usr/bin/env bash
# render-demo.sh <demo-name>
#
# Renders a complete demo video from three inputs:
#   scenarios/<demo-name>.txt    - terminal-demo scenario
#   narration/<demo-name>.md     - narration text by section
#   titles/<demo-name>-*.txt     - title cards (optional)
#
# Outputs:
#   final/<demo-name>.mp4        - full demo video
#   final/<demo-name>-clip.mp4   - 30-second highlight clip
#
# Usage:
#   ./render-demo.sh demo-0-install
#   ./render-demo.sh demo-3-persona

set -euo pipefail

DEMO_NAME="$1"
DEMO_DIR="$(cd "$(dirname "$0")" && pwd)"
LIB="$DEMO_DIR/lib"

echo ""
echo "========================================"
echo "  Demo Video Pipeline: $DEMO_NAME"
echo "========================================"
echo ""

# Verify inputs
SCENARIO="$DEMO_DIR/scenarios/${DEMO_NAME}.txt"
NARRATION="$DEMO_DIR/narration/${DEMO_NAME}.md"

[[ ! -f "$SCENARIO" ]] && echo "ERROR: scenario not found: $SCENARIO" >&2 && exit 1
[[ ! -f "$NARRATION" ]] && echo "ERROR: narration not found: $NARRATION" >&2 && exit 1

# Output paths
RAW_DIR="$DEMO_DIR/raw"
AUDIO_DIR="$DEMO_DIR/audio/${DEMO_NAME}"
FINAL_DIR="$DEMO_DIR/final"
mkdir -p "$RAW_DIR" "$AUDIO_DIR" "$FINAL_DIR"

TERMINAL_VIDEO="$RAW_DIR/${DEMO_NAME}-terminal.mp4"
FINAL_VIDEO="$FINAL_DIR/${DEMO_NAME}.mp4"
CLIP_VIDEO="$FINAL_DIR/${DEMO_NAME}-clip.mp4"

# --- Stage 1: Record terminal session ---
echo "[1/4] Recording terminal scenario..."
bash "$LIB/cast-to-mp4.sh" "$SCENARIO" "$TERMINAL_VIDEO" 2
echo ""

# --- Stage 2: Generate narration audio ---
echo "[2/4] Generating narration audio..."
bash "$LIB/generate-audio.sh" "$NARRATION" "$AUDIO_DIR"
echo ""

# --- Stage 3: Composite video ---
echo "[3/4] Compositing video..."
bash "$LIB/composite-video.sh" "$DEMO_NAME" "$TERMINAL_VIDEO" "$AUDIO_DIR" "$NARRATION" "$FINAL_VIDEO"
echo ""

# --- Stage 4: Extract clip ---
echo "[4/4] Extracting 30-second clip..."
bash "$LIB/extract-clip.sh" "$FINAL_VIDEO" "$CLIP_VIDEO"
echo ""

# --- Summary ---
echo "========================================"
echo "  COMPLETE: $DEMO_NAME"
echo "========================================"
echo ""
echo "  Full:  $FINAL_VIDEO"
echo "  Clip:  $CLIP_VIDEO"
echo ""
```

- [ ] **Step 2: Commit**

```bash
chmod +x demos/render-demo.sh
git add demos/render-demo.sh
git commit -m "feat(demos): render-demo.sh orchestrator"
```

---

## Task 6: Author Demo 0 -- Install

The gateway video. 90 seconds. "You got a link from a colleague."

**Files:**
- Create: `demos/scenarios/demo-0-install.txt`
- Create: `demos/narration/demo-0-install.md`
- Create: `demos/titles/endorsement.txt`
- Create: `demos/titles/demo-0-install-opening.txt`

- [ ] **Step 1: Run a real bootstrap session and capture the output**

Run the actual bootstrap flow in a separate terminal. Copy the real output for the scenario file. The scenario must contain authentic output, not guesses.

```bash
# In a separate terminal, run:
# gh repo clone gim-home/craftworks-research /tmp/cr -- --depth=1 --filter=blob:none --sparse --quiet
# cd /tmp/cr && git sparse-checkout set toolkits/simlab --quiet
# bash toolkits/simlab/bootstrap.sh test-demo
#
# Copy the output from each step into the scenario file below.
```

- [ ] **Step 2: Write the scenario file**

Create `demos/scenarios/demo-0-install.txt` using real output from Step 1:
```
$ gh repo clone gim-home/craftworks-research /tmp/cr -- --depth=1 --filter=blob:none --sparse --quiet
Cloning into '/tmp/cr'...

$ cd /tmp/cr && git sparse-checkout set toolkits/simlab --quiet

$ bash toolkits/simlab/bootstrap.sh my-simlab

Signal simlab bootstrap
  destination : /c/src/my-simlab

Fetching simlab from craftworks-research...
Copying to /c/src/my-simlab...
Installing Signal skills...
Done.

  Your Signal workspace is ready at /c/src/my-simlab
  cd ../my-simlab && claude

$ cd ../my-simlab && claude

Claude Code v1.0.0

$ /signal

Signal - 63 skills across 9 namespaces

  discover:  competitors, feasibility, inertia, hypothesis, risk, analysis, synthesize
  specify:   spec, proposal, pitch, commitment, abstract
  validate:  design, users, customers, code, adoption, feedback, support
  simulate:  lifecycle, request, state, contract, conversation, argument
  rhythm:    decide, status, story, qa, brief, rebuttal
  roles:     scan, build, check, product-review, pull-request
  research:  pre-write, post-write
  tools:     coverage, preview, accept
  signal:    signal, signal-health, signal-setup

  Type /signal <namespace> for details.
```

Note: Replace the output above with actual output from Step 1 before rendering.

- [ ] **Step 3: Write the narration script**

Create `demos/narration/demo-0-install.md`:
```markdown
## opening
You are a principal PM. A colleague sent you a link and said: try this on your next spec. This is a representative session showing what happens in the next 90 seconds.

## clone
One command pulls the Signal toolkit from GitHub. Sparse clone -- only what you need.

## bootstrap
The bootstrap script creates your workspace and installs 63 skills across 9 namespaces. Each skill produces a signal -- an auditable artifact toward your feature decision.

## launch
Claude Code opens in the workspace. Signal is ready.

## skills
Sixty-three skills. Investigation, specification, validation, simulation. Every stage of product design, one command each. You are ready to run your first investigation.
```

- [ ] **Step 4: Write title cards**

Create `demos/titles/endorsement.txt`:
```
"I ran this on my actual feature spec.
 It found three issues my team missed in review."

 -- [Name], Principal PM, [Product Area]
```

Create `demos/titles/demo-0-install-opening.txt`:
```
You got a link from a colleague.

"Try this on your next spec."
```

- [ ] **Step 5: Commit**

```bash
git add demos/scenarios/demo-0-install.txt demos/narration/demo-0-install.md
git add demos/titles/endorsement.txt demos/titles/demo-0-install-opening.txt
git commit -m "feat(demos): Demo 0 Install scenario and narration"
```

---

## Task 7: Author Demo 3 -- Spec + Persona Test

The signature video. 3 minutes. "You wrote a spec. Before the review meeting..."

**Files:**
- Create: `demos/scenarios/demo-3-persona.txt`
- Create: `demos/narration/demo-3-persona.md`
- Create: `demos/titles/demo-3-persona-opening.txt`
- Create: `demos/titles/demo-3-persona-prev.txt`

- [ ] **Step 1: Run a real /validate-users session and capture output**

Run `/validate-users` on a real topic in simlab. Copy the actual output for the scenario.

```bash
# In Claude Code in simlab workspace:
# /validate-users api-copilot
#
# Copy the output including persona names, findings, scores.
# Also copy your steering prompts and the AI's responses.
```

- [ ] **Step 2: Write the scenario file**

Create `demos/scenarios/demo-3-persona.txt` using real output from Step 1. Structure:

```
$ /validate-users api-copilot

[Paste real persona walkthrough output here]

$ Persona 3 raised a good point about the onboarding flow. Go deeper on that. What specifically would confuse a new user in the first 5 minutes?

[Paste real response here]

$ The mobile PM persona is not relevant for this feature. Focus on the platform PM and data analyst personas. What would they change about section 3?

[Paste real response here]

$ Summarize the top 5 findings I should fix before Thursday. Priority order.

[Paste real prioritized summary here]
```

- [ ] **Step 3: Write the narration script**

Create `demos/narration/demo-3-persona.md`:
```markdown
## opening
You wrote a spec. The review meeting is Thursday. What if five different personas could read it first? This is a representative session showing how a PM validates a spec with Signal.

## personas
The validate-users skill sends the spec through five persona advocates. Each reads in first person and flags what confuses them. Watch the findings come in -- each persona sees the spec differently.

## steer
Here is the moment that matters. The PM reads the output and pushes back. Persona 3 flagged the onboarding flow -- the PM decides to go deeper. This is not a passive tool. The PM steers it.

## focus
Another judgment call. The PM drops an irrelevant persona and narrows focus to the two that matter. The AI follows the PM's domain knowledge.

## summary
Five personas. Twelve findings. The PM asks for the top five in priority order. The spec improves before a single engineer reads it.
```

- [ ] **Step 4: Write title cards**

Create `demos/titles/demo-3-persona-opening.txt`:
```
You wrote a spec. The review meeting is Thursday.

What if five different personas read it first?
```

Create `demos/titles/demo-3-persona-prev.txt`:
```
Signals gathered so far:

  discover-hypothesis: claim stated, falsification defined
  discover-competitors: 4 alternatives mapped, inertia is #1
  discover-synthesize: PROCEED with conditions

Now: validate the spec with 5 personas.
```

- [ ] **Step 5: Commit**

```bash
git add demos/scenarios/demo-3-persona.txt demos/narration/demo-3-persona.md
git add demos/titles/demo-3-persona-opening.txt demos/titles/demo-3-persona-prev.txt
git commit -m "feat(demos): Demo 3 Spec + Persona Test scenario and narration"
```

---

## Task 8: End-to-End Test

Run the full pipeline on Demo 0 and verify all acceptance criteria.

**Files:** No new files.

- [ ] **Step 1: Set up config.env**

```bash
cp demos/config.env.example demos/config.env
# Add ELEVENLABS_API_KEY to demos/config.env
```

- [ ] **Step 2: Run Demo 0**

```bash
bash demos/render-demo.sh demo-0-install
```

Expected:
```
========================================
  Demo Video Pipeline: demo-0-install
========================================

[1/4] Recording terminal scenario...
[2/4] Generating narration audio...
[3/4] Compositing video...
[4/4] Extracting 30-second clip...

========================================
  COMPLETE: demo-0-install
========================================

  Full:  demos/final/demo-0-install.mp4
  Clip:  demos/final/demo-0-install-clip.mp4
```

- [ ] **Step 3: Verify acceptance criteria**

Open both videos:
```bash
start demos/final/demo-0-install.mp4
start demos/final/demo-0-install-clip.mp4
```

Check:
- [ ] Opening title card visible for ~5 seconds
- [ ] Endorsement card visible for ~10-15 seconds
- [ ] Terminal text readable at playback speed
- [ ] Narration syncs with terminal content
- [ ] Subtitles present and timed correctly
- [ ] Clip is ~30 seconds
- [ ] File size under 150MB

- [ ] **Step 4: Run Demo 3**

```bash
bash demos/render-demo.sh demo-3-persona
```

Same verification as above.

- [ ] **Step 5: Commit any fixes**

```bash
git add demos/lib/
git commit -m "fix(demos): iteration fixes from end-to-end test"
```

---

## Task Summary

| Task | What | Depends On | Parallelizable With |
|------|------|-----------|-------------------|
| 1 | Scaffold + cast-to-mp4 wrapper | -- | -- |
| 2 | Parser + subtitles + title cards | 1 | 3 |
| 3 | ElevenLabs TTS | 1 | 2 |
| 4 | Compositor + clip extractor | 2, 3 | -- |
| 5 | Orchestrator (render-demo.sh) | 4 | -- |
| 6 | Author Demo 0: Install | 5 | 7 |
| 7 | Author Demo 3: Persona Test | 5 | 6 |
| 8 | End-to-end test | 6, 7 | -- |
