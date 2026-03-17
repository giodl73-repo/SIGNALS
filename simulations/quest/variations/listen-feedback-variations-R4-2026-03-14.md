Written to `simulations/quest/variations/listen-feedback-variations-R4-2026-03-14.md`.

---

## listen-feedback R4 — 5 Variations

| # | Axis | Predicted score |
|---|------|----------------|
| V-01 | A-08 structural field (non-phased) — labeled `Dominant Detractor objection:` vs. V-02 R3's prose instruction | **115** |
| V-02 | Combined A-08+A-09 non-phased ceiling — V-02 R3 + V-03 R3 merged; `Current approach:` before NPS in card | **120** |
| V-03 | V-05 R3 + A-09 fix only — card body reordered to `Current approach:` → `NPS:` → feedback | **130** |
| V-04 | V-05 R3 + A-08 fix only — Phase 1 aggregate gains `Dominant Detractor objection:` field | **130*** |
| V-05 | Combined ceiling — both fixes; Phase 1 dominant objection + Phase 2 card ordering | **135** |

*V-04 is the A-09 ambiguity resolver: score 135 = lenient "or" reading (before feedback items suffices); score 130 = strict "and" reading (must precede NPS). V-05 targets 135 either way since it explicitly orders `Current approach:` before `NPS:` in the card body.

**Key structural bets vs. R3:**
- R3 V-05 scored 125 against v3. Against v4 it scores 125 — both A-08 and A-09 fail: A-08 lacks the named dominant Detractor objection in aggregate; A-09 has `Current approach:` after NPS in the card header.
- V-01/V-02 establish the non-phased ceiling (115/120) before adding phase overhead.
- V-03 and V-04 are single-axis phase-structure tests — together they confirm whether A-08 and A-09 fail independently in V-05 R3.
- V-05 is the first 135 attempt. New patterns: `dominant-detractor-objection-labeled-field-in-aggregate` and `current-approach-before-nps-card-field-ordering`.

**Recommended scoring order:** V-01 → V-02 → V-03 → V-04 → V-05.
th present; misses A-02/A-04/A-05 (no phases) |
| V-01 | 115 | Single-axis A-08 labeled field; misses A-09/A-02/A-04/A-05 |

**Key structural bets:**
- **V-04 is the A-09 ambiguity resolver** — does a `Current approach:` field after NPS (but before feedback) pass A-09 by the "or" reading? V-04 result settles it definitively. If V-04 scores 135, the lenient reading applies. If 130, strict reading applies and all future ceiling variations must put `Current approach:` before NPS in the card header.
- **V-01 vs. V-02** tests whether adding `Current approach:` (A-09) to the A-08 structure is additive (+5) or creates interference — non-phased card format handles two new structural fields.
- **V-03 vs. V-04** isolates each fix independently within the phase structure before combining in V-05.
- **V-05** targets 135: if both single-axis fixes (V-03 and V-04) score 130, V-05 should score 135 by conjunction.

**New R4 patterns to capture if V-05 reaches 135:**
- `dominant-detractor-objection-labeled-field-in-aggregate` — A-08 structural field; label+colon format in aggregate section forces a specific objection pattern name, not a prose paragraph
- `current-approach-before-nps-card-field-ordering` — A-09 structural ordering; `Current approach:` must precede `NPS:` in card body; achieved by separating persona header (id/name/role) from card fields (`Current approach:`, `NPS:`, feedback items)

**Recommended scoring order:** V-01 → V-02 → V-03 → V-04 → V-05.
Rationale: lightweight variations first (V-01/V-02) establish A-08/A-09 baselines; single-axis phased variations (V-03/V-04) test each fix in isolation; ceiling variation (V-05) is scored last to confirm conjunction.

---

## V-01: A-08 structural field (non-phased)

