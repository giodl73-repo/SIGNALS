---
skill: quest-rubric
skill_target: quest-rubric
date: 2026-03-15
version: 10
round: R10
changes: Targets C-35 (competitor-defeat annotations co-located at mechanism introduction
  points and in the SV preamble, extending C-32/C-33 from structural declaration to
  provenance declaration) and C-36 (pre-phase skeleton formatted as operational tick-off
  checklist with live-construction tracking instruction, extending C-31 from
  declare-and-cross-reference to declare-track-and-cross-reference); both criteria added
  in rubric v10 from R9 excellence signals ES-R9-1 and ES-R9-2
---

# quest-rubric Variate -- v10, Round 10
**Date:** 2026-03-15
**Rubric:** v10 (adds C-35: competitor-defeat annotations at mechanism introduction points
and SV preamble; C-36: pre-phase skeleton as operational tick-off checklist with
live-construction tracking instruction)
**Target criteria:** C-35, C-36

**Round 10 against rubric v10 design note:** Rounds 1--9 produced mechanisms for C-01
through C-34. The two new criteria sharpen provenance and live-tracking requirements at
two structural positions:

**C-32/C-33 vs C-35.** C-32 requires the mechanism overview to declare the pre-phase
skeleton step's heading pattern. C-33 requires the SV preamble to declare both sources
and their failure classes. A rubric satisfies both with a mechanism set that is
structurally complete but not provenance-auditable. C-35 closes the provenance gap: each
MECHANISMS entry must name the competing protocol whose gap it closes; the SV preamble
must name at least one competing SV design with its failure class. Two rubrics with
identical mechanism sets differ on C-35 solely by presence or absence of competitor-defeat
annotations co-located at mechanism introduction points. Without provenance, the mechanism
set is verifiably complete but not auditable for minimality.

**C-31 vs C-36.** C-31 requires the skeleton to be declared pre-phase and
cross-referenced in SV. A rubric satisfies C-31 by producing a skeleton with correct
headings and cross-referencing it in the SV pass. C-36 requires a third, real-time
mechanism: `- [ ]` format plus an explicit "tick each checkbox as you construct the
corresponding section" instruction co-located in the skeleton step. A skeleton with
correct headings in prose or dash format, or missing the tick instruction, satisfies C-31
but fails C-36. The partially-ticked skeleton at Author Phase end names missed headings
before any SV scan begins -- a builder-commitment signal detectable independently of both
SV sources.

**Axis selection:**

Three axes map directly to the two new criteria:
- Inertia framing --> C-35: competitor-defeat annotations at mechanism introduction points
  and SV preamble
- Lifecycle emphasis --> C-36: pre-phase skeleton formatted as `- [ ]` with
  tick-during-construction instruction
- Output format --> C-35 partial + C-36 partial: structured table format forces a
  Competitor column; checklist format forces `- [ ]`

Single-axis variations: V-01 (inertia framing), V-02 (lifecycle emphasis), V-03 (output
format)
Combined variations: V-04 (inertia framing + lifecycle emphasis), V-05 (role sequence +
lifecycle emphasis)

---

## Round 10 Variation Map

| Variation | Axis | C-35 probe | C-36 probe | Notes |
|-----------|------|-----------|-----------|-------|
| V-01 | Inertia framing (competitor annotations at mechanism introduction + SV preamble) | Very strong -- Phase 3 requires COMPETITOR ANNOTATION block at each mechanism introduction naming the competing protocol and failure class; Phase 4 Emit requires a Competing Implementations Preamble section before Aspirational Criteria as the SV anchor table | None -- no skeleton format requirement; existing Phase 1 structure unchanged | Single-axis; tests whether competitor annotation requirements at both structural positions are sufficient for C-35 without format or lifecycle changes for C-36 |
| V-02 | Lifecycle emphasis (pre-phase skeleton as `- [ ]` with tick instruction) | None -- no competitor annotation requirement; Phase 3 standard structure | Very strong -- PRE-PHASE SKELETON step added before Phase 1; must use `- [ ]` format exactly; explicit "tick each checkbox as you complete the corresponding section" instruction co-located in the skeleton step | Single-axis; tests whether a dedicated lifecycle step with format and tracking instruction satisfies C-36 without the provenance annotation requirement for C-35 |
| V-03 | Output format (Aspirational Criteria table with Competitor column; `- [ ]` format specified at Emit) | Partial -- Aspirational Criteria table gains a "Competitor Defeated" column; format-level instruction without a dedicated structural step or STOP condition for missing values | Partial -- Phase 4 Emit specifies `- [ ]` format for the output skeleton section; no pre-phase skeleton step; no co-located tick instruction | Single-axis format; tests whether format-level column and checklist specifications alone satisfy C-35 and C-36 without dedicated lifecycle steps or explicit construction-tracking instructions |
| V-04 | Inertia framing + lifecycle emphasis (C-35 + C-36) | Very strong -- COMPETITOR ANNOTATION blocks at each mechanism introduction AND Competing Implementations Preamble before Aspirational Criteria; both structural positions required | Very strong -- PRE-PHASE SKELETON step before Phase 1 with `- [ ]` format and co-located tick instruction; skeleton updated at Emit | Combined; both target mechanisms present simultaneously; tests whether joint presence is additive or whether C-35 annotation depth degrades when C-36 skeleton step also consumes token budget |
| V-05 | Role sequence + lifecycle emphasis (C-35 via named prior role, C-36 via dedicated step) | Very strong -- dedicated PROVENANCE ANNOTATOR role runs after Phase 2 and before Phase 3; produces one register entry per mechanism naming competing protocol and failure class; register is Builder's binding input | Very strong -- dedicated SKELETON CONSTRUCTOR step runs before Phase 1; produces `- [ ]` checklist with tick instruction; skeleton is build manifest for entire rubric | Combined; C-35 via role separation (PROVENANCE ANNOTATOR before Builder); C-36 via dedicated lifecycle step before Phase 1; tests whether role separation produces deeper competitor content than V-01's inline annotation approach |

