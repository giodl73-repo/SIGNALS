---
skill: quest-variate
skill_target: org-chart
date: 2026-03-16
round: R15
rubric_version: v14
status: variate
---

# org-chart Variate -- Round 15

**Date:** 2026-03-16
**Skill:** org-chart
**Rubric:** v14 (A-01 through A-36; A-34/A-35/A-36 new from R14)
**Round:** R15 -- single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

**R14 ceiling under v14:**
V-05/R14 achieves 36/36 aspirationally under rubric v14 (composite 100.0).
A-34 is satisfied via ROLE-TIER-ACCOUNTING: block immediately after ROLE-TYPE-CLASSIFICATION,
emitting one row per tier with actual count and TIER-PRESENT/TIER-ABSENT verdict. A-35 is satisfied
via CHARTER-COMPLETENESS-AUDIT: block after all charters and before the CHARTERS COMPLETE gate,
presenting a cross-charter table with PRESENT/MISSING per field. A-36 is satisfied via
REGISTER-CATEGORY-CONTRACT: block as first element in ORG-ELEMENT REGISTER, enumerating each
cat-N code and declaring the set closed.

**R15 target:** 36/36 aspirationally with new compression resistance gains beyond A-34/A-35/A-36.
Three structural gaps remain in V-05/R14 not yet captured by any criterion:

1. **Charter-rhythm correspondence gap:** A-35 (CHARTER-COMPLETENESS-AUDIT) verifies that each
   charter that exists has all required fields. But the audit's scope is charters already written --
   it does not verify that the number of charters equals the number of governance meetings in the
   Operating Rhythm Table. A governance row with no charter below it passes the audit silently.
   The count correspondence is an implicit sequential scan property; no named block makes it
   structurally detectable.

2. **Register category population gap:** A-36 (REGISTER-CATEGORY-CONTRACT) declares four cat-N
   codes as a closed set. After the register body is populated, there is no production-time check
   that each declared category has at least one entry. A cat-N category could have zero entries
   and the contract would still be satisfied because the code was declared, just never populated.
   Zero-entry category population is a silent absence rather than a scannable row.

3. **Roadmap trigger distinctness gap:** The roadmap requires two rows from "distinct trigger
   categories" (Row 1 headcount; Row 2 different category). The distinctness is stated once as a
   production-time instruction with no post-production verification. A model can write Row 2 as a
   headcount condition and label it "Milestone" -- the Type column would pass visual inspection but
   the structural property (truly distinct categories) is not verified as a named block.

---

## Variation Map

| V | Axis | Hypothesis |
|---|------|------------|
| V-01 | Charter-rhythm parity (A-37 candidate) | A CHARTER-RHYTHM-PARITY: block after CHARTER-COMPLETENESS-AUDIT closes the correspondence gap: RHYTHM-GOVERNANCE-COUNT vs CHARTER-COUNT, with PARITY-CONFIRMED/PARITY-MISMATCH verdict, making the missing-charter case a count-detectable failure rather than a silent audit pass |
| V-02 | Register population audit (A-38 candidate) | A REGISTER-POPULATION-AUDIT: block after the register body closes the zero-entry gap: one row per declared cat-N with entry count and POPULATED/EMPTY verdict, making an empty category a directly scannable row rather than a silent absence |
| V-03 | Roadmap trigger diversity verification (A-39 candidate) | A ROADMAP-TRIGGER-DIVERSITY: block after the roadmap table closes the implicit-distinctness gap: extracts declared Type from Row 1 and Row 2, compares them, emits DIVERSITY-CONFIRMED or DIVERSITY-MISMATCH, making trigger-category distinctness a named verifiable property |
| V-04 | Charter parity + register population audit (A-37 + A-38) | Combining CHARTER-RHYTHM-PARITY and REGISTER-POPULATION-AUDIT closes the two count-verification gaps at structurally isolated positions (charters phase vs analysis phase) without interaction |
| V-05 | Full integration: R14-V05 baseline + A-37 + A-38 + A-39 | Layering CHARTER-RHYTHM-PARITY, REGISTER-POPULATION-AUDIT, and ROADMAP-TRIGGER-DIVERSITY onto the R14-V05 foundation closes all three new gaps and achieves maximum compression resistance across the v15 cluster |

---

## V-01 -- Charter-Rhythm Parity Verification

**axis:** role sequence / lifecycle emphasis (CHARTER-RHYTHM-PARITY: block between
CHARTER-COMPLETENESS-AUDIT and CHARTERS COMPLETE gate; declares RHYTHM-GOVERNANCE-COUNT from
rhythm table; compares to CHARTER-COUNT from audit; emits PARITY-CONFIRMED or PARITY-MISMATCH;
missing charter is count-detectable; additive to A-35 CHARTER-COMPLETENESS-AUDIT)
**hypothesis:** A-35 verifies field completeness for charters that exist. It does not verify that
the count of charters equals the count of governance meetings in the Operating Rhythm Table. A
governance row can have no charter and the audit passes because there is nothing to inspect. The
CHARTER-RHYTHM-PARITY: block makes this a count comparison: RHYTHM-GOVERNANCE-COUNT vs
CHARTER-COUNT. PARITY-MISMATCH blocks the gate and requires the missing charter before proceeding.

---

```
You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block at the top listing each role and one-line description.
If absent: produce `ROLES-NOTE:` block with inferred roles.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER -- CLASSIFICATION SEQUENCE CONSTRAINT

DO classify roles in this exact tier order when producing ROLE-TYPE-CLASSIFICATION:
  Tier 1: Engineering roles (classify all Engineering entries before any Tier 2 or Tier 3 entry)
  Tier 2: Operations roles (classify all Operations entries before any Tier 3 entry)
  Tier 3: PM / Design / Research / Other roles
DO NOT write a Tier 2 entry before all Tier 1 entries are written.
DO NOT write a Tier 3 entry before all Tier 2 entries are written.
DO NOT interleave tiers.
If no Engineering roles are present, begin with Tier 2.
If no Engineering or Operations roles are present, classify all in any order.
This block governs sequence only. Type assignment rules are in ROLE-TYPE-CLASSIFICATION.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

DO produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE,
following the ROLE-LOAD-ORDER tier sequence above.
DO assign each role exactly one type from: `Engineering / PM / Design / Operations / Research / Other`
DO format each entry as: `- [role name] -- [domain type]`
DO annotate each Key Roles cell in the Headcount table as `[role name] ([domain type])`.
DO annotate each Membership field in Committee Charters in the same format.
DO NOT skip any role from ROLES-LOADED or ROLES-NOTE.

ROLE-TIER-ACCOUNTING -- REQUIRED IMMEDIATELY AFTER ROLE-TYPE-CLASSIFICATION

DO produce a `ROLE-TIER-ACCOUNTING:` block immediately after ROLE-TYPE-CLASSIFICATION.
The block MUST emit one row per tier declared in ROLE-LOAD-ORDER, in declaration order:
  `Tier 1 (Engineering): [N] role(s) classified -- TIER-PRESENT`
  `Tier 2 (Operations): [N] role(s) classified -- TIER-PRESENT`
  `Tier 3 (PM/Design/Research/Other): [N] role(s) classified -- TIER-PRESENT`
If a tier has zero classified entries:
  `Tier [N] ([tier name]): 0 roles classified -- TIER-ABSENT (no roles of this type in input set)`
TIER-ABSENT is not a constraint violation -- it records that the tier was declared and checked.
Count MUST match actual entries in ROLE-TYPE-CLASSIFICATION for that tier.
DO NOT proceed until all three tiers are accounted for. DO NOT omit this block.

DO emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
DO NOT proceed until this gate is present.

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.

STRUCTURING-COST FRAME -- PRE-ASSESSMENT BLOCK
`[Zone: PRE-ASSESSMENT]`

DO produce a labeled `STRUCTURING-COST FRAME:` block immediately before Sub-section 1.
MUST name both error risks with >= 1 concrete consequence each:
- Over-structuring risk
- Under-coordination risk
DO NOT merge with Sub-section 1. DO NOT omit.

**Sub-section 1 -- Case for Staying Flat**

DO produce a mechanism evidence table with exactly four columns:
`Mechanism Name | Mechanism Type | Frequency / Participants | Estimated Coordination Cost`
Mechanism Type from: `Channel / Informal Role / Recurring Cadence / Shared Artifact`
Floor: >= 2 data rows with >= 2 distinct Mechanism Type values. Numeric cost estimates required.

Count rows (N) and distinct types (K), then emit:
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded; {K} of 4 type classes represented. How We Coordinate Today begins.] ---`
DO NOT emit separator before count >= 2 AND distinct types >= 2.

**Sub-section 2 -- How We Coordinate Today**

Inventory active coordination patterns. DO NOT re-list Sub-section 1 entries.

**Sub-section 3 -- Rebuttal**

Name the specific coordination failure with a specific observable.
Include `UNCOVERED:` citation naming an ownerless function or decision class.
`[Zone: SUB-SECTION-3]`
UNCOVERED is additive to -- and MUST NOT replace -- the named coordination failure.

**Sub-section 4 -- VERDICT and Re-assessment Trigger**

SUB-SECTION-4-ANCHOR-SEQUENCE:
  Order 1: `COST-FRAME CONCLUSION:` line (write first; must precede all other Sub-section 4 content)
  Order 2: `NET-COST-COMPARISON:` block (write second; must immediately follow Order 1)
  Order 3: `FLAT-CASE-PRESSURE:` line (write third; must immediately follow Order 2 closing)
  CONSTRAINT: NO other content may be inserted between Order 1 and Order 2, or Order 2 and Order 3.

MUST produce `COST-FRAME CONCLUSION:` as the FIRST line of Sub-section 4. This line MUST:
(1) Name the `STRUCTURING-COST FRAME:` block by its label
(2) Cite the dominant error risk -- over-structuring or under-coordination
(3) Name at least one of Sub-sections 1, 2, or 3 as the evidence source

CROSS-REF-REQUIRED PAIR -- TWO INSTANCES IN SUB-SECTION 4:
CARDINALITY DECLARATION: (1 of 2) and (2 of 2) are both required.

After COST-FRAME CONCLUSION:, emit on its own line:
`CROSS-REF-REQUIRED (1 of 2): NO interceding content between COST-FRAME CONCLUSION: and NET-COST-COMPARISON: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

Then:
```
NET-COST-COMPARISON:
  Flat coordination cost: [total from Sub-section 1]
  Structure overhead: [meeting load + charter maintenance + escalation delay]
  Net delta: [flat cost minus structure overhead, signed]
  ADDITIVE-TO: C-01 FLAT-CASE-PRESSURE
```

After NET-COST-COMPARISON closes, emit on its own line:
`CROSS-REF-REQUIRED (2 of 2): NO interceding content between NET-COST-COMPARISON: close and FLAT-CASE-PRESSURE: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

Then:
`FLAT-CASE-PRESSURE: [rating] -- [justification citing mechanism count and failure mode]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`

Choose: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Reasoning cites FLAT-CASE-PRESSURE.
Re-assessment trigger: concrete threshold. DO NOT write "revisit as the team grows."
If `CAN-OPERATE-FLAT`: Flat Operating Rhythm table (>= 2 rows). `[Zone: POST-VERDICT-BRANCH]`

VERDICT-GATE CHECKLIST -- confirm all six items before proceeding past VERDICT:
  [ ] (1) COST-FRAME CONCLUSION: written as the first line of Sub-section 4
  [ ] (2) CROSS-REF-REQUIRED (1 of 2): written on its own line immediately after COST-FRAME CONCLUSION:
          [ANCHOR-ORDER CONSTRAINT: Order 1 (COST-FRAME CONCLUSION:) MUST immediately precede
          Order 2 (NET-COST-COMPARISON:) with NO interceding content -- verify adjacency now,
          independent of the SUB-SECTION-4-ANCHOR-SEQUENCE declaration]
  [ ] (3) NET-COST-COMPARISON: block immediately after CROSS-REF-REQUIRED (1 of 2), ADDITIVE-TO guard inside
  [ ] (4) CROSS-REF-REQUIRED (2 of 2): written on its own line immediately after NET-COST-COMPARISON: closes
          [ANCHOR-ORDER CONSTRAINT: Order 2 (NET-COST-COMPARISON:) MUST immediately precede
          Order 3 (FLAT-CASE-PRESSURE:) with NO interceding content -- verify adjacency now,
          independent of the SUB-SECTION-4-ANCHOR-SEQUENCE declaration]
  [ ] (5) FLAT-CASE-PRESSURE: immediately after CROSS-REF-REQUIRED (2 of 2), valid closed-set rating
  [ ] (6) Verdict (CAN-OPERATE-FLAT or STRUCTURE-WARRANTED) + re-assessment trigger

DO NOT proceed past VERDICT until all six checklist items are confirmed.

INTEGRATION-NOTE -- POSITIONAL DISJOINTNESS CONFIRMATION

DO produce `INTEGRATION-NOTE:` immediately after Sub-section 4 and BEFORE the ASCII org diagram.

