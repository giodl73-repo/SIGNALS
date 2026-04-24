# quest-variate Variate — Round 5

**Date:** 2026-03-15
**Skill:** quest-variate
**Rubric:** v5 (C-01 through C-27; essential C-01–C-05)
**Round:** R5 — 3 single-axis passes + 2 combination passes (C-04 combination exception applies to V-04 and V-05)

---

## Pre-Generation: Per-Axis Pole Declaration (C-16)

Before any variation body is written, declare the baseline pole for each axis.

**Champion baseline:** the R4 V-05 body (output-format × scoring-granularity combination) — a
two-phase generator with Phase 1A (axis selection) and Phase 1B (full variation header commitment
including per-criterion score-prediction block with five rows), followed by Phase 2 (generate
bodies with per-body Steps A/B/C: read axis → generically name/freeze other axes → write), and
Phase 3 (findings). Hypothesis composed of four labeled sub-fields: `criterion-target:`,
`direction:`, `mechanism:`, `failure-condition:` as a single field. No standalone pre-phase
variation map (predictions embedded inside Phase 1B headers). Per-body axis naming is generic
("name every other axis that might tempt a change; freeze each explicitly") — no per-axis named
declarations. `failure-condition:` is a single required field, not split into outcome and
implementation keys.

| Axis | Baseline Pole (Champion = R4 V-05) | R5 Committed Variation Pole |
|------|-----------------------------------|-----------------------------|
| output-format | `failure-condition:` as single required field in each variation header | V-01 single: replaced with two distinct named keys — `failure-condition-outcome:` and `failure-condition-implementation:` — each required non-blank; `failure-condition-implementation:` must name a separate criterion ID |
| lifecycle-emphasis | Per-variation score-prediction block embedded inside Phase 1B header commitment sub-stage (satisfies C-24 content, not C-27 document-scope structure) | V-02 single: prediction table extracted to standalone `## VARIATION MAP` section before Phase 1, with explicit "Do not revise after Phase 2 begins" instruction; Phase 1B retains all other header fields without the score-prediction block |
| role-sequence | Generic per-body Steps A/B/C: "name every other axis that might tempt a change; freeze each explicitly" — no per-axis named declarations | V-03 single: AXIS-FREEZE PROTOCOL with one named declaration per canonical axis (FROZEN or COMMITTED) written before each body; generic instruction replaced |
| phrasing-register | Formal-technical imperative ("Do not advance until...", "Commit.", "Phase N begins.") | Not tested single-axis R5; reserved for R6 |
| inertia-framing | No champion declared; variations compared against abstract baseline | Not tested single-axis R5; reserved for R6 |
| scoring-granularity | Per-criterion score-prediction block with five rows (C-01, C-03, C-04, C-07, C-09) required in each Phase 1B variation header | Combination target only; baseline pole unchanged in single-axis passes |

This table is the isolation reference. Only the committed axis changes per variation; all other
axes hold at their baseline pole.

---

## VARIATION MAP — Immutable after Phase 2 begins (C-27)

Committed before any variation body is written. **Do not revise after Phase 2 begins.**

| V | Axis | Pass Type | Criterion Target | Expected Direction | Mechanism Sketch |
|---|------|-----------|-----------------|-------------------|-----------------|
| V-01 | output-format | single-axis | C-25 | C-25: up; C-20 detectability: up | Two named failure-condition keys make dual-mechanism compliance structurally detectable by field presence — `failure-condition-implementation:` absent = C-20 violation visible without prose parsing |
| V-02 | lifecycle-emphasis | single-axis | C-27 | C-27: up; C-24: no-change (content same, placement changes) | Standalone pre-phase section satisfies C-27's document-scope structural requirement; freeze instruction at section level meets C-27's immutability requirement |
| V-03 | role-sequence | single-axis | C-26 | C-26: up; C-04: up | Named per-axis declarations (one per canonical axis) replace generic "freeze others" — contamination risk named before writing, not audited after |
| V-04 | output-format × lifecycle-emphasis | combination (R5 P1) | C-25, C-27 | C-25: up, C-27: up | Dual failure keys inside standalone variation map: failure condition types declared at document scope with structural detectability, satisfying C-25 within a C-27-compliant artifact |
| V-05 | role-sequence × lifecycle-emphasis | combination (R5 P2) | C-26, C-27 | C-26: up, C-27: up | Standalone map assigns axes at document scope; per-body named freeze confirms each locally — two-level commitment system that eliminates pre-generation and per-body contamination risk simultaneously |

---

## V-01 — Output Format: Dual Failure Condition Keys

**axis:** output-format
**criterion-targeted:** C-25 — "Dual failure condition sub-fields as separately labeled keys: when
a hypothesis contains two failure conditions satisfying C-20, each condition appears as a distinct
named key — `failure-condition-outcome:` and `failure-condition-implementation:` — rather than two
sentences within a single `failure-condition:` field. The separation makes C-20 compliance
structurally detectable by field presence." Mechanism: a `failure-condition-implementation:` key
that is absent or blank is detectable by structural inspection alone; two sentences inside a single
`failure-condition:` field require prose parsing to determine whether two mechanistically-distinct
conditions are present. The key naming also signals to the generator that the implementation-failure
field must point to a separate criterion, not restate the outcome failure.

**hypothesis:**
- **criterion-target:** C-25
- **direction:** increases C-25 pass rates; increases C-20 compliance detectability
- **mechanism:** because splitting `failure-condition:` into two required, distinctly named keys
  converts C-20 compliance from a content judgment (did the author include two distinct mechanisms?)
  to a structural check (is `failure-condition-implementation:` non-blank and does it name a
  separate criterion ID?). The key heading functions as a constraint: a generator filling
  `failure-condition-implementation:` must write something that identifies an implementation-specific
  failure mode and names the criterion it would independently violate — the heading itself rules out
  restating the outcome failure in different words.
- **failure-condition-outcome:** if C-25 pass rate does not exceed zero (C-25 was not targeted in
  any R4 single-axis variation — R4 V-04 combination introduced dual keys as an excellence signal
  but not as a deliberate single-axis test; no R4 single-axis body split `failure-condition:` into
  two keys), the dual-key format adds no detectability benefit over a single field with two
  sentences, and output-format should remain pointed at C-19 as its primary criterion target.
- **failure-condition-implementation:** if `failure-condition-implementation:` fields in bodies
  generated with this format describe the same mechanism as `failure-condition-outcome:` (restated
  in different words rather than naming a structurally distinct failure mode and a separate criterion
  ID), this independently fails C-20 — the dual-key structure is present but the mechanism is not
  distinct, so C-25 cannot be satisfied because C-25 only activates for hypotheses that claim or
  target C-20, and C-20 requires mechanistically-distinct conditions regardless of key naming.

