---
skill: quest-variate
skill_target: corps-chart
date: 2026-03-17
round: 3
rubric: simulations/quest/rubrics/corps-chart-rubric-v3-2026-03-17.md
---

# Quest Variate -- corps-chart (Round 3)

Five complete, runnable skill body variations targeting the v3 rubric.
New in v3: C-13 (ROLE-NAME LOCK block) and C-14 (mandatory four-field Rebuttal form).
R1 variations predate both criteria. R3 explores distinct enforcement strategies for each.

---

## Variation Summary

| ID | Axis | Hypothesis |
|----|------|------------|
| V-01 | C-13 placement: lock-as-active-contract | Framing ROLE-NAME LOCK as an explicit reference contract that downstream steps invoke (not just a list) closes the gap between list existence and per-section use, reducing role drift in rhythm DRI/Owner and charter Membership |
| V-02 | C-14 form: header-driven four-field structure | Writing the Rebuttal as four section headers (not labeled bullets) enforces sequential completion -- the model cannot produce OBSERVABLE BREAKDOWN without writing ROLE UNDER PRESSURE first, because headers are generated before their content |
| V-03 | Lifecycle emphasis: per-section ROLE-LOCK-CHECK | Inserting an explicit ROLE-LOCK-CHECK at the start of each post-classification section makes role coherence a per-section precondition rather than a global prose expectation, directly targeting C-12 failures in rhythm table and charters |
| V-04 | Combined: C-13 contract + C-14 form (paired mechanics) | C-13 provides the reference list; C-14 provides the intake form. Combining them creates a structural pair -- lock defines what is permitted, form enforces sequential grounding -- that closes the fluent-default failure mode more reliably than either alone |
| V-05 | Combined: format contract + C-13 + C-14 + per-section checks | Full mechanical integration: upfront format schemas + role-name lock as contract + four-field Rebuttal form + per-section lock-checks. Highest expected compliance; tests whether layering all mechanisms over-constrains the model or produces clean output |

---

## V-01 -- C-13 Placement: Lock-as-Active-Contract

**Axis**: C-13 placement mechanics -- ROLE-NAME LOCK framed as an active per-section reference contract, not a passive list
**Hypothesis**: If the ROLE-NAME LOCK is introduced as a named contract that downstream sections are explicitly instructed to invoke before writing role names, role-drift in the rhythm DRI/Owner and charter Membership fields drops -- because the model is given a concrete action ("check against ROLE-NAME LOCK") rather than an implicit expectation ("don't introduce new roles").

---

You are running `/org-chart {topic}`.

STEP 1 -- LOAD ROLES

Read `.craft/roles/`. Produce a `ROLES-LOADED:` block: `- [role name] -- [one-line description from role file]` per role. If no files are found, produce `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` with inferred roles in the same format.

DO NOT write any other section until this block exists.

STEP 2 -- CLASSIFY ROLES

Immediately after ROLES-LOADED or ROLES-NOTE, produce a `ROLE-TYPE-CLASSIFICATION:` block. Assign each role exactly one type: `Engineering / PM / Design / Operations / Research / Other`. Format: `- [role name] -- [domain type]`. Tier order: Engineering first, then Operations, then PM / Design / Research / Other. Complete one tier before starting the next. Every loaded role must appear. No role may appear that was absent from the loaded block.

STEP 3 -- EMIT ROLE-NAME LOCK (REQUIRED BEFORE FIRST GATE)

Immediately after ROLE-TYPE-CLASSIFICATION, before any phase gate, produce the following block:

```
ROLE-NAME LOCK
==============
The following roles are the complete set of permitted role references for this document.
No role name may appear in any section below that is not listed here.

[list every role from ROLES-LOADED, one per line]
```

This block is the reference contract for all downstream sections. Every section that names a role must name a role from this list -- not an archetype, not an inferred title, not a paraphrase.

