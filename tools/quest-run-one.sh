#!/bin/bash
# quest-run-one.sh -- Run the quest loop for a single skill via relay
# Usage: dispatch via relay with args: {"script":"tools/quest-run-one.sh","args":["scout-feasibility"],"cwd":"C:/src/sim"}
#
# Steps: trace check -> rubric -> variate R1 -> score R1 -> [evolve rubric] -> variate R2 -> score R2 -> golden
# Writes all artifacts to simulations/quest/ independently (P-01 concurrent by default)
# Updates signal.skills.yaml with golden: and quest_status: on completion

set -e

SKILL_ID="${1:-scout-feasibility}"
TODAY=$(date +%Y-%m-%d)
REPO="C:/src/sim"
QUEST_DIR="$REPO/simulations/quest"
TRACE_DIR="$REPO/simulations/trace/skill"
SPEC_FILE="$REPO/simulations/draft/specs/signal-scout-$TODAY.md"
MAX_ROUNDS=20  # experimental -- let the rubric discover

echo "=== quest-run-one: $SKILL_ID ==="

# ── Helpers ──────────────────────────────────────────────────────────────────

# claude_ask: write prompt to temp file, pipe via stdin to claude --print
# bypasses shell ARG_MAX / "Argument list too long" for large rubrics/variations
# Uses bash redirection directly -- avoids Python subprocess stdin issues in relay context
claude_ask() {
  local prompt="$1"
  local out_file="$2"
  local tmp_prompt
  # Use explicit POSIX path for temp file -- mktemp may return Windows paths in relay context
  tmp_prompt="/tmp/claude-ask-$$.txt"
  printf '%s' "$prompt" > "$tmp_prompt"
  claude --print < "$tmp_prompt" > "$out_file"
  local rc=$?
  rm -f "$tmp_prompt"
  return $rc
}

# ── Step 1: find trace artifact ───────────────────────────────────────────────

echo "--- Step 1: find trace artifact"
TRACE_FILE=$(ls "$TRACE_DIR"/plugin-${SKILL_ID}-*.md 2>/dev/null | head -1 || true)
if [ -n "$TRACE_FILE" ]; then
  echo "Found trace: $TRACE_FILE"
  TRACE_CONTENT=$(cat "$TRACE_FILE")
else
  echo "No trace artifact -- will use spec only"
  TRACE_CONTENT="No trace artifact available. Use the skill description and spec."
fi

# ── Step 2: load skill description from signal.skills.yaml ───────────────────

echo "--- Step 2: load skill from signal.skills.yaml"
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

# ── Step 3: generate initial rubric ──────────────────────────────────────────

echo "--- Step 3: generate rubric (v1)"
RUBRIC_FILE="$QUEST_DIR/rubrics/${SKILL_ID}-rubric-$TODAY.md"
mkdir -p "$QUEST_DIR/rubrics"

RUBRIC_PROMPT="You are running /quest:rubric for the Signal plugin skill: $SKILL_ID

Skill description:
$SKILL_DESC

Trace artifact (hand-compiled expected output -- ground truth):
${TRACE_CONTENT:0:3000}

Generate a scoring rubric with:
- 3-5 ESSENTIAL criteria (must all pass -- without these the output is not useful)
- 2-3 RECOMMENDED criteria (output is better with these)
- 1-2 ASPIRATIONAL criteria (raise the bar once essential/recommended are stable)

Each criterion needs: ID (C-01...), text, weight (essential/recommended/aspirational),
category (correctness/depth/format/coverage/behavior), and a clear pass condition.

Composite score = (essential_pass/N * 60) + (recommended_pass/N * 30) + (aspirational_pass/N * 10)
Golden threshold: all essential pass + composite >= 80.

Output as a Markdown document with frontmatter:
---
skill: quest-rubric
skill_target: $SKILL_ID
date: $TODAY
version: 1
---"

claude_ask "$RUBRIC_PROMPT" "$RUBRIC_FILE"
echo "Rubric written: $RUBRIC_FILE"

# ── Quest loop ────────────────────────────────────────────────────────────────

RUBRIC_VERSION=1
PLATEAU_COUNT=0
LAST_SCORE=0
LAST_VARIATIONS=""
LAST_SCORECARD=""

for ROUND in $(seq 1 $MAX_ROUNDS); do
  echo "--- Round $ROUND"

  # Step A: generate variations
  VARIATIONS_FILE="$QUEST_DIR/variations/${SKILL_ID}-variations-R${ROUND}-$TODAY.md"
  mkdir -p "$QUEST_DIR/variations"

  VARIATE_PROMPT="You are running /quest:variate for Signal skill: $SKILL_ID (Round $ROUND)

Skill description:
$SKILL_DESC

