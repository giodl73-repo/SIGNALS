# quest-rubric Variate — Round 8 (First round against rubric v6)
**Date:** 2026-03-15
**Rubric:** v6 (C-01--C-19; adds C-18: quality dimensions enumerated in protocol; C-19: explicit anti-overlap constraints for aspirational tier)
**Target criteria:** C-18, C-19 (two new aspirational criteria added in v6)

**Round 8 design note:** Rounds 4--7 produced mechanisms for C-01 through C-17 across four rubric tracks (v1, v2, v3, v5). Against rubric v6 specifically, the two new aspirational criteria are: C-18 (the protocol must contain an explicit named enumeration of quality dimensions -- >= 2 -- that recommended pass conditions must instantiate: e.g., "degree, precision, specificity") and C-19 (the protocol must contain an explicit anti-overlap statement binding the aspirational tier: "aspirational criteria must go beyond what essential and recommended already require"). Both criteria target the protocol's vocabulary layer: "quality" and "go beyond" must be defined in the authoring instructions, not asserted. Prior rounds probed mechanisms for deriving tiers from failure modes (C-17, R5), grounding category diversity in tier design (C-13, R6/R7 v2/v3-tracks), and embedding causal arguments in criterion text (C-12, R6/R7 tracks). For C-18 and C-19, the challenge is different: the protocol must contain named definitions at two specific authoring moments -- before recommended criteria are written (C-18) and before aspirational criteria are written (C-19). This round probes five mechanisms for embedding those definitions structurally, using three single-axis variations and two combined variations.

---

## Round 8 Variation Map

| Variation | Axis | C-18 probe | C-19 probe | Notes |
|-----------|------|-----------|-----------|-------|
| V-01 | Inertia framing (Imprecise-Quality competitor) | Strong -- naming a competitor that passes C-08 but uses "quality" without enumerating dimensions in its authoring protocol forces the builder to produce specific dimension names to distinguish the protocol from the competitor | Moderate -- competitor framing does not address anti-overlap; aspirational section not the competitor's failure | Single-axis; tests whether competitor naming at the recommended-tier authoring step produces C-18 compliance analogously to how inertia framing produced C-11/C-17 compliance in prior rounds |
| V-02 | Phrasing register (quality dimensions as constitutive terms) | Very strong -- "degree," "precision," and "specificity" defined constitutively; a pass condition that invokes none by name is using "quality" as a class label; the definition cannot be satisfied syntactically without selecting a named dimension | Moderate -- aspirational tier scope stated as an authoring instruction but not made constitutive; C-19 addressed by rule rather than definition | Single-axis; highest single-axis C-18 probe; mirrors R5 V-04 (essential IS blocking) applied now to quality dimensions |
| V-03 | Lifecycle emphasis (coverage map before aspirational tier) | Moderate -- coverage map context may invite quality-dimension thinking but does not structurally require dimension enumeration in recommended-phase authoring | Very strong -- coverage map makes the anti-overlap constraint operational: aspirational criteria must cite a named gap from the map; overlap becomes a placement error, not a judgment call | Single-axis; highest single-axis C-19 probe; analogous to how the severity table (R5 V-02) made tier assignment a lookup rather than a judgment |
| V-04 | Role sequence + Lifecycle (Vocabulary Definer + Coverage Mapper) | Very strong -- Vocabulary Definer role enumerates >= 2 named quality dimensions with definitions and examples before recommended criteria are written; hard gate; Builder must cite a dimension per recommended criterion | Very strong -- Coverage Mapper role produces gap statement before aspirational criteria are written; hard gate; Builder must cite a gap per aspirational criterion | Combined; closes C-18 and C-19 simultaneously with dedicated pre-authoring roles and per-role hard gates; structurally parallel to Classifier+Builder (R5 V-01) applied to vocabulary and scope |
| V-05 | Phrasing register + Inertia framing (Two-Layer competitor) | Strong -- Imprecise-Quality competitor named before recommended-tier authoring; constitutive definition of quality dimensions accompanies the competitor description; builder must name dimensions to exceed the competitor | Strong -- Implicit-Scope competitor named before aspirational-tier authoring; constitutive definition of tier scope accompanies it; builder must state the anti-overlap rule to exceed the competitor | Combined; two competitors paired with two constitutive definitions, one per new criterion; risk: two competitor descriptions may crowd the authoring instructions; each competitor scoped to its phase |

