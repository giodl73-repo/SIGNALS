---
skill: quest-variate
skill_target: org-chart
date: 2026-03-17
round: R17
rubric_version: v17
status: variate
---

# org-chart Variate -- Round 17

**Date:** 2026-03-17
**Skill:** org-chart
**Rubric:** v17 (C-01 through C-46; C-46 new from R17, subsumes C-45)
**Round:** R17 -- single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

**R16 ceiling under v16:**
R16 V-05 achieves C-46 PASS -- numbered 1-through-4 sub-list with anti-pointer prohibition
("DO NOT write item (b) in pointer-reference form") and self-containment directive ("Item (b)
MUST be self-contained -- the four transitions must be readable and verifiable at this
checkpoint location without cross-referencing any prior block"). C-46 is now the standard:
the anti-pointer prohibition with named example forms must be present in item (b).

Three structural gaps remain after R16 V-05 that C-46 does not close:

1. **Count-guard bypass (possible C-47 target):** C-46 requires the four transitions to be
   restated inline but does not require an explicit count verification step within item (b).
   A model could write three entries in the numbered list (1, 2, 3) and omit the fourth,
   satisfying the inline-enumeration form requirement and the anti-pointer prohibition while
   failing completeness. The numbered format makes omission structurally visible (1-2-3 where
   1-2-3-4 is expected) but does not prevent it -- nothing in the spec says "exactly 4 entries
   are required" or "if any entry is missing, this checkpoint fails."

2. **Gate-label format bypass (possible C-47 target):** V-05 item (b) shows the GATE X->Y:
   format by example, but the spec does not require that format when a model re-expresses item
   (b). A model could write "1. typed role list, 2. inertia verdict, 3. org diagram, 4. charter
   set" -- informal names without GATE X->Y: notation -- and satisfy the inline-enumeration
   and anti-pointer requirements while losing the gate-boundary labels that C-25 (named
   artifact handoff at each gate interface) requires. The gate-label format is present in the
   inventory block but not anchored as a format constraint in item (b) itself.

3. **Introductory preamble bypass (possible C-47 target):** V-05's self-containment directive
   ("verifiable at this checkpoint location without cross-referencing any prior block") targets
   pointer-reference forms. But a model could add an introductory preamble sentence before the
   numbered list that references the inventory block without technically pointing to it -- e.g.,
   "The following four gate transitions are restated from the inventory block for confirmation:"
   -- and still produce the numbered list inline. The preamble sentence is not pointer-reference
   form (it is a declarative statement, not a deferral), so the anti-pointer prohibition does
   not fire. But the preamble softens self-containment by anchoring the list to an earlier block.

**Variation axes for R17:**

**Axis A** -- Count guard: whether item (b) carries an explicit count verification statement
  A-form-1 (R16 V-05 baseline): count implied by numbered 1-4 list; no explicit count statement
  A-form-2 (V-01, V-04, V-05): adds explicit count guard immediately after the numbered list:
    "COUNT CHECK: this list must contain exactly 4 entries -- if any GATE transition is missing,
    this checkpoint item FAILS and no PASS declaration is permitted"

**Axis B** -- Gate-label format anchor: whether item (b) requires GATE X->Y: format in output
  B-form-1 (R16 V-05 baseline): GATE X->Y: format present by example; not stated as a required
    format constraint in the item (b) instruction
  B-form-2 (V-02, V-04, V-05): adds explicit format constraint: "each entry MUST use the exact
    format GATE X->Y: [artifact name] -- DO NOT use informal names or paraphrase form in place
    of the canonical artifact name from the ARTIFACT-HANDOFF INVENTORY"

**Axis C** -- Introductory cross-reference prohibition: whether preamble sentences referencing
  the inventory block before the numbered list are explicitly banned
  C-form-1 (R16 V-05 baseline): no prohibition on introductory preamble phrases; self-
    containment directive targets pointer-reference form but not declarative preamble sentences
  C-form-2 (V-03, V-05): adds: "DO NOT write a preamble sentence referencing the inventory
    block before this list (e.g., 'the following transitions are restated from the block above')
    -- item (b) MUST open directly with entry 1"

Single-axis: V-01 (Axis A, form 2), V-02 (Axis B, form 2), V-03 (Axis C, form 2)
Combined:    V-04 (A-form-2 + B-form-2), V-05 (A-form-2 + B-form-2 + C-form-2)

---

## V-01

**Variation axis:** Axis A, form 2 -- explicit count guard in item (b)
**Hypothesis:** The numbered 1-through-4 sub-list implies a count of four but does not
enforce it -- a model under compression pressure could produce entries 1, 2, 3 and stop,
leaving the sequence incomplete without violating any named rule. Adding an explicit COUNT
CHECK statement that declares "exactly 4 entries" and names the failure condition ("this
checkpoint item FAILS") converts the count from an implied structural expectation to an
explicit pass/fail obligation. A model reading the COUNT CHECK statement before populating
the list is forced to carry the count-to-four constraint forward as an active rule, not as
an inference from the numbered format alone.

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
      COUNT CHECK: this list must contain exactly 4 entries -- if any GATE transition is
        missing from the numbered list above, this checkpoint item FAILS and no PASS
        declaration is permitted.
  [ ] No GATE 0 content has been produced before this checkpoint passes

FAIL: If the ARTIFACT-HANDOFF INVENTORY has not been read, STOP. Do not produce GATE 0 content.
PASS: All three items above confirmed and COUNT CHECK satisfied. Proceed to GATE 0.

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
    numbered 1-through-4 sub-list, anti-pointer prohibition, self-containment directive,
    and explicit COUNT CHECK guard requiring exactly 4 entries)
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

**Variation axis:** Axis B, form 2 -- gate-label format anchor in item (b)
**Hypothesis:** R16 V-05 item (b) shows the GATE X->Y: format by example in the numbered
list, but no instruction requires that format -- a model re-expressing item (b) can satisfy
the inline-enumeration and anti-pointer requirements using informal names ("role list",
"inertia result") without GATE X->Y: labels, losing the gate-boundary structure that C-25
(named artifact handoff at each gate interface) requires. Anchoring the format as an explicit
requirement -- naming the template (`GATE X->Y: [artifact name]`) and prohibiting paraphrase
names -- converts the format from a demonstrated-by-example expectation to an enforced
constraint. This tests whether format anchoring as an in-spec instruction changes failure
modes on the gate-label dimension independently of count or preamble bypasses.

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
      inventory block"). Each entry MUST use the exact format `GATE X->Y: [artifact name]`
      -- DO NOT use informal names (e.g., "role list" in place of "typed role list") or
      paraphrase form (e.g., "inertia output") instead of the canonical artifact name from
      the ARTIFACT-HANDOFF INVENTORY. The four transitions are:
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
    numbered 1-through-4 sub-list, anti-pointer prohibition, self-containment directive,
    and gate-label format anchor requiring GATE X->Y: [artifact name] for each entry)
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

