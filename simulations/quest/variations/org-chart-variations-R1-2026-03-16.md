Now I have the full T3 runbook. Generating 5 complete variations.

---

# /quest:variate — org-chart — Round 1

**Skill:** `org-chart` — Org structure generation with areas, committees, and operating rhythms.
**Variation method:** 3 single-axis, 2 combined.

---

## V-01 — Axis: Role Sequence (reversed tier order: PM/Design/Research → Operations → Engineering)

**Hypothesis:** Leading with strategy-facing roles (PM, Design, Research) before Engineering surfacing the org from a product-outcomes frame rather than a technical headcount frame — producing committee charters that are more decision-quality-oriented and less staffing-oriented.

```
You are running `/org-chart {topic}`.

ROLES — READ FIRST

DO check `.roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role in the format `- [role name] — [one-line description from role file]`.
DO NOT invent role names unless no roles files are found.
If no files are found, DO produce a `ROLES-NOTE: No .roles/ files found. Using inferred roles:` block instead, with one inferred entry per role in the format `- [role name] — [description]`.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER — THREE-TIER CLASSIFICATION SEQUENCE CONSTRAINT

DO classify roles in this strict three-tier order: `PM`, `Design`, and `Research` types first, then `Operations` types, then `Engineering` and `Other` types.
If no `PM/Design/Research` roles are present, begin with `Operations` types.
If neither group is present, classify all roles in any order.
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
2. ROLE-LOAD-ORDER three-tier constraint applied (PM/Design/Research / Operations / Engineering+Other)
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
```

---

## V-02 — Axis: Output Format (table-based hierarchy replaces ASCII diagram; scoring scale added to Anti-Pattern Watch)

**Hypothesis:** A structured indented-table representation of org structure is more machine-parseable and copy-pasteable than ASCII art, while a severity rating column on Anti-Pattern Watch creates an actionable priority signal rather than a flat list.

```
You are running `/org-chart {topic}`.

ROLES — READ FIRST

DO check `.roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role in the format `- [role name] — [one-line description from role file]`.
DO NOT invent role names unless no roles files are found.
If no files are found, DO produce a `ROLES-NOTE: No .roles/ files found. Using inferred roles:` block instead, with one inferred entry per role in the format `- [role name] — [description]`.
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

DO write the Inertia Assessment before any org structure.
DO NOT write an org structure as the first section.
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

When VERDICT is written, DO emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`; DO NOT draw any org structure until this gate line is present in the output.

ORG HIERARCHY TABLE — REPLACES ASCII DIAGRAM

DO NOT draw an ASCII art diagram. Instead, produce a four-column table with columns `Level | Node Name | Reports To | Node Type`.
DO include at minimum two levels (Level 1 = top of hierarchy, Level 2 = direct reports, Level 3+ = sub-areas if present).
The `Node Type` column MUST use only values from this closed set: `Area / Committee / Role / Forum`.
DO NOT produce a flat list — every non-top-level node MUST name its parent in `Reports To`.
DO show committees as distinct rows with `Node Type = Committee`, not embedded in an area row.
DO use role names from ROLES-LOADED or ROLES-NOTE — DO NOT introduce new names.

When the hierarchy table is complete, DO emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`; DO NOT begin the Headcount table until this gate line is present in the output.

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

ANTI-PATTERN WATCH — TYPED CITATIONS AND SEVERITY RATING REQUIRED

DO produce this section after the Org Evolution Roadmap with columns `Anti-Pattern | Severity | Why It Applies Here | Mitigation`.
The `Severity` column MUST contain exactly one value from this closed set: `Critical / High / Medium / Low`.
MUST open each `Why It Applies Here` cell with typed citation syntax in the format `[element name] (cat-N) — [one sentence of specific relevance]`.
DO NOT write a cell that names an element without the `(cat-N)` typed syntax.
DO NOT use a `cat-N` code that does not match the category schema in the ORG-ELEMENT REGISTER.
DO include at minimum two anti-pattern rows.
DO sort rows by Severity descending (Critical first, Low last).

SECTION ORDER

DO produce sections in this exact sequence:
1. ROLES-LOADED or ROLES-NOTE
2. ROLE-LOAD-ORDER three-tier constraint applied (Engineering / Operations / remaining types)
3. ROLE-TYPE-CLASSIFICATION
4. `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`
5. Inertia Assessment (Case for Staying Flat [row-count separator] / How We Coordinate Today / Rebuttal / VERDICT [opens with FLAT-CASE-PRESSURE line])
6. `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`
7. Org Hierarchy Table
8. `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`
9. Headcount by Area
10. Operating Rhythm Table
11. Committee Charters (Purpose / Membership / Decides / Escalates / Quorum [N of M fraction] per charter)
12. `=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`
13. ORG-ELEMENT REGISTER
14. Org Evolution Roadmap
15. Anti-Pattern Watch (with Severity column)

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} — {date}`
```

---

## V-03 — Axis: Inertia Framing (inertia as a hard blocker with a go/no-go gate before any structure is drawn)

**Hypothesis:** Elevating the inertia verdict to a binary go/no-go gate — and requiring the flat case to be explicitly overruled before a single org box appears — forces the model to genuinely interrogate whether structure is warranted, rather than treating the assessment as a formality before the "real" output.

```
You are running `/org-chart {topic}`.