After the ROLE-NAME LOCK block, emit:
`=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

DO NOT proceed past this gate until the ROLE-NAME LOCK block is present above it.

STEP 4 -- INERTIA ASSESSMENT

Write before any org diagram. Four sub-sections in this exact order.

**Sub-section 1 -- Case for Staying Flat**

Produce a mechanism evidence table: `Mechanism Name | Type | Frequency / Participants`.
Minimum two data rows. Type closed vocabulary: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.

Count data rows. Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
DO NOT begin Sub-section 2 before this separator.

**Sub-section 2 -- How We Coordinate Today**

Inventory active coordination patterns: channels, cadences, informal roles, artifacts with frequency and participants. Do not re-list mechanism rows from Sub-section 1.

**Sub-section 3 -- Rebuttal**

>> ROLE-NAME LOCK CHECK: Before naming any role in this sub-section, verify it appears in the ROLE-NAME LOCK block above. <<

Structure the Rebuttal as a four-field form with explicit labels:

ROLE UNDER PRESSURE: [name exactly one role from ROLE-NAME LOCK]
OBSERVABLE BREAKDOWN: [current coordination failure this role experiences -- not a future growth risk]
WHY EXISTING MECHANISMS FAIL: [why the mechanisms in Sub-section 1 cannot resolve this failure]
RE-ASSESSMENT TRIGGER: [specific measurable threshold -- hire count, milestone event, or structural symptom]

**Sub-section 4 -- VERDICT**

Open with: `FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 OBSERVABLE BREAKDOWN]`
Rating from closed set: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`

DO NOT emit the verdict declaration before the pressure line. Declare exactly one: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Reference FLAT-CASE-PRESSURE by name.

The re-assessment trigger is already written in Sub-section 3 -- reference it here by quoting the RE-ASSESSMENT TRIGGER field value. Do not write a new one.

Emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

STEP 5 -- ASCII ORG DIAGRAM

>> ROLE-NAME LOCK CHECK: Every role name in this diagram must appear in the ROLE-NAME LOCK block. <<

Draw ASCII hierarchy with at minimum two levels. Committees as distinct labeled nodes. Role names from ROLE-NAME LOCK only.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

STEP 6 -- HEADCOUNT BY AREA

>> ROLE-NAME LOCK CHECK: All Key Roles entries must name roles from ROLE-NAME LOCK. <<

Table with five columns: `Area | Headcount | Key Roles | Decides | Escalates`.
DO NOT merge Decides and Escalates into a single column.
Key Roles: `[role name] ([domain type])` from ROLE-TYPE-CLASSIFICATION.
Decides: decision types owned at this area level.
Escalates: decision types referred upward, naming destination role or forum.
Minimum two area rows plus `**Total**` row with sum.

STEP 7 -- OPERATING RHYTHM TABLE

>> ROLE-NAME LOCK CHECK: All DRI / Owner entries must name roles from ROLE-NAME LOCK. <<

Columns: `Cadence | Frequency | DRI / Owner | Purpose`.
Minimum three distinct rows: (a) ROB, (b) shiproom or gate, (c) governance meeting.
Do not merge two meetings. DRI / Owner references a loaded role.

STEP 8 -- COMMITTEE CHARTERS

>> ROLE-NAME LOCK CHECK: All Membership and Decides role names must appear in ROLE-NAME LOCK. <<

Charter per governance meeting. All five fields required:
- `Purpose`
- `Membership` -- minimum two roles as `[role name] ([domain type])`
- `Decides`
- `Escalates` -- named destination, not "everything not listed under Decides"
- `Quorum: [N] of [M] member roles required for binding decisions` (fraction format required)

Emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

STEP 9 -- ORG-ELEMENT REGISTER

`ORG-ELEMENT REGISTER` with all four categories populated:
- `cat-1 (Areas)` -- `- [area name] -- headcount: [N]`
- `cat-2 (Committees/Cadences)` -- `- [name]`
- `cat-3 (Headcount)` -- `- Total headcount: [N]`
- `cat-4 (DRI Roles)` -- `- [DRI role]`

STEP 10 -- ORG EVOLUTION ROADMAP

Trigger table: `Trigger | Structural Change | Type`. Minimum two rows.
Row 1: headcount threshold trigger.
Row 2: different category -- workload signal, structural symptom, or milestone event.

STEP 11 -- ANTI-PATTERN WATCH

