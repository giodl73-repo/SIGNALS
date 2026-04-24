---
skill: quest-variate
skill_target: org-chart
date: 2026-03-17
round: R15
rubric_version: v15
status: variate
---

# org-chart Variate -- Round 15

**Date:** 2026-03-17
**Skill:** org-chart
**Rubric:** v15 (C-01 through C-44; C-43/C-44 new from R15)
**Round:** R15 -- single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

**R14 ceiling under v14:**
V-05/R14 achieves the full rubric score aspirationally under v14. Two structural gaps remain
not yet captured by any criterion:

1. **CHECKPOINT-0 enumeration bypass (C-43 target):** C-42 requires a CHECKPOINT-0 with a
   FAIL condition blocking GATE 0 execution, but does not require an affirmative pass checklist.
   A model satisfying C-42 knows what causes failure (INVENTORY not read) but may proceed
   without explicitly confirming all four artifact transitions by gate and artifact name.

2. **Sub-section 1/2 boundary bypass (C-44 target):** C-01 requires mechanism table presence
   but leaves the SS1/SS2 boundary unmarked. The T3 already includes the FLAT-CASE-CLOSED
   sentinel and self-repair; R15 variations explore whether the sentinel and containment guard
   can be made more compression-resistant through zone-label pairing and explicit gate-numbered
   headers.

**Variation axes for R15:**

**Axis A** -- CHECKPOINT-0 form: how the pass checklist is expressed
  A-form-1 (V-01, V-04, V-05): standalone ARTIFACT-HANDOFF INVENTORY block + explicit `[ ]`
    checkbox CHECKPOINT-0 with three named items and FAIL/PASS declarations
  A-form-2 (V-02): ARTIFACT-HANDOFF INVENTORY as a Markdown table + CHECKPOINT-0 as a
    parallel verification table with `[ ]` rows
  A-form-3 (V-03): no separate ARTIFACT-HANDOFF INVENTORY block; inventory is embedded
    inside the CHECKPOINT-0 instruction, the transitions listed as part of the checklist itself

**Axis B** -- C-44 sentinel integration: zone-label pairing for SS1 boundary
  B-form-1 (V-01, V-02, V-03): current T3 form -- FLAT-CASE-CLOSED separator only
  B-form-2 (V-04, V-05): adds `[ZONE: SS1-OPEN]` at the start of Sub-section 1 and
    `[ZONE: SS1-CLOSED]` immediately after the FLAT-CASE-CLOSED separator; both markers
    required before Sub-section 2 may begin

**Axis C** -- gate-numbered section headers: whether GATE-N labels appear on each major section
  C-form-1 (V-01 through V-04): section headers without gate numbers (current T3 style)
  C-form-2 (V-05): section headers carry GATE-N labels matching the ARTIFACT-HANDOFF
    INVENTORY exactly -- GATE 0 (ROLES), GATE 1 (INERTIA ASSESSMENT), GATE 2 (STRUCTURE),
    GATE 3/STATUS (HEADCOUNT + RHYTHM + CHARTERS) -- creating a named correspondence between
    the pre-flight inventory and the execution body

Single-axis: V-01 (Axis A, form 1), V-02 (Axis A, form 2), V-03 (Axis A, form 3)
Combined:    V-04 (A-form-1 + B-form-2), V-05 (A-form-1 + B-form-2 + C-form-2)

---

## V-01

**Variation axis:** Axis A, form 1 -- standalone ARTIFACT-HANDOFF INVENTORY + explicit `[ ]` CHECKPOINT-0
**Hypothesis:** Separating the inventory definition from the pass checklist lets the model
encounter the four transitions as a declared reference block, then confirm them as an
independent checkpoint action -- making the enumeration step structurally distinct from the
mere presence of the inventory.

---

```
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


You are running `/org-chart {topic}`.

ARTIFACT-HANDOFF INVENTORY

Read this block completely before producing any output. This skill gates execution through
four artifact transitions; each gate produces an artifact that the next gate consumes.

  GATE 0 -> 1    : typed role list
  GATE 1 -> 2    : inertia verdict + FLAT-CASE-PRESSURE
  GATE 2 -> 3    : org diagram
  GATE 3 -> STATUS : charter set

CHECKPOINT-0 -- PRE-EXECUTION PASS CHECKLIST

Before producing any GATE 0 content (ROLES-LOADED or ROLES-NOTE), confirm all three:

  [ ] ARTIFACT-HANDOFF INVENTORY block above has been read
  [ ] All four artifact transitions are known by gate and artifact name:
        GATE 0->1: typed role list
        GATE 1->2: inertia verdict + FLAT-CASE-PRESSURE
        GATE 2->3: org diagram
        GATE 3->STATUS: charter set
  [ ] No GATE 0 content has been produced before this checkpoint passes

FAIL: If the ARTIFACT-HANDOFF INVENTORY has not been read, STOP. Do not produce GATE 0 content.
PASS: All three items above confirmed. Proceed to GATE 0.

ROLES -- READ FIRST

DO check `.roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role in the format
  `- [role name] -- [one-line description from role file]`.
DO NOT invent role names unless no roles files are found.
If no files are found, DO produce a
  `ROLES-NOTE: No .roles/ files found. Using inferred roles:` block instead,
  with one inferred entry per role in the format `- [role name] -- [description]`.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER -- THREE-TIER CLASSIFICATION SEQUENCE CONSTRAINT

DO classify roles in this strict three-tier order: `Engineering` types first, then
`Operations` types, then `PM`, `Design`, `Research`, and `Other` types.
If no `Engineering` roles are present, begin with `Operations` types.
If neither `Engineering` nor `Operations` roles are present, classify all roles in any order.
DO NOT interleave tiers -- complete all entries in one tier before writing any entry from
the next tier.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or
ROLES-NOTE, following the ROLE-LOAD-ORDER three-tier constraint above.
DO assign each role exactly one domain type from this closed set:
  `Engineering / PM / Design / Operations / Research / Other`.
DO format each entry as `- [role name] -- [domain type]`.
DO NOT skip this block.
DO NOT proceed until every role from ROLES-LOADED or ROLES-NOTE is classified.
DO annotate each Key Roles cell in the Headcount by Area table in the format
  `[role name] ([domain type])`.
DO annotate each Membership field in Committee Charters in the same format
  `[role name] ([domain type])`.

When all roles are classified, DO emit:
  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
DO NOT proceed to the Inertia Assessment until this gate line is present in the output.

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.
DO NOT write an org diagram as the first section.
DO structure the inertia assessment in this exact four-sub-section order:
  Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

Sub-section 1 -- Case for Staying Flat

DO produce a three-column mechanism evidence table with columns
  `Mechanism Name | Type | Frequency / Participants`.
