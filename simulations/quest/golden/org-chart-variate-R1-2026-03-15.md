---
skill: quest-variate
skill_target: org-chart
date: 2026-03-15
round: R1
rubric_version: v1
status: variate
---

# org-chart Variate — Round 1

**Date:** 2026-03-15
**Skill:** org-chart
**Rubric:** v1 (C-01 through C-10; essential C-01–C-05)
**Round:** R1 — single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

---

## Round 1 Variation Map

| V | Axis | What Changed | Hypothesis |
|---|------|--------------|------------|
| V-01 | inertia-framing | Inertia assessment is a labeled gate with an explicit VERDICT field that must be resolved before any org boxes are written | Requiring a named VERDICT (CAN-OPERATE-FLAT / STRUCTURE-WARRANTED) before structure output protects C-01 from omission and prevents the gate from being absorbed into a generic introduction paragraph |
| V-02 | output-format | Four section templates (INERTIA-ASSESSMENT, ASCII-ORG-BOX, HEADCOUNT-TABLE, RHYTHM-TABLE) are given as fill-in scaffolds, each with structural slot requirements | Pre-specifying section slots with required fields improves C-07 (all four sections present) and C-04/C-05 (headcount and rhythm completeness) because the format makes omission structurally impossible |
| V-03 | role-sequence | .roles/ read step is the first action, roles are named in a ROLES-LOADED list, and subsequent sections must reference at least one loaded role by name | Front-loading the roles step before any writing ensures C-03 is satisfied from context, not as a retrofit; named roles anchor the org design rather than appearing as optional flavor |
| V-04 | phrasing-register + inertia-framing | Fully imperative DO/DO NOT register combined with the inertia gate and VERDICT requirement | Prohibitions prevent jumping to org boxes without the inertia check; combined with the VERDICT gate, this covers C-01 (inertia), C-02 (ASCII diagram), C-04 (headcount), and C-05 (rhythm table) simultaneously |
| V-05 | lifecycle-emphasis + output-format | Explicit five-phase sequence (READ-ROLES → ASSESS-INERTIA → DESIGN-STRUCTURE → DOCUMENT-RHYTHMS → CHARTER-COMMITTEES) with per-phase output templates and charter element checklist | Naming each phase as a discrete step with its own output contract improves C-06 (committee charters with all three elements) and C-08 (decision rights per area) because those sections have explicit slots that must be filled before advancing |

---

## V-01 — Inertia Framing: Inertia as a Named Gate with VERDICT

**axis:** inertia-framing
**hypothesis:** Requiring a named VERDICT field (CAN-OPERATE-FLAT or STRUCTURE-WARRANTED) before any org box is written forces C-01 to be substantive and prevents generic filler. If C-01 pass rate does not improve over a baseline that lacks the VERDICT requirement, the gate adds no protective value.

---

You are running `/org-chart {topic}`.

---

INERTIA GATE

Before drawing any org box or proposing any committee, answer the inertia question.
The inertia question is: **Can this team operate effectively without a formal org structure?**

The primary competitor to formal structure is always the status quo — informal coordination,
direct communication, shared Slack channels, ad-hoc leadership. Structure imposes cost
(coordination overhead, reporting lines, slower decisions). Structure is only warranted when
the cost of informal coordination exceeds the cost of formalization.

Write the inertia assessment as a labeled section:

```
## Inertia Assessment

### Current state
[Describe how the team coordinates today. What informal mechanisms exist?
What is working? What is breaking down?]

### Flat-team viability
[State the maximum headcount at which the team could operate without a
formal org. If headcount is already above that threshold, say so explicitly.
If below, state that flat operation remains viable and identify the trigger
that would change this.]

### VERDICT
[Choose one: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED]

Reasoning: [One or two sentences connecting the current state and headcount
analysis to the verdict. Must be specific — not "the team is growing" but
"at N people across M time zones with P concurrent work streams, informal
coordination produces [specific failure mode]".]
```

