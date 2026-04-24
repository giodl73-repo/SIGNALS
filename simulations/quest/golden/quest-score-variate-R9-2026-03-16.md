# quest-score Variations -- Round 9 (v8 rubric, convergence confirmation)

**Skill**: quest-score
**Rubric**: v8-2026-03-16 (C-01--C-05 essential, C-06--C-08 recommended, C-09--C-24 aspirational)
**N_essential=5, N_recommended=3, N_aspirational=16**
**Date**: 2026-03-16
**Round**: 9

---

## Context: what informed this round

R8 scored five variations against the v8 rubric. V-05 (P+Q+R+U+V) was the champion at 99.6875.
The R8 scorecard closed with `"new_patterns": []` -- no excellence signals generated new criteria.

| Finding | R8 result | R9 implication |
|---------|-----------|----------------|
| V-05 (P+Q+R+U+V) champion at 99.6875 | Axis V (Partial-Reason Schema) was additive given U (+0.3125 from C-24 PARTIAL -> PASS) | V-05 carries forward as convergence confirmation target |
| C-09 PARTIAL across all R8 variations | No prior-round scorecard was provided; N/A rule correctly applied in all 5 outputs | Can C-09 PASS be achieved by structural change? Or is it purely an input availability issue? |
| No new patterns extracted | R8 found no excellence signals that would generate new rubric criteria | R9 must confirm same finding to satisfy dual-convergence rule |

**Dual convergence condition**: all scenarios pass AND no new excellence patterns emerge across
2 consecutive rounds. R8 = first round with no new patterns. R9 must confirm to close.

**What R9 variations must test:**

1. **C-09 structural gap (Axis X)**: Can the prompt architecture enable C-09 PASS when prior-round
   data IS available, without degrading any other criterion? A Phase 0 input-gate pattern that
   conditionally builds a PRIOR-ROUND REGISTER when data is present, and correctly invokes the N/A
   rule when absent, tests whether this criterion is STRUCTURALLY achievable or purely input-limited.

2. **Formula stability (Axis Y)**: A composite pre-derivation block placed before Phase 2 forces
   the scorer to compute the formula actively before scoring begins. Targets C-10 and C-04 stability:
   does explicit pre-commitment to the formula prevent denominator errors at composite computation?
   This is a Phase 1 addition that makes formula engagement visible, not just declared.

3. **Phrasing register stability (Axis Z)**: Replace PHASE/SECTION structural labels with numbered
   checklist steps and second-person imperatives ("Record:", "Confirm:", "Verify:") while preserving
   all structural mechanisms and Inertia labels. If phrasing register change causes any criterion to
   degrade, it signals an implicit format dependency in the rubric that should be made explicit.
   Predicts identical verdicts to same-base variations.

**Variation axes explored this round:**

| Code | Axis | Target criterion | Hypothesis |
|------|------|-----------------|-----------|
| X | PRIOR-ROUND INPUT GATE -- Phase 0 added before Phase 1. Conditionally reads a prior-round scorecard when provided as input; builds a PRIOR-ROUND REGISTER with per-output, per-criterion verdicts. Regression section at 3b references the register. When no prior-round file is provided, Phase 0 writes the N/A declaration explicitly. | C-09 | Named Phase 0 gate converts C-09 from a structural input limit into a conditional PASS. When prior data is available, C-09 PASS achievable. When absent, the explicit N/A declaration is more informative than the bare "No prior round data" sentence. C-09 PARTIAL (without prior data in scoring run). All other criteria unchanged from simple base. |
| Y | COMPOSITE PRE-DERIVATION BLOCK -- placed at Phase 1 exit (after 1d, before Phase 2). The block pre-derives the composite formula range using the v8 parameters: maximum contribution, Golden threshold minimum, and what aspirational count achieves Golden given full essential and recommended pass. Forces formula engagement before scoring begins. | C-04, C-10 | Pre-derivation makes the /16 denominator active in the scorer's working context before the first verdict row is written. If any single-axis variation achieves C-10 or C-04 at higher confidence than the baseline (scored output shows zero arithmetic errors), this is a finding. No criterion from FAIL -> PASS predicted: C-04/C-10 already PASS at simple base. |
| Z | PHRASING REGISTER -- all structural labels preserved, imperative phrasing throughout. PHASE 1: becomes "Step 1:". Inertia labels preserved verbatim. MODEL CELL preserved. ENTRY LOCK preserved. All Inertia label criterion-ID format unchanged. Scoring table, composite formula, and synthesis sections identical in content, rewritten in second-person imperative style. | stability | Stability test: no criterion should degrade when phrasing changes but structure is preserved. If any criterion degrades (e.g., C-17 FAIL because "Inertia (C-XX):" label is syntactically renamed), that is a finding: the rubric has a latent format dependency. Predicts identical verdicts to V-01 (same structural content, different phrasing register). |

