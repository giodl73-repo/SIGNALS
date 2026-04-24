---
skill: quest-variate
skill_target: org-chart
date: 2026-03-17
round: R16
rubric_version: v16
status: variate
---

# org-chart Variate -- Round 16

**Date:** 2026-03-17
**Skill:** org-chart
**Rubric:** v16 (C-01 through C-45; C-45 new from R16)
**Round:** R16 -- single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

**R15 ceiling under v15:**
R15 V-01/V-04/V-05 achieve C-45 PASS -- inline enumeration appears as an indented
sub-list under checklist item (b). R15 V-02 earns C-45 FAIL (pointer-reference form).
R15 V-03 earns C-45 FAIL (checkpoint merged with inventory; item (b) becomes redundant).
C-45 is now the benchmark: item (b) must enumerate all four transitions inline, not by
pointer.

Two structural gaps remain not yet captured by any criterion:

1. **Item (b) completeness bypass (possible C-46 target):** C-45 requires inline
   enumeration in item (b) but does not require that the enumeration be complete across
   all four transitions. A model could write item (b) with two or three transitions listed
   inline (e.g., "GATE 0->1: typed role list, GATE 1->2: inertia verdict") and earn a
   C-45 PASS or PARTIAL without enumerating all four gate+artifact pairs. The inline form
   is present; the count constraint is not enforced.

2. **Anti-pointer prohibition bypass (possible C-46 or axis variation target):** C-45 is
   a scoring criterion that rewards inline form -- but the skill body prompt does not yet
   explicitly prohibit the pointer-reference form. A model prompted to run the skill under
   time pressure may revert to pointer form ("as listed above") even when the rubric
   rewards inline form, because nothing in the instructions names the pointer form as
   forbidden.

**Variation axes for R16:**

**Axis A** -- Item (b) inline format shape: how the four transitions are listed inline
  A-form-1 (R15 V-01 baseline): indented sub-list under the `[ ]` checkbox body
    using four lines: `GATE 0->1: typed role list` etc.
  A-form-2 (V-01): numbered 1-through-4 sub-list under item (b), each entry on its own
    line prefixed with its ordinal -- making "4 items" an explicit count obligation
  A-form-3 (V-02): compact single-line semicolon-separated enumeration within the
    checkbox body parenthetical -- maximal compression of the same four pairs

**Axis B** -- Anti-pointer prohibition: whether the checkpoint instruction bans pointer form
  B-form-1 (R15 V-01 baseline): no explicit prohibition of pointer-reference form
  B-form-2 (V-03, V-04, V-05): adds "DO NOT write item (b) in pointer-reference form
    (e.g., 'as listed above' or 'as enumerated in the inventory block')" as a named
    prohibition immediately following item (b)

**Axis C** -- Self-containment instruction: whether item (b) carries an explicit
  self-containment directive
  C-form-1 (R15 V-01 baseline, V-01 through V-04): no self-containment instruction
  C-form-2 (V-05): adds "Item (b) MUST be self-contained -- the four transitions must be
    readable and verifiable at this checkpoint location without cross-referencing any
    prior block"

Single-axis: V-01 (Axis A, form 2), V-02 (Axis A, form 3), V-03 (Axis B, form 2)
Combined:    V-04 (A-form-2 + B-form-2), V-05 (A-form-2 + B-form-2 + C-form-2)

---

## V-01

**Variation axis:** Axis A, form 2 -- numbered 1-through-4 sub-list in item (b)
**Hypothesis:** Making the four transitions a numbered list (1. through 4.) explicitly
encodes a count obligation: the model must produce exactly four numbered entries, and
omitting any transition leaves a gap in the ordinal sequence that is structurally
visible. This is harder to compress than an unordered indented block because skipping
entry 3 breaks the 1-2-4 sequence, making incompleteness detectable without counting.

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

  GATE 0 -> 1      : typed role list
  GATE 1 -> 2      : inertia verdict + FLAT-CASE-PRESSURE
  GATE 2 -> 3      : org diagram
  GATE 3 -> STATUS : charter set

