#!/bin/bash
# quest-resume.sh -- Resume a quest loop from the best available state on disk.
# Usage: dispatch via relay with args: {"script":"tools/quest-resume.sh","args":["scout-feasibility"],"cwd":"sim"}
#
# Detects the latest rubric version and last completed scorecard round,
# then resumes from START_ROUND = last_round + 1.
# If no prior state exists, delegates to quest-run-one.sh.
#
# Key differences from quest-run-one.sh:
#   - NO set -e (failures are recoverable; retry logic handles transient errors)
#   - claude_ask() retries up to 3 times with sleep 2 between attempts
#   - Starts from detected round, not round 1
#   - Uses existing rubric files, does not regenerate rubric from scratch

SKILL_ID="${1:-scout-feasibility}"
TODAY=$(date +%Y-%m-%d)
REPO="sim"
QUEST_DIR="$REPO/simulations/quest"
TRACE_DIR="$REPO/simulations/trace/skill"
MAX_ROUNDS=20

echo "=== quest-resume: $SKILL_ID ==="

# ── Helpers ──────────────────────────────────────────────────────────────────

# claude_ask: write prompt to temp file, pipe via stdin to claude --print
# Retries up to 3 times with 2-second sleep between attempts.
claude_ask() {
  local prompt="$1"
  local out_file="$2"
  local tmp_prompt rc attempt
  tmp_prompt="/tmp/claude-ask-$$.txt"
  printf '%s' "$prompt" > "$tmp_prompt"
  attempt=0
  while [ $attempt -lt 3 ]; do
    claude --print < "$tmp_prompt" > "$out_file"
    rc=$?
    if [ $rc -eq 0 ] && [ -s "$out_file" ]; then
      rm -f "$tmp_prompt"
      return 0
    fi
    attempt=$((attempt + 1))
    echo "  retry $attempt (rc=$rc)"
    sleep 2
  done
  rm -f "$tmp_prompt"
  return 1
}

# ── Step 1: detect best available state ──────────────────────────────────────

echo "--- Step 1: detect state from disk"

# Find the latest rubric by version number (versioned files are named -vN-DATE.md)
RUBRIC_FILE=$(ls "$QUEST_DIR/rubrics/${SKILL_ID}-rubric-v"*"-"*.md 2>/dev/null | sort -V | tail -1)

# If no versioned rubric exists, try the unversioned initial rubric
if [ -z "$RUBRIC_FILE" ]; then
  RUBRIC_FILE=$(ls "$QUEST_DIR/rubrics/${SKILL_ID}-rubric-"*.md 2>/dev/null | sort -V | tail -1)
fi

if [ -z "$RUBRIC_FILE" ]; then
  echo "No rubric found for $SKILL_ID -- delegating to quest-run-one.sh"
  exec "$REPO/tools/quest-run-one.sh" "$SKILL_ID"
fi
echo "Rubric found: $RUBRIC_FILE"

