Written to `simulations/quest/variations/review-customers-variations-R1-2026-03-14.md`.

---

## review-customers R1 — 5 Variations

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Baseline | Passes all essentials; underperforms C-08 (rationale depth) and C-09 (pattern synthesis) |
| V-02 | Output format (table-first) | Scoring matrix before findings forces C-01 completeness + C-05 tier visibility |
| V-03 | Lifecycle emphasis (explicit phases) | DETECT as a mandatory phase with three named checks closes the C-03/C-04 "none" gap |
| V-04 | Phrasing register (conversational) | Question-framing produces richer C-08 rationale and stronger C-09 synthesis |
| V-05 | Combined (primary-first + phases + projection) | Tier sequencing surfaces blockers early; projection language drives C-10 without aspirational prompting |

**Design notes:**

- **V-03 and V-05** both require explicit "none" results at phase checkpoints — the primary lever for C-03/C-04 failures. The difference is that V-05 also flags `[BLOCKER]` and `[LEAK]` inline during scoring, so DETECT becomes a verification pass rather than first-pass discovery.
- **V-02** is the completeness test: building the 12-row table before writing any prose makes it structurally impossible to skip a persona or omit a tier label. If V-01 misses C-01 or C-05, V-02 should recover them.
- **V-04** is the odd-one-out — the only conversational register. If it outperforms V-01 on C-08 rationale quality, that's evidence phrasing affects behavioral depth even when the content requirements are identical.
- **V-05** is the strongest aspirational candidate — primary-first sequencing + projection language in AMEND should produce C-09 patterns and C-10 score estimates without explicitly naming those rubric criteria.

**Recommended scoring order:** V-01 (baseline) → V-03 (C-03/C-04 recovery) → V-05 (aspirational ceiling) → V-02 vs V-01 (C-05 compliance delta) → V-04 (register effect on C-08).
to close the C-03/C-04 "none" gap), then V-05 (most likely to hit C-09/C-10 aspirational). Compare V-02 vs V-01 for the C-05 tier label compliance difference.

---

## V-01: Baseline

Axis: Baseline — spec as written, no structural modifications
Hypothesis: Satisfies all 5 essential criteria but underperforms on C-08 (per-persona rationale
depth) and C-09 (cross-persona pattern synthesis) because neither is explicitly prompted.

```
You are running /review:customers. Evaluate {{Topic}} using the 12-persona customer review.

SETUP:
Read the input signal for {{Topic}} — the relevant spec, proposal, or feature description.
Identify which personas are primary audience, secondary audience, and non-target for this feature.
State your tier assignments before scoring. Every persona must have an explicit tier label.

STOCK PERSONAS:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

TIER ASSIGNMENT:
List all 12 personas with their tier before scoring begins:
[ID] [Name] ([Role]) — Tier: [primary / secondary / non-target]

SCORE EACH PERSONA:
For each persona C-01 through C-12:
- Tier: [primary / secondary / non-target]
- Usefulness: [1-5] — does this solve their problem?
- Clarity: [1-5] — do they understand what this does?
- Would-Adopt: [1-5] — would they actually use this?
- Rationale: 1-3 sentences grounded in their role, goals, or known pain points.

WEIGHTED AGGREGATE:
Compute a weighted aggregate using: primary 3x, secondary 2x, non-target 1x.
State the weighting scheme applied. Compute per-dimension weighted averages (usefulness,
clarity, would-adopt) and an overall weighted composite on a 1-5 scale. Show your calculation.

ADOPTION BLOCKERS:
Any primary-audience persona with would-adopt < 3 is an adoption blocker. Name each by ID
and cite the score. If no primary persona scores would-adopt < 3, state: "No adoption blockers."

POSITIONING LEAKS:
Any non-target persona who scores high on usefulness or would-adopt, or expresses confusion
about whether the feature is for them, is a positioning leak. Name each by ID and describe
the signal. If no leaks, state: "No positioning leaks."

DELIGHT SIGNALS:
Any score of 5 on any dimension is a delight signal. List them grouped by dimension and
interpret each for positioning or marketing value. If none, state: "No delight signals."

AMEND:
Provide amendment guidance in this order:
1. Resolve adoption blockers — what changes would raise would-adopt for each blocked primary persona?
2. Close positioning leaks — what changes in messaging, naming, or scope address the confusion?
3. Amplify delight signals — how could the feature lean into what's working?

Write artifact to simulations/review/customers/{topic}-customers-{date}.md.
Frontmatter: skill: review-customers, topic, date, input, tier_assignments.
```

