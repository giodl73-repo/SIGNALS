# quest-score Variations -- Round 6 (v6 rubric, targeting C-19/C-20)

**Skill**: quest-score
**Rubric**: v6-2026-03-16 (C-01--C-05 essential, C-06--C-08 recommended, C-09--C-20 aspirational)
**N_essential=5, N_recommended=3, N_aspirational=12**
**Date**: 2026-03-16
**Round**: 6

---

## Context: what informed this round

Round 5 targeted the v5 rubric. The R5 champion (V-03 = N+O, tied with V-05 = N+O+K) carried:

| Axis | Mechanism | Phase | Criterion target |
|------|-----------|-------|-----------------|
| N | Standardized "Inertia (C-XX): [failure mode]" required output fields at every mechanism | All phases | C-17 |
| O | BILATERAL SYMMETRY AUDIT SWEEP at Phase 1 exit with per-comparison Symmetric: YES/NO | Phase 1 exit | C-18 |
| K | Pre-Phase-1 MECHANISM INDEX table declaring mechanism, phase, criterion, Inertia prevented | Pre-Phase 1 | C-16, C-17 |

R5 ceiling: V-03 and V-05 tied at 99.5 on the v5 rubric. K was non-additive given N+O: no
criterion can score above PASS; K adds planning depth but not composite points.

v6 adds two new Aspirational criteria extracted from R5 excellence signals:

| Change | R5 (v5) | R6 (v6) | Design consequence |
|--------|---------|---------|-------------------|
| C-19 (Phase 2 entry gate binary declaration) | Not in rubric | The MODEL CELL at Phase 2 entry must include a labeled binary field declaring the entry constraint was satisfied: "ENTRY LOCK: ... Confirmed" or equivalent | R5's ENTRY LOCK was a structural imperative ("do not write any verdict row until model cell is written"). C-19 requires the anchor to DECLARE the constraint was satisfied -- a binary affirmation scannable without tracing output order. |
| C-20 (Criterion-anchored inertia labels) | Not in rubric | Every inertia departure label must name at least one criterion ID in parentheses: "Inertia (C-01):" not bare "Inertia:" | R5's N-axis used "(C-XX):" as a template placeholder. C-20 requires the scorer's OUTPUT to contain actual criterion IDs. This round tests whether "(C-XX)" template instructions are sufficient, or whether explicit IDs must be provided per mechanism. |
| N_aspirational | 10 (C-09--C-18) | 12 (C-09--C-20) | Formula denominator: aspirational_pass / 10 -> aspirational_pass / 12 |

**What R6 variations must achieve beyond the R5 N+O base:**

1. **C-19 PASS**: The MODEL CELL at Phase 2 entry must include an explicit binary gate
   declaration field -- "ENTRY LOCK: no verdict row written before model cell. Confirmed."
   A structural imperative alone (C-14 PASS) is not sufficient for C-19 PASS.

2. **C-20 PASS**: Every Inertia departure label must name the specific criterion ID(s) that
   would fail if the mechanism were omitted. Bare "Inertia: [failure mode]" satisfies C-17
   but not C-20.

3. **N_aspirational update**: FORMULA CHANGE ALERT declares N_aspirational: 10 (v5) -> 12
   (v6). Any computation using /10 or /8 is a formula version error.

**Variation axes explored this round:**

| Code | Axis | Target criterion | Hypothesis |
|------|------|-----------------|-----------|
| P | ENTRY LOCK BINARY DECLARATION -- required labeled field "ENTRY LOCK: ... [Confirmed \| Violated]" added to MODEL CELL block; makes entry constraint declared and scannable | C-19 | Binary declaration converts entry constraint from structurally-evidenced (verifiable by tracing output order) to explicitly-declared (verifiable by scanning labeled field). C-14 PASS is prerequisite; C-19 PASS requires the declaration in addition. |
| Q | EXPLICIT CRITERION-ID ANCHORING -- each mechanism instruction names the exact criterion ID(s) to write in the Inertia label, replacing "(C-XX)" template; plus a CRITERION-INERTIA COVERAGE ASSERTION at Phase 1 exit | C-20 | Specifying actual criterion IDs in the prompt instruction eliminates ambiguity about whether scorers fill in IDs or copy the "(C-XX)" template literally. The coverage assertion audits whether every scored criterion appears in at least one Inertia label -- making omissions detectable before any verdict row is written. |
| R | CRITERION-COVERAGE AUDIT at synthesis end -- scans all Inertia labels written throughout the output and checks whether each criterion ID appears; no changes to per-mechanism wording | C-20 | Separates "coverage catch" (detecting gaps after writing) from "coverage prevention" (Q's explicit-ID approach). Tests whether an audit-only approach achieves C-20 PARTIAL or FAIL. |

Single-axis: V-01 (P), V-02 (Q), V-03 (R).
Minimum combination: V-04 (P+Q -- both new criteria targeted simultaneously).
Full integration: V-05 (N+O+P+Q -- v5 champion axes plus both new axes; K omitted to re-test non-additivity).

**Predicted outcomes (v6 rubric, N_aspirational=12):**

| Criterion | V-01 (P) | V-02 (Q) | V-03 (R) | V-04 (P+Q) | V-05 (N+O+P+Q) |
|-----------|----------|----------|----------|-----------|----------------|
| C-17 | PASS | PASS | PASS | PASS | PASS |
| C-18 | PASS | PASS | PASS | PASS | PASS |
| C-19 | PASS | PARTIAL | PARTIAL | PASS | PASS |
| C-20 | PARTIAL | PASS | PARTIAL | PASS | PASS |

Note on V-01/C-20: P adds the binary declaration field but leaves "(C-XX)" as a template.
Whether C-20 earns PASS or PARTIAL depends on whether scorers fill in actual criterion IDs
when instructed with the template. Predicted PARTIAL -- template is ambiguous.

Note on V-02/C-19: Q does not add the binary declaration field. ENTRY LOCK remains a structural
imperative. C-14 PASS; C-19 PARTIAL predicted (ordering structurally verifiable, undeclared).

Note on V-03/C-20: The coverage audit detects gaps after writing but does not change how labels
are written. If scorers write bare "Inertia: [text]" labels, the audit will detect the gap but
the labels already exist. C-20 is scored on label content, not on whether an audit detected the
gap. C-20 PARTIAL predicted (audit present; label criterion-ID content may be absent).

**Predicted composite scores:**

```
aspirational base: C-09 PARTIAL=0.5, all others PASS=1

V-01: 10x1 + 2x0.5 = 11.0/12 -> composite = 60 + 30 + (11.0/12 * 10) = 99.17
V-02: 10x1 + 2x0.5 = 11.0/12 -> composite = 60 + 30 + (11.0/12 * 10) = 99.17
V-03: 9x1  + 3x0.5 = 10.5/12 -> composite = 60 + 30 + (10.5/12 * 10) = 98.75
V-04: 11x1 + 1x0.5 = 11.5/12 -> composite = 60 + 30 + (11.5/12 * 10) = 99.58
V-05: 11x1 + 1x0.5 = 11.5/12 -> composite = 60 + 30 + (11.5/12 * 10) = 99.58
```

Key diagnostics this round provides:
- V-01 == V-02 (predicted 99.17 tie): Are C-19 and C-20 symmetrically valued at PARTIAL?
- V-04 == V-05 (predicted 99.58 tie): Is the N+O base non-additive given P+Q, as K was
  non-additive given N+O in v5? If so, P+Q is the minimal sufficient combination for v6.
- V-03 (98.75): Does R's audit-only approach earn C-20 PARTIAL or FAIL? PARTIAL confirms
  catch has independent value; FAIL means prevention (Q) is necessary.

---

## V-01: Axis P -- ENTRY LOCK Binary Declaration Field

**Variation axis**: Lifecycle emphasis -- the MODEL CELL at Phase 2 entry gains a required
labeled binary gate declaration field that makes the Phase 2 entry constraint declared and
scannable rather than structurally-inferred from output order.

**Hypothesis**: R5 N+O champion's ENTRY LOCK was a structural imperative ("do not write any
verdict row until model cell is written"). C-19 is a tightening of C-14: structural placement
earns C-14 PASS but not C-19 PASS. Adding "ENTRY LOCK: no verdict row written before model
cell. [Confirmed | Violated]" as a required output field achieves C-19 PASS without other
changes. The "(C-XX)" template in Inertia instructions is inherited; C-20 earns PARTIAL
because the template is a format hint, not a guarantee that actual criterion IDs are produced.

---

You are running quest-score against the v6 rubric.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite score computed from the
rubric formula, and a golden-threshold determination. The final scorecard includes a ranked
leaderboard, excellence signals, failure patterns, and regression signals.

---

FORMULA CHANGE ALERT -- READ BEFORE ANY COMPUTATION

The v6 rubric changes the aspirational denominator from the v5 value.

  N_aspirational: 10 (v5) -> 12 (v6)

Composite formula (v6, active):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 12 * 10)

  PARTIAL counts as 0.5 toward pass count. FAIL counts as 0.
  Golden threshold: ALL 5 essentials PASS AND composite >= 80.

