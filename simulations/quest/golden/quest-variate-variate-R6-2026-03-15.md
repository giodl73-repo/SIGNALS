# quest-variate Variate — Round 6

**Date:** 2026-03-15
**Skill:** quest-variate
**Rubric:** v6 (C-01 through C-31; essential C-01–C-05)
**Round:** R6 — 3 single-axis passes + 2 combination passes (C-04 combination exception applies to V-04 and V-05)

---

## Pre-Generation: Per-Axis Pole Declaration (C-16)

Before any variation body is written, declare the baseline pole for each axis.

**Champion baseline:** the R5 V-05 body (role-sequence × lifecycle-emphasis combination) — a
three-phase generator with a standalone pre-phase `## VARIATION MAP` section (C-27) carrying a
"Do not revise after Phase 2 begins" instruction and a declaration that the AXIS-FREEZE PROTOCOL
reads axis assignments from this table (C-29). Phase 1 commits variation headers with a single
`failure-condition:` field per header. Phase 2 includes an AXIS-FREEZE PROTOCOL with six named
per-axis freeze declarations reading from the VARIATION MAP (C-26, C-29), a count-completeness
gate "A freeze list with fewer than six entries is incomplete — do not proceed" (C-28), and a
post-loop label "Verify VARIATION MAP axis matches Phase 1 header axis before advancing to
Phase 3." Phase 3 includes an axis alignment check table, prediction calibration, combination
candidates, evaluation order, and anchor. The VARIATION MAP rows carry per-variation criterion
direction predictions only — no failure-condition-type prediction columns (C-30 not satisfied).
The cross-artifact axis consistency check fires only in the Phase 3 axis alignment table (after
all bodies are written), not inside the Phase 2 generation loop before each body is written
(C-31 not satisfied). Phase 1 headers use a single `failure-condition:` field, not split into
dual named keys (C-25 not satisfied).

| Axis | Baseline Pole (Champion = R5 V-05) | R6 Committed Variation Pole |
|------|-----------------------------------|-----------------------------|
| output-format | Single `failure-condition:` field in each Phase 1 variation header — one field carries both outcome and implementation failure signals; C-25 not satisfied because dual mechanism signals are co-located in one field requiring prose parsing to distinguish | V-01 single: `failure-condition:` replaced with two distinct required keys — `failure-condition-outcome:` (what observable outcome refutes the axis claim) and `failure-condition-implementation:` (what implementation flaw independently violates a named separate criterion ID); structural detectability of C-20 by field presence alone |
| scoring-granularity | VARIATION MAP table carries per-variation per-criterion directional predictions (C-24 satisfied) but no failure-condition prediction columns — map commits what improves but not what breaks and how (C-30 not satisfied) | V-02 single: VARIATION MAP table gains two required columns per variation row — `failure-condition-outcome prediction` (expected failure signature if hypothesis produces no criterion improvement) and `failure-condition-implementation prediction` (expected failure signature if mechanism is wrong, naming the criterion independently violated) — extending the map from a "what improves" record to a "what breaks and how" record |
| lifecycle-emphasis | Cross-artifact axis consistency check fires in Phase 3 axis alignment table (post-generation, before combination candidates section) — not inside the Phase 2 AXIS-FREEZE PROTOCOL loop before each body is written; C-31 not satisfied because divergence is detectable only after the body has been written | V-03 single: AXIS-FREEZE PROTOCOL gains a Step 2B — cross-artifact axis consistency check — that fires after the six-entry freeze list and before Step 3 (body writing): state VARIATION MAP assigned axis for this V, state Phase 1 header declared axis for this V, halt with AXIS DIVERGENCE flag if they differ; divergence caught before the body is written |
| phrasing-register | Formal-technical imperative register; freeze declarations use "[FROZEN | COMMITTED — read from VARIATION MAP for this body]" format | Not tested single-axis R6; reserved for R7 |
| role-sequence | Named per-axis AXIS-FREEZE PROTOCOL reading from VARIATION MAP as authoritative source (C-26, C-28, C-29 all satisfied) | Not tested single-axis R6; held stable at R5 V-05 pole |
| inertia-framing | No champion declared; variations compared against abstract "baseline skill body" without naming a prior-round variation as comparison denominator in the generation scaffold | Not tested single-axis R6; deferred |

This table is the isolation reference. Only the committed axis changes per variation body; all
other axes hold at their baseline pole.

---

## VARIATION MAP — Immutable after Phase 2 begins (C-27, C-29, C-30)

**[AUTHORITATIVE SOURCE] The AXIS-FREEZE PROTOCOL in Phase 2 reads axis assignments from this
table. Do not revise after Phase 2 begins.**

| V | Axis | Pass Type | Criterion Target | Expected Direction | Mechanism Sketch | failure-condition-outcome prediction | failure-condition-implementation prediction |
|---|------|-----------|-----------------|-------------------|-----------------|--------------------------------------|----------------------------------------------|
| V-01 | output-format | single-axis | C-25 | C-25: up; C-20 structural detectability: up | Splitting `failure-condition:` into two required named keys makes C-20 compliance detectable by field presence — absent `failure-condition-implementation:` key signals C-20 violation without prose inspection | C-25 pass rate does not exceed R5 V-01 result; named-key split adds no detectability benefit over two sentences in one field if generators treat the split as cosmetic | `failure-condition-implementation:` fields describe the same mechanism as `failure-condition-outcome:` in different words, independently failing C-20 — detectable because the implementation key names no separate criterion ID |
| V-02 | scoring-granularity | single-axis | C-30 | C-30: up; C-24: no-change (direction predictions preserved, failure-condition type columns added as new requirement) | Failure-condition type columns extend the pre-generation VARIATION MAP from predicting criterion direction to pre-committing the expected failure signature per variation — makes the map verifiable against body failure conditions post-generation | C-30 pass rate does not exceed zero (C-30 was not targeted in any R5 single-axis pass); the two-column extension adds no pre-commitment value if generators treat the prediction columns as a post-hoc summary rather than a gate-enforced pre-commitment | Failure-condition prediction columns are populated but implementation column names the same failure mode as outcome column (no mechanistically distinct second mode), independently failing C-20 at the map level — map columns satisfy C-30 structural form but not C-20 content requirement |
| V-03 | lifecycle-emphasis | single-axis | C-31 | C-31: up; C-26 retention: up (named freeze and count gate preserved, step added inside loop) | Moving the axis consistency check from Phase 3 into the AXIS-FREEZE PROTOCOL before each body converts the check from a post-generation audit to a per-body pre-write gate — divergence between VARIATION MAP and Phase 1 header is caught before contamination enters the body | C-31 pass rate does not exceed zero (C-31 was not targeted in any R5 single-axis pass); the in-loop check adds no divergence-detection benefit if VARIATION MAP and Phase 1 headers are identical in practice (no divergence to catch) | The in-loop cross-artifact check fires but checks Phase 1 header axis against itself rather than against the VARIATION MAP, or the check label does not name "VARIATION MAP" explicitly — independently failing C-29 because the VARIATION MAP is no longer confirmed as authoritative source for the per-body enforcement |
| V-04 | output-format × lifecycle-emphasis | combination (R6 Priority 1 — V-01 R6 dual keys × V-03 R6 in-loop cross-artifact gate) | C-25, C-31 | C-25: up, C-31: up | Dual failure-condition keys in Phase 1 headers (output-format) combined with in-loop axis consistency gate (lifecycle-emphasis): the gate verifies that the header being populated with dual keys corresponds to the VARIATION MAP assignment before writing begins — prevents structurally-correct dual keys under the wrong axis | C-25 and C-31 pass rates do not jointly exceed V-01 R6 alone and V-03 R6 alone; combination provides no compound benefit over independent single-axis results | In-loop gate verifies axis consistency but does not check that `failure-condition-implementation:` in the verified header names a separate criterion ID — independently failing C-20 even though dual keys are structurally present and axis is confirmed correct |
| V-05 | scoring-granularity × lifecycle-emphasis | combination (R6 Priority 2 — V-02 R6 failure-condition prediction columns × V-03 R6 in-loop cross-artifact gate) | C-30, C-31 | C-30: up, C-31: up | Failure-condition prediction columns in VARIATION MAP (scoring-granularity) combined with in-loop axis consistency gate (lifecycle-emphasis): the gate verifies VARIATION MAP axis matches Phase 1 header axis before the body is written; the map's failure-condition predictions for that variation are already committed at document scope — three-level pre-commitment chain: map commits failure predictions at document scope, gate verifies axis consistency at loop scope, body is written under verified assignment | C-30 and C-31 pass rates do not jointly exceed V-02 R6 alone and V-03 R6 alone; three-level chain provides no compound benefit over independent single-axis results | The failure-condition prediction columns in the VARIATION MAP are populated and the in-loop gate fires but the gate does not reference the map's failure-condition predictions (verifies axis only), leaving the failure-condition predictions unlinked to the gate — independently failing C-29 because the VARIATION MAP is not fully authoritative: the gate reads axis assignments but ignores the failure-condition prediction content, creating a partial read-source relationship |

