Here are all findings, organized by severity.

---

## Findings

### F-01 — Dead variable: `SPEC_FILE` hardcodes wrong skill namespace
**Line 16**
```bash
SPEC_FILE="$REPO/simulations/draft/specs/signal-scout-$TODAY.md"
```
`scout` is hardcoded instead of `$SKILL_ID`. More importantly, `SPEC_FILE` is never read anywhere in the script — it's assigned and immediately abandoned. Dead variable.

---

### F-02 — Dead variables: `VARS_CONTENT` and `RUBRIC_CONTENT` assigned but never used
**Lines 251–252**
```bash
VARS_CONTENT=$(cat "$LAST_VARIATIONS" | head -100)
RUBRIC_CONTENT=$(cat "$RUBRIC_FILE" | head -60)
```
Both are assigned but the QU5 Python block reads the files directly via `open(sys.argv[3]).read()` (lines 257–258). These two assignments do nothing and spawn two unnecessary subprocesses.

---

### F-03 — Three separate Python subprocesses parse the same file
**Lines 172–204**
```python
TOP_SCORE=$(python -c "..." 2>/dev/null || echo "0")
ALL_ESSENTIAL=$(python -c "..." 2>/dev/null || echo "false")
NEW_PATTERNS=$(python -c "..." 2>/dev/null || echo "0")
```
The same file is opened and the same regex is applied three times, in three separate Python processes, per round. One call that returns all three values would be cleaner and faster.

---

### F-04 — JSON regex breaks on non-trivial `new_patterns` arrays
**Lines 175, 186, 196, 297**
```python
m = re.search(r'```json\s*({[^}]+})\s*```', txt, re.DOTALL)
```
`[^}]+` stops at the first `}`. For a flat JSON like `{"top_score": 85, "new_patterns": []}` this works. But if `new_patterns` contains object elements — `[{"axis": "role"}]` — the pattern stops at the first `}` inside the nested object, yielding a truncated (invalid) match. Safer: use `re.search(r'```json\s*(\{.*?\})\s*```', txt, re.DOTALL)` or `json.loads` on the captured block after extracting delimiters properly.

---

### F-05 — `mktemp` used in QU5 step despite comment explaining why it's avoided
**Lines 250 vs 31**
```bash
QU5_PROMPT_FILE=$(mktemp /tmp/qu5-prompt-XXXXXX.txt)  # line 250
# vs claude_ask():
tmp_prompt="/tmp/claude-ask-$$.txt"  # line 31, comment: "mktemp may return Windows paths in relay context"
```
The `claude_ask` helper was explicitly written to avoid `mktemp` in relay context. The QU5 step re-introduces `mktemp`, contradicting that decision with no explanation.

---

### F-06 — QU5 calls `claude --print` directly instead of `claude_ask`
**Line 286**
```bash
claude --print < "$QU5_PROMPT_FILE" > "$SIMPLIFIED_FILE" || { ... }
```
All other Claude calls use `claude_ask`, which handles rc, cleanup, and is the documented abstraction for this script. The QU5 step is a one-off exception with manual `rm -f` on line 290. Should use `claude_ask "$(<"$QU5_PROMPT_FILE")" "$SIMPLIFIED_FILE"`.

---

### F-07 — Shell variable injection into Python `-c` string
**Lines 54–62 and 361–380**
```bash
SKILL_DESC=$(python -c "
...
    if s['id'] == '$SKILL_ID':    # ← $SKILL_ID injected into Python source
```
```bash
skill['quest_status'] = 'GOLDEN (Round $ROUND, score $LAST_SCORE)'
```
`$SKILL_ID` is shell-expanded into Python source code. A value like `x'; import os; os.system(...)  #` would be valid shell and execute as Python. Though `SKILL_ID` is caller-supplied, the pattern is unsafe. Fix: pass as arguments and read from `sys.argv`, as the QU5 block already does correctly (lines 255–258).

---