Do not write an org diagram or rhythm table until the VERDICT is written.

If VERDICT is CAN-OPERATE-FLAT: the output should still include a lightweight
coordination model (who owns what, when the team syncs) rather than a formal
org chart. Note the trigger that would flip the verdict to STRUCTURE-WARRANTED.

If VERDICT is STRUCTURE-WARRANTED: proceed to the full org chart output below.

---

ROLES INPUT

Check whether `.roles/` contains role files for this domain. If role files exist:
- List the roles found in a ROLES-LOADED line at the top of the org chart section
- Use those role names in the org hierarchy, headcount table, and committee charters
- Do not invent role names that contradict or duplicate roles already defined

If `.roles/` is absent or empty:
- Write a ROLES-NOTE line: "No .roles/ files found — using inferred roles."
- Proceed with inferred role names appropriate to the domain

---

ASCII ORG BOX

Render an ASCII hierarchy showing at minimum two levels. Use boxes or indented tree.

Example structure (not prescriptive):
```
+-------------------+
|  Area Lead        |
+-------------------+
     |         |
+--------+  +--------+
| Sub-A  |  | Sub-B  |
+--------+  +--------+
```

The org box must show area leads, sub-teams or functions, and any cross-cutting
committees. Committees should appear as a separate layer or labeled node, not
embedded in a single area's subtree.

---

HEADCOUNT BY AREA

Produce a table with at minimum two rows (two distinct areas), a numeric or range count
for each, and any known named roles from `.roles/`:

| Area | Headcount | Key Roles |
|------|-----------|-----------|
| ...  | N or N-M  | role names from .roles/ or inferred |

Include a total row at the bottom.

---

OPERATING RHYTHM TABLE

Produce a structured table of operating cadences. The table must contain at minimum
three distinct entries covering:
1. ROB (Review of the Business / weekly business review or equivalent)
2. A shiproom or feature-gate meeting
3. One governance meeting (architecture board, steering committee, or equivalent)

Required columns:

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|

Do not combine multiple meetings into a single row to meet the three-entry minimum.

---

ARTIFACT OUTPUT

Write the complete artifact to `org-chart.md` with this section order:
1. Inertia Assessment (with VERDICT)
2. ASCII Org Box (with ROLES-LOADED or ROLES-NOTE)
3. Headcount by Area
4. Operating Rhythm Table

---

FINAL LINE

The last line of the artifact must be:

```
Generated by: /org-chart {topic} — {date}
```

Replace {topic} and {date} with actual values.

---

## V-02 — Output Format: Section Scaffolds with Required Slots

**axis:** output-format
**hypothesis:** Providing four section templates with required slot fields makes omission structurally impossible — the model cannot skip a section because the section header and required fields are already present as a fill-in scaffold. This improves C-07 (all four sections) and prevents C-04/C-05 from being reduced to a paragraph when a table was required. Falsifiable: if sections are still missing or fields are omitted despite the scaffold, format alone does not fix coverage gaps.

---

You are running `/org-chart {topic}`.

Generate an org structure for the topic domain. Use the four section templates below.
Fill in every slot. Do not omit any template section or skip a required field.

---

### SECTION 1 — INERTIA ASSESSMENT (required)

Fill in this section before writing anything else.

```
## Inertia Assessment

**Can this team operate without formal structure?**

Current coordination mode: [how the team coordinates today — what meetings,
channels, or informal leads already exist]

Flat-team threshold: [the headcount or complexity level at which flat
coordination breaks down for this type of team]

Current team position: [below threshold / at threshold / above threshold]

Verdict: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]

Justification: [specific reason tied to the above, not generic]
```

---

### SECTION 2 — ASCII ORG BOX (required)

Fill in this section after the inertia assessment.

```
## Org Structure

ROLES-LOADED: [comma-separated list of role names from .roles/, or
"none — using inferred roles" if .roles/ is absent]

[ASCII org diagram — must show at least two levels]
```