---

## V-01 — Output Format: Dual Failure Condition Keys

**axis:** output-format
**criterion-targeted:** C-25 — "When a hypothesis contains two failure conditions satisfying C-20,
each condition appears as a distinct named key — `failure-condition-outcome:` and
`failure-condition-implementation:` — rather than two sentences within a single
`failure-condition:` field. The separation makes C-20 compliance structurally detectable by field
presence." Mechanism: an absent or blank `failure-condition-implementation:` key is detectable by
structural inspection alone; two sentences inside a single `failure-condition:` field require
prose parsing to determine whether two mechanistically-distinct conditions are present. The key
heading also signals to the generator that the implementation-failure field must point to a
separate criterion ID, not restate the outcome failure.

**hypothesis:**
- **criterion-target:** C-25
- **direction:** increases C-25 pass rates; increases C-20 compliance detectability
- **mechanism:** because splitting `failure-condition:` into two required, distinctly named keys
  converts C-20 compliance from a content judgment (did the author write two distinct mechanisms
  in one field?) to a structural check (is `failure-condition-implementation:` non-blank and does
  it name a separate criterion ID?). A generator filling `failure-condition-implementation:` must
  write something identifying an implementation-specific failure mode and naming the criterion it
  would independently violate — the key heading itself rules out restating the outcome failure.
- **failure-condition-outcome:** if C-25 pass rate does not exceed R5 V-01 result (R5 V-01 was
  the first single-axis test of dual failure condition keys under the output-format axis), the
  dual-key format adds no detectability benefit over a single field with two sentences, and
  output-format should be pointed back at C-19 or C-24 as its primary criterion target in R7.
- **failure-condition-implementation:** if `failure-condition-implementation:` fields produced
  for this format describe the same mechanism as `failure-condition-outcome:` (restated in
  different words rather than naming a mechanistically distinct failure mode and a separate
  criterion ID), this independently fails C-20 — the dual-key structure is present but the
  mechanism is not distinct, so C-25 cannot be satisfied (C-25 only activates for hypotheses
  that claim or target C-20, and C-20 requires mechanistically-distinct conditions regardless
  of key naming). Detectable because the implementation key names no separate criterion ID.

**baseline-delta:** the `failure-condition:` field in Phase 1 variation headers is replaced with
two separately named keys: `failure-condition-outcome:` and `failure-condition-implementation:`.
The `failure-condition-implementation:` key carries the additional constraint that it must name a
separate criterion ID. No other field, section, or phase changes.

**completeness-risk:** the `failure-condition-implementation:` key in each Phase 1 header —
generators tend to describe the same failure mode twice in different words rather than naming a
mechanistically distinct implementation failure that independently violates a separate criterion.

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

## VARIATION MAP — Immutable after Phase 2 begins

Before Phase 1 begins, commit the axis assignment and per-variation per-criterion directional
predictions for each of the {N} planned variations. Fill every row and every direction cell.
A direction cell without both a verdict and a mechanism sentence is not complete.

| V | Assigned Axis | Criterion Target | C-01 Direction | C-04 Direction | C-07 Direction | Notes |
|---|--------------|-----------------|----------------|----------------|----------------|-------|
[Fill all {N} rows. Each direction cell: verdict (up / down / no-change) + one sentence
mechanism stating why that criterion moves in that direction for this specific axis change.
Do not proceed to Phase 1 until all rows are filled.]

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
mechanism: [structural pathway from axis change to criterion outcome — name the mechanism,
            not the outcome]
failure-condition-outcome: [the specific observable outcome that would prove this axis change
                            produced no improvement on the targeted criterion. Must name a
                            specific prior-round comparison baseline (V-NN R-N result).
                            Format: "if [criterion] pass rate does not exceed [V-NN R-N
                            result], the outcome mechanism is refuted."]