Single-axis: V-01 (X), V-02 (Y), V-03 (Z).
Minimum champion+X: V-04 (P+Q+R+U+V+X).
Convergence confirmation: V-05 (P+Q+R+U+V, R8 champion verbatim).

**Predicted outcomes (v8 rubric, N_aspirational=16, no prior-round data in scoring run):**

| Criterion | V-01 (X) | V-02 (Y) | V-03 (Z) | V-04 (P+Q+R+U+V+X) | V-05 (P+Q+R+U+V) |
|-----------|----------|----------|----------|---------------------|------------------|
| C-01--C-08 | PASS | PASS | PASS | PASS | PASS |
| C-09 | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| C-10--C-13 | PASS | PASS | PASS | PASS | PASS |
| C-14 | PASS | PASS | PASS | PASS | PASS |
| C-15--C-18 | PASS | PASS | PASS | PASS | PASS |
| C-19 | PARTIAL | PARTIAL | PARTIAL | PASS | PASS |
| C-20 | PARTIAL | PARTIAL | PARTIAL | PASS | PASS |
| C-21 | FAIL | FAIL | FAIL | PASS | PASS |
| C-22 | FAIL | FAIL | FAIL | PASS | PASS |
| C-23 | PARTIAL | PARTIAL | PARTIAL | PASS | PASS |
| C-24 | PARTIAL | PARTIAL | PARTIAL | PASS | PASS |

Note on C-09: when prior-round data IS provided as input to V-01 or V-04, Phase 0 activates
the PRIOR-ROUND REGISTER path and C-09 PASS is achievable. Without prior data, C-09 PARTIAL
across all variations. R9 scoring assumes no prior data available -- same context as R8.

Note on V-02 vs V-01: the composite pre-derivation block (Axis Y) targets C-10/C-04, both
already at PASS in V-01. No composite increment predicted. This confirms non-additivity of Y
given the existing arithmetic verification structure.

Note on V-03: phrasing register change predicts identical verdicts to V-01 (same structural
base, different imperative style). Any deviation from V-01's predicted verdicts is a finding.

**Predicted composite scores:**

```
V-01 (X):       A: 0.5+1+1+1+1+0.5+1+1+1+1+0.5+0.5+0+0+0.5+0.5 = 11.0/16
  composite = 60 + 30 + (11.0/16 * 10) = 96.875

V-02 (Y):       A: same as V-01 = 11.0/16
  composite = 60 + 30 + (11.0/16 * 10) = 96.875

V-03 (Z):       A: same as V-01 = 11.0/16 (stability prediction -- any deviation is a finding)
  composite = 60 + 30 + (11.0/16 * 10) = 96.875

V-04 (P+Q+R+U+V+X): A: 0.5+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1 = 15.5/16
  composite = 60 + 30 + (15.5/16 * 10) = 99.6875

V-05 (P+Q+R+U+V): A: 0.5+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1 = 15.5/16
  composite = 60 + 30 + (15.5/16 * 10) = 99.6875
```

Key diagnostics this round provides:
- V-01 vs V-02: X and Y are non-additive with each other when both target already-PASS criteria
  (Y) vs PARTIAL criteria on different lifecycle phases (X). No incremental composite expected.
