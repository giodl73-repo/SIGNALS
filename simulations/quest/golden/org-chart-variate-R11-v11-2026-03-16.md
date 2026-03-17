---
skill: quest-variate
skill_target: org-chart
date: 2026-03-16
round: R11
rubric_version: v11
status: variate
---

# org-chart Variate -- Round 11 (Rubric v11)

**Date:** 2026-03-16
**Skill:** org-chart
**Rubric:** v11 (C-01 through C-36; C-35/C-36 new from R10 excellence signals)
**Round:** R11 -- single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

## R10 ceiling and R11 target

R10-V-05 achieves full coverage of C-01 through C-34 under the v10 rubric (230 pts total
with v11 weighting -- 220 pts awarded, 10 pts unaddressed). Two gaps remain under v11:

**C-35 gap (per-charter iteration structure in GATE 3 field-format verification):**
R10-V-05 has a CHARTER-FORMAT-AUDIT block that iterates "for each committee charter
produced" with per-charter REJECT conditions for Quorum format and Membership TYPE.
C-35 is PASS in R10-V-05. The rubric notes C-35 as newly named criterion with a
bypass: inline FORMAT-VERIFY items in CHECKPOINT-3 that apply collectively fail C-35.
R10-V-05's dedicated loop structure satisfies C-35; V-01 inherits this as the control.

**C-36 gap (per-charter role continuity within GATE 3 charter audit):**
R10-V-05's CHARTER-FORMAT-AUDIT loop checks Quorum format and Membership TYPE per-charter
but does NOT check Membership role names against GATE 0 within the loop. The ROLE-CONTINUITY
step lives in CHECKPOINT-3 as a separate aggregate item executed AFTER all charters are
processed. C-36 requires role continuity to be integrated as a per-charter step within the
same iteration -- each charter's Membership role names cross-referenced against GATE 0 before
the loop advances to the next charter. A role name undeclared in GATE 0 but syntactically
correct (passing the TYPE check) introduced mid-sequence passes through the R10-V-05 loop
unchallenged and is only caught at the aggregate CHECKPOINT-3 level.

**R11 target:** Close the C-36 gap. V-01 establishes the control (no C-36 change).
V-02 adds per-charter role continuity inside the loop with aggregate backup in CHECKPOINT-3.
V-03 adds per-charter role continuity inside the loop with CHECKPOINT-3 referencing the loop
(no separate aggregate item). V-04 combines V-02 loop with richer inertia framing (C-01 depth).
V-05 is full integration: V-02 loop + V-04 inertia + explicit gate chain articulation.

---

## R11 Variation Map

| V | Axis | What changes vs R10-V-05 | C-35 | C-36 |
|---|------|--------------------------|------|------|
| V-01 | Phrasing register (formal/imperative) | Inherits R10-V-05 CHARTER-FORMAT-AUDIT loop unchanged; ROLE-CONTINUITY stays in CHECKPOINT-3 aggregate; formal DO/DO NOT register throughout | PASS (control) | absent |
| V-02 | Loop structure: role continuity inside loop with aggregate backup | Adds third per-charter ROLE-CONTINUITY check inside CHARTER-FORMAT-AUDIT loop; CHECKPOINT-3 ROLE-CONTINUITY item retained as aggregate reference | PASS | TARGET |
| V-03 | Loop structure: role continuity inside loop only (no aggregate) | Adds third check to loop; CHECKPOINT-3 replaces separate ROLE-CONTINUITY item with reference to completed loop result | PASS | TARGET (alt) |
| V-04 | Inertia framing emphasis + V-02 loop | Richer COST-FRAME and NET-COST-COMPARISON language in inertia sub-sections; V-02 loop for C-36 | PASS | TARGET |
| V-05 | Full integration: V-02 loop + V-04 inertia + explicit gate chain articulation | Maximum coverage: per-charter role continuity in loop, enriched inertia framing, explicit named-artifact handoffs in each gate preamble | PASS | TARGET |

**Single-axis hypothesis:**
- V-01: R10-V-05 loop satisfies C-35; ROLE-CONTINUITY in CHECKPOINT-3 satisfies C-34.
  C-36 absent. Composite: 220/230 = 95.7%.
- V-02: Adding a third per-charter check inside the loop integrates role continuity at the
  earliest detection point for each charter. The per-charter HALT + remediation directive
  binds GATE 0 correction to charter-production sequence, not post-hoc. C-36 PASS predicted.
- V-03: Removing the aggregate ROLE-CONTINUITY from CHECKPOINT-3 and replacing with a
  reference to the loop's completed result tests whether C-34 is satisfied via C-36's
  subsumption (C-36 implies C-34) or requires an independent aggregate declaration.
- V-04: Inertia framing richness does not affect GATE 3 loop structure; C-36 inherits from
  V-02. Tests whether inertia depth independently improves composite without loop interference.
- V-05: All positive signals combined. Predicted full coverage C-01 through C-36.

---

## V-01 -- Phrasing Register (Formal/Imperative); Control for C-36

**Axis:** phrasing register -- formal/imperative register throughout; extensive DO/DO NOT
lists at each gate; CHARTER-FORMAT-AUDIT loop inherited unchanged from R10-V-05.
**Hypothesis:** The formal DO/DO NOT phrasing register makes compliance conditions
independently verifiable by label. CHARTER-FORMAT-AUDIT loop satisfies C-35 (per-charter
iteration for format). ROLE-CONTINUITY item in CHECKPOINT-3 satisfies C-34 (aggregate
cross-gate lookup). C-36 is not targeted: role continuity does not enter the loop body.
Composite predicted: 220/230. Establishes the control against which V-02/V-03 are compared.

---

You are running `/org-chart {topic}`.

DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.

Formal org structure is not the answer -- it is the proposal. Informal coordination
(channels, standups, de-facto leads, shared documents) is the status quo you are
trying to displace. Do not draw an org box until you have argued the case for staying
flat and found the specific failure mode it cannot answer.

---

GATE CHAIN CONTRACT

Gates GATE 0, GATE 1, GATE 2, GATE 3. Each gate's outputs are required inputs for the
subsequent gate. MUST emit in strictly ascending numeric order. Sequence provable from
gate labels. Every gate carries a dedicated verification checkpoint before STATUS -- no
gate may emit STATUS without its own checkpoint clearing first.

---

### GATE 0 -- ROLES AND CLASSIFICATION

**Prerequisite:** none
**Produces:** typed role list

GATE 0 DO/DO NOT:
- DO: Read `.craft/roles/` before writing any content.
- DO: List every discovered role in ROLES-LOADED.
- DO NOT: Write any content outside the roles block and classification block before GATE 0 STATUS.
- DO NOT: Introduce a role name in any downstream section that does not appear in this block.

GATE 0 CONTAINMENT CONTRACT -- the following content types MUST NOT appear within GATE 0
before STATUS is emitted:
- Inertia assessment rows or sub-sections
- Org diagram nodes or ASCII hierarchy
- Headcount area entries
- Operating rhythm rows
- Committee charter fields

**Step 0.1 -- Load Roles**

Check `.craft/roles/` for existing role definitions.

```
ROLES-LOADED:
  - [role name] -- [one-line description from role file]
  - [role name] -- [one-line description from role file]
```

If no role files found:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] -- [description]
  - [role name] -- [description]
```

**Step 0.2 -- Role-Type Classification**

Immediately after the roles block -- no structural content may appear between Step 0.1
and Step 0.2. Every role listed in Step 0.1 MUST be typed from the closed set:
{DECISION, EXECUTION, ADVISORY, GOVERNANCE}. Three-tier order: DECISION first,
EXECUTION second, ADVISORY/GOVERNANCE third.

```
ROLE-TYPE-CLASSIFICATION:
  DECISION:
    - [role name]
  EXECUTION:
    - [role name]
  ADVISORY:
    - [role name]
  GOVERNANCE:
    - [role name]
```

MUST NOT proceed past this block until every role from Step 0.1 is typed.

**CHECKPOINT-0 (C-29 -- all-gate blocking)**

Before emitting GATE 0 STATUS, verify all items:
- [ ] ROLES-LOADED or ROLES-NOTE block is present and lists all roles
- [ ] ROLE-TYPE-CLASSIFICATION assigns every role a type from {DECISION, EXECUTION, ADVISORY, GOVERNANCE}
- [ ] No structural content appeared between Step 0.1 and Step 0.2
- [ ] No content from the GATE 0 CONTAINMENT CONTRACT appears above this line

All checkboxes MUST be ticked before GATE 0 STATUS can read PASS.

GATE 0 STATUS:
- [ ] Roles block present
- [ ] All roles typed from closed set
- [ ] Containment contract satisfied
- [ ] CHECKPOINT-0 cleared

```
GATE 0 STATUS: [PASS / FAIL]
```

If FAIL: DO NOT advance to GATE 1. Correct the gap above and re-verify.

**Named artifact handoff:** GATE 1 requires the typed role list produced here.
If GATE 0 STATUS is FAIL, GATE 1 MUST NOT begin.

---

### GATE 1 -- INERTIA ASSESSMENT

**Prerequisite:** typed role list from GATE 0
**Produces:** inertia verdict + FLAT-CASE-PRESSURE rating

GATE 1 DO/DO NOT:
- DO: Write the default-position statement as the first executable step (Step 1.0),
  before any mechanism rows.
- DO: Present all four sub-sections in sequence.
- DO NOT: Write an org diagram node or headcount entry before GATE 1 STATUS.
- DO NOT: Use "the team is growing" as a rebuttal without naming the failure mode.
- DO NOT: Use a FLAT-CASE-PRESSURE rating outside the closed set {LOW, MEDIUM, HIGH}.
- DO NOT: Use "revisit as the team grows" -- trigger MUST name a concrete condition.

GATE 1 PROHIBITED CONTENT -- MUST NOT appear within GATE 1 before STATUS:
- ASCII org diagram nodes or hierarchy lines
- Headcount area rows
- Operating rhythm cadence rows
- Committee charter fields (Mission, Membership, Quorum, Escalates)

**Step 1.0 -- Default-Position Statement (C-28 step embed)**

Write the following statement as the first line of GATE 1, before any mechanism rows:

> DEFAULT POSITION: The team can operate flat; structure must earn its place.

This is an executable step. It MUST be encountered during execution of GATE 1.
It MUST precede the mechanism table. It is not a preamble or scene-setter.

**Step 1.1 -- Case for Staying Flat**

Present a mechanism table with Type from the closed set {CADENCE, CHANNEL, INFORMAL-LEAD,
ARTIFACT}. Produce at least two rows before the separator.

Inline example row (complete, not a label):

| Type | Mechanism | Current Evidence |
|------|-----------|-----------------|
| CADENCE | Weekly cross-area standup | Resolves sprint-level dependencies across two areas without escalation -- no blocked decision in the last quarter |

```
### Case for Staying Flat

