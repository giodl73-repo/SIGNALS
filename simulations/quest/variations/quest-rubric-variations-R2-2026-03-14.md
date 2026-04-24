Written to `simulations/quest/variations/quest-rubric-variations-R2-2026-03-14.md`.

---

## Variations Summary

| ID | Axis | Hypothesis |
|----|------|------------|
| **V-01** | Rejection log gate | Step 0 forces enumeration of rejected generic criteria before spec is read — produces C-13 and trains the specificity filter before construction begins |
| **V-02** | Banned-qualifier enforcement | Embedding the banned qualifier list in the prompt makes C-12 a writing constraint rather than a post-hoc audit target |
| **V-03** | Self-application gate | Scoring the draft rubric against itself before finalizing forces the concrete good/poor thought experiment that has been PARTIAL on C-09 across all R1 variations |
| **V-04** | V-05 + rejection log gate + banned-qualifier | Three-layer filter: V-05 names the failure mode, Step 0 documents the rejected generics, banned-qualifier list closes pass condition language |
| **V-05** | V-05 + self-application gate + PARTIAL rule + design rationale before criteria | Closes every remaining R1 gap: self-application raises C-09, PARTIAL rule completes the scoring section, design rationale *before* the first table satisfies C-11 structurally |

**Key bets to watch in R2 scoring:**
- V-01 vs V-05 R1: Does Step 0 rejection log alone (without the full V-05 base) get C-13 to PASS?
- V-02 vs V-05 R1: Does the banned-qualifier list move C-12 from PARTIAL to PASS without the other signals?
- V-03 vs V-05 R1: Does the self-application gate alone move C-09 from PARTIAL to PASS?
- V-05 R2 vs V-05 R1: Does the design-rationale-before-criteria structural requirement actually guarantee C-11, or does it just move it closer?
jection log proves filter ran, banned-qualifier list closes pass condition language |
| **V-05** | Combination: V-05 + self-application gate + PARTIAL rule + design rationale gate | V-05 base + self-application + explicit PARTIAL scoring + design rationale required before first criteria table | Closes all remaining R1 gaps: self-application elevates C-09; PARTIAL rule completes scoring section; pre-criteria design rationale satisfies C-11 |

---

## V-01 — Rejection Log Gate

**Axis**: Rejection log gate — enumerate and formally reject generic criteria before reading spec
**Hypothesis**: Forcing explicit rejection before construction produces the rejection log (C-13), trains the specificity filter for all subsequent criterion decisions, and makes C-04 a guaranteed pass rather than a risk.

---

You are running `/quest:rubric`.

**Step 0 -- Enumerate and reject generics**

Before you open the skill spec, write down five generic quality criteria -- the kind that could appear in a rubric for any skill, regardless of what that skill does. These are the criteria you are NOT building.

Write them now as an explicit rejection log:

```
Rejected (generic -- would pass any skill's output, not this one's):
- "output is well-structured"
- "covers all required phases"
- "is clear and complete"
- "is appropriately detailed"
- "follows the correct format"
```

You may replace these with your own examples if they are more specific to the skill you are about to read. The point is to name them, not just intend to avoid them. Keep this list. It will go into the design rationale.

**Step 1 -- Read the skill spec**

Read the skill spec. Extract:
- The artifact the skill produces (name and required structure)
- The lifecycle phases and what each one outputs
- Any constraints stated in the spec: counts, formats, required fields, threshold values
- What the downstream consumer (quest:score) needs from the rubric to function

**Step 2 -- Generate criteria**

Produce criteria C-01 through C-NN. Before including any criterion, apply the skill-specificity test: "Does this criterion name a behavior, output, or structural property unique to this skill -- a field name, a count range, a formula, a required section -- or is it generic?"

If the candidate criterion resembles anything in the Step 0 rejection log: rewrite or discard it.

For each criterion:

| Field | Requirement |
|-------|-------------|
| ID | C-01, C-02... sequential, no gaps |
| Text | Bold title + dash + one sentence. The sentence must name something specific to this skill. |
| Weight | essential / recommended / aspirational |
| Category | correctness / depth / format / coverage / behavior |
| Pass condition | Binary and observable. Use counts, presence/absence, specific patterns, or measurable thresholds. |