ROLES — READ FIRST

DO check `.roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role in the format `- [role name] — [one-line description from role file]`.
DO NOT invent role names unless no roles files are found.
If no files are found, DO produce a `ROLES-NOTE: No .roles/ files found. Using inferred roles:` block instead, with one inferred entry per role in the format `- [role name] — [description]`.
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

INERTIA ASSESSMENT — HARD BLOCKER — ALL FIVE SUB-SECTIONS REQUIRED

The Inertia Assessment is a hard blocker. DO NOT write any org structure — no diagram, no headcount table, no charter — until the `GO / NO-GO` declaration in Sub-section 5 is written.
DO NOT write an org diagram as the first section.
DO structure the inertia assessment in this exact five-sub-section order: Case for Staying Flat / Evidence Inventory / Rebuttal / Pressure Rating / GO / NO-GO Declaration.

Sub-section 1 — Case for Staying Flat

Write the strongest possible argument for NOT creating formal structure. Do not straw-man.
DO produce a four-column mechanism evidence table with columns `Mechanism Name | Type | Frequency / Participants | Coordination Load Covered`.
The `Coordination Load Covered` column MUST estimate what percentage of total coordination load this mechanism handles (e.g., "~40%").
DO include at minimum three data rows.
The Type column MUST contain only values from this closed vocabulary: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
DO NOT use Type values outside this vocabulary.
Each Mechanism Name MUST name a specific, observable coordination mechanism.

After writing the table, DO count the data rows (header row excluded).
IF count < 3: DO write the missing mechanism row(s) until count reaches 3.
THEN substitute the final row count as N and DO emit exactly: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. Evidence Inventory begins.] ---`
DO NOT emit this separator before count >= 3.
DO NOT begin Sub-section 2 before this separator is present in the output.

Sub-section 2 — Evidence Inventory

DO inventory all coordination patterns currently in active use, beyond what the table above captured.
DO name channels, cadences, informal roles, and artifacts with frequency and participants.
DO NOT re-list entries from the Sub-section 1 table.
At the end of this sub-section, DO write a single line in this format: `COVERAGE-ESTIMATE: Existing mechanisms cover approximately [N]% of coordination load without formal structure.`

Sub-section 3 — Rebuttal

DO name the coordination failure(s) that existing mechanisms cannot answer.
DO reference at minimum two specific observables: blocked decisions, missed SLAs, time-zone gaps, knowledge silos, or competing roadmaps.
DO NOT write "the team is growing" without specifying which failure mode growth produces.
At the end of this sub-section, DO write: `FAILURE-MODES-IDENTIFIED: [N]` where N is the count of distinct failure modes named above.

Sub-section 4 — Pressure Rating

MUST open with: `FLAT-CASE-PRESSURE: [rating] — [one-sentence justification citing Sub-section 1 mechanism count, Sub-section 2 COVERAGE-ESTIMATE, and Sub-section 3 FAILURE-MODES count]`.
The rating MUST be exactly one value from this closed set: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
DO NOT omit this line.

Sub-section 5 — GO / NO-GO Declaration

MUST open with exactly one of these two lines:
  `GO: STRUCTURE-WARRANTED — FLAT-CASE-PRESSURE is [rating]; failure modes outweigh coordination coverage. Proceeding to org structure.`
  `NO-GO: CAN-OPERATE-FLAT — FLAT-CASE-PRESSURE is [rating]; existing mechanisms are sufficient. Recommend re-assessment when: [concrete threshold].`

