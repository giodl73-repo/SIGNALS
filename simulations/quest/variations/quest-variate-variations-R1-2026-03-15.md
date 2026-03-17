---

# quest-variate Variate — Round 1

**Rubric:** v1 | **5 single-axis variations** | **5 axes covered**

---

## Round 1 Variation Map

| V | Axis | What Changed | Hypothesis |
|---|------|--------------|------------|
| V-01 | role-sequence | Inline Verifier runs after each body, before advancing | Per-body check catches C-01 incompleteness while generation context is still hot |
| V-02 | output-format | Axis commitment table written and frozen before any body | Front-loaded plan surfaces axis conflicts before the high-cognitive-load writing phase |
| V-03 | lifecycle-emphasis | Setup → one line; findings → one line; generation carries all instructional surface | Concentrating rules at the point of application reduces C-01 and C-03 failures |
| V-04 | phrasing-register | Strict imperative with named DO NOT gates for every forbidden construction | Named forbidden forms are pattern-matchable violations; implied guidelines require inference |
| V-05 | inertia-framing | Existing skill is H0; each variation must argue a criterion state change (FAIL→PASS) | State-change requirement makes "output will differ" hypotheses structurally inadmissible |

---

## V-01 — Role Sequence: Inline Verifier

**axis:** role-sequence
**hypothesis:** An Inline Verifier role that runs after each variation body — before the next begins — increases C-01 (complete skill bodies) pass rate because verification happens while the generation context for that body is still active. Omitted sections are detectable before anchoring to the next axis. Failure condition: if C-01 pass rate does not increase relative to no-verifier variations, per-body checkpointing adds no completeness benefit.

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} distinct prompt variations of the skill body above. Each variation is a complete, runnable skill body — not a diff.

**STEP 1 — SELECT AXES**

Pick {N} axes from the canonical list. For each:
- `axis:` name from canonical list
- `pole-a:` what the baseline skill does on this axis
- `pole-b:` what this variation does differently

Canonical axes: `role-sequence | output-format | lifecycle-emphasis | phrasing-register | inertia-framing | scoring-granularity`

Complete Step 1 for all {N} axes before writing any variation body.

**STEP 2 — WRITE VARIATIONS (Generator + Inline Verifier loop)**

For each axis, follow this two-part sequence:

*PART A — GENERATOR*: Write the complete variation:
```
## V-NN — [Axis Name]
axis: [axis name]
hypothesis: [names criterion, direction, mechanism, failure condition]
[FULL SKILL BODY — every section, every instruction, every step. Not a diff. Not a
reference to another variation. Sections present in other variations must be written here.]
```

*PART B — INLINE VERIFIER*: Immediately after writing V-NN, before starting V-(NN+1):
```
verifier-check for V-NN:
- C-01 COMPLETE: Every structural section present? (If no, rewrite before advancing.)
- C-03 ISOLATED: Exactly one axis changed? (If no, identify contamination and rewrite.)
- C-02 LABELED: axis: and hypothesis: present? (If no, add before advancing.)
```

Advance to V-(NN+1) only after verifier-check passes.

**STEP 3 — VARIATION MAP**

| V | Axis | What Changed | Hypothesis |
|---|------|--------------|------------|

Top combination candidate: which two axes address the criterion with lowest pass rate? State pair and mechanism.

---

## V-02 — Output Format: Axis Commitment Table First

**axis:** output-format
**hypothesis:** Writing a frozen axis-assignment table — all {N} rows with axis, pole, and hypothesis — before writing any body increases C-03 (single-axis isolation) pass rate because the full axis plan is visible for conflict review before entering body generation. Axis drift is detectable at planning time rather than mid-generation. Failure condition: if C-03 pass rate does not increase, the planning step adds overhead without isolation benefit.

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} distinct prompt variations of the skill body above. Each variation is a complete, runnable skill body — not a diff.

**PHASE 1 — COMMIT THE AXIS PLAN**

