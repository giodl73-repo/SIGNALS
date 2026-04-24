# quest-score Variations -- Round 7 (v7 rubric, targeting C-21/C-22)

**Skill**: quest-score
**Rubric**: v7-2026-03-16 (C-01--C-05 essential, C-06--C-08 recommended, C-09--C-22 aspirational)
**N_essential=5, N_recommended=3, N_aspirational=14**
**Date**: 2026-03-16
**Round**: 7

---

## Context: what informed this round

Round 6 found P+Q as the minimal sufficient combination for v6. V-04 (P+Q) and V-05 (N+O+P+Q)
tied at 99.58, confirming N+O were non-additive given P+Q. R6 synthesis named the reason:
"N's criterion-ID behavior is subsumed by Q's explicit-ID assignment plus COVERAGE ASSERTION;
O's structural sweep targets criteria at v5-baseline PASS."

v7 adds two new Aspirational criteria extracted from R6 excellence signals:

| Change | R6 (v6) | R7 (v7) | Design consequence |
|--------|---------|---------|-------------------|
| C-21 (Phase 1 exit criterion-coverage assertion) | Not in rubric | Q's 1e COVERAGE ASSERTION field becomes a scored criterion | Q-axis variations already satisfy C-21. Non-Q single-axis variations will score FAIL on C-21. |
| C-22 (Axis non-additivity identification) | Not in rubric | Scorecard must name at least one axis as redundant, name the criterion it targets, explain the subsuming mechanism | R6 synthesis notes contained this content by observation; v7 requires it structurally. |
| N_aspirational | 12 (C-09--C-20) | 14 (C-09--C-22) | Formula denominator: /12 -> /14 |

**What R7 variations must achieve beyond the R6 P+Q base:**

1. **C-21 PASS**: Already achieved by Q's 1e block. Non-Q single-axis variations expose
   C-21 FAIL as the baseline when the coverage assertion is absent.

2. **C-22 PASS**: The scoring output must, in synthesis or per-output notes, identify at
   least one axis as redundant given another, name the criterion it targets, and name the
   subsuming mechanism. Requires structural enforcement -- not just optional observation.

3. **N_aspirational update**: FORMULA CHANGE ALERT declares N_aspirational: 12 (v6) -> 14
   (v7). Any computation using /12 is a formula version error.

**Variation axes explored this round:**

| Code | Axis | Target criterion | Hypothesis |
|------|------|-----------------|-----------|
| R | NON-ADDITIVITY ANALYSIS BLOCK -- required section in SYNTHESIS with three-field schema: (a) redundant axis, (b) criterion it targets, (c) mechanism in the other axis that subsumes its function | C-22 | A schema-bound section with three required named fields forces the structural reasoning C-22 requires. Omitting any field is a visible structural gap. C-22 PASS predicted. |
| S | COMPOSITE INCREMENT TABLE -- Leaderboard gains a delta column showing composite increment per variation over the next-lower-ranked variation; zero-delta rows require a zero-increment note ("explain why this axis added no composite increment") | C-22 (numeric path) | The delta column surfaces non-additivity numerically. The "explain why" instruction requires a statement but does not mandate all three elements (axis/criterion/mechanism). C-22 PARTIAL predicted: delta present, structural explanation may be incomplete. |
| T | AXIS ARCHITECTURE AUDIT -- Phase 3 block producing a per-axis table: axis name, criterion targeted, composite increment when axis added; rows where increment = 0 are flagged with a required annotation | C-22 (systematic path) | The per-axis audit forces enumeration but the annotation instruction ("flag ZERO rows") may not produce the specific mechanism-subsuming statement required for PASS. C-22 PARTIAL predicted: per-axis verdicts present, subsuming-mechanism identification absent. |

Single-axis: V-01 (R), V-02 (S), V-03 (T).
Minimum combination: V-04 (P+Q+R -- R6 champion base plus the new C-22 axis).
Full integration test: V-05 (P+Q+R+S -- tests whether S is non-additive given R).

**Predicted outcomes (v7 rubric, N_aspirational=14):**

| Criterion | V-01 (R) | V-02 (S) | V-03 (T) | V-04 (P+Q+R) | V-05 (P+Q+R+S) |
|-----------|----------|----------|----------|-------------|----------------|
| C-01--C-08 | PASS | PASS | PASS | PASS | PASS |
| C-09 | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| C-10--C-18 | PASS | PASS | PASS | PASS | PASS |
| C-19 | PARTIAL | PARTIAL | PARTIAL | PASS | PASS |
| C-20 | FAIL | FAIL | FAIL | PASS | PASS |
| C-21 | FAIL | FAIL | FAIL | PASS | PASS |
| C-22 | PASS | PARTIAL | PARTIAL | PASS | PASS |

Note on V-01/C-22: R's three-field schema (redundant axis / criterion / subsuming mechanism)
makes all three required elements mandatory. Omitting any field is a visible structural gap.
C-22 PASS predicted.

Note on V-02/C-22: S's zero-increment note says "explain why" without mandating the three
elements. A scorer may write "scores tied -- no additional criteria passed," which demonstrates
non-additivity numerically but omits the structural subsuming-mechanism explanation. C-22
PARTIAL predicted.

Note on V-03/C-22: T's AXIS ARCHITECTURE AUDIT requires annotation for ZERO rows but
the annotation instruction is not specific enough to mandate the subsuming-mechanism field.
C-22 PARTIAL predicted -- per-axis verdicts present but mechanism identification absent.

Note on V-04/V-05 predicted tie: R's NON-ADDITIVITY ANALYSIS block already forces C-22
PASS; S's delta table corroborates numerically but cannot push C-22 above PASS. If the tie
holds, R7's non-additivity finding mirrors R6's: S is subsumed by R for C-22 purposes.

**Predicted composite scores:**

```
aspirational base: C-09 PARTIAL=0.5; others per table above

V-01 (R):   A: C09=0.5, C10-C18=9.0, C19=0.5, C20=0, C21=0, C22=1.0 -> 11.0/14
  composite = 60 + 30 + (11.0/14 * 10) = 97.86

V-02 (S):   A: C09=0.5, C10-C18=9.0, C19=0.5, C20=0, C21=0, C22=0.5 -> 10.5/14
  composite = 60 + 30 + (10.5/14 * 10) = 97.50

V-03 (T):   A: C09=0.5, C10-C18=9.0, C19=0.5, C20=0, C21=0, C22=0.5 -> 10.5/14
  composite = 60 + 30 + (10.5/14 * 10) = 97.50

V-04 (P+Q+R): A: C09=0.5, C10-C22=13.0 -> 13.5/14
  composite = 60 + 30 + (13.5/14 * 10) = 99.64

V-05 (P+Q+R+S): same as V-04 if S is non-additive given R
  composite = 60 + 30 + (13.5/14 * 10) = 99.64
```

Key diagnostics this round provides:
- V-01 > V-02 == V-03: Does R achieve C-22 PASS (schema-enforced) while S and T achieve
  only PARTIAL (narrative-based)?
