# flow-throttle Variate — Round 8 Score (Rubric v7)
**Date:** 2026-03-15
**Rubric:** v7 (C-01 through C-25, denominator /17 aspirational)
**Baseline ceiling:** R7 V-05 = 100/100 under v7 (all 17 aspirational pass)
**Note:** A separate R8 file exists for rubric v22 (C-01–C-32). This file scores the v7 R8
variation set only.

---

## Scoring Basis

R7 V-05 established the 100/100 ceiling under v7 by carrying all three R7 axes simultaneously:
- C-23: VOLUME ARITHMETIC pre-computation block before TABLE A
- C-24: TIER-ID COVERAGE AUDIT matrix after full analysis
- C-25: `Without this change (at 2x nominal)` column + `Source` field in TABLE F

Each R8 variation **adds** new structural axes to the R7 V-05 base without removing any
existing structural elements. The scoring question for each variation is therefore:

1. Do the new additions preserve all 17 aspirational criteria?
2. Do any additions displace or compress existing structures that carry critical criteria?

All five variations predict 100. Risk analysis below documents the displacement test for each.

---

## V-01 — Mitigation Dependency Ordering

**Axis:** `Depends-on` column added to TABLE F. MITIGATION EXECUTION ORDER block added
immediately after TABLE F, before TIER-ID COVERAGE AUDIT.

**Displacement risk assessed:** `Depends-on` column widens TABLE F to 9 columns. Risk: the
`Without this change (at 2x nominal)` column (C-25) is compressed to accommodate width.
Mitigation in prompt: "`Depends-on` field is short (MR-ID or `--`) and informational only."
The column note explicitly distinguishes `Depends-on` from C-25 content — both are required.

**C-01 Bottleneck sequencing** — PASS. TABLE A + CASCADE SCENARIO retained; binding tier named.
**C-02 Backpressure propagation** — PASS. TABLE B two-hop minimum retained.
**C-03 UX per throttle tier** — PASS. TABLE C one-row-per-T-NN retained.
**C-04 Unprotected burst path** — PASS. TABLE D retained with absence-evidence requirement.
**C-05 Quantified limits** — PASS. TABLE A Limit column with number + unit retained.
**C-06 Retry-after handling** — PASS. RETRY-AFTER GAP ASSESSMENT section retained.
**C-07 Cascade failure scenario** — PASS. CASCADE SCENARIO three-tier minimum retained.
**C-08 Throttle tier matrix** — PASS. TABLE A scannable structure retained.
**C-09 Mitigation prescriptions** — PASS. TABLE F `Setting or API parameter` column retained;
  inline WRONG/PASS contrast retained; two-row minimum retained.
**C-10 Load shape sensitivity** — PASS. LOAD SHAPE COMPARISON UNIFORM vs BURST retained with
  numeric comparison requirement.
**C-11 Multi-volume sweep** — PASS. TABLE A three STATUS columns (1x/2x/5x) retained; inline
  flag "if all identical, VOLUME ARITHMETIC was not used" retained.
**C-12 Cross-section tier traceability** — PASS. T-NN convention enforced throughout; synonym
  prohibition retained.
**C-13 Test coverage gap identification** — PASS. TABLE E (implied from baseline) retained.
  MITIGATION EXECUTION ORDER adds dependency rationale that pre-loads causal chains for TABLE E
  `Structural reason` field — Q1 answer: yes, dependency edge rationale feeds C-13/C-15.
**C-14 Test infrastructure inertia catalog** — PASS. Stage 1 catalog preamble retained.
**C-15 Labeled gap entry completeness** — PASS. GAP-NN four-field template retained.
**C-16 Negative exemplar contrast injection** — PASS. WRONG/PASS contrast in test section and
  TABLE F column retained.
**C-17 Stage-boundary completion declaration** — PASS. "Stage 1 complete" gate retained.
**C-18 Load shape null-case grounding** — PASS. Null-case mechanism-citation requirement
  retained in LOAD SHAPE COMPARISON.
**C-19 Multi-section exemplar coverage** — PASS. Both section exemplars retained.
**C-20 Instruction-adjacent rationale annotation** — PASS. WHY-first register throughout
  retained; `The reason:` annotations adjacent to each enforcement instruction.
**C-21 Section-adjacent inertia callout placement** — PASS. Distributed inertia callouts at
  TABLE A, TABLE D, and STAGE 1 retained.
**C-22 Dual-role execution sequence** — PASS. ROLE 1 → ROLE 2 boundary declaration retained;
  ROLE 2 frames at least one finding as review of ROLE 1 output.
**C-23 Volume arithmetic pre-computation** — PASS. VOLUME ARITHMETIC block before TABLE A
  retained; unit-conversion requirement and STATUS annotation retained.
