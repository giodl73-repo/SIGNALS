Rubric written to `simulations/quest/rubrics/signal-rubric-v1-2026-03-17.md`.

**Summary of criteria:**

| ID | Weight | Category | What it tests |
|----|--------|----------|---------------|
| C-01 | essential | coverage | All 12 namespaces present |
| C-02 | essential | correctness | Sub-skills listed per namespace |
| C-03 | essential | format | One-line description per sub-skill |
| C-04 | essential | behavior | `--bare` emits command names only |
| C-05 | essential | behavior | `<namespace>` filter scopes output |
| C-06 | recommended | correctness | Sub-skill count per namespace accurate |
| C-07 | recommended | format | Dispatch footer per namespace |
| C-08 | recommended | coverage | Namespace headers state purpose |
| C-09 | aspirational | correctness | Descriptions match canonical one-liners |
| C-10 | aspirational | format | Scannable without overwhelming |

**Golden threshold**: all 5 essentials pass + composite >= 80. C-04/C-05 can be marked N/A if only a single invocation mode is being evaluated (denominator adjusts to 3 essentials).