- V-04 == V-05: Is S non-additive given R? Does the delta table add zero increment when the
  NON-ADDITIVITY ANALYSIS block is already present?
- V-01 vs V-04 spread: Does adding P+Q to R produce the expected ~1.79-point composite jump
  from three criteria (C-19, C-20, C-21) moving from FAIL/PARTIAL to PASS?

---

## V-01: Axis R -- Non-Additivity Analysis Block

**Variation axis**: Lifecycle emphasis / output format -- SYNTHESIS gains a required
NON-ADDITIVITY ANALYSIS section with a three-field schema (redundant axis, criterion it
targets, subsuming mechanism), making all three elements of C-22 PASS a mandatory,
labeled output.

**Hypothesis**: The most common C-22 failure mode is identifying tied scores without
explaining the structural reason. A schema-bound section with named fields makes omitting
any element a visible structural gap -- the same way a blank register cell makes a missing
prior-state value detectable without reading prose. C-22 PASS predicted. C-19 PARTIAL
(entry lock as structural imperative, no binary declaration). C-20, C-21 FAIL (no
criterion-ID anchoring, no COVERAGE ASSERTION).

---

You are running quest-score against the v7 rubric.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite score computed from
the rubric formula, and a golden-threshold determination. The final scorecard includes a
ranked leaderboard, excellence signals, failure patterns, regression signals, and
non-additivity analysis.

---

FORMULA CHANGE ALERT -- READ BEFORE ANY COMPUTATION

The v7 rubric changes the aspirational denominator from the v6 value.

  N_aspirational: 12 (v6) -> 14 (v7)

Composite formula (v7, active):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 14 * 10)

  PARTIAL counts as 0.5 toward pass count. FAIL counts as 0.
  Golden threshold: ALL 5 essentials PASS AND composite >= 80.

Do not compute any score using /12 or any prior denominator. If a conflict exists between
this prompt and a rubric file, the rubric file governs.

---

PHASE 1: LOAD, DELTA REGISTER, AND BILATERAL AUDIT

Before scoring any output, complete sections 1a through 1d in order. Do not proceed to
Phase 2 until all four sections are written and the bilateral audit shows no Symmetric: NO rows.

**1a. Load summary**

Produce a block confirming the rubric was read. The block must name all four elements:
  (a) all criteria IDs with tier labels (C-01--C-05 essential, C-06--C-08 recommended,
      C-09--C-22 aspirational)
  (b) the exact composite formula text (v7 active: /14 aspirational denominator)
  (c) the golden threshold condition (all 5 essentials PASS AND composite >= 80)
  (d) the count and list of outputs being scored

A load summary missing any one of (a)--(d) earns PARTIAL on C-01. Missing entirely earns FAIL.

After writing the load summary, write this required labeled field:

  Inertia (C-01): Without this load block, criteria count (22), formula denominator (/14),
  and threshold are unverified before any verdict is written. A scorer who skips produces a
  verdict matrix missing C-21 and C-22 rows and computes all composites using /12 -- both
  errors invisible until Phase 3.

**1b. Formula version delta**

Write in your scoring output:

  Formula version delta: N_aspirational changed from [prior value] to [current value] in v[N].

If the prior version cannot be determined:
  "No prior version delta detectable -- scoring under v7 as the baseline version."

After writing, write this required labeled field:

  Inertia (C-13, C-15): "N_aspirational=14" passes C-01 but fails C-15 -- the prior value
  (12) is absent. Both sides of every delta comparison are required to confirm the transition
  was registered, not just the endpoint loaded.

**1c. SYMMETRIC DELTA REGISTER**

Produce the following table. Fill every cell before proceeding to 1d.

  | Comparison type | Prior state | Current state |
  |-----------------|-------------|---------------|
  | N_aspirational (formula denominator) | [prior -- e.g., "12 (v6)"] | [current -- e.g., "14 (v7)"] |
  | Regression verdicts | [prior verdict or "No prior-round data -- row N/A"] | [current verdict or "--"] |
  | Arithmetic discrepancies | [stated score or "No discrepancy -- row N/A"] | [computed score or "--"] |

Rules:
  - A blank Prior State cell is a structural violation. Write the value or "N/A -- [reason]".
  - A blank Current State cell is also a structural violation.
  - The register must contain at least the N_aspirational row.

After writing, write this required labeled field:

  Inertia (C-15): Without the two-column table, a scorer writes "N_aspirational=14" correctly
  but never names the prior value (12). The column structure makes a one-sided entry a visible
  structural gap -- detectable by column scan without reading prose.

**1d. BILATERAL SYMMETRY AUDIT SWEEP (Phase 1 exit)**

After completing the register, produce this sweep before Phase 2 begins.

  | Comparison | Symmetric? |
  |------------|-----------|
  | N_aspirational | [YES -- Prior: [v], Current: [v] | NO -- [missing side] | PARTIAL -- N/A declared] |
  | Regression verdicts | [YES | NO -- [missing side] | PARTIAL -- no prior data] |
  | Arithmetic discrepancies | [YES | NO -- [missing side] | PARTIAL -- no discrepancy found] |

Verdict rules:
  - Symmetric: YES -- both Prior state and Current state present in register row.
  - Symmetric: NO -- one or both sides missing; remediate before Phase 2.
  - Symmetric: PARTIAL -- N/A rule invoked correctly. Not a failure.

After writing, write this required labeled field:

  Inertia (C-18): The SYMMETRIC DELTA REGISTER prevents asymmetric entries by requiring both
  columns. This audit sweep provides an independent catch -- a Symmetric: NO is visible by
  scanning the sweep without re-reading register prose. Prevention and catch are both required.

PHASE 1 COMPLETE. Proceed to Phase 2 only after 1a, 1b, 1c, and 1d are written.

---

PHASE 2: SCORE EACH OUTPUT

**MODEL CELL (Phase 2 entry -- write before any verdict row)**

Write a model evidence cell as the first action of Phase 2, before any criterion-output row.

  Evidence (model): "from [output ID], [section or structural element]: [verbatim quote or
  structural observation that locates a specific feature in the output -- not a criterion
  restatement]"
  Locatability test: could a reader find the referenced feature using only this evidence text?
  YES: proceed. NO: rewrite before entering any verdict row.

After writing the model cell, write this required labeled field:

  Inertia (C-11, C-14): Without a model cell at Phase 2 entry, evidence cells default to
  criterion restatement -- "the output has a leaderboard" cannot locate any specific feature.
  The model cell fires before the first verdict, establishing the evidence standard before any
  cell can set a lower norm.

ENTRY LOCK: do not write any verdict row until the model cell is written and passes the
locatability test. A verdict row written before the model cell is a Phase 2 protocol violation.

For each output, produce a scoring table:

  | ID | Criterion | Tier | Verdict | Evidence |

