Written to `simulations/quest/variations/listen-feedback-variations-R1-2026-03-14.md`.

---

## listen-feedback R1 — 5 Variations

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Baseline | Covers all essentials; A-01/A-02 likely missed; R-01 blocking escalation may appear inline rather than as a dedicated section |
| V-02 | Output format (scorecard-first) | NPS table before any feedback prose forces C-01 completeness and C-04 threshold check before findings prose can begin |
| V-03 | Lifecycle phases (explicit gates) | READ > SCORE > FEEDBACK > ESCALATE > SYNTHESIZE; ESCALATE as a named phase with explicit zero-result closes R-01 reliably |
| V-04 | Phrasing register (conversational) | Question-framed advisory panel tone produces richer per-persona rationale and more specific feedback item text |
| V-05 | Combined (ascending NPS + phases + sensitivity) | Lowest scorer first anchors revision priority; inline `[BLOCKING]` flags make escalation a verification pass; explicit sensitivity section drives A-02 |

---

### Key design decisions across variations

**Threshold placement differs across variations** — the primary structural bet. V-01 puts it at the end (most natural, most likely to be a throwaway line). V-02 puts it in the scorecard table header before any feedback is written. V-03 ends Phase 2 with it as a phase gate. V-05 ends Phase 1 with it as a hard stop. This is the most likely source of C-04 variance across runs.

**The R-01 gap** (blocking escalation as a dedicated section, not inline) is the most common failure mode. V-01 relies on per-card formatting. V-03 and V-05 make it a named phase with mandatory explicit result — if no blocking items exist, you must state "No blocking items." Neither can silently omit the section.

**A-02 (sensitivity analysis)** only appears in V-05, by name and with explicit format. If any other variation produces a sensitivity analysis, that is a signal the rubric criterion is reachable without explicit prompting.

**Recommended scoring order:** V-01 (baseline) → V-03 (C-04/R-01 recovery) → V-05 (aspirational ceiling) → V-02 vs V-01 (C-01 completeness delta) → V-04 (register effect on feedback item specificity).
.

---

## V-01: Baseline

Axis: Baseline — skill description as written, no structural modifications
Hypothesis: Satisfies all 5 essential criteria (C-01 through C-05) but underperforms on A-01
(persona-specific revision recs for NPS < 6) and A-02 (NPS sensitivity analysis) because neither
is explicitly prompted; R-01 blocking escalation may appear inline rather than as a dedicated section.

```
You are running /listen:feedback. Simulate customer reactions to the spec or design for {{Topic}}
before it ships.

SETUP:
Read the input signal for {{Topic}} — the relevant spec, proposal, or design artifact.
Understand what the feature does, what it asks of users, and what decisions it embeds.

STOCK PERSONAS:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

PERSONA FEEDBACK CARDS:
For each persona C-01 through C-12, produce a feedback card in this format:

[C-NN] [Name] ([Role])
NPS: [1-10] — [1-2 sentences connecting this persona's context, goals, or anxieties to the
score. Do not restate the number — explain what about the spec produced this reaction.]

Feedback items (list each separately):
- [severity: blocking | major | minor | cosmetic] [feedback item text]
- (repeat for each item; zero items is valid if the persona has no objections)

All 12 cards required before proceeding to any aggregate section.

THEME MATRIX:
After all 12 cards, build a cross-persona theme matrix mapping recurring themes to the personas
that raised them. Format as a table or tagged list — either passes. Minimum one theme required.
Include the highest severity level raised under each theme.

| Theme | Personas | Highest Severity |
|-------|----------|-----------------|
| [theme name] | [C-NN, C-NN, ...] | [blocking / major / minor / cosmetic] |

BLOCKING ITEMS:
List every feedback item tagged `blocking` across all 12 cards in a dedicated section.
Format: [C-NN] [Name] — [blocking item text]
If no blocking items exist across all cards, state: "No blocking items."

PM READ:
Synthesize a 2-3 sentence read from a PM lens: what does this feedback pattern mean for
scope decisions, prioritization, and launch readiness? PM reads do not affect aggregate NPS.

UX READ:
Synthesize a 2-3 sentence read from a UX lens: what does the severity distribution and feedback
content reveal about the design's usability and the user's mental model fit?

AGGREGATE NPS:
Compute the mean of all 12 persona NPS scores. Show the calculation.
State explicitly: threshold is 7.0 (>= 7.0 passes).
If aggregate NPS >= 7.0: state "Threshold met. Spec may proceed."
If aggregate NPS < 7.0: state "Threshold not met. Spec requires revision before proceeding."

Write artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input, aggregate_nps: [value],
threshold_met: [true/false].
```

