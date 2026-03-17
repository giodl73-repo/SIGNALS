# quest-variate Variate -- Round 4

**Date:** 2026-03-15
**Skill:** quest-variate
**Rubric:** v4 (C-01 through C-24; essential C-01--C-05)
**Round:** R4 -- 3 single-axis passes + 2 combination passes (C-04 combination exception applies to V-04 and V-05)

---

## Pre-Generation: Per-Axis Pole Declaration (C-16)

Before any variation body is written, declare the baseline pole for each axis.

**Champion baseline:** the R3 V-04 body -- a two-phase generator with a structured variation
envelope (six required fields committed before each body) and a Loop-Gate Verifier role that
fires per body checking C-01 and C-04 before advancing. Findings section uses prose combination
candidates, a variation map, and an anchor designation. No four-part hypothesis sub-fields.
No per-criterion score predictions. No dedicated cross-round dependency phase.

| Axis | Baseline Pole (Champion) | R4 Committed Variation Pole |
|------|-------------------------|-----------------------------|
| role-sequence | Loop-Gate Verifier fires per body, checks C-01 and C-04 only | V-04 combo: Loop-Gate Verifier + champion-challenger role added pre-body |
| output-format | Structured envelope with 6 prose fields; hypothesis is a single prose paragraph | V-01 single: hypothesis field split into four labeled sub-fields (criterion-target, direction, mechanism, failure-condition) |
| lifecycle-emphasis | Phase 1 (commit envelopes) -> Phase 2 (generate+gate) -> Phase 3 (findings); equal weight per phase | V-02 single: Phase 1 expanded with mandatory per-variation score prediction sub-stage before Phase 2 opens |
| phrasing-register | Formal-technical imperative ("Do not advance until...") | Not tested single-axis R4; reserved for R5 |
| inertia-framing | No champion declared; variations compared against abstract baseline | V-04 combo: champion declared with three-failure inventory; each hypothesis attacks named champion failure |
| scoring-granularity | No per-criterion predictions; criterion ID cited in prose only | V-03 single: per-criterion score prediction block (pass/partial/fail + mechanism) required in variation header before body is written |

This table is the isolation reference. Only the committed axis changes per variation; all
other axes hold at their baseline pole.

---

## R4 Variation Map with Pre-Generation Score Predictions (C-24)

Committed before any variation body is written. Do not revise after Phase 2 begins.

| V | Axis | Pass Type | Criteria Targeted | C-19 Pred | C-20 Pred | C-23 Pred | C-24 Pred |
|---|------|-----------|-------------------|-----------|-----------|-----------|-----------|
| V-01 | output-format | single-axis | C-19 | up: four sub-fields structurally enforce all four C-19 parts | no-change: one failure condition per variation | no-change: no phase restructuring | no-change: no pre-generation prediction block |
| V-02 | lifecycle-emphasis | single-axis | C-23, C-24 | no-change: hypothesis prose unchanged | no-change: failure condition count unchanged | up: labeled phases with declared responsibilities added | up: score prediction sub-stage in Phase 1 requires per-criterion directional commitments before Phase 2 |
| V-03 | scoring-granularity | single-axis | C-24 | partial: criterion-target field present via prediction block, but mechanism and failure-condition sub-fields not separately enforced | no-change: one prediction per criterion, not dual failure conditions | no-change: no phase restructuring | up: per-criterion prediction block required in header before body written |
| V-04 | role-sequence x inertia-framing | combination (R3 P1) | C-01, C-15, C-20 | up: champion-failure targeting grounds hypotheses in named failure mechanisms enabling four-part structure | up: outcome failure from champion inventory + implementation failure from gate-position enforcement = dual distinct conditions | up: phased structure inherited from champion; role additions labeled per phase | partial: champion inventory provides pre-generation context but no criterion-keyed directional table |
| V-05 | output-format x scoring-granularity | combination (R3 P2) | C-19, C-24 | up: four-part hypothesis sub-fields (V-01 R4) combined with prediction block ensures all C-19 parts present | partial: four-part format adds failure-condition sub-field but does not require a second mechanistically-distinct condition | up: phased structure inherited; commitment phase includes both envelope and prediction block | up: per-criterion prediction block committed in Phase 1 before any body written |

---

## V-01 -- Output Format: Four-Part Hypothesis Schema

**axis:** output-format
**criterion-targeted:** C-19 -- "Structured four-part hypothesis schema: at least one variation's
hypothesis field is composed of all four named parts: criterion-target, directional prediction,
causal mechanism, and explicit failure condition." Mechanism: splitting the prose `hypothesis:`
field into four labeled sub-fields makes each part a required declaration -- a generator cannot
produce a blank `mechanism:` sub-field without it being structurally visible as an omission,
unlike a prose paragraph where mechanism and failure condition can blend together or one can
be absent without detection.

**hypothesis:**
- **criterion-target:** C-19
- **direction:** increases C-19 pass rates
- **mechanism:** because the four-part sub-field format requires each C-19 component to be a
  separately labeled, non-blank field in the variation header -- a hypothesis with a blank
  `failure-condition:` sub-field is visually and structurally detectable, whereas a prose
  `hypothesis:` paragraph that omits the failure condition is only detectable by close reading
  of content, not by structural inspection. The `criterion-target:` sub-field simultaneously
  satisfies C-14 by construction for every variation that uses this header format.
- **failure-condition:** if C-19 pass rate for variations generated with four-part sub-fields
  does not exceed C-19 pass rate for variations generated with prose `hypothesis:` paragraphs
  (any R3 variation, none of which used this sub-field format), the sub-field structure adds
  no completeness benefit over prose and should be merged with another axis rather than
  promoted as a standalone mechanism.

