---
skill: quest-variate
skill_target: org-chart
date: 2026-03-17
round: R19
rubric_version: v19
status: variate
---

# org-chart Variate -- Round 19

**Date:** 2026-03-17
**Skill:** org-chart
**Rubric:** v19 (C-01 through C-51; C-50/C-51 new from v19)
**Round:** R19 -- single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

## R18 ceiling and R19 target

R18 V-05 achieves maximum composite score against rubric v18. Against rubric v19 (which adds
C-50/C-51), two structural gaps remain:

1. **C-50 gap (STEELMAN FIRST anti-form):** R18 V-05 uses "FOUR SUB-SECTIONS, STEELMAN FIRST"
   as the INERTIA ASSESSMENT header. STEELMAN FIRST is a structural-ordering device -- it
   positions the flat case's strongest arguments first as a rhetorical presentation choice.
   C-09 requires outcome-based rationale (referencing coordination costs, team scale, or
   delivery evidence) and prohibits asserting flat as a general principle -- but does not
   name structural-ordering devices as a prohibited form. A model using STEELMAN FIRST satisfies
   C-09's "not a general principle" requirement while providing no observable indicator. C-50
   closes this bypass by naming STEELMAN FIRST as the example anti-form and requiring the
   rationale to cite at least one observable indicator from the closed set.

2. **C-51 gap (CHECKPOINT-INERTIA PASS CHECKLIST absent):** R18 V-05 carries CHECKPOINT-INERTIA
   as inline IF/THEN conditions (satisfying C-41's FAIL-condition requirement), but has no
   affirmative PASS CHECKLIST. The C-42->C-43 pattern converted CHECKPOINT-0 from FAIL-condition
   to affirmative PASS CHECKLIST with three checkbox items. C-51 applies the same pattern to
   CHECKPOINT-INERTIA: adds a three-item PASS CHECKLIST -- (a) frame-close confirmation,
   (b) COUNT CHECK mechanism rows >= 2 with named FAIL, (c) FLAT-CASE-CLOSED sentinel
   confirmation -- converting CHECKPOINT-INERTIA from absence-of-failure gate to positive
   structural confirmation before GATE 1 STATUS emits.

**R19 target:** Close C-50 (observable-indicator rationale, STEELMAN FIRST prohibition), close
C-51 (CHECKPOINT-INERTIA PASS CHECKLIST). V-01/V-02/V-03 single-axis. V-04 combines V-01+V-02.
V-05 integrates all three on R18 V-05 baseline.

---

## Variation Map

| V    | Axis                                                                 | Hypothesis |
|------|----------------------------------------------------------------------|------------|
| V-01 | Observable-indicator rationale + STEELMAN FIRST prohibition (C-50, inertia framing) | R18 V-05 names STEELMAN FIRST without prohibiting it; a named prohibition with observable-indicator requirement closes the structural-ordering bypass in C-09 without affecting CHECKPOINT-INERTIA -- tests whether rationale grounding changes FLAT-CASE-PRESSURE specificity independently of checkpoint structure |
| V-02 | CHECKPOINT-INERTIA affirmative PASS CHECKLIST (C-51, lifecycle emphasis) | R18 V-05 CHECKPOINT-INERTIA is FAIL-condition-only (inline IF/THEN); adding a three-item PASS CHECKLIST mirrors the C-42->C-43 pattern -- converts gate from absence-of-failure to positive structural confirmation, tests whether checklist form changes gate enforcement without rationale changes |
| V-03 | Named RATIONALE-FORM-CONTRACT block (C-50 hardening, phrasing register) | V-01 adds an inline prohibition; V-03 elevates the same contract to a standalone named block -- parallel to how VIOLATION-LABEL-CONTRACT (C-44) is a named block rather than inline instructions; tests whether named-block form is the maximally scannable version of the C-50 constraint |
| V-04 | C-50 inline prohibition + C-51 PASS CHECKLIST (V-01 + V-02) | The two R19 axes address independent dimensions: C-50 governs rationale form, C-51 governs checkpoint structure; neither subsumes the other; tests A+B combined without the V-03 named-block hardening |
| V-05 | Full integration: V-01 + V-02 + V-03 on R18 V-05 baseline | RATIONALE-FORM-CONTRACT named block + observable-indicator prohibition + CHECKPOINT-INERTIA PASS CHECKLIST all active simultaneously; six-layer Sub-section 1 structure: declare cost frame -> cite observable indicator from contract -> write mechanism table -> run count check -> emit sentinel -> run CHECKPOINT-INERTIA pass checklist before gate |

---

## V-01

**Variation axis:** Axis A -- observable-indicator rationale + STEELMAN FIRST prohibition (C-50, inertia framing)
**Hypothesis:** R18 V-05's "FOUR SUB-SECTIONS, STEELMAN FIRST" header names STEELMAN FIRST as
a structural-ordering device without prohibiting it. A model reading this header uses STEELMAN
FIRST as a presentation instruction -- "lead with the flat case's strongest arguments" -- which
satisfies C-09's "not a general principle" requirement (the flat default is not asserted as
abstract doctrine) but provides no observable indicator from the team's coordination reality.
Replacing the header with "FOUR SUB-SECTIONS -- INERTIA-FIRST EVALUATION" and adding an explicit
named prohibition ("DO NOT use structural-ordering devices such as STEELMAN FIRST as a rationale
substitute") paired with a closed-set observable-indicator requirement converts the rationale from
presentation-order grounding to evidence grounding. This tests whether the rationale form changes
FLAT-CASE-PRESSURE specificity independently of checkpoint structure changes.

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
      name]` -- DO NOT use informal names (e.g., "role list" in place of "typed role list")
      or paraphrase form (e.g., "inertia output") instead of the canonical artifact name
      from the ARTIFACT-HANDOFF INVENTORY. The four transitions are:
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

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role in the format
  `- [role name] -- [one-line description from role file]`.
DO NOT invent role names unless no roles files are found.
If no files are found, DO produce a
  `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` block instead,
  with one inferred entry per role in the format `- [role name] -- [description]`.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER -- THREE-TIER CLASSIFICATION SEQUENCE CONSTRAINT

DO classify roles in this strict three-tier order: `Engineering` types first, then
`Operations` types, then `PM`, `Design`, `Research`, and `Other` types.
If no `Engineering` roles are present, begin with `Operations` types.
If neither `Engineering` nor `Operations` roles are present, classify all roles in any order.
DO NOT interleave tiers -- complete all entries in one tier before writing any entry from
the next tier.
IF any tier-N entry appears before all tier-(N-1) entries are written, the
  ROLE-TYPE-CLASSIFICATION block is invalid -- re-emit the full classification in strict
  tier order before proceeding to GATE 0 STATUS.

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

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS -- INERTIA-FIRST EVALUATION

DO write the Inertia Assessment before any org boxes.
DO NOT write an org diagram as the first section.
DO structure the inertia assessment in this exact four-sub-section order:
  Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

The flat-case default position MUST be grounded in at least one observable indicator from
this closed set before the mechanism evidence table begins:
  - coordination costs observable: committee formation load, governance cadence hours,
    role-specialization coordination tax observable in the team's current operating state
  - team scale observable: current headcount, geographic distribution, synchronous overlap
    window that currently covers all necessary coordination without dedicated structure
  - delivery evidence observable: shipped milestone record, SLA met rate, decision latency
    record that demonstrates flat operation is sufficient at current scale
DO NOT use structural-ordering devices as a substitute for this rationale. STEELMAN FIRST
  is a structural-ordering device -- it positions the flat case's strongest arguments first
  as a rhetorical presentation choice, not as a citation of an observable indicator.
  A rationale that leads with the flat case's most favorable arguments without citing any
  observable indicator from the closed set above does not satisfy this requirement.
DO cite the chosen observable indicator explicitly before the STRUCTURING-COST FRAME block.

Sub-section 1 -- Case for Staying Flat

Before writing the mechanism table, produce a STRUCTURING-COST FRAME block that names
the two cost categories to weigh:

  STRUCTURING-COST FRAME:
  - Over-structuring overhead: committee formation load, governance cadence cost
    (meeting hours/quarter), role-specialization coordination tax
  - Under-coordination risk: decision latency, missed SLA exposure, knowledge silo
    formation, competing roadmap without arbitration owner

These two categories are the evaluative lens for every mechanism row below.
DO NOT begin the mechanism table before this block is present.

DO produce a three-column mechanism evidence table with columns
  `Mechanism Name | Type | Frequency / Participants`.
DO include at minimum two data rows.
The Type column MUST contain only values from this closed vocabulary:
  `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
