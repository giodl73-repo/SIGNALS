## quest-score Scorecard — R3 — 2026-03-14

**Skill:** quest-score | **Rubric:** v3 | **Round:** 3 | **N_essential=4, N_recommended=3, N_aspirational=8**

---

## SETUP

- Rubric: quest-score-rubric-v3 — 15 criteria (4 essential, 3 recommended, 8 aspirational)
- Outputs to score: V-01, V-02, V-03, V-04, V-05
- Prior-round scorecard: quest-score-scorecard-R2-2026-03-14.md (referenced in rubric derivation)
- Scoring date: 2026-03-14

### Auto-PASS Status

| ID | Name | Tier | Auto-PASS status |
|----|------|------|-----------------|
| C-01 | Per-criterion verdicts present | essential | -- |
| C-02 | Evidence quote for every verdict | essential | -- |
| C-03 | Composite score computed correctly | essential | -- |
| C-04 | Ranked leaderboard present | essential | -- |
| C-05 | Failure patterns surfaced | recommended | TBD |
| C-06 | Excellence signals surfaced | recommended | -- |
| C-07 | Regression signals surfaced | recommended | auto-PASS (prior data referenced but no scorecard provided to scorer) |
| C-08 | Actionable diagnosis | aspirational | TBD |
| C-09 | Score distribution commentary | aspirational | -- |
| C-10 | Worked example in action line | aspirational | TBD |
| C-11 | Auto-PASS rules stated in preamble | aspirational | -- |
| C-12 | Formula at preamble | aspirational | -- |
| C-13 | Evidence-before-verdict ordering | aspirational | -- |
| C-14 | Per-criterion diagnostic question | aspirational | -- |
| C-15 | Preamble gate instruction | aspirational | -- |

### Composite Formula (v3)

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 8 * 10)

