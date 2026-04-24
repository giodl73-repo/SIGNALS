# quest-rubric Variate — Round 12 (First round against rubric v8)
**Date:** 2026-03-15
**Rubric:** v8 (C-01--C-23; adds C-22: pass condition schema explicitly requires causal grounding; C-23: each recommended criterion carries a required per-criterion dimension claim)
**Target criteria:** C-22, C-23

**Round 12 design note:** Rounds 8--11 produced mechanisms for C-01 through C-21 across rubric tracks v5 and v6. Against rubric v8 specifically, the two new aspirational criteria address a gap that persisted through all Round 7 variations: C-22 (the pass condition *format rule* must explicitly state causal grounding, not merely "observable anchors") and C-23 (each recommended criterion must carry a required per-criterion Dimension field naming which quality dimension from the C-18 enumeration its pass condition tests). The Round 7 insight: all three variations had causal text templates ("without [property], [failure] occurs") that taught the pattern, yet all three scored PARTIAL on C-11 because their pass condition schema said "one auditable sentence with observable anchors" — a rule that permits count-only pass conditions decoupled from the failure boundary. C-22 requires the format rule itself to contain a causal-grounding clause. C-23 addresses a parallel gap: C-18 enumerates quality dimensions at the protocol level and C-08 requires recommended criteria to test quality, but neither requires each recommended criterion to name which dimension it tests. C-23 requires a required "Dimension:" field per recommended criterion. This round probes five mechanisms for embedding these two constraints — three single-axis and two combined — following the structural evolution pattern: taught is not required; required is not schema-enforced; schema-enforced is not per-criterion grounded.

---

## Round 12 Variation Map

| Variation | Axis | C-22 probe | C-23 probe | Notes |
|-----------|------|-----------|-----------|-------|
| V-01 | Phrasing register (constitutive pass condition schema) | Very strong — a pass condition IS constitutively a causal-grounding statement; satisfying "observable anchors" alone fails the constitutive definition; cannot be produced without the causal clause | Strong — required Dimension annotation on each recommended criterion named as structural sub-field before proceeding | Single-axis; constitutive definition cannot be satisfied by a count-only observable; risk: constitutive framing abstract enough that builders satisfy letter without testing causal boundary |
| V-02 | Output format (pass condition slot template + Dimension column) | Very strong — explicit three-slot template (Observable / Failure / Test) makes the Failure slot a blank-cell error; a count-only pass condition has no Failure value to fill | Very strong — Dimension column in recommended criteria table makes blank cell a structural violation; format-level enforcement independent of author discipline | Single-axis; structural blank-cell detection for both C-22 and C-23 simultaneously; risk: Failure slot filled with generic class description ("output incomplete") rather than specific failure mode |
| V-03 | Inertia framing (Schema-Shallow competitor) | Very strong — names the competitor that passes C-01--C-21 but whose pass condition schema says "one auditable sentence with observable anchors"; identifies the exact gap (schema and text template decoupled); builder must insert causal-grounding clause to exceed competitor | Moderate — competitor framing does not address per-criterion Dimension field; C-23 addressed by required annotation, not competitor motivation | Single-axis; competitor naming mirrors R8 V-01 (Imprecise-Quality Protocol) applied to the schema layer; risk: builder inserts causal clause in preamble, not in schema rule |
| V-04 | Role sequence + Lifecycle (Schema Definer + Dimension Enforcer) | Very strong — Schema Definer role produces binding pass condition schema with explicit causal-grounding clause before any criteria written; hard gate; Builder must satisfy schema for each pass condition | Very strong — Dimension Enforcer role reviews each recommended criterion post-draft; issues per-criterion revision instruction for blank, unlisted, or presence-only Dimension field; per-criterion gate | Combined; closes C-22 upstream (schema-level, pre-authoring) and C-23 post-draft (per-criterion, at authoring time); structurally parallel to Vocabulary Definer + Coverage Mapper (R8 V-04) applied to schema and dimension enforcement |
| V-05 | Phrasing register + Inertia framing (Two-Layer Schema Competitor) | Very strong — Schema-Shallow Protocol named before pass condition schema is written; constitutive definition distinguishes "observable anchors" (what the competitor requires) from "causal-grounding statement" (what this protocol requires); two tests provided | Very strong — Dimension-Implicit Protocol named before recommended criteria are written; constitutive definition states a recommended criterion IS a dimension-claim; Dimension field is the commitment that the Dimension-Implicit Protocol lacks | Combined; two competitors × two constitutive definitions × two phase-specific authoring moments; mirrors R8 V-05 architecture applied to v8's C-22 and C-23 |

---

## V-01 — Phrasing Register (Constitutive Pass Condition Schema)

