#!/usr/bin/env bash
# generate-srt.sh <durations.json> <narration.md> <output.srt>
# Generates SRT subtitles timed to audio durations.
# Splits text into ~10-word chunks.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/find-tools.sh"

DURATIONS="$1"
NARRATION="$2"
OUTPUT="$3"

SECTIONS=$("$SCRIPT_DIR/parse-narration.sh" "$NARRATION")
COUNT=$(echo "$SECTIONS" | "$JQ" length)

format_ts() {
  # Convert seconds to SRT timestamp HH:MM:SS,mmm using awk
  awk "BEGIN {
    t = $1;
    h = int(t / 3600);
    m = int((t - h*3600) / 60);
    s = int(t - h*3600 - m*60);
    ms = int((t - int(t)) * 1000);
    printf \"%02d:%02d:%02d,%03d\", h, m, s, ms;
  }"
}

SUBTITLE_NUM=1
CURRENT_TIME=0
> "$OUTPUT"

for i in $(seq 0 $((COUNT - 1))); do
  TEXT=$(echo "$SECTIONS" | "$JQ" -r ".[$i].text")
  DURATION=$("$JQ" -r ".[$i].duration_s" "$DURATIONS")

  WORDS=($TEXT)
  TOTAL_WORDS=${#WORDS[@]}
  CHUNK_SIZE=10
  NUM_CHUNKS=$(( (TOTAL_WORDS + CHUNK_SIZE - 1) / CHUNK_SIZE ))
  [[ $NUM_CHUNKS -eq 0 ]] && NUM_CHUNKS=1

  CHUNK_DURATION=$(awk "BEGIN {printf \"%.6f\", $DURATION / $NUM_CHUNKS}")

  for c in $(seq 0 $((NUM_CHUNKS - 1))); do
    START_WORD=$((c * CHUNK_SIZE))
    CHUNK_WORDS=("${WORDS[@]:$START_WORD:$CHUNK_SIZE}")
    CHUNK_TEXT="${CHUNK_WORDS[*]}"

    START_TS=$(format_ts "$CURRENT_TIME")
    CURRENT_TIME=$(awk "BEGIN {printf \"%.6f\", $CURRENT_TIME + $CHUNK_DURATION}")
    END_TS=$(format_ts "$CURRENT_TIME")

    echo "$SUBTITLE_NUM" >> "$OUTPUT"
    echo "$START_TS --> $END_TS" >> "$OUTPUT"
    echo "$CHUNK_TEXT" >> "$OUTPUT"
    echo "" >> "$OUTPUT"

    SUBTITLE_NUM=$((SUBTITLE_NUM + 1))
  done
done

echo "Subtitles: $OUTPUT ($((SUBTITLE_NUM - 1)) entries)"
