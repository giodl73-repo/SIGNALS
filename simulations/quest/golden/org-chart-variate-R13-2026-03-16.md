---
skill: quest-variate
skill_target: org-chart
date: 2026-03-16
round: R13
rubric_version: v12
status: variate
---

# org-chart Variate -- Round 13

**Date:** 2026-03-16
**Skill:** org-chart
**Rubric:** v12 (A-01 through A-30; A-28/A-29/A-30 new from R12)
**Round:** R13 -- single-axis (V-01/V-02/V-03) + combined (V-04/V-05)

**R12 ceiling under v12:**
V-05/R12 achieves 30/30 aspirationally under rubric v12 (composite 100.0).
A-28 is satisfied via numbered `CROSS-REF-REQUIRED (1 of 2)` / `(2 of 2)` pair with
cardinality preamble. A-29 is satisfied via enumerated `ZONE-NOTATION RULE:` block with
one numbered prohibited form per line. A-30 is satisfied via self-contained VERDICT-GATE
checklist items 2 and 4 carrying inline `[ANCHOR-ORDER CONSTRAINT: ...]` restatements.

**R13 target:** 30/30 aspirationally with new compression resistance gains beyond A-28/A-29/A-30.
Three structural gaps remain in V-05/R12 not yet captured by any criterion:

