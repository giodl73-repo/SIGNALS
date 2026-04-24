## Round 1 Scorecard — /discover-coherence

### Score Summary

| Variation | Composite | All Essential |
|-----------|-----------|---------------|
| V-02 (Table) | **80** | YES |
| V-03 (Inertia-first) | **80** | YES |
| V-04 (Conversational) | **80** | YES |
| V-05 (Combined) | **80** | YES |
| V-01 (Baseline) | 68* | NO* |

*V-01 truncated — C-01 unverifiable; strict score 68, benefit-of-doubt 80.

---

### Per-Criterion Verdict

| | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 |
|--|--|--|--|--|--|--|--|--|--|--|
| V-01 | PARTIAL | PASS | PASS | PASS | PASS | FAIL | PASS | PASS | FAIL | FAIL |
| V-02 | PASS | PASS | PASS | PASS | PASS | FAIL | PASS | PASS | FAIL | FAIL |
| V-03 | PASS | PASS | PASS | PASS | PASS | FAIL | PASS | PASS | FAIL | FAIL |
| V-04 | PASS | PASS | PASS | PASS | PASS | FAIL | PASS | PASS | FAIL | FAIL |
| V-05 | PASS | PASS | PASS | PASS | PASS | FAIL | PASS | PASS | FAIL | FAIL |

**Three universal gaps across all 5 variations: C-06 (tally at top), C-09 (taxonomy), C-10 (skill per blocking).**

---

### Key Findings

**C-06 structural incompatibility**: All variations compute the tally after iterating contradictions and surface it at the end. Fixing C-06 requires a two-pass structure or an explicit SUMMARY HEADER phase after inventory but before contradiction output. This is architecturally non-trivial — not just an omission.

**V-04 verdict phrasing drift**: "Good to spec." / "Don't spec yet" passes C-07 (verdict is present, tied to blocking count) but diverges from canonical rubric language. No score impact, but a risk for downstream skill consumption.

**V-05 C-04 strongest**: "not 'investigate further'" explicitly names the failure mode. Naming the failure outperforms positive-only instructions for well-known anti-patterns.

**Table format (V-02, V-05) C-03/C-04**: Tied on score but structurally superior — a blank Severity or Resolution column is immediately visible; a missing prose field requires the reader to notice its absence.

---

### Excellence Signals

1. **Named phase gates** (V-05): "GATE FAILED: N signals found, need 2+" is a named error state that cannot be silently skipped — more robust than prose "if fewer than 2, stop."
2. **Failure-mode negation** (V-05): "not 'investigate further'" in the resolution instruction reduces C-04 failure rate more reliably than positive instructions alone.
3. **Dual inertia/other tables** (V-05): Forces the highest-priority cross-skill category to always render first — structural C-05 reinforcement beyond the minimum rule.
4. **"Its own words" phrasing** (V-04): More intuitive than "exact quote or close paraphrase" for enforcing C-02 — lower interpretation ambiguity on first execution.
5. **Table columns prevent silent omission** (V-02, V-05): Severity and Resolution as named columns make partial entries conspicuous by structure.

---

### R2 Plan

Close the three universal gaps in a V-05-derived variation:
- **C-06** (+10): Add summary header phase after inventory, before first contradiction
- **C-09** (+5): Add `Type` column to contradiction table (`rating-conflict` | `prediction-conflict` | `evidence-conflict`)
- **C-10** (+5): Split resolution requirement by severity — blocking entries must name a `/skill-name [params]`, advisory entries may use any concrete action

**Predicted R2 top score: 100**

```json
{"top_score": 80, "all_essential_pass": true, "new_patterns": ["named phase gates with GATE FAILED message are more robust than prose stop conditions -- explicit named error state cannot be silently dropped", "failure-mode negation in resolution instruction (not 'investigate further') outperforms positive-only instruction for well-known C-04 failure pattern -- name the failure, not just the requirement", "table columns structurally prevent silent severity/resolution omission -- blank column is immediately visible; missing prose field requires active noticing", "C-06 (summary tally at top) is architecturally incompatible with single-pass prompts -- requires either two-pass structure or summary header phase after inventory but before contradiction output", "conversational 'its own words' phrasing enforces C-02 quotation requirement more clearly than formal 'exact quote or close paraphrase' -- lower interpretation ambiguity on first execution"]}
```