DO NOT use Type values outside this vocabulary.
Each Mechanism Name MUST name a specific, observable coordination mechanism.
DO NOT move mechanism-typed table content into Sub-section 2.
IF any mechanism row is written in Sub-section 2 instead of Sub-section 1, the
  FLAT-CASE-CLOSED count is understated -- move all mechanism-typed rows to Sub-section 1
  and recount before emitting the FLAT-CASE-CLOSED sentinel.

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

Before writing any headcount row, produce a GATE-CONDITION-MET block confirming receipt
of the org diagram artifact from GATE 2->3:

  GATE-CONDITION-MET:
    SOURCE-GATE: === [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===
    GATE-VERDICT: authorized to proceed -- org diagram artifact received from GATE 2->3
    ARRIVAL-COUNTERPART: Headcount by Area section

DO NOT write any headcount row before this block is present.
DO NOT omit the SOURCE-GATE field -- it must quote the exact gate line text from the
  departure site, not a paraphrase.

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
IF any charter is missing the Quorum field, that charter is incomplete -- add the
  Quorum field in `N of M member roles` fraction form before emitting CHARTERS COMPLETE.

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
    prohibition, preamble-sentence prohibition, and COUNT CHECK guard requiring exactly
    4 entries)
3.  ROLES-LOADED or ROLES-NOTE
4.  ROLE-LOAD-ORDER three-tier constraint applied (Engineering / Operations / remaining types)
    with IF/THEN tier-interleaving FAIL condition
5.  ROLE-TYPE-CLASSIFICATION
6.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
7.  Inertia Assessment (observable-indicator rationale cited before STRUCTURING-COST FRAME /
    STRUCTURING-COST FRAME before mechanism table / Case for Staying Flat [FLAT-CASE-CLOSED
    separator with IF/THEN mechanism-row misplacement FAIL] / How We Coordinate Today /
    Rebuttal / VERDICT [opens with FLAT-CASE-PRESSURE line])