1. **ROLE-LOAD-ORDER embedding gap:** The classification tier-sequence constraint ("Engineering
   first, Operations second, PM/Design/Research/Other third") is embedded as a single DO clause
   inside the ROLE-TYPE-CLASSIFICATION block header. Under compression, the "classify by type"
   directive survives but the specific three-tier sequence and inter-tier ordering prohibition
   may be simplified away. No structural gap exists when the constraint is elided -- the
   ROLE-TYPE-CLASSIFICATION block is still present, just without guaranteed tier order. A named
   `ROLE-LOAD-ORDER:` block before ROLE-TYPE-CLASSIFICATION makes the sequence constraint a
   structurally distinct, independently detectable section: its absence creates a visible gap.

2. **Quorum denominator semantic gap:** V-05/R12 requires `[N] of [M] member roles required
   for binding decisions` format. The format directive is present but M is not semantically
   bound to the Membership field count -- a model can emit `2 of 5` without verifying that 5
   equals the number of roles listed in Membership. The N and M slots are syntactically required
   but semantically unconstrained. Adding an explicit pre-write count instruction that binds M
   to the Membership role count and requires an inline `[QUORUM-COUNT: ...]` verification line
   makes the denominator semantically anchored, not just syntactically present.

3. **Zone-label definition-site traceability gap:** V-05/R12 requires INTEGRATION-NOTE entries
   to use `[Zone: X]` bracket format matching the inline labels at artifact definition sites
   (enforced by A-26 ZONE-NOTATION RULE and A-29 enumerated prohibition list). But the
   match requirement is stated as a rule ("MUST match... same bracket format, same designator
   string") without a production-time verification step. A model can satisfy A-26/A-29 by using
   bracket notation while still mis-matching a designator string (e.g., `[Zone: PRE-ASSESS]`
   vs `[Zone: PRE-ASSESSMENT]`). A post-INTEGRATION-NOTE traceability check requiring explicit
   `ZONE-TRACE-CONFIRMED:` lines for each artifact enforces the match at production time.

**Three questions drive R13:**

1. Does a named `ROLE-LOAD-ORDER:` block (V-01) -- a pure-imperative tier-sequence section
   placed between ROLES-LOADED and ROLE-TYPE-CLASSIFICATION, with the constraint removed from
   ROLE-TYPE-CLASSIFICATION's header text -- make the three-tier ordering independently
   detectable as a structural gap rather than an embedded clause? (V-01)

2. Does a `QUORUM-DENOMINATOR CONSTRAINT:` block (V-02) -- requiring an explicit Membership
   role count before each Quorum line and a `[QUORUM-COUNT: M=N]` verification inline --
   make M semantically bound to the Membership field rather than syntactically free? (V-02)

3. Does a `ZONE-LABEL-TRACEABILITY` verification step (V-03) -- requiring one
   `ZONE-TRACE-CONFIRMED:` line per INTEGRATION-NOTE artifact entry, each stating the
   INTEGRATION-NOTE designator and the definition-site designator side-by-side -- make the
   bracket-form match independently verifiable at production time? (V-03)

V-04/R13 combines V-01 (ROLE-LOAD-ORDER block) + V-02 (Quorum denominator binding) on V-05/R12 base.
V-05/R13 is full integration: V-05/R12 base + all three improvements together.

---

## Round 13 Variation Map

| V | Axis | What Changes vs V-05/R12 | Hypothesis |
|---|------|--------------------------|------------|
| V-01 | role sequence | Extract three-tier ordering constraint from ROLE-TYPE-CLASSIFICATION header into a named `ROLE-LOAD-ORDER:` block placed between ROLES-LOADED and ROLE-TYPE-CLASSIFICATION; remove the embedded clause from ROLE-TYPE-CLASSIFICATION. | Embedded tier-sequence clause is one DO among many and survives compression only as "classify by type." Named block makes absence structurally detectable. Expected: A-31 PASS. All others unchanged from V-05/R12. Composite: 30/30. |
| V-02 | output format | Add `QUORUM-DENOMINATOR CONSTRAINT:` block inside COMMITTEE CHARTERS, requiring pre-write Membership count, binding M to that count, and requiring `[QUORUM-COUNT: Membership roles listed = M; minimum binding quorum = N of M]` verification line per charter. | Quorum denominator M is syntactically required but semantically free in V-05/R12. Explicit count-then-bind instruction makes M semantically anchored. Expected: A-32 PASS. All others unchanged. Composite: 30/30. |
| V-03 | lifecycle emphasis | Add `ZONE-LABEL-TRACEABILITY` verification step after INTEGRATION-NOTE, requiring one `ZONE-TRACE-CONFIRMED:` line per artifact entry naming the INTEGRATION-NOTE designator and definition-site designator side-by-side; gate the INERTIA COMPLETE phase gate on all ZONE-TRACE-CONFIRMED lines being present. | Zone-label match rule exists (A-26/A-29) but no production-time verification step. Inline traceability confirmation makes designation-string match detectable before the phase gate passes. Expected: A-33 PASS. All others unchanged. Composite: 30/30. |
| V-04 | combined | V-05/R12 base + V-01 (ROLE-LOAD-ORDER block) + V-02 (Quorum denominator binding). | Both improvements operate at structurally isolated positions (roles phase vs charters phase). No interaction surface. Expected: 30/30. |
| V-05 | full integration | V-05/R12 base + V-01 (ROLE-LOAD-ORDER) + V-02 (Quorum denominator) + V-03 (zone-label traceability). | Maximum per-element compression resistance: A-31 via named block, A-32 via count-bind-verify, A-33 via side-by-side traceability confirmation before phase gate. Expected: 30/30, maximum robustness across A-31/A-32/A-33 cluster. |

---

## V-01 -- Role Sequence: Named ROLE-LOAD-ORDER Block

**axis:** role sequence (three-tier classification order extracted from ROLE-TYPE-CLASSIFICATION
header text into a named `ROLE-LOAD-ORDER:` block placed between ROLES-LOADED and
ROLE-TYPE-CLASSIFICATION)
**hypothesis:** V-05/R12 satisfies the tier-ordering requirement via the clause "DO classify in
three-tier order: Engineering first, Operations second, PM/Design/Research/Other third" embedded
inside the ROLE-TYPE-CLASSIFICATION block header. This clause is one of many DO directives;
under compression it may survive only as "classify by type" without preserving the specific
three-tier sequence or the inter-tier ordering prohibition ("DO NOT interleave tiers"). The
structural gap is invisible: the ROLE-TYPE-CLASSIFICATION block is still present, so no section
is missing -- only the ordering constraint within it is potentially elided. V-01/R13 extracts
the tier-sequence constraint into a named `ROLE-LOAD-ORDER:` block placed immediately before
ROLE-TYPE-CLASSIFICATION, containing only a pure-imperative ordered list of tiers (no motivation
sentence). Absence of this block is structurally detectable. ROLE-TYPE-CLASSIFICATION references
it by name. All other criteria unchanged from V-05/R12. Expected: A-01 through A-30 all PASS.
Composite: 30/30.

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

CROSS-REF-REQUIRED PAIR -- TWO INSTANCES REQUIRED IN SUB-SECTION 4:
Exactly two `CROSS-REF-REQUIRED:` lines must appear in Sub-section 4: one at the
CONCLUSION->COMPARISON transition and one at the COMPARISON->PRESSURE transition.
Both must be present. A single instance does not satisfy this requirement.
CARDINALITY DECLARATION: this pair has exactly 2 members; the (1 of 2) instance and the
(2 of 2) instance are both required; emitting only (1 of 2) leaves the declared set incomplete.

After writing `COST-FRAME CONCLUSION:`, emit the following standalone declaration on its own line
before producing any other content:
`CROSS-REF-REQUIRED (1 of 2): NO interceding content between COST-FRAME CONCLUSION: and NET-COST-COMPARISON: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

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
`CROSS-REF-REQUIRED (2 of 2): NO interceding content between NET-COST-COMPARISON: close and FLAT-CASE-PRESSURE: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

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
  [ ] (2) CROSS-REF-REQUIRED (1 of 2): written on its own line immediately after COST-FRAME CONCLUSION:
          [ANCHOR-ORDER CONSTRAINT: Order 1 (COST-FRAME CONCLUSION:) MUST immediately precede
          Order 2 (NET-COST-COMPARISON:) with NO interceding content -- verify adjacency now,
          independent of the SUB-SECTION-4-ANCHOR-SEQUENCE declaration]
  [ ] (3) NET-COST-COMPARISON: block written immediately after CROSS-REF-REQUIRED (1 of 2), with ADDITIVE-TO guard inside
  [ ] (4) CROSS-REF-REQUIRED (2 of 2): written on its own line immediately after NET-COST-COMPARISON: closes
          [ANCHOR-ORDER CONSTRAINT: Order 2 (NET-COST-COMPARISON:) MUST immediately precede
          Order 3 (FLAT-CASE-PRESSURE:) with NO interceding content -- verify adjacency now,
          independent of the SUB-SECTION-4-ANCHOR-SEQUENCE declaration]
  [ ] (5) FLAT-CASE-PRESSURE: written immediately after CROSS-REF-REQUIRED (2 of 2), with valid closed-set rating
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

ZONE-NOTATION RULE:
REQUIRED: Each artifact entry in INTEGRATION-NOTE MUST use `[Zone: X]` bracket format --
the same bracket form used at each artifact's definition site inline label.
PROHIBITED forms -- each of the following is a rule violation requiring correction:
  (1) `(PRE-ASSESSMENT)` -- prohibited; use `[Zone: PRE-ASSESSMENT]` instead
  (2) `(SUB-SECTION-3)` -- prohibited; use `[Zone: SUB-SECTION-3]` instead
  (3) `(POST-VERDICT-BRANCH)` -- prohibited; use `[Zone: POST-VERDICT-BRANCH]` instead
The `[Zone: X]` notation in INTEGRATION-NOTE MUST match the inline `[Zone: X]` labels at the
artifact definition sites exactly -- same bracket format, same designator string.
DO NOT use any parenthetical zone designator form anywhere in the document.

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
2. ROLE-LOAD-ORDER sequence constraint applied (Tier 1 Engineering, Tier 2 Operations, Tier 3 PM/Design/Research/Other)
3. ROLE-TYPE-CLASSIFICATION (following ROLE-LOAD-ORDER)
4. Phase gate: ROLES COMPLETE
5. STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT] (before Sub-section 1)
6. Sub-section 1 (mechanism table + FLAT-CASE-CLOSED with type-diversity count)
7. Sub-section 2: How We Coordinate Today
8. Sub-section 3: Rebuttal (with UNCOVERED: citation [Zone: SUB-SECTION-3])
9. Sub-section 4: VERDICT (SUB-SECTION-4-ANCHOR-SEQUENCE mandatory order: COST-FRAME CONCLUSION + CROSS-REF-REQUIRED (1 of 2) + NET-COST-COMPARISON with ADDITIVE-TO guard + CROSS-REF-REQUIRED (2 of 2) + FLAT-CASE-PRESSURE + verdict + re-assessment trigger + VERDICT-GATE CHECKLIST + Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH] if applicable)
10. INTEGRATION-NOTE with [Zone: X] bracket notation + ZONE-NOTATION RULE enumerated block (after Sub-section 4, before org diagram)
11. Phase gate: INERTIA COMPLETE
12. ASCII Org Diagram
13. Phase gate: STRUCTURE COMPLETE
14. Headcount by Area
15. Operating Rhythm Table
16. Committee Charters
17. Phase gate: CHARTERS COMPLETE
18. ORG-ELEMENT REGISTER
19. Org Evolution Roadmap
20. Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-02 -- Output Format: Quorum Denominator Membership Binding

