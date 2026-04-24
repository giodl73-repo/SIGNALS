---
skill: quest-variate
skill_target: org-chart
date: 2026-03-16
round: R10
rubric_version: v9
status: variate
---

# org-chart Variate -- Round 10

**Date:** 2026-03-16
**Skill:** org-chart
**Rubric:** v9 (A-01 through A-22; A-21/A-22 new from R9 excellence signals)
**Round:** R10 -- single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

**R9 ceiling:** V-05/R9 combines all A-01 through A-20 behaviors under v8. Score under v8:
20/20 = 10.0 aspirational, composite 100.0. Under v9 (denominator /22): V-05/R9 scores
20/22 = 9.09 aspirational, composite 99.09. Two new criteria are unaddressed:

- **A-21** `sub-section-4-anchor-ordering` -- When COST-FRAME CONCLUSION: (A-18),
  NET-COST-COMPARISON: block (A-10), and FLAT-CASE-PRESSURE: line (C-01) all co-occur
  in Sub-section 4, they must appear in fixed linear order with NO interceding content
  between adjacent anchors. V-05/R9 uses sequential "after X, produce Y" instructions
  but does not prohibit interceding content -- a reviewer cannot confirm the ordering
  constraint without parsing narrative semantics.
- **A-22** `per-artifact-inline-zone-label` -- When A-20 (INTEGRATION-NOTE) is active,
  each of A-14/A-15/A-16 must carry its canonical zone designator as an inline label
  (`[Zone: PRE-ASSESSMENT]`, `[Zone: SUB-SECTION-3]`, `[Zone: POST-VERDICT-BRANCH]`)
  inside the artifact's own instruction block. V-05/R9 uses prose notes ("Canonical zone
  designator for this artifact: PRE-ASSESSMENT") -- correct designator, wrong format.
  A-22 requires the bracketed `[Zone: X]` format matching the A-20 designators exactly.

**R10 target:** 22/22 aspirationally (composite 100.0 under v9) by adding:

- Explicit Sub-section 4 anchor ordering constraint with interceding-content prohibition (A-21)
- Per-artifact `[Zone: X]` inline zone labels on each of A-14/A-15/A-16 (A-22)

**Three questions drive R10:**

1. Does **inline MUST-PRECEDE anchor ordering** (A-21) -- adding a numbered anchor sequence
   with explicit MUST-PRECEDE gates and "NO other content between adjacent anchors" prohibition
   distributed across the Sub-section 4 instructions -- make the three-anchor order
   independently verifiable without a dedicated block? (V-01)
2. Does **per-artifact `[Zone: X]` inline label** (A-22) -- replacing prose "Canonical zone
   designator: X" with `[Zone: X]` format inside each artifact's own instruction block --
   satisfy the A-22 requirement that zone assignment be readable at the definition site? (V-02)
3. Does a **dedicated SUB-SECTION-4-ANCHOR-SEQUENCE block** (A-21 alternative) -- a labeled
   block that lists the three anchors as an ordered sequence with an explicit CONSTRAINT line --
   provide stronger positional enforcement than inline MUST-PRECEDE language alone? (V-03)

V-04/R10 combines A-21 (V-01 inline approach) + A-22, testing both additions together.
V-05/R10 combines A-21 (V-03 dedicated block approach) + A-22, testing maximum structural
enforcement against the same A-22 change.

---

## Round 10 Variation Map

