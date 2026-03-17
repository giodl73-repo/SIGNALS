# quest-variate Variate — Round 1

**Date:** 2026-03-15
**Skill:** quest-variate
**Rubric:** v1 (C-01 through C-10; essential C-01–C-05)
**Round:** R1 — single-axis pass (5 single-axis variations across 5 axes)

---

## Baseline (Reference)

The implicit baseline is a minimal, neutral-register prompt with linear steps and no roles:

```
You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} distinct prompt variations of the skill body above. Each variation is a
complete, runnable skill body — not a diff.

STEP 1 — SELECT AXES

Pick {N} axes from the canonical list. For each, define:
- What the baseline skill does on that axis (pole-A)
- What this variation does differently (pole-B)

Canonical axes: role-sequence | output-format | lifecycle-emphasis |
                phrasing-register | inertia-framing | scoring-granularity

STEP 2 — WRITE VARIATIONS

For each axis:

## V-NN — [Axis Name]
axis: [axis name]
hypothesis: [falsifiable prediction — names the rubric criterion expected to change and direction]
[full skill body — complete, standalone, not a diff]

STEP 3 — VARIATION MAP

| V | Axis | What Changed | Hypothesis |
|---|------|--------------|------------|

Identify the top combination candidate for the next round.
```

All five variations below change exactly one axis from this baseline.

---

## Round 1 Variation Map

| Variation | Axis | What Changed | Hypothesis |
|-----------|------|--------------|------------|
| V-01 | role-sequence | Inline Verifier role runs after each body before advancing | Per-body verification catches C-01 incompleteness while the generation context is still hot |
| V-02 | output-format | Axis commitment table written and frozen before any body is started | Front-loading the full axis plan reduces post-hoc rationalization and C-03 isolation failures |
| V-03 | lifecycle-emphasis | Axis-selection phase compressed to one line; generation phase carries all instructional surface | Concentrating isolation rules at the point of application reduces C-01 and C-03 failure rates |
| V-04 | phrasing-register | Strict imperative with named DO NOT gates for every forbidden construction | Named forbidden forms reduce C-01 failures more than positive-framing guidelines because they name the violation pattern |
| V-05 | inertia-framing | Existing skill body labeled as null hypothesis H0; each variation is H1 that argues a state change | Null-hypothesis framing forces C-07 compliance — an H1 that says "output will differ" cannot survive the state-change requirement |

---

## V-01 — Role Sequence: Inline Verifier

**axis:** role-sequence
**hypothesis:** An Inline Verifier role that runs immediately after each variation body is written — before the next variation begins — increases C-01 (complete skill bodies) pass rate because the verification happens while the generation context for that body is still active, making omitted sections detectable before anchoring to the next axis. Failure condition: if C-01 pass rate does not increase relative to variations generated without an inline verification step, the per-body checkpoint adds no completeness benefit and the role overhead is unjustified.

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} distinct prompt variations of the skill body above. Each variation is a
complete, runnable skill body — not a diff.

STEP 1 — SELECT AXES

Pick {N} axes from the canonical list. For each axis, write:
- axis: [name from canonical list]
- pole-a: [what the baseline skill does on this axis]
- pole-b: [what this variation does differently]

Canonical axes: role-sequence | output-format | lifecycle-emphasis |
                phrasing-register | inertia-framing | scoring-granularity

Complete Step 1 for all {N} axes before writing any variation body.

STEP 2 — WRITE VARIATIONS (with Inline Verifier)

For each axis selected in Step 1, follow this two-part sequence:

**PART A — GENERATOR**

Write the complete variation body:

## V-NN — [Axis Name]
axis: [axis name]
hypothesis: [falsifiable prediction naming rubric criterion, direction, and failure condition]
[FULL SKILL BODY — every section, every instruction, every step written out completely.
Not a diff. Not a reference to another variation. If a section appears in other variations,
it must be written here too.]

**PART B — INLINE VERIFIER**

Immediately after writing V-NN's body, and before starting V-(NN+1), check:

verifier-check for V-NN:
- C-01 COMPLETENESS: Is every structural section present? (If no, rewrite before advancing.)
- C-03 AXIS ISOLATION: Does this body change exactly one axis? (If no, identify the second
  axis and rewrite the contaminating section before advancing.)
- C-02 LABEL: Is axis: and hypothesis: declared? (If no, add before advancing.)

Advance to V-(NN+1) only after verifier-check passes for V-NN.

Repeat the PART A → PART B sequence for each of the {N} variations.

STEP 3 — VARIATION MAP

After all {N} variations have passed their verifier-check, produce:

| V | Axis | What Changed | Hypothesis |
|---|------|--------------|------------|