**axis:** output format (QUORUM-DENOMINATOR CONSTRAINT block requiring pre-write Membership count,
M bound to that count, and inline `[QUORUM-COUNT: ...]` verification line per charter)
**hypothesis:** V-05/R12 satisfies the Quorum format requirement via "Quorum REQUIRED format:
`[N] of [M] member roles required for binding decisions`" and "DO NOT use a bare percentage or
short N-only form." This enforces syntactic structure (two slot values, prescribed phrase) but
M is semantically unconstrained -- a model can emit `2 of 5 member roles required` without
verifying that 5 equals the count of roles listed in the Membership field. Under compression,
the model may substitute plausible-looking integers without performing a Membership count. V-02/R13
adds a `QUORUM-DENOMINATOR CONSTRAINT:` block inside COMMITTEE CHARTERS requiring an explicit
pre-write count instruction (count Membership roles, that count is M), binding M to that count,
and requiring a `[QUORUM-COUNT: Membership roles listed = M; minimum binding quorum = N of M]`
verification line immediately before each Quorum line. Each charter's denominator is now
semantically anchored and independently verifiable. All other criteria unchanged from V-05/R12.
Expected: A-01 through A-30 all PASS. Composite: 30/30.

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

CROSS-REF-REQUIRED PAIR -- TWO INSTANCES REQUIRED IN SUB-SECTION 4:
Exactly two `CROSS-REF-REQUIRED:` lines must appear in Sub-section 4: one at the
CONCLUSION->COMPARISON transition and one at the COMPARISON->PRESSURE transition.
Both must be present. A single instance does not satisfy this requirement.
CARDINALITY DECLARATION: this pair has exactly 2 members; the (1 of 2) instance and the
(2 of 2) instance are both required; emitting only (1 of 2) leaves the declared set incomplete.

After writing `COST-FRAME CONCLUSION:`, emit the following standalone declaration on its own line
before producing any other content:
`CROSS-REF-REQUIRED (1 of 2): NO interceding content between COST-FRAME CONCLUSION: and NET-COST-COMPARISON: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

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
`CROSS-REF-REQUIRED (2 of 2): NO interceding content between NET-COST-COMPARISON: close and FLAT-CASE-PRESSURE: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

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
  [ ] (2) CROSS-REF-REQUIRED (1 of 2): written on its own line immediately after COST-FRAME CONCLUSION:
          [ANCHOR-ORDER CONSTRAINT: Order 1 (COST-FRAME CONCLUSION:) MUST immediately precede
          Order 2 (NET-COST-COMPARISON:) with NO interceding content -- verify adjacency now,
          independent of the SUB-SECTION-4-ANCHOR-SEQUENCE declaration]
  [ ] (3) NET-COST-COMPARISON: block written immediately after CROSS-REF-REQUIRED (1 of 2), with ADDITIVE-TO guard inside
  [ ] (4) CROSS-REF-REQUIRED (2 of 2): written on its own line immediately after NET-COST-COMPARISON: closes
          [ANCHOR-ORDER CONSTRAINT: Order 2 (NET-COST-COMPARISON:) MUST immediately precede
          Order 3 (FLAT-CASE-PRESSURE:) with NO interceding content -- verify adjacency now,
          independent of the SUB-SECTION-4-ANCHOR-SEQUENCE declaration]
  [ ] (5) FLAT-CASE-PRESSURE: written immediately after CROSS-REF-REQUIRED (2 of 2), with valid closed-set rating
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

