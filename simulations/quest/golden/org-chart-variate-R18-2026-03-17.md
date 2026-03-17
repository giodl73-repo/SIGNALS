---
skill: quest-variate
skill_target: org-chart
date: 2026-03-17
round: R18
rubric_version: v18
status: variate
---

# org-chart Variate -- Round 18

**Date:** 2026-03-17
**Skill:** org-chart
**Rubric:** v18 (C-01 through C-49; C-47/C-48/C-49 new from v18, all parallel extensions of C-46)
**Round:** R18 -- single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

**R17 ceiling under v17:**
R17 V-05 achieves all three v18 target behaviors as non-scoring signals:
- C-47 (count guard): COUNT CHECK after numbered list in item (b); named FAIL condition
- C-48 (format anchor): "Each entry MUST use the exact format GATE X->Y: [artifact name]" with named anti-forms
- C-49 (preamble prohibition): "DO NOT write a preamble sentence" with two example banned forms; "item (b) MUST open directly with entry 1"

R17 V-05 is the R18 baseline. All five R18 variations carry C-47 + C-48 + C-49 in CHECKPOINT-0 item (b) as the new floor.

**Remaining structural gaps after R17 V-05:**

R17 V-05 closes all three item (b) bypasses. Three structural dimensions outside item (b) are not yet constrained:

1. **FAIL-path consequence gap (Axis A target):** The DO/DO NOT vocabulary names prohibited actions at key points (tier interleaving, mechanism row misplacement, Quorum omission) but does not state what happens when the prohibition is violated. A model can encounter "DO NOT interleave tiers" or "DO NOT omit the Quorum field" and continue producing output that violates the constraint without a named stop condition at the violation site. The CHECKPOINT at gate completion is the only recovery point -- but it fires after the violation has already propagated. Inline FAIL-path consequence statements at the three highest-risk constraint sites convert bare prohibitions into recoverable FAIL conditions with named remediation paths.

2. **Cost-frame position gap (Axis B target):** The INERTIA ASSESSMENT begins with Sub-section 1 (Case for Staying Flat) directly -- the mechanism table is the first element the model writes. The cost categories (over-structuring overhead vs. under-coordination risk) are inferred from the VERDICT sub-section, not declared before evidence is gathered. A STRUCTURING-COST FRAME placed before the mechanism table converts the table from evidence-first to cost-lens-first: the model reads cost categories before populating mechanism rows, establishing the evaluative lens that governs Sub-section 1 before any row is written.

3. **Arrival-site gate gap (Axis C target):** Every gate transition has a departure-site emission ("=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===") but no arrival-site acknowledgment. The consuming section begins writing immediately after the gate line, with no confirmation that the upstream artifact was received and meets its contract. A GATE-CONDITION-MET acknowledgment block at the start of the HEADCOUNT section (arrival site of GATE 2->3) closes the one-sided gate pattern: the departure declares; the arrival confirms. This tests whether an arrival token changes cross-gate continuity enforcement for the org diagram -> headcount handoff.

**Variation axes for R18:**

**Axis A** -- FAIL-path consequence injection (phrasing register)
  A-form-1 (R17 V-05 baseline): DO/DO NOT prohibitions at violation sites; no inline consequence; recovery only at gate CHECKPOINT
  A-form-2 (V-01, V-04, V-05): adds inline "IF [violation] THEN STOP -- [remediation]" at three highest-risk sites:
    (1) tier interleaving in ROLE-LOAD-ORDER
    (2) mechanism row misplacement in Sub-section 1
    (3) Quorum field omission in COMMITTEE CHARTERS

**Axis B** -- STRUCTURING-COST FRAME before mechanism table (inertia framing)
  B-form-1 (R17 V-05 baseline): Sub-section 1 opens with mechanism table; cost categories inferred from VERDICT
  B-form-2 (V-02, V-04, V-05): adds STRUCTURING-COST FRAME block immediately before mechanism table, naming the two cost categories (over-structuring overhead, under-coordination risk) with observable cost anchors before any mechanism row is written

**Axis C** -- GATE-CONDITION-MET arrival acknowledgment at HEADCOUNT (lifecycle emphasis)
  C-form-1 (R17 V-05 baseline): arrival site (HEADCOUNT section) begins immediately after departure gate line; no arrival confirmation
  C-form-2 (V-03, V-04, V-05): adds a three-field GATE-CONDITION-MET block at the start of HEADCOUNT:
    SOURCE-GATE: [exact departure gate line text]
    GATE-VERDICT: authorized to proceed -- org diagram artifact received
    ARRIVAL-COUNTERPART: Headcount by Area section