**baseline-delta:** the `hypothesis:` field in the variation header is replaced with four
labeled sub-fields: `criterion-target:`, `direction:`, `mechanism:`, and `failure-condition:`.
No other field changes.

**completeness-risk:** the `mechanism:` sub-field -- generators tend to compress mechanism
into the direction sentence, producing a `mechanism:` sub-field that is syntactically present
but substantively empty ("because this changes how the model generates output" rather than
naming the specific structural change and its causal pathway to the criterion).

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

STEP 1 -- SELECT AXES

Read the skill spec. Select {N} distinct axes from the canonical list, one per variation:

  role-sequence | output-format | lifecycle-emphasis |
  phrasing-register | inertia-framing | scoring-granularity

No two variations may share the same axis. List all {N} axes before proceeding to Step 2.

STEP 2 -- GENERATE VARIATION BODIES

For each axis selected in Step 1, write one complete variation body. Precede each body
with a variation header. The header is a commitment made before the body is written.
Fill every field before writing the body. No field may be blank.

Header format (all fields required):

```
variation: V-NN
axis: [axis name from canonical list]
pole: [one phrase -- the specific change this variation makes on this axis]
baseline-delta: [one sentence naming the single structural element that differs from the
                 baseline skill -- the one element that changes and nothing else]
completeness-risk: [the section of this variation body most at risk of omission]
criterion-target: [the rubric criterion ID (C-NN) this axis is designed to improve]
direction: [increases / decreases / stabilizes] [criterion name] pass rates
mechanism: [one or two sentences -- the specific structural pathway connecting this axis
            change to the criterion improvement. Name what changes, what that produces,
            and why it causes the criterion outcome]
failure-condition: [the specific observable outcome that would refute the mechanism --
                   must be criterion-keyed and state what prior-round baseline it must
                   exceed to constitute improvement. Format: "if [criterion] pass rate
                   does not exceed [comparison baseline], the mechanism is refuted."]
```

After completing the header, write the complete variation body. Every section. Every
instruction. No diffs. No cross-references to other variations. Every structural section
present. Do not advance to the next variation until this body is complete and all header
fields are filled.

Label format:

### V-NN -- [Axis Name: Pole Description]

[variation header -- all fields filled before body is written]

[COMPLETE SKILL BODY -- all sections, all steps, all instructions written in full]

STEP 3 -- FINDINGS

After all {N} bodies are written:

1. Variation summary:

| V | Axis | Pole | Criterion-Target | Direction | Baseline Delta |
|---|------|------|-----------------|-----------|----------------|

2. Header completeness check: for each variation, confirm every header field is non-blank.
   Flag any blank field and state which criterion it would cause to fail.

3. Failure condition audit: for each variation, confirm the `failure-condition:` field
   names a specific prior-round comparison baseline (not just "does not improve").
   Flag any failure condition without a named baseline.

4. Combination candidates: the two most promising axis pairings for a follow-up pass.
   For each candidate, state:
   - Which failure mode each axis targets (criterion ID).
   - What residual weakness remains after only the first axis is applied.
   - What criterion improvement is achievable only when both axes are simultaneously active.
   - Priority: HIGH / MEDIUM / LOW -- one sentence.

5. Evaluation order: rank all {N} variations from lowest evaluation cost to highest,
   with one-line rationale and any cross-round dependency noted as:
   round + variation label + metric name.

---

## V-02 -- Lifecycle Emphasis: Pre-Generation Score Prediction Phase

**axis:** lifecycle-emphasis
**criterion-targeted:** C-23 and C-24. C-23 -- "Phased prompt architecture: explicitly
numbered, labeled phase structure with declared responsibilities." C-24 -- "Pre-generation
variation score predictions: planning phase includes per-variation criterion predictions
before generation begins." Mechanism: inserting a mandatory prediction sub-stage inside
Phase 1 (before Phase 2 opens) creates a structural phase boundary that generation cannot
cross without having committed directional per-criterion predictions per variation. The phase
labeling makes the commitment point explicit, satisfying C-23's requirement for declared phase
responsibilities. Together, the phase container and the prediction sub-stage address C-23
and C-24 jointly without requiring a separate role or format change.

**hypothesis:**
- **criterion-target:** C-24 (primary); C-23 (secondary)
- **direction:** increases C-24 and C-23 pass rates
- **mechanism:** because Phase 1 is divided into two sub-stages -- (1A) axis selection and
  (1B) per-variation score predictions -- with Phase 2 barred from opening until both are
  complete. The phase boundary is an enforcement mechanism: a generator that begins writing
  variation bodies without committing predictions is structurally in the wrong phase. The
  labeled phase structure also satisfies C-23's requirement for a commitment/planning phase
  with declared responsibilities distinct from the generation phase.
- **failure-condition:** if C-24 pass rate does not exceed zero (C-24 was not tested as a
  target in any R3 single-axis variation -- R3 V-05 combination included per-criterion
  predictions as part of the scoring-granularity axis, not the lifecycle-emphasis axis) and
  C-23 pass rate does not improve over any R3 variation (none of which used an explicitly
  labeled, numbered phase structure with named transition points), the expanded Phase 1
  sub-stage adds no structural commitment benefit and lifecycle-emphasis should remain a
  combination-only axis for C-24 targeting.

**baseline-delta:** Phase 1 is divided into sub-stage 1A (axis selection) and sub-stage 1B
(per-variation score predictions); Phase 2 cannot begin until both sub-stages are complete.
No other lifecycle change.

**completeness-risk:** the score prediction table in sub-stage 1B -- generators tend to write
"pass" for all criteria without mechanism sentences, which is structurally present but
substantively empty and would not satisfy C-24's requirement for per-criterion directional
predictions with mechanism.

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

PHASE 1 -- COMMIT AXES AND SCORE PREDICTIONS

