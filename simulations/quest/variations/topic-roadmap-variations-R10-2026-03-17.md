Written to `simulations/quest/golden/topic-roadmap-variate-R10-2026-03-17.md`.

---

## Round 10 Variations — Summary

**Target criteria**: C-24 (spatial mechanism separation) and C-25 (Phase 5 verdict deferral + anti-duplication).

**Key diagnostic**: R9 V-05 already passes C-25 — "Apply the Verdict Vocabulary defined above. Do not redefine DEFEATED or HOLDS here." is present. But C-24 fails because the Phase 5 INERTIA-GATE annotation block re-embeds verdict semantic descriptions ("HOLDS is the default verdict; DEFEATED requires specific named signal evidence") alongside gate-exclusion text.

| Variation | Axis | C-21 | C-22 | C-23 | C-24 | C-25 |
|-----------|------|------|------|------|------|------|
| **V-01** | C-24 only (SECTION SCOPE inline blocks) | pass | pass | pass | **pass** | partial |
| **V-02** | C-25 only (categorical anti-duplication) | pass | pass | pass | FAIL | **pass** |
| **V-03** | C-24 + C-25 minimal (R9 V-03 base) | fail | fail | pass | **pass** | **pass** |
| **V-04** | All 5 from R9 V-04 base + MUST NOT CONTAIN | pass | pass | pass | **pass** | **pass** |
| **V-05** | All 5 with heading-level `[SCOPE: ...]` annotations | pass | pass | pass | **pass** | **pass** |

**Orthogonality demonstrated**:
- V-02: C-24 FAIL / C-25 pass — exactly the scenario from the rubric matrix (Phase 5 INERTIA-GATE co-locates gate text and verdict semantics)
- V-01: C-24 pass / C-25 partial — forward-reference without anti-duplication clause

**Primary C-24 question for scoring**: Does heading-level scope (V-05's `## Phase 1 [SCOPE: ...]`) score higher than inline annotation blocks (V-04's `[>> SECTION SCOPE: MUST NOT CONTAIN <<]`)? V-05 is verifiable from the document outline; V-04 requires reading section body to find the scope declaration.