Table: `Anti-Pattern | Why It Applies Here | Mitigation`. Minimum two rows.
Every `Why It Applies Here` cell opens with: `[element name] (cat-N) -- [one sentence]` using a valid cat-N from ORG-ELEMENT REGISTER.

End with: `Generated by: /org-chart {topic} -- {date}`

---

## V-02 -- C-14 Form: Header-Driven Four-Field Structure

**Axis**: C-14 form enforcement -- the Rebuttal four-field form is expressed as four section headers, not labeled bullets
**Hypothesis**: When ROLE UNDER PRESSURE / OBSERVABLE BREAKDOWN / WHY EXISTING MECHANISMS FAIL / RE-ASSESSMENT TRIGGER are section headers rather than field labels in a bullet list, the model generates each header before its content, making it structurally impossible to write OBSERVABLE BREAKDOWN without first committing to ROLE UNDER PRESSURE. This eliminates the fluent-default failure mode where the breakdown prose is written and the role reference is retrofitted or omitted.

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

Read `.craft/roles/`. Produce a `ROLES-LOADED:` block: `- [role name] -- [one-line description]` per role. If no files found, produce `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` with inferred roles in the same format. DO NOT write any other section until this block exists.

ROLE-TYPE-CLASSIFICATION -- REQUIRED

Immediately after ROLES-LOADED or ROLES-NOTE, produce a `ROLE-TYPE-CLASSIFICATION:` block. One type per role: `Engineering / PM / Design / Operations / Research / Other`. Format: `- [role name] -- [domain type]`. Tier order: Engineering first, then Operations, then PM / Design / Research / Other. Every loaded role classified; no unlisted roles added.

ROLE-NAME LOCK -- REQUIRED BEFORE FIRST GATE

Immediately after ROLE-TYPE-CLASSIFICATION, produce a `ROLE-NAME LOCK:` block that lists every role from ROLES-LOADED as a flat enumeration. This is the canonical role list. No role name may appear after this point that is not in this list.

Emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

INERTIA ASSESSMENT

Write the full assessment before drawing any org structure. Four sub-sections in order.

**Case for Staying Flat**

Produce a mechanism evidence table: `Mechanism Name | Type | Frequency / Participants`. Minimum two rows. Type values: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.

Count rows. Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

**How We Coordinate Today**

Inventory active coordination: channels, cadences, informal roles, artifacts with frequency and participants. Do not re-list mechanism rows.

**Rebuttal**

Write this sub-section using the four-header form below. Each header is a required section.
The headers must appear in this exact order.
Do not write a prose paragraph in place of the form.

#### ROLE UNDER PRESSURE
Name exactly one role from ROLE-NAME LOCK. This is the role that the coordination failure falls on.

#### OBSERVABLE BREAKDOWN
Describe the current coordination failure this role experiences today. This must be observable and present -- not a future growth risk. Acceptable: blocked decision, missed SLA, time-zone gap, knowledge silo, competing roadmap. Not acceptable: "as the team grows, this role will..."

#### WHY EXISTING MECHANISMS FAIL
Explain why the coordination mechanisms documented in Case for Staying Flat cannot prevent or resolve the OBSERVABLE BREAKDOWN. Name at least one mechanism from the table and explain why it is insufficient.

#### RE-ASSESSMENT TRIGGER
Name the specific measurable threshold at which the verdict should be reconsidered. Acceptable: a hire count, a named milestone event, a structural symptom. Not acceptable: "revisit as the team grows."

**VERDICT**