DO include at minimum two data rows.
The Type column MUST contain only values from this closed vocabulary:
  `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
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
DO reference a specific observable: a blocked decision, missed SLA, time-zone gap,
  knowledge silo, or competing roadmap.
DO NOT write "the team is growing" without specifying the failure mode.

Sub-section 4 -- VERDICT and Re-assessment Trigger

MUST open this sub-section with a pressure rating line in this format:
  `FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing Sub-section 1
  mechanism count and Sub-section 3 failure mode]`.
The rating MUST be exactly one value from this closed set:
  `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
DO NOT omit this line.
DO NOT emit the verdict declaration before this line is present.
After emitting the pressure line, DO choose exactly one of:
  `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
The reasoning sentence MUST reference the FLAT-CASE-PRESSURE rating by name.
DO write a re-assessment trigger immediately after the verdict naming a concrete threshold.
DO NOT write "revisit as the team grows."
DO NOT proceed past the VERDICT until the pressure line, verdict declaration, and
re-assessment trigger are all written.

When VERDICT is written, DO emit:
  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
DO NOT draw any org boxes until this gate line is present in the output.

ASCII ORG DIAGRAM

DO draw an ASCII hierarchy after the inertia assessment phase gate.
DO show at minimum two levels.
DO NOT produce a flat list of names without hierarchy.
DO show committees as distinct labeled nodes, not embedded in one area.
DO use role names from ROLES-LOADED or ROLES-NOTE -- DO NOT introduce new role names.

When the org diagram is complete, DO emit:
  `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
DO NOT begin the Headcount table until this gate line is present in the output.

HEADCOUNT BY AREA -- DECIDES / ESCALATES REQUIRED

DO produce a headcount table with columns
  `Area | Headcount | Key Roles | Decides | Escalates`.
DO NOT use a single `Decision Scope` column -- the Decides and Escalates columns are
  separate and both REQUIRED.
DO NOT write `owns the area` or generic ownership phrases in either column.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward, naming the destination role
  or forum.
DO annotate each Key Roles entry in the format `[role name] ([domain type])` from
  ROLE-TYPE-CLASSIFICATION.
DO include at minimum two area rows with individual counts plus a `**Total**` row
  with the sum.
DO NOT produce only a single total with no area breakdown.

OPERATING RHYTHM TABLE

DO produce a cadence table after the headcount section with columns
  `Cadence | Frequency | DRI / Owner | Purpose`.
DO include at minimum three distinct rows: ROB, a shiproom or gate, and a governance meeting.
DO NOT combine two meetings into one row.
DO NOT produce a rhythm table with only ROB.
DO reference a role from ROLES-LOADED in the `DRI / Owner` column where possible.

COMMITTEE CHARTERS -- FIVE FIELDS REQUIRED

DO write a charter for each governance meeting in the rhythm table.
DO include all five fields: `Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`.
DO NOT label this section optional.
DO NOT write a rhythm table row for a committee and then omit its charter.
DO annotate each Membership role in the format `[role name] ([domain type])` from
  ROLE-TYPE-CLASSIFICATION, listing at minimum two roles.
DO populate the Escalates field with a named destination.
DO NOT write `everything not listed under Decides.`
DO populate the Quorum field using this format:
  `Quorum: [N] of [M] member roles required for binding decisions`,
  where N is the minimum required count and M is the total number of roles listed
  in the Membership field.
DO NOT use the short `Quorum: [N roles required for binding decisions]` form -- the
  full fraction format is required.
DO NOT omit the Quorum field from any charter.

When all charters are written, DO emit:
  `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
DO NOT begin the ORG-ELEMENT REGISTER until this gate line is present in the output.

ORG-ELEMENT REGISTER -- REQUIRED BEFORE ORG EVOLUTION ROADMAP

MUST produce an `ORG-ELEMENT REGISTER` block immediately after the charters phase gate.
DO NOT skip it.
DO NOT proceed to Org Evolution Roadmap until all four category entries are populated:
  `cat-1 (Areas)` -- all area names from the Headcount table, each as
    `- [area name] -- headcount: [N]`
  `cat-2 (Committees/Cadences)` -- all committee and cadence names from the Rhythm
    Table and Charters, each as `- [name]`
  `cat-3 (Headcount)` -- total headcount as `- Total headcount: [N]`
  `cat-4 (DRI Roles)` -- all DRI role names from the Operating Rhythm Table, each as
    `- [DRI role]`

ORG EVOLUTION ROADMAP -- REQUIRED

DO produce a trigger table after the ORG-ELEMENT REGISTER with columns
  `Trigger | Structural Change | Type`.
DO NOT label it optional.
DO include at minimum two rows.
Row 1: a headcount threshold trigger.
Row 2: MUST come from a different category -- a workload signal, structural symptom,
  or milestone event.
DO NOT use two headcount thresholds as the two rows.

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

DO produce this section after the Org Evolution Roadmap with columns
  `Anti-Pattern | Why It Applies Here | Mitigation`.
MUST open each `Why It Applies Here` cell with typed citation syntax in the format
  `[element name] (cat-N) -- [one sentence of specific relevance]`.
DO NOT write a cell that names an element without the `(cat-N)` typed syntax.
DO NOT use a `cat-N` code that does not match the category schema in the
  ORG-ELEMENT REGISTER.
DO include at minimum two anti-pattern rows.

SECTION ORDER

DO produce sections in this exact sequence:
1.  ARTIFACT-HANDOFF INVENTORY
2.  CHECKPOINT-0 PASS CHECKLIST (all three items confirmed before proceeding)
3.  ROLES-LOADED or ROLES-NOTE
4.  ROLE-LOAD-ORDER three-tier constraint applied (Engineering / Operations / remaining types)
5.  ROLE-TYPE-CLASSIFICATION
6.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
7.  Inertia Assessment (Case for Staying Flat [FLAT-CASE-CLOSED separator] / How We
    Coordinate Today / Rebuttal / VERDICT [opens with FLAT-CASE-PRESSURE line])
8.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
9.  ASCII Org Diagram
10. `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
11. Headcount by Area
12. Operating Rhythm Table
13. Committee Charters (Purpose / Membership / Decides / Escalates / Quorum [N of M fraction])
14. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
15. ORG-ELEMENT REGISTER
16. Org Evolution Roadmap
17. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```

---

## V-02

**Variation axis:** Axis A, form 2 -- ARTIFACT-HANDOFF INVENTORY as Markdown table + CHECKPOINT-0 as parallel verification table
**Hypothesis:** Expressing the inventory as a table and the checkpoint as a matching table
creates visual parallelism that makes the enumeration obligation structurally harder to
compress away -- each row in the inventory has a corresponding row in the checkpoint,
so omitting any transition is visually obvious.

---

```
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


You are running `/org-chart {topic}`.

ARTIFACT-HANDOFF INVENTORY

Read the table below completely before producing any output. Each row is a gate transition
this skill must complete. Know each transition by gate boundary and artifact name.

| Gate Transition   | Artifact Produced                   |
|-------------------|-------------------------------------|
| GATE 0 -> 1       | typed role list                     |
| GATE 1 -> 2       | inertia verdict + FLAT-CASE-PRESSURE|
| GATE 2 -> 3       | org diagram                         |
| GATE 3 -> STATUS  | charter set                         |