Do not compute any score using aspirational_pass / 10. Any computation using the v5
denominator is an error. If a conflict exists between this prompt and a rubric file,
the rubric file governs.

---

PHASE 1: LOAD, DELTA REGISTER, AND BILATERAL AUDIT

Before scoring any output, complete sections 1a through 1d in order. Do not proceed to
Phase 2 until all four sections are written and the bilateral audit shows no Symmetric: NO rows.

**1a. Load summary**

Produce a block confirming the rubric was read. The block must name all four elements:
  (a) all criteria IDs with tier labels (C-01--C-05 essential, C-06--C-08 recommended,
      C-09--C-20 aspirational)
  (b) the exact composite formula text (as written above)
  (c) the golden threshold condition (all 5 essentials PASS AND composite >= 80)
  (d) the count and list of outputs being scored

A load summary missing any one of (a)--(d) earns PARTIAL on C-01. Missing entirely earns FAIL.

After writing the load summary, write this required labeled field:

  Inertia (C-01): Without this load block, criteria count (20), formula denominator (/12),
  and threshold are unverified before any verdict is written. A scorer who skips this step
  produces a verdict matrix missing C-19 and C-20 rows, and computes all composites using
  the v5 denominator -- both errors invisible until Phase 3.

**1b. Formula version delta**

Write in your scoring output (visible to the reader):

  Formula version delta: N_aspirational changed from [prior value] to [current value] in v[N].

If the prior version cannot be determined:
  "No prior version delta detectable -- scoring under v6 as the baseline version."

After writing the formula version delta, write this required labeled field:

  Inertia (C-13, C-15): "N_aspirational=12" in the output confirms the current value was
  loaded but does not confirm the prior value (10) was registered as distinct. C-15 requires
  both sides of every delta comparison. A current-only statement fails C-15 even when C-01
  (correct formula loaded) is PASS.

**1c. SYMMETRIC DELTA REGISTER**

Produce the following table. Fill every cell before proceeding to 1d.

  | Comparison type | Prior state | Current state |
  |-----------------|-------------|---------------|
  | N_aspirational (formula denominator) | [value from prior rubric version] | [value in v6] |
  | Regression verdicts | [prior verdict for each regressed pair, or "No prior-round data -- row N/A"] | [current verdict, or "--"] |
  | Arithmetic discrepancies | [stated score if discrepancy found, or "No discrepancy -- row N/A"] | [computed score, or "--"] |

Rules:
  - A blank Prior State cell is a structural violation. Write the value or "N/A -- [reason]".
  - A blank Current State cell is also a structural violation.
  - The register must contain at least the N_aspirational row.

After writing the register, write this required labeled field:

  Inertia (C-15): Without the two-column table, a scorer writes "N_aspirational=12" correctly
  but never names the prior value (10). The column structure makes a one-sided entry a visible
  structural gap -- a blank Prior State cell is detectable by column scan without reading prose.

**1d. BILATERAL SYMMETRY AUDIT SWEEP (Phase 1 exit)**

After completing the register, produce this sweep before Phase 2 begins.

  | Comparison | Symmetric? |
  |------------|-----------|
  | N_aspirational (formula denominator) | [YES -- Prior: [value], Current: [value] | NO -- [which side missing] | PARTIAL -- N/A declared] |
  | Regression verdicts | [YES | NO -- [missing side] | PARTIAL -- no prior data] |
  | Arithmetic discrepancies | [YES | NO -- [missing side] | PARTIAL -- no discrepancy found] |

Verdict rules:
  - Symmetric: YES -- both Prior state and Current state present in register row.
  - Symmetric: NO -- one or both sides missing. Fill the missing cell or write "N/A -- [reason]"
    to convert NO to PARTIAL before proceeding to Phase 2.
  - Symmetric: PARTIAL -- N/A rule invoked correctly. Not a failure.

