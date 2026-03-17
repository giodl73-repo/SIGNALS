---
skill: quest-variate
skill_target: corps-chart
date: 2026-03-17
round: 7
rubric: simulations/quest/rubrics/corps-chart-rubric-v6-2026-03-17.md
---

# Quest Variate — corps-chart (Round 7)

Five complete, runnable skill body variations for the `corps-chart` skill.
Single-axis first (V-01 through V-03), then combinations (V-04, V-05).

R7 targets rubric additions from v4–v6 that were absent from R1 and R3 variations:
C-15 (CAT-N-CITATION-SCHEMA), C-16 (TRIGGER-TYPE VOCABULARY), C-17 (5th phase gate),
C-18 (VERIFY blocks), C-19 (MECHANISM-TYPE VOCABULARY).

---

## Variation Summary

| ID | Axis | Target Criteria | Hypothesis |
|----|------|-----------------|------------|
| V-01 | MECHANISM-TYPE VOCABULARY (single axis) | C-19 | Emitting a named vocabulary block before the Flat-Case mechanism table makes Type-column compliance syntactically checkable, eliminating the prose-discipline failure mode where the model invents Type values not in the closed set |
| V-02 | VERIFY blocks (single axis) | C-18 | Placing present-tense disqualification statements immediately after each high-risk PRODUCE command closes known evasion modes that vocabulary locks alone cannot close — merged columns, duplicate trigger types, future-tense rebuttals |
| V-03 | CAT-N-CITATION-SCHEMA + TRIGGER-TYPE VOCABULARY pair (single round, two mechanisms) | C-15, C-16 | Introducing both inner-table vocabulary contracts together tests whether the shared structural-mechanism principle (named contract before table) transfers cleanly to the Anti-Pattern Watch and Org Evolution sections without requiring VERIFY support |
| V-04 | 5th phase gate + vocabulary-lock trilogy | C-15, C-16, C-17, C-19 | Adding a structural phase gate for Anti-Pattern Watch makes section omission visible at the gate level; all three vocabulary locks convert the remaining prose-discipline requirements into per-row checkable constraints |
| V-05 | Full integration: R3-V05 base + all v4–v6 mechanisms | C-13 through C-19 | Maximum mechanical enforcement: role-name lock as active contract + four-field Rebuttal form + all vocabulary locks + VERIFY blocks + 5th phase gate; tests whether layering all mechanisms over-constrains output or produces the highest aspirational score |

---

## V-01 — MECHANISM-TYPE VOCABULARY (single axis)

**Axis**: MECHANISM-TYPE VOCABULARY block before the Flat-Case mechanism table (C-19)
**Hypothesis**: If the mechanism table is introduced with an explicit named vocabulary block enumerating the closed Type set, the model has a syntactically checkable contract for every Type cell rather than a prose-embedded constraint. This eliminates the failure mode where a valid-sounding but non-vocabulary Type value (e.g. "Tool" or "Meeting") passes casual review.

---

You are running `/org-chart {topic}`.

ROLES — READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role: `- [role name] — [one-line description from role file]`.
DO NOT invent role names unless no role files are found.
If no files are found, DO produce `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` with one inferred entry per role in the same format.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER — THREE-TIER CLASSIFICATION SEQUENCE

DO classify roles in this strict three-tier order: Engineering types first, then Operations types, then PM / Design / Research / Other types. Complete all entries in one tier before writing any entry from the next tier. If no Engineering roles are present, begin with Operations types.

ROLE-TYPE-CLASSIFICATION — REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE, following the three-tier order above.
DO assign each role exactly one type from: `Engineering / PM / Design / Operations / Research / Other`.
DO format each entry as `- [role name] — [domain type]`.
DO NOT skip this block. DO NOT proceed until every loaded role is classified.
DO annotate each Key Roles cell in the Headcount table: `[role name] ([domain type])`.
DO annotate each Membership field in Committee Charters the same way.

When all roles are classified, emit: `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`
DO NOT proceed to the Inertia Assessment until this gate line is present.

INERTIA ASSESSMENT — FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes. DO structure it in this exact order:
Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

Sub-section 1 — Case for Staying Flat

Before writing the mechanism table, emit this vocabulary block exactly as shown:

```
MECHANISM-TYPE VOCABULARY
=========================
Permitted Type values for the mechanism table below:
  Channel          — async or sync communication path (Slack, email, standup)
  Informal Role    — person-as-coordinator without a formal title
  Recurring Cadence — scheduled meeting or review cycle
  Shared Artifact  — document, dashboard, or shared state that coordinates work

No row in the mechanism table may use a Type value outside this list.
```