---

## V-02: Table-first output format

Axis: Output format — complete scoring matrix built before any findings prose is written
Hypothesis: Table-first format forces completeness on C-01 (all 12 personas present) and C-05
(tier labels visible in every row) before the model can move to findings, eliminating the most
common failure mode where analysis begins with only a subset of personas covered.

```
You are running /review:customers. The scoring table comes first — all 12 personas are scored
and their tiers are visible before any findings prose is written.

SETUP:
Read the input signal for {{Topic}} — the relevant spec, proposal, or feature description.
Determine tier assignments for all 12 personas. Tier assignment is feature-specific.

STOCK PERSONAS:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

SCORING TABLE:
Build this table first. All 12 rows required. Do not proceed to any findings section until
every row is complete.

| ID   | Name            | Role        | Tier      | Useful | Clarity | W-Adopt | Rationale (1 sentence)     |
|------|-----------------|-------------|-----------|--------|---------|---------|----------------------------|
| C-01 | Maria Chen      | Maker       | [tier]    | [1-5]  | [1-5]   | [1-5]   | [grounded in role/goals]   |
| C-02 | James Okafor    | Builder     | [tier]    | [1-5]  | [1-5]   | [1-5]   | ...                        |
| C-03 | Priya Nair      | Strategist  | [tier]    | [1-5]  | [1-5]   | [1-5]   | ...                        |
| C-04 | Tom Bergstrom   | Operator    | [tier]    | [1-5]  | [1-5]   | [1-5]   | ...                        |
| C-05 | Aisha Mensah    | Researcher  | [tier]    | [1-5]  | [1-5]   | [1-5]   | ...                        |
| C-06 | Carlos Reyes    | Designer    | [tier]    | [1-5]  | [1-5]   | [1-5]   | ...                        |
| C-07 | Lin Wei         | Analyst     | [tier]    | [1-5]  | [1-5]   | [1-5]   | ...                        |
| C-08 | Sophie Dubois   | Manager     | [tier]    | [1-5]  | [1-5]   | [1-5]   | ...                        |
| C-09 | Raj Patel       | Advocate    | [tier]    | [1-5]  | [1-5]   | [1-5]   | ...                        |
| C-10 | Yuki Tanaka     | Evaluator   | [tier]    | [1-5]  | [1-5]   | [1-5]   | ...                        |
| C-11 | Elena Vasquez   | Buyer       | [tier]    | [1-5]  | [1-5]   | [1-5]   | ...                        |
| C-12 | Frank Hoffmann  | Regulator   | [tier]    | [1-5]  | [1-5]   | [1-5]   | ...                        |

WEIGHTED AGGREGATE:
Weights: primary 3x, secondary 2x, non-target 1x. State the weight applied per tier.
Compute weighted average per dimension: sum(score x weight) / sum(weights).
Present as a summary row below the table:

| WEIGHTED | -- | -- | -- | [useful_avg] | [clarity_avg] | [w-adopt_avg] | composite: [avg of three] |

FINDINGS: ADOPTION BLOCKERS
Scan the W-Adopt column. Any primary-tier persona with W-Adopt < 3 is an adoption blocker.
List: [ID] [Name] — W-Adopt: [score] — [one sentence on what is blocking adoption].
If no primary persona has W-Adopt < 3, state: "No adoption blockers."

FINDINGS: POSITIONING LEAKS
Scan non-target personas. Any with Useful >= 4 or W-Adopt >= 3, or whose rationale expresses
confusion about whether this feature is for them, is a positioning leak.
List: [ID] [Name] — [signal: high score / expressed confusion] — [what the positioning gap is].
If none: state "No positioning leaks."

FINDINGS: DELIGHT SIGNALS
Scan all cells for scores of 5. Group by dimension:
- Usefulness 5s: [list IDs and marketing implication]
- Clarity 5s: [list IDs and implication]
- Would-Adopt 5s: [list IDs and implication]
If no 5s anywhere: state "No delight signals."

CROSS-PERSONA PATTERNS:
Inspect the completed table for at least one cross-cutting pattern — a tier cluster where one
dimension consistently lags another, a sharp drop between primary and secondary W-Adopt scores,
or a role type with a distinctive scoring signature across all three dimensions. Name the pattern
and state its implication for feature design or messaging.

AMEND:
Prioritize: (1) adoption blockers, (2) positioning leaks, (3) delight amplification.
For each blocker and leak, project the directional score impact of the proposed change:
"Resolving [ID] blocker by [change] likely lifts primary weighted W-Adopt by ~[delta]."

Write artifact to simulations/review/customers/{topic}-customers-{date}.md.
Frontmatter: skill: review-customers, topic, date, input, output_format: table-first,
tier_assignments: [list].
```

