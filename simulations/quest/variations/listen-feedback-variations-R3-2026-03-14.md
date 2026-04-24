---

## listen-feedback R3 — 5 Variations

| # | Axis | Hypothesis |
|---|------|------------|
| V-01 | Phrasing register (conversational) | Same content as R2 V-01, natural prose register — tests if formal imperative is load-bearing for A-03/A-07 reliability |
| V-02 | NPS categories (detractor/passive/promoter) | Named bands anchor A-06 structurally: "Detractor = switching cost > benefit" forces an inertia comparison by category definition |
| V-03 | Per-card inline inertia (no global SETUP) | Named `Current approach:` field in card template achieves A-06 without a global baseline sentence; tests if per-card embedding is sufficient |
| V-04 | Declarative sort rule (A-07 via rule, not template) | "Sort by severity descending" instruction vs. demonstrated template; tests if the template is structurally required for A-07 compliance |
| V-05 | Combined ceiling (phases + categories + named field) | R2 V-05 phase structure + NPS category bands + `Current approach:` card field; two new patterns targeting 125/125 |

---

**Predicted scores against v3 rubric (125 max):**

| Variation | Score | Differentiator |
|-----------|-------|----------------|
| V-05 | 125 | First 125 attempt; all 7 aspirational active |
| V-01 | 110* | A-06 + A-07 structurally present; reliability concern in conversational register |
| V-02 | 110 | A-06 via category definition; A-07 via template; misses A-02/A-04/A-05 |
| V-03 | 110 | A-06 via `Current approach:` field; cleaner per-card specificity |
| V-04 | 100 | A-07 compliance TBD; if declarative rule fails A-07, drops to 95 |

**Key structural bets:**
- **V-03 vs. V-02** both predict 110 via different A-06 paths — the winner tells us whether per-card named fields or category definitions produce more reliable inertia comparisons
- **V-04** is the critical infrastructure test: if declarative sort fails A-07, the R2 template demonstration is confirmed as load-bearing and all future high-ceiling prompts must include it
- **V-05** introduces two new patterns: `nps-category-bands-with-aggregate-mean` (category label per card, mean for threshold) and `named-current-approach-field-in-phase-card` (Phase 2 card template has `Current approach:` as a named field, doubling A-06 enforcement alongside Phase 1's inertia baseline)

**Recommended scoring order:** V-04 → V-03 → V-02 → V-01 → V-05.
ia, no severity-first). V-01 R3 carries the full content of R2 V-01 — inertia baseline, A-01 revision recs, A-06/A-07 — written conversationally. The test: does formal imperative register improve *reliability* of structural compliance, or just *legibility*?

- **V-02** is the first NPS-category variation across any round. Named bands (detractor/passive/promoter) make the inertia comparison structurally required by definition — a detractor must explain why switching cost exceeds benefit. The aggregate still uses mean for the 7.0 threshold, but the category breakdown provides a supplemental adoption signal.

- **V-03** is the critical single-axis A-06 test: can a named `Current approach:` field in the card template replace a global SETUP section? If yes, A-06 is achievable with fewer words and no preamble overhead. Implication: future combined prompts can embed A-06 directly in the card format without needing a dedicated setup phase.

- **V-04** is the critical single-axis A-07 test: can a declarative "sort by severity descending" rule achieve the same structural compliance as a template that demonstrates the order? V-03 R2 proved the template works. V-04 R3 tests whether the template is necessary or the rule suffices.

- **V-05** combines R2 V-05's proven phase structure with two new patterns from R3: NPS category bands (V-02) and a named `Current approach:` field (V-03). Prediction: 125/125. New patterns captured: `nps-category-bands-with-aggregate-mean` and `named-current-approach-field-in-phase-card`.

**Recommended scoring order:** V-04 → V-03 → V-02 → V-01 → V-05.

**Predicted scoring:**

