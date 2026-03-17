---
skill: quest-variate
skill_target: org-chart
date: 2026-03-16
round: R11
rubric_version: v10
status: variate
---

# org-chart Variate -- Round 11

**Date:** 2026-03-16
**Skill:** org-chart
**Rubric:** v10 (A-01 through A-24; A-23/A-24 new from R10 excellence signals)
**Round:** R11 -- single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

**R10 ceiling:** Both V-04/R10 (inline approach) and V-05/R10 (dedicated block approach) achieve
24/24 aspirationally under rubric v10 (composite 100.0). A-23 is satisfied in both:
- V-04/R10: cross-references embedded as parenthetical asides in production instructions --
  "(NO interceding content -- see anchor ordering above)"
- V-05/R10: cross-references embedded as constraint citations in production instructions --
  "(following the SUB-SECTION-4-ANCHOR-SEQUENCE CONSTRAINT -- NO other content between Order X
  and Order Y)"
A-24 is satisfied in both via `[Zone: X]` bracket notation in the INTEGRATION-NOTE required
format block.

**R11 target:** 24/24 aspirationally with higher compression resistance. The R10 approaches
embed A-23 cross-references as parenthetical asides within production instructions. Parenthetical
asides are syntactically subordinate to their containing sentence and can be elided without
breaking grammar. R11 tests whether standalone labeled cross-reference declarations (V-01) and
a verification-gate checklist (V-03) provide stronger resistance than inline asides, and whether
an explicit format prohibition (V-02) closes the A-24 parenthetical-reversion risk.

**Three questions drive R11:**

1. Does **standalone labeled cross-reference declaration** (V-01) -- replacing the parenthetical
   aside with a dedicated `CROSS-REF-REQUIRED:` line emitted at each transition site -- make
   A-23 compliance independently verifiable without parsing the surrounding sentence? (V-01)
2. Does **explicit A-24 format prohibition** (V-02) -- adding a `ZONE-NOTATION RULE:` block
   after the INTEGRATION-NOTE format example that names and prohibits parenthetical `(X)` form --
   close the format reversion risk beyond what the positive example provides alone? (V-02)
3. Does a **VERDICT-GATE checklist** (V-03) -- replacing the prose DO-NOT-PROCEED guard with a
   6-item checklist where items 2 and 4 carry cross-references to the anchor ordering declaration
   -- create a second A-23 enforcement site at verification time, separate from production time?
   (V-03)

V-04/R11 combines V-05/R10 dedicated block base + V-01 standalone declarations + V-02 explicit
prohibition.
V-05/R11 is full integration: V-05/R10 dedicated block base + all three improvements together.

---

## Round 11 Variation Map

| V | Axis | What Changes vs R10 ceiling | Hypothesis |
|---|------|----------------------------|------------|
| V-01 | phrasing register | V-04/R10 inline base. Replace parenthetical cross-ref asides with standalone labeled `CROSS-REF-REQUIRED:` lines at each of the two transition sites in Sub-section 4. | Parenthetical asides can be elided without breaking the containing sentence. Standalone labeled declarations are independent assertions -- omitting one leaves a structural gap. A-23 robustness +. Expected: 24/24. |
| V-02 | output format | V-05/R10 dedicated block base. Add `ZONE-NOTATION RULE:` block after INTEGRATION-NOTE format example, explicitly prohibiting parenthetical `(DESIGNATOR)` form and requiring bracket `[Zone: DESIGNATOR]` to match A-22 inline labels. | Format example shows the required pattern; explicit prohibition names the wrong form. Teaching by contrast closes the reversion risk that positive example alone does not. A-24 robustness +. Expected: 24/24. |
| V-03 | lifecycle emphasis | V-04/R10 inline base. Replace prose DO-NOT-PROCEED guard at end of Sub-section 4 with a 6-item `VERDICT-GATE CHECKLIST:` where items 2 and 4 carry explicit cross-references to the anchor ordering declaration. | A-23 is enforced at production time in V-04/R10. VERDICT-GATE creates a second enforcement site at verification time. Dual-site enforcement closes the gap between instruction and confirmed compliance. Expected: 24/24. |
| V-04 | combined | V-05/R10 dedicated block base + V-01 standalone `CROSS-REF-REQUIRED:` declarations at both transition sites + V-02 `ZONE-NOTATION RULE:` prohibition. | Dedicated block (A-21 max) + standalone declarations (A-23 max) + explicit prohibition (A-24 max). Each improvement is structurally isolated. Expected: 24/24, maximum robustness for A-21/A-23/A-24 cluster. |
| V-05 | full integration | V-05/R10 dedicated block base + V-01 standalone declarations + V-02 explicit prohibition + V-03 VERDICT-GATE checklist. | Maximum independently verifiable constraint density across all four A-21/A-22/A-23/A-24 criteria. Dual-site A-23 enforcement (production instructions + verification gate). Expected: 24/24. |

---

## V-01 -- Phrasing Register: Standalone Cross-Reference Declarations

**axis:** phrasing register (standalone labeled `CROSS-REF-REQUIRED:` declarations at transition sites)
**hypothesis:** V-04/R10 satisfies A-23 via parenthetical asides embedded in production
instructions: "(NO interceding content -- see anchor ordering above)". These are syntactically
subordinate -- a model can elide the parenthetical while preserving the grammatical sentence and
still violating the ordering. V-01/R11 replaces each aside with a standalone `CROSS-REF-REQUIRED:`
line emitted on its own line after the preceding anchor, before the next production instruction.
A standalone labeled line is an independent assertion: omitting it creates a structural gap.
Expected: A-23 PASS with higher compression resistance. All other criteria unchanged from
V-04/R10: A-01 through A-22 and A-24 PASS. Composite: 24/24.

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block at the top listing each role and one-line description.
If absent: produce `ROLES-NOTE:` block with inferred roles.
DO NOT write any other section until this block exists.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