Now produce a three-column mechanism evidence table with columns `Mechanism Name | Type | Frequency / Participants`.
Include at minimum two data rows. Every Type cell MUST contain one value from the MECHANISM-TYPE VOCABULARY above.
DO NOT use a Type value outside that vocabulary.

After writing the table, count the data rows (header excluded).
If count < 2, add the missing rows until count reaches 2.
Substitute the final count as N and emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
DO NOT emit this separator before count >= 2. DO NOT begin Sub-section 2 before this separator.

Sub-section 2 — How We Coordinate Today

Inventory the coordination patterns currently in active use. Name channels, cadences, informal roles, and artifacts with frequency and participants. DO NOT re-list entries from the Sub-section 1 table.

Sub-section 3 — Rebuttal

Name the coordination failure the flat-team case and current mechanisms cannot answer. Reference a specific observable: a blocked decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap. DO NOT write "the team is growing" without specifying the failure mode.

Sub-section 4 — VERDICT

MUST open with: `FLAT-CASE-PRESSURE: [rating] — [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
Rating MUST be exactly one value from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
After the pressure line, declare exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
Write a re-assessment trigger naming a concrete threshold. DO NOT write "revisit as the team grows."
DO NOT proceed past VERDICT until the pressure line, verdict declaration, and re-assessment trigger are all written.

When VERDICT is complete, emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

ASCII ORG DIAGRAM

DO draw an ASCII hierarchy. Show at minimum two levels. Show committees as distinct labeled nodes — not embedded in one area. DO NOT produce a flat list of names. Role names in the diagram must match ROLES-LOADED or ROLES-NOTE.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

DO produce a headcount table with columns `Area | Headcount | Key Roles | Decides | Escalates`.
DO NOT use a single `Decision Scope` column — Decides and Escalates are separate and both REQUIRED.
Populate Decides with decision types owned at this level. Populate Escalates with decision types referred upward, naming the destination role or forum.
Annotate each Key Roles entry: `[role name] ([domain type])`.
Include at minimum two area rows plus a `**Total**` row with the sum.

OPERATING RHYTHM TABLE

Produce a cadence table with columns `Cadence | Frequency | DRI / Owner | Purpose`.
Include at minimum three distinct rows covering: ROB, a shiproom or gate meeting, and a governance meeting.
DO NOT combine two meetings into one row. Reference a role from ROLES-LOADED in DRI / Owner where possible.

COMMITTEE CHARTERS

Write a charter for each governance meeting in the rhythm table with all five fields:
`Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`.
Annotate each Membership role: `[role name] ([domain type])`. List at minimum two roles per charter.
Escalates must name a destination — not "everything not listed under Decides."
Quorum format: `Quorum: [N] of [M] member roles required for binding decisions`.

When all charters are written, emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

MUST produce immediately after the charters phase gate with all four categories:
  `cat-1 (Areas)` — each area as `- [area name] — headcount: [N]`
  `cat-2 (Committees/Cadences)` — each as `- [name]`
  `cat-3 (Headcount)` — total as `- Total headcount: [N]`
  `cat-4 (DRI Roles)` — each DRI role from rhythm table as `- [DRI role]`
No category may be empty. DO NOT proceed to Org Evolution Roadmap until all four are populated.

ORG EVOLUTION ROADMAP

Produce a trigger table with columns `Trigger | Structural Change | Type`.
Include at minimum two rows. Row 1: a headcount threshold trigger. Row 2: a different category (workload signal, structural symptom, or milestone event). DO NOT use two headcount thresholds.

ANTI-PATTERN WATCH

Produce a table with columns `Anti-Pattern | Why It Applies Here | Mitigation`.
Include at minimum two rows. Every `Why It Applies Here` cell MUST open with: `[element name] (cat-N) — [one sentence]`.
DO NOT write a cell naming an element without the `(cat-N)` typed syntax.
cat-N codes must match categories in the ORG-ELEMENT REGISTER.

SECTION ORDER

Produce sections in this exact sequence:
1. ROLES-LOADED or ROLES-NOTE
2. ROLE-TYPE-CLASSIFICATION (three-tier order)
3. `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`
4. Inertia Assessment — [MECHANISM-TYPE VOCABULARY] / mechanism table / [FLAT-CASE-CLOSED] / How We Coordinate Today / Rebuttal / VERDICT [FLAT-CASE-PRESSURE first]
5. `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`
6. ASCII Org Diagram
7. `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`
8. Headcount by Area
9. Operating Rhythm Table
10. Committee Charters
11. `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`
12. ORG-ELEMENT REGISTER
13. Org Evolution Roadmap
14. Anti-Pattern Watch

End with: `Generated by: /org-chart {topic} — {date}`

---

## V-02 — VERIFY Blocks (single axis)

**Axis**: VERIFY blocks immediately after each high-risk PRODUCE command (C-18)
**Hypothesis**: Present-tense disqualification statements placed directly after PRODUCE commands close known evasion modes that vocabulary locks cannot close — specifically: merged Decision Scope columns, duplicate trigger category rows, and future-tense rebuttals. Each VERIFY block names the exact disqualifying output variant, making the failure syntactically recognizable rather than requiring rubric-level judgment.

---

You are running `/org-chart {topic}`.

ROLES — READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role: `- [role name] — [one-line description from role file]`.
DO NOT invent role names unless no role files are found.
If no files are found, DO produce `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` with one inferred entry per role in the same format.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER — THREE-TIER CLASSIFICATION SEQUENCE

DO classify roles in this strict three-tier order: Engineering types first, then Operations types, then PM / Design / Research / Other types. Complete all entries in one tier before writing any entry from the next. If no Engineering roles are present, begin with Operations types.

ROLE-TYPE-CLASSIFICATION — REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE, following the three-tier order.
Assign each role exactly one type from: `Engineering / PM / Design / Operations / Research / Other`.
Format each entry as `- [role name] — [domain type]`. Every loaded role must appear.
Annotate Key Roles cells in Headcount and Membership fields in Charters: `[role name] ([domain type])`.

When all roles are classified, emit: `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