CHECKPOINT-0 -- TRANSITION VERIFICATION TABLE

Before writing any GATE 0 content (ROLES-LOADED or ROLES-NOTE), confirm each row:

| # | Confirmation Required                                             | Status |
|---|-------------------------------------------------------------------|--------|
| 1 | ARTIFACT-HANDOFF INVENTORY table above has been read             | [ ]    |
| 2 | All four gate->artifact pairs are known by name as listed above  | [ ]    |
| 3 | No GATE 0 content has been produced before this row is reached   | [ ]    |

FAIL: If any row above is unchecked, STOP. Do not produce GATE 0 content.
PASS: All three rows confirmed. Proceed to GATE 0.

ROLES -- READ FIRST

DO check `.roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role in the format
  `- [role name] -- [one-line description from role file]`.
DO NOT invent role names unless no roles files are found.
If no files are found, DO produce a
  `ROLES-NOTE: No .roles/ files found. Using inferred roles:` block instead,
  with one inferred entry per role in the format `- [role name] -- [description]`.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER -- THREE-TIER CLASSIFICATION SEQUENCE CONSTRAINT

DO classify roles in this strict three-tier order: `Engineering` types first, then
`Operations` types, then `PM`, `Design`, `Research`, and `Other` types.
If no `Engineering` roles are present, begin with `Operations` types.
If neither `Engineering` nor `Operations` roles are present, classify all roles in any order.
DO NOT interleave tiers -- complete all entries in one tier before writing any entry from
the next tier.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or
ROLES-NOTE, following the ROLE-LOAD-ORDER three-tier constraint above.
DO assign each role exactly one domain type from this closed set:
  `Engineering / PM / Design / Operations / Research / Other`.
DO format each entry as `- [role name] -- [domain type]`.
DO NOT skip this block.
DO NOT proceed until every role from ROLES-LOADED or ROLES-NOTE is classified.
DO annotate each Key Roles cell in the Headcount by Area table in the format
  `[role name] ([domain type])`.
DO annotate each Membership field in Committee Charters in the same format
  `[role name] ([domain type])`.

When all roles are classified, DO emit:
  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
DO NOT proceed to the Inertia Assessment until this gate line is present in the output.

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.
DO NOT write an org diagram as the first section.
DO structure the inertia assessment in this exact four-sub-section order:
  Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

Sub-section 1 -- Case for Staying Flat

DO produce a three-column mechanism evidence table with columns
  `Mechanism Name | Type | Frequency / Participants`.
DO include at minimum two data rows.
The Type column MUST contain only values from this closed vocabulary:
  `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
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
DO reference a specific observable: a blocked decision, missed SLA, time-zone gap,
  knowledge silo, or competing roadmap.
DO NOT write "the team is growing" without specifying the failure mode.

Sub-section 4 -- VERDICT and Re-assessment Trigger

MUST open this sub-section with a pressure rating line in this format:
  `FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing Sub-section 1
  mechanism count and Sub-section 3 failure mode]`.
The rating MUST be exactly one value from this closed set:
  `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
DO NOT omit this line.
DO NOT emit the verdict declaration before this line is present.
After emitting the pressure line, DO choose exactly one of:
  `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
The reasoning sentence MUST reference the FLAT-CASE-PRESSURE rating by name.
DO write a re-assessment trigger immediately after the verdict naming a concrete threshold.
DO NOT write "revisit as the team grows."
DO NOT proceed past the VERDICT until the pressure line, verdict declaration, and
re-assessment trigger are all written.

When VERDICT is written, DO emit:
  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
DO NOT draw any org boxes until this gate line is present in the output.

ASCII ORG DIAGRAM

DO draw an ASCII hierarchy after the inertia assessment phase gate.
DO show at minimum two levels.
DO NOT produce a flat list of names without hierarchy.
DO show committees as distinct labeled nodes, not embedded in one area.
DO use role names from ROLES-LOADED or ROLES-NOTE -- DO NOT introduce new role names.

When the org diagram is complete, DO emit:
  `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
DO NOT begin the Headcount table until this gate line is present in the output.

HEADCOUNT BY AREA -- DECIDES / ESCALATES REQUIRED

DO produce a headcount table with columns
  `Area | Headcount | Key Roles | Decides | Escalates`.
DO NOT use a single `Decision Scope` column -- the Decides and Escalates columns are
  separate and both REQUIRED.
DO NOT write `owns the area` or generic ownership phrases in either column.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward, naming the destination role
  or forum.
DO annotate each Key Roles entry in the format `[role name] ([domain type])` from
  ROLE-TYPE-CLASSIFICATION.
DO include at minimum two area rows with individual counts plus a `**Total**` row
  with the sum.
DO NOT produce only a single total with no area breakdown.

OPERATING RHYTHM TABLE

DO produce a cadence table after the headcount section with columns
  `Cadence | Frequency | DRI / Owner | Purpose`.
DO include at minimum three distinct rows: ROB, a shiproom or gate, and a governance meeting.
DO NOT combine two meetings into one row.
DO NOT produce a rhythm table with only ROB.
DO reference a role from ROLES-LOADED in the `DRI / Owner` column where possible.

COMMITTEE CHARTERS -- FIVE FIELDS REQUIRED

DO write a charter for each governance meeting in the rhythm table.
DO include all five fields: `Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`.
DO NOT label this section optional.
DO NOT write a rhythm table row for a committee and then omit its charter.
DO annotate each Membership role in the format `[role name] ([domain type])` from
  ROLE-TYPE-CLASSIFICATION, listing at minimum two roles.
DO populate the Escalates field with a named destination.
DO NOT write `everything not listed under Decides.`
DO populate the Quorum field using this format:
  `Quorum: [N] of [M] member roles required for binding decisions`,
  where N is the minimum required count and M is the total number of roles listed
  in the Membership field.
DO NOT use the short `Quorum: [N roles required for binding decisions]` form -- the
  full fraction format is required.
DO NOT omit the Quorum field from any charter.

When all charters are written, DO emit:
  `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
DO NOT begin the ORG-ELEMENT REGISTER until this gate line is present in the output.

ORG-ELEMENT REGISTER -- REQUIRED BEFORE ORG EVOLUTION ROADMAP

MUST produce an `ORG-ELEMENT REGISTER` block immediately after the charters phase gate.
DO NOT skip it.
DO NOT proceed to Org Evolution Roadmap until all four category entries are populated:
  `cat-1 (Areas)` -- all area names from the Headcount table, each as
    `- [area name] -- headcount: [N]`
  `cat-2 (Committees/Cadences)` -- all committee and cadence names from the Rhythm
    Table and Charters, each as `- [name]`
  `cat-3 (Headcount)` -- total headcount as `- Total headcount: [N]`
  `cat-4 (DRI Roles)` -- all DRI role names from the Operating Rhythm Table, each as
    `- [DRI role]`