Column rules:
  - Verdict: PASS | PARTIAL | FAIL only.
  - Evidence: must quote, paraphrase with location, or name a specific structural feature.
    Criterion restatement is not evidence.
  - No row may be blank or missing. Include rows for all criteria C-01 through C-22.

After the scoring table, write the composite:

  essential_pass = [count; PARTIAL = 0.5]
  recommended_pass = [count; PARTIAL = 0.5]
  aspirational_pass = [count; PARTIAL = 0.5]
  composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 14 * 10) = [result]
  Golden: YES -- all essentials PASS; composite >= 80 | NO -- [which essential failed or composite < 80]

Score all N outputs before proceeding to Phase 3.

---

PHASE 3: VERIFY

**3a. Arithmetic verification**

Pick one output. Recompute its composite from the stated verdict counts and formula.

  Verification (output: [ID]):
    stated counts: E=[X]/5, R=[X]/3, A=[X]/14
    computed composite: ([X]/5 * 60) + ([X]/3 * 30) + ([X]/14 * 10) = [result]
    Matches stated score: YES | NO -- discrepancy: stated [X], computed [Y]

After writing, write this required labeled field:

  Inertia (C-12): "Verification performed" satisfies C-10 at PARTIAL but does not produce a
  binary result. The YES/NO field forces an explicit affirmation or names the exact discrepancy,
  making arithmetic errors visible even when the scorer is not looking for them.

The "Matches stated score:" field is required. Narrative equivalents do not satisfy C-12.

**3b. Regression section**

If a prior-round scorecard was provided:
  - "[Output ID] / [Criterion ID]: prior=[verdict], current=[verdict]"
  - Both verdicts required. Update SYMMETRIC DELTA REGISTER Regression row.

If no prior-round file was provided:
  "No prior round data -- regression analysis cannot be performed."

After writing, write this required labeled field:

  Inertia (C-09): Section required even when empty. An absent section is structurally
  indistinguishable from a section with no regressions.

---

SYNTHESIS

Write the following sections in order.

**LEADERBOARD**

  | Rank | Output | Composite | Golden? |

All N outputs ranked descending. Ties noted explicitly with tiebreak rule or
"tied -- no tiebreak applied." "See scores above" does not satisfy C-06.

**EXCELLENCE SIGNALS**

For each criterion where one output scores noticeably higher than others:
  Signal: [output ID] -- [criterion ID] -- [structural mechanism that produced the difference]

Generic rankings ("V-04 scored highest overall") are not excellence signals. The signal must
name the output-criterion pair and the mechanism. If no outlier pair: state explicitly.

**FAILURE PATTERNS**

  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

Required even when empty: "No failure patterns -- all criteria passed in at least one output."

**NON-ADDITIVITY ANALYSIS**

For each pair of variations where one variation uses a strict subset of the other's axes
(i.e., one variation's axis combination is fully contained in the other's), compute the
composite increment:
  Increment = variation_with_more_axes.composite - variation_with_fewer_axes.composite

For any pair where Increment = 0:

  Redundant axis: [name the axis that was added but produced zero composite increment]
  Criterion target: [name the criterion the redundant axis was designed to advance]
  Subsuming mechanism: [name the specific mechanism in the other axis that performs the same
    function -- identify what it does that makes the redundant axis's contribution zero]

All three fields are required for each zero-increment pair. A zero-increment declaration
without the subsuming mechanism satisfies C-22 at PARTIAL only.

If no zero-increment pair exists:
  "No non-additivity observed -- all axes produced positive composite increment."

If only one variation is scored:
  "Single variation scored -- non-additivity analysis not applicable."

Required: this section must appear whether or not non-additivity is observed. Omitting it
entirely earns C-22 FAIL even when per-output synthesis notes discuss tied scores.

**PER-OUTPUT SYNTHESIS NOTES**

One paragraph per output explaining structural score drivers. Explain the mechanism, not
the verdict counts.

---

## V-02: Axis S -- Composite Increment Table

**Variation axis**: Output format -- the LEADERBOARD gains a delta column showing each
variation's composite increment over the next-lower-ranked variation. For any row where
the delta is 0 and the higher-ranked variation has more axes than the lower, a required
zero-increment note explains why the additional axis contributed no composite increment.

**Hypothesis**: The delta column surfaces non-additivity numerically at a glance. The
zero-increment note instruction says "explain why" but does not mandate the three specific
elements (redundant axis / criterion / subsuming mechanism). A scorer writing "scores equal
-- no additional criteria passed" satisfies the note requirement without identifying the
mechanism subsuming the redundant axis's function. C-22 PARTIAL predicted: numerical
non-additivity visible, structural explanation present but potentially incomplete. C-19
PARTIAL (entry lock as imperative, no binary declaration). C-20, C-21 FAIL (no
criterion-ID anchoring, no COVERAGE ASSERTION).

---

You are running quest-score against the v7 rubric.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite score computed from
the rubric formula, and a golden-threshold determination. The final scorecard includes a
ranked leaderboard with composite increments, excellence signals, failure patterns, and
regression signals.

---

FORMULA CHANGE ALERT -- READ BEFORE ANY COMPUTATION

The v7 rubric changes the aspirational denominator from the v6 value.

  N_aspirational: 12 (v6) -> 14 (v7)

Composite formula (v7, active):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 14 * 10)

  PARTIAL counts as 0.5. FAIL counts as 0. Golden: ALL 5 essentials PASS AND composite >= 80.

Do not compute any score using /12 or any prior denominator.

---

PHASE 1: LOAD, DELTA REGISTER, AND BILATERAL AUDIT

Before scoring, complete sections 1a through 1d in order. Do not proceed to Phase 2 until
all four sections are written and the bilateral audit shows no Symmetric: NO rows.

**1a. Load summary**

  (a) all criteria IDs with tier labels (C-01--C-05 essential, C-06--C-08 recommended,
      C-09--C-22 aspirational)
  (b) exact composite formula text (v7 active: /14 aspirational denominator)
  (c) golden threshold: all 5 essentials PASS AND composite >= 80
  (d) count and list of outputs being scored

After writing, write this required labeled field:

  Inertia (C-01): Without the load block, criteria count (22), formula denominator (/14),
  and threshold are unverified. A scorer who skips produces a matrix missing C-21/C-22 rows
  and composites using /12 -- both invisible until Phase 3.

**1b. Formula version delta**

  Formula version delta: N_aspirational changed from [prior value] to [current value] in v[N].

If prior unknown: "No prior version delta detectable -- scoring under v7 as baseline."

After writing, write this required labeled field:

  Inertia (C-13, C-15): "N_aspirational=14" passes C-01 but fails C-15. Prior value (12)
  must be named. Both sides required to confirm the transition was registered.

**1c. SYMMETRIC DELTA REGISTER**

  | Comparison type | Prior state | Current state |
  |-----------------|-------------|---------------|
  | N_aspirational | [prior -- e.g., "12 (v6)"] | [current -- e.g., "14 (v7)"] |
  | Regression verdicts | [prior or "No prior-round data -- row N/A"] | [current or "--"] |
  | Arithmetic discrepancies | [stated or "No discrepancy -- row N/A"] | [computed or "--"] |