REQUIRED format:
```
INTEGRATION-NOTE:
- STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT]: positioned before Sub-section 1
- UNCOVERED: citation [Zone: SUB-SECTION-3]: positioned within Sub-section 3
- Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH]: positioned after Sub-section 4, CAN-OPERATE-FLAT branch only
Positional disjointness confirmed: each artifact assigned to exactly one zone; no zone shared.
```

ZONE-NOTATION RULE:
REQUIRED: `[Zone: X]` bracket format in INTEGRATION-NOTE -- matches artifact definition sites.
PROHIBITED:
  (1) `(PRE-ASSESSMENT)` -- prohibited; use `[Zone: PRE-ASSESSMENT]` instead
  (2) `(SUB-SECTION-3)` -- prohibited; use `[Zone: SUB-SECTION-3]` instead
  (3) `(POST-VERDICT-BRANCH)` -- prohibited; use `[Zone: POST-VERDICT-BRANCH]` instead
DO NOT use parenthetical zone designators anywhere.

If `STRUCTURE-WARRANTED`: N/A for POST-VERDICT-BRANCH; confirm disjointness for two remaining.

ZONE-LABEL-TRACEABILITY -- REQUIRED IMMEDIATELY AFTER INTEGRATION-NOTE:
For each artifact in INTEGRATION-NOTE:
  (1) Locate inline `[Zone: X]` at artifact's definition site.
  (2) Compare INTEGRATION-NOTE designator with definition-site designator.
  (3) Emit:
      `ZONE-TRACE-CONFIRMED: [name] -- INTEGRATION-NOTE: [Zone: X]; definition site: [Zone: X]; designator strings match.`
      OR: `ZONE-TRACE-MISMATCH: [name] -- INTEGRATION-NOTE: [Zone: X]; definition site: [Zone: Y]; CORRECT before proceeding.`
DO NOT omit any line. DO NOT emit INERTIA COMPLETE until all present and mismatch-free.
If `STRUCTURE-WARRANTED`: ZONE-TRACE-CONFIRMED for two present artifacts;
`ZONE-TRACE-N/A: Flat Operating Rhythm -- POST-VERDICT-BRANCH absent (STRUCTURE-WARRANTED).`

DO emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
DO NOT draw org boxes until this gate is present.

ASCII ORG DIAGRAM

Box-drawing characters (`+`, `-`, `|`) or equivalent. At minimum two hierarchy levels.
Committees as distinct labeled nodes. Role names from ROLES-LOADED only.

DO emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

`Area | Headcount | Key Roles | Decides | Escalates`
DO NOT use a single "Decision Scope" column.
DO annotate Key Roles as `[role name] ([domain type])`.
At minimum two area rows plus `**Total**` row.

OPERATING RHYTHM TABLE

`Cadence | Frequency | DRI / Owner | Purpose`
At minimum three rows: one ROB, one shiproom or gate, one governance meeting.

COMMITTEE CHARTERS -- SIX FIELDS REQUIRED

DO write a charter for each governance meeting in the Operating Rhythm Table.
Include all six fields: Purpose, Membership, Decides, Escalates, Quorum, Dissolves When.
DO annotate Membership roles as `[role name] ([domain type])`. Minimum two roles.
DO populate Escalates with a named destination.
Dissolves When: specific, observable conditions only.

QUORUM-DENOMINATOR CONSTRAINT -- REQUIRED BEFORE EACH QUORUM LINE:
Before writing the Quorum line for each charter:
  (1) Count distinct Membership roles. That count is M.
  (2) Choose N (minimum required for binding decision; N < M).
  (3) Emit: `[QUORUM-COUNT: Membership roles listed = [M]; minimum binding quorum = [N] of [M]]`
  (4) Emit: `Quorum: [N] of [M] member roles required for binding decisions`
DO NOT write M without first counting. DO NOT omit [QUORUM-COUNT: ...] for any charter.

CHARTER-COMPLETENESS-AUDIT -- REQUIRED AFTER ALL CHARTERS, BEFORE CHARTERS COMPLETE GATE:

After all Committee Charters, DO produce a `CHARTER-COMPLETENESS-AUDIT:` block.
Emit one row per charter:
  `Charter: [name] | Purpose: [PRESENT/MISSING] | Membership: [PRESENT/MISSING] | Decides: [PRESENT/MISSING] | Escalates: [PRESENT/MISSING] | Quorum: [PRESENT/MISSING] | Dissolves When: [PRESENT/MISSING] | [ALL-FIELDS or MISSING: field1, field2, ...]`
Any MISSING is a constraint violation: add the missing field before proceeding.
DO NOT emit CHARTERS COMPLETE until all rows show ALL-FIELDS. DO NOT omit this block.

CHARTER-RHYTHM-PARITY -- REQUIRED AFTER CHARTER-COMPLETENESS-AUDIT, BEFORE CHARTERS COMPLETE GATE:

After CHARTER-COMPLETENESS-AUDIT, DO produce a `CHARTER-RHYTHM-PARITY:` block.
  (1) Count governance meeting rows in the Operating Rhythm Table (rows that require a charter).
      Emit: `RHYTHM-GOVERNANCE-COUNT: [N] governance meeting row(s) identified in Operating Rhythm Table`
  (2) Count charters written (rows in CHARTER-COMPLETENESS-AUDIT).
      Emit: `CHARTER-COUNT: [N] charter(s) written`
  (3) Compare:
      If counts match:
        `PARITY-CONFIRMED: every governance meeting has a corresponding charter.`
      If counts differ:
        `PARITY-MISMATCH: [RHYTHM-GOVERNANCE-COUNT] governance row(s) but [CHARTER-COUNT] charter(s) written. Identify the unchartered governance meeting and write its charter before proceeding.`
PARITY-MISMATCH blocks the CHARTERS COMPLETE gate. Resolve before emitting gate.
DO NOT omit this block. DO NOT emit CHARTERS COMPLETE until PARITY-CONFIRMED is present.

DO emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
DO NOT begin the ORG-ELEMENT REGISTER until this gate is present.

ORG-ELEMENT REGISTER -- MUST PRECEDE ORG EVOLUTION ROADMAP

REGISTER-CATEGORY-CONTRACT -- REQUIRED AS FIRST ELEMENT IN ORG-ELEMENT REGISTER:

Before any category entries, DO produce a `REGISTER-CATEGORY-CONTRACT:` block as the first
named element within the ORG-ELEMENT REGISTER.
The block MUST enumerate each category code and its canonical label:
  `cat-1 = Areas (all area names from the Headcount by Area table)`
  `cat-2 = Committees/Cadences (all committee and cadence names from Rhythm Table and Charters)`
  `cat-3 = Headcount (total and per-area headcount counts)`
  `cat-4 = DRI Roles (all DRI role names from the Operating Rhythm Table)`
The block MUST declare: `This code set is closed. cat-1 through cat-4 are the only valid codes.`
The block MUST prohibit: `Any (cat-N) citation in Anti-Pattern Watch using a code outside cat-1
through cat-4 is a constraint violation requiring correction.`
DO NOT begin cat-1 through cat-4 category entries until this block is written.

After REGISTER-CATEGORY-CONTRACT, populate all four categories:
  cat-1 (Areas): `- [area name] -- headcount: [N]`
  cat-2 (Committees/Cadences): `- [committee or cadence name]`
  cat-3 (Headcount): `- Total headcount: [N]`
  cat-4 (DRI Roles): `- [DRI role]`

ORG EVOLUTION ROADMAP -- REQUIRED

After ORG-ELEMENT REGISTER. Columns: `Trigger | Structural Change | Type`
At minimum two rows. Row 1: headcount threshold. Row 2: different category (workload signal,
structural symptom, or milestone event -- not another headcount threshold).

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

After Org Evolution Roadmap.
Open each "Why It Applies Here" cell:
`[element name] (cat-N) -- [one sentence of specific relevance]`
DO NOT use a cat-N code outside those declared in REGISTER-CATEGORY-CONTRACT.
At minimum two anti-pattern rows.

SECTION ORDER -- DO NOT REORDER

1.  ROLES-LOADED or ROLES-NOTE
2.  ROLE-LOAD-ORDER (Tier 1 Engineering, Tier 2 Operations, Tier 3 PM/Design/Research/Other)
3.  ROLE-TYPE-CLASSIFICATION (following ROLE-LOAD-ORDER)
4.  ROLE-TIER-ACCOUNTING (one row per tier with count and TIER-PRESENT/TIER-ABSENT)
5.  Phase gate: ROLES COMPLETE
6.  STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT] (before Sub-section 1)
7.  Sub-section 1 (mechanism table + FLAT-CASE-CLOSED with type-diversity count)
8.  Sub-section 2: How We Coordinate Today
9.  Sub-section 3: Rebuttal (UNCOVERED: citation [Zone: SUB-SECTION-3])
10. Sub-section 4: VERDICT (SUB-SECTION-4-ANCHOR-SEQUENCE + CROSS-REF-REQUIRED pair +
    NET-COST-COMPARISON + FLAT-CASE-PRESSURE + verdict + trigger + VERDICT-GATE CHECKLIST +
    Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH] if applicable)
11. INTEGRATION-NOTE with [Zone: X] bracket notation + ZONE-NOTATION RULE enumerated block
12. ZONE-LABEL-TRACEABILITY: one ZONE-TRACE-CONFIRMED per artifact, gating INERTIA COMPLETE
13. Phase gate: INERTIA COMPLETE
14. ASCII Org Diagram
15. Phase gate: STRUCTURE COMPLETE
16. Headcount by Area
17. Operating Rhythm Table
18. Committee Charters (QUORUM-DENOMINATOR CONSTRAINT per charter: [QUORUM-COUNT: ...] before each Quorum)
19. CHARTER-COMPLETENESS-AUDIT (six fields per charter, ALL-FIELDS required before gate)
20. CHARTER-RHYTHM-PARITY (RHYTHM-GOVERNANCE-COUNT vs CHARTER-COUNT, PARITY-CONFIRMED required)
21. Phase gate: CHARTERS COMPLETE
22. ORG-ELEMENT REGISTER (REGISTER-CATEGORY-CONTRACT as first element, then cat-1 through cat-4)
23. Org Evolution Roadmap
24. Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```

---

## V-02 -- Register Population Audit

**axis:** output format (REGISTER-POPULATION-AUDIT: block immediately after ORG-ELEMENT REGISTER
body; one row per declared cat-N category; emits entry count and POPULATED/EMPTY verdict; zero-entry
category emits EMPTY making the population gap a directly scannable row; additive to A-36
REGISTER-CATEGORY-CONTRACT closed-set declaration)
**hypothesis:** A-36 requires REGISTER-CATEGORY-CONTRACT to declare the four cat-N codes as a
closed set before entries are written. The contract verifies that codes are declared and that
Anti-Pattern Watch citations stay within the declared set. But it does not require each declared
category to have entries. A category could have zero entries -- the contract is satisfied because
the code was declared, just never used. V-02/R15 adds REGISTER-POPULATION-AUDIT: immediately after
the register body, emitting one row per declared category with actual entry count and POPULATED or
EMPTY verdict. EMPTY is not automatically a gate-blocking violation for small teams with few areas
or roles, but it converts silent absence into a scannable row -- the same logic that led A-34 to add
TIER-ABSENT for zero-entry tiers. The audit gate logic: any EMPTY that represents a structural
omission (e.g., cat-4 DRI Roles empty when rhythm table has DRI roles) requires correction; EMPTY
that is legitimately expected is noted and passes.

---

```
You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block at the top listing each role and one-line description.
If absent: produce `ROLES-NOTE:` block with inferred roles.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER -- CLASSIFICATION SEQUENCE CONSTRAINT

DO classify roles in this exact tier order when producing ROLE-TYPE-CLASSIFICATION:
  Tier 1: Engineering roles (classify all Engineering entries before any Tier 2 or Tier 3 entry)
  Tier 2: Operations roles (classify all Operations entries before any Tier 3 entry)
  Tier 3: PM / Design / Research / Other roles
DO NOT write a Tier 2 entry before all Tier 1 entries are written.
DO NOT write a Tier 3 entry before all Tier 2 entries are written.
DO NOT interleave tiers.
If no Engineering roles are present, begin with Tier 2.
If no Engineering or Operations roles are present, classify all in any order.
This block governs sequence only. Type assignment rules are in ROLE-TYPE-CLASSIFICATION.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

DO produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE,
following the ROLE-LOAD-ORDER tier sequence above.
DO assign each role exactly one type from: `Engineering / PM / Design / Operations / Research / Other`
DO format each entry as: `- [role name] -- [domain type]`
DO annotate each Key Roles cell in the Headcount table as `[role name] ([domain type])`.
DO annotate each Membership field in Committee Charters in the same format.
DO NOT skip any role from ROLES-LOADED or ROLES-NOTE.

ROLE-TIER-ACCOUNTING -- REQUIRED IMMEDIATELY AFTER ROLE-TYPE-CLASSIFICATION

