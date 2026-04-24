# quest-variate Variate — Round 3

**Date:** 2026-03-15
**Skill:** quest-variate
**Rubric:** v3 (C-01 through C-18; essential C-01–C-05)
**Round:** R3 — 3 single-axis passes + 2 combination passes (C-04 combination exception applies to V-04 and V-05)

---

## Pre-Generation: Per-Axis Pole Declaration (C-16)

Before any variation body is written, the current baseline pole for each axis is declared.

**Baseline skill (champion):** the unvaried quest-variate prompt — a single-phase generator
that produces N labeled variations with `axis:` and `hypothesis:` inline fields, no specialized
roles, flat Markdown format, equal lifecycle weight to all phases, formal-descriptive register,
no champion declared, and no per-criterion scoring.

| Axis | Baseline Pole (What the Champion Currently Does) | R3 Variation Pole Committed |
|------|--------------------------------------------------|------------------------------|
| role-sequence | Single generator role; no critic, verifier, archivist, or scorekeeper role | V-02: Loop-Gate Verifier role added — fires after each body, names C-01 and C-04 as check targets |
| output-format | Markdown headers with inline `axis:` and `hypothesis:` fields only | V-01: Structured variation envelope with required named fields including `criterion-targeted:` |
| lifecycle-emphasis | Equal weight to axis selection, body generation, and findings phases | Not tested single-axis in R3 (R2 V-03 covered; reserved for combination) |
| phrasing-register | Formal-descriptive imperative ("Generate {N} complete, runnable...") | Not tested single-axis in R3 (covered by R2; reserved for R4 combination) |
| inertia-framing | No champion declared; variations described relative to abstract baseline | V-03: Named status-quo champion with three-failure inventory; each hypothesis attacks a named failure |
| scoring-granularity | No per-criterion scoring; hypothesis cites criterion by name in prose only | V-05 (combination only): per-criterion score prediction block per variation header |

This table is the single-axis isolation reference. During generation, only the committed axis
changes per variation; all other axes remain at their baseline pole.

---

## Round 3 Variation Map

| Variation | Axis | Pass Type | What Changes | Criteria Targeted |
|-----------|------|-----------|--------------|-------------------|
| V-01 | output-format | single-axis | Structured variation envelope precedes each body; `criterion-targeted:` field names the rubric criterion ID the axis targets; `baseline-delta:` commits the one structural change | C-03, C-07, C-14 |
| V-02 | role-sequence | single-axis | Loop-Gate Verifier fires after each variation body — before advancing — and checks C-01 and C-04 by name | C-01, C-15, C-14 |
| V-03 | inertia-framing | single-axis | Champion declared with three-failure inventory; `champion-failure-targeted:` field required per variation; each hypothesis argues against a named champion failure | C-07, C-09 |
| V-04 | output-format × role-sequence | combination (R3 Priority 1 — V-01 × V-02) | Structured envelope + Loop-Gate Verifier combined; pre-generation axis lock active; C-18 failure denominator names V-01 | C-01, C-03, C-15, C-17, C-18 |
| V-05 | inertia-framing × scoring-granularity | combination (R3 Priority 2 — V-03 × uncovered) | Champion-challenger framing + per-criterion score prediction; pre-generation axis lock active; C-18 failure denominator names V-03 | C-07, C-09, C-14, C-17, C-18 |

**Anchor designation (C-12):** V-02. See anchor section at end.

---

## V-01 — Output Format: Structured Variation Envelope

**axis:** output-format
**targets-criterion:** C-03 — "Axis declaration: every variation has `axis:` and `hypothesis:`
fields, both non-empty." Mechanism: a structured variation envelope with required named fields
forces field completeness before the body is written. An envelope with a blank `hypothesis:`
is visually and structurally distinct — it cannot be silently omitted the way inline prose
fields can. The `criterion-targeted:` field additionally satisfies C-14 by making the
axis-to-criterion connection a required declaration rather than buried in hypothesis prose.
This is the C-14-passing form: the axis (output-format) is chosen to improve C-03 pass rates,
the criterion ID is named directly, and the mechanism connecting output-format to C-03 is stated.