Blank Prior State = structural violation.

After writing, write this required labeled field:

  Inertia (C-15): Two-column structure makes prior-state omission a visible structural gap
  detectable by column scan without reading prose.

**1d. BILATERAL SYMMETRY AUDIT SWEEP (Phase 1 exit)**

  | Comparison | Symmetric? |
  |------------|-----------|
  | N_aspirational | [YES -- Prior: [v], Current: [v] | NO -- [missing] | PARTIAL -- N/A] |
  | Regression verdicts | [YES | NO | PARTIAL] |
  | Arithmetic discrepancies | [YES | NO | PARTIAL] |

Symmetric: NO requires remediation before Phase 2.

After writing, write this required labeled field:

  Inertia (C-18): Register prevents asymmetric entries. Sweep catches them independently.
  A Symmetric: NO is visible by scan without re-reading register prose.

PHASE 1 COMPLETE.

---

PHASE 2: SCORE EACH OUTPUT

**MODEL CELL (Phase 2 entry -- write before any verdict row)**

  Evidence (model): "from [output ID], [section or structural element]: [verbatim quote or
  structural observation that locates a specific feature -- not a criterion restatement]"
  Locatability test: YES -- proceed. NO -- rewrite.

After writing, write this required labeled field:

  Inertia (C-11, C-14): Without a model cell at Phase 2 entry, evidence cells default to
  criterion restatement. The model cell fires first, establishing the standard before any
  cell can set a lower norm.

ENTRY LOCK: no verdict row before the model cell passes the locatability test.

For each output, produce a scoring table:

  | ID | Criterion | Tier | Verdict | Evidence |

Include rows for all criteria C-01 through C-22. No row blank or missing.

After the table:
  essential_pass = [count; PARTIAL = 0.5]
  recommended_pass = [count; PARTIAL = 0.5]
  aspirational_pass = [count; PARTIAL = 0.5]
  composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 14 * 10) = [result]
  Golden: YES | NO -- [reason]

Score all N outputs before proceeding to Phase 3.

---

PHASE 3: VERIFY

**3a. Arithmetic verification**

  Verification (output: [ID]):
    stated counts: E=[X]/5, R=[X]/3, A=[X]/14
    computed composite: ([X]/5 * 60) + ([X]/3 * 30) + ([X]/14 * 10) = [result]
    Matches stated score: YES | NO -- discrepancy: stated [X], computed [Y]

After writing, write this required labeled field:

  Inertia (C-12): YES/NO binary field required. "Verification performed" satisfies C-10 at
  PARTIAL but does not produce a binary result and does not satisfy C-12.

**3b. Regression section**

  If prior data: "[Output ID] / [Criterion ID]: prior=[verdict], current=[verdict]"
  If no prior data: "No prior round data -- regression analysis cannot be performed."

After writing, write this required labeled field:

  Inertia (C-09): Section required even when empty. Absence is structurally indistinguishable
  from no regressions.

---

SYNTHESIS

Write the following sections in order.

**LEADERBOARD WITH COMPOSITE INCREMENT TABLE**

  | Rank | Output | Axes | Composite | Golden? | Delta from prior rank |
  |------|--------|------|-----------|---------|----------------------|

Column rules:
  - Axes: list all variation axes in the variation (e.g., "P+Q", "R").
  - Delta from prior rank: composite(this row) - composite(next lower rank). For Rank 1: "--".
    For ties: "0 -- [state tiebreak rule or 'no tiebreak applied']".
  - For any row where Delta = 0 AND the variation contains more axes than the one ranked
    one lower, write a ZERO INCREMENT NOTE immediately below the row:

      ZERO INCREMENT NOTE -- [output ID]: Adding [axis name] to [prior combination] produced
      zero composite increment. Explain why: [what mechanism or criterion the axis targeted
      and why it added no new PASS verdicts given the other axes already present]

All N outputs must appear. "See scores above" does not satisfy C-06.

**EXCELLENCE SIGNALS**

Signal: [output ID] -- [criterion ID] -- [structural mechanism producing the difference]

Generic rankings are not excellence signals. If no outlier pair: state explicitly.

**FAILURE PATTERNS**

Required even when empty: "No failure patterns -- all criteria passed in at least one output."

**REGRESSION SIGNALS**

If prior data: named regressions with output ID, criterion ID, prior and current verdict.
If no prior data: "No prior round data; regression analysis not possible."

**PER-OUTPUT SYNTHESIS NOTES**

One paragraph per output on structural score drivers. Explain the mechanism, not the counts.

---

## V-03: Axis T -- Axis Architecture Audit

**Variation axis**: Lifecycle emphasis -- a new AXIS ARCHITECTURE AUDIT block at Phase 3
exit (before synthesis) produces a per-axis verdict table: for each axis present across any
variation, list the criterion it targeted and whether it produced a composite increment in
this scoring run. Rows where increment = 0 are flagged ZERO and require an annotation.

**Hypothesis**: The per-axis audit forces systematic enumeration of all axes and their
criterion contributions. The annotation requirement for ZERO rows ("explain why the targeted
criterion was already satisfied") produces a statement about why the axis failed to increment
but does not mandate the three elements C-22 PASS requires (redundant axis name, criterion,
subsuming mechanism name). A scorer may write "criterion already PASS -- axis redundant"
without naming which mechanism in the other axis performs the subsuming function. C-22
PARTIAL predicted: per-axis verdicts present, mechanism-subsuming identification absent
unless the scorer infers the stricter requirement. C-19 PARTIAL (entry lock as structural
imperative, no binary declaration). C-20, C-21 FAIL (no criterion-ID anchoring, no
COVERAGE ASSERTION).

---

You are running quest-score against the v7 rubric.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite score computed from
the rubric formula, and a golden-threshold determination. The final scorecard includes a
ranked leaderboard, excellence signals, failure patterns, regression signals, and an axis
architecture audit.

---

FORMULA CHANGE ALERT -- READ BEFORE ANY COMPUTATION

The v7 rubric changes the aspirational denominator from the v6 value.

  N_aspirational: 12 (v6) -> 14 (v7)

Composite formula (v7, active):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 14 * 10)

  PARTIAL counts as 0.5. FAIL counts as 0. Golden: ALL 5 essentials PASS AND composite >= 80.

Do not compute any score using /12 or any prior denominator.

---

PHASE 1: LOAD, DELTA REGISTER, AND BILATERAL AUDIT

Before scoring, complete sections 1a through 1d in order.

**1a. Load summary**

  (a) all criteria IDs with tier labels (C-01--C-05 essential, C-06--C-08 recommended,
      C-09--C-22 aspirational)
  (b) exact composite formula text (v7 active: /14 aspirational denominator)
  (c) golden threshold: all 5 essentials PASS AND composite >= 80
  (d) count and list of outputs being scored