8.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
9.  ASCII Org Diagram
10. `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
11. GATE-CONDITION-MET block (SOURCE-GATE / GATE-VERDICT / ARRIVAL-COUNTERPART)
12. Headcount by Area
13. Operating Rhythm Table
14. Committee Charters (Purpose / Membership / Decides / Escalates / Quorum [N of M
    fraction] with IF/THEN Quorum-omission FAIL condition)
15. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
16. ORG-ELEMENT REGISTER
17. Org Evolution Roadmap
18. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```

---

## V-02

**Variation axis:** Axis B -- CHECKPOINT-INERTIA affirmative PASS CHECKLIST (C-51, lifecycle emphasis)
**Hypothesis:** R18 V-05's CHECKPOINT-INERTIA satisfies C-41 (FAIL-condition present) via inline
IF/THEN statements in Sub-section 1, but there is no dedicated named CHECKPOINT-INERTIA block
with an affirmative PASS CHECKLIST. A model operating under C-41's FAIL-condition-only form knows
what causes failure (mechanism row before STRUCTURING-COST FRAME) but has no checkpoint that
positively confirms (a) the frame was closed before the first mechanism row, (b) the row count
meets the minimum, and (c) the FLAT-CASE-CLOSED sentinel was emitted correctly, before GATE 1
STATUS fires. This mirrors the C-42->C-43 pattern exactly: C-42 added a FAIL condition to
CHECKPOINT-0; C-43 added an affirmative PASS CHECKLIST. Adding the same three-item PASS CHECKLIST
to CHECKPOINT-INERTIA converts it from an absence-of-failure gate to a positive structural
confirmation of all Sub-section 1 prerequisites. This tests whether checklist form changes gate
enforcement quality independently of any rationale form changes.

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
      name]` -- DO NOT use informal names (e.g., "role list" in place of "typed role list")
      or paraphrase form (e.g., "inertia output") instead of the canonical artifact name
      from the ARTIFACT-HANDOFF INVENTORY. The four transitions are:
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

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role in the format
  `- [role name] -- [one-line description from role file]`.
DO NOT invent role names unless no roles files are found.
If no files are found, DO produce a
  `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` block instead,
  with one inferred entry per role in the format `- [role name] -- [description]`.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER -- THREE-TIER CLASSIFICATION SEQUENCE CONSTRAINT

DO classify roles in this strict three-tier order: `Engineering` types first, then
`Operations` types, then `PM`, `Design`, `Research`, and `Other` types.
If no `Engineering` roles are present, begin with `Operations` types.
If neither `Engineering` nor `Operations` roles are present, classify all roles in any order.
DO NOT interleave tiers -- complete all entries in one tier before writing any entry from
the next tier.
IF any tier-N entry appears before all tier-(N-1) entries are written, the
  ROLE-TYPE-CLASSIFICATION block is invalid -- re-emit the full classification in strict
  tier order before proceeding to GATE 0 STATUS.

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

Before writing the mechanism table, produce a STRUCTURING-COST FRAME block that names
the two cost categories to weigh:

  STRUCTURING-COST FRAME:
  - Over-structuring overhead: committee formation load, governance cadence cost
    (meeting hours/quarter), role-specialization coordination tax
  - Under-coordination risk: decision latency, missed SLA exposure, knowledge silo
    formation, competing roadmap without arbitration owner

These two categories are the evaluative lens for every mechanism row below.
DO NOT begin the mechanism table before this block is present.

DO produce a three-column mechanism evidence table with columns
  `Mechanism Name | Type | Frequency / Participants`.
DO include at minimum two data rows.
The Type column MUST contain only values from this closed vocabulary:
  `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
DO NOT use Type values outside this vocabulary.
Each Mechanism Name MUST name a specific, observable coordination mechanism.
DO NOT move mechanism-typed table content into Sub-section 2.
IF any mechanism row is written in Sub-section 2 instead of Sub-section 1, the
  FLAT-CASE-CLOSED count is understated -- move all mechanism-typed rows to Sub-section 1
  and recount before emitting the FLAT-CASE-CLOSED sentinel.

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

CHECKPOINT-INERTIA -- PRE-GATE 1 PASS CHECKLIST

Before emitting GATE 1 STATUS, confirm all three:

  [ ] (a) STRUCTURING-COST FRAME block is closed before the first mechanism row --
          confirmed: the STRUCTURING-COST FRAME block appeared in produced output
          before the `Mechanism Name | Type | Frequency / Participants` header row.
  [ ] (b) COUNT CHECK: mechanism row count >= 2 -- count data rows in the Sub-section 1
          table (header excluded). IF count < 2: STOP -- write missing rows until count
          reaches 2 before proceeding to (c). FAIL if fewer than 2 mechanism rows are
          present when this checkpoint runs and no remediation has been applied.
  [ ] (c) FLAT-CASE-CLOSED sentinel emitted with correct count -- the sentinel
          `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today
          begins.] ---` is present in produced output with N equal to the actual data
          row count confirmed in item (b).

FAIL: If any of (a), (b), or (c) cannot be confirmed, STOP. Do not emit GATE 1 STATUS.
PASS: All three items above confirmed. Proceed to emit GATE 1 STATUS.

When CHECKPOINT-INERTIA PASSES, DO emit:
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

