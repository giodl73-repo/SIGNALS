Written to `simulations/quest/rubrics/review-design-variate-R18-2026-03-15.md`.

---

## Round 18 Variations — Summary

**Root diagnostic**: R17 V-02 BLOCK 2.7 F-30 fires on *absence* (`when this block is absent`). C-51 requires F-30 to fire on *wrong position* — a block that exists inside BLOCK 5 or after BLOCK 3 is non-conformant but wouldn't trigger the R17 halt. All five variations fix this.

---

| Variation | Axis | Hypothesis |
|-----------|------|-----------|
| **V-01** | Lifecycle Emphasis | Two explicit phases (Phase A: position gate, Phase B: inbound gate) make C-51 a named lifecycle checkpoint. Tests whether phase labels alone drive C-51 pass. |
| **V-02** | Output Format | `BLOCK 2 P1 Backed?` column makes C-50 structurally visible at the cell level — a `No` value is as detectable as a blank `Sev` cell. F-30 absence→position fix carried forward. |
| **V-03** | Phrasing Register | F-30 stated as a proactive SHALL/SHALL NOT position contract ("BLOCK 2.7 SHALL occupy the lifecycle window...") rather than a reactive CONSTRAINT VIOLATED trigger. Tests whether formal modal declaration of the position class achieves C-51 without phase labels. |
| **V-04** | Lifecycle + Format | V-01 two-phase structure + V-02 3-column `BLOCK 2 P1 Backed?` table. Both C-50 and C-51 addressed structurally and simultaneously. |
| **V-05** | Register + Lifecycle + Inertia | Full ceiling: formal modal contracts, two-phase gate, **plus an explicit inertia note** at BLOCK 2.7 documenting the prior-round absence-vs-position gap so the position-integrity scope of F-30 survives future edits. |

**Key structural difference across variations** — BLOCK 2.7 only; all other blocks are identical:

- V-01/V-04/V-05: two-phase label forces position check before registry population
- V-02/V-04: `BLOCK 2 P1 Backed?` column surfaces inbound violations without executing halt logic
- V-03/V-05: SHALL/SHALL NOT contracts declare the class proactively
- V-05 only: inertia note names the prior-round gap explicitly for maintainers
