# Quest Scorecard — mock-accept · Round 5 · Rubric v5

**Date:** 2026-03-17
**Skill:** mock-accept
**Rubric:** v5 (17 aspirational; C-23/C-24/C-25 new this round)
**Base:** R4 V-05 — all 14 v4 aspirational criteria pass; fails C-23, C-24, C-25 against v5

---

## 1 · Base-Carry Assessment

All R5 variations inherit R4 V-05. Criteria below are PASS across all five variations unless overridden in §2.

| Band | Criteria | Status |
|------|----------|--------|
| Essential | C-01 auto-flag rules | PASS — Rules 1/2/3 produce unconditional artifact-as-subject output; no first-person language in auto-flag block |
| Essential | C-02 forbidden triad | PASS — All three labels present; completeness check enforced with "two-of-three does not satisfy" |
| Essential | C-03 status writeback + CANARY | PASS — Phase N Edit call, CANARY ASSERTION verbatim, CANARY-FALSE-POSITIVE named, CANARY SUPPRESSED branch defined (inherited from R4 V-05 STEP 5–8) |
| Essential | C-04 review artifact structure | PASS — Coverage table (4 cols), Structural records, Risk with urgency labels, Next Steps under single Write block |
| Essential | C-05 MOCK-ACCEPTED positive argument | PASS — Slot 1 and Slot 2 structurally separate; exact-token constraint; revert-on-violation per slot; paraphrase named as violation class |
| Recommended | C-06 entity-naming in roles | PASS — SQ-1/SQ-2/SQ-3 require named element citations; yes/no alone forbidden |
| Recommended | C-07 step sequencing + guard compliance | PASS — Arch-blocked and Strategy-blocked named; empty-list statement required ("Arch-blocked: [] (none…)"); partition explicit before phase exit |
| Recommended | C-08 eval-driven REAL-REQUIRED template | PASS — 5-field template inherited (trigger condition · SQ answer · Artifact state · verdict · required action); VERDICT-ECHO named |
| Aspirational | C-09–C-22 (14 criteria) | PASS × 14 — all inherited from R4 V-05 including artifact-as-subject grammar (C-09), tier sourcing (C-10), inline completeness gate (C-11), reason-code co-location (C-12), phase exit assertions (C-13), blank-line failure signal (C-14), forbidden-form enumeration (C-15), written-gate blocking (C-16), named gate registry (C-17), adjacent CONSTRAINT co-location (C-18), universal blank-slot enforcement (C-19), halt-on-violation (C-20), C-21 Phase 6 gate structure, C-22 Slot 1 paraphrase examples |

Essential cap: not triggered (no FAIL). Recommended: 30/30. Aspirational base: 14 passes carried forward.

---

## 2 · Differential Assessment — New v5 Criteria

C-09 N/A cascade: C-09 PASS in all variations → full 17-criterion denominator applies.

### C-23 — Three-Step Halt Sequence

| Variation | Evidence | Verdict |
|-----------|----------|---------|
| V-01 | STANDING RULE block added at top; halt reads: `"HALT. Delete the violating line. Rewrite in PASS form."` — three discrete imperatives, no combined gerunds | **PASS** |
| V-02 | Axis isolates C-25; halt text carries R4 borderline two-step form ("halt and rewrite before advancing") — two imperatives, not three atomic steps | **FAIL** |
| V-03 | Three-step imperatives co-located at each CONSTRAINT site; however C-23 criterion specifies "the Standing Rule halt instruction" — no named Standing Rule block is added; co-location satisfies C-20 (halt present) but not the Standing Rule placement requirement | **PARTIAL** (not counted) |
| V-04 | V-01 opening rule inherited | **PASS** |
| V-05 | V-01 opening rule inherited | **PASS** |

### C-24 — Gate-to-Section Traceability in Phase 6 Gate

All R5 variations explicitly add GATE F per author declaration ("R5 makes it explicit in all variations as a free base carry"). V-03 / V-05 further anchor it as a standalone STEP 9.

| Variation | Evidence | Verdict |
|-----------|----------|---------|
| V-01 | GATE F added to STEP 8 (base carry); cites Coverage, Structural records, Risk, Next Steps by section ID | **PASS** |
| V-02 | Same base carry | **PASS** |
| V-03 | GATE F elevated to dedicated STEP 9 with explicit section IDs — strongest anchor | **PASS** |
| V-04 | Base carry | **PASS** |
| V-05 | STEP 9 explicit (V-03 contribution) | **PASS** |

### C-25 — Slot 2 Paraphrase Violation Examples