DO produce a `ROLE-TIER-ACCOUNTING:` block immediately after ROLE-TYPE-CLASSIFICATION.
The block MUST emit one row per tier declared in ROLE-LOAD-ORDER, in declaration order:
  `Tier 1 (Engineering): [N] role(s) classified -- TIER-PRESENT`
  `Tier 2 (Operations): [N] role(s) classified -- TIER-PRESENT`
  `Tier 3 (PM/Design/Research/Other): [N] role(s) classified -- TIER-PRESENT`
If a tier has zero classified entries:
  `Tier [N] ([tier name]): 0 roles classified -- TIER-ABSENT (no roles of this type in input set)`
TIER-ABSENT is not a constraint violation -- it records that the tier was declared and checked.
Count MUST match actual entries in ROLE-TYPE-CLASSIFICATION for that tier.
DO NOT proceed until all three tiers are accounted for. DO NOT omit this block.

DO emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
DO NOT proceed until this gate is present.

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.

STRUCTURING-COST FRAME -- PRE-ASSESSMENT BLOCK
`[Zone: PRE-ASSESSMENT]`

DO produce a labeled `STRUCTURING-COST FRAME:` block immediately before Sub-section 1.
MUST name both error risks with >= 1 concrete consequence each:
- Over-structuring risk
- Under-coordination risk
DO NOT merge with Sub-section 1. DO NOT omit.

**Sub-section 1 -- Case for Staying Flat**

DO produce a mechanism evidence table with exactly four columns:
`Mechanism Name | Mechanism Type | Frequency / Participants | Estimated Coordination Cost`
Mechanism Type from: `Channel / Informal Role / Recurring Cadence / Shared Artifact`
Floor: >= 2 data rows with >= 2 distinct Mechanism Type values. Numeric cost estimates required.

Count rows (N) and distinct types (K), then emit:
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded; {K} of 4 type classes represented. How We Coordinate Today begins.] ---`
DO NOT emit separator before count >= 2 AND distinct types >= 2.

**Sub-section 2 -- How We Coordinate Today**

Inventory active coordination patterns. DO NOT re-list Sub-section 1 entries.

**Sub-section 3 -- Rebuttal**

Name the specific coordination failure with a specific observable.
Include `UNCOVERED:` citation naming an ownerless function or decision class.
`[Zone: SUB-SECTION-3]`
UNCOVERED is additive to -- and MUST NOT replace -- the named coordination failure.

**Sub-section 4 -- VERDICT and Re-assessment Trigger**

SUB-SECTION-4-ANCHOR-SEQUENCE:
  Order 1: `COST-FRAME CONCLUSION:` line (write first; must precede all other Sub-section 4 content)
  Order 2: `NET-COST-COMPARISON:` block (write second; must immediately follow Order 1)
  Order 3: `FLAT-CASE-PRESSURE:` line (write third; must immediately follow Order 2 closing)
  CONSTRAINT: NO other content may be inserted between Order 1 and Order 2, or Order 2 and Order 3.

MUST produce `COST-FRAME CONCLUSION:` as the FIRST line of Sub-section 4. This line MUST:
(1) Name the `STRUCTURING-COST FRAME:` block by its label
(2) Cite the dominant error risk -- over-structuring or under-coordination
(3) Name at least one of Sub-sections 1, 2, or 3 as the evidence source

CROSS-REF-REQUIRED PAIR -- TWO INSTANCES IN SUB-SECTION 4:
CARDINALITY DECLARATION: (1 of 2) and (2 of 2) are both required.

After COST-FRAME CONCLUSION:, emit on its own line:
`CROSS-REF-REQUIRED (1 of 2): NO interceding content between COST-FRAME CONCLUSION: and NET-COST-COMPARISON: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

Then:
```
NET-COST-COMPARISON:
  Flat coordination cost: [total from Sub-section 1]
  Structure overhead: [meeting load + charter maintenance + escalation delay]
  Net delta: [flat cost minus structure overhead, signed]
  ADDITIVE-TO: C-01 FLAT-CASE-PRESSURE
```

After NET-COST-COMPARISON closes, emit on its own line:
`CROSS-REF-REQUIRED (2 of 2): NO interceding content between NET-COST-COMPARISON: close and FLAT-CASE-PRESSURE: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

Then:
`FLAT-CASE-PRESSURE: [rating] -- [justification citing mechanism count and failure mode]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`

Choose: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Reasoning cites FLAT-CASE-PRESSURE.
Re-assessment trigger: concrete threshold. DO NOT write "revisit as the team grows."
If `CAN-OPERATE-FLAT`: Flat Operating Rhythm table (>= 2 rows). `[Zone: POST-VERDICT-BRANCH]`

VERDICT-GATE CHECKLIST -- confirm all six items before proceeding past VERDICT:
  [ ] (1) COST-FRAME CONCLUSION: written as the first line of Sub-section 4
  [ ] (2) CROSS-REF-REQUIRED (1 of 2): written on its own line immediately after COST-FRAME CONCLUSION:
          [ANCHOR-ORDER CONSTRAINT: Order 1 (COST-FRAME CONCLUSION:) MUST immediately precede
          Order 2 (NET-COST-COMPARISON:) with NO interceding content -- verify adjacency now,
          independent of the SUB-SECTION-4-ANCHOR-SEQUENCE declaration]
  [ ] (3) NET-COST-COMPARISON: block immediately after CROSS-REF-REQUIRED (1 of 2), ADDITIVE-TO guard inside
  [ ] (4) CROSS-REF-REQUIRED (2 of 2): written on its own line immediately after NET-COST-COMPARISON: closes
          [ANCHOR-ORDER CONSTRAINT: Order 2 (NET-COST-COMPARISON:) MUST immediately precede
          Order 3 (FLAT-CASE-PRESSURE:) with NO interceding content -- verify adjacency now,
          independent of the SUB-SECTION-4-ANCHOR-SEQUENCE declaration]
  [ ] (5) FLAT-CASE-PRESSURE: immediately after CROSS-REF-REQUIRED (2 of 2), valid closed-set rating
  [ ] (6) Verdict (CAN-OPERATE-FLAT or STRUCTURE-WARRANTED) + re-assessment trigger

DO NOT proceed past VERDICT until all six checklist items are confirmed.

INTEGRATION-NOTE -- POSITIONAL DISJOINTNESS CONFIRMATION

DO produce `INTEGRATION-NOTE:` immediately after Sub-section 4 and BEFORE the ASCII org diagram.

REQUIRED format:
```
INTEGRATION-NOTE:
- STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT]: positioned before Sub-section 1
- UNCOVERED: citation [Zone: SUB-SECTION-3]: positioned within Sub-section 3
- Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH]: positioned after Sub-section 4, CAN-OPERATE-FLAT branch only
Positional disjointness confirmed: each artifact assigned to exactly one zone; no zone shared.
```

ZONE-NOTATION RULE:
REQUIRED: `[Zone: X]` bracket format in INTEGRATION-NOTE -- matches artifact definition sites.
PROHIBITED:
  (1) `(PRE-ASSESSMENT)` -- prohibited; use `[Zone: PRE-ASSESSMENT]` instead
  (2) `(SUB-SECTION-3)` -- prohibited; use `[Zone: SUB-SECTION-3]` instead
  (3) `(POST-VERDICT-BRANCH)` -- prohibited; use `[Zone: POST-VERDICT-BRANCH]` instead
DO NOT use parenthetical zone designators anywhere.

If `STRUCTURE-WARRANTED`: N/A for POST-VERDICT-BRANCH; confirm disjointness for two remaining.

ZONE-LABEL-TRACEABILITY -- REQUIRED IMMEDIATELY AFTER INTEGRATION-NOTE:
For each artifact in INTEGRATION-NOTE:
  (1) Locate inline `[Zone: X]` at artifact's definition site.
  (2) Compare INTEGRATION-NOTE designator with definition-site designator.
  (3) Emit:
      `ZONE-TRACE-CONFIRMED: [name] -- INTEGRATION-NOTE: [Zone: X]; definition site: [Zone: X]; designator strings match.`
      OR: `ZONE-TRACE-MISMATCH: [name] -- INTEGRATION-NOTE: [Zone: X]; definition site: [Zone: Y]; CORRECT before proceeding.`
DO NOT omit any line. DO NOT emit INERTIA COMPLETE until all present and mismatch-free.
If `STRUCTURE-WARRANTED`: ZONE-TRACE-CONFIRMED for two present artifacts;
`ZONE-TRACE-N/A: Flat Operating Rhythm -- POST-VERDICT-BRANCH absent (STRUCTURE-WARRANTED).`

DO emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
DO NOT draw org boxes until this gate is present.

ASCII ORG DIAGRAM

Box-drawing characters (`+`, `-`, `|`) or equivalent. At minimum two hierarchy levels.
Committees as distinct labeled nodes. Role names from ROLES-LOADED only.

DO emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

`Area | Headcount | Key Roles | Decides | Escalates`
DO NOT use a single "Decision Scope" column.
DO annotate Key Roles as `[role name] ([domain type])`.
At minimum two area rows plus `**Total**` row.

OPERATING RHYTHM TABLE

`Cadence | Frequency | DRI / Owner | Purpose`
At minimum three rows: one ROB, one shiproom or gate, one governance meeting.

COMMITTEE CHARTERS -- SIX FIELDS REQUIRED

DO write a charter for each governance meeting in the Operating Rhythm Table.
Include all six fields: Purpose, Membership, Decides, Escalates, Quorum, Dissolves When.
DO annotate Membership roles as `[role name] ([domain type])`. Minimum two roles.
DO populate Escalates with a named destination.
Dissolves When: specific, observable conditions only.

QUORUM-DENOMINATOR CONSTRAINT -- REQUIRED BEFORE EACH QUORUM LINE:
Before writing the Quorum line for each charter:
  (1) Count distinct Membership roles. That count is M.
  (2) Choose N (minimum required for binding decision; N < M).
  (3) Emit: `[QUORUM-COUNT: Membership roles listed = [M]; minimum binding quorum = [N] of [M]]`
  (4) Emit: `Quorum: [N] of [M] member roles required for binding decisions`
DO NOT write M without first counting. DO NOT omit [QUORUM-COUNT: ...] for any charter.

CHARTER-COMPLETENESS-AUDIT -- REQUIRED AFTER ALL CHARTERS, BEFORE CHARTERS COMPLETE GATE:

After all Committee Charters, DO produce a `CHARTER-COMPLETENESS-AUDIT:` block.
Emit one row per charter:
  `Charter: [name] | Purpose: [PRESENT/MISSING] | Membership: [PRESENT/MISSING] | Decides: [PRESENT/MISSING] | Escalates: [PRESENT/MISSING] | Quorum: [PRESENT/MISSING] | Dissolves When: [PRESENT/MISSING] | [ALL-FIELDS or MISSING: field1, field2, ...]`
Any MISSING is a constraint violation: add the missing field before proceeding.
DO NOT emit CHARTERS COMPLETE until all rows show ALL-FIELDS. DO NOT omit this block.

DO emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
DO NOT begin the ORG-ELEMENT REGISTER until this gate is present.

ORG-ELEMENT REGISTER -- MUST PRECEDE ORG EVOLUTION ROADMAP

REGISTER-CATEGORY-CONTRACT -- REQUIRED AS FIRST ELEMENT IN ORG-ELEMENT REGISTER:

Before any category entries, DO produce a `REGISTER-CATEGORY-CONTRACT:` block as the first
named element within the ORG-ELEMENT REGISTER.
The block MUST enumerate each category code and its canonical label:
  `cat-1 = Areas (all area names from the Headcount by Area table)`
  `cat-2 = Committees/Cadences (all committee and cadence names from Rhythm Table and Charters)`
  `cat-3 = Headcount (total and per-area headcount counts)`
  `cat-4 = DRI Roles (all DRI role names from the Operating Rhythm Table)`
The block MUST declare: `This code set is closed. cat-1 through cat-4 are the only valid codes.`
The block MUST prohibit: `Any (cat-N) citation in Anti-Pattern Watch using a code outside cat-1
through cat-4 is a constraint violation requiring correction.`
DO NOT begin cat-1 through cat-4 category entries until this block is written.

After REGISTER-CATEGORY-CONTRACT, populate all four categories:
  cat-1 (Areas): `- [area name] -- headcount: [N]`
  cat-2 (Committees/Cadences): `- [committee or cadence name]`
  cat-3 (Headcount): `- Total headcount: [N]`
  cat-4 (DRI Roles): `- [DRI role]`

REGISTER-POPULATION-AUDIT -- REQUIRED IMMEDIATELY AFTER REGISTER BODY, BEFORE ROADMAP:

After all four categories are populated, DO produce a `REGISTER-POPULATION-AUDIT:` block.
Emit one row per declared category code, in order cat-1 through cat-4:
  `cat-1 (Areas): [N] entry(ies) -- POPULATED`
  `cat-2 (Committees/Cadences): [N] entry(ies) -- POPULATED`
  `cat-3 (Headcount): [N] entry(ies) -- POPULATED`
  `cat-4 (DRI Roles): [N] entry(ies) -- POPULATED`
If a category has zero entries:
  `cat-N ([name]): 0 entries -- EMPTY`
EMPTY verdict: determine whether zero entries are structurally expected or represent an omission.
  - If the Operating Rhythm Table has DRI roles and cat-4 is EMPTY: constraint violation -- add entries.
  - If the team has areas and cat-1 is EMPTY: constraint violation -- add entries.
  - If EMPTY is expected (e.g., cat-3 Headcount for a single-person team): note reason and continue.
DO NOT proceed to Org Evolution Roadmap until all EMPTY verdicts are resolved or noted. DO NOT omit.

ORG EVOLUTION ROADMAP -- REQUIRED

After REGISTER-POPULATION-AUDIT. Columns: `Trigger | Structural Change | Type`
At minimum two rows. Row 1: headcount threshold. Row 2: different category (workload signal,
structural symptom, or milestone event -- not another headcount threshold).

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

After Org Evolution Roadmap.
Open each "Why It Applies Here" cell:
`[element name] (cat-N) -- [one sentence of specific relevance]`
DO NOT use a cat-N code outside those declared in REGISTER-CATEGORY-CONTRACT.
At minimum two anti-pattern rows.

SECTION ORDER -- DO NOT REORDER

1.  ROLES-LOADED or ROLES-NOTE
2.  ROLE-LOAD-ORDER (Tier 1 Engineering, Tier 2 Operations, Tier 3 PM/Design/Research/Other)
3.  ROLE-TYPE-CLASSIFICATION (following ROLE-LOAD-ORDER)
4.  ROLE-TIER-ACCOUNTING (one row per tier with count and TIER-PRESENT/TIER-ABSENT)
5.  Phase gate: ROLES COMPLETE
6.  STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT] (before Sub-section 1)
7.  Sub-section 1 (mechanism table + FLAT-CASE-CLOSED with type-diversity count)
8.  Sub-section 2: How We Coordinate Today
9.  Sub-section 3: Rebuttal (UNCOVERED: citation [Zone: SUB-SECTION-3])
10. Sub-section 4: VERDICT (SUB-SECTION-4-ANCHOR-SEQUENCE + CROSS-REF-REQUIRED pair +
    NET-COST-COMPARISON + FLAT-CASE-PRESSURE + verdict + trigger + VERDICT-GATE CHECKLIST +
    Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH] if applicable)
11. INTEGRATION-NOTE with [Zone: X] bracket notation + ZONE-NOTATION RULE enumerated block
12. ZONE-LABEL-TRACEABILITY: one ZONE-TRACE-CONFIRMED per artifact, gating INERTIA COMPLETE
13. Phase gate: INERTIA COMPLETE
14. ASCII Org Diagram
15. Phase gate: STRUCTURE COMPLETE
16. Headcount by Area
17. Operating Rhythm Table
18. Committee Charters (QUORUM-DENOMINATOR CONSTRAINT per charter: [QUORUM-COUNT: ...] before each Quorum)
19. CHARTER-COMPLETENESS-AUDIT (six fields per charter, ALL-FIELDS required before gate)
20. Phase gate: CHARTERS COMPLETE
21. ORG-ELEMENT REGISTER (REGISTER-CATEGORY-CONTRACT as first element, then cat-1 through cat-4)
22. REGISTER-POPULATION-AUDIT (one row per cat-N, POPULATED/EMPTY, EMPTY resolved before roadmap)
23. Org Evolution Roadmap
24. Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```

