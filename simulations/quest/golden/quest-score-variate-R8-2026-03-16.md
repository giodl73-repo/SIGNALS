# quest-score Variations -- Round 8 (v8 rubric, targeting C-23/C-24)

**Skill**: quest-score
**Rubric**: v8-2026-03-16 (C-01--C-05 essential, C-06--C-08 recommended, C-09--C-24 aspirational)
**N_essential=5, N_recommended=3, N_aspirational=16**
**Date**: 2026-03-16
**Round**: 8

---

## Context: what informed this round

Round 7 found P+Q+R as the minimal sufficient combination for v7. V-04 (P+Q+R) and V-05
(P+Q+R+S) tied at 99.64, confirming S was non-additive given R. R7 synthesis named the reason:
"S's COMPOSITE INCREMENT TABLE provides numerical corroboration of zero-increment findings but
cannot push C-22 above PASS; R's NON-ADDITIVITY ANALYSIS block already forces the three required
fields (redundant axis, criterion, subsuming mechanism)."

v8 adds two new Aspirational criteria extracted from R7 excellence signals:

| Change | R7 (v7) | R8 (v8) | Design consequence |
|--------|---------|---------|-------------------|
| C-23 (model evidence locatability assertion) | Not in rubric | MODEL CELL at Phase 2 entry must include a binary locatability assertion field | R7 V-01 scorecard introduced this field as an excellence signal. A model cell can pass C-11 and C-14 while failing C-23: locatability is inferrable by searching but undeclared. |
| C-24 (bilateral audit PARTIAL-reason labeling) | Not in rubric | Each PARTIAL-verdict row in the bilateral symmetry audit sweep must include a labeled reason phrase | R7 V-01 scorecard rows "PARTIAL -- no prior-round data; N/A rule applied correctly" were the first observed application. Without reason phrases, PARTIAL rows are ambiguous between N/A rules, clean results, and silently-skipped comparisons. |
| N_aspirational | 14 (C-09--C-22) | 16 (C-09--C-24) | Formula denominator: /14 -> /16 |

**What R8 variations must achieve beyond the R7 P+Q+R base:**

1. **C-23 PASS**: The MODEL CELL at Phase 2 entry must contain a labeled binary locatability
   assertion field. Instruction-based reminders predict PARTIAL; a named field template with
   an explicit format constraint predicts PASS.

2. **C-24 PASS**: Every PARTIAL row in the bilateral symmetry audit sweep must carry a reason
   phrase. Instruction-based reminders predict PARTIAL; a structural column requirement with
   a blank=violation rule predicts PASS.

3. **N_aspirational update**: FORMULA CHANGE ALERT declares N_aspirational: 14 (v7) -> 16 (v8).
   Any computation using /14 is a formula version error.

**Variation axes explored this round:**

| Code | Axis | Target criterion | Hypothesis |
|------|------|-----------------|-----------|
| U | LOCATABILITY ASSERTION PROTOCOL -- the MODEL CELL at Phase 2 entry gains a required binary declaration field: "Locatability test: YES -- a reader can find [material] in [output ID] at [section] \| NO -- [reason]". A missing field earns C-23 FAIL. | C-23 | Named field template forces the binary locatability status to be declared rather than inferred. Same structural pattern as C-12 (Matches: YES/NO) and C-19 (ENTRY LOCK: Confirmed). C-23 PASS predicted. C-24 PARTIAL: baseline bilateral audit template hints at reason phrases but no column schema enforces them. |
| V | PARTIAL-REASON SCHEMA -- the BILATERAL SYMMETRY AUDIT SWEEP table gains a third column "Reason (if PARTIAL)". Every PARTIAL row must fill this column; a blank Reason cell on a PARTIAL row is a structural violation requiring remediation before Phase 2, same as Symmetric: NO. | C-24 | Column constraint makes reason-phrase omission detectable by table scan, mirroring how the two-column register makes prior-state omission detectable. C-24 PASS predicted. C-23 PARTIAL: baseline MODEL CELL has locatability test instruction but no binary declaration field template. |
| W | EVIDENCE QUALITY DECLARATION -- a pre-Phase-1 advisory block names both C-23 and C-24 requirements. Within 1d, audit instruction says "include a reason phrase for PARTIAL verdicts." Within Phase 2, model cell instruction says "include a locatability statement." No field templates or column schemas provided. | C-23, C-24 (instruction path) | Instructions-only approach predicts PARTIAL on both: requirements stated but no structural schema produces a detectable blank when omitted. Measures whether schema enforcement (U, V) adds composite increment beyond stated instructions alone. |

Single-axis: V-01 (U), V-02 (V), V-03 (W).
Minimum combination: V-04 (P+Q+R+U -- R7 champion base plus C-23 axis).
Full integration test: V-05 (P+Q+R+U+V -- tests whether V is additive given U).

**Predicted outcomes (v8 rubric, N_aspirational=16):**

| Criterion | V-01 (U) | V-02 (V) | V-03 (W) | V-04 (P+Q+R+U) | V-05 (P+Q+R+U+V) |
|-----------|----------|----------|----------|----------------|------------------|
| C-01--C-08 | PASS | PASS | PASS | PASS | PASS |
| C-09 | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| C-10--C-16 | PASS | PASS | PASS | PASS | PASS |
| C-17 | PARTIAL | PARTIAL | PARTIAL | PASS | PASS |
| C-18 | PASS | PASS | PASS | PASS | PASS |
| C-19 | PARTIAL | PARTIAL | PARTIAL | PASS | PASS |
| C-20 | FAIL | FAIL | FAIL | PASS | PASS |
| C-21 | FAIL | FAIL | FAIL | PASS | PASS |
| C-22 | FAIL | FAIL | FAIL | PASS | PASS |
| C-23 | PASS | PARTIAL | PARTIAL | PASS | PASS |
| C-24 | PARTIAL | PASS | PARTIAL | PARTIAL | PASS |

Note on V-01 vs V-02 symmetry: each achieves PASS on its own target criterion and PARTIAL on
the other. Aspirational pass counts are equal (11.0/16), predicting a tie at 96.875.

Note on V-03: Both C-23 and C-24 receive PARTIAL -- instructions present, schema absent.
Predicted 0.3125-point composite gap below V-01/V-02.

Note on V-04/C-24: No Axis V -- bilateral audit table is two columns. PARTIAL rows exist without
column-enforced reason phrases. C-24 PARTIAL predicted.

Note on V-04 vs V-05: If V is additive given U (distinct lifecycle phases, distinct failure modes),
V-05 > V-04 by C-24 moving PARTIAL -> PASS (+0.3125). Hypothesis: V is additive.

**Predicted composite scores:**