# Extract rubric version number from filename (e.g. scout-feasibility-rubric-v3-2026-03-14.md -> 3)
RUBRIC_VERSION=$(python -c "
import re, sys
fname = sys.argv[1]
m = re.search(r'-rubric-v(\d+)-', fname)
if m:
    print(m.group(1))
else:
    print(1)
" "$RUBRIC_FILE" 2>/dev/null || echo "1")
echo "Rubric version: $RUBRIC_VERSION"

# Find latest scorecard by highest round number
LAST_SCORECARD=$(ls "$QUEST_DIR/scorecards/${SKILL_ID}-scorecard-R"*.md 2>/dev/null \
  | sort -V | tail -1)

if [ -z "$LAST_SCORECARD" ]; then
  echo "No scorecard found -- will start from Round 1 with existing rubric"
  LAST_ROUND=0
  LAST_VARIATIONS=""
  LAST_SCORECARD=""
else
  echo "Last scorecard: $LAST_SCORECARD"
  # Extract round number from filename (e.g. scout-feasibility-scorecard-R3-2026-03-14.md -> 3)
  LAST_ROUND=$(python -c "
import re, sys
fname = sys.argv[1]
m = re.search(r'-scorecard-R(\d+)-', fname)
if m:
    print(m.group(1))
else:
    print(0)
" "$LAST_SCORECARD" 2>/dev/null || echo "0")
  echo "Last completed round: $LAST_ROUND"

  # Find matching variations file for that round
  LAST_VARIATIONS=$(ls "$QUEST_DIR/variations/${SKILL_ID}-variations-R${LAST_ROUND}-"*.md 2>/dev/null \
    | sort -V | tail -1)
  if [ -z "$LAST_VARIATIONS" ]; then
    echo "Warning: no variations file found for R${LAST_ROUND} -- LAST_VARIATIONS unset"
  else
    echo "Matching variations: $LAST_VARIATIONS"
  fi
fi

START_ROUND=$((LAST_ROUND + 1))
echo "Resuming from Round $START_ROUND"

if [ "$START_ROUND" -gt "$MAX_ROUNDS" ]; then
  echo "Already at MAX_ROUNDS ($MAX_ROUNDS) -- nothing to resume"
  exit 0
fi

# ── Step 2: find trace artifact ───────────────────────────────────────────────

echo "--- Step 2: find trace artifact"
TRACE_FILE=$(ls "$TRACE_DIR/plugin-${SKILL_ID}-"*.md 2>/dev/null | head -1 || true)
if [ -n "$TRACE_FILE" ]; then
  echo "Found trace: $TRACE_FILE"
  TRACE_CONTENT=$(cat "$TRACE_FILE")
else
  echo "No trace artifact -- will use skill description only"
  TRACE_CONTENT="No trace artifact available. Use the skill description and spec."
fi

# ── Step 3: load skill description from signal.skills.yaml ───────────────────

echo "--- Step 3: load skill from signal.skills.yaml"
SKILL_DESC=$(python -c "
import yaml
with open('$REPO/signal.skills.yaml') as f:
    data = yaml.safe_load(f)
for s in data.get('skills', []):
    if s['id'] == '$SKILL_ID':
        print(s.get('description', 'No description found'))
        break
" 2>/dev/null || echo "Skill not found in registry")
echo "Skill description loaded (${#SKILL_DESC} chars)"

# ── Quest loop (resume from START_ROUND) ─────────────────────────────────────

PLATEAU_COUNT=0
LAST_SCORE=0
ROUND=$((START_ROUND - 1))  # will be incremented at loop entry

for ROUND in $(seq "$START_ROUND" "$MAX_ROUNDS"); do
  echo "--- Round $ROUND"

  # Step A: VARIATE -- generate variations
  VARIATIONS_FILE="$QUEST_DIR/variations/${SKILL_ID}-variations-R${ROUND}-$TODAY.md"
  mkdir -p "$QUEST_DIR/variations"

  VARIATE_PROMPT="You are running /quest:variate for Signal skill: $SKILL_ID (Round $ROUND)

Skill description:
$SKILL_DESC

Current rubric (v$RUBRIC_VERSION):
$(head -80 "$RUBRIC_FILE")

Generate 5 complete, runnable skill body prompt variations (V-01 through V-05).
Each variation is a COMPLETE prompt body -- not a diff. Single-axis variation first.
Label each with its variation axis and hypothesis.

Variation axes to explore (pick 3 for single-axis, then combine):
- Role sequence (which roles run first, what order)
- Output format (table vs prose vs list, scoring scale)
- Lifecycle emphasis (how much space per phase, how explicit boundaries are)
- Phrasing register (formal/technical vs conversational, imperative vs descriptive)
- Inertia framing (how prominently the status-quo competitor is featured)

Output as Markdown."

  if claude_ask "$VARIATE_PROMPT" "$VARIATIONS_FILE"; then
    echo "Variations written: $VARIATIONS_FILE"
  else
    echo "VARIATE failed for Round $ROUND -- skipping round"
    continue
  fi

  # Step B: SCORE -- score variations against rubric
  SCORECARD_FILE="$QUEST_DIR/scorecards/${SKILL_ID}-scorecard-R${ROUND}-$TODAY.md"
  mkdir -p "$QUEST_DIR/scorecards"

  SCORE_PROMPT="You are running /quest:score for Signal skill: $SKILL_ID (Round $ROUND)

Rubric (v$RUBRIC_VERSION):
$(head -80 "$RUBRIC_FILE")

Variations to score:
$(head -200 "$VARIATIONS_FILE")

Trace artifact (ground truth):
${TRACE_CONTENT:0:800}

For each variation (V-01 through V-05), evaluate each rubric criterion: PASS/PARTIAL/FAIL
with a brief evidence note. Compute composite score. Rank variations.

Identify EXCELLENCE SIGNALS: patterns from the top-scoring variation that made it better.

Then output EXACTLY this JSON block (no other JSON):
\`\`\`json
{\"top_score\": NUMBER, \"all_essential_pass\": BOOLEAN, \"new_patterns\": [\"pattern 1\", \"pattern 2\"]}
\`\`\`
Use empty array if no new patterns: {\"top_score\": 85, \"all_essential_pass\": true, \"new_patterns\": []}

Output as Markdown."

  if claude_ask "$SCORE_PROMPT" "$SCORECARD_FILE"; then
    echo "Scorecard written: $SCORECARD_FILE"
  else
    echo "SCORE failed for Round $ROUND -- skipping round"
    continue
  fi

  # Parse result
  TOP_SCORE=$(python -c "
import re, json, sys
txt = open('$SCORECARD_FILE').read()
m = re.search(r'\`\`\`json\s*({[^}]+})\s*\`\`\`', txt, re.DOTALL)
if m:
    d = json.loads(m.group(1))
    print(d.get('top_score', 0))
else:
    print(0)
" 2>/dev/null || echo "0")

  ALL_ESSENTIAL=$(python -c "
import re, json
txt = open('$SCORECARD_FILE').read()
m = re.search(r'\`\`\`json\s*({[^}]+})\s*\`\`\`', txt, re.DOTALL)
if m:
    d = json.loads(m.group(1))
    print('true' if d.get('all_essential_pass', False) else 'false')
else:
    print('false')
" 2>/dev/null || echo "false")

  NEW_PATTERNS=$(python -c "
import re, json
txt = open('$SCORECARD_FILE').read()
m = re.search(r'\`\`\`json\s*({[^}]+})\s*\`\`\`', txt, re.DOTALL)
if m:
    d = json.loads(m.group(1))
    patterns = d.get('new_patterns', [])
    print(len(patterns))
else:
    print(0)
" 2>/dev/null || echo "0")

  echo "R${ROUND}: score=$TOP_SCORE essential=$ALL_ESSENTIAL new_patterns=$NEW_PATTERNS"
  LAST_SCORE=$TOP_SCORE
  LAST_VARIATIONS="$VARIATIONS_FILE"
  LAST_SCORECARD="$SCORECARD_FILE"

  # DUAL CONVERGENCE check
  if [ "$ALL_ESSENTIAL" = "true" ] && [ "$NEW_PATTERNS" = "0" ]; then
    PLATEAU_COUNT=$((PLATEAU_COUNT + 1))
    echo "Plateau count: $PLATEAU_COUNT"
    if [ "$PLATEAU_COUNT" -ge 2 ]; then
      echo "DUAL CONVERGENCE at round $ROUND"
      break
    fi
  else
    PLATEAU_COUNT=0
    # EVOLVE -- evolve rubric if new patterns found
    if [ "$NEW_PATTERNS" -gt "0" ]; then
      RUBRIC_VERSION=$((RUBRIC_VERSION + 1))
      NEW_RUBRIC_FILE="$QUEST_DIR/rubrics/${SKILL_ID}-rubric-v${RUBRIC_VERSION}-$TODAY.md"
      EVOLVE_PROMPT="You are updating a quest rubric based on excellence signals from Round $ROUND.

Current rubric (v$((RUBRIC_VERSION - 1))):
$(head -80 "$RUBRIC_FILE")

Scorecard with excellence signals:
$(head -100 "$SCORECARD_FILE")

Extract the new excellence patterns from the scorecard and add them as new
aspirational criteria (C-NN). Bump the rubric version to v$RUBRIC_VERSION.
Output the complete updated rubric as Markdown."

      if claude_ask "$EVOLVE_PROMPT" "$NEW_RUBRIC_FILE"; then
        RUBRIC_FILE="$NEW_RUBRIC_FILE"
        echo "Rubric evolved to v$RUBRIC_VERSION: $NEW_RUBRIC_FILE"
      else
        echo "EVOLVE failed -- continuing with rubric v$((RUBRIC_VERSION - 1))"
        RUBRIC_VERSION=$((RUBRIC_VERSION - 1))
      fi
    fi
  fi
done

# Guard: if loop never ran (START_ROUND > MAX_ROUNDS handled above, but be safe)
if [ -z "$LAST_VARIATIONS" ]; then
  echo "No rounds completed -- cannot write golden prompt"
  exit 1
fi

# ── QU5: simplification pass ──────────────────────────────────────────────────

echo "--- QU5: simplification (minimum viable golden prompt)"
SIMPLIFIED_FILE="$QUEST_DIR/variations/${SKILL_ID}-simplified-$TODAY.md"

QU5_PROMPT_FILE=$(mktemp /tmp/qu5-prompt-XXXXXX.txt)
python -c "
import sys
skill = sys.argv[1]
rubric_v = sys.argv[2]
variations = open(sys.argv[3]).read()
rubric = open(sys.argv[4]).read()
prompt = f'''You are running QU5 -- the simplification pass for Signal skill: {skill}.

The quest loop found the COMPLETE golden prompt. Now find the MINIMAL golden prompt:
the shortest version that still passes all essential rubric criteria.

Winning variation (the complete golden prompt):
{variations[:3000]}

Final rubric (v{rubric_v}):
{rubric[:2000]}

Task:
1. Identify every sentence or phrase in the winning prompt that is doing NO work
2. Remove those sentences/phrases
3. Verify: does the simplified version still pass all essential criteria? YES/NO
4. Report: word count before vs. after, what was removed and why

Goal: 20-40% word reduction with zero essential criteria lost.
Output the simplified prompt body and the simplification report.

End with this JSON:
\`\`\`json
{{\"simplified_word_count\": NUMBER, \"original_word_count\": NUMBER, \"all_essential_still_pass\": BOOLEAN}}
\`\`\`'''
open(sys.argv[5], 'w').write(prompt)
" "$SKILL_ID" "$RUBRIC_VERSION" "$LAST_VARIATIONS" "$RUBRIC_FILE" "$QU5_PROMPT_FILE"

claude --print < "$QU5_PROMPT_FILE" > "$SIMPLIFIED_FILE" || {
  echo "QU5 failed -- skipping simplification, proceeding with original variations"
  cp "$LAST_VARIATIONS" "$SIMPLIFIED_FILE"
}
rm -f "$QU5_PROMPT_FILE"
echo "Simplification written: $SIMPLIFIED_FILE"

SIMPLIFIED_PASS=$(python -c "
import re, json
txt = open('$SIMPLIFIED_FILE').read()
m = re.search(r'\`\`\`json\s*({[^}]+})\s*\`\`\`', txt, re.DOTALL)
if m:
    d = json.loads(m.group(1))
    if d.get('all_essential_still_pass', False):
        orig = d.get('original_word_count', 0)
        simp = d.get('simplified_word_count', 0)
        pct = round((1 - simp/orig) * 100) if orig > 0 else 0
        print(f'PASS ({pct}% reduction)')
    else:
        print('FAIL (essential criteria lost -- use original)')
else:
    print('PARSE_FAILED (use original)')
" 2>/dev/null || echo "UNKNOWN")
echo "Simplification: $SIMPLIFIED_PASS"

# ── GOLDEN: write golden prompt ───────────────────────────────────────────────

echo "--- GOLDEN: write golden prompt"
GOLDEN_FILE="$QUEST_DIR/golden/${SKILL_ID}-golden-$TODAY.md"
mkdir -p "$QUEST_DIR/golden"

GOLDEN_PROMPT="You are finalizing a quest run for Signal skill: $SKILL_ID

Simplification result: $SIMPLIFIED_PASS
Use the SIMPLIFIED prompt body if simplification passed. Otherwise use the winning variation.

Simplified prompt (prefer this if PASS):
$(head -80 "$SIMPLIFIED_FILE")

Final scorecard (Round $ROUND):
$(head -100 "$LAST_SCORECARD")

Final variations:
$(head -150 "$LAST_VARIATIONS")

Final rubric (v$RUBRIC_VERSION):
$(head -80 "$RUBRIC_FILE")

Extract the GOLDEN PROMPT -- the winning variation body.
Write the golden prompt document with:

1. Frontmatter:
---
skill: quest-golden
skill_target: $SKILL_ID
date: $TODAY
rounds: $ROUND
rubric_final: ${RUBRIC_FILE##*/}
score: $LAST_SCORE
status: GOLDEN
---

2. The exact winning prompt body (copy it verbatim from the variations)
3. 'What made it golden' -- 3-5 key patterns that distinguish it from the baseline V-01
4. Final rubric criteria summary

Output as Markdown."

if claude_ask "$GOLDEN_PROMPT" "$GOLDEN_FILE"; then
  echo "Golden prompt written: $GOLDEN_FILE"
else
  echo "GOLDEN step failed"
fi

# ── Update signal.skills.yaml ─────────────────────────────────────────────────

echo "--- Update signal.skills.yaml"
python -c "
import yaml, re
from pathlib import Path

yaml_file = '$REPO/signal.skills.yaml'
with open(yaml_file) as f:
    data = yaml.safe_load(f)

for skill in data.get('skills', []):
    if skill['id'] == '$SKILL_ID':
        skill['golden'] = 'simulations/quest/golden/${SKILL_ID}-golden-$TODAY.md'
        skill['rubric'] = 'simulations/quest/rubrics/' + Path('$RUBRIC_FILE').name
        skill['quest_status'] = 'GOLDEN (Round $ROUND, score $LAST_SCORE)'
        break

with open(yaml_file, 'w') as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

print('signal.skills.yaml updated')
" || echo "signal.skills.yaml update failed (non-fatal)"

echo "=== quest-resume: $SKILL_ID COMPLETE ==="
echo "Golden: $GOLDEN_FILE"
echo "Score: $LAST_SCORE, Rounds completed from $START_ROUND to $ROUND, Rubric: v$RUBRIC_VERSION"
