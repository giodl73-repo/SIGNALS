Written to `simulations/quest/variations/review-customers-variations-R4-2026-03-14.md`.

---

## review-customers R4 -- 5 Variations

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Amendment scaffolding (C-17, single) | Structured per-blocker/per-leak template forcing sub-feature property naming closes the rationale/amend parity gap without touching persona block behavior |
| V-02 | Pattern synthesis worked example (C-18, single) | Feature-level vs sub-feature-level contrast example in CROSS-PERSONA section drives sub-feature resolution into pattern statements the same way R3 V-02 drove it into per-persona rationale |
| V-03 | Three-tier blocker traversal explicit labeling (C-19, single) | Requiring at least one blocker with explicit L1/L2/L3 labels tests chain completeness vs terminological compliance -- labels force traversal; abstract instructions allow skip-bridging |
| V-04 | C-17 + C-18 combined (formal) | Disjoint sections (amend vs synthesis) -- combining holds all post-scoring sections to sub-feature resolution without mutual interference |
| V-05 | Full R4 -- C-17 + C-18 + C-19 in conversational register | All three R4 mechanisms target post-persona sections; they layer onto R3's conversational per-persona baseline without displacing it |

---

**Key design decisions:**

**V-01 vs V-02 vs V-03** each isolate one R4 failure mode in a different output section. V-01 tests the amend section gap (C-17): rationale reaches sub-feature but the fix names only the feature. V-02 tests the synthesis section gap (C-18): per-persona sub-feature rationale does not automatically propagate into cross-persona pattern statements. V-03 tests chain completeness in the blocker section (C-19): naming L3 is necessary but not sufficient without L1 stakes and L2 bridge.

**V-04 vs V-05**: V-04 in formal register tests whether C-17/C-18 are achievable without conversational framing. V-05 adds C-19 and conversational register. If V-05 outperforms V-04 on C-19 at comparable C-17/C-18 scores, conversational framing is the enabling variable for causal chain completeness in blocker rationales.

**Recommended scoring order:** V-03 (C-19 isolation) → V-02 (C-18 isolation) → V-01 (C-17 isolation) → V-04 (C-17+C-18 combined) → V-05 (full R4 conversational).
nal framing. V-05 adds C-19 and conversational register. If V-05 outperforms V-04 on C-19 at comparable C-17/C-18 scores, conversational framing is the enabling variable for causal chain completeness -- the same role it played for per-persona depth in R3.

**Recommended scoring order:** V-03 (C-19 isolation) -> V-02 (C-18 isolation) -> V-01 (C-17 isolation) -> V-04 (C-17+C-18 combined) -> V-05 (full R4 conversational).

---

## V-01: Amendment Scaffolding

Axis: Lifecycle emphasis -- the AMEND section gets a per-item structured template that requires
naming a sub-feature property as the amendment target. Single-axis test of C-17.
Hypothesis: A template that forces the model to complete "the sub-feature to change is [X]"
for every blocker and leak prevents generic "improve the feature for [persona]" recommendations.
If V-01 passes C-17 while R3 V-04's C-14/C-15/C-16 performance holds, the amendment template
is confirmed orthogonal -- the lowest-friction addition that closes the scoring/amend parity gap.