Phase 1 has two sub-stages. Phase 2 does not begin until both are complete.

Sub-stage 1A -- Axis selection.

Select {N} distinct axes from the canonical list. Use each once:

  role-sequence | output-format | lifecycle-emphasis |
  phrasing-register | inertia-framing | scoring-granularity

List all {N} axes now. Do not proceed to 1B until the axis list is complete and each
axis appears exactly once.

Sub-stage 1B -- Score predictions.

Before writing any variation body, commit directional score predictions per criterion
per variation. Fill the prediction table below. Every cell must contain a verdict
(up / down / no-change) and a one-sentence mechanism. A blank or verdict-only cell
is not complete.

| V | Axis | C-01 Completeness | C-03 Axis Declaration | C-04 Isolation | C-07 Hypothesis Quality | C-09 Combination Readiness |
|---|------|-------------------|-----------------------|----------------|-------------------------|---------------------------|
[Fill all {N} rows. Each cell: verdict + one sentence on why that criterion moves in
that direction for this specific axis change.]

Phase 1 review before Phase 2:
- Every axis is distinct and appears in the canonical list.
- Every prediction cell has a verdict and a mechanism sentence.
- No variation body has been written yet.

Commit. Phase 2 begins.

PHASE 2 -- GENERATE VARIATION BODIES

For each axis committed in Phase 1, write one complete variation body.
Read the axis from the committed table. Do not revise axis assignments.

Label format:

### V-NN -- [Axis Name]

```
axis: [axis name -- matches Phase 1 committed axis]
hypothesis: [falsifiable prediction -- names the rubric criterion, direction, mechanism,
             and explicit failure condition. The failure condition must name the specific
             prior-round comparison baseline it must exceed to constitute improvement.]
baseline-delta: [one sentence -- the single structural element that changes and nothing else]
```

[COMPLETE SKILL BODY -- every section, every instruction, fully written.
 No diffs. No cross-references to other variations. Every structural section present.]

Do not begin the next variation until the current body is complete.

PHASE 3 -- FINDINGS

Declared responsibility: synthesize, compare score predictions to actual variation structures,
identify combination candidates, establish evaluation order.

1. Score prediction calibration:

| V | Axis | C-07 Predicted | C-07 Actual Structure | Prediction Correct? | Mis-prediction Mechanism |
|---|------|---------------|-----------------------|---------------------|--------------------------|

2. Combination candidates: two axis pairings from this run.
   For each candidate:
   - Which failure modes each axis targets (cite criterion IDs).
   - What residual weakness remains after only the first axis is applied.
   - What criterion improvement requires both axes active simultaneously (name the criterion ID).
   - Priority: HIGH / MEDIUM / LOW -- one sentence.

3. Evaluation order: rank all {N} variations from lowest evaluation cost to highest.
   For each variation state: cost, independence, cross-round dependency
   (format: round label + variation label + metric, or "none").

4. Anchor: one variation designated as the structural anchor for combination runs.
   Justify against: (a) structural impact, (b) isolation quality, (c) detectable failure
   condition -- one sentence each.

---

## V-03 -- Scoring Granularity: Per-Criterion Prediction Block Required

**axis:** scoring-granularity
**criterion-targeted:** C-24 -- "Pre-generation variation score predictions: the output
includes a variation map that predicts, for each planned variation, which rubric criteria
are expected to improve and in which direction. A champion inventory without per-variation
criterion predictions does not pass." Mechanism: requiring a per-criterion score prediction
block as a named field in each variation header -- filled before the body is written --
creates a structural pre-commitment that cannot be bypassed: a header with a blank
`score-prediction:` block cannot advance to body-writing, just as a blank `axis:` field
would fail C-03.

**hypothesis:**
- **criterion-target:** C-24
- **direction:** increases C-24 pass rates
- **mechanism:** because the prediction block is a required field in the variation header,
  filled before the body is written. The block must contain a verdict (pass/partial/fail)
  and a one-sentence mechanism for each of five rubric criteria. A header with any blank
  prediction cell is structurally incomplete in the same way a blank `axis:` field is
  structurally incomplete -- the format enforcement applies pre-generation rather than as
  a post-generation review.
- **failure-condition:** if C-24 pass rate does not improve over zero when evaluated against
  any R3 single-axis variation (R3 V-01 through V-03 -- none of which required per-criterion
  prediction blocks in variation headers; R3 V-05 included predictions but only as a
  combination-pass element not as a required header field in single-axis bodies), the
  per-criterion header block adds no pre-commitment benefit that directional prose hypotheses
  cannot achieve, and scoring-granularity should remain a combination-only axis.

**baseline-delta:** each variation header gains a `score-prediction:` block with five required
criterion rows (C-01, C-03, C-04, C-07, C-09), each requiring verdict + mechanism sentence,
filled before the body is written. No other header field changes.

**completeness-risk:** the `score-prediction:` block's C-07 row -- generators tend to write
"pass -- hypothesis quality improves" as the mechanism, which is circular reasoning rather
than a mechanism statement. The mechanism must name what structural element of this specific
axis change causes C-07 to behave differently.

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

STEP 1 -- SELECT AXES

Read the skill spec. Select {N} distinct axes from the canonical list, one per variation:

  role-sequence | output-format | lifecycle-emphasis |
  phrasing-register | inertia-framing | scoring-granularity

No two variations may share the same axis. List all {N} axes before proceeding to Step 2.

STEP 2 -- GENERATE VARIATION BODIES

For each axis selected in Step 1, write one complete variation body. Precede each body
with a variation header. The header is a commitment made before the body is written.
Every field in the header must be filled before writing the body.

Header format (all fields required):