- V-01 vs V-03: phrasing stability test. Equal composites = format-agnostic rubric confirmed.
- V-04 vs V-05: X is non-additive given P+Q+R+U+V when no prior data is available. C-09 remains
  PARTIAL in both. V-04's advantage is CAPABILITY: when called with prior-round data, Phase 0
  enables C-09 PASS. This capability improvement is not visible in this run's composite.
- If all three single-axis variations score identically (96.875): confirms no hidden patterns in
  Axes X, Y, Z -- dual convergence confirmed.

---

## V-01: Axis X -- Prior-Round Input Gate

**Variation axis**: Lifecycle emphasis -- Phase 0 added before Phase 1. When a prior-round
scorecard is provided as input, Phase 0 reads it and builds a PRIOR-ROUND REGISTER that feeds
the regression section at 3b. When no prior-round file is provided, Phase 0 writes an explicit
N/A declaration, naming the N/A rule. All other phase structure is identical to the simple base.

**Hypothesis**: The most common C-09 failure mode is the absence of prior-round data, not a
structural failure to include a regression section. Axis X addresses the STRUCTURAL side of this
gap: by providing an explicit Phase 0 gate with a conditional path, the output produces a more
informative C-09 PARTIAL (one that explicitly names the N/A rule and why it applies) vs. a bare
"No prior round data" sentence. When prior data IS available, Phase 0 enables C-09 PASS. Without
prior data: C-09 PARTIAL. C-19 PARTIAL (ENTRY LOCK instruction, no binary field). C-20 PARTIAL
(criterion-ID anchoring demonstrated in templates but not universally required). C-21 FAIL (no 1e).
C-22 FAIL (no NON-ADDITIVITY ANALYSIS). C-23 PARTIAL (model cell exists, locatability instruction
but no binary template). C-24 PARTIAL (2-column bilateral audit, reason phrases advised not enforced).

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

PHASE 0: PRIOR-ROUND INPUT GATE

Before Phase 1, check whether a prior-round scorecard was provided as input to this scoring run.

IF a prior-round scorecard file is provided:
  Read it. For each scored output, extract per-criterion verdicts.

  Produce a PRIOR-ROUND REGISTER:

    | Output ID | Criterion ID | Prior verdict |
    |-----------|--------------|---------------|
    | [V-XX]    | [C-NN]       | PASS/PARTIAL/FAIL |

  After completing the register, write:
    PRIOR-ROUND REGISTER COMPLETE -- [N] outputs, [M] criterion-output pairs recorded.

  The regression section at 3b will compare current verdicts against this register.

IF no prior-round scorecard was provided:
  Write: "No prior-round file provided. C-09 N/A rule applies: the regression section at 3b
  will report 'No prior round data -- regression analysis cannot be performed.' This earns
  C-09 PARTIAL, not FAIL -- the section is present and the N/A rule is correctly applied."

Proceed to Phase 1 regardless of prior-round availability.

After completing Phase 0, write this required labeled field:

  Inertia (C-09): Without the Phase 0 gate, a scorer who finds no prior data either omits the
  regression section (C-09 FAIL) or writes a bare "No prior round data" sentence that is
  structurally indistinguishable from a section that was skipped. The explicit N/A declaration
  in Phase 0 makes the absence-of-data condition named and auditable.

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

  Inertia (C-13, C-15): "N_aspirational=16" passes C-01 but fails C-15 -- the prior value (14)
  is absent. Both sides of every delta comparison are required to confirm the transition was
  registered, not just the current endpoint loaded.

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

IF PRIOR-ROUND REGISTER COMPLETE (from Phase 0):
  Compare each current verdict against the prior verdict from the PRIOR-ROUND REGISTER.
  For any criterion-output pair where the current verdict is lower than the prior verdict:
    "[Output ID] / [Criterion ID]: prior=[verdict], current=[verdict]"
  If no regressions: "No regressions -- all prior-round PASS or PARTIAL verdicts maintained."

IF no prior-round data was available (Phase 0 N/A rule applied):
  "No prior round data -- regression analysis cannot be performed."