**hypothesis:** Replacing flat Markdown variation headers with a structured variation envelope
that includes required named fields — `axis:`, `pole:`, `criterion-targeted:`, `hypothesis:`,
`baseline-delta:`, and `completeness-risk:` — increases C-03 (axis declaration completeness)
pass rates because the required-field structure cannot be silently omitted: an envelope with
a blank field is immediately detectable, unlike an inline prose `hypothesis:` that may be
present but empty or vague. The `criterion-targeted:` field additionally advances C-14
(criterion-targeted axis selection) by making the axis-to-criterion connection a first-class
declaration rather than inferable from hypothesis prose. Failure condition: if C-03 pass rates
for variations generated with this envelope format do not exceed those from inline-header
variations in R2 (where C-03 was assessed without a structured envelope), the required-field
structure adds no axis declaration completeness benefit and this format should not be promoted
to combination runs.

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each variation changes exactly one axis.

STEP 1 — SELECT AXES

Read the skill spec. Select {N} distinct axes from the canonical list, one per variation:

  role-sequence | output-format | lifecycle-emphasis |
  phrasing-register | inertia-framing | scoring-granularity

No two variations may share the same axis. List your {N} axes now, one per line,
before writing any body.

STEP 2 — GENERATE VARIATION BODIES

For each axis selected in Step 1, write one complete variation body. Precede each body
with a structured variation envelope. The envelope is a commitment made before the body
is written — not a summary added after. Fill every required field before writing the body.

Envelope format (all fields required — no field may be blank):

```
variation: V-NN
axis: [axis name from canonical list]
pole: [one phrase describing the specific change this variation makes on this axis]
criterion-targeted: [rubric criterion ID (e.g., C-03) that this axis choice is designed to
                    improve, plus one sentence stating the mechanism connecting this axis
                    to that criterion]
hypothesis: [falsifiable prediction — names rubric criterion ID, direction, mechanism,
             and an explicit failure condition: the specific observable outcome that would
             disprove the prediction]
baseline-delta: [one sentence naming the single structural element that differs from the
                 baseline skill — the element that changes and nothing else]
completeness-risk: [the section of this specific variation body most at risk of being
                    omitted or shortened relative to the others]
```

After completing the envelope, write the complete variation body. Every section. Every
instruction. No diffs. No cross-references to other variations. Every structural section
present. Do not advance to the next variation until this body is complete and all envelope
fields are filled.

Label format:

### V-NN — [Axis Name: Pole Description]

```
[variation envelope — all fields filled before body is written]
```

[COMPLETE SKILL BODY — all sections, all steps, all instructions written in full]

STEP 3 — FINDINGS

After all {N} bodies are written:

1. Variation summary:

| V | Axis | Pole | Criterion Targeted | Baseline Delta | Hypothesis |
|---|------|------|-------------------|----------------|------------|

2. Envelope completeness check: for each variation, confirm every envelope field is non-blank.
   Flag any blank field and state whether it would cause C-03 or C-07 to fail.

3. Top combination candidate: one axis pair with a one-sentence mechanism stating which
   criteria the combination would jointly improve beyond either single-axis variation alone.

4. Evaluation order: rank the {N} variations from lowest evaluation cost to highest,
   with a one-line rationale for each.

---

## V-02 — Role Sequence: Loop-Gate Verifier

**axis:** role-sequence
**targets-criterion:** C-01 — "Runnable completeness: every variation is a full, standalone
skill body." Mechanism: a Loop-Gate Verifier role fires after each variation body is written —
before advancing to the next — and checks C-01 (completeness) and C-04 (single-axis isolation)
as named check targets. Errors caught while the body's generation context is active are
correctable without reconstructing context; errors caught post-generation require re-reading
and re-tracing the full body. This is the C-14-passing form: the axis (role-sequence) is
chosen to improve C-01 pass rates, and the mechanism is stated explicitly. This is
simultaneously the C-15-passing form: the gate fires inside the generation loop, not as a
post-generation review step, and it names the criteria it is checking.