**baseline-delta:** the `failure-condition:` field in the variation header is replaced with two
separately named keys: `failure-condition-outcome:` and `failure-condition-implementation:`. The
`failure-condition-implementation:` key carries the additional constraint that it must name a
separate criterion ID. No other field changes.

**completeness-risk:** the `failure-condition-implementation:` key — generators tend to describe
the same failure mode twice in different words rather than naming a mechanistically distinct
implementation failure that independently violates a separate criterion.

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

PHASE 1 — COMMIT AXES AND VARIATION HEADERS

Phase 1 has two sub-stages. Phase 2 does not begin until both are complete.

Sub-stage 1A — Axis selection.

Select {N} distinct axes from the canonical list. Use each once:

  role-sequence | output-format | lifecycle-emphasis |
  phrasing-register | inertia-framing | scoring-granularity

List all {N} axes now. Do not proceed to 1B until all axes are named and no axis appears twice.

Sub-stage 1B — Variation header commitment.

Before writing any variation body, commit a full variation header for each of the {N} selected
axes. Every field required. No field may be blank.

Header format:

```
variation: V-NN
axis: [axis name — must match Phase 1A committed axis]
pole: [one phrase — the specific change this variation makes on this axis]
baseline-delta: [one sentence — the single structural element that changes, nothing else]
completeness-risk: [the section of this specific body most at risk of omission]
criterion-target: [C-NN by ID]
direction: [increases / decreases / stabilizes] [criterion name] pass rates
mechanism: [the specific structural pathway from this axis change to the criterion outcome.
            Name what changes, what that produces structurally, and why it causes the
            criterion to move in the declared direction. Do not write "quality improves"
            — name the mechanism.]
failure-condition-outcome: [the specific observable outcome that would prove this axis
                            change produced no improvement on the targeted criterion.
                            Must name a specific prior-round comparison baseline.
                            Format: "if [criterion] pass rate does not exceed [V-NN R-N
                            result], the outcome mechanism is refuted."]
failure-condition-implementation: [the specific observable outcome that would prove this
                                   variation's mechanism was instantiated incorrectly even
                                   if the outcome metric is met. Must name a separate
                                   criterion ID that this implementation failure would
                                   independently violate. Format: "if [structural element]
                                   is [wrong state], this independently fails [C-NN],
                                   regardless of outcome metric."]
score-prediction:
  C-01 completeness:     [pass / partial / fail] — [one sentence: what about this axis
                          change causes completeness to hold or fail?]
  C-03 axis-declaration: [pass / partial / fail] — [one sentence: axis declaration risk
                          for this specific variation]
  C-04 isolation:        [pass / partial / fail] — [one sentence: name the contamination
                          risk; "no contamination risk" is valid if justified]
  C-07 hypothesis:       [pass / partial / fail] — [one sentence: name the structural
                          element that produces or fails hypothesis quality — do not write
                          "improves" — name the mechanism]
  C-09 combination:      [pass / partial / fail] — [one sentence: does this axis change
                          improve or reduce combination readiness? Why?]
```

Review all {N} headers before Phase 2:
- Every axis is distinct and from the canonical list.
- Every `criterion-target:` names a criterion ID (C-NN).
- Every `failure-condition-outcome:` names a specific prior-round comparison baseline.
- Every `failure-condition-implementation:` names a separate criterion ID it would violate.
- Every `score-prediction:` cell has a verdict and a mechanism sentence — no blank cells.
- Every `mechanism:` field names a structural pathway, not an outcome restatement.

Commit. Do not revise axis assignments after Phase 2 begins.

PHASE 2 — GENERATE VARIATION BODIES

For each committed header, write the complete variation body. Read the axis from the committed
Phase 1B header. Do not revise the header. Do not change the axis mid-generation.

For each body, apply isolation:
- Step A: Read the committed axis from Phase 1B.
- Step B: Name every other axis that might tempt a change. Freeze each explicitly.
- Step C: Change only the committed axis. Write the full body — every section, every instruction.
  No diffs. No cross-references to other variations. Every structural section present.

Label format:

### V-NN — [Axis: Pole Description]

[variation header from Phase 1B — do not revise]

[COMPLETE SKILL BODY — all sections, all instructions, fully written]

Do not begin the next variation until the current body is complete. Confirm that the section
named in `completeness-risk:` is present and fully written in the body before advancing.

PHASE 3 — FINDINGS

Declared responsibility: calibrate predictions, identify combination candidates, set evaluation
order, designate anchor.

1. Score prediction calibration:

| V | Axis | C-07 Predicted | C-07 Structure Actually Present | Prediction Correct? | Mis-prediction Mechanism |
|---|------|---------------|---------------------------------|---------------------|--------------------------|

For each wrong prediction, state in one sentence why the structural element in the body did not
behave as predicted.

2. Combination candidates (compound-effects model):

| Priority | Axis Pair | V-NN Basis | Failure Modes Per Axis | Residual Weakness After First Axis Only | Compound Criterion Effect (Both Active) | Criteria Targeted |
|----------|-----------|------------|------------------------|-----------------------------------------|-----------------------------------------|-------------------|

Column rules: V-NN Basis names the Phase 1B headers motivating the pairing. Failure Modes cites
criterion ID per axis. Residual Weakness is a concrete gap, not a restatement. Compound Criterion
Effect names a criterion ID distinct from what either axis achieves alone. A row with any blank
column is omitted.

Priority rationale: one sentence per HIGH or MEDIUM row after the table.

3. Evaluation order:

| Priority | V | Axis | Cost | Independence | Cross-Round Dependency | Sequencing Rationale |
|----------|----|------|------|--------------|------------------------|----------------------|

Cross-round dependency format: "R[round] / V-NN / [metric name]" or "none."

4. Anchor: one variation designated as the structural anchor for combination runs.
   Justify: (a) structural impact, (b) isolation quality, (c) detectable failure condition
   — one sentence each.

---

## V-02 — Lifecycle Emphasis: Standalone Pre-Phase Variation Map

**axis:** lifecycle-emphasis
**criterion-targeted:** C-27 — "The pre-generation variation map (satisfying C-24) is placed as a
distinct, independently labeled section at document scope — not embedded inside a phase body,
planning sub-stage, or preamble block — and carries an explicit immutability instruction at the
section level." Mechanism: extracting the per-variation per-criterion prediction table from Phase 1B
and placing it as a named top-level section before Phase 1 creates a standalone artifact with
document-scope visibility. The freeze instruction at the section level converts the commitment from
an implicit convention to an explicit, named immutability constraint visible before any phase begins.

