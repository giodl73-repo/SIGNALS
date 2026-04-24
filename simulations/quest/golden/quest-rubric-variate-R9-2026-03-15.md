# quest-rubric Variate — Round 9 (First round against rubric v9)
**Date:** 2026-03-15
**Rubric:** v9 (C-01--C-25; adds C-24: template instruction for essential criterion text models the generic-vs-skill-specific contrast inline; C-25: causal schema includes a neighboring-value test distinguishing failure boundaries from measurement choices)
**Target criteria:** C-24, C-25

**Round 9 design note:** Round 8 (against rubric v8) achieved universal PASS on C-22 (causal grounding clause in the pass condition schema) and C-23 (per-criterion dimension claim for recommended criteria). The persistent gap from Round 12 was C-12 (all five variations PARTIAL): all variations carry the causal template "without [property], [failure] occurs" in their text authoring instructions, but none embed an inline example showing the generic-vs-skill-specific contrast alongside the template string. C-24 targets this gap at the instruction level -- the instruction that requires the pattern must also demonstrate it. C-25 targets V-04's excellence signal from Round 12: its Schema Definer Property 2 included a neighboring-value test ("if replacing the count with N+1 or N-1 still catches the same failure, the original was a measurement choice, not the failure boundary") that no other variation matched -- converting "causally linked" from an assertion into a mechanical falsification procedure. Both new criteria operate at the instruction level of the protocol, not the criterion output level: C-24 requires the essential criterion text instruction to model the contrast it requires; C-25 requires the pass condition schema to operationalize the causal clause it states. Secondary targets: C-14 (V-02 PASS only in Round 12 -- structural enforcement) and C-15 (V-04 PASS only -- per-criterion gates), both persistent weak spots. This round probes three single-axis mechanisms and two combined variations targeting C-24 and C-25 as primaries.

---

## Round 9 Variation Map

| Variation | Axis | C-24 probe | C-25 probe | Notes |
|-----------|------|-----------|-----------|-------|
| V-01 | Inertia framing (two near-excellent competitors) | Strong -- Taught-Not-Modeled Protocol named before essential-criteria authoring: has causal template, no inline contrast example; forces builder to embed the contrast model in the text instruction to distinguish from competitor | Strong -- Stated-Causal Protocol named before pass condition schema: has causal grounding clause, no falsification procedure; forces builder to include the neighboring-value test to distinguish from competitor | Single-axis; competitor framing at the instruction level (not the criterion output level); tests whether naming the gap concretely before each authoring moment produces reliable dual compliance |
| V-02 | Phrasing register (self-demonstrating instructions) | Very strong -- text instruction IS a contrast pair: "Self-demonstrating contrast: [generic example] vs. [skill-specific example]" inline; the instruction models the pattern at the point of the requirement, not in a separate section | Very strong -- pass condition schema defines causal grounding constitutively via the neighboring-value test: "a threshold is causally grounded when and only when replacing it with a neighboring value changes whether the failure mode is caught" | Single-axis; highest single-axis treatment of both targets; instructions are self-instantiating: what is required is also demonstrated at the point of requiring it |
| V-03 | Lifecycle emphasis (Contrast Contract + Threshold Verification phases) | Strong -- Contrast Contract is an explicit lifecycle phase before essential criteria: produces >= 1 generic-vs-skill-specific pair as a deliverable; the pair is retained as the instruction model for essential text authoring; DO NOT gate blocks criterion authoring until contract complete | Strong -- Threshold Verification is an explicit lifecycle phase (Stage 4) applied to each pass condition with a quantitative threshold: produces T+1/T-1 records before the criterion is finalized; the test is a phase exit condition, not a per-criterion advisory | Single-axis; analogs to Coverage Map (R8 V-03) and Vocabulary Definer (R8 V-04) applied now to the instruction-level targets of C-24/C-25 |
| V-04 | Role sequence + lifecycle (Contrast Modeler + Schema Definer) | Very strong -- Contrast Modeler is a dedicated pre-authoring role with exit gate; produces >= 2 skill-scoped contrast pairs; pairs are retained as the Builder's text instruction model; DO NOT proceed until exit condition met; per-criterion gate: text must match a Contrast Modeler pair before next criterion is authored | Very strong -- Schema Definer is a dedicated pre-authoring role with exit gate; produces the pass condition format contract with causal grounding clause AND neighboring-value test as Rule 3; DO NOT proceed until exit condition met; per-criterion: every quantitative threshold requires a recorded test result before finalization | Combined; closes C-24 and C-25 via dedicated pre-authoring roles with hard exit gates and per-criterion checks; structurally parallel to Vocabulary Definer + Coverage Mapper (R8 V-04) |
| V-05 | Phrasing register + output format (self-demonstrating + column-enforced table) | Strong -- text instruction contains inline contrast model; Contrast-Check column required for essential criteria ("not: [generic] / but: [skill-specific]"); blank = format error; two mechanisms at two levels | Strong -- pass condition schema contains neighboring-value test procedure; Threshold-Test column required for criteria with quantitative thresholds; blank = format error; two mechanisms at two levels | Combined; names Well-Structured-But-Unverified competitor to motivate both additions; tests whether column enforcement makes both properties un-skippable regardless of instruction attention |

