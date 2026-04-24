## listen-feedback R6 — 5 Variations

**Context:** R5 V-05 = 145/145 under v5 rubric; already passes A-12 and A-13 under v6, so baseline is 155/155. R6 tests A-12/A-13 robustness specifically.

| # | Axis | Predicted |
|---|------|-----------|
| V-01 | **Explicit synthesis-order constraint** — preamble block naming exact Phase 3 section order + terminal declaration | **155** |
| V-02 | **Sensitivity analysis nested inside THEME MATRIX** — A-13 terminal by construction, A-02 content preserved | **155** |
| V-03 | **Soft synthesis phrasing** — Phase 1/2 imperative gates preserved; Phase 3 descriptive/guidance register | **150** |
| V-04 | **Combined** — V-01 + V-02 (double-enforcement of A-12/A-13) | **155** |
| V-05 | **Combined** — V-01 + V-02 + V-03 (compensation test: does preamble constraint override soft Phase 3?) | **155** |

---

**Key design decisions:**

**V-01** adds a `SYNTHESIS ORDER CONSTRAINT` block to the preamble listing all 6 sections in order with "UX READ must appear before PM READ" and "THEME MATRIX is the terminal section: no substantive analysis appears after it" as explicit pre-commitments before any phase begins.

**V-02** restructures Phase 3 from 6 peer sections to 5 — NPS SENSITIVITY ANALYSIS moves inside THEME MATRIX as a "Leverage personas" sub-section below the table. THEME MATRIX is structurally last because nothing can follow it. A-02 content survives (2-3 leverage personas + ROI estimate still required); only the section boundary changes.

**V-03** is the adversarial axis. Phase 3 switches to guidance language ("The analysis phase synthesizes... begin with escalations... conclude with the theme matrix"). Tests whether A-12 (UX before PM) has the same fragility to soft phrasing as A-04 had in R5 V-01. PM-before-UX is a natural default model tendency — the executive summary frame leads with PM synthesis. A-13 (matrix terminal) is lower risk because "conclude with" has unambiguous positional meaning.

**V-05** is the compensation test: if V-03 scores 150 (A-12 fails), does the V-01 preamble constraint ("UX READ must appear before PM READ. These positions are fixed regardless of output length.") restore compliance even with soft Phase 3 phrasing? Result determines whether preamble pre-commitments or local instruction register is the load-bearing mechanism for ordering compliance.

**Recommended scoring order:** V-03 → V-01 → V-02 → V-04 → V-05 — adversarial axis first, then controls, then compensation test last.

models sometimes lead with the more adoption-strategic PM frame first. A-13 (matrix terminal)
is lower risk because "concluding with the theme matrix" has a clear positional meaning even in
descriptive register.

**Compensation test in V-05:** If V-03 scores 150 (A-12 fails), V-05 tests whether the
explicit constraint header from V-01 restores A-12 compliance even with soft Phase 3 phrasing.
If V-05 scores 155, the explicit constraint header is confirmed as load-bearing for A-12
reliability — it can be used to harden any soft-register variation.

**Recommended scoring order:** V-03 → V-01 → V-02 → V-04 → V-05.
Rationale: V-03 tests the adversarial axis first to establish whether A-12/A-13 are fragile
under soft phrasing. V-01 and V-02 are expected-155 controls. V-04 and V-05 depend on knowing
whether V-01/V-02/V-03 hit their predicted scores.

---

## V-01: Explicit synthesis-order constraint

Axis: Explicit sequence annotation — add a SYNTHESIS ORDER CONSTRAINT block to the preamble,
listing the exact Phase 3 section order and naming THEME MATRIX as the terminal section. No
structural changes to the prompt body; the constraint block makes A-12 and A-13 explicit as
preamble requirements rather than implicit from section ordering instructions in Phase 3.
Hypothesis: Making A-12 and A-13 explicit in the preamble (before any phase begins) prevents
model drift during long outputs where the model may reorder Phase 3 sections if the synthesis
framing feels more natural in a different order. The preamble constraint functions as a
pre-commitment that applies globally, whereas section-level ordering instructions apply only
locally within Phase 3 — shorter scope, easier to lose under long generation. Expected score:
155 (all criteria pass; preamble constraint is a robustness addition with no criterion cost).