```
You are running /review:customers. Evaluate {{Topic}} using the 12-persona customer review.
Two structural rules govern output order. Both are mandatory.

STRUCTURAL RULE 1 -- PROSE-FIRST ORDER:
All 12 persona prose blocks appear before the scoring table. Do not write any table row until
all 12 persona blocks are complete.

STRUCTURAL RULE 2 -- CLOSE-BEFORE-ADVANCE:
Each persona block carries all applicable inline flags before the output advances to the next
persona. Do not defer flags to a later section. A flag that appears only in a summary section
and not in the persona block where the score was assigned is deferred -- a structural failure.

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

PERSONA BLOCKS (all 12 before the table):
For each persona C-01 through C-12, follow this sequence:

  Step 1 -- Header line (tier label; flags added in Step 4):
  [C-NN] [Name] ([Role]) | Tier: [tier]

  Step 2 -- Scores:
  - Usefulness [1-5]: [score]
  - Clarity [1-5]: [score]
  - Would-Adopt [1-5]: [score]

  Step 3 -- Rationale (2-3 sentences):
  Name the specific feature property, design gap, or workflow mismatch that produced these
  scores. The framing is "the feature's [X] produced this reaction" -- not "this persona
  values [Y]." Name the sub-feature property where possible: the specific capability, threshold,
  design decision, or workflow step -- not the feature generically.

  Step 4 -- Flag resolution (mandatory before advancing):
    CHECK A: primary tier AND Would-Adopt < 3?
    -> YES: add [BLOCKER] to this persona's header line. NO: continue.

    CHECK B: non-target tier AND (Useful >= 4 OR Would-Adopt >= 3)?
    -> YES: add [LEAK] to this persona's header line. NO: continue.

    CHECK C: any score equal to 5?
    -> YES: add [DELIGHT: dimension] to header line for each qualifying dimension. NO: continue.

  You may not write the next persona's header line until Step 4 is complete.

Write all 12 persona blocks before writing any part of the scoring table.

SCORING TABLE (after all 12 persona blocks):
Compile scores from the persona blocks. All 12 rows and tier labels required.

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
List: [ID] [Name] -- Would-Adopt: [score] -- [feature property blocking adoption].
If none: "No adoption blockers."

POSITIONING LEAKS:
Collect all [LEAK] entries from the persona blocks.
List: [ID] [Name] -- [signal score] -- [feature framing or scope element causing leak].
If none: "No positioning leaks."

DELIGHT SIGNALS:
Collect all [DELIGHT] entries from the persona blocks. Group by dimension.
List: [ID] [Name] -- [dimension] -- [positioning or marketing implication].
If none: "No delight signals."

CROSS-PERSONA PATTERNS:
Identify at least one named cross-cutting pattern that names a feature mechanism as its cause.
State the design or messaging implication. Generic observations ("scores vary") do not qualify.

AMEND:
Address findings in this order: blockers first, then leaks, then delight amplification.

For each [BLOCKER], use this template exactly:

  Blocker: [ID] [Name]
  Sub-feature to change: [name the specific capability, threshold, design decision, or workflow
    step that is the amendment target -- not the feature generically]
  Change description: [what specifically changes about that sub-feature]
  Projected impact: "Resolving [ID] blocker by [change] likely lifts primary Would-Adopt by
    ~[delta], moving weighted composite from [current] to approximately [current + effect]."

The sub-feature to change must be the same sub-feature property named in the persona's rationale
or a more refined decomposition of it. A generic target ("improve [feature]" or "add support for
[feature capability]") does not satisfy this template -- it must name the sub-feature element
that is the mechanism (e.g., "the event schema's missing timestamp_start field" or "the sync
step's hard write-connection requirement").

For each [LEAK], use this template exactly:

  Leak: [ID] [Name]
  Sub-feature or framing element causing leak: [name it]
  Change description: [specific naming, scope, or framing change]
  Projected impact: directional estimate of effect on non-target confusion or composite movement.

For each [DELIGHT]: [ID] [Name] -- sub-feature property landing well -- how to amplify.

If no blockers: "No adoption blockers to resolve."
If no leaks: "No positioning leaks to close."

Write artifact to simulations/review/customers/{topic}-customers-{date}.md.
Frontmatter: skill: review-customers, topic, date, input,
output_format: prose-first-then-table, c14_mechanism: table-locked-last,
c15_mechanism: close-before-advance-checkpoint, c17_mechanism: sub-feature-amendment-template.
```

---

## V-02: Pattern Synthesis Worked Example

Axis: Phrasing register -- the CROSS-PERSONA PATTERNS section receives a worked contrast example
showing feature-level vs sub-feature-level pattern statements, mirroring the R3 V-02 mechanism
that drove C-16 compliance in per-persona rationale. Single-axis test of C-18.
Hypothesis: The same mechanism that drove sub-feature specificity in per-persona rationale
(showing what the two levels look like side by side) will drive it in pattern synthesis. Pattern
analysis is a different cognitive task than per-persona scoring -- it requires aggregating across
entries rather than reasoning within one -- so a dedicated worked example for the pattern section
is necessary even when per-persona C-16 compliance is already established.

