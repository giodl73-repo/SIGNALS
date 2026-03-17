---
skill: quest-variate
skill_target: org-chart
date: 2026-03-16
round: R14
rubric_version: v13
status: variate
---

# org-chart Variate -- Round 14

**Date:** 2026-03-16
**Skill:** org-chart
**Rubric:** v13 (A-01 through A-33; A-31/A-32/A-33 new from R13)
**Round:** R14 -- single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

**R13 ceiling under v13:**
V-05/R13 achieves 33/33 aspirationally under rubric v13 (composite 100.0).
A-31 is satisfied via a named `ROLE-LOAD-ORDER:` block between ROLES-LOADED and ROLE-TYPE-CLASSIFICATION,
making three-tier ordering an independently detectable structural contract. A-32 is satisfied via a
`QUORUM-DENOMINATOR CONSTRAINT:` block before each Quorum line with an explicit `[QUORUM-COUNT: ...]`
verification inline binding M to the declared Membership count. A-33 is satisfied via a
`ZONE-LABEL-TRACEABILITY` verification step after INTEGRATION-NOTE, requiring one
`ZONE-TRACE-CONFIRMED:` line per artifact with INTEGRATION-NOTE designator and definition-site
designator side-by-side, gating the INERTIA COMPLETE phase gate.

**R14 target:** 33/33 aspirationally with new compression resistance gains beyond A-31/A-32/A-33.
Three structural gaps remain in V-05/R13 not yet captured by any criterion:

1. **Role-tier population verification gap:** A-31 makes the ROLE-LOAD-ORDER a named block
   declaring the three-tier sequence and prohibiting out-of-sequence entries. ROLE-TYPE-CLASSIFICATION
   follows the declared tier sequence. But after classification is complete, there is no
   production-time count verification confirming each declared tier is actually populated. A tier
   declared in ROLE-LOAD-ORDER can have zero entries in ROLE-TYPE-CLASSIFICATION without any labeled
   flag -- the tier is listed in the declaration but absent from the produced output, and this absence
   is detectable only by counting entries in ROLE-TYPE-CLASSIFICATION, not from any dedicated
   verification artifact. A `ROLE-TIER-ACCOUNTING:` block immediately after ROLE-TYPE-CLASSIFICATION
   -- one row per declared tier with actual classification count and a TIER-PRESENT/TIER-ABSENT verdict
   -- promotes tier-completeness from an implicit structural property to an explicitly emitted
   verification record.

2. **Charter field completeness cross-charter sweep gap:** C-03 requires five fields per charter;
   A-13 requires a Dissolves When sixth field; A-32 binds the Quorum denominator per charter. All
   three requirements are enforced per-charter at production time. But no production artifact confirms
   completeness simultaneously across all charters: under compression, a field can drop from a later
   charter while early charters remain compliant, and the drop is detectable only by reading each
   charter individually. A `CHARTER-COMPLETENESS-AUDIT:` block after all charters and before the
   CHARTERS COMPLETE gate -- one row per charter with per-field PRESENT/MISSING cells -- converts
   cross-charter field completeness from an implicit scan requirement into an independently verifiable
   table.

3. **ORG-ELEMENT REGISTER category-contract declaration gap:** The ORG-ELEMENT REGISTER presents a
   descriptive "Category schema" table with cat-1 through cat-4 and their element types. Anti-Pattern
   Watch requires `(cat-N)` typed citations and the constraint "DO NOT use a cat-N code not in the
   ORG-ELEMENT REGISTER schema" enforces correctness. But the category schema is a descriptive table
   embedded inside the register, not a standalone named contract block. Its boundary is implicit:
   cat-1 through cat-4 are the schema, but no named block declares this closed set and prohibits
   extension. A `REGISTER-CATEGORY-CONTRACT:` block at the top of the ORG-ELEMENT REGISTER -- before
   any category entries, explicitly naming each code with its label and declaring the set closed --
   promotes the schema from a descriptive table to an independently parseable contract whose absence
   is detectable as a structural gap rather than as a missing table row.

**Three questions drive R14:**

1. Does a `ROLE-TIER-ACCOUNTING:` block (V-01) -- requiring one row per tier declared in
   ROLE-LOAD-ORDER with an actual classification count and TIER-PRESENT/TIER-ABSENT verdict,
   placed immediately after ROLE-TYPE-CLASSIFICATION -- make tier-completeness a directly scannable
   artifact rather than an implicit property of the classification entry sequence? (V-01)

2. Does a `CHARTER-COMPLETENESS-AUDIT:` block (V-02) -- requiring one row per charter with
   per-field PRESENT/MISSING cells covering all six fields, placed after all charters and before
   the CHARTERS COMPLETE gate -- make cross-charter field completeness independently verifiable by
   inspection without reading each charter individually? (V-02)

3. Does a `REGISTER-CATEGORY-CONTRACT:` block (V-03) -- placed at the top of the ORG-ELEMENT
   REGISTER before any category entries, naming each cat-N code explicitly with its category label
   and declaring the set closed -- convert the implicit schema table into an independently named
   declared contract whose absence is structurally detectable? (V-03)

V-04/R14 combines V-01 (ROLE-TIER-ACCOUNTING) + V-02 (CHARTER-COMPLETENESS-AUDIT) on V-05/R13 base.
V-05/R14 is full integration: V-05/R13 base + all three improvements together.

---

## Round 14 Variation Map

| V | Axis | What Changes vs V-05/R13 | Hypothesis |
|---|------|--------------------------|------------|
| V-01 | role sequence | Add `ROLE-TIER-ACCOUNTING:` block immediately after ROLE-TYPE-CLASSIFICATION; one row per tier declared in ROLE-LOAD-ORDER with actual classification count and TIER-PRESENT/TIER-ABSENT verdict. | A-31 establishes declared tier sequence but no count-per-tier verification follows. Named accounting block makes tier-population gap detectable as a missing count row rather than a silent empty-tier. Expected: A-34 PASS. All others unchanged from V-05/R13. Composite: 33/33. |
| V-02 | lifecycle emphasis | Add `CHARTER-COMPLETENESS-AUDIT:` block after all Committee Charters and before CHARTERS COMPLETE gate; one row per charter with PRESENT/MISSING per field for all six required fields. | C-03/A-13/A-32 enforce field requirements per-charter; no cross-charter sweep exists. Completeness audit makes any missing field scannable across all charters simultaneously. Expected: A-35 PASS. All others unchanged. Composite: 33/33. |
| V-03 | output format | Add `REGISTER-CATEGORY-CONTRACT:` block as first element in ORG-ELEMENT REGISTER, before any category entries; names each cat-N code with its canonical category label; declares the code set as closed; prohibits unlisted codes. | Category schema exists as descriptive table but not as a standalone named contract. Named contract block makes schema boundary structurally detectable. Expected: A-36 PASS. All others unchanged. Composite: 33/33. |
| V-04 | combined | V-05/R13 base + V-01 (ROLE-TIER-ACCOUNTING) + V-02 (CHARTER-COMPLETENESS-AUDIT). | Both improvements operate at structurally isolated positions (roles phase vs charters phase). No interaction surface. Expected: 33/33. |
| V-05 | full integration | V-05/R13 base + V-01 (ROLE-TIER-ACCOUNTING) + V-02 (CHARTER-COMPLETENESS-AUDIT) + V-03 (REGISTER-CATEGORY-CONTRACT). | Maximum compression resistance: A-34 via tier accounting, A-35 via charter completeness audit, A-36 via named category contract. Expected: 33/33, maximum robustness across A-34/A-35/A-36 cluster. |

