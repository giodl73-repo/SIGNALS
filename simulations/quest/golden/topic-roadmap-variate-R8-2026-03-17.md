---
skill: quest-variate
skill_target: topic-plan
round: R8
date: 2026-03-17
rubric: topic-roadmap-rubric-v8-2026-03-17.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [lifecycle_emphasis, inertia_framing, bias_label_completeness]
  combined:
    V-04: lifecycle_emphasis + inertia_framing
    V-05: lifecycle_emphasis + inertia_framing + bias_label_completeness + output_format
rubric_anchor: >
  v8 adds C-19 (phase entry/exit conditions making gate sequencing verifiable)
  and C-20 (bias labels at every structural guard point — not just proposal table
  columns or phase-level annotations, but inline at EVERY named guard site).
  V-05 of R7 was the pattern that drove both criteria. R8 isolates the two axes
  (lifecycle_emphasis for C-19, bias_label_completeness for C-20) as single-axis
  variations before combining them in V-04 and V-05.
round_targets: >
  C-19 full pass requires: entry conditions that reference the preceding phase by
  number, exit conditions that confirm phase completion, and both INERTIA-GATE
  and confirmation gate carrying entry+exit pairs. The key distinguisher between
  partial and full pass is whether skipping is detectable at the boundary (entry
  condition present) vs inferred from output structure (phase ordering only).
  C-20 full pass requires: bias label inline AT the guard site for EVERY named
  structural guard — PHASE-1-READ-BARRIER, SIGNAL READ-LOCK, INERTIA-GATE,
  confirmation gate, write guard. A summary section or proposal-table column
  alone is partial pass. The label must appear at the guard itself.
---

## V-01 — Axis: Lifecycle Emphasis

**Variation axis**: Every phase carries explicit ENTRY CONDITION and EXIT CRITERION.
Phase N may not open until Phase N-1's EXIT CRITERION is met in the output.
The INERTIA-GATE and confirmation gate both carry explicit entry and exit conditions,
making gate skipping detectable at the boundary — a violation is visible before
Phase N-1's output is inspected.

**Hypothesis**: C-19 requires entry/exit conditions that reference preceding phases
by number. A prompt that bakes ENTRY CONDITION and EXIT CRITERION as labeled fields
in every phase header makes skipping structurally detectable: the absence of the
EXIT CRITERION token in Phase N-1's output is a visible gap before Phase N opens.
Phase ordering alone does not achieve this — the condition must be stated as a
named constraint, not implied by sequence.

---

