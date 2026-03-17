---
skill: quest-variate
skill_target: org-chart
date: 2026-03-16
round: R8
rubric_version: v8
status: variate
---

# org-chart Variate — Round 8

**Date:** 2026-03-16
**Skill:** org-chart
**Rubric:** v8 (C-01 through C-25; C-25 added from V-03/R7 finding)
**Round:** R8 — single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

**R7 ceiling:** V-03/R7 is the first design to combine all four structural features — 4-part
inertia with sequencing guard, mechanism-reason count, ORG-ELEMENT REGISTER with inline
category-schema table, and typed APW citation syntax — in a single variation. It earns all
C-09 through C-24 (16 criteria, 99.4 under v8). It fails C-25: all compliance directives
are phrased descriptively ("by convention," "the purpose is to serve as") rather than
imperatively. C-25 is the first criterion blocked by directive framing rather than structural
omission. Score ceiling at R7: 99.4 (16/17).

**R8 target:** Produce the first 17/17 run by adding imperative-mode directives to V-03/R7's
complete structural synthesis. C-25 requires at least one DO NOT / MUST / REQUIRED directive
for each of the three compliance behaviors: guard enforcement, register construction, and
typed citation format. Three questions drive R8:

1. Does **targeted imperative injection** — replacing only the guard, register, and citation
   directives with imperative mode while leaving the rest of V-03/R7 conversational — earn
   C-25 without disturbing the 16/17 pass pattern? (V-01/R8)
2. Does **full imperative conversion** of all directives in V-03/R7 earn C-25 without
   compressing essential output quality? (V-02/R8)
3. Does **isolated enforcement block injection** — adding labeled ENFORCEMENT blocks at
   compliance points while leaving surrounding prose conversational — satisfy C-25's
   "imperative mode" requirement? (V-03/R8)

V-04/R8 combines targeted imperative conversion (V-01) with V-01/R7's two-step count-
verification protocol, adding a second reliability layer for C-23. V-05/R8 adds a MUST-
PRECEDE gate to the register section over V-02/R8's full-imperative base, testing whether
structural gating over imperative language improves or over-constrains output.

---

## Round 8 Variation Map

| V | Axis | What Changed vs V-03/R7 | Hypothesis |
|---|------|-------------------------|------------|
| V-01 | phrasing register (targeted imperative injection) | V-03/R7 base. The three compliance behaviors — guard emit, register construction, typed citation format — have their conversational explanations augmented with appended imperative directives. All other prose remains conversational. Minimal diff from V-03/R7. | C-25 requires at least one DO NOT / MUST / REQUIRED per compliance behavior. Appending imperative directives immediately after the conversational explanations satisfies the framing check without restructuring the prompt. All C-09-C-24 behaviors are preserved from V-03/R7. Predicted: 17/17. |
| V-02 | phrasing register (full imperative conversion) | V-03/R7 structure with ALL descriptive/conversational framing replaced by imperative DO/DO-NOT style. Every section that used "the purpose is," "after writing," "aim for" becomes "DO," "DO NOT," "MUST." Full alignment with the V-01/R6 and V-01/R7 directive style. | Full conversion eliminates descriptive framing entirely. C-25 passes by construction. Risk: all-imperative prompts may feel more mechanical and produce slightly compressed output (fewer explanatory connectives). If essential criteria hold, full imperative is the most reliable baseline. Predicted: 17/17. |
| V-03 | phrasing register (enforcement block injection) | V-03/R7 conversational prose is preserved verbatim. After each compliance directive, an isolated labeled block is injected: `[ENFORCEMENT: ...]` containing the imperative DO NOT / MUST phrasing. The enforcement blocks are visually distinct from the surrounding prose. | C-25 requires imperative framing to be present in the directive layer; it does not require every directive to be imperative. Isolated enforcement blocks supply the required imperative framing while keeping the explanatory prose readable. If C-25 evaluators require inline imperative framing (not blocked), this may fail. Predicted: 17/17 if block injection counts; 16/17 if inline integration is required. |
| V-04 | phrasing register + inertia framing (targeted imperative + two-step count protocol) | V-01/R8 targeted imperative conversion plus V-01/R7's two-step count-check protocol: the prompt directs the model to explicitly count the numbered reasons in Case for Staying Flat, verify the count is at least two, and only then substitute N and emit the separator. This strengthens C-23 reliability beyond V-03/R7's single-step substitution. | V-03/R7 passed C-23 via single-step `{N}` substitution. The two-step protocol guards against the premature-guard failure mode (guard emitted before all reasons are written). Combining with targeted imperative conversion produces C-25 without restructuring. Predicted: 17/17 with higher C-23 confidence than V-01/R8. |
| V-05 | phrasing register + output format (full imperative + MUST-PRECEDE register gate) | V-02/R8 full-imperative base plus an explicit MUST-PRECEDE gate in the register section: after the register block, a labeled gate directive states "MUST NOT proceed to Org Evolution Roadmap until the register block above is complete and all four category entries are populated." Tests whether structural gating reinforces C-21 reliability in the full-imperative architecture. | Structural gates were effective in V-04/R5 (section-completion gates). Adding a MUST-PRECEDE gate to the register in an already-imperative prompt tests for over-constraint: if the gate causes the model to produce a truncated register (satisfying the gate but losing element completeness), C-21 degrades. If the gate improves C-21 completion rate, V-05 is the preferred production design. Predicted: 17/17. |

---

## V-01 — Phrasing Register: Targeted Imperative Injection

**axis:** phrasing register (minimal: conversational prose preserved; imperative directives
appended at the three C-25 compliance points — guard enforcement, register construction,
typed citation format)
**hypothesis:** V-03/R7 produced all four structural behaviors with conversational framing,
passing C-09 through C-24 (99.4). It failed C-25 because no DO NOT / MUST / REQUIRED
directive appeared for the three compliance behaviors. V-01/R8 appends an imperative
directive immediately after each conversational explanation — preserving V-03/R7's prose
context while adding the framing required for C-25. No structural change from V-03/R7.
C-09 through C-24 pass pattern expected to hold. C-25 PASS predicted.
Expected: 17/17.

---

You are running `/org-chart {topic}`.

---

ROLES — READ FIRST

Before writing anything else, check `.craft/roles/` for existing role definitions. If role
files are present, produce a ROLES-LOADED block listing each role name and a one-line
description drawn from the role file. If no role files are found, produce a ROLES-NOTE block
that says so explicitly and lists the inferred roles you will use. The roles block is the
first thing in the document; no other content appears before it.

Role files found:
```
ROLES-LOADED:
  - [role name] — [one-line description from role file]
```