| V | Axis | What Changes vs V-05/R9 | Hypothesis |
|---|------|-------------------------|------------|
| V-01 | correctness (anchor ordering: inline MUST-PRECEDE) | Sub-section 4: add numbered anchor sequence with MUST-PRECEDE gates and "NO interceding content" prohibition on each adjacent anchor pair. Prose zone designators unchanged. | V-05/R9 implies ordering but does not prohibit interceding content. Inline MUST-PRECEDE gates make the three-anchor sequence independently verifiable. A-21 PASS. A-22 absent. Composite: 21/22. |
| V-02 | output format (per-artifact inline zone labels) | Replace prose "Canonical zone designator: X" with `[Zone: X]` inline label inside each of A-14 (UNCOVERED:), A-15 (Flat Operating Rhythm), A-16 (STRUCTURING-COST FRAME) instruction blocks. Anchor ordering unchanged from V-05/R9. | V-05/R9 zone prose has correct designators but wrong format. `[Zone: X]` labels match A-20 canonical designators exactly and are readable at the definition site without consulting INTEGRATION-NOTE. A-22 PASS. A-21 absent. Composite: 21/22. |
| V-03 | correctness (anchor ordering: dedicated block) | Replace distributed Sub-section 4 ordering language with a dedicated labeled `SUB-SECTION-4-ANCHOR-SEQUENCE:` block listing the three anchors in order with an explicit CONSTRAINT line prohibiting interceding content. Prose zone designators unchanged. | Consolidated block provides a single independently verifiable constraint. Inline MUST-PRECEDE (V-01) can be dispersed under model compression; a dedicated block with an explicit CONSTRAINT line is harder to partially omit. A-21 PASS. A-22 absent. Composite: 21/22. |
| V-04 | combined (A-21 inline + A-22) | V-01 + V-02: inline MUST-PRECEDE anchor ordering + `[Zone: X]` inline zone labels on all three positional artifacts. | Isolated positions: Sub-section 4 ordering vs. per-artifact zone labels in three artifact blocks. No positional conflict. A-21 + A-22 PASS. Composite: 22/22 = 100.0. |
| V-05 | full integration (A-21 dedicated block + A-22) | V-03 + V-02: dedicated SUB-SECTION-4-ANCHOR-SEQUENCE block + `[Zone: X]` inline zone labels. Maximum positional enforcement for both new criteria. | Dedicated block resists compression more than inline instructions. Combined with `[Zone: X]` labels, provides the strongest independently verifiable specification for A-21 and A-22 together. A-21 + A-22 PASS. Composite: 22/22 = 100.0. |

---

## V-01 -- Correctness: Sub-section 4 Anchor Ordering (Inline MUST-PRECEDE)

**axis:** correctness (Sub-section 4 anchor ordering -- inline MUST-PRECEDE approach)
**hypothesis:** V-05/R9 passes A-01 through A-20 but uses sequential "after X, produce Y"
language in Sub-section 4 without an explicit prohibition on interceding content. A-21
requires that when COST-FRAME CONCLUSION: (A-18), NET-COST-COMPARISON: block (A-10), and
FLAT-CASE-PRESSURE: line (C-01) co-occur in Sub-section 4, they appear in fixed linear
order with NO other content between adjacent anchor pairs. V-01/R10 adds: (1) a numbered
three-anchor sequence rule at the top of Sub-section 4 with MUST-PRECEDE gates, (2)
"immediately after" precision on the COST-FRAME CONCLUSION to NET-COST-COMPARISON transition,
and (3) an explicit "NO other content between the NET-COST-COMPARISON block and FLAT-CASE-PRESSURE:"
prohibition. Prose zone designators inherited unchanged from V-05/R9 -- A-22 not targeted.
Expected: A-21 PASS; A-22 absent. Composite under v9: 21/22 aspirationally.

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.roles/` before writing anything.
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

DO produce a labeled `STRUCTURING-COST FRAME:` block immediately before Sub-section 1.
MUST name both error risks:
- Over-structuring risk: principal risk of introducing structure prematurely, with >= 1
  concrete consequence (e.g., "decision overhead added before coordination failure rate
  justifies the cost")
- Under-coordination risk: principal risk of staying flat too long, with >= 1 concrete
  consequence (e.g., "competing roadmap commitments shipped to the same customer without
  a tie-break forum")
DO NOT merge this block with Sub-section 1. DO NOT omit.
Canonical zone designator for this artifact: PRE-ASSESSMENT.

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
class, or responsibility area with no current owner under the flat structure. Label it
`UNCOVERED:` or equivalent. REQUIRED: additive to -- and MUST NOT replace -- the named failure.
Canonical zone designator for this artifact: SUB-SECTION-3.

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
Canonical zone designator for this artifact: POST-VERDICT-BRANCH.

DO NOT proceed past VERDICT until: COST-FRAME CONCLUSION + NET-COST-COMPARISON (with
ADDITIVE-TO guard) + FLAT-CASE-PRESSURE + verdict declaration + re-assessment trigger
are all written in the mandatory anchor order.

INTEGRATION-NOTE -- POSITIONAL DISJOINTNESS CONFIRMATION

DO produce a labeled `INTEGRATION-NOTE:` block immediately after Sub-section 4 (after
re-assessment trigger and any CAN-OPERATE-FLAT branch content) and BEFORE the ASCII org
diagram. This block applies when all three positional aspirational artifacts are present.

REQUIRED format:
```
INTEGRATION-NOTE:
- STRUCTURING-COST FRAME (PRE-ASSESSMENT): positioned before Sub-section 1
- UNCOVERED: citation (SUB-SECTION-3): positioned within Sub-section 3
- Flat Operating Rhythm (POST-VERDICT-BRANCH): positioned after Sub-section 4, CAN-OPERATE-FLAT branch only
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
4. STRUCTURING-COST FRAME (PRE-ASSESSMENT block, before Sub-section 1)
5. Sub-section 1 (mechanism table with Mechanism Type diversity floor + FLAT-CASE-CLOSED with type-diversity count)
6. Sub-section 2: How We Coordinate Today
7. Sub-section 3: Rebuttal (with UNCOVERED: citation)
8. Sub-section 4: VERDICT (mandatory anchor order: COST-FRAME CONCLUSION + NET-COST-COMPARISON with ADDITIVE-TO guard + FLAT-CASE-PRESSURE + verdict + re-assessment trigger + Flat Operating Rhythm if applicable)
9. INTEGRATION-NOTE (after Sub-section 4, before org diagram)
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