| Variation | Expected score | Differentiator |
|-----------|---------------|----------------|
| V-05 | 125 | All 7 aspirational criteria; first 125 output |
| V-01 | 110 | A-06 + A-07 both present; A-03 reliability concern |
| V-02 | 110 | A-06 via category definition; A-07 via template |
| V-03 | 110 | A-06 via `Current approach:` field; no global setup |
| V-04 | 100 | A-07 reliability TBD; declarative sort may not hold |

---

## V-01: Phrasing register (conversational)

Axis: Phrasing register — all structural requirements expressed in natural, flowing prose rather
than imperative section headers and explicit templates. Section titles become paragraph transitions;
templates become descriptions of what each element "should include."
Hypothesis: Formal imperative register may be structurally load-bearing for A-03 (inline
[BLOCKING] tags) and A-07 (severity-first within cards), since these rely on the model following
an explicit output template precisely. A conversational register may produce lower structural
reliability for format-sensitive criteria even when all requirements are described. Tests whether
R2 V-01's 95-point output depends on the phrasing register or just the presence of the
instructions. Content matched to R2 V-01 plus A-07 (severity-first) for a direct comparison.

```
You are running /listen:feedback for {{Topic}}. Before this spec ships, simulate how your 12
customer personas would react to it. Every persona evaluates from their own context — and every
NPS score reflects whether this feature beats what they already do.

Start by reading the input signal for {{Topic}}: the relevant spec, proposal, or design artifact.
Before writing any cards, name the inertia baseline in a sentence or two: what current workflow,
tool, or behavior does this feature change or replace? This framing grounds every persona reaction
that follows.

Your stock cast of 12:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

Write a feedback card for each of the 12 personas — all 12, in this order, before any summary
sections. Each card should open with the persona ID, name, and role, then give their NPS score
(1 through 10) with a sentence or two explaining it. The explanation should directly compare this
feature against the inertia baseline you named above: does it beat what they do today? Is the
switching cost worth the net benefit? That comparison is the justification — describing the
persona's preferences alone is not enough.

For each persona's feedback items, list them in descending severity — blocking concerns first,
then major, then minor, then cosmetic. Only include severity levels that actually have items.
Each item carries its severity label. Any blocking-severity item also carries a [BLOCKING] marker
inline — this makes the escalation section at the end a collection pass, not a first-pass search.
If a persona has no feedback items at all, say so explicitly.

For any persona whose NPS falls below 6, include a revision recommendation right after their
feedback items. The recommendation should name the specific section, decision, or design choice
that is causing the low score, and say what to change. "Improve clarity" or "simplify the flow"
don't count — name the thing.

Once all 12 cards are written, look across them for recurring themes. Build a cross-persona theme
matrix: for each theme, note which personas raised it and the highest severity level it reached.
Identify whether the theme is driven by switching friction and loss of current capability, or
whether it is a net-new objection to the spec as designed.

Collect all [BLOCKING] items from the 12 cards into a dedicated section. Because blocking items
appear at the top of each card (severity-first ordering), this is a scan of each card's leading
items for the inline marker. If no blocking items exist anywhere, say so.

Include a PM read (2-3 sentences on adoption strategy, switching-cost blockers, and launch
readiness in light of what the feedback shows) and a UX read (2-3 sentences on design fit and
whether the spec reduces switching friction enough for the personas who scored it low). Neither
the PM read nor the UX read contributes to aggregate NPS.

Finally, compute the aggregate NPS as the mean of all 12 persona scores. Show the arithmetic.
The threshold is 7.0. State the result explicitly: "Aggregate NPS: [value]. Threshold: 7.0.
[Met / Not met]." If the aggregate falls below 7.0, flag the spec as requiring revision before
proceeding.

Write the artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input, register: conversational,
framing: inertia, aggregate_nps: [value], threshold_met: [true/false].
```

---

## V-02: NPS categories (detractor/passive/promoter)