After writing, write this required labeled field:

  Inertia (C-09): Section required even when empty. An absent section is structurally
  indistinguishable from a section with no regressions found.

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

Generic rankings are not excellence signals. If no outlier pair: state explicitly.

**FAILURE PATTERNS**

Required even when empty: "No failure patterns -- all criteria passed in at least one output."

**REGRESSION SIGNALS**

If prior data: named regressions with output ID, criterion ID, prior and current verdict.
If no prior data: "No prior round data; regression analysis not possible."

**PER-OUTPUT SYNTHESIS NOTES**

One paragraph per output explaining structural score drivers. Explain the mechanism, not
the verdict counts.

---

## V-02: Axis Y -- Composite Pre-Derivation Block

**Variation axis**: Lifecycle emphasis -- a COMPOSITE RANGE PRE-DERIVATION block is added
at Phase 1 exit (after 1d, before Phase 2 begins). The block uses v8 formula parameters to
compute: (1) the maximum possible composite, (2) the minimum aspirational contribution needed
for Golden given full essential and recommended pass, (3) the minimum aspirational pass count
needed for a composite >= 80. No other structural changes from the simple base.

**Hypothesis**: Pre-derivation makes the /16 denominator an active working value before the
first verdict row is written, reducing formula version errors. C-10 and C-04 are already at
PASS with the simple base, so no composite increment is expected. The pre-derivation block
is a prevention mechanism at Phase 1 exit (adding a third Phase 1 mechanism after register and
audit), which may strengthen C-16 at PARTIAL -> PASS (Phase 1 exit is a third distinct
enforcement point). If C-16 is already PASS, no change. C-19 PARTIAL, C-21/C-22 FAIL,
C-23/C-24 PARTIAL -- same as V-01. Predicted composite: same as V-01 (96.875).

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

PHASE 1: LOAD, DELTA REGISTER, BILATERAL AUDIT, AND FORMULA PRE-DERIVATION

Before scoring any output, complete sections 1a through 1e in order. Do not proceed to
Phase 2 until all five sections are written and the bilateral audit shows no Symmetric: NO rows.

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
  rows and computes all composites using /14 -- both errors invisible until Phase 3.

**1b. Formula version delta**

  Formula version delta: N_aspirational changed from [prior value] to [current value] in v[N].

If prior unknown: "No prior version delta detectable -- scoring under v8 as the baseline version."

After writing, write this required labeled field:

  Inertia (C-13, C-15): "N_aspirational=16" passes C-01 but fails C-15. Prior value (14) must
  be named. Both sides required to confirm the transition was registered, not just the endpoint.

**1c. SYMMETRIC DELTA REGISTER**

  | Comparison type | Prior state | Current state |
  |-----------------|-------------|---------------|
  | N_aspirational (formula denominator) | [prior -- e.g., "14 (v7)"] | [current -- e.g., "16 (v8)"] |
  | Regression verdicts | [prior or "No prior-round data -- row N/A"] | [current or "--"] |
  | Arithmetic discrepancies | [stated or "No discrepancy -- row N/A"] | [computed or "--"] |

Blank Prior State = structural violation.

After writing, write this required labeled field:

  Inertia (C-15): Two-column structure makes prior-state omission detectable by column scan.

**1d. BILATERAL SYMMETRY AUDIT SWEEP (Phase 1 audit)**

  | Comparison | Symmetric? |
  |------------|-----------|
  | N_aspirational | [YES -- Prior: [v], Current: [v] | NO -- [missing] | PARTIAL -- N/A declared] |
  | Regression verdicts | [YES | NO -- [missing] | PARTIAL] |
  | Arithmetic discrepancies | [YES | NO -- [missing] | PARTIAL] |

Symmetric: NO requires remediation before Phase 2.

After writing, write this required labeled field:

  Inertia (C-18): Register prevents asymmetric entries by column structure. Sweep catches them
  independently. Both are required: prevention and catch at the same phase.

**1e. COMPOSITE RANGE PRE-DERIVATION**