After writing the sweep, write this required labeled field:

  Inertia (C-18): The SYMMETRIC DELTA REGISTER prevents asymmetric entries by requiring both
  columns. This audit sweep provides an independent catch mechanism -- a Symmetric: NO cell
  is detectable by scanning the sweep without re-reading register prose column by column.
  An output can pass C-15 (both sides present through prevention) while failing C-18 (no
  independent catch). Prevention and catch are both required.

PHASE 1 COMPLETE. Proceed to Phase 2 only after 1a, 1b, 1c, and 1d are written.

---

PHASE 2: SCORE EACH OUTPUT

**MODEL CELL + ENTRY LOCK (Phase 2 entry -- write before any verdict row)**

Write the following three elements in sequence as the first action of Phase 2, before any
criterion-output evidence row.

(1) Evidence (model):
  "from [output ID], [section or structural element]: [verbatim quote or structural observation
  that locates a specific feature in the output -- not a restatement of the criterion]"
  Locatability test: could a reader find the referenced feature using only this evidence text?
  YES: proceed. NO: rewrite before entering any verdict row.

(2) Required labeled field after the model cell and locatability test:

  Inertia (C-11, C-14): Without a model cell at Phase 2 entry, evidence cells default to
  criterion restatement -- "the output has a leaderboard" cannot locate any specific feature.
  The model cell fires before the first verdict, establishing the evidence standard before any
  cell can establish a lower norm. Deferring the anchor to mid-Phase-2 allows restatement in
  earlier cells before the standard is visible.

(3) Binary gate declaration:

  ENTRY LOCK: no verdict row written before model cell. [Confirmed | Violated -- first verdict
  row appears at: ___]

  Write "Confirmed" if the model cell above is the first Phase 2 content written.
  Write "Violated -- first verdict row appears at: [location]" if any verdict row preceded
  the model cell. A "Violated" declaration earns C-14 FAIL but C-19 PASS (the mechanism
  reported accurately). The ENTRY LOCK field is required; omitting it earns C-19 FAIL.

For each output, produce a scoring table:

  | ID | Criterion | Tier | Verdict | Evidence |
  |----|-----------|------|---------|----------|

Column rules:
  - Verdict: PASS | PARTIAL | FAIL only.
  - Evidence: must quote, paraphrase with location, or name a specific structural feature of
    the scored output. Criterion restatement is not evidence.
  - No row may be blank or missing. Include rows for all criteria C-01 through C-20.

After the table, write the composite:

  essential_pass = [count; PARTIAL = 0.5]
  recommended_pass = [count; PARTIAL = 0.5]
  aspirational_pass = [count; PARTIAL = 0.5]
  composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 12 * 10) = [result]
  Golden: YES -- all essentials PASS; composite >= 80 | NO -- [which essential failed or composite < 80]

Score all N outputs before proceeding to Phase 3.

---

PHASE 3: VERIFY

**3a. Arithmetic verification**

Pick one output. Recompute its composite from the stated verdict counts and formula.

  Verification (output: [ID]):
    stated counts: E=[X]/5, R=[X]/3, A=[X]/12
    computed composite: ([X]/5 * 60) + ([X]/3 * 30) + ([X]/12 * 10) = [result]
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
  section with no regressions. The section is required even when empty -- its presence
  confirms the check was performed.

---

SYNTHESIS

Write the following sections in order.

**LEADERBOARD**

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

All N outputs ranked descending. Ties noted explicitly with stated tiebreak rule or
"tied -- no tiebreak applied." "See scores above" does not satisfy C-06.

**EXCELLENCE SIGNALS**

For each criterion where one output scores noticeably higher than others:
  Signal: [output ID] -- [criterion ID] -- [structural mechanism that produced the difference]

Generic rankings ("V-04 scored highest overall") are not excellence signals. Requires
output-criterion pair with mechanism explanation. If no outlier pair: state explicitly.

**FAILURE PATTERNS**

  Pattern: [criterion ID] -- [criterion name]
  Diagnosis: [rubric gap | skill design issue | input quality issue] -- [one sentence]

Required even when empty: "No failure patterns -- all criteria passed in at least one output."

**PER-OUTPUT SYNTHESIS NOTES**

One paragraph per output on structural score drivers. Explain the mechanism, not the counts.

---

## V-02: Axis Q -- Explicit Criterion-ID Anchoring + Coverage Assertion

**Variation axis**: Inertia framing -- each mechanism instruction specifies the concrete
criterion ID(s) to include in the Inertia label, replacing the "(C-XX)" template placeholder
with actual IDs. A CRITERION-INERTIA COVERAGE ASSERTION at Phase 1 exit verifies every scored
criterion appears in at least one Inertia label before scoring begins.

**Hypothesis**: The v5 N-axis used "Inertia (C-XX): [failure mode]" as a format template.
C-20 requires actual criterion IDs in the scored output. Q eliminates the ambiguity by
specifying the exact IDs in each instruction. The coverage assertion makes omissions auditable
at Phase 1 exit -- before any verdict row is written. C-19 is not addressed; ENTRY LOCK
remains a structural imperative. C-19 predicted PARTIAL.

---

You are running quest-score against the v6 rubric.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite score computed from the
rubric formula, and a golden-threshold determination. The final scorecard includes a ranked
leaderboard, excellence signals, failure patterns, and regression signals.

---

FORMULA CHANGE ALERT -- READ BEFORE ANY COMPUTATION

  N_aspirational: 10 (v5) -> 12 (v6)

Composite formula (v6, active):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 12 * 10)

  PARTIAL = 0.5. FAIL = 0. Golden threshold: ALL 5 essentials PASS AND composite >= 80.

Do not compute any score using /10. If a conflict exists between this prompt and a rubric
file, the rubric file governs.

---

PHASE 1: LOAD, DELTA REGISTER, BILATERAL AUDIT, AND COVERAGE ASSERTION

Complete sections 1a through 1e in order. Do not proceed to Phase 2 until all five sections
are written, the bilateral audit shows no Symmetric: NO rows, and the coverage assertion is
complete.

**1a. Load summary**

  (a) all criteria IDs with tier labels (C-01--C-05 essential, C-06--C-08 recommended,
      C-09--C-20 aspirational)
  (b) exact composite formula text (v6 active: /12 aspirational denominator)
  (c) golden threshold: all 5 essentials PASS AND composite >= 80
  (d) count and list of outputs being scored

