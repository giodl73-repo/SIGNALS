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
  > /dev/null 2>&1

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
  2>&1

# Move final output
cp "$WORK/video/output.mp4" "$OUTPUT"

FFPROBE="ffprobe"
if ! command -v "$FFPROBE" &>/dev/null; then
  FFPROBE="$(find /c/Users/*/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/ffmpeg-*/bin/ffprobe.exe 2>/dev/null | head -1)"
fi

DURATION=$("$FFPROBE" -v quiet -show_entries format=duration -of csv=p=0 "$OUTPUT" 2>/dev/null || echo "unknown")
SIZE=$(du -h "$OUTPUT" | cut -f1)
echo "  [cast-to-mp4] Done: ${DURATION}s, ${SIZE}"