Before Phase 2 begins, compute the formula range using v8 parameters. Write in your output:

  FORMULA PRE-DERIVATION (v8 active)
  N_essential=5, N_recommended=3, N_aspirational=16
  Maximum composite: (5/5 * 60) + (3/3 * 30) + (16/16 * 10) = 100
  Golden threshold: all 5 essentials PASS AND composite >= 80
  Golden with zero aspirational PASS: (5/5 * 60) + (3/3 * 30) + (0/16 * 10) = 90 -- above 80
  Golden with partial aspirational: achievable with any aspirational count >= 0 if all E+R pass
  Minimum aspirational count for Golden when E=5/5, R=3/3: 0 (since 90 >= 80)
  Minimum aspirational count for Golden when E=5/5, R=2/3: need >= 10 points from A;
    (2/3 * 30) = 20; need >= 10 from A; 10/10 = 1.0; aspirational_pass >= 1.6 -- 2 PASS needed

This block is informational. It does not replace the arithmetic verification at 3a, which
re-derives the composite for a specific output after scoring.

After writing, write this required labeled field:

  Inertia (C-04, C-10): Pre-derivation forces active engagement with /16 before any verdict
  row is written. A scorer who skips may write /14 in the composite formula, producing an error
  that is visible only at 3a -- after all verdicts have been written. The pre-derivation fires
  at Phase 1 exit, before any scoring, when the error can be caught by comparison to 1b delta.

PHASE 1 COMPLETE. Proceed to Phase 2 only after 1a, 1b, 1c, 1d, and 1e are written and no
Symmetric: NO row remains in 1d.

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
  criterion restatement. The model cell fires before the first verdict row, setting the
  evidence standard before any cell can establish a lower norm.

ENTRY LOCK: do not write any verdict row until the model cell is written and passes the
locatability test. A verdict row written before the model cell is a Phase 2 protocol violation.

For each output, produce a scoring table:

  | ID | Criterion | Tier | Verdict | Evidence |

Column rules:
  - Verdict: PASS | PARTIAL | FAIL only.
  - Evidence: must quote, paraphrase with location, or name a specific structural feature.
    Criterion restatement is not evidence.
  - No row blank or missing. Include rows for all criteria C-01 through C-24.

After the scoring table, write the composite using the formula confirmed in 1e:

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

All N outputs ranked descending. Ties noted explicitly with tiebreak rule or
"tied -- no tiebreak applied." "See scores above" does not satisfy C-06.

**EXCELLENCE SIGNALS**

Signal: [output ID] -- [criterion ID] -- [structural mechanism producing the difference]

Generic rankings are not excellence signals. If no outlier pair: state explicitly.

**FAILURE PATTERNS**

Required even when empty: "No failure patterns -- all criteria passed in at least one output."

**REGRESSION SIGNALS**

If prior data: named regressions. If no prior data: "No prior round data; regression analysis
not possible."

**PER-OUTPUT SYNTHESIS NOTES**

One paragraph per output on structural score drivers. Explain the mechanism, not the counts.

---

## V-03: Axis Z -- Phrasing Register (Stability Test)

**Variation axis**: Phrasing register -- all structural PHASE/SECTION headers replaced with
numbered checklist steps ("1. Load and register", "2. Formula delta"). All structural mechanisms,
all Inertia labeled fields, all table schemas, all criterion-ID formats, and all enforcement rules
are preserved verbatim. Only the surrounding imperative phrasing changes: "Produce a block" ->
"Record:", "Write the following elements" -> "Write:", "Provide" -> "State:".

**Hypothesis**: No criterion should degrade when the phrasing register changes but the structural
content is identical. C-17 requires Inertia labels -- these are preserved. C-11 requires a model
cell -- this is preserved. C-19 requires an ENTRY LOCK -- this is preserved (as an instruction, no
binary field). The question: does any rubric criterion implicitly depend on PHASE-labeled syntax
rather than structural content? Predicted: identical verdicts to V-01. Any deviation from this
prediction is a finding about latent format dependencies in the rubric.

---

You are running quest-score against the v8 rubric.

