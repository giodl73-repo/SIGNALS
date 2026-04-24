Written to `simulations/quest/variations/review-customers-variations-R2-2026-03-14.md`.

---

## review-customers R2 -- 5 Variations

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Hybrid format (C-12, single axis) | Separating the table from prose blocks resolves the V-02 completeness-depth trade-off |
| V-02 | Causal rationale (C-13, single axis) | Naming the feature property/gap as mechanism produces C-13-qualifying rationale in 8+ personas |
| V-03 | Inline flags isolated (C-11, single axis) | The [BLOCKER]/[LEAK] mechanism from V-05 can work without the 7-phase scaffold |
| V-04 | Full C-11+C-12+C-13 combined | V-05 + hybrid + causal targets all 13 criteria simultaneously |
| V-05 | Causal conversational + hybrid (C-12+C-13) | Prose-first then table produces richer C-13 rationale than table-first structures |

**Key design decisions:**

**V-01 vs V-04** isolates the cost of V-05's phase-gate mechanism when C-12 and C-13 are already present. If both score the same, phase gates add no value over a simpler hybrid prompt.

**V-03** is the critical structural question from R1: is inline flagging orthogonal to phase complexity? If V-03 passes C-11 without phases, the flag mechanism is cheap to backport anywhere.

**V-05 inverts the ordering hypothesis**: V-01 and V-04 both go table-first then prose. V-05 goes prose-first then compiles the table. If V-05 produces stronger C-13 rationale, it means the structure was constraining the reasoning in table-first formats.

**Recommended scoring order:** V-03 -> V-02 -> V-01 -> V-05 -> V-04.
 when C-12 and C-13 are already present.
- **V-02** is the isolated C-13 test. It descends from V-04 (conversational) because R1 showed
  register is the strongest predictor of rationale depth. The hypothesis is that upgrading the
  rationale instruction from "explain what produced" to "name the feature mechanism" moves the
  output from C-08 to C-13 without format changes.
- **V-03** is the isolated C-11 test. The question from R1: does inline flagging require 7 phases,
  or is it an orthogonal mechanism? If V-03 passes C-11 without phases, the flag mechanism can
  be backported into V-01/V-02 cheaply.
- **V-05** tests prose-first ordering: all twelve persona rationales before the table. The
  hypothesis is that building the table after reasoning (rather than before writing prose)
  produces better C-13 rationale because the model reasons through the persona encounter before
  committing to a structure.

**Recommended scoring order:** V-03 (C-11 isolation) -> V-02 (C-13 isolation) -> V-01 (C-12
isolation) -> V-05 (C-12+C-13 in conversational) -> V-04 (all three combined).

---

## V-01: Hybrid Format

Axis: Output format -- scoring table (completeness layer) separated from per-persona prose blocks
(rationale layer). Single-axis test of C-12.
Hypothesis: Splitting the table from the prose eliminates the V-02 R1 completeness-depth trade-off.
The table guarantees C-01/C-05 completeness and tier auditability before any prose is written.
The prose blocks guarantee 2+ sentence rationale depth that the table row constraint prevented.
Inline flags during prose phase achieve C-11 without requiring a separate DETECT phase.