**hypothesis:**
- **criterion-target:** C-27
- **direction:** increases C-27 pass rates; C-24 content is preserved with no-change (same
  per-variation per-criterion directional predictions, different placement)
- **mechanism:** because C-27 requires the variation map to have its own top-level section header
  and a freeze instruction at the section level — conditions that a map embedded inside Phase 1B
  cannot satisfy regardless of its content. Moving the map to document scope before Phase 1 creates
  the required independent section header; adding "Do not revise after Phase 2 begins" at that
  section level satisfies the immutability requirement. The content of the map is equivalent to the
  Phase 1B score-prediction block — only the structural placement changes, making this a pure
  lifecycle-emphasis change with no output-format or scoring-granularity component.
- **failure-condition-outcome:** if C-27 pass rate does not exceed zero (C-27 was not achieved in
  any R4 single-axis variation — R4 V-05 combination had Phase 1B score-prediction blocks but no
  standalone pre-phase variation map section; the R4 variate output document had a standalone map
  at document level, but that is the output document, not the skill body prompt), the standalone
  section structure adds no compliance benefit over embedding the map in Phase 1B, and lifecycle-
  emphasis should remain pointed at C-23 and C-24 as its primary criterion targets.
- **failure-condition-implementation:** if the standalone `## VARIATION MAP` section lacks the
  explicit freeze instruction at the section level (e.g., the freeze instruction is placed inside
  Phase 1 instead of at the VARIATION MAP section heading), this independently fails C-23 (phased
  prompt architecture) by introducing a commitment-phase element whose responsibility boundary is
  not clearly declared at the section level — the section becomes a preamble block without a
  declared lifecycle role, violating C-27's structural requirement for a named immutability
  declaration at the section level regardless of whether map content satisfies C-24.

**baseline-delta:** a standalone `## VARIATION MAP — Immutable after Phase 2 begins` section is
added before Phase 1, containing the per-variation per-criterion prediction table with freeze
instruction at the section level; the Phase 1B header format removes the `score-prediction:` block
(that content is now in the standalone map). No other lifecycle changes.

**completeness-risk:** the standalone variation map's per-criterion prediction rows — generators
tend to write "up" without a mechanism sentence, producing structurally-present rows that fail
C-24's per-direction-per-mechanism requirement.

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

## VARIATION MAP — Immutable after Phase 2 begins

Before Phase 1 begins, commit directional score predictions per criterion per variation. Fill
every row. A blank or verdict-only cell (no mechanism sentence) is not complete.

| V | Axis | C-01 Direction | C-04 Direction | C-07 Direction | C-09 Direction | Notes |
|---|------|----------------|----------------|----------------|----------------|-------|
[Fill all {N} rows. Each cell: verdict (up / down / no-change) + one sentence mechanism
stating why that criterion moves in that direction for this specific axis change. Do not
proceed to Phase 1 until every cell is filled with verdict and mechanism.]

**Do not revise this table after Phase 2 begins.**

PHASE 1 — COMMIT AXES AND VARIATION HEADERS

Phase 1 has two sub-stages. Phase 2 does not begin until both are complete.

Sub-stage 1A — Axis selection.

Select {N} distinct axes from the canonical list. Use each once:

  role-sequence | output-format | lifecycle-emphasis |
  phrasing-register | inertia-framing | scoring-granularity

List all {N} axes now. Do not proceed to 1B until the list is complete with no duplicates.

Sub-stage 1B — Variation header commitment.

Before writing any variation body, commit a full variation header for each of the {N} selected
axes. Every field required. No field may be blank.

Header format:

```
variation: V-NN
axis: [axis name — must match Phase 1A committed axis]
pole: [one phrase — the specific change this variation makes on this axis]
baseline-delta: [one sentence — the single structural element that changes, nothing else]
completeness-risk: [the section most at risk of omission in this specific body]
criterion-target: [C-NN by ID]
direction: [increases / decreases / stabilizes] [criterion name] pass rates
mechanism: [the specific structural pathway from this axis change to the criterion outcome.
            Name what changes, what that produces, and why it causes the criterion to move.
            Do not write "quality improves" — name the mechanism.]
failure-condition: [the specific observable outcome that would refute the mechanism.
                   Must name the prior-round comparison baseline.
                   Format: "if [criterion] pass rate does not exceed [V-NN R-N result],
                   the mechanism is refuted."]
```

Review all {N} headers before Phase 2:
- Every axis is distinct and from the canonical list.
- Every `criterion-target:` names a criterion ID (C-NN).
- Every `failure-condition:` names a specific prior-round comparison baseline.
- Every `mechanism:` field names a structural pathway, not an outcome restatement.
- The VARIATION MAP above is complete — every cell has a verdict and mechanism sentence.

Commit. Do not revise axis assignments after Phase 2 begins.

PHASE 2 — GENERATE VARIATION BODIES

For each committed header, write the complete variation body. Read the axis from Phase 1B.

For each body, apply isolation:
- Step A: Read the committed axis from Phase 1B.
- Step B: Name every other axis that might tempt a change. Freeze each explicitly.
- Step C: Change only the committed axis. Write the full body — every section, every instruction.
  No diffs. No cross-references to other variations. Every structural section present.

Label format:

### V-NN — [Axis: Pole Description]

[variation header from Phase 1B — do not revise]

[COMPLETE SKILL BODY — all sections, all instructions, fully written]

Do not begin the next variation until the current body is complete. Confirm the section named
in `completeness-risk:` is present and fully written before advancing.

PHASE 3 — FINDINGS

Declared responsibility: calibrate VARIATION MAP predictions against actual body structures,
identify combination candidates, rank evaluation order, designate anchor.

1. Prediction calibration:

| V | Axis | C-07 Predicted | C-07 Structure Actually Present | Prediction Correct? | Mis-prediction Mechanism |
|---|------|---------------|---------------------------------|---------------------|--------------------------|

For each wrong prediction, state in one sentence why the structural element in the body did not
behave as the mechanism predicted.

2. Combination candidates (compound-effects model):

| Priority | Axis Pair | V-NN Basis | Failure Modes Per Axis | Residual Weakness After First Axis Only | Compound Criterion Effect (Both Active) | Criteria Targeted |
|----------|-----------|------------|------------------------|-----------------------------------------|-----------------------------------------|-------------------|