---

## V-01 -- Inertia Framing

**Axis:** Inertia framing -- how prominently the status-quo competitor is featured at
mechanism introduction points and whether the rubric's SV preamble declares competing
implementations with named failure classes.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will contain: (a) a COMPETITOR ANNOTATION block co-located at each aspirational mechanism's introduction point naming the specific competing protocol and its failure class, and (b) a Competing Implementations Preamble section in the output document positioned before the Aspirational Criteria section -- any body missing either position falsifies the respective C-35 half; the falsification signals are an aspirational criterion with a COMPETITOR block that omits the failure class, or a preamble table that names competing approaches generically without specific failure classes. | Requiring competitor annotations at both mechanism introduction points AND the SV preamble creates a two-tier structure: detailed per-mechanism annotations at construction time, and a higher-level preamble summary at emit time; the preamble forces the builder to aggregate competitor content across all mechanisms, which may surface naming inconsistencies that the per-mechanism annotations missed; generated rubrics under V-01 should show tighter naming consistency (same protocol referenced by the same name in both positions) than V-03 (which has a single column without aggregation). | V-04 is the primary comparison site -- V-01 has competitor annotations and SV preamble; V-04 adds the skeleton step; if V-04's competitor content shows no degradation vs V-01, the skeleton step consumes no annotation budget and the combined prompt is a Pareto improvement. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function
for quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### PHASE 1 -- FAILURE MODE ANALYSIS

Read the skill spec. For every way an output of this skill can fail, record:

```
F-NN | failure behavior | structural gap: what the skill omitted | blocking / suboptimal / cosmetic
```

Minimum: 3 blocking entries, 2 suboptimal entries. Do not begin Phase 2 until at least 5
entries are logged. A blocking failure makes the output non-functional. A suboptimal
failure makes the output less useful. A cosmetic failure affects presentation only.

---

### PHASE 2 -- ESSENTIAL AND RECOMMENDED CRITERIA

Draft essential criteria (3--5) from blocking failure modes. Draft recommended criteria
(2--3) from suboptimal failure modes. Use sequential C-NN numbering across both tiers.

Each criterion requires five fields:

- **ID**: C-NN
- **Text**: one sentence stating what must be true in a passing output
- **Weight**: essential | recommended
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence naming an observable anchor -- a count, a
  named pattern, a specific artifact field, or a presence/absence gate. No "is clear",
  "adequately covers", or equivalent bare qualifiers without a measurable anchor alongside.

Recommended criteria: the pass condition must test degree, precision, or specificity --
not whether a field is present. A recommended criterion whose pass condition reduces to
"the field exists" is a STOP condition -- rewrite as essential or remove.

---

### PHASE 3 -- ASPIRATIONAL CRITERIA

For each aspirational mechanism, write the COMPETITOR ANNOTATION block before stating the
mechanism. Follow this structure exactly:

```
COMPETITOR ANNOTATION -- M-NN:
Competing protocol: [Name the specific existing approach -- a named tool, protocol, or
framework -- that performs this mechanism's surface function. What does it do? Why does
it appear to satisfy the gap but fail to close it? State the specific failure class the
competing approach leaves open. Be specific enough that a reader can identify any
instantiation of this wrong approach without reading the required mechanism below.]

Failure class left open by [competing protocol name]: [one sentence]

REQUIRED MECHANISM -- M-NN: [State the mechanism that closes the gap. The positive
definition must be derivable from the COMPETITOR ANNOTATION above.]
```

