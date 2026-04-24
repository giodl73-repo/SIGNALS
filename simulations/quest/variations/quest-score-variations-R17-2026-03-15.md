Written to `simulations/quest/golden/quest-score-variate-R17-new-2026-03-15.md`.

---

## Summary

**5 variations generated. Variation matrix:**

| Element | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| SPECIFICITY AUDIT MANIFEST (C-43 req 1) | YES | YES | NO | YES | YES |
| VERIFIER references manifest by key (C-43 req 2) | YES | YES | NO | YES | **NO** |
| SYNTHESIS prohibition on SA blocks (C-43 req 3) | YES | YES | NO | **NO** | YES |
| [ANALYST COMPLETE] alone exclusion (C-42) | YES | YES | YES | YES | YES |
| [SPECIFICITY AUDIT COMPLETE] alone exclusion (C-44) | YES | **NO** | YES | YES | YES |
| **Predicted C-43** | **PASS** | PASS | FAIL | PARTIAL | PARTIAL |
| **Predicted C-44** | **PASS** | PARTIAL | PASS | PASS | PASS |

**V-01** is the ceiling: combines V-04 R16 architecture (manifest + key + prohibition) with V-05 R16 architecture (symmetric exclusion), inheriting all 35 prior aspirationals. Predicts composite = (37/37 × 220) + 50 + 40 = 310.

**Single-axis probes:**
- V-02 separates C-43 PASS from C-44 PARTIAL (forward exclusion only)
- V-03 separates C-44 PASS from C-43 FAIL (no manifest)

**PARTIAL-path probes:**
- V-04 tests C-43 PARTIAL via missing SYNTHESIS prohibition (manifest + key present)
- V-05 tests C-43 PARTIAL via missing VERIFIER key reference (manifest + prohibition present)

**New failure modes added to anti-pattern anchor:**
- **G** — Dispersed SA body reread → C-43 (all variations that probe manifest)
- **H** — Reverse bypass path (asymmetric gate) → C-44 (all variations that probe symmetric exclusion)