Weight distribution: 3-5 essential, 2-3 recommended, 1-2 aspirational.

Essential criteria answer: "If this fails, is the output genuinely not usable?" Only write essential if the answer is yes with no exceptions.

**Step 3 -- Write the rubric file**

Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`.

Frontmatter:
```yaml
---
skill: {skill-id}
skill_target: {what this rubric evaluates}
date: {date}
version: 1
---
```

Three sections in order: Essential / Recommended / Aspirational. Each section is a table:
`| ID | Text | Weight | Category | Pass Condition |`

Scoring section (state exactly):
```
Composite = (essential passes / essential count) * 60 + (recommended passes / recommended count) * 30 + (aspirational passes / aspirational count) * 10

Golden threshold: all essential PASS + composite >= 80.

PARTIAL on an essential criterion counts as 0.5 for score math but does not satisfy the all-essential-pass precondition.
```

Design rationale section: one paragraph naming the dominant failure mode for this skill, the failure modes the essential criteria catch, and the rejection log from Step 0 -- copy it in, marking which criteria you considered and discarded.

Notes section: "Version 1. Grows as /quest:golden discovers excellence patterns."

**Step 4 -- Amend**

User can revise any criterion. For each flagged criterion, check: Is it skill-specific? Is the pass condition binary? Does it catch a failure mode not already caught by another criterion? Revise. Bump version on each accepted change.

---

## V-02 -- Banned-Qualifier Enforcement

**Axis**: Banned-qualifier enforcement -- embed an explicit banned-qualifier list in the prompt; pass conditions must not use listed qualifiers without a measurable anchor
**Hypothesis**: Naming the banned qualifiers before construction propagates C-12 compliance as a writing constraint, not a review criterion. The author never needs to retroactively audit pass conditions because the constraint is active during construction.

---

You are running `/quest:rubric`.

**Read the skill spec. Then build the rubric.**

**Criterion construction rules**

For each criterion, produce:
- **ID**: C-01, C-02... sequential, no gaps
- **Text**: bold title + dash + one sentence stating what this criterion requires, naming something specific to this skill
- **Weight**: essential / recommended / aspirational
- **Category**: correctness / depth / format / coverage / behavior -- no other values
- **Pass condition**: binary and observable

**Banned qualifiers in pass conditions**

The following words and phrases are BANNED in pass conditions unless paired with a measurable anchor (count, threshold, or presence/absence pattern):

> good * sufficient * appropriate * thorough * complete * clear * comprehensive * adequate * proper * well-structured * detailed * robust

A banned qualifier used without an anchor means the pass condition requires subjective judgment. A rubric criterion that requires judgment is not a criterion -- it is a question. Rewrite until the pass condition is a count, a presence/absence check, a specific pattern, or a measurable threshold.

**Acceptable pass condition patterns:**
- "Count of X in [N, M]"
- "Field Y is present and non-empty"
- "All items in set Z satisfy property P"
- "Section S exists with header H"
- "Pattern R matches / does not match"
- "Value V equals / does not equal"

**Banned pattern example:**
- "pass condition is appropriate" -- rewrite as: "pass condition does not contain any banned qualifiers without a count or presence/absence anchor"

**Skill-specificity rule**

Every essential criterion must name something specific to this skill -- a field name, a count range, a formula, a structural property, a lifecycle output. Run this test on each candidate: "Could this criterion appear word-for-word in a rubric for a completely different skill?" If yes, rewrite it.

**Weight distribution:** 3-5 essential, 2-3 recommended, 1-2 aspirational.

**Findings**

Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`.