**Variation axis:** Axis C, form 2 -- introductory cross-reference prohibition
**Hypothesis:** R16 V-05's self-containment directive ("verifiable at this checkpoint location
without cross-referencing any prior block") targets pointer-reference forms -- "as listed above"
or "as enumerated in the inventory block" -- which defer the content entirely. But a model can
write a declarative preamble sentence before the numbered list that is not technically a
pointer: "The following four gate transitions are restated from the inventory for confirmation:"
-- this names the inventory as the source without pointing to it as the content. The sentence
satisfies "not pointer-reference form" while softening self-containment by establishing a
dependency relationship in the reader's mental model. Explicitly prohibiting preamble sentences
that reference the inventory block before the list ("item (b) MUST open directly with entry 1")
closes this softening path. This is a C-axis-only test against the V-05 baseline.

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
      inventory block"). DO NOT write a preamble sentence referencing the inventory block
      before this list (e.g., "the following transitions are restated from the block above"
      or "as stated in the inventory, the four gate transitions are") -- item (b) MUST open
      directly with entry 1. The four transitions are:
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
    numbered 1-through-4 sub-list, anti-pointer prohibition, self-containment directive,
    and explicit ban on introductory preamble sentences referencing the inventory block;
    item (b) opens directly with entry 1)
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
**Hypothesis:** Combining the count guard (A-form-2) with the gate-label format anchor
(B-form-2) closes two independent failure paths that neither axis closes alone: A-form-2
fails when a model produces fewer than four numbered entries but uses the correct GATE X->Y:
format (count bypass, format correct); B-form-2 fails when a model produces all four entries
using informal names but no explicit count constraint (count correct, format bypass). A model
satisfying both must produce exactly 4 entries in GATE X->Y: [artifact name] format -- the
combination makes both count omission and format paraphrase simultaneously prohibited rather
than independently patched. Neither A nor B alone leaves the other dimension unguarded; their
combination closes both simultaneously.

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
      inventory block"). Each entry MUST use the exact format `GATE X->Y: [artifact name]`
      -- DO NOT use informal names or paraphrase form in place of the canonical artifact
      name from the ARTIFACT-HANDOFF INVENTORY. The four transitions are:
        1. GATE 0->1: typed role list
        2. GATE 1->2: inertia verdict + FLAT-CASE-PRESSURE
        3. GATE 2->3: org diagram
        4. GATE 3->STATUS: charter set
      COUNT CHECK: this list must contain exactly 4 entries -- if any GATE transition is
        missing from the numbered list above, this checkpoint item FAILS and no PASS
        declaration is permitted.
  [ ] No GATE 0 content has been produced before this checkpoint passes