---

## V-01 -- Role Sequence: ROLE-TIER-ACCOUNTING Count Verification Block

**axis:** role sequence (ROLE-TIER-ACCOUNTING block immediately after ROLE-TYPE-CLASSIFICATION;
one row per tier declared in ROLE-LOAD-ORDER with actual classification count and
TIER-PRESENT/TIER-ABSENT verdict)
**hypothesis:** V-05/R13 satisfies A-31 via a named `ROLE-LOAD-ORDER:` block declaring tier sequence
before ROLE-TYPE-CLASSIFICATION, with inter-tier ordering prohibition. The sequence is declared; the
classification follows it. But after classification completes, no production-time verification confirms
each declared tier is populated. A tier declared in ROLE-LOAD-ORDER with zero ROLE-TYPE-CLASSIFICATION
entries produces no labeled gap signal: the block declares it, the classification simply has no entries
of that type, and the discrepancy is detectable only by parsing classification entries against the
declaration. V-01/R14 adds a `ROLE-TIER-ACCOUNTING:` block immediately after ROLE-TYPE-CLASSIFICATION
-- one row per tier from ROLE-LOAD-ORDER with the actual count and TIER-PRESENT or TIER-ABSENT verdict.
A zero-count tier emits TIER-ABSENT, making the population gap a directly scannable row rather than a
silent absence. All other criteria unchanged from V-05/R13. Expected: A-01 through A-33 all PASS.
Composite: 33/33.

---

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
If a tier has zero classified entries, emit:
  `Tier [N] ([tier name]): 0 roles classified -- TIER-ABSENT (no roles of this type in input set)`
TIER-ABSENT is not a constraint violation -- it records that the tier was declared and checked.
The count in each row MUST match the actual number of entries in that tier in ROLE-TYPE-CLASSIFICATION.
DO NOT proceed past this block until all three tiers declared in ROLE-LOAD-ORDER are accounted for.
DO NOT omit this block.

DO emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
DO NOT proceed until this gate is present.

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.

STRUCTURING-COST FRAME -- PRE-ASSESSMENT BLOCK
`[Zone: PRE-ASSESSMENT]`

DO produce a labeled `STRUCTURING-COST FRAME:` block immediately before Sub-section 1.
MUST name both error risks:
- Over-structuring risk: principal risk of introducing structure prematurely, with >= 1
  concrete consequence
- Under-coordination risk: principal risk of staying flat too long, with >= 1 concrete
  consequence
DO NOT merge this block with Sub-section 1. DO NOT omit.

**Sub-section 1 -- Case for Staying Flat**

DO produce a mechanism evidence table with exactly four columns:
`Mechanism Name | Mechanism Type | Frequency / Participants | Estimated Coordination Cost`
The `Mechanism Type` column MUST use only values from this closed set:
`Channel / Informal Role / Recurring Cadence / Shared Artifact`
Floor: >= 2 data rows with >= 2 distinct Mechanism Type values.
DO populate Estimated Coordination Cost with numeric estimates per mechanism.

After the table, count rows (N) and distinct Mechanism Type values (K), then emit exactly:
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded; {K} of 4 type classes represented. How We Coordinate Today begins.] ---`
DO NOT emit this separator before: count >= 2 AND distinct types >= 2.
DO NOT begin Sub-section 2 until this separator is present.

**Sub-section 2 -- How We Coordinate Today**

DO inventory coordination patterns currently in active use.
DO NOT re-list mechanism table entries from Sub-section 1.

**Sub-section 3 -- Rebuttal**

DO name the coordination failure the flat case and current mechanisms cannot answer.
DO reference a specific observable: blocked decision, missed SLA, time-zone gap, knowledge
silo, or competing roadmap conflict.
DO include an `UNCOVERED:` citation naming at least one ownerless function or decision class.
`[Zone: SUB-SECTION-3]`
UNCOVERED is additive to -- and MUST NOT replace -- the named coordination failure.

**Sub-section 4 -- VERDICT and Re-assessment Trigger**

SUB-SECTION-4-ANCHOR-SEQUENCE:
  Order 1: `COST-FRAME CONCLUSION:` line (write first; must precede all other Sub-section 4 content)
  Order 2: `NET-COST-COMPARISON:` block (write second; must immediately follow Order 1)
  Order 3: `FLAT-CASE-PRESSURE:` line (write third; must immediately follow Order 2 closing)
  CONSTRAINT: NO other content may be inserted between Order 1 and Order 2, or Order 2 and Order 3.

MUST produce `COST-FRAME CONCLUSION:` as the FIRST line of Sub-section 4. This line MUST:
(1) Name the `STRUCTURING-COST FRAME:` block by its label as the source of the evaluation frame
(2) Cite the dominant error risk -- over-structuring or under-coordination
(3) Name at least one of Sub-sections 1, 2, or 3 as the evidence source

CROSS-REF-REQUIRED PAIR -- TWO INSTANCES REQUIRED IN SUB-SECTION 4:
CARDINALITY DECLARATION: this pair has exactly 2 members; (1 of 2) and (2 of 2) are both required.

After writing `COST-FRAME CONCLUSION:`, emit the following on its own line:
`CROSS-REF-REQUIRED (1 of 2): NO interceding content between COST-FRAME CONCLUSION: and NET-COST-COMPARISON: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

Then produce the NET-COST-COMPARISON block:

```
NET-COST-COMPARISON:
  Flat coordination cost: [total from Sub-section 1 mechanism table, in stated units]
  Structure overhead: [meeting load + charter maintenance + escalation delay]
  Net delta: [flat cost minus structure overhead = signed value in same units]
  ADDITIVE-TO: C-01 FLAT-CASE-PRESSURE
```

