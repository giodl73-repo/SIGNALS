---
skill: quest-variate
skill_target: org-chart
date: 2026-03-16
round: R16
rubric_version: v15
status: variate
---

# org-chart Variate -- Round 16 (Rubric v15)

**Date:** 2026-03-16
**Skill:** org-chart
**Rubric:** v15 (criteria C-01 through A-39)
**Round:** R16 overall / Round 1 of the v15 rubric cycle

## R15 ceiling and R16 target

R15-V-05 achieves coverage of all criteria through A-36. Three gaps remain across all R15
variations not yet addressed:

1. **Charter-rhythm parity gap (A-37):** All R15 variations include CHARTER-COMPLETENESS-AUDIT
   per-field sweeps but none require a bidirectional correspondence check between charters and
   rhythm table governance rows. A charter naming a non-existent rhythm meeting escapes A-35.
   A governance rhythm row with no corresponding charter also escapes A-35. The one-directional
   field audit passes while 1:1 correspondence remains unverified.

2. **Register population gap (A-38):** All R15 variations declare the REGISTER-CATEGORY-CONTRACT
   closed set (A-36) but none require per-category population counts. A declared category with
   zero entries satisfies A-36's closed-set declaration while being silently empty -- the gap is
   invisible without explicit row-level accounting.

3. **Roadmap trigger diversity gap (A-39):** All R15 variations include the Observable Signal
   column required by A-11 but none constrain signal-type homogeneity. A roadmap where all tier
   signals use capacity thresholds satisfies A-11 while providing no discriminative trigger
   coverage. The diversity of trigger types is an implicit quality expectation that the column-
   presence check cannot enforce.

**R16 target:** Close all three v15 gaps. V-01/V-02/V-03 are single-axis. V-04/V-05 combine.

---

## Variation Map

| V  | Axis                                        | Hypothesis                                                                                                                                                      |
|----|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| V-01 | CHARTER-RHYTHM-PARITY: block (A-37 only) | A two-column bidirectional correspondence table between CHARTER-COMPLETENESS-AUDIT and the CHARTERS COMPLETE gate catches charter-rhythm mismatches invisible to the per-field A-35 audit |
| V-02 | REGISTER-POPULATION-AUDIT: block (A-38 only) | A per-category population count block immediately after the register body makes zero-entry declared categories a directly scannable CATEGORY-EMPTY row rather than a silent absence |
| V-03 | ROADMAP-TRIGGER-DIVERSITY: block (A-39 only) | A trigger-type enumeration after the roadmap table with a minimum-two-distinct-types constraint prevents trigger homogeneity that formally satisfies A-11 while providing no discriminative coverage |
| V-04 | A-37 + A-38 combined                       | Charter-rhythm parity and register population audit close both correspondence gaps without introducing the roadmap diversity constraint; tests whether the parity and population blocks compose cleanly |
| V-05 | Full integration: A-37 + A-38 + A-39 on R15-V-05 baseline | All three new blocks layered onto the proven foundation achieves the v15 composite target |

---

## V-01: Charter-Rhythm Parity Verification (A-37 only)

**Axis:** Insert `CHARTER-RHYTHM-PARITY:` block between CHARTER-COMPLETENESS-AUDIT and CHARTERS COMPLETE gate
**Hypothesis:** Bidirectional charter-to-rhythm-row mapping catches mismatches the per-field A-35 audit cannot detect

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role in the format `- [role name] -- [one-line description from role file]`.
DO NOT invent role names unless no roles files are found.
If no files are found, DO produce a `ROLES-NOTE: No .roles/ files found. Using inferred roles:` block instead, with one inferred entry per role in the format `- [role name] -- [description]`.
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
DO NOT proceed to Org Evolution Roadmap until all four category entries are populated:
  `cat-1 (Areas)` -- all area names from the Headcount table, each as `- [area name] -- headcount: [N]`
  `cat-2 (Committees/Cadences)` -- all committee and cadence names from the Rhythm Table and Charters, each as `- [name]`
  `cat-3 (Headcount)` -- total headcount as `- Total headcount: [N]`
  `cat-4 (DRI Roles)` -- all DRI role names from the Operating Rhythm Table, each as `- [DRI role]`

ORG EVOLUTION ROADMAP -- REQUIRED

DO produce a trigger table after the ORG-ELEMENT REGISTER with columns `Trigger | Structural Change | Type | Observable Signal | Probability Weight`.
DO NOT label it optional.
DO include at minimum two rows:
  Row 1: a headcount threshold trigger.
  Row 2: MUST come from a different category -- a workload signal, structural symptom, or milestone event.
DO NOT use two headcount thresholds as the two rows.
DO include a `WATCH-FIRST:` declaration naming the leading indicator to monitor before acting.

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

DO produce this section after the Org Evolution Roadmap with columns `Anti-Pattern | Why It Applies Here | Mitigation`.
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
18. Org Evolution Roadmap
19. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-02: Register Population Audit (A-38 only)