INERTIA ASSESSMENT — FOUR SUB-SECTIONS, STEELMAN FIRST

Sub-section 1 — Case for Staying Flat

Produce a three-column mechanism evidence table with columns `Mechanism Name | Type | Frequency / Participants`.
Type values from closed vocabulary: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
Include at minimum two data rows.

After writing the table, count rows (header excluded). If count < 2, add rows until count reaches 2.
Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 — How We Coordinate Today

Inventory coordination patterns in active use (channels, cadences, informal roles, artifacts with frequency and participants). DO NOT re-list Sub-section 1 entries.

Sub-section 3 — Rebuttal

Name the coordination failure the flat-team case cannot answer. Reference a specific observable (blocked decision, missed SLA, time-zone gap, knowledge silo, competing roadmap).

VERIFY: A Rebuttal that opens with "As we scale..." or "as the team grows..." without naming a specific current failure mode does not satisfy this step.

Sub-section 4 — VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] — [justification citing mechanism count and failure mode]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
Declare exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
Write a concrete re-assessment trigger. DO NOT write "revisit as the team grows."

When VERDICT is complete, emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

ASCII ORG DIAGRAM

Draw an ASCII hierarchy with at minimum two levels. Show committees as distinct labeled nodes. Role names must match ROLES-LOADED or ROLES-NOTE.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

Produce a headcount table with columns `Area | Headcount | Key Roles | Decides | Escalates`.

VERIFY: A table with a `Decision Scope` column that merges Decides and Escalates into one column does not satisfy this step. The five-column schema is required: Area, Headcount, Key Roles, Decides, Escalates.

Populate Decides with decision types owned at this level. Populate Escalates with decisions referred upward, naming the destination role or forum. Annotate Key Roles: `[role name] ([domain type])`. Include at minimum two area rows plus a `**Total**` row.

OPERATING RHYTHM TABLE

Produce a cadence table with columns `Cadence | Frequency | DRI / Owner | Purpose`.
Include at minimum three distinct rows covering ROB, a shiproom or gate meeting, and a governance meeting.
DO NOT combine two meetings into one row.

COMMITTEE CHARTERS

Write a charter for each governance meeting with all five fields: `Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`.
Membership: at minimum two roles annotated `[role name] ([domain type])`.
Escalates must name a destination.

VERIFY: A Quorum field written as `Quorum: [N roles required for binding decisions]` without the denominator M does not satisfy this step. Required format: `Quorum: [N] of [M] member roles required for binding decisions`.

When all charters are written, emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

Produce immediately after the charters phase gate with all four categories:
  `cat-1 (Areas)` — `- [area name] — headcount: [N]`
  `cat-2 (Committees/Cadences)` — `- [name]`
  `cat-3 (Headcount)` — `- Total headcount: [N]`
  `cat-4 (DRI Roles)` — `- [DRI role]`

ORG EVOLUTION ROADMAP

Produce a trigger table with columns `Trigger | Structural Change | Type`.
Include at minimum two rows. Row 1: headcount threshold. Row 2: a different category.

VERIFY: Two rows that are both headcount threshold triggers do not satisfy this step. Row 2 must come from a different category: workload signal, structural symptom, or milestone event.

ANTI-PATTERN WATCH

Produce a table with columns `Anti-Pattern | Why It Applies Here | Mitigation`. Include at minimum two rows.
Every `Why It Applies Here` cell MUST open with: `[element name] (cat-N) — [specific relevance]`.

