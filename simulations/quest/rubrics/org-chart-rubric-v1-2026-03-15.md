---
skill: quest-rubric
skill_target: org-chart
date: 2026-03-15
version: 1
---

# Scoring Rubric — org-chart

## Skill Summary

Generate an org structure for a product or domain: areas, divisions, committees, operating
rhythms (ROB cadence, shiprooms, architecture boards). Reads existing `.roles/` to build
from real roles. Output: `org-chart.md` with ASCII org box, headcount by area, committee
charters, and operating rhythm table. **Inertia first**: always assess whether the team can
operate without a formal org before proposing structure.

---

## Essential Criteria (60 pts total — all must pass)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Inertia assessment present** — Output includes an explicit evaluation of whether the team can operate without a formal org structure, *before* proposing any structure. | behavior | essential | A clearly labeled section or paragraph addresses the inertia question. It must state a conclusion (e.g., "team can operate flat up to N people" or "structure is warranted because…"). Generic filler does not pass. |
| C-02 | **ASCII org box rendered** — Output contains an ASCII diagram showing the org hierarchy (boxes, lines, or indented tree). | format | essential | At least one ASCII org diagram is present and readable as a hierarchy. Must show at minimum two levels (e.g., top-level area → sub-team or role). A flat list of names without hierarchy does not pass. |
| C-03 | **Roles input honored** — When `.roles/` files exist, the org chart is built from those real roles. When absent, the skill explicitly notes it and uses inferred/placeholder roles. | correctness | essential | If roles files were available: at least one named role from `.roles/` appears in the org chart or headcount table. If no roles files: output contains an explicit statement acknowledging the absence and describing the fallback. |
| C-04 | **Headcount by area** — Output includes a table or list showing estimated or actual headcount broken down by area or division. | coverage | essential | A distinct headcount section exists with at least two areas and a count (numeric or range) for each. A single undifferentiated total does not pass. |
| C-05 | **Operating rhythm table** — Output includes a table of operating cadences covering at minimum ROB, a shiproom or equivalent, and one governance meeting (e.g., architecture board or steering committee). | coverage | essential | A table or structured list is present with columns for cadence name, frequency, owner/DRI, and purpose. At least three distinct rhythm entries appear. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Committee charters complete** — Each committee or board listed in the operating rhythm has a mini-charter: stated purpose (one sentence), membership (roles, not names), and decision-making authority (what it decides vs. what it escalates). | depth | recommended | At least two committees have all three charter elements (purpose, membership, authority). A table row with only a name and frequency does not pass this criterion. |
| C-07 | **All four output sections present** — The document contains all four canonical sections: (1) inertia assessment, (2) ASCII org diagram, (3) headcount by area, (4) operating rhythm table. | format | recommended | All four sections are identifiable by heading or clear structural separation. A document missing any one section does not pass this criterion. |
| C-08 | **Decision rights indicated** — For each major area or division, the output notes what kinds of decisions are made at that level vs. escalated upward. | depth | recommended | At least two areas have an explicit decision-rights note (e.g., a column in the headcount table, a bullet under the org box, or a RACI hint). A generic "owns the area" statement does not pass. |

---

## Aspirational Criteria (10 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Org evolution path** — Output describes how the proposed structure should change as the team grows (e.g., at what headcount a new area splits off, when a committee becomes standing vs. ad-hoc). | depth | aspirational | At least one concrete growth trigger is stated (headcount threshold, workload signal, or milestone) with an associated structural change. Vague "the org will evolve" language does not pass. |
| C-10 | **Anti-patterns flagged** — Output identifies at least one org anti-pattern that would be risky given the proposed structure, with a brief rationale. | depth | aspirational | A named anti-pattern (e.g., "committee capture," "too many dotted lines," "shiproom without a DRI") is called out with a one-sentence explanation of why it applies here. Generic warnings do not pass. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Publishable, meets full contract |
| Acceptable | all essential + 70–79 | Usable, recommended gaps noted |
| Partial | >= 3 essential + any score | Needs rework before use |
| Failing | < 3 essential pass | Not useful; regenerate |

---

## Evaluator Notes

- **C-01 is the hardest to fake** — a skill that jumps straight to org boxes without the
  inertia check has missed the core design principle. Fail immediately if absent.
- **C-03 requires inspecting the run context** — check whether `.roles/` was populated
  before scoring. The pass condition differs by whether roles existed.
- **C-05 rhythm table** — "ROB" is the minimum anchor; a skill that only lists ROB with no
  shiproom or governance meeting scores lower even if technically present.
- **Aspirational criteria are independent** — C-09 and C-10 can each pass or fail separately.
