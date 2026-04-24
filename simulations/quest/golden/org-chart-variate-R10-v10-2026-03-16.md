---
skill: quest-variate
skill_target: org-chart
date: 2026-03-16
round: R10
rubric_version: v10
status: variate
---

# org-chart Variate -- Round 10 (Rubric v10)

**Date:** 2026-03-16
**Skill:** org-chart
**Rubric:** v10 (C-01 through C-34; C-33/C-34 new from R9 excellence signals)
**Round:** R10 -- single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

## R9 ceiling and R10 target

R9-V-05 achieves 210/210 on the v9 rubric (all C-01 through C-32 pass). v10 adds two
aspirational criteria (5 pts each), bringing total to 220 pts, golden >= 176/220 (80%).
R9-V-05 scores 210/220 = 95.5% on v10 -- two gaps remain:

**C-33 gap (GATE 3 field-format verification coverage):**
CHECKPOINT-3 in R9-V-05 carries two relevant items:

```
- [ ] Quorum in `N of M member roles` form for all charters
- [ ] Membership >= 2 roles with `(TYPE)` annotation for all charters
```

These verify presence but not closed-set compliance: the Quorum check does not name the
prohibited alternatives (ratio notation, percentage, prose quorum, bare number), and the
Membership TYPE check does not name the closed set {DECISION, EXECUTION, ADVISORY,
GOVERNANCE} within the checkpoint item itself. C-33 requires the GATE 3 checkpoint to
inspect field-level format compliance with the specific pattern and closed-set constraints,
not only confirm that the fields exist in some form. The gap: a model verifying "Quorum in
N of M member roles form" could read a "majority of 5" Quorum as conformant because it
contains the fraction shape; a model verifying "Membership has (TYPE) annotation" could
accept (OWNER) or (LEAD) as TYPE values. The closed-set rejection must live in the
checkpoint item, not only in the production instruction.

**C-34 gap (cross-gate role continuity assertion in GATE 3 checkpoint):**
CHECKPOINT-3 in R9-V-05 has no item that cross-references Membership role names against
the GATE 0 typed role list. C-02 declares "no role introduced later that wasn't declared
here" at GATE 0 declaration scope (authoring-time enforcement). C-25 names the typed role
list as a GATE 3 prerequisite (handoff-scope). But CHECKPOINT-3 has no lookup-table step
that consumes the GATE 0 list when verifying Membership fields at checkpoint-execution
time. A Membership entry that satisfies C-33 syntactically -- correct TYPE value from the
closed set, correct Quorum fraction -- can pass CHECKPOINT-3 if the role name itself was
never declared in GATE 0. C-34 requires the lookup to execute at GATE 3 checkpoint time,
converting C-02's declaration-scope constraint into a checkpoint-execution verification.

**R10 target:** Close both gaps. V-01/V-02/V-03 single-axis. V-04 combines V-01+V-02.
V-05 integrates V-03+V-02 on the full R9-V-05 baseline.

---

## R10 Variation Map

| V | Axis | New element(s) | C-33 | C-34 |
|---|------|---------------|------|------|
| V-01 | Lifecycle emphasis: CHECKPOINT-3 explicit closed-set format items | Replace generic items 4-5 with FORMAT-VERIFY items naming prohibited patterns and closed sets by value | TARGET | open |
| V-02 | Lifecycle emphasis: CHECKPOINT-3 cross-gate role-continuity item | Add ROLE-CONTINUITY lookup item; FAIL directive if any Membership name absent from GATE 0 | open | TARGET |
| V-03 | Output format: dedicated CHARTER-FORMAT-AUDIT loop before CHECKPOINT-3 | Per-charter audit block with REJECT conditions; CHECKPOINT-3 references completed audit | TARGET (alt) | open |
| V-04 | Combined: V-01 + V-02 | FORMAT-VERIFY items (C-33) + ROLE-CONTINUITY item (C-34) in CHECKPOINT-3 | TARGET | TARGET |
| V-05 | Full integration: V-03 + V-02 | CHARTER-FORMAT-AUDIT block (C-33) + ROLE-CONTINUITY item (C-34) on R9-V-05 baseline | TARGET | TARGET |

**Single-axis hypothesis:**
- V-01: Strengthening CHECKPOINT-3 items 4-5 to name the prohibited Quorum patterns
  and the TYPE closed set converts generic presence checks into field-format compliance
  verification. C-33 PASS predicted; C-34 open.
- V-02: Adding a ROLE-CONTINUITY lookup item to CHECKPOINT-3 that names the GATE 0 list
  as the authority and states a FAIL directive with remediation converts C-02's
  declaration-scope constraint into a checkpoint-execution lookup. C-34 PASS predicted;
  C-33 open.
