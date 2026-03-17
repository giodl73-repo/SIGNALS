Written to `simulations/quest/golden/mock-accept-variate-R8-2026-03-17.md`.

---

## R8 Axis Summary

| Variation | Axis | Key change from R7 V-05 | Predicted |
|-----------|------|--------------------------|-----------|
| **V-01** | output-format | MOCK COST REGISTER as 3-column table instead of field-list | 24/24 |
| **V-02** | lifecycle-emphasis | COST REGISTER merged into GATE D sub-block; no separate STEP 5 | C-32 FAIL — 23/24 |
| **V-03** | inertia-framing | INERTIA LEDGER at gate-entry (before STEP 3/4 loops) instead of gate-exit (inside GATE C/D) | C-31 FAIL — 23/24 |
| **V-04** | output-format + lifecycle | V-01 table + GATE E-COST extended with explicit column names (Namespace, Phase, Cost-of-MOCK) parallel to GATE F's section naming | 24/24 |
| **V-05** | output-format + inertia + phrasing | V-01 table + GATE D INERTIA LEDGER gets cumulative cross-phase sum assertion + formal declarative prose register (HALT/DELETE/REWRITE triples preserved verbatim) | 24/24 |

**What R8 confirms:**
- V-02 tests the "distinct numbered step" requirement of C-32 — embedding in GATE D is the predicted failure path
- V-03 tests the "phase exit" requirement of C-31 — entry position is the predicted failure path  
- V-01/V-04/V-05 probe whether the 24/24 path is format-independent and register-independent, and whether GATE D's LEDGER can carry a cross-phase cumulative sum without conflict