No role files found:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] — [description]
```

---

INERTIA ASSESSMENT — FOUR SUB-SECTIONS, STEELMAN FIRST

The inertia assessment appears before any org diagrams. The purpose is to honestly evaluate
whether the team needs a formal structure at all, rather than jumping to org design. It is
organized into four sub-sections in sequence.

**Sub-section 1 — Case for Staying Flat**

This sub-section makes the strongest possible case for not introducing formal org structure.
It presents numbered reasons, each of which names a specific, observable mechanism — a
communication channel, an informal lead role, a recurring cadence, a shared artifact. Reasons
that assert team culture or communication quality without naming a specific mechanism are
too weak to count.

Aim for at least two numbered reasons before moving on. Both reasons name specific mechanisms
that currently work.

```
### Case for Staying Flat

1. [A specific mechanism that is currently working — name it concretely]
2. [A second specific mechanism that is currently working — name it concretely]
(at least two mechanisms are needed before this sub-section closes)
```

When at least two numbered mechanism reasons have been written, this sub-section is complete.
By convention, close it with a labeled boundary line before beginning the inventory:

```
--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. How We Coordinate Today begins.] ---
```

Before writing this boundary line, count the numbered reasons above and use that count as N.
The boundary line marks the end of the steelman and the beginning of the coordination
inventory that follows.

**ENFORCEMENT — GUARD:** DO NOT EMIT the `--- [FLAT-CASE-CLOSED: ...]` separator line
before at least two numbered mechanism reasons exist in Case for Staying Flat. DO NOT begin
Sub-section 2 until this separator line has been written.

**Sub-section 2 — How We Coordinate Today**

This sub-section inventories the coordination patterns in active use. It catalogs the
channels, cadences, informal roles, and artifacts that currently exist — adding context
(frequency, participants, artifacts produced) to the picture the reasons above sketched.
It does not re-list the numbered reasons from Sub-section 1; it adds depth.

```
### How We Coordinate Today

[Catalog of coordination patterns: meetings, shared documents, escalation paths, informal
roles — named specifically with frequency and participants where known]
```

**Sub-section 3 — Rebuttal**

This sub-section names the coordination failure that the current flat-team case cannot
answer: a specific blocked decision, missed SLA, time-zone gap, knowledge silo, or
roadmap conflict. "The team is growing" is not a sufficient failure mode; it must name
what breaks.

```
### Rebuttal

[The specific coordination failure that the flat case cannot handle]
```

**Sub-section 4 — VERDICT and Re-assessment Trigger**

The verdict is one of two outcomes: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED. A reasoning
sentence connects the steelman reasons, the coordination inventory, and the rebuttal to the
verdict. The verdict is followed immediately by a re-assessment trigger that names a concrete
condition — a headcount threshold, a coordination-failure signal, or a milestone — at which
this verdict would be revisited. "Revisit as the team grows" is not a sufficient trigger.

```
### VERDICT

[CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]

Reasoning: [one or two sentences connecting sub-sections 1, 2, and 3 to the verdict]

Re-assessment trigger: [a specific condition, e.g., "when headcount exceeds 12" or
"when the on-call rotation spans more than two areas" or
"when the first external SLA is signed"]
```

---

ASCII ORG DIAGRAM

After the inertia assessment, draw an ASCII hierarchy showing the proposed structure.
The diagram shows at minimum two levels — a top level and at least one level below it —
with at minimum two distinct nodes. Committees appear as labeled nodes, not embedded in
an area. Role names come from the ROLES-LOADED or ROLES-NOTE block; do not introduce
names that did not appear there.

---

HEADCOUNT BY AREA

After the org diagram, produce a headcount table with five columns: Area, Headcount, Key
Roles, Decides, and Escalates. The Decides and Escalates columns are separate; a single
"Decision Scope" column does not satisfy this requirement. Each Decides cell names the
decision types owned at this level. Each Escalates cell names the decision types referred
upward and identifies the destination role or forum by name.

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| [name] | [N or N-M] | [roles] | [decisions owned here] | [decisions escalated — name destination] |
| [name] | [N or N-M] | [roles] | [decisions owned here] | [decisions escalated — name destination] |
| **Total** | **[N]** | | | |

At minimum two area rows with individual headcount counts; a single total without area
breakdown does not satisfy this section.

---

OPERATING RHYTHM TABLE

After the headcount section, produce a cadence table. The table covers at minimum three
distinct meetings: the ROB, a shiproom or ship gate, and a governance meeting such as an
architecture board. Two meetings do not belong in the same row. The DRI / Owner column
references a role from ROLES-LOADED where possible.

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|

---

COMMITTEE CHARTERS

For each governance meeting in the rhythm table, write a charter with four fields: Purpose
(one sentence), Membership (roles from ROLES-LOADED, not personal names), Decides (decision
types in scope), and Escalates (decision types referred upward, naming the destination role
or forum). The charter section is not optional; a rhythm table row without a corresponding
charter is incomplete.

```
### [Committee name]

**Purpose:** [one sentence]
**Membership:** [roles — at minimum two]
**Decides:** [decision types in scope]
**Escalates:** [decisions referred upward — name the destination]
```

---

ORG-ELEMENT REGISTER

Before the Anti-Pattern Watch begins, produce a named register block that catalogs the
output elements available for citation. The register's purpose is to serve as the lookup
source for the watch section — it makes citations traceable rather than recalled.

The register opens with a schema table defining the category codes, then lists the actual
elements from this document under each category.

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
    - [DRI role]
    (all DRI roles from the Rhythm Table)
```

**ENFORCEMENT — REGISTER:** MUST produce this ORG-ELEMENT REGISTER block immediately after
Committee Charters. DO NOT proceed to Org Evolution Roadmap until all four category entries
(cat-1 through cat-4) are populated with named elements from the sections above.

---

ORG EVOLUTION ROADMAP

After Committee Charters and the register, produce an evolution roadmap that describes how
the structure should change as the team grows. The roadmap is a table with at minimum two
rows, each naming a trigger and a structural response. The two rows address categorically
different trigger types: the first is a headcount threshold; the second comes from a
different category — a workload signal, structural symptom, or milestone event. Two
headcount numbers at different values are one trigger dimension, not two.

```
## Org Evolution Roadmap

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| [headcount threshold — e.g., "when headcount reaches 15"] | [Named change] | [type] |
| [workload signal, structural symptom, or milestone — not a second headcount number] | [Named change] | [type] |
```

---

ANTI-PATTERN WATCH

After the Org Evolution Roadmap, produce an Anti-Pattern Watch table. The "Why It Applies
Here" column draws from the ORG-ELEMENT REGISTER above using typed citation syntax:

  `[element name] (cat-N) — [one sentence]`

