Here are all findings, organized by type:

---

## Findings: quest-run-one.sh

---

### F-01 — Dead variable: `SPEC_FILE` defined but never used
**Line 16**
`SPEC_FILE` is assigned but referenced nowhere in the script. Either it's a leftover from a prior design or it was meant to be passed into a prompt. As-is it's pure noise.

---

### F-02 — Dead variables: `VARS_CONTENT` and `RUBRIC_CONTENT`
**Lines 251–252**
Both are assigned via `cat | head` but never referenced. The Python subprocess on lines 253–284 reads `$LAST_VARIATIONS` and `$RUBRIC_FILE` directly via `sys.argv`. These two lines can be deleted.

---

### F-03 — Temp file leak on `claude_ask` failure
**Lines 33–36** (inside `claude_ask`)
With `set -e` active, if `claude --print` exits non-zero, the script terminates before `rm -f "$tmp_prompt"` on line 35. The temp file at `/tmp/claude-ask-$$.txt` leaks. Fix with a `trap`:
```bash
trap 'rm -f "$tmp_prompt"' EXIT
```
inside the function scope, or use `trap` at the script level for all temp files.

---

### F-04 — Shell injection via `$SKILL_ID` in Python `-c` source code
**Lines 54–62** (Step 2 Python inline)
```bash
SKILL_DESC=$(python -c "
...
    if s['id'] == '$SKILL_ID':
```
`$SKILL_ID` is interpolated into Python source code inside a double-quoted bash string. A SKILL_ID containing `'` breaks Python parsing; one with `'; import os; os.system(...)#` achieves code injection. Fix: pass SKILL_ID as `sys.argv[1]` — as the QU5 block on line 284 already does correctly.

---

### F-05 — Command substitutions in prompt strings expand content from YAML/files
**Lines 71–96, 116–135, 144–166, 225–235, 318–353**
All major prompt variables are built with double-quoted strings containing `$(cat ...)`. Any content loaded from `$SKILL_DESC`, `$TRACE_CONTENT`, or the rubric/variations files that contains backticks or `$(...)` will be shell-expanded before assignment. This is an injection vector for anyone who controls the YAML or any artifact on disk. The QU5 block avoids this by writing through Python — the other prompts should do the same or use `printf` with `%s`.

---

### F-06 — `set -e` without `set -o pipefail`
**Line 9**
```bash
set -e
```
Pipeline failures (e.g., `cat "$RUBRIC_FILE" | head -80` where `cat` fails) won't trigger script exit. Add `set -o pipefail`. While `set -u` for unbound variables would also help, many variables here are intentionally conditional.

---

### F-07 — Useless use of `cat` in 14+ command substitutions
**Lines 122, 147, 148, 150, 228, 230, 251, 252, 324, 327, 329, 331, 333, 251, 252**
Pattern: `$(cat "$FILE" | head -N)`. Should be `$(head -N "$FILE")`. Minor but consistent throughout.

---

### F-08 — `ls` for glob is fragile
**Line 42**
```bash
TRACE_FILE=$(ls "$TRACE_DIR"/plugin-${SKILL_ID}-*.md 2>/dev/null | head -1 || true)
```
`ls` output breaks on filenames with spaces. Also picks the first alphabetically, not the most recent. Use:
```bash
TRACE_FILE=$(find "$TRACE_DIR" -name "plugin-${SKILL_ID}-*.md" -printf '%T@ %p\n' 2>/dev/null | sort -rn | head -1 | cut -d' ' -f2- || true)
```
or a bash glob:
```bash
files=("$TRACE_DIR"/plugin-${SKILL_ID}-*.md)
TRACE_FILE="${files[0]}"
```

---

### F-09 — Three separate Python processes parse the same file
**Lines 172–204**
`$SCORECARD_FILE` is opened, regex-searched, and JSON-parsed three times in sequence to extract `top_score`, `all_essential_pass`, and `new_patterns`. This runs three Python interpreter startups per round, 20 rounds maximum. A single Python call extracting all three values would be cleaner and faster.

---

### F-10 — Inconsistent trace content truncation limits
**Lines 77 vs 153**
Rubric generation gets `${TRACE_CONTENT:0:3000}` (3000 chars). Scoring gets `${TRACE_CONTENT:0:800}` (800 chars). The scorer is grading variations against ground truth with 73% less trace context than the rubric writer used to define the criteria. If the rubric writer derived criteria from content in chars 801–3000 of the trace, the scorer will silently miss them.