Open with: `FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing mechanism count and OBSERVABLE BREAKDOWN field content]`
Rating: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`
DO NOT emit verdict declaration before the pressure line.
Declare: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Reference FLAT-CASE-PRESSURE by name.

Emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

ASCII ORG DIAGRAM

Draw hierarchy with at minimum two levels. Committees as distinct labeled nodes. Role names from ROLE-NAME LOCK only.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

Five columns: `Area | Headcount | Key Roles | Decides | Escalates`.
DO NOT merge Decides and Escalates.
Key Roles: `[role name] ([domain type])` from ROLE-TYPE-CLASSIFICATION.
Minimum two area rows plus `**Total**` row.

OPERATING RHYTHM TABLE

Columns: `Cadence | Frequency | DRI / Owner | Purpose`. Minimum three rows: ROB + shiproom/gate + governance. No merged rows. DRI / Owner from ROLE-NAME LOCK.

COMMITTEE CHARTERS

Charter per governance meeting. Five fields required:
- `Purpose`
- `Membership` -- minimum two roles as `[role name] ([domain type])`
- `Decides`
- `Escalates` -- named destination
- `Quorum: [N] of [M] member roles required for binding decisions`

Emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

All four categories:
- `cat-1 (Areas)` -- `- [area name] -- headcount: [N]`
- `cat-2 (Committees/Cadences)` -- `- [name]`
- `cat-3 (Headcount)` -- `- Total headcount: [N]`
- `cat-4 (DRI Roles)` -- `- [DRI role]`

ORG EVOLUTION ROADMAP

`Trigger | Structural Change | Type`. Two rows minimum. Row 1: headcount threshold. Row 2: different category.

ANTI-PATTERN WATCH

`Anti-Pattern | Why It Applies Here | Mitigation`. Two rows minimum.
Every `Why It Applies Here`: `[element name] (cat-N) -- [one sentence]` with valid cat-N from register.

End with: `Generated by: /org-chart {topic} -- {date}`

---

## V-03 -- Lifecycle Emphasis: Per-Section ROLE-LOCK-CHECK

**Axis**: Lifecycle emphasis -- after the ROLE-NAME LOCK is emitted, each subsequent section opens with an inline ROLE-LOCK-CHECK that names which fields or cells must be verified against the lock
**Hypothesis**: A global "do not introduce new roles" instruction is routinely satisfied by the roles block itself but fails silently in the rhythm DRI/Owner column and charter Membership fields, because those sections are written independently with local context. Injecting a ROLE-LOCK-CHECK at the top of each section re-activates the constraint locally, producing C-12 compliance without requiring the model to maintain global state.

---

You are running `/org-chart {topic}`.

PHASE 1: ROLE LOADING AND CLASSIFICATION

Read `.craft/roles/`. Produce a `ROLES-LOADED:` block: `- [role name] -- [one-line description]` per role. If no files found: `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` with inferred roles in the same format. No other section until this block is complete.

Immediately after ROLES-LOADED or ROLES-NOTE, produce a `ROLE-TYPE-CLASSIFICATION:` block. One type per role: `Engineering / PM / Design / Operations / Research / Other`. Format: `- [role name] -- [domain type]`. Tier order: Engineering first, then Operations, then PM / Design / Research / Other. Complete one tier before starting the next. Every loaded role must be classified. No unlisted roles added.

Immediately after ROLE-TYPE-CLASSIFICATION, produce a `ROLE-NAME LOCK:` block enumerating every role from ROLES-LOADED as the complete permitted set for this document. Format: `- [role name]` per line.

Emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

PHASE 2: INERTIA ASSESSMENT

> ROLE-LOCK-CHECK (Rebuttal): Sub-section 3 (Rebuttal) must name exactly one role from ROLE-NAME LOCK in the ROLE UNDER PRESSURE field. No role name may appear in this sub-section that is not in ROLE-NAME LOCK.

Write before any org structure. Four sub-sections in order.

**Sub-section 1 -- Case for Staying Flat**

Mechanism table: `Mechanism Name | Type | Frequency / Participants`. Two rows minimum. Type values: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.

Count rows. Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
Do not begin Sub-section 2 before this separator.

**Sub-section 2 -- How We Coordinate Today**

Inventory active coordination patterns. Do not re-list mechanism table rows.

**Sub-section 3 -- Rebuttal**

Write as the following four-field form. All fields required. Order is fixed.

```
ROLE UNDER PRESSURE: [exactly one role from ROLE-NAME LOCK]
OBSERVABLE BREAKDOWN: [current failure -- not a future growth projection]
WHY EXISTING MECHANISMS FAIL: [why the flat-case mechanisms cannot resolve this]
RE-ASSESSMENT TRIGGER: [specific measurable threshold]
```

**Sub-section 4 -- VERDICT**

Open with: `FLAT-CASE-PRESSURE: [rating] -- [justification citing mechanism count and OBSERVABLE BREAKDOWN]`
Rating: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`
Declare: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Reference FLAT-CASE-PRESSURE by name.

Emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

PHASE 3: ORG STRUCTURE

> ROLE-LOCK-CHECK (Diagram): Every role name in the ASCII diagram must appear in ROLE-NAME LOCK. No new role names introduced.

Draw ASCII hierarchy with at minimum two levels. Committees as distinct labeled nodes.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

PHASE 4: HEADCOUNT AND RHYTHM

> ROLE-LOCK-CHECK (Headcount): All Key Roles cell entries must name roles from ROLE-NAME LOCK.
> ROLE-LOCK-CHECK (Rhythm): All DRI / Owner column entries must name roles from ROLE-NAME LOCK.

**Headcount by Area**

`Area | Headcount | Key Roles | Decides | Escalates` -- five columns, Decides and Escalates separate.
Key Roles: `[role name] ([domain type])`. Escalates: named destination. Minimum two area rows plus `**Total**`.

**Operating Rhythm Table**

`Cadence | Frequency | DRI / Owner | Purpose`. Minimum three rows: ROB + shiproom/gate + governance.

PHASE 5: COMMITTEE CHARTERS

> ROLE-LOCK-CHECK (Charters): All Membership field role names and all Decides field role names must appear in ROLE-NAME LOCK.

Charter per governance meeting in the rhythm table. All five fields:
- `Purpose`
- `Membership` -- minimum two roles as `[role name] ([domain type])`
- `Decides`
- `Escalates` -- named destination (not "everything not listed under Decides")
- `Quorum: [N] of [M] member roles required for binding decisions` (fraction format required)

Emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

PHASE 6: REGISTER AND ANALYSIS

**ORG-ELEMENT REGISTER**

All four categories:
- `cat-1 (Areas)` -- `- [area name] -- headcount: [N]`
- `cat-2 (Committees/Cadences)` -- `- [name]`
- `cat-3 (Headcount)` -- `- Total headcount: [N]`
- `cat-4 (DRI Roles)` -- `- [DRI role]`

**Org Evolution Roadmap**

`Trigger | Structural Change | Type`. Two rows minimum. Row 1: headcount threshold. Row 2: different category (workload signal, structural symptom, or milestone event).

**Anti-Pattern Watch**

`Anti-Pattern | Why It Applies Here | Mitigation`. Two rows minimum.
Every `Why It Applies Here`: `[element name] (cat-N) -- [one sentence]` with valid cat-N from ORG-ELEMENT REGISTER.

End with: `Generated by: /org-chart {topic} -- {date}`

---

## V-04 -- Combined: C-13 Contract + C-14 Form (Paired Mechanics)

**Axes**: C-13 (ROLE-NAME LOCK as explicit contract with downstream invoke instruction) + C-14 (four-field form as primary Rebuttal structure)
**Hypothesis**: C-13 and C-14 are structurally paired: C-13 defines the permitted name set, C-14 forces the model to name a role before it can write a breakdown. Combining them in a single variation that emphasizes both as a unit -- rather than introducing them independently -- produces higher joint compliance than either alone, because the model internalizes the pair as a coherent mechanic: lock names the set, form forces the selection.

---

You are running `/org-chart {topic}`.

THE ROLE CONTRACT -- READ BEFORE WRITING ANYTHING

This skill uses a two-part role contract that governs every section of the output:

1. **ROLE-NAME LOCK** (emitted after classification): the complete set of permitted role names for this document
2. **Rebuttal form** (used in Inertia Assessment): a four-field form where ROLE UNDER PRESSURE must be filled before any breakdown prose can begin

Both parts of the contract must be present and satisfied. Sections that name roles are checked against ROLE-NAME LOCK. The Rebuttal is written as the form -- not as free prose.

STEP 1 -- LOAD ROLES

Read `.craft/roles/`. Produce `ROLES-LOADED:` with one entry per role: `- [role name] -- [one-line description]`. If no files found: `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` with inferred roles in the same format. No other section until this block is written.

STEP 2 -- CLASSIFY ROLES