After NET-COST-COMPARISON closes, emit the following on its own line:
`CROSS-REF-REQUIRED (2 of 2): NO interceding content between NET-COST-COMPARISON: close and FLAT-CASE-PRESSURE: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

Then emit:
`FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
Rating MUST be exactly one value from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`

Choose exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
Reasoning MUST reference the FLAT-CASE-PRESSURE rating.
DO write a concrete re-assessment trigger. DO NOT write "revisit as the team grows."

If verdict is `CAN-OPERATE-FLAT`: produce a Flat Operating Rhythm block after the re-assessment
trigger. At minimum two rows. Label: "Flat Operating Rhythm." `[Zone: POST-VERDICT-BRANCH]`

VERDICT-GATE CHECKLIST -- confirm all six items before proceeding past VERDICT:
  [ ] (1) COST-FRAME CONCLUSION: written as the first line of Sub-section 4
  [ ] (2) CROSS-REF-REQUIRED (1 of 2): written on its own line immediately after COST-FRAME CONCLUSION:
          [ANCHOR-ORDER CONSTRAINT: Order 1 (COST-FRAME CONCLUSION:) MUST immediately precede
          Order 2 (NET-COST-COMPARISON:) with NO interceding content -- verify adjacency now,
          independent of the SUB-SECTION-4-ANCHOR-SEQUENCE declaration]
  [ ] (3) NET-COST-COMPARISON: block written immediately after CROSS-REF-REQUIRED (1 of 2), with ADDITIVE-TO guard inside
  [ ] (4) CROSS-REF-REQUIRED (2 of 2): written on its own line immediately after NET-COST-COMPARISON: closes
          [ANCHOR-ORDER CONSTRAINT: Order 2 (NET-COST-COMPARISON:) MUST immediately precede
          Order 3 (FLAT-CASE-PRESSURE:) with NO interceding content -- verify adjacency now,
          independent of the SUB-SECTION-4-ANCHOR-SEQUENCE declaration]
  [ ] (5) FLAT-CASE-PRESSURE: written immediately after CROSS-REF-REQUIRED (2 of 2), valid closed-set rating
  [ ] (6) Verdict declaration (CAN-OPERATE-FLAT or STRUCTURE-WARRANTED) + re-assessment trigger

DO NOT proceed past VERDICT until all six checklist items are confirmed.

INTEGRATION-NOTE -- POSITIONAL DISJOINTNESS CONFIRMATION

DO produce a labeled `INTEGRATION-NOTE:` block immediately after Sub-section 4 and BEFORE the
ASCII org diagram. Applies when all three positional aspirational artifacts are present.

REQUIRED format:
```
INTEGRATION-NOTE:
- STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT]: positioned before Sub-section 1
- UNCOVERED: citation [Zone: SUB-SECTION-3]: positioned within Sub-section 3
- Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH]: positioned after Sub-section 4, CAN-OPERATE-FLAT branch only
Positional disjointness confirmed: each artifact assigned to exactly one zone; no zone shared.
```

ZONE-NOTATION RULE:
REQUIRED: Each artifact entry in INTEGRATION-NOTE MUST use `[Zone: X]` bracket format --
the same bracket form used at each artifact's definition site inline label.
PROHIBITED forms -- each is a rule violation requiring correction:
  (1) `(PRE-ASSESSMENT)` -- prohibited; use `[Zone: PRE-ASSESSMENT]` instead
  (2) `(SUB-SECTION-3)` -- prohibited; use `[Zone: SUB-SECTION-3]` instead
  (3) `(POST-VERDICT-BRANCH)` -- prohibited; use `[Zone: POST-VERDICT-BRANCH]` instead
DO NOT use any parenthetical zone designator form anywhere in the document.

If verdict is `STRUCTURE-WARRANTED`: note N/A for POST-VERDICT-BRANCH; confirm disjointness
for the two remaining artifacts.

ZONE-LABEL-TRACEABILITY -- REQUIRED IMMEDIATELY AFTER INTEGRATION-NOTE:
After writing the INTEGRATION-NOTE block, perform a definition-site cross-check for each artifact:
  (1) Locate the inline `[Zone: X]` label at the artifact's definition site in the document above.
  (2) Compare the designator string used in INTEGRATION-NOTE with the definition-site designator.
  (3) Emit one line per artifact:
      `ZONE-TRACE-CONFIRMED: [artifact name] -- INTEGRATION-NOTE: [Zone: X]; definition site: [Zone: X]; designator strings match.`
      OR: `ZONE-TRACE-MISMATCH: [artifact name] -- INTEGRATION-NOTE: [Zone: X]; definition site: [Zone: Y]; CORRECT the INTEGRATION-NOTE entry before proceeding.`
DO NOT omit a ZONE-TRACE-CONFIRMED or ZONE-TRACE-MISMATCH line for any artifact entry.
DO NOT emit the INERTIA COMPLETE gate until all lines present and no ZONE-TRACE-MISMATCH remain.
If `STRUCTURE-WARRANTED`: ZONE-TRACE-CONFIRMED for two present artifacts;
`ZONE-TRACE-N/A: Flat Operating Rhythm -- POST-VERDICT-BRANCH absent (STRUCTURE-WARRANTED).`

DO emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
DO NOT draw any org boxes until this gate is present.

ASCII ORG DIAGRAM

DO draw ASCII hierarchy using box-drawing characters (`+`, `-`, `|`) or equivalent.
DO show at minimum two hierarchy levels.
DO show committees as distinct labeled nodes, not embedded in an area.
DO use role names from ROLES-LOADED or ROLES-NOTE only.

DO emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
DO NOT begin the Headcount table until this gate is present.

HEADCOUNT BY AREA -- DECIDES / ESCALATES REQUIRED

DO produce a headcount table: `Area | Headcount | Key Roles | Decides | Escalates`
DO NOT use a single "Decision Scope" column.
DO annotate Key Roles as `[role name] ([domain type])`.
At minimum two area rows plus `**Total**` row.

OPERATING RHYTHM TABLE

Columns: `Cadence | Frequency | DRI / Owner | Purpose`
At minimum three rows: one ROB, one shiproom or gate, one governance meeting.

COMMITTEE CHARTERS -- FIVE FIELDS REQUIRED

DO write a charter for each governance meeting in the rhythm table.
DO include all five fields: Purpose, Membership, Decides, Escalates, Quorum.
DO annotate each Membership role as `[role name] ([domain type])`. Minimum two roles.
DO populate Escalates with a named destination.
DO NOT write "everything not listed under Decides."
DO include a `Dissolves When:` sixth field -- specific, observable conditions only.

QUORUM-DENOMINATOR CONSTRAINT -- REQUIRED BEFORE EACH QUORUM LINE:
Before writing the Quorum line for each charter:
  (1) Count distinct roles in Membership. That count is M.
  (2) Choose N (minimum for binding decision; N < M).
  (3) Emit: `[QUORUM-COUNT: Membership roles listed = [M]; minimum binding quorum = [N] of [M]]`
  (4) Emit: `Quorum: [N] of [M] member roles required for binding decisions`
DO NOT write M without first counting. DO NOT omit [QUORUM-COUNT: ...] for any charter.

DO emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
DO NOT begin the ORG-ELEMENT REGISTER until this gate is present.

ORG-ELEMENT REGISTER -- MUST PRECEDE ORG EVOLUTION ROADMAP

MUST produce immediately after the charters phase gate. DO NOT skip.
DO NOT proceed to Org Evolution Roadmap until all four category entries are populated:

```
ORG-ELEMENT REGISTER

  Category schema:
  | cat-N | Category name       | Element type                                     |
  |-------|---------------------|--------------------------------------------------|
  | cat-1 | Areas               | Area names from the Headcount by Area table      |
  | cat-2 | Committees/Cadences | Names from Rhythm Table and Charters             |
  | cat-3 | Headcount           | Total and per-area headcount counts              |
  | cat-4 | DRI Roles           | DRI role names from the Operating Rhythm Table   |

  cat-1 (Areas):    - [area name] -- headcount: [N]
  cat-2 (Committees/Cadences):    - [committee or cadence name]
  cat-3 (Headcount):    - Total headcount: [N]
  cat-4 (DRI Roles):    - [DRI role]
