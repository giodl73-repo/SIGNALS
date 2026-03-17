# quest-rubric Variate — Round 2 against rubric v2

**Date:** 2026-03-15
**Skill:** quest-rubric
**Rubric:** v2 (C-01 through C-13; essential C-01–C-05)
**Round:** R2 — 3 single-axis passes + 2 combination passes

**Round 2 design note:** Round 1 (against rubric v1) established the essential and recommended
baseline (C-01–C-10). Three R1 excellence signals were absorbed into v2 as aspirational criteria:
C-11 (discriminating pass conditions via inertia test, from V-05), C-12 (calibration example,
from V-04), C-13 (phase-gate enforcement, from V-01). Round 2 probes whether skill body variations
can reliably produce rubrics that reach all three new criteria. Each single-axis variation isolates
one mechanism. The two combinations test whether mechanism pairs interact to address criteria that
resist single-axis treatment.

---

## Round 2 Variation Map

| Variation | Axis | Pass Type | What Changes | Criteria Targeted |
|-----------|------|-----------|--------------|-------------------|
| V-01 | inertia-framing | single-axis | Named competitor ("The Status-Quo Rubric") invoked per-criterion at pass condition authoring time; inertia test result documented inline | C-11 |
| V-02 | output-format | single-axis | Essential criteria table gains required `Calibration Example` column with mandatory GENERIC/GROUNDED pair per row | C-12 |
| V-03 | lifecycle-emphasis | single-axis | Phase 2 expands into four numbered sub-steps per criterion; hard gate blocks advancement until sub-steps 2b and 2c are complete | C-11, C-12, C-13 |
| V-04 | phrasing-register | single-axis | All definitional instructions structured as IS:/IS NOT: constitutive pairs; the contrast structure IS the instruction | C-11 |
| V-05 | role-sequence × inertia-framing | combination (R2 Priority 1) | Challenger role applies inertia test to every Author-drafted pass condition; named competitor motivates why; Challenger blocks finalization until all essential pass conditions survive | C-11, C-12 |

**Anchor designation (C-12 of the quest-variate rubric):** V-03. See anchor section at end.

---

## V-01 — Inertia Framing: The Status-Quo Rubric Competitor

**axis:** inertia-framing
**hypothesis:** Naming a single concrete competitor ("The Status-Quo Rubric") at the start and
invoking it by name at each pass condition authoring moment increases C-11 pass rates because
the inertia test is applied at the precise moment the builder is most likely to write a generic
condition — not as a post-hoc audit. The competitor's name gives the builder a self-test that
does not require re-reading the rubric definition of C-11. Failure condition: if C-11 pass rate
does not improve relative to variations with no competitor framing, the named-competitor approach
adds no targeting benefit over a generic "be specific" instruction and should not be carried into
combination runs.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden: it must enable two independent evaluators to reach the same pass/fail verdict for
any skill output, without discussion.

**Your primary competitor: The Status-Quo Rubric**

Before you write a single criterion, name your competitor:

> **The Status-Quo Rubric**: "Output quality — the output is clear, comprehensive, and
> well-formatted." One criterion. No counts. No named fields. Applies to any skill.
> Can never be wrong and can never distinguish.

Every pass condition you write will be held against the Status-Quo Rubric with one question:

> **Inertia test**: Could a rubric containing only "the output is clear and comprehensive"
> pass this condition? If YES, your condition is not yet skill-specific. Revise until NO.

A pass condition survives the inertia test only when it names at least one of: a count, a named
field, a structural pattern, or an enumeration that only this specific skill's output contract
can supply — not a shared structural minimum that any artifact has.

---

Read the skill spec. Answer:

1. What does this skill produce? Name the artifact type and its key fields.
2. What lifecycle phases does it have? Name them in order.
3. What would a completely non-functional output look like? Name the failure, not the
   absence of quality.

**PHASE 1: FAILURE MODES**