---

## V-03 -- Roadmap Trigger Diversity Verification

**axis:** lifecycle emphasis (ROADMAP-TRIGGER-DIVERSITY: block after Org Evolution Roadmap table;
extracts declared Type from Row 1 and Row 2; confirms they are from distinct categories; emits
DIVERSITY-CONFIRMED or DIVERSITY-MISMATCH; additive to the existing two-rows requirement)
**hypothesis:** V-05/R14 requires two roadmap rows from "distinct trigger categories" (Row 1:
headcount threshold; Row 2: different category). The two-rows requirement has structural enforcement
via SECTION ORDER. The distinctness requirement does not -- it is stated once as a production-time
instruction. A model can write Row 2 as a headcount condition while labeling the Type column
"Milestone." The ROADMAP-TRIGGER-DIVERSITY: block extracts both Type values, compares them, and
emits DIVERSITY-CONFIRMED if they are from different categories or DIVERSITY-MISMATCH with a
correction instruction if they are the same. This promotes trigger-category distinctness from an
implicit production property to a named verifiable post-production check.

---

```
You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block at the top listing each role and one-line description.
If absent: produce `ROLES-NOTE:` block with inferred roles.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER -- CLASSIFICATION SEQUENCE CONSTRAINT

DO classify roles in this exact tier order when producing ROLE-TYPE-CLASSIFICATION:
  Tier 1: Engineering roles (classify all Engineering entries before any Tier 2 or Tier 3 entry)
  Tier 2: Operations roles (classify all Operations entries before any Tier 3 entry)
  Tier 3: PM / Design / Research / Other roles
DO NOT write a Tier 2 entry before all Tier 1 entries are written.
DO NOT write a Tier 3 entry before all Tier 2 entries are written.
DO NOT interleave tiers.
If no Engineering roles are present, begin with Tier 2.
If no Engineering or Operations roles are present, classify all in any order.
This block governs sequence only. Type assignment rules are in ROLE-TYPE-CLASSIFICATION.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

DO produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE,
following the ROLE-LOAD-ORDER tier sequence above.
DO assign each role exactly one type from: `Engineering / PM / Design / Operations / Research / Other`
DO format each entry as: `- [role name] -- [domain type]`
DO annotate each Key Roles cell in the Headcount table as `[role name] ([domain type])`.
DO annotate each Membership field in Committee Charters in the same format.
DO NOT skip any role from ROLES-LOADED or ROLES-NOTE.

ROLE-TIER-ACCOUNTING -- REQUIRED IMMEDIATELY AFTER ROLE-TYPE-CLASSIFICATION

DO produce a `ROLE-TIER-ACCOUNTING:` block immediately after ROLE-TYPE-CLASSIFICATION.
The block MUST emit one row per tier declared in ROLE-LOAD-ORDER, in declaration order:
  `Tier 1 (Engineering): [N] role(s) classified -- TIER-PRESENT`
  `Tier 2 (Operations): [N] role(s) classified -- TIER-PRESENT`
  `Tier 3 (PM/Design/Research/Other): [N] role(s) classified -- TIER-PRESENT`
If a tier has zero classified entries:
  `Tier [N] ([tier name]): 0 roles classified -- TIER-ABSENT (no roles of this type in input set)`
TIER-ABSENT is not a constraint violation -- it records that the tier was declared and checked.
Count MUST match actual entries in ROLE-TYPE-CLASSIFICATION for that tier.
DO NOT proceed until all three tiers are accounted for. DO NOT omit this block.

DO emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
DO NOT proceed until this gate is present.

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.

STRUCTURING-COST FRAME -- PRE-ASSESSMENT BLOCK
`[Zone: PRE-ASSESSMENT]`

DO produce a labeled `STRUCTURING-COST FRAME:` block immediately before Sub-section 1.
MUST name both error risks with >= 1 concrete consequence each:
- Over-structuring risk
- Under-coordination risk
DO NOT merge with Sub-section 1. DO NOT omit.

**Sub-section 1 -- Case for Staying Flat**

DO produce a mechanism evidence table with exactly four columns:
`Mechanism Name | Mechanism Type | Frequency / Participants | Estimated Coordination Cost`
Mechanism Type from: `Channel / Informal Role / Recurring Cadence / Shared Artifact`
Floor: >= 2 data rows with >= 2 distinct Mechanism Type values. Numeric cost estimates required.

Count rows (N) and distinct types (K), then emit:
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded; {K} of 4 type classes represented. How We Coordinate Today begins.] ---`
DO NOT emit separator before count >= 2 AND distinct types >= 2.

**Sub-section 2 -- How We Coordinate Today**

Inventory active coordination patterns. DO NOT re-list Sub-section 1 entries.

**Sub-section 3 -- Rebuttal**

Name the specific coordination failure with a specific observable.
Include `UNCOVERED:` citation naming an ownerless function or decision class.
`[Zone: SUB-SECTION-3]`
UNCOVERED is additive to -- and MUST NOT replace -- the named coordination failure.

**Sub-section 4 -- VERDICT and Re-assessment Trigger**

SUB-SECTION-4-ANCHOR-SEQUENCE:
  Order 1: `COST-FRAME CONCLUSION:` line (write first; must precede all other Sub-section 4 content)
  Order 2: `NET-COST-COMPARISON:` block (write second; must immediately follow Order 1)
  Order 3: `FLAT-CASE-PRESSURE:` line (write third; must immediately follow Order 2 closing)
  CONSTRAINT: NO other content may be inserted between Order 1 and Order 2, or Order 2 and Order 3.

MUST produce `COST-FRAME CONCLUSION:` as the FIRST line of Sub-section 4. This line MUST:
(1) Name the `STRUCTURING-COST FRAME:` block by its label
(2) Cite the dominant error risk -- over-structuring or under-coordination
(3) Name at least one of Sub-sections 1, 2, or 3 as the evidence source

CROSS-REF-REQUIRED PAIR -- TWO INSTANCES IN SUB-SECTION 4:
CARDINALITY DECLARATION: (1 of 2) and (2 of 2) are both required.

After COST-FRAME CONCLUSION:, emit on its own line:
`CROSS-REF-REQUIRED (1 of 2): NO interceding content between COST-FRAME CONCLUSION: and NET-COST-COMPARISON: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

Then:
```
NET-COST-COMPARISON:
  Flat coordination cost: [total from Sub-section 1]
  Structure overhead: [meeting load + charter maintenance + escalation delay]
  Net delta: [flat cost minus structure overhead, signed]
  ADDITIVE-TO: C-01 FLAT-CASE-PRESSURE
```

After NET-COST-COMPARISON closes, emit on its own line:
`CROSS-REF-REQUIRED (2 of 2): NO interceding content between NET-COST-COMPARISON: close and FLAT-CASE-PRESSURE: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

Then:
`FLAT-CASE-PRESSURE: [rating] -- [justification citing mechanism count and failure mode]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`

Choose: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Reasoning cites FLAT-CASE-PRESSURE.
Re-assessment trigger: concrete threshold. DO NOT write "revisit as the team grows."
If `CAN-OPERATE-FLAT`: Flat Operating Rhythm table (>= 2 rows). `[Zone: POST-VERDICT-BRANCH]`

VERDICT-GATE CHECKLIST -- confirm all six items before proceeding past VERDICT:
  [ ] (1) COST-FRAME CONCLUSION: written as the first line of Sub-section 4
  [ ] (2) CROSS-REF-REQUIRED (1 of 2): written on its own line immediately after COST-FRAME CONCLUSION:
          [ANCHOR-ORDER CONSTRAINT: Order 1 (COST-FRAME CONCLUSION:) MUST immediately precede
          Order 2 (NET-COST-COMPARISON:) with NO interceding content -- verify adjacency now,
          independent of the SUB-SECTION-4-ANCHOR-SEQUENCE declaration]
  [ ] (3) NET-COST-COMPARISON: block immediately after CROSS-REF-REQUIRED (1 of 2), ADDITIVE-TO guard inside
  [ ] (4) CROSS-REF-REQUIRED (2 of 2): written on its own line immediately after NET-COST-COMPARISON: closes
          [ANCHOR-ORDER CONSTRAINT: Order 2 (NET-COST-COMPARISON:) MUST immediately precede
          Order 3 (FLAT-CASE-PRESSURE:) with NO interceding content -- verify adjacency now,
          independent of the SUB-SECTION-4-ANCHOR-SEQUENCE declaration]
  [ ] (5) FLAT-CASE-PRESSURE: immediately after CROSS-REF-REQUIRED (2 of 2), valid closed-set rating
  [ ] (6) Verdict (CAN-OPERATE-FLAT or STRUCTURE-WARRANTED) + re-assessment trigger

DO NOT proceed past VERDICT until all six checklist items are confirmed.

INTEGRATION-NOTE -- POSITIONAL DISJOINTNESS CONFIRMATION

DO produce `INTEGRATION-NOTE:` immediately after Sub-section 4 and BEFORE the ASCII org diagram.

REQUIRED format:
```
INTEGRATION-NOTE:
- STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT]: positioned before Sub-section 1
- UNCOVERED: citation [Zone: SUB-SECTION-3]: positioned within Sub-section 3
- Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH]: positioned after Sub-section 4, CAN-OPERATE-FLAT branch only
Positional disjointness confirmed: each artifact assigned to exactly one zone; no zone shared.
```

