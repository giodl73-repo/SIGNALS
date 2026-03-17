---
skill: quest-variate
skill_target: org-chart
date: 2026-03-16
round: R20
rubric_version: v18
status: variate
---

# org-chart Variate -- Round 20 (Rubric v18)

**Date:** 2026-03-16
**Skill:** org-chart
**Rubric:** v18 (criteria C-01 through A-48)
**Round:** R20 overall / Round 1 of the v18 rubric cycle

## R19 ceiling and R20 target

R19-V-05 achieves full coverage of A-01 through A-45 under the v17 rubric. Three gaps remain
under v18:

1. **Signature-gap (A-46):** GATE-CONDITION-MET (A-43) exists as an arrival acknowledgment block
   at the Operating Rhythm Table entry, but its body does not require three separately labeled
   fields -- SOURCE-GATE, GATE-VERDICT, and ARRIVAL-COUNTERPART. Gate compliance is currently
   expressed as a prose block; each component is present implicitly but not independently
   scannable by label. The three-field minimal signature (SOURCE / VERDICT / COUNTERPART)
   follows the A-23/A-43 dual-site pattern: each component of the acknowledgment must be
   independently verifiable without parsing prose context.

2. **Traceability-gap (A-47):** AUDIT-CHAIN-CARDINALITY (A-44) declares the count of audit
   blocks; each audit block carries an ordinal label (N of 2). But the ordinal label does not
   back-reference the specific AUDIT-CHAIN-CARDINALITY line that authorized that count. The
   ordinal assertion (1 of 2) is self-certified -- a reader scanning a single block cannot
   confirm that "2" came from a declared cardinality rather than from the block author's
   assumption. The A-28/A-44 cardinality-source binding pattern requires each ordinal label to
   cite the count declaration that authorized it.

3. **Gate-gap (A-48):** RHYTHM-DRI-ASSIGNMENT-COVERAGE (A-45) declares DRI-MISSING a
   constraint violation. But the enforcement block does not name the gate that is blocked.
   The constraint consequence (what is blocked and by what) exists only in the rubric, not in
   the document itself. Following the A-40/A-35 constraint-gate naming pattern, the gate
   consequence must be declared inside the enforcement block -- naming the gated section and
   the blocker at the gate declaration site.

**R20 target:** Close all three gaps. V-01/V-02/V-03 are single-axis. V-04 combines A-46+A-47.
V-05 integrates all three on the R19-V-05 baseline.

---

## Variation Map

| V    | Axis                                                              | New block(s)                                                      |
|------|-------------------------------------------------------------------|-------------------------------------------------------------------|
| V-01 | A-46 only (GATE-CONDITION-MET three-field signature)              | SOURCE-GATE / GATE-VERDICT / ARRIVAL-COUNTERPART fields in block  |
| V-02 | A-47 only (audit-block cardinality-source back-reference)         | Each AUDIT-BLOCK label cites AUDIT-CHAIN-CARDINALITY source       |
| V-03 | A-48 only (DRI-coverage constraint-gate declaration)              | DRI-COVERAGE-GATE block inside RHYTHM-DRI-ASSIGNMENT-COVERAGE     |
| V-04 | A-46 + A-47 combined                                              | Three-field gate signature + cardinality source; no coverage gate |
| V-05 | Full integration: A-46 + A-47 + A-48 on R19-V-05 baseline        | All three blocks; complete v18 coverage                           |

---

## V-01: Gate-Condition-Met Three-Field Signature (A-46 only)

**Axis:** Expand the `GATE-CONDITION-MET: SUM-VERIFIED` block (A-43) to require three separately
labeled fields: `SOURCE-GATE`, `GATE-VERDICT`, and `ARRIVAL-COUNTERPART`. Each field is a named
line item, making every component of the arrival acknowledgment independently scannable by label
scan without parsing prose.
**Hypothesis:** A-43 adds the arrival acknowledgment at the ORT entry, but its content is
expressed as an unlabeled prose block. A scanner checking gate compliance must parse the body to
confirm that the source, verdict, and arrival counterpart are all present. Adding three mandatory
labeled fields -- SOURCE-GATE naming the departure block, GATE-VERDICT naming the verdict value,
ARRIVAL-COUNTERPART naming the section being unlocked -- converts the prose acknowledgment into
a three-field minimal signature that is independently verifiable at the field level. This follows
the A-23/A-43 dual-site pattern applied to the internal structure of the acknowledgment itself.

---

You are running `/org-chart {topic}`.

DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.

Formal org structure is not the answer -- it is the proposal. Informal coordination
(channels, standups, de-facto leads, shared documents) is the status quo you are
trying to displace. Do not draw an org box until you have argued the case for staying
flat and found the specific failure mode it cannot answer.

---

PHASE 1: LOAD AND CLASSIFY ROLES

Glob `.craft/roles/`. Produce ROLES-LOADED:

  ROLES-LOADED:
  - [role name] -- [one-line description from role file]

If no files found:
  ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] -- [description]

Every role name appearing anywhere in this document must be declared here.

Immediately produce:

  ROLE-LOAD-ORDER:
  Tier 1: Engineering -- complete before writing Tier 2
  Tier 2: Operations  -- complete before writing Tier 3
  Tier 3: PM / Design / Research / Other
  PROHIBITION: No tier may be defined or processed out of this declared sequence.

Then produce ROLE-TYPE-CLASSIFICATION in that tier order:

  ROLE-TYPE-CLASSIFICATION:
  - [role name] -- [domain type]

Domain type closed set: Engineering / PM / Design / Operations / Research / Other
DO NOT proceed until every role is classified.

Then produce ROLE-TIER-ACCOUNTING immediately after ROLE-TYPE-CLASSIFICATION:

  ROLE-TIER-ACCOUNTING:
  - Tier 1 Engineering: [N roles] -- TIER-PRESENT / TIER-ABSENT
  - Tier 2 Operations:  [N roles] -- TIER-PRESENT / TIER-ABSENT
  - Tier 3 Other:       [N roles] -- TIER-PRESENT / TIER-ABSENT

One row per declared tier. TIER-ABSENT required for empty tiers.

Emit: === [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===

---

PHASE 2: INERTIA ASSESSMENT -- FOUR SUB-SECTIONS

Write before any org diagram. You are the advocate for staying flat.

STRUCTURING-COST FRAME -- PRE-ASSESSMENT BLOCK [Zone: PRE-ASSESSMENT]

Before Sub-section 1, emit a labeled STRUCTURING-COST FRAME: block naming:
  - Over-structuring risk: at least one concrete consequence of premature formalization
  - Under-coordination risk: at least one concrete consequence of staying flat too long
The VERDICT (Sub-section 4) must name which risk is dominant as an explicit conclusion.

Sub-section 1 -- Case for Staying Flat

Fill this schema (minimum four columns; Estimated Coordination Cost column required):

  | Mechanism Name                    | Type               | Frequency / Participants      | Estimated Coordination Cost |
  |-----------------------------------|--------------------|-------------------------------|----------------------------|
  | (specific observable mechanism)   | (type value)       | (frequency, participant count)| (cost in eng-weeks/qtr)    |

Type column closed set: Channel / Informal Role / Recurring Cadence / Shared Artifact

COUNT CHECKPOINT:
  MECHANISM-ROW-COUNT: [N] rows.
  TYPE-DIVERSITY: [K of 4] type classes represented.
  If N < 2: add missing rows until N >= 2. Re-emit count.
When count >= 2 AND >= 2 distinct type classes, emit:
  --- [FLAT-CASE-CLOSED: {N} mechanism rows. {K} of 4 type classes. Total cost: [sum]. How We Coordinate Today begins.] ---

Sub-section 2 -- How We Coordinate Today
Describe coordination patterns in practice. Do not repeat Sub-section 1 table entries.

Sub-section 3 -- Rebuttal [Zone: SUB-SECTION-3]

Name the ONE failure mode Sub-section 1 mechanisms cannot resolve. Use a specific observable
with a quantifier (count, duration, date, or dollar magnitude) or a named event.

UNCOVERED: [function or decision class with no current owner under flat structure]

Sub-section 4 -- VERDICT

COST-FRAME CONCLUSION:
First line in Sub-section 4 before NET-COST-COMPARISON. Names STRUCTURING-COST FRAME: block,
cites dominant error risk, names >= 1 sub-section as evidence source.
CROSS-REF-REQUIRED (1 of 2): NO interceding content -- see anchor ordering above

NET-COST-COMPARISON:
  Flat coordination cost:    [total from FLAT-CASE-CLOSED]
  Structure overhead:        [meeting load + charter maintenance + escalation delay]
  Net delta:                 [signed delta]
  ADDITIVE-TO: C-01 FLAT-CASE-PRESSURE
CROSS-REF-REQUIRED (2 of 2): NO interceding content -- see anchor ordering above

FLAT-CASE-PRESSURE: [rating] -- [one sentence: mechanism count + cost anchor + named failure mode]
Rating closed set: Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)

