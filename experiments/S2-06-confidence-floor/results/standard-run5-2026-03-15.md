Here is the full findings report.

---

## Findings: `tools/quest-run-one.sh`

---

### F-01 — Bug: `SPEC_FILE` hardcodes `signal-scout-` and is never used
**Line 16**
```bash
SPEC_FILE="$REPO/simulations/draft/specs/signal-scout-$TODAY.md"
```
`SKILL_ID` is the parameter the whole script runs on, but the path is hardcoded to `signal-scout-`. This variable is also never referenced anywhere in the script. Dead and wrong.

**Fix:** Either remove it entirely or change to `signal-${SKILL_ID}-$TODAY.md`.

---

### F-02 — Bug: `VARS_CONTENT` and `RUBRIC_CONTENT` assigned but never read
**Lines 251–252**
```bash
VARS_CONTENT=$(cat "$LAST_VARIATIONS" | head -100)
RUBRIC_CONTENT=$(cat "$RUBRIC_FILE" | head -60)
```
The QU5 Python script reads the files directly via `sys.argv[3]` and `sys.argv[4]`. Both assignments are dead. They also run `cat | head` inside subshells, spawning processes for nothing.

**Fix:** Remove both lines.

---

### F-03 — Bug: `set -e` + no fallback on QU5 Python prompt-build
**Lines 253–284**
```bash
python -c "..." "$SKILL_ID" "$RUBRIC_VERSION" "$LAST_VARIATIONS" "$RUBRIC_FILE" "$QU5_PROMPT_FILE"
```
If this Python command fails (e.g., `LAST_VARIATIONS` file missing, yaml parse error), `set -e` kills the script with no diagnostic. The `|| { ... }` fallback at line 286 only covers the subsequent `claude` call, not the Python build step.

**Fix:** Add `|| { echo "QU5 prompt build failed -- skipping"; cp "$LAST_VARIATIONS" "$SIMPLIFIED_FILE"; }` to this Python call, or wrap the whole QU5 block in a `set +e` / `set -e` guard.

---

### F-04 — Bug: No convergence-failure signal when loop exhausts MAX_ROUNDS
**Lines 109–242**
If all 20 rounds complete without DUAL CONVERGENCE, the script silently continues to write a golden file and update `signal.skills.yaml` with `status: GOLDEN`. The golden output is from a non-converged run, but nothing in the output distinguishes it from a converged one.

**Fix:** After the loop, check whether `PLATEAU_COUNT >= 2` was ever reached. If not, log a warning and set a different `quest_status` (e.g., `PARTIAL (max rounds, score $LAST_SCORE)`).

---

### F-05 — Security: `$SKILL_ID` interpolated into Python source code
**Lines 54–62, 361–380**
```bash
SKILL_DESC=$(python -c "
...
    if s['id'] == '$SKILL_ID':
...
")
```
`$SKILL_ID` is substituted directly into Python code. A SKILL_ID containing a single quote (e.g., `foo'` or `foo'; import os; os.system(...)`) breaks the Python syntax or injects code. Same issue at line 373 where `$SKILL_ID` appears in the YAML-update Python script.

**Fix:** Pass `SKILL_ID` as a command-line argument (`sys.argv[1]`) or environment variable (`os.environ['SKILL_ID']`), not as an inline string literal. The QU5 block already does this correctly — use that pattern throughout.

---

### F-06 — Bug: Claude-generated file content interpolated into bash strings
**Lines 122, 147, 228, 231, 324, 329, 333**
```bash
VARIATE_PROMPT="...
$(cat "$RUBRIC_FILE" | head -80)
..."
```
Content from Claude-generated files is expanded inside double-quoted bash strings. If a generated rubric or scorecard contains backticks or `$(...)`, bash executes them during assignment. This is an uncontrolled code execution path once the loop is running.

**Fix:** Write all multi-source prompts to temp files via Python (as QU5 does), avoiding bash string interpolation of file content entirely.

---

### F-07 — Correctness: Rubric truncated to 80 lines in score and evolve prompts
**Lines 147, 228**
```bash
$(cat "$RUBRIC_FILE" | head -80)
```
A rubric with 6–8 criteria, each with several fields, easily exceeds 80 lines. The rubric provided to `/quest:score` and `/quest:evolve` silently drops any criteria past line 80. Claude scores against an incomplete rubric, which corrupts the convergence signal.