After writing the load summary, write this required labeled field:

  Inertia (C-01): Without this load block, criteria count (20), formula denominator (/12),
  and threshold are unverified. Missing C-19 and C-20 rows (C-02 error) and /10 denominator
  in composite calculations (C-04 error) remain invisible until Phase 3.

**1b. Formula version delta**

Write in your output:
  Formula version delta: N_aspirational changed from [prior value] to [current value] in v[N].
  Example: "N_aspirational changed from 10 (v5) to 12 (v6)."

If prior unknown: "No prior version delta detectable -- scoring under v6 as baseline."

After writing, write this required labeled field:

  Inertia (C-13, C-15): "N_aspirational=12" passes C-01 but fails C-15 -- the prior value
  (10) is absent. Both sides are required to confirm the transition was registered, not just
  the endpoint loaded.

**1c. SYMMETRIC DELTA REGISTER**

  | Comparison type | Prior state | Current state |
  |-----------------|-------------|---------------|
  | N_aspirational (formula denominator) | [prior value -- e.g., "10 (v5)"] | [current value -- e.g., "12 (v6)"] |
  | Regression verdicts | [prior verdict or "No prior-round data -- row N/A"] | [current verdict or "--"] |
  | Arithmetic discrepancies | [stated score or "No discrepancy -- row N/A"] | [computed score or "--"] |

Blank Prior State = structural violation. Write value or "N/A -- [reason]".

After writing, write this required labeled field:

  Inertia (C-15): Without the two-column table, a scorer writing "N_aspirational=12" never
  names the prior value (10). The column structure makes a one-sided entry a visible structural
  gap detectable by column scan, not requiring re-reading of prose.

**1d. BILATERAL SYMMETRY AUDIT SWEEP (Phase 1 exit)**

  | Comparison | Symmetric? |
  |------------|-----------|
  | N_aspirational (formula denominator) | [YES -- Prior: [v], Current: [v] | NO -- [missing side] | PARTIAL -- N/A declared] |
  | Regression verdicts | [YES | NO | PARTIAL -- no prior data] |
  | Arithmetic discrepancies | [YES | NO | PARTIAL -- no discrepancy found] |

Symmetric: NO requires remediation before Phase 2.

After writing the sweep, write this required labeled field:

  Inertia (C-18): The DELTA REGISTER prevents asymmetric entries by column structure. This
  audit sweep provides an independent catch: a Symmetric: NO is visible by scanning the sweep
  table without reading register prose. Prevention and catch are both required.

**1e. CRITERION-INERTIA COVERAGE ASSERTION**

After 1d, verify that every scored criterion ID will appear in at least one Inertia label
in this output. Produce the following assertion table:

  | Criterion | Covered? | Location |
  |-----------|----------|----------|
  | C-01 | YES | Inertia (C-01): at 1a |
  | C-13 | YES | Inertia (C-13, C-15): at 1b |
  | C-15 | YES | Inertia (C-15): at 1c; also 1b |
  | C-18 | YES | Inertia (C-18): at 1d |
  | C-11, C-14, C-19 | DEFERRED | Covered by MODEL CELL block at Phase 2 entry |
  | C-12, C-10 | DEFERRED | Covered by 3a arithmetic verification block |
  | C-09 | DEFERRED | Covered by 3b regression section block |
  | C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-16, C-17, C-20 | DEFERRED | Covered by Phase 2 and synthesis mechanisms |

After writing, write this required labeled field:

  Inertia (C-20): A bare "Inertia: [text]" label satisfies C-17 (departure label present)
  but fails C-20 (criterion ID absent). Criterion-ID anchoring -- "Inertia (C-01):" not bare
  "Inertia:" -- makes coverage auditable: a reader verifies all criteria appear in at least
  one label by scanning labels, rather than cross-referencing mechanisms and criteria.

PHASE 1 COMPLETE. Proceed to Phase 2 only after 1a, 1b, 1c, 1d, and 1e are written.

---

PHASE 2: SCORE EACH OUTPUT

**MODEL CELL (Phase 2 entry -- write before any verdict row)**

  Evidence (model): "from [output ID], [section or structural element]: [verbatim quote or
  structural observation that locates a specific feature -- not a criterion restatement]"
  Locatability test: YES -- proceed. NO -- rewrite.

After writing the model cell, write this required labeled field:

  Inertia (C-11, C-14): Without a model cell before any verdict, evidence defaults to criterion
  restatement. The model cell fires first, establishing the standard before any cell can
  establish a lower norm.

ENTRY LOCK: do not write any verdict row until the model cell is written and passes the
locatability test. A verdict written before the model cell is a Phase 2 protocol violation.

For each output, produce a scoring table:

  | ID | Criterion | Tier | Verdict | Evidence |

Include rows for all criteria C-01 through C-20. No row blank or missing.

After the table:
  essential_pass = [count]
  recommended_pass = [count]
  aspirational_pass = [count]
  composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 12 * 10) = [result]
  Golden: YES | NO -- [reason]

---

PHASE 3: VERIFY

**3a. Arithmetic verification**

  Verification (output: [ID]):
    stated counts: E=[X]/5, R=[X]/3, A=[X]/12
    computed composite: ([X]/5 * 60) + ([X]/3 * 30) + ([X]/12 * 10) = [result]
    Matches stated score: YES | NO -- discrepancy: stated [X], computed [Y]

After writing, write this required labeled field:

  Inertia (C-12): A binary YES/NO declaration forces explicit affirmation or names the exact
  discrepancy. "The composite checks out" is indistinguishable from a silent pass-through.

**3b. Regression section**

If prior data: "[Output] / [Criterion]: prior=[verdict], current=[verdict]"
If no prior data: "No prior round data -- regression analysis cannot be performed."

After writing, write this required labeled field:

  Inertia (C-09): Absent section indistinguishable from empty section. Required always.

---

SYNTHESIS

**LEADERBOARD** -- All N outputs ranked descending. Ties noted.

**EXCELLENCE SIGNALS** -- Output-criterion-mechanism triples. Generic rankings not accepted.

**FAILURE PATTERNS** -- Required even when empty:
  "No failure patterns -- all criteria passed in at least one output."

**PER-OUTPUT SYNTHESIS NOTES** -- One paragraph per output on structural score drivers.

---

## V-03: Axis R -- Criterion-Coverage Audit at Synthesis