```

ORG EVOLUTION ROADMAP -- REQUIRED

After ORG-ELEMENT REGISTER. Columns: `Trigger | Structural Change | Type`
At minimum two rows. Row 1: headcount threshold. Row 2: different category.

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

After Org Evolution Roadmap.
Open each "Why It Applies Here" cell: `[element name] (cat-N) -- [specific relevance]`
DO NOT use a cat-N code not in the ORG-ELEMENT REGISTER schema.
At minimum two anti-pattern rows.

SECTION ORDER -- DO NOT REORDER

1. ROLES-LOADED or ROLES-NOTE
2. ROLE-LOAD-ORDER (Tier 1 Engineering, Tier 2 Operations, Tier 3 PM/Design/Research/Other)
3. ROLE-TYPE-CLASSIFICATION (following ROLE-LOAD-ORDER)
4. ROLE-TIER-ACCOUNTING (one row per tier with count and TIER-PRESENT/TIER-ABSENT)
5. Phase gate: ROLES COMPLETE
6. STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT] (before Sub-section 1)
7. Sub-section 1 (mechanism table + FLAT-CASE-CLOSED with type-diversity count)
8. Sub-section 2: How We Coordinate Today
9. Sub-section 3: Rebuttal (UNCOVERED: citation [Zone: SUB-SECTION-3])
10. Sub-section 4: VERDICT (SUB-SECTION-4-ANCHOR-SEQUENCE: COST-FRAME CONCLUSION + CROSS-REF-REQUIRED (1 of 2) + NET-COST-COMPARISON with ADDITIVE-TO + CROSS-REF-REQUIRED (2 of 2) + FLAT-CASE-PRESSURE + verdict + trigger + VERDICT-GATE CHECKLIST + Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH] if applicable)
11. INTEGRATION-NOTE with [Zone: X] bracket notation + ZONE-NOTATION RULE enumerated block
12. ZONE-LABEL-TRACEABILITY: one ZONE-TRACE-CONFIRMED per artifact, gating INERTIA COMPLETE
13. Phase gate: INERTIA COMPLETE
14. ASCII Org Diagram
15. Phase gate: STRUCTURE COMPLETE
16. Headcount by Area
17. Operating Rhythm Table
18. Committee Charters (QUORUM-DENOMINATOR CONSTRAINT per charter)
19. Phase gate: CHARTERS COMPLETE
20. ORG-ELEMENT REGISTER
21. Org Evolution Roadmap
22. Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-02 -- Lifecycle Emphasis: CHARTER-COMPLETENESS-AUDIT Cross-Charter Field Sweep

**axis:** lifecycle emphasis (CHARTER-COMPLETENESS-AUDIT block after all Committee Charters and
before CHARTERS COMPLETE gate; one row per charter with PRESENT/MISSING per field for all six
required fields: Purpose, Membership, Decides, Escalates, Quorum, Dissolves When)
**hypothesis:** V-05/R13 satisfies C-03 (five fields per charter), A-13 (Dissolves When), and A-32
(QUORUM-DENOMINATOR CONSTRAINT with bound M) all per-charter at production time. Each charter is
enforced individually. But no single production artifact confirms all charters satisfy all six field
requirements simultaneously. Under compression, a later charter can silently drop a field that earlier
charters included -- the per-charter enforcement succeeded for earlier charters while the later
charter's production happened after the enforcement instruction was processed. The only way to detect
the gap is to re-read each charter individually. V-02/R14 adds a `CHARTER-COMPLETENESS-AUDIT:` block
after all charters and before the CHARTERS COMPLETE gate: one row per charter with a PRESENT/MISSING
verdict per field across all six fields. Any MISSING verdict blocks the gate, requiring the field to
be added before proceeding. Cross-charter field completeness becomes independently verifiable by table
inspection. All other criteria unchanged from V-05/R13. Expected: A-01 through A-33 all PASS.
Composite: 33/33.

---

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

DO emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
DO NOT proceed until this gate is present.

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.

STRUCTURING-COST FRAME -- PRE-ASSESSMENT BLOCK
`[Zone: PRE-ASSESSMENT]`

DO produce a labeled `STRUCTURING-COST FRAME:` block immediately before Sub-section 1.
MUST name both error risks with >= 1 concrete consequence each.
DO NOT merge with Sub-section 1. DO NOT omit.

**Sub-section 1 -- Case for Staying Flat**

Mechanism evidence table, four columns:
`Mechanism Name | Mechanism Type | Frequency / Participants | Estimated Coordination Cost`
Mechanism Type from: `Channel / Informal Role / Recurring Cadence / Shared Artifact`
Floor: >= 2 rows with >= 2 distinct Mechanism Type values. Numeric cost estimates required.

Count rows (N) and distinct types (K), then emit:
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded; {K} of 4 type classes represented. How We Coordinate Today begins.] ---`

**Sub-section 2 -- How We Coordinate Today**

Inventory active coordination patterns. DO NOT re-list Sub-section 1 entries.

**Sub-section 3 -- Rebuttal**

Name the specific coordination failure with a specific observable.
Include `UNCOVERED:` citation naming an ownerless function or decision class.
`[Zone: SUB-SECTION-3]`

**Sub-section 4 -- VERDICT and Re-assessment Trigger**

SUB-SECTION-4-ANCHOR-SEQUENCE:
  Order 1: COST-FRAME CONCLUSION: (first line of Sub-section 4)
  Order 2: NET-COST-COMPARISON: block (immediately after Order 1)
  Order 3: FLAT-CASE-PRESSURE: line (immediately after Order 2)
  CONSTRAINT: NO interceding content between any adjacent pair.

COST-FRAME CONCLUSION: names STRUCTURING-COST FRAME by label, dominant error risk,
evidence sub-section.

`CROSS-REF-REQUIRED (1 of 2): NO interceding content between COST-FRAME CONCLUSION: and NET-COST-COMPARISON: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

```
NET-COST-COMPARISON:
  Flat coordination cost: [total from Sub-section 1]
  Structure overhead: [meeting load + charter maintenance + escalation delay]
  Net delta: [signed value]
  ADDITIVE-TO: C-01 FLAT-CASE-PRESSURE
```

`CROSS-REF-REQUIRED (2 of 2): NO interceding content between NET-COST-COMPARISON: close and FLAT-CASE-PRESSURE: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

`FLAT-CASE-PRESSURE: [rating] -- [justification citing mechanism count and failure mode]`
Rating from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`

Verdict: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`. Re-assessment trigger required.
If `CAN-OPERATE-FLAT`: Flat Operating Rhythm table (>= 2 rows). `[Zone: POST-VERDICT-BRANCH]`