quest-score scores N skill outputs against a rubric. Each output receives a per-criterion
verdict (PASS | PARTIAL | FAIL) with specific evidence, a composite score computed from
the rubric formula, and a golden-threshold determination. The final scorecard includes a
ranked leaderboard, excellence signals, failure patterns, and regression signals.

---

READ BEFORE ANY COMPUTATION

The v8 rubric changes the aspirational denominator from the v7 value:
  N_aspirational: 14 (v7) -> 16 (v8)

Use this formula:
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 16 * 10)

  PARTIAL = 0.5. FAIL = 0. Golden: all 5 essentials PASS AND composite >= 80.

Do not use /14 or any prior denominator.

---

STEP 1: LOAD

1. Record a load block naming:
   (a) all criteria IDs with tier labels (C-01--C-05 essential, C-06--C-08 recommended,
       C-09--C-24 aspirational)
   (b) the composite formula text with /16 denominator
   (c) the golden threshold (all 5 essentials PASS AND composite >= 80)
   (d) the count and list of outputs being scored

   Then record:

   Inertia (C-01): Without this block, criteria count (24), denominator (/16), and threshold
   are unverified. A scorer who skips produces a matrix missing C-23 and C-24 and computes
   composites using /14 -- both invisible until Step 4 verification.

---

STEP 2: DELTA REGISTER AND AUDIT

2. State the formula version delta:

   Formula version delta: N_aspirational changed from [prior] to [current] in v[N].

   If unknown: "No prior version delta detectable -- scoring under v8 as baseline."

   Then record:

   Inertia (C-13, C-15): Stating only "N_aspirational=16" satisfies C-01 but not C-15.
   Both the prior value (14) and the current value (16) are required.

3. Fill the symmetric delta register:

   | Comparison type | Prior state | Current state |
   |-----------------|-------------|---------------|
   | N_aspirational  | [prior]     | [current]     |
   | Regression verdicts | [prior or "No prior-round data -- row N/A"] | [current or "--"] |
   | Arithmetic discrepancies | [stated or "No discrepancy -- row N/A"] | [computed or "--"] |

   Blank prior state = structural violation.

   Then record:

   Inertia (C-15): Two-column structure makes prior-state omission a visible gap by scan.

4. Run the bilateral symmetry audit:

   | Comparison | Symmetric? |
   |------------|-----------|
   | N_aspirational | [YES | NO -- [missing] | PARTIAL -- N/A declared] |
   | Regression verdicts | [YES | NO | PARTIAL] |
   | Arithmetic discrepancies | [YES | NO | PARTIAL] |

   Symmetric: NO requires remediation before Step 3 (scoring).

   Then record:

   Inertia (C-18): Register prevents asymmetric entries by column structure. Audit catches
   them independently. Both required: prevention and catch at the same step.

Proceed to Step 3 only after items 1--4 are complete and no Symmetric: NO row remains.

---

STEP 3: SCORE EACH OUTPUT

5. Before any verdict row, write a model evidence cell:

   Evidence (model): "from [output ID], [section]: [verbatim quote or structural observation --
   not a criterion restatement]"

   Locatability test: YES -- proceed. NO -- rewrite before any verdict row.

   Then record:

   Inertia (C-11, C-14): Model cell must be the first scoring content. Without it, evidence
   cells default to criterion restatement. Placement at entry prevents the norm from being
   set by a lower-quality cell.

   ENTRY LOCK: do not write any verdict row until the model cell is written and locatability
   test passes. A verdict row before the model cell is a protocol violation.

6. For each output, produce a scoring table:

   | ID | Criterion | Tier | Verdict | Evidence |

   Rules:
   - Verdict: PASS | PARTIAL | FAIL only.
   - Evidence: quote, paraphrase with location, or specific structural observation.
     Criterion restatement is not evidence.
   - No row blank. Include C-01 through C-24.

7. After each scoring table, compute the composite:

   essential_pass = [count; PARTIAL=0.5]
   recommended_pass = [count; PARTIAL=0.5]
   aspirational_pass = [count; PARTIAL=0.5]
   composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 16 * 10) = [result]
   Golden: YES -- all essentials PASS; composite >= 80 | NO -- [reason]

   Complete all N outputs before Step 4.