| Variation | Evidence | Verdict |
|-----------|----------|---------|
| V-01 | Prose note at Slot 2 references violation class ("near-miss paraphrase") — no quoted altered-token forms; C-25 requires ≥ 2 quoted examples by token | **FAIL** |
| V-02 | Dedicated SLOT 2 VIOLATION TABLE: 3 rows × 2 columns (quoted near-miss form · violation type); all examples are quoted altered-token forms | **PASS** |
| V-03 | C-25 not targeted; Slot 2 carries R4 form (class label only) | **FAIL** |
| V-04 | V-02 Slot 2 table inherited | **PASS** |
| V-05 | V-02 Slot 2 table inherited | **PASS** |

---

## 3 · Composite Scores

```
Scoring: Essential (5 × 12 = 60) + Recommended (3 × 10 = 30) + Aspirational ((N/17) × 10)
```

| Variation | C-23 | C-24 | C-25 | Asp passes | Asp score | Total |
|-----------|------|------|------|------------|-----------|-------|
| V-01 | PASS | PASS | FAIL | 16/17 | 9.41 | **99.41** |
| V-02 | FAIL | PASS | PASS | 16/17 | 9.41 | **99.41** |
| V-03 | PARTIAL | PASS | FAIL | 15/17 | 8.82 | **98.82** |
| V-04 | PASS | PASS | PASS | 17/17 | 10.00 | **100.00** |
| V-05 | PASS | PASS | PASS | 17/17 | 10.00 | **100.00** |

---

## 4 · Ranking

| Rank | Variation | Score | Notes |
|------|-----------|-------|-------|
| **1** | **V-05** | **100.00** | Full combination — V-01 (opening rule) + V-02 (Slot 2 table) + V-03 (explicit STEP 9 gate); C-24 anchored at maximum strength; recommended as R5 golden |
| **1** | **V-04** | **100.00** | Minimal complete set — opening rule + Slot 2 table; C-24 from base carry; achieves 17/17 without STEP 9 overhead |
| **3** | V-01 | 99.41 | Axis isolation confirms C-23 requires opening STANDING RULE; C-25 gap explicit |
| **3** | V-02 | 99.41 | Axis isolation confirms C-25 requires quoted table; C-23 gap explicit |
| **5** | V-03 | 98.82 | C-23 co-location approach misses Standing Rule placement requirement; two-criterion gap |

**Golden recommendation: V-05** — V-04 is the minimal 100-point path, but V-05's explicit STEP 9 makes GATE F independently verifiable from a named step number rather than embedded in STEP 8. More durable against context compression and future variation.

---

## 5 · Excellence Signals

Three new patterns extracted from R5:

**ES-R5-01 — Opening STANDING RULE with exempt list** (V-01 · C-23 anchor):
The forbidden-form enumeration and three-step halt are placed in a named block before STEP 1, with an explicit exempt list (tier sourcing line; auto-flag rule definitions; role verdict labels). Exempt list prevents the grammar rule from misfiring on output that must use non-artifact-subject form by design. Elevates C-09 from in-flow to pre-flow: every evaluator encounters the rule before seeing any step instruction.

**ES-R5-02 — SLOT 2 VIOLATION TABLE with quoted altered-token forms** (V-02 · C-25 anchor):
Revert-on-violation for Slot 2 uses a structured 3-row × 2-column table (quoted near-miss form, violation type) rather than class-label description. Enables token-level matching: the evaluator matches by reading quoted text, not by interpreting a category name. Closes the C-22/C-25 Slot 1/Slot 2 asymmetry. Pattern: whenever C-22-style examples exist for Slot 1, extend the same table structure to Slot 2.

**ES-R5-03 — Explicit GATE F as standalone STEP 9** (V-03 · C-24 at maximum strength):
Phase 6 completeness gate promoted from a clause inside STEP 8 to its own numbered step with section IDs cited by name (Coverage, Structural records, Risk, Next Steps). A separate numbered step cannot be accidentally merged with its predecessor during generation. Section-ID citations create verifiable traceability: gate assertion → artifact structure → named sections → evaluator can confirm gate without narrative parsing.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Opening STANDING RULE with exempt list places forbidden-form enumeration and three-step halt before all steps; exempt list prevents grammar rule misfiring on required non-artifact-subject output (tier sourcing, auto-flag rule definitions, verdict labels)", "SLOT 2 VIOLATION TABLE with quoted altered-token near-miss forms (3 rows × 2 cols) enables token-level matching; closes Slot 1/Slot 2 asymmetry; whenever Slot 1 has C-22 quoted examples extend the same table to Slot 2", "Explicit GATE F as standalone STEP 9 with section IDs cited by name creates verifiable traceability from gate assertion to artifact structure; promotion from embedded clause to numbered step prevents merging during generation"]}
```