CHECKPOINT-0 -- PRE-EXECUTION PASS CHECKLIST

Before producing any GATE 0 content (ROLES-LOADED or ROLES-NOTE), confirm all three:

  [ ] ARTIFACT-HANDOFF INVENTORY block above has been read
  [ ] All four artifact transitions are known by gate and artifact name:
        1. GATE 0->1: typed role list
        2. GATE 1->2: inertia verdict + FLAT-CASE-PRESSURE
        3. GATE 2->3: org diagram
        4. GATE 3->STATUS: charter set
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
2.  CHECKPOINT-0 PASS CHECKLIST (all three items confirmed; item (b) as numbered
    1-through-4 sub-list inline before proceeding)
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

**Variation axis:** Axis A, form 3 -- compact single-line semicolon-separated enumeration in item (b)
**Hypothesis:** Compressing all four transitions into a single line within the checkbox
parenthetical tests maximum compression tolerance: if the model preserves the semicolon-
separated form under pressure, the inline enumeration is present even in the most
compressed representation. If it collapses to a pointer reference, that failure is
detectable against the baseline A-form-1. This form also reveals whether the model
treats a single-line inline as "counted" -- if it abbreviates mid-sentence, it will
drop artifact names rather than gate boundaries first, which is a different failure
signature than A-form-1 omission.

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

  GATE 0 -> 1      : typed role list
  GATE 1 -> 2      : inertia verdict + FLAT-CASE-PRESSURE
  GATE 2 -> 3      : org diagram
  GATE 3 -> STATUS : charter set

CHECKPOINT-0 -- PRE-EXECUTION PASS CHECKLIST

Before producing any GATE 0 content (ROLES-LOADED or ROLES-NOTE), confirm all three:

  [ ] ARTIFACT-HANDOFF INVENTORY block above has been read
  [ ] All four artifact transitions are known by gate and artifact name
      (GATE 0->1: typed role list; GATE 1->2: inertia verdict + FLAT-CASE-PRESSURE;
       GATE 2->3: org diagram; GATE 3->STATUS: charter set)
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
2.  CHECKPOINT-0 PASS CHECKLIST (all three items confirmed; item (b) as compact
    single-line semicolon-separated enumeration inline in the checkbox body)
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

**Variation axis:** Axis B, form 2 -- explicit anti-pointer prohibition added to CHECKPOINT-0
**Hypothesis:** C-45 is a scoring criterion that rewards inline form, but the skill body
prompt does not yet name the pointer-reference form as forbidden. A model under output
pressure may revert to "as listed above" because nothing in the instructions calls it out
as wrong. Making the prohibition explicit -- naming the banned forms by example -- closes
the reversion path before it is attempted, rather than relying on the rubric to detect
failure post-hoc. This is a B-axis test: same A-form-1 inline enumeration as R15 V-01,
but with an explicit prohibition sentence added below item (b).

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

  GATE 0 -> 1      : typed role list
  GATE 1 -> 2      : inertia verdict + FLAT-CASE-PRESSURE
  GATE 2 -> 3      : org diagram
  GATE 3 -> STATUS : charter set

CHECKPOINT-0 -- PRE-EXECUTION PASS CHECKLIST

Before producing any GATE 0 content (ROLES-LOADED or ROLES-NOTE), confirm all three:

  [ ] ARTIFACT-HANDOFF INVENTORY block above has been read
  [ ] All four artifact transitions are known by gate and artifact name:
        GATE 0->1: typed role list
        GATE 1->2: inertia verdict + FLAT-CASE-PRESSURE
        GATE 2->3: org diagram
        GATE 3->STATUS: charter set
      DO NOT write item (b) in pointer-reference form (e.g., "as listed above" or
        "as enumerated in the inventory block") -- the four transitions MUST be
        restated inline within this checklist item, not deferred to any prior block.
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
2.  CHECKPOINT-0 PASS CHECKLIST (all three items confirmed; item (b) enumerates all four
    transitions inline with explicit anti-pointer prohibition; no pointer-reference form
    permitted)
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