Axis: Output format — NPS expressed in named bands (detractor 1-6, passive 7-8, promoter 9-10)
with band definitions anchored in inertia comparison. Severity-first template retained from R2
V-03. Aggregate still computed as mean for threshold test; category breakdown is supplemental.
Hypothesis: Named NPS bands make the inertia framing structurally required by definition —
a detractor score mandates explaining why switching cost exceeds net benefit; a promoter score
mandates identifying the net gain that overcomes friction. This achieves A-06 through the category
definition rather than a separate "compare to status quo" instruction. Also tests whether the
category label (Detractor/Passive/Promoter) in the card header adds a useful adoption-readiness
signal above the raw numeric score.

```
You are running /listen:feedback. Simulate customer reactions to the spec or design for {{Topic}}
before it ships. NPS scores use standard bands: Detractor (1-6), Passive (7-8), Promoter (9-10).
A Detractor score means the switching cost from their current approach exceeds the net benefit.
A Promoter score means the net benefit is clear enough to overcome switching friction.

SETUP:
Read the input signal for {{Topic}} — the relevant spec, proposal, or design artifact.
State in 1-2 sentences: what current workflow, tool, or behavior does this feature change or
replace? This is the inertia baseline that every NPS score is a comparison against.

STOCK PERSONAS:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

PERSONA FEEDBACK CARDS:
For each persona C-01 through C-12, produce a feedback card in this format:

[C-NN] [Name] ([Role])
NPS: [1-10] ([Detractor | Passive | Promoter]) — [1-2 sentences: what makes this a Detractor/
Passive/Promoter score for this persona? State the comparison: does this feature beat their
current approach? What is the net benefit vs. the switching cost from the inertia baseline?]

Feedback items (descending severity — blocking first):
- blocking: [feedback item text] [BLOCKING]
- major: [feedback item text]
- minor: [feedback item text]
- cosmetic: [feedback item text]
(Only include severity levels that have items. Zero items valid — state "No feedback items.")

For any persona with NPS < 6 (Detractor): include a revision recommendation immediately after
their items:
  Revision rec: [specific, actionable change — name the section, decision, or design choice
  and what to change. Not "improve clarity." Name the thing.]

All 12 cards required before any aggregate section.

CATEGORY SUMMARY (after all 12 cards):
Count personas per band:
  Promoters (9-10): [count] — [persona IDs]
  Passives (7-8): [count] — [persona IDs]
  Detractors (1-6): [count] — [persona IDs]

Note the dominant Detractor objection pattern — what switching-cost or inertia issue drove the
most Detractor scores?

THEME MATRIX:
| Theme | Personas | Highest Severity |
|-------|----------|-----------------|
| [theme] | [C-NN, ...] | [blocking / major / minor / cosmetic] |

Classify each theme as: inertia-driven (switching cost, capability loss, migration friction) or
spec-specific (net-new design objection). Minimum one theme required.

BLOCKING ITEMS:
Collect every item marked [BLOCKING] from the 12 cards. Because blocking items appear at the
top of each card (severity-first ordering), this is a verification pass over each card's leading
feedback item(s).

List: [C-NN] [Name] — [blocking item text]
If no [BLOCKING] items: "No blocking items."

PM READ:
2-3 sentences: what does the Detractor/Passive/Promoter distribution and the dominant inertia
objection pattern signal for adoption strategy, launch sequencing, and onboarding scope?

UX READ:
2-3 sentences: what does the severity distribution across Detractor cards reveal about design fit
and whether the spec reduces switching friction sufficiently for the highest-risk personas?

(Neither PM READ nor UX READ contributes to aggregate NPS.)

AGGREGATE NPS:
Compute the mean of all 12 persona NPS scores. Show the calculation.
Threshold: >= 7.0.
State: "Aggregate NPS: [value]. Threshold: 7.0. [Met / Not met]."
If below 7.0: "Spec requires revision before proceeding."

Write artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input, nps_format: categories,
framing: inertia, aggregate_nps: [value], threshold_met: [true/false].
```

