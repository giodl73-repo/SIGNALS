Written to `simulations/quest/variations/listen-feedback-variations-R5-2026-03-14.md`.

---

## listen-feedback R5 — 5 Variations

**Context:** R4 V-05 = 135/135 under v4 rubric. Under v5 (max 145), R4 V-05 already passes A-10 and A-11 — baseline is 145/145. R5 tests robustness and seeks simplification.

| # | Axis | Predicted |
|---|------|-----------|
| V-01 | **Phrasing register** — conversational/descriptive | **140** |
| V-02 | **Inertia-led framing** — status-quo comparison as organizing principle | **145** |
| V-03 | **Phase compaction** — 3-phase (SCORE, FEEDBACK CARDS, ANALYSIS) | **145** |
| V-04 | **Role sequence** — UX READ first; theme matrix as final synthesis | **145** |
| V-05 | **Combined** — V-02 + V-03 + V-04 | **145** |

**Key structural invariants held across all 5:** A-10 labeled `Dominant Detractor objection:` field in Phase 1; A-11 card header = id/name/role only, body = `Current approach:` → `NPS:` → feedback; A-04 pre-scoring in ascending NPS order; A-05 two-pass revision recs.

**Predicted breakpoint in V-01:** Soft gate language ("make sure Phase 1 is complete before moving to Phase 2") is weaker than the imperative block in V-05 R4 ("Do not proceed to Phase 2 until..."). A-04 ascending NPS order is the most likely casualty — A-05 two-pass is lower risk because REVISION RECS SUMMARY is still an explicitly labeled required section.

**The key question in V-03:** is the ESCALATE phase boundary load-bearing for any criterion, or is it organizational overhead? If V-03 scores 145, the four-phase structure can be simplified to three in all future variations.

**Recommended scoring order:** V-01 → V-03 → V-02 → V-04 → V-05.
ting:**
- V-01 isolates the risk of conversational phrasing on phase gate strength (A-04 blocker)
- V-02 tests whether inertia-first framing sharpens A-10 synthesis without changing criteria
- V-03 tests whether the ESCALATE phase boundary is load-bearing for A-05
- V-04 tests role sequence and theme-matrix position without affecting any pass/fail
- V-05 tests combined axes for a shorter, more readable prompt at the same ceiling

**Predicted breakpoint in V-01:** A-04 (ascending NPS order) — soft gating language
("make sure Phase 1 is complete before Phase 2") is weaker than the imperative block in V-05
R4 ("Do not proceed to Phase 2 until..."). If the model writes Phase 2 cards without the
ascending sort committed in Phase 1, A-04 fails. A-05 likely survives since the REVISION RECS
SUMMARY section is still explicitly labeled and required.

**Recommended scoring order:** V-01 → V-03 → V-02 → V-04 → V-05.
Rationale: V-01 and V-03 test the two riskiest single axes first. V-02 and V-04 serve as
expected-145 controls. V-05 last — confirms combined ceiling and whether combination produces
interference.

---

## V-01: Phrasing register — conversational/descriptive

