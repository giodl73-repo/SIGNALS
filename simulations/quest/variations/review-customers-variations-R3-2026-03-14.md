Written to `simulations/quest/variations/review-customers-variations-R3-2026-03-14.md`.

---

## review-customers R3 — 5 Variations

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Deferral prohibition (C-15, single) | Close-before-advance checkpoint makes deferral structurally impermissible without requiring prose-first ordering |
| V-02 | Sub-feature worked example (C-16, single) | Three-tier anti-pattern (contextual → feature-level → sub-feature-level) drives C-16 precision in 6+ personas where abstract rules plateau at Level 2 |
| V-03 | Prose-first table-locked-last (C-14, single) | A single ordering constraint ("compile after, not before") produces C-14 compliance without conversational register or multi-phase scaffolding |
| V-04 | C-14 + C-15 combined (formal) | Prose-first + close-before-advance form a reinforcing contract: macro-level ordering gap eliminated (C-14) and micro-level advance failure eliminated (C-15) |
| V-05 | Full R3 — C-14 + C-15 + C-16, conversational | Conversational register (R2's strongest depth predictor) with all three R3 mechanisms layered in; if it outperforms V-04 on C-16 at similar C-14/C-15 scores, register is the enabling variable |

---

**Key design decisions:**

**V-01 vs V-03** isolate the two orthogonal failure modes C-11 PARTIAL exposed in R2: V-01 targets the within-block advance failure (qualifies, advances, flag deferred); V-03 targets the structural phase gap (table before prose separates scores from flags at the macro level). If both pass independently, they're confirmed additive in V-04.

**V-02's three-tier example** is the mechanism V-02 used in R2 for C-13, extended one level deeper. The key addition is making the sub-feature level *visibly distinct* — not just "more specific" than feature-level — by showing that "the feature lacks X" and "the feature's [sub-feature Y] produces this reaction" are different categories, not a continuum.

**V-04 vs V-05**: the formal/conversational split. R2 showed register was the dominant variable for rationale depth. V-04 and V-05 have identical structural constraints (C-14 + C-15) and differ only in register and whether the C-16 example is present. This pair cleanly separates the register and example effects.

**Recommended scoring order:** V-03 (C-14 isolation) → V-01 (C-15 isolation) → V-02 (C-16 isolation) → V-04 (C-14+C-15 combined, no example) → V-05 (full R3).
lation) -> V-01 (C-15 isolation) -> V-02
(C-16 isolation) -> V-04 (C-14+C-15 combined) -> V-05 (full R3).

---

## V-01: Deferral Prohibition

Axis: Lifecycle emphasis -- per-persona close-before-advance checkpoint makes it
structurally impermissible to advance past a persona without closing all applicable flags.
Single-axis test of C-15.
Hypothesis: The deferral failure mode (score qualifies for BLOCKER/LEAK, advance to next
persona, surface flag post-hoc) is prevented by an explicit per-persona checkpoint that
must be satisfied before the next persona header is written. This mechanism operates
independently of output ordering -- it works in a table-first format where C-14 would fail,
proving C-15 is orthogonal to C-14.

