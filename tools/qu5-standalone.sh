#!/usr/bin/env bash
# QU5 standalone: run simplification pass on an existing golden file
# Usage: qu5-standalone.sh <skill-id>
set -e

SKILL_ID="$1"
[ -z "$SKILL_ID" ] && echo "Usage: $0 <skill-id>" && exit 1

QUEST_DIR="C:/src/sim/simulations/quest"
TODAY=$(date +%Y-%m-%d)

# Find the latest golden file
GOLDEN_FILE=$(ls "$QUEST_DIR/golden/${SKILL_ID}-golden-"*.md 2>/dev/null | sort | tail -1)
[ -z "$GOLDEN_FILE" ] && echo "No golden file found for $SKILL_ID" && exit 1

# Find the latest rubric
RUBRIC_FILE=$(ls "$QUEST_DIR/rubrics/${SKILL_ID}-rubric-"*.md 2>/dev/null | sort | tail -1)
[ -z "$RUBRIC_FILE" ] && echo "No rubric file found for $SKILL_ID" && exit 1

RUBRIC_VERSION=$(echo "$RUBRIC_FILE" | grep -o 'v[0-9]*' | tail -1 | tr -d 'v')

echo "=== QU5 standalone: $SKILL_ID ==="
echo "  Golden:  $GOLDEN_FILE"
echo "  Rubric:  $RUBRIC_FILE (v$RUBRIC_VERSION)"

SIMPLIFIED_FILE="$QUEST_DIR/golden/${SKILL_ID}-golden-simplified-${TODAY}.md"
QU5_PROMPT_FILE=$(mktemp /tmp/qu5-prompt-XXXXXX.txt)

python -c "
import sys
skill = sys.argv[1]
rubric_v = sys.argv[2]
golden = open(sys.argv[3], encoding='utf-8', errors='replace').read()
rubric = open(sys.argv[4], encoding='utf-8', errors='replace').read()
prompt = f'''You are running QU5 -- the simplification pass for Signal skill: {skill}.

The quest loop found the COMPLETE golden prompt. Now find the MINIMAL golden prompt:
the shortest version that still passes all essential rubric criteria.

Current golden prompt file:
{golden[:4000]}

Final rubric (v{rubric_v}):
{rubric[:2000]}

Task:
1. Extract the prompt body from the golden file (inside the code block)
2. Identify every sentence or phrase doing NO work toward rubric criteria
3. Remove those sentences/phrases
4. Verify: does the simplified version still pass all essential criteria?
5. Report: word count before vs. after, what was removed and why

Goal: 20-40% word reduction with zero essential criteria lost.

Output format:
- Section: ## Simplified Prompt
  - The simplified prompt body inside a markdown code block
- Section: ## Simplification Report
  - Before word count, after word count, % reduction
  - List of what was removed and why

End with this JSON:
\`\`\`json
{{"simplified_word_count": NUMBER, "original_word_count": NUMBER, "all_essential_still_pass": true, "reduction_pct": NUMBER}}
\`\`\`'''
open(sys.argv[5], 'w').write(prompt)
" "$SKILL_ID" "$RUBRIC_VERSION" "$GOLDEN_FILE" "$RUBRIC_FILE" "$QU5_PROMPT_FILE"

claude -p "$(cat "$QU5_PROMPT_FILE")" > "$SIMPLIFIED_FILE" || {
  echo "QU5 failed for $SKILL_ID"
  rm -f "$QU5_PROMPT_FILE"
  exit 1
}
rm -f "$QU5_PROMPT_FILE"

echo "=== QU5 complete: $SKILL_ID ==="
echo "Simplified written: $SIMPLIFIED_FILE"
python -c "
import re, json
txt = open('$SIMPLIFIED_FILE').read()
m = re.search(r'\`\`\`json\s*(\{[^}]+\})\s*\`\`\`', txt, re.DOTALL)
if m:
    d = json.loads(m.group(1))
    orig = d.get('original_word_count', 0)
    simp = d.get('simplified_word_count', 0)
    pct = d.get('reduction_pct', round((1-simp/orig)*100) if orig else 0)
    print(f'  {orig} -> {simp} words ({pct}% reduction, essential_pass={d.get(\"all_essential_still_pass\")})')
else:
    wc = len(txt.split())
    print(f'  Written ({wc} words, no JSON summary found)')
"