ZONE-NOTATION RULE:
REQUIRED: `[Zone: X]` bracket format in INTEGRATION-NOTE -- matches artifact definition sites.
PROHIBITED:
  (1) `(PRE-ASSESSMENT)` -- prohibited; use `[Zone: PRE-ASSESSMENT]` instead
  (2) `(SUB-SECTION-3)` -- prohibited; use `[Zone: SUB-SECTION-3]` instead
  (3) `(POST-VERDICT-BRANCH)` -- prohibited; use `[Zone: POST-VERDICT-BRANCH]` instead
DO NOT use parenthetical zone designators anywhere.

If `STRUCTURE-WARRANTED`: N/A for POST-VERDICT-BRANCH; confirm disjointness for two remaining.

ZONE-LABEL-TRACEABILITY -- REQUIRED IMMEDIATELY AFTER INTEGRATION-NOTE:
For each artifact in INTEGRATION-NOTE:
  (1) Locate inline `[Zone: X]` at artifact's definition site.
  (2) Compare INTEGRATION-NOTE designator with definition-site designator.
  (3) Emit:
      `ZONE-TRACE-CONFIRMED: [name] -- INTEGRATION-NOTE: [Zone: X]; definition site: [Zone: X]; designator strings match.`
      OR: `ZONE-TRACE-MISMATCH: [name] -- INTEGRATION-NOTE: [Zone: X]; definition site: [Zone: Y]; CORRECT before proceeding.`
DO NOT omit any line. DO NOT emit INERTIA COMPLETE until all present and mismatch-free.
If `STRUCTURE-WARRANTED`: ZONE-TRACE-CONFIRMED for two present artifacts;
`ZONE-TRACE-N/A: Flat Operating Rhythm -- POST-VERDICT-BRANCH absent (STRUCTURE-WARRANTED).`

DO emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
DO NOT draw org boxes until this gate is present.

ASCII ORG DIAGRAM

Box-drawing characters (`+`, `-`, `|`) or equivalent. At minimum two hierarchy levels.
Committees as distinct labeled nodes. Role names from ROLES-LOADED only.

DO emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

`Area | Headcount | Key Roles | Decides | Escalates`
DO NOT use a single "Decision Scope" column.
DO annotate Key Roles as `[role name] ([domain type])`.
At minimum two area rows plus `**Total**` row.

OPERATING RHYTHM TABLE

`Cadence | Frequency | DRI / Owner | Purpose`
At minimum three rows: one ROB, one shiproom or gate, one governance meeting.

COMMITTEE CHARTERS -- SIX FIELDS REQUIRED

DO write a charter for each governance meeting in the Operating Rhythm Table.
Include all six fields: Purpose, Membership, Decides, Escalates, Quorum, Dissolves When.
DO annotate Membership roles as `[role name] ([domain type])`. Minimum two roles.
DO populate Escalates with a named destination.
Dissolves When: specific, observable conditions only.

QUORUM-DENOMINATOR CONSTRAINT -- REQUIRED BEFORE EACH QUORUM LINE:
Before writing the Quorum line for each charter:
  (1) Count distinct Membership roles. That count is M.
  (2) Choose N (minimum required for binding decision; N < M).
  (3) Emit: `[QUORUM-COUNT: Membership roles listed = [M]; minimum binding quorum = [N] of [M]]`
  (4) Emit: `Quorum: [N] of [M] member roles required for binding decisions`
DO NOT write M without first counting. DO NOT omit [QUORUM-COUNT: ...] for any charter.

CHARTER-COMPLETENESS-AUDIT -- REQUIRED AFTER ALL CHARTERS, BEFORE CHARTERS COMPLETE GATE:

After all Committee Charters, DO produce a `CHARTER-COMPLETENESS-AUDIT:` block.
Emit one row per charter:
  `Charter: [name] | Purpose: [PRESENT/MISSING] | Membership: [PRESENT/MISSING] | Decides: [PRESENT/MISSING] | Escalates: [PRESENT/MISSING] | Quorum: [PRESENT/MISSING] | Dissolves When: [PRESENT/MISSING] | [ALL-FIELDS or MISSING: field1, field2, ...]`
Any MISSING is a constraint violation: add the missing field before proceeding.
DO NOT emit CHARTERS COMPLETE until all rows show ALL-FIELDS. DO NOT omit this block.

DO emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
DO NOT begin the ORG-ELEMENT REGISTER until this gate is present.

ORG-ELEMENT REGISTER -- MUST PRECEDE ORG EVOLUTION ROADMAP

REGISTER-CATEGORY-CONTRACT -- REQUIRED AS FIRST ELEMENT IN ORG-ELEMENT REGISTER:

Before any category entries, DO produce a `REGISTER-CATEGORY-CONTRACT:` block as the first
named element within the ORG-ELEMENT REGISTER.
The block MUST enumerate each category code and its canonical label:
  `cat-1 = Areas (all area names from the Headcount by Area table)`
  `cat-2 = Committees/Cadences (all committee and cadence names from Rhythm Table and Charters)`
  `cat-3 = Headcount (total and per-area headcount counts)`
  `cat-4 = DRI Roles (all DRI role names from the Operating Rhythm Table)`
The block MUST declare: `This code set is closed. cat-1 through cat-4 are the only valid codes.`
The block MUST prohibit: `Any (cat-N) citation in Anti-Pattern Watch using a code outside cat-1
through cat-4 is a constraint violation requiring correction.`
DO NOT begin cat-1 through cat-4 category entries until this block is written.

After REGISTER-CATEGORY-CONTRACT, populate all four categories:
  cat-1 (Areas): `- [area name] -- headcount: [N]`
  cat-2 (Committees/Cadences): `- [committee or cadence name]`
  cat-3 (Headcount): `- Total headcount: [N]`
  cat-4 (DRI Roles): `- [DRI role]`

ORG EVOLUTION ROADMAP -- REQUIRED

After ORG-ELEMENT REGISTER. Columns: `Trigger | Structural Change | Type`
At minimum two rows. Row 1: headcount threshold. Row 2: different category (workload signal,
structural symptom, or milestone event -- not another headcount threshold).

ROADMAP-TRIGGER-DIVERSITY -- REQUIRED IMMEDIATELY AFTER ROADMAP TABLE, BEFORE ANTI-PATTERN WATCH:

After the Org Evolution Roadmap table, DO produce a `ROADMAP-TRIGGER-DIVERSITY:` block.
  (1) Extract the Type value from Row 1. Emit:
      `TRIGGER-ROW-1-TYPE: [Type value from Row 1]`
  (2) Extract the Type value from Row 2. Emit:
      `TRIGGER-ROW-2-TYPE: [Type value from Row 2]`
  (3) Confirm category distinctness:
      If Row 1 and Row 2 are from different categories (e.g., Headcount vs Milestone, Headcount vs
      Workload, Headcount vs Structural Symptom):
        `DIVERSITY-CONFIRMED: Row 1 ([Type]) and Row 2 ([Type]) are from distinct trigger categories.`
      If both rows are from the same category (e.g., both Headcount):
        `DIVERSITY-MISMATCH: Row 1 ([Type]) and Row 2 ([Type]) are from the same category. Rewrite
        Row 2 with a trigger from a different category before proceeding to Anti-Pattern Watch.`
DIVERSITY-MISMATCH blocks Anti-Pattern Watch. Resolve before proceeding.
DO NOT omit this block. DO NOT proceed to Anti-Pattern Watch until DIVERSITY-CONFIRMED is present.

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

After ROADMAP-TRIGGER-DIVERSITY.
Open each "Why It Applies Here" cell:
`[element name] (cat-N) -- [one sentence of specific relevance]`
DO NOT use a cat-N code outside those declared in REGISTER-CATEGORY-CONTRACT.
At minimum two anti-pattern rows.

SECTION ORDER -- DO NOT REORDER

1.  ROLES-LOADED or ROLES-NOTE
2.  ROLE-LOAD-ORDER (Tier 1 Engineering, Tier 2 Operations, Tier 3 PM/Design/Research/Other)
3.  ROLE-TYPE-CLASSIFICATION (following ROLE-LOAD-ORDER)
4.  ROLE-TIER-ACCOUNTING (one row per tier with count and TIER-PRESENT/TIER-ABSENT)
5.  Phase gate: ROLES COMPLETE
6.  STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT] (before Sub-section 1)
7.  Sub-section 1 (mechanism table + FLAT-CASE-CLOSED with type-diversity count)
8.  Sub-section 2: How We Coordinate Today
9.  Sub-section 3: Rebuttal (UNCOVERED: citation [Zone: SUB-SECTION-3])
10. Sub-section 4: VERDICT (SUB-SECTION-4-ANCHOR-SEQUENCE + CROSS-REF-REQUIRED pair +
    NET-COST-COMPARISON + FLAT-CASE-PRESSURE + verdict + trigger + VERDICT-GATE CHECKLIST +
    Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH] if applicable)
11. INTEGRATION-NOTE with [Zone: X] bracket notation + ZONE-NOTATION RULE enumerated block
12. ZONE-LABEL-TRACEABILITY: one ZONE-TRACE-CONFIRMED per artifact, gating INERTIA COMPLETE
13. Phase gate: INERTIA COMPLETE
14. ASCII Org Diagram
15. Phase gate: STRUCTURE COMPLETE
16. Headcount by Area
17. Operating Rhythm Table
18. Committee Charters (QUORUM-DENOMINATOR CONSTRAINT per charter: [QUORUM-COUNT: ...] before each Quorum)
19. CHARTER-COMPLETENESS-AUDIT (six fields per charter, ALL-FIELDS required before gate)
20. Phase gate: CHARTERS COMPLETE
21. ORG-ELEMENT REGISTER (REGISTER-CATEGORY-CONTRACT as first element, then cat-1 through cat-4)
22. Org Evolution Roadmap
23. ROADMAP-TRIGGER-DIVERSITY (Row 1 and Row 2 Types extracted, DIVERSITY-CONFIRMED required)
24. Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```

---

## V-04 -- Combined: Charter-Rhythm Parity + Register Population Audit

**axis:** combined lifecycle emphasis (V-01/R15 CHARTER-RHYTHM-PARITY + V-02/R15
REGISTER-POPULATION-AUDIT; both are count-verification audit blocks at structurally isolated
positions -- charters phase vs analysis phase -- with no shared state or interaction surface)
**hypothesis:** V-01/R15 closes the charter-count gap by adding CHARTER-RHYTHM-PARITY after
CHARTER-COMPLETENESS-AUDIT. V-02/R15 closes the register-population gap by adding
REGISTER-POPULATION-AUDIT after the register body. The two blocks operate at structurally isolated
positions in different phases: charters phase (between CHARTER-COMPLETENESS-AUDIT and CHARTERS
COMPLETE gate) and analysis phase (between register body and Org Evolution Roadmap). No interaction
surface exists. Combined, they provide named count-verification artifacts at two positions that
V-05/R14 leaves implicit.

---

```
You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block at the top listing each role and one-line description.
If absent: produce `ROLES-NOTE:` block with inferred roles.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER -- CLASSIFICATION SEQUENCE CONSTRAINT

DO classify roles in this exact tier order when producing ROLE-TYPE-CLASSIFICATION:
  Tier 1: Engineering roles (classify all Engineering entries before any Tier 2 or Tier 3 entry)
  Tier 2: Operations roles (classify all Operations entries before any Tier 3 entry)
  Tier 3: PM / Design / Research / Other roles
DO NOT write a Tier 2 entry before all Tier 1 entries are written.
DO NOT write a Tier 3 entry before all Tier 2 entries are written.
DO NOT interleave tiers.
If no Engineering roles are present, begin with Tier 2.
If no Engineering or Operations roles are present, classify all in any order.
This block governs sequence only. Type assignment rules are in ROLE-TYPE-CLASSIFICATION.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

DO produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE,
following the ROLE-LOAD-ORDER tier sequence above.
DO assign each role exactly one type from: `Engineering / PM / Design / Operations / Research / Other`
DO format each entry as: `- [role name] -- [domain type]`
DO annotate each Key Roles cell in the Headcount table as `[role name] ([domain type])`.
DO annotate each Membership field in Committee Charters in the same format.
DO NOT skip any role from ROLES-LOADED or ROLES-NOTE.

ROLE-TIER-ACCOUNTING -- REQUIRED IMMEDIATELY AFTER ROLE-TYPE-CLASSIFICATION

DO produce a `ROLE-TIER-ACCOUNTING:` block immediately after ROLE-TYPE-CLASSIFICATION.
The block MUST emit one row per tier declared in ROLE-LOAD-ORDER, in declaration order:
  `Tier 1 (Engineering): [N] role(s) classified -- TIER-PRESENT`
  `Tier 2 (Operations): [N] role(s) classified -- TIER-PRESENT`
  `Tier 3 (PM/Design/Research/Other): [N] role(s) classified -- TIER-PRESENT`
If a tier has zero classified entries:
  `Tier [N] ([tier name]): 0 roles classified -- TIER-ABSENT (no roles of this type in input set)`