**Variation axis**: Role sequence -- a CRITERION-INERTIA COVERAGE AUDIT appears at the END of
the synthesis section, scanning all Inertia labels written throughout the output and checking
whether each scored criterion ID appears in at least one label. No changes to per-mechanism
Inertia label wording; the "(C-XX)" template is preserved throughout Phase 1 and Phase 2.

**Hypothesis**: R separates "catch" (detecting coverage gaps after writing) from "prevention"
(Q's approach of specifying IDs upfront). A post-hoc audit detects gaps but cannot prevent
bare "Inertia: [text]" labels from having been written. C-20 is scored on label content, not
on whether an audit detected the gap. R alone earns C-20 PARTIAL: the audit mechanism is
present (satisfying the spirit of coverage verification) but labels may lack criterion IDs
(failing the literal C-20 pass condition). C-19 remains PARTIAL (no binary declaration field).
V-03 establishes the audit-only baseline to contrast with Q's prevention approach.

---

You are running quest-score against the v6 rubric.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite score computed from the
rubric formula, and a golden-threshold determination. The final scorecard includes a ranked
leaderboard, excellence signals, failure patterns, and regression signals.

---

FORMULA CHANGE ALERT -- READ BEFORE ANY COMPUTATION

  N_aspirational: 10 (v5) -> 12 (v6)

Composite formula (v6, active):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 12 * 10)

  PARTIAL = 0.5. FAIL = 0. Golden threshold: ALL 5 essentials PASS AND composite >= 80.

Do not compute any score using /10.

---

PHASE 1: LOAD, DELTA REGISTER, AND BILATERAL AUDIT

Complete sections 1a through 1d in order before Phase 2.

**1a. Load summary**

  (a) all criteria IDs with tier labels (C-01--C-05 essential, C-06--C-08 recommended,
      C-09--C-20 aspirational)
  (b) exact composite formula text
  (c) golden threshold: all 5 essentials PASS AND composite >= 80
  (d) count and list of outputs being scored

After writing, write this required labeled field:

  Inertia (C-01): Without this load block, criteria count (20), formula denominator (/12),
  and threshold are unverified before any verdict is written.

**1b. Formula version delta**

Write: "Formula version delta: N_aspirational changed from [prior] to [current] in v[N]."
If prior unknown: "No prior version delta detectable -- scoring under v6 as baseline."

After writing, write this required labeled field:

  Inertia (C-13, C-15): "N_aspirational=12" names the current value but not the prior (10).
  C-15 requires both sides to confirm the transition was registered, not just the endpoint.

**1c. SYMMETRIC DELTA REGISTER**

  | Comparison type | Prior state | Current state |
  |-----------------|-------------|---------------|
  | N_aspirational (formula denominator) | [prior value] | [current value] |
  | Regression verdicts | [prior verdict or "No prior-round data -- row N/A"] | [current or "--"] |
  | Arithmetic discrepancies | [stated score or "No discrepancy -- row N/A"] | [computed or "--"] |

Blank Prior State = structural violation.

After writing, write this required labeled field:

  Inertia (C-15): Without the two-column table, a one-sided entry -- naming only the current
  value -- is not structurally visible as incomplete. The column structure makes it detectable
  by column scan without reading prose.

**1d. BILATERAL SYMMETRY AUDIT SWEEP (Phase 1 exit)**

  | Comparison | Symmetric? |
  |------------|-----------|
  | N_aspirational (formula denominator) | [YES -- Prior: [v], Current: [v] | NO | PARTIAL -- N/A] |
  | Regression verdicts | [YES | NO | PARTIAL -- no prior data] |
  | Arithmetic discrepancies | [YES | NO | PARTIAL -- no discrepancy found] |

Symmetric: NO requires remediation before Phase 2.

After writing, write this required labeled field:

  Inertia (C-18): The DELTA REGISTER prevents asymmetric entries. This sweep catches them
  independently -- a Symmetric: NO is visible by scanning the sweep without reading register
  prose. Both prevention and catch are required.

PHASE 1 COMPLETE. Proceed to Phase 2 only after 1a, 1b, 1c, and 1d are written.

---

PHASE 2: SCORE EACH OUTPUT

**MODEL CELL (Phase 2 entry -- write before any verdict row)**

  Evidence (model): "from [output ID], [section]: [verbatim quote or structural observation
  that locates a specific feature -- not a criterion restatement]"
  Locatability test: YES -- proceed. NO -- rewrite.

After writing, write this required labeled field:

  Inertia (C-11, C-14): Without a model cell before any verdict, evidence defaults to
  criterion restatement. The model cell fires first, establishing the evidence standard.

ENTRY LOCK: do not write any verdict row until the model cell passes the locatability test.

For each output, produce a scoring table:
  | ID | Criterion | Tier | Verdict | Evidence |
Include all criteria C-01 through C-20. No row blank.

After the table:
  essential_pass = [count]
  recommended_pass = [count]
  aspirational_pass = [count]
  composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 12 * 10) = [result]
  Golden: YES | NO -- [reason]

---

PHASE 3: VERIFY

**3a. Arithmetic verification**

  Verification (output: [ID]):
    stated counts: E=[X]/5, R=[X]/3, A=[X]/12
    computed composite: ([X]/5 * 60) + ([X]/3 * 30) + ([X]/12 * 10) = [result]
    Matches stated score: YES | NO -- discrepancy: stated [X], computed [Y]

After writing, write this required labeled field:

  Inertia (C-12): A binary YES/NO declaration forces explicit affirmation. Narrative
  equivalents are indistinguishable from silent pass-through.

**3b. Regression section**

If prior data: "[Output] / [Criterion]: prior=[verdict], current=[verdict]"
If no prior data: "No prior round data -- regression analysis cannot be performed."

After writing, write this required labeled field:

  Inertia (C-09): Absent section is indistinguishable from an empty section. Required always.

---

SYNTHESIS

**LEADERBOARD** -- All N outputs ranked descending. Ties noted.

**EXCELLENCE SIGNALS** -- Output-criterion-mechanism triples. Generic rankings not accepted.

**FAILURE PATTERNS** -- Required even when empty:
  "No failure patterns -- all criteria passed in at least one output."

**PER-OUTPUT SYNTHESIS NOTES** -- One paragraph per output on structural score drivers.

**CRITERION-INERTIA COVERAGE AUDIT**

After completing the per-output notes, produce the following audit table. Scan all Inertia
labels written throughout this scoring output and check whether each scored criterion ID
appears in at least one label.

  | Criterion | Appears in >= 1 Inertia label? | Label excerpt |
  |-----------|-------------------------------|---------------|
  | C-01 | [YES -- "Inertia (C-01):" at Phase 1 / 1a | NO -- no label names C-01] | [excerpt or "none"] |
  | C-02 | [YES | NO] | ... |
  ... (one row per criterion, C-01 through C-20)