- V-03: A dedicated CHARTER-FORMAT-AUDIT loop placed between Step 3.5 and CHECKPOINT-3,
  with per-charter REJECT conditions and a DO NOT advance directive, satisfies C-33's
  "for every produced charter" requirement more explicitly than inline checkpoint items;
  tests whether the dedicated-block format is structurally distinct from the inline-item
  format for rubric-scoring purposes.

---

## V-01 -- Explicit Closed-Set Format Items in CHECKPOINT-3 (C-33 only)

**Axis:** lifecycle emphasis -- strengthen CHECKPOINT-3 items 4 and 5 to name the
prohibited alternative patterns for Quorum (ratio, percentage, prose, bare number) and to
name the closed set {DECISION, EXECUTION, ADVISORY, GOVERNANCE} for Membership TYPE
verification, making each a FORMAT-VERIFY item rather than a generic presence check.
**Hypothesis:** Items 4-5 in R9-V-05's CHECKPOINT-3 verify that Quorum and Membership
exist in approximately the correct form but do not name what is prohibited. A model can
read "Quorum in N of M member roles form" as satisfied by "majority of 5" (contains
number-of-number shape) or read "(TYPE) annotation" as satisfied by "(OWNER)". Adding
FORMAT-VERIFY items that name each prohibited pattern and the TYPE closed set by value
makes each rejection condition independently verifiable at the checkpoint without parsing
surrounding prose. C-34 remains open: no cross-gate Membership name lookup is added.

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
- DO: Read `.roles/` before writing any content.
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

Check `.roles/` for existing role definitions.

```
ROLES-LOADED:
  - [role name] -- [one-line description from role file]
  - [role name] -- [one-line description from role file]
```

If no role files found:
```
ROLES-NOTE: No .roles/ files found. Using inferred roles:
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
- [ ] Default-position statement present before mechanism table
- [ ] All 4 sub-sections complete
- [ ] FLAT-CASE-PRESSURE from closed set
- [ ] VERDICT from closed set with reasoning and concrete trigger
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

**Charter format -- 5 fields required (C-05 / C-32 -- complete example)**

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
  ("majority"), or missing Quorum field is not acceptable. See filled example above.

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

**CHECKPOINT-3 (C-29/C-33 -- all-gate blocking + field-format verification)**

Before emitting GATE 3 STATUS, verify all checkboxes:
- [ ] Operating Rhythm Table has >= 3 distinct rows (ROB, shiproom/gate, governance)
- [ ] Pair count verified: governance rows in ORT == charter count produced
- [ ] Each charter has all 5 fields: Name (header), Mission, Membership, Quorum, Escalates
- [ ] FORMAT-VERIFY QUORUM: For each charter produced -- Quorum field value is in the
  form `[integer] of [integer] member roles`; fractional notation ("3/5"), percentage
  ("60%"), prose quorum ("majority of members"), or bare number alone are NOT acceptable
  alternatives; absence of the word "roles" is not acceptable
- [ ] FORMAT-VERIFY MEMBERSHIP TYPE: For each charter produced -- every Membership role
  entry carries a `(TYPE)` annotation where TYPE is exactly one value from the closed set
  {DECISION, EXECUTION, ADVISORY, GOVERNANCE}; an unannotated entry, a TYPE value outside
  this closed set (e.g., "(OWNER)", "(LEAD)", "(APPROVER)"), or multiple TYPE annotations
  on a single entry do not satisfy this check
- [ ] ORG-ELEMENT REGISTER has all four categories (cat-1 through cat-4) populated
- [ ] Org Evolution Roadmap has >= 2 rows with distinct trigger categories
- [ ] Anti-Pattern Watch has >= 2 rows with typed citations from register
- [ ] No prohibited content from GATE 3 contract appears above this line

All checkboxes MUST be ticked before GATE 3 STATUS can read PASS.

GATE 3 STATUS:
- [ ] Operating rhythm >= 3 distinct rows
- [ ] Charters complete (5 fields; Quorum fraction form verified; Membership closed-set TYPE verified)
- [ ] Pair count verified
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

## V-02 -- Cross-Gate Role Continuity in CHECKPOINT-3 (C-34 only)

**Axis:** lifecycle emphasis -- add a ROLE-CONTINUITY lookup item to CHECKPOINT-3 that
cross-references every Membership role name against the GATE 0 typed role list; if any
name is absent from GATE 0, the checkpoint FAILS with an explicit remediation directive.
**Hypothesis:** C-02 enforces "no role introduced later" at GATE 0 declaration scope.
C-25 names the typed role list as a GATE 3 prerequisite at handoff scope. Neither
embeds a lookup-table step at GATE 3 checkpoint-execution time. A Membership entry
can satisfy the existing format checks (C-33 remains at the R9-V-05 generic level here)
while referencing a role never declared in GATE 0 -- passing C-02 at authoring-time read
but violating it at execution time. Adding a ROLE-CONTINUITY item that explicitly names
the GATE 0 list as the lookup authority and states a FAIL directive with remediation
converts the declaration-scope constraint into a checkpoint-execution lookup. C-33
remains at R9-V-05 generic level in this variation; only C-34 is targeted.

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
- DO: Read `.roles/` before writing any content.
- DO: List every discovered role in ROLES-LOADED.
- DO NOT: Write any content outside the roles block and classification block before GATE 0 STATUS.
- DO NOT: Introduce a role name in any downstream section that does not appear in this block.

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
ROLES-NOTE: No .roles/ files found. Using inferred roles:
  - [role name] -- [description]
  - [role name] -- [description]
```