DO produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE.
DO classify in three-tier order: Engineering first, Operations second, PM/Design/Research/Other third.
DO NOT interleave tiers.
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
MUST name both error risks:
- Over-structuring risk: principal risk of introducing structure prematurely, with >= 1
  concrete consequence (e.g., "decision overhead added before coordination failure rate
  justifies the cost")
- Under-coordination risk: principal risk of staying flat too long, with >= 1 concrete
  consequence (e.g., "competing roadmap commitments shipped to the same customer without
  a tie-break forum")
DO NOT merge this block with Sub-section 1. DO NOT omit.

**Sub-section 1 -- Case for Staying Flat**

DO produce a mechanism evidence table with exactly four columns:
`Mechanism Name | Mechanism Type | Frequency / Participants | Estimated Coordination Cost`
The `Mechanism Type` column MUST use only values from this closed set:
`Channel / Informal Role / Recurring Cadence / Shared Artifact`
DO NOT use values outside this vocabulary.
Floor is >= 2 data rows. Floor MUST include at least two distinct Mechanism Type category
values. Two rows of the same Mechanism Type value do NOT together satisfy the floor.
DO populate Estimated Coordination Cost with a numeric estimate per mechanism
(eng-hours per sprint, hours per week, or equivalent unit).

After the table, perform two counts before emitting the separator:
(1) Count data rows (header excluded). Verify count >= 2.
(2) Count distinct Mechanism Type category values represented.
Substitute N (rows) and K (categories), then emit exactly:
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded; {K} of 4 type classes represented. How We Coordinate Today begins.] ---`
DO NOT EMIT this separator before: row count >= 2 AND distinct Mechanism Type categories >= 2.
DO NOT begin Sub-section 2 until this separator is present.

**Sub-section 2 -- How We Coordinate Today**

DO inventory coordination patterns currently in active use.
DO name channels, cadences, informal roles, and artifacts with frequency and participants.
DO NOT re-list mechanism table entries from Sub-section 1.

**Sub-section 3 -- Rebuttal**

DO name the coordination failure the flat case and current mechanisms cannot answer.
DO reference a specific observable: blocked decision, missed SLA, time-zone gap, knowledge
silo, or competing roadmap conflict. DO NOT write "the team is growing" without a failure mode.

DO include an `UNCOVERED:` citation -- a labeled block naming at least one function, decision
class, or responsibility area with no current owner under the flat structure.
`[Zone: SUB-SECTION-3]`
Label it `UNCOVERED:` or equivalent. REQUIRED: additive to -- and MUST NOT replace -- the
named coordination failure.

**Sub-section 4 -- VERDICT and Re-assessment Trigger**

SUB-SECTION-4 ANCHOR ORDERING: MANDATORY THREE-ANCHOR SEQUENCE

The following three anchors MUST appear in Sub-section 4 in this exact order:
  (1) `COST-FRAME CONCLUSION:` line -- MUST be written first; MUST-PRECEDE all other content
  (2) `NET-COST-COMPARISON:` block -- MUST immediately follow item (1);
      DO NOT insert any content between `COST-FRAME CONCLUSION:` and `NET-COST-COMPARISON:`
  (3) `FLAT-CASE-PRESSURE:` line -- MUST immediately follow the close of item (2);
      DO NOT insert any content between the close of `NET-COST-COMPARISON:` and `FLAT-CASE-PRESSURE:`

DO NOT emit item (2) before item (1) is written.
DO NOT emit item (3) before item (2) is written and closed.

MUST produce `COST-FRAME CONCLUSION:` as the FIRST line of Sub-section 4. This line MUST:
(1) Name the `STRUCTURING-COST FRAME:` block by its label as the source of the evaluation frame
(2) Cite the dominant error risk by name -- exactly one of: over-structuring or under-coordination
(3) Name at least one of Sub-sections 1, 2, or 3 as the evidence source that elevated that risk

Example: `COST-FRAME CONCLUSION: STRUCTURING-COST FRAME applied; dominant risk is under-coordination; Sub-section 3 supplies the elevating evidence.`

After writing `COST-FRAME CONCLUSION:`, emit the following standalone declaration on its own line
before any other content:
`CROSS-REF-REQUIRED: NO interceding content between COST-FRAME CONCLUSION: and NET-COST-COMPARISON: -- see anchor ordering declaration above.`

Then produce the NET-COST-COMPARISON block:

```
NET-COST-COMPARISON:
  Flat coordination cost: [total from Sub-section 1 mechanism table, in stated units]
  Structure overhead: [meeting load + charter maintenance + escalation delay]
  Net delta: [flat cost minus structure overhead = signed value in same units]
  ADDITIVE-TO: C-01 FLAT-CASE-PRESSURE
```

The `ADDITIVE-TO: C-01 FLAT-CASE-PRESSURE` guard MUST appear as a labeled line inside the
NET-COST-COMPARISON block. DO NOT place it outside the block.
REQUIRED: guard line present inside the block before proceeding.
This block adds quantitative precision to FLAT-CASE-PRESSURE. It does NOT replace it.

After the NET-COST-COMPARISON block closes, emit the following standalone declaration on its own
line before any other content:
`CROSS-REF-REQUIRED: NO interceding content between NET-COST-COMPARISON: close and FLAT-CASE-PRESSURE: -- see anchor ordering declaration above.`

Then emit:
`FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
Rating MUST be exactly one value from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`
DO NOT omit this line. The arithmetic block does not discharge this requirement.

Choose exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
Reasoning MUST reference the FLAT-CASE-PRESSURE rating.
Verdict MUST be linked to the sign of the NET-COST-COMPARISON net delta.
DO write a concrete re-assessment trigger naming a threshold (headcount count, coordination-failure
signal, or milestone event). DO NOT write "revisit as the team grows."

If verdict is `CAN-OPERATE-FLAT`: produce a Flat Operating Rhythm block immediately after the
re-assessment trigger. At minimum two rows: one recurring alignment cadence and one
decision-escalation mechanism available under flat structure. Label: "Flat Operating Rhythm."
`[Zone: POST-VERDICT-BRANCH]`

DO NOT proceed past VERDICT until: COST-FRAME CONCLUSION + CROSS-REF-REQUIRED (first) +
NET-COST-COMPARISON (with ADDITIVE-TO guard) + CROSS-REF-REQUIRED (second) +
FLAT-CASE-PRESSURE + verdict declaration + re-assessment trigger are all written in the
mandatory anchor order.

INTEGRATION-NOTE -- POSITIONAL DISJOINTNESS CONFIRMATION

DO produce a labeled `INTEGRATION-NOTE:` block immediately after Sub-section 4 (after
re-assessment trigger and any CAN-OPERATE-FLAT branch content) and BEFORE the ASCII org
diagram. This block applies when all three positional aspirational artifacts are present.

REQUIRED format:
```
INTEGRATION-NOTE:
- STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT]: positioned before Sub-section 1
- UNCOVERED: citation [Zone: SUB-SECTION-3]: positioned within Sub-section 3
- Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH]: positioned after Sub-section 4, CAN-OPERATE-FLAT branch only
Positional disjointness confirmed: each artifact assigned to exactly one zone; no zone shared.
```

DO NOT omit when all three positional artifacts are present.
DO NOT place before Sub-section 4 or after the ASCII org diagram.
If verdict is `STRUCTURE-WARRANTED` (Flat Operating Rhythm absent): note N/A for the
POST-VERDICT-BRANCH entry and confirm disjointness for the two remaining artifacts.

DO emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
DO NOT draw any org boxes until this gate is present (after INTEGRATION-NOTE).

ASCII ORG DIAGRAM

DO draw ASCII hierarchy using box-drawing characters (`+`, `-`, `|`) or equivalent.
DO show at minimum two hierarchy levels.
DO NOT produce a flat list of names without hierarchy.
DO show committees as distinct labeled nodes, not embedded in an area.
DO use role names from ROLES-LOADED or ROLES-NOTE only. DO NOT introduce new role names.

DO emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
DO NOT begin the Headcount table until this gate is present.

HEADCOUNT BY AREA -- DECIDES / ESCALATES REQUIRED

DO produce a headcount table with exactly five columns:
`Area | Headcount | Key Roles | Decides | Escalates`
DO NOT use a single "Decision Scope" column. Decides and Escalates are separate and both REQUIRED.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward, naming the destination role or forum.
DO annotate each Key Roles entry as `[role name] ([domain type])` from ROLE-TYPE-CLASSIFICATION.
DO include at minimum two area rows plus a `**Total**` row with the sum.

OPERATING RHYTHM TABLE

DO produce a cadence table after the headcount section.
Columns: `Cadence | Frequency | DRI / Owner | Purpose`
DO include at minimum three distinct rows: one ROB, one shiproom or gate, one governance meeting.
DO NOT combine two meetings into one row.
DO reference a role from ROLES-LOADED in the DRI / Owner column where possible.

COMMITTEE CHARTERS -- FIVE FIELDS REQUIRED

DO write a charter for each governance meeting in the rhythm table.
DO include all five fields: Purpose, Membership, Decides, Escalates, Quorum.
DO NOT omit a charter for any governance meeting row.
DO annotate each Membership role as `[role name] ([domain type])`.
DO list at minimum two roles in Membership.
DO populate Escalates with a named destination.
DO NOT write "everything not listed under Decides."
Quorum REQUIRED format: `[N] of [M] member roles required for binding decisions`
DO NOT use a bare percentage or short N-only form. DO NOT omit Quorum from any charter.

DO emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
DO NOT begin the ORG-ELEMENT REGISTER until this gate is present.

ORG-ELEMENT REGISTER -- MUST PRECEDE ORG EVOLUTION ROADMAP

MUST produce as a named, physically distinct section immediately after the charters phase gate.
DO NOT embed entries as inline notes elsewhere. DO NOT skip this block.
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

  cat-1 (Areas):
    - [area name] -- headcount: [N]

  cat-2 (Committees/Cadences):
    - [committee or cadence name]

  cat-3 (Headcount):
    - Total headcount: [N]

  cat-4 (DRI Roles):
    - [DRI role]
```

ORG EVOLUTION ROADMAP -- REQUIRED

DO produce after the ORG-ELEMENT REGISTER.
Columns: `Trigger | Structural Change | Type`
REQUIRED: at minimum two rows.
Row 1: a headcount threshold trigger.
Row 2: a different category -- workload signal, structural symptom, or milestone event.
DO NOT write two headcount thresholds.

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

DO produce after the Org Evolution Roadmap.
MUST open each "Why It Applies Here" cell with:
`[element name] (cat-N) -- [one sentence of specific relevance]`
DO NOT name an element without the `(cat-N)` code.
DO NOT use a cat-N code not in the ORG-ELEMENT REGISTER schema.
DO include at minimum two anti-pattern rows.

SECTION ORDER -- DO NOT REORDER

1. ROLES-LOADED or ROLES-NOTE
2. ROLE-TYPE-CLASSIFICATION
3. Phase gate: ROLES COMPLETE
4. STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT] (before Sub-section 1)
5. Sub-section 1 (mechanism table + FLAT-CASE-CLOSED with type-diversity count)
6. Sub-section 2: How We Coordinate Today
7. Sub-section 3: Rebuttal (with UNCOVERED: citation [Zone: SUB-SECTION-3])
8. Sub-section 4: VERDICT (mandatory order: COST-FRAME CONCLUSION + CROSS-REF-REQUIRED + NET-COST-COMPARISON with ADDITIVE-TO guard + CROSS-REF-REQUIRED + FLAT-CASE-PRESSURE + verdict + re-assessment trigger + Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH] if applicable)
9. INTEGRATION-NOTE with [Zone: X] bracket notation (after Sub-section 4, before org diagram)
10. Phase gate: INERTIA COMPLETE
11. ASCII Org Diagram
12. Phase gate: STRUCTURE COMPLETE
13. Headcount by Area
14. Operating Rhythm Table
15. Committee Charters
16. Phase gate: CHARTERS COMPLETE
17. ORG-ELEMENT REGISTER
18. Org Evolution Roadmap
19. Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-02 -- Output Format: Explicit A-24 Format Prohibition

**axis:** output format (explicit `ZONE-NOTATION RULE:` prohibition in INTEGRATION-NOTE instruction)
**hypothesis:** V-05/R10 satisfies A-24 by showing the required `[Zone: X]` format in the
INTEGRATION-NOTE required-format example. A model with internalized parenthetical zone notation
`(DESIGNATOR)` may revert to it under compression even after seeing the bracket example, because
the example shows the right form but does not name or prohibit the wrong form. V-02/R11 adds a
`ZONE-NOTATION RULE:` block immediately after the required-format example, explicitly naming the
prohibited parenthetical forms and requiring `[Zone: X]` to match the A-22 inline labels exactly.
Teaching by contrast closes the reversion risk that positive example alone does not.
Expected: A-24 PASS with lower reversion probability. All other criteria unchanged from V-05/R10.
Composite: 24/24.

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block at the top listing each role and one-line description.
If absent: produce `ROLES-NOTE:` block with inferred roles.
DO NOT write any other section until this block exists.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