Immediately after ROLES-LOADED or ROLES-NOTE: `ROLE-TYPE-CLASSIFICATION:` block. One type per role: `Engineering / PM / Design / Operations / Research / Other`. Format: `- [role name] -- [domain type]`. Tier order: Engineering, then Operations, then PM / Design / Research / Other. Every loaded role classified. No unlisted roles added.

STEP 3 -- EMIT ROLE-NAME LOCK

Immediately after ROLE-TYPE-CLASSIFICATION:

```
ROLE-NAME LOCK
==============
Permitted role references for all subsequent sections:
[one bullet per role from ROLES-LOADED]

No role name may appear in any downstream section that is not listed above.
Downstream sections: ASCII diagram, rhythm DRI/Owner, charter Membership, charter Decides, all Inertia sub-sections.
```

Emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

STEP 4 -- INERTIA ASSESSMENT

Before any org diagram. Four sub-sections in order.

**Sub-section 1 -- Case for Staying Flat**

Mechanism table: `Mechanism Name | Type | Frequency / Participants`. Minimum two rows.
Type values only from: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.

Count rows. Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
Do not begin Sub-section 2 before this separator.

**Sub-section 2 -- How We Coordinate Today**

Active coordination patterns. No re-listing of mechanism rows.

**Sub-section 3 -- Rebuttal**

This sub-section is written as the four-field form. Do not substitute free prose.
Each field label is required. Each field is required. Order is fixed.

```
ROLE UNDER PRESSURE:
[Name exactly one role from ROLE-NAME LOCK. This field must be filled before OBSERVABLE BREAKDOWN can be written.]

OBSERVABLE BREAKDOWN:
[The current coordination failure that falls on the role named above. Must be present-tense and observable: blocked decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap. NOT a future growth projection.]

WHY EXISTING MECHANISMS FAIL:
[Why the mechanisms documented in Sub-section 1 cannot prevent or resolve the OBSERVABLE BREAKDOWN. Name at least one specific mechanism from the table and explain its insufficiency.]

RE-ASSESSMENT TRIGGER:
[The specific measurable threshold at which this verdict should be reconsidered: a hire count, a named milestone event, or a structural symptom. Not "revisit as the team grows."]
```

**Sub-section 4 -- VERDICT**

`FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing mechanism count and OBSERVABLE BREAKDOWN]`
Rating: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`
Declare: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Reference FLAT-CASE-PRESSURE by name.
Re-assessment trigger: quote the RE-ASSESSMENT TRIGGER field from Sub-section 3.

Emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

STEP 5 -- ASCII ORG DIAGRAM

All role names in diagram must appear in ROLE-NAME LOCK. At minimum two levels. Committees as distinct labeled nodes.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

STEP 6 -- HEADCOUNT BY AREA

`Area | Headcount | Key Roles | Decides | Escalates` -- five columns, Decides and Escalates separate.
Key Roles: `[role name] ([domain type])` -- all names from ROLE-NAME LOCK.
Minimum two area rows plus `**Total**`.

STEP 7 -- OPERATING RHYTHM TABLE

`Cadence | Frequency | DRI / Owner | Purpose`. Minimum three rows: ROB + shiproom/gate + governance.
DRI / Owner: all from ROLE-NAME LOCK. No merged rows.

STEP 8 -- COMMITTEE CHARTERS

Charter per governance meeting. Five fields:
- `Purpose`
- `Membership` -- minimum two roles from ROLE-NAME LOCK as `[role name] ([domain type])`
- `Decides`
- `Escalates` -- named destination
- `Quorum: [N] of [M] member roles required for binding decisions`

Emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

STEP 9 -- ORG-ELEMENT REGISTER

All four categories:
- `cat-1 (Areas)` -- `- [area name] -- headcount: [N]`
- `cat-2 (Committees/Cadences)` -- `- [name]`
- `cat-3 (Headcount)` -- `- Total headcount: [N]`
- `cat-4 (DRI Roles)` -- `- [DRI role]`

STEP 10 -- ORG EVOLUTION ROADMAP

`Trigger | Structural Change | Type`. Two rows minimum. Row 1: headcount threshold. Row 2: different category.

STEP 11 -- ANTI-PATTERN WATCH

`Anti-Pattern | Why It Applies Here | Mitigation`. Two rows minimum.
`Why It Applies Here`: `[element name] (cat-N) -- [one sentence]` with valid cat-N.

End with: `Generated by: /org-chart {topic} -- {date}`

---

## V-05 -- Combined: Format Contract + C-13 + C-14 + Per-Section Checks

**Axes**: Upfront format schemas (all table and form templates declared before output begins) + C-13 as reference contract + C-14 as enforced form template + per-section ROLE-LOCK-CHECKs at each post-classification section
**Hypothesis**: Full mechanical integration. The format contract eliminates schema ambiguity (merged Decides/Escalates, short-form Quorum). The role-name lock eliminates role drift. The four-field form template eliminates the fluent-default Rebuttal. The per-section checks activate the constraint locally at each boundary. The hypothesis is that layering all four does not over-constrain output -- the mechanisms are orthogonal, each targeting a different failure mode, so their combination produces higher joint rubric scores than any single-axis variation.

---

You are running `/org-chart {topic}`.

=== FORMAT CONTRACT AND ROLE CONTRACT -- READ BEFORE WRITING ANYTHING ===

The following contracts govern all output in this document. Reference them before writing each section.

---

**FORMAT CONTRACT**

All tables must match these schemas exactly. Refer here before writing each.

```
TABLE A -- Mechanism Evidence (Inertia Assessment, Sub-section 1)
Columns: Mechanism Name | Type | Frequency / Participants
Type vocabulary (closed): Channel / Informal Role / Recurring Cadence / Shared Artifact
Min rows: 2 data rows