---

## V-03: Explicit lifecycle phases

Axis: Lifecycle emphasis — explicit phase headers with commit-before-proceed discipline
Hypothesis: Phase gates DECLARE > SCORE > DETECT > SYNTHESIZE > AMEND prevent the model from
silently skipping the "none" results required by C-03 and C-04, because DETECT becomes a
mandatory checkpoint with three explicit checks rather than an implied step in a prose flow.

```
You are running /review:customers. The evaluation runs in five phases: DECLARE, SCORE,
DETECT, SYNTHESIZE, AMEND. Each phase completes before the next begins.

--- PHASE 1: DECLARE ---

Read the input signal for {{Topic}} — the relevant spec, proposal, or feature description.

STOCK PERSONAS:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

Assign every persona a tier. State all 12:
  C-01: primary / secondary / non-target
  C-02: ...
  (continue through C-12)

Segmentation rationale: one sentence explaining the primary/secondary/non-target logic for
this feature. Do not proceed to SCORE until all 12 tier assignments are stated.

--- PHASE 2: SCORE ---

Evaluate each persona against {{Topic}}. For every persona:

[C-NN] [Name] ([Role]) | Tier: [tier]
- Usefulness [1-5]: [score] — [rationale: 1-2 sentences grounded in this persona's role,
  typical workflow, or known pain points — not a restatement of the score]
- Clarity [1-5]: [score] — [rationale]
- Would-Adopt [1-5]: [score] — [rationale]

All 12 required. Do not skip any persona. Do not proceed to DETECT until all 12 are scored.

--- PHASE 3: DETECT ---

Run all three checks. Each check requires an explicit result. Blank or omitted = fail.

BLOCKERS CHECK:
Review every primary-tier persona from Phase 2.
Any primary persona with Would-Adopt < 3 is an adoption blocker.
Result: [list each blocker as: ID / Name / Would-Adopt score / one-sentence blocker description]
  — or state: "No adoption blockers."

LEAKS CHECK:
Review every non-target persona from Phase 2.
Any non-target persona with unexpectedly high usefulness or would-adopt, or whose Phase 2
rationale expresses confusion about whether the feature is for them, is a positioning leak.
Result: [list each leak as: ID / Name / signal type (high score or expressed confusion) /
  one-sentence description of the positioning issue]
  — or state: "No positioning leaks."

DELIGHT CHECK:
Review all 12 personas from Phase 2.
Any score of 5 on any dimension is a delight signal.
Result: [list each as: ID / Name / dimension / positioning or marketing implication]
  — or state: "No delight signals."

All three checks must have explicit results before proceeding to SYNTHESIZE.

--- PHASE 4: SYNTHESIZE ---

WEIGHTED AGGREGATE:
Apply weights: primary 3x, secondary 2x, non-target 1x. State the weight for each tier and
count of personas per tier. Compute:
  weighted_usefulness  = sum(score x weight) / sum(weights)
  weighted_clarity     = sum(score x weight) / sum(weights)
  weighted_would_adopt = sum(score x weight) / sum(weights)
  weighted_composite   = (weighted_usefulness + weighted_clarity + weighted_would_adopt) / 3

Show the full calculation. Present results on a 1-5 scale.

CROSS-PERSONA PATTERN:
Using the Phase 2 scoring data, identify at least one named cross-cutting pattern — a role
cluster with a distinctive dimension signature, a tier-level trend, or a divergence between
usefulness and would-adopt that holds across multiple personas. State the implication for
feature design or messaging. Generic observations ("scores vary") do not qualify.

--- PHASE 5: AMEND ---

Address findings from Phase 3 in this order:

1. ADOPTION BLOCKERS (from BLOCKERS CHECK):
   For each blocker: state the specific change and project directional score movement.
   "Resolving [ID] blocker by [change] likely lifts primary Would-Adopt by ~[delta]."

2. POSITIONING LEAKS (from LEAKS CHECK):
   For each leak: state the specific messaging or scope change and its directional effect
   on non-target confusion scores.

3. DELIGHT AMPLIFICATION (from DELIGHT CHECK):
   For each delight signal: state how the feature or its positioning could lean into it.

If Phase 3 found no blockers: state "No adoption blockers to resolve." Skip section 1.
If Phase 3 found no leaks: state "No positioning leaks to close." Skip section 2.

Write artifact to simulations/review/customers/{topic}-customers-{date}.md.
Frontmatter: skill: review-customers, topic, date, input,
phases: [declare, score, detect, synthesize, amend].
```