Column rules: Failure Modes cites criterion ID per axis. Residual Weakness is a concrete gap.
Compound Criterion Effect names a criterion ID distinct from what either axis achieves alone.
A row with any blank column is omitted.

Priority rationale: one sentence per HIGH or MEDIUM row.

3. Evaluation order:

| Priority | V | Axis | Cost | Independence | Cross-Round Dependency | Sequencing Rationale |
|----------|----|------|------|--------------|------------------------|----------------------|

Cross-round dependency format: "R[round] / V-NN / [metric name]" or "none."

4. Anchor: one variation. Justify: (a) structural impact, (b) isolation quality,
   (c) detectable failure condition — one sentence each.

---

## V-03 — Role Sequence: Named Per-Axis Freeze Protocol

**axis:** role-sequence
**criterion-targeted:** C-26 — "Inside the generation phase, before writing each variation body,
the prompt instructs the generator to: (1) read the committed axis from the pre-generation
declaration; (2) explicitly name every other axis that could tempt drift and freeze each by name;
(3) proceed to write only the committed axis change. Converts C-04 single-axis isolation from a
post-body audit to a per-body pre-write checklist, surfacing contamination risk before it occurs."
Mechanism: R4 V-05's Steps A/B/C already named the pattern in generic form ("name every other axis
that might tempt a change; freeze each explicitly"). C-26 requires naming each axis specifically.
This single-axis pass promotes the generic Step B to a structured AXIS-FREEZE PROTOCOL requiring
one named declaration per canonical axis, making contamination risk visible and enumerable before
writing rather than discoverable only by post-body comparison.

**hypothesis:**
- **criterion-target:** C-26
- **direction:** increases C-26 pass rates; increases C-04 isolation quality
- **mechanism:** because requiring one named declaration per axis (from the canonical list) before
  writing each body forces the generator to confront every contamination risk explicitly rather
  than generically. A generator writing "output-format: FROZEN — no change to header key structure
  in this body" must consciously verify that output-format is unchanged; a generic "freeze others"
  instruction does not require this verification, allowing drift to occur before the generator
  notices. The per-axis declaration also functions as a count check: if six canonical axes exist
  and the generator writes only four freeze declarations, the omission is detectable by count
  inspection before the body is written.
- **failure-condition-outcome:** if C-26 pass rate does not exceed zero (C-26 was not targeted in
  any R4 single-axis variation — R4 V-05's per-body Steps A/B/C introduced the per-body pattern
  as a combination-pass excellence signal; no R4 single-axis variation required named per-axis
  declarations), the named-declaration protocol adds no C-04 improvement over the generic "freeze
  others" instruction in R4 V-05 Step B, and role-sequence should remain pointed at Loop-Gate
  Verifier mechanics as its primary C-01/C-04 targeting mechanism.
- **failure-condition-implementation:** if the AXIS-FREEZE PROTOCOL produces declarations for
  fewer than all five non-committed canonical axes (e.g., omitting phrasing-register or
  inertia-framing as "obviously not relevant"), this independently fails C-04 — the incomplete
  freeze list leaves undeclared axes available for drift, and the contamination prevention that
  C-26 requires is only partially present, reducing C-04 isolation to the same risk level as the
  generic Step B instruction.

**baseline-delta:** Steps A/B/C in Phase 2 are replaced with an AXIS-FREEZE PROTOCOL that requires
the generator to write one named freeze declaration per non-committed canonical axis before writing
each body. No other Phase 2 changes.

**completeness-risk:** the AXIS-FREEZE PROTOCOL freeze declarations — generators tend to write
incomplete freeze lists, omitting axes they consider irrelevant, defeating the purpose of the
named per-axis protocol.

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

PHASE 1 — COMMIT AXES AND VARIATION HEADERS

Phase 1 has two sub-stages. Phase 2 does not begin until both are complete.

Sub-stage 1A — Axis selection.

Select {N} distinct axes from the canonical list. Use each once:

  role-sequence | output-format | lifecycle-emphasis |
  phrasing-register | inertia-framing | scoring-granularity

List all {N} axes now. Do not proceed to 1B until all axes are named with no duplicates.

Sub-stage 1B — Variation header commitment.

Before writing any variation body, commit a full variation header for each of the {N} selected
axes. Every field required. No field may be blank.

Header format:

```
variation: V-NN
axis: [axis name — must match Phase 1A committed axis]
pole: [one phrase — the specific change this variation makes on this axis]
baseline-delta: [one sentence — the single structural element that changes, nothing else]
completeness-risk: [the section most at risk of omission in this specific body]
criterion-target: [C-NN by ID]
direction: [increases / decreases / stabilizes] [criterion name] pass rates
mechanism: [the specific structural pathway from this axis change to the criterion outcome.
            Name what changes, what that produces, and why it causes the criterion to move.
            Do not write "quality improves" — name the mechanism.]
failure-condition: [the specific observable outcome that would refute the mechanism.
                   Must name the prior-round comparison baseline.
                   Format: "if [criterion] pass rate does not exceed [V-NN R-N result],
                   the mechanism is refuted."]
score-prediction:
  C-01 completeness:     [pass / partial / fail] — [one sentence mechanism]
  C-03 axis-declaration: [pass / partial / fail] — [one sentence mechanism]
  C-04 isolation:        [pass / partial / fail] — [one sentence: name the contamination
                          risk for this specific axis; "no risk" is valid if justified]
  C-07 hypothesis:       [pass / partial / fail] — [one sentence: name the structural
                          element that produces or fails hypothesis quality — not
                          "improves" — name the mechanism]
  C-09 combination:      [pass / partial / fail] — [one sentence mechanism]
```

Review all {N} headers before Phase 2:
- Every axis is distinct and from the canonical list.
- Every `criterion-target:` names a criterion ID (C-NN).
- Every `failure-condition:` names a specific prior-round comparison baseline.
- Every `score-prediction:` cell has a verdict and a mechanism sentence — no blank cells.
- Every `mechanism:` field names a structural pathway, not an outcome restatement.

Commit. Do not revise axis assignments after Phase 2 begins.

PHASE 2 — GENERATE VARIATION BODIES

For each committed header, write the complete variation body.