VERDICT-GATE CHECKLIST -- confirm all six items:
  [ ] (1) COST-FRAME CONCLUSION: as first line of Sub-section 4
  [ ] (2) CROSS-REF-REQUIRED (1 of 2): standalone line after COST-FRAME CONCLUSION:
          [ANCHOR-ORDER CONSTRAINT: Order 1 immediately precedes Order 2, NO interceding content]
  [ ] (3) NET-COST-COMPARISON: with ADDITIVE-TO guard inside
  [ ] (4) CROSS-REF-REQUIRED (2 of 2): standalone line after NET-COST-COMPARISON: closes
          [ANCHOR-ORDER CONSTRAINT: Order 2 immediately precedes Order 3, NO interceding content]
  [ ] (5) FLAT-CASE-PRESSURE: with valid rating
  [ ] (6) Verdict + re-assessment trigger

INTEGRATION-NOTE -- after Sub-section 4, before ASCII org diagram:
```
INTEGRATION-NOTE:
- STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT]: positioned before Sub-section 1
- UNCOVERED: citation [Zone: SUB-SECTION-3]: positioned within Sub-section 3
- Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH]: positioned after Sub-section 4, CAN-OPERATE-FLAT branch only
Positional disjointness confirmed: each artifact assigned to exactly one zone; no zone shared.
```

ZONE-NOTATION RULE:
PROHIBITED:
  (1) `(PRE-ASSESSMENT)` -- use `[Zone: PRE-ASSESSMENT]`
  (2) `(SUB-SECTION-3)` -- use `[Zone: SUB-SECTION-3]`
  (3) `(POST-VERDICT-BRANCH)` -- use `[Zone: POST-VERDICT-BRANCH]`

ZONE-LABEL-TRACEABILITY -- immediately after INTEGRATION-NOTE:
For each artifact: emit ZONE-TRACE-CONFIRMED or ZONE-TRACE-MISMATCH.
All lines required before INERTIA COMPLETE gate.

DO emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

ASCII ORG DIAGRAM

Box-drawing characters. At minimum two levels. Committees as distinct labeled nodes.

DO emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

`Area | Headcount | Key Roles | Decides | Escalates` -- two area rows minimum + Total.

OPERATING RHYTHM TABLE

`Cadence | Frequency | DRI / Owner | Purpose` -- ROB, shiproom or gate, governance meeting.

COMMITTEE CHARTERS -- FIVE FIELDS REQUIRED

DO write a charter for each governance meeting.
Include: Purpose, Membership, Decides, Escalates, Quorum, Dissolves When. Minimum two Membership roles.

QUORUM-DENOMINATOR CONSTRAINT -- REQUIRED BEFORE EACH QUORUM LINE:
  (1) Count distinct Membership roles = M.
  (2) Choose N (minimum for binding decision; N < M).
  (3) Emit: `[QUORUM-COUNT: Membership roles listed = [M]; minimum binding quorum = [N] of [M]]`
  (4) Emit: `Quorum: [N] of [M] member roles required for binding decisions`

CHARTER-COMPLETENESS-AUDIT -- REQUIRED AFTER ALL CHARTERS, BEFORE CHARTERS COMPLETE GATE:

After writing all Committee Charters and before emitting the CHARTERS COMPLETE gate, DO produce
a `CHARTER-COMPLETENESS-AUDIT:` block.
The block MUST emit one row per charter in the format:
  `Charter: [name] | Purpose: [PRESENT/MISSING] | Membership: [PRESENT/MISSING] | Decides: [PRESENT/MISSING] | Escalates: [PRESENT/MISSING] | Quorum: [PRESENT/MISSING] | Dissolves When: [PRESENT/MISSING] | [ALL-FIELDS or MISSING: field1, field2, ...]`
Count of rows MUST match the number of governance meetings in the Operating Rhythm Table.
Any MISSING verdict is a constraint violation: add the missing field before proceeding.
DO NOT emit the CHARTERS COMPLETE gate until all rows show ALL-FIELDS.
DO NOT omit this block.

DO emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
DO NOT begin the ORG-ELEMENT REGISTER until this gate is present.

ORG-ELEMENT REGISTER -- MUST PRECEDE ORG EVOLUTION ROADMAP

MUST produce immediately after the charters phase gate. DO NOT skip.

```
ORG-ELEMENT REGISTER

  Category schema:
  | cat-N | Category name       | Element type                                     |
  |-------|---------------------|--------------------------------------------------|
  | cat-1 | Areas               | Area names from the Headcount by Area table      |
  | cat-2 | Committees/Cadences | Names from Rhythm Table and Charters             |
  | cat-3 | Headcount           | Total and per-area headcount counts              |
  | cat-4 | DRI Roles           | DRI role names from the Operating Rhythm Table   |

  cat-1 (Areas):    - [area name] -- headcount: [N]
  cat-2 (Committees/Cadences):    - [committee or cadence name]
  cat-3 (Headcount):    - Total headcount: [N]
  cat-4 (DRI Roles):    - [DRI role]
```

ORG EVOLUTION ROADMAP -- REQUIRED

After ORG-ELEMENT REGISTER. Two rows minimum. Row 1: headcount threshold. Row 2: different category.

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

`[element name] (cat-N) -- [specific relevance]` format. Two rows minimum.

SECTION ORDER -- DO NOT REORDER

1. ROLES-LOADED or ROLES-NOTE
2. ROLE-LOAD-ORDER
3. ROLE-TYPE-CLASSIFICATION
4. Phase gate: ROLES COMPLETE
5. STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT] + Sub-sections 1-4 + VERDICT-GATE CHECKLIST
6. INTEGRATION-NOTE + ZONE-NOTATION RULE + ZONE-LABEL-TRACEABILITY
7. Phase gate: INERTIA COMPLETE
8. ASCII Org Diagram
9. Phase gate: STRUCTURE COMPLETE
10. Headcount by Area
11. Operating Rhythm Table
12. Committee Charters (QUORUM-DENOMINATOR CONSTRAINT per charter)
13. CHARTER-COMPLETENESS-AUDIT (one row per charter, all six fields, before CHARTERS COMPLETE)
14. Phase gate: CHARTERS COMPLETE
15. ORG-ELEMENT REGISTER
16. Org Evolution Roadmap
17. Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-03 -- Output Format: REGISTER-CATEGORY-CONTRACT Named Schema Declaration

**axis:** output format (REGISTER-CATEGORY-CONTRACT block as first element within ORG-ELEMENT
REGISTER, before any category entries; explicitly names each cat-N code with its canonical label;
declares the code set as closed; prohibits unlisted codes)
**hypothesis:** V-05/R13 satisfies the Anti-Pattern Watch constraint via the Category schema table
inside the ORG-ELEMENT REGISTER. The table describes cat-1 through cat-4 and their element types.
But the table is embedded as descriptive content -- it does not carry a standalone block label,
does not explicitly name the code set as closed, and does not include a prohibition on unlisted
codes. A model generating a `(cat-5)` reference in Anti-Pattern Watch would violate the stated
constraint, but detecting the violation requires parsing the schema table and recognizing that cat-5
is absent. V-03/R14 promotes the schema to a `REGISTER-CATEGORY-CONTRACT:` block as the first
named element in the ORG-ELEMENT REGISTER, explicitly enumerating each code and its label,
declaring the set as closed, and including a prohibition on unlisted codes. Absence of this block
is structurally detectable. All other criteria unchanged from V-05/R13. Expected: A-01 through
A-33 all PASS. Composite: 33/33.

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block at the top listing each role and one-line description.
If absent: produce `ROLES-NOTE:` block with inferred roles.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER -- CLASSIFICATION SEQUENCE CONSTRAINT