```
You are running /topic:plan — signal strategy revision for a Signal topic.

INERTIA PRIOR: strategy.md unchanged is the default outcome.
Zero proposals is a valid, complete execution. The burden of proof rests on change.

---

## Phase 1 — Pre-Signal Defense Register
[Bias blocked: anchor bias]

ENTRY CONDITION: No files have been read yet.
DO NOT read strategy.md or any signal file before Phase 1 is complete.

For each active strategy dimension you are aware of from prior context, write one row:

| Defense ID | Strategy dimension | Strongest keep-it argument | What evidence would defeat this |

EXIT CRITERION: Defense register table is present in output with at least one row
per known dimension. No file has been read. Phase 2 may NOT open until this is met.

---

## Phase 2 — Signal Inventory
[Bias blocked: recency bias]

ENTRY CONDITION: Phase 1 EXIT CRITERION met (defense register present; no file read).
Do NOT begin Phase 2 until Phase 1 EXIT CRITERION is confirmed in output above.

Scan simulations/ for artifacts matching the topic slug across all 9 namespaces:
scout / draft / review / flow / trace / prove / listen / program / topic

Read TOPICS.md to locate strategy.md. Record STRATEGY DATE as a named field before
classification begins.
Date rule: NEW = artifact date > STRATEGY DATE | PRIOR = artifact date <= STRATEGY DATE

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

All 9 namespaces must appear. A namespace with zero artifacts emits an explicit null row.

---
SIGNAL READ-LOCK: Signal files may not be re-read after this inventory is written.
[Bias blocked: confirmation bias / vocabulary contamination from strategy re-read]
All subsequent phases use the written inventory only.
---

EXIT CRITERION: Inventory table present; all 9 namespaces covered (explicit null rows
for empty namespaces); SIGNAL READ-LOCK in effect. Phase 3 may NOT open until this is met.

---

## Phase 3 — Read Strategy
[Bias blocked: framing bias]

ENTRY CONDITION: Phase 2 EXIT CRITERION met.
Do NOT read strategy.md until Phase 2 EXIT CRITERION is confirmed in output above.

Read strategy.md. Record:
- STRATEGY DATE as a named field
- Goal statement (verbatim or paraphrase)
- Every planned signal entry by namespace

EXIT CRITERION: STRATEGY DATE recorded as named field; goal statement present;
planned signals enumerated by namespace. Phase 4 may NOT open until this is met.

---

## Phase 4 — Delta Analysis
[Bias blocked: confirmation bias]

ENTRY CONDITION: Phase 3 EXIT CRITERION met.
Do NOT begin delta analysis until Phase 3 EXIT CRITERION is confirmed in output above.

For each NEW artifact, classify each finding into one of four categories.
Do not merge categories. Each category has its own table.

### CONFIRMED
| Finding ID | Existing assumption | Confirmed by | Understanding changed: prior -> now |
Null: "CONFIRMED: none — no NEW artifacts confirm existing assumptions."

### EXPANDED
| Finding ID | Existing assumption | Expanded to | Understanding changed: prior -> now |
Null: "EXPANDED: none — no NEW artifacts expand existing assumptions."

### UNEXPECTED
| Finding ID | Gap (what was missing) | Signal revealed | Understanding changed: prior -> now |
Null: "UNEXPECTED: none — no NEW artifacts reveal uncovered dimensions."

### CHALLENGED
| Finding ID | Strategy assumed | Signal challenges | Understanding changed: prior -> now |
Null: "CHALLENGED: none — no NEW artifacts challenge existing strategy."

EXIT CRITERION: All four delta category tables present (with labeled nulls where
empty); each NEW artifact appears in at least one category. Phase 5 may NOT open
until this is met.

---

## Phase 5 — Defeat Assessment
[INERTIA-GATE: This phase runs only for adjudicated dimensions]

ENTRY CONDITION: Phase 4 EXIT CRITERION met (all four delta categories present
with labeled nulls). Do NOT open Phase 5 until Phase 4 EXIT CRITERION is confirmed.

Verdict semantics:
- DEFEATED: Signal overcomes the Phase 1 defense. Dimension advances to Phase 6.
- HOLDS: Defense survives. Dimension receives NO CHANGE. Dimension has no path to Phase 6.

| Defense ID | Dimension | Phase 1 defense | Defeating evidence | Verdict (DEFEATED / HOLDS) | Consequence if HOLDS |

Confidence tiers (for DEFEATED rows only):
- HIGH: two or more independent NEW artifacts
- MEDIUM: one NEW artifact
- LOW: inference only

If all verdicts are HOLDS: emit "NULL_DELTA: all defenses hold." Stop.
Do NOT open Phase 6.

EXIT CRITERION: Verdict table complete; all dimensions adjudicated; NULL_DELTA
emitted if all HOLDS; at least one DEFEATED verdict to proceed to Phase 6.

---

## Phase 6 — Change Proposals (DEFEATED dimensions only)
[INERTIA-GATE: Only DEFEATED dimensions from Phase 5 appear here]

ENTRY CONDITION: Phase 5 EXIT CRITERION met; at least one DEFEATED verdict present;
NULL_DELTA not emitted. Do NOT open Phase 6 if NULL_DELTA was emitted in Phase 5.

### Additions
| # | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because |
Null: "ADDITIONS: none — inertia holds for all addition candidates."

### Removals and Reprioritizations
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because |
Null-REMOVALS: "REMOVALS: none — inertia holds."
Null-REPRIORITIZATIONS: "REPRIORITIZATIONS: none — inertia holds."

All 9 namespaces must have a row. Silence is not a null declaration.

EXIT CRITERION: All three change-type tables present (with labeled nulls); all 9
namespaces covered; each DEFEATED dimension has a corresponding row. Phase 7 may
NOT open until this is met.

---

## Phase 7 — Confirmation Gate
[Bias blocked: recency bias / premature closure bias]

ENTRY CONDITION: Phase 6 EXIT CRITERION met.
Do NOT modify strategy.md before Phase 7 confirmation is received.

Present: Phase 4 delta findings (all four categories), Phase 6 proposals (all
three tables).

---
PENDING CONFIRMATION — strategy.md has NOT been modified.
Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table
to apply custom version | WITHDRAW [#] to remove specific proposals before confirming
  WITHDRAW syntax: WITHDRAW [2] or WITHDRAW [1, 3]. Removes named proposals only;
  remainder is applied on YES.
  WITHDRAW is not NO (rejects all) and not REVISED (requires resubmitted table).
---
STOP HERE. Write nothing further until the user replies.

EXIT CRITERION: User has replied YES, NO, REVISED, or WITHDRAW.

---

## Phase 8 — Apply (after YES or REVISED only)

ENTRY CONDITION: Phase 7 EXIT CRITERION met (explicit YES or REVISED received).
Do NOT write to strategy.md before this ENTRY CONDITION is satisfied.

Write confirmed (non-withdrawn) changes to strategy.md.
No reformatting of unchanged sections.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-02 — Axis: Inertia Framing

**Variation axis**: INERTIA is named as the primary competitor that wins by default.
Strategy.md's current state is the incumbent position. Every proposal is a
"defeat verdict" against a named opponent. The confirmation gate frames the
decision as: does the user authorize displacing INERTIA on the listed dimensions?

**Hypothesis**: Framing inertia as a named competitor rather than a process rule
converts every decision cell from "should I propose this change?" (action-default
bias) to "does this evidence defeat INERTIA?" (challenge burden). This framing
eliminates action-default bias at the cognitive level — not just the structural
level. C-01 pass becomes natural rather than enforced. C-11 (INERTIA-GATE) and
C-13 (DEFEATED/HOLDS semantics) are strengthened because the vocabulary
(INERTIA wins / INERTIA is defeated) is built into the prompt's worldview.

---

```
You are running /topic:plan — signal strategy revision for a Signal topic.

---

## INERTIA COMPETITOR DECLARATION

INERTIA is the named competitor. INERTIA wins by default.
Strategy.md in its current state is the incumbent position held by INERTIA.

To displace INERTIA on a strategy dimension, specific NEW signal evidence must
overcome the pre-registered defense for that dimension. The skill does not
produce changes — it produces defeat verdicts. A run with zero defeats is a
complete, valid, excellent outcome: INERTIA RETAINED ACROSS ALL DIMENSIONS.

The burden of proof rests entirely on the challenger (new signal evidence).
Volume of signals does not transfer burden. Each defeat requires its own evidence.

---

## Phase 1 — Pre-Signal Defense Register
[Bias blocked: anchor bias]

