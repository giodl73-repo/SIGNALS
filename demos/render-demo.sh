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