| Type | Mechanism | Current Evidence |
|------|-----------|-----------------|
| [CADENCE|CHANNEL|INFORMAL-LEAD|ARTIFACT] | [specific named mechanism] | [observable evidence this mechanism works] |
| [CADENCE|CHANNEL|INFORMAL-LEAD|ARTIFACT] | [second mechanism] | [evidence] |
```

Two-step separator protocol:
- Step A: Count mechanism rows written above.
- Step B: If count < 2, write missing rows first. Once count >= 2, substitute as N and emit:

```
--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. FLAT-CASE-PRESSURE: [LOW|MEDIUM|HIGH]. How We Coordinate Today begins.] ---
```

**ENFORCEMENT -- GUARD:** DO NOT EMIT the separator before row count >= 2.
DO NOT begin Step 1.2 until the separator appears in output.
Two-site: Sub-section 1.2 prose MUST be preceded by the separator -- no Sub-section 1.2
content before the separator is acceptable.

**Step 1.2 -- How We Coordinate Today**

Inventory current coordination: channels, cadences, informal roles, artifacts.
DO NOT re-list mechanism rows from Step 1.1.

**Step 1.3 -- Rebuttal**

Name the coordination failure the flat case cannot answer. Reference a specific observable.

**Step 1.4 -- VERDICT and Re-assessment Trigger**

Choose exactly one: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED. Reasoning sentence.
Concrete re-assessment trigger. DO NOT use "revisit as the team grows."

Flat-verdict branch -- if CAN-OPERATE-FLAT:
```
[ABSENT: ASCII Org Diagram] -- flat verdict. "Simplified" or "compact" alternatives are
not acceptable substitutes for this ABSENT label.
[ABSENT: Headcount by Area] -- flat verdict.
[ABSENT: Operating Rhythm Table] -- flat verdict.
[ABSENT: Committee Charters] -- flat verdict.
[ABSENT: ORG-ELEMENT REGISTER] -- flat verdict.
[ABSENT: Org Evolution Roadmap] -- flat verdict.
[ABSENT: Anti-Pattern Watch] -- flat verdict.
STOP -- ARTIFACT COMPLETE. No content follows this directive.
```

**CHECKPOINT INERTIA-CHECK (C-22 -- blocking)**

Before emitting GATE 1 STATUS, verify all checkboxes:
- [ ] Default-position statement precedes mechanism table
- [ ] Case for Staying Flat has >= 2 mechanism rows with Types from closed set
- [ ] FLAT-CASE-PRESSURE is from {LOW, MEDIUM, HIGH}
- [ ] VERDICT is from {CAN-OPERATE-FLAT, STRUCTURE-WARRANTED} with reasoning sentence
- [ ] Re-assessment trigger is concrete (not "revisit as the team grows")
- [ ] No prohibited content from GATE 1 contract appears above this line

GATE 1 STATUS:
- [ ] Default-position present before mechanism table
- [ ] All 4 sub-sections complete
- [ ] FLAT-CASE-PRESSURE from closed set
- [ ] VERDICT with reasoning and concrete trigger
- [ ] CHECKPOINT INERTIA-CHECK cleared

```
GATE 1 STATUS: [PASS / FAIL]
```

If FAIL: DO NOT advance to GATE 2.

**Named artifact handoff:** GATE 2 requires inertia verdict + FLAT-CASE-PRESSURE rating.
If GATE 1 STATUS is FAIL, GATE 2 MUST NOT begin.

---

### GATE 2 -- STRUCTURAL ARTIFACT GENERATION

**Prerequisite:** inertia verdict + FLAT-CASE-PRESSURE rating from GATE 1
**Produces:** org diagram with typed nodes

GATE 2 DO/DO NOT:
- DO: Draw ASCII hierarchy using only role names from ROLES-LOADED.
- DO: Use split Decides/Escalates columns -- separate, not merged.
- DO NOT: Introduce any role name not in GATE 0's typed role list.
- DO NOT: Use a single "Decision Scope" column.

GATE 2 PROHIBITED CONTENT -- MUST NOT appear within GATE 2 before STATUS:
- Operating rhythm cadence rows
- Committee charter fields

**Step 2.1 -- ASCII Org Diagram**

Draw ASCII hierarchy with at minimum two levels. Committees as distinct labeled nodes.
All role names MUST come from ROLES-LOADED.

**Step 2.2 -- Headcount by Area**

Five columns: Area, Headcount, Key Roles, Decides, Escalates. Key Roles annotated with
`(domain type)`. Decides and Escalates are separate columns.

Inline example row (complete, not a label):

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| Platform Engineering | 6 | Principal Engineer (DECISION) | API versioning policy, breaking-change gates | Cross-product dependency resolution --> Architecture Board |

```
| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| [name] | [N or N-M] | [role (domain type)] | [decision types owned] | [decisions escalated -- named destination] |
| [name] | [N or N-M] | [role (domain type)] | [decision types owned] | [decisions escalated -- named destination] |
| **Total** | **[N]** | | | |
```

At minimum two area rows with individual counts and a Total row.

**CHECKPOINT DIAGRAM-CHECK (C-22 -- blocking)**

Before emitting GATE 2 STATUS, verify all checkboxes:
- [ ] ASCII diagram >= 2 hierarchy levels
- [ ] All role names in diagram sourced from ROLES-LOADED
- [ ] Committees appear as distinct nodes (not embedded in area boxes)
- [ ] Headcount table has five columns (Area, Headcount, Key Roles, Decides, Escalates)
- [ ] At least two area rows and a Total row present
- [ ] No rhythm rows or charter fields appear above this line

GATE 2 STATUS:
- [ ] ASCII diagram present with >= 2 hierarchy levels
- [ ] Committees as distinct nodes
- [ ] Headcount has split Decides/Escalates columns
- [ ] >= 2 area rows + Total row
- [ ] CHECKPOINT DIAGRAM-CHECK cleared

```
GATE 2 STATUS: [PASS / FAIL]
```

If FAIL: DO NOT advance to GATE 3.

**Named artifact handoff:** GATE 3 requires org diagram with typed nodes.
If GATE 2 STATUS is FAIL, GATE 3 MUST NOT begin.

---

### GATE 3 -- GOVERNANCE DOCUMENTATION

**Prerequisite:** org diagram with typed nodes from GATE 2; typed role list from GATE 0
**Produces:** complete governance artifact

GATE 3 DO/DO NOT:
- DO: Produce operating rhythm rows and committee charters in interleaved pairs -- each
  governance row immediately followed by its charter.
- DO: Verify pair count equals governance row count after all pairs are written.
- DO NOT: Batch all rhythm rows first and all charters second.
- DO NOT: Reference a role not in ROLES-LOADED in a charter Membership field.
- DO NOT: Write a Quorum field without `N of M member roles` fraction form.
- DO NOT: Write Membership without `(TYPE)` annotation on each role.

GATE 3 PROHIBITED CONTENT (C-30 -- terminal gate contract) -- MUST NOT appear within
GATE 3 before STATUS is emitted:
- Appendices of any kind
- Supplementary sections (additional tables, notes, annexes)
- Editorial commentary or rationale paragraphs after the Anti-Pattern Watch table
- Additional committee charters not paired with an operating rhythm row
- Any content category not explicitly part of Steps 3.1 through 3.5

Terminal-gate position does not exempt GATE 3 from this contract. The intra-gate content
risk at GATE 3 is content appended after the Anti-Pattern Watch table and before STATUS.

**Step 3.1 -- Operating Rhythm and Charters (Interleaved)**

Operating rhythm: >= 3 distinct cadences (ROB, shiproom/gate, governance). No merged rows.

Inline example row for operating rhythm (complete, not a label):

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|
| Architecture Board | Monthly | Principal Engineer | Review and approve cross-cutting design decisions affecting two or more service areas |

**Charter format -- 5 fields required (complete example)**

Complete filled example (model this format; fill concrete values for your topic):

```
### Architecture Review Board

**Mission:** Evaluate and approve cross-cutting architectural decisions before
implementation begins, ensuring consistency across all service areas.
**Membership:** Principal Engineer (DECISION), Engineering Manager (GOVERNANCE),
Staff Engineer (ADVISORY)
**Quorum:** 2 of 3 member roles
**Escalates:** VP Engineering
```

Charter template for each governance committee in this artifact:

```
### [Committee Name]

**Mission:** [one sentence -- what this committee decides or governs]
**Membership:** [Role A (TYPE)], [Role B (TYPE)]
**Quorum:** [N] of [M] member roles
**Escalates:** [named destination role or forum]
```

REQUIRED:
- Membership MUST list >= 2 roles each annotated with `(TYPE)` from
  {DECISION, EXECUTION, ADVISORY, GOVERNANCE}.
- Quorum MUST use `N of M member roles` fraction form. Percentage, prose quorum
  ("majority"), or missing Quorum field is not acceptable.

For each governance cadence row, immediately produce its charter. DO NOT batch.

**Step 3.2 -- Post-Interleave Pair-Count Verification (C-19)**

After all rhythm-charter pairs are produced:
- Count governance rows in the Operating Rhythm Table: [N]
- Count committee charters produced: [N]
- MUST match. If mismatch: identify the gap, produce missing charter, recount.
  DO NOT advance to Step 3.3 until counts match.

**Step 3.3 -- ORG-ELEMENT REGISTER**

MUST produce immediately after Committee Charters. All four categories MUST be
populated before advancing to Step 3.4.

```
ORG-ELEMENT REGISTER

  Category schema:
  | cat-N | Category name         | Element type                                          |
  |-------|-----------------------|-------------------------------------------------------|
  | cat-1 | Areas                 | Area names from the Headcount by Area table           |
  | cat-2 | Committees/Cadences   | Committee and cadence names from Rhythm Table/Charters|
  | cat-3 | Headcount             | Total headcount and per-area headcount counts         |
  | cat-4 | DRI Roles             | DRI role names from the Operating Rhythm Table        |

  cat-1 (Areas):
    - [area name] -- headcount: [N]

  cat-2 (Committees/Cadences):
    - [committee or cadence name]

  cat-3 (Headcount):
    - Total headcount: [N]

  cat-4 (DRI Roles):
    - [DRI role name]
