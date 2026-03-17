Written to `simulations/quest/rubrics/listen-adoption-rubric-v5-2026-03-15.md`.

---

**Changes from v4 to v5:**

Two new aspirational criteria extracted from R4 excellence:

**C-17: Preamble Downstream Citation Contract** — from V-01. The distinction from C-11:

- **vs C-11** (incumbent anchor threading): C-11 scores *backward* — did 3+ downstream sections cite the incumbent? C-17 scores *forward* — did the preamble declare which sections must cite the incumbent, enumerated by name? The contract makes citation accountability checkable at the setup stage, not only inferred from downstream content at scoring time.

The structural device: a PREAMBLE block that names at least 4 specific downstream sections (chasm, interventions, champion table, churn risks, SCHEDULE RECONCILIATION) using directive language ("must," "required," "contract") before the simulation body begins.

**C-18: Dependency Gravity Assessment** — from V-02. The distinction from C-11 and C-16:

- **vs C-11** (incumbent anchor threading): C-11 requires a named incumbent as a through-thread; C-18 requires per-role *quantified* inertia scores (1–5) that propagate as numeric anchors. Generic assertions ("delayed due to dependency") become unacceptable — deviation reasons must cite the specific gravity score.
- **vs C-16** (pre-committed schedule): C-16 requires the committed prediction column; C-18 provides the *mechanism* that justifies each committed month, distinguishing roles that slip because of gravity depth from other delay causes.

The structural device: DEPENDENCY GRAVITY ASSESSMENT in the PREAMBLE assigns scores to all 16 roles; scores propagate into SECTION 1 committed month justifications, the PHASE 3 "Gravity cluster" chasm row, or SCHEDULE RECONCILIATION deviation reasons.

**Scoring formula update:** aspirational denominator changes from 8 to 10. Maximum composite remains 100; aspirational band (10 points) is now split across 10 criteria at 1.0 point each. An output passing all 18 criteria scores 100.
 ordered
highest to lowest.

**C-05** -- Churn Risk Identification
Weight: essential | Category: coverage
At least two churn risks are named -- roles or cohorts that could disengage before reaching
full adoption -- with a brief reason for each.
**Pass condition**: 2+ named churn risks with rationale present in the output.

---

## Recommended Criteria (30% of composite)

**C-06** -- Champion Network
Weight: recommended | Category: depth
Output identifies which roles act as champions (bridges between early adopters and early
majority) and describes the mechanism by which each champion accelerates spread (e.g.,
demo culture, advocacy in standups, pairing with laggard cohort).
**Pass condition**: At least 2 named champions with a described bridging mechanism each.

**C-07** -- Quantified Adoption Curve
Weight: recommended | Category: correctness
The simulation includes numeric adoption counts or percentages at each time step, enabling
a reader to sketch an S-curve. Totals must be consistent with the 16-role stock cast.
**Pass condition**: Numeric values (count or %) for adopters at each month; values sum
correctly against the 16-role total.

**C-08** -- Full Role Coverage Traceability
Weight: recommended | Category: coverage
Every one of the 16 stock roles (PM, UX, C-01..C-12, Support, SRE) appears somewhere in
the simulation body -- not just in the mapping table. Each role's adoption month or
archetype cohort arrival is traceable.
**Pass condition**: All 16 roles referenced in simulation narrative or timeline, not only
in the initial mapping.

---

## Aspirational Criteria (10% of composite)

**C-09** -- Cross-Archetype Influence Dynamics
Weight: aspirational | Category: depth
Output models how innovators and early adopters actively influence later cohorts -- social
proof, internal case studies, tool evangelism -- distinguishing passive diffusion from active
sponsorship.
**Pass condition**: At least one explicit influence pathway described from an earlier cohort
to a later cohort, with mechanism and expected timing.