DO produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE.
DO classify in three-tier order: Engineering first, Operations second, PM/Design/Research/Other third.
DO NOT interleave tiers.
DO assign each role exactly one type from: `Engineering / PM / Design / Operations / Research / Other`
DO format each entry as: `- [role name] -- [domain type]`
DO annotate each Key Roles cell as `[role name] ([domain type])`.
DO annotate each Membership field as `[role name] ([domain type])`.
DO NOT skip any role from ROLES-LOADED or ROLES-NOTE.

DO emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
DO NOT proceed until this gate is present.

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.

STRUCTURING-COST FRAME -- PRE-ASSESSMENT BLOCK
`[Zone: PRE-ASSESSMENT]`

DO produce a labeled `STRUCTURING-COST FRAME:` block immediately before Sub-section 1.
MUST name both error risks:
- Over-structuring risk: principal risk of introducing structure prematurely, with >= 1
  concrete consequence (e.g., "decision overhead added before coordination failure rate
  justifies the cost")
- Under-coordination risk: principal risk of staying flat too long, with >= 1 concrete
  consequence (e.g., "competing roadmap commitments shipped to the same customer without
  a tie-break forum")
DO NOT merge this block with Sub-section 1. DO NOT omit.

**Sub-section 1 -- Case for Staying Flat**

DO produce a mechanism evidence table with exactly four columns:
`Mechanism Name | Mechanism Type | Frequency / Participants | Estimated Coordination Cost`
The `Mechanism Type` column MUST use only values from this closed set:
`Channel / Informal Role / Recurring Cadence / Shared Artifact`
DO NOT use values outside this vocabulary.
Floor is >= 2 data rows. Floor MUST include at least two distinct Mechanism Type category
values. Two rows of the same Mechanism Type value do NOT together satisfy the floor.
DO populate Estimated Coordination Cost with a numeric estimate per mechanism
(eng-hours per sprint, hours per week, or equivalent unit).

After the table, perform two counts before emitting the separator:
(1) Count data rows (header excluded). Verify count >= 2.
(2) Count distinct Mechanism Type category values represented.
Substitute N (rows) and K (categories), then emit exactly:
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded; {K} of 4 type classes represented. How We Coordinate Today begins.] ---`
DO NOT EMIT this separator before: row count >= 2 AND distinct Mechanism Type categories >= 2.
DO NOT begin Sub-section 2 until this separator is present.

**Sub-section 2 -- How We Coordinate Today**

DO inventory coordination patterns currently in active use.
DO name channels, cadences, informal roles, and artifacts with frequency and participants.
DO NOT re-list mechanism table entries from Sub-section 1.

**Sub-section 3 -- Rebuttal**

DO name the coordination failure the flat case and current mechanisms cannot answer.
DO reference a specific observable: blocked decision, missed SLA, time-zone gap, knowledge
silo, or competing roadmap conflict. DO NOT use vague failure modes.

DO include an `UNCOVERED:` citation -- a labeled block naming at least one function, decision
class, or responsibility area with no current owner under the flat structure.
`[Zone: SUB-SECTION-3]`
Label it `UNCOVERED:` or equivalent. REQUIRED: additive to -- and MUST NOT replace -- the
named coordination failure.

**Sub-section 4 -- VERDICT and Re-assessment Trigger**

SUB-SECTION-4-ANCHOR-SEQUENCE:
  Order 1: `COST-FRAME CONCLUSION:` line (write first; must precede all other Sub-section 4 content)
  Order 2: `NET-COST-COMPARISON:` block (write second; must immediately follow Order 1)
  Order 3: `FLAT-CASE-PRESSURE:` line (write third; must immediately follow Order 2 closing)
  CONSTRAINT: NO other content -- prose, labels, blank lines with content, or other blocks --
    may be inserted between Order 1 and Order 2, or between Order 2 and Order 3.

MUST produce `COST-FRAME CONCLUSION:` as the FIRST line of Sub-section 4 (see
SUB-SECTION-4-ANCHOR-SEQUENCE above). This line MUST:
(1) Name the `STRUCTURING-COST FRAME:` block by its label as the source of the evaluation frame
(2) Cite the dominant error risk by name -- exactly one of: over-structuring or under-coordination
(3) Name at least one of Sub-sections 1, 2, or 3 as the evidence source that elevated that risk

Example: `COST-FRAME CONCLUSION: STRUCTURING-COST FRAME applied; dominant risk is under-coordination; Sub-section 3 supplies the elevating evidence.`

Immediately after `COST-FRAME CONCLUSION:` (following the SUB-SECTION-4-ANCHOR-SEQUENCE CONSTRAINT --
NO other content between Order 1 and Order 2), produce the NET-COST-COMPARISON block:

```
NET-COST-COMPARISON:
  Flat coordination cost: [total from Sub-section 1 mechanism table, in stated units]
  Structure overhead: [meeting load + charter maintenance + escalation delay]
  Net delta: [flat cost minus structure overhead = signed value in same units]
  ADDITIVE-TO: C-01 FLAT-CASE-PRESSURE
```

The `ADDITIVE-TO: C-01 FLAT-CASE-PRESSURE` guard MUST appear as a labeled line inside the
NET-COST-COMPARISON block. DO NOT place it outside the block.
REQUIRED: guard line present inside the block before proceeding.
This block adds quantitative precision to FLAT-CASE-PRESSURE. It does NOT replace it.

Immediately after the NET-COST-COMPARISON block closes (following the SUB-SECTION-4-ANCHOR-SEQUENCE
CONSTRAINT -- NO other content between Order 2 and Order 3), emit:
`FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
Rating MUST be exactly one value from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`
DO NOT omit this line. The arithmetic block does not discharge this requirement.

Choose exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
Reasoning MUST reference the FLAT-CASE-PRESSURE rating.
Verdict MUST be linked to the sign of the NET-COST-COMPARISON net delta.
DO write a concrete re-assessment trigger naming a threshold (headcount count, coordination-failure
signal, or milestone event). DO NOT write "revisit as the team grows."

If verdict is `CAN-OPERATE-FLAT`: produce a Flat Operating Rhythm block immediately after the
re-assessment trigger. At minimum two rows: one recurring alignment cadence and one
decision-escalation mechanism available under flat structure. Label: "Flat Operating Rhythm."
`[Zone: POST-VERDICT-BRANCH]`

DO NOT proceed past VERDICT until: COST-FRAME CONCLUSION + NET-COST-COMPARISON (with
ADDITIVE-TO guard) + FLAT-CASE-PRESSURE + verdict declaration + re-assessment trigger
are all written in the SUB-SECTION-4-ANCHOR-SEQUENCE mandatory order.

INTEGRATION-NOTE -- POSITIONAL DISJOINTNESS CONFIRMATION

DO produce a labeled `INTEGRATION-NOTE:` block immediately after Sub-section 4 (after
re-assessment trigger and any CAN-OPERATE-FLAT branch content) and BEFORE the ASCII org
diagram. This block applies when all three positional aspirational artifacts are present.

REQUIRED format:
```
INTEGRATION-NOTE:
- STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT]: positioned before Sub-section 1
- UNCOVERED: citation [Zone: SUB-SECTION-3]: positioned within Sub-section 3
- Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH]: positioned after Sub-section 4, CAN-OPERATE-FLAT branch only
Positional disjointness confirmed: each artifact assigned to exactly one zone; no zone shared.
```

ZONE-NOTATION RULE: Each artifact entry in INTEGRATION-NOTE MUST use `[Zone: X]` bracket
format. DO NOT use parenthetical form: `(PRE-ASSESSMENT)`, `(SUB-SECTION-3)`, and
`(POST-VERDICT-BRANCH)` are all prohibited. The `[Zone: X]` notation in INTEGRATION-NOTE MUST
match the inline `[Zone: X]` labels at the artifact definition sites exactly -- same bracket
format, same designator string. No parenthetical alternatives.

DO NOT omit when all three positional artifacts are present.
DO NOT place before Sub-section 4 or after the ASCII org diagram.
If verdict is `STRUCTURE-WARRANTED` (Flat Operating Rhythm absent): note N/A for the
POST-VERDICT-BRANCH entry and confirm disjointness for the two remaining artifacts.

DO emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
DO NOT draw any org boxes until this gate is present (after INTEGRATION-NOTE).

ASCII ORG DIAGRAM

DO draw ASCII hierarchy using box-drawing characters (`+`, `-`, `|`) or equivalent.
DO show at minimum two hierarchy levels.
DO NOT produce a flat list of names without hierarchy.
DO show committees as distinct labeled nodes, not embedded in an area.
DO use role names from ROLES-LOADED or ROLES-NOTE only. DO NOT introduce new role names.

DO emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
DO NOT begin the Headcount table until this gate is present.

HEADCOUNT BY AREA -- DECIDES / ESCALATES REQUIRED

DO produce a headcount table with exactly five columns:
`Area | Headcount | Key Roles | Decides | Escalates`
DO NOT use a single "Decision Scope" column. Decides and Escalates are separate and both REQUIRED.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward, naming the destination role or forum.
DO annotate each Key Roles entry as `[role name] ([domain type])` from ROLE-TYPE-CLASSIFICATION.
DO include at minimum two area rows plus a `**Total**` row with the sum.

OPERATING RHYTHM TABLE

DO produce a cadence table after the headcount section.
Columns: `Cadence | Frequency | DRI / Owner | Purpose`
DO include at minimum three distinct rows: one ROB, one shiproom or gate, one governance meeting.
DO NOT combine two meetings into one row.
DO reference a role from ROLES-LOADED in the DRI / Owner column where possible.

COMMITTEE CHARTERS -- FIVE FIELDS REQUIRED

DO write a charter for each governance meeting in the rhythm table.
DO include all five fields: Purpose, Membership, Decides, Escalates, Quorum.
DO NOT omit a charter for any governance meeting row.
DO annotate each Membership role as `[role name] ([domain type])`.
DO list at minimum two roles in Membership.
DO populate Escalates with a named destination.
DO NOT write "everything not listed under Decides."
Quorum REQUIRED format: `[N] of [M] member roles required for binding decisions`
DO NOT use a bare percentage or short N-only form. DO NOT omit Quorum from any charter.

DO emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
DO NOT begin the ORG-ELEMENT REGISTER until this gate is present.

ORG-ELEMENT REGISTER -- MUST PRECEDE ORG EVOLUTION ROADMAP

MUST produce as a named, physically distinct section immediately after the charters phase gate.
DO NOT embed entries as inline notes elsewhere. DO NOT skip this block.
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

  cat-1 (Areas):
    - [area name] -- headcount: [N]

  cat-2 (Committees/Cadences):
    - [committee or cadence name]

  cat-3 (Headcount):
    - Total headcount: [N]

  cat-4 (DRI Roles):
    - [DRI role]
```

