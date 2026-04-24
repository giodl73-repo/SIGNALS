## quest-score Scorecard — Round 2

---

## SETUP

- **Rubric:** quest-score rubric v2 — 12 criteria (4 essential, 3 recommended, 5 aspirational)
- **Outputs to score:** V-01, V-02, V-03, V-04, V-05
- **Prior-round scorecard:** quest-score-scorecard-R1-2026-03-14.md — provided
- **Scoring date:** 2026-03-14

### Criterion Roster

| ID | Name | Tier | Auto-PASS status for this run |
|----|------|------|-------------------------------|
| C-01 | Per-criterion verdicts present | essential | -- |
| C-02 | Evidence quote for every verdict | essential | -- |
| C-03 | Composite score computed correctly | essential | -- |
| C-04 | Ranked leaderboard present | essential | -- |
| C-05 | Failure patterns surfaced | recommended | TBD |
| C-06 | Excellence signals surfaced | recommended | -- |
| C-07 | Regression signals surfaced | recommended | -- (prior-round data provided; scoring required) |
| C-08 | Actionable diagnosis in failure patterns | aspirational | TBD |
| C-09 | Score distribution commentary | aspirational | -- |
| C-10 | Worked example in action line | aspirational | TBD |
| C-11 | Auto-PASS rules stated in preamble | aspirational | -- |
| C-12 | Formula reproduced before first output section | aspirational | -- |

### Composite Formula (v2 N values)

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 5.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

---

## SCORING

### OUTPUT: V-01 — Criterion Roster Up-Front

| Criterion | Verdict | Evidence Quote |
|-----------|---------|----------------|
| C-01 Verdicts present | PASS | "C-01 Verdicts present … C-12 Formula at preamble" — all 12 rows pre-printed in scoring template table |
| C-02 Evidence quotes | PASS | Mandatory three-column table: "Criterion \| Verdict \| Evidence Quote" — every row has a quote slot, structural enforcement |
| C-03 Composite score | PASS | "composite = (essential_pass / 4 * 60) + … N_aspirational = 5" printed in SETUP before any output + per-output arithmetic template with correct denominators |
| C-04 Leaderboard | PASS | "## LEADERBOARD / Rank all outputs from highest to lowest composite score. Ties resolved alphabetically." with column spec |
| C-05 Failure patterns | PASS | "[If no universal failures: 'No universal failures — C-05 auto-PASS.']" — both branches covered; TBD mechanism in roster |
| C-06 Excellence signals | PASS | "## EXCELLENCE SIGNALS / For each output-criterion pair where one output outperforms the group by >= one tier" |
| C-07 Regression signals | PASS | "[Prior-round scorecard provided: list every output-criterion pair that regressed (PASS -> FAIL or PARTIAL).]" — handles the provided case |
| C-08 Actionable diagnosis | PASS | "Action: [fully instantiated — verb + artifact + location, e.g., 'Add a 12-row criterion roster to quest-score.md SETUP block so C-10/C-11/C-12 rows are pre-printed for every run.']" — worked example present |
| C-09 Score distribution | PASS | "## SCORE DISTRIBUTION / [1-3 sentences: state min score, max score, spread, and calibration implication.]" |
| C-10 Worked example | PARTIAL | Template says "[fully instantiated — verb + artifact + location, e.g., …]" with a concrete worked example but no explicit "do NOT write a placeholder" prohibition; model may output the template framing verbatim |
| C-11 Auto-PASS in preamble | PASS | Criterion Roster in SETUP has "Auto-PASS status for this run" column with TBD/auto-PASS entries for C-05/C-07/C-08/C-10 — preamble block before any output section |
| C-12 Formula at preamble | PASS | "### Composite Formula (v2 N values)" with N_aspirational=5 in SETUP section, before "Do not open any output file until SETUP is complete" |