Diagram requirements:
- Top level: area or division leads
- Second level: sub-teams, functions, or named roles
- Committees or boards: shown as a separate labeled node or layer
- At least two top-level nodes required (one node is a single person, not an org)

---

### SECTION 3 — HEADCOUNT BY AREA (required)

Fill in this table immediately after the org diagram.

```
## Headcount by Area

| Area | Headcount | Key Roles | Decision Scope |
|------|-----------|-----------|----------------|
| [name] | [N or N–M] | [roles] | [what this area decides] |
| [name] | [N or N–M] | [roles] | [what this area decides] |
| **Total** | **[sum]** | | |
```

Rules:
- At minimum two areas with distinct counts — no single undifferentiated total only
- Decision Scope column satisfies C-08 (decision rights per area)
- Use role names from `.roles/` if available; inferred roles otherwise

---

### SECTION 4 — OPERATING RHYTHM TABLE (required)

Fill in this table immediately after headcount.

```
## Operating Rhythm

| Cadence | Frequency | DRI / Owner | Purpose | Meeting type |
|---------|-----------|-------------|---------|--------------|
| ROB | [weekly/bi-weekly] | [owner] | Review business health, unblock escalations | business review |
| [Shiproom or gate] | [frequency] | [owner] | [gate criteria, ship/no-ship decision] | shiproom |
| [Architecture board or steering] | [frequency] | [owner] | [governance scope, what it decides vs escalates] | governance |
| [additional rows as needed] | | | | |
```

Rules:
- Must include ROB, at least one shiproom/gate, at least one governance meeting
- Three entries is the minimum — more is better if the domain warrants it
- DRI column should reference a role name from `.roles/` where possible

---

### OPTIONAL: COMMITTEE CHARTERS

For each committee listed in Section 4, write a mini-charter:

```
### [Committee name]

**Purpose:** [one sentence]
**Membership:** [roles, not names — who attends by role]
**Decides:** [what decisions this committee makes vs. escalates]
```

Two or more charters with all three fields improves the quality score.

---

ROLES INPUT PROTOCOL

Before filling in any section:
1. Check whether `.roles/` contains role files for {topic} or the domain
2. If found: list roles in the ROLES-LOADED field in Section 2
3. If not found: write "none — using inferred roles" and proceed

Roles found in `.roles/` must appear in at least one of: the org diagram,
the Key Roles column in Section 3, or a committee membership field.

---

FINAL LINE

End the artifact with:

```
Generated by: /org-chart {topic} — {date}
```

---

## V-03 — Role Sequence: Roles-First with Named ROLES-LOADED Step

**axis:** role-sequence
**hypothesis:** Making the `.roles/` read the first named step — before inertia assessment — and requiring the model to produce a ROLES-LOADED list that subsequent sections must reference forces C-03 compliance. If roles exist, they anchor the org design from the start rather than being inserted as flavor after the fact. If roles are absent, the explicit absence statement prevents silent omission. Falsifiable: if C-03 still fails (role names absent from org chart despite being loaded), sequence alone does not fix the integration problem.

---

You are running `/org-chart {topic}`.

---

STEP 1 — READ ROLES

Check `.roles/` for role files relevant to {topic} or the domain.

Produce a ROLES-LOADED block immediately:

```
ROLES-LOADED:
  - [role name] — [one-line orientation from the role file]
  - [role name] — [one-line orientation from the role file]
  (repeat for each role found)
```

If `.roles/` is empty or absent, produce instead:

```
ROLES-NOTE: No .roles/ files found for {topic}. Using inferred roles.
Inferred roles: [list of roles appropriate for the domain]
```

Do not proceed to Step 2 until this block is written.

---

STEP 2 — INERTIA ASSESSMENT

Using the roles loaded in Step 1, assess whether a formal org is warranted.

Write a section titled "Inertia Assessment" containing:

- How the team currently coordinates (informal mechanisms, existing leads)
- What coordination failures the loaded roles are experiencing today
- The flat-team viability threshold for this team type
- An explicit verdict: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED
- One sentence connecting the roles context to the verdict

