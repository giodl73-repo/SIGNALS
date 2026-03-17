Here are all findings, by category:

---

## Bugs

**F-01 — SPEC_FILE hardcoded to "scout" and never used (line 16)**
```bash
SPEC_FILE="$REPO/simulations/draft/specs/signal-scout-$TODAY.md"
```
Two problems: (1) the literal `scout` string ignores `$SKILL_ID`, so every skill would try to load the scout spec; (2) `SPEC_FILE` is assigned but never referenced anywhere in the script. Dead variable with a wrong value.

---

**F-02 — VARS_CONTENT and RUBRIC_CONTENT assigned but unused (lines 251–252)**
```bash
VARS_CONTENT=$(cat "$LAST_VARIATIONS" | head -100)
RUBRIC_CONTENT=$(cat "$RUBRIC_FILE" | head -60)
```
Both are computed here but the Python script on lines 253–284 opens `sys.argv[3]` and `sys.argv[4]` (the file paths) directly. The shell variables are dead code.

---

**F-03 — Step 3.5 uses `mktemp` despite relay-context warning (line 250)**
```bash
QU5_PROMPT_FILE=$(mktemp /tmp/qu5-prompt-XXXXXX.txt)
```
The `claude_ask` helper was specifically designed to avoid `mktemp` because it "may return Windows paths in relay context" (comment at line 30). Step 3.5 bypasses that helper and calls `mktemp` directly, introducing the same problem the helper was built to prevent. Should use the same `$$`-based explicit path pattern as `claude_ask`.

---

**F-04 — QU5 fallback copies full variations file, not the winning variation (line 288)**
```bash
cp "$LAST_VARIATIONS" "$SIMPLIFIED_FILE"
```
The fallback path is triggered when QU5 fails. `$LAST_VARIATIONS` contains all 5 variations (V-01–V-05). Step 4 at line 321 says "Use the SIMPLIFIED prompt body if simplification passed. Otherwise use the winning variation" — but the content supplied is all 5 variations, not the winner. The golden synthesis prompt receives misleading input on the fallback path.

---

**F-05 — `yaml.safe_load` + `yaml.dump` silently destroys all YAML comments (lines 361–380)**
```python
with open(yaml_file) as f:
    data = yaml.safe_load(f)
# ... mutate data ...
with open(yaml_file, 'w') as f:
    yaml.dump(data, f, ...)
```
PyYAML's round-trip drops every `#` comment in `signal.skills.yaml`. If that file has documentation inline (skill intent, notes, status history), it is gone on the first run. Use `ruamel.yaml` with `RoundTripLoader`/`RoundTripDumper` to preserve comments, or patch with `sed`/`re.sub` instead of full rewrite.

---

**F-06 — Shell injection via SKILL_ID interpolated into Python `-c` strings (lines 54–62, 361–380)**
```bash
python -c "
...
    if s['id'] == '$SKILL_ID':
...
"
```
A `SKILL_ID` containing a single quote (e.g., `foo'bar`) breaks the Python string literal and creates arbitrary code execution. Also triggered at line 373: `skill['quest_status'] = 'GOLDEN (Round $ROUND, score $LAST_SCORE)'`. Pass these as `sys.argv` arguments (as already done in the QU5 block, lines 253–284) rather than interpolating into the code string.

---

## Truncation / context quality

**F-07 — Rubric truncated at 80 lines throughout the loop (lines 122, 147, 228, 333)**
```bash
$(cat "$RUBRIC_FILE" | head -80)
```
The rubric grows with each evolution pass (new aspirational criteria added). By round 3+, 80 lines likely clips mid-criterion. The variate, score, evolve, and golden prompts all use this same limit — meaning Claude is scoring against an incomplete rubric. There is no character budget being respected here; 80 is an arbitrary line count.

---

**F-08 — Variations truncated at 200 lines for scoring (line 150)**
```bash
$(cat "$VARIATIONS_FILE" | head -200)
```
5 complete runnable prompt variations in 200 lines means roughly 40 lines each. Skill prompt bodies for complex skills (with role sequences, multi-phase flows, and scoring rubrics) easily exceed that. V-03 through V-05 may be partially or fully absent from the scoring context.

---

**F-09 — Scorecard truncated at 100 lines for rubric evolution (line 231)**
```bash
$(cat "$SCORECARD_FILE" | head -100)
```
The excellence signals the evolution prompt needs to extract are typically at the end of the scorecard (after per-variation scoring tables). Truncating at 100 lines risks cutting them off and producing an empty or incorrect rubric update.

---

## Robustness / logic

**F-10 — Skill not found in registry: silent continuation (line 62)**
```bash
" 2>/dev/null || echo "Skill not found in registry")
```
If `SKILL_ID` does not exist in `signal.skills.yaml`, `SKILL_DESC` is set to the literal string `"Skill not found in registry"` and the script continues. The rubric, 20 rounds of variations, and golden prompt are generated using that fallback as the skill description. The script should exit with an error here.

---

**F-11 — JSON parse failures silently default to 0/"false", blocking convergence detection (lines 172–204)**
```python
else:
    print(0)   # TOP_SCORE fallback
    print('false')  # ALL_ESSENTIAL fallback
    print(0)   # NEW_PATTERNS fallback
```
If Claude produces malformed output (no JSON block, or truncated JSON), the parsing subshells return `0`/`false`/`0`. `ALL_ESSENTIAL=false` resets `PLATEAU_COUNT` to 0 each round. The script then runs all MAX_ROUNDS (20 calls × 2 = 40 Claude API calls) without ever converging. There is no detection of "Claude never emitted parseable JSON."

---

**F-12 — No composite score threshold enforced at convergence (lines 211–217)**
```bash
if [ "$ALL_ESSENTIAL" = "true" ] && [ "$NEW_PATTERNS" = "0" ]; then
  PLATEAU_COUNT=$((PLATEAU_COUNT + 1))
  if [ "$PLATEAU_COUNT" -ge 2 ]; then
    echo "DUAL CONVERGENCE at round $ROUND"
    break
  fi
fi
```
The rubric prompt (line 87) defines the golden threshold as "all essential pass + composite >= 80." The loop's convergence check only tests `ALL_ESSENTIAL` and `NEW_PATTERNS`. A skill scoring composite=15 with all essentials passing and no new patterns for 2 rounds exits as "GOLDEN." The `TOP_SCORE >= 80` check is never performed.

---

## Summary table

| ID | Line(s) | Severity | Type |
|----|---------|----------|------|
| F-01 | 16 | Medium | Bug — dead variable with wrong value |
| F-02 | 251–252 | Low | Dead code |
| F-03 | 250 | Medium | Bug — contradicts relay-context safety design |
| F-04 | 288 | Medium | Logic error — wrong content on fallback path |
| F-05 | 361–380 | High | Data loss — YAML comments destroyed on write |
| F-06 | 54–62, 361–380 | Medium | Shell injection via unguarded interpolation |
| F-07 | 122, 147, 228, 333 | Medium | Truncation — rubric clipped mid-criterion |
| F-08 | 150 | Medium | Truncation — variations 3–5 likely absent from scoring |
| F-09 | 231 | Medium | Truncation — excellence signals likely cut off |
| F-10 | 62 | Medium | Robustness — missing input validation |
| F-11 | 172–204 | High | Logic error — parse failure = infinite loop |
| F-12 | 211–217 | Medium | Logic error — score threshold never checked |