### F-08 — `yaml.dump` destroys comments and may alter key ordering
**Lines 376–377**
```python
yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
```
`PyYAML`'s `dump` discards all inline comments and reformats values (multi-line strings become flow-style, etc.). `signal.skills.yaml` likely has comments or formatting that matters. Fix: use `ruamel.yaml` with round-trip loader, or write only the specific fields that changed rather than dumping the whole document.

---

### F-09 — Aggressive `head -N` truncations cut context passed to Claude
**Lines 122, 147, 228, 231, 324, 327, 329, 333**
```bash
$(cat "$RUBRIC_FILE" | head -80)
$(cat "$VARIATIONS_FILE" | head -200)
$(cat "$LAST_SCORECARD" | head -100)
```
The golden step passes `head -150` of `$LAST_VARIATIONS` (line 329). With 5 variations of ~50+ lines each, 250+ lines are typical — the golden prompt is asked to "copy verbatim" a variation that may be truncated out of its own context window. The rubric evolution step (line 228) likewise passes `head -80` of the rubric it's supposed to evolve. All of these also use `cat file | head -N` (UUOC) — prefer `head -N "$file"` directly.

---

### F-10 — `ls` used for glob; no deterministic ordering guarantee
**Line 42**
```bash
TRACE_FILE=$(ls "$TRACE_DIR"/plugin-${SKILL_ID}-*.md 2>/dev/null | head -1 || true)
```
`ls` ordering is filesystem-dependent. If multiple trace files exist (e.g., from multiple dates), `head -1` may select an older one. Use `ls -t ... | head -1` to get the most recent, or `find ... -newer ... ` for date-sorted selection.

---

### F-11 — No timeout on `claude --print` — script can hang indefinitely
**Lines 33, 137, 168, 237, 286, 355**
With `MAX_ROUNDS=20` and 2 Claude calls per round plus rubric evolutions and the golden step, up to ~45 calls with no timeout. In relay context a hung process blocks forever. Add `timeout 300 claude --print ...` or equivalent.

---

### F-12 — `set -e` with no recovery: a single Claude failure aborts the full run
**Line 9 + lines 137, 168**
`claude_ask` propagates `$rc`. With `set -e`, any failure inside the loop exits the script immediately, discarding all rounds already completed. Consider wrapping loop calls with `|| { echo "round $ROUND failed, continuing"; continue; }` or trapping `ERR`.

---

### F-13 — No re-run protection: same-day re-run silently overwrites artifacts
**Lines 68, 113, 141, 224**
Rubric file: `${SKILL_ID}-rubric-$TODAY.md`. Scorecard: `${SKILL_ID}-scorecard-R${ROUND}-$TODAY.md`. A second run on the same day overwrites R1–R20 scorecards and all rubric versions from the first run. A run counter in the filename (or a check for existing artifacts) would prevent silent data loss.

---

### F-14 — `set -u` not set; unset variable access not caught
**Line 9**
`set -e` is present but `set -u` is not. If `LAST_VARIATIONS` or `LAST_SCORECARD` were ever empty (e.g., if `LAST_VARIATIONS=""` and `cat ""` were called), it would fail silently or with a confusing error. `set -euo pipefail` is the standard hardening baseline.

---

### Summary Table

| ID | Severity | Category | Line(s) |
|----|----------|----------|---------|
| F-01 | Low | Dead code | 16 |
| F-02 | Low | Dead code | 251–252 |
| F-03 | Low | Performance | 172–204 |
| F-04 | Medium | Bug | 175, 186, 196, 297 |
| F-05 | Medium | Inconsistency | 250 vs 31 |
| F-06 | Low | Inconsistency | 286 |
| F-07 | Medium | Security | 54–62, 361–380 |
| F-08 | Medium | Data loss risk | 376–377 |
| F-09 | Medium | Correctness | 122, 147, 228, 231, 324–333 |
| F-10 | Low | Fragility | 42 |
| F-11 | High | Reliability | 33, 137, 168, 237, 286, 355 |
| F-12 | Medium | Reliability | 9, 137, 168 |
| F-13 | Medium | Data safety | 68, 113, 141, 224 |
| F-14 | Low | Hardening | 9 |
