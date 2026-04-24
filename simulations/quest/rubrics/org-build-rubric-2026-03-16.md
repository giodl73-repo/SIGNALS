---
skill: quest-rubric
skill_target: org-build
date: 2026-03-16
version: 1
---

# Scoring Rubric — org-build

## Essential Criteria (5)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| **C-01** | org-chart.md present with ASCII hierarchy | correctness | File exists and contains an ASCII box/line diagram with min 2 org levels. Flat name list fails. |
| **C-02** | All five role fields present in every .roles/ file | correctness | Every role file contains `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`. Any missing field fails. |
| **C-03** | inertia-advocate role always present | correctness | A role file with `inertia` or `advocate` in name/title exists under `.roles/`. Absence fails unconditionally. |
| **C-04** | Role count within depth range | coverage | Standard: 20-30 files. Deep: 50+. Below lower bound fails. Exceeding upper bound by >20% without deep flag also fails. |
| **C-05** | Headcount by area table present | format | org-chart.md has table with `Area`, `Headcount`, `Key Roles`, `Decides`, `Escalates` columns. Table without Decides/Escalates fails. |

## Recommended Criteria (3)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| **C-06** | Role files grouped by area subdirectories | format | `.roles/` has min 2 area subdirs. All roles flat with no grouping fails. |
| **C-07** | Operating rhythm table and committee charters complete | depth | Rhythm table with 3+ distinct rows (ROB + shiproom + governance) AND a charter per governance meeting with all 5 fields including Quorum as `N of M` fraction. |
| **C-08** | Inertia assessment reaches VERDICT with FLAT-CASE-PRESSURE rating | depth | org-chart.md contains `FLAT-CASE-PRESSURE:` with a closed-set rating and a `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED` verdict. Generic prose without rated verdict fails. |

## Aspirational Criteria (2)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| **C-09** | Org Evolution Roadmap with typed triggers | depth | 2+ rows: Row 1 is headcount threshold, Row 2 is different category. Two headcount thresholds fails. |
| **C-10** | Anti-Pattern Watch uses cat-N typed citations | correctness | 2+ rows where every "Why It Applies Here" cell opens with `[element name] (cat-N) —` syntax. Plain prose fails. |

## Formula

```
composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)
```

**Golden threshold**: all 5 essential pass + composite >= 80.

Saved to `simulations/quest/rubrics/org-build-rubric-v1-2026-03-16.md`.