The element name is copied exactly from the register; the cat-N code comes from the schema
table in the register.

**ENFORCEMENT — CITATIONS:** MUST open each "Why It Applies Here" cell with typed citation
syntax `[element name] (cat-N)`. DO NOT write a "Why It Applies Here" cell that names an
element in prose without the typed syntax. DO NOT use a cat-N code that does not match the
category schema defined in the ORG-ELEMENT REGISTER.

```
## Anti-Pattern Watch

| Anti-Pattern | Why It Applies Here | Mitigation |
|--------------|---------------------|------------|
| [Named anti-pattern] | `[element name] (cat-N) — [one sentence of specific relevance]` | [Mitigation] |
| [Second anti-pattern] | `[element name] (cat-N) — [one sentence]` | [Mitigation] |
```

At minimum two anti-pattern rows, each with a typed citation from the register.

---

SECTION ORDER

The document is organized in this sequence:
1. ROLES-LOADED or ROLES-NOTE
2. Inertia Assessment (Case for Staying Flat [boundary line] / How We Coordinate Today / Rebuttal / VERDICT)
3. ASCII Org Diagram
4. Headcount by Area
5. Operating Rhythm Table
6. Committee Charters
7. ORG-ELEMENT REGISTER
8. Org Evolution Roadmap
9. Anti-Pattern Watch

---

FINAL LINE

End with exactly:

```
Generated by: /org-chart {topic} — {date}
```

---

## V-02 — Phrasing Register: Full Imperative Conversion

**axis:** phrasing register (complete conversion: all conversational/descriptive directives
in V-03/R7 replaced with DO/DO-NOT/MUST imperative mode throughout)
**hypothesis:** V-03/R7's conversational framing produced all four structural behaviors
but failed C-25. A full conversion to imperative style — matching the V-01/R6 and V-01/R7
lineage — eliminates descriptive framing entirely. C-25 passes by construction (every
directive is imperative). Risk: full imperative may produce more mechanical output with
slightly compressed explanatory connectives, but all structural requirements hold. The
primary verification is whether essential criteria (C-01 through C-05) are unchanged.
Expected: 17/17.

---

You are running `/org-chart {topic}`.

---

ROLES — READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a ROLES-LOADED block at the top of the output.
DO NOT invent role names unless no roles files are found.

If roles are found:
```
ROLES-LOADED:
  - [role name] — [one-line description from role file]
```

If absent:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] — [description]
```

DO NOT write any other section until this block exists.

---

INERTIA ASSESSMENT — FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.
DO NOT write an org diagram as the first section.
DO structure the inertia assessment in this exact four-sub-section order.

**Sub-section 1 — Case for Staying Flat**

DO list at minimum two numbered reasons here.
DO NOT proceed until at least two reasons are written.
Each reason MUST name a specific, observable coordination mechanism — a communication
channel, an informal lead role, a recurring cadence, or a shared artifact.
DO NOT use generic statements like "the team communicates well" as a reason.
DO NOT move mechanism-typed content into Sub-section 2.

```
### Case for Staying Flat

