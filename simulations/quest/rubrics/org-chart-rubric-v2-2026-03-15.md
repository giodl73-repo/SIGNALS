---
skill: quest-rubric
skill_target: org-chart
date: 2026-03-15
version: 2
---

# Scoring Rubric -- org-chart

## Skill Summary

Generate an org structure for a product or domain: areas, divisions, committees, operating
rhythms (ROB cadence, shiprooms, architecture boards). Reads existing `.roles/` to build
from real roles. Output: `org-chart.md` with ASCII org box, headcount by area, committee
charters, and operating rhythm table. **Inertia first**: always assess whether the team can
operate without a formal org before proposing structure.

---

## Essential Criteria (60 pts total -- all must pass)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Inertia assessment present** -- Output includes an explicit evaluation of whether the team can operate without a formal org structure, *before* proposing any structure. | behavior | essential | A clearly labeled section or paragraph addresses the inertia question. It must state a conclusion (e.g., "team can operate flat up to N people" or "structure is warranted because..."). Generic filler does not pass. |
| C-02 | **ASCII org box rendered** -- Output contains an ASCII diagram showing the org hierarchy (boxes, lines, or indented tree). | format | essential | At least one ASCII org diagram is present and readable as a hierarchy. Must show at minimum two levels (e.g., top-level area -> sub-team or role). A flat list of names without hierarchy does not pass. |
| C-03 | **Roles input honored** -- When `.roles/` files exist, the org chart is built from those real roles. When absent, the skill explicitly notes it and uses inferred/placeholder roles. | correctness | essential | If roles files were available: at least one named role from `.roles/` appears in the org chart or headcount table. If no roles files: output contains an explicit statement acknowledging the absence and describing the fallback. |
| C-04 | **Headcount by area** -- Output includes a table or list showing estimated or actual headcount broken down by area or division. | coverage | essential | A distinct headcount section exists with at least two areas and a count (numeric or range) for each. A single undifferentiated total does not pass. |
| C-05 | **Operating rhythm table** -- Output includes a table of operating cadences covering at minimum ROB, a shiproom or equivalent, and one governance meeting (e.g., architecture board or steering committee). | coverage | essential | A table or structured list is present with columns for cadence name, frequency, owner/DRI, and purpose. At least three distinct rhythm entries appear. A table that combines two meetings into one row does not pass. |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Committee charters complete** -- Each committee or board listed in the operating rhythm has a mini-charter: stated purpose (one sentence), membership (roles, not names), and decision-making authority (what it decides vs. what it escalates). | depth | recommended | At least two committees have all three charter elements (purpose, membership, authority). A table row with only a name and frequency does not pass this criterion. An "OPTIONAL" label on the charter section does not pass -- the section must be enforced. |
| C-07 | **All four output sections present** -- The document contains all four canonical sections: (1) inertia assessment, (2) ASCII org diagram, (3) headcount by area, (4) operating rhythm table. | format | recommended | All four sections are identifiable by heading or clear structural separation. A document missing any one section does not pass this criterion. |
| C-08 | **Decision rights indicated** -- For each major area or division, the output notes what kinds of decisions are made at that level vs. escalated upward. | depth | recommended | At least two areas have an explicit decision-rights note (e.g., a column in the headcount table, a bullet under the org box, or a RACI hint). A generic "owns the area" statement does not pass. |

---

