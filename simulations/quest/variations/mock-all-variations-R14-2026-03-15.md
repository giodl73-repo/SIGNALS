Written to `simulations/quest/golden/mock-all-variate-R14-2026-03-15.md`.

---

## Round 14 -- 5 Variations

**Primary objective:** C-30 three-way separation (rationale-authorship chain)

| Variation | Axis | C-13 | C-29 | C-30 | C-27 | C-28 | Predicted |
|-----------|------|------|------|------|------|------|-----------|
| V-01 | Rationale seed pre-authored + skeleton seeds + paraphrase gate | PASS | PASS | PASS | FAIL | FAIL | 20/22 |
| V-02 | Delegation instruction (substantive) + verbatim gate + annotation | PASS | FAIL | FAIL | PASS | PASS | 20/22 |
| V-03 | Bare `{rationale}` placeholder + verbatim gate, annotation absent | PARTIAL | FAIL | FAIL | PASS | FAIL | ~18/22 |
| V-04 | Skeleton seeds + rationale seed + verbatim gate, annotation absent | PASS | PASS | PASS | PASS | FAIL | 21/22 |
| V-05 | All three structural choices -- full cluster ceiling | PASS | PASS | PASS | PASS | PASS | 22/22 |

**What the three-way separation tests:**
- V-01: Case 1 -- C-13 PASS + C-30 PASS (template is author of both fields)
- V-02: Case 2 -- C-13 PASS + C-30 FAIL (block present, model is author; delegation instruction substantive enough to drive correct rationale)
- V-03: Case 3 -- C-13 PARTIAL + C-30 FAIL (bare placeholder, no content, no directive)

**Secondary objectives:**
- V-04 confirms the authorship-residency pair (C-29 + C-30) can be achieved as a dual-field ceiling below C-28 -- one meta-choice satisfies both
- V-05 confirms the full 14-criterion table-coupling cluster ceiling under v14

**Key structural variation in ROLE 2 rationale block:**
- V-01/V-04/V-05: pre-authored literal text (`prove: requires actual experiment data...`), model copies verbatim
- V-02: `{write one sentence: explain specifically why this namespace requires real artifacts...}`, model generates
- V-03: bare `{rationale}`, nothing authored