```
You are running /review:customers. Evaluate {{Topic}} using the 12-persona customer review.
Two structural rules govern output order. Both are mandatory.

STRUCTURAL RULE 1 -- PROSE-FIRST ORDER:
All 12 persona prose blocks appear before the scoring table. Do not write any table row until
all 12 persona blocks are complete.

STRUCTURAL RULE 2 -- CLOSE-BEFORE-ADVANCE:
Each persona block carries all applicable inline flags before the output advances to the next
persona. A flag that appears only in a summary section and not in the persona block where the
score was assigned is deferred -- a structural failure.

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

Segmentation rationale: one sentence.

CAUSAL PRECISION IN RATIONALE:
Rationale for each persona must name the sub-feature property that drove the score: a specific
capability, threshold, design decision, or workflow step -- not the feature generically.
Feature-level: "the feature lacks audit log support." Sub-feature-level: "the feature's event
schema records only completion events -- no status_change fields -- making audit reconstruction
impossible." Write sub-feature-level rationale for every persona.

PERSONA BLOCKS (all 12 before the table):
For each persona C-01 through C-12:

  [C-NN] [Name] ([Role]) | Tier: [tier] | [flags after flag resolution]
  - Usefulness [1-5]: [score]
  - Clarity [1-5]: [score]
  - Would-Adopt [1-5]: [score]
  - Rationale: 2-3 sentences at sub-feature specificity.

  Flag resolution (mandatory before advancing):
    CHECK A: primary tier AND Would-Adopt < 3? -> add [BLOCKER] to header line.
    CHECK B: non-target tier AND (Useful >= 4 OR Would-Adopt >= 3)? -> add [LEAK] to header line.
    CHECK C: any score = 5? -> add [DELIGHT: dimension] to header for each qualifying dimension.
  Complete all checks before writing the next persona's header line.

Write all 12 persona blocks before the table.

SCORING TABLE (after all 12 persona blocks):
Compile scores from the persona blocks. All 12 rows and tier labels required.

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
State count and weight per tier. Compute weighted averages per dimension and a composite on a
1-5 scale. Show the full calculation.

ADOPTION BLOCKERS:
Collect all [BLOCKER] entries. For each:
[ID] [Name] -- Would-Adopt: [score] -- [sub-feature property blocking adoption].
If none: "No adoption blockers."

POSITIONING LEAKS:
Collect all [LEAK] entries. For each:
[ID] [Name] -- [signal score] -- [sub-feature or framing element causing leak].
If none: "No positioning leaks."

DELIGHT SIGNALS:
Collect all [DELIGHT] entries. Group by dimension.
[ID] [Name] -- [dimension] -- [sub-feature property producing delight; marketing implication].
If none: "No delight signals."

CROSS-PERSONA PATTERNS -- SUB-FEATURE RESOLUTION REQUIRED:

A cross-persona pattern is not a description of the scoring distribution. It is a named causal
finding: a single sub-feature property that explains a consistent reaction across a cluster of
personas. The pattern is only actionable if it names the sub-feature mechanism, because a single
design intervention at the sub-feature level can lift the entire cluster simultaneously.

Here is what the two levels look like:

FEATURE-LEVEL PATTERN (passes C-09, fails C-18):
"The workflow-integration cluster (C-04, C-07, C-08) scores consistently low on clarity.
These personas work in structured, multi-step environments and find the feature hard to
place in their existing flow."
Why it fails: names the affected cluster and the dimension but treats the feature as a single
object. "Hard to place" does not name a specific design decision as the mechanism.
Not directly actionable: the team cannot address "hard to place" without further diagnosis.

SUB-FEATURE-LEVEL PATTERN (passes C-09 and C-18):
"The workflow-integration cluster (C-04, C-07, C-08) scores consistently low on clarity
because the feature's invocation model requires a manual context-switch out of the existing
tool -- there is no ambient trigger or inline activation path -- making it structurally
invisible to personas who do not already know to look for it. The sub-feature mechanism is
the activation model design, not the feature's overall approach. A single intervention
(an inline trigger that surfaces the feature at the natural workflow decision point)
would lift clarity for all three personas without redesigning anything else."
Why it works: names the cluster, the sub-feature (activation model design, absence of inline
trigger), the structural cause (requires context-switch), and a single intervention that
addresses the cross-cluster pattern. Directly actionable as one design decision.

Write at least one pattern at sub-feature resolution. If you find yourself describing the score
distribution without naming a specific design decision or capability constraint as the mechanism,
you are at feature-level -- ask "which specific part of the feature causes this cluster to react
this way?" until you can name it.

AMEND:
Address findings in this order:
1. Adoption blockers -- for each [BLOCKER], name the specific sub-feature change and project:
   "Resolving [ID] blocker by [specific sub-feature change] likely lifts primary Would-Adopt
   by ~[delta], moving weighted composite from [current] to approximately [current + effect]."
2. Positioning leaks -- for each [LEAK], name the specific framing, naming, or scope change
   and a directional estimate.
3. Delight amplification -- for each [DELIGHT], which sub-feature property is landing and
   how to amplify it.

If no blockers: "No adoption blockers to resolve."
If no leaks: "No positioning leaks to close."

Write artifact to simulations/review/customers/{topic}-customers-{date}.md.
Frontmatter: skill: review-customers, topic, date, input,
output_format: prose-first-then-table, c14_mechanism: table-locked-last,
c15_mechanism: close-before-advance-checkpoint, c16_mechanism: sub-feature-specificity,
c18_mechanism: pattern-synthesis-worked-example.
```