After the COMPETITOR ANNOTATION --> REQUIRED MECHANISM pair, write the aspirational
criterion that the mechanism closes. The criterion Text field must reference the mechanism
by operative substance. The criterion Notes field must state which competing protocol it
supersedes and the failure class closed.

Assign M-IDs sequentially (M-01, M-02...).

STOP conditions for Phase 3:
- An aspirational criterion written before its COMPETITOR ANNOTATION block: rewrite.
- A COMPETITOR ANNOTATION that names the competing protocol but omits the failure class:
  rewrite.
- A REQUIRED MECHANISM whose content could not be inferred from the COMPETITOR ANNOTATION
  alone (the competitor block was underspecified): rewrite the competitor block until it
  supports derivation.

---

### PHASE 4 -- EMIT

Output the complete rubric document with sections in this order:

1. **Failure Mode Log** -- all F-NN entries from Phase 1
2. **Design Rationale** -- dominant failure mode, self-application, >= 3 rejected generic
   criteria with reasons; must appear before the first criteria table
3. **Competing Implementations Preamble** -- before the Aspirational Criteria section,
   list every competing approach surfaced in Phase 3 annotations:
   ```
   | Competing protocol | Failure class left open | Mechanism that closes it |
   ```
   This table is the SV anchor. An evaluator scanning only the Competing Implementations
   Preamble must be able to: (a) name the competing approach for every mechanism, (b)
   name its failure class, and (c) identify which M-NN closes each gap -- without reading
   the Aspirational Criteria section. Every COMPETITOR ANNOTATION in Phase 3 must have
   exactly one row in this table.
4. **Essential Criteria** -- all five fields per criterion
5. **Recommended Criteria** -- all five fields per criterion
6. **Aspirational Criteria** -- COMPETITOR ANNOTATION blocks inline immediately before the
   criterion each closes; do not move competitor blocks to a separate section
7. **Scoring** -- composite formula, golden threshold, PARTIAL handling
8. **Notes** -- `**Version**: N`, growth trigger, banned qualifier list, N/A scope blocks
9. **vN Candidates** -- patterns approaching promotion; evidence needed per candidate

The Competing Implementations Preamble must appear before the Aspirational Criteria
section. A reader of the Preamble must find no generic competitor entries -- every row
names a specific protocol and a specific failure class.

---

## V-02 -- Lifecycle Emphasis

**Axis:** Lifecycle emphasis -- a dedicated PRE-PHASE SKELETON step is added before Phase
1, producing a `- [ ]` checklist of all expected output headings with an explicit
tick-during-construction instruction co-located in the skeleton step.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will begin with a PRE-PHASE SKELETON section containing `- [ ]` checkbox bullets for each expected output heading AND an explicit instruction reading "tick each checkbox as you complete the corresponding section" -- any body where the skeleton uses `- ` prose bullets or dashes instead of `- [ ]`, or where the tick instruction is absent or appears in a different phase, falsifies the C-36 hypothesis; the falsification signal is a skeleton section with correct heading content but wrong bullet format, or a tick instruction that appears in Phase 4 Emit rather than co-located with the skeleton step. | A `- [ ]` skeleton with an explicit tick instruction commits the builder to construction state tracking before any output content is written -- a partially-ticked skeleton at Phase 4 entry names missed sections before any SV scan begins, creating a builder-commitment signal independent of the post-production audit; generated rubrics under V-02 should show lower section-completion drift (sections listed in skeleton but absent from output) than V-03, which specifies `- [ ]` format in the Emit section without a pre-phase skeleton step or co-located tick instruction. | V-03 is the primary comparison site for C-36 -- V-02 has a dedicated lifecycle step before Phase 1; V-03 has a format-level specification at Emit; if V-02-generated rubrics show higher section-completion fidelity, the pre-phase position and co-located tick instruction are the load-bearing mechanisms. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function
for quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### PRE-PHASE SKELETON

Before beginning Phase 1, write the output skeleton -- the complete list of sections the
finished rubric document will contain. Use this format exactly:

```
OUTPUT SKELETON:
- [ ] Failure Mode Log
- [ ] Design Rationale
- [ ] Essential Criteria
- [ ] Recommended Criteria
- [ ] Aspirational Criteria
- [ ] Scoring
- [ ] Notes
- [ ] vN Candidates
```