If NO-GO is declared: DO NOT produce any further sections. Output ends at the NO-GO declaration.
If GO is declared: DO write a re-assessment trigger naming a concrete threshold, then proceed.

DO NOT proceed past this declaration until it is written.

When GO is declared, DO emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`; DO NOT draw any org boxes until this gate line is present in the output.

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
5. Inertia Assessment (Case for Staying Flat [row-count separator] / Evidence Inventory [COVERAGE-ESTIMATE] / Rebuttal [FAILURE-MODES-IDENTIFIED] / Pressure Rating / GO / NO-GO Declaration)
6. `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===` (only if GO)
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
```

---

## V-04 — Axes: Phrasing Register (conversational/descriptive) + Lifecycle Emphasis (lighter inertia, heavier charters)

**Hypothesis:** Replacing the imperative DO/DO NOT constraint language with descriptive guidance shifts the model from compliance-mode to reasoning-mode, producing richer charter content and more nuanced escalation paths — at the cost of some structural reliability. Worth measuring whether the tradeoff is real.

```
You are running `/org-chart {topic}`.

Start by loading the role context for this topic.

---

### Step 1 — Load Roles

Look for role definitions in `.roles/`. If you find role files there, list every role you found in a `ROLES-LOADED:` block, one per line, formatted as `- [role name] — [one-line description from the role file]`.

If no role files exist, list the roles you'll work with in a `ROLES-NOTE:` block, noting that these are inferred, using the same format.

Don't write anything else until this block is done.

---

### Step 2 — Classify Roles

After the roles block, add a `ROLE-TYPE-CLASSIFICATION:` block. Assign each role a domain type from this set: Engineering, PM, Design, Operations, Research, or Other. Format as `- [role name] — [domain type]`.

Work through the roles in tier order: Engineering roles first, then Operations, then the rest (PM, Design, Research, Other). Don't mix tiers.

You'll use these domain types as annotations throughout the document — every role name that appears in a Key Roles cell or a Membership field gets `([domain type])` appended.

Once every role is classified, mark the transition:

`=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`

---

### Step 3 — Inertia Check

Before drawing any org structure, take a moment to ask: does this topic actually need formal structure, or can coordination continue working informally?

**Case for Staying Flat**

Build the strongest honest case for not introducing formal structure. Identify the specific mechanisms — channels, cadences, informal roles, artifacts — that are already keeping coordination working. Capture them in a table:

| Mechanism Name | Type | Frequency / Participants |

Types allowed: Channel, Informal Role, Recurring Cadence, Shared Artifact. Use at least two rows.

After you've finished the table (minimum two rows), emit:
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`

**How We Coordinate Today**

Beyond the table above, describe the broader coordination landscape — what else keeps alignment without org structure? Name specific channels, rituals, roles, documents, and how often they run.

**Rebuttal**

Now make the case that the flat approach is breaking down. Point to something observable: a decision that got stuck, a handoff that missed its SLA, a knowledge silo that nobody can see across, a timezone gap that's slowing a team. Be specific — "the team is growing" is not a failure mode.

**Verdict**

Open with the pressure line:
`FLAT-CASE-PRESSURE: [rating] — [one-sentence reason citing the mechanisms found above and the failure you identified]`

Choose a rating from: Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1).

Then declare: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Reference the FLAT-CASE-PRESSURE rating by name in your reasoning.

Follow immediately with a re-assessment trigger — a concrete, named threshold (not "revisit as the team grows").

Once the verdict, pressure line, and trigger are all written:

`=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`

---

### Step 4 — Org Diagram

Draw the org hierarchy as ASCII art. Show at least two levels. Committees are separate labeled nodes, not embedded in an area box. Use only role names from the ROLES-LOADED or ROLES-NOTE block.

`=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`

---

### Step 5 — Headcount by Area

Produce a table:

| Area | Headcount | Key Roles | Decides | Escalates |

- Key Roles: annotate as `[role name] ([domain type])`
- Decides: specific decision types owned here
- Escalates: specific decision types referred upward, with named destination
- Don't use generic phrases like "owns the area" in either column
- At least two area rows, plus a **Total** row with the headcount sum

---

### Step 6 — Operating Rhythm

Show the meeting cadence:

| Cadence | Frequency | DRI / Owner | Purpose |

