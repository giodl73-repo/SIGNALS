Written to `simulations/quest/golden/topic-retro-variate-R7-2026-03-17.md`.

---

**R7 variations summary:**

| ID | Axis | Primary Target | Key Mechanism |
|----|------|----------------|---------------|
| V-01 | Single: C-20 | Gap assumption column | Dedicated "Assumption held without evidence" column in Phase 7; SEAL requires belief distinct from outcome |
| V-02 | Single: C-10 | AMEND per-table | `{{#if amend}}` scope marker above every table + OOS secondary table in Phase 2 |
| V-03 | Single: C-16 | 9-row namespace table | Fixed scout→topic row order in Phase 2; COVERED/EMPTY only; TOTAL row |
| V-04 | Combined: C-20+C-10 | Assumption + AMEND | Both Phase 7 column and per-table markers; zero-interference hypothesis |
| V-05 | Full integration | C-20+C-10+C-15+C-16+C-21 | All four PARTIAL criteria + seals with exact format strings per field |

**Critical design note in V-01/V-04/V-05:** The assumption column in Phase 7 is framed as "We assumed X" (inertia belief) versus "Would have surfaced: Y" (missed discovery) — two structurally distinct statements that must differ. The SEAL explicitly checks this distinction, which is exactly what C-20 requires: naming the prior belief that made the gap invisible, not just the outcome.