---

## V-03: Three-Tier Blocker Traversal Explicit Labeling

Axis: Lifecycle emphasis -- the ADOPTION BLOCKERS collection section requires at least one
blocker to be written with explicit L1/L2/L3 labels, proving causal chain completeness rather
than sub-feature naming alone. Single-axis test of C-19.
Hypothesis: An output can pass C-16 by learning to name sub-features without constructing the
full causal chain. L3 alone (sub-feature named) is terminological compliance. L1+L2+L3 together
(stakes + feature-level gap + mechanism) is chain completeness. Explicit labels make the chain
visible in output structure, proving traversability: the reader can follow stakes to mechanism
without inferring missing steps. Abstract instructions ("show the full chain") allow skip-bridging;
labeled structure does not.

```
You are running /review:customers. Evaluate {{Topic}} using the 12-persona customer review.
Two structural rules govern output order. Both are mandatory.

STRUCTURAL RULE 1 -- PROSE-FIRST ORDER:
All 12 persona prose blocks appear before the scoring table. Do not write any table row until
all 12 persona blocks are complete.

STRUCTURAL RULE 2 -- CLOSE-BEFORE-ADVANCE:
Each persona block carries all applicable inline flags before the output advances to the next
persona. A flag that appears only in a summary section and not in the persona block where the
score was assigned is deferred -- a structural failure.

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

Segmentation rationale: one sentence.

PERSONA BLOCKS (all 12 before the table):
For each persona C-01 through C-12:

  [C-NN] [Name] ([Role]) | Tier: [tier] | [flags after flag resolution]
  - Usefulness [1-5]: [score]
  - Clarity [1-5]: [score]
  - Would-Adopt [1-5]: [score]
  - Rationale: 2-3 sentences. Name the specific feature property, design gap, or workflow
    mismatch that produced these scores. Framing: "the feature's [X] produced this reaction."
    Name the sub-feature property where possible: capability, threshold, design decision, or
    workflow step -- not the feature generically.

  Flag resolution (mandatory before advancing):
    CHECK A: primary tier AND Would-Adopt < 3? -> add [BLOCKER] to header line.
    CHECK B: non-target tier AND (Useful >= 4 OR Would-Adopt >= 3)? -> add [LEAK] to header.
    CHECK C: any score = 5? -> add [DELIGHT: dimension] to header for each qualifying dimension.
  Complete all checks before writing the next persona's header line.

Write all 12 persona blocks before the table.

SCORING TABLE (after all 12 persona blocks):
Compile scores from the persona blocks. All 12 rows and tier labels required.

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
State count and weight per tier. Compute weighted averages per dimension and composite on 1-5
scale. Show the full calculation.

ADOPTION BLOCKERS -- THREE-TIER CHAIN REQUIRED FOR AT LEAST ONE:

Collect all [BLOCKER] entries from the persona blocks.

For every blocker, write:
[ID] [Name] -- Would-Adopt: [score] -- [causal statement]

For at least one blocker, the causal statement must traverse all three levels explicitly labeled:
  L1 (persona context): [the goal, workflow constraint, or responsibility that makes this
    persona care about the gap -- their stake in the outcome]
  L2 (feature-level gap): [what the feature as a whole does not support -- the gap at the
    feature level that blocks this persona]
  L3 (sub-feature mechanism): [which specific capability, threshold, design decision, or
    workflow step in the feature is the reason L2 exists -- the named amendment target]

The three levels are a chain, not a list. L1 establishes why the persona is blocked. L2 names
the gap at feature level. L3 names the specific sub-feature property that produces L2.
An entry with L1 and L3 but no L2 skips the feature-level bridge -- the gap is unstated.
An entry with L2 and L3 but no L1 names the mechanism without explaining why it matters to
this persona. An entry with only L3 (sub-feature named) is terminological compliance -- it names
the mechanism but omits the stakes (L1) and the feature-level gap (L2) that make the mechanism
a blocker rather than a neutral design observation.

All three levels are required in at least one blocker entry. Remaining blockers may use prose
format without labels, but must still state what is blocking adoption.

If no adoption blockers exist: "No adoption blockers." (criterion auto-waived)

POSITIONING LEAKS:
Collect all [LEAK] entries. For each:
[ID] [Name] -- [signal score] -- [sub-feature or framing element causing leak].
If none: "No positioning leaks."

DELIGHT SIGNALS:
Collect all [DELIGHT] entries. Group by dimension.
[ID] [Name] -- [dimension] -- [sub-feature property producing delight; marketing implication].
If none: "No delight signals."

CROSS-PERSONA PATTERNS:
Identify at least one named cross-cutting pattern that names a feature mechanism as its cause.
State the design or messaging implication. Generic observations ("scores vary") do not qualify.

AMEND:
Address findings in this order:
1. Adoption blockers -- for each [BLOCKER], state the specific sub-feature change and project:
   "Resolving [ID] blocker by [specific sub-feature change] likely lifts primary Would-Adopt
   by ~[delta], moving weighted composite from [current] to approximately [current + effect]."
2. Positioning leaks -- for each [LEAK], name the specific framing or scope change and a
   directional estimate.
3. Delight amplification -- for each [DELIGHT], sub-feature property landing well; how to
   amplify in messaging or onboarding.

If no blockers: "No adoption blockers to resolve."
If no leaks: "No positioning leaks to close."

Write artifact to simulations/review/customers/{topic}-customers-{date}.md.
Frontmatter: skill: review-customers, topic, date, input,
output_format: prose-first-then-table, c14_mechanism: table-locked-last,
c15_mechanism: close-before-advance-checkpoint, c19_mechanism: three-tier-explicit-labels.
```

