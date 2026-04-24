Rubric written to `simulations/quest/rubrics/scout-inertia-rubric-v1-2026-03-17.md`.

**Structure summary:**

| ID | Weight | Category | Core test |
|----|--------|----------|-----------|
| C-01 | essential | coverage | Workaround described concretely (not just named) |
| C-02 | essential | correctness | Costs quantified across 2+ dimensions with numbers |
| C-03 | essential | correctness | Threat score present and = HIGH (binary, no partial) |
| C-04 | essential | depth | 2+ falsifiable conditions under which inertia loses |
| C-05 | essential | coverage | 2+ specific workaround failure modes (staying, not moving) |
| C-06 | recommended | depth | Time / training / disruption as separate line items |
| C-07 | recommended | depth | Loss conditions use observable thresholds |
| C-08 | recommended | coverage | Forward-looking risk of staying on workaround |
| C-09 | aspirational | depth | Failure modes ranked by severity |
| C-10 | aspirational | depth | Steelman argument presented and rebutted |

**Key design decisions:**

- C-03 is binary — missing or sub-HIGH score is an automatic essential fail, no partial credit
- C-04 and C-05 are intentionally distinct: *failure modes* = what goes wrong staying; *loss conditions* = when inertia loses the argument. Conflating them is a common output failure
- C-10 (steelman) is aspirational because it's genuinely hard — a weak steelman is worse than none
