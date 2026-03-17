Written to `simulations/quest/golden/mock-ns-variate-R17-2026-03-17.md`.

---

## R17 Variations Summary

| Variation | Axis | CONSTRAINT form | Hypothesis | Expected score |
|-----------|------|-----------------|------------|----------------|
| **V-01** | CONSTRAINT form: step-IDs-only | `Do not perform S-1, S-2, S-3.1, S-3.2, or S-3.3...` | C-44 FAIL, C-15 FAIL, C-21 FAIL, C-24 FAIL; C-45 PASS | **142/154** |
| **V-02** | CONSTRAINT annotation placement: trailing group | Step IDs only + separate sentence "Operations blocked: skill selection, category lookup, carry, compliance detection, flag computation" | C-44 FAIL (types not co-located per-ID); C-15/C-21/C-24 PASS (5 types in block); C-45 PASS | **152/154** |
| **V-03** | CONSTRAINT S-3 granularity: collapsed | `S-1 (skill selection), S-2 (category lookup), S-3 (flag computation)` | C-45 FAIL; C-21 FAIL; C-24 FAIL; C-44 PASS; C-15 PASS | **148/154** |
| **V-04** | CONSTRAINT annotation punctuation: em-dash | `S-1 -- skill selection, S-2 -- category lookup, S-3.1 -- carry, S-3.2 -- compliance detection, S-3.3 -- flag computation` | C-44 PASS if em-dash = "equivalent co-located form"; C-45 PASS | **154/154** |
| **V-05** | Combined: golden CONSTRAINT + prose S-1/S-2 + declarative phrasing | Full `S-1 (skill selection)...S-3.3 (flag computation)` parenthetical form; prose format; "The step emits..." throughout | All criteria pass; axes confirmed independent | **154/154** |

**Key questions this round answers:**
- **V-01 vs V-02**: Can C-44 fire independently of C-15/C-21/C-24? V-02 tests the exact scenario — 5 operation types present in the CONSTRAINT block, but none co-located per-ID.
- **V-03**: C-45 first isolated canonical failure. Also reveals that S-3 collapse reduces type count (3 < 4), so C-21/C-24 co-fire.
- **V-04**: First test of the "equivalent co-located form" clause in C-44. Em-dash is syntactically adjacent but not parenthetical.
- **V-05**: Confirms the prose/declarative axes from R16 are orthogonal to the new CONSTRAINT criteria.