## V-02 -- Output Format: Per-Artifact Inline Zone Labels

**axis:** output format (per-artifact inline zone labels)
**hypothesis:** V-05/R9 passes A-01 through A-20 but uses prose notes for zone designators:
"Canonical zone designator for this artifact: PRE-ASSESSMENT." A-22 requires that each
positional artifact (A-14, A-15, A-16) carries its canonical zone designator as an INLINE
LABEL using the bracketed format `[Zone: PRE-ASSESSMENT]`, `[Zone: SUB-SECTION-3]`,
`[Zone: POST-VERDICT-BRANCH]` -- matching the A-20 canonical designators exactly -- inside
the artifact's own instruction block. V-02/R10 replaces the three prose notes with `[Zone: X]`
inline labels in the correct format inside each artifact block. Sub-section 4 anchor ordering
instructions inherited unchanged from V-05/R9 -- A-21 not targeted. The INTEGRATION-NOTE
format also updated to use `[Zone: X]` labels in the listing, consistent with the
per-artifact labels. Expected: A-22 PASS; A-21 absent. Composite under v9: 21/22 aspirationally.

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.roles/` before writing anything.
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
  concrete consequence
- Under-coordination risk: principal risk of staying flat too long, with >= 1 concrete
  consequence
DO NOT merge this block with Sub-section 1. DO NOT omit.

**Sub-section 1 -- Case for Staying Flat**

DO produce a mechanism evidence table with exactly four columns:
`Mechanism Name | Mechanism Type | Frequency / Participants | Estimated Coordination Cost`
The `Mechanism Type` column MUST use only values from this closed set:
`Channel / Informal Role / Recurring Cadence / Shared Artifact`
DO NOT use values outside this vocabulary.
Floor is >= 2 data rows. Floor MUST include at least two distinct Mechanism Type category
values. Two rows of the same Mechanism Type value do NOT together satisfy the floor.
DO populate Estimated Coordination Cost with a numeric estimate per mechanism.

After the table, perform two counts:
(1) Data row count -- verify >= 2.
(2) Distinct Mechanism Type category count.
Substitute N (rows) and K (categories), emit exactly:
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded; {K} of 4 type classes represented. How We Coordinate Today begins.] ---`
DO NOT EMIT before: row count >= 2 AND distinct categories >= 2.
DO NOT begin Sub-section 2 until separator is present.

**Sub-section 2 -- How We Coordinate Today**

DO inventory coordination patterns. DO NOT re-list Sub-section 1 entries.

**Sub-section 3 -- Rebuttal**

DO name the coordination failure the flat case cannot handle. DO reference a specific
observable. DO NOT use vague failure modes.

DO include an `UNCOVERED:` citation block naming at least one ownerless function or decision
class. `[Zone: SUB-SECTION-3]`
Label it `UNCOVERED:` or equivalent. REQUIRED: additive to -- and MUST NOT replace -- the
named coordination failure.

**Sub-section 4 -- VERDICT and Re-assessment Trigger**

MUST produce `COST-FRAME CONCLUSION:` as the FIRST line of Sub-section 4, before all other
content. This line MUST:
(1) Name the `STRUCTURING-COST FRAME:` block by its label as the source of the evaluation frame
(2) Cite the dominant error risk by name (over-structuring or under-coordination)
(3) Name at least one of Sub-sections 1, 2, or 3 as the evidence source that elevated that risk

