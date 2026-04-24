Here are all findings from the script, organized by severity.

---

## Findings

### BUG — F-01: `SPEC_FILE` is dead code with wrong namespace prefix
**Line 16**
```bash
SPEC_FILE="$REPO/simulations/draft/specs/signal-scout-$TODAY.md"
```
The variable is defined but never referenced anywhere in the script. Additionally, the path hardcodes `signal-scout-` regardless of `SKILL_ID` — for `draft-proposal` or `trace-contract` skills this would point to the wrong file. Dead code with a latent naming bug.

---

### BUG — F-02: `VARS_CONTENT` and `RUBRIC_CONTENT` assigned but never used
**Lines 251–252**
```bash
VARS_CONTENT=$(cat "$LAST_VARIATIONS" | head -100)
RUBRIC_CONTENT=$(cat "$RUBRIC_FILE" | head -60)
```
Both variables are computed (costing two subprocess calls) then ignored. The QU5 Python block that follows opens the files directly via `sys.argv[3]` and `sys.argv[4]`. The shell-side truncation (`head -100`, `head -60`) was presumably intended but has no effect.

---

### BUG — F-03: JSON regex breaks on nested objects
**Lines 175, 185, 196**
```python
m = re.search(r'\`\`\`json\s*({[^}]+})\s*\`\`\`', txt, re.DOTALL)
```
`[^}]+` matches any character except `}` and stops at the **first** `}` encountered. For the expected payload `{"top_score": 85, "all_essential_pass": true, "new_patterns": ["p1"]}` this works only because the array uses `[]`, not `{}`. If Claude wraps a pattern in a nested object — `"new_patterns": [{"text": "..."}]` — the match halts at the inner `}` and `json.loads` fails silently, causing `TOP_SCORE=0` and `NEW_PATTERNS=0`, which incorrectly resets `PLATEAU_COUNT` and may terminate the loop early with a false golden.

---

### BUG — F-04: `TRACE_CONTENT` truncation is inconsistent between rubric and score steps
**Lines 77, 153**
```bash
# rubric prompt:
${TRACE_CONTENT:0:3000}

# score prompt:
${TRACE_CONTENT:0:800}
```
The rubric is generated with up to 3 000 chars of trace context; the scorer sees only 800 chars. Rubric criteria can reference patterns from the bottom 2 200 chars that the scorer never sees, making those criteria unverifiable during scoring.

---

### BUG — F-05: Rubric evolve truncates at 80 lines — drops criteria on multi-evolution runs
**Line 228**
```bash
$(cat "$RUBRIC_FILE" | head -80)
```
Each evolution pass only feeds 80 lines of the *previous* rubric into the evolve prompt. A rubric with 3+ criteria tiers and frontmatter can easily exceed 80 lines after the first evolution. Criteria beyond line 80 are silently dropped, causing the evolved rubric to regress on coverage.

The same truncation applies on lines 122, 147 (variate and score prompts) but is less dangerous there since those are read-only inputs. On the evolve path it causes data loss.

---

### QUALITY — F-06: Silent failure on `SKILL_DESC` lookup masks YAML parse errors
**Lines 54–62**
```bash
SKILL_DESC=$(python -c "..." 2>/dev/null || echo "Skill not found in registry")
```
`2>/dev/null` suppresses all Python errors including `ModuleNotFoundError: No module named 'yaml'`, a malformed YAML file, or a permissions error. The script continues with `SKILL_DESC="Skill not found in registry"` and generates a rubric with no real skill description. No warning distinguishes "skill genuinely absent" from "yaml module not installed."

---

### QUALITY — F-07: Arbitrary head-line truncation may silently cut prompt content
**Lines 122, 147, 150, 228, 231, 251, 324, 327, 330, 333**
Truncation limits across the script: 60, 80, 100, 150, 200 lines. These are all arbitrary. As rubrics and variations grow across rounds, important content is silently omitted. The script has no mechanism to detect or warn when truncation occurs. A character-budget approach (e.g., `${content:0:4000}`) or logging the actual vs. truncated line count would make this observable.

---

### QUALITY — F-08: `claude_ask` does not capture stderr
**Line 33**
```bash
claude --print < "$tmp_prompt" > "$out_file"
```
stderr from `claude` goes to the terminal but not into `$out_file`. If `claude` exits 0 but writes its error to stderr and nothing to stdout, the artifact file is created empty (because `>` truncates on open). `set -e` only catches non-zero exit codes; an empty-but-successful artifact will silently propagate through downstream `cat "$file" | head -N` calls.

---

### STYLE — F-09: Useless use of `cat` throughout
**Lines 122, 147, 150, 228, 231, 251, 252, 324, 327, 330, 333**
Every pattern `$(cat "$file" | head -N)` forks an extra `cat` process. The idiomatic form is `$(head -N "$file")`. Not a correctness issue, but inconsistent with the stated preference for built-in tools over unnecessary Bash subprocesses.

---

### STYLE — F-10: Shell variable interpolated directly into inline Python — injection risk
**Lines 54–62, 172–204, 361–380**
`$SKILL_ID` and `$TODAY` are interpolated into `python -c "..."` strings without escaping:
```bash
python -c "
...
    if s['id'] == '$SKILL_ID':
...
"
```
A skill ID containing `'` (e.g., `foo'; import os; os.unlink('/important')`) would break or execute arbitrary Python. The QU5 block (lines 253–284) correctly avoids this by writing the script to a file and passing values via `sys.argv`. That pattern should be used consistently.

---

### STYLE — F-11: Inconsistent temp file creation strategies
**Lines 31 vs 250**
`claude_ask` uses a deterministic PID-based path:
```bash
tmp_prompt="/tmp/claude-ask-$$.txt"
```
QU5 uses `mktemp`:
```bash
QU5_PROMPT_FILE=$(mktemp /tmp/qu5-prompt-XXXXXX.txt)
```
The PID-based path is safe for single-instance use but provides no collision protection if the script is ever parallelized (P-01 is mentioned as a design intent in the header comments). `mktemp` is the standard for safe temp files.

---

### Summary Table

| ID | Severity | Line(s) | Issue |
|----|----------|---------|-------|
| F-01 | Bug | 16 | `SPEC_FILE` dead code with wrong namespace prefix |
| F-02 | Bug | 251–252 | `VARS_CONTENT`/`RUBRIC_CONTENT` computed but unused |
| F-03 | Bug | 175, 185, 196 | JSON regex `[^}]+` breaks on nested objects |
| F-04 | Bug | 77, 153 | Trace truncation inconsistency breaks scoring fidelity |
| F-05 | Bug | 228 | Rubric evolve truncates at 80 lines — drops criteria |
| F-06 | Quality | 54–62 | Silent YAML failure masked by `2>/dev/null` |
| F-07 | Quality | multiple | Arbitrary line-count truncation with no observability |
| F-08 | Quality | 33 | `claude_ask` drops stderr; empty artifacts undetected |
| F-09 | Style | multiple | UUOC: `cat file \| head -N` → `head -N file` |
| F-10 | Style | 54–62, 172–204, 361–380 | `$SKILL_ID` interpolated into inline Python |
| F-11 | Style | 31, 250 | Inconsistent temp file strategy (`$$` vs `mktemp`) |
