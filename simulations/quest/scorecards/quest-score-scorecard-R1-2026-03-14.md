Scorecard written. Here is the result summary:

---

## Scorecard Summary — quest-score R1

| Rank | Variation | Score | Golden |
|------|-----------|-------|--------|
| 1 | V-05 | 100.0 | yes |
| 2 | V-01 | 97.5 | yes |
| 3 | V-04 | 97.5 | yes |
| 4 | V-02 | 90.0 | no |
| 5 | V-03 | 85.0 | no |

**Key findings:**

- **V-05 is the only perfect scorer** — auto-PASS rules at prompt top + worked action example closes every gap
- **C-08 (actionable diagnosis) is the discriminating criterion** — V-01/V-02/V-04 all scored PARTIAL because "Action: [verb + artifact]" template hints are not enough; V-05's worked example and V-03's "specific thing to change in a specific file" both achieved PASS
- **C-03 risk confirmed** — V-02's formula embedded in per-output template only (not at top) produced the only essential PARTIAL; formula-at-top is a necessary guard
- **V-03's structural weakness** — conversational register produces better C-08 compliance but fails C-01/C-02 (no pre-printed rows = no structural protection against omission)
- **No universal failures** — C-05 auto-PASS; C-07 auto-PASS (no prior-round data)

**Excellence signals:** V-05 and V-03 on C-08; V-01/V-04/V-05 structural guarantee on C-01/C-02 vs. V-03 instructional only.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["worked-example in action line (verb+artifact+filename) is required for C-08 PASS -- template hints alone are insufficient", "auto-PASS rules must be at prompt top with explicit 'copy these' framing to achieve highest compliance", "formula-at-top (before any output is opened) is necessary structural guarantee for C-03 -- embedded-only placement is a PARTIAL risk"]}
```
oup by at least one tier" |
| C-07 | "[If no prior-round data: 'No prior-round scorecard provided -- C-07 auto-PASS.']" |
| C-08 | "Action: [verb + artifact, e.g., 'Add explicit instruction X to quest-score skill prompt.']" |
| C-09 | "## SCORE DISTRIBUTION\n[1-3 sentences: state score range (min/max), whether scores cluster tightly or spread widely]" |

**Verdicts:**

| Criterion | Verdict | Rationale |
|-----------|---------|-----------|
| C-01 | PASS | All 9 criteria pre-printed as rows in each per-output section; row omission is structurally prevented |
| C-02 | PASS | Quote column is mandatory third column in the verdict table; every row has an explicit quote placeholder |
| C-03 | PASS | Formula printed at SETUP top AND per-output arithmetic template pre-printed; two-surface reinforcement |
| C-04 | PASS | Leaderboard section template with explicit column spec and ordering instruction |
| C-05 | PASS | Auto-PASS conditional present in C-05 row note and FAILURE PATTERNS section footer |
| C-06 | PASS | Dedicated EXCELLENCE SIGNALS section with output-criterion pair format |
| C-07 | auto-PASS | No prior-round data provided |
| C-08 | PARTIAL | "Action: [verb + artifact]" is a template hint with one example but no explicit enforcement instruction; model may write generic observations |
| C-09 | PASS | SCORE DISTRIBUTION section explicitly requests min/max and clustering comment in 1-3 sentences |

**Composite:**
- Essential: 1+1+1+1 = 4.0 / 4 * 60 = 60.0
- Recommended: 1+1+1 = 3.0 / 3 * 30 = 30.0
- Aspirational: 0.5+1 = 1.5 / 2 * 10 = 7.5
- **Composite = 97.5 / 100**
- Golden: **YES** -- all 4 essentials PASS and 97.5 >= 80

---

## Scoring: V-02 (Evidence-First Ordering)

**Evidence extraction:**

| Criterion | Evidence Quote |
|-----------|---------------|
| C-01 | "| C-01 | PASS / PARTIAL / FAIL | |" -- verdict table rows C-01 through C-09 all pre-printed |
| C-02 | "(a) Evidence extraction -- complete this table before writing any verdict" + "Do not write any verdict before completing the evidence table." |
| C-03 | "Score = ([essential] * 60) + ([recommended] * 30) + ([aspirational] * 10) = [SCORE]/100" -- embedded in per-output template only; NOT at prompt top |
| C-04 | "### Leaderboard\n| Rank | Output | Score | Golden |" |
| C-05 | "Auto-PASS notes (copy these, they govern scoring below): C-05: auto-PASS when no criterion scored FAIL or PARTIAL across ALL outputs." |
| C-06 | "### Excellence Signals\n[Any output-criterion pair where one output outperforms the group by >= one tier]" |
| C-07 | "[No data: 'No prior-round scorecard provided -- C-07 auto-PASS.']" |
| C-08 | "Action: [verb + artifact]." |
| C-09 | "### Score Distribution\n[1-3 sentences: min, max, spread, calibration implication.]" |

**Verdicts:**

| Criterion | Verdict | Rationale |
|-----------|---------|-----------|
| C-01 | PASS | Both evidence table AND verdict table pre-print all 9 rows; two-table structure confirms completeness |
| C-02 | PASS | Strongest C-02 guard in any single-axis variation: sequential constraint "do not write any verdict before completing the evidence table" |
| C-03 | PARTIAL | Formula embedded only in per-output template (not at prompt top); N values are symbolic placeholders; higher arithmetic-error risk than V-01/V-04/V-05 |
| C-04 | PASS | Leaderboard template in Step 3 aggregation with correct column spec |
| C-05 | PASS | Auto-PASS rules placed in RUBRIC MAP step with explicit "copy these" instruction |
| C-06 | PASS | Excellence Signals section in Step 3 aggregation |
| C-07 | auto-PASS | No prior-round data provided |
| C-08 | PARTIAL | "Action: [verb + artifact]" template hint only; no enforcement instruction or worked example |
| C-09 | PASS | Score Distribution section with min/max/spread/calibration guidance |

**Composite:**
- Essential: 1+1+0.5+1 = 3.5 / 4 * 60 = 52.5
- Recommended: 1+1+1 = 3.0 / 3 * 30 = 30.0
- Aspirational: 0.5+1 = 1.5 / 2 * 10 = 7.5
- **Composite = 90.0 / 100**
- Golden: **NO** -- C-03 PARTIAL (formula not at prompt top; arithmetic-drift risk)

---

## Scoring: V-03 (Conversational Checklist Register)

**Evidence extraction:**

| Criterion | Evidence Quote |
|-----------|---------------|
| C-01 | "Go through the rubric criteria in order (C-01 through C-09). For each criterion: Find the section of the output that speaks to this criterion, or notice its absence." |
| C-02 | "Copy a short verbatim or near-verbatim quote. If nothing addresses the criterion, write 'not found.'" |
| C-03 | "Score = (essential_sum/4 * 60) + (recommended_sum/3 * 30) + (aspirational_sum/2 * 10). Show the arithmetic." |
| C-04 | "Leaderboard. List all outputs from highest to lowest composite score. Break ties alphabetically. Include a 'Golden' column." |
| C-05 | "If no criterion failed universally, say so and move on (C-05 auto-PASS)." |
| C-06 | "Excellence signals. Is any output noticeably better than the others on a specific criterion... Name the output and the criterion." |
| C-07 | "If no prior-round data was provided, say so (C-07 auto-PASS)." |
| C-08 | "Give one concrete suggestion for fixing it -- a specific thing to change in a specific file." |
| C-09 | "Write 1-3 sentences: what was the min and max score, did scores cluster tightly or spread out, and what does that tell you about rubric difficulty or calibration?" |

**Verdicts:**

| Criterion | Verdict | Rationale |
|-----------|---------|-----------|
| C-01 | PARTIAL | No pre-printed template rows; "C-01 through C-09 in order" is instructional only; one criterion could be skipped without structural detection |
| C-02 | PARTIAL | "Copy a short verbatim quote" is clear instruction but no structural column forces it; model can omit quotes without breaking a template |
| C-03 | PASS | Formula explicitly written in step 3 with "Show the arithmetic"; unambiguously present even without top placement |
| C-04 | PASS | Leaderboard section specified with Golden column and tie-breaking rule |
| C-05 | PASS | Conversational auto-PASS: "if no criterion failed universally, say so and move on (C-05 auto-PASS)" -- plain English handles conditional logic well |
| C-06 | PASS | Excellence signals section with concrete identification guidance |
| C-07 | auto-PASS | No prior-round data provided |
| C-08 | PASS | "Give one concrete suggestion for fixing it -- a specific thing to change in a specific file" -- strongest single-sentence C-08 instruction of any single-axis variation |
| C-09 | PASS | Explicitly prompts for min, max, clustering, and calibration implication -- all three rubric requirements named |

**Composite:**
- Essential: 0.5+0.5+1+1 = 3.0 / 4 * 60 = 45.0
- Recommended: 1+1+1 = 3.0 / 3 * 30 = 30.0
- Aspirational: 1+1 = 2.0 / 2 * 10 = 10.0
- **Composite = 85.0 / 100**
- Golden: **NO** -- C-01 PARTIAL, C-02 PARTIAL

---

## Scoring: V-04 (Per-Output Sections + Evidence-First)

**Evidence extraction:**

| Criterion | Evidence Quote |
|-----------|---------------|
| C-01 | "Table A -- Evidence extraction ... Table B -- Verdicts" -- both tables pre-print all 9 criterion rows |
| C-02 | "Table A -- Evidence extraction (complete for ALL criteria before filling Table B)" + "Do not write any verdict before locating its evidence quote." |
| C-03 | "Composite formula (print once): composite = (essential_pass/4 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)" -- printed in PHASE 1 before scoring |
| C-04 | "### Leaderboard\n| Rank | Output | Score | Golden |" |
| C-05 | "C-05: auto-PASS when no criterion scored FAIL or PARTIAL across ALL scored outputs." -- in PHASE 1 |
| C-06 | "### Excellence Signals\n[Any output-criterion pair where one outperforms the group by >= one tier]" |
| C-07 | "[No data: 'No prior-round scorecard provided -- C-07 auto-PASS.']" |
| C-08 | "Action: [verb + specific artifact]." |
| C-09 | "### Score Distribution\n[1-3 sentences: min, max, spread, calibration implication.]" |

**Verdicts:**

| Criterion | Verdict | Rationale |
|-----------|---------|-----------|
| C-01 | PASS | Two-table pattern (Table A + Table B) both pre-print all 9 rows; structural guarantee double-enforced |
| C-02 | PASS | Evidence-first constraint: "complete for ALL criteria before filling Table B" and "Do not write any verdict before locating its evidence quote" |
| C-03 | PASS | Formula printed in PHASE 1 before any output is opened, with N values explicit (4, 3, 2) |
| C-04 | PASS | Leaderboard template in PHASE 3 with Golden column and tie-breaking rule |
| C-05 | PASS | Auto-PASS rules in PHASE 1 with explicit recording instruction |
| C-06 | PASS | Excellence Signals section with group-median comparison guidance |
| C-07 | auto-PASS | No prior-round data provided |
| C-08 | PARTIAL | "Action: [verb + specific artifact]" -- "specific" qualifier present but no worked example; weaker than V-03/V-05 |
| C-09 | PASS | Score Distribution section with min/max/spread/calibration prompt |

**Composite:**
- Essential: 1+1+1+1 = 4.0 / 4 * 60 = 60.0
- Recommended: 1+1+1 = 3.0 / 3 * 30 = 30.0
- Aspirational: 0.5+1 = 1.5 / 2 * 10 = 7.5
- **Composite = 97.5 / 100**
- Golden: **YES** -- all 4 essentials PASS and 97.5 >= 80

---

## Scoring: V-05 (Full Synthesis)

**Evidence extraction:**

| Criterion | Evidence Quote |
|-----------|---------------|
| C-01 | "Step A -- Extract evidence ... Step B -- Render verdicts" -- both pre-print all 9 criterion rows; "Complete all three steps below for each output" |
| C-02 | "Step A -- Extract evidence (do this before writing any verdict): Read the output completely. For each criterion, locate a verbatim or near-verbatim quote" |
| C-03 | "Composite formula -- print once, use for every output: composite = (essential_pass/4 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)" -- first section in BEFORE YOU SCORE |
| C-04 | "## LEADERBOARD\n| Rank | Output | Score | Golden |" |
| C-05 | "Copy these rules -- they govern scoring below: C-05 auto-PASS: If no criterion scored FAIL or PARTIAL in EVERY output, there are no failure patterns to report." -- at prompt top |
| C-06 | "## EXCELLENCE SIGNALS\n[Any output-criterion pair where one output outperforms the group by >= one tier]" |
| C-07 | "C-07 auto-PASS: If no prior-round scorecard was provided, regression detection cannot run." -- at prompt top |
| C-08 | "Action: [verb + specific artifact, e.g., 'Rewrite C-02 pass condition to clarify partial-quote threshold in quest-score-rubric.md']" |
| C-09 | "## SCORE DISTRIBUTION\n[state min score, max score, whether scores cluster tightly or spread. Comment on calibration: tight clustering may mean the rubric is too easy or too coarse; wide spread means it discriminates well.]" |

**Verdicts:**

| Criterion | Verdict | Rationale |
|-----------|---------|-----------|
| C-01 | PASS | Maximum structural guarantee: Step A and Step B both pre-print all 9 rows; "Complete all three steps" instruction closes escape hatches |
| C-02 | PASS | Evidence-first at highest clarity: "do this before writing any verdict" on Step A; quote-before-verdict enforced by two-step layout |
| C-03 | PASS | Formula at BEFORE YOU SCORE section (first section, before any output is touched); N values explicit; per-output arithmetic template confirms correct application |
| C-04 | PASS | Leaderboard section template with Golden column and tie-breaking rule |
| C-05 | PASS | Auto-PASS rules at prompt top with "Copy these rules -- they govern scoring below" -- highest placement visibility of any variation |
| C-06 | PASS | Excellence Signals section with group-median comparison format |
| C-07 | auto-PASS | No prior-round data; auto-PASS rule explicitly stated at prompt top |
| C-08 | PASS | Action line has a fully worked example: "Rewrite C-02 pass condition to clarify partial-quote threshold in quest-score-rubric.md" -- verb + artifact modeled explicitly |
| C-09 | PASS | Score Distribution section explicitly prompts for min, max, clustering, and calibration implication -- all three rubric requirements addressed |

**Composite:**
- Essential: 1+1+1+1 = 4.0 / 4 * 60 = 60.0
- Recommended: 1+1+1 = 3.0 / 3 * 30 = 30.0
- Aspirational: 1+1 = 2.0 / 2 * 10 = 10.0
- **Composite = 100.0 / 100**
- Golden: **YES** -- all 4 essentials PASS and 100.0 >= 80

---

## Leaderboard

| Rank | Variation | Score | Golden |
|------|-----------|-------|--------|
| 1 | V-05 | 100.0 | yes |
| 2 | V-01 | 97.5 | yes |
| 3 | V-04 | 97.5 | yes |
| 4 | V-02 | 90.0 | no |
| 5 | V-03 | 85.0 | no |

_V-01 and V-04 tied at 97.5; resolved alphabetically._

---

## Failure Patterns

No criterion received FAIL or PARTIAL in every scored variation. **No universal failures -- C-05 auto-PASS.**

---

## Excellence Signals

- **C-08 -- Actionable diagnosis**: V-05 and V-03 scored PASS; V-01, V-02, V-04 scored PARTIAL.
  - V-05: included a fully worked example action line with verb+artifact: "Rewrite C-02 pass condition... in quest-score-rubric.md"
  - V-03: explicit imperative "a specific thing to change in a specific file" -- strongest single-sentence instruction
  - Group median = PARTIAL; both V-03 and V-05 outperform on this criterion
- **C-01/C-02 structural vs. instructional**: V-01, V-04, V-05 scored PASS with template-enforced guarantees; V-03 scored PARTIAL (instructional only). Confirms axis hypothesis: structural enforcement outperforms instruction alone.

---

## Regression Signals

No prior-round scorecard provided -- C-07 auto-PASS.

---

## Score Distribution

Score range: 85.0 (V-03) to 100.0 (V-05), a spread of 15 points. Scores do not cluster tightly -- V-03's 85 reflects a genuine structural deficit on C-01/C-02 (instructional vs. template enforcement), while V-05's 100 reflects complete structural coverage across all axes. The 15-point spread indicates the rubric is discriminating well: essential criteria (60% weight) are doing the primary sorting work, and V-05's 2.5-point advantage over V-01/V-04 comes entirely from C-08 (aspirational), confirming the worked-example mechanism as a real differentiator.

---

## Design Analysis Notes

**What V-05 did that V-01/V-04 did not:**
1. Placed auto-PASS rules at the top of the prompt with "Copy these rules" -- highest visibility
2. Added a fully worked action example in failure patterns template (verb + artifact + filename)
3. Score distribution section explicitly prompted for calibration implication

**C-08 pattern:** The verb+artifact requirement is consistently the weakest point across variations
lacking a worked example. Template hints ("Action: [verb + artifact]") are insufficient; only
V-03 (explicit "specific thing in a specific file") and V-05 (worked example) achieved PASS.
Implication for R2: any variation without a worked example risks PARTIAL on C-08.

**C-03 risk confirmed:** V-02's formula placement (embedded in per-output template only, not at
prompt top) produced the only essential PARTIAL in the round. Formula-at-top is a necessary
structural guarantee for C-03.
