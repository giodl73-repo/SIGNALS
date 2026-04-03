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
