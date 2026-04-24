# quest-score Variations -- Round 5 (v5 rubric, actual C-17/C-18)

**Skill**: quest-score
**Rubric**: v5-2026-03-16 (C-01--C-05 essential, C-06--C-08 recommended, C-09--C-18 aspirational)
**N_essential=5, N_recommended=3, N_aspirational=10**
**Date**: 2026-03-16
**Round**: 5

---

## Context: what informed this round

Round 4 targeted the v4 rubric. The R4 champion (V-05) carried axes D+E+F+G+H+J+K+M:

| Axis | Mechanism | Phase | Criterion target |
|------|-----------|-------|-----------------|
| D | MODEL CELL advisory -- positive evidence anchor at Phase 2 entry | Phase 2 | C-11, C-14 |
| E | YES/NO labeled declaration field for arithmetic verification | Phase 3 | C-12 |
| F | FORMULA CHANGE ALERT at prompt load | Pre-Phase 1 | C-13 (prompt side) |
| G | Formula version delta block in scorer output -- prior AND current named | Phase 1 | C-13 (output side) |
| H | Phase 2 entry lock -- gates first evidence row on model cell | Phase 2 | C-14 |
| J | SYMMETRIC DELTA REGISTER -- two-column table (Prior state / Current state) | Phase 1 | C-15 |
| K | PHASE MECHANISM INVENTORY -- pre-Phase-1 declaration of mechanisms by phase | Pre-Phase 1 | C-16 |
| M | Inertia framing -- "*Departure from inertia*" labels at each mechanism | All phases | C-03, C-16 |

R4 ceiling: V-05 reached ~98-100 on the v4 rubric. C-17 and C-18 were not in the v4 rubric.

v5 adds two new Aspirational criteria extracted from R4 signals:

| Change | R4 (v4) | R5 (v5) | Design consequence |
|--------|---------|---------|-------------------|
| C-17 (inertia departure labeling) | Not in rubric | Each structural enforcement mechanism must carry a labeled statement of the failure mode it prevents -- "Inertia:" label, "without this mechanism:" clause, or concrete negative example | R4's Axis M placed "*Departure from inertia*" labels in the PROMPT. C-17 requires these labels in the SCORER'S OUTPUT. The variation must instruct scorers to write "Inertia: [failure mode]" as a required output field at each mechanism. |
| C-18 (bilateral symmetry audit sweep) | Not in rubric | Post-write bilateral audit sweep at Phase 1 exit or Phase 3 exit, producing per-comparison Symmetric: YES/NO verdicts | R4's Axis L (V-03 only, not in V-05 champion) had a symmetry check but not the formal Symmetric: YES/NO format. C-18 requires a structured sweep table with binary per-comparison verdicts, independent of J's prevention mechanism. |
| N_aspirational | 8 (C-09--C-16) | 10 (C-09--C-18) | Formula denominator: aspirational_pass / 8 -> aspirational_pass / 10 |

**What R5 variations must achieve beyond the R4 base:**

1. **C-17 PASS**: The scorer's output must contain labeled departure statements for each structural enforcement mechanism it deploys. "Inertia: [failure mode]" must appear as a required output field, not optional annotation.

2. **C-18 PASS**: The scorer's output must include a bilateral audit sweep at Phase 1 exit or Phase 3 exit with a per-comparison Symmetric: YES/NO verdict. This is distinct from J's prevention (filling the register) -- C-18 is the independent catch mechanism.

3. **N_aspirational update**: FORMULA CHANGE ALERT declares N_aspirational: 8 (v4) -> 10 (v5). All computations use /10.

**Variation axes explored this round:**

| Code | Axis | Target criterion | Hypothesis |
|------|------|-----------------|-----------|
| N | STANDARDIZED INERTIA LABELS -- each mechanism instruction requires the scorer to write "Inertia: [failure mode]" as a required output field | C-17 | Making "Inertia: [failure mode]" a required output field at each mechanism (not optional prose) ensures C-17 compliance structurally. The scorer cannot skip the field without a visible omission. |
| O | BILATERAL SYMMETRY AUDIT SWEEP -- Symmetric: YES/NO table at Phase 1 exit for each comparison in the DELTA REGISTER | C-18 | A post-register sweep with per-row Symmetric: YES/NO provides an independent catch mechanism. Analogous to E (YES/NO for arithmetic): the sweep detects asymmetry regardless of whether J's prevention succeeded. |
| K+N | MECHANISM INDEX WITH DEPARTURE LABELS -- pre-Phase-1 table declaring mechanism, phase, criterion, and inertia failure; each field reproduced at execution | C-16, C-17 | Moving departure label planning to a pre-execution table converts C-17 from per-mechanism compliance burden to a planning artifact declared before any phase begins. |

Single-axis: V-01 (N), V-02 (O).
Minimum combination: V-03 (N+O -- both C-17 and C-18 targets, no mechanism index).
Combined: V-04 (K+N -- mechanism index with departure labels, no sweep), V-05 (N+O+K -- full integration).

**Predicted outcomes:**

| Criterion | V-01 (N) | V-02 (O) | V-03 (N+O) | V-04 (K+N) | V-05 (N+O+K) |
|-----------|----------|----------|-----------|-----------|-------------|
| C-15 | PASS | PASS | PASS | PASS | PASS |
| C-16 | PASS | PASS | PASS | PASS | PASS |
| C-17 | PASS | PARTIAL | PASS | PASS | PASS |
| C-18 | FAIL | PASS | PASS | FAIL | PASS |

Note on V-02/C-17: R4 V-05 base carries M-axis informal departure labels ("*Departure from inertia*"). V-02 inherits these -- C-17 PARTIAL expected because M-style labels are present but not standardized as required "Inertia:" fields. V-01 upgrades M to N, producing C-17 PASS.

---

## V-01: Axis N -- Standardized Inertia Departure Labels