---

## V-04: C-17 + C-18 Combined (Formal)

Axis: Amendment sub-feature targeting (C-17) combined with cross-persona pattern sub-feature
resolution (C-18), in formal phrasing register. Combined test without three-tier traversal
labeling (C-19).
Hypothesis: C-17 and C-18 address disjoint sections (AMEND vs CROSS-PERSONA PATTERNS) with
no shared output budget and no structural dependency. Combining them should not require register
change or additional per-persona scaffolding. If V-04 passes both C-17 and C-18 in formal
register while preserving C-14/C-15/C-16, formal register is sufficient for post-scoring section
precision. Comparison to V-05 isolates whether conversational framing is necessary for C-19
(chain traversal) or optional.

```
You are running /review:customers. Evaluate {{Topic}} using the 12-persona customer review.
Two structural rules govern output order. Both are mandatory.

STRUCTURAL RULE 1 -- PROSE-FIRST ORDER:
All 12 persona prose blocks appear before the scoring table. Do not write any table row until
all 12 persona blocks are complete. The table is a verified artifact of finished reasoning.

STRUCTURAL RULE 2 -- CLOSE-BEFORE-ADVANCE:
Each persona block must carry all applicable inline flags before the output advances to the next
persona. The failure mode is: score qualifies for [BLOCKER] or [LEAK], advance to the next
persona, surface the flag post-hoc. That sequence is not permitted. A flag appearing only in a
summary section and not in the persona block where the score was assigned = structural failure.

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
For each persona C-01 through C-12, follow this sequence:

  Step 1 -- Header line:
  [C-NN] [Name] ([Role]) | Tier: [tier]

  Step 2 -- Scores:
  - Usefulness [1-5]: [score]
  - Clarity [1-5]: [score]
  - Would-Adopt [1-5]: [score]

  Step 3 -- Rationale (2-3 sentences):
  Name the specific feature property, design gap, or workflow mismatch that produced these
  scores. The framing is "the feature's [X] produced this reaction" -- not "this persona
  values [Y]." Name the sub-feature property: the specific capability, threshold, design
  decision, or workflow step -- not the feature generically.

  Step 4 -- Flag resolution (mandatory before advancing):
    CHECK A: primary tier AND Would-Adopt < 3?
    -> YES: add [BLOCKER] to this persona's header line. NO: continue.

    CHECK B: non-target tier AND (Useful >= 4 OR Would-Adopt >= 3)?
    -> YES: add [LEAK] to this persona's header line. NO: continue.

    CHECK C: any score equal to 5?
    -> YES: add [DELIGHT: dimension] to header line for each qualifying dimension. NO: continue.

  You may not write the next persona's header line until Step 4 is complete.

Write all 12 persona blocks before writing any part of the scoring table.

SCORING TABLE (after all 12 persona blocks):
Compile scores from the persona blocks. All 12 rows and tier labels required.

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
List: [ID] [Name] -- Would-Adopt: [score] -- [sub-feature property blocking adoption].
If none: "No adoption blockers."

POSITIONING LEAKS:
Collect all [LEAK] entries from the persona blocks.
List: [ID] [Name] -- [signal score] -- [sub-feature or framing element causing leak].
If none: "No positioning leaks."

DELIGHT SIGNALS:
Collect all [DELIGHT] entries from the persona blocks. Group by dimension.
List: [ID] [Name] -- [dimension] -- [sub-feature property producing delight; marketing implication].
If none: "No delight signals."

CROSS-PERSONA PATTERNS -- SUB-FEATURE MECHANISM REQUIRED:
Identify at least one named cross-cutting pattern. The pattern must name a sub-feature property
as the structural cause across the cluster -- not the feature generically and not the affected
segment alone. The distinction:

  Segment only (fails): "The manager/buyer cluster (C-08, C-11) scores low on would-adopt."
  Feature-level (passes C-09, fails C-18): "The manager/buyer cluster scores low on would-adopt
    because the feature lacks integration with approval workflows."
  Sub-feature-level (passes C-09 and C-18): "The manager/buyer cluster scores low on would-adopt
    because the feature's permission model has no delegation layer -- there is no way to assign
    review rights to a subordinate -- which means personas whose workflows require distributed
    approval cannot use it without becoming a personal bottleneck. The sub-feature mechanism is
    the permission model's flat ownership design."

Name the sub-feature mechanism. State the design or messaging implication.

AMEND -- SUB-FEATURE AMENDMENT TARGETS REQUIRED:
Address findings in this order: blockers first, then leaks, then delight amplification.

For each [BLOCKER]:
  Sub-feature amendment target: [name the specific capability, threshold, design decision, or
    workflow step to change -- the same sub-feature property named in the persona's rationale
    or a more refined decomposition of it]
  Change: [what specifically changes about that sub-feature]
  Projection: "Resolving [ID] blocker by [sub-feature change] likely lifts primary Would-Adopt
    by ~[delta], moving weighted composite from [current] to approximately [current + effect]."

A generic amendment target ("improve the feature," "add support for X") does not satisfy this
requirement. The sub-feature property must be named as a specific capability, threshold, design
decision, or workflow step directly assignable to a design decision without further decomposition.

For each [LEAK]:
  Sub-feature or framing element causing leak: [name it]
  Change: [specific naming, scope, or framing adjustment]
  Projection: directional estimate of effect on non-target confusion or composite.

For each [DELIGHT]: [ID] [Name] -- sub-feature property landing well -- amplification in
messaging or onboarding.

If no blockers: "No adoption blockers to resolve."
If no leaks: "No positioning leaks to close."

Write artifact to simulations/review/customers/{topic}-customers-{date}.md.
Frontmatter: skill: review-customers, topic, date, input,
output_format: prose-first-then-table, c14_mechanism: table-locked-last,
c15_mechanism: close-before-advance-checkpoint, c16_mechanism: sub-feature-specificity,
c17_mechanism: sub-feature-amendment-targets, c18_mechanism: sub-feature-pattern-contrast.
```