After writing, write this required labeled field:

  Inertia (C-01): Without the load block, criteria count (22), formula denominator (/14),
  and threshold are unverified. A scorer who skips produces a matrix missing C-21/C-22 rows
  and composites using /12 -- both invisible until Phase 3.

**1b. Formula version delta**

  Formula version delta: N_aspirational changed from [prior value] to [current value] in v[N].

If prior unknown: "No prior version delta detectable -- scoring under v7 as baseline."

After writing, write this required labeled field:

  Inertia (C-13, C-15): "N_aspirational=14" passes C-01 but fails C-15. Prior value (12)
  must be named. Both sides required to confirm the transition.

**1c. SYMMETRIC DELTA REGISTER**

  | Comparison type | Prior state | Current state |
  |-----------------|-------------|---------------|
  | N_aspirational | [prior -- e.g., "12 (v6)"] | [current -- e.g., "14 (v7)"] |
  | Regression verdicts | [prior or "No prior -- N/A"] | [current or "--"] |
  | Arithmetic discrepancies | [stated or "No discrepancy -- N/A"] | [computed or "--"] |

Blank Prior State = structural violation.

After writing, write this required labeled field:

  Inertia (C-15): Two-column structure makes prior-state omission detectable by column scan.

**1d. BILATERAL SYMMETRY AUDIT SWEEP (Phase 1 exit)**

  | Comparison | Symmetric? |
  |------------|-----------|
  | N_aspirational | [YES -- Prior: [v], Current: [v] | NO | PARTIAL -- N/A] |
  | Regression verdicts | [YES | NO | PARTIAL] |
  | Arithmetic discrepancies | [YES | NO | PARTIAL] |

Symmetric: NO requires remediation before Phase 2.

After writing, write this required labeled field:

  Inertia (C-18): Register prevents asymmetric entries. Sweep catches them independently.
  A Symmetric: NO is visible by scan without re-reading register prose.

PHASE 1 COMPLETE.

---

PHASE 2: SCORE EACH OUTPUT

**MODEL CELL (Phase 2 entry -- write before any verdict row)**

  Evidence (model): "from [output ID], [section or structural element]: [verbatim quote or
  structural observation -- not a criterion restatement]"
  Locatability test: YES -- proceed. NO -- rewrite.

After writing, write this required labeled field:

  Inertia (C-11, C-14): Model cell fires before the first verdict, establishing the evidence
  standard before any cell can set a lower norm.

ENTRY LOCK: no verdict row before the model cell passes the locatability test.

For each output, produce a scoring table:

  | ID | Criterion | Tier | Verdict | Evidence |

Include rows for all criteria C-01 through C-22. No row blank or missing.

After the table:
  essential_pass = [count; PARTIAL = 0.5]
  recommended_pass = [count; PARTIAL = 0.5]
  aspirational_pass = [count; PARTIAL = 0.5]
  composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 14 * 10) = [result]
  Golden: YES | NO -- [reason]

Score all N outputs before proceeding to Phase 3.

---

PHASE 3: VERIFY

**3a. Arithmetic verification**

  Verification (output: [ID]):
    stated counts: E=[X]/5, R=[X]/3, A=[X]/14
    computed composite: ([X]/5 * 60) + ([X]/3 * 30) + ([X]/14 * 10) = [result]
    Matches stated score: YES | NO -- discrepancy: stated [X], computed [Y]

After writing, write this required labeled field:

  Inertia (C-12): YES/NO binary field required. Narrative verification does not satisfy C-12.

**3b. Regression section**

  If prior data: "[Output ID] / [Criterion ID]: prior=[verdict], current=[verdict]"
  If no prior data: "No prior round data -- regression analysis cannot be performed."

After writing, write this required labeled field:

  Inertia (C-09): Section required even when empty.

**3c. AXIS ARCHITECTURE AUDIT**

After completing regression and before synthesis, produce this table. Include one row per
axis present across the full set of scored variations.

  | Axis | Criterion targeted | Present in variations | Composite increment when axis added | Verdict |
  |------|-------------------|-----------------------|---------------------------------------|---------|

Column rules:
  - Axis: name of the variation axis (e.g., P, Q, R, S).
  - Criterion targeted: the criterion the axis was designed to advance (e.g., C-19, C-20).
  - Present in variations: list which variation IDs include this axis.
  - Composite increment when axis added: the highest delta observed between a variation without
    this axis and a variation with only this axis added. If the axis appears only in
    combinations, state the combination-level delta with the combination noted.
  - Verdict: POSITIVE (increment > 0) | ZERO (increment = 0).

For every ZERO verdict row, write an annotation immediately below:

  ZERO AXIS NOTE -- [axis]: Adding [axis] to [variation without axis] -> [variation with axis]
  produced zero composite increment. [State which criterion the axis targeted and explain
  why it added no PASS verdicts given the mechanisms already present in the other variation.]

AXIS ARCHITECTURE AUDIT COMPLETE.

---

SYNTHESIS

Write the following sections in order.

**LEADERBOARD**

  | Rank | Output | Composite | Golden? |

All N outputs ranked descending. Ties noted explicitly.

**EXCELLENCE SIGNALS**

Signal: [output ID] -- [criterion ID] -- [structural mechanism producing the difference]

If no outlier pair: state explicitly.

**FAILURE PATTERNS**

Required even when empty: "No failure patterns -- all criteria passed in at least one output."

**REGRESSION SIGNALS**

If prior data: named regressions. If no prior data: "No prior round data; regression
analysis not possible."

**PER-OUTPUT SYNTHESIS NOTES**

One paragraph per output on structural score drivers. Explain the mechanism, not the counts.

---

## V-04: Axes P+Q+R -- Entry Lock Declaration + Coverage Assertion + Non-Additivity Block

**Variation axis**: Combination -- P (Phase 2 entry gate binary declaration), Q (explicit
criterion-ID anchoring in inertia labels plus Phase 1 exit COVERAGE ASSERTION), and R
(NON-ADDITIVITY ANALYSIS block in synthesis). The R6 minimal-sufficient-combination (P+Q)
plus the new C-22 axis (R).

**Hypothesis**: P achieves C-19 PASS (ENTRY LOCK binary declaration). Q achieves C-20 PASS
(criterion-ID anchoring in every Inertia label) and C-21 PASS (COVERAGE ASSERTION at Phase 1
exit). R achieves C-22 PASS (three-field non-additivity schema). All four criteria added since
v5 are satisfied simultaneously. If V-05 (P+Q+R+S) ties V-04 at 99.64, S is confirmed
non-additive given R: the delta table provides numerical corroboration but no additional
criterion pass, mirroring the R6 finding that N+O added zero increment given P+Q.

---

You are running quest-score against the v7 rubric.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite score computed from
the rubric formula, and a golden-threshold determination. The final scorecard includes a
ranked leaderboard, excellence signals, failure patterns, regression signals, and
non-additivity analysis.

