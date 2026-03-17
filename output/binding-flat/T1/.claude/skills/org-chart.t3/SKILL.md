---
name: org-chart
description: Org structure generation with areas, committees, and operating rhythms.
allowed-tools: [Read, Write, Glob]
param_set: standard
---
You are running `/org-chart {topic}`.

ROLES — READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role in the format `- [role name] — [one-line description from role file]`.
DO NOT invent role names unless no roles files are found.
If no files are found, DO produce a `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` block instead, with one inferred entry per role in the format `- [role name] — [description]`.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER — THREE-TIER CLASSIFICATION SEQUENCE CONSTRAINT

DO classify roles in this strict three-tier order: `Engineering` types first, then `Operations` types, then `PM`, `Design`, `Research`, and `Other` types.
If no `Engineering` roles are present, begin with `Operations` types.
If neither `Engineering` nor `Operations` roles are present, classify all roles in any order.
DO NOT interleave tiers — complete all entries in one tier before writing any entry from the next tier.

ROLE-TYPE-CLASSIFICATION — REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE, following the ROLE-LOAD-ORDER three-tier constraint above.
DO assign each role exactly one domain type from this closed set: `Engineering / PM / Design / Operations / Research / Other`.
DO format each entry as `- [role name] — [domain type]`.
DO NOT skip this block.
DO NOT proceed until every role from ROLES-LOADED or ROLES-NOTE is classified.
DO annotate each Key Roles cell in the Headcount by Area table in the format `[role name] ([domain type])`.
DO annotate each Membership field in Committee Charters in the same format `[role name] ([domain type])`.

When all roles are classified, DO emit: `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`; DO NOT proceed to the Inertia Assessment until this gate line is present in the output.

INERTIA ASSESSMENT — FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.
DO NOT write an org diagram as the first section.
DO structure the inertia assessment in this exact four-sub-section order: Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

Sub-section 1 — Case for Staying Flat

DO produce a three-column mechanism evidence table with columns `Mechanism Name | Type | Frequency / Participants`.
DO include at minimum two data rows.
The Type column MUST contain only values from this closed vocabulary: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
DO NOT use Type values outside this vocabulary.
Each Mechanism Name MUST name a specific, observable coordination mechanism.
DO NOT move mechanism-typed table content into Sub-section 2.

After writing the table, DO count the data rows (header row excluded).
IF count < 2: DO write the missing mechanism row(s) until count reaches 2.
THEN substitute the final row count as N and DO emit exactly: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
DO NOT emit this separator before count >= 2.
DO NOT begin Sub-section 2 before this separator is present in the output.

Sub-section 2 — How We Coordinate Today

DO inventory the coordination patterns currently in active use.
DO name channels, cadences, informal roles, and artifacts with frequency and participants.
DO NOT re-list entries from the Sub-section 1 table.

Sub-section 3 — Rebuttal

DO name the coordination failure the flat-team case and current mechanisms cannot answer.
DO reference a specific observable: a blocked decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap.
DO NOT write "the team is growing" without specifying the failure mode.

Sub-section 4 — VERDICT and Re-assessment Trigger

MUST open this sub-section with a pressure rating line in this format: `FLAT-CASE-PRESSURE: [rating] — [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`.
The rating MUST be exactly one value from this closed set: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
DO NOT omit this line.
DO NOT emit the verdict declaration before this line is present.
After emitting the pressure line, DO choose exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
The reasoning sentence MUST reference the FLAT-CASE-PRESSURE rating by name.
DO write a re-assessment trigger immediately after the verdict naming a concrete threshold.
DO NOT write "revisit as the team grows."
DO NOT proceed past the VERDICT until the pressure line, verdict declaration, and re-assessment trigger are all written.

When VERDICT is written, DO emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`; DO NOT draw any org boxes until this gate line is present in the output.

ASCII ORG DIAGRAM

DO draw an ASCII hierarchy after the inertia assessment phase gate.
DO show at minimum two levels.
DO NOT produce a flat list of names without hierarchy.
DO show committees as distinct labeled nodes, not embedded in one area.
DO use role names from ROLES-LOADED or ROLES-NOTE — DO NOT introduce new role names.

When the org diagram is complete, DO emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`; DO NOT begin the Headcount table until this gate line is present in the output.

HEADCOUNT BY AREA — DECIDES / ESCALATES REQUIRED

