Written to `simulations/quest/variations/quest-rubric-variations-R1-2026-03-14.md`.

---

## Variations Summary

| ID | Axis | What changed | Hypothesis |
|----|------|-------------|------------|
| **V-01** | Baseline | Lifecycle-structured, imperative, table output | Standard structure mirrors how downstream consumers (quest:score) read rubrics |
| **V-02** | Output format | Prose blocks instead of table rows, plus explicit "Failure signal" field per criterion | Prose cells force richer pass condition explanation; cold reviewers can use the rubric without the spec |
| **V-03** | Phrasing register | Second-person reflective guidance ("ask yourself...", "once essential are solid, ask...") | Conversational framing surfaces the "why" and produces stronger design rationale; tradeoff is verbosity |
| **V-04** | Lifecycle emphasis | Setup compressed to one sentence; all space given to criterion construction protocol | The hard part isn't knowing what to read — it's deriving well-calibrated criteria; front-loading that logic produces better pass conditions |
| **V-05** | Combination: inertia framing + imperative + table | Opens with "the competitor you are beating" — names generic quality criteria as the status quo failure before any construction begins | Naming the failure mode first acts as a persistent filter on every criterion decision; the "skill-specificity test" is introduced at the top, not buried mid-prompt |

**Key design bets to test in scoring:**
- V-02 vs V-01: Does prose format produce richer pass conditions, or just noisier ones?
- V-04 vs V-01: Does front-loading construction logic reduce generic criteria, or does it overwhelm and produce worse essential sets?
- V-05 vs V-04: Does naming the failure mode explicitly outperform the construction protocol alone, or is it redundant once the protocol is present?
gotiable behaviors the skill must always exhibit. Every essential criterion must answer: "If this fails, the output is not usable -- full stop."

For each criterion, produce:
- **ID**: C-01, C-02... sequential, no gaps
- **Text**: bold title -- what the criterion checks -- followed by a dash and one plain-English sentence stating what it requires
- **Weight**: essential / recommended / aspirational
- **Category**: correctness / depth / format / coverage / behavior
- **Pass condition**: a binary, observable check -- counts, presence/absence, specific patterns, measurable thresholds. No "sufficient", "appropriate", or "good" without a number attached.

Weight distribution: 3-5 essential, 2-3 recommended, 1-2 aspirational.

After essential, add 2-3 recommended criteria (output is weaker without them but not broken) and 1-2 aspirational criteria (raise the bar once essential criteria are stable).

**Findings**

Write the rubric to `simulations/quest/rubrics/{skill}-rubric-{date}.md`.

Structure:

```
---
skill: {skill-id}
skill_target: {what skill this rubric evaluates}
date: {date}
version: 1
---

## Essential Criteria

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-01 | ... | essential | ... | ... |
...

## Recommended Criteria

| ID | Text | Weight | Category | Pass Condition |
...

## Aspirational Criteria

| ID | Text | Weight | Category | Pass Condition |
...

## Composite Score

Essential: 60 pts (each criterion = 60/N essential)
Recommended: 30 pts (each = 30/N recommended)
Aspirational: 10 pts (each = 10/N aspirational)

Golden threshold: all essential PASS + composite >= 80.

## Notes

Version 1. Grows as /quest:golden discovers excellence patterns.
```

**Amend**

User can add, remove, reweight, or reword criteria. The rubric is a living document. Bump the version field on each accepted change.

---

## V-02 — Output Format: Prose-First Criteria

