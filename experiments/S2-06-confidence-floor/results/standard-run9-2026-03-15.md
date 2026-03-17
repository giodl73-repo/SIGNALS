Here are all findings, by section:

---

## F-01 · `set -e` breaks the loop on score parse failure (Line 9, 172–204)

`set -e` is active throughout, but the three `python -c ... || echo "0"` parse blocks swallow errors. If Python itself crashes (not a parse miss), the `|| echo` catches it — so `TOP_SCORE` becomes `"0"` and `ALL_ESSENTIAL` becomes `"false"`. That means a Python crash silently looks like a low-scoring round. The loop continues producing junk artifacts for up to 20 rounds.

**Fix:** After the parse block, validate that `$TOP_SCORE` is a number before proceeding.

---

## F-02 · `SPEC_FILE` is assigned but never used (Line 16)

`SPEC_FILE="$REPO/simulations/draft/specs/signal-scout-$TODAY.md"` is hardcoded to `signal-scout-` regardless of `$SKILL_ID`. It's never read or written anywhere in the script. Dead variable.

**Fix:** Remove it, or pass `$SKILL_ID` into the name if it's meant to be used in a future step.

---

## F-03 · Shell injection via `$SKILL_ID` in Python inline (Lines 54–62, 361–380)

`$SKILL_ID` is interpolated directly into `-c "..."` Python strings:
```bash
python -c "
...
    if s['id'] == '$SKILL_ID':
```
If `SKILL_ID` contains a single quote, the Python string breaks. A value like `foo' or True  #` would corrupt the comparison. Same issue in Step 5's yaml update block.

**Fix:** Pass `SKILL_ID` as a `sys.argv` argument instead of embedding it in the string literal (the QU5 block at line 253 already does this correctly — use that pattern for all Python blocks).

---

## F-04 · `head -80` on rubric/variations truncates silently (Lines 122, 147, 229, 252, 324, 328, 330, 333)

The rubric and variations files are fed to prompts via `$(cat "$FILE" | head -80)`. 80 lines is very likely to truncate a rubric mid-criterion. The LLM sees an incomplete document with no truncation notice. This would cause the evolution step to work from a partial rubric, possibly dropping criteria silently.

**Fix:** Either remove the `head` limit and pass via file (preferred — `claude_ask` already does this), or add a `# [TRUNCATED]` sentinel so the model knows.

---

## F-05 · `ROUND` is undefined after the loop exits at `MAX_ROUNDS` (Lines 109, 342–384)

If the loop reaches `MAX_ROUNDS=20` without breaking on dual convergence, `$ROUND` is `20` at exit — which is correct for `seq`. But the golden frontmatter says `rounds: $ROUND`, implying "rounds completed", not "last round index". If convergence breaks at round 7, `$ROUND` is `7`. That's consistent. No bug — but the variable is never explicitly documented as "the last round index" vs "total rounds run". Minor clarity finding.

---

## F-06 · `LAST_VARIATIONS` and `LAST_SCORECARD` are empty if loop never runs (Lines 106–107, 251, 327–328)

If `MAX_ROUNDS=0` (or the loop body is skipped), `$LAST_VARIATIONS` and `$LAST_SCORECARD` remain empty strings. Step 3.5 then calls `open(sys.argv[3])` on an empty path, crashing Python. `set -e` would halt the script there with no useful message.

This can't happen with `MAX_ROUNDS=20`, but if someone sets it to 0 for testing the golden-write path, it silently crashes.

**Fix:** Add a guard: `[ -z "$LAST_VARIATIONS" ] && { echo "ERROR: no rounds completed"; exit 1; }`

---

## F-07 · QU5 fallback `cp "$LAST_VARIATIONS" "$SIMPLIFIED_FILE"` copies the full 5-variation file (Lines 287–289)

On QU5 failure, the script copies the entire variations file as the "simplified" output. The golden step then reads `head -80` of that file, which is the preamble and V-01 only — not the winning variation. The golden prompt would be built from an arbitrary variation, not the winner.

**Fix:** Track which variation won (`WINNING_VARIATION`) during the score step and copy only that section, or use the last scorecard's top-ranked variation ID.

---

## F-08 · `$LAST_SCORE` comparison uses string equality for convergence, but score is numeric (Lines 212–222)

The plateau/convergence check uses:
```bash
if [ "$ALL_ESSENTIAL" = "true" ] && [ "$NEW_PATTERNS" = "0" ]; then
```
`NEW_PATTERNS` is extracted as a number from Python and compared as a string to `"0"`. This works, but if Python returns `"0\n"` with a trailing newline (common with `print()`), the comparison fails silently and `PLATEAU_COUNT` never increments — the loop runs all 20 rounds even after convergence.

**Fix:** Strip whitespace: `NEW_PATTERNS=$(... | tr -d '[:space:]')` or use arithmetic comparison `[ "$NEW_PATTERNS" -eq 0 ]`.

---

## F-09 · YAML round-trip via `yaml.dump` may reorder or reformat signal.skills.yaml (Lines 361–380)

`yaml.safe_load` + `yaml.dump` with `sort_keys=False` preserves key order within each skill node but will still normalize YAML formatting: multi-line strings become block scalars, inline lists may change style, comments are stripped. Since `signal.skills.yaml` is a hand-maintained file, this could produce noisy diffs on every quest run.

**Fix:** Use a line-patch approach (`re.sub` or `sed`) targeting only the `$SKILL_ID` stanza, rather than a full parse-and-dump round-trip.

---

## F-10 · Trace file selection uses `head -1` on `ls` output (Line 42)

```bash
TRACE_FILE=$(ls "$TRACE_DIR"/plugin-${SKILL_ID}-*.md 2>/dev/null | head -1 || true)
```
`ls` output order is filesystem-dependent (typically alphabetical, but not guaranteed across filesystems). If multiple trace files exist (e.g., from prior runs), this silently picks one non-deterministically. No warning is emitted.

**Fix:** Emit a warning if more than one trace file matches: `ls ... | wc -l` → warn if > 1. Or use the most recent: `ls -t ... | head -1`.

---

## Summary Table

| # | Line(s) | Severity | Category |
|---|---------|----------|----------|
| F-01 | 9, 172–204 | Medium | Silent failure masking |
| F-02 | 16 | Low | Dead code |
| F-03 | 54–62, 361–380 | High | Shell injection |
| F-04 | 122, 147, 229, 324–333 | Medium | Prompt truncation |
| F-05 | 384 | Low | Clarity/docs |
| F-06 | 106–107 | Low | Edge-case crash |
| F-07 | 287–289 | Medium | Wrong artifact in golden |
| F-08 | 212–222 | Medium | Convergence never triggers |
| F-09 | 361–380 | Medium | YAML round-trip corruption |
| F-10 | 42 | Low | Non-deterministic file selection |

**F-03 and F-08 are the highest priority.** F-03 is a correctness/security issue on any skill ID with punctuation. F-08 means the loop never converges early even when it should, burning 20 rounds on every run.