**Fix:** Remove the `head -80` guard or raise it substantially (e.g., `head -200`). The rubric is the authoritative evaluation spec and should be provided complete.

---

### F-08 — Fragility: `ls` used for file discovery
**Line 42**
```bash
TRACE_FILE=$(ls "$TRACE_DIR"/plugin-${SKILL_ID}-*.md 2>/dev/null | head -1 || true)
```
`ls` output is unreliable for filenames containing spaces, newlines, or glob metacharacters. On no-match, `ls` exits non-zero (suppressed by `2>/dev/null || true`), but the glob could also expand unexpectedly.

**Fix:**
```bash
TRACE_FILE=$(find "$TRACE_DIR" -maxdepth 1 -name "plugin-${SKILL_ID}-*.md" 2>/dev/null | head -1)
```
Or use a bash glob array and take index 0.

---

### F-09 — Duplication: JSON parsing regex repeated three times
**Lines 172–204**
The same `re.search(r'\`\`\`json\s*({[^}]+})\s*\`\`\`', txt, re.DOTALL)` block appears in three separate `python -c` invocations to extract `top_score`, `all_essential_pass`, and `new_patterns`. This triples the I/O and parse cost for the same file on every round.

**Fix:** One Python call reads the scorecard once, prints all three values (e.g., space-separated), and one `read` assignment splits them:
```bash
read TOP_SCORE ALL_ESSENTIAL NEW_PATTERNS < <(python -c "..." "$SCORECARD_FILE")
```

---

### F-10 — Inconsistency: Mixed prompt construction strategies
**Lines 71–96 (bash interpolation) vs lines 253–284 (Python file args)**
The QU5 block correctly writes the prompt via Python using `sys.argv` file paths, avoiding shell injection and ARG_MAX issues. All other prompts use bash double-quoted string interpolation with embedded `$(cat ...)`. The safe pattern is already in the script; it's just not applied uniformly.

**Fix:** Standardize all prompt construction to the Python-writes-to-tempfile approach used in QU5. Refactor `claude_ask` to accept a file path option or make a `claude_ask_file` variant.

---

### F-11 — Minor: Useless use of `cat` throughout
**Lines 122, 147, 228, 231, 252, 324, 329, 333**
```bash
cat "$RUBRIC_FILE" | head -80
```
`head` accepts a filename directly. `cat file | head` spawns an extra process for no benefit.

**Fix:** `head -80 "$RUBRIC_FILE"` throughout.

---

### F-12 — Bug: QU5 fallback copies entire variations file as simplified output
**Lines 287–289**
```bash
cp "$LAST_VARIATIONS" "$SIMPLIFIED_FILE"
```
`LAST_VARIATIONS` contains all five V-01…V-05 variations. When QU5 fails and this file is copied as `SIMPLIFIED_FILE`, the golden prompt step (line 324) truncates it to 80 lines, which likely captures only part of V-01 and no winning variation body. The golden prompt instruction (`"Use the SIMPLIFIED prompt body if simplification passed"`) then operates on garbled input.

**Fix:** On QU5 failure, leave `SIMPLIFIED_FILE` unset and let the golden step fall through to `LAST_VARIATIONS` with explicit logic — do not write a misleading "simplified" file.

---

### Summary Table

| ID | Severity | Category | Line(s) |
|----|----------|----------|---------|
| F-01 | Bug | Dead/wrong variable | 16 |
| F-02 | Bug | Dead assignments | 251–252 |
| F-03 | Bug | Missing error handling | 253–284 |
| F-04 | Bug | Silent bad state | 109–242 |
| F-05 | Security | Shell→Python injection | 54–62, 361–380 |
| F-06 | Bug | Bash executes generated content | 122, 147, 228, 231, 324, 329, 333 |
| F-07 | Correctness | Silent rubric truncation | 147, 228 |
| F-08 | Fragility | `ls` for file discovery | 42 |
| F-09 | Duplication | Triple JSON parse | 172–204 |
| F-10 | Inconsistency | Mixed prompt construction | throughout |
| F-11 | Minor | Useless `cat` | multiple |
| F-12 | Bug | Bad QU5 fallback output | 287–289 |