Single-axis: V-01 (Axis A, form 2), V-02 (Axis B, form 2), V-03 (Axis C, form 2)
Combined:    V-04 (A-form-2 + B-form-2), V-05 (A-form-2 + B-form-2 + C-form-2)

---

## V-01

**Variation axis:** Axis A, form 2 -- FAIL-path consequence injection at three highest-risk DO NOT sites
**Hypothesis:** R17 V-05's DO/DO NOT vocabulary names what must not happen but leaves the model without a named consequence at the violation site. A model under compression or context pressure can pass a "DO NOT interleave tiers" constraint by acknowledging it and continuing with the violation, because no inline FAIL condition fires until the gate CHECKPOINT -- which arrives after the violation has propagated through several downstream sections. Adding explicit "IF [violation] THEN STOP -- [remediation]" statements at the three sites where silent violations are most consequential (tier interleaving, mechanism row misplacement, Quorum omission) converts the prohibition from a one-way declaration into a bidirectional consequence chain. This tests whether consequence visibility at the violation site -- not just at the gate checkpoint -- changes model behavior on the highest-risk format constraints.

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
7.  Inertia Assessment (Case for Staying Flat [FLAT-CASE-CLOSED separator with IF/THEN
    mechanism-row misplacement FAIL] / How We Coordinate Today / Rebuttal / VERDICT
    [opens with FLAT-CASE-PRESSURE line])
8.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
9.  ASCII Org Diagram
10. `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
11. Headcount by Area
12. Operating Rhythm Table
13. Committee Charters (Purpose / Membership / Decides / Escalates / Quorum [N of M
    fraction] with IF/THEN Quorum-omission FAIL condition)
14. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
15. ORG-ELEMENT REGISTER
16. Org Evolution Roadmap
17. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```

---

## V-02

**Variation axis:** Axis B, form 2 -- STRUCTURING-COST FRAME before mechanism table (inertia framing)
**Hypothesis:** The R17 V-05 baseline opens Sub-section 1 with the mechanism evidence table directly
-- the model writes mechanism rows before any cost categories are declared. Over-structuring overhead
and under-coordination risk are named only in the VERDICT sub-section, after the evidence has already
been gathered. This reverses the causal logic: cost categories should be the governing lens through
which mechanisms are evaluated, not a conclusion reached after mechanisms are listed. A
STRUCTURING-COST FRAME block placed before the mechanism table declares the two cost categories with
observable cost anchors (committee formation overhead, governance cadence load, role-specialization
coordination cost vs. decision latency, SLA exposure, knowledge silo formation) before any mechanism
row is written. This converts Sub-section 1 from evidence-first to premise-first -- the model reads
the cost framework before evaluating whether mechanisms are sufficient. This tests whether front-loading
the evaluative lens changes the quality and specificity of mechanism classifications and the
FLAT-CASE-PRESSURE rating independently of the item (b) constraint chain.

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
    prohibition, preamble-sentence prohibition, and COUNT CHECK guard requiring exactly
    4 entries)
3.  ROLES-LOADED or ROLES-NOTE
4.  ROLE-LOAD-ORDER three-tier constraint applied (Engineering / Operations / remaining types)
5.  ROLE-TYPE-CLASSIFICATION
6.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
7.  Inertia Assessment (STRUCTURING-COST FRAME before mechanism table / Case for Staying
    Flat [FLAT-CASE-CLOSED separator] / How We Coordinate Today / Rebuttal / VERDICT
    [opens with FLAT-CASE-PRESSURE line])
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