```

**Step 3.4 -- Org Evolution Roadmap**

At minimum two rows, distinct trigger categories. Row 1 MUST be a headcount threshold.
Row 2 MUST be from a different category (workload signal, structural symptom, or milestone).

Inline example row (complete, not a label):

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| Headcount exceeds 15 engineers | Split Platform area into Core and Extensions sub-areas; add Area Lead role | headcount-threshold |

**Step 3.5 -- Anti-Pattern Watch**

At minimum two rows. Each "Why It Applies Here" cell MUST open with:
`[element name] (cat-N) -- [one sentence]`

Element names copied exactly from ORG-ELEMENT REGISTER.
DO NOT use a cat-N code not in the register schema.

**CHARTER-FORMAT-AUDIT (C-33/C-35 -- per-charter field-level compliance, dedicated loop)**

DO NOT advance to CHECKPOINT-3 until this audit loop has been completed for every
charter produced in Step 3.1.

For each committee charter produced, in sequence, complete this field audit before
advancing to the next charter:

```
Charter: [Committee Name]
[ ] Quorum field: value is in the form `[integer] of [integer] member roles`
    REJECT: fractional notation ("3/5"), percentage ("60%"), prose quorum ("majority of
    members", "quorum required"), bare number without "member roles" suffix ("3"), absent field
[ ] Membership entries: each listed role carries exactly one `(TYPE)` annotation where
    TYPE is a value from the closed set {DECISION, EXECUTION, ADVISORY, GOVERNANCE}
    REJECT: role listed without parenthetical; parenthetical value outside the closed set
    (e.g., "(OWNER)", "(LEAD)", "(APPROVER)"); multiple TYPE values on a single entry
```

If any charter fails any check: STOP. Correct the failing charter. Re-run the full
CHARTER-FORMAT-AUDIT loop from the first charter before advancing to CHECKPOINT-3.

**CHECKPOINT-3 (C-29/C-33/C-34 -- all-gate blocking + format audit + role continuity)**

Before emitting GATE 3 STATUS, verify all checkboxes:
- [ ] Operating Rhythm Table has >= 3 distinct rows (ROB, shiproom/gate, governance)
- [ ] Pair count verified: governance rows in ORT == charter count produced
- [ ] Each charter has all 5 fields: Name (header), Mission, Membership, Quorum, Escalates
- [ ] CHARTER-FORMAT-AUDIT completed -- all charters passed Quorum fraction-pattern check
  and Membership closed-set TYPE check (see CHARTER-FORMAT-AUDIT block above)
- [ ] ROLE-CONTINUITY: For each role name appearing in any charter Membership field --
  verify the role name is present in the GATE 0 ROLES-LOADED or ROLES-NOTE list.
  If any Membership role name is absent from GATE 0: CHECKPOINT-3 STATUS FAILS.
  Remediation directive: add the undeclared role to GATE 0 ROLES-LOADED and re-emit
  GATE 0 STATUS before GATE 3 STATUS can emit.
- [ ] ORG-ELEMENT REGISTER has all four categories (cat-1 through cat-4) populated
- [ ] Org Evolution Roadmap has >= 2 rows with distinct trigger categories
- [ ] Anti-Pattern Watch has >= 2 rows with typed citations from register
- [ ] No prohibited content from GATE 3 contract appears above this line

All checkboxes MUST be ticked before GATE 3 STATUS can read PASS.

GATE 3 STATUS:
- [ ] Operating rhythm >= 3 distinct rows
- [ ] Charters complete (5 fields; CHARTER-FORMAT-AUDIT passed)
- [ ] Pair count verified
- [ ] ROLE-CONTINUITY passed -- all Membership names present in GATE 0
- [ ] ORG-ELEMENT REGISTER populated (cat-1 through cat-4)
- [ ] Org Evolution Roadmap >= 2 rows with distinct trigger categories
- [ ] Anti-Pattern Watch with typed citations from register
- [ ] GATE 3 prohibited-content contract satisfied
- [ ] CHECKPOINT-3 cleared

```
GATE 3 STATUS: [PASS / FAIL]
```

STOP -- ARTIFACT COMPLETE. No additional content, sections, appendices, or commentary
follows this line. (C-31 -- successful-completion path terminal seal)

---

## V-02 -- Loop Structure: Per-Charter Role Continuity Inside Loop + Aggregate Backup (C-36 target)

**Axis:** loop structure -- integrate Membership role-continuity check as a third per-charter
step inside the CHARTER-FORMAT-AUDIT loop; CHECKPOINT-3 ROLE-CONTINUITY item retained as
aggregate backup reference.
**Hypothesis:** R10-V-05's CHARTER-FORMAT-AUDIT loop visits each charter for Quorum format
and Membership TYPE but does not check Membership role names against GATE 0 within the loop
body. A role name undeclared in GATE 0 but syntactically correct (TYPE annotation present and
from closed set) passes through the loop and is only caught at the post-loop CHECKPOINT-3
ROLE-CONTINUITY item. C-36 requires per-charter role lookup within the iteration before the
loop advances. Adding a third check item to the loop -- verifying each Membership role name
against GATE 0 and emitting per-charter HALT + remediation if absent -- satisfies C-36.
CHECKPOINT-3 retains the ROLE-CONTINUITY item as an aggregate backup; C-34 is satisfied
both by the loop (per-charter) and by the checkpoint item (aggregate). C-36 PASS predicted.
All prior criteria preserved. Composite predicted: 230/230.

---

You are running `/org-chart {topic}`.

DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.

Formal org structure is not the answer -- it is the proposal. Informal coordination
(channels, standups, de-facto leads, shared documents) is the status quo you are
trying to displace. Do not draw an org box until you have argued the case for staying
flat and found the specific failure mode it cannot answer.

---

GATE CHAIN CONTRACT

Gates GATE 0, GATE 1, GATE 2, GATE 3. Each gate's outputs are required inputs for the
subsequent gate. MUST emit in strictly ascending numeric order. Sequence provable from
gate labels. Every gate carries a dedicated verification checkpoint before STATUS -- no
gate may emit STATUS without its own checkpoint clearing first.

---

### GATE 0 -- ROLES AND CLASSIFICATION

**Prerequisite:** none
**Produces:** typed role list

GATE 0 DO/DO NOT:
- DO: Read `.craft/roles/` before writing any content.
- DO: List every discovered role in ROLES-LOADED.
- DO NOT: Write any content outside the roles block and classification block before GATE 0 STATUS.
- DO NOT: Introduce a role name in any downstream section that does not appear in this block.

GATE 0 CONTAINMENT CONTRACT -- the following content types MUST NOT appear within GATE 0
before STATUS is emitted:
- Inertia assessment rows or sub-sections
- Org diagram nodes or ASCII hierarchy
- Headcount area entries
- Operating rhythm rows
- Committee charter fields

**Step 0.1 -- Load Roles**

Check `.craft/roles/` for existing role definitions.

```
ROLES-LOADED:
  - [role name] -- [one-line description from role file]
  - [role name] -- [one-line description from role file]
```

If no role files found:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] -- [description]
  - [role name] -- [description]
```

**Step 0.2 -- Role-Type Classification**

Immediately after the roles block -- no structural content may appear between Step 0.1
and Step 0.2. Every role listed in Step 0.1 MUST be typed from the closed set:
{DECISION, EXECUTION, ADVISORY, GOVERNANCE}. Three-tier order: DECISION first,
EXECUTION second, ADVISORY/GOVERNANCE third.

```
ROLE-TYPE-CLASSIFICATION:
  DECISION:
    - [role name]
  EXECUTION:
    - [role name]
  ADVISORY:
    - [role name]
  GOVERNANCE:
    - [role name]
```

MUST NOT proceed past this block until every role from Step 0.1 is typed.

**CHECKPOINT-0 (C-29 -- all-gate blocking)**

Before emitting GATE 0 STATUS, verify all items:
- [ ] ROLES-LOADED or ROLES-NOTE block is present and lists all roles
- [ ] ROLE-TYPE-CLASSIFICATION assigns every role a type from {DECISION, EXECUTION, ADVISORY, GOVERNANCE}
- [ ] No structural content appeared between Step 0.1 and Step 0.2
- [ ] No content from the GATE 0 CONTAINMENT CONTRACT appears above this line

All checkboxes MUST be ticked before GATE 0 STATUS can read PASS.

GATE 0 STATUS:
- [ ] Roles block present
- [ ] All roles typed from closed set
- [ ] Containment contract satisfied
- [ ] CHECKPOINT-0 cleared

```
GATE 0 STATUS: [PASS / FAIL]
```

If FAIL: DO NOT advance to GATE 1. Correct the gap above and re-verify.

**Named artifact handoff:** GATE 1 requires the typed role list produced here.
If GATE 0 STATUS is FAIL, GATE 1 MUST NOT begin.

---

### GATE 1 -- INERTIA ASSESSMENT

**Prerequisite:** typed role list from GATE 0
**Produces:** inertia verdict + FLAT-CASE-PRESSURE rating

GATE 1 DO/DO NOT:
- DO: Write the default-position statement as the first executable step (Step 1.0),
  before any mechanism rows.
- DO: Present all four sub-sections in sequence.
- DO NOT: Write an org diagram node or headcount entry before GATE 1 STATUS.
- DO NOT: Use "the team is growing" as a rebuttal without naming the failure mode.
- DO NOT: Use a FLAT-CASE-PRESSURE rating outside the closed set {LOW, MEDIUM, HIGH}.
- DO NOT: Use "revisit as the team grows" -- trigger MUST name a concrete condition.

GATE 1 PROHIBITED CONTENT -- MUST NOT appear within GATE 1 before STATUS:
- ASCII org diagram nodes or hierarchy lines
- Headcount area rows
- Operating rhythm cadence rows
- Committee charter fields (Mission, Membership, Quorum, Escalates)

**Step 1.0 -- Default-Position Statement (C-28 step embed)**

Write the following statement as the first line of GATE 1, before any mechanism rows:

> DEFAULT POSITION: The team can operate flat; structure must earn its place.

This is an executable step. It MUST be encountered during execution of GATE 1.
It MUST precede the mechanism table. It is not a preamble or scene-setter.

**Step 1.1 -- Case for Staying Flat**

Present a mechanism table with Type from the closed set {CADENCE, CHANNEL, INFORMAL-LEAD,
ARTIFACT}. Produce at least two rows before the separator.

Inline example row (complete, not a label):

| Type | Mechanism | Current Evidence |
|------|-----------|-----------------|
| CADENCE | Weekly cross-area standup | Resolves sprint-level dependencies across two areas without escalation -- no blocked decision in the last quarter |

Two-step separator protocol:
- Step A: Count mechanism rows written above.
- Step B: If count < 2, write missing rows first. Once count >= 2, substitute as N and emit:

```
--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. FLAT-CASE-PRESSURE: [LOW|MEDIUM|HIGH]. How We Coordinate Today begins.] ---
```

**ENFORCEMENT -- GUARD:** DO NOT EMIT the separator before row count >= 2.
DO NOT begin Step 1.2 until the separator appears in output.
Two-site: Sub-section 1.2 prose MUST be preceded by the separator.

**Step 1.2 -- How We Coordinate Today**

Inventory current coordination: channels, cadences, informal roles, artifacts.
DO NOT re-list mechanism rows from Step 1.1.

**Step 1.3 -- Rebuttal**

Name the coordination failure the flat case cannot answer. Reference a specific observable.

**Step 1.4 -- VERDICT and Re-assessment Trigger**

Choose exactly one: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED. Reasoning sentence.
Concrete re-assessment trigger. DO NOT use "revisit as the team grows."

Flat-verdict branch -- if CAN-OPERATE-FLAT:
```
[ABSENT: ASCII Org Diagram] -- flat verdict.
[ABSENT: Headcount by Area] -- flat verdict.
[ABSENT: Operating Rhythm Table] -- flat verdict.
[ABSENT: Committee Charters] -- flat verdict.
[ABSENT: ORG-ELEMENT REGISTER] -- flat verdict.
[ABSENT: Org Evolution Roadmap] -- flat verdict.
[ABSENT: Anti-Pattern Watch] -- flat verdict.
STOP -- ARTIFACT COMPLETE. No content follows this directive.
```

**CHECKPOINT INERTIA-CHECK (C-22 -- blocking)**

Before emitting GATE 1 STATUS, verify all checkboxes:
- [ ] Default-position statement precedes mechanism table
- [ ] Case for Staying Flat has >= 2 mechanism rows with Types from closed set
- [ ] FLAT-CASE-PRESSURE is from {LOW, MEDIUM, HIGH}
- [ ] VERDICT is from {CAN-OPERATE-FLAT, STRUCTURE-WARRANTED} with reasoning sentence
- [ ] Re-assessment trigger is concrete
- [ ] No prohibited content from GATE 1 contract appears above this line

```
GATE 1 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 2 requires inertia verdict + FLAT-CASE-PRESSURE rating.
If GATE 1 STATUS is FAIL, GATE 2 MUST NOT begin.

---

### GATE 2 -- STRUCTURAL ARTIFACT GENERATION

**Prerequisite:** inertia verdict + FLAT-CASE-PRESSURE rating from GATE 1
**Produces:** org diagram with typed nodes

GATE 2 DO/DO NOT:
- DO: Draw ASCII hierarchy using only role names from ROLES-LOADED.
- DO: Use split Decides/Escalates columns -- separate, not merged.
- DO NOT: Introduce any role name not in GATE 0's typed role list.
- DO NOT: Use a single "Decision Scope" column.

GATE 2 PROHIBITED CONTENT: Operating rhythm cadence rows; committee charter fields.

**Step 2.1 -- ASCII Org Diagram**

Draw ASCII hierarchy with at minimum two levels. Committees as distinct labeled nodes.
All role names MUST come from ROLES-LOADED.

**Step 2.2 -- Headcount by Area**

Five columns: Area, Headcount, Key Roles (with `(domain type)`), Decides, Escalates.
Minimum two area rows + Total row.

Inline example row:

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| Platform Engineering | 6 | Principal Engineer (DECISION) | API versioning policy, breaking-change gates | Cross-product dependency resolution --> Architecture Board |

**CHECKPOINT DIAGRAM-CHECK (C-22 -- blocking)**

- [ ] Diagram >= 2 levels, roles from ROLES-LOADED, committees distinct
- [ ] 5-column headcount, Decides/Escalates split, >= 2 areas + Total
- [ ] No rhythm rows or charter fields above this line

```
GATE 2 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 3 requires org diagram with typed nodes.
If GATE 2 STATUS is FAIL, GATE 3 MUST NOT begin.

---

### GATE 3 -- GOVERNANCE DOCUMENTATION

**Prerequisite:** org diagram with typed nodes from GATE 2; typed role list from GATE 0
**Produces:** complete governance artifact

GATE 3 DO/DO NOT:
- DO: Interleave rhythm rows and charters -- each governance row immediately followed by its charter.
- DO: Verify pair count after all pairs written.
- DO NOT: Batch rhythm first, charters second.
- DO NOT: Reference a role not in ROLES-LOADED in charter Membership.
- DO NOT: Quorum without `N of M member roles` fraction form.
- DO NOT: Membership without `(TYPE)` annotation on each role.

GATE 3 PROHIBITED CONTENT (C-30): Appendices, supplementary sections, editorial commentary
after Anti-Pattern Watch, unpaired charters, content outside Steps 3.1--3.5.
Terminal-gate position does not exempt GATE 3 from this contract.

**Step 3.1 -- Operating Rhythm and Charters (Interleaved)**

>= 3 distinct cadences (ROB, shiproom/gate, governance). No merged rows.

Complete filled charter example:

```
### Architecture Review Board

**Mission:** Evaluate and approve cross-cutting architectural decisions before
implementation begins, ensuring consistency across all service areas.
**Membership:** Principal Engineer (DECISION), Engineering Manager (GOVERNANCE),
Staff Engineer (ADVISORY)
**Quorum:** 2 of 3 member roles
**Escalates:** VP Engineering
```

REQUIRED: Membership >= 2 roles with `(TYPE)` from {DECISION, EXECUTION, ADVISORY, GOVERNANCE}.
Quorum MUST use `N of M member roles`. Percentage, prose quorum, absence: not acceptable.
For each governance cadence row, immediately produce its charter. DO NOT batch.

**Step 3.2 -- Pair-Count Verification** (ORT rows == charter count; DO NOT advance until match)

**Step 3.3 -- ORG-ELEMENT REGISTER** (all four categories cat-1 through cat-4 populated)

**Step 3.4 -- Org Evolution Roadmap** (>= 2 rows, distinct triggers; Row 1: headcount threshold)

**Step 3.5 -- Anti-Pattern Watch** (>= 2 rows, `[element name] (cat-N) -- [one sentence]`)

**CHARTER-FORMAT-AUDIT (C-33/C-35/C-36 -- per-charter field-level compliance and role continuity)**

DO NOT advance to CHECKPOINT-3 until this audit loop has been completed for every
charter produced in Step 3.1.

For each committee charter produced, in sequence, complete this three-check field audit
before advancing to the next charter. Each check is evaluated at this charter before the
loop may proceed:

```
Charter: [Committee Name]
[ ] Quorum field: value is in the form `[integer] of [integer] member roles`
    REJECT: fractional notation ("3/5"), percentage ("60%"), prose quorum ("majority of
    members", "quorum required"), bare number without "member roles" suffix ("3"), absent field
[ ] Membership entries: each listed role carries exactly one `(TYPE)` annotation where
    TYPE is a value from the closed set {DECISION, EXECUTION, ADVISORY, GOVERNANCE}
    REJECT: role listed without parenthetical; parenthetical value outside the closed set
    (e.g., "(OWNER)", "(LEAD)", "(APPROVER)"); multiple TYPE values on a single entry
[ ] Membership role continuity: for each role name in this charter's Membership field,
    verify the name is present in the GATE 0 ROLES-LOADED or ROLES-NOTE typed role list
    REJECT: role name [X] not found in GATE 0 typed role list -- halt loop at this charter;
    remediation: add [X] to GATE 0 ROLES-LOADED and re-emit GATE 0 STATUS before this
    loop may continue; DO NOT advance to the next charter until this charter passes
```

If any charter fails any check: STOP. Correct the failure at this charter. Re-run the full
CHARTER-FORMAT-AUDIT loop from the first charter before advancing to CHECKPOINT-3.

**CHECKPOINT-3 (C-29/C-33/C-34 -- all-gate blocking + format audit + role continuity backup)**

Before emitting GATE 3 STATUS, verify all checkboxes:
- [ ] Operating Rhythm Table has >= 3 distinct rows (ROB, shiproom/gate, governance)
- [ ] Pair count verified: governance rows in ORT == charter count produced
- [ ] Each charter has all 5 fields: Name (header), Mission, Membership, Quorum, Escalates
- [ ] CHARTER-FORMAT-AUDIT completed -- all charters passed all three checks: Quorum
  fraction-pattern, Membership closed-set TYPE, and per-charter Membership role-continuity
  against GATE 0 typed role list (see CHARTER-FORMAT-AUDIT block above)
- [ ] ROLE-CONTINUITY (aggregate backup): For each role name appearing in any charter
  Membership field -- verify the role name is present in the GATE 0 ROLES-LOADED or
  ROLES-NOTE list. If any name is absent: CHECKPOINT-3 STATUS FAILS. Remediation:
  add the undeclared role to GATE 0 and re-emit GATE 0 STATUS.
- [ ] ORG-ELEMENT REGISTER has all four categories (cat-1 through cat-4) populated
- [ ] Org Evolution Roadmap has >= 2 rows with distinct trigger categories
- [ ] Anti-Pattern Watch has >= 2 rows with typed citations from register
- [ ] No prohibited content from GATE 3 contract appears above this line

All checkboxes MUST be ticked before GATE 3 STATUS can read PASS.

GATE 3 STATUS:
- [ ] Operating rhythm >= 3 distinct rows
- [ ] Charters complete (5 fields; CHARTER-FORMAT-AUDIT all three checks passed)
- [ ] Pair count verified
- [ ] ROLE-CONTINUITY (per-charter in loop + aggregate in checkpoint) passed
- [ ] ORG-ELEMENT REGISTER populated (cat-1 through cat-4)
- [ ] Org Evolution Roadmap >= 2 rows with distinct trigger categories
- [ ] Anti-Pattern Watch with typed citations from register
- [ ] GATE 3 prohibited-content contract satisfied
- [ ] CHECKPOINT-3 cleared

```
GATE 3 STATUS: [PASS / FAIL]
```

STOP -- ARTIFACT COMPLETE. No additional content, sections, appendices, or commentary
follows this line.

---

## V-03 -- Loop Structure: Per-Charter Role Continuity Inside Loop Only (C-36 alt; C-34 via subsumption)

**Axis:** loop structure -- integrate Membership role-continuity check inside the
CHARTER-FORMAT-AUDIT loop per-charter; replace the separate aggregate ROLE-CONTINUITY
item in CHECKPOINT-3 with a reference to the completed loop result.
**Hypothesis:** V-02 retains the aggregate ROLE-CONTINUITY in CHECKPOINT-3 as backup.
V-03 tests whether C-34 is satisfied through C-36's subsumption (a variation satisfying
C-36 necessarily satisfies C-34) without an independent aggregate declaration in
CHECKPOINT-3. CHECKPOINT-3 references the completed CHARTER-FORMAT-AUDIT loop rather
than repeating the lookup. If C-34 requires an independent CHECKPOINT-3 item regardless
of C-36, V-03 would score C-36 PASS but C-34 FAIL -- revealing whether the subsumption
claim in the rubric hierarchy is sufficient or whether independent aggregate declaration
is still required. This variation is the rubric-probing control for C-34 subsumption.
C-36 PASS predicted in both V-02 and V-03; the distinguishing signal is C-34 behavior.

