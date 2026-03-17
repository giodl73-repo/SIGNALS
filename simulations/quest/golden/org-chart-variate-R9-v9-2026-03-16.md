---
skill: quest-variate
skill_target: org-chart
date: 2026-03-16
round: R9
rubric_version: v9
status: variate
---

# org-chart Variate — Round 9 (Rubric v9)

**Date:** 2026-03-16
**Skill:** org-chart
**Rubric:** v9 (C-01 through C-32; C-29/C-30/C-31/C-32 new from R8 signals)
**Round:** R9 of C-track — single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

## R8 ceiling and R9 target

The v9 rubric identifies four gaps in the best R8 variation, each a distinct bypass:

1. **All-gate blocking gap (C-29):** Blocking verification existed at GATE 1 and GATE 2
   (satisfying C-22 "a mandatory step") but GATE 0 and GATE 3 emit STATUS without any
   preceding verification hold. C-29 requires all-gate coverage.

2. **GATE 3 prohibited-content gap (C-30):** Prohibited-content contracts at GATE 0, GATE 1,
   and GATE 2 (C-26 PARTIAL) but GATE 3 carries a bare STATUS line. Terminal-gate
   rationalization ("no downstream gate to receive leaked content") is the bypass C-30 closes.

3. **Successful-completion exit gap (C-31):** Flat-verdict exit sealed with "STOP — ARTIFACT
   COMPLETE" (C-18 pass), but GATE 3 STATUS has no analogous seal on the full-artifact path.
   Content can be appended after GATE 3 STATUS without prohibition.

4. **Charter example gap (C-32):** Complete inline example rows for mechanism table,
   operating rhythm table, and headcount table, but the charter section shows only field
   labels (Name:, Mission:, Membership:, Quorum:, Escalates:) without a filled example.
   C-11 earns PARTIAL (3/4 tables); C-32 requires the filled charter instance.

**R9 target:** Close all four gaps. V-01/V-02/V-03 single-axis; V-04 combines V-01+V-02;
V-05 combines all four.

---

## Round 9 Variation Map

| V | Axis | What Changes vs v8 best | Hypothesis |
|---|------|-------------------------|------------|
| V-01 | Lifecycle emphasis (all-gate blocking) | Add CHECKPOINT-0 (between GATE 0 classification step and GATE 0 STATUS) and CHECKPOINT-3 (between Anti-Pattern Watch and GATE 3 STATUS). GATE 1/GATE 2 checkpoints preserved unchanged. | C-29 requires a blocking step at every gate. GATE 0 and GATE 3 are the two unguarded gates. Adding two checkpoints closes the coverage gap without touching other criteria. C-29 PASS predicted; C-30/C-31/C-32 open. |
| V-02 | Lifecycle emphasis (GATE 3 dual-boundary) | Add GATE 3 PROHIBITED CONTENT contract naming categories that MUST NOT appear before GATE 3 STATUS; add post-STATUS terminal seal directive immediately after GATE 3 STATUS. | C-30 (intra-GATE 3 guard before STATUS) and C-31 (post-STATUS seal on successful-completion exit) are complementary boundary conditions on GATE 3 — C-30 guards content within GATE 3, C-31 guards content after STATUS. Both additions are isolated to GATE 3. C-29/C-32 open. |
| V-03 | Output format (complete charter example) | Replace 5-field charter field-label template with a concrete filled example charter: Name (committee name), Mission (one sentence), Membership with (TYPE) annotations, Quorum as N of M fraction, Escalates naming a concrete destination. | C-32 requires a filled charter example, not labels. C-11 upgrades from PARTIAL (3/4) to PASS (4/4). Change isolated to charter section; all gate structure unchanged. C-29/C-30/C-31 open. |
| V-04 | Combined: all-gate blocking + GATE 3 dual-boundary | V-01 + V-02 applied together: CHECKPOINT-0, CHECKPOINT-3, GATE 3 prohibited-content contract, post-STATUS terminal seal. | C-29, C-30, C-31 are independent structural additions with no cross-criterion interference. Combination closes three gaps. C-32 open. Predicted: C-29/C-30/C-31 PASS. |
| V-05 | Full combination (all four v9 criteria) | V-01 + V-02 + V-03: all four gaps closed. | V-04 closes C-29/C-30/C-31. V-03 closes C-32 independently. Complete combination predicted C-01 through C-32 (32/32). |

---

## V-01 — Lifecycle Emphasis: All-Gate Blocking Verification

**axis:** lifecycle emphasis — add dedicated intermediate verification checkpoints at GATE 0
and GATE 3; GATE 1 CHECKPOINT INERTIA-CHECK and GATE 2 CHECKPOINT DIAGRAM-CHECK preserved
unchanged from v8 baseline
**hypothesis:** C-29 requires every gate to carry a blocking verification step between its
last production step and its STATUS emission. V-01/R8 left GATE 0 and GATE 3 unguarded
while GATE 1 and GATE 2 had checkpoints, satisfying C-22 ("a mandatory step") but not C-29
("every gate"). Adding CHECKPOINT-0 and CHECKPOINT-3 closes the coverage gap. No other
structural change. C-29 PASS predicted. C-30/C-31/C-32 remain open in this variation.

---

You are running `/org-chart {topic}`.

---

GATE CHAIN CONTRACT

Gates are numbered GATE 0, GATE 1, GATE 2, GATE 3. Each gate's outputs are required inputs
for the subsequent gate. Gates MUST be emitted in strictly ascending numeric order. The
sequence constraint is provable from the gate labels themselves without reading surrounding
prose.

---

### GATE 0 — ROLES AND CLASSIFICATION

**Prerequisite:** none
**Produces:** typed role list

GATE 0 DO/DO NOT:
- DO: Read `.craft/roles/` before writing any content.
- DO: List every discovered role in ROLES-LOADED.
- DO NOT: Write any content outside the roles block and classification block before GATE 0 STATUS.
- DO NOT: Introduce a role name in any downstream section that does not appear in this block.

GATE 0 CONTAINMENT CONTRACT — the following content types MUST NOT appear within GATE 0
before STATUS is emitted:
- Inertia assessment rows or sub-sections
- Org diagram nodes or ASCII hierarchy
- Headcount area entries
- Operating rhythm rows
- Committee charter fields

**Step 0.1 — Load Roles**

Check `.craft/roles/` for existing role definitions.

```
ROLES-LOADED:
  - [role name] — [one-line description from role file]
  - [role name] — [one-line description from role file]
```

If no role files found:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] — [description]
  - [role name] — [description]
```

**Step 0.2 — Role-Type Classification**

Immediately after the roles block — no structural content may appear between Step 0.1
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

**CHECKPOINT-0 (C-29 — all-gate blocking verification)**

Before emitting GATE 0 STATUS, verify all items:
- [ ] ROLES-LOADED or ROLES-NOTE block is present and lists all roles
- [ ] ROLE-TYPE-CLASSIFICATION assigns every role a type from the closed set {DECISION, EXECUTION, ADVISORY, GOVERNANCE}
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

### GATE 1 — INERTIA ASSESSMENT

**Prerequisite:** typed role list from GATE 0
**Produces:** inertia verdict + FLAT-CASE-PRESSURE rating

GATE 1 DO/DO NOT:
- DO: Write the default-position statement as the first executable step (Step 1.0).
- DO: Present all four sub-sections in sequence.
- DO NOT: Write an org diagram node or headcount entry before GATE 1 STATUS.
- DO NOT: Use "the team is growing" as a rebuttal without naming the failure mode.
- DO NOT: Use a FLAT-CASE-PRESSURE rating outside the closed set {LOW, MEDIUM, HIGH}.

GATE 1 PROHIBITED CONTENT — the following MUST NOT appear within GATE 1 before STATUS:
- ASCII org diagram nodes or hierarchy lines
- Headcount area rows
- Operating rhythm cadence rows
- Committee charter fields (Mission, Membership, Quorum, Escalates)

**Step 1.0 — Default-Position Statement (C-28 step embed)**

Write the following statement as the first line of GATE 1, before any mechanism rows:

> DEFAULT POSITION: The team can operate flat; structure must earn its place.

This is an executable step. It MUST be encountered during execution of GATE 1, not only
visible in a preamble. It MUST precede the mechanism table.

**Step 1.1 — Case for Staying Flat**

Present a mechanism table with Type from the closed set {CADENCE, CHANNEL, INFORMAL-LEAD,
ARTIFACT}. Produce at least two rows before the separator.

Inline example row (complete, not a label):

| Type | Mechanism | Current Evidence |
|------|-----------|-----------------|
| CADENCE | Weekly cross-area standup | Resolves sprint-level dependencies across two areas without escalation — no blocked decision in the last quarter |

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

**ENFORCEMENT — GUARD:** DO NOT EMIT the separator before row count >= 2.
DO NOT begin Step 1.2 until the separator appears in output.
Two-site: if Sub-section 1.2 prose appears, the FLAT-CASE-CLOSED separator MUST immediately
precede it — Sub-section 1.2 content before the separator is not acceptable.

**Step 1.2 — How We Coordinate Today**

Inventory current coordination patterns: channels, cadences, informal roles, artifacts.
Add frequency and participants. DO NOT re-list mechanism rows from Step 1.1.

```
### How We Coordinate Today
[Catalog: named meetings, shared artifacts, escalation paths, informal roles with frequency and participants]
```

**Step 1.3 — Rebuttal**

Name the coordination failure the flat case cannot answer. Reference a specific observable:
blocked decision, missed SLA, time-zone gap, knowledge silo, competing roadmap.

```
### Rebuttal
[Named failure mode specific to this team and topic]
```

**Step 1.4 — VERDICT and Re-assessment Trigger**

Choose exactly one: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED. Reasoning sentence connecting
sub-sections 1.1, 1.2, 1.3 to the verdict. Concrete re-assessment trigger immediately after.

```
### VERDICT

[CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]

Reasoning: [specific — connecting all three sub-sections]

Re-assessment trigger: [concrete condition — e.g., "when headcount exceeds 12" or
"when on-call rotation spans more than two distinct service areas"]
```

DO NOT use "revisit as the team grows" — the trigger MUST name a concrete threshold.

Flat-verdict branch — if CAN-OPERATE-FLAT:
```
[ABSENT: ASCII Org Diagram] — flat verdict. "Simplified" or "compact" alternatives are
not acceptable substitutes for this ABSENT label.

[ABSENT: Headcount by Area] — flat verdict.
[ABSENT: Operating Rhythm Table] — flat verdict.
[ABSENT: Committee Charters] — flat verdict.
[ABSENT: ORG-ELEMENT REGISTER] — flat verdict.
[ABSENT: Org Evolution Roadmap] — flat verdict.
[ABSENT: Anti-Pattern Watch] — flat verdict.

STOP — ARTIFACT COMPLETE. No content follows this directive.
```

**CHECKPOINT INERTIA-CHECK (C-22 — blocking verification)**

Before emitting GATE 1 STATUS, verify all checkboxes:
- [ ] Default-position statement precedes mechanism table
- [ ] Case for Staying Flat has >= 2 mechanism rows with Types from closed set
- [ ] FLAT-CASE-PRESSURE is from {LOW, MEDIUM, HIGH}
- [ ] VERDICT is from {CAN-OPERATE-FLAT, STRUCTURE-WARRANTED} with reasoning sentence
- [ ] Re-assessment trigger is concrete (not "revisit as the team grows")
- [ ] No prohibited content from GATE 1 contract appears above this line

GATE 1 STATUS:
- [ ] Default-position statement present before mechanism table
- [ ] All 4 sub-sections written
- [ ] FLAT-CASE-PRESSURE from closed set
- [ ] VERDICT from closed set with reasoning
- [ ] Concrete re-assessment trigger

```
GATE 1 STATUS: [PASS / FAIL]
```

If FAIL: DO NOT advance to GATE 2.

**Named artifact handoff:** GATE 2 requires inertia verdict + FLAT-CASE-PRESSURE rating.
If GATE 1 STATUS is FAIL, GATE 2 MUST NOT begin.

---

### GATE 2 — STRUCTURAL ARTIFACT GENERATION

**Prerequisite:** inertia verdict + FLAT-CASE-PRESSURE rating from GATE 1
**Produces:** org diagram with typed nodes

GATE 2 DO/DO NOT:
- DO: Draw ASCII hierarchy using only role names from ROLES-LOADED.
- DO: Use split Decides/Escalates columns — separate, not merged.
- DO NOT: Introduce any role name not in GATE 0's typed role list.
- DO NOT: Use a single "Decision Scope" column.

GATE 2 PROHIBITED CONTENT — MUST NOT appear within GATE 2 before STATUS:
- Operating rhythm cadence rows
- Committee charter fields

**Step 2.1 — ASCII Org Diagram**

Draw an ASCII hierarchy with at minimum two levels. Committees appear as distinct labeled
nodes, not embedded within an area box. All role names MUST come from ROLES-LOADED.

**Step 2.2 — Headcount by Area**

Five columns: Area, Headcount, Key Roles, Decides, Escalates. Key Roles annotated with
`(domain type)`. Decides and Escalates are separate columns.

Inline example row (complete, not a label):

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| Platform Engineering | 6 | Principal Engineer (DECISION) | API versioning policy, breaking-change gates | Cross-product dependency resolution → Architecture Board |

```
| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| [name] | [N or N-M] | [role (domain type)] | [decision types owned] | [decisions escalated — named destination] |
| [name] | [N or N-M] | [role (domain type)] | [decision types owned] | [decisions escalated — named destination] |
| **Total** | **[N]** | | | |
```

MUST include at minimum two area rows with individual counts and a Total row.

**CHECKPOINT DIAGRAM-CHECK (C-22 — blocking verification)**

Before emitting GATE 2 STATUS, verify all checkboxes:
- [ ] ASCII diagram shows >= 2 hierarchy levels
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

```
GATE 2 STATUS: [PASS / FAIL]
```

If FAIL: DO NOT advance to GATE 3.

**Named artifact handoff:** GATE 3 requires org diagram with typed nodes.
If GATE 2 STATUS is FAIL, GATE 3 MUST NOT begin.

---

### GATE 3 — GOVERNANCE DOCUMENTATION

**Prerequisite:** org diagram with typed nodes from GATE 2
**Produces:** complete governance artifact

GATE 3 DO/DO NOT:
- DO: Produce operating rhythm rows and committee charters in interleaved pairs.
- DO: Verify pair count equals governance row count after all pairs are written.
- DO NOT: Batch all rhythm rows first and all charters second.
- DO NOT: Reference a role not in ROLES-LOADED in a charter Membership field.
- DO NOT: Write a Quorum field without `N of M member roles` fraction form.
- DO NOT: Write Membership without `(TYPE)` annotation on each role.

**Step 3.1 — Operating Rhythm and Charters (Interleaved)**

Operating rhythm covers at minimum three distinct cadences: the ROB, a shiproom or ship
gate, and a governance meeting. No two cadences share a row.

Inline example row for operating rhythm (complete, not a label):

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|
| Architecture Board | Monthly | Principal Engineer | Review and approve cross-cutting design decisions affecting two or more service areas |

For each governance cadence row, immediately produce its charter. DO NOT batch governance
charters after all rhythm rows are written.

Charter format — 5 fields required:
```
### [Committee Name]

**Mission:** [one sentence — what this committee decides or governs]
**Membership:** [Role A (TYPE)], [Role B (TYPE)]
**Quorum:** [N] of [M] member roles
**Escalates:** [named destination role or forum]
```

REQUIRED: Membership MUST list >= 2 roles each annotated with `(TYPE)` from
{DECISION, EXECUTION, ADVISORY, GOVERNANCE}. Quorum MUST use `N of M member roles`
fraction form — percentage or prose quorum is not acceptable.

**Step 3.2 — Post-Interleave Pair-Count Verification (C-19)**

After all rhythm-charter pairs are produced:
- Count governance rows in the Operating Rhythm Table: [N]
- Count committee charters produced: [N]
- MUST match. If mismatch: identify the gap, produce missing charter, recount.
  DO NOT advance to Step 3.3 until counts match.

**Step 3.3 — ORG-ELEMENT REGISTER**

MUST produce immediately after Committee Charters. All four category entries MUST be
populated before proceeding to Step 3.4.

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
    - [area name] — headcount: [N]

  cat-2 (Committees/Cadences):
    - [committee or cadence name]

  cat-3 (Headcount):
    - Total headcount: [N]

  cat-4 (DRI Roles):
    - [DRI role name]
```

**Step 3.4 — Org Evolution Roadmap**

At minimum two rows, distinct trigger categories. Row 1 MUST be a headcount threshold.
Row 2 MUST be from a different category (workload signal, structural symptom, or milestone).
Two headcount numbers at different values count as one dimension, not two.

Inline example row (complete, not a label):

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| Headcount exceeds 15 engineers | Split Platform area into Core and Extensions sub-areas; add Area Lead role | headcount-threshold |