---

## V-03: Per-card inline inertia (no global setup)

Axis: Inertia framing — A-06 achieved through a named `Current approach:` field embedded in
the card template rather than through a global SETUP section that names the inertia baseline
before any cards are written.
Hypothesis: A-06 requires an explicit per-card comparison to what the persona currently does.
The R2 V-01/V-05 implementation used a global SETUP sentence ("State what this feature replaces")
plus per-card NPS justification anchored to it. V-03 removes the global SETUP entirely and
places the comparison responsibility on a named card field (`Current approach:`). If A-06 passes
reliably via this approach, the global setup is scaffolding overhead — the per-card field is
sufficient and produces tighter card-level specificity (each persona's current behavior named
explicitly rather than inferred from a single shared baseline sentence).

```
You are running /listen:feedback for {{Topic}}. Simulate customer reactions to the spec or
design before it ships. Every persona names what they currently do in the relevant area, then
evaluates the spec against it.

Read the input signal for {{Topic}} — the spec, proposal, or design artifact.

STOCK PERSONAS:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

PERSONA FEEDBACK CARDS:
For each persona C-01 through C-12, produce a feedback card in this format:

[C-NN] [Name] ([Role])
Current approach: [1 sentence — what does this persona currently do in the area this feature
addresses? Name their specific tool, workflow, or behavior, not their general role description.]
NPS: [1-10] — [1-2 sentences: does this feature beat their current approach? State the net
benefit vs. the switching cost. The comparison must be explicit — "beats their status quo" or
"switching cost is too high" framing qualifies; describing persona preferences alone does not.]

Feedback items (descending severity — blocking first):
- blocking: [feedback item text] [BLOCKING]
- major: [feedback item text]
- minor: [feedback item text]
- cosmetic: [feedback item text]
(Only include severity levels that have items. Zero items valid — state "No feedback items.")

For any persona with NPS < 6: include a revision recommendation immediately after their items:
  Revision rec: [specific, actionable change — name the section, decision, or design choice
  and what to change. Not "improve clarity." Not "simplify." Name the thing and what to do.]

All 12 cards required before any aggregate section.

THEME MATRIX:
After all 12 cards:

| Theme | Personas | Highest Severity |
|-------|----------|-----------------|
| [theme] | [C-NN, ...] | [blocking / major / minor / cosmetic] |

Classify each theme as inertia-driven (switching cost, current capability loss, migration
friction) or spec-specific (net-new design objection). Minimum one theme required.

BLOCKING ITEMS:
Collect every item marked [BLOCKING] from the 12 cards. Because blocking items appear at the
top of each card (severity-first ordering), this is a verification pass over each card's leading
feedback item(s).

List: [C-NN] [Name] — [blocking item text]
If no [BLOCKING] items: "No blocking items."

PM READ:
2-3 sentences: what do the `Current approach:` fields reveal about adoption strategy and
migration scope? Which persona groups have the highest switching cost and what does that signal
for launch phasing?

UX READ:
2-3 sentences: what does the severity distribution and the gap between current approaches and
the spec's design reveal about mental model fit? Which personas face the steepest conceptual
switching cost?

(Neither read contributes to aggregate NPS.)

AGGREGATE NPS:
Compute the mean of all 12 persona NPS scores. Show the calculation.
Threshold: >= 7.0.
State: "Aggregate NPS: [value]. Threshold: 7.0. [Met / Not met]."
If below 7.0: "Spec requires revision before proceeding."

Write artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input, inertia_field: per-card,
aggregate_nps: [value], threshold_met: [true/false].
```

---

## V-04: Declarative sort rule (A-07 via rule, not template)