---

You are running `/org-chart {topic}`.

DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.

Formal org structure is not the answer -- it is the proposal. Informal coordination
(channels, standups, de-facto leads, shared documents) is the status quo you are
trying to displace. Do not draw an org box until you have argued the case for staying
flat and found the specific failure mode it cannot answer.

---

GATE CHAIN CONTRACT

Gates GATE 0, GATE 1, GATE 2, GATE 3. Each gate's outputs are required inputs for the
subsequent gate. MUST emit in strictly ascending numeric order. Every gate carries a
dedicated verification checkpoint before STATUS.

---

### GATE 0 -- ROLES AND CLASSIFICATION

**Prerequisite:** none
**Produces:** typed role list

GATE 0 DO/DO NOT:
- DO: Read `.craft/roles/` before writing any content.
- DO: List every discovered role in ROLES-LOADED.
- DO NOT: Write any content outside roles and classification blocks before GATE 0 STATUS.
- DO NOT: Introduce a role name downstream not declared here.

GATE 0 CONTAINMENT CONTRACT -- MUST NOT appear within GATE 0 before STATUS:
- Inertia assessment rows or sub-sections
- Org diagram nodes or ASCII hierarchy
- Headcount area entries
- Operating rhythm rows
- Committee charter fields

**Step 0.1 -- Load Roles**

```
ROLES-LOADED:
  - [role name] -- [one-line description from role file]
  - [role name] -- [one-line description from role file]
```

If no role files found:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] -- [description]
```

**Step 0.2 -- Role-Type Classification**

Immediately after roles block. Every role MUST be typed from {DECISION, EXECUTION,
ADVISORY, GOVERNANCE}. Three-tier order.

```
ROLE-TYPE-CLASSIFICATION:
  DECISION:
    - [role name]
  EXECUTION:
    - [role name]
  ADVISORY:
    - [role name]
  GOVERNANCE:
    - [role name]
```

**CHECKPOINT-0 (C-29)**

- [ ] ROLES-LOADED or ROLES-NOTE present and lists all roles
- [ ] Every role typed from {DECISION, EXECUTION, ADVISORY, GOVERNANCE}
- [ ] No structural content between Step 0.1 and Step 0.2
- [ ] No GATE 0 CONTAINMENT CONTRACT content above this line

```
GATE 0 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 1 requires typed role list. GATE 1 MUST NOT begin if FAIL.

---

### GATE 1 -- INERTIA ASSESSMENT

**Prerequisite:** typed role list from GATE 0
**Produces:** inertia verdict + FLAT-CASE-PRESSURE rating

GATE 1 DO/DO NOT:
- DO: Default-position statement as Step 1.0 before mechanism rows.
- DO: Four sub-sections in sequence.
- DO NOT: Org diagram or headcount before GATE 1 STATUS.
- DO NOT: FLAT-CASE-PRESSURE outside {LOW, MEDIUM, HIGH}.
- DO NOT: "Revisit as the team grows."

GATE 1 PROHIBITED CONTENT: ASCII org nodes, headcount rows, rhythm rows, charter fields.

**Step 1.0 -- Default-Position Statement (C-28)**

> DEFAULT POSITION: The team can operate flat; structure must earn its place.

MUST precede mechanism table. Executable step, not a preamble.

**Step 1.1 -- Case for Staying Flat** (mechanism table >= 2 rows, Types from {CADENCE, CHANNEL, INFORMAL-LEAD, ARTIFACT})

Two-step separator: count rows, verify >= 2, emit:
```
--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. FLAT-CASE-PRESSURE: [LOW|MEDIUM|HIGH]. How We Coordinate Today begins.] ---
```
ENFORCEMENT GUARD: DO NOT EMIT separator before row count >= 2. Two-site enforcement.

**Steps 1.2--1.4:** How We Coordinate Today / Rebuttal / VERDICT + concrete trigger.

Flat-verdict branch:
```
[ABSENT: ASCII Org Diagram] -- flat verdict.
[ABSENT: Headcount by Area] -- flat verdict.
[ABSENT: Operating Rhythm Table] -- flat verdict.
[ABSENT: Committee Charters] -- flat verdict.
[ABSENT: ORG-ELEMENT REGISTER] -- flat verdict.
[ABSENT: Org Evolution Roadmap] -- flat verdict.
[ABSENT: Anti-Pattern Watch] -- flat verdict.
STOP -- ARTIFACT COMPLETE.
```

**CHECKPOINT INERTIA-CHECK (C-22)**

- [ ] Default-position statement precedes mechanism table
- [ ] >= 2 mechanism rows with Types from closed set
- [ ] FLAT-CASE-PRESSURE from {LOW, MEDIUM, HIGH}
- [ ] VERDICT with reasoning and concrete trigger
- [ ] No prohibited content above this line