**C-10** -- Intervention Timing Tied to Simulation
Weight: aspirational | Category: behavior
Each recommended intervention is pinned to a specific month or simulation gate (e.g.,
"deploy before month 3 to prevent late-majority stall") rather than stated generically.
Interventions are sequenced in the timeline.
**Pass condition**: Every intervention in C-04 carries a month reference or simulation
gate; at least one is inserted into the month-by-month timeline.

**C-11** -- Incumbent Anchor Threading
Weight: aspirational | Category: depth
*From R1 excellence signal 3: incumbent PREAMBLE anchor propagates causal specificity
through all downstream sections from a single forcing point.*
Output names a specific incumbent tool, workflow, or behavior in a preamble block before
the simulation begins, and each subsequent section -- chasm cause, interventions, champion
table, churn risks -- references that named incumbent by name. The incumbent is the
through-thread, not a one-time mention.
**Pass condition**: A named incumbent appears in a preamble or setup block, and at least
3 downstream sections (chasm, interventions, champions, or churn) reference it explicitly.

**C-12** -- Causal Champion Column
Weight: aspirational | Category: depth
*From R1 excellence signal 1: "what argument does this champion counter?" converts champion
network from structural description to active displacement mechanism -- the only structural
device that forced C-09 to PASS.*
The champion network table or section includes an explicit column or field that names the
specific incumbent argument, objection, or habit each champion counters. This transforms
the champion listing from a passive roster into an active displacement plan.
**Pass condition**: Each named champion carries an explicit "counters / displaces /
answers" annotation identifying which incumbent advantage they are positioned to overcome.

**C-13** -- Three-Axis Gap Coverage
Weight: aspirational | Category: coverage
*From R1 excellence signal 2: format, lifecycle, and inertia axes close independent gap
types; no axis covers another's surface.*
The output demonstrates simultaneous closure across three independent gap dimensions:
(a) role completeness -- all 16 roles individually named and traceable,
(b) temporal completeness -- each action or adoption event pinned to a specific month,
(c) causal specificity -- each gap, risk, and intervention explained with a named cause
rather than generic change-resistance language.
**Pass condition**: All three dimensions present and each demonstrated by at least one
concrete, non-generic example in the output.

**C-14** -- Phase-Embedded Champion Formation
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

**C-15** -- Cited Role-to-Month Traceability Audit
Weight: aspirational | Category: coverage
*From R2 excellence: V-02 and V-05 add an Axis-A audit block that cites each of the 16
roles back to the specific simulation row evidencing their adoption month. C-08 requires
traceability to be present in the narrative; this criterion requires it to be mechanically
checkable -- no role passes on assertion alone.*
A dedicated audit block or table lists every one of the 16 roles with: (a) the specific
adoption month, and (b) a citation back to the simulation phase block or row that evidences
the claim. Traceability is verified, not narrated.
**Pass condition**: An audit table or block lists all 16 roles with adoption month and
simulation source citation in parseable format (e.g., [PHASE N / Month M / Row K]);
no role appears with a month claim without a supporting citation.

**C-16** -- Pre-committed Adoption Schedule with Reconciliation
Weight: aspirational | Category: correctness
*From R3 excellence: V-03 converts C-01's "earliest adoption month" into a committed
prediction made before the simulation runs, then closes with a SCHEDULE RECONCILIATION
block that audits committed vs actual for all 16 roles. This transforms the adoption map
from a descriptor into a falsifiable forecast.*
The distinction from C-01, C-02, and C-07: C-01 maps archetypes to an expected range;
C-16 requires a single committed month per role entered before the simulation begins,
tracked during it, and reconciled against actual outcomes at close. C-02's phase-close
ledgers confirm who adopted in that phase; C-16's reconciliation compares the
pre-committed prediction against what actually happened and names deviations.
Before the simulation begins, each role's adoption month is committed as a prediction
(column labeled "Committed adoption month," not "Earliest adoption month"). The simulation
month blocks open by listing roles committed to that month. Phase closes confirm whether
scheduled roles were met. The final phase includes a SCHEDULE RECONCILIATION block
comparing committed month to actual month for all 16 roles, with deviation reasons for
any role that missed its committed month.
**Pass condition**: SECTION 1 uses a "Committed adoption month" column (not "Earliest");
each simulation month block includes a committed-roles prompt; PHASE 5 CLOSE contains a
SCHEDULE RECONCILIATION block with committed vs actual status for all 16 roles.