ZONE-NOTATION RULE:
REQUIRED: Each artifact entry in INTEGRATION-NOTE MUST use `[Zone: X]` bracket format --
the same bracket form used at each artifact's definition site inline label.
PROHIBITED forms -- each of the following is a rule violation requiring correction:
  (1) `(PRE-ASSESSMENT)` -- prohibited; use `[Zone: PRE-ASSESSMENT]` instead
  (2) `(SUB-SECTION-3)` -- prohibited; use `[Zone: SUB-SECTION-3]` instead
  (3) `(POST-VERDICT-BRANCH)` -- prohibited; use `[Zone: POST-VERDICT-BRANCH]` instead
The `[Zone: X]` notation in INTEGRATION-NOTE MUST match the inline `[Zone: X]` labels at the
artifact definition sites exactly -- same bracket format, same designator string.
DO NOT use any parenthetical zone designator form anywhere in the document.

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

QUORUM-DENOMINATOR CONSTRAINT -- REQUIRED BEFORE EACH QUORUM LINE:
Before writing the Quorum line for each charter, perform this three-step count:
  (1) Count the number of distinct roles listed in this charter's Membership field. That count is M.
  (2) Choose N as the minimum count of those roles required for a binding decision (N < M).
  (3) Emit the verification inline on its own line:
      `[QUORUM-COUNT: Membership roles listed = [M]; minimum binding quorum = [N] of [M]]`
  (4) Then emit the Quorum line: `Quorum: [N] of [M] member roles required for binding decisions`
      where N and M are the specific integers determined in steps 1 and 2.
DO NOT write M without first counting Membership roles.
DO NOT emit a Quorum line where M does not equal the Membership count from step 1.
DO NOT omit the [QUORUM-COUNT: ...] verification line for any charter.

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
8. Sub-section 4: VERDICT (SUB-SECTION-4-ANCHOR-SEQUENCE mandatory order: COST-FRAME CONCLUSION + CROSS-REF-REQUIRED (1 of 2) + NET-COST-COMPARISON with ADDITIVE-TO guard + CROSS-REF-REQUIRED (2 of 2) + FLAT-CASE-PRESSURE + verdict + re-assessment trigger + VERDICT-GATE CHECKLIST + Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH] if applicable)
9. INTEGRATION-NOTE with [Zone: X] bracket notation + ZONE-NOTATION RULE enumerated block (after Sub-section 4, before org diagram)
10. Phase gate: INERTIA COMPLETE
11. ASCII Org Diagram
12. Phase gate: STRUCTURE COMPLETE
13. Headcount by Area
14. Operating Rhythm Table
15. Committee Charters (with QUORUM-DENOMINATOR CONSTRAINT per charter: [QUORUM-COUNT: ...] line before each Quorum line)
16. Phase gate: CHARTERS COMPLETE
17. ORG-ELEMENT REGISTER
18. Org Evolution Roadmap
19. Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-03 -- Lifecycle Emphasis: Zone-Label Definition-Site Traceability

**axis:** lifecycle emphasis (post-INTEGRATION-NOTE traceability step requiring one
`ZONE-TRACE-CONFIRMED:` line per artifact entry, each stating the INTEGRATION-NOTE designator
and definition-site designator side-by-side; INERTIA COMPLETE phase gate gated on all
ZONE-TRACE-CONFIRMED lines being present)
**hypothesis:** V-05/R12 satisfies A-26/A-29 (enumerated ZONE-NOTATION RULE prohibition) and
requires the bracket notation in INTEGRATION-NOTE to "match the inline `[Zone: X]` labels at
the artifact definition sites exactly -- same bracket format, same designator string." This is
a stated rule but has no production-time verification step. A model can satisfy the rule
syntactically by using bracket notation while still mis-matching a designator string (e.g.,
`[Zone: PRE-ASSESS]` instead of `[Zone: PRE-ASSESSMENT]`; `[Zone: SUBSECTION-3]` instead of
`[Zone: SUB-SECTION-3]`). The ZONE-NOTATION RULE enforcement catches parenthetical forms but
does not catch bracket-form designation-string mismatches. V-03/R13 adds a
`ZONE-LABEL-TRACEABILITY` verification step immediately after INTEGRATION-NOTE: for each
artifact entry, one `ZONE-TRACE-CONFIRMED:` line naming the INTEGRATION-NOTE designator and
the definition-site designator side-by-side, with an explicit match/mismatch verdict. The
INERTIA COMPLETE phase gate is gated on all ZONE-TRACE-CONFIRMED lines being present.
Expected: A-01 through A-30 all PASS. Composite: 30/30.

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

CROSS-REF-REQUIRED PAIR -- TWO INSTANCES REQUIRED IN SUB-SECTION 4:
Exactly two `CROSS-REF-REQUIRED:` lines must appear in Sub-section 4: one at the
CONCLUSION->COMPARISON transition and one at the COMPARISON->PRESSURE transition.
Both must be present. A single instance does not satisfy this requirement.
CARDINALITY DECLARATION: this pair has exactly 2 members; the (1 of 2) instance and the
(2 of 2) instance are both required; emitting only (1 of 2) leaves the declared set incomplete.