```
GATE 1 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 2 requires inertia verdict + FLAT-CASE-PRESSURE.
GATE 2 MUST NOT begin if GATE 1 STATUS is FAIL.

---

### GATE 2 -- STRUCTURAL ARTIFACT GENERATION

**Prerequisite:** inertia verdict + FLAT-CASE-PRESSURE from GATE 1
**Produces:** org diagram with typed nodes

GATE 2 DO/DO NOT: ASCII hierarchy from ROLES-LOADED only. Split Decides/Escalates.
GATE 2 PROHIBITED CONTENT: rhythm rows, charter fields.

**Step 2.1 -- ASCII Org Diagram** (>= 2 levels, committees as distinct nodes)
**Step 2.2 -- Headcount by Area** (5 columns, Key Roles with `(domain type)`, >= 2 areas + Total)

**CHECKPOINT DIAGRAM-CHECK**

- [ ] Diagram >= 2 levels, roles from ROLES-LOADED, committees distinct
- [ ] 5-column headcount, Decides/Escalates split, >= 2 areas + Total
- [ ] No rhythm rows or charter fields above this line

```
GATE 2 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 3 requires org diagram with typed nodes.
GATE 3 MUST NOT begin if GATE 2 STATUS is FAIL.

---

### GATE 3 -- GOVERNANCE DOCUMENTATION

**Prerequisite:** org diagram with typed nodes from GATE 2; typed role list from GATE 0
**Produces:** complete governance artifact

GATE 3 DO/DO NOT:
- DO: Interleave rhythm rows and charters.
- DO: Verify pair count after all pairs written.
- DO NOT: Batch rhythm first, charters second.
- DO NOT: Role not in ROLES-LOADED in charter Membership.
- DO NOT: Quorum without `N of M member roles` form.
- DO NOT: Membership without `(TYPE)` annotation on each role.

GATE 3 PROHIBITED CONTENT (C-30): Appendices, supplementary sections, editorial
commentary after Anti-Pattern Watch, unpaired charters, content outside Steps 3.1--3.5.

**Step 3.1 -- Operating Rhythm and Charters (Interleaved)**

>= 3 distinct cadences. No merged rows.
REQUIRED: Membership >= 2 roles with `(TYPE)` from {DECISION, EXECUTION, ADVISORY, GOVERNANCE}.
Quorum MUST use `N of M member roles`. For each governance row, immediately produce its charter.

**Step 3.2 -- Pair-Count Verification** (ORT rows == charter count; DO NOT advance until match)
**Step 3.3 -- ORG-ELEMENT REGISTER** (all four categories populated before Step 3.4)
**Step 3.4 -- Org Evolution Roadmap** (>= 2 rows, distinct triggers; Row 1: headcount threshold)
**Step 3.5 -- Anti-Pattern Watch** (>= 2 rows, `[element name] (cat-N) -- [one sentence]`)

**CHARTER-FORMAT-AUDIT (C-33/C-35/C-36 -- per-charter loop: format + role continuity)**

DO NOT advance to CHECKPOINT-3 until this audit loop has been completed for every
charter produced in Step 3.1.

For each committee charter produced, in sequence, apply all three checks to this charter
before the loop may advance to the next:

```
Charter: [Committee Name]
[ ] Quorum field: value is in the form `[integer] of [integer] member roles`
    REJECT: fractional notation ("3/5"), percentage ("60%"), prose quorum ("majority of
    members"), bare number without "member roles" suffix, absent field
[ ] Membership entries: each listed role carries exactly one `(TYPE)` annotation where
    TYPE is a value from the closed set {DECISION, EXECUTION, ADVISORY, GOVERNANCE}
    REJECT: unannotated role; TYPE value outside the closed set; multiple TYPE values
[ ] Membership role continuity: for each role name listed in this charter's Membership
    field, verify the name is present in the GATE 0 ROLES-LOADED or ROLES-NOTE typed
    role list
    REJECT: role name [X] absent from GATE 0 typed role list -- HALT loop at this
    charter; do not advance to the next charter; remediation: add [X] to GATE 0
    ROLES-LOADED and re-emit GATE 0 STATUS; then restart CHARTER-FORMAT-AUDIT from
    the first charter
```

LOOP HALT CONDITION: If any check emits REJECT for any charter, the loop halts at that
charter. Correct the specific failure. Re-run the complete loop from the first charter
before proceeding to CHECKPOINT-3.

**CHECKPOINT-3 (C-29 -- all-gate blocking; C-33/C-35/C-36 enforced via completed loop)**

Before emitting GATE 3 STATUS, verify all checkboxes:
- [ ] Operating Rhythm Table has >= 3 distinct rows (ROB, shiproom/gate, governance)
- [ ] Pair count verified: governance rows in ORT == charter count produced
- [ ] Each charter has all 5 fields: Name (header), Mission, Membership, Quorum, Escalates
- [ ] CHARTER-FORMAT-AUDIT loop completed without REJECT -- all charters individually
  passed Quorum fraction-pattern check, Membership closed-set TYPE check, and per-charter
  Membership role-continuity check against the GATE 0 typed role list (see loop above;
  role-continuity was enforced per-charter within the loop before each advance)
- [ ] ORG-ELEMENT REGISTER has all four categories (cat-1 through cat-4) populated
- [ ] Org Evolution Roadmap has >= 2 rows with distinct trigger categories
- [ ] Anti-Pattern Watch has >= 2 rows with typed citations from register
- [ ] No prohibited content from GATE 3 contract appears above this line

All checkboxes MUST be ticked before GATE 3 STATUS can read PASS.

GATE 3 STATUS:
- [ ] Operating rhythm >= 3 distinct rows
- [ ] Charters complete (5 fields; CHARTER-FORMAT-AUDIT loop passed all three checks per-charter)
- [ ] Pair count verified
- [ ] ORG-ELEMENT REGISTER populated
- [ ] Org Evolution Roadmap >= 2 distinct triggers
- [ ] Anti-Pattern Watch with typed citations
- [ ] GATE 3 prohibited-content contract satisfied
- [ ] CHECKPOINT-3 cleared

```
GATE 3 STATUS: [PASS / FAIL]
```

STOP -- ARTIFACT COMPLETE. No additional content, sections, appendices, or commentary
follows this line.

---

## V-04 -- Inertia Framing Emphasis + V-02 Loop (C-01 depth + C-36)

**Axis:** inertia framing emphasis -- enrich GATE 1 with COST-FRAME, NET-COST-COMPARISON,
and explicit FLAT-CASE-CLOSED semantics; V-02 loop structure (per-charter role continuity
inside CHARTER-FORMAT-AUDIT loop) applied unchanged.
**Hypothesis:** The inertia framing enrichments target aspirational criteria in the C-09
through C-32 range that depend on Sub-section 4 anchor ordering, cost-frame completeness,
and net-cost comparison block presence. These enrichments are structurally independent
of the GATE 3 loop changes from V-02. C-36 inherits the V-02 per-charter role continuity
loop; inertia richness does not interact with the loop. Combined effect: V-04 should
achieve the same C-36 PASS as V-02 while improving depth scores on aspirational inertia
criteria. This tests whether inertia depth and loop structure improvements compose without
interference. Composite predicted: 230/230.

---

You are running `/org-chart {topic}`.

DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.

Formal org structure is not the answer -- it is the proposal. Informal coordination
(channels, standups, de-facto leads, shared documents) is the status quo you are
trying to displace. Do not draw an org box until you have argued the case for staying
flat and found the specific failure mode it cannot answer.

---

GATE CHAIN CONTRACT

Gates GATE 0, GATE 1, GATE 2, GATE 3. Each gate's outputs are required inputs for the
subsequent gate. MUST emit in strictly ascending numeric order. Sequence provable from
gate labels. Every gate carries a dedicated verification checkpoint before STATUS.

---

### GATE 0 -- ROLES AND CLASSIFICATION

**Prerequisite:** none
**Produces:** typed role list

GATE 0 DO/DO NOT:
- DO: Read `.craft/roles/` before writing any content.
- DO: List every discovered role in ROLES-LOADED.
- DO NOT: Write any content outside the roles block and classification block before GATE 0 STATUS.
- DO NOT: Introduce a role name in any downstream section that does not appear in this block.

GATE 0 CONTAINMENT CONTRACT -- the following content types MUST NOT appear within GATE 0
before STATUS is emitted:
- Inertia assessment rows or sub-sections
- Org diagram nodes or ASCII hierarchy
- Headcount area entries
- Operating rhythm rows
- Committee charter fields

**Step 0.1 -- Load Roles**

Check `.craft/roles/` for existing role definitions.

```
ROLES-LOADED:
  - [role name] -- [one-line description from role file]
  - [role name] -- [one-line description from role file]
```

If no role files found:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] -- [description]
  - [role name] -- [description]
```

**Step 0.2 -- Role-Type Classification**

Immediately after the roles block -- no structural content may appear between Step 0.1
and Step 0.2. Every role listed in Step 0.1 MUST be typed from the closed set:
{DECISION, EXECUTION, ADVISORY, GOVERNANCE}. Three-tier order: DECISION first,
EXECUTION second, ADVISORY/GOVERNANCE third.

```
ROLE-TYPE-CLASSIFICATION:
  DECISION:
    - [role name]
  EXECUTION:
    - [role name]
  ADVISORY:
    - [role name]
  GOVERNANCE:
    - [role name]
```

MUST NOT proceed past this block until every role from Step 0.1 is typed.

**CHECKPOINT-0 (C-29 -- all-gate blocking)**

- [ ] ROLES-LOADED or ROLES-NOTE present and lists all roles
- [ ] Every role typed from {DECISION, EXECUTION, ADVISORY, GOVERNANCE}
- [ ] No structural content between Step 0.1 and Step 0.2
- [ ] No GATE 0 CONTAINMENT CONTRACT content above this line

```
GATE 0 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 1 requires typed role list. GATE 1 MUST NOT begin if FAIL.

---

### GATE 1 -- INERTIA ASSESSMENT

**Prerequisite:** typed role list from GATE 0
**Produces:** inertia verdict + FLAT-CASE-PRESSURE rating + STRUCTURING-COST FRAME

GATE 1 DO/DO NOT:
- DO: Write the default-position statement as the first executable step (Step 1.0),
  before any mechanism rows.
- DO: Present all four sub-sections in sequence.
- DO: Produce STRUCTURING-COST FRAME and NET-COST-COMPARISON in Sub-section 4 (Step 1.4),
  in fixed anchor order: COST-FRAME CONCLUSION first, NET-COST-COMPARISON second,
  FLAT-CASE-PRESSURE third. NO other content between adjacent anchors.
- DO NOT: Write an org diagram node or headcount entry before GATE 1 STATUS.
- DO NOT: Use a FLAT-CASE-PRESSURE rating outside the closed set {LOW, MEDIUM, HIGH}.
- DO NOT: Use "revisit as the team grows" as trigger.

GATE 1 PROHIBITED CONTENT -- MUST NOT appear within GATE 1 before STATUS:
- ASCII org diagram nodes or hierarchy lines
- Headcount area rows
- Operating rhythm cadence rows
- Committee charter fields

SUB-SECTION-4-ANCHOR-SEQUENCE (A-21 -- Sub-section 4 anchor ordering):
The following three anchors MUST appear in Sub-section 4 in this exact linear order:
  Order 1: COST-FRAME CONCLUSION: (from STRUCTURING-COST FRAME)
  Order 2: NET-COST-COMPARISON: block
  Order 3: FLAT-CASE-PRESSURE: line
CONSTRAINT: No content may appear between Order 1 and Order 2, or between Order 2 and
Order 3. MUST-PRECEDE: Order 1 MUST appear before Order 2; Order 2 MUST appear
before Order 3. Violation of this sequence is a GATE 1 FAIL condition.

**Step 1.0 -- Default-Position Statement (C-28 step embed)**

Write the following statement as the first line of GATE 1, before any mechanism rows:

> DEFAULT POSITION: The team can operate flat; structure must earn its place.

This is an executable step. It MUST be encountered during execution of GATE 1.
It MUST precede the mechanism table. It is not a preamble or scene-setter.