Identify the top combination candidate for the next round: which two axes, if combined,
are most likely to improve the criterion with the lowest pass rate across this variation set?
State the axis pair and the mechanism.

---

## V-02 — Output Format: Axis Commitment Table First

**axis:** output-format
**hypothesis:** Writing a frozen axis-assignment table (all {N} rows, each with axis, pole, and hypothesis) before writing any variation body increases C-03 (single-axis isolation) pass rate because the full axis plan is visible for conflict review before entering the high-cognitive-load body-writing phase, making axis drift detectable at planning time rather than mid-generation. Failure condition: if C-03 pass rate does not increase relative to variations generated without a pre-committed table, the up-front planning step adds coordination cost without isolation benefit.

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} distinct prompt variations of the skill body above. Each variation is a
complete, runnable skill body — not a diff.

PHASE 1 — COMMIT THE AXIS PLAN

Before writing any variation body, fill in the complete axis plan:

| V | Axis | Pole Being Tested | Hypothesis |
|---|------|-------------------|------------|
| V-01 | [axis from canonical list] | [what this variation does differently from the baseline] | [falsifiable prediction: names rubric criterion, direction, mechanism] |
| V-02 | [axis from canonical list] | [what this variation does differently from the baseline] | [falsifiable prediction: names rubric criterion, direction, mechanism] |
| V-03 | [axis from canonical list] | [what this variation does differently from the baseline] | [falsifiable prediction: names rubric criterion, direction, mechanism] |
| V-04 | [axis from canonical list] | [what this variation does differently from the baseline] | [falsifiable prediction: names rubric criterion, direction, mechanism] |
| V-05 | [axis from canonical list] | [what this variation does differently from the baseline] | [falsifiable prediction: names rubric criterion, direction, mechanism] |

Canonical axes: role-sequence | output-format | lifecycle-emphasis |
                phrasing-register | inertia-framing | scoring-granularity

Review the plan before proceeding:
- Every axis is distinct (no two rows share the same axis name).
- Every hypothesis names a rubric criterion and a predicted direction.
- No row is blank or marked "TBD."

Commit the plan. Do not revise axis assignments after Phase 2 begins.

PHASE 2 — WRITE VARIATION BODIES

For each row in the committed plan, write the complete variation body.
Write them in the order V-01 through V-{N}.

Rules:
- Each body is self-contained. Every section written in full. No diffs. No references to
  other variations. A body that omits a section present in other variations fails C-01.
- The axis for this body is fixed by the committed plan. If you feel tempted to change an
  axis during body writing, do not. Finish the body as planned.

Label format:
## V-NN — [Axis: Pole Description]
axis: [axis name — must match Phase 1 plan]
hypothesis: [from the Phase 1 plan — copy exactly, do not revise]
[COMPLETE SKILL BODY — all sections, all steps, all instructions written in full]

Write all {N} bodies before proceeding to Phase 3.

PHASE 3 — COMBINATION CANDIDATE

Confirm the variation map matches the Phase 1 commitment (no axis reassignments).
Then identify the top combination candidate: one axis pair whose combination is most likely
to produce a variation that outperforms all single-axis variations on at least one criterion.
State the mechanism in one sentence.

| V | Axis | Pole Tested | Hypothesis |
|---|------|-------------|------------|

Top combination candidate: [axis pair] — [mechanism]

---

## V-03 — Lifecycle Emphasis: Generation-Dominant

**axis:** lifecycle-emphasis
**hypothesis:** Compressing the axis-selection phase to a single instruction line and the findings phase to a single summary line while expanding the generation phase with explicit contamination patterns and isolation rules increases C-01 (complete skill bodies) and C-03 (single-axis isolation) pass rates because the operator receives maximum instructional surface precisely at the step where failures occur — during body generation — rather than before or after it. Failure condition: if C-01 and C-03 pass rates are unchanged relative to balanced-lifecycle variations, the additional generation-phase instruction surface provides no quality benefit, and the lifecycle compression adds only instruction loss at setup and findings.

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} distinct prompt variations of the skill body above. Each variation is a
complete, runnable skill body — not a diff.

SETUP

Pick {N} distinct axes from: role-sequence | output-format | lifecycle-emphasis |
phrasing-register | inertia-framing | scoring-granularity. Note the two poles of each. Proceed.

GENERATE

Write V-01 through V-{N}. Each body is complete and standalone.

For each variation, follow this isolation discipline:

Step A — Name the axis. What does the baseline do on this axis? What does this variation do?
Step B — Name every other axis that might tempt a change during body writing. Freeze each.
Step C — Write the complete body. Every line. Every section. Every step.