The loaded roles must inform the assessment — if signal:pm, signal:architect, or
signal:inertia-advocate are loaded, their lens should shape which coordination
failures are highlighted.

Do not write an org diagram until the verdict is written.

---

STEP 3 — ASCII ORG DIAGRAM

Draw the hierarchy. Every named box or node must use a role name from ROLES-LOADED
(or an inferred role name from ROLES-NOTE). Do not introduce role names that were
not established in Step 1.

Minimum requirements:
- At least two levels
- At least two distinct nodes at the top level or second level
- Committees or boards shown as a separate labeled node

---

STEP 4 — HEADCOUNT BY AREA

Produce a table with at minimum two areas. The Key Roles column must reference
role names from ROLES-LOADED or ROLES-NOTE.

| Area | Headcount | Key Roles | Notes |
|------|-----------|-----------|-------|

Include a total row.

---

STEP 5 — OPERATING RHYTHM TABLE

Produce a cadence table covering at minimum:
1. ROB (business review)
2. Shiproom or equivalent gate meeting
3. Governance meeting (architecture board, steering committee, or equivalent)

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|

DRI / Owner should reference a role from ROLES-LOADED where possible.

---

STEP 6 — COMMITTEE CHARTERS (if committees were listed in Step 5)

For each committee or board in the rhythm table, write:

**[Name]**
Purpose: [one sentence]
Membership: [roles from ROLES-LOADED — not personal names]
Decides: [what is in scope for this committee vs. what it escalates]

---

STEP 7 — ARTIFACT OUTPUT

Write all sections to `org-chart.md` in this order:
1. ROLES-LOADED (or ROLES-NOTE)
2. Inertia Assessment
3. ASCII Org Diagram
4. Headcount by Area
5. Operating Rhythm Table
6. Committee Charters (if applicable)

---

FINAL LINE

```
Generated by: /org-chart {topic} — {date}
```

---

## V-04 — Phrasing Register + Inertia Framing: Imperative DO/DO NOT + Inertia Gate

**axis:** phrasing-register + inertia-framing
**hypothesis:** Fully imperative DO/DO NOT register combined with the inertia gate and VERDICT requirement will protect C-01 through C-05 simultaneously. Hard prohibitions (DO NOT draw an org box without a VERDICT; DO NOT produce a rhythm table with fewer than three entries) prevent the most common essential-criterion failures. Falsifiable: if essential pass rate does not improve over single-axis variations, the imperative register adds no incremental value over the gate alone.

---

You are running `/org-chart {topic}`.

---

ROLES — READ FIRST

DO check `.roles/` before writing anything.
DO list every role found in a ROLES-LOADED block at the top of the output.
DO NOT invent role names not found in `.roles/` unless no roles are present.
If no roles are present, DO write: "ROLES-NOTE: No .roles/ files found — using inferred roles."
DO reference at least one loaded role in the org diagram, headcount table, or committee charter.

---

INERTIA GATE — ANSWER BEFORE ANY ORG BOXES

DO write an Inertia Assessment section before the org diagram.
DO NOT skip or abbreviate the inertia section.
DO NOT write an org box as the first section.
DO NOT write "the team is growing" without specifying the headcount or coordination failure.

The Inertia Assessment MUST include:
- Description of current coordination mode
- Flat-team viability threshold (a number or condition, not a platitude)
- VERDICT field: either CAN-OPERATE-FLAT or STRUCTURE-WARRANTED
- Reasoning (one or two sentences, specific to this team and topic)

DO NOT proceed past the Inertia Assessment until VERDICT is written.

If VERDICT is CAN-OPERATE-FLAT:
  DO produce a lightweight coordination model (sync cadence, ownership map) instead of a
  formal org chart.
  DO note the trigger that would change the verdict to STRUCTURE-WARRANTED.
  DO NOT produce a full hierarchical org box for a team that does not warrant structure.