After writing `COST-FRAME CONCLUSION:`, emit the following standalone declaration on its own line
before producing any other content:
`CROSS-REF-REQUIRED (1 of 2): NO interceding content between COST-FRAME CONCLUSION: and NET-COST-COMPARISON: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

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
`CROSS-REF-REQUIRED (2 of 2): NO interceding content between NET-COST-COMPARISON: close and FLAT-CASE-PRESSURE: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

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
  [ ] (2) CROSS-REF-REQUIRED (1 of 2): written on its own line immediately after COST-FRAME CONCLUSION:
          [ANCHOR-ORDER CONSTRAINT: Order 1 (COST-FRAME CONCLUSION:) MUST immediately precede
          Order 2 (NET-COST-COMPARISON:) with NO interceding content -- verify adjacency now,
          independent of the SUB-SECTION-4-ANCHOR-SEQUENCE declaration]
  [ ] (3) NET-COST-COMPARISON: block written immediately after CROSS-REF-REQUIRED (1 of 2), with ADDITIVE-TO guard inside
  [ ] (4) CROSS-REF-REQUIRED (2 of 2): written on its own line immediately after NET-COST-COMPARISON: closes
          [ANCHOR-ORDER CONSTRAINT: Order 2 (NET-COST-COMPARISON:) MUST immediately precede
          Order 3 (FLAT-CASE-PRESSURE:) with NO interceding content -- verify adjacency now,
          independent of the SUB-SECTION-4-ANCHOR-SEQUENCE declaration]
  [ ] (5) FLAT-CASE-PRESSURE: written immediately after CROSS-REF-REQUIRED (2 of 2), with valid closed-set rating
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

ZONE-NOTATION RULE:
REQUIRED: Each artifact entry in INTEGRATION-NOTE MUST use `[Zone: X]` bracket format --
the same bracket form used at each artifact's definition site inline label.
PROHIBITED forms -- each of the following is a rule violation requiring correction:
  (1) `(PRE-ASSESSMENT)` -- prohibited; use `[Zone: PRE-ASSESSMENT]` instead
  (2) `(SUB-SECTION-3)` -- prohibited; use `[Zone: SUB-SECTION-3]` instead
  (3) `(POST-VERDICT-BRANCH)` -- prohibited; use `[Zone: POST-VERDICT-BRANCH]` instead
The `[Zone: X]` notation in INTEGRATION-NOTE MUST match the inline `[Zone: X]` labels at the
artifact definition sites exactly -- same bracket format, same designator string.
DO NOT use any parenthetical zone designator form anywhere in the document.

DO NOT omit when all three positional artifacts are present.
DO NOT place before Sub-section 4 or after the ASCII org diagram.
If verdict is `STRUCTURE-WARRANTED` (Flat Operating Rhythm absent): note N/A for the
POST-VERDICT-BRANCH entry and confirm disjointness for the two remaining artifacts.

ZONE-LABEL-TRACEABILITY -- REQUIRED IMMEDIATELY AFTER INTEGRATION-NOTE:
After writing the INTEGRATION-NOTE block, perform a definition-site cross-check for each
artifact entry. For each artifact in INTEGRATION-NOTE:
  (1) Locate the inline `[Zone: X]` label at the artifact's definition site in the document above.
  (2) Compare the designator string used in INTEGRATION-NOTE with the designator string at the definition site.
  (3) Emit one line per artifact:
      `ZONE-TRACE-CONFIRMED: [artifact name] -- INTEGRATION-NOTE: [Zone: X]; definition site: [Zone: X]; designator strings match.`
      OR, if strings differ:
      `ZONE-TRACE-MISMATCH: [artifact name] -- INTEGRATION-NOTE: [Zone: X]; definition site: [Zone: Y]; CORRECT the INTEGRATION-NOTE entry before proceeding.`
DO NOT omit a ZONE-TRACE-CONFIRMED or ZONE-TRACE-MISMATCH line for any artifact entry.
DO NOT emit the INERTIA COMPLETE phase gate until all artifact traceability lines are present and
no ZONE-TRACE-MISMATCH lines remain unresolved.
If verdict is `STRUCTURE-WARRANTED`: emit ZONE-TRACE-CONFIRMED for the two present artifacts only;
emit `ZONE-TRACE-N/A: Flat Operating Rhythm -- POST-VERDICT-BRANCH absent (STRUCTURE-WARRANTED).`

DO emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
DO NOT draw any org boxes until this gate is present (after INTEGRATION-NOTE and
all ZONE-TRACE-CONFIRMED lines).

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
8. Sub-section 4: VERDICT (SUB-SECTION-4-ANCHOR-SEQUENCE mandatory order: COST-FRAME CONCLUSION + CROSS-REF-REQUIRED (1 of 2) + NET-COST-COMPARISON with ADDITIVE-TO guard + CROSS-REF-REQUIRED (2 of 2) + FLAT-CASE-PRESSURE + verdict + re-assessment trigger + VERDICT-GATE CHECKLIST + Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH] if applicable)
9. INTEGRATION-NOTE with [Zone: X] bracket notation + ZONE-NOTATION RULE enumerated block (after Sub-section 4, before org diagram)
10. ZONE-LABEL-TRACEABILITY: one ZONE-TRACE-CONFIRMED line per artifact, gating the INERTIA COMPLETE phase gate
11. Phase gate: INERTIA COMPLETE
12. ASCII Org Diagram
13. Phase gate: STRUCTURE COMPLETE
14. Headcount by Area
15. Operating Rhythm Table
16. Committee Charters
17. Phase gate: CHARTERS COMPLETE
18. ORG-ELEMENT REGISTER
19. Org Evolution Roadmap
20. Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-04 -- Combined: ROLE-LOAD-ORDER Block + Quorum Denominator Binding

