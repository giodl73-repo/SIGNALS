#!/bin/bash
# claude-test-batch.sh -- Same test as github-test-batch but via claude -p
# Uses installed SKILL.md files from sim-test for apples-to-apples comparison
# Usage: {"script":"tools/claude-test-batch.sh","args":["ai-code-review"],"cwd":"C:/src/sim"}

TOPIC="${1:-ai-code-review}"
TODAY=$(date +%Y-%m-%d)
REPO="C:/src/sim"
SKILLS_DIR="$REPO/../sim-test/.claude/skills"
OUTPUT_DIR="$REPO/simulations/quest/scorecards"
mkdir -p "$OUTPUT_DIR"

echo "=== claude-test-batch: topic=$TOPIC ==="
echo "Testing $(date)"

SKILLS=(
  "discover-inertia"
  "discover-hypothesis"
  "specify-proposal"
  "validate-design"
  "validate-customers"
  "simulate-state"
  "rhythm-status"
  "rhythm-decide"
  "roles-check"
  "signal-health"
  "tools-coverage"
)

PASS=0
FAIL=0
RESULTS=()

for SKILL in "${SKILLS[@]}"; do
  echo ""
  echo "--- Testing: $SKILL"

  SKILL_FILE="$SKILLS_DIR/$SKILL/SKILL.md"
  OUTPUT_FILE="$OUTPUT_DIR/claude-${SKILL}-${TOPIC}-${TODAY}.md"

  if [ ! -f "$SKILL_FILE" ]; then
    echo "  MISSING: $SKILL_FILE"
    FAIL=$((FAIL + 1))
    RESULTS+=("FAIL: $SKILL (missing SKILL.md)")
    continue
  fi

  # Extract body (after depth comments)
  TMP=$(mktemp /tmp/claude-XXXXXX.txt)
  {
    echo "You are running Signal skill /${SKILL} for topic: ${TOPIC}."
    echo ""
    awk '/# deep/{n=1;next} n{print}' "$SKILL_FILE" | sed "s/{{topic}}/${TOPIC}/g; s/{topic}/${TOPIC}/g" | tail -n +2
    echo ""
    echo "---"
    echo "After completing the skill output, append:"
    echo "QUALITY: [1-5]"
    echo "CLAUDE_COMPATIBLE: [Y/N]"
    echo "NOTES: [any issues]"
  } > "$TMP"

  echo "  Prompt: $(wc -c < "$TMP") bytes"

  claude --print < "$TMP" > "$OUTPUT_FILE" 2>&1
  EXIT=$?
  rm -f "$TMP"

  if [ $EXIT -eq 0 ] && [ -s "$OUTPUT_FILE" ]; then
    PASS=$((PASS + 1))
    QUALITY=$(grep "^QUALITY:" "$OUTPUT_FILE" | tail -1)
    RESULTS+=("PASS: $SKILL -- $QUALITY")
    echo "  PASS: $QUALITY"
  else
    FAIL=$((FAIL + 1))
    RESULTS+=("FAIL: $SKILL (exit $EXIT)")
    echo "  FAIL (exit $EXIT)"
  fi
done

echo ""
echo "=== claude-test-batch COMPLETE: $PASS passed, $FAIL failed ==="
for R in "${RESULTS[@]}"; do echo "  $R"; done

SUMMARY="$REPO/simulations/quest/scorecards/claude-batch-${TOPIC}-${TODAY}.md"
{
  echo "# Claude -p Batch Test"
  echo "Date: $TODAY | Topic: $TOPIC | Skills: $((PASS+FAIL))"
  echo "Passed: $PASS / $((PASS+FAIL))"
  echo ""
  for R in "${RESULTS[@]}"; do echo "- $R"; done
} > "$SUMMARY"
echo "Summary: $SUMMARY"