```
## Org Evolution Roadmap

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| [headcount threshold] | [Named structural change] | headcount-threshold |
| [workload signal, structural symptom, or milestone] | [Named structural change] | [type] |
```

**Step 3.5 — Anti-Pattern Watch**

At minimum two rows. Each "Why It Applies Here" cell MUST open with typed citation syntax:
`[element name] (cat-N) — [one sentence]`. Element names copied exactly from the
ORG-ELEMENT REGISTER. DO NOT use a cat-N code not in the register schema.

```
## Anti-Pattern Watch

| Anti-Pattern | Why It Applies Here | Mitigation |
|--------------|---------------------|------------|
| [Named anti-pattern] | `[element name] (cat-N) — [one sentence of specific relevance]` | [Mitigation] |
| [Second anti-pattern] | `[element name] (cat-N) — [one sentence]` | [Mitigation] |
```

**CHECKPOINT-3 (C-29 — all-gate blocking verification)**

Before emitting GATE 3 STATUS, verify all checkboxes:
- [ ] Operating Rhythm Table has >= 3 distinct rows (ROB, shiproom/gate, governance)
- [ ] Pair count verified: governance rows in ORT == charter count produced
- [ ] Each charter has all 5 fields: Name (header), Mission, Membership, Quorum, Escalates
- [ ] Quorum in `N of M member roles` form for all charters
- [ ] Membership lists >= 2 roles each with `(TYPE)` annotation
- [ ] ORG-ELEMENT REGISTER has all four categories (cat-1 through cat-4) populated
- [ ] Org Evolution Roadmap has >= 2 rows with distinct trigger categories
- [ ] Anti-Pattern Watch has >= 2 rows with typed citations from register

All checkboxes MUST be ticked before GATE 3 STATUS can read PASS.

GATE 3 STATUS:
- [ ] Operating rhythm >= 3 distinct rows
- [ ] Charters complete (5 fields, Quorum fraction, Membership typed)
- [ ] Pair count verified
- [ ] ORG-ELEMENT REGISTER populated
- [ ] Org Evolution Roadmap >= 2 distinct triggers
- [ ] Anti-Pattern Watch with typed citations
- [ ] CHECKPOINT-3 cleared

```
GATE 3 STATUS: [PASS / FAIL]
```

---

```
Generated by: /org-chart {topic} — {date}
```

---

## V-02 — Lifecycle Emphasis: GATE 3 Dual-Boundary Sealing

**axis:** lifecycle emphasis — add GATE 3 PROHIBITED CONTENT contract (names content
categories that MUST NOT appear within GATE 3 before STATUS) and a post-STATUS terminal
seal directive immediately after GATE 3 STATUS on the successful-completion exit path
**hypothesis:** C-30 requires GATE 3 to carry a prohibited-content list regardless of its
terminal position — the "no downstream gate" rationalization is the bypass C-30 closes.
C-31 requires a STOP directive immediately after GATE 3 STATUS on the full-artifact path,
symmetric to the flat-verdict STOP required by C-18. Both are additions to the GATE 3
boundary only. C-29 remains open (GATE 0 and GATE 3 lack blocking checkpoints). C-32
remains open (charter is field-labels only). Predicted: C-30 PASS, C-31 PASS.

---

You are running `/org-chart {topic}`.

---

GATE CHAIN CONTRACT

Gates GATE 0, GATE 1, GATE 2, GATE 3. Each gate's outputs are required inputs for the
subsequent gate. MUST emit in strictly ascending numeric order. Sequence provable from
gate labels.

---

### GATE 0 — ROLES AND CLASSIFICATION

**Prerequisite:** none
**Produces:** typed role list

GATE 0 DO/DO NOT:
- DO: Read `.craft/roles/` before writing any content.
- DO NOT: Write any content outside the roles and classification blocks before GATE 0 STATUS.
- DO NOT: Introduce role names downstream not declared here.

GATE 0 CONTAINMENT CONTRACT — MUST NOT appear before GATE 0 STATUS:
- Inertia rows, org diagram nodes, headcount entries, rhythm rows, charter fields

**Step 0.1 — Load Roles**

```
ROLES-LOADED:
  - [role name] — [one-line description from role file]
```
or
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] — [description]
```

**Step 0.2 — Role-Type Classification**

Immediately after roles block. Every role MUST be typed from {DECISION, EXECUTION,
ADVISORY, GOVERNANCE}. Three-tier order.

```
ROLE-TYPE-CLASSIFICATION:
  DECISION: [role names]
  EXECUTION: [role names]
  ADVISORY: [role names]
  GOVERNANCE: [role names]
```

GATE 0 STATUS:
- [ ] Roles block present
- [ ] All roles typed from closed set
- [ ] Containment contract satisfied

```
GATE 0 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 1 requires typed role list.

---

### GATE 1 — INERTIA ASSESSMENT

**Prerequisite:** typed role list from GATE 0
**Produces:** inertia verdict + FLAT-CASE-PRESSURE rating

GATE 1 DO/DO NOT:
- DO: Write default-position statement as Step 1.0 before mechanism table.
- DO: Four sub-sections in sequence.
- DO NOT: Write org diagram or headcount content before GATE 1 STATUS.
- DO NOT: Use "revisit as the team grows" as a trigger.

GATE 1 PROHIBITED CONTENT — MUST NOT appear before GATE 1 STATUS:
- ASCII org diagram nodes, headcount area rows, rhythm cadence rows, charter fields

**Step 1.0 — Default-Position Statement (C-28)**

> DEFAULT POSITION: The team can operate flat; structure must earn its place.

MUST appear before any mechanism rows. Executable step, not a scene-setter.

**Step 1.1 — Case for Staying Flat**

Mechanism table, Type from {CADENCE, CHANNEL, INFORMAL-LEAD, ARTIFACT}, >= 2 rows.

Inline example row:

| Type | Mechanism | Current Evidence |
|------|-----------|-----------------|
| CADENCE | Weekly cross-area standup | Resolves sprint-level dependencies across two areas without escalation — no blocked decision in the last quarter |

```
### Case for Staying Flat

| Type | Mechanism | Current Evidence |
|------|-----------|-----------------|
| [type] | [named mechanism] | [observable evidence] |
| [type] | [second mechanism] | [evidence] |
```

Two-step separator protocol: count rows, verify >= 2, emit:
```
--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. FLAT-CASE-PRESSURE: [LOW|MEDIUM|HIGH]. How We Coordinate Today begins.] ---
```

**ENFORCEMENT — GUARD:** DO NOT EMIT separator before row count >= 2.
Two-site: Sub-section 1.2 prose MUST be preceded by the separator. No Sub-section 1.2
content before the separator is acceptable.

**Step 1.2 — How We Coordinate Today** (inventory; no re-listing of mechanism rows)
**Step 1.3 — Rebuttal** (specific failure mode; not "the team is growing")
**Step 1.4 — VERDICT and Re-assessment Trigger** (CAN-OPERATE-FLAT or STRUCTURE-WARRANTED;
concrete trigger)

Flat-verdict branch:
```
[ABSENT: ASCII Org Diagram] — flat verdict. No simplified alternative acceptable.
[ABSENT: Headcount by Area] — flat verdict.
[ABSENT: Operating Rhythm Table] — flat verdict.
[ABSENT: Committee Charters] — flat verdict.
[ABSENT: ORG-ELEMENT REGISTER] — flat verdict.
[ABSENT: Org Evolution Roadmap] — flat verdict.
[ABSENT: Anti-Pattern Watch] — flat verdict.
STOP — ARTIFACT COMPLETE. No content follows this directive.
```

**CHECKPOINT INERTIA-CHECK (C-22)**

Before GATE 1 STATUS:
- [ ] Default-position statement precedes mechanism table
- [ ] >= 2 mechanism rows with Types from closed set
- [ ] FLAT-CASE-PRESSURE from {LOW, MEDIUM, HIGH}
- [ ] VERDICT from {CAN-OPERATE-FLAT, STRUCTURE-WARRANTED} with reasoning
- [ ] Concrete re-assessment trigger
- [ ] No prohibited content above this line

