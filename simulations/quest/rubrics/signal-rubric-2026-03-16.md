Rubric written to `simulations/quest/rubrics/signal-rubric-v1-2026-03-16.md`.

---

**Summary of criteria:**

| ID | Weight | Category | Text |
|----|--------|----------|------|
| C-01 | essential | correctness | All 12 namespaces present |
| C-02 | essential | correctness | Sub-skill counts match canonical registry |
| C-03 | essential | coverage | Every sub-skill has a one-line description in non-bare mode |
| C-04 | essential | behavior | `/signal <namespace>` filters to that namespace only |
| C-05 | essential | behavior | `/signal --bare` produces only command names |
| C-06 | recommended | depth | Descriptions are specific and differentiating |
| C-07 | recommended | format | Visual hierarchy — sub-skills subordinate to namespace headers |
| C-08 | recommended | behavior | Routing hint per namespace ("describe your need") |
| C-09 | aspirational | format | Skill count in namespace header |
| C-10 | aspirational | depth | T3 tier annotations on T3-only skills |

**Golden threshold**: all 5 essential pass + composite >= 80.