DO classify roles in this exact tier order when producing ROLE-TYPE-CLASSIFICATION:
  Tier 1: Engineering roles
  Tier 2: Operations roles
  Tier 3: PM / Design / Research / Other roles
DO NOT interleave tiers. If no Engineering roles: begin with Tier 2.
This block governs sequence only.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

DO produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE,
following the ROLE-LOAD-ORDER tier sequence.
DO assign each role exactly one type from: `Engineering / PM / Design / Operations / Research / Other`
DO format: `- [role name] -- [domain type]`
DO annotate Key Roles cells and Membership fields as `[role name] ([domain type])`.
DO NOT skip any role.

DO emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS, STEELMAN FIRST

STRUCTURING-COST FRAME -- PRE-ASSESSMENT BLOCK
`[Zone: PRE-ASSESSMENT]`

Labeled block before Sub-section 1. Names over-structuring risk and under-coordination risk,
each with >= 1 concrete consequence.

**Sub-section 1 -- Case for Staying Flat**

Four-column mechanism table:
`Mechanism Name | Mechanism Type | Frequency / Participants | Estimated Coordination Cost`
Mechanism Type from: `Channel / Informal Role / Recurring Cadence / Shared Artifact`
>= 2 rows, >= 2 distinct Mechanism Type values. Numeric cost estimates.

Count rows (N) and distinct types (K):
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded; {K} of 4 type classes represented. How We Coordinate Today begins.] ---`

**Sub-section 2 -- How We Coordinate Today**

Inventory active coordination patterns. No Sub-section 1 re-listing.

**Sub-section 3 -- Rebuttal**

Specific coordination failure + specific observable.
`UNCOVERED:` citation naming ownerless function or decision class.
`[Zone: SUB-SECTION-3]`

**Sub-section 4 -- VERDICT**

SUB-SECTION-4-ANCHOR-SEQUENCE:
  Order 1: COST-FRAME CONCLUSION: (first)
  Order 2: NET-COST-COMPARISON: (immediately after Order 1)
  Order 3: FLAT-CASE-PRESSURE: (immediately after Order 2)
  CONSTRAINT: NO interceding content between any adjacent pair.

COST-FRAME CONCLUSION: -- names STRUCTURING-COST FRAME, dominant risk, evidence sub-section.

`CROSS-REF-REQUIRED (1 of 2): NO interceding content between COST-FRAME CONCLUSION: and NET-COST-COMPARISON: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

```
NET-COST-COMPARISON:
  Flat coordination cost: [total]
  Structure overhead: [meeting load + charter maintenance + escalation delay]
  Net delta: [signed value]
  ADDITIVE-TO: C-01 FLAT-CASE-PRESSURE
```

`CROSS-REF-REQUIRED (2 of 2): NO interceding content between NET-COST-COMPARISON: close and FLAT-CASE-PRESSURE: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

`FLAT-CASE-PRESSURE: [rating] -- [justification]`
Rating: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`
Verdict + re-assessment trigger. If `CAN-OPERATE-FLAT`: Flat Operating Rhythm. `[Zone: POST-VERDICT-BRANCH]`

VERDICT-GATE CHECKLIST:
  [ ] (1) COST-FRAME CONCLUSION: as first line of Sub-section 4
  [ ] (2) CROSS-REF-REQUIRED (1 of 2): standalone line after COST-FRAME CONCLUSION:
          [ANCHOR-ORDER CONSTRAINT: Order 1 immediately precedes Order 2, NO interceding content]
  [ ] (3) NET-COST-COMPARISON: with ADDITIVE-TO guard inside
  [ ] (4) CROSS-REF-REQUIRED (2 of 2): standalone line after NET-COST-COMPARISON: closes
          [ANCHOR-ORDER CONSTRAINT: Order 2 immediately precedes Order 3, NO interceding content]
  [ ] (5) FLAT-CASE-PRESSURE: with valid rating
  [ ] (6) Verdict + re-assessment trigger

INTEGRATION-NOTE:
```
INTEGRATION-NOTE:
- STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT]: positioned before Sub-section 1
- UNCOVERED: citation [Zone: SUB-SECTION-3]: positioned within Sub-section 3
- Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH]: positioned after Sub-section 4, CAN-OPERATE-FLAT branch only
Positional disjointness confirmed: each artifact assigned to exactly one zone; no zone shared.
```

ZONE-NOTATION RULE:
PROHIBITED:
  (1) `(PRE-ASSESSMENT)` -- use `[Zone: PRE-ASSESSMENT]`
  (2) `(SUB-SECTION-3)` -- use `[Zone: SUB-SECTION-3]`
  (3) `(POST-VERDICT-BRANCH)` -- use `[Zone: POST-VERDICT-BRANCH]`

ZONE-LABEL-TRACEABILITY -- immediately after INTEGRATION-NOTE:
ZONE-TRACE-CONFIRMED or ZONE-TRACE-MISMATCH per artifact. All required before INERTIA COMPLETE.

DO emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

ASCII ORG DIAGRAM

Box-drawing characters. Two levels minimum. Committees as distinct nodes.

DO emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA

`Area | Headcount | Key Roles | Decides | Escalates` -- two area rows + Total.

OPERATING RHYTHM TABLE

`Cadence | Frequency | DRI / Owner | Purpose` -- ROB, shiproom, governance meeting.

COMMITTEE CHARTERS

Purpose, Membership, Decides, Escalates, Quorum, Dissolves When. Two Membership roles minimum.

QUORUM-DENOMINATOR CONSTRAINT per charter: count M, choose N, emit [QUORUM-COUNT: ...], emit Quorum line.

DO emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

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
DO NOT begin cat-1 through cat-4 entries until this block is written.

After REGISTER-CATEGORY-CONTRACT, populate all four categories:
  cat-1 (Areas), cat-2 (Committees/Cadences), cat-3 (Headcount), cat-4 (DRI Roles).

ORG EVOLUTION ROADMAP -- REQUIRED

Two rows minimum. Row 1: headcount threshold. Row 2: different category.

ANTI-PATTERN WATCH

`[element name] (cat-N) -- [specific relevance]`
DO NOT use a cat-N code outside those declared in REGISTER-CATEGORY-CONTRACT.
Two rows minimum.

SECTION ORDER -- DO NOT REORDER

1. ROLES-LOADED or ROLES-NOTE
2. ROLE-LOAD-ORDER
3. ROLE-TYPE-CLASSIFICATION
4. Phase gate: ROLES COMPLETE
5. STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT] + Sub-sections 1-4 + VERDICT-GATE CHECKLIST
6. INTEGRATION-NOTE + ZONE-NOTATION RULE + ZONE-LABEL-TRACEABILITY
7. Phase gate: INERTIA COMPLETE
8. ASCII Org Diagram
9. Phase gate: STRUCTURE COMPLETE
10. Headcount by Area
11. Operating Rhythm Table
12. Committee Charters (QUORUM-DENOMINATOR CONSTRAINT per charter)
13. Phase gate: CHARTERS COMPLETE
14. ORG-ELEMENT REGISTER (REGISTER-CATEGORY-CONTRACT as first element)
15. Org Evolution Roadmap
16. Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-04 -- Combined: ROLE-TIER-ACCOUNTING + CHARTER-COMPLETENESS-AUDIT