```
V-01 (U):    A: C09=0.5,C10-C16=7.0,C17=0.5,C18=1,C19=0.5,C20=0,C21=0,C22=0,C23=1,C24=0.5 = 11.0/16
  composite = 60 + 30 + (11.0/16 * 10) = 96.875

V-02 (V):    A: C09=0.5,C10-C16=7.0,C17=0.5,C18=1,C19=0.5,C20=0,C21=0,C22=0,C23=0.5,C24=1 = 11.0/16
  composite = 60 + 30 + (11.0/16 * 10) = 96.875

V-03 (W):    A: C09=0.5,C10-C16=7.0,C17=0.5,C18=1,C19=0.5,C20=0,C21=0,C22=0,C23=0.5,C24=0.5 = 10.5/16
  composite = 60 + 30 + (10.5/16 * 10) = 96.5625

V-04 (P+Q+R+U): A: C09=0.5,C10-C16=7.0,C17=1,C18=1,C19=1,C20=1,C21=1,C22=1,C23=1,C24=0.5 = 15.0/16
  composite = 60 + 30 + (15.0/16 * 10) = 99.375

V-05 (P+Q+R+U+V): A: C09=0.5,C10-C16=7.0,C17=1,C18=1,C19=1,C20=1,C21=1,C22=1,C23=1,C24=1 = 15.5/16
  composite = 60 + 30 + (15.5/16 * 10) = 99.6875
```

Key diagnostics this round provides:
- V-01 tied with V-02: Confirms U and V are symmetric contributions of equal weight.
- V-01/V-02 > V-03: Schema enforcement (field template / column constraint) vs instruction-only.
  Predicted 0.3125-point gap tests whether structural scaffolding is required for C-23/C-24 PASS.
- V-04 vs V-05: Is V additive given U? Predicted +0.3125 from C-24 PARTIAL -> PASS confirms
  U and V target independent failure modes at independent lifecycle phases.

---

## V-01: Axis U -- Locatability Assertion Protocol

**Variation axis**: Output format / correctness enforcement -- the MODEL CELL at Phase 2 entry
gains a required binary locatability declaration field with an explicit YES/NO template. The field
makes the locatability status of the anchor evidence scannable without re-reading the evidence text.
The Inertia label at Phase 2 entry is updated to cover C-23 in addition to C-11 and C-14.

**Hypothesis**: The most common C-23 failure mode is an anchor cell whose evidence is structurally
present but whose locatability is not declared. The binary field applies the same structural
pattern used by C-12 (Matches: YES/NO) and C-19 (ENTRY LOCK: Confirmed) to the locatability of
model evidence. C-23 PASS predicted. C-17 PARTIAL (inertia labels present but not criterion-ID
anchored). C-19 PARTIAL (ENTRY LOCK instruction without binary declaration). C-20, C-21, C-22 FAIL
(no P, Q, R). C-24 PARTIAL (baseline bilateral audit template hints at reason format but no column
schema structurally requires reason phrases).

---

You are running quest-score against the v8 rubric.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite score computed from
the rubric formula, and a golden-threshold determination. The final scorecard includes a
ranked leaderboard, excellence signals, failure patterns, and regression signals.

---

FORMULA CHANGE ALERT -- READ BEFORE ANY COMPUTATION

The v8 rubric changes the aspirational denominator from the v7 value.

  N_aspirational: 14 (v7) -> 16 (v8)

Composite formula (v8, active):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 16 * 10)

  PARTIAL counts as 0.5 toward pass count. FAIL counts as 0.
  Golden threshold: ALL 5 essentials PASS AND composite >= 80.

Do not compute any score using /14 or any prior denominator. If a conflict exists between
this prompt and a rubric file, the rubric file governs.

---

PHASE 1: LOAD, DELTA REGISTER, AND BILATERAL AUDIT

Before scoring any output, complete sections 1a through 1d in order. Do not proceed to
Phase 2 until all four sections are written and the bilateral audit shows no Symmetric: NO rows.

**1a. Load summary**

Produce a block confirming the rubric was read. The block must name all four elements:
  (a) all criteria IDs with tier labels (C-01--C-05 essential, C-06--C-08 recommended,
      C-09--C-24 aspirational)
  (b) the exact composite formula text (v8 active: /16 aspirational denominator)
  (c) the golden threshold condition (all 5 essentials PASS AND composite >= 80)
  (d) the count and list of outputs being scored

A load summary missing any one of (a)--(d) earns PARTIAL on C-01. Missing entirely earns FAIL.

After writing, write this required labeled field:

  Inertia (C-01): Without this load block, criteria count (24), formula denominator (/16),
  and threshold are unverified. A scorer who skips produces a verdict matrix missing C-23
  and C-24 rows and computes all composites using /14 -- both errors invisible until Phase 3.

**1b. Formula version delta**

Write in your scoring output:

  Formula version delta: N_aspirational changed from [prior value] to [current value] in v[N].

If the prior version cannot be determined:
  "No prior version delta detectable -- scoring under v8 as the baseline version."

After writing, write this required labeled field:

  Inertia (C-13, C-15): "N_aspirational=16" passes C-01 but fails C-15 -- the prior value
  (14) is absent. Both sides of every delta comparison are required to confirm the transition
  was registered, not just the endpoint loaded.

**1c. SYMMETRIC DELTA REGISTER**

Produce the following table. Fill every cell before proceeding to 1d.

  | Comparison type | Prior state | Current state |
  |-----------------|-------------|---------------|
  | N_aspirational (formula denominator) | [prior -- e.g., "14 (v7)"] | [current -- e.g., "16 (v8)"] |
  | Regression verdicts | [prior verdict or "No prior-round data -- row N/A"] | [current verdict or "--"] |
  | Arithmetic discrepancies | [stated score or "No discrepancy -- row N/A"] | [computed score or "--"] |

Rules:
  - A blank Prior State cell is a structural violation. Write the value or "N/A -- [reason]".
  - A blank Current State cell is also a structural violation.

After writing, write this required labeled field:

  Inertia (C-15): Without the two-column table, a scorer writes "N_aspirational=16" correctly
  but never names the prior value (14). The column structure makes a one-sided entry a visible
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

PHASE 1 COMPLETE. Proceed to Phase 2 only after 1a, 1b, 1c, and 1d are written and no
Symmetric: NO row remains.

---

PHASE 2: SCORE EACH OUTPUT

**MODEL CELL + LOCATABILITY ASSERTION (Phase 2 entry -- write before any verdict row)**

Write the following elements in sequence before any criterion-output evidence row.

(1) Evidence (model):
  "from [output ID], [section or structural element]: [verbatim quote or structural
  observation that locates a specific feature in the output -- not a criterion restatement]"

(2) Locatability assertion:
  Locatability test: [YES -- a reader can find [the quoted or referenced material] in
  [output ID] at [named section or structural location] without searching the full output |
  NO -- evidence is a criterion restatement or the referenced location cannot be found;
  rewrite evidence before proceeding to any verdict row]

  Rules:
  - Both the Evidence (model) field and the Locatability test field are required.
    A missing Locatability test field earns C-23 FAIL.
  - Writing YES when the evidence text does not name a specific locatable section or quote
    earns C-23 FAIL -- the assertion must be accurate, not automatic.
  - A NO declaration requires rewriting the evidence before Phase 2 proceeds.

