---
skill: quest-rubric
skill_target: quest-rubric
date: 2026-03-15
version: 11
round: R11
changes: Targets C-37 (Competing Implementations Preamble structured as a tabular mapping
  enabling independent completeness verification by row count and minimality verification
  by failure-class column uniqueness, extending C-35's naming requirement to audit-table
  self-sufficiency) and C-38 (format-compliance STOP conditions co-located at the
  declaration step naming the non-compliant variant and stating its consequence, extending
  C-36/C-22/C-25's enforcement pattern to format-level gate-blocking); both criteria
  added in rubric v11 from R10 excellence signals ES-R10-1 and ES-R10-2
---

# quest-rubric Variate -- v11, Round 11
**Date:** 2026-03-15
**Rubric:** v11 (adds C-37: Competing Implementations Preamble as tabular audit surface
with co-located completeness instruction (row count == mechanism count) and minimality
instruction (failure-class column must be unique); C-38: format-compliance STOP condition
at declaration step naming non-compliant variant and stating consequence)
**Target criteria:** C-37, C-38

**Round 11 against rubric v11 design note:** Rounds 1--10 produced mechanisms for C-01
through C-36. The two new criteria extend two established enforcement patterns to new
structural positions:

**C-35 vs C-37.** C-35 requires the Competing Implementations Preamble to name at least
one competing SV design with its failure class. A rubric satisfies C-35 with a prose
preamble listing "approach X fails because Y." C-37 is not satisfied: the preamble must
be structured as a table -- one row per mechanism (M-NN x competing protocol x failure
class) -- with co-located instructions enabling two independent audits: (1) completeness
check by row count against the mechanism list, detectable without reading the Aspirational
Criteria section; (2) minimality check by verifying no two rows share a failure class,
detectable by column scan alone. A prose preamble cannot be audited for completeness
without reading the mechanism list, and cannot be audited for minimality without
comparing failure class sentences. A table with audit instructions makes both checks
independent of the Aspirational Criteria section. Prose naming satisfies C-35 but is
not an audit surface; a table with co-located audit instructions is.

**C-36/C-22/C-25 vs C-38.** C-36 requires the pre-phase skeleton to use `- [ ]` format
with a co-located tick instruction. C-22/C-25 establish anti-deferral patterns for
structural requirements. A rubric satisfies C-36 by declaring `- [ ]` format and
instructing the builder to tick checkboxes during construction. C-38 is not satisfied:
when two visually similar formats have non-equivalent compliance value (`- [ ]` tracked
vs `- ` untracked), the declaration step must include a STOP condition that (a) names the
non-compliant variant explicitly, (b) states the consequence (untracked section cannot be
verified by partial-tick inspection), and (c) blocks forward progress until corrected. A
declarative instruction alone allows format degradation during construction; only a gate
at declaration time naming the bad variant and its consequence prevents it.

**Axis selection:**

Two axes map directly to the two new criteria:
- Output format --> C-37: tabular preamble structure with audit columns and co-located
  completeness + minimality instructions
- Lifecycle emphasis --> C-38: STOP condition at the `- [ ]` declaration step naming the
  non-compliant variant and stating the consequence

Single-axis variations: V-01 (output format -> C-37), V-02 (lifecycle emphasis -> C-38),
V-03 (phrasing register -> partial both)
Combined variations: V-04 (role sequence + output format -> C-37 via PROVENANCE
ANNOTATOR, C-38 via SKELETON CONSTRUCTOR STOP), V-05 (inertia framing + lifecycle
emphasis -> C-37 via preamble inertia framing, C-38 via STOP with derivation link)

---

## Round 11 Variation Map

| Variation | Axis | C-37 probe | C-38 probe | Notes |
|-----------|------|-----------|-----------|-------|
| V-01 | Output format (tabular preamble with co-located completeness + minimality audit instructions at Emit) | Very strong -- Phase 4 Emit requires the Competing Implementations Preamble as a table with two co-located STOP conditions: (a) row count must equal M-ID count in Aspirational Criteria, (b) no two rows may share the same Failure class cell; both checks declared at the table declaration point before proceeding to Essential Criteria | None -- no STOP condition naming non-compliant skeleton format; PRE-PHASE SKELETON absent; `- [ ]` format requirement inherited from C-36 but without naming `- ` as non-compliant variant | Single-axis; tests whether co-located audit instructions at the Emit preamble declaration are sufficient for C-37 without format-compliance STOP conditions for C-38 |
| V-02 | Lifecycle emphasis (STOP condition at PRE-PHASE SKELETON declaration naming `- ` as non-compliant with consequence) | None -- Competing Implementations Preamble required as a table (C-35 satisfied) without audit instructions; no completeness or minimality instructions at the preamble declaration | Very strong -- PRE-PHASE SKELETON step before Phase 1 includes a STOP condition naming `- ` (dash-space) as the non-compliant variant, stating "a `- ` entry is untracked -- section completion cannot be verified by partial-tick inspection," and blocking forward progress until every entry uses `- [ ]` format | Single-axis; tests whether naming the non-compliant variant and its consequence at the skeleton declaration satisfies C-38 without the tabular audit structure for C-37 |
| V-03 | Phrasing register (conversational/instructional throughout) | Partial -- tracking table described as "keep track of what each mechanism replaces" without explicit row-count or failure-class-uniqueness instructions; table format present but no audit language co-located at the table declaration | Partial -- skeleton step uses instructional language ("make sure each entry uses `- [ ]`") without a formal STOP condition naming `- ` as non-compliant or stating the untracked-section consequence | Single-axis; tests whether conversational register degrades STOP condition robustness; primary comparison site for C-37 (vs V-01 audit depth) and C-38 (vs V-02 gate strength) under register shift |
| V-04 | Role sequence + output format (PROVENANCE ANNOTATOR produces audit table with construction-time completeness + minimality checks; SKELETON CONSTRUCTOR includes format STOP condition) | Very strong -- PROVENANCE ANNOTATOR (Phase 2.5) produces the Mechanism Provenance Register table with co-located completeness instruction (row count == M-ID count) and minimality instruction (failure class column must be unique); both checks enforced at register construction time before Phase 3 begins | Very strong -- SKELETON CONSTRUCTOR step (before Phase 1) includes STOP condition naming `- ` as non-compliant, stating "untracked -- section completion cannot be verified by partial-tick inspection," and blocking Phase 1 until corrected | Combined; C-37 via PROVENANCE ANNOTATOR construction-time audit (vs V-01's Emit-time audit); C-38 via SKELETON CONSTRUCTOR STOP condition (matches V-02 mechanism); tests whether construction-time audit enforcement produces tighter failure-class uniqueness than Emit-time enforcement |
| V-05 | Inertia framing + lifecycle emphasis (preamble audit instructions framed as inertia tests naming prose-preamble failure classes; STOP condition with derivation link) | Very strong -- Phase 4 Emit: Competing Implementations Preamble table framed as inertia test against prose preambles; audit instructions name "prose-preamble incompleteness" and "prose-preamble non-minimality" as the specific failure classes the table avoids; row-count and failure-class-uniqueness checks co-located at the table declaration | Very strong -- PRE-PHASE SKELETON STOP condition names `- ` as the inertia competitor, states the consequence ("a `- ` entry cannot be ticked"), and adds a derivation link ("only `- [ ]` entries satisfy the construction-tracking intent of the checklist") | Combined; C-37 via inertia framing (names prose-preamble approach as competitor with specific failure classes); C-38 via STOP condition + derivation link; comparison with V-01 isolates inertia framing effect on audit instruction specificity; comparison with V-02 isolates derivation link effect on STOP condition depth |

---

## V-01 -- Output Format

**Axis:** Output format -- the Competing Implementations Preamble is structured as a
table with co-located completeness-audit (row count must equal mechanism count) and
minimality-audit (failure class column must be unique) instructions declared as STOP
conditions at the Phase 4 Emit preamble declaration point before proceeding to Essential
Criteria.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will contain a Competing Implementations Preamble table with two co-located STOP conditions: (a) "row count must equal the number of M-IDs in the Aspirational Criteria section -- if counts differ, a mechanism is missing from the preamble," and (b) "if any two rows share the same Failure class cell, two mechanisms target the same gap -- merge or remove one before continuing"; any body where the preamble is prose-only, or where the table lacks either audit instruction, falsifies the respective C-37 half; the falsification signal is a table present but without co-located audit language, or audit language that appears in a section other than the preamble declaration point. | Co-locating both audit instructions at the preamble table declaration creates a two-check gate at Emit: the builder must verify completeness and minimality before writing Essential Criteria; generated rubrics under V-01 should show tighter failure-class uniqueness (no duplicate failure class sentences across mechanisms) than V-03, where the table is present but no minimality check is specified; V-04 applies the same audit instructions at construction time (PROVENANCE ANNOTATOR Phase 2.5) rather than at Emit -- if V-04 shows tighter failure-class uniqueness than V-01, construction-time enforcement is the load-bearing mechanism. | V-04 primary comparison for C-37 (same audit instructions; Emit-time vs construction-time); V-03 secondary comparison (table present in both; audit instructions present in V-01, absent in V-03); V-05 tertiary comparison (both have audit instructions at Emit; V-01 frames as structural verification, V-05 frames as inertia test). |

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
- A COMPETITOR ANNOTATION that names the competing protocol but omits the failure class
  sentence: rewrite.
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
   produce the table:
   ```
   | M-ID | Competing protocol | Failure class left open | Mechanism that closes it |
   ```
   Every COMPETITOR ANNOTATION in Phase 3 must have exactly one row in this table.

   STOP: Count the rows in this table. Count the M-IDs in the Aspirational Criteria
   section. If counts differ, a mechanism is missing from the preamble -- add the missing
   row before continuing.

   STOP: Scan the "Failure class left open" column. If any two rows share the same failure
   class, two mechanisms target the same gap. Merge or remove one mechanism before
   continuing. The preamble is minimal when every failure class in the column is unique.

   An evaluator reading only the Competing Implementations Preamble must be able to: (a)
   name the competing approach for every mechanism, (b) name its failure class, and (c)
   identify which M-NN closes each gap -- without reading the Aspirational Criteria
   section.
4. **Essential Criteria** -- all five fields per criterion
5. **Recommended Criteria** -- all five fields per criterion
6. **Aspirational Criteria** -- COMPETITOR ANNOTATION blocks inline immediately before
   the criterion each closes; do not move competitor blocks to a separate section
7. **Scoring** -- composite formula, golden threshold, PARTIAL handling
8. **Notes** -- `**Version**: N`, growth trigger, banned qualifier list, N/A scope blocks
9. **vN Candidates** -- patterns approaching promotion; evidence needed per candidate

The two STOP conditions at the Competing Implementations Preamble are gates: do not
proceed to Essential Criteria until both pass (row count verified, failure classes unique).

---

## V-02 -- Lifecycle Emphasis

**Axis:** Lifecycle emphasis -- a dedicated PRE-PHASE SKELETON step before Phase 1
includes a STOP condition that (a) names `- ` (dash-space) as the non-compliant format
variant, (b) states the consequence ("a `- ` entry is untracked -- section completion
cannot be verified by partial-tick inspection"), and (c) blocks forward progress until
every entry uses `- [ ]` format.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will have a PRE-PHASE SKELETON step containing `- [ ]` entries AND a co-located STOP condition that: (a) names `- ` as the non-compliant variant, (b) states "a `- ` entry is untracked -- section completion cannot be verified by partial-tick inspection without re-reading the entire document," and (c) instructs the builder to rewrite before proceeding; any body where the STOP condition is absent, or where it names the wrong variant, or where it states the format requirement without naming the consequence, falsifies the C-38 half; falsification signal: a skeleton step that reads "use `- [ ]` only" without naming `- ` as the specific wrong alternative and stating the untracked-section consequence. | Naming the non-compliant variant and its consequence at the declaration step makes the compliance value of `- [ ]` explicit before any output content is written; generated rubrics under V-02 should show lower format-compliance drift (accidental use of `- ` in output sections that should be tracked) than V-03, which uses instructional language without naming the non-compliant alternative; the consequence statement ("untracked section") also reinforces the C-36 mechanism's intent, which may appear in the rubric's own Notes section as evidence of self-application. | V-04 primary comparison for C-38 (both have STOP condition naming `- ` as non-compliant; V-04 adds tabular audit for C-37); V-03 secondary comparison (both have skeleton step with `- [ ]`; V-02 has STOP condition, V-03 has instructional language only); V-05 tertiary comparison (both have STOP condition naming `- `; V-05 adds derivation link). |

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
- [ ] Competing Implementations Preamble
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

If the skill being evaluated requires additional output sections, add `- [ ]` entries
before Phase 1. Each added section requires its own `- [ ]` entry.

STOP CONDITION: A skeleton entry that uses `- ` (dash-space) rather than `- [ ] ` is
non-compliant. A `- ` entry is untracked -- section completion cannot be verified by
partial-tick inspection without re-reading the entire document. Rewrite every `- ` entry
as `- [ ]` before proceeding. Do not begin Phase 1 until all skeleton entries use
`- [ ]` format.

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
1. Name the structural gap it closes (one sentence: what passes essential+recommended but
   falls short of excellence here).
2. Name the mechanism that closes the gap (one sentence).
3. Write the five-field criterion. Text must reference the mechanism's operative substance.
   Notes must state: "mechanism: M-NN -- [mechanism description] | defeats: [competing
   approach] | closes: [failure class]."

Assign M-IDs sequentially (M-01, M-02...).

STOP conditions:
- An aspirational criterion without a named mechanism: rewrite.
- A mechanism that overlaps with an existing mechanism: merge or split before writing
  the criterion.

---

### PHASE 4 -- EMIT

Return to the PRE-PHASE SKELETON. Tick each checkbox as you write the corresponding
section.

Output the complete rubric document in this order:

1. **Failure Mode Log**
2. **Design Rationale** -- before the first criteria table
3. **Competing Implementations Preamble** -- a table listing each competing approach
   surfaced in Phase 3:
   ```
   | Competing protocol | Failure class left open | Mechanism that closes it |
   ```
   Every aspirational criterion must have exactly one row. An evaluator reading only
   this table must be able to name the competing approach and failure class for every
   mechanism without reading the Aspirational Criteria section.
4. **Essential Criteria**
5. **Recommended Criteria**
6. **Aspirational Criteria**
7. **Scoring**
8. **Notes** -- `**Version**: N`, growth trigger, banned qualifiers
9. **vN Candidates**

At the end of Phase 4, review the PRE-PHASE SKELETON. Every checkbox must be ticked.
If any checkbox is unticked, the corresponding section is missing -- write it before
submitting the rubric.

---

## V-03 -- Phrasing Register

**Axis:** Phrasing register -- formal/technical instruction language throughout is
replaced with conversational/instructional register. Phase headers become action-oriented.
Criterion field requirements are described as guidance. The Competing Implementations
tracking table is described without explicit audit instructions. The skeleton step uses
plain instructional language without a formal STOP condition naming the non-compliant
format variant.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Generated rubric bodies under V-03 will contain: (a) a Competing Implementations tracking table (C-35 satisfied) without completeness or minimality audit instructions co-located at the table declaration -- the table column for competing approaches will be present but no row-count check or failure-class-uniqueness check will be stated, and (b) a skeleton section using `- [ ]` format (C-36 satisfied) without a STOP condition naming `- ` as non-compliant or stating the untracked-section consequence; the C-37 and C-38 halves are partially probed -- table structure present for C-37 without audit-instruction gate, `- [ ]` format present for C-38 without consequence-naming gate; falsification signal: a body where the table declaration includes an explicit row-count verification or failure-class-uniqueness check (C-37 would be incorrectly probed). | Conversational register reduces gate-blocking language density; "make sure each entry uses `- [ ]`" is instructional but does not name the non-compliant alternative or state a consequence, satisfying C-36 intent but failing C-38's gate requirement; "keep track of what each mechanism replaces" is descriptive but does not verify completeness or minimality, satisfying C-35 but failing C-37's audit-table requirement; generated rubrics under V-03 should be distinguishable from V-01 and V-02 by the absence of co-located audit language at structural decision points, providing the negative control for both C-37 and C-38 probes. | V-01 primary comparison for C-37 (both have table; V-01 has audit instructions, V-03 does not); V-02 primary comparison for C-38 (both have `- [ ]` skeleton; V-02 has STOP condition naming non-compliant variant, V-03 does not). |

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function
for quest-golden.

Start by reading the skill spec and any sample outputs provided. Don't write anything yet.

---

### Start here: build your skeleton

Before you do any analysis, write down every section your finished rubric will contain.
Use checkbox format for each entry:

```
- [ ] Failure Mode Log
- [ ] Design Rationale
- [ ] Essential Criteria
- [ ] Recommended Criteria
- [ ] Aspirational Criteria
- [ ] Scoring
- [ ] Notes
- [ ] vN Candidates
```

Make sure each line uses `- [ ]` checkbox format. Add any additional sections the skill
requires. Tick each checkbox when you finish writing that section.

---

### Now build the failure log

Read through the skill spec. For each way an output can fail, write:

```
F-NN | what goes wrong | what the skill left out | blocking / suboptimal / cosmetic
```

Keep going until you have at least 3 blocking failures and 2 suboptimal ones. Don't move
on until you're there.

---

### Now write the core criteria

From your blocking failures, draft 3--5 essential criteria. From your suboptimal
failures, draft 2--3 recommended criteria. Number them sequentially (C-01, C-02...).

For each criterion, include:
- **ID**: C-NN
- **Text**: one sentence -- what a good output does
- **Weight**: essential | recommended
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: something you can actually check -- a count, a named pattern, a
  specific thing that's either present or absent

For recommended criteria: the pass condition should test quality, not just presence.

---

### Now write the aspirational criteria

For each aspirational criterion:
1. Describe the gap -- what passes the core criteria but still falls short of excellent?
2. Describe the mechanism -- what structural element would close that gap?
3. Write the criterion with all five fields. In the Notes field, name the mechanism and
   which prior approach this replaces.

Keep track of what each mechanism replaces by adding a tracking table:

```
| Competing approach | What it gets wrong | Mechanism that fixes it |
```

Include one row for each aspirational mechanism. Name the competing approach precisely --
don't just say "prior methods" or "existing implementations."

---

### Now emit the full rubric

Write the complete rubric in this order:

1. **Failure Mode Log** -- all your F-NN entries
2. **Design Rationale** -- the dominant failure mode, how the rubric applies to itself,
   and at least 3 generic criteria you considered but rejected (with reasons why)
3. **Competing Implementations Preamble** -- your tracking table from the aspirational
   step
4. **Essential Criteria**
5. **Recommended Criteria**
6. **Aspirational Criteria**
7. **Scoring** -- formula, golden threshold, how to handle partial criteria
8. **Notes** -- version number, when the rubric should grow, and a banned qualifier list
9. **vN Candidates** -- patterns that keep coming up but aren't criteria yet

Tick each checkbox in your skeleton as you finish each section.

---

## V-04 -- Role Sequence + Output Format

**Axis:** Combined -- a SKELETON CONSTRUCTOR step (before Phase 1) produces the `- [ ]`
checklist with a co-located STOP condition naming `- ` as non-compliant and stating the
consequence (C-38 target); a PROVENANCE ANNOTATOR role (Phase 2.5) produces the Mechanism
Provenance Register as a table with co-located completeness and minimality audit
instructions applied at construction time before Phase 3 (C-37 target). This is the
three-position combination signaled by R10 Set-Level Design Notes: V-05-R10's role
separation extended with construction-time audit enforcement for both criteria.

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will contain: (a) a SKELETON CONSTRUCTOR output using `- [ ]` format with a STOP condition naming `- ` as non-compliant and stating "untracked -- section completion cannot be verified by partial-tick inspection," AND (b) a Mechanism Provenance Register table produced by the PROVENANCE ANNOTATOR with co-located completeness instruction (row count == M-ID count) and minimality instruction (failure class column must be unique); both halves independently falsifiable; falsification signals: (a) SKELETON CONSTRUCTOR output present but STOP condition absent or missing consequence statement, (b) PROVENANCE ANNOTATOR register present but audit instructions absent or appearing at Emit rather than at Phase 2.5 declaration. | Applying the completeness and minimality audit instructions at PROVENANCE ANNOTATOR time (Phase 2.5) means the builder verifies both properties before Phase 3 begins -- a mechanism with a duplicate failure class is caught before its criterion is written, rather than after the Aspirational Criteria section is complete; V-01 applies the same audit instructions at Emit -- if V-04 shows tighter failure-class uniqueness than V-01 in generated rubrics, construction-time auditing produces more constraint enforcement than Emit-time auditing; the SKELETON CONSTRUCTOR STOP condition matches V-02's mechanism exactly, isolating the C-37 audit instruction timing as the sole variable. | V-01 primary comparison for C-37 (same audit instructions; Emit-time vs Phase 2.5 construction-time); V-02 primary comparison for C-38 (both have STOP condition naming `- ` and stating consequence; V-04 additionally has C-37 audit). |

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

**Tick each checkbox as you complete the corresponding section during EMIT. Do not mark a
checkbox complete until the corresponding section is fully written.**

STOP CONDITION: A skeleton entry that uses `- ` (dash-space) rather than `- [ ] ` is
non-compliant. A `- ` entry is untracked -- section completion cannot be verified by
partial-tick inspection. Rewrite every `- ` entry as `- [ ]` before proceeding. Do not
begin Phase 1 until all entries use `- [ ]` format.

If the skill being evaluated requires additional sections, add `- [ ]` entries now. The
skeleton is the build manifest. Do not begin Phase 1 until it is final.

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

### PHASE 2.5 -- PROVENANCE ANNOTATOR

**You are now the PROVENANCE ANNOTATOR. This role runs after Phase 2 and before Phase 3.
Do not write aspirational criteria during this phase.**

Your deliverable is the Mechanism Provenance Register. Phase 3 cannot begin without a
completed register that passes the row-count and failure-class-uniqueness checks below.

For each aspirational gap you identify (a property of excellent outputs not tested by any
essential or recommended criterion):

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
```

STOP CONDITION: Row count in the register summary must equal the number of M-IDs in your
provenance entries. If counts differ, an entry is missing from the summary -- add it
before proceeding.

STOP CONDITION: Scan the "Failure class" column. If any two rows share the same failure
class, two mechanisms target the same gap -- merge or remove one before proceeding. The
register is minimal when every failure class is unique.

STOP CONDITION: Any provenance entry missing a "Competing protocol" or "Failure class"
field is incomplete. Rewrite before proceeding. A mechanism without provenance cannot be
introduced in Phase 3.

STOP CONDITION: A "Competing protocol" that names a category ("rubrics that use tables")
rather than a specific named approach ("criterion-matrix format as used in [specific
tool]") is underspecified. Name the specific approach before proceeding.

Do not begin Phase 3 until every entry has a named competing protocol, a named failure
class, and the register summary passes both the row-count check and the failure-class-
uniqueness check.

---

### PHASE 3 -- ASPIRATIONAL CRITERIA (Builder)

**Your input is the completed Mechanism Provenance Register from Phase 2.5.**

For each entry in the register:
1. Write the aspirational criterion that the mechanism closes.
2. Text: names the mechanism's operative substance from the register.
3. Notes: "mechanism M-NN | defeats: [competing protocol] | closes: [failure class]"

Do not introduce mechanisms here. If a gap requires a new mechanism, add a PROVENANCE
ENTRY to Phase 2.5, verify the register still passes both checks, then return here.

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
   ```
   | M-ID | Mechanism | Competing protocol | Failure class | Criterion |
   ```
   Every aspirational criterion must have exactly one row. An evaluator reading only the
   register must be able to name, for every aspirational criterion: (a) the mechanism,
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

## V-05 -- Inertia Framing + Lifecycle Emphasis

**Axis:** Combined -- inertia framing applied to the Competing Implementations Preamble
declaration (C-37 target: preamble table framed as an inertia test against prose
preambles, with audit instructions naming prose-preamble incompleteness and
non-minimality as the specific failure classes the table structure avoids) + lifecycle
emphasis at the PRE-PHASE SKELETON declaration step (C-38 target: STOP condition names
`- ` as the inertia competitor, states the consequence, and adds a derivation link
explaining why `- [ ]` is the required format).

**Hypothesis:**

| Primary-effect | Secondary-effect | Predicted manifestation sites |
|---|---|---|
| Every generated rubric body will contain: (a) a Competing Implementations Preamble table framed as an inertia test against prose preambles, with co-located audit instructions that name "prose-preamble incompleteness" (a mechanism may exist without a preamble row, undetectable without reading the Aspirational Criteria section) and "prose-preamble non-minimality" (two mechanisms with shared failure classes are indistinguishable in prose) as the two failure classes the table structure closes, AND (b) a PRE-PHASE SKELETON STOP condition that names `- ` as the inertia competitor, states "a `- ` entry cannot be ticked -- section completion cannot be verified by partial-tick inspection," and adds a derivation link ("only `- [ ]` entries satisfy the construction-tracking intent of the checklist"); both halves independently falsifiable. | Framing audit instructions as inertia tests (naming the competing approach and its failure class) produces more specific audit language than V-01's structural audit instructions (which state row-count and failure-class checks without naming the prose-preamble as the competitor); the derivation link in V-05's STOP condition names the reason `- [ ]` is required (construction-tracking intent) rather than just naming the non-compliant format, which may reduce accidental use of `- ` more than V-02's STOP condition alone; generated rubrics under V-05 should show more explicit failure-class naming in the preamble audit instructions than V-01, where the instructions are structural without an inertia target. | V-01 primary comparison for C-37 (both have audit instructions at Emit; V-01 frames as structural verification, V-05 frames as inertia test naming prose-preamble failure classes); V-02 primary comparison for C-38 (both have STOP condition naming `- ` with consequence; V-05 adds derivation link explaining construction-tracking intent). |

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
- [ ] Competing Implementations Preamble
- [ ] Essential Criteria
- [ ] Recommended Criteria
- [ ] Aspirational Criteria
- [ ] Scoring
- [ ] Notes
- [ ] vN Candidates
```

**Tick each checkbox as you complete the corresponding section during Phase 4 Emit.**

If the skill being evaluated requires additional output sections, add `- [ ]` entries
before Phase 1. Do not begin Phase 1 until the skeleton is finalized.

STOP CONDITION: A skeleton entry using `- ` (dash-space) is the non-compliant variant.
The competing approach -- a dash-bullet list -- appears to track sections but cannot be
ticked during construction. A `- ` entry is untracked: section completion cannot be
verified by partial-tick inspection without re-reading the entire document. Only `- [ ]`
entries satisfy the construction-tracking intent of the checklist -- the builder must be
able to verify completeness by scanning ticked vs unticked states alone. Rewrite every
`- ` entry as `- [ ]` before proceeding.

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

For each aspirational mechanism, write the COMPETITOR ANNOTATION block before stating the
mechanism. Follow this structure exactly:

```
COMPETITOR ANNOTATION -- M-NN:
Competing protocol: [Name the specific existing approach -- a named tool, protocol, or
framework -- that performs this mechanism's surface function. What does it do? Why does
it appear to satisfy the gap but fail to close it? State the specific failure class the
competing approach leaves open.]

Failure class left open by [competing protocol name]: [one sentence]

REQUIRED MECHANISM -- M-NN: [State the mechanism that closes the gap. The positive
definition must be derivable from the COMPETITOR ANNOTATION above.]
```

After the COMPETITOR ANNOTATION --> REQUIRED MECHANISM pair, write the aspirational
criterion. The criterion Notes field must state which competing protocol it supersedes
and the failure class closed.

Assign M-IDs sequentially (M-01, M-02...).

STOP conditions for Phase 3:
- An aspirational criterion written before its COMPETITOR ANNOTATION block: rewrite.
- A COMPETITOR ANNOTATION that omits the failure class sentence: rewrite.
- A REQUIRED MECHANISM whose content could not be inferred from the COMPETITOR ANNOTATION
  alone: rewrite the competitor block until it supports derivation.

---

### PHASE 4 -- EMIT

Return to the PRE-PHASE SKELETON. Tick each checkbox as you write the corresponding
section.

Output the complete rubric document in this order:

1. **Failure Mode Log** -- all F-NN entries from Phase 1
2. **Design Rationale** -- dominant failure mode, self-application, >= 3 rejected generic
   criteria with reasons; must appear before the first criteria table
3. **Competing Implementations Preamble** -- the inertia test for table structure over
   prose preambles. A prose preamble is the competing approach: it names competitors but
   cannot be audited for completeness (a mechanism may exist without a preamble entry,
   undetectable without reading the Aspirational Criteria section -- the
   "prose-preamble incompleteness" failure class) and cannot be audited for minimality
   (two mechanisms targeting the same gap are indistinguishable when their failure classes
   appear in prose -- the "prose-preamble non-minimality" failure class). The table closes
   both failure classes:
   ```
   | M-ID | Competing protocol | Failure class left open | Mechanism that closes it |
   ```
   STOP: Row count must equal the number of M-IDs in the Aspirational Criteria section.
   The prose-preamble incompleteness failure class is realized when this count fails --
   a mechanism exists without a preamble row. Fix before continuing.

   STOP: Scan the "Failure class left open" column. If any two rows share the same failure
   class, the prose-preamble non-minimality failure class is realized -- two mechanisms
   target the same gap. Merge or remove one before continuing. The table is minimal when
   every row's failure class is unique.

   An evaluator reading only this table must find: (a) one row per M-ID, (b) a named
   competing approach per row, (c) a unique failure class per row, (d) the M-ID of the
   mechanism that closes each gap. No generic competitor entries.
4. **Essential Criteria**
5. **Recommended Criteria**
6. **Aspirational Criteria** -- COMPETITOR ANNOTATION blocks inline before each criterion
7. **Scoring** -- composite formula, golden threshold, PARTIAL handling
8. **Notes** -- `**Version**: N`, growth trigger, banned qualifier list
9. **vN Candidates** -- patterns approaching promotion; evidence needed per candidate

At the end of Phase 4: confirm every PRE-PHASE SKELETON checkbox is ticked. Confirm the
Competing Implementations Preamble row count equals the M-ID count in Aspirational
Criteria. Confirm no two rows in the preamble share a failure class.

---

## Set-Level Design Notes

**C-07 axis coverage:** Three distinct axis families across V-01--V-05: output format
(tabular audit contract with co-located completeness + minimality instructions), lifecycle
emphasis (STOP condition at declaration step naming non-compliant variant and consequence),
phrasing register (conversational/instructional language throughout). C-07 SET-LEVEL PASS.

**C-37 coverage:** V-01 (strong, tabular preamble with completeness + minimality STOP
conditions at Emit declaration), V-04 (very strong, via PROVENANCE ANNOTATOR
construction-time audit before Phase 3), V-05 (very strong, via inertia framing naming
prose-preamble incompleteness + non-minimality as the specific failure classes closed).
V-02 ablates C-37. V-03 partially probes C-37 (table present without audit instructions).

**C-38 coverage:** V-02 (strong, STOP condition at PRE-PHASE SKELETON declaration naming
`- ` and stating untracked-section consequence), V-04 (very strong, via SKELETON
CONSTRUCTOR STOP condition matching V-02 mechanism exactly), V-05 (very strong, via
STOP condition + derivation link naming construction-tracking intent as the requirement
source). V-01 ablates C-38. V-03 partially probes C-38 (`- [ ]` format present without
STOP condition naming non-compliant variant).

**Ablation map:**

| | C-37 | C-38 |
|-|------|------|
| V-01 | Target | Ablated |
| V-02 | Ablated | Target |
| V-03 | Partial | Partial |
| V-04 | Target | Target |
| V-05 | Target | Target |

**Isolation pairs:**
- V-01 vs V-04: isolates C-38 contribution under joint presence (C-37 held constant via
  same audit instructions; V-04 adds SKELETON CONSTRUCTOR STOP condition for C-38)
- V-02 vs V-04: isolates C-37 contribution under joint presence (C-38 held constant via
  same STOP condition; V-04 adds PROVENANCE ANNOTATOR audit table for C-37)
- V-01 vs V-05: isolates inertia-framing effect on C-37 audit instruction specificity
  (both have row-count + failure-class audit at Emit; V-01 structural, V-05 inertia-named)
- V-02 vs V-05: isolates derivation-link effect on C-38 STOP condition depth (both name
  `- ` as non-compliant with consequence; V-05 adds construction-tracking derivation link)
- V-03 vs V-01: isolates audit instruction presence for C-37 (both have table; V-01 has
  STOP conditions, V-03 does not)
- V-03 vs V-02: isolates STOP condition presence for C-38 (both have `- [ ]` skeleton;
  V-02 has STOP condition naming non-compliant variant, V-03 does not)

**R11 --> R12 candidate:** V-04 tests construction-time vs Emit-time audit enforcement
for C-37. If V-04's PROVENANCE ANNOTATOR register shows tighter failure-class uniqueness
than V-01's Emit-time audit, construction-time position is the load-bearing mechanism for
C-37 depth. V-05's inertia framing names prose-preamble failure classes explicitly, which
may produce stronger audit language than V-01's structural check. If V-05 shows more
specific failure-class naming in the preamble than V-01, inertia framing is the
load-bearing mechanism for C-37 audit specificity. A potential C-39 combines both:
PROVENANCE ANNOTATOR (construction-time) with inertia framing (names prose-preamble as
the competitor with specific failure classes) + SKELETON CONSTRUCTOR STOP with derivation
link. R12 should test whether the three-position combination (construction-time + inertia
framing + derivation link) is additive over any two-position pair, or whether one position
dominates.