Include at least three rows covering: a ROB, a shiproom or gate review, and a governance meeting. Each meeting gets its own row. Reference a role from ROLES-LOADED in the DRI/Owner column where possible.

---

### Step 7 — Committee Charters

For every governance meeting in the rhythm table, write a full charter. Each charter needs all five fields:

**Purpose** — what this body exists to resolve
**Membership** — all member roles, annotated as `[role name] ([domain type])`, minimum two roles listed
**Decides** — the specific decision types this body has authority over
**Escalates** — what it refers upward and to whom (name the destination)
**Quorum** — written as `Quorum: [N] of [M] member roles required for binding decisions`

Don't leave any rhythm-table meeting without a charter. Don't leave any field blank. Don't write "everything not in Decides" for Escalates — name the actual escalation paths.

Charters are the most important governance artifact in this document. Invest the most depth here.

`=== [PHASE GATE: CHARTERS COMPLETE — REGISTER AND ANALYSIS BEGIN] ===`

---

### Step 8 — Org-Element Register

List every named element from the document in this four-category register:

```
ORG-ELEMENT REGISTER
cat-1 (Areas): [one entry per area from the headcount table, format: - [name] — headcount: [N]]
cat-2 (Committees/Cadences): [one entry per cadence/committee from the rhythm table and charters]
cat-3 (Headcount): [- Total headcount: [N]]
cat-4 (DRI Roles): [one entry per DRI from the rhythm table]
```

Don't proceed until all four categories are complete.

---

### Step 9 — Org Evolution Roadmap

When should this structure change? Produce a trigger table:

| Trigger | Structural Change | Type |

Row 1: a headcount threshold that would warrant restructuring.
Row 2: a different kind of signal — a workload pattern, a structural symptom, a milestone event.
Don't use two headcount thresholds.

---

### Step 10 — Anti-Pattern Watch

What structural risks should this org watch for? Produce:

| Anti-Pattern | Why It Applies Here | Mitigation |

For each row, open the "Why It Applies Here" cell with a typed element citation: `[element name] (cat-N) — [one sentence]`. Match the cat-N code to the register above. At least two rows.

---

End with exactly: `Generated by: /org-chart {topic} — {date}`
```

---

## V-05 — Axes: Role Sequence (Operations-first) + Output Format (prose hierarchy, no ASCII) + Inertia Framing (dominant first section, explicit GO before structure)

**Hypothesis:** Combining an Operations-first role ordering with a narrative (prose) hierarchy and a hard inertia gate produces an output that reads as an operational brief rather than an engineering org chart — more suitable for use in a shiproom or ROB context, where operations and cadence clarity matter more than reporting-line visualization.

```
You are running `/org-chart {topic}`.

ROLES — READ FIRST

DO check `.roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role in the format `- [role name] — [one-line description from role file]`.
DO NOT invent role names unless no roles files are found.
If no files are found, DO produce a `ROLES-NOTE: No .roles/ files found. Using inferred roles:` block instead, with one inferred entry per role in the format `- [role name] — [description]`.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER — THREE-TIER CLASSIFICATION SEQUENCE CONSTRAINT

DO classify roles in this strict three-tier order: `Operations` types first, then `Engineering` types, then `PM`, `Design`, `Research`, and `Other` types.
If no `Operations` roles are present, begin with `Engineering` types.
If neither `Operations` nor `Engineering` roles are present, classify all roles in any order.
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

INERTIA ASSESSMENT — HARD GATE — FIVE SUB-SECTIONS

The inertia assessment is the primary section of this document. DO NOT produce any org structure until the GO declaration in Sub-section 5 is written.

DO structure the inertia assessment in this exact five-sub-section order: Case for Staying Flat / How We Coordinate Today / Rebuttal / Pressure Rating / GO Declaration.

Sub-section 1 — Case for Staying Flat

DO produce a four-column mechanism evidence table with columns `Mechanism Name | Type | Frequency / Participants | Coordination Load Covered`.
The `Coordination Load Covered` column MUST estimate the percentage of coordination load this mechanism handles (e.g., "~35%").
DO include at minimum three data rows.
The Type column MUST contain only values from this closed vocabulary: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
DO NOT use Type values outside this vocabulary.
Each Mechanism Name MUST name a specific, observable coordination mechanism.

After writing the table, DO count the data rows (header row excluded).
IF count < 3: DO write the missing mechanism row(s) until count reaches 3.
THEN substitute the final row count as N and DO emit exactly: `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
DO NOT emit this separator before count >= 3.
DO NOT begin Sub-section 2 before this separator is present in the output.

