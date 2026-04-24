Here is the complete updated rubric as Markdown:

---

**What changed from v13:**

**One new aspirational criterion extracted from R13 excellence signals:**

| ID | Criterion | Source Axis | Independence from Parent |
|----|-----------|-------------|--------------------------|
| C-38 | **Amendment table T-37 trigger entry includes inline failure-condition exemplar** | V-02 R13 excellence signal | C-18 requires front-loaded trigger rules naming conditions. C-29 requires a PHASE column. C-38 requires the T-37 entry specifically to carry an inline exemplar note within the CONDITION field quoting the exact document construct that fires T-37. A T-37 entry stating "C-37: per-column attribution absent" satisfies C-18 and C-29 but fails C-38 (no inline exemplar). V-02 R13 demonstrated: "row-level confirmation 'R-NN IDs applied to risk row' fires T-37" — the trigger entry tells a reviewer what to look for without consulting the rubric. |

**Denominator:** `/30` → `/31`. Score projections for R13 variations under v14:

| Variation | Fails | Composite |
|-----------|-------|-----------|
| V-02 R13 (C-37, C-24 cascade) | 2 | 99.35 |
| V-01 R13 (C-36, C-24, C-38) | 3 | 99.03 |
| V-03 R13 (C-24, C-36, C-37, C-38) | 4 | 98.71 |

**Cascade invariants:**
- **C-38 cascade from stale table**: T-37 absent from amendment table → C-38 FAIL (no entry to carry the exemplar).
- **C-38 independent fail**: 38-row table (C-24 PASS) with T-37 carrying only abstract condition text fails C-38 while C-18 and C-29 pass.
- **C-24 version-bump cascade**: All R13 variations had 37-row tables; all fail C-24 under v14's 38-row requirement.

**Key changes to existing criteria:**
- **C-24**: updated from "exactly 37 trigger rows" → "exactly 38 trigger rows (one per C-01..C-38)"
- **Scoring formula denominator**: `/30` → `/31`

Written to `simulations/quest/rubrics/draft-proposal-rubric-v14-2026-03-15.md`.
