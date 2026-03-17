Written to `simulations/quest/rubrics/draft-proposal-rubric-v15-2026-03-15.md`.

---

**What changed v14 → v15:**

**C-39** extracted from V-02 R14's C-38 PASS note. The excellence signal is the **two-part T-37 CONDITION structure**:

- **Part 1** (C-38's requirement): quotes the exact failure construct — `"row-level confirmation 'R-NN IDs applied to risk row' fires T-37"`
- **Part 2** (C-39's new requirement): prescribes the correct replacement format — `"per-column format required: [OPTION-A column: R-NN IDs] | [OPTION-B: R-NN IDs]"`

C-38 only required Part 1. C-39 independently requires Part 2. A T-37 entry with the failure exemplar but no correct-format prescription passes C-38 and fails C-39.

**Cascade invariant**: C-38 FAIL → C-39 FAIL (deterministic — an abstract entry satisfies neither part).

**Score projections under v15 for R14 variations** (denominator /32):

| Variation | Fails | Composite |
|-----------|-------|-----------|
| V-02 R14 (C-37) | 1 | 99.69 |
| V-01 R14 (C-38, C-39 cascade) | 2 | 99.38 |
| V-03 R14 (C-24, C-38, C-39 cascade) | 3 | 99.06 |

**C-24** updated: 38 → 39 rows (one per C-01..C-39).