**Variation axis:** Axis C, form 2 -- GATE-CONDITION-MET arrival acknowledgment at HEADCOUNT (lifecycle emphasis)
**Hypothesis:** The R17 V-05 baseline enforces gates only at the departure site: each section ends
with a gate-emission line ("=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===")
and the consuming section begins immediately after. There is no arrival-site confirmation that the
upstream artifact was received, verified, and accepted before the consuming section executes. This
means the gate is one-sided: declaration only, with no echo. The highest-risk transition is GATE 2->3
(org diagram -> headcount), because the headcount section must faithfully reflect the org diagram's
hierarchy, area names, and role assignments -- any drift between diagram and headcount table indicates
the model re-derived the structure independently rather than consuming the diagram artifact. A
three-field GATE-CONDITION-MET block placed at the start of the HEADCOUNT section forces the arrival
site to actively confirm receipt of the org diagram artifact before any row is written. The three
fields (SOURCE-GATE, GATE-VERDICT, ARRIVAL-COUNTERPART) make the acknowledgment independently
scannable. This tests whether arrival-site confirmation changes cross-gate continuity for the
diagram-to-headcount handoff independently of any CHECKPOINT-0 or inertia changes.

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
5.  ROLE-TYPE-CLASSIFICATION
6.  `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
7.  Inertia Assessment (Case for Staying Flat [FLAT-CASE-CLOSED separator] / How We
    Coordinate Today / Rebuttal / VERDICT [opens with FLAT-CASE-PRESSURE line])
8.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
9.  ASCII Org Diagram
10. `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
11. GATE-CONDITION-MET block (SOURCE-GATE / GATE-VERDICT / ARRIVAL-COUNTERPART)
12. Headcount by Area
13. Operating Rhythm Table
14. Committee Charters (Purpose / Membership / Decides / Escalates / Quorum [N of M fraction])
15. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
16. ORG-ELEMENT REGISTER
17. Org Evolution Roadmap
18. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```

---

## V-04

**Variation axes:** Axis A, form 2 + Axis B, form 2 -- FAIL-path consequence injection + STRUCTURING-COST FRAME
**Hypothesis:** Axes A and B address different dimensions of the GATE 1 production path: Axis A
targets enforcement vocabulary (adding named FAIL conditions to the three highest-risk violations),
while Axis B targets the evaluative frame (adding a STRUCTURING-COST FRAME before the mechanism
table). Neither axis alone closes the other's gap. Together they address both when violations
are recoverable (Axis A: inline FAIL-path with named remediation) and what cost categories govern
mechanism quality (Axis B: cost categories declared before mechanisms). The interaction hypothesis:
a model reading cost categories before mechanism rows AND carrying inline FAIL conditions at
violation sites is more likely to produce Sub-section 1 tables with higher specificity
(mechanisms classified by their cost-offset function) and FLAT-CASE-PRESSURE ratings with richer
justification. Axis C (arrival acknowledgment) is withheld to test the A+B combination in isolation.

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
    How We Coordinate Today / Rebuttal / VERDICT [opens with FLAT-CASE-PRESSURE line])
8.  `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
9.  ASCII Org Diagram
10. `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
11. Headcount by Area
12. Operating Rhythm Table
13. Committee Charters (Purpose / Membership / Decides / Escalates / Quorum [N of M
    fraction] with IF/THEN Quorum-omission FAIL condition)
14. `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
15. ORG-ELEMENT REGISTER
16. Org Evolution Roadmap
17. Anti-Pattern Watch

DO NOT produce any section before its predecessor is complete.

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```

---

## V-05

**Variation axes:** Axis A, form 2 + Axis B, form 2 + Axis C, form 2 (maximum combination)
**Hypothesis:** The three R18 axes address separate structural dimensions that do not interact at
the bypass level: Axis A closes violation-consequence visibility (inline FAIL paths at the three
highest-risk constraint sites), Axis B closes evaluative-lens sequencing (cost frame before evidence
table), and Axis C closes arrival-site gap (GATE-CONDITION-MET acknowledgment at the consuming
section). None of the three axes subsumes any other. V-05 is the strongest R18 form: a model
executing against this prompt encounters cost categories before mechanism rows (B), carries named
FAIL conditions at the three highest-risk violation sites (A), and must explicitly confirm receipt
of the org diagram artifact before writing a single headcount row (C). The combined effect tests
whether the three independent improvements, when active simultaneously, produce qualitatively
different output than any single-axis or two-axis form -- specifically whether the arrival
acknowledgment (C) reveals org-diagram-to-headcount drift patterns that neither A nor B can detect.
V-05 also serves as the seed for identifying R19 gaps: any bypass that remains after all three
axes are active points directly to the next deepening target.

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
7.  Inertia Assessment (STRUCTURING-COST FRAME before mechanism table / Case for Staying
    Flat [FLAT-CASE-CLOSED separator with IF/THEN mechanism-row misplacement FAIL] /
    How We Coordinate Today / Rebuttal / VERDICT [opens with FLAT-CASE-PRESSURE line])
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