ORG EVOLUTION ROADMAP -- REQUIRED

DO produce a trigger table after the ORG-ELEMENT REGISTER with columns
  `Trigger | Structural Change | Type`.
DO NOT label it optional.
DO include at minimum two rows.
Row 1: a headcount threshold trigger.
Row 2: MUST come from a different category -- a workload signal, structural symptom,
  or milestone event.
DO NOT use two headcount thresholds as the two rows.

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

DO produce this section after the Org Evolution Roadmap with columns
  `Anti-Pattern | Why It Applies Here | Mitigation`.
MUST open each `Why It Applies Here` cell with typed citation syntax in the format
  `[element name] (cat-N) -- [one sentence of specific relevance]`.
DO NOT write a cell that names an element without the `(cat-N)` typed syntax.
DO NOT use a `cat-N` code that does not match the category schema in the
  ORG-ELEMENT REGISTER.
DO include at minimum two anti-pattern rows.

SECTION ORDER

DO produce sections in this exact sequence:
1.  ARTIFACT-HANDOFF INVENTORY (table form)
2.  CHECKPOINT-0 TRANSITION VERIFICATION TABLE (all three rows confirmed before proceeding)
3.  ROLES-LOADED or ROLES-NOTE
4.  ROLE-LOAD-ORDER three-tier constraint applied (Engineering / Operations / remaining types)
5.  ROLE-TYPE-CLASSIFICATION
6.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
7.  Inertia Assessment (Case for Staying Flat [FLAT-CASE-CLOSED separator] / How We
    Coordinate Today / Rebuttal / VERDICT [opens with FLAT-CASE-PRESSURE line])
8.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
9.  ASCII Org Diagram
10. `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
11. Headcount by Area
12. Operating Rhythm Table
13. Committee Charters (Purpose / Membership / Decides / Escalates / Quorum [N of M fraction])
14. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
15. ORG-ELEMENT REGISTER
16. Org Evolution Roadmap
17. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```

---

## V-03

**Variation axis:** Axis A, form 3 -- no separate ARTIFACT-HANDOFF INVENTORY block; inventory is embedded inside the CHECKPOINT-0 instruction
**Hypothesis:** Merging the inventory definition and the enumeration checkpoint into a single
block removes the possibility of the model reading the inventory but skipping the checkpoint,
or vice versa -- the inventory listing IS the checklist, making the two actions inseparable.

---

```
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


You are running `/org-chart {topic}`.

CHECKPOINT-0 -- READ AND ENUMERATE BEFORE ANY OUTPUT

Before writing any content, confirm all three items below. The four artifact transitions
that define this skill's gate chain are listed here as items to be read and confirmed,
not merely observed:

  [ ] The following four artifact transitions have been read and are known by gate
      boundary and artifact name:
        GATE 0->1   : typed role list
        GATE 1->2   : inertia verdict + FLAT-CASE-PRESSURE
        GATE 2->3   : org diagram
        GATE 3->STATUS : charter set
  [ ] Each transition above is known by its gate number, direction, and artifact name
  [ ] No output has been produced before this checklist is fully confirmed

FAIL: If the four transitions above have not been internalized, STOP. Do not produce
  any GATE 0 content (ROLES-LOADED or ROLES-NOTE).
PASS: All three items confirmed. Proceed to GATE 0 (ROLES section).

ROLES -- READ FIRST

DO check `.roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role in the format
  `- [role name] -- [one-line description from role file]`.
DO NOT invent role names unless no roles files are found.
If no files are found, DO produce a
  `ROLES-NOTE: No .roles/ files found. Using inferred roles:` block instead,
  with one inferred entry per role in the format `- [role name] -- [description]`.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER -- THREE-TIER CLASSIFICATION SEQUENCE CONSTRAINT

DO classify roles in this strict three-tier order: `Engineering` types first, then
`Operations` types, then `PM`, `Design`, `Research`, and `Other` types.
If no `Engineering` roles are present, begin with `Operations` types.
If neither `Engineering` nor `Operations` roles are present, classify all roles in any order.
DO NOT interleave tiers -- complete all entries in one tier before writing any entry from
the next tier.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or
ROLES-NOTE, following the ROLE-LOAD-ORDER three-tier constraint above.
DO assign each role exactly one domain type from this closed set:
  `Engineering / PM / Design / Operations / Research / Other`.
DO format each entry as `- [role name] -- [domain type]`.
DO NOT skip this block.
DO NOT proceed until every role from ROLES-LOADED or ROLES-NOTE is classified.
DO annotate each Key Roles cell in the Headcount by Area table in the format
  `[role name] ([domain type])`.
DO annotate each Membership field in Committee Charters in the same format
  `[role name] ([domain type])`.

When all roles are classified, DO emit:
  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
DO NOT proceed to the Inertia Assessment until this gate line is present in the output.

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.
DO NOT write an org diagram as the first section.
DO structure the inertia assessment in this exact four-sub-section order:
  Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

Sub-section 1 -- Case for Staying Flat

DO produce a three-column mechanism evidence table with columns
  `Mechanism Name | Type | Frequency / Participants`.
DO include at minimum two data rows.
The Type column MUST contain only values from this closed vocabulary:
  `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
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
DO reference a specific observable: a blocked decision, missed SLA, time-zone gap,
  knowledge silo, or competing roadmap.
DO NOT write "the team is growing" without specifying the failure mode.

Sub-section 4 -- VERDICT and Re-assessment Trigger

MUST open this sub-section with a pressure rating line in this format:
  `FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing Sub-section 1
  mechanism count and Sub-section 3 failure mode]`.
The rating MUST be exactly one value from this closed set:
  `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
DO NOT omit this line.
DO NOT emit the verdict declaration before this line is present.
After emitting the pressure line, DO choose exactly one of:
  `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
The reasoning sentence MUST reference the FLAT-CASE-PRESSURE rating by name.
DO write a re-assessment trigger immediately after the verdict naming a concrete threshold.
DO NOT write "revisit as the team grows."
DO NOT proceed past the VERDICT until the pressure line, verdict declaration, and
re-assessment trigger are all written.

When VERDICT is written, DO emit:
  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
DO NOT draw any org boxes until this gate line is present in the output.

ASCII ORG DIAGRAM

DO draw an ASCII hierarchy after the inertia assessment phase gate.
DO show at minimum two levels.
DO NOT produce a flat list of names without hierarchy.
DO show committees as distinct labeled nodes, not embedded in one area.
DO use role names from ROLES-LOADED or ROLES-NOTE -- DO NOT introduce new role names.

When the org diagram is complete, DO emit:
  `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
DO NOT begin the Headcount table until this gate line is present in the output.

HEADCOUNT BY AREA -- DECIDES / ESCALATES REQUIRED

DO produce a headcount table with columns
  `Area | Headcount | Key Roles | Decides | Escalates`.