```
You are running /review:customers. Evaluate {{Topic}} using the 12-persona customer review.
Inline flags ([BLOCKER], [LEAK], [DELIGHT]) are applied at the point of scoring, inside
each persona's entry. Deferral is not permitted: every qualifying persona block must carry
its inline flags before the output advances to the next persona.

SETUP:
Read the input signal for {{Topic}} -- the relevant spec, proposal, or feature description.

STOCK PERSONAS:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

TIER ASSIGNMENT:
Assign all 12 personas to a tier before scoring. List them explicitly:
  Primary:    [IDs and names]
  Secondary:  [IDs and names]
  Non-target: [IDs and names]

Segmentation rationale: one sentence explaining the tier logic for this feature.

SCORE EACH PERSONA:
For each persona C-01 through C-12, write the entry in this exact sequence:

  Step 1 -- Header line (tier only, no flags yet):
  [C-NN] [Name] ([Role]) | Tier: [tier]

  Step 2 -- Three scores:
  - Usefulness [1-5]: [score]
  - Clarity [1-5]: [score]
  - Would-Adopt [1-5]: [score]

  Step 3 -- Rationale (2-3 sentences):
  Explain what about the feature produced these scores. Name the specific feature property,
  design gap, or workflow fit/mismatch as the driver. The framing is "the feature's [X]
  produced this reaction" -- not "this persona values [Y]."

  Step 4 -- CLOSE-BEFORE-ADVANCE CHECKPOINT (mandatory for every persona):
  Before writing the next persona's header line, answer these three checks:

    CHECK A: Is this persona in the primary tier AND Would-Adopt < 3?
    If YES: add [BLOCKER] to this persona's header line now. If NO: proceed.

    CHECK B: Is this persona in the non-target tier AND (Useful >= 4 OR Would-Adopt >= 3)?
    If YES: add [LEAK] to this persona's header line now. If NO: proceed.

    CHECK C: Does any score equal 5?
    If YES: add [DELIGHT: dimension] to this persona's header line for each 5. If NO: proceed.

  Only after completing all four steps may you write the next persona's header line.
  This checkpoint is not optional. A persona block that ends at Step 3 without Step 4
  having been evaluated is structurally incomplete.

After all 12 persona entries are written:

SCORING TABLE:
Compile the scoring table from the persona entries above.

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

WEIGHTED AGGREGATE:
Weights: primary 3x, secondary 2x, non-target 1x.
State the count and weight for each tier. Compute:
  weighted_usefulness  = sum(score x weight) / sum(weights)
  weighted_clarity     = sum(score x weight) / sum(weights)
  weighted_would_adopt = sum(score x weight) / sum(weights)
  weighted_composite   = (weighted_usefulness + weighted_clarity + weighted_would_adopt) / 3
Show the full calculation. Present results on a 1-5 scale.

ADOPTION BLOCKERS:
Collect every [BLOCKER] flag from the persona entries.
List: [ID] [Name] -- Would-Adopt: [score] -- [one sentence: which feature property/gap is blocking adoption].
If none: state "No adoption blockers."

POSITIONING LEAKS:
Collect every [LEAK] flag from the persona entries.
List: [ID] [Name] -- [signal: Useful or W-Adopt score] -- [what feature framing/scope caused this].
If none: state "No positioning leaks."

DELIGHT SIGNALS:
Collect every [DELIGHT] flag from the persona entries. Group by dimension.
List: [ID] [Name] -- [dimension] -- [positioning or marketing implication].
If none: state "No delight signals."

CROSS-PERSONA PATTERNS:
Identify at least one named cross-cutting pattern with a feature mechanism as its cause.
Name the pattern and state its implication for feature design or messaging.
Generic observations ("scores vary") do not qualify.

AMEND:
Address findings in this order:
1. Adoption blockers -- for each [BLOCKER], state the specific change and project:
   "Resolving [ID] blocker by [change] likely lifts primary Would-Adopt by ~[delta],
   moving weighted composite from [current] to approximately [current + effect]."
2. Positioning leaks -- for each [LEAK], state the specific messaging or scope change
   and a directional estimate of its effect on non-target confusion or composite movement.
3. Delight amplification -- for each [DELIGHT], how to reinforce what is landing.

If no blockers: state "No adoption blockers to resolve."
If no leaks: state "No positioning leaks to close."
(C-10 auto-passes when both blockers and leaks are absent -- the score is clean by definition.)

Write artifact to simulations/review/customers/{topic}-customers-{date}.md.
Frontmatter: skill: review-customers, topic, date, input,
c15_mechanism: close-before-advance-checkpoint, inline_flags: true.
```

---

## V-02: Sub-Feature Worked Example