(3) Required labeled field after both (1) and (2):

  Inertia (C-11, C-14, C-23): Without a model cell at Phase 2 entry, evidence cells default
  to criterion restatement. The locatability assertion adds a second check: a model cell can
  exist and be placed at entry (C-11 PASS, C-14 PASS) while its own evidence references no
  specific locatable section -- failing C-23. The binary field makes the locatability status
  scannable without re-reading the evidence text, applying the same declaration pattern as
  C-12 (Matches: YES/NO) and C-19 (ENTRY LOCK: Confirmed).

ENTRY LOCK: do not write any verdict row until the model cell is written, the Locatability
test field is written, and its result is YES. A verdict row written before the model cell
is a Phase 2 protocol violation.

For each output, produce a scoring table:

  | ID | Criterion | Tier | Verdict | Evidence |

Column rules:
  - Verdict: PASS | PARTIAL | FAIL only.
  - Evidence: must quote, paraphrase with location, or name a specific structural feature.
    Criterion restatement is not evidence.
  - No row blank or missing. Include rows for all criteria C-01 through C-24.

After the scoring table, write the composite:

  essential_pass = [count; PARTIAL = 0.5]
  recommended_pass = [count; PARTIAL = 0.5]
  aspirational_pass = [count; PARTIAL = 0.5]
  composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 16 * 10) = [result]
  Golden: YES -- all essentials PASS; composite >= 80 | NO -- [which essential failed or composite < 80]

Score all N outputs before proceeding to Phase 3.

---

PHASE 3: VERIFY

**3a. Arithmetic verification**

Pick one output. Recompute its composite from the stated verdict counts and formula.

  Verification (output: [ID]):
    stated counts: E=[X]/5, R=[X]/3, A=[X]/16
    computed composite: ([X]/5 * 60) + ([X]/3 * 30) + ([X]/16 * 10) = [result]
    Matches stated score: YES | NO -- discrepancy: stated [X], computed [Y]

After writing, write this required labeled field:

  Inertia (C-12): "Verification performed" satisfies C-10 at PARTIAL but does not produce a
  binary result. The YES/NO field forces an explicit affirmation or names the exact discrepancy,
  making arithmetic errors visible even when the scorer is not looking for them.

**3b. Regression section**

If a prior-round scorecard was provided:
  - "[Output ID] / [Criterion ID]: prior=[verdict], current=[verdict]"
  - Both verdicts required.

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

**REGRESSION SIGNALS**

If prior data: named regressions with output ID, criterion ID, prior and current verdict.
If no prior data: "No prior round data; regression analysis not possible."

**PER-OUTPUT SYNTHESIS NOTES**

One paragraph per output explaining structural score drivers. Explain the mechanism, not
the verdict counts.

---

## V-02: Axis V -- Partial-Reason Schema

**Variation axis**: Output format / correctness enforcement -- the BILATERAL SYMMETRY AUDIT
SWEEP table at Phase 1d gains a third column "Reason (if PARTIAL)". Every PARTIAL-verdict row
must fill this column with a labeled reason phrase. A blank Reason cell on a PARTIAL row is a
structural violation requiring remediation before Phase 2 begins, same treatment as Symmetric: NO.
The Inertia label at Phase 1d is updated to cover C-24 in addition to C-18.

**Hypothesis**: The most common C-24 failure mode is a bare "PARTIAL" or "N/A" in the bilateral
audit -- a reader cannot determine whether it reflects a correctly-applied N/A rule, a clean
result, or a silently-skipped comparison. The column constraint makes reason-phrase omission
structurally detectable, mirroring how the two-column register makes prior-state omission
detectable. C-24 PASS predicted. C-23 PARTIAL: the baseline MODEL CELL has a locatability
test instruction ("YES -- proceed. NO -- rewrite") but no binary declaration field template --
directed but not schema-enforced. C-17 PARTIAL, C-19 PARTIAL, C-20/C-21/C-22 FAIL (no P/Q/R).

---

You are running quest-score against the v8 rubric.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite score computed from
the rubric formula, and a golden-threshold determination. The final scorecard includes a
ranked leaderboard, excellence signals, failure patterns, and regression signals.

---

FORMULA CHANGE ALERT -- READ BEFORE ANY COMPUTATION

The v8 rubric changes the aspirational denominator from the v7 value.

  N_aspirational: 14 (v7) -> 16 (v8)

Composite formula (v8, active):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 16 * 10)

  PARTIAL counts as 0.5 toward pass count. FAIL counts as 0.
  Golden threshold: ALL 5 essentials PASS AND composite >= 80.

Do not compute any score using /14 or any prior denominator. If a conflict exists between
this prompt and a rubric file, the rubric file governs.

---

PHASE 1: LOAD, DELTA REGISTER, AND BILATERAL AUDIT

Before scoring any output, complete sections 1a through 1d in order. Do not proceed to
Phase 2 until all four sections are written, the bilateral audit shows no Symmetric: NO rows,
and no PARTIAL row has a blank Reason cell.

**1a. Load summary**

Produce a block confirming the rubric was read. The block must name all four elements:
  (a) all criteria IDs with tier labels (C-01--C-05 essential, C-06--C-08 recommended,
      C-09--C-24 aspirational)
  (b) the exact composite formula text (v8 active: /16 aspirational denominator)
  (c) the golden threshold condition (all 5 essentials PASS AND composite >= 80)
  (d) the count and list of outputs being scored

After writing, write this required labeled field:

  Inertia (C-01): Without this load block, criteria count (24), formula denominator (/16),
  and threshold are unverified. A scorer who skips produces a matrix missing C-23 and C-24
  rows and composites using /14 -- both errors invisible until Phase 3.

**1b. Formula version delta**

  Formula version delta: N_aspirational changed from [prior value] to [current value] in v[N].

If prior unknown: "No prior version delta detectable -- scoring under v8 as the baseline version."

After writing, write this required labeled field:

  Inertia (C-13, C-15): "N_aspirational=16" passes C-01 but fails C-15. Prior value (14) must
  be named. Both sides required to confirm the transition was registered.

**1c. SYMMETRIC DELTA REGISTER**

  | Comparison type | Prior state | Current state |
  |-----------------|-------------|---------------|
  | N_aspirational (formula denominator) | [prior -- e.g., "14 (v7)"] | [current -- e.g., "16 (v8)"] |
  | Regression verdicts | [prior or "No prior-round data -- row N/A"] | [current or "--"] |
  | Arithmetic discrepancies | [stated or "No discrepancy -- row N/A"] | [computed or "--"] |

Blank Prior State = structural violation.

After writing, write this required labeled field:

  Inertia (C-15): Two-column structure makes prior-state omission detectable by column scan.