**hypothesis:** Adding a Loop-Gate Verifier role that fires after each variation body —
before the generator advances — and names C-01 (completeness) and C-04 (single-axis
isolation) as its check targets increases C-01 pass rates because incomplete bodies are
caught while the generation context that produced them is still active, enabling immediate
correction rather than post-generation patching. This also directly satisfies C-15 (inline
generation loop gate) because the gate fires inside the loop, not after all bodies are written,
and it names the criteria it is checking. Failure condition: if C-01 pass rates do not
improve relative to variations generated without an inline gate (any R2 baseline that
generated all bodies before running a review pass), the loop-gate mechanism adds no
completeness benefit and the role should not be carried into combination runs. Additionally
fails if the gate is implemented as a final-step review of all bodies rather than a per-body
check that fires before advancing — that form cannot satisfy C-15 regardless of its result.

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each variation changes exactly one axis.

STEP 1 — SELECT AXES

Read the skill spec. Select {N} distinct axes from the canonical list, one per variation:

  role-sequence | output-format | lifecycle-emphasis |
  phrasing-register | inertia-framing | scoring-granularity

No two variations may share the same axis. List your {N} axes now before writing any body.

STEP 2 — GENERATE VARIATION BODIES

--- ROLE: GENERATOR ---

For each axis selected in Step 1, write one complete variation body. Every section.
Every instruction. No diffs. No cross-references to other variations.

Label format:

### V-NN — [Axis Name]
axis: [axis name]
hypothesis: [falsifiable prediction — names rubric criterion ID, direction, mechanism,
             and explicit failure condition]
[COMPLETE SKILL BODY — all sections, all instructions, fully written]

--- ROLE: LOOP-GATE VERIFIER ---

The Loop-Gate Verifier fires after the Generator writes each variation body, before the
Generator begins the next variation. The Generator does not advance until the Loop-Gate
Verifier issues a PASS.

For each body just written, the Loop-Gate Verifier checks:

CHECK C-01 COMPLETENESS
Is the body full and standalone? Could it be copied into a skill file and run without
referencing any other variation? Are all structural sections present — no placeholders,
no ellipses, no "same as V-NN except" constructs?
- If any section is missing or shortened relative to the others: FAIL C-01.
  State the missing section. The Generator must complete it before advancing.

CHECK C-04 SINGLE-AXIS ISOLATION
Does the body change exactly one axis relative to the baseline skill?
- If two or more structural elements changed simultaneously: FAIL C-04.
  Name the contamination. The Generator must revert the unintended change before advancing.

Issue verdict: PASS (both checks clear) or FAIL (list each failed check with required fix).

If FAIL: Generator rewrites the flagged section. Loop-Gate Verifier re-runs both checks
before advancing. The Gate fires once per variation, in sequence:
- After V-01 is written, before V-02 begins.
- After V-02 is written, before V-03 begins.
- And so on through V-{N}.

The Gate does not consolidate. It does not review all bodies after generation ends.
It fires per body, inside the loop.

STEP 3 — FINDINGS

After all {N} bodies have passed the Loop-Gate Verifier:

1. Variation map:

| V | Axis | Change Made | Hypothesis | Loop-Gate Verdict |
|---|------|-------------|------------|-------------------|

2. Top combination candidate: one axis pair with a one-sentence mechanism naming the criteria
   the combination would jointly improve beyond either single-axis variation alone. Note any
   tension between the two axes that could produce interaction effects in a combination run.

3. Evaluation order: rank all {N} variations from lowest evaluation cost to highest,
   with one-line rationale per variation and dependency notes.

4. Anchor designation: identify one variation as the structural anchor for combination runs.
   State: (a) structural impact, (b) isolation quality, (c) detectable failure condition.

---

## V-03 — Inertia Framing: Status-Quo Challenger