**Axis:** Phrasing register
**Hypothesis:** Prior rounds applied constitutive definitions at escalating levels: R6 V-02 defined a criterion Text IS a contrast statement (not a preference assertion); R8 V-02 defined a quality property IS a named dimension (not a class label); R8 V-05 defined tier scope IS a stated constraint (not an inferred boundary). V-01 applies the constitutive move to the pass condition schema itself. A pass condition is not merely "one auditable sentence" or "an observable with a threshold" — a pass condition IS a causal-grounding statement. It names the specific state whose absence directly instantiates the failure mode the criterion catches. A sentence that names a count threshold without naming the failure that the count-level guards against is not a pass condition — it is a count assertion. The constitutive definition forces the schema rule to contain a causal-grounding clause (satisfying C-22) because the definition IS the causal clause: a pass condition that specifies only what is observable, without specifying why that observation catches the named failure, fails the constitutive definition and must be rewritten. V-01 also addresses C-23 by requiring each recommended criterion to carry a Dimension annotation as a required sub-field, following the per-criterion commitment pattern established in prior rounds.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden.

**A pass condition has a constitutive definition.**

A pass condition IS a causal-grounding statement. It names the specific state whose absence directly instantiates the failure mode the criterion was written to catch. Apply two tests before finalizing any pass condition:

1. **Boundary test**: Is the observable the failure boundary itself — the exact point where the output transitions from passing to failing — or is it a count threshold chosen because it correlates with failure? If replacing the count with a neighboring value (N+1 or N-1) still catches the same failure mode, the original count was a measurement choice, not the failure boundary. A pass condition whose observable is a measurement choice has not named the failure state.

2. **Absence test**: Remove the pass condition. Does the criterion text name the failure whose instantiation the pass condition was meant to catch? If yes: confirm that the observable's absence directly instantiates that failure — not as a downstream effect, but as the failure state itself. If the observable's absence only correlates with the failure (a symptom, an indicator, a proxy), the pass condition has named a measurement instruction, not a grounding statement.

A pass condition that satisfies "one auditable sentence with observable anchors" but fails both tests is not a pass condition by the constitutive definition. It is a count assertion or a symptom-detector. The constitutive definition requires causal grounding: the observable IS the failure state — its absence IS the failure.

---

**Read the skill spec.**

What does this skill produce? What lifecycle phases does it have? What does a complete correct output contain?

**Name the failure modes.** For each, assign severity and identify the failure state:

```
F-01: [failure mode] | blocking
  Failure state: [the specific state whose absence IS this failure — not a symptom
                  or correlate, but the condition that directly instantiates the
                  failure when absent. Apply the absence test: removing this state
                  from the output causes the failure by direct instantiation, not
                  via a downstream chain.]
F-02: ...
```

Minimum: 3 blocking, 2 degrading, 1 cosmetic.

DO NOT proceed to criteria until the failure state is named for every blocking failure mode and each naming survives the absence test.

---

**Build the rubric.**

Each criterion requires all five fields. The pass condition field must satisfy the constitutive definition — not merely an observable anchor:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence — "without [property], [failure] occurs because [mechanism]"
- **Weight**: essential | recommended | aspirational
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence. Must name the observable AND state the causal link: this observable's absence directly instantiates the failure mode named in the criterion text. Before finalizing: apply the boundary test and the absence test. If either fails, rewrite to name the failure boundary rather than a correlated count.

**Essential criteria (3-5):** from blocking failure modes. Derive each pass condition from the failure state named in the failure mode list, not from a count chosen to correlate with it.

**Recommended criteria (2-3):** from degrading failure modes. Before writing each recommended criterion, name the quality dimension it tests:

```
Before C-NN (recommended):
  Quality dimension tested: [degree | precision | specificity]
  Definition: [one sentence scoped to this skill — what does this dimension
               measure for outputs of this specific skill?]
  This criterion's pass condition instantiates this dimension when it asks: [question]
```