**1d. BILATERAL SYMMETRY AUDIT SWEEP (Phase 1 exit)**

After completing the register, produce this sweep before Phase 2 begins.

  | Comparison | Symmetric? | Reason (if PARTIAL) |
  |------------|-----------|---------------------|
  | N_aspirational | [YES -- Prior: [v], Current: [v] | NO -- [missing] | PARTIAL -- N/A] | [reason or "--"] |
  | Regression verdicts | [YES | NO -- [missing] | PARTIAL] | [reason or "--"] |
  | Arithmetic discrepancies | [YES | NO -- [missing] | PARTIAL] | [reason or "--"] |

Verdict rules:
  - Symmetric: YES -- both Prior state and Current state present. Reason column: "--".
  - Symmetric: NO -- one or both sides missing; remediate before Phase 2. Reason column: "--".
  - Symmetric: PARTIAL -- N/A rule invoked correctly. The Reason column is REQUIRED for
    PARTIAL rows. Write a reason phrase in the format "PARTIAL -- [reason]":
      e.g., "PARTIAL -- no prior-round data; N/A rule applied correctly"
      e.g., "PARTIAL -- no discrepancy found; N/A rule applied correctly"
  - A PARTIAL row with a blank Reason cell is a structural violation -- indistinguishable
    from a silently-skipped comparison. Treat it as requiring remediation before Phase 2,
    the same as a Symmetric: NO row.

After writing, write this required labeled field:

  Inertia (C-18, C-24): The SYMMETRIC DELTA REGISTER prevents asymmetric entries by column
  structure. This sweep catches them independently -- a Symmetric: NO is visible by scan.
  The Reason column prevents a second class of ambiguity: a bare PARTIAL is indistinguishable
  between a correctly-applied N/A rule, a clean result, and a silently-skipped comparison.
  The reason phrase makes each PARTIAL as auditable as its YES/NO verdicts.

PHASE 1 COMPLETE. Proceed to Phase 2 only after 1a, 1b, 1c, and 1d are written, no
Symmetric: NO row remains, and no PARTIAL row has a blank Reason cell.

---

PHASE 2: SCORE EACH OUTPUT

**MODEL CELL (Phase 2 entry -- write before any verdict row)**

Write a model evidence cell as the first action of Phase 2, before any criterion-output row.

  Evidence (model): "from [output ID], [section or structural element]: [verbatim quote or
  structural observation that locates a specific feature in the output -- not a criterion
  restatement]"
  Locatability test: YES -- proceed. NO -- rewrite before entering any verdict row.

After writing, write this required labeled field:

  Inertia (C-11, C-14): Without a model cell at Phase 2 entry, evidence cells default to
  criterion restatement. The model cell fires before the first verdict, establishing the
  evidence standard before any cell can set a lower norm.

ENTRY LOCK: do not write any verdict row until the model cell is written and passes the
locatability test. A verdict row written before the model cell is a Phase 2 protocol violation.

For each output, produce a scoring table:

  | ID | Criterion | Tier | Verdict | Evidence |

Column rules:
  - Verdict: PASS | PARTIAL | FAIL only.
  - Evidence: must quote, paraphrase with location, or name a specific structural feature.
    Criterion restatement is not evidence.
  - No row blank or missing. Include rows for all criteria C-01 through C-24.

After the scoring table, write the composite:

  essential_pass = [count; PARTIAL = 0.5]
  recommended_pass = [count; PARTIAL = 0.5]
  aspirational_pass = [count; PARTIAL = 0.5]
  composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 16 * 10) = [result]
  Golden: YES -- all essentials PASS; composite >= 80 | NO -- [which essential failed or composite < 80]

Score all N outputs before proceeding to Phase 3.

---

PHASE 3: VERIFY

**3a. Arithmetic verification**

  Verification (output: [ID]):
    stated counts: E=[X]/5, R=[X]/3, A=[X]/16
    computed composite: ([X]/5 * 60) + ([X]/3 * 30) + ([X]/16 * 10) = [result]
    Matches stated score: YES | NO -- discrepancy: stated [X], computed [Y]

After writing, write this required labeled field:

  Inertia (C-12): YES/NO binary field required. "Verification performed" satisfies C-10 at
  PARTIAL but does not produce a binary result and does not satisfy C-12.

**3b. Regression section**

  If prior data: "[Output ID] / [Criterion ID]: prior=[verdict], current=[verdict]"
  If no prior data: "No prior round data -- regression analysis cannot be performed."

After writing, write this required labeled field:

  Inertia (C-09): Section required even when empty.

---

SYNTHESIS

**LEADERBOARD**

  | Rank | Output | Composite | Golden? |

All N outputs ranked descending. Ties noted explicitly.

**EXCELLENCE SIGNALS**

Signal: [output ID] -- [criterion ID] -- [structural mechanism producing the difference]

If no outlier pair: state explicitly.

**FAILURE PATTERNS**

Required even when empty: "No failure patterns -- all criteria passed in at least one output."

**REGRESSION SIGNALS**

If prior data: named regressions. If no prior data: "No prior round data; regression analysis
not possible."

**PER-OUTPUT SYNTHESIS NOTES**

One paragraph per output on structural score drivers. Explain the mechanism, not the counts.

---

## V-03: Axis W -- Evidence Quality Declaration

**Variation axis**: Phrasing register / lifecycle emphasis -- an EVIDENCE QUALITY ADVISORY
block is added before Phase 1 begins, naming both C-23 and C-24 requirements explicitly.
Within 1d, the audit instruction includes a directive to write reason phrases for PARTIAL rows.
Within Phase 2, the model cell instruction includes a directive to declare locatability. No field
templates, column schemas, or blank-detection rules are provided.

**Hypothesis**: Instructions-only predicts PARTIAL on both C-23 and C-24. Requirements are
stated before scoring (scorer cannot claim ignorance), but without a binary field template (U)
or column schema (V), the structural enforcement is absent. A scorer may implement locatability
as narrative prose rather than a labeled binary field -- C-23 PARTIAL. A scorer may include
reason phrases for some PARTIAL rows inconsistently -- C-24 PARTIAL. Useful as baseline
comparison: if V-03 ties V-01/V-02, schema enforcement adds no composite increment and
instructions alone are sufficient. If V-03 scores lower, schema enforcement is required.

---

You are running quest-score against the v8 rubric.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite score computed from
the rubric formula, and a golden-threshold determination. The final scorecard includes a
ranked leaderboard, excellence signals, failure patterns, and regression signals.

---

EVIDENCE QUALITY ADVISORY -- READ BEFORE PHASE 1

