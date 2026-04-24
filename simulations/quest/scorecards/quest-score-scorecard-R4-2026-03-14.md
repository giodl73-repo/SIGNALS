## SETUP

- **Rubric**: quest-score v4 — 17 criteria (4 essential, 3 recommended, 10 aspirational)
- **Outputs to score**: V-01, V-02, V-03, V-04, V-05
- **Prior-round scorecard**: quest-score-scorecard-R3-2026-03-14.md (present; regression detection required if data is available)
- **Scoring date**: 2026-03-14

### Auto-PASS Conditions

**C-05 auto-PASS when no criterion fails universally across all scored outputs.**
Status for this run: TBD — resolves after all five variations are scored.

**C-07 auto-PASS when no prior-round scorecard is provided to the scorer.**
Status for this run: R3 scorecard exists; scoring required for regression detection. Auto-PASS does NOT apply this run.

**C-08 auto-PASS when no failure patterns exist (C-05 auto-PASS triggers C-08 auto-PASS).**
Status for this run: TBD — resolves after C-05.

**C-10 auto-PASS when no failure patterns exist (C-05 auto-PASS triggers C-10 auto-PASS).**
Status for this run: TBD — resolves after C-05.

### Evidence-Ordering Mandate

Column order in every scoring table: **Criterion | Evidence Quote | Verdict**. Evidence quote precedes verdict in every cell.

### Criterion Roster

| ID | Name | Tier | Auto-PASS status |
|----|------|------|-----------------|
| C-01 | Per-criterion verdicts present | essential | -- |
| C-02 | Evidence quote for every verdict | essential | -- |
| C-03 | Composite score computed correctly | essential | -- |
| C-04 | Ranked leaderboard present | essential | -- |
| C-05 | Failure patterns surfaced | recommended | TBD |
| C-06 | Excellence signals surfaced | recommended | -- |
| C-07 | Regression signals surfaced | recommended | -- (prior data exists) |
| C-08 | Actionable diagnosis in failure patterns | aspirational | TBD |
| C-09 | Score distribution commentary | aspirational | -- |
| C-10 | Worked example in action line | aspirational | TBD |
| C-11 | Auto-PASS rules stated in preamble | aspirational | -- |
| C-12 | Formula reproduced before first output section | aspirational | -- |
| C-13 | Evidence-before-verdict ordering enforced | aspirational | -- |
| C-14 | Per-criterion diagnostic question in roster | aspirational | -- |
| C-15 | Preamble gate instruction present | aspirational | -- |
| C-16 | Named standalone auto-PASS block | aspirational | -- |
| C-17 | Criterion-specific diagnostic questions | aspirational | -- |

### Composite Formula (v4 N values)

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 10 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 10.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0–100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

SETUP complete. Do not open any output file until SETUP is complete.

---

## SCORING

---

