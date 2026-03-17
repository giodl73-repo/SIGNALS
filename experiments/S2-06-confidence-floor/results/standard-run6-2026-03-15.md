Here are all findings, organized by severity:

---

## Bugs

**F-01 — `SPEC_FILE` hardcodes `scout` regardless of `SKILL_ID` (line 16)**
```bash
SPEC_FILE="$REPO/simulations/draft/specs/signal-scout-$TODAY.md"
```
Path bakes in `scout` unconditionally. For any non-scout skill this is wrong. The variable is also never read anywhere in the script — dead and wrong.

---

**F-02 — Shell injection in Python inline script (lines 54–62)**
```bash
SKILL_DESC=$(python -c "
...
    if s['id'] == '$SKILL_ID':
```
`$SKILL_ID` is interpolated bare into the Python string literal. A value like `scout']; import os; os.system('...')  #` would break or exploit this. Minimal fix: pass as `sys.argv[1]` like the QU5 block does on lines 253–284.

---

**F-03 — `mktemp` used in QU5 block but avoided in `claude_ask` for the same reason (lines 31 vs 250)**
```bash
# claude_ask (line 31) — avoids mktemp, citing Windows relay path issue
tmp_prompt="/tmp/claude-ask-$$.txt"

# QU5 block (line 250) — uses mktemp anyway
QU5_PROMPT_FILE=$(mktemp /tmp/qu5-prompt-XXXXXX.txt)
```
The two code paths contradict each other. If `mktemp` returns Windows-style paths in relay context, the QU5 block fails for the same reason `claude_ask` is written to avoid it.

---

**F-04 — Dead variables `VARS_CONTENT` and `RUBRIC_CONTENT` (lines 251–252)**
```bash
VARS_CONTENT=$(cat "$LAST_VARIATIONS" | head -100)
RUBRIC_CONTENT=$(cat "$RUBRIC_FILE" | head -60)
```
Both are assigned but never referenced. The Python subprocess reads the files directly via `sys.argv[3]` and `sys.argv[4]`. These lines are leftover scaffolding.

---

## Correctness Issues

**F-05 — Missing `set -o pipefail` (line 9)**
```bash
set -e
```
Without `pipefail`, a failing left side of a pipe (e.g., `cat "$RUBRIC_FILE" | head -80` when the file doesn't exist) exits zero because `head` succeeds on EOF. Errors in piped subcommands are silently swallowed throughout the script.

---

**F-06 — JSON regex `[^}]+` breaks on arrays or nested values (line 175, 186, 197, 297)**
```python
m = re.search(r'```json\s*({[^}]+})\s*```', txt, re.DOTALL)
```
`[^}]` stops at the first `}`. The expected JSON includes an array field `"new_patterns": ["pattern 1", "pattern 2"]` — array elements don't contain `}`, but if any string value ever does (or if the schema grows a nested object), the match silently falls through to the `else: print(0)` fallback with no warning. A safer pattern: `\{.*?\}` with `re.DOTALL`, or proper JSON extraction via `re.search(r'```json\s*([\s\S]*?)\s*```', ...)` then `json.loads`.

---

**F-07 — Three separate file reads to parse the same scorecard (lines 172–204)**
```bash
TOP_SCORE=$(python -c "...open('$SCORECARD_FILE')..." || echo "0")
ALL_ESSENTIAL=$(python -c "...open('$SCORECARD_FILE')..." || echo "false")
NEW_PATTERNS=$(python -c "...open('$SCORECARD_FILE')..." || echo "0")
```
Each invocation re-reads and re-parses independently. If one parse fails and falls to its `|| echo` default, the three variables will reflect inconsistent state (e.g., `ALL_ESSENTIAL=true`, `NEW_PATTERNS=0`, `TOP_SCORE=0`) with no indication that parsing failed. All three should come from one Python call.

---

**F-08 — No convergence vs. timeout distinction in final output (line 384)**
```bash
echo "Score: $LAST_SCORE, Rounds: $ROUND, Rubric: v$RUBRIC_VERSION"
```
Whether the loop converged at round 3 or exhausted all 20 rounds, the output is identical. The golden frontmatter (`status: GOLDEN`) is also unconditional. A non-converged run should carry a different status (e.g., `TIMEOUT`) or at minimum a warning.

---

**F-09 — Arbitrary `head -N` line truncation may cut rubric mid-criterion (lines 122, 147, 228, 231, 324–333)**
```bash
$(cat "$RUBRIC_FILE" | head -80)
```
Line-count truncation of structured Markdown (rubric criteria, scorecard tables) will silently drop trailing criteria. The model in the evolve and score prompts may then produce rubrics with missing criteria without knowing content was cut. These should be character/token budgets or, better, the full file since it's being passed to `claude` anyway.

---

## Minor / Style

**F-10 — Useless use of `cat` throughout (lines 122, 147, 228, 231, 251, 252, 324–333)**
```bash
$(cat "$FILE" | head -N)   # should be: $(head -N "$FILE")
```
`cat file | head` forks an extra process unnecessarily. Appears 8+ times.

---

**F-11 — Step numbering is inconsistent (section headers)**
The loop body has no step label in its `echo` output. "Step 3.5" is non-standard. The original header comment (`Steps: trace check -> rubric -> ...`) doesn't map cleanly to the code's step labels. The echo for the QU5 block reads `--- Step 3.5:` rather than a sequential step number.

---

**F-12 — `SKILL_ID` not validated (line 11)**
No check that `$1` is a legal skill ID (alphanumeric + hyphen). A value containing `/`, `..`, or spaces would produce malformed paths silently since `set -e` won't catch a `mkdir -p` that succeeds on a garbled path.

---

**Summary table**

| ID | Line(s) | Severity | Category |
|----|---------|----------|----------|
| F-01 | 16 | Bug | Wrong path / dead variable |
| F-02 | 54–62 | Bug | Shell injection |
| F-03 | 31 vs 250 | Bug | mktemp inconsistency |
| F-04 | 251–252 | Bug | Dead variables |
| F-05 | 9 | Correctness | Missing pipefail |
| F-06 | 175, 186, 197, 297 | Correctness | Regex fragility |
| F-07 | 172–204 | Correctness | Triple parse / inconsistent state |
| F-08 | 384 | Correctness | No convergence signal |
| F-09 | 122, 147, 228, 231, 324–333 | Correctness | Silent content truncation |
| F-10 | multiple | Style | Useless cat |
| F-11 | section headers | Style | Step numbering |
| F-12 | 11 | Minor | No input validation |
