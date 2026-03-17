# topic-plan Skill Variations — Round 19 (2026-03-16)

Rubric: v19 (C-56 Downstream inertia recurrence as named labeled blocks;
C-57 Per-step analytical purpose declaration "This step exists so that...")

Three single-axis variations (V-01, V-02, V-03) then two combinations (V-04, V-05).

---

## V-01: Inertia Framing — Site-labeled INERTIA-GATE block headers (C-56)

**Variation axis**: Inertia framing — each INERTIA-GATE reproduction site
carries a unique numbered site label in the block header (e.g., "INERTIA-GATE
[SITE 1 of 3: Step 4]"), making each recurrence point independently scannable
by block label without reading surrounding step content. The template defines
the label slot and enumerates all three site labels in its closing verification
line. Reproducing the block at a site requires filling the slot with the
correct site-specific label — a blank or wrong label is visibly incorrect.

**Hypothesis**: R18 V-01 established that verbatim blocks are structurally
visible at presence/absence resolution — a missing block is a missing section.
C-56 requires a finer resolution: independently scannable by label, meaning
each block is identifiable at header-scan level without reading body text. A
block labelled "INERTIA-GATE" at all three sites is scannable for count but
not for site identity — you cannot distinguish site 1 from site 3 without
reading surrounding context. A numbered site label ("INERTIA-GATE [SITE 2 of
3: Step 4b]") makes site identity a header-level property: a reader who scans
only block headers can verify which of the three gates is present or missing
without reading step text. This tests whether the labeled-header extension
changes compliance behavior beyond the verbatim-block requirement alone.

```
The result of this skill may be zero changes, some changes, or a full strategy
replacement. Inertia is a co-equal option, not a fallback. The burden of proof
rests on change, not on stability.

---

You are running /topic:plan for the topic named in the user's message.

---

## COLUMN CONTRACT

Rule 1 — Enumerated column values
Valid values (select one; prose is not valid):
  Action: ADD / REMOVE / REPRIORITIZE [Rule 1]
  Challenge strength: Strong / Moderate / Weak [Rule 1]
  Reversibility: Reversible at same cost / Gets harder / Becomes impossible [Rule 1]
  Delta-candidate: Yes / No / Pending signal [Rule 1]
PASS: "Weak" — FAIL: "weak challenge, mostly"

Rule 2 — Column independence
Test: Can I fill this cell without reading the source document?
PASS: "Team assumed biweekly review cadence prevents drift accumulation"
FAIL: "Assumption A evidence" (row-key reconstruction)

Rule 3 — Null-case enforcement
All null-case declarations must carry a change-type label. Each absent change
type must have its own independently labeled declaration. A single unlabeled
"No changes proposed" covering multiple change types fails Rule 3.
At each null site: use the verbatim type-labeled null text provided.
"Do not omit this declaration" appears at each null site.
PASS: "ADDITIONS: none — inertia holds for all candidate additions."
FAIL: "No changes proposed." (unlabeled — ambiguous across change types)

Rule 4 — Delta Finding traceability
Delta Finding column mandatory in all proposal rows.
Format: "Strategy assumed [X] / Signal revealed [Y]."
Null rows: "Delta Finding: N/A."
PASS: "Strategy assumed weekly cadence / Signal revealed daily drift frequency"
FAIL: "scout-feasibility-2026-03-14.md" (single-hop, assumption not surfaced)

Rule 5 — Symmetric inertia-rejection justification
Column name: Inertia Rejected Because [REQUIRED]
Required in ALL change-type proposal tables (Step 4a and Step 4b).
Schema: identical column name, identical REQUIRED status, identical
prose-prohibition rule across both tables.
Format: one sentence naming the specific signal evidence or logic that defeats
the keep-unchanged option.
PASS: specific named signal with deferral consequence stated.
FAIL: "compelling argument exists" (generic, non-specific, prose substitute)
FAIL: "Why this beats NO CHANGE" (wrong column name — not a valid substitute)
The REQUIRED label is part of the enforcement contract. Do not merge the two
tables. Do not rename the column in either table.

---

## INERTIA-GATE TEMPLATE

This template must be reproduced verbatim at each of the three numbered sites
below. At each site, fill the SITE slot with the site-specific label shown in
the step instruction. The site label makes each gate independently scannable
by header without reading surrounding step text.

  ┌──────────────────────────────────────────────────────────────────────────┐
  │ INERTIA-GATE [SITE: _______________________________________]             │
  │ The result of this step may leave this section unchanged.               │
  │ Inertia is a co-equal option. The burden of proof rests on change.      │
  │                                                                          │
  │ Verification: three INERTIA-GATE blocks in this output, at sites:       │
  │   [SITE 1 of 3: Step 4 — Before proposals]                              │
  │   [SITE 2 of 3: Step 4b — Before removals/reprioritizations]            │
  │   [SITE 3 of 3: Step 7 — Before confirmation]                           │
  └──────────────────────────────────────────────────────────────────────────┘

---

## Upfront Output Schema

Commit to this schema before reading any file.

**Assumption table** (Step 1b)
| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

**Signal inventory** (Step 3)
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**Delta findings** (Step 3b)
| Finding ID | Strategy assumed | Signal revealed | Source artifact | Delta-candidate [Rule 1] |

**Additions table** (Step 4a)
| # | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

**Removals and Reprioritizations table** (Step 4b)
| # | Action [Rule 1] | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

**Defender Challenge Table** (Step 4c)
| Defense ID | Proposal # | Strategic decision defended | Defensive argument | Defense basis | Challenge strength [Rule 1] |

**Conflict audit** (Step 5)
| Conflict ID | Signal A | Signal B | Nature of conflict | Resolution |

**Diff table** (Step 6)
| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

Pre-read commitment: columns above are fixed. No prose substitutes.
No table merges. I will not merge Step 4a and 4b.

---

## Step 1 — Read strategy.md and extract assumptions

Read `simulations/TOPICS.md` to locate the strategy file path. Read
strategy.md (STRATEGY DATE = last-modified date).

Extract stated dimensions. Scan: scope of coverage / sequencing /
completion criteria / success thresholds.
Apply Rule 2 before populating each Implicit evidence cell.

| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

Null (Rule 3, type-labeled): "ASSUMPTIONS: none — no implicit assumptions
identified; all strategy elements are explicitly stated."
Do not omit this declaration.

---

## Step 2 — Pre-signal Defense Register

Output before reading any NEW artifact.

| Defense ID | Strategic decision | Strongest keep-it argument | What would invalidate |

---

## Step 3 — Signal inventory

List every artifact in `simulations/` matching the topic slug. Classify NEW
(date > STRATEGY DATE) or PRIOR. All 9 namespaces must be explicitly
assessed: scout / draft / review / flow / trace / prove / listen / program /
topic.

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**SIGNAL READ-LOCK**: Signal files may not be re-read after this step.
All subsequent steps use the written inventory only.

Null (Rule 3, type-labeled): "SIGNAL INVENTORY: null — no artifacts found
for topic [name]. Cannot run /topic:plan."
Do not omit this declaration.

---

## Step 3b — Delta findings

For each NEW artifact, one row per substantive finding:

| Finding ID | Strategy assumed | Signal revealed | Source artifact | Delta-candidate [Rule 1] |

Null (Rule 3, type-labeled): "DELTA FINDINGS: null — no NEW artifacts exist.
Strategy is current."
Do not omit this declaration.

---

## Step 4 — Change proposals (preamble)

Reproduce the INERTIA-GATE block verbatim with SITE label:
  INERTIA-GATE [SITE 1 of 3: Step 4 — Before proposals]

A proposal that cannot name a concrete consequence of deferral (the "If
unchanged" column) is a preference, not a decision — structurally invalid,
not merely incomplete.

---

## Step 4a — Additions

"Inertia Rejected Because [REQUIRED]": one sentence per row naming the
specific evidence or logic defeating the keep-unchanged option (Rule 5).
PASS: specific signal evidence named — FAIL: "compelling reason"

| # | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

Null (Rule 3, type-labeled): "ADDITIONS: none — inertia holds."
Do not omit this declaration.

---

## Step 4b — Removals and Reprioritizations

Reproduce the INERTIA-GATE block verbatim with SITE label:
  INERTIA-GATE [SITE 2 of 3: Step 4b — Before removals/reprioritizations]

"Inertia Rejected Because [REQUIRED]": identical schema to Step 4a (Rule 5).
FAIL: "compelling reason" or any prose substitute.

| # | Action [Rule 1] | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

Null declarations (Rule 3, type-labeled):
  "REMOVALS: none — inertia holds. Do not omit this declaration."
  "REPRIORITIZATIONS: none — inertia holds. Do not omit this declaration."

---

## Step 4c — Defender Challenge Table

A table where every challenge is Weak is a structural signal of rubber-stamp
processing, not genuine evaluation.

Defense basis: D-ID if pre-registered; "Newly constructed" if built after
signal reading.

| Defense ID | Proposal # | Strategic decision defended | Defensive argument | Defense basis | Challenge strength [Rule 1] |

**Calibration check** (required artifact): After completing the table,
produce one sentence:
  - All Weak → "Calibration: rubber-stamp risk — all challenges are Weak."
  - All Strong → "Calibration: over-zealous risk — all challenges are Strong."
  - Otherwise → "Calibration: balanced — challenge strength distribution is varied."

---

## Step 5 — Conflict audit

Identify any NEW artifacts that contradict each other on the same strategy
dimension.

| Conflict ID | Signal A | Signal B | Nature of conflict | Resolution |

Null (Rule 3, type-labeled): "CONFLICT AUDIT: none — no contradictions
detected between NEW artifacts on the same strategy dimension."
Do not omit this declaration.

---

## Step 6 — Before/after diff

Include [evidence brackets] in each After cell and Proposal cross-refs
(e.g., "ADD-1") per row.

| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

---

## Step 7 — Confirmation gate

Reproduce the INERTIA-GATE block verbatim with SITE label:
  INERTIA-GATE [SITE 3 of 3: Step 7 — Before confirmation]
NO is a complete and valid outcome.

Display: Step 3b / Step 4a / Step 4b / Step 4c (with calibration check) /
Step 6.

Individual proposals may be withdrawn before gate execution. Reply YES
applies only to non-withdrawn proposals.

Write exactly:

---
PENDING CONFIRMATION — strategy.md has NOT been modified.

Proposed (non-withdrawn): [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table
to apply custom version | WITHDRAW [#] to remove specific proposals before
confirming
---

Stop here. Write nothing further until the user replies.

---

## Step 8 — Apply

Triggered only after YES or REVISED.

Write exactly the confirmed (non-withdrawn) changes. No additional formatting
of unchanged sections.

Confirm: "strategy.md updated: [N] additions, [N] removals, [N]
reprioritizations."
```

---

## V-02: Lifecycle Emphasis — Per-step analytical purpose declarations (C-57)

**Variation axis**: Lifecycle emphasis — each step opens with an explicit
"This step exists so that: [purpose]" declaration before any instructions.
The purpose statement names the analytical function of the step, not its
procedural output, and makes explicit what downstream steps depend on this
step producing. INERTIA-GATE blocks remain as verbatim reproduction blocks
(R18 V-01 baseline) without numbered site labels.

**Hypothesis**: A step instruction tells the model what to do. A purpose
declaration tells the model why the step exists in the protocol — which
downstream step it enables and what failure mode it prevents. Without the
purpose declaration, a model that produces structurally correct output can
still satisfy the step through a path that violates the analytical contract
(e.g., producing a delta table by re-reading signal files rather than using
the closed inventory). The purpose declaration makes the intended analytical
path auditable: a reader who asks "is this step serving its declared purpose?"
can evaluate correctness independent of output structure. This tests whether
purpose declarations change execution path fidelity beyond structural
compliance alone.

```
The result of this skill may be zero changes, some changes, or a full strategy
replacement. Inertia is a co-equal option, not a fallback. The burden of proof
rests on change, not on stability.

---

You are running /topic:plan for the topic named in the user's message.

---

## COLUMN CONTRACT

Rule 1 — Enumerated column values
Valid values (select one; prose is not valid):
  Action: ADD / REMOVE / REPRIORITIZE [Rule 1]
  Challenge strength: Strong / Moderate / Weak [Rule 1]
  Reversibility: Reversible at same cost / Gets harder / Becomes impossible [Rule 1]
  Delta-candidate: Yes / No / Pending signal [Rule 1]
PASS: "Weak" — FAIL: "weak challenge, mostly"

Rule 2 — Column independence
Test: Can I fill this cell without reading the source document?
PASS: "Team assumed biweekly review cadence prevents drift accumulation"
FAIL: "Assumption A evidence" (row-key reconstruction)

Rule 3 — Null-case enforcement
All null-case declarations must carry a change-type label. Each absent change
type must have its own independently labeled declaration. A single unlabeled
"No changes proposed" covering multiple change types fails Rule 3.
At each null site: use the verbatim type-labeled null text provided.
"Do not omit this declaration" appears at each null site.
PASS: "ADDITIONS: none — inertia holds for all candidate additions."
FAIL: "No changes proposed." (unlabeled — ambiguous across change types)

Rule 4 — Delta Finding traceability
Delta Finding column mandatory in all proposal rows.
Format: "Strategy assumed [X] / Signal revealed [Y]."
Null rows: "Delta Finding: N/A."
PASS: "Strategy assumed weekly cadence / Signal revealed daily drift frequency"
FAIL: "scout-feasibility-2026-03-14.md" (single-hop, assumption not surfaced)

Rule 5 — Symmetric inertia-rejection justification
Column name: Inertia Rejected Because [REQUIRED]
Required in ALL change-type proposal tables (Step 4a and Step 4b).
Schema: identical column name, identical REQUIRED status across both tables.
FAIL: "compelling argument exists" — FAIL: "Why this beats NO CHANGE"
Do not merge the two tables. Do not rename the column in either table.

---

## INERTIA-GATE TEMPLATE

Reproduce this block verbatim at each [INERTIA-GATE] site below.
Do not abbreviate, paraphrase, or omit. Its presence at each site is required.

  ┌─────────────────────────────────────────────────────────────────────┐
  │ INERTIA-GATE                                                        │
  │ The result of this step may leave this section unchanged.           │
  │ Inertia is a co-equal option. The burden of proof rests on change.  │
  └─────────────────────────────────────────────────────────────────────┘

---

## Upfront Output Schema

Commit to this schema before reading any file.

**Assumption table** (Step 1b)
| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

**Signal inventory** (Step 3)
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**Delta findings** (Step 3b)
| Finding ID | Strategy assumed | Signal revealed | Source artifact | Delta-candidate [Rule 1] |

**Additions table** (Step 4a)
| # | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

**Removals and Reprioritizations table** (Step 4b)
| # | Action [Rule 1] | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

**Defender Challenge Table** (Step 4c)
| Defense ID | Proposal # | Strategic decision defended | Defensive argument | Defense basis | Challenge strength [Rule 1] |

**Conflict audit** (Step 5)
| Conflict ID | Signal A | Signal B | Nature of conflict | Resolution |

**Diff table** (Step 6)
| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

Pre-read commitment: columns above are fixed. No prose substitutes.
No table merges. I will not merge Step 4a and 4b.

---

## Step 1 — Read strategy.md and extract assumptions

This step exists so that: the strategy's last-modified date becomes the
temporal partition anchor — every artifact dated after this anchor is a NEW
candidate signal; every artifact dated before is an already-incorporated
PRIOR. Without this anchor, delta detection has no reference line and NEW
vs. PRIOR classification is impossible.

Read `simulations/TOPICS.md` to locate the strategy file path. Read
strategy.md (STRATEGY DATE = last-modified date).

Extract stated dimensions. Scan: scope of coverage / sequencing /
completion criteria / success thresholds.
Apply Rule 2 before populating each Implicit evidence cell.

| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

Null (Rule 3, type-labeled): "ASSUMPTIONS: none — no implicit assumptions
identified; all strategy elements are explicitly stated."
Do not omit this declaration.

---

## Step 2 — Pre-signal Defense Register

This step exists so that: the strongest keep-arguments and invalidation
conditions for each strategy element are committed to before any disconfirming
signal is read. Post-signal defenses cannot be audited as genuine
pre-commitments; pre-signal defenses can. The Defense basis column in Step 4c
draws on this register — a D-ID citation is a pre-committed defense; a
"Newly constructed" label signals post-hoc rationalization.

Complete and output before reading any NEW artifact.

| Defense ID | Strategic decision | Strongest keep-it argument | What would invalidate |

---

## Step 3 — Signal inventory

This step exists so that: the evidence base is closed before analysis begins.
A closed inventory makes the set of signals auditable as a fixed input;
re-reading files during later steps makes the effective evidence set
unverifiable and introduces recency bias toward whichever file was last read.

List every artifact in `simulations/` matching the topic slug. Classify NEW
(date > STRATEGY DATE) or PRIOR. All 9 namespaces must be explicitly
assessed: scout / draft / review / flow / trace / prove / listen / program /
topic.

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**SIGNAL READ-LOCK**: Signal files may not be re-read after this step.
All subsequent steps use the written inventory only.

Null (Rule 3, type-labeled): "SIGNAL INVENTORY: null — no artifacts found
for topic [name]. Cannot run /topic:plan."
Do not omit this declaration.

---

## Step 3b — Delta findings

This step exists so that: each substantive contradiction between what the
strategy assumed and what NEW signals revealed is named as a Finding with
its own ID, making the chain from signal to proposal traceable. A proposal
in Step 4 that cannot cite a Finding ID has no auditable analytical path
from evidence to conclusion.

For each NEW artifact, one row per substantive finding:

| Finding ID | Strategy assumed | Signal revealed | Source artifact | Delta-candidate [Rule 1] |

Null (Rule 3, type-labeled): "DELTA FINDINGS: null — no NEW artifacts exist.
Strategy is current."
Do not omit this declaration.

---

## Step 4 — Change proposals (preamble)

This step exists so that: each strategy element is evaluated against the
inertia competitor — the option of leaving the element unchanged — before any
proposal is accepted. A proposal without an explicit inertia-rejection reason
has not defeated the null competitor; it is a preference stated without
analysis.

[INERTIA-GATE] — Reproduce verbatim here before writing any proposal row.

A proposal that cannot name a concrete consequence of deferral (the "If
unchanged" column) is a preference, not a decision — structurally invalid,
not merely incomplete.

---

## Step 4a — Additions

This step exists so that: new coverage dimensions that emerged from NEW
signals but are absent from the current strategy are evaluated for explicit
addition. The "Inertia Rejected Because" column requires each addition to
defeat the argument that the existing strategy coverage is already sufficient.

"Inertia Rejected Because [REQUIRED]": one sentence per row naming the
specific evidence or logic defeating the keep-unchanged option (Rule 5).
PASS: specific signal evidence named — FAIL: "compelling reason"

| # | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

Null (Rule 3, type-labeled): "ADDITIONS: none — inertia holds."
Do not omit this declaration.

---

## Step 4b — Removals and Reprioritizations

This step exists so that: existing strategy elements are evaluated for
removal or de-prioritization when NEW signals reveal they are redundant,
superseded, or misaligned. Symmetric treatment with Step 4a ensures the
protocol applies the same inertia standard to both directions of change —
adding and removing — rather than treating removal as the default safe option.

[INERTIA-GATE] — Reproduce verbatim here before writing any row.

"Inertia Rejected Because [REQUIRED]": identical schema to Step 4a (Rule 5).
FAIL: "compelling reason" or any prose substitute.

| # | Action [Rule 1] | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

Null declarations (Rule 3, type-labeled):
  "REMOVALS: none — inertia holds. Do not omit this declaration."
  "REPRIORITIZATIONS: none — inertia holds. Do not omit this declaration."

---

## Step 4c — Defender Challenge Table

This step exists so that: each proposal faces its strongest available
counter-argument before confirmation, testing whether the proposal survives
genuine challenge rather than only defeating the null competitor. A table
where every challenge is Weak signals rubber-stamp processing, not evaluation.

Defense basis: D-ID if pre-registered; "Newly constructed" if built after
signal reading.

| Defense ID | Proposal # | Strategic decision defended | Defensive argument | Defense basis | Challenge strength [Rule 1] |

**Calibration check** (required artifact):
  - All Weak → "Calibration: rubber-stamp risk — all challenges are Weak."
  - All Strong → "Calibration: over-zealous risk — all challenges are Strong."
  - Otherwise → "Calibration: balanced — challenge strength distribution is varied."

---

## Step 5 — Conflict audit

This step exists so that: contradictions between NEW artifacts on the same
strategy dimension are surfaced before confirmation. An unresolved conflict
between two NEW signals means the proposal row citing either signal inherits
an unresolved evidentiary basis — confirming the proposal without resolving
the conflict propagates the contradiction into strategy.md.

Identify any NEW artifacts that contradict each other on the same strategy
dimension.

| Conflict ID | Signal A | Signal B | Nature of conflict | Resolution |

Null (Rule 3, type-labeled): "CONFLICT AUDIT: none — no contradictions
detected between NEW artifacts on the same strategy dimension."
Do not omit this declaration.

---

## Step 6 — Before/after diff

This step exists so that: the reviewer can evaluate the complete set of
proposed changes at once, with evidence brackets tracing each proposed After
value to its source signal and Proposal cross-references linking each diff
row to the numbered proposal that motivates it.

Include [evidence brackets] in each After cell and Proposal cross-refs
(e.g., "ADD-1") per row.

| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

---

## Step 7 — Confirmation gate

This step exists so that: strategy.md is not modified until the reviewer
has explicitly confirmed the complete diff. NO is a structurally complete
outcome — an unmodified strategy that has been deliberately reviewed is
better than an unreviewed modification.

[INERTIA-GATE] — Reproduce verbatim here before presenting any output.
NO is a complete and valid outcome.

Display: Step 3b / Step 4a / Step 4b / Step 4c (with calibration check) /
Step 6.

Individual proposals may be withdrawn before gate execution. Reply YES
applies only to non-withdrawn proposals.

Write exactly:

---
PENDING CONFIRMATION — strategy.md has NOT been modified.

Proposed (non-withdrawn): [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table
to apply custom version | WITHDRAW [#] to remove specific proposals before
confirming
---

Stop here. Write nothing further until the user replies.

---

## Step 8 — Apply

This step exists so that: exactly the confirmed (non-withdrawn) changes are
applied to strategy.md with no collateral reformatting of unchanged sections.
Applying more or fewer than the confirmed set violates the confirmation gate
contract established in Step 7.

Triggered only after YES or REVISED.

Write exactly the confirmed (non-withdrawn) changes. No additional formatting
of unchanged sections.

Confirm: "strategy.md updated: [N] additions, [N] removals, [N]
reprioritizations."
```

---

## V-03: Role Sequence — Pre-signal defense before strategy read

**Variation axis**: Role sequence — Step 2 (Pre-signal Defense Register) is
moved to the first execution position, before reading strategy.md. The model
must commit to its strongest keep-arguments and invalidation conditions for
each expected strategy element before encountering the actual content. Step 1
(Read strategy.md) follows, with the defense register in view. INERTIA-GATE
blocks remain at Steps 4, 4b, and 7 as verbatim blocks (no numbered labels).
No per-step purpose declarations.

**Hypothesis**: In the baseline sequence, the Pre-signal Defense Register is
produced after reading strategy.md. A model that has already absorbed the
strategy text will construct defenses shaped by what it read — defenses that
are epistemically post-hoc even if temporally prior to reading NEW artifacts.
Moving the defense register before strategy.md is read forces genuine
pre-commitment: the model must articulate what it believes the strategy says,
and what evidence would justify changing it, without having read the document.
This surfaces a sharper contrast: a defense constructed before reading
strategy.md tests the model's prior beliefs; a defense constructed after
represents post-hoc rationalization dressed as pre-commitment. The Defense
basis column in Step 4c can then distinguish D-IDs from before-read defenses
vs. after-read defenses, adding a temporal audit dimension.

```
The result of this skill may be zero changes, some changes, or a full strategy
replacement. Inertia is a co-equal option, not a fallback. The burden of proof
rests on change, not on stability.

---

You are running /topic:plan for the topic named in the user's message.

---

## COLUMN CONTRACT

Rule 1 — Enumerated column values
Valid values (select one; prose is not valid):
  Action: ADD / REMOVE / REPRIORITIZE [Rule 1]
  Challenge strength: Strong / Moderate / Weak [Rule 1]
  Reversibility: Reversible at same cost / Gets harder / Becomes impossible [Rule 1]
  Delta-candidate: Yes / No / Pending signal [Rule 1]
PASS: "Weak" — FAIL: "weak challenge, mostly"

Rule 2 — Column independence
Test: Can I fill this cell without reading the source document?
PASS: "Team assumed biweekly review cadence prevents drift accumulation"
FAIL: "Assumption A evidence" (row-key reconstruction)

Rule 3 — Null-case enforcement
All null-case declarations must carry a change-type label. Each absent change
type must have its own independently labeled declaration. A single unlabeled
"No changes proposed" covering multiple change types fails Rule 3.
At each null site: use the verbatim type-labeled null text provided.
"Do not omit this declaration" appears at each null site.
PASS: "ADDITIONS: none — inertia holds for all candidate additions."
FAIL: "No changes proposed." (unlabeled — ambiguous across change types)

Rule 4 — Delta Finding traceability
Delta Finding column mandatory in all proposal rows.
Format: "Strategy assumed [X] / Signal revealed [Y]."
Null rows: "Delta Finding: N/A."
PASS: "Strategy assumed weekly cadence / Signal revealed daily drift frequency"
FAIL: "scout-feasibility-2026-03-14.md" (single-hop, assumption not surfaced)

Rule 5 — Symmetric inertia-rejection justification
Column name: Inertia Rejected Because [REQUIRED]
Required in ALL change-type proposal tables (Step 4a and Step 4b).
Schema: identical column name, identical REQUIRED status across both tables.
FAIL: "compelling argument exists" — FAIL: "Why this beats NO CHANGE"
Do not merge the two tables. Do not rename the column in either table.

---

## INERTIA-GATE TEMPLATE

Reproduce this block verbatim at each [INERTIA-GATE] site below.
Do not abbreviate, paraphrase, or omit. Its presence at each site is required.

  ┌─────────────────────────────────────────────────────────────────────┐
  │ INERTIA-GATE                                                        │
  │ The result of this step may leave this section unchanged.           │
  │ Inertia is a co-equal option. The burden of proof rests on change.  │
  └─────────────────────────────────────────────────────────────────────┘

---

## Upfront Output Schema

Commit to this schema before reading any file.

**Pre-read defense register** (Step 1 — before reading strategy.md)
| Defense ID | Expected strategy element | Strongest keep-it argument | What would invalidate |

**Assumption table** (Step 2b — after reading strategy.md)
| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

**Signal inventory** (Step 3)
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**Delta findings** (Step 3b)
| Finding ID | Strategy assumed | Signal revealed | Source artifact | Delta-candidate [Rule 1] |

**Additions table** (Step 4a)
| # | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

**Removals and Reprioritizations table** (Step 4b)
| # | Action [Rule 1] | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

**Defender Challenge Table** (Step 4c)
| Defense ID | Proposal # | Strategic decision defended | Defensive argument | Defense basis | Challenge strength [Rule 1] |

**Conflict audit** (Step 5)
| Conflict ID | Signal A | Signal B | Nature of conflict | Resolution |

**Diff table** (Step 6)
| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

Pre-read commitment: columns above are fixed. No prose substitutes.
No table merges. I will not merge Step 4a and 4b.

---

## Step 1 — Pre-signal Defense Register (before reading strategy.md)

Complete before reading strategy.md or any NEW artifact. Based on the topic
name alone, commit to: which strategy elements you expect to find, the
strongest argument for keeping each, and what signal pattern would justify
changing it.

Defense basis legend:
  PRE-READ: committed before reading strategy.md (this step)
  POST-READ: constructed after reading strategy.md (Step 2)
  POST-SIGNAL: constructed after reading NEW artifacts (Step 4c)

| Defense ID | Expected strategy element | Strongest keep-it argument | What would invalidate |
| D-01 | [expected element] | [argument] | [signal pattern] |

---

## Step 2 — Read strategy.md and extract assumptions

Read `simulations/TOPICS.md` to locate the strategy file path. Read
strategy.md (STRATEGY DATE = last-modified date).

Extract stated dimensions. Scan: scope of coverage / sequencing /
completion criteria / success thresholds.
Apply Rule 2 before populating each Implicit evidence cell.

Cross-reference with Step 1: note any expected elements that do not appear
in strategy.md, and any strategy elements not anticipated in the pre-read
defense register.

| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

Null (Rule 3, type-labeled): "ASSUMPTIONS: none — no implicit assumptions
identified; all strategy elements are explicitly stated."
Do not omit this declaration.

---

## Step 3 — Signal inventory

List every artifact in `simulations/` matching the topic slug. Classify NEW
(date > STRATEGY DATE) or PRIOR. All 9 namespaces must be explicitly
assessed: scout / draft / review / flow / trace / prove / listen / program /
topic.

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**SIGNAL READ-LOCK**: Signal files may not be re-read after this step.
All subsequent steps use the written inventory only.

Null (Rule 3, type-labeled): "SIGNAL INVENTORY: null — no artifacts found
for topic [name]. Cannot run /topic:plan."
Do not omit this declaration.

---

## Step 3b — Delta findings

For each NEW artifact, one row per substantive finding:

| Finding ID | Strategy assumed | Signal revealed | Source artifact | Delta-candidate [Rule 1] |

Null (Rule 3, type-labeled): "DELTA FINDINGS: null — no NEW artifacts exist.
Strategy is current."
Do not omit this declaration.

---

## Step 4 — Change proposals (preamble)

[INERTIA-GATE] — Reproduce verbatim here before writing any proposal row.

A proposal that cannot name a concrete consequence of deferral (the "If
unchanged" column) is a preference, not a decision — structurally invalid,
not merely incomplete.

---

## Step 4a — Additions

"Inertia Rejected Because [REQUIRED]": one sentence per row naming the
specific evidence or logic defeating the keep-unchanged option (Rule 5).
PASS: specific signal evidence named — FAIL: "compelling reason"

| # | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

Null (Rule 3, type-labeled): "ADDITIONS: none — inertia holds."
Do not omit this declaration.

---

## Step 4b — Removals and Reprioritizations

[INERTIA-GATE] — Reproduce verbatim here before writing any row.

"Inertia Rejected Because [REQUIRED]": identical schema to Step 4a (Rule 5).
FAIL: "compelling reason" or any prose substitute.

| # | Action [Rule 1] | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

Null declarations (Rule 3, type-labeled):
  "REMOVALS: none — inertia holds. Do not omit this declaration."
  "REPRIORITIZATIONS: none — inertia holds. Do not omit this declaration."

---

## Step 4c — Defender Challenge Table

A table where every challenge is Weak is a structural signal of rubber-stamp
processing, not genuine evaluation.

Defense basis: cite D-ID if pre-registered (Step 1); write "Post-read
constructed" if built after reading strategy.md; write "Post-signal
constructed" if built after reading NEW artifacts.

| Defense ID | Proposal # | Strategic decision defended | Defensive argument | Defense basis | Challenge strength [Rule 1] |

**Calibration check** (required artifact):
  - All Weak → "Calibration: rubber-stamp risk — all challenges are Weak."
  - All Strong → "Calibration: over-zealous risk — all challenges are Strong."
  - Otherwise → "Calibration: balanced — challenge strength distribution is varied."

---

## Step 5 — Conflict audit

Identify any NEW artifacts that contradict each other on the same strategy
dimension.

| Conflict ID | Signal A | Signal B | Nature of conflict | Resolution |

Null (Rule 3, type-labeled): "CONFLICT AUDIT: none — no contradictions
detected between NEW artifacts on the same strategy dimension."
Do not omit this declaration.

---

## Step 6 — Before/after diff

Include [evidence brackets] in each After cell and Proposal cross-refs
(e.g., "ADD-1") per row.

| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

---

## Step 7 — Confirmation gate

[INERTIA-GATE] — Reproduce verbatim here before presenting any output.
NO is a complete and valid outcome.

Display: Step 3b / Step 4a / Step 4b / Step 4c (with calibration check) /
Step 6.

Individual proposals may be withdrawn before gate execution. Reply YES
applies only to non-withdrawn proposals.

Write exactly:

---
PENDING CONFIRMATION — strategy.md has NOT been modified.

Proposed (non-withdrawn): [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table
to apply custom version | WITHDRAW [#] to remove specific proposals before
confirming
---

Stop here. Write nothing further until the user replies.

---

## Step 8 — Apply

Triggered only after YES or REVISED.

Write exactly the confirmed (non-withdrawn) changes. No additional formatting
of unchanged sections.

Confirm: "strategy.md updated: [N] additions, [N] removals, [N]
reprioritizations."
```

---

## V-04: Combined — Site-labeled blocks + Per-step purpose (V-01 + V-02)

**Variation axis**: Combined — C-56 (numbered site-labeled INERTIA-GATE block
headers, from V-01) + C-57 (per-step analytical purpose declaration "This step
exists so that...", from V-02). Role sequence unchanged from baseline.

**Hypothesis**: C-56 and C-57 target independent failure modes at different
structural levels. C-56 targets the INERTIA-GATE recurrence sites: a block
that is present but unlabeled allows site-identity to be established only by
reading surrounding context, not by scanning block headers. C-57 targets each
step's analytical contract: a step that omits its purpose declaration can be
satisfied by structurally correct output that violates the intended execution
path. These failure modes are orthogonal — a prompt can achieve labeled gates
without purpose declarations (V-01) or purpose declarations without labeled
gates (V-02). Combining them tests whether the two innovations reinforce each
other (labeled gates make INERTIA-GATE purpose explicit by site identity;
purpose declarations make step contracts explicit) or whether one subsumes the
other. If V-04 scores higher than both V-01 and V-02, the innovations are
additive; if V-04 scores similarly to whichever single-axis variant scores
higher, one innovation dominates.

```
The result of this skill may be zero changes, some changes, or a full strategy
replacement. Inertia is a co-equal option, not a fallback. The burden of proof
rests on change, not on stability.

---

You are running /topic:plan for the topic named in the user's message.

---

## COLUMN CONTRACT

Rule 1 — Enumerated column values
Valid values (select one; prose is not valid):
  Action: ADD / REMOVE / REPRIORITIZE [Rule 1]
  Challenge strength: Strong / Moderate / Weak [Rule 1]
  Reversibility: Reversible at same cost / Gets harder / Becomes impossible [Rule 1]
  Delta-candidate: Yes / No / Pending signal [Rule 1]
PASS: "Weak" — FAIL: "weak challenge, mostly"

Rule 2 — Column independence
Test: Can I fill this cell without reading the source document?
PASS: "Team assumed biweekly review cadence prevents drift accumulation"
FAIL: "Assumption A evidence" (row-key reconstruction)

Rule 3 — Null-case enforcement
All null-case declarations must carry a change-type label. Each absent change
type must have its own independently labeled declaration. A single unlabeled
"No changes proposed" covering multiple change types fails Rule 3.
At each null site: use the verbatim type-labeled null text provided.
"Do not omit this declaration" appears at each null site.
PASS: "ADDITIONS: none — inertia holds for all candidate additions."
FAIL: "No changes proposed." (unlabeled — ambiguous across change types)

Rule 4 — Delta Finding traceability
Delta Finding column mandatory in all proposal rows.
Format: "Strategy assumed [X] / Signal revealed [Y]."
Null rows: "Delta Finding: N/A."
PASS: "Strategy assumed weekly cadence / Signal revealed daily drift frequency"
FAIL: "scout-feasibility-2026-03-14.md" (single-hop, assumption not surfaced)

Rule 5 — Symmetric inertia-rejection justification
Column name: Inertia Rejected Because [REQUIRED]
Required in ALL change-type proposal tables (Step 4a and Step 4b).
Schema: identical column name, identical REQUIRED status across both tables.
FAIL: "compelling argument exists" — FAIL: "Why this beats NO CHANGE"
Do not merge the two tables. Do not rename the column in either table.

---

## INERTIA-GATE TEMPLATE

This template must be reproduced verbatim at each of the three numbered sites
below. At each site, fill the SITE slot with the site-specific label shown in
the step instruction. Each gate carries a unique site label, making it
independently scannable by header without reading surrounding step text.

  ┌──────────────────────────────────────────────────────────────────────────┐
  │ INERTIA-GATE [SITE: _______________________________________]             │
  │ The result of this step may leave this section unchanged.               │
  │ Inertia is a co-equal option. The burden of proof rests on change.      │
  │                                                                          │
  │ Verification: three INERTIA-GATE blocks in this output, at sites:       │
  │   [SITE 1 of 3: Step 4 — Before proposals]                              │
  │   [SITE 2 of 3: Step 4b — Before removals/reprioritizations]            │
  │   [SITE 3 of 3: Step 7 — Before confirmation]                           │
  └──────────────────────────────────────────────────────────────────────────┘

---

## Upfront Output Schema

Commit to this schema before reading any file.

**Assumption table** (Step 1b)
| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

**Signal inventory** (Step 3)
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**Delta findings** (Step 3b)
| Finding ID | Strategy assumed | Signal revealed | Source artifact | Delta-candidate [Rule 1] |

**Additions table** (Step 4a)
| # | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

**Removals and Reprioritizations table** (Step 4b)
| # | Action [Rule 1] | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

**Defender Challenge Table** (Step 4c)
| Defense ID | Proposal # | Strategic decision defended | Defensive argument | Defense basis | Challenge strength [Rule 1] |

**Conflict audit** (Step 5)
| Conflict ID | Signal A | Signal B | Nature of conflict | Resolution |

**Diff table** (Step 6)
| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

Pre-read commitment: columns above are fixed. No prose substitutes.
No table merges. I will not merge Step 4a and 4b.

---

## Step 1 — Read strategy.md and extract assumptions

This step exists so that: the strategy's last-modified date becomes the
temporal partition anchor — every artifact dated after this anchor is a NEW
candidate signal; every artifact dated before is an already-incorporated
PRIOR. Without this anchor, delta detection has no reference line and NEW
vs. PRIOR classification is impossible.

Read `simulations/TOPICS.md` to locate the strategy file path. Read
strategy.md (STRATEGY DATE = last-modified date).

Extract stated dimensions. Scan: scope of coverage / sequencing /
completion criteria / success thresholds.
Apply Rule 2 before populating each Implicit evidence cell.

| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

Null (Rule 3, type-labeled): "ASSUMPTIONS: none — no implicit assumptions
identified; all strategy elements are explicitly stated."
Do not omit this declaration.

---

## Step 2 — Pre-signal Defense Register

This step exists so that: the strongest keep-arguments and invalidation
conditions for each strategy element are committed to before any disconfirming
signal is read. Post-signal defenses are not pre-commitments; they are
post-hoc rationalizations. The Defense basis column in Step 4c exposes this
distinction — a D-ID citation is a pre-committed defense; "Newly constructed"
signals post-hoc rationalization.

Complete and output before reading any NEW artifact.

| Defense ID | Strategic decision | Strongest keep-it argument | What would invalidate |

---

## Step 3 — Signal inventory

This step exists so that: the evidence base is closed before analysis begins.
A closed inventory makes the set of signals auditable as a fixed input. Re-
reading files during later steps makes the effective evidence set unverifiable
and introduces recency bias toward whichever file was last read.

List every artifact in `simulations/` matching the topic slug. Classify NEW
(date > STRATEGY DATE) or PRIOR. All 9 namespaces must be explicitly
assessed: scout / draft / review / flow / trace / prove / listen / program /
topic.

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**SIGNAL READ-LOCK**: Signal files may not be re-read after this step.
All subsequent steps use the written inventory only.

Null (Rule 3, type-labeled): "SIGNAL INVENTORY: null — no artifacts found
for topic [name]. Cannot run /topic:plan."
Do not omit this declaration.

---

## Step 3b — Delta findings

This step exists so that: each substantive contradiction between what the
strategy assumed and what NEW signals revealed is named as a Finding with
its own ID, making the chain from signal to proposal traceable. A proposal
in Step 4 that cannot cite a Finding ID has no auditable analytical path
from evidence to conclusion.

For each NEW artifact, one row per substantive finding:

| Finding ID | Strategy assumed | Signal revealed | Source artifact | Delta-candidate [Rule 1] |

Null (Rule 3, type-labeled): "DELTA FINDINGS: null — no NEW artifacts exist.
Strategy is current."
Do not omit this declaration.

---

## Step 4 — Change proposals (preamble)

This step exists so that: each strategy element is evaluated against the
inertia competitor — the option of leaving the element unchanged — before any
proposal is accepted. A proposal without an explicit inertia-rejection reason
has not defeated the null competitor; it is a preference stated without
analysis.

Reproduce the INERTIA-GATE block verbatim with SITE label:
  INERTIA-GATE [SITE 1 of 3: Step 4 — Before proposals]

A proposal that cannot name a concrete consequence of deferral (the "If
unchanged" column) is a preference, not a decision — structurally invalid,
not merely incomplete.

---

## Step 4a — Additions

This step exists so that: new coverage dimensions that emerged from NEW
signals but are absent from the current strategy are evaluated for explicit
addition. The "Inertia Rejected Because" column requires each addition to
defeat the argument that existing strategy coverage is already sufficient.

"Inertia Rejected Because [REQUIRED]": one sentence per row naming the
specific evidence or logic defeating the keep-unchanged option (Rule 5).
PASS: specific signal evidence named — FAIL: "compelling reason"

| # | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

Null (Rule 3, type-labeled): "ADDITIONS: none — inertia holds."
Do not omit this declaration.

---

## Step 4b — Removals and Reprioritizations

This step exists so that: existing strategy elements are evaluated for
removal or de-prioritization when NEW signals reveal they are redundant,
superseded, or misaligned. Symmetric treatment with Step 4a ensures inertia
is applied as equally to removing as to adding.

Reproduce the INERTIA-GATE block verbatim with SITE label:
  INERTIA-GATE [SITE 2 of 3: Step 4b — Before removals/reprioritizations]

"Inertia Rejected Because [REQUIRED]": identical schema to Step 4a (Rule 5).
FAIL: "compelling reason" or any prose substitute.

| # | Action [Rule 1] | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

Null declarations (Rule 3, type-labeled):
  "REMOVALS: none — inertia holds. Do not omit this declaration."
  "REPRIORITIZATIONS: none — inertia holds. Do not omit this declaration."

---

## Step 4c — Defender Challenge Table

This step exists so that: each proposal faces its strongest available
counter-argument before confirmation. A table where every challenge is Weak
signals rubber-stamp processing, not evaluation.

Defense basis: D-ID if pre-registered; "Newly constructed" if built after
signal reading.

| Defense ID | Proposal # | Strategic decision defended | Defensive argument | Defense basis | Challenge strength [Rule 1] |

**Calibration check** (required artifact):
  - All Weak → "Calibration: rubber-stamp risk — all challenges are Weak."
  - All Strong → "Calibration: over-zealous risk — all challenges are Strong."
  - Otherwise → "Calibration: balanced — challenge strength distribution is varied."

---

## Step 5 — Conflict audit

This step exists so that: contradictions between NEW artifacts on the same
strategy dimension are surfaced before confirmation. An unresolved conflict
means the proposal citing either signal inherits an unresolved evidentiary
basis — confirming without resolving propagates the contradiction into
strategy.md.

Identify any NEW artifacts that contradict each other on the same strategy
dimension.

| Conflict ID | Signal A | Signal B | Nature of conflict | Resolution |

Null (Rule 3, type-labeled): "CONFLICT AUDIT: none — no contradictions
detected between NEW artifacts on the same strategy dimension."
Do not omit this declaration.

---

## Step 6 — Before/after diff

This step exists so that: the reviewer can evaluate the complete proposed
change set at once, with each After value traced to its source signal via
evidence brackets and each diff row linked to its numbered proposal.

Include [evidence brackets] in each After cell and Proposal cross-refs
(e.g., "ADD-1") per row.

| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

---

## Step 7 — Confirmation gate

This step exists so that: strategy.md is not modified until the reviewer has
explicitly confirmed the complete diff. An unmodified strategy that has been
deliberately reviewed is a structurally complete outcome, not a failure.

Reproduce the INERTIA-GATE block verbatim with SITE label:
  INERTIA-GATE [SITE 3 of 3: Step 7 — Before confirmation]
NO is a complete and valid outcome.

Display: Step 3b / Step 4a / Step 4b / Step 4c (with calibration check) /
Step 6.

Individual proposals may be withdrawn before gate execution. Reply YES
applies only to non-withdrawn proposals.

Write exactly:

---
PENDING CONFIRMATION — strategy.md has NOT been modified.

Proposed (non-withdrawn): [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table
to apply custom version | WITHDRAW [#] to remove specific proposals before
confirming
---

Stop here. Write nothing further until the user replies.

---

## Step 8 — Apply

This step exists so that: exactly the confirmed (non-withdrawn) changes are
applied to strategy.md with no collateral reformatting of unchanged sections.

Triggered only after YES or REVISED.

Write exactly the confirmed (non-withdrawn) changes. No additional formatting
of unchanged sections.

Confirm: "strategy.md updated: [N] additions, [N] removals, [N]
reprioritizations."
```

---

## V-05: Combined — Site-labeled blocks + Per-step purpose + Pre-read defense first

**Variation axis**: Combined — C-56 (numbered site-labeled INERTIA-GATE block
headers, from V-01) + C-57 (per-step analytical purpose declarations, from
V-02) + role sequence innovation (pre-signal defense register moved before
reading strategy.md, from V-03).

**Hypothesis**: The three innovations operate at distinct protocol layers.
C-56 operates at the gate layer: the INERTIA-GATE recurrence sites are
independently scannable by site-label, making missing gates visible without
reading step bodies. C-57 operates at the step layer: each step declares its
analytical purpose before instructions, making execution-path violations
visible without structural output inspection. The V-03 role sequence operates
at the commitment layer: the defense register is produced before the strategy
text is read, making pre-commitment genuine rather than post-hoc. Because
these layers are independent — gate-label visibility does not require purpose
declarations, purpose declarations do not require pre-read defense, pre-read
defense does not require labeled gates — combining all three should be additive.
The key test is whether the V-03 resequencing introduces friction that
degrades compliance with C-01 (strategy read cited) or C-02 (all 9 namespaces
assessed), since those criteria depend on later steps that now follow the
pre-read defense step.

```
The result of this skill may be zero changes, some changes, or a full strategy
replacement. Inertia is a co-equal option, not a fallback. The burden of proof
rests on change, not on stability.

---

You are running /topic:plan for the topic named in the user's message.

---

## COLUMN CONTRACT

Rule 1 — Enumerated column values
Valid values (select one; prose is not valid):
  Action: ADD / REMOVE / REPRIORITIZE [Rule 1]
  Challenge strength: Strong / Moderate / Weak [Rule 1]
  Reversibility: Reversible at same cost / Gets harder / Becomes impossible [Rule 1]
  Delta-candidate: Yes / No / Pending signal [Rule 1]
PASS: "Weak" — FAIL: "weak challenge, mostly"

Rule 2 — Column independence
Test: Can I fill this cell without reading the source document?
PASS: "Team assumed biweekly review cadence prevents drift accumulation"
FAIL: "Assumption A evidence" (row-key reconstruction)

Rule 3 — Null-case enforcement
All null-case declarations must carry a change-type label. Each absent change
type must have its own independently labeled declaration. A single unlabeled
"No changes proposed" covering multiple change types fails Rule 3.
At each null site: use the verbatim type-labeled null text provided.
"Do not omit this declaration" appears at each null site.
PASS: "ADDITIONS: none — inertia holds for all candidate additions."
FAIL: "No changes proposed." (unlabeled — ambiguous across change types)

Rule 4 — Delta Finding traceability
Delta Finding column mandatory in all proposal rows.
Format: "Strategy assumed [X] / Signal revealed [Y]."
Null rows: "Delta Finding: N/A."
PASS: "Strategy assumed weekly cadence / Signal revealed daily drift frequency"
FAIL: "scout-feasibility-2026-03-14.md" (single-hop, assumption not surfaced)

Rule 5 — Symmetric inertia-rejection justification
Column name: Inertia Rejected Because [REQUIRED]
Required in ALL change-type proposal tables (Step 4a and Step 4b).
Schema: identical column name, identical REQUIRED status across both tables.
FAIL: "compelling argument exists" — FAIL: "Why this beats NO CHANGE"
The REQUIRED label is part of the enforcement contract. Do not merge the two
tables. Do not rename the column in either table.

---

## INERTIA-GATE TEMPLATE

This template must be reproduced verbatim at each of the three numbered sites
below. At each site, fill the SITE slot with the site-specific label shown in
the step instruction. Each gate carries a unique site label, making it
independently scannable by header without reading surrounding step text.

  ┌──────────────────────────────────────────────────────────────────────────┐
  │ INERTIA-GATE [SITE: _______________________________________]             │
  │ The result of this step may leave this section unchanged.               │
  │ Inertia is a co-equal option. The burden of proof rests on change.      │
  │                                                                          │
  │ Verification: three INERTIA-GATE blocks in this output, at sites:       │
  │   [SITE 1 of 3: Step 4 — Before proposals]                              │
  │   [SITE 2 of 3: Step 4b — Before removals/reprioritizations]            │
  │   [SITE 3 of 3: Step 7 — Before confirmation]                           │
  └──────────────────────────────────────────────────────────────────────────┘

---

## Upfront Output Schema

Commit to this schema before reading any file or executing any step.

**Pre-read defense register** (Step 1 — before strategy.md)
| Defense ID | Expected strategy element | Strongest keep-it argument | What would invalidate |

**Assumption table** (Step 2b — after strategy.md)
| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

**Signal inventory** (Step 3)
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**Delta findings** (Step 3b)
| Finding ID | Strategy assumed | Signal revealed | Source artifact | Delta-candidate [Rule 1] |

**Additions table** (Step 4a)
| # | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

**Removals and Reprioritizations table** (Step 4b)
| # | Action [Rule 1] | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

**Defender Challenge Table** (Step 4c)
| Defense ID | Proposal # | Strategic decision defended | Defensive argument | Defense basis | Challenge strength [Rule 1] |

**Conflict audit** (Step 5)
| Conflict ID | Signal A | Signal B | Nature of conflict | Resolution |

**Diff table** (Step 6)
| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

Pre-read commitment: columns above are fixed. No prose substitutes.
No table merges. I will not merge Step 4a and 4b.

---

## Step 1 — Pre-signal Defense Register (before reading strategy.md)

This step exists so that: the strongest keep-arguments and invalidation
conditions for each strategy element are committed to before the strategy text
is encountered. A defense constructed before reading strategy.md cannot be
shaped by its content; a defense constructed after is epistemically
post-hoc regardless of its temporal position in the protocol. The Defense
basis column in Step 4c exposes the distinction: D-IDs citing Step 1 entries
are genuine pre-commitments; "Newly constructed" labels are post-hoc.

Complete before reading strategy.md or any artifact. Based on the topic name
alone, commit to expected strategy elements, keep-arguments, and invalidation
conditions.

| Defense ID | Expected strategy element | Strongest keep-it argument | What would invalidate |
| D-01 | [expected element] | [argument] | [signal pattern] |

---

## Step 2 — Read strategy.md and extract assumptions

This step exists so that: the strategy's actual content and last-modified date
are established as the baseline for delta detection. The STRATEGY DATE
partitions all artifacts into PRIOR (already incorporated) and NEW (candidate
signals). Without this anchor, the NEW / PRIOR classification in Step 3 has
no reference line.

Read `simulations/TOPICS.md` to locate the strategy file path. Read
strategy.md (STRATEGY DATE = last-modified date).

Extract stated dimensions. Scan: scope of coverage / sequencing /
completion criteria / success thresholds.
Apply Rule 2 before populating each Implicit evidence cell.

Cross-reference with Step 1: note any expected elements absent from strategy.md
and any strategy elements not anticipated in the pre-read register.

| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

Null (Rule 3, type-labeled): "ASSUMPTIONS: none — no implicit assumptions
identified; all strategy elements are explicitly stated."
Do not omit this declaration.

---

## Step 3 — Signal inventory

This step exists so that: the evidence base is closed before analysis begins.
A closed inventory makes the full set of signals auditable as a fixed input.
Re-reading files during later steps makes the effective evidence set
unverifiable and introduces recency bias toward the most recently read file.

List every artifact in `simulations/` matching the topic slug. Classify NEW
(date > STRATEGY DATE) or PRIOR. All 9 namespaces must be explicitly
assessed: scout / draft / review / flow / trace / prove / listen / program /
topic.

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**SIGNAL READ-LOCK**: Signal files may not be re-read after this step.
All subsequent steps use the written inventory only.

Null (Rule 3, type-labeled): "SIGNAL INVENTORY: null — no artifacts found
for topic [name]. Cannot run /topic:plan."
Do not omit this declaration.

---

## Step 3b — Delta findings

This step exists so that: each substantive contradiction between what the
strategy assumed and what NEW signals revealed is named as a Finding with its
own ID. A proposal in Step 4 that cannot cite a Finding ID has no auditable
analytical path from evidence to conclusion — it is a preference, not a
signal-driven decision.

For each NEW artifact, one row per substantive finding:

| Finding ID | Strategy assumed | Signal revealed | Source artifact | Delta-candidate [Rule 1] |

Null (Rule 3, type-labeled): "DELTA FINDINGS: null — no NEW artifacts exist.
Strategy is current."
Do not omit this declaration.

---

## Step 4 — Change proposals (preamble)

This step exists so that: each strategy element faces the inertia competitor
— the option of leaving it unchanged — before any proposal is accepted. The
INERTIA-GATE at this site is the first of three recurrence points at which
the inertia standard is re-asserted, making it impossible to begin proposal
writing without affirming the burden of proof.

Reproduce the INERTIA-GATE block verbatim with SITE label:
  INERTIA-GATE [SITE 1 of 3: Step 4 — Before proposals]

A proposal that cannot name a concrete consequence of deferral (the "If
unchanged" column) is a preference, not a decision — structurally invalid,
not merely incomplete.

---

## Step 4a — Additions

This step exists so that: new coverage dimensions that emerged from NEW
signals but are absent from the current strategy are evaluated for explicit
addition. The "Inertia Rejected Because" column requires each addition to
defeat the argument that existing coverage is already sufficient — not merely
to assert that coverage would improve.

"Inertia Rejected Because [REQUIRED]": one sentence per row naming the
specific evidence or logic defeating the keep-unchanged option (Rule 5).
PASS: specific signal evidence named — FAIL: "compelling reason"

| # | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

Null (Rule 3, type-labeled): "ADDITIONS: none — inertia holds."
Do not omit this declaration.

---

## Step 4b — Removals and Reprioritizations

This step exists so that: existing strategy elements are evaluated for removal
or de-prioritization when NEW signals reveal they are redundant, superseded,
or misaligned. The INERTIA-GATE at this site is the second of three
recurrence points — symmetric application of the inertia standard to removal
prevents asymmetric bias where addition requires justification but removal
does not.

Reproduce the INERTIA-GATE block verbatim with SITE label:
  INERTIA-GATE [SITE 2 of 3: Step 4b — Before removals/reprioritizations]

"Inertia Rejected Because [REQUIRED]": identical schema to Step 4a (Rule 5).
FAIL: "compelling reason" or any prose substitute.

| # | Action [Rule 1] | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

Null declarations (Rule 3, type-labeled):
  "REMOVALS: none — inertia holds. Do not omit this declaration."
  "REPRIORITIZATIONS: none — inertia holds. Do not omit this declaration."

---

## Step 4c — Defender Challenge Table

This step exists so that: each proposal faces its strongest available counter-
argument before confirmation, testing whether the proposal survives genuine
challenge rather than only defeating the null competitor. A table where every
challenge is Weak signals rubber-stamp processing; a table where every
challenge is Strong signals over-zealous rejection bias.

Defense basis: cite D-ID if the defense was pre-registered in Step 1;
write "Post-read constructed" if built after reading strategy.md;
write "Post-signal constructed" if built after reading NEW artifacts.

| Defense ID | Proposal # | Strategic decision defended | Defensive argument | Defense basis | Challenge strength [Rule 1] |

**Calibration check** (required artifact):
  - All Weak → "Calibration: rubber-stamp risk — all challenges are Weak."
  - All Strong → "Calibration: over-zealous risk — all challenges are Strong."
  - Otherwise → "Calibration: balanced — challenge strength distribution is varied."

---

## Step 5 — Conflict audit

This step exists so that: contradictions between NEW artifacts on the same
strategy dimension are surfaced before confirmation. An unresolved conflict
between two NEW signals means any proposal citing either signal inherits an
unresolved evidentiary basis — confirming the proposal propagates the
contradiction into strategy.md without resolution.

Identify any NEW artifacts that contradict each other on the same strategy
dimension.

| Conflict ID | Signal A | Signal B | Nature of conflict | Resolution |

Null (Rule 3, type-labeled): "CONFLICT AUDIT: none — no contradictions
detected between NEW artifacts on the same strategy dimension."
Do not omit this declaration.

---

## Step 6 — Before/after diff

This step exists so that: the reviewer can evaluate the complete proposed
change set at a single glance, with each After value traced to its source
signal via evidence brackets and each diff row linked to its numbered
proposal via the cross-ref column.

Include [evidence brackets] in each After cell and Proposal cross-refs
(e.g., "ADD-1") per row.

| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

---

## Step 7 — Confirmation gate

This step exists so that: strategy.md is not modified until the reviewer
explicitly confirms the complete diff. The INERTIA-GATE at this site is the
third and final recurrence point — its presence immediately before the
confirmation prompt ensures the inertia standard is active at the decision
moment, not only at the proposal-writing stage. NO is a structurally complete
outcome.

Reproduce the INERTIA-GATE block verbatim with SITE label:
  INERTIA-GATE [SITE 3 of 3: Step 7 — Before confirmation]
NO is a complete and valid outcome.

Display: Step 3b / Step 4a / Step 4b / Step 4c (with calibration check) /
Step 6.

Individual proposals may be withdrawn before gate execution. Reply YES
applies only to non-withdrawn proposals.

Write exactly:

---
PENDING CONFIRMATION — strategy.md has NOT been modified.

Proposed (non-withdrawn): [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table
to apply custom version | WITHDRAW [#] to remove specific proposals before
confirming
---

Stop here. Write nothing further until the user replies.

---

## Step 8 — Apply

This step exists so that: exactly the confirmed (non-withdrawn) changes —
no more, no fewer — are applied to strategy.md, with no collateral
reformatting of unchanged sections. Applying more or fewer than the confirmed
set violates the confirmation gate contract from Step 7.

Triggered only after YES or REVISED.

Write exactly the confirmed (non-withdrawn) changes. No additional formatting
of unchanged sections.

Confirm: "strategy.md updated: [N] additions, [N] removals, [N]
reprioritizations."
```

---

## Variation Summary

| Variation | Axis / Axes | C-56 (Labeled blocks) | C-57 (Per-step purpose) | Role sequence |
|-----------|-------------|----------------------|------------------------|---------------|
| V-01 | Inertia framing | Numbered site labels in block header | Absent | Baseline |
| V-02 | Lifecycle emphasis | Verbatim blocks, no site labels | All steps | Baseline |
| V-03 | Role sequence | Verbatim blocks, no site labels | Absent | Defense first |
| V-04 | V-01 + V-02 | Numbered site labels | All steps | Baseline |
| V-05 | V-01 + V-02 + V-03 | Numbered site labels | All steps | Defense first |

**C-56 gradient**: V-01 / V-04 / V-05 satisfy (numbered labels); V-02 / V-03
satisfy coverage only (verbatim blocks present, unlabeled — passes recurrence
presence but not independent-scannability by label).

**C-57 gradient**: V-02 / V-04 / V-05 satisfy (all steps carry "This step
exists so that:"); V-01 / V-03 do not satisfy.

**Expected scoring order**: V-05 > V-04 > V-01 = V-02 > V-03 (if C-56 and
C-57 are additive and role-sequence reordering is neutral or slightly positive
for commitment-layer fidelity).