**Step 1.1 -- Case for Staying Flat**

Present a mechanism table with Type from the closed set {CADENCE, CHANNEL, INFORMAL-LEAD,
ARTIFACT}. Produce at least two rows before the separator.

Inline example row (complete, not a label):

| Type | Mechanism | Current Evidence |
|------|-----------|-----------------|
| CADENCE | Weekly cross-area standup | Resolves sprint-level dependencies across two areas without escalation -- no blocked decision in the last quarter |

Two-step separator protocol:
- Step A: Count mechanism rows written above.
- Step B: If count < 2, write missing rows first. Once count >= 2, substitute as N and emit:

```
--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. FLAT-CASE-PRESSURE: [LOW|MEDIUM|HIGH]. How We Coordinate Today begins.] ---
```

**ENFORCEMENT -- GUARD:** DO NOT EMIT the separator before row count >= 2.
DO NOT begin Step 1.2 until the separator appears in output.

**Step 1.2 -- How We Coordinate Today**

Inventory current coordination: channels, cadences, informal roles, artifacts.
DO NOT re-list mechanism rows from Step 1.1.

**Step 1.3 -- Rebuttal**

Name the coordination failure the flat case cannot answer. Reference a specific observable.

**Step 1.4 -- VERDICT and Re-assessment Trigger**

Produce the following in fixed anchor order (SUB-SECTION-4-ANCHOR-SEQUENCE enforced):

STRUCTURING-COST FRAME:
Enumerate the costs of adding structure: decision latency added per approval layer,
coordination overhead (meeting hours per week), onboarding complexity increase,
escalation path length. Each cost entry states the mechanism and its measurable effect.

```
STRUCTURING-COST FRAME:
  [cost mechanism] -- [measurable effect on coordination velocity or overhead]
  [cost mechanism] -- [measurable effect]

COST-FRAME CONCLUSION: [one sentence -- does the structure's benefit outweigh these costs?]
```

NET-COST-COMPARISON block (immediately after COST-FRAME CONCLUSION, no intervening content):

```
NET-COST-COMPARISON:
  Without structure: [coordination overhead without org; reference Step 1.1 mechanisms]
  With structure: [coordination overhead with proposed org; reference failure mode from Step 1.3]
  Net: [direction -- structure reduces/increases net coordination cost by estimated magnitude]
```

FLAT-CASE-PRESSURE (immediately after NET-COST-COMPARISON, no intervening content):
Choose from {LOW, MEDIUM, HIGH}. One-sentence justification.

VERDICT: Choose exactly one: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED.
Concrete re-assessment trigger. DO NOT use "revisit as the team grows."

Flat-verdict branch -- if CAN-OPERATE-FLAT:
```
[ABSENT: ASCII Org Diagram] -- flat verdict.
[ABSENT: Headcount by Area] -- flat verdict.
[ABSENT: Operating Rhythm Table] -- flat verdict.
[ABSENT: Committee Charters] -- flat verdict.
[ABSENT: ORG-ELEMENT REGISTER] -- flat verdict.
[ABSENT: Org Evolution Roadmap] -- flat verdict.
[ABSENT: Anti-Pattern Watch] -- flat verdict.
STOP -- ARTIFACT COMPLETE.
```

**CHECKPOINT INERTIA-CHECK (C-22 -- blocking)**

Before emitting GATE 1 STATUS, verify all checkboxes:
- [ ] Default-position statement precedes mechanism table
- [ ] Case for Staying Flat has >= 2 mechanism rows with Types from closed set
- [ ] STRUCTURING-COST FRAME present with >= 2 cost entries and COST-FRAME CONCLUSION
- [ ] NET-COST-COMPARISON block immediately follows COST-FRAME CONCLUSION (no interceding content)
- [ ] FLAT-CASE-PRESSURE immediately follows NET-COST-COMPARISON (no interceding content)
- [ ] FLAT-CASE-PRESSURE is from {LOW, MEDIUM, HIGH}
- [ ] VERDICT is from {CAN-OPERATE-FLAT, STRUCTURE-WARRANTED} with reasoning sentence
- [ ] Re-assessment trigger is concrete
- [ ] No prohibited content from GATE 1 contract appears above this line

GATE 1 STATUS:
- [ ] Default-position present before mechanism table
- [ ] All 4 sub-sections complete
- [ ] STRUCTURING-COST FRAME + NET-COST-COMPARISON present in anchor order
- [ ] FLAT-CASE-PRESSURE from closed set
- [ ] VERDICT with reasoning and concrete trigger
- [ ] CHECKPOINT INERTIA-CHECK cleared

```
GATE 1 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 2 requires inertia verdict + FLAT-CASE-PRESSURE rating.
If GATE 1 STATUS is FAIL, GATE 2 MUST NOT begin.

---

### GATE 2 -- STRUCTURAL ARTIFACT GENERATION

**Prerequisite:** inertia verdict + FLAT-CASE-PRESSURE rating from GATE 1
**Produces:** org diagram with typed nodes

GATE 2 DO/DO NOT:
- DO: Draw ASCII hierarchy using only role names from ROLES-LOADED.
- DO: Use split Decides/Escalates columns -- separate, not merged.
- DO NOT: Introduce any role name not in GATE 0's typed role list.
- DO NOT: Use a single "Decision Scope" column.

GATE 2 PROHIBITED CONTENT: Operating rhythm cadence rows; committee charter fields.

**Step 2.1 -- ASCII Org Diagram**

Draw ASCII hierarchy with at minimum two levels. Committees as distinct labeled nodes.
All role names MUST come from ROLES-LOADED.

**Step 2.2 -- Headcount by Area**

Five columns: Area, Headcount, Key Roles (with `(domain type)`), Decides, Escalates.
Minimum two area rows + Total row.

Inline example row:

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| Platform Engineering | 6 | Principal Engineer (DECISION) | API versioning policy, breaking-change gates | Cross-product dependency resolution --> Architecture Board |

**CHECKPOINT DIAGRAM-CHECK (C-22 -- blocking)**

- [ ] ASCII diagram >= 2 hierarchy levels
- [ ] All role names in diagram sourced from ROLES-LOADED
- [ ] Committees appear as distinct nodes
- [ ] 5-column headcount (Area, Headcount, Key Roles, Decides, Escalates)
- [ ] >= 2 area rows and a Total row
- [ ] No rhythm rows or charter fields above this line

```
GATE 2 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 3 requires org diagram with typed nodes.
If GATE 2 STATUS is FAIL, GATE 3 MUST NOT begin.

---

### GATE 3 -- GOVERNANCE DOCUMENTATION

**Prerequisite:** org diagram with typed nodes from GATE 2; typed role list from GATE 0
**Produces:** complete governance artifact

GATE 3 DO/DO NOT:
- DO: Interleave rhythm rows and charters.
- DO: Verify pair count after all pairs written.
- DO NOT: Batch rhythm first, charters second.
- DO NOT: Role not in ROLES-LOADED in charter Membership.
- DO NOT: Quorum without `N of M member roles` fraction form.
- DO NOT: Membership without `(TYPE)` annotation on each role.

GATE 3 PROHIBITED CONTENT (C-30): Appendices, supplementary sections, editorial commentary
after Anti-Pattern Watch, unpaired charters, content outside Steps 3.1--3.5.

**Step 3.1 -- Operating Rhythm and Charters (Interleaved)**

>= 3 distinct cadences (ROB, shiproom/gate, governance). No merged rows.

Complete filled charter example:
```
### Architecture Review Board
**Mission:** Evaluate and approve cross-cutting architectural decisions before implementation.
**Membership:** Principal Engineer (DECISION), Engineering Manager (GOVERNANCE), Staff Engineer (ADVISORY)
**Quorum:** 2 of 3 member roles
**Escalates:** VP Engineering
```

REQUIRED: Membership >= 2 roles with `(TYPE)` from {DECISION, EXECUTION, ADVISORY, GOVERNANCE}.
Quorum MUST use `N of M member roles`. For each governance row, immediately produce its charter.

**Step 3.2 -- Pair-Count Verification** (ORT rows == charter count; DO NOT advance until match)
**Step 3.3 -- ORG-ELEMENT REGISTER** (all four categories cat-1 through cat-4 populated)
**Step 3.4 -- Org Evolution Roadmap** (>= 2 rows, distinct triggers; Row 1: headcount threshold)
**Step 3.5 -- Anti-Pattern Watch** (>= 2 rows, `[element name] (cat-N) -- [one sentence]`)

**CHARTER-FORMAT-AUDIT (C-33/C-35/C-36 -- per-charter loop: format + role continuity)**

DO NOT advance to CHECKPOINT-3 until this audit loop has been completed for every
charter produced in Step 3.1.

For each committee charter produced, in sequence, complete this three-check field audit
before advancing to the next charter:

```
Charter: [Committee Name]
[ ] Quorum field: value is in the form `[integer] of [integer] member roles`
    REJECT: fractional notation ("3/5"), percentage ("60%"), prose quorum ("majority of
    members", "quorum required"), bare number without "member roles" suffix, absent field
[ ] Membership entries: each listed role carries exactly one `(TYPE)` annotation where
    TYPE is a value from the closed set {DECISION, EXECUTION, ADVISORY, GOVERNANCE}
    REJECT: role listed without parenthetical; parenthetical value outside the closed set
    (e.g., "(OWNER)", "(LEAD)", "(APPROVER)"); multiple TYPE values on a single entry
[ ] Membership role continuity: for each role name in this charter's Membership field,
    verify the name is present in the GATE 0 ROLES-LOADED or ROLES-NOTE typed role list
    REJECT: role name [X] not found in GATE 0 typed role list -- halt loop at this charter;
    remediation: add [X] to GATE 0 ROLES-LOADED and re-emit GATE 0 STATUS; DO NOT advance
    to the next charter until this charter passes all three checks
```

If any charter fails any check: STOP. Correct the failure. Re-run the full
CHARTER-FORMAT-AUDIT loop from the first charter before advancing to CHECKPOINT-3.

**CHECKPOINT-3 (C-29/C-33/C-34 -- all-gate blocking + format audit + role continuity backup)**

Before emitting GATE 3 STATUS, verify all checkboxes:
- [ ] Operating Rhythm Table has >= 3 distinct rows (ROB, shiproom/gate, governance)
- [ ] Pair count verified: governance rows in ORT == charter count produced
- [ ] Each charter has all 5 fields: Name (header), Mission, Membership, Quorum, Escalates
- [ ] CHARTER-FORMAT-AUDIT completed -- all charters passed all three checks: Quorum
  fraction-pattern, Membership closed-set TYPE, and per-charter Membership role-continuity
  against GATE 0 typed role list (see CHARTER-FORMAT-AUDIT block above)
- [ ] ROLE-CONTINUITY (aggregate backup): For each role name appearing in any charter
  Membership field -- verify present in GATE 0 list; if absent: CHECKPOINT-3 FAILS;
  remediation: add to GATE 0 and re-emit GATE 0 STATUS.
- [ ] ORG-ELEMENT REGISTER has all four categories (cat-1 through cat-4) populated
- [ ] Org Evolution Roadmap has >= 2 rows with distinct trigger categories
- [ ] Anti-Pattern Watch has >= 2 rows with typed citations from register
- [ ] No prohibited content from GATE 3 contract appears above this line

All checkboxes MUST be ticked before GATE 3 STATUS can read PASS.

GATE 3 STATUS:
- [ ] Operating rhythm >= 3 distinct rows
- [ ] Charters complete (5 fields; CHARTER-FORMAT-AUDIT all three checks passed per-charter)
- [ ] Pair count verified
- [ ] ROLE-CONTINUITY (per-charter + aggregate) passed
- [ ] ORG-ELEMENT REGISTER populated (cat-1 through cat-4)
- [ ] Org Evolution Roadmap >= 2 rows with distinct trigger categories
- [ ] Anti-Pattern Watch with typed citations from register
- [ ] GATE 3 prohibited-content contract satisfied
- [ ] CHECKPOINT-3 cleared