Axis: Output format — severity-first within-card ordering stated as a declarative sort rule
rather than demonstrated via a template that enumerates severity levels in order. The template
approach (R2 V-03/V-05) shows: `- blocking: [text] [BLOCKING] / - major: [text] / ...` which
implicitly demonstrates the correct order. V-04 replaces this with: "Sort feedback items in
descending severity: blocking first, then major, minor, cosmetic."
Hypothesis: The R2 template demonstration is structurally load-bearing for A-07 compliance.
Without a template that shows blocking as the first line item, models may revert to arbitrary
or chronological ordering. A declarative sort rule is less structurally constraining — it
describes the intended output without demonstrating its form. If A-07 reliability drops with
this variation, the template is confirmed as structurally necessary. If it holds, the rule is
sufficient and the template can be simplified in future variations.
Note: A-06 (inertia baseline) included via SETUP section to isolate the A-07 axis.

```
You are running /listen:feedback for {{Topic}}. Simulate customer reactions to the spec or
design before it ships. Every NPS score is a comparison against the status quo.

SETUP:
Read the input signal for {{Topic}} — the relevant spec, proposal, or design artifact.
State in 1-2 sentences: what current workflow, tool, or behavior does this feature change or
replace? This is the inertia baseline that every persona NPS score is measured against.

STOCK PERSONAS:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

PERSONA FEEDBACK CARDS:
For each persona C-01 through C-12, produce a feedback card:

[C-NN] [Name] ([Role])
NPS: [1-10] — [1-2 sentences: does this feature beat their current approach? State the switching
cost vs. net benefit explicitly. Persona preference description alone does not qualify.]

Feedback items:
- [severity: blocking | major | minor | cosmetic] [feedback item text]

Sort feedback items in descending severity: blocking items first, then major, then minor, then
cosmetic. Only include severity levels that have at least one item. Zero items valid — state
"No feedback items." Tag every blocking-severity item with [BLOCKING] inline.

For any persona with NPS < 6: include a revision recommendation immediately after their items:
  Revision rec: [specific, actionable change — name the section, decision, or design choice
  and what to change. Not "improve clarity."]

All 12 cards required before any aggregate section.

THEME MATRIX:
After all 12 cards:

| Theme | Personas | Highest Severity |
|-------|----------|-----------------|
| [theme] | [C-NN, ...] | [blocking / major / minor / cosmetic] |

Minimum one theme required. Note whether each theme is inertia-driven or a net-new spec
objection.

BLOCKING ITEMS:
Collect every item tagged [BLOCKING] from all 12 cards.
List: [C-NN] [Name] — [blocking item text]
If no [BLOCKING] items: "No blocking items."

PM READ:
2-3 sentences: scope, adoption risk, and launch readiness based on this feedback pattern.

UX READ:
2-3 sentences: design fit and mental model alignment based on severity distribution.

(Neither read contributes to aggregate NPS.)

AGGREGATE NPS:
Compute the mean of all 12 persona NPS scores. Show the calculation.
Threshold: >= 7.0.
State: "Aggregate NPS: [value]. Threshold: 7.0. [Met / Not met]."
If below 7.0: "Spec requires revision before proceeding."

Write artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input, card_format: declarative-sort,
framing: inertia, aggregate_nps: [value], threshold_met: [true/false].
```

---

## V-05: Combined ceiling (phases + categories + named field)

Axis: Combined — R2 V-05 full phase structure (ascending NPS pre-scoring, severity-first +
[BLOCKING] in cards, Phase 3 escalation bundle, NPS sensitivity analysis) plus NPS category
bands from V-02 (detractor/passive/promoter annotation) plus named `Current approach:` field
from V-03 (per-card explicit inertia, no reliance on global SETUP sentence for A-06).
Hypothesis: The R2 V-05 ceiling was 115/115 against the v2 rubric. Against v3 rubric (125 max),
R2 V-05 would score 125 — it already has A-06 (inertia framing) and A-07 (severity-first).
V-05 R3 tests whether two new structural additions (NPS category annotation + named field)
produce a cleaner, more reliable 125 by making A-06 doubly enforced (named field in Phase 2
card + inertia baseline from Phase 1) and the category label a structural checkpoint for
NPS justification quality. New patterns: `nps-category-bands-with-aggregate-mean` and
`named-current-approach-field-in-phase-card`.