Coverage summary:
  Covered: [N] criteria
  Not covered: [N] criteria -- [list criterion IDs]
  Full coverage: YES | NO

If full coverage is NO, note whether any uncovered criterion represents a design gap (no
mechanism targets it) or an omission (a mechanism exists but its label lacks the criterion ID).

This audit verifies criterion-coverage completeness at the output level. A reader can determine
which criteria are covered by Inertia labels by scanning this table rather than reading every
label in the scoring body.

---

## V-04: Axes P+Q -- Binary Entry Lock + Criterion-ID Anchoring

**Variation axis combination**: P (ENTRY LOCK binary declaration field) + Q (explicit
criterion-ID anchoring per mechanism with CRITERION-INERTIA COVERAGE ASSERTION at Phase 1 exit).
Both new v6 criteria targeted simultaneously.

**Hypothesis**: P achieves C-19 PASS (binary gate declaration makes entry constraint declared
and scannable). Q achieves C-20 PASS (explicit criterion IDs in every Inertia label, coverage
assertion audits completeness before scoring begins). Combined, P+Q achieves full PASS on both
new criteria. The v5 N+O base is inherited; K is omitted. Predicted co-champion with V-05.

---

You are running quest-score against the v6 rubric.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite score computed from the
rubric formula, and a golden-threshold determination. The final scorecard includes a ranked
leaderboard, excellence signals, failure patterns, and regression signals.

---

FORMULA CHANGE ALERT -- READ BEFORE ANY COMPUTATION

  N_aspirational: 10 (v5) -> 12 (v6)

Composite formula (v6, active):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 12 * 10)

  PARTIAL = 0.5. FAIL = 0.
  Golden threshold: ALL 5 essentials PASS AND composite >= 80.

Do not compute any score using /10. If a conflict exists between this prompt and the rubric
file, the rubric file governs.

---

PHASE 1: LOAD, DELTA REGISTER, BILATERAL AUDIT, AND COVERAGE ASSERTION

Complete 1a through 1e in order. Do not proceed to Phase 2 until all five are written, the
bilateral audit shows no Symmetric: NO rows, and the coverage assertion is complete.

**1a. Load summary**

  (a) all criteria IDs with tier labels (C-01--C-05 essential, C-06--C-08 recommended,
      C-09--C-20 aspirational)
  (b) exact composite formula text (v6 active: /12 aspirational denominator)
  (c) golden threshold: all 5 essentials PASS AND composite >= 80
  (d) count and list of outputs being scored

Required field after writing:

  Inertia (C-01): Without this load block, criteria count (20), formula denominator (/12),
  and threshold are unverified. Missing C-19 and C-20 rows and /10 denominator errors remain
  invisible until Phase 3.

**1b. Formula version delta**

Write: "Formula version delta: N_aspirational changed from [prior] to [current] in v[N]."
If prior unknown: "No prior version delta detectable -- scoring under v6 as baseline."

Required field after writing:

  Inertia (C-13, C-15): "N_aspirational=12" passes C-01 but fails C-15 -- prior value (10)
  absent. Both sides confirm the transition was registered, not just the endpoint loaded.

**1c. SYMMETRIC DELTA REGISTER**

  | Comparison type | Prior state | Current state |
  |-----------------|-------------|---------------|
  | N_aspirational (formula denominator) | [prior -- e.g., "10 (v5)"] | [current -- e.g., "12 (v6)"] |
  | Regression verdicts | [prior verdict or "No prior-round data -- row N/A"] | [current or "--"] |
  | Arithmetic discrepancies | [stated score or "No discrepancy -- row N/A"] | [computed or "--"] |

Blank Prior State = structural violation. Write value or "N/A -- [reason]".

Required field after writing:

  Inertia (C-15): Without the two-column table, a scorer writing only the current value
  produces a gap detectable only by re-reading prose. The column structure makes the gap
  visible by column scan.

**1d. BILATERAL SYMMETRY AUDIT SWEEP (Phase 1 exit)**

  | Comparison | Symmetric? |
  |------------|-----------|
  | N_aspirational | [YES -- Prior: [v], Current: [v] | NO | PARTIAL -- N/A] |
  | Regression verdicts | [YES | NO | PARTIAL] |
  | Arithmetic discrepancies | [YES | NO | PARTIAL] |

Symmetric: NO requires remediation before Phase 2.

Required field after writing:

  Inertia (C-18): DELTA REGISTER prevents asymmetric entries. This sweep catches them
  independently -- Symmetric: NO visible by scanning the sweep table. Both are required.

**1e. CRITERION-INERTIA COVERAGE ASSERTION**

After 1d, verify every scored criterion ID will appear in at least one Inertia label.

  | Criterion | Covered? | Location |
  |-----------|----------|----------|
  | C-01 | YES | Inertia (C-01): at 1a |
  | C-13 | YES | Inertia (C-13, C-15): at 1b |
  | C-15 | YES | Inertia (C-15): at 1c; also 1b |
  | C-18 | YES | Inertia (C-18): at 1d |
  | C-11, C-14, C-19 | DEFERRED | Covered by MODEL CELL + ENTRY LOCK block (Phase 2 entry) |
  | C-12, C-10 | DEFERRED | Covered by 3a arithmetic verification block |
  | C-09 | DEFERRED | Covered by 3b regression section block |
  | C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-16, C-17, C-20 | DEFERRED | Phase 2 and synthesis mechanisms |

Required field after writing:

  Inertia (C-20): A bare "Inertia: [text]" label explains the failure mode but does not
  anchor to a criterion ID. Without criterion-ID anchoring, departure labels are present
  (C-17 PASS) but coverage is not auditable by scanning labels (C-20 FAIL or PARTIAL).
  "Inertia (C-01):" makes coverage verifiable: a reader checks which criteria appear in
  Inertia labels without cross-referencing mechanisms and criteria separately.

PHASE 1 COMPLETE. All five sections written.

---

PHASE 2: SCORE EACH OUTPUT

**MODEL CELL + ENTRY LOCK (Phase 2 entry -- three elements in sequence before any verdict row)**

(1) Evidence (model):
  "from [output ID], [section or structural element]: [verbatim quote or structural observation
  that locates a specific feature -- not a criterion restatement]"
  Locatability test: YES -- proceed. NO -- rewrite.

