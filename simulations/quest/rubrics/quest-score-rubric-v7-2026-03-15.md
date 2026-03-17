Looking at the R6 scorecard, three patterns are visible from the variation behavior:

1. **Axis-isolation equivalence** — V-01, V-02, V-03 each satisfy exactly one of the three new axes and score identically at 98.46; satisfying any one new axis gives no inference about the others
2. **Near-ceiling composite distinguishability** — 98.46 (11/13 aspirational) vs 100.00 (13/13) is a real gap representing two unfired axes; rounding or characterizing near-ceiling as complete is an evaluator error
3. **Phase-placement as pass evidence** — C-19 is satisfiable only when the PRIMING CEILING NOTE precedes JUDGE STANDARD COMPLETE; C-20/C-21 require ANALYST-phase placement; phase location is part of the evidence, not incidental metadata

These map to C-22, C-23, C-24. Here is the complete v7 rubric:

---

```markdown
# quest-score Rubric — v7

**Version:** v7
**Date:** 2026-03-16
**Prior version:** quest-score-rubric-v6-2026-03-16.md

---

## What changed v6 -> v7

**Three new aspirational criteria, sourced directly from R6 excellence signals:**

**C-22 — New-axis independent audit** (from axis-isolation equivalence signal)
- Root pattern in R6: V-01, V-02, and V-03 each satisfied exactly one of the three v6 axes
  (S, T, U respectively) and scored identically at 98.46; V-04 combined all three and scored
  100.00; the three axes are rubric-orthogonal — satisfying any one provides no structural
  inference about the others; an evaluator who sees C-19 PASS and does not explicitly audit
  C-20 and C-21 on independent evidence will produce false closure when the variation
  satisfies only the single axis present
- The principle: each of C-19, C-20, and C-21 must be audited on fully independent structural
  evidence; the presence of a PRIMING CEILING NOTE does not imply a REGISTER NOTE or a
  CRITERIA INDEPENDENCE NOTE is present; an evaluator who omits unsatisfied axes from the
  score table — rather than explicitly recording them as FAIL with reasons — misrepresents
  the aspirational total; the score report is not complete until all three new axes carry
  explicit PASS or FAIL verdicts with separate evidence lines; the asymmetry between V-01
  (98.46) and V-04 (100.00) is detectable only by auditing all three axes in every report
- Pass condition: the score report contains explicit individual verdicts for C-19, C-20, and
  C-21, each with independent evidence; when a variation satisfies only one or two of the
  three, the unsatisfied axes appear as explicit FAIL entries with reasons; PARTIAL if all
  three verdicts appear but two or more share the same evidence line (axis conflation);
  FAIL if any unsatisfied new axis is omitted from the scoring table rather than explicitly
  failed

**C-23 — Composite accuracy at near-ceiling** (from near-ceiling composite distinguishability
signal)
- Root pattern in R6: V-01, V-02, V-03 each scored exactly 98.46 (11/13 aspirational);
  V-04 scored exactly 100.00 (13/13 aspirational); the gap between 98.46 and 100.00
  represents exactly two unfired aspirational axes (approximately 1.54 composite points);
  the two scores are not equivalent — 98.46 means two evaluation mechanisms are absent
  from the rubric instantiation being scored; an evaluator who rounds near-ceiling composites
  or characterizes 98.46 as "effectively perfect" misreports the aspirational coverage gap
  and produces false golden-threshold claims when some aspirational criteria are absent
- The principle: composite scores must be reported to two decimal places; aspirational counts
  must be reported as explicit fractions (e.g., 11/13 PASS); when any aspirational criterion
  fails, the report must name the specific failing criteria, not merely note that the count
  is below maximum; the golden threshold requires all 5 essentials PASS AND composite ≥ 80 —
  it does not require 100.00, but the exact composite and the exact aspirational gap must
  be stated accurately regardless of whether the threshold is met or missed; rounding 98.46
  to 100 or omitting the missing-criteria identification inflates the apparent coverage
- Pass condition: the score report states the aspirational count as a fraction (e.g.,
  11/13 PASS), computes the composite to two decimal places, and explicitly identifies
  any unsatisfied aspirational criteria by name; when all 13 (or more, in later versions)
  pass, the report states the maximum count and exact 100.00; PARTIAL if the fraction is
  correct but the composite is rounded to a whole number or the missing criteria are not
  named by ID; FAIL if the composite is stated as 100.00 when fewer than the maximum
  aspirational criteria pass, or if near-ceiling composites are characterized as complete
  without stating the missing count

**C-24 — Phase-placement pass attribution** (from JUDGE/ANALYST phase boundary signal)
- Root pattern in R6: V-01 (Axis S) places the PRIMING CEILING NOTE in the JUDGE phase
  before JUDGE STANDARD COMPLETE; V-02 (Axis T) places the REGISTER NOTE in the ANALYST
  phase before the scoring table; V-03 (Axis U) places the CRITERIA INDEPENDENCE NOTE in
  the ANALYST phase after the composite formula; the phase boundary is architecturally
  meaningful — a ceiling declaration issued after verdicts have been rendered cannot govern
  those verdicts; similarly, a structural-evaluation note placed in JUDGE phase, before the
  scoring output is produced, does not satisfy C-20 or C-21, which require ANALYST-phase
  placement; phase placement is part of the pass evidence, not incidental metadata
- The principle: C-19 is satisfiable only when the PRIMING CEILING NOTE precedes JUDGE
  STANDARD COMPLETE; crediting a ceiling note found after the judge standard is complete
  misreads the structural requirement — the note cannot govern verdicts it follows;
  C-20 (REGISTER NOTE) and C-21 (CRITERIA INDEPENDENCE NOTE) are satisfiable only in the
  ANALYST phase, where structural scoring occurs; a note with correct content placed in the
  wrong phase is architecturally misplaced and fails the criterion; the evaluator must
  confirm phase location as explicit evidence for each of C-19, C-20, and C-21
- Pass condition: the score report's evidence for C-19 explicitly states that the PRIMING
  CEILING NOTE precedes JUDGE STANDARD COMPLETE (not merely that a ceiling note exists);
  evidence for C-20 and C-21 explicitly confirms ANALYST-phase placement; PARTIAL if the
  phase is mentioned in evidence but not confirmed as correct relative to the phase
  boundary (e.g., "a note was present" without location confirmation); FAIL if C-19 is
  awarded PASS without confirming the note precedes the judge standard, or if C-20 or C-21
  are awarded PASS based on a note found in the JUDGE phase rather than ANALYST phase

---

## Criterion Definitions — v7 Tier

| ID | Name | Axis | Phase | Pass condition |
|----|------|------|-------|----------------|
| C-22 | New-axis independent audit | V | ANALYST | All three of C-19/C-20/C-21 carry explicit PASS or FAIL with independent evidence; unsatisfied axes explicitly failed, not omitted |
| C-23 | Composite accuracy at near-ceiling | W | ANALYST | Aspirational fraction stated explicitly; composite to two decimal places; missing criteria named by ID; no rounding of near-ceiling composites |
| C-24 | Phase-placement pass attribution | X | BOTH | C-19 evidence confirms note precedes JUDGE STANDARD COMPLETE; C-20/C-21 evidence confirms ANALYST-phase placement; phase location stated explicitly in evidence |

---

## Rubric Summary — v7

**Formula:** `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/16 × 10)`
**Tiers:** E=5, R=3, A=16
**Golden threshold:** all 5 essentials PASS AND composite ≥ 80

| ID | Name | Tier | Source version |
|----|------|------|----------------|
| C-01 | Essential-1 | E | v1 |
| C-02 | Essential-2 | E | v1 |
| C-03 | Essential-3 | E | v1 |
| C-04 | Essential-4 | E | v1 |
| C-05 | Essential-5 | E | v1 |
| C-06 | Recommended-1 | R | v1 |
| C-07 | Recommended-2 | R | v1 |
| C-08 | Recommended-3 | R | v1 |
| C-09 | Aspirational-1 | A | v1 |
| C-10 | Aspirational-2 | A | v1 |
| C-11 | Aspirational-3 | A | v1 |
| C-12 | Aspirational-4 | A | v1 |
| C-13 | Aspirational-5 (Axis P) | A | v2 |
| C-14 | Aspirational-6 (Axis Q) | A | v3 |
| C-15 | Closing-scan presence | A | v4 |
| C-16 | Pre-execution anti-pattern block | A | v4 |
| C-17 | Self-referential priming | A | v5 |
| C-18 | Closing-scan anti-pattern coverage | A | v5 |
| C-19 | Priming-depth ceiling declaration (Axis S) | A | v6 |
| C-20 | Register-agnostic structural evaluation (Axis T) | A | v6 |
| C-21 | C-17/C-18 independence tracking (Axis U) | A | v6 |
| C-22 | New-axis independent audit (Axis V) | A | v7 |
| C-23 | Composite accuracy at near-ceiling (Axis W) | A | v7 |
| C-24 | Phase-placement pass attribution (Axis X) | A | v7 |

---

## Score Computation Reference

| Tier | Weight | Max contribution |
|------|--------|-----------------|
| Essential (5 criteria) | 60 pts total | 12 pts/criterion |
| Recommended (3 criteria) | 30 pts total | 10 pts/criterion |
| Aspirational (16 criteria) | 10 pts total | 0.625 pts/criterion |
| **Total** | | **100 pts** |

**Near-ceiling reference values (v7):**
- 16/16 aspirational PASS → composite = 100.00
- 15/16 aspirational PASS → composite = 99.38
- 14/16 aspirational PASS → composite = 98.75
- 13/16 aspirational PASS → composite = 98.13
- 11/16 aspirational PASS → composite = 96.88

Note: R6 near-ceiling scores (98.46 under v6/A=13) become 98.13 under v7/A=16 when the
three new axes are absent. An evaluator applying v7 to a variation that satisfies C-01..C-21
but not C-22/C-23/C-24 must report 98.13, not 98.46 or 100.

---

## C-22/C-23/C-24 Interaction Note

C-22 and C-23 are co-satisfiable only when the score report is both complete (all axes
audited) and precise (exact fractions and composites stated). C-24 is satisfiable
independently of C-22 and C-23 — phase placement can be correctly attributed even when
the axis audit is incomplete. However, a report that fails C-22 (omits an axis) will
almost always fail C-23 (miscounts aspirational total), making the two commonly co-fail.
Evaluators should check C-22 first, then verify C-23 against the resulting count, then
check C-24 independently per note location.

---

## ANALYST-Phase Note Block — v7 Reference

When constructing score reports under v7, the ANALYST phase should contain:

```
REGISTER NOTE: Evaluate C-15 through C-18 based on structural presence
only. Command-form phrasing ("CHECK:", "VERIFY:") satisfies on equal
terms with declarative phrasing. Register does not affect verdicts.