---

FORMULA CHANGE ALERT -- READ BEFORE ANY COMPUTATION

The v7 rubric changes the aspirational denominator from the v6 value.

  N_aspirational: 12 (v6) -> 14 (v7)

Composite formula (v7, active):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 14 * 10)

  PARTIAL counts as 0.5. FAIL counts as 0. Golden: ALL 5 essentials PASS AND composite >= 80.

Do not compute any score using /12 or any prior denominator. If a conflict exists between
this prompt and a rubric file, the rubric file governs.

---

PHASE 1: LOAD, DELTA REGISTER, BILATERAL AUDIT, AND COVERAGE ASSERTION

Complete sections 1a through 1e in order. Do not proceed to Phase 2 until all five sections
are written, the bilateral audit shows no Symmetric: NO rows, and the coverage assertion
is complete.

**1a. Load summary**

Produce a block confirming the rubric was read. The block must name all four elements:
  (a) all criteria IDs with tier labels (C-01--C-05 essential, C-06--C-08 recommended,
      C-09--C-22 aspirational)
  (b) the exact composite formula text (v7 active: /14 aspirational denominator)
  (c) the golden threshold condition (all 5 essentials PASS AND composite >= 80)
  (d) the count and list of outputs being scored

After writing, write this required labeled field:

  Inertia (C-01): Without this load block, criteria count (22), formula denominator (/14),
  and threshold are unverified. A scorer who skips produces a matrix missing C-21/C-22 rows
  and composites using /12 -- both invisible until Phase 3.

**1b. Formula version delta**

  Formula version delta: N_aspirational changed from [prior value] to [current value] in v[N].
  Example: "N_aspirational changed from 12 (v6) to 14 (v7)."

If prior unknown: "No prior version delta detectable -- scoring under v7 as baseline."

After writing, write this required labeled field:

  Inertia (C-13, C-15): "N_aspirational=14" passes C-01 but fails C-15. Prior value (12)
  must be named. Both sides required to confirm the transition.

**1c. SYMMETRIC DELTA REGISTER**

  | Comparison type | Prior state | Current state |
  |-----------------|-------------|---------------|
  | N_aspirational | [prior -- e.g., "12 (v6)"] | [current -- e.g., "14 (v7)"] |
  | Regression verdicts | [prior or "No prior-round data -- row N/A"] | [current or "--"] |
  | Arithmetic discrepancies | [stated or "No discrepancy -- row N/A"] | [computed or "--"] |

Blank Prior State = structural violation.

After writing, write this required labeled field:

  Inertia (C-15): Two-column structure makes prior-state omission a detectable gap by column
  scan. A scorer writing only "N_aspirational=14" produces a visible blank in Prior State.

**1d. BILATERAL SYMMETRY AUDIT SWEEP (Phase 1 exit)**

  | Comparison | Symmetric? |
  |------------|-----------|
  | N_aspirational | [YES -- Prior: [v], Current: [v] | NO -- [missing] | PARTIAL -- N/A] |
  | Regression verdicts | [YES | NO | PARTIAL] |
  | Arithmetic discrepancies | [YES | NO | PARTIAL] |

Symmetric: NO requires remediation before Phase 2.

After writing, write this required labeled field:

  Inertia (C-18): Register prevents asymmetric entries by column structure. Sweep catches
  them independently. Prevention and catch are both required.

**1e. CRITERION-INERTIA COVERAGE ASSERTION**

After the bilateral audit, verify that every scored criterion ID (C-01 through C-22) will
appear in at least one Inertia label in this output. Produce the following assertion table:

  | Criterion | Covered? | Location |
  |-----------|----------|----------|
  | C-01 | YES | Inertia (C-01): at 1a |
  | C-13 | YES | Inertia (C-13, C-15): at 1b |
  | C-15 | YES | Inertia (C-15): at 1c; also 1b |
  | C-18 | YES | Inertia (C-18): at 1d |
  | C-20 | YES | Inertia (C-20, C-21): at 1e |
  | C-21 | YES | Inertia (C-20, C-21): at 1e |
  | C-11, C-14, C-19 | DEFERRED | Covered by MODEL CELL + ENTRY LOCK at Phase 2 entry |
  | C-12 | DEFERRED | Covered by arithmetic verification block at 3a |
  | C-09 | DEFERRED | Covered by regression section at 3b |
  | C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-16, C-17, C-22 | DEFERRED | Covered by Phase 2 scoring and synthesis mechanisms |

For any criterion not appearing in the table: add it to DEFERRED and note the coverage
location. Criteria absent from all rows is a coverage gap.

After writing, write this required labeled field:

  Inertia (C-20, C-21): Bare "Inertia: [text]" satisfies C-17 but fails C-20 -- no criterion
  ID. C-21 requires this phase-boundary assertion: a reader confirms total inertia-label
  coverage by reading one field rather than scanning every label.

PHASE 1 COMPLETE. Proceed to Phase 2 only after 1a, 1b, 1c, 1d, and 1e are written.

---

PHASE 2: SCORE EACH OUTPUT

**MODEL CELL + ENTRY LOCK (Phase 2 entry -- write before any verdict row)**

Write the following three elements in sequence before any criterion-output evidence row.

(1) Evidence (model):
  "from [output ID], [section or structural element]: [verbatim quote or structural
  observation that locates a specific feature -- not a criterion restatement]"
  Locatability test: YES -- proceed. NO -- rewrite before entering any verdict row.

(2) Required labeled field after the model cell:

  Inertia (C-11, C-14): Without a model cell at Phase 2 entry, evidence cells default to
  criterion restatement. The model cell fires first, establishing the evidence standard before
  any cell can set a lower norm.

(3) Binary gate declaration:

  ENTRY LOCK: no verdict row written before model cell. [Confirmed | Violated -- first verdict
  row appears at: ___]

  Write "Confirmed" if the model cell is the first Phase 2 content written.
  Write "Violated -- first verdict row appears at: [location]" if any verdict row preceded
  the model cell. A "Violated" declaration earns C-14 FAIL but C-19 PASS (the mechanism
  reported accurately). The ENTRY LOCK field is required; omitting it earns C-19 FAIL.

For each output, produce a scoring table:

  | ID | Criterion | Tier | Verdict | Evidence |

Column rules:
  - Verdict: PASS | PARTIAL | FAIL only.
  - Evidence: must quote, paraphrase with location, or name a specific structural feature.
    Criterion restatement is not evidence.
  - Every Inertia label written in evidence or annotations must use criterion-ID anchoring:
    "Inertia (C-XX): [failure mode]" -- not bare "Inertia: [failure mode]".
  - No row blank or missing. Include rows for all criteria C-01 through C-22.

After the scoring table, write the composite:

  essential_pass = [count; PARTIAL = 0.5]
  recommended_pass = [count; PARTIAL = 0.5]
  aspirational_pass = [count; PARTIAL = 0.5]
  composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 14 * 10) = [result]
  Golden: YES -- all essentials PASS; composite >= 80 | NO -- [which essential failed or composite < 80]