```
GATE 3 STATUS: [PASS / FAIL]
```

STOP -- ARTIFACT COMPLETE. No additional content, sections, appendices, or commentary
follows this line.

---

## V-05 -- Full Integration: V-02 Loop + V-04 Inertia + Explicit Gate Chain Articulation

**Axis:** full integration -- V-02 per-charter role-continuity loop (C-36) + V-04
enriched inertia framing (C-01 depth + aspirational Sub-section 4 criteria) + explicit
named-artifact gate chain articulation (each gate preamble names its prerequisite
artifact with source gate reference; each handoff names the consuming gate).
**Hypothesis:** All three axes are structurally independent. The loop targets C-36.
The inertia framing targets aspirational inertia criteria. The explicit gate chain
articulation strengthens C-07 (gate sequence verifiable by label) and aspirational
gate-contract criteria by making each prerequisite artifact explicitly traceable to
its source gate in the preamble. No interaction effect predicted. This is the
strongest composite for v11. C-36 PASS + improved composite on aspirational criteria.
Composite predicted: 230/230 with highest depth score on aspirational subset.

---

You are running `/org-chart {topic}`.

DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.

Formal org structure is not the answer -- it is the proposal. Informal coordination
(channels, standups, de-facto leads, shared documents) is the status quo you are
trying to displace. Do not draw an org box until you have argued the case for staying
flat and found the specific failure mode it cannot answer.

---

GATE CHAIN CONTRACT

Gates GATE 0, GATE 1, GATE 2, GATE 3 in strictly ascending numeric order. Each gate's
named output artifact is a required input for the subsequent gate. No gate may emit
STATUS without its own checkpoint clearing first. Gate sequence is independently
verifiable from gate labels alone -- no gate may precede its numeric predecessor.

```
GATE CHAIN:
  GATE 0 --> [artifact: typed role list] --> GATE 1
  GATE 1 --> [artifact: inertia verdict + FLAT-CASE-PRESSURE rating] --> GATE 2
  GATE 2 --> [artifact: org diagram with typed nodes] --> GATE 3
  GATE 3 --> [artifact: complete governance document] --> TERMINAL
```

---

### GATE 0 -- ROLES AND CLASSIFICATION

**Prerequisite:** none (first gate)
**Produces:** typed role list [consumed by GATE 1 as prerequisite]

GATE 0 DO/DO NOT:
- DO: Read `.craft/roles/` before writing any content.
- DO: List every discovered role in ROLES-LOADED.
- DO NOT: Write any content outside the roles block and classification block before GATE 0 STATUS.
- DO NOT: Introduce a role name in any downstream section that does not appear in this block.

GATE 0 CONTAINMENT CONTRACT -- the following content types MUST NOT appear within GATE 0
before STATUS is emitted:
- Inertia assessment rows or sub-sections
- Org diagram nodes or ASCII hierarchy
- Headcount area entries
- Operating rhythm rows
- Committee charter fields

**Step 0.1 -- Load Roles**

Check `.craft/roles/` for existing role definitions.

```
ROLES-LOADED:
  - [role name] -- [one-line description from role file]
  - [role name] -- [one-line description from role file]
```

If no role files found:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] -- [description]
  - [role name] -- [description]
```

**Step 0.2 -- Role-Type Classification**

Immediately after the roles block -- no structural content may appear between Step 0.1
and Step 0.2. Every role listed in Step 0.1 MUST be typed from the closed set:
{DECISION, EXECUTION, ADVISORY, GOVERNANCE}. Three-tier order: DECISION first,
EXECUTION second, ADVISORY/GOVERNANCE third.

```
ROLE-TYPE-CLASSIFICATION:
  DECISION:
    - [role name]
  EXECUTION:
    - [role name]
  ADVISORY:
    - [role name]
  GOVERNANCE:
    - [role name]
```

MUST NOT proceed past this block until every role from Step 0.1 is typed.

**CHECKPOINT-0 (C-29 -- all-gate blocking)**

Before emitting GATE 0 STATUS, verify all items:
- [ ] ROLES-LOADED or ROLES-NOTE block is present and lists all roles
- [ ] ROLE-TYPE-CLASSIFICATION assigns every role a type from {DECISION, EXECUTION, ADVISORY, GOVERNANCE}
- [ ] No structural content appeared between Step 0.1 and Step 0.2
- [ ] No content from the GATE 0 CONTAINMENT CONTRACT appears above this line

All checkboxes MUST be ticked before GATE 0 STATUS can read PASS.

GATE 0 STATUS:
- [ ] Roles block present
- [ ] All roles typed from closed set
- [ ] Containment contract satisfied
- [ ] CHECKPOINT-0 cleared

```
GATE 0 STATUS: [PASS / FAIL]
```

If FAIL: DO NOT advance to GATE 1. Correct the gap above and re-verify.

**Named artifact handoff to GATE 1:** typed role list produced in Steps 0.1--0.2.
GATE 1 MUST NOT begin until GATE 0 STATUS is PASS.

---

### GATE 1 -- INERTIA ASSESSMENT

**Prerequisite:** typed role list [from GATE 0, Steps 0.1--0.2]
**Produces:** inertia verdict + FLAT-CASE-PRESSURE rating + STRUCTURING-COST FRAME
             [consumed by GATE 2 as prerequisite]

GATE 1 DO/DO NOT:
- DO: Write the default-position statement as Step 1.0 before any mechanism rows.
- DO: Present all four sub-sections in sequence.
- DO: Produce STRUCTURING-COST FRAME with COST-FRAME CONCLUSION in Step 1.4.
- DO: Produce NET-COST-COMPARISON block immediately after COST-FRAME CONCLUSION.
- DO: Emit FLAT-CASE-PRESSURE immediately after NET-COST-COMPARISON (no intervening content).
- DO NOT: Write an org diagram node or headcount entry before GATE 1 STATUS.
- DO NOT: Use FLAT-CASE-PRESSURE outside {LOW, MEDIUM, HIGH}.
- DO NOT: Use "revisit as the team grows" -- trigger MUST name a concrete condition.

GATE 1 PROHIBITED CONTENT -- MUST NOT appear within GATE 1 before STATUS:
- ASCII org diagram nodes or hierarchy lines
- Headcount area rows
- Operating rhythm cadence rows
- Committee charter fields

SUB-SECTION-4-ANCHOR-SEQUENCE (mandatory ordering in Step 1.4):
Three anchors in fixed order with no interceding content between adjacent pairs:
  Order 1: COST-FRAME CONCLUSION: (last line of STRUCTURING-COST FRAME block)
  Order 2: NET-COST-COMPARISON: (block immediately after Order 1)
  Order 3: FLAT-CASE-PRESSURE: (line immediately after Order 2)
CONSTRAINT: NO other content between Order 1 and Order 2.
CONSTRAINT: NO other content between Order 2 and Order 3.

**Step 1.0 -- Default-Position Statement (C-28 step embed)**

Write the following statement as the first line of GATE 1, before any mechanism rows:

> DEFAULT POSITION: The team can operate flat; structure must earn its place.

This is an executable step. It MUST be encountered during execution of GATE 1.
It MUST precede the mechanism table. It is not a preamble or scene-setter.

**Step 1.1 -- Case for Staying Flat**

Present a mechanism table with Type from the closed set {CADENCE, CHANNEL, INFORMAL-LEAD,
ARTIFACT}. Produce at least two rows before the separator.

Inline example row (complete, not a label):

| Type | Mechanism | Current Evidence |
|------|-----------|-----------------|
| CADENCE | Weekly cross-area standup | Resolves sprint-level dependencies across two areas without escalation -- no blocked decision in the last quarter |

Two-step separator protocol:
- Step A: Count mechanism rows written above.
- Step B: If count < 2, write missing rows first. Once count >= 2, substitute as N and emit:

```
--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. FLAT-CASE-PRESSURE: [LOW|MEDIUM|HIGH]. How We Coordinate Today begins.] ---
```

**ENFORCEMENT -- GUARD:** DO NOT EMIT separator before row count >= 2.
Two-site: Step 1.2 MUST be preceded by the separator.

**Step 1.2 -- How We Coordinate Today**

Inventory current coordination: channels, cadences, informal roles, artifacts.
DO NOT re-list mechanism rows from Step 1.1.

**Step 1.3 -- Rebuttal**

Name the coordination failure the flat case cannot answer. Reference a specific observable.

**Step 1.4 -- VERDICT and Re-assessment Trigger**

Produce the following in SUB-SECTION-4-ANCHOR-SEQUENCE order:

STRUCTURING-COST FRAME:
Enumerate the costs of adding structure -- decision latency, coordination overhead
(meeting hours per week), onboarding complexity, escalation path length. Each entry
states the mechanism and measurable effect.

```
STRUCTURING-COST FRAME:
  [cost mechanism] -- [measurable effect on velocity or overhead]
  [cost mechanism] -- [measurable effect]