TIER-ABSENT is not a constraint violation -- it records that the tier was declared and checked.
Count MUST match actual entries in ROLE-TYPE-CLASSIFICATION for that tier.
DO NOT proceed until all three tiers are accounted for. DO NOT omit this block.

DO emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
DO NOT proceed until this gate is present.

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.

STRUCTURING-COST FRAME -- PRE-ASSESSMENT BLOCK
`[Zone: PRE-ASSESSMENT]`

DO produce a labeled `STRUCTURING-COST FRAME:` block immediately before Sub-section 1.
MUST name both error risks with >= 1 concrete consequence each:
- Over-structuring risk
- Under-coordination risk
DO NOT merge with Sub-section 1. DO NOT omit.

**Sub-section 1 -- Case for Staying Flat**

DO produce a mechanism evidence table with exactly four columns:
`Mechanism Name | Mechanism Type | Frequency / Participants | Estimated Coordination Cost`
Mechanism Type from: `Channel / Informal Role / Recurring Cadence / Shared Artifact`
Floor: >= 2 data rows with >= 2 distinct Mechanism Type values. Numeric cost estimates required.

Count rows (N) and distinct types (K), then emit:
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded; {K} of 4 type classes represented. How We Coordinate Today begins.] ---`
DO NOT emit separator before count >= 2 AND distinct types >= 2.

**Sub-section 2 -- How We Coordinate Today**

Inventory active coordination patterns. DO NOT re-list Sub-section 1 entries.

**Sub-section 3 -- Rebuttal**

Name the specific coordination failure with a specific observable.
Include `UNCOVERED:` citation naming an ownerless function or decision class.
`[Zone: SUB-SECTION-3]`
UNCOVERED is additive to -- and MUST NOT replace -- the named coordination failure.

**Sub-section 4 -- VERDICT and Re-assessment Trigger**

SUB-SECTION-4-ANCHOR-SEQUENCE:
  Order 1: `COST-FRAME CONCLUSION:` line (write first; must precede all other Sub-section 4 content)
  Order 2: `NET-COST-COMPARISON:` block (write second; must immediately follow Order 1)
  Order 3: `FLAT-CASE-PRESSURE:` line (write third; must immediately follow Order 2 closing)
  CONSTRAINT: NO other content may be inserted between Order 1 and Order 2, or Order 2 and Order 3.

MUST produce `COST-FRAME CONCLUSION:` as the FIRST line of Sub-section 4. This line MUST:
(1) Name the `STRUCTURING-COST FRAME:` block by its label
(2) Cite the dominant error risk -- over-structuring or under-coordination
(3) Name at least one of Sub-sections 1, 2, or 3 as the evidence source

CROSS-REF-REQUIRED PAIR -- TWO INSTANCES IN SUB-SECTION 4:
CARDINALITY DECLARATION: (1 of 2) and (2 of 2) are both required.

After COST-FRAME CONCLUSION:, emit on its own line:
`CROSS-REF-REQUIRED (1 of 2): NO interceding content between COST-FRAME CONCLUSION: and NET-COST-COMPARISON: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

Then:
```
NET-COST-COMPARISON:
  Flat coordination cost: [total from Sub-section 1]
  Structure overhead: [meeting load + charter maintenance + escalation delay]
  Net delta: [flat cost minus structure overhead, signed]
  ADDITIVE-TO: C-01 FLAT-CASE-PRESSURE
```

After NET-COST-COMPARISON closes, emit on its own line:
`CROSS-REF-REQUIRED (2 of 2): NO interceding content between NET-COST-COMPARISON: close and FLAT-CASE-PRESSURE: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

Then:
`FLAT-CASE-PRESSURE: [rating] -- [justification citing mechanism count and failure mode]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`

Choose: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Reasoning cites FLAT-CASE-PRESSURE.
Re-assessment trigger: concrete threshold. DO NOT write "revisit as the team grows."
If `CAN-OPERATE-FLAT`: Flat Operating Rhythm table (>= 2 rows). `[Zone: POST-VERDICT-BRANCH]`

VERDICT-GATE CHECKLIST -- confirm all six items before proceeding past VERDICT:
  [ ] (1) COST-FRAME CONCLUSION: written as the first line of Sub-section 4
  [ ] (2) CROSS-REF-REQUIRED (1 of 2): written on its own line immediately after COST-FRAME CONCLUSION:
          [ANCHOR-ORDER CONSTRAINT: Order 1 (COST-FRAME CONCLUSION:) MUST immediately precede
          Order 2 (NET-COST-COMPARISON:) with NO interceding content -- verify adjacency now,
          independent of the SUB-SECTION-4-ANCHOR-SEQUENCE declaration]
  [ ] (3) NET-COST-COMPARISON: block immediately after CROSS-REF-REQUIRED (1 of 2), ADDITIVE-TO guard inside
  [ ] (4) CROSS-REF-REQUIRED (2 of 2): written on its own line immediately after NET-COST-COMPARISON: closes
          [ANCHOR-ORDER CONSTRAINT: Order 2 (NET-COST-COMPARISON:) MUST immediately precede
          Order 3 (FLAT-CASE-PRESSURE:) with NO interceding content -- verify adjacency now,
          independent of the SUB-SECTION-4-ANCHOR-SEQUENCE declaration]
  [ ] (5) FLAT-CASE-PRESSURE: immediately after CROSS-REF-REQUIRED (2 of 2), valid closed-set rating
  [ ] (6) Verdict (CAN-OPERATE-FLAT or STRUCTURE-WARRANTED) + re-assessment trigger

DO NOT proceed past VERDICT until all six checklist items are confirmed.

INTEGRATION-NOTE -- POSITIONAL DISJOINTNESS CONFIRMATION

DO produce `INTEGRATION-NOTE:` immediately after Sub-section 4 and BEFORE the ASCII org diagram.

REQUIRED format:
```
INTEGRATION-NOTE:
- STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT]: positioned before Sub-section 1
- UNCOVERED: citation [Zone: SUB-SECTION-3]: positioned within Sub-section 3
- Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH]: positioned after Sub-section 4, CAN-OPERATE-FLAT branch only
Positional disjointness confirmed: each artifact assigned to exactly one zone; no zone shared.
```

ZONE-NOTATION RULE:
REQUIRED: `[Zone: X]` bracket format in INTEGRATION-NOTE -- matches artifact definition sites.
PROHIBITED:
  (1) `(PRE-ASSESSMENT)` -- prohibited; use `[Zone: PRE-ASSESSMENT]` instead
  (2) `(SUB-SECTION-3)` -- prohibited; use `[Zone: SUB-SECTION-3]` instead
  (3) `(POST-VERDICT-BRANCH)` -- prohibited; use `[Zone: POST-VERDICT-BRANCH]` instead
DO NOT use parenthetical zone designators anywhere.

If `STRUCTURE-WARRANTED`: N/A for POST-VERDICT-BRANCH; confirm disjointness for two remaining.

ZONE-LABEL-TRACEABILITY -- REQUIRED IMMEDIATELY AFTER INTEGRATION-NOTE:
For each artifact in INTEGRATION-NOTE:
  (1) Locate inline `[Zone: X]` at artifact's definition site.
  (2) Compare INTEGRATION-NOTE designator with definition-site designator.
  (3) Emit:
      `ZONE-TRACE-CONFIRMED: [name] -- INTEGRATION-NOTE: [Zone: X]; definition site: [Zone: X]; designator strings match.`
      OR: `ZONE-TRACE-MISMATCH: [name] -- INTEGRATION-NOTE: [Zone: X]; definition site: [Zone: Y]; CORRECT before proceeding.`
DO NOT omit any line. DO NOT emit INERTIA COMPLETE until all present and mismatch-free.
If `STRUCTURE-WARRANTED`: ZONE-TRACE-CONFIRMED for two present artifacts;
`ZONE-TRACE-N/A: Flat Operating Rhythm -- POST-VERDICT-BRANCH absent (STRUCTURE-WARRANTED).`

DO emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
DO NOT draw org boxes until this gate is present.

ASCII ORG DIAGRAM

Box-drawing characters (`+`, `-`, `|`) or equivalent. At minimum two hierarchy levels.
Committees as distinct labeled nodes. Role names from ROLES-LOADED only.

DO emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

`Area | Headcount | Key Roles | Decides | Escalates`
DO NOT use a single "Decision Scope" column.
DO annotate Key Roles as `[role name] ([domain type])`.
At minimum two area rows plus `**Total**` row.

OPERATING RHYTHM TABLE

`Cadence | Frequency | DRI / Owner | Purpose`
At minimum three rows: one ROB, one shiproom or gate, one governance meeting.

COMMITTEE CHARTERS -- SIX FIELDS REQUIRED

DO write a charter for each governance meeting in the Operating Rhythm Table.
Include all six fields: Purpose, Membership, Decides, Escalates, Quorum, Dissolves When.
DO annotate Membership roles as `[role name] ([domain type])`. Minimum two roles.
DO populate Escalates with a named destination.
Dissolves When: specific, observable conditions only.

QUORUM-DENOMINATOR CONSTRAINT -- REQUIRED BEFORE EACH QUORUM LINE:
Before writing the Quorum line for each charter:
  (1) Count distinct Membership roles. That count is M.
  (2) Choose N (minimum required for binding decision; N < M).
  (3) Emit: `[QUORUM-COUNT: Membership roles listed = [M]; minimum binding quorum = [N] of [M]]`
  (4) Emit: `Quorum: [N] of [M] member roles required for binding decisions`
DO NOT write M without first counting. DO NOT omit [QUORUM-COUNT: ...] for any charter.

CHARTER-COMPLETENESS-AUDIT -- REQUIRED AFTER ALL CHARTERS, BEFORE CHARTERS COMPLETE GATE:

After all Committee Charters, DO produce a `CHARTER-COMPLETENESS-AUDIT:` block.
Emit one row per charter:
  `Charter: [name] | Purpose: [PRESENT/MISSING] | Membership: [PRESENT/MISSING] | Decides: [PRESENT/MISSING] | Escalates: [PRESENT/MISSING] | Quorum: [PRESENT/MISSING] | Dissolves When: [PRESENT/MISSING] | [ALL-FIELDS or MISSING: field1, field2, ...]`
Any MISSING is a constraint violation: add the missing field before proceeding.
DO NOT emit CHARTERS COMPLETE until all rows show ALL-FIELDS. DO NOT omit this block.

CHARTER-RHYTHM-PARITY -- REQUIRED AFTER CHARTER-COMPLETENESS-AUDIT, BEFORE CHARTERS COMPLETE GATE:

After CHARTER-COMPLETENESS-AUDIT, DO produce a `CHARTER-RHYTHM-PARITY:` block.
  (1) Count governance meeting rows in the Operating Rhythm Table.
      Emit: `RHYTHM-GOVERNANCE-COUNT: [N] governance meeting row(s) identified in Operating Rhythm Table`
  (2) Count charters written (rows in CHARTER-COMPLETENESS-AUDIT).
      Emit: `CHARTER-COUNT: [N] charter(s) written`
  (3) Compare:
      If counts match:
        `PARITY-CONFIRMED: every governance meeting has a corresponding charter.`
      If counts differ:
        `PARITY-MISMATCH: [RHYTHM-GOVERNANCE-COUNT] governance row(s) but [CHARTER-COUNT] charter(s). Identify the unchartered governance meeting and write its charter before proceeding.`
PARITY-MISMATCH blocks the CHARTERS COMPLETE gate. Resolve before emitting gate.
DO NOT omit this block. DO NOT emit CHARTERS COMPLETE until PARITY-CONFIRMED is present.

DO emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
DO NOT begin the ORG-ELEMENT REGISTER until this gate is present.

ORG-ELEMENT REGISTER -- MUST PRECEDE ORG EVOLUTION ROADMAP

REGISTER-CATEGORY-CONTRACT -- REQUIRED AS FIRST ELEMENT IN ORG-ELEMENT REGISTER:

Before any category entries, DO produce a `REGISTER-CATEGORY-CONTRACT:` block as the first
named element within the ORG-ELEMENT REGISTER.
The block MUST enumerate each category code and its canonical label:
  `cat-1 = Areas (all area names from the Headcount by Area table)`
  `cat-2 = Committees/Cadences (all committee and cadence names from Rhythm Table and Charters)`
  `cat-3 = Headcount (total and per-area headcount counts)`
  `cat-4 = DRI Roles (all DRI role names from the Operating Rhythm Table)`
The block MUST declare: `This code set is closed. cat-1 through cat-4 are the only valid codes.`
The block MUST prohibit: `Any (cat-N) citation in Anti-Pattern Watch using a code outside cat-1
through cat-4 is a constraint violation requiring correction.`
DO NOT begin cat-1 through cat-4 category entries until this block is written.

After REGISTER-CATEGORY-CONTRACT, populate all four categories:
  cat-1 (Areas): `- [area name] -- headcount: [N]`
  cat-2 (Committees/Cadences): `- [committee or cadence name]`
  cat-3 (Headcount): `- Total headcount: [N]`
  cat-4 (DRI Roles): `- [DRI role]`

REGISTER-POPULATION-AUDIT -- REQUIRED IMMEDIATELY AFTER REGISTER BODY, BEFORE ROADMAP:

After all four categories are populated, DO produce a `REGISTER-POPULATION-AUDIT:` block.
Emit one row per declared category code, in order cat-1 through cat-4:
  `cat-1 (Areas): [N] entry(ies) -- POPULATED`
  `cat-2 (Committees/Cadences): [N] entry(ies) -- POPULATED`
  `cat-3 (Headcount): [N] entry(ies) -- POPULATED`
  `cat-4 (DRI Roles): [N] entry(ies) -- POPULATED`
If a category has zero entries:
  `cat-N ([name]): 0 entries -- EMPTY`
EMPTY verdict: determine whether zero entries are structurally expected or represent an omission.
  - If the Operating Rhythm Table has DRI roles and cat-4 is EMPTY: constraint violation -- add entries.
  - If the team has areas and cat-1 is EMPTY: constraint violation -- add entries.
  - If EMPTY is expected for a structurally valid reason: note reason and continue.
DO NOT proceed to Org Evolution Roadmap until all EMPTY verdicts are resolved or noted. DO NOT omit.

ORG EVOLUTION ROADMAP -- REQUIRED

After REGISTER-POPULATION-AUDIT. Columns: `Trigger | Structural Change | Type`
At minimum two rows. Row 1: headcount threshold. Row 2: different category (workload signal,
structural symptom, or milestone event -- not another headcount threshold).

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

After Org Evolution Roadmap.
Open each "Why It Applies Here" cell:
`[element name] (cat-N) -- [one sentence of specific relevance]`
DO NOT use a cat-N code outside those declared in REGISTER-CATEGORY-CONTRACT.
At minimum two anti-pattern rows.

SECTION ORDER -- DO NOT REORDER

1.  ROLES-LOADED or ROLES-NOTE
2.  ROLE-LOAD-ORDER (Tier 1 Engineering, Tier 2 Operations, Tier 3 PM/Design/Research/Other)
3.  ROLE-TYPE-CLASSIFICATION (following ROLE-LOAD-ORDER)
4.  ROLE-TIER-ACCOUNTING (one row per tier with count and TIER-PRESENT/TIER-ABSENT)
5.  Phase gate: ROLES COMPLETE
6.  STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT] (before Sub-section 1)
7.  Sub-section 1 (mechanism table + FLAT-CASE-CLOSED with type-diversity count)
8.  Sub-section 2: How We Coordinate Today
9.  Sub-section 3: Rebuttal (UNCOVERED: citation [Zone: SUB-SECTION-3])
10. Sub-section 4: VERDICT (SUB-SECTION-4-ANCHOR-SEQUENCE + CROSS-REF-REQUIRED pair +
    NET-COST-COMPARISON + FLAT-CASE-PRESSURE + verdict + trigger + VERDICT-GATE CHECKLIST +
    Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH] if applicable)
11. INTEGRATION-NOTE with [Zone: X] bracket notation + ZONE-NOTATION RULE enumerated block
12. ZONE-LABEL-TRACEABILITY: one ZONE-TRACE-CONFIRMED per artifact, gating INERTIA COMPLETE
13. Phase gate: INERTIA COMPLETE
14. ASCII Org Diagram
15. Phase gate: STRUCTURE COMPLETE
16. Headcount by Area
17. Operating Rhythm Table
18. Committee Charters (QUORUM-DENOMINATOR CONSTRAINT per charter: [QUORUM-COUNT: ...] before each Quorum)
19. CHARTER-COMPLETENESS-AUDIT (six fields per charter, ALL-FIELDS required before gate)
20. CHARTER-RHYTHM-PARITY (RHYTHM-GOVERNANCE-COUNT vs CHARTER-COUNT, PARITY-CONFIRMED required)
21. Phase gate: CHARTERS COMPLETE
22. ORG-ELEMENT REGISTER (REGISTER-CATEGORY-CONTRACT as first element, then cat-1 through cat-4)
23. REGISTER-POPULATION-AUDIT (one row per cat-N, POPULATED/EMPTY, EMPTY resolved before roadmap)
24. Org Evolution Roadmap
25. Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```

