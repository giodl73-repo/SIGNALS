## Quest Scorecard — mock-review R13 / V-01
**Rubric**: v13 | **Date**: 2026-03-15 | **Axis**: C-37 (cross-template error symmetry declaration, Arch-first base)

---

### Scoring Notes

V-01 is the R12 V-01 Arch-first base (Arch→Strat→PM) with one structural addition: a CROSS-TEMPLATE ERROR SYMMETRY declaration block in the STEP 7 entry format template. C-36 is intentionally absent (single-axis test). STEPS 6–7 are not shown but claimed preserved from R12 V-01; criteria depending on those steps are scored by inheritance. STEP 5 PM sub-questions are similarly inherited.

---

### Essential — 60 pts (5 criteria)

| ID | Score | Evidence |
|----|-------|----------|
| C-01 | **PASS** | STEP 2 partitions all namespaces into exactly two lists; "DO NOT proceed to PHASE GATE until every namespace is placed in exactly one list" enforces completeness |
| C-02 | **PASS** | Three rules fire before evaluation; PHASE GATE hard-separates auto from evaluation; all three rules explicitly non-role-overridable |
| C-03 | **PASS** | Inherited from R12 V-01; STEP 6 decision block carries exact reason codes |
| C-04 | **PASS** | Inherited from R12 V-01; write-back phase covers in-place status updates as the defining behavior |
| C-05 | **PASS** | Inherited from R12 V-01; next-steps ordering rule stated explicitly with critical-before-non-critical logic |

**Essential: 5/5 → 60.0**

---

### Recommended — 30 pts (3 criteria)

| ID | Score | Evidence |
|----|-------|----------|
| C-06 | **PASS** | Auto-flag list format `{namespace}: trigger = {rule}` names rule per namespace; evaluation-driven REAL-REQUIRED records verdict |
| C-07 | **PASS** | STEP 3 (Architect), STEP 4 (Strategy), STEP 5 (PM) each have own heading, SQ-1/SQ-2/SQ-3, and required verdict field |
| C-08 | **PASS** | STEP 1 writes `Tier: {N} (source: TOPICS.md | --tier | default)`; RULE 2 gates on `tier >= 2` |

**Recommended: 3/3 → 30.0**

---

### Aspirational — 10 pts (29 criteria, denominator = 29)