```
variation: V-NN
axis: [axis name from canonical list]
pole: [one phrase -- the specific change this variation makes on this axis]
baseline-delta: [one sentence -- the single structural element that changes and nothing else]
completeness-risk: [the section most at risk of omission in this specific body]
hypothesis: [falsifiable prediction -- names the rubric criterion, direction, mechanism,
             and an explicit failure condition naming the specific prior-round baseline
             it must exceed]
score-prediction:
  C-01 completeness:     [pass / partial / fail] -- [one sentence: what about this axis
                          change causes completeness to hold or fail?]
  C-03 axis-declaration: [pass / partial / fail] -- [one sentence: declaration risk for
                          this specific axis]
  C-04 isolation:        [pass / partial / fail] -- [one sentence: contamination risk --
                          what other axis might this variation accidentally change?]
  C-07 hypothesis:       [pass / partial / fail] -- [one sentence: name the structural
                          mechanism in this body that produces or fails hypothesis quality.
                          Do not write "hypothesis quality improves" -- name the mechanism.]
  C-09 combination:      [pass / partial / fail] -- [one sentence: does this axis change
                          improve or reduce combination readiness? Why?]
```

After completing the header (all fields filled, score-prediction block complete), write
the complete variation body. Every section. Every instruction. No diffs. No cross-
references to other variations. Every structural section present. Do not advance to the
next variation until the current body is complete and every header field is filled.

Label format:

### V-NN -- [Axis Name: Pole Description]

[variation header -- all fields filled, score-prediction block complete]

[COMPLETE SKILL BODY -- all sections, all instructions, fully written]

STEP 3 -- FINDINGS

After all {N} bodies are written:

1. Variation summary:

| V | Axis | Pole | Criterion Targeted | C-04 Risk | Score Prediction Calibration |
|---|------|------|-------------------|-----------|------------------------------|

"Score Prediction Calibration": for each variation, state whether the C-07 prediction
was correct. If wrong, name the mechanism of the mis-prediction in one sentence.

2. Combination candidates: the two most promising axis pairings.
   For each candidate, state:
   - Which failure modes each axis targets (criterion ID per axis).
   - Residual weakness after only the first axis's improvement is applied.
   - Criterion improvement achievable only when both axes are active simultaneously (name C-NN).
   - Priority: HIGH / MEDIUM / LOW -- one sentence.

3. Evaluation order: rank all {N} variations from lowest evaluation cost to highest.
   For each: cost, independence, cross-round dependency (round + variation + metric, or "none").

4. Anchor: one variation. Justify against structural impact, isolation quality, and
   detectable failure condition -- one sentence each.

---

## V-04 -- Combination: Role Sequence x Inertia Framing

**axis:** role-sequence x inertia-framing
**pass-type:** combination (R3 Priority 1 -- V-02 R3 Loop-Gate Verifier x V-03 R3 Champion-Challenger Framing)
*C-04 exception explicitly invoked.*

**hypothesis:** Combining champion-challenger framing (V-03 R3, inertia-framing axis: champion
declared with three named failure modes; every variation hypothesis argues against one named
failure) with a Loop-Gate Verifier role (V-02 R3, role-sequence axis: fires per body, checks
C-01 and C-04 before advancing) increases C-20 (dual mechanistically-distinct failure conditions)
because:
- **criterion-target:** C-20
- **direction:** increases C-20 pass rates beyond what either axis achieves alone
- **mechanism:** the champion inventory produces outcome-failure conditions by construction --
  a hypothesis that argues against "the champion fails to name a criterion ID in its failure
  condition" has a natural outcome-failure statement ("if this variation does not improve C-11
  pass rates, the champion's failure mode persists"). The Loop-Gate Verifier adds an
  implementation-failure condition by a distinct mechanism -- a gate that fires in the wrong
  position (post-generation rather than per-body) would independently fail C-15, naming C-15
  as the second failure mode. Together, the combination produces hypotheses with two failure
  conditions that are mechanistically distinct (outcome failure sourced from champion inventory;
  implementation failure sourced from gate-position enforcement) -- neither axis produces this
  dual structure alone.
- **failure-condition (outcome):** if C-20 pass rate does not exceed zero (C-20 was not achieved
  in any R3 variation -- R3 V-02 loop-gate single-axis produced one failure condition per
  hypothesis, not two mechanistically-distinct ones), the champion-inventory + gate-position
  mechanism does not produce the dual-failure structure, and these axes should remain
  independent with single-failure-condition hypotheses.
- **failure-condition (implementation):** if the Loop-Gate Verifier in this combination is
  implemented as a post-generation review of all bodies rather than a per-body gate that fires
  before advancing, this combination independently fails C-15 -- the gate-position enforcement
  mechanism that produces the implementation-failure condition does not exist, and the C-20
  dual-failure claim collapses to a C-11 single-failure claim regardless of whether C-20 pass
  rate improves.

---

**Combination pass: role-sequence x inertia-framing**
*C-04 exception explicitly invoked. Champion-challenger framing (inertia-framing axis) and
Loop-Gate Verifier role (role-sequence axis) are both active in the generation scaffolding.
The generated variations are still single-axis -- each challenger changes one axis from the
target skill's champion. The combination applies to the generation process structure, not to
the variations themselves.*

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis from
the champion.

PHASE 1 -- DECLARE THE CHAMPION

The current skill body is the status-quo champion. Before writing any variation, produce
the champion inventory.

Part A -- Champion strengths: the three rubric criteria the champion most reliably passes
and the structural mechanism producing each pass. Be specific about mechanism -- not
"the champion produces complete bodies" but "the champion's per-body completeness check
fires immediately after each body while generation context is active."

Part B -- Champion failure inventory: the three most significant rubric criteria the
champion struggles with, the structural mechanism producing each weakness, and the
criterion ID that measures it.