The "Quality dimension tested" block becomes a required sub-field of each recommended criterion in the output. Blank = format error. A recommended criterion that annotates a dimension but whose pass condition tests only presence (not the degree, precision, or specificity of the property's content) fails the per-criterion commitment; rewrite the pass condition before the annotation is final.

**Aspirational criteria (1-2):** Before writing, state the tier scope constraint:

```
SCOPE CONSTRAINT: Aspirational criteria must go beyond what essential and recommended
  tiers already require. A criterion that restates a lower-tier requirement — even at
  a higher threshold, a narrower pass band, or a more precisely formulated observable
  — is not aspirational. It is a tightened lower-tier criterion.
```

Each aspirational criterion carries: **Fills gap:** [the specific territory not covered by essential or recommended].

---

**Write the composite formula:**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

---

**Output:** Write to `simulations/quest/rubrics/{skill_target}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences — invoke the constitutive definition: a pass condition IS a causal-grounding statement naming the specific state whose absence directly instantiates the failure; a pass condition that specifies only a count threshold without naming the failure boundary it guards has not been defined as a pass condition but as a measurement instruction; recommended criteria commit to a named quality dimension per criterion via a required "Quality dimension tested" sub-field), then criteria ordered essential → recommended → aspirational (quality dimension annotations retained for recommended criteria; tier scope constraint retained as preamble to aspirational section; failure mode list omitted), then scoring section.

---

## V-02 — Output Format (Pass Condition Slot Template + Dimension Column)

**Axis:** Output format
**Hypothesis:** Format-level enforcement makes structural properties detectable without reading for semantic content: the six-column contrast-pair table (R7 V-02) made blank "Rejects" cells visually obvious violations independent of the author's attention. V-02 applies the same mechanism to C-22 and C-23 simultaneously. The pass condition format becomes an explicit three-slot template: (1) Observable — the state being measured; (2) Failure — the specific failure mode directly caused by this observable's absence; (3) Test — how an evaluator verifies the observable. Slot 2 is the causal-grounding clause: it names the failure mode that makes the observable non-arbitrary. A pass condition filling Slot 2 with a generic description ("output degrades," "evaluators disagree") fails the slot constraint — it must name the specific failure mode from the criterion text, with the specificity of "without [X], [failure] occurs." The criteria table for recommended criteria adds a "Dimension" column that must name one of the enumerated quality dimensions; blank = format error. Both C-22 and C-23 compliance become detectable as structural blank-cell errors without requiring evaluation of semantic content.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden.

**Read the skill spec.**

What does this skill produce? What lifecycle phases does it have? What does a complete correct output contain?

Name at least 3 failure modes. For each, assign severity: blocking, degrading, cosmetic.

---

**Pass condition template.**

Every pass condition in this rubric must use the following three-slot template. All slots are required. No slot may be blank, null, or "TBD."

```
Observable: [the specific state being measured — count threshold, named field,
             structural pattern, or explicit enumeration]
Failure:    [the specific failure mode directly caused by this observable's absence.
             Must match or trace to the failure mode named in the criterion text.
             Must be specific: "the rubric cannot function as an objective function
             because no formula exists" not "output quality degrades."
             A Failure slot naming a class of badness without naming the specific
             failure from the criterion text fails the slot constraint.]
Test:       [how an evaluator checks the observable — one auditable operation
             a third party can perform without subjective judgment]
```

The Failure slot is the causal-grounding clause. It is what distinguishes a pass condition that names a measurement (Observable + Test only) from a pass condition that names a failure boundary (Observable + Failure + Test). A pass condition satisfying only Observable and Test satisfies "observable anchors." A pass condition satisfying all three slots is causally grounded.

Before finalizing each pass condition: does the Failure slot name the specific failure mode from the criterion text? If the Failure slot says "output is worse" or "quality decreases," identify the specific failure mode and replace the generic description.

---

**Quality dimension definitions.**

Before writing recommended criteria, define each quality dimension scoped to this skill's output:

```
Degree:      [what "how much" or "how many" measures in this skill's output specifically —
              what does a count threshold test for outputs of this skill?]
Precision:   [what the pass band boundary measures in this skill's output specifically —
              what does the gap between "barely passing" and "clearly passing" mean here?]
Specificity: [what "tightly bound to this skill's artifact" means for this skill specifically —
              what observable would change if this criterion were applied to a different skill?]
```

---

**Criteria tables.**

Produce two tables — one for essential and aspirational criteria, one for recommended criteria. All columns required. No cell may be blank, null, or "TBD."

**Essential and aspirational criteria:**

| ID | Text | Weight | Category | Observable | Failure | Test |
|----|------|--------|----------|------------|---------|------|

Column rules:
- **ID**: C-NN sequential
- **Text**: one sentence — "without [property], [failure] occurs because [mechanism]"
- **Weight**: `essential` | `aspirational`
- **Category**: `correctness` | `depth` | `format` | `coverage` | `behavior`
- **Observable**, **Failure**, **Test**: the three pass condition slots. All required.

**Recommended criteria:**

| ID | Text | Weight | Category | Dimension | Observable | Failure | Test |
|----|------|--------|----------|-----------|------------|---------|------|

Same column rules, plus:
- **Dimension**: the quality dimension this criterion's pass condition instantiates — must be one of: `degree` | `precision` | `specificity` from the quality dimension definitions above. A pass condition testing only whether a field exists (not the degree, precision, or specificity of that field's content) has dimension: `presence` — which is not a valid entry. Blank Dimension cell = format error.

**Tier targets:** Essential: 3-5. Recommended: 2-3. Aspirational: 1-2. All three tiers required.

Before writing aspirational criteria, confirm that no aspirational criterion's Observable falls within territory already covered by an essential or recommended criterion — even at a higher threshold. Placement in the covered zone is a table error; reclassify or revise before finalizing the row.

---

**Scoring section.**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

---

**Output.** Write to `simulations/quest/rubrics/{skill_target}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences — state that every pass condition in this rubric carries a Failure slot naming the specific failure mode directly caused by the observable's absence; a pass condition without a Failure slot is a measurement instruction; the Dimension column commits each recommended criterion to a named quality dimension per criterion, making the commitment auditable as a cell value), then quality dimension definitions (retained), then essential/aspirational criteria table, then recommended criteria table, then scoring section.

---

## V-03 — Inertia Framing (Schema-Shallow Competitor)

**Axis:** Inertia framing
**Hypothesis:** Prior rounds named near-excellent competitors that passed all criteria up to a specific ceiling: the Correct-Tier Rubric (R5 V-05: passes C-01–C-16, fails C-17 because tier labels are correct but not traceable); the Imprecise-Quality Protocol (R8 V-01: passes C-08, fails C-18 because "quality" is named without dimensions). V-03 names a competitor that fails at the schema layer: the Schema-Shallow Protocol. It passes C-01 through C-21 — it has causal text templates, per-criterion Dimension annotations, structural gap-claim fields, a "SCOPE CONSTRAINT" block, and hard gates at phase transitions. Its single gap: the pass condition format rule says "one auditable sentence with observable anchors." This rule permits count-only pass conditions. A builder following it can comply with the causal text template in the Text field while writing a pass condition that tests "count >= N" without naming the failure mode that count guards against. The schema and the text template are decoupled: taught is not required; required is not schema-enforced. Naming this competitor before the pass condition format rule is written forces the builder to insert the causal-grounding clause that closes the gap — the same mechanism by which naming the Imprecise-Quality Protocol (R8 V-01) forced enumeration of quality dimensions.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden. Your protocol has a near-excellent competitor.

**The Schema-Shallow Protocol** is a rubric-generation protocol built using the full enforcement architecture from prior rounds. It has:
- Five-field completeness; zero blank or "TBD" entries
- Causal text templates in criterion Text fields: "without [property], [failure] occurs because [mechanism]"
- Per-criterion Dimension annotations on recommended criteria naming degree, precision, or specificity
- A "Fills gap" required field on aspirational criteria; blank = format error
- A "SCOPE CONSTRAINT" block placed structurally before aspirational authoring, explicitly naming threshold escalation as a prohibited form of aspirational distinction
- Hard gates at phase transitions; per-criterion schema compliance test before finalizing each essential criterion
- Tier assignments traceable to blocking/degrading/cosmetic severity labels

Against the v8 rubric formula, the Schema-Shallow Protocol scores approximately 96. It passes C-01 through C-21.

**Its single gap: C-22.**

The Schema-Shallow Protocol's pass condition format rule states: "one auditable sentence with observable anchors (count thresholds, named fields, structural patterns, explicit enumerations)."

This rule permits count-only pass conditions. A builder following it can comply fully with the causal text template — "without [X], [failure] occurs because [Z]" — while writing a pass condition that tests whether a count reaches a threshold without naming the failure that count-level guards against. The causal pattern is taught in the Text field instruction; it is not required in the pass condition schema. A pass condition testing "count >= 3" satisfies "observable anchors" whether or not 3 is the failure boundary or a measurement choice. The schema and the text template are decoupled.

Your protocol must close this gap. The pass condition format rule must explicitly state that the observable must be causally linked to the failure mode: its absence must directly instantiate the failure named in the criterion text, not merely correlate with it. The rule must be distinguishable from "observable anchors": it must name causal grounding as a schema-level requirement, not only as a text template guidance.

---

**Read the skill spec.**

What does this skill produce? What lifecycle phases does it have? What does a complete correct output contain?

**PHASE 1: FAILURE MODE ANALYSIS**

Name failure modes and assign severity:

```
F-01: [failure mode] | blocking
  Failure state: [the condition whose absence directly instantiates this failure —
                  not a symptom or correlate. The failure state is what the pass
                  condition must causally ground itself in.]
F-02: [failure mode] | degrading
F-03: [failure mode] | cosmetic
...
```

Minimum: 3 blocking, 2 degrading, 1 cosmetic.

DO NOT proceed to Phase 2 until every blocking failure mode has a named failure state.

**PHASE 2: PASS CONDITION SCHEMA**

Before writing any criteria, define the pass condition schema. This is the binding format rule for every pass condition in the rubric. The Schema-Shallow Protocol's schema says: "one auditable sentence with observable anchors." Your schema must go further.

Write the pass condition schema:

```
Pass condition schema for {skill_target} rubrics:

A pass condition is a causal-grounding statement. It must satisfy three requirements:

1. Observable: names a count threshold, named field, structural pattern, or explicit
   enumeration — verifiable by a third party without subjective judgment.

2. Causal grounding: the observable's absence directly instantiates the failure mode
   named in the criterion text. The observable is not merely correlated with the failure
   — its absence IS the failure state named in the criterion. The schema distinguishes
   this from "observable anchors": a pass condition satisfying observable anchors may
   name any count that correlates with the failure; a causally grounded pass condition
   names the specific count that IS the failure boundary, because below it the named
   failure directly occurs, not merely becomes more likely.

3. Falsifiability: a real output exists that fails this condition.

A pass condition satisfying requirements 1 and 3 only (observable + falsifiable) satisfies
the Schema-Shallow Protocol. A pass condition satisfying all three requirements (causally
grounded) satisfies this schema.

Schema compliance test: for each pass condition, ask — "what failure does this observable
directly cause when absent?" If the answer is "insufficient count" without naming what
insufficient count directly causes in this skill's output, the pass condition has not
identified the failure state. Rewrite to name it.
```

DO NOT write criteria until the pass condition schema is written and contains an explicit causal-grounding clause distinguishable from "observable anchors."

**PHASE 3: CRITERIA**

Build criteria following the pass condition schema. Each criterion requires all five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence — "without [property], [failure] occurs because [mechanism]"
- **Weight**: essential | recommended | aspirational
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence satisfying all three schema requirements. Before finalizing: apply the schema compliance test. If the answer to "what failure does this observable directly cause?" does not match the failure mode in the criterion text, rewrite.

**Essential criteria (3-5):** from blocking failure modes.

**Recommended criteria (2-3):** from degrading failure modes. Each required additional field:
- **Dimension:** [degree | precision | specificity] — the quality dimension this pass condition instantiates. Blank = format error. A Dimension field claiming one dimension while the pass condition tests only presence/absence fails the per-criterion commitment; rewrite before proceeding.

Before writing aspirational criteria, state:

```
SCOPE CONSTRAINT: Aspirational criteria must go beyond what essential and recommended
  tiers already require. A criterion that restates a lower-tier requirement — even at
  a higher threshold, a narrower pass band, or a more precisely formulated observable
  — is not aspirational.
```

**Aspirational criteria (1-2):** Each carries: **Fills gap:** [the specific uncovered territory].

**PHASE 4: SCORING AND OUTPUT**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

Write to: `simulations/quest/rubrics/{skill_target}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences — name the Schema-Shallow competitor and state the gap: where the Schema-Shallow Protocol's pass condition schema says "observable anchors," this rubric's schema requires the observable to causally instantiate the failure mode named in the criterion text; the delta is the causal-grounding clause — a schema requirement, not a text template guidance), then Phase 2 pass condition schema (retained in output), then criteria ordered essential → recommended → aspirational (Dimension and Fills gap fields retained; failure mode list and competitor description omitted), then scoring section.

---

## V-04 — Role Sequence + Lifecycle (Schema Definer + Dimension Enforcer)

**Axis:** Role sequence (two specialized roles) + lifecycle emphasis (phase-gated pre-authoring)
**Hypothesis:** R8 V-04 (Vocabulary Definer + Coverage Mapper) closed C-18 and C-19 simultaneously by assigning each to a dedicated pre-authoring role with a hard gate and a single exit condition: the Vocabulary Definer defined quality dimensions before recommended criteria were written; the Coverage Mapper produced the gap zone before aspirational criteria were written. V-04 applies the same dedicated-role architecture to C-22 and C-23 with two roles operating at different phases and via different mechanisms. The Schema Definer runs before any criteria are written — it produces the binding pass condition schema with an explicit causal-grounding clause, naming both the observable requirement and the causal requirement as distinct properties, and blocks progress until the schema is complete. The Dimension Enforcer does not run pre-authoring but per-criterion: it reviews each recommended criterion as the Builder drafts it and issues a revision instruction if the Dimension field is blank, names an unlisted dimension, or names a dimension while the pass condition tests only presence. The two roles operate at different scopes: the Schema Definer fixes the schema rule once (upstream, structural), while the Dimension Enforcer validates the per-criterion commitment at authoring time (per-criterion, at the moment of writing). Combined, they close C-22 at the schema layer and C-23 at the per-criterion layer — the same split as C-22 and C-23 in the rubric: C-22 is a schema-level requirement, C-23 is a per-criterion requirement.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden. Three roles operate in sequence: Analyst, Schema Definer, and Dimension Enforcer. Each role's output is a required input to the next phase. No phase begins without its required input.

---

**ANALYST ROLE**

Read the skill spec. Extract:
1. What the skill produces — artifact type, required fields, structural shape.
2. Lifecycle phases — what each phase delivers.
3. Failure modes — at least 3 blocking, 2 degrading, 1 cosmetic. Assign severity labels.

For each blocking failure mode, name:
- **Failure state**: the specific condition whose absence directly instantiates the failure — not a symptom, not a correlate. The failure state is the observable the pass condition will be grounded in.

DO NOT write criteria until the Schema Definer role is complete.

---

**SCHEMA DEFINER ROLE**

Before any criteria are written, produce the pass condition schema. This schema is the binding format rule for every pass condition in the rubric.

```
Pass condition schema for {skill_target} rubrics:

Format: one auditable sentence.

Required properties:

  Property 1 — Observable:
    Names a count threshold, named field, structural pattern, or explicit enumeration.
    Verifiable by a third party without subjective judgment.

  Property 2 — Causal grounding:
    The observable's absence directly instantiates the failure mode named in the
    criterion text. Directly means: the failure mode occurs because this state is
    absent, not merely that this state's absence correlates with the failure mode.
    The observable is the failure boundary — the exact state whose presence or
    absence determines whether the failure occurs. If replacing the observable with
    a neighboring value (count +1 or -1, field renamed, pattern relaxed) still catches
    the same failure mode, the original observable was a measurement choice, not the
    failure boundary. The failure boundary must be what is named.

  Property 3 — Falsifiability:
    An output exists that fails this condition.

A pass condition satisfying Properties 1 and 3 only is an observable-anchored
measurement instruction.
A pass condition satisfying Properties 1, 2, and 3 is a causal-grounding statement.
This schema requires all three.

Schema compliance test: for each pass condition, ask —
  "If this observable is absent from an output, what failure mode directly occurs in
   that output?" If the answer does not match the failure mode in the criterion text,
   the pass condition has not grounded the observable in the named failure.
   Rewrite to name the failure boundary, not a correlated count.
```

The Schema Definer must also enumerate quality dimensions for recommended pass conditions:

```
Quality vocabulary for recommended criteria in {skill_target} rubrics:

  Degree:
    Definition: [what "how much" or "how many" measures for outputs of this skill]
    A pass condition tests degree when it asks: [skill-specific question]
    Example: [a concrete example pass condition for this skill instantiating degree]

  Precision:
    Definition: [what the pass band boundary measures for outputs of this skill]
    A pass condition tests precision when it asks: [skill-specific question]
    Example: [a concrete example pass condition for this skill instantiating precision]

  Specificity:
    Definition: [what "tightly bound to this skill's artifact" means for this skill]
    A pass condition tests specificity when it asks: [skill-specific question]
    Example: [a concrete example pass condition for this skill instantiating specificity]
```

DO NOT write criteria until the Schema Definer output is complete: pass condition schema with explicit causal-grounding clause (Property 2) and quality vocabulary with at least 2 named dimensions, each with definition, question, and example.

---

**ANALYST ROLE (criteria authoring)**

Draft criteria following the Schema Definer's output. Each criterion requires all five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence — "without [property], [failure] occurs because [mechanism]"
- **Weight**: essential | recommended | aspirational
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence satisfying all three Schema Definer properties

After drafting each essential criterion, apply the schema compliance test. If the answer to "what failure does this observable directly cause when absent?" does not match the failure mode in the criterion text, revise before proceeding to the next criterion.

Draft recommended criteria one at a time. For each recommended criterion, include:
- **Dimension**: [name from Schema Definer quality vocabulary]

After drafting each recommended criterion, the Dimension Enforcer reviews it before the next recommended criterion is written.

DO NOT write aspirational criteria until the Coverage Mapper step is complete.

---

**DIMENSION ENFORCER ROLE**

The Dimension Enforcer reviews each recommended criterion one at a time as the Analyst drafts it. Apply the dimension diagnostic:

> "Does the Dimension field name one of the three Schema Definer quality dimensions? Does the pass condition's observable instantiate that dimension — testing its degree, precision, or specificity — or does it test only presence/absence of the property?"

For each recommended criterion failing the diagnostic:

```
C-NN Dimension field revision required:
  Current Dimension: [as stated]
  Current Pass condition: [as drafted]
  Issue: [one of:
    (a) Dimension field blank — no quality dimension committed
    (b) Dimension names a term not in the Schema Definer vocabulary
    (c) Dimension claims degree/precision/specificity but pass condition
        tests only whether the property exists, not how much/precisely/
        specifically it is present]
  Correct dimension: [name the dimension the pass condition actually tests,
                      or rewrite the pass condition to test the claimed
                      dimension as defined in the Schema Definer vocabulary]
  Instruction: Revise Dimension field or pass condition before proceeding
               to the next recommended criterion.
```

After all recommended criteria are reviewed and approved by the Dimension Enforcer, the Analyst proceeds to aspirational criteria.

---

**ASPIRATIONAL CRITERIA**

Before writing aspirational criteria, produce the coverage map:

```
SCOPE CONSTRAINT — territory already covered:

  Essential tier guards against:
    [List each blocking failure mode covered by essential criteria —
     "C-NN guards against [F-NN: failure mode]." One line per criterion.]

  Recommended tier guards against:
    [List each quality dimension covered by recommended criteria —
     "C-NN guards against [dimension: specific property]." One line per criterion.]

  Gap zone — not yet covered by essential or recommended:
    [At least 1 specific property a passing-but-not-excellent output would lack.
     Must not be reachable by tightening or combining existing criteria — must
     require a genuinely new observation. A criterion that falls in the essential
     or recommended coverage zone — even at a higher threshold — is not aspirational.]
```

Draft aspirational criteria (1-2) from the gap zone. Each requires:
- **Fills gap**: [quote the gap zone property this criterion addresses]

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

Write to: `simulations/quest/rubrics/{skill_target}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences — state the Schema Definer + Dimension Enforcer sequence: the Schema Definer defines the pass condition schema with an explicit causal-grounding clause before any criteria are written, making causal grounding a schema requirement rather than an authoring pattern; the Dimension Enforcer reviews each recommended criterion at authoring time, making per-criterion quality-dimension commitment a format constraint rather than a documentation convention; the two roles close C-22 at the schema layer and C-23 at the per-criterion layer), then Schema Definer output — pass condition schema and quality vocabulary (both retained), then coverage map (retained), then criteria ordered essential → recommended → aspirational (Dimension and Fills gap fields retained; Analyst failure mode list and Dimension Enforcer revision notes omitted from output), then scoring section.