(2) Required labeled field after model cell:

  Inertia (C-11, C-14): Without a model cell before any verdict, evidence defaults to criterion
  restatement. The model cell fires first, establishing the evidence standard before any cell
  can establish a lower norm.

(3) Binary gate declaration:

  ENTRY LOCK: no verdict row written before model cell. [Confirmed | Violated -- first verdict
  row appears at: ___]

  "Confirmed" if model cell is the first Phase 2 content written.
  "Violated" and location if any verdict row preceded the model cell.

Required field after the gate declaration:

  Inertia (C-19): The ENTRY LOCK imperative prevents violations structurally -- C-14 PASS.
  But the constraint remains inferred from output order. The binary gate declaration makes it
  declared and scannable: "ENTRY LOCK: ... Confirmed" is verifiable by scanning the labeled
  field. C-14 (structural placement) and C-19 (declaration of that placement) are separable.

For each output, produce a scoring table:
  | ID | Criterion | Tier | Verdict | Evidence |
Include all criteria C-01 through C-20. No row blank.

After the table:
  essential_pass = [count]
  recommended_pass = [count]
  aspirational_pass = [count]
  composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 12 * 10) = [result]
  Golden: YES | NO -- [reason]

---

PHASE 3: VERIFY

**3a. Arithmetic verification**

  Verification (output: [ID]):
    stated counts: E=[X]/5, R=[X]/3, A=[X]/12
    computed: ([X]/5 * 60) + ([X]/3 * 30) + ([X]/12 * 10) = [result]
    Matches stated score: YES | NO -- discrepancy: stated [X], computed [Y]

Required field: Inertia (C-12): Binary declaration forces explicit result. Narrative
equivalents indistinguishable from silent pass-through.

**3b. Regression section**

If prior data: "[Output] / [Criterion]: prior=[verdict], current=[verdict]"
If no prior data: "No prior round data -- regression analysis cannot be performed."

Required field: Inertia (C-09): Absent section indistinguishable from empty. Required always.

---

SYNTHESIS

**LEADERBOARD** -- All N outputs ranked descending. Ties noted.
**EXCELLENCE SIGNALS** -- Output-criterion-mechanism triples.
**FAILURE PATTERNS** -- Required even when empty.
**PER-OUTPUT SYNTHESIS NOTES** -- One paragraph per output on structural score drivers.

---

## V-05: Full Integration -- N+O+P+Q

**Variation axis combination**: All four axes applied. N (standardized "Inertia (C-XX):"
required output fields), O (bilateral symmetry audit sweep), P (ENTRY LOCK binary declaration),
Q (explicit criterion-ID anchoring + coverage assertion). K (mechanism index) is omitted to
re-test whether K is non-additive in v6, as it was in v5. Highest-ceiling candidate.

**Hypothesis**: N+O achieved the v5 ceiling at 99.5/100. P and Q target the two new v6 criteria.
Combined, N+O+P+Q should reach the v6 ceiling. The key question is whether N (standardized
"(C-XX)" template) already subsumes Q (explicit IDs) -- if scorers consistently fill in actual
criterion IDs when prompted with the template, then Q adds defensive redundancy but no new
criterion coverage. If not, Q is strictly additive. The predicted tie between V-04 and V-05
tests this: V-04 has P+Q without N+O; V-05 has N+O+P+Q. If they tie, N+O are non-additive
given P+Q (Q already subsumes N's criterion-ID function).

---

You are running quest-score against the v6 rubric.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite score computed from the
rubric formula, and a golden-threshold determination. The final scorecard includes a ranked
leaderboard, excellence signals, failure patterns, and regression signals.

---

FORMULA CHANGE ALERT -- READ BEFORE ANY COMPUTATION

The v6 rubric changes the aspirational denominator from the v5 value.

  N_aspirational: 10 (v5) -> 12 (v6)

Composite formula (v6, active):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 12 * 10)

  PARTIAL = 0.5. FAIL = 0.
  Golden threshold: ALL 5 essentials PASS AND composite >= 80.

Do not compute any score using aspirational_pass / 10 or /8.
If a conflict exists between this prompt and the rubric file, the rubric file governs.

---

PHASE 1: LOAD, DELTA REGISTER, BILATERAL AUDIT, AND COVERAGE ASSERTION

Complete 1a through 1e in order. Do not proceed to Phase 2 until all five sections are written,
bilateral audit shows no Symmetric: NO rows, and coverage assertion is complete.

**1a. Load summary**

  (a) all criteria IDs with tier labels (C-01--C-05 essential, C-06--C-08 recommended,
      C-09--C-20 aspirational)
  (b) exact composite formula text (v6: /12 aspirational denominator)
  (c) golden threshold: all 5 essentials PASS AND composite >= 80
  (d) count and list of outputs being scored

Required field after writing:

  Inertia (C-01): Without this load block, criteria count (20), formula denominator (/12 not
  /10), and threshold are unverified before any verdict. A scorer who skips this step produces
  an 18-row verdict matrix (missing C-19 and C-20) and computes composites with the v5
  denominator -- both errors invisible until Phase 3.

**1b. Formula version delta**

Write: "Formula version delta: N_aspirational changed from [prior] to [current] in v[N]."
Example: "N_aspirational changed from 10 (v5) to 12 (v6)."
If prior unknown: "No prior version delta detectable -- scoring under v6 as baseline."

Required field after writing:

  Inertia (C-13, C-15): "N_aspirational=12" passes C-01 (formula loaded correctly) but fails
  C-15 (prior value 10 absent -- transition not confirmed). Both sides required: the formula
  version delta block names prior AND current explicitly to confirm the transition was
  registered, not just the endpoint.

**1c. SYMMETRIC DELTA REGISTER**

  | Comparison type | Prior state | Current state |
  |-----------------|-------------|---------------|
  | N_aspirational (formula denominator) | [prior value -- write "10 (v5)" if known] | [current -- write "12 (v6)"] |
  | Regression verdicts | [prior verdict or "No prior-round data -- row N/A"] | [current verdict or "--"] |
  | Arithmetic discrepancies | [stated score or "No discrepancy -- row N/A"] | [computed score or "--"] |

Blank Prior State = structural violation. Write value or "N/A -- [reason]".

Required field after writing:

  Inertia (C-15): Without the two-column table, a scorer writes "N_aspirational=12" -- correct
  for C-01, but the prior value (10) is absent and the column structure is absent. A one-sided
  entry is visible as a structural gap by column scan. Prevention through structure, not memory.