Sub-section 2 — How We Coordinate Today

DO inventory the coordination patterns currently in active use beyond what the table captured.
DO name channels, cadences, informal roles, and artifacts with frequency and participants.
DO NOT re-list entries from the Sub-section 1 table.
At the end of this sub-section, DO write: `COVERAGE-ESTIMATE: Existing mechanisms cover approximately [N]% of coordination load without formal structure.`

Sub-section 3 — Rebuttal

DO name the coordination failures that existing mechanisms cannot answer.
DO reference at minimum two specific observables: blocked decisions, missed SLAs, time-zone gaps, knowledge silos, or competing roadmaps.
DO NOT write "the team is growing" without specifying the failure mode growth produces.
At the end, DO write: `FAILURE-MODES-IDENTIFIED: [N]` where N is the count of distinct failure modes named.

Sub-section 4 — Pressure Rating

MUST open with: `FLAT-CASE-PRESSURE: [rating] — [one-sentence justification citing Sub-section 1 mechanism count, Sub-section 2 COVERAGE-ESTIMATE, and Sub-section 3 FAILURE-MODES count]`.
The rating MUST be exactly one value from this closed set: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
DO NOT omit this line.

Sub-section 5 — GO Declaration

MUST write exactly: `GO: STRUCTURE-WARRANTED — FLAT-CASE-PRESSURE is [rating]; failure modes identified ([N]) outweigh coordination coverage ([N]%). Proceeding to org structure.`
DO write a re-assessment trigger naming a concrete threshold.
DO NOT proceed past this line until it is written.

When GO is declared, DO emit: `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`; DO NOT write any org structure until this gate line is present in the output.

ORG NARRATIVE — PROSE HIERARCHY REPLACES ASCII DIAGRAM

DO NOT draw an ASCII art diagram.
Instead, describe the org structure as a nested prose outline using Markdown heading levels:

- `###` for top-level areas (Level 1)
- `####` for sub-areas or teams within an area (Level 2)
- `#####` for sub-teams if needed (Level 3)

For each node, write one or two sentences: what this area owns, who leads it (referencing a role from ROLES-LOADED), and how it interfaces with adjacent areas.

DO show committees as separate `###` sections with the label `[COMMITTEE]` in the heading.
DO NOT produce a flat list of names without nesting.
DO use role names from ROLES-LOADED or ROLES-NOTE — DO NOT introduce new names.

When the narrative is complete, DO emit: `=== [PHASE GATE: STRUCTURE COMPLETE — HEADCOUNT AND RHYTHM BEGIN] ===`; DO NOT begin the Headcount table until this gate line is present in the output.

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
2. ROLE-LOAD-ORDER three-tier constraint applied (Operations / Engineering / remaining types)
3. ROLE-TYPE-CLASSIFICATION
4. `=== [PHASE GATE: ROLES COMPLETE — INERTIA ASSESSMENT BEGINS] ===`
5. Inertia Assessment (Case for Staying Flat [3-row minimum, row-count separator] / How We Coordinate Today [COVERAGE-ESTIMATE] / Rebuttal [FAILURE-MODES-IDENTIFIED] / Pressure Rating / GO Declaration)
6. `=== [PHASE GATE: INERTIA COMPLETE — STRUCTURE SECTION BEGINS] ===`
7. Org Narrative (prose hierarchy with Markdown headings)
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
```

---

## Variation Summary

| ID | Primary Axis | Secondary Axes | Key Structural Difference |
|----|-------------|----------------|--------------------------|
| V-01 | Role sequence | — | PM/Design/Research tier first; org framed from product-outcomes perspective |
| V-02 | Output format | — | Hierarchy table replaces ASCII; Severity column added to Anti-Pattern Watch |
| V-03 | Inertia framing | — | Hard NO-GO path terminates early; 5-sub-section inertia with COVERAGE-ESTIMATE and FAILURE-MODES count |
| V-04 | Phrasing register | Lifecycle emphasis | Conversational imperative replaced by descriptive guidance; charters section flagged as highest-investment |
| V-05 | Role sequence + Output format + Inertia framing | — | Operations-first ordering; prose narrative hierarchy; hard GO gate with coverage vs failure-mode math |
