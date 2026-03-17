# quest-variate Variate — Round 2

**Date:** 2026-03-15
**Skill:** quest-variate
**Rubric:** v2 (C-01 through C-14; essential C-01–C-05)
**Round:** R2 — 3 single-axis passes + 2 combination passes (explicit combination run; C-04 combination exception applies)

---

## Round 2 Variation Map

| Variation | Axis | Pass Type | What Changes | Criteria Targeted |
|-----------|------|-----------|--------------|-------------------|
| V-01 | role-sequence | single-axis | Scorekeeper role maps rubric criteria → skill elements before generation; `scorekeeper-check:` field per variation | C-01, C-08 |
| V-02 | output-format | single-axis | YAML envelope preceding each body declares axis, pole, hypothesis, and `baseline-delta:` | C-03, C-07 |
| V-03 | lifecycle-emphasis | single-axis | Findings phase expanded with per-pair combination analysis and dependency-aware evaluation ordering | C-09, C-10 |
| V-04 | role-sequence × inertia-framing | combination (R1 Priority 1) | Critic catalogs champion-specific weaknesses; Generator writes challengers targeting those weaknesses | C-04, C-07 |
| V-05 | output-format × lifecycle-emphasis | combination (R1 Priority 2) | Map committed before any body is written; execute phase carries explicit isolation rules | C-04, C-05 |

**Anchor designation (C-12):** V-01. See anchor section at end.

---

## V-01 — Role Sequence: Scorekeeper-First

**axis:** role-sequence
**hypothesis:** A Scorekeeper role that maps each essential rubric criterion to its structural element in this skill produces a per-variation completion checklist that increases C-08 (structural fidelity) pass rates because the operator verifies element presence criterion-by-criterion rather than by global impression. Failure condition: if C-08 pass rate across generated variations does not increase relative to variations generated without a Scorekeeper role, the criterion-element mapping adds no structural completeness benefit and should not be carried forward into combination runs.

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations.

--- ROLE: SCOREKEEPER ---

Before writing any variation body, produce a criterion-element map for this specific skill.
For each essential rubric criterion, name the structural element in this skill body that satisfies it.