| Champion Failure # | Criterion ID | Criterion Name | Failure Mechanism |
|--------------------|--------------|----------------|-------------------|
| CF-1 | | | |
| CF-2 | | | |
| CF-3 | | | |

The failure inventory is the hypothesis brief. Every challenger hypothesis must name the
Champion Failure # it targets and state what outcome-failure condition would prove the
champion is still preferable on that criterion.

PHASE 2 -- GENERATE CHALLENGERS

--- ROLE: GENERATOR ---

Write V-01 through V-{N}. Each challenger is a complete, standalone skill body that
changes exactly one axis from the champion.

Canonical axes: role-sequence | output-format | lifecycle-emphasis |
                phrasing-register | inertia-framing | scoring-granularity

No two challengers may share the same axis. List all {N} axes before writing any body.

Label format:

### V-NN -- [Axis: Champion Failure Targeted]

```
axis: [axis name from canonical list]
champion-failure-targeted: [CF-# from the inventory -- must match exactly]
hypothesis:
  criterion-target: [C-NN by ID]
  direction: [increases / decreases] [criterion name] pass rates
  mechanism: [one or two sentences -- what the champion cannot do on this criterion,
              what this challenger does instead, and why the mechanism produces the
              criterion outcome]
  failure-condition-outcome: [the specific observable outcome that would prove the
                              champion still preferable on the targeted criterion.
                              Must be more specific than "does not improve C-NN" --
                              name the prior-round comparison baseline.]
  failure-condition-implementation: [the specific observable outcome that would prove
                                     this challenger's mechanism was instantiated
                                     incorrectly even if the outcome metric is met.
                                     Must name a separate criterion ID that this
                                     implementation failure would independently violate.]
```

[COMPLETE SKILL BODY -- all sections, all instructions, fully written.
 No diffs. Every section present. No cross-references to other variations.]

A hypothesis that describes only what this challenger does, without naming a CF-# from
the inventory, is invalid. Rewrite before advancing.

--- ROLE: LOOP-GATE VERIFIER ---

The Loop-Gate Verifier fires after the Generator writes each challenger body, before the
Generator begins the next challenger. The Generator does not advance until the Loop-Gate
Verifier issues a PASS.

CHECK C-01 COMPLETENESS: Is the body full and standalone? Every section present? No
placeholders or ellipses? If not: state the missing section. Generator must complete it.

CHECK C-04 ISOLATION: Does the body change exactly the one axis named in the header?
If a second element changed, name the contamination. Generator must revert it.

CHECK HYPOTHESIS DUAL-FAILURE: Does the hypothesis contain both `failure-condition-outcome:`
and `failure-condition-implementation:` sub-fields, each non-blank? Does `failure-condition-
implementation:` name a separate criterion ID? If not: state which sub-field is missing
or incomplete. Generator must complete it before advancing.

Issue verdict: PASS or FAIL with required fixes listed. Generator advances only on PASS.

The Gate fires per body, inside the loop:
- After V-01 is written, before V-02 begins.
- After V-02 is written, before V-03 begins.
- And so on through V-{N}.

PHASE 3 -- FINDINGS

Declared responsibility: challenger map, combination candidates, evaluation order.

1. Challenger map:

| V | Axis | CF-# Targeted | C-04 Risk | Dual Failure Conditions Present? | Loop-Gate Verdict |
|---|------|---------------|-----------|----------------------------------|-------------------|

