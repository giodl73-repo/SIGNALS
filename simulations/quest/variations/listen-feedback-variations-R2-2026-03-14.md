Written to `simulations/quest/variations/listen-feedback-variations-R2-2026-03-14.md`.

---

## listen-feedback R2 — 5 Variations

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Inertia framing | Status-quo comparison grounds NPS in switching cost vs. net benefit; more discriminating scores, adoption-blocking objections surface |
| V-02 | Role sequence (PM/UX-first) | PM + UX set the evaluation frame before persona cards; tests anchoring vs. independent-insight tradeoff |
| V-03 | Severity-first within-card format | Simpler path to A-03 than V-05 R1 — no ascending NPS order, no phase gates required |
| V-04 | Compressed format | Minimum viable prompt; identifies which instructions are load-bearing vs. scaffolding |
| V-05 | Combined ceiling (all patterns + inertia) | V-05 R1 + inertia framing + severity-first within cards; expected 115/115 |

---

**Rubric v2 coverage by variation:**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|:----:|:----:|:----:|:----:|:----:|
| C-01 through C-05, R-01 through R-03, A-01 | ✓ | ✓ | ✓ | ✓* | ✓ |
| A-02 NPS sensitivity | ✗ | ✗ | ✗ | ✗ | ✓ |
| A-03 Inline [BLOCKING] | ✗ | ✗ | **✓** | ✗ | ✓ |
| A-04 Ascending NPS | ✗ | ✗ | ✗ | ✗ | ✓ |
| A-05 Two-pass recs | ✗ | ✗ | ✗ | ✗ | ✓ |
| **Score** | **95** | **95** | **100** | **95*** | **115** |

*V-04: compliance rate test — compressed instructions may drop essential criteria in practice.

**Key structural bets:**

- **V-01** is the first clean test of inertia framing. Identical score prediction to V-01 R1, but feedback item quality should be meaningfully higher — objections are anchored to what personas actually do today.

- **V-03** is the most interesting single-axis variation: it reaches A-03 through a single format rule (severity descending within cards, `[BLOCKING]` inline) without needing ascending NPS ordering or phase gates. If it passes A-03 reliably, that's a simpler path to 100 than V-05 R1.

- **V-05** combines inertia framing with all V-05 R1 patterns. The new hypothesis: does inertia context plus severity-first make `[BLOCKING]` items appear at two structural checkpoints per card (top-of-card via severity-first, plus inline tag), making A-03 more reliable than either technique alone?

**Recommended scoring order:** V-04 → V-03 → V-01 → V-02 → V-05.
sses any essential criterion, that identifies the specific instruction that is load-bearing.

**Predicted scoring:**

| Variation | Expected score | Differentiator |
|-----------|---------------|----------------|
| V-05 | 115 | All five aspirational criteria active |
| V-03 | 100 | A-03 via severity-first; misses A-02/A-04/A-05 |
| V-01 | 95 | A-01 present; inertia framing improves quality not structure |
| V-02 | 95 | A-01 present; PM/UX-first tests role sequence, not aspirational depth |
| V-04 | 95 | A-01 present in parenthetical; other aspirational criteria absent |

---

## V-01: Inertia framing

Axis: Inertia framing — every persona reacts from their current workflow; NPS reflects net
benefit over the status quo rather than feature satisfaction in isolation
Hypothesis: Status-quo grounding produces more discriminating NPS scores and surfaces
switching-cost objections (adoption blockers) that abstract evaluation misses. Even if
structural score matches V-01 R1, feedback item quality — specificity of blocking and major
items — should be higher because each objection is anchored in a concrete current behavior.