**axis:** combined role sequence + output format (V-05/R12 base + V-01/R13 ROLE-LOAD-ORDER
named block + V-02/R13 QUORUM-DENOMINATOR CONSTRAINT with membership-count binding)
**hypothesis:** V-01/R13 closes the tier-sequence structural gap by making ROLE-LOAD-ORDER a
named section whose absence is detectable. V-02/R13 closes the denominator semantic gap by
binding M to the Membership count via an explicit count-then-verify instruction. Both
improvements operate at structurally isolated positions (roles phase vs charters phase) with
no shared directive surface or interaction. V-03/R13 (zone-label traceability) is not included
-- V-04 targets A-31 and A-32 simultaneously while holding A-33 at V-05/R12 levels.
Expected: A-01 through A-30 all PASS. Composite: 30/30. Maximum robustness for A-31/A-32 cluster.

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

CROSS-REF-REQUIRED PAIR -- TWO INSTANCES REQUIRED IN SUB-SECTION 4:
Exactly two `CROSS-REF-REQUIRED:` lines must appear in Sub-section 4: one at the
CONCLUSION->COMPARISON transition and one at the COMPARISON->PRESSURE transition.
Both must be present. A single instance does not satisfy this requirement.
CARDINALITY DECLARATION: this pair has exactly 2 members; the (1 of 2) instance and the
(2 of 2) instance are both required; emitting only (1 of 2) leaves the declared set incomplete.

After writing `COST-FRAME CONCLUSION:`, emit the following standalone declaration on its own line
before producing any other content:
`CROSS-REF-REQUIRED (1 of 2): NO interceding content between COST-FRAME CONCLUSION: and NET-COST-COMPARISON: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

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
`CROSS-REF-REQUIRED (2 of 2): NO interceding content between NET-COST-COMPARISON: close and FLAT-CASE-PRESSURE: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

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
  [ ] (2) CROSS-REF-REQUIRED (1 of 2): written on its own line immediately after COST-FRAME CONCLUSION:
          [ANCHOR-ORDER CONSTRAINT: Order 1 (COST-FRAME CONCLUSION:) MUST immediately precede
          Order 2 (NET-COST-COMPARISON:) with NO interceding content -- verify adjacency now,
          independent of the SUB-SECTION-4-ANCHOR-SEQUENCE declaration]
  [ ] (3) NET-COST-COMPARISON: block written immediately after CROSS-REF-REQUIRED (1 of 2), with ADDITIVE-TO guard inside
  [ ] (4) CROSS-REF-REQUIRED (2 of 2): written on its own line immediately after NET-COST-COMPARISON: closes
          [ANCHOR-ORDER CONSTRAINT: Order 2 (NET-COST-COMPARISON:) MUST immediately precede
          Order 3 (FLAT-CASE-PRESSURE:) with NO interceding content -- verify adjacency now,
          independent of the SUB-SECTION-4-ANCHOR-SEQUENCE declaration]
  [ ] (5) FLAT-CASE-PRESSURE: written immediately after CROSS-REF-REQUIRED (2 of 2), with valid closed-set rating
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

ZONE-NOTATION RULE:
REQUIRED: Each artifact entry in INTEGRATION-NOTE MUST use `[Zone: X]` bracket format --
the same bracket form used at each artifact's definition site inline label.
PROHIBITED forms -- each of the following is a rule violation requiring correction:
  (1) `(PRE-ASSESSMENT)` -- prohibited; use `[Zone: PRE-ASSESSMENT]` instead
  (2) `(SUB-SECTION-3)` -- prohibited; use `[Zone: SUB-SECTION-3]` instead
  (3) `(POST-VERDICT-BRANCH)` -- prohibited; use `[Zone: POST-VERDICT-BRANCH]` instead
The `[Zone: X]` notation in INTEGRATION-NOTE MUST match the inline `[Zone: X]` labels at the
artifact definition sites exactly -- same bracket format, same designator string.
DO NOT use any parenthetical zone designator form anywhere in the document.

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

QUORUM-DENOMINATOR CONSTRAINT -- REQUIRED BEFORE EACH QUORUM LINE:
Before writing the Quorum line for each charter, perform this three-step count:
  (1) Count the number of distinct roles listed in this charter's Membership field. That count is M.
  (2) Choose N as the minimum count of those roles required for a binding decision (N < M).
  (3) Emit the verification inline on its own line:
      `[QUORUM-COUNT: Membership roles listed = [M]; minimum binding quorum = [N] of [M]]`
  (4) Then emit the Quorum line: `Quorum: [N] of [M] member roles required for binding decisions`
      where N and M are the specific integers determined in steps 1 and 2.