TABLE B -- Headcount by Area
Columns: Area | Headcount | Key Roles | Decides | Escalates
CRITICAL: Decides and Escalates are TWO separate columns. Never merge as "Decision Scope".
Key Roles format: [role name] ([domain type])
Min rows: 2 area rows + 1 Total row

TABLE C -- Operating Rhythm
Columns: Cadence | Frequency | DRI / Owner | Purpose
Min rows: 3 distinct rows (ROB + shiproom/gate + governance meeting)
CRITICAL: Never combine two meetings into one row.

TABLE D -- Committee Charter (one block per governance meeting)
Required fields: Purpose / Membership / Decides / Escalates / Quorum
Membership format: [role name] ([domain type]), minimum 2 roles
Escalates: must name a destination -- never "everything not listed under Decides"
Quorum format REQUIRED: Quorum: [N] of [M] member roles required for binding decisions
CRITICAL: Short form "N roles required" is NOT accepted.

TABLE E -- Org Evolution Roadmap
Columns: Trigger | Structural Change | Type
Min rows: 2 rows; Row 1 = headcount threshold; Row 2 = DIFFERENT category

TABLE F -- Anti-Pattern Watch
Columns: Anti-Pattern | Why It Applies Here | Mitigation
Min rows: 2 rows
Why It Applies Here format: [element name] (cat-N) -- [one sentence]
(cat-N) MUST be a valid code from ORG-ELEMENT REGISTER
```

**REBUTTAL FORM CONTRACT**

The Rebuttal sub-section in the Inertia Assessment must use this exact four-field form.
Do not substitute free prose.

```
REBUTTAL FORM
=============
ROLE UNDER PRESSURE: [exactly one role from ROLE-NAME LOCK]
OBSERVABLE BREAKDOWN: [current failure -- present-tense observable, NOT "as we scale..."]
WHY EXISTING MECHANISMS FAIL: [name at least one mechanism from TABLE A and explain insufficiency]
RE-ASSESSMENT TRIGGER: [specific measurable threshold -- not "revisit as the team grows"]
```

---

STEP 1 -- LOAD ROLES

Read `.craft/roles/`. Produce `ROLES-LOADED:`: `- [role name] -- [one-line description]` per role. If no files found: `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` with inferred roles. No other section until complete.

STEP 2 -- CLASSIFY ROLES

Immediately after ROLES-LOADED or ROLES-NOTE: `ROLE-TYPE-CLASSIFICATION:` block. One type per role: `Engineering / PM / Design / Operations / Research / Other`. Format: `- [role name] -- [domain type]`. Tier order: Engineering, then Operations, then PM / Design / Research / Other. Every loaded role classified; no unlisted roles added.

STEP 3 -- ROLE-NAME LOCK

Immediately after ROLE-TYPE-CLASSIFICATION:

```
ROLE-NAME LOCK
==============
[list every role from ROLES-LOADED, one per line]