```
GATE 1 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 2 requires inertia verdict + FLAT-CASE-PRESSURE rating.

---

### GATE 2 — STRUCTURAL ARTIFACT GENERATION

**Prerequisite:** inertia verdict + FLAT-CASE-PRESSURE rating from GATE 1
**Produces:** org diagram with typed nodes

GATE 2 DO/DO NOT:
- DO: ASCII hierarchy from roles in ROLES-LOADED only.
- DO: Split Decides/Escalates columns.
- DO NOT: New roles. DO NOT: Merged "Decision Scope" column.

GATE 2 PROHIBITED CONTENT: rhythm rows, charter fields.

**Step 2.1 — ASCII Org Diagram** (>= 2 levels, committees as distinct nodes, roles from ROLES-LOADED)

**Step 2.2 — Headcount by Area** (5 columns, Key Roles with `(domain type)`)

Inline example row:

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| Platform Engineering | 6 | Principal Engineer (DECISION) | API versioning policy, breaking-change gates | Cross-product dependency resolution → Architecture Board |

At minimum two area rows + Total row.

**CHECKPOINT DIAGRAM-CHECK (C-22)**

Before GATE 2 STATUS:
- [ ] Diagram >= 2 levels, roles from ROLES-LOADED, committees distinct
- [ ] 5-column headcount with Decides/Escalates split, >= 2 areas + Total
- [ ] No rhythm rows or charter fields above this line

```
GATE 2 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 3 requires org diagram with typed nodes.

---

### GATE 3 — GOVERNANCE DOCUMENTATION

**Prerequisite:** org diagram with typed nodes from GATE 2
**Produces:** complete governance artifact

GATE 3 DO/DO NOT:
- DO: Interleave rhythm rows and charters — each governance row immediately followed by charter.
- DO: Verify pair count after all pairs are written.
- DO NOT: Batch all rhythm rows first and all charters second.
- DO NOT: Quorum without `N of M member roles` fraction.
- DO NOT: Membership without `(TYPE)` annotations.

**Step 3.1 — Operating Rhythm and Charters (Interleaved)**

Operating rhythm: >= 3 rows (ROB, shiproom/gate, governance). No merged rows.

Inline example rhythm row:

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|
| Architecture Board | Monthly | Principal Engineer | Review and approve cross-cutting design decisions affecting two or more service areas |

Charter format — 5 fields:
```
### [Committee Name]

**Mission:** [one sentence]
**Membership:** [Role A (TYPE)], [Role B (TYPE)]
**Quorum:** [N] of [M] member roles
**Escalates:** [named destination]
```

REQUIRED: Membership >= 2 roles with `(TYPE)`. Quorum in `N of M member roles` form.

**Step 3.2 — Pair-Count Verification (C-19)**

Governance rows in ORT: [N]. Charters produced: [N]. MUST match before advancing.

**Step 3.3 — ORG-ELEMENT REGISTER** (all four categories before proceeding)

```
ORG-ELEMENT REGISTER

  Category schema:
  | cat-N | Category name         | Element type                                          |
  |-------|-----------------------|-------------------------------------------------------|
  | cat-1 | Areas                 | Area names from the Headcount by Area table           |
  | cat-2 | Committees/Cadences   | Committee and cadence names from Rhythm Table/Charters|
  | cat-3 | Headcount             | Total headcount and per-area headcount counts         |
  | cat-4 | DRI Roles             | DRI role names from the Operating Rhythm Table        |

  cat-1 (Areas): - [area name] — headcount: [N]
  cat-2 (Committees/Cadences): - [name]
  cat-3 (Headcount): - Total headcount: [N]
  cat-4 (DRI Roles): - [DRI role]
```

**Step 3.4 — Org Evolution Roadmap** (>= 2 rows, distinct trigger categories)

Inline example row:

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| Headcount exceeds 15 engineers | Split Platform area into Core and Extensions; add Area Lead role | headcount-threshold |

**Step 3.5 — Anti-Pattern Watch** (>= 2 rows, typed citations `[element name] (cat-N)`)

**GATE 3 PROHIBITED CONTENT (C-30 — terminal gate contract)**

The following MUST NOT appear within GATE 3 before STATUS is emitted:
- Appendices of any kind
- Supplementary sections (additional tables, notes, annexes)
- Editorial commentary or rationale paragraphs after the Anti-Pattern Watch table
- Additional committee charters not paired with an operating rhythm row
- Any content category not part of Steps 3.1 through 3.5

This contract applies to GATE 3 regardless of its terminal position. The absence of a
downstream gate does not exempt GATE 3 from a prohibited-content contract. Content that
appears after the Anti-Pattern Watch table and before GATE 3 STATUS is a contract violation.

GATE 3 STATUS:
- [ ] Operating rhythm >= 3 distinct rows
- [ ] Charters complete (5 fields, Quorum fraction, Membership typed)
- [ ] Pair count verified
- [ ] ORG-ELEMENT REGISTER populated (cat-1 through cat-4)
- [ ] Org Evolution Roadmap >= 2 distinct trigger categories
- [ ] Anti-Pattern Watch with typed citations from register
- [ ] No prohibited content from GATE 3 contract appears above this line

```
GATE 3 STATUS: [PASS / FAIL]
```

STOP — ARTIFACT COMPLETE. No additional content, sections, appendices, or commentary
follows this line. (C-31 — successful-completion path terminal seal)

---

## V-03 — Output Format: Complete Charter Inline Example

**axis:** output format — replace the 5-field charter field-label template with a complete
filled-in example charter: Name (concrete committee name as section header), Mission (one
sentence), Membership (>= 2 roles with `(TYPE)` annotations), Quorum (`N of M member roles`
fraction), Escalates (named destination)
**hypothesis:** C-32 requires a filled example charter, not field labels. V-01/R8's charter
section showed "Mission:", "Membership:", "Quorum:", "Escalates:" without concrete values,
earning C-11 PARTIAL (3/4 tables). Adding a complete filled example teaches the valid
instance format — especially Quorum fraction syntax and Membership annotation syntax — and
upgrades C-11 from PARTIAL to PASS. All gate structure, verification checkpoints (GATE 1
and GATE 2 only), and boundary contracts unchanged. C-29/C-30/C-31 remain open. Predicted:
C-32 PASS, C-11 PASS.

---

You are running `/org-chart {topic}`.

---

GATE CHAIN CONTRACT

Gates GATE 0, GATE 1, GATE 2, GATE 3. Each gate's outputs are required inputs for the
subsequent gate. Emitted in strictly ascending numeric order.

---

### GATE 0 — ROLES AND CLASSIFICATION

**Prerequisite:** none
**Produces:** typed role list

GATE 0 DO/DO NOT:
- DO: Read `.craft/roles/` before writing any content.
- DO NOT: Write any content outside the roles and classification blocks before GATE 0 STATUS.
- DO NOT: Introduce role names downstream not declared here.

GATE 0 CONTAINMENT CONTRACT — MUST NOT appear before GATE 0 STATUS:
- Inertia rows, org diagram nodes, headcount entries, rhythm rows, charter fields

**Step 0.1 — Load Roles**

```
ROLES-LOADED:
  - [role name] — [one-line description]
```
or
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] — [description]
```

**Step 0.2 — Role-Type Classification**

Immediately after roles block. Every role typed from {DECISION, EXECUTION, ADVISORY,
GOVERNANCE}. Three-tier order.

```
ROLE-TYPE-CLASSIFICATION:
  DECISION: [role names]
  EXECUTION: [role names]
  ADVISORY: [role names]
  GOVERNANCE: [role names]
```

GATE 0 STATUS:
- [ ] Roles block present
- [ ] All roles typed from closed set
- [ ] Containment contract satisfied

```
GATE 0 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 1 requires typed role list.

---

### GATE 1 — INERTIA ASSESSMENT

**Prerequisite:** typed role list from GATE 0
**Produces:** inertia verdict + FLAT-CASE-PRESSURE rating

GATE 1 DO/DO NOT:
- DO: Write default-position statement as Step 1.0, before mechanism table.
- DO: Four sub-sections in sequence.
- DO NOT: Write org diagram or headcount content before GATE 1 STATUS.

GATE 1 PROHIBITED CONTENT: ASCII org nodes, headcount rows, rhythm rows, charter fields.

**Step 1.0 — Default-Position Statement (C-28)**

> DEFAULT POSITION: The team can operate flat; structure must earn its place.

**Step 1.1 — Case for Staying Flat**

Mechanism table, Type from {CADENCE, CHANNEL, INFORMAL-LEAD, ARTIFACT}, >= 2 rows.

Inline example row:

| Type | Mechanism | Current Evidence |
|------|-----------|-----------------|
| CADENCE | Weekly cross-area standup | Resolves sprint-level dependencies across two areas without escalation — no blocked decision in the last quarter |

Two-step separator: count, verify >= 2, emit:
```
--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. FLAT-CASE-PRESSURE: [LOW|MEDIUM|HIGH]. How We Coordinate Today begins.] ---
```