Before writing any headcount row, produce a GATE-CONDITION-MET block confirming receipt
of the org diagram artifact from GATE 2->3:

  GATE-CONDITION-MET:
    SOURCE-GATE: === [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===
    GATE-VERDICT: authorized to proceed -- org diagram artifact received from GATE 2->3
    ARRIVAL-COUNTERPART: Headcount by Area section

DO NOT write any headcount row before this block is present.
DO NOT omit the SOURCE-GATE field -- it must quote the exact gate line text from the
  departure site, not a paraphrase.

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
IF any charter is missing the Quorum field, that charter is incomplete -- add the
  Quorum field in `N of M member roles` fraction form before emitting CHARTERS COMPLETE.

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
    prohibition, preamble-sentence prohibition, and COUNT CHECK guard requiring exactly
    4 entries)
3.  ROLES-LOADED or ROLES-NOTE
4.  ROLE-LOAD-ORDER three-tier constraint applied (Engineering / Operations / remaining types)
    with IF/THEN tier-interleaving FAIL condition
5.  ROLE-TYPE-CLASSIFICATION
6.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
7.  Inertia Assessment (STRUCTURING-COST FRAME before mechanism table / Case for Staying
    Flat [FLAT-CASE-CLOSED separator with IF/THEN mechanism-row misplacement FAIL] /
    How We Coordinate Today / Rebuttal / VERDICT [opens with FLAT-CASE-PRESSURE line] /
    CHECKPOINT-INERTIA PASS CHECKLIST [(a) STRUCTURING-COST FRAME close confirmation,
    (b) COUNT CHECK mechanism rows >= 2 with named FAIL, (c) FLAT-CASE-CLOSED sentinel
    confirmation with correct count])
8.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
9.  ASCII Org Diagram
10. `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
11. GATE-CONDITION-MET block (SOURCE-GATE / GATE-VERDICT / ARRIVAL-COUNTERPART)
12. Headcount by Area
13. Operating Rhythm Table
14. Committee Charters (Purpose / Membership / Decides / Escalates / Quorum [N of M
    fraction] with IF/THEN Quorum-omission FAIL condition)
15. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
16. ORG-ELEMENT REGISTER
17. Org Evolution Roadmap
18. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```

---

## V-03

**Variation axis:** Axis C -- named RATIONALE-FORM-CONTRACT block (C-50 hardening, phrasing register)
**Hypothesis:** V-01 adds an inline prohibition against STEELMAN FIRST and an observable-indicator
requirement within the INERTIA ASSESSMENT section body. This satisfies C-50's pass condition but
the prohibition is embedded in a multi-line instruction block and requires the reader to parse
it inline with the mechanism table instructions. V-03 elevates the same constraint to a standalone
named RATIONALE-FORM-CONTRACT block declared before the INERTIA ASSESSMENT section -- parallel to
how VIOLATION-LABEL-CONTRACT (A-44) is a named block separate from the correspondence section
instructions. A named block is independently scannable: a reviewer checking C-50 can locate the
contract by name rather than parsing the INERTIA ASSESSMENT instruction body. The contract declares
both the VALID forms (observable indicators) and the PROHIBITED forms (structural-ordering devices,
with STEELMAN FIRST as the named example) as a formal vocabulary contract. This tests whether the
named-block form is the maximally detectable version of the C-50 constraint, independent of any
CHECKPOINT-INERTIA changes.

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
      name]` -- DO NOT use informal names (e.g., "role list" in place of "typed role list")
      or paraphrase form (e.g., "inertia output") instead of the canonical artifact name
      from the ARTIFACT-HANDOFF INVENTORY. The four transitions are:
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

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role in the format
  `- [role name] -- [one-line description from role file]`.
DO NOT invent role names unless no roles files are found.
If no files are found, DO produce a
  `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` block instead,
  with one inferred entry per role in the format `- [role name] -- [description]`.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER -- THREE-TIER CLASSIFICATION SEQUENCE CONSTRAINT

DO classify roles in this strict three-tier order: `Engineering` types first, then
`Operations` types, then `PM`, `Design`, `Research`, and `Other` types.
If no `Engineering` roles are present, begin with `Operations` types.
If neither `Engineering` nor `Operations` roles are present, classify all roles in any order.
DO NOT interleave tiers -- complete all entries in one tier before writing any entry from
the next tier.
IF any tier-N entry appears before all tier-(N-1) entries are written, the
  ROLE-TYPE-CLASSIFICATION block is invalid -- re-emit the full classification in strict
  tier order before proceeding to GATE 0 STATUS.

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

RATIONALE-FORM-CONTRACT

The flat-case default position in the Inertia Assessment is governed by this contract.
Read this block before writing Sub-section 1.

  VALID rationale forms -- cite at least one observable indicator:
    - coordination costs observable: committee formation load, governance cadence hours,
      role-specialization coordination tax observable in the team's current operating state
    - team scale observable: current headcount count, geographic distribution, synchronous
      overlap window that currently covers all necessary coordination without dedicated
      structure
    - delivery evidence observable: shipped milestone record, SLA met rate, decision
      latency record demonstrating flat operation is sufficient at current scale

  PROHIBITED rationale forms -- DO NOT use as an observable-indicator substitute:
    - structural-ordering devices: e.g., STEELMAN FIRST -- presenting the flat case's
      arguments in a favorable order is a rhetorical presentation choice, not a citation
      of an observable indicator from the team's coordination reality; a rationale that
      leads with the flat case's strongest arguments without naming any observable
      indicator from the VALID set above does not satisfy this contract
    - general principles: e.g., "flat teams are more agile" or "small teams do not need
      structure" without grounding in the team's observable coordination state

This contract is independently scannable. The rationale cited in Sub-section 1 MUST name
at least one VALID form indicator before the STRUCTURING-COST FRAME block begins.
DO NOT proceed to Sub-section 1 until this contract has been read.

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS

DO write the Inertia Assessment before any org boxes.
DO NOT write an org diagram as the first section.
DO structure the inertia assessment in this exact four-sub-section order:
  Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

Sub-section 1 -- Case for Staying Flat

Cite the observable indicator from RATIONALE-FORM-CONTRACT that grounds the flat-case
default position for this team. DO NOT use a structural-ordering device in place of
this citation.

Before writing the mechanism table, produce a STRUCTURING-COST FRAME block that names
the two cost categories to weigh:

  STRUCTURING-COST FRAME:
  - Over-structuring overhead: committee formation load, governance cadence cost
    (meeting hours/quarter), role-specialization coordination tax
  - Under-coordination risk: decision latency, missed SLA exposure, knowledge silo
    formation, competing roadmap without arbitration owner

These two categories are the evaluative lens for every mechanism row below.
DO NOT begin the mechanism table before this block is present.

DO produce a three-column mechanism evidence table with columns
  `Mechanism Name | Type | Frequency / Participants`.
DO include at minimum two data rows.
The Type column MUST contain only values from this closed vocabulary:
  `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