DO produce a headcount table with columns `Area | Headcount | Key Roles | Decides | Escalates`.
DO NOT use a single `Decision Scope` column — the Decides and Escalates columns are separate and both REQUIRED.
DO NOT write `owns the area` or generic ownership phrases in either column.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward, naming the destination role or forum.
DO annotate each Key Roles entry in the format `[role name] ([domain type])` from ROLE-TYPE-CLASSIFICATION.
DO include at minimum two area rows with individual counts plus a `**Total**` row with the sum.
DO NOT produce only a single total with no area breakdown.

OPERATING RHYTHM TABLE

DO produce a cadence table after the headcount section with columns `Cadence | Frequency | DRI / Owner | Purpose`.
DO include at minimum three distinct rows: ROB, a shiproom or gate, and a governance meeting.
DO NOT combine two meetings into one row.
DO NOT produce a rhythm table with only ROB.
DO reference a role from ROLES-LOADED in the `DRI / Owner` column where possible.

COMMITTEE CHARTERS — FIVE FIELDS REQUIRED

DO write a charter for each governance meeting in the rhythm table.
DO include all five fields: `Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`.
DO NOT label this section optional.
DO NOT write a rhythm table row for a committee and then omit its charter.
DO annotate each Membership role in the format `[role name] ([domain type])` from ROLE-TYPE-CLASSIFICATION, listing at minimum two roles.
DO populate the Escalates field with a named destination.
DO NOT write `everything not listed under Decides.`
DO populate the Quorum field using this format: `Quorum: [N] of [M] member roles required for binding decisions`, where N is the minimum required count and M is the total number of roles listed in the Membership field.
DO NOT use the short `Quorum: [N roles required for binding decisions]` form — the full fraction format is required.
DO NOT omit the Quorum field from any charter.

When all charters are written, DO emit: `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`; DO NOT begin the ORG-ELEMENT REGISTER until this gate line is present in the output.

ORG-ELEMENT REGISTER — REQUIRED BEFORE ORG EVOLUTION ROADMAP

MUST produce an `ORG-ELEMENT REGISTER` block immediately after the charters phase gate.
DO NOT skip it.
DO NOT proceed to Org Evolution Roadmap until all four category entries are populated:
  `cat-1 (Areas)` — all area names from the Headcount table, each in the format `- [area name] — headcount: [N]`
  `cat-2 (Committees/Cadences)` — all committee and cadence names from the Rhythm Table and Charters, each as `- [name]`
  `cat-3 (Headcount)` — total headcount in the format `- Total headcount: [N]`
  `cat-4 (DRI Roles)` — all DRI role names from the Operating Rhythm Table, each as `- [DRI role]`

ORG EVOLUTION ROADMAP — REQUIRED

DO produce a trigger table after the ORG-ELEMENT REGISTER with columns `Trigger | Structural Change | Type`.
DO NOT label it optional.
DO include at minimum two rows.
Row 1: a headcount threshold trigger.
Row 2: MUST come from a different category — a workload signal, structural symptom, or milestone event.
DO NOT use two headcount thresholds as the two rows.

ANTI-PATTERN WATCH — TYPED CITATIONS REQUIRED

DO produce this section after the Org Evolution Roadmap with columns `Anti-Pattern | Why It Applies Here | Mitigation`.
MUST open each `Why It Applies Here` cell with typed citation syntax in the format `[element name] (cat-N) — [one sentence of specific relevance]`.
DO NOT write a cell that names an element without the `(cat-N)` typed syntax.
DO NOT use a `cat-N` code that does not match the category schema in the ORG-ELEMENT REGISTER.
DO include at minimum two anti-pattern rows.

SECTION ORDER

DO produce sections in this exact sequence:
1. ROLES-LOADED or ROLES-NOTE
2. ROLE-LOAD-ORDER three-tier constraint applied (Engineering / Operations / remaining types)
3. ROLE-TYPE-CLASSIFICATION
4. `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`
5. Inertia Assessment (Case for Staying Flat [row-count separator] / How We Coordinate Today / Rebuttal / VERDICT [opens with FLAT-CASE-PRESSURE line])
6. `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`
7. ASCII Org Diagram
8. `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`
9. Headcount by Area
10. Operating Rhythm Table
11. Committee Charters (Purpose / Membership / Decides / Escalates / Quorum [N of M fraction] per charter)
12. `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`
13. ORG-ELEMENT REGISTER
14. Org Evolution Roadmap
15. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} — {date}`