Before writing each body, execute the AXIS-FREEZE PROTOCOL:

  AXIS-FREEZE PROTOCOL (fires once per body, before writing begins):

  Step 1 — Read committed axis: state the axis name from the Phase 1B header for this body.

  Step 2 — Write one freeze declaration for every axis in the canonical list:
    - role-sequence:       [FROZEN | COMMITTED — this is the axis for this body]
    - output-format:       [FROZEN | COMMITTED — this is the axis for this body]
    - lifecycle-emphasis:  [FROZEN | COMMITTED — this is the axis for this body]
    - phrasing-register:   [FROZEN | COMMITTED — this is the axis for this body]
    - inertia-framing:     [FROZEN | COMMITTED — this is the axis for this body]
    - scoring-granularity: [FROZEN | COMMITTED — this is the axis for this body]

  All six canonical axes must appear. Exactly one must be marked COMMITTED. The remaining
  five must be marked FROZEN. A freeze list with fewer than six entries is incomplete —
  do not proceed until all six entries are present.

  Step 3 — Write the body: change only the COMMITTED axis. Write the full body — every
  section, every instruction. No diffs. No cross-references to other variations.

Label format:

### V-NN — [Axis: Pole Description]

[variation header from Phase 1B — do not revise]

AXIS-FREEZE PROTOCOL:
[Step 1 committed-axis declaration]
[Step 2 six-entry freeze list — all six canonical axes filled]
[Step 3 confirmation: "Proceeding to write COMMITTED axis change only."]

[COMPLETE SKILL BODY — all sections, all instructions, fully written]

Do not begin the next variation until the current body is complete and the AXIS-FREEZE
PROTOCOL shows all six canonical axis entries filled.

PHASE 3 — FINDINGS

Declared responsibility: calibrate predictions, identify combination candidates, set evaluation
order, designate anchor.

1. Score prediction calibration:

| V | Axis | C-07 Predicted | C-07 Structure Actually Present | Prediction Correct? | Mis-prediction Mechanism |
|---|------|---------------|---------------------------------|---------------------|--------------------------|

2. Combination candidates (compound-effects model):

| Priority | Axis Pair | V-NN Basis | Failure Modes Per Axis | Residual Weakness After First Axis Only | Compound Criterion Effect (Both Active) | Criteria Targeted |
|----------|-----------|------------|------------------------|-----------------------------------------|-----------------------------------------|-------------------|

Column rules: Failure Modes cites criterion ID per axis. Residual Weakness is a concrete gap,
not a restatement. Compound Criterion Effect names a criterion ID distinct from what either
axis achieves alone. A row with any blank column is omitted.

3. Evaluation order:

| Priority | V | Axis | Cost | Independence | Cross-Round Dependency | Sequencing Rationale |
|----------|----|------|------|--------------|------------------------|----------------------|

Cross-round dependency format: "R[round] / V-NN / [metric name]" or "none."

4. Anchor: one variation. Justify: (a) structural impact, (b) isolation quality,
   (c) detectable failure condition — one sentence each.

---

## V-04 — Combination: Output Format × Lifecycle Emphasis

**axis:** output-format × lifecycle-emphasis
**pass-type:** combination (R5 Priority 1 — V-01 R5 dual failure condition keys × V-02 R5 standalone variation map)
*C-04 exception explicitly invoked.*

**hypothesis:** Combining the dual failure condition keys (V-01 R5, output-format axis:
`failure-condition-outcome:` and `failure-condition-implementation:` as distinct required keys)
with the standalone pre-phase variation map (V-02 R5, lifecycle-emphasis axis: `## VARIATION MAP`
section before Phase 1 with freeze instruction) increases C-25 and C-27 jointly:
- **criterion-target:** C-25 (primary), C-27 (secondary)
- **direction:** increases C-25 and C-27 pass rates beyond what either axis achieves alone
- **mechanism:** V-01 alone satisfies C-25 (dual keys in Phase 1B headers, structurally detectable)
  but the failure condition keys are embedded inside Phase 1B — not visible at document scope
  before Phase 1 begins. V-02 alone satisfies C-27 (standalone section before Phase 1 with freeze)
  but the variation map rows carry a single-direction verdict, not the dual-key structure C-25
  requires. The combination produces a VARIATION MAP section (C-27 structure: standalone, freeze
  instruction) whose per-variation rows include both `failure-condition-outcome:` and
  `failure-condition-implementation:` predictions (C-25 structure: named keys, separate criterion
  ID required). This is the only R5 configuration where failure condition types are declared with
  C-25's structural detectability at C-27's document scope — before any phase begins.
- **failure-condition-outcome:** if C-25 and C-27 pass rates do not jointly exceed those achieved
  by V-01 R5 alone (C-25 at header scope) and V-02 R5 alone (C-27 at document scope), the
  combination provides no compound benefit and these axes should be carried as independent
  single-axis variations in R6 rather than promoted as a compound configuration.
- **failure-condition-implementation:** if the `## VARIATION MAP` section in this combination does
  not include both `failure-condition-outcome:` and `failure-condition-implementation:` prediction
  columns per variation row (reverting to a single direction field), this independently fails C-24
  — the standalone map lacks per-variation per-criterion directional completeness, reducing the
  artifact to a structural shell without C-24-compliant prediction content, regardless of whether
  C-27's section-header and freeze-instruction requirements are met.

---

**Combination pass: output-format × lifecycle-emphasis**
*C-04 exception explicitly invoked. Dual failure condition keys (output-format axis) and standalone
pre-phase variation map (lifecycle-emphasis axis) are both active. The generated variations are
still single-axis — each changes one axis from the baseline skill. The combination applies to the
generation scaffolding structure, not to the individual variations themselves.*

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

## VARIATION MAP — Immutable after Phase 2 begins

Before Phase 1 begins, commit the axis assignment and per-variation failure condition
predictions for each of the {N} planned variations. Fill every row and every column.
A row with any blank cell is not complete.

| V | Axis | Criterion Target | failure-condition-outcome prediction | failure-condition-implementation prediction |
|---|------|-----------------|--------------------------------------|---------------------------------------------|
[Fill all {N} rows. outcome column: one sentence stating the specific observable outcome that
would prove no improvement if the mechanism is refuted, with prior-round baseline named.
implementation column: one sentence naming the structural element that would instantiate the
mechanism incorrectly and the separate criterion ID it would independently violate. Do not
proceed to Phase 1 until all rows are complete.]

**Do not revise this table after Phase 2 begins.**

PHASE 1 — COMMIT AXES AND VARIATION HEADERS

Sub-stage 1A — Axis selection.

Select {N} distinct axes from the canonical list. Use each once:

  role-sequence | output-format | lifecycle-emphasis |
  phrasing-register | inertia-framing | scoring-granularity

List all {N} axes now. No axis may appear twice.

Sub-stage 1B — Variation header commitment.

Before writing any variation body, commit a full header for each axis. Every field required.

Header format:

```
variation: V-NN
axis: [axis name — must match VARIATION MAP assigned axis and Phase 1A committed axis]
pole: [one phrase — the specific change this variation makes on this axis]
baseline-delta: [one sentence — the single structural element that changes, nothing else]
completeness-risk: [the section most at risk of omission in this specific body]
criterion-target: [C-NN by ID]
direction: [increases / decreases / stabilizes] [criterion name] pass rates
mechanism: [structural pathway from axis change to criterion outcome — name the mechanism]
failure-condition-outcome: [matches VARIATION MAP row for this V — paste or restate]
failure-condition-implementation: [matches VARIATION MAP row for this V — paste or restate;
                                   must name a separate criterion ID]
score-prediction:
  C-01: [pass / partial / fail] — [mechanism sentence]
  C-04: [pass / partial / fail] — [name the contamination risk for this axis]
  C-07: [pass / partial / fail] — [name the structural element producing hypothesis quality]
  C-09: [pass / partial / fail] — [mechanism sentence]
```

Review all {N} headers. Verify that `failure-condition-outcome:` and
`failure-condition-implementation:` in each header are consistent with the VARIATION MAP row.
Commit. Do not revise axis assignments after Phase 2 begins.

PHASE 2 — GENERATE VARIATION BODIES

For each committed header, write the complete variation body. Read the axis from Phase 1B.

For each body, apply isolation:
- Step A: Read the committed axis from Phase 1B.
- Step B: Name every other axis that might tempt a change. Freeze each explicitly.
- Step C: Change only the committed axis. Write the full body — every section, every instruction.
  No diffs. No cross-references to other variations.

Label format:

### V-NN — [Axis: Pole Description]

[variation header from Phase 1B — do not revise]

[COMPLETE SKILL BODY — all sections, all instructions, fully written]

Do not begin the next variation until the current body is complete.

PHASE 3 — FINDINGS

Declared responsibility: calibrate VARIATION MAP predictions against actual body structures,
identify combination candidates, rank evaluation order, designate anchor.

1. Prediction calibration:

| V | Axis | failure-condition-outcome predicted | Outcome condition present in body? | Match? | Mis-prediction mechanism |
|---|------|-------------------------------------|------------------------------------|--------|--------------------------|

For each mismatch, state in one sentence why the structural element did not behave as predicted.

2. Combination candidates — compound-effects model (all four elements required per row):

| Priority | Axis Pair | V-NN Basis | Failure Modes Per Axis | Residual Weakness After First Axis Only | Compound Criterion Effect (Both Active) | Criteria Targeted |
|----------|-----------|------------|------------------------|-----------------------------------------|-----------------------------------------|-------------------|

A row with any blank column is omitted. Priority rationale: one sentence per HIGH or MEDIUM row.

3. Evaluation order:

| Priority | V | Axis | Cost | Independence | Cross-Round Dependency | Sequencing Rationale |
|----------|----|------|------|--------------|------------------------|----------------------|

4. Anchor: one variation. Justify structural impact, isolation quality, detectable failure
   condition — one sentence each.

---

## V-05 — Combination: Role Sequence × Lifecycle Emphasis

**axis:** role-sequence × lifecycle-emphasis
**pass-type:** combination (R5 Priority 2 — V-03 R5 named per-axis freeze × V-02 R5 standalone variation map)
*C-04 exception explicitly invoked.*

**hypothesis:** Combining the AXIS-FREEZE PROTOCOL with named per-axis declarations (V-03 R5,
role-sequence axis) with the standalone pre-phase variation map (V-02 R5, lifecycle-emphasis axis)
increases C-26 and C-27 jointly beyond what either axis achieves alone:
- **criterion-target:** C-26 (primary), C-27 (secondary)
- **direction:** increases C-26 and C-27 pass rates beyond what either axis achieves alone
- **mechanism:** V-03 alone satisfies C-26 (per-body named freeze inside the generation loop)
  but does not satisfy C-27 (no standalone pre-phase section with section-level freeze). V-02
  alone satisfies C-27 (standalone section with freeze instruction) but retains the generic Steps
  A/B/C, not the named per-axis AXIS-FREEZE PROTOCOL that C-26 requires. The combination creates
  a two-level commitment system: the standalone variation map (lifecycle-emphasis axis) commits
  axis assignments at document scope before Phase 1 begins; the AXIS-FREEZE PROTOCOL (role-sequence
  axis) confirms each assignment locally before each body is written, reading from the VARIATION
  MAP as the authoritative source. This two-level system is the only R5 configuration that satisfies
  C-27 (document-scope commitment artifact with section-level freeze) and C-26 (per-body named
  enforcement inside the generation loop) simultaneously. The read-source dependency is the critical
  implementation detail: the protocol must read from the VARIATION MAP, not Phase 1 headers, to
  create a connected two-level system rather than two independent commitment records.
- **failure-condition-outcome:** if C-26 and C-27 pass rates do not jointly exceed those achieved
  by V-03 R5 alone (C-26 at per-body scope) and V-02 R5 alone (C-27 at document scope), the two-
  level system provides no compound benefit over independent enforcement, and these axes should
  remain independent in R6 rather than promoted as a compound configuration.
- **failure-condition-implementation:** if the AXIS-FREEZE PROTOCOL in this combination reads
  axis assignments from Phase 1 headers rather than the VARIATION MAP, the two-level commitment
  system is broken — the per-body freeze is not reinforcing the document-scope commitment but
  creating a second independent commitment record that could diverge. This independently fails
  C-17 (pre-generation axis lock): the document-scope axis lock in the VARIATION MAP is not the
  authoritative source for the per-body freeze, so the single-axis isolation mechanism is split
  across two uncoordinated artifacts, and C-26's enforcement depends on a record that may not
  match the C-27 map.

---

**Combination pass: role-sequence × lifecycle-emphasis**
*C-04 exception explicitly invoked. Named per-axis AXIS-FREEZE PROTOCOL (role-sequence axis) and
standalone pre-phase variation map (lifecycle-emphasis axis) are both active. The generated
variations are still single-axis — each changes one axis from the baseline skill. The combination
applies to the generation scaffolding structure, not to the individual variations themselves.*

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

## VARIATION MAP — Immutable after Phase 2 begins

Before Phase 1 begins, commit the axis assignment and per-criterion directional predictions
for each of the {N} planned variations. Fill every row. A blank row or a row missing a verdict
and mechanism sentence in any column is not complete.

| V | Assigned Axis | Criterion Target | C-01 Direction | C-04 Direction | C-07 Direction | Notes |
|---|--------------|-----------------|----------------|----------------|----------------|-------|
[Fill all {N} rows. Each direction cell: verdict (up / down / no-change) + one sentence
mechanism. Do not proceed to Phase 1 until all rows are filled.]