ORG EVOLUTION ROADMAP -- REQUIRED

DO produce after the ORG-ELEMENT REGISTER.
Columns: `Trigger | Structural Change | Type`
REQUIRED: at minimum two rows.
Row 1: a headcount threshold trigger.
Row 2: a different category -- workload signal, structural symptom, or milestone event.
DO NOT write two headcount thresholds.

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

DO produce after the Org Evolution Roadmap.
MUST open each "Why It Applies Here" cell with:
`[element name] (cat-N) -- [one sentence of specific relevance]`
DO NOT name an element without the `(cat-N)` code.
DO NOT use a cat-N code not in the ORG-ELEMENT REGISTER schema.
DO include at minimum two anti-pattern rows.

SECTION ORDER -- DO NOT REORDER

1. ROLES-LOADED or ROLES-NOTE
2. ROLE-TYPE-CLASSIFICATION
3. Phase gate: ROLES COMPLETE
4. STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT] (before Sub-section 1)
5. Sub-section 1 (mechanism table + FLAT-CASE-CLOSED with type-diversity count)
6. Sub-section 2: How We Coordinate Today
7. Sub-section 3: Rebuttal (with UNCOVERED: citation [Zone: SUB-SECTION-3])
8. Sub-section 4: VERDICT (SUB-SECTION-4-ANCHOR-SEQUENCE mandatory order: COST-FRAME CONCLUSION + NET-COST-COMPARISON with ADDITIVE-TO guard + FLAT-CASE-PRESSURE + verdict + re-assessment trigger + Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH] if applicable)
9. INTEGRATION-NOTE with [Zone: X] bracket notation + ZONE-NOTATION RULE (after Sub-section 4, before org diagram)
10. Phase gate: INERTIA COMPLETE
11. ASCII Org Diagram
12. Phase gate: STRUCTURE COMPLETE
13. Headcount by Area
14. Operating Rhythm Table
15. Committee Charters
16. Phase gate: CHARTERS COMPLETE
17. ORG-ELEMENT REGISTER
18. Org Evolution Roadmap
19. Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-03 -- Lifecycle Emphasis: VERDICT-GATE Checklist with Dual A-23 Enforcement

**axis:** lifecycle emphasis (VERDICT-GATE checklist replacing prose DO-NOT-PROCEED guard)
**hypothesis:** V-04/R10 enforces A-23 at production time: cross-references appear in the
production instructions for NET-COST-COMPARISON and FLAT-CASE-PRESSURE. A model that emits
cross-references at production time but simplifies them during a revision or summary pass
would still fail A-23 in the final artifact. V-03/R11 adds a VERDICT-GATE checklist at
verification time -- a 6-item structured checklist that replaces the prose DO-NOT-PROCEED
guard. Items 2 and 4 of the checklist carry explicit cross-references to the anchor ordering
declaration, making A-23 compliance a stated verification requirement at gate passage. Dual-site
enforcement (production instructions + verification gate) closes the gap between instruction
and confirmed compliance. Expected: A-23 PASS with dual enforcement. Composite: 24/24.

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block at the top listing each role and one-line description.
If absent: produce `ROLES-NOTE:` block with inferred roles.
DO NOT write any other section until this block exists.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