DO NOT emit any other Sub-section 4 content before `COST-FRAME CONCLUSION:` is written.

After `COST-FRAME CONCLUSION:`, produce the NET-COST-COMPARISON block:

```
NET-COST-COMPARISON:
  Flat coordination cost: [total from Sub-section 1, in stated units]
  Structure overhead: [meeting load + charter maintenance + escalation delay]
  Net delta: [flat cost minus structure overhead = signed value]
  ADDITIVE-TO: C-01 FLAT-CASE-PRESSURE
```

The `ADDITIVE-TO: C-01 FLAT-CASE-PRESSURE` guard MUST appear as a labeled line inside the
NET-COST-COMPARISON block. DO NOT place it outside the block.
REQUIRED: guard line present inside the block before proceeding.
This block does NOT replace FLAT-CASE-PRESSURE.

After NET-COST-COMPARISON, emit:
`FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
Rating from closed set: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`
DO NOT omit. The arithmetic block does not discharge this requirement.

Choose exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
Reasoning MUST reference the FLAT-CASE-PRESSURE rating.
Verdict MUST be linked to the NET-COST-COMPARISON net delta sign.
DO write a concrete re-assessment trigger. DO NOT write "revisit as the team grows."

If verdict is `CAN-OPERATE-FLAT`: produce a Flat Operating Rhythm block immediately after the
re-assessment trigger. At minimum two rows: one recurring alignment cadence and one
decision-escalation mechanism available under flat structure. Label: "Flat Operating Rhythm."
`[Zone: POST-VERDICT-BRANCH]`

DO NOT proceed past VERDICT until: COST-FRAME CONCLUSION + NET-COST-COMPARISON (with
ADDITIVE-TO guard) + FLAT-CASE-PRESSURE + verdict declaration + re-assessment trigger
are all written.

INTEGRATION-NOTE -- POSITIONAL DISJOINTNESS CONFIRMATION

DO produce a labeled `INTEGRATION-NOTE:` block immediately after Sub-section 4 (after
re-assessment trigger and any CAN-OPERATE-FLAT branch content) and BEFORE the ASCII org
diagram. Applies when all three positional aspirational artifacts are present.

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
If verdict is `STRUCTURE-WARRANTED`: note N/A for POST-VERDICT-BRANCH; confirm disjointness
for the two remaining artifacts.

DO emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
DO NOT draw any org boxes until this gate is present (after INTEGRATION-NOTE).

ASCII ORG DIAGRAM

DO draw ASCII hierarchy using box-drawing characters. At minimum two hierarchy levels.
DO show committees as distinct labeled nodes. DO use ROLES-LOADED names only.

DO emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA -- DECIDES / ESCALATES REQUIRED

Columns: `Area | Headcount | Key Roles | Decides | Escalates` -- both required.
Annotate Key Roles as `[role name] ([domain type])`.
At minimum two area rows plus a `**Total**` row.

OPERATING RHYTHM TABLE

Columns: `Cadence | Frequency | DRI / Owner | Purpose`
At minimum three rows: one ROB, one shiproom or gate, one governance meeting.

COMMITTEE CHARTERS -- FIVE FIELDS REQUIRED

Charter per governance meeting. All five: Purpose, Membership, Decides, Escalates, Quorum.
Annotate Membership as `[role name] ([domain type])`. At minimum two roles.
Quorum REQUIRED: `[N] of [M] member roles required for binding decisions`

DO emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER -- MUST PRECEDE ORG EVOLUTION ROADMAP

MUST produce as a named, physically distinct section. DO NOT embed elsewhere. DO NOT skip.
Populate cat-1 through cat-4 before proceeding. (Category schema and format same as V-01.)

ORG EVOLUTION ROADMAP -- REQUIRED

After ORG-ELEMENT REGISTER. At minimum two rows. Row 1: headcount threshold. Row 2: different category.

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

Each "Why It Applies Here" cell: `[element name] (cat-N) -- [one sentence]`. At minimum two rows.

SECTION ORDER -- same as V-01 (19 sections in sequence).

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-03 -- Correctness: Dedicated SUB-SECTION-4-ANCHOR-SEQUENCE Block