---

## V-01 -- Inertia Framing (Taught-Not-Modeled + Stated-Causal Competitors)

**Axis:** Inertia framing
**Hypothesis:** Prior rounds named near-excellent competitors at the essential tier (Vague Rubric), the causal tier (C-11: observables but not causal failure states), the vocabulary tier (C-18: quality dimensions absent), and the scope tier (C-19: anti-overlap implied but not stated). Round 12 identified two new instruction-level gaps that all five variations share: (1) causal text template present in the essential text instruction, no inline contrast example showing generic vs. skill-specific -- C-12 all PARTIAL; (2) causal-grounding clause in pass condition schema, no mechanical falsification procedure. V-01 names both gaps as dedicated competitors placed at their respective authoring moments: the Taught-Not-Modeled Protocol (before essential criteria) forces the builder to embed an inline contrast model to distinguish; the Stated-Causal Protocol (before pass condition schema) forces the builder to include the neighboring-value test to distinguish. Hypothesis: competitor framing at the instruction level -- not the criterion output level -- produces reliable dual compliance because each competitor's failure names exactly the property the builder must add.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden. Your protocol has two competitors. Each passes C-01 through C-23. Each fails exactly one of the Round 9 target criteria.

**Competitor 1: The Taught-Not-Modeled Protocol**

Essential criterion texts use the causal template: "without [X], [failure] occurs." The instruction teaches the pattern. But the instruction contains no inline example showing what generic looks like vs. what skill-specific looks like in practice. A builder following this protocol must infer the generic-vs-skill-specific distinction without a model. One builder writes: "without complete criteria, the rubric fails" (generic -- "complete" and "fails" apply to any artifact). Another writes: "without a scoring formula, quest-golden cannot compute a composite score" (skill-specific -- names quest-golden, composite score computation). Both satisfy the template. The Taught-Not-Modeled Protocol cannot distinguish them from the instruction alone. Your text instruction must contain an inline contrast model demonstrating both, not merely state the template.

**Competitor 2: The Stated-Causal Protocol**

Pass conditions carry the causal grounding clause: "the observable must be causally linked to the failure mode." Authors write pass conditions they believe satisfy this clause. But the protocol provides no procedure to reject a threshold that is a measurement choice rather than a failure boundary. "Count of essential criteria >= 3" -- is 3 the failure boundary or a measurement choice? Both satisfy "causally linked." The Stated-Causal Protocol cannot distinguish them. Your pass condition schema must include a mechanical procedure to reject measurement-choice thresholds.

---

**Read the skill spec.**

What does this skill produce? What lifecycle phases does it have? What does a complete, correct output contain?

**PHASE 1: FAILURE MODES**