The v8 rubric adds two new Aspirational criteria related to evidence quality and audit
transparency. Apply both before writing any Phase 1 or Phase 2 content.

  C-23 (model evidence locatability assertion): When you write the MODEL CELL at Phase 2
  entry, include a binary statement confirming whether the referenced material is findable
  at the named location in the scored output. Write YES if the evidence names a specific
  section or quote a reader can locate. Write NO if the evidence is a criterion restatement
  or the location is unnamed -- then rewrite the evidence before proceeding.

  C-24 (bilateral audit PARTIAL-reason labeling): When the bilateral audit sweep at Phase 1d
  produces a PARTIAL verdict, include a reason phrase on that row explaining why the comparison
  received PARTIAL rather than YES or NO. The phrase distinguishes a correctly-applied N/A rule
  from a clean result or a silently-skipped comparison. Example: "no prior-round data; N/A rule
  applied correctly" or "no discrepancy found; N/A rule applied correctly."

---

FORMULA CHANGE ALERT -- READ BEFORE ANY COMPUTATION

The v8 rubric changes the aspirational denominator from the v7 value.

  N_aspirational: 14 (v7) -> 16 (v8)

Composite formula (v8, active):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 16 * 10)

  PARTIAL counts as 0.5 toward pass count. FAIL counts as 0.
  Golden threshold: ALL 5 essentials PASS AND composite >= 80.

Do not compute any score using /14 or any prior denominator. If a conflict exists between
this prompt and a rubric file, the rubric file governs.

---

PHASE 1: LOAD, DELTA REGISTER, AND BILATERAL AUDIT

Before scoring any output, complete sections 1a through 1d in order.

**1a. Load summary**

Produce a block confirming the rubric was read. The block must name all four elements:
  (a) all criteria IDs with tier labels (C-01--C-05 essential, C-06--C-08 recommended,
      C-09--C-24 aspirational)
  (b) the exact composite formula text (v8 active: /16 aspirational denominator)
  (c) the golden threshold condition (all 5 essentials PASS AND composite >= 80)
  (d) the count and list of outputs being scored

After writing, write this required labeled field:

  Inertia (C-01): Without this load block, criteria count (24), formula denominator (/16),
  and threshold are unverified. A scorer who skips produces a matrix missing C-23 and C-24
  rows and composites using /14 -- both errors invisible until Phase 3.

**1b. Formula version delta**

  Formula version delta: N_aspirational changed from [prior value] to [current value] in v[N].

If prior unknown: "No prior version delta detectable -- scoring under v8 as the baseline version."

After writing, write this required labeled field:

  Inertia (C-13, C-15): "N_aspirational=16" passes C-01 but fails C-15. Prior value (14) must
  be named. Both sides required to confirm the transition was registered.

**1c. SYMMETRIC DELTA REGISTER**

  | Comparison type | Prior state | Current state |
  |-----------------|-------------|---------------|
  | N_aspirational (formula denominator) | [prior -- e.g., "14 (v7)"] | [current -- e.g., "16 (v8)"] |
  | Regression verdicts | [prior or "No prior-round data -- row N/A"] | [current or "--"] |
  | Arithmetic discrepancies | [stated or "No discrepancy -- row N/A"] | [computed or "--"] |

Blank Prior State = structural violation.

After writing, write this required labeled field:

  Inertia (C-15): Two-column structure makes prior-state omission detectable by column scan.

**1d. BILATERAL SYMMETRY AUDIT SWEEP (Phase 1 exit)**

  | Comparison | Symmetric? |
  |------------|-----------|
  | N_aspirational | [YES -- Prior: [v], Current: [v] | NO -- [missing] | PARTIAL -- N/A declared] |
  | Regression verdicts | [YES | NO | PARTIAL] |
  | Arithmetic discrepancies | [YES | NO | PARTIAL] |

Verdict rules:
  - Symmetric: YES -- both Prior state and Current state present.
  - Symmetric: NO -- one or both sides missing; remediate before Phase 2.
  - Symmetric: PARTIAL -- N/A rule invoked correctly. Include a reason phrase on the same
    row explaining why this comparison received PARTIAL (see EVIDENCE QUALITY ADVISORY above
    for C-24 requirement).

After writing, write this required labeled field:

  Inertia (C-18): The SYMMETRIC DELTA REGISTER prevents asymmetric entries by column structure.
  This audit sweep catches them independently. Prevention and catch are both required.

PHASE 1 COMPLETE. Proceed to Phase 2 only after 1a, 1b, 1c, and 1d are written and the
bilateral audit shows no Symmetric: NO rows.

---

PHASE 2: SCORE EACH OUTPUT

**MODEL CELL (Phase 2 entry -- write before any verdict row)**

Write a model evidence cell as the first action of Phase 2, before any criterion-output row.

  Evidence (model): "from [output ID], [section or structural element]: [verbatim quote or
  structural observation that locates a specific feature in the output -- not a criterion
  restatement]"

  Include a locatability check: state whether a reader can find the referenced material using
  only this evidence text. Write YES if the evidence names a specific locatable section or
  quote; write NO if the evidence is a criterion restatement or the location is unnamed.
  (See EVIDENCE QUALITY ADVISORY above for C-23 requirement.)

After writing, write this required labeled field:

  Inertia (C-11, C-14): Without a model cell at Phase 2 entry, evidence cells default to
  criterion restatement. The model cell fires before the first verdict, establishing the
  evidence standard before any cell can set a lower norm.

ENTRY LOCK: do not write any verdict row until the model cell is written and passes the
locatability check. A verdict row written before the model cell is a Phase 2 protocol violation.

For each output, produce a scoring table:

  | ID | Criterion | Tier | Verdict | Evidence |

Column rules:
  - Verdict: PASS | PARTIAL | FAIL only.
  - Evidence: must quote, paraphrase with location, or name a specific structural feature.
    Criterion restatement is not evidence.
  - No row blank or missing. Include rows for all criteria C-01 through C-24.

After the scoring table, write the composite:

  essential_pass = [count; PARTIAL = 0.5]
  recommended_pass = [count; PARTIAL = 0.5]
  aspirational_pass = [count; PARTIAL = 0.5]
  composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 16 * 10) = [result]
  Golden: YES -- all essentials PASS; composite >= 80 | NO -- [which essential failed or composite < 80]

Score all N outputs before proceeding to Phase 3.

---

PHASE 3: VERIFY

**3a. Arithmetic verification**

  Verification (output: [ID]):
    stated counts: E=[X]/5, R=[X]/3, A=[X]/16
    computed composite: ([X]/5 * 60) + ([X]/3 * 30) + ([X]/16 * 10) = [result]
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

**LEADERBOARD**

  | Rank | Output | Composite | Golden? |

All N outputs ranked descending. Ties noted explicitly.

**EXCELLENCE SIGNALS**

Signal: [output ID] -- [criterion ID] -- [structural mechanism producing the difference]

If no outlier pair: state explicitly.

**FAILURE PATTERNS**

Required even when empty: "No failure patterns -- all criteria passed in at least one output."

**REGRESSION SIGNALS**

If prior data: named regressions. If no prior data: "No prior round data; regression analysis
not possible."

