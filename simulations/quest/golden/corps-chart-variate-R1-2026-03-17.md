---
skill: quest-variate
skill_target: corps-chart
date: 2026-03-17
round: 1
rubric: simulations/quest/rubrics/corps-chart-rubric-v1-2026-03-17.md
---

# Quest Variate — corps-chart (Round 1)

Five complete, runnable skill body variations for the `corps-chart` skill.
Single-axis first (V-01 through V-03), then combinations (V-04, V-05).

---

## Variation Summary

| ID | Axis | Hypothesis |
|----|------|------------|
| V-01 | Phrasing register | Conversational "will/should" style preserves structural correctness while reducing instruction density, lowering the risk of the model reading DO NOT constraints as blockers rather than guides |
| V-02 | Inertia framing | Positioning the flat team as the default winner until the rebuttal beats it forces richer failure-mode specificity and stronger FLAT-CASE-PRESSURE justifications |
| V-03 | Role sequence | Requiring loaded role names to appear explicitly in the mechanism table and Rebuttal grounds the inertia assessment in actual team composition rather than generic patterns, reducing C-01/C-06 drift |
| V-04 | V-01 + V-02 | Combining soft register with inertia-first framing produces richer inertia content without the cognitive overhead of rule lists |
| V-05 | V-02 + V-03 + Format contract | Stating all table schemas in a reference block upfront, plus role cross-reference injection and inertia-first framing, minimizes format errors by giving the model the contract before any output begins |

---

## V-01 — Phrasing Register (Conversational "will/should")

**Axis**: Phrasing register — formal/imperative DO/DO NOT replaced with conversational you-will/you-should
**Hypothesis**: Softer phrasing reduces rule-list cognitive load while preserving all structural requirements; may reduce cases where the model skips a section because it reads DO NOT as a hard block on output rather than a format guide.

---

You are running `/org-chart {topic}`.

STEP 1 — LOAD ROLES

Start by reading `.craft/roles/`. You will produce a `ROLES-LOADED:` block listing every role found, one per line in this format: `- [role name] — [one-line description from role file]`.

If no files are found, produce a `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` block instead, with one inferred role per line in the same format.

You should not write any other section until this block exists.

STEP 2 — CLASSIFY ROLES

Immediately after ROLES-LOADED or ROLES-NOTE, produce a `ROLE-TYPE-CLASSIFICATION:` block. Assign each role exactly one type from this closed set: `Engineering / PM / Design / Operations / Research / Other`. Format each entry as: `- [role name] — [domain type]`.

Classify in this tier order: Engineering types first, then Operations types, then PM / Design / Research / Other types. Complete all entries in one tier before starting the next tier.

Every role listed in ROLES-LOADED or ROLES-NOTE should appear in the classification. No role should appear in the classification that was not in the loaded block.

