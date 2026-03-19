#!/bin/bash
# github-test-one.sh -- Test a Signal .prompt.md via copilot -p relay
# Usage: {"script":"tools/github-test-one.sh","args":["discover-competitors","ai-code-review"],"cwd":"C:/src/sim"}

set -e
SKILL_ID="${1:-discover-competitors}"
TOPIC="${2:-payment-reminders}"
TODAY=$(date +%Y-%m-%d)
REPO="C:/src/sim"
PROMPT_DIR="$REPO/../sim-test/.github/prompts"
OUTPUT_DIR="$REPO/simulations/quest/scorecards"
mkdir -p "$OUTPUT_DIR"

PROMPT_FILE="$PROMPT_DIR/${SKILL_ID}.prompt.md"
OUTPUT_FILE="$OUTPUT_DIR/github-${SKILL_ID}-${TOPIC}-${TODAY}.md"

echo "=== github-test-one: $SKILL_ID / $TOPIC ==="

if [ ! -f "$PROMPT_FILE" ]; then
  echo "ERROR: prompt file not found: $PROMPT_FILE"; exit 1
fi

# Extract body (skip frontmatter), substitute topic
TMP=$(mktemp /tmp/copilot-XXXXXX.txt)

{
  echo "You are running Signal skill /${SKILL_ID} for topic: ${TOPIC}."
  echo ""
  awk '/^---/{n++;next} n>=2{print}' "$PROMPT_FILE" | sed "s/{{topic}}/${TOPIC}/g; s/{topic}/${TOPIC}/g"
  echo ""
  echo "---"
  echo "After completing the skill output, append:"
  echo "QUALITY: [1-5]"
  echo "COPILOT_COMPATIBLE: [Y/N]"
  echo "NOTES: [any Copilot-specific issues vs Claude Code]"
} > "$TMP"

echo "Prompt: $(wc -c < "$TMP") bytes, $(wc -l < "$TMP") lines"

# Use stdin redirect like claude-run.py does
copilot -p "$(cat "$TMP")" --yolo > "$OUTPUT_FILE" 2>&1
STATUS=$?

rm -f "$TMP"

if [ -s "$OUTPUT_FILE" ]; then
  echo "Output: $OUTPUT_FILE ($(wc -l < "$OUTPUT_FILE") lines)"
  echo "Quality: $(grep "^QUALITY:" "$OUTPUT_FILE" | tail -1)"
  echo "Copilot-compatible: $(grep "^COPILOT_COMPATIBLE:" "$OUTPUT_FILE" | tail -1)"
else
  echo "ERROR: empty output"
  exit 1
fi

echo "=== github-test-one: $SKILL_ID COMPLETE (exit $STATUS) ==="