Declare: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED (must follow from sign of net delta)

VERDICT-GATE CHECKLIST:
- [ ] COST-FRAME CONCLUSION: appears before NET-COST-COMPARISON, no interceding content
      (NET-COST-COMPARISON: immediately follows COST-FRAME CONCLUSION: -- per SUB-SECTION-4-ANCHOR-SEQUENCE)
- [ ] NET-COST-COMPARISON: closes before FLAT-CASE-PRESSURE:, no interceding content
      (FLAT-CASE-PRESSURE: immediately follows NET-COST-COMPARISON: close -- per SUB-SECTION-4-ANCHOR-SEQUENCE)

RE-ASSESSMENT TRIGGER: concrete measurable threshold in cost units.

INTEGRATION-NOTE:
  STRUCTURING-COST FRAME:       [Zone: PRE-ASSESSMENT]
  UNCOVERED: citation:          [Zone: SUB-SECTION-3]
  Flat rhythm table (if CAN):   [Zone: POST-VERDICT-BRANCH]
  Disjointness confirmed.

ZONE-NOTATION RULE:
Bracket form [Zone: X] required. Prohibited parenthetical forms:
  - (PRE-ASSESSMENT)
  - (SUB-SECTION-3)
  - (POST-VERDICT-BRANCH)

ZONE-LABEL-TRACEABILITY:
  | Artifact                     | Inline [Zone: X]            | INTEGRATION-NOTE designator | Verdict |
  |------------------------------|-----------------------------|-----------------------------|---------|
  | STRUCTURING-COST FRAME:      | [Zone: PRE-ASSESSMENT]      | PRE-ASSESSMENT              | MATCH   |
  | UNCOVERED: citation          | [Zone: SUB-SECTION-3]       | SUB-SECTION-3               | MATCH   |
  | Flat rhythm table            | [Zone: POST-VERDICT-BRANCH] | POST-VERDICT-BRANCH         | MATCH   |

---

FLAT-VERDICT BRANCH -- ABSENT LABELING

IF VERDICT = CAN-OPERATE-FLAT:

    ### ASCII Org Diagram -- ABSENT
    REASON: CAN-OPERATE-FLAT verdict. Formal hierarchy is not warranted.
    PROHIBITED ALTERNATIVE: simplified hierarchy and compact org chart both require STRUCTURE-WARRANTED.
    Remaining sections also ABSENT: Headcount by Area, HEADCOUNT-AREA-SUM, HEADCOUNT-SUM-GATE,
    GATE-CONDITION-MET, Operating Rhythm Table, RHYTHM-DRI-COLUMN-CONTRACT, RHYTHM-DRI-ROLE-CHECK,
    RHYTHM-DRI-ASSIGNMENT-COVERAGE, Committee Charters, CHARTER-AUDIT-ORDER,
    CHARTER-COMPLETENESS-AUDIT, RHYTHM-CHARTER-NAME-AUDIT, ORG-ELEMENT REGISTER,
    Org Evolution Roadmap, Anti-Pattern Watch.

    ONE affirmative investment action for the flat state [Zone: POST-VERDICT-BRANCH].

  End artifact: Generated by: /org-chart {topic} -- {date}

IF VERDICT = STRUCTURE-WARRANTED: emit gate and continue.