```
You are running /listen:feedback. Simulate customer reactions to the spec or design for {{Topic}}
before it ships. Every persona evaluates from their current workflow — what they do today in
the area this feature addresses. NPS reflects net benefit over the status quo, not just feature
satisfaction in isolation.

SETUP:
Read the input signal for {{Topic}} — the relevant spec, proposal, or design artifact.
State in 1-2 sentences: what current workflow, tool, or behavior does this feature change or
replace? This is the inertia baseline that every persona reaction is grounded against.

STOCK PERSONAS:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

PERSONA FEEDBACK CARDS:
For each persona C-01 through C-12, produce a feedback card in this format:

[C-NN] [Name] ([Role])
Status quo: [1 sentence — what this persona currently does in the area this feature addresses]
NPS: [1-10] — [1-2 sentences: does this feature beat their status quo? What is the switching
cost vs. the net benefit? Ground the score in the comparison, not the feature in isolation.]

Feedback items:
- [severity: blocking | major | minor | cosmetic] [feedback item text]
- (repeat for each item; zero items valid — state "No feedback items.")

For any persona with NPS < 6: include a revision recommendation immediately after their items:
  Revision rec: [specific, actionable change — name the section, decision, or design choice
  that is causing the low score and what to change. Not "improve clarity."]

All 12 cards required before any aggregate section.

THEME MATRIX:
After all 12 cards, build a cross-persona theme matrix. For each theme, note whether it is
inertia-driven (switching cost, loss of current capability, migration friction) or a net-new
objection to the spec as designed.

| Theme | Personas | Highest Severity |
|-------|----------|-----------------|
| [theme] | [C-NN, ...] | [blocking / major / minor / cosmetic] |

Minimum one theme required.

BLOCKING ITEMS:
List every feedback item tagged `blocking` across all 12 cards.
Format: [C-NN] [Name] — [blocking item text]
If no blocking items exist: "No blocking items."

PM READ:
2-3 sentences: what does this feedback pattern — particularly the inertia objections and
switching-cost blockers — signal for adoption strategy, migration scope, and launch readiness?

UX READ:
2-3 sentences: what does the severity distribution reveal about design fit and whether the
spec reduces switching friction sufficiently for the personas who rated it low?

AGGREGATE NPS:
Compute the mean of all 12 persona NPS scores. Show the calculation.
Threshold: >= 7.0.
State explicitly: "Aggregate NPS: [value]. Threshold: 7.0. [Met / Not met]."
If below 7.0: "Spec requires revision before proceeding."

Write artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input, framing: inertia,
aggregate_nps: [value], threshold_met: [true/false].
```

---

## V-02: PM/UX-first role sequence

Axis: Role sequence — PM and UX reads precede all persona cards rather than following them
Hypothesis: Pre-framing the session with professional synthesis (PM: scope and prioritization
lens; UX: design decision and mental model lens) before persona reactions may anchor persona
cards toward higher-signal design-level objections rather than shallow preference complaints.
The counterhypothesis: PM/UX framing anchors persona scores toward what the professional
reviewers noticed, suppressing genuine persona-specific insights that surface independently.
Either outcome is informative about the interaction between role sequence and output quality.

```
You are running /listen:feedback. The PM and UX reads come first — professional synthesis
before customer reactions. PM and UX set the evaluation frame; the 12 customer personas then
react to the same artifact through their own lens.

SETUP:
Read the input signal for {{Topic}} — the relevant spec, proposal, or design artifact.
Understand what the feature does, what it asks of users, and what design decisions it embeds.

STOCK PERSONAS:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

STEP 1: PM READ (pre-persona)
Write 2-3 sentences from a PM lens before any persona cards.
What is this spec committing the team to? What audience decisions are embedded in it?
What would a high-NPS outcome look like for this feature vs. a low-NPS outcome — what is the
spec betting on? PM reads do not affect aggregate NPS.

STEP 2: UX READ (pre-persona)
Write 2-3 sentences from a UX lens before any persona cards.
What design choices does this spec make that users will encounter directly?
Where are the seams between the design's assumptions and how these personas actually work?
UX reads do not affect aggregate NPS.

STEP 3: PERSONA FEEDBACK CARDS
For each persona C-01 through C-12, produce a feedback card:

[C-NN] [Name] ([Role])
NPS: [1-10] — [1-2 sentences connecting this persona's context, goals, or anxieties to the
score. Ground the score in their specific role — do not echo the PM or UX read.]

Feedback items:
- [severity: blocking | major | minor | cosmetic] [feedback item text]
- (repeat; zero items valid — state "No feedback items.")

For any persona with NPS < 6: include a revision recommendation immediately after their items:
  Revision rec: [specific, actionable change — name the section, decision, or design choice]

All 12 cards required before any aggregate section.

STEP 4: THEME MATRIX
After all 12 cards:

| Theme | Personas | Highest Severity |
|-------|----------|-----------------|
| [theme] | [C-NN, ...] | [blocking / major / minor / cosmetic] |

Minimum one theme. Note whether themes were anticipated by the PM/UX reads in STEP 1/2 or
emerged independently from persona reactions.

STEP 5: BLOCKING ITEMS
List every `blocking` item from all 12 cards:
[C-NN] [Name] — [blocking item text]
If no blocking items: "No blocking items."

STEP 6: AGGREGATE NPS
Compute the mean of all 12 persona NPS scores. Show the calculation.
Threshold: >= 7.0.
State: "Aggregate NPS: [value]. Threshold: 7.0. [Met / Not met]."
If below 7.0: "Spec requires revision before proceeding."

Write artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input, role_sequence: pm-ux-first,
aggregate_nps: [value], threshold_met: [true/false].
```