If VERDICT is STRUCTURE-WARRANTED:
  DO proceed to the org diagram and all remaining sections.

---

ASCII ORG BOX

DO draw an ASCII hierarchy after the Inertia Assessment.
DO show at minimum two levels (area leads + sub-teams or roles).
DO NOT produce a flat list of names without hierarchy.
DO NOT draw a single-node diagram (one person is not an org).
DO label committees or boards as distinct nodes — not embedded in a single area.

---

HEADCOUNT BY AREA

DO produce a headcount table immediately after the org diagram.
DO include at minimum two distinct areas with individual counts.
DO NOT produce only a single total with no area breakdown.
DO reference role names from ROLES-LOADED in the Key Roles column.

Required columns:

| Area | Headcount | Key Roles | Decision Scope |
|------|-----------|-----------|----------------|

DO fill in the Decision Scope column for every area row.
DO NOT write "owns the area" — write what kinds of decisions are made at this level
versus escalated upward.

---

OPERATING RHYTHM TABLE

DO produce a cadence table after the headcount section.
DO include at minimum three distinct rows: ROB, a shiproom or gate meeting, and
one governance meeting (architecture board, steering committee, or equivalent).
DO NOT combine two meetings into one row to meet the three-entry minimum.
DO NOT produce a rhythm table with only ROB.

Required columns:

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|

DO reference a role from ROLES-LOADED in the DRI / Owner column where possible.

---

COMMITTEE CHARTERS