DO NOT use a single `Decision Scope` column -- the Decides and Escalates columns are
  separate and both REQUIRED.
DO NOT write `owns the area` or generic ownership phrases in either column.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward, naming the destination role
  or forum.
DO annotate each Key Roles entry in the format `[role name] ([domain type])` from
  ROLE-TYPE-CLASSIFICATION.
DO include at minimum two area rows with individual counts plus a `**Total**` row
  with the sum.
DO NOT produce only a single total with no area breakdown.

OPERATING RHYTHM TABLE

DO produce a cadence table after the headcount section with columns
  `Cadence | Frequency | DRI / Owner | Purpose`.
DO include at minimum three distinct rows: ROB, a shiproom or gate, and a governance meeting.
DO NOT combine two meetings into one row.
DO NOT produce a rhythm table with only ROB.
DO reference a role from ROLES-LOADED in the `DRI / Owner` column where possible.

COMMITTEE CHARTERS -- FIVE FIELDS REQUIRED

DO write a charter for each governance meeting in the rhythm table.
DO include all five fields: `Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`.
DO NOT label this section optional.
DO NOT write a rhythm table row for a committee and then omit its charter.
DO annotate each Membership role in the format `[role name] ([domain type])` from
  ROLE-TYPE-CLASSIFICATION, listing at minimum two roles.
DO populate the Escalates field with a named destination.
DO NOT write `everything not listed under Decides.`
DO populate the Quorum field using this format:
  `Quorum: [N] of [M] member roles required for binding decisions`,
  where N is the minimum required count and M is the total number of roles listed
  in the Membership field.
DO NOT use the short `Quorum: [N roles required for binding decisions]` form -- the
  full fraction format is required.
DO NOT omit the Quorum field from any charter.

When all charters are written, DO emit:
  `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
DO NOT begin the ORG-ELEMENT REGISTER until this gate line is present in the output.

ORG-ELEMENT REGISTER -- REQUIRED BEFORE ORG EVOLUTION ROADMAP

MUST produce an `ORG-ELEMENT REGISTER` block immediately after the charters phase gate.
DO NOT skip it.
DO NOT proceed to Org Evolution Roadmap until all four category entries are populated:
  `cat-1 (Areas)` -- all area names from the Headcount table, each as
    `- [area name] -- headcount: [N]`
  `cat-2 (Committees/Cadences)` -- all committee and cadence names from the Rhythm
    Table and Charters, each as `- [name]`
  `cat-3 (Headcount)` -- total headcount as `- Total headcount: [N]`
  `cat-4 (DRI Roles)` -- all DRI role names from the Operating Rhythm Table, each as
    `- [DRI role]`

ORG EVOLUTION ROADMAP -- REQUIRED

DO produce a trigger table after the ORG-ELEMENT REGISTER with columns
  `Trigger | Structural Change | Type`.
DO NOT label it optional.
DO include at minimum two rows.
Row 1: a headcount threshold trigger.
Row 2: MUST come from a different category -- a workload signal, structural symptom,
  or milestone event.
DO NOT use two headcount thresholds as the two rows.

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

DO produce this section after the Org Evolution Roadmap with columns
  `Anti-Pattern | Why It Applies Here | Mitigation`.
MUST open each `Why It Applies Here` cell with typed citation syntax in the format
  `[element name] (cat-N) -- [one sentence of specific relevance]`.
DO NOT write a cell that names an element without the `(cat-N)` typed syntax.
DO NOT use a `cat-N` code that does not match the category schema in the
  ORG-ELEMENT REGISTER.
DO include at minimum two anti-pattern rows.

SECTION ORDER

DO produce sections in this exact sequence:
1.  CHECKPOINT-0 READ AND ENUMERATE (transitions embedded; all three items confirmed before
    proceeding; no separate ARTIFACT-HANDOFF INVENTORY block)
2.  ROLES-LOADED or ROLES-NOTE
3.  ROLE-LOAD-ORDER three-tier constraint applied (Engineering / Operations / remaining types)
4.  ROLE-TYPE-CLASSIFICATION
5.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
6.  Inertia Assessment (Case for Staying Flat [FLAT-CASE-CLOSED separator] / How We
    Coordinate Today / Rebuttal / VERDICT [opens with FLAT-CASE-PRESSURE line])
7.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
8.  ASCII Org Diagram
9.  `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
10. Headcount by Area
11. Operating Rhythm Table
12. Committee Charters (Purpose / Membership / Decides / Escalates / Quorum [N of M fraction])
13. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
14. ORG-ELEMENT REGISTER
15. Org Evolution Roadmap
16. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```

---

## V-04

**Variation axes:** Axis A, form 1 + Axis B, form 2
**Hypothesis:** Combining the explicit `[ ]` CHECKPOINT-0 (V-01) with zone-label pairing for
the C-44 boundary creates two independent compression-resistance mechanisms targeting different
bypass points: CHECKPOINT-0 closes the enumeration bypass before GATE 0, and the
ZONE:SS1-OPEN/SS1-CLOSED pair closes the Sub-section 1/2 boundary bypass by making the zone
transition a named, detectable artifact -- two named sentinels instead of one.

---

```
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


You are running `/org-chart {topic}`.

ARTIFACT-HANDOFF INVENTORY

Read this block completely before producing any output. This skill gates execution through
four artifact transitions; each gate produces an artifact that the next gate consumes.

  GATE 0 -> 1    : typed role list
  GATE 1 -> 2    : inertia verdict + FLAT-CASE-PRESSURE
  GATE 2 -> 3    : org diagram
  GATE 3 -> STATUS : charter set

CHECKPOINT-0 -- PRE-EXECUTION PASS CHECKLIST

Before producing any GATE 0 content (ROLES-LOADED or ROLES-NOTE), confirm all three:

  [ ] ARTIFACT-HANDOFF INVENTORY block above has been read
  [ ] All four artifact transitions are known by gate and artifact name:
        GATE 0->1: typed role list
        GATE 1->2: inertia verdict + FLAT-CASE-PRESSURE
        GATE 2->3: org diagram
        GATE 3->STATUS: charter set
  [ ] No GATE 0 content has been produced before this checkpoint passes

FAIL: If the ARTIFACT-HANDOFF INVENTORY has not been read, STOP. Do not produce GATE 0 content.
PASS: All three items above confirmed. Proceed to GATE 0.

ROLES -- READ FIRST