DO NOT use Type values outside this vocabulary.
Each Mechanism Name MUST name a specific, observable coordination mechanism.
DO NOT move mechanism-typed table content into Sub-section 2.
IF any mechanism row is written in Sub-section 2 instead of Sub-section 1, the
  FLAT-CASE-CLOSED count is understated -- move all mechanism-typed rows to Sub-section 1
  and recount before emitting the FLAT-CASE-CLOSED sentinel.

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

Before writing any headcount row, produce a GATE-CONDITION-MET block confirming receipt
of the org diagram artifact from GATE 2->3:

  GATE-CONDITION-MET:
    SOURCE-GATE: === [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===
    GATE-VERDICT: authorized to proceed -- org diagram artifact received from GATE 2->3
    ARRIVAL-COUNTERPART: Headcount by Area section

DO NOT write any headcount row before this block is present.
DO NOT omit the SOURCE-GATE field -- it must quote the exact gate line text from the
  departure site, not a paraphrase.

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
IF any charter is missing the Quorum field, that charter is incomplete -- add the
  Quorum field in `N of M member roles` fraction form before emitting CHARTERS COMPLETE.

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
    prohibition, preamble-sentence prohibition, and COUNT CHECK guard requiring exactly
    4 entries)
3.  ROLES-LOADED or ROLES-NOTE
4.  ROLE-LOAD-ORDER three-tier constraint applied (Engineering / Operations / remaining types)
    with IF/THEN tier-interleaving FAIL condition
5.  ROLE-TYPE-CLASSIFICATION
6.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
7.  RATIONALE-FORM-CONTRACT (VALID observable-indicator forms / PROHIBITED structural-ordering
    device forms with STEELMAN FIRST named as example anti-form)
8.  Inertia Assessment (observable-indicator rationale from RATIONALE-FORM-CONTRACT cited
    before STRUCTURING-COST FRAME / STRUCTURING-COST FRAME before mechanism table / Case for
    Staying Flat [FLAT-CASE-CLOSED separator with IF/THEN mechanism-row misplacement FAIL] /
    How We Coordinate Today / Rebuttal / VERDICT [opens with FLAT-CASE-PRESSURE line])
9.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
10. ASCII Org Diagram
11. `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
12. GATE-CONDITION-MET block (SOURCE-GATE / GATE-VERDICT / ARRIVAL-COUNTERPART)
13. Headcount by Area
14. Operating Rhythm Table
15. Committee Charters (Purpose / Membership / Decides / Escalates / Quorum [N of M
    fraction] with IF/THEN Quorum-omission FAIL condition)
16. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
17. ORG-ELEMENT REGISTER
18. Org Evolution Roadmap
19. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```

---

## V-04