2. Combination candidates with compound-effects model.
   For each candidate, state all four sub-elements -- omit any candidate for which you
   cannot complete all four:
   - **Failure modes per axis** (criterion ID per axis, semicolon-separated).
   - **Residual weakness after first axis only** (specific gap, not a restatement of
     the second axis's improvement).
   - **Compound criterion effect (both active)** -- name the criterion ID(s).
   - **Priority**: HIGH / MEDIUM / LOW -- one sentence.

   Combination roadmap table:

   | Priority | Axis Pair | V-NN Basis | Failure Modes Per Axis | Residual Weakness | Compound Criterion Effect | Criteria Targeted |
   |----------|-----------|------------|------------------------|-------------------|--------------------------|-------------------|

3. Evaluation order: rank all {N} challengers from lowest evaluation cost to highest.
   For each: cost, independence, cross-round dependency (round + variation + metric, or "none").

---

## V-05 -- Combination: Output Format x Scoring Granularity

**axis:** output-format x scoring-granularity
**pass-type:** combination (R3 Priority 2 -- V-01 R3 Structured Envelope x Scoring-Granularity uncovered single-axis)
*C-04 exception explicitly invoked.*

**hypothesis:** Combining the four-part hypothesis sub-field format (V-01 R4, output-format
axis: `criterion-target:`, `direction:`, `mechanism:`, `failure-condition:` as separately
labeled required fields) with a per-criterion score prediction block (V-03 R4, scoring-granularity
axis: prediction block required in header before body is written) increases C-19 and C-24 jointly:
- **criterion-target:** C-19 (primary), C-24 (secondary)
- **direction:** increases C-19 and C-24 pass rates beyond what either axis achieves alone
- **mechanism:** the four-part sub-field format structurally enforces all four C-19 components
  as separate required fields (criterion-target, direction, mechanism, failure-condition) --
  none can be silently omitted. The per-criterion prediction block commits directional outcome
  expectations per criterion before the body is written -- directly satisfying C-24's
  "per-variation criterion predictions" requirement. Together: the sub-field format closes the
  structural-completeness gap at the hypothesis level (C-19), and the prediction block closes
  the pre-generation commitment gap at the evaluation level (C-24). V-01 R4 alone satisfies
  C-19 but not C-24 (no prediction block); V-03 R4 alone satisfies C-24 but not C-19 (no
  four-part sub-field structure). The combination is the only R4 configuration that achieves
  both in one pass.
- **failure-condition (outcome):** if C-19 and C-24 pass rates do not jointly exceed those
  achieved by V-01 R4 alone (output-format single-axis, where C-19 was the primary target) and
  V-03 R4 alone (scoring-granularity single-axis, where C-24 was the primary target), the
  combination provides no compound benefit and these axes should be carried forward as
  independent single-axis variations in R5 rather than promoted as a combination.
- **failure-condition (implementation):** if the four-part sub-field format and the prediction
  block are implemented in conflicting positions -- e.g., the prediction block appears after
  the body is written rather than before -- the scoring-granularity axis's pre-generation
  enforcement mechanism is violated, independently failing C-24 regardless of whether the
  four-part sub-fields are structurally complete. This implementation failure would leave
  C-24 unsatisfied while C-19 might pass, which is a distinct failure mode from outcome
  failure and names C-24 as the independently violated criterion.

---

**Combination pass: output-format x scoring-granularity**
*C-04 exception explicitly invoked. Four-part hypothesis sub-field format (output-format axis)
and per-criterion score prediction block (scoring-granularity axis) are both active in the
variation header format. The generated variations are still single-axis -- each changes one
axis from the baseline skill. The combination applies to the header format required for each
variation, not to the variations themselves.*

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

PHASE 1 -- COMMIT AXES AND VARIATION HEADERS

Phase 1 has two sub-stages. Phase 2 does not begin until both are complete.

Sub-stage 1A -- Axis selection.

Select {N} distinct axes from the canonical list. Use each once:

  role-sequence | output-format | lifecycle-emphasis |
  phrasing-register | inertia-framing | scoring-granularity

List all {N} selected axes now. Do not proceed to 1B until the axis list is complete
with no duplicates.

Sub-stage 1B -- Variation header commitment.

Before writing any variation body, commit a full variation header for each of the {N}
selected axes. The header must be complete before Phase 2 begins. Every field required.

Header format (all fields required -- no field may be blank):

```
variation: V-NN
axis: [axis name -- must match Phase 1A committed axis]
pole: [one phrase -- the specific change this variation makes on this axis]
baseline-delta: [one sentence naming the single structural element that changes]
completeness-risk: [the section most at risk of omission in this specific body]
criterion-target: [C-NN by ID]
direction: [increases / decreases / stabilizes] [criterion name] pass rates
mechanism: [the specific structural pathway from this axis change to the criterion outcome.
            Name what changes, what that produces structurally, and why it causes the
            criterion to move in the declared direction. Do not write "quality improves"
            -- name the mechanism.]
failure-condition: [the specific observable outcome that would refute this mechanism.
                   Must name the prior-round comparison baseline: if [criterion] pass
                   rate does not exceed [V-NN R-N result], the mechanism is refuted.]
score-prediction:
  C-01 completeness:     [pass / partial / fail] -- [one sentence mechanism]
  C-03 axis-declaration: [pass / partial / fail] -- [one sentence mechanism]
  C-04 isolation:        [pass / partial / fail] -- [name the contamination risk for
                          this specific axis; "no risk" is valid if justified]
  C-07 hypothesis:       [pass / partial / fail] -- [name the structural element in
                          this body that produces or fails hypothesis quality. Do not
                          write "improves" -- name the mechanism.]
  C-09 combination:      [pass / partial / fail] -- [one sentence mechanism]
```

Review all {N} headers before Phase 2:
- Every axis is distinct and from the canonical list.
- Every `criterion-target:` names a criterion ID.
- Every `failure-condition:` names a specific prior-round baseline.
- Every `score-prediction:` cell has a verdict and a mechanism sentence -- no blank cells.
- Every `mechanism:` field names a structural pathway, not an outcome restatement.

Commit. Do not revise axis assignments after Phase 2 begins.

PHASE 2 -- GENERATE VARIATION BODIES

For each committed header, write the complete variation body. Read the axis from the
committed header. Do not revise the header. Do not change the axis mid-generation.

For each body, apply isolation:
- Step A: Read the committed axis from Phase 1B.
- Step B: Name every other axis that might tempt a change. Freeze each explicitly.
- Step C: Change only the committed axis. Write the full body -- every section, every
  instruction. No diffs. No cross-references to other variations.

Label format:

### V-NN -- [Axis: Pole Description]

[variation header from Phase 1B -- do not revise]

[COMPLETE SKILL BODY -- all sections, all instructions, fully written]

Do not begin the next variation until the current body is complete. Confirm the
`completeness-risk:` section named in the header is present and fully written in the body.

PHASE 3 -- FINDINGS

Declared responsibility: calibrate predictions, identify combination candidates, set
evaluation order, designate anchor.

1. Score prediction calibration:

| V | Axis | C-07 Predicted | C-07 Structure Actually Present | Prediction Correct? | Mis-prediction Mechanism |
|---|------|---------------|---------------------------------|---------------------|--------------------------|

For each wrong prediction, state in one sentence why the structural element in the body
did not behave as the mechanism predicted.

2. Combination candidates (compound-effects model):

| Priority | Axis Pair | V-NN Basis | Failure Modes Per Axis | Residual Weakness After First Axis Only | Compound Criterion Effect (Both Active) | Criteria Targeted |
|----------|-----------|------------|------------------------|-----------------------------------------|-----------------------------------------|-------------------|

Column rules:
- **V-NN Basis**: name the specific Phase 1B headers that motivate the pairing.
- **Failure Modes Per Axis**: one clause per axis, citing the criterion ID.
- **Residual Weakness After First Axis Only**: a concrete gap, not a restatement.
- **Compound Criterion Effect**: must name a criterion ID; must be distinct from what
  either axis achieves alone.

A row with any blank column is omitted from the table.

Priority rationale: one sentence per HIGH or MEDIUM row after the table.

3. Evaluation order: rank all {N} variations from lowest evaluation cost to highest.

| Priority | V | Axis | Cost | Independence | Cross-Round Dependency | Sequencing Rationale |
|----------|----|------|------|--------------|------------------------|----------------------|

Cross-round dependency format: "R[round] / V-NN / [metric name]" or "none."

4. Anchor: one variation designated as the structural anchor for combination runs.
   Justify against: (a) structural impact, (b) isolation quality, (c) detectable failure
   condition -- one sentence each.

---

## Axis Tension Note (C-13 -- before combination roadmap)

**Tension: output-format x scoring-granularity (V-05)**

The four-part hypothesis sub-field format (output-format, V-01 R4) structures the hypothesis
at the declaration level -- fields are separated before the body is written. The per-criterion
prediction block (scoring-granularity, V-03 R4) structures the evaluation at the prediction
level -- verdicts are committed per criterion before the body is written. Both mechanisms
operate pre-body. The risk: a generator that fills the hypothesis sub-fields and then fills
the prediction block may be expressing the same information twice in different formats,
producing apparent compliance with both C-19 and C-24 without adding independent commitment
value. The prediction block's C-07 row may simply restate the hypothesis `direction:` field
in a different format.

**Dominant axis prediction: output-format will dominate.** The four-part sub-field format
enforces C-19 structural compliance regardless of whether a prediction block is present.
The prediction block adds C-24 compliance (per-criterion directionality before generation)
but may not add C-19 compliance beyond what the sub-fields already enforce. If V-01 R4
alone achieves C-19 and V-05 does not achieve C-24 beyond what V-03 R4 achieves alone,
the combination is redundant on the scoring-granularity axis side.

**Tension: role-sequence x inertia-framing (V-04)**

The Loop-Gate Verifier (role-sequence) fires post-body -- inside the loop. The champion
inventory (inertia-framing) fires pre-body -- before any variation is written. They operate
at opposite lifecycle positions, providing front-and-back coverage. However, the two failure
condition types they produce (implementation failure from gate position; outcome failure from
champion failure inventory) may not be independently observable in a single evaluation run:
if the Gate fires on a body that would have passed C-01 anyway, the implementation-failure
condition is never activated, and the C-20 dual-failure structure exists in the hypothesis
but was never tested.

**Dominant axis prediction: inertia-framing will dominate.** The champion inventory grounds
hypothesis specificity (C-07, C-20 outcome-failure) before any body is written. If the
inventory alone produces hypotheses with two distinct failure types by the nature of
competitive argumentation, the Gate's addition adds enforcement overhead without adding
failure-condition depth beyond what the inventory's structural logic already produces.

---

## Combination Roadmap for Round 5 (C-09, C-22)

| Priority | Axis Pair | R4 Basis | Failure Modes Per Axis | Residual Weakness After First Axis Only | Compound Criterion Effect (Both Active) | Criteria Targeted |
|----------|-----------|----------|------------------------|-----------------------------------------|-----------------------------------------|-------------------|
| 1 | output-format x role-sequence | V-01 R4 (four-part sub-field format targets C-19 by structural enforcement) x V-04 R4 (champion-challenger + loop-gate targets C-20 by dual failure condition production) | output-format: hypothesis fields lack four-part structural sub-division, C-19 fails because mechanism and failure-condition blend into prose; role-sequence: loop-gate catches C-01 and C-04 but produces only implementation-failure conditions -- outcome-failure conditions require the inertia-framing axis to supply champion inventory | After output-format alone: C-19 passes (four sub-fields present), but C-20 fails -- the four-part format adds a `failure-condition:` sub-field but does not require two mechanistically-distinct conditions; only one failure condition is present per hypothesis | After both active: the four-part format's `failure-condition:` sub-field combined with the Loop-Gate Verifier's per-body position check produces a header format where the `failure-condition:` sub-field is expected to carry an outcome failure (from the hypothesis argument) AND the gate's implementation-failure check adds a second condition by structural necessity -- the only configuration that produces C-19 (four-part completeness) and C-20 (dual-failure distinction) in the same header | C-19 structured four-part hypothesis schema, C-20 dual mechanistically-distinct failure conditions |
| 2 | lifecycle-emphasis x scoring-granularity | V-02 R4 (Phase 1 expanded to include score prediction sub-stage, C-23 and C-24) x V-03 R4 (per-criterion prediction block required in variation header, C-24) | lifecycle-emphasis: Phase 1B sub-stage enforces that no variation body is written before predictions are committed -- C-24 enforcement at phase boundary level; scoring-granularity: prediction block in variation header enforces C-24 at the field level -- same criterion, two enforcement positions | After lifecycle-emphasis alone: C-23 (phased architecture) and C-24 (pre-generation predictions in phase table) both improve, but the phase-level table in Phase 1B is not the same commitment artifact as a per-variation prediction block in the variation header -- C-24 requires per-variation criterion predictions, which the Phase 1B table provides but not in the same per-header format that V-03's block provides | After both active: the Phase 1B commitment table (lifecycle-emphasis axis) and the per-variation header block (scoring-granularity axis) enforce C-24 at two levels -- phase-boundary level (cannot enter Phase 2 without the table) and field-boundary level (cannot write a body without filling the block) -- double enforcement that reduces the risk of a generator writing bodies with an unfilled or incomplete prediction record compared to either enforcement point alone | C-23 phased prompt architecture, C-24 pre-generation variation score predictions |

Priority rationale: Candidate 1 is HIGH because C-19 and C-20 are both v4 additions targeting
hypothesis-level structural completeness -- the compound effect tests whether a single header
format can satisfy both criteria simultaneously, which is the most direct test of v4's
structural requirements. Candidate 2 is MEDIUM because C-23 and C-24 both target the
commitment phase (same lifecycle position), making their compound effect less clearly
distinguishable than Candidate 1's cross-lifecycle combination.

---

## Anchor Designation

**Designated anchor: V-03 (scoring-granularity: Per-Criterion Prediction Block Required)**

- **High structural impact**: V-03 adds a per-criterion score prediction block as a required
  field in every variation header -- a structural change to the header format that applies to
  all {N} variations in a single run and directly targets C-24 (pre-generation criterion
  predictions), which was not satisfied by any R3 single-axis variation. A format change that
  adds a required commitment field per variation at header-scope is the highest-impact
  single-axis change for C-24 because it applies before the body is written, preventing
  post-hoc construction.

- **Clean isolation**: The only change from the baseline is the addition of the `score-
  prediction:` block with five required criterion rows in the variation header. No roles
  added, no lifecycle phases inserted, no register changes, no hypothesis field restructuring.
  The single-axis delta is verifiable by structural diff: prediction block with five criterion
  rows present in header, or absent.

- **Detectable failure**: The C-24 target is observable within one run without multi-round
  comparison: if any variation header has a blank `score-prediction:` cell, or a cell with
  only a verdict and no mechanism sentence, C-24 fails on its own terms. This is checkable
  per-cell, per-variation, per-run -- no prior-round scoring result is required.

V-03 is the anchor for all R5 combination runs. Both R5 candidates (output-format x
scoring-granularity and lifecycle-emphasis x scoring-granularity) hold V-03's prediction
block requirement stable and add a second axis.

---

## Evaluation Order Guidance (C-12)

| Priority | Variation | Axis | Evaluation Cost | Independence | Cross-Round Dependency | Sequencing Rationale |
|----------|-----------|------|-----------------|--------------|------------------------|----------------------|
| 1 | V-01 | output-format (four-part hypothesis sub-fields) | Low -- format change to variation header only; no role or phase additions; C-19 is checkable per-field per-variation | Independent | None -- C-19 compliance is determined by whether all four sub-fields are present and non-blank; no prior-round result required | Cheapest to evaluate, fully self-contained. Establishes the output-format/four-part-schema single-axis baseline that R5 Candidate 1 (output-format x role-sequence) must exceed on C-19. |
| 2 | V-03 | scoring-granularity (per-criterion prediction block) | Low -- adds one structured block to the variation header; C-24 is checkable per-cell per-variation within one run | Independent | None -- C-24 compliance is determined by whether the prediction block is present, complete, and filled before the body is written; no prior-round result required | Evaluate before V-05: V-03's C-24 single-axis result is the comparison denominator for V-05's failure-condition-outcome ("does not jointly exceed V-03 R4 alone on C-24"). Result must be established before V-05 is run. |
| 3 | V-02 | lifecycle-emphasis (pre-generation score prediction phase) | Medium -- adds a Phase 1B sub-stage with a prediction table; evaluating C-23 requires confirming the phase labels and declared responsibilities are present; evaluating C-24 requires confirming the prediction table is populated before any body is written | Partially independent | Partial dependency on V-03 R4: V-02's C-24 claim via Phase 1B is most informative once V-03's per-header C-24 result is known, since R5 Candidate 2 (lifecycle-emphasis x scoring-granularity) requires both single-axis baselines to isolate the combination's compound contribution | Evaluate after V-01 and V-03. V-02's C-24 improvement claim is meaningful relative to V-03's C-24 single-axis result -- if V-03 fully satisfies C-24 via per-header blocks, V-02's Phase 1B sub-stage adds phase-structure compliance (C-23) but not additional C-24 coverage. |
| 4 | V-04 | role-sequence x inertia-framing (combination) | Medium-high -- two mechanisms active (champion inventory + loop-gate verifier); evaluating C-20 requires checking that both failure-condition-outcome and failure-condition-implementation sub-fields are present and mechanistically distinct per hypothesis; requires reading champion inventory to verify CF-# citations | Dependent on R3 V-02 and R3 V-03 baselines | Depends on R3 V-02 C-01 baseline and R3 V-03 C-07 baseline: V-04's compound claim (C-20 pass rate exceeds what loop-gate alone or champion-framing alone achieves) requires both single-axis R3 results to isolate the combination's contribution -- R3 / V-02 / C-01 pass rate; R3 / V-03 / C-07 pass rate | Evaluate after V-01 and V-03 are scored. V-04's C-20 outcome-failure condition ("does not exceed zero -- C-20 not achieved in any R3 single-axis variation") is the weakest verifiable bar in this round; evaluate as the first combination to determine whether the V-02 x V-03 combination produces C-20 at all. |
| 5 | V-05 | output-format x scoring-granularity (combination) | High -- two mechanisms active in header format (four-part sub-fields + prediction block); evaluating C-19 and C-24 jointly requires confirming both header structures are present, each complete, each filled before the body is written; most structurally dense header format in R4 | Dependent on V-01 R4 and V-03 R4 baselines | Depends on V-01 R4 (C-19 single-axis baseline) and V-03 R4 (C-24 single-axis baseline): V-05's failure-condition-outcome names both baselines -- "does not jointly exceed V-01 R4 alone on C-19 and V-03 R4 alone on C-24"; neither baseline can be declared without running V-01 and V-03 first | Evaluate last: V-05's compound claim is only verifiable after V-01 R4 C-19 result and V-03 R4 C-24 result are both established. If either single-axis variation already satisfies both criteria simultaneously, the combination adds no compound benefit and the implementation-failure condition ("scoring-granularity axis applied post-generation, independently failing C-24") becomes the only novel test. |