Axis: Phrasing register — V-05 R4 uses formal/imperative blocking language ("You are running
/listen:feedback. Cards are written in ascending NPS order... Do not proceed to Phase 2
until..."). V-01 rewrites the same structural requirements in a conversational/descriptive
register — first-person guidance, soft gate language ("make sure... before moving to"), and
descriptive card-format instructions instead of imperative templates.
Hypothesis: Structural fields (A-10, A-11) are defined by template format — they survive
register change because the label+colon format and header-only card structure are still named
explicitly. Phase gates are defined by blocking language — soft phrasing weakens the Phase 1
commitment. A-04 ascending NPS order is the most likely casualty: if the Phase 1 sort
instruction is soft ("work through all 12, then list them in ascending order"), a model may
begin card writing before the ascending sort is committed. A-05 two-pass revision recs is
lower risk because the REVISION RECS SUMMARY section is still explicitly required as a labeled
section.
Expected score: 140 (A-04 fails under soft Phase 1 gate; all other criteria pass).

```
This is a /listen:feedback run for {{Topic}}. The goal is to simulate how 12 customer personas
would react to the spec or design, then check whether the aggregate NPS clears the 7.0 threshold.

NPS bands encode switching-cost economics: a Detractor (1-6) is someone whose switching cost
exceeds the net benefit of adopting; a Passive (7-8) finds marginal net benefit with real
friction; a Promoter (9-10) sees net benefit that clearly outweighs switching friction.

Start by reading the input signal for {{Topic}} — the spec, proposal, or design. Then in 1-2
sentences, name what current workflow, tool, or behavior this feature displaces. That's the
inertia baseline — the default every persona is already running, and the thing every NPS score
is measured against.

--- PHASE 1: SCORE ---

Work through all 12 personas and score each one before writing any feedback cards. Collect all
12 scores first, then list them in ascending NPS order (lowest scorer first).

PERSONAS:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

For each persona:
- NPS: [1-10] ([Detractor | Passive | Promoter])
- Rationale: [1 sentence — does this feature beat what they currently do? Name the net benefit
  and the switching cost from the inertia baseline. The band label needs to follow from the
  comparison: Detractor means switching cost wins; Promoter means net benefit wins.]

List all 12 in ascending NPS order once scored (lowest first; ties by persona ID).

Then compute the aggregate:
- Aggregate NPS = sum / 12 (show the math)
- Promoters (9-10): [count] — [C-NN, ...]
- Passives (7-8): [count] — [C-NN, ...]
- Detractors (1-6): [count] — [C-NN, ...]
- Dominant Detractor objection: [one phrase naming the specific switching-cost or inertia concern
  shared most across Detractor scores — drawn from their rationale sentences; not a restatement
  of the band definition; "No Detractors" if none]
- Threshold: >= 7.0. Write: "Aggregate NPS: [value]. Result: PASS / FAIL." Add "REVISION
  REQUIRED." if below threshold.

Make sure Phase 1 is complete — all 12 scores in ascending order, the category breakdown, the
dominant Detractor objection, and the aggregate result — before moving to Phase 2.

--- PHASE 2: FEEDBACK CARDS ---

Write a feedback card for each persona in the same ascending NPS order from Phase 1. Each card
should open with what the persona currently does (before showing the NPS score), then give the
NPS score, then list feedback from most to least severe.

Card format — in this order:
[C-NN] [Name] ([Role])
Current approach: [1 sentence — what does this persona currently do in the area this feature
  addresses? Name the specific tool, workflow, or behavior, not their general role description.]
NPS: [Phase 1 score] ([Detractor | Passive | Promoter])
Feedback items (blocking first, then major, minor, cosmetic — only levels with items):
- blocking: [item text] [BLOCKING]
- major: [item text]
- minor: [item text]
- cosmetic: [item text]
(Zero items is fine — write "No feedback items.")

For any persona with NPS below 6, add a revision rec right after their items:
  Revision rec: [specific change — name the section, decision, or design choice and what to
  change about it. Not "improve clarity." Name the thing.]

Write all 12 cards before moving to Phase 3.

--- PHASE 3: ESCALATE ---

Both of these outputs are required. Both need an explicit result even if empty.

BLOCKING ITEMS:
Go through the 12 Phase 2 cards and pull out every [BLOCKING]-tagged item. Since blocking
items appear first in each card (severity-first ordering), check each card's leading feedback
item(s) and confirm the inline [BLOCKING] tag.
List: [C-NN] [Name] (NPS [score], [band]) — [blocking item text]
If no blocking items: write "No blocking items."

REVISION RECS SUMMARY:
Pull out every revision rec from Phase 2 (personas whose NPS was below 6).
List: [C-NN] [Name] (NPS [score]) — [revision rec text]
If no personas scored below 6: write "No personas below NPS 6."

Both outputs should be complete before Phase 4.

--- PHASE 4: SYNTHESIZE ---

THEME MATRIX:
Build the cross-persona theme matrix from Phase 2 feedback. Annotate each theme with its
highest severity. Classify each as inertia-driven (switching cost, capability loss, migration
friction) or spec-specific (net-new design objection).

| Theme | Personas | Highest Severity |
|-------|----------|-----------------|
| [theme] | [C-NN, ...] | [blocking / major / minor / cosmetic] |

At least one theme required.

PM READ:
2-3 sentences: what does the Detractor/Passive/Promoter distribution, the dominant Detractor
objection from Phase 1, and the `Current approach:` patterns across Phase 2 say about adoption
strategy, migration scope, and launch sequencing?

UX READ:
2-3 sentences: what does the gap between `Current approach:` entries and the spec's design
reveal about mental model fit and switching friction? Which Detractor personas face the steepest
conceptual transition?

NPS SENSITIVITY ANALYSIS:
Name the 2-3 personas whose scores have the most leverage over the aggregate. For each:
  [C-NN] [Name] — NPS: [score] ([band]) — Why leverage: [low base, cluster representative, or
  single addressable inertia change that other Detractors share]
  Highest-ROI change: [the one spec change most likely to move their category band — reference
  their `Current approach:` and revision rec if present]
State: "Single highest-ROI change: [change] — estimated aggregate NPS lift: ~[delta], from
[current] to approximately [projected]."

Write artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input,
framing: inertia, nps_format: categories, inertia_field: per-card,
sequence: ascending-nps, card_format: current-approach-first,
a10_field: labeled, a11_header: id-name-role-only,
phases: [score, feedback, escalate, synthesize],
aggregate_nps: [value], threshold_met: [true/false].
```

---

## V-02: Inertia-led framing — status-quo comparison as organizing principle

Axis: Inertia framing — V-05 R4 organizes around NPS mechanics with inertia as a supporting
frame. V-02 reorganizes around the status-quo comparison as the primary question: "does this
proposal beat the status quo for this persona?" NPS becomes the scoring verdict of the
comparison. All structural requirements (A-10 labeled field, A-11 card format, phase gates)
preserved; only the motivating frame changes.
Hypothesis: Foregrounding the inertia question produces more specific `Current approach:`
entries because the persona's current behavior is the answer to the organizing question —
not an optional field. This should improve `Dominant Detractor objection:` specificity (A-10)
since the aggregate synthesizes comparison verdicts rather than NPS justifications. No pass/fail
criteria are affected — the test is quality improvement at the same structural level.
Expected score: 145 (all criteria met; inertia-led framing sharpens A-09/A-10 outputs without
changing any pass/fail boundary).

```
You are running /listen:feedback for {{Topic}}. The organizing question is: does this proposal
beat the status quo for each persona? Every persona already has a default — a workflow, tool,
or habit that this feature asks them to change. A Detractor (1-6) is someone whose switching
cost exceeds the net benefit of changing; a Passive (7-8) finds marginal net benefit with real
friction; a Promoter (9-10) sees net benefit that clearly outweighs switching friction.

--- PHASE 1: STATUS-QUO COMPARISON ---

Read the input signal for {{Topic}} — the spec, proposal, or design artifact.
State in 1-2 sentences: what current workflow, tool, or behavior does this feature change or
replace? This is the status quo. Every NPS score is a verdict on whether switching from it is
worthwhile.

STOCK PERSONAS:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

For each persona, answer: does this proposal beat their status quo?
- NPS: [1-10] ([Detractor | Passive | Promoter])
- Status-quo verdict: [1 sentence — name the net benefit and the switching cost explicitly.
  Band label must follow from this comparison: Detractor = switching cost wins, net benefit is
  insufficient; Promoter = net benefit wins, friction is acceptable. Persona preference
  description alone does not qualify as a verdict.]

List all 12 in ascending NPS order (lowest first; ties by persona ID).

After all 12:
  Aggregate NPS = sum / 12. Show calculation.
  Category breakdown:
    Promoters (9-10): [count] — [C-NN, ...]
    Passives (7-8): [count] — [C-NN, ...]
    Detractors (1-6): [count] — [C-NN, ...]
  Dominant Detractor objection: [one phrase naming the specific status-quo attachment or
    switching-cost pattern driving the most Detractor verdicts — synthesized from the comparison
    sentences above. Must be a named inertia pattern (e.g., "migration effort from existing
    workflow", "feature parity gap vs. current tool", "setup cost blocks initial adoption").
    Not a restatement of the Detractor band definition. "No Detractors" if none.]
  Threshold: >= 7.0.
  State: "Aggregate NPS: [value]. Result: PASS / FAIL."
  If FAIL: append "REVISION REQUIRED."

Do not proceed to Phase 2 until all 12 scores, ascending list, category breakdown, dominant
Detractor objection, and aggregate result are stated.

--- PHASE 2: PER-PERSONA CARDS ---

Write a card for each persona in ascending NPS order from Phase 1. The organizing question per
card: what is the gap between what this persona currently does and what the proposal asks them
to do?

Card format — strictly in this order:
[C-NN] [Name] ([Role])
Current approach: [1 sentence — what this persona currently does in the area this feature
  addresses; name the specific tool, workflow, or behavior — not a role description. This is
  the status quo for this persona specifically.]
NPS: [Phase 1 score] ([Detractor | Passive | Promoter])
Feedback items (most severe first):
- blocking: [feedback item text] [BLOCKING]
- major: [feedback item text]
- minor: [feedback item text]
- cosmetic: [feedback item text]
(Only include severity levels with items. Zero items valid — state "No feedback items.")

For any persona with NPS < 6: include a REVISION REC immediately after their items:
  Revision rec: [specific, actionable change — name the section, decision, or design choice
  and what to change. Not "improve clarity." Not "add more detail." Name the thing and the
  specific change needed.]

All 12 cards required before Phase 3.

--- PHASE 3: ESCALATE ---

Both outputs required. Both require an explicit result.

BLOCKING ITEMS:
Collect every [BLOCKING]-tagged item from Phase 2. Blocking items appear first in each card
(severity-first ordering) — verification: leading feedback item(s) of each card, then inline
[BLOCKING] tag.
List: [C-NN] [Name] (NPS [score], [band]) — [blocking item text]
No blocking items: state "No blocking items."

REVISION RECS SUMMARY:
Collect every REVISION REC from Phase 2 (NPS < 6 personas).
List: [C-NN] [Name] (NPS [score]) — [revision rec text]
No personas below NPS 6: state "No personas below NPS 6."

Both outputs complete before Phase 4.

--- PHASE 4: SYNTHESIZE ---

THEME MATRIX:
Synthesize Phase 2 feedback into recurring themes. Annotate each with highest severity.
Classify as inertia-driven (status-quo attachment, switching cost, migration friction) or
spec-specific (net-new design objection). The split reveals whether revision effort should
target the proposal's design or its migration and adoption story.

| Theme | Personas | Highest Severity |
|-------|----------|-----------------|
| [theme] | [C-NN, ...] | [blocking / major / minor / cosmetic] |

Minimum one theme.

PM READ:
2-3 sentences: what does the status-quo verdict pattern — the band distribution, the dominant
Detractor objection, and the `Current approach:` field data — reveal about adoption strategy,
onboarding investment, and launch sequencing? Reference specific Phase 1 and Phase 2 findings.

UX READ:
2-3 sentences: what does the gap between `Current approach:` entries (Phase 2) and the spec's
proposed interaction reveal about mental model fit? Which Detractor personas carry the steepest
switching friction from their specific status quo?

NPS SENSITIVITY ANALYSIS:
Identify the 2-3 personas whose NPS scores most drive the aggregate. These are the highest-ROI
revision targets — the ones where a single spec change addressing their status-quo objection
could move the aggregate most.

For each leverage persona:
  [C-NN] [Name] — NPS: [score] ([band]) — Why leverage: [low base, cluster representative, or
  single addressable switching-cost objection shared with other Detractors]
  Highest-ROI change: [one spec change most likely to move their band — ground it in their
  `Current approach:` entry and their Revision rec if present]

State: "Single highest-ROI change: [change] — estimated aggregate NPS lift: ~[delta], from
[current] to approximately [projected]."

Write artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input,
framing: status-quo-comparison, nps_format: categories, inertia_field: per-card,
sequence: ascending-nps, card_format: current-approach-first,
a10_field: labeled, a11_header: id-name-role-only,
phases: [status-quo-comparison, per-persona-cards, escalate, synthesize],
aggregate_nps: [value], threshold_met: [true/false].
```

---

## V-03: Phase compaction — 3-phase structure (SCORE, FEEDBACK CARDS, ANALYSIS)

Axis: Lifecycle emphasis — collapse Phase 3 (ESCALATE) and Phase 4 (SYNTHESIZE) into a single
ANALYSIS phase. Structure becomes SCORE → FEEDBACK CARDS → ANALYSIS. ANALYSIS must produce
all six outputs: blocking items, revision recs summary, theme matrix, PM read, UX read, NPS
sensitivity analysis. All section labels preserved; only the phase boundary between escalation
and synthesis is removed.
Hypothesis: A-05 (two-pass revision recs) requires inline recs in Phase 2 AND a collected
summary section. The summary section can appear in ANALYSIS regardless of whether ESCALATE is
a separate phase — "collected summary" is a structural requirement on the section, not on a
phase boundary. A-02 (sensitivity analysis) and R-01 (blocking escalation) similarly only
require dedicated sections, not a separate phase. V-03 tests whether the four-phase structure
is required for any criterion or is organizational overhead. If all 11 aspirational criteria
survive with 3 phases, V-05 R4's four-phase gate structure is over-engineering.
Expected score: 145 (A-05 survives because inline + summary both present in explicit labeled
sections; ANALYSIS provides a dedicated section for every required output).

```
You are running /listen:feedback. Cards are written in ascending NPS order (lowest scorer
first). Within each card, `Current approach:` appears first (before NPS), then feedback items
in descending severity. Every NPS score is a named-category comparison against the status quo.
Phase 1 commits all scores, category breakdown, and dominant Detractor objection before any
card is written. Phase 3 collects all escalations and synthesizes all findings in one pass.

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
  beat what they do today? Net benefit vs. switching cost from the baseline?]

List all 12 in ascending NPS order (lowest first). Ties: order by persona ID.

After all 12:
  Aggregate NPS = sum / 12. Show calculation.
  Category breakdown:
    Promoters (9-10): [count] — [C-NN, ...]
    Passives (7-8): [count] — [C-NN, ...]
    Detractors (1-6): [count] — [C-NN, ...]
  Dominant Detractor objection: [one phrase naming the specific switching-cost or inertia
    concern shared across the most Detractor scores — drawn from the rationale sentences above;
    not a band definition restatement; "No Detractors" if none]
  Threshold: >= 7.0.
  State: "Aggregate NPS: [value]. Result: PASS / FAIL."
  If FAIL: append "REVISION REQUIRED."

Do not proceed to Phase 2 until all 12 scores, ascending list, category breakdown, dominant
Detractor objection, and aggregate result are stated.

--- PHASE 2: FEEDBACK CARDS ---

Write feedback cards in ascending NPS order from Phase 1 (lowest scorer first).
Card body order: `Current approach:` first, then NPS, then feedback items in descending
severity. Only include severity levels with items.

[C-NN] [Name] ([Role])
Current approach: [1 sentence — what does this persona currently do in the area this feature
  addresses? Name the specific tool, workflow, or behavior, not their general role description.]
NPS: [Phase 1 score] ([Detractor | Passive | Promoter])
Feedback items (descending severity — blocking first):
- blocking: [feedback item text] [BLOCKING]
- major: [feedback item text]
- minor: [feedback item text]
- cosmetic: [feedback item text]
(Zero items valid — state "No feedback items.")

For any persona with NPS < 6 (Detractor): include a REVISION REC immediately after their items:
  Revision rec: [specific, actionable change — name the section, decision, or design choice
  and what to change. Not "improve clarity." Not "simplify." Name the thing.]

All 12 cards required before Phase 3.

--- PHASE 3: ANALYSIS ---

Complete all six sections in order. No section may be omitted. Explicit result required for
every section that has a binary outcome.

BLOCKING ITEMS:
Collect every [BLOCKING]-tagged item from Phase 2. Blocking items appear first in each card
(severity-first ordering) — verification: check each card's leading feedback item(s), then
confirm the inline [BLOCKING] tag.
List: [C-NN] [Name] (NPS [score], [band]) — [blocking item text]
If no blocking items: "No blocking items."

REVISION RECS SUMMARY:
Collect every REVISION REC from Phase 2 (NPS < 6 personas).
List: [C-NN] [Name] (NPS [score]) — [revision rec text]
If no personas below NPS 6: "No personas below NPS 6."

THEME MATRIX:
Build from Phase 2 feedback. Annotate each theme with highest severity. Classify each as
inertia-driven (switching cost, capability loss, migration friction) or spec-specific (net-new
design objection).
| Theme | Personas | Highest Severity |
|-------|----------|-----------------|
| [theme] | [C-NN, ...] | [blocking / major / minor / cosmetic] |
Minimum one theme required.

PM READ:
2-3 sentences: what does the Detractor/Passive/Promoter distribution, the dominant Detractor
objection from Phase 1, and the `Current approach:` patterns signal for adoption strategy,
migration scope, and launch sequencing? Reference specific Phase 1 and Phase 2 findings.

UX READ:
2-3 sentences: what does the gap between `Current approach:` entries and the spec's design
reveal about mental model fit and switching friction? Which Detractor personas face the steepest
conceptual transition?

NPS SENSITIVITY ANALYSIS:
Identify the 2-3 personas whose scores most influence the aggregate NPS.
For each:
  [C-NN] [Name] — NPS: [score] ([band]) — Why leverage: [low base, cluster representative, or
  single addressable inertia change other Detractors share]
  Highest-ROI change: [one spec change most likely to move their band — reference `Current
  approach:` and revision rec if present]
State: "Single highest-ROI change: [change] — estimated aggregate NPS lift: ~[delta], from
[current] to approximately [projected]."

Write artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input,
framing: inertia, nps_format: categories, inertia_field: per-card,
sequence: ascending-nps, card_format: current-approach-first,
a10_field: labeled, a11_header: id-name-role-only,
phases: [score, feedback, analysis],
aggregate_nps: [value], threshold_met: [true/false].
```

---

## V-04: Role sequence — UX READ first, theme matrix as final synthesis

Axis: Role sequence — swap PM READ and UX READ so UX synthesizes first (switching friction,
mental model fit), then PM synthesizes second (adoption strategy, launch sequencing) with UX
findings available as input. Additionally, move the THEME MATRIX to after both reads so it
synthesizes the PM/UX lenses rather than preceding them. All other structures unchanged from
V-05 R4 (four phases, A-10 field in Phase 1, A-11 card format in Phase 2).
Hypothesis: In V-05 R4, the theme matrix precedes PM/UX reads and serves as the source for
them. When the theme matrix follows the reads, it can incorporate PM/UX framing — each theme
gets classified through both design fit (UX) and adoption risk (PM). UX-before-PM creates a
natural dependency: PM adoption strategy references UX friction analysis. No pass/fail criteria
have ordering requirements on PM vs. UX (R-02 requires both present; no sequencing rule).
C-05 and R-03 require the theme matrix with severity annotation — position doesn't affect pass.
Expected score: 145 (role ordering doesn't change any pass/fail; theme matrix as final synthesis
may improve R-03 depth at same binary pass condition).

```
You are running /listen:feedback. Cards are written in ascending NPS order (lowest scorer
first). Within each card, `Current approach:` appears first, then NPS, then feedback items in
descending severity (blocking first). Every NPS score is a named-category comparison against
the status quo. Phase 1 commits all scores, category breakdown, and dominant Detractor objection
before any card is written. Phase 3 collects blocking items and revision recs. Phase 4 produces
UX read first, then PM read, then theme matrix as final cross-persona synthesis.

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
  beat what they do today? Net benefit vs. switching cost from the baseline?]

List all 12 in ascending NPS order (lowest first). Ties: order by persona ID.

After all 12:
  Aggregate NPS = sum / 12. Show calculation.
  Category breakdown:
    Promoters (9-10): [count] — [C-NN, ...]
    Passives (7-8): [count] — [C-NN, ...]
    Detractors (1-6): [count] — [C-NN, ...]
  Dominant Detractor objection: [one phrase naming the specific switching-cost or inertia
    concern shared across the most Detractor scores — drawn from the rationale sentences above;
    not a band definition restatement; "No Detractors" if none]
  Threshold: >= 7.0.
  State: "Aggregate NPS: [value]. Result: PASS / FAIL."
  If FAIL: append "REVISION REQUIRED."

Do not proceed to Phase 2 until all 12 scores, ascending list, category breakdown, dominant
Detractor objection, and aggregate result are stated.

--- PHASE 2: FEEDBACK CARDS ---

Write feedback cards in ascending NPS order from Phase 1 (lowest scorer first).
Within each card: `Current approach:` first, then NPS, then feedback items in descending
severity. Only include severity levels with items.

[C-NN] [Name] ([Role])
Current approach: [1 sentence — what does this persona currently do in the area this feature
  addresses? Name the specific tool, workflow, or behavior, not their general role description.]
NPS: [Phase 1 score] ([Detractor | Passive | Promoter])
Feedback items (descending severity — blocking first):
- blocking: [feedback item text] [BLOCKING]
- major: [feedback item text]
- minor: [feedback item text]
- cosmetic: [feedback item text]
(Zero items valid — state "No feedback items.")

For any persona with NPS < 6 (Detractor): include a REVISION REC immediately after their items:
  Revision rec: [specific, actionable change — name the section, decision, or design choice
  and what to change. Not "improve clarity." Not "simplify." Name the thing.]

All 12 cards required before Phase 3.

--- PHASE 3: ESCALATE ---

Both outputs required. Both require an explicit result.

BLOCKING ITEMS:
Collect every [BLOCKING]-tagged item from Phase 2. Blocking items appear first in each card
(severity-first ordering) — verification: leading feedback item(s) of each card, then inline
[BLOCKING] tag.
List: [C-NN] [Name] (NPS [score], [band]) — [blocking item text]
If no blocking items: "No blocking items."

REVISION RECS SUMMARY:
Collect every REVISION REC from Phase 2 (NPS < 6 personas).
List: [C-NN] [Name] (NPS [score]) — [revision rec text]
If no personas below NPS 6: "No personas below NPS 6."

Both outputs complete before Phase 4.

--- PHASE 4: SYNTHESIZE ---

UX READ:
2-3 sentences: what does the gap between `Current approach:` entries (Phase 2) and the spec's
design reveal about mental model fit and switching friction? Which Detractor personas face the
steepest conceptual transition, and what specific interaction or design assumption creates
that gap?

PM READ:
2-3 sentences: drawing on the UX switching-friction analysis above and the Detractor/Passive/
Promoter distribution from Phase 1 — what does the dominant Detractor objection and the
`Current approach:` pattern signal for adoption strategy, migration scope, and launch
sequencing?

NPS SENSITIVITY ANALYSIS:
Identify the 2-3 personas whose scores most influence the aggregate NPS.
For each:
  [C-NN] [Name] — NPS: [score] ([band]) — Why leverage: [low base, cluster representative, or
  single addressable inertia change other Detractors share]
  Highest-ROI change: [one spec change most likely to move their band — reference `Current
  approach:` and revision rec if present]
State: "Single highest-ROI change: [change] — estimated aggregate NPS lift: ~[delta], from
[current] to approximately [projected]."

THEME MATRIX:
Build the cross-persona theme matrix from Phase 2 feedback, incorporating the UX and PM lenses
above. Annotate each theme with highest severity. Classify as inertia-driven (switching cost,
capability loss, migration friction) or spec-specific (net-new design objection).
| Theme | Personas | Highest Severity |
|-------|----------|-----------------|
| [theme] | [C-NN, ...] | [blocking / major / minor / cosmetic] |
Minimum one theme.

Write artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input,
framing: inertia, nps_format: categories, inertia_field: per-card,
sequence: ascending-nps, card_format: current-approach-first,
a10_field: labeled, a11_header: id-name-role-only,
role_sequence: ux-before-pm, theme_matrix: post-reads,
phases: [score, feedback, escalate, synthesize],
aggregate_nps: [value], threshold_met: [true/false].
```

---

## V-05: Combined — inertia-led (V-02) + 3-phase (V-03) + UX-first (V-04)

Axis: Combined inertia-led framing + 3-phase lifecycle + UX-before-PM role sequence + theme
matrix as final synthesis.
Hypothesis: V-02 (inertia-led framing), V-03 (3-phase compaction), and V-04 (UX-before-PM with
theme matrix after reads) each test independent axes expected to score 145 individually. Combined,
they produce a shorter prompt with a clearer organizing question, one fewer phase boundary, and
a more natural synthesis sequence (UX friction → PM adoption → theme matrix synthesizes both).
All structural invariants maintained: A-10 `Dominant Detractor objection:` labeled field in
Phase 1; A-11 card header = id/name/role only, body = `Current approach:` → `NPS:` → feedback;
A-04 Phase 1 pre-scoring in ascending order; A-05 inline recs in Phase 2 + REVISION RECS
SUMMARY in ANALYSIS phase.
Test question: does combining three individually safe axes produce interference? Shorter
combined prompts sometimes lose structural guarantees present in each individual variation
because any single instruction becomes proportionally smaller. If V-01 confirms that phrasing
register is the soft axis (scoring 140), V-05 can't combine V-01 phrasing since it was excluded
from the axis selection.
Expected score: 145.

```
You are running /listen:feedback for {{Topic}}. The organizing question is: does this proposal
beat the status quo for each persona? Every persona has a default workflow, tool, or habit that
this feature asks them to change. A Detractor (1-6) is someone whose switching cost exceeds the
net benefit of changing; a Passive (7-8) finds marginal net benefit with real friction; a
Promoter (9-10) sees net benefit that clearly outweighs switching friction.

--- PHASE 1: STATUS-QUO COMPARISON ---

Read the input signal for {{Topic}} — the spec, proposal, or design artifact.
State in 1-2 sentences: what current workflow, tool, or behavior does this feature change or
replace? This is the status quo. Every NPS score is a verdict on whether switching from it is
worthwhile.

STOCK PERSONAS:
C-01 Maria Chen (Maker) | C-02 James Okafor (Builder) | C-03 Priya Nair (Strategist)
C-04 Tom Bergstrom (Operator) | C-05 Aisha Mensah (Researcher) | C-06 Carlos Reyes (Designer)
C-07 Lin Wei (Analyst) | C-08 Sophie Dubois (Manager) | C-09 Raj Patel (Advocate)
C-10 Yuki Tanaka (Evaluator) | C-11 Elena Vasquez (Buyer) | C-12 Frank Hoffmann (Regulator)

For each persona, answer: does this proposal beat their status quo?
- NPS: [1-10] ([Detractor | Passive | Promoter])
- Status-quo verdict: [1 sentence — name the net benefit and switching cost explicitly. Band
  label must follow from the comparison: Detractor = switching cost wins; Promoter = net benefit
  wins. Persona preference description alone is not a verdict.]

List all 12 in ascending NPS order (lowest first; ties by persona ID).

After all 12:
  Aggregate NPS = sum / 12. Show calculation.
  Category breakdown:
    Promoters (9-10): [count] — [C-NN, ...]
    Passives (7-8): [count] — [C-NN, ...]
    Detractors (1-6): [count] — [C-NN, ...]
  Dominant Detractor objection: [one phrase — the specific status-quo attachment or switching-
    cost pattern driving the most Detractor verdicts; synthesized from the comparison sentences
    above; not a band definition restatement; "No Detractors" if none]
  Threshold: >= 7.0.
  State: "Aggregate NPS: [value]. Result: PASS / FAIL."
  If FAIL: append "REVISION REQUIRED."

Do not proceed to Phase 2 until all 12 scores, ascending list, category breakdown, dominant
Detractor objection, and aggregate result are stated.

--- PHASE 2: PER-PERSONA CARDS ---

Write a card for each persona in ascending NPS order from Phase 1. The organizing question per
card: what is the gap between what this persona currently does and what the proposal asks them
to do?

Card format — strictly in this order:
[C-NN] [Name] ([Role])
Current approach: [1 sentence — what this persona currently does in the area this feature
  addresses; specific tool, workflow, or behavior; not a role description]
NPS: [Phase 1 score] ([Detractor | Passive | Promoter])
Feedback items (most severe first):
- blocking: [feedback item text] [BLOCKING]
- major: [feedback item text]
- minor: [feedback item text]
- cosmetic: [feedback item text]
(Only include severity levels with items. Zero items valid — state "No feedback items.")

For any persona with NPS < 6: include a REVISION REC immediately after their items:
  Revision rec: [specific, actionable change — name the design decision, section, or behavior
  to change and what to change about it. Not "improve clarity." Name the thing.]

All 12 cards required before Phase 3.

--- PHASE 3: ANALYSIS ---

Complete all six sections in order. No section may be omitted.

BLOCKING ITEMS:
Collect every [BLOCKING]-tagged item from Phase 2. Blocking items appear first in each card —
check each card's leading feedback item(s), then confirm the inline [BLOCKING] tag.
List: [C-NN] [Name] (NPS [score], [band]) — [blocking item text]
No blocking items: "No blocking items."

REVISION RECS SUMMARY:
Collect every REVISION REC from Phase 2 (NPS < 6 personas).
List: [C-NN] [Name] (NPS [score]) — [revision rec text]
No personas below NPS 6: "No personas below NPS 6."

UX READ:
2-3 sentences: what does the gap between `Current approach:` entries (Phase 2) and the spec's
design reveal about mental model fit and switching friction? Which Detractor personas face the
steepest conceptual transition, and what specific interaction or design assumption creates
that gap?

PM READ:
2-3 sentences: drawing on the UX friction analysis above and the Phase 1 band distribution —
what does the dominant Detractor objection and `Current approach:` pattern signal for adoption
strategy, migration scope, and launch sequencing?

NPS SENSITIVITY ANALYSIS:
Identify the 2-3 personas whose scores most influence the aggregate NPS.
For each:
  [C-NN] [Name] — NPS: [score] ([band]) — Why leverage: [low base, cluster representative, or
  single addressable switching-cost objection shared with other Detractors]
  Highest-ROI change: [one spec change most likely to move their band — reference `Current
  approach:` and revision rec if present]
State: "Single highest-ROI change: [change] — estimated aggregate NPS lift: ~[delta], from
[current] to approximately [projected]."

THEME MATRIX:
Build from Phase 2 feedback, informed by the UX and PM reads above. Annotate each theme with
highest severity. Classify as inertia-driven (status-quo attachment, switching cost, migration
friction) or spec-specific (net-new design objection).
| Theme | Personas | Highest Severity |
|-------|----------|-----------------|
| [theme] | [C-NN, ...] | [blocking / major / minor / cosmetic] |
Minimum one theme.

Write artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input,
framing: status-quo-comparison, nps_format: categories, inertia_field: per-card,
sequence: ascending-nps, card_format: current-approach-first,
a10_field: labeled, a11_header: id-name-role-only,
role_sequence: ux-before-pm, theme_matrix: post-reads,
phases: [status-quo-comparison, per-persona-cards, analysis],
aggregate_nps: [value], threshold_met: [true/false].
```

---

## v5 rubric coverage map (predicted)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 All 12 personas | PASS | PASS | PASS | PASS | PASS |
| C-02 Severity tags | PASS | PASS | PASS | PASS | PASS |
| C-03 NPS + justification | PASS | PASS | PASS | PASS | PASS |
| C-04 Aggregate NPS + threshold | PASS | PASS | PASS | PASS | PASS |
| C-05 Theme matrix | PASS | PASS | PASS | PASS | PASS |
| R-01 Blocking escalated | PASS | PASS | PASS | PASS | PASS |
| R-02 PM + UX reads | PASS | PASS | PASS | PASS | PASS |
| R-03 Theme matrix severity | PASS | PASS | PASS | PASS | PASS |
| A-01 Revision recs NPS < 6 | PASS | PASS | PASS | PASS | PASS |
| A-02 NPS sensitivity | PASS | PASS | PASS | PASS | PASS |
| A-03 Inline [BLOCKING] | PASS | PASS | PASS | PASS | PASS |
| A-04 Ascending NPS order | FAIL* | PASS | PASS | PASS | PASS |
| A-05 Two-pass revision recs | PASS | PASS | PASS | PASS | PASS |
| A-06 Inertia baseline NPS | PASS | PASS | PASS | PASS | PASS |
| A-07 Severity-first within card | PASS | PASS | PASS | PASS | PASS |
| A-08 Category bands + dominant | PASS | PASS | PASS | PASS | PASS |
| A-09 `Current approach:` before NPS | PASS | PASS | PASS | PASS | PASS |
| A-10 `Dominant Detractor objection:` field | PASS | PASS | PASS | PASS | PASS |
| A-11 Header id/name/role; body `Current approach:` first | PASS | PASS | PASS | PASS | PASS |
| **Predicted score** | **140** | **145** | **145** | **145** | **145** |

*V-01 predicted A-04 fail: soft phase gate ("make sure Phase 1 is complete before moving to
Phase 2") is weaker than V-05 R4's "Do not proceed to Phase 2 until..." If the model begins
writing cards without committing the ascending sort, A-04 fails. A-05 predicted to pass because
the REVISION RECS SUMMARY section is explicitly labeled and required — soft gate language is
less likely to cause omission of a named section than to cause skipped pre-sorting.

---

## Recommended scoring order

V-01 → V-03 → V-02 → V-04 → V-05.

- **V-01 first**: tests the riskiest axis. If V-01 scores 140 (A-04 fails), confirms imperative
  Phase 1 gate language is load-bearing for ascending NPS order — a key design constraint for
  all future variations. If V-01 scores 145, soft phrasing is sufficient and conversational
  register is safe to combine in future rounds.
- **V-03 second**: tests phase compaction. If V-03 scores 145, the four-phase structure in
  V-05 R4 is organizational overhead rather than a structural requirement — V-05 R5 and all
  future variations can use 3 phases. If V-03 scores 140, identifies which criterion requires
  the ESCALATE phase boundary.
- **V-02 third**: expected 145 control. Confirms inertia-led framing doesn't disturb any
  criterion. If 145, framing axis is safe for V-05 R5.
- **V-04 fourth**: expected 145 control. Confirms role sequence and theme-matrix position don't
  affect any criterion.
- **V-05 last**: ceiling confirmation under combined axes. Inherits V-02 framing (safe), V-03
  phase structure (safe if 145), V-04 role sequence (safe). If any single-axis variation scores
  140, V-05 will inherit that failure and also score 140.