**ENFORCEMENT — GUARD:** DO NOT EMIT separator before row count >= 2.
Two-site: Sub-section 1.2 MUST be preceded by the separator.

**Steps 1.2 through 1.4** (How We Coordinate Today / Rebuttal / VERDICT + concrete trigger)

Flat-verdict branch:
```
[ABSENT: ASCII Org Diagram] — flat verdict. No simplified alternative acceptable.
[ABSENT: Headcount by Area] — flat verdict.
[ABSENT: Operating Rhythm Table] — flat verdict.
[ABSENT: Committee Charters] — flat verdict.
[ABSENT: ORG-ELEMENT REGISTER] — flat verdict.
[ABSENT: Org Evolution Roadmap] — flat verdict.
[ABSENT: Anti-Pattern Watch] — flat verdict.
STOP — ARTIFACT COMPLETE.
```

**CHECKPOINT INERTIA-CHECK (C-22)**

Before GATE 1 STATUS:
- [ ] Default-position statement precedes mechanism table
- [ ] >= 2 mechanism rows with closed-set Types
- [ ] FLAT-CASE-PRESSURE from {LOW, MEDIUM, HIGH}
- [ ] VERDICT from {CAN-OPERATE-FLAT, STRUCTURE-WARRANTED} with reasoning
- [ ] Concrete re-assessment trigger
- [ ] No prohibited content above this line

```
GATE 1 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 2 requires inertia verdict + FLAT-CASE-PRESSURE rating.

---

### GATE 2 — STRUCTURAL ARTIFACT GENERATION

**Prerequisite:** inertia verdict + FLAT-CASE-PRESSURE rating from GATE 1
**Produces:** org diagram with typed nodes

GATE 2 DO/DO NOT:
- DO: ASCII hierarchy using ROLES-LOADED roles only. Split Decides/Escalates columns.
- DO NOT: New roles. DO NOT: Merged column.

GATE 2 PROHIBITED CONTENT: rhythm rows, charter fields.

**Step 2.1 — ASCII Org Diagram** (>= 2 levels, committees distinct, names from ROLES-LOADED)

**Step 2.2 — Headcount by Area** (5 columns, `(domain type)` on Key Roles)

Inline example row:

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| Platform Engineering | 6 | Principal Engineer (DECISION) | API versioning policy, breaking-change gates | Cross-product dependency resolution → Architecture Board |

At minimum two area rows + Total row.

**CHECKPOINT DIAGRAM-CHECK (C-22)**

Before GATE 2 STATUS:
- [ ] Diagram >= 2 levels, roles from ROLES-LOADED, committees distinct
- [ ] 5-column headcount, Decides/Escalates split, >= 2 areas + Total
- [ ] No rhythm rows or charter fields above this line

```
GATE 2 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 3 requires org diagram with typed nodes.

---

### GATE 3 — GOVERNANCE DOCUMENTATION

**Prerequisite:** org diagram with typed nodes from GATE 2
**Produces:** complete governance artifact

GATE 3 DO/DO NOT:
- DO: Interleave rhythm rows and charters.
- DO NOT: Batch rhythm first, charters second.
- DO NOT: Quorum without `N of M member roles` fraction.
- DO NOT: Membership without `(TYPE)` annotations.

**Step 3.1 — Operating Rhythm and Charters (Interleaved)**

Operating rhythm: >= 3 rows (ROB, shiproom/gate, governance). No merged rows.

Inline example rhythm row:

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|
| Architecture Board | Monthly | Principal Engineer | Review and approve cross-cutting design decisions affecting two or more service areas |

**Charter format — 5 fields required (C-05 / C-32 — complete example required)**

Complete filled example. Model this format exactly; fill concrete values for your topic:

```
### Architecture Review Board

**Mission:** Evaluate and approve cross-cutting architectural decisions before
implementation begins, ensuring consistency across all service areas.
**Membership:** Principal Engineer (DECISION), Engineering Manager (GOVERNANCE),
Staff Engineer (ADVISORY)
**Quorum:** 2 of 3 member roles
**Escalates:** VP Engineering
```

Template for each governance committee in this artifact:

```
### [Committee Name]

**Mission:** [one sentence — what this committee decides or governs]
**Membership:** [Role A (TYPE)], [Role B (TYPE)]
**Quorum:** [N] of [M] member roles
**Escalates:** [named destination role or forum]
```

REQUIRED:
- Membership MUST list >= 2 roles each annotated with `(TYPE)` from
  {DECISION, EXECUTION, ADVISORY, GOVERNANCE}.
- Quorum MUST use `N of M member roles` fraction form. Percentage or prose quorum is
  not acceptable. The filled example above shows the required format.
- Name MUST be a concrete committee name as the section header (not a placeholder).

**Step 3.2 — Pair-Count Verification (C-19)**

Governance rows in ORT: [N]. Charters produced: [N]. MUST match before advancing.

**Step 3.3 — ORG-ELEMENT REGISTER** (all four categories populated before Step 3.4)

```
ORG-ELEMENT REGISTER

  Category schema:
  | cat-N | Category name         | Element type                                          |
  |-------|-----------------------|-------------------------------------------------------|
  | cat-1 | Areas                 | Area names from the Headcount by Area table           |
  | cat-2 | Committees/Cadences   | Committee and cadence names from Rhythm Table/Charters|
  | cat-3 | Headcount             | Total headcount and per-area headcount counts         |
  | cat-4 | DRI Roles             | DRI role names from the Operating Rhythm Table        |

  cat-1 (Areas): - [area name] — headcount: [N]
  cat-2 (Committees/Cadences): - [name]
  cat-3 (Headcount): - Total headcount: [N]
  cat-4 (DRI Roles): - [DRI role]
```

**Step 3.4 — Org Evolution Roadmap** (>= 2 rows, distinct trigger categories)

Inline example row:

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| Headcount exceeds 15 engineers | Split Platform area into Core and Extensions; add Area Lead role | headcount-threshold |

**Step 3.5 — Anti-Pattern Watch** (>= 2 rows, typed citations from register)

GATE 3 STATUS:
- [ ] Operating rhythm >= 3 rows
- [ ] Charters complete (5 fields, Quorum fraction, Membership typed)
- [ ] Pair count verified
- [ ] ORG-ELEMENT REGISTER populated
- [ ] Org Evolution Roadmap >= 2 distinct triggers
- [ ] Anti-Pattern Watch with typed citations

```
GATE 3 STATUS: [PASS / FAIL]
```

---

```
Generated by: /org-chart {topic} — {date}
```

---

## V-04 — Combined: All-Gate Blocking + GATE 3 Dual-Boundary

**axis:** lifecycle emphasis (combined) — V-01 all-gate blocking checkpoints (CHECKPOINT-0
and CHECKPOINT-3) + V-02 GATE 3 prohibited-content contract and post-STATUS terminal seal.
Charter example remains field-labels only (C-32 open).
**hypothesis:** C-29, C-30, C-31 are independent structural additions. CHECKPOINT-0 and
CHECKPOINT-3 do not affect GATE 3's boundary contracts; GATE 3 prohibited-content contract
and terminal seal do not affect GATE 0's verification checkpoint. No cross-criterion
interference. Combination closes three gaps simultaneously. Predicted: C-29/C-30/C-31 PASS.

---

You are running `/org-chart {topic}`.

---

GATE CHAIN CONTRACT

Gates GATE 0, GATE 1, GATE 2, GATE 3. Each gate's outputs are required inputs for the
subsequent gate. MUST emit in strictly ascending numeric order. Every gate carries a
dedicated verification checkpoint before STATUS — no gate may emit STATUS without its
own checkpoint clearing first.

---

### GATE 0 — ROLES AND CLASSIFICATION

**Prerequisite:** none
**Produces:** typed role list

GATE 0 DO/DO NOT:
- DO: Read `.craft/roles/` before writing any content.
- DO NOT: Write any content outside the roles and classification blocks before GATE 0 STATUS.
- DO NOT: Introduce role names downstream not declared here.

GATE 0 CONTAINMENT CONTRACT — MUST NOT appear within GATE 0 before STATUS:
- Inertia rows, org diagram nodes, headcount entries, rhythm rows, charter fields

**Step 0.1 — Load Roles**

```
ROLES-LOADED:
  - [role name] — [one-line description]
```
or
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] — [description]
```

**Step 0.2 — Role-Type Classification**

Immediately after roles block. Every role typed from {DECISION, EXECUTION, ADVISORY,
GOVERNANCE}. Three-tier order.

```
ROLE-TYPE-CLASSIFICATION:
  DECISION: [role names]
  EXECUTION: [role names]
  ADVISORY: [role names]
  GOVERNANCE: [role names]