---

## V-05 — Phrasing Register + Inertia Framing (Two-Layer Schema Competitor)

**Axis:** Phrasing register (constitutive definitions) + inertia framing (two competitors, one per target criterion)
**Hypothesis:** R8 V-05 named two competitors each failing exactly one of the target criteria (C-18: Imprecise-Quality Protocol; C-19: Implicit-Scope Protocol) and paired each with a constitutive definition at its respective authoring moment. V-05 applies the same two-competitor architecture to C-22 and C-23. Competitor 1 (Schema-Shallow Protocol) passes C-01–C-21 but fails C-22: its pass condition format rule specifies "observable anchors" without a causal-grounding clause. Competitor 2 (Dimension-Implicit Protocol) passes C-01–C-22 but fails C-23: it enumerates quality dimensions at the protocol level (C-18) and requires recommended criteria to test quality (C-08), but its recommended criterion format does not include a required Dimension field — the per-criterion commitment is absent. Each competitor is named before its respective authoring phase and paired with a constitutive definition: (1) a pass condition IS a causal-grounding statement — it names the failure state, not a measurement that correlates with it; (2) a recommended criterion IS a dimension-claim — it commits to a named quality dimension at the criterion level via a required structural field, not at the protocol level via an enumeration. The hypothesis is that two competitors × two constitutive definitions × two phase-specific authoring moments produces higher simultaneous C-22 and C-23 compliance than either mechanism alone — because the competitor makes the definition's necessity concrete (not abstract), and the constitutive definition makes the commitment's structure mandatory (not optional).

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden. Your protocol has two competitors. Each passes C-01 through their respective ceiling. Each fails exactly one of the new target criteria.

