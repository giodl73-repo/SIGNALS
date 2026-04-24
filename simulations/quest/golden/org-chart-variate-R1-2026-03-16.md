---
skill: quest-variate
skill_target: org-chart
date: 2026-03-16
round: R1
rubric_version: v1
status: variate
---

# org-chart Variate — Round 1

**Date:** 2026-03-16
**Skill:** org-chart
**Rubric:** v1 (C-01 through C-10; essential C-01–C-05)
**Round:** R1 — single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

---

## Round 1 Variation Map

| V | Axis | What Changed | Hypothesis |
|---|------|--------------|------------|
| V-01 | inertia-framing | The inertia-advocate role drives the assessment: status-quo defense is written first, switching cost is named, and the VERDICT field must resolve the inertia case — not describe the team's ambition | Grounding the gate in the inertia-advocate's lens (what is the team doing today, and is that actually worse?) produces a more credible C-01 gate than a generic "is structure needed?" prompt, because the model must argue both sides before choosing a verdict |
| V-02 | output-format | All four required outputs are pre-labeled scaffolds with slot constraints; the inertia section gets a fill-in template with a discrete Verdict line; headcount table includes a Decision Scope column | Pre-specifying slot names makes structural omission visible — a missing slot stands out as a gap rather than a natural prose choice; improves C-04, C-05, and C-08 pass rates |
| V-03 | role-sequence | `.roles/` read is Step 1 and produces a typed ROLES-LOADED table; every downstream section contains a role-propagation rule referencing that table | Front-loading role discovery before the inertia assessment ensures loaded roles inform which coordination failures are highlighted — and the propagation rule closes the gap where roles appear once at the top then vanish |
| V-04 | phrasing-register + inertia-framing | Fully imperative DO/DO NOT phrasing throughout; the inertia gate carries explicit prohibition: DO NOT write org boxes before VERDICT; CAN-OPERATE-FLAT verdict prohibits a full hierarchy | Hard prohibitions close the two most common essential gaps (C-01 skipped or written after C-02; C-07 verdict ignored when org is drawn anyway) because the model must satisfy the prohibition before continuing |
| V-05 | lifecycle-emphasis + output-format | Five named phases with typed deliverables and phase-complete conditions; Phase 2 includes a formal status-quo defense sub-section; Phase 5 has a three-element charter checklist that must be ticked before the phase is declared done | Explicit phase-complete conditions prevent partial outputs from being accepted — C-06 (charter with all three elements) and C-09 (concrete re-assessment trigger) require specificity that phase checkboxes enforce |

---

## V-01 — Inertia Framing: Status-Quo Defense Before VERDICT

**axis:** inertia-framing
**hypothesis:** Requiring the model to argue the case for the status quo — what coordination mechanisms exist today and why they might be sufficient — before rendering a verdict produces a more credible C-01 gate. The inertia-advocate role from `.roles/signal/inertia-advocate.md` defines this lens: "the burden of proof is on the feature, not on inertia." If the model cannot name what the team does today, it has not answered the inertia case. Falsifiable: if C-01 pass rate does not improve over a baseline that skips the status-quo defense, framing the gate as an adversarial argument adds no value.

---

You are running `/org-chart {topic}`.

---

INERTIA GATE

The primary competitor to formal org structure is always the status quo: informal coordination,
direct communication, shared channels, ad-hoc ownership. Before drawing any org box, you must
answer whether the status quo is actually worse.

Write an Inertia Assessment section. The assessment has four required parts:

**Part 1 — Status-quo description**
Describe how the team coordinates today. Name the informal mechanisms that exist: which
channels, which recurring standups, which informal leads. Do not assume these are broken.

**Part 2 — Status-quo defense**
Argue the case for doing nothing. Apply the inertia-advocate lens:
- What is the team doing today instead of formal structure, and is that actually worse?
- What is the switching cost of formalizing — reporting overhead, title politics, slower
  decisions?
- What coordination failures has the team NOT experienced that might justify continuing
  informal operation?

**Part 3 — Flat-team viability threshold**
Name the headcount or complexity threshold at which informal coordination fails for this
type of team. State whether the team is currently above or below that threshold.

**Part 4 — VERDICT**
Choose one: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`

Write the verdict as a discrete labeled field:

```
VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]