```

**CHECKPOINT-0 (C-29 — all-gate blocking)**

Before emitting GATE 0 STATUS, verify all items:
- [ ] ROLES-LOADED or ROLES-NOTE block present and lists all roles
- [ ] ROLE-TYPE-CLASSIFICATION assigns every role a type from the closed set
- [ ] No structural content between Step 0.1 and Step 0.2
- [ ] No content from GATE 0 CONTAINMENT CONTRACT appears above this line

GATE 0 STATUS:
- [ ] Roles block present
- [ ] All roles typed from closed set
- [ ] Containment contract satisfied
- [ ] CHECKPOINT-0 cleared

```
GATE 0 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 1 requires typed role list. GATE 1 MUST NOT begin
if GATE 0 STATUS is FAIL.

---

### GATE 1 — INERTIA ASSESSMENT

**Prerequisite:** typed role list from GATE 0
**Produces:** inertia verdict + FLAT-CASE-PRESSURE rating

GATE 1 DO/DO NOT:
- DO: Write default-position statement as Step 1.0 before mechanism table.
- DO: Four sub-sections in sequence.
- DO NOT: Org diagram or headcount content before GATE 1 STATUS.
- DO NOT: "Revisit as the team grows" as a trigger.

GATE 1 PROHIBITED CONTENT: ASCII org nodes, headcount rows, rhythm rows, charter fields.

**Step 1.0 — Default-Position Statement (C-28)**

> DEFAULT POSITION: The team can operate flat; structure must earn its place.

Executable step — MUST precede mechanism table.

**Step 1.1 — Case for Staying Flat**

Mechanism table, Type from {CADENCE, CHANNEL, INFORMAL-LEAD, ARTIFACT}, >= 2 rows.

Inline example row:

| Type | Mechanism | Current Evidence |
|------|-----------|-----------------|
| CADENCE | Weekly cross-area standup | Resolves sprint-level dependencies across two areas without escalation — no blocked decision in the last quarter |

Two-step separator: count, verify >= 2, emit:
```
--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. FLAT-CASE-PRESSURE: [LOW|MEDIUM|HIGH]. How We Coordinate Today begins.] ---
```

**ENFORCEMENT — GUARD:** DO NOT EMIT separator before row count >= 2.
Two-site: Sub-section 1.2 MUST be preceded by the separator.

**Steps 1.2–1.4** (How We Coordinate Today / Rebuttal / VERDICT + concrete trigger)

Flat-verdict branch:
```
[ABSENT: ASCII Org Diagram] — flat verdict. No simplified alternative acceptable.
[ABSENT: Headcount by Area] — flat verdict.
[ABSENT: Operating Rhythm Table] — flat verdict.
[ABSENT: Committee Charters] — flat verdict.
[ABSENT: ORG-ELEMENT REGISTER] — flat verdict.
[ABSENT: Org Evolution Roadmap] — flat verdict.
[ABSENT: Anti-Pattern Watch] — flat verdict.
STOP — ARTIFACT COMPLETE. No content follows this directive.
```

**CHECKPOINT INERTIA-CHECK (C-22)**

Before GATE 1 STATUS:
- [ ] Default-position statement precedes mechanism table
- [ ] >= 2 mechanism rows with closed-set Types
- [ ] FLAT-CASE-PRESSURE from {LOW, MEDIUM, HIGH}
- [ ] VERDICT with reasoning
- [ ] Concrete re-assessment trigger
- [ ] No prohibited content above this line

```
GATE 1 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 2 requires inertia verdict + FLAT-CASE-PRESSURE rating.
GATE 2 MUST NOT begin if GATE 1 STATUS is FAIL.

---

### GATE 2 — STRUCTURAL ARTIFACT GENERATION

**Prerequisite:** inertia verdict + FLAT-CASE-PRESSURE rating from GATE 1
**Produces:** org diagram with typed nodes

GATE 2 DO/DO NOT:
- DO: ASCII hierarchy using ROLES-LOADED roles only. Split Decides/Escalates.
- DO NOT: New roles. DO NOT: Merged column.

GATE 2 PROHIBITED CONTENT: rhythm rows, charter fields.

**Step 2.1 — ASCII Org Diagram** (>= 2 levels, committees as distinct nodes, ROLES-LOADED names)

**Step 2.2 — Headcount by Area** (5 columns, Key Roles `(domain type)`)

Inline example row:

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| Platform Engineering | 6 | Principal Engineer (DECISION) | API versioning policy, breaking-change gates | Cross-product dependency resolution → Architecture Board |

At minimum two area rows + Total row.

**CHECKPOINT DIAGRAM-CHECK (C-22)**

Before GATE 2 STATUS:
- [ ] Diagram >= 2 levels, roles from ROLES-LOADED, committees distinct
- [ ] 5-column headcount, Decides/Escalates split, >= 2 areas + Total
- [ ] No rhythm rows or charter fields above this line

```
GATE 2 STATUS: [PASS / FAIL]
```

**Named artifact handoff:** GATE 3 requires org diagram with typed nodes.
GATE 3 MUST NOT begin if GATE 2 STATUS is FAIL.

---

### GATE 3 — GOVERNANCE DOCUMENTATION

**Prerequisite:** org diagram with typed nodes from GATE 2
**Produces:** complete governance artifact

GATE 3 DO/DO NOT:
- DO: Interleave rhythm rows and charters.
- DO: Verify pair count after all pairs written.
- DO NOT: Batch rhythm first, charters second.
- DO NOT: Quorum without `N of M member roles` fraction.
- DO NOT: Membership without `(TYPE)` annotations.

**Step 3.1 — Operating Rhythm and Charters (Interleaved)**

Operating rhythm: >= 3 rows (ROB, shiproom/gate, governance). No merged rows.

Inline example rhythm row:

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|
| Architecture Board | Monthly | Principal Engineer | Review and approve cross-cutting design decisions affecting two or more service areas |

Charter format — 5 fields:
```
### [Committee Name]

**Mission:** [one sentence]
**Membership:** [Role A (TYPE)], [Role B (TYPE)]
**Quorum:** [N] of [M] member roles
**Escalates:** [named destination]
```

REQUIRED: Membership >= 2 roles with `(TYPE)`. Quorum in `N of M member roles` form.

**Step 3.2 — Pair-Count Verification (C-19)**

Governance rows in ORT: [N]. Charters produced: [N]. MUST match before advancing.

**Step 3.3 — ORG-ELEMENT REGISTER**

```
ORG-ELEMENT REGISTER

  Category schema:
  | cat-N | Category name         | Element type                                          |
  |-------|-----------------------|-------------------------------------------------------|
  | cat-1 | Areas                 | Area names from the Headcount by Area table           |
  | cat-2 | Committees/Cadences   | Committee and cadence names from Rhythm Table/Charters|
  | cat-3 | Headcount             | Total headcount and per-area headcount counts         |
  | cat-4 | DRI Roles             | DRI role names from the Operating Rhythm Table        |

  cat-1 (Areas): - [area name] — headcount: [N]
  cat-2 (Committees/Cadences): - [name]
  cat-3 (Headcount): - Total headcount: [N]
  cat-4 (DRI Roles): - [DRI role]