**Variation axis**: Phrasing register -- each mechanism instruction requires the scorer to
write "Inertia: [failure mode]" as a labeled required field in their output.

**Hypothesis**: R4's M axis placed informal "*Departure from inertia*" labels in the prompt
to motivate mechanisms. C-17 requires departure labels in the SCORER'S OUTPUT. V-01 bridges
this by requiring the scorer to write "Inertia: [specific failure mode]" immediately after
completing each mechanism. The label is a required output field -- not optional annotation --
so C-17 compliance is structural. The bilateral audit sweep (C-18) is absent. V-01 establishes
the C-17 PASS / C-18 FAIL baseline.

---

You are running quest-score against the v5 rubric.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite score computed from the
rubric formula, and a golden-threshold determination. The final scorecard includes a ranked
leaderboard, excellence signals, failure patterns, and regression signals.

---

FORMULA CHANGE ALERT -- READ BEFORE ANY COMPUTATION

The v5 rubric changes the aspirational denominator from the v4 value.

  N_aspirational: 8 (v4) -> 10 (v5)

Composite formula (v5, active):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 10 * 10)

  PARTIAL counts as 0.5 toward pass count. FAIL counts as 0.
  Golden threshold: ALL 5 essentials PASS AND composite >= 80.

Do not compute any score using aspirational_pass / 8. Any computation using the v4
denominator is an error. If a conflict exists between this prompt and a rubric file,
the rubric file governs.

---

PHASE 1: LOAD AND DELTA REGISTER

Before scoring any output, complete the following in order. Do not proceed to Phase 2 until
all three sections are written.

**1a. Load summary**

Produce a block confirming the rubric was read. The block must name all four elements:
  (a) all criteria IDs with tier labels (C-01--C-05 essential, C-06--C-08 recommended,
      C-09--C-18 aspirational)
  (b) the exact composite formula text (as written above)
  (c) the golden threshold condition (all 5 essentials PASS AND composite >= 80)
  (d) the count and list of outputs being scored

A load summary missing any one of (a)--(d) earns PARTIAL on C-01. Missing entirely earns FAIL.

After writing the load summary, write this required labeled field:

  Inertia (C-01): Without this load block, criteria count, formula denominator, and golden
  threshold are unverified before any verdict is written. Errors in C-02 (wrong criteria
  count) and C-04 (wrong denominator in composite calculation) remain invisible until Phase 3.

**1b. Formula version delta**

Write in your scoring output (visible to the reader, not only internally):

  Formula version delta: N_aspirational changed from [prior value] to [current value] in v[N].

If the prior version cannot be determined:
  "No prior version delta detectable -- scoring under v5 as the baseline version."

After writing the formula version delta, write this required labeled field:

  Inertia (C-13, C-15): "N_aspirational=10" in the output confirms the current value was
  loaded but does not confirm the prior value (8) was registered as distinct. C-15 requires
  both sides of every delta comparison. A current-only statement fails C-15 even when C-01
  (correct formula loaded) is PASS.

**1c. SYMMETRIC DELTA REGISTER**

Produce the following table. Fill every cell before proceeding to Phase 2.

  | Comparison type | Prior state | Current state |
  |-----------------|-------------|---------------|
  | N_aspirational (formula denominator) | [value from prior rubric version] | [value in v5] |
  | Regression verdicts | [prior verdict for each regressed pair, or "No prior-round data -- row N/A"] | [current verdict, or "--"] |
  | Arithmetic discrepancies | [stated score if discrepancy found, or "No discrepancy -- row N/A"] | [computed score, or "--"] |

Rules:
  - A blank Prior State cell is a structural violation. Write the value or write
    "N/A -- [reason]" to trigger the N/A rule.
  - A blank Current State cell is also a structural violation.
  - If no applicable comparison exists for a row, write "No prior-state value available
    in this scoring context" in Prior State.
  - The register must contain at least the N_aspirational row.

After writing the register, write this required labeled field:

  Inertia (C-15): Without the two-column table, symmetric comparison completeness depends on
  the scorer remembering to write both sides for each delta type. A scorer who writes
  "N_aspirational=10" correctly never names the prior value (8). The column structure makes
  a one-sided entry a visible structural gap -- a blank Prior State cell is detectable by
  column scan without reading cell content.

PHASE 1 COMPLETE -- proceed to Phase 2 only after 1a, 1b, and 1c are written.

---

PHASE 2: SCORE EACH OUTPUT

**MODEL CELL INSTRUCTION (fire at Phase 2 entry -- before any evidence row is written)**

Write as the first action of Phase 2, before any verdict row:

  Evidence (model): "from [output ID], [section or structural element]: [verbatim quote or
  structural observation that locates a specific feature in the output -- not a restatement
  of the criterion]"

  Locatability test: could a reader find the referenced feature using only this evidence text?
  YES: proceed. NO: rewrite before entering the cell.

After writing the model cell, write this required labeled field:

  Inertia (C-11, C-14): Without a model cell at Phase 2 entry, evidence cells default to
  criterion restatement -- "the output has a leaderboard", "evidence exists for each verdict"
  -- content that cannot locate any specific feature. The model cell fires before the first
  verdict, establishing the evidence standard before any cell can establish a lower norm.
  A model cell deferred to mid-Phase-2 fires after cells may already contain restatement.

ENTRY LOCK: do not write any verdict row until the model cell is written and passes the test.
A verdict written before the model cell is a Phase 2 protocol violation.

For each output, produce a scoring table:

  | ID | Criterion | Tier | Verdict | Evidence |
  |----|-----------|------|---------|----------|

Column rules:
  - Verdict: PASS | PARTIAL | FAIL only.
  - Evidence: must quote, paraphrase with location, or name a specific structural feature
    of the scored output. Criterion restatement is not evidence.
  - No row may be blank or missing.