```
You are running /review:customers. Scoring is structured in two layers: a summary table for
completeness and auditability, followed by per-persona prose blocks for rationale depth. Both
layers are required. Inline flags surface blockers and leaks during the prose phase.

--- PHASE 1: DECLARE TIERS ---

Read the input signal for {{Topic}} -- the relevant spec, proposal, or feature description.

STOCK PERSONAS:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

Assign each persona a tier. State all 12 grouped by tier:
  Primary:    [list IDs and names]
  Secondary:  [list IDs and names]
  Non-target: [list IDs and names]

Segmentation rationale: one sentence explaining the tier logic for this feature.
Do not proceed to Phase 2 until all 12 are classified.

--- PHASE 2: SCORING TABLE ---

Build the scoring table first. All 12 rows required. Tier labels must appear in every row.
This table is the completeness layer -- do not write prose rationale here.

| ID   | Name            | Role        | Tier       | Useful | Clarity | W-Adopt |
|------|-----------------|-------------|------------|--------|---------|---------|
| C-01 | Maria Chen      | Maker       | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-02 | James Okafor    | Builder     | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-03 | Priya Nair      | Strategist  | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-04 | Tom Bergstrom   | Operator    | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-05 | Aisha Mensah    | Researcher  | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-06 | Carlos Reyes    | Designer    | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-07 | Lin Wei         | Analyst     | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-08 | Sophie Dubois   | Manager     | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-09 | Raj Patel       | Advocate    | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-10 | Yuki Tanaka     | Evaluator   | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-11 | Elena Vasquez   | Buyer       | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-12 | Frank Hoffmann  | Regulator   | [tier]     | [1-5]  | [1-5]   | [1-5]   |

The table carries all scores and tier labels. It must be complete before Phase 3 begins.
Do not proceed to Phase 3 until every row is filled.

--- PHASE 3: PROSE RATIONALE BLOCKS ---

For each persona, write a prose block of 2-3 sentences. The table already carries the scores;
the prose block adds the explanation. The prose block must go beyond the table:
- Do not restate the scores.
- Identify the specific feature property, design gap, or workflow fit/mismatch that produced
  the scores. The rationale must implicate the feature, not just describe the persona's role
  or preferences. "The feature's [X] produced this reaction" -- not "This persona values [Y]."
- Apply inline flags to the persona header line before the prose (based on Phase 2 table):
    [BLOCKER]            -- primary tier, W-Adopt < 3
    [LEAK]               -- non-target tier, Useful >= 4 or W-Adopt >= 3
    [DELIGHT: dimension] -- any score of 5

Format per persona:

[C-NN] [Name] ([Role]) | [tier] | [inline flags if applicable]
[2-3 sentence causal prose rationale]

Write all 12. Do not proceed to Phase 4 until all 12 prose blocks are complete.

--- PHASE 4: DETECT ---

Review the inline flags from Phase 3. Each check requires an explicit result.
Blank or omitted = fail. Do not proceed until all three checks are stated.

ADOPTION BLOCKERS:
Collect all [BLOCKER] entries from Phase 3.
List: [ID] [Name] -- W-Adopt: [score] -- [one sentence on which feature property/gap is blocking adoption].
If no [BLOCKER] entries exist: state "No adoption blockers."

POSITIONING LEAKS:
Collect all [LEAK] entries from Phase 3.
List: [ID] [Name] -- [signal: Useful or W-Adopt score] -- [what feature framing/scope caused this].
If no [LEAK] entries exist: state "No positioning leaks."

DELIGHT SIGNALS:
Collect all [DELIGHT] entries from Phase 3. Group by dimension.
List: [ID] [Name] -- [dimension] -- [positioning or marketing implication].
If none: state "No delight signals."

--- PHASE 5: AGGREGATE ---

WEIGHTED SCORE:
Weights: primary 3x, secondary 2x, non-target 1x.
State the count and weight for each tier. Compute from the Phase 2 table:

  weighted_usefulness  = (sum primary useful x 3 + sum secondary useful x 2 +
                          sum nontarget useful x 1) / (3 x n_p + 2 x n_s + 1 x n_nt)
  weighted_clarity     = (same formula)
  weighted_would_adopt = (same formula)
  weighted_composite   = (weighted_usefulness + weighted_clarity + weighted_would_adopt) / 3

Show the full calculation. Present results on a 1-5 scale.

CROSS-PERSONA PATTERN:
Using the Phase 2 table and Phase 3 prose blocks, identify at least one named cross-cutting
pattern -- a tier cluster where one dimension consistently lags another, a sharp drop between
primary and secondary W-Adopt scores, or a role type with a distinctive scoring signature.
Name the pattern and state the design or messaging implication.
Generic observations ("scores vary") do not qualify.

--- PHASE 6: AMEND ---

Address Phase 4 findings in this order:

1. ADOPTION BLOCKERS:
   For each [BLOCKER]:
   - Change: [specific feature scope, messaging, UX, or framing change]
   - Projected impact: "Resolving [ID] blocker by [change] likely lifts primary W-Adopt by ~[delta],
     moving weighted composite from [current] to approximately [current + effect]."

2. POSITIONING LEAKS:
   For each [LEAK]:
   - Change: [specific messaging, scoping, or naming change]
   - Projected impact: directional estimate on non-target confusion or composite movement.

3. DELIGHT AMPLIFICATION:
   For each delight signal: how the feature or its positioning could reinforce what is landing.

If Phase 4 found no blockers: state "No adoption blockers to resolve." Skip section 1.
If Phase 4 found no leaks: state "No positioning leaks to close." Skip section 2.
(C-10 auto-passes when both blockers and leaks are absent -- the score is clean by definition.)

Write artifact to simulations/review/customers/{topic}-customers-{date}.md.
Frontmatter: skill: review-customers, topic, date, input, output_format: hybrid-table-prose,
phases: [declare, table, prose, detect, aggregate, amend].
```

