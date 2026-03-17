Written to `simulations/quest/golden/topic-roadmap-variate-R13-2026-03-17.md`.

---

## R13 Variation Summary

| Variation | Axis | C-29 | C-30 | C-27 | C-28 | C-21--C-25 |
|-----------|------|------|------|------|------|------------|
| **V-01** | Three-way naming (C-29) | **FULL** | absent | full | full | full |
| **V-02** | Proposal bias column (C-30) | partial | **FULL** | full | partial | full |
| **V-03** | C-29 + C-30, minimal | **FULL** | **FULL** | partial | partial | absent |
| **V-04** | Full stack C-21--C-30 | **FULL** | **FULL** | full | full | full |
| **V-05** | Dual schema contract | **FULL** | **FULL** | full | full | full |

**V-01** bases on R12 V-02 (C-28 dual-site full, C-27 partial). The single fix: rename Phase 5 column from `Consequence if HOLDS` to `Consequence if unchanged`, unifying all three consequence sites. C-30 deliberately absent -- no bias column in Phase 6.

**V-02** bases on R12 V-01 (C-27 full, C-28 partial). Adds `Bias blocked by guard` column to Phase 6a and 6b table schemas plus a `PROPOSAL BIAS AUDIT` guard. Phase 5 column deliberately left as `Consequence if HOLDS` to produce C-29 partial -- confirming C-30 is scored independently.

**V-03** minimal base (no SECTION SCOPE, no dual-site INERTIA-GATE, no standalone verdict block). Both C-29 and C-30 targeted, confirming neither requires the full structural stack.

**V-04** is the full nine-criterion integration: R12 V-04 + `PROPOSAL BIAS AUDIT` guard + `Bias blocked by guard` column + schema CONTRACT extended to cover all three consequence sites.

**V-05** adds a dual-column OUTPUT SCHEMA CONTRACT that pre-commits both `Consequence if unchanged` (CONTRACT A, four sites) and `Bias blocked by guard` (CONTRACT B) before any file is read. A scorer can detect C-29 or C-30 failures from the schema block alone.

**Target score for V-04/V-05**: 38 (R12 baseline) + 2 (C-29) + 2 (C-30) = **42/44 = 9.55**