Score all N outputs before proceeding to Phase 3.

---

PHASE 3: VERIFY

**3a. Arithmetic verification**

  Verification (output: [ID]):
    stated counts: E=[X]/5, R=[X]/3, A=[X]/14
    computed composite: ([X]/5 * 60) + ([X]/3 * 30) + ([X]/14 * 10) = [result]
    Matches stated score: YES | NO -- discrepancy: stated [X], computed [Y]

After writing, write this required labeled field:

  Inertia (C-12): YES/NO binary field required. Narrative verification does not satisfy C-12.

If a discrepancy is found, update the SYMMETRIC DELTA REGISTER Arithmetic Discrepancy row.

**3b. Regression section**

  If prior data: "[Output ID] / [Criterion ID]: prior=[verdict], current=[verdict]"
  If no prior data: "No prior round data -- regression analysis cannot be performed."

After writing, write this required labeled field:

  Inertia (C-09): Section required even when empty.

---

SYNTHESIS

Write the following sections in order.

**LEADERBOARD**

  | Rank | Output | Composite | Golden? |

All N outputs ranked descending. Ties noted explicitly with tiebreak rule or
"tied -- no tiebreak applied." "See scores above" does not satisfy C-06.

**EXCELLENCE SIGNALS**

Signal: [output ID] -- [criterion ID] -- [structural mechanism producing the difference]

Generic rankings are not excellence signals. If no outlier pair: state explicitly.

**FAILURE PATTERNS**

Required even when empty: "No failure patterns -- all criteria passed in at least one output."

**NON-ADDITIVITY ANALYSIS**

For each pair of variations where one variation uses a strict subset of the other's axes,
compute the composite increment:
  Increment = variation_with_more_axes.composite - variation_with_fewer_axes.composite

For any pair where Increment = 0:

  Redundant axis: [name the axis added that produced zero composite increment]
  Criterion target: [name the criterion the redundant axis was designed to advance]
  Subsuming mechanism: [name the specific mechanism in the other axis that performs the same
    function -- identify what it does that makes the redundant axis's contribution zero]

All three fields are required for each zero-increment pair. A zero-increment declaration
without the subsuming mechanism satisfies C-22 at PARTIAL only.

If no zero-increment pair exists:
  "No non-additivity observed -- all axes produced positive composite increment."

If only one variation is scored:
  "Single variation scored -- non-additivity analysis not applicable."

Required: this section must appear whether or not non-additivity is observed. Omitting it
entirely earns C-22 FAIL.

**REGRESSION SIGNALS**

If prior data: named regressions with output ID, criterion ID, prior and current verdict.
If no prior data: "No prior round data; regression analysis not possible."

**PER-OUTPUT SYNTHESIS NOTES**

One paragraph per output on structural score drivers. Explain the mechanism, not the counts.

---

## V-05: Axes P+Q+R+S -- Entry Lock + Coverage Assertion + Non-Additivity Block + Increment Table

**Variation axis**: Full combination -- P+Q+R from V-04 plus S (COMPOSITE INCREMENT TABLE
in the leaderboard with zero-increment notes). Tests whether S is non-additive given R.

**Hypothesis**: R's NON-ADDITIVITY ANALYSIS block already satisfies C-22 with the three
required fields (redundant axis, criterion, subsuming mechanism). S's COMPOSITE INCREMENT
TABLE provides numerical corroboration of zero-increment findings but cannot push C-22 above
PASS. If V-05 ties V-04 at 99.64, the R7 non-additivity finding is: S is redundant given R.
S's mechanism -- numeric delta surfacing -- is subsumed by R's mechanism: the schema-bound
structural analysis block forces the same criterion-targeting and mechanism-naming that S's
explanation would provide, making S's contribution zero.

---

You are running quest-score against the v7 rubric.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite score computed from
the rubric formula, and a golden-threshold determination. The final scorecard includes a
ranked leaderboard with composite increments, excellence signals, failure patterns,
regression signals, and non-additivity analysis.

---

FORMULA CHANGE ALERT -- READ BEFORE ANY COMPUTATION

The v7 rubric changes the aspirational denominator from the v6 value.

  N_aspirational: 12 (v6) -> 14 (v7)

Composite formula (v7, active):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 14 * 10)

  PARTIAL counts as 0.5. FAIL counts as 0. Golden: ALL 5 essentials PASS AND composite >= 80.

Do not compute any score using /12 or any prior denominator. If a conflict exists between
this prompt and a rubric file, the rubric file governs.

---

PHASE 1: LOAD, DELTA REGISTER, BILATERAL AUDIT, AND COVERAGE ASSERTION

Complete sections 1a through 1e in order. Do not proceed to Phase 2 until all five sections
are written, the bilateral audit shows no Symmetric: NO rows, and the coverage assertion
is complete.

**1a. Load summary**

  (a) all criteria IDs with tier labels (C-01--C-05 essential, C-06--C-08 recommended,
      C-09--C-22 aspirational)
  (b) exact composite formula text (v7 active: /14 aspirational denominator)
  (c) golden threshold: all 5 essentials PASS AND composite >= 80
  (d) count and list of outputs being scored

After writing, write this required labeled field:

  Inertia (C-01): Without the load block, criteria count (22), formula denominator (/14),
  and threshold are unverified. A scorer who skips produces a matrix missing C-21/C-22 rows
  and composites using /12 -- both invisible until Phase 3.

**1b. Formula version delta**

  Formula version delta: N_aspirational changed from [prior value] to [current value] in v[N].
  Example: "N_aspirational changed from 12 (v6) to 14 (v7)."

If prior unknown: "No prior version delta detectable -- scoring under v7 as baseline."

After writing, write this required labeled field:

  Inertia (C-13, C-15): "N_aspirational=14" passes C-01 but fails C-15. Prior value (12)
  must be named. Both sides required to confirm the transition.

**1c. SYMMETRIC DELTA REGISTER**

  | Comparison type | Prior state | Current state |
  |-----------------|-------------|---------------|
  | N_aspirational | [prior -- e.g., "12 (v6)"] | [current -- e.g., "14 (v7)"] |
  | Regression verdicts | [prior or "No prior -- N/A"] | [current or "--"] |
  | Arithmetic discrepancies | [stated or "No discrepancy -- N/A"] | [computed or "--"] |

Blank Prior State = structural violation.

After writing, write this required labeled field:

  Inertia (C-15): Two-column structure makes prior-state omission detectable by column scan.

**1d. BILATERAL SYMMETRY AUDIT SWEEP (Phase 1 exit)**

  | Comparison | Symmetric? |
  |------------|-----------|
  | N_aspirational | [YES -- Prior: [v], Current: [v] | NO | PARTIAL -- N/A] |
  | Regression verdicts | [YES | NO | PARTIAL] |
  | Arithmetic discrepancies | [YES | NO | PARTIAL] |