Axis: Phrasing register -- three-tier anti-pattern example (contextual → feature-level →
sub-feature-level) shows the model what C-16-qualifying rationale looks like by showing
what it does not look like. Single-axis test of C-16.
Hypothesis: Showing all three levels of specificity in a worked example drives the model
to sub-feature-level rationale in 6+ of 12 personas. An abstract rule ("be specific")
produces feature-level framing (C-13 passes). A worked example that makes the sub-feature
level visible as a distinct, named category produces sub-feature-level framing (C-16 passes).

```
You are running /review:customers. Evaluate {{Topic}} using the 12-persona customer review.
Persona rationales must reach sub-feature specificity -- name the exact capability, threshold,
design decision, or workflow step that produced the score, not the feature generically.

SETUP:
Read the input signal for {{Topic}} -- the relevant spec, proposal, or feature description.

STOCK PERSONAS:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

TIER ASSIGNMENT:
Assign all 12 personas to a tier before scoring:
  Primary:    [IDs and names]
  Secondary:  [IDs and names]
  Non-target: [IDs and names]

Segmentation rationale: one sentence.

CAUSAL PRECISION -- THREE LEVELS:

Every persona's rationale must reach Level 3. The three levels are:

LEVEL 1 -- Contextual (fails C-13 and C-16):
"This persona values documentation and audit trails, so the feature's complexity makes them
cautious about adopting it."
Problem: describes the persona's preferences. No feature property is named.
The feature is mentioned generically ("complexity") but nothing specific is implicated.

LEVEL 2 -- Feature-level (passes C-13, fails C-16):
"The feature lacks an audit log, which this persona requires for compliance workflows."
Better: names a feature gap (no audit log) as the causal driver. C-13 passes.
Still not enough: the gap is stated at feature level. "Lacks an audit log" implicates the
feature as a whole but does not name which specific design decision, capability boundary,
or configuration constraint produces this absence. Not directly actionable.

LEVEL 3 -- Sub-feature level (passes C-13 and C-16):
"The feature's event stream records only completion events with no intermediate state
transitions -- the schema has no timestamp_start or status_change fields -- which means
the audit trail this persona needs for compliance sign-off cannot be reconstructed from
the output. The specific gap is the event schema, not the feature's approach overall."
Correct: names the sub-feature property (event schema design, missing fields), the specific
constraint (no timestamp_start or status_change), and the exact impact. Directly actionable
as an amendment target (add fields, or offer a verbose event mode).

Write Level 3 rationale for every persona. If you cannot name a specific capability,
threshold, design decision, or workflow step as the mechanism, your rationale is at Level 2
at best. Keep asking "which part of the feature, specifically, produced this reaction?"
until you can name it.

SCORE EACH PERSONA:
For each persona C-01 through C-12:

[C-NN] [Name] ([Role]) | Tier: [tier] | [inline flags: see rules below]
- Usefulness [1-5]: [score]
- Clarity [1-5]: [score]
- Would-Adopt [1-5]: [score]
- Rationale: 2-3 sentences at Level 3 specificity.

Inline flag rules (apply to the header line, based on the scores just assigned):
  [BLOCKER]            -- primary tier AND Would-Adopt < 3
  [LEAK]               -- non-target tier AND (Useful >= 4 OR Would-Adopt >= 3)
  [DELIGHT: dimension] -- any score of 5
Apply every flag the entry qualifies for. Do not defer flags to a later section.

Score all 12 personas before proceeding.

SCORING TABLE:
Compile the scoring table:

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

WEIGHTED AGGREGATE:
Weights: primary 3x, secondary 2x, non-target 1x.
State the count and weight per tier. Compute weighted averages for each dimension and a
composite on a 1-5 scale. Show the full calculation.

ADOPTION BLOCKERS:
Collect all [BLOCKER] entries. For each:
[ID] [Name] -- Would-Adopt: [score] -- [the sub-feature property blocking adoption].
If none: "No adoption blockers."

POSITIONING LEAKS:
Collect all [LEAK] entries. For each:
[ID] [Name] -- [signal: Useful or W-Adopt score] -- [the sub-feature or framing element causing the leak].
If none: "No positioning leaks."

DELIGHT SIGNALS:
Collect all [DELIGHT] entries. Group by dimension.
[ID] [Name] -- [dimension] -- [the sub-feature property that produced this delight; marketing implication].
If none: "No delight signals."

CROSS-PERSONA PATTERNS:
Identify at least one named cross-cutting pattern at sub-feature specificity. The pattern
must name a specific feature property, capability boundary, or design decision as its
cause -- not a general feature observation. State the design or messaging implication.

AMEND:
Address findings in this order:
1. Adoption blockers -- for each [BLOCKER], name the sub-feature amendment and project:
   "Resolving [ID] blocker by [specific sub-feature change] likely lifts primary Would-Adopt
   by ~[delta], moving weighted composite from [current] to approximately [current + effect]."
2. Positioning leaks -- for each [LEAK], name the specific framing, naming, or scope
   change and a directional estimate.
3. Delight amplification -- for each [DELIGHT], what sub-feature property is landing and
   how to reinforce it.

If no blockers: "No adoption blockers to resolve."
If no leaks: "No positioning leaks to close."

Write artifact to simulations/review/customers/{topic}-customers-{date}.md.
Frontmatter: skill: review-customers, topic, date, input,
causal_precision: sub-feature-level, c16_mechanism: three-tier-worked-example.
```