**Tick each checkbox as you complete the corresponding section during Phase 4 Emit. A
section not yet written remains unchecked. Do not mark a section complete until it is
fully written.**

If the skill being evaluated requires additional output sections (for example: a phase
architecture table, a mechanism map, a competitor register), add them to the skeleton
before Phase 1. Each added section requires a `- [ ]` entry. Do not begin Phase 1 until
the skeleton is finalized.

STOP CONDITION: A skeleton entry that uses `- ` (dash-space) rather than `- [ ] ` is
not a tracked section -- rewrite as `- [ ]` before proceeding.

---

### PHASE 1 -- FAILURE MODE ANALYSIS

Read the skill spec. For every way an output of this skill can fail, record:

```
F-NN | failure behavior | structural gap: what the skill omitted | blocking / suboptimal / cosmetic
```

Minimum: 3 blocking entries, 2 suboptimal entries. Do not begin Phase 2 until at least 5
entries are logged.

---

### PHASE 2 -- ESSENTIAL AND RECOMMENDED CRITERIA

Draft essential criteria (3--5) from blocking failure modes. Draft recommended criteria
(2--3) from suboptimal failure modes. Sequential C-NN numbering.

Each criterion requires five fields:

- **ID**: C-NN
- **Text**: one sentence -- what must be true in a passing output
- **Weight**: essential | recommended
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: observable anchor only; no bare qualifiers

Recommended pass conditions must test degree or specificity, not presence.

---

### PHASE 3 -- ASPIRATIONAL CRITERIA

For each aspirational criterion:
1. Name the structural gap it closes (one sentence: what passes
   essential+recommended but falls short of excellence here).
2. Name the mechanism that closes the gap (one sentence).
3. Write the five-field criterion. Text must reference the mechanism's operative
   substance. Notes must state: "mechanism: M-NN -- [mechanism description]."

Assign M-IDs sequentially (M-01, M-02...).

STOP conditions:
- An aspirational criterion without a named mechanism: rewrite.
- A mechanism that overlaps with an existing mechanism: merge or split before
  writing the criterion.

---

### PHASE 4 -- EMIT

Return to the PRE-PHASE SKELETON. Tick each checkbox as you write the corresponding
section.

Output the complete rubric document in this order:

1. **Failure Mode Log**
2. **Design Rationale** -- before the first criteria table
3. **Essential Criteria**
4. **Recommended Criteria**
5. **Aspirational Criteria**
6. **Scoring**
7. **Notes** -- `**Version**: N`, growth trigger, banned qualifiers
8. **vN Candidates**

At the end of Phase 4, review the PRE-PHASE SKELETON. Every checkbox must be ticked. If
any checkbox is unticked, the corresponding section is missing -- write it before
submitting the rubric.

---

## V-03 -- Output Format

**Axis:** Output format -- the Aspirational Criteria table requires a "Competitor
Defeated" column for each mechanism; the Phase 4 Emit section specifies `- [ ]` format
for the Output Skeleton section in the emitted document. Both C-35 and C-36 are probed
via format-level instructions without dedicated lifecycle steps or STOP conditions.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will contain: (a) an Aspirational Criteria table with a "Competitor Defeated" column populated for each criterion, and (b) an Output Skeleton section in the emitted document formatted as `- [ ]` checkbox bullets -- any body whose Aspirational Criteria table lacks the column, or whose Output Skeleton uses `- ` prose bullets, falsifies the respective hypothesis half; the falsification signals are a missing column or a skeleton section with dash bullets. | Format-level instructions without dedicated lifecycle enforcement produce shallower compliance: the "Competitor Defeated" column may be present but populated with generic descriptions ("prior approaches") rather than named protocols with specific failure classes; the `- [ ]` skeleton may appear in the output document without a co-located tick instruction (which is not specified in V-03), satisfying format but not the construction-tracking intent of C-36; generated rubrics under V-03 should be distinguishable from V-01 and V-02 by content depth (named protocol + failure class present in V-01 but not necessarily in V-03; tick instruction co-located in V-02 but not necessarily in V-03). | V-01 is the primary comparison site for C-35 (column annotation vs inline annotation block with STOP condition); V-02 is the primary comparison site for C-36 (Emit-time skeleton specification vs pre-phase skeleton step with co-located tick instruction). |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function
for quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### PHASE 1 -- FAILURE MODE ANALYSIS

Read the skill spec. For every way an output of this skill can fail, record:

```
F-NN | failure behavior | structural gap: what the skill omitted | blocking / suboptimal / cosmetic
```

Minimum: 3 blocking entries, 2 suboptimal entries. Do not begin Phase 2 until at least 5
entries are logged.

---

