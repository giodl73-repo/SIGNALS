#!/usr/bin/env bash
# S2-06: Confidence floor experiment
# Tests: does requiring evidence citations improve precision at cost of recall?
# Conditions: low, standard, strict (N=10 each)
set -e
SKILL="review-code"
TODAY=$(date +%Y-%m-%d)
OUT="sim/experiments/S2-06-confidence-floor/results"
mkdir -p "$OUT"

TOPIC="Signal plugin quest-run-one.sh script"
ARTIFACT="sim/tools/quest-run-one.sh"

declare -A CONFIDENCE=(
  [low]="Find all findings. You do not need to cite specific lines."
  [standard]="Find all findings. For each finding, cite the source section or line number."
  [strict]="Only include a finding if you can quote specific evidence from the artifact. If you cannot cite it, do not include it."
)

for condition in low standard strict; do
  conf_instruction="${CONFIDENCE[$condition]}"
  for run in $(seq 1 10); do
    echo "=== $condition run $run ==="
    outfile="$OUT/${condition}-run${run}-${TODAY}.md"
    
    ARTIFACT_CONTENT=$(head -100 "$ARTIFACT")
    
    prompt="You are reviewing a script for findings, bugs, and improvement opportunities.

Artifact: quest-run-one.sh (Signal plugin quest loop script)

$conf_instruction

Artifact content:
$ARTIFACT_CONTENT"
    
    tmpfile="/tmp/s206-prompt-$$.txt"
    printf '%s' "$prompt" > "$tmpfile"
    claude --print < "$tmpfile" > "$outfile"
    rm -f "$tmpfile"
    
    count=$(grep -c "^\*\*\|^- \|^[0-9]\+\." "$outfile" 2>/dev/null || echo 0)
    echo "condition=$condition run=$run findings_est=$count" >> "$OUT/summary.tsv"
  done
done
echo "=== S2-06 experiment complete ==="