After the table, write the composite:

  essential_pass = [count; PARTIAL = 0.5]
  recommended_pass = [count; PARTIAL = 0.5]
  aspirational_pass = [count; PARTIAL = 0.5]
  composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 10 * 10) = [result]
  Golden: YES -- all essentials PASS; composite >= 80 | NO -- [which essential failed or composite < 80]

Score all N outputs. Then proceed to Phase 3.

---

PHASE 3: VERIFY

**3a. Arithmetic verification**

Pick one output. Recompute its composite from the stated verdict counts and formula.

  Verification (output: [ID]):
    stated counts: E=[X]/5, R=[X]/3, A=[X]/10
    computed composite: ([X]/5 * 60) + ([X]/3 * 30) + ([X]/10 * 10) = [result]
    Matches stated score: YES | NO -- discrepancy: stated [X], computed [Y]

After writing the verification, write this required labeled field:

  Inertia (C-12): "Verification performed" satisfies C-10 at PARTIAL but does not produce
  a binary result. "The composite checks out" is indistinguishable from a silent pass-through
  that never ran the computation. The YES/NO field forces an explicit affirmation or names
  the exact discrepancy, making errors visible even when the scorer is not looking for them.

The "Matches stated score:" field is required. Narrative equivalents do not satisfy C-12.

If a discrepancy is found, update the SYMMETRIC DELTA REGISTER Arithmetic Discrepancy row.

**3b. Regression section**

If a prior-round scorecard was provided:
  - Name any criterion-output pair that degraded from PASS (or PARTIAL) to a lower verdict.
  - Format: "[Output ID] / [Criterion ID]: prior=[verdict], current=[verdict]"
  - Both verdicts required. Update SYMMETRIC DELTA REGISTER Regression row.

If no prior-round file was provided:
  "No prior round data -- regression analysis cannot be performed."

After writing the regression section, write this required labeled field:

  Inertia (C-09): An absent regression section is structurally indistinguishable from a
  section with no regressions. The user cannot determine whether regressions were checked
  or skipped. The section is required even when empty -- its presence confirms the check.

Do not omit this section. An absent regression section earns C-09 FAIL.

---

SYNTHESIS

Write the following sections in order.

**LEADERBOARD**

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

All N outputs ranked descending. Ties noted explicitly. "See scores above" does not
satisfy C-06 -- the leaderboard must be a standalone sorted structure.

**EXCELLENCE SIGNALS**

For each criterion where one output clearly outperforms others:
  Signal: [output ID] -- [criterion ID] -- [structural mechanism that produced the difference]

"V-05 scored highest overall" is not an excellence signal. Requires output-criterion pair
and structural explanation.

If no spread: "No score spread found. All-pass rounds confirm stability but do not advance
plateau detection. Consider redesigning variations for divergence."

**FAILURE PATTERNS**

  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

Required even when empty: "No failure patterns -- all criteria passed in at least one output."

**PER-OUTPUT SYNTHESIS NOTES**

One paragraph per output on structural score drivers. Do not list verdict counts -- explain
the mechanism.

---

## V-02: Axis O -- Bilateral Symmetry Audit Sweep

**Variation axis**: Output format -- BILATERAL AUDIT SWEEP table at Phase 1 exit producing
a per-comparison Symmetric: YES/NO verdict for each row in the SYMMETRIC DELTA REGISTER.

**Hypothesis**: J's SYMMETRIC DELTA REGISTER prevents asymmetric comparisons by requiring
both columns. C-18 requires an independent catch mechanism that detects asymmetry AFTER
prevention -- analogous to how E's YES/NO declaration independently checks arithmetic
beyond the scorer's computation. The bilateral sweep fires at Phase 1 exit; a Symmetric: NO
cell is detectable by scanning the sweep without reading the underlying register prose. C-17
(departure labels) is not explicitly upgraded from M -- V-02 establishes the C-18 PASS /
C-17-as-inherited baseline.

---

You are running quest-score against the v5 rubric.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite score computed from the
rubric formula, and a golden-threshold determination. The final scorecard includes a ranked
leaderboard, excellence signals, failure patterns, and regression signals.

---

FORMULA CHANGE ALERT -- READ BEFORE ANY COMPUTATION

The v5 rubric changes the aspirational denominator from the v4 value.

  N_aspirational: 8 (v4) -> 10 (v5)

Composite formula (v5, active):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 10 * 10)

  PARTIAL counts as 0.5 toward pass count. FAIL counts as 0.
  Golden threshold: ALL 5 essentials PASS AND composite >= 80.

Do not compute any score using aspirational_pass / 8. If a conflict exists between this
prompt and a rubric file, the rubric file governs.

---

PHASE 1: LOAD, DELTA REGISTER, AND BILATERAL AUDIT

Before scoring any output, complete sections 1a through 1d in order. Do not proceed to
Phase 2 until all four sections are written and the bilateral audit shows no Symmetric: NO rows.

**1a. Load summary**

  (a) all criteria IDs with tier labels (C-01--C-05 essential, C-06--C-08 recommended,
      C-09--C-18 aspirational)
  (b) exact composite formula text
  (c) golden threshold: all 5 essentials PASS AND composite >= 80
  (d) count and list of outputs being scored

A load summary missing any one of (a)--(d) earns PARTIAL on C-01. Missing entirely earns FAIL.

**1b. Formula version delta**

Write in your output:
  Formula version delta: N_aspirational changed from [prior value] to [current value] in v[N].

If prior version cannot be determined:
  "No prior version delta detectable -- scoring under v5 as the baseline version."

**1c. SYMMETRIC DELTA REGISTER**

  | Comparison type | Prior state | Current state |
  |-----------------|-------------|---------------|
  | N_aspirational (formula denominator) | [prior value] | [current value] |
  | Regression verdicts | [prior verdict or "No prior-round data -- row N/A"] | [current verdict or "--"] |
  | Arithmetic discrepancies | [stated score if found, or "No discrepancy -- row N/A"] | [computed score or "--"] |

Rules: blank Prior State cell = structural violation. Write value or "N/A -- [reason]".