```
You are running /listen:feedback. Cards are written in ascending NPS order (lowest scorer
first). Within each card, feedback items are listed in descending severity (blocking first).
Every NPS score is framed as a named-category comparison against the status quo. Blocking items
are flagged inline and escalated separately. Phase 3 collects both escalation outputs. Phase 4
synthesizes themes, PM/UX reads, and NPS sensitivity analysis.

NPS bands: Detractor (1-6) = switching cost > net benefit; Passive (7-8) = net benefit exists
but friction is significant; Promoter (9-10) = net benefit clear, switching friction acceptable.

--- PHASE 1: SCORE ---

Read the input signal for {{Topic}} — the spec, proposal, or design artifact.
State in 1-2 sentences: what current workflow, tool, or behavior does this feature change or
replace? This is the inertia baseline. Every NPS score is a comparison against it.

STOCK PERSONAS:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

For each persona, state:
- NPS: [1-10] ([Detractor | Passive | Promoter])
- Rationale: [1 sentence grounding the category in the inertia comparison — does this feature
  beat what they do today? What is the net benefit vs. the switching cost from the baseline?]

List all 12 in ascending NPS order (lowest first). Tied scores: order by persona ID.

After all 12:
  Aggregate NPS = sum / 12. Show calculation.
  Category breakdown: Promoters [count], Passives [count], Detractors [count].
  Threshold: >= 7.0.
  State: "Aggregate NPS: [value]. Result: PASS / FAIL."
  If FAIL: append "REVISION REQUIRED."

Do not proceed to Phase 2 until all 12 scores, their ascending-order list, the category
breakdown, and the aggregate result are stated.

--- PHASE 2: FEEDBACK CARDS ---

Write feedback cards in the same ascending NPS order from Phase 1 (lowest scorer first).
Within each card, list feedback items in descending severity: blocking first, then major,
minor, cosmetic. Only include severity levels that have items.

[C-NN] [Name] ([Role]) | NPS: [Phase 1 score] ([Detractor | Passive | Promoter])
Current approach: [1 sentence — what does this persona currently do in the area this feature
addresses? Name the specific tool, workflow, or behavior, not their general role description.]
Feedback items (descending severity — blocking first):
- blocking: [feedback item text] [BLOCKING]
- major: [feedback item text]
- minor: [feedback item text]
- cosmetic: [feedback item text]
(Zero items valid — state "No feedback items.")

For any persona with NPS < 6 (Detractor): include a REVISION REC immediately after their items:
  Revision rec: [specific, actionable change — name the section, decision, or design choice
  and what to change. Not "improve clarity." Not "simplify." Name the thing.]

All 12 cards required, in ascending NPS order, before Phase 3.

--- PHASE 3: ESCALATE ---

Both outputs required. Both require an explicit result.

BLOCKING ITEMS:
Collect every item marked [BLOCKING] from Phase 2. Because blocking items appear at the top
of each card (severity-first ordering), this is a two-checkpoint verification: leading
feedback item(s) of each card, then the inline [BLOCKING] tag.

List: [C-NN] [Name] (NPS [score], [Detractor | Passive | Promoter]) — [blocking item text]
If no [BLOCKING] items across all 12 cards: "No blocking items."

REVISION RECS SUMMARY:
Collect every REVISION REC from Phase 2 (NPS < 6 Detractor personas).
List: [C-NN] [Name] (NPS [score]) — [revision rec]
If no persona scored below 6: "No personas below NPS 6."

Both outputs complete before Phase 4.

--- PHASE 4: SYNTHESIZE ---

THEME MATRIX:
Build the cross-persona theme matrix from Phase 2 feedback. Annotate each theme with its
highest severity. Classify each theme as inertia-driven (switching cost, current capability
loss, migration friction) or spec-specific (net-new design objection).

| Theme | Personas | Highest Severity |
|-------|----------|-----------------|
| [theme] | [C-NN, ...] | [blocking / major / minor / cosmetic] |

Minimum one theme required.

PM READ:
2-3 sentences: what does the Detractor/Passive/Promoter distribution and the `Current approach:`
field patterns signal for adoption strategy, migration scope, and launch sequencing? Reference
specific Phase 2 findings.

UX READ:
2-3 sentences: what does the gap between `Current approach:` entries and the spec's design
reveal about mental model fit and switching friction? Which Detractor personas face the steepest
conceptual transition?

NPS SENSITIVITY ANALYSIS:
Identify the 2-3 personas whose scores most influence the aggregate NPS. These are the leverage
personas — the ones where a single spec change addressing their inertia objection could move
the aggregate most.

For each leverage persona:
  [C-NN] [Name] — NPS: [score] ([category]) — Why leverage: [why this score has outsized
  aggregate impact: low base, representative of a Detractor cluster, or addressable with a
  single inertia-reducing change that other Detractors share]
  Highest-ROI change: [the one spec change most likely to raise their category band and move
  the aggregate — reference their `Current approach:` entry and their Revision rec if present]

State: "Single highest-ROI change: [change] — estimated aggregate NPS lift: ~[delta],
moving from [current] to approximately [projected]."

Write artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input,
framing: inertia, nps_format: categories, inertia_field: per-card,
sequence: ascending-nps, card_format: severity-first,
phases: [score, feedback, escalate, synthesize],
aggregate_nps: [value], threshold_met: [true/false].
```