Reasoning: [One or two sentences. Must name the specific coordination failure or threshold
condition that determined the verdict. "The team is growing" is not acceptable — state
what failure mode is occurring or what threshold has been crossed.]
```

Do not write an org diagram or any downstream section until VERDICT is written.

If VERDICT is CAN-OPERATE-FLAT:
  The output should be a lightweight coordination model only: an ownership map, a sync
  cadence, and the trigger that would flip the verdict to STRUCTURE-WARRANTED.
  Do not produce a formal ASCII hierarchy.

If VERDICT is STRUCTURE-WARRANTED:
  Proceed to the sections below.

---

ROLES INPUT

Check `.roles/` for role files relevant to {topic}.

If roles exist, write a ROLES-LOADED block before the org diagram:
```
ROLES-LOADED: [role-1], [role-2], ...
```

If no roles exist, write:
```
ROLES-NOTE: No .roles/ files found — using inferred roles: [list]
```

---

ASCII ORG DIAGRAM

Draw an ASCII hierarchy showing at minimum two levels and two distinct nodes.
Label committees or boards as separate nodes — not embedded in a single area's subtree.

---

HEADCOUNT BY AREA

| Area | Headcount | Key Roles |
|------|-----------|-----------|
| ...  | N or N–M  | role names |
| **Total** | **N** | |

At minimum two area rows with distinct counts.

---

OPERATING RHYTHM TABLE

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|

Required entries (minimum three):
1. ROB or business review
2. Shiproom or feature-gate meeting
3. Governance meeting (architecture board, steering committee, or equivalent)

Do not combine two meetings into one row.

---

ARTIFACT OUTPUT

Write the complete artifact to `org-chart.md` in this section order:
1. Inertia Assessment (with VERDICT)
2. ROLES-LOADED (or ROLES-NOTE) + ASCII Org Diagram
3. Headcount by Area
4. Operating Rhythm Table

End with:
```
Generated by: /org-chart {topic} — {date}
```

---

## V-02 — Output Format: Section Scaffolds with Required Slots

**axis:** output-format
**hypothesis:** Providing four fill-in-the-blank section scaffolds with named slot constraints makes structural omission visible and forces completeness. When the scaffold already contains the headcount table header (with a Decision Scope column) and the rhythm table header (with three required meeting types pre-labeled), the model cannot reduce those sections to prose — the slots must be filled. Falsifiable: if section omission continues despite the scaffold, the model is ignoring structural format rather than needing clearer instructions.

---

You are running `/org-chart {topic}`.

Generate an org structure for the topic domain. Use the four section templates below.
Fill in every slot. Do not omit any template section or leave a slot blank.

---

### SECTION 1 — INERTIA ASSESSMENT (required before all other sections)

```
## Inertia Assessment

Current coordination mode:
[How does the team coordinate today? Name the channels, meetings, or informal leads
that exist right now — before any formal structure.]

Flat-team threshold:
[At what headcount or complexity level does this type of team outgrow informal
coordination? State a number or a named condition, not a platitude.]

Current position:
[below threshold / at threshold / above threshold]

VERDICT: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]

Reasoning:
[One to two sentences. Must be specific: name the failure mode or threshold
condition. "The team needs structure" does not satisfy this slot.]

Re-assessment trigger:
[The headcount number, milestone, or workload signal that would flip or revisit
this verdict. Required regardless of which verdict is chosen.]
```

---

### SECTION 2 — ROLES INPUT + ASCII ORG DIAGRAM (required)

```
## Org Structure

ROLES-LOADED: [comma-separated list of role names from .roles/, or
"none — using inferred roles: [list]" if .roles/ is absent]

[ASCII org diagram]
Requirements:
  - At least two levels (area leads + sub-teams or roles)
  - At least two distinct nodes at the top level or second level
  - Committees or boards shown as a separate labeled node or layer
```

---

### SECTION 3 — HEADCOUNT BY AREA (required)

```
## Headcount by Area

| Area | Headcount | Key Roles | Decision Scope |
|------|-----------|-----------|----------------|
| [name] | [N or N–M] | [role names] | [what this area decides vs escalates] |
| [name] | [N or N–M] | [role names] | [what this area decides vs escalates] |
| **Total** | **[N]** | | |
```

Slot rules:
- At minimum two area rows
- Key Roles must reference names from ROLES-LOADED (or inferred roles)
- Decision Scope must name a specific decision class — not "owns the area"

---

### SECTION 4 — OPERATING RHYTHM TABLE (required)

```
## Operating Rhythm

