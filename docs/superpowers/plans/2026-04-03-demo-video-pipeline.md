# Demo Video Pipeline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an automated pipeline that renders professional demo videos from three text inputs (tape file, narration script, title card text) with one shell command.

**Architecture:** A bash orchestrator (`render-demo.sh`) coordinates three stages: (1) VHS records a real terminal session from a tape file, (2) ElevenLabs API generates voiceover from a narration markdown file, (3) FFmpeg composites terminal video + audio + subtitles + title cards into a final mp4 and a 30-second clip. Narration duration is the master clock; terminal video is speed-adjusted to match.

**Tech Stack:** VHS (terminal recording), FFmpeg (video compositing), ElevenLabs API (TTS), bash + jq (orchestration), curl (API calls)

**Spec:** `docs/superpowers/specs/2026-04-03-demo-video-pipeline-design.md`

**Platform note:** VHS has known issues on Windows 11 with Git Bash (issues #541, #631). Plan includes a WSL2 path as primary and native Windows with ttyd 1.7.3 as fallback.

---

## File Structure

```
demos/
  render-demo.sh              # Main orchestrator (Task 7)
  lib/
    parse-narration.sh         # Markdown -> section JSON (Task 2)
    generate-audio.sh          # ElevenLabs TTS per section (Task 3)
    composite-video.sh         # FFmpeg assembly (Task 5)
    extract-clip.sh            # 30-second clip extraction (Task 6)
    generate-srt.sh            # Subtitle generation from narration (Task 4)
    generate-title-card.sh     # Title card image generation (Task 4)
  config.env.example           # Template for API keys and settings (Task 1)
  tapes/
    demo-0-install.tape        # Demo 0 tape file (Task 7)
    demo-3-persona.tape        # Demo 3 tape file (Task 8)
  narration/
    demo-0-install.md          # Demo 0 narration script (Task 7)
    demo-3-persona.md          # Demo 3 narration script (Task 8)
  titles/
    endorsement.txt            # Endorsement card text (Task 7)
    demo-0-opening.txt         # "You got a link from a colleague." (Task 7)
    demo-3-opening.txt         # "You wrote a spec..." (Task 8)
    demo-3-previously.txt      # "Previously gathered" card (Task 8)
  raw/                         # VHS output (git-ignored)
  audio/                       # Generated voiceover (git-ignored)
  final/                       # Finished mp4s and clips (git-ignored)
```

---

## Task 1: Project Scaffolding and Tooling Setup

**Files:**
- Create: `demos/config.env.example`
- Create: `demos/.gitignore`
- Create: `demos/README.md`

- [ ] **Step 1: Create the demos directory structure**

```bash
cd /c/src/signals
mkdir -p demos/{lib,tapes,narration,titles,openings,raw,audio,final}
```

- [ ] **Step 2: Create .gitignore for generated files**

Create `demos/.gitignore`:
```
raw/
audio/
final/
config.env
```

- [ ] **Step 3: Create config.env.example**

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
VIDEO_FONT_SIZE=14
VIDEO_THEME="Catppuccin Mocha"
VIDEO_FRAMERATE=30

# Paths (auto-detected if blank)
VHS_BIN=""
FFMPEG_BIN=""
```

- [ ] **Step 4: Verify VHS is available**

Run in WSL2 (preferred) or native:
```bash
# WSL2 path (recommended):
wsl -- bash -c "which vhs && vhs --version"

# Native fallback:
vhs --version

# If neither works, install:
# WSL2: go install github.com/charmbracelet/vhs@latest
# Native: winget install charmbracelet.vhs
```

Expected: version string like `vhs version v0.7.2`

- [ ] **Step 5: Verify FFmpeg is available**

```bash
ffmpeg -version | head -1
```

Expected: `ffmpeg version X.X.X`

If missing: `choco install ffmpeg`

- [ ] **Step 6: Test VHS with a minimal tape**

Create `demos/tapes/test.tape`:
```tape
Output demos/raw/test.mp4
Set FontSize 14
Set Width 1400
Set Height 800
Set Theme "Catppuccin Mocha"
Set Shell "bash"

Type "echo hello world"
Enter
Sleep 2s
```

Run:
```bash
# WSL2 path:
wsl -- bash -c "cd /mnt/c/src/signals && vhs demos/tapes/test.tape"

# Native path:
vhs demos/tapes/test.tape
```

Expected: `demos/raw/test.mp4` exists and shows "hello world" in terminal.

- [ ] **Step 7: Commit scaffolding**

```bash
git add demos/.gitignore demos/config.env.example
git commit -m "feat(demos): scaffold video pipeline directory structure"
```

---

## Task 2: Narration Parser

Parses a narration markdown file into a JSON array of sections. Each section has a name and text. No timestamps in the input -- those are calculated at render time from audio durations.

**Files:**
- Create: `demos/lib/parse-narration.sh`

- [ ] **Step 1: Write a test narration file**

Create `demos/narration/test.md`:
```markdown
## intro
This is the introduction section.
It can span multiple lines.

## middle
This is the middle section with a single line.

## outro
This is the outro.
Short and direct.
```

- [ ] **Step 2: Write the parser**

Create `demos/lib/parse-narration.sh`:
```bash
#!/usr/bin/env bash
# parse-narration.sh <narration.md>
# Parses narration markdown into JSON sections.
# Output: JSON array to stdout
#   [{"name":"intro","text":"This is the intro..."},...]
#
# Format: ## section-name followed by narration text.
# Blank lines between sections are ignored.

set -euo pipefail

INPUT="$1"

if [[ ! -f "$INPUT" ]]; then
  echo "ERROR: narration file not found: $INPUT" >&2
  exit 1
fi

awk '
BEGIN {
  printf "["
  first = 1
  name = ""
  text = ""
}

/^## / {
  if (name != "") {
    # Emit previous section
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

- [ ] **Step 3: Make it executable and test**

```bash
chmod +x demos/lib/parse-narration.sh
bash demos/lib/parse-narration.sh demos/narration/test.md | jq .
```

Expected output:
```json
[
  {
    "name": "intro",
    "text": "This is the introduction section. It can span multiple lines."
  },
  {
    "name": "middle",
    "text": "This is the middle section with a single line."
  },
  {
    "name": "outro",
    "text": "This is the outro. Short and direct."
  }
]
```

- [ ] **Step 4: Commit**

```bash
git add demos/lib/parse-narration.sh demos/narration/test.md
git commit -m "feat(demos): narration markdown parser"
```

---

## Task 3: ElevenLabs TTS Integration

Generates mp3 audio files from narration sections using the ElevenLabs API. One mp3 per section. Also calculates duration of each clip for the sync contract.

**Files:**
- Create: `demos/lib/generate-audio.sh`

- [ ] **Step 1: Write the audio generator**

Create `demos/lib/generate-audio.sh`:
```bash
#!/usr/bin/env bash
# generate-audio.sh <narration.md> <output-dir>
# Generates one mp3 per narration section via ElevenLabs API.
# Outputs a durations JSON file: <output-dir>/durations.json
#   [{"name":"intro","file":"intro.mp3","duration_s":8.2},...]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
NARRATION="$1"
OUTPUT_DIR="$2"

# Load config
CONFIG="$(cd "$SCRIPT_DIR/.." && pwd)/config.env"
if [[ ! -f "$CONFIG" ]]; then
  echo "ERROR: config.env not found at $CONFIG" >&2
  echo "Copy config.env.example to config.env and add your ElevenLabs API key." >&2
  exit 1
fi
source "$CONFIG"

if [[ -z "${ELEVENLABS_API_KEY:-}" || "$ELEVENLABS_API_KEY" == "your-key-here" ]]; then
  echo "ERROR: ELEVENLABS_API_KEY not set in config.env" >&2
  exit 1
fi

mkdir -p "$OUTPUT_DIR"

# Parse narration into sections
SECTIONS=$("$SCRIPT_DIR/parse-narration.sh" "$NARRATION")
COUNT=$(echo "$SECTIONS" | jq length)

echo "Generating audio for $COUNT sections..."

DURATIONS="["
FIRST=true

for i in $(seq 0 $((COUNT - 1))); do
  NAME=$(echo "$SECTIONS" | jq -r ".[$i].name")
  TEXT=$(echo "$SECTIONS" | jq -r ".[$i].text")
  OUTFILE="$OUTPUT_DIR/${NAME}.mp3"

  echo "  [$((i+1))/$COUNT] $NAME..."

  # ElevenLabs text-to-speech API
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
    echo "ERROR: ElevenLabs API returned HTTP $HTTP_CODE for section '$NAME'" >&2
    echo "Response:" >&2
    cat "$OUTFILE" >&2
    exit 1
  fi

  # Get duration using ffprobe
  DURATION=$(ffprobe -v quiet -show_entries format=duration -of csv=p=0 "$OUTFILE")

  if [[ "$FIRST" == "true" ]]; then
    FIRST=false
  else
    DURATIONS="${DURATIONS},"
  fi
  DURATIONS="${DURATIONS}{\"name\":\"${NAME}\",\"file\":\"${NAME}.mp3\",\"duration_s\":${DURATION}}"
done

DURATIONS="${DURATIONS}]"
echo "$DURATIONS" | jq . > "$OUTPUT_DIR/durations.json"

echo "Audio generation complete. Durations:"
cat "$OUTPUT_DIR/durations.json" | jq -r '.[] | "  \(.name): \(.duration_s)s"'
```

- [ ] **Step 2: Test with the test narration (requires API key)**

```bash
chmod +x demos/lib/generate-audio.sh
# First, copy config.env.example to config.env and add your key
cp demos/config.env.example demos/config.env
# Edit demos/config.env with your ElevenLabs API key

bash demos/lib/generate-audio.sh demos/narration/test.md demos/audio/test
```

Expected: `demos/audio/test/` contains `intro.mp3`, `middle.mp3`, `outro.mp3`, and `durations.json`.

- [ ] **Step 3: Verify durations.json**

```bash
cat demos/audio/test/durations.json | jq .
```

Expected: JSON array with name, file, and duration_s for each section.

- [ ] **Step 4: Commit**

```bash
git add demos/lib/generate-audio.sh
git commit -m "feat(demos): ElevenLabs TTS audio generation"
```

---

## Task 4: Title Card and Subtitle Generators

Generates static title card images (endorsement, opening frame, "previously gathered") and SRT subtitle files from narration sections.

**Files:**
- Create: `demos/lib/generate-title-card.sh`
- Create: `demos/lib/generate-srt.sh`

- [ ] **Step 1: Write the title card generator**

Uses FFmpeg to render text onto a dark background image. No external image tools needed.

Create `demos/lib/generate-title-card.sh`:
```bash
#!/usr/bin/env bash
# generate-title-card.sh <text-file> <output.png> [duration_s]
# Renders text from a file onto a dark background image using FFmpeg.
# Default resolution: 1400x800 to match VHS output.

set -euo pipefail

TEXT_FILE="$1"
OUTPUT="$2"
DURATION="${3:-5}"

# Load config for dimensions
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CONFIG="$(cd "$SCRIPT_DIR/.." && pwd)/config.env"
if [[ -f "$CONFIG" ]]; then
  source "$CONFIG"
fi

WIDTH="${VIDEO_WIDTH:-1400}"
HEIGHT="${VIDEO_HEIGHT:-800}"

# Read text and escape for FFmpeg drawtext
TEXT=$(cat "$TEXT_FILE" | sed "s/'/\\\\'/g" | sed ':a;N;$!ba;s/\n/\\n/g')

# Generate a dark background with centered white text
ffmpeg -y -f lavfi \
  -i "color=c=#1e1e2e:s=${WIDTH}x${HEIGHT}:d=${DURATION}:r=30" \
  -vf "drawtext=text='${TEXT}':fontsize=28:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2:line_spacing=12" \
  -frames:v 1 \
  "$OUTPUT" \
  2>/dev/null

echo "Title card: $OUTPUT"
```

- [ ] **Step 2: Test the title card generator**

Create `demos/titles/test-card.txt`:
```
Signals gathered so far:

  discover-hypothesis: claim stated
  discover-competitors: 4 alternatives mapped
  discover-synthesize: PROCEED with conditions

Now: validate the spec with 5 personas.
```

```bash
chmod +x demos/lib/generate-title-card.sh
bash demos/lib/generate-title-card.sh demos/titles/test-card.txt demos/raw/test-card.png
```

Expected: `demos/raw/test-card.png` is a 1400x800 dark image with white text centered.

- [ ] **Step 3: Write the SRT subtitle generator**

Create `demos/lib/generate-srt.sh`:
```bash
#!/usr/bin/env bash
# generate-srt.sh <durations.json> <narration.md> <output.srt>
# Generates SRT subtitles from narration sections, timed to audio durations.
# Splits long narration text into subtitle chunks of ~10 words each.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DURATIONS="$1"
NARRATION="$2"
OUTPUT="$3"

SECTIONS=$("$SCRIPT_DIR/parse-narration.sh" "$NARRATION")
COUNT=$(echo "$SECTIONS" | jq length)

# Format seconds as SRT timestamp: HH:MM:SS,mmm
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
  NAME=$(echo "$SECTIONS" | jq -r ".[$i].name")
  TEXT=$(echo "$SECTIONS" | jq -r ".[$i].text")
  DURATION=$(jq -r ".[$i].duration_s" "$DURATIONS")

  # Split text into chunks of ~10 words
  WORDS=($TEXT)
  TOTAL_WORDS=${#WORDS[@]}
  CHUNK_SIZE=10
  NUM_CHUNKS=$(( (TOTAL_WORDS + CHUNK_SIZE - 1) / CHUNK_SIZE ))

  if [[ $NUM_CHUNKS -eq 0 ]]; then
    NUM_CHUNKS=1
  fi

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

- [ ] **Step 4: Commit**

```bash
chmod +x demos/lib/generate-title-card.sh demos/lib/generate-srt.sh
git add demos/lib/generate-title-card.sh demos/lib/generate-srt.sh demos/titles/test-card.txt
git commit -m "feat(demos): title card and subtitle generators"
```

---

## Task 5: Video Compositor

Takes the raw VHS terminal video, narration audio clips, and durations JSON, then produces the composited full-length video with speed ramping, title cards, and subtitles.

**Files:**
- Create: `demos/lib/composite-video.sh`

- [ ] **Step 1: Write the compositor**

This is the core of the pipeline. It:
1. Reads durations.json to know how long each narration section is
2. Probes the raw VHS video for total duration
3. Divides the VHS video into segments matching each narration section
4. Speed-adjusts each terminal segment to match its narration duration
5. Concatenates narration audio into one track
6. Overlays subtitles
7. Prepends title cards (endorsement, opening frame)

Create `demos/lib/composite-video.sh`:
```bash
#!/usr/bin/env bash
# composite-video.sh <demo-name> <raw-video> <audio-dir> <narration.md> <output.mp4>
#
# Composites raw terminal video with narration audio, subtitles, and title cards.
# The narration audio is the master clock -- terminal video is speed-adjusted to match.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DEMO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

DEMO_NAME="$1"
RAW_VIDEO="$2"
AUDIO_DIR="$3"
NARRATION="$4"
OUTPUT="$5"

DURATIONS="$AUDIO_DIR/durations.json"

# Load config
CONFIG="$DEMO_DIR/config.env"
if [[ -f "$CONFIG" ]]; then source "$CONFIG"; fi
WIDTH="${VIDEO_WIDTH:-1400}"
HEIGHT="${VIDEO_HEIGHT:-800}"
FPS="${VIDEO_FRAMERATE:-30}"

# --- Step 1: Calculate total narration duration ---
TOTAL_NARRATION=$(jq '[.[].duration_s] | add' "$DURATIONS")
SECTION_COUNT=$(jq 'length' "$DURATIONS")
echo "Total narration duration: ${TOTAL_NARRATION}s across $SECTION_COUNT sections"

# --- Step 2: Get raw video duration ---
RAW_DURATION=$(ffprobe -v quiet -show_entries format=duration -of csv=p=0 "$RAW_VIDEO")
echo "Raw terminal video duration: ${RAW_DURATION}s"

# --- Step 3: Calculate uniform speed factor ---
# Simple approach: apply uniform speed to entire terminal video to match narration length.
# This avoids complex per-section splitting which is fragile.
# The tape file's Wait commands already create natural section breaks.
SPEED_FACTOR=$(echo "$RAW_DURATION / $TOTAL_NARRATION" | bc -l)
echo "Speed factor: ${SPEED_FACTOR}x"

# --- Step 4: Concatenate all audio sections ---
AUDIO_LIST="$AUDIO_DIR/concat.txt"
> "$AUDIO_LIST"
for i in $(seq 0 $((SECTION_COUNT - 1))); do
  FILE=$(jq -r ".[$i].file" "$DURATIONS")
  echo "file '$(cd "$AUDIO_DIR" && pwd)/${FILE}'" >> "$AUDIO_LIST"
done

COMBINED_AUDIO="$AUDIO_DIR/combined.mp3"
ffmpeg -y -f concat -safe 0 -i "$AUDIO_LIST" -c copy "$COMBINED_AUDIO" 2>/dev/null
echo "Combined audio: $COMBINED_AUDIO"

# --- Step 5: Generate subtitles ---
SRT_FILE="$AUDIO_DIR/subtitles.srt"
bash "$SCRIPT_DIR/generate-srt.sh" "$DURATIONS" "$NARRATION" "$SRT_FILE"

# --- Step 6: Check for title cards ---
ENDORSEMENT="$DEMO_DIR/titles/endorsement.txt"
OPENING="$DEMO_DIR/titles/${DEMO_NAME}-opening.txt"
PREVIOUSLY="$DEMO_DIR/titles/${DEMO_NAME}-previously.txt"

# Build title card videos (5s each) if text files exist
TITLE_PARTS=""
TITLE_CONCAT="$AUDIO_DIR/title-concat.txt"
> "$TITLE_CONCAT"

for CARD_FILE in "$ENDORSEMENT" "$OPENING" "$PREVIOUSLY"; do
  if [[ -f "$CARD_FILE" ]]; then
    CARD_NAME=$(basename "$CARD_FILE" .txt)
    CARD_VIDEO="$AUDIO_DIR/${CARD_NAME}-card.mp4"
    CARD_TEXT=$(cat "$CARD_FILE" | sed "s/'/\\\\'/g" | sed ':a;N;$!ba;s/\n/\\n/g')

    ffmpeg -y -f lavfi \
      -i "color=c=#1e1e2e:s=${WIDTH}x${HEIGHT}:d=5:r=${FPS}" \
      -vf "drawtext=text='${CARD_TEXT}':fontsize=28:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2:line_spacing=12" \
      -c:v libx264 -pix_fmt yuv420p \
      "$CARD_VIDEO" 2>/dev/null

    echo "file '$CARD_VIDEO'" >> "$TITLE_CONCAT"
    echo "Title card: $CARD_NAME (5s)"
  fi
done

# --- Step 7: Composite everything ---
# Speed-adjust terminal video, add title cards at front, overlay audio + subtitles

# Speed-adjusted terminal video
SPEED_VIDEO="$AUDIO_DIR/speed-adjusted.mp4"
# FFmpeg setpts: PTS/speed_factor speeds up, PTS*factor slows down
# For speed factor > 1 (video longer than audio), we speed up: PTS/factor
ffmpeg -y -i "$RAW_VIDEO" \
  -filter:v "setpts=PTS/${SPEED_FACTOR}" \
  -an \
  -c:v libx264 -pix_fmt yuv420p -r "$FPS" \
  "$SPEED_VIDEO" 2>/dev/null
echo "Speed-adjusted video: ${SPEED_FACTOR}x"

# Concatenate: title cards + speed-adjusted terminal
FINAL_CONCAT="$AUDIO_DIR/final-concat.txt"
> "$FINAL_CONCAT"

# Add title card parts if they exist
if [[ -s "$TITLE_CONCAT" ]]; then
  cat "$TITLE_CONCAT" >> "$FINAL_CONCAT"
fi

echo "file '$SPEED_VIDEO'" >> "$FINAL_CONCAT"

CONCAT_VIDEO="$AUDIO_DIR/concat-video.mp4"
ffmpeg -y -f concat -safe 0 -i "$FINAL_CONCAT" \
  -c:v libx264 -pix_fmt yuv420p -r "$FPS" \
  "$CONCAT_VIDEO" 2>/dev/null

# Calculate title card total duration for subtitle offset
TITLE_DURATION=0
if [[ -s "$TITLE_CONCAT" ]]; then
  TITLE_COUNT=$(wc -l < "$TITLE_CONCAT")
  TITLE_DURATION=$((TITLE_COUNT * 5))
fi

# Final composite: video + audio + subtitles
# Offset subtitles by title card duration
ffmpeg -y \
  -i "$CONCAT_VIDEO" \
  -i "$COMBINED_AUDIO" \
  -c:v libx264 -pix_fmt yuv420p \
  -c:a aac -b:a 192k \
  -vf "subtitles=${SRT_FILE}:force_style='FontSize=20,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,Outline=2,MarginV=40'" \
  -map 0:v -map 1:a \
  -shortest \
  "$OUTPUT" 2>/dev/null

echo ""
echo "=== OUTPUT: $OUTPUT ==="
FINAL_DURATION=$(ffprobe -v quiet -show_entries format=duration -of csv=p=0 "$OUTPUT")
FINAL_SIZE=$(du -h "$OUTPUT" | cut -f1)
echo "Duration: ${FINAL_DURATION}s | Size: ${FINAL_SIZE}"
```

- [ ] **Step 2: Make executable**

```bash
chmod +x demos/lib/composite-video.sh
```

- [ ] **Step 3: Commit**

```bash
git add demos/lib/composite-video.sh
git commit -m "feat(demos): FFmpeg video compositor with speed ramping and title cards"
```

---

## Task 6: Clip Extractor

Extracts a 30-second highlight clip from the full video, targeting the "money moment."

**Files:**
- Create: `demos/lib/extract-clip.sh`

- [ ] **Step 1: Write the clip extractor**

Create `demos/lib/extract-clip.sh`:
```bash
#!/usr/bin/env bash
# extract-clip.sh <full-video.mp4> <output-clip.mp4> [start_time] [duration]
# Extracts a clip from the full video.
# Default: last 30 seconds (where the money moment typically is).

set -euo pipefail

INPUT="$1"
OUTPUT="$2"
DURATION="${4:-30}"

# Get total video duration
TOTAL=$(ffprobe -v quiet -show_entries format=duration -of csv=p=0 "$INPUT")

# Default start: 30 seconds before end, minus title cards (~15s into terminal section)
if [[ -z "${3:-}" ]]; then
  # Find a good start point: skip title cards, grab the climactic section
  # Heuristic: start at 60% of the way through
  START=$(echo "$TOTAL * 0.6" | bc -l)
else
  START="$3"
fi

# Ensure we don't go past the end
MAX_START=$(echo "$TOTAL - $DURATION" | bc -l)
if (( $(echo "$START > $MAX_START" | bc -l) )); then
  START="$MAX_START"
fi

ffmpeg -y \
  -ss "$START" -i "$INPUT" \
  -t "$DURATION" \
  -c:v libx264 -pix_fmt yuv420p \
  -c:a aac -b:a 192k \
  "$OUTPUT" 2>/dev/null

CLIP_SIZE=$(du -h "$OUTPUT" | cut -f1)
echo "Clip: $OUTPUT (${DURATION}s from ${START}s, ${CLIP_SIZE})"
```

- [ ] **Step 2: Commit**

```bash
chmod +x demos/lib/extract-clip.sh
git add demos/lib/extract-clip.sh
git commit -m "feat(demos): 30-second clip extractor"
```

---

## Task 7: Main Orchestrator (render-demo.sh)

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
#   tapes/<demo-name>.tape     - VHS terminal recording script
#   narration/<demo-name>.md   - Narration text by section
#   titles/<demo-name>-*.txt   - Title card text files (optional)
#
# Outputs:
#   final/<demo-name>.mp4      - Full demo video
#   final/<demo-name>-clip.mp4 - 30-second highlight clip
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

# Verify inputs exist
TAPE="$DEMO_DIR/tapes/${DEMO_NAME}.tape"
NARRATION="$DEMO_DIR/narration/${DEMO_NAME}.md"

if [[ ! -f "$TAPE" ]]; then
  echo "ERROR: tape file not found: $TAPE" >&2
  exit 1
fi

if [[ ! -f "$NARRATION" ]]; then
  echo "ERROR: narration file not found: $NARRATION" >&2
  exit 1
fi

# Create output directories
RAW_DIR="$DEMO_DIR/raw"
AUDIO_DIR="$DEMO_DIR/audio/${DEMO_NAME}"
FINAL_DIR="$DEMO_DIR/final"
mkdir -p "$RAW_DIR" "$AUDIO_DIR" "$FINAL_DIR"

RAW_VIDEO="$RAW_DIR/${DEMO_NAME}.mp4"
FINAL_VIDEO="$FINAL_DIR/${DEMO_NAME}.mp4"
CLIP_VIDEO="$FINAL_DIR/${DEMO_NAME}-clip.mp4"

# --- Stage 1: Record terminal session ---
echo "[1/4] Recording terminal session..."
echo "      Tape: $TAPE"

# Detect VHS environment
if command -v vhs &>/dev/null; then
  vhs "$TAPE"
elif wsl -- bash -c "which vhs" &>/dev/null 2>&1; then
  # Convert Windows path to WSL path
  WSL_TAPE=$(wsl -- wslpath -u "$(cygpath -w "$TAPE")")
  wsl -- bash -c "cd /mnt/c/src/signals && vhs '$WSL_TAPE'"
else
  echo "ERROR: VHS not found. Install with:" >&2
  echo "  go install github.com/charmbracelet/vhs@latest" >&2
  exit 1
fi

if [[ ! -f "$RAW_VIDEO" ]]; then
  echo "ERROR: VHS did not produce output at $RAW_VIDEO" >&2
  echo "Check that the tape file Output path matches: $RAW_VIDEO" >&2
  exit 1
fi
echo "      Done: $RAW_VIDEO"
echo ""

# --- Stage 2: Generate narration audio ---
echo "[2/4] Generating narration audio..."
bash "$LIB/generate-audio.sh" "$NARRATION" "$AUDIO_DIR"
echo ""

# --- Stage 3: Composite video ---
echo "[3/4] Compositing video..."
bash "$LIB/composite-video.sh" "$DEMO_NAME" "$RAW_VIDEO" "$AUDIO_DIR" "$NARRATION" "$FINAL_VIDEO"
echo ""

# --- Stage 4: Extract 30-second clip ---
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

FULL_DURATION=$(ffprobe -v quiet -show_entries format=duration -of csv=p=0 "$FINAL_VIDEO")
CLIP_DURATION=$(ffprobe -v quiet -show_entries format=duration -of csv=p=0 "$CLIP_VIDEO")
FULL_SIZE=$(du -h "$FINAL_VIDEO" | cut -f1)
CLIP_SIZE=$(du -h "$CLIP_VIDEO" | cut -f1)

echo "  Full:  ${FULL_DURATION}s (${FULL_SIZE})"
echo "  Clip:  ${CLIP_DURATION}s (${CLIP_SIZE})"
echo ""
```

- [ ] **Step 2: Make executable and commit**

```bash
chmod +x demos/render-demo.sh
git add demos/render-demo.sh
git commit -m "feat(demos): render-demo.sh orchestrator - one command to build"
```

---

## Task 8: Author Demo 0 -- Install

The gateway video. 90 seconds. "You got a link from a colleague."

**Files:**
- Create: `demos/tapes/demo-0-install.tape`
- Create: `demos/narration/demo-0-install.md`
- Create: `demos/titles/endorsement.txt`
- Create: `demos/titles/demo-0-install-opening.txt`

- [ ] **Step 1: Write the opening frame text**

Create `demos/titles/demo-0-install-opening.txt`:
```
You got a link from a colleague.

"Try this on your next spec."
```

- [ ] **Step 2: Write the endorsement card**

Create `demos/titles/endorsement.txt`:
```
"I ran this on my actual feature spec.
 It found three issues my team missed in review."

 -- [Name], Principal PM, [Product Area]
```

Note: Replace `[Name]` and `[Product Area]` with real endorsement before Phase 2 launch.

- [ ] **Step 3: Write the VHS tape file**

Create `demos/tapes/demo-0-install.tape`:
```tape
Output demos/raw/demo-0-install.mp4
Set FontSize 14
Set Width 1400
Set Height 800
Set Theme "Catppuccin Mocha"
Set Shell "bash"
Set TypingSpeed 50ms

Require claude

# Pause for opening title card (added in post)
Sleep 1s

# Step 1: Clone and bootstrap
Type "gh repo clone gim-home/craftworks-research /tmp/cr -- --depth=1 --filter=blob:none --sparse --quiet"
Enter
Wait+Screen /\$/ 30s
Sleep 1s

Type "cd /tmp/cr && git sparse-checkout set toolkits/simlab --quiet"
Enter
Wait+Screen /\$/ 10s
Sleep 1s

Type "bash toolkits/simlab/bootstrap.sh my-simlab"
Enter
Wait+Screen /Signal simlab bootstrap/ 10s
Wait+Screen /\$/ 60s
Sleep 2s

# Step 2: Enter simlab and launch Claude Code
Type "cd ../my-simlab && claude"
Enter
Wait+Screen /claude/ 15s
Sleep 2s

# Step 3: Show what's installed
Type "/signal"
Enter
Wait+Screen /signal-health/ 30s
Sleep 3s

# Step 4: Show the namespace map
Type "/tools-preview"
Enter
Wait+Screen /validate/ 30s
Sleep 5s
```

- [ ] **Step 4: Write the narration script**

Create `demos/narration/demo-0-install.md`:
```markdown
## opening
You are a principal PM. A colleague sent you a link and said: try this on your next spec. Here is what happens in the next 90 seconds.

## clone
First, one command pulls the Signal toolkit from GitHub. This is a sparse clone -- it downloads only what you need, nothing else.

## bootstrap
The bootstrap script creates your workspace. It installs 63 skills across 9 namespaces: discover, specify, validate, simulate, and more. Each skill produces a signal -- an auditable artifact toward your feature decision.

## launch
Now we launch Claude Code inside the workspace. Signal is ready.

## show-skills
Sixty-three skills. Investigation, specification, validation, simulation -- every stage of product design, one command each.

## preview
Here is the full map. Nine namespaces covering the entire decision lifecycle. From competitive analysis to customer persona testing to support ticket prediction. This is a representative session showing how a PM sets up Signal. You are ready to run your first investigation.
```

- [ ] **Step 5: Commit**

```bash
git add demos/tapes/demo-0-install.tape demos/narration/demo-0-install.md
git add demos/titles/endorsement.txt demos/titles/demo-0-install-opening.txt
git commit -m "feat(demos): Demo 0 Install -- tape file and narration script"
```

---

## Task 9: Author Demo 3 -- Spec + Persona Test

The signature video. 3 minutes. "You wrote a spec. Before the review meeting..."

**Files:**
- Create: `demos/tapes/demo-3-persona.tape`
- Create: `demos/narration/demo-3-persona.md`
- Create: `demos/titles/demo-3-persona-opening.txt`
- Create: `demos/titles/demo-3-persona-previously.txt`

- [ ] **Step 1: Write the opening frame text**

Create `demos/titles/demo-3-persona-opening.txt`:
```
You wrote a spec. The review meeting is Thursday.

What if five different personas read it first?
```

- [ ] **Step 2: Write the "previously gathered" card**

Create `demos/titles/demo-3-persona-previously.txt`:
```
Signals gathered so far:

  discover-hypothesis: claim stated, falsification defined
  discover-competitors: 4 alternatives mapped, inertia is #1
  discover-synthesize: PROCEED with conditions

Now: validate the spec with 5 personas.
```

- [ ] **Step 3: Write the VHS tape file**

Create `demos/tapes/demo-3-persona.tape`:
```tape
Output demos/raw/demo-3-persona.mp4
Set FontSize 14
Set Width 1400
Set Height 800
Set Theme "Catppuccin Mocha"
Set Shell "bash"
Set TypingSpeed 50ms

Require claude

Sleep 1s

# PM launches Claude Code in their simlab
Type "cd /c/src/signals/simlab && claude"
Enter
Wait+Screen /claude/ 15s
Sleep 2s

# PM runs persona validation on their spec topic
Type "/validate-users api-copilot"
Enter
Wait+Screen /Persona 1/ 60s
Sleep 1s

# Wait for all 5 personas to complete
Wait+Screen /Cross-Persona/ 180s
Sleep 3s

# PM reacts to findings -- steers the AI
Type "Persona 3 raised a good point about the onboarding flow. Go deeper on that. What specifically would confuse a new user in the first 5 minutes?"
Enter
Wait+Screen /onboarding/ 60s
Sleep 2s

# PM makes a judgment call
Type "OK, the mobile PM persona is not relevant for this feature. Focus on the platform PM and the data analyst personas instead. What would they change about section 3 of the spec?"
Enter
Wait+Screen /section 3/ 60s
Sleep 3s

# PM asks for the summary
Type "Summarize the top 5 findings I should fix before Thursday's review meeting. Priority order."
Enter
Wait+Screen /Priority/ 45s
Sleep 5s
```

- [ ] **Step 4: Write the narration script**

Create `demos/narration/demo-3-persona.md`:
```markdown
## opening
You wrote a spec. The review meeting is Thursday. What if five different personas could read it first and tell you what they think? This is a representative session showing how a PM validates a spec with Signal.

## launch
The PM opens Claude Code in their Signal workspace. Three investigation signals have already been gathered for this topic -- hypothesis, competitors, and a synthesis. Now it is time to validate.

## personas-run
The validate-users skill sends the spec through five persona advocates. Each persona reads in first person and flags what confuses them, what they would change, and what they like. Watch the findings come in -- each persona sees the spec differently.

## steer-onboarding
Here is the moment that matters. The PM reads the output and makes a judgment call. Persona 3 flagged the onboarding flow. The PM decides this is worth investigating deeper and asks the AI to expand. The PM is steering, not spectating.

## steer-focus
Another judgment call. The PM decides the mobile persona is irrelevant and narrows the focus to the two personas that matter most for this feature. The AI follows the PM's direction. This is not a generic review -- it is shaped by the PM's domain knowledge.

## summary
Five personas. Twelve findings. The PM asks for the top five in priority order -- the ones to fix before Thursday. The spec improves before a single engineer reads it. No meetings were needed to get here.
```

- [ ] **Step 5: Commit**

```bash
git add demos/tapes/demo-3-persona.tape demos/narration/demo-3-persona.md
git add demos/titles/demo-3-persona-opening.txt demos/titles/demo-3-persona-previously.txt
git commit -m "feat(demos): Demo 3 Spec + Persona Test -- tape file and narration script"
```

---

## Task 10: End-to-End Test Run

Run the full pipeline on Demo 0 to verify everything works together.

**Files:**
- No new files

- [ ] **Step 1: Ensure config.env is set up**

```bash
cp demos/config.env.example demos/config.env
# Edit demos/config.env: set ELEVENLABS_API_KEY
```

- [ ] **Step 2: Run the full pipeline for Demo 0**

```bash
cd /c/src/signals
bash demos/render-demo.sh demo-0-install
```

Expected output:
```
========================================
  Demo Video Pipeline: demo-0-install
========================================

[1/4] Recording terminal session...
      Tape: demos/tapes/demo-0-install.tape
      Done: demos/raw/demo-0-install.mp4

[2/4] Generating narration audio...
  [1/6] opening...
  [2/6] clone...
  [3/6] bootstrap...
  [4/6] launch...
  [5/6] show-skills...
  [6/6] preview...

[3/4] Compositing video...
  ...speed factor, compositing details...

[4/4] Extracting 30-second clip...

========================================
  COMPLETE: demo-0-install
========================================

  Full:  demos/final/demo-0-install.mp4
  Clip:  demos/final/demo-0-install-clip.mp4
```

- [ ] **Step 3: Verify output files**

```bash
ls -la demos/final/demo-0-install*
ffprobe -v quiet -show_entries format=duration -of csv=p=0 demos/final/demo-0-install.mp4
ffprobe -v quiet -show_entries format=duration -of csv=p=0 demos/final/demo-0-install-clip.mp4
```

Check against acceptance criteria:
- Full video exists and plays
- Clip is ~30 seconds
- 1080p H.264, AAC audio
- File size under 150MB
- Subtitles visible

- [ ] **Step 4: Watch and iterate**

Open both videos:
```bash
start demos/final/demo-0-install.mp4
start demos/final/demo-0-install-clip.mp4
```

Review for:
- [ ] Opening title card displays for ~5 seconds
- [ ] Endorsement card displays for ~10-15 seconds
- [ ] Terminal text is readable at the playback speed
- [ ] Narration syncs with terminal activity
- [ ] Subtitles are present and correctly timed
- [ ] Human typing is at real speed (can read PM input)

- [ ] **Step 5: Run Demo 3 if Demo 0 passes**

```bash
bash demos/render-demo.sh demo-3-persona
```

Same verification steps as above.

- [ ] **Step 6: Commit any fixes from iteration**

```bash
git add -A demos/lib/ demos/tapes/ demos/narration/
git commit -m "fix(demos): iteration fixes from end-to-end test run"
```

---

## Task Summary

| Task | What | Depends On |
|------|------|-----------|
| 1 | Scaffolding + tool verification | -- |
| 2 | Narration parser | 1 |
| 3 | ElevenLabs TTS integration | 2 |
| 4 | Title card + subtitle generators | 1 |
| 5 | Video compositor | 2, 3, 4 |
| 6 | Clip extractor | 1 |
| 7 | Main orchestrator (render-demo.sh) | 5, 6 |
| 8 | Author Demo 0: Install | 7 |
| 9 | Author Demo 3: Spec + Persona | 7 |
| 10 | End-to-end test run | 8, 9 |

**Parallelizable:** Tasks 2+4 can run in parallel. Tasks 8+9 can run in parallel.