This is the complete permitted set. No role name may appear in any downstream section
unless it is listed here. Downstream sections checked against this lock:
  - ASCII diagram (all role names)
  - TABLE B Key Roles column
  - TABLE C DRI / Owner column
  - TABLE D Membership field
  - TABLE D Decides field
  - Rebuttal ROLE UNDER PRESSURE field
  - All Inertia sub-sections
```

Emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

STEP 4 -- INERTIA ASSESSMENT

**Sub-section 1 -- Case for Staying Flat** (use TABLE A)

Produce TABLE A. Two data rows minimum. Type values from closed vocabulary only.
Count rows. Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
Do not begin Sub-section 2 before separator.

**Sub-section 2 -- How We Coordinate Today**

Active coordination patterns. No re-listing TABLE A rows.

**Sub-section 3 -- Rebuttal** (use REBUTTAL FORM CONTRACT)

>> ROLE-LOCK-CHECK: ROLE UNDER PRESSURE must name a role from ROLE-NAME LOCK. <<

Produce the REBUTTAL FORM exactly as specified in the contract above. All four fields. Fixed order.

**Sub-section 4 -- VERDICT**

`FLAT-CASE-PRESSURE: [rating] -- [justification citing TABLE A row count and OBSERVABLE BREAKDOWN field]`
Rating: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`
Declare: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Reference FLAT-CASE-PRESSURE by name.
Re-assessment trigger: quote RE-ASSESSMENT TRIGGER field from the REBUTTAL FORM.

Emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

STEP 5 -- ASCII ORG DIAGRAM

>> ROLE-LOCK-CHECK: All role names in diagram must appear in ROLE-NAME LOCK. <<

Two levels minimum. Committees as distinct labeled nodes.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

STEP 6 -- HEADCOUNT BY AREA (use TABLE B)

>> ROLE-LOCK-CHECK: All Key Roles entries must name roles from ROLE-NAME LOCK. <<

Produce TABLE B. Apply ROLE-TYPE-CLASSIFICATION annotations. Two area rows minimum plus `**Total**`.

STEP 7 -- OPERATING RHYTHM (use TABLE C)

>> ROLE-LOCK-CHECK: All DRI / Owner entries must name roles from ROLE-NAME LOCK. <<

Produce TABLE C. Three rows minimum: ROB + shiproom/gate + governance. No merged rows.

STEP 8 -- COMMITTEE CHARTERS (use TABLE D)

>> ROLE-LOCK-CHECK: All Membership and Decides role names must appear in ROLE-NAME LOCK. <<

One TABLE D per governance meeting in TABLE C. Check FORMAT CONTRACT before writing Quorum.

Emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

STEP 9 -- ORG-ELEMENT REGISTER

`ORG-ELEMENT REGISTER` -- all four categories populated:
- `cat-1 (Areas)` -- `- [area name] -- headcount: [N]`
- `cat-2 (Committees/Cadences)` -- `- [name]`
- `cat-3 (Headcount)` -- `- Total headcount: [N]`
- `cat-4 (DRI Roles)` -- `- [DRI role]`

Do not proceed to TABLE E until all four categories are present.

STEP 10 -- ORG EVOLUTION ROADMAP (use TABLE E)

Produce TABLE E. Row 1: headcount threshold. Row 2: different category.

STEP 11 -- ANTI-PATTERN WATCH (use TABLE F)

Produce TABLE F. Every `Why It Applies Here` cell: `[element name] (cat-N) -- [one sentence]` with valid cat-N from ORG-ELEMENT REGISTER.

End with: `Generated by: /org-chart {topic} -- {date}`

---

*Generated by: /quest-variate corps-chart -- 2026-03-17*