**axis:** correctness (Sub-section 4 anchor ordering -- dedicated block approach)
**hypothesis:** V-01/R10 adds inline MUST-PRECEDE gates distributed across the Sub-section 4
instructions. Under model compression, inline ordering directives can be selectively omitted
because no single instruction enforces the full three-anchor sequence as a unit. A-21 requires
the ordering to be independently verifiable -- a reviewer can confirm the chain without parsing
narrative semantics. V-03/R10 replaces the distributed inline ordering language with a dedicated
labeled `SUB-SECTION-4-ANCHOR-SEQUENCE:` block that lists the three anchors as an ordered
numbered sequence and adds a single explicit CONSTRAINT line prohibiting interceding content
between any adjacent anchor pair. This consolidates the three ordering requirements into one
independently verifiable structural rule. Prose zone designators inherited unchanged from
V-05/R9 -- A-22 not targeted. Expected: A-21 PASS; A-22 absent. Composite under v9: 21/22.

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.roles/` before writing anything.
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

DO produce a labeled `STRUCTURING-COST FRAME:` block immediately before Sub-section 1.
MUST name both error risks:
- Over-structuring risk: principal risk of introducing structure prematurely, with >= 1
  concrete consequence
- Under-coordination risk: principal risk of staying flat too long, with >= 1 concrete
  consequence
DO NOT merge this block with Sub-section 1. DO NOT omit.
Canonical zone designator for this artifact: PRE-ASSESSMENT.

**Sub-section 1 -- Case for Staying Flat**

DO produce a mechanism evidence table with exactly four columns:
`Mechanism Name | Mechanism Type | Frequency / Participants | Estimated Coordination Cost`
The `Mechanism Type` column MUST use only values from this closed set:
`Channel / Informal Role / Recurring Cadence / Shared Artifact`
Floor is >= 2 data rows. Floor MUST include at least two distinct Mechanism Type category values.
DO populate Estimated Coordination Cost per mechanism.

After the table, perform two counts:
(1) Data row count -- verify >= 2.
(2) Distinct Mechanism Type category count.
Substitute N and K, emit exactly:
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded; {K} of 4 type classes represented. How We Coordinate Today begins.] ---`
DO NOT EMIT before: row count >= 2 AND distinct categories >= 2.

**Sub-section 2 -- How We Coordinate Today**

DO inventory coordination patterns. DO NOT re-list Sub-section 1 entries.

**Sub-section 3 -- Rebuttal**

DO name the specific coordination failure. DO reference a specific observable.

DO include an `UNCOVERED:` citation naming at least one ownerless function or decision class.
Label it `UNCOVERED:` or equivalent. Additive to -- MUST NOT replace -- the named failure.
Canonical zone designator for this artifact: SUB-SECTION-3.

**Sub-section 4 -- VERDICT and Re-assessment Trigger**

SUB-SECTION-4-ANCHOR-SEQUENCE:
  Order 1: `COST-FRAME CONCLUSION:` line (write first; must precede all other Sub-section 4 content)
  Order 2: `NET-COST-COMPARISON:` block (write second; must immediately follow Order 1)
  Order 3: `FLAT-CASE-PRESSURE:` line (write third; must immediately follow Order 2 closing)
  CONSTRAINT: NO other content -- prose, labels, blank lines with content, or other blocks --
    may be inserted between Order 1 and Order 2, or between Order 2 and Order 3.

MUST produce `COST-FRAME CONCLUSION:` as the FIRST line of Sub-section 4 (see
SUB-SECTION-4-ANCHOR-SEQUENCE above). This line MUST:
(1) Name the `STRUCTURING-COST FRAME:` block by its label
(2) Cite the dominant error risk by name (over-structuring or under-coordination)
(3) Name at least one sub-section as the evidence source

Immediately after `COST-FRAME CONCLUSION:` (following the SUB-SECTION-4-ANCHOR-SEQUENCE CONSTRAINT),
produce the NET-COST-COMPARISON block:

```
NET-COST-COMPARISON:
  Flat coordination cost: [total from Sub-section 1, in stated units]
  Structure overhead: [meeting load + charter maintenance + escalation delay]
  Net delta: [flat cost minus structure overhead = signed value]
  ADDITIVE-TO: C-01 FLAT-CASE-PRESSURE
```

The `ADDITIVE-TO: C-01 FLAT-CASE-PRESSURE` guard MUST appear as a labeled line inside the block.
DO NOT place it outside the block. This block does NOT replace FLAT-CASE-PRESSURE.