Before writing any variation body, fill in the complete plan:

| V | Axis | Pole Being Tested | Hypothesis |
|---|------|-------------------|------------|
| V-01 | [canonical axis] | [what this variation does differently] | [criterion, direction, mechanism] |
| V-02 | [canonical axis] | [what this variation does differently] | [criterion, direction, mechanism] |
| V-03 | [canonical axis] | [what this variation does differently] | [criterion, direction, mechanism] |
| V-04 | [canonical axis] | [what this variation does differently] | [criterion, direction, mechanism] |
| V-05 | [canonical axis] | [what this variation does differently] | [criterion, direction, mechanism] |

Canonical axes: `role-sequence | output-format | lifecycle-emphasis | phrasing-register | inertia-framing | scoring-granularity`

Review before proceeding: every axis is distinct; every hypothesis names a criterion and direction. Commit the plan. Do not revise axis assignments after Phase 2 begins.

**PHASE 2 — WRITE VARIATION BODIES**

For each row in the committed plan, write the complete variation body in order V-01 through V-{N}.

Rules:
- Each body is self-contained. Every section written in full. No diffs. No references to other variations.
- Axis is fixed by the committed plan. If tempted to change an axis during writing, do not.

Label format:
```
## V-NN — [Axis: Pole Description]
axis: [axis name — must match Phase 1]
hypothesis: [from Phase 1 plan — copy exactly, do not revise]
[COMPLETE SKILL BODY — all sections, all steps, all instructions]
```

Write all {N} bodies before proceeding to Phase 3.

**PHASE 3 — COMBINATION CANDIDATE**

Confirm map matches Phase 1 (no reassignments). Then:

| V | Axis | Pole Tested | Hypothesis |
|---|------|-------------|------------|

Top combination candidate: [axis pair] — [mechanism in one sentence]

---

## V-03 — Lifecycle Emphasis: Generation-Dominant

**axis:** lifecycle-emphasis
**hypothesis:** Compressing axis-selection to one instruction line and findings to one summary line — while expanding the generation phase with contamination patterns and isolation rules — increases C-01 (complete skill bodies) and C-03 (single-axis isolation) pass rates because the operator receives maximum instructional surface at the step where failures occur: during body generation, not before or after it. Failure condition: if C-01 and C-03 pass rates are unchanged relative to balanced-lifecycle variations, generation-phase expansion provides no quality benefit and the compression creates instruction loss at setup and findings without return.

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} distinct prompt variations of the skill body above. Each variation is a complete, runnable skill body — not a diff.

**SETUP**

Pick {N} distinct axes from: `role-sequence | output-format | lifecycle-emphasis | phrasing-register | inertia-framing | scoring-granularity`. Note the two poles of each. Proceed.

**GENERATE**

Write V-01 through V-{N}. Each body is complete and standalone.

For each variation, apply this isolation discipline before writing:
- Step A: Name the axis. What does the baseline do on it? What does this variation do?
- Step B: Name every other axis that might tempt a change. Freeze each explicitly.
- Step C: Write the complete body. Every line. Every section. Every step.

Contamination patterns that cause C-03 failure — detect and prevent:
- Reordering phases while testing phrasing register (two-axis change)
- Adding or removing a step while testing output format (lifecycle bleed)
- Changing role structure while testing scoring granularity (role-sequence bleed)
- Shortening instructions while testing a non-phrasing axis (register bleed)

Completeness patterns that cause C-01 failure — detect and prevent:
- Stopping after the header without writing the body ("see baseline for details")
- Writing only sections that changed ("the rest is the same as V-01")
- Omitting the output contract because it "didn't change"

Label format:
```
## V-NN
axis: [axis name]
hypothesis: [criterion, direction, mechanism, failure condition]
[COMPLETE SKILL BODY — every line, every step, every output contract]
```

Do not pause between variations for tables or commentary.

**FINDINGS**