---

## V-01 -- Inertia Framing (Imprecise-Quality Competitor)

**Axis:** Inertia framing
**Hypothesis:** Prior rounds named inertia competitors at the essential level (vague rubric, generic rubric), the aspirational level (good rubric passes C-01--C-08 but fails causal linkage), and the tier-assignment level (Correct-Tier Rubric passes everything but lacks derivable tier labels). For C-18, the competitor belongs at the recommended-tier authoring step: the Imprecise-Quality Protocol. It passes C-08 -- its recommended criteria test quality properties, not just presence. Its pass conditions are observable-anchored. But its authoring instruction says "test quality, not presence" without naming what counts as a quality property. Two builders following it produce rubrics that both satisfy C-08 while testing entirely different dimensions: one tests degree (how many criteria exceed a threshold), another tests precision (how narrow the pass band), a third tests specificity (how tightly bound to this skill's output). All three outputs satisfy the instruction's letter. None is reproducible from the protocol alone. Naming this competitor before the recommended tier is written forces the builder to enumerate the specific dimensions that distinguish a reproducible protocol from an underdefined one -- the same mechanism by which naming the Correct-Tier Rubric (R5 V-05) forced the builder to produce the enumeration record that distinguishes auditable tier assignments from correct-but-unauditable ones.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden.

Your recommended tier has a competitor: the **Imprecise-Quality Protocol** -- a rubric-generation protocol whose recommended criteria test quality properties, not just presence. Its pass conditions use observable anchors. It satisfies C-08. But its authoring instruction says only "test quality, not presence" without defining what counts as a quality property. Two builders following the Imprecise-Quality Protocol produce rubrics that both satisfy C-08 while testing different dimensions: one tests degree, another tests precision, a third tests specificity. All three satisfy the protocol's letter. None is reproducible from it alone.

Your protocol must go further.

**Read the skill spec.**

What does this skill produce? What lifecycle phases does it run through? What does a complete correct output contain?

**PHASE 1: FAILURE MODES**

Name at least 3 failure modes -- ways this skill's output can be non-functional or misleading. Assign severity:

```
FAIL-01: [failure mode] | severity: blocking
FAIL-02: [failure mode] | severity: blocking
FAIL-03: [failure mode] | severity: degrading
...
```

Minimum: 3 blocking failure modes. DO NOT proceed to Phase 2 until the list contains at least 3 blocking entries.

**PHASE 2: ESSENTIAL CRITERIA (3-5)**

Draft essential criteria from the blocking failure modes. Each criterion requires all five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence -- what must be true in a passing output. State the downstream consequence before naming the observable: "without [X], [failure] occurs."
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence using observable anchors: count thresholds, named fields, structural patterns, explicit enumerations. No "is clear", "adequately covers" as sole criterion.

**PHASE 3: RECOMMENDED CRITERIA (2-3)**

Before writing recommended criteria, go beyond the Imprecise-Quality Protocol. Name the gap:

```
Imprecise-Quality gap: The protocol says "test quality, not presence" but does not
  define what counts as a quality property. A builder following it could test any of:
  [name 2-3 candidate dimensions -- e.g., degree, precision, specificity -- that would
  each satisfy C-08 but produce incompatible pass conditions]. Without naming the
  expected dimensions, two builders produce incompatible recommended criteria that
  both satisfy C-08.

Quality dimensions for this rubric's recommended tier:
  [Dimension 1]: [one-line definition scoped to this skill's output]
  [Dimension 2]: [one-line definition scoped to this skill's output]
  [optional Dimension 3 if clearly distinct]
```

Then draft recommended criteria. Each pass condition must instantiate a named dimension -- not assert "quality" as the sole criterion. Annotate each recommended criterion: **Dimension:** [name].

A recommended criterion that tests only whether a field exists (not degree, precision, or specificity of that field's content) satisfies the Imprecise-Quality Protocol but not yours.

**PHASE 4: ASPIRATIONAL CRITERIA (1-2)**

Write aspirational criteria that go beyond what essential and recommended require. Aspirational criteria must not restate essential or recommended requirements -- they must operate in territory the lower tiers do not cover.

**PHASE 5: SCORING AND OUTPUT**

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

Body: purpose statement (2-3 sentences -- name the Imprecise-Quality competitor and state what the named quality dimensions in Phase 3 add: where the competitor's protocol says "quality," yours says which dimensions; the recommended tier is reproducible across builders because its vocabulary is defined), then criteria ordered essential -> recommended -> aspirational (Phase 3 quality dimension enumeration retained as a preamble to the recommended section; Imprecise-Quality gap description omitted from output), then scoring section.

---

## V-02 -- Phrasing Register (Quality Dimensions as Constitutive Terms)

**Axis:** Phrasing register
**Hypothesis:** Prior rounds applied definitional register at different levels: R4 V-03 defined what a pass condition IS (the observable whose absence is the failure); R6 V-02 defined what a criterion Text IS (the argument establishing why the observable matters downstream); R5 V-04 defined what "essential" IS (guards against a blocking failure mode, not a preference). V-02 applies definitional register to the recommended tier vocabulary. "Quality" is a class label, not a property name. A protocol that instructs authors to write recommended criteria that "test quality" without naming the class members is asserting rather than specifying -- two authors reading it may select different members and produce incompatible criteria that both satisfy the instruction's letter. Three quality dimensions are defined constitutively: degree, precision, and specificity. A recommended pass condition must invoke at least one by name; a pass condition that uses "quality" as the sole criterion has not instantiated a named dimension. The constitutive definition forces the builder to select a named dimension before writing the pass condition -- dimension selection is the authoring act, not an option. The variation also addresses C-19 via a stated rule (not a constitutive definition), probing whether a single constitutive definition (C-18) combined with an explicit rule (C-19) produces adequate simultaneous compliance.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden.

A **quality property** is a named dimension with a direction and a measurable pass band -- not a general class. In this rubric system, quality properties for recommended criteria are defined as follows:

**Degree** -- the quantity of a property present. A pass condition tests degree when it asks: how much, how many, how often. Degree pass conditions use count thresholds or proportion ratios. A pass condition that only confirms the property exists is not testing degree -- it is testing presence.

**Precision** -- the width of the pass band. A pass condition tests precision when it specifies the boundary between barely-passing and clearly-passing such that two independent evaluators applying it to the same output reach the same verdict. A pass condition that uses characterizations like "adequately" or "reasonably" without a boundary specification is not testing precision.

**Specificity** -- how tightly the criterion is bound to this skill's artifact vs any artifact. A pass condition tests specificity when its observable would change if applied to a different skill's output. A pass condition that would yield the same observable for any skill's rubric is not testing specificity.

These definitions are constitutive. A recommended pass condition that invokes none of these dimensions by name is using "quality" as a class label -- it has labeled a requirement without specifying which requirement. Two builders reading the same instruction that says "test quality, not presence" may select different dimensions and produce incompatible recommended criteria that both satisfy the instruction.

---

**Read the skill spec.**

Name the failure modes. For each, classify severity: blocking, degrading, cosmetic.

**Build the rubric.**

Each criterion requires all five fields -- no blanks, no "TBD":

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence -- what must be true in a passing output
- **Weight**: essential | recommended | aspirational
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence with an observable anchor

Tier targets: 3-5 essential (blocking failure modes), 2-3 recommended (degrading failure modes), 1-2 aspirational. All three tiers required.

Before writing each **recommended** criterion: select the quality dimension it will test -- degree, precision, or specificity -- and verify the pass condition names that dimension. If the pass condition uses "quality" as the sole criterion, it has not instantiated a named dimension; rewrite before proceeding to the next criterion. Annotate: **Dimension tested:** [degree | precision | specificity].

Before writing **aspirational** criteria, state the scope constraint:

```
Aspirational tier scope: aspirational criteria must not cover failure modes or
  quality dimensions already covered by the essential or recommended tiers. A
  criterion that tests a property already guarded by a lower tier -- even at a
  higher threshold or a narrower pass band -- is not aspirational. It is a tighter
  version of an existing lower-tier criterion and belongs in that tier. Write
  aspirational criteria only for properties the lower tiers leave uncovered.
```

---

**Write the composite formula:**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- invoke the constitutive definitions: quality properties are named dimensions -- degree, precision, specificity -- not a general class; a recommended pass condition that invokes none of them by name is asserting "quality," not specifying it; aspirational criteria must occupy uncovered territory, not restate lower-tier requirements at higher precision), then criteria ordered essential -> recommended -> aspirational (Dimension tested annotation retained for recommended criteria; tier scope constraint statement retained as preamble to aspirational section), then scoring section.

---

## V-03 -- Lifecycle Emphasis (Coverage Map Before Aspirational Tier)

**Axis:** Lifecycle emphasis
**Hypothesis:** C-19 requires the protocol to state tier scope as an explicit anti-overlap constraint. The standard instruction "aspirational criteria must go beyond essential and recommended" is semantic -- it relies on the author to judge what "beyond" means in each case. Two authors reading the instruction may disagree: one concludes that a criterion testing the same failure mode as an essential at a higher count threshold is "beyond" the essential; another concludes it is a tightening, not an extension. The coverage map makes the constraint operational: before writing aspirational criteria, the builder maps what the essential and recommended tiers already cover -- which failure modes, output properties, and behavioral checks are guarded -- and explicitly names what they leave uncovered. Aspirational criteria must then fall in the uncovered zone. An aspirational criterion that falls in the "essential covers" or "recommended covers" zone is a placement error, not a judgment call. This is the same principle that made tier assignment mechanical in R5 (C-17: severity enumeration + lookup replaces judgment) applied now to tier scope: the coverage map replaces "does this go beyond?" with "where does this fall in the map?" -- a query with a structural answer.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden. Build it in three stages: failure mode analysis, essential and recommended criteria, coverage map and aspirational criteria.

**Read the skill spec.**

What does the skill produce? What lifecycle phases does it have? What does a complete correct output contain?

**PHASE 1: FAILURE MODE ANALYSIS**

Name every failure mode -- every way an output of this skill can be non-functional, degraded, or cosmetically flawed. Assign severity:

```
F-01: [failure mode] | blocking
F-02: [failure mode] | degrading
F-03: [failure mode] | cosmetic
...
```

Minimum: 3 blocking, 2 degrading, 1 cosmetic.

DO NOT proceed to Phase 2 until the failure mode list is complete.

**PHASE 2: ESSENTIAL AND RECOMMENDED CRITERIA**

Draft essential criteria (3-5) from blocking failure modes and recommended criteria (2-3) from degrading failure modes. Continue C-NN numbering across both tiers.

Each criterion requires all five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence -- what must be true in a passing output
- **Weight**: essential | recommended
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence with observable anchors. No "is clear", "adequately covers" as sole criterion.

Recommended criteria: each pass condition tests a quality property -- the degree, precision, or specificity of the output -- not just whether a field exists.

**PHASE 3: COVERAGE MAP**

Before writing aspirational criteria, produce the coverage map:

```
Coverage map (what essential and recommended tiers cover):

Essential tier covers:
  [List 3-5 specific output properties or failure modes guarded by essential criteria.
   Name them precisely: not "structural completeness" but the specific fields and
   their minimum counts that an evaluator can check without judgment.]

Recommended tier covers:
  [List 2-3 specific quality properties guarded by recommended criteria.
   Name them precisely: not "quality" but the specific degree, precision, or
   specificity dimension each criterion targets.]

What the essential and recommended tiers do NOT cover:
  [Name at least 1 property that a passing-but-not-excellent output would lack.
   An output scoring only on essential and recommended could miss this. This is the
   aspirational gap. Be specific: not "could be better" but the property whose
   absence makes a passing rubric good but not excellent for this specific skill's
   objective function role.]
```

DO NOT write aspirational criteria until the coverage map is complete and at least 1 aspirational gap is named.

Tier scope constraint: aspirational criteria must fall in the "What the essential and recommended tiers do NOT cover" zone of the coverage map. An aspirational criterion that falls in "Essential tier covers" or "Recommended tier covers" is a placement error -- revise or reclassify before proceeding.

**PHASE 4: ASPIRATIONAL CRITERIA (1-2)**

Write aspirational criteria from the coverage map's gap zone. Each criterion requires all five fields plus one additional field:

- **ID**: C-NN (continuing)
- **Text**: one sentence
- **Weight**: aspirational
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence with observable anchors
- **Fills gap**: [quote or paraphrase the gap from Phase 3 that this criterion addresses]

The Fills gap field must be non-blank. A blank Fills gap field means the aspirational criterion cannot be verified against the anti-overlap constraint.

**PHASE 5: SCORING AND OUTPUT**

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

Body: purpose statement (2-3 sentences -- state the coverage-map principle: aspirational criteria are not stretch goals but gap-fillers; the coverage map makes "goes beyond essential and recommended" a placement operation rather than a judgment call; an aspirational criterion that falls in the map's covered zone is a placement error), then the coverage map (retained in output as the tier scope record), then criteria ordered essential -> recommended -> aspirational (Fills gap field retained for aspirational criteria; Phase 1 failure mode list omitted), then scoring section.

---

## V-04 -- Role Sequence + Lifecycle (Vocabulary Definer + Coverage Mapper)

**Axis:** Role sequence (two pre-authoring roles) + lifecycle emphasis (phase-gated pre-authoring steps)
**Hypothesis:** C-18 and C-19 both require the protocol to define something before certain criteria are written: C-18 requires quality dimension enumeration before recommended criteria; C-19 requires the coverage map before aspirational criteria. These are parallel pre-authoring requirements at different phases. V-04 separates them as dedicated roles with hard gates between each role and its downstream phase: the Vocabulary Definer runs before recommended-tier authoring and must produce >= 2 named quality dimensions with definitions, questions, and examples scoped to this skill; the Coverage Mapper runs after recommended-tier authoring and must produce a named gap zone before aspirational-tier authoring begins. Neither role is an optional analysis step embedded in a broader phase -- each has a single exit condition and blocks progression until that condition is met. The combined architecture closes C-18 and C-19 simultaneously, structurally parallel to how the Classifier + Builder (R5 V-01) closed C-17 by making tier assignment a lookup operation: the Vocabulary Definer makes recommended-tier authoring a dimension-instantiation operation, and the Coverage Mapper makes aspirational-tier authoring a gap-filling operation.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden. Three roles operate in sequence: Analyst, Vocabulary Definer, and Coverage Mapper. Each role's output is a required input to the next phase. No phase begins without its required input.

---

**ANALYST ROLE**

Read the skill spec. Enumerate failure modes:

```
F-01: [failure mode] | blocking
F-02: [failure mode] | degrading
F-03: [failure mode] | cosmetic
...
```

Minimum: 3 blocking, 2 degrading, 1 cosmetic.

Draft essential criteria (3-5) from blocking failure modes. Each criterion requires all five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence -- what must be true in a passing output. State the downstream consequence: "without [X], [failure] occurs."
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence with observable anchors. No "is clear", "adequately covers" as sole criterion.

DO NOT write recommended criteria until the Vocabulary Definer role is complete.

---

**VOCABULARY DEFINER ROLE**

Before writing recommended criteria, enumerate the quality dimensions that recommended pass conditions in this rubric must instantiate.

```
Quality vocabulary for the recommended tier of {skill_target} rubrics:

Dimension 1: [Name]
  Definition: [one sentence -- what this dimension measures, scoped to this skill's output]
  A pass condition tests this when it asks: [the question a pass condition testing
    this dimension answers -- specific to this skill]
  Example: [a concrete example pass condition for this skill that instantiates
    this dimension -- must name an observable specific to {skill_target} outputs]

Dimension 2: [Name]
  Definition: [one sentence]
  A pass condition tests this when it asks: [the question]
  Example: [example pass condition]

[Add Dimension 3 if clearly distinct from 1 and 2 and relevant to this skill's
  recommended criteria.]
```

Minimum: 2 named dimensions with definitions, questions, and examples scoped to this skill. The dimensions must be distinct -- testing one does not test the other.

DO NOT write recommended criteria until the Vocabulary Definer output contains at least 2 named dimensions satisfying all three subfields.

---

**RECOMMENDED CRITERIA (Analyst, consuming Vocabulary Definer output)**

Draft recommended criteria (2-3) from degrading failure modes. Each criterion's pass condition must instantiate a named dimension from the Vocabulary Definer output. Required fields:

- **ID**: C-NN (continuing from essential criteria)
- **Text**: one sentence
- **Weight**: recommended
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence instantiating a named quality dimension
- **Dimension tested**: [name the Vocabulary Definer dimension this pass condition instantiates]

A recommended criterion whose Dimension tested field is blank or cites an unlisted dimension is using undefined vocabulary. Revise before proceeding.

DO NOT write aspirational criteria until the Coverage Mapper role is complete.

---

**COVERAGE MAPPER ROLE**

Before writing aspirational criteria, produce the coverage map:

```
Coverage map:

Essential tier guards against:
  [List each blocking failure mode covered by essential criteria -- one line per
   essential criterion: "C-NN guards against [F-NN: failure mode]."]

Recommended tier guards against:
  [List each quality dimension covered by recommended criteria -- one line per
   recommended criterion: "C-NN guards against [dimension: specific property]."]

Gap zone -- not yet covered by essential or recommended:
  [Name at least 1 specific property that an output passing essential + recommended
   could still lack. This property must not be reachable by tightening or combining
   existing criteria -- it must require a genuinely new observation. Be specific:
   name what a passing-but-not-excellent output would lack that the gap-zone
   criterion will catch.]
```

The gap zone is the anti-overlap constraint: aspirational criteria must fall in the gap zone. A criterion that falls in "Essential tier guards against" or "Recommended tier guards against" -- even at a higher threshold -- is not aspirational. Reclassify or revise before writing aspirational criteria.

DO NOT write aspirational criteria until the Coverage Mapper output contains at least 1 named gap.

---

**ASPIRATIONAL CRITERIA (Analyst, consuming Coverage Mapper output)**

Draft aspirational criteria (1-2) from the Coverage Mapper's gap zone. Each criterion:

- Must cite the gap it fills (from the Coverage Mapper output)
- Must not restate what essential or recommended already require

Required fields:

- **ID**: C-NN (continuing from recommended criteria)
- **Text**: one sentence
- **Weight**: aspirational
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence with observable anchors
- **Fills gap**: [quote the gap from the Coverage Mapper output]

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

Body: purpose statement (2-3 sentences -- state the Vocabulary Definer + Coverage Mapper sequence: the Vocabulary Definer names quality dimensions before recommended criteria are written, making recommended authoring a dimension-instantiation operation; the Coverage Mapper names the gap zone before aspirational criteria are written, making aspirational authoring a gap-filling operation; both make the protocol's vocabulary defined before authoring rather than asserted during it), then Vocabulary Definer output (retained as the recommended-tier vocabulary record), then Coverage Mapper output (retained as the aspirational-tier scope record), then criteria ordered essential -> recommended -> aspirational (Dimension tested and Fills gap fields retained; Analyst failure mode list omitted), then scoring section.

---

## V-05 -- Phrasing Register + Inertia Framing (Two-Layer Competitor)

**Axis:** Phrasing register (constitutive definitions) + inertia framing (two competitors, one per new criterion)
**Hypothesis:** Prior rounds established that naming a near-excellent competitor creates structural pressure toward the property the competitor lacks: the builder must produce the distinguishing property, not just satisfy criteria by the letter. V-05 extends the two-competitor architecture from R6 (which named competitors at the essential and aspirational tiers for C-11/C-17) to the recommended and aspirational tiers for C-18 and C-19 respectively. Two competitors are named, each failing exactly one of the target criteria: (1) the Imprecise-Quality Protocol fails C-18 -- its authoring instruction says "test quality" without naming the dimensions; (2) the Implicit-Scope Protocol fails C-19 -- its authoring instruction says "go beyond essential and recommended" without stating the anti-overlap rule, relying on tier ordering to imply it. Each competitor description is accompanied by a constitutive definition: a quality property IS a named dimension (not a class label); tier scope IS a stated constraint (not an inferred boundary). The two definitions create phase-specific targets: at the recommended-tier authoring step, beat the Imprecise-Quality Protocol by enumerating dimensions; at the aspirational-tier authoring step, beat the Implicit-Scope Protocol by stating the anti-overlap rule. The hypothesis is that two competitors each paired with a constitutive definition produce higher simultaneous C-18 and C-19 compliance than either mechanism alone, because each competitor's failure makes the corresponding definition's necessity concrete.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden. Your protocol has two competitors. Each passes C-01 through C-17. Each fails exactly one of the new target criteria.

**Competitor 1: The Imprecise-Quality Protocol**

Recommended criteria pass C-08: they test quality properties, not just presence. Pass conditions are observable-anchored. Criteria are skill-specific. But the authoring instruction says: "recommended criteria should test quality, not just presence." The word "quality" is undefined. A builder following this protocol might test degree, another might test precision, a third might test specificity. All three satisfy the instruction. None is reproducible from the protocol alone -- the instruction admits any quality dimension, including ones that produce incompatible pass conditions.

**A quality property is constitutively a named dimension.** "Quality" as a class label is not a quality property -- it is a container for unnamed members. Three named dimensions: **degree** (how much of a property is present -- pass conditions use count thresholds or proportions), **precision** (how narrow the pass band is -- pass conditions specify the boundary that separates borderline from clear pass, such that two evaluators reach the same verdict), **specificity** (how tightly bound to this skill's artifact -- the observable changes if applied to a different skill's output). A recommended pass condition that invokes none of these by name is using the container label. The Imprecise-Quality Protocol does this. Your protocol must enumerate at least 2 named dimensions before recommended criteria are written.

**Competitor 2: The Implicit-Scope Protocol**

Aspirational criteria pass C-09: they distinguish excellent from merely passing. They are not verbatim restatements of essential criteria. Tier distribution is correct. But the authoring instruction says: "aspirational criteria should go beyond essential and recommended." The phrase "go beyond" is undefined. An author following this protocol might write an aspirational criterion that tests the same failure mode as an essential at a count one higher -- technically distinct, occupying the same failure-dimension territory. Another might write a criterion that belongs in the recommended tier but is labeled aspirational because the author judged it non-blocking. The Implicit-Scope Protocol's anti-overlap constraint is implied by tier ordering; it is not stated as a rule in the authoring instructions.

**Tier scope is constitutively a stated constraint, not an inferred boundary.** "Go beyond" means: aspirational criteria must not cover failure modes or quality dimensions already covered by essential or recommended criteria. This is an anti-overlap rule -- it must appear as an explicit statement in the protocol's authoring instructions for the aspirational tier. A protocol that defines tiers by severity (blocking -> essential, degrading -> recommended) but does not state the anti-overlap rule for the aspirational tier relies on the author to infer that the cosmetic/excellence zone is distinct from the failure-mode zones below -- an inference that is correct by design but invisible in the instruction. The Implicit-Scope Protocol does this. Your protocol must state the constraint.

---

**Read the skill spec.**

Name the failure modes. Assign severity: blocking, degrading, cosmetic.

**Build the rubric.**

**Before writing essential criteria:** confirm at least 3 blocking failure modes.

Draft essential criteria (3-5). Each requires all five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence -- state the downstream consequence before naming the observable: "without [X], [failure] occurs because [Z]"
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence with observable anchors

**Before writing recommended criteria:** go beyond the Imprecise-Quality Protocol.

Name the quality dimensions your recommended criteria will test:

```
Quality dimensions for recommended criteria in this rubric:
  [Dimension 1]: [one-line definition scoped to this skill's output]
  [Dimension 2]: [one-line definition scoped to this skill's output]
```

At least 2 dimensions. Definitions must be scoped to this skill -- name the observable this dimension targets in this skill's output specifically.

Draft recommended criteria (2-3). Each pass condition must instantiate a named dimension -- not assert "quality." Annotate: **Dimension:** [name].

**Before writing aspirational criteria:** go beyond the Implicit-Scope Protocol.

State the anti-overlap constraint:

```
Tier scope constraint: aspirational criteria must not cover failure modes or
  quality dimensions already covered by the essential or recommended tiers. A
  criterion that tests a property already guarded by a lower tier -- even at a
  higher threshold, a narrower pass band, or a more precise formulation -- is not
  aspirational. It is a tighter version of an existing lower-tier criterion.
  Write aspirational criteria only for properties the lower tiers genuinely leave
  uncovered.
```

Draft aspirational criteria (1-2). After writing each, apply the check: "Is there an essential or recommended criterion that guards against the same failure mode or quality dimension as this criterion?" If yes: reclassify.

---

**Write the composite formula:**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- name the two competitors and state what each constitutive definition adds: where the Imprecise-Quality Protocol says "quality," yours names the dimensions; where the Implicit-Scope Protocol says "go beyond," yours states the anti-overlap rule; both definitions appear at their respective authoring moments, not as retrospective documentation), then criteria ordered essential -> recommended -> aspirational (quality dimension annotations and tier scope constraint statement retained; competitor descriptions and failure mode list omitted from output), then scoring section.