**PER-OUTPUT SYNTHESIS NOTES**

One paragraph per output on structural score drivers. Explain the mechanism, not the counts.

---

## V-04: Axes P+Q+R+U -- Entry Lock + Coverage Assertion + Non-Additivity Block + Locatability Assertion

**Variation axis**: Combination -- P (Phase 2 entry gate binary declaration), Q (criterion-ID
anchoring in inertia labels plus Phase 1 exit COVERAGE ASSERTION), R (NON-ADDITIVITY ANALYSIS
block in synthesis), and U (binary locatability assertion field in MODEL CELL). The R7 minimal-
sufficient-combination (P+Q+R) plus the new C-23 axis (U). The COVERAGE ASSERTION at 1e is
updated to include C-23 as DEFERRED (covered by MODEL CELL + LOCATABILITY ASSERTION at Phase 2
entry).

**Hypothesis**: P achieves C-19 PASS (ENTRY LOCK binary declaration). Q achieves C-20 PASS
(criterion-ID anchoring in every Inertia label) and C-21 PASS (COVERAGE ASSERTION at Phase 1
exit). R achieves C-22 PASS (three-field non-additivity schema). U achieves C-23 PASS (binary
locatability assertion field in MODEL CELL). C-24 PARTIAL predicted: bilateral audit remains a
two-column table (no Axis V) -- PARTIAL rows exist without a column-enforced reason schema.
C-24 coverage in 1e is DEFERRED because the current scope of 1e's inertia label covers C-20/C-21
but not C-24; C-24 would need to be surfaced via the synthesis notes or a specific evidence row.

---

You are running quest-score against the v8 rubric.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite score computed from
the rubric formula, and a golden-threshold determination. The final scorecard includes a
ranked leaderboard, excellence signals, failure patterns, regression signals, and
non-additivity analysis.

---

FORMULA CHANGE ALERT -- READ BEFORE ANY COMPUTATION

The v8 rubric changes the aspirational denominator from the v7 value.

  N_aspirational: 14 (v7) -> 16 (v8)

Composite formula (v8, active):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 16 * 10)

  PARTIAL counts as 0.5 toward pass count. FAIL counts as 0.
  Golden threshold: ALL 5 essentials PASS AND composite >= 80.

Do not compute any score using /14 or any prior denominator. If a conflict exists between
this prompt and a rubric file, the rubric file governs.

---

PHASE 1: LOAD, DELTA REGISTER, BILATERAL AUDIT, AND COVERAGE ASSERTION

Complete sections 1a through 1e in order. Do not proceed to Phase 2 until all five sections
are written, the bilateral audit shows no Symmetric: NO rows, and the coverage assertion
is complete.

**1a. Load summary**

Produce a block confirming the rubric was read. The block must name all four elements:
  (a) all criteria IDs with tier labels (C-01--C-05 essential, C-06--C-08 recommended,
      C-09--C-24 aspirational)
  (b) the exact composite formula text (v8 active: /16 aspirational denominator)
  (c) the golden threshold condition (all 5 essentials PASS AND composite >= 80)
  (d) the count and list of outputs being scored

After writing, write this required labeled field:

  Inertia (C-01): Without this load block, criteria count (24), formula denominator (/16),
  and threshold are unverified. A scorer who skips produces a matrix missing C-23 and C-24
  rows and composites using /14 -- both errors invisible until Phase 3.

**1b. Formula version delta**

  Formula version delta: N_aspirational changed from [prior value] to [current value] in v[N].
  Example: "N_aspirational changed from 14 (v7) to 16 (v8)."

If prior unknown: "No prior version delta detectable -- scoring under v8 as baseline."

After writing, write this required labeled field:

  Inertia (C-13, C-15): "N_aspirational=16" passes C-01 but fails C-15. Prior value (14) must
  be named. Both sides required to confirm the transition.

**1c. SYMMETRIC DELTA REGISTER**

  | Comparison type | Prior state | Current state |
  |-----------------|-------------|---------------|
  | N_aspirational (formula denominator) | [prior -- e.g., "14 (v7)"] | [current -- e.g., "16 (v8)"] |
  | Regression verdicts | [prior or "No prior-round data -- row N/A"] | [current or "--"] |
  | Arithmetic discrepancies | [stated or "No discrepancy -- row N/A"] | [computed or "--"] |

Blank Prior State = structural violation.

After writing, write this required labeled field:

  Inertia (C-15): Two-column structure makes prior-state omission a detectable gap by column
  scan. A scorer writing only "N_aspirational=16" produces a visible blank in Prior State.

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

After the bilateral audit, verify that every scored criterion ID (C-01 through C-24) will
appear in at least one Inertia label in this output. Produce the following assertion table:

  | Criterion | Covered? | Location |
  |-----------|----------|----------|
  | C-01 | YES | Inertia (C-01): at 1a |
  | C-13 | YES | Inertia (C-13, C-15): at 1b |
  | C-15 | YES | Inertia (C-15): at 1c; also 1b |
  | C-18 | YES | Inertia (C-18): at 1d |
  | C-20 | YES | Inertia (C-20, C-21): at 1e |
  | C-21 | YES | Inertia (C-20, C-21): at 1e |
  | C-11, C-14, C-19, C-23 | DEFERRED | Covered by MODEL CELL + ENTRY LOCK + LOCATABILITY ASSERTION at Phase 2 entry |
  | C-12 | DEFERRED | Covered by arithmetic verification block at 3a |
  | C-09 | DEFERRED | Covered by regression section at 3b |
  | C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-16, C-17, C-22, C-24 | DEFERRED | Covered by Phase 2 scoring and synthesis mechanisms |

For any criterion not appearing: add it to DEFERRED with intended coverage location. Criteria
absent from all rows is a coverage gap.

After writing, write this required labeled field:

  Inertia (C-20, C-21): Bare "Inertia: [text]" satisfies C-17 but fails C-20 -- no criterion
  ID. C-21 requires this phase-boundary assertion: total inertia-label coverage confirmable by
  reading one field, not by scanning every label.

PHASE 1 COMPLETE. Proceed to Phase 2 only after 1a, 1b, 1c, 1d, and 1e are written.

---

PHASE 2: SCORE EACH OUTPUT

**MODEL CELL + LOCATABILITY ASSERTION + ENTRY LOCK (Phase 2 entry -- write before any verdict row)**

Write the following four elements in sequence before any criterion-output evidence row.

(1) Evidence (model):
  "from [output ID], [section or structural element]: [verbatim quote or structural
  observation that locates a specific feature in the output -- not a criterion restatement]"

(2) Locatability assertion:
  Locatability test: [YES -- a reader can find [the quoted or referenced material] in
  [output ID] at [named section or structural location] without searching the full output |
  NO -- evidence is a criterion restatement or the referenced location cannot be found;
  rewrite evidence before proceeding to any verdict row]

  Rules:
  - Both fields are required. A missing Locatability test field earns C-23 FAIL.
  - Writing YES when the evidence text does not name a specific locatable section or quote
    earns C-23 FAIL -- the assertion must be accurate, not automatic.