DO NOT READ ANY FILES YET.

For each active strategy dimension, write INERTIA's strongest defense:

| Defense ID | Strategy dimension | INERTIA's best defense | What evidence would defeat INERTIA here |

---

## Phase 2 — Signal Inventory

Scan simulations/ for artifacts matching the topic slug across all 9 namespaces:
scout / draft / review / flow / trace / prove / listen / program / topic

Read TOPICS.md to locate strategy.md. Record STRATEGY DATE as a named field
before classification begins.
Date rule: NEW = artifact date > STRATEGY DATE | PRIOR = artifact date <= STRATEGY DATE

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

All 9 namespaces must appear. Zero-artifact namespaces emit an explicit null row.

---
SIGNAL READ-LOCK: Signal files may not be re-read after this inventory closes.
[Bias blocked: confirmation bias — vocabulary contamination from strategy re-read
is structurally blocked after this point]
---

## Phase 3 — Read Strategy

Read strategy.md. Record STRATEGY DATE as a named field. Record every planned
signal entry by namespace. Do not reclassify inventory artifacts against strategy
until Phase 4.

---

## Phase 4 — Delta Analysis (INERTIA's intelligence report)

For each NEW artifact, classify findings into four categories.
Do not merge categories.

### CONFIRMED — INERTIA's assumptions validated by new signals
| Finding ID | Existing assumption | Confirmed by | Understanding changed: prior -> now |
Null: "CONFIRMED: none — no NEW artifacts validate INERTIA's assumptions."

### EXPANDED — INERTIA's assumptions broadened by new signals
| Finding ID | Existing assumption | Expanded to | Understanding changed: prior -> now |
Null: "EXPANDED: none."

### UNEXPECTED — dimensions INERTIA's strategy did not cover
| Finding ID | Gap (INERTIA missed this) | Signal revealed | Understanding changed |
Null: "UNEXPECTED: none."

### CHALLENGED — INERTIA's assumptions directly questioned
| Finding ID | INERTIA assumed | Signal challenges | Understanding changed |
Null: "CHALLENGED: none."

---

## Phase 5 — INERTIA DEFEAT ASSESSMENT
[INERTIA-GATE: INERTIA wins every dimension by default. Only DEFEATED verdicts advance.]

Adjudicate the competition for each strategy dimension:
- DEFEATED: challenger evidence overcomes INERTIA's Phase 1 defense.
  This dimension advances to the Challenge Phase.
- HOLDS: INERTIA's defense survives. This dimension receives NO CHANGE.
  It does not enter the Challenge Phase.

| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict | Consequence if INERTIA wins |

Confidence tiers (INERTIA defeated by strength of):
- HIGH: two or more independent NEW artifacts on the same dimension
- MEDIUM: one NEW artifact
- LOW: inference only

If all verdicts are HOLDS: emit "INERTIA RETAINED ACROSS ALL DIMENSIONS."
Stop. The Challenge Phase does not open.

---

## Phase 6 — Challenge Table (DEFEATED dimensions only)
[INERTIA-GATE: Only DEFEATED dimensions appear here. HOLDS have no row and no path.]

### Additions (dimensions INERTIA did not cover)
| # | Dimension | Defeating evidence | Before (INERTIA: none) | After (proposed) | Confidence | Consequence if INERTIA wins | INERTIA defeated because |
Null: "ADDITIONS: none — INERTIA holds on all addition candidates."

### Removals and Reprioritizations
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Defeating evidence | Before (INERTIA) | After (proposed) | Confidence | Consequence if INERTIA wins | INERTIA defeated because |
Null-REMOVALS: "REMOVALS: none — INERTIA holds."
Null-REPRIORITIZATIONS: "REPRIORITIZATIONS: none — INERTIA holds."

All 9 namespaces must have a row. Silence is not a null declaration.

---

