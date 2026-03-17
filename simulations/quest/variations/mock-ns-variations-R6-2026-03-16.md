Written to `simulations/quest/golden/mock-ns-variate-R6-2026-03-16.md`.

---

## mock-ns Round 6 Variations (rubric v6, C-23 + C-24 target)

**New criteria targeted:**
- **C-23**: Preamble gate is the absolute opening sentence of S-0 -- zero pre-gate surface area. CONSTRAINT block or any introductory sentence before the preamble gate fails C-23, even when C-19 passes.
- **C-24**: CONSTRAINT names 5+ prohibited op types, closing the artifact-write phase (path construction / file write) beyond the C-21 minimum of 4.

**Variation axes:**

| # | Axis | C-23 | C-24 | Score |
|---|------|------|------|-------|
| V-01 | C-24 boundary: 4-op CONSTRAINT, preamble gate first | PASS | FAIL | 110/112 |
| V-02 | C-23 boundary: CONSTRAINT-first placement, 5-op | FAIL | PASS | 110/112 |
| V-03 | C-23 boundary: intro prose before gate, 5-op | FAIL | PASS | 110/112 |
| V-04 | Double: R5 baseline form unchanged | FAIL | FAIL | 108/112 |
| V-05 | Convergent: all 24 via form-variant language | PASS | PASS | 112/112 |

**Key structural moves:**
- V-01 isolates C-24 by moving preamble gate first (C-23 fixed) while leaving CONSTRAINT at 4 ops
- V-02 and V-03 isolate C-23 via two distinct surface mechanisms: CONSTRAINT-block-first vs intro-prose-first -- both are pre-gate surface
- V-04 documents the R5 baseline score (108/112) under v6
- V-05 convergent swaps `"This step emits first..."` as the opening sentence and expands CONSTRAINT to 5 ops using synonym phrasings (`"No artifact path assembly or file output"`)

**Two new failure traps encoded:** `C-21 count satisfies C-24` and `C-19 awarded as C-23` (two forms confirmed by V-02 and V-03).
