#!/usr/bin/env bash
# generate-title-card.sh <text-file> <output.mp4> [duration_s]
# Renders text onto a dark background as a short mp4 clip.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DEMO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

TEXT_FILE="$1"
OUTPUT="$2"
DURATION="${3:-5}"

source "$SCRIPT_DIR/find-tools.sh"

CONFIG="$DEMO_DIR/config.env"
if [[ -f "$CONFIG" ]]; then source "$CONFIG"; fi
WIDTH="${VIDEO_WIDTH:-1400}"
HEIGHT="${VIDEO_HEIGHT:-800}"
FPS="${VIDEO_FPS:-10}"

WORK=$(mktemp -d)
trap "rm -rf $WORK" EXIT

TEXT=$(cat "$TEXT_FILE")
TOTAL_FRAMES=$((DURATION * FPS))

# Render one frame via Puppeteer
node "$SCRIPT_DIR/render-title-card.js" "$TEXT" "$WORK/frame.png" "$WIDTH" "$HEIGHT"

# Duplicate frame for duration
for i in $(seq 0 $((TOTAL_FRAMES - 1))); do
  cp "$WORK/frame.png" "$WORK/frame-$(printf '%05d' $i).png"
done

# FFmpeg: frames -> mp4
"$FFMPEG" -y \
  -framerate "$FPS" \
  -i "$WORK/frame-%05d.png" \
  -c:v libx264 -pix_fmt yuv420p -r 30 \
  "$OUTPUT" \
  2>/dev/null

echo "Title card: $OUTPUT (${DURATION}s)"