Current rubric (v$RUBRIC_VERSION):
$(cat "$RUBRIC_FILE" | head -80)

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

  claude_ask "$VARIATE_PROMPT" "$VARIATIONS_FILE"
  echo "Variations written: $VARIATIONS_FILE"

  # Step B: score variations
  SCORECARD_FILE="$QUEST_DIR/scorecards/${SKILL_ID}-scorecard-R${ROUND}-$TODAY.md"
  mkdir -p "$QUEST_DIR/scorecards"

  SCORE_PROMPT="You are running /quest:score for Signal skill: $SKILL_ID (Round $ROUND)

Rubric (v$RUBRIC_VERSION):
$(cat "$RUBRIC_FILE" | head -80)

Variations to score:
$(cat "$VARIATIONS_FILE" | head -200)

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

  claude_ask "$SCORE_PROMPT" "$SCORECARD_FILE"
  echo "Scorecard written: $SCORECARD_FILE"

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

  # Check dual convergence
  if [ "$ALL_ESSENTIAL" = "true" ] && [ "$NEW_PATTERNS" = "0" ]; then
    PLATEAU_COUNT=$((PLATEAU_COUNT + 1))
    echo "Plateau count: $PLATEAU_COUNT"
    if [ "$PLATEAU_COUNT" -ge 2 ]; then
      echo "DUAL CONVERGENCE at round $ROUND"
      break
    fi
  else
    PLATEAU_COUNT=0
    # Evolve rubric if new patterns found
    if [ "$NEW_PATTERNS" -gt "0" ]; then
      RUBRIC_VERSION=$((RUBRIC_VERSION + 1))
      NEW_RUBRIC_FILE="$QUEST_DIR/rubrics/${SKILL_ID}-rubric-v${RUBRIC_VERSION}-$TODAY.md"
      EVOLVE_PROMPT="You are updating a quest rubric based on excellence signals from Round $ROUND.

Current rubric (v$((RUBRIC_VERSION - 1))):
$(cat "$RUBRIC_FILE" | head -80)

Scorecard with excellence signals:
$(cat "$SCORECARD_FILE" | head -100)

Extract the new excellence patterns from the scorecard and add them as new
aspirational criteria (C-NN). Bump the rubric version to v$RUBRIC_VERSION.
Output the complete updated rubric as Markdown."

      claude_ask "$EVOLVE_PROMPT" "$NEW_RUBRIC_FILE"
      RUBRIC_FILE="$NEW_RUBRIC_FILE"
      echo "Rubric evolved to v$RUBRIC_VERSION: $NEW_RUBRIC_FILE"
    fi
  fi
done

# ── Step 3.5: QU5 simplification pass ────────────────────────────────────────

echo "--- Step 3.5: QU5 simplification (minimum viable golden prompt)"
SIMPLIFIED_FILE="$QUEST_DIR/variations/${SKILL_ID}-simplified-$TODAY.md"

# Write QU5 prompt to temp file using python to avoid heredoc/arg-length issues
QU5_PROMPT_FILE=$(mktemp /tmp/qu5-prompt-XXXXXX.txt)
VARS_CONTENT=$(cat "$LAST_VARIATIONS" | head -100)
RUBRIC_CONTENT=$(cat "$RUBRIC_FILE" | head -60)
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
  echo "QU5 failed -- skipping simplification, proceeding to golden prompt with original"
  cp "$LAST_VARIATIONS" "$SIMPLIFIED_FILE"
}
rm -f "$QU5_PROMPT_FILE"
echo "Simplification written: $SIMPLIFIED_FILE"

# Check if simplification succeeded
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

# ── Step 4: write golden prompt ───────────────────────────────────────────────

echo "--- Step 4: write golden prompt"
GOLDEN_FILE="$QUEST_DIR/golden/${SKILL_ID}-golden-$TODAY.md"
mkdir -p "$QUEST_DIR/golden"

GOLDEN_PROMPT="You are finalizing a quest run for Signal skill: $SKILL_ID

Simplification result: $SIMPLIFIED_PASS
Use the SIMPLIFIED prompt body if simplification passed. Otherwise use the winning variation.

Simplified prompt (prefer this if PASS):
$(cat "$SIMPLIFIED_FILE" | head -80)

Final scorecard (Round $ROUND):
$(cat "$LAST_SCORECARD" | head -100)

Final variations:
$(cat "$LAST_VARIATIONS" | head -150)

Final rubric (v$RUBRIC_VERSION):
$(cat "$RUBRIC_FILE" | head -80)

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

claude_ask "$GOLDEN_PROMPT" "$GOLDEN_FILE"
echo "Golden prompt written: $GOLDEN_FILE"

# ── Step 5: update signal.skills.yaml ────────────────────────────────────────

echo "--- Step 5: update signal.skills.yaml"
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
"

echo "=== quest-run-one: $SKILL_ID COMPLETE ==="
echo "Golden: $GOLDEN_FILE"
echo "Score: $LAST_SCORE, Rounds: $ROUND, Rubric: v$RUBRIC_VERSION"