**Step 0.2 -- Role-Type Classification**

Immediately after the roles block -- no structural content may appear between Step 0.1
and Step 0.2. Every role MUST be typed from {DECISION, EXECUTION, ADVISORY, GOVERNANCE}.
Three-tier order: DECISION first, EXECUTION second, ADVISORY/GOVERNANCE third.

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

Before emitting GATE 0 STATUS, verify:
- [ ] ROLES-LOADED or ROLES-NOTE present and lists all roles
- [ ] ROLE-TYPE-CLASSIFICATION assigns every role a type from {DECISION, EXECUTION, ADVISORY, GOVERNANCE}
- [ ] No structural content between Step 0.1 and Step 0.2
- [ ] No content from GATE 0 CONTAINMENT CONTRACT above this line

```
GATE 0 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 1 requires typed role list. GATE 1 MUST NOT begin if GATE 0 FAIL.

---

### GATE 1 -- INERTIA ASSESSMENT

**Prerequisite:** typed role list from GATE 0
**Produces:** inertia verdict + FLAT-CASE-PRESSURE rating

GATE 1 DO/DO NOT:
- DO: Write default-position statement as Step 1.0 before any mechanism rows.
- DO: Four sub-sections in sequence.
- DO NOT: Org diagram or headcount content before GATE 1 STATUS.
- DO NOT: FLAT-CASE-PRESSURE outside {LOW, MEDIUM, HIGH}.
- DO NOT: "Revisit as the team grows" as trigger.

GATE 1 PROHIBITED CONTENT -- MUST NOT appear before GATE 1 STATUS:
- ASCII org diagram nodes, headcount area rows, rhythm cadence rows, charter fields

**Step 1.0 -- Default-Position Statement (C-28)**

> DEFAULT POSITION: The team can operate flat; structure must earn its place.

MUST precede mechanism table. Executable step, not a preamble.

**Step 1.1 -- Case for Staying Flat**

Mechanism table, Type from {CADENCE, CHANNEL, INFORMAL-LEAD, ARTIFACT}, >= 2 rows.

Inline example row:

| Type | Mechanism | Current Evidence |
|------|-----------|-----------------|
| CADENCE | Weekly cross-area standup | Resolves sprint-level dependencies across two areas without escalation -- no blocked decision in the last quarter |

Two-step separator: count rows, verify >= 2, emit:
```
--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. FLAT-CASE-PRESSURE: [LOW|MEDIUM|HIGH]. How We Coordinate Today begins.] ---
```

ENFORCEMENT GUARD: DO NOT EMIT separator before row count >= 2.
Two-site: Sub-section 1.2 MUST be preceded by separator.

**Steps 1.2--1.4:** How We Coordinate Today / Rebuttal / VERDICT with concrete trigger.

Flat-verdict branch:
```
[ABSENT: ASCII Org Diagram] -- flat verdict. No simplified alternative acceptable.
[ABSENT: Headcount by Area] -- flat verdict.
[ABSENT: Operating Rhythm Table] -- flat verdict.
[ABSENT: Committee Charters] -- flat verdict.
[ABSENT: ORG-ELEMENT REGISTER] -- flat verdict.
[ABSENT: Org Evolution Roadmap] -- flat verdict.
[ABSENT: Anti-Pattern Watch] -- flat verdict.
STOP -- ARTIFACT COMPLETE. No content follows this directive.
```

**CHECKPOINT INERTIA-CHECK (C-22)**

- [ ] Default-position statement precedes mechanism table
- [ ] >= 2 mechanism rows with Types from closed set
- [ ] FLAT-CASE-PRESSURE from {LOW, MEDIUM, HIGH}
- [ ] VERDICT from {CAN-OPERATE-FLAT, STRUCTURE-WARRANTED} with reasoning
- [ ] Concrete re-assessment trigger
- [ ] No prohibited content above this line

```
GATE 1 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 2 requires inertia verdict + FLAT-CASE-PRESSURE.

---

### GATE 2 -- STRUCTURAL ARTIFACT GENERATION

**Prerequisite:** inertia verdict + FLAT-CASE-PRESSURE rating from GATE 1
**Produces:** org diagram with typed nodes