DO produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE.
DO classify in three-tier order: Engineering first, Operations second, PM/Design/Research/Other third.
DO NOT interleave tiers.
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
MUST name both error risks:
- Over-structuring risk: principal risk of introducing structure prematurely, with >= 1
  concrete consequence (e.g., "decision overhead added before coordination failure rate
  justifies the cost")
- Under-coordination risk: principal risk of staying flat too long, with >= 1 concrete
  consequence (e.g., "competing roadmap commitments shipped to the same customer without
  a tie-break forum")
DO NOT merge this block with Sub-section 1. DO NOT omit.

**Sub-section 1 -- Case for Staying Flat**

DO produce a mechanism evidence table with exactly four columns:
`Mechanism Name | Mechanism Type | Frequency / Participants | Estimated Coordination Cost`
The `Mechanism Type` column MUST use only values from this closed set:
`Channel / Informal Role / Recurring Cadence / Shared Artifact`
DO NOT use values outside this vocabulary.
Floor is >= 2 data rows. Floor MUST include at least two distinct Mechanism Type category
values. Two rows of the same Mechanism Type value do NOT together satisfy the floor.
DO populate Estimated Coordination Cost with a numeric estimate per mechanism
(eng-hours per sprint, hours per week, or equivalent unit).

After the table, perform two counts before emitting the separator:
(1) Count data rows (header excluded). Verify count >= 2.
(2) Count distinct Mechanism Type category values represented.
Substitute N (rows) and K (categories), then emit exactly:
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded; {K} of 4 type classes represented. How We Coordinate Today begins.] ---`
DO NOT EMIT this separator before: row count >= 2 AND distinct Mechanism Type categories >= 2.
DO NOT begin Sub-section 2 until this separator is present.

**Sub-section 2 -- How We Coordinate Today**

DO inventory coordination patterns currently in active use.
DO name channels, cadences, informal roles, and artifacts with frequency and participants.
DO NOT re-list mechanism table entries from Sub-section 1.

**Sub-section 3 -- Rebuttal**

DO name the coordination failure the flat case and current mechanisms cannot answer.
DO reference a specific observable: blocked decision, missed SLA, time-zone gap, knowledge
silo, or competing roadmap conflict. DO NOT write "the team is growing" without a failure mode.

DO include an `UNCOVERED:` citation -- a labeled block naming at least one function, decision
class, or responsibility area with no current owner under the flat structure.
`[Zone: SUB-SECTION-3]`
Label it `UNCOVERED:` or equivalent. REQUIRED: additive to -- and MUST NOT replace -- the
named coordination failure.

**Sub-section 4 -- VERDICT and Re-assessment Trigger**

SUB-SECTION-4 ANCHOR ORDERING: MANDATORY THREE-ANCHOR SEQUENCE

The following three anchors MUST appear in Sub-section 4 in this exact order:
  (1) `COST-FRAME CONCLUSION:` line -- MUST be written first; MUST-PRECEDE all other content
  (2) `NET-COST-COMPARISON:` block -- MUST immediately follow item (1);
      DO NOT insert any content between `COST-FRAME CONCLUSION:` and `NET-COST-COMPARISON:`
  (3) `FLAT-CASE-PRESSURE:` line -- MUST immediately follow the close of item (2);
      DO NOT insert any content between the close of `NET-COST-COMPARISON:` and `FLAT-CASE-PRESSURE:`

DO NOT emit item (2) before item (1) is written.
DO NOT emit item (3) before item (2) is written and closed.

MUST produce `COST-FRAME CONCLUSION:` as the FIRST line of Sub-section 4. This line MUST:
(1) Name the `STRUCTURING-COST FRAME:` block by its label as the source of the evaluation frame
(2) Cite the dominant error risk by name -- exactly one of: over-structuring or under-coordination
(3) Name at least one of Sub-sections 1, 2, or 3 as the evidence source that elevated that risk

Example: `COST-FRAME CONCLUSION: STRUCTURING-COST FRAME applied; dominant risk is under-coordination; Sub-section 3 supplies the elevating evidence.`

Immediately after `COST-FRAME CONCLUSION:` (NO interceding content -- see anchor ordering above),
produce the NET-COST-COMPARISON block:

```
NET-COST-COMPARISON:
  Flat coordination cost: [total from Sub-section 1 mechanism table, in stated units]
  Structure overhead: [meeting load + charter maintenance + escalation delay]
  Net delta: [flat cost minus structure overhead = signed value in same units]
  ADDITIVE-TO: C-01 FLAT-CASE-PRESSURE
```

The `ADDITIVE-TO: C-01 FLAT-CASE-PRESSURE` guard MUST appear as a labeled line inside the
NET-COST-COMPARISON block. DO NOT place it outside the block.
REQUIRED: guard line present inside the block before proceeding.
This block adds quantitative precision to FLAT-CASE-PRESSURE. It does NOT replace it.

Immediately after the NET-COST-COMPARISON block closes (NO interceding content -- see anchor
ordering above), emit:
`FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
Rating MUST be exactly one value from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`
DO NOT omit this line. The arithmetic block does not discharge this requirement.

Choose exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
Reasoning MUST reference the FLAT-CASE-PRESSURE rating.
Verdict MUST be linked to the sign of the NET-COST-COMPARISON net delta.
DO write a concrete re-assessment trigger naming a threshold (headcount count, coordination-failure
signal, or milestone event). DO NOT write "revisit as the team grows."

If verdict is `CAN-OPERATE-FLAT`: produce a Flat Operating Rhythm block immediately after the
re-assessment trigger. At minimum two rows: one recurring alignment cadence and one
decision-escalation mechanism available under flat structure. Label: "Flat Operating Rhythm."
`[Zone: POST-VERDICT-BRANCH]`

VERDICT-GATE CHECKLIST -- confirm all six items before proceeding past VERDICT:
  [ ] (1) COST-FRAME CONCLUSION: written as the first line of Sub-section 4
  [ ] (2) NET-COST-COMPARISON: written immediately after, with NO interceding content
          (see anchor ordering declaration above -- items (1) and (2) must be adjacent)
  [ ] (3) ADDITIVE-TO: C-01 FLAT-CASE-PRESSURE guard line present inside NET-COST-COMPARISON block
  [ ] (4) FLAT-CASE-PRESSURE: written immediately after NET-COST-COMPARISON closes, with NO
          interceding content (see anchor ordering declaration above -- items (2) and (3) must be adjacent)
  [ ] (5) Verdict declaration present: exactly `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`
  [ ] (6) Re-assessment trigger present, naming a specific threshold

DO NOT proceed past VERDICT until all six checklist items are confirmed.

INTEGRATION-NOTE -- POSITIONAL DISJOINTNESS CONFIRMATION

DO produce a labeled `INTEGRATION-NOTE:` block immediately after Sub-section 4 (after
re-assessment trigger and any CAN-OPERATE-FLAT branch content) and BEFORE the ASCII org
diagram. This block applies when all three positional aspirational artifacts are present.

REQUIRED format:
```
INTEGRATION-NOTE:
- STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT]: positioned before Sub-section 1
- UNCOVERED: citation [Zone: SUB-SECTION-3]: positioned within Sub-section 3
- Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH]: positioned after Sub-section 4, CAN-OPERATE-FLAT branch only
Positional disjointness confirmed: each artifact assigned to exactly one zone; no zone shared.
```

DO NOT omit when all three positional artifacts are present.
DO NOT place before Sub-section 4 or after the ASCII org diagram.
If verdict is `STRUCTURE-WARRANTED` (Flat Operating Rhythm absent): note N/A for the
POST-VERDICT-BRANCH entry and confirm disjointness for the two remaining artifacts.

DO emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
DO NOT draw any org boxes until this gate is present (after INTEGRATION-NOTE).

ASCII ORG DIAGRAM

DO draw ASCII hierarchy using box-drawing characters (`+`, `-`, `|`) or equivalent.
DO show at minimum two hierarchy levels.
DO NOT produce a flat list of names without hierarchy.
DO show committees as distinct labeled nodes, not embedded in an area.
DO use role names from ROLES-LOADED or ROLES-NOTE only. DO NOT introduce new role names.

DO emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
DO NOT begin the Headcount table until this gate is present.

HEADCOUNT BY AREA -- DECIDES / ESCALATES REQUIRED

DO produce a headcount table with exactly five columns:
`Area | Headcount | Key Roles | Decides | Escalates`
DO NOT use a single "Decision Scope" column. Decides and Escalates are separate and both REQUIRED.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward, naming the destination role or forum.
DO annotate each Key Roles entry as `[role name] ([domain type])` from ROLE-TYPE-CLASSIFICATION.
DO include at minimum two area rows plus a `**Total**` row with the sum.

OPERATING RHYTHM TABLE

DO produce a cadence table after the headcount section.
Columns: `Cadence | Frequency | DRI / Owner | Purpose`
DO include at minimum three distinct rows: one ROB, one shiproom or gate, one governance meeting.
DO NOT combine two meetings into one row.
DO reference a role from ROLES-LOADED in the DRI / Owner column where possible.

COMMITTEE CHARTERS -- FIVE FIELDS REQUIRED

DO write a charter for each governance meeting in the rhythm table.
DO include all five fields: Purpose, Membership, Decides, Escalates, Quorum.
DO NOT omit a charter for any governance meeting row.
DO annotate each Membership role as `[role name] ([domain type])`.
DO list at minimum two roles in Membership.
DO populate Escalates with a named destination.
DO NOT write "everything not listed under Decides."
Quorum REQUIRED format: `[N] of [M] member roles required for binding decisions`
DO NOT use a bare percentage or short N-only form. DO NOT omit Quorum from any charter.

DO emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
DO NOT begin the ORG-ELEMENT REGISTER until this gate is present.

ORG-ELEMENT REGISTER -- MUST PRECEDE ORG EVOLUTION ROADMAP

MUST produce as a named, physically distinct section immediately after the charters phase gate.
DO NOT embed entries as inline notes elsewhere. DO NOT skip this block.
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

  cat-1 (Areas):
    - [area name] -- headcount: [N]

  cat-2 (Committees/Cadences):
    - [committee or cadence name]

  cat-3 (Headcount):
    - Total headcount: [N]

  cat-4 (DRI Roles):
    - [DRI role]
```

ORG EVOLUTION ROADMAP -- REQUIRED

DO produce after the ORG-ELEMENT REGISTER.
Columns: `Trigger | Structural Change | Type`
REQUIRED: at minimum two rows.
Row 1: a headcount threshold trigger.
Row 2: a different category -- workload signal, structural symptom, or milestone event.
DO NOT write two headcount thresholds.

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

DO produce after the Org Evolution Roadmap.
MUST open each "Why It Applies Here" cell with:
`[element name] (cat-N) -- [one sentence of specific relevance]`
DO NOT name an element without the `(cat-N)` code.
DO NOT use a cat-N code not in the ORG-ELEMENT REGISTER schema.
DO include at minimum two anti-pattern rows.

SECTION ORDER -- DO NOT REORDER

1. ROLES-LOADED or ROLES-NOTE
2. ROLE-TYPE-CLASSIFICATION
3. Phase gate: ROLES COMPLETE
4. STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT] (before Sub-section 1)
5. Sub-section 1 (mechanism table + FLAT-CASE-CLOSED with type-diversity count)
6. Sub-section 2: How We Coordinate Today
7. Sub-section 3: Rebuttal (with UNCOVERED: citation [Zone: SUB-SECTION-3])
8. Sub-section 4: VERDICT (mandatory order: COST-FRAME CONCLUSION + NET-COST-COMPARISON with ADDITIVE-TO guard + FLAT-CASE-PRESSURE + verdict + re-assessment trigger + VERDICT-GATE CHECKLIST + Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH] if applicable)
9. INTEGRATION-NOTE with [Zone: X] bracket notation (after Sub-section 4, before org diagram)
10. Phase gate: INERTIA COMPLETE
11. ASCII Org Diagram
12. Phase gate: STRUCTURE COMPLETE
13. Headcount by Area
14. Operating Rhythm Table
15. Committee Charters
16. Phase gate: CHARTERS COMPLETE
17. ORG-ELEMENT REGISTER
18. Org Evolution Roadmap
19. Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-04 -- Combined: Dedicated Block + Standalone Declarations + Explicit Prohibition

**axis:** combined correctness + output format (V-05/R10 dedicated block base + V-01 standalone
cross-ref declarations + V-02 explicit A-24 prohibition)
**hypothesis:** V-05/R10 achieves 24/24 under v10 but relies on embedded constraint citations
for A-23 and a format example alone for A-24. V-04/R11 adds two robustness improvements:
(1) Standalone `CROSS-REF-REQUIRED:` declarations on their own lines at each transition site
(A-23 -- declarations cannot be elided without leaving a structural gap), and
(2) `ZONE-NOTATION RULE:` block explicitly prohibiting parenthetical form in INTEGRATION-NOTE
(A-24 -- teaching by contrast, not positive example only).
Both improvements target structurally isolated positions in the prompt and have no interactions.
Expected: A-01 through A-24 PASS. Composite: 24/24, maximum robustness for the A-21/A-23/A-24
cluster under the dedicated block architecture.

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block at the top listing each role and one-line description.
If absent: produce `ROLES-NOTE:` block with inferred roles.
DO NOT write any other section until this block exists.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