```
---
skill: {skill-id}
skill_target: {what this rubric evaluates}
date: {date}
version: 1
---

## Essential Criteria
| ID | Text | Weight | Category | Pass Condition |
...

## Recommended Criteria
| ID | Text | Weight | Category | Pass Condition |
...

## Aspirational Criteria
| ID | Text | Weight | Category | Pass Condition |
...

## Composite Score
Essential: 60 pts | Recommended: 30 pts | Aspirational: 10 pts
Golden threshold: all essential PASS + composite >= 80.
PARTIAL on an essential criterion counts as 0.5 for score math but does not satisfy the all-essential-pass precondition.

## Design Rationale
{One paragraph: the dominant failure mode for this skill; which failure modes the essential
criteria catch; which criterion is hardest to satisfy and why.}

## Notes
Version 1. Grows as /quest:golden discovers excellence patterns.
```

**Amend**

User can flag any criterion. For each: Is the pass condition free of banned qualifiers without anchors? Is it skill-specific? Is it distinct from other essential criteria? Revise on feedback. Bump version on each accepted change.

---

## V-03 -- Self-Application Gate

**Axis**: Self-application gate -- score the draft rubric against its own essential criteria before writing the final file
**Hypothesis**: Self-application forces a concrete thought experiment (C-09): the rubric author must identify at least one failure the rubric would catch on a poor output and at least one it passes on a strong output. It also catches structural defects (field gaps, wrong weight counts, subjective pass conditions) before delivery.

---

You are running `/quest:rubric`.

**Setup**

Read the skill spec. Extract: the artifact the skill produces, its required structure, the lifecycle phases and their outputs, any constraints in the spec (counts, formats, required fields, threshold values).

**Execute**

Generate criteria C-01 through C-NN using this format:

| Field | Requirement |
|-------|-------------|
| ID | C-01, C-02... sequential, no gaps |
| Text | Bold title + dash + one sentence. Name something specific to this skill. |
| Weight | essential / recommended / aspirational |
| Category | correctness / depth / format / coverage / behavior |
| Pass condition | Binary, observable -- counts, presence/absence, patterns, thresholds. No "sufficient", "good", or "appropriate" without a measurable anchor. |

Weight distribution: 3-5 essential, 2-3 recommended, 1-2 aspirational.

Skill-specificity test for every criterion: "Could this appear in a rubric for a completely different skill?" If yes, rewrite it.

**Self-application gate -- run before writing the file**

Before you write the rubric file, score your draft rubric against itself. For each essential criterion you just wrote, answer:

1. Does this criterion pass against my own rubric? If no, fix it before proceeding.
2. Think of a mediocre rubric output -- one that looks like a rubric but is full of generic criteria, or has the wrong weight distribution, or has subjective pass conditions. Which of my essential criteria does it fail first? Name the criterion ID and why.
3. Think of a strong rubric output -- one that passes all essential criteria. Which recommended or aspirational criterion would it still fail? Name one.

If you cannot answer (2) with a specific essential criterion ID, your essential set is not catching real failures. Revise before proceeding.

Record your answers to (2) and (3) in the design rationale section.

**Findings**

Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`.

```
---
skill: {skill-id}
skill_target: {what this rubric evaluates}
date: {date}
version: 1
---

## Essential Criteria
| ID | Text | Weight | Category | Pass Condition |
...

## Recommended Criteria
| ID | Text | Weight | Category | Pass Condition |
...

## Aspirational Criteria
| ID | Text | Weight | Category | Pass Condition |
...

## Composite Score
Essential: 60 pts | Recommended: 30 pts | Aspirational: 10 pts
Golden threshold: all essential PASS + composite >= 80.
PARTIAL on an essential criterion counts as 0.5 for score math but does not satisfy the all-essential-pass precondition.

## Design Rationale
{Dominant failure mode for this skill. Failure modes the essential criteria catch.
Self-application results: (a) which essential criterion a mediocre output would fail first,
and why; (b) which recommended or aspirational criterion a strong output would still fail.
Which criterion is hardest to satisfy.}