---

## V-02: Scorecard-first output format

Axis: Output format — NPS scorecard table built for all 12 personas before any feedback prose
Hypothesis: Scorecard-first format forces C-01 (all 12 personas present with NPS) and C-04
(threshold check visible as a single computation rather than buried at the end) before the model
can write any per-card feedback; low-NPS entries in the table naturally anchor which cards deserve
the deepest feedback and revision recs.

```
You are running /listen:feedback. The NPS scorecard comes first — all 12 personas are scored
and the aggregate threshold checked before any per-persona feedback prose is written.

SETUP:
Read the input signal for {{Topic}} — the relevant spec, proposal, or design artifact.

STOCK PERSONAS:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

STEP 1: NPS SCORECARD
Build this table first. All 12 rows required. Do not write any feedback cards until
every row has an NPS score and a one-sentence rationale.

| ID   | Name            | Role        | NPS [1-10] | One-sentence rationale                          |
|------|-----------------|-------------|------------|-------------------------------------------------|
| C-01 | Maria Chen      | Maker       | [score]    | [grounded in role/goals/anxieties]              |
| C-02 | James Okafor    | Builder     | [score]    | ...                                             |
| C-03 | Priya Nair      | Strategist  | [score]    | ...                                             |
| C-04 | Tom Bergstrom   | Operator    | [score]    | ...                                             |
| C-05 | Aisha Mensah    | Researcher  | [score]    | ...                                             |
| C-06 | Carlos Reyes    | Designer    | [score]    | ...                                             |
| C-07 | Lin Wei         | Analyst     | [score]    | ...                                             |
| C-08 | Sophie Dubois   | Manager     | [score]    | ...                                             |
| C-09 | Raj Patel       | Advocate    | [score]    | ...                                             |
| C-10 | Yuki Tanaka     | Evaluator   | [score]    | ...                                             |
| C-11 | Elena Vasquez   | Buyer       | [score]    | ...                                             |
| C-12 | Frank Hoffmann  | Regulator   | [score]    | ...                                             |
| AGG  | --              | --          | [mean]     | Threshold: >= 7.0 passes. State PASS or FAIL.   |

The aggregate row must be completed before proceeding. If FAIL, mark the table header
"REVISION REQUIRED" — the feedback cards that follow are revision inputs, not launch review.

STEP 2: FEEDBACK CARDS
Write feedback cards in ascending NPS order (lowest scorer first). This surfaces the highest-risk
personas before higher-scoring ones.

For each persona:
[C-NN] [Name] ([Role]) | NPS: [score]
Feedback items:
- [severity: blocking | major | minor | cosmetic] [feedback item text]
- (repeat; zero items valid for personas with no objections — state "No objections.")

For any persona with NPS < 6: include at least one revision recommendation — a specific,
actionable change to the spec that would raise their score. "Improve clarity" is not
actionable. Name the section, decision, or design choice that is the problem and what to do.

STEP 3: THEME MATRIX
After all cards, build the cross-persona theme matrix:

| Theme | Personas | Highest Severity |
|-------|----------|-----------------|
| [theme] | [C-NN, ...] | [blocking / major / minor / cosmetic] |

Minimum one theme required.

STEP 4: BLOCKING ITEMS
List every `blocking` severity item from all cards:
[C-NN] [Name] — [blocking item text]
If none: "No blocking items."

STEP 5: SUPPLEMENTAL READS
PM Read (2-3 sentences): scope, prioritization, and launch readiness signal from this feedback set.
UX Read (2-3 sentences): usability and mental model fit signal from the severity distribution.
Neither read affects the aggregate NPS.

Write artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input, output_format: scorecard-first,
aggregate_nps: [value], threshold_met: [true/false].
```