(3) Required labeled field:

  Inertia (C-11, C-14, C-23): Without a model cell at Phase 2 entry, evidence cells default
  to criterion restatement. The locatability assertion extends the check: a model cell can
  pass C-11 and C-14 while its evidence is unlocatable -- C-23 fails if the test is omitted.
  The binary field makes locatability status scannable without re-reading the evidence text.

(4) Binary gate declaration:

  ENTRY LOCK: no verdict row written before model cell. [Confirmed | Violated -- first verdict
  row appears at: ___]

  Write "Confirmed" if the model cell (including locatability assertion) is the first Phase 2
  content written. The ENTRY LOCK field is required; omitting it earns C-19 FAIL.

For each output, produce a scoring table:

  | ID | Criterion | Tier | Verdict | Evidence |

Column rules:
  - Verdict: PASS | PARTIAL | FAIL only.
  - Evidence: must quote, paraphrase with location, or name a specific structural feature.
    Criterion restatement is not evidence.
  - Every Inertia label must use criterion-ID anchoring: "Inertia (C-XX): [failure mode]"
    -- not bare "Inertia: [failure mode]".
  - No row blank or missing. Include rows for all criteria C-01 through C-24.

After the scoring table, write the composite:

  essential_pass = [count; PARTIAL = 0.5]
  recommended_pass = [count; PARTIAL = 0.5]
  aspirational_pass = [count; PARTIAL = 0.5]
  composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 16 * 10) = [result]
  Golden: YES -- all essentials PASS; composite >= 80 | NO -- [which essential failed or composite < 80]

Score all N outputs before proceeding to Phase 3.

---

PHASE 3: VERIFY

**3a. Arithmetic verification**

  Verification (output: [ID]):
    stated counts: E=[X]/5, R=[X]/3, A=[X]/16
    computed composite: ([X]/5 * 60) + ([X]/3 * 30) + ([X]/16 * 10) = [result]
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

All three fields are required for each zero-increment pair. Zero-increment declaration without
the subsuming mechanism satisfies C-22 at PARTIAL only.

If no zero-increment pair: "No non-additivity observed -- all axes produced positive increment."
If single variation scored: "Single variation scored -- non-additivity analysis not applicable."

Required: this section must appear whether or not non-additivity is observed. Omitting earns
C-22 FAIL.

**REGRESSION SIGNALS**

If prior data: named regressions. If no prior data: "No prior round data; regression analysis
not possible."

**PER-OUTPUT SYNTHESIS NOTES**

One paragraph per output on structural score drivers. Explain the mechanism, not the counts.

---

## V-05: Axes P+Q+R+U+V -- Entry Lock + Coverage Assertion + Non-Additivity Block + Locatability Assertion + Partial-Reason Schema

**Variation axis**: Full combination -- P+Q+R+U from V-04 plus V (PARTIAL-REASON SCHEMA in
bilateral audit sweep). Tests whether V is additive given U, or whether U's locatability
mechanism and V's reason-labeling mechanism subsume each other.

**Hypothesis**: U targets C-23 (locatability of model cell evidence at Phase 2 entry). V targets
C-24 (reason labeling of PARTIAL rows in Phase 1 bilateral audit). These are structurally
independent -- different lifecycle phases, different failure modes, different structural locations.
Neither axis's mechanism performs the other's function. V is additive given U: V-05 > V-04 by
C-24 moving from PARTIAL to PASS (+0.3125 composite). If the prediction holds, both U and V are
required in the R8 champion combination, and R8's non-additivity finding will be W is subsumed by
U+V: W's instructions achieve PARTIAL on both criteria; U achieves PASS on C-23 and V achieves
PASS on C-24; neither can be replaced by W's advisory text alone.

---

You are running quest-score against the v8 rubric.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite score computed from
the rubric formula, and a golden-threshold determination. The final scorecard includes a
ranked leaderboard, excellence signals, failure patterns, regression signals, and
non-additivity analysis.

---

FORMULA CHANGE ALERT -- READ BEFORE ANY COMPUTATION

The v8 rubric changes the aspirational denominator from the v7 value.

  N_aspirational: 14 (v7) -> 16 (v8)

Composite formula (v8, active):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 16 * 10)

  PARTIAL counts as 0.5 toward pass count. FAIL counts as 0.
  Golden threshold: ALL 5 essentials PASS AND composite >= 80.

Do not compute any score using /14 or any prior denominator. If a conflict exists between
this prompt and a rubric file, the rubric file governs.

---

PHASE 1: LOAD, DELTA REGISTER, BILATERAL AUDIT, AND COVERAGE ASSERTION

Complete sections 1a through 1e in order. Do not proceed to Phase 2 until all five sections
are written, the bilateral audit shows no Symmetric: NO rows and no blank PARTIAL Reason cells,
and the coverage assertion is complete.

**1a. Load summary**

Produce a block confirming the rubric was read. The block must name all four elements:
  (a) all criteria IDs with tier labels (C-01--C-05 essential, C-06--C-08 recommended,
      C-09--C-24 aspirational)
  (b) the exact composite formula text (v8 active: /16 aspirational denominator)
  (c) the golden threshold condition (all 5 essentials PASS AND composite >= 80)
  (d) the count and list of outputs being scored

After writing, write this required labeled field:

  Inertia (C-01): Without this load block, criteria count (24), formula denominator (/16),
  and threshold are unverified. A scorer who skips produces a matrix missing C-23 and C-24
  rows and composites using /14 -- both errors invisible until Phase 3.

**1b. Formula version delta**

  Formula version delta: N_aspirational changed from [prior value] to [current value] in v[N].
  Example: "N_aspirational changed from 14 (v7) to 16 (v8)."

If prior unknown: "No prior version delta detectable -- scoring under v8 as baseline."

After writing, write this required labeled field:

  Inertia (C-13, C-15): "N_aspirational=16" passes C-01 but fails C-15. Prior value (14) must
  be named. Both sides required to confirm the transition.

**1c. SYMMETRIC DELTA REGISTER**

  | Comparison type | Prior state | Current state |
  |-----------------|-------------|---------------|
  | N_aspirational (formula denominator) | [prior -- e.g., "14 (v7)"] | [current -- e.g., "16 (v8)"] |
  | Regression verdicts | [prior or "No prior-round data -- row N/A"] | [current or "--"] |
  | Arithmetic discrepancies | [stated or "No discrepancy -- row N/A"] | [computed or "--"] |

Blank Prior State = structural violation.

After writing, write this required labeled field:

  Inertia (C-15): Two-column structure makes prior-state omission detectable by column scan.