## Notes
Version 1. Grows as /quest:golden discovers excellence patterns.
```

**Amend**

User can flag any criterion. For each revision, re-run the self-application gate answers: does the change break any self-application result? Revise. Bump version.

---

## V-04 -- Combination: V-05 Base + Rejection Log Gate + Banned-Qualifier List

**Axis**: Combination -- V-05's inertia framing + Step 0 rejection log gate + banned-qualifier enforcement
**Hypothesis**: Stacking V-05's pre-construction failure mode framing with an explicit rejection log and a banned-qualifier list creates maximum filter pressure at every stage: intent is named before construction begins, rejection is documented at the top, and language constraints propagate into every pass condition.

---

You are running `/quest:rubric`.

**The competitor you are beating**

Before you write a single criterion, name the failure you are preventing: generic quality criteria. These are criteria that could appear in a rubric for any skill -- "output is well-structured," "covers all required phases," "is clear and complete," "is appropriately detailed." They are the status quo. They feel like a rubric. They do not function as one.

A rubric full of generic criteria will pass every mediocre output and fail to distinguish excellent from adequate. quest:score becomes meaningless. quest:golden has no signal to optimize.

Your rubric beats the status quo by being specific: every criterion names a behavior, output, or property unique to the target skill.

**Step 0 -- Write the rejection log**

Before you open the skill spec, write five generic criteria you are committing to exclude:

```
Rejected (generic -- applicable to any skill's output, not this one's):
1. ...
2. ...
3. ...
4. ...
5. ...
```

Keep this list. It goes into the design rationale. Any criterion that resembles an item on this list must be rewritten or discarded.

**Step 1 -- Setup**

Read the skill spec. Extract:
- The artifact the skill produces (name and required structure)
- The lifecycle phases and what each one outputs
- Any constraints stated in the spec (counts, formats, required fields, threshold values)
- What the downstream consumer (quest:score) needs from the rubric

**Step 2 -- Execute**

Generate criteria C-01 through C-NN. Run each candidate through:
1. **Skill-specificity test**: "Does this criterion name something specific to this skill -- a field name, a count range, a formula, a structural property?" If no: rewrite or discard.
2. **Rejection log check**: Does it resemble any item on the Step 0 rejection log? If yes: rewrite or discard.

For each criterion:

| Field | Requirement |
|-------|-------------|
| ID | C-01, C-02... sequential, no gaps |
| Text | Bold title + dash + one sentence naming something specific to this skill |
| Weight | essential / recommended / aspirational |
| Category | correctness / depth / format / coverage / behavior -- **no other values** |
| Pass condition | Binary, observable. Must not use these without a measurable anchor: *good * sufficient * appropriate * thorough * complete * clear * comprehensive * adequate*. Use counts, presence/absence, or patterns instead. |

Weight distribution: 3-5 essential, 2-3 recommended, 1-2 aspirational.

For every essential criterion: "If this fails, is the output genuinely not usable -- full stop?" Only genuinely unusable failures are essential.

**Step 3 -- Findings**

Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`.

```
---
skill: {skill-id}
skill_target: {what this rubric evaluates}
date: {date}
version: 1
---

## Essential Criteria
| ID | Text | Weight | Category | Pass Condition |
...

## Recommended Criteria
| ID | Text | Weight | Category | Pass Condition |
...

## Aspirational Criteria
| ID | Text | Weight | Category | Pass Condition |
...

## Composite Score
Essential: 60 pts | Recommended: 30 pts | Aspirational: 10 pts
Golden threshold: all essential PASS + composite >= 80.
PARTIAL on an essential criterion counts as 0.5 for score math but does not satisfy the all-essential-pass precondition.

## Design Rationale
{One paragraph. Open with the dominant failure mode for this skill -- state it as the
first sentence, before any criterion is described. Then: which failure modes the essential
criteria catch; the rejection log from Step 0 verbatim -- name the generic criteria
considered and discarded; which criterion is hardest to satisfy and why.}

## Notes
Version 1. Grows as /quest:golden discovers excellence patterns.
```

**Step 4 -- Amend**

User reviews the rubric. For each flagged criterion: Is it specific to this skill? Is the pass condition free of banned qualifiers without anchors? Is it distinct from other essential criteria -- does it catch a different failure? Revise. Bump version.

---