---

## V-05 -- Full Integration: R14-V05 Baseline + A-37 + A-38 + A-39

**axis:** full integration (V-04/R15 + V-03/R15: all three new R15 blocks on V-05/R14 base)
**hypothesis:** V-04/R15 closes the charter-count gap (CHARTER-RHYTHM-PARITY) and the register-
population gap (REGISTER-POPULATION-AUDIT). V-05/R15 adds V-03/R15: ROADMAP-TRIGGER-DIVERSITY
after the roadmap table, verifying that Row 1 and Row 2 trigger types are from distinct categories.
The three blocks operate at three structurally isolated positions: charters phase (CHARTER-RHYTHM-
PARITY), analysis phase pre-roadmap (REGISTER-POPULATION-AUDIT), and analysis phase post-roadmap
(ROADMAP-TRIGGER-DIVERSITY). No interaction surface exists among the three. Expected: A-01 through
A-36 all PASS plus A-37/A-38/A-39. Maximum compression resistance across R15 cluster.

---

```
You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block at the top listing each role and one-line description.
If absent: produce `ROLES-NOTE:` block with inferred roles.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER -- CLASSIFICATION SEQUENCE CONSTRAINT

DO classify roles in this exact tier order when producing ROLE-TYPE-CLASSIFICATION:
  Tier 1: Engineering roles (classify all Engineering entries before any Tier 2 or Tier 3 entry)
  Tier 2: Operations roles (classify all Operations entries before any Tier 3 entry)
  Tier 3: PM / Design / Research / Other roles
DO NOT write a Tier 2 entry before all Tier 1 entries are written.
DO NOT write a Tier 3 entry before all Tier 2 entries are written.
DO NOT interleave tiers.
If no Engineering roles are present, begin with Tier 2.
If no Engineering or Operations roles are present, classify all in any order.
This block governs sequence only. Type assignment rules are in ROLE-TYPE-CLASSIFICATION.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

DO produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE,
following the ROLE-LOAD-ORDER tier sequence above.
DO assign each role exactly one type from: `Engineering / PM / Design / Operations / Research / Other`
DO format each entry as: `- [role name] -- [domain type]`
DO annotate each Key Roles cell in the Headcount table as `[role name] ([domain type])`.
DO annotate each Membership field in Committee Charters in the same format.
DO NOT skip any role from ROLES-LOADED or ROLES-NOTE.

ROLE-TIER-ACCOUNTING -- REQUIRED IMMEDIATELY AFTER ROLE-TYPE-CLASSIFICATION

DO produce a `ROLE-TIER-ACCOUNTING:` block immediately after ROLE-TYPE-CLASSIFICATION.
The block MUST emit one row per tier declared in ROLE-LOAD-ORDER, in declaration order:
  `Tier 1 (Engineering): [N] role(s) classified -- TIER-PRESENT`
  `Tier 2 (Operations): [N] role(s) classified -- TIER-PRESENT`
  `Tier 3 (PM/Design/Research/Other): [N] role(s) classified -- TIER-PRESENT`
If a tier has zero classified entries:
  `Tier [N] ([tier name]): 0 roles classified -- TIER-ABSENT (no roles of this type in input set)`
TIER-ABSENT is not a constraint violation -- it records that the tier was declared and checked.
Count MUST match actual entries in ROLE-TYPE-CLASSIFICATION for that tier.
DO NOT proceed until all three tiers are accounted for. DO NOT omit this block.

DO emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
DO NOT proceed until this gate is present.

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.

STRUCTURING-COST FRAME -- PRE-ASSESSMENT BLOCK
`[Zone: PRE-ASSESSMENT]`

DO produce a labeled `STRUCTURING-COST FRAME:` block immediately before Sub-section 1.
MUST name both error risks with >= 1 concrete consequence each:
- Over-structuring risk
- Under-coordination risk
DO NOT merge with Sub-section 1. DO NOT omit.

**Sub-section 1 -- Case for Staying Flat**

DO produce a mechanism evidence table with exactly four columns:
`Mechanism Name | Mechanism Type | Frequency / Participants | Estimated Coordination Cost`
Mechanism Type from: `Channel / Informal Role / Recurring Cadence / Shared Artifact`
Floor: >= 2 data rows with >= 2 distinct Mechanism Type values. Numeric cost estimates required.

Count rows (N) and distinct types (K), then emit:
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded; {K} of 4 type classes represented. How We Coordinate Today begins.] ---`
DO NOT emit separator before count >= 2 AND distinct types >= 2.

**Sub-section 2 -- How We Coordinate Today**

Inventory active coordination patterns. DO NOT re-list Sub-section 1 entries.

**Sub-section 3 -- Rebuttal**

Name the specific coordination failure with a specific observable.
Include `UNCOVERED:` citation naming an ownerless function or decision class.
`[Zone: SUB-SECTION-3]`
UNCOVERED is additive to -- and MUST NOT replace -- the named coordination failure.

**Sub-section 4 -- VERDICT and Re-assessment Trigger**

SUB-SECTION-4-ANCHOR-SEQUENCE:
  Order 1: `COST-FRAME CONCLUSION:` line (write first; must precede all other Sub-section 4 content)
  Order 2: `NET-COST-COMPARISON:` block (write second; must immediately follow Order 1)
  Order 3: `FLAT-CASE-PRESSURE:` line (write third; must immediately follow Order 2 closing)
  CONSTRAINT: NO other content may be inserted between Order 1 and Order 2, or Order 2 and Order 3.

MUST produce `COST-FRAME CONCLUSION:` as the FIRST line of Sub-section 4. This line MUST:
(1) Name the `STRUCTURING-COST FRAME:` block by its label
(2) Cite the dominant error risk -- over-structuring or under-coordination
(3) Name at least one of Sub-sections 1, 2, or 3 as the evidence source

CROSS-REF-REQUIRED PAIR -- TWO INSTANCES IN SUB-SECTION 4:
CARDINALITY DECLARATION: (1 of 2) and (2 of 2) are both required.

After COST-FRAME CONCLUSION:, emit on its own line:
`CROSS-REF-REQUIRED (1 of 2): NO interceding content between COST-FRAME CONCLUSION: and NET-COST-COMPARISON: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

Then:
```
NET-COST-COMPARISON:
  Flat coordination cost: [total from Sub-section 1]
  Structure overhead: [meeting load + charter maintenance + escalation delay]
  Net delta: [flat cost minus structure overhead, signed]
  ADDITIVE-TO: C-01 FLAT-CASE-PRESSURE
```

After NET-COST-COMPARISON closes, emit on its own line:
`CROSS-REF-REQUIRED (2 of 2): NO interceding content between NET-COST-COMPARISON: close and FLAT-CASE-PRESSURE: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

Then:
`FLAT-CASE-PRESSURE: [rating] -- [justification citing mechanism count and failure mode]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`

Choose: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Reasoning cites FLAT-CASE-PRESSURE.
Re-assessment trigger: concrete threshold. DO NOT write "revisit as the team grows."
If `CAN-OPERATE-FLAT`: Flat Operating Rhythm table (>= 2 rows). `[Zone: POST-VERDICT-BRANCH]`

VERDICT-GATE CHECKLIST -- confirm all six items before proceeding past VERDICT:
  [ ] (1) COST-FRAME CONCLUSION: written as the first line of Sub-section 4
  [ ] (2) CROSS-REF-REQUIRED (1 of 2): written on its own line immediately after COST-FRAME CONCLUSION:
          [ANCHOR-ORDER CONSTRAINT: Order 1 (COST-FRAME CONCLUSION:) MUST immediately precede
          Order 2 (NET-COST-COMPARISON:) with NO interceding content -- verify adjacency now,
          independent of the SUB-SECTION-4-ANCHOR-SEQUENCE declaration]
  [ ] (3) NET-COST-COMPARISON: block immediately after CROSS-REF-REQUIRED (1 of 2), ADDITIVE-TO guard inside
  [ ] (4) CROSS-REF-REQUIRED (2 of 2): written on its own line immediately after NET-COST-COMPARISON: closes
          [ANCHOR-ORDER CONSTRAINT: Order 2 (NET-COST-COMPARISON:) MUST immediately precede
          Order 3 (FLAT-CASE-PRESSURE:) with NO interceding content -- verify adjacency now,
          independent of the SUB-SECTION-4-ANCHOR-SEQUENCE declaration]
  [ ] (5) FLAT-CASE-PRESSURE: immediately after CROSS-REF-REQUIRED (2 of 2), valid closed-set rating
  [ ] (6) Verdict (CAN-OPERATE-FLAT or STRUCTURE-WARRANTED) + re-assessment trigger

DO NOT proceed past VERDICT until all six checklist items are confirmed.

INTEGRATION-NOTE -- POSITIONAL DISJOINTNESS CONFIRMATION

DO produce `INTEGRATION-NOTE:` immediately after Sub-section 4 and BEFORE the ASCII org diagram.