```
Essential:    1+1+1+1 = 4.0 / 4 * 60 = 60.0
Recommended:  1+1+1 = 3.0 / 3 * 30 = 30.0
Aspirational: 1+1+0.5+1+1 = 4.5 / 5 * 10 = 9.0
Composite = 60.0 + 30.0 + 9.0 = 99.0/100
Golden: YES — all 4 essentials PASS and 99.0 >= 80
```

---

### OUTPUT: V-02 — Diagnostic-Question Register

| Criterion | Verdict | Evidence Quote |
|-----------|---------|----------------|
| C-01 Verdicts present | PASS | "C-01 Verdicts present … C-12 Formula at preamble" — all 12 rows in diagnostic table with criterion-specific questions |
| C-02 Evidence quotes | PASS | Four-column table: "Criterion \| Diagnostic Question \| Evidence Quote \| Verdict" — evidence quote before verdict; "Write the evidence quote, then the verdict; never the reverse" |
| C-03 Composite score | PASS | "composite = (essential_pass / 4 * 60) + … N_aspirational = 5" in PREAMBLE section + per-output arithmetic with all 5 aspirational terms |
| C-04 Leaderboard | PASS | "## LEADERBOARD / Rank \| Output \| Score \| Golden" with "Ties resolved alphabetically" |
| C-05 Failure patterns | PASS | "[None: 'No universal failures — C-05 auto-PASS.']" — TBD auto-PASS declared in PREAMBLE table |
| C-06 Excellence signals | PASS | "## EXCELLENCE SIGNALS / [Any output-criterion pair outperforming the group by >= one tier:]" |
| C-07 Regression signals | PASS | "[Provided: list every output-criterion pair that regressed (PASS -> FAIL or PARTIAL).]" |
| C-08 Actionable diagnosis | PASS | "Action: [fully worked example: verb + artifact name + section, e.g., 'Add a preamble gate section to quest-score.md (before any SCORING heading) requiring auto-PASS declarations for C-05, C-07, C-08, and C-10.']" |
| C-09 Score distribution | PASS | "## SCORE DISTRIBUTION / [1-3 sentences: min score, max score, spread, calibration implication.]" |
| C-10 Worked example | PARTIAL | Diagnostic question "Is each action line fully instantiated — naming a real artifact and location — rather than left as a fill-in-the-blank placeholder?" interrogates the criterion but no "do NOT write a placeholder" output mandate |
| C-11 Auto-PASS in preamble | PASS | "## PREAMBLE / ### Auto-PASS Declaration" table with C-05/C-07/C-08/C-10 rows, "TBD (resolve after scoring)" justifications — preamble before first output |
| C-12 Formula at preamble | PASS | "### Composite Formula (v2 N values)" with N_essential=4, N_recommended=3, N_aspirational=5 in PREAMBLE, before first output section; "Preamble is complete. Open output files only after this section is written." |

```
Essential:    1+1+1+1 = 4.0 / 4 * 60 = 60.0
Recommended:  1+1+1 = 3.0 / 3 * 30 = 30.0
Aspirational: 1+1+0.5+1+1 = 4.5 / 5 * 10 = 9.0
Composite = 60.0 + 30.0 + 9.0 = 99.0/100
Golden: YES — all 4 essentials PASS and 99.0 >= 80
```

---

### OUTPUT: V-03 — Two-Gate Preamble