---

**Competitor 1: The Schema-Shallow Protocol**

The Schema-Shallow Protocol passes C-01 through C-21. It has causal text templates, per-criterion Dimension annotations, structural gap-claim fields on aspirational criteria, a structural "SCOPE CONSTRAINT" block, hard gates at phase transitions, and tier assignments traceable to severity labels.

Its pass condition format rule: "one auditable sentence with observable anchors (count thresholds, named fields, structural patterns, explicit enumerations)."

**Its failure:** C-22. The format rule permits count-only pass conditions. A builder following it can comply with the causal text template — "without [X], [failure] occurs because [Z]" — while writing a pass condition that tests "count >= N" without naming what failure N directly guards against. The text template teaches "without [X], [failure] occurs." The schema rule requires only "observable anchors." These are decoupled: taught is not required; required is not schema-enforced.

**A pass condition IS constitutively a causal-grounding statement.** Two tests distinguish a causal-grounding statement from an observable-anchored measurement instruction:

- **Boundary test**: Is the observable the failure boundary — the exact count or state below/beyond which the named failure directly occurs? Or is it a threshold chosen because it correlates with failure? If N+1 or N-1 would also catch the same failure, N was a measurement choice, not a boundary.
- **Absence test**: Remove the observable from the pass condition. Does the criterion text name the failure whose instantiation the observable was meant to directly catch? If yes: the observable's absence IS the failure state — it directly causes the failure, not via a downstream chain. If no: the observable was a symptom detector.