| Criterion | What it requires | Element in this skill that satisfies it |
|-----------|-----------------|------------------------------------------|
| C-01 Completeness | Every variation is full and standalone | [name the section most likely to be omitted in this skill] |
| C-02 Count | Exactly {N} variations labeled V-01 through V-{N} | [label format this skill uses] |
| C-03 Axis declaration | axis: and hypothesis: present in every variation | [location in this skill's variation header] |
| C-04 Single-axis isolation | Exactly one structural element changes per variation | [the structural decision most likely to co-vary accidentally in this skill] |
| C-05 Axis diversity | No two variations share the same axis | [the axis pair most likely to be confused in this skill's domain] |

Complete the map before proceeding. This map is the completion checklist used during body generation.

--- ROLE: GENERATOR ---

Using the Scorekeeper's criterion-element map, write V-01 through V-{N}.

For each variation:
1. Select one axis from the canonical list. No two variations may share the same axis.
2. Declare axis and hypothesis. Hypothesis must name a rubric criterion, the predicted direction, and an explicit failure condition: what outcome would disprove the prediction.
3. Write the complete skill body. Every section. Every instruction. No diffs. No cross-references to other variations.
4. Before advancing to the next variation, run the Scorekeeper checklist: verify each criterion element from the map is present in the body just written.

Canonical axes: role-sequence | output-format | lifecycle-emphasis |
                phrasing-register | inertia-framing | scoring-granularity

Label format for each variation:

## V-NN — [Axis Name]
axis: [axis name]
hypothesis: [falsifiable prediction naming rubric criterion, direction, and failure condition]
scorekeeper-check: [list C-01 through C-05 elements verified present in this body]
[full skill body — complete and standalone]

--- ROLE: SYNTHESIZER ---

After all {N} bodies are written:

1. Variation map:

| V | Axis | What Changed | Hypothesis |
|---|------|--------------|------------|

2. Combination candidate: which two axes, combined, would most likely address the criterion currently weakest across all {N} variations? Name the criterion, the axis pair, and the mechanism.

3. Anchor designation: identify one variation as the structural anchor for all subsequent combination runs. The anchor must have high structural impact, clean single-axis isolation, and a detectable failure condition. State which variation is the anchor and justify each criterion.

---

## V-02 — Output Format: YAML Variation Envelope

**axis:** output-format
**hypothesis:** A YAML envelope preceding each skill body forces the operator to commit field-level declarations — including `baseline-delta:`, which names the single structural element that changed — before writing the body, reducing post-hoc axis rationalization and increasing C-03 (axis declaration) completeness because the envelope's required fields cannot be silently omitted. Failure condition: if C-03 pass rate and C-07 (hypothesis specificity) do not improve relative to variations generated without a YAML envelope, the structured pre-body commitment adds no declaration quality benefit and the field format should not be carried forward.

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each variation changes exactly one axis.

STEP 1 — AXIS SELECTION

Read the skill spec. Select {N} distinct axes, one per variation.
For each axis:
  axis: [name from canonical list]
  pole-a: [what the baseline skill body does on this axis]
  pole-b: [what this variation does differently]

Canonical axes: role-sequence | output-format | lifecycle-emphasis |
                phrasing-register | inertia-framing | scoring-granularity

No two variations may share the same axis. Complete Step 1 before writing any body.

STEP 2 — GENERATE VARIATION BODIES

For each axis selected in Step 1, write one complete variation body.
Each body must include all structural sections present in the others.
No diffs. No cross-references. Every section written in full.

Precede each skill body with a YAML envelope:

```yaml
variation: V-NN
axis: [axis name]
pole: [pole-b description — the single change this variation makes]
hypothesis: [falsifiable prediction: which criterion changes, in which direction, by what mechanism, and what outcome would disprove it]
baseline-delta: [one sentence naming the single structural element that differs from the baseline]
```

[COMPLETE SKILL BODY — all sections, all steps, all instructions written in full]

The YAML envelope declares structure. The skill body following it is complete, runnable prose/markdown. A body that omits sections present in other variations fails C-01 regardless of what the envelope declares.

STEP 3 — COMBINATION ANALYSIS

After all {N} bodies are written:

Variation summary:

| V | Axis | Pole Tested | Hypothesis |
|---|------|-------------|------------|

Top combination candidate: one axis pair, one-sentence mechanism stating which criteria the combination would jointly improve.

---

## V-03 — Lifecycle Emphasis: Findings-Heavy

**axis:** lifecycle-emphasis
**hypothesis:** Expanding the findings phase with per-pair combination analysis and dependency-aware evaluation ordering increases C-09 (combination readiness) and C-10 (evaluation order guidance) pass rates because the operator receives instructional surface precisely where synthesis failures occur — not during generation, but during post-generation analysis. Failure condition: if C-09 and C-10 pass rates are unchanged relative to compressed-findings variations, expanding the findings phase has no quality effect on combination guidance or ordering, and the lifecycle proportion should not be carried into combination runs.

---

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, single-axis skill body variations.

SETUP

Read the spec. Select {N} axes from the canonical list, one per variation:
role-sequence | output-format | lifecycle-emphasis |
phrasing-register | inertia-framing | scoring-granularity

Proceed.

GENERATE

Write V-01 through V-{N}. Each body is complete and standalone. No diffs.

## V-NN
axis: [axis name]
hypothesis: [concrete prediction — names criterion, direction, mechanism, and explicit failure condition]
[full skill body — every section, every instruction]

FINDINGS

After all {N} bodies are written:

**Variation map:**

| V | Axis | Change | Hypothesis |
|---|------|--------|------------|

**Combination pair analysis:**

For each distinct axis pair present in the variation map:
- Name the pair.
- State which rubric criterion each single-axis variation targets.
- State the compound hypothesis: if both axes are active simultaneously, which criterion improves beyond what either axis achieves alone?
- Assign priority: HIGH / MEDIUM / LOW with one-sentence rationale.

List all pairs before naming the top candidate.

**Evaluation order:**

Rank the {N} variations in evaluation sequence. For each:
- Evaluation cost: how structurally complex is this variation's change?
- Independence: can this hypothesis be tested without knowing other variations' results?
- Dependency: which other variation's result would change the interpretation of this outcome?

Name the variation that, evaluated first, maximizes information gained per subsequent run.

---

## V-04 — Combination: Role Sequence × Inertia Framing

**axis:** role-sequence × inertia-framing
**pass-type:** combination (R1 Priority 1 — V-04 Critic-Before-Generator + V-05 Champion-Challenger)
**hypothesis:** Combining a Critic role that catalogs champion-specific failure modes with challenger framing that requires each hypothesis to argue improvement over the champion increases C-04 (single-axis isolation) and C-07 (hypothesis specificity) simultaneously: the Critic narrows the contamination search space to this champion's specific structure, while challenger framing eliminates "output will differ" hypotheses by forcing improvement arguments. Failure condition: if C-04 and C-07 pass rates do not jointly exceed those of both R1 single-axis baselines (R1 V-04 and R1 V-05), the combination provides no compound benefit and these axes should remain as independent single-axis variations only.

---

**Combination pass: role-sequence × inertia-framing**
*Both axes are active in the generation process. Generated variations are still single-axis — each varies one axis from the champion. The combination applies to the generation process structure, not to the variations themselves.*

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations.

--- ROLE: CRITIC (examining the champion) ---

The skill body above is the champion — the current status quo.

Examine the champion and produce:

1. The three rubric criteria where the champion is weakest. For each:
   - Criterion ID and name.
   - What the champion currently does that produces weakness on this criterion.
   - The axis that, if varied, most directly addresses this weakness.

2. For each of those three axes: the contamination pattern most likely to appear
   if that axis is varied while another structural dimension also drifts.

Write the Critic output in full before proceeding to the Generator role.

--- ROLE: GENERATOR (building challengers) ---

Each variation is a challenger to the champion. A valid challenger:
1. Changes exactly one axis from the champion (single-axis isolation preserved).
2. Has a hypothesis that names the criterion it improves, the mechanism of improvement,
   and the champion weakness being exploited.
3. Does not regress on any criterion the champion currently passes.
4. Is a complete, standalone skill body — not a diff or annotation.

A hypothesis of the form "this variation will differ" is not a valid challenger hypothesis.
It must argue a concrete improvement. It must also name an explicit failure condition: what
outcome would disprove that the challenger improves over the champion.

Canonical axes: role-sequence | output-format | lifecycle-emphasis |
                phrasing-register | inertia-framing | scoring-granularity

For each challenger:

## V-NN — [Axis: Challenger Stance]
axis: [axis name]
champion-stance: [what the champion does on this axis]
challenger-stance: [what this variation does instead]
hypothesis: [argument against the champion — names criterion, mechanism, champion weakness exploited, and failure condition]
critic-check: [confirms this challenger addresses a Critic-named weakness without introducing a Critic-named contamination pattern]
[full skill body — complete, standalone, not a diff]

--- ROLE: SYNTHESIZER ---

After all {N} challengers are written:

Challenger summary:

| V | Axis | Champion Stance | Challenger Stance | Criterion Targeted | Predicted Outcome |
|---|------|-----------------|-------------------|-------------------|-------------------|

Combination candidate: which two challengers, if their stances were combined, produce the
strongest compound argument against the champion? Name the criterion compound effect and
the mechanism by which both stances reinforce each other.

Anchor designation: identify one challenger as the structural anchor for all subsequent
combination runs. The anchor must meet all three criteria:
- High structural impact: its axis adds or removes a role, phase, or contract element.
- Clean isolation: its single-axis change is verifiable without ambiguity.
- Detectable failure: its hypothesis negation condition is observable within one evaluation run.

State which challenger is the anchor and justify each of the three anchor criteria explicitly.

---

## V-05 — Combination: Output Format × Lifecycle Emphasis

**axis:** output-format × lifecycle-emphasis
**pass-type:** combination (R1 Priority 2 — V-02 Map-First + V-03 Execute-Heavy)
**hypothesis:** Combining map-first output format (axis assignment committed in a table before any body is written) with execute-heavy lifecycle emphasis (expanded isolation rules during generation) increases C-04 (single-axis isolation) and C-05 (axis diversity) simultaneously: the committed map prevents mid-generation axis reassignment, while the expanded isolation rules reduce within-body contamination during writing. Failure condition: if C-04 and C-05 pass rates do not jointly exceed those achieved by the map-first variation alone (R1 V-02), the execute-heavy addition does not compound the map-first benefit and the lifecycle expansion adds only cost.

---

**Combination pass: output-format × lifecycle-emphasis**
*Map-first structure (output-format axis) is the planning scaffold. Execute-heavy isolation rules (lifecycle-emphasis axis) govern body generation. Both axes are active.*

You are running /quest:variate for Signal skill: {skill-name}

Skill description:
{skill-description}

Current rubric ({rubric-version}):
{rubric-content}

Generate {N} complete, runnable skill body variations. Each varies exactly one axis.

PHASE 1 — COMMIT THE VARIATION MAP

Before writing any skill body:

a. Name {N} axes from the canonical list, one per row. No two rows may share an axis.
b. For each axis, define its two poles in this skill's context.
c. Write the hypothesis for each row. Hypothesis must name a rubric criterion, predict direction, and include an explicit failure condition.
d. Finalize the map:

| V | Axis | Pole Being Tested | Hypothesis |
|---|------|-------------------|------------|
| V-01 | [axis] | [pole description] | [falsifiable prediction with failure condition] |
| V-02 | [axis] | [pole description] | [falsifiable prediction with failure condition] |
| V-03 | [axis] | [pole description] | [falsifiable prediction with failure condition] |
| V-04 | [axis] | [pole description] | [falsifiable prediction with failure condition] |
| V-05 | [axis] | [pole description] | [falsifiable prediction with failure condition] |

Canonical axes: role-sequence | output-format | lifecycle-emphasis |
                phrasing-register | inertia-framing | scoring-granularity

Review: every axis is distinct. Every hypothesis names a criterion and a failure condition.
Commit the map. Do not revise axis assignments after Phase 2 begins.

PHASE 2 — GENERATE VARIATION BODIES

For each row in the committed map, write the complete skill body.

Axis isolation — apply actively for each body:
Step A: Identify the axis for this variation from the committed map.
Step B: Identify what the baseline body does on that axis.
Step C: Name every other axis that might tempt change. Freeze each explicitly.
Step D: Change only the committed axis. Write the full body.

Contamination patterns to detect and block:
- Changing phrasing register while reordering phases (two-axis change)
- Adding a step while testing output format (lifecycle-emphasis bleed)
- Removing a role while reformatting output (role-sequence + output-format bleed)
- Shortening instructions while testing scoring granularity (phrasing-register bleed)

Label format:

## V-NN — [Axis: Pole Description]
axis: [axis name]
hypothesis: [from the committed map — do not revise during body writing]
[COMPLETE SKILL BODY — every section, every instruction, fully written]

Do not stop between variations to revise the map or add summaries. Write all {N} bodies.

PHASE 3 — FINDINGS

After all {N} bodies are written:

1. Variation map (confirm against Phase 1 commitment — no axis reassignments):

| V | Axis | Change | Hypothesis |
|---|------|--------|------------|

2. Top combination candidate: one axis pair, one-sentence mechanism.

---

## Combination Candidates for Round 3

| Priority | Axis Pair | V-NN Basis | Mechanism | Criteria Targeted |
|----------|-----------|------------|-----------|-------------------|
| 1 | role-sequence × scoring-granularity | V-01 × uncovered | Scorekeeper maps rubric criteria to elements (V-01); a scoring-granularity variation adds per-criterion inline score fields to the output contract. Combined: each variation body carries a Scorekeeper completion map AND the output contract has per-criterion score slots, producing evidence at two levels of verification simultaneously. | C-08 structural fidelity, C-07 hypothesis specificity |
| 2 | output-format × role-sequence | V-02 × V-01 | YAML envelope (V-02) forces field-level declaration including `baseline-delta:`; Scorekeeper role (V-01) verifies element presence via criterion-element map. Combined: the envelope's required fields align with the Scorekeeper's map, making the pre-body commitment and the post-body verification coherent. | C-01 completeness, C-03 axis declaration, C-08 structural fidelity |

---

## Anchor Designation

**Designated anchor: V-01 (role-sequence: Scorekeeper-First)**

Rationale against the three anchor criteria:

- **High structural impact**: V-01 adds a named Scorekeeper role — a distinct phase not present in the baseline. Role additions are the most structurally significant single-axis change available: they reshape how every downstream section is generated and verified, which means their effect is observable across all five essential criteria, not just one.

- **Clean isolation**: The only change from the baseline is the insertion of the Scorekeeper role and its `scorekeeper-check:` field. No format, lifecycle proportion, phrasing register, or framing element changes. The single-axis delta is verifiable by structural diff: Scorekeeper present or absent.

- **Detectable failure**: The hypothesis failure condition is explicit and binary — if C-08 pass rate does not increase relative to no-Scorekeeper variations within the same evaluation run, the role is ineffective. This does not require multi-round comparison; it is observable in the first run that includes a Scorekeeper and a non-Scorekeeper variation.

V-01 is the anchor for all R3 combination runs. Combination pairings should hold the Scorekeeper role stable and vary one additional axis (scoring-granularity is the highest-priority candidate per the R3 combination table above).

---

## Evaluation Order Guidance

| Priority | Variation | Axis | Evaluation Cost | Independence | Dependency Note |
|----------|-----------|------|-----------------|--------------|-----------------|
| 1 | V-01 | role-sequence (Scorekeeper) | Low — one role added, behaviorally contained | Independent | No dependency on other variations. Establishes anchor baseline. |
| 2 | V-02 | output-format (YAML envelope) | Low — format change only, no role or phase addition | Independent | No dependency. Cheapest format-axis test; isolates C-03/C-07 effect cleanly. |
| 3 | V-05 | output-format × lifecycle-emphasis (combination) | Medium — two axes active, no role changes | Partially dependent | Interpret after V-02: if V-02 alone resolves C-04, the combination's lifecycle addition contributes no additional benefit. |
| 4 | V-04 | role-sequence × inertia-framing (combination) | High — two roles active (Critic + Challenger framing), structurally complex | Partially dependent | Interpret after V-01: if V-01's Scorekeeper role already improves C-08, V-04 must justify its added complexity by compound gains on C-04 + C-07, not just C-08. |
| 5 | V-03 | lifecycle-emphasis (findings-heavy) | Medium — phase proportion shift only | Dependent | Evaluate last: V-03's per-pair combination analysis is most valuable when the rest of the variation set's results are known. Evaluated early, it analyzes hypothetical pairs; evaluated last, it analyzes real data. |