```

**Step 3.4 — Org Evolution Roadmap** (>= 2 rows, distinct trigger categories)

Inline example row:

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| Headcount exceeds 15 engineers | Split Platform area into Core and Extensions; add Area Lead role | headcount-threshold |

**Step 3.5 — Anti-Pattern Watch** (>= 2 rows, typed citations `[element name] (cat-N)`)

**GATE 3 PROHIBITED CONTENT (C-30 — terminal gate contract)**

The following MUST NOT appear within GATE 3 before STATUS is emitted:
- Appendices of any kind
- Supplementary sections (additional tables, notes, annexes)
- Editorial commentary or rationale paragraphs after the Anti-Pattern Watch table
- Additional committee charters not paired with an operating rhythm row
- Any content category not part of Steps 3.1 through 3.5

Terminal-gate position does not exempt GATE 3 from this contract. The intra-gate content
risk at GATE 3 is content appended after the Anti-Pattern Watch table and before STATUS —
this contract closes that path.

**CHECKPOINT-3 (C-29 — all-gate blocking)**

Before emitting GATE 3 STATUS, verify all checkboxes:
- [ ] Operating Rhythm Table >= 3 distinct rows (ROB, shiproom/gate, governance)
- [ ] Pair count verified: governance rows == charter count
- [ ] Each charter has all 5 fields (Mission, Membership, Quorum, Escalates + Name as header)
- [ ] Quorum in `N of M member roles` form for all charters
- [ ] Membership >= 2 roles with `(TYPE)` annotation
- [ ] ORG-ELEMENT REGISTER has all four categories (cat-1 through cat-4) populated
- [ ] Org Evolution Roadmap >= 2 rows with distinct trigger categories
- [ ] Anti-Pattern Watch >= 2 rows with typed citations from register
- [ ] No prohibited content from GATE 3 contract appears above this line

GATE 3 STATUS:
- [ ] Operating rhythm >= 3 rows
- [ ] Charters complete (5 fields, Quorum fraction, Membership typed)
- [ ] Pair count verified
- [ ] ORG-ELEMENT REGISTER populated
- [ ] Org Evolution Roadmap >= 2 distinct triggers
- [ ] Anti-Pattern Watch with typed citations
- [ ] GATE 3 prohibited-content contract satisfied
- [ ] CHECKPOINT-3 cleared

```
GATE 3 STATUS: [PASS / FAIL]
```

STOP — ARTIFACT COMPLETE. No additional content, sections, appendices, or commentary
follows this line. (C-31 — successful-completion path terminal seal)

---

## V-05 — Full Combination: All Four v9 Criteria (C-29 + C-30 + C-31 + C-32)

**axis:** full combination — V-01 (CHECKPOINT-0 + CHECKPOINT-3) + V-02 (GATE 3
prohibited-content contract + post-STATUS terminal seal) + V-03 (complete filled charter
example with all 5 fields). Charter example uses concrete values, not field labels.
**hypothesis:** V-04 closes C-29/C-30/C-31 without interfering with C-32. V-03 closes C-32
without affecting gate boundary structure. Full combination targets C-01 through C-32.
Predicted: 32/32.

---

You are running `/org-chart {topic}`.

---

GATE CHAIN CONTRACT

Gates GATE 0, GATE 1, GATE 2, GATE 3. Each gate's outputs are required inputs for the
subsequent gate. MUST emit in strictly ascending numeric order. Every gate carries a
dedicated verification checkpoint before STATUS — no gate may emit STATUS without its
own checkpoint clearing first.

---

### GATE 0 — ROLES AND CLASSIFICATION

**Prerequisite:** none
**Produces:** typed role list

GATE 0 DO/DO NOT:
- DO: Read `.craft/roles/` before writing any content.
- DO NOT: Write any content outside the roles and classification blocks before GATE 0 STATUS.
- DO NOT: Introduce role names downstream not declared here.

GATE 0 CONTAINMENT CONTRACT — MUST NOT appear within GATE 0 before STATUS:
- Inertia assessment rows or sub-sections
- Org diagram nodes or ASCII hierarchy
- Headcount area entries
- Operating rhythm rows
- Committee charter fields

**Step 0.1 — Load Roles**

Check `.craft/roles/` for existing role definitions.

```
ROLES-LOADED:
  - [role name] — [one-line description from role file]
  - [role name] — [one-line description from role file]
```

If no role files found:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] — [description]
  - [role name] — [description]
```

**Step 0.2 — Role-Type Classification**

Immediately after the roles block — no structural content may appear between Step 0.1
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

**CHECKPOINT-0 (C-29 — all-gate blocking)**

Before emitting GATE 0 STATUS, verify all items:
- [ ] ROLES-LOADED or ROLES-NOTE block present and lists all roles
- [ ] ROLE-TYPE-CLASSIFICATION assigns every role a type from the closed set
- [ ] No structural content appeared between Step 0.1 and Step 0.2
- [ ] No content from GATE 0 CONTAINMENT CONTRACT appears above this line

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

### GATE 1 — INERTIA ASSESSMENT

**Prerequisite:** typed role list from GATE 0
**Produces:** inertia verdict + FLAT-CASE-PRESSURE rating

GATE 1 DO/DO NOT:
- DO: Write the default-position statement as the first executable step (Step 1.0),
  before any mechanism rows.
- DO: Present all four sub-sections in sequence.
- DO NOT: Write an org diagram node or headcount entry before GATE 1 STATUS.
- DO NOT: Use "the team is growing" as a rebuttal without naming the failure mode.
- DO NOT: Use a FLAT-CASE-PRESSURE rating outside the closed set {LOW, MEDIUM, HIGH}.
- DO NOT: Use "revisit as the team grows" — trigger MUST name a concrete condition.

GATE 1 PROHIBITED CONTENT — MUST NOT appear within GATE 1 before STATUS:
- ASCII org diagram nodes or hierarchy lines
- Headcount area rows
- Operating rhythm cadence rows
- Committee charter fields (Mission, Membership, Quorum, Escalates)

**Step 1.0 — Default-Position Statement (C-28 step embed)**

Write the following statement as the first line of GATE 1, before any mechanism rows:

> DEFAULT POSITION: The team can operate flat; structure must earn its place.

This is an executable step. It MUST be encountered during execution of GATE 1.
It MUST precede the mechanism table. It is not a preamble or scene-setter.

**Step 1.1 — Case for Staying Flat**

Present a mechanism table with Type from the closed set {CADENCE, CHANNEL, INFORMAL-LEAD,
ARTIFACT}. Produce at least two rows before the separator.

Inline example row (complete, not a label):

| Type | Mechanism | Current Evidence |
|------|-----------|-----------------|
| CADENCE | Weekly cross-area standup | Resolves sprint-level dependencies across two areas without escalation — no blocked decision in the last quarter |

```
### Case for Staying Flat

| Type | Mechanism | Current Evidence |
|------|-----------|-----------------|
| [CADENCE|CHANNEL|INFORMAL-LEAD|ARTIFACT] | [specific named mechanism] | [observable evidence this mechanism works] |
| [CADENCE|CHANNEL|INFORMAL-LEAD|ARTIFACT] | [second mechanism] | [evidence] |
```

Two-step separator protocol:
- Step A: Count mechanism rows in the table above.
- Step B: If count < 2, write missing rows first. Once count >= 2, substitute as N.

DO NOT EMIT the separator before Step B passes:
```
--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. FLAT-CASE-PRESSURE: [LOW|MEDIUM|HIGH]. How We Coordinate Today begins.] ---
```

**ENFORCEMENT — GUARD:** DO NOT EMIT the FLAT-CASE-CLOSED separator before row count >= 2.
DO NOT begin Step 1.2 until the separator appears in output.
Two-site: Sub-section 1.2 prose MUST be preceded by the separator — no Sub-section 1.2
content before the separator is acceptable.

**Step 1.2 — How We Coordinate Today**

Inventory current coordination: channels, cadences, informal roles, artifacts.
DO NOT re-list mechanism rows from Step 1.1.

```
### How We Coordinate Today
[Catalog: named meetings, shared artifacts, escalation paths, informal roles with frequency and participants]
```

**Step 1.3 — Rebuttal**

Name the coordination failure the flat case cannot answer.

```
### Rebuttal
[Named failure mode — specific, observable]
```

**Step 1.4 — VERDICT and Re-assessment Trigger**

```
### VERDICT

[CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]

Reasoning: [specific — connecting all three sub-sections]

Re-assessment trigger: [concrete condition]
```

Flat-verdict branch:
```
[ABSENT: ASCII Org Diagram] — flat verdict. "Simplified" or "compact" alternatives
are not acceptable substitutes for this ABSENT label.
[ABSENT: Headcount by Area] — flat verdict.
[ABSENT: Operating Rhythm Table] — flat verdict.
[ABSENT: Committee Charters] — flat verdict.
[ABSENT: ORG-ELEMENT REGISTER] — flat verdict.
[ABSENT: Org Evolution Roadmap] — flat verdict.
[ABSENT: Anti-Pattern Watch] — flat verdict.
STOP — ARTIFACT COMPLETE. No content follows this directive.
```

**CHECKPOINT INERTIA-CHECK (C-22 — blocking)**

Before emitting GATE 1 STATUS, verify all checkboxes:
- [ ] Default-position statement precedes mechanism table
- [ ] Case for Staying Flat has >= 2 mechanism rows with Types from closed set
- [ ] FLAT-CASE-PRESSURE is from {LOW, MEDIUM, HIGH}
- [ ] VERDICT is from {CAN-OPERATE-FLAT, STRUCTURE-WARRANTED} with reasoning
- [ ] Re-assessment trigger is concrete
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

### GATE 2 — STRUCTURAL ARTIFACT GENERATION

**Prerequisite:** inertia verdict + FLAT-CASE-PRESSURE rating from GATE 1
**Produces:** org diagram with typed nodes

