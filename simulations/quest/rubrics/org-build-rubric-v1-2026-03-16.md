---
skill: quest-rubric
skill_target: org-build
date: 2026-03-16
version: 1
---

# Scoring Rubric — org-build

`org-build` produces two outputs from a single invocation: (1) an `org-chart.md` with ASCII
hierarchy, headcount table, operating rhythm, and committee charters, and (2) a set of typed
`.roles/{area}/{role}.md` files with five required fields per role. The rubric tests both
artifacts. Standard depth targets 20-30 roles; deep targets 50+.

---

## Essential Criteria

All essential criteria must pass. Any single failure disqualifies the output regardless of
composite score.

| ID   | Text | Category | Pass Condition |
|------|------|----------|----------------|
| C-01 | **org-chart.md present with ASCII hierarchy** | correctness | File `org-chart.md` (or equivalent named artifact) exists and contains an ASCII box/line diagram showing at minimum two org levels. A flat list of names without parent-child structure fails. |
| C-02 | **All five role fields present in every .roles/ file** | correctness | Every `.roles/{area}/{role}.md` file contains all five fields: `orientation`, `lens`, `expertise`, `scope`, `collaborates_with`. Any role file missing one or more fields fails this criterion. |
| C-03 | **inertia-advocate role always present** | correctness | A role file whose name or title contains `inertia` or `advocate` (case-insensitive) exists under `.roles/`. The inertia-advocate is the devil's-advocate role whose job is to challenge every proposal with why the status quo is sufficient. Absence fails unconditionally. |
| C-04 | **Role count within depth range** | coverage | Standard depth: 20-30 role files total. Deep depth: 50+ role files total. Fewer than the lower bound fails. Exceeding the upper bound by more than 20% without the deep flag also fails (signals padding, not depth). |
| C-05 | **Headcount by area table present** | format | `org-chart.md` contains a table with columns `Area`, `Headcount`, `Key Roles`, `Decides`, and `Escalates`. A table with only `Area` and `Headcount` (no decision columns) fails. |

---

## Recommended Criteria

Output is meaningfully better when these pass. Failure here penalizes score but does not
disqualify.

| ID   | Text | Category | Pass Condition |
|------|------|----------|----------------|
| C-06 | **Role files grouped by area in subdirectories** | format | `.roles/` contains at minimum two area subdirectories (e.g., `.roles/engineering/`, `.roles/operations/`). All roles dumped flat into `.roles/` with no area grouping fails. |
| C-07 | **Operating rhythm table and committee charters complete** | depth | `org-chart.md` contains an operating rhythm table with at minimum three distinct rows (ROB, a shiproom/gate, and a governance meeting) AND a charter for each governance meeting listing all five charter fields: `Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`. A quorum field must use the fraction format `N of M member roles`. Missing any charter or any charter field fails. |
| C-08 | **Inertia assessment reaches VERDICT with FLAT-CASE-PRESSURE rating** | depth | `org-chart.md` contains an Inertia Assessment section with a `FLAT-CASE-PRESSURE:` line using one of the closed-set ratings (`Strong (5)` / `Moderate (4)` / `Weak (3)` / `Negligible (2)` / `Insufficient (1)`) and a `VERDICT` of either `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Generic prose without a rated verdict fails. |

---

## Aspirational Criteria

Raise the bar once essential and recommended are stable.

| ID   | Text | Category | Pass Condition |
|------|------|----------|----------------|
| C-09 | **Org Evolution Roadmap with typed triggers** | depth | `org-chart.md` contains an Org Evolution Roadmap table with at minimum two rows where Row 1 is a headcount threshold trigger and Row 2 is from a different category (workload signal, structural symptom, or milestone event). Both rows have `Trigger`, `Structural Change`, and `Type` columns populated. Two headcount thresholds fails. |
| C-10 | **Anti-Pattern Watch uses cat-N typed citations** | correctness | `org-chart.md` contains an Anti-Pattern Watch table with at minimum two rows. Every `Why It Applies Here` cell opens with `[element name] (cat-N) —` syntax referencing a category from the ORG-ELEMENT REGISTER. Generic prose without typed citations fails. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band | Composite | Meaning |
|------|-----------|---------|
| Golden | >= 80 + all essential | Publishable, meets spec |
| Passing | >= 65 + all essential | Usable with minor gaps |
| Failing | any essential fails OR < 65 | Not useful as-is |

---

## Quick-Reference Checklist

```
ESSENTIAL (must all pass)
[ ] C-01  org-chart.md exists with 2-level ASCII hierarchy
[ ] C-02  every .roles/ file has all 5 fields
[ ] C-03  inertia-advocate role present
[ ] C-04  role count in depth range (std: 20-30, deep: 50+)
[ ] C-05  headcount table has Area/Headcount/KeyRoles/Decides/Escalates

RECOMMENDED (penalizes if missing)
[ ] C-06  role files grouped by area subdirectories
[ ] C-07  rhythm table (3+ rows) + committee charters (5 fields + N-of-M quorum)
[ ] C-08  inertia assessment with FLAT-CASE-PRESSURE rating + VERDICT

ASPIRATIONAL (raises bar)
[ ] C-09  org evolution roadmap with typed triggers (headcount + different category)
[ ] C-10  anti-pattern watch with cat-N typed citations
```

---

*Generated by: /quest-rubric org-build — 2026-03-16*