GATE 2 DO/DO NOT:
- DO: ASCII hierarchy from ROLES-LOADED only. Split Decides/Escalates.
- DO NOT: New roles. DO NOT: Merged decision column.

GATE 2 PROHIBITED CONTENT: rhythm rows, charter fields.

**Step 2.1 -- ASCII Org Diagram** (>= 2 levels, committees as distinct nodes, ROLES-LOADED names)

**Step 2.2 -- Headcount by Area**

Five columns: Area, Headcount, Key Roles (with `(domain type)`), Decides, Escalates.

Inline example row:

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| Platform Engineering | 6 | Principal Engineer (DECISION) | API versioning policy, breaking-change gates | Cross-product dependency resolution --> Architecture Board |

Minimum two area rows + Total row.

**CHECKPOINT DIAGRAM-CHECK (C-22)**

- [ ] Diagram >= 2 levels, roles from ROLES-LOADED, committees distinct
- [ ] 5-column headcount, Decides/Escalates split, >= 2 areas + Total
- [ ] No rhythm rows or charter fields above this line

```
GATE 2 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 3 requires org diagram with typed nodes.

---

### GATE 3 -- GOVERNANCE DOCUMENTATION

**Prerequisite:** org diagram with typed nodes from GATE 2; typed role list from GATE 0
**Produces:** complete governance artifact

GATE 3 DO/DO NOT:
- DO: Interleave rhythm rows and charters -- each governance row immediately followed by charter.
- DO: Verify pair count after all pairs written.
- DO NOT: Batch rhythm first, charters second.
- DO NOT: Reference a role not in ROLES-LOADED in charter Membership.
- DO NOT: Quorum without `N of M member roles` fraction form.
- DO NOT: Membership without `(TYPE)` annotation on each role.

GATE 3 PROHIBITED CONTENT (C-30) -- MUST NOT appear before STATUS:
- Appendices, supplementary sections, editorial commentary after Anti-Pattern Watch,
  additional unpaired charters, content outside Steps 3.1--3.5.
Terminal-gate position does not exempt GATE 3 from this contract.

**Step 3.1 -- Operating Rhythm and Charters (Interleaved)**

>= 3 distinct cadences (ROB, shiproom/gate, governance). No merged rows.

Inline example rhythm row:

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|
| Architecture Board | Monthly | Principal Engineer | Review and approve cross-cutting design decisions affecting two or more service areas |

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

Charter template:
```
### [Committee Name]
**Mission:** [one sentence]
**Membership:** [Role A (TYPE)], [Role B (TYPE)]
**Quorum:** [N] of [M] member roles
**Escalates:** [named destination]
```

REQUIRED: Membership >= 2 roles with `(TYPE)` from {DECISION, EXECUTION, ADVISORY, GOVERNANCE}.
Quorum MUST use `N of M member roles` form. Percentage, prose quorum, or absence is not acceptable.

**Step 3.2 -- Pair-Count Verification (C-19)**

Governance ORT rows: [N]. Charters produced: [N]. MUST match. DO NOT advance to Step 3.3 until match.

**Step 3.3 -- ORG-ELEMENT REGISTER** (all four categories cat-1 through cat-4 populated)

**Step 3.4 -- Org Evolution Roadmap** (>= 2 rows, distinct triggers; Row 1: headcount threshold)

Inline example row:

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| Headcount exceeds 15 engineers | Split Platform area into Core and Extensions; add Area Lead role | headcount-threshold |

**Step 3.5 -- Anti-Pattern Watch** (>= 2 rows, typed citations `[element name] (cat-N)`)

**CHECKPOINT-3 (C-29/C-34 -- all-gate blocking + cross-gate role continuity)**

Before emitting GATE 3 STATUS, verify all checkboxes:
- [ ] Operating Rhythm Table has >= 3 distinct rows (ROB, shiproom/gate, governance)
- [ ] Pair count verified: governance rows in ORT == charter count produced
- [ ] Each charter has all 5 fields: Name (header), Mission, Membership, Quorum, Escalates
- [ ] Quorum in `N of M member roles` form for all charters
- [ ] Membership >= 2 roles with `(TYPE)` annotation for all charters
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
- [ ] Charters complete (5 fields, Quorum fraction, Membership typed)
- [ ] Pair count verified
- [ ] ROLE-CONTINUITY check passed -- all Membership names present in GATE 0
- [ ] ORG-ELEMENT REGISTER populated
- [ ] Org Evolution Roadmap >= 2 distinct triggers
- [ ] Anti-Pattern Watch with typed citations
- [ ] GATE 3 prohibited-content contract satisfied
- [ ] CHECKPOINT-3 cleared

```
GATE 3 STATUS: [PASS / FAIL]
```

STOP -- ARTIFACT COMPLETE. No additional content, sections, appendices, or commentary
follows this line. (C-31 -- successful-completion path terminal seal)

---

## V-03 -- Dedicated CHARTER-FORMAT-AUDIT Loop (C-33 alternate implementation)

**Axis:** output format -- replace inline CHECKPOINT-3 format items with a dedicated
CHARTER-FORMAT-AUDIT block placed between Step 3.5 and CHECKPOINT-3; the audit block
iterates over each charter individually with explicit REJECT conditions; CHECKPOINT-3
references the completed audit rather than repeating the format checks.
**Hypothesis:** V-01 strengthens CHECKPOINT-3 items 4-5 inline. V-03 tests whether
extracting those checks into a dedicated, structurally distinct block -- with a per-charter
iteration loop, explicit REJECT condition labels, and a DO NOT advance directive -- provides
a stronger C-33 signal. A per-charter loop ("For each committee charter produced...") makes
the "every produced charter" requirement explicit in the instruction text rather than implied
by "for all charters" in a list item. The dedicated block also places the audit as a separate
mandatory step before the checkbox phase, matching the pattern of CHECKPOINT-0's expansion
over GATE 0 STATUS. C-34 remains open.

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
- DO: Read `.roles/` before writing any content.
- DO: List every discovered role in ROLES-LOADED.
- DO NOT: Write any content outside the roles block and classification block before GATE 0 STATUS.
- DO NOT: Introduce a role name in any downstream section that does not appear in this block.

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
ROLES-NOTE: No .roles/ files found. Using inferred roles:
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

(Same as V-01 GATE 1 content -- steps 1.0 through 1.4, flat-verdict branch,
CHECKPOINT INERTIA-CHECK, GATE 1 STATUS, named handoff to GATE 2.)

**Prerequisite:** typed role list from GATE 0
**Produces:** inertia verdict + FLAT-CASE-PRESSURE rating

GATE 1 DO/DO NOT:
- DO: Write default-position statement as Step 1.0 before mechanism rows.
- DO: Four sub-sections in sequence.
- DO NOT: Org diagram or headcount before GATE 1 STATUS.
- DO NOT: FLAT-CASE-PRESSURE outside {LOW, MEDIUM, HIGH}.
- DO NOT: "Revisit as the team grows."

GATE 1 PROHIBITED CONTENT: ASCII org nodes, headcount rows, rhythm rows, charter fields.

**Step 1.0 -- Default-Position Statement (C-28)**

> DEFAULT POSITION: The team can operate flat; structure must earn its place.

**Step 1.1 -- Case for Staying Flat** (mechanism table >= 2 rows, Types from {CADENCE, CHANNEL, INFORMAL-LEAD, ARTIFACT})

Inline example row:

| Type | Mechanism | Current Evidence |
|------|-----------|-----------------|
| CADENCE | Weekly cross-area standup | Resolves sprint-level dependencies across two areas without escalation -- no blocked decision in the last quarter |

Two-step separator: count, verify >= 2, emit:
```
--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. FLAT-CASE-PRESSURE: [LOW|MEDIUM|HIGH]. How We Coordinate Today begins.] ---
```
ENFORCEMENT GUARD: DO NOT EMIT separator before row count >= 2. Two-site enforcement.

**Steps 1.2--1.4:** How We Coordinate Today / Rebuttal / VERDICT + concrete trigger.

Flat-verdict branch:
```
[ABSENT: ASCII Org Diagram] -- flat verdict. No simplified alternative acceptable.
[ABSENT: Headcount by Area] -- flat verdict.
[ABSENT: Operating Rhythm Table] -- flat verdict.
[ABSENT: Committee Charters] -- flat verdict.
[ABSENT: ORG-ELEMENT REGISTER] -- flat verdict.
[ABSENT: Org Evolution Roadmap] -- flat verdict.
[ABSENT: Anti-Pattern Watch] -- flat verdict.
STOP -- ARTIFACT COMPLETE. No content follows this directive.
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

