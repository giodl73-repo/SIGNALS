Written to `simulations/quest/golden/topic-reflect-variate-R5-2026-03-17.md`.

---

## Round 5 Variations — topic-reflect (v5 rubric)

**Three single-axis + two combined. All include C-17 as base.**

| Variation | Axis | New criteria targeted | Hypothesis |
|-----------|------|----------------------|------------|
| **V-01** | A — Synonym mapping | C-18 | Mapping table closes the substitution loop C-17 opens; "Reliability → Correctness" leaves no residual ambiguity about what to use |
| **V-02** | B — ENTER/EXIT per stage | C-19 | ENTER as coverage check prevents premature transition; EXIT as completeness gate prevents thin field entries and stage collapse |
| **V-03** | C — Gate sequence map | C-15 | Gate topology surfaced before Stage 1 makes token semantics self-locating; model re-consults map without re-reading stage prose |
| **V-04** | A + B | C-18 + C-19 | Two independent failure modes (substitution + transition); non-redundant — a model can pass one while failing the other |
| **V-05** | A + B + C + worked example | C-18 + C-19 + C-15 + C-16 | Maximum coverage: four axes target four distinct failure modes (orientation, substitution, transition, quality floor) |

**Predicted scores under v5 rubric** (max 145):
- V-01: 130 (all essential + all recommended + C-09 through C-18 minus C-19, C-15)
- V-02: 125 (all essential + all recommended + C-09 through C-14 + C-19, no mapping table)
- V-03: 125 (all essential + all recommended + C-09 through C-15 + C-17, no C-18/C-19)
- V-04: 135 (all essential + all recommended + C-09 through C-19 minus C-15, C-16)
- V-05: 145 (all 19 criteria — perfect score under v5)

**Key structural decision:** C-17 promoted to base mechanism (achievable in R4); C-18 and C-19 are the discriminating axes. V-05 is the first variation to target all 11 aspirational criteria simultaneously.