COST-FRAME CONCLUSION: [one sentence -- does structure's benefit outweigh these costs?]
```

NET-COST-COMPARISON block (immediately after COST-FRAME CONCLUSION; NO intervening content):

```
NET-COST-COMPARISON:
  Without structure: [coordination overhead; reference Step 1.1 mechanisms]
  With structure: [coordination overhead with org; reference failure mode from Step 1.3]
  Net: [direction -- structure reduces/increases net coordination cost by estimated magnitude]
```

FLAT-CASE-PRESSURE (immediately after NET-COST-COMPARISON; NO intervening content):
Choose from {LOW, MEDIUM, HIGH}. One-sentence justification referencing NET-COST-COMPARISON.

VERDICT: Choose exactly one: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED.
Reasoning sentence. Concrete re-assessment trigger. DO NOT use "revisit as the team grows."

Flat-verdict branch -- if CAN-OPERATE-FLAT:
```
[ABSENT: ASCII Org Diagram] -- flat verdict. "Simplified" alternatives not acceptable.
[ABSENT: Headcount by Area] -- flat verdict.
[ABSENT: Operating Rhythm Table] -- flat verdict.
[ABSENT: Committee Charters] -- flat verdict.
[ABSENT: ORG-ELEMENT REGISTER] -- flat verdict.
[ABSENT: Org Evolution Roadmap] -- flat verdict.
[ABSENT: Anti-Pattern Watch] -- flat verdict.
STOP -- ARTIFACT COMPLETE. No content follows this directive.
```

**CHECKPOINT INERTIA-CHECK (C-22 -- blocking)**

Before emitting GATE 1 STATUS, verify all checkboxes:
- [ ] Default-position statement precedes mechanism table
- [ ] Case for Staying Flat has >= 2 mechanism rows with Types from closed set
- [ ] STRUCTURING-COST FRAME present with >= 2 cost entries and COST-FRAME CONCLUSION
- [ ] NET-COST-COMPARISON block immediately follows COST-FRAME CONCLUSION (no interceding content)
- [ ] FLAT-CASE-PRESSURE immediately follows NET-COST-COMPARISON (no interceding content)
- [ ] FLAT-CASE-PRESSURE is from {LOW, MEDIUM, HIGH}
- [ ] VERDICT is from {CAN-OPERATE-FLAT, STRUCTURE-WARRANTED} with reasoning sentence
- [ ] Re-assessment trigger is concrete
- [ ] No prohibited content from GATE 1 contract appears above this line

GATE 1 STATUS:
- [ ] Default-position present before mechanism table
- [ ] All 4 sub-sections complete
- [ ] STRUCTURING-COST FRAME + NET-COST-COMPARISON in SUB-SECTION-4-ANCHOR-SEQUENCE order
- [ ] FLAT-CASE-PRESSURE from closed set
- [ ] VERDICT with reasoning and concrete trigger
- [ ] CHECKPOINT INERTIA-CHECK cleared

```
GATE 1 STATUS: [PASS / FAIL]
```

If FAIL: DO NOT advance to GATE 2.

**Named artifact handoff to GATE 2:** inertia verdict + FLAT-CASE-PRESSURE rating
[produced in Steps 1.0--1.4]. GATE 2 MUST NOT begin until GATE 1 STATUS is PASS.

---

### GATE 2 -- STRUCTURAL ARTIFACT GENERATION

**Prerequisite:** inertia verdict + FLAT-CASE-PRESSURE rating [from GATE 1, Step 1.4]
**Produces:** org diagram with typed nodes [consumed by GATE 3 as prerequisite]

GATE 2 DO/DO NOT:
- DO: Draw ASCII hierarchy using only role names from ROLES-LOADED [from GATE 0].
- DO: Use split Decides/Escalates columns -- separate, not merged.
- DO NOT: Introduce any role name not in GATE 0's typed role list.
- DO NOT: Use a single "Decision Scope" column.

GATE 2 PROHIBITED CONTENT -- MUST NOT appear within GATE 2 before STATUS:
- Operating rhythm cadence rows
- Committee charter fields

**Step 2.1 -- ASCII Org Diagram**

Draw ASCII hierarchy with at minimum two levels. Committees as distinct labeled nodes.
All role names MUST come from ROLES-LOADED [GATE 0].

**Step 2.2 -- Headcount by Area**

Five columns: Area, Headcount, Key Roles, Decides, Escalates. Key Roles annotated with
`(domain type)`. Decides and Escalates are separate columns.

Inline example row (complete, not a label):

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| Platform Engineering | 6 | Principal Engineer (DECISION) | API versioning policy, breaking-change gates | Cross-product dependency resolution --> Architecture Board |

```
| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| [name] | [N or N-M] | [role (domain type)] | [decision types owned] | [decisions escalated] |
| [name] | [N or N-M] | [role (domain type)] | [decision types owned] | [decisions escalated] |
| **Total** | **[N]** | | | |
```

At minimum two area rows with individual counts and a Total row.

**CHECKPOINT DIAGRAM-CHECK (C-22 -- blocking)**

Before emitting GATE 2 STATUS, verify all checkboxes:
- [ ] ASCII diagram >= 2 hierarchy levels
- [ ] All role names in diagram sourced from ROLES-LOADED [GATE 0]
- [ ] Committees appear as distinct nodes (not embedded)
- [ ] Headcount table has five columns (Area, Headcount, Key Roles, Decides, Escalates)
- [ ] At least two area rows and a Total row present
- [ ] No rhythm rows or charter fields above this line

GATE 2 STATUS:
- [ ] ASCII diagram present with >= 2 hierarchy levels
- [ ] Committees as distinct nodes
- [ ] Headcount has split Decides/Escalates columns
- [ ] >= 2 area rows + Total row
- [ ] CHECKPOINT DIAGRAM-CHECK cleared

```
GATE 2 STATUS: [PASS / FAIL]
```

If FAIL: DO NOT advance to GATE 3.

**Named artifact handoff to GATE 3:** org diagram with typed nodes [produced in Step 2.1].
GATE 3 MUST NOT begin until GATE 2 STATUS is PASS.

---

### GATE 3 -- GOVERNANCE DOCUMENTATION

**Prerequisite:** org diagram with typed nodes [from GATE 2, Step 2.1];
               typed role list [from GATE 0, Steps 0.1--0.2]
**Produces:** complete governance artifact [terminal output]

GATE 3 DO/DO NOT:
- DO: Produce operating rhythm rows and committee charters in interleaved pairs -- each
  governance row immediately followed by its charter.
- DO: Verify pair count equals governance row count after all pairs are written.
- DO NOT: Batch all rhythm rows first and all charters second.
- DO NOT: Reference a role not in ROLES-LOADED [GATE 0] in a charter Membership field.
- DO NOT: Write a Quorum field without `N of M member roles` fraction form.
- DO NOT: Write Membership without `(TYPE)` annotation on each role.

GATE 3 PROHIBITED CONTENT (C-30 -- terminal gate contract) -- MUST NOT appear within
GATE 3 before STATUS is emitted:
- Appendices of any kind
- Supplementary sections (additional tables, notes, annexes)
- Editorial commentary or rationale paragraphs after the Anti-Pattern Watch table
- Additional committee charters not paired with an operating rhythm row
- Any content category not explicitly part of Steps 3.1 through 3.5

Terminal-gate position does not exempt GATE 3 from this contract. The intra-gate content
risk at GATE 3 is content appended after the Anti-Pattern Watch table and before STATUS.

**Step 3.1 -- Operating Rhythm and Charters (Interleaved)**

Operating rhythm: >= 3 distinct cadences (ROB, shiproom/gate, governance). No merged rows.

Inline example row for operating rhythm (complete, not a label):

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|
| Architecture Board | Monthly | Principal Engineer | Review and approve cross-cutting design decisions affecting two or more service areas |

**Charter format -- 5 fields required (complete example)**

Complete filled example (model this format; fill concrete values for your topic):

```
### Architecture Review Board

**Mission:** Evaluate and approve cross-cutting architectural decisions before
implementation begins, ensuring consistency across all service areas.
**Membership:** Principal Engineer (DECISION), Engineering Manager (GOVERNANCE),
Staff Engineer (ADVISORY)
**Quorum:** 2 of 3 member roles
**Escalates:** VP Engineering
```

Charter template for each governance committee:

```
### [Committee Name]

**Mission:** [one sentence -- what this committee decides or governs]
**Membership:** [Role A (TYPE)], [Role B (TYPE)]
**Quorum:** [N] of [M] member roles
**Escalates:** [named destination role or forum]
```

REQUIRED:
- Membership MUST list >= 2 roles each annotated with `(TYPE)` from
  {DECISION, EXECUTION, ADVISORY, GOVERNANCE}.
- Quorum MUST use `N of M member roles` fraction form. Percentage, prose quorum
  ("majority"), or missing Quorum field is not acceptable. See filled example above.
- All role names in Membership MUST come from ROLES-LOADED [GATE 0].

For each governance cadence row, immediately produce its charter. DO NOT batch.

**Step 3.2 -- Post-Interleave Pair-Count Verification (C-19)**

After all rhythm-charter pairs are produced:
- Count governance rows in the Operating Rhythm Table: [N]
- Count committee charters produced: [N]
- MUST match. If mismatch: identify the gap, produce missing charter, recount.
  DO NOT advance to Step 3.3 until counts match.

**Step 3.3 -- ORG-ELEMENT REGISTER**

MUST produce immediately after Committee Charters. All four categories MUST be
populated before advancing to Step 3.4.

```
ORG-ELEMENT REGISTER

  Category schema:
  | cat-N | Category name         | Element type                                          |
  |-------|-----------------------|-------------------------------------------------------|
  | cat-1 | Areas                 | Area names from the Headcount by Area table           |
  | cat-2 | Committees/Cadences   | Committee and cadence names from Rhythm Table/Charters|
  | cat-3 | Headcount             | Total headcount and per-area headcount counts         |
  | cat-4 | DRI Roles             | DRI role names from the Operating Rhythm Table        |

  cat-1 (Areas):
    - [area name] -- headcount: [N]

  cat-2 (Committees/Cadences):
    - [committee or cadence name]

  cat-3 (Headcount):
    - Total headcount: [N]

  cat-4 (DRI Roles):
    - [DRI role name]
```

**Step 3.4 -- Org Evolution Roadmap**

At minimum two rows, distinct trigger categories. Row 1 MUST be a headcount threshold.
Row 2 MUST be from a different category (workload signal, structural symptom, or milestone).

Inline example row (complete, not a label):

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| Headcount exceeds 15 engineers | Split Platform area into Core and Extensions sub-areas; add Area Lead role | headcount-threshold |

**Step 3.5 -- Anti-Pattern Watch**

At minimum two rows. Each "Why It Applies Here" cell MUST open with:
`[element name] (cat-N) -- [one sentence]`

Element names copied exactly from ORG-ELEMENT REGISTER.
DO NOT use a cat-N code not in the register schema.

**CHARTER-FORMAT-AUDIT (C-33/C-35/C-36 -- per-charter loop: format + role continuity integrated)**

DO NOT advance to CHECKPOINT-3 until this audit loop has been completed for every
charter produced in Step 3.1.

For each committee charter produced, in sequence, complete this three-check field audit
before advancing the loop to the next charter. All three checks execute at this charter
before the loop may advance:

```
Charter: [Committee Name]
[ ] Quorum field: value is in the form `[integer] of [integer] member roles`
    REJECT: fractional notation ("3/5"), percentage ("60%"), prose quorum ("majority of
    members", "quorum required"), bare number without "member roles" suffix ("3"), absent field
[ ] Membership entries: each listed role carries exactly one `(TYPE)` annotation where
    TYPE is a value from the closed set {DECISION, EXECUTION, ADVISORY, GOVERNANCE}
    REJECT: role listed without parenthetical; parenthetical value outside the closed set
    (e.g., "(OWNER)", "(LEAD)", "(APPROVER)"); multiple TYPE values on a single entry
[ ] Membership role continuity: for each role name in this charter's Membership field,
    verify the name is present in the GATE 0 ROLES-LOADED or ROLES-NOTE typed role list
    REJECT: role name [X] not found in GATE 0 typed role list -- halt loop at this charter;
    remediation: add [X] to GATE 0 ROLES-LOADED and re-emit GATE 0 STATUS before the
    loop continues; DO NOT advance to the next charter until this charter passes check 3
```

LOOP HALT CONDITION: any REJECT on any check halts the loop at the failing charter.
Correct the specific failure. Re-run the complete CHARTER-FORMAT-AUDIT loop from the
first charter. DO NOT advance to CHECKPOINT-3 until all charters pass all three checks.

**CHECKPOINT-3 (C-29/C-33/C-34 -- all-gate blocking + charter audit reference + aggregate backup)**

Before emitting GATE 3 STATUS, verify all checkboxes:
- [ ] Operating Rhythm Table has >= 3 distinct rows (ROB, shiproom/gate, governance)
- [ ] Pair count verified: governance rows in ORT == charter count produced
- [ ] Each charter has all 5 fields: Name (header), Mission, Membership, Quorum, Escalates
- [ ] CHARTER-FORMAT-AUDIT loop completed -- every charter individually passed all three
  checks in sequence: (1) Quorum fraction-pattern, (2) Membership closed-set TYPE,
  (3) per-charter Membership role-continuity against the GATE 0 typed role list;
  the loop halted and remediated at any REJECT before advancing (see loop above)
- [ ] ROLE-CONTINUITY (aggregate backup): For each role name appearing in any charter
  Membership field -- verify present in GATE 0 ROLES-LOADED or ROLES-NOTE list.
  If absent: CHECKPOINT-3 FAILS. Remediation: add to GATE 0, re-emit GATE 0 STATUS.
- [ ] ORG-ELEMENT REGISTER has all four categories (cat-1 through cat-4) populated
- [ ] Org Evolution Roadmap has >= 2 rows with distinct trigger categories
- [ ] Anti-Pattern Watch has >= 2 rows with typed citations from register
- [ ] No prohibited content from GATE 3 contract appears above this line

All checkboxes MUST be ticked before GATE 3 STATUS can read PASS.

GATE 3 STATUS:
- [ ] Operating rhythm >= 3 distinct rows
- [ ] Charters complete (5 fields; CHARTER-FORMAT-AUDIT three-check loop passed per-charter)
- [ ] Pair count verified
- [ ] ROLE-CONTINUITY (per-charter in loop + aggregate in checkpoint) passed
- [ ] ORG-ELEMENT REGISTER populated (cat-1 through cat-4)
- [ ] Org Evolution Roadmap >= 2 rows with distinct trigger categories
- [ ] Anti-Pattern Watch with typed citations from register
- [ ] GATE 3 prohibited-content contract satisfied
- [ ] CHECKPOINT-3 cleared

```
GATE 3 STATUS: [PASS / FAIL]
```

STOP -- ARTIFACT COMPLETE. No additional content, sections, appendices, or commentary
follows this line. (C-31 -- successful-completion path terminal seal)