### PHASE 2 -- ESSENTIAL AND RECOMMENDED CRITERIA

Draft essential criteria (3--5) from blocking failure modes. Draft recommended criteria
(2--3) from suboptimal failure modes. Sequential C-NN numbering.

Each criterion requires five fields:

- **ID**: C-NN
- **Text**: one sentence -- what must be true in a passing output
- **Weight**: essential | recommended
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: observable anchor only; no bare qualifiers

---

### PHASE 3 -- ASPIRATIONAL CRITERIA

For each aspirational criterion, write the entry using this seven-field format:

```
| Field             | Value |
|-------------------|-------|
| ID                | C-NN  |
| Text              | [one sentence: what must be true in a passing output] |
| Weight            | aspirational |
| Category          | correctness / depth / format / coverage / behavior |
| Pass condition    | [observable anchor] |
| Mechanism         | M-NN: [one sentence: structural element closing the gap] |
| Competitor Defeated | [Name the specific existing approach this mechanism supersedes.
|                   | State the failure class that approach leaves open.] |
```

The "Competitor Defeated" field must name a specific approach -- not "existing
implementations" or "prior methods" -- and must state the failure class that approach
leaves open in one sentence. A "Competitor Defeated" field that contains a generic
description without a named approach and failure class is malformed -- rewrite before
continuing.

Assign M-IDs sequentially (M-01, M-02...).

---

### PHASE 4 -- EMIT

Output the complete rubric document with sections in this order:

1. **Failure Mode Log**
2. **Design Rationale** -- before the first criteria table; self-application,
   >= 3 rejected generic criteria
3. **Essential Criteria** -- five-field table for each criterion
4. **Recommended Criteria** -- five-field table for each criterion
5. **Aspirational Criteria** -- seven-field table (including Mechanism and
   Competitor Defeated) for each criterion; do not collapse to five fields
6. **Output Skeleton** -- a `- [ ]` checklist of all sections in this document:
   ```
   - [ ] Failure Mode Log
   - [ ] Design Rationale
   - [ ] Essential Criteria
   - [ ] Recommended Criteria
   - [ ] Aspirational Criteria
   - [ ] Output Skeleton
   - [ ] Scoring
   - [ ] Notes
   - [ ] vN Candidates
   ```
   The Output Skeleton includes itself. Tick each checkbox for every section
   present in this document.
7. **Scoring** -- composite formula, golden threshold, PARTIAL handling
8. **Notes** -- `**Version**: N`, growth trigger, banned qualifiers
9. **vN Candidates**

An evaluator reading only the Aspirational Criteria section must be able to name the
specific competing approach for every mechanism without consulting any other section.

---

## V-04 -- Inertia Framing + Lifecycle Emphasis

**Axis:** Combined -- V-01's competitor annotation requirement (C-35 target) joined with
V-02's PRE-PHASE SKELETON lifecycle step (C-36 target). C-35 is achieved via inline
COMPETITOR ANNOTATION blocks plus Competing Implementations Preamble; C-36 is achieved
via a dedicated pre-phase skeleton step with `- [ ]` format and co-located tick
instruction. C-35 and C-36 are simultaneously targeted.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will contain: (a) COMPETITOR ANNOTATION blocks co-located at each mechanism introduction naming the competing protocol and failure class, AND a Competing Implementations Preamble section before Aspirational Criteria, AND (b) a PRE-PHASE SKELETON step using `- [ ]` format with co-located tick instruction -- both halves must be present; failure of either half is independently detectable. | C-35 and C-36 operate on different structural positions (mechanism introduction content vs output structure tracking), creating no direct token-budget competition at the mechanism level; the interaction point is Phase 4 Emit, where both the Competing Implementations Preamble (C-35) and the ticked skeleton (C-36) must be completed simultaneously; generated rubrics under V-04 should show no degradation in competitor content depth vs V-01 (since annotations are written during Phase 3 before Emit), and no degradation in skeleton completeness vs V-02 (since the skeleton is written before Phase 1). | V-01 is the primary comparison site for C-35 depth under joint conditions; V-02 is the primary comparison site for C-36 completeness under joint conditions; if V-04 matches V-01 on C-35 and V-02 on C-36, the joint prompt is Pareto-optimal over either single-axis variation. |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function
for quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### PRE-PHASE SKELETON

Before beginning Phase 1, write the output skeleton. Use `- [ ]` format exactly:

```
OUTPUT SKELETON:
- [ ] Failure Mode Log
- [ ] Design Rationale
- [ ] Competing Implementations Preamble
- [ ] Essential Criteria
- [ ] Recommended Criteria
- [ ] Aspirational Criteria
- [ ] Scoring
- [ ] Notes
- [ ] vN Candidates
```