*Departure from inertia (C-15): Without the two-column table, a scorer writes "N_aspirational=10"
with no visible Prior State column. The column structure makes a one-sided entry structurally
detectable by column scan.*

**1d. BILATERAL SYMMETRY AUDIT SWEEP (Phase 1 exit)**

After completing the register, produce this sweep. Phase 2 does not begin until this sweep
is written and all rows show Symmetric: YES or PARTIAL.

  | Comparison | Symmetric? |
  |------------|-----------|
  | N_aspirational (formula denominator) | [YES -- Prior: [value], Current: [value] | NO -- [which side missing] | PARTIAL -- N/A declared] |
  | Regression verdicts | [YES | NO -- [missing side] | PARTIAL -- no prior data] |
  | Arithmetic discrepancies | [YES | NO -- [missing side] | PARTIAL -- no discrepancy found] |

Verdict rules:
  - Symmetric: YES -- both Prior state and Current state present in register row.
  - Symmetric: NO -- one or both sides missing. Remediate before Phase 2: fill the missing
    cell or write "N/A -- [reason]" to convert NO to PARTIAL.
  - Symmetric: PARTIAL -- N/A rule invoked (no prior data, or no discrepancy found).
    This is the correct outcome when a comparison is not applicable -- not a failure.

AUDIT SWEEP WRITTEN -- Phase 2 may begin.

---

PHASE 2: SCORE EACH OUTPUT

**MODEL CELL INSTRUCTION (fire at Phase 2 entry -- before any evidence row is written)**

  Evidence (model): "from [output ID], [section]: [verbatim quote or structural observation
  that locates a specific feature in the output -- not a criterion restatement]"

  Locatability test: YES = proceed. NO = rewrite before entering the cell.

*Departure from inertia (C-11, C-14): Without a model cell before any verdict, evidence cells
default to criterion restatement. The model cell fires before the first verdict, establishing
the evidence standard before any cell can establish a lower norm.*

ENTRY LOCK: no verdict row before model cell. A verdict before the model cell is a protocol
violation.

For each output:

  | ID | Criterion | Tier | Verdict | Evidence |
  |----|-----------|------|---------|----------|

Evidence: must quote, paraphrase with location, or name a specific structural feature.
Criterion restatement is not evidence.

Composite:
  essential_pass = [count; PARTIAL = 0.5]
  recommended_pass = [count; PARTIAL = 0.5]
  aspirational_pass = [count; PARTIAL = 0.5]
  composite = (E/5 * 60) + (R/3 * 30) + (A/10 * 10) = [result]
  Golden: YES -- all essentials PASS; composite >= 80 | NO -- [failing condition]

Score all N outputs.

---

PHASE 3: VERIFY

**3a. Arithmetic verification**

  Verification (output: [ID]):
    stated counts: E=[X]/5, R=[X]/3, A=[X]/10
    computed: ([X]/5*60) + ([X]/3*30) + ([X]/10*10) = [result]
    Matches stated score: YES | NO -- discrepancy: stated [X], computed [Y]

*Departure from inertia (C-12): "Verification performed" satisfies C-10 at PARTIAL but not
C-12. The YES/NO field forces an explicit affirmation or names the exact discrepancy.*

If discrepancy found, update SYMMETRIC DELTA REGISTER Arithmetic row and re-run the
BILATERAL AUDIT SWEEP for that comparison.

**3b. Regression section**

If prior data provided: "[Output ID] / [Criterion ID]: prior=[verdict], current=[verdict]"
  Update SYMMETRIC DELTA REGISTER Regression row.
If no prior data: "No prior round data -- regression analysis cannot be performed."

*Departure from inertia (C-09): An absent section is indistinguishable from no regressions.
Required even when empty.*

---

SYNTHESIS

**LEADERBOARD**: all outputs ranked descending. Standalone structure. Ties noted explicitly.

**EXCELLENCE SIGNALS**: output-criterion-mechanism triples. Generic observations not accepted.
If none: "No score spread found."

**FAILURE PATTERNS**: criteria with no PASS across all outputs. Required even when empty.

**PER-OUTPUT SYNTHESIS NOTES**: structural explanation per output. Not verdict counts.

---

## V-03: Axes N+O -- Departure Labels + Bilateral Sweep (Minimum Combination)

**Variation axis**: Combined -- standardized per-mechanism "Inertia:" required fields (N)
+ bilateral symmetry audit sweep at Phase 1 exit with Symmetric: YES/NO (O). No pre-Phase-1
mechanism index.

**Hypothesis**: V-01 addresses C-17 but not C-18. V-02 addresses C-18 but not C-17. V-03
is the minimum combination targeting both simultaneously without the overhead of a
mechanism index. If V-03 reaches the same ceiling as V-05, the mechanism index is
non-additive given N+O and should not be included in the golden prompt.

---

You are running quest-score against the v5 rubric.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite score computed from the
rubric formula, and a golden-threshold determination. The final scorecard includes a ranked
leaderboard, excellence signals, failure patterns, and regression signals.

---

FORMULA CHANGE ALERT -- READ BEFORE ANY COMPUTATION

  N_aspirational: 8 (v4) -> 10 (v5)

Composite formula (v5):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 10 * 10)

  PARTIAL = 0.5. FAIL = 0. Golden threshold: ALL 5 essentials PASS AND composite >= 80.

Do not compute using aspirational_pass / 8. Rubric file governs conflicts.

---

PHASE 1: LOAD, DELTA REGISTER, AND BILATERAL AUDIT

**1a. Load summary**

  (a) all criteria IDs with tier labels (C-01--C-05 essential, C-06--C-08 recommended,
      C-09--C-18 aspirational)
  (b) exact composite formula
  (c) golden threshold
  (d) count and list of outputs

  Required field after writing:
  Inertia (C-01): Criteria count, formula denominator, and threshold unverified without this
  block. Errors in C-02/C-04 invisible until Phase 3. The load block makes inputs explicit
  before any verdict is written.