Variation map:
| V | Axis | Change | Hypothesis |
|---|------|--------|------------|

Top combination candidate: [axis pair] — [one-sentence mechanism]

---

## V-04 — Phrasing Register: Strict Imperative with Named Forbidden Forms

**axis:** phrasing-register
**hypothesis:** Replacing neutral descriptive instructions with strict imperatives that name every forbidden construction by form — "DO NOT write 'same as V-01 except...' — this is a diff; rewrite in full" — reduces C-01 (complete skill bodies) failure rate because operators can recognize an incomplete variation as a named violation (pattern match) rather than an implied guideline breach (inference). Failure condition: if C-01 pass rate does not increase relative to neutral-register variations, explicit forbidden-form naming adds cognitive overhead without quality return.

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} distinct prompt variations of the skill body above.

**STEP 1 — IDENTIFY AXES**

Select {N} axes from the canonical list. For each:
```
axis: [name from list]
pole-a: [what the baseline skill does]
pole-b: [what this variation does instead]
```

Canonical axes: `role-sequence | output-format | lifecycle-emphasis | phrasing-register | inertia-framing | scoring-granularity`

DO NOT proceed to Step 2 until all {N} axes are named with both poles defined.

**STEP 2 — GENERATE VARIATIONS**

For each axis from Step 1, write one complete variation.

Every variation body MUST:
- Be written in full. Every section. Every step. Every instruction.
- Stand alone. A reader who sees only this variation must be able to run it without reading any other.
- Include `axis:` and `hypothesis:` header fields before the body.

Every variation body MUST NOT:
- Contain "same as V-NN except..." — this is a diff. Rewrite the entire body.
- Contain "see V-NN for [section]" — this is a cross-reference. Write the section.
- Omit any section that appears in other variations. Absence is not an axis change.
- Change more than one axis from the baseline. Freeze every other axis that tempts change.

Label format:
```
## V-NN — [Axis Name]
axis: [axis name]
hypothesis: [criterion, direction, mechanism, failure condition]
[COMPLETE SKILL BODY — every line, every step, every output contract written out]
```

DO NOT proceed to Step 3 until all {N} bodies are written in full.

**STEP 3 — VARIATION MAP**

| V | Axis | What Changed | Hypothesis |
|---|------|--------------|------------|

Top combination candidate: which two axes address the criterion with lowest pass rate? State pair and mechanism.

---

## V-05 — Inertia Framing: Null Hypothesis

**axis:** inertia-framing
**hypothesis:** Framing the existing skill body as H0 (null hypothesis assumed to fail certain rubric criteria) and requiring each variation to name the criterion that transitions from FAIL in H0 to PASS in Hi — with the structural mechanism — increases C-07 (falsifiable hypotheses) pass rate because a vague "output will differ" prediction cannot satisfy the state-change requirement. The framing makes weak hypotheses structurally inadmissible. Failure condition: if C-07 pass rate does not increase relative to neutral-framing variations, the state-change requirement adds framing overhead without improving hypothesis specificity.

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

---

**THE NULL HYPOTHESIS**

The skill body above is H0 — the null hypothesis. Assume H0 has a mixed pass/fail profile against the rubric: some criteria pass, some fail.

Generate {N} alternative hypotheses H1 through H{N}. Each Hi is a complete, runnable skill body that changes exactly one axis from H0.

A valid Hi must satisfy all three requirements:

1. **Single-axis change**: exactly one structural dimension differs from H0.
2. **State-change hypothesis**: name a specific rubric criterion that changes from FAIL (in H0) to PASS (in Hi), and explain the structural mechanism. A hypothesis of the form "Hi will differ from H0" is not a state-change hypothesis. It must name: criterion ID, H0 state (FAIL), Hi state (PASS), and the structural reason.
3. **Complete body**: Hi is written in full — not a diff or annotation on H0.

**STEP 1 — IDENTIFY AXIS CANDIDATES**