---

## V-03: Prose-First Table-Locked-Last

Axis: Output format -- a single structural rule locks the scoring table to appear only
after all 12 prose blocks are complete. Single-axis test of C-14 without conversational
register or phase scaffolding.
Hypothesis: The C-14 failure mode (table-first creates a structural phase gap between
scores and flags) is prevented by a single explicit rule ("the table is the last structured
element you write") without requiring conversational phrasing or a multi-phase scaffold.
If V-03 produces C-14 compliance in a formal-register prompt, the ordering constraint
is a lightweight addition orthogonal to register.

```
You are running /review:customers. Evaluate {{Topic}} using the 12-persona customer review.

TABLE ORDERING RULE -- ENFORCED:
The scoring table is compiled after all 12 persona prose blocks are written -- not before.
Do not build a table first and fill in prose later. Reason through each persona, assign
scores as part of that reasoning, and compile the scores into the table only after all
12 personas are complete. The table is a verified artifact of finished reasoning, not a
preliminary scaffold. A table appearing before any per-persona prose block is the wrong
output order.

SETUP:
Read the input signal for {{Topic}} -- the relevant spec, proposal, or feature description.

STOCK PERSONAS:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

TIER ASSIGNMENT:
Assign all 12 personas to a tier. Write the full list before the first persona block:
  Primary:    [IDs and names]
  Secondary:  [IDs and names]
  Non-target: [IDs and names]

Segmentation rationale: one sentence.

PERSONA BLOCKS (all 12 before the table):
For each persona C-01 through C-12, write a prose block in this format:

[C-NN] [Name] ([Role]) | Tier: [tier] | [inline flags if applicable]
- Usefulness [1-5]: [score]
- Clarity [1-5]: [score]
- Would-Adopt [1-5]: [score]
- Rationale: 2-3 sentences. Identify the specific feature property, design gap, or workflow
  fit/mismatch that produced these scores. The framing is "the feature's [X] produced this
  reaction" -- not "this persona values [Y]."

Inline flag rules (apply to the header line at the time of scoring):
  [BLOCKER]            -- primary tier AND Would-Adopt < 3
  [LEAK]               -- non-target tier AND (Useful >= 4 OR Would-Adopt >= 3)
  [DELIGHT: dimension] -- any score of 5
Apply all applicable flags to each persona's header line at the time you score that persona.
Do not defer flags. Do not proceed to the next persona without applying all flags this entry
qualifies for.

Write all 12 persona blocks. After the last persona block is complete, proceed to the table.

SCORING TABLE (after all 12 prose blocks):
Compile scores from the persona blocks above into this table. Every row required.

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

Scores in this table must match scores from the persona blocks above.

WEIGHTED AGGREGATE:
Weights: primary 3x, secondary 2x, non-target 1x.
State the count and weight for each tier. Compute:
  weighted_usefulness  = sum(score x weight) / sum(weights)
  weighted_clarity     = sum(score x weight) / sum(weights)
  weighted_would_adopt = sum(score x weight) / sum(weights)
  weighted_composite   = (weighted_usefulness + weighted_clarity + weighted_would_adopt) / 3
Show the full calculation. Present results on a 1-5 scale.

ADOPTION BLOCKERS:
Collect all [BLOCKER] entries from the persona blocks.
List: [ID] [Name] -- Would-Adopt: [score] -- [one sentence: which feature property/gap is blocking adoption].
If none: "No adoption blockers."

POSITIONING LEAKS:
Collect all [LEAK] entries from the persona blocks.
List: [ID] [Name] -- [signal: Useful or W-Adopt score] -- [what feature framing/scope caused this].
If none: "No positioning leaks."

DELIGHT SIGNALS:
Collect all [DELIGHT] entries from the persona blocks. Group by dimension.
List: [ID] [Name] -- [dimension] -- [positioning or marketing implication].
If none: "No delight signals."

CROSS-PERSONA PATTERNS:
Identify at least one named cross-cutting pattern that names a feature mechanism as its
cause. State the design or messaging implication. Generic observations do not qualify.

AMEND:
Address findings in this order:
1. Adoption blockers -- for each [BLOCKER], state the specific change and project the
   score impact: "Resolving [ID] blocker by [change] likely lifts primary Would-Adopt by
   ~[delta], moving weighted composite from [current] to approximately [current + effect]."
2. Positioning leaks -- for each [LEAK], state the specific framing or scope change and
   a directional estimate of its effect on non-target confusion or composite movement.
3. Delight amplification -- for each [DELIGHT], how to reinforce what is landing.

If no blockers: "No adoption blockers to resolve."
If no leaks: "No positioning leaks to close."

Write artifact to simulations/review/customers/{topic}-customers-{date}.md.
Frontmatter: skill: review-customers, topic, date, input,
output_format: prose-first-then-table, c14_mechanism: table-locked-last.
```

---

## V-04: C-14 + C-15 Combined (Formal)

Axis: Prose-first ordering (C-14) combined with per-persona deferral prohibition (C-15),
in formal phrasing register. Combined test without sub-feature specificity (C-16).
Hypothesis: These two constraints form a reinforcing structural contract. C-14 eliminates
the macro-level phase gap (table before prose creates separation between where scores live
and where flags land). C-15 eliminates the micro-level advance failure (moving to the
next persona without closing the current block's flags). Together they close both
pathways to C-11 PARTIAL. Formal register isolates whether the constraint combination
or conversational register is the primary driver when compared against V-05.

```
You are running /review:customers. Evaluate {{Topic}} using the 12-persona customer review.
Two structural rules govern this output. Both are mandatory.

STRUCTURAL RULE 1 -- PROSE-FIRST ORDER (C-14):
All 12 persona prose blocks appear before the scoring table. The table is compiled from
finished reasoning -- it is not a preliminary scaffold. Do not write any row of the scoring
table until all 12 persona prose blocks are complete. A table appearing before any
per-persona prose block is the wrong output order.

STRUCTURAL RULE 2 -- CLOSE-BEFORE-ADVANCE (C-15):
Each persona block must carry all applicable inline flags before the output advances to
the next persona. The failure mode is: score a primary persona Would-Adopt: 2, write the
rationale, then move on -- intending to surface the BLOCKER flag in a later section. That
sequence is not permitted. Every persona block that qualifies for a flag must have that
flag on its header line before the next persona's header line is written. A flag that
appears only in a post-hoc DETECT or FINDINGS section, and not in the persona block itself,
is deferred -- which is a structural failure, not a style choice.

SETUP:
Read the input signal for {{Topic}} -- the relevant spec, proposal, or feature description.

STOCK PERSONAS:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

TIER ASSIGNMENT:
Assign all 12 personas to a tier before writing any persona block:
  Primary:    [IDs and names]
  Secondary:  [IDs and names]
  Non-target: [IDs and names]

Segmentation rationale: one sentence explaining the tier logic for this feature.

PERSONA BLOCKS (12 complete blocks before the table):
For each persona C-01 through C-12, follow this exact sequence:

  Step 1 -- Header line (tier label; flags added in Step 4):
  [C-NN] [Name] ([Role]) | Tier: [tier]

  Step 2 -- Scores:
  - Usefulness [1-5]: [score]
  - Clarity [1-5]: [score]
  - Would-Adopt [1-5]: [score]

  Step 3 -- Rationale (2-3 sentences):
  Name the specific feature property, design gap, or workflow fit/mismatch that produced
  these scores. The framing is "the feature's [X] produced this reaction" -- not "this
  persona values [Y]." Rationale that only describes the persona's context without
  implicating a specific feature element is not sufficient.

  Step 4 -- Flag resolution (before advancing):
  Evaluate all three flag conditions against the scores just written:

    CHECK A: primary tier AND Would-Adopt < 3?
    → YES: add [BLOCKER] to this persona's header line. NO: continue.

    CHECK B: non-target tier AND (Useful >= 4 OR Would-Adopt >= 3)?
    → YES: add [LEAK] to this persona's header line. NO: continue.

    CHECK C: any score equal to 5?
    → YES: add [DELIGHT: dimension] to this persona's header line for each qualifying
      dimension. NO: continue.

  This step is mandatory. You may not write the next persona's header line until Step 4
  is complete for the current persona.

Write all 12 persona blocks before writing any part of the scoring table.

SCORING TABLE (after all 12 persona blocks):
Compile scores from the persona blocks. All 12 rows and all tier labels required.

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

WEIGHTED AGGREGATE:
Weights: primary 3x, secondary 2x, non-target 1x.
State the count and weight per tier. Compute:
  weighted_usefulness  = sum(score x weight) / sum(weights)
  weighted_clarity     = sum(score x weight) / sum(weights)
  weighted_would_adopt = sum(score x weight) / sum(weights)
  weighted_composite   = (weighted_usefulness + weighted_clarity + weighted_would_adopt) / 3
Show the full calculation. Present results on a 1-5 scale.

ADOPTION BLOCKERS:
Collect all [BLOCKER] entries from the persona blocks.
List: [ID] [Name] -- Would-Adopt: [score] -- [one sentence: which feature property is blocking adoption].
If none: "No adoption blockers."

POSITIONING LEAKS:
Collect all [LEAK] entries from the persona blocks.
List: [ID] [Name] -- [signal score] -- [what feature framing/scope caused this].
If none: "No positioning leaks."

DELIGHT SIGNALS:
Collect all [DELIGHT] entries from the persona blocks. Group by dimension.
List: [ID] [Name] -- [dimension] -- [positioning or marketing implication].
If none: "No delight signals."

CROSS-PERSONA PATTERNS:
Identify at least one named cross-cutting pattern that names a feature mechanism as its
cause. State the design or messaging implication. Generic observations do not qualify.

AMEND:
Address findings in this order:
1. Adoption blockers -- for each [BLOCKER], state the specific change and project:
   "Resolving [ID] blocker by [change] likely lifts primary Would-Adopt by ~[delta],
   moving weighted composite from [current] to approximately [current + effect]."
2. Positioning leaks -- for each [LEAK], state the specific framing or scope change and
   a directional estimate.
3. Delight amplification -- for each [DELIGHT], what feature property is landing and
   how to reinforce it.

If no blockers: "No adoption blockers to resolve."
If no leaks: "No positioning leaks to close."

Write artifact to simulations/review/customers/{topic}-customers-{date}.md.
Frontmatter: skill: review-customers, topic, date, input,
output_format: prose-first-then-table, c14_mechanism: table-locked-last,
c15_mechanism: close-before-advance-checkpoint, inline_flags: true.
```

---

## V-05: Full R3 -- C-14 + C-15 + C-16 in Conversational Register

Axis: All three R3 criteria (C-14 prose-first, C-15 deferral prohibition, C-16 sub-feature
worked example) embedded in conversational phrasing register. Full R3 target.
Hypothesis: Conversational register was R2's strongest predictor of rationale depth (V-05
produced the best C-13 results). Adding C-15's deferral prohibition and C-16's three-tier
worked example to the conversational+prose-first frame from R2's V-05 layers all three R3
targets without degrading the R2 baseline. If V-05 R3 outperforms V-04 on C-16 specificity
at comparable C-14/C-15 scores, conversational framing is the enabling variable for depth.

```
You are running /review:customers. Work through this as a customer advisory panel. The goal
is to understand what twelve different people would actually think, feel, and decide if they
encountered this feature today. The output structure matters: reason through each persona
in prose first, then compile all results into a scoring table afterward. The prose comes
before the table -- always -- because the table should reflect genuine reasoning, not a
scaffold that reasoning fits into after the fact.

---

WHAT ARE WE EVALUATING?

Read the spec or signal for {{Topic}}. Understand what the feature does, what problem it
solves, and what it asks of the people who would use it. Before you invite anyone into the
room, make sure you know what you are showing them.

---

WHO IS THIS FEATURE FOR?

The panel has twelve seats:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

Decide: who is in the primary audience? Who is secondary? Who is not the target?
Write it out for all twelve before reasoning through any individual:
"C-01 Maria Chen -- primary," and so on.

---

WHAT DOES EACH PERSONA ACTUALLY ENCOUNTER?

Take each person through the feature one at a time. For each one:

Score three dimensions from 1 to 5:
- Usefulness: Does this solve a real problem they actually have? (1 = irrelevant to their
  work; 5 = solves something they struggle with today)
- Clarity: Do they understand what this is and what it does? (1 = confused about the basic
  proposition; 5 = immediately obvious)
- Would-Adopt: Would they actually use this, given how they work right now? (1 = no chance;
  5 = adopts immediately without being asked)

Then write 2-3 sentences explaining what happened. The explanation must name the specific
sub-feature property that drove the scores -- not the feature generically, and not the
persona's preferences. Here is what the three levels of explanation look like:

  LEVEL 1 -- Not sufficient (no feature named):
  "This persona values reliability and documentation, so the feature's opaque approach
  makes them hesitant."
  Why it fails: describes the person, not the feature.

  LEVEL 2 -- Better but not enough (feature named, not sub-feature):
  "The feature lacks offline support, which this persona needs for field deployments."
  Why it fails: names a feature gap but doesn't name which specific design decision, limit,
  or capability boundary creates it. "Lacks offline support" implicates the feature as
  a whole -- it doesn't give the team an amendment target.

  LEVEL 3 -- What's required (sub-feature mechanism named):
  "The feature's sync step requires an active write connection to the central registry --
  there is no local-cache mode and no queue-and-flush option -- which means this persona
  cannot use it in the field environments where their work actually happens. The blocker is
  the sync architecture, not the feature's overall approach, and it has a specific fix:
  a local-first cache with background sync."
  Why it works: names the sub-feature (sync step design), the specific constraint (no
  local-cache or queue-and-flush), the impact, and the amendment target. Directly actionable.

Write Level 3 for every persona.

After the three scores and the explanation, check flags before moving on to the next person.
This check is not optional and cannot be deferred:

  Is this person in the primary tier AND Would-Adopt < 3?
  If yes: add [BLOCKER] to their header line now, before writing the next person's name.

  Is this person in the non-target tier AND (Useful >= 4 OR Would-Adopt >= 3)?
  If yes: add [LEAK] to their header line now, before writing the next person's name.

  Does any score equal 5?
  If yes: add [DELIGHT: dimension] to their header line now, before writing the next person's name.

You may not write the next person's name until the current person's flags are resolved.
A flag that only appears in a summary section later -- and not in the entry where the score
was assigned -- was deferred, not applied. Deferral is not the same as inline flagging.

Do this for all twelve. Write all twelve prose entries before writing any part of the table.

---

COMPILE THE SCORING TABLE

After reasoning through all 12 personas in prose, compile the results into a summary table.
Every row is required. Scores must match the prose entries above.

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

All 12 rows and all tier labels required. The table is a summary of reasoning already done
-- not a scoring step.

---

IS ADOPTION BLOCKED?

Look at the would-adopt scores for your primary-audience personas. Did any score below 3?
If yes, name each blocker by ID, cite the score, and name the specific sub-feature property
holding them back. Not "this persona is cautious" -- but "the feature's [specific design
decision or capability boundary] means [specific workflow consequence]." That is the causal
statement that makes the blocker actionable.

If none scored below 3: "No adoption blockers." Do not skip the check.

---

IS THE POSITIONING LEAKING?

Check your non-target personas. Did any score surprisingly high on usefulness or would-adopt?
Or does their explanation show confusion about whether this feature is meant for them?
Name each leak by ID and describe the sub-feature or framing element causing it: what
specific property of how the feature is named, described, or scoped made this non-target
persona think it might be for them?

If no leaks: "No positioning leaks." Do not skip the check.

---

WHO IS DELIGHTED?

Any score of 5 anywhere is worth pausing on. Group by dimension: usefulness 5s, clarity 5s,
would-adopt 5s. For each, ask: which sub-feature property produced this reaction? What would
you amplify in messaging, onboarding, or positioning?

If there are no 5s: "No delight signals."

---

WHAT DO THE NUMBERS SAY IN AGGREGATE?

Primary personas carry 3x the weight of non-target; secondary carries 2x. Compute weighted
averages for each dimension and an overall composite on a 1-5 scale. Show how you weighted
it -- state the weight per tier and count per tier.

Now look across all twelve explanations for a pattern that names a sub-feature mechanism.
Is there a specific design decision or capability constraint that consistently produces a
characteristic reaction across a role cluster or tier? Is there a gap between usefulness and
would-adopt that holds for a specific segment -- and if so, which sub-feature property is
causing it? Name the sub-feature mechanism behind the pattern, state what it implies for the
team, and explain how it differs from just observing the scoring distribution.
Generic observations ("scores vary") do not qualify.

---

WHAT SHOULD CHANGE?

Address adoption blockers first. For each blocked primary persona, name the specific
sub-feature change to make and project the score movement:
"Fixing [specific sub-feature property] for [ID] likely lifts primary Would-Adopt by ~[delta],
moving weighted composite from [current] to approximately [current + effect]."

Then address positioning leaks. What specific sub-feature or framing element is causing
non-target personas to be attracted or confused? Name the change.

Then amplify delight signals. Which sub-feature property is already landing? How do you
lean into it in messaging or onboarding?

---

Write the artifact to simulations/review/customers/{topic}-customers-{date}.md.
Frontmatter: skill: review-customers, topic, date, input,
register: conversational, output_format: prose-first-then-table,
c14_mechanism: table-locked-last, c15_mechanism: close-before-advance,
c16_mechanism: three-tier-worked-example, causal_precision: sub-feature-level.
```