| Criterion | Verdict | Evidence Quote |
|-----------|---------|----------------|
| C-01 Verdicts present | PASS | "C-01 Verdicts present … C-12 Formula at preamble" — all 12 rows pre-printed in PHASE 2 scoring template; explicit structural enforcement from R1's weakness |
| C-02 Evidence quotes | PASS | Three-column "Criterion \| Verdict \| Evidence Quote" table in PHASE 2 — structural column enforcement |
| C-03 Composite score | PASS | "composite = (essential_pass / 4 * 60) + … N_aspirational = 5" in PHASE 1 Step 1.2 + per-output arithmetic template with all 5 aspirational terms |
| C-04 Leaderboard | PASS | "### Leaderboard / Rank \| Output \| Score \| Golden" in PHASE 3; tie-breaking specified |
| C-05 Failure patterns | PASS | "[None: 'No universal failures — C-05 auto-PASS.']" — TBD declared in PHASE 1 Step 1.3 table, resolved in PHASE 3 |
| C-06 Excellence signals | PASS | "### Excellence Signals / [Any output-criterion pair outperforming the group by >= one tier:]" |
| C-07 Regression signals | PASS | "[Prior-round data provided: list every output-criterion pair that regressed.]" |
| C-08 Actionable diagnosis | PASS | "Action: [fully instantiated verb + artifact + location, e.g., 'Add a mandatory PHASE 1 PREAMBLE gate to quest-score.md that requires formula and auto-PASS declarations before any per-output SCORING section is rendered.']" |
| C-09 Score distribution | PASS | "### Score Distribution / [1-3 sentences: min, max, spread, calibration implication.]" |
| C-10 Worked example | PARTIAL | "[fully instantiated verb + artifact + location, e.g., …]" template with concrete example but no explicit prohibition on leaving the template unfilled |
| C-11 Auto-PASS in preamble | PASS | "### Step 1.3 — Auto-PASS Declaration" table in PHASE 1 with Justification column: "Cannot determine before scoring" — most explicit justification phrase of all V-01/V-03/V-04 |
| C-12 Formula at preamble | PASS | "### Step 1.2 — Composite Formula (print with v2 N values)" in PHASE 1 before any PHASE 2 section; "Proceed to Phase 2 only after Phase 1 is complete" gate |

```
Essential:    1+1+1+1 = 4.0 / 4 * 60 = 60.0
Recommended:  1+1+1 = 3.0 / 3 * 30 = 30.0
Aspirational: 1+1+0.5+1+1 = 4.5 / 5 * 10 = 9.0
Composite = 60.0 + 30.0 + 9.0 = 99.0/100
Golden: YES — all 4 essentials PASS and 99.0 >= 80
```

---

### OUTPUT: V-04 — Criterion Roster + Two-Gate Preamble

| Criterion | Verdict | Evidence Quote |
|-----------|---------|----------------|
| C-01 Verdicts present | PASS | "Table A — Evidence extraction (complete ALL 12 rows before filling Table B)" + "Table B — Verdicts" — both tables pre-print all 12 rows; double-enforcement |
| C-02 Evidence quotes | PASS | "Do not open any output file before Phase 1 is complete" + two-table structure requires Table A (quotes) before Table B (verdicts) for all 12 criteria |
| C-03 Composite score | PASS | "composite = (essential_pass / 4 * 60) + … N_aspirational = 5" in PHASE 1 Composite Formula section + per-output arithmetic with explicit [sum]/5 term |
| C-04 Leaderboard | PASS | "### Leaderboard / Rank \| Output \| Score \| Golden" in PHASE 3 |
| C-05 Failure patterns | PASS | "[None: 'No universal failures — C-05 auto-PASS.']" — TBD in Phase 1 roster, resolved at Phase 3 |
| C-06 Excellence signals | PASS | "### Excellence Signals / [Any output-criterion pair where one outperforms the group by >= one tier:]" |
| C-07 Regression signals | PASS | "[Prior-round data provided: list regressions or 'No regressions detected.']" |
| C-08 Actionable diagnosis | PASS | "Action: [fully instantiated — verb + artifact + section, e.g., 'Add criterion roster (12 rows, with auto-PASS column) to quest-score.md PHASE 1 PREAMBLE block.']" |
| C-09 Score distribution | PASS | "### Score Distribution / [1-3 sentences: min, max, spread, calibration implication.]" |
| C-10 Worked example | PARTIAL | Table A C-10 row: "[quote showing fully instantiated action line (real artifact + location, no placeholder), or: auto-PASS (TBD), or: not found]" — identifies the distinction but action template still uses fill-in-the-blank framing; no explicit output prohibition |
| C-11 Auto-PASS in preamble | PASS | PHASE 1 Criterion Roster with "Auto-PASS status" column for all 12 criteria + "Justification for any criterion already resolved (e.g., C-07): [one phrase per resolved item]" — preamble gate before any output file |
| C-12 Formula at preamble | PASS | "### Composite Formula (v2 N values)" in PHASE 1 with N_essential=4, N_recommended=3, N_aspirational=5; "Do not open any output file before Phase 1 is complete" |