1. [Specific mechanism — e.g., "weekly standup plus shared backlog resolves sprint-level
   cross-area dependencies without escalation"]
2. [Specific mechanism — e.g., "a single senior engineer acts as informal architecture
   arbiter; no cross-cutting decision has been blocked by lack of formal authority"]
(at minimum two numbered reasons; write all reasons before proceeding)
```

After writing all numbered mechanism reasons, perform a count-check: count the numbered
items above. MUST verify the count is at least two before continuing. Substitute that
count as N and DO emit the separator line exactly as shown:

```
--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. How We Coordinate Today begins.] ---
```

DO NOT EMIT this separator line before at least two numbered mechanism reasons are present.
DO NOT write Sub-section 2 until this separator line appears.

**Sub-section 2 — How We Coordinate Today**

DO inventory the coordination patterns currently in active use.
DO name channels, cadences, informal roles, and artifacts with frequency and participants.
DO NOT re-list the numbered reasons from Sub-section 1.

```
### How We Coordinate Today

[Catalog: recurring meetings, shared artifacts, escalation paths, informal roles —
named specifically with frequency and participants]
```

**Sub-section 3 — Rebuttal**

DO name the coordination failure the flat-team case and current mechanisms cannot answer.
DO reference a specific observable: a blocked decision, missed SLA, time-zone gap,
knowledge silo, or competing roadmap.
DO NOT write "the team is growing" without specifying the failure mode.

```
### Rebuttal

[Named failure mode, specific to this team and topic]
```

**Sub-section 4 — VERDICT and Re-assessment Trigger**

DO choose exactly one of: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED.
DO write a reasoning sentence connecting sub-sections 1, 2, and 3 to the verdict.
DO write a re-assessment trigger immediately after the verdict.
DO NOT write "revisit as the team grows" — the trigger MUST name a concrete threshold.

```
### VERDICT

[CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]

Reasoning: [one or two sentences — specific, not generic]

Re-assessment trigger: [concrete condition — e.g., "when headcount exceeds 12" or
"when on-call rotation spans more than two distinct service areas" or
"when the first external SLA is signed"]
```

DO NOT proceed past this sub-section until VERDICT and re-assessment trigger are both written.

---

ASCII ORG DIAGRAM

DO draw an ASCII hierarchy after the inertia assessment.
DO show at minimum two levels.
DO NOT produce a flat list of names without hierarchy.
DO show committees as distinct labeled nodes, not embedded in one area.
DO use role names from ROLES-LOADED or ROLES-NOTE — DO NOT introduce new role names.

---

HEADCOUNT BY AREA — DECIDES / ESCALATES REQUIRED

DO produce a headcount table immediately after the org diagram.
DO use five columns — Area, Headcount, Key Roles, Decides, Escalates.
DO NOT use a single "Decision Scope" column — the Decides and Escalates columns are
separate and both REQUIRED.
DO NOT write "owns the area" or generic ownership phrases in either column.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward, naming the destination role or forum.

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| [name] | [N or N-M] | [roles] | [decision types owned here] | [decision types escalated — name destination] |
| [name] | [N or N-M] | [roles] | [decision types owned here] | [decision types escalated — name destination] |
| **Total** | **[N]** | | | |

DO include at minimum two area rows with individual counts.
DO NOT produce only a single total with no area breakdown.

---

OPERATING RHYTHM TABLE

DO produce a cadence table after the headcount section.
DO include at minimum three distinct rows: ROB, a shiproom or gate, and a governance meeting.
DO NOT combine two meetings into one row.
DO NOT produce a rhythm table with only ROB.

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|

DO reference a role from ROLES-LOADED in the DRI / Owner column where possible.

---

COMMITTEE CHARTERS

DO write a charter for each governance meeting in the rhythm table.
DO include all four fields: Purpose, Membership, Decides, Escalates.
DO NOT label this section optional.
DO NOT write a rhythm table row for a committee and then omit its charter.

```
### [Committee name]

**Purpose:** [one sentence]
**Membership:** [roles from ROLES-LOADED — at minimum two roles; not personal names]
**Decides:** [decision types in scope]
**Escalates:** [decision types referred upward — name the destination role or forum]
```

DO populate the Escalates field with a named destination.
DO NOT write "everything not listed under Decides."

---

ORG-ELEMENT REGISTER — REQUIRED BEFORE ANTI-PATTERN WATCH

MUST produce this block immediately after Committee Charters.
DO NOT skip it.
DO NOT proceed to Org Evolution Roadmap until this block is complete.
REQUIRED: all four category entries (cat-1 through cat-4) MUST be populated with named
elements from the sections above before this block is closed.

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
    (all committees and named cadences from the Rhythm Table and Charters)

  cat-3 (Headcount):
    - Total headcount: [N]

  cat-4 (DRI Roles):
    - [DRI role]
    (all DRI roles from the Rhythm Table)
```

---

ORG EVOLUTION ROADMAP — REQUIRED

DO produce this section after the ORG-ELEMENT REGISTER.
DO NOT label it optional.
DO NOT omit it.

```
## Org Evolution Roadmap

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| [Row 1 — headcount threshold: "when headcount reaches N"] | [Named structural change] | [type] |
| [Row 2 — workload signal or structural symptom — NOT a second headcount number] | [Named structural change] | [type] |
```

REQUIRED: at minimum two rows. Row 1 MUST be a headcount threshold. Row 2 MUST come from
a different trigger category. DO NOT write two headcount thresholds — this counts as one
dimension, not two.

DO NOT proceed until both rows are written with distinct trigger dimensions.

---

ANTI-PATTERN WATCH — REQUIRED

DO produce this section after the Org Evolution Roadmap.
DO NOT label it optional.
DO NOT omit it.

MUST open each "Why It Applies Here" cell with typed citation syntax:

  `[element name] (cat-N) — [one sentence]`

DO NOT write a "Why It Applies Here" cell that names an element without the `(cat-N)` code.
DO NOT use a cat-N code that does not match the category schema in the ORG-ELEMENT REGISTER.
REQUIRED: the element name MUST be copied exactly from the register.

```
## Anti-Pattern Watch

| Anti-Pattern | Why It Applies Here | Mitigation |
|--------------|---------------------|------------|
| [Named anti-pattern] | `[element name] (cat-N) — [one sentence of specific relevance]` | [Mitigation] |
| [Second anti-pattern] | `[element name] (cat-N) — [one sentence]` | [Mitigation] |
```

DO include at minimum two named anti-patterns.

---

SECTION ORDER — DO NOT REORDER

DO write sections in this order:
1. ROLES-LOADED or ROLES-NOTE
2. Inertia Assessment (Case for Staying Flat [+ separator] / How We Coordinate Today / Rebuttal / VERDICT + Re-assessment Trigger)
3. ASCII Org Diagram
4. Headcount by Area (Decides / Escalates columns)
5. Operating Rhythm Table
6. Committee Charters
7. ORG-ELEMENT REGISTER
8. Org Evolution Roadmap
9. Anti-Pattern Watch

DO NOT reorder sections.
DO NOT omit any of the nine sections.

---

FINAL LINE

DO end with exactly:

```
Generated by: /org-chart {topic} — {date}
```

DO NOT emit literal placeholder text in the final line.

---

## V-03 — Phrasing Register: Enforcement Block Injection

**axis:** phrasing register (enforcement blocks injected at compliance points; surrounding
conversational prose from V-03/R7 preserved verbatim)
**hypothesis:** C-25 requires imperative-mode language in the skill's enforcement directives.
The rubric evaluator "checks C-25 by locating the skill's guard enforcement, register
construction, and citation format directives and confirming that at least one DO NOT / MUST /
REQUIRED form appears for each." V-03/R8 tests whether isolated labeled ENFORCEMENT blocks
— injected as visually distinct sections, not integrated into prose — satisfy this
requirement. If C-25 evaluators accept block-injected imperative framing as sufficient, this
design preserves V-03/R7's conversational readability while adding compliance insurance.
If C-25 requires inline imperative integration rather than adjacent blocks, this design fails
C-25 while preserving C-09-C-24. Expected: 17/17 if block injection counts; 16/17 if
inline integration is required.

---

You are running `/org-chart {topic}`.

---

ROLES — READ FIRST

Before writing anything else, check `.craft/roles/` for existing role definitions. If role
files are present, produce a ROLES-LOADED block listing each role name and a one-line
description drawn from the role file. If no role files are found, produce a ROLES-NOTE block
that says so explicitly and lists the inferred roles you will use. The roles block is the
first thing in the document; no other content appears before it.

Role files found:
```
ROLES-LOADED:
  - [role name] — [one-line description from role file]
```

No role files found:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] — [description]
```

---

INERTIA ASSESSMENT — FOUR SUB-SECTIONS, STEELMAN FIRST

The inertia assessment appears before any org diagrams. The purpose is to honestly evaluate
whether the team needs a formal structure at all, rather than jumping to org design. It is
organized into four sub-sections in sequence.

**Sub-section 1 — Case for Staying Flat**

This sub-section makes the strongest possible case for not introducing formal org structure.
It presents numbered reasons, each of which names a specific, observable mechanism — a
communication channel, an informal lead role, a recurring cadence, a shared artifact. Reasons
that assert team culture or communication quality without naming a specific mechanism are
too weak to count.

Aim for at least two numbered reasons before moving on. Both reasons name specific mechanisms
that currently work.

```
### Case for Staying Flat

1. [A specific mechanism that is currently working — name it concretely]
2. [A second specific mechanism that is currently working — name it concretely]
(at least two mechanisms are needed before this sub-section closes)
```

When at least two numbered mechanism reasons have been written, this sub-section is complete.
By convention, close it with a labeled boundary line before beginning the inventory:

```
--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. How We Coordinate Today begins.] ---
```

Before writing this boundary line, count the numbered reasons above and use that count as N.
The boundary line marks the end of the steelman and the beginning of the coordination
inventory that follows.

```
[ENFORCEMENT — SEQUENCING GUARD]
DO NOT EMIT the `--- [FLAT-CASE-CLOSED: ...]` separator line before at least two numbered
mechanism reasons are present in Case for Staying Flat.
DO NOT begin Sub-section 2 (How We Coordinate Today) until this separator line has been
emitted into the output.
REQUIRED: the count N in the separator MUST match the number of numbered reasons written.
[END ENFORCEMENT]
```

**Sub-section 2 — How We Coordinate Today**

This sub-section inventories the coordination patterns in active use. It catalogs the
channels, cadences, informal roles, and artifacts that currently exist — adding context
(frequency, participants, artifacts produced) to the picture the reasons above sketched.
It does not re-list the numbered reasons from Sub-section 1; it adds depth.

```
### How We Coordinate Today

