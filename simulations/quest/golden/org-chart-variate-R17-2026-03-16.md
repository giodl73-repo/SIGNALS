---
skill: quest-variate
skill_target: org-chart
date: 2026-03-16
round: R17
rubric_version: v15
status: variate
---

# org-chart Variate -- Round 17 (Rubric v15)

**Date:** 2026-03-16
**Skill:** org-chart
**Rubric:** v15 (criteria C-01 through A-39)
**Round:** R17 overall / Round 2 of the v15 rubric cycle

## R16 ceiling and R17 target

R16-V-05 achieves the maximum composite score of 100.00/100, covering all criteria through A-39.
The R16 scorecard identified two excellence patterns in V-05 that are not yet encoded as rubric
criteria:

1. **Trigger-type accounting gap (A-40 candidate):** ROADMAP-TRIGGER-DIVERSITY confirms >= 2
   distinct trigger types across roadmap rows (A-39 pass). But it does not account for which of
   the four declared types (Capacity / Process / Strategic / Structural) remain unused. A roadmap
   where two of four declared types appear satisfies A-39 while leaving two declared types silently
   absent. ROLE-TIER-ACCOUNTING solves the parallel problem in the role domain: each declared tier
   emits TIER-PRESENT or TIER-ABSENT, making gaps scannable. The same per-type accounting block
   is absent from the trigger type domain.

2. **Register-roadmap correspondence gap (A-41 candidate):** REGISTER-POPULATION-AUDIT confirms
   that every declared register category has >= 1 entry (A-38 pass). But it does not verify that
   each cat-1 (Area) entry has at least one roadmap row that addresses it. The charter domain has
   two-pass verification: CHARTER-COMPLETENESS-AUDIT (field completeness per charter) followed by
   CHARTER-RHYTHM-PARITY (bidirectional charter-rhythm correspondence). The register domain has
   one-pass: REGISTER-POPULATION-AUDIT (category population). No correspondence check exists
   between register areas and roadmap coverage -- an area can be populated in the register while
   receiving zero roadmap attention.

3. **Roadmap type vocabulary gap (A-42 candidate):** The Org Evolution Roadmap has a Type column.
   There is no declared closed set for its values -- REGISTER-CATEGORY-CONTRACT declares valid
   register category labels before the register body, but no parallel vocabulary declaration exists
   for roadmap Type column values. ROLE-TYPE-CLASSIFICATION uses a closed set (Engineering / PM /
   Design / Operations / Research / Other). Mechanism Type in Sub-section 1 uses a closed set
   (Channel / Informal Role / Recurring Cadence / Shared Artifact). Trigger types in ROADMAP-
   TRIGGER-DIVERSITY use a closed set (Capacity / Process / Strategic / Structural). The roadmap
   Type column is the only typed column in the output without a vocabulary constraint.

**R17 target:** Close all three gaps. V-01/V-02/V-03 are single-axis. V-04 combines V-01+V-02.
V-05 integrates all three on the R16-V-05 baseline.

---

## Variation Map

| V    | Axis                                             | Hypothesis                                                                                                                                                                                                          |
|------|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| V-01 | TRIGGER-TYPE-ACCOUNTING: block (A-40 only)       | A per-type accounting block after ROADMAP-TRIGGER-DIVERSITY emitting TYPE-USED/TYPE-UNUSED for each declared trigger type makes unused types a directly scannable row, parallel to ROLE-TIER-ACCOUNTING              |
| V-02 | REGISTER-ROADMAP-CORRESPONDENCE: block (A-41 only) | A per-area correspondence block after ROADMAP-TRIGGER-DIVERSITY verifying each cat-1 area is addressed by at least one roadmap row provides the register domain's second verification pass, parallel to CHARTER-RHYTHM-PARITY |
| V-03 | ROADMAP-TYPE-VOCABULARY: block (A-42 only)       | A closed-set declaration before the roadmap table constraining valid Type column values, parallel to REGISTER-CATEGORY-CONTRACT for the register body and ROLE-TYPE-CLASSIFICATION for role domain types             |
| V-04 | A-40 + A-41 combined                             | The accounting and correspondence blocks compose cleanly without the vocabulary block; tests whether TRIGGER-TYPE-ACCOUNTING and REGISTER-ROADMAP-CORRESPONDENCE reinforce each other with no interference            |
| V-05 | Full integration: A-40 + A-41 + A-42 on R16-V-05 baseline | All three new blocks layered onto the proven foundation; vocabulary declaration before roadmap + two post-roadmap verification blocks form a four-layer chain: declare -> write -> verify diversity -> account types -> verify area coverage |

---

## V-01: Trigger-Type Accounting (A-40 candidate only)

**Axis:** Insert `TRIGGER-TYPE-ACCOUNTING:` block immediately after ROADMAP-TRIGGER-DIVERSITY
**Hypothesis:** Per-type accounting parallel to ROLE-TIER-ACCOUNTING makes unused declared trigger
types a directly scannable TYPE-UNUSED row rather than an implicit absence inferred from the
diversity count alone

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
DO NOT proceed to Anti-Pattern Watch until this block is complete with one row per declared trigger type.

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

DO produce this section after the TRIGGER-TYPE-ACCOUNTING block with columns `Anti-Pattern | Why It Applies Here | Mitigation`.
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
21. TRIGGER-TYPE-ACCOUNTING:
22. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-02: Register-Roadmap Correspondence (A-41 candidate only)