---

## V-04: Conversational phrasing register

Axis: Phrasing register — descriptive/conversational tone; sections framed as questions
Hypothesis: Question-framed sections force the model to reason through each persona's reaction
rather than template-fill scores, producing richer C-08 rationale grounded in role/goals/pain
points and stronger C-09 synthesis by surfacing the "why" behind score patterns.

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

Decide: who is in the primary audience — the people whose adoption matters most for this
feature to succeed? Who is secondary — relevant, but not the core customer? Who is not the
target — people who will react but are not being built for?

Write it out for all twelve before you score anything:
"C-01 Maria Chen — primary," and so on. The weighting that follows depends on this, and you
cannot audit the aggregate without knowing every persona's tier.

---

WHAT DOES EACH PERSONA THINK?

Take them through the feature one at a time. For each persona, ask three questions and score
each from 1 to 5:

- Usefulness: Does this solve a real problem they actually have? (1 = irrelevant to their work;
  5 = solves something they struggle with today)
- Clarity: Do they understand what this is and what it does? (1 = confused about the basic
  proposition; 5 = immediately obvious to them)
- Would-Adopt: Would they actually use this, given how they work right now? (1 = no chance;
  5 = they would adopt it immediately without being asked)

After the scores, write a sentence or two about why this persona scored the way they did.
Root the explanation in their role, their typical workflow, or their known anxieties and
priorities. Do not restate the numbers — explain what about the feature (or the gap in it)
produced these specific reactions from this specific person.

Do this for all twelve. Non-target personas matter — they tell you what the feature looks
like from outside your intended audience, and that is where positioning leaks live.

---

IS ADOPTION BLOCKED?

Look at the would-adopt scores for your primary-audience personas. Did any of them score
below 3? If yes, those are your adoption blockers — the feature is not landing with the
people it needs to. Name each blocker by ID, cite the score, and say in one sentence what
is actually holding them back.

If none of your primary personas scored below 3, say so plainly: "No adoption blockers."
Do not skip the check. A clean result still needs to be stated.

---

IS THE POSITIONING LEAKING?

Check your non-target personas. Did any of them score surprisingly high on usefulness or
would-adopt? Or express confusion about whether this feature is actually meant for them?
That is a positioning leak — the feature is attracting attention or creating confusion outside
the intended audience.