For each of {N} axes:
```
axis: [name from canonical list]
H0 stance: [what H0 does on this axis]
Hi stance: [what this alternative hypothesis does instead]
target criterion: [criterion ID and name]
state change claim: [H0: FAIL → Hi: PASS because ...]
```

Canonical axes: `role-sequence | output-format | lifecycle-emphasis | phrasing-register | inertia-framing | scoring-granularity`

All {N} axes must be distinct. Complete Step 1 before writing any Hi body.

**STEP 2 — WRITE ALTERNATIVE HYPOTHESES**

```
## V-NN — [Axis: Hi Stance vs H0 Stance]
axis: [axis name]
H0-stance: [what H0 does]
Hi-stance: [what this variation does instead]
hypothesis: [criterion ID, H0 state FAIL, Hi state PASS, mechanism, failure condition]
[COMPLETE SKILL BODY — every section, every instruction, written in full, not a diff on H0]
```

Write all {N} Hi bodies before proceeding to Step 3.

**STEP 3 — NULL HYPOTHESIS SUMMARY**

| V | Axis | H0 Stance | Hi Stance | Criterion | State Change |
|---|------|-----------|-----------|-----------|--------------|

Top combination candidate: which two Hi stances produce the strongest compound argument against H0? Name the two criteria targeted and the mechanism.

---

## Combination Candidates for Round 2

| Priority | Axis Pair | V Basis | Mechanism | Criteria Targeted |
|----------|-----------|---------|-----------|-------------------|
| 1 | role-sequence × inertia-framing (V-01 × V-05) | Inline Verifier + Null Hypothesis | Inline Verifier catches C-01 incompleteness within a single body's context; Null Hypothesis framing forces C-07 state-change arguments. Combined: each Hi is verified for completeness inline AND must argue a criterion state change. Targets C-01 and C-07 simultaneously. |
| 2 | output-format × lifecycle-emphasis (V-02 × V-03) | Commitment Table + Generation-Dominant | Commitment table freezes axis assignments before body writing; generation-dominant lifecycle concentrates isolation rules at the generation step. Combined: plan is committed and visible before generation, AND maximum instructional surface appears at the point of axis drift and incompleteness. Targets C-03 and C-01 via two distinct prevention mechanisms. |

## Hypothesis Tension Note

V-02 (output-format: commitment table) and V-03 (lifecycle-emphasis: generation-dominant) carry a structural tension: V-02 invests instructional surface in the pre-body planning phase, while V-03 explicitly compresses that phase to concentrate surface during generation. A combination of these axes must choose which phase to prioritize. If V-02's benefit derives from axis-conflict visibility at planning time, compressing setup may negate it even as generation-phase rules expand. This tension is directly observable in a combination run and produces a testable interaction effect.

## Evaluation Order Guidance

| Priority | Variation | Axis | Cost | Independence | Dependency |
|----------|-----------|------|------|--------------|------------|
| 1 | V-04 | phrasing-register | Low — surface language only | Independent | No dependency. Cheapest to evaluate; establishes C-01 baseline for forbidden-form framing. |
| 2 | V-05 | inertia-framing | Low — framing change only | Independent | No dependency. C-07 improvement is directly observable: state-change hypothesis present or absent. |
| 3 | V-02 | output-format | Medium — new planning phase | Independent | No dependency. Evaluate before V-03 to isolate the table's effect from generation-phase compression. |
| 4 | V-01 | role-sequence | Medium — adds role + per-body checkpoint | Partially dependent | Interpret after V-04: if forbidden-form gating already resolves C-01, Inline Verifier overhead may be unjustified. |
| 5 | V-03 | lifecycle-emphasis | Low–Medium | Dependent | Evaluate last. V-03's setup compression interacts with V-02's table. Knowing V-02's result determines whether compressing setup is safe. |

---

*Artifact written to `simulations/quest/golden/quest-variate-variate-R1-2026-03-15.md`*