Emit: === [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===

---

PHASE 3: ASCII ORG DIAGRAM

Draw after the gate using box-drawing characters (+, -, |).
  - Minimum THREE hierarchy levels
  - Committees as distinct nodes -- not inside area boxes
  - Every committee node name must match its charter header exactly
  - All role names from ROLES-LOADED or ROLES-NOTE only

Emit: === [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===

---

PHASE 4: HEADCOUNT BY AREA

  | Area     | Headcount | Key Roles                  | Decides          | Escalates          | ANNOTATION-REGISTER |
  |----------|-----------|----------------------------|------------------|--------------------|---------------------|
  | (area 1) | N         | [role] (Engineering)       | (CF-12 ref)      | (types) -> [dest.] | --                  |
  | (area 2) | N         | [role] (PM)                | (CF-07 ref)      | does not decide [X]; escalates [Y] -> [dest.] | -- |
  | **Total**| N         |                            |                  |                    |                     |

At least two area rows + Total. >= 2 Decides entries with CF-coded references. >= 1 exclusion clause.

HEADCOUNT-AREA-SUM:
  - [area 1 name]: [N1]
  - [area 2 name]: [N2]
  SUM: [N1] + [N2] + ... = [computed total]
  Total claimed in table: [Total row value]
  VERDICT: SUM-VERIFIED / SUM-MISMATCH

On SUM-MISMATCH: correct the table, re-emit the corrected table and HEADCOUNT-AREA-SUM block,
confirm SUM-VERIFIED, then continue.

HEADCOUNT-SUM-GATE:                    <-- A-40 (departure site)
  Gate condition:  SUM-VERIFIED (from HEADCOUNT-AREA-SUM above)
  Gated section:   Operating Rhythm Table
  SUM-MISMATCH blocks this gate -- the Operating Rhythm Table must not appear
  until SUM-MISMATCH is resolved and SUM-VERIFIED is confirmed.

---

PHASE 5: OPERATING RHYTHM TABLE

GATE-CONDITION-MET: SUM-VERIFIED      <-- A-43 (arrival acknowledgment) / A-46 (three-field signature)
  SOURCE-GATE: HEADCOUNT-SUM-GATE (declared in Phase 4 above)
  GATE-VERDICT: SUM-VERIFIED
  ARRIVAL-COUNTERPART: Operating Rhythm Table

RHYTHM-DRI-COLUMN-CONTRACT:            <-- A-42
  DRI-COLUMN-PRESENT: The operating rhythm table includes a DRI / Owner column.
  Row types requiring DRI assignment:
    - Shiproom / gate meeting rows: DRI REQUIRED
    - Governance meeting rows: DRI REQUIRED
    - ROB rows: DRI REQUIRED
  Any DRI/Owner value must be traceable to a role declared in ROLE-TYPE-CLASSIFICATION.
  An empty DRI cell for a DRI REQUIRED row type is a constraint violation.

Produce cadence table: Cadence | Frequency | DRI / Owner | Purpose.
Minimum three rows: one ROB, one shiproom/gate, one governance.
Include explicit entry/exit criteria or decision gate in >= 1 row.

RHYTHM-DRI-ROLE-CHECK:                 <-- A-39
  - [Cadence row] -- DRI: [value] -- traces to [ROLE-TYPE-CLASSIFICATION entry] -- ROLE-VERIFIED / ROLE-UNVERIFIED

One row per DRI/Owner assignment. ROLE-UNVERIFIED is a constraint violation.

RHYTHM-DRI-ASSIGNMENT-COVERAGE:        <-- A-45 (no DRI-COVERAGE-GATE -- A-48 ABSENT)
  One row per row type declared as DRI REQUIRED in RHYTHM-DRI-COLUMN-CONTRACT above.
  - ROB rows: DRI-ASSIGNED (DRI = [role name]) / DRI-MISSING
  - Shiproom / gate meeting rows: DRI-ASSIGNED (DRI = [role name]) / DRI-MISSING
  - Governance meeting rows: DRI-ASSIGNED (DRI = [role name]) / DRI-MISSING
  DRI-MISSING is a constraint violation.

---

PHASE 6: COMMITTEE CHARTERS

Write a charter for each governance meeting in prose-paragraph format (bold labels):
  **Purpose:** ...
  **Membership:** [role] ([type]), [role] ([type]) (>= 2 roles)
  **Decides:** ...
  **Escalates:** ... (named destination)
  **Dissolves When:** [specific, observable, independently verifiable condition]
  QUORUM-DENOMINATOR CONSTRAINT: M = [count of Membership roles]
  **Quorum:** [N] of [M] member roles required for binding decisions

CHARTER-AUDIT-ORDER:                   <-- A-41 + A-44 (cardinality declared; no A-47 back-ref in ordinal labels)
  Required sequence: CHARTER-COMPLETENESS-AUDIT first, then RHYTHM-CHARTER-NAME-AUDIT second.
  PROHIBITION: No content may appear between CHARTER-COMPLETENESS-AUDIT and
  RHYTHM-CHARTER-NAME-AUDIT once CHARTER-COMPLETENESS-AUDIT opens.
  AUDIT-CHAIN-CARDINALITY: 2 blocks
  Block 1: CHARTER-COMPLETENESS-AUDIT
  Block 2: RHYTHM-CHARTER-NAME-AUDIT
  Both audit blocks must carry: (a) backward reference to this CHARTER-AUDIT-ORDER declaration,
  (b) ordinal label in the form AUDIT-BLOCK (N of 2).

CHARTER-COMPLETENESS-AUDIT: [AUDIT-BLOCK (1 of 2) -- governed by CHARTER-AUDIT-ORDER above]

  | Charter | Purpose | Membership | Decides | Escalates | Quorum | Dissolves When | QUORUM-DENOMINATOR CONSTRAINT |
  |---------|---------|------------|---------|-----------|--------|----------------|-------------------------------|
  | [name]  | PRESENT | PRESENT    | PRESENT | PRESENT   | PRESENT| PRESENT        | PRESENT                       |

  Any MISSING cell blocks the gate.

RHYTHM-CHARTER-NAME-AUDIT: [AUDIT-BLOCK (2 of 2) -- governed by CHARTER-AUDIT-ORDER above]

  | Rhythm Table Label | Charter Header Name | Verdict                    |
  |--------------------|---------------------|----------------------------|
  | [governance row]   | [charter header]    | NAME-MATCH / NAME-MISMATCH |

  NAME-MISMATCH blocks the gate.

Emit: === [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===

---

PHASE 7: ORG-ELEMENT REGISTER

REGISTER-CATEGORY-CONTRACT:
  - cat-1 (Areas)
  - cat-2 (Committees/Cadences)
  - cat-3 (Headcount)
  - cat-4 (DRI Roles)

ORG-ELEMENT REGISTER:
  cat-1 (Areas): - [area] -- headcount: [N]
  cat-2 (Committees/Cadences): - [name]
  cat-3 (Headcount): - Total headcount: [N]
  cat-4 (DRI Roles): - [DRI role]

REGISTER-POPULATION-AUDIT:
  - cat-1: [N] -- CATEGORY-POPULATED / CATEGORY-EMPTY
  - cat-2: [N] -- CATEGORY-POPULATED / CATEGORY-EMPTY
  - cat-3: [N] -- CATEGORY-POPULATED / CATEGORY-EMPTY
  - cat-4: [N] -- CATEGORY-POPULATED / CATEGORY-EMPTY

---

PHASE 8: ORG EVOLUTION ROADMAP

COST-DELTA CALIBRATION:
  Net delta: [from NET-COST-COMPARISON]
  CALIBRATION-ANCHOR: Capacity-High
  CALIBRATION-ANCHOR: Process-Medium
  CALIBRATION-ANCHOR: Strategic-Low

Trigger table: Trigger | Structural Change | Type | Observable Signal | Probability Weight
>= 2 rows, >= 2 distinct trigger types. Row 1: headcount threshold. Row 2: different category.
Probability Weight cells reference CALIBRATION-ANCHOR values.

WATCH-FIRST: [Observable Signal from most-likely-next tier]

ROADMAP-TRIGGER-DIVERSITY:
  [Row 1] -- [Signal] -- [Type: Capacity/Process/Strategic/Structural]
  [Row 2] -- [Signal] -- [Type]
  Trigger type diversity: [N] distinct types ([list])

---

PHASE 9: ANTI-PATTERN WATCH

Table: Anti-Pattern | Why It Applies Here | Mitigation
Each Why It Applies Here cell: [element name] (cat-N) -- [one sentence]
Minimum two rows.

---

SECTION ORDER (V-01 -- A-46 only)

1.  ROLES-LOADED or ROLES-NOTE
2.  ROLE-LOAD-ORDER:
3.  ROLE-TYPE-CLASSIFICATION:
4.  ROLE-TIER-ACCOUNTING:
5.  === [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===
6.  STRUCTURING-COST FRAME: [Zone: PRE-ASSESSMENT]
7.  Inertia Assessment (FLAT-CASE-CLOSED / UNCOVERED: / COST-FRAME CONCLUSION: /
    NET-COST-COMPARISON: / CROSS-REF-REQUIRED (1 of 2) and (2 of 2) / FLAT-CASE-PRESSURE: /
    verdict / VERDICT-GATE CHECKLIST / re-assessment trigger / INTEGRATION-NOTE /
    ZONE-NOTATION RULE / ZONE-LABEL-TRACEABILITY)
8.  === [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===
9.  ASCII Org Diagram (box-drawing, >= 3 levels, committee names match charters)
10. === [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===
11. Headcount by Area (CF-coded Decides, exclusion clause, ANNOTATION-REGISTER)
12. HEADCOUNT-AREA-SUM:
13. HEADCOUNT-SUM-GATE:                     <-- A-40 (departure site)
13a. GATE-CONDITION-MET: SUM-VERIFIED        <-- A-43 + A-46 (three-field: SOURCE-GATE / GATE-VERDICT / ARRIVAL-COUNTERPART)
13b. RHYTHM-DRI-COLUMN-CONTRACT:             <-- A-42 (pre-table DRI contract)
14. Operating Rhythm Table (DRI/Owner column)
15. RHYTHM-DRI-ROLE-CHECK:                   (A-39)
15a. RHYTHM-DRI-ASSIGNMENT-COVERAGE:         <-- A-45 (no DRI-COVERAGE-GATE -- A-48 ABSENT)
16. Committee Charters (prose, 7 fields, QUORUM-DENOMINATOR CONSTRAINT)
16a. CHARTER-AUDIT-ORDER:                    <-- A-41 + A-44 (AUDIT-CHAIN-CARDINALITY: 2 blocks; ordinal labels without A-47 back-ref)
17. CHARTER-COMPLETENESS-AUDIT:              [AUDIT-BLOCK (1 of 2)]  (no cardinality-source back-ref -- A-47 ABSENT)
18. RHYTHM-CHARTER-NAME-AUDIT:               [AUDIT-BLOCK (2 of 2)]  (no cardinality-source back-ref -- A-47 ABSENT)
19. === [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===
20. REGISTER-CATEGORY-CONTRACT:
21. ORG-ELEMENT REGISTER
22. REGISTER-POPULATION-AUDIT:
23. COST-DELTA CALIBRATION:
24. Org Evolution Roadmap (WATCH-FIRST, CALIBRATION-ANCHOR references)
25. ROADMAP-TRIGGER-DIVERSITY:
26. Anti-Pattern Watch

End with: Generated by: /org-chart {topic} -- {date}

---

## V-02: Audit-Block Cardinality-Source Back-Reference (A-47 only)

**Axis:** Each AUDIT-BLOCK ordinal label gains an explicit cardinality-source back-reference
to the specific `AUDIT-CHAIN-CARDINALITY:` line declared in CHARTER-AUDIT-ORDER. The label
format becomes `[AUDIT-BLOCK (N of 2) -- cardinality-source: AUDIT-CHAIN-CARDINALITY: 2 blocks
per CHARTER-AUDIT-ORDER above]` on both audit blocks.
**Hypothesis:** CHARTER-AUDIT-ORDER (A-41) declares the ordering; AUDIT-CHAIN-CARDINALITY (A-44)
declares the count; each block carries an (N of 2) ordinal label. But the ordinal assertion is
self-certified: a reader seeing "(1 of 2)" cannot, from the label alone, confirm that "2" derives
from the AUDIT-CHAIN-CARDINALITY declaration rather than from inline authorial judgment. Adding
an explicit cardinality-source back-reference to each ordinal label -- citing the specific
AUDIT-CHAIN-CARDINALITY line and its parent block -- converts the ordinal into a traceable
claim: the count is declared at one site and certified at each usage site.

---

You are running `/org-chart {topic}`.

DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.

Formal org structure is not the answer -- it is the proposal. Informal coordination
(channels, standups, de-facto leads, shared documents) is the status quo you are
trying to displace. Do not draw an org box until you have argued the case for staying
flat and found the specific failure mode it cannot answer.

---

PHASES 1-4: [identical to V-01, including HEADCOUNT-AREA-SUM and HEADCOUNT-SUM-GATE;
NO three-field GATE-CONDITION-MET -- A-46 ABSENT]

PHASE 5: OPERATING RHYTHM TABLE

GATE-CONDITION-MET: SUM-VERIFIED      <-- A-43 (arrival acknowledgment; no three-field signature -- A-46 ABSENT)
  Source: HEADCOUNT-SUM-GATE declared above (Phase 4)
  HEADCOUNT-AREA-SUM verdict = SUM-VERIFIED
  This block is the arrival-site counterpart to the HEADCOUNT-SUM-GATE departure-site declaration.
  Operating Rhythm Table proceeds.

RHYTHM-DRI-COLUMN-CONTRACT:
[identical to V-01 RHYTHM-DRI-COLUMN-CONTRACT block]

Produce cadence table: Cadence | Frequency | DRI / Owner | Purpose.
Minimum three rows: one ROB, one shiproom/gate, one governance.
Include explicit entry/exit criteria or decision gate in >= 1 row.

RHYTHM-DRI-ROLE-CHECK:
[identical to V-01 RHYTHM-DRI-ROLE-CHECK block]

RHYTHM-DRI-ASSIGNMENT-COVERAGE:        <-- A-45 (no DRI-COVERAGE-GATE -- A-48 ABSENT)
[identical to V-01 RHYTHM-DRI-ASSIGNMENT-COVERAGE block]

---

PHASE 6: COMMITTEE CHARTERS

Write a charter for each governance meeting in prose-paragraph format (bold labels):
[identical charter format to V-01: 7 fields, QUORUM-DENOMINATOR CONSTRAINT, N-of-M Quorum]

CHARTER-AUDIT-ORDER:                   <-- A-41 + A-44 + A-47 (cardinality-source back-ref on both blocks)

  CHARTER-AUDIT-ORDER:
  Required sequence: CHARTER-COMPLETENESS-AUDIT first, then RHYTHM-CHARTER-NAME-AUDIT second.
  PROHIBITION: No content may appear between CHARTER-COMPLETENESS-AUDIT and
  RHYTHM-CHARTER-NAME-AUDIT once CHARTER-COMPLETENESS-AUDIT opens.
  AUDIT-CHAIN-CARDINALITY: 2 blocks        <-- count declaration; each ordinal label below traces here
  Block 1: CHARTER-COMPLETENESS-AUDIT
  Block 2: RHYTHM-CHARTER-NAME-AUDIT
  Both audit blocks must carry: (a) backward reference to this CHARTER-AUDIT-ORDER declaration,
  (b) ordinal label in the form AUDIT-BLOCK (N of 2) with explicit cardinality-source back-reference.

CHARTER-COMPLETENESS-AUDIT: [AUDIT-BLOCK (1 of 2) -- cardinality-source: AUDIT-CHAIN-CARDINALITY: 2 blocks per CHARTER-AUDIT-ORDER above]

  | Charter | Purpose | Membership | Decides | Escalates | Quorum | Dissolves When | QUORUM-DENOMINATOR CONSTRAINT |
  |---------|---------|------------|---------|-----------|--------|----------------|-------------------------------|
  | [name]  | PRESENT | PRESENT    | PRESENT | PRESENT   | PRESENT| PRESENT        | PRESENT                       |

  Any MISSING cell blocks the gate.

RHYTHM-CHARTER-NAME-AUDIT: [AUDIT-BLOCK (2 of 2) -- cardinality-source: AUDIT-CHAIN-CARDINALITY: 2 blocks per CHARTER-AUDIT-ORDER above]

  | Rhythm Table Label | Charter Header Name | Verdict                    |
  |--------------------|---------------------|----------------------------|
  | [governance row]   | [charter header]    | NAME-MATCH / NAME-MISMATCH |

  NAME-MISMATCH blocks the gate.

Emit: === [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===

PHASES 7-9: [identical to V-01]

FLAT-VERDICT BRANCH -- ABSENT LABELING

IF VERDICT = CAN-OPERATE-FLAT:
  Remaining sections also ABSENT: Headcount by Area, HEADCOUNT-AREA-SUM, HEADCOUNT-SUM-GATE,
  GATE-CONDITION-MET, Operating Rhythm Table, RHYTHM-DRI-COLUMN-CONTRACT, RHYTHM-DRI-ROLE-CHECK,
  RHYTHM-DRI-ASSIGNMENT-COVERAGE, Committee Charters, CHARTER-AUDIT-ORDER,
  CHARTER-COMPLETENESS-AUDIT, RHYTHM-CHARTER-NAME-AUDIT, ORG-ELEMENT REGISTER,
  Org Evolution Roadmap, Anti-Pattern Watch.
  ONE affirmative investment action [Zone: POST-VERDICT-BRANCH].
  End artifact: Generated by: /org-chart {topic} -- {date}

IF VERDICT = STRUCTURE-WARRANTED: emit gate and continue.

SECTION ORDER (V-02 -- A-47 only)

1-12. [identical to V-01 steps 1-12]
13. HEADCOUNT-SUM-GATE:                      (A-40)
13a. GATE-CONDITION-MET: SUM-VERIFIED        (A-43 prose form -- A-46 ABSENT)
13b. RHYTHM-DRI-COLUMN-CONTRACT:             (A-42)
14. Operating Rhythm Table
15. RHYTHM-DRI-ROLE-CHECK:
15a. RHYTHM-DRI-ASSIGNMENT-COVERAGE:         (A-45, no DRI-COVERAGE-GATE -- A-48 ABSENT)
16. Committee Charters
16a. CHARTER-AUDIT-ORDER:                    (A-41 + A-44 + A-47: AUDIT-CHAIN-CARDINALITY: 2 blocks; cardinality-source back-ref on both ordinal labels)
17. CHARTER-COMPLETENESS-AUDIT:              [AUDIT-BLOCK (1 of 2) -- cardinality-source: AUDIT-CHAIN-CARDINALITY: 2 blocks per CHARTER-AUDIT-ORDER above]  <-- A-47
18. RHYTHM-CHARTER-NAME-AUDIT:               [AUDIT-BLOCK (2 of 2) -- cardinality-source: AUDIT-CHAIN-CARDINALITY: 2 blocks per CHARTER-AUDIT-ORDER above]  <-- A-47
19-26. [identical to V-01 steps 19-26]

End with: Generated by: /org-chart {topic} -- {date}

---

## V-03: DRI Coverage Constraint-Gate Declaration (A-48 only)

**Axis:** Add a `DRI-COVERAGE-GATE:` block inside `RHYTHM-DRI-ASSIGNMENT-COVERAGE`, naming the
gated section and the blocker. The gate follows the A-40 HEADCOUNT-SUM-GATE structural pattern:
it names a gate condition, the gated section, and the blocker inline within the enforcement block.
**Hypothesis:** RHYTHM-DRI-ASSIGNMENT-COVERAGE (A-45) declares DRI-MISSING a constraint violation
but does not name what is blocked. A reader sees the violation label but must consult the rubric
to know the consequence. Following the A-40/A-35 constraint-gate naming pattern, the enforcement
block must itself name the gated section and the blocker -- making the consequence independently
readable at the enforcement site. The DRI-COVERAGE-GATE sub-block converts a prose constraint
statement into a first-class gate declaration with independently verifiable fields.

---

You are running `/org-chart {topic}`.

DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.

Formal org structure is not the answer -- it is the proposal. Informal coordination
(channels, standups, de-facto leads, shared documents) is the status quo you are
trying to displace. Do not draw an org box until you have argued the case for staying
flat and found the specific failure mode it cannot answer.

---

PHASES 1-4: [identical to V-01, including HEADCOUNT-AREA-SUM and HEADCOUNT-SUM-GATE;
NO three-field GATE-CONDITION-MET -- A-46 ABSENT]

PHASE 5: OPERATING RHYTHM TABLE

GATE-CONDITION-MET: SUM-VERIFIED      <-- A-43 (arrival acknowledgment; no three-field signature -- A-46 ABSENT)
  Source: HEADCOUNT-SUM-GATE declared above (Phase 4)
  HEADCOUNT-AREA-SUM verdict = SUM-VERIFIED
  This block is the arrival-site counterpart to the HEADCOUNT-SUM-GATE departure-site declaration.
  Operating Rhythm Table proceeds.

RHYTHM-DRI-COLUMN-CONTRACT:
[identical to V-01 RHYTHM-DRI-COLUMN-CONTRACT block]

Produce cadence table: Cadence | Frequency | DRI / Owner | Purpose.
Minimum three rows: one ROB, one shiproom/gate, one governance.
Include explicit entry/exit criteria or decision gate in >= 1 row.

RHYTHM-DRI-ROLE-CHECK:
[identical to V-01 RHYTHM-DRI-ROLE-CHECK block]

RHYTHM-DRI-ASSIGNMENT-COVERAGE:        <-- A-45 + A-48 (DRI-COVERAGE-GATE added)
  One row per row type declared as DRI REQUIRED in RHYTHM-DRI-COLUMN-CONTRACT above.
  - ROB rows: DRI-ASSIGNED (DRI = [role name]) / DRI-MISSING
  - Shiproom / gate meeting rows: DRI-ASSIGNED (DRI = [role name]) / DRI-MISSING
  - Governance meeting rows: DRI-ASSIGNED (DRI = [role name]) / DRI-MISSING

  DRI-COVERAGE-GATE:                   <-- A-48 (constraint-gate declaration)
    Gate condition:  All DRI REQUIRED row types emit DRI-ASSIGNED
    Gated section:   Operating Rhythm Table section completion
    DRI-MISSING blocks this gate -- the Operating Rhythm Table section is NOT COMPLETE
    until every DRI REQUIRED row type emits DRI-ASSIGNED.

---

PHASE 6: COMMITTEE CHARTERS

[identical to V-01 Phase 6 -- CHARTER-AUDIT-ORDER with AUDIT-CHAIN-CARDINALITY: 2 blocks;
audit blocks carry (N of 2) ordinal labels without cardinality-source back-ref -- A-47 ABSENT]

PHASES 7-9: [identical to V-01]

FLAT-VERDICT BRANCH -- ABSENT LABELING

IF VERDICT = CAN-OPERATE-FLAT:
  Remaining sections also ABSENT: Headcount by Area, HEADCOUNT-AREA-SUM, HEADCOUNT-SUM-GATE,
  GATE-CONDITION-MET, Operating Rhythm Table, RHYTHM-DRI-COLUMN-CONTRACT, RHYTHM-DRI-ROLE-CHECK,
  RHYTHM-DRI-ASSIGNMENT-COVERAGE, DRI-COVERAGE-GATE, Committee Charters, CHARTER-AUDIT-ORDER,
  CHARTER-COMPLETENESS-AUDIT, RHYTHM-CHARTER-NAME-AUDIT, ORG-ELEMENT REGISTER,
  Org Evolution Roadmap, Anti-Pattern Watch.
  ONE affirmative investment action [Zone: POST-VERDICT-BRANCH].
  End artifact: Generated by: /org-chart {topic} -- {date}

IF VERDICT = STRUCTURE-WARRANTED: emit gate and continue.

SECTION ORDER (V-03 -- A-48 only)

1-12. [identical to V-01 steps 1-12]
13. HEADCOUNT-SUM-GATE:                      (A-40)
13a. GATE-CONDITION-MET: SUM-VERIFIED        (A-43 prose form -- A-46 ABSENT)
13b. RHYTHM-DRI-COLUMN-CONTRACT:             (A-42)
14. Operating Rhythm Table
15. RHYTHM-DRI-ROLE-CHECK:
15a. RHYTHM-DRI-ASSIGNMENT-COVERAGE:         (A-45)
15b.   DRI-COVERAGE-GATE:                    <-- A-48 (inside RHYTHM-DRI-ASSIGNMENT-COVERAGE)
16. Committee Charters
16a. CHARTER-AUDIT-ORDER:                    (A-41 + A-44: AUDIT-CHAIN-CARDINALITY: 2 blocks; ordinal labels without A-47 back-ref)
17. CHARTER-COMPLETENESS-AUDIT:              [AUDIT-BLOCK (1 of 2)] (no cardinality-source back-ref -- A-47 ABSENT)
18. RHYTHM-CHARTER-NAME-AUDIT:               [AUDIT-BLOCK (2 of 2)] (no cardinality-source back-ref -- A-47 ABSENT)
19-26. [identical to V-01 steps 19-26]

End with: Generated by: /org-chart {topic} -- {date}

---

## V-04: A-46 + A-47 Combined (Three-Field Gate Signature + Cardinality-Source Back-Reference)

**Axis:** GATE-CONDITION-MET three-field signature (A-46) and AUDIT-BLOCK cardinality-source
back-reference (A-47) together, without the DRI-COVERAGE-GATE (A-48 absent).
**Hypothesis:** A-46 and A-47 address structurally independent regions -- Phase 5 entry
vs. Phase 6 audit chain ordinal labels -- with no shared state or dependency. Testing them
together without A-48 validates that the two back-reference patterns compose without
ambiguity, and confirms that the three-field gate block and the cardinality-source label
augmentation are independently additive to the R19-V-05 baseline.

---

You are running `/org-chart {topic}`.

DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.

Formal org structure is not the answer -- it is the proposal. Informal coordination
(channels, standups, de-facto leads, shared documents) is the status quo you are
trying to displace. Do not draw an org box until you have argued the case for staying
flat and found the specific failure mode it cannot answer.

---

PHASES 1-4: [identical to V-01, including HEADCOUNT-AREA-SUM and HEADCOUNT-SUM-GATE]

PHASE 5: OPERATING RHYTHM TABLE

GATE-CONDITION-MET: SUM-VERIFIED      <-- A-43 + A-46 (three-field signature present)
  SOURCE-GATE: HEADCOUNT-SUM-GATE (declared in Phase 4 above)
  GATE-VERDICT: SUM-VERIFIED
  ARRIVAL-COUNTERPART: Operating Rhythm Table

RHYTHM-DRI-COLUMN-CONTRACT:
[identical to V-01 RHYTHM-DRI-COLUMN-CONTRACT block]

Produce cadence table: Cadence | Frequency | DRI / Owner | Purpose.
Minimum three rows: one ROB, one shiproom/gate, one governance.
Include explicit entry/exit criteria or decision gate in >= 1 row.

RHYTHM-DRI-ROLE-CHECK:
[identical to V-01 RHYTHM-DRI-ROLE-CHECK block]

RHYTHM-DRI-ASSIGNMENT-COVERAGE:        <-- A-45 (no DRI-COVERAGE-GATE -- A-48 ABSENT)
[identical to V-01 RHYTHM-DRI-ASSIGNMENT-COVERAGE block, without DRI-COVERAGE-GATE]

---

PHASE 6: COMMITTEE CHARTERS

Write a charter for each governance meeting in prose-paragraph format (bold labels):
[identical charter format to V-01: 7 fields, QUORUM-DENOMINATOR CONSTRAINT, N-of-M Quorum]

CHARTER-AUDIT-ORDER:                   <-- A-41 + A-44 + A-47 (cardinality-source back-ref on both blocks)

  CHARTER-AUDIT-ORDER:
  Required sequence: CHARTER-COMPLETENESS-AUDIT first, then RHYTHM-CHARTER-NAME-AUDIT second.
  PROHIBITION: No content may appear between CHARTER-COMPLETENESS-AUDIT and
  RHYTHM-CHARTER-NAME-AUDIT once CHARTER-COMPLETENESS-AUDIT opens.
  AUDIT-CHAIN-CARDINALITY: 2 blocks        <-- count declaration; each ordinal label below traces here
  Block 1: CHARTER-COMPLETENESS-AUDIT
  Block 2: RHYTHM-CHARTER-NAME-AUDIT
  Both audit blocks must carry: (a) backward reference to this CHARTER-AUDIT-ORDER declaration,
  (b) ordinal label in the form AUDIT-BLOCK (N of 2) with explicit cardinality-source back-reference.

CHARTER-COMPLETENESS-AUDIT: [AUDIT-BLOCK (1 of 2) -- cardinality-source: AUDIT-CHAIN-CARDINALITY: 2 blocks per CHARTER-AUDIT-ORDER above]

  | Charter | Purpose | Membership | Decides | Escalates | Quorum | Dissolves When | QUORUM-DENOMINATOR CONSTRAINT |
  |---------|---------|------------|---------|-----------|--------|----------------|-------------------------------|
  | [name]  | PRESENT | PRESENT    | PRESENT | PRESENT   | PRESENT| PRESENT        | PRESENT                       |

  Any MISSING cell blocks the gate.

RHYTHM-CHARTER-NAME-AUDIT: [AUDIT-BLOCK (2 of 2) -- cardinality-source: AUDIT-CHAIN-CARDINALITY: 2 blocks per CHARTER-AUDIT-ORDER above]

  | Rhythm Table Label | Charter Header Name | Verdict                    |
  |--------------------|---------------------|----------------------------|
  | [governance row]   | [charter header]    | NAME-MATCH / NAME-MISMATCH |

  NAME-MISMATCH blocks the gate.

Emit: === [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===

PHASES 7-9: [identical to V-01]

FLAT-VERDICT BRANCH -- ABSENT LABELING

IF VERDICT = CAN-OPERATE-FLAT:
  Remaining sections also ABSENT: Headcount by Area, HEADCOUNT-AREA-SUM, HEADCOUNT-SUM-GATE,
  GATE-CONDITION-MET, Operating Rhythm Table, RHYTHM-DRI-COLUMN-CONTRACT, RHYTHM-DRI-ROLE-CHECK,
  RHYTHM-DRI-ASSIGNMENT-COVERAGE, Committee Charters, CHARTER-AUDIT-ORDER,
  CHARTER-COMPLETENESS-AUDIT, RHYTHM-CHARTER-NAME-AUDIT, ORG-ELEMENT REGISTER,
  Org Evolution Roadmap, Anti-Pattern Watch.
  ONE affirmative investment action [Zone: POST-VERDICT-BRANCH].
  End artifact: Generated by: /org-chart {topic} -- {date}

IF VERDICT = STRUCTURE-WARRANTED: emit gate and continue.

SECTION ORDER (V-04 -- A-46 + A-47)

1-12. [identical to V-01 steps 1-12]
13. HEADCOUNT-SUM-GATE:                      <-- A-40 (departure site)
13a. GATE-CONDITION-MET: SUM-VERIFIED        <-- A-43 + A-46 (three-field: SOURCE-GATE / GATE-VERDICT / ARRIVAL-COUNTERPART)
13b. RHYTHM-DRI-COLUMN-CONTRACT:             (A-42)
14. Operating Rhythm Table
15. RHYTHM-DRI-ROLE-CHECK:
15a. RHYTHM-DRI-ASSIGNMENT-COVERAGE:         (A-45, no DRI-COVERAGE-GATE -- A-48 ABSENT)
16. Committee Charters
16a. CHARTER-AUDIT-ORDER:                    (A-41 + A-44 + A-47: AUDIT-CHAIN-CARDINALITY + cardinality-source back-ref)
17. CHARTER-COMPLETENESS-AUDIT:              [AUDIT-BLOCK (1 of 2) -- cardinality-source: ...]  <-- A-47
18. RHYTHM-CHARTER-NAME-AUDIT:               [AUDIT-BLOCK (2 of 2) -- cardinality-source: ...]  <-- A-47
19-26. [identical to V-01 steps 19-26]

End with: Generated by: /org-chart {topic} -- {date}

---

## V-05: Full Integration -- A-46 + A-47 + A-48 on R19-V-05 Baseline

**Axis:** All three new blocks layered onto the proven R19-V-05 foundation.
**Hypothesis:** GATE-CONDITION-MET three-field signature (A-46), AUDIT-BLOCK cardinality-source
back-reference (A-47), and DRI-COVERAGE-GATE constraint declaration (A-48) address three
structurally independent insertion points with no shared state: Phase 5 gate acknowledgment
fields / Phase 6 charter audit ordinal labels / Phase 5 post-ROLE-CHECK coverage gate. They
should compose without interference and without regressions against A-01 through A-45. V-05
achieves full 48/48 aspirational coverage and establishes the R20 ceiling.

---

You are running `/org-chart {topic}`.

DEFAULT POSITION: THE TEAM CAN OPERATE FLAT.

Formal org structure is not the answer -- it is the proposal. Informal coordination
(channels, standups, de-facto leads, shared documents) is the status quo you are
trying to displace. Do not draw an org box until you have argued the case for staying
flat and found the specific failure mode it cannot answer.

---

PHASE 1: LOAD AND CLASSIFY ROLES

Glob `.craft/roles/`. Produce ROLES-LOADED:

  ROLES-LOADED:
  - [role name] -- [one-line description from role file]

If no files found:
  ROLES-NOTE: No .craft/roles/ files found. Using inferred roles:
  - [role name] -- [description]

Every role name appearing anywhere in this document must be declared here.

Immediately produce:

  ROLE-LOAD-ORDER:
  Tier 1: Engineering -- complete before writing Tier 2
  Tier 2: Operations  -- complete before writing Tier 3
  Tier 3: PM / Design / Research / Other
  PROHIBITION: No tier may be defined or processed out of this declared sequence.

Then produce ROLE-TYPE-CLASSIFICATION in that tier order:

  ROLE-TYPE-CLASSIFICATION:
  - [role name] -- [domain type]

Domain type closed set: Engineering / PM / Design / Operations / Research / Other
DO NOT proceed until every role is classified.

Then produce ROLE-TIER-ACCOUNTING immediately after ROLE-TYPE-CLASSIFICATION:

  ROLE-TIER-ACCOUNTING:
  - Tier 1 Engineering: [N roles] -- TIER-PRESENT / TIER-ABSENT
  - Tier 2 Operations:  [N roles] -- TIER-PRESENT / TIER-ABSENT
  - Tier 3 Other:       [N roles] -- TIER-PRESENT / TIER-ABSENT

One row per declared tier. TIER-ABSENT required for empty tiers.

Emit: === [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===

---

PHASE 2: INERTIA ASSESSMENT -- FOUR SUB-SECTIONS

Write before any org diagram. You are the advocate for staying flat.

STRUCTURING-COST FRAME -- PRE-ASSESSMENT BLOCK [Zone: PRE-ASSESSMENT]

Before Sub-section 1, emit a labeled STRUCTURING-COST FRAME: block naming:
  - Over-structuring risk: at least one concrete consequence of premature formalization
  - Under-coordination risk: at least one concrete consequence of staying flat too long
The VERDICT (Sub-section 4) must name which risk is dominant as an explicit conclusion.

Sub-section 1 -- Case for Staying Flat

Fill this schema (minimum four columns; Estimated Coordination Cost column required):

  | Mechanism Name                    | Type               | Frequency / Participants      | Estimated Coordination Cost |
  |-----------------------------------|--------------------|-------------------------------|----------------------------|
  | (specific observable mechanism)   | (type value)       | (frequency, participant count)| (cost in eng-weeks/qtr)    |

Type column closed set: Channel / Informal Role / Recurring Cadence / Shared Artifact

COUNT CHECKPOINT:
  MECHANISM-ROW-COUNT: [N] rows.
  TYPE-DIVERSITY: [K of 4] type classes represented.
  If N < 2: add missing rows until N >= 2. Re-emit count.
When count >= 2 AND >= 2 distinct type classes, emit:
  --- [FLAT-CASE-CLOSED: {N} mechanism rows. {K} of 4 type classes. Total cost: [sum]. How We Coordinate Today begins.] ---

Sub-section 2 -- How We Coordinate Today
Describe coordination patterns in practice. Do not repeat Sub-section 1 table entries.

Sub-section 3 -- Rebuttal [Zone: SUB-SECTION-3]

Name the ONE failure mode Sub-section 1 mechanisms cannot resolve. Use a specific observable
with a quantifier (count, duration, date, or dollar magnitude) or a named event.

UNCOVERED: [function or decision class with no current owner under flat structure]

Sub-section 4 -- VERDICT

COST-FRAME CONCLUSION:
First line in Sub-section 4 before NET-COST-COMPARISON. Names STRUCTURING-COST FRAME: block,
cites dominant error risk, names >= 1 sub-section as evidence source.
CROSS-REF-REQUIRED (1 of 2): NO interceding content -- see anchor ordering above

NET-COST-COMPARISON:
  Flat coordination cost:    [total from FLAT-CASE-CLOSED]
  Structure overhead:        [meeting load + charter maintenance + escalation delay]
  Net delta:                 [signed delta]
  ADDITIVE-TO: C-01 FLAT-CASE-PRESSURE
CROSS-REF-REQUIRED (2 of 2): NO interceding content -- see anchor ordering above

FLAT-CASE-PRESSURE: [rating] -- [one sentence: mechanism count + cost anchor + named failure mode]
Rating closed set: Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)

Declare: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED (must follow from sign of net delta)

VERDICT-GATE CHECKLIST:
- [ ] COST-FRAME CONCLUSION: appears before NET-COST-COMPARISON, no interceding content
      (NET-COST-COMPARISON: immediately follows COST-FRAME CONCLUSION: -- per SUB-SECTION-4-ANCHOR-SEQUENCE)
- [ ] NET-COST-COMPARISON: closes before FLAT-CASE-PRESSURE:, no interceding content
      (FLAT-CASE-PRESSURE: immediately follows NET-COST-COMPARISON: close -- per SUB-SECTION-4-ANCHOR-SEQUENCE)

RE-ASSESSMENT TRIGGER: concrete measurable threshold in cost units.

INTEGRATION-NOTE:
  STRUCTURING-COST FRAME:       [Zone: PRE-ASSESSMENT]
  UNCOVERED: citation:          [Zone: SUB-SECTION-3]
  Flat rhythm table (if CAN):   [Zone: POST-VERDICT-BRANCH]
  Disjointness confirmed.

ZONE-NOTATION RULE:
Bracket form [Zone: X] required. Prohibited parenthetical forms:
  - (PRE-ASSESSMENT)
  - (SUB-SECTION-3)
  - (POST-VERDICT-BRANCH)

ZONE-LABEL-TRACEABILITY:
  | Artifact                     | Inline [Zone: X]            | INTEGRATION-NOTE designator | Verdict |
  |------------------------------|-----------------------------|-----------------------------|---------|
  | STRUCTURING-COST FRAME:      | [Zone: PRE-ASSESSMENT]      | PRE-ASSESSMENT              | MATCH   |
  | UNCOVERED: citation          | [Zone: SUB-SECTION-3]       | SUB-SECTION-3               | MATCH   |
  | Flat rhythm table            | [Zone: POST-VERDICT-BRANCH] | POST-VERDICT-BRANCH         | MATCH   |

---

FLAT-VERDICT BRANCH -- ABSENT LABELING

IF VERDICT = CAN-OPERATE-FLAT:

    ### ASCII Org Diagram -- ABSENT
    REASON: CAN-OPERATE-FLAT verdict. Formal hierarchy is not warranted.
    PROHIBITED ALTERNATIVE: simplified hierarchy and compact org chart both require STRUCTURE-WARRANTED.
    Remaining sections also ABSENT: Headcount by Area, HEADCOUNT-AREA-SUM, HEADCOUNT-SUM-GATE,
    GATE-CONDITION-MET, Operating Rhythm Table, RHYTHM-DRI-COLUMN-CONTRACT, RHYTHM-DRI-ROLE-CHECK,
    RHYTHM-DRI-ASSIGNMENT-COVERAGE, DRI-COVERAGE-GATE, Committee Charters, CHARTER-AUDIT-ORDER,
    CHARTER-COMPLETENESS-AUDIT, RHYTHM-CHARTER-NAME-AUDIT, ORG-ELEMENT REGISTER,
    Org Evolution Roadmap, Anti-Pattern Watch.

    ONE affirmative investment action for the flat state [Zone: POST-VERDICT-BRANCH].

  End artifact: Generated by: /org-chart {topic} -- {date}

IF VERDICT = STRUCTURE-WARRANTED: emit gate and continue.

Emit: === [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===

---

PHASE 3: ASCII ORG DIAGRAM

Draw after the gate using box-drawing characters (+, -, |).
  - Minimum THREE hierarchy levels
  - Committees as distinct nodes -- not inside area boxes
  - Every committee node name must match its charter header exactly
  - All role names from ROLES-LOADED or ROLES-NOTE only

Emit: === [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===

---

PHASE 4: HEADCOUNT BY AREA

  | Area     | Headcount | Key Roles                  | Decides          | Escalates          | ANNOTATION-REGISTER |
  |----------|-----------|----------------------------|------------------|--------------------|---------------------|
  | (area 1) | N         | [role] (Engineering)       | (CF-12 ref)      | (types) -> [dest.] | --                  |
  | (area 2) | N         | [role] (PM)                | (CF-07 ref)      | does not decide [X]; escalates [Y] -> [dest.] | -- |
  | **Total**| N         |                            |                  |                    |                     |

At least two area rows + Total. >= 2 Decides entries with CF-coded references. >= 1 exclusion clause.

HEADCOUNT-AREA-SUM:
  - [area 1 name]: [N1]
  - [area 2 name]: [N2]
  SUM: [N1] + [N2] + ... = [computed total]
  Total claimed in table: [Total row value]
  VERDICT: SUM-VERIFIED / SUM-MISMATCH

On SUM-MISMATCH: correct the table, re-emit the corrected table and HEADCOUNT-AREA-SUM block,
confirm SUM-VERIFIED, then continue.

HEADCOUNT-SUM-GATE:                    <-- A-40 (departure site)
  Gate condition:  SUM-VERIFIED (from HEADCOUNT-AREA-SUM above)
  Gated section:   Operating Rhythm Table
  SUM-MISMATCH blocks this gate -- the Operating Rhythm Table must not appear
  until SUM-MISMATCH is resolved and SUM-VERIFIED is confirmed.

---

PHASE 5: OPERATING RHYTHM TABLE

GATE-CONDITION-MET: SUM-VERIFIED      <-- A-43 (arrival acknowledgment) / A-46 (three-field signature)
  SOURCE-GATE: HEADCOUNT-SUM-GATE (declared in Phase 4 above)
  GATE-VERDICT: SUM-VERIFIED
  ARRIVAL-COUNTERPART: Operating Rhythm Table

RHYTHM-DRI-COLUMN-CONTRACT:            <-- A-42
  DRI-COLUMN-PRESENT: The operating rhythm table includes a DRI / Owner column.
  Row types requiring DRI assignment:
    - Shiproom / gate meeting rows: DRI REQUIRED
    - Governance meeting rows: DRI REQUIRED
    - ROB rows: DRI REQUIRED
  Any DRI/Owner value must be traceable to a role declared in ROLE-TYPE-CLASSIFICATION.
  An empty DRI cell for a DRI REQUIRED row type is a constraint violation.

Produce cadence table: Cadence | Frequency | DRI / Owner | Purpose.
Minimum three rows: one ROB, one shiproom/gate, one governance.
Include explicit entry/exit criteria or decision gate in >= 1 row.

RHYTHM-DRI-ROLE-CHECK:                 <-- A-39
  - [Cadence row] -- DRI: [value] -- traces to [ROLE-TYPE-CLASSIFICATION entry] -- ROLE-VERIFIED / ROLE-UNVERIFIED

One row per DRI/Owner assignment. ROLE-UNVERIFIED is a constraint violation.

RHYTHM-DRI-ASSIGNMENT-COVERAGE:        <-- A-45 + A-48 (DRI-COVERAGE-GATE added)
  One row per row type declared as DRI REQUIRED in RHYTHM-DRI-COLUMN-CONTRACT above.
  - ROB rows: DRI-ASSIGNED (DRI = [role name]) / DRI-MISSING
  - Shiproom / gate meeting rows: DRI-ASSIGNED (DRI = [role name]) / DRI-MISSING
  - Governance meeting rows: DRI-ASSIGNED (DRI = [role name]) / DRI-MISSING

  DRI-COVERAGE-GATE:                   <-- A-48 (constraint-gate declaration inside enforcement block)
    Gate condition:  All DRI REQUIRED row types emit DRI-ASSIGNED
    Gated section:   Operating Rhythm Table section completion
    DRI-MISSING blocks this gate -- the Operating Rhythm Table section is NOT COMPLETE
    until every DRI REQUIRED row type emits DRI-ASSIGNED.

---

PHASE 6: COMMITTEE CHARTERS

Write a charter for each governance meeting in prose-paragraph format (bold labels):
  **Purpose:** ...
  **Membership:** [role] ([type]), [role] ([type]) (>= 2 roles)
  **Decides:** ...
  **Escalates:** ... (named destination)
  **Dissolves When:** [specific, observable, independently verifiable condition]
  QUORUM-DENOMINATOR CONSTRAINT: M = [count of Membership roles]
  **Quorum:** [N] of [M] member roles required for binding decisions

CHARTER-AUDIT-ORDER:                   <-- A-41 + A-44 + A-47 (cardinality-source back-ref on both blocks)

  CHARTER-AUDIT-ORDER:
  Required sequence: CHARTER-COMPLETENESS-AUDIT first, then RHYTHM-CHARTER-NAME-AUDIT second.
  PROHIBITION: No content may appear between CHARTER-COMPLETENESS-AUDIT and
  RHYTHM-CHARTER-NAME-AUDIT once CHARTER-COMPLETENESS-AUDIT opens.
  AUDIT-CHAIN-CARDINALITY: 2 blocks        <-- count declaration; each ordinal label below traces here
  Block 1: CHARTER-COMPLETENESS-AUDIT
  Block 2: RHYTHM-CHARTER-NAME-AUDIT
  Both audit blocks must carry: (a) backward reference to this CHARTER-AUDIT-ORDER declaration,
  (b) ordinal label in the form AUDIT-BLOCK (N of 2) with explicit cardinality-source back-reference.

CHARTER-COMPLETENESS-AUDIT: [AUDIT-BLOCK (1 of 2) -- cardinality-source: AUDIT-CHAIN-CARDINALITY: 2 blocks per CHARTER-AUDIT-ORDER above]

  | Charter | Purpose | Membership | Decides | Escalates | Quorum | Dissolves When | QUORUM-DENOMINATOR CONSTRAINT |
  |---------|---------|------------|---------|-----------|--------|----------------|-------------------------------|
  | [name]  | PRESENT | PRESENT    | PRESENT | PRESENT   | PRESENT| PRESENT        | PRESENT                       |

  Any MISSING cell blocks the gate.

RHYTHM-CHARTER-NAME-AUDIT: [AUDIT-BLOCK (2 of 2) -- cardinality-source: AUDIT-CHAIN-CARDINALITY: 2 blocks per CHARTER-AUDIT-ORDER above]

  | Rhythm Table Label | Charter Header Name | Verdict                    |
  |--------------------|---------------------|----------------------------|
  | [governance row]   | [charter header]    | NAME-MATCH / NAME-MISMATCH |

  NAME-MISMATCH blocks the gate.

Emit: === [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===

---

PHASE 7: ORG-ELEMENT REGISTER

REGISTER-CATEGORY-CONTRACT:
  - cat-1 (Areas)
  - cat-2 (Committees/Cadences)
  - cat-3 (Headcount)
  - cat-4 (DRI Roles)

ORG-ELEMENT REGISTER:
  cat-1 (Areas): - [area] -- headcount: [N]
  cat-2 (Committees/Cadences): - [name]
  cat-3 (Headcount): - Total headcount: [N]
  cat-4 (DRI Roles): - [DRI role]

REGISTER-POPULATION-AUDIT:
  - cat-1: [N] -- CATEGORY-POPULATED / CATEGORY-EMPTY
  - cat-2: [N] -- CATEGORY-POPULATED / CATEGORY-EMPTY
  - cat-3: [N] -- CATEGORY-POPULATED / CATEGORY-EMPTY
  - cat-4: [N] -- CATEGORY-POPULATED / CATEGORY-EMPTY

---

PHASE 8: ORG EVOLUTION ROADMAP

COST-DELTA CALIBRATION:
  Net delta: [from NET-COST-COMPARISON]
  CALIBRATION-ANCHOR: Capacity-High
  CALIBRATION-ANCHOR: Process-Medium
  CALIBRATION-ANCHOR: Strategic-Low

Trigger table: Trigger | Structural Change | Type | Observable Signal | Probability Weight
>= 2 rows, >= 2 distinct trigger types. Row 1: headcount threshold. Row 2: different category.
Probability Weight cells reference CALIBRATION-ANCHOR values.

WATCH-FIRST: [Observable Signal from most-likely-next tier]

ROADMAP-TRIGGER-DIVERSITY:
  [Row 1] -- [Signal] -- [Type: Capacity/Process/Strategic/Structural]
  [Row 2] -- [Signal] -- [Type]
  Trigger type diversity: [N] distinct types ([list])

---

PHASE 9: ANTI-PATTERN WATCH

Table: Anti-Pattern | Why It Applies Here | Mitigation
Each Why It Applies Here cell: [element name] (cat-N) -- [one sentence]
Minimum two rows.

---

SECTION ORDER (V-05 -- full A-46/A-47/A-48 integration)

1.  ROLES-LOADED or ROLES-NOTE
2.  ROLE-LOAD-ORDER:
3.  ROLE-TYPE-CLASSIFICATION:
4.  ROLE-TIER-ACCOUNTING:
5.  === [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===
6.  STRUCTURING-COST FRAME: [Zone: PRE-ASSESSMENT]
7.  Inertia Assessment (FLAT-CASE-CLOSED / UNCOVERED: / COST-FRAME CONCLUSION: /
    NET-COST-COMPARISON: / CROSS-REF-REQUIRED (1 of 2) and (2 of 2) / FLAT-CASE-PRESSURE: /
    verdict / VERDICT-GATE CHECKLIST / re-assessment trigger / INTEGRATION-NOTE /
    ZONE-NOTATION RULE / ZONE-LABEL-TRACEABILITY)
8.  === [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===
9.  ASCII Org Diagram (box-drawing, >= 3 levels, committee names match charters)
10. === [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===
11. Headcount by Area (CF-coded Decides, exclusion clause, ANNOTATION-REGISTER)
12. HEADCOUNT-AREA-SUM:
13. HEADCOUNT-SUM-GATE:                     <-- A-40 (departure site)
13a. GATE-CONDITION-MET: SUM-VERIFIED        <-- A-43 + A-46 (three-field: SOURCE-GATE / GATE-VERDICT / ARRIVAL-COUNTERPART)
13b. RHYTHM-DRI-COLUMN-CONTRACT:             <-- A-42 (pre-table DRI contract)
14. Operating Rhythm Table (DRI/Owner column)
15. RHYTHM-DRI-ROLE-CHECK:                   (A-39)
15a. RHYTHM-DRI-ASSIGNMENT-COVERAGE:         <-- A-45
15b.   DRI-COVERAGE-GATE:                    <-- A-48 (inside RHYTHM-DRI-ASSIGNMENT-COVERAGE)
16. Committee Charters (prose, 7 fields, QUORUM-DENOMINATOR CONSTRAINT)
16a. CHARTER-AUDIT-ORDER:                    <-- A-41 + A-44 + A-47 (AUDIT-CHAIN-CARDINALITY: 2 blocks; cardinality-source back-ref on both labels)
17. CHARTER-COMPLETENESS-AUDIT:              [AUDIT-BLOCK (1 of 2) -- cardinality-source: AUDIT-CHAIN-CARDINALITY: 2 blocks per CHARTER-AUDIT-ORDER above]  <-- A-47
18. RHYTHM-CHARTER-NAME-AUDIT:               [AUDIT-BLOCK (2 of 2) -- cardinality-source: AUDIT-CHAIN-CARDINALITY: 2 blocks per CHARTER-AUDIT-ORDER above]  <-- A-47
19. === [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===
20. REGISTER-CATEGORY-CONTRACT:
21. ORG-ELEMENT REGISTER
22. REGISTER-POPULATION-AUDIT:
23. COST-DELTA CALIBRATION:
24. Org Evolution Roadmap (WATCH-FIRST, CALIBRATION-ANCHOR references)
25. ROADMAP-TRIGGER-DIVERSITY:
26. Anti-Pattern Watch

End with: Generated by: /org-chart {topic} -- {date}

---

## Scoring

### Baseline assumptions

All five variations share the same R19-V-05 baseline covering A-01 through A-45. Only A-46/A-47/A-48
differ between variations. The R19-V-05 baseline is presumed to cover all prior criteria; only the
three new criteria are differentiated here.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence note |
|-----------|------|------|------|------|------|---------------|
| A-46      | PASS | FAIL | FAIL | PASS | PASS | GATE-CONDITION-MET with SOURCE-GATE / GATE-VERDICT / ARRIVAL-COUNTERPART fields |
| A-47      | FAIL | PASS | FAIL | PASS | PASS | AUDIT-BLOCK ordinal label cites AUDIT-CHAIN-CARDINALITY source per CHARTER-AUDIT-ORDER |
| A-48      | FAIL | FAIL | PASS | FAIL | PASS | DRI-COVERAGE-GATE inside RHYTHM-DRI-ASSIGNMENT-COVERAGE names gated section + blocker |

V-05 is the predicted top scorer and establishes the R20 ceiling at 48/48 aspirational coverage.