VERIFY: A `Why It Applies Here` cell that names an org element without the `(cat-N)` typed citation prefix does not satisfy this criterion for that row.

SECTION ORDER

1. ROLES-LOADED or ROLES-NOTE
2. ROLE-TYPE-CLASSIFICATION (three-tier)
3. `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`
4. Inertia Assessment (mechanism table / [FLAT-CASE-CLOSED] / How We Coordinate Today / Rebuttal [VERIFY: future-tense fails] / VERDICT)
5. `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`
6. ASCII Org Diagram
7. `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`
8. Headcount by Area [VERIFY: merged column fails]
9. Operating Rhythm Table
10. Committee Charters [VERIFY: short Quorum fails]
11. `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`
12. ORG-ELEMENT REGISTER
13. Org Evolution Roadmap [VERIFY: duplicate headcount threshold fails]
14. Anti-Pattern Watch [VERIFY: un-typed citation fails per row]

End with: `Generated by: /org-chart {topic} — {date}`

---

## V-03 — CAT-N-CITATION-SCHEMA + TRIGGER-TYPE VOCABULARY Pair

**Axis**: Two inner-table vocabulary contracts — TRIGGER-TYPE VOCABULARY before Org Evolution Roadmap and CAT-N-CITATION-SCHEMA before Anti-Pattern Watch (C-15, C-16)
**Hypothesis**: The shared named-contract principle (vocabulary block before table) transfers cleanly to both the Org Evolution and Anti-Pattern Watch sections without requiring VERIFY support. If the schema block is explicit enough — enumerating permitted values and the mandatory cell-prefix format — compliance becomes syntactically checkable without disqualification statements.

---

You are running `/org-chart {topic}`.

ROLES — READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block: `- [role name] — [one-line description from role file]` per role.
If no files are found, produce `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` with inferred roles.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER — THREE-TIER CLASSIFICATION SEQUENCE

Classify roles in this strict order: Engineering first, then Operations, then PM / Design / Research / Other.
Complete one tier before starting the next.

ROLE-TYPE-CLASSIFICATION — REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE.
Assign each role exactly one type from: `Engineering / PM / Design / Operations / Research / Other`.
Format: `- [role name] — [domain type]`. Every loaded role must appear.
Annotate Key Roles in Headcount: `[role name] ([domain type])`.
Annotate Membership in Charters: `[role name] ([domain type])`.

When all roles are classified, emit: `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

INERTIA ASSESSMENT

Write before any org boxes. Four sub-sections in this exact order.

Sub-section 1 — Case for Staying Flat

Produce a mechanism evidence table: columns `Mechanism Name | Type | Frequency / Participants`.
Type values from closed vocabulary: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
Minimum two data rows. After writing, count rows and emit:
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 — How We Coordinate Today

Inventory current coordination patterns. DO NOT re-list Sub-section 1 entries.

Sub-section 3 — Rebuttal

Name the coordination failure that the flat-team case cannot answer. Reference a specific observable.
DO NOT write "the team is growing" without specifying the failure mode.

Sub-section 4 — VERDICT

MUST open with: `FLAT-CASE-PRESSURE: [rating] — [justification]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
Declare: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Write a concrete re-assessment trigger.

When VERDICT is complete, emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

ASCII ORG DIAGRAM

Draw an ASCII hierarchy (minimum two levels). Committees as distinct labeled nodes. Role names from ROLES-LOADED.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

Produce a headcount table: `Area | Headcount | Key Roles | Decides | Escalates`.
DO NOT merge Decides and Escalates into a single Decision Scope column.
Decides: decision types owned at this level. Escalates: decisions referred upward (name the destination).
Key Roles annotated: `[role name] ([domain type])`. Minimum two area rows plus `**Total**`.

OPERATING RHYTHM TABLE

Cadence table: `Cadence | Frequency | DRI / Owner | Purpose`.
Minimum three rows: ROB, a shiproom or gate, and a governance meeting. No two meetings merged.

COMMITTEE CHARTERS

Charter for each governance meeting: `Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`.
Membership: minimum two roles annotated `[role name] ([domain type])`.
Escalates: names a destination. Quorum: `Quorum: [N] of [M] member roles required for binding decisions`.

When all charters are written, emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

Produce immediately after the charters gate:
  `cat-1 (Areas)` — `- [area name] — headcount: [N]`
  `cat-2 (Committees/Cadences)` — `- [name]`
  `cat-3 (Headcount)` — `- Total headcount: [N]`
  `cat-4 (DRI Roles)` — `- [DRI role]`
All four categories required. DO NOT proceed to Org Evolution Roadmap until all are populated.

ORG EVOLUTION ROADMAP

Before writing the trigger table, emit this vocabulary block:

```
TRIGGER-TYPE VOCABULARY
=======================
Permitted Type values for the trigger table below:
  headcount threshold  — a specific hire count that changes coordination needs
  workload signal      — a measurable increase in cross-area dependencies or throughput
  structural symptom   — an observable breakdown (missed SLAs, blocked decisions, decision latency)
  milestone event      — a named program event (GA, external launch, compliance review)

No two consecutive rows may share the same Type value.
```

Now produce the trigger table: `Trigger | Structural Change | Type`.
Minimum two rows. Row 1: headcount threshold type. Row 2: a different Type from the vocabulary above.

ANTI-PATTERN WATCH

Before writing the anti-pattern table, emit this schema block:

```
CAT-N-CITATION-SCHEMA
=====================
Valid cat-N codes from the ORG-ELEMENT REGISTER:
  cat-1 — Areas
  cat-2 — Committees/Cadences
  cat-3 — Headcount
  cat-4 — DRI Roles

Mandatory format for every "Why It Applies Here" cell:
  [element name] (cat-N) — [one sentence of specific relevance]

A cell that names an org element without the (cat-N) prefix does not satisfy this schema.
```

Now produce the anti-pattern table: `Anti-Pattern | Why It Applies Here | Mitigation`.
Minimum two rows. Every `Why It Applies Here` cell MUST use the `[element name] (cat-N) — [sentence]` format.

SECTION ORDER

1. ROLES-LOADED or ROLES-NOTE
2. ROLE-TYPE-CLASSIFICATION (three-tier)
3. `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`
4. Inertia Assessment (mechanism table / [FLAT-CASE-CLOSED] / How We Coordinate Today / Rebuttal / VERDICT)
5. `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`
6. ASCII Org Diagram
7. `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`
8. Headcount by Area
9. Operating Rhythm Table
10. Committee Charters
11. `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`
12. ORG-ELEMENT REGISTER
13. [TRIGGER-TYPE VOCABULARY] + Org Evolution Roadmap
14. [CAT-N-CITATION-SCHEMA] + Anti-Pattern Watch

End with: `Generated by: /org-chart {topic} — {date}`

---

## V-04 — 5th Phase Gate + Vocabulary-Lock Trilogy

**Axis**: Structural phase gate for Anti-Pattern Watch (C-17) combined with all three inner-table vocabulary locks: MECHANISM-TYPE VOCABULARY (C-19), TRIGGER-TYPE VOCABULARY (C-16), CAT-N-CITATION-SCHEMA (C-15)
**Hypothesis**: A dedicated phase gate makes Anti-Pattern Watch structurally non-skippable — its absence is a visible gate omission, not a silent skip. Combined with vocabulary locks at all three inner tables, this variation tests whether the section-presence problem (C-17) and the section-quality problem (C-15, C-16, C-19) can be solved simultaneously without VERIFY block support.

---

You are running `/org-chart {topic}`.

ROLES — READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block: `- [role name] — [one-line description from role file]` per role.
If no files are found, produce `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` with inferred roles.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER — THREE-TIER CLASSIFICATION SEQUENCE

Classify roles: Engineering first, then Operations, then PM / Design / Research / Other.
Complete one tier before starting the next. If no Engineering roles, begin with Operations.

ROLE-TYPE-CLASSIFICATION — REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE.
Assign each role exactly one type from: `Engineering / PM / Design / Operations / Research / Other`.
Format: `- [role name] — [domain type]`. Every loaded role must appear. No role absent from ROLES-LOADED may appear.
Annotate Key Roles in Headcount: `[role name] ([domain type])`.
Annotate Membership in Charters: `[role name] ([domain type])`.

When all roles are classified, emit: `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

INERTIA ASSESSMENT — FOUR SUB-SECTIONS, STEELMAN FIRST

Sub-section 1 — Case for Staying Flat

Before writing the mechanism table, emit this block:

```
MECHANISM-TYPE VOCABULARY
=========================
Permitted Type values for the mechanism table:
  Channel           — async or sync communication path
  Informal Role     — person-as-coordinator without a formal title
  Recurring Cadence — scheduled meeting or review cycle
  Shared Artifact   — document, dashboard, or shared state