**Variation axes:** Axis A + Axis B -- observable-indicator rationale + STEELMAN FIRST prohibition
(C-50) + CHECKPOINT-INERTIA PASS CHECKLIST (C-51)
**Hypothesis:** C-50 and C-51 address independent dimensions of the Sub-section 1 production path:
C-50 governs rationale form (what grounding is cited before the mechanism table), C-51 governs
checkpoint structure (what the gate positively confirms after VERDICT before GATE 1 STATUS emits).
Neither subsumes the other. A model under V-01 knows the rationale must be observable-indicator
grounded but has no affirmative checklist confirming Sub-section 1 structural prerequisites at gate
time. A model under V-02 has the checklist but can still use STEELMAN FIRST as rationale. V-04
combines both: the rationale is grounded before the mechanism table AND the CHECKPOINT-INERTIA
confirms frame-close, row count, and sentinel before GATE 1 STATUS. Axis C (named contract block)
is withheld to test the A+B combination without the additional named-block overhead.

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
      name]` -- DO NOT use informal names (e.g., "role list" in place of "typed role list")
      or paraphrase form (e.g., "inertia output") instead of the canonical artifact name
      from the ARTIFACT-HANDOFF INVENTORY. The four transitions are:
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

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role in the format
  `- [role name] -- [one-line description from role file]`.
DO NOT invent role names unless no roles files are found.
If no files are found, DO produce a
  `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` block instead,
  with one inferred entry per role in the format `- [role name] -- [description]`.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER -- THREE-TIER CLASSIFICATION SEQUENCE CONSTRAINT

DO classify roles in this strict three-tier order: `Engineering` types first, then
`Operations` types, then `PM`, `Design`, `Research`, and `Other` types.
If no `Engineering` roles are present, begin with `Operations` types.
If neither `Engineering` nor `Operations` roles are present, classify all roles in any order.
DO NOT interleave tiers -- complete all entries in one tier before writing any entry from
the next tier.
IF any tier-N entry appears before all tier-(N-1) entries are written, the
  ROLE-TYPE-CLASSIFICATION block is invalid -- re-emit the full classification in strict
  tier order before proceeding to GATE 0 STATUS.

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

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS -- INERTIA-FIRST EVALUATION

DO write the Inertia Assessment before any org boxes.
DO NOT write an org diagram as the first section.
DO structure the inertia assessment in this exact four-sub-section order:
  Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

The flat-case default position MUST be grounded in at least one observable indicator from
this closed set before the mechanism evidence table begins:
  - coordination costs observable: committee formation load, governance cadence hours,
    role-specialization coordination tax observable in the team's current operating state
  - team scale observable: current headcount, geographic distribution, synchronous overlap
    window that currently covers all necessary coordination without dedicated structure
  - delivery evidence observable: shipped milestone record, SLA met rate, decision latency
    record that demonstrates flat operation is sufficient at current scale
DO NOT use structural-ordering devices as a substitute for this rationale. STEELMAN FIRST
  is a structural-ordering device -- it positions the flat case's strongest arguments first
  as a rhetorical presentation choice, not as a citation of an observable indicator.
  A rationale that leads with the flat case's most favorable arguments without citing any
  observable indicator from the closed set above does not satisfy this requirement.
DO cite the chosen observable indicator explicitly before the STRUCTURING-COST FRAME block.

Sub-section 1 -- Case for Staying Flat

Before writing the mechanism table, produce a STRUCTURING-COST FRAME block that names
the two cost categories to weigh:

  STRUCTURING-COST FRAME:
  - Over-structuring overhead: committee formation load, governance cadence cost
    (meeting hours/quarter), role-specialization coordination tax
  - Under-coordination risk: decision latency, missed SLA exposure, knowledge silo
    formation, competing roadmap without arbitration owner

These two categories are the evaluative lens for every mechanism row below.
DO NOT begin the mechanism table before this block is present.

DO produce a three-column mechanism evidence table with columns
  `Mechanism Name | Type | Frequency / Participants`.
DO include at minimum two data rows.
The Type column MUST contain only values from this closed vocabulary:
  `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
DO NOT use Type values outside this vocabulary.
Each Mechanism Name MUST name a specific, observable coordination mechanism.
DO NOT move mechanism-typed table content into Sub-section 2.
IF any mechanism row is written in Sub-section 2 instead of Sub-section 1, the
  FLAT-CASE-CLOSED count is understated -- move all mechanism-typed rows to Sub-section 1
  and recount before emitting the FLAT-CASE-CLOSED sentinel.

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

CHECKPOINT-INERTIA -- PRE-GATE 1 PASS CHECKLIST

Before emitting GATE 1 STATUS, confirm all three:

  [ ] (a) STRUCTURING-COST FRAME block is closed before the first mechanism row --
          confirmed: the STRUCTURING-COST FRAME block appeared in produced output
          before the `Mechanism Name | Type | Frequency / Participants` header row.
  [ ] (b) COUNT CHECK: mechanism row count >= 2 -- count data rows in the Sub-section 1
          table (header excluded). IF count < 2: STOP -- write missing rows until count
          reaches 2 before proceeding to (c). FAIL if fewer than 2 mechanism rows are
          present when this checkpoint runs and no remediation has been applied.
  [ ] (c) FLAT-CASE-CLOSED sentinel emitted with correct count -- the sentinel
          `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today
          begins.] ---` is present in produced output with N equal to the actual data
          row count confirmed in item (b).

FAIL: If any of (a), (b), or (c) cannot be confirmed, STOP. Do not emit GATE 1 STATUS.
PASS: All three items above confirmed. Proceed to emit GATE 1 STATUS.

When CHECKPOINT-INERTIA PASSES, DO emit:
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

Before writing any headcount row, produce a GATE-CONDITION-MET block confirming receipt
of the org diagram artifact from GATE 2->3:

  GATE-CONDITION-MET:
    SOURCE-GATE: === [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===
    GATE-VERDICT: authorized to proceed -- org diagram artifact received from GATE 2->3
    ARRIVAL-COUNTERPART: Headcount by Area section

DO NOT write any headcount row before this block is present.
DO NOT omit the SOURCE-GATE field -- it must quote the exact gate line text from the
  departure site, not a paraphrase.

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
IF any charter is missing the Quorum field, that charter is incomplete -- add the
  Quorum field in `N of M member roles` fraction form before emitting CHARTERS COMPLETE.

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
    prohibition, preamble-sentence prohibition, and COUNT CHECK guard requiring exactly
    4 entries)
3.  ROLES-LOADED or ROLES-NOTE
4.  ROLE-LOAD-ORDER three-tier constraint applied (Engineering / Operations / remaining types)
    with IF/THEN tier-interleaving FAIL condition
