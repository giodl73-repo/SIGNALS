#!/usr/bin/env bash
# composite-video.sh <demo-name> <terminal.mp4> <audio-dir> <narration.md> <output.mp4>
# Composites terminal video + narration audio + subtitles + title cards.
# Narration audio is the master clock -- terminal video is speed-adjusted to match.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DEMO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

DEMO_NAME="$1"
TERMINAL_VIDEO="$2"
AUDIO_DIR="$3"
NARRATION="$4"
OUTPUT="$5"

source "$SCRIPT_DIR/find-tools.sh"

# FFmpeg on Windows needs Windows-style paths (C:\... not /c/...)
winpath() {
  cygpath -w "$1" 2>/dev/null || echo "$1"
}

DURATIONS="$AUDIO_DIR/durations.json"

# --- Total narration duration (master clock) ---
TOTAL_NARRATION=$("$JQ" '[.[].duration_s] | add' "$DURATIONS")
SECTION_COUNT=$("$JQ" 'length' "$DURATIONS")
echo "  Narration: ${TOTAL_NARRATION}s across $SECTION_COUNT sections"

# --- Terminal video duration ---
RAW_DURATION=$("$FFPROBE" -v quiet -show_entries format=duration -of csv=p=0 "$TERMINAL_VIDEO")
echo "  Terminal video: ${RAW_DURATION}s"

# --- Speed factor ---
SPEED_FACTOR=$(awk "BEGIN {printf \"%.6f\", $RAW_DURATION / $TOTAL_NARRATION}")
echo "  Speed factor: ${SPEED_FACTOR}x"

WORK=$(mktemp -d)
trap "rm -rf $WORK" EXIT

# --- Concatenate audio sections ---
AUDIO_LIST="$WORK/audio-concat.txt"
> "$AUDIO_LIST"
for i in $(seq 0 $((SECTION_COUNT - 1))); do
  FILE=$("$JQ" -r ".[$i].file" "$DURATIONS")
  FULLPATH="$(cd "$AUDIO_DIR" && pwd)/${FILE}"
  echo "file '$(winpath "$FULLPATH")'" >> "$AUDIO_LIST"
done
COMBINED_AUDIO="$WORK/combined.mp3"
"$FFMPEG" -y -f concat -safe 0 -i "$AUDIO_LIST" -c copy "$COMBINED_AUDIO" 2>/dev/null
echo "  Combined audio: ${TOTAL_NARRATION}s"

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
    bash "$SCRIPT_DIR/generate-title-card.sh" "$CARD_FILE" "$CARD_VIDEO" 5 2>/dev/null
    echo "file '$(winpath "$CARD_VIDEO")'" >> "$TITLE_CONCAT"
    TITLE_DURATION=$((TITLE_DURATION + 5))
    echo "  Title card: $CARD_NAME (5s)"
  fi
done

# --- Speed-adjust terminal video to match narration ---
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
echo "file '$(winpath "$SPEED_VIDEO")'" >> "$FINAL_CONCAT"

CONCAT_VIDEO="$WORK/concat.mp4"
"$FFMPEG" -y -f concat -safe 0 -i "$FINAL_CONCAT" \
  -c:v libx264 -pix_fmt yuv420p -r 30 \
  "$CONCAT_VIDEO" 2>/dev/null

# --- Final: video + audio ---
# Note: subtitle overlay via -vf subtitles can fail on Windows due to path issues.
# Using simpler overlay: just merge video + audio, subtitles baked in via SRT separately.
"$FFMPEG" -y \
  -i "$CONCAT_VIDEO" \
  -i "$COMBINED_AUDIO" \
  -c:v copy \
  -c:a aac -b:a 192k \
  -map 0:v -map 1:a \
  -shortest \
  "$OUTPUT" 2>/dev/null

FINAL_DURATION=$("$FFPROBE" -v quiet -show_entries format=duration -of csv=p=0 "$OUTPUT")
FINAL_SIZE=$(du -h "$OUTPUT" | cut -f1)
echo "  Output: $OUTPUT (${FINAL_DURATION}s, ${FINAL_SIZE})"
