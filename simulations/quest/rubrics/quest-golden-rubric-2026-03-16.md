Rubric written to `simulations/quest/rubrics/quest-golden-rubric-v1-2026-03-16.md`.

---

**Summary**

10 criteria across 3 tiers:

| ID | Text | Tier | Category |
|----|------|------|----------|
| C-01 | Dual convergence termination | essential | correctness |
| C-02 | Golden prompt written as full skill body | essential | correctness |
| C-03 | Final rubric written as standalone artifact | essential | correctness |
| C-04 | QU2 precedes QU3 | essential | behavior |
| C-05 | Rubric present at loop start | essential | correctness |
| C-06 | Per-round iteration record | recommended | coverage |
| C-07 | Excellence signal isolation | recommended | depth |
| C-08 | Criterion proposal completeness (tier + pass condition) | recommended | format |
| C-09 | "What made it golden" mechanism narrative | aspirational | depth |
| C-10 | Persistent gap identification (ablated criteria) | aspirational | coverage |

**Composite formula:** `(essential_pass/5)*60 + (recommended_pass/3)*30 + (aspirational_pass/2)*10`

**Golden threshold:** all 5 essential pass AND composite >= 80.

The 5 essentials enforce the loop contract — without any one of them the output cannot be called a quest-golden execution. The 3 recommended push quality of the iteration record and signal extraction. The 2 aspirationals reward explanation and gap awareness. The rubric grows from here as quest:golden discovers excellence patterns in subsequent rounds.