DO NOT write M without first counting Membership roles.
DO NOT emit a Quorum line where M does not equal the Membership count from step 1.
DO NOT omit the [QUORUM-COUNT: ...] verification line for any charter.

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
2. ROLE-LOAD-ORDER sequence constraint applied (Tier 1 Engineering, Tier 2 Operations, Tier 3 PM/Design/Research/Other)
3. ROLE-TYPE-CLASSIFICATION (following ROLE-LOAD-ORDER)
4. Phase gate: ROLES COMPLETE
5. STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT] (before Sub-section 1)
6. Sub-section 1 (mechanism table + FLAT-CASE-CLOSED with type-diversity count)
7. Sub-section 2: How We Coordinate Today
8. Sub-section 3: Rebuttal (with UNCOVERED: citation [Zone: SUB-SECTION-3])
9. Sub-section 4: VERDICT (SUB-SECTION-4-ANCHOR-SEQUENCE mandatory order: COST-FRAME CONCLUSION + CROSS-REF-REQUIRED (1 of 2) + NET-COST-COMPARISON with ADDITIVE-TO guard + CROSS-REF-REQUIRED (2 of 2) + FLAT-CASE-PRESSURE + verdict + re-assessment trigger + VERDICT-GATE CHECKLIST + Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH] if applicable)
10. INTEGRATION-NOTE with [Zone: X] bracket notation + ZONE-NOTATION RULE enumerated block (after Sub-section 4, before org diagram)
11. Phase gate: INERTIA COMPLETE
12. ASCII Org Diagram
13. Phase gate: STRUCTURE COMPLETE
14. Headcount by Area
15. Operating Rhythm Table
16. Committee Charters (with QUORUM-DENOMINATOR CONSTRAINT per charter: [QUORUM-COUNT: ...] line before each Quorum line)
17. Phase gate: CHARTERS COMPLETE
18. ORG-ELEMENT REGISTER
19. Org Evolution Roadmap
20. Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} -- {date}`

---

## V-05 -- Full Integration: ROLE-LOAD-ORDER + Quorum Denominator + Zone-Label Traceability

**axis:** full integration (V-04/R13 + V-03/R13: named ROLE-LOAD-ORDER block + Quorum denominator
membership binding + ZONE-LABEL-TRACEABILITY post-INTEGRATION-NOTE verification step)
**hypothesis:** V-04/R13 provides maximum robustness for A-31 and A-32 through named block
extraction and count-bind-verify denominator binding. V-05/R13 adds the V-03/R13 zone-label
traceability improvement: a `ZONE-LABEL-TRACEABILITY` step immediately after INTEGRATION-NOTE
requiring one `ZONE-TRACE-CONFIRMED:` line per artifact, each stating the INTEGRATION-NOTE
designator and the definition-site designator side-by-side, gating the INERTIA COMPLETE phase
gate on all confirmations being present and mismatch-free. The total enforcement chain for
A-33: (1) ZONE-NOTATION RULE declares bracket format requirement and enumerated prohibitions
(A-26/A-29), (2) ZONE-LABEL-TRACEABILITY confirms at production time that designator strings
match the definition sites before the phase gate passes. Expected: A-01 through A-30 all PASS.
Composite: 30/30. Maximum compression resistance across A-31/A-32/A-33 cluster simultaneously.

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

CROSS-REF-REQUIRED PAIR -- TWO INSTANCES REQUIRED IN SUB-SECTION 4:
Exactly two `CROSS-REF-REQUIRED:` lines must appear in Sub-section 4: one at the
CONCLUSION->COMPARISON transition and one at the COMPARISON->PRESSURE transition.
Both must be present. A single instance does not satisfy this requirement.
CARDINALITY DECLARATION: this pair has exactly 2 members; the (1 of 2) instance and the
(2 of 2) instance are both required; emitting only (1 of 2) leaves the declared set incomplete.

After writing `COST-FRAME CONCLUSION:`, emit the following standalone declaration on its own line
before producing any other content:
`CROSS-REF-REQUIRED (1 of 2): NO interceding content between COST-FRAME CONCLUSION: and NET-COST-COMPARISON: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

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
`CROSS-REF-REQUIRED (2 of 2): NO interceding content between NET-COST-COMPARISON: close and FLAT-CASE-PRESSURE: -- see SUB-SECTION-4-ANCHOR-SEQUENCE above.`

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
  [ ] (2) CROSS-REF-REQUIRED (1 of 2): written on its own line immediately after COST-FRAME CONCLUSION:
          [ANCHOR-ORDER CONSTRAINT: Order 1 (COST-FRAME CONCLUSION:) MUST immediately precede
          Order 2 (NET-COST-COMPARISON:) with NO interceding content -- verify adjacency now,
          independent of the SUB-SECTION-4-ANCHOR-SEQUENCE declaration]
  [ ] (3) NET-COST-COMPARISON: block written immediately after CROSS-REF-REQUIRED (1 of 2), with ADDITIVE-TO guard inside
  [ ] (4) CROSS-REF-REQUIRED (2 of 2): written on its own line immediately after NET-COST-COMPARISON: closes
          [ANCHOR-ORDER CONSTRAINT: Order 2 (NET-COST-COMPARISON:) MUST immediately precede
          Order 3 (FLAT-CASE-PRESSURE:) with NO interceding content -- verify adjacency now,
          independent of the SUB-SECTION-4-ANCHOR-SEQUENCE declaration]
  [ ] (5) FLAT-CASE-PRESSURE: written immediately after CROSS-REF-REQUIRED (2 of 2), with valid closed-set rating
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

ZONE-NOTATION RULE:
REQUIRED: Each artifact entry in INTEGRATION-NOTE MUST use `[Zone: X]` bracket format --
the same bracket form used at each artifact's definition site inline label.
PROHIBITED forms -- each of the following is a rule violation requiring correction:
  (1) `(PRE-ASSESSMENT)` -- prohibited; use `[Zone: PRE-ASSESSMENT]` instead
  (2) `(SUB-SECTION-3)` -- prohibited; use `[Zone: SUB-SECTION-3]` instead
  (3) `(POST-VERDICT-BRANCH)` -- prohibited; use `[Zone: POST-VERDICT-BRANCH]` instead