DO check `.roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role in the format
  `- [role name] -- [one-line description from role file]`.
DO NOT invent role names unless no roles files are found.
If no files are found, DO produce a
  `ROLES-NOTE: No .roles/ files found. Using inferred roles:` block instead,
  with one inferred entry per role in the format `- [role name] -- [description]`.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER -- THREE-TIER CLASSIFICATION SEQUENCE CONSTRAINT

DO classify roles in this strict three-tier order: `Engineering` types first, then
`Operations` types, then `PM`, `Design`, `Research`, and `Other` types.
If no `Engineering` roles are present, begin with `Operations` types.
If neither `Engineering` nor `Operations` roles are present, classify all roles in any order.
DO NOT interleave tiers -- complete all entries in one tier before writing any entry from
the next tier.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or
ROLES-NOTE, following the ROLE-LOAD-ORDER three-tier constraint above.
DO assign each role exactly one domain type from this closed set:
  `Engineering / PM / Design / Operations / Research / Other`.
DO format each entry as `- [role name] -- [domain type]`.
DO NOT skip this block.
DO NOT proceed until every role from ROLES-LOADED or ROLES-NOTE is classified.
DO annotate each Key Roles cell in the Headcount by Area table in the format
  `[role name] ([domain type])`.
DO annotate each Membership field in Committee Charters in the same format
  `[role name] ([domain type])`.

When all roles are classified, DO emit:
  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
DO NOT proceed to the Inertia Assessment until this gate line is present in the output.

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.
DO NOT write an org diagram as the first section.
DO structure the inertia assessment in this exact four-sub-section order:
  Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

Sub-section 1 -- Case for Staying Flat

DO emit `[ZONE: SS1-OPEN]` as the first line of this sub-section, before any table content.
This zone marker signals that mechanism-typed content has begun; DO NOT produce
Sub-section 2 content until the corresponding `[ZONE: SS1-CLOSED]` marker appears.

DO produce a three-column mechanism evidence table with columns
  `Mechanism Name | Type | Frequency / Participants`.
DO include at minimum two data rows.
The Type column MUST contain only values from this closed vocabulary:
  `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
DO NOT use Type values outside this vocabulary.
Each Mechanism Name MUST name a specific, observable coordination mechanism.
DO NOT move mechanism-typed table content into Sub-section 2.

After writing the table, DO count the data rows (header row excluded).
IF count < 2: DO write the missing mechanism row(s) until count reaches 2.
THEN substitute the final row count as N and DO emit the following two lines in order:
  `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
  `[ZONE: SS1-CLOSED]`
DO NOT emit these two lines before count >= 2.
DO NOT begin Sub-section 2 before BOTH FLAT-CASE-CLOSED separator and `[ZONE: SS1-CLOSED]`
  are present in the output.

Sub-section 2 -- How We Coordinate Today

DO inventory the coordination patterns currently in active use.
DO name channels, cadences, informal roles, and artifacts with frequency and participants.
DO NOT re-list entries from the Sub-section 1 table.

Sub-section 3 -- Rebuttal

DO name the coordination failure the flat-team case and current mechanisms cannot answer.
DO reference a specific observable: a blocked decision, missed SLA, time-zone gap,
  knowledge silo, or competing roadmap.
DO NOT write "the team is growing" without specifying the failure mode.

Sub-section 4 -- VERDICT and Re-assessment Trigger

MUST open this sub-section with a pressure rating line in this format:
  `FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing Sub-section 1
  mechanism count and Sub-section 3 failure mode]`.
The rating MUST be exactly one value from this closed set:
  `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
DO NOT omit this line.
DO NOT emit the verdict declaration before this line is present.
After emitting the pressure line, DO choose exactly one of:
  `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
The reasoning sentence MUST reference the FLAT-CASE-PRESSURE rating by name.
DO write a re-assessment trigger immediately after the verdict naming a concrete threshold.
DO NOT write "revisit as the team grows."
DO NOT proceed past the VERDICT until the pressure line, verdict declaration, and
re-assessment trigger are all written.

When VERDICT is written, DO emit:
  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
DO NOT draw any org boxes until this gate line is present in the output.

ASCII ORG DIAGRAM

DO draw an ASCII hierarchy after the inertia assessment phase gate.
DO show at minimum two levels.
DO NOT produce a flat list of names without hierarchy.
DO show committees as distinct labeled nodes, not embedded in one area.
DO use role names from ROLES-LOADED or ROLES-NOTE -- DO NOT introduce new role names.

When the org diagram is complete, DO emit:
  `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
DO NOT begin the Headcount table until this gate line is present in the output.

HEADCOUNT BY AREA -- DECIDES / ESCALATES REQUIRED

DO produce a headcount table with columns
  `Area | Headcount | Key Roles | Decides | Escalates`.
DO NOT use a single `Decision Scope` column -- the Decides and Escalates columns are
  separate and both REQUIRED.
DO NOT write `owns the area` or generic ownership phrases in either column.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward, naming the destination role
  or forum.
DO annotate each Key Roles entry in the format `[role name] ([domain type])` from
  ROLE-TYPE-CLASSIFICATION.
DO include at minimum two area rows with individual counts plus a `**Total**` row
  with the sum.
DO NOT produce only a single total with no area breakdown.

OPERATING RHYTHM TABLE

DO produce a cadence table after the headcount section with columns
  `Cadence | Frequency | DRI / Owner | Purpose`.
DO include at minimum three distinct rows: ROB, a shiproom or gate, and a governance meeting.
DO NOT combine two meetings into one row.
DO NOT produce a rhythm table with only ROB.
DO reference a role from ROLES-LOADED in the `DRI / Owner` column where possible.

COMMITTEE CHARTERS -- FIVE FIELDS REQUIRED

DO write a charter for each governance meeting in the rhythm table.
DO include all five fields: `Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`.
DO NOT label this section optional.
DO NOT write a rhythm table row for a committee and then omit its charter.
DO annotate each Membership role in the format `[role name] ([domain type])` from
  ROLE-TYPE-CLASSIFICATION, listing at minimum two roles.
DO populate the Escalates field with a named destination.
DO NOT write `everything not listed under Decides.`
DO populate the Quorum field using this format:
  `Quorum: [N] of [M] member roles required for binding decisions`,
  where N is the minimum required count and M is the total number of roles listed
  in the Membership field.
DO NOT use the short `Quorum: [N roles required for binding decisions]` form -- the
  full fraction format is required.
DO NOT omit the Quorum field from any charter.