```
Essential:    1+1+1+1 = 4.0 / 4 * 60 = 60.0
Recommended:  1+1+1 = 3.0 / 3 * 30 = 30.0
Aspirational: 1+1+0.5+1+1 = 4.5 / 5 * 10 = 9.0
Composite = 60.0 + 30.0 + 9.0 = 99.0/100
Golden: YES — all 4 essentials PASS and 99.0 >= 80
```

---

### OUTPUT: V-05 — Full Synthesis

| Criterion | Verdict | Evidence Quote |
|-----------|---------|----------------|
| C-01 Verdicts present | PASS | "Step A — Evidence extraction (complete ALL 12 rows before filling Step B)" + "Step B — Verdicts" — both steps pre-print all 12 rows; maximum structural redundancy |
| C-02 Evidence quotes | PASS | "Do not write any verdict before its evidence quote in Step A is written" — most explicit two-step sequencing constraint of any variation |
| C-03 Composite score | PASS | "composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 5 * 10) / N_aspirational = 5" in PHASE 1 + per-output arithmetic with correct 5-term aspirational sum |
| C-04 Leaderboard | PASS | "### Leaderboard / Rank \| Output \| Score \| Golden" in PHASE 3; ties resolved alphabetically |
| C-05 Failure patterns | PASS | "[If no universal failures: 'No universal failures — C-05 auto-PASS.']" — TBD in Phase 1 roster, resolved at Phase 3 |
| C-06 Excellence signals | PASS | "### Excellence Signals / [Any output-criterion pair where one output outperforms the group by >= one tier:] / What it did differently: [one sentence on the mechanism.]" — stronger than all other variations |
| C-07 Regression signals | PASS | "Prior-round scorecard: [provided / not provided] [Provided: list every output-criterion pair that regressed (PASS -> FAIL or PARTIAL).]" |
| C-08 Actionable diagnosis | PASS | "Action: [fully instantiated: verb + artifact name + exact section — do NOT write a placeholder like 'Action: [verb + artifact]'. Example: 'Rewrite the criterion roster in quest-score.md PHASE 1 PREAMBLE to add C-10/C-11/C-12 rows…']" |
| C-09 Score distribution | PASS | "Note if the expanded N_aspirational=5 denominator affected ceiling scores relative to R1" — adds R2-specific calibration guidance absent from all other variations |
| C-10 Worked example | PASS | "do NOT write a placeholder like 'Action: [verb + artifact]'" — explicit output prohibition closes the gap that all V-01/V-02/V-03/V-04 left open with examples-only guidance |
| C-11 Auto-PASS in preamble | PASS | PHASE 1 Criterion Roster with "Auto-PASS status for this run" column for all 12 criteria + "Justification for any criterion already resolved (e.g., C-07): [one phrase per resolved item]"; gate instruction before Phase 2 |
| C-12 Formula at preamble | PASS | "### Composite Formula (v2 — print with correct N values)" in PHASE 1 with N_essential=4, N_recommended=3, N_aspirational=5; "Do not open any output file before Phase 1 is complete" |

```
Essential:    1+1+1+1 = 4.0 / 4 * 60 = 60.0
Recommended:  1+1+1 = 3.0 / 3 * 30 = 30.0
Aspirational: 1+1+1+1+1 = 5.0 / 5 * 10 = 10.0
Composite = 60.0 + 30.0 + 10.0 = 100.0/100
Golden: YES — all 4 essentials PASS and 100.0 >= 80
```

---

## LEADERBOARD