---

## V-03: Explicit lifecycle phases

Axis: Lifecycle emphasis — explicit phase gates enforce completeness at each step; ESCALATE
is a mandatory named phase rather than an implied formatting convention
Hypothesis: Separating SCORE (NPS only) from FEEDBACK (severity items) prevents NPS from being
buried in prose and forces C-04 threshold check before feedback is written; ESCALATE as a named
phase with an explicit zero-result option closes R-01 without relying on per-card formatting.

```
You are running /listen:feedback. The evaluation runs in five phases: READ, SCORE, FEEDBACK,
ESCALATE, SYNTHESIZE. Each phase completes before the next begins.

--- PHASE 1: READ ---

Read the input signal for {{Topic}} — the spec, proposal, or design artifact.
State in 1-2 sentences what the feature does and what decision or design it embeds.
This anchors every persona's reaction to the same artifact.

STOCK PERSONAS:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

--- PHASE 2: SCORE ---

For each persona C-01 through C-12, predict their NPS score only. No feedback items yet.
All 12 must be scored before Phase 3 begins.

[C-NN] [Name] ([Role])
NPS: [1-10] — [1-2 sentences: what about this spec, through this persona's lens, produces
this specific score? Ground the explanation in their role, workflow, or priorities.]

After all 12 scores, compute the aggregate:
  Aggregate NPS = sum of 12 scores / 12
  Threshold: >= 7.0

State explicitly:
  Aggregate NPS: [value]
  Result: PASS (>= 7.0) or FAIL (< 7.0)

If FAIL: the feedback in Phase 3 is revision input. If PASS: Phase 3 is refinement input.
Do not proceed to Phase 3 until all 12 scores and the aggregate result are stated.

--- PHASE 3: FEEDBACK ---

For each persona C-01 through C-12, write the feedback card. The NPS from Phase 2 is fixed —
do not change it here. Focus on the feedback items.

[C-NN] [Name] ([Role]) | NPS: [Phase 2 score]
Feedback items:
- [severity: blocking | major | minor | cosmetic] [specific feedback item]
- (repeat; zero items is valid — state "No feedback items." if the persona has no objections)

All 12 cards required before Phase 4.

--- PHASE 4: ESCALATE ---

This phase has two required outputs. Both require an explicit result.

BLOCKING ITEMS:
Collect every item tagged `blocking` from Phase 3 across all 12 cards.
List: [C-NN] [Name] — [blocking item text]
If no blocking items exist across all 12 cards: state "No blocking items."

LOW-NPS REVISION RECOMMENDATIONS:
For every persona with NPS < 6 from Phase 2, provide at least one actionable revision
recommendation — a specific change to the spec that would raise their score. Name the
section, decision, or design choice that is the problem. "Improve clarity" is not actionable.
Format: [C-NN] [Name] (NPS [score]) — Recommendation: [specific change]
If no persona scored below 6: state "No personas below NPS 6."

Both outputs required before Phase 5.

--- PHASE 5: SYNTHESIZE ---

THEME MATRIX:
Using the feedback items from Phase 3, build the cross-persona theme matrix. Map recurring
themes to the personas that raised them and annotate each theme with its highest severity.

| Theme | Personas | Highest Severity |
|-------|----------|-----------------|
| [theme] | [C-NN, ...] | [blocking / major / minor / cosmetic] |

Minimum one theme required. Themes should reflect actual feedback patterns, not generic categories.

PM READ:
2-3 sentences from a PM lens: what does this feedback pattern mean for scope, prioritization,
and launch readiness? Reference specific Phase 3 findings.

UX READ:
2-3 sentences from a UX lens: what does the severity distribution and Phase 3 feedback content
reveal about usability and mental model alignment?

Neither supplemental read affects the Phase 2 aggregate NPS.

Write artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input,
phases: [read, score, feedback, escalate, synthesize],
aggregate_nps: [value], threshold_met: [true/false].
```

---

## V-04: Conversational phrasing register