Contamination patterns that cause C-03 failure — detect and prevent:
- Reordering phases while testing phrasing register (two-axis change)
- Adding or removing a step while testing output format (lifecycle bleed)
- Changing the role structure while testing scoring granularity (role-sequence bleed)
- Shortening or lengthening instructions while testing a non-phrasing axis (register bleed)

Completeness patterns that cause C-01 failure — detect and prevent:
- Stopping after the axis-declaration header without writing the body ("see baseline for details")
- Writing only the sections that changed ("the rest is the same as V-01")
- Omitting the output contract or post-generation summary section because it "didn't change"

Each variation label:

## V-NN
axis: [axis name]
hypothesis: [names criterion, predicts direction and mechanism, includes failure condition]
[COMPLETE SKILL BODY — written in full, not a diff, not a reference]

Write all {N} bodies. Do not pause between variations for tables or commentary.

FINDINGS

After all {N} bodies are written, produce:

Variation map:
| V | Axis | Change | Hypothesis |
|---|------|--------|------------|

Top combination candidate: [axis pair] — [mechanism in one sentence]

---

## V-04 — Phrasing Register: Strict Imperative with Named Forbidden Forms

**axis:** phrasing-register
**hypothesis:** Replacing neutral descriptive instructions ("each variation should be complete") with strict imperative instructions that name every forbidden construction by form ("DO NOT write 'same as V-01 except...' — this is a diff; rewrite in full") reduces C-01 (complete skill bodies) failure rate because operators can recognize an incomplete variation as a named violation rather than an implied guideline breach. The failure mode is visible as a pattern match, not an inference. Failure condition: if C-01 pass rate does not increase relative to neutral-register variations, explicit forbidden-form naming provides no advantage over implied completeness norms, and the additional negative framing adds cognitive overhead without quality return.

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} distinct prompt variations of the skill body above.

STEP 1 — IDENTIFY AXES

Select {N} axes from the canonical list. For each:
  axis: [name from list]
  pole-a: [what the baseline skill does]
  pole-b: [what this variation does instead]

Canonical axes: role-sequence | output-format | lifecycle-emphasis |
                phrasing-register | inertia-framing | scoring-granularity

DO NOT proceed to Step 2 until all {N} axes are named with both poles defined.

STEP 2 — GENERATE VARIATIONS

For each axis from Step 1, write one complete variation.

Every variation body MUST:
- Be written in full. Every section. Every step. Every instruction.
- Stand alone. A reader who sees only this variation must be able to run it without
  reading any other variation.
- Include the axis: and hypothesis: header fields before the body.

Every variation body MUST NOT:
- Contain "same as V-NN except..." — this is a diff. Rewrite the entire body.
- Contain "see V-NN for [section]" — this is a reference. Write the section.
- Omit any section that appears in other variations. Absence is not a valid axis change.
- Change more than one axis relative to the baseline. Multiple simultaneous axis changes
  produce contaminated data. If a second axis tempts change, freeze it.

Label format for each variation:

## V-NN — [Axis Name]
axis: [axis name]
hypothesis: [falsifiable prediction: names criterion, direction, mechanism, failure condition]
[COMPLETE SKILL BODY — every line, every step, every output contract instruction written out]

DO NOT proceed to Step 3 until all {N} variation bodies are written in full.

STEP 3 — VARIATION MAP

| V | Axis | What Changed | Hypothesis |
|---|------|--------------|------------|

Top combination candidate: the two axes whose combination is most likely to address the
criterion with lowest pass rate in this variation set. State the pair and mechanism.

---

## V-05 — Inertia Framing: Null Hypothesis

**axis:** inertia-framing
**hypothesis:** Framing the existing skill body as H0 (the null hypothesis, assumed to fail certain rubric criteria) and requiring each variation to argue a state change — naming which criterion transitions from FAIL in H0 to PASS in H1 and the mechanism — increases C-07 (falsifiable hypotheses) pass rate because a hypothesis that only says "output will differ" cannot satisfy the H1 requirement of a named state change. The framing makes vague directional predictions structurally inadmissible. Failure condition: if C-07 pass rate does not increase relative to neutral-framing variations, the null-hypothesis requirement adds framing overhead without improving hypothesis specificity, and the criterion-state-change form should not be carried into combination runs.

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

---

**THE NULL HYPOTHESIS**

The skill body above is H0 — the null hypothesis. H0 is the current state. Assume H0 has
a mixed pass/fail profile against the rubric: some criteria pass, some fail.

Your task is to generate {N} alternative hypotheses (H1 through H{N}). Each Hi is a
complete, runnable skill body that changes exactly one axis from H0.

A valid Hi must satisfy all three of the following:

1. **Single-axis change**: exactly one structural dimension differs from H0.
2. **State-change hypothesis**: the hypothesis for Hi must name a specific rubric criterion
   that Hi changes from FAIL (in H0) to PASS (in Hi), and explain the mechanism.
   A hypothesis of the form "Hi will produce different output" is not a state-change
   hypothesis. It must name: criterion ID, current state in H0 (FAIL), predicted state in
   Hi (PASS), and the structural reason the state changes.
3. **Complete body**: Hi is written in full — not a diff or annotation on H0.

---

STEP 1 — IDENTIFY AXIS CANDIDATES

For each of {N} axes you plan to vary, produce:

axis: [name from canonical list]
H0 stance: [what H0 does on this axis]
Hi stance: [what this alternative hypothesis does instead]
target criterion: [criterion ID and name]
state change claim: [H0 state: FAIL → Hi state: PASS because ...]

Canonical axes: role-sequence | output-format | lifecycle-emphasis |
                phrasing-register | inertia-framing | scoring-granularity

All {N} axes must be distinct. Complete Step 1 before writing any Hi body.

STEP 2 — WRITE ALTERNATIVE HYPOTHESES

For each axis from Step 1, write the complete Hi body:

## V-NN — [Axis: Hi Stance vs H0 Stance]
axis: [axis name]
H0-stance: [what H0 does on this axis]
Hi-stance: [what this variation does instead]
hypothesis: [state-change claim: criterion ID, H0 state, Hi state, mechanism, failure condition]
[COMPLETE SKILL BODY — every section, every instruction, fully written, not a diff or delta on H0]

Write all {N} Hi bodies before proceeding to Step 3.

STEP 3 — NULL HYPOTHESIS SUMMARY

After all {N} Hi bodies are written:

| V | Axis | H0 Stance | Hi Stance | Criterion Targeted | State Change Predicted |
|---|------|-----------|-----------|-------------------|----------------------|

Top combination candidate: which two Hi stances, if combined, produce the strongest compound
argument against H0? Name the two criteria they jointly target and the mechanism.

---

## Combination Candidates for Round 2

| Priority | Axis Pair | V Basis | Mechanism | Criteria Targeted |
|----------|-----------|---------|-----------|-------------------|
| 1 | role-sequence × inertia-framing (V-01 × V-05) | Inline Verifier + Null Hypothesis | The Inline Verifier catches C-01 incompleteness within a single variation's generation context; the Null Hypothesis framing forces C-07 compliance by requiring state-change arguments. Combined: each Hi body is verified for completeness inline AND its hypothesis must argue a criterion state change. Targets C-01 and C-07 simultaneously, addressing the two highest-failure-rate criteria in the variation generation task. |
| 2 | output-format × lifecycle-emphasis (V-02 × V-03) | Commitment Table + Generation-Dominant | The commitment table (V-02) freezes axis assignments before body writing begins; the generation-dominant lifecycle (V-03) concentrates isolation rules at the generation step. Combined: the plan is committed and visible before generation starts, AND the most instructional surface appears exactly where axis drift and incompleteness occur. Targets C-03 isolation and C-01 completeness via two distinct prevention mechanisms (planning vs. real-time instruction). |

## Hypothesis Tension Note

V-02 (output-format: commitment table) and V-03 (lifecycle-emphasis: generation-dominant)
have a structural tension: V-02 invests instructional surface in the planning phase
(pre-body), while V-03 explicitly *compresses* the pre-body phase to concentrate surface
in generation. A combination of these axes requires choosing which phase to prioritize —
the combination will produce a different effect depending on whether the commitment table
or the generation-phase rules are emphasized. This tension is observable in the combination
run: if the commitment table's benefit comes from axis-conflict visibility at planning time,
compressing setup may negate that benefit even as it amplifies generation-phase rules.

## Evaluation Order Guidance

| Priority | Variation | Axis | Cost | Independence | Dependency |
|----------|-----------|------|------|--------------|------------|
| 1 | V-04 | phrasing-register | Low — surface language only, no structural addition | Independent | No dependency. Cheapest to evaluate; establishes C-01 baseline for forbidden-form framing. |
| 2 | V-05 | inertia-framing | Low — framing change only, no structural addition | Independent | No dependency. C-07 improvement is directly observable: state-change hypothesis present or absent. |
| 3 | V-02 | output-format | Medium — new phase structure (table before bodies) | Independent | No dependency. Evaluate before V-03 to isolate the table's effect from generation-phase compression. |
| 4 | V-01 | role-sequence | Medium — adds a role and per-body checkpoint | Partially dependent | Interpret after V-04: if forbidden-form gating (V-04) already resolves C-01, the Inline Verifier's added overhead may not be justified. |
| 5 | V-03 | lifecycle-emphasis | Low–Medium | Dependent | Evaluate last: V-03's compression of the setup phase interacts with V-02's table. Knowing V-02's result first determines whether compressing setup is safe. |