Immediately after the NET-COST-COMPARISON block closes (following the SUB-SECTION-4-ANCHOR-SEQUENCE
CONSTRAINT), emit:
`FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification]`
Rating from closed set: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`
DO NOT omit. The arithmetic block does not discharge this requirement.

Choose exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
Reasoning MUST reference FLAT-CASE-PRESSURE rating. Verdict linked to net delta sign.
DO write a concrete re-assessment trigger.

If verdict is `CAN-OPERATE-FLAT`: produce Flat Operating Rhythm block immediately after
re-assessment trigger. At minimum two rows: one alignment cadence + one decision-escalation
mechanism. Label: "Flat Operating Rhythm."
Canonical zone designator for this artifact: POST-VERDICT-BRANCH.

DO NOT proceed past VERDICT until: COST-FRAME CONCLUSION + NET-COST-COMPARISON (with
ADDITIVE-TO guard) + FLAT-CASE-PRESSURE + verdict declaration + re-assessment trigger
are all written in the SUB-SECTION-4-ANCHOR-SEQUENCE mandatory order.

INTEGRATION-NOTE -- POSITIONAL DISJOINTNESS CONFIRMATION

DO produce a labeled `INTEGRATION-NOTE:` block immediately after Sub-section 4 and BEFORE
the ASCII org diagram. Applies when all three positional artifacts are present.

REQUIRED format:
```
INTEGRATION-NOTE:
- STRUCTURING-COST FRAME (PRE-ASSESSMENT): positioned before Sub-section 1
- UNCOVERED: citation (SUB-SECTION-3): positioned within Sub-section 3
- Flat Operating Rhythm (POST-VERDICT-BRANCH): positioned after Sub-section 4, CAN-OPERATE-FLAT branch only
Positional disjointness confirmed: each artifact assigned to exactly one zone; no zone shared.
```

DO NOT omit when all three positional artifacts are present.
If verdict is `STRUCTURE-WARRANTED`: note N/A for POST-VERDICT-BRANCH; confirm disjointness
for the two remaining artifacts.

DO emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
DO NOT draw any org boxes until this gate is present (after INTEGRATION-NOTE).

ASCII ORG DIAGRAM

DO draw ASCII hierarchy using box-drawing characters. At minimum two levels.
DO show committees as distinct labeled nodes. DO use ROLES-LOADED names only.

DO emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA -- DECIDES / ESCALATES REQUIRED

Columns: `Area | Headcount | Key Roles | Decides | Escalates` -- both required.
Annotate Key Roles as `[role name] ([domain type])`. At minimum two area rows plus `**Total**`.

OPERATING RHYTHM TABLE

Columns: `Cadence | Frequency | DRI / Owner | Purpose`
At minimum three rows: one ROB, one shiproom or gate, one governance meeting.

COMMITTEE CHARTERS -- FIVE FIELDS REQUIRED

Charter per governance meeting. All five: Purpose, Membership, Decides, Escalates, Quorum.
Annotate Membership as `[role name] ([domain type])`. At minimum two roles.
Quorum: `[N] of [M] member roles required for binding decisions`

DO emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER -- MUST PRECEDE ORG EVOLUTION ROADMAP

MUST produce as named, physically distinct section. DO NOT embed elsewhere. DO NOT skip.
Populate cat-1 through cat-4 before proceeding. (Category schema same as V-01.)

ORG EVOLUTION ROADMAP -- REQUIRED

After ORG-ELEMENT REGISTER. At minimum two rows. Row 1: headcount threshold. Row 2: different.

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

Each "Why It Applies Here" cell: `[element name] (cat-N) -- [one sentence]`. At minimum two rows.

SECTION ORDER -- same as V-01 (19 sections in sequence).

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-04 -- Combined: Anchor Ordering (Inline MUST-PRECEDE) + Inline Zone Labels

**axis:** combined correctness + output format (A-21 inline approach + A-22)
**hypothesis:** V-01/R10 and V-02/R10 each test one new criterion in isolation. V-04/R10
combines both: (1) Sub-section 4 anchor ordering with inline MUST-PRECEDE gates and explicit
NO-interceding-content prohibition on each adjacent anchor pair (A-21), and (2) `[Zone: X]`
inline zone labels replacing prose "Canonical zone designator" notes inside each of the three
positional artifact blocks (A-22). The two changes target structurally isolated positions:
Sub-section 4 ordering constraints vs. per-artifact labels in the A-14/A-15/A-16 instruction
blocks. No positional conflict. Expected: A-21 + A-22 PASS. Composite under v9: 22/22 = 100.0.

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.roles/` before writing anything.
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
  concrete consequence
- Under-coordination risk: principal risk of staying flat too long, with >= 1 concrete
  consequence