A pass condition satisfying "observable anchors" but failing both tests is a measurement instruction. The Schema-Shallow Protocol allows this. Your protocol must require causal grounding in the schema rule itself — not only in the text template.

---

**Competitor 2: The Dimension-Implicit Protocol**

The Dimension-Implicit Protocol passes C-01 through C-22. It has the Schema-Shallow Protocol's full stack plus a pass condition schema with an explicit causal-grounding clause (satisfying C-22). Its quality vocabulary is correct: it enumerates degree, precision, and specificity before recommended criteria are written (satisfying C-18). Its recommended criteria test quality properties, not just presence (satisfying C-08).

Its recommended criterion format: ID, Text, Weight, Category, Pass condition — five fields. No Dimension field.

**Its failure:** C-23. The quality dimension each recommended criterion tests is implicit — inferable from the pass condition structure but not committed to by a required field. The protocol-level enumeration (C-18) and the per-criterion quality practice (C-08) do not together require each recommended criterion to name which dimension it instantiates. An evaluator checking the output must read each pass condition and infer the dimension. Two evaluators may infer differently. The per-criterion commitment is absent.

**A recommended criterion IS constitutively a dimension-claim.** It does not merely test a quality property — it commits to a named quality dimension from the protocol's enumeration, per criterion, in a required structural field. The field is the commitment. A recommended criterion without a Dimension field is a criterion that tests some quality without committing which quality it tests. The Dimension field makes the commitment structural: it exists per criterion, its value is a specific named dimension, and its correctness is auditable against the pass condition. Blank Dimension = format error.