---

STEP 4: VERIFY

8. Verify one output's composite:

   Verification (output: [ID]):
     stated counts: E=[X]/5, R=[X]/3, A=[X]/16
     computed: ([X]/5*60) + ([X]/3*30) + ([X]/16*10) = [result]
     Matches stated score: YES | NO -- discrepancy: stated [X], computed [Y]

   Then record:

   Inertia (C-12): "YES | NO" binary field required. Narrative does not satisfy C-12.

9. Regression section:

   If prior data: "[Output ID] / [Criterion ID]: prior=[verdict], current=[verdict]"
   If no prior data: "No prior round data -- regression analysis cannot be performed."

   Then record:

   Inertia (C-09): Section required even when empty.

---

STEP 5: SYNTHESIZE

Write the following sections:

LEADERBOARD

  | Rank | Output | Composite | Golden? |

All N outputs ranked descending. Ties noted explicitly.

EXCELLENCE SIGNALS

  Signal: [output ID] -- [criterion ID] -- [structural mechanism]

Generic rankings are not excellence signals. If none: state explicitly.

FAILURE PATTERNS

Required when empty: "No failure patterns -- all criteria passed in at least one output."

REGRESSION SIGNALS

If prior data: named regressions. If none: "No prior round data; regression analysis not possible."

PER-OUTPUT SYNTHESIS NOTES

One paragraph per output. Explain structural score drivers, not verdict counts.

---

## V-04: Axes P+Q+R+U+V+X -- R8 Champion Plus Prior-Round Input Gate

**Variation axis**: Combination -- the R8 champion (P+Q+R+U+V) with Axis X (PRIOR-ROUND INPUT
GATE at Phase 0) added. Tests whether X is additive given P+Q+R+U+V when no prior-round data is
available. The champion carries C-19 PASS (binary ENTRY LOCK), C-20 PASS (criterion-ID anchoring
rule), C-21 PASS (1e COVERAGE ASSERTION), C-22 PASS (NON-ADDITIVITY ANALYSIS), C-23 PASS (binary
locatability assertion field), C-24 PASS (Reason column in bilateral audit). Axis X adds Phase 0.

**Hypothesis**: X is non-additive given P+Q+R+U+V when no prior-round data is available in this
scoring run -- C-09 remains PARTIAL because Phase 0 correctly applies the N/A rule. V-04 and V-05
composite scores are equal (99.6875). V-04's advantage is STRUCTURAL CAPABILITY: when called with
a prior-round scorecard, Phase 0 activates the PRIOR-ROUND REGISTER path and enables C-09 PASS.
This capability improvement is not visible in the composite for a run without prior data.

The 1e COVERAGE ASSERTION is updated to include C-09 with coverage path: "Inertia (C-09): at
Phase 0 (N/A declaration) and at 3b regression section."

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

PHASE 0: PRIOR-ROUND INPUT GATE

Check whether a prior-round scorecard was provided as input.

IF provided:
  Read it. For each scored output, extract per-criterion verdicts.

  PRIOR-ROUND REGISTER:

    | Output ID | Criterion ID | Prior verdict |
    |-----------|--------------|---------------|
    | [V-XX]    | [C-NN]       | PASS/PARTIAL/FAIL |

  After completing: PRIOR-ROUND REGISTER COMPLETE -- [N] outputs, [M] pairs recorded.
  The regression section at 3b uses this register.

IF not provided:
  "No prior-round file provided. C-09 N/A rule applies."

After writing:

  Inertia (C-09): Without Phase 0, a scorer who finds no prior data either omits the regression
  section (FAIL) or writes a bare sentence that is indistinguishable from a skipped section.
  Phase 0 makes the absence-of-data condition explicit and auditable before Phase 1 begins.

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
  rows and computes all composites using /14 -- both errors invisible until Phase 3.

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
  A scorer writing only "N_aspirational=16" produces a visible blank in Prior State.

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
  indistinguishable between a correctly-applied N/A rule, a clean result, and a silently-skipped
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
  | C-09 | DEFERRED | Covered by Phase 0 N/A declaration and regression section at 3b |
  | C-02, C-03, C-04, C-05, C-06, C-07, C-08, C-16, C-17, C-22 | DEFERRED | Covered by Phase 2 scoring and synthesis mechanisms |