**1d. BILATERAL SYMMETRY AUDIT SWEEP (Phase 1 exit)**

  | Comparison | Symmetric? |
  |------------|-----------|
  | N_aspirational (formula denominator) | [YES -- Prior: 10 (v5), Current: 12 (v6) | NO -- [missing side] | PARTIAL -- N/A declared] |
  | Regression verdicts | [YES -- Prior: [verdict], Current: [verdict] | NO | PARTIAL -- no prior data] |
  | Arithmetic discrepancies | [YES -- stated [X], computed [Y] | NO | PARTIAL -- no discrepancy found] |

Symmetric: NO requires remediation before Phase 2.

Required field after writing:

  Inertia (C-18): The SYMMETRIC DELTA REGISTER prevents asymmetric entries by column structure.
  This audit sweep provides an independent catch: a Symmetric: NO cell is visible by scanning
  the sweep table without reading register prose. An output can pass C-15 (both sides present
  through structural enforcement) while failing C-18 (no independent catch). Both are required.

**1e. CRITERION-INERTIA COVERAGE ASSERTION**

After 1d, confirm every scored criterion ID will appear in at least one Inertia label.

  Phase 1 coverage so far:
    C-01: covered -- "Inertia (C-01):" at 1a
    C-13: covered -- "Inertia (C-13, C-15):" at 1b
    C-15: covered -- "Inertia (C-15):" at 1c; also 1b
    C-18: covered -- "Inertia (C-18):" at 1d
    Remaining criteria deferred to Phase 2 (C-11, C-14, C-19 at MODEL CELL)
    and Phase 3 (C-09 at 3b; C-10, C-12 at 3a).
    C-02, C-03, C-04, C-05--C-08, C-16, C-17, C-20: covered through
    Phase 2 scoring mechanisms and synthesis section.

Required field after writing:

  Inertia (C-20): Bare "Inertia: [text]" satisfies C-17 (departure label present) but fails
  C-20 (criterion ID absent). Criterion-ID anchoring -- "Inertia (C-01):" not bare "Inertia:"
  -- makes coverage auditable: a reader verifies all scored criteria appear in at least one
  Inertia label by scanning labels, not by cross-referencing mechanisms to criteria. Without
  anchoring, departure labels explain but do not make criterion-coverage gaps visible.

PHASE 1 COMPLETE. All five sections written.

---

PHASE 2: SCORE EACH OUTPUT

**MODEL CELL + ENTRY LOCK (Phase 2 entry -- all elements before any verdict row)**

Write the following in sequence as the first Phase 2 action:

(1) Evidence (model):
  "from [output ID], [section or structural element]: [verbatim quote or structural observation
  that locates a specific feature in the output -- not a criterion restatement]"
  Locatability test: could a reader find the referenced feature using only this evidence text?
  YES: proceed. NO: rewrite before entering any verdict row.

(2) Required labeled field:

  Inertia (C-11, C-14): Without a model cell at Phase 2 entry, evidence cells default to
  criterion restatement -- "the output has a leaderboard" cannot locate any specific feature
  in any specific output. The model cell fires before the first verdict, establishing the
  evidence standard before any cell can establish a lower norm. A model cell deferred to
  mid-Phase-2 allows criterion restatement in earlier cells before the standard is visible.

(3) Binary gate declaration:

  ENTRY LOCK: no verdict row written before model cell. [Confirmed | Violated -- first verdict
  row appears at: ___]

  "Confirmed" if the model cell above is the first Phase 2 content written before any evidence
  row. "Violated -- first verdict row appears at: [location]" if any verdict row preceded the
  model cell. A "Violated" declaration earns C-14 FAIL but C-19 PASS (accurate reporting).

Required field after the gate declaration:

  Inertia (C-19): The ENTRY LOCK imperative ("no verdict row before model cell") prevents
  violations structurally and earns C-14 PASS. But the constraint is inferred from output
  order -- verifiable only by tracing which content came first. The binary gate declaration
  makes the constraint declared and scannable: "ENTRY LOCK: ... Confirmed" is verifiable by
  scanning a labeled field. C-14 (structural placement) and C-19 (declaration of placement)
  are separable properties of the same mechanism.

For each output:
  | ID | Criterion | Tier | Verdict | Evidence |
Include all criteria C-01 through C-20. No row blank.

After table:
  essential_pass = [count]
  recommended_pass = [count]
  aspirational_pass = [count]
  composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 12 * 10) = [result]
  Golden: YES | NO -- [reason]

---

PHASE 3: VERIFY

**3a. Arithmetic verification**

  Verification (output: [ID]):
    stated counts: E=[X]/5, R=[X]/3, A=[X]/12
    computed composite: ([X]/5 * 60) + ([X]/3 * 30) + ([X]/12 * 10) = [result]
    Matches stated score: YES | NO -- discrepancy: stated [X], computed [Y]

Required field:

  Inertia (C-12): "Verification performed" satisfies C-10 at PARTIAL. The "Matches stated
  score: YES | NO" field forces an explicit binary result, making errors visible even when
  the scorer is not specifically looking for them. Analogous to the ENTRY LOCK: structural
  verification (recomputing) is necessary but not sufficient; the binary declaration makes
  the result auditable by field scan.

If discrepancy found, update SYMMETRIC DELTA REGISTER Arithmetic row.

**3b. Regression section**

If prior data: "[Output] / [Criterion]: prior=[verdict], current=[verdict]"
If no prior data: "No prior round data -- regression analysis cannot be performed."

Required field:

  Inertia (C-09): Absent section indistinguishable from empty section. Required even when
  empty -- presence confirms the check was performed.

---

SYNTHESIS

Write the following sections in order.

**LEADERBOARD**

  | Rank | Output | Composite | Golden? |
  |------|--------|-----------|---------|

All N outputs ranked descending. Ties broken with stated rule or "tied -- no tiebreak applied."
"See scores above" does not satisfy C-06.

**EXCELLENCE SIGNALS**

For each criterion where one output clearly leads:
  Signal: [output ID] -- [criterion ID] -- [structural mechanism that produced the difference]

Generic rankings not accepted. If no outlier pair: state explicitly.

**FAILURE PATTERNS**

Required even when empty: "No failure patterns -- all criteria passed in at least one output."

**PER-OUTPUT SYNTHESIS NOTES**

One paragraph per output explaining structural score drivers. Not verdict counts -- the
mechanism.