---

**Read the skill spec.**

Name the failure modes. Assign severity: blocking, degrading, cosmetic.

**Build the rubric.**

**Before writing any criteria:** Define the pass condition schema. Go beyond the Schema-Shallow Protocol.

```
Pass condition schema for this rubric:

A pass condition IS a causal-grounding statement. It must satisfy:
  1. Observable: count, field, pattern, or enumeration — verifiable without judgment.
  2. Causal grounding: the observable's absence directly instantiates the failure mode
     named in the criterion text. Not correlated with — directly instantiates. The
     observable IS the failure boundary. This requirement distinguishes this schema
     from the Schema-Shallow Protocol: "observable anchors" satisfies requirement 1;
     "causal grounding" requires both 1 and 2.
  3. Falsifiable: an output exists that fails this condition.

Before finalizing each pass condition: apply the boundary test and absence test.
If either fails: name the failure boundary and rewrite.
```

Draft essential criteria (3-5) from blocking failure modes.

**Before writing recommended criteria:** Name the quality dimensions. Go beyond the Dimension-Implicit Protocol by making each recommended criterion carry a required Dimension field.

```
Quality dimensions for recommended criteria:
  [Dimension 1]: [one-line definition scoped to this skill]
  [Dimension 2]: [one-line definition scoped to this skill]
```