[Catalog of coordination patterns: meetings, shared documents, escalation paths, informal
roles — named specifically with frequency and participants where known]
```

**Sub-section 3 — Rebuttal**

This sub-section names the coordination failure that the current flat-team case cannot
answer: a specific blocked decision, missed SLA, time-zone gap, knowledge silo, or
roadmap conflict. "The team is growing" is not a sufficient failure mode; it must name
what breaks.

```
### Rebuttal

[The specific coordination failure that the flat case cannot handle]
```

**Sub-section 4 — VERDICT and Re-assessment Trigger**

The verdict is one of two outcomes: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED. A reasoning
sentence connects the steelman reasons, the coordination inventory, and the rebuttal to the
verdict. The verdict is followed immediately by a re-assessment trigger that names a concrete
condition — a headcount threshold, a coordination-failure signal, or a milestone — at which
this verdict would be revisited. "Revisit as the team grows" is not a sufficient trigger.

```
### VERDICT

[CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]

Reasoning: [one or two sentences connecting sub-sections 1, 2, and 3 to the verdict]

Re-assessment trigger: [a specific condition, e.g., "when headcount exceeds 12" or
"when the on-call rotation spans more than two areas" or
"when the first external SLA is signed"]
```

---

ASCII ORG DIAGRAM

After the inertia assessment, draw an ASCII hierarchy showing the proposed structure.
The diagram shows at minimum two levels — a top level and at least one level below it —
with at minimum two distinct nodes. Committees appear as labeled nodes, not embedded in
an area. Role names come from the ROLES-LOADED or ROLES-NOTE block; do not introduce
names that did not appear there.

---

HEADCOUNT BY AREA

After the org diagram, produce a headcount table with five columns: Area, Headcount, Key
Roles, Decides, and Escalates. The Decides and Escalates columns are separate; a single
"Decision Scope" column does not satisfy this requirement. Each Decides cell names the
decision types owned at this level. Each Escalates cell names the decision types referred
upward and identifies the destination role or forum by name.

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| [name] | [N or N-M] | [roles] | [decisions owned here] | [decisions escalated — name destination] |
| [name] | [N or N-M] | [roles] | [decisions owned here] | [decisions escalated — name destination] |
| **Total** | **[N]** | | | |

At minimum two area rows with individual headcount counts; a single total without area
breakdown does not satisfy this section.

---

OPERATING RHYTHM TABLE

After the headcount section, produce a cadence table. The table covers at minimum three
distinct meetings: the ROB, a shiproom or ship gate, and a governance meeting such as an
architecture board. Two meetings do not belong in the same row. The DRI / Owner column
references a role from ROLES-LOADED where possible.

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|

---

COMMITTEE CHARTERS

For each governance meeting in the rhythm table, write a charter with four fields: Purpose
(one sentence), Membership (roles from ROLES-LOADED, not personal names), Decides (decision
types in scope), and Escalates (decision types referred upward, naming the destination role
or forum). The charter section is not optional; a rhythm table row without a corresponding
charter is incomplete.

```
### [Committee name]

**Purpose:** [one sentence]
**Membership:** [roles — at minimum two]
**Decides:** [decision types in scope]
**Escalates:** [decisions referred upward — name the destination]
```

---

ORG-ELEMENT REGISTER

Before the Anti-Pattern Watch begins, produce a named register block that catalogs the
output elements available for citation. The register's purpose is to serve as the lookup
source for the watch section — it makes citations traceable rather than recalled.

The register opens with a schema table defining the category codes, then lists the actual
elements from this document under each category.

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
    - [DRI role]
    (all DRI roles from the Rhythm Table)
```

```
[ENFORCEMENT — REGISTER CONSTRUCTION]
MUST produce the ORG-ELEMENT REGISTER block immediately after Committee Charters.
DO NOT skip this block.
DO NOT proceed to Org Evolution Roadmap until all four category entries (cat-1 through
cat-4) are populated with at least one named element from the sections above.
REQUIRED: the register MUST appear as a physically distinct labeled block, not as inline
notes within the Anti-Pattern Watch section.
[END ENFORCEMENT]
```

---

ORG EVOLUTION ROADMAP

After Committee Charters and the register, produce an evolution roadmap that describes how
the structure should change as the team grows. The roadmap is a table with at minimum two
rows, each naming a trigger and a structural response. The two rows address categorically
different trigger types: the first is a headcount threshold; the second comes from a
different category — a workload signal, structural symptom, or milestone event. Two
headcount numbers at different values are one trigger dimension, not two.

```
## Org Evolution Roadmap

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| [headcount threshold — e.g., "when headcount reaches 15"] | [Named change] | [type] |
| [workload signal, structural symptom, or milestone — not a second headcount number] | [Named change] | [type] |
```

---

ANTI-PATTERN WATCH

After the Org Evolution Roadmap, produce an Anti-Pattern Watch table. The "Why It Applies
Here" column draws from the ORG-ELEMENT REGISTER above using typed citation syntax:

  `[element name] (cat-N) — [one sentence]`

The element name is copied exactly from the register; the cat-N code comes from the schema
table in the register. A cell that names an element in prose without the typed syntax, or
uses a cat-N code that does not match the schema, does not satisfy this requirement.

```
[ENFORCEMENT — TYPED CITATIONS]
MUST open each "Why It Applies Here" cell with typed citation syntax `[element name] (cat-N)`.
DO NOT write a "Why It Applies Here" cell that names an element without the `(cat-N)` code.
DO NOT use a cat-N code that is not defined in the ORG-ELEMENT REGISTER category schema.
REQUIRED: element names in APW cells MUST be copied exactly from the register entries.
[END ENFORCEMENT]
```

```
## Anti-Pattern Watch

| Anti-Pattern | Why It Applies Here | Mitigation |
|--------------|---------------------|------------|
| [Named anti-pattern] | `[element name] (cat-N) — [one sentence of specific relevance]` | [Mitigation] |
| [Second anti-pattern] | `[element name] (cat-N) — [one sentence]` | [Mitigation] |
```

At minimum two anti-pattern rows, each with a typed citation from the register.

---

SECTION ORDER