**1b. Formula version delta**

  Formula version delta: N_aspirational changed from [prior] to [current] in v[N].

  Required field after writing:
  Inertia (C-13, C-15): A current-only statement ("N_aspirational=10") confirms the endpoint
  was loaded but does not confirm the prior value (8) was registered as distinct. Both sides
  required: "8 (v4) -> 10 (v5)".

**1c. SYMMETRIC DELTA REGISTER**

  | Comparison type | Prior state | Current state |
  |-----------------|-------------|---------------|
  | N_aspirational | [prior value] | [current value] |
  | Regression verdicts | [prior or "No prior-round data -- row N/A"] | [current or "--"] |
  | Arithmetic discrepancies | [stated if found, or "No discrepancy -- row N/A"] | [computed or "--"] |

  Required field after writing:
  Inertia (C-15): Without the two-column structure, one-sided comparisons have no visible
  structural gap. The column makes a blank Prior State detectable by column scan.

**1d. BILATERAL SYMMETRY AUDIT SWEEP (Phase 1 exit)**

  | Comparison | Symmetric? |
  |------------|-----------|
  | N_aspirational | [YES -- Prior: [v], Current: [v] | NO -- [missing side] | PARTIAL -- N/A] |
  | Regression verdicts | [YES | NO | PARTIAL -- no prior data] |
  | Arithmetic discrepancies | [YES | NO | PARTIAL -- not found] |

  Symmetric: NO requires remediation before Phase 2.
  Symmetric: PARTIAL -- N/A rule invoked, acceptable.

  Required field after writing:
  Inertia (C-18): J's DELTA REGISTER prevents asymmetric entries by requiring both columns.
  The AUDIT SWEEP catches asymmetric entries independently -- a Symmetric: NO cell is
  visible by scanning the sweep without reading the register prose. C-15 compliance through
  prevention only has no independent catch mechanism; C-18 requires the sweep to exist.

  AUDIT SWEEP WRITTEN. Phase 2 may begin.

---

PHASE 2: SCORE EACH OUTPUT

**MODEL CELL (Phase 2 entry -- before any verdict row)**

  Evidence (model): "from [output ID], [section]: [structural observation locating a specific
  feature -- not a criterion restatement]"

  Locatability test: YES = proceed. NO = rewrite.

  Required field after writing:
  Inertia (C-11, C-14): Without a model cell before any verdict, evidence defaults to
  criterion restatement. The model cell fires before the first verdict establishes a norm.
  A model cell deferred to mid-Phase-2 fires after the restatement pattern is established.

  ENTRY LOCK: no verdict row before model cell.

For each output:

  | ID | Criterion | Tier | Verdict | Evidence |
  |----|-----------|------|---------|----------|

Composite after each output table:
  E=[n]/5, R=[n]/3, A=[n]/10
  composite = (E/5*60) + (R/3*30) + (A/10*10) = [result]
  Golden: YES | NO -- [reason if NO]

---

PHASE 3: VERIFY

**3a. Arithmetic verification**

  Verification ([output ID]):
    stated: E=[X]/5, R=[X]/3, A=[X]/10
    recomputed: ([X]/5*60) + ([X]/3*30) + ([X]/10*10) = [result]
    Matches stated score: YES | NO -- discrepancy: stated [X], computed [Y]

  Required field after writing:
  Inertia (C-12): "Verification performed" satisfies C-10 at PARTIAL but not C-12. The
  YES/NO field forces a binary affirmation or names the exact discrepancy.

  If discrepancy found, update DELTA REGISTER and re-check bilateral audit for that row.

**3b. Regression section**

  If prior data: "[Output] / [Criterion]: prior=[verdict], current=[verdict]"
  If no prior data: "No prior round data -- regression analysis cannot be performed."

  Required field after writing:
  Inertia (C-09): Absent section indistinguishable from no regressions. Required even empty.

---

SYNTHESIS

**LEADERBOARD**: ranked descending, standalone structure, ties noted.

**EXCELLENCE SIGNALS**: output-criterion-mechanism triples. If none: "No score spread found."

**FAILURE PATTERNS**: criteria with no PASS across all outputs. Required even when empty.

**PER-OUTPUT SYNTHESIS NOTES**: structural explanation, not verdict counts.

---

## V-04: Axes K+N -- Mechanism Index with Departure Labels

**Variation axis**: Lifecycle emphasis -- pre-Phase-1 MECHANISM INDEX table declaring each
mechanism, its phase, its target criterion, and its inertia failure prevented. Each mechanism's
"Inertia:" field is declared in the index and reproduced as a required output field at execution
time. No bilateral audit sweep.

**Hypothesis**: K (R4) forced the scorer to plan phase distribution. N forces departure labels
at each mechanism. Combining them in a pre-Phase-1 table raises structural awareness of both
C-16 and C-17 before any phase begins. The index creates a double declaration: departure labels
planned at index time AND reproduced at execution. V-04 tests whether this pre-planning approach
reaches C-17 PASS and whether the index's declaration of the sweep as a mechanism satisfies
C-18 or requires actual sweep execution.

---

You are running quest-score against the v5 rubric.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite score computed from the
rubric formula, and a golden-threshold determination. The final scorecard includes a ranked
leaderboard, excellence signals, failure patterns, and regression signals.

---

FORMULA CHANGE ALERT -- READ BEFORE ANY COMPUTATION

  N_aspirational: 8 (v4) -> 10 (v5)

Composite formula (v5):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 10 * 10)

  PARTIAL = 0.5. FAIL = 0. Golden threshold: ALL 5 essentials PASS AND composite >= 80.

Do not compute using aspirational_pass / 8. Rubric file governs conflicts.

---

MECHANISM INDEX (complete before any phase begins)

