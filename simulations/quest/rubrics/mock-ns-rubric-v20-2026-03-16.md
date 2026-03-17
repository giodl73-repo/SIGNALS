**Written to**: `simulations/quest/rubrics/mock-ns-rubric-v20-2026-03-17.md` (574 lines)

---

## Summary of changes in v20

**Three new aspirational criteria extracted from R20 excellence signals. Max rises from 162 to 168 (44 x 2 = 88).**

All three axes target the **S-4 FLAG prohibition chain** -- a zone no existing criterion (C-01 through C-49) reaches. All five R20 variations pass all 49 existing criteria at 162/162 under v19.

### New criteria

| Criterion | Axis | Pattern | Default-pass condition |
|-----------|------|---------|----------------------|
| **C-50** | A | Priority row with modal impossibility form ("No instruction in this step can precede this rule.") | Passes by default when no FLAG prohibition chain is present |
| **C-51** | B | Anti-bypass echo header: `[P-0:ABD]:` as row header label, attribution removed from content cell | Passes by default when no anti-bypass echo entry is present |
| **C-52** | C | All-governed dual closure: explicit scope expansion to atypical paths ("including paths that do not pass through prior steps in normal order") | Passes by default when no governing closure sentence is present |

### Scoring under v20

The R19 V-05 baseline S-4 has attribution-in-cell echo (C-51 **fails**), no priority row (C-50 default pass), no closure sentence (C-52 default pass) -- scores **160/168** under v20.

| Variation | C-50 | C-51 | C-52 | Score |
|-----------|------|------|------|-------|
| V-01 Axis A only | PASS | FAIL | PASS (default) | **164/168** |
| V-02 Axis B only | PASS (default) | PASS | PASS (default) | **164/168** |
| V-03 Axis C only | PASS (default) | FAIL | PASS | **164/168** |
| V-04 Axis A+B | PASS | PASS | PASS (default) | **166/168** |
| **V-05 Axis A+B+C** | **PASS** | **PASS** | **PASS** | **168/168** |

**Note on V-03 parity:** Axis C alone nets 162/168 -- the +2 from C-52 exactly cancels the -2 from C-51 (attribution-in-cell form unchanged). Axis B (or any combination including B) is required to exceed 162 under v20.