Resolve TBD statuses before ranking:
- **C-05**: No criterion received FAIL or PARTIAL in every output → **auto-PASS**
- **C-08**: No universal failures exist → **auto-PASS**
- **C-10**: V-01/V-02/V-03/V-04 PARTIAL, V-05 PASS → **scoring required** (not auto-PASS; partial failures exist but not universal)

| Rank | Output | Score | Golden |
|------|--------|-------|--------|
| 1 | V-05 | 100.0 | yes |
| 2 | V-01 | 99.0 | yes |
| 3 | V-02 | 99.0 | yes |
| 4 | V-03 | 99.0 | yes |
| 5 | V-04 | 99.0 | yes |

_V-01/V-02/V-03/V-04 tied at 99.0; resolved alphabetically._

---

## FAILURE PATTERNS

Roster updates: C-05 = auto-PASS, C-08 = auto-PASS, C-10 = scoring required (PARTIAL for V-01 through V-04; PASS for V-05).

No criterion received FAIL or PARTIAL in **every** scored output. **No universal failures — C-05 auto-PASS.**

---

## EXCELLENCE SIGNALS

- **C-10 — Worked example in action line**: V-05 = PASS; group median = PARTIAL (V-01/V-02/V-03/V-04).
  V-05 added the explicit "do NOT write a placeholder like 'Action: [verb + artifact]'" prohibition alongside the worked example. This output mandate — not the worked example itself — is what achieves PASS; all other variations had worked examples but no prohibition, leaving the template framing as a legal output form.

- **C-06 — Excellence signals surfaced**: V-05 introduces "What it did differently: [one sentence on the mechanism.]" — a structured follow-up field absent from all other variations. Slight overperformance vs. group, which all PASS the minimum bar.

- **C-09 — Score distribution commentary**: V-05 adds "Note if the expanded N_aspirational=5 denominator affected ceiling scores relative to R1" — an R2-specific calibration probe not present in V-01/V-02/V-03/V-04. All PASS minimum but V-05 produces richer output.

---

## REGRESSION SIGNALS

Prior-round scorecard provided: quest-score-scorecard-R1-2026-03-14.md

Mapping R1 verdicts to R2 (criteria C-01 through C-09 existed in both rounds; C-10/C-11/C-12 are new):

| Output | Criterion | R1 Verdict | R2 Verdict | Change |
|--------|-----------|------------|------------|--------|
| V-02 | C-03 | PARTIAL | PASS | improvement |
| V-03 | C-01 | PARTIAL | PASS | improvement |
| V-03 | C-02 | PARTIAL | PASS | improvement |
| V-01 | C-08 | PARTIAL | PASS | improvement |
| V-02 | C-08 | PARTIAL | PASS | improvement |
| V-04 | C-08 | PARTIAL | PASS | improvement |

**No regressions detected.** All R1 weaknesses that were PARTIAL improved to PASS or remained stable. Zero PASS→FAIL or PASS→PARTIAL transitions across any output-criterion pair.

---

## SCORE DISTRIBUTION

Score range: 99.0 (V-01/V-02/V-03/V-04) to 100.0 (V-05), a spread of 1 point. The near-uniform cluster at 99 reflects that all five R2 variations directly absorbed the R1 new_patterns (C-10/C-11/C-12) as first-class structural sections, collapsing R1's 15-point spread (85–100) to a tight 1-point spread. The sole discriminator is C-10's output mandate: a 1-point gap from the aspirational tier is a real but narrow difference, suggesting the R2 rubric's expansion to N_aspirational=5 successfully isolated the remaining design variable — worked example prohibition — while confirming all other structural mechanisms were effectively solved by R1's learnings.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["explicit 'do NOT write a placeholder' prohibition in the action template is required for C-10 PASS — worked examples alone are insufficient because they still permit template-framing output; the mandate must target the output format, not just model it", "R2 rubric expansion (N_aspirational 2→5, new C-10/C-11/C-12) collapsed R1 spread (85–100) to 1-point cluster (99–100) — all five variations absorbed the new criteria as first-class preamble structures, confirming that R1 new_patterns translated directly into effective structural guidance"]}
```