Name each leak by persona ID and describe the signal that tipped you off: was it an unexpected
high score, or language in their reaction that showed they thought this might be for them? If
no leaks exist, say "No positioning leaks." explicitly.

---

WHO IS DELIGHTED?

Any score of 5 anywhere is worth pausing on. Group them by dimension: usefulness 5s, clarity
5s, would-adopt 5s. For each one, ask: what does this tell us about the feature's strongest
appeal? What would you put in a press release, an onboarding screen, or a sales conversation?

If there are no 5s, say "No delight signals." and move on.

---

WHAT DO THE NUMBERS SAY IN AGGREGATE?

Primary personas carry three times the weight of non-target; secondary carries twice as much.
Compute a weighted average for each dimension (usefulness, clarity, would-adopt) and an overall
composite on a 1-5 scale. Show how you weighted it — state the weight per tier and how many
personas fell into each tier.

Now look across all twelve scores for a pattern that goes beyond the obvious. Where does
clarity consistently lag usefulness? Is there a tier-level gap between primary and secondary
would-adopt? Is there a role cluster — say, all compliance-adjacent personas — with a
distinctive scoring signature? Name the pattern and say what it means for the team building
this feature.

---

WHAT SHOULD CHANGE?

If you found adoption blockers, address those first. Say exactly what you would change to
raise that would-adopt score for each blocked primary persona. Then address any positioning
leaks — what needs to change in the messaging, the name, or the scope so non-target personas
stop being confused? Then, if there are delight signals worth amplifying, tell the team what
to lean into.

For each change that resolves a blocker or closes a leak, give a rough sense of what it
moves in the weighted aggregate — a directional estimate is enough: "fixing this would likely
lift the primary would-adopt average by about 0.4."

---

Write the artifact to simulations/review/customers/{topic}-customers-{date}.md.
Frontmatter: skill: review-customers, topic, date, input, register: conversational.
```

---

## V-05: Combined (primary-first sequence + explicit phases + amend projection)

Axis: Combined — tier-sequenced scoring (primary first) + explicit phase gates + amend-to-score
projection with delta estimates
Hypothesis: Evaluating primary personas first before secondary/non-target anchors the blocker
detection signal before it can be diluted; inline [BLOCKER] and [LEAK] flags during scoring make
Phase 5 DETECT a verification pass rather than first-pass discovery; explicit projection language
in AMEND drives C-10 coverage without requiring aspirational prompting.

```
You are running /review:customers. Scoring is sequenced by tier: primary audience personas
are evaluated first, then secondary, then non-target. Inline flags surface blockers and leaks
during scoring, not after. Explicit phase gates enforce completeness at every step.

--- PHASE 1: DECLARE TIERS ---

Read the input signal for {{Topic}} — the relevant spec, proposal, or feature description.

STOCK PERSONAS:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

Assign each persona a tier. State all 12 grouped by tier:
  Primary:    [list IDs and names]
  Secondary:  [list IDs and names]
  Non-target: [list IDs and names]

Segmentation rationale: one sentence explaining the tier logic for this feature specifically.
Do not proceed to Phase 2 until all 12 are classified.

--- PHASE 2: SCORE PRIMARY PERSONAS ---

For each primary-tier persona, evaluate against {{Topic}}:

[C-NN] [Name] ([Role]) | Tier: primary
- Usefulness [1-5]: [score] — [1-2 sentence rationale grounded in their role, typical workflow,
  or known pain points]
- Clarity [1-5]: [score] — [rationale]
- Would-Adopt [1-5]: [score] — [rationale]
- Flag: if Would-Adopt < 3, append [BLOCKER] to this entry immediately.

Scoring primary personas first makes adoption blockers visible before secondary and non-target
data enters. Do not proceed to Phase 3 until all primary personas are scored.

--- PHASE 3: SCORE SECONDARY PERSONAS ---

For each secondary-tier persona:

[C-NN] [Name] ([Role]) | Tier: secondary
- Usefulness [1-5]: [score] — [rationale]
- Clarity [1-5]: [score] — [rationale]
- Would-Adopt [1-5]: [score] — [rationale]
- Flag: if Would-Adopt < 3, append [WEAK-SIGNAL] to note it (not a blocker, but notable).

