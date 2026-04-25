#!/bin/bash
# github-test-compact.sh -- Test Signal skills with --compact flag
# Tests skills that previously OOMed copilot, now with --compact mode
# Usage: {"script":"tools/github-test-compact.sh","args":["ai-code-review"],"cwd":"sim"}

TOPIC="${1:-ai-code-review}"
TODAY=$(date +%Y-%m-%d)
REPO="sim"
TEST_DIR="sim-test"
OUTPUT_DIR="$REPO/simulations/quest/scorecards"
mkdir -p "$OUTPUT_DIR"

# Skills that previously OOMed -- test with --compact added to topic
SKILLS=(
  "discover-hypothesis"
  "discover-risk"
  "discover-brainstorm"
  "discover-synthesize"
  "validate-design"
  "validate-code"
  "validate-users"
  "validate-customers"
  "simulate-lifecycle"
  "simulate-request"
  "specify-proposal"
  "roles-committee"
  "rhythm-behavior"
)

echo "=== github-test-compact: topic=$TOPIC (${#SKILLS[@]} skills) ==="
echo "Testing $(date)"

PASS=0
FAIL=0
RESULTS=()

for SKILL in "${SKILLS[@]}"; do
  echo ""
  echo "--- Testing: $SKILL --compact"
  PROMPT_FILE="$TEST_DIR/.github/prompts/${SKILL}.prompt.md"
  OUTPUT_FILE="$OUTPUT_DIR/github-${SKILL}-compact-${TOPIC}-${TODAY}.md"

  if [ ! -f "$PROMPT_FILE" ]; then
    echo "  MISSING: $PROMPT_FILE"
    FAIL=$((FAIL + 1))
    RESULTS+=("FAIL: $SKILL (missing)")
    continue
  fi

  TMP=$(mktemp /tmp/copilot-compact-XXXXXX.txt)
  {
    echo "You are running Signal skill /${SKILL} for topic: ${TOPIC}."
    echo "Use --compact mode: produce a shorter output as described in the compact instructions."
    echo ""
    awk '/^---/{n++;next} n>=2{print}' "$PROMPT_FILE" | sed "s/{{topic}}/${TOPIC}/g; s/{topic}/${TOPIC}/g"
    echo ""
    echo "---"
    echo "After completing the skill output, append:"
    echo "QUALITY: [1-5]"
    echo "COMPACT_WORKED: [Y/N]"
    echo "OUTPUT_SIZE: [small/medium/large]"
  } > "$TMP"

  echo "  Prompt: $(wc -c < "$TMP") bytes"

  cd "$TEST_DIR"
  copilot -p "$(cat "$TMP")" --yolo > "$OUTPUT_FILE" 2>&1
  STATUS=$?
  cd - > /dev/null
  rm -f "$TMP"

  if [ -s "$OUTPUT_FILE" ] && ! grep -q "FatalOOM\|node::MultiIsolatePlatform" "$OUTPUT_FILE"; then
    PASS=$((PASS + 1))
    QUALITY=$(grep "^QUALITY:" "$OUTPUT_FILE" | tail -1)
    RESULTS+=("PASS: $SKILL -- $QUALITY")
    echo "  PASS: $QUALITY"
  else
    FAIL=$((FAIL + 1))
    RESULTS+=("FAIL: $SKILL (OOM or empty)")
    echo "  FAIL"
  fi
done

echo ""
echo "=== COMPACT TEST COMPLETE: $PASS passed, $FAIL failed ==="
for R in "${RESULTS[@]}"; do echo "  $R"; done

SUMMARY="$REPO/simulations/quest/scorecards/github-compact-${TOPIC}-${TODAY}.md"
{
  echo "# GitHub Copilot Compact Mode Test"
  echo "Date: $TODAY | Topic: $TOPIC | Skills: $((PASS+FAIL))"
  echo "Passed: $PASS / $((PASS+FAIL))"
  echo ""
  for R in "${RESULTS[@]}"; do echo "- $R"; done
} > "$SUMMARY"
echo "Summary: $SUMMARY"