**Tick each checkbox as you complete the corresponding section during Phase 4 Emit. Do
not mark a section complete until it is fully written.**

If the skill being evaluated requires additional output sections, add `- [ ]` entries for
them before Phase 1. Do not begin Phase 1 until the skeleton is finalized.

---

### PHASE 1 -- FAILURE MODE ANALYSIS

Read the skill spec. For every way an output of this skill can fail, record:

```
F-NN | failure behavior | structural gap: what the skill omitted | blocking / suboptimal / cosmetic
```

Minimum: 3 blocking entries, 2 suboptimal entries. Do not begin Phase 2 until at least 5
entries are logged.

---

### PHASE 2 -- ESSENTIAL AND RECOMMENDED CRITERIA

Draft essential criteria (3--5) from blocking failure modes. Draft recommended criteria
(2--3) from suboptimal failure modes. Sequential C-NN numbering.

Each criterion requires five fields:

- **ID**: C-NN
- **Text**: one sentence -- what must be true in a passing output
- **Weight**: essential | recommended
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: observable anchor only; no bare qualifiers

Recommended pass conditions must test degree or specificity, not presence.

---

### PHASE 3 -- ASPIRATIONAL CRITERIA

For each aspirational mechanism, write the COMPETITOR ANNOTATION block before stating
the mechanism. Follow this structure exactly:

```
COMPETITOR ANNOTATION -- M-NN:
Competing protocol: [Name the specific existing approach. What does it do? Why does it
appear to close the gap but fail? State the specific failure class it leaves open.]

Failure class left open: [one sentence]

REQUIRED MECHANISM -- M-NN: [The mechanism that closes the gap. Derivable from the
COMPETITOR ANNOTATION above.]
```

After the COMPETITOR ANNOTATION --> REQUIRED MECHANISM pair, write the aspirational
criterion. The criterion Notes field must name the competing protocol and the failure
class closed.

STOP conditions for Phase 3:
- An aspirational criterion written before its COMPETITOR ANNOTATION block: rewrite.
- A COMPETITOR ANNOTATION that omits the failure class sentence: rewrite.
- A REQUIRED MECHANISM whose content could not be inferred from the COMPETITOR
  ANNOTATION alone: rewrite the competitor block until it supports derivation.

---

### PHASE 4 -- EMIT

Return to the PRE-PHASE SKELETON. Tick each checkbox as you write the corresponding
section.

Output the complete rubric document in this order:

1. **Failure Mode Log** -- all F-NN entries
2. **Design Rationale** -- dominant failure mode, self-application, >= 3 rejected generic
   criteria; must appear before the first criteria table
3. **Competing Implementations Preamble** -- summarize all competitors from Phase 3:
   ```
   | Competing protocol | Failure class left open | Mechanism (M-NN) |
   ```
   Every COMPETITOR ANNOTATION in Phase 3 must have exactly one row here. An evaluator
   reading only this table must be able to name the competing approach and failure class
   for every mechanism without reading the Aspirational Criteria section.
4. **Essential Criteria**
5. **Recommended Criteria**
6. **Aspirational Criteria** -- COMPETITOR ANNOTATION blocks inline before each criterion
7. **Scoring**
8. **Notes** -- `**Version**: N`, growth trigger, banned qualifiers
9. **vN Candidates**

At the end of Phase 4, confirm: every PRE-PHASE SKELETON checkbox is ticked. Every
COMPETITOR ANNOTATION has a corresponding row in the Competing Implementations Preamble.

---

## V-05 -- Role Sequence + Lifecycle Emphasis

**Axis:** Combined -- a dedicated PROVENANCE ANNOTATOR role runs after Phase 2 and before
Phase 3, producing one register entry per mechanism naming the competing protocol and
failure class (C-35 via named prior role); a dedicated SKELETON CONSTRUCTOR step runs
before Phase 1, producing the `- [ ]` checklist with tick instruction (C-36 via dedicated
lifecycle step). The derivation instruction from V-01/V-04 is ablated to isolate the
effect of role separation on C-35 compliance.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will contain: (a) a named PROVENANCE ANNOTATOR phase prior to Phase 3 whose output is a Mechanism Provenance Register with one entry per mechanism, each naming a specific competing protocol and failure class, AND (b) a SKELETON CONSTRUCTOR step before Phase 1 producing `- [ ]` format with co-located tick instruction -- any body missing either phase falsifies the respective criterion's half; falsification signals: (a) competitor annotations written inline by the Builder without a prior PROVENANCE ANNOTATOR phase boundary, (b) skeleton produced during or after Phase 1 rather than before. | Assigning competitor annotation production to the PROVENANCE ANNOTATOR role before Phase 3 creates a structural dependency: the Builder cannot start Phase 3 without a completed register, one entry per mechanism, each naming a specific competing protocol and failure class -- this dependency makes annotation completeness a pre-condition for construction rather than an audit finding after construction; V-01 (annotations inline by Builder during Phase 3) is the comparison site: if V-05's register entries show no difference in competitor specificity vs V-01's inline annotations, role separation adds no compliance advantage over inline requirements with STOP conditions. | V-01 is the primary comparison site for C-35 (PROVENANCE ANNOTATOR role vs inline annotation blocks); V-02 is the comparison site for C-36 (both have pre-phase skeleton steps -- the difference is that V-05 names the step SKELETON CONSTRUCTOR as a role, which may enforce completion more reliably). |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function
for quest-golden.