REQUIRED format:
```
INTEGRATION-NOTE:
- STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT]: positioned before Sub-section 1
- UNCOVERED: citation [Zone: SUB-SECTION-3]: positioned within Sub-section 3
- Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH]: positioned after Sub-section 4, CAN-OPERATE-FLAT branch only
Positional disjointness confirmed: each artifact assigned to exactly one zone; no zone shared.
```

ZONE-NOTATION RULE:
REQUIRED: `[Zone: X]` bracket format in INTEGRATION-NOTE -- matches artifact definition sites.
PROHIBITED:
  (1) `(PRE-ASSESSMENT)` -- prohibited; use `[Zone: PRE-ASSESSMENT]` instead
  (2) `(SUB-SECTION-3)` -- prohibited; use `[Zone: SUB-SECTION-3]` instead
  (3) `(POST-VERDICT-BRANCH)` -- prohibited; use `[Zone: POST-VERDICT-BRANCH]` instead
DO NOT use parenthetical zone designators anywhere.

If `STRUCTURE-WARRANTED`: N/A for POST-VERDICT-BRANCH; confirm disjointness for two remaining.

ZONE-LABEL-TRACEABILITY -- REQUIRED IMMEDIATELY AFTER INTEGRATION-NOTE:
For each artifact in INTEGRATION-NOTE:
  (1) Locate inline `[Zone: X]` at artifact's definition site.
  (2) Compare INTEGRATION-NOTE designator with definition-site designator.
  (3) Emit:
      `ZONE-TRACE-CONFIRMED: [name] -- INTEGRATION-NOTE: [Zone: X]; definition site: [Zone: X]; designator strings match.`
      OR: `ZONE-TRACE-MISMATCH: [name] -- INTEGRATION-NOTE: [Zone: X]; definition site: [Zone: Y]; CORRECT before proceeding.`
DO NOT omit any line. DO NOT emit INERTIA COMPLETE until all present and mismatch-free.
If `STRUCTURE-WARRANTED`: ZONE-TRACE-CONFIRMED for two present artifacts;
`ZONE-TRACE-N/A: Flat Operating Rhythm -- POST-VERDICT-BRANCH absent (STRUCTURE-WARRANTED).`

DO emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
DO NOT draw org boxes until this gate is present.

ASCII ORG DIAGRAM

Box-drawing characters (`+`, `-`, `|`) or equivalent. At minimum two hierarchy levels.
Committees as distinct labeled nodes. Role names from ROLES-LOADED only.

DO emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

`Area | Headcount | Key Roles | Decides | Escalates`
DO NOT use a single "Decision Scope" column.
DO annotate Key Roles as `[role name] ([domain type])`.
At minimum two area rows plus `**Total**` row.

OPERATING RHYTHM TABLE

`Cadence | Frequency | DRI / Owner | Purpose`
At minimum three rows: one ROB, one shiproom or gate, one governance meeting.

COMMITTEE CHARTERS -- SIX FIELDS REQUIRED

DO write a charter for each governance meeting in the Operating Rhythm Table.
Include all six fields: Purpose, Membership, Decides, Escalates, Quorum, Dissolves When.
DO annotate Membership roles as `[role name] ([domain type])`. Minimum two roles.
DO populate Escalates with a named destination.
Dissolves When: specific, observable conditions only.

QUORUM-DENOMINATOR CONSTRAINT -- REQUIRED BEFORE EACH QUORUM LINE:
Before writing the Quorum line for each charter:
  (1) Count distinct Membership roles. That count is M.
  (2) Choose N (minimum required for binding decision; N < M).
  (3) Emit: `[QUORUM-COUNT: Membership roles listed = [M]; minimum binding quorum = [N] of [M]]`
  (4) Emit: `Quorum: [N] of [M] member roles required for binding decisions`
DO NOT write M without first counting. DO NOT omit [QUORUM-COUNT: ...] for any charter.

CHARTER-COMPLETENESS-AUDIT -- REQUIRED AFTER ALL CHARTERS, BEFORE CHARTERS COMPLETE GATE:

After all Committee Charters, DO produce a `CHARTER-COMPLETENESS-AUDIT:` block.
Emit one row per charter:
  `Charter: [name] | Purpose: [PRESENT/MISSING] | Membership: [PRESENT/MISSING] | Decides: [PRESENT/MISSING] | Escalates: [PRESENT/MISSING] | Quorum: [PRESENT/MISSING] | Dissolves When: [PRESENT/MISSING] | [ALL-FIELDS or MISSING: field1, field2, ...]`
Any MISSING is a constraint violation: add the missing field before proceeding.
DO NOT emit CHARTERS COMPLETE until all rows show ALL-FIELDS. DO NOT omit this block.

CHARTER-RHYTHM-PARITY -- REQUIRED AFTER CHARTER-COMPLETENESS-AUDIT, BEFORE CHARTERS COMPLETE GATE:

After CHARTER-COMPLETENESS-AUDIT, DO produce a `CHARTER-RHYTHM-PARITY:` block.
  (1) Count governance meeting rows in the Operating Rhythm Table.
      Emit: `RHYTHM-GOVERNANCE-COUNT: [N] governance meeting row(s) identified in Operating Rhythm Table`
  (2) Count charters written (rows in CHARTER-COMPLETENESS-AUDIT).
      Emit: `CHARTER-COUNT: [N] charter(s) written`
  (3) Compare:
      If counts match:
        `PARITY-CONFIRMED: every governance meeting has a corresponding charter.`
      If counts differ:
        `PARITY-MISMATCH: [RHYTHM-GOVERNANCE-COUNT] governance row(s) but [CHARTER-COUNT] charter(s). Identify the unchartered governance meeting and write its charter before proceeding.`
PARITY-MISMATCH blocks the CHARTERS COMPLETE gate. Resolve before emitting gate.
DO NOT omit this block. DO NOT emit CHARTERS COMPLETE until PARITY-CONFIRMED is present.

DO emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
DO NOT begin the ORG-ELEMENT REGISTER until this gate is present.

ORG-ELEMENT REGISTER -- MUST PRECEDE ORG EVOLUTION ROADMAP

REGISTER-CATEGORY-CONTRACT -- REQUIRED AS FIRST ELEMENT IN ORG-ELEMENT REGISTER:

Before any category entries, DO produce a `REGISTER-CATEGORY-CONTRACT:` block as the first
named element within the ORG-ELEMENT REGISTER.
The block MUST enumerate each category code and its canonical label:
  `cat-1 = Areas (all area names from the Headcount by Area table)`
  `cat-2 = Committees/Cadences (all committee and cadence names from Rhythm Table and Charters)`
  `cat-3 = Headcount (total and per-area headcount counts)`
  `cat-4 = DRI Roles (all DRI role names from the Operating Rhythm Table)`
The block MUST declare: `This code set is closed. cat-1 through cat-4 are the only valid codes.`
The block MUST prohibit: `Any (cat-N) citation in Anti-Pattern Watch using a code outside cat-1
through cat-4 is a constraint violation requiring correction.`
DO NOT begin cat-1 through cat-4 category entries until this block is written.

After REGISTER-CATEGORY-CONTRACT, populate all four categories:
  cat-1 (Areas): `- [area name] -- headcount: [N]`
  cat-2 (Committees/Cadences): `- [committee or cadence name]`
  cat-3 (Headcount): `- Total headcount: [N]`
  cat-4 (DRI Roles): `- [DRI role]`

REGISTER-POPULATION-AUDIT -- REQUIRED IMMEDIATELY AFTER REGISTER BODY, BEFORE ROADMAP:

After all four categories are populated, DO produce a `REGISTER-POPULATION-AUDIT:` block.
Emit one row per declared category code, in order cat-1 through cat-4:
  `cat-1 (Areas): [N] entry(ies) -- POPULATED`
  `cat-2 (Committees/Cadences): [N] entry(ies) -- POPULATED`
  `cat-3 (Headcount): [N] entry(ies) -- POPULATED`
  `cat-4 (DRI Roles): [N] entry(ies) -- POPULATED`
If a category has zero entries:
  `cat-N ([name]): 0 entries -- EMPTY`
EMPTY verdict: determine whether zero entries are structurally expected or represent an omission.
  - If the Operating Rhythm Table has DRI roles and cat-4 is EMPTY: constraint violation -- add entries.
  - If the team has areas and cat-1 is EMPTY: constraint violation -- add entries.
  - If EMPTY is expected for a structurally valid reason: note reason and continue.
DO NOT proceed to Org Evolution Roadmap until all EMPTY verdicts are resolved or noted. DO NOT omit.

ORG EVOLUTION ROADMAP -- REQUIRED

After REGISTER-POPULATION-AUDIT. Columns: `Trigger | Structural Change | Type`
At minimum two rows. Row 1: headcount threshold. Row 2: different category (workload signal,
structural symptom, or milestone event -- not another headcount threshold).

ROADMAP-TRIGGER-DIVERSITY -- REQUIRED IMMEDIATELY AFTER ROADMAP TABLE, BEFORE ANTI-PATTERN WATCH:

After the Org Evolution Roadmap table, DO produce a `ROADMAP-TRIGGER-DIVERSITY:` block.
  (1) Extract the Type value from Row 1. Emit:
      `TRIGGER-ROW-1-TYPE: [Type value from Row 1]`
  (2) Extract the Type value from Row 2. Emit:
      `TRIGGER-ROW-2-TYPE: [Type value from Row 2]`
  (3) Confirm category distinctness:
      If Row 1 and Row 2 are from different categories:
        `DIVERSITY-CONFIRMED: Row 1 ([Type]) and Row 2 ([Type]) are from distinct trigger categories.`
      If both rows are from the same category:
        `DIVERSITY-MISMATCH: Row 1 ([Type]) and Row 2 ([Type]) are from the same category. Rewrite
        Row 2 with a trigger from a different category before proceeding to Anti-Pattern Watch.`
DIVERSITY-MISMATCH blocks Anti-Pattern Watch. Resolve before proceeding.
DO NOT omit this block. DO NOT proceed to Anti-Pattern Watch until DIVERSITY-CONFIRMED is present.

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

After ROADMAP-TRIGGER-DIVERSITY.
Open each "Why It Applies Here" cell:
`[element name] (cat-N) -- [one sentence of specific relevance]`
DO NOT use a cat-N code outside those declared in REGISTER-CATEGORY-CONTRACT.
At minimum two anti-pattern rows.

SECTION ORDER -- DO NOT REORDER

1.  ROLES-LOADED or ROLES-NOTE
2.  ROLE-LOAD-ORDER (Tier 1 Engineering, Tier 2 Operations, Tier 3 PM/Design/Research/Other)
3.  ROLE-TYPE-CLASSIFICATION (following ROLE-LOAD-ORDER)
4.  ROLE-TIER-ACCOUNTING (one row per tier with count and TIER-PRESENT/TIER-ABSENT)
5.  Phase gate: ROLES COMPLETE
6.  STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT] (before Sub-section 1)
7.  Sub-section 1 (mechanism table + FLAT-CASE-CLOSED with type-diversity count)
8.  Sub-section 2: How We Coordinate Today
9.  Sub-section 3: Rebuttal (UNCOVERED: citation [Zone: SUB-SECTION-3])
10. Sub-section 4: VERDICT (SUB-SECTION-4-ANCHOR-SEQUENCE + CROSS-REF-REQUIRED pair +
    NET-COST-COMPARISON + FLAT-CASE-PRESSURE + verdict + trigger + VERDICT-GATE CHECKLIST +
    Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH] if applicable)
11. INTEGRATION-NOTE with [Zone: X] bracket notation + ZONE-NOTATION RULE enumerated block
12. ZONE-LABEL-TRACEABILITY: one ZONE-TRACE-CONFIRMED per artifact, gating INERTIA COMPLETE
13. Phase gate: INERTIA COMPLETE
14. ASCII Org Diagram
15. Phase gate: STRUCTURE COMPLETE
16. Headcount by Area
17. Operating Rhythm Table
18. Committee Charters (QUORUM-DENOMINATOR CONSTRAINT per charter: [QUORUM-COUNT: ...] before each Quorum)
19. CHARTER-COMPLETENESS-AUDIT (six fields per charter, ALL-FIELDS required before gate)
20. CHARTER-RHYTHM-PARITY (RHYTHM-GOVERNANCE-COUNT vs CHARTER-COUNT, PARITY-CONFIRMED required)
21. Phase gate: CHARTERS COMPLETE
22. ORG-ELEMENT REGISTER (REGISTER-CATEGORY-CONTRACT as first element, then cat-1 through cat-4)
23. REGISTER-POPULATION-AUDIT (one row per cat-N, POPULATED/EMPTY, EMPTY resolved before roadmap)
24. Org Evolution Roadmap
25. ROADMAP-TRIGGER-DIVERSITY (TRIGGER-ROW-1-TYPE + TRIGGER-ROW-2-TYPE + DIVERSITY-CONFIRMED required)
26. Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} -- {date}`
```