DO produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE.
DO classify in three-tier order: Engineering first, Operations second, PM/Design/Research/Other third.
DO NOT interleave tiers.
DO assign each role exactly one type from: `Engineering / PM / Design / Operations / Research / Other`
DO format each entry as: `- [role name] -- [domain type]`
DO annotate each Key Roles cell as `[role name] ([domain type])`.
DO annotate each Membership field as `[role name] ([domain type])`.
DO NOT skip any role from ROLES-LOADED or ROLES-NOTE.

DO emit: `=== [PHASE GATE: ROLES COMPLETE -- INERTIA ASSESSMENT BEGINS] ===`
DO NOT proceed until this gate is present.

INERTIA ASSESSMENT -- FOUR SUB-SECTIONS, STEELMAN FIRST

DO write the Inertia Assessment before any org boxes.

STRUCTURING-COST FRAME -- PRE-ASSESSMENT BLOCK
`[Zone: PRE-ASSESSMENT]`

DO produce a labeled `STRUCTURING-COST FRAME:` block immediately before Sub-section 1.
MUST name both error risks:
- Over-structuring risk: principal risk of introducing structure prematurely, with >= 1
  concrete consequence (e.g., "decision overhead added before coordination failure rate
  justifies the cost")
- Under-coordination risk: principal risk of staying flat too long, with >= 1 concrete
  consequence (e.g., "competing roadmap commitments shipped to the same customer without
  a tie-break forum")
DO NOT merge this block with Sub-section 1. DO NOT omit.

**Sub-section 1 -- Case for Staying Flat**

DO produce a mechanism evidence table with exactly four columns:
`Mechanism Name | Mechanism Type | Frequency / Participants | Estimated Coordination Cost`
The `Mechanism Type` column MUST use only values from this closed set:
`Channel / Informal Role / Recurring Cadence / Shared Artifact`
DO NOT use values outside this vocabulary.
Floor is >= 2 data rows. Floor MUST include at least two distinct Mechanism Type category
values. Two rows of the same Mechanism Type value do NOT together satisfy the floor.
DO populate Estimated Coordination Cost with a numeric estimate per mechanism
(eng-hours per sprint, hours per week, or equivalent unit).

After the table, perform two counts before emitting the separator:
(1) Count data rows (header excluded). Verify count >= 2.
(2) Count distinct Mechanism Type category values represented.
Substitute N (rows) and K (categories), then emit exactly:
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded; {K} of 4 type classes represented. How We Coordinate Today begins.] ---`
DO NOT EMIT this separator before: row count >= 2 AND distinct Mechanism Type categories >= 2.
DO NOT begin Sub-section 2 until this separator is present.

**Sub-section 2 -- How We Coordinate Today**

DO inventory coordination patterns currently in active use.
DO name channels, cadences, informal roles, and artifacts with frequency and participants.
DO NOT re-list mechanism table entries from Sub-section 1.

**Sub-section 3 -- Rebuttal**

DO name the coordination failure the flat case and current mechanisms cannot answer.
DO reference a specific observable: blocked decision, missed SLA, time-zone gap, knowledge
silo, or competing roadmap conflict. DO NOT use vague failure modes.

DO include an `UNCOVERED:` citation -- a labeled block naming at least one function, decision
class, or responsibility area with no current owner under the flat structure.
`[Zone: SUB-SECTION-3]`
Label it `UNCOVERED:` or equivalent. REQUIRED: additive to -- and MUST NOT replace -- the
named coordination failure.

**Sub-section 4 -- VERDICT and Re-assessment Trigger**

SUB-SECTION-4-ANCHOR-SEQUENCE:
  Order 1: `COST-FRAME CONCLUSION:` line (write first; must precede all other Sub-section 4 content)
  Order 2: `NET-COST-COMPARISON:` block (write second; must immediately follow Order 1)
  Order 3: `FLAT-CASE-PRESSURE:` line (write third; must immediately follow Order 2 closing)
  CONSTRAINT: NO other content -- prose, labels, blank lines with content, or other blocks --
    may be inserted between Order 1 and Order 2, or between Order 2 and Order 3.

MUST produce `COST-FRAME CONCLUSION:` as the FIRST line of Sub-section 4 (see
SUB-SECTION-4-ANCHOR-SEQUENCE above). This line MUST:
(1) Name the `STRUCTURING-COST FRAME:` block by its label as the source of the evaluation frame
(2) Cite the dominant error risk by name -- exactly one of: over-structuring or under-coordination
(3) Name at least one of Sub-sections 1, 2, or 3 as the evidence source that elevated that risk

Example: `COST-FRAME CONCLUSION: STRUCTURING-COST FRAME applied; dominant risk is under-coordination; Sub-section 3 supplies the elevating evidence.`

After writing `COST-FRAME CONCLUSION:`, emit the following standalone declaration on its own line
before producing any other content:
`CROSS-REF-REQUIRED: NO interceding content between COST-FRAME CONCLUSION: and NET-COST-COMPARISON: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

Then produce the NET-COST-COMPARISON block:

```
NET-COST-COMPARISON:
  Flat coordination cost: [total from Sub-section 1 mechanism table, in stated units]
  Structure overhead: [meeting load + charter maintenance + escalation delay]
  Net delta: [flat cost minus structure overhead = signed value in same units]
  ADDITIVE-TO: C-01 FLAT-CASE-PRESSURE
```

The `ADDITIVE-TO: C-01 FLAT-CASE-PRESSURE` guard MUST appear as a labeled line inside the
NET-COST-COMPARISON block. DO NOT place it outside the block.
REQUIRED: guard line present inside the block before proceeding.
This block adds quantitative precision to FLAT-CASE-PRESSURE. It does NOT replace it.

After the NET-COST-COMPARISON block closes, emit the following standalone declaration on its own
line before producing any other content:
`CROSS-REF-REQUIRED: NO interceding content between NET-COST-COMPARISON: close and FLAT-CASE-PRESSURE: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

Then emit:
`FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
Rating MUST be exactly one value from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`
DO NOT omit this line. The arithmetic block does not discharge this requirement.

Choose exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
Reasoning MUST reference the FLAT-CASE-PRESSURE rating.
Verdict MUST be linked to the sign of the NET-COST-COMPARISON net delta.
DO write a concrete re-assessment trigger naming a threshold (headcount count, coordination-failure
signal, or milestone event). DO NOT write "revisit as the team grows."

If verdict is `CAN-OPERATE-FLAT`: produce a Flat Operating Rhythm block immediately after the
re-assessment trigger. At minimum two rows: one recurring alignment cadence and one
decision-escalation mechanism available under flat structure. Label: "Flat Operating Rhythm."
`[Zone: POST-VERDICT-BRANCH]`

DO NOT proceed past VERDICT until: COST-FRAME CONCLUSION + CROSS-REF-REQUIRED (first) +
NET-COST-COMPARISON (with ADDITIVE-TO guard) + CROSS-REF-REQUIRED (second) +
FLAT-CASE-PRESSURE + verdict declaration + re-assessment trigger are all written in the
SUB-SECTION-4-ANCHOR-SEQUENCE mandatory order.

INTEGRATION-NOTE -- POSITIONAL DISJOINTNESS CONFIRMATION

DO produce a labeled `INTEGRATION-NOTE:` block immediately after Sub-section 4 (after
re-assessment trigger and any CAN-OPERATE-FLAT branch content) and BEFORE the ASCII org
diagram. This block applies when all three positional aspirational artifacts are present.

REQUIRED format:
```
INTEGRATION-NOTE:
- STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT]: positioned before Sub-section 1
- UNCOVERED: citation [Zone: SUB-SECTION-3]: positioned within Sub-section 3
- Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH]: positioned after Sub-section 4, CAN-OPERATE-FLAT branch only
Positional disjointness confirmed: each artifact assigned to exactly one zone; no zone shared.
```

ZONE-NOTATION RULE: Each artifact entry in INTEGRATION-NOTE MUST use `[Zone: X]` bracket
format. DO NOT use parenthetical form: `(PRE-ASSESSMENT)`, `(SUB-SECTION-3)`, and
`(POST-VERDICT-BRANCH)` are all prohibited. The `[Zone: X]` notation in INTEGRATION-NOTE MUST
match the inline `[Zone: X]` labels at the artifact definition sites exactly -- same bracket
format, same designator string. No parenthetical alternatives.

DO NOT omit when all three positional artifacts are present.
DO NOT place before Sub-section 4 or after the ASCII org diagram.
If verdict is `STRUCTURE-WARRANTED` (Flat Operating Rhythm absent): note N/A for the
POST-VERDICT-BRANCH entry and confirm disjointness for the two remaining artifacts.

DO emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
DO NOT draw any org boxes until this gate is present (after INTEGRATION-NOTE).

ASCII ORG DIAGRAM

DO draw ASCII hierarchy using box-drawing characters (`+`, `-`, `|`) or equivalent.
DO show at minimum two hierarchy levels.
DO NOT produce a flat list of names without hierarchy.
DO show committees as distinct labeled nodes, not embedded in an area.
DO use role names from ROLES-LOADED or ROLES-NOTE only. DO NOT introduce new role names.

DO emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
DO NOT begin the Headcount table until this gate is present.

HEADCOUNT BY AREA -- DECIDES / ESCALATES REQUIRED

DO produce a headcount table with exactly five columns:
`Area | Headcount | Key Roles | Decides | Escalates`
DO NOT use a single "Decision Scope" column. Decides and Escalates are separate and both REQUIRED.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward, naming the destination role or forum.
DO annotate each Key Roles entry as `[role name] ([domain type])` from ROLE-TYPE-CLASSIFICATION.
DO include at minimum two area rows plus a `**Total**` row with the sum.

OPERATING RHYTHM TABLE

DO produce a cadence table after the headcount section.
Columns: `Cadence | Frequency | DRI / Owner | Purpose`
DO include at minimum three distinct rows: one ROB, one shiproom or gate, one governance meeting.
DO NOT combine two meetings into one row.
DO reference a role from ROLES-LOADED in the DRI / Owner column where possible.

COMMITTEE CHARTERS -- FIVE FIELDS REQUIRED

DO write a charter for each governance meeting in the rhythm table.
DO include all five fields: Purpose, Membership, Decides, Escalates, Quorum.
DO NOT omit a charter for any governance meeting row.
DO annotate each Membership role as `[role name] ([domain type])`.
DO list at minimum two roles in Membership.
DO populate Escalates with a named destination.
DO NOT write "everything not listed under Decides."
Quorum REQUIRED format: `[N] of [M] member roles required for binding decisions`
DO NOT use a bare percentage or short N-only form. DO NOT omit Quorum from any charter.

DO emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
DO NOT begin the ORG-ELEMENT REGISTER until this gate is present.

ORG-ELEMENT REGISTER -- MUST PRECEDE ORG EVOLUTION ROADMAP

MUST produce as a named, physically distinct section immediately after the charters phase gate.
DO NOT embed entries as inline notes elsewhere. DO NOT skip this block.
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

  cat-1 (Areas):
    - [area name] -- headcount: [N]

  cat-2 (Committees/Cadences):
    - [committee or cadence name]

  cat-3 (Headcount):
    - Total headcount: [N]

  cat-4 (DRI Roles):
    - [DRI role]
```