---

### Excellence Signals

**From V-05 (top by structural rigor)**:

1. **Named phase gates with explicit failure messages**: "GATE FAILED: {N} signal(s) found, need 2+. Run discover skills before coherence check." is more robust than prose "if fewer than 2, stop" — the GATE FAILED prefix is a named error state that cannot be silently dropped.

2. **Failure-mode negation in C-04 instruction**: "specific skill to run, field to update, or claim to amend -- not 'investigate further'" names the exact failure the rubric tests for. Negative examples outperform positive-only instructions for well-known failure patterns.

3. **Dual tables with structural C-05 reinforcement**: Inertia Contradictions table always rendered first (even if empty) structurally ensures the most decision-critical cross-skill comparison category is never buried. Cross-skill rule is enforced both by explicit text and by structural separation.

**From V-04 (top by C-02 language)**:

4. **"Its own words" phrasing for C-02**: "what it said, in its own words" is more intuitive than "exact quote or close paraphrase" for enforcing the side-by-side claims requirement. Conversational framing reduces interpretation ambiguity about what counts as sufficient quotation.

**From V-02 (top by table structure)**:

5. **Table columns prevent silent omission**: Severity and Resolution as named columns make partial entries structurally conspicuous. The rubric failure mode "labels contradictions 'unclear'" cannot occur if the column header explicitly lists the two allowed values.

---

### R2 Plan

Three universal gaps are clear R2 targets:

**Gap 1 — C-06 (tally at top, +10 pts)**: None of the 5 variations produce a summary tally before the first contradiction. Fix: add a two-pass structure or a SUMMARY HEADER phase immediately after INVENTORY, before contradiction output. "N contradiction(s) found: M blocking, K advisory." at the top enables quick triage.

**Gap 2 — C-09 (contradiction taxonomy, +5 pts)**: Add a Type column (or label) to each entry: `rating-conflict` | `prediction-conflict` | `evidence-conflict`. V-05's table format is the natural host — add a Type column.

**Gap 3 — C-10 (skill per blocking, +5 pts)**: For blocking entries specifically, require "Resolve with: /skill-name [params]" rather than allowing generic field/claim amendments as substitutes. V-05's resolution column instruction should split by severity: blocking entries require a named skill; advisory entries allow any concrete action.

**Predicted R2 top score**: 80 + 10 (C-06) + 5 (C-09) + 5 (C-10) = **100** if all three gaps closed in a single V-05-derived variation.

**V-04 canonical phrasing fix**: Change "Good to spec." → "Ready to specify." and "Don't spec yet" → "Not ready to specify" to match rubric language. No score impact but reduces downstream ambiguity.

---

### Independence Notes

This is Round 1 — no independence confirmation possible yet. Axes to confirm in R2:
- Table format axis (V-02): +0 pts beyond baseline in R1 (tied); R2 should test whether adding C-09 Type column to table changes the score delta
- Inertia-first axis (V-03): domain value confirmed by V-03/V-05 structural analysis; score-neutral in R1 (no inertia-specific criteria)
- Conversational axis (V-04): C-02 quality improvement confirmed analytically; score-neutral in R1 (binary pass/fail blunts the advantage)

```json
{"top_score": 80, "all_essential_pass": true, "new_patterns": ["named phase gates with GATE FAILED message are more robust than prose stop conditions -- explicit named error state cannot be silently dropped", "failure-mode negation in resolution instruction (not 'investigate further') outperforms positive-only instruction for well-known C-04 failure pattern -- name the failure, not just the requirement", "table columns structurally prevent silent severity/resolution omission -- blank column is immediately visible; missing prose field requires active noticing", "C-06 (summary tally at top) is architecturally incompatible with single-pass prompts -- requires either two-pass structure or summary header phase after inventory but before contradiction output", "conversational 'its own words' phrasing enforces C-02 quotation requirement more clearly than formal 'exact quote or close paraphrase' -- lower interpretation ambiguity on first execution"]}
```