5.  ROLE-TYPE-CLASSIFICATION
6.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
7.  Inertia Assessment (observable-indicator rationale cited before STRUCTURING-COST FRAME /
    STRUCTURING-COST FRAME before mechanism table / Case for Staying Flat [FLAT-CASE-CLOSED
    separator with IF/THEN mechanism-row misplacement FAIL] / How We Coordinate Today /
    Rebuttal / VERDICT [opens with FLAT-CASE-PRESSURE line] / CHECKPOINT-INERTIA PASS
    CHECKLIST [(a) STRUCTURING-COST FRAME close confirmation, (b) COUNT CHECK mechanism
    rows >= 2 with named FAIL, (c) FLAT-CASE-CLOSED sentinel confirmation with correct count])
8.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
9.  ASCII Org Diagram
10. `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
11. GATE-CONDITION-MET block (SOURCE-GATE / GATE-VERDICT / ARRIVAL-COUNTERPART)
12. Headcount by Area
13. Operating Rhythm Table
14. Committee Charters (Purpose / Membership / Decides / Escalates / Quorum [N of M
    fraction] with IF/THEN Quorum-omission FAIL condition)
15. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
16. ORG-ELEMENT REGISTER
17. Org Evolution Roadmap
18. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```

---

## V-05

**Variation axes:** Axis A + Axis B + Axis C -- full integration on R18 V-05 baseline
**Hypothesis:** All three R19 axes address independent dimensions that do not interact at the
bypass level: Axis A closes the inline rationale form (observable-indicator prohibition), Axis B
closes the CHECKPOINT-INERTIA pass-checklist gap, Axis C closes the named-contract detectability
gap. V-05 is the strongest R19 form: a model executing against this prompt reads the
RATIONALE-FORM-CONTRACT before writing Sub-section 1 (C), cites an observable indicator from the
contract's VALID set before the STRUCTURING-COST FRAME (A), then at gate time runs the
CHECKPOINT-INERTIA PASS CHECKLIST confirming frame-close, row count, and sentinel (B). The combined
effect tests whether the named-block contract (C) plus inline observable-indicator requirement (A)
plus affirmative pass checklist (B) produce qualitatively different Sub-section 1 output than any
single-axis or two-axis form. V-05 also serves as the seed for R20 gap identification: any bypass
that survives all three active axes points to the next deepening target.

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
      name]` -- DO NOT use informal names (e.g., "role list" in place of "typed role list")
      or paraphrase form (e.g., "inertia output") instead of the canonical artifact name
      from the ARTIFACT-HANDOFF INVENTORY. The four transitions are:
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

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block with one entry per role in the format
  `- [role name] -- [one-line description from role file]`.
DO NOT invent role names unless no roles files are found.
If no files are found, DO produce a
  `ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:` block instead,
  with one inferred entry per role in the format `- [role name] -- [description]`.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER -- THREE-TIER CLASSIFICATION SEQUENCE CONSTRAINT

DO classify roles in this strict three-tier order: `Engineering` types first, then
`Operations` types, then `PM`, `Design`, `Research`, and `Other` types.
If no `Engineering` roles are present, begin with `Operations` types.
If neither `Engineering` nor `Operations` roles are present, classify all roles in any order.
DO NOT interleave tiers -- complete all entries in one tier before writing any entry from
the next tier.
IF any tier-N entry appears before all tier-(N-1) entries are written, the
  ROLE-TYPE-CLASSIFICATION block is invalid -- re-emit the full classification in strict
  tier order before proceeding to GATE 0 STATUS.

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

RATIONALE-FORM-CONTRACT

The flat-case default position in the Inertia Assessment is governed by this contract.
Read this block before writing Sub-section 1.

  VALID rationale forms -- cite at least one observable indicator:
    - coordination costs observable: committee formation load, governance cadence hours,
      role-specialization coordination tax observable in the team's current operating state
    - team scale observable: current headcount count, geographic distribution, synchronous
      overlap window that currently covers all necessary coordination without dedicated
      structure
    - delivery evidence observable: shipped milestone record, SLA met rate, decision
      latency record demonstrating flat operation is sufficient at current scale

  PROHIBITED rationale forms -- DO NOT use as an observable-indicator substitute:
    - structural-ordering devices: e.g., STEELMAN FIRST -- presenting the flat case's
      arguments in a favorable order is a rhetorical presentation choice, not a citation
      of an observable indicator from the team's coordination reality; a rationale that
      leads with the flat case's strongest arguments without naming any observable
      indicator from the VALID set above does not satisfy this contract
    - general principles: e.g., "flat teams are more agile" or "small teams do not need
      structure" without grounding in the team's observable coordination state

This contract is independently scannable. The rationale cited in Sub-section 1 MUST name
at least one VALID form indicator before the STRUCTURING-COST FRAME block begins.
DO NOT proceed to Sub-section 1 until this contract has been read.

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS -- INERTIA-FIRST EVALUATION

DO write the Inertia Assessment before any org boxes.
DO NOT write an org diagram as the first section.
DO structure the inertia assessment in this exact four-sub-section order:
  Case for Staying Flat / How We Coordinate Today / Rebuttal / VERDICT.

The flat-case default position MUST be grounded in at least one observable indicator from
the RATIONALE-FORM-CONTRACT VALID set before the mechanism evidence table begins.
DO NOT use structural-ordering devices (e.g., STEELMAN FIRST) as a substitute for this
  rationale -- STEELMAN FIRST positions the flat case's arguments favorably as a
  presentation choice, not as a citation of any observable indicator.
DO cite the chosen observable indicator explicitly before the STRUCTURING-COST FRAME block.

Sub-section 1 -- Case for Staying Flat

Cite the observable indicator from RATIONALE-FORM-CONTRACT that grounds the flat-case
default position for this team. DO NOT use a structural-ordering device in place of
this citation.

Before writing the mechanism table, produce a STRUCTURING-COST FRAME block that names
the two cost categories to weigh:

  STRUCTURING-COST FRAME:
  - Over-structuring overhead: committee formation load, governance cadence cost
    (meeting hours/quarter), role-specialization coordination tax
  - Under-coordination risk: decision latency, missed SLA exposure, knowledge silo
    formation, competing roadmap without arbitration owner

These two categories are the evaluative lens for every mechanism row below.
DO NOT begin the mechanism table before this block is present.

DO produce a three-column mechanism evidence table with columns
  `Mechanism Name | Type | Frequency / Participants`.
DO include at minimum two data rows.
The Type column MUST contain only values from this closed vocabulary:
  `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