DO NOT merge this block with Sub-section 1. DO NOT omit.

**Sub-section 1 -- Case for Staying Flat**

DO produce a mechanism evidence table with exactly four columns:
`Mechanism Name | Mechanism Type | Frequency / Participants | Estimated Coordination Cost`
The `Mechanism Type` column MUST use only values from this closed set:
`Channel / Informal Role / Recurring Cadence / Shared Artifact`
DO NOT use values outside this vocabulary.
Floor is >= 2 data rows. Floor MUST include at least two distinct Mechanism Type category
values. Two rows of the same type do NOT satisfy the floor.
DO populate Estimated Coordination Cost per mechanism.

After the table, perform two counts:
(1) Data row count -- verify >= 2.
(2) Distinct Mechanism Type category count.
Substitute N (rows) and K (categories), emit exactly:
`--- [FLAT-CASE-CLOSED: {N} mechanism rows recorded; {K} of 4 type classes represented. How We Coordinate Today begins.] ---`
DO NOT EMIT before: row count >= 2 AND distinct categories >= 2.

**Sub-section 2 -- How We Coordinate Today**

DO inventory coordination patterns. DO NOT re-list Sub-section 1 entries.

**Sub-section 3 -- Rebuttal**

DO name the specific coordination failure. DO reference a specific observable.

DO include an `UNCOVERED:` citation block naming at least one ownerless function or decision class.
`[Zone: SUB-SECTION-3]`
Label it `UNCOVERED:` or equivalent. Additive to -- MUST NOT replace -- the named failure.

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
(1) Name the `STRUCTURING-COST FRAME:` block by its label
(2) Cite the dominant error risk by name (over-structuring or under-coordination)
(3) Name at least one sub-section as the evidence source

Immediately after `COST-FRAME CONCLUSION:` (NO interceding content -- see anchor ordering above),
produce the NET-COST-COMPARISON block:

```
NET-COST-COMPARISON:
  Flat coordination cost: [total from Sub-section 1, in stated units]
  Structure overhead: [meeting load + charter maintenance + escalation delay]
  Net delta: [flat cost minus structure overhead = signed value]
  ADDITIVE-TO: C-01 FLAT-CASE-PRESSURE
```

The `ADDITIVE-TO: C-01 FLAT-CASE-PRESSURE` guard MUST appear as a labeled line inside the block.
DO NOT place it outside the block. This block does NOT replace FLAT-CASE-PRESSURE.

Immediately after the NET-COST-COMPARISON block closes (NO interceding content -- see anchor
ordering above), emit:
`FLAT-CASE-PRESSURE: [rating] -- [one-sentence justification citing Sub-section 1 mechanism count and Sub-section 3 failure mode]`
Rating from closed set: `Strong (5) / Moderate (4) / Weak (3) / Negligible (2) / Insufficient (1)`
DO NOT omit. The arithmetic block does not discharge this requirement.

Choose exactly one of: `CAN-OPERATE-FLAT` or `STRUCTURE-WARRANTED`.
Reasoning MUST reference FLAT-CASE-PRESSURE rating. Verdict linked to net delta sign.
DO write a concrete re-assessment trigger. DO NOT write "revisit as the team grows."

If verdict is `CAN-OPERATE-FLAT`: produce a Flat Operating Rhythm block immediately after the
re-assessment trigger. At minimum two rows: one alignment cadence + one decision-escalation
mechanism. Label: "Flat Operating Rhythm."
`[Zone: POST-VERDICT-BRANCH]`

DO NOT proceed past VERDICT until: COST-FRAME CONCLUSION + NET-COST-COMPARISON (with
ADDITIVE-TO guard) + FLAT-CASE-PRESSURE + verdict declaration + re-assessment trigger
are all written in the mandatory anchor order.

INTEGRATION-NOTE -- POSITIONAL DISJOINTNESS CONFIRMATION

DO produce a labeled `INTEGRATION-NOTE:` block immediately after Sub-section 4 and BEFORE
the ASCII org diagram. Applies when all three positional artifacts are present.

REQUIRED format:
```
INTEGRATION-NOTE:
- STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT]: positioned before Sub-section 1
- UNCOVERED: citation [Zone: SUB-SECTION-3]: positioned within Sub-section 3
- Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH]: positioned after Sub-section 4, CAN-OPERATE-FLAT branch only
Positional disjointness confirmed: each artifact assigned to exactly one zone; no zone shared.
```