**C-17** -- Preamble Downstream Citation Contract
Weight: aspirational | Category: depth
*From R4 V-01 excellence: the PREAMBLE enumerates the specific downstream sections
required to cite the named incumbent by name, creating a forward-declared accountability
contract that is checkable before the simulation runs.*
The distinction from C-11: C-11 scores backward -- did 3+ downstream sections cite the
incumbent? C-17 scores forward -- did the preamble declare which sections must cite the
incumbent, naming them explicitly? The enumerated contract converts C-11's post-hoc audit
into a pre-committed obligation, making citation accountability visible at the structural
setup stage rather than only at scoring time.
The PREAMBLE includes an explicit list of downstream sections (at minimum: chasm,
interventions, champion table, churn risks, and SCHEDULE RECONCILIATION) that are
required to cite the named incumbent by name. The list is stated as a contract or
requirement, not as a summary of what was done.
**Pass condition**: The PREAMBLE enumerates at least 4 named downstream sections obligated
to cite the incumbent; the enumeration is forward-declared (appears before the simulation
body) and uses directive language (e.g., "must," "required," "contract").

**C-18** -- Dependency Gravity Assessment
Weight: aspirational | Category: correctness
*From R4 V-02 excellence: a per-role dependency gravity score (1-5) in the PREAMBLE
provides a numeric anchor that mechanically justifies committed adoption months, identifies
the gravity cluster as the early-majority barrier, and forces specific deviation reasoning
in SCHEDULE RECONCILIATION -- making "delayed due to dependency" a claim that must cite a
score, not a generic assertion.*
The distinction from C-11 (incumbent anchor threading): C-11 requires a named incumbent as
a through-thread across sections; C-18 requires per-role quantified inertia scores that
propagate as numeric anchors. From C-16 (pre-committed schedule): C-16 requires the
prediction column; C-18 provides the mechanism that justifies each committed month,
distinguishing roles that slip because of gravity depth from those that slip for other
reasons. The structural device that elevates C-16 quality: deviation reasons can no longer
read "delayed due to incumbent dependency" -- they must read "delayed -- gravity 4:
[specific hold the incumbent had for this role]."
A DEPENDENCY GRAVITY ASSESSMENT block in the preamble assigns a numeric score (1-5) to
each of the 16 roles before the simulation begins. These scores propagate into at least one
of: (a) SECTION 1 committed month column (high-gravity roles receive later committed months,
with gravity score cited as justification), (b) PHASE 3 chasm table as a "Gravity cluster"
row identifying which high-gravity roles form the early-majority barrier, or (c) SCHEDULE
RECONCILIATION deviation reason column (delay explanation must cite the specific gravity
score, not generic dependency language).
**Pass condition**: PREAMBLE assigns a dependency gravity score (1-5 scale) to each of
the 16 roles; at least one downstream section (SECTION 1 committed month justification,
PHASE 3 chasm table, or SCHEDULE RECONCILIATION deviation reason) cites a specific gravity
score as a cause rather than using generic dependency language.

---

## Scoring Formula

```
essential_score    = (essential criteria passed / 5) * 60
recommended_score  = (recommended criteria passed / 3) * 30
aspirational_score = (aspirational criteria passed / 10) * 10

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
| v4      | 2026-03-15 | Add C-16 (pre-committed adoption schedule with reconciliation) from R3 V-03 excellence signal; aspirational denominator 7 -> 8 |
| v5      | 2026-03-15 | Add C-17 (preamble downstream citation contract) from R4 V-01 excellence; add C-18 (dependency gravity assessment) from R4 V-02 excellence; aspirational denominator 8 -> 10 |