---

### F-11 — Rubric truncated to 80 lines in scoring and evolution contexts
**Lines 147, 228**
`$(cat "$RUBRIC_FILE" | head -80)` is used in both the score prompt and the evolve prompt. A rubric with detailed pass conditions, examples, or commentary can easily exceed 80 lines. Truncated rubric in the scorer means criteria at the end are not evaluated — the resulting scores are silently wrong.

---

### F-12 — Stagnation path: no escape when `ALL_ESSENTIAL=false` and `NEW_PATTERNS=0`
**Lines 219–241**
The `else` branch fires when the plateau condition is not met. Inside it, rubric evolution only triggers when `NEW_PATTERNS > 0`. If `ALL_ESSENTIAL=false` and `NEW_PATTERNS=0`, nothing evolves and the loop re-runs with identical rubric and no new signal — guaranteed stagnation for the remaining rounds. Add a secondary evolution trigger when essential criteria fail for N consecutive rounds.

---

### F-13 — `mktemp` usage inconsistency
**Line 31 vs line 250**
`claude_ask` avoids `mktemp` explicitly (comment on line 30: "mktemp may return Windows paths in relay context") and uses `/tmp/claude-ask-$$.txt` instead. The QU5 block on line 250 uses `mktemp /tmp/qu5-prompt-XXXXXX.txt`. If the Windows-path concern is real, line 250 is affected by the same issue. Pick one approach and use it everywhere.

---

### F-14 — `status: GOLDEN` is hardcoded regardless of exit condition
**Line 346**
```yaml
status: GOLDEN
```
Both early convergence (dual plateau) and max-round timeout produce `status: GOLDEN`. A skill that hit `MAX_ROUNDS=20` without converging should be marked differently (e.g., `TIMED_OUT` or `PARTIAL`). The round count in frontmatter (`rounds: $ROUND`) hints at this but `status` gives no signal.

---

### F-15 — `yaml.dump` drops all comments from `signal.skills.yaml`
**Lines 376–378**
PyYAML's `yaml.safe_load` + `yaml.dump` round-trip discards all comments. If `signal.skills.yaml` has inline comments (which YAML files in this project often do), they're silently lost on every quest completion. Consider a line-targeted `sed` update or use `ruamel.yaml` which preserves comments.

---

### F-16 — QU5 fallback copies wrong content as simplified file
**Lines 286–289**
```bash
claude --print < "$QU5_PROMPT_FILE" > "$SIMPLIFIED_FILE" || {
  cp "$LAST_VARIATIONS" "$SIMPLIFIED_FILE"
}
```
When QU5 fails, the entire variations file (all 5 variations V-01 through V-05) is copied as `$SIMPLIFIED_FILE`. The golden step then reads `head -80` of this and asks Claude to "extract the winning variation" — which is recoverable, but fragile. The fallback should copy the best-scored variation explicitly, or at minimum the fallback path should be flagged in the golden frontmatter.

---

### F-17 — Hardcoded `REPO` path
**Line 13**
```bash
REPO="sim"
```
Script is not relocatable. If run from any other machine or path, it silently uses a wrong root. Derive it from the script's own location:
```bash
REPO="$(cd "$(dirname "$0")/.." && pwd)"
```

---

### Summary Table

| ID | Severity | Type | Line(s) |
|----|----------|------|---------|
| F-01 | Low | Dead code | 16 |
| F-02 | Low | Dead code | 251–252 |
| F-03 | Medium | Resource leak | 33–36 |
| F-04 | High | Injection | 54–62 |
| F-05 | High | Injection | 71–96, 116–166, 225–235, 318–353 |
| F-06 | Medium | Error handling | 9 |
| F-07 | Low | Style | 14 locations |
| F-08 | Low | Robustness | 42 |
| F-09 | Low | Efficiency | 172–204 |
| F-10 | Medium | Logic | 77 vs 153 |
| F-11 | Medium | Logic | 147, 228 |
| F-12 | Medium | Logic | 219–241 |
| F-13 | Low | Consistency | 31 vs 250 |
| F-14 | Low | Observability | 346 |
| F-15 | Medium | Data loss | 376–378 |
| F-16 | Low | Logic | 286–289 |
| F-17 | Low | Portability | 13 |

The two highest-severity findings are **F-04** (Python code injection via SKILL_ID) and **F-05** (shell expansion of file content into prompt strings), both of which are injection risks. **F-10**, **F-11**, and **F-12** are the most likely to silently corrupt quest results.