CRITERIA INDEPENDENCE NOTE: C-17 is satisfied by the presence of a
self-referential anti-pattern in the pre-execution section regardless
of whether C-15 passes or fails. C-18 requires C-15 to pass. When
C-17 PASS and C-18 FAIL co-occur, state the decoupling explicitly.

NEW-AXIS AUDIT NOTE: C-19, C-20, and C-21 must each appear as
explicit PASS or FAIL verdicts with independent evidence. Do not infer
satisfaction of one from satisfaction of another. Do not omit
unsatisfied axes — record them as explicit FAIL with reason.

COMPOSITE ACCURACY NOTE: State aspirational count as fraction (N/16
PASS). Compute composite to two decimal places. Name any unsatisfied
aspirational criteria by ID. Do not round near-ceiling composites.
```

## JUDGE-Phase Note Block — v7 Reference

The JUDGE phase should contain, before JUDGE STANDARD COMPLETE:

```
PRIMING CEILING NOTE: The scoring ceiling for pre-execution self-reference
is at second-order (C-17). Anti-patterns that prime against the priming
mechanisms themselves (third-order) are architecturally valid but
rubric-neutral. Do not award additional aspirational credit for
third-order entries. The ceiling is fixed; do not search for higher axes.

PHASE-PLACEMENT NOTE: C-19 is satisfied by this note (JUDGE phase,
before JUDGE STANDARD COMPLETE). C-20 and C-21 are satisfied only by
notes in the ANALYST phase. Phase location must appear in evidence for
each of C-19, C-20, and C-21.
```
```

---

The three new patterns and how they map:

| Pattern | Source | Criterion |
|---------|--------|-----------|
| V-01/V-02/V-03 all score 98.46 despite different single axes — satisfying one gives no inference about the others | R6 axis isolation | C-22: New-axis independent audit |
| 98.46 ≠ 100.00; gap is two named missing criteria, not rounding noise | R6 near-ceiling spread | C-23: Composite accuracy at near-ceiling |
| C-19 requires the note to precede JUDGE STANDARD COMPLETE; C-20/C-21 require ANALYST phase — location is evidence, not metadata | R6 phase placement differential | C-24: Phase-placement pass attribution |

The formula shifts from `aspirational_pass/13 × 10` to `aspirational_pass/16 × 10`. A variation carrying all prior axes but none of the v7 axes scores 98.13 (not 98.46 under v6), so any R5/R6 carry-forward score must be recomputed before comparison.