Axis: Phrasing register — question-framed, advisory session tone; descriptive rather than
imperative instruction style
Hypothesis: Asking "What would this persona think?" forces the model to reason through each
reaction rather than template-fill severity items; conversational framing produces richer
NPS justifications grounded in role and context, and more specific feedback item text because
the model is inhabiting the persona rather than evaluating against it.

```
You are running /listen:feedback. Work through this as a customer advisory panel that has
just been handed the spec for {{Topic}}. Twelve different people with twelve different contexts
are reading the same document. What do they think? What do they flag? Would they recommend this?

---

WHAT ARE WE REVIEWING?

Read the spec or design artifact for {{Topic}}. Understand what the feature does, what it
asks of the people using it, and what choices the team made that users will encounter directly.
Before you bring anyone into the room, make sure you know what you are showing them.

---

THE PANEL:

C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

---

WHAT DOES EACH PERSON THINK?

Take the panel through the spec one at a time. For each person, answer:

What would they flag as a problem — and how serious is it?

Write each piece of feedback as its own item. Tag the severity honestly:
- `blocking` — they cannot or will not use this as designed; the spec needs a change before
  they would engage
- `major` — a real concern that would meaningfully reduce their satisfaction or adoption
- `minor` — a friction point or preference; they would still use it
- `cosmetic` — a small thing; it does not affect behavior

It is fine if a person has no objections. State "No feedback items." and move on. Not every
panel member will have problems with every spec.

After listing their feedback, answer: on a scale of 1 to 10, how likely would they be to
recommend this feature to someone like them? Give the score and then explain why — in terms
of their role, their workflow, their concerns, or their priorities. The explanation should
say something that the score alone does not.

Do this for all twelve people. Do not skip anyone. Quiet panel members still have a voice —
even if it is a shrug or a thumbs-up, record it.

---

WHAT THEMES EMERGED?

After all twelve cards, step back and look across the feedback. What topics came up repeatedly?
Which personas agreed with each other — even if they came from different angles?

Map those themes to the people who raised them. For each theme, note the most serious severity
level anyone attached to it. A theme where two people flagged `blocking` issues is a different
kind of problem than a theme that only produced `minor` feedback.

| Theme | Who raised it | Most serious severity |
|-------|--------------|----------------------|
| [theme] | [C-NN, ...] | [blocking / major / minor / cosmetic] |

At least one theme is required. Generic observations ("some people liked it, some did not")
do not qualify — name what the issue actually was.

---

DID ANYONE FLAG A SHOWSTOPPER?

Collect every `blocking` item from every card. These are the things that have to change before
this feature is ready for the people who flagged them.

[C-NN] [Name] — [the blocking item, in their voice]

If no one flagged a blocking item across all twelve cards, say so plainly:
"No blocking items across the panel."

---

WHAT DOES THE PM SEE?

Write 2-3 sentences from a product manager's view: what does this feedback pattern tell you
about scope, sequencing, and whether the team should launch, iterate, or hold? Be specific
about what in the feedback is driving the recommendation.

---

WHAT DOES THE UX DESIGNER SEE?

Write 2-3 sentences from a designer's view: what does the severity distribution and the
content of the feedback say about how well the spec's design decisions match the way these
people actually think and work?

---

WOULD THE PANEL RECOMMEND IT?

Average the twelve NPS scores. Show the math. The threshold is 7.0 — at or above passes,
below means the spec needs revision before it ships.

State the result plainly:
"Aggregate NPS: [value]. Threshold: 7.0. [Met / Not met]."
If not met: "Spec requires revision before proceeding."

---

WHAT SHOULD CHANGE?

For any panel member who scored below 6, write at least one concrete revision recommendation.
Point to the specific section, decision, or design choice that produced their low score.
"Improve clarity" is not a recommendation — say exactly what to clarify, and how.

---

Write artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input, register: conversational,
aggregate_nps: [value], threshold_met: [true/false].
```

---

## V-05: Combined (severity-first sequencing + phase gates + NPS sensitivity)