**1d. BILATERAL SYMMETRY AUDIT SWEEP (Phase 1 exit)**

  | Comparison | Symmetric? | Reason (if PARTIAL) |
  |------------|-----------|---------------------|
  | N_aspirational | [YES -- Prior: [v], Current: [v] | NO -- [missing] | PARTIAL -- N/A] | [reason or "--"] |
  | Regression verdicts | [YES | NO -- [missing] | PARTIAL] | [reason or "--"] |
  | Arithmetic discrepancies | [YES | NO -- [missing] | PARTIAL] | [reason or "--"] |

Verdict rules:
  - Symmetric: YES -- both Prior and Current state present. Reason column: "--".
  - Symmetric: NO -- one or both sides missing; remediate before Phase 2. Reason column: "--".
  - Symmetric: PARTIAL -- N/A rule invoked correctly. The Reason column is REQUIRED for
    PARTIAL rows. Write "PARTIAL -- [reason phrase]":
      e.g., "PARTIAL -- no prior-round data; N/A rule applied correctly"
      e.g., "PARTIAL -- no discrepancy found; N/A rule applied correctly"
  - A PARTIAL row with a blank Reason cell is a structural violation. Treat it as requiring
    remediation before Phase 2, same as Symmetric: NO.

After writing, write this required labeled field:

  Inertia (C-18, C-24): Register prevents asymmetric entries by column structure. Sweep catches
  them independently. The Reason column prevents a second class of ambiguity: bare PARTIAL is
  indistinguishable between correctly-applied N/A rule, clean result, and silently-skipped
  comparison. Reason phrases make each PARTIAL as auditable as its YES/NO verdicts.

**1e. CRITERION-INERTIA COVERAGE ASSERTION**

After the bilateral audit, verify that every scored criterion ID (C-01 through C-24) will
appear in at least one Inertia label in this output. Produce the following assertion table:

  | Criterion | Covered? | Location |
  |-----------|----------|----------|
  | C-01 | YES | Inertia (C-01): at 1a |
  | C-13 | YES | Inertia (C-13, C-15): at 1b |
  | C-15 | YES | Inertia (C-15): at 1c; also 1b |
  | C-18 | YES | Inertia (C-18, C-24): at 1d |
  | C-24 | YES | Inertia (C-18, C-24): at 1d |
  | C-20 | YES | Inertia (C-20, C-21): at 1e |
  | C-21 | YES | Inertia (C-20, C-21): at 1e |
  | C-11, C-14, C-19, C-23 | DEFERRED | Covered by MODEL CELL + ENTRY LOCK + LOCATABILITY ASSERTION at Phase 2 entry |
  | C-12 | DEFERRED | Covered by arithmetic verification block at 3a |
  | C-09 | DEFERRED | Covered by regression section at 3b |
  | C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-16, C-17, C-22 | DEFERRED | Covered by Phase 2 scoring and synthesis mechanisms |

For any criterion not appearing: add it to DEFERRED with intended coverage location. Criteria
absent from all rows is a coverage gap.

After writing, write this required labeled field:

  Inertia (C-20, C-21): Bare "Inertia: [text]" satisfies C-17 but fails C-20. C-21 requires
  this phase-boundary assertion: total inertia-label coverage confirmable by reading one field,
  not by scanning every label.

PHASE 1 COMPLETE. Proceed to Phase 2 only after 1a, 1b, 1c, 1d, and 1e are written, the
bilateral audit shows no Symmetric: NO rows, and no PARTIAL row has a blank Reason cell.

---

PHASE 2: SCORE EACH OUTPUT

**MODEL CELL + LOCATABILITY ASSERTION + ENTRY LOCK (Phase 2 entry -- write before any verdict row)**

Write the following four elements in sequence before any criterion-output evidence row.

(1) Evidence (model):
  "from [output ID], [section or structural element]: [verbatim quote or structural
  observation that locates a specific feature in the output -- not a criterion restatement]"

(2) Locatability assertion:
  Locatability test: [YES -- a reader can find [the quoted or referenced material] in
  [output ID] at [named section or structural location] without searching the full output |
  NO -- evidence is a criterion restatement or the referenced location cannot be found;
  rewrite evidence before proceeding to any verdict row]

  Rules:
  - Both fields are required. A missing Locatability test field earns C-23 FAIL.
  - Writing YES when the evidence text does not name a specific locatable section or quote
    earns C-23 FAIL -- the assertion must be accurate, not automatic.
  - A NO declaration requires rewriting the evidence before Phase 2 proceeds.

(3) Required labeled field:

  Inertia (C-11, C-14, C-23): Without a model cell at Phase 2 entry, evidence cells default
  to criterion restatement. The locatability assertion extends the check: a model cell can pass
  C-11 and C-14 while its evidence is unlocatable -- C-23 fails if the test is omitted. The
  binary field makes locatability status scannable without re-reading the evidence text.

(4) Binary gate declaration:

  ENTRY LOCK: no verdict row written before model cell. [Confirmed | Violated -- first verdict
  row appears at: ___]

  Write "Confirmed" if the model cell (including locatability assertion) is the first Phase 2
  content written. Write "Violated -- first verdict row at: [location]" if any verdict row
  preceded. The ENTRY LOCK field is required; omitting it earns C-19 FAIL.

For each output, produce a scoring table:

  | ID | Criterion | Tier | Verdict | Evidence |

Column rules:
  - Verdict: PASS | PARTIAL | FAIL only.
  - Evidence: must quote, paraphrase with location, or name a specific structural feature.
    Criterion restatement is not evidence.
  - Every Inertia label must use criterion-ID anchoring: "Inertia (C-XX): [failure mode]"
    -- not bare "Inertia: [failure mode]".
  - No row blank or missing. Include rows for all criteria C-01 through C-24.

After the scoring table, write the composite:

  essential_pass = [count; PARTIAL = 0.5]
  recommended_pass = [count; PARTIAL = 0.5]
  aspirational_pass = [count; PARTIAL = 0.5]
  composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 16 * 10) = [result]
  Golden: YES -- all essentials PASS; composite >= 80 | NO -- [which essential failed or composite < 80]

Score all N outputs before proceeding to Phase 3.

---

PHASE 3: VERIFY

**3a. Arithmetic verification**

  Verification (output: [ID]):
    stated counts: E=[X]/5, R=[X]/3, A=[X]/16
    computed composite: ([X]/5 * 60) + ([X]/3 * 30) + ([X]/16 * 10) = [result]
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

All three fields are required for each zero-increment pair. Zero-increment declaration without
the subsuming mechanism satisfies C-22 at PARTIAL only.

If no zero-increment pair: "No non-additivity observed -- all axes produced positive increment."
If single variation scored: "Single variation scored -- non-additivity analysis not applicable."

Required: this section must appear whether or not non-additivity is observed.

**REGRESSION SIGNALS**

If prior data: named regressions. If no prior data: "No prior round data; regression analysis
not possible."

**PER-OUTPUT SYNTHESIS NOTES**

One paragraph per output on structural score drivers. Explain the mechanism, not the counts.