---

### GATE 2 -- STRUCTURAL ARTIFACT GENERATION

**Prerequisite:** inertia verdict + FLAT-CASE-PRESSURE from GATE 1
**Produces:** org diagram with typed nodes

GATE 2 DO/DO NOT:
- DO: ASCII hierarchy from ROLES-LOADED only. Split Decides/Escalates.
- DO NOT: New roles. DO NOT: Merged decision column.

GATE 2 PROHIBITED CONTENT: rhythm rows, charter fields.

**Step 2.1 -- ASCII Org Diagram** (>= 2 levels, committees as distinct nodes)

**Step 2.2 -- Headcount by Area** (5 columns, Key Roles with `(domain type)`, >= 2 areas + Total)

Inline example row:

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| Platform Engineering | 6 | Principal Engineer (DECISION) | API versioning policy, breaking-change gates | Cross-product dependency resolution --> Architecture Board |

**CHECKPOINT DIAGRAM-CHECK (C-22)**

- [ ] Diagram >= 2 levels, roles from ROLES-LOADED, committees distinct
- [ ] 5-column headcount, Decides/Escalates split, >= 2 areas + Total
- [ ] No rhythm rows or charter fields above this line

```
GATE 2 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 3 requires org diagram with typed nodes.

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
Terminal-gate position does not exempt GATE 3 from this contract.

**Step 3.1 -- Operating Rhythm and Charters (Interleaved)**

>= 3 distinct cadences. No merged rows.

Inline example rhythm row:

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|
| Architecture Board | Monthly | Principal Engineer | Review and approve cross-cutting design decisions affecting two or more service areas |

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

Charter template:
```
### [Committee Name]
**Mission:** [one sentence]
**Membership:** [Role A (TYPE)], [Role B (TYPE)]
**Quorum:** [N] of [M] member roles
**Escalates:** [named destination]
```

REQUIRED: Membership >= 2 roles with `(TYPE)` from {DECISION, EXECUTION, ADVISORY, GOVERNANCE}.
Quorum MUST use `N of M member roles`. Percentage, prose quorum, absence: not acceptable.

**Step 3.2 -- Pair-Count Verification** (ORT rows == charter count; DO NOT advance until match)

**Step 3.3 -- ORG-ELEMENT REGISTER** (all four categories populated before Step 3.4)

**Step 3.4 -- Org Evolution Roadmap** (>= 2 rows, distinct triggers; Row 1: headcount threshold)

Inline example row:

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| Headcount exceeds 15 engineers | Split Platform area into Core and Extensions; add Area Lead role | headcount-threshold |

**Step 3.5 -- Anti-Pattern Watch** (>= 2 rows, `[element name] (cat-N) -- [one sentence]`)

**CHARTER-FORMAT-AUDIT (C-33 -- per-charter field-level compliance)**

DO NOT advance to CHECKPOINT-3 until this audit loop has been completed for every
charter produced in Step 3.1.

For each committee charter produced, complete this field audit in sequence:

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

**CHECKPOINT-3 (C-29 -- all-gate blocking, references CHARTER-FORMAT-AUDIT)**

Before emitting GATE 3 STATUS, verify all checkboxes:
- [ ] Operating Rhythm Table has >= 3 distinct rows (ROB, shiproom/gate, governance)
- [ ] Pair count verified: governance rows in ORT == charter count produced
- [ ] Each charter has all 5 fields: Name (header), Mission, Membership, Quorum, Escalates
- [ ] CHARTER-FORMAT-AUDIT completed -- all charters passed Quorum fraction-pattern check
  and Membership closed-set TYPE check (see CHARTER-FORMAT-AUDIT block above)
- [ ] ORG-ELEMENT REGISTER has all four categories (cat-1 through cat-4) populated
- [ ] Org Evolution Roadmap has >= 2 rows with distinct trigger categories
- [ ] Anti-Pattern Watch has >= 2 rows with typed citations from register
- [ ] No prohibited content from GATE 3 contract appears above this line

All checkboxes MUST be ticked before GATE 3 STATUS can read PASS.

GATE 3 STATUS:
- [ ] Operating rhythm >= 3 distinct rows
- [ ] Charters complete (5 fields; CHARTER-FORMAT-AUDIT passed)
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

## V-04 -- Combined: FORMAT-VERIFY Items + Role Continuity (C-33 V-01 + C-34 V-02)

**Axis:** combined -- V-01's explicit FORMAT-VERIFY items for Quorum and Membership TYPE
in CHECKPOINT-3 + V-02's ROLE-CONTINUITY lookup item in CHECKPOINT-3.
**Hypothesis:** C-33 and C-34 are independent checkpoint additions within GATE 3.
C-33 governs what the checkpoint inspects within each charter (format compliance).
C-34 governs cross-gate lookup against the GATE 0 role list (referential integrity).
Neither check depends on the other: a charter can have correct format but introduce an
undeclared role (C-33 PASS, C-34 FAIL); a charter can reference a declared role but
express Quorum as a ratio (C-33 FAIL, C-34 PASS). Combination in a single CHECKPOINT-3
closes both axes simultaneously without interference. V-03's dedicated loop structure
is not used in V-04; the FORMAT-VERIFY items remain as inline checkbox items.
Predicted: C-33 PASS, C-34 PASS. All prior criteria preserved from R9-V-05.

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
- DO: Read `.roles/` before writing any content.
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
ROLES-NOTE: No .roles/ files found. Using inferred roles:
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

MUST NOT proceed past this block until every role from Step 0.1 is typed.

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
- DO NOT: "Revisit as the team grows" as trigger.

GATE 1 PROHIBITED CONTENT: ASCII org nodes, headcount rows, rhythm rows, charter fields.

**Step 1.0 -- Default-Position Statement (C-28)**

> DEFAULT POSITION: The team can operate flat; structure must earn its place.

**Step 1.1 -- Case for Staying Flat** (mechanism table >= 2 rows)

Inline example row:

| Type | Mechanism | Current Evidence |
|------|-----------|-----------------|
| CADENCE | Weekly cross-area standup | Resolves sprint-level dependencies across two areas without escalation -- no blocked decision in the last quarter |

Two-step separator: count rows, verify >= 2, emit:
```
--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. FLAT-CASE-PRESSURE: [LOW|MEDIUM|HIGH]. How We Coordinate Today begins.] ---
```
ENFORCEMENT GUARD: DO NOT EMIT separator before row count >= 2. Two-site enforcement.

**Steps 1.2--1.4:** How We Coordinate Today / Rebuttal / VERDICT + concrete trigger.

Flat-verdict branch:
```
[ABSENT: ASCII Org Diagram] -- flat verdict. No simplified alternative acceptable.
[ABSENT: Headcount by Area] -- flat verdict.
[ABSENT: Operating Rhythm Table] -- flat verdict.
[ABSENT: Committee Charters] -- flat verdict.
[ABSENT: ORG-ELEMENT REGISTER] -- flat verdict.
[ABSENT: Org Evolution Roadmap] -- flat verdict.
[ABSENT: Anti-Pattern Watch] -- flat verdict.
STOP -- ARTIFACT COMPLETE. No content follows this directive.
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