```
You are running /listen:feedback for {{Topic}}. The organizing question is: does this proposal
beat the status quo for each persona? Every persona already has a default workflow, tool, or
habit that this feature asks them to change. A Detractor (1-6) is someone whose switching cost
exceeds the net benefit of changing; a Passive (7-8) finds marginal net benefit with real
friction; a Promoter (9-10) sees net benefit that clearly outweighs switching friction.

SYNTHESIS ORDER CONSTRAINT: In Phase 3, sections must appear in exactly this order —
(1) BLOCKING ITEMS, (2) REVISION RECS SUMMARY, (3) UX READ, (4) PM READ,
(5) NPS SENSITIVITY ANALYSIS, (6) THEME MATRIX.
THEME MATRIX is the terminal section: no substantive analysis appears after it.
UX READ must appear before PM READ. These positions are fixed regardless of output length.

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

Complete all six sections in order per the SYNTHESIS ORDER CONSTRAINT stated above.
No section may be omitted.

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
| Theme | Personas | Highest Severity | Type |
|-------|----------|-----------------|------|
| [theme] | [C-NN, ...] | [blocking / major / minor / cosmetic] | [inertia-driven / spec-specific] |
Minimum one theme. No section follows this one.

Write artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input,
framing: status-quo-comparison, nps_format: categories, inertia_field: per-card,
sequence: ascending-nps, card_format: current-approach-first,
a10_field: labeled, a11_header: id-name-role-only,
synthesis_constraint: explicit-preamble, role_sequence: ux-before-pm, theme_matrix: terminal,
phases: [status-quo-comparison, per-persona-cards, analysis],
aggregate_nps: [value], threshold_met: [true/false].
```

---

## V-02: Sensitivity analysis nested inside THEME MATRIX

Axis: NPS sensitivity analysis placement — move NPS SENSITIVITY ANALYSIS from its own peer
section in Phase 3 (position 5 of 6) to inside the THEME MATRIX block as a "Leverage" sub-
section below the matrix table. The THEME MATRIX section becomes: (a) inertia baseline
statement, (b) matrix table, (c) leverage personas + ROI recommendation. Nothing follows the
THEME MATRIX block. R5 V-05 structure otherwise unchanged.
Hypothesis: A-13 pass condition is "no major analysis section appears after the theme matrix."
If sensitivity analysis is a sub-section inside THEME MATRIX — not a peer section after it —
A-13 passes by construction. The relevant question is whether A-02 still passes: A-02 requires
the 2-3 leverage personas and a highest-ROI change estimate. The content remains present; only
the section boundary changes. R-02 (PM + UX reads) and A-12 (UX before PM) are unaffected:
UX READ and PM READ remain as peer sections in Phase 3 positions 3 and 4, before the matrix
block. Expected score: 155 (A-02 passes on content; A-13 passes by construction; A-12
unaffected).

```
You are running /listen:feedback for {{Topic}}. The organizing question is: does this proposal
beat the status quo for each persona? Every persona already has a default workflow, tool, or
habit that this feature asks them to change. A Detractor (1-6) is someone whose switching cost
exceeds the net benefit of changing; a Passive (7-8) finds marginal net benefit with real
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

Complete all five sections in order. No section may be omitted.

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

THEME MATRIX:
Build from Phase 2 feedback, informed by the UX and PM reads above. Annotate each theme with
highest severity. Classify as inertia-driven (status-quo attachment, switching cost, migration
friction) or spec-specific (net-new design objection).

| Theme | Personas | Highest Severity | Type |
|-------|----------|-----------------|------|
| [theme] | [C-NN, ...] | [blocking / major / minor / cosmetic] | [inertia-driven / spec-specific] |

Minimum one theme.

Leverage personas (NPS sensitivity):
Identify the 2-3 personas from the matrix whose scores most influence the aggregate NPS — the
highest-ROI revision targets. For each:
  [C-NN] [Name] — NPS: [score] ([band]) — Why leverage: [low base, cluster representative, or
  single addressable switching-cost objection from their status-quo verdict]
  Highest-ROI change: [one spec change most likely to move their band — reference `Current
  approach:` and revision rec if present]
Single highest-ROI change: [change] — estimated aggregate NPS lift: ~[delta], from [current]
to approximately [projected].

Write artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input,
framing: status-quo-comparison, nps_format: categories, inertia_field: per-card,
sequence: ascending-nps, card_format: current-approach-first,
a10_field: labeled, a11_header: id-name-role-only,
role_sequence: ux-before-pm, theme_matrix: terminal,
sensitivity_placement: inside-matrix,
phases: [status-quo-comparison, per-persona-cards, analysis],
aggregate_nps: [value], threshold_met: [true/false].
```