GATE 2 DO/DO NOT:
- DO: Draw ASCII hierarchy using only role names from ROLES-LOADED.
- DO: Use split Decides/Escalates columns — separate, not merged.
- DO NOT: Introduce any role name not in GATE 0's typed role list.
- DO NOT: Use a single "Decision Scope" column.

GATE 2 PROHIBITED CONTENT — MUST NOT appear within GATE 2 before STATUS:
- Operating rhythm cadence rows
- Committee charter fields

**Step 2.1 — ASCII Org Diagram**

Draw ASCII hierarchy with at minimum two levels. Committees as distinct labeled nodes.
All role names MUST come from ROLES-LOADED.

**Step 2.2 — Headcount by Area**

Five columns: Area, Headcount, Key Roles, Decides, Escalates. Key Roles annotated
with `(domain type)`.

Inline example row (complete, not a label):

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| Platform Engineering | 6 | Principal Engineer (DECISION) | API versioning policy, breaking-change gates | Cross-product dependency resolution → Architecture Board |

```
| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| [name] | [N or N-M] | [role (domain type)] | [decision types owned] | [decisions escalated — named destination] |
| [name] | [N or N-M] | [role (domain type)] | [decision types owned] | [decisions escalated — named destination] |
| **Total** | **[N]** | | | |
```

At minimum two area rows with individual counts and a Total row.

**CHECKPOINT DIAGRAM-CHECK (C-22 — blocking)**

Before emitting GATE 2 STATUS, verify all checkboxes:
- [ ] ASCII diagram >= 2 hierarchy levels
- [ ] All role names in diagram from ROLES-LOADED
- [ ] Committees as distinct nodes
- [ ] Headcount table has five columns (Area, Headcount, Key Roles, Decides, Escalates)
- [ ] At least two area rows and a Total row present
- [ ] No rhythm rows or charter fields above this line

GATE 2 STATUS:
- [ ] ASCII diagram with >= 2 levels
- [ ] Committees as distinct nodes
- [ ] Headcount has split Decides/Escalates
- [ ] >= 2 area rows + Total
- [ ] CHECKPOINT DIAGRAM-CHECK cleared

```
GATE 2 STATUS: [PASS / FAIL]
```

If FAIL: DO NOT advance to GATE 3.

**Named artifact handoff:** GATE 3 requires org diagram with typed nodes.
If GATE 2 STATUS is FAIL, GATE 3 MUST NOT begin.

---

### GATE 3 — GOVERNANCE DOCUMENTATION

**Prerequisite:** org diagram with typed nodes from GATE 2
**Produces:** complete governance artifact

GATE 3 DO/DO NOT:
- DO: Produce operating rhythm rows and committee charters in interleaved pairs —
  each governance row immediately followed by its charter.
- DO: Verify pair count equals governance row count after all pairs are written.
- DO NOT: Batch all rhythm rows first and all charters second.
- DO NOT: Reference a role not in ROLES-LOADED in charter Membership.
- DO NOT: Write Quorum without `N of M member roles` fraction form.
- DO NOT: Write Membership without `(TYPE)` annotation on each role.

**Step 3.1 — Operating Rhythm and Charters (Interleaved)**

Operating rhythm: >= 3 distinct cadences (ROB, shiproom/gate, governance). No merged rows.

Inline example row for operating rhythm (complete, not a label):

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|
| Architecture Board | Monthly | Principal Engineer | Review and approve cross-cutting design decisions affecting two or more service areas |

**Charter format — 5 fields required (C-05 / C-32 — complete example)**

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

**Mission:** [one sentence — what this committee decides or governs]
**Membership:** [Role A (TYPE)], [Role B (TYPE)]
**Quorum:** [N] of [M] member roles
**Escalates:** [named destination role or forum]
```

REQUIRED:
- Membership MUST list >= 2 roles each annotated with `(TYPE)` from
  {DECISION, EXECUTION, ADVISORY, GOVERNANCE}.
- Quorum MUST use `N of M member roles` fraction form. Percentage, prose quorum
  ("majority"), or missing Quorum field is not acceptable. See filled example above.
- Name MUST be a concrete committee name as the section header — not a placeholder.

**Step 3.2 — Post-Interleave Pair-Count Verification (C-19)**

After all rhythm-charter pairs are produced:
- Count governance rows in the Operating Rhythm Table: [N]
- Count committee charters produced: [N]
- MUST match. If mismatch: identify the gap, produce missing charter, recount.
  DO NOT advance to Step 3.3 until counts match.

**Step 3.3 — ORG-ELEMENT REGISTER**

MUST produce immediately after Committee Charters. All four category entries MUST be
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
    - [area name] — headcount: [N]
    (all areas from the Headcount table)

  cat-2 (Committees/Cadences):
    - [committee or cadence name]
    (all committees and named cadences)

  cat-3 (Headcount):
    - Total headcount: [N]

  cat-4 (DRI Roles):
    - [DRI role name]
    (all DRI roles from the Rhythm Table)
```

All four categories MUST be populated before advancing to Step 3.4.

**Step 3.4 — Org Evolution Roadmap**

At minimum two rows, distinct trigger categories. Row 1 MUST be a headcount threshold.
Row 2 MUST be from a different category (workload signal, structural symptom, milestone).
Two headcount numbers at different values count as one dimension, not two.

Inline example row (complete, not a label):

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| Headcount exceeds 15 engineers | Split Platform area into Core and Extensions sub-areas; add Area Lead role | headcount-threshold |

```
## Org Evolution Roadmap

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| [headcount threshold] | [Named structural change] | headcount-threshold |
| [workload signal, structural symptom, or milestone] | [Named structural change] | [type] |
```

**Step 3.5 — Anti-Pattern Watch**

At minimum two rows. Each "Why It Applies Here" cell MUST open with:
`[element name] (cat-N) — [one sentence]`

Element names copied exactly from the ORG-ELEMENT REGISTER.
DO NOT use a cat-N code not in the register schema.

```
## Anti-Pattern Watch

| Anti-Pattern | Why It Applies Here | Mitigation |
|--------------|---------------------|------------|
| [Named anti-pattern] | `[element name] (cat-N) — [one sentence of specific relevance]` | [Mitigation] |
| [Second anti-pattern] | `[element name] (cat-N) — [one sentence]` | [Mitigation] |
```

**GATE 3 PROHIBITED CONTENT (C-30 — terminal gate contract)**

The following MUST NOT appear within GATE 3 before STATUS is emitted:
- Appendices of any kind
- Supplementary sections (additional tables, notes, annexes)
- Editorial commentary or rationale paragraphs after the Anti-Pattern Watch table
- Additional committee charters not paired with an operating rhythm row
- Any content category not explicitly part of Steps 3.1 through 3.5

Terminal-gate position does not exempt GATE 3 from this contract. The intra-gate content
risk at GATE 3 is content appended after the Anti-Pattern Watch table and before STATUS.

**CHECKPOINT-3 (C-29 — all-gate blocking)**

Before emitting GATE 3 STATUS, verify all checkboxes:
- [ ] Operating Rhythm Table has >= 3 distinct rows (ROB, shiproom/gate, governance)
- [ ] Pair count verified: governance rows in ORT == charter count produced
- [ ] Each charter has all 5 fields: Name (header), Mission, Membership, Quorum, Escalates
- [ ] Quorum in `N of M member roles` form for all charters
- [ ] Membership >= 2 roles with `(TYPE)` annotation for all charters
- [ ] ORG-ELEMENT REGISTER has all four categories (cat-1 through cat-4) populated
- [ ] Org Evolution Roadmap has >= 2 rows with distinct trigger categories
- [ ] Anti-Pattern Watch has >= 2 rows with typed citations from register
- [ ] No prohibited content from GATE 3 contract appears above this line

All checkboxes MUST be ticked before GATE 3 STATUS can read PASS.

GATE 3 STATUS:
- [ ] Operating rhythm >= 3 distinct rows
- [ ] Charters complete (5 fields, Quorum fraction, Membership typed)
- [ ] Pair count verified
- [ ] ORG-ELEMENT REGISTER populated (cat-1 through cat-4)
- [ ] Org Evolution Roadmap >= 2 rows with distinct trigger categories
- [ ] Anti-Pattern Watch with typed citations from register
- [ ] GATE 3 prohibited-content contract satisfied
- [ ] CHECKPOINT-3 cleared

```
GATE 3 STATUS: [PASS / FAIL]
```

STOP — ARTIFACT COMPLETE. No additional content, sections, appendices, or commentary
follows this line. (C-31 — successful-completion path terminal seal)