## Aspirational Criteria (10 pts total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Org evolution path** -- Output describes how the proposed structure should change as the team grows (e.g., at what headcount a new area splits off, when a committee becomes standing vs. ad-hoc). | depth | aspirational | At least one concrete growth trigger is stated (headcount threshold, workload signal, or milestone) with an associated structural change. Vague "the org will evolve" language does not pass. |
| C-10 | **Anti-patterns flagged** -- Output identifies at least one org anti-pattern that would be risky given the proposed structure, with a brief rationale. | depth | aspirational | A named anti-pattern (e.g., "committee capture," "too many dotted lines," "shiproom without a DRI") is called out with a one-sentence explanation of why it applies here. Generic warnings do not pass. |
| C-11 | **Inertia section steelmans the status quo** -- Before delivering the VERDICT, the inertia assessment includes a sub-section or named paragraph that explicitly argues in favor of remaining flat -- listing the strongest reasons the current state works. | depth | aspirational | A clearly labeled "status-quo defense" or equivalent presents at least two reasons to stay flat, followed by the rebuttal and VERDICT. A VERDICT that immediately condemns the status quo without presenting its defense does not pass. |
| C-12 | **Decides/Escalates split in decision rights** -- Decision rights are expressed as two separate fields or columns: decisions made autonomously at this level, and decisions that escalate upward. | depth | aspirational | At least two areas have both a Decides field and an Escalates field populated with distinct, concrete content. A single "Decision Scope" description or "owns X" phrase does not pass, even if decision language is present. |
| C-13 | **Inertia verdict includes re-assessment trigger** -- The VERDICT states a specific, concrete condition -- headcount threshold, coordination-failure signal, or milestone -- at which the verdict would be revisited. | behavior | aspirational | A concrete re-assessment trigger appears in or immediately adjacent to the VERDICT. Vague language such as "revisit as the team grows" does not pass. The trigger must name a threshold (e.g., "when headcount exceeds 12" or "when the on-call rotation spans more than two areas"). |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Publishable, meets full contract |
| Acceptable | all essential + 70-79 | Usable, recommended gaps noted |
| Partial | >= 3 essential + any score | Needs rework before use |
| Failing | < 3 essential pass | Not useful; regenerate |

---

## Round 1 Reference Scores

| Variation | Essential | Recommended | Aspirational | Total | Band |
|-----------|-----------|-------------|--------------|-------|------|
| V-01 | 5/5 (60) | 1/3 (10) | 0/5 (0) | 70 | Acceptable |
| V-02 | 5/5 (60) | 2.5/3 (25) | 0/5 (0) | 85 | Golden-adjacent |
| V-03 | 5/5 (60) | 2.5/3 (25) | 0/5 (0) | 85 | Golden-adjacent |
| V-04 | 5/5 (60) | 3/3 (30) | 0/5 (0) | 90 | Golden |
| V-05 | 5/5 (60) | 3/3 (30) | 1/5 (2) | 92 | Golden |

*V-05 earns partial C-13 credit (re-assessment trigger present, concrete threshold stated); C-09
partial credit not awarded (trigger precedes structure adoption rather than describing post-
adoption structural evolution).*

---

## Evaluator Notes

- **C-01 is the hardest to fake** -- a skill that jumps straight to org boxes without the
  inertia check has missed the core design principle. Fail immediately if absent.
- **C-03 requires inspecting the run context** -- check whether `.roles/` was populated
  before scoring. The pass condition differs by whether roles existed.
- **C-05 rhythm table** -- "ROB" is the minimum anchor; a skill that only lists ROB with no
  shiproom or governance meeting scores lower even if technically present.
- **C-06 OPTIONAL label is a FAIL** -- if the charter section exists but is labeled optional,
  score as FAIL. The mechanism being present is not enough; it must be enforced.
- **C-11 vs C-01** -- C-01 requires any inertia conclusion; C-11 requires the steelman first.
  A run can pass C-01 and fail C-11 if it jumps straight to the verdict.
- **C-12 vs C-08** -- C-08 requires decision rights exist; C-12 requires the Decides/Escalates
  split specifically. A run with a single "Decision Scope" column passes C-08, fails C-12.
- **C-13 vs C-09** -- C-13 is about when to revisit the decision to structure at all (inertia
  reversal trigger). C-09 is about how structure evolves *after* adoption. They test different
  things and are scored independently.
- **Aspirational criteria are fully independent** -- C-09 through C-13 can each pass or fail
  separately; passing any one does not imply the others.