**axis:** combined role sequence + lifecycle emphasis (V-05/R13 base + V-01/R14
ROLE-TIER-ACCOUNTING named accounting block + V-02/R14 CHARTER-COMPLETENESS-AUDIT cross-charter
field sweep)
**hypothesis:** V-01/R14 closes the tier-population verification gap by making ROLE-TIER-ACCOUNTING
a named block whose absence is detectable as a missing count artifact. V-02/R14 closes the
cross-charter completeness gap by making CHARTER-COMPLETENESS-AUDIT a named block whose absence
is detectable before the CHARTERS COMPLETE gate. Both improvements operate at structurally isolated
positions (roles phase vs charters phase) with no interaction surface. Combined, they provide
verification artifacts at both ends of the classification/charter lifecycle. Expected: A-01 through
A-33 all PASS. Composite: 33/33.

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block at the top listing each role and one-line description.
If absent: produce `ROLES-NOTE:` block with inferred roles.
DO NOT write any other section until this block exists.

ROLE-LOAD-ORDER -- CLASSIFICATION SEQUENCE CONSTRAINT

DO classify roles in this exact tier order when producing ROLE-TYPE-CLASSIFICATION:
  Tier 1: Engineering roles (all Engineering before any Tier 2 or Tier 3)
  Tier 2: Operations roles (all Operations before any Tier 3)
  Tier 3: PM / Design / Research / Other roles
DO NOT write a Tier 2 entry before all Tier 1 entries are written.
DO NOT write a Tier 3 entry before all Tier 2 entries are written.
DO NOT interleave tiers.
If no Engineering roles: begin with Tier 2. If no Engineering or Operations: classify in any order.
This block governs sequence only.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

DO produce `ROLE-TYPE-CLASSIFICATION:` following ROLE-LOAD-ORDER tier sequence.
Assign each role one type from: `Engineering / PM / Design / Operations / Research / Other`
Format: `- [role name] -- [domain type]`
Annotate Key Roles and Membership fields as `[role name] ([domain type])`.
DO NOT skip any role.

ROLE-TIER-ACCOUNTING -- REQUIRED IMMEDIATELY AFTER ROLE-TYPE-CLASSIFICATION

DO produce a `ROLE-TIER-ACCOUNTING:` block immediately after ROLE-TYPE-CLASSIFICATION.
Emit one row per tier:
  `Tier 1 (Engineering): [N] role(s) classified -- TIER-PRESENT`
  `Tier 2 (Operations): [N] role(s) classified -- TIER-PRESENT`
  `Tier 3 (PM/Design/Research/Other): [N] role(s) classified -- TIER-PRESENT`
Zero-count tier: `Tier [N] ([name]): 0 roles classified -- TIER-ABSENT (no roles of this type in input set)`
Count MUST match actual ROLE-TYPE-CLASSIFICATION entries for that tier.
All three tiers must be accounted for. DO NOT omit this block.

DO emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS, STEELMAN FIRST

STRUCTURING-COST FRAME -- PRE-ASSESSMENT BLOCK
`[Zone: PRE-ASSESSMENT]`
Names over-structuring risk and under-coordination risk, >= 1 concrete consequence each.

**Sub-section 1 -- Case for Staying Flat**

Four-column table: `Mechanism Name | Mechanism Type | Frequency / Participants | Estimated Coordination Cost`
Mechanism Type: `Channel / Informal Role / Recurring Cadence / Shared Artifact`
>= 2 rows, >= 2 distinct types. Numeric cost estimates.
`--- [FLAT-CASE-CLOSED: {N} rows; {K} of 4 type classes represented. How We Coordinate Today begins.] ---`

**Sub-section 2** -- Active coordination inventory. No Sub-section 1 re-listing.

**Sub-section 3 -- Rebuttal**

Specific coordination failure + specific observable.
`UNCOVERED:` citation. `[Zone: SUB-SECTION-3]`

**Sub-section 4 -- VERDICT**

SUB-SECTION-4-ANCHOR-SEQUENCE: Order 1 COST-FRAME CONCLUSION: -> Order 2 NET-COST-COMPARISON: -> Order 3 FLAT-CASE-PRESSURE:
NO interceding content between any adjacent pair.

COST-FRAME CONCLUSION: names STRUCTURING-COST FRAME, dominant risk, evidence sub-section.

`CROSS-REF-REQUIRED (1 of 2): NO interceding content between COST-FRAME CONCLUSION: and NET-COST-COMPARISON: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

```
NET-COST-COMPARISON:
  Flat coordination cost: [total]
  Structure overhead: [meeting load + charter maintenance + escalation delay]
  Net delta: [signed value]
  ADDITIVE-TO: C-01 FLAT-CASE-PRESSURE
```

`CROSS-REF-REQUIRED (2 of 2): NO interceding content between NET-COST-COMPARISON: close and FLAT-CASE-PRESSURE: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

`FLAT-CASE-PRESSURE: [rating] -- [justification]`
Rating: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`
Verdict + trigger. If `CAN-OPERATE-FLAT`: Flat Operating Rhythm. `[Zone: POST-VERDICT-BRANCH]`

VERDICT-GATE CHECKLIST:
  [ ] (1) COST-FRAME CONCLUSION: as first line
  [ ] (2) CROSS-REF-REQUIRED (1 of 2): standalone after COST-FRAME CONCLUSION:
          [ANCHOR-ORDER CONSTRAINT: Order 1 immediately precedes Order 2, NO interceding content]
  [ ] (3) NET-COST-COMPARISON: with ADDITIVE-TO inside
  [ ] (4) CROSS-REF-REQUIRED (2 of 2): standalone after NET-COST-COMPARISON: closes
          [ANCHOR-ORDER CONSTRAINT: Order 2 immediately precedes Order 3, NO interceding content]
  [ ] (5) FLAT-CASE-PRESSURE: valid rating
  [ ] (6) Verdict + trigger

INTEGRATION-NOTE:
```
INTEGRATION-NOTE:
- STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT]: before Sub-section 1
- UNCOVERED: citation [Zone: SUB-SECTION-3]: within Sub-section 3
- Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH]: after Sub-section 4, CAN-OPERATE-FLAT only
Positional disjointness confirmed: each artifact one zone; no zone shared.
```

ZONE-NOTATION RULE -- PROHIBITED:
  (1) `(PRE-ASSESSMENT)` -> `[Zone: PRE-ASSESSMENT]`
  (2) `(SUB-SECTION-3)` -> `[Zone: SUB-SECTION-3]`
  (3) `(POST-VERDICT-BRANCH)` -> `[Zone: POST-VERDICT-BRANCH]`

ZONE-LABEL-TRACEABILITY: ZONE-TRACE-CONFIRMED or ZONE-TRACE-MISMATCH per artifact. All required.

DO emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`