**Axis**: Output format -- prose blocks instead of table rows
**Hypothesis**: Prose format forces the rubric author to write richer pass conditions (the table's compact cell constrains explanation). Criteria become more self-documenting, which matters when a reviewer reads the rubric cold without the skill spec.

---

You are running `/quest:rubric`.

Your job is to define the objective function for a skill: a scoring rubric that quest:score can apply mechanically and quest:golden can optimize against.

**Step 1 -- Read the skill spec**

Identify the promises: what the skill produces, what structure that artifact has, what each lifecycle phase contributes, what roles or lenses shape the output. Every promise is a candidate criterion. A rubric criterion is a broken promise made testable.

**Step 2 -- Generate essential criteria**

Write 3-5 essential criteria first. These are the non-negotiable behaviors. If any essential criterion fails, the output is not usable.

For each essential criterion, write a prose block:

```
**C-01 [essential / {category}]** -- {Title}: {one sentence stating what this criterion requires}

Pass condition: {one or two sentences describing what "pass" looks like in observable,
binary terms -- counts, presence/absence, specific patterns, measurable thresholds}

Failure signal: {one sentence on the most common way this criterion fails}
```

Repeat for C-02, C-03, etc.

**Step 3 -- Generate recommended and aspirational criteria**

Add 2-3 recommended criteria (output is weaker without them, not broken) using the same prose block format. Then 1-2 aspirational criteria (these raise the bar once essential criteria are stable).

Label each: [recommended] or [aspirational].

**Step 4 -- Write the rubric file**

Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`.

Open with YAML frontmatter:
```yaml
---
skill: {skill-id}
skill_target: {what skill this rubric evaluates}
date: {date}
version: 1
---
```

Then the prose blocks, grouped: Essential / Recommended / Aspirational.

Close with the scoring formula:

> Composite score = (essential passes / essential count) * 60 + (recommended passes / recommended count) * 30 + (aspirational passes / aspirational count) * 10.
> Golden threshold: all essential pass + composite >= 80.

End with a one-paragraph design rationale: why these criteria, what failure modes they catch, which criterion is hardest to satisfy and why.

**Step 5 -- Amend**

User can revise any criterion. Version field increments on each accepted change.

---

## V-03 -- Phrasing Register: Conversational/Reflective

**Axis**: Phrasing register -- second-person reflective guidance instead of imperative commands
**Hypothesis**: Conversational framing surfaces the "why" behind each decision and produces rubrics with stronger design rationale. Tradeoff: more verbose, potentially less precise on pass conditions.

---

You are building the objective function for a skill -- the scoring rubric that tells quest:score what "good" looks like and tells quest:golden what it's optimizing toward.

Start here: what does this skill promise?

Read the skill spec. As you read, write down the promises: what artifact it produces, what structure that artifact has, what each lifecycle phase contributes, what roles or lenses shape the output. Every promise is a candidate criterion. A rubric criterion is a broken promise made testable.

**Building your essential criteria**

Ask yourself: "If I gave this rubric to a reviewer who had never seen the skill spec, could they distinguish a usable output from a broken one?" That's your essential set -- 3 to 5 criteria that form a complete "is this output usable?" gate.

For each essential criterion, ask:
- What behavior am I actually testing? (Be specific to this skill -- not "is it well-structured" but "does it contain X, Y, Z")
- How would I check this in 30 seconds? (Counts, presence/absence, specific patterns -- no judgment calls)
- What's the most common way someone would get this wrong? (That's your failure signal)

Assign each criterion to one of five categories: correctness (does it do what the spec says?), depth (does it go deep enough?), format (is it shaped right?), coverage (does it cover the right ground?), behavior (does it behave correctly under all conditions?).

**Layering in recommended and aspirational criteria**

Once essential criteria are solid, ask: "What would make this output not just usable but genuinely good?" Those are your recommended criteria -- 2 to 3 of them.

Then: "What would make it excellent?" Those are aspirational -- 1 to 2. Aspirational criteria often require human judgment to evaluate; that's fine, but note it explicitly in the pass condition.

**Writing the rubric file**

Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md` with this structure:

- Frontmatter: skill, skill_target, date, version: 1
- Three sections: Essential / Recommended / Aspirational
- Each criterion: ID (C-01, C-02...), text, weight, category, pass condition
- Scoring: essential 60 pts, recommended 30 pts, aspirational 10 pts; golden = all essential pass + composite >= 80
- Design rationale: one paragraph on why these criteria, what failure modes they catch, which is hardest and why

Use table format for the criteria. Keep pass conditions in the table cell -- one or two sentences, binary and observable.

After you write the file, name the one criterion you're least confident about and why. That's usually where the rubric needs the most iteration.

---

## V-04 -- Lifecycle Emphasis: Compressed Setup, Expanded Construction Logic

**Axis**: Lifecycle emphasis -- minimal setup instructions, maximum space on rubric construction logic
**Hypothesis**: The real difficulty in quest:rubric is not knowing what to read -- it's knowing how to derive good criteria from what you read. Compressing setup and expanding the construction protocol produces better-calibrated essential criteria and better pass conditions.

---

You are running `/quest:rubric`. Read the skill spec. Then build the rubric as follows.

**Criterion construction protocol**

For each lifecycle phase in the skill spec (setup, execute, findings, amend), ask:
1. What does this phase produce? Candidate correctness or coverage criterion.
2. What does "complete" look like for this phase's output? Candidate pass condition.
3. What's the most common way this phase's output fails? Alternative framing of the same criterion.

For the skill's output artifact, ask:
1. What fields or sections must be present? Structural completeness criterion.
2. What values are constrained? (counts, types, ranges) Constraint criterion.
3. What would make the artifact unusable to the downstream consumer (quest:score)? Essential criterion.

**The skill-specificity test**

For every candidate criterion, run this test: "Could this criterion appear word-for-word in a rubric for a completely different skill?"

If yes: rewrite it. A criterion for quest:rubric should reference weight counts, formula presence, pass condition binary-ness, criterion IDs -- not "is well-organized" or "covers all bases."

A criterion that fails the skill-specificity test is not a criterion -- it is noise.

**Pass condition construction**

For each criterion, derive the pass condition by answering: "What would I count, look for, or measure to know this passes -- in 30 seconds, without judgment?"

Acceptable anchors: count in range [N, M], string present / absent, section exists, field non-empty, all items satisfy property X, N of M items satisfy property X.

Unacceptable without anchors: good, sufficient, appropriate, thorough, complete (these require a measurable anchor to be usable).

**Weight assignment**

Essential (3-5 criteria): output is not usable if this fails. No exceptions.
Recommended (2-3): output is weaker without this, not broken.
Aspirational (1-2): distinguishes excellent from merely acceptable.

**Scoring formula -- state this exactly in the rubric**

Composite = (essential passes / essential count) * 60 + (recommended passes / recommended count) * 30 + (aspirational passes / aspirational count) * 10.

Golden threshold: all essential criteria pass AND composite >= 80.

**Rubric file**

Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`.

Frontmatter: skill, skill_target, date, version: 1.

Body: three sections (Essential / Recommended / Aspirational), each a table with columns: ID | Text | Weight | Category | Pass Condition.

Close with: Notes section stating this is version 1 and the rubric grows as /quest:golden discovers excellence patterns.

---

## V-05 -- Combination: Inertia Framing + Imperative + Table

**Axis**: Combination -- prominent inertia framing (leading with the most common failure mode) + imperative + table
**Hypothesis**: The dominant failure mode for quest:rubric is producing generic quality criteria ("is well-written", "covers all phases") that apply to any skill. Naming this failure mode first -- as the "status quo competitor" the rubric must beat -- anchors all subsequent criterion construction toward specificity. The inertia framing acts as a persistent filter on every criterion decision.

---

You are running `/quest:rubric`.

**The competitor you are beating**

Before you write a single criterion, name the failure you are preventing: generic quality criteria. These are criteria that could appear in a rubric for any skill -- "output is well-structured," "covers all required phases," "is clear and complete." They are the status quo. They feel like a rubric. They do not function as one.

A rubric full of generic criteria will pass every mediocre output and fail to distinguish excellent from adequate. quest:score becomes meaningless. quest:golden has no signal to optimize.

Your rubric beats the status quo by being specific: every criterion names a behavior, output, or property unique to the target skill.

**Setup**

Read the skill spec. Extract:
- The artifact the skill produces (name it, describe its required structure)
- The lifecycle phases and what each one outputs
- Any constraints stated in the spec (counts, formats, required fields, threshold values)
- What the downstream consumer (quest:score) needs from the rubric to function

**Execute**

Generate criteria C-01 through C-NN. Run each candidate through the skill-specificity test before including it: "Does this criterion name something specific to this skill -- a field name, a count range, a formula, a structural property -- or is it generic?" If generic, rewrite or discard.

For each criterion:

| Field | Requirement |
|-------|-------------|
| ID | C-01, C-02... sequential, no gaps |
| Text | Bold title + dash + one sentence. The sentence must name something specific to this skill. |
| Weight | essential / recommended / aspirational |
| Category | correctness / depth / format / coverage / behavior -- no other values |
| Pass condition | Binary, observable. Counts, presence/absence, patterns, thresholds. No judgment words without a measurable anchor. |

Weight distribution: 3-5 essential, 2-3 recommended, 1-2 aspirational.

Essential first. For each candidate essential criterion, ask: "If this fails, is the output genuinely not usable -- or just worse?" Only genuinely unusable failures are essential.

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

## Design Rationale
{One paragraph: why these criteria, what failure modes they catch, which generic
criteria were considered and rejected, which criterion is hardest to satisfy.}

## Notes
Version 1. Grows as /quest:golden discovers excellence patterns not yet captured here.
```

**Amend**

User reviews the rubric. For each criterion they flag: is it specific enough? Is the pass condition binary? Does it catch a real failure mode? Revise on feedback. Bump the version field on each accepted change.