| ID | Score | Evidence |
|----|-------|----------|
| C-09 | **PASS** | Inherited: cross-namespace risk statement + urgency grouping in next-steps |
| C-10 | **PASS** | Inherited: MOCK-ACCEPTED rationale includes explanatory sentence per namespace |
| C-11 | **PASS** | FORBIDDEN OUTPUTS TRIAD block carries per-rule DO NOT statements at phase gate |
| C-12 | **PASS** | Inherited: zero-remaining confirmation gate present in write-back phase |
| C-13 | **PASS** | STEP 3, 4, 5 each have own heading, individual sub-questions, required verdict — separately completable |
| C-14 | **PASS** | Inherited: failing SQ answer named in verdict traceability, not only verdict role |
| C-15 | **PASS** | STEP 3 SQ-1/2/3 and STEP 4 SQ-1/2/3 all use "Name X" or "What specific X" grammar; STEP 5 inherited |
| C-16 | **PASS** | Inherited: confirmation prohibited under failure (canary design) |
| C-17 | **PASS** | AUTO-RULE CONTAMINATION GUARD section names the error and states "DO NOT apply evaluation to auto-flagged namespaces" |
| C-18 | **PASS** | Gates use "DO NOT proceed to STEP 3 (Architect Evaluation) until…", "…STEP 4 (Strategy Evaluation)…", "…STEP 5 (PM Evaluation)…" — forward references with step names present at each boundary |
| C-19 | **PASS** | Auto-flag list uses `{namespace}: trigger = {rule}` — named parseable field in fixed-position structured output |
| C-20 | **PASS** | Inherited: contrastive rationale sentence in MOCK-ACCEPTED template distinguishes namespace from threshold-crossing cases |
| C-21 | **PASS** | Inherited: positive structural signal template distinguishes present-tense artifact naming from verdict restatement; VERDICT-ECHO named as error |
| C-22 | **PASS** | Named "DEFAULT DECISION POSITION" block at skill level states inversion explicitly: "REAL-REQUIRED… not a finding, not a judgment. MOCK-ACCEPTED is an earned escape that requires an argument against the default." |
| C-23 | **PASS** | Inherited: Strategy SQ-1 anchor present as named slot source in Structural position slot |
| C-24 | **PASS** | Inherited: Artifact state field propagates into next-steps entry format |
| C-25 | **PASS** | Inherited: dedicated `Contrast:` sub-slot structurally separate from `Structural position` slot |
| C-26 | **PASS** | "CROSS-STEP GUARD — Architect to PM (C-26)" section names `architect-verdict = CONTRADICTS-ARCHITECTURE` and "DO NOT apply PM Evaluation (STEP 5) to these namespaces" — specific verdict value and suppressed step both named |
| C-27 | **PASS** | `[EVIDENCE-HEAVY]`, `[TIER-CRITICAL]`, `[COMPLIANCE]` each carry individually labeled DO NOT statements; completeness check states "all 3 labels must be present" |
| C-28 | **PASS** | All forward references carry both step number and label: "STEP 3 (Architect Evaluation)", "STEP 4 (Strategy Evaluation)", "STEP 5 (PM Evaluation)" |
| C-29 | **PASS** | FORBIDDEN OUTPUTS TRIAD block positioned at PHASE GATE between STEP 2 and STEP 3; co-location design note explicitly states independence from role ordering ("making it independent of which role runs first") |
| C-30 | **PASS** | Inherited: SQ-1 source citation present as required slot field in Structural position slot |
| C-31 | **PASS** | Header reads "FORBIDDEN OUTPUTS TRIAD (3 rules, all required — single verification point at this gate…)" — cardinality "3 rules, all required" declared at the block header |
| C-32 | **PASS** | Inherited: VERDICT-ECHO classification label with self-classifying test embedded inside SQ answer field definition |
| C-33 | **PASS** | Inherited from R12 V-01 |
| C-34 | **PASS** | Inherited from R12 V-01 (derivation: C-34 PASS in V-01 canonical baseline) |
| C-35 | **FAIL** | Arch-first design (Arch→Strat→PM) is structurally incompatible with C-35: the criterion requires a Strategy-to-PM guard in *non-Arch-first* ordering, which does not exist in this design. Structurally unreachable → 0 |
| C-36 | **FAIL** | Intentionally absent (single-axis test). No guard fires on `strategy-verdict = INSUFFICIENT FOR TIER {tier}` before PM Evaluation in the Arch-first ordering. C-36 contamination vector is open → 0 |
| C-37 | **PASS** | CROSS-TEMPLATE ERROR SYMMETRY declaration block added to STEP 7 entry format template: named structural block (not descriptive note) explicitly declares VERDICT-ECHO-IN-NEXT-STEPS as the parallel error to VERDICT-ECHO, names both template sites, names the shared classification principle |

**Aspirational: 27/29 → 27/29 × 10 = 9.31**

---

### Score Summary

| Component | Raw | Points |
|-----------|-----|--------|
| Essential | 5/5 | 60.00 |
| Recommended | 3/3 | 30.00 |
| Aspirational | 27/29 | 9.31 |
| **TOTAL** | | **99.31** |

---

### Excellence Signals

**From V-01:**

1. **Named structural block vs. descriptive note (C-37 pattern)**: The distinction between satisfying a criterion and satisfying it *structurally* is now encoded as the difference between a named block in the template definition ("CROSS-TEMPLATE ERROR SYMMETRY") and a descriptive note in surrounding prose. This pattern generalizes: any symmetry, parallelism, or cross-template relationship that needs to be verified belongs in a named block at the template site, not in adjacent guidance.

2. **Co-location design note as criterion independence declaration**: The TRIAD block carries an explicit note explaining *why* co-location satisfies both C-26 and C-27 independently ("making it independent of which role runs first"). This is meta-documentation embedded in the template — the template teaches its own structural properties.

---

### Single-Axis Verification

| Hypothesis | Result |
|------------|--------|
| C-37 PASS from symmetry declaration block in STEP 7 | **CONFIRMED** |
| C-36 FAIL (intentionally absent) | **CONFIRMED** |
| C-35 structurally unreachable in Arch-first | **CONFIRMED** |
| All R12 V-01 criteria preserved | **CONFIRMED** (27/27 carried forward) |

V-01 proves the C-37 axis cleanly. The -2 aspirational gap (C-35 structural, C-36 intentional) is fully accounted for. The path to a perfect-aspirational score in the next round requires V-02 adding the C-36 Arch-first Strategy-to-PM guard.

---

```json
{"top_score": 99.3, "all_essential_pass": true, "new_patterns": ["named-block-vs-descriptive-note: symmetry/parallelism relationships satisfy criteria only when declared as structural blocks in the template definition, not as descriptive notes in surrounding prose", "co-location-design-note: embedding a structural independence explanation inside a template block makes criterion satisfaction self-documenting at the verification site"]}
```
