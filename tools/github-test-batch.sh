#!/bin/bash
# github-test-batch.sh -- Test Signal .prompt.md files via copilot -p relay
# Usage: {"script":"tools/github-test-batch.sh","args":["ai-code-review"],"cwd":"C:/src/sim"}

TOPIC="${1:-ai-code-review}"
TODAY=$(date +%Y-%m-%d)
REPO="C:/src/sim"

echo "=== github-test-batch: topic=$TOPIC ==="
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
  if bash "$REPO/tools/github-test-one.sh" "$SKILL" "$TOPIC" 2>&1; then
    PASS=$((PASS + 1))
    RESULTS+=("PASS: $SKILL")
  else
    FAIL=$((FAIL + 1))
    RESULTS+=("FAIL: $SKILL")
    echo "  FAIL (continuing)"
  fi
done

echo ""
echo "=== COMPLETE: $PASS passed, $FAIL failed ==="
for R in "${RESULTS[@]}"; do echo "  $R"; done

SUMMARY="$REPO/simulations/quest/scorecards/github-batch-${TOPIC}-${TODAY}.md"
{
  echo "# GitHub Copilot Batch Test"
  echo "Date: $TODAY | Topic: $TOPIC | Skills: $((PASS+FAIL))"
  echo "Passed: $PASS / $((PASS+FAIL))"
  echo ""
  for R in "${RESULTS[@]}"; do echo "- $R"; done
} > "$SUMMARY"
echo "Summary: $SUMMARY"