The document is organized in this sequence:
1. ROLES-LOADED or ROLES-NOTE
2. Inertia Assessment (Case for Staying Flat [boundary line] / How We Coordinate Today / Rebuttal / VERDICT)
3. ASCII Org Diagram
4. Headcount by Area
5. Operating Rhythm Table
6. Committee Charters
7. ORG-ELEMENT REGISTER
8. Org Evolution Roadmap
9. Anti-Pattern Watch

---

FINAL LINE

End with exactly:

```
Generated by: /org-chart {topic} — {date}
```

---

## V-04 — Combined: Targeted Imperative Injection + Two-Step Count Protocol

**axis:** phrasing register + inertia framing (V-01/R8 targeted imperative conversion plus
V-01/R7's two-step count-verification protocol for the Case for Staying Flat separator)
**hypothesis:** V-01/R8 adds imperative directives for the three compliance behaviors and
predicts 17/17. The residual failure mode for C-23 in V-03/R7 is the single-step `{N}`
substitution: the model may emit the separator before all reasons are written (guard-before-
reasons) or substitute an incorrect count. V-01/R7 showed that a two-step protocol — count
the reasons explicitly, verify the count is at least two, then substitute and emit — makes
C-23 more auditable. V-04/R8 combines both layers: targeted imperative injection (C-25) plus
two-step count protocol (C-23 reliability). All other structure from V-03/R7 is preserved.
Expected: 17/17 with higher C-23 confidence than V-01/R8 alone.

---

You are running `/org-chart {topic}`.

---

ROLES — READ FIRST

Before writing anything else, check `.craft/roles/` for existing role definitions. If role
files are present, produce a ROLES-LOADED block listing each role name and a one-line
description drawn from the role file. If no role files are found, produce a ROLES-NOTE block
that says so explicitly and lists the inferred roles you will use. The roles block is the
first thing in the document; no other content appears before it.

Role files found:
```
ROLES-LOADED:
  - [role name] — [one-line description from role file]
```

No role files found:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] — [description]
```

---

INERTIA ASSESSMENT — FOUR SUB-SECTIONS, STEELMAN FIRST

The inertia assessment appears before any org diagrams. The purpose is to honestly evaluate
whether the team needs a formal structure at all, rather than jumping to org design. It is
organized into four sub-sections in sequence.

**Sub-section 1 — Case for Staying Flat**

This sub-section makes the strongest possible case for not introducing formal org structure.
It presents numbered reasons, each of which names a specific, observable mechanism — a
communication channel, an informal lead role, a recurring cadence, a shared artifact. Reasons
that assert team culture or communication quality without naming a specific mechanism are
too weak to count.

Aim for at least two numbered reasons before moving on. Both reasons name specific mechanisms
that currently work.

```
### Case for Staying Flat

1. [A specific mechanism that is currently working — name it concretely]
2. [A second specific mechanism that is currently working — name it concretely]
(at least two mechanisms are needed before this sub-section closes)
```

When at least two numbered mechanism reasons have been written, perform a two-step
count-verification before emitting the boundary line:

**Step 1 — Count:** Count the numbered items in Case for Staying Flat above.
**Step 2 — Verify:** If the count is fewer than two, write the missing reasons first.
Once the count is at least two, substitute that count as N and emit the separator line
exactly as shown:

```
--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. How We Coordinate Today begins.] ---
```

**ENFORCEMENT — GUARD:** DO NOT EMIT this separator line before the count-check in Step 2
passes (count >= 2). DO NOT begin Sub-section 2 until this separator line appears in the
output. REQUIRED: the count N MUST equal the actual number of numbered reasons written in
Case for Staying Flat — verify before substituting.

**Sub-section 2 — How We Coordinate Today**

This sub-section inventories the coordination patterns in active use. It catalogs the
channels, cadences, informal roles, and artifacts that currently exist — adding context
(frequency, participants, artifacts produced) to the picture the reasons above sketched.
It does not re-list the numbered reasons from Sub-section 1; it adds depth.

```
### How We Coordinate Today

[Catalog of coordination patterns: meetings, shared documents, escalation paths, informal
roles — named specifically with frequency and participants where known]
```

**Sub-section 3 — Rebuttal**

This sub-section names the coordination failure that the current flat-team case cannot
answer: a specific blocked decision, missed SLA, time-zone gap, knowledge silo, or
roadmap conflict. "The team is growing" is not a sufficient failure mode; it must name
what breaks.

```
### Rebuttal

[The specific coordination failure that the flat case cannot handle]
```

**Sub-section 4 — VERDICT and Re-assessment Trigger**

The verdict is one of two outcomes: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED. A reasoning
sentence connects the steelman reasons, the coordination inventory, and the rebuttal to the
verdict. The verdict is followed immediately by a re-assessment trigger that names a concrete
condition — a headcount threshold, a coordination-failure signal, or a milestone — at which
this verdict would be revisited. "Revisit as the team grows" is not a sufficient trigger.

```
### VERDICT

[CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]

Reasoning: [one or two sentences connecting sub-sections 1, 2, and 3 to the verdict]

Re-assessment trigger: [a specific condition, e.g., "when headcount exceeds 12" or
"when the on-call rotation spans more than two areas" or
"when the first external SLA is signed"]
```

---

ASCII ORG DIAGRAM

After the inertia assessment, draw an ASCII hierarchy showing the proposed structure.
The diagram shows at minimum two levels — a top level and at least one level below it —
with at minimum two distinct nodes. Committees appear as labeled nodes, not embedded in
an area. Role names come from the ROLES-LOADED or ROLES-NOTE block; do not introduce
names that did not appear there.

---

HEADCOUNT BY AREA

After the org diagram, produce a headcount table with five columns: Area, Headcount, Key
Roles, Decides, and Escalates. The Decides and Escalates columns are separate; a single
"Decision Scope" column does not satisfy this requirement. Each Decides cell names the
decision types owned at this level. Each Escalates cell names the decision types referred
upward and identifies the destination role or forum by name.

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| [name] | [N or N-M] | [roles] | [decisions owned here] | [decisions escalated — name destination] |
| [name] | [N or N-M] | [roles] | [decisions owned here] | [decisions escalated — name destination] |
| **Total** | **[N]** | | | |

At minimum two area rows with individual headcount counts; a single total without area
breakdown does not satisfy this section.

---

OPERATING RHYTHM TABLE

After the headcount section, produce a cadence table. The table covers at minimum three
distinct meetings: the ROB, a shiproom or ship gate, and a governance meeting such as an
architecture board. Two meetings do not belong in the same row. The DRI / Owner column
references a role from ROLES-LOADED where possible.

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|

---

COMMITTEE CHARTERS

For each governance meeting in the rhythm table, write a charter with four fields: Purpose
(one sentence), Membership (roles from ROLES-LOADED, not personal names), Decides (decision
types in scope), and Escalates (decision types referred upward, naming the destination role
or forum). The charter section is not optional; a rhythm table row without a corresponding
charter is incomplete.

```
### [Committee name]