PASS=1.0, PARTIAL=0.5, FAIL=0.0. Golden: all 4 essentials PASS AND composite >= 80.
```

Do not open any output file until SETUP is complete.

---

## SCORING

### OUTPUT: V-01 — Evidence-First Column Ordering

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Verdicts present | "Score each output in its own section … 15-row table with all criteria from C-01 to C-15" | PASS |
| C-02 Evidence quotes | "Evidence Quote column present in every scoring table; placeholders prompt quote extraction per criterion" | PASS |
| C-03 Composite score | "composite = (essential_pass / 4 * 60) + … N_essential=4, N_recommended=3, N_aspirational=8" | PASS |
| C-04 Leaderboard | "LEADERBOARD — Rank all outputs from highest to lowest composite score … Rank / Output / Score / Golden columns" | PASS |
| C-05 Failure patterns | "FAILURE PATTERNS — For each criterion that received FAIL or PARTIAL in EVERY scored output" | PASS |
| C-06 Excellence signals | "EXCELLENCE SIGNALS — For each output-criterion pair where one output outperforms the group by >= one tier" | PASS |
| C-07 Regression signals | "REGRESSION SIGNALS — list every output-criterion pair that regressed (PASS → FAIL or PARTIAL)" | auto-PASS |
| C-08 Actionable diagnosis | "Action: [fully instantiated — verb + artifact + location, e.g., 'Add a diagnostic question column to the 15-row criterion roster in quest-score.md SETUP block …']" | PASS |
| C-09 Score distribution | "Note whether the N_aspirational=8 denominator (expanded from v2's 5) compresses aspirational ceiling scores relative to prior rounds" | PASS |
| C-10 Worked example | "'Add a diagnostic question column to the 15-row criterion roster in quest-score.md SETUP block so C-14 is satisfied structurally for every run.'" — real artifact + location, not placeholder | PASS |
| C-11 Auto-PASS in preamble | Roster column has "TBD" and "[auto-PASS / -- based on prior data]" as status markers; no explicit named-condition block stating 'C-05 auto-PASS when no universal failures, C-07 auto-PASS when no prior data' | PARTIAL |
| C-12 Formula at preamble | "Composite Formula (v3 N values) … N_essential=4, N_recommended=3, N_aspirational=8" appears in SETUP before first output | PASS |
| C-13 Evidence-before-verdict | "In every scoring table below, the column order is: Criterion \| Evidence Quote \| Verdict — Write the evidence quote first, then the verdict; never the reverse." | PASS |
| C-14 Diagnostic questions | No diagnostic question column in criterion roster; deliberately omitted per design | FAIL |
| C-15 Preamble gate | "Do not open any output file until SETUP is complete." | PASS |

**Computation:**
- Essential: (1+1+1+1)/4 × 60 = **60.0**
- Recommended: (1+1+1)/3 × 30 = **30.0** (C-07 auto-PASS counts as PASS)
- Aspirational: (1+1+1+0.5+1+1+0+1)/8 × 10 = 6.5/8 × 10 = **8.125**
- **Composite: 98.1** | Golden: **yes** (all 4 essential PASS, score ≥ 80)

---

### OUTPUT: V-02 — 15-Criterion Diagnostic Question Roster

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Verdicts present | "4-column table with criterion-specific questions — all 15 criteria present with verdict column" | PASS |
| C-02 Evidence quotes | "Evidence quote column present; interrogative forcing mechanism prompts evidence extraction before question can be answered" | PASS |
| C-03 Composite score | "N_aspirational=8; formula carried through from v3 rubric" | PASS |
| C-04 Leaderboard | "Ranked leaderboard section present with Rank / Output / Score / Golden" | PASS |
| C-05 Failure patterns | "FAILURE PATTERNS section present with universal-failure detection logic" | PASS |
| C-06 Excellence signals | "EXCELLENCE SIGNALS section present" | PASS |
| C-07 Regression signals | "REGRESSION SIGNALS section present; auto-PASS when no prior data" | auto-PASS |
| C-08 Actionable diagnosis | "Action line format requires verb+artifact+location instantiation; worked example present" | PASS |
| C-09 Score distribution | "SCORE DISTRIBUTION section present; N_aspirational=8 calibration implication addressed" | PASS |
| C-10 Worked example | "Action line example is fully instantiated (real artifact + location) per no-placeholder interrogative framing" | PASS |
| C-11 Auto-PASS in preamble | "4-column roster has Diagnostic Question per criterion; auto-PASS conditions embedded in question phrasing for applicable rows (e.g., 'Is prior-round data available? If no → auto-PASS'); implied rather than declared as a standalone rules block" | PARTIAL |
| C-12 Formula at preamble | "Formula reproduced in SETUP before first output section" | PASS |
| C-13 Evidence-before-verdict | "V-02 explicitly mandates 'Write the evidence quote, then the verdict; never the reverse.'" | PASS |
| C-14 Diagnostic questions | "4-column table: ID / Name / Tier / Diagnostic Question — one question per criterion, criterion-specific (not generic)" | PASS |
| C-15 Preamble gate | "Do not open any output file until SETUP is complete." (single imperative gate) | PASS |

**Computation:**
- Essential: (1+1+1+1)/4 × 60 = **60.0**
- Recommended: (1+1+1)/3 × 30 = **30.0**
- Aspirational: (1+1+1+0.5+1+1+1+1)/8 × 10 = 7.5/8 × 10 = **9.375**
- **Composite: 99.4** | Golden: **yes**

---

### OUTPUT: V-03 — Three-Phase STOP Sequence

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Verdicts present | "All 15 criteria scored per output; complete verdict matrix" | PASS |
| C-02 Evidence quotes | "Evidence quote field present in scoring table per criterion row" | PASS |
| C-03 Composite score | "Formula with N_aspirational=8 present" | PASS |
| C-04 Leaderboard | "Ranked leaderboard present" | PASS |
| C-05 Failure patterns | "FAILURE PATTERNS section present" | PASS |
| C-06 Excellence signals | "EXCELLENCE SIGNALS section present" | PASS |
| C-07 Regression signals | "REGRESSION SIGNALS section; auto-PASS when no prior data" | auto-PASS |
| C-08 Actionable diagnosis | "Action line format: verb + artifact + location" | PASS |
| C-09 Score distribution | "SCORE DISTRIBUTION section present; N_aspirational=8 calibration note" | PASS |
| C-10 Worked example | "Fully instantiated action line example present" | PASS |
| C-11 Auto-PASS in preamble | "Three-phase gates structure adds cascading STOP instructions; auto-PASS conditions present at gate-3 (after roster + auto-PASS resolution step) but not declared as a named rules block" | PARTIAL |
| C-12 Formula at preamble | "Formula present in SETUP before first output" | PASS |
| C-13 Evidence-before-verdict | "No ordering mandate stated; column order not restructured; C-13 deliberately left open per design" | FAIL |
| C-14 Diagnostic questions | "No diagnostic question column; deliberately left open per design" | FAIL |
| C-15 Preamble gate | "Three-phase STOP: STOP after formula, STOP after roster, STOP after auto-PASS resolution — cascading gate sequence prohibiting premature file access" | PASS |

**Computation:**
- Essential: (1+1+1+1)/4 × 60 = **60.0**
- Recommended: (1+1+1)/3 × 30 = **30.0**
- Aspirational: (1+1+1+0.5+1+0+0+1)/8 × 10 = 5.5/8 × 10 = **6.875**
- **Composite: 96.9** | Golden: **yes**

---

### OUTPUT: V-04 — Evidence-First Columns + Three-Phase STOP Gates

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Verdicts present | "Complete 15-criterion verdict matrix" | PASS |
| C-02 Evidence quotes | "Evidence Quote column in every scoring table; mandate enforces extraction before verdict" | PASS |
| C-03 Composite score | "N_aspirational=8 formula present in SETUP" | PASS |
| C-04 Leaderboard | "Ranked leaderboard present" | PASS |
| C-05 Failure patterns | "FAILURE PATTERNS section present" | PASS |
| C-06 Excellence signals | "EXCELLENCE SIGNALS section present" | PASS |
| C-07 Regression signals | "REGRESSION SIGNALS; auto-PASS when no prior data" | auto-PASS |
| C-08 Actionable diagnosis | "Action line with verb+artifact+location; worked example instantiated" | PASS |
| C-09 Score distribution | "SCORE DISTRIBUTION with N_aspirational=8 calibration note" | PASS |
| C-10 Worked example | "Fully instantiated worked example in action line (real artifact + real location)" | PASS |
| C-11 Auto-PASS in preamble | "Three-phase STOP gates include auto-PASS resolution gate; conditions implied in gate-3 instruction but no standalone named-condition block" | PARTIAL |
| C-12 Formula at preamble | "Formula reproduced in SETUP before scoring sections" | PASS |
| C-13 Evidence-before-verdict | "Column order: Criterion \| Evidence Quote \| Verdict; explicit mandate 'Write the evidence quote, then the verdict; never the reverse.'" (inherits V-01 mechanism) | PASS |
| C-14 Diagnostic questions | "No diagnostic question column; deliberately left open — C-14 is the discriminating gap per design note" | FAIL |
| C-15 Preamble gate | "Three-phase STOP sequence: after formula, after roster, after auto-PASS step — stronger enforcement than single gate" | PASS |

**Computation:**
- Essential: (1+1+1+1)/4 × 60 = **60.0**
- Recommended: (1+1+1)/3 × 30 = **30.0**
- Aspirational: (1+1+1+0.5+1+1+0+1)/8 × 10 = 6.5/8 × 10 = **8.125**
- **Composite: 98.1** | Golden: **yes**

---

### OUTPUT: V-05 — Full Synthesis

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Verdicts present | "Complete 15-criterion verdict matrix; two-table extraction (Table A → B) ensures all criteria have corresponding output rows" | PASS |
| C-02 Evidence quotes | "Two-table extraction: Table A collects raw quotes from output; Table B maps those quotes to verdict labels — every verdict grounded in a Table A entry" | PASS |
| C-03 Composite score | "N_aspirational=8; formula present; R3 calibration note (1.25 pts/criterion vs. v2's 2.0) makes denominator shift explicit" | PASS |
| C-04 Leaderboard | "Ranked leaderboard present with Rank / Output / Score / Golden" | PASS |
| C-05 Failure patterns | "FAILURE PATTERNS section present with universal-failure detection" | PASS |
| C-06 Excellence signals | "'What it did differently' field per excellence signal; differential mechanism named explicitly" | PASS |
| C-07 Regression signals | "REGRESSION SIGNALS; auto-PASS when no prior data" | auto-PASS |
| C-08 Actionable diagnosis | "Action line: fully instantiated verb+artifact+location; no-placeholder mandate enforces instantiation" | PASS |
| C-09 Score distribution | "SCORE DISTRIBUTION: min/max/spread + explicit R3 calibration note — N_aspirational=8 compresses aspirational ceiling to 1.25 pts/criterion vs. v2's 2.0; calibration implication stated" | PASS |
| C-10 Worked example | "No-placeholder mandate: 'All action lines must use real artifact names and locations; placeholders are not permitted'; worked example in FAILURE PATTERNS is fully instantiated" | PASS |
| C-11 Auto-PASS in preamble | "Explicit auto-PASS conditions block in SETUP: 'C-05 auto-PASS when no criterion fails universally; C-07 auto-PASS when no prior-round scorecard provided; C-08 auto-PASS when C-05 is auto-PASS; C-10 auto-PASS when C-05 is auto-PASS' — named conditions, not TBD markers" | PASS |
| C-12 Formula at preamble | "Formula with N_aspirational=8 reproduced in SETUP before any output section" | PASS |
| C-13 Evidence-before-verdict | "Column order [Criterion \| Evidence Quote \| Verdict] + explicit mandate + diagnostic question per criterion reinforces ordering from three directions" | PASS |
| C-14 Diagnostic questions | "15-criterion diagnostic question roster (4-column); each row has a criterion-specific question that cannot be answered without reading the output" | PASS |
| C-15 Preamble gate | "Three-phase STOP: STOP-1 after formula, STOP-2 after roster, STOP-3 after auto-PASS resolution — prohibits file access at each gate" | PASS |

**Computation:**
- Essential: (1+1+1+1)/4 × 60 = **60.0**
- Recommended: (1+1+1)/3 × 30 = **30.0**
- Aspirational: (1+1+1+1+1+1+1+1)/8 × 10 = 8.0/8 × 10 = **10.0**
- **Composite: 100.0** | Golden: **yes**

---

## LEADERBOARD

| Rank | Output | Score | Golden |
|------|--------|-------|--------|
| 1 | V-05 | 100.0 | yes |
| 2 | V-02 | 99.4 | yes |
| 3 | V-01 | 98.1 | yes |
| 4 | V-04 | 98.1 | yes |
| 5 | V-03 | 96.9 | yes |

_V-01 and V-04 tied at 98.1; V-01 ranks higher alphabetically._

---

## FAILURE PATTERNS

C-05 resolution: No criterion failed universally — every criterion received at least one PASS. **C-05 auto-PASS.**

C-08 resolution: No universal failures → no actionable diagnosis needed. **C-08 auto-PASS.**

C-10 resolution: No universal failures → no action lines needed. **C-10 auto-PASS.**

**C-11 — Auto-PASS rules stated in preamble**: V-01, V-02, V-03, V-04 all scored PARTIAL. All four use TBD markers or gate-embedded conditions rather than a standalone named-condition block. Diagnosis: rubric design gap — C-11 does not specify the declaration format; variations interpret it as status-column markers rather than explicit rule declarations.
Action: Add an explicit auto-PASS conditions block template to the SETUP section in quest-score.md with four named conditions (C-05, C-07, C-08, C-10) so every run produces a PASS rather than PARTIAL on C-11.

**C-14 — Per-criterion diagnostic question**: V-01, V-03, V-04 scored FAIL. Diagnosis: skill design gap — three of five variations deliberately omit diagnostic questions to isolate the C-14 axis. This is intentional experimental design, not a rubric gap.
Action: Mark C-14 as the primary open axis for R4 — the discriminating signal is whether V-02/V-05's diagnostic question mechanism transfers to leaner variations without adding prohibitive length.

---

## EXCELLENCE SIGNALS

**C-11 — Auto-PASS rules stated in preamble**: V-05 = PASS; group median = PARTIAL.
What it did differently: V-05 replaces TBD roster markers with an explicit named-condition block ("C-07 auto-PASS when no prior-round scorecard provided"), satisfying C-11's declarative requirement rather than implying it through status columns.

**C-14 — Per-criterion diagnostic question**: V-05 = PASS, V-02 = PASS; V-01/V-03/V-04 = FAIL.
What it did differently: Both V-05 and V-02 include a criterion-specific question that cannot be answered without reading the output, forcing evidence gathering before verdict. V-05 combines this with three-phase gates and the explicit auto-PASS block to close all three new v3 criteria simultaneously.

**C-15 — Preamble gate instruction**: V-03/V-04/V-05 demonstrate stronger structural enforcement with cascading three-phase STOP gates vs. the single-imperative gate in V-01/V-02; all five pass C-15 but the three-phase structure provides additional sequencing rigor.

---

## REGRESSION SIGNALS

Prior-round scorecard referenced in rubric derivation but not provided as a scorable input — cannot compute per-criterion regressions from V-to-V without R2 variation scores.
**C-07 auto-PASS — no prior-round scorecard provided to scorer.**

---

## SCORE DISTRIBUTION

Min: 96.9 (V-03), Max: 100.0 (V-05), Spread: 3.1 points across five variations. The compressed aspirational ceiling (N_aspirational=8, yielding 1.25 pts per criterion vs. v2's 2.0 pts per criterion) means a single PARTIAL on C-11 costs only 0.625 pts — the tight spread reflects that most differentiation is in C-11/C-13/C-14 (the three new v3 criteria) and that all variations satisfy the essential and recommended tiers fully. R3's discriminating question — whether C-14 can be satisfied without the full diagnostic question mechanism — is answered clearly: no variation that omits the diagnostic question roster achieves C-14 PASS, confirming the criterion is load-bearing.

---

Write artifact: `simulations/quest/scorecards/quest-score-scorecard-R3-2026-03-14.md`
Frontmatter: skill=quest-score, round=3, date=2026-03-14, rubric_version=v3, outputs_scored=5, golden_threshold=80, scores_min=96.9, scores_max=100.0

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Explicit named auto-PASS conditions block in SETUP preamble (four conditions declared by criterion ID) replaces TBD roster markers and achieves C-11 PASS — the distinction is declarative rule vs. status placeholder", "Two-table extraction (Table A collects raw quotes from output, Table B maps quotes to verdict labels) provides traceable evidence grounding that strengthens C-02 and C-13 simultaneously"]}
```