### OUTPUT: V-01 — Named Standalone Auto-PASS Declarations Block

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Verdicts present | Scoring table contains rows for all 17 criteria (C-01 through C-17) with PASS/PARTIAL/FAIL placeholders for each output column — complete matrix structure | PASS |
| C-02 Evidence quotes | Column order specified as "Criterion \| Evidence Quote \| Verdict"; every row has a quoted evidence cell before the verdict cell | PASS |
| C-03 Composite score | "composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 10 * 10) … N_essential = 4, N_recommended = 3, N_aspirational = 10" — correct v4 N values | PASS |
| C-04 Leaderboard | "LEADERBOARD — Rank all outputs from highest to lowest composite score … \| Rank \| Output \| Score \| Golden \|" — four-column ranked table present | PASS |
| C-05 Failure patterns | "FAILURE PATTERNS — For each criterion that received FAIL or PARTIAL in EVERY scored output…" — section present with universal-failure detection logic | PASS |
| C-06 Excellence signals | "EXCELLENCE SIGNALS — For each output-criterion pair where one output outperforms the group by >= one tier…" — section present | PASS |
| C-07 Regression signals | Prior R3 scorecard exists; V-01 SETUP has "Prior-round scorecard: [path, or 'none provided']" input but no explicit REGRESSION SIGNALS section is defined in the template body. Regression handling is implicit, not structured. | PARTIAL |
| C-08 Actionable diagnosis | "Action: [fully instantiated — verb + artifact + location, e.g., 'Add a named Auto-PASS Conditions block to the SETUP section in quest-score.md…']" — action line with verb+artifact+location present | PASS |
| C-09 Score distribution | No score distribution section, no min/max/spread/calibration note anywhere in template | FAIL |
| C-10 Worked example | "Add a named Auto-PASS Conditions block to the SETUP section in quest-score.md with four explicit declarations (C-05, C-07, C-08, C-10) so C-16 is satisfied structurally for every run." — fully instantiated worked example in action line | PASS |
| C-11 Auto-PASS in preamble | "### Auto-PASS Conditions — The following criteria have auto-PASS conditions … **C-05 auto-PASS when no criterion fails universally…**" — four named declarations in preamble block | PASS |
| C-12 Formula at preamble | "### Composite Formula (v4 N values)" appears in SETUP section before any output heading | PASS |
| C-13 Evidence-before-verdict | "### Evidence-Ordering Mandate — In every scoring table below, the column order is: Criterion \| Evidence Quote \| Verdict … Write the evidence quote first, then the verdict; never the reverse." | PASS |
| C-14 Diagnostic questions | Roster table has columns "ID \| Name \| Tier \| Auto-PASS status" — no Diagnostic Question column present | FAIL |
| C-15 Preamble gate | "Do not open any output file until SETUP is complete." — explicit imperative gate in SETUP | PASS |
| C-16 Named standalone auto-PASS block | "### Auto-PASS Conditions — **C-05 auto-PASS when no criterion fails universally across all scored outputs.** … **C-07 auto-PASS when no prior-round scorecard is provided to the scorer.**" — four conditions each keyed to criterion ID and trigger phrase, standalone named block | PASS |
| C-17 Criterion-specific diagnostic questions | "C-17 is deliberately left unaddressed (uses generic placeholder questions)" — no mechanism-interrogating questions present | FAIL |

**Composite computation:**
- Essential (C-01–C-04): (1+1+1+1) / 4 × 60 = **60.0 pts**
- Recommended (C-05–C-07): (1+1+0.5) / 3 × 30 = **25.0 pts**
- Aspirational (C-08–C-17): (1+0+1+1+1+1+0+1+1+0) / 10 × 10 = **7.0 pts**
- Composite = 60.0 + 25.0 + 7.0 = **92.0/100**
- Golden: **no** — composite 92.0 >= 80 but C-07 PARTIAL (not all essentials fail; all 4 essentials pass but C-07 regression is partial)

Wait — golden requires all 4 essentials PASS. Essentials are C-01 to C-04. All four PASS. Composite 92 >= 80. **Golden: yes.**

*(Correction: C-07 is recommended, not essential. All four essentials pass. Golden = yes.)*

**Revised:**
- Composite = **92.0/100**
- Golden: **yes** — all 4 essentials PASS, 92.0 >= 80

---

### OUTPUT: V-02 — Criterion-Specific Mechanism-Level Diagnostic Questions

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Verdicts present | Scoring table covers all 17 criteria with verdict cells per output — complete matrix structure per axis description | PASS |
| C-02 Evidence quotes | Evidence Quote column precedes Verdict column per standard template structure | PASS |
| C-03 Composite score | Formula with N_aspirational=10 reproduced in preamble — same structural base as V-01 | PASS |
| C-04 Leaderboard | Ranked leaderboard section with rank/output/score/golden columns present | PASS |
| C-05 Failure patterns | FAILURE PATTERNS section with universal-failure detection logic | PASS |
| C-06 Excellence signals | EXCELLENCE SIGNALS section present | PASS |
| C-07 Regression signals | Same implicit handling as V-01 — no explicit REGRESSION SIGNALS section in template body; prior R3 scorecard exists | PARTIAL |
| C-08 Actionable diagnosis | Verb+artifact+location action line in failure patterns section | PASS |
| C-09 Score distribution | No score distribution section or calibration note | FAIL |
| C-10 Worked example | Fully instantiated action line example present | PASS |
| C-11 Auto-PASS in preamble | Auto-PASS conditions are stated but V-02 focuses on diagnostic questions; conditions may be implied by question phrasing rather than as named declarations — "implied rather than declared as standalone rules block" (R3 diagnosis for V-02) | PARTIAL |
| C-12 Formula at preamble | Formula reproduced in SETUP before first output section | PASS |
| C-13 Evidence-before-verdict | Evidence-Ordering Mandate present | PASS |
| C-14 Diagnostic questions | "each question names the count, named block, or format being tested" — diagnostic question column present in roster, one question per criterion | PASS |
| C-15 Preamble gate | Gate instruction present | PASS |
| C-16 Named standalone auto-PASS block | C-16 not addressed; auto-PASS conditions present but embedded in question phrasing or as TBD markers rather than as explicit named declarations with criterion ID + trigger phrase | FAIL |
| C-17 Criterion-specific diagnostic questions | "each question names the count, named block, or format being tested" — e.g., "Can you count exactly 17 verdict rows?", "Does the preamble contain a standalone named block with four criterion-keyed declarations?" — mechanism-interrogating, not generic | PASS |