Once every role is classified, emit this exact line:
`=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

STEP 3 — INERTIA ASSESSMENT

Before drawing any org boxes, work through the question: could this team operate effectively without formal structure? Write four sub-sections in this exact order.

**Sub-section 1 — Case for Staying Flat**

Produce a three-column mechanism evidence table: `Mechanism Name | Type | Frequency / Participants`. Include at least two data rows. The Type column should use only these four values: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.

After writing the rows, count the data rows (header excluded). When you reach at least two rows, emit this separator: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

You should not begin Sub-section 2 until this separator is present.

**Sub-section 2 — How We Coordinate Today**

Describe the coordination patterns currently in active use: channels, cadences, informal roles, artifacts, with frequency and participants. Do not re-list mechanism rows from Sub-section 1.

**Sub-section 3 — Rebuttal**

Name the coordination failure that the flat-team case and current mechanisms cannot answer. Reference a specific observable — a blocked decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap. Do not write "the team is growing" unless you also name what specifically breaks when it does.

**Sub-section 4 — VERDICT**

Open this sub-section with a pressure rating line in this exact format:
`FLAT-CASE-PRESSURE: [rating] — [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`

The rating must be exactly one of: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.

You should not write the verdict declaration until this line is present. After the pressure line, declare exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. The reasoning sentence should reference the FLAT-CASE-PRESSURE rating by name.

Follow the verdict with a re-assessment trigger naming a concrete threshold (not "revisit as the team grows").

When the VERDICT sub-section is complete, emit:
`=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

STEP 4 — ASCII ORG DIAGRAM

Draw an ASCII hierarchy showing at least two levels of hierarchy. Committees should appear as distinct labeled nodes — not embedded inside an area box. Role names in the diagram should match those in ROLES-LOADED or ROLES-NOTE.

When the diagram is complete, emit:
`=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

STEP 5 — HEADCOUNT BY AREA

Produce a table with five columns: `Area | Headcount | Key Roles | Decides | Escalates`. Decides and Escalates are separate columns — do not merge them into a single "Decision Scope" column.

- Key Roles: annotate each entry as `[role name] ([domain type])` using classifications from ROLE-TYPE-CLASSIFICATION
- Decides: decision types owned at this level
- Escalates: decision types referred upward, naming the destination role or forum

Include at least two area rows with individual headcounts, plus a `**Total**` row with the sum. Do not produce only a single total with no area breakdown.

STEP 6 — OPERATING RHYTHM TABLE

Produce a cadence table with columns `Cadence | Frequency | DRI / Owner | Purpose`. Include at least three distinct rows covering: (a) ROB, (b) a shiproom or gate meeting, (c) a governance meeting. Do not combine two meetings into one row, and do not produce a rhythm table with only ROB. Reference a role from ROLES-LOADED in the DRI / Owner column where possible.

STEP 7 — COMMITTEE CHARTERS

Write a charter for each governance meeting listed in the rhythm table. Every charter must include all five fields:

- `Purpose`
- `Membership` — list at least two roles, annotated as `[role name] ([domain type])`
- `Decides`
- `Escalates` — name a destination; do not write "everything not listed under Decides"
- `Quorum` — use this exact format: `Quorum: [N] of [M] member roles required for binding decisions`, where N is the minimum count and M is the total roles in Membership

Do not use the short form `Quorum: N roles required`. The fraction form (N of M) is required.

When all charters are written, emit:
`=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

STEP 8 — ORG-ELEMENT REGISTER

Immediately after the charters gate, produce an `ORG-ELEMENT REGISTER` block with all four categories populated. Do not proceed to the Org Evolution Roadmap until all four are present:

- `cat-1 (Areas)` — all area names from the Headcount table, format: `- [area name] — headcount: [N]`
- `cat-2 (Committees/Cadences)` — all committee and cadence names from the Rhythm Table and Charters, format: `- [name]`
- `cat-3 (Headcount)` — total headcount, format: `- Total headcount: [N]`
- `cat-4 (DRI Roles)` — all DRI role names from the Operating Rhythm Table, format: `- [DRI role]`

STEP 9 — ORG EVOLUTION ROADMAP

Produce a trigger table with columns `Trigger | Structural Change | Type`. Include at least two rows. Row 1 should be a headcount threshold trigger. Row 2 must come from a different category: a workload signal, structural symptom, or milestone event. Two headcount thresholds do not satisfy this requirement.

STEP 10 — ANTI-PATTERN WATCH

Produce a table with columns `Anti-Pattern | Why It Applies Here | Mitigation`. Include at least two rows. Every `Why It Applies Here` cell must open with typed citation syntax: `[element name] (cat-N) — [one sentence of specific relevance]`, using a valid cat-N code from the ORG-ELEMENT REGISTER. Do not name an org element in this column without the (cat-N) typed syntax.

End with: `Generated by: /org-chart {topic} — {date}`

---

## V-02 — Inertia Framing (Flat team wins by default)

**Axis**: Inertia framing — structure must earn its place; flat coordination is the default winner until the rebuttal proves otherwise
**Hypothesis**: Framing the flat team as the presumptive winner forces the model to make the Rebuttal do real argumentative work, producing more specific failure modes and better FLAT-CASE-PRESSURE justifications rather than boilerplate "as the team grows" verdicts.

---

You are running `/org-chart {topic}`.

OPENING FRAME: THE BURDEN OF PROOF

Formal org structure is expensive — it adds coordination overhead, slows decisions, and requires ongoing maintenance. Flat coordination wins by default. For structure to be warranted, it must answer a specific failure the flat team cannot.

This skill works through that question before drawing any boxes.

STEP 1 — LOAD ROLES

Read `.craft/roles/`. Produce a `ROLES-LOADED:` block listing every role found: `- [role name] — [one-line description from role file]`. If no files are found, produce `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` followed by inferred roles in the same format.

DO NOT write any other section until this block exists.

STEP 2 — CLASSIFY ROLES

Immediately after ROLES-LOADED or ROLES-NOTE, produce a `ROLE-TYPE-CLASSIFICATION:` block. Assign each role exactly one type: `Engineering / PM / Design / Operations / Research / Other`. Format: `- [role name] — [domain type]`.

Tier order: Engineering first, then Operations, then PM / Design / Research / Other. Complete one tier before starting the next. Every loaded role must be classified. No role may appear in classification that was absent from the loaded block.

Emit: `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

STEP 3 — INERTIA ASSESSMENT

The flat team has already won. Four sub-sections now determine whether structure can beat it.

**Sub-section 1 — Case for Staying Flat (the winning side)**

The flat-team case is strong until proven otherwise. Build the best possible case for staying flat:

Produce a mechanism evidence table: `Mechanism Name | Type | Frequency / Participants`. Minimum two data rows. Type values from closed vocabulary only: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.

Name only specific, observable coordination mechanisms — not aspirational ones. Each row is evidence that structure is not yet needed.

After writing the rows, count them (header excluded). Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

DO NOT begin Sub-section 2 before this separator.

**Sub-section 2 — How We Coordinate Today (the status quo)**

Inventory the coordination patterns currently running. Name channels, cadences, informal roles, and artifacts with frequency and participants. This is the system that structure would displace. Do not re-list mechanism rows from Sub-section 1.

**Sub-section 3 — Rebuttal (the challenge to the flat team)**

This is where structure makes its case. Name the exact failure that the flat team and its current mechanisms cannot prevent or recover from. It must be:

- A specific observable: blocked decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap
- Tied to the actual team composition loaded in ROLES-LOADED — name the role or roles involved in the failure
- Not a growth projection — name what breaks now or at a concrete near threshold

If you cannot name a specific, observable failure, write `STRUCTURE-NOT-YET-WARRANTED` and stop. Do not invent a rebuttal.

**Sub-section 4 — VERDICT (the ruling)**

Open with the pressure rating — this quantifies how strong the flat-team case was:
`FLAT-CASE-PRESSURE: [rating] — [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`

Rating from closed set only: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`

DO NOT emit the verdict declaration before this line is present.

Declare exactly one: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. The reasoning sentence must reference FLAT-CASE-PRESSURE by name and explain how the Sub-section 3 rebuttal overcame (or failed to overcome) the flat-case pressure.

Write a re-assessment trigger: name the exact condition that would flip the verdict. Name a concrete threshold — headcount, SLA breach count, roadmap conflict count. Do not write "revisit as the team grows."

Emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

STEP 4 — ASCII ORG DIAGRAM

Only draw this if STRUCTURE-WARRANTED was declared. If CAN-OPERATE-FLAT, still produce the diagram as a proposed structure for the trigger-condition future state, labeled accordingly.

Draw an ASCII hierarchy with at least two levels. Committees as distinct labeled nodes, not embedded in area boxes. Role names must match ROLES-LOADED or ROLES-NOTE.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

STEP 5 — HEADCOUNT BY AREA

Table with five columns: `Area | Headcount | Key Roles | Decides | Escalates`.
DO NOT use a merged `Decision Scope` column. Decides and Escalates are separate.

- Key Roles: `[role name] ([domain type])` from ROLE-TYPE-CLASSIFICATION
- Decides: decision types owned at this area level
- Escalates: decision types referred upward — name the destination role or forum

Minimum two area rows plus `**Total**` row with sum.

STEP 6 — OPERATING RHYTHM TABLE

Columns: `Cadence | Frequency | DRI / Owner | Purpose`.
Minimum three distinct rows: (a) ROB, (b) shiproom or gate, (c) governance meeting.
Do not merge two meetings into one row. Reference a loaded role in DRI / Owner.

STEP 7 — COMMITTEE CHARTERS

Charter for every governance meeting in the rhythm table. Five fields required per charter:

- `Purpose`
- `Membership` — minimum two roles as `[role name] ([domain type])`
- `Decides`
- `Escalates` — named destination, not "everything not listed under Decides"
- `Quorum: [N] of [M] member roles required for binding decisions`

The fraction format (N of M) is required. Short form `N roles required` is not accepted.

Emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

STEP 8 — ORG-ELEMENT REGISTER

`ORG-ELEMENT REGISTER` block with all four categories:

- `cat-1 (Areas)` — `- [area name] — headcount: [N]`
- `cat-2 (Committees/Cadences)` — `- [name]`
- `cat-3 (Headcount)` — `- Total headcount: [N]`
- `cat-4 (DRI Roles)` — `- [DRI role]`

No category may be empty or missing.

STEP 9 — ORG EVOLUTION ROADMAP

Trigger table: `Trigger | Structural Change | Type`. Minimum two rows.
Row 1: headcount threshold trigger.
Row 2: different category — workload signal, structural symptom, or milestone event.
Two headcount thresholds do not satisfy this requirement.

STEP 10 — ANTI-PATTERN WATCH

Table: `Anti-Pattern | Why It Applies Here | Mitigation`. Minimum two rows.
Every `Why It Applies Here` cell opens with: `[element name] (cat-N) — [one sentence]`
Valid cat-N code from ORG-ELEMENT REGISTER only. No element cited without typed syntax.

End with: `Generated by: /org-chart {topic} — {date}`

---

## V-03 — Role Sequence (Roles cross-referenced into Inertia)

**Axis**: Role sequence — after loading and classifying roles, the inertia sub-sections explicitly require role names to appear in mechanism rows and the Rebuttal
**Hypothesis**: Requiring loaded role names in the mechanism table and Rebuttal grounds the inertia assessment in actual team composition, reducing the risk of generic "as the team grows" failure modes and improving the specificity of FLAT-CASE-PRESSURE justifications.

---

You are running `/org-chart {topic}`.

STEP 1 — LOAD ROLES

Read `.craft/roles/`. Produce a `ROLES-LOADED:` block with one entry per role: `- [role name] — [one-line description from role file]`. If no files are found, produce `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` with inferred roles in the same format.

DO NOT write any other section until this block exists.

STEP 2 — CLASSIFY ROLES

Immediately after ROLES-LOADED or ROLES-NOTE, produce a `ROLE-TYPE-CLASSIFICATION:` block. Assign each role exactly one type: `Engineering / PM / Design / Operations / Research / Other`. Format: `- [role name] — [domain type]`.

Tier order: Engineering first, then Operations, then PM / Design / Research / Other. Complete one tier before starting the next. Every loaded role must be classified. No role may appear in classification that was absent from the loaded block.

After classification, note the loaded role names — you will use them explicitly in Steps 3a and 3c below.

Emit: `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

STEP 3 — INERTIA ASSESSMENT

Four sub-sections in this order. Steps 3a and 3c require direct use of role names from ROLES-LOADED.

**Sub-section 3a — Case for Staying Flat**

Produce a mechanism evidence table: `Mechanism Name | Type | Frequency / Participants`.
Minimum two data rows. Type values: `Channel / Informal Role / Recurring Cadence / Shared Artifact` only.

ROLE CROSS-REFERENCE REQUIRED: At least one row in the Mechanism Name column must name a specific role from ROLES-LOADED as a participant or owner of that mechanism (e.g., "Weekly sync run by [role name]" or "[role name] acts as de facto PM for cross-team requests"). Mechanisms that reference actual loaded roles score higher than generic mechanisms.

After writing the rows, count them (header excluded). Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

DO NOT begin Sub-section 3b before this separator.

**Sub-section 3b — How We Coordinate Today**

Inventory the coordination patterns currently in active use: channels, cadences, informal roles, artifacts with frequency and participants. Do not re-list mechanism rows from Sub-section 3a.

**Sub-section 3c — Rebuttal**

ROLE-GROUNDED FAILURE REQUIRED: Name the coordination failure using specific role names from ROLES-LOADED. The failure mode must identify which role or pair of roles is involved (e.g., "decisions that require both [role A] and [role B] block at the interface because neither has a defined escalation path"). Do not describe a failure mode without naming the role context.

Reference a specific observable: a blocked decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap.

**Sub-section 3d — VERDICT**

Open with: `FLAT-CASE-PRESSURE: [rating] — [one-sentence justification citing Sub-section 3a mechanism count and Sub-section 3c failure mode]`

Rating from closed set: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`

DO NOT emit the verdict declaration before this line. Declare exactly one: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Reference FLAT-CASE-PRESSURE by name in the reasoning sentence.

Write a re-assessment trigger naming a concrete threshold. Do not write "revisit as the team grows."

Emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

STEP 4 — ASCII ORG DIAGRAM

Draw an ASCII hierarchy with at least two levels. Committees as distinct labeled nodes, not embedded in area boxes. Role names must match ROLES-LOADED or ROLES-NOTE — no new role names introduced.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

STEP 5 — HEADCOUNT BY AREA

Table with five columns: `Area | Headcount | Key Roles | Decides | Escalates`.
DO NOT merge Decides and Escalates into a single column.

- Key Roles: `[role name] ([domain type])` from ROLE-TYPE-CLASSIFICATION
- Decides: decision types owned at this area level
- Escalates: decision types referred upward — name destination role or forum

Minimum two area rows plus `**Total**` row with sum.

STEP 6 — OPERATING RHYTHM TABLE

Columns: `Cadence | Frequency | DRI / Owner | Purpose`.
Minimum three distinct rows: (a) ROB, (b) shiproom or gate, (c) governance meeting.
Do not merge two meetings into one row. Reference a loaded role in DRI / Owner.

STEP 7 — COMMITTEE CHARTERS

Charter for every governance meeting in the rhythm table. All five fields required:

- `Purpose`
- `Membership` — minimum two roles as `[role name] ([domain type])`
- `Decides`
- `Escalates` — named destination, not "everything not listed under Decides"
- `Quorum: [N] of [M] member roles required for binding decisions` (fraction format required)

DO NOT use the short form `N roles required`.

Emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

STEP 8 — ORG-ELEMENT REGISTER

`ORG-ELEMENT REGISTER` block with all four categories:

- `cat-1 (Areas)` — `- [area name] — headcount: [N]`
- `cat-2 (Committees/Cadences)` — `- [name]`
- `cat-3 (Headcount)` — `- Total headcount: [N]`
- `cat-4 (DRI Roles)` — `- [DRI role]`

All four categories must be populated. Do not proceed to Org Evolution Roadmap until complete.

STEP 9 — ORG EVOLUTION ROADMAP

Trigger table: `Trigger | Structural Change | Type`. Minimum two rows.
Row 1: headcount threshold trigger.
Row 2: different category — workload signal, structural symptom, or milestone event.

STEP 10 — ANTI-PATTERN WATCH

Table: `Anti-Pattern | Why It Applies Here | Mitigation`. Minimum two rows.
Every `Why It Applies Here` cell: `[element name] (cat-N) — [one sentence]` using valid cat-N from ORG-ELEMENT REGISTER.

End with: `Generated by: /org-chart {topic} — {date}`

---

## V-04 — Combined: Conversational Register + Inertia-Led Framing

**Axes**: V-01 (phrasing register) + V-02 (inertia framing)
**Hypothesis**: Combining soft phrasing with inertia-first framing reduces instruction friction while producing richer inertia content — the model engages with the question rather than executing a rule list.

---

You are running `/org-chart {topic}`.

FRAMING: DOES THIS TEAM NEED STRUCTURE?

Formal org structure carries overhead — added decision latency, maintenance cost, coordination tax. This skill starts with the honest question: would this team be better served staying flat?

Work through that question before drawing any boxes.

LOADING ROLES

Start by reading `.craft/roles/`. You'll produce a `ROLES-LOADED:` block — one entry per role found: `- [role name] — [one-line description from role file]`.

If no files are there, use `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` and list inferred roles in the same format. Nothing else should be written until this block exists.

CLASSIFYING ROLES

Right after the loaded block, produce a `ROLE-TYPE-CLASSIFICATION:` block. Each role gets exactly one type: `Engineering / PM / Design / Operations / Research / Other`. Format: `- [role name] — [domain type]`.

Go in tier order: Engineering first, then Operations, then PM / Design / Research / Other. Finish one tier before starting the next. Every loaded role should appear in classification. No classification entry should reference a role that wasn't loaded.

When done with classification, emit:
`=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

INERTIA ASSESSMENT — THE MAIN QUESTION

The flat team wins until proven otherwise. Work through four sub-sections to determine if structure earns its place.

**The Case for Staying Flat**

Build the strongest possible case for not adding structure. Produce a mechanism table: `Mechanism Name | Type | Frequency / Participants`. You'll want at least two rows. Type values are constrained to: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.

Each row should name a real, observable coordination mechanism — not a hypothetical one. These are the things that make structure look unnecessary.

After writing the rows, count them. When you have at least two, emit:
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

**How We Coordinate Today**

Describe what's actually running: channels, cadences, informal roles, artifacts. Include frequency and who participates. Don't re-list mechanism rows from the table above.

**The Rebuttal**

Now make the case for structure. Name the specific failure the flat team cannot prevent. This should be tied to a real observable — a decision that keeps getting blocked, an SLA that can't be met with current coordination, a knowledge silo forming around a specific area, or two roadmaps in active conflict. Be specific: what breaks and who gets stuck.

If there's no real failure to name, say so. Don't invent one.

**VERDICT**

Open with the pressure line — it quantifies how strong the flat-team case was:
`FLAT-CASE-PRESSURE: [rating] — [justification citing mechanism count from the Case for Staying Flat and the failure mode from the Rebuttal]`

Rating options: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`

The pressure line should come before the verdict declaration. Then declare one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. The reasoning should explain how the Rebuttal fared against the flat-case pressure.

Close with a re-assessment trigger — a concrete condition that would flip the verdict. Make it measurable (a headcount number, a missed SLA count, a specific milestone), not "revisit as the team grows."

Emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

THE ORG DIAGRAM

Draw an ASCII hierarchy with at least two levels. Committees get their own nodes — don't fold them into an area box. Role names should match what you loaded.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

A five-column table: `Area | Headcount | Key Roles | Decides | Escalates`. Keep Decides and Escalates as separate columns — don't merge them into a single "Decision Scope" column.

- Key Roles: `[role name] ([domain type])` from your classification
- Decides: what decisions this area owns at its level
- Escalates: what it refers upward, naming where it goes

At least two area rows plus a `**Total**` row.

OPERATING RHYTHM TABLE

Four columns: `Cadence | Frequency | DRI / Owner | Purpose`. At least three distinct rows covering ROB, a shiproom or gate, and a governance meeting. Two meetings shouldn't share a row, and the table shouldn't have only ROB. Pull a loaded role into the DRI / Owner column where you can.

COMMITTEE CHARTERS

A charter for each governance meeting in the rhythm table. Every charter needs all five fields:

- `Purpose`
- `Membership` — at least two roles as `[role name] ([domain type])`
- `Decides`
- `Escalates` — a named destination, not "everything not in Decides"
- `Quorum: [N] of [M] member roles required for binding decisions`

The full fraction format (N of M) is required. The short form `N roles required` isn't sufficient.

Emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

After the charters gate, produce the `ORG-ELEMENT REGISTER`. All four categories need to be populated:

- `cat-1 (Areas)` — `- [area name] — headcount: [N]`
- `cat-2 (Committees/Cadences)` — `- [name]`
- `cat-3 (Headcount)` — `- Total headcount: [N]`
- `cat-4 (DRI Roles)` — `- [DRI role]`

ORG EVOLUTION ROADMAP

Trigger table: `Trigger | Structural Change | Type`. Two rows minimum. Row 1 is a headcount threshold. Row 2 comes from a different category: workload signal, structural symptom, or milestone event. Two headcount rows don't count.

ANTI-PATTERN WATCH

Table: `Anti-Pattern | Why It Applies Here | Mitigation`. Two rows minimum. Every "Why It Applies Here" cell opens with typed citation: `[element name] (cat-N) — [one sentence]` using a valid cat-N from the ORG-ELEMENT REGISTER.

End with: `Generated by: /org-chart {topic} — {date}`

---

## V-05 — Combined: Format Contract + Inertia-Led + Role Cross-Reference

**Axes**: Output format contract (all table schemas declared upfront) + V-02 (inertia-first) + V-03 (role cross-reference into inertia)
**Hypothesis**: Declaring all required table schemas in a reference block before any output begins, combined with inertia-first framing and role-grounded inertia sub-sections, minimizes the two most common format failures (merged Decides/Escalates columns and short-form Quorum) by giving the model the contract before it writes anything.

---

You are running `/org-chart {topic}`.

FORMAT CONTRACT — READ BEFORE WRITING ANYTHING

All tables in this output must match these exact schemas. Refer back to this section before writing each table.

```
TABLE A — Mechanism Evidence (used in Inertia Assessment, Sub-section 1)
Columns: Mechanism Name | Type | Frequency / Participants
Type closed vocabulary: Channel / Informal Role / Recurring Cadence / Shared Artifact
Min rows: 2 data rows

TABLE B — Headcount by Area
Columns: Area | Headcount | Key Roles | Decides | Escalates
NOTE: Decides and Escalates are TWO separate columns. Never merge as "Decision Scope".
Key Roles format: [role name] ([domain type])
Min rows: 2 area rows + 1 Total row

TABLE C — Operating Rhythm
Columns: Cadence | Frequency | DRI / Owner | Purpose
Min rows: 3 distinct rows (ROB + shiproom/gate + governance meeting)
NOTE: Never combine two meetings into one row

TABLE D — Committee Charter (one block per governance meeting)
Fields: Purpose / Membership / Decides / Escalates / Quorum
Membership format: [role name] ([domain type]), minimum 2 roles
Escalates: must name a destination — never "everything not in Decides"
Quorum format: Quorum: [N] of [M] member roles required for binding decisions
NOTE: Fraction format (N of M) required. Short form "N roles required" is NOT accepted.

TABLE E — Org Evolution Roadmap
Columns: Trigger | Structural Change | Type
Min rows: 2 rows, Row 1 = headcount threshold, Row 2 = different category

TABLE F — Anti-Pattern Watch
Columns: Anti-Pattern | Why It Applies Here | Mitigation
Min rows: 2 rows
Why It Applies Here format: [element name] (cat-N) — [one sentence]
(cat-N) must be a valid code from the ORG-ELEMENT REGISTER
```

STEP 1 — LOAD ROLES

Read `.craft/roles/`. Produce a `ROLES-LOADED:` block: `- [role name] — [one-line description from role file]` per role found. If no files are found: `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` with inferred roles in the same format. DO NOT write any other section until this block exists.

STEP 2 — CLASSIFY ROLES

Immediately after ROLES-LOADED or ROLES-NOTE, produce a `ROLE-TYPE-CLASSIFICATION:` block. One type per role from: `Engineering / PM / Design / Operations / Research / Other`. Format: `- [role name] — [domain type]`. Tier order: Engineering → Operations → PM / Design / Research / Other. Complete one tier before starting the next. Every loaded role must be classified. No role may appear in classification that was absent from the loaded block.

After classification, hold the loaded role names in mind — they are required in Steps 3a and 3c.

Emit: `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

STEP 3 — INERTIA ASSESSMENT

Structure must earn its place. The flat team wins by default. Work through four sub-sections.

**Sub-section 3a — Case for Staying Flat** (use TABLE A)

Produce TABLE A (see Format Contract). At least two data rows. Type values from closed vocabulary only.

ROLE CROSS-REFERENCE: At least one row must name a role from ROLES-LOADED in the Mechanism Name or Frequency / Participants column. Mechanisms grounded in actual loaded roles are stronger evidence for the flat-case.

Count data rows. Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
DO NOT begin Sub-section 3b before this separator.

**Sub-section 3b — How We Coordinate Today**

Inventory active coordination patterns. Name channels, cadences, informal roles, artifacts with frequency and participants. Do not re-list TABLE A rows.

**Sub-section 3c — Rebuttal**

ROLE-GROUNDED FAILURE: Name the coordination failure using specific role names from ROLES-LOADED. Identify which role or pair of roles is involved in the failure and why existing mechanisms cannot resolve it. Reference a specific observable: blocked decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap.

**Sub-section 3d — VERDICT**

Open with: `FLAT-CASE-PRESSURE: [rating] — [one-sentence justification citing Sub-section 3a mechanism count and Sub-section 3c failure mode]`

Rating from closed set: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`

DO NOT emit the verdict declaration before this line is present. Declare exactly one: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Reference FLAT-CASE-PRESSURE by name.

Write a re-assessment trigger: concrete threshold, not "revisit as the team grows."

Emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

STEP 4 — ASCII ORG DIAGRAM

Draw ASCII hierarchy with at least two levels. Committees as distinct labeled nodes. Role names must match ROLES-LOADED or ROLES-NOTE — no new names.

Emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

STEP 5 — HEADCOUNT BY AREA (use TABLE B)

Produce TABLE B (see Format Contract). Apply ROLE-TYPE-CLASSIFICATION annotations in Key Roles column. Minimum two area rows + Total row.

STEP 6 — OPERATING RHYTHM (use TABLE C)

Produce TABLE C (see Format Contract). Minimum three distinct rows: ROB + shiproom/gate + governance. No merged rows. DRI / Owner references a loaded role where possible.

STEP 7 — COMMITTEE CHARTERS (use TABLE D)

One TABLE D charter block per governance meeting in TABLE C. All five fields required. Quorum must use fraction form (N of M). Check Format Contract before writing.

Emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

STEP 8 — ORG-ELEMENT REGISTER

`ORG-ELEMENT REGISTER` with all four categories populated:

- `cat-1 (Areas)` — `- [area name] — headcount: [N]`
- `cat-2 (Committees/Cadences)` — `- [name]`
- `cat-3 (Headcount)` — `- Total headcount: [N]`
- `cat-4 (DRI Roles)` — `- [DRI role]`

DO NOT proceed to Org Evolution Roadmap until all four categories are populated.

STEP 9 — ORG EVOLUTION ROADMAP (use TABLE E)

Produce TABLE E (see Format Contract). Row 1: headcount threshold. Row 2: different category.

STEP 10 — ANTI-PATTERN WATCH (use TABLE F)

Produce TABLE F (see Format Contract). Every `Why It Applies Here` cell must use `(cat-N)` syntax from the ORG-ELEMENT REGISTER.

End with: `Generated by: /org-chart {topic} — {date}`

---

*Generated by: /quest-variate corps-chart — 2026-03-17*