**axis:** inertia-framing
**hypothesis:** Declaring the current skill body as the named status-quo champion — with an
explicit inventory of its three most significant rubric failure modes — and requiring every
variation hypothesis to name the specific champion failure it corrects increases C-07
(hypothesis specificity) because it replaces directional predictions ("this variation will
produce better output") with competitive arguments that are criterion-grounded by construction:
a valid challenger hypothesis must state what the champion cannot do and why this variation
corrects it, producing specificity that directional predictions structurally cannot achieve.
This framing also increases C-09 (combination readiness) because hypotheses that identify
distinct champion failures naturally expose which failure pairs require compound correction,
surfacing combination candidates without a separate analysis pass. Failure condition: if
C-07 pass rate for variations generated with this prompt does not exceed the R2 single-axis
baselines (R2 V-01 through V-03, which passed C-07 with prose-level directional predictions
rather than competitive-argument hypotheses), the champion-failure framing adds no hypothesis
specificity benefit and inertia-framing should be treated as a low-priority combination
candidate. Also fails if any variation hypothesis describes only what the challenger does,
without naming a specific champion failure — that indicates the framing is decorative rather
than structurally enforced.

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis from
the champion. Each hypothesis argues against a named champion failure.

DECLARE THE CHAMPION

The current skill body is the status-quo champion. Before writing any variation, produce
a champion inventory:

1. What the champion does well: list the rubric criteria it reliably passes and the
   structural mechanism producing each strength.

2. Where the champion fails: the three most significant rubric criteria the champion
   struggles with, and the structural mechanism producing each weakness. Be precise:
   - "the hypothesis field permits directional predictions that are not falsifiable because
     it sets no specific criterion ID or observable failure condition" is a valid failure mode.
   - "the output could be improved" is not.
   - "C-04 single-axis isolation fails because complex skill bodies tempt co-variation when
     two elements feel conceptually related" is a valid failure mode.

3. The combination signal: for each failure mode, name the single axis most likely to
   correct it, and state whether correction is achievable alone or requires a second axis.

This inventory is the competitive brief. Every challenger variation must attack at least
one named failure from this inventory.

GENERATE CHALLENGERS

Write V-01 through V-{N}. Each variation is a challenger: a complete, standalone skill
body that changes exactly one axis.

Canonical axes: role-sequence | output-format | lifecycle-emphasis |
                phrasing-register | inertia-framing | scoring-granularity

No two variations may share the same axis.

Label format:

### V-NN — [Axis: Challenge Target]
axis: [axis name]
champion-failure-targeted: [which of the three inventory failures this challenger attacks —
                             must match one named in the champion inventory above]
hypothesis: [competitive argument — what the champion cannot do on this criterion, what
             this variation does instead, by what mechanism, and what specific observable
             outcome would prove the champion is still preferable — the explicit failure
             condition for this challenger]
[COMPLETE SKILL BODY — all sections, all instructions, fully written. No diffs.
 Every section present. No cross-references to other variations.]

A hypothesis that only describes what this challenger does, without naming a specific
champion failure, does not meet the format. Rewrite until the champion weakness is
named explicitly.

FINDINGS

After all {N} challengers are written:

Challenger map:

| V | Axis | Champion Failure Targeted | Predicted Criterion Gain | Failure Condition |
|---|------|--------------------------|--------------------------|-------------------|

Combination candidates: for each pair of challengers targeting distinct champion failures:
- Name the pair.
- State what residual champion weakness remains after the first challenger's correction alone.
- State the compound criterion effect if both challenger stances are active simultaneously.
- Assign priority: HIGH / MEDIUM / LOW with one-sentence rationale.

List all pairs before naming the top candidate.

Evaluation order: list the {N} challengers in the sequence that maximizes learning.
Evaluate cheapest and most independent first. For each: evaluation cost, independence
from other results, dependency note.

Anchor designation: identify one challenger as the structural anchor for combination runs.
Justify against: (a) structural impact, (b) isolation quality, (c) detectable failure condition.

---

## V-04 — Combination: Output Format × Role Sequence

**axis:** output-format × role-sequence
**pass-type:** combination (R3 Priority 1 — V-01 structured envelope × V-02 loop-gate verifier)
**hypothesis:** Combining a structured variation envelope that requires `criterion-targeted:`
and `baseline-delta:` field pre-commitment before each body (V-01, output-format axis) with
a Loop-Gate Verifier that checks C-01 and C-04 after each body before advancing (V-02,
role-sequence axis) increases C-01 (completeness) and C-03 (axis declaration) jointly: the
envelope prevents silent field omissions before the body is written, while the loop gate
catches completeness failures immediately after the body is written — together providing
front-and-back coverage that neither axis achieves alone. The `criterion-targeted:` field
also compounds C-14 (criterion-targeted axis selection) by making the axis-to-criterion
connection a required declaration per variation. Failure condition: if C-01 and C-03 pass
rates do not jointly exceed those achieved by V-01 alone (R3 V-01 structured-envelope
single-axis baseline, where C-03 was the primary targeted criterion), the Loop-Gate
Verifier addition does not compound the envelope's declaration quality benefit and adds
only structural cost without measurable correctness improvement.

---

**Combination pass: output-format × role-sequence**
*Structured variation envelope (output-format axis) and Loop-Gate Verifier role (role-sequence
axis) are both active in the generation process. The generated variations are still single-axis
— each changes one axis from the target skill's baseline. The combination applies to how the
generation process is scaffolded, not to the variations themselves.*

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each varies exactly one axis.

PHASE 1 — COMMIT VARIATION ENVELOPES

Before writing any skill body, write the variation envelope for all {N} variations.

Canonical axes: role-sequence | output-format | lifecycle-emphasis |
                phrasing-register | inertia-framing | scoring-granularity

No two variations may share the same axis.

Each envelope must include all required fields:

```
variation: V-NN
axis: [axis name from canonical list]
pole: [one phrase — the specific change this variation makes on this axis]
criterion-targeted: [rubric criterion ID + one sentence on the mechanism connecting
                    this axis to that criterion]
hypothesis: [falsifiable prediction — criterion ID, direction, mechanism, explicit
             failure condition]
baseline-delta: [one sentence naming the single structural element that differs from
                 the baseline skill — the one element that changes and nothing else]
completeness-risk: [the section of this variation body most at risk of being omitted]
```

Do not revise axis assignments after Phase 2 begins. The axis committed in each
envelope is immutable once Phase 2 starts.

Phase 1 review (complete before Phase 2):
- Every axis is distinct and from the canonical list.
- Every `hypothesis:` names a criterion ID and a failure condition.
- Every `baseline-delta:` names exactly one structural element.
- Every `criterion-targeted:` names a rubric criterion ID and a mechanism sentence.

Commit. Phase 2 begins.

PHASE 2 — GENERATE VARIATION BODIES

--- ROLE: GENERATOR ---

For each committed envelope, write the complete variation body. Read the axis from the
committed envelope. Do not revise the envelope. Do not change the axis mid-generation.

For each body, apply isolation:
- Step A: Read the axis from the committed envelope.
- Step B: State what the baseline skill does on that axis.
- Step C: Name every other axis that might tempt a change. Freeze each explicitly.
- Step D: Change only the committed axis. Write the full body. Every section. Every instruction.

Label format:

### V-NN — [Axis: Pole Description]

[variation envelope from Phase 1 — do not revise]

[COMPLETE SKILL BODY — all sections, all instructions, fully written. Not a diff.]

--- ROLE: LOOP-GATE VERIFIER (fires after EACH body, before Generator advances) ---

After each variation body is written, the Loop-Gate Verifier fires before the Generator
begins the next variation.

CHECK C-01 COMPLETENESS: Is the body full and standalone? If no, state the missing section.
Generator must complete it before advancing.

CHECK C-04 ISOLATION: Does the body change exactly the axis committed in Phase 1?
If a second element changed, state the contamination. Generator must revert it before advancing.

CHECK ENVELOPE FIDELITY: Is the `baseline-delta:` field consistent with what actually changed?
Is the `completeness-risk:` section present and complete in the body? If not, state the
discrepancy. Generator must resolve before advancing.

Issue verdict: PASS or FAIL with required fixes. Generator advances only on PASS.

PHASE 3 — FINDINGS

After all {N} bodies have passed the Loop-Gate Verifier:

1. Variation map (confirm axes match Phase 1 envelopes — no reassignments):

| V | Axis | Pole | Baseline Delta | Loop-Gate Verdict |
|---|------|------|----------------|-------------------|

2. Combination candidates:

| Priority | Axis Pair | V-NN Basis | Mechanism | Criteria Targeted |
|----------|-----------|------------|-----------|-------------------|

3. Anchor designation: one variation. Justify against structural impact, isolation quality,
   detectable failure condition.

---

## V-05 — Combination: Inertia Framing × Scoring Granularity

**axis:** inertia-framing × scoring-granularity
**pass-type:** combination (R3 Priority 2 — V-03 champion-challenger × scoring-granularity uncovered single-axis)
**hypothesis:** Combining champion-challenger framing that requires each hypothesis to name
a specific champion failure (V-03, inertia-framing axis) with per-criterion score prediction
blocks that require the operator to commit expected pass/partial/fail outcomes before each
body is written (scoring-granularity axis) increases C-07 (hypothesis specificity) jointly:
the champion-failure mechanism forces hypotheses to argue improvement over a named weakness,
while the score prediction mechanism forces the improvement argument to resolve to a
criterion-keyed expected outcome — together producing hypotheses that are both competitively
grounded and criterion-mapped, which neither axis achieves alone. The `criterion-targeted:`
field produced by the score prediction block also advances C-14 (criterion-targeted axis
selection) for each generated variation. Failure condition: if C-07 pass rates do not
jointly exceed those achieved by V-03 alone (R3 V-03 inertia-framing single-axis baseline,
where champion-challenger framing increased C-07 pass rates with competitive arguments but
without criterion-keyed score predictions), the scoring-granularity addition does not compound
the framing benefit and these axes should remain as independent single-axis variations.

---

**Combination pass: inertia-framing × scoring-granularity**
*Champion-challenger framing (inertia-framing axis) and per-criterion score prediction
(scoring-granularity axis) are both active in the generation process. The generated variations
are still single-axis — each changes one axis from the target skill's baseline. The combination
applies to the generation scaffolding, not to the variations themselves.*

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each changes exactly one axis from
the champion.

PHASE 1 — DECLARE THE CHAMPION AND COMMIT THE VARIATION MAP

Do not revise axis assignments after Phase 2 begins.

Step 1A — Champion inventory.

The current skill body is the status-quo champion. Produce a champion inventory:

1. Champion strengths: rubric criteria the champion reliably passes, with the structural
   mechanism for each.
2. Champion failure modes: the three most significant rubric criteria the champion struggles
   with, with the precise structural mechanism producing each failure.
3. Axis mapping: for each failure mode, the single axis most likely to correct it, and
   whether correction requires a second axis for full coverage.

Step 1B — Commit the variation map.

Select {N} axes from the canonical list. No two rows may share an axis. For each axis,
assign it to a champion failure mode from Step 1A and fill the score prediction cells.

Canonical axes: role-sequence | output-format | lifecycle-emphasis |
                phrasing-register | inertia-framing | scoring-granularity

| V | Axis | Champion Failure Targeted | Score Prediction: C-07 | Score Prediction: C-04 | Score Prediction: C-09 |
|---|------|--------------------------|------------------------|------------------------|------------------------|
[Fill all {N} rows. Each score prediction cell: [pass/partial/fail] + mechanism sentence.]

Review before Phase 2: every axis distinct; every row names a champion failure; every
score prediction cell is non-blank with a verdict and a mechanism. Commit. Do not revise.

PHASE 2 — GENERATE CHALLENGERS

For each row in the committed map, write one complete variation body. Apply isolation:
read axis from committed map; name every other axis that might tempt change; freeze each
explicitly; change only the committed axis.

Score prediction block — carry values from Phase 1B without revision:

score-prediction:
  C-07 hypothesis specificity: [from committed map]
  C-04 isolation:              [from committed map]
  C-09 combination readiness:  [from committed map]

Label format:

### V-NN — [Axis: Champion Failure Targeted]
axis: [axis name]
champion-failure-targeted: [cited from Phase 1A inventory]
hypothesis: [competitive argument — what the champion cannot do on this criterion, what this
             variation corrects, by what mechanism, and what outcome would prove the champion
             still preferable — the explicit failure condition for this challenger]
[score-prediction block — Phase 1B values, not revised during Phase 2]
[COMPLETE SKILL BODY — all sections, all instructions, fully written. No diffs.
 Every section present. No cross-references to other variations.]

PHASE 3 — FINDINGS

After all {N} challengers are written:

Challenger map (confirm axes and failure assignments match Phase 1 commitments):

| V | Axis | Champion Failure Targeted | C-07 Predicted | C-04 Contamination Risk | Score Prediction Correct? |
|---|------|--------------------------|----------------|-------------------------|---------------------------|

Score prediction calibration: for each variation, which criterion-keyed predictions were
wrong? State the mechanism of each mis-prediction.

Combination candidates:

| Priority | Axis Pair | V-NN Basis | Residual Champion Weakness | Compound Effect | Criteria Targeted |
|----------|-----------|------------|-----------------------------|-----------------|-------------------|

Evaluation order: rank all {N} challengers from cheapest to most expensive to evaluate,
with independence and dependency notes.

---

## Axis Tension Note (C-13 — before combination roadmap)

**Tension: output-format × role-sequence (V-04)**

The structured variation envelope (output-format) commits fields before the body is written.
The Loop-Gate Verifier (role-sequence) fires after the body is written. These axes operate
at opposite lifecycle positions: pre-body and post-body. Their combination provides front-and-
back coverage, but if one mechanism is sufficient, the other adds only overhead.

Dominant axis prediction: **output-format will dominate.** The envelope's pre-commitment
eliminates the most common C-01 failure mode (silently omitted sections, which are absent
before writing begins). The Loop-Gate Verifier catches failures after writing — more expensive
to correct. If the envelope alone achieves C-01 and C-03, the gate fires on bodies that are
already complete and adds no measurable correctness benefit.

**Tension: inertia-framing × scoring-granularity (V-05)**

Champion-challenger framing grounds hypotheses in specific champion failures.
Per-criterion score prediction grounds hypotheses in criterion-keyed outcome commitments.
Both improve C-07 by different mechanisms, but they may be redundant: a competitive
hypothesis that names "the champion produces directional predictions with no criterion ID
or failure condition" is already criterion-targeted by the nature of the competitive argument.
Adding a score prediction block after the fact may measure the same specificity by a
different instrument without adding evidence.

Dominant axis prediction: **inertia-framing will dominate.** If C-07 pass rate from V-03 alone
equals C-07 pass rate from V-05, the scoring-granularity axis is redundant and should not be
carried into further combination runs. The combination is most valuable when V-03 produces
competitive arguments that are specific enough to pass C-07 prose-level but not specific
enough to pass C-14 criterion-ID-level — in that case, the score prediction block closes
the remaining gap.

---

## Combination Roadmap for Round 4 (C-09)

| Priority | Axis Pair | R3 Basis | Mechanism | Criteria Targeted |
|----------|-----------|----------|-----------|-------------------|
| 1 | role-sequence × inertia-framing | V-02 (loop-gate verifier catches C-04 and C-01 inside loop) × V-03 (champion-failure framing directs C-07 before body is written) | V-02's gate narrows the contamination detection to what was just written; V-03's framing narrows what the body is trying to argue before writing begins. Combined: front-loaded competitive framing (inertia-framing) + back-loaded contamination check (role-sequence), providing coverage at non-overlapping lifecycle positions. Predicts C-01, C-04, and C-07 all improve simultaneously because direction and verification operate at distinct points without interaction. | C-01, C-04, C-07 |
| 2 | output-format × scoring-granularity | V-01 (structured envelope with `criterion-targeted:` field) × uncovered single-axis | The structured envelope already includes `criterion-targeted:` as a declared field. Adding a per-criterion score prediction block aligns the envelope's declared criterion with an expected outcome per criterion. Combined: the commitment is bidirectional — the operator declares which criterion the axis targets AND what outcome to expect on each criterion — producing the strongest C-14 pass mechanism in the variation set without requiring a specialized role. | C-03, C-07, C-14 |

---

## Anchor Designation (C-12)

**Designated anchor: V-02 (role-sequence: Loop-Gate Verifier)**

- **High structural impact**: V-02 adds a named Loop-Gate Verifier role that fires inside the
  generation loop — a structural position not present in any prior single-axis variation. A role
  that fires per-iteration (not per-run) reshapes the generation process at the variation level,
  making its effect observable per body within a single run. Role additions at loop-scope are
  the highest structural impact single-axis changes available.

- **Clean isolation**: The only change from the baseline is the addition of the Loop-Gate
  Verifier role and its per-body check protocol. No format changes, no lifecycle proportion
  shift, no inertia framing, no scoring fields. The single-axis delta is verifiable by structural
  diff: Gate present or absent, and gate position inside the loop (not post-generation).
  A post-generation review step would fail C-15 — the gate must fire per body.

- **Detectable failure**: The failure condition is specific and binary within one evaluation
  run: if C-01 pass rate for bodies generated with the loop gate equals C-01 pass rate for
  bodies generated without it (any R2 baseline), the gate adds no completeness benefit.
  This is observable without multi-round comparison — one run with the gate, one without,
  same skill body, same evaluator.

V-02 is the anchor for all R4 combination runs. The highest-priority R4 combination
(role-sequence × inertia-framing) holds the loop-gate verifier stable and adds V-03's
champion-challenger framing as the second axis.

---

## Evaluation Order Guidance (C-12)

| Priority | Variation | Axis | Evaluation Cost | Independence | Dependency Note |
|----------|-----------|------|-----------------|--------------|-----------------|
| 1 | V-01 | output-format (structured envelope) | Low — format change only; no role or phase additions | Independent | No dependency on other R3 variations. Establishes the output-format single-axis baseline that V-04 must exceed. Evaluate first to establish the C-03 and C-14 baseline. |
| 2 | V-03 | inertia-framing (champion-challenger) | Medium — introduces champion inventory and per-variation `champion-failure-targeted:` field | Independent | No dependency on V-01 or V-02. V-03's C-07 improvement claim stands alone. Evaluate before V-05: V-03 is the comparison denominator for V-05's failure condition and must be scored first. |
| 3 | V-02 | role-sequence (loop-gate verifier) | Low-Medium — one role added with per-iteration firing | Partially independent | Evaluate after V-01: if V-01's structured envelope already achieves C-01 by preventing pre-body omissions, V-02's gate is testing a correction mechanism whose failure mode may not fire. V-02's result is independently valuable for C-15 regardless of V-01's outcome. |
| 4 | V-04 | output-format × role-sequence (combination) | Medium — two mechanisms active; moderate structural complexity | Dependent on V-01 | Interpret after V-01 is scored: V-04's failure condition ("does not jointly exceed V-01 alone on C-01 and C-03") is only verifiable once V-01's single-axis baseline is established. |
| 5 | V-05 | inertia-framing × scoring-granularity (combination) | High — two mechanisms active; champion inventory + per-criterion score prediction; most complex in R3 | Dependent on V-03 | Evaluate last: V-05's failure condition ("does not jointly exceed V-03 alone on C-07") is only verifiable after V-03 is scored. The score prediction calibration in V-05's Phase 3 is most informative when V-03's actual C-07 result is known for comparison. |