---

### GATE 2 -- STRUCTURAL ARTIFACT GENERATION

**Prerequisite:** inertia verdict + FLAT-CASE-PRESSURE from GATE 1
**Produces:** org diagram with typed nodes

GATE 2 DO/DO NOT:
- DO: ASCII hierarchy from ROLES-LOADED only. Split Decides/Escalates.
- DO NOT: New roles. DO NOT: Merged decision column.

GATE 2 PROHIBITED CONTENT: rhythm rows, charter fields.

**Step 2.1 -- ASCII Org Diagram** (>= 2 levels, committees as distinct nodes)

**Step 2.2 -- Headcount by Area**

Inline example row:

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| Platform Engineering | 6 | Principal Engineer (DECISION) | API versioning policy, breaking-change gates | Cross-product dependency resolution --> Architecture Board |

Minimum two area rows + Total row.

**CHECKPOINT DIAGRAM-CHECK (C-22)**

- [ ] Diagram >= 2 levels, roles from ROLES-LOADED, committees distinct
- [ ] 5-column headcount, Decides/Escalates split, >= 2 areas + Total
- [ ] No rhythm rows or charter fields above this line

```
GATE 2 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 3 requires org diagram with typed nodes.

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

GATE 3 PROHIBITED CONTENT (C-30): Appendices, supplementary sections, editorial commentary
after Anti-Pattern Watch, unpaired charters, content outside Steps 3.1--3.5.
Terminal-gate position does not exempt GATE 3 from this contract.

**Step 3.1 -- Operating Rhythm and Charters (Interleaved)**

>= 3 distinct cadences. No merged rows.

Inline example rhythm row:

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|
| Architecture Board | Monthly | Principal Engineer | Review and approve cross-cutting design decisions affecting two or more service areas |

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

Charter template:
```
### [Committee Name]
**Mission:** [one sentence]
**Membership:** [Role A (TYPE)], [Role B (TYPE)]
**Quorum:** [N] of [M] member roles
**Escalates:** [named destination]
```

REQUIRED: Membership >= 2 roles with `(TYPE)` from {DECISION, EXECUTION, ADVISORY, GOVERNANCE}.
Quorum MUST use `N of M member roles`. Percentage, prose quorum, absence: not acceptable.

**Step 3.2 -- Pair-Count Verification** (ORT rows == charter count; DO NOT advance until match)

**Step 3.3 -- ORG-ELEMENT REGISTER** (all four categories populated)

**Step 3.4 -- Org Evolution Roadmap** (>= 2 rows, distinct triggers)

Inline example row:

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| Headcount exceeds 15 engineers | Split Platform area into Core and Extensions; add Area Lead role | headcount-threshold |

**Step 3.5 -- Anti-Pattern Watch** (>= 2 rows, `[element name] (cat-N) -- [one sentence]`)

**CHECKPOINT-3 (C-29/C-33/C-34 -- all-gate blocking + format verification + role continuity)**

Before emitting GATE 3 STATUS, verify all checkboxes:
- [ ] Operating Rhythm Table has >= 3 distinct rows (ROB, shiproom/gate, governance)
- [ ] Pair count verified: governance rows in ORT == charter count produced
- [ ] Each charter has all 5 fields: Name (header), Mission, Membership, Quorum, Escalates
- [ ] FORMAT-VERIFY QUORUM: For each charter produced -- Quorum field value is in the
  form `[integer] of [integer] member roles`; fractional notation ("3/5"), percentage
  ("60%"), prose quorum ("majority of members"), or bare number are NOT acceptable
- [ ] FORMAT-VERIFY MEMBERSHIP TYPE: For each charter produced -- every Membership role
  entry carries `(TYPE)` where TYPE is exactly one value from {DECISION, EXECUTION,
  ADVISORY, GOVERNANCE}; unannotated entries or values outside this closed set do not
  satisfy this check
- [ ] ROLE-CONTINUITY: For each role name in any charter Membership field -- verify the
  role name appears in the GATE 0 ROLES-LOADED or ROLES-NOTE list. If any Membership
  role name is absent from GATE 0: CHECKPOINT-3 FAILS. Remediation: add the undeclared
  role to GATE 0 and re-emit GATE 0 STATUS before GATE 3 STATUS can emit.
- [ ] ORG-ELEMENT REGISTER has all four categories (cat-1 through cat-4) populated
- [ ] Org Evolution Roadmap has >= 2 rows with distinct trigger categories
- [ ] Anti-Pattern Watch has >= 2 rows with typed citations from register
- [ ] No prohibited content from GATE 3 contract appears above this line

All checkboxes MUST be ticked before GATE 3 STATUS can read PASS.

GATE 3 STATUS:
- [ ] Operating rhythm >= 3 distinct rows
- [ ] Charters complete (5 fields; FORMAT-VERIFY QUORUM passed; FORMAT-VERIFY MEMBERSHIP TYPE passed)
- [ ] Pair count verified
- [ ] ROLE-CONTINUITY passed -- all Membership names present in GATE 0
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

## V-05 -- Full Integration: CHARTER-FORMAT-AUDIT + Role Continuity (C-33 V-03 + C-34 V-02)

**Axis:** full integration -- V-03's dedicated CHARTER-FORMAT-AUDIT loop (C-33) +
V-02's ROLE-CONTINUITY lookup item (C-34) on the complete R9-V-05 baseline.
**Hypothesis:** V-03's dedicated audit block and V-02's ROLE-CONTINUITY item are
structurally independent: the CHARTER-FORMAT-AUDIT executes before CHECKPOINT-3
and inspects format compliance within each charter; the ROLE-CONTINUITY step executes
within CHECKPOINT-3 and inspects cross-gate name continuity. The CHARTER-FORMAT-AUDIT
block's "re-run from first charter" directive and the ROLE-CONTINUITY FAIL directive
are distinct gating mechanisms with no shared state. Combining them produces the
strongest C-33 enforcement (dedicated loop with REJECT conditions, DO NOT advance
guard, and re-run directive) with the strongest C-34 enforcement (named lookup
authority, named FAIL directive, named remediation path). Predicted: C-33 PASS,
C-34 PASS, all prior criteria preserved. Full v10 coverage.

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
- DO: Read `.roles/` before writing any content.
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

Check `.roles/` for existing role definitions.

```
ROLES-LOADED:
  - [role name] -- [one-line description from role file]
  - [role name] -- [one-line description from role file]