---

## Rubric v3 coverage map

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 All 12 personas | PASS | PASS | PASS | PASS | PASS |
| C-02 Severity tags | PASS | PASS | PASS | PASS | PASS |
| C-03 NPS with justification | PASS | PASS | PASS | PASS | PASS |
| C-04 Aggregate NPS + threshold | PASS | PASS | PASS | PASS | PASS |
| C-05 Theme matrix | PASS | PASS | PASS | PASS | PASS |
| R-01 Blocking escalated | PASS | PASS | PASS | PASS | PASS |
| R-02 PM and UX reads | PASS | PASS | PASS | PASS | PASS |
| R-03 Theme matrix with severity | PASS | PASS | PASS | PASS | PASS |
| A-01 Revision recs NPS < 6 | PASS | PASS | PASS | PASS | PASS |
| A-02 NPS sensitivity analysis | FAIL | FAIL | FAIL | FAIL | PASS |
| A-03 Inline [BLOCKING] flags | PASS* | PASS | PASS | PASS* | PASS |
| A-04 Ascending NPS ordering | FAIL | FAIL | FAIL | FAIL | PASS |
| A-05 Two-pass revision recs | FAIL | FAIL | FAIL | FAIL | PASS |
| A-06 Inertia-baseline NPS | PASS | PASS | PASS | PASS | PASS |
| A-07 Severity-first within card | PASS* | PASS | PASS | PASS* | PASS |
| **Score** | **110** | **110** | **110** | **100** | **125** |

*V-01 A-03 and A-07: present structurally; reliability concern due to conversational register —
actual run scores may fall to 100 if either criterion fails in practice.
*V-04 A-03 and A-07: declarative rule without template demonstration — compliance rate TBD;
predicted 100 assumes both pass; if A-07 fails, score drops to 95.

---

## Recommended scoring order

V-04 first (declarative sort rule — tests if A-07 template is load-bearing) → V-03 (per-card
inertia field — tests if global setup is load-bearing for A-06) → V-02 (NPS categories —
new vocabulary test; compare A-06 reliability vs. V-03) → V-01 (register test — qualitative
comparison of structural compliance across register) → V-05 (combined ceiling; first 125 attempt;
validates both new R3 patterns under full phase structure).