Draft recommended criteria (2-3). Each requires five fields plus:
- **Dimension**: [name from quality dimension list above] — required. Blank = format error.

The Dimension-Implicit Protocol's recommended criteria satisfy C-08 and C-18 — quality is tested and dimensions are enumerated — but carry no Dimension field. Your recommended criteria must carry the field. The distinction: the Dimension-Implicit Protocol's quality dimension is implied by the pass condition; your recommended criterion's quality dimension is committed to by the field.

**Before writing aspirational criteria:** State the tier scope constraint.

```
SCOPE CONSTRAINT: Aspirational criteria must go beyond what essential and recommended
  tiers already require. A criterion that restates a lower-tier requirement — even at
  a higher threshold, a narrower pass band, or a more precisely formulated observable
  — is not aspirational. It is a tightened lower-tier criterion.
```

Draft aspirational criteria (1-2). Each carries: **Fills gap:** [the specific uncovered territory].

---

**Write the composite formula:**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

---

**Output:** Write to `simulations/quest/rubrics/{skill_target}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences — name both competitors and state what each constitutive definition adds: where the Schema-Shallow Protocol's pass condition schema says "observable anchors," this rubric's schema requires the observable to causally instantiate the failure mode named in the criterion text; where the Dimension-Implicit Protocol's recommended criteria imply a quality dimension, this rubric's recommended criteria commit to one via a required Dimension field; both definitions appear at their respective authoring moments — before any criteria are written and before recommended criteria are written respectively), then pass condition schema (retained), then quality dimension definitions (retained), then criteria ordered essential → recommended → aspirational (Dimension and Fills gap fields retained; tier scope constraint retained as preamble to aspirational section; failure mode list and competitor descriptions omitted), then scoring section.