FAIL: If the ARTIFACT-HANDOFF INVENTORY has not been read, STOP. Do not produce GATE 0 content.
PASS: All three items above confirmed and COUNT CHECK satisfied. Proceed to GATE 0.

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
    numbered 1-through-4 sub-list in GATE X->Y: [artifact name] format, anti-pointer
    prohibition, self-containment directive, gate-label format anchor, and COUNT CHECK
    guard requiring exactly 4 entries)
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
**Hypothesis:** The full triple combination -- count guard + gate-label format anchor +
introductory preamble prohibition -- closes three independent bypass paths simultaneously.
A-form-2 closes count omission (fewer than 4 entries in the numbered list). B-form-2 closes
format paraphrase (informal artifact names without GATE X->Y: notation). C-form-2 closes
preamble softening (declarative sentences anchoring the list to a prior block before entry 1).
Each of the three axes targets a distinct failure mode; no single axis closes the other two.
V-05 is the strongest form tested in R17: a model satisfying all three must produce exactly
4 GATE X->Y: [artifact name] entries, starting with entry 1, with no introductory sentence
referencing the inventory block, and with the pointer-reference forms already prohibited by
C-46. This sets up the next deepening question: whether any bypass path remains after all
three guards are active simultaneously.

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
      inventory block"). DO NOT write a preamble sentence referencing the inventory block
      before this list (e.g., "the following transitions are restated from the block above"
      or "as stated in the inventory, the four gate transitions are") -- item (b) MUST open
      directly with entry 1. Each entry MUST use the exact format `GATE X->Y: [artifact
      name]` -- DO NOT use informal names or paraphrase form in place of the canonical
      artifact name from the ARTIFACT-HANDOFF INVENTORY. The four transitions are:
        1. GATE 0->1: typed role list
        2. GATE 1->2: inertia verdict + FLAT-CASE-PRESSURE
        3. GATE 2->3: org diagram
        4. GATE 3->STATUS: charter set
      COUNT CHECK: this list must contain exactly 4 entries -- if any GATE transition is
        missing from the numbered list above, this checkpoint item FAILS and no PASS
        declaration is permitted.
  [ ] No GATE 0 content has been produced before this checkpoint passes

FAIL: If the ARTIFACT-HANDOFF INVENTORY has not been read, STOP. Do not produce GATE 0 content.
PASS: All three items above confirmed and COUNT CHECK satisfied. Proceed to GATE 0.

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
    numbered 1-through-4 sub-list in GATE X->Y: [artifact name] format, anti-pointer
    prohibition, self-containment directive, preamble prohibition opening directly with
    entry 1, gate-label format anchor, and COUNT CHECK guard requiring exactly 4 entries)
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