Name at least 5 failure modes. Assign severity:

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
[F-06+: additional if present]
```

Minimum: 3 blocking, 2 degrading. DO NOT proceed to Phase 2 until the list contains at least 3 blocking entries.

**PHASE 2: ESSENTIAL CRITERIA (3-5)**

Before writing essential criteria, beat the Taught-Not-Modeled Protocol. The text instruction for this rubric's essential criteria includes the following contrast model:

> **Generic formulation** (satisfies the causal template but applies to any artifact): "Without [required property], the output is non-functional." The observable could belong to any document. The failure names no specific downstream operation.
>
> **Skill-specific formulation** (applies only to this skill's artifact): "Without [observable specific to {skill_target}'s output], [{skill_target}'s specific operational function] cannot proceed." Names a concrete property of this skill's artifact and the downstream agent or function that depends on it.
>
> Example contrast for `quest-rubric`: NOT "without complete criteria, the rubric is non-functional" (generic) BUT "without a scoring formula, quest-golden cannot derive a composite score -- the rubric cannot function as an objective function" (skill-specific -- names quest-golden, composite score derivation, objective function role).
>
> For {skill_target}: identify the output properties unique to this skill's artifact. Substitute them. A text whose observable could be replaced by "a required field" without loss of meaning is generic; revise.

Template: "Without [observable specific to {skill_target}'s output], [{skill_target}'s operational function] cannot proceed."

Each essential criterion requires all five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence. Apply the contrast model above. Generic texts must be revised before drafting the next criterion.
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence. Before finalizing any quantitative threshold: apply the Pass Condition Schema (Phase 5).

DO NOT finalize an essential criterion until its Text matches the skill-specific pattern from the contrast model.

**PHASE 3: RECOMMENDED CRITERIA (2-3)**

Before writing recommended criteria, enumerate quality dimensions:

```
Quality dimensions for {skill_target} rubrics:
  [Dimension 1]: [definition scoped to this skill's output]
  [Dimension 2]: [definition scoped to this skill's output]
```

Draft recommended criteria from degrading failure modes. Each pass condition must instantiate a named dimension. Annotate: **Dimension:** [name]. Apply the Pass Condition Schema to any quantitative threshold.

**PHASE 4: ASPIRATIONAL CRITERIA (1-2)**

Before writing aspirational criteria, produce the coverage map:

```
Coverage map:
  Essential tier covers: [list of blocking failure modes guarded by essential criteria]
  Recommended tier covers: [list of quality dimensions guarded by recommended criteria]
  Gap zone: [at least 1 specific property a passing-but-not-excellent output would lack]
```

SCOPE CONSTRAINT: Aspirational criteria must fall in the gap zone. A criterion restating a lower-tier requirement -- even at a higher threshold or narrower pass band -- is not aspirational. Reclassify before proceeding.

Each aspirational criterion: standard five fields + **Fills gap**: [cite the gap from the coverage map].

**PHASE 5: PASS CONDITION SCHEMA**

Beat the Stated-Causal Protocol. Every pass condition in this rubric must satisfy all three requirements:

1. **Observable anchor**: names a specific, countable, or structurally identifiable property. Characterizations like "is clear" or "adequately covers" are not acceptable as the sole criterion.
2. **Causal grounding**: the observable's failure state directly instantiates the failure mode the criterion catches -- not a symptom, the failure itself.
3. **Neighboring-value test** (required for any quantitative threshold T):
   - Identify the failure mode F the pass condition catches.
   - If T were T+1, would the pass condition still catch F? Record: [yes / no].
   - If T were T-1, would it still catch F? Record: [yes / no].
   - If T+1 still catches F: T is a measurement choice; the actual boundary is higher. Revise to the boundary value.
   - If T-1 also catches F: T is a measurement choice; the actual boundary is lower. Revise.
   - If neither T+1 nor T-1 catches F: T is the failure boundary. Accept.
   - Record: `T=[value] | F=[failure mode] | T+1=[yes/no] | T-1=[yes/no] | verdict=[boundary/measurement-choice]`

DO NOT finalize any criterion with a quantitative threshold until the neighboring-value test record is complete and the verdict is "boundary."

**PHASE 6: SCORING AND OUTPUT**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

Write to: `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- name the two competitors and state what each addition provides: where the Taught-Not-Modeled Protocol teaches the causal template without modeling the generic-vs-skill-specific distinction inline, your text instruction embeds a contrast model at the point of the requirement; where the Stated-Causal Protocol states the causal grounding clause without a falsification procedure, your schema embeds the neighboring-value test to reject measurement-choice thresholds; both additions operate at the instruction level), then criteria ordered essential -> recommended -> aspirational (threshold test records retained as per-criterion annotations; contrast model, competitor descriptions, failure mode list, and coverage map preamble omitted), then scoring section.

---

## V-02 -- Phrasing Register (Self-Demonstrating Instructions)

**Axis:** Phrasing register
**Hypothesis:** Prior rounds applied constitutive definitional register at multiple levels: R5 V-04 defined what "essential" IS (guards against a blocking failure mode); R8 V-02 defined quality dimensions constitutively (degree, precision, specificity as named members of the quality class). V-02 applies self-demonstrating register to the Round 9 targets. For C-24: the text field instruction IS a contrast example -- the instruction that requires skill-specific formulation demonstrates the distinction inline, not in a separate section. For C-25: the pass condition schema defines causal grounding constitutively with the neighboring-value test as its definitional procedure: "a threshold is causally grounded when and only when replacing it with a neighboring value changes whether the failure mode is caught." The constitutive definition makes the test the meaning of causal grounding, not an additional check on top of it. Hypothesis: instructions that instantiate their own requirements are harder to satisfy hollowly -- an author reading an inline contrast model sees what skill-specific means rather than inferring it; an author reading a constitutive neighboring-value definition knows causal grounding means the threshold survives the test.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden.

**Read the skill spec.**

Name the failure modes. Assign severity: blocking (prevents the skill from functioning), degrading (reduces output quality without breaking function), cosmetic (presentation only). Minimum: 3 blocking, 2 degrading.

---

**ESSENTIAL CRITERIA (3-5)**

Draft essential criteria from blocking failure modes. Each criterion requires all five fields:

- **ID**: C-NN (sequential, starting at C-01)

- **Text**: One sentence -- what must be true in a passing output.

  A text is **skill-specific** when its observable would change if the skill changed. A text is **generic** when its observable applies to any artifact regardless of function.

  > **Self-demonstrating contrast (essential criterion text):**
  >
  > GENERIC: "Without a complete set of criteria, the rubric fails to evaluate outputs correctly." Nothing in this sentence belongs to {skill_target} specifically -- any artifact requiring a "complete set" of something could carry this text.
  >
  > SKILL-SPECIFIC: "Without a scoring formula, quest-golden cannot derive a composite score from criterion results -- the rubric cannot serve as an objective function." Three properties belong uniquely to quest-rubric outputs: the scoring formula (artifact property), composite score derivation (downstream operation), quest-golden (dependent agent).
  >
  > For {skill_target}: substitute the observable specific to this skill's output, the downstream operation it enables, and the agent or function that fails without it. A text whose observable could be "some required property" without losing meaning is generic; revise before drafting the next criterion.

  Form: "Without [observable specific to {skill_target}'s output], [{skill_target}'s specific operational function] fails."

- **Weight**: essential

- **Category**: correctness | depth | format | coverage | behavior

- **Pass condition**: One auditable sentence. A pass condition is **causally grounded** -- not merely observable-anchored -- when its threshold T is the failure boundary:

  > **Self-demonstrating neighboring-value test:**
  >
  > A threshold T is causally grounded when it is the smallest value such that T-1 no longer catches the same failure mode. Equivalently: T is the boundary when replacing it with T+1 does not change whether the failure is caught (T was already sufficient), AND replacing it with T-1 causes the failure mode to go uncaught (T was necessary, not convenient).
  >
  > Example: "Count of essential criteria >= 3." Failure mode: rubric cannot distinguish non-functional outputs. Apply: Does >= 4 still catch this failure? If yes, >= 3 was a measurement choice. Does >= 2 also catch it? If yes, >= 3 is still a measurement choice. Only when >= 3 is the exact value where the failure is first caught is it the failure boundary.
  >
  > Record: `T=[value] | T+1 catches failure=[yes/no] | T-1 catches failure=[yes/no] | verdict=[boundary / measurement-choice]`
  >
  > A threshold where T+1 still catches the failure is not the boundary; revise before finalizing.

  DO NOT finalize a criterion with a quantitative threshold until the test record is complete and the verdict is "boundary."

---

**RECOMMENDED CRITERIA (2-3)**

Before writing recommended criteria, define the quality dimensions constitutively:

A **quality property** is a named dimension with a direction and a pass band -- not the class label "quality." Three constitutively defined dimensions:

```
Quality dimensions for {skill_target} rubrics:

  [Dimension 1: name]
    IS: [what this dimension measures, scoped to this skill's output]
    A pass condition tests this when: [the specific question it answers for {skill_target}]

  [Dimension 2: name]
    IS: [definition]
    A pass condition tests this when: [the question]

  [optional Dimension 3 if clearly distinct and relevant]
```

Draft recommended criteria from degrading failure modes. Each pass condition must invoke a named dimension. A pass condition using "quality" as its sole criterion has not instantiated a named dimension -- revise. Annotate: **Dimension tested:** [name]. Apply the neighboring-value test to any quantitative threshold.

---

**ASPIRATIONAL CRITERIA (1-2)**

Before writing aspirational criteria, state the scope constraint:

```
SCOPE CONSTRAINT: Aspirational criteria must not cover failure modes or quality
  dimensions already covered by essential or recommended criteria. A criterion that
  tests a property already guarded by a lower tier -- even at a higher threshold,
  a narrower pass band, or a more precise formulation -- is not aspirational. Write
  aspirational criteria only for properties the lower tiers genuinely leave uncovered.
```

Draft aspirational criteria (1-2). After each, apply the coverage check: "Is there an essential or recommended criterion that guards against the same failure mode or dimension?" If yes: reclassify.

Each aspirational criterion: standard five fields + **Fills gap**: [name the specific territory not covered by essential or recommended tiers].

---

**SCORING**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

---

**OUTPUT**

Write to: `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- state the self-demonstrating principle: the text instruction models the generic-vs-skill-specific contrast inline at the point of the requirement; the pass condition schema defines causal grounding constitutively via the neighboring-value test, making the test the meaning of causal grounding rather than an additional check on top of a stated requirement; an instruction that demonstrates its own pattern is harder to satisfy hollowly than one that states the pattern without instantiating it), then criteria ordered essential -> recommended -> aspirational (threshold test records retained as per-criterion annotations; quality dimension definitions retained as recommended-tier preamble; scope constraint retained as aspirational-tier preamble), then scoring section.

---

## V-03 -- Lifecycle Emphasis (Contrast Contract + Threshold Verification Phases)

**Axis:** Lifecycle emphasis
**Hypothesis:** Prior rounds introduced lifecycle phases for pre-authoring work: R5 introduced failure-mode severity classification before tier assignment; R8 V-03 introduced the coverage map before aspirational criteria; R8 V-04 introduced Vocabulary Definer and Coverage Mapper as phase-gated steps. V-03 applies the same pattern to C-24 and C-25 with two mandatory contracts as explicit lifecycle phases. The Contrast Contract (Stage 2) runs before essential criteria and produces a generic-vs-skill-specific pair as a deliverable -- this pair becomes the instruction model for essential text authoring. The Threshold Verification Phase (Stage 4) is applied per criterion to every pass condition with a quantitative threshold and requires the neighboring-value test record before the criterion is finalized. Both are blocking gates with verifiable exit conditions. Hypothesis: explicit lifecycle phases with deliverables produce more reliable compliance than embedded instructions because they separate the pre-authoring work into a distinct step whose output cannot be skipped.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden. Build it in six stages: failure mode analysis, contrast contract, essential and recommended criteria, threshold verification, aspirational criteria, scoring and output.

**Read the skill spec.**

What does this skill produce? What lifecycle phases does it have? What does a complete correct output contain?

---

**STAGE 1: FAILURE MODE ANALYSIS**

Enumerate failure modes:

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
[F-06+: additional if present]
```

Minimum: 3 blocking, 2 degrading. DO NOT proceed to Stage 2 until the list contains at least 3 blocking entries.

---

**STAGE 2: CONTRAST CONTRACT**

Before writing essential criteria, produce a contrast record for this skill:

```
Contrast record for {skill_target}:

Generic formulation:
  [A criterion text that could appear in a rubric for any artifact. Uses language
   applicable regardless of the skill's function: "the output is incomplete",
   "a required property is absent". The observable belongs to no specific domain.]

Skill-specific formulation:
  [The same failure mode restated using an observable specific to {skill_target}'s
   output domain. Names: (1) the concrete artifact property unique to this skill,
   (2) the downstream operation or agent that depends on it, (3) the failure that
   occurs when it is absent -- all three scoped to this skill specifically.]

Distinguishing observable:
  [The property in the skill-specific formulation that would change if the target
   skill changed. Must be identifiable in an output without judgment.]
```

Exit condition: contrast record contains a non-blank Distinguishing observable naming a property specific to {skill_target}'s output domain.

DO NOT write essential criteria until the Stage 2 contrast record is complete.

The contrast record is the instruction model for essential text authoring. Essential criterion texts must match the skill-specific pattern -- the text names an observable comparable to the Distinguishing observable field. A text matching the generic formulation pattern must be revised before the next criterion is drafted.

---

**STAGE 3: ESSENTIAL AND RECOMMENDED CRITERIA**

**Essential criteria (3-5):** from blocking failure modes.

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence. Must match the skill-specific pattern from Stage 2. Names an observable specific to {skill_target}'s output domain and its downstream consequence. Generic texts (matching the Stage 2 generic formulation) must be revised before the next criterion is drafted.
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence with observable anchors. For quantitative thresholds: complete Stage 4 before finalizing.

**Recommended criteria (2-3):** from degrading failure modes.

Before writing recommended criteria, enumerate quality dimensions:

```
Quality dimensions for {skill_target} rubrics:
  [Dimension 1]: [definition scoped to this skill's output]
  [Dimension 2]: [definition scoped to this skill's output]
```

Each recommended criterion's pass condition must instantiate a named dimension. Annotate: **Dimension:** [name]. For quantitative thresholds: complete Stage 4 before finalizing.

---

**STAGE 4: THRESHOLD VERIFICATION**

For every criterion whose pass condition contains a quantitative threshold (count, proportion, named minimum), apply the neighboring-value test before finalizing:

```
Threshold verification record:

  Criterion: [C-NN]
  Pass condition: [full sentence]
  Threshold value: T = [value]
  Failure mode caught: [F-NN: description]

  Neighboring-value test:
    T+1 = [value+1]: does this threshold still catch [failure mode]? [yes / no]
    T-1 = [value-1]: does this threshold still catch [failure mode]? [yes / no]

  Verdict:
    T+1 and T-1 both still catch F: T is a measurement choice; identify the
      actual failure boundary (value where one substitution first fails) and revise.
    T+1 misses F, T-1 catches F: T is the minimum value that catches F -- failure
      boundary. Accept.
    T+1 catches F, T-1 misses F: T is above the boundary; revise downward.
    Neither T+1 nor T-1 catches F: T is the precise failure boundary. Accept.
    => Verdict: [boundary / measurement-choice -- revise to [value]]
```

DO NOT finalize a criterion until its threshold verification record is complete and the verdict is "boundary."

---

**STAGE 5: ASPIRATIONAL CRITERIA (1-2)**

Before writing aspirational criteria, produce the coverage map:

```
Coverage map:
  Essential tier covers:
    [One entry per essential criterion: "C-NN guards against [F-NN: failure mode]."]

  Recommended tier covers:
    [One entry per recommended criterion: "C-NN tests [dimension] for [property]."]

  Gap zone -- not covered by essential or recommended:
    [At least 1 specific property a passing-but-not-excellent output would lack.
     Must not be reachable by tightening or combining existing criteria.]
```

DO NOT write aspirational criteria until the gap zone names at least 1 property.

Tier scope constraint: aspirational criteria must fall in the gap zone. A criterion falling in "Essential tier covers" or "Recommended tier covers" -- even at a higher threshold -- is a placement error. Reclassify before proceeding.

Each aspirational criterion: standard five fields + **Fills gap**: [cite the gap from the coverage map]. The Fills gap field must be non-blank.

---

**STAGE 6: SCORING AND OUTPUT**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

Write to: `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- state the contract principle: the Contrast Contract makes the generic-vs-skill-specific distinction a pre-authoring deliverable rather than a runtime judgment, with the contract record serving as the instruction model for all essential criteria; the Threshold Verification record makes causal grounding a per-criterion procedure rather than a post-hoc assertion, with the test record serving as evidence that each threshold is the failure boundary; both contracts are blocking gates), then criteria ordered essential -> recommended -> aspirational (contrast record retained as essential-tier preamble; threshold verification records retained as per-criterion annotations; quality dimension enumeration retained as recommended-tier preamble; coverage map retained as aspirational-tier preamble; failure mode list omitted), then scoring section.

---

## V-04 -- Role Sequence + Lifecycle (Contrast Modeler + Schema Definer)

**Axis:** Role sequence (two dedicated pre-authoring roles) + lifecycle emphasis (phase-gated outputs as required inputs)
**Hypothesis:** C-24 and C-25 both require work before criterion authoring begins: C-24 requires an inline contrast example in the essential text authoring instruction; C-25 requires the pass condition schema to include the neighboring-value falsification procedure. V-04 structures these as dedicated pre-authoring roles with hard exit gates producing required inputs to downstream authoring. The Contrast Modeler runs before essential criteria and produces >= 2 skill-scoped contrast pairs (generic vs. skill-specific) incorporated into the Builder's text instruction. The Schema Definer runs before any pass conditions and produces the pass condition format contract with Rule 3 (neighboring-value test). Both roles have single exit conditions; no downstream phase begins without their outputs. This is structurally parallel to Vocabulary Definer + Coverage Mapper (R8 V-04) applied now to C-24/C-25. Hypothesis: dedicated pre-authoring roles with hard exit gates and per-criterion checks produce highest simultaneous compliance: the Contrast Modeler output IS the text instruction model; the Schema Definer output IS the format contract; per-criterion gates verify each criterion individually.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden. Four roles operate in sequence: Analyst, Contrast Modeler, Schema Definer, Builder. Each role's output is a required input to the next phase. No phase begins without its required input.

---

**ANALYST ROLE -- Failure Mode Enumeration**

Read the skill spec. Enumerate failure modes:

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
[additional modes as found]
```

Minimum: 3 blocking, 2 degrading.

DO NOT proceed until the failure mode list contains at least 3 blocking entries.

---

**CONTRAST MODELER ROLE**

Before essential criteria are written, produce the contrast record for this specific skill:

```
Contrast record for {skill_target}:

Pair 1:
  Generic: [a criterion text using language applicable to any artifact -- no
    observable specific to {skill_target}'s output domain]
  Skill-specific: [same failure mode using an observable that names a concrete
    property of {skill_target}'s output, the downstream function or agent that
    depends on it, and the failure that occurs when it is absent]
  Distinguishing observable: [the property in the skill-specific formulation that
    would change if the target skill changed; identifiable without judgment]

Pair 2:
  Generic: [second generic formulation]
  Skill-specific: [second skill-specific formulation]
  Distinguishing observable: [second distinguishing property]
```

Exit condition: >= 2 pairs, each with a non-blank Distinguishing observable field. Each pair scoped to this skill's actual output domain.

DO NOT proceed to Builder (essential criteria) until the Contrast Modeler exit condition is met.

---

**SCHEMA DEFINER ROLE**

Before any pass conditions are written, produce the pass condition schema for this rubric:

```
Pass condition schema for {skill_target} rubrics:

Rule 1 -- Observable anchor:
  The pass condition must name a specific, countable, or structurally identifiable
  property. Characterizations without anchors ("is clear", "adequately covers") are
  not acceptable as the sole criterion.

Rule 2 -- Causal grounding:
  The observable must be the state whose absence directly instantiates the failure
  mode the criterion catches -- not a symptom of it. The failure mode occurs because
  the observable is absent, not merely alongside it.

Rule 3 -- Neighboring-value test (required for every quantitative threshold T):
  Step 1: Identify the failure mode F this pass condition catches.
  Step 2: If T were T+1, would the pass condition still catch F? Record: [yes/no].
  Step 3: If T were T-1, would the pass condition still catch F? Record: [yes/no].
  Step 4: If T+1 still catches F: T is above the failure boundary; T was a
    measurement choice. Revise to the actual boundary value.
  Step 5: If T-1 also catches F: T is above the failure boundary; revise downward.
  Step 6: If T+1 misses F and T-1 catches F: T is the minimum value that catches F.
    Accept. Record verdict: boundary.
  Step 7: If neither T+1 nor T-1 catches F: T is the unique failure boundary.
    Accept. Record verdict: boundary.

  Record: T=[value] | T+1=[yes/no] | T-1=[yes/no] | verdict=
    [boundary / measurement-choice: revise to [value]]

  A pass condition with a quantitative threshold and no test record is incomplete.
```

Exit condition: Schema Definer output contains Rules 1, 2, and 3, with Rule 3 naming the step-by-step neighboring-value procedure including the revision instruction for measurement-choice thresholds.

DO NOT write any pass condition until the Schema Definer exit condition is met.

---

**BUILDER ROLE -- Criterion Authoring**

Draft all criteria consuming the Contrast Modeler and Schema Definer outputs.

**Essential criteria (3-5)** from blocking failure modes:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence. Must match the skill-specific pattern from the Contrast Modeler -- the observable must be comparable to the Distinguishing observable from at least one pair. A text matching the Generic column of any Contrast Modeler pair must be revised before proceeding to the next criterion.
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: must conform to the Schema Definer format template. Apply Rule 3 to any quantitative threshold before finalizing.

DO NOT finalize an essential criterion until: (a) Text matches the skill-specific pattern from the Contrast Modeler; (b) pass condition conforms to the Schema Definer format template; (c) any quantitative threshold has a complete test record with verdict "boundary."

**Recommended criteria (2-3)** from degrading failure modes:

Before writing recommended criteria, enumerate quality dimensions:

```
Quality vocabulary for {skill_target} rubrics:

  Dimension 1: [Name]
    Definition: [one sentence scoped to this skill's output]
    A pass condition tests this when it asks: [the question specific to {skill_target}]
    Example: [a concrete pass condition for this skill instantiating this dimension]

  Dimension 2: [Name]
    Definition: [one sentence]
    A pass condition tests this when it asks: [the question]
    Example: [example pass condition]
```

Minimum: 2 named dimensions. DO NOT write recommended criteria until vocabulary output contains at least 2 named dimensions.

Each recommended criterion's pass condition must instantiate a named dimension. Annotate: **Dimension tested:** [name]. Apply Schema Definer format template.

**Aspirational criteria (1-2):**

Before writing aspirational criteria, produce the coverage map:

```
Coverage map:
  Essential tier guards against:
    ["C-NN guards against [F-NN: failure mode]." -- one line per essential criterion]

  Recommended tier guards against:
    ["C-NN tests [dimension: specific property]." -- one line per recommended criterion]

  Gap zone:
    [At least 1 specific property passing essential + recommended could still lack.
     Must require a genuinely new observation. Name what a passing output could
     still lack.]
```

SCOPE CONSTRAINT (placed here, structurally, before aspirational criteria are drafted): Aspirational criteria must fall in the gap zone. A criterion falling in "Essential tier guards against" or "Recommended tier guards against" -- even at a higher threshold -- is not aspirational. Reclassify before writing aspirational criteria.

DO NOT write aspirational criteria until the coverage map contains at least 1 named gap.

Each aspirational criterion: standard five fields + **Fills gap**: [quote the gap from the coverage map]. Non-blank required.

---

**SCORING**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

---

**OUTPUT**

Write to: `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- state the Contrast Modeler + Schema Definer sequence: the Contrast Modeler produces the inline contrast pairs that make essential criterion text authoring a skill-specificity check rather than a template fill; the Schema Definer produces the causal schema with the neighboring-value test that makes pass condition authoring a boundary-identification procedure rather than an assertion; both role outputs are retained in the rubric as the authoring contracts that produced it), then Contrast Modeler output (retained as the skill-specificity record), then Schema Definer output (retained as the pass condition schema), then criteria ordered essential -> recommended -> aspirational (contrast and threshold annotations retained; quality vocabulary and coverage map retained at their tier positions; Analyst failure mode list omitted), then scoring section.

---

## V-05 -- Phrasing Register + Output Format (Self-Demonstrating + Column-Enforced Table)

**Axis:** Phrasing register (self-demonstrating instructions) + output format (tabular with mandatory validation columns)
**Hypothesis:** V-02 embeds the contrast example and neighboring-value test in prose instructions. V-05 combines self-demonstrating instructions with a structured table format that makes both properties un-skippable via dedicated required columns: **Contrast-Check** (required for essential criteria -- blank = format error) and **Threshold-Test** (required for any criterion with a quantitative pass condition -- blank = format error). The inertia framing names the near-excellent competitor: the Well-Structured-But-Unverified Protocol passes C-01 through C-23. Its text instruction states the requirement without an inline contrast model (C-24 fails). Its pass condition schema states the causal grounding clause without a neighboring-value test procedure (C-25 fails). The two added columns close both gaps simultaneously: the Contrast-Check column makes the distinction a format requirement; the Threshold-Test column makes the falsification procedure a format requirement. Both close the gap where the competitor states requirements without providing the structural evidence that satisfies them.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden.

Your output format has a near-excellent competitor: the **Well-Structured-But-Unverified Protocol**. It produces a rubric with five required fields, quality dimension annotations, a coverage map, and a scoring formula. It passes C-01 through C-23. It fails two:

- Its essential criterion text instruction states "write skill-specific texts using the causal template." No inline example shows what generic vs. skill-specific looks like. An author satisfies the template while writing a text whose observable could belong to any artifact.
- Its pass condition schema states "the observable must be causally linked to the failure mode." No procedure is provided to reject a measurement-choice threshold. An author asserts causal grounding without verifying it.

Your protocol closes both gaps.

---

**Read the skill spec.**

Name the failure modes. Assign severity: blocking, degrading, cosmetic. Minimum: 3 blocking, 2 degrading.

---

**Build the rubric as a structured table with the following required columns:**

| Column | Required for | Blank = |
|--------|-------------|---------|
| ID | all criteria | format error |
| Text | all criteria | format error |
| Weight | all criteria | format error |
| Category | all criteria | format error |
| Pass condition | all criteria | format error |
| Contrast-Check | essential criteria only | format error |
| Dimension | recommended criteria only | format error |
| Threshold-Test | any criterion with a quantitative threshold | format error |
| Fills gap | aspirational criteria only | format error |

---

**Text field instruction** (self-demonstrating):

A text is skill-specific when its observable would change if the skill changed. A text is generic when its observable applies to any artifact regardless of function.

> **Inline contrast model:**
>
> GENERIC: "Without [a required property], the output cannot fulfill its function." "Required property" and "fulfill its function" apply to any artifact -- identical language could appear in a rubric for a different skill with a different output structure.
>
> SKILL-SPECIFIC: "Without a scoring formula, quest-golden cannot derive a composite score from criterion pass/fail results -- the rubric cannot serve as an objective function." Three properties are unique to quest-rubric outputs: scoring formula (artifact property), composite score derivation (dependent operation), quest-golden (dependent agent).
>
> For {skill_target}: substitute the observable specific to this skill's output, the downstream operation it enables, and the agent or function that fails without it. A text whose observable could be replaced by "a required property" without changing its meaning is generic.

Form: "Without [observable specific to {skill_target}'s output], [{skill_target}'s specific operational function] cannot proceed."

**Contrast-Check column (required for essential criteria):**

Fill with: `not: "[the generic formulation you rejected]" / but: "[the skill-specific formulation you accepted]"`

Both entries must be present. The generic entry must be recognizably generic. The skill-specific entry must name an observable from {skill_target}'s output domain.

---

**Pass condition field instruction** (operationalized):

A pass condition is acceptable when:

1. **Observable anchor**: names a specific, countable, or structurally identifiable property.
2. **Causal grounding**: the observable's failure state IS the failure mode -- not a symptom.
3. **Neighboring-value test** (required for any quantitative threshold T):

   A threshold is causally grounded when and only when it is the failure boundary: the value where the failure mode is first caught. Equivalently: T-1 no longer catches the failure mode, AND T+1 does not require a higher value to catch it.

   > Self-demonstrating test: "Count of essential criteria >= 3." Failure mode: rubric cannot distinguish non-functional outputs. T=3. T+1=4: if >= 4 still catches this failure, then 3 was not the minimum needed. T-1=2: if >= 2 also catches this failure, then 3 was not the minimum needed. Only if >= 3 is the exact boundary (>= 2 misses, >= 3 catches) is 3 causally grounded.

**Threshold-Test column (required when pass condition contains a quantitative threshold):**

Fill with: `T=[value] | failure mode=[F-NN] | T+1 catches=[yes/no] | T-1 catches=[yes/no] | verdict=[boundary / measurement-choice: revise to [value]]`

A criterion with a measurement-choice verdict must be revised before finalization.

---

**Before writing recommended criteria**, enumerate quality dimensions:

```
Quality dimensions for {skill_target} rubrics:
  [Dimension 1]: [definition scoped to this skill's output]
  [Dimension 2]: [definition scoped to this skill's output]
```

Each recommended criterion's Dimension column must name a dimension from this enumeration. Apply Threshold-Test to any quantitative threshold.

---

**Before writing aspirational criteria**, produce the coverage map:

```
Coverage map:
  Essential tier covers: [list]
  Recommended tier covers: [list]
  Gap zone: [at least 1 named property]
```

SCOPE CONSTRAINT (placed here, structurally, before aspirational criteria are authored): Aspirational criteria must fall in the gap zone. A criterion restating a lower-tier requirement at a higher threshold or narrower pass band is a placement error -- reclassify before proceeding.

Each aspirational criterion's Fills gap column must name the gap from the coverage map. Apply Threshold-Test to any quantitative threshold.

---

**SCORING**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

---

**OUTPUT**

Write to: `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- name the Well-Structured-But-Unverified competitor and state what the two added columns provide: the Contrast-Check column makes the generic-vs-skill-specific distinction a format requirement rather than a compliance judgment -- a blank column is a format error, not a failed criterion; the Threshold-Test column makes the neighboring-value falsification procedure a format requirement rather than a stated-but-unverified causal claim; both additions close the gap where the competitor states requirements without structural evidence that they are satisfied), then quality dimension enumeration (retained as recommended-tier vocabulary record), then coverage map (retained as aspirational-tier scope record), then the rubric table (all columns per specification above), then scoring section.