**Do not revise this table after Phase 2 begins.
The AXIS-FREEZE PROTOCOL in Phase 2 reads axis assignments from this table.**

PHASE 1 — COMMIT VARIATION HEADERS

Before writing any variation body, commit a full variation header for each of the {N} axes
assigned in the VARIATION MAP. Every field required. No field may be blank.

Header format:

```
variation: V-NN
axis: [axis name — must match VARIATION MAP assigned axis for this V]
pole: [one phrase — the specific change this variation makes on this axis]
baseline-delta: [one sentence — the single structural element that changes, nothing else]
completeness-risk: [the section most at risk of omission in this specific body]
criterion-target: [C-NN by ID]
direction: [increases / decreases / stabilizes] [criterion name] pass rates
mechanism: [structural pathway from axis change to criterion outcome — name the mechanism]
failure-condition: [if criterion pass rate does not exceed [V-NN R-N baseline], the
                   mechanism is refuted.]
score-prediction:
  C-01: [pass / partial / fail] — [mechanism sentence]
  C-04: [pass / partial / fail] — [name the contamination risk for this axis]
  C-07: [pass / partial / fail] — [name the structural element producing hypothesis quality]
  C-09: [pass / partial / fail] — [mechanism sentence]
```

Review all {N} headers. Verify every axis matches the VARIATION MAP. Commit. Do not revise
axis assignments after Phase 2 begins.

PHASE 2 — GENERATE VARIATION BODIES

For each committed header, write the complete variation body.