---

## V-02: Causal Rationale

Axis: Rationale framing -- explicit causal instruction requiring feature property/gap named as
the mechanism that drove the score. Single-axis test of C-13.
Hypothesis: Upgrading from "explain what produced these reactions" (V-04 R1) to "name the specific
feature property, design gap, or workflow mismatch as the causal driver -- not the persona's
context" produces C-13-qualifying rationale in 8+ of 12 personas. The instruction specifies the
mechanism rather than prohibiting a behavior (R1's winning formulation), taken one step further.

```
You are running /review:customers. Work through this as a customer advisory panel, not a
checklist. The goal is to understand what twelve different people would actually think, feel,
and decide if they encountered this feature today.

---

WHAT ARE WE EVALUATING?

Read the spec or signal for {{Topic}}. Understand what the feature does, what problem it
solves, and what it asks of the people who use it. Before you invite anyone into the room,
make sure you know what you are showing them.

---

WHO IS THIS FEATURE FOR?

The panel has twelve seats:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

Decide: who is in the primary audience? Who is secondary? Who is not the target?

Write it out for all twelve before you score anything:
"C-01 Maria Chen -- primary," and so on. The weighting that follows depends on this, and you
cannot audit the aggregate without knowing every persona's tier.

---

WHAT DOES EACH PERSONA ACTUALLY ENCOUNTER?

Take them through the feature one at a time. For each persona, score three dimensions from
1 to 5 and then explain the scores:

- Usefulness: Does this solve a real problem they actually have? (1 = irrelevant to their
  work; 5 = solves something they struggle with today)
- Clarity: Do they understand what this is and what it does? (1 = confused about the basic
  proposition; 5 = immediately obvious)
- Would-Adopt: Would they actually use this, given how they work right now? (1 = no chance;
  5 = adopts immediately without being asked)

After the three scores, write 2-3 sentences of causal rationale. The rationale must name a
specific feature property, design gap, or workflow fit/mismatch as the driver of these scores.
The framing is: "The feature's [specific property or gap] produces this reaction" -- not "This
persona values [thing]." If a gap in the feature explains why a primary persona would hesitate,
name that gap. If a property of the feature is exactly right for this persona, name that
property. Rationale that only describes who the persona is or what they care about in general
-- without tying back to something the feature does or fails to do -- does not explain the scores.

Do this for all twelve. Non-target personas matter: if the feature's framing or naming attracts
or confuses them, that is a signal about the feature, not about them.

---

IS ADOPTION BLOCKED?

Look at the would-adopt scores for your primary-audience personas. Did any score below 3?
If yes, name each blocker by ID, cite the score, and name the specific feature property or gap
that is holding them back -- not the persona's general caution, but the feature's specific
shortcoming. "This persona is risk-averse" is contextual. "The feature requires [X], which this
persona's workflow does not support yet" is causal.

If none of your primary personas scored below 3, say so plainly: "No adoption blockers."
Do not skip the check. A clean result still needs to be stated.

---

IS THE POSITIONING LEAKING?

Check your non-target personas. Did any score surprisingly high on usefulness or would-adopt?
Or does their rationale show confusion about whether this feature is meant for them? Name each
leak by ID and describe the feature-level cause: what about how the feature is described, named,
or scoped made this non-target persona think it might be for them?

If no leaks exist, say "No positioning leaks." explicitly. Do not skip the check.

---

WHO IS DELIGHTED?

Any score of 5 anywhere is worth pausing on. Group them by dimension: usefulness 5s, clarity 5s,
would-adopt 5s. For each, ask: what specific feature property produced this reaction? What would
you amplify in messaging, onboarding, or a sales conversation?

If there are no 5s, say "No delight signals." and move on.

---

WHAT DO THE NUMBERS SAY IN AGGREGATE?

Primary personas carry three times the weight of non-target; secondary carries twice as much.
Compute a weighted average for each dimension (usefulness, clarity, would-adopt) and an overall
composite on a 1-5 scale. Show how you weighted it -- state the weight per tier and count per tier.

Now look across all twelve causal rationales for a pattern. Is there a feature property that
consistently produces a particular reaction across a role cluster or tier? Is there a gap between
usefulness and would-adopt that holds for a specific segment -- and if so, what feature element
is causing it? Name the feature mechanism behind the pattern, not just the scoring distribution.
State what it means for the team building this feature. Generic observations ("scores vary") do
not qualify as a named pattern.

---

WHAT SHOULD CHANGE?

Address adoption blockers first. For each blocked primary persona, name the specific feature
property or gap to address and project the score movement:
"Fixing [feature X] for [ID] likely lifts primary W-Adopt by ~[delta], moving weighted
composite from [current] to approximately [current + effect]."

Then address positioning leaks. What about the feature's framing, scope, or naming is causing
non-target personas to be attracted or confused? Name the specific change.

Then amplify delight signals. What feature property is already landing? How do you lean into it?

---

Write the artifact to simulations/review/customers/{topic}-customers-{date}.md.
Frontmatter: skill: review-customers, topic, date, input, rationale_framing: causal.
```

---

## V-03: Inline Flags Isolated

Axis: Inline flagging mechanism ([BLOCKER]/[LEAK]/[DELIGHT]) extracted from V-05's 7-phase
scaffold and placed in a simpler prompt. Single-axis test of C-11.
Hypothesis: V-05's inline flag mechanism produces C-11 reliability without requiring 7 phases.
If so, C-11 is a lightweight addition orthogonal to structural complexity -- it can be
backported into any variation by adding ~5 lines to the SCORE section.

```
You are running /review:customers. Evaluate {{Topic}} using the 12-persona customer review.
Inline flags ([BLOCKER], [LEAK], [DELIGHT]) are appended to persona entries during scoring at
the point of discovery -- not surfaced in a post-hoc section only. This makes it structurally
impossible for a qualifying signal to be present in the scores but absent from the findings.

SETUP:
Read the input signal for {{Topic}} -- the relevant spec, proposal, or feature description.
Identify which personas are primary, secondary, and non-target for this feature.

STOCK PERSONAS:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

TIER ASSIGNMENT:
List all 12 personas with their tier before scoring begins:
  [ID] [Name] ([Role]) -- Tier: [primary / secondary / non-target]

Segmentation rationale: one sentence explaining the tier logic for this feature.

SCORE EACH PERSONA:
For each persona C-01 through C-12, write the entry in this format:

[C-NN] [Name] ([Role]) | Tier: [tier] | [inline flags: see rules below]
- Usefulness [1-5]: [score]
- Clarity [1-5]: [score]
- Would-Adopt [1-5]: [score]
- Rationale: 2-3 sentences grounded in the persona's role, typical workflow, or known pain
  points. Identify the specific feature property, design gap, or workflow fit/mismatch that
  produced these scores -- not just what this persona values in general.

Inline flag rules (apply to the header line, based on the scores just assigned):
  [BLOCKER]            -- primary tier AND Would-Adopt < 3
  [LEAK]               -- non-target tier AND (Useful >= 4 OR Would-Adopt >= 3)
  [DELIGHT: dimension] -- any score of 5 (e.g., [DELIGHT: clarity])
A persona can carry multiple flags. Apply every flag the entry qualifies for before moving
to the next persona. Flags go on the header line -- not in the rationale block. Do not defer
flags to the findings sections -- they must appear here, adjacent to the scores that triggered them.

Score all 12 personas before proceeding to any subsequent section.

WEIGHTED AGGREGATE:
Compute a weighted aggregate using: primary 3x, secondary 2x, non-target 1x.
State the weighting scheme and count per tier. Compute:
  weighted_usefulness  = sum(score x weight) / sum(weights)
  weighted_clarity     = sum(score x weight) / sum(weights)
  weighted_would_adopt = sum(score x weight) / sum(weights)
  weighted_composite   = (weighted_usefulness + weighted_clarity + weighted_would_adopt) / 3
Show the full calculation. Present results on a 1-5 scale.

ADOPTION BLOCKERS:
Collect every [BLOCKER] entry from the scoring section.
List: [ID] [Name] -- Would-Adopt: [score] -- [one sentence on what is blocking adoption].
If no [BLOCKER] entries exist: state "No adoption blockers."

POSITIONING LEAKS:
Collect every [LEAK] entry from the scoring section.
List: [ID] [Name] -- [signal: Useful or W-Adopt score] -- [what the positioning gap is].
If no [LEAK] entries exist: state "No positioning leaks."

DELIGHT SIGNALS:
Collect every [DELIGHT] entry from the scoring section. Group by dimension.
List: [ID] [Name] -- [dimension] -- [positioning or marketing implication].
If none: state "No delight signals."

CROSS-PERSONA PATTERNS:
Using the scoring data, identify at least one named cross-cutting pattern -- a tier cluster
where one dimension consistently lags another, a dimension divergence across role types, or
a gap between primary and secondary would-adopt scores. Name the pattern and state its
implication for feature design or messaging.
Generic observations ("scores vary") do not qualify.

AMEND:
Address findings in this order:
1. Adoption blockers -- for each [BLOCKER], state the specific change and project:
   "Resolving [ID] blocker by [change] likely lifts primary Would-Adopt by ~[delta],
   moving weighted composite from [current] to approximately [current + effect]."
2. Positioning leaks -- for each [LEAK], state the specific messaging or scope change and
   a directional estimate of its effect on non-target confusion or composite movement.
3. Delight amplification -- for each [DELIGHT], how to reinforce what is landing.

If no blockers: state "No adoption blockers to resolve."
If no leaks: state "No positioning leaks to close."
(C-10 auto-passes when both blockers and leaks are absent -- the score is clean by definition.)

Write artifact to simulations/review/customers/{topic}-customers-{date}.md.
Frontmatter: skill: review-customers, topic, date, input, inline_flags: true.
```

---

## V-04: Full C-11 + C-12 + C-13 Combined

Axis: Combined -- V-05 R1 phase structure (C-11 inline flags) + hybrid table+prose (C-12) +
causal rationale framing (C-13). All three new v2 criteria targeted together.
Hypothesis: Adding C-12 and C-13 to V-05's existing inline-flag and phase-gate architecture is
additive without breaking the 100/100 baseline. The table provides C-01/C-05; prose blocks
provide C-08/C-12/C-13; inline flags provide C-11; phase gates provide C-03/C-04 reliability.
This is the first variation to explicitly target all 13 criteria simultaneously.

```
You are running /review:customers. Scoring uses a two-layer hybrid format: a summary table
(completeness and auditability) followed by per-persona causal prose blocks (rationale depth).
Inline flags surface blockers and leaks during the prose phase. Explicit phase gates enforce
completeness at every boundary.

--- PHASE 1: DECLARE TIERS ---

Read the input signal for {{Topic}} -- the relevant spec, proposal, or feature description.

STOCK PERSONAS:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

Assign each persona a tier. State all 12 grouped by tier:
  Primary:    [list IDs and names]
  Secondary:  [list IDs and names]
  Non-target: [list IDs and names]

Segmentation rationale: one sentence explaining the tier logic for this feature.
Do not proceed to Phase 2 until all 12 are classified.

--- PHASE 2: SCORING TABLE ---

Build the scoring table. All 12 rows required. Tier labels must appear in every row.
This is the completeness layer -- do not write prose rationale in this table.

| ID   | Name            | Role        | Tier       | Useful | Clarity | W-Adopt |
|------|-----------------|-------------|------------|--------|---------|---------|
| C-01 | Maria Chen      | Maker       | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-02 | James Okafor    | Builder     | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-03 | Priya Nair      | Strategist  | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-04 | Tom Bergstrom   | Operator    | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-05 | Aisha Mensah    | Researcher  | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-06 | Carlos Reyes    | Designer    | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-07 | Lin Wei         | Analyst     | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-08 | Sophie Dubois   | Manager     | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-09 | Raj Patel       | Advocate    | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-10 | Yuki Tanaka     | Evaluator   | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-11 | Elena Vasquez   | Buyer       | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-12 | Frank Hoffmann  | Regulator   | [tier]     | [1-5]  | [1-5]   | [1-5]   |

All 12 rows must be complete before Phase 3 begins. Do not proceed until the table is full.

--- PHASE 3: CAUSAL PROSE BLOCKS ---

For each persona, write a causal prose block of 2-3 sentences. The table carries the scores;
the prose block is the rationale layer. Two rules:

1. Do not restate the scores. The prose block adds explanation, not repetition.
2. Name the specific feature property, design gap, or workflow fit/mismatch that drove the
   scores. The framing is: "The feature's [X] produced this reaction" -- not "This persona
   values [Y]." Rationale that only describes the persona's context or preferences without
   implicating a specific element of the feature is contextual, not causal. Causal rationale
   is required for every persona.

Apply inline flags to the persona header line (based on Phase 2 table scores):
  [BLOCKER]            -- primary tier, W-Adopt < 3
  [LEAK]               -- non-target tier, Useful >= 4 or W-Adopt >= 3
  [DELIGHT: dimension] -- any score of 5

Format per persona:

[C-NN] [Name] ([Role]) | [tier] | [inline flags if applicable]
[2-3 sentence causal prose rationale]

Write all 12. Do not proceed to Phase 4 until all 12 prose blocks are complete.

--- PHASE 4: DETECT ---

Review the inline flags from Phase 3. Each check requires an explicit result.
Blank or omitted = fail.

ADOPTION BLOCKERS:
Collect all [BLOCKER] entries.
List: [ID] [Name] -- W-Adopt: [score] -- [one sentence: which feature property/gap is blocking adoption].
If none: state "No adoption blockers."

POSITIONING LEAKS:
Collect all [LEAK] entries.
List: [ID] [Name] -- [signal: Useful or W-Adopt score] -- [what feature framing/scope caused this].
If none: state "No positioning leaks."

DELIGHT SIGNALS:
Collect all [DELIGHT] entries. Group by dimension.
List: [ID] [Name] -- [dimension] -- [positioning or marketing implication].
If none: state "No delight signals."

All three checks must have explicit results before proceeding to Phase 5.

--- PHASE 5: AGGREGATE ---

WEIGHTED SCORE:
Weights: primary 3x, secondary 2x, non-target 1x.
State the count and weight for each tier. Compute from the Phase 2 table:

  weighted_usefulness  = (sum primary useful x 3 + sum secondary useful x 2 +
                          sum nontarget useful x 1) / (3 x n_p + 2 x n_s + 1 x n_nt)
  weighted_clarity     = (same formula)
  weighted_would_adopt = (same formula)
  weighted_composite   = (weighted_usefulness + weighted_clarity + weighted_would_adopt) / 3

Show the full calculation. Present results on a 1-5 scale.

CROSS-PERSONA PATTERN:
Using the Phase 2 table and Phase 3 prose blocks, identify at least one named cross-cutting
pattern. The pattern must name a feature mechanism as its cause -- not just describe a scoring
distribution. For example: "The feature's [property] consistently suppresses clarity scores
across all non-technical personas" or "The absence of [X] creates a would-adopt ceiling for
secondary personas despite high usefulness." State the design or messaging implication.
Generic observations ("scores vary") do not qualify.

--- PHASE 6: AMEND ---

Address Phase 4 findings in this order:

1. ADOPTION BLOCKERS:
   For each [BLOCKER]:
   - Change: [the specific feature property or gap to address]
   - Projected impact: "Resolving [ID] blocker by [change] likely lifts primary W-Adopt
     by ~[delta], moving weighted composite from [current] to approximately [current + effect]."

2. POSITIONING LEAKS:
   For each [LEAK]:
   - Change: [specific feature framing, naming, or scope change]
   - Projected impact: directional estimate on non-target confusion or composite movement.

3. DELIGHT AMPLIFICATION:
   For each delight signal: what feature property is landing and how to reinforce it.

If Phase 4 found no blockers: state "No adoption blockers to resolve." Skip section 1.
If Phase 4 found no leaks: state "No positioning leaks to close." Skip section 2.
(C-10 auto-passes when both blockers and leaks are absent -- the score is clean by definition.)

Write artifact to simulations/review/customers/{topic}-customers-{date}.md.
Frontmatter: skill: review-customers, topic, date, input,
output_format: hybrid-table-prose, rationale_framing: causal, inline_flags: true,
phases: [declare, table, prose, detect, aggregate, amend].
```

---

## V-05: Causal Conversational with Hybrid Format

Axis: Phrasing register (conversational) + hybrid format (prose-first, table-second) + causal
rationale framing. Combined test of C-12 + C-13 in conversational register.
Hypothesis: Reasoning through each persona in prose before compiling the table (prose-first hybrid)
produces richer C-13 causal rationale than table-first formats. The model commits to a causal
explanation before committing to a structure, so the table becomes a compilation of genuine
reasoning rather than a scaffold that reasoning must fit into.

```
You are running /review:customers. Work through this as a customer advisory panel. The goal
is to understand what twelve different people would actually think, feel, and decide if they
encountered this feature today. The output is hybrid: reason through each persona in prose
first, then compile all results into a structured table. The prose comes before the table --
not after -- so the table reflects genuine reasoning, not a template being filled in.

---

WHAT ARE WE EVALUATING?

Read the spec or signal for {{Topic}}. Understand what the feature does, what problem it
solves, and what it asks of the people who use it. Before you invite anyone into the room,
make sure you know what you are showing them.

---

WHO IS THIS FEATURE FOR?

The panel has twelve seats:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

Decide: who is in the primary audience? Who is secondary? Who is not the target?
Write it out for all twelve before reasoning through any persona:
"C-01 Maria Chen -- primary," and so on.

---

WHAT DOES EACH PERSONA ACTUALLY ENCOUNTER?

Take each persona through the feature. For each one, score three dimensions from 1 to 5:

- Usefulness: Does this solve a real problem they actually have? (1 = irrelevant; 5 = solves
  something they struggle with today)
- Clarity: Do they understand what this is and what it does? (1 = confused; 5 = immediately
  obvious)
- Would-Adopt: Would they actually use this, given how they work right now? (1 = no chance;
  5 = adopts immediately without being asked)

After the three scores, write 2-3 sentences of causal explanation. The explanation must name
the specific feature property, design gap, or workflow fit/mismatch that produced these scores.
Not "this persona values reliability" -- but "the feature's lack of [X] means this persona
cannot integrate it into [specific workflow step], which is why would-adopt lags usefulness."
If a property of the feature is exactly right for this persona, name that property. If a gap
in the feature is the cause of a low score, name that gap. The explanation must implicate the
feature, not just describe the person.

Inline flags (append to the persona's header line during scoring):
  [BLOCKER]            -- primary tier, Would-Adopt < 3
  [LEAK]               -- non-target tier, Useful >= 4 or Would-Adopt >= 3
  [DELIGHT: dimension] -- any score of 5

Do this for all twelve.

---

COMPILE THE SCORING TABLE

After reasoning through all 12 personas in prose, compile the results into a summary table.
The scores in the table must match the scores from the prose reasoning above.

| ID   | Name            | Role        | Tier       | Useful | Clarity | W-Adopt |
|------|-----------------|-------------|------------|--------|---------|---------|
| C-01 | Maria Chen      | Maker       | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-02 | James Okafor    | Builder     | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-03 | Priya Nair      | Strategist  | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-04 | Tom Bergstrom   | Operator    | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-05 | Aisha Mensah    | Researcher  | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-06 | Carlos Reyes    | Designer    | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-07 | Lin Wei         | Analyst     | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-08 | Sophie Dubois   | Manager     | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-09 | Raj Patel       | Advocate    | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-10 | Yuki Tanaka     | Evaluator   | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-11 | Elena Vasquez   | Buyer       | [tier]     | [1-5]  | [1-5]   | [1-5]   |
| C-12 | Frank Hoffmann  | Regulator   | [tier]     | [1-5]  | [1-5]   | [1-5]   |

All 12 rows and all tier labels are required. The table is a summary of the reasoning
above -- not a scoring step.

---

IS ADOPTION BLOCKED?

Look at the would-adopt scores for your primary-audience personas. Did any score below 3?
If yes, name each blocker by ID, cite the score, and name the specific feature property or
gap that is holding them back -- not the persona's general hesitation, but the feature's
specific shortcoming. "This persona is risk-averse" is contextual. "The feature requires [X],
which this persona's workflow does not support yet" is causal.

If none of your primary personas scored below 3, say so plainly: "No adoption blockers."
Do not skip the check. A clean result still needs to be stated.

---

IS THE POSITIONING LEAKING?

Check your non-target personas. Did any score surprisingly high on usefulness or would-adopt?
Or does their causal rationale show confusion about whether this feature is meant for them?
Name each leak by ID and describe the feature-level cause: what about how the feature is
framed, named, or scoped made this non-target persona think it might be for them?

If no leaks: "No positioning leaks." Do not skip the check.

---

WHO IS DELIGHTED?

Any score of 5 anywhere is worth pausing on. Group by dimension: usefulness 5s, clarity 5s,
would-adopt 5s. For each, ask: what specific feature property produced this reaction? What
would you amplify in messaging, onboarding, or a press release?

If there are no 5s: "No delight signals."

---

WHAT DO THE NUMBERS SAY IN AGGREGATE?

Primary personas carry 3x the weight of non-target; secondary carries 2x. Compute a weighted
average for each dimension and an overall composite on a 1-5 scale. Show how you weighted it
-- state the weight per tier and count per tier.

Now look across all twelve causal rationales for a pattern that names a feature mechanism. Is
there a feature property that consistently produces a characteristic reaction across a role
cluster or tier? Is there a gap between usefulness and would-adopt that holds for a specific
segment -- and if so, what feature element is causing it? Name the feature mechanism behind
the pattern, not just the scoring distribution. State what it means for the team building this
feature. Generic observations ("scores vary") do not qualify.

---

WHAT SHOULD CHANGE?

Address adoption blockers first. For each blocked primary persona, name the specific feature
property or gap to address and project the score movement:
"Fixing [feature X] for [ID] likely lifts primary W-Adopt by ~[delta], moving weighted
composite from [current] to approximately [current + effect]."

Then address positioning leaks. What about the feature's framing, scope, or naming is causing
non-target personas to be attracted or confused? Name the specific change.

Then amplify delight signals. What feature property is already landing? How do you lean into it?

---

Write the artifact to simulations/review/customers/{topic}-customers-{date}.md.
Frontmatter: skill: review-customers, topic, date, input,
register: conversational, output_format: hybrid-prose-then-table, rationale_framing: causal.
```