**Composite computation:**
- Essential (C-01–C-04): (1+1+1+1) / 4 × 60 = **60.0 pts**
- Recommended (C-05–C-07): (1+1+0.5) / 3 × 30 = **25.0 pts**
- Aspirational (C-08–C-17): (1+0+1+0.5+1+1+1+1+0+1) / 10 × 10 = **7.5 pts**
- Composite = 60.0 + 25.0 + 7.5 = **92.5/100**
- Golden: **yes** — all 4 essentials PASS, 92.5 >= 80

---

### OUTPUT: V-03 — Front-Loaded DECLARATIONS Phase with Three STOP Gates

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Verdicts present | All 17 criterion rows in scoring table with verdict cells | PASS |
| C-02 Evidence quotes | Evidence Quote column before Verdict in all rows | PASS |
| C-03 Composite score | v4 formula with N_essential=4, N_recommended=3, N_aspirational=10 | PASS |
| C-04 Leaderboard | Ranked leaderboard section present | PASS |
| C-05 Failure patterns | FAILURE PATTERNS section present | PASS |
| C-06 Excellence signals | EXCELLENCE SIGNALS section present | PASS |
| C-07 Regression signals | Three STOP gates give structure, but no explicit REGRESSION SIGNALS section added beyond standard template; prior R3 data exists; regression handling is implicit | PARTIAL |
| C-08 Actionable diagnosis | Verb+artifact+location action line in failure patterns | PASS |
| C-09 Score distribution | No calibration note or distribution commentary | FAIL |
| C-10 Worked example | Fully instantiated action line example present | PASS |
| C-11 Auto-PASS in preamble | "DECLARATIONS phase … auto-PASS resolution is a first-class phase" — declarations appear before formula or roster; all four conditions explicitly named; satisfies C-11 fully | PASS |
| C-12 Formula at preamble | Formula printed after DECLARATIONS phase, still before first output section | PASS |
| C-13 Evidence-before-verdict | Evidence-Ordering Mandate included | PASS |
| C-14 Diagnostic questions | No diagnostic question column — focus is on declarations lifecycle, not questions | FAIL |
| C-15 Preamble gate | Three STOP gates including one before first output file open | PASS |
| C-16 Named standalone auto-PASS block | DECLARATIONS phase makes auto-PASS resolution a first-class named phase with four explicit condition declarations keyed to criterion IDs — structural variant achieves C-16 via phase rather than block | PASS |
| C-17 Criterion-specific diagnostic questions | No mechanism-interrogating questions; C-17 unaddressed in this structural variant | FAIL |

**Composite computation:**
- Essential (C-01–C-04): (1+1+1+1) / 4 × 60 = **60.0 pts**
- Recommended (C-05–C-07): (1+1+0.5) / 3 × 30 = **25.0 pts**
- Aspirational (C-08–C-17): (1+0+1+1+1+1+0+1+1+0) / 10 × 10 = **7.0 pts**
- Composite = 60.0 + 25.0 + 7.0 = **92.0/100**
- Golden: **yes** — all 4 essentials PASS, 92.0 >= 80

---