ORG EVOLUTION ROADMAP -- REQUIRED

DO produce after the ORG-ELEMENT REGISTER.
Columns: `Trigger | Structural Change | Type`
REQUIRED: at minimum two rows.
Row 1: a headcount threshold trigger.
Row 2: a different category -- workload signal, structural symptom, or milestone event.
DO NOT write two headcount thresholds.

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

DO produce after the Org Evolution Roadmap.
MUST open each "Why It Applies Here" cell with:
`[element name] (cat-N) -- [one sentence of specific relevance]`
DO NOT name an element without the `(cat-N)` code.
DO NOT use a cat-N code not in the ORG-ELEMENT REGISTER schema.
DO include at minimum two anti-pattern rows.

SECTION ORDER -- DO NOT REORDER

1. ROLES-LOADED or ROLES-NOTE
2. ROLE-TYPE-CLASSIFICATION
3. Phase gate: ROLES COMPLETE
4. STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT] (before Sub-section 1)
5. Sub-section 1 (mechanism table + FLAT-CASE-CLOSED with type-diversity count)
6. Sub-section 2: How We Coordinate Today
7. Sub-section 3: Rebuttal (with UNCOVERED: citation [Zone: SUB-SECTION-3])
8. Sub-section 4: VERDICT (SUB-SECTION-4-ANCHOR-SEQUENCE mandatory order: COST-FRAME CONCLUSION + CROSS-REF-REQUIRED + NET-COST-COMPARISON with ADDITIVE-TO guard + CROSS-REF-REQUIRED + FLAT-CASE-PRESSURE + verdict + re-assessment trigger + Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH] if applicable)
9. INTEGRATION-NOTE with [Zone: X] bracket notation + ZONE-NOTATION RULE (after Sub-section 4, before org diagram)
10. Phase gate: INERTIA COMPLETE
11. ASCII Org Diagram
12. Phase gate: STRUCTURE COMPLETE
13. Headcount by Area
14. Operating Rhythm Table
15. Committee Charters
16. Phase gate: CHARTERS COMPLETE
17. ORG-ELEMENT REGISTER
18. Org Evolution Roadmap
19. Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-05 -- Full Integration: Dedicated Block + Standalone Declarations + Explicit Prohibition + Gate Checklist

**axis:** full integration (V-04/R11 + V-03/R11: dedicated block + standalone declarations +
explicit prohibition + VERDICT-GATE checklist)
**hypothesis:** V-04/R11 provides maximum robustness for A-21, A-23, and A-24 through the
dedicated block + standalone cross-ref declarations + explicit parenthetical prohibition.
V-05/R11 adds the V-03 VERDICT-GATE checklist as a second enforcement site for A-23: items 2
and 4 of the checklist carry cross-references to the anchor ordering declaration, making the
sub-section 4 ordering a stated verification requirement at gate passage in addition to a
production-time instruction. The total enforcement chain for A-23: (1) SUB-SECTION-4-ANCHOR-
SEQUENCE block declares the ordering, (2) two CROSS-REF-REQUIRED standalone lines enforce it
at production time, (3) VERDICT-GATE checklist items 2 and 4 enforce it at verification time.
Expected: A-01 through A-24 all PASS. Composite: 24/24. Maximum compression resistance.

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.craft/roles/` before writing anything.
DO produce a `ROLES-LOADED:` block at the top listing each role and one-line description.
If absent: produce `ROLES-NOTE:` block with inferred roles.
DO NOT write any other section until this block exists.

ROLE-TYPE-CLASSIFICATION -- REQUIRED IMMEDIATELY AFTER ROLES-LOADED

DO produce a `ROLE-TYPE-CLASSIFICATION:` block immediately after ROLES-LOADED or ROLES-NOTE.
DO classify in three-tier order: Engineering first, Operations second, PM/Design/Research/Other third.
DO NOT interleave tiers.
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
MUST name both error risks:
- Over-structuring risk: principal risk of introducing structure prematurely, with >= 1
  concrete consequence (e.g., "decision overhead added before coordination failure rate
  justifies the cost")
- Under-coordination risk: principal risk of staying flat too long, with >= 1 concrete
  consequence (e.g., "competing roadmap commitments shipped to the same customer without
  a tie-break forum")
DO NOT merge this block with Sub-section 1. DO NOT omit.

**Sub-section 1 -- Case for Staying Flat**

DO produce a mechanism evidence table with exactly four columns:
`Mechanism Name | Mechanism Type | Frequency / Participants | Estimated Coordination Cost`
The `Mechanism Type` column MUST use only values from this closed set:
`Channel / Informal Role / Recurring Cadence / Shared Artifact`
DO NOT use values outside this vocabulary.
Floor is >= 2 data rows. Floor MUST include at least two distinct Mechanism Type category
values. Two rows of the same Mechanism Type value do NOT together satisfy the floor.
DO populate Estimated Coordination Cost with a numeric estimate per mechanism
(eng-hours per sprint, hours per week, or equivalent unit).

After the table, perform two counts before emitting the separator:
(1) Count data rows (header excluded). Verify count >= 2.
(2) Count distinct Mechanism Type category values represented.
Substitute N (rows) and K (categories), then emit exactly:
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded; {K} of 4 type classes represented. How We Coordinate Today begins.] ---`
DO NOT EMIT this separator before: row count >= 2 AND distinct Mechanism Type categories >= 2.
DO NOT begin Sub-section 2 until this separator is present.

**Sub-section 2 -- How We Coordinate Today**

DO inventory coordination patterns currently in active use.
DO name channels, cadences, informal roles, and artifacts with frequency and participants.
DO NOT re-list mechanism table entries from Sub-section 1.

**Sub-section 3 -- Rebuttal**

DO name the coordination failure the flat case and current mechanisms cannot answer.
DO reference a specific observable: blocked decision, missed SLA, time-zone gap, knowledge
silo, or competing roadmap conflict. DO NOT write "the team is growing" without a failure mode.

DO include an `UNCOVERED:` citation -- a labeled block naming at least one function, decision
class, or responsibility area with no current owner under the flat structure.
`[Zone: SUB-SECTION-3]`
Label it `UNCOVERED:` or equivalent. REQUIRED: additive to -- and MUST NOT replace -- the
named coordination failure.

**Sub-section 4 -- VERDICT and Re-assessment Trigger**

SUB-SECTION-4-ANCHOR-SEQUENCE:
  Order 1: `COST-FRAME CONCLUSION:` line (write first; must precede all other Sub-section 4 content)
  Order 2: `NET-COST-COMPARISON:` block (write second; must immediately follow Order 1)
  Order 3: `FLAT-CASE-PRESSURE:` line (write third; must immediately follow Order 2 closing)
  CONSTRAINT: NO other content -- prose, labels, blank lines with content, or other blocks --
    may be inserted between Order 1 and Order 2, or between Order 2 and Order 3.

MUST produce `COST-FRAME CONCLUSION:` as the FIRST line of Sub-section 4 (see
SUB-SECTION-4-ANCHOR-SEQUENCE above). This line MUST:
(1) Name the `STRUCTURING-COST FRAME:` block by its label as the source of the evaluation frame
(2) Cite the dominant error risk by name -- exactly one of: over-structuring or under-coordination
(3) Name at least one of Sub-sections 1, 2, or 3 as the evidence source that elevated that risk

Example: `COST-FRAME CONCLUSION: STRUCTURING-COST FRAME applied; dominant risk is under-coordination; Sub-section 3 supplies the elevating evidence.`