Before writing any phase content, produce this table. Each mechanism listed will appear
at its declared phase. A mechanism listed but absent from its phase is a structural violation.

  | Phase | Mechanism | Criterion | Inertia (failure prevented) |
  |-------|-----------|-----------|----------------------------|
  | Pre-Phase 1 | FORMULA CHANGE ALERT | C-13 (prompt-side) | v4 denominator (/8) used in computation; aspirational contribution inflated; golden threshold misjudged |
  | Phase 1 | Load summary (1a) | C-01 | Criteria count, formula denominator, threshold unverified; C-02/C-04 errors invisible until Phase 3 |
  | Phase 1 | Formula version delta (1b) | C-13 (output-side), C-15 | "N_aspirational=10" without prior (8); transition confirmed by endpoint but not by prior-state naming |
  | Phase 1 | SYMMETRIC DELTA REGISTER (1c) | C-15 | Prior State column structurally absent; one-sided comparisons possible without visible gap |
  | Phase 2 entry | MODEL CELL + ENTRY LOCK | C-11, C-14 | Evidence defaults to criterion restatement; norm established before model cell fires |
  | Phase 3 | Arithmetic verification (3a) | C-10, C-12 | Silent arithmetic pass; YES/NO declaration absent |
  | Phase 3 | Regression section (3b) | C-09 | Absent section indistinguishable from no regressions |

  MECHANISM INDEX WRITTEN. Each mechanism above will appear at its declared phase.
  Inertia (mechanism index): Without this pre-Phase-1 declaration, phase distribution (C-16)
  and departure labeling (C-17) depend on the scorer's memory. The index converts accidental
  compliance into a structural contract declared before any scoring begins.

---

PHASE 1: LOAD AND DELTA REGISTER

**1a. Load summary**

  (a) all criteria IDs with tier labels (C-01--C-05 essential, C-06--C-08 recommended,
      C-09--C-18 aspirational)
  (b) exact composite formula
  (c) golden threshold: all 5 essentials PASS AND composite >= 80
  (d) count and list of outputs

  Inertia (C-01): [as declared in Mechanism Index -- criteria count, formula denominator,
  threshold unverified without this block; C-02/C-04 errors invisible until Phase 3]

**1b. Formula version delta**

  Formula version delta: N_aspirational changed from [prior] to [current] in v[N].

  Inertia (C-13, C-15): [as declared -- "N_aspirational=10" without prior (8) confirms
  endpoint but not transition; both sides required]

**1c. SYMMETRIC DELTA REGISTER**

  | Comparison type | Prior state | Current state |
  |-----------------|-------------|---------------|
  | N_aspirational | [prior] | [current] |
  | Regression verdicts | [prior or "No prior-round data -- row N/A"] | [current or "--"] |
  | Arithmetic discrepancies | [stated if found, or "No discrepancy -- row N/A"] | [computed or "--"] |

  Inertia (C-15): [as declared -- Prior State column absent without the table; one-sided
  entries detectable only by re-reading prose, not by column scan]

PHASE 1 COMPLETE

---

PHASE 2: SCORE EACH OUTPUT

**MODEL CELL + ENTRY LOCK (Phase 2 entry)**

  Evidence (model): "from [output ID], [section]: [structural observation locating a specific
  feature -- not a criterion restatement]"

  Locatability test: YES = proceed. NO = rewrite.

  Inertia (C-11, C-14): [as declared -- evidence defaults to criterion restatement without
  model cell; norm established before model fires if deferred]

  ENTRY LOCK: no verdict row before model cell.

For each output:

  | ID | Criterion | Tier | Verdict | Evidence |
  |----|-----------|------|---------|----------|

Composite:
  E=[n]/5, R=[n]/3, A=[n]/10
  composite = (E/5*60) + (R/3*30) + (A/10*10) = [result]
  Golden: YES | NO -- [reason if NO]

---

PHASE 3: VERIFY

**3a. Arithmetic verification**

  Verification ([output ID]):
    stated: E=[X]/5, R=[X]/3, A=[X]/10
    recomputed: ([X]/5*60) + ([X]/3*30) + ([X]/10*10) = [result]
    Matches stated score: YES | NO -- discrepancy: stated [X], computed [Y]

  Inertia (C-12): [as declared -- "verification performed" satisfies C-10 at PARTIAL but
  not C-12; YES/NO field required]

  If discrepancy found, update DELTA REGISTER Arithmetic row.

**3b. Regression section**

  If prior data: "[Output] / [Criterion]: prior=[verdict], current=[verdict]"
  If no prior data: "No prior round data -- regression analysis cannot be performed."

  Inertia (C-09): [as declared -- absent section indistinguishable from no regressions]

---

SYNTHESIS

**LEADERBOARD**: ranked descending, standalone structure, ties noted.

**EXCELLENCE SIGNALS**: output-criterion-mechanism triples. If none: "No score spread found."

**FAILURE PATTERNS**: criteria with no PASS across all outputs. Required even when empty.

**PER-OUTPUT SYNTHESIS NOTES**: structural explanation per output. Not verdict counts.

---

## V-05: Axes N+O+K -- Full Integration

**Variation axis**: Full integration -- pre-Phase-1 MECHANISM INDEX with departure labels
(K+N), bilateral symmetry audit sweep at Phase 1 exit with Symmetric: YES/NO (O), and
"Inertia:" required fields reproduced at each mechanism during execution (N). Highest-ceiling
candidate.

**Hypothesis**: V-04 (K+N) moves departure label planning to the pre-Phase-1 index, targeting
C-17. V-02 (O) adds the bilateral sweep for C-18. V-05 combines both: the mechanism index
declares the sweep as a mechanism (so C-16 phase distribution includes Phase 1 exit), the
sweep fires with Symmetric: YES/NO verdicts, and each mechanism reproduces its departure label
from the index. This produces full structural coverage:
  - C-16: mechanisms at Phase 1 (delta register), Phase 2 (model cell + entry lock), Phase 3
    (arithmetic verification + regression)
  - C-17: every mechanism carries a labeled "Inertia:" departure statement
  - C-18: bilateral sweep at Phase 1 exit with per-comparison Symmetric: YES/NO

