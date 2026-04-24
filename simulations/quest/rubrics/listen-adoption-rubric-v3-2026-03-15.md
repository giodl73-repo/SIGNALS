Written to `simulations/quest/rubrics/listen-adoption-rubric-v3-2026-03-15.md`.

---

**Changes from v2 to v3:**

Two new aspirational criteria extracted from R2 excellence signals:

- **C-14: Phase-Embedded Champion Formation** — from V-05's "Champion forming?" entries inside monthly simulation blocks. The distinction from C-09 and C-12: those criteria govern *what* the champion table contains; C-14 governs *where* champion causality appears — inside the simulation timeline itself, not in a satellite table. This is the structural device that moved V-03 from PARTIAL to PASS on C-09: timing was finally *structurally required* at the simulation phase block, not just inferable from context.

- **C-15: Cited Role-to-Month Traceability Audit** — from V-02/V-05's Axis-A audit block. The distinction from C-08 and C-13(a): C-08 requires roles to be traceable; C-15 requires each traceability claim to carry a citation back to the simulation row. No role passes on assertion alone. Transforms C-08's narrative traceability into a mechanically checkable audit.

**Scoring formula update:** aspirational denominator changed from 5 to 7. Maximum composite remains 100; aspirational band (10 points) is now split across 7 criteria at ~1.43 points each. A V-05-equivalent output passing all 15 criteria scores 100.
ed roles appear in at least one simulation row.

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

**C-14** — Phase-Embedded Champion Formation
Weight: aspirational | Category: depth
*From R2 excellence: V-05 embeds champion formation entries inside monthly simulation
blocks, making champion emergence a first-class simulation event. A satellite champion
table without this embedding leaves C-09 at PARTIAL because timing is only inferable, not
structurally required.*
The month-by-month simulation contains, within the phase blocks where champions first
emerge, an explicit champion formation entry naming: (a) the role becoming a champion,
(b) the bridging mechanism, and (c) the specific incumbent argument that champion is
positioned to answer. Champion causality is a live simulation event, not a post-hoc
annotation in a separate table.
**Pass condition**: At least one simulation phase block (in the month-by-month section)
contains an embedded champion formation entry with role, mechanism, and incumbent argument
targeted, pinned to a specific month.

**C-15** — Cited Role-to-Month Traceability Audit
Weight: aspirational | Category: coverage
*From R2 excellence: V-02 and V-05 add an Axis-A audit block that cites each of the 16
roles back to the specific simulation row evidencing their adoption month. C-08 requires
traceability to be present in the narrative; this criterion requires it to be mechanically
checkable — no role passes on assertion alone.*
A dedicated audit block or table lists every one of the 16 roles with: (a) the specific
adoption month, and (b) a citation back to the simulation phase block or row that evidences
the claim. Traceability is verified, not narrated.
**Pass condition**: An audit table or block lists all 16 roles with adoption month and
simulation source citation; no role appears with a month claim without a supporting
citation.

---

## Scoring Formula

```
essential_score    = (essential criteria passed / 5) * 60
recommended_score  = (recommended criteria passed / 3) * 30
aspirational_score = (aspirational criteria passed / 7) * 10

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
| v3      | 2026-03-15 | Add C-14 (phase-embedded champion formation), C-15 (cited role-to-month traceability audit) from R2 excellence signals; aspirational denominator 5 -> 7 |