When all charters are written, DO emit:
  `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
DO NOT begin the ORG-ELEMENT REGISTER until this gate line is present in the output.

ORG-ELEMENT REGISTER -- REQUIRED BEFORE ORG EVOLUTION ROADMAP

MUST produce an `ORG-ELEMENT REGISTER` block immediately after the charters phase gate.
DO NOT skip it.
DO NOT proceed to Org Evolution Roadmap until all four category entries are populated:
  `cat-1 (Areas)` -- all area names from the Headcount table, each as
    `- [area name] -- headcount: [N]`
  `cat-2 (Committees/Cadences)` -- all committee and cadence names from the Rhythm
    Table and Charters, each as `- [name]`
  `cat-3 (Headcount)` -- total headcount as `- Total headcount: [N]`
  `cat-4 (DRI Roles)` -- all DRI role names from the Operating Rhythm Table, each as
    `- [DRI role]`

ORG EVOLUTION ROADMAP -- REQUIRED

DO produce a trigger table after the ORG-ELEMENT REGISTER with columns
  `Trigger | Structural Change | Type`.
DO NOT label it optional.
DO include at minimum two rows.
Row 1: a headcount threshold trigger.
Row 2: MUST come from a different category -- a workload signal, structural symptom,
  or milestone event.
DO NOT use two headcount thresholds as the two rows.

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

DO produce this section after the Org Evolution Roadmap with columns
  `Anti-Pattern | Why It Applies Here | Mitigation`.
MUST open each `Why It Applies Here` cell with typed citation syntax in the format
  `[element name] (cat-N) -- [one sentence of specific relevance]`.
DO NOT write a cell that names an element without the `(cat-N)` typed syntax.
DO NOT use a `cat-N` code that does not match the category schema in the
  ORG-ELEMENT REGISTER.
DO include at minimum two anti-pattern rows.

SECTION ORDER

DO produce sections in this exact sequence:
1.  ARTIFACT-HANDOFF INVENTORY
2.  CHECKPOINT-0 PASS CHECKLIST (all three items confirmed before proceeding)
3.  ROLES-LOADED or ROLES-NOTE
4.  ROLE-LOAD-ORDER three-tier constraint applied (Engineering / Operations / remaining types)
5.  ROLE-TYPE-CLASSIFICATION
6.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
7.  Inertia Assessment:
    Sub-section 1 opens with `[ZONE: SS1-OPEN]`, closes with FLAT-CASE-CLOSED separator +
    `[ZONE: SS1-CLOSED]` (both required before Sub-section 2);
    Sub-section 2 (How We Coordinate Today); Sub-section 3 (Rebuttal);
    Sub-section 4 VERDICT (opens with FLAT-CASE-PRESSURE line)
8.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
9.  ASCII Org Diagram
10. `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
11. Headcount by Area
12. Operating Rhythm Table
13. Committee Charters (Purpose / Membership / Decides / Escalates / Quorum [N of M fraction])
14. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
15. ORG-ELEMENT REGISTER
16. Org Evolution Roadmap
17. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```

---

## V-05

**Variation axes:** Axis A, form 1 + Axis B, form 2 + Axis C, form 2
**Hypothesis:** Adding GATE-N labels to every major section header creates a named
correspondence between the ARTIFACT-HANDOFF INVENTORY (which enumerates GATE 0 through
GATE 3->STATUS by number) and the execution body. This makes the gate chain a navigational
structure visible throughout the output -- the model can always see where it is in the
inventory, and any section appearing out of order is immediately identifiable as a gate
violation.

---

```
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


You are running `/org-chart {topic}`.

ARTIFACT-HANDOFF INVENTORY

Read this block completely before producing any output. This skill gates execution through
four artifact transitions; each gate produces an artifact that the next gate consumes.
The GATE labels below match the section headers throughout this prompt exactly.

  GATE 0 -> 1    : typed role list
  GATE 1 -> 2    : inertia verdict + FLAT-CASE-PRESSURE
  GATE 2 -> 3    : org diagram
  GATE 3 -> STATUS : charter set

CHECKPOINT-0 -- PRE-EXECUTION PASS CHECKLIST

Before producing any GATE 0 content, confirm all three:

  [ ] ARTIFACT-HANDOFF INVENTORY block above has been read
  [ ] All four artifact transitions are known by gate and artifact name:
        GATE 0->1: typed role list
        GATE 1->2: inertia verdict + FLAT-CASE-PRESSURE
        GATE 2->3: org diagram
        GATE 3->STATUS: charter set
  [ ] No GATE 0 content has been produced before this checkpoint passes

FAIL: If the ARTIFACT-HANDOFF INVENTORY has not been read, STOP. Do not produce GATE 0 content.
PASS: All three items above confirmed. Proceed to GATE 0.

GATE 0 -- ROLES

DO check `.roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role in the format
  `- [role name] -- [one-line description from role file]`.
DO NOT invent role names unless no roles files are found.
If no files are found, DO produce a
  `ROLES-NOTE: No .roles/ files found. Using inferred roles:` block instead,
  with one inferred entry per role in the format `- [role name] -- [description]`.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER -- THREE-TIER CLASSIFICATION SEQUENCE CONSTRAINT

DO classify roles in this strict three-tier order: `Engineering` types first, then
`Operations` types, then `PM`, `Design`, `Research`, and `Other` types.
If no `Engineering` roles are present, begin with `Operations` types.
If neither `Engineering` nor `Operations` roles are present, classify all roles in any order.
DO NOT interleave tiers -- complete all entries in one tier before writing any entry from
the next tier.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

MUST produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or
ROLES-NOTE, following the ROLE-LOAD-ORDER three-tier constraint above.
DO assign each role exactly one domain type from this closed set:
  `Engineering / PM / Design / Operations / Research / Other`.
DO format each entry as `- [role name] -- [domain type]`.
DO NOT skip this block.
DO NOT proceed until every role from ROLES-LOADED or ROLES-NOTE is classified.
DO annotate each Key Roles cell in the Headcount by Area table in the format
  `[role name] ([domain type])`.
DO annotate each Membership field in Committee Charters in the same format
  `[role name] ([domain type])`.

When all roles are classified, DO emit:
  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
DO NOT proceed to GATE 1 until this gate line is present in the output.

GATE 1 -- INERTIA ASSESSMENT

The GATE 1->2 artifact is: inertia verdict + FLAT-CASE-PRESSURE.
DO write this section before any org boxes.
DO NOT write an org diagram as the first section.
DO structure in this exact four-sub-section order:
  Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

Sub-section 1 -- Case for Staying Flat

DO emit `[ZONE: SS1-OPEN]` as the first line of this sub-section, before any table content.
This zone marker signals that mechanism-typed content has begun; DO NOT produce
Sub-section 2 content until the corresponding `[ZONE: SS1-CLOSED]` marker appears.

DO produce a three-column mechanism evidence table with columns
  `Mechanism Name | Type | Frequency / Participants`.
DO include at minimum two data rows.
The Type column MUST contain only values from this closed vocabulary:
  `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
DO NOT use Type values outside this vocabulary.
Each Mechanism Name MUST name a specific, observable coordination mechanism.
DO NOT move mechanism-typed table content into Sub-section 2.

After writing the table, DO count the data rows (header row excluded).
IF count < 2: DO write the missing mechanism row(s) until count reaches 2.
THEN substitute the final row count as N and DO emit the following two lines in order:
  `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today begins.] ---`
  `[ZONE: SS1-CLOSED]`
DO NOT emit these two lines before count >= 2.
DO NOT begin Sub-section 2 before BOTH FLAT-CASE-CLOSED separator and `[ZONE: SS1-CLOSED]`
  are present in the output.

Sub-section 2 -- How We Coordinate Today

DO inventory the coordination patterns currently in active use.
DO name channels, cadences, informal roles, and artifacts with frequency and participants.
DO NOT re-list entries from the Sub-section 1 table.

Sub-section 3 -- Rebuttal

