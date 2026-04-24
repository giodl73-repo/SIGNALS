Written to `simulations/quest/rubrics/listen-adoption-rubric-v6-2026-03-15.md`.

---

**Changes from v5 to v6:**

Two new aspirational criteria extracted from R5 excellence:

**C-19: Citation Contract Closure Audit** -- from V-01. The distinction from C-17:

- **vs C-17** (preamble downstream citation contract): C-17 scores *forward* -- did the preamble declare which sections must cite the incumbent? C-19 scores *backward* -- did the artifact close the contract by auditing each declared row at artifact end? C-17 is a promise; C-19 is the checksum that verifies the promise was honored, without requiring an external scorer to hunt through the artifact.

The structural device: a CITATION CONTRACT TABLE in the PREAMBLE with section / required form / directive / Met? columns (Met? blank at declaration), plus a CONTRACT COMPLIANCE AUDIT block at artifact close that fills every Met? row with PASS/FAIL + direct evidence citation.

**C-20: Typed Gravity Citation Mandate** -- from V-02. The distinction from C-18:

- **vs C-18** (dependency gravity assessment): C-18 requires per-role gravity scores and at least one downstream section citing a score. C-20 mandates the typed format `G[N]: [exact behavior THE INCUMBENT had for this role]` for every gravity-citing deviation reason in SCHEDULE RECONCILIATION -- generic forms ("delayed due to dependency," "gravity 4: strong dependency") are explicitly prohibited by a stated rule. C-20 also requires the DEPENDENCY GRAVITY ASSESSMENT to add a "Derived month range" column computed from gravity scores *before* SECTION 1, so C-16's committed months are traceable to a derivation rather than asserted.

The structural devices: (a) "Derived month range" column in the PREAMBLE gravity table, (b) TYPED GRAVITY CITATION RULE header in SCHEDULE RECONCILIATION with format mandate and explicit rejection of generic forms, (c) compliance ledger check in at least one phase close.

**Scoring formula update:** aspirational denominator changes from 10 to 12. Maximum composite remains 100; aspirational band (10 points) is now split across 12 criteria at ~0.833 points each. An output passing all 20 criteria scores 100.
s or cohorts that could disengage before reaching
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

**C-19** -- Citation Contract Closure Audit
Weight: aspirational | Category: depth
*From R5 V-01 excellence: upgrading C-17's pipe-list contract to a structured CITATION
CONTRACT TABLE plus a closing CONTRACT COMPLIANCE AUDIT makes the citation obligation
self-verifying. C-17 is a forward declaration; C-19 is the backward closure that confirms
the contract was honored without requiring an external scorer to hunt through the artifact.*
The distinction from C-17: C-17 requires the preamble to declare which sections must cite
the incumbent (forward contract). C-19 requires the artifact to close that contract by
auditing each declared row at the end -- producing PASS/FAIL per section with evidence
citation. The contract becomes a checksum, not a promise.
The structural device: a CITATION CONTRACT TABLE in the PREAMBLE lists each obligated
section with columns for required form, directive, and a Met? field (initially blank). At
artifact close, a CONTRACT COMPLIANCE AUDIT block returns to each table row and fills Met?
with PASS or FAIL plus a direct evidence citation (e.g., "PASS -- SECTION 3, row 2:
'[incumbent] dependency cited as bridge blocker'").
**Pass condition**: A CITATION CONTRACT TABLE appears in the PREAMBLE with at least 4
section rows and an explicit Met? or compliance column; a CONTRACT COMPLIANCE AUDIT block
appears at artifact close and fills each row's compliance status with PASS/FAIL and
evidence; every section declared in the contract receives a verdict.

**C-20** -- Typed Gravity Citation Mandate
Weight: aspirational | Category: correctness
*From R5 V-02 excellence: adding a "Derived month range" column to the DEPENDENCY GRAVITY
ASSESSMENT and enforcing a TYPED GRAVITY CITATION RULE in SCHEDULE RECONCILIATION closes
the gap C-18 leaves open. C-18 requires a gravity score to appear downstream; C-20 requires
the downstream citation to name both the score and the specific incumbent behavior it
encodes -- eliminating gravity scores that appear but carry no causal content.*
The distinction from C-18: C-18 requires per-role gravity scores and at least one
downstream reference citing a score. C-20 tightens the downstream requirement to a typed
format: `G[N]: [exact behavior THE INCUMBENT had for this role]`. Generic forms such as
"delayed due to dependency" or "gravity 4: strong dependency" are explicitly prohibited.
Additionally, C-20 requires the DEPENDENCY GRAVITY ASSESSMENT to include a "Derived month
range" column that mechanically translates each gravity score into an expected adoption
month range before SECTION 1 is written, so committed months in C-16 are traceable to a
gravity derivation rather than asserted.
The structural devices:
(a) DEPENDENCY GRAVITY ASSESSMENT in the PREAMBLE adds a "Derived month range" column
computed from the gravity score (e.g., G5 -> month 7-9, G1 -> month 1-2), filled before
SECTION 1 committed months are entered.
(b) SCHEDULE RECONCILIATION includes a TYPED GRAVITY CITATION RULE header that states the
mandatory format and explicitly rejects generic dependency language.
(c) Every deviation reason in SCHEDULE RECONCILIATION that references gravity must use the
typed format; compliance ledger checks in at least one phase close verify the rule is met.
**Pass condition**: DEPENDENCY GRAVITY ASSESSMENT includes a "Derived month range" column
with values filled before SECTION 1; SCHEDULE RECONCILIATION contains a TYPED GRAVITY
CITATION RULE header or stated format mandate; at least one deviation reason uses the typed
format `G[N]: [specific incumbent behavior]`; generic-only deviation reasons are absent
for any role citing gravity as cause.

---

## Scoring Formula

```
essential_score    = (essential criteria passed / 5) * 60
recommended_score  = (recommended criteria passed / 3) * 30
aspirational_score = (aspirational criteria passed / 12) * 10

composite = essential_score + recommended_score + aspirational_score
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

PARTIAL credit: a criterion scored PARTIAL counts as 0.5 toward the numerator.

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
| v6      | 2026-03-15 | Add C-19 (citation contract closure audit) from R5 V-01 excellence; add C-20 (typed gravity citation mandate) from R5 V-02 excellence; aspirational denominator 10 -> 12 |