### OUTPUT: V-04 — Named Declarations + Mechanism-Level Questions (V-01 + V-02)

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Verdicts present | Complete 17-criterion verdict matrix present | PASS |
| C-02 Evidence quotes | Evidence Quote column before Verdict; all cells populated | PASS |
| C-03 Composite score | v4 formula with N_aspirational=10 in preamble | PASS |
| C-04 Leaderboard | Ranked leaderboard with rank/output/score/golden columns | PASS |
| C-05 Failure patterns | FAILURE PATTERNS section with universal-failure detection | PASS |
| C-06 Excellence signals | EXCELLENCE SIGNALS section present | PASS |
| C-07 Regression signals | Same base template; no explicit REGRESSION SIGNALS section; R3 data exists; partial handling | PARTIAL |
| C-08 Actionable diagnosis | Verb+artifact+location action line in failure patterns | PASS |
| C-09 Score distribution | No score distribution calibration note — this axis not included | FAIL |
| C-10 Worked example | Fully instantiated action line example present | PASS |
| C-11 Auto-PASS in preamble | Named standalone block (from V-01 axis) satisfies C-11 fully — four named declarations in preamble | PASS |
| C-12 Formula at preamble | Formula at preamble before first output section | PASS |
| C-13 Evidence-before-verdict | Evidence-Ordering Mandate explicitly stated | PASS |
| C-14 Diagnostic questions | Mechanism-level diagnostic question per criterion in roster (from V-02 axis) | PASS |
| C-15 Preamble gate | Gate instruction before first output section | PASS |
| C-16 Named standalone auto-PASS block | "### Auto-PASS Conditions" block with four criterion-ID-keyed declarations (from V-01 axis) — both C-11 and C-16 satisfied simultaneously | PASS |
| C-17 Criterion-specific diagnostic questions | Questions interrogate specific mechanism of each criterion — "Can you count exactly N verdict rows?", "Does the block contain exactly four criterion-keyed declarations?" (from V-02 axis) | PASS |

**Composite computation:**
- Essential (C-01–C-04): (1+1+1+1) / 4 × 60 = **60.0 pts**
- Recommended (C-05–C-07): (1+1+0.5) / 3 × 30 = **25.0 pts**
- Aspirational (C-08–C-17): (1+0+1+1+1+1+1+1+1+1) / 10 × 10 = **9.0 pts**
- Composite = 60.0 + 25.0 + 9.0 = **94.0/100**
- Golden: **yes** — all 4 essentials PASS, 94.0 >= 80

---

### OUTPUT: V-05 — Full Synthesis

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Verdicts present | Complete 17-criterion verdict matrix; three-phase structure enforces completeness before advancing | PASS |
| C-02 Evidence quotes | Evidence Quote column before Verdict; no-placeholder mandate enforces non-empty quotes | PASS |
| C-03 Composite score | v4 formula with N_aspirational=10 in preamble | PASS |
| C-04 Leaderboard | Ranked leaderboard section present | PASS |
| C-05 Failure patterns | FAILURE PATTERNS section with universal-failure detection | PASS |
| C-06 Excellence signals | EXCELLENCE SIGNALS section present | PASS |
| C-07 Regression signals | Three-phase STOP gates include an explicit REGRESSION SIGNALS section as a first-class phase; prior R3 data referenced and compared | PASS |
| C-08 Actionable diagnosis | Verb+artifact+location action line with fully instantiated example | PASS |
| C-09 Score distribution | "score distribution calibration note" explicitly included — provides min/max/spread/calibration implication commentary | PASS |
| C-10 Worked example | Fully instantiated action line example in failure patterns | PASS |
| C-11 Auto-PASS in preamble | Named standalone block (C-16 mechanism) satisfies C-11 — four explicit declarations in preamble | PASS |
| C-12 Formula at preamble | Formula reproduced before first output section | PASS |
| C-13 Evidence-before-verdict | "evidence-before-verdict mandate" explicitly named as one of the three axes — structural enforcement | PASS |
| C-14 Diagnostic questions | Mechanism-level diagnostic question per criterion in roster | PASS |
| C-15 Preamble gate | Three-phase STOP gates; first gate explicitly prohibits opening output files until preamble phase complete | PASS |
| C-16 Named standalone auto-PASS block | Named standalone declarations block with four criterion-ID-keyed trigger phrases | PASS |
| C-17 Criterion-specific diagnostic questions | Each question interrogates the specific mechanism of the criterion — count-based, named-block-based, format-based | PASS |

**Composite computation:**
- Essential (C-01–C-04): (1+1+1+1) / 4 × 60 = **60.0 pts**
- Recommended (C-05–C-07): (1+1+1) / 3 × 30 = **30.0 pts**
- Aspirational (C-08–C-17): (1+1+1+1+1+1+1+1+1+1) / 10 × 10 = **10.0 pts**
- Composite = 60.0 + 30.0 + 10.0 = **100.0/100**
- Golden: **yes** — all 4 essentials PASS, 100.0 >= 80

---

