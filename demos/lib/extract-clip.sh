#!/usr/bin/env bash
# extract-clip.sh <full-video.mp4> <output-clip.mp4> [start_s] [duration_s]
# Extracts a clip. Default: 30 seconds starting at 60% through.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/find-tools.sh"

INPUT="$1"
OUTPUT="$2"
DURATION="${4:-30}"

TOTAL=$("$FFPROBE" -v quiet -show_entries format=duration -of csv=p=0 "$INPUT")

# If video is shorter than clip duration, use the whole video
SHORTER=$(awk "BEGIN {print ($TOTAL <= $DURATION) ? 1 : 0}")
if [[ "$SHORTER" == "1" ]]; then
  cp "$INPUT" "$OUTPUT"
  echo "  Clip: $OUTPUT (full video, ${TOTAL}s)"
  exit 0
fi

if [[ -z "${3:-}" ]]; then
  START=$(awk "BEGIN {printf \"%.2f\", $TOTAL * 0.6}")
else
  START="$3"
fi

MAX_START=$(awk "BEGIN {printf \"%.2f\", $TOTAL - $DURATION}")
PAST_MAX=$(awk "BEGIN {print ($START > $MAX_START) ? 1 : 0}")
if [[ "$PAST_MAX" == "1" ]]; then
  START="$MAX_START"
fi

"$FFMPEG" -y -ss "$START" -i "$INPUT" \
  -t "$DURATION" \
  -c:v libx264 -pix_fmt yuv420p \
  -c:a aac -b:a 192k \
  "$OUTPUT" 2>/dev/null

CLIP_SIZE=$(du -h "$OUTPUT" | cut -f1)
echo "  Clip: $OUTPUT (${DURATION}s from ${START}s, ${CLIP_SIZE})"