```

If no role files found:
```
ROLES-NOTE: No .roles/ files found. Using inferred roles:
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
- [ ] Re-assessment trigger is concrete
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
- [ ] Committees appear as distinct nodes
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

**Charter format -- 5 fields required (C-05 / C-32 -- complete example)**

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
  ("majority"), or missing Quorum field is not acceptable. See filled example above.

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

All four categories MUST be populated before advancing to Step 3.4.

**Step 3.4 -- Org Evolution Roadmap**

At minimum two rows, distinct trigger categories. Row 1 MUST be a headcount threshold.
Row 2 MUST be from a different category (workload signal, structural symptom, milestone).

Inline example row (complete, not a label):

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| Headcount exceeds 15 engineers | Split Platform area into Core and Extensions sub-areas; add Area Lead role | headcount-threshold |

**Step 3.5 -- Anti-Pattern Watch**

At minimum two rows. Each "Why It Applies Here" cell MUST open with:
`[element name] (cat-N) -- [one sentence]`

Element names copied exactly from ORG-ELEMENT REGISTER.
DO NOT use a cat-N code not in the register schema.

**CHARTER-FORMAT-AUDIT (C-33 -- per-charter field-level compliance)**

DO NOT advance to CHECKPOINT-3 until this audit loop has been completed for every
charter produced in Step 3.1.

For each committee charter produced, complete this field audit in sequence:

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

If any charter fails any check above: STOP. Correct the failing charter. Re-run the full
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
- [ ] Charters complete (5 fields; CHARTER-FORMAT-AUDIT passed; ROLE-CONTINUITY passed)
- [ ] Pair count verified
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