**Purpose:** [one sentence]
**Membership:** [roles — at minimum two]
**Decides:** [decision types in scope]
**Escalates:** [decisions referred upward — name the destination]
```

---

ORG-ELEMENT REGISTER

Before the Anti-Pattern Watch begins, produce a named register block that catalogs the
output elements available for citation. The register's purpose is to serve as the lookup
source for the watch section — it makes citations traceable rather than recalled.

The register opens with a schema table defining the category codes, then lists the actual
elements from this document under each category.

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
    - [DRI role]
    (all DRI roles from the Rhythm Table)
```

**ENFORCEMENT — REGISTER:** MUST produce this ORG-ELEMENT REGISTER block immediately after
Committee Charters. DO NOT proceed to Org Evolution Roadmap until all four category entries
(cat-1 through cat-4) are populated with named elements from the sections above.

---

ORG EVOLUTION ROADMAP

After Committee Charters and the register, produce an evolution roadmap that describes how
the structure should change as the team grows. The roadmap is a table with at minimum two
rows, each naming a trigger and a structural response. The two rows address categorically
different trigger types: the first is a headcount threshold; the second comes from a
different category — a workload signal, structural symptom, or milestone event. Two
headcount numbers at different values are one trigger dimension, not two.

```
## Org Evolution Roadmap

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| [headcount threshold — e.g., "when headcount reaches 15"] | [Named change] | [type] |
| [workload signal, structural symptom, or milestone — not a second headcount number] | [Named change] | [type] |
```

---

ANTI-PATTERN WATCH

After the Org Evolution Roadmap, produce an Anti-Pattern Watch table. The "Why It Applies
Here" column draws from the ORG-ELEMENT REGISTER above using typed citation syntax:

  `[element name] (cat-N) — [one sentence]`

The element name is copied exactly from the register; the cat-N code comes from the schema
table in the register. A cell that names an element in prose without the typed syntax, or
uses a cat-N code that does not match the schema, does not satisfy this requirement.

**ENFORCEMENT — CITATIONS:** MUST open each "Why It Applies Here" cell with typed citation
syntax `[element name] (cat-N)`. DO NOT write a cell that names an element without the
`(cat-N)` code. REQUIRED: cat-N codes MUST match the category schema defined in the
ORG-ELEMENT REGISTER.

```
## Anti-Pattern Watch

| Anti-Pattern | Why It Applies Here | Mitigation |
|--------------|---------------------|------------|
| [Named anti-pattern] | `[element name] (cat-N) — [one sentence of specific relevance]` | [Mitigation] |
| [Second anti-pattern] | `[element name] (cat-N) — [one sentence]` | [Mitigation] |
```

At minimum two anti-pattern rows, each with a typed citation from the register.

---

SECTION ORDER

The document is organized in this sequence:
1. ROLES-LOADED or ROLES-NOTE
2. Inertia Assessment (Case for Staying Flat [two-step count + boundary line] / How We Coordinate Today / Rebuttal / VERDICT)
3. ASCII Org Diagram
4. Headcount by Area
5. Operating Rhythm Table
6. Committee Charters
7. ORG-ELEMENT REGISTER
8. Org Evolution Roadmap
9. Anti-Pattern Watch

---

FINAL LINE

End with exactly:

```
Generated by: /org-chart {topic} — {date}
```

---

## V-05 — Combined: Full Imperative Conversion + MUST-PRECEDE Register Gate

**axis:** phrasing register + output format (V-02/R8 full-imperative base plus a
MUST-PRECEDE gate assertion in the register section — an explicit stated dependency that
Org Evolution Roadmap is gated on register completion)
**hypothesis:** V-02/R8 converts all directives to imperative mode (C-25 PASS predicted).
The primary residual failure mode for C-21 is the model producing the register block as a
note or inline comment rather than as a physically distinct labeled artifact. A MUST-PRECEDE
gate — "MUST appear as a named block preceding Org Evolution Roadmap; DO NOT embed register
entries as inline notes within Org Evolution Roadmap or Anti-Pattern Watch" — enforces the
physical distinctness required by C-21. Tests whether adding a structural gate to an already-
imperative prompt improves C-21 reliability or causes unnecessary compression. If the gate
triggers early truncation of the register body, C-21 degrades; if it improves completion
rate, V-05 is the preferred production form. Expected: 17/17.

---

You are running `/org-chart {topic}`.

---

ROLES — READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a ROLES-LOADED block at the top of the output.
DO NOT invent role names unless no roles files are found.

If roles are found:
```
ROLES-LOADED:
  - [role name] — [one-line description from role file]
```

If absent:
```
ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] — [description]
```

DO NOT write any other section until this block exists.

---

INERTIA ASSESSMENT — FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.
DO NOT write an org diagram as the first section.
DO structure the inertia assessment in this exact four-sub-section order.

**Sub-section 1 — Case for Staying Flat**

DO list at minimum two numbered reasons here.
DO NOT proceed until at least two reasons are written.
Each reason MUST name a specific, observable coordination mechanism — a communication
channel, an informal lead role, a recurring cadence, or a shared artifact.
DO NOT use generic statements like "the team communicates well" as a reason.
DO NOT move mechanism-typed content into Sub-section 2.

```
### Case for Staying Flat

1. [Specific mechanism — e.g., "weekly standup plus shared backlog resolves sprint-level
   cross-area dependencies without escalation"]
2. [Specific mechanism — e.g., "a single senior engineer acts as informal architecture
   arbiter; no cross-cutting decision has been blocked by lack of formal authority"]
(at minimum two numbered reasons; write all reasons before proceeding)
```

After writing all numbered mechanism reasons, perform a count-check: count the numbered
items above. MUST verify the count is at least two before continuing. Substitute that
count as N and emit the separator line exactly as shown:

```
--- [FLAT-CASE-CLOSED: {N} mechanism reasons recorded. How We Coordinate Today begins.] ---
```

DO NOT EMIT this separator line before at least two numbered mechanism reasons are present.
DO NOT write Sub-section 2 until this separator line appears.

**Sub-section 2 — How We Coordinate Today**

DO inventory the coordination patterns currently in active use.
DO name channels, cadences, informal roles, and artifacts with frequency and participants.
DO NOT re-list the numbered reasons from Sub-section 1.

```
### How We Coordinate Today

[Catalog: recurring meetings, shared artifacts, escalation paths, informal roles —
named specifically with frequency and participants]
```

**Sub-section 3 — Rebuttal**

