Rubric written to `simulations/quest/rubrics/listen-adoption-rubric-v2-2026-03-15.md`.

**Changes from v1 to v2:**

Three new aspirational criteria extracted from R1 excellence signals:

- **C-11: Incumbent Anchor Threading** — from signal 3. Names a specific incumbent in a preamble block and requires at least 3 downstream sections (chasm, interventions, champions, churn) to reference it by name. The incumbent is the through-thread, not a one-time mention.

- **C-12: Causal Champion Column** — from signal 1. Each champion carries an explicit "counters / displaces / answers" annotation. This is what took C-09 from PARTIAL to PASS in every prior variation — it forces the champion table from passive roster to active displacement plan.

- **C-13: Three-Axis Gap Coverage** — from signal 2. Simultaneous closure of all three independent gap types: (a) role completeness, (b) temporal completeness, (c) causal specificity. Framed as a coverage criterion so the evaluator checks all three are present, not just two.

**Scoring formula update:** aspirational denominator changed from 2 to 5. The maximum composite is still 100; the aspirational band (10 points) is now split across 5 criteria at 2 points each rather than 5 points each. A V-05-equivalent output that passes all 13 criteria still scores 100.
itly identifies the chasm: the gap between early-adopter exit and early-majority
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

**C-11** — Incumbent Anchor Threading
Weight: aspirational | Category: depth
*From R1 excellence signal 3: incumbent PREAMBLE anchor propagates causal specificity
through all downstream sections from a single forcing point.*
Output names a specific incumbent tool, workflow, or behavior in a preamble block before
the simulation begins, and each subsequent section — chasm cause, interventions, champion
table, churn risks — references that named incumbent by name. The incumbent is the
through-thread, not a one-time mention.
**Pass condition**: A named incumbent appears in a preamble or setup block, and at least
3 downstream sections (chasm, interventions, champions, or churn) reference it explicitly.

**C-12** — Causal Champion Column
Weight: aspirational | Category: depth
*From R1 excellence signal 1: "what argument does this champion counter?" converts champion
network from structural description to active displacement mechanism — the only structural
device that forced C-09 to PASS.*
The champion network table or section includes an explicit column or field that names the
specific incumbent argument, objection, or habit each champion counters. This transforms
the champion listing from a passive roster into an active displacement plan.
**Pass condition**: Each named champion carries an explicit "counters / displaces /
answers" annotation identifying which incumbent advantage they are positioned to overcome.

**C-13** — Three-Axis Gap Coverage
Weight: aspirational | Category: coverage
*From R1 excellence signal 2: format, lifecycle, and inertia axes close independent gap
types; no axis covers another's surface.*
The output demonstrates simultaneous closure across three independent gap dimensions:
(a) role completeness — all 16 roles individually named and traceable,
(b) temporal completeness — each action or adoption event pinned to a specific month,
(c) causal specificity — each gap, risk, and intervention explained with a named cause
rather than generic change-resistance language.
**Pass condition**: All three dimensions present and each demonstrated by at least one
concrete, non-generic example in the output.

---

## Scoring Formula

```
essential_score    = (essential criteria passed / 5) * 60
recommended_score  = (recommended criteria passed / 3) * 30
aspirational_score = (aspirational criteria passed / 5) * 10

composite = essential_score + recommended_score + aspirational_score
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band   | Composite             | Meaning                              |
|--------|-----------------------|--------------------------------------|
| Gold   | >= 80, all essential  | Ship-ready signal                    |
| Silver | 65-79                 | Useful, gaps in depth or coverage    |
| Bronze | 50-64                 | Structurally present, weak specifics |
| Fail   | < 50 or any essential | Not yet useful                       |

---

## Version History

| Version | Date       | Change |
|---------|------------|--------|
| v1      | 2026-03-15 | Initial rubric -- 5E / 3R / 2A |
| v2      | 2026-03-15 | Add C-11 (incumbent anchor threading), C-12 (causal champion column), C-13 (three-axis gap coverage) from R1 excellence signals; aspirational denominator 2 -> 5 |