The mechanism index ensures C-16 and C-17 compliance is planned before execution; the
bilateral sweep ensures C-18 independent of whether J (prevention) succeeded.

---

You are running quest-score against the v5 rubric.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite score computed from the
rubric formula, and a golden-threshold determination. The final scorecard includes a ranked
leaderboard, excellence signals, failure patterns, and regression signals.

---

FORMULA CHANGE ALERT -- READ BEFORE ANY COMPUTATION

  N_aspirational: 8 (v4) -> 10 (v5)

Composite formula (v5):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 10 * 10)

  PARTIAL = 0.5. FAIL = 0. Golden threshold: ALL 5 essentials PASS AND composite >= 80.

  Inertia (FORMULA CHANGE ALERT): A scorer who does not read this alert may use the v4
  denominator (/8), producing a composite higher than the correct v5 score on the same
  verdict counts. On identical counts, /8 returns a higher aspirational contribution than
  /10 -- a golden threshold that appears met may be unmet by the correct formula.

Do not compute using aspirational_pass / 8. Rubric file governs conflicts.

---

MECHANISM INDEX (complete before any phase begins)

Produce this table. Each mechanism will appear at its declared phase. An absent mechanism
is a structural violation against its declared criterion.

  | Phase | Mechanism | Criterion | Inertia (failure prevented) |
  |-------|-----------|-----------|----------------------------|
  | Pre-Phase 1 | FORMULA CHANGE ALERT | C-13 (prompt-side) | v4 denominator (/8) used; aspirational contribution inflated; golden threshold misjudged |
  | Phase 1 | Load summary (1a) | C-01 | Criteria count, formula denominator, threshold unverified; C-02/C-04 errors invisible until Phase 3 |
  | Phase 1 | Formula version delta (1b) | C-13 (output-side), C-15 | "N_aspirational=10" without prior (8); transition from v4 confirmed by endpoint but not by prior-state naming |
  | Phase 1 | SYMMETRIC DELTA REGISTER (1c) | C-15 | Prior State column absent; one-sided comparisons produce no visible structural gap |
  | Phase 1 exit | BILATERAL SYMMETRY AUDIT SWEEP (1d) | C-18 | Register may be correctly filled but no independent catch exists; asymmetric entry undetected if J's prevention was incomplete |
  | Phase 2 entry | MODEL CELL + ENTRY LOCK | C-11, C-14 | Evidence defaults to criterion restatement; anchor fires after restatement norm is established |
  | Phase 3 | Arithmetic verification (3a) | C-10, C-12 | Silent arithmetic pass; YES/NO declaration absent |
  | Phase 3 | Regression section (3b) | C-09 | Absent section indistinguishable from no regressions |

  MECHANISM INDEX WRITTEN.
  Inertia (mechanism index): Without this pre-Phase-1 declaration, phase distribution (C-16)
  and departure labeling (C-17) depend on scorer memory. The index converts accidental
  compliance into a structural contract -- departure labels are planned before execution and
  reproduced at each mechanism during execution.

---

PHASE 1: LOAD, DELTA REGISTER, AND BILATERAL AUDIT

**1a. Load summary**

  (a) all criteria IDs with tier labels (C-01--C-05 essential, C-06--C-08 recommended,
      C-09--C-18 aspirational)
  (b) exact composite formula: composite = (E/5*60) + (R/3*30) + (A/10*10)
  (c) golden threshold: all 5 essentials PASS AND composite >= 80
  (d) count and list of outputs being scored

  Inertia (C-01): Criteria count, formula denominator, and threshold unverified without this
  block. Errors in C-02 (wrong criteria count) and C-04 (wrong denominator) remain invisible
  until Phase 3. This block makes inputs explicit before any verdict is written.

**1b. Formula version delta**

  Formula version delta: N_aspirational changed from [prior value] to [current value] in v[N].

  Inertia (C-13, C-15): "N_aspirational=10" passes C-01 (correct formula loaded) but fails
  C-15 (prior value absent). Both values required: "8 (v4) -> 10 (v5)". This declaration
  also satisfies C-13's output-side requirement by naming the prior version explicitly.

**1c. SYMMETRIC DELTA REGISTER**

  | Comparison type | Prior state | Current state |
  |-----------------|-------------|---------------|
  | N_aspirational (formula denominator) | [prior value, e.g. 8 (v4)] | [current value, e.g. 10 (v5)] |
  | Regression verdicts | [prior verdict or "No prior-round data -- row N/A"] | [current verdict or "--"] |
  | Arithmetic discrepancies | [stated score if found, or "No discrepancy -- row N/A"] | [computed score or "--"] |

  Rules: blank Prior State = structural violation (write value or "N/A -- [reason]").

  Inertia (C-15): Without the two-column structure, a scorer writes "N_aspirational=10" with
  no visible Prior State column. A blank Prior State is detectable only by re-reading
  comparison prose -- not by column scan. The column structure makes asymmetry visible.

**1d. BILATERAL SYMMETRY AUDIT SWEEP (Phase 1 exit)**

After completing the register, produce this sweep. Phase 2 does not begin until this sweep
is written and all rows show Symmetric: YES or PARTIAL.

  | Comparison | Symmetric? |
  |------------|-----------|
  | N_aspirational (formula denominator) | [YES -- Prior: [value], Current: [value] | NO -- [missing side] | PARTIAL -- N/A declared] |
  | Regression verdicts | [YES | NO -- [missing side] | PARTIAL -- no prior data] |
  | Arithmetic discrepancies | [YES | NO -- [missing side] | PARTIAL -- not found] |

  Verdict rules:
    - YES: both Prior state and Current state present in register row.
    - NO: one or both sides missing. Remediate: fill missing cell or write "N/A -- [reason]".
    - PARTIAL: N/A rule invoked. Acceptable -- confirms the scorer audited the cell.

  Inertia (C-18): J's DELTA REGISTER prevents asymmetric comparisons by requiring both
  columns to be filled. The AUDIT SWEEP provides an independent catch mechanism -- a
  Symmetric: NO cell is detectable by scanning the sweep without reading the register.
  An output can pass C-15 (both sides present through prevention) while failing C-18 (no
  independent catch). The sweep complements prevention; both are required for full coverage.

  AUDIT SWEEP WRITTEN. Phase 2 may begin.