The `[Zone: X]` notation in INTEGRATION-NOTE MUST match the inline `[Zone: X]` labels at the
artifact definition sites exactly -- same bracket format, same designator string.
DO NOT use any parenthetical zone designator form anywhere in the document.

DO NOT omit when all three positional artifacts are present.
DO NOT place before Sub-section 4 or after the ASCII org diagram.
If verdict is `STRUCTURE-WARRANTED` (Flat Operating Rhythm absent): note N/A for the
POST-VERDICT-BRANCH entry and confirm disjointness for the two remaining artifacts.

ZONE-LABEL-TRACEABILITY -- REQUIRED IMMEDIATELY AFTER INTEGRATION-NOTE:
After writing the INTEGRATION-NOTE block, perform a definition-site cross-check for each
artifact entry. For each artifact in INTEGRATION-NOTE:
  (1) Locate the inline `[Zone: X]` label at the artifact's definition site in the document above.
  (2) Compare the designator string used in INTEGRATION-NOTE with the designator string at the definition site.
  (3) Emit one line per artifact:
      `ZONE-TRACE-CONFIRMED: [artifact name] -- INTEGRATION-NOTE: [Zone: X]; definition site: [Zone: X]; designator strings match.`
      OR, if strings differ:
      `ZONE-TRACE-MISMATCH: [artifact name] -- INTEGRATION-NOTE: [Zone: X]; definition site: [Zone: Y]; CORRECT the INTEGRATION-NOTE entry before proceeding.`
DO NOT omit a ZONE-TRACE-CONFIRMED or ZONE-TRACE-MISMATCH line for any artifact entry.
DO NOT emit the INERTIA COMPLETE phase gate until all artifact traceability lines are present and
no ZONE-TRACE-MISMATCH lines remain unresolved.
If verdict is `STRUCTURE-WARRANTED`: emit ZONE-TRACE-CONFIRMED for the two present artifacts only;
emit `ZONE-TRACE-N/A: Flat Operating Rhythm -- POST-VERDICT-BRANCH absent (STRUCTURE-WARRANTED).`

DO emit: `=== [PHASE GATE: INERTIA COMPLETE -- STRUCTURE SECTION BEGINS] ===`
DO NOT draw any org boxes until this gate is present (after INTEGRATION-NOTE and
all ZONE-TRACE-CONFIRMED lines).

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

QUORUM-DENOMINATOR CONSTRAINT -- REQUIRED BEFORE EACH QUORUM LINE:
Before writing the Quorum line for each charter, perform this three-step count:
  (1) Count the number of distinct roles listed in this charter's Membership field. That count is M.
  (2) Choose N as the minimum count of those roles required for a binding decision (N < M).
  (3) Emit the verification inline on its own line:
      `[QUORUM-COUNT: Membership roles listed = [M]; minimum binding quorum = [N] of [M]]`
  (4) Then emit the Quorum line: `Quorum: [N] of [M] member roles required for binding decisions`
      where N and M are the specific integers determined in steps 1 and 2.
DO NOT write M without first counting Membership roles.
DO NOT emit a Quorum line where M does not equal the Membership count from step 1.
DO NOT omit the [QUORUM-COUNT: ...] verification line for any charter.

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
2. ROLE-LOAD-ORDER sequence constraint applied (Tier 1 Engineering, Tier 2 Operations, Tier 3 PM/Design/Research/Other)
3. ROLE-TYPE-CLASSIFICATION (following ROLE-LOAD-ORDER)
4. Phase gate: ROLES COMPLETE
5. STRUCTURING-COST FRAME [Zone: PRE-ASSESSMENT] (before Sub-section 1)
6. Sub-section 1 (mechanism table + FLAT-CASE-CLOSED with type-diversity count)
7. Sub-section 2: How We Coordinate Today
8. Sub-section 3: Rebuttal (with UNCOVERED: citation [Zone: SUB-SECTION-3])
9. Sub-section 4: VERDICT (SUB-SECTION-4-ANCHOR-SEQUENCE mandatory order: COST-FRAME CONCLUSION + CROSS-REF-REQUIRED (1 of 2) + NET-COST-COMPARISON with ADDITIVE-TO guard + CROSS-REF-REQUIRED (2 of 2) + FLAT-CASE-PRESSURE + verdict + re-assessment trigger + VERDICT-GATE CHECKLIST + Flat Operating Rhythm [Zone: POST-VERDICT-BRANCH] if applicable)
10. INTEGRATION-NOTE with [Zone: X] bracket notation + ZONE-NOTATION RULE enumerated block (after Sub-section 4, before org diagram)
11. ZONE-LABEL-TRACEABILITY: one ZONE-TRACE-CONFIRMED line per artifact, gating the INERTIA COMPLETE phase gate
12. Phase gate: INERTIA COMPLETE
13. ASCII Org Diagram
14. Phase gate: STRUCTURE COMPLETE
15. Headcount by Area
16. Operating Rhythm Table
17. Committee Charters (with QUORUM-DENOMINATOR CONSTRAINT per charter: [QUORUM-COUNT: ...] line before each Quorum line)
18. Phase gate: CHARTERS COMPLETE
19. ORG-ELEMENT REGISTER
20. Org Evolution Roadmap
21. Anti-Pattern Watch

End with exactly: `Generated by: /org-chart {topic} -- {date}`