DO NOT use Type values outside this vocabulary.
Each Mechanism Name MUST name a specific, observable coordination mechanism.
DO NOT move mechanism-typed table content into Sub-section 2.
IF any mechanism row is written in Sub-section 2 instead of Sub-section 1, the
  FLAT-CASE-CLOSED count is understated -- move all mechanism-typed rows to Sub-section 1
  and recount before emitting the FLAT-CASE-CLOSED sentinel.

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

CHECKPOINT-INERTIA -- PRE-GATE 1 PASS CHECKLIST

Before emitting GATE 1 STATUS, confirm all three:

  [ ] (a) STRUCTURING-COST FRAME block is closed before the first mechanism row --
          confirmed: the STRUCTURING-COST FRAME block appeared in produced output
          before the `Mechanism Name | Type | Frequency / Participants` header row.
  [ ] (b) COUNT CHECK: mechanism row count >= 2 -- count data rows in the Sub-section 1
          table (header excluded). IF count < 2: STOP -- write missing rows until count
          reaches 2 before proceeding to (c). FAIL if fewer than 2 mechanism rows are
          present when this checkpoint runs and no remediation has been applied.
  [ ] (c) FLAT-CASE-CLOSED sentinel emitted with correct count -- the sentinel
          `--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded. How We Coordinate Today
          begins.] ---` is present in produced output with N equal to the actual data
          row count confirmed in item (b).

FAIL: If any of (a), (b), or (c) cannot be confirmed, STOP. Do not emit GATE 1 STATUS.
PASS: All three items above confirmed. Proceed to emit GATE 1 STATUS.

When CHECKPOINT-INERTIA PASSES, DO emit:
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

Before writing any headcount row, produce a GATE-CONDITION-MET block confirming receipt
of the org diagram artifact from GATE 2->3:

  GATE-CONDITION-MET:
    SOURCE-GATE: === [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===
    GATE-VERDICT: authorized to proceed -- org diagram artifact received from GATE 2->3
    ARRIVAL-COUNTERPART: Headcount by Area section

DO NOT write any headcount row before this block is present.
DO NOT omit the SOURCE-GATE field -- it must quote the exact gate line text from the
  departure site, not a paraphrase.

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
IF any charter is missing the Quorum field, that charter is incomplete -- add the
  Quorum field in `N of M member roles` fraction form before emitting CHARTERS COMPLETE.

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
    prohibition, preamble-sentence prohibition, and COUNT CHECK guard requiring exactly
    4 entries)
3.  ROLES-LOADED or ROLES-NOTE
4.  ROLE-LOAD-ORDER three-tier constraint applied (Engineering / Operations / remaining types)
    with IF/THEN tier-interleaving FAIL condition
5.  ROLE-TYPE-CLASSIFICATION
6.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
7.  RATIONALE-FORM-CONTRACT (VALID observable-indicator forms / PROHIBITED structural-ordering
    device forms with STEELMAN FIRST named as example anti-form)
8.  Inertia Assessment (observable-indicator rationale from RATIONALE-FORM-CONTRACT cited
    before STRUCTURING-COST FRAME / STRUCTURING-COST FRAME before mechanism table / Case for
    Staying Flat [FLAT-CASE-CLOSED separator with IF/THEN mechanism-row misplacement FAIL] /
    How We Coordinate Today / Rebuttal / VERDICT [opens with FLAT-CASE-PRESSURE line] /
    CHECKPOINT-INERTIA PASS CHECKLIST [(a) STRUCTURING-COST FRAME close confirmation,
    (b) COUNT CHECK mechanism rows >= 2 with named FAIL, (c) FLAT-CASE-CLOSED sentinel
    confirmation with correct count])
9.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
10. ASCII Org Diagram
11. `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
12. GATE-CONDITION-MET block (SOURCE-GATE / GATE-VERDICT / ARRIVAL-COUNTERPART)
13. Headcount by Area
14. Operating Rhythm Table
15. Committee Charters (Purpose / Membership / Decides / Escalates / Quorum [N of M
    fraction] with IF/THEN Quorum-omission FAIL condition)
16. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
17. ORG-ELEMENT REGISTER
18. Org Evolution Roadmap
19. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```