---

PHASE 2: SCORE EACH OUTPUT

**MODEL CELL + ENTRY LOCK (Phase 2 entry -- before any verdict row)**

  Evidence (model): "from [output ID], [section or structural element]: [verbatim quote or
  structural observation sufficient for a reader to locate this feature in the output]"

  Locatability test: YES = proceed. NO = rewrite until YES.

  Inertia (C-11, C-14): Without a model cell before any verdict, evidence cells default to
  criterion restatement ("the output has a leaderboard") which cannot locate any specific
  feature. The model cell fires before the first verdict -- establishing the evidence standard
  before any cell can establish a lower norm. A model cell deferred to mid-Phase-2 fires
  after earlier cells may already contain restatement; C-14 fails even when C-11 passes.

  ENTRY LOCK: no verdict row before model cell. A verdict before the model cell is a
  Phase 2 protocol violation.

For each output, produce a scoring table:

  | ID | Criterion | Tier | Verdict | Evidence |
  |----|-----------|------|---------|----------|

Evidence standard: each cell names a specific structural element, section heading, field
label, or direct quote from the scored output. Claims applicable to any output are not
evidence. Criterion restatements are not evidence.

Composite after each table:
  essential_pass = [count; PARTIAL = 0.5]
  recommended_pass = [count; PARTIAL = 0.5]
  aspirational_pass = [count; PARTIAL = 0.5]
  composite = (E/5*60) + (R/3*30) + (A/10*10) = [result]
  Golden: YES -- all essentials PASS; composite >= 80 | NO -- [failing condition]

Score all N outputs.

---

PHASE 3: VERIFY

**3a. Arithmetic verification**

  Verification (output: [ID]):
    stated counts: E=[X]/5, R=[X]/3, A=[X]/10
    computed: ([X]/5*60) + ([X]/3*30) + ([X]/10*10) = [result]
    Matches stated score: YES | NO -- discrepancy: stated [X], computed [Y]

  Inertia (C-12): "Verification performed" satisfies C-10 at PARTIAL but does not produce
  a binary result. "The score checks out" is indistinguishable from a silent pass-through.
  The YES/NO field forces an explicit affirmation or names the exact discrepancy -- making
  errors visible even when the scorer is not looking for them.

  If discrepancy found, update DELTA REGISTER Arithmetic row and re-check bilateral audit
  for that comparison.

**3b. Regression section**

  If prior data provided:
    "[Output ID] / [Criterion ID]: prior=[verdict], current=[verdict]"
    Both verdicts required -- writing only the current verdict violates C-15.
    Update SYMMETRIC DELTA REGISTER Regression row.

  If no prior data:
    "No prior round data -- regression analysis cannot be performed."

  Inertia (C-09): An absent regression section is structurally indistinguishable from a
  section with no regressions. The user cannot determine whether regressions were checked
  or skipped. The section is required even when empty -- presence confirms the check.

---

SYNTHESIS

Write all four sections in order. All are required.

**LEADERBOARD**

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

All N outputs ranked descending. Ties noted explicitly. "See scores above" does not
satisfy C-06 -- the leaderboard must be a standalone sorted structure.

**EXCELLENCE SIGNALS**

  Signal: [output ID] -- [criterion ID] -- [structural mechanism that produced the difference]

"V-05 scored highest overall" is not an excellence signal. Requires specific output-criterion
pair and structural explanation of mechanism.

If no spread: "No score spread found. All-pass rounds confirm stability but do not advance
plateau detection. Consider redesigning variations for divergence."

**FAILURE PATTERNS**

  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

Required even when empty: "No failure patterns -- all criteria passed in at least one output."

**PER-OUTPUT SYNTHESIS NOTES**

One paragraph per output on structural score drivers. Do not list verdict counts -- explain
the structural mechanism that differentiated the output's score from others.

---

## Synthesis note

**V-05 (N+O+K) is the expected ceiling candidate for R5.** It carries all R4 champion
mechanisms (D+E+F+G+H+J+K+M) updated for v5 (N_aspirational=10) and adds:
  - Axis N: "Inertia:" labeled fields as required output entries at every mechanism
  - Axis O: Bilateral symmetry audit sweep with per-comparison Symmetric: YES/NO
  - Axis K extended: Mechanism index includes the bilateral sweep as a declared mechanism

**V-01 (N only)** establishes the C-17 PASS / C-18 FAIL baseline.

**V-02 (O only)** establishes the C-18 PASS / C-17-as-inherited baseline. The R4 V-05
base carries M-axis informal departure labels; V-02 tests whether those satisfy C-17 or
whether the N-axis standardized format is required.

**V-03 (N+O)** is the minimum combination for both C-17 and C-18. Its comparison to V-05
reveals whether K (mechanism index) adds ceiling value or is redundant given N+O.

**V-04 (K+N)** tests whether the pre-Phase-1 mechanism index approach reaches C-17 PASS
and where C-18 sits without actual sweep execution. If the index's declaration of the sweep
as a mechanism satisfies C-18, K+N is sufficient and O is redundant. Expected: C-18 FAIL
(declaration is not execution -- the sweep must actually produce Symmetric: YES/NO verdicts).

**Key comparison**: If V-03 == V-05, K is non-additive; include N+O in golden, drop K.
If V-05 > V-03, K provides ceiling value through the planning mechanism.