After writing `COST-FRAME CONCLUSION:`, emit the following standalone declaration on its own line
before producing any other content:
`CROSS-REF-REQUIRED: NO interceding content between COST-FRAME CONCLUSION: and NET-COST-COMPARISON: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

Then produce the NET-COST-COMPARISON block:

```
NET-COST-COMPARISON:
  Flat coordination cost: [total from Sub-section 1 mechanism table, in stated units]
  Structure overhead: [meeting load + charter maintenance + escalation delay]
  Net delta: [flat cost minus structure overhead = signed value in same units]
  ADDITIVE-TO: C-01 FLAT-CASE-PRESSURE
```

The `ADDITIVE-TO: C-01 FLAT-CASE-PRESSURE` guard MUST appear as a labeled line inside the
NET-COST-COMPARISON block. DO NOT place it outside the block.
REQUIRED: guard line present inside the block before proceeding.
This block adds quantitative precision to FLAT-CASE-PRESSURE. It does NOT replace it.

After the NET-COST-COMPARISON block closes, emit the following standalone declaration on its own
line before producing any other content:
`CROSS-REF-REQUIRED: NO interceding content between NET-COST-COMPARISON: close and FLAT-CASE-PRESSURE: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

Then emit:
`FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
Rating MUST be exactly one value from: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`
DO NOT omit this line. The arithmetic block does not discharge this requirement.

Choose exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
Reasoning MUST reference the FLAT-CASE-PRESSURE rating.
Verdict MUST be linked to the sign of the NET-COST-COMPARISON net delta.
DO write a concrete re-assessment trigger naming a threshold (headcount count, coordination-failure
signal, or milestone event). DO NOT write "revisit as the team grows."

If verdict is `CAN-OPERATE-FLAT`: produce a Flat Operating Rhythm block immediately after the
re-assessment trigger. At minimum two rows: one recurring alignment cadence and one
decision-escalation mechanism available under flat structure. Label: "Flat Operating Rhythm."
`[Zone: POST-VERDICT-BRANCH]`

VERDICT-GATE CHECKLIST -- confirm all six items before proceeding past VERDICT:
  [ ] (1) COST-FRAME CONCLUSION: written as the first line of Sub-section 4
  [ ] (2) CROSS-REF-REQUIRED declaration written on its own line immediately after
          (referencing SUB-SECTION-4-ANCHOR-SEQUENCE -- no interceding content before Order 2)
  [ ] (3) NET-COST-COMPARISON: block written immediately after, with ADDITIVE-TO guard inside
  [ ] (4) CROSS-REF-REQUIRED declaration written on its own line immediately after block closes
          (referencing SUB-SECTION-4-ANCHOR-SEQUENCE -- no interceding content before Order 3)
  [ ] (5) FLAT-CASE-PRESSURE: written immediately after, with valid closed-set rating
  [ ] (6) Verdict declaration (CAN-OPERATE-FLAT or STRUCTURE-WARRANTED) + re-assessment trigger

DO NOT proceed past VERDICT until all six checklist items are confirmed.

INTEGRATION-NOTE -- POSITIONAL DISJOINTNESS CONFIRMATION

DO produce a labeled `INTEGRATION-NOTE:` block immediately after Sub-section 4 (after
re-assessment trigger and any CAN-OPERATE-FLAT branch content) and BEFORE the ASCII org
diagram. This block applies when all three positional aspirational artifacts are present.

REQUIRED format:
```
INTEGRATION-NOTE:
- STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT]: positioned before Sub-section 1
- UNCOVERED: citation [Zone: SUB-SECTION-3]: positioned within Sub-section 3
- Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH]: positioned after Sub-section 4, CAN-OPERATE-FLAT branch only
Positional disjointness confirmed: each artifact assigned to exactly one zone; no zone shared.
```

ZONE-NOTATION RULE: Each artifact entry in INTEGRATION-NOTE MUST use `[Zone: X]` bracket
format. DO NOT use parenthetical form: `(PRE-ASSESSMENT)`, `(SUB-SECTION-3)`, and
`(POST-VERDICT-BRANCH)` are all prohibited. The `[Zone: X]` notation in INTEGRATION-NOTE MUST
match the inline `[Zone: X]` labels at the artifact definition sites exactly -- same bracket
format, same designator string. No parenthetical alternatives.

DO NOT omit when all three positional artifacts are present.
DO NOT place before Sub-section 4 or after the ASCII org diagram.
If verdict is `STRUCTURE-WARRANTED` (Flat Operating Rhythm absent): note N/A for the
POST-VERDICT-BRANCH entry and confirm disjointness for the two remaining artifacts.

DO emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
DO NOT draw any org boxes until this gate is present (after INTEGRATION-NOTE).

ASCII ORG DIAGRAM

DO draw ASCII hierarchy using box-drawing characters (`+`, `-`, `|`) or equivalent.
DO show at minimum two hierarchy levels.
DO NOT produce a flat list of names without hierarchy.
DO show committees as distinct labeled nodes, not embedded in an area.
DO use role names from ROLES-LOADED or ROLES-NOTE only. DO NOT introduce new role names.

DO emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`
DO NOT begin the Headcount table until this gate is present.

HEADCOUNT BY AREA -- DECIDES / ESCALATES REQUIRED

DO produce a headcount table with exactly five columns:
`Area | Headcount | Key Roles | Decides | Escalates`
DO NOT use a single "Decision Scope" column. Decides and Escalates are separate and both REQUIRED.
DO populate Decides with decision types owned at this level.
DO populate Escalates with decision types referred upward, naming the destination role or forum.
DO annotate each Key Roles entry as `[role name] ([domain type])` from ROLE-TYPE-CLASSIFICATION.
DO include at minimum two area rows plus a `**Total**` row with the sum.

OPERATING RHYTHM TABLE

DO produce a cadence table after the headcount section.
Columns: `Cadence | Frequency | DRI / Owner | Purpose`
DO include at minimum three distinct rows: one ROB, one shiproom or gate, one governance meeting.
DO NOT combine two meetings into one row.
DO reference a role from ROLES-LOADED in the DRI / Owner column where possible.

COMMITTEE CHARTERS -- FIVE FIELDS REQUIRED

DO write a charter for each governance meeting in the rhythm table.
DO include all five fields: Purpose, Membership, Decides, Escalates, Quorum.
DO NOT omit a charter for any governance meeting row.
DO annotate each Membership role as `[role name] ([domain type])`.
DO list at minimum two roles in Membership.
DO populate Escalates with a named destination.
DO NOT write "everything not listed under Decides."
Quorum REQUIRED format: `[N] of [M] member roles required for binding decisions`
DO NOT use a bare percentage or short N-only form. DO NOT omit Quorum from any charter.

DO emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`
DO NOT begin the ORG-ELEMENT REGISTER until this gate is present.

ORG-ELEMENT REGISTER -- MUST PRECEDE ORG EVOLUTION ROADMAP

MUST produce as a named, physically distinct section immediately after the charters phase gate.
DO NOT embed entries as inline notes elsewhere. DO NOT skip this block.
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

  cat-1 (Areas):
    - [area name] -- headcount: [N]

  cat-2 (Committees/Cadences):
    - [committee or cadence name]

  cat-3 (Headcount):
    - Total headcount: [N]

  cat-4 (DRI Roles):
    - [DRI role]
```

ORG EVOLUTION ROADMAP -- REQUIRED

DO produce after the ORG-ELEMENT REGISTER.
Columns: `Trigger | Structural Change | Type`
REQUIRED: at minimum two rows.
Row 1: a headcount threshold trigger.
Row 2: a different category -- workload signal, structural symptom, or milestone event.
DO NOT write two headcount thresholds.

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

DO produce after the Org Evolution Roadmap.
MUST open each "Why It Applies Here" cell with:
`[element name] (cat-N) -- [one sentence of specific relevance]`
DO NOT name an element without the `(cat-N)` code.
DO NOT use a cat-N code not in the ORG-ELEMENT REGISTER schema.
DO include at minimum two anti-pattern rows.

SECTION ORDER -- DO NOT REORDER

1. ROLES-LOADED or ROLES-NOTE
2. ROLE-TYPE-CLASSIFICATION
3. Phase gate: ROLES COMPLETE
4. STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT] (before Sub-section 1)
5. Sub-section 1 (mechanism table + FLAT-CASE-CLOSED with type-diversity count)
6. Sub-section 2: How We Coordinate Today
7. Sub-section 3: Rebuttal (with UNCOVERED: citation [Zone: SUB-SECTION-3])
8. Sub-section 4: VERDICT (SUB-SECTION-4-ANCHOR-SEQUENCE mandatory order: COST-FRAME CONCLUSION + CROSS-REF-REQUIRED + NET-COST-COMPARISON with ADDITIVE-TO guard + CROSS-REF-REQUIRED + FLAT-CASE-PRESSURE + verdict + re-assessment trigger + VERDICT-GATE CHECKLIST + Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH] if applicable)
9. INTEGRATION-NOTE with [Zone: X] bracket notation + ZONE-NOTATION RULE (after Sub-section 4, before org diagram)
10. Phase gate: INERTIA COMPLETE
11. ASCII Org Diagram
12. Phase gate: STRUCTURE COMPLETE
13. Headcount by Area
14. Operating Rhythm Table
15. Committee Charters
16. Phase gate: CHARTERS COMPLETE
17. ORG-ELEMENT REGISTER
18. Org Evolution Roadmap
19. Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} -- {date}`
