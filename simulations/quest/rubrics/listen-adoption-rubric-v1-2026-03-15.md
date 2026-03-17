---
skill: quest-rubric
skill_target: listen-adoption
date: 2026-03-15
version: 1
---

# Rubric: listen-adoption

Scores adoption simulation output for the Signal plugin skill. The skill maps stock roles
to Rogers archetypes, runs a month-by-month simulation, identifies the chasm, surfaces
champion networks and churn risks, and ranks interventions by adoption delta.

---

## Essential Criteria (60% of composite)

**C-01** — Rogers Archetype Mapping
Weight: essential | Category: correctness
Every stock role (PM, UX, C-01 through C-12, Support, SRE — 16 total) is assigned to
exactly one Rogers archetype (innovator / early-adopter / early-majority / late-majority /
laggard). No role is omitted. No role carries two archetypes.
**Pass condition**: All 16 roles appear in the mapping table with a valid archetype label.

**C-02** — Month-by-Month Adoption Simulation
Weight: essential | Category: correctness
Output contains a chronological simulation across at least 3 months. Each month names
which archetype cohort (or specific roles) first try or adopt the feature, and what
mechanism drives the spread (demo, pairing, mandate, etc.).
**Pass condition**: Minimum 3 time steps present; each step identifies who adopts and why.

**C-03** — Chasm Analysis
Weight: essential | Category: depth
Output explicitly identifies the chasm: the gap between early-adopter exit and early-majority
entry. Must state what causes the gap for this specific feature/context and what is at risk
if the chasm is not bridged.
**Pass condition**: A dedicated chasm section or paragraph names the gap, its cause, and the
risk of stall.

**C-04** — Intervention Recommendations Ranked by Adoption Delta
Weight: essential | Category: behavior
At least 3 interventions are listed. Each carries an explicit adoption delta (e.g., "+2 roles
in month 4", "+15% coverage by Q2") so recommendations are orderable. The highest-delta
intervention appears first.
**Pass condition**: List of 3+ interventions, each with a stated adoption delta, ordered
highest to lowest.

**C-05** — Churn Risk Identification
Weight: essential | Category: coverage
At least two churn risks are named — roles or cohorts that could disengage before reaching
full adoption — with a brief reason for each.
**Pass condition**: 2+ named churn risks with rationale present in the output.

---

## Recommended Criteria (30% of composite)

**C-06** — Champion Network
Weight: recommended | Category: depth
Output identifies which roles act as champions (bridges between early adopters and early
majority) and describes the mechanism by which each champion accelerates spread (e.g.,
demo culture, advocacy in standups, pairing with laggard cohort).
**Pass condition**: At least 2 named champions with a described bridging mechanism each.

**C-07** — Quantified Adoption Curve
Weight: recommended | Category: correctness
The simulation includes numeric adoption counts or percentages at each time step, enabling
a reader to sketch an S-curve. Totals must be consistent with the 16-role stock cast.
**Pass condition**: Numeric values (count or %) for adopters at each month; values sum
correctly against the 16-role total.

**C-08** — Full Role Coverage Traceability
Weight: recommended | Category: coverage
Every one of the 16 stock roles (PM, UX, C-01..C-12, Support, SRE) appears somewhere in
the simulation body — not just in the mapping table. Each role's adoption month or
archetype cohort arrival is traceable.
**Pass condition**: All 16 roles referenced in simulation narrative or timeline, not only
in the initial mapping.

---

## Aspirational Criteria (10% of composite)

**C-09** — Cross-Archetype Influence Dynamics
Weight: aspirational | Category: depth
Output models how innovators and early adopters actively influence later cohorts — social
proof, internal case studies, tool evangelism — distinguishing passive diffusion from active
sponsorship.
**Pass condition**: At least one explicit influence pathway described from an earlier cohort
to a later cohort, with mechanism and expected timing.

**C-10** — Intervention Timing Tied to Simulation
Weight: aspirational | Category: behavior
Each recommended intervention is pinned to a specific month or simulation gate (e.g.,
"deploy before month 3 to prevent late-majority stall") rather than stated generically.
Interventions are sequenced in the timeline.
**Pass condition**: Every intervention in C-04 carries a month reference or simulation
gate; at least one is inserted into the month-by-month timeline.

---

## Scoring Formula

```
essential_score   = (essential criteria passed / 5) * 60
recommended_score = (recommended criteria passed / 3) * 30
aspirational_score = (aspirational criteria passed / 2) * 10

composite = essential_score + recommended_score + aspirational_score
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band | Composite | Meaning |
|------|-----------|---------|
| Gold | >= 80, all essential pass | Ship-ready signal |
| Silver | 65–79 | Useful, gaps in depth or coverage |
| Bronze | 50–64 | Structurally present, weak on specifics |
| Fail | < 50 or any essential fails | Not yet useful |