---

## V-03: Soft synthesis phrasing in Phase 3 only

Axis: Phrasing register for Phase 3 — Phase 1 and Phase 2 preserve imperative blocking
language ("Do not proceed to Phase 2 until..."; card format "strictly in this order"). Phase 3
switches to descriptive/guidance language: section names are preserved as headers, but the
instructions are framed as guidance ("The analysis should begin with...", "Conclude with the
theme matrix as the final synthesis section.") rather than as constraints. No content removed.
Hypothesis: A-12 (UX before PM) and A-13 (matrix terminal) both depend on within-Phase 3
section ordering. Imperative Phase 3 framing in R5 V-05 lists sections in order and says
"Complete all six sections in order. No section may be omitted." Soft framing replaces this
with guidance. Risk: under long outputs, models occasionally front-load the synthesis (writing
the theme matrix early, or leading Phase 3 with the PM frame because it feels like the
strategic summary). A-12 is higher risk than A-13 because PM-before-UX is a natural default
(PM synthesis reads as the "executive summary" that many templates lead with). A-13 is lower
risk because "conclude with the theme matrix" has a clear positional meaning even in guidance
language. Expected score: 150 (A-12 fails under soft Phase 3 framing; all other criteria pass).

```
You are running /listen:feedback for {{Topic}}. The organizing question is: does this proposal
beat the status quo for each persona? Every persona already has a default workflow, tool, or
habit that this feature asks them to change. A Detractor (1-6) is someone whose switching cost
exceeds the net benefit of changing; a Passive (7-8) finds marginal net benefit with real
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

The analysis phase synthesizes all Phase 1 and Phase 2 findings into six sections. Each section
should be completed in full before moving to the next. The sections flow from escalation
(blocking items and revision recs) through professional lenses (UX perspective first, then PM
perspective drawing on it), then sensitivity, and conclude with the theme matrix as the final
cross-persona synthesis.

BLOCKING ITEMS:
Pull out every [BLOCKING]-tagged item from Phase 2 and list them here. Blocking items are the
first feedback item in any card that has one — look for the inline [BLOCKING] tag. If there are
none, state that explicitly.
Format: [C-NN] [Name] (NPS [score], [band]) — [blocking item text]

REVISION RECS SUMMARY:
Gather every REVISION REC written in Phase 2 for personas whose NPS was below 6. If no
personas scored below 6, state that explicitly.
Format: [C-NN] [Name] (NPS [score]) — [revision rec text]

UX READ:
From the UX design perspective, what does the spread of `Current approach:` entries reveal
about switching friction and mental model fit? Which Detractor personas face the steepest
conceptual transition, and what specific design assumption in the spec creates that gap?
(2-3 sentences)

PM READ:
Drawing on the UX friction analysis above and the Phase 1 distribution, what does the dominant
Detractor objection and the `Current approach:` pattern say about adoption strategy, migration
scope, and launch sequencing? (2-3 sentences)

NPS SENSITIVITY ANALYSIS:
Which 2-3 personas most drive the aggregate NPS, and what single spec change would move it
most? For each leverage persona:
  [C-NN] [Name] — NPS: [score] ([band]) — Why leverage: [low base, cluster representative, or
  shared addressable switching-cost objection]
  Highest-ROI change: [specific change grounded in `Current approach:` and revision rec]
State: "Single highest-ROI change: [change] — estimated aggregate NPS lift: ~[delta], from
[current] to approximately [projected]."

THEME MATRIX:
Conclude with the cross-persona theme matrix as the final synthesis. Build from Phase 2
feedback, informed by the UX and PM reads. Annotate each theme with highest severity. Classify
as inertia-driven or spec-specific.
| Theme | Personas | Highest Severity | Type |
|-------|----------|-----------------|------|
| [theme] | [C-NN, ...] | [blocking / major / minor / cosmetic] | [inertia-driven / spec-specific] |
Minimum one theme.

Write artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input,
framing: status-quo-comparison, nps_format: categories, inertia_field: per-card,
sequence: ascending-nps, card_format: current-approach-first,
a10_field: labeled, a11_header: id-name-role-only,
role_sequence: ux-before-pm, theme_matrix: terminal,
synthesis_register: descriptive,
phases: [status-quo-comparison, per-persona-cards, analysis],
aggregate_nps: [value], threshold_met: [true/false].
```

---

## V-04: Combined — explicit constraint (V-01) + sensitivity inside matrix (V-02)

Axis: V-01 preamble constraint block + V-02 sensitivity-in-matrix restructure. The explicit
SYNTHESIS ORDER CONSTRAINT no longer lists NPS SENSITIVITY ANALYSIS as a peer section (since
it moves inside THEME MATRIX), so the constraint is updated to 5 positions: (1) BLOCKING ITEMS,
(2) REVISION RECS SUMMARY, (3) UX READ, (4) PM READ, (5) THEME MATRIX (terminal, includes
leverage analysis). THEME MATRIX is both explicitly declared terminal in the constraint and
structurally terminal via sensitivity being nested inside it.
Hypothesis: Two complementary mechanisms for A-13 compliance: (1) explicit preamble constraint
naming THEME MATRIX as terminal, (2) nothing follows the matrix structurally because sensitivity
analysis is absorbed inside it. A-12 also has two enforcement points: preamble constraint
("UX READ must appear before PM READ") and Phase 3 section ordering. Double-enforcement should
be the most reliable A-12/A-13 combination. Expected score: 155.

```
You are running /listen:feedback for {{Topic}}. The organizing question is: does this proposal
beat the status quo for each persona? Every persona already has a default workflow, tool, or
habit that this feature asks them to change. A Detractor (1-6) is someone whose switching cost
exceeds the net benefit of changing; a Passive (7-8) finds marginal net benefit with real
friction; a Promoter (9-10) sees net benefit that clearly outweighs switching friction.

SYNTHESIS ORDER CONSTRAINT: In Phase 3, sections must appear in exactly this order —
(1) BLOCKING ITEMS, (2) REVISION RECS SUMMARY, (3) UX READ, (4) PM READ,
(5) THEME MATRIX (terminal; includes leverage analysis sub-section).
UX READ must appear before PM READ. THEME MATRIX is the final section: nothing follows it.

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

Complete all five sections in order per the SYNTHESIS ORDER CONSTRAINT stated above.
No section may be omitted.

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

THEME MATRIX:
Build from Phase 2 feedback, informed by the UX and PM reads above. Annotate each theme with
highest severity. Classify as inertia-driven (status-quo attachment, switching cost, migration
friction) or spec-specific (net-new design objection).

| Theme | Personas | Highest Severity | Type |
|-------|----------|-----------------|------|
| [theme] | [C-NN, ...] | [blocking / major / minor / cosmetic] | [inertia-driven / spec-specific] |

Minimum one theme.

Leverage personas (NPS sensitivity):
Identify the 2-3 personas from the above whose scores most influence the aggregate NPS. For
each:
  [C-NN] [Name] — NPS: [score] ([band]) — Why leverage: [low base, cluster representative, or
  single addressable switching-cost objection shared with other Detractors]
  Highest-ROI change: [one spec change most likely to move their band — reference `Current
  approach:` and revision rec if present]
Single highest-ROI change: [change] — estimated aggregate NPS lift: ~[delta], from [current]
to approximately [projected].

Write artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input,
framing: status-quo-comparison, nps_format: categories, inertia_field: per-card,
sequence: ascending-nps, card_format: current-approach-first,
a10_field: labeled, a11_header: id-name-role-only,
synthesis_constraint: explicit-preamble, role_sequence: ux-before-pm, theme_matrix: terminal,
sensitivity_placement: inside-matrix,
phases: [status-quo-comparison, per-persona-cards, analysis],
aggregate_nps: [value], threshold_met: [true/false].
```

---

## V-05: Combined — explicit constraint (V-01) + sensitivity inside matrix (V-02) + soft synthesis phrasing (V-03)

Axis: All three single-axis axes combined. Explicit SYNTHESIS ORDER CONSTRAINT in preamble
(V-01) + sensitivity analysis nested inside THEME MATRIX (V-02) + Phase 3 written in
descriptive/guidance register (V-03). Phase 1 and Phase 2 remain imperative. The compensation
test: if V-03 alone scores 150 (A-12 fails under soft Phase 3 phrasing), does the explicit
preamble constraint from V-01 restore A-12 compliance?
Hypothesis: The preamble constraint ("UX READ must appear before PM READ. These positions are
fixed regardless of output length.") is a pre-commitment that applies before Phase 3 is written.
Even when Phase 3 guidance-language suggests "begin with the UX perspective," the preamble has
already declared the ordering as fixed. If the model respects pre-commitments over local
guidance, V-05 scores 155. If soft Phase 3 phrasing overrides the preamble constraint, V-05
scores 150 (same as V-03). This creates a falsifiable test: the preamble constraint either
compensates for soft Phase 3 phrasing or it does not. Expected score: 155.

```
You are running /listen:feedback for {{Topic}}. The organizing question is: does this proposal
beat the status quo for each persona? Every persona already has a default workflow, tool, or
habit that this feature asks them to change. A Detractor (1-6) is someone whose switching cost
exceeds the net benefit of changing; a Passive (7-8) finds marginal net benefit with real
friction; a Promoter (9-10) sees net benefit that clearly outweighs switching friction.

SYNTHESIS ORDER CONSTRAINT: In Phase 3, sections must appear in exactly this order —
(1) BLOCKING ITEMS, (2) REVISION RECS SUMMARY, (3) UX READ, (4) PM READ,
(5) THEME MATRIX (terminal; includes leverage analysis sub-section).
UX READ must appear before PM READ. THEME MATRIX is the final section: nothing follows it.
These positions are fixed regardless of output length.

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

The analysis phase synthesizes all Phase 1 and Phase 2 findings per the SYNTHESIS ORDER
CONSTRAINT stated above. Five sections, in order. Each should be complete before moving to the
next.

BLOCKING ITEMS:
Pull out every [BLOCKING]-tagged item from Phase 2. Blocking items appear first in any card
that has one — look for the inline [BLOCKING] tag. State results explicitly even if empty.
Format: [C-NN] [Name] (NPS [score], [band]) — [blocking item text]

REVISION RECS SUMMARY:
Gather every REVISION REC written in Phase 2 for personas with NPS below 6. State explicitly
if none.
Format: [C-NN] [Name] (NPS [score]) — [revision rec text]

UX READ:
From the UX design perspective, what does the spread of `Current approach:` entries reveal
about switching friction and mental model fit? Which Detractor personas face the steepest
conceptual transition, and what specific design assumption in the spec creates that gap?
(2-3 sentences)

PM READ:
Drawing on the UX friction analysis above and the Phase 1 distribution, what does the dominant
Detractor objection and the `Current approach:` pattern say about adoption strategy, migration
scope, and launch sequencing? (2-3 sentences)

THEME MATRIX:
Conclude with the cross-persona theme matrix as the final synthesis. Build from Phase 2
feedback, informed by the UX and PM reads. Annotate each theme with highest severity. Classify
as inertia-driven or spec-specific.

| Theme | Personas | Highest Severity | Type |
|-------|----------|-----------------|------|
| [theme] | [C-NN, ...] | [blocking / major / minor / cosmetic] | [inertia-driven / spec-specific] |

Minimum one theme.

Leverage personas (NPS sensitivity):
Which 2-3 personas most drive the aggregate NPS, and what single change would move it most?
  [C-NN] [Name] — NPS: [score] ([band]) — Why leverage: [low base, cluster representative, or
  shared addressable switching-cost objection]
  Highest-ROI change: [specific change grounded in `Current approach:` and revision rec]
Single highest-ROI change: [change] — estimated aggregate NPS lift: ~[delta], from [current]
to approximately [projected].

Write artifact to simulations/listen/feedback/{topic}-feedback-{date}.md.
Frontmatter: skill: listen-feedback, topic, date, input,
framing: status-quo-comparison, nps_format: categories, inertia_field: per-card,
sequence: ascending-nps, card_format: current-approach-first,
a10_field: labeled, a11_header: id-name-role-only,
synthesis_constraint: explicit-preamble, role_sequence: ux-before-pm, theme_matrix: terminal,
sensitivity_placement: inside-matrix, synthesis_register: descriptive,
phases: [status-quo-comparison, per-persona-cards, analysis],
aggregate_nps: [value], threshold_met: [true/false].
```

---

## v6 rubric coverage map (predicted)

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
| A-02 NPS sensitivity analysis | PASS | PASS | PASS | PASS | PASS |
| A-03 Inline [BLOCKING] | PASS | PASS | PASS | PASS | PASS |
| A-04 Ascending NPS order | PASS | PASS | PASS | PASS | PASS |
| A-05 Two-pass revision recs | PASS | PASS | PASS | PASS | PASS |
| A-06 Inertia baseline NPS | PASS | PASS | PASS | PASS | PASS |
| A-07 Severity-first within card | PASS | PASS | PASS | PASS | PASS |
| A-08 Band labels + distribution | PASS | PASS | PASS | PASS | PASS |
| A-09 `Current approach:` field | PASS | PASS | PASS | PASS | PASS |
| A-10 `Dominant Detractor objection:` | PASS | PASS | PASS | PASS | PASS |
| A-11 Header id/name/role only | PASS | PASS | PASS | PASS | PASS |
| A-12 UX READ before PM READ | PASS | PASS | FAIL* | PASS | PASS** |
| A-13 Theme matrix as terminal | PASS | PASS | PASS | PASS | PASS |
| **Predicted score** | **155** | **155** | **150** | **155** | **155** |

*V-03 predicted A-12 fail: soft Phase 3 framing ("begin with the UX perspective, then PM
perspective drawing on it") is a preference, not a constraint. Under long outputs, the PM READ
tends to be written first as the "executive summary" frame. The THEME MATRIX terminal position
("conclude with the theme matrix") has a clearer positional meaning — A-13 is predicted to
survive soft phrasing.

**V-05 A-12: compensation test. The explicit preamble constraint ("UX READ must appear before
PM READ. These positions are fixed regardless of output length.") is a pre-commitment made
before Phase 3 begins. If preamble pre-commitments override local guidance-language during
generation, A-12 passes and V-05 scores 155. If the descriptive Phase 3 register weakens
compliance despite the preamble constraint, V-05 scores 150 (same as V-03), proving preamble
constraints cannot compensate for soft local instructions.

---

## Recommended scoring order

V-03 → V-01 → V-02 → V-04 → V-05.

- **V-03 first**: the adversarial axis. If V-03 scores 150 (A-12 fails), confirms that A-12
  has the same soft-phrasing fragility as A-04. Establishes which mechanism (preamble vs.
  local instruction) is load-bearing. If V-03 scores 155, soft synthesis phrasing is safe and
  all four other variations are expected-155 confirmations.
- **V-01 second**: expected-155 control. Confirms explicit preamble constraint doesn't
  inadvertently create any criterion cost (all criteria should still pass with an extra
  constraint block in preamble). If V-03 scored 150, V-01 being 155 shows the preamble
  constraint alone is sufficient to fix V-03's failure.
- **V-02 third**: expected-155 structural variation. Confirms sensitivity-inside-matrix
  satisfies A-02 content requirement and strengthens A-13 by construction.
- **V-04 fourth**: double-enforcement control. If both V-01 and V-02 hit 155, V-04 should
  also hit 155 with no interference.
- **V-05 last**: the compensation test. If V-03 scored 150, V-05 answers: does the V-01
  preamble constraint rescue A-12 under V-03's soft Phase 3 register? Score of 155 = yes,
  preamble pre-commitments override local guidance. Score of 150 = no, local register is the
  load-bearing instruction level for A-12 ordering.