**Axis:** Insert `REGISTER-POPULATION-AUDIT:` block immediately after ORG-ELEMENT REGISTER body
**Hypothesis:** Per-category population counts make zero-entry declared categories a directly scannable CATEGORY-EMPTY row, paralleling the A-34 ROLE-TIER-ACCOUNTING pattern in the register domain

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role in the format `- [role name] -- [one-line description from role file]`.
DO NOT invent role names unless no roles files are found.
If no files are found, DO produce a `ROLES-NOTE: No .roles/ files found. Using inferred roles:` block instead, with one inferred entry per role in the format `- [role name] -- [description]`.
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

When the CHARTER-COMPLETENESS-AUDIT confirms full coverage:
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
A CATEGORY-EMPTY row is a constraint violation -- add the missing entries to the register before proceeding to the Org Evolution Roadmap.
DO NOT proceed to the Org Evolution Roadmap until all declared categories have a CATEGORY-POPULATED verdict.

ORG EVOLUTION ROADMAP -- REQUIRED

DO produce a trigger table after the REGISTER-POPULATION-AUDIT block with columns `Trigger | Structural Change | Type | Observable Signal | Probability Weight`.
DO NOT label it optional.
DO include at minimum two rows:
  Row 1: a headcount threshold trigger.
  Row 2: MUST come from a different category -- a workload signal, structural symptom, or milestone event.
DO NOT use two headcount thresholds as the two rows.
DO include a `WATCH-FIRST:` declaration naming the leading indicator to monitor before acting.

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

DO produce this section after the Org Evolution Roadmap with columns `Anti-Pattern | Why It Applies Here | Mitigation`.
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
14. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
15. REGISTER-CATEGORY-CONTRACT:
16. ORG-ELEMENT REGISTER
17. REGISTER-POPULATION-AUDIT:
18. Org Evolution Roadmap
19. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-03: Roadmap Trigger Diversity Verification (A-39 only)

**Axis:** Insert `ROADMAP-TRIGGER-DIVERSITY:` block after Org Evolution Roadmap and before Anti-Pattern Watch
**Hypothesis:** Explicit trigger-type enumeration with a minimum-two-distinct-types constraint prevents signal-type homogeneity that satisfies A-11 while providing no discriminative trigger coverage

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role in the format `- [role name] -- [one-line description from role file]`.
DO NOT invent role names unless no roles files are found.
If no files are found, DO produce a `ROLES-NOTE: No .roles/ files found. Using inferred roles:` block instead, with one inferred entry per role in the format `- [role name] -- [description]`.
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

When the CHARTER-COMPLETENESS-AUDIT confirms full coverage:
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
DO NOT proceed to Org Evolution Roadmap until all four category entries are populated:
  `cat-1 (Areas)` -- all area names from the Headcount table, each as `- [area name] -- headcount: [N]`
  `cat-2 (Committees/Cadences)` -- all committee and cadence names from the Rhythm Table and Charters, each as `- [name]`
  `cat-3 (Headcount)` -- total headcount as `- Total headcount: [N]`
  `cat-4 (DRI Roles)` -- all DRI role names from the Operating Rhythm Table, each as `- [DRI role]`

ORG EVOLUTION ROADMAP -- REQUIRED

DO produce a trigger table after the ORG-ELEMENT REGISTER with columns `Trigger | Structural Change | Type | Observable Signal | Probability Weight`.
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
14. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
15. REGISTER-CATEGORY-CONTRACT:
16. ORG-ELEMENT REGISTER
17. Org Evolution Roadmap
18. ROADMAP-TRIGGER-DIVERSITY:
19. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-04: Charter-Rhythm Parity + Register Population Audit (A-37 + A-38)

**Axis:** Combine CHARTER-RHYTHM-PARITY: block and REGISTER-POPULATION-AUDIT: block; no roadmap diversity block
**Hypothesis:** Parity and population audit blocks compose cleanly without introducing the roadmap diversity constraint; tests whether the two correspondence gaps close without the third

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role in the format `- [role name] -- [one-line description from role file]`.
DO NOT invent role names unless no roles files are found.
If no files are found, DO produce a `ROLES-NOTE: No .roles/ files found. Using inferred roles:` block instead, with one inferred entry per role in the format `- [role name] -- [description]`.
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

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

DO produce this section after the Org Evolution Roadmap with columns `Anti-Pattern | Why It Applies Here | Mitigation`.
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
20. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-05: Full Integration -- A-37 + A-38 + A-39 on R15-V-05 Baseline

**Axis:** All three new blocks layered onto the proven R15-V-05 foundation
**Hypothesis:** CHARTER-RHYTHM-PARITY, REGISTER-POPULATION-AUDIT, and ROADMAP-TRIGGER-DIVERSITY together achieve the v15 composite target with no regressions against prior criteria

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role in the format `- [role name] -- [one-line description from role file]`.
DO NOT invent role names unless no roles files are found.
If no files are found, DO produce a `ROLES-NOTE: No .roles/ files found. Using inferred roles:` block instead, with one inferred entry per role in the format `- [role name] -- [description]`.
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
19. Org Evolution Roadmap
20. ROADMAP-TRIGGER-DIVERSITY:
21. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`