---

## V-03: Severity-first within-card format

Axis: Output format — within each persona card, feedback items are listed in descending
severity order (blocking first, then major, minor, cosmetic); blocking items additionally
carry an inline [BLOCKING] flag
Hypothesis: Severity-first ordering within cards is a simpler structural path to A-03 than
the V-05 R1 phased approach. V-05 required: ascending NPS ordering (Phase 1), explicit
[BLOCKING] inline format directive, and a dedicated ESCALATE phase gate. V-03 achieves
A-03 through a single format rule applied within each card — blocking items naturally surface
at the top, making the escalation section a mechanical collection pass. Tests whether the
[BLOCKING] flag can be reliably generated without phase gates or ascending NPS ordering.

```
You are running /listen:feedback. Within each persona card, feedback items are listed in
descending severity order — blocking first, then major, minor, cosmetic. Blocking-severity
items carry an inline [BLOCKING] flag.

SETUP:
Read the input signal for {{Topic}} — the relevant spec, proposal, or design artifact.
Understand what the feature does and what design decisions it embeds.

STOCK PERSONAS:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

PERSONA FEEDBACK CARDS:
For each persona C-01 through C-12, produce a feedback card. List feedback items in
descending severity: blocking first, then major, then minor, then cosmetic. Only include
severity levels that have items.

[C-NN] [Name] ([Role])
NPS: [1-10] — [1-2 sentences connecting this persona's context, goals, or anxieties to the
score. Do not restate the number — explain what about the spec produced this reaction.]

Feedback items (descending severity — blocking first):
- blocking: [feedback item text] [BLOCKING]
- major: [feedback item text]
- minor: [feedback item text]
- cosmetic: [feedback item text]
(Zero items valid — state "No feedback items.")

For any persona with NPS < 6: include a revision recommendation immediately after their items:
  Revision rec: [specific, actionable change — name the section, decision, or design choice.
  Not "improve clarity." Name the thing and what to do.]

All 12 cards required before any aggregate section.

THEME MATRIX:
After all 12 cards, build the cross-persona theme matrix:

| Theme | Personas | Highest Severity |
|-------|----------|-----------------|
| [theme] | [C-NN, ...] | [blocking / major / minor / cosmetic] |

Minimum one theme required.

BLOCKING ITEMS:
Collect every item marked [BLOCKING] from the 12 cards. Because blocking items appear at the
top of each card (severity-first ordering), this section is a verification pass — scan each
card's first item(s), collect what is tagged.

List: [C-NN] [Name] — [blocking item text]
If no [BLOCKING] items exist across all cards: "No blocking items."

PM READ:
2-3 sentences: what does the severity distribution — particularly the count and distribution
of blocking and major items — signal for scope, prioritization, and launch readiness?

UX READ:
2-3 sentences: what do the leading (blocking/major) feedback items across personas reveal
about design fit and mental model alignment?

AGGREGATE NPS:
Compute the mean of all 12 persona NPS scores. Show the calculation.
Threshold: >= 7.0.
State: "Aggregate NPS: [value]. Threshold: 7.0. [Met / Not met]."
If below 7.0: "Spec requires revision before proceeding."

Write artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input, card_format: severity-first,
aggregate_nps: [value], threshold_met: [true/false].
```

---

## V-04: Compressed format

Axis: Output format (compression) — all essential and recommended criteria satisfied with
minimum prompting; no phase headers, no extended anti-pattern guidance, maximum structural
density
Hypothesis: Identifies which instructions are load-bearing vs. redundant scaffolding. If V-04
passes all essential + recommended criteria at the same rate as elaborated variations, the
extra instructional text in other variations is defensiveness, not necessity. If V-04 drops
any essential criterion, that identifies the specific instruction whose absence causes failure.
A-01 appears in a parenthetical and is expected to be less reliable than in fully scaffolded
variations; A-02 through A-05 are absent.

