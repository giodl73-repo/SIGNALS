#!/usr/bin/env bash
# generate-audio.sh <narration.md> <output-dir>
# Generates one mp3 per narration section via Edge TTS (free, no API key).
# Writes durations.json with per-section timing.
#
# Requires: edge-tts (pip install edge-tts), ffprobe

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
NARRATION="$1"
OUTPUT_DIR="$2"

source "$SCRIPT_DIR/find-tools.sh"

# Voice selection -- Microsoft neural voices, no API key needed
VOICE="${TTS_VOICE:-en-US-GuyNeural}"

mkdir -p "$OUTPUT_DIR"

SECTIONS=$("$SCRIPT_DIR/parse-narration.sh" "$NARRATION")
COUNT=$(echo "$SECTIONS" | "$JQ" length)

echo "  Generating audio for $COUNT sections (voice: $VOICE)..."

DURATIONS="["
FIRST=true

for i in $(seq 0 $((COUNT - 1))); do
  NAME=$(echo "$SECTIONS" | "$JQ" -r ".[$i].name")
  TEXT=$(echo "$SECTIONS" | "$JQ" -r ".[$i].text")
  OUTFILE="$OUTPUT_DIR/${NAME}.mp3"

  echo "    [$((i+1))/$COUNT] $NAME..."

  # Edge TTS -- free Microsoft neural TTS
  edge-tts --text "$TEXT" --voice "$VOICE" --write-media "$OUTFILE" 2>/dev/null

  if [[ ! -f "$OUTFILE" ]]; then
    echo "ERROR: edge-tts failed for section '$NAME'" >&2
    exit 1
  fi

  DURATION=$("$FFPROBE" -v quiet -show_entries format=duration -of csv=p=0 "$OUTFILE")

  [[ "$FIRST" == "true" ]] && FIRST=false || DURATIONS="${DURATIONS},"
  DURATIONS="${DURATIONS}{\"name\":\"${NAME}\",\"file\":\"${NAME}.mp3\",\"duration_s\":${DURATION}}"
done

DURATIONS="${DURATIONS}]"
echo "$DURATIONS" | "$JQ" . > "$OUTPUT_DIR/durations.json"

TOTAL=$(echo "$DURATIONS" | "$JQ" '[.[].duration_s] | add')
echo "  Audio complete. Total: ${TOTAL}s"