DO NOT omit when all three positional artifacts are present.
If verdict is `STRUCTURE-WARRANTED`: note N/A for POST-VERDICT-BRANCH; confirm disjointness
for the two remaining artifacts.

DO emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
DO NOT draw any org boxes until this gate is present (after INTEGRATION-NOTE).

ASCII ORG DIAGRAM

DO draw ASCII hierarchy using box-drawing characters. At minimum two levels.
DO show committees as distinct labeled nodes. DO use ROLES-LOADED names only.

DO emit: `=== [PHASE GATE: STRUCTURE COMPLETE -- HEADCOUNT AND RHYTHM BEGIN] ===`

HEADCOUNT BY AREA -- DECIDES / ESCALATES REQUIRED

Columns: `Area | Headcount | Key Roles | Decides | Escalates` -- both required.
Annotate Key Roles as `[role name] ([domain type])`. At minimum two area rows plus `**Total**`.

OPERATING RHYTHM TABLE

Columns: `Cadence | Frequency | DRI / Owner | Purpose`
At minimum three rows: one ROB, one shiproom or gate, one governance meeting.

COMMITTEE CHARTERS -- FIVE FIELDS REQUIRED

Charter per governance meeting. All five: Purpose, Membership, Decides, Escalates, Quorum.
Annotate Membership as `[role name] ([domain type])`. At minimum two roles.
Quorum: `[N] of [M] member roles required for binding decisions`

DO emit: `=== [PHASE GATE: CHARTERS COMPLETE -- REGISTER AND ANALYSIS BEGIN] ===`

ORG-ELEMENT REGISTER -- MUST PRECEDE ORG EVOLUTION ROADMAP

MUST produce as named, physically distinct section. DO NOT embed elsewhere. DO NOT skip.
Populate cat-1 through cat-4 before proceeding. (Category schema same as V-01.)

ORG EVOLUTION ROADMAP -- REQUIRED

After ORG-ELEMENT REGISTER. At minimum two rows. Row 1: headcount threshold. Row 2: different.

ANTI-PATTERN WATCH -- TYPED CITATIONS REQUIRED

Each "Why It Applies Here" cell: `[element name] (cat-N) -- [one sentence]`. At minimum two rows.

SECTION ORDER -- same as V-01 (19 sections in sequence).

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-05 -- Full Integration: Dedicated Anchor Block + Inline Zone Labels

**axis:** full integration (dedicated SUB-SECTION-4-ANCHOR-SEQUENCE block + per-artifact inline zone labels)
**hypothesis:** V-04/R10 combines A-21 (inline MUST-PRECEDE) + A-22. V-05/R10 replaces the
inline MUST-PRECEDE approach with the V-03 dedicated `SUB-SECTION-4-ANCHOR-SEQUENCE:` block,
which consolidates the three ordering requirements into a single labeled, independently
verifiable constraint. The hypothesis: a dedicated block with an explicit CONSTRAINT line
is harder to partially omit under model compression than inline ordering directives distributed
across several Sub-section 4 instructions. V-05/R10 combines: (1) the dedicated
`SUB-SECTION-4-ANCHOR-SEQUENCE:` block (V-03's A-21 approach) and (2) `[Zone: X]` inline
labels on all three positional artifacts (V-02/V-04's A-22 approach). This is the maximum
structural enforcement formulation for both new v9 criteria.
Expected: A-21 + A-22 PASS. Composite under v9: 22/22 = 100.0.

---

You are running `/org-chart {topic}`.

ROLES -- READ FIRST

DO check `.roles/` before writing anything.
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
DO write a concrete re-assessment trigger naming a threshold. DO NOT write "revisit as the team grows."

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

DO NOT proceed to Org Evolution Roadmap until cat-1 through cat-4 are each populated.

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
5. Sub-section 1 (mechanism table with Mechanism Type diversity floor + FLAT-CASE-CLOSED with type-diversity count)
6. Sub-section 2: How We Coordinate Today
7. Sub-section 3: Rebuttal (with UNCOVERED: citation [Zone: SUB-SECTION-3])
8. Sub-section 4: VERDICT (SUB-SECTION-4-ANCHOR-SEQUENCE order: COST-FRAME CONCLUSION + NET-COST-COMPARISON with ADDITIVE-TO guard + FLAT-CASE-PRESSURE + verdict + re-assessment trigger + Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH] if applicable)
9. INTEGRATION-NOTE (after Sub-section 4, before org diagram)
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