failure-condition-implementation: [the specific observable outcome that would prove this
                                   variation's mechanism was instantiated incorrectly even
                                   if the outcome metric is met. Must name a separate
                                   criterion ID that this implementation failure would
                                   independently violate. Format: "if [structural element]
                                   is [wrong state], this independently fails [C-NN],
                                   regardless of whether the outcome metric is met."]
score-prediction:
  C-01: [pass / partial / fail] — [one sentence mechanism]
  C-04: [pass / partial / fail] — [name the contamination risk for this axis]
  C-07: [pass / partial / fail] — [name the structural element producing hypothesis quality]
  C-09: [pass / partial / fail] — [one sentence mechanism]
```

Review all {N} headers. Verify every axis matches the VARIATION MAP. Every
`failure-condition-implementation:` must name a separate criterion ID it would violate.
Commit. Do not revise axis assignments after Phase 2 begins.

PHASE 2 — GENERATE VARIATION BODIES

For each committed header, write the complete variation body. The AXIS-FREEZE PROTOCOL reads
the committed axis from the VARIATION MAP — the authoritative source.

AXIS-FREEZE PROTOCOL (fires once per body, before writing begins):

  Step 1 — Read: state the axis name assigned in the VARIATION MAP for this body (V-NN:
  [axis name]). [read from VARIATION MAP]

  Step 2 — Write one freeze declaration for every axis in the canonical list:
    - role-sequence:       [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - output-format:       [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - lifecycle-emphasis:  [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - phrasing-register:   [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - inertia-framing:     [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - scoring-granularity: [FROZEN | COMMITTED — read from VARIATION MAP for this body]

  All six canonical axes must appear. Exactly one marked COMMITTED. Five marked FROZEN.
  A freeze list with fewer than six entries is incomplete — do not proceed until all six
  entries are present.

  Step 3 — Write the body: change only the COMMITTED axis. Write the full body — every
  section, every instruction. No diffs. No cross-references to other variations.
  Every structural section present.

Label format:

### V-NN — [Axis: Pole Description]

[variation header from Phase 1 — do not revise]

AXIS-FREEZE PROTOCOL:
[Step 1: VARIATION MAP axis declaration for this V]
[Step 2: six-entry freeze list — all six canonical axes filled, each labeled "read from VARIATION MAP"]
[Step 3: "Proceeding to write COMMITTED axis change only."]

[COMPLETE SKILL BODY — all sections, all instructions, fully written]

Do not begin the next variation until the current body is complete and the AXIS-FREEZE
PROTOCOL shows all six canonical axis entries. Verify VARIATION MAP axis matches Phase 1
header axis before advancing to Phase 3.

PHASE 3 — FINDINGS

Declared responsibility: calibrate VARIATION MAP predictions against actual body structures,
verify VARIATION MAP–Phase 1 axis alignment, identify combination candidates, rank evaluation
order, designate anchor.

1. Axis alignment check:

| V | Axis (VARIATION MAP) | Axis (Phase 1 header) | Match? |
|---|---------------------|----------------------|--------|

Flag any mismatch as AXIS DIVERGENCE — a protocol violation. Do not proceed to combination
candidates until all rows show Match.

2. Prediction calibration:

| V | Axis | C-07 Predicted (MAP) | C-07 Structure Present in Body | Prediction Correct? | Mis-prediction Mechanism |
|---|------|----------------------|-------------------------------|---------------------|--------------------------|

For each wrong prediction, state in one sentence why the structural element did not behave
as the mechanism predicted.

3. Combination candidates (compound-effects model):

| Priority | Axis Pair | V-NN Basis | Failure Modes Per Axis | Residual Weakness After First Axis Only | Compound Criterion Effect (Both Active) | Criteria Targeted |
|----------|-----------|------------|------------------------|-----------------------------------------|-----------------------------------------|-------------------|

Column rules: Failure Modes cites criterion ID per axis. Residual Weakness is a concrete gap,
not a restatement. Compound Criterion Effect names a criterion ID distinct from what either
axis achieves alone. A row with any blank column is omitted.

Priority rationale: one sentence per HIGH or MEDIUM row.

4. Evaluation order:

| Priority | V | Axis | Cost | Independence | Cross-Round Dependency | Sequencing Rationale |
|----------|----|------|------|--------------|------------------------|----------------------|

Cross-round dependency format: "R[round] / V-NN / [metric name]" or "none."

5. Anchor: one variation. Justify structural impact, isolation quality, detectable failure
   condition — one sentence each.

---

## V-02 — Scoring Granularity: Failure-Condition Prediction Columns in Variation Map

**axis:** scoring-granularity
**criterion-targeted:** C-30 — "The pre-generation variation map (satisfying C-24) includes, for
each variation, a separately labeled prediction of which failure mode — outcome failure or
implementation failure — is expected to manifest if the hypothesis is false. Two distinct
prediction fields or columns per variation row qualify: `failure-condition-outcome prediction`
and `failure-condition-implementation prediction`." Mechanism: the VARIATION MAP in the R5 V-05
champion tracks which criteria improve (C-24) but not what breaks and how. Adding two required
failure-condition prediction columns per row creates a verifiable pre-commitment to the expected
failure signature before generation begins — a scorecard can later check whether the actual body
failure modes matched the predicted failure modes, recovering negative experimental results.

**hypothesis:**
- **criterion-target:** C-30
- **direction:** increases C-30 pass rates; C-24 content preserved (direction predictions remain);
  C-20 detectability at map scope: up
- **mechanism:** because C-30 requires the VARIATION MAP to contain per-variation predictions of
  which failure mode (outcome vs implementation) is expected if the hypothesis is false — a
  content requirement beyond C-24's "which criteria improve" record. Adding two labeled columns
  per row forces the generator to distinguish outcome failure (axis produced no measurable effect
  on the target criterion) from implementation failure (mechanism was instantiated incorrectly,
  independently violating a named criterion) at the planning stage, before any body is written.
  The pre-commitment can be audited against actual body failure conditions in Phase 3.
- **failure-condition-outcome:** if C-30 pass rate does not exceed zero (C-30 was not targeted
  in any R5 single-axis pass; the closest prior signal was R5 V-04 combination which included
  dual failure-condition keys in VARIATION MAP rows, but as an output-format change, not a
  scoring-granularity single-axis test), the failure-condition prediction columns add no
  verifiable pre-commitment value over a pure criterion-direction table, and scoring-granularity
  should remain pointed at criterion depth targets (C-24, C-19) rather than C-30 in R7.
- **failure-condition-implementation:** if the `failure-condition-implementation prediction`
  columns in the VARIATION MAP are populated but describe the same failure mode as the
  `failure-condition-outcome prediction` column (no mechanistically distinct second mode named
  per row), this independently fails C-20 at the map level — the columns satisfy C-30's
  structural form (two separately labeled prediction fields) but not C-20's content requirement
  (two mechanistically distinct failure conditions), making C-30 compliance a structural artifact
  without experimental value.

**baseline-delta:** the VARIATION MAP table gains two required columns per variation row:
`failure-condition-outcome prediction` and `failure-condition-implementation prediction`. Each
must be filled with a distinct failure signature. No other change to the VARIATION MAP section,
Phase 1 headers, Phase 2 protocol, or Phase 3 structure.

**completeness-risk:** the `failure-condition-implementation prediction` column in VARIATION MAP
rows — generators tend to name the same failure mode as the outcome column, defeating the
mechanistic distinction C-30 requires.

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

## VARIATION MAP — Immutable after Phase 2 begins

Before Phase 1 begins, commit the axis assignment, per-criterion directional predictions, and
failure-condition type predictions for each of the {N} planned variations. Fill every row and
every column. A row with any blank cell is not complete.

| V | Assigned Axis | Criterion Target | C-01 Direction | C-04 Direction | C-07 Direction | failure-condition-outcome prediction | failure-condition-implementation prediction | Notes |
|---|--------------|-----------------|----------------|----------------|----------------|--------------------------------------|----------------------------------------------|-------|
[Fill all {N} rows. Direction cells: verdict (up / down / no-change) + one sentence mechanism.
failure-condition-outcome prediction: the expected observable failure if the axis change
  produces no improvement on the target criterion — name the criterion and prior baseline.
failure-condition-implementation prediction: the expected observable failure if the mechanism
  is instantiated incorrectly — name the specific structural flaw and the separate criterion
  ID it would independently violate.
Do not proceed to Phase 1 until all rows and all columns are filled.]

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
failure-condition: [the specific observable outcome that would refute the mechanism. Must
                   name the prior-round comparison baseline. Format: "if [criterion] pass
                   rate does not exceed [V-NN R-N result], the mechanism is refuted."]
score-prediction:
  C-01: [pass / partial / fail] — [one sentence mechanism]
  C-04: [pass / partial / fail] — [name the contamination risk for this axis]
  C-07: [pass / partial / fail] — [name the structural element producing hypothesis quality]
  C-09: [pass / partial / fail] — [one sentence mechanism]
```

Review all {N} headers. Verify every axis matches the VARIATION MAP. Commit. Do not revise
axis assignments after Phase 2 begins.

PHASE 2 — GENERATE VARIATION BODIES

For each committed header, write the complete variation body. The AXIS-FREEZE PROTOCOL reads
the committed axis from the VARIATION MAP — the authoritative source.

AXIS-FREEZE PROTOCOL (fires once per body, before writing begins):

  Step 1 — Read: state the axis name assigned in the VARIATION MAP for this body (V-NN:
  [axis name]). [read from VARIATION MAP]

  Step 2 — Write one freeze declaration for every axis in the canonical list:
    - role-sequence:       [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - output-format:       [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - lifecycle-emphasis:  [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - phrasing-register:   [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - inertia-framing:     [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - scoring-granularity: [FROZEN | COMMITTED — read from VARIATION MAP for this body]

  All six canonical axes must appear. Exactly one marked COMMITTED. Five marked FROZEN.
  A freeze list with fewer than six entries is incomplete — do not proceed until all six
  entries are present.

  Step 3 — Write the body: change only the COMMITTED axis. Write the full body — every
  section, every instruction. No diffs. No cross-references to other variations.
  Every structural section present.

Label format:

### V-NN — [Axis: Pole Description]

[variation header from Phase 1 — do not revise]

AXIS-FREEZE PROTOCOL:
[Step 1: VARIATION MAP axis declaration for this V]
[Step 2: six-entry freeze list — all six canonical axes filled, each labeled "read from VARIATION MAP"]
[Step 3: "Proceeding to write COMMITTED axis change only."]

[COMPLETE SKILL BODY — all sections, all instructions, fully written]

Do not begin the next variation until the current body is complete and the AXIS-FREEZE
PROTOCOL shows all six canonical axis entries. Verify VARIATION MAP axis matches Phase 1
header axis before advancing to Phase 3.

PHASE 3 — FINDINGS

Declared responsibility: calibrate VARIATION MAP failure-condition predictions against actual
body failure conditions, verify VARIATION MAP–Phase 1 axis alignment, identify combination
candidates, rank evaluation order, designate anchor.

1. Axis alignment check:

| V | Axis (VARIATION MAP) | Axis (Phase 1 header) | Match? |
|---|---------------------|----------------------|--------|

Flag any mismatch as AXIS DIVERGENCE — do not proceed until resolved.

2. Failure-condition prediction calibration:

| V | failure-condition-outcome predicted (MAP) | Outcome condition present in body? | Match? | failure-condition-implementation predicted (MAP) | Implementation condition present in body? | Match? | Mis-prediction Mechanism |
|---|-------------------------------------------|-------------------------------------|--------|---------------------------------------------------|-------------------------------------------|--------|--------------------------|

For each mismatch, state in one sentence why the predicted failure signature did not appear
as expected in the body.

3. Combination candidates (compound-effects model):

| Priority | Axis Pair | V-NN Basis | Failure Modes Per Axis | Residual Weakness After First Axis Only | Compound Criterion Effect (Both Active) | Criteria Targeted |
|----------|-----------|------------|------------------------|-----------------------------------------|-----------------------------------------|-------------------|

Column rules: Failure Modes cites criterion ID per axis. Residual Weakness is a concrete gap,
not a restatement. Compound Criterion Effect names a criterion ID distinct from what either
axis achieves alone. A row with any blank column is omitted.

Priority rationale: one sentence per HIGH or MEDIUM row.

4. Evaluation order:

| Priority | V | Axis | Cost | Independence | Cross-Round Dependency | Sequencing Rationale |
|----------|----|------|------|--------------|------------------------|----------------------|

5. Anchor: one variation. Justify structural impact, isolation quality, detectable failure
   condition — one sentence each.

---

## V-03 — Lifecycle Emphasis: Cross-Artifact Axis Consistency Gate in Generation Loop

**axis:** lifecycle-emphasis
**criterion-targeted:** C-31 — "The inline generation loop gate (satisfying C-15) includes an
explicit cross-artifact consistency check that verifies the axis declared in the standalone
VARIATION MAP matches the axis declared in the current variation's per-variation planning header
before the body is written. Detects silent divergence between the immutable pre-generation
commitment and the per-variation declaration — a case not caught by C-26 (which freezes drift
during writing) or C-29 (which links the freeze protocol to the map) because the inconsistency
would exist in the planning headers before writing begins." Mechanism: the R5 V-05 champion
places an axis alignment check in Phase 3, after all bodies are written. That timing detects
divergence but does not prevent a body from being written under the wrong axis. Moving the
check inside the AXIS-FREEZE PROTOCOL — after Step 2 (freeze declarations) but before Step 3
(body writing) — converts the check from a post-generation audit to a per-body pre-write gate.

**hypothesis:**
- **criterion-target:** C-31
- **direction:** increases C-31 pass rates; C-26 retention: no-change (named freeze and count
  gate preserved); C-29 retention: no-change (VARIATION MAP still authoritative source)
- **mechanism:** because C-31 requires the consistency check to fire inside the generation loop
  before the body is written — the R5 V-05 post-loop check satisfies the spirit of C-31 but not
  the letter: C-31 requires the check to be inside the loop, not a Phase 3 table that fires after
  all bodies are complete. Adding Step 2B inside the AXIS-FREEZE PROTOCOL (after the six-entry
  freeze list, before Step 3) makes the divergence check temporal with the freeze protocol: the
  generator declares which axes are frozen, then immediately checks whether the axis being
  committed matches the VARIATION MAP assignment, before writing a single line of the body. The
  lifecycle position of the check — inside the loop, before the body — is the entire axis change.
- **failure-condition-outcome:** if C-31 pass rate does not exceed zero (C-31 was not targeted
  in any R5 single-axis pass; R5 V-05 had an equivalent check in Phase 3 but not inside the loop),
  moving the check inside the loop adds no divergence-detection benefit, and lifecycle-emphasis
  should remain pointed at C-23 and C-24 lifecycle-gate targets rather than the in-loop placement
  of an alignment check in R7.
- **failure-condition-implementation:** if the Step 2B cross-artifact check fires inside the
  loop but checks Phase 1 header axis against Phase 1 header axis (comparing the header to itself
  rather than to the VARIATION MAP), or if the check label does not name "VARIATION MAP" explicitly
  as the comparison source, this independently fails C-29 — the VARIATION MAP is no longer
  confirmed as the authoritative source for the in-loop enforcement, because the gate can be
  satisfied without reading from the map, breaking the traceable protocol chain C-29 requires.

**baseline-delta:** the AXIS-FREEZE PROTOCOL gains a Step 2B — cross-artifact axis consistency
check — that fires after the six-entry freeze list and before Step 3 (body writing). No other
change to the VARIATION MAP section, Phase 1 headers, Phase 2 protocol structure, or Phase 3.
The Phase 3 axis alignment check table is retained (it now serves as a post-generation
confirmation that no divergence escaped the in-loop gate).

**completeness-risk:** Step 2B — generators may write the cross-artifact check label but omit
the explicit naming of "VARIATION MAP" as the comparison source, or place the check after Step 3
rather than before it (reverting to Phase 3 placement).

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

## VARIATION MAP — Immutable after Phase 2 begins

Before Phase 1 begins, commit the axis assignment and per-variation per-criterion directional
predictions for each of the {N} planned variations. Fill every row and every direction cell.
A direction cell without both a verdict and a mechanism sentence is not complete.

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
  C-01: [pass / partial / fail] — [one sentence mechanism]
  C-04: [pass / partial / fail] — [name the contamination risk for this axis]
  C-07: [pass / partial / fail] — [name the structural element producing hypothesis quality]
  C-09: [pass / partial / fail] — [one sentence mechanism]
```

Review all {N} headers. Verify every axis matches the VARIATION MAP. Commit. Do not revise
axis assignments after Phase 2 begins.

PHASE 2 — GENERATE VARIATION BODIES

For each committed header, write the complete variation body. The AXIS-FREEZE PROTOCOL reads
the committed axis from the VARIATION MAP — the authoritative source.

AXIS-FREEZE PROTOCOL (fires once per body, before writing begins):

  Step 1 — Read: state the axis name assigned in the VARIATION MAP for this body (V-NN:
  [axis name]). [read from VARIATION MAP]

  Step 2 — Write one freeze declaration for every axis in the canonical list:
    - role-sequence:       [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - output-format:       [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - lifecycle-emphasis:  [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - phrasing-register:   [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - inertia-framing:     [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - scoring-granularity: [FROZEN | COMMITTED — read from VARIATION MAP for this body]

  All six canonical axes must appear. Exactly one marked COMMITTED. Five marked FROZEN.
  A freeze list with fewer than six entries is incomplete — do not proceed until all six
  entries are present.

  Step 2B — Cross-artifact axis consistency check (fires before Step 3):
    - VARIATION MAP assigned axis for this V-NN: [state the axis from the VARIATION MAP row]
      [read from VARIATION MAP]
    - Phase 1 header declared axis for this V-NN: [state the axis from the Phase 1 header]
    - Consistency verdict: [CONSISTENT | AXIS DIVERGENCE]
    - If AXIS DIVERGENCE: state which artifact carries the incorrect axis assignment and halt.
      Do not proceed to Step 3 until the divergence is resolved and the consistency verdict
      reads CONSISTENT.

  Step 3 — Write the body: change only the COMMITTED axis. Write the full body — every
  section, every instruction. No diffs. No cross-references to other variations.
  Every structural section present.

Label format:

### V-NN — [Axis: Pole Description]

[variation header from Phase 1 — do not revise]

AXIS-FREEZE PROTOCOL:
[Step 1: VARIATION MAP axis declaration]
[Step 2: six-entry freeze list — all six canonical axes, each labeled "read from VARIATION MAP"]
[Step 2B: VARIATION MAP axis, Phase 1 header axis, CONSISTENT / AXIS DIVERGENCE verdict]
[Step 3: "Proceeding to write COMMITTED axis change only."]

[COMPLETE SKILL BODY — all sections, all instructions, fully written]

Do not begin the next variation until the current body is complete, the AXIS-FREEZE PROTOCOL
shows all six canonical axis entries, and Step 2B shows CONSISTENT.

PHASE 3 — FINDINGS

Declared responsibility: confirm in-loop axis consistency (post-generation audit), calibrate
VARIATION MAP predictions against actual body structures, identify combination candidates, rank
evaluation order, designate anchor.

1. Axis alignment confirmation (post-generation audit — all in-loop Step 2B checks should
   have already caught any divergence; this table is a post-generation confirmation only):

| V | Axis (VARIATION MAP) | Axis (Phase 1 header) | Step 2B In-Loop Result | Post-Generation Match? |
|---|---------------------|----------------------|------------------------|------------------------|

Flag any post-generation mismatch as ESCAPED DIVERGENCE — a protocol failure indicating the
Step 2B check was not executed correctly in the loop.

2. Prediction calibration:

| V | Axis | C-07 Predicted (MAP) | C-07 Structure Present in Body | Prediction Correct? | Mis-prediction Mechanism |
|---|------|----------------------|-------------------------------|---------------------|--------------------------|

3. Combination candidates (compound-effects model):

| Priority | Axis Pair | V-NN Basis | Failure Modes Per Axis | Residual Weakness After First Axis Only | Compound Criterion Effect (Both Active) | Criteria Targeted |
|----------|-----------|------------|------------------------|-----------------------------------------|-----------------------------------------|-------------------|

Column rules: Failure Modes cites criterion ID per axis. Residual Weakness is a concrete gap.
Compound Criterion Effect names a criterion ID distinct from what either axis achieves alone.
A row with any blank column is omitted. Priority rationale: one sentence per HIGH or MEDIUM row.

4. Evaluation order:

| Priority | V | Axis | Cost | Independence | Cross-Round Dependency | Sequencing Rationale |
|----------|----|------|------|--------------|------------------------|----------------------|

5. Anchor: one variation. Justify structural impact, isolation quality, detectable failure
   condition — one sentence each.

---

## V-04 — Combination: Output Format × Lifecycle Emphasis

**axis:** output-format × lifecycle-emphasis
**pass-type:** combination (R6 Priority 1 — V-01 R6 dual failure-condition keys × V-03 R6
in-loop cross-artifact axis consistency gate)
*C-04 exception explicitly invoked.*

**hypothesis:** Combining the dual failure-condition keys (V-01 R6, output-format axis:
`failure-condition-outcome:` and `failure-condition-implementation:` as distinct required keys
in Phase 1 headers) with the in-loop cross-artifact axis consistency gate (V-03 R6, lifecycle-
emphasis axis: Step 2B inside the AXIS-FREEZE PROTOCOL before each body) increases C-25 and C-31
jointly beyond what either axis achieves alone:
- **criterion-target:** C-25 (primary), C-31 (secondary)
- **direction:** increases C-25 and C-31 pass rates beyond what either axis achieves alone
- **mechanism:** V-01 R6 alone satisfies C-25 (dual keys in Phase 1 headers, C-20 compliance
  structurally detectable) but the Phase 1 headers can carry correct dual keys for the wrong axis
  if the VARIATION MAP and Phase 1 header axes diverge silently. V-03 R6 alone satisfies C-31 (in-
  loop axis consistency check before each body) but the Phase 1 header being verified by the gate
  carries only a single `failure-condition:` field — the gate confirms the correct axis without
  ensuring the header's failure conditions are structurally adequate for C-20. The combination
  produces a Phase 1 header with dual failure-condition keys (C-25: structurally detectable C-20
  compliance) verified by an in-loop gate (C-31: confirmed to match VARIATION MAP assignment) before
  the body is written — the only R6 configuration where the axis assignment is verified and the
  failure condition structure is auditable before a single line of the body is written.
- **failure-condition-outcome:** if C-25 and C-31 pass rates do not jointly exceed V-01 R6 alone
  (C-25 single-axis baseline) and V-03 R6 alone (C-31 single-axis baseline), the combination
  provides no compound benefit and these axes should remain as independent single-axis variations
  in R7 rather than promoted as a compound configuration.
- **failure-condition-implementation:** if the in-loop Step 2B gate verifies axis consistency but
  does not inspect whether the verified Phase 1 header's `failure-condition-implementation:` key
  names a separate criterion ID, the combination leaves C-20 content validity unverified at the
  gate — independently failing C-22 (criterion-keyed combination roadmap rows) because the
  compound effect claimed is "verified axis + verifiable C-20 compliance" but the gate only verifies
  axis, not C-20 content, making the criterion-keyed claim unprovable from the gate output alone.

---

**Combination pass: output-format × lifecycle-emphasis**
*C-04 exception explicitly invoked. Dual failure-condition keys (output-format axis) and in-loop
cross-artifact axis consistency gate (lifecycle-emphasis axis) are both active. The generated
variations are still single-axis — each changes one axis from the baseline skill. The combination
applies to the generation scaffolding structure, not to the individual variations themselves.*

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

## VARIATION MAP — Immutable after Phase 2 begins

Before Phase 1 begins, commit the axis assignment and per-variation per-criterion directional
predictions for each of the {N} planned variations. Fill every row and every direction cell.
A direction cell without a verdict and mechanism sentence is not complete.

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
failure-condition-outcome: [the specific observable outcome that would prove this axis change
                            produced no improvement on the targeted criterion. Must name a
                            specific prior-round comparison baseline. Format: "if [criterion]
                            pass rate does not exceed [V-NN R-N result], the outcome mechanism
                            is refuted."]
failure-condition-implementation: [the specific observable outcome that would prove the
                                   mechanism was instantiated incorrectly even if the outcome
                                   metric is met. Must name a separate criterion ID this
                                   implementation failure would independently violate. Format:
                                   "if [structural element] is [wrong state], this independently
                                   fails [C-NN], regardless of outcome metric."]
score-prediction:
  C-01: [pass / partial / fail] — [one sentence mechanism]
  C-04: [pass / partial / fail] — [name the contamination risk for this axis]
  C-07: [pass / partial / fail] — [name the structural element producing hypothesis quality]
  C-09: [pass / partial / fail] — [one sentence mechanism]
```

Review all {N} headers. Verify every axis matches the VARIATION MAP. Every
`failure-condition-implementation:` must name a separate criterion ID. Commit. Do not revise
axis assignments after Phase 2 begins.

PHASE 2 — GENERATE VARIATION BODIES

For each committed header, write the complete variation body. The AXIS-FREEZE PROTOCOL reads
the committed axis from the VARIATION MAP — the authoritative source.

AXIS-FREEZE PROTOCOL (fires once per body, before writing begins):

  Step 1 — Read: state the axis name assigned in the VARIATION MAP for this body (V-NN:
  [axis name]). [read from VARIATION MAP]

  Step 2 — Write one freeze declaration for every axis in the canonical list:
    - role-sequence:       [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - output-format:       [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - lifecycle-emphasis:  [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - phrasing-register:   [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - inertia-framing:     [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - scoring-granularity: [FROZEN | COMMITTED — read from VARIATION MAP for this body]

  All six canonical axes must appear. Exactly one marked COMMITTED. Five marked FROZEN.
  A freeze list with fewer than six entries is incomplete — do not proceed until all six
  entries are present.

  Step 2B — Cross-artifact axis consistency check (fires before Step 3):
    - VARIATION MAP assigned axis for this V-NN: [state the axis from the VARIATION MAP row]
      [read from VARIATION MAP]
    - Phase 1 header declared axis for this V-NN: [state the axis from the Phase 1 header]
    - Consistency verdict: [CONSISTENT | AXIS DIVERGENCE]
    - If AXIS DIVERGENCE: halt. Do not proceed to Step 3 until resolved.

  Step 3 — Write the body: change only the COMMITTED axis. Write the full body — every
  section, every instruction. No diffs. No cross-references to other variations.
  Every structural section present.

Label format:

### V-NN — [Axis: Pole Description]

[variation header from Phase 1 — do not revise]

AXIS-FREEZE PROTOCOL:
[Step 1: VARIATION MAP axis declaration]
[Step 2: six-entry freeze list — all six canonical axes, each labeled "read from VARIATION MAP"]
[Step 2B: VARIATION MAP axis, Phase 1 header axis, CONSISTENT / AXIS DIVERGENCE verdict]
[Step 3: "Proceeding to write COMMITTED axis change only."]

[COMPLETE SKILL BODY — all sections, all instructions, fully written]

Do not begin the next variation until the current body is complete, the AXIS-FREEZE PROTOCOL
shows all six canonical axis entries, and Step 2B shows CONSISTENT.

PHASE 3 — FINDINGS

Declared responsibility: post-generation axis consistency audit, calibrate predictions against
actual body structures, identify combination candidates, rank evaluation order, designate anchor.

1. Axis alignment confirmation (post-generation audit):

| V | Axis (VARIATION MAP) | Axis (Phase 1 header) | Step 2B Result | Post-Generation Match? |
|---|---------------------|----------------------|----------------|------------------------|

Flag any ESCAPED DIVERGENCE as a protocol failure.

2. Dual-key content audit:

| V | failure-condition-outcome present? | failure-condition-implementation present? | implementation key names separate C-NN? |
|---|------------------------------------|--------------------------------------------|------------------------------------------|

A row with "No" in column 3 fails C-20 and C-25 regardless of key structural presence.

3. Combination candidates (compound-effects model):

| Priority | Axis Pair | V-NN Basis | Failure Modes Per Axis | Residual Weakness After First Axis Only | Compound Criterion Effect (Both Active) | Criteria Targeted |
|----------|-----------|------------|------------------------|-----------------------------------------|-----------------------------------------|-------------------|

4. Evaluation order:

| Priority | V | Axis | Cost | Independence | Cross-Round Dependency | Sequencing Rationale |
|----------|----|------|------|--------------|------------------------|----------------------|

5. Anchor: one variation. Justify structural impact, isolation quality, detectable failure
   condition — one sentence each.

---

## V-05 — Combination: Scoring Granularity × Lifecycle Emphasis

**axis:** scoring-granularity × lifecycle-emphasis
**pass-type:** combination (R6 Priority 2 — V-02 R6 failure-condition prediction columns ×
V-03 R6 in-loop cross-artifact axis consistency gate)
*C-04 exception explicitly invoked.*

**hypothesis:** Combining the failure-condition prediction columns in the VARIATION MAP (V-02 R6,
scoring-granularity axis: `failure-condition-outcome prediction` and
`failure-condition-implementation prediction` per variation row) with the in-loop cross-artifact
axis consistency gate (V-03 R6, lifecycle-emphasis axis: Step 2B inside the AXIS-FREEZE PROTOCOL)
increases C-30 and C-31 jointly beyond what either axis achieves alone:
- **criterion-target:** C-30 (primary), C-31 (secondary)
- **direction:** increases C-30 and C-31 pass rates beyond what either axis achieves alone
- **mechanism:** V-02 R6 alone satisfies C-30 (failure-condition prediction columns in the
  VARIATION MAP at document scope) but the VARIATION MAP's predictions can be for the wrong axis
  if the map and Phase 1 headers diverge. V-03 R6 alone satisfies C-31 (in-loop axis consistency
  gate before each body) but the VARIATION MAP being checked carries only criterion direction
  predictions — the gate confirms axis assignment but cannot verify whether the predicted failure
  modes are appropriate for the confirmed axis. The combination creates a three-level chain: the
  VARIATION MAP commits both direction predictions and failure-condition predictions for each axis
  (scoring-granularity axis, C-30); the in-loop gate verifies that the axis being committed matches
  the VARIATION MAP before the body is written (lifecycle-emphasis axis, C-31); the generator
  writes the body under the verified axis with pre-committed failure predictions at document scope.
  This is the only R6 configuration where the failure-condition predictions and the axis
  consistency check are temporally linked: the predictions exist before the gate fires, and the
  gate fires before the body is written under those predictions.
- **failure-condition-outcome:** if C-30 and C-31 pass rates do not jointly exceed V-02 R6 alone
  (C-30 single-axis baseline) and V-03 R6 alone (C-31 single-axis baseline), the three-level chain
  provides no compound benefit over independent single-axis results, and these axes should remain
  independent in R7 rather than being promoted as a compound configuration.
- **failure-condition-implementation:** if the in-loop Step 2B gate verifies the VARIATION MAP
  axis assignment but the failure-condition prediction columns in the VARIATION MAP are not linked
  to the gate output (the gate does not reference the map's failure-condition predictions, only
  the axis assignment), this independently fails C-29 — the VARIATION MAP is not fully the
  authoritative source for the AXIS-FREEZE PROTOCOL: the protocol reads axis assignments but
  ignores the failure-condition prediction content, creating a partial read-source relationship
  rather than the single-source-of-truth chain C-29 requires.

---

**Combination pass: scoring-granularity × lifecycle-emphasis**
*C-04 exception explicitly invoked. Failure-condition prediction columns in VARIATION MAP
(scoring-granularity axis) and in-loop cross-artifact axis consistency gate (lifecycle-emphasis
axis) are both active. The generated variations are still single-axis — each changes one axis
from the baseline skill. The combination applies to the generation scaffolding structure.*

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis.

## VARIATION MAP — Immutable after Phase 2 begins

Before Phase 1 begins, commit the axis assignment, per-criterion directional predictions, and
failure-condition type predictions for each of the {N} planned variations. Fill every row and
every column. A row with any blank cell is not complete.

| V | Assigned Axis | Criterion Target | C-01 Direction | C-04 Direction | C-07 Direction | failure-condition-outcome prediction | failure-condition-implementation prediction | Notes |
|---|--------------|-----------------|----------------|----------------|----------------|--------------------------------------|----------------------------------------------|-------|
[Fill all {N} rows. Direction cells: verdict + one sentence mechanism. Prediction columns:
failure-condition-outcome prediction: expected observable failure if axis change produces no
  improvement on the target criterion — name the criterion and prior baseline.
failure-condition-implementation prediction: expected observable failure if mechanism is wrong —
  name the structural flaw and the separate criterion ID independently violated.
Do not proceed to Phase 1 until all rows and all columns are filled.]

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
  C-01: [pass / partial / fail] — [one sentence mechanism]
  C-04: [pass / partial / fail] — [name the contamination risk for this axis]
  C-07: [pass / partial / fail] — [name the structural element producing hypothesis quality]
  C-09: [pass / partial / fail] — [one sentence mechanism]
```

Review all {N} headers. Verify every axis matches the VARIATION MAP. Commit. Do not revise
axis assignments after Phase 2 begins.

PHASE 2 — GENERATE VARIATION BODIES

For each committed header, write the complete variation body. The AXIS-FREEZE PROTOCOL reads
the committed axis from the VARIATION MAP — the authoritative source.

AXIS-FREEZE PROTOCOL (fires once per body, before writing begins):

  Step 1 — Read: state the axis name assigned in the VARIATION MAP for this body (V-NN:
  [axis name]). [read from VARIATION MAP]

  Step 2 — Write one freeze declaration for every axis in the canonical list:
    - role-sequence:       [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - output-format:       [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - lifecycle-emphasis:  [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - phrasing-register:   [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - inertia-framing:     [FROZEN | COMMITTED — read from VARIATION MAP for this body]
    - scoring-granularity: [FROZEN | COMMITTED — read from VARIATION MAP for this body]

  All six canonical axes must appear. Exactly one marked COMMITTED. Five marked FROZEN.
  A freeze list with fewer than six entries is incomplete — do not proceed until all six
  entries are present.

  Step 2B — Cross-artifact axis consistency check (fires before Step 3):
    - VARIATION MAP assigned axis for this V-NN: [state the axis from the VARIATION MAP row]
      [read from VARIATION MAP]
    - VARIATION MAP failure-condition-outcome prediction for this V-NN: [state the prediction
      from the VARIATION MAP row] [read from VARIATION MAP]
    - Phase 1 header declared axis for this V-NN: [state the axis from the Phase 1 header]
    - Consistency verdict: [CONSISTENT | AXIS DIVERGENCE]
    - If AXIS DIVERGENCE: halt. Do not proceed to Step 3 until resolved.

  Step 3 — Write the body: change only the COMMITTED axis. Write the full body — every
  section, every instruction. No diffs. No cross-references to other variations.
  Every structural section present.

Label format:

### V-NN — [Axis: Pole Description]

[variation header from Phase 1 — do not revise]

AXIS-FREEZE PROTOCOL:
[Step 1: VARIATION MAP axis declaration]
[Step 2: six-entry freeze list — all six canonical axes, each labeled "read from VARIATION MAP"]
[Step 2B: VARIATION MAP axis, VARIATION MAP failure-condition-outcome prediction, Phase 1 header
          axis, CONSISTENT / AXIS DIVERGENCE verdict]
[Step 3: "Proceeding to write COMMITTED axis change only."]

[COMPLETE SKILL BODY — all sections, all instructions, fully written]

Do not begin the next variation until the current body is complete, the AXIS-FREEZE PROTOCOL
shows all six canonical axis entries, and Step 2B shows CONSISTENT.

PHASE 3 — FINDINGS

Declared responsibility: post-generation axis consistency audit, calibrate VARIATION MAP
failure-condition predictions against actual body failure conditions, identify combination
candidates, rank evaluation order, designate anchor.

1. Axis and failure-condition alignment confirmation:

| V | Axis (VARIATION MAP) | Axis (Phase 1 header) | Step 2B Result | failure-condition-outcome predicted | Outcome condition in body? | Match? |
|---|---------------------|----------------------|----------------|-------------------------------------|---------------------------|--------|

Flag ESCAPED DIVERGENCE for any axis mismatch that was not caught by Step 2B.

2. Failure-condition implementation prediction calibration:

| V | failure-condition-implementation predicted (MAP) | Implementation condition in body? | Match? | Mis-prediction Mechanism |
|---|--------------------------------------------------|----------------------------------|--------|--------------------------|

For each mismatch, state in one sentence why the predicted implementation failure signature
did not appear in the body as expected.

3. Combination candidates (compound-effects model):

| Priority | Axis Pair | V-NN Basis | Failure Modes Per Axis | Residual Weakness After First Axis Only | Compound Criterion Effect (Both Active) | Criteria Targeted |
|----------|-----------|------------|------------------------|-----------------------------------------|-----------------------------------------|-------------------|

A row with any blank column is omitted. Priority rationale: one sentence per HIGH or MEDIUM row.

4. Evaluation order:

| Priority | V | Axis | Cost | Independence | Cross-Round Dependency | Sequencing Rationale |
|----------|----|------|------|--------------|------------------------|----------------------|

5. Anchor: one variation. Justify structural impact, isolation quality, detectable failure
   condition — one sentence each.

---

## Axis Tension Note (C-13 — before combination roadmap)

**Tension: output-format × lifecycle-emphasis (V-04)**

The dual failure-condition keys (output-format axis, V-01 R6) operate at Phase 1 header scope:
each header must contain two named failure-condition keys with the implementation key naming a
separate criterion ID. The in-loop cross-artifact consistency gate (lifecycle-emphasis axis,
V-03 R6) operates at per-body generation scope: a Step 2B check fires inside the AXIS-FREEZE
PROTOCOL before each body. The combination risk: the in-loop gate verifies axis assignment but
not the content of the failure-condition keys in the verified header. A generator that satisfies
C-31 (axis confirmed CONSISTENT by Step 2B) may still produce a `failure-condition-implementation:`
key that restates the outcome failure in different words rather than naming a separate criterion
ID — C-25 structural form present, C-20 content absent — and the gate does not catch this because
it checks axis identity, not failure-condition content.

**Dominant axis prediction: output-format will dominate.** The dual-key structure in Phase 1
headers enforces C-25 structural compliance at the point where failure conditions are authored;
the in-loop gate confirms axis assignment but cannot prevent a generator from writing a
structurally-present but content-invalid implementation key. If V-01 R6 alone achieves C-25 at
full pass rate and V-04 does not push C-31 compliance beyond V-03 R6 alone, the lifecycle-
emphasis contribution is the weaker axis in this combination.

**Tension: scoring-granularity × lifecycle-emphasis (V-05)**

The failure-condition prediction columns (scoring-granularity axis, V-02 R6) commit failure mode
predictions in the VARIATION MAP at document scope. The in-loop axis consistency gate (lifecycle-
emphasis axis, V-03 R6) reads the VARIATION MAP for axis assignment but does not read the
failure-condition predictions. The combination risk: the failure-condition predictions are
committed in the map, and the gate confirms the axis is consistent — but the gate's Step 2B does
not verify that the body's failure conditions are aligned with the map's pre-committed predictions.
The V-05 combination addresses this by including the failure-condition-outcome prediction in
Step 2B's output, surfacing the prediction at gate-fire time — but if the gate does not also
require the generator to acknowledge or compare against the prediction, the link between the
committed prediction and the written body remains informal.

**Dominant axis prediction: lifecycle-emphasis will dominate.** The in-loop gate is the
load-bearing structural element because the compound value of V-05 derives from the gate
surfacing the VARIATION MAP's failure-condition predictions at body-write time. If the gate
exists but does not include the prediction in its output (reverting to axis-only verification),
the scoring-granularity contribution collapses to V-02 R6 standalone, and the compound effect
disappears. The prediction columns must be referenced in the gate for the combination to deliver
criterion value beyond the independent single-axis results.

---

## Combination Roadmap for Round 7 (C-09, C-22)

| Priority | Axis Pair | R6 Basis | Failure Modes Per Axis | Residual Weakness After First Axis Only | Compound Criterion Effect (Both Active) | Criteria Targeted |
|----------|-----------|----------|------------------------|-----------------------------------------|-----------------------------------------|-------------------|
| 1 | output-format × scoring-granularity | V-01 R6 (dual failure-condition keys, C-25) × V-02 R6 (failure-condition prediction columns in VARIATION MAP, C-30) | output-format: single `failure-condition:` field makes C-20 compliance detectable only by prose parsing, failing C-25; scoring-granularity: VARIATION MAP rows carry no failure-condition predictions, failing C-30 | After output-format alone (V-01 R6): Phase 1 headers have dual failure-condition keys (C-25 passes), but the VARIATION MAP rows still carry only criterion direction predictions — no pre-committed failure signatures for each variation at document scope (C-30 fails) | After both active: dual failure-condition keys in Phase 1 headers (output-format: C-25) + failure-condition prediction columns in VARIATION MAP rows (scoring-granularity: C-30) — the only R7 configuration where failure condition types are declared with C-25's structural detectability at Phase 1 header scope AND pre-committed with C-30's map-scope predictive requirement simultaneously | C-25, C-30 |
| 2 | phrasing-register × lifecycle-emphasis | phrasing-register untested R6 (reserved from R5) × V-03 R6 (in-loop cross-artifact gate, C-31) | phrasing-register: formal-technical imperative register untested; may push hypothesis sub-fields toward terse single-clause entries that collapse mechanism sentences, degrading C-07 quality; lifecycle-emphasis: in-loop gate checks axis but not failure-condition key content | After lifecycle-emphasis alone (V-03 R6): C-31 passes (in-loop axis check before each body), but failure-condition keys in Phase 1 headers retain the baseline single-field format — gate confirms axis without inspecting key structure | After both active: a phrasing-register calibrated to enforce per-key length and content norms (outcome key: one sentence on criterion impact + baseline; implementation key: one sentence on mechanism + separate C-NN ID) combined with the in-loop gate yields a configuration where axis is verified (C-31) and failure-condition key quality is structurally enforced by format norms (improving C-07 mechanism quality within each key) | C-31, C-07 |

Priority rationale: Candidate 1 is HIGH because C-25 (Phase 1 header scope) and C-30 (VARIATION
MAP scope) address failure-condition structural requirements at two different lifecycle positions;
their combination tests whether failure condition type information propagates correctly from the
pre-generation map commitment to the per-variation header implementation. Candidate 2 is MEDIUM
because phrasing-register has not been tested single-axis in R5 or R6; its interaction with the
in-loop gate is speculative until the single-axis pass runs.

---

## Evaluation Order (C-12)

| Priority | V | Axis | Cost | Independence | Cross-Round Dependency | Sequencing Rationale |
|----------|----|------|------|--------------|------------------------|----------------------|
| 1 | V-02 | scoring-granularity | Low | Full — adding two VARIATION MAP columns is purely additive; no Phase 1 header fields change; no dependency on output-format or lifecycle-emphasis | none | Lowest structural impact, fully independent. Run first to establish C-30 single-axis baseline before any combination. Results needed for V-05. |
| 2 | V-03 | lifecycle-emphasis | Low | Full — Step 2B is purely additive inside the AXIS-FREEZE PROTOCOL; no header fields or VARIATION MAP columns change | none | Second: purely additive, independent. Run before V-04 and V-05 (both use lifecycle-emphasis). C-31 single-axis baseline must be established before either combination is interpretable. |
| 3 | V-01 | output-format | Medium | Partial — Phase 1 header field rename interacts with Phase 3 dual-key content audit (V-04 uses this); needs V-02 and V-03 single-axis baselines to contextualize combination results | R6 / V-02 / C-30 baseline | Third: header field change is more invasive than additive. V-01 result establishes C-25 single-axis baseline for V-04. Run after V-02 and V-03 are complete. |
| 4 | V-04 | output-format × lifecycle-emphasis | High | Combination — depends on V-01 (C-25 single-axis baseline) and V-03 (C-31 single-axis baseline) | R6 / V-01 / C-25 baseline; R6 / V-03 / C-31 baseline | Fourth: requires V-01 and V-03 results. Tests whether dual keys at Phase 1 header scope plus in-loop axis verification produce a compound C-25 + C-31 effect beyond independent single-axis results. |
| 5 | V-05 | scoring-granularity × lifecycle-emphasis | High | Combination — depends on V-02 (C-30 baseline) and V-03 (C-31 baseline); highest-cost evaluation due to Step 2B failure-condition prediction surfacing requirement | R6 / V-02 / C-30 baseline; R6 / V-03 / C-31 baseline | Fifth: most complex. Requires V-02 and V-03 results. Tests the three-level chain: map failure-condition predictions committed at document scope, axis verified in loop, body written under confirmed assignment. The key verification: does Step 2B in V-05 surface the map's failure-condition-outcome prediction at gate-fire time? |

---

## Anchor Designation

**Designated anchor: V-03 (lifecycle-emphasis: Cross-Artifact Axis Consistency Gate in
Generation Loop)**

- **Structural impact:** V-03 promotes the post-generation Phase 3 axis alignment check (R5
  V-05) to an in-loop pre-body gate inside the AXIS-FREEZE PROTOCOL — the highest-impact single
  change for C-31 because it converts axis divergence detection from a post-generation audit (body
  already written under potentially wrong axis) to a per-body pre-write gate (divergence caught
  before any body content is generated), making the VARIATION MAP–Phase 1 header consistency
  requirement enforceable at the point of maximum intervention.

- **Isolation quality:** Step 2B is purely additive inside the AXIS-FREEZE PROTOCOL — it inserts
  a named sub-step after Step 2 and before Step 3 without changing the VARIATION MAP section, Phase
  1 header format, Phase 2 general structure, or Phase 3 content; the only observable behavioral
  change is the presence of a CONSISTENT / AXIS DIVERGENCE verdict before each body's Step 3,
  making contamination risk at the axis level zero.

- **Detectable failure condition:** if Step 2B produces an AXIS DIVERGENCE verdict for any
  variation, the failure is detectable by label presence before the body is read — the protocol
  failure is visible at the gate output level, not requiring full-body content comparison; if Step
  2B is absent from the AXIS-FREEZE PROTOCOL entirely, C-31 fails by structural inspection of
  the Phase 2 instructions without running any variation.