For any criterion not appearing: add it to DEFERRED with intended coverage location. Criteria
absent from all rows is a coverage gap.

After writing, write this required labeled field:

  Inertia (C-20, C-21): Bare "Inertia: [text]" satisfies C-17 but fails C-20 -- no criterion
  ID. C-21 requires this phase-boundary assertion: total inertia-label coverage confirmable
  by reading one table, not by scanning every label in the output.

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

IF PRIOR-ROUND REGISTER COMPLETE:
  Compare each current verdict against the prior verdict.
  "[Output ID] / [Criterion ID]: prior=[verdict], current=[verdict]" for any degradation.
  If no regressions: "No regressions -- all prior-round verdicts maintained or improved."

IF no prior-round data:
  "No prior round data -- regression analysis cannot be performed."

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

For each pair of variations where one uses a strict subset of the other's axes:
  Increment = variation_with_more_axes.composite - variation_with_fewer_axes.composite

For any pair where Increment = 0:

  Redundant axis: [name]
  Criterion target: [criterion]
  Subsuming mechanism: [specific mechanism in the other axis that performs the same function]

All three fields are required. Zero-increment declaration without subsuming mechanism = PARTIAL on C-22.

If no zero-increment pair: "No non-additivity observed -- all axes produced positive increment."
If single variation scored: "Single variation scored -- non-additivity analysis not applicable."

Required: this section must appear whether or not non-additivity is observed. Omitting = C-22 FAIL.

**REGRESSION SIGNALS**

If prior data: named regressions. If no prior data: "No prior round data; regression analysis
not possible."

**PER-OUTPUT SYNTHESIS NOTES**

One paragraph per output on structural score drivers. Explain the mechanism, not the counts.

---

## V-05: Axes P+Q+R+U+V -- R8 Champion (Convergence Confirmation)

**Variation axis**: Convergence confirmation -- the R8 champion prompt (V-05 from R8,
axes P+Q+R+U+V) reproduced verbatim. This variation is unchanged from R8 to confirm that:
(1) the prompt is stable -- R9 scoring produces the same verdicts as R8 scoring, (2) no new
excellence patterns have emerged from the R9 round's single-axis tests, and (3) the dual
convergence condition is met: R8 found no new patterns, R9 finding no new patterns closes.

**Hypothesis**: V-05 scores 99.6875 (C-09 PARTIAL, all others PASS). No criterion degrades
from R8 verdicts. No new output-criterion pair emerges as an excellence signal from R9's
single-axis variations that would require a new rubric criterion. DUAL CONVERGENCE ACHIEVED.

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
  rows and computes all composites using /14 -- both errors invisible until Phase 3.

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
  indistinguishable between a correctly-applied N/A rule, a clean result, and a silently-skipped
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
  this phase-boundary assertion: total inertia-label coverage confirmable by reading one table,
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

For each pair of variations where one uses a strict subset of the other's axes:
  Increment = variation_with_more_axes.composite - variation_with_fewer_axes.composite

For any pair where Increment = 0:

  Redundant axis: [name]
  Criterion target: [criterion]
  Subsuming mechanism: [specific mechanism in the other axis that performs the same function]

All three fields are required. Zero-increment declaration without subsuming mechanism = PARTIAL on C-22.

If no zero-increment pair: "No non-additivity observed -- all axes produced positive increment."
If single variation scored: "Single variation scored -- non-additivity analysis not applicable."

Required: this section must appear whether or not non-additivity is observed.

**REGRESSION SIGNALS**

If prior data: named regressions. If no prior data: "No prior round data; regression analysis
not possible."

**PER-OUTPUT SYNTHESIS NOTES**

One paragraph per output on structural score drivers. Explain the mechanism, not the counts.