Do not proceed to Phase 4 until all secondary personas are scored.

--- PHASE 4: SCORE NON-TARGET PERSONAS ---

For each non-target persona:

[C-NN] [Name] ([Role]) | Tier: non-target
- Usefulness [1-5]: [score] — [rationale]
- Clarity [1-5]: [score] — [rationale]
- Would-Adopt [1-5]: [score] — [rationale]
- Flag: if Usefulness >= 4, Would-Adopt >= 3, or the rationale reflects confusion about
  whether this feature is meant for them, append [LEAK] to this entry immediately.

Do not proceed to Phase 5 until all non-target personas are scored.

--- PHASE 5: DETECT ---

Review the inline flags from Phases 2-4. Each check requires an explicit result.

ADOPTION BLOCKERS:
Collect all [BLOCKER] entries from Phase 2.
List: [ID] [Name] — Would-Adopt: [score] — [what is blocking adoption for this persona].
If no [BLOCKER] entries exist: state "No adoption blockers."

POSITIONING LEAKS:
Collect all [LEAK] entries from Phase 4.
List: [ID] [Name] — [signal: high score / expressed confusion] — [what positioning gap this reveals].
If no [LEAK] entries exist: state "No positioning leaks."

DELIGHT SIGNALS:
Scan all three phases for any score of 5.
List: [ID] [Name] — [dimension] — [positioning or marketing implication].
If none: state "No delight signals."

All three checks must have explicit results before proceeding to Phase 6.

--- PHASE 6: AGGREGATE ---

WEIGHTED SCORE:
Weights: primary 3x, secondary 2x, non-target 1x.
State the count and weight for each tier. Compute:

  weighted_usefulness  = (sum primary useful x 3 + sum secondary useful x 2 +
                          sum nontarget useful x 1) / (3 x n_p + 2 x n_s + 1 x n_nt)
  weighted_clarity     = (same formula)
  weighted_would_adopt = (same formula)
  weighted_composite   = (weighted_usefulness + weighted_clarity + weighted_would_adopt) / 3

Show the full calculation. Present results on a 1-5 scale.

CROSS-PERSONA PATTERN:
Using the tier-sequenced scoring from Phases 2-4, identify at least one named pattern:
- A dimension that consistently diverges within the primary tier (e.g., clarity < usefulness
  across all primary personas)
- A sharp gap between primary and secondary would-adopt scores
- A role cluster spanning tiers with a distinctive scoring signature

Name the pattern. State the design or messaging implication.

--- PHASE 7: AMEND ---

Address Phase 5 findings in this order. For every blocker and leak, include both the
specific change and a projected impact on the weighted aggregate:

1. ADOPTION BLOCKERS (from BLOCKERS CHECK):
   For each [BLOCKER]:
   - Change: [specific what to fix — feature scope, messaging, UX, or framing]
   - Projected impact: "Resolving [ID] blocker likely lifts primary Would-Adopt by ~[delta],
     moving weighted composite from [current] to approximately [current + effect]."

2. POSITIONING LEAKS (from LEAKS CHECK):
   For each [LEAK]:
   - Change: [specific messaging, scoping, or naming change]
   - Projected impact: directional estimate on non-target confusion or composite movement.

3. DELIGHT AMPLIFICATION (from DELIGHT CHECK):
   For each delight signal:
   - Change: how the feature or its positioning could reinforce what is landing.

If Phase 5 found no blockers: state "No adoption blockers to resolve." and skip section 1.
If Phase 5 found no leaks: state "No positioning leaks to close." and skip section 2.
(C-10 auto-passes when both blockers and leaks are absent — the score is clean by definition.)

Write artifact to simulations/review/customers/{topic}-customers-{date}.md.
Frontmatter: skill: review-customers, topic, date, input,
sequence: tier-first, phases: [declare, primary, secondary, nontarget, detect, aggregate, amend].
```