## Phase 7 — Confirmation Gate
[Bias blocked: recency bias — INERTIA's position is preserved until user confirms]

WRITE GUARD: strategy.md is not modified until the user's explicit reply.
[Bias blocked: premature closure bias]
Present: Phase 4 delta findings, Phase 6 challenge table.

---
PENDING CONFIRMATION — strategy.md has NOT been modified. INERTIA currently holds.

Proposed challenges to INERTIA: [N] additions / [N] removals / [N] reprioritizations

Reply YES to displace INERTIA on all listed dimensions
Reply NO to retain INERTIA (all dimensions unchanged)
Reply REVISED + edited table to displace INERTIA on custom dimensions
Reply WITHDRAW [#] to remove specific challenges before confirming
  WITHDRAW [2] removes only challenge #2; remaining challenges are applied.
  WITHDRAW is not NO (rejects all) and not REVISED (requires resubmitted table).
---
Stop here. Write nothing further until the user replies.

---

## Phase 8 — Apply (after YES or REVISED only)

Write confirmed (non-withdrawn) changes to strategy.md.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations.
INERTIA displaced on: [dimension list]."
```

---

## V-03 — Axis: Bias Label Completeness

**Variation axis**: Every named structural guard in the skill carries an inline bias
label at the guard site itself — not in a summary section, not only in proposal
table columns, but inline at the guard using a consistent >>> GUARD / >>> Bias
blocked / >>> Mechanism format. Guards labeled: PHASE-1-READ-BARRIER, SIGNAL
READ-LOCK, INERTIA-GATE (twice), CONFIRMATION GATE, WRITE GUARD.

**Hypothesis**: C-20 distinguishes between bias labels in proposal tables and phase
headings (C-17) vs bias labels at every named guard site (C-20). A prompt that
places the bias label inline at the guard itself — with explicit >>> GUARD name,
>>> Bias blocked: [name], >>> Mechanism: [description] — passes C-20 because the
label is auditable at the guard site without consulting any other section. A
scoring agent looking for the label at the SIGNAL READ-LOCK can find it directly
at the lock, not inferred from a proposal table column or preamble annotation.

---

```
You are running /topic:plan — signal strategy revision for a Signal topic.

INERTIA PRIOR: strategy.md unchanged is the default outcome.
Zero proposals is a valid, complete execution. The burden of proof rests on change.

---

## Phase 1 — Pre-Signal Defense Register

>>> GUARD: PHASE-1-READ-BARRIER
>>> Bias blocked: anchor bias
>>> Mechanism: Defenses written before any file is read declare prior belief.
>>>   Defenses written after reading rationalize evidence — not a valid anchor-
>>>   bias block. This is the only structural position where genuine prior belief
>>>   can be captured.
>>> DO NOT read strategy.md or any signal artifact before this phase is complete.

For each active strategy dimension you are aware of from prior context, write one row:

| Defense ID | Strategy dimension | Strongest keep-it argument | What evidence would defeat this |

---

## Phase 2 — Signal Inventory

Scan simulations/ for artifacts matching the topic slug across all 9 namespaces:
scout / draft / review / flow / trace / prove / listen / program / topic

Read TOPICS.md to locate strategy.md. Record STRATEGY DATE as a named field
before classification begins.
Date rule: NEW = artifact date > STRATEGY DATE | PRIOR = artifact date <= STRATEGY DATE

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

All 9 namespaces must appear. Zero-artifact namespaces emit an explicit null row.

>>> GUARD: SIGNAL READ-LOCK
>>> Bias blocked: confirmation bias; vocabulary contamination
>>> Mechanism: Signal files are fixed as of this inventory. Re-reading a signal
>>>   file after this point introduces post-hoc vocabulary alignment with the
>>>   strategy frame — the reader unconsciously matches artifact language to
>>>   strategy categories they have already read. This lock prevents that.
>>>   Signal files may NOT be re-read after this inventory is written.
>>>   All subsequent phases use the written inventory only.

---

## Phase 3 — Read Strategy

Read strategy.md. Record STRATEGY DATE as a named field. Record every planned
signal entry by namespace.

---

## Phase 4 — Delta Analysis
[Bias blocked: confirmation bias — four-category forcing function prevents selective classification]

For each NEW artifact, classify findings into four categories.
Do not merge categories. Each category has its own table.

### CONFIRMED
| Finding ID | Existing assumption | Confirmed by | Understanding changed: prior -> now |
Null: "CONFIRMED: none — no NEW artifacts confirm existing assumptions."

### EXPANDED
| Finding ID | Existing assumption | Expanded to | Understanding changed: prior -> now |
Null: "EXPANDED: none — no NEW artifacts expand existing assumptions."

### UNEXPECTED
| Finding ID | Gap (what was missing) | Signal revealed | Understanding changed: prior -> now |
Null: "UNEXPECTED: none — no NEW artifacts reveal uncovered dimensions."

### CHALLENGED
| Finding ID | Strategy assumed | Signal challenges | Understanding changed: prior -> now |
Null: "CHALLENGED: none — no NEW artifacts challenge existing strategy."

---

## Phase 5 — Defeat Assessment

>>> GUARD: INERTIA-GATE (Phase 5)
>>> Bias blocked: action-default bias; status-quo neglect
>>> Mechanism: HOLDS is the default verdict — it does not require evidence, the
>>>   same way inertia does not require justification. DEFEATED requires specific
>>>   named signal evidence. Both verdicts are structurally equal outputs: a
>>>   dimension without an explicit verdict is a structural gap, not a null.
>>>   Only DEFEATED dimensions advance to Phase 6.

Verdict semantics:
- DEFEATED: Signal overcomes the Phase 1 defense. Dimension advances to Phase 6.
- HOLDS: Defense survives. Dimension receives NO CHANGE. Has no path to Phase 6.

| Defense ID | Dimension | Phase 1 defense | Defeating evidence | Verdict (DEFEATED / HOLDS) | Consequence if HOLDS |

Confidence tiers (DEFEATED rows only):
- HIGH: two or more independent NEW artifacts
- MEDIUM: one NEW artifact
- LOW: inference only

If all verdicts are HOLDS: emit "NULL_DELTA: all defenses hold." Stop.
Do NOT open Phase 6.

---

## Phase 6 — Change Proposals (DEFEATED dimensions only)

>>> GUARD: INERTIA-GATE (Phase 6)
>>> Bias blocked: action-default bias
>>> Mechanism: HOLDS dimensions have no row and no path to this phase.
>>>   The gate fires before the first row is written. A HOLDS dimension
>>>   appearing in the proposal table is a structural violation detectable
>>>   against the Phase 5 verdict table.

Confidence tiers (defined above in Phase 5).

### Additions
| # | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Bias blocked: action-default | Inertia defeated because |
Null: "ADDITIONS: none — inertia holds for all addition candidates."

### Removals and Reprioritizations
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Bias blocked: action-default | Inertia defeated because |
Null-REMOVALS: "REMOVALS: none — inertia holds."
Null-REPRIORITIZATIONS: "REPRIORITIZATIONS: none — inertia holds."

All 9 namespaces must have a row. Silence is not a null declaration.

---

## Phase 7 — Confirmation Gate

>>> GUARD: CONFIRMATION GATE
>>> Bias blocked: recency bias; sunk-cost bias
>>> Mechanism: Proposals are presented for explicit user confirmation before
>>>   any write occurs. The most-recently-read signals are disproportionately
>>>   salient; this gate ensures the full proposal set is reviewed before the
>>>   user authorizes displacement. The absence of a NO reply is not an
>>>   implicit YES.

>>> GUARD: WRITE GUARD
>>> Bias blocked: premature closure bias
>>> Mechanism: strategy.md is not modified until explicit YES or REVISED is
>>>   received at this gate. The write step does not execute based on the
>>>   agent's confidence in the proposals — only on explicit user authorization.
>>>   strategy.md has NOT been modified at this point.

Present: Phase 4 delta findings (all four categories), Phase 6 proposals (all
three tables).

---
PENDING CONFIRMATION — strategy.md has NOT been modified.
Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table
to apply custom version | WITHDRAW [#] to remove specific proposals before confirming
  WITHDRAW syntax: WITHDRAW [2] or WITHDRAW [1, 3]. Removes named proposals only;
  remainder is applied.
  WITHDRAW is not NO (rejects all) and not REVISED (requires a resubmitted table).
---
STOP HERE. Write nothing further until the user replies.

---

## Phase 8 — Apply (after YES or REVISED only)

Triggered only after explicit YES or REVISED from the user.
Write confirmed (non-withdrawn) changes to strategy.md. No reformatting of
unchanged sections.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-04 — Combined: Lifecycle Emphasis + Inertia Framing

**Variation axes**: V-01 (entry/exit conditions per phase) + V-02 (INERTIA as named
competitor). The two axes are synergistic: explicit ENTRY CONDITIONs that reference
Phase N-1 by number make the INERTIA COMPETITOR DECLARATION's gate structure
verifiable at the phase boundary, not just by reading the output. V-02's defeat
vocabulary (INERTIA RETAINED / INERTIA DEFEATED) maps naturally to the ENTRY
CONDITION blocks: "Phase 6 may not open unless Phase 5 produced at least one
DEFEATED verdict" is a consequence of the inertia framing — INERTIA having won
all verdicts is an explicit, named outcome.

**Hypothesis**: Entry/exit conditions (C-19) are easiest to read when they flow
from the inertia framing (C-01, C-11). When the prompt declares "INERTIA wins
by default," the entry conditions for Phase 6 become: "INERTIA was defeated on
at least one dimension." This is a tighter boundary condition than "Phase 5 is
complete" because it names the relevant output token (DEFEATED verdict) rather
than relying on general completion.

---

```
You are running /topic:plan — signal strategy revision for a Signal topic.

---

## INERTIA COMPETITOR DECLARATION

INERTIA is the named competitor. INERTIA wins by default.
Strategy.md in its current state is the incumbent position.

To displace INERTIA on any dimension, specific NEW signal evidence must overcome
the pre-registered defense for that dimension. Zero defeats is a complete, valid,
excellent outcome: INERTIA RETAINED ACROSS ALL DIMENSIONS.

The burden of proof rests entirely on the challenger (new signal evidence).

---

## Phase 1 — Pre-Signal Defense Register
[Bias blocked: anchor bias — pre-read defenses declare prior belief]

ENTRY CONDITION: No files have been read yet.
DO NOT read strategy.md or any signal file before Phase 1 is complete.

For each strategy dimension, write INERTIA's strongest defense:

| Defense ID | Dimension | INERTIA's best defense | Defeating evidence requirement |

EXIT CRITERION: Defense register table present with at least one row per known
dimension. No file has been read. Phase 2 may NOT open until this is met.

---

## Phase 2 — Signal Inventory
[Bias blocked: recency bias]

ENTRY CONDITION: Phase 1 EXIT CRITERION met.
Do NOT begin Phase 2 until the Phase 1 defense register is confirmed in output.

Scan simulations/ for artifacts matching the topic slug across all 9 namespaces:
scout / draft / review / flow / trace / prove / listen / program / topic

Read TOPICS.md. Record STRATEGY DATE as a named field before classification begins.
Date rule: NEW = artifact date > STRATEGY DATE | PRIOR = artifact date <= STRATEGY DATE

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

All 9 namespaces must appear. Zero-artifact namespaces emit an explicit null row.

---
SIGNAL READ-LOCK: Signal files may not be re-read after this inventory closes.
[Bias blocked: confirmation bias / vocabulary contamination from strategy re-read]
All subsequent phases use the written inventory only.
---

EXIT CRITERION: Inventory table present; all 9 namespaces covered; SIGNAL READ-LOCK
in effect. Phase 3 may NOT open until this is met.

---

## Phase 3 — Read Strategy
[Bias blocked: framing bias — signals classified before strategy vocabulary opens]

ENTRY CONDITION: Phase 2 EXIT CRITERION met (inventory written; lock in effect).
Do NOT read strategy.md until Phase 2 EXIT CRITERION is confirmed in output.

Read strategy.md. Record STRATEGY DATE as a named field. Record goal statement
and every planned signal entry by namespace.

EXIT CRITERION: STRATEGY DATE recorded; goal statement present; planned signals
enumerated. Phase 4 may NOT open until this is met.

---

## Phase 4 — Delta Analysis (INERTIA's intelligence report)
[Bias blocked: confirmation bias]

ENTRY CONDITION: Phase 3 EXIT CRITERION met.
Do NOT begin delta analysis until Phase 3 EXIT CRITERION is confirmed in output.

Classify findings for each NEW artifact. Do not merge categories.

### CONFIRMED
| Finding ID | Existing assumption | Confirmed by | Understanding changed: prior -> now |
Null: "CONFIRMED: none — no NEW artifacts validate INERTIA's assumptions."

### EXPANDED
| Finding ID | Existing assumption | Expanded to | Understanding changed: prior -> now |
Null: "EXPANDED: none."

### UNEXPECTED
| Finding ID | Gap (INERTIA missed this) | Signal revealed | Understanding changed |
Null: "UNEXPECTED: none."

### CHALLENGED
| Finding ID | INERTIA assumed | Signal challenges | Understanding changed |
Null: "CHALLENGED: none."

EXIT CRITERION: All four category tables present with labeled nulls where empty.
Phase 5 may NOT open until this is met.

---

## Phase 5 — INERTIA DEFEAT ASSESSMENT
[INERTIA-GATE: INERTIA wins every dimension by default. Only DEFEATED verdicts advance.]

ENTRY CONDITION: Phase 4 EXIT CRITERION met (all four delta categories present).
Do NOT open Phase 5 until Phase 4 EXIT CRITERION is confirmed in output.

Verdict semantics:
- DEFEATED: challenger evidence overcomes INERTIA's Phase 1 defense.
  Dimension advances to Phase 6.
- HOLDS: INERTIA's defense survives. Dimension receives NO CHANGE.
  Dimension does NOT enter Phase 6.

| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if INERTIA wins |

Confidence tiers (DEFEATED rows):
- HIGH: two or more independent NEW artifacts
- MEDIUM: one NEW artifact
- LOW: inference only

If all verdicts are HOLDS: emit "INERTIA RETAINED ACROSS ALL DIMENSIONS." Stop.
Phase 6 does NOT open.

EXIT CRITERION: Verdict table complete; all dimensions adjudicated. If any DEFEATED
verdict exists, Phase 6 may open. If INERTIA RETAINED emitted, execution ends here.

---

## Phase 6 — Challenge Table (DEFEATED dimensions only)
[INERTIA-GATE: Only DEFEATED dimensions from Phase 5 appear here]

ENTRY CONDITION: Phase 5 EXIT CRITERION met; at least one DEFEATED verdict present;
INERTIA RETAINED not emitted. Do NOT open Phase 6 if Phase 5 ended with
INERTIA RETAINED ACROSS ALL DIMENSIONS.

### Additions
| # | Dimension | Defeating evidence | Before (INERTIA: none) | After (proposed) | Confidence | Consequence if INERTIA wins | INERTIA defeated because |
Null: "ADDITIONS: none — INERTIA holds on all addition candidates."

### Removals and Reprioritizations
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Defeating evidence | Before (INERTIA) | After (proposed) | Confidence | Consequence if INERTIA wins | INERTIA defeated because |
Null-REMOVALS: "REMOVALS: none — INERTIA holds."
Null-REPRIORITIZATIONS: "REPRIORITIZATIONS: none — INERTIA holds."

All 9 namespaces must have a row. Silence is not a null declaration.

EXIT CRITERION: All three change-type tables present; all 9 namespaces covered.
Phase 7 may NOT open until this is met.

---

## Phase 7 — Confirmation Gate
[Bias blocked: recency bias — INERTIA's position preserved until user confirms]

ENTRY CONDITION: Phase 6 EXIT CRITERION met.
WRITE GUARD: strategy.md is not modified until the user's explicit reply.
[Bias blocked: premature closure bias]
Do NOT modify strategy.md before Phase 7 confirmation is received.

Present: Phase 4 delta findings (all four categories), Phase 6 challenge table
(all three tables).

---
PENDING CONFIRMATION — strategy.md has NOT been modified. INERTIA currently holds.

Proposed challenges: [N] additions / [N] removals / [N] reprioritizations

Reply YES to displace INERTIA on all listed dimensions
Reply NO to retain INERTIA (all dimensions unchanged)
Reply REVISED + edited table to displace INERTIA on custom dimensions
Reply WITHDRAW [#] to remove specific challenges before confirming
  WITHDRAW [2] removes only challenge #2; remaining challenges are applied.
  WITHDRAW is not NO (rejects all) and not REVISED (requires resubmitted table).
---
STOP HERE. Write nothing further until the user replies.

EXIT CRITERION: User has replied YES, NO, REVISED, or WITHDRAW.

---

## Phase 8 — Apply (after YES or REVISED only)

ENTRY CONDITION: Phase 7 EXIT CRITERION met (explicit YES or REVISED received).
Do NOT write to strategy.md before this ENTRY CONDITION is confirmed.

Write confirmed (non-withdrawn) changes to strategy.md.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations.
INERTIA displaced on: [dimension list]."
```

---

## V-05 — Full Integration: Lifecycle Emphasis + Inertia Framing + Bias Label Completeness + Output Schema

**Variation axes**: V-01 (entry/exit conditions per phase, C-19) + V-02 (INERTIA
as named competitor, C-01/C-11/C-13) + V-03 (bias labels inline at every structural
guard site, C-20) + table-first output schema committed before any file is read
(C-03/C-05 hardening).

**Hypothesis**: C-19 and C-20 are orthogonal and require independent structural
mechanisms. A skill can have per-gate entry/exit conditions (C-19) while leaving
the WRITE GUARD or SIGNAL READ-LOCK unlabeled (C-20 fail). A skill can label every
guard inline (C-20) while using soft narrative phrasing that describes phases without
explicit entry/exit conditions (C-19 fail). V-05 achieves both simultaneously by
combining the entry/exit lifecycle structure (V-01) with inline guard labels at
every named guard site (V-03) and the inertia-competitor framing that makes the
INERTIA-GATE conditions semantically crisp (V-02). The upfront schema commitment
(table-first) converts column completeness from a soft requirement into a format
violation — adding hardening for C-03 and C-05 that complements the gate structure.

---

```
You are running /topic:plan — signal strategy revision for a Signal topic.

---

## INERTIA COMPETITOR DECLARATION

[>> GUARD: INERTIA PRIOR <<]
[>> Bias blocked: action-default bias — change is not the default; INERTIA is <<]
[>> Mechanism: Every phase is a test of whether challenger evidence defeats the
     incumbent position. INERTIA wins without evidence. Change requires a verdict. <<]

INERTIA is the named competitor. INERTIA wins by default.
Zero proposals is a valid, complete, excellent execution.
The burden of proof rests entirely on the challenger (new signal evidence).

---

## Output Schema — Committed Before Any File Is Read

[>> GUARD: SCHEMA COMMITMENT <<]
[>> Bias blocked: post-hoc rationalization — table columns fixed before evidence is seen <<]
[>> Mechanism: A schema committed before reading cannot be retrospectively adjusted
     to fit the evidence shape. Column violations are detectable against this block. <<]

The following schemas are fixed. No column may be added, removed, or renamed.

Phase 1 — Defense register:
| Defense ID | Dimension | INERTIA's best defense | Defeating evidence requirement |

Phase 2 — Signal inventory:
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

Phase 4 — Delta findings (per category):
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |

Phase 5 — Defeat assessment:
| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if HOLDS |

Phase 6a — Additions:
| # | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because |

Phase 6b — Removals and Reprioritizations:
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because |

---

## Phase 1 — Pre-Signal Defense Register

[>> GUARD: PHASE-1-READ-BARRIER <<]
[>> Bias blocked: anchor bias <<]
[>> Mechanism: Defenses written before any file is read declare prior belief.
     Defenses written after reading rationalize evidence — that is not a valid
     anchor-bias block. This is the only structural position where genuine prior
     belief can be captured. <<]

ENTRY CONDITION: No files have been read yet.
DO NOT read strategy.md or any signal file before Phase 1 is complete.
If any file has been read, restart Phase 1 without it in context.

| Defense ID | Dimension | INERTIA's best defense | Defeating evidence requirement |

EXIT CRITERION: Defense register table present; each known dimension has a row;
no file has been read. Phase 2 may NOT open until this is met.

---

## Phase 2 — Signal Inventory
[Bias blocked: recency bias — full namespace scan before strategy frame opens]

ENTRY CONDITION: Phase 1 EXIT CRITERION met (defense register present; no file read).
Do NOT begin Phase 2 until Phase 1 EXIT CRITERION is confirmed in output above.

Scan simulations/ for artifacts matching the topic slug across all 9 namespaces:
scout / draft / review / flow / trace / prove / listen / program / topic

Read TOPICS.md to locate strategy.md. Record STRATEGY DATE as a named field
before classification begins.
Date rule: NEW = artifact date > STRATEGY DATE | PRIOR = artifact date <= STRATEGY DATE

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

All 9 namespaces must appear. Zero-artifact namespaces emit an explicit null row.

[>> GUARD: SIGNAL READ-LOCK <<]
[>> Bias blocked: confirmation bias; vocabulary contamination <<]
[>> Mechanism: Signal files are fixed as of this inventory. Re-reading a signal
     file after this point introduces post-hoc vocabulary alignment with the
     strategy frame — the reader unconsciously matches artifact language to
     strategy categories already read. This lock closes that path. <<]
Signal files may NOT be re-read after this inventory is written.
All subsequent phases use the written inventory only.

EXIT CRITERION: Inventory table present; all 9 namespaces covered (explicit null
rows for empty namespaces); SIGNAL READ-LOCK in effect.
Phase 3 may NOT open until this is met.

---

## Phase 3 — Read Strategy
[Bias blocked: framing bias — signals already classified; strategy vocabulary cannot anchor retroactively]

ENTRY CONDITION: Phase 2 EXIT CRITERION met.
Do NOT read strategy.md until Phase 2 EXIT CRITERION is confirmed in output above.

Read strategy.md. Record:
- STRATEGY DATE as a named field
- Goal statement (verbatim or paraphrase)
- Every planned signal entry by namespace

EXIT CRITERION: STRATEGY DATE recorded as named field; goal statement present;
planned signals enumerated by namespace. Phase 4 may NOT open until this is met.

---

## Phase 4 — Delta Analysis
[Bias blocked: confirmation bias — four-category forcing function prevents selective classification]

ENTRY CONDITION: Phase 3 EXIT CRITERION met.
Do NOT begin delta analysis until Phase 3 EXIT CRITERION is confirmed in output above.

For each NEW artifact, classify each finding. Do not merge categories.

### CONFIRMED — INERTIA's assumptions validated by NEW signals
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "CONFIRMED: none — no NEW artifacts validate INERTIA's assumptions."

### EXPANDED — INERTIA's assumptions broadened by NEW signals
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "EXPANDED: none — no NEW artifacts expand INERTIA's assumptions."

### UNEXPECTED — dimensions INERTIA's strategy did not cover
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "UNEXPECTED: none — no NEW artifacts reveal uncovered dimensions."

### CHALLENGED — INERTIA's assumptions directly questioned
| Finding ID | Category | Dimension | Understanding changed: prior -> now | Source artifact |
Null: "CHALLENGED: none — no NEW artifacts challenge INERTIA's assumptions."

EXIT CRITERION: All four category tables present with labeled nulls; each NEW
artifact appears in at least one category. Phase 5 may NOT open until this is met.

---

## Phase 5 — INERTIA DEFEAT ASSESSMENT

[>> GUARD: INERTIA-GATE <<]
[>> Bias blocked: action-default bias; status-quo neglect <<]
[>> Mechanism: HOLDS is the default verdict and does not require evidence; DEFEATED
     requires specific named signal evidence. Both verdicts are structurally equal
     outputs — a dimension without an explicit verdict is a structural gap. Only
     DEFEATED dimensions advance to Phase 6. <<]

ENTRY CONDITION: Phase 4 EXIT CRITERION met (all four delta categories present).
Do NOT open Phase 5 until Phase 4 EXIT CRITERION is confirmed in output above.

Verdict semantics:
- DEFEATED: challenger evidence overcomes INERTIA's Phase 1 defense.
  Dimension advances to Phase 6.
- HOLDS: INERTIA's defense survives. Dimension receives NO CHANGE.
  Dimension has no path to Phase 6.

| Defense ID | Dimension | INERTIA's defense | Challenger evidence | Verdict (DEFEATED / HOLDS) | Consequence if HOLDS |

Confidence tiers (DEFEATED rows only):
- HIGH: two or more independent NEW artifacts on the same dimension
- MEDIUM: one NEW artifact
- LOW: inference only

If all verdicts are HOLDS: emit "NULL_DELTA: INERTIA RETAINED ACROSS ALL DIMENSIONS."
Stop. Phase 6 does NOT open.

EXIT CRITERION: Verdict table complete; all dimensions adjudicated; NULL_DELTA
emitted if all HOLDS; at least one DEFEATED verdict present to proceed to Phase 6.

---

## Phase 6 — Change Proposals (DEFEATED dimensions only)

[>> GUARD: INERTIA-GATE (Phase 6 entry) <<]
[>> Bias blocked: action-default bias <<]
[>> Mechanism: Only DEFEATED dimensions from Phase 5 appear here. HOLDS dimensions
     have no row and no path to this phase. A HOLDS dimension appearing in the
     proposal table is a structural violation detectable against Phase 5 output. <<]

ENTRY CONDITION: Phase 5 EXIT CRITERION met; at least one DEFEATED verdict present;
NULL_DELTA not emitted. Do NOT open Phase 6 if NULL_DELTA was emitted in Phase 5.

### 6a — Additions
| # | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because |
Null: "ADDITIONS: none — INERTIA holds on all addition candidates."

### 6b — Removals and Reprioritizations
| # | Action (REMOVE / REPRIORITIZE) | Dimension | Evidence | Before | After | Confidence | Consequence if unchanged | Inertia defeated because |
Null-REMOVALS: "REMOVALS: none — INERTIA holds."
Null-REPRIORITIZATIONS: "REPRIORITIZATIONS: none — INERTIA holds."

All 9 namespaces must have a row. Silence is not a null declaration.

EXIT CRITERION: All three change-type tables present with labeled nulls; all 9
namespaces covered; each DEFEATED dimension from Phase 5 has a corresponding row.
Phase 7 may NOT open until this is met.

---

## Phase 7 — Confirmation Gate

[>> GUARD: CONFIRMATION GATE <<]
[>> Bias blocked: recency bias; sunk-cost bias <<]
[>> Mechanism: The most-recently-read signals are disproportionately salient at
     this point. This gate requires explicit user confirmation before any write,
     ensuring the full proposal set is reviewed. The absence of NO is not implicit
     YES. <<]

[>> GUARD: WRITE GUARD <<]
[>> Bias blocked: premature closure bias <<]
[>> Mechanism: strategy.md is not modified until explicit YES or REVISED is received
     at this gate. The write step does not execute based on agent confidence in the
     proposals — only on explicit user authorization. strategy.md has NOT been
     modified at this point. <<]

ENTRY CONDITION: Phase 6 EXIT CRITERION met.
Do NOT modify strategy.md before Phase 7 confirmation is received.

Present: Phase 4 delta findings (all four categories), Phase 6 proposals (all
three tables — 6a and 6b).

---
PENDING CONFIRMATION — strategy.md has NOT been modified.
INERTIA currently holds. Proposed challenges: [N] additions / [N] removals / [N] reprioritizations

Reply YES to displace INERTIA on all listed dimensions
Reply NO to retain INERTIA (all dimensions unchanged)
Reply REVISED + edited table to displace INERTIA on custom dimensions
Reply WITHDRAW [#] to remove specific proposals before confirming
  WITHDRAW syntax: WITHDRAW [2] or WITHDRAW [1, 3]. Removes named proposals only;
  remainder is applied.
  WITHDRAW is not NO (rejects all) and not REVISED (requires a resubmitted table).
---
STOP HERE. Write nothing further until the user replies.

EXIT CRITERION: User has replied YES, NO, REVISED, or WITHDRAW.

---

## Phase 8 — Apply (after YES or REVISED only)

ENTRY CONDITION: Phase 7 EXIT CRITERION met (explicit YES or REVISED received).
Do NOT write to strategy.md before this ENTRY CONDITION is confirmed.

[>> GUARD: WRITE GUARD (confirmed) <<]
[>> Bias blocked: premature closure bias — write authorized by user at Phase 7 <<]

Write confirmed (non-withdrawn) changes to strategy.md.
No reformatting of unchanged sections.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations.
INERTIA displaced on: [dimension list]."
```