No row may use a Type value outside this vocabulary.
```

Produce mechanism evidence table: `Mechanism Name | Type | Frequency / Participants`.
Minimum two data rows. Every Type cell: one value from the vocabulary above only.

Count data rows. If count < 2, add rows. Emit:
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

Sub-section 2 — How We Coordinate Today

Inventory current coordination patterns. DO NOT re-list Sub-section 1 entries.

Sub-section 3 — Rebuttal

Name the coordination failure the flat-team case cannot answer. Reference a specific observable. DO NOT write "the team is growing" without a failure mode.

Sub-section 4 — VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] — [justification citing mechanism count and failure mode]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
Declare: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Write a concrete re-assessment trigger.

When VERDICT is complete, emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

ASCII ORG DIAGRAM

Draw an ASCII hierarchy (minimum two levels). Committees as distinct labeled nodes. Names from ROLES-LOADED.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

Produce: `Area | Headcount | Key Roles | Decides | Escalates`. Five columns required.
Decides: decision types owned here. Escalates: decisions referred upward, naming destination.
Key Roles annotated: `[role name] ([domain type])`. Minimum two area rows plus `**Total**`.

OPERATING RHYTHM TABLE

Produce: `Cadence | Frequency | DRI / Owner | Purpose`. Minimum three rows: ROB, shiproom or gate, governance. No merged rows.

COMMITTEE CHARTERS

Charter per governance meeting: `Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`.
Membership: minimum two roles annotated `[role name] ([domain type])`.
Escalates: named destination. Quorum: `Quorum: [N] of [M] member roles required for binding decisions`.

When all charters are written, emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

Produce immediately after the charters gate:
  `cat-1 (Areas)` — `- [area name] — headcount: [N]`
  `cat-2 (Committees/Cadences)` — `- [name]`
  `cat-3 (Headcount)` — `- Total headcount: [N]`
  `cat-4 (DRI Roles)` — `- [DRI role]`

ORG EVOLUTION ROADMAP

Before writing the trigger table, emit:

```
TRIGGER-TYPE VOCABULARY
=======================
Permitted Type values:
  headcount threshold  — a specific hire count
  workload signal      — measurable increase in cross-area dependencies or throughput
  structural symptom   — observable breakdown (missed SLAs, blocked decisions)
  milestone event      — named program event (GA, launch, compliance date)

No two consecutive rows may share the same Type value.
```

Produce trigger table: `Trigger | Structural Change | Type`.
Minimum two rows. Row 1: headcount threshold. Row 2: different Type from vocabulary.

When the Org Evolution Roadmap table is complete, emit:
`=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===`
DO NOT begin Anti-Pattern Watch until this gate line is present.

ANTI-PATTERN WATCH

Before writing the anti-pattern table, emit:

```
CAT-N-CITATION-SCHEMA
=====================
Valid cat-N codes from the ORG-ELEMENT REGISTER:
  cat-1 — Areas
  cat-2 — Committees/Cadences
  cat-3 — Headcount
  cat-4 — DRI Roles

Required format for every "Why It Applies Here" cell:
  [element name] (cat-N) — [one sentence of specific relevance]

A cell that names an element without (cat-N) does not satisfy this schema.
```

Produce: `Anti-Pattern | Why It Applies Here | Mitigation`. Minimum two rows.
Every `Why It Applies Here` cell MUST use the `[element name] (cat-N) —` prefix format.

SECTION ORDER — 15 STEPS, 5 PHASE GATES

1. ROLES-LOADED or ROLES-NOTE
2. ROLE-TYPE-CLASSIFICATION (three-tier)
3. `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`
4. Inertia Assessment — [MECHANISM-TYPE VOCABULARY] / mechanism table / [FLAT-CASE-CLOSED] / How We Coordinate Today / Rebuttal / VERDICT
5. `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`
6. ASCII Org Diagram
7. `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`
8. Headcount by Area
9. Operating Rhythm Table
10. Committee Charters
11. `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`
12. ORG-ELEMENT REGISTER
13. [TRIGGER-TYPE VOCABULARY] + Org Evolution Roadmap
14. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===`
15. [CAT-N-CITATION-SCHEMA] + Anti-Pattern Watch

End with: `Generated by: /org-chart {topic} — {date}`

---

## V-05 — Full Integration

**Axis**: R3-V05 base (upfront format contract + active ROLE-NAME LOCK) + four-field Rebuttal form + all vocabulary locks (C-19, C-15, C-16) + VERIFY blocks (C-18) + 5th phase gate (C-17)
**Hypothesis**: Maximum mechanical enforcement across all aspirational criteria. The upfront format contract eliminates column-schema errors before any table is written. The ROLE-NAME LOCK as active per-section contract reduces role drift. The four-field Rebuttal form prevents future-tense failures. Vocabulary locks make each inner table's type column syntactically checkable. VERIFY blocks disqualify specific failure variants. The 5th phase gate makes Anti-Pattern Watch structurally non-skippable. Tests whether full constraint density produces the highest rubric score or whether cognitive overload causes section-skip failures.

---

You are running `/org-chart {topic}`.

UPFRONT FORMAT CONTRACT — READ BEFORE WRITING ANYTHING

The following table schemas apply throughout this document. No output produced before reading this block.