Axis: Combined — lowest-NPS-first card ordering within a phased structure; inline [BLOCKING]
flags during the card loop; explicit NPS sensitivity analysis prompt in the final phase
Hypothesis: Surfacing the lowest-scoring personas first anchors revision priority before
higher-scoring cards can dilute attention; inline [BLOCKING] flags during Phase 2 make the
Phase 3 escalation section a verification pass rather than first-pass discovery; an explicit
sensitivity section in Phase 4 drives A-02 without naming the rubric criterion.

```
You are running /listen:feedback. Cards are written in ascending NPS order (worst-scoring
persona first). Blocking severity items are flagged inline during the card loop and then
escalated separately. The final phase includes an NPS sensitivity analysis.

--- PHASE 1: SCORE ---

Read the input signal for {{Topic}} — the spec, proposal, or design artifact.

STOCK PERSONAS:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

Assign a predicted NPS [1-10] to each persona. Do not write feedback items yet.
List all 12 with their score and a one-sentence rationale. Order the list by NPS ascending
(lowest score first). If scores are tied, order by persona ID.

After all 12 scores:
  Aggregate NPS = sum / 12. Show the calculation.
  Threshold: >= 7.0.
  State: "Aggregate NPS: [value]. Result: PASS / FAIL."
  If FAIL: append "REVISION REQUIRED" — Phase 2 cards are revision input.

Do not proceed to Phase 2 until all 12 scores, their ascending-order list, and the aggregate
result are stated.

--- PHASE 2: FEEDBACK CARDS ---

Write feedback cards in the same ascending NPS order from Phase 1 (lowest scorer first).
This surfaces the highest-risk personas before higher-scoring ones.

For each persona:

[C-NN] [Name] ([Role]) | NPS: [Phase 1 score]
Feedback items:
- [severity: blocking | major | minor | cosmetic] [specific feedback item]
  If severity is `blocking`, append [BLOCKING] to the line.
- (repeat; zero items valid — state "No feedback items.")

For any persona with NPS < 6: include a REVISION REC immediately after their feedback items:
  Revision rec: [specific, actionable change — name the section, decision, or design choice
  and what to do differently. Not "improve clarity." Not "simplify the flow." Name the thing.]

All 12 cards required, in ascending NPS order, before Phase 3.

--- PHASE 3: ESCALATE ---

Both outputs required. Both require an explicit result.

BLOCKING ITEMS:
Collect every line marked [BLOCKING] from Phase 2.
List: [C-NN] [Name] (NPS [score]) — [blocking item text]
If no [BLOCKING] lines exist across all 12 cards: state "No blocking items."

REVISION RECS SUMMARY:
Collect every revision rec from Phase 2 (NPS < 6 personas).
List: [C-NN] [Name] (NPS [score]) — [revision rec]
If no persona scored below 6: state "No personas below NPS 6."

Both outputs must have explicit results before Phase 4.

--- PHASE 4: SYNTHESIZE ---

THEME MATRIX:
Build the cross-persona theme matrix from the Phase 2 feedback items. Map recurring themes
to the personas that raised them. Annotate each theme with its highest severity across
all personas that raised it.

| Theme | Personas | Highest Severity |
|-------|----------|-----------------|
| [theme] | [C-NN, ...] | [blocking / major / minor / cosmetic] |

Minimum one theme required.

PM READ:
2-3 sentences from a PM lens: what does this feedback pattern signal for scope, prioritization,
and launch readiness? Reference specific Phase 2 findings.

UX READ:
2-3 sentences from a UX lens: what does the severity distribution and feedback content reveal
about design fit and mental model alignment?

NPS SENSITIVITY ANALYSIS:
Identify the 2-3 personas whose scores most influence the aggregate NPS. These are the
leverage personas — the ones where a single spec change could move the aggregate the most.
For each:
  [C-NN] [Name] — NPS: [score] — Why leverage: [why this persona's score has outsized aggregate
  impact — low base, representative of a cluster, or addressable with a single change]
  Highest-ROI change: [the one spec change most likely to raise their score and move the aggregate]

Then state: "Single highest-ROI change across all personas: [change] — estimated aggregate NPS
lift: ~[delta], moving from [current] to approximately [projected]."

Write artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input,
sequence: ascending-nps, phases: [score, feedback, escalate, synthesize],
aggregate_nps: [value], threshold_met: [true/false].
```