```
You are running /listen:feedback for {{Topic}}.

Read the input spec or design artifact.

PERSONAS:
C-01 Maria Chen (Maker), C-02 James Okafor (Builder), C-03 Priya Nair (Strategist),
C-04 Tom Bergstrom (Operator), C-05 Aisha Mensah (Researcher), C-06 Carlos Reyes (Designer),
C-07 Lin Wei (Analyst), C-08 Sophie Dubois (Manager), C-09 Raj Patel (Advocate),
C-10 Yuki Tanaka (Evaluator), C-11 Elena Vasquez (Buyer), C-12 Frank Hoffmann (Regulator).

CARDS — all 12 required:

[C-NN] [Name] ([Role])
NPS: [1-10] — [justification grounded in persona role, goals, or anxieties]
- [severity: blocking | major | minor | cosmetic] [feedback item]
(Zero items valid. NPS < 6: add "Revision rec: [specific, actionable change].")

THEME MATRIX (after all 12 cards):
| Theme | Personas | Highest Severity |
Minimum one theme required.

BLOCKING ITEMS:
List all blocking-severity items from all 12 cards.
[C-NN] [Name] — [item]
If none: "No blocking items."

PM READ: 2-3 sentences, scope/prioritization/launch readiness.
UX READ: 2-3 sentences, usability/mental-model-fit.
(Neither affects aggregate NPS.)

AGGREGATE NPS:
Mean of 12 scores. Show calculation.
Threshold: >= 7.0.
State: "Aggregate NPS: [value]. Threshold: 7.0. [Met / Not met]."
If below 7.0: "Spec requires revision before proceeding."

Write artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input, format: compressed,
aggregate_nps: [value], threshold_met: [true/false].
```

---

## V-05: Combined ceiling (all patterns + inertia framing + severity-first within cards)

Axis: Combined — V-05 R1 structure (ascending NPS ordering, inline [BLOCKING], two-pass
revision recs, NPS sensitivity analysis) plus inertia framing (status-quo comparison grounds
NPS) plus severity-first within-card ordering (blocking items at top of each card)
Hypothesis: The highest-ceiling variation; should score 115/115 against v2 rubric. Inertia
framing improves feedback item specificity (objections are anchored in concrete current
behavior, not abstract preference). Severity-first within cards reinforces A-03: blocking
items appear at both the top of each card AND in the escalation section, giving two structural
checkpoints for verification. Tests whether combining inertia context with phased structure
introduces ordering conflicts or instruction ambiguity.