## V-04

**Variation axes:** Axis A, form 2 + Axis B, form 2
**Hypothesis:** Combining the numbered sub-list form (A-form-2) with the anti-pointer
prohibition (B-form-2) creates two independent defenses against C-45 failure:
A-form-2 makes incompleteness visible through ordinal gaps (a model that drops transition
3 breaks the 1-2-4 sequence), while B-form-2 closes the reversion path by naming the
pointer form as explicitly forbidden. Neither defense alone closes all bypass routes --
A-form-2 does not stop a model from reverting to pointer form on compression, and
B-form-2 does not prevent a numbered list from being abbreviated -- but together they
leave fewer unguarded failure modes than either single axis.

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

  GATE 0 -> 1      : typed role list
  GATE 1 -> 2      : inertia verdict + FLAT-CASE-PRESSURE
  GATE 2 -> 3      : org diagram
  GATE 3 -> STATUS : charter set

CHECKPOINT-0 -- PRE-EXECUTION PASS CHECKLIST

Before producing any GATE 0 content (ROLES-LOADED or ROLES-NOTE), confirm all three:

  [ ] ARTIFACT-HANDOFF INVENTORY block above has been read
  [ ] All four artifact transitions are known by gate and artifact name:
        1. GATE 0->1: typed role list
        2. GATE 1->2: inertia verdict + FLAT-CASE-PRESSURE
        3. GATE 2->3: org diagram
        4. GATE 3->STATUS: charter set
      DO NOT write item (b) in pointer-reference form (e.g., "as listed above" or
        "as enumerated in the inventory block") -- the four transitions MUST be
        restated as a numbered list inline within this checklist item.
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
2.  CHECKPOINT-0 PASS CHECKLIST (all three items confirmed; item (b) as numbered
    1-through-4 sub-list inline with explicit anti-pointer prohibition)
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

## V-05

**Variation axes:** Axis A, form 2 + Axis B, form 2 + Axis C, form 2
**Hypothesis:** Adding the self-containment directive (C-form-2) to the A+B combination
closes the third distinct failure path: a model might produce a numbered 1-through-4
list without pointer form, but still write a summary sentence above the list that
references the inventory ("all four transitions from the block above are re-stated here
for confirmation") -- which technically satisfies the anti-pointer prohibition while
softening the self-containment property. C-form-2 makes self-containment an explicit
first-class instruction: the checkpoint location must be independently verifiable, not
just non-pointing. This is the strongest form tested in R16: numbered + non-pointer +
self-contained. It also sets up the next deepening question -- whether the "four
transitions must be readable without cross-referencing any prior block" instruction
closes the summary-sentence softening bypass, or whether a further criterion is needed.

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

  GATE 0 -> 1      : typed role list
  GATE 1 -> 2      : inertia verdict + FLAT-CASE-PRESSURE
  GATE 2 -> 3      : org diagram
  GATE 3 -> STATUS : charter set

CHECKPOINT-0 -- PRE-EXECUTION PASS CHECKLIST

Before producing any GATE 0 content (ROLES-LOADED or ROLES-NOTE), confirm all three:

  [ ] ARTIFACT-HANDOFF INVENTORY block above has been read
  [ ] All four artifact transitions are known by gate and artifact name. Item (b) MUST be
      self-contained -- the four transitions must be readable and verifiable at this
      checkpoint location without cross-referencing any prior block. DO NOT write this
      item in pointer-reference form (e.g., "as listed above" or "as enumerated in the
      inventory block"). The four transitions are:
        1. GATE 0->1: typed role list
        2. GATE 1->2: inertia verdict + FLAT-CASE-PRESSURE
        3. GATE 2->3: org diagram
        4. GATE 3->STATUS: charter set
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
2.  CHECKPOINT-0 PASS CHECKLIST (all three items confirmed; item (b) self-contained with
    numbered 1-through-4 sub-list, anti-pointer prohibition, and self-containment
    directive; verifiable at this location without cross-referencing any prior block)
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
