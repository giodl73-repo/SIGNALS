Here are all findings, by section:

---

## Bugs

**F-01: `ROUND` variable is out of scope after the loop (line 327, 373, 384)**
The final `echo` and `GOLDEN_PROMPT` reference `$ROUND` outside the `for` loop. In bash, the loop variable persists after a `break` but is *undefined* if the loop exhausts all iterations without breaking (e.g., `MAX_ROUNDS=20` reached without convergence). If that happens, `$ROUND` retains its last value (20) — technically correct but unintentional. More critically, the `quest_status` write on line 373 embeds `$ROUND` inside a Python string literal via shell interpolation, which works but is fragile.

**F-02: Regex too strict for LLM JSON output (lines 175, 186, 197)**
The pattern `r'\`\`\`json\s*({[^}]+})\s*\`\`\`'` uses `[^}]+` — this matches any character except `}`. If the JSON contains nested objects (e.g., `"patterns": [{"key":"val"}]`) the regex stops at the first `}` and `json.loads` fails. The regex should use `re.DOTALL` with a greedy match up to the closing fence, not `[^}]+`. (The `re.DOTALL` flag is already passed but doesn't help here — the issue is `[^}]` blocking the closing brace of nested structures.)

**F-03: QU5 pass reads `$LAST_VARIATIONS` but passes it verbatim as a file path (line 284)**
`python -c "..."` receives `$LAST_VARIATIONS` as `sys.argv[3]` and calls `open(sys.argv[3]).read()`. This is correct only if the file exists. However, if the loop converges on Round 1 and `$LAST_VARIATIONS` was just written, it works — but if `claude_ask` failed silently (due to the `|| true` suppression on line 181), the file may be empty or missing, and Python will raise an unhandled exception. The outer `set -e` won't catch a Python exception inside a subshell string here.

**F-04: `set -e` interacts poorly with the `|| echo "0"` fallbacks (lines 181, 192, 204)**
The `|| echo "0"` suppresses `$?` failures from the Python subshells, which is intentional — but `set -e` also applies inside `$()` subshells in some bash versions. If `claude_ask` inside the loop fails (e.g., `claude --print` exits non-zero), `set -e` fires and terminates the script mid-loop without cleanup or summary output.

---

## Logic Issues

**F-05: `SPEC_FILE` is set but never used (line 16)**
`SPEC_FILE="$REPO/simulations/draft/specs/signal-scout-$TODAY.md"` is hardcoded to `scout` regardless of `$SKILL_ID`. It's never referenced anywhere in the script. Dead code, and the hardcoded namespace (`scout`) is clearly wrong for non-scout skills.

**F-06: Rubric and variation prompts truncate to `head -80` / `head -200` / `head -100` (lines 122, 147, 150, 229, 231)**
These line-count caps are applied via shell pipe inside the prompt string using `$(cat "$FILE" | head -N)`. For a rubric that grew to v8+ with many criteria, 80 lines may cut it mid-criterion, producing malformed rubric context. The evolve prompt on line 228 uses `head -80` on the current rubric — if that rubric is already 100 lines, the evolution prompt sees a truncated rubric and may drop criteria.

**F-07: `PLATEAU_COUNT` resets on any non-converged round, including rubric-evolve rounds (line 220)**
The intent of `PLATEAU_COUNT` is to require two consecutive stable rounds. But a rubric-evolve round resets the count to 0, which is correct — however the condition on line 212 checks `[ "$ALL_ESSENTIAL" = "true" ] && [ "$NEW_PATTERNS" = "0" ]`. If essential is not passing yet, `PLATEAU_COUNT` resets even when there are no new patterns. This means a skill that never gets all essentials passing will loop to `MAX_ROUNDS` with `PLATEAU_COUNT` always 0, with no early-exit for "hopeless" runs.

**F-08: Simplification pass fallback copies `$LAST_VARIATIONS` instead of the best variation (line 288)**
When QU5 fails, `cp "$LAST_VARIATIONS" "$SIMPLIFIED_FILE"` copies the entire multi-variation file (V-01 through V-05), not just the winning variation. The golden step then reads `$SIMPLIFIED_FILE` as if it contains the winning variation body. This silently produces a malformed golden prompt that contains all 5 variations instead of one.

---

## Security / Injection

**F-09: Shell injection via `$SKILL_ID` inside the Python `-c` inline string (lines 54–62, 361–380)**
`$SKILL_ID` is interpolated directly into Python source code passed to `python -c "..."`. If a caller passes `SKILL_ID` containing a single quote or backslash (e.g., `foo'; import os; os.system('rm -rf /'); #`), the Python code is corrupted or exploited. The existing relay usage is trusted, but it's still a latent injection path. Safer: pass `$SKILL_ID` as a Python `sys.argv` argument (as QU5 already does correctly on line 284).

---

## Style / Minor

**F-10: `cat "$FILE" | head -N` antipattern (lines 122, 147, 150, 229, 231, 251, 252, 324, 327, 330, 333)**
`cat file | head -N` can be replaced with `head -n N "$file"`. Not a bug, but it's a UUOC (Useless Use of Cat) pattern. More relevant here: it means the prompt is assembled via `$()` capture of a piped command, which works but adds unnecessary subshells.

**F-11: `VARS_CONTENT` and `RUBRIC_CONTENT` are assigned but never used (lines 251–252)**
```bash
VARS_CONTENT=$(cat "$LAST_VARIATIONS" | head -100)
RUBRIC_CONTENT=$(cat "$RUBRIC_FILE" | head -60)
```
Both variables are computed and then discarded — the QU5 python script reads the files directly via `sys.argv`. Dead code left over from an earlier version.

**F-12: `LAST_SCORE` type is a string, not a number (line 207)**
`LAST_SCORE=$TOP_SCORE` where `TOP_SCORE` comes from a Python `print()`. It's used in the YAML update as `'GOLDEN (Round $ROUND, score $LAST_SCORE)'` — a string embed — which is fine. But if you ever compare it numerically (e.g., `[ $LAST_SCORE -ge 80 ]`), it will break on an empty or non-numeric value.

---

**Summary table:**

| ID | Severity | Category | Line(s) |
|----|----------|----------|---------|
| F-01 | Medium | Bug | 327, 373, 384 |
| F-02 | High | Bug | 175, 186, 197 |
| F-03 | Medium | Bug | 284 |
| F-04 | Medium | Bug | 9, 181 |
| F-05 | Low | Dead code | 16 |
| F-06 | High | Logic | 122, 147, 150, 229, 231 |
| F-07 | Medium | Logic | 212–220 |
| F-08 | High | Logic | 288 |
| F-09 | Medium | Security | 54–62, 361–380 |
| F-10 | Low | Style | 122+ |
| F-11 | Low | Dead code | 251–252 |
| F-12 | Low | Robustness | 207 |