**Read the skill spec and sample outputs before writing anything.**

---

### SKELETON CONSTRUCTOR

**This step runs before Phase 1.**

Produce the `- [ ]` checklist listing every section the finished rubric document will
contain. Format exactly:

```
OUTPUT SKELETON:
- [ ] Failure Mode Log
- [ ] Design Rationale
- [ ] Mechanism Provenance Register
- [ ] Essential Criteria
- [ ] Recommended Criteria
- [ ] Aspirational Criteria
- [ ] Scoring
- [ ] Notes
- [ ] vN Candidates
```

**Tick each checkbox as you complete the corresponding section during EMIT. Do not begin
EMIT until every checkbox is ready to be ticked. Do not mark a checkbox complete until
the corresponding section is fully written.**

If the skill being evaluated requires additional sections, add `- [ ]` entries for them
now. The skeleton is the build manifest. Do not begin Phase 1 until it is final.

---

### PHASE 1 -- FAILURE MODE ANALYSIS

Read the skill spec. For every way an output of this skill can fail, record:

```
F-NN | failure behavior | structural gap: what the skill omitted | blocking / suboptimal / cosmetic
```

Minimum: 3 blocking entries, 2 suboptimal entries. Do not begin Phase 2 until at least 5
entries are logged.

---

### PHASE 2 -- ESSENTIAL AND RECOMMENDED CRITERIA

Draft essential criteria (3--5) from blocking failure modes. Draft recommended criteria
(2--3) from suboptimal failure modes. Sequential C-NN numbering.

Each criterion requires five fields:

- **ID**: C-NN
- **Text**: one sentence -- what must be true in a passing output
- **Weight**: essential | recommended
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: observable anchor only; no bare qualifiers

---

### PHASE 2.5 -- PROVENANCE ANNOTATOR

**You are now the PROVENANCE ANNOTATOR. This role runs after Phase 2 and before Phase 3.
Do not write aspirational criteria during this phase.**

Your deliverable is the Mechanism Provenance Register. Phase 3 cannot begin without a
completed register.

For each aspirational gap you identify (a property of excellent outputs not tested by
any essential or recommended criterion):

1. Identify the mechanism that closes the gap.
2. Write its provenance entry:

```
PROVENANCE ENTRY -- M-NN:
  Mechanism: [one sentence: the structural element that closes the gap]
  Competing protocol: [Name the specific existing approach -- tool, protocol, or
    framework -- that performs this mechanism's surface function. What does it do?
    Why does it appear to close the gap but fail?]
  Failure class: [one sentence: the specific gap the competing protocol leaves open]
  Targeted criterion: C-NN (assign next available number)
```

3. After all entries, produce the register summary:

```
MECHANISM PROVENANCE REGISTER:
| M-ID | Mechanism | Competing protocol | Failure class | Criterion |
| M-01 | ...        | ...                | ...           | C-NN      |
```

STOP CONDITION -- Phase 2.5: Any entry missing a "Competing protocol" or "Failure class"
row is incomplete. Rewrite before proceeding. A mechanism without provenance cannot be
introduced in Phase 3.

