---
skill: quest-variate
skill_target: org-chart
date: 2026-03-16
round: R18
rubric_version: v16
status: variate
---

# org-chart Variate -- Round 18 (Rubric v16)

**Date:** 2026-03-16
**Skill:** org-chart
**Rubric:** v16 (criteria C-01 through A-42)
**Round:** R18 overall / Round 1 of the v16 rubric cycle

## R17 ceiling and R18 target

R17-V-05 achieves maximum composite score against rubric v15. Against rubric v16 (which added
A-40/A-41/A-42), three precision gaps remain in the V-05 baseline:

1. **TRIGGER-TYPE-ACCOUNTING terminology gap (A-40):** V-05 instructs `TYPE-USED` / `TYPE-UNUSED`
   per row, but rubric A-40 specifies `TYPE-REPRESENTED (count >= 1) or TYPE-ABSENT (count = 0)`.
   V-05 also omits the per-type signal count that A-40 requires ("the count of roadmap tier signals
   assigned that type"). The implementation passes presence but fails row-format precision: count
   absent, verdict labels misaligned with A-40 pass condition.

2. **REGISTER-ROADMAP-CORRESPONDENCE scope gap (A-41):** V-05 checks only cat-1 (Areas) against
   roadmap rows (ROADMAP-COVERED / ROADMAP-UNCOVERED). Rubric A-41 requires all four register
   categories mapped to roadmap tier Observable Signals with bidirectional flagging: coverage gaps
   (register category with no tier signal) AND unanchored triggers (roadmap tier with no register
   category). V-05 satisfies the spirit but not the letter of the A-41 pass condition.

3. **ROADMAP-TYPE-VOCABULARY omission gap (A-42):** V-05 claims to integrate A-40+A-41+A-42 but
   its prompt body and section order omit the ROADMAP-TYPE-VOCABULARY block. R17-V-03 introduced
   this block correctly; V-05's full integration did not carry it forward. A-42 requires the block
   immediately before the Org Evolution Roadmap table.

**R18 target:** Close all three precision gaps. V-01/V-02/V-03 are single-axis. V-04 combines
V-01+V-02. V-05 integrates all three on the R17-V-05 baseline.

---

## Variation Map

| V    | Axis                                                                      | Hypothesis                                                                                                                                                                                                                                                                                 |
|------|---------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| V-01 | TRIGGER-TYPE-ACCOUNTING spec alignment (A-40 terminology + count)         | Replacing TYPE-USED/TYPE-UNUSED with TYPE-REPRESENTED/TYPE-ABSENT and adding explicit signal count makes each row parallel to REGISTER-POPULATION-AUDIT and ROLE-TIER-ACCOUNTING -- count plus verdict, verifiable against A-40 pass condition without terminology mapping                 |
| V-02 | REGISTER-ROADMAP-CORRESPONDENCE full A-41 spec (all 4 cats + bidirectional) | Extending from cat-1-only to all four register categories with bidirectional gap flags (COVERAGE-GAP + UNANCHORED-TRIGGER) precisely implements A-41's pass condition; the full table is the register-roadmap parallel to CHARTER-RHYTHM-PARITY                                           |
| V-03 | ROADMAP-TYPE-VOCABULARY integration + VOCABULARY-DISAMBIGUATION (A-42 gap closure) | Restoring ROADMAP-TYPE-VOCABULARY before the Org Evolution Roadmap closes the A-42 gap absent from V-05; adding a VOCABULARY-DISAMBIGUATION note prevents conflation of the roadmap Type column vocabulary (A-42) with the ROADMAP-TRIGGER-DIVERSITY trigger type vocabulary (A-39) |
| V-04 | A-40 spec alignment + full A-41 spec combined (V-01 + V-02)              | The terminology fix and scope expansion compose without interference; tests whether the two precision improvements together close A-40+A-41 without introducing A-42                                                                                                                         |
| V-05 | Full integration: V-01 + V-02 + V-03 on R17-V-05 baseline               | All three precision gaps closed simultaneously; five-layer roadmap verification chain: declare type vocabulary -> write roadmap -> verify trigger diversity -> account types per-represented/absent -> verify register-roadmap alignment bidirectionally                                     |

---

## V-01: TRIGGER-TYPE-ACCOUNTING Spec Alignment (A-40 only)

**Axis:** Replace TYPE-USED/TYPE-UNUSED with TYPE-REPRESENTED/TYPE-ABSENT + signal count per row
**Hypothesis:** A row format of `[Type] -- [N signals] -- TYPE-REPRESENTED` (count >= 1) or
`TYPE-ABSENT` (count = 0) is the direct parallel to REGISTER-POPULATION-AUDIT (`[cat] -- [N
entries] -- CATEGORY-POPULATED/CATEGORY-EMPTY`) and ROLE-TIER-ACCOUNTING (`[Tier] -- [N roles]
-- TIER-PRESENT/TIER-ABSENT`); the three-element row (name, count, verdict) is the canonical
accounting pattern and makes A-40 output verifiable against the rubric pass condition by count
comparison rather than terminology mapping

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role in the format `- [role name] -- [one-line description from role file]`.
DO NOT invent role names unless no roles files are found.
If no files are found, DO produce a `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` block instead, with one inferred entry per role in the format `- [role name] -- [description]`.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER:

Canonical three-tier classification sequence declared as a standalone named block:
1. Engineering types first
2. Operations types second
3. PM, Design, Research, and Other types last

If no Engineering roles are present, begin with Operations types.
If neither Engineering nor Operations roles are present, classify all roles in any order.
DO NOT interleave tiers -- complete all entries in one tier before writing any entry from the next tier.
This block is the independently verifiable ordering declaration for ROLE-TYPE-CLASSIFICATION.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE, following the ROLE-LOAD-ORDER three-tier constraint above.
DO assign each role exactly one domain type from this closed set: `Engineering / PM / Design / Operations / Research / Other`.
DO format each entry as `- [role name] -- [domain type]`.
DO NOT skip this block.
DO NOT proceed until every role from ROLES-LOADED or ROLES-NOTE is classified.
DO annotate each Key Roles cell in the Headcount by Area table in the format `[role name] ([domain type])`.
DO annotate each Membership field in Committee Charters in the same format `[role name] ([domain type])`.

ROLE-TIER-ACCOUNTING -- REQUIRED IMMEDIATELY AFTER ROLE-TYPE-CLASSIFICATION

DO emit a `ROLE-TIER-ACCOUNTING:` block immediately after ROLE-TYPE-CLASSIFICATION.
For each tier declared in the ROLE-LOAD-ORDER block (Engineering / Operations / remaining types), emit one row:
- Populated tier: `[Tier] -- [N roles] -- TIER-PRESENT`
- Empty tier: `[Tier] -- 0 roles -- TIER-ABSENT`
DO NOT skip any declared tier. A TIER-ABSENT row makes the population gap a directly scannable row.

When all roles are classified and tier accounting is complete, DO emit:
`=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
DO NOT proceed to the Inertia Assessment until this gate line is present in the output.

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.
DO NOT write an org diagram as the first section.
DO structure the inertia assessment in this exact four-sub-section order: Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

Sub-section 1 -- Case for Staying Flat

DO produce a three-column mechanism evidence table with columns `Mechanism Name | Type | Frequency / Participants`.
DO include at minimum two data rows.
The Type column MUST contain only values from this closed vocabulary: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
DO NOT use Type values outside this vocabulary.
Each Mechanism Name MUST name a specific, observable coordination mechanism.
DO NOT move mechanism-typed table content into Sub-section 2.

After writing the table, DO count the data rows (header row excluded).
IF count < 2: DO write the missing mechanism row(s) until count reaches 2.
THEN substitute the final row count as N and DO emit exactly:
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
DO NOT emit this separator before count >= 2.
DO NOT begin Sub-section 2 before this separator is present in the output.

Sub-section 2 -- How We Coordinate Today

DO inventory the coordination patterns currently in active use.
DO name channels, cadences, informal roles, and artifacts with frequency and participants.
DO NOT re-list entries from the Sub-section 1 table.

Sub-section 3 -- Rebuttal

DO name the coordination failure the flat-team case and current mechanisms cannot answer.
DO reference a specific observable: a blocked decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap.
DO NOT write "the team is growing" without specifying the failure mode.

Sub-section 4 -- VERDICT and Re-assessment Trigger

MUST open this sub-section with a pressure rating line in this format:
`FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
The rating MUST be exactly one value from this closed set: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
DO NOT omit this line.
DO NOT emit the verdict declaration before this line is present.
After emitting the pressure line, DO choose exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
The reasoning sentence MUST reference the FLAT-CASE-PRESSURE rating by name.
DO write a re-assessment trigger immediately after the verdict naming a concrete threshold.
DO NOT write "revisit as the team grows."
DO NOT proceed past the VERDICT until the pressure line, verdict declaration, and re-assessment trigger are all written.

When VERDICT is written, DO emit:
`=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
DO NOT draw any org boxes until this gate line is present in the output.

ASCII ORG DIAGRAM

DO draw an ASCII hierarchy after the inertia assessment phase gate.
DO show at minimum two levels.
DO NOT produce a flat list of names without hierarchy.
DO show committees as distinct labeled nodes, not embedded in one area.
DO use role names from ROLES-LOADED or ROLES-NOTE -- DO NOT introduce new role names.
DO use box-drawing characters (`+`, `-`, `|`) for the diagram, not indented lists or plain-text trees.

When the org diagram is complete, DO emit:
`=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
DO NOT begin the Headcount table until this gate line is present in the output.

HEADCOUNT BY AREA -- DECIDES / ESCALATES REQUIRED

DO produce a headcount table with columns `Area | Headcount | Key Roles | Decides | Escalates`.
DO NOT use a single `Decision Scope` column -- the Decides and Escalates columns are separate and both REQUIRED.
DO NOT write `owns the area` or generic ownership phrases in either column.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward, naming the destination role or forum.
DO annotate each Key Roles entry in the format `[role name] ([domain type])` from ROLE-TYPE-CLASSIFICATION.
DO include at minimum two area rows with individual counts plus a `**Total**` row with the sum.
DO NOT produce only a single total with no area breakdown.

OPERATING RHYTHM TABLE

DO produce a cadence table after the headcount section with columns `Cadence | Frequency | DRI / Owner | Purpose`.
DO include at minimum three distinct rows: one ROB, one shiproom or gate meeting, and one governance meeting.
DO NOT combine two meetings into one row.
DO NOT produce a rhythm table with only ROB.
DO reference a role from ROLES-LOADED in the `DRI / Owner` column where possible.

COMMITTEE CHARTERS -- SIX FIELDS REQUIRED

DO write a charter for each governance meeting in the rhythm table.
DO include all six fields: `Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`, `Dissolves When`.
DO NOT label this section optional.
DO NOT write a rhythm table row for a committee and then omit its charter.
DO annotate each Membership role in the format `[role name] ([domain type])` from ROLE-TYPE-CLASSIFICATION, listing at minimum two roles.
DO populate the Escalates field with a named destination.
DO NOT write `everything not listed under Decides.`

Before writing the Quorum line for each charter:
DO emit a `QUORUM-DENOMINATOR CONSTRAINT: M = [count of roles listed in this charter's Membership field]` line.
DO populate the Quorum field using this format: `Quorum: [N] of [M] member roles required for binding decisions`, where M MUST equal the QUORUM-DENOMINATOR CONSTRAINT value above.
DO NOT use the short `Quorum: [N roles required for binding decisions]` form -- the full N-of-M fraction is required.
DO NOT omit the Quorum field from any charter.

DO populate the `Dissolves When` field with specific, observable dissolution conditions.
DO NOT write "when no longer needed" or equivalent vague conditions.
DO NOT omit the Dissolves When field from any charter.

CHARTER-COMPLETENESS-AUDIT -- REQUIRED AFTER ALL CHARTERS

After all committee charters are written:
DO emit a `CHARTER-COMPLETENESS-AUDIT:` block as a single table with one row per charter.
Columns: `Charter | Purpose | Membership | Decides | Escalates | Quorum | Dissolves When | QUORUM-DENOMINATOR CONSTRAINT`
Each cell: `PRESENT` or `MISSING`.
Any cell marked `MISSING` blocks the CHARTERS COMPLETE gate -- write the missing field before proceeding.
DO NOT emit the CHARTERS COMPLETE gate until every cell in this audit table is `PRESENT`.

CHARTER-RHYTHM-PARITY -- REQUIRED AFTER CHARTER-COMPLETENESS-AUDIT

DO emit a `CHARTER-RHYTHM-PARITY:` block immediately after the CHARTER-COMPLETENESS-AUDIT block.
DO produce a two-column table with columns `Charter Name | Rhythm Table Governance Row`.
DO map every charter to its corresponding governance row in the Operating Rhythm Table.
DO verify bidirectional correspondence:
  - Every charter MUST name a governance row that exists in the Operating Rhythm Table.
  - Every governance row in the Operating Rhythm Table MUST have a corresponding charter.
If any charter lacks a corresponding rhythm row, emit `[charter name] | NO MATCHING RHYTHM ROW -- PARITY VIOLATION`.
If any governance rhythm row lacks a charter, emit `MISSING CHARTER FOR: [rhythm row name] -- PARITY VIOLATION`.
DO NOT emit the CHARTERS COMPLETE gate if any PARITY VIOLATION row is present.
Only emit the gate after this block confirms full bidirectional correspondence.

When the CHARTER-COMPLETENESS-AUDIT and CHARTER-RHYTHM-PARITY blocks both confirm full coverage:
DO emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
DO NOT begin the ORG-ELEMENT REGISTER until this gate line is present in the output.

ORG-ELEMENT REGISTER -- REQUIRED BEFORE ORG EVOLUTION ROADMAP

Before writing the register body, DO emit a `REGISTER-CATEGORY-CONTRACT:` block enumerating each valid category label as a separate line item:
- cat-1 (Areas)
- cat-2 (Committees/Cadences)
- cat-3 (Headcount)
- cat-4 (DRI Roles)
Any category label used in the register body that is not listed in this block is a constraint violation.

MUST produce an `ORG-ELEMENT REGISTER` block immediately after the REGISTER-CATEGORY-CONTRACT block.
DO NOT skip it.
DO NOT proceed to REGISTER-POPULATION-AUDIT until all four category entries are populated:
  `cat-1 (Areas)` -- all area names from the Headcount table, each as `- [area name] -- headcount: [N]`
  `cat-2 (Committees/Cadences)` -- all committee and cadence names from the Rhythm Table and Charters, each as `- [name]`
  `cat-3 (Headcount)` -- total headcount as `- Total headcount: [N]`
  `cat-4 (DRI Roles)` -- all DRI role names from the Operating Rhythm Table, each as `- [DRI role]`

REGISTER-POPULATION-AUDIT -- REQUIRED IMMEDIATELY AFTER ORG-ELEMENT REGISTER

DO emit a `REGISTER-POPULATION-AUDIT:` block immediately after the ORG-ELEMENT REGISTER body.
For each category declared in the REGISTER-CATEGORY-CONTRACT block, emit one row:
  - Populated category: `[category label] -- [N entries] -- CATEGORY-POPULATED`
  - Empty category: `[category label] -- 0 entries -- CATEGORY-EMPTY`
DO NOT skip any category declared in the REGISTER-CATEGORY-CONTRACT block.
A CATEGORY-EMPTY row is a constraint violation -- add the missing entries to the register before proceeding.
DO NOT proceed to the Org Evolution Roadmap until all declared categories have a CATEGORY-POPULATED verdict.

ORG EVOLUTION ROADMAP -- REQUIRED

DO produce a trigger table after the REGISTER-POPULATION-AUDIT block with columns `Trigger | Structural Change | Type | Observable Signal | Probability Weight`.
DO NOT label it optional.
DO include at minimum two rows:
  Row 1: a headcount threshold trigger.
  Row 2: MUST come from a different category -- a workload signal, structural symptom, or milestone event.
DO NOT use two headcount thresholds as the two rows.
DO include a `WATCH-FIRST:` declaration naming the leading indicator to monitor before acting.

ROADMAP-TRIGGER-DIVERSITY -- REQUIRED AFTER ORG EVOLUTION ROADMAP

DO emit a `ROADMAP-TRIGGER-DIVERSITY:` block immediately after the Org Evolution Roadmap table.
For each tier row in the roadmap, enumerate its Observable Signal with a declared trigger type from this closed set: `Capacity / Process / Strategic / Structural`.
DO format each entry as: `[Tier/Row label] -- [Observable Signal text] -- [Trigger Type]`
DO count the number of distinct trigger types present across all rows.
DO emit: `Trigger type diversity: [N] distinct types ([comma-separated list of types used])`
MINIMUM TWO DISTINCT TRIGGER TYPES are required across all roadmap tier signals.
If fewer than two distinct trigger types are present, this is a constraint violation -- revise the roadmap Observable Signal column before proceeding.
DO NOT proceed to TRIGGER-TYPE-ACCOUNTING until this block is present and the diversity count is >= 2.

TRIGGER-TYPE-ACCOUNTING -- REQUIRED IMMEDIATELY AFTER ROADMAP-TRIGGER-DIVERSITY

DO emit a `TRIGGER-TYPE-ACCOUNTING:` block immediately after the ROADMAP-TRIGGER-DIVERSITY block.
For each trigger type in the ROADMAP-TRIGGER-DIVERSITY closed set (Capacity / Process / Strategic / Structural), emit one row using this three-element format:
  - Type with >= 1 tier signal: `[Trigger Type] -- [N signals] -- TYPE-REPRESENTED`
  - Type with 0 tier signals: `[Trigger Type] -- 0 signals -- TYPE-ABSENT`
DO NOT use TYPE-USED or TYPE-UNUSED -- the required verdict labels are TYPE-REPRESENTED and TYPE-ABSENT.
DO NOT omit the signal count -- each row MUST state the count of roadmap tier signals assigned that type.
DO NOT skip any type from the declared closed set.
A TYPE-ABSENT row makes the absent trigger type a directly scannable row rather than an implicit absence from the diversity count.
The ROADMAP-TRIGGER-DIVERSITY >= 2 constraint remains independently enforced; TRIGGER-TYPE-ACCOUNTING is additive full-set accounting with per-type count.
DO NOT proceed to REGISTER-ROADMAP-CORRESPONDENCE until this block is complete with one row per declared trigger type.

REGISTER-ROADMAP-CORRESPONDENCE -- REQUIRED AFTER TRIGGER-TYPE-ACCOUNTING

DO emit a `REGISTER-ROADMAP-CORRESPONDENCE:` block immediately after the TRIGGER-TYPE-ACCOUNTING block.
For each cat-1 (Areas) entry in the ORG-ELEMENT REGISTER, emit one row:
  - Addressed area: `[area name] -- [roadmap row label or structural change referencing this area] -- ROADMAP-COVERED`
  - Unaddressed area: `[area name] -- ROADMAP-UNCOVERED`
DO NOT skip any cat-1 area from the ORG-ELEMENT REGISTER.
A ROADMAP-UNCOVERED row is a constraint violation -- add a roadmap row whose Structural Change addresses the uncovered area before proceeding.
DO NOT proceed to Anti-Pattern Watch until every cat-1 area has a ROADMAP-COVERED verdict.

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

DO produce this section after the REGISTER-ROADMAP-CORRESPONDENCE block with columns `Anti-Pattern | Why It Applies Here | Mitigation`.
MUST open each `Why It Applies Here` cell with typed citation syntax: `[element name] (cat-N) -- [one sentence of specific relevance]`.
DO NOT write a cell that names an element without the `(cat-N)` typed syntax.
DO NOT use a `cat-N` code that does not match the REGISTER-CATEGORY-CONTRACT schema.
DO include at minimum two anti-pattern rows.

SECTION ORDER

DO produce sections in this exact sequence:
1. ROLES-LOADED or ROLES-NOTE
2. ROLE-LOAD-ORDER: named block
3. ROLE-TYPE-CLASSIFICATION:
4. ROLE-TIER-ACCOUNTING:
5. `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
6. Inertia Assessment (Case for Staying Flat [FLAT-CASE-CLOSED] / How We Coordinate Today / Rebuttal / VERDICT [FLAT-CASE-PRESSURE line])
7. `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
8. ASCII Org Diagram (box-drawing characters)
9. `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
10. Headcount by Area
11. Operating Rhythm Table
12. Committee Charters (QUORUM-DENOMINATOR CONSTRAINT + six fields per charter)
13. CHARTER-COMPLETENESS-AUDIT:
14. CHARTER-RHYTHM-PARITY:
15. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
16. REGISTER-CATEGORY-CONTRACT:
17. ORG-ELEMENT REGISTER
18. REGISTER-POPULATION-AUDIT:
19. Org Evolution Roadmap
20. ROADMAP-TRIGGER-DIVERSITY:
21. TRIGGER-TYPE-ACCOUNTING: (three-element rows: type -- N signals -- TYPE-REPRESENTED/TYPE-ABSENT)
22. REGISTER-ROADMAP-CORRESPONDENCE: (cat-1 areas, ROADMAP-COVERED/ROADMAP-UNCOVERED)
23. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-02: REGISTER-ROADMAP-CORRESPONDENCE Full A-41 Spec (A-41 only)

**Axis:** Extend from cat-1-only unidirectional check to all-four-categories bidirectional
correspondence table with COVERAGE-GAP and UNANCHORED-TRIGGER flagging
**Hypothesis:** A-41's pass condition requires all register categories (not just cat-1 Areas) mapped
to roadmap tier Observable Signals AND bidirectional flagging; V-05's implementation satisfies only
the cat-1 / one-direction subset; the full four-category bidirectional table is the register-roadmap
parallel to CHARTER-RHYTHM-PARITY's bidirectional charter-rhythm table, closing the same
correspondence gap A-37 closes between charter and rhythm domains

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role in the format `- [role name] -- [one-line description from role file]`.
DO NOT invent role names unless no roles files are found.
If no files are found, DO produce a `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` block instead, with one inferred entry per role in the format `- [role name] -- [description]`.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER:

Canonical three-tier classification sequence declared as a standalone named block:
1. Engineering types first
2. Operations types second
3. PM, Design, Research, and Other types last

If no Engineering roles are present, begin with Operations types.
If neither Engineering nor Operations roles are present, classify all roles in any order.
DO NOT interleave tiers -- complete all entries in one tier before writing any entry from the next tier.
This block is the independently verifiable ordering declaration for ROLE-TYPE-CLASSIFICATION.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE, following the ROLE-LOAD-ORDER three-tier constraint above.
DO assign each role exactly one domain type from this closed set: `Engineering / PM / Design / Operations / Research / Other`.
DO format each entry as `- [role name] -- [domain type]`.
DO NOT skip this block.
DO NOT proceed until every role from ROLES-LOADED or ROLES-NOTE is classified.
DO annotate each Key Roles cell in the Headcount by Area table in the format `[role name] ([domain type])`.
DO annotate each Membership field in Committee Charters in the same format `[role name] ([domain type])`.

ROLE-TIER-ACCOUNTING -- REQUIRED IMMEDIATELY AFTER ROLE-TYPE-CLASSIFICATION

DO emit a `ROLE-TIER-ACCOUNTING:` block immediately after ROLE-TYPE-CLASSIFICATION.
For each tier declared in the ROLE-LOAD-ORDER block (Engineering / Operations / remaining types), emit one row:
- Populated tier: `[Tier] -- [N roles] -- TIER-PRESENT`
- Empty tier: `[Tier] -- 0 roles -- TIER-ABSENT`
DO NOT skip any declared tier. A TIER-ABSENT row makes the population gap a directly scannable row.

When all roles are classified and tier accounting is complete, DO emit:
`=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
DO NOT proceed to the Inertia Assessment until this gate line is present in the output.

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.
DO NOT write an org diagram as the first section.
DO structure the inertia assessment in this exact four-sub-section order: Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

Sub-section 1 -- Case for Staying Flat

DO produce a three-column mechanism evidence table with columns `Mechanism Name | Type | Frequency / Participants`.
DO include at minimum two data rows.
The Type column MUST contain only values from this closed vocabulary: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
DO NOT use Type values outside this vocabulary.
Each Mechanism Name MUST name a specific, observable coordination mechanism.
DO NOT move mechanism-typed table content into Sub-section 2.

After writing the table, DO count the data rows (header row excluded).
IF count < 2: DO write the missing mechanism row(s) until count reaches 2.
THEN substitute the final row count as N and DO emit exactly:
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
DO NOT emit this separator before count >= 2.
DO NOT begin Sub-section 2 before this separator is present in the output.

Sub-section 2 -- How We Coordinate Today

DO inventory the coordination patterns currently in active use.
DO name channels, cadences, informal roles, and artifacts with frequency and participants.
DO NOT re-list entries from the Sub-section 1 table.

Sub-section 3 -- Rebuttal

DO name the coordination failure the flat-team case and current mechanisms cannot answer.
DO reference a specific observable: a blocked decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap.
DO NOT write "the team is growing" without specifying the failure mode.

Sub-section 4 -- VERDICT and Re-assessment Trigger

MUST open this sub-section with a pressure rating line in this format:
`FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
The rating MUST be exactly one value from this closed set: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
DO NOT omit this line.
DO NOT emit the verdict declaration before this line is present.
After emitting the pressure line, DO choose exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
The reasoning sentence MUST reference the FLAT-CASE-PRESSURE rating by name.
DO write a re-assessment trigger immediately after the verdict naming a concrete threshold.
DO NOT write "revisit as the team grows."
DO NOT proceed past the VERDICT until the pressure line, verdict declaration, and re-assessment trigger are all written.

When VERDICT is written, DO emit:
`=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
DO NOT draw any org boxes until this gate line is present in the output.

ASCII ORG DIAGRAM

DO draw an ASCII hierarchy after the inertia assessment phase gate.
DO show at minimum two levels.
DO NOT produce a flat list of names without hierarchy.
DO show committees as distinct labeled nodes, not embedded in one area.
DO use role names from ROLES-LOADED or ROLES-NOTE -- DO NOT introduce new role names.
DO use box-drawing characters (`+`, `-`, `|`) for the diagram, not indented lists or plain-text trees.

When the org diagram is complete, DO emit:
`=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
DO NOT begin the Headcount table until this gate line is present in the output.

HEADCOUNT BY AREA -- DECIDES / ESCALATES REQUIRED

DO produce a headcount table with columns `Area | Headcount | Key Roles | Decides | Escalates`.
DO NOT use a single `Decision Scope` column -- the Decides and Escalates columns are separate and both REQUIRED.
DO NOT write `owns the area` or generic ownership phrases in either column.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward, naming the destination role or forum.
DO annotate each Key Roles entry in the format `[role name] ([domain type])` from ROLE-TYPE-CLASSIFICATION.
DO include at minimum two area rows with individual counts plus a `**Total**` row with the sum.
DO NOT produce only a single total with no area breakdown.

OPERATING RHYTHM TABLE

DO produce a cadence table after the headcount section with columns `Cadence | Frequency | DRI / Owner | Purpose`.
DO include at minimum three distinct rows: one ROB, one shiproom or gate meeting, and one governance meeting.
DO NOT combine two meetings into one row.
DO NOT produce a rhythm table with only ROB.
DO reference a role from ROLES-LOADED in the `DRI / Owner` column where possible.

COMMITTEE CHARTERS -- SIX FIELDS REQUIRED

DO write a charter for each governance meeting in the rhythm table.
DO include all six fields: `Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`, `Dissolves When`.
DO NOT label this section optional.
DO NOT write a rhythm table row for a committee and then omit its charter.
DO annotate each Membership role in the format `[role name] ([domain type])` from ROLE-TYPE-CLASSIFICATION, listing at minimum two roles.
DO populate the Escalates field with a named destination.
DO NOT write `everything not listed under Decides.`

Before writing the Quorum line for each charter:
DO emit a `QUORUM-DENOMINATOR CONSTRAINT: M = [count of roles listed in this charter's Membership field]` line.
DO populate the Quorum field using this format: `Quorum: [N] of [M] member roles required for binding decisions`, where M MUST equal the QUORUM-DENOMINATOR CONSTRAINT value above.
DO NOT use the short `Quorum: [N roles required for binding decisions]` form -- the full N-of-M fraction is required.
DO NOT omit the Quorum field from any charter.

DO populate the `Dissolves When` field with specific, observable dissolution conditions.
DO NOT write "when no longer needed" or equivalent vague conditions.
DO NOT omit the Dissolves When field from any charter.

CHARTER-COMPLETENESS-AUDIT -- REQUIRED AFTER ALL CHARTERS

After all committee charters are written:
DO emit a `CHARTER-COMPLETENESS-AUDIT:` block as a single table with one row per charter.
Columns: `Charter | Purpose | Membership | Decides | Escalates | Quorum | Dissolves When | QUORUM-DENOMINATOR CONSTRAINT`
Each cell: `PRESENT` or `MISSING`.
Any cell marked `MISSING` blocks the CHARTERS COMPLETE gate -- write the missing field before proceeding.
DO NOT emit the CHARTERS COMPLETE gate until every cell in this audit table is `PRESENT`.

CHARTER-RHYTHM-PARITY -- REQUIRED AFTER CHARTER-COMPLETENESS-AUDIT

DO emit a `CHARTER-RHYTHM-PARITY:` block immediately after the CHARTER-COMPLETENESS-AUDIT block.
DO produce a two-column table with columns `Charter Name | Rhythm Table Governance Row`.
DO map every charter to its corresponding governance row in the Operating Rhythm Table.
DO verify bidirectional correspondence:
  - Every charter MUST name a governance row that exists in the Operating Rhythm Table.
  - Every governance row in the Operating Rhythm Table MUST have a corresponding charter.
If any charter lacks a corresponding rhythm row, emit `[charter name] | NO MATCHING RHYTHM ROW -- PARITY VIOLATION`.
If any governance rhythm row lacks a charter, emit `MISSING CHARTER FOR: [rhythm row name] -- PARITY VIOLATION`.
DO NOT emit the CHARTERS COMPLETE gate if any PARITY VIOLATION row is present.
Only emit the gate after this block confirms full bidirectional correspondence.

When the CHARTER-COMPLETENESS-AUDIT and CHARTER-RHYTHM-PARITY blocks both confirm full coverage:
DO emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
DO NOT begin the ORG-ELEMENT REGISTER until this gate line is present in the output.

ORG-ELEMENT REGISTER -- REQUIRED BEFORE ORG EVOLUTION ROADMAP

Before writing the register body, DO emit a `REGISTER-CATEGORY-CONTRACT:` block enumerating each valid category label as a separate line item:
- cat-1 (Areas)
- cat-2 (Committees/Cadences)
- cat-3 (Headcount)
- cat-4 (DRI Roles)
Any category label used in the register body that is not listed in this block is a constraint violation.

MUST produce an `ORG-ELEMENT REGISTER` block immediately after the REGISTER-CATEGORY-CONTRACT block.
DO NOT skip it.
DO NOT proceed to REGISTER-POPULATION-AUDIT until all four category entries are populated:
  `cat-1 (Areas)` -- all area names from the Headcount table, each as `- [area name] -- headcount: [N]`
  `cat-2 (Committees/Cadences)` -- all committee and cadence names from the Rhythm Table and Charters, each as `- [name]`
  `cat-3 (Headcount)` -- total headcount as `- Total headcount: [N]`
  `cat-4 (DRI Roles)` -- all DRI role names from the Operating Rhythm Table, each as `- [DRI role]`

REGISTER-POPULATION-AUDIT -- REQUIRED IMMEDIATELY AFTER ORG-ELEMENT REGISTER

DO emit a `REGISTER-POPULATION-AUDIT:` block immediately after the ORG-ELEMENT REGISTER body.
For each category declared in the REGISTER-CATEGORY-CONTRACT block, emit one row:
  - Populated category: `[category label] -- [N entries] -- CATEGORY-POPULATED`
  - Empty category: `[category label] -- 0 entries -- CATEGORY-EMPTY`
DO NOT skip any category declared in the REGISTER-CATEGORY-CONTRACT block.
A CATEGORY-EMPTY row is a constraint violation -- add the missing entries to the register before proceeding.
DO NOT proceed to the Org Evolution Roadmap until all declared categories have a CATEGORY-POPULATED verdict.

ORG EVOLUTION ROADMAP -- REQUIRED

DO produce a trigger table after the REGISTER-POPULATION-AUDIT block with columns `Trigger | Structural Change | Type | Observable Signal | Probability Weight`.
DO NOT label it optional.
DO include at minimum two rows:
  Row 1: a headcount threshold trigger.
  Row 2: MUST come from a different category -- a workload signal, structural symptom, or milestone event.
DO NOT use two headcount thresholds as the two rows.
DO include a `WATCH-FIRST:` declaration naming the leading indicator to monitor before acting.

ROADMAP-TRIGGER-DIVERSITY -- REQUIRED AFTER ORG EVOLUTION ROADMAP

DO emit a `ROADMAP-TRIGGER-DIVERSITY:` block immediately after the Org Evolution Roadmap table.
For each tier row in the roadmap, enumerate its Observable Signal with a declared trigger type from this closed set: `Capacity / Process / Strategic / Structural`.
DO format each entry as: `[Tier/Row label] -- [Observable Signal text] -- [Trigger Type]`
DO count the number of distinct trigger types present across all rows.
DO emit: `Trigger type diversity: [N] distinct types ([comma-separated list of types used])`
MINIMUM TWO DISTINCT TRIGGER TYPES are required across all roadmap tier signals.
If fewer than two distinct trigger types are present, this is a constraint violation -- revise the roadmap Observable Signal column before proceeding.
DO NOT proceed to TRIGGER-TYPE-ACCOUNTING until this block is present and the diversity count is >= 2.

TRIGGER-TYPE-ACCOUNTING -- REQUIRED IMMEDIATELY AFTER ROADMAP-TRIGGER-DIVERSITY

DO emit a `TRIGGER-TYPE-ACCOUNTING:` block immediately after the ROADMAP-TRIGGER-DIVERSITY block.
For each trigger type in the ROADMAP-TRIGGER-DIVERSITY closed set (Capacity / Process / Strategic / Structural), emit one row:
  - Used type: `[Trigger Type] -- TYPE-USED`
  - Unused type: `[Trigger Type] -- TYPE-UNUSED`
DO NOT skip any type from the declared closed set.
A TYPE-UNUSED row makes the absent trigger type a directly scannable row rather than an implicit absence from the diversity count.
The ROADMAP-TRIGGER-DIVERSITY >= 2 constraint remains independently enforced; TRIGGER-TYPE-ACCOUNTING is additive full-set accounting.
DO NOT proceed to REGISTER-ROADMAP-CORRESPONDENCE until this block is complete with one row per declared trigger type.

REGISTER-ROADMAP-CORRESPONDENCE -- REQUIRED AFTER TRIGGER-TYPE-ACCOUNTING

DO emit a `REGISTER-ROADMAP-CORRESPONDENCE:` block immediately after the TRIGGER-TYPE-ACCOUNTING block.
This block closes the cross-domain alignment gap: each register category must correspond to a roadmap tier Observable Signal, and each roadmap tier must be anchored to a register category.

DO produce a three-column correspondence table with columns `Register Category | Corresponding Roadmap Tier | Observable Signal Link`.
For each category declared in the REGISTER-CATEGORY-CONTRACT block (cat-1 through cat-4), emit one row:
  - Category with a corresponding roadmap tier: `[category label] -- [roadmap tier / row label] -- [Observable Signal activated by changes in this category's population or composition]`
  - Category with no corresponding roadmap tier: `[category label] -- COVERAGE-GAP -- no roadmap tier signal linked to this register category`
DO NOT skip any register category declared in the REGISTER-CATEGORY-CONTRACT block.
A COVERAGE-GAP row is a constraint violation -- add a roadmap row whose Observable Signal links to the uncovered register category before proceeding.

After completing the register-to-roadmap direction, verify the reverse direction:
For each roadmap tier present in the Org Evolution Roadmap table that does NOT already appear in a row above:
  emit `UNANCHORED-TRIGGER: [roadmap tier / row label] -- no register category linked to this tier's Observable Signal`
An UNANCHORED-TRIGGER row is a constraint violation -- link the tier's Observable Signal to the most relevant register category before proceeding.

DO NOT proceed to Anti-Pattern Watch until all COVERAGE-GAP and UNANCHORED-TRIGGER violations are resolved.

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

DO produce this section after the REGISTER-ROADMAP-CORRESPONDENCE block with columns `Anti-Pattern | Why It Applies Here | Mitigation`.
MUST open each `Why It Applies Here` cell with typed citation syntax: `[element name] (cat-N) -- [one sentence of specific relevance]`.
DO NOT write a cell that names an element without the `(cat-N)` typed syntax.
DO NOT use a `cat-N` code that does not match the REGISTER-CATEGORY-CONTRACT schema.
DO include at minimum two anti-pattern rows.

SECTION ORDER

DO produce sections in this exact sequence:
1. ROLES-LOADED or ROLES-NOTE
2. ROLE-LOAD-ORDER: named block
3. ROLE-TYPE-CLASSIFICATION:
4. ROLE-TIER-ACCOUNTING:
5. `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
6. Inertia Assessment (Case for Staying Flat [FLAT-CASE-CLOSED] / How We Coordinate Today / Rebuttal / VERDICT [FLAT-CASE-PRESSURE line])
7. `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
8. ASCII Org Diagram (box-drawing characters)
9. `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
10. Headcount by Area
11. Operating Rhythm Table
12. Committee Charters (QUORUM-DENOMINATOR CONSTRAINT + six fields per charter)
13. CHARTER-COMPLETENESS-AUDIT:
14. CHARTER-RHYTHM-PARITY:
15. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
16. REGISTER-CATEGORY-CONTRACT:
17. ORG-ELEMENT REGISTER
18. REGISTER-POPULATION-AUDIT:
19. Org Evolution Roadmap
20. ROADMAP-TRIGGER-DIVERSITY:
21. TRIGGER-TYPE-ACCOUNTING: (TYPE-USED/TYPE-UNUSED per type)
22. REGISTER-ROADMAP-CORRESPONDENCE: (all 4 categories + bidirectional COVERAGE-GAP / UNANCHORED-TRIGGER)
23. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-03: ROADMAP-TYPE-VOCABULARY Integration + Disambiguation Note (A-42 only)

**Axis:** Restore the ROADMAP-TYPE-VOCABULARY block (absent from R17-V-05) before the Org
Evolution Roadmap, and add a VOCABULARY-DISAMBIGUATION note separating it from the
ROADMAP-TRIGGER-DIVERSITY closed set
**Hypothesis:** V-05 omits ROADMAP-TYPE-VOCABULARY despite claiming A-42 integration; the block
governs the roadmap Type column (nature of structural change), distinct from ROADMAP-TRIGGER-DIVERSITY
trigger types (nature of observable signal); the disambiguation note prevents vocabulary conflation --
without it, generators populate the roadmap Type column with trigger type labels (Capacity/Strategic)
rather than structural change labels (Structural/Process/Personnel/Governance)

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role in the format `- [role name] -- [one-line description from role file]`.
DO NOT invent role names unless no roles files are found.
If no files are found, DO produce a `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` block instead, with one inferred entry per role in the format `- [role name] -- [description]`.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER:

Canonical three-tier classification sequence declared as a standalone named block:
1. Engineering types first
2. Operations types second
3. PM, Design, Research, and Other types last

If no Engineering roles are present, begin with Operations types.
If neither Engineering nor Operations roles are present, classify all roles in any order.
DO NOT interleave tiers -- complete all entries in one tier before writing any entry from the next tier.
This block is the independently verifiable ordering declaration for ROLE-TYPE-CLASSIFICATION.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE, following the ROLE-LOAD-ORDER three-tier constraint above.
DO assign each role exactly one domain type from this closed set: `Engineering / PM / Design / Operations / Research / Other`.
DO format each entry as `- [role name] -- [domain type]`.
DO NOT skip this block.
DO NOT proceed until every role from ROLES-LOADED or ROLES-NOTE is classified.
DO annotate each Key Roles cell in the Headcount by Area table in the format `[role name] ([domain type])`.
DO annotate each Membership field in Committee Charters in the same format `[role name] ([domain type])`.

ROLE-TIER-ACCOUNTING -- REQUIRED IMMEDIATELY AFTER ROLE-TYPE-CLASSIFICATION

DO emit a `ROLE-TIER-ACCOUNTING:` block immediately after ROLE-TYPE-CLASSIFICATION.
For each tier declared in the ROLE-LOAD-ORDER block (Engineering / Operations / remaining types), emit one row:
- Populated tier: `[Tier] -- [N roles] -- TIER-PRESENT`
- Empty tier: `[Tier] -- 0 roles -- TIER-ABSENT`
DO NOT skip any declared tier. A TIER-ABSENT row makes the population gap a directly scannable row.

When all roles are classified and tier accounting is complete, DO emit:
`=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
DO NOT proceed to the Inertia Assessment until this gate line is present in the output.

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.
DO NOT write an org diagram as the first section.
DO structure the inertia assessment in this exact four-sub-section order: Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

Sub-section 1 -- Case for Staying Flat

DO produce a three-column mechanism evidence table with columns `Mechanism Name | Type | Frequency / Participants`.
DO include at minimum two data rows.
The Type column MUST contain only values from this closed vocabulary: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
DO NOT use Type values outside this vocabulary.
Each Mechanism Name MUST name a specific, observable coordination mechanism.
DO NOT move mechanism-typed table content into Sub-section 2.

After writing the table, DO count the data rows (header row excluded).
IF count < 2: DO write the missing mechanism row(s) until count reaches 2.
THEN substitute the final row count as N and DO emit exactly:
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
DO NOT emit this separator before count >= 2.
DO NOT begin Sub-section 2 before this separator is present in the output.

Sub-section 2 -- How We Coordinate Today

DO inventory the coordination patterns currently in active use.
DO name channels, cadences, informal roles, and artifacts with frequency and participants.
DO NOT re-list entries from the Sub-section 1 table.

Sub-section 3 -- Rebuttal

DO name the coordination failure the flat-team case and current mechanisms cannot answer.
DO reference a specific observable: a blocked decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap.
DO NOT write "the team is growing" without specifying the failure mode.

Sub-section 4 -- VERDICT and Re-assessment Trigger

MUST open this sub-section with a pressure rating line in this format:
`FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
The rating MUST be exactly one value from this closed set: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
DO NOT omit this line.
DO NOT emit the verdict declaration before this line is present.
After emitting the pressure line, DO choose exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
The reasoning sentence MUST reference the FLAT-CASE-PRESSURE rating by name.
DO write a re-assessment trigger immediately after the verdict naming a concrete threshold.
DO NOT write "revisit as the team grows."
DO NOT proceed past the VERDICT until the pressure line, verdict declaration, and re-assessment trigger are all written.

When VERDICT is written, DO emit:
`=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
DO NOT draw any org boxes until this gate line is present in the output.

ASCII ORG DIAGRAM

DO draw an ASCII hierarchy after the inertia assessment phase gate.
DO show at minimum two levels.
DO NOT produce a flat list of names without hierarchy.
DO show committees as distinct labeled nodes, not embedded in one area.
DO use role names from ROLES-LOADED or ROLES-NOTE -- DO NOT introduce new role names.
DO use box-drawing characters (`+`, `-`, `|`) for the diagram, not indented lists or plain-text trees.

When the org diagram is complete, DO emit:
`=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
DO NOT begin the Headcount table until this gate line is present in the output.

HEADCOUNT BY AREA -- DECIDES / ESCALATES REQUIRED

DO produce a headcount table with columns `Area | Headcount | Key Roles | Decides | Escalates`.
DO NOT use a single `Decision Scope` column -- the Decides and Escalates columns are separate and both REQUIRED.
DO NOT write `owns the area` or generic ownership phrases in either column.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward, naming the destination role or forum.
DO annotate each Key Roles entry in the format `[role name] ([domain type])` from ROLE-TYPE-CLASSIFICATION.
DO include at minimum two area rows with individual counts plus a `**Total**` row with the sum.
DO NOT produce only a single total with no area breakdown.

OPERATING RHYTHM TABLE

DO produce a cadence table after the headcount section with columns `Cadence | Frequency | DRI / Owner | Purpose`.
DO include at minimum three distinct rows: one ROB, one shiproom or gate meeting, and one governance meeting.
DO NOT combine two meetings into one row.
DO NOT produce a rhythm table with only ROB.
DO reference a role from ROLES-LOADED in the `DRI / Owner` column where possible.

COMMITTEE CHARTERS -- SIX FIELDS REQUIRED

DO write a charter for each governance meeting in the rhythm table.
DO include all six fields: `Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`, `Dissolves When`.
DO NOT label this section optional.
DO NOT write a rhythm table row for a committee and then omit its charter.
DO annotate each Membership role in the format `[role name] ([domain type])` from ROLE-TYPE-CLASSIFICATION, listing at minimum two roles.
DO populate the Escalates field with a named destination.
DO NOT write `everything not listed under Decides.`

Before writing the Quorum line for each charter:
DO emit a `QUORUM-DENOMINATOR CONSTRAINT: M = [count of roles listed in this charter's Membership field]` line.
DO populate the Quorum field using this format: `Quorum: [N] of [M] member roles required for binding decisions`, where M MUST equal the QUORUM-DENOMINATOR CONSTRAINT value above.
DO NOT use the short `Quorum: [N roles required for binding decisions]` form -- the full N-of-M fraction is required.
DO NOT omit the Quorum field from any charter.

DO populate the `Dissolves When` field with specific, observable dissolution conditions.
DO NOT write "when no longer needed" or equivalent vague conditions.
DO NOT omit the Dissolves When field from any charter.

CHARTER-COMPLETENESS-AUDIT -- REQUIRED AFTER ALL CHARTERS

After all committee charters are written:
DO emit a `CHARTER-COMPLETENESS-AUDIT:` block as a single table with one row per charter.
Columns: `Charter | Purpose | Membership | Decides | Escalates | Quorum | Dissolves When | QUORUM-DENOMINATOR CONSTRAINT`
Each cell: `PRESENT` or `MISSING`.
Any cell marked `MISSING` blocks the CHARTERS COMPLETE gate -- write the missing field before proceeding.
DO NOT emit the CHARTERS COMPLETE gate until every cell in this audit table is `PRESENT`.

CHARTER-RHYTHM-PARITY -- REQUIRED AFTER CHARTER-COMPLETENESS-AUDIT

DO emit a `CHARTER-RHYTHM-PARITY:` block immediately after the CHARTER-COMPLETENESS-AUDIT block.
DO produce a two-column table with columns `Charter Name | Rhythm Table Governance Row`.
DO map every charter to its corresponding governance row in the Operating Rhythm Table.
DO verify bidirectional correspondence:
  - Every charter MUST name a governance row that exists in the Operating Rhythm Table.
  - Every governance row in the Operating Rhythm Table MUST have a corresponding charter.
If any charter lacks a corresponding rhythm row, emit `[charter name] | NO MATCHING RHYTHM ROW -- PARITY VIOLATION`.
If any governance rhythm row lacks a charter, emit `MISSING CHARTER FOR: [rhythm row name] -- PARITY VIOLATION`.
DO NOT emit the CHARTERS COMPLETE gate if any PARITY VIOLATION row is present.
Only emit the gate after this block confirms full bidirectional correspondence.

When the CHARTER-COMPLETENESS-AUDIT and CHARTER-RHYTHM-PARITY blocks both confirm full coverage:
DO emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
DO NOT begin the ORG-ELEMENT REGISTER until this gate line is present in the output.

ORG-ELEMENT REGISTER -- REQUIRED BEFORE ORG EVOLUTION ROADMAP

Before writing the register body, DO emit a `REGISTER-CATEGORY-CONTRACT:` block enumerating each valid category label as a separate line item:
- cat-1 (Areas)
- cat-2 (Committees/Cadences)
- cat-3 (Headcount)
- cat-4 (DRI Roles)
Any category label used in the register body that is not listed in this block is a constraint violation.

MUST produce an `ORG-ELEMENT REGISTER` block immediately after the REGISTER-CATEGORY-CONTRACT block.
DO NOT skip it.
DO NOT proceed to REGISTER-POPULATION-AUDIT until all four category entries are populated:
  `cat-1 (Areas)` -- all area names from the Headcount table, each as `- [area name] -- headcount: [N]`
  `cat-2 (Committees/Cadences)` -- all committee and cadence names from the Rhythm Table and Charters, each as `- [name]`
  `cat-3 (Headcount)` -- total headcount as `- Total headcount: [N]`
  `cat-4 (DRI Roles)` -- all DRI role names from the Operating Rhythm Table, each as `- [DRI role]`

REGISTER-POPULATION-AUDIT -- REQUIRED IMMEDIATELY AFTER ORG-ELEMENT REGISTER

DO emit a `REGISTER-POPULATION-AUDIT:` block immediately after the ORG-ELEMENT REGISTER body.
For each category declared in the REGISTER-CATEGORY-CONTRACT block, emit one row:
  - Populated category: `[category label] -- [N entries] -- CATEGORY-POPULATED`
  - Empty category: `[category label] -- 0 entries -- CATEGORY-EMPTY`
DO NOT skip any category declared in the REGISTER-CATEGORY-CONTRACT block.
A CATEGORY-EMPTY row is a constraint violation -- add the missing entries to the register before proceeding.
DO NOT proceed to ROADMAP-TYPE-VOCABULARY until all declared categories have a CATEGORY-POPULATED verdict.

ROADMAP-TYPE-VOCABULARY -- REQUIRED BEFORE ORG EVOLUTION ROADMAP

Before writing the Org Evolution Roadmap table, DO emit a `ROADMAP-TYPE-VOCABULARY:` block declaring the valid Type column values as a closed set. Each valid label is a separate line item:
- Structural
- Process
- Personnel
- Governance
Any Type value used in the roadmap table that is not listed in this block is a constraint violation.
This block governs the roadmap's Type column -- the nature of the structural change being triggered.
This block is the independently verifiable vocabulary declaration for the roadmap Type column, parallel to REGISTER-CATEGORY-CONTRACT for the register body.

VOCABULARY-DISAMBIGUATION:
The ROADMAP-TYPE-VOCABULARY closed set (Structural / Process / Personnel / Governance) classifies
the nature of the structural change a trigger produces. This is a distinct classification axis from
the ROADMAP-TRIGGER-DIVERSITY closed set (Capacity / Process / Strategic / Structural), which
classifies the nature of the observable signal that triggers the change. Both axes share the labels
"Process" and "Structural" but with different referents:
  - ROADMAP-TYPE-VOCABULARY "Process": the triggered change is a process adjustment
  - ROADMAP-TRIGGER-DIVERSITY "Process": the observable signal is a process-level event
  - ROADMAP-TYPE-VOCABULARY "Structural": the triggered change is an org structure change
  - ROADMAP-TRIGGER-DIVERSITY "Structural": the observable signal is a structural symptom
DO NOT populate the roadmap Type column with trigger type labels (Capacity / Strategic) -- those
belong only in ROADMAP-TRIGGER-DIVERSITY type assignments, never in the roadmap Type column.

ORG EVOLUTION ROADMAP -- REQUIRED

DO produce a trigger table after the ROADMAP-TYPE-VOCABULARY block with columns `Trigger | Structural Change | Type | Observable Signal | Probability Weight`.
DO NOT label it optional.
The Type column MUST contain only values from the ROADMAP-TYPE-VOCABULARY closed set: `Structural / Process / Personnel / Governance`.
DO NOT use Type values outside this closed set -- using trigger type labels (Capacity / Strategic) in the roadmap Type column is a constraint violation.
DO include at minimum two rows:
  Row 1: a headcount threshold trigger.
  Row 2: MUST come from a different category -- a workload signal, structural symptom, or milestone event.
DO NOT use two headcount thresholds as the two rows.
DO include a `WATCH-FIRST:` declaration naming the leading indicator to monitor before acting.

ROADMAP-TRIGGER-DIVERSITY -- REQUIRED AFTER ORG EVOLUTION ROADMAP

DO emit a `ROADMAP-TRIGGER-DIVERSITY:` block immediately after the Org Evolution Roadmap table.
For each tier row in the roadmap, enumerate its Observable Signal with a declared trigger type from this closed set: `Capacity / Process / Strategic / Structural`.
DO format each entry as: `[Tier/Row label] -- [Observable Signal text] -- [Trigger Type]`
DO count the number of distinct trigger types present across all rows.
DO emit: `Trigger type diversity: [N] distinct types ([comma-separated list of types used])`
MINIMUM TWO DISTINCT TRIGGER TYPES are required across all roadmap tier signals.
If fewer than two distinct trigger types are present, this is a constraint violation -- revise the roadmap Observable Signal column before proceeding.
DO NOT proceed to TRIGGER-TYPE-ACCOUNTING until this block is present and the diversity count is >= 2.

TRIGGER-TYPE-ACCOUNTING -- REQUIRED IMMEDIATELY AFTER ROADMAP-TRIGGER-DIVERSITY

DO emit a `TRIGGER-TYPE-ACCOUNTING:` block immediately after the ROADMAP-TRIGGER-DIVERSITY block.
For each trigger type in the ROADMAP-TRIGGER-DIVERSITY closed set (Capacity / Process / Strategic / Structural), emit one row:
  - Used type: `[Trigger Type] -- TYPE-USED`
  - Unused type: `[Trigger Type] -- TYPE-UNUSED`
DO NOT skip any type from the declared closed set.
A TYPE-UNUSED row makes the absent trigger type a directly scannable row rather than an implicit absence from the diversity count.
DO NOT proceed to REGISTER-ROADMAP-CORRESPONDENCE until this block is complete with one row per declared trigger type.

REGISTER-ROADMAP-CORRESPONDENCE -- REQUIRED AFTER TRIGGER-TYPE-ACCOUNTING

DO emit a `REGISTER-ROADMAP-CORRESPONDENCE:` block immediately after the TRIGGER-TYPE-ACCOUNTING block.
For each cat-1 (Areas) entry in the ORG-ELEMENT REGISTER, emit one row:
  - Addressed area: `[area name] -- [roadmap row label or structural change referencing this area] -- ROADMAP-COVERED`
  - Unaddressed area: `[area name] -- ROADMAP-UNCOVERED`
DO NOT skip any cat-1 area from the ORG-ELEMENT REGISTER.
A ROADMAP-UNCOVERED row is a constraint violation -- add a roadmap row whose Structural Change addresses the uncovered area before proceeding.
DO NOT proceed to Anti-Pattern Watch until every cat-1 area has a ROADMAP-COVERED verdict.

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

DO produce this section after the REGISTER-ROADMAP-CORRESPONDENCE block with columns `Anti-Pattern | Why It Applies Here | Mitigation`.
MUST open each `Why It Applies Here` cell with typed citation syntax: `[element name] (cat-N) -- [one sentence of specific relevance]`.
DO NOT write a cell that names an element without the `(cat-N)` typed syntax.
DO NOT use a `cat-N` code that does not match the REGISTER-CATEGORY-CONTRACT schema.
DO include at minimum two anti-pattern rows.

SECTION ORDER

DO produce sections in this exact sequence:
1. ROLES-LOADED or ROLES-NOTE
2. ROLE-LOAD-ORDER: named block
3. ROLE-TYPE-CLASSIFICATION:
4. ROLE-TIER-ACCOUNTING:
5. `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
6. Inertia Assessment (Case for Staying Flat [FLAT-CASE-CLOSED] / How We Coordinate Today / Rebuttal / VERDICT [FLAT-CASE-PRESSURE line])
7. `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
8. ASCII Org Diagram (box-drawing characters)
9. `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
10. Headcount by Area
11. Operating Rhythm Table
12. Committee Charters (QUORUM-DENOMINATOR CONSTRAINT + six fields per charter)
13. CHARTER-COMPLETENESS-AUDIT:
14. CHARTER-RHYTHM-PARITY:
15. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
16. REGISTER-CATEGORY-CONTRACT:
17. ORG-ELEMENT REGISTER
18. REGISTER-POPULATION-AUDIT:
19. ROADMAP-TYPE-VOCABULARY: (with VOCABULARY-DISAMBIGUATION note)
20. Org Evolution Roadmap (Type column: Structural/Process/Personnel/Governance only)
21. ROADMAP-TRIGGER-DIVERSITY:
22. TRIGGER-TYPE-ACCOUNTING: (TYPE-USED/TYPE-UNUSED per type)
23. REGISTER-ROADMAP-CORRESPONDENCE: (cat-1 areas, ROADMAP-COVERED/ROADMAP-UNCOVERED)
24. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-04: A-40 Spec Alignment + Full A-41 Spec Combined (V-01 + V-02)

**Axis:** TYPE-REPRESENTED/TYPE-ABSENT + count rows AND all-four-categories bidirectional
correspondence, without ROADMAP-TYPE-VOCABULARY
**Hypothesis:** The terminology fix and scope expansion compose without interference; TRIGGER-TYPE-
ACCOUNTING rows reference the ROADMAP-TRIGGER-DIVERSITY closed set for type labels while
REGISTER-ROADMAP-CORRESPONDENCE operates over the register domain independently; tests whether
A-40+A-41 precision improvements are sufficient or whether A-42 vocabulary block is also needed

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role in the format `- [role name] -- [one-line description from role file]`.
DO NOT invent role names unless no roles files are found.
If no files are found, DO produce a `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` block instead, with one inferred entry per role in the format `- [role name] -- [description]`.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER:

Canonical three-tier classification sequence declared as a standalone named block:
1. Engineering types first
2. Operations types second
3. PM, Design, Research, and Other types last

If no Engineering roles are present, begin with Operations types.
If neither Engineering nor Operations roles are present, classify all roles in any order.
DO NOT interleave tiers -- complete all entries in one tier before writing any entry from the next tier.
This block is the independently verifiable ordering declaration for ROLE-TYPE-CLASSIFICATION.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE, following the ROLE-LOAD-ORDER three-tier constraint above.
DO assign each role exactly one domain type from this closed set: `Engineering / PM / Design / Operations / Research / Other`.
DO format each entry as `- [role name] -- [domain type]`.
DO NOT skip this block.
DO NOT proceed until every role from ROLES-LOADED or ROLES-NOTE is classified.
DO annotate each Key Roles cell in the Headcount by Area table in the format `[role name] ([domain type])`.
DO annotate each Membership field in Committee Charters in the same format `[role name] ([domain type])`.

ROLE-TIER-ACCOUNTING -- REQUIRED IMMEDIATELY AFTER ROLE-TYPE-CLASSIFICATION

DO emit a `ROLE-TIER-ACCOUNTING:` block immediately after ROLE-TYPE-CLASSIFICATION.
For each tier declared in the ROLE-LOAD-ORDER block (Engineering / Operations / remaining types), emit one row:
- Populated tier: `[Tier] -- [N roles] -- TIER-PRESENT`
- Empty tier: `[Tier] -- 0 roles -- TIER-ABSENT`
DO NOT skip any declared tier. A TIER-ABSENT row makes the population gap a directly scannable row.

When all roles are classified and tier accounting is complete, DO emit:
`=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
DO NOT proceed to the Inertia Assessment until this gate line is present in the output.

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.
DO NOT write an org diagram as the first section.
DO structure the inertia assessment in this exact four-sub-section order: Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

Sub-section 1 -- Case for Staying Flat

DO produce a three-column mechanism evidence table with columns `Mechanism Name | Type | Frequency / Participants`.
DO include at minimum two data rows.
The Type column MUST contain only values from this closed vocabulary: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
DO NOT use Type values outside this vocabulary.
Each Mechanism Name MUST name a specific, observable coordination mechanism.
DO NOT move mechanism-typed table content into Sub-section 2.

After writing the table, DO count the data rows (header row excluded).
IF count < 2: DO write the missing mechanism row(s) until count reaches 2.
THEN substitute the final row count as N and DO emit exactly:
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
DO NOT emit this separator before count >= 2.
DO NOT begin Sub-section 2 before this separator is present in the output.

Sub-section 2 -- How We Coordinate Today

DO inventory the coordination patterns currently in active use.
DO name channels, cadences, informal roles, and artifacts with frequency and participants.
DO NOT re-list entries from the Sub-section 1 table.

Sub-section 3 -- Rebuttal

DO name the coordination failure the flat-team case and current mechanisms cannot answer.
DO reference a specific observable: a blocked decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap.
DO NOT write "the team is growing" without specifying the failure mode.

Sub-section 4 -- VERDICT and Re-assessment Trigger

MUST open this sub-section with a pressure rating line in this format:
`FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
The rating MUST be exactly one value from this closed set: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
DO NOT omit this line.
DO NOT emit the verdict declaration before this line is present.
After emitting the pressure line, DO choose exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
The reasoning sentence MUST reference the FLAT-CASE-PRESSURE rating by name.
DO write a re-assessment trigger immediately after the verdict naming a concrete threshold.
DO NOT write "revisit as the team grows."
DO NOT proceed past the VERDICT until the pressure line, verdict declaration, and re-assessment trigger are all written.

When VERDICT is written, DO emit:
`=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
DO NOT draw any org boxes until this gate line is present in the output.

ASCII ORG DIAGRAM

DO draw an ASCII hierarchy after the inertia assessment phase gate.
DO show at minimum two levels.
DO NOT produce a flat list of names without hierarchy.
DO show committees as distinct labeled nodes, not embedded in one area.
DO use role names from ROLES-LOADED or ROLES-NOTE -- DO NOT introduce new role names.
DO use box-drawing characters (`+`, `-`, `|`) for the diagram, not indented lists or plain-text trees.

When the org diagram is complete, DO emit:
`=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
DO NOT begin the Headcount table until this gate line is present in the output.

HEADCOUNT BY AREA -- DECIDES / ESCALATES REQUIRED

DO produce a headcount table with columns `Area | Headcount | Key Roles | Decides | Escalates`.
DO NOT use a single `Decision Scope` column -- the Decides and Escalates columns are separate and both REQUIRED.
DO NOT write `owns the area` or generic ownership phrases in either column.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward, naming the destination role or forum.
DO annotate each Key Roles entry in the format `[role name] ([domain type])` from ROLE-TYPE-CLASSIFICATION.
DO include at minimum two area rows with individual counts plus a `**Total**` row with the sum.
DO NOT produce only a single total with no area breakdown.

OPERATING RHYTHM TABLE

DO produce a cadence table after the headcount section with columns `Cadence | Frequency | DRI / Owner | Purpose`.
DO include at minimum three distinct rows: one ROB, one shiproom or gate meeting, and one governance meeting.
DO NOT combine two meetings into one row.
DO NOT produce a rhythm table with only ROB.
DO reference a role from ROLES-LOADED in the `DRI / Owner` column where possible.

COMMITTEE CHARTERS -- SIX FIELDS REQUIRED

DO write a charter for each governance meeting in the rhythm table.
DO include all six fields: `Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`, `Dissolves When`.
DO NOT label this section optional.
DO NOT write a rhythm table row for a committee and then omit its charter.
DO annotate each Membership role in the format `[role name] ([domain type])` from ROLE-TYPE-CLASSIFICATION, listing at minimum two roles.
DO populate the Escalates field with a named destination.
DO NOT write `everything not listed under Decides.`

Before writing the Quorum line for each charter:
DO emit a `QUORUM-DENOMINATOR CONSTRAINT: M = [count of roles listed in this charter's Membership field]` line.
DO populate the Quorum field using this format: `Quorum: [N] of [M] member roles required for binding decisions`, where M MUST equal the QUORUM-DENOMINATOR CONSTRAINT value above.
DO NOT use the short `Quorum: [N roles required for binding decisions]` form -- the full N-of-M fraction is required.
DO NOT omit the Quorum field from any charter.

DO populate the `Dissolves When` field with specific, observable dissolution conditions.
DO NOT write "when no longer needed" or equivalent vague conditions.
DO NOT omit the Dissolves When field from any charter.

CHARTER-COMPLETENESS-AUDIT -- REQUIRED AFTER ALL CHARTERS

After all committee charters are written:
DO emit a `CHARTER-COMPLETENESS-AUDIT:` block as a single table with one row per charter.
Columns: `Charter | Purpose | Membership | Decides | Escalates | Quorum | Dissolves When | QUORUM-DENOMINATOR CONSTRAINT`
Each cell: `PRESENT` or `MISSING`.
Any cell marked `MISSING` blocks the CHARTERS COMPLETE gate -- write the missing field before proceeding.
DO NOT emit the CHARTERS COMPLETE gate until every cell in this audit table is `PRESENT`.

CHARTER-RHYTHM-PARITY -- REQUIRED AFTER CHARTER-COMPLETENESS-AUDIT

DO emit a `CHARTER-RHYTHM-PARITY:` block immediately after the CHARTER-COMPLETENESS-AUDIT block.
DO produce a two-column table with columns `Charter Name | Rhythm Table Governance Row`.
DO map every charter to its corresponding governance row in the Operating Rhythm Table.
DO verify bidirectional correspondence:
  - Every charter MUST name a governance row that exists in the Operating Rhythm Table.
  - Every governance row in the Operating Rhythm Table MUST have a corresponding charter.
If any charter lacks a corresponding rhythm row, emit `[charter name] | NO MATCHING RHYTHM ROW -- PARITY VIOLATION`.
If any governance rhythm row lacks a charter, emit `MISSING CHARTER FOR: [rhythm row name] -- PARITY VIOLATION`.
DO NOT emit the CHARTERS COMPLETE gate if any PARITY VIOLATION row is present.
Only emit the gate after this block confirms full bidirectional correspondence.

When the CHARTER-COMPLETENESS-AUDIT and CHARTER-RHYTHM-PARITY blocks both confirm full coverage:
DO emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
DO NOT begin the ORG-ELEMENT REGISTER until this gate line is present in the output.

ORG-ELEMENT REGISTER -- REQUIRED BEFORE ORG EVOLUTION ROADMAP

Before writing the register body, DO emit a `REGISTER-CATEGORY-CONTRACT:` block enumerating each valid category label as a separate line item:
- cat-1 (Areas)
- cat-2 (Committees/Cadences)
- cat-3 (Headcount)
- cat-4 (DRI Roles)
Any category label used in the register body that is not listed in this block is a constraint violation.

MUST produce an `ORG-ELEMENT REGISTER` block immediately after the REGISTER-CATEGORY-CONTRACT block.
DO NOT skip it.
DO NOT proceed to REGISTER-POPULATION-AUDIT until all four category entries are populated:
  `cat-1 (Areas)` -- all area names from the Headcount table, each as `- [area name] -- headcount: [N]`
  `cat-2 (Committees/Cadences)` -- all committee and cadence names from the Rhythm Table and Charters, each as `- [name]`
  `cat-3 (Headcount)` -- total headcount as `- Total headcount: [N]`
  `cat-4 (DRI Roles)` -- all DRI role names from the Operating Rhythm Table, each as `- [DRI role]`

REGISTER-POPULATION-AUDIT -- REQUIRED IMMEDIATELY AFTER ORG-ELEMENT REGISTER

DO emit a `REGISTER-POPULATION-AUDIT:` block immediately after the ORG-ELEMENT REGISTER body.
For each category declared in the REGISTER-CATEGORY-CONTRACT block, emit one row:
  - Populated category: `[category label] -- [N entries] -- CATEGORY-POPULATED`
  - Empty category: `[category label] -- 0 entries -- CATEGORY-EMPTY`
DO NOT skip any category declared in the REGISTER-CATEGORY-CONTRACT block.
A CATEGORY-EMPTY row is a constraint violation -- add the missing entries to the register before proceeding.
DO NOT proceed to the Org Evolution Roadmap until all declared categories have a CATEGORY-POPULATED verdict.

ORG EVOLUTION ROADMAP -- REQUIRED

DO produce a trigger table after the REGISTER-POPULATION-AUDIT block with columns `Trigger | Structural Change | Type | Observable Signal | Probability Weight`.
DO NOT label it optional.
DO include at minimum two rows:
  Row 1: a headcount threshold trigger.
  Row 2: MUST come from a different category -- a workload signal, structural symptom, or milestone event.
DO NOT use two headcount thresholds as the two rows.
DO include a `WATCH-FIRST:` declaration naming the leading indicator to monitor before acting.

ROADMAP-TRIGGER-DIVERSITY -- REQUIRED AFTER ORG EVOLUTION ROADMAP

DO emit a `ROADMAP-TRIGGER-DIVERSITY:` block immediately after the Org Evolution Roadmap table.
For each tier row in the roadmap, enumerate its Observable Signal with a declared trigger type from this closed set: `Capacity / Process / Strategic / Structural`.
DO format each entry as: `[Tier/Row label] -- [Observable Signal text] -- [Trigger Type]`
DO count the number of distinct trigger types present across all rows.
DO emit: `Trigger type diversity: [N] distinct types ([comma-separated list of types used])`
MINIMUM TWO DISTINCT TRIGGER TYPES are required across all roadmap tier signals.
If fewer than two distinct trigger types are present, this is a constraint violation -- revise the roadmap Observable Signal column before proceeding.
DO NOT proceed to TRIGGER-TYPE-ACCOUNTING until this block is present and the diversity count is >= 2.

TRIGGER-TYPE-ACCOUNTING -- REQUIRED IMMEDIATELY AFTER ROADMAP-TRIGGER-DIVERSITY

DO emit a `TRIGGER-TYPE-ACCOUNTING:` block immediately after the ROADMAP-TRIGGER-DIVERSITY block.
For each trigger type in the ROADMAP-TRIGGER-DIVERSITY closed set (Capacity / Process / Strategic / Structural), emit one row using this three-element format:
  - Type with >= 1 tier signal: `[Trigger Type] -- [N signals] -- TYPE-REPRESENTED`
  - Type with 0 tier signals: `[Trigger Type] -- 0 signals -- TYPE-ABSENT`
DO NOT use TYPE-USED or TYPE-UNUSED -- the required verdict labels are TYPE-REPRESENTED and TYPE-ABSENT.
DO NOT omit the signal count -- each row MUST state the count of roadmap tier signals assigned that type.
DO NOT skip any type from the declared closed set.
A TYPE-ABSENT row makes the absent trigger type a directly scannable row rather than an implicit absence from the diversity count.
The ROADMAP-TRIGGER-DIVERSITY >= 2 constraint remains independently enforced; TRIGGER-TYPE-ACCOUNTING is additive full-set accounting with per-type count.
DO NOT proceed to REGISTER-ROADMAP-CORRESPONDENCE until this block is complete with one row per declared trigger type.

REGISTER-ROADMAP-CORRESPONDENCE -- REQUIRED AFTER TRIGGER-TYPE-ACCOUNTING

DO emit a `REGISTER-ROADMAP-CORRESPONDENCE:` block immediately after the TRIGGER-TYPE-ACCOUNTING block.
This block closes the cross-domain alignment gap: each register category must correspond to a roadmap tier Observable Signal, and each roadmap tier must be anchored to a register category.

DO produce a three-column correspondence table with columns `Register Category | Corresponding Roadmap Tier | Observable Signal Link`.
For each category declared in the REGISTER-CATEGORY-CONTRACT block (cat-1 through cat-4), emit one row:
  - Category with a corresponding roadmap tier: `[category label] -- [roadmap tier / row label] -- [Observable Signal activated by changes in this category's population or composition]`
  - Category with no corresponding roadmap tier: `[category label] -- COVERAGE-GAP -- no roadmap tier signal linked to this register category`
DO NOT skip any register category declared in the REGISTER-CATEGORY-CONTRACT block.
A COVERAGE-GAP row is a constraint violation -- add a roadmap row whose Observable Signal links to the uncovered register category before proceeding.

After completing the register-to-roadmap direction, verify the reverse direction:
For each roadmap tier present in the Org Evolution Roadmap table that does NOT already appear in a correspondence row above:
  emit `UNANCHORED-TRIGGER: [roadmap tier / row label] -- no register category linked to this tier's Observable Signal`
An UNANCHORED-TRIGGER row is a constraint violation -- link the tier's Observable Signal to the most relevant register category before proceeding.

DO NOT proceed to Anti-Pattern Watch until all COVERAGE-GAP and UNANCHORED-TRIGGER violations are resolved.

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

DO produce this section after the REGISTER-ROADMAP-CORRESPONDENCE block with columns `Anti-Pattern | Why It Applies Here | Mitigation`.
MUST open each `Why It Applies Here` cell with typed citation syntax: `[element name] (cat-N) -- [one sentence of specific relevance]`.
DO NOT write a cell that names an element without the `(cat-N)` typed syntax.
DO NOT use a `cat-N` code that does not match the REGISTER-CATEGORY-CONTRACT schema.
DO include at minimum two anti-pattern rows.

SECTION ORDER

DO produce sections in this exact sequence:
1. ROLES-LOADED or ROLES-NOTE
2. ROLE-LOAD-ORDER: named block
3. ROLE-TYPE-CLASSIFICATION:
4. ROLE-TIER-ACCOUNTING:
5. `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
6. Inertia Assessment (Case for Staying Flat [FLAT-CASE-CLOSED] / How We Coordinate Today / Rebuttal / VERDICT [FLAT-CASE-PRESSURE line])
7. `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
8. ASCII Org Diagram (box-drawing characters)
9. `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
10. Headcount by Area
11. Operating Rhythm Table
12. Committee Charters (QUORUM-DENOMINATOR CONSTRAINT + six fields per charter)
13. CHARTER-COMPLETENESS-AUDIT:
14. CHARTER-RHYTHM-PARITY:
15. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
16. REGISTER-CATEGORY-CONTRACT:
17. ORG-ELEMENT REGISTER
18. REGISTER-POPULATION-AUDIT:
19. Org Evolution Roadmap
20. ROADMAP-TRIGGER-DIVERSITY:
21. TRIGGER-TYPE-ACCOUNTING: (three-element rows: type -- N signals -- TYPE-REPRESENTED/TYPE-ABSENT)
22. REGISTER-ROADMAP-CORRESPONDENCE: (all 4 categories + bidirectional COVERAGE-GAP / UNANCHORED-TRIGGER)
23. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-05: Full Integration -- V-01 + V-02 + V-03 on R17-V-05 Baseline

**Axis:** All three precision improvements simultaneously
**Hypothesis:** TYPE-REPRESENTED/TYPE-ABSENT + per-type count (A-40), all-four-categories
bidirectional correspondence with COVERAGE-GAP/UNANCHORED-TRIGGER (A-41), and ROADMAP-TYPE-
VOCABULARY + VOCABULARY-DISAMBIGUATION (A-42) together produce an output passing all 42
aspirational criteria under rubric v16 with no regressions; the five-layer roadmap verification
chain is: declare type vocabulary -> write roadmap -> verify trigger diversity -> account types
per-represented/absent -> verify register-roadmap alignment bidirectionally

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role in the format `- [role name] -- [one-line description from role file]`.
DO NOT invent role names unless no roles files are found.
If no files are found, DO produce a `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` block instead, with one inferred entry per role in the format `- [role name] -- [description]`.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER:

Canonical three-tier classification sequence declared as a standalone named block:
1. Engineering types first
2. Operations types second
3. PM, Design, Research, and Other types last

If no Engineering roles are present, begin with Operations types.
If neither Engineering nor Operations roles are present, classify all roles in any order.
DO NOT interleave tiers -- complete all entries in one tier before writing any entry from the next tier.
This block is the independently verifiable ordering declaration for ROLE-TYPE-CLASSIFICATION.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE, following the ROLE-LOAD-ORDER three-tier constraint above.
DO assign each role exactly one domain type from this closed set: `Engineering / PM / Design / Operations / Research / Other`.
DO format each entry as `- [role name] -- [domain type]`.
DO NOT skip this block.
DO NOT proceed until every role from ROLES-LOADED or ROLES-NOTE is classified.
DO annotate each Key Roles cell in the Headcount by Area table in the format `[role name] ([domain type])`.
DO annotate each Membership field in Committee Charters in the same format `[role name] ([domain type])`.

ROLE-TIER-ACCOUNTING -- REQUIRED IMMEDIATELY AFTER ROLE-TYPE-CLASSIFICATION

DO emit a `ROLE-TIER-ACCOUNTING:` block immediately after ROLE-TYPE-CLASSIFICATION.
For each tier declared in the ROLE-LOAD-ORDER block (Engineering / Operations / remaining types), emit one row:
- Populated tier: `[Tier] -- [N roles] -- TIER-PRESENT`
- Empty tier: `[Tier] -- 0 roles -- TIER-ABSENT`
DO NOT skip any declared tier. A TIER-ABSENT row makes the population gap a directly scannable row.

When all roles are classified and tier accounting is complete, DO emit:
`=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
DO NOT proceed to the Inertia Assessment until this gate line is present in the output.

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.
DO NOT write an org diagram as the first section.
DO structure the inertia assessment in this exact four-sub-section order: Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

Sub-section 1 -- Case for Staying Flat

DO produce a three-column mechanism evidence table with columns `Mechanism Name | Type | Frequency / Participants`.
DO include at minimum two data rows.
The Type column MUST contain only values from this closed vocabulary: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
DO NOT use Type values outside this vocabulary.
Each Mechanism Name MUST name a specific, observable coordination mechanism.
DO NOT move mechanism-typed table content into Sub-section 2.

After writing the table, DO count the data rows (header row excluded).
IF count < 2: DO write the missing mechanism row(s) until count reaches 2.
THEN substitute the final row count as N and DO emit exactly:
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
DO NOT emit this separator before count >= 2.
DO NOT begin Sub-section 2 before this separator is present in the output.

Sub-section 2 -- How We Coordinate Today

DO inventory the coordination patterns currently in active use.
DO name channels, cadences, informal roles, and artifacts with frequency and participants.
DO NOT re-list entries from the Sub-section 1 table.

Sub-section 3 -- Rebuttal

DO name the coordination failure the flat-team case and current mechanisms cannot answer.
DO reference a specific observable: a blocked decision, missed SLA, time-zone gap, knowledge silo, or competing roadmap.
DO NOT write "the team is growing" without specifying the failure mode.

Sub-section 4 -- VERDICT and Re-assessment Trigger

MUST open this sub-section with a pressure rating line in this format:
`FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
The rating MUST be exactly one value from this closed set: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
DO NOT omit this line.
DO NOT emit the verdict declaration before this line is present.
After emitting the pressure line, DO choose exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
The reasoning sentence MUST reference the FLAT-CASE-PRESSURE rating by name.
DO write a re-assessment trigger immediately after the verdict naming a concrete threshold.
DO NOT write "revisit as the team grows."
DO NOT proceed past the VERDICT until the pressure line, verdict declaration, and re-assessment trigger are all written.

When VERDICT is written, DO emit:
`=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
DO NOT draw any org boxes until this gate line is present in the output.

ASCII ORG DIAGRAM

DO draw an ASCII hierarchy after the inertia assessment phase gate.
DO show at minimum two levels.
DO NOT produce a flat list of names without hierarchy.
DO show committees as distinct labeled nodes, not embedded in one area.
DO use role names from ROLES-LOADED or ROLES-NOTE -- DO NOT introduce new role names.
DO use box-drawing characters (`+`, `-`, `|`) for the diagram, not indented lists or plain-text trees.

When the org diagram is complete, DO emit:
`=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
DO NOT begin the Headcount table until this gate line is present in the output.

HEADCOUNT BY AREA -- DECIDES / ESCALATES REQUIRED

DO produce a headcount table with columns `Area | Headcount | Key Roles | Decides | Escalates`.
DO NOT use a single `Decision Scope` column -- the Decides and Escalates columns are separate and both REQUIRED.
DO NOT write `owns the area` or generic ownership phrases in either column.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward, naming the destination role or forum.
DO annotate each Key Roles entry in the format `[role name] ([domain type])` from ROLE-TYPE-CLASSIFICATION.
DO include at minimum two area rows with individual counts plus a `**Total**` row with the sum.
DO NOT produce only a single total with no area breakdown.

OPERATING RHYTHM TABLE

DO produce a cadence table after the headcount section with columns `Cadence | Frequency | DRI / Owner | Purpose`.
DO include at minimum three distinct rows: one ROB, one shiproom or gate meeting, and one governance meeting.
DO NOT combine two meetings into one row.
DO NOT produce a rhythm table with only ROB.
DO reference a role from ROLES-LOADED in the `DRI / Owner` column where possible.

COMMITTEE CHARTERS -- SIX FIELDS REQUIRED

DO write a charter for each governance meeting in the rhythm table.
DO include all six fields: `Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`, `Dissolves When`.
DO NOT label this section optional.
DO NOT write a rhythm table row for a committee and then omit its charter.
DO annotate each Membership role in the format `[role name] ([domain type])` from ROLE-TYPE-CLASSIFICATION, listing at minimum two roles.
DO populate the Escalates field with a named destination.
DO NOT write `everything not listed under Decides.`

Before writing the Quorum line for each charter:
DO emit a `QUORUM-DENOMINATOR CONSTRAINT: M = [count of roles listed in this charter's Membership field]` line.
DO populate the Quorum field using this format: `Quorum: [N] of [M] member roles required for binding decisions`, where M MUST equal the QUORUM-DENOMINATOR CONSTRAINT value above.
DO NOT use the short `Quorum: [N roles required for binding decisions]` form -- the full N-of-M fraction is required.
DO NOT omit the Quorum field from any charter.

DO populate the `Dissolves When` field with specific, observable dissolution conditions.
DO NOT write "when no longer needed" or equivalent vague conditions.
DO NOT omit the Dissolves When field from any charter.

CHARTER-COMPLETENESS-AUDIT -- REQUIRED AFTER ALL CHARTERS

After all committee charters are written:
DO emit a `CHARTER-COMPLETENESS-AUDIT:` block as a single table with one row per charter.
Columns: `Charter | Purpose | Membership | Decides | Escalates | Quorum | Dissolves When | QUORUM-DENOMINATOR CONSTRAINT`
Each cell: `PRESENT` or `MISSING`.
Any cell marked `MISSING` blocks the CHARTERS COMPLETE gate -- write the missing field before proceeding.
DO NOT emit the CHARTERS COMPLETE gate until every cell in this audit table is `PRESENT`.

CHARTER-RHYTHM-PARITY -- REQUIRED AFTER CHARTER-COMPLETENESS-AUDIT

DO emit a `CHARTER-RHYTHM-PARITY:` block immediately after the CHARTER-COMPLETENESS-AUDIT block.
DO produce a two-column table with columns `Charter Name | Rhythm Table Governance Row`.
DO map every charter to its corresponding governance row in the Operating Rhythm Table.
DO verify bidirectional correspondence:
  - Every charter MUST name a governance row that exists in the Operating Rhythm Table.
  - Every governance row in the Operating Rhythm Table MUST have a corresponding charter.
If any charter lacks a corresponding rhythm row, emit `[charter name] | NO MATCHING RHYTHM ROW -- PARITY VIOLATION`.
If any governance rhythm row lacks a charter, emit `MISSING CHARTER FOR: [rhythm row name] -- PARITY VIOLATION`.
DO NOT emit the CHARTERS COMPLETE gate if any PARITY VIOLATION row is present.
Only emit the gate after this block confirms full bidirectional correspondence.

When the CHARTER-COMPLETENESS-AUDIT and CHARTER-RHYTHM-PARITY blocks both confirm full coverage:
DO emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
DO NOT begin the ORG-ELEMENT REGISTER until this gate line is present in the output.

ORG-ELEMENT REGISTER -- REQUIRED BEFORE ORG EVOLUTION ROADMAP

Before writing the register body, DO emit a `REGISTER-CATEGORY-CONTRACT:` block enumerating each valid category label as a separate line item:
- cat-1 (Areas)
- cat-2 (Committees/Cadences)
- cat-3 (Headcount)
- cat-4 (DRI Roles)
Any category label used in the register body that is not listed in this block is a constraint violation.

MUST produce an `ORG-ELEMENT REGISTER` block immediately after the REGISTER-CATEGORY-CONTRACT block.
DO NOT skip it.
DO NOT proceed to REGISTER-POPULATION-AUDIT until all four category entries are populated:
  `cat-1 (Areas)` -- all area names from the Headcount table, each as `- [area name] -- headcount: [N]`
  `cat-2 (Committees/Cadences)` -- all committee and cadence names from the Rhythm Table and Charters, each as `- [name]`
  `cat-3 (Headcount)` -- total headcount as `- Total headcount: [N]`
  `cat-4 (DRI Roles)` -- all DRI role names from the Operating Rhythm Table, each as `- [DRI role]`

REGISTER-POPULATION-AUDIT -- REQUIRED IMMEDIATELY AFTER ORG-ELEMENT REGISTER

DO emit a `REGISTER-POPULATION-AUDIT:` block immediately after the ORG-ELEMENT REGISTER body.
For each category declared in the REGISTER-CATEGORY-CONTRACT block, emit one row:
  - Populated category: `[category label] -- [N entries] -- CATEGORY-POPULATED`
  - Empty category: `[category label] -- 0 entries -- CATEGORY-EMPTY`
DO NOT skip any category declared in the REGISTER-CATEGORY-CONTRACT block.
A CATEGORY-EMPTY row is a constraint violation -- add the missing entries to the register before proceeding.
DO NOT proceed to ROADMAP-TYPE-VOCABULARY until all declared categories have a CATEGORY-POPULATED verdict.

ROADMAP-TYPE-VOCABULARY -- REQUIRED BEFORE ORG EVOLUTION ROADMAP

Before writing the Org Evolution Roadmap table, DO emit a `ROADMAP-TYPE-VOCABULARY:` block declaring the valid Type column values as a closed set. Each valid label is a separate line item:
- Structural
- Process
- Personnel
- Governance
Any Type value used in the roadmap table that is not listed in this block is a constraint violation.
This block governs the roadmap's Type column -- the nature of the structural change being triggered.
This block is the independently verifiable vocabulary declaration for the roadmap Type column, parallel to REGISTER-CATEGORY-CONTRACT for the register body.

VOCABULARY-DISAMBIGUATION:
The ROADMAP-TYPE-VOCABULARY closed set (Structural / Process / Personnel / Governance) classifies
the nature of the structural change a trigger produces. This is a distinct classification axis from
the ROADMAP-TRIGGER-DIVERSITY closed set (Capacity / Process / Strategic / Structural), which
classifies the nature of the observable signal that triggers the change. Both axes share the labels
"Process" and "Structural" but with different referents:
  - ROADMAP-TYPE-VOCABULARY "Process": the triggered change is a process adjustment
  - ROADMAP-TRIGGER-DIVERSITY "Process": the observable signal is a process-level event
  - ROADMAP-TYPE-VOCABULARY "Structural": the triggered change is an org structure change
  - ROADMAP-TRIGGER-DIVERSITY "Structural": the observable signal is a structural symptom
DO NOT populate the roadmap Type column with trigger type labels (Capacity / Strategic) -- those
belong only in ROADMAP-TRIGGER-DIVERSITY type assignments, never in the roadmap Type column.

ORG EVOLUTION ROADMAP -- REQUIRED

DO produce a trigger table after the ROADMAP-TYPE-VOCABULARY block with columns `Trigger | Structural Change | Type | Observable Signal | Probability Weight`.
DO NOT label it optional.
The Type column MUST contain only values from the ROADMAP-TYPE-VOCABULARY closed set: `Structural / Process / Personnel / Governance`.
DO NOT use Type values outside this closed set -- using trigger type labels (Capacity / Strategic) in the roadmap Type column is a constraint violation.
DO include at minimum two rows:
  Row 1: a headcount threshold trigger.
  Row 2: MUST come from a different category -- a workload signal, structural symptom, or milestone event.
DO NOT use two headcount thresholds as the two rows.
DO include a `WATCH-FIRST:` declaration naming the leading indicator to monitor before acting.

ROADMAP-TRIGGER-DIVERSITY -- REQUIRED AFTER ORG EVOLUTION ROADMAP

DO emit a `ROADMAP-TRIGGER-DIVERSITY:` block immediately after the Org Evolution Roadmap table.
For each tier row in the roadmap, enumerate its Observable Signal with a declared trigger type from this closed set: `Capacity / Process / Strategic / Structural`.
DO format each entry as: `[Tier/Row label] -- [Observable Signal text] -- [Trigger Type]`
DO count the number of distinct trigger types present across all rows.
DO emit: `Trigger type diversity: [N] distinct types ([comma-separated list of types used])`
MINIMUM TWO DISTINCT TRIGGER TYPES are required across all roadmap tier signals.
If fewer than two distinct trigger types are present, this is a constraint violation -- revise the roadmap Observable Signal column before proceeding.
DO NOT proceed to TRIGGER-TYPE-ACCOUNTING until this block is present and the diversity count is >= 2.

TRIGGER-TYPE-ACCOUNTING -- REQUIRED IMMEDIATELY AFTER ROADMAP-TRIGGER-DIVERSITY

DO emit a `TRIGGER-TYPE-ACCOUNTING:` block immediately after the ROADMAP-TRIGGER-DIVERSITY block.
For each trigger type in the ROADMAP-TRIGGER-DIVERSITY closed set (Capacity / Process / Strategic / Structural), emit one row using this three-element format:
  - Type with >= 1 tier signal: `[Trigger Type] -- [N signals] -- TYPE-REPRESENTED`
  - Type with 0 tier signals: `[Trigger Type] -- 0 signals -- TYPE-ABSENT`
DO NOT use TYPE-USED or TYPE-UNUSED -- the required verdict labels are TYPE-REPRESENTED and TYPE-ABSENT.
DO NOT omit the signal count -- each row MUST state the count of roadmap tier signals assigned that type.
DO NOT skip any type from the declared closed set.
A TYPE-ABSENT row makes the absent trigger type a directly scannable row rather than an implicit absence from the diversity count.
The ROADMAP-TRIGGER-DIVERSITY >= 2 constraint remains independently enforced; TRIGGER-TYPE-ACCOUNTING is additive full-set accounting with per-type count.
DO NOT proceed to REGISTER-ROADMAP-CORRESPONDENCE until this block is complete with one row per declared trigger type.

REGISTER-ROADMAP-CORRESPONDENCE -- REQUIRED AFTER TRIGGER-TYPE-ACCOUNTING

DO emit a `REGISTER-ROADMAP-CORRESPONDENCE:` block immediately after the TRIGGER-TYPE-ACCOUNTING block.
This block closes the cross-domain alignment gap: each register category must correspond to a roadmap tier Observable Signal, and each roadmap tier must be anchored to a register category.

DO produce a three-column correspondence table with columns `Register Category | Corresponding Roadmap Tier | Observable Signal Link`.
For each category declared in the REGISTER-CATEGORY-CONTRACT block (cat-1 through cat-4), emit one row:
  - Category with a corresponding roadmap tier: `[category label] -- [roadmap tier / row label] -- [Observable Signal activated by changes in this category's population or composition]`
  - Category with no corresponding roadmap tier: `[category label] -- COVERAGE-GAP -- no roadmap tier signal linked to this register category`
DO NOT skip any register category declared in the REGISTER-CATEGORY-CONTRACT block.
A COVERAGE-GAP row is a constraint violation -- add a roadmap row whose Observable Signal links to the uncovered register category before proceeding.

After completing the register-to-roadmap direction, verify the reverse direction:
For each roadmap tier present in the Org Evolution Roadmap table that does NOT already appear in a correspondence row above:
  emit `UNANCHORED-TRIGGER: [roadmap tier / row label] -- no register category linked to this tier's Observable Signal`
An UNANCHORED-TRIGGER row is a constraint violation -- link the tier's Observable Signal to the most relevant register category before proceeding.

DO NOT proceed to Anti-Pattern Watch until all COVERAGE-GAP and UNANCHORED-TRIGGER violations are resolved.

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

DO produce this section after the REGISTER-ROADMAP-CORRESPONDENCE block with columns `Anti-Pattern | Why It Applies Here | Mitigation`.
MUST open each `Why It Applies Here` cell with typed citation syntax: `[element name] (cat-N) -- [one sentence of specific relevance]`.
DO NOT write a cell that names an element without the `(cat-N)` typed syntax.
DO NOT use a `cat-N` code that does not match the REGISTER-CATEGORY-CONTRACT schema.
DO include at minimum two anti-pattern rows.

SECTION ORDER

DO produce sections in this exact sequence:
1. ROLES-LOADED or ROLES-NOTE
2. ROLE-LOAD-ORDER: named block
3. ROLE-TYPE-CLASSIFICATION:
4. ROLE-TIER-ACCOUNTING:
5. `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
6. Inertia Assessment (Case for Staying Flat [FLAT-CASE-CLOSED] / How We Coordinate Today / Rebuttal / VERDICT [FLAT-CASE-PRESSURE line])
7. `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
8. ASCII Org Diagram (box-drawing characters)
9. `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
10. Headcount by Area
11. Operating Rhythm Table
12. Committee Charters (QUORUM-DENOMINATOR CONSTRAINT + six fields per charter)
13. CHARTER-COMPLETENESS-AUDIT:
14. CHARTER-RHYTHM-PARITY:
15. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
16. REGISTER-CATEGORY-CONTRACT:
17. ORG-ELEMENT REGISTER
18. REGISTER-POPULATION-AUDIT:
19. ROADMAP-TYPE-VOCABULARY: (with VOCABULARY-DISAMBIGUATION note)
20. Org Evolution Roadmap (Type column: Structural/Process/Personnel/Governance only)
21. ROADMAP-TRIGGER-DIVERSITY:
22. TRIGGER-TYPE-ACCOUNTING: (three-element rows: type -- N signals -- TYPE-REPRESENTED/TYPE-ABSENT)
23. REGISTER-ROADMAP-CORRESPONDENCE: (all 4 categories + bidirectional COVERAGE-GAP / UNANCHORED-TRIGGER)
24. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`