**Axis:** Insert `REGISTER-ROADMAP-CORRESPONDENCE:` block immediately after ROADMAP-TRIGGER-DIVERSITY
**Hypothesis:** A per-area correspondence check verifying each cat-1 register area is addressed by
at least one roadmap row provides the register domain's second verification pass, parallel to
CHARTER-RHYTHM-PARITY in the charter domain -- closing the single-pass gap in register verification

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
DO NOT proceed to REGISTER-ROADMAP-CORRESPONDENCE until this block is present and the diversity count is >= 2.

REGISTER-ROADMAP-CORRESPONDENCE -- REQUIRED AFTER ROADMAP-TRIGGER-DIVERSITY

DO emit a `REGISTER-ROADMAP-CORRESPONDENCE:` block immediately after the ROADMAP-TRIGGER-DIVERSITY block.
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
21. REGISTER-ROADMAP-CORRESPONDENCE:
22. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-03: Roadmap-Type Vocabulary (A-42 candidate only)

**Axis:** Insert `ROADMAP-TYPE-VOCABULARY:` block immediately before the Org Evolution Roadmap
**Hypothesis:** A closed-set declaration for the roadmap Type column, parallel to REGISTER-CATEGORY-
CONTRACT for the register body, makes invalid or ad-hoc Type values a constraint violation rather
than an unconstrained free-text cell -- extending the closed-set discipline already applied to role
types, mechanism types, and trigger types into the final uncontrolled typed column

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

Before writing the Org Evolution Roadmap table, DO emit a `ROADMAP-TYPE-VOCABULARY:` block declaring the valid Type column values as a closed set:
- Structural
- Process
- Personnel
- Governance
Any Type value used in the roadmap table that is not listed in this block is a constraint violation.
This block is the independently verifiable vocabulary declaration for the roadmap Type column, parallel to REGISTER-CATEGORY-CONTRACT for the register body.

ORG EVOLUTION ROADMAP -- REQUIRED

DO produce a trigger table after the ROADMAP-TYPE-VOCABULARY block with columns `Trigger | Structural Change | Type | Observable Signal | Probability Weight`.
DO NOT label it optional.
The Type column MUST contain only values from the ROADMAP-TYPE-VOCABULARY closed set: `Structural / Process / Personnel / Governance`.
DO NOT use Type values outside this closed set.
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
DO NOT proceed to Anti-Pattern Watch until this block is present and the diversity count is >= 2.

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

DO produce this section after the ROADMAP-TRIGGER-DIVERSITY block with columns `Anti-Pattern | Why It Applies Here | Mitigation`.
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
19. ROADMAP-TYPE-VOCABULARY:
20. Org Evolution Roadmap
21. ROADMAP-TRIGGER-DIVERSITY:
22. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-04: A-40 + A-41 Combined (TRIGGER-TYPE-ACCOUNTING + REGISTER-ROADMAP-CORRESPONDENCE)

**Axis:** Per-type accounting and area-to-roadmap correspondence together, no vocabulary block
**Hypothesis:** TRIGGER-TYPE-ACCOUNTING and REGISTER-ROADMAP-CORRESPONDENCE compose cleanly --
the former accounts for which trigger types declared in ROADMAP-TRIGGER-DIVERSITY are used or
unused, the latter verifies that each register area is addressed by at least one roadmap row;
tests composition without the vocabulary constraint from V-03

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
21. TRIGGER-TYPE-ACCOUNTING:
22. REGISTER-ROADMAP-CORRESPONDENCE:
23. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-05: Full Integration -- A-40 + A-41 + A-42 on R16-V-05 Baseline

**Axis:** All three new blocks layered onto the proven R16-V-05 foundation
**Hypothesis:** TRIGGER-TYPE-ACCOUNTING, REGISTER-ROADMAP-CORRESPONDENCE, and ROADMAP-TYPE-
VOCABULARY together close all three R17 gaps with no regressions against A-01 through A-39;
the vocabulary declaration (ROADMAP-TYPE-VOCABULARY) placed before the roadmap table and the two
post-roadmap verification blocks (TRIGGER-TYPE-ACCOUNTING, REGISTER-ROADMAP-CORRESPONDENCE) form
a four-layer roadmap verification chain: declare vocabulary -> write roadmap -> verify trigger
diversity -> account trigger types -> verify area coverage

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

Before writing the Org Evolution Roadmap table, DO emit a `ROADMAP-TYPE-VOCABULARY:` block declaring the valid Type column values as a closed set:
- Structural
- Process
- Personnel
- Governance
Any Type value used in the roadmap table that is not listed in this block is a constraint violation.
This block is the independently verifiable vocabulary declaration for the roadmap Type column, parallel to REGISTER-CATEGORY-CONTRACT for the register body and ROLE-TYPE-CLASSIFICATION for role domain types.

ORG EVOLUTION ROADMAP -- REQUIRED

DO produce a trigger table after the ROADMAP-TYPE-VOCABULARY block with columns `Trigger | Structural Change | Type | Observable Signal | Probability Weight`.
DO NOT label it optional.
The Type column MUST contain only values from the ROADMAP-TYPE-VOCABULARY closed set: `Structural / Process / Personnel / Governance`.
DO NOT use Type values outside this closed set.
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
19. ROADMAP-TYPE-VOCABULARY:
20. Org Evolution Roadmap
21. ROADMAP-TRIGGER-DIVERSITY:
22. TRIGGER-TYPE-ACCOUNTING:
23. REGISTER-ROADMAP-CORRESPONDENCE:
24. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`