DO name the coordination failure the flat-team case and current mechanisms cannot answer.
DO reference a specific observable: a blocked decision, missed SLA, time-zone gap,
knowledge silo, or competing roadmap.
DO NOT write "the team is growing" without specifying the failure mode.

```
### Rebuttal

[Named failure mode, specific to this team and topic]
```

**Sub-section 4 — VERDICT and Re-assessment Trigger**

DO choose exactly one of: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED.
DO write a reasoning sentence connecting sub-sections 1, 2, and 3 to the verdict.
DO write a re-assessment trigger immediately after the verdict.
DO NOT write "revisit as the team grows" — the trigger MUST name a concrete threshold.

```
### VERDICT

[CAN-OPERATE-FLAT | STRUCTURE-WARRANTED]

Reasoning: [one or two sentences — specific, not generic]

Re-assessment trigger: [concrete condition — e.g., "when headcount exceeds 12" or
"when on-call rotation spans more than two distinct service areas"]
```

DO NOT proceed past this sub-section until VERDICT and re-assessment trigger are both written.

---

ASCII ORG DIAGRAM

DO draw an ASCII hierarchy after the inertia assessment.
DO show at minimum two levels.
DO NOT produce a flat list of names without hierarchy.
DO show committees as distinct labeled nodes, not embedded in one area.
DO use role names from ROLES-LOADED or ROLES-NOTE — DO NOT introduce new role names.

---

HEADCOUNT BY AREA — DECIDES / ESCALATES REQUIRED

DO produce a headcount table immediately after the org diagram.
DO use five columns — Area, Headcount, Key Roles, Decides, Escalates.
DO NOT use a single "Decision Scope" column — the Decides and Escalates columns are
separate and both REQUIRED.
DO NOT write "owns the area" or generic ownership phrases in either column.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward, naming the destination role or forum.

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| [name] | [N or N-M] | [roles] | [decision types owned here] | [decision types escalated — name destination] |
| [name] | [N or N-M] | [roles] | [decision types owned here] | [decision types escalated — name destination] |
| **Total** | **[N]** | | | |

DO include at minimum two area rows with individual counts.
DO NOT produce only a single total with no area breakdown.

---

OPERATING RHYTHM TABLE

DO produce a cadence table after the headcount section.
DO include at minimum three distinct rows: ROB, a shiproom or gate, and a governance meeting.
DO NOT combine two meetings into one row.
DO NOT produce a rhythm table with only ROB.

| Cadence | Frequency | DRI / Owner | Purpose |
|---------|-----------|-------------|---------|

DO reference a role from ROLES-LOADED in the DRI / Owner column where possible.

---

COMMITTEE CHARTERS

DO write a charter for each governance meeting in the rhythm table.
DO include all four fields: Purpose, Membership, Decides, Escalates.
DO NOT label this section optional.
DO NOT write a rhythm table row for a committee and then omit its charter.

```
### [Committee name]

**Purpose:** [one sentence]
**Membership:** [roles from ROLES-LOADED — at minimum two roles; not personal names]
**Decides:** [decision types in scope]
**Escalates:** [decision types referred upward — name the destination role or forum]
```

DO populate the Escalates field with a named destination.
DO NOT write "everything not listed under Decides."

---

ORG-ELEMENT REGISTER — MUST PRECEDE ORG EVOLUTION ROADMAP

MUST produce this block as a named, physically distinct section immediately after Committee
Charters. DO NOT embed register entries as inline notes within Org Evolution Roadmap or
Anti-Pattern Watch. DO NOT skip this block. DO NOT proceed to Org Evolution Roadmap until
this block is written and all four category entries are populated.

REQUIRED: the register MUST appear with the label `ORG-ELEMENT REGISTER` as a section
header. Inline taxonomy notes inside other sections do NOT satisfy this requirement — the
register is a standalone artifact.

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
    (all committees and named cadences from the Rhythm Table and Charters)

  cat-3 (Headcount):
    - Total headcount: [N]

  cat-4 (DRI Roles):
    - [DRI role]
    (all DRI roles from the Rhythm Table)
```

DO NOT proceed to Org Evolution Roadmap until cat-1 through cat-4 above are each populated
with at least one named element from the sections preceding this block.

---

ORG EVOLUTION ROADMAP — REQUIRED

DO produce this section after the ORG-ELEMENT REGISTER.
DO NOT label it optional.
DO NOT omit it.

```
## Org Evolution Roadmap

| Trigger | Structural Change | Type |
|---------|-------------------|------|
| [Row 1 — headcount threshold: "when headcount reaches N"] | [Named structural change] | [type] |
| [Row 2 — workload signal or structural symptom — NOT a second headcount number] | [Named structural change] | [type] |
```

REQUIRED: at minimum two rows. Row 1 MUST be a headcount threshold. Row 2 MUST come from
a different trigger category. DO NOT write two headcount thresholds — this counts as one
dimension, not two.

DO NOT proceed until both rows are written with distinct trigger dimensions.

---

ANTI-PATTERN WATCH — REQUIRED

DO produce this section after the Org Evolution Roadmap.
DO NOT label it optional.
DO NOT omit it.

MUST open each "Why It Applies Here" cell with typed citation syntax:

  `[element name] (cat-N) — [one sentence]`

DO NOT write a "Why It Applies Here" cell that names an element without the `(cat-N)` code.
DO NOT use a cat-N code that does not match the category schema in the ORG-ELEMENT REGISTER.
REQUIRED: element names MUST be copied exactly from the register entries.

```
## Anti-Pattern Watch

| Anti-Pattern | Why It Applies Here | Mitigation |
|--------------|---------------------|------------|
| [Named anti-pattern] | `[element name] (cat-N) — [one sentence of specific relevance]` | [Mitigation] |
| [Second anti-pattern] | `[element name] (cat-N) — [one sentence]` | [Mitigation] |
```

DO include at minimum two named anti-patterns.

---

SECTION ORDER — DO NOT REORDER

DO write sections in this order:
1. ROLES-LOADED or ROLES-NOTE
2. Inertia Assessment (Case for Staying Flat [+ separator] / How We Coordinate Today / Rebuttal / VERDICT + Re-assessment Trigger)
3. ASCII Org Diagram
4. Headcount by Area (Decides / Escalates columns)
5. Operating Rhythm Table
6. Committee Charters
7. ORG-ELEMENT REGISTER
8. Org Evolution Roadmap
9. Anti-Pattern Watch

DO NOT reorder sections.
DO NOT omit any of the nine sections.

---

FINAL LINE

DO end with exactly:

```
Generated by: /org-chart {topic} — {date}
```

DO NOT emit literal placeholder text in the final line.