Symmetric: NO requires remediation before Phase 2.

After writing, write this required labeled field:

  Inertia (C-18): Register prevents asymmetric entries. Sweep catches them independently.
  A Symmetric: NO is visible by scan without reading register prose.

**1e. CRITERION-INERTIA COVERAGE ASSERTION**

After the bilateral audit, verify that every scored criterion ID (C-01 through C-22) will
appear in at least one Inertia label in this output. Produce the following assertion table:

  | Criterion | Covered? | Location |
  |-----------|----------|----------|
  | C-01 | YES | Inertia (C-01): at 1a |
  | C-13 | YES | Inertia (C-13, C-15): at 1b |
  | C-15 | YES | Inertia (C-15): at 1c; also 1b |
  | C-18 | YES | Inertia (C-18): at 1d |
  | C-20 | YES | Inertia (C-20, C-21): at 1e |
  | C-21 | YES | Inertia (C-20, C-21): at 1e |
  | C-11, C-14, C-19 | DEFERRED | Covered by MODEL CELL + ENTRY LOCK at Phase 2 entry |
  | C-12 | DEFERRED | Covered by arithmetic verification block at 3a |
  | C-09 | DEFERRED | Covered by regression section at 3b |
  | C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-16, C-17, C-22 | DEFERRED | Covered by Phase 2 and synthesis mechanisms |

For any criterion not appearing: add to DEFERRED with intended coverage location. Criteria
absent from all rows is a coverage gap.

After writing, write this required labeled field:

  Inertia (C-20, C-21): Bare "Inertia: [text]" satisfies C-17 but fails C-20. C-21 requires
  this phase-boundary assertion: total inertia-label coverage confirmable by reading one field,
  not by scanning every label.

PHASE 1 COMPLETE. Proceed to Phase 2 only after 1a, 1b, 1c, 1d, and 1e are written.

---

PHASE 2: SCORE EACH OUTPUT

**MODEL CELL + ENTRY LOCK (Phase 2 entry -- write before any verdict row)**

Write the following three elements in sequence before any criterion-output evidence row.

(1) Evidence (model):
  "from [output ID], [section or structural element]: [verbatim quote or structural
  observation that locates a specific feature -- not a criterion restatement]"
  Locatability test: YES -- proceed. NO -- rewrite.

(2) Required labeled field:

  Inertia (C-11, C-14): Without a model cell at Phase 2 entry, evidence cells default to
  criterion restatement. The model cell fires first, establishing the standard before any
  cell can set a lower norm.

(3) Binary gate declaration:

  ENTRY LOCK: no verdict row written before model cell. [Confirmed | Violated -- first verdict
  row appears at: ___]

  "Confirmed" if model cell is first Phase 2 content. "Violated -- first verdict row at:
  [location]" if any verdict row preceded. The ENTRY LOCK field is required; omitting earns
  C-19 FAIL.

For each output, produce a scoring table:

  | ID | Criterion | Tier | Verdict | Evidence |

Column rules:
  - Verdict: PASS | PARTIAL | FAIL only.
  - Evidence: must quote, paraphrase with location, or name a specific structural feature.
    Criterion restatement is not evidence.
  - Every Inertia label must use criterion-ID anchoring: "Inertia (C-XX): [text]".
  - No row blank or missing. Include rows for all criteria C-01 through C-22.

After the scoring table, write the composite:

  essential_pass = [count; PARTIAL = 0.5]
  recommended_pass = [count; PARTIAL = 0.5]
  aspirational_pass = [count; PARTIAL = 0.5]
  composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 14 * 10) = [result]
  Golden: YES | NO -- [reason]

Score all N outputs before proceeding to Phase 3.

---

PHASE 3: VERIFY

**3a. Arithmetic verification**

  Verification (output: [ID]):
    stated counts: E=[X]/5, R=[X]/3, A=[X]/14
    computed composite: ([X]/5 * 60) + ([X]/3 * 30) + ([X]/14 * 10) = [result]
    Matches stated score: YES | NO -- discrepancy: stated [X], computed [Y]

After writing, write this required labeled field:

  Inertia (C-12): YES/NO binary field required. Narrative verification does not satisfy C-12.

**3b. Regression section**

  If prior data: "[Output ID] / [Criterion ID]: prior=[verdict], current=[verdict]"
  If no prior data: "No prior round data -- regression analysis cannot be performed."

After writing, write this required labeled field:

  Inertia (C-09): Section required even when empty.

---

SYNTHESIS

Write the following sections in order.

**LEADERBOARD WITH COMPOSITE INCREMENT TABLE**

  | Rank | Output | Axes | Composite | Golden? | Delta from prior rank |
  |------|--------|------|-----------|---------|----------------------|

Column rules:
  - Axes: list all variation axes (e.g., "P+Q+R+S", "P+Q+R").
  - Delta from prior rank: composite(this row) - composite(next lower rank). Rank 1: "--".
    Ties: "0 -- [tiebreak rule or 'no tiebreak applied']".
  - For any row where Delta = 0 AND the variation contains more axes than the one ranked
    one lower, write a ZERO INCREMENT NOTE immediately below:

      ZERO INCREMENT NOTE -- [output ID]: Adding [axis name] to [prior combination] produced
      zero composite increment. Explain why: [what mechanism or criterion was targeted and
      why it added no new PASS verdicts given the other axes already present]

All N outputs must appear. "See scores above" does not satisfy C-06.

**EXCELLENCE SIGNALS**

Signal: [output ID] -- [criterion ID] -- [structural mechanism producing the difference]

Generic rankings are not excellence signals. If no outlier pair: state explicitly.

**FAILURE PATTERNS**

Required even when empty: "No failure patterns -- all criteria passed in at least one output."

**NON-ADDITIVITY ANALYSIS**

For each pair of variations where one variation uses a strict subset of the other's axes,
compute the composite increment:
  Increment = variation_with_more_axes.composite - variation_with_fewer_axes.composite

For any pair where Increment = 0:

  Redundant axis: [name the axis added that produced zero composite increment]
  Criterion target: [name the criterion the redundant axis was designed to advance]
  Subsuming mechanism: [name the specific mechanism in the other axis that performs the same
    function -- identify what it does that makes the redundant axis's contribution zero]

All three fields are required for each zero-increment pair. A zero-increment declaration
without the subsuming mechanism satisfies C-22 at PARTIAL only.

If no zero-increment pair:
  "No non-additivity observed -- all axes produced positive composite increment."

If only one variation scored:
  "Single variation scored -- non-additivity analysis not applicable."

Required: this section must appear whether or not non-additivity is observed.

**REGRESSION SIGNALS**

If prior data: named regressions with output ID, criterion ID, prior and current verdict.
If no prior data: "No prior round data; regression analysis not possible."

**PER-OUTPUT SYNTHESIS NOTES**

One paragraph per output on structural score drivers. Explain the mechanism, not the counts.