| Cadence | Frequency | DRI / Owner | Purpose | Meeting Type |
|---------|-----------|-------------|---------|--------------|
| ROB | [weekly/bi-weekly] | [owner role] | Review business health, unblock escalations | business-review |
| [Shiproom name] | [frequency] | [owner role] | [gate criteria, ship/no-ship decision] | shiproom |
| [Architecture Board or Steering] | [frequency] | [owner role] | [governance scope] | governance |
| [additional rows as needed] | | | | |
```

Slot rules:
- ROB row is pre-labeled — fill in Frequency, DRI/Owner, Purpose
- Shiproom row is pre-labeled — fill in name, details
- Governance row is pre-labeled — fill in name, details
- Add rows beyond the three minimums if the domain warrants it
- Do not merge two meetings into one row

---

### SECTION 5 — COMMITTEE CHARTERS (recommended for each governance meeting)

For each row with Meeting Type = governance (or shiproom), write:

```
### [Committee name]

**Purpose:** [one sentence — what question does this body answer?]
**Membership:** [roles from ROLES-LOADED — not personal names; at minimum two roles]
**Decides:** [what is in this committee's authority]
**Escalates:** [what this committee sends to a higher body or individual]
```

All four fields required per charter. "Makes decisions" without scope does not satisfy Decides.

---

ROLES PROTOCOL

Before filling in any section:
1. Check `.roles/` for files relevant to {topic} or the domain
2. If found: populate ROLES-LOADED in Section 2
3. If not found: write "none — using inferred roles" and list the inferred roles
4. Role names from ROLES-LOADED must appear in at least two sections

---

End the artifact with:
```
Generated by: /org-chart {topic} — {date}
```

---

## V-03 — Role Sequence: Roles-First with Propagation Rule

**axis:** role-sequence
**hypothesis:** Making `.roles/` the first named action — producing a typed ROLES-LOADED table before inertia assessment begins — anchors the org design in real roles rather than generic titles. The propagation rule (role names from Step 1 must appear in at least two downstream sections) closes the gap where roles are listed at the top and then replaced by "Team Lead" and "Engineer" in the actual org boxes. Falsifiable: if C-10 (role names in two or more sections) still fails despite the propagation rule, the model is treating the rule as advisory rather than structural.

---

You are running `/org-chart {topic}`.

---

STEP 1 — READ ROLES (do this before writing anything else)

Check `.roles/` for role files relevant to {topic} or the domain.

Produce a ROLES-LOADED table:

```
## Roles Input

Source: .roles/{domain}/ [or "absent — using inferred roles"]

| Role | Archetype | Orientation |
|------|-----------|-------------|
| [name] | [product/technical/challenger/...] | [one-line from role file] |
```

If `.roles/` is absent or contains no relevant files, mark Source as
"absent — using inferred roles" and populate the table with roles appropriate
for the domain.

Do not proceed to Step 2 until this table is written.

**Propagation rule:** Every role name in this table must appear in at least two of
the following downstream sections: org diagram node labels, headcount Key Roles column,
committee membership list, rhythm DRI/Owner column. Do not replace role names with
generic titles ("Team Lead," "Engineer") in any section.

---

STEP 2 — INERTIA ASSESSMENT

Using the roles loaded in Step 1, assess whether a formal org is warranted.

Write a section titled `## Inertia Assessment` containing:

- How the team currently coordinates (informal mechanisms — name them specifically)
- What coordination failures the loaded roles are experiencing today
  (if signal:pm, signal:architect, or signal:inertia-advocate are loaded, their
  orientation should inform which failures are highlighted)
- The flat-team viability threshold for this team type (a number or named condition)
- An explicit `VERDICT: CAN-OPERATE-FLAT` or `VERDICT: STRUCTURE-WARRANTED`
- One sentence connecting the role context and coordination analysis to the verdict

Do not proceed to Step 3 until VERDICT is written.

If VERDICT is CAN-OPERATE-FLAT:
  Proceed directly to Step 5 — produce a coordination model, not a hierarchy.
  Note the trigger that would change the verdict.

---

STEP 3 — ASCII ORG DIAGRAM

Draw the hierarchy. Every named node must use a role name from Step 1's ROLES-LOADED table.
Do not introduce role names not established in Step 1.

Minimum:
- Two levels of hierarchy
- Two distinct nodes at the top level or second level
- Committees shown as a separate labeled node

---

STEP 4 — HEADCOUNT BY AREA

Produce a table with at minimum two area rows. Key Roles column must reference role names
from Step 1 — not generic titles.

| Area | Headcount | Key Roles | Decision Scope |
|------|-----------|-----------|----------------|

Include a totals row. Decision Scope column: name what each area decides vs. escalates
(not "owns the area").

---

STEP 5 — OPERATING RHYTHM TABLE

Produce a cadence table covering at minimum:
1. ROB (business review)
2. Shiproom or feature-gate meeting
3. Governance meeting

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|

DRI / Owner must reference a role from Step 1's table where possible.

---

STEP 6 — COMMITTEE CHARTERS

For each governance meeting in the rhythm table, write:

```
### [Name]
Purpose: [one sentence]
Membership: [roles from Step 1 table — not personal names; minimum two roles]
Decides: [what is in scope for this committee]
Escalates: [what goes to a higher body]
```

---

STEP 7 — ARTIFACT OUTPUT

Write all steps to `org-chart.md` in this order:
1. Roles Input (Step 1)
2. Inertia Assessment (Step 2)
3. ASCII Org Diagram (Step 3)
4. Headcount by Area (Step 4)
5. Operating Rhythm Table (Step 5)
6. Committee Charters (Step 6)

End with:
```
Generated by: /org-chart {topic} — {date}
```

---

## V-04 — Phrasing Register + Inertia Framing: Imperative DO/DO NOT with Hard Gate

**axis:** phrasing-register + inertia-framing
**hypothesis:** Fully imperative DO/DO NOT phrasing combined with hard prohibitions on skipping the inertia gate will close the two most common essential failures: (1) C-01 reduced to a generic paragraph without a VERDICT field, and (2) C-07 violated when a CAN-OPERATE-FLAT verdict is followed by a full org hierarchy anyway. The prohibitions are falsifiable: if the model still skips the VERDICT or draws a full org chart under CAN-OPERATE-FLAT, then imperative register does not constrain output structure.

---

You are running `/org-chart {topic}`.

---

ROLES — READ FIRST

DO check `.roles/` before writing anything.
DO list every role found in a ROLES-LOADED block.
DO NOT invent role names that contradict roles already defined in `.roles/`.
If no role files exist: DO write "ROLES-NOTE: No .roles/ files found — using inferred roles: [list]."
DO reference at least one loaded role name in each of: the org diagram, the headcount table, and the rhythm table.

---

INERTIA GATE — MUST COMPLETE BEFORE ANY ORG BOXES

DO write an `## Inertia Assessment` section as the first output section.
DO NOT write an org diagram as the first section.
DO NOT skip the inertia assessment or replace it with a general introduction.

The Inertia Assessment MUST include ALL of these — missing any one fails the gate:
1. Current coordination mode (specific — name the meetings, channels, or informal leads)
2. Status-quo defense (argue the case for doing nothing — what is working today?)
3. Flat-team viability threshold (a number or named condition — not "when the team grows")
4. `VERDICT: CAN-OPERATE-FLAT` or `VERDICT: STRUCTURE-WARRANTED` as a discrete labeled field
5. Reasoning (one or two sentences, tied to a specific failure mode or threshold)

DO NOT write "the team is growing" as reasoning.
DO NOT write a VERDICT without a Reasoning field.
DO NOT proceed past the Inertia Assessment until VERDICT is written.

If VERDICT is CAN-OPERATE-FLAT:
  DO produce a lightweight coordination model (ownership map + sync cadence).
  DO note the specific trigger that would flip the verdict to STRUCTURE-WARRANTED.
  DO NOT produce a full hierarchical org box for a flat team.
  DO NOT draw a formal ASCII hierarchy when the verdict is CAN-OPERATE-FLAT.

If VERDICT is STRUCTURE-WARRANTED:
  DO proceed to all remaining sections.

---

ASCII ORG DIAGRAM

DO draw an ASCII hierarchy after the Inertia Assessment.
DO show at minimum two levels (area leads + sub-teams or named roles).
DO label committees or boards as distinct nodes — not embedded inside a single area.
DO NOT produce a flat list of names without structural hierarchy.
DO NOT draw a single-node diagram (one person is not an org).

---

HEADCOUNT BY AREA

DO produce a headcount table immediately after the org diagram.
DO include at minimum two distinct area rows with individual counts.
DO NOT produce only a single aggregate total with no area breakdown.
DO fill in the Decision Scope column for every area row.
DO NOT write "owns the area" in Decision Scope — write what decision class is made here
    versus escalated upward.

Required table format:

| Area | Headcount | Key Roles | Decision Scope |
|------|-----------|-----------|----------------|

DO include a totals row.

---

OPERATING RHYTHM TABLE

DO produce a cadence table after the headcount section.
DO include at minimum three distinct rows.
DO NOT combine two meetings into one row to reach the minimum.
DO NOT produce a rhythm table with only ROB.

Required meeting types (one row each):
  - ROB or business review
  - Shiproom or feature-gate meeting
  - Governance meeting (architecture board, steering committee, or equivalent)

Required columns:
| Cadence | Frequency | DRI / Owner | Purpose |

DO reference a role from ROLES-LOADED in DRI / Owner where possible.

---

COMMITTEE CHARTERS

DO write a mini-charter for every committee or board in the rhythm table.
DO include all three elements per charter:
  - Purpose: one sentence
  - Membership: roles from ROLES-LOADED — not personal names; minimum two roles
  - Decides / Escalates: at minimum one item on each side
DO NOT write a rhythm table row for a committee and then omit its charter.

---

SECTION ORDER — DO NOT REORDER

DO write sections in this order:
1. ROLES-LOADED (or ROLES-NOTE)
2. Inertia Assessment (with VERDICT)
3. ASCII Org Diagram
4. Headcount by Area (with Decision Scope column)
5. Operating Rhythm Table
6. Committee Charters

DO NOT omit any of these six sections (when VERDICT is STRUCTURE-WARRANTED).
DO NOT reorder sections.

---

End with exactly:
```
Generated by: /org-chart {topic} — {date}
```
DO NOT emit placeholder text in the final line.

---

## V-05 — Lifecycle Emphasis + Output Format: Five-Phase Sequence with Phase-Complete Conditions

**axis:** lifecycle-emphasis + output-format
**hypothesis:** Naming each phase as a discrete step with an explicit phase-complete condition prevents partial outputs. C-06 (committee charters with all three elements: purpose + membership + decides/escalates) and C-09 (concrete re-assessment trigger) require specificity that is easy to skip in a flat prompt — but hard to skip when Phase 5 has a three-item checklist that must be satisfied before the phase is declared complete. The status-quo defense sub-section in Phase 2 ensures the inertia-advocate lens is applied. Falsifiable: if C-06 and C-09 do not improve over V-02, phase gating adds no value over section scaffolding alone.

---

You are running `/org-chart {topic}`.

Complete the following five phases in order. Do not begin a phase until the previous
phase's deliverable is written and its phase-complete condition is satisfied.

---

### PHASE 1 — READ ROLES

**Deliverable:** ROLES-LOADED table
**Phase-complete condition:** Table is written with at least one row.

Check `.roles/` for role files relevant to {topic} or the domain.

```
## Roles Input

Source: .roles/{domain}/ [or "absent — using inferred roles"]

| Role | Archetype | Orientation |
|------|-----------|-------------|
| [name] | [archetype from role file] | [one-line orientation from role file] |
```

If `.roles/` is absent: mark Source as "absent — using inferred roles" and
populate the table with roles appropriate for the domain.

**Propagation contract:** Role names in this table must appear in at least two
of the following: org diagram nodes, headcount Key Roles column, committee membership,
rhythm DRI/Owner column.

---

### PHASE 2 — INERTIA ASSESSMENT

**Deliverable:** Inertia Assessment section with VERDICT and re-assessment trigger
**Phase-complete condition:** VERDICT field is written AND re-assessment trigger is specific.

Before proposing any structure, answer: can this team operate without a formal org?

```
## Inertia Assessment

### Status-quo defense
[Argue the case for doing nothing. Using the inertia-advocate lens: what coordination
mechanisms exist today? What is working? What would the team lose by formalizing?
Name the switching cost (reporting overhead, title weight, decision latency).]

### Coordination failures
[What is breaking down that the status quo cannot fix? Name specific failure modes:
cross-area dependencies that have no owner, escalation paths that are unclear, work
that falls into gaps between informal leads. If nothing is breaking down, the verdict
should be CAN-OPERATE-FLAT.]

### Flat-team threshold
[The headcount or complexity level at which informal coordination fails for this type
of team. Is the team above or below that threshold today?]

### VERDICT
[Choose one: CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]

Verdict: [CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]

Re-assessment trigger: [The specific headcount number, milestone event, or workload
signal that would flip or revisit this verdict. "When the team grows" does not satisfy
this field — name a number, a failure threshold, or a named condition.]
```

**Phase-complete condition check:**
- [ ] VERDICT field is written (not embedded in prose)
- [ ] Re-assessment trigger names a specific number, event, or failure condition

If VERDICT is CAN-OPERATE-FLAT: proceed to Phase 4 only (operating rhythm / coordination model).
If VERDICT is STRUCTURE-WARRANTED: proceed to Phase 3.

---

### PHASE 3 — DESIGN STRUCTURE

**Deliverable:** ASCII Org Diagram + Headcount by Area with Decides/Escalates
**Phase-complete condition:** Diagram has two or more levels; headcount table has two or more area rows; Decides and Escalates columns are populated.

Draw the hierarchy using role names from Phase 1.

```
## Org Structure

[ASCII org diagram]
Requirements:
  - At least two levels
  - At least two distinct nodes
  - Committees shown as separate labeled nodes
  - Node labels use role names from Phase 1 table
```

Immediately after the diagram:

```
## Headcount by Area

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| [name] | [N or N–M] | [roles from Phase 1] | [decision class owned here] | [decisions sent up] |
| [name] | [N or N–M] | [roles from Phase 1] | [decision class owned here] | [decisions sent up] |
| **Total** | **[N]** | | | |
```

Decides and Escalates split satisfies C-08. At minimum one specific decision class per row.
"Owns the area" does not satisfy the Decides column.

---

### PHASE 4 — DOCUMENT RHYTHMS

**Deliverable:** Operating Rhythm table with three or more distinct rows
**Phase-complete condition:** ROB row, shiproom row, and governance row are each present as distinct rows.

```
## Operating Rhythm

| Cadence | Frequency | DRI / Owner | Purpose | Type |
|---------|-----------|-------------|---------|------|
| ROB | [freq] | [role from Phase 1] | Review business health, unblock escalations | business-review |
| [Shiproom name] | [freq] | [role from Phase 1] | Gate for ship/no-ship decisions | shiproom |
| [Governance name] | [freq] | [role from Phase 1] | [governance scope, what it decides vs escalates] | governance |
| [additional rows] | | | | |
```

Type column values: business-review, shiproom, governance, planning, other.
DRI / Owner references a role from Phase 1 table.

---

### PHASE 5 — CHARTER COMMITTEES

**Deliverable:** Mini-charter for each governance (and optionally shiproom) row
**Phase-complete condition:** Every governance row has a charter with all three elements checked.

For each governance row in the Phase 4 rhythm table:

```
### [Committee name]

**Purpose:** [One sentence — what question does this body answer?]

**Membership:**
  - [role from Phase 1 table] — [why this role attends]
  - [role] — [reason]
  (list standing members by role, not by name; minimum two roles)

**Decides:**
  - [specific decision type 1]
  - [specific decision type 2]

**Escalates:**
  - [decision type that goes to a higher body or individual]
```

**Charter checklist (required for each governance committee):**
- [ ] Purpose: one sentence, not generic
- [ ] Membership: minimum two roles from Phase 1 table, not personal names
- [ ] Decides: at minimum one specific decision type
- [ ] Escalates: at minimum one item

Phase 5 is complete when every governance row has a charter with all four checklist items marked.

---

### ARTIFACT OUTPUT

Collect all phase deliverables into `org-chart.md` in this section order:
1. Roles Input (Phase 1)
2. Inertia Assessment (Phase 2)
3. Org Structure + Headcount by Area (Phase 3, if STRUCTURE-WARRANTED)
4. Operating Rhythm (Phase 4)
5. Committee Charters (Phase 5)

End with:
```
Generated by: /org-chart {topic} — {date}
```

---

*Generated by: /quest:variate org-chart R1 — 2026-03-16*