DO name the coordination failure the flat-team case and current mechanisms cannot answer.
DO reference a specific observable: a blocked decision, missed SLA, time-zone gap,
  knowledge silo, or competing roadmap.
DO NOT write "the team is growing" without specifying the failure mode.

Sub-section 4 -- VERDICT and Re-assessment Trigger

MUST open this sub-section with a pressure rating line in this format:
  `FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing Sub-section 1
  mechanism count and Sub-section 3 failure mode]`.
The rating MUST be exactly one value from this closed set:
  `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`.
DO NOT omit this line.
DO NOT emit the verdict declaration before this line is present.
After emitting the pressure line, DO choose exactly one of:
  `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
The reasoning sentence MUST reference the FLAT-CASE-PRESSURE rating by name.
DO write a re-assessment trigger immediately after the verdict naming a concrete threshold.
DO NOT write "revisit as the team grows."
DO NOT proceed past the VERDICT until the pressure line, verdict declaration, and
re-assessment trigger are all written.

When VERDICT is written, DO emit:
  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
DO NOT proceed to GATE 2 until this gate line is present in the output.

GATE 2 -- ASCII ORG DIAGRAM

The GATE 2->3 artifact is: org diagram.
DO draw an ASCII hierarchy after the inertia assessment phase gate.
DO show at minimum two levels.
DO NOT produce a flat list of names without hierarchy.
DO show committees as distinct labeled nodes, not embedded in one area.
DO use role names from ROLES-LOADED or ROLES-NOTE -- DO NOT introduce new role names.

When the org diagram is complete, DO emit:
  `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
DO NOT proceed to GATE 3 until this gate line is present in the output.

GATE 3 -- STATUS (HEADCOUNT + RHYTHM + CHARTERS)

The GATE 3->STATUS artifact is: charter set.

HEADCOUNT BY AREA -- DECIDES / ESCALATES REQUIRED

DO produce a headcount table with columns
  `Area | Headcount | Key Roles | Decides | Escalates`.
DO NOT use a single `Decision Scope` column -- the Decides and Escalates columns are
  separate and both REQUIRED.
DO NOT write `owns the area` or generic ownership phrases in either column.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward, naming the destination role
  or forum.
DO annotate each Key Roles entry in the format `[role name] ([domain type])` from
  ROLE-TYPE-CLASSIFICATION.
DO include at minimum two area rows with individual counts plus a `**Total**` row
  with the sum.
DO NOT produce only a single total with no area breakdown.

OPERATING RHYTHM TABLE

DO produce a cadence table after the headcount section with columns
  `Cadence | Frequency | DRI / Owner | Purpose`.
DO include at minimum three distinct rows: ROB, a shiproom or gate, and a governance meeting.
DO NOT combine two meetings into one row.
DO NOT produce a rhythm table with only ROB.
DO reference a role from ROLES-LOADED in the `DRI / Owner` column where possible.

COMMITTEE CHARTERS -- FIVE FIELDS REQUIRED

DO write a charter for each governance meeting in the rhythm table.
DO include all five fields: `Purpose`, `Membership`, `Decides`, `Escalates`, `Quorum`.
DO NOT label this section optional.
DO NOT write a rhythm table row for a committee and then omit its charter.
DO annotate each Membership role in the format `[role name] ([domain type])` from
  ROLE-TYPE-CLASSIFICATION, listing at minimum two roles.
DO populate the Escalates field with a named destination.
DO NOT write `everything not listed under Decides.`
DO populate the Quorum field using this format:
  `Quorum: [N] of [M] member roles required for binding decisions`,
  where N is the minimum required count and M is the total number of roles listed
  in the Membership field.
DO NOT use the short `Quorum: [N roles required for binding decisions]` form -- the
  full fraction format is required.
DO NOT omit the Quorum field from any charter.

When all charters are written, DO emit:
  `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
DO NOT begin the ORG-ELEMENT REGISTER until this gate line is present in the output.

ORG-ELEMENT REGISTER -- REQUIRED BEFORE ORG EVOLUTION ROADMAP

MUST produce an `ORG-ELEMENT REGISTER` block immediately after the charters phase gate.
DO NOT skip it.
DO NOT proceed to Org Evolution Roadmap until all four category entries are populated:
  `cat-1 (Areas)` -- all area names from the Headcount table, each as
    `- [area name] -- headcount: [N]`
  `cat-2 (Committees/Cadences)` -- all committee and cadence names from the Rhythm
    Table and Charters, each as `- [name]`
  `cat-3 (Headcount)` -- total headcount as `- Total headcount: [N]`
  `cat-4 (DRI Roles)` -- all DRI role names from the Operating Rhythm Table, each as
    `- [DRI role]`

ORG EVOLUTION ROADMAP -- REQUIRED

DO produce a trigger table after the ORG-ELEMENT REGISTER with columns
  `Trigger | Structural Change | Type`.
DO NOT label it optional.
DO include at minimum two rows.
Row 1: a headcount threshold trigger.
Row 2: MUST come from a different category -- a workload signal, structural symptom,
  or milestone event.
DO NOT use two headcount thresholds as the two rows.

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

DO produce this section after the Org Evolution Roadmap with columns
  `Anti-Pattern | Why It Applies Here | Mitigation`.
MUST open each `Why It Applies Here` cell with typed citation syntax in the format
  `[element name] (cat-N) -- [one sentence of specific relevance]`.
DO NOT write a cell that names an element without the `(cat-N)` typed syntax.
DO NOT use a `cat-N` code that does not match the category schema in the
  ORG-ELEMENT REGISTER.
DO include at minimum two anti-pattern rows.

SECTION ORDER

DO produce sections in this exact sequence:
1.  ARTIFACT-HANDOFF INVENTORY (gate labels match section headers below exactly)
2.  CHECKPOINT-0 PASS CHECKLIST (all three items confirmed before proceeding)
3.  GATE 0 -- ROLES (ROLES-LOADED or ROLES-NOTE)
4.  ROLE-LOAD-ORDER three-tier constraint applied (Engineering / Operations / remaining types)
5.  ROLE-TYPE-CLASSIFICATION
6.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
7.  GATE 1 -- INERTIA ASSESSMENT:
    Sub-section 1 opens with `[ZONE: SS1-OPEN]`, closes with FLAT-CASE-CLOSED separator +
    `[ZONE: SS1-CLOSED]` (both required before Sub-section 2);
    Sub-section 2 (How We Coordinate Today); Sub-section 3 (Rebuttal);
    Sub-section 4 VERDICT (opens with FLAT-CASE-PRESSURE line)
8.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
9.  GATE 2 -- ASCII Org Diagram
10. `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
11. GATE 3 -- STATUS: Headcount by Area
12. Operating Rhythm Table
13. Committee Charters (Purpose / Membership / Decides / Escalates / Quorum [N of M fraction])
14. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
15. ORG-ELEMENT REGISTER
16. Org Evolution Roadmap
17. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```