Before writing each body, execute the AXIS-FREEZE PROTOCOL. The protocol reads the committed
axis from the VARIATION MAP — the authoritative source. Do not read from Phase 1 headers.

  AXIS-FREEZE PROTOCOL (fires once per body, before writing begins):

  Step 1 — Read: state the axis name assigned in the VARIATION MAP for this body (V-NN:
  [axis name]).

  Step 2 — Write one freeze declaration per canonical axis:
    - role-sequence:       [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - output-format:       [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - lifecycle-emphasis:  [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - phrasing-register:   [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - inertia-framing:     [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - scoring-granularity: [FROZEN | COMMITTED — read from VARIATION MAP for this body]

  All six canonical axes must appear. Exactly one marked COMMITTED. Five marked FROZEN.
  A freeze list with fewer than six entries is incomplete — do not proceed.

  Step 3 — Write the body: change only the COMMITTED axis. Write the full body — every
  section, every instruction. No diffs. No cross-references to other variations.

Label format:

### V-NN — [Axis: Pole Description]

[variation header from Phase 1 — do not revise]

AXIS-FREEZE PROTOCOL:
[Step 1: VARIATION MAP axis declaration for this V]
[Step 2: six-entry freeze list — all six canonical axes filled]
[Step 3: "Proceeding to write COMMITTED axis change only."]

[COMPLETE SKILL BODY — all sections, all instructions, fully written]

Do not begin the next variation until the current body is complete and the AXIS-FREEZE
PROTOCOL shows all six canonical axis entries. Verify VARIATION MAP axis matches Phase 1
header axis before advancing to Phase 3.

PHASE 3 — FINDINGS

Declared responsibility: calibrate VARIATION MAP predictions against actual body structures,
verify VARIATION MAP—Phase 1 axis alignment, identify combination candidates, rank evaluation
order, designate anchor.

1. Axis alignment check:

| V | Axis (VARIATION MAP) | Axis (Phase 1 header) | Match? |
|---|---------------------|----------------------|--------|

Flag any mismatch as a protocol violation. Do not proceed to combination candidates until all
rows match.

2. Prediction calibration:

| V | Axis | C-07 Predicted (MAP) | C-07 Structure Present | Prediction Correct? | Mis-prediction Mechanism |
|---|------|----------------------|------------------------|---------------------|--------------------------|

3. Combination candidates:

| Priority | Axis Pair | V-NN Basis | Failure Modes Per Axis | Residual Weakness After First Axis Only | Compound Criterion Effect (Both Active) | Criteria Targeted |
|----------|-----------|------------|------------------------|-----------------------------------------|-----------------------------------------|-------------------|

Column rules: Failure Modes cites criterion ID per axis. Residual Weakness is a concrete gap.
Compound Criterion Effect names a criterion ID distinct from what either axis achieves alone.
A row with any blank column is omitted. Priority rationale: one sentence per HIGH or MEDIUM row.

4. Evaluation order:

| Priority | V | Axis | Cost | Independence | Cross-Round Dependency | Sequencing Rationale |
|----------|----|------|------|--------------|------------------------|----------------------|

5. Anchor: one variation. Justify structural impact, isolation quality, and detectable failure
   condition — one sentence each.

---

## Axis Tension Note (C-13 — before combination roadmap)

**Tension: output-format × lifecycle-emphasis (V-04)**

The dual failure condition keys (output-format axis, V-01 R5) operate at variation-header scope:
each Phase 1B header must contain two named failure-condition keys. The standalone variation map
(lifecycle-emphasis axis, V-02 R5) operates at document scope: a section before Phase 1 with a
section-level freeze instruction. The combination risk: a generator filling the standalone map
and then Phase 1B headers has two locations where failure conditions must be specified. If the
generator treats them as the same commitment written twice, the dual-key format in headers becomes
redundant with the map's prediction rows, and a generator that fills the map completely may
produce abbreviated Phase 1B keys that do not independently satisfy C-25's named-key requirement.

**Dominant axis prediction: output-format will dominate.** The dual-key structure in Phase 1B
headers enforces C-25 compliance at the point where failure conditions are most actionable —
inside the header governing the body to be written. The standalone map adds C-27 compliance
(document-scope placement, section-level freeze) but its failure condition columns are predictions,
not commitments that govern body content. If V-01 R5 alone achieves C-25 in headers and V-04
does not add C-27 value beyond V-02 R5 alone, the lifecycle-emphasis contribution is the weaker
axis in this combination.

**Tension: role-sequence × lifecycle-emphasis (V-05)**

The AXIS-FREEZE PROTOCOL (role-sequence axis, V-03 R5) reads the committed axis per body.
The standalone variation map (lifecycle-emphasis axis, V-02 R5) establishes axis assignments at
document scope. In V-05, the protocol is designed to read from the VARIATION MAP rather than
Phase 1 headers, creating a single authoritative source. The risk: if the generator defaults
to Phase 1 headers (the proximate source), the VARIATION MAP becomes a document-scope artifact
with no enforcement connection to the per-body protocol — two independent commitment records
that could diverge rather than a two-level system.

**Dominant axis prediction: lifecycle-emphasis will dominate.** The standalone variation map
is the load-bearing structural element: the AXIS-FREEZE PROTOCOL's compound value in V-05
derives from reading the map as the authoritative source. If the map is missing or the protocol
reads from Phase 1 headers instead, the role-sequence contribution collapses to the same generic
freeze as R4 V-05 Step B. The map must exist and be designated as the read source for the
per-body protocol to contribute the enforcement layer that C-26 requires.

---

## Combination Roadmap for Round 6 (C-09, C-22)

| Priority | Axis Pair | R5 Basis | Failure Modes Per Axis | Residual Weakness After First Axis Only | Compound Criterion Effect (Both Active) | Criteria Targeted |
|----------|-----------|----------|------------------------|-----------------------------------------|-----------------------------------------|-------------------|
| 1 | output-format × role-sequence | V-01 R5 (dual failure condition keys, C-25) × V-03 R5 (AXIS-FREEZE PROTOCOL, C-26) | output-format: single `failure-condition:` field makes C-20 compliance detectable only by prose parsing, failing C-25; role-sequence: generic "freeze others" Step B names no specific axes, leaving contamination risk unconfronted per body, failing C-26 | After output-format alone (V-01 R5): C-25 passes (dual keys in Phase 1B headers), but C-26 fails — named failure-condition keys in headers do not add per-body axis declarations before writing; contamination risk is still confronted only generically | After both active: dual failure condition keys in Phase 1B headers (output-format: C-25) + AXIS-FREEZE PROTOCOL with six named declarations before each body (role-sequence: C-26) produces a variation set where every body is preceded by a named contamination check AND every hypothesis header carries structurally-detectable dual failure conditions — C-25 and C-26 both satisfied from a single combined scaffolding | C-25, C-26 |
| 2 | phrasing-register × output-format | phrasing-register reserved from R4 and R5 (untested) × V-01 R5 (dual failure condition keys, C-25) | phrasing-register: formal-technical imperative register (untested) may push failure-condition fields toward terse one-clause entries that collapse mechanism sentences, degrading C-07 hypothesis quality; output-format: dual keys present but if register compression shortens `failure-condition-implementation:` to a bare criterion ID without mechanism, C-20 content fails | After phrasing-register alone: register change may improve structural consistency and reduce instruction verbosity, but hypothesis sub-fields requiring verbose mechanism descriptions may resist concise register, producing tension between C-07 mechanism quality and brevity | After both active: a phrasing-register calibrated to the dual-key structure could enforce consistent per-key length norms (outcome key: one sentence on criterion impact with baseline; implementation key: one sentence on mechanism + criterion ID), resolving verbosity tension while preserving C-25's named-key structural detectability | C-25, C-07 |

Priority rationale: Candidate 1 is HIGH because C-25 and C-26 are both R5 single-axis targets
addressing different scope levels (header scope and per-body scope); their combination tests
whether structural detectability and contamination prevention are mutually reinforcing in one
generation pass. Candidate 2 is MEDIUM because phrasing-register has not been tested single-
axis in either R4 or R5; its interaction with the dual-key format is speculative until the
single-axis pass runs first.

---

## Evaluation Order (C-12)

| Priority | V | Axis | Cost | Independence | Cross-Round Dependency | Sequencing Rationale |
|----------|----|------|------|--------------|------------------------|----------------------|
| 1 | V-03 | role-sequence | Low | Full — AXIS-FREEZE PROTOCOL is purely additive inside Phase 2 loop; no header field changes; no dependency on output-format or lifecycle-emphasis changes | none | Lowest cost, highest independence. Run first to establish C-26 single-axis baseline before combinations. Results needed for V-05 combination. |
| 2 | V-01 | output-format | Low | Full — `failure-condition:` field rename is self-contained; no dependency on standalone map or per-body freeze | none | Second lowest cost. Results directly inform V-04 (C-25 single-axis baseline required before V-04 combination is interpretable). |
| 3 | V-02 | lifecycle-emphasis | Medium | Partial — Phase 1B simplification (removing score-prediction block) needs V-01 context to confirm C-24 is not regressed; the standalone map must carry equivalent C-24 content to what the block carried | R5 / V-01 / C-24 baseline | Third: more invasive than header changes; Phase 1B restructuring needs V-01 as context. Must run before V-04 and V-05 (both use lifecycle-emphasis axis). |
| 4 | V-04 | output-format × lifecycle-emphasis | High | Combination — depends on V-01 (C-25 single-axis baseline) and V-02 (C-27 single-axis baseline) | R5 / V-01 / C-25 baseline; R5 / V-02 / C-27 baseline | Fourth: requires V-01 and V-02 results. Tests whether dual keys at document scope (VARIATION MAP rows) add compound value beyond header-scope dual keys alone. |
| 5 | V-05 | role-sequence × lifecycle-emphasis | High | Combination — depends on V-03 (C-26 baseline) and V-02 (C-27 baseline); highest-cost evaluation due to read-source dependency check (protocol must cite VARIATION MAP, not Phase 1, as authoritative source) | R5 / V-03 / C-26 baseline; R5 / V-02 / C-27 baseline | Fifth: most complex. Requires V-03 and V-02 results AND verification that AXIS-FREEZE PROTOCOL reads from VARIATION MAP — a structural dependency that is the unique test of the two-level commitment system. |

---

## Anchor Designation

**Designated anchor: V-03 (role-sequence: Named Per-Axis AXIS-FREEZE PROTOCOL)**

- **Structural impact:** V-03 promotes the generic Steps A/B/C freeze instruction (R4 V-05) to a
  structured per-body protocol with one named declaration per canonical axis — the highest-impact
  single change for C-26 because it converts contamination detection from a post-body audit to a
  per-body pre-write checklist with six enumerated, required entries, each requiring a deliberate
  FROZEN or COMMITTED declaration.

- **Isolation quality:** the AXIS-FREEZE PROTOCOL is purely additive — it inserts a named sub-
  section inside the Phase 2 generation loop without changing any header field, phase structure,
  findings content, or output format; contamination risk at the axis level is zero because the
  protocol change occurs inside the loop, not at the axis definition or scoring level.

- **Detectable failure condition:** if the generated AXIS-FREEZE PROTOCOL entries for any body
  contain fewer than six canonical axis declarations, C-04 isolation is not satisfied for that
  body regardless of whether body content is clean — the omission is detectable by count
  inspection of the freeze list before reading the body, making failure visible at the protocol
  level rather than requiring full-body comparison.