---

## V-05: Full R4 -- C-17 + C-18 + C-19 in Conversational Register

Axis: All three R4 criteria (C-17 amendment sub-feature targets, C-18 cross-persona pattern at
sub-feature resolution, C-19 three-tier blocker chain traversal) embedded in conversational
phrasing register with all R3 mechanisms preserved. Full R4 target.
Hypothesis: Conversational register was R3's strongest depth predictor (V-05 R3 produced the
best C-16 results). C-17/C-18/C-19 all target post-persona sections (amend, synthesis, blockers),
so they layer onto the R3 conversational baseline without displacing per-persona depth. If V-05
outperforms V-04 on C-19 at comparable C-17/C-18 scores, conversational framing is the enabling
variable for blocker chain completeness -- describing the chain to the reader in natural language
forces traversal in a way that formal templating does not.

```
You are running /review:customers. Work through this as a customer advisory panel. The goal is
to understand what twelve different people would actually think, feel, and decide if they
encountered this feature today. The output structure matters: reason through each persona in
prose first, then compile all results into a scoring table afterward. The prose comes before the
table -- always -- because the table should reflect genuine reasoning, not a scaffold that
reasoning fits into after the fact.

---

WHAT ARE WE EVALUATING?

Read the spec or signal for {{Topic}}. Understand what the feature does, what problem it solves,
and what it asks of the people who would use it. Before you invite anyone into the room, make
sure you know what you are showing them.

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
- Usefulness: Does this solve a real problem they actually have? (1 = irrelevant to their work;
  5 = solves something they struggle with today)
- Clarity: Do they understand what this is and what it does? (1 = confused about the basic
  proposition; 5 = immediately obvious)
- Would-Adopt: Would they actually use this, given how they work right now? (1 = no chance;
  5 = adopts immediately without being asked)

Then write 2-3 sentences explaining what happened. The explanation must name the specific
sub-feature property that drove the scores -- not the feature generically, and not the persona's
preferences. The three levels of explanation:

  LEVEL 1 -- Not sufficient (no feature named):
  "This persona values reliability and documentation, so the feature's opaque approach makes
  them hesitant."
  Why it fails: describes the person, not the feature.

  LEVEL 2 -- Better but not enough (feature named, sub-feature not):
  "The feature lacks offline support, which this persona needs for field deployments."
  Why it fails: names a feature gap but not the specific design decision or capability boundary
  that creates it. "Lacks offline support" implicates the whole feature. Not actionable.

  LEVEL 3 -- What's required (sub-feature mechanism named):
  "The feature's sync step requires an active write connection to the central registry --
  there is no local-cache mode and no queue-and-flush option -- which means this persona
  cannot use it in the field environments where their work actually happens. The blocker is
  the sync architecture, not the feature's overall approach, and it has a specific fix: a
  local-first cache with background sync."
  Why it works: names the sub-feature (sync step design), the specific constraint (no local-cache
  or queue-and-flush), the impact, and the amendment target. Directly actionable.

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
A flag that only appears in a summary section later -- and not in the entry where the score was
assigned -- was deferred, not applied. Deferral is not the same as inline flagging.

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

All 12 rows and all tier labels required. The table is a summary of reasoning already done --
not a scoring step.

---

IS ADOPTION BLOCKED?

Look at the would-adopt scores for your primary-audience personas. Did any score below 3?

If yes, write each blocker as a three-part case that a reader can follow from the persona's
situation to the exact mechanism blocking them:

  First, the stakes: what goal, workflow constraint, or responsibility makes this persona care?
  Why does this gap matter to this specific person? This is what makes the blocker a blocker
  and not just a limitation.

  Then, the feature-level gap: what does the feature as a whole fail to support? State it plainly
  before naming the mechanism. This is the bridge -- without it, the sub-feature name is a
  technical observation floating without context.

  Then, the sub-feature mechanism: which specific capability, threshold, design decision, or
  workflow step in the feature is the reason the gap exists? Name it as the amendment target.
  This is where the fix lives -- specific enough to assign to a design decision.

Write this three-part chain for at least one blocker. The goal is a rationale that a reader can
traverse from "why this persona is affected" to "exactly what to change" without inferring missing
steps. An entry that names only the sub-feature (the third part) without establishing stakes and
feature-level gap is not a causal chain -- it is a named mechanism without context.

If no primary persona scored below 3: "No adoption blockers." Do not skip the check.

---

IS THE POSITIONING LEAKING?

Check your non-target personas. Did any score surprisingly high on usefulness or would-adopt?
Or does their explanation show confusion about whether this feature is meant for them?
Name each leak by ID and describe the sub-feature or framing element causing it: what specific
property of how the feature is named, described, or scoped made this non-target persona think
it might be for them?

If no leaks: "No positioning leaks." Do not skip the check.

---

WHO IS DELIGHTED?

Any score of 5 anywhere is worth pausing on. Group by dimension. For each, ask: which sub-feature
property produced this reaction? What would you amplify in messaging, onboarding, or positioning?

If there are no 5s: "No delight signals."

---

WHAT DO THE NUMBERS SAY IN AGGREGATE?

Primary personas carry 3x the weight of non-target; secondary carries 2x. Compute weighted
averages for each dimension and an overall composite on a 1-5 scale. Show how you weighted it --
state the weight per tier and count per tier.

Now look across all twelve explanations for a pattern that names a sub-feature mechanism. Not a
description of the score distribution -- a named causal finding: a single sub-feature property
that explains a consistent reaction across a cluster of personas. Ask yourself: is there a
specific design decision or capability constraint that multiple personas are reacting to in the
same way? If so, that is the highest-leverage finding in this review -- a single sub-feature
cause that explains a cluster's scores means one intervention can lift all of them simultaneously.

The difference between a pattern and a distribution observation:
  Distribution observation: "Role cluster X scores low on clarity."
  Pattern with feature-level cause: "Role cluster X scores low on clarity because the feature
    lacks documentation." (Names the gap; not the mechanism.)
  Pattern with sub-feature cause: "Role cluster X scores low on clarity because the feature's
    onboarding flow shows the configuration UI before the concept is introduced -- personas who
    have not seen the concept before see options without context." (Names the sub-feature
    mechanism: the onboarding flow's sequencing, not "lacks documentation".)

Name the sub-feature mechanism. State what it implies for the team. Explain how a single
design intervention at that sub-feature would affect the cluster.

---

WHAT SHOULD CHANGE?

Address adoption blockers first. For each blocked primary persona, the amendment target is the
sub-feature mechanism from their three-part chain -- the same one you named as L3. Project the
score movement:
"Fixing [specific sub-feature property] for [ID] likely lifts primary Would-Adopt by ~[delta],
moving weighted composite from [current] to approximately [current + effect]."

The amendment target must be the sub-feature mechanism, not a restatement of the feature-level
gap. If the chain said "the sync architecture's hard write-connection requirement," the amendment
is "add a local-cache mode to the sync step" -- not "improve offline support." The causal chain
that drove the score drives the fix.

Then address positioning leaks. What specific sub-feature or framing element is causing non-target
personas to be attracted or confused? Name the change.

Then amplify delight signals. Which sub-feature property is already landing? How do you lean into
it in messaging or onboarding?

---

Write the artifact to simulations/review/customers/{topic}-customers-{date}.md.
Frontmatter: skill: review-customers, topic, date, input,
register: conversational, output_format: prose-first-then-table,
c14_mechanism: table-locked-last, c15_mechanism: close-before-advance,
c16_mechanism: three-tier-worked-example, causal_precision: sub-feature-level,
c17_mechanism: sub-feature-amendment-targets-chain-parity,
c18_mechanism: sub-feature-pattern-structural-cause,
c19_mechanism: three-tier-blocker-chain-traversal.
```