```
You are running /listen:feedback. Cards are written in ascending NPS order (lowest scorer
first). Within each card, feedback items are listed in descending severity (blocking first).
Every NPS score is grounded in status-quo comparison. Blocking items are flagged inline and
escalated separately. The final phase includes NPS sensitivity analysis.

--- PHASE 1: SCORE ---

Read the input signal for {{Topic}} — the spec, proposal, or design artifact.
State in 1-2 sentences: what current workflow or approach does this feature change or replace?
This is the inertia baseline. Every NPS score is a comparison against it.

STOCK PERSONAS:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

For each persona, state:
- Status quo: [1 sentence — what they currently do in this area]
- NPS: [1-10]
- Rationale: [1 sentence grounding the score in status-quo comparison — does this feature
  beat what they do today? What is the switching cost vs. the net benefit?]

List all 12 in ascending NPS order (lowest first). Tied scores: order by persona ID.

After all 12:
  Aggregate NPS = sum / 12. Show calculation.
  Threshold: >= 7.0.
  State: "Aggregate NPS: [value]. Result: PASS / FAIL."
  If FAIL: append "REVISION REQUIRED."

Do not proceed to Phase 2 until all 12 scores, their ascending-order list, and the aggregate
result are stated.

--- PHASE 2: FEEDBACK CARDS ---

Write feedback cards in the same ascending NPS order from Phase 1 (lowest scorer first).
Within each card, list feedback items in descending severity: blocking first, then major,
minor, cosmetic. Only include severity levels that have items.

[C-NN] [Name] ([Role]) | NPS: [Phase 1 score]
Feedback items (descending severity — blocking first):
- blocking: [feedback item text] [BLOCKING]
- major: [feedback item text]
- minor: [feedback item text]
- cosmetic: [feedback item text]
(Zero items valid — state "No feedback items.")

For any persona with NPS < 6: include a REVISION REC immediately after their feedback items:
  Revision rec: [specific, actionable change — name the section, decision, or design choice
  and what to change. Not "improve clarity." Not "simplify the flow." Name the thing.]

All 12 cards required, in ascending NPS order, before Phase 3.

--- PHASE 3: ESCALATE ---

Both outputs required. Both require an explicit result.

BLOCKING ITEMS:
Collect every item marked [BLOCKING] from Phase 2. Because blocking items appear at the top
of each card (severity-first ordering), this is a two-checkpoint verification: first item(s)
of each card, then the inline [BLOCKING] tag.

List: [C-NN] [Name] (NPS [score]) — [blocking item text]
If no [BLOCKING] items across all 12 cards: "No blocking items."

REVISION RECS SUMMARY:
Collect every REVISION REC from Phase 2 (NPS < 6 personas).
List: [C-NN] [Name] (NPS [score]) — [revision rec]
If no persona scored below 6: "No personas below NPS 6."

Both outputs complete before Phase 4.

--- PHASE 4: SYNTHESIZE ---

THEME MATRIX:
Build the cross-persona theme matrix from Phase 2 feedback. Annotate each theme with its
highest severity. Note whether themes are inertia-driven (switching cost, status-quo loss,
migration friction) or net-new objections to the spec as designed.

| Theme | Personas | Highest Severity |
|-------|----------|-----------------|
| [theme] | [C-NN, ...] | [blocking / major / minor / cosmetic] |

Minimum one theme required.

PM READ:
2-3 sentences: what does this feedback pattern — including inertia objections — signal for
adoption strategy, scope decisions, and launch readiness? Reference specific Phase 2 findings.

UX READ:
2-3 sentences: what does the severity distribution and Phase 2 content reveal about design
fit, mental model alignment, and switching friction reduction?

NPS SENSITIVITY ANALYSIS:
Identify the 2-3 personas whose scores most influence the aggregate NPS. These are the
leverage personas — the ones where a single spec change could move the aggregate the most.

For each leverage persona:
  [C-NN] [Name] — NPS: [score] — Why leverage: [why this score has outsized aggregate impact:
  low base, representative of a cluster, or addressable with a single inertia-reducing change]
  Highest-ROI change: [the one spec change most likely to raise their score and move the aggregate]

State: "Single highest-ROI change: [change] — estimated aggregate NPS lift: ~[delta],
moving from [current] to approximately [projected]."

Write artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input,
framing: inertia, sequence: ascending-nps, card_format: severity-first,
phases: [score, feedback, escalate, synthesize],
aggregate_nps: [value], threshold_met: [true/false].
```

---

## Rubric v2 coverage map

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 All 12 personas | PASS | PASS | PASS | PASS* | PASS |
| C-02 Severity tags | PASS | PASS | PASS | PASS* | PASS |
| C-03 NPS with justification | PASS | PASS | PASS | PASS* | PASS |
| C-04 Aggregate NPS + threshold | PASS | PASS | PASS | PASS* | PASS |
| C-05 Theme matrix | PASS | PASS | PASS | PASS | PASS |
| R-01 Blocking escalated | PASS | PASS | PASS | PASS | PASS |
| R-02 PM and UX reads | PASS | PASS | PASS | PASS | PASS |
| R-03 Theme matrix with severity | PASS | PASS | PASS | PASS | PASS |
| A-01 Revision recs NPS < 6 | PASS | PASS | PASS | PASS* | PASS |
| A-02 NPS sensitivity analysis | FAIL | FAIL | FAIL | FAIL | PASS |
| A-03 Inline [BLOCKING] flags | FAIL | FAIL | PASS | FAIL | PASS |
| A-04 Ascending NPS ordering | FAIL | FAIL | FAIL | FAIL | PASS |
| A-05 Two-pass revision recs | FAIL | FAIL | FAIL | FAIL | PASS |
| **Score** | **95** | **95** | **100** | **95*** | **115** |

*V-04 compressed format: essential criteria are present but structural enforcement is weaker.
Actual scores may drop if a run fails C-01 (model stops before all 12) or C-04 (threshold
statement omitted). V-04's purpose is to test compliance rate, not just prompt structure.

---

## Recommended scoring order

V-04 first (minimum viable baseline — establishes which essential criteria need structural
enforcement) → V-03 (A-03 via severity-first alone — single path test) → V-01 (inertia
framing quality delta — same score as V-01 R1 expected but feedback item specificity higher)
→ V-02 (PM/UX-first anchoring effect on persona reactions — qualitative comparison to V-02 R1)
→ V-05 (ceiling — all patterns active; inertia + severity-first interaction test).
