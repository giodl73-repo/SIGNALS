#!/usr/bin/env bash
# S2-04: Floor variation experiment
# Tests: does output quantity scale with stated minimum floor?
# Conditions: no-floor, floor-5, floor-10, floor-15, floor-20 (N=5 each)
set -e
SKILL="scout-competitors"
TODAY=$(date +%Y-%m-%d)
OUT="sim/experiments/S2-04-floor-variation/results"
mkdir -p "$OUT"

TOPIC="Signal plugin for Claude Code — a developer tool for feature decision-making"

declare -A FLOORS=(
  [no-floor]="Find all competitive threats and findings."
  [floor-5]="Find all competitive threats and findings. Include at least 5 findings."
  [floor-10]="Find all competitive threats and findings. Include at least 10 findings."
  [floor-15]="Find all competitive threats and findings. Include at least 15 findings."
  [floor-20]="Find all competitive threats and findings. Include at least 20 findings."
)

for condition in no-floor floor-5 floor-10 floor-15 floor-20; do
  floor_instruction="${FLOORS[$condition]}"
  for run in 1 2 3 4 5; do
    echo "=== $condition run $run ==="
    outfile="$OUT/${condition}-run${run}-${TODAY}.md"
    
    # Build prompt using golden skill + floor instruction
    GOLDEN=$(cat "sim/simulations/quest/golden/scout-competitors-golden-2026-03-14.md" | head -60)
    
    prompt="Topic: $TOPIC

$floor_instruction

$GOLDEN"
    
    tmpfile="/tmp/s204-prompt-$$.txt"
    printf '%s' "$prompt" > "$tmpfile"
    claude --print < "$tmpfile" > "$outfile"
    rm -f "$tmpfile"
    
    # Count findings
    count=$(grep -c "^- \|^[0-9]\+\.\|^##\|FINDING\|finding" "$outfile" 2>/dev/null || echo 0)
    echo "  findings estimate: $count"
    echo "condition=$condition run=$run findings=$count" >> "$OUT/summary.tsv"
  done
done
echo "=== S2-04 experiment complete ==="
