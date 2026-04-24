Here are all findings, organized by severity:

---

## Bugs

**B-01** (line 42) — `ls` with glob + `head -1` silently picks an arbitrary trace file when multiple exist. No sort, no warning. If two `plugin-scout-feasibility-*.md` files exist you get whichever `ls` returns first (filesystem order). Use `ls -t ... | head -1` for newest, or error if count > 1.

**B-02** (lines 172–204) — Three separate Python invocations each reopen and re-parse the same scorecard. If the file is large or the JSON block appears in a different position between reads, you could get inconsistent values for `TOP_SCORE`, `ALL_ESSENTIAL`, and `NEW_PATTERNS` from the same round. Parse once, emit all three values on stdout separated by a delimiter, split in bash.

**B-03** (lines 175, 186, 197) — The regex `{[^}]+}` fails if `new_patterns` contains strings with `}` in them (e.g., `"pattern with {foo} inside"`). `[^}]+` is not a valid JSON object parser — it stops at the first `}` it sees. Use `re.search(r'```json\s*(.*?)\s*```', txt, re.DOTALL)` and then `json.loads(...)` instead.

**B-04** (line 222) — `[ "$NEW_PATTERNS" -gt "0" ]` does integer comparison on a value that comes from `echo "0"` in the error path. If the Python script fails and emits something non-numeric (e.g., a Python traceback leaks through), this arithmetic test throws `integer expression expected` and kills the script under `set -e`.

**B-05** (lines 253–284) — QU5 passes `$LAST_VARIATIONS` as both a filename argument (line 257) and reads it again in Python via `open(sys.argv[3]).read()` (line 257), but the `$LAST_VARIATIONS` variable is also used as a shell-expanded string in the f-string at line 265 (`{variations[:3000]}`). These are consistent, but **if the loop exits without running a single round** (i.e., `MAX_ROUNDS=0`), `LAST_VARIATIONS` is empty string and `open('').read()` raises `FileNotFoundError`, crashing QU5 silently (caught by `||` on line 286, but you lose the golden with no explanation).

**B-06** (line 303) — Division `simp/orig` with integer division in Python 3 only if both are int, which they are from JSON. This is fine, but if `orig` somehow comes in as a string (JSON parse coercion edge case), it becomes a silent `0` percentage. Not critical but worth a `int()` cast.

---

## Data Loss / Silent Failure Risks

**D-01** (lines 68, 324) — `$RUBRIC_FILE` is initialized to `v1` path at line 68 but the variable is mutated in the loop (line 238). In Step 4 at line 324, the prompt reads `$(cat "$RUBRIC_FILE" | head -80)` — correct. But the frontmatter line 344 uses `${RUBRIC_FILE##*/}` — also correct. No data loss, but the mutation is subtle and a reader could miss that `$RUBRIC_FILE` no longer points to the v1 file at Step 4.

**D-02** (line 371) — Python inline script uses shell variable interpolation inside a Python string literal: `'simulations/quest/golden/${SKILL_ID}-golden-$TODAY.md'`. Single quotes in shell **do not expand** variables. `${SKILL_ID}` and `$TODAY` will be written as literal strings into the YAML. This is a bug — should be double-quoted or constructed in Python using `sys.argv` or an environment variable.

**D-03** (lines 373–374) — `quest_status` writes `'GOLDEN (Round $ROUND, score $LAST_SCORE)'` — same single-quote shell expansion bug. `$ROUND` and `$LAST_SCORE` will be literal in the YAML output.

---

## Logic Issues

**L-01** (lines 212–220) — Plateau detection resets `PLATEAU_COUNT=0` when either `ALL_ESSENTIAL != true` OR `NEW_PATTERNS != 0`. This means a round with `all_essential=true` but one new pattern resets the counter to 0. Intended? If the rubric evolves but you're otherwise converging, you'll never plateau until patterns stop appearing. The score could be 98 but you keep looping because one minor new pattern was found. Consider: converge when score is above a threshold regardless of new patterns.

**L-02** (line 16) — `SPEC_FILE` is set but never used anywhere in the script. Dead variable.

**L-03** (lines 122, 147, 228) — `$(cat "$RUBRIC_FILE" | head -80)` — useless use of `cat`. Should be `head -80 "$RUBRIC_FILE"`. Minor but repeated 5+ times.