```
TABLE SCHEMAS
=============

Headcount by Area (Step 8):
  Area | Headcount | Key Roles | Decides | Escalates
  -- five columns; "Decision Scope" is NOT a valid column name
  -- Key Roles format: [role name] ([domain type])
  -- Total row required

Operating Rhythm (Step 9):
  Cadence | Frequency | DRI / Owner | Purpose

Committee Charter (Step 10, per governance meeting):
  Purpose: [text]
  Membership: [role name] ([domain type]), [role name] ([domain type]), ...
  Decides: [decision types owned at this level]
  Escalates: [decision types referred upward — name the destination]
  Quorum: [N] of [M] member roles required for binding decisions
  -- short form "Quorum: [N roles]" does NOT satisfy this schema

Mechanism Table (Inertia Step 1):
  Mechanism Name | Type | Frequency / Participants
  -- Type from closed set: Channel / Informal Role / Recurring Cadence / Shared Artifact

Org Evolution Roadmap (Step 13):
  Trigger | Structural Change | Type
  -- Type from: headcount threshold / workload signal / structural symptom / milestone event
  -- No two consecutive rows may share the same Type

Anti-Pattern Watch (Step 15):
  Anti-Pattern | Why It Applies Here | Mitigation
  -- Every "Why It Applies Here" cell: [element name] (cat-N) — [sentence]
  -- valid cat-N codes: cat-1 cat-2 cat-3 cat-4 (from ORG-ELEMENT REGISTER)
```

STEP 1 — LOAD ROLES

Read `.craft/roles/`. Produce `ROLES-LOADED:` block: `- [role name] — [one-line description]` per role.
If no files: produce `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` instead.
DO NOT write any other section until this block exists.

STEP 2 — CLASSIFY ROLES

Immediately after ROLES-LOADED or ROLES-NOTE, produce `ROLE-TYPE-CLASSIFICATION:`.
Assign each role exactly one type from: `Engineering / PM / Design / Operations / Research / Other`.
Format: `- [role name] — [domain type]`. Tier order: Engineering first, then Operations, then remaining.
Every loaded role must appear. No role absent from ROLES-LOADED may appear.

STEP 3 — EMIT ROLE-NAME LOCK

Immediately after ROLE-TYPE-CLASSIFICATION, emit this block:

```
ROLE-NAME LOCK
==============
The following roles are the complete set of permitted references for this document.
No role name may appear in any section below that is not listed here.

[list every role from ROLES-LOADED, one per line]

CHECK: Before writing any role name in the Rhythm Table DRI/Owner column, Charter
Membership/Decides fields, or Inertia sub-sections, verify it appears in this list.
```

When the ROLE-NAME LOCK block is present, emit:
`=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

STEP 4 — INERTIA ASSESSMENT

DO NOT draw any org boxes until the Inertia Assessment is complete. Four sub-sections in order.

Sub-section 1 — Case for Staying Flat

Emit before the mechanism table:

```
MECHANISM-TYPE VOCABULARY
=========================
  Channel           — async or sync communication path
  Informal Role     — person-as-coordinator without formal title
  Recurring Cadence — scheduled meeting or review cycle
  Shared Artifact   — document, dashboard, or shared state

No row may use a Type value outside this list.
```

Produce mechanism table per the schema above (minimum two rows). Every Type cell: vocabulary value only.
Count rows. If < 2, add rows. Emit: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded.] ---`

Sub-section 2 — How We Coordinate Today

Inventory current coordination patterns. DO NOT repeat Sub-section 1 entries.

Sub-section 3 — Rebuttal

Use this mandatory four-field form with these exact field labels in this order:

```
ROLE UNDER PRESSURE: [name exactly one role from ROLE-NAME LOCK]
OBSERVABLE BREAKDOWN: [describe a current coordination failure — not a future growth risk]
WHY EXISTING MECHANISMS FAIL: [explain why Sub-section 1 mechanisms do not resolve this breakdown]
RE-ASSESSMENT TRIGGER: [name a concrete measurable threshold — a hire count, milestone, or structural symptom]
```

VERIFY: A Rebuttal that fills `OBSERVABLE BREAKDOWN` with "As we scale..." or "as the team grows..." does not satisfy this step. The breakdown must describe a current failure, not a projected future risk.

Sub-section 4 — VERDICT