STOP CONDITION -- Phase 2.5: A "Competing protocol" that names a category ("rubrics
that use tables") rather than a specific named approach ("criterion-matrix format as
used in [specific tool]") is underspecified. Name the specific approach before proceeding.

Do not begin Phase 3 until every entry has a named competing protocol and a named failure
class.

---

### PHASE 3 -- ASPIRATIONAL CRITERIA (Builder)

**Your input is the completed Mechanism Provenance Register from Phase 2.5.**

For each entry in the register:
1. Write the aspirational criterion that the mechanism closes.
2. Text: names the mechanism's operative substance from the register.
3. Notes: "mechanism M-NN | defeats: [competing protocol] | closes: [failure class]"

Do not introduce mechanisms here. If a gap requires a new mechanism, add a PROVENANCE
ENTRY to Phase 2.5 and return here.

STOP condition: An aspirational criterion whose Notes field lacks an M-NN citation, a
named competing protocol, and a named failure class: rewrite.

---

### EMIT

Return to the SKELETON CONSTRUCTOR. Tick each checkbox as you write the corresponding
section.

Output the complete rubric document in this order:

1. **Failure Mode Log**
2. **Design Rationale** -- before the first criteria table; self-application, >= 3
   rejected generic criteria
3. **Mechanism Provenance Register** -- the Phase 2.5 register summary:
   M-NN | mechanism | competing protocol | failure class | criterion closed
   Every aspirational criterion must have exactly one row. An evaluator reading only
   the register must be able to name, for every aspirational criterion: (a) the mechanism,
   (b) the competing protocol it supersedes, (c) the failure class it closes -- without
   reading the Aspirational Criteria section.
4. **Essential Criteria**
5. **Recommended Criteria**
6. **Aspirational Criteria** -- Notes field cites M-NN, competing protocol, failure class
7. **Scoring**
8. **Notes** -- `**Version**: N`, growth trigger, banned qualifiers
9. **vN Candidates**

At the end of EMIT, confirm: every SKELETON CONSTRUCTOR checkbox is ticked.

---

## Set-Level Design Notes

**C-07 axis coverage:** Three distinct axis families across V-01--V-05: inertia framing
(competitor annotation placement and SV preamble requirement), lifecycle emphasis (pre-phase
skeleton with `- [ ]` format and tick instruction), output format (table structure with
dedicated Competitor Defeated column). C-07 SET-LEVEL PASS.

**C-35 coverage:** V-01 (strong, inline COMPETITOR ANNOTATION blocks + Competing
Implementations Preamble table), V-04 (very strong, combined with skeleton step), V-05
(very strong, via PROVENANCE ANNOTATOR role producing register before Phase 3). V-02
ablates C-35. V-03 partially probes C-35 via format column without STOP conditions.

**C-36 coverage:** V-02 (strong, dedicated PRE-PHASE SKELETON step with `- [ ]` and
co-located tick instruction), V-04 (very strong, combined with COMPETITOR ANNOTATIONS),
V-05 (very strong, via SKELETON CONSTRUCTOR role before Phase 1). V-01 ablates C-36.
V-03 partially probes C-36 via format-level Emit specification without pre-phase step.

**Ablation map (for comparison scoring):**

| | C-35 | C-36 |
|-|------|------|
| V-01 | Target | Ablated |
| V-02 | Ablated | Target |
| V-03 | Partial | Partial |
| V-04 | Target | Target |
| V-05 | Target (via role) | Target (via role) |

**Isolation pairs:**
- V-01 vs V-04: isolates C-36 contribution (C-35 held constant; V-04 adds skeleton step)
- V-02 vs V-04: isolates C-35 contribution (C-36 held constant; V-04 adds annotations)
- V-01 vs V-05: isolates role-separation effect on C-35 (both target C-35; V-01 inline,
  V-05 via named prior role)
- V-02 vs V-05: isolates role-naming effect on C-36 (both have pre-phase skeleton steps;
  V-05 names it SKELETON CONSTRUCTOR as a role boundary)
- V-03 vs V-01: isolates STOP condition effect on C-35 (both have competitor content;
  V-01 has inline block with STOP condition; V-03 has table column without)
- V-03 vs V-02: isolates pre-phase position effect on C-36 (both produce `- [ ]` output;
  V-02 is pre-phase with tick instruction; V-03 is Emit-time without tick instruction)

**R10 --> R11 candidate:** The hypothesis tables predict that V-01 (inline annotations
with STOP conditions) and V-05 (PROVENANCE ANNOTATOR role) will show different failure
modes for C-35: V-01 failures are missing failure class sentences (the STOP condition
catches protocol omission but the failure class sentence may remain generic); V-05 failures
are underspecified competing protocols in the register (the STOP condition fires on
category-level names). If V-05's register entries show measurably more specific competing
protocol names than V-01's inline blocks, R11 should test a three-position combination:
PROVENANCE ANNOTATOR role (V-05) producing competitor blocks ending with a derivation
instruction (V-01-style terminal sentence) plus SKELETON CONSTRUCTOR (V-05), targeting
potential C-37: PROVENANCE ANNOTATOR role as prior named phase producing one derivation-
instruction-terminated competitor block per mechanism, converting both provenance and
reader-commitment into pre-construction phase outputs.