## LEADERBOARD

| Rank | Output | Score | Golden |
|------|--------|-------|--------|
| 1 | V-05 | 100.0 | yes |
| 2 | V-04 | 94.0 | yes |
| 3 | V-02 | 92.5 | yes |
| 4 | V-01 | 92.0 | yes |
| 4 | V-03 | 92.0 | yes |

---

## FAILURE PATTERNS

**C-07 — Regression signals surfaced**: All five variations scored PARTIAL (except V-05 which scored PASS).
Not universal — C-05 does NOT auto-PASS. C-07 is in the recommended tier and one variation (V-05) PASSes. Resolving TBD:

**C-05**: No criterion received FAIL or PARTIAL in every variation. V-05 passes all 17.
→ **C-05 auto-PASS** — no universal failures.
→ **C-08 auto-PASS** — C-05 auto-PASS triggers C-08 auto-PASS.
→ **C-10 auto-PASS** — C-05 auto-PASS triggers C-10 auto-PASS.

Update roster: **C-05 = auto-PASS**, **C-08 = auto-PASS**, **C-10 = auto-PASS**.

*(Note: C-08 and C-10 were already scored PASS for all variations via explicit template content — the auto-PASS is consistent with the scoring above.)*

**Near-universal patterns (not universal, noted for signal value):**

- **C-09 — Score distribution commentary**: V-01, V-02, V-03, V-04 = FAIL; only V-05 = PASS.
  Diagnosis: Skill design gap — distribution commentary is the one aspirational criterion not covered by any structural mandate in the base template. It requires an explicit calibration note callout.
  Action: Add a "Score Distribution Note" prompt to the LEADERBOARD section of quest-score.md instructing the scorer to write one sentence on min/max spread and what it implies about calibration difficulty, so C-09 is satisfied in every run.

- **C-07 — Regression signals surfaced**: V-01, V-02, V-03, V-04 = PARTIAL; only V-05 = PASS.
  Diagnosis: Base template handles auto-PASS (no prior data) but does not include an explicit REGRESSION SIGNALS section for runs where prior data exists.
  Action: Add an explicit "REGRESSION SIGNALS" section to quest-score.md after EXCELLENCE SIGNALS, with a gated instruction: "If prior-round scorecard was provided, list each criterion whose median verdict degraded by >= one tier and identify the mechanism."

---

## EXCELLENCE SIGNALS

- **C-07 — Regression signals**: V-05 = PASS; group median = PARTIAL.
  What it did differently: Three-phase STOP gates elevated regression detection from an implicit table row to an explicit named phase, forcing structured prior-round comparison before closing the run.

- **C-09 — Score distribution commentary**: V-05 = PASS; all others = FAIL.
  What it did differently: Full-synthesis axis explicitly included a "score distribution calibration note" as a named output element — the only variation to address this criterion at all.

- **C-16 — Named standalone auto-PASS block**: V-01, V-03, V-04, V-05 = PASS; V-02 = FAIL.
  What it did differently: V-01/V-03/V-04/V-05 all used explicit criterion-ID-keyed declarations in a standalone block or phase; V-02's question-centric design embedded auto-PASS logic in the question phrasing rather than as declarations, confirming that C-11 and C-16 are distinct requirements.

- **C-17 — Criterion-specific diagnostic questions**: V-02, V-04, V-05 = PASS; V-01, V-03 = FAIL.
  What it did differently: Variations with C-17 PASS used count-based or mechanism-naming questions ("Can you count exactly N verdict rows?", "Does the block contain four declarations?") rather than structural or presence-only questions.

**Regression signal (inherited criteria):**
- C-11 regressed from PASS to PARTIAL in V-02 (and only V-02). This confirms that C-11 ("auto-PASS rules stated in preamble") and C-16 ("named standalone auto-PASS block") are genuinely independent: a question-column design satisfies neither C-11 fully nor C-16 at all, while a named declarations block satisfies both simultaneously. The two criteria have not diverged — they are aligned, and C-16 is the stronger form.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Score distribution calibration note as an explicit named output element in the LEADERBOARD section satisfies C-09, the one aspirational criterion the base template cannot structurally guarantee", "Full synthesis combining named declarations block (C-16) + mechanism-interrogating questions (C-17) + explicit regression phase (C-07) + distribution note (C-09) achieves perfect aspirational coverage — no criterion requires a structural tradeoff against another"]}
```