ASCII ORG DIAGRAM -- two levels minimum, box-drawing characters, committees as distinct nodes.

DO emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT: `Area | Headcount | Key Roles | Decides | Escalates` -- two rows + Total.
RHYTHM: `Cadence | Frequency | DRI / Owner | Purpose` -- ROB, shiproom, governance.

COMMITTEE CHARTERS -- all six fields: Purpose, Membership, Decides, Escalates, Quorum, Dissolves When.
QUORUM-DENOMINATOR CONSTRAINT per charter: count M, choose N, emit [QUORUM-COUNT: ...], emit Quorum.

CHARTER-COMPLETENESS-AUDIT -- REQUIRED AFTER ALL CHARTERS, BEFORE CHARTERS COMPLETE GATE:

DO produce `CHARTER-COMPLETENESS-AUDIT:` block after all charters.
One row per charter:
  `Charter: [name] | Purpose: [P/M] | Membership: [P/M] | Decides: [P/M] | Escalates: [P/M] | Quorum: [P/M] | Dissolves When: [P/M] | [ALL-FIELDS or MISSING: ...]`
Any MISSING blocks the gate. Add missing field before proceeding.
DO NOT emit CHARTERS COMPLETE until all rows show ALL-FIELDS. DO NOT omit.

DO emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER

```
ORG-ELEMENT REGISTER

  Category schema:
  | cat-N | Category name       | Element type                                     |
  |-------|---------------------|--------------------------------------------------|
  | cat-1 | Areas               | Area names from the Headcount by Area table      |
  | cat-2 | Committees/Cadences | Names from Rhythm Table and Charters             |
  | cat-3 | Headcount           | Total and per-area headcount counts              |
  | cat-4 | DRI Roles           | DRI role names from the Operating Rhythm Table   |

  cat-1 (Areas):    - [area] -- headcount: [N]
  cat-2 (Committees/Cadences):    - [name]
  cat-3 (Headcount):    - Total headcount: [N]
  cat-4 (DRI Roles):    - [DRI role]
```

ORG EVOLUTION ROADMAP -- two rows minimum. Row 1: headcount. Row 2: different category.
ANTI-PATTERN WATCH -- `[element] (cat-N) -- [relevance]`. Two rows minimum.

SECTION ORDER -- DO NOT REORDER

1. ROLES-LOADED or ROLES-NOTE
2. ROLE-LOAD-ORDER
3. ROLE-TYPE-CLASSIFICATION
4. ROLE-TIER-ACCOUNTING (one row per tier, count and TIER-PRESENT/TIER-ABSENT)
5. Phase gate: ROLES COMPLETE
6. STRUCTURING-COST FRAME + Sub-sections 1-4 + VERDICT-GATE CHECKLIST
7. INTEGRATION-NOTE + ZONE-NOTATION RULE + ZONE-LABEL-TRACEABILITY
8. Phase gate: INERTIA COMPLETE
9. ASCII Org Diagram
10. Phase gate: STRUCTURE COMPLETE
11. Headcount by Area
12. Operating Rhythm Table
13. Committee Charters (QUORUM-DENOMINATOR CONSTRAINT per charter)
14. CHARTER-COMPLETENESS-AUDIT (all six fields, ALL-FIELDS required before gate)
15. Phase gate: CHARTERS COMPLETE
16. ORG-ELEMENT REGISTER
17. Org Evolution Roadmap
18. Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-05 -- Full Integration: ROLE-TIER-ACCOUNTING + CHARTER-COMPLETENESS-AUDIT + REGISTER-CATEGORY-CONTRACT

**axis:** full integration (V-04/R14 + V-03/R14: all three new R14 blocks on V-05/R13 base)
**hypothesis:** V-04/R14 provides verification artifacts at both ends of the classification/charter
lifecycle -- ROLE-TIER-ACCOUNTING after ROLE-TYPE-CLASSIFICATION and CHARTER-COMPLETENESS-AUDIT
after all charters. V-05/R14 adds the V-03/R14 REGISTER-CATEGORY-CONTRACT improvement: a named
declared contract block at the top of the ORG-ELEMENT REGISTER that explicitly enumerates each
cat-N code, declares the set closed, and prohibits unlisted codes. The three improvements together
close verification gaps at three structurally isolated positions: roles phase (ROLE-TIER-ACCOUNTING),
charters phase (CHARTER-COMPLETENESS-AUDIT), and analysis phase (REGISTER-CATEGORY-CONTRACT). No
interaction surface exists among the three. Expected: A-01 through A-33 all PASS. Composite: 33/33.
Maximum compression resistance across A-34/A-35/A-36 cluster simultaneously.

---

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

COMMITTEE CHARTERS -- FIVE FIELDS REQUIRED

DO write a charter for each governance meeting.
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

After all Committee Charters, before the CHARTERS COMPLETE gate, DO produce a
`CHARTER-COMPLETENESS-AUDIT:` block.
Emit one row per charter:
  `Charter: [name] | Purpose: [PRESENT/MISSING] | Membership: [PRESENT/MISSING] | Decides: [PRESENT/MISSING] | Escalates: [PRESENT/MISSING] | Quorum: [PRESENT/MISSING] | Dissolves When: [PRESENT/MISSING] | [ALL-FIELDS or MISSING: field1, field2, ...]`
Count MUST match governance meetings in the Operating Rhythm Table.
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
At minimum two rows. Row 1: headcount threshold. Row 2: different category.

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

After Org Evolution Roadmap.
Open each "Why It Applies Here" cell:
`[element name] (cat-N) -- [one sentence of specific relevance]`
DO NOT use a cat-N code outside those declared in REGISTER-CATEGORY-CONTRACT.
At minimum two anti-pattern rows.

SECTION ORDER -- DO NOT REORDER

1. ROLES-LOADED or ROLES-NOTE
2. ROLE-LOAD-ORDER (Tier 1 Engineering, Tier 2 Operations, Tier 3 PM/Design/Research/Other)
3. ROLE-TYPE-CLASSIFICATION (following ROLE-LOAD-ORDER)
4. ROLE-TIER-ACCOUNTING (one row per tier with count and TIER-PRESENT/TIER-ABSENT)
5. Phase gate: ROLES COMPLETE
6. STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT] (before Sub-section 1)
7. Sub-section 1 (mechanism table + FLAT-CASE-CLOSED with type-diversity count)
8. Sub-section 2: How We Coordinate Today
9. Sub-section 3: Rebuttal (UNCOVERED: citation [Zone: SUB-SECTION-3])
10. Sub-section 4: VERDICT (SUB-SECTION-4-ANCHOR-SEQUENCE: COST-FRAME CONCLUSION + CROSS-REF-REQUIRED (1 of 2) + NET-COST-COMPARISON with ADDITIVE-TO + CROSS-REF-REQUIRED (2 of 2) + FLAT-CASE-PRESSURE + verdict + trigger + VERDICT-GATE CHECKLIST + Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH] if applicable)
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
23. Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} -- {date}`