## V-05 -- Combination: V-05 Base + Self-Application Gate + PARTIAL Rule + Design Rationale Gate

**Axis**: Combination -- V-05's inertia framing + self-application gate + explicit PARTIAL scoring rule + design rationale required BEFORE first criteria table
**Hypothesis**: Self-application elevates C-09 to PASS (concrete good/poor classification); explicit PARTIAL rule closes the scoring section gap; requiring design rationale before the first criteria table satisfies C-11 structurally. Together these close all remaining gaps that prevented V-05 R1 from scoring 100 against the v2 rubric.

---

You are running `/quest:rubric`.

**The competitor you are beating**

Before you write a single criterion, name the failure you are preventing: generic quality criteria. These are criteria that could appear in a rubric for any skill -- "output is well-structured," "covers all required phases," "is clear and complete." They feel like a rubric. They do not function as one.

Your rubric beats the status quo by being specific: every criterion names a behavior, output, or structural property unique to the target skill.

**Setup**

Read the skill spec. Extract:
- The artifact the skill produces and its required structure
- The lifecycle phases and what each one outputs
- Any constraints in the spec: counts, formats, required fields, threshold values
- What the downstream consumer (quest:score) needs from the rubric to function

**Execute**

Generate criteria C-01 through C-NN. Run each candidate through the skill-specificity test before including it: "Does this criterion name something specific to this skill -- a field name, a count range, a formula, a structural property -- or is it generic?" If generic: rewrite or discard.

For each criterion:

| Field | Requirement |
|-------|-------------|
| ID | C-01, C-02... sequential, no gaps |
| Text | Bold title + dash + one sentence. The sentence must name something specific to this skill. |
| Weight | essential / recommended / aspirational |
| Category | correctness / depth / format / coverage / behavior -- no other values |
| Pass condition | Binary, observable. Counts, presence/absence, patterns, thresholds. No "sufficient", "appropriate", "good", "thorough", "complete" without a measurable anchor. |

Weight distribution: 3-5 essential, 2-3 recommended, 1-2 aspirational.

Essential: if this fails, is the output genuinely not usable -- full stop? Only genuinely unusable failures are essential.

**Self-application gate -- run before writing the file**

Score your draft rubric against its own essential criteria:

1. For each essential criterion: does my draft rubric satisfy its own pass condition? If no, fix before proceeding.
2. Construct a minimal poor output: a rubric-shaped document full of generic criteria, wrong weight counts, or missing fields. Which essential criterion does it fail first? Name the criterion ID and explain why.
3. Construct a minimal strong output: a rubric that passes all essential criteria. Which recommended or aspirational criterion would it still fail? Name one.

If you cannot complete (2), your essential set does not catch real failures. Revise.

**Findings**

Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`.

The file must be structured in this exact order:

```
---
skill: {skill-id}
skill_target: {what this rubric evaluates}
date: {date}
version: 1
---

## Design Rationale
{One paragraph, written BEFORE the first criteria table. First sentence states the
dominant failure mode for this skill. Then: which failure modes the essential criteria
catch; which generic criteria were considered and rejected (name them explicitly);
self-application results (criterion ID a poor output fails first; criterion a strong output
still fails); which criterion is hardest to satisfy.}

## Essential Criteria
| ID | Text | Weight | Category | Pass Condition |
...

## Recommended Criteria
| ID | Text | Weight | Category | Pass Condition |
...

## Aspirational Criteria
| ID | Text | Weight | Category | Pass Condition |
...

## Composite Score
Essential: 60 pts | Recommended: 30 pts | Aspirational: 10 pts
Golden threshold: all essential PASS + composite >= 80.
PARTIAL on an essential criterion counts as 0.5 for score math but does not satisfy
the all-essential-pass precondition.

## Notes
Version 1. Grows as /quest:golden discovers excellence patterns not yet captured here.
```

**Amend**

User reviews the rubric. For each flagged criterion: Is it specific to this skill? Is the pass condition binary and free of bare subjective qualifiers? Does it catch a failure mode not caught by another criterion? Revise. Bump version on each accepted change.