**C-24 Cross-section tier-ID coverage audit** — PASS. TIER-ID COVERAGE AUDIT section retained
  after MITIGATION EXECUTION ORDER. MITIGATION EXECUTION ORDER placed before audit as stated.
**C-25 Counterfactual harm column** — PASS. `Without this change (at 2x nominal)` column
  retained in TABLE F; `Source` column retained. Prompt explicitly distinguishes from new
  `Depends-on` column.

**Aspirational pass:** 17/17
**Composite:** 60 + 30 + (17/17 × 10) = **100**

**V-01 Q1 answer:** MITIGATION EXECUTION ORDER requires articulating dependency-edge rationale
("MR-03 depends on MR-01 because the retry policy determines what throttle signal the circuit
breaker sees"). This pre-loads the component → cause → effect causal chain that TABLE E
`Structural reason` entries require. C-13 and C-15 specificity improves as a consequence.

---

## V-02 — Quota Exhaustion Timeline

**Axis:** QUOTA EXHAUSTION PROJECTION section added between TABLE A and TABLE B. For each tier
at HIT or SAT at 2x nominal, computes time to full quota depletion using VOLUME ARITHMETIC 2x
arrival rate and the tier's window size.

**Displacement risk assessed:** QUOTA EXHAUSTION PROJECTION appears after TABLE A and before
TABLE B. Risk: tiers discovered during TABLE B are not projected (scope limited to TABLE A
tiers). Mitigation in prompt: "scope QUOTA section explicitly to tiers already present in
TABLE A." The section adds a computation pass after TABLE A — it does not reorder or remove
existing sections.

**C-23 Volume arithmetic pre-computation** — PASS. VOLUME ARITHMETIC still before TABLE A;
  QUOTA EXHAUSTION PROJECTION appears after TABLE A, using pre-computed rates. No displacement.
**C-24 Cross-section tier-ID coverage audit** — PASS. Coverage audit still at end of analysis.
  QUOTA EXHAUSTION PROJECTION adds a T-NN-referenced section — if the audit is comprehensive it
  will now include this section in its matrix. Net effect: richer coverage audit.
**C-25 Counterfactual harm column** — PASS. TABLE F structure unchanged.

All other criteria: PASS (same as V-01 — no displacement from new section).

**V-02 Q2 answer:** QUOTA EXHAUSTION PROJECTION grounds TABLE A `Failure visibility window`
entries in arithmetic. The computation (VOLUME ARITHMETIC 2x arrival rate × window size)
converts vague time-range assertions ("seconds to minutes") into computed depletion intervals.
C-11 STATUS columns at 2x become more precise, and C-23's arithmetic anchor is extended
downstream into a concrete timeline rather than stopping at rate-comparison.

**Aspirational pass:** 17/17
**Composite:** 60 + 30 + (17/17 × 10) = **100**

---

## V-03 — Burst Shape Sensitivity Matrix

**Axis:** LOAD SHAPE COMPARISON replaced by BURST SHAPE MATRIX testing three concentration
fractions: 20%, 10%, 5% of the window. Per-tier status at each concentration. Replaces
(does not extend) existing LOAD SHAPE COMPARISON.

**Displacement risk assessed:** LOAD SHAPE COMPARISON is where C-10 and C-18 are satisfied.
Replacement changes the comparison from UNIFORM vs one BURST to three BURST concentrations.
Assessment per criterion:

**C-10 Load shape sensitivity** — PASS. Pass condition: "demonstrates that the same total
request count produces different throttle outcomes depending on arrival shape, with at least
one numeric comparison grounded in cited rate limits." Three concentration fractions at fixed
total volume demonstrate exactly this: at 5% concentration (very spiky), per-second arrival
rate = total/(0.05 × window) — a rate that may exceed a per-second limit that 20% concentration
would not. The same total count produces different outcomes depending on arrival shape. The
"(uniform vs. spiky)" in the criterion description is an example form, not the only form;
the required property is shape-sensitive status difference. PASS.

**C-18 Load shape null-case grounding** — PASS. With three concentration fractions:
  - Positive case (C-18a): If any concentration fraction produces a different tier STATUS than
    another, the condition is met with a numeric comparison.
  - Null case (C-18b): If no tier STATUS changes across all three fractions, the output names
    the specific rate limit mechanism as the structural reason per concentration fraction. Three
    null cases each require a mechanism citation — richer than the single LOAD SHAPE null case.
  The BURST SHAPE MATRIX provides stronger C-18 coverage than the single LOAD SHAPE
  COMPARISON because it demands per-shape mechanism citations rather than a single shared
  explanation.

**V-03 Q3 answer:** BURST SHAPE MATRIX produces richer C-18 null-case grounding. Three shapes
without status transitions requires three per-shape mechanism citations rather than one generic
reason. The critical burst threshold (the concentration fraction at which the first tier
transitions from OK to HIT) becomes explicitly computable: it is the fraction at which
per-second arrival rate = limit. A single LOAD SHAPE COMPARISON produces a binary finding;
the matrix produces a threshold.

All other criteria: PASS (no existing structure removed).

**Aspirational pass:** 17/17
**Composite:** 60 + 30 + (17/17 × 10) = **100**

---

## V-04 — Combined: Mitigation Dependency Ordering + Quota Exhaustion Timeline

**Axes:** V-01 (TABLE F `Depends-on` + MITIGATION EXECUTION ORDER) + V-02 (QUOTA EXHAUSTION
PROJECTION after TABLE A). No BURST SHAPE MATRIX.

**Displacement risk assessed:** Cumulative cost of TABLE F width (V-01) + QUOTA section (V-02).
MITIGATION EXECUTION ORDER appears between TABLE F and TIER-ID COVERAGE AUDIT; QUOTA
EXHAUSTION PROJECTION appears between TABLE A and TABLE B. Neither removes existing sections.
The TIER-ID COVERAGE AUDIT may now include QUOTA EXHAUSTION PROJECTION in its matrix if the
prompt instructs the audit to cover all T-NN-referenced sections.

**C-24 Cross-section tier-ID coverage audit** — PASS. Coverage audit now covers one additional
  T-NN-referenced section (QUOTA EXHAUSTION PROJECTION). Net effect: audit becomes more
  comprehensive, not less.
**C-25 Counterfactual harm column** — PASS. `Without this change` column and `Source` field
  retained; `Depends-on` column is independent.

All 17 aspirational criteria: PASS.

**Aspirational pass:** 17/17
**Composite:** 60 + 30 + (17/17 × 10) = **100**

---

## V-05 — All Three Axes

**Axes:** V-01 (dependency ordering) + V-02 (quota projection) + V-03 (burst shape matrix).
Maximum structural density.

**Displacement risk assessed:** BURST SHAPE MATRIX is the most compressible element under
token pressure (large per-tier table), but it replaces rather than adds, keeping net cost
comparable. The primary token risk is the combination of:
- TABLE F now 9 columns wide (with `Depends-on`)
- QUOTA EXHAUSTION PROJECTION between TABLE A and TABLE B
- BURST SHAPE MATRIX (3-row per-tier structure) replacing LOAD SHAPE COMPARISON

C-10 and C-18 risk same as V-03: PASS by shape-sensitivity argument.
C-25 risk same as V-01: PASS by `Depends-on` column being short and informational.
C-23 risk: VOLUME ARITHMETIC must still appear before TABLE A, with QUOTA section after TABLE A.
  Prompt structure places VOLUME ARITHMETIC → TABLE A → QUOTA PROJECTION → TABLE B. C-23 PASS.

All 17 aspirational criteria: PASS.

**Aspirational pass:** 17/17
**Composite:** 60 + 30 + (17/17 × 10) = **100**

---

## Summary Scorecard

| Criterion | Tier | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|------|
| C-01 Bottleneck sequencing | essential | PASS | PASS | PASS | PASS | PASS |
| C-02 Backpressure propagation | essential | PASS | PASS | PASS | PASS | PASS |
| C-03 UX per tier | essential | PASS | PASS | PASS | PASS | PASS |
| C-04 Unprotected burst path | essential | PASS | PASS | PASS | PASS | PASS |
| C-05 Quantified limits | essential | PASS | PASS | PASS | PASS | PASS |
| C-06 Retry-after handling | recommended | PASS | PASS | PASS | PASS | PASS |
| C-07 Cascade failure scenario | recommended | PASS | PASS | PASS | PASS | PASS |
| C-08 Throttle tier matrix | recommended | PASS | PASS | PASS | PASS | PASS |
| C-09 Mitigation prescriptions | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-10 Load shape sensitivity | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-11 Multi-volume sweep | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-12 Cross-section tier traceability | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-13 Test coverage gap identification | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-14 Test infrastructure inertia catalog | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-15 Labeled gap entry completeness | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-16 Negative exemplar contrast | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-17 Stage-boundary completion | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-18 Load shape null-case grounding | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-19 Multi-section exemplar coverage | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-20 Instruction-adjacent rationale | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-21 Section-adjacent inertia callout | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-22 Dual-role execution sequence | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-23 Volume arithmetic pre-computation | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-24 Cross-section tier-ID coverage audit | aspirational | PASS | PASS | PASS | PASS | PASS |
| C-25 Counterfactual harm column | aspirational | PASS | PASS | PASS | PASS | PASS |
| **All essential pass** | | YES | YES | YES | YES | YES |
| **Aspirational pass** | | 17/17 | 17/17 | 17/17 | 17/17 | 17/17 |
| **Composite** | | **100** | **100** | **100** | **100** | **100** |

---

## Ranking

All five variations score 100. Under v7 the ceiling is flat — every combination of R8 axes
preserves the full 17-criteria suite. The ranking is therefore by **structural richness** and
**new patterns introduced**, not by score differential.

| Rank | Variation | Axes | Score | Structural contribution |
|------|-----------|------|-------|------------------------|
| 1 | V-05 | All three | 100 | Maximum structural density; all three action-readiness axes active |
| 2 | V-04 | Dep ordering + quota | 100 | Execution-plan + arithmetic timeline; closes TABLE F and TABLE A loop |
| 3 | V-01 | Dep ordering | 100 | Converts TABLE F from registry to sequenced execution plan |
| 4 | V-02 | Quota projection | 100 | Grounds TABLE A time-range entries in arithmetic |
| 5 | V-03 | Burst shape matrix | 100 | Elevates C-10 from point-sample to threshold-finding sensitivity sweep |

V-05 is the strongest variation by structural richness even though it is tied on score. V-03
introduces the most novel structural change (replacing a binary comparison with a sensitivity
sweep) and opens the clearest path to C-26 (critical burst threshold as a computable value).

---

## Excellence Signals

Three patterns from V-05 (top by richness) that contribute beyond the score:

**1. Dependency-explicit execution planning (V-01/V-04/V-05)**
The MITIGATION EXECUTION ORDER block requires articulating the causal reason for each
dependency edge: "MR-03 depends on MR-01 because the retry policy determines what throttle
signal the circuit breaker observes." This is the same component-cause-effect chain that TABLE E
`Structural reason` entries require. A model that has pre-stated the dependency rationale in
MITIGATION EXECUTION ORDER enters TABLE E with the causal vocabulary already in scope —
C-13/C-15 specificity improves as a side effect.

Pattern candidate for C-26: **Dependency-grounded mitigation sequencing** — the `Depends-on`
column + execution order block converts TABLE F into a risk-sequenced execution plan where
each row's prerequisite state is declared rather than inferred.

**2. Arithmetic-grounded quota timeline (V-02/V-04/V-05)**
QUOTA EXHAUSTION PROJECTION converts TABLE A `Failure visibility window` cells from qualitative
time-range assertions into arithmetic products: (quota remaining) / (2x arrival rate) = minutes
to depletion. C-11's 2x STATUS column gains a quantitative consequence beyond "SAT." C-23's
arithmetic anchor is extended downstream into a specific timeline rather than stopping at
rate-comparison. The reader sees not just that a tier SATs at 2x but when it becomes completely
unavailable.

Pattern candidate for C-27: **Timeline-grounded saturation analysis** — a depletion-time
computation for each HIT/SAT tier at 2x nominal, grounded in VOLUME ARITHMETIC, appended
immediately after TABLE A.

**3. Threshold-finding sensitivity sweep (V-03/V-05)**
BURST SHAPE MATRIX elevates C-10 from a binary (status changes yes/no) to a threshold-finding
structure: the critical concentration fraction is the smallest value at which the first tier
transitions from OK to HIT. This value is computable: it is the fraction such that
total_requests / (fraction × window) > tier_limit. The matrix produces an actionable number
rather than a qualitative finding. Three null cases each require an independent mechanism
citation, making C-18 grounding structurally richer than the single LOAD SHAPE null case.

Pattern candidate for C-28: **Critical burst threshold computation** — the concentration
fraction at which the first tier transitions status, derived from VOLUME ARITHMETIC and TABLE A
limit values, stated as an explicit threshold rather than a qualitative shape comparison.

---

## Round 8 → Round 9 Signal

Under v7, R8 axes produce no score differentiation — the ceiling was already flat at 100.
The structural value is in the three new patterns (C-26/C-27/C-28 candidates). Round 9 should:

1. **Elevate C-26 (dependency-grounded sequencing):** Add `Depends-on` column and MITIGATION
   EXECUTION ORDER as criteria. V-01/V-04/V-05 carry C-26; V-02 and V-03 do not.

2. **Elevate C-27 (timeline-grounded saturation):** Add QUOTA EXHAUSTION PROJECTION as a
   criterion for HIT/SAT tiers at 2x nominal. V-02/V-04/V-05 carry C-27; V-01 and V-03 do not.

3. **Elevate C-28 (critical burst threshold):** Add BURST SHAPE MATRIX or equivalent
   threshold-finding structure as a criterion. V-03/V-05 carry C-28; V-01, V-02, V-04 do not.

Predicted v8 rubric scores with C-26/C-27/C-28 added (denominator /20 aspirational):
- V-01: 17+1 = 18/20 → composite 99
- V-02: 17+1 = 18/20 → composite 99
- V-03: 17+1 = 18/20 → composite 99
- V-04: 17+2 = 19/20 → composite 99.5 → **99**
- V-05: 17+3 = 20/20 → composite **100**

100 remains achievable at V-05.
