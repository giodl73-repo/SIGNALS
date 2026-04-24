Written to `simulations/quest/golden/signal-variate-R7-2026-03-16.md`.

---

## Round 7 Summary

**R6 gap**: V-05 scored 100/100 on v5 rubric but v6 adds C-20, C-21, C-22 -- three criteria satisfied by content in R6 V-05 but with no dedicated RULE entries. Bijection: 11 rules but 14 criteria on v6.

**Structural progression**:

| Variation | Rules | New entry | Gate threshold | Key change |
|-----------|-------|-----------|----------------|------------|
| V-01 | 12 | RULE 12 (C-20) | "All 12 boxes checked" | C-20 gets O(1) dedicated lookup; RULE 9 count=12 |
| V-02 | 13 | RULE 13 (C-21) | **"13/13 checked = valid output"** | C-21 explicit PASS fraction added; RULE 9 count=13 |
| V-03 | 14 | RULE 14 (C-22) | "14/14 checked = valid output" | Full bijection closed; RULE 9 count=14 |
| V-04 | 14 | -- | same | Bijective invariant declared in QUALITY CONTRACT **header** |
| V-05 | 14 | -- | same | RULE 12/13/14 cross-reference their evidence by name ("RULE 9 above", "14/14 checked", "RULE 11 (C-19) above") |

**Expected scoring gradient on v6 rubric**:
- V-01: C-20 PASS (dedicated rule), C-21 FAIL (no "N/N" format), C-22 PASS (RULE 11 exists) -- 12/14 aspirational
- V-02: C-20 + C-21 PASS, C-22 PASS -- 13/14 aspirational (RULE 14 absent means C-22's bijection entry missing)
- V-03: all 14 aspirational PASS -- 14/14 aspirational, composite 100/100
- V-04: same score as V-03, higher structural robustness (invariant declared)
- V-05: same score as V-04, maximum O(1) auditability per new rule

**Predicted champion**: V-05 (all criteria, all cross-references explicit). V-03 is the minimum-viable 100/100 path.
