Here are all findings, grouped by severity.

---

## Bugs

**B-01 — `SPEC_FILE` is declared but never read (line 16)**
`SPEC_FILE="$REPO/simulations/draft/specs/signal-scout-$TODAY.md"` is set once and never referenced again. Dead code. It also hardcodes `scout` instead of `$SKILL_ID`, so it would be wrong for any non-scout skill even if it were used.

**B-02 — QU5 `mktemp` contradicts the relay-context workaround (line 250)**
`claude_ask` explicitly avoids `mktemp` with the comment "mktemp may return Windows paths in relay context" and uses `/tmp/claude-ask-$$.txt` instead. Line 250 calls `mktemp /tmp/qu5-prompt-XXXXXX.txt` directly — the same problem can occur. Should use the same explicit POSIX path pattern.

**B-03 — QU5 failure fallback copies the entire variations file (line 288)**
```bash
cp "$LAST_VARIATIONS" "$SIMPLIFIED_FILE"
```
`$LAST_VARIATIONS` contains 5 complete variation bodies (V-01 through V-05). The golden step then tries to "extract the winning variation body" from this blob. There is no explicit tracking of which variation won — the golden prompt builder is left to guess. Should copy only the top-scoring variation, or persist its identity.

**B-04 — `VARS_CONTENT` and `RUBRIC_CONTENT` are computed and never used (lines 251–252)**
```bash
VARS_CONTENT=$(cat "$LAST_VARIATIONS" | head -100)
RUBRIC_CONTENT=$(cat "$RUBRIC_FILE" | head -60)
```
The QU5 Python script reads the files directly via `sys.argv[3]` and `sys.argv[4]`. These two assignments are dead code and waste two subprocess invocations.

**B-05 — PyYAML round-trip destroys comments and may alter formatting (line 377)**
`yaml.dump(data, ...)` re-serializes the entire file. Any YAML comments (e.g., section headers, inline notes in `signal.skills.yaml`) are silently dropped. `sort_keys=False` preserves key order but block style vs flow style may still change. Use `ruamel.yaml` for a comment-preserving update, or do a targeted line replacement with `re.sub`.

---

## Security / Correctness

**S-01 — Shell injection via `$SKILL_ID` interpolated into `python -c` strings (lines 54–62, 172–204, 294–309, 361–380)**
```bash
python -c "
...
    if s['id'] == '$SKILL_ID':
...
"
```
A `SKILL_ID` containing a single quote (e.g., `foo'bar`) breaks the Python string literal and could execute arbitrary Python. Same problem with `$SCORECARD_FILE`, `$SIMPLIFIED_FILE`, and `$RUBRIC_FILE` interpolated into Python `open(...)` calls. The QU5 block (lines 253–284) avoids this correctly by passing all values via `sys.argv`. The other four python invocations should do the same, or use `os.environ`.

---

## Quality / Reliability

**Q-01 — Useless use of `cat` before `head` (lines 122, 147, 228, 231, 251, 252, 324, 327, 329, 333)**
```bash
$(cat "$RUBRIC_FILE" | head -80)   # repeated ~8 times
```
Should be `$(head -80 "$RUBRIC_FILE")`. Avoids a fork and a pipe.

**Q-02 — Aggressive context truncation in the score prompt (line 150 and 153)**
The score prompt gives Claude only 200 lines of variations (40 lines per variation) and 800 chars of trace. For complex skills, the scoring model likely can't see a complete variation or a meaningful trace. Consider raising the variations limit to the full file and trace to at least 2000 chars (consistent with the rubric prompt).

**Q-03 — Scorecard capped at 100 lines in the evolve prompt (line 231)**
Excellence signals extracted later in the scorecard document (e.g., ranking section, pattern notes) are cut off before the rubric evolution prompt sees them.

**Q-04 — v1 rubric filename has no version suffix; evolved rubrics do (lines 68 vs 224)**
Initial: `${SKILL_ID}-rubric-$TODAY.md`
Evolved: `${SKILL_ID}-rubric-v${RUBRIC_VERSION}-$TODAY.md` (v starts at 2)

The v1 artifact has no `v1` in its name, so the series is `rubric-DATE.md`, `rubric-v2-DATE.md`, ... which is inconsistent. Consider naming the first file `rubric-v1-DATE.md` so the glob pattern and audit trail are uniform.

**Q-05 — v1 rubric silently overwritten on same-day re-run (line 68)**
`RUBRIC_FILE="$QUEST_DIR/rubrics/${SKILL_ID}-rubric-$TODAY.md"` has no uniqueness guard. Running the script twice on the same day for the same skill overwrites the initial rubric without warning. Evolved rubrics include version numbers so they accumulate. Add a run-ID or timestamp (HH:MM) for the initial file.

**Q-06 — No preflight check for `claude` binary**
The script calls `claude --print` throughout but never checks `command -v claude`. A missing CLI silently produces empty output files and the script runs to "completion" with all-zero scores.

**Q-07 — `set -e` means any Claude API error kills the entire run with no checkpoint**
If Claude fails mid-loop (network error, rate limit), the script exits immediately with no record of which rounds completed. Consider wrapping `claude_ask` calls in explicit error handling that saves partial state before exiting.

**Q-08 — `ls` in command substitution is fragile (line 42)**
```bash
TRACE_FILE=$(ls "$TRACE_DIR"/plugin-${SKILL_ID}-*.md 2>/dev/null | head -1 || true)
```
`ls` output is not reliable for parsing (can differ by locale, coloring). If filenames contain spaces it breaks. Prefer a glob in bash: `for f in "$TRACE_DIR"/plugin-${SKILL_ID}-*.md; do ... break; done` or `find ... -name ... -print -quit`.

**Q-09 — No inter-run locking**
The header says "P-01 concurrent by default" but two simultaneous invocations for the same `SKILL_ID` will race on `$RUBRIC_FILE` (read-write from multiple rounds), `signal.skills.yaml` (concurrent YAML rewrite), and the temp file `/tmp/claude-ask-$$.txt` (different PIDs so safe, actually fine here). The YAML write in Step 5 is the main race risk.

---

## Summary Table

| ID | Category | Severity | Line(s) |
|----|----------|----------|---------|
| B-01 | Bug | Medium | 16 |
| B-02 | Bug | Medium | 250 |
| B-03 | Bug | High | 288 |
| B-04 | Bug | Low | 251–252 |
| B-05 | Bug | Medium | 377 |
| S-01 | Security | High | 54–62, 172–204, 294–309, 361–380 |
| Q-01 | Quality | Low | 8 occurrences |
| Q-02 | Quality | Medium | 150, 153 |
| Q-03 | Quality | Medium | 231 |
| Q-04 | Quality | Low | 68, 224 |
| Q-05 | Quality | Low | 68 |
| Q-06 | Quality | Medium | — |
| Q-07 | Quality | Medium | 9, 33 |
| Q-08 | Quality | Low | 42 |
| Q-09 | Quality | Low | — |

**Highest priority to fix:** B-03 (wrong fallback content reaches golden), S-01 (shell injection in Python inlines), and B-05 (YAML comment destruction).
