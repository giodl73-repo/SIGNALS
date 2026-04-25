#!/bin/bash
# github-test-batch.sh -- Test Signal .prompt.md files via copilot -p relay
# Usage: {"script":"tools/github-test-batch.sh","args":["ai-code-review","G1"],"cwd":"sim"}
# Second arg selects group: G1=discover, G2=specify+validate, G3=simulate+rhythm, G4=roles+tools, ALL=everything

TOPIC="${1:-ai-code-review}"
GROUP="${2:-ALL}"
TODAY=$(date +%Y-%m-%d)
REPO="sim"

# Skill groups
G1=(discover-competitors discover-competitors-alt discover-inertia discover-feasibility
    discover-feasibility-alt discover-hypothesis discover-risk discover-brainstorm
    discover-analysis discover-synthesize discover-websearch discover-orchestrate
    discover-causal discover-coherence discover-compare)

G2=(specify-spec specify-proposal specify-pitch specify-commitment
    validate-design validate-code validate-users validate-customers
    validate-adoption validate-adoption-blocker validate-feedback validate-support)

G3=(simulate-lifecycle simulate-request simulate-state simulate-contract
    simulate-conversation simulate-permissions simulate-stress
    rhythm-status rhythm-story rhythm-decide rhythm-behavior rhythm-qa rhythm-brief achievements)

G4=(roles-scan roles-build roles-chart roles-generate roles-create roles-check
    roles-committee roles-product-review roles-pull-request roles-leaderboard
    signal signal-health signal-layout signal-setup
    tools-accept tools-coverage tools-preview)

case "$GROUP" in
  G1) SKILLS=("${G1[@]}") ;;
  G2) SKILLS=("${G2[@]}") ;;
  G3) SKILLS=("${G3[@]}") ;;
  G4) SKILLS=("${G4[@]}") ;;
  *)  SKILLS=("${G1[@]}" "${G2[@]}" "${G3[@]}" "${G4[@]}") ;;
esac

echo "=== github-test-batch: group=$GROUP topic=$TOPIC (${#SKILLS[@]} skills) ==="
echo "Testing $(date)"

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

SUMMARY="$REPO/simulations/quest/scorecards/github-batch-${GROUP}-${TOPIC}-${TODAY}.md"
{
  echo "# GitHub Copilot Batch — $GROUP"
  echo "Date: $TODAY | Topic: $TOPIC | Skills: $((PASS+FAIL))"
  echo "Passed: $PASS / $((PASS+FAIL))"
  echo ""
  for R in "${RESULTS[@]}"; do echo "- $R"; done
} > "$SUMMARY"
echo "Summary: $SUMMARY"