List failure modes. Each mode is a specific, detectable way the output can fail to function
as intended. Assign severity.

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
[F-06+: additional if present]
```

Minimum: 3 blocking, 2 degrading.

DO NOT proceed to Phase 2 until you have at least 3 blocking failure modes listed.

**PHASE 2: ESSENTIAL CRITERIA (3-5)**

Each criterion requires five fields: ID (C-NN), criterion text with a bold label, category
(correctness/depth/format/coverage/behavior), weight (essential), and pass condition.

For each pass condition, apply the inertia test before finalizing:

> Inertia test check: Could "the output is clear and comprehensive" pass this condition?
> — If YES: the condition is generic. Find the count, named field, or enumeration from
>   this skill's contract and add it. Re-run the test.
> — If NO: the condition is skill-specific. Proceed.

Document the inertia test result inline for each essential criterion:

`[Inertia test: NO — condition requires {specific element from this skill's contract}]`

**PHASE 3: RECOMMENDED CRITERIA (2-3)**

Write 2-3 recommended criteria. Apply the inertia test to each pass condition before
finalizing. Documentation inline is not required but the test must be applied.

**PHASE 4: ASPIRATIONAL CRITERIA (1-2)**

Write 1-2 aspirational criteria covering excellence patterns beyond minimum viability.

**PHASE 5: SCORING FORMULA AND GOLDEN THRESHOLD**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

Scoring band table:

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**PHASE 6: QUICK CHECKLIST**

One checkbox per criterion: `- [ ] C-NN: [one-line assertion]`

---

## V-02 — Output Format: Required Calibration-Example Column

**axis:** output-format
**hypothesis:** Adding a required `Calibration Example` column to the essential criteria table
forces a concrete GENERIC/GROUNDED pair at authoring time for every essential criterion, because
an empty column is a visible structural failure rather than an omission-by-neglect. When the
table schema itself demands the pair, the author cannot finish the table row without writing it.
This increases C-12 pass rates by converting an aspirational behavior into a format requirement.
Failure condition: if C-12 pass rate does not improve relative to variations using standard
five-column tables, the schema-embedded column adds no compliance benefit over a prose
instruction to "include a calibration example."

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden: it must enable systematic scoring across all variations.

Read the skill spec. Answer:

1. What does this skill produce? Name the artifact and its key fields.
2. What lifecycle phases does it have?
3. What failure would make the output completely non-functional?

**PHASE 1: FAILURE MODES**

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Minimum: 3 blocking, 2 degrading.

DO NOT proceed to Phase 2 until you have at least 3 blocking failure modes.

**PHASE 2: ESSENTIAL CRITERIA (3-5)**

Use the extended table format for essential criteria. The `Calibration Example` column is
required — an empty cell is a criterion completion failure.

| ID | Criterion | Category | Weight | Pass Condition | Calibration Example |
|----|-----------|----------|--------|----------------|---------------------|

The `Calibration Example` column must contain a **GENERIC/GROUNDED pair** for each row:

```
GENERIC: [a pass condition formulation that would apply to any artifact regardless of
          which skill produced it]
GROUNDED: [a pass condition formulation naming this skill's specific output contract —
           a count, field name, structural element, or enumeration that only this skill
           supplies]
```

Both entries must reference the target skill by name or by a term from its output contract.
The GROUNDED entry must differ from the GENERIC entry in that it names something skill-specific —
not a property that any well-formed output has.

**PHASE 3: RECOMMENDED CRITERIA (2-3)**

Standard five-column table (no calibration example required):

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**PHASE 4: ASPIRATIONAL CRITERIA (1-2)**

Standard five-column table.

**PHASE 5: SCORING FORMULA AND GOLDEN THRESHOLD**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**PHASE 6: QUICK CHECKLIST**

One checkbox per criterion: `- [ ] C-NN: [one-line assertion]`

---

## V-03 — Lifecycle Emphasis: Per-Criterion Sub-Steps with Hard Gates

**axis:** lifecycle-emphasis
**hypothesis:** Expanding Phase 2 into four numbered sub-steps — (2a) draft pass condition,
(2b) apply inertia test, (2c) write calibration pair, (2d) gate check — with an explicit hard
gate blocking advancement before both 2b and 2c are complete addresses all three new v2 criteria
simultaneously: C-11 because the inertia test is a required sub-step not a post-hoc audit;
C-12 because the calibration pair is a required sub-step not an aspirational annotation; C-13
because the gate language is explicit, blocking, and references a checkable structural condition
(not a quality judgment). Failure condition: if the three-criteria improvement does not
materialize — if C-11, C-12, and C-13 pass rates are not higher than V-01 or V-02 individually —
the sequential sub-step protocol adds no benefit over independent per-criterion instructions and
the overhead cost (longer prompts, more structure) is not justified.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden.

Read the skill spec. Answer:

1. What does this skill produce? Name the artifact and its key fields.
2. What lifecycle phases does it have?
3. What failure would make the output completely non-functional?

**PHASE 1: FAILURE MODES**

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Minimum: 3 blocking, 2 degrading.

**DO NOT proceed to Phase 2 until the failure mode list contains at least 3 blocking entries.**

**PHASE 2: ESSENTIAL CRITERIA (3-5)**

For each essential criterion, complete all four sub-steps before starting the next criterion.

**Sub-step 2a — Draft the pass condition.**

Write the pass condition text: a specific, observable outcome. State what an evaluator would
look for and what would constitute a pass.

**Sub-step 2b — Apply the inertia test.**

Ask: Could a rubric containing only "the output is clear and comprehensive" pass this condition?

- If YES: the condition is generic. Revise to name a count, field name, structural element,
  or enumeration from this skill's output contract. Re-run the test until NO.
- If NO: the condition is skill-specific. Record result.

Record inline: `Inertia test: PASS [NO]` or `Inertia test: FAIL [YES — revised to add {element}]`

**Sub-step 2c — Write the calibration pair.**

Write a GENERIC/GROUNDED pair for this criterion:

```
GENERIC: [pass condition text that could belong to the Status-Quo Rubric — applies to
          any artifact, names no skill-specific element]
GROUNDED: [pass condition text naming this skill's specific output contract — the element
           you identified in sub-step 2b that makes this condition discriminating]
```

Both entries must reference the target skill by name or by a term from its output contract.

**Sub-step 2d — Gate check.**

**DO NOT finalize this criterion and advance to the next until:**

- [ ] Sub-step 2b result is `PASS [NO]` — inertia test survived (original or revised)
- [ ] Sub-step 2c calibration pair is written with both GENERIC and GROUNDED entries present

After completing all four sub-steps, record the criterion in the standard table:

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**PHASE 3: RECOMMENDED CRITERIA (2-3)**

Write 2-3 recommended criteria. Four-sub-step protocol is not required; standard five-field
table format only.

**PHASE 4: ASPIRATIONAL CRITERIA (1-2)**

Write 1-2 aspirational criteria. Standard five-field table format.

**PHASE 5: SCORING FORMULA AND GOLDEN THRESHOLD**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**PHASE 6: QUICK CHECKLIST**

One checkbox per criterion: `- [ ] C-NN: [one-line assertion]`

---

## V-04 — Phrasing Register: IS:/IS NOT: Constitutive Pairs

**axis:** phrasing-register
**hypothesis:** Structuring all definitional instructions as IS:/IS NOT: constitutive pairs —
where the contrast structure IS the instruction, not prose augmented with an example — causes
the author to internalize the discriminating test as a definition rather than a post-hoc check.
The form "A DISCRIMINATING PASS CONDITION IS: [biconditional] / IS NOT: [generic alternative]"
means the author applies the definition at authoring time because the definition block is read
before writing. Failure condition: if C-11 pass rates do not improve relative to V-01 (which
uses a named competitor with imperative instructions), the constitutive-pair register adds no
benefit over competitor framing and should not be carried into combination runs.

---

You are building a scoring rubric for a Signal skill.

**A DISCRIMINATING PASS CONDITION IS:**
A condition naming at least one count, named field, structural pattern, or enumeration from
this specific skill's output contract — an element that only this skill can supply. Two
independent evaluators can reach the same pass/fail verdict without discussion.

**A DISCRIMINATING PASS CONDITION IS NOT:**
A condition that could apply to any artifact regardless of which skill produced it ("the output
is clear", "the output is comprehensive", "output quality is high"). Such conditions cannot
distinguish a skill-specific failure from general mediocrity. They belong to the Status-Quo
Rubric, not a skill rubric.

**A CALIBRATION PAIR IS:**
A concrete GENERIC/GROUNDED pair where the GENERIC example shows what not to write and the
GROUNDED example shows what to write instead. Both examples must reference the target skill
by name or by a term from its output contract. The GROUNDED example must contain a term that
only this skill's contract supplies.

**A CALIBRATION PAIR IS NOT:**
A pair where the grounded example could be used in a rubric for a different skill without
modification. "The output contains a summary" is not grounded in any specific skill; "the
output contains a criteria table with all five fields (ID, text, weight, category, pass
condition)" is grounded in quest-rubric's output contract.

**A PHASE GATE IS:**
An explicit blocking statement using "DO NOT proceed until..." that names a checkable
condition — a count, a field's presence, or a structural property — whose satisfaction an
evaluator could verify from the output alone.

**A PHASE GATE IS NOT:**
A quality suggestion, an aspiration, or a condition requiring subjective judgment ("until the
output is good enough", "until criteria are sufficiently specific"). Gates that cannot be
verified without discussion are not gates.

---

Read the skill spec. Answer:

1. What does this skill produce? Name the artifact and its key fields.
2. What lifecycle phases does it have?
3. What failure would make the output non-functional?

**PHASE 1: FAILURE MODES**

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Minimum: 3 blocking, 2 degrading.

DO NOT proceed to Phase 2 until this minimum is met.

**PHASE 2: ESSENTIAL CRITERIA (3-5)**

Each criterion requires five fields: ID (C-NN), criterion text with bold label, category
(correctness/depth/format/coverage/behavior), weight (essential), pass condition.

Apply the IS:/IS NOT: definitions above when writing each pass condition. A pass condition
satisfies its definition when the IS: form applies and the IS NOT: form does not. If the IS NOT:
form applies to your draft, revise the condition before finalizing.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**PHASE 3: RECOMMENDED CRITERIA (2-3)**

Write 2-3 recommended criteria. Five-field format. IS:/IS NOT: self-check applies.

**PHASE 4: ASPIRATIONAL CRITERIA (1-2)**

Write 1-2 aspirational criteria. Five-field format.

**PHASE 5: SCORING FORMULA AND GOLDEN THRESHOLD**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**PHASE 6: QUICK CHECKLIST**

One checkbox per criterion: `- [ ] C-NN: [one-line assertion]`

---

## V-05 — Role Sequence × Inertia Framing (Combination)

**axis:** role-sequence × inertia-framing
**hypothesis:** A Challenger role that applies the inertia test to every Author-drafted pass
condition, combined with named competitor framing that motivates why the test matters, addresses
C-11 and C-12 together: the competitor framing establishes the stakes at setup time (WHY the
inertia test exists), the Challenger role enforces the test structurally after drafting (THAT
it fires for every essential criterion), and the Challenger's calibration pair requirement
satisfies C-12 without adding sub-step overhead to the Author's drafting phase. Failure
condition: if C-11 and C-12 pass rates are not both higher than V-01 (inertia-framing alone)
and V-02 (output-format alone), the role-split mechanism adds no benefit over single-axis
treatments and the combination should not be pursued further.

---

You are building a scoring rubric for a Signal skill. Two roles operate in sequence:
Author drafts criteria; Challenger verifies pass conditions and enforces skill-specificity.

**Your competitor: The Status-Quo Rubric**

The Status-Quo Rubric wins by default unless every essential pass condition is skill-specific.
It contains one criterion: "Output quality — the output is clear, comprehensive, and
well-formatted." It passes every rubric that lacks skill-specific counts, fields, or enumerations.
If your essential pass conditions could belong to it, your rubric adds no signal over doing nothing.

---

--- ROLE: AUTHOR ---

Read the skill spec. Answer:

1. What does this skill produce? Name the artifact and its key fields.
2. What lifecycle phases does it have?
3. What failure would make the output non-functional?

**PHASE 1: FAILURE MODES**

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Minimum: 3 blocking, 2 degrading.

**DO NOT hand off to the Challenger until Phase 1 is complete with at least 3 blocking entries.**

**PHASE 2: ESSENTIAL CRITERIA (3-5)**

Write essential criteria. Five fields each: ID (C-NN), criterion text with bold label, category,
weight (essential), pass condition. Draft pass conditions without self-reviewing for
skill-specificity — the Challenger handles this. Focus on coverage: each criterion should
target a distinct failure mode from Phase 1.

**PHASE 3: RECOMMENDED AND ASPIRATIONAL CRITERIA**

Write 2-3 recommended and 1-2 aspirational criteria. Five fields each.

--- END AUTHOR ---

--- ROLE: CHALLENGER ---

Read all Author-drafted essential criteria. For each essential pass condition, apply the inertia
test:

> Inertia test: Could a rubric containing only "the output is clear and comprehensive" pass
> this condition?
> — YES: the condition is generic. The Author must revise before the rubric is final.
> — NO: condition survives. Note the skill-specific element that makes it discriminating.

Produce the Challenger Review table:

| Criterion | Pass Condition (quoted) | Inertia Test | Revision Required? | Skill-Specific Element |
|-----------|------------------------|--------------|-------------------|------------------------|

For each condition flagged YES: write one revised pass condition that survives the inertia test.
Name the specific count, field, or enumeration you added.

For the single most critical essential criterion, write a calibration pair:

```
GENERIC: [the condition as it appeared in the YES-flagged form, or the weakest surviving
          form — what belongs to the Status-Quo Rubric]
GROUNDED: [the revised condition naming the skill-specific element — what makes it
           discriminating for this skill only]
```

**DO NOT finalize the rubric until every essential pass condition has a Challenger result
of NO (original or Challenger-revised).**

--- END CHALLENGER ---

**PHASE 4: SCORING FORMULA AND GOLDEN THRESHOLD**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**PHASE 5: QUICK CHECKLIST**

One checkbox per criterion: `- [ ] C-NN: [one-line assertion]`

---

## Anchor Designation

**Anchor: V-03**

V-03 is designated the combination anchor for all Round 3 combination runs.

**Structural impact**: V-03's four-sub-step lifecycle change requires the builder to produce
three distinct structural artifacts per essential criterion — a pass condition, an inertia test
result, and a calibration pair — before the criterion is recorded in the table. This makes the
output of each sub-step a prerequisite for the next, so the lifecycle change propagates to all
three new v2 criteria (C-11, C-12, C-13) simultaneously. No other single-axis variation targets
all three.

**Isolation quality**: Only Phase 2 is modified. Phases 1, 3, 4, 5, and 6 are structurally
identical to V-01 and V-02. The per-criterion sub-step protocol is the only variable; any
co-variation observed in combination runs can be traced to V-03's sub-step structure.

**Detectable failure condition**: If a combination-run builder omits sub-step 2b or 2c, the
criterion table will be present but the inertia test result and calibration pair will be absent.
The gap is visible in the output as missing inline records, not as degraded quality — making
the failure mode mechanical and auditable. This is the kind of failure condition that makes
a variation useful as a combination anchor.

**Combination priority**: V-03 × V-05 is the highest-priority combination. V-03's per-criterion
sub-step gates enforce C-11/C-12/C-13 mechanically; V-05's Challenger role enforces C-11/C-12
socially (via role-level review). The combination tests whether structural gating and social
enforcement are redundant (both fire → both are needed) or additive (one fires where the other
misses → they cover different failure modes). If additive, the combination is the Round 3
candidate for the golden prompt.