Axis: Output format — `Dominant Detractor objection:` added as a dedicated labeled field in the
CATEGORY SUMMARY section. Based on V-02 R3 (which already has Detractor/Passive/Promoter counts
and a prose "Note the dominant Detractor objection" instruction). V-01 R4 replaces the prose
instruction with a labeled field using the standard label+colon format.
Hypothesis: V-02 R3 likely passes A-08 already (prose "Note the dominant Detractor objection
pattern" is present alongside counts and inertia-framed band definitions). V-01 R4 tests whether
the labeled-field format (`Dominant Detractor objection: [phrase]`) produces more structurally
reliable A-08 compliance than the prose instruction — specifically, whether the label forces a
specific pattern name rather than a paragraph. If both pass A-08, the labeled field is preferred
for future variations due to scanability and structural consistency with A-09's field format.
Expected score: 115 (passes A-08; fails A-09, A-02, A-04, A-05).

```
You are running /listen:feedback. Simulate customer reactions to the spec or design for {{Topic}}
before it ships. NPS scores use standard bands: Detractor (1-6) = switching cost exceeds net
benefit; Passive (7-8) = net benefit exists but friction is significant; Promoter (9-10) = net
benefit clear, switching friction acceptable.

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
current approach? What is the net benefit vs. the switching cost from the inertia baseline?
The band label must be consistent with the comparison — a Detractor score means switching
cost exceeds net benefit for this persona.]

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
Dominant Detractor objection: [one phrase naming the specific switching-cost or inertia concern
  shared across the most Detractor scores — e.g., "migration effort from existing tooling",
  "setup complexity blocks initial adoption", "capability gap vs. current tool". Name the
  specific pattern; do not restate the band definition. If no Detractors: "No Detractors."]

THEME MATRIX:
| Theme | Personas | Highest Severity |
|-------|----------|-----------------|
| [theme] | [C-NN, ...] | [blocking / major / minor / cosmetic] |

Classify each theme as inertia-driven (switching cost, capability loss, migration friction) or
spec-specific (net-new design objection). Minimum one theme required.

BLOCKING ITEMS:
Collect every item marked [BLOCKING] from the 12 cards. Because blocking items appear at the
top of each card (severity-first ordering), this is a verification pass over each card's leading
feedback item(s).

List: [C-NN] [Name] — [blocking item text]
If no [BLOCKING] items: "No blocking items."

PM READ:
2-3 sentences: what does the Detractor/Passive/Promoter distribution and the dominant Detractor
objection signal for adoption strategy, launch sequencing, and onboarding scope?

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
framing: inertia, a08_field: labeled, aggregate_nps: [value], threshold_met: [true/false].
```

---

## V-02: Combined A-08+A-09 non-phased (lightweight ceiling)

Axis: Combined A-08+A-09 in lightweight non-phased format — V-02 R3 (category bands + dominant
Detractor objection) merged with V-03 R3 per-card `Current approach:` field, with the field
placed before NPS in the card template.
Hypothesis: A 120-point score is achievable without phase structure by combining both new R4
criteria. `Current approach:` before NPS satisfies A-09; `Dominant Detractor objection:` labeled
field in CATEGORY SUMMARY satisfies A-08. Without phases, A-02 (sensitivity analysis), A-04
(ascending NPS order), and A-05 (two-pass revision recs) remain out of reach — those require
Phase 1 pre-scoring and Phase 3 bundled collection. This is the ceiling for lightweight format.
The variation also tests whether the two structural additions (`Current approach:` as first card
field + `Dominant Detractor objection:` in aggregate) interact cleanly — does the labeled
`Current approach:` field make the `Dominant Detractor objection:` more specific because each
persona's current behavior is named explicitly in the cards?
Expected score: 120 (passes A-08 and A-09; fails A-02, A-04, A-05).

```
You are running /listen:feedback for {{Topic}}. Simulate customer reactions to the spec or
design before it ships. NPS scores use standard bands: Detractor (1-6) = switching cost exceeds
net benefit; Passive (7-8) = net benefit exists but friction is significant; Promoter (9-10) =
net benefit clear, switching friction acceptable.

SETUP:
Read the input signal for {{Topic}} — the relevant spec, proposal, or design artifact.
State in 1-2 sentences: what current workflow, tool, or behavior does this feature change or
replace? This is the inertia baseline that every NPS score is measured against.

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
NPS: [1-10] ([Detractor | Passive | Promoter]) — [1-2 sentences: does this feature beat their
  current approach? State the net benefit vs. the switching cost. The band label must be
  consistent with the comparison: a Detractor score means switching cost exceeds net benefit
  for this persona; a Promoter score means net benefit clears switching friction. Persona
  preference description alone does not qualify as a justification.]

Feedback items (descending severity — blocking first):
- blocking: [feedback item text] [BLOCKING]
- major: [feedback item text]
- minor: [feedback item text]
- cosmetic: [feedback item text]
(Only include severity levels that have items. Zero items valid — state "No feedback items.")

For any persona with NPS < 6 (Detractor): include a revision recommendation immediately after
their items:
  Revision rec: [specific, actionable change — name the section, decision, or design choice
  and what to change. Not "improve clarity." Not "simplify." Name the thing and what to do.]

All 12 cards required before any aggregate section.

CATEGORY SUMMARY (after all 12 cards):
Count personas per band:
  Promoters (9-10): [count] — [persona IDs]
  Passives (7-8): [count] — [persona IDs]
  Detractors (1-6): [count] — [persona IDs]
Dominant Detractor objection: [one phrase naming the specific switching-cost or inertia concern
  shared across the most Detractor scores — draw on the `Current approach:` fields above to
  identify the common inertia pattern. E.g., "migration effort from existing tooling",
  "setup complexity blocks initial adoption", "capability gap vs. current tool". Name the
  specific pattern; do not restate the band definition. If no Detractors: "No Detractors."]

THEME MATRIX:
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
2-3 sentences: what do the Detractor/Passive/Promoter distribution, the `Current approach:`
field patterns, and the dominant Detractor objection reveal about adoption strategy, migration
scope, and launch sequencing?

UX READ:
2-3 sentences: what does the gap between `Current approach:` entries and the spec's design
reveal about mental model fit and switching friction? Which Detractor personas face the steepest
conceptual switching cost?

(Neither read contributes to aggregate NPS.)

AGGREGATE NPS:
Compute the mean of all 12 persona NPS scores. Show the calculation.
Threshold: >= 7.0.
State: "Aggregate NPS: [value]. Threshold: 7.0. [Met / Not met]."
If below 7.0: "Spec requires revision before proceeding."

Write artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input, nps_format: categories,
inertia_field: per-card, a08_field: labeled, a09_field: before-nps,
aggregate_nps: [value], threshold_met: [true/false].
```

---

## V-03: A-09 fix in V-05 phase structure (single-axis: card field ordering)

Axis: Card structure — Phase 2 card format restructured so `Current approach:` appears as the
first field in the card body, before NPS, before feedback items. Single targeted change from
V-05 R3: the NPS is no longer in the card header line; the card header is persona ID/name/role
only, followed by `Current approach:`, then NPS, then feedback.
Hypothesis: V-05 R3 Phase 2 placed NPS in the card header (`[C-NN] [Name] ([Role]) | NPS:
[score]`) with `Current approach:` as the second field — NPS first, then named field. Under the
strict A-09 reading ("before NPS and feedback"), this fails. Moving `Current approach:` before
NPS in the card body is the minimal structural fix. This variation tests whether that single
reordering unlocks A-09 without requiring any other changes to the phase structure. If V-03
scores 130 (A-09 now passes, A-08 still fails due to missing dominant Detractor in aggregate),
the card field ordering is confirmed as the sole A-09 blocker in V-05 R3.
Expected score: 130 (gains A-09; fails A-08 — Phase 1 aggregate has counts but no dominant
Detractor objection field).

```
You are running /listen:feedback. Cards are written in ascending NPS order (lowest scorer
first). Within each card, `Current approach:` appears first, then NPS, then feedback items in
descending severity (blocking first). Every NPS score is a named-category comparison against
the status quo. Blocking items are flagged inline and escalated separately. Phase 3 collects
both escalation outputs. Phase 4 synthesizes themes, PM/UX reads, and NPS sensitivity analysis.

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
  Category breakdown:
    Promoters (9-10): [count] — [C-NN, ...]
    Passives (7-8): [count] — [C-NN, ...]
    Detractors (1-6): [count] — [C-NN, ...]
  Threshold: >= 7.0.
  State: "Aggregate NPS: [value]. Result: PASS / FAIL."
  If FAIL: append "REVISION REQUIRED."

Do not proceed to Phase 2 until all 12 scores, their ascending-order list, the category
breakdown, and the aggregate result are stated.

--- PHASE 2: FEEDBACK CARDS ---

Write feedback cards in the same ascending NPS order from Phase 1 (lowest scorer first).
Within each card: `Current approach:` first, then NPS, then feedback items in descending
severity. Only include severity levels that have items.

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
sequence: ascending-nps, card_format: severity-first, a09_field: before-nps,
phases: [score, feedback, escalate, synthesize],
aggregate_nps: [value], threshold_met: [true/false].
```

---

## V-04: A-08 fix in V-05 phase structure (single-axis: aggregate dominant Detractor)

Axis: Aggregate format — Phase 1 aggregate section gains a `Dominant Detractor objection:`
labeled field placed after the category breakdown, naming the specific inertia concern pattern
that drove the most Detractor scores. Single targeted change from V-05 R3.
Hypothesis: V-05 R3 Phase 1 already has category counts (Promoters/Passives/Detractors) and
inertia-framed band definitions, but no named dominant Detractor objection. Adding a single
labeled field in Phase 1 satisfies A-08's final requirement. This is the minimal structural
diff. V-04 also serves as the A-09 ambiguity resolver: V-05 R3 Phase 2 card places NPS in
the header (`[C-NN] [Name] ([Role]) | NPS: [score]`) with `Current approach:` as the second
field — NPS before named field. If the rubric's "before NPS score or feedback items" is
interpreted leniently (passing if `Current approach:` precedes feedback items, even if after
NPS), V-04 passes A-09 and scores 135. If the rubric requires `Current approach:` before
both NPS and feedback, V-04 fails A-09 and scores 130. V-04 is the definitive A-09
interpretation experiment.
Expected score: 130 (strict reading) or 135 (lenient reading of A-09).

```
You are running /listen:feedback. Cards are written in ascending NPS order (lowest scorer
first). Within each card, feedback items are listed in descending severity (blocking first).
Every NPS score is a named-category comparison against the status quo. Phase 1 commits all
scores and names the dominant Detractor objection before any card is written. Blocking items
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
  Category breakdown:
    Promoters (9-10): [count] — [C-NN, ...]
    Passives (7-8): [count] — [C-NN, ...]
    Detractors (1-6): [count] — [C-NN, ...]
  Dominant Detractor objection: [one phrase naming the specific switching-cost or inertia
    concern shared across the most Detractor scores — e.g., "migration cost from existing
    workflow", "setup complexity for initial adopters", "capability gap vs. current tool".
    Not a restatement of the band definition. If no Detractors: "No Detractors."]
  Threshold: >= 7.0.
  State: "Aggregate NPS: [value]. Result: PASS / FAIL."
  If FAIL: append "REVISION REQUIRED."

Do not proceed to Phase 2 until all 12 scores, their ascending-order list, the category
breakdown, the dominant Detractor objection, and the aggregate result are stated.

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
2-3 sentences: what does the Detractor/Passive/Promoter distribution, the dominant Detractor
objection from Phase 1, and the `Current approach:` field patterns signal for adoption strategy,
migration scope, and launch sequencing? Reference specific Phase 1 and Phase 2 findings.

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
sequence: ascending-nps, card_format: severity-first, a08_dominant: phase1,
phases: [score, feedback, escalate, synthesize],
aggregate_nps: [value], threshold_met: [true/false].
```

---

## V-05: Combined ceiling (V-05 R3 + A-08 fix + A-09 fix)

Axis: Combined — Phase 1 aggregate gains `Dominant Detractor objection:` labeled field (A-08
fix); Phase 2 card restructured so `Current approach:` appears before NPS in card body (A-09
fix). All V-05 R3 mechanisms preserved: four-phase structure, ascending NPS pre-scoring, phase
gates, severity-first template, two-checkpoint A-03 verification, two-pass A-05 recs, Phase 4
sensitivity analysis.
Hypothesis: 135/135. Both new R4 criteria are structurally enforced on top of V-05 R3's
existing 125-point structure. A-08: Phase 1 already has band definitions with inertia framing
and category counts; the single addition of `Dominant Detractor objection:` labeled field
completes the criterion. A-09: separating the card header (persona id/name/role only) from card
fields (`Current approach:` first, then NPS) makes the field ordering unambiguous and structurally
guaranteed — the label+colon fields appear in the correct sequence regardless of whether the
model would otherwise embed NPS in the header.
New patterns captured if 135:
- `dominant-detractor-objection-labeled-field-in-aggregate` — phase 1 aggregate names dominant
  inertia objection pattern as a labeled field, not prose; structurally consistent with
  `Current approach:` field format in cards
- `current-approach-before-nps-card-field-ordering` — persona header carries id/name/role only;
  card body fields begin with `Current approach:` then `NPS:` then feedback; ordering
  structurally guaranteed by template sequence
Expected score: 135 (all 9 aspirational criteria pass).

```
You are running /listen:feedback. Cards are written in ascending NPS order (lowest scorer
first). Within each card, `Current approach:` appears first, then NPS, then feedback items in
descending severity (blocking first). Every NPS score is a named-category comparison against
the status quo. Phase 1 commits all scores, category breakdown, and dominant Detractor objection
before any card is written. Phase 3 collects blocking items and revision recs. Phase 4
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
  Category breakdown:
    Promoters (9-10): [count] — [C-NN, ...]
    Passives (7-8): [count] — [C-NN, ...]
    Detractors (1-6): [count] — [C-NN, ...]
  Dominant Detractor objection: [one phrase naming the specific switching-cost or inertia
    concern shared across the most Detractor scores — draw on the Phase 1 rationale sentences
    above to identify the common pattern. E.g., "migration cost from existing workflow",
    "setup complexity for initial adopters", "capability gap vs. current tool". Name the
    specific pattern; do not restate the band definition. If no Detractors: "No Detractors."]
  Threshold: >= 7.0.
  State: "Aggregate NPS: [value]. Result: PASS / FAIL."
  If FAIL: append "REVISION REQUIRED."

Do not proceed to Phase 2 until all 12 scores, their ascending-order list, the category
breakdown, the dominant Detractor objection, and the aggregate result are stated.

--- PHASE 2: FEEDBACK CARDS ---

Write feedback cards in the same ascending NPS order from Phase 1 (lowest scorer first).
Within each card: `Current approach:` first, then NPS, then feedback items in descending
severity. Only include severity levels that have items.

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
2-3 sentences: what does the Detractor/Passive/Promoter distribution, the dominant Detractor
objection from Phase 1, and the `Current approach:` field patterns signal for adoption strategy,
migration scope, and launch sequencing? Reference specific Phase 1 and Phase 2 findings.

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
a08_dominant: phase1, a09_field: before-nps,
phases: [score, feedback, escalate, synthesize],
aggregate_nps: [value], threshold_met: [true/false].
```

---

## v4 rubric coverage map

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
| A-02 NPS sensitivity analysis | FAIL | FAIL | PASS | PASS | PASS |
| A-03 Inline [BLOCKING] flags | PASS | PASS | PASS | PASS | PASS |
| A-04 Ascending NPS ordering | FAIL | FAIL | PASS | PASS | PASS |
| A-05 Two-pass revision recs | FAIL | FAIL | PASS | PASS | PASS |
| A-06 Inertia-baseline NPS | PASS | PASS | PASS | PASS | PASS |
| A-07 Severity-first within card | PASS | PASS | PASS | PASS | PASS |
| A-08 Category bands + dominant | PASS | PASS | FAIL | PASS | PASS |
| A-09 Current approach: before NPS | FAIL | PASS | PASS | FAIL* | PASS |
| **Score** | **115** | **120** | **130** | **130*** | **135** |

*V-04 A-09: FAIL under strict reading ("before NPS and feedback" — AND); PASS under lenient
reading ("before NPS score or feedback items" — OR, preceding feedback items suffices).
V-04 is the definitive A-09 interpretation experiment. If V-04 scores 135, the lenient reading
applies and all current phased variations already pass A-09 by having `Current approach:` before
feedback items. If V-04 scores 130, the strict reading applies and A-09 requires `Current
approach:` to precede NPS in the card body — V-05's explicit ordering is then the load-bearing
fix.

---

## Recommended scoring order

V-01 → V-02 → V-03 → V-04 → V-05.

- **V-01 first**: establishes whether the A-08 labeled field format (`Dominant Detractor
  objection:`) is more reliable than the V-02 R3 prose instruction. If V-01 passes A-08,
  it confirms that a non-phased variation can reach 115 via labeled field.
- **V-02 second**: tests the non-phased ceiling (120) by combining A-08 labeled field +
  A-09 `Current approach:` before NPS. Confirms that lightweight format handles both new
  criteria without interference.
- **V-03 third**: isolates A-09 in the phase structure. If V-03 scores 130, card field
  ordering is confirmed as the sole A-09 gap in V-05 R3.
- **V-04 fourth**: isolates A-08 in the phase structure AND resolves the A-09 strict/lenient
  ambiguity. Score 135 = lenient reading, 130 = strict reading.
- **V-05 last**: ceiling attempt. Validates both new R4 patterns under full phase structure.
  Should score 135 regardless of V-04's A-09 outcome, since V-05 puts `Current approach:`
  before NPS explicitly.