Open with: `FLAT-CASE-PRESSURE: [rating] — [justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
Declare: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Reasoning must reference FLAT-CASE-PRESSURE by name.
Re-assessment trigger from the four-field form applies here — do not repeat unless it differs.

When VERDICT is complete, emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

STEP 5 — ASCII ORG DIAGRAM

Draw ASCII hierarchy (minimum two levels). Committees as distinct labeled nodes — not embedded in any area box.
ROLE-NAME LOCK check: every role name in the diagram must appear in the ROLE-NAME LOCK list.

When complete, emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

STEP 6 — HEADCOUNT BY AREA

Produce per the TABLE SCHEMAS block (Step 0): `Area | Headcount | Key Roles | Decides | Escalates`.

VERIFY: A table with a `Decision Scope` column that merges Decides and Escalates does not satisfy this step. The five-column schema is required.

Minimum two area rows plus `**Total**`. Key Roles annotated `[role name] ([domain type])`.

STEP 7 — OPERATING RHYTHM TABLE

Produce per schema: `Cadence | Frequency | DRI / Owner | Purpose`. Minimum three rows: ROB, shiproom or gate, governance.
ROLE-NAME LOCK check: every role in DRI / Owner must appear in the ROLE-NAME LOCK list. No merged rows.

STEP 8 — COMMITTEE CHARTERS

Charter per governance rhythm row per the Charter schema above. Five fields each.
ROLE-NAME LOCK check: every role in Membership and Decides must appear in the ROLE-NAME LOCK list.

VERIFY: A Quorum field written as `Quorum: [N roles required for binding decisions]` without the fraction denominator M does not satisfy this step. Required: `Quorum: [N] of [M] member roles required for binding decisions`.

When all charters are written, emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

STEP 9 — ORG-ELEMENT REGISTER

Produce immediately after the charters gate:
  `cat-1 (Areas)` — `- [area name] — headcount: [N]`
  `cat-2 (Committees/Cadences)` — `- [name]`
  `cat-3 (Headcount)` — `- Total headcount: [N]`
  `cat-4 (DRI Roles)` — `- [DRI role]`
All four categories required. DO NOT proceed to Org Evolution Roadmap until all four are populated.

STEP 10 — ORG EVOLUTION ROADMAP

Emit before the trigger table:

```
TRIGGER-TYPE VOCABULARY
=======================
Permitted Type values:
  headcount threshold  — a specific hire count that changes coordination needs
  workload signal      — measurable increase in cross-area dependencies or throughput
  structural symptom   — observable breakdown (missed SLAs, blocked decisions, decision latency)
  milestone event      — named program event (GA, external launch, compliance review)

No two consecutive rows may share the same Type value.
```

Produce trigger table per schema (minimum two rows). Row 1: headcount threshold. Row 2: different Type.

VERIFY: Two rows that are both headcount threshold triggers do not satisfy this step. Row 2 must use a different Type from the vocabulary above.

When the Org Evolution Roadmap is complete, emit:
`=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===`
DO NOT begin Anti-Pattern Watch until this gate line is present.

STEP 11 — ANTI-PATTERN WATCH

Emit before the table:

```
CAT-N-CITATION-SCHEMA
=====================
Valid cat-N codes from the ORG-ELEMENT REGISTER:
  cat-1 — Areas
  cat-2 — Committees/Cadences
  cat-3 — Headcount
  cat-4 — DRI Roles

Required prefix for every "Why It Applies Here" cell:
  [element name] (cat-N) — [one sentence of specific relevance]

A cell that names an org element without the (cat-N) prefix does not satisfy this schema.
```

Produce per schema: `Anti-Pattern | Why It Applies Here | Mitigation`. Minimum two rows.
VERIFY: A `Why It Applies Here` cell that names an org element without the `(cat-N)` prefix does not satisfy the citation requirement for that row.

SECTION ORDER — 15 STEPS, 5 PHASE GATES

1. UPFRONT FORMAT CONTRACT
2. ROLES-LOADED or ROLES-NOTE
3. ROLE-TYPE-CLASSIFICATION (three-tier)
4. ROLE-NAME LOCK (active contract listing all permitted role names)
5. `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`
6. Inertia Assessment — [MECHANISM-TYPE VOCABULARY] / mechanism table / [FLAT-CASE-CLOSED] / How We Coordinate Today / [four-field Rebuttal form] / VERDICT [FLAT-CASE-PRESSURE first]
7. `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`
8. ASCII Org Diagram [ROLE-NAME LOCK check]
9. `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`
10. Headcount by Area [VERIFY: merged column fails]
11. Operating Rhythm Table [ROLE-NAME LOCK check]
12. Committee Charters [ROLE-NAME LOCK check] [VERIFY: short Quorum fails]
13. `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`
14. ORG-ELEMENT REGISTER
15. [TRIGGER-TYPE VOCABULARY] + Org Evolution Roadmap [VERIFY: duplicate threshold fails]
16. `=== [PHASE GATE: ORG-EVOLUTION COMPLETE — ANTI-PATTERN WATCH BEGINS] ===`
17. [CAT-N-CITATION-SCHEMA] + Anti-Pattern Watch [VERIFY: un-typed citation fails]

End with: `Generated by: /org-chart {topic} — {date}`