DO write a mini-charter for each committee listed in the rhythm table.
Each charter MUST include:
- Purpose: [one sentence]
- Membership: [roles from ROLES-LOADED — not personal names]
- Decides: [what is in this committee's authority vs. what it escalates]

DO NOT write a rhythm table row for a committee and then omit its charter.

---

SECTION ORDER — DO NOT REORDER

DO write sections in this order:
1. ROLES-LOADED (or ROLES-NOTE)
2. Inertia Assessment
3. ASCII Org Diagram
4. Headcount by Area (with Decision Scope column)
5. Operating Rhythm Table
6. Committee Charters

DO NOT reorder sections.
DO NOT omit any of these six sections.

---

FINAL LINE

DO end with exactly:

```
Generated by: /org-chart {topic} — {date}
```

DO NOT emit literal placeholder text in the final line.

---

## V-05 — Lifecycle Emphasis + Output Format: Five-Phase Sequence with Per-Phase Templates

**axis:** lifecycle-emphasis + output-format
**hypothesis:** Naming each phase as a discrete step with its own output contract and charter-element checklist will improve C-06 (committee charters with all three elements: purpose + membership + authority) and C-08 (decision rights per area) because those sections have explicit slots that must be filled before the phase is complete. Combined with lifecycle ordering, the model cannot produce later phases (rhythm, charters) before completing earlier phases (roles, inertia). Falsifiable: if C-06 and C-08 do not improve over V-02, phase gating adds no value over section scaffolding alone.

---

You are running `/org-chart {topic}`.

Complete the following five phases in order. Do not begin a phase until the previous
phase output is written.

---

PHASE 1 — READ ROLES

**Deliverable:** ROLES-LOADED block

Read `.roles/` for role files relevant to {topic} or the domain. Produce:

```
## Roles Input

Source: .roles/{domain}/ (or "absent — using inferred roles")

| Role | Archetype | Orientation (one line) |
|------|-----------|------------------------|
| [name] | [product/technical/challenger/etc.] | [from role file] |
```

If `.roles/` is absent: note it explicitly and list inferred roles in the same
table format with Source marked as "inferred."

Phase 1 complete when: table is written with at least one row.

---

PHASE 2 — INERTIA ASSESSMENT

**Deliverable:** Inertia Assessment section with VERDICT

Before proposing any structure, answer: can this team operate without a formal org?

```
## Inertia Assessment

### Status-quo defense
[Argue the case for doing nothing. What coordination mechanisms exist today?
What is actually working? Reference the inertia-advocate lens: what is the team
doing instead of formalizing? Is that actually worse?]

### Flat-team viability
[State the headcount threshold at which informal coordination fails for this type
of team. Is the team above or below that threshold today?]

### Switching cost
[What does formalizing cost? Reporting overhead, slower decisions, political weight
of titles and reporting lines. Be specific.]

### VERDICT
CAN-OPERATE-FLAT — if the team is below the viability threshold and informal
  coordination is not producing specific failures.
STRUCTURE-WARRANTED — if the team is above threshold or specific coordination
  failures are documented.

Verdict: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]

Trigger for re-assessment: [the headcount, milestone, or workload signal that
would flip this verdict — required regardless of which verdict is chosen]
```

Phase 2 complete when: VERDICT and re-assessment trigger are written.

If VERDICT is CAN-OPERATE-FLAT: proceed to Phase 5 (Operating Rhythm only).
If VERDICT is STRUCTURE-WARRANTED: proceed to Phase 3.

---

PHASE 3 — DESIGN STRUCTURE

**Deliverable:** ASCII Org Diagram + Headcount by Area

Draw the org hierarchy using role names from Phase 1.

```
## Org Structure

[ASCII diagram — at least two levels, at least two top-level or second-level nodes,
committees shown as distinct labeled nodes]
```

Immediately after the diagram, produce the headcount table:

```
## Headcount by Area

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| [name] | [N or N–M] | [roles from Phase 1] | [decisions owned here] | [decisions sent up] |
| [name] | [N or N–M] | [roles from Phase 1] | [decisions owned here] | [decisions sent up] |
| **Total** | **[N]** | | | |
```

The Decides / Escalates split satisfies C-08 (decision rights per area).
At minimum two area rows required.

Phase 3 complete when: diagram and headcount table (with Decides/Escalates) are written.

---

PHASE 4 — DOCUMENT RHYTHMS

**Deliverable:** Operating Rhythm Table

List every recurring meeting. Cover at minimum:
- ROB or business review cadence
- Shiproom or feature-gate meeting
- Governance meeting (architecture board, steering committee, or equivalent)

```
## Operating Rhythm

| Cadence | Frequency | DRI / Owner | Purpose | Type |
|---------|-----------|-------------|---------|------|
| ROB | [freq] | [role] | Review business health, escalations | business-review |
| [Shiproom] | [freq] | [role] | Gate for ship/no-ship decisions | shiproom |
| [Architecture Board] | [freq] | [role] | Technical governance, cross-cutting decisions | governance |
| [additional rows] | | | | |
```

Type column values: business-review, shiproom, governance, planning, other.

Phase 4 complete when: three or more distinct rows are written.

---

PHASE 5 — CHARTER COMMITTEES

**Deliverable:** Mini-charter for each governance meeting in the rhythm table

For every row with Type = governance (and optionally shiproom):

```
### [Committee name]

**Purpose:** [One sentence — what question does this committee answer?]

**Membership:**
  - [role from Phase 1 table] — [why this role attends]
  - [role] — [reason]
  (list all standing members by role, not by name)

**Decides (in-scope):**
  - [decision type 1]
  - [decision type 2]

**Escalates (out-of-scope):**
  - [decision type that goes to a higher body or individual]
```

Charter checklist — all three elements required per committee:
  [ ] Purpose (one sentence, not generic)
  [ ] Membership (roles, not names; at minimum two roles)
  [ ] Decides / Escalates split (at minimum one item each side)

Phase 5 complete when: every governance row has a charter with all three elements checked.

---

ARTIFACT OUTPUT

Collect all phase deliverables into `org-chart.md` in this section order:
1. Roles Input (Phase 1)
2. Inertia Assessment (Phase 2)
3. Org Structure + Headcount by Area (Phase 3)
4. Operating Rhythm (Phase 4)
5. Committee Charters (Phase 5)

---

FINAL LINE

```
Generated by: /org-chart {topic} — {date}
```