**L-04** (lines 122, 147, 228, 324, 333) — All rubric/variations reads are truncated (`head -80`, `head -100`, `head -60`). The rubric could be well over 80 lines, especially after several `EVOLVE` passes that add new aspirational criteria. Truncating the rubric passed to the scoring step means criteria added in late rounds may never be evaluated. Either pass the full file, or track a line-count budget.

**L-05** (line 153) — `${TRACE_CONTENT:0:800}` — trace truncated to 800 chars in the score prompt (down from 3000 in the rubric prompt). The scorer is working with less ground truth than the rubric generator. Likely intentional to save tokens, but worth an explicit comment.

---

## Robustness / Portability

**R-01** (line 31) — `/tmp/claude-ask-$$.txt` uses PID as disambiguator. If `claude_ask` is called concurrently (e.g., from a parallel wrapper), two calls with the same PID collide. A `$$` is process-local, so this is safe in a sequential script — but the comment in the header says "P-01 concurrent by default." If this script is ever parallelized, the temp file name needs `mktemp` or a round/step suffix.

**R-02** (line 250) — `mktemp /tmp/qu5-prompt-XXXXXX.txt` is used for QU5 but `printf` to a fixed name is used for `claude_ask`. Inconsistent approach. The QU5 temp file is cleaned up on line 290, but only if execution reaches that line. If the `python -c` at line 253 fails, `QU5_PROMPT_FILE` holds a path to a file that may or may not exist, and line 290 does `rm -f` which is fine. But if the script exits before line 290 (e.g., `set -e` triggers on a later step), the temp file leaks.

**R-03** (line 9) — `set -e` means any non-zero exit code terminates the script. `claude_ask` captures `rc` and returns it — but `claude --print` could fail for network/auth reasons mid-loop. With `set -e`, this kills the entire run silently at whatever round it's on, discarding all prior round artifacts (which were written). Consider `set -e` only for setup steps and add explicit error handling inside the loop.

**R-04** (line 54–62) — `$SKILL_ID` is interpolated directly into a Python string passed to `-c`. If a skill ID contains a single quote (unlikely given current naming, but not validated), the Python code breaks. Validate `$SKILL_ID` is alphanumeric+hyphen before use, or pass it as `sys.argv`.

**R-05** (line 13) — `REPO="C:/src/sim"` is hardcoded. The script accepts a `cwd` in the relay dispatch (line 3 comment) but ignores it — the repo path is baked in. Running this from a different checkout or on another machine requires editing the script. Should use `REPO="$(cd "$(dirname "$0")/.." && pwd)"` or `REPO="${SIM_REPO:-C:/src/sim}"` with an env override.

---

## Summary Table

| ID | Severity | Category | One-liner |
|----|----------|----------|-----------|
| D-02 | High | Bug | Single-quoted Python string won't expand `$SKILL_ID`/`$TODAY` in YAML update |
| D-03 | High | Bug | Same single-quote issue for `quest_status` field |
| B-02 | Medium | Bug | Scorecard parsed 3× independently — inconsistent values possible |
| B-03 | Medium | Bug | Regex `[^}]+` breaks on `}` inside JSON string values |
| B-04 | Medium | Bug | Non-numeric `NEW_PATTERNS` breaks integer test under `set -e` |
| L-04 | Medium | Logic | Rubric truncated to 80 lines — late criteria never scored |
| L-01 | Medium | Logic | Plateau reset too aggressive — one new pattern blocks convergence indefinitely |
| B-01 | Low | Bug | Trace file selection non-deterministic when multiple files match |
| B-05 | Low | Bug | Empty `LAST_VARIATIONS` crashes QU5 if loop runs 0 rounds |
| R-03 | Low | Robustness | `set -e` kills entire run on any `claude` failure mid-loop |
| R-05 | Low | Portability | Hardcoded `C:/src/sim` repo path |
| L-02 | Info | Cleanup | `SPEC_FILE` is set but never used |
| L-03 | Info | Cleanup | Useless `cat` pipe — `head -80 "$RUBRIC_FILE"` is sufficient |
| R-01 | Info | Note | PID-based temp file is safe now, fragile if parallelized |
| R-04 | Info | Note | `$SKILL_ID` not validated before Python interpolation |
