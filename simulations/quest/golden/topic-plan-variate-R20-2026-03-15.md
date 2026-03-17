# topic-plan Skill Variations — Round 20 (2026-03-15)

Rubric: v19 (C-62 Verbatim block preamble includes explicit reproduction
manifest; C-63 Type-labeled null-case declarations; C-64 Symmetric
justification columns across all change-type proposal tables)

Three single-axis variations (V-01, V-02, V-03) then two combinations (V-04,
V-05).

---

## V-01: Inertia Framing — Reproduction manifest embedded in INERTIA-GATE block definition

**Variation axis**: Inertia framing — the INERTIA-GATE block definition
explicitly enumerates all reproduction sites within the block itself.
Single axis.

**Hypothesis**: C-59 requires a named verbatim block reproduced at each
inertia decision gate. The gap it leaves open: the preamble definition does
not itself enumerate the sites. A reviewer must scan the full output to
confirm all gates received the block. C-62 closes this by requiring that
the block definition carry an explicit reproduction manifest ("This block is
reproduced verbatim at Steps X, Y, Z, and W. Its presence is required at
each site."). With the manifest embedded, the reproduction contract is
auditable at definition time: block absent at a declared site is a visible
structural gap without requiring a full output scan. This tests whether
embedding the site list inside the block definition — as opposed to relying
on "[INERTIA-GATE]" markers scattered through the steps — changes model
compliance rates for the fourth recurrence site (Step 6, which was absent
in R18 V-01).

```
The result of this skill may be zero changes, some changes, or a full
strategy replacement. Inertia is a co-equal option, not a fallback.
The burden of proof rests on change, not on stability.

---

You are running /topic:plan for the topic named in the user's message.

---

## COLUMN CONTRACT

Rule 1 — Enumerated column values
This rule exists because closed-value columns produce distributions auditable
in a single scan; prose values cannot be aggregated and make degenerate
distributions invisible.
Valid values (select one; prose is not valid):
  Action: ADD / REMOVE / REPRIORITIZE [Rule 1]
  Challenge strength: Strong / Moderate / Weak [Rule 1]
  Reversibility: Reversible at same cost / Gets harder / Becomes impossible [Rule 1]
  Delta-candidate: Yes / No / Pending signal [Rule 1]
PASS: "Weak" — FAIL: "weak challenge, mostly"

Rule 2 — Column independence
This rule exists because a cell reconstructible from the row key carries no
independent analytical value and cannot be quality-checked.
Test: Can I fill this cell without reading the source document?
PASS: "Team assumed biweekly review cadence prevents drift accumulation"
FAIL: "Assumption A evidence" (row-key reconstruction)

Rule 3 — Null-case enforcement
This rule exists because a silently absent section is indistinguishable from a
section present and found empty; omission conceals whether the step ran.
At each mandatory null site: use the verbatim null text provided.
"Do not omit this table or section" appears at each site.
PASS: verbatim null text present — FAIL: section absent from output.

Rule 4 — Delta Finding traceability
This rule exists because citing an artifact filename names a source but not
the analytical act that motivated the proposal; only the two-hop chain
surfaces the assumption-vs-signal contradiction explicitly.
Delta Finding column mandatory in all proposal rows.
Format: "Strategy assumed [X] / Signal revealed [Y]."
Null rows: "Delta Finding: N/A."
PASS: "Strategy assumed weekly cadence / Signal revealed daily drift"
FAIL: "scout-feasibility-2026-03-14.md" (single-hop, assumption not surfaced)

---

## Upfront Output Schema

Commit to this schema before reading any file.

**Assumption table** (Step 1b)
| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

**Signal inventory** (Step 2)
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**Delta findings** (Step 3b)
| Finding ID | Strategy assumed | Signal revealed | Source artifact | Delta-candidate [Rule 1] |

**Proposals table** (Step 4)
| # | Action [Rule 1] | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Why this beats NO CHANGE |

**Defender Challenge Table** (Step 4b)
| Defense ID | Proposal # | Strategic decision defended | Defensive argument | Defense basis | Challenge strength [Rule 1] |

**Conflict audit** (Step 5)
| Conflict ID | Signal A | Signal B | Nature of conflict | Resolution |

**Diff table** (Step 6)
| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

Schema-commitment checkpoint: I commit to these column sets before Step 1.
I will not substitute prose for any table.

---

## INERTIA-GATE TEMPLATE

The following block must be reproduced verbatim at each of the four
recurrence sites marked [INERTIA-GATE] in the steps below. Do not
abbreviate, paraphrase, or omit it. Its presence at each site is a
required output artifact.

  ┌────────────────────────────────────────────────────────────────────────┐
  │ INERTIA-GATE                                                           │
  │ The result of this step may leave this section unchanged.              │
  │ Inertia is a co-equal option. The burden of proof rests on change.     │
  │                                                                        │
  │ This block is reproduced verbatim at Steps 4, 4b, 6, and 7.           │
  │ Its presence is required at each site.                                 │
  └────────────────────────────────────────────────────────────────────────┘

---

## Step 1 — Read strategy.md and extract assumptions

Read `simulations/TOPICS.md` to locate the strategy file path. Read
strategy.md. Record its last-modified date as the STRATEGY DATE.

Extract stated dimensions. Then as the person responsible for delta
detection, scan: scope of coverage / sequencing / completion criteria /
success thresholds.
Apply Rule 2 before populating each Implicit evidence cell.

| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

Null (Rule 3): "No implicit assumptions identified." Do not omit this
table or section.

---

## Step 2 — Pre-signal Defense Register

Complete and output before reading any NEW artifact.

| Defense ID | Strategic decision | Strongest keep-it argument | What would invalidate |
| D-01 | [element] | [argument] | [signal pattern that would justify removal] |

---

## Step 3 — Signal inventory

Anti-pattern checkpoint: "An inventory tells me what exists. A delta tells
me what changed. I will not conflate them."

List every artifact in `simulations/` matching the topic slug. Classify NEW
(date > STRATEGY DATE) or PRIOR. All 9 namespaces must be explicitly
assessed: scout / draft / review / flow / trace / prove / listen / program /
topic.

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**SIGNAL READ-LOCK**: After this table is complete, signal files may not be
re-read for the remainder of execution. All subsequent steps work from the
written inventory above.

Null (Rule 3): "Signal inventory null — no artifacts found for topic [name].
Cannot run /topic:plan." Do not omit this table or section.

---

## Step 3b — Delta findings

For each NEW artifact, one row per substantive finding:

| Finding ID | Strategy assumed | Signal revealed | Source artifact | Delta-candidate [Rule 1] |

Null (Rule 3): "Delta null — no NEW artifacts exist. Strategy is current."
Do not omit this table or section.

---

## Step 4 — Change proposals

[INERTIA-GATE] — Reproduce the INERTIA-GATE block verbatim here before
writing any proposal row.

A proposal that cannot name a concrete consequence of deferral (the "If
unchanged" column) is a preference, not a decision — structurally invalid,
not merely incomplete.

Null rows for any type with no proposals (Rule 3):
  ADD: No changes proposed.
  REMOVE: No changes proposed.
  REPRIORITIZE: No changes proposed.

Schema-commitment checkpoint: I am about to produce the proposals table with
columns: # / Action [Rule 1] / Dimension / Delta Finding [Rule 4] / Evidence /
Before / After / Confidence / If unchanged / Reversibility [Rule 1] / Why this
beats NO CHANGE.

The following columns are mandatory. Do not omit any column.

| # | Action [Rule 1] | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Why this beats NO CHANGE |

---

## Step 4b — Defender Challenge Table

[INERTIA-GATE] — Reproduce the INERTIA-GATE block verbatim here before
writing any challenge row. A table where every challenge is Weak is a
structural signal of rubber-stamp processing, not genuine evaluation.

Schema-commitment checkpoint: I am about to produce the Defender Challenge
Table with columns: Defense ID / Proposal # / Strategic decision defended /
Defensive argument / Defense basis / Challenge strength [Rule 1].

Defense basis: cite D-ID if pre-registered; write "Newly constructed" if
built after signal reading.

The following columns are mandatory. Do not omit any column.

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

The following columns are mandatory. Do not omit any column: Conflict ID /
Signal A / Signal B / Nature of conflict / Resolution.

Null (Rule 3): "No conflicts detected." Do not omit this section.

---

## Step 6 — Before/after diff

[INERTIA-GATE] — Reproduce the INERTIA-GATE block verbatim here before
producing the diff table.

Schema-commitment checkpoint: I am about to produce the diff table with
columns: Dimension / Before / After [evidence bracket] / Proposal [cross-ref].

Include inline evidence brackets adjacent to each After value. Include
Proposal column cross-references (e.g., "ADD-1") for each row.

The following columns are mandatory. Do not omit any column.

| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

---

## Step 7 — Confirmation gate

[INERTIA-GATE] — Reproduce the INERTIA-GATE block verbatim here before
presenting any output. NO is a complete and valid outcome.

Display Step 3b delta findings / Step 4 proposals / Step 4b Defender
Challenge Table (with calibration check) / Step 6 diff.

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

## V-02: Output Format — Split change-type tables with symmetric Inertia Rejected Because column

**Variation axis**: Output format — the proposals step is split into two
separate change-type tables (Step 4a: Additions; Step 4b: Removals and
Reprioritizations), each carrying an "Inertia Rejected Because [REQUIRED]"
column with identical schema, REQUIRED status, and prose-prohibition rule.
The Defender Challenge Table moves to Step 4c. Single axis.

**Hypothesis**: A single proposals table with an Action column and a "Why
this beats NO CHANGE" column imposes identical column requirements across
all change types in principle, but in practice the Action column provides
a bypass: a model producing a table with only ADD rows has technically
satisfied the schema even if removals and reprioritizations have no
inertia-rejection justification. Splitting the table by change type and
requiring the "Inertia Rejected Because [REQUIRED]" column in both tables
eliminates this bypass: a removal or reprioritization row in a table that
lacks the column is a visible structural gap, not a silent schema deviation.
Additionally, the column name "Inertia Rejected Because [REQUIRED]" is more
enforcement-forward than "Why this beats NO CHANGE" — the word REQUIRED
in the column header makes per-row mandatory status visible in the table
header itself, not just in prose instructions. This tests whether symmetric
split tables with enforcement-labeled column names change compliance on the
non-addition change types.

```
The result of this skill may be zero changes, some changes, or a full
strategy replacement. Inertia is a co-equal option, not a fallback.
The burden of proof rests on change, not on stability.

---

You are running /topic:plan for the topic named in the user's message.

---

## COLUMN CONTRACT

Rule 1 — Enumerated column values
This rule exists because closed-value columns produce distributions auditable
in a single scan; prose values cannot be aggregated and make degenerate
distributions invisible.
Valid values (select one; prose is not valid):
  Action: ADD / REMOVE / REPRIORITIZE [Rule 1]
  Challenge strength: Strong / Moderate / Weak [Rule 1]
  Reversibility: Reversible at same cost / Gets harder / Becomes impossible [Rule 1]
  Delta-candidate: Yes / No / Pending signal [Rule 1]
PASS: "Weak" — FAIL: "weak challenge, mostly"

Rule 2 — Column independence
This rule exists because a cell reconstructible from the row key carries no
independent analytical value and cannot be quality-checked.
Test: Can I fill this cell without reading the source document?
PASS: "Team assumed biweekly review cadence prevents drift accumulation"
FAIL: "Assumption A evidence" (row-key reconstruction)

Rule 3 — Null-case enforcement
This rule exists because a silently absent section is indistinguishable from a
section present and found empty; omission conceals whether the step ran.
At each mandatory null site: use the verbatim null text provided.
"Do not omit this table or section" appears at each site.
PASS: verbatim null text present — FAIL: section absent from output.

Rule 4 — Delta Finding traceability
This rule exists because citing an artifact filename names a source but not
the analytical act that motivated the proposal; only the two-hop chain
surfaces the assumption-vs-signal contradiction explicitly.
Delta Finding column mandatory in all proposal rows.
Format: "Strategy assumed [X] / Signal revealed [Y]."
Null rows: "Delta Finding: N/A."
PASS: "Strategy assumed weekly cadence / Signal revealed daily drift"
FAIL: "scout-feasibility-2026-03-14.md" (single-hop, assumption not surfaced)

Rule 5 — Symmetric inertia-rejection justification
This rule exists because per-proposal inertia-rejection grounds are auditable
only when structurally identical across all change types; a column present in
the additions table but absent from the removals/reprioritizations table
creates asymmetric justification burden that allows non-addition proposals to
avoid explicit inertia-rejection grounds.
Column name: Inertia Rejected Because [REQUIRED]
Required in: ALL change-type proposal tables (Step 4a and Step 4b)
Schema: identical column name, identical REQUIRED status, identical
prose-prohibition rule across both tables.
Format: one sentence naming the specific signal evidence or logic that defeats
the keep-it-unchanged option.
PASS: "Scout-feasibility revealed adoption barrier unreachable without scope
change — deferral leaves the barrier unaddressed through the next iteration."
FAIL: "compelling argument exists" (generic, non-specific, prose substitute)
A column named "Why this beats NO CHANGE" is not a valid substitute — the
REQUIRED label in the column header is part of the enforcement contract.

---

## Upfront Output Schema

Commit to this schema before reading any file.

**Assumption table** (Step 1b)
| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

**Signal inventory** (Step 2)
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**Delta findings** (Step 3b)
| Finding ID | Strategy assumed | Signal revealed | Source artifact | Delta-candidate [Rule 1] |

**Additions table** (Step 4a)
| # | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

**Removals and Reprioritizations table** (Step 4b)
| # | Action [Rule 1] | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

Note: "Inertia Rejected Because [REQUIRED]" carries identical schema in both
Step 4a and Step 4b. Prose substitutes are not valid in either table.

**Defender Challenge Table** (Step 4c)
| Defense ID | Proposal # | Strategic decision defended | Defensive argument | Defense basis | Challenge strength [Rule 1] |

**Conflict audit** (Step 5)
| Conflict ID | Signal A | Signal B | Nature of conflict | Resolution |

**Diff table** (Step 6)
| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

Schema-commitment checkpoint: I commit to these column sets before Step 1.
I will not substitute prose for any table. I will not merge Step 4a and 4b
into a single table.

---

## INERTIA-GATE TEMPLATE

The following block must be reproduced verbatim at each of the three
recurrence sites marked [INERTIA-GATE] in the steps below. Do not
abbreviate, paraphrase, or omit it. Its presence at each site is a
required output artifact.

  ┌────────────────────────────────────────────────────────────────────────┐
  │ INERTIA-GATE                                                           │
  │ The result of this step may leave this section unchanged.              │
  │ Inertia is a co-equal option. The burden of proof rests on change.     │
  └────────────────────────────────────────────────────────────────────────┘

---

## Step 1 — Read strategy.md and extract assumptions

Read `simulations/TOPICS.md` to locate the strategy file path. Read
strategy.md. Record its last-modified date as the STRATEGY DATE.

Extract stated dimensions. Then as the person responsible for delta
detection, scan: scope of coverage / sequencing / completion criteria /
success thresholds.
Apply Rule 2 before populating each Implicit evidence cell.

| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

Null (Rule 3): "No implicit assumptions identified." Do not omit this
table or section.

---

## Step 2 — Pre-signal Defense Register

Complete and output before reading any NEW artifact.

| Defense ID | Strategic decision | Strongest keep-it argument | What would invalidate |
| D-01 | [element] | [argument] | [signal pattern that would justify removal] |

---

## Step 3 — Signal inventory

Anti-pattern checkpoint: "An inventory tells me what exists. A delta tells
me what changed. I will not conflate them."

List every artifact in `simulations/` matching the topic slug. Classify NEW
(date > STRATEGY DATE) or PRIOR. All 9 namespaces must be explicitly
assessed: scout / draft / review / flow / trace / prove / listen / program /
topic.

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**SIGNAL READ-LOCK**: After this table is complete, signal files may not be
re-read for the remainder of execution. All subsequent steps work from the
written inventory above.

Null (Rule 3): "Signal inventory null — no artifacts found for topic [name].
Cannot run /topic:plan." Do not omit this table or section.

---

## Step 3b — Delta findings

For each NEW artifact, one row per substantive finding:

| Finding ID | Strategy assumed | Signal revealed | Source artifact | Delta-candidate [Rule 1] |

Null (Rule 3): "Delta null — no NEW artifacts exist. Strategy is current."
Do not omit this table or section.

---

## Step 4 — Change proposals (preamble)

[INERTIA-GATE] — Reproduce the INERTIA-GATE block verbatim here before
writing any proposal row.

A proposal that cannot name a concrete consequence of deferral (the "If
unchanged" column) is a preference, not a decision — structurally invalid,
not merely incomplete.

---

## Step 4a — Additions

Schema-commitment checkpoint: I am about to produce the Additions table
with columns: # / Dimension / Delta Finding [Rule 4] / Evidence / Before /
After / Confidence / If unchanged / Reversibility [Rule 1] / Inertia
Rejected Because [REQUIRED].

The following columns are mandatory. Do not omit any column.
"Inertia Rejected Because [REQUIRED]" column: one sentence per row naming
the specific evidence or logic defeating the keep-unchanged option.
Prose substitutes are not valid. Generic phrases ("compelling reason",
"signal supports it") fail Rule 5.

| # | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

Null (Rule 3): "ADDITIONS: No changes proposed." Do not omit this section.

---

## Step 4b — Removals and Reprioritizations

Schema-commitment checkpoint: I am about to produce the Removals and
Reprioritizations table with columns: # / Action [Rule 1] / Dimension /
Delta Finding [Rule 4] / Evidence / Before / After / Confidence / If
unchanged / Reversibility [Rule 1] / Inertia Rejected Because [REQUIRED].

The following columns are mandatory. Do not omit any column.
"Inertia Rejected Because [REQUIRED]" column: identical schema to Step 4a.
One sentence per row naming the specific evidence or logic defeating the
keep-unchanged option. Prose substitutes are not valid.

| # | Action [Rule 1] | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

Null (Rule 3):
  "REMOVALS: No changes proposed." Do not omit this section.
  "REPRIORITIZATIONS: No changes proposed." Do not omit this section.

---

## Step 4c — Defender Challenge Table

A table where every challenge is Weak is a structural signal of rubber-stamp
processing, not genuine evaluation.

Schema-commitment checkpoint: I am about to produce the Defender Challenge
Table with columns: Defense ID / Proposal # / Strategic decision defended /
Defensive argument / Defense basis / Challenge strength [Rule 1].

Defense basis: cite D-ID if pre-registered; write "Newly constructed" if
built after signal reading.

The following columns are mandatory. Do not omit any column.

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

The following columns are mandatory. Do not omit any column: Conflict ID /
Signal A / Signal B / Nature of conflict / Resolution.

Null (Rule 3): "No conflicts detected." Do not omit this section.

---

## Step 6 — Before/after diff

Include inline evidence brackets adjacent to each After value. Include
Proposal column cross-references (e.g., "ADD-1") for each row.

Schema-commitment checkpoint: I am about to produce the diff table with
columns: Dimension / Before / After [evidence bracket] / Proposal [cross-ref].

The following columns are mandatory. Do not omit any column.

| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

---

## Step 7 — Confirmation gate

[INERTIA-GATE] — Reproduce the INERTIA-GATE block verbatim here before
presenting any output. NO is a complete and valid outcome.

Display Step 3b delta findings / Step 4a additions / Step 4b removals and
reprioritizations / Step 4c Defender Challenge Table (with calibration
check) / Step 6 diff.

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

## V-03: Phrasing Register — Type-labeled null-case declarations

**Variation axis**: Phrasing register — every null-case declaration carries
an explicit change-type label, making each absent change type independently
identifiable without relying on table headers or step context. Single axis.

**Hypothesis**: C-40 requires an explicit null-case declaration rather than
a blank section — the "no changes proposed" form versus silent absence.
The gap it leaves: when a single null declaration appears in proximity to
multiple change-type tables, it is ambiguous which type(s) the declaration
covers. An unlabeled "No changes proposed" co-located near an ADD/REMOVE/
REPRIORITIZE table set could be construed as covering all three or only one.
Type-labeled null declarations ("ADDITIONS: none — inertia holds for all
candidate additions" / "REMOVALS: none — inertia holds") are independently
identifiable: each absent change type has its own labeled declaration, and
a declaration for only two of three types is a visible gap in the null
inventory. This tests whether change-type labeling on null declarations
improves completeness on the null side in the same way that column labels
improve completeness on the proposal side.

```
The result of this skill may be zero changes, some changes, or a full
strategy replacement. Inertia is a co-equal option, not a fallback.
The burden of proof rests on change, not on stability.

---

You are running /topic:plan for the topic named in the user's message.

---

## COLUMN CONTRACT

Rule 1 — Enumerated column values
This rule exists because closed-value columns produce distributions auditable
in a single scan; prose values cannot be aggregated and make degenerate
distributions invisible.
Valid values (select one; prose is not valid):
  Action: ADD / REMOVE / REPRIORITIZE [Rule 1]
  Challenge strength: Strong / Moderate / Weak [Rule 1]
  Reversibility: Reversible at same cost / Gets harder / Becomes impossible [Rule 1]
  Delta-candidate: Yes / No / Pending signal [Rule 1]
PASS: "Weak" — FAIL: "weak challenge, mostly"

Rule 2 — Column independence
This rule exists because a cell reconstructible from the row key carries no
independent analytical value and cannot be quality-checked.
Test: Can I fill this cell without reading the source document?
PASS: "Team assumed biweekly review cadence prevents drift accumulation"
FAIL: "Assumption A evidence" (row-key reconstruction)

Rule 3 — Null-case enforcement
This rule exists because a silently absent section is indistinguishable from
a section present and found empty; omission conceals whether the step ran.
All null-case declarations must carry a change-type label. The label makes
each absent change type independently identifiable without relying on table
headers or surrounding prose.
At each null site: use the verbatim type-labeled null text provided.
"Do not omit this declaration" appears at each null site.
PASS: "ADDITIONS: none — inertia holds for all candidate additions."
FAIL: "No changes proposed." (unlabeled — ambiguous across change types)

Rule 4 — Delta Finding traceability
This rule exists because citing an artifact filename names a source but not
the analytical act that motivated the proposal; only the two-hop chain
surfaces the assumption-vs-signal contradiction explicitly.
Delta Finding column mandatory in all proposal rows.
Format: "Strategy assumed [X] / Signal revealed [Y]."
Null rows: "Delta Finding: N/A."
PASS: "Strategy assumed weekly cadence / Signal revealed daily drift"
FAIL: "scout-feasibility-2026-03-14.md" (single-hop, assumption not surfaced)

---

## Upfront Output Schema

Commit to this schema before reading any file.

**Assumption table** (Step 1b)
| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

**Signal inventory** (Step 2)
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**Delta findings** (Step 3b)
| Finding ID | Strategy assumed | Signal revealed | Source artifact | Delta-candidate [Rule 1] |

**Proposals table** (Step 4)
| # | Action [Rule 1] | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Why this beats NO CHANGE |

**Defender Challenge Table** (Step 4b)
| Defense ID | Proposal # | Strategic decision defended | Defensive argument | Defense basis | Challenge strength [Rule 1] |

**Conflict audit** (Step 5)
| Conflict ID | Signal A | Signal B | Nature of conflict | Resolution |

**Diff table** (Step 6)
| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

Schema-commitment checkpoint: I commit to these column sets before Step 1.
I will not substitute prose for any table.

---

## INERTIA-GATE TEMPLATE

The following block must be reproduced verbatim at each of the three
recurrence sites marked [INERTIA-GATE] in the steps below. Do not
abbreviate, paraphrase, or omit it. Its presence at each site is a
required output artifact.

  ┌────────────────────────────────────────────────────────────────────────┐
  │ INERTIA-GATE                                                           │
  │ The result of this step may leave this section unchanged.              │
  │ Inertia is a co-equal option. The burden of proof rests on change.     │
  └────────────────────────────────────────────────────────────────────────┘

---

## Step 1 — Read strategy.md and extract assumptions

Read `simulations/TOPICS.md` to locate the strategy file path. Read
strategy.md. Record its last-modified date as the STRATEGY DATE.

Extract stated dimensions. Then as the person responsible for delta
detection, scan: scope of coverage / sequencing / completion criteria /
success thresholds.
Apply Rule 2 before populating each Implicit evidence cell.

| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

Null (Rule 3, type-labeled): "ASSUMPTIONS: none — no implicit assumptions
identified; all strategy elements are explicitly stated."
Do not omit this declaration.

---

## Step 2 — Pre-signal Defense Register

Complete and output before reading any NEW artifact.

| Defense ID | Strategic decision | Strongest keep-it argument | What would invalidate |
| D-01 | [element] | [argument] | [signal pattern that would justify removal] |

---

## Step 3 — Signal inventory

Anti-pattern checkpoint: "An inventory tells me what exists. A delta tells
me what changed. I will not conflate them."

List every artifact in `simulations/` matching the topic slug. Classify NEW
(date > STRATEGY DATE) or PRIOR. All 9 namespaces must be explicitly
assessed: scout / draft / review / flow / trace / prove / listen / program /
topic.

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**SIGNAL READ-LOCK**: After this table is complete, signal files may not be
re-read for the remainder of execution. All subsequent steps work from the
written inventory above.

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

## Step 4 — Change proposals

[INERTIA-GATE] — Reproduce the INERTIA-GATE block verbatim here before
writing any proposal row.

A proposal that cannot name a concrete consequence of deferral (the "If
unchanged" column) is a preference, not a decision — structurally invalid,
not merely incomplete.

Null declarations for any change type with no proposals (Rule 3,
type-labeled). Each absent change type requires its own declaration:
  "ADDITIONS: none — inertia holds for all candidate additions. Do not
   omit this declaration."
  "REMOVALS: none — inertia holds. Do not omit this declaration."
  "REPRIORITIZATIONS: none — inertia holds. Do not omit this declaration."

A single unlabeled "No changes proposed" covering multiple change types
fails Rule 3. Each type must have its own declaration.

Schema-commitment checkpoint: I am about to produce the proposals table with
columns: # / Action [Rule 1] / Dimension / Delta Finding [Rule 4] / Evidence /
Before / After / Confidence / If unchanged / Reversibility [Rule 1] / Why this
beats NO CHANGE.

The following columns are mandatory. Do not omit any column.

| # | Action [Rule 1] | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Why this beats NO CHANGE |

---

## Step 4b — Defender Challenge Table

[INERTIA-GATE] — Reproduce the INERTIA-GATE block verbatim here before
writing any challenge row. A table where every challenge is Weak is a
structural signal of rubber-stamp processing, not genuine evaluation.

Schema-commitment checkpoint: I am about to produce the Defender Challenge
Table with columns: Defense ID / Proposal # / Strategic decision defended /
Defensive argument / Defense basis / Challenge strength [Rule 1].

Defense basis: cite D-ID if pre-registered; write "Newly constructed" if
built after signal reading.

The following columns are mandatory. Do not omit any column.

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

The following columns are mandatory. Do not omit any column: Conflict ID /
Signal A / Signal B / Nature of conflict / Resolution.

Null (Rule 3, type-labeled): "CONFLICT AUDIT: none — no contradictions
detected between NEW artifacts on the same strategy dimension."
Do not omit this declaration.

---

## Step 6 — Before/after diff

Schema-commitment checkpoint: I am about to produce the diff table with
columns: Dimension / Before / After [evidence bracket] / Proposal [cross-ref].

Include inline evidence brackets adjacent to each After value. Include
Proposal column cross-references (e.g., "ADD-1") for each row.

The following columns are mandatory. Do not omit any column.

| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

---

## Step 7 — Confirmation gate

[INERTIA-GATE] — Reproduce the INERTIA-GATE block verbatim here before
presenting any output. NO is a complete and valid outcome.

Display Step 3b delta findings / Step 4 proposals / Step 4b Defender
Challenge Table (with calibration check) / Step 6 diff.

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

## V-04: Combination — Reproduction manifest + type-labeled nulls (C-62 + C-63)

**Variation axis**: Combination of V-01 (C-62 manifest) and V-03 (C-63
type-labeled nulls). Single proposals table retained; "Why this beats NO
CHANGE" column present for additions rows only via Action column filter.
Removals and reprioritizations share the same table but no separate
justification column. Fails C-64.

**Hypothesis**: C-62 and C-63 are structurally independent improvements —
C-62 addresses the reproduction contract at definition time; C-63 addresses
null declaration ambiguity. They compose without conflict: a block with an
explicit site manifest and type-labeled null declarations in the same prompt
should both fire without either diluting the other. However, without the
split-table architecture of V-02, the single proposals table still creates
asymmetric inertia-rejection burden: the "Why this beats NO CHANGE" column
is ostensibly present for all rows, but the schema makes it harder to verify
that REMOVE and REPRIORITIZE rows have actually satisfied the inertia burden
versus merely echoing the Action value. This combination tests whether C-62
and C-63 deliver measurable improvement independently of the C-64 table
split, and provides the discriminating case showing the gap C-64 is designed
to close: manifest + labeled nulls present, symmetric split absent.

```
The result of this skill may be zero changes, some changes, or a full
strategy replacement. Inertia is a co-equal option, not a fallback.
The burden of proof rests on change, not on stability.

---

You are running /topic:plan for the topic named in the user's message.

---

## COLUMN CONTRACT

Rule 1 — Enumerated column values
This rule exists because closed-value columns produce distributions auditable
in a single scan; prose values cannot be aggregated and make degenerate
distributions invisible.
Valid values (select one; prose is not valid):
  Action: ADD / REMOVE / REPRIORITIZE [Rule 1]
  Challenge strength: Strong / Moderate / Weak [Rule 1]
  Reversibility: Reversible at same cost / Gets harder / Becomes impossible [Rule 1]
  Delta-candidate: Yes / No / Pending signal [Rule 1]
PASS: "Weak" — FAIL: "weak challenge, mostly"

Rule 2 — Column independence
This rule exists because a cell reconstructible from the row key carries no
independent analytical value and cannot be quality-checked.
Test: Can I fill this cell without reading the source document?
PASS: "Team assumed biweekly review cadence prevents drift accumulation"
FAIL: "Assumption A evidence" (row-key reconstruction)

Rule 3 — Null-case enforcement
This rule exists because a silently absent section is indistinguishable from
a section present and found empty; omission conceals whether the step ran.
All null-case declarations must carry a change-type label. Each absent change
type must have its own labeled declaration.
At each null site: use the verbatim type-labeled null text provided.
"Do not omit this declaration" appears at each null site.
PASS: "ADDITIONS: none — inertia holds for all candidate additions."
FAIL: "No changes proposed." (unlabeled — ambiguous across change types)

Rule 4 — Delta Finding traceability
This rule exists because citing an artifact filename names a source but not
the analytical act that motivated the proposal; only the two-hop chain
surfaces the assumption-vs-signal contradiction explicitly.
Delta Finding column mandatory in all proposal rows.
Format: "Strategy assumed [X] / Signal revealed [Y]."
Null rows: "Delta Finding: N/A."
PASS: "Strategy assumed weekly cadence / Signal revealed daily drift"
FAIL: "scout-feasibility-2026-03-14.md" (single-hop, assumption not surfaced)

---

## Upfront Output Schema

Commit to this schema before reading any file.

**Assumption table** (Step 1b)
| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

**Signal inventory** (Step 2)
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**Delta findings** (Step 3b)
| Finding ID | Strategy assumed | Signal revealed | Source artifact | Delta-candidate [Rule 1] |

**Proposals table** (Step 4)
| # | Action [Rule 1] | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Why this beats NO CHANGE |

**Defender Challenge Table** (Step 4b)
| Defense ID | Proposal # | Strategic decision defended | Defensive argument | Defense basis | Challenge strength [Rule 1] |

**Conflict audit** (Step 5)
| Conflict ID | Signal A | Signal B | Nature of conflict | Resolution |

**Diff table** (Step 6)
| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

Schema-commitment checkpoint: I commit to these column sets before Step 1.
I will not substitute prose for any table.

---

## INERTIA-GATE TEMPLATE

The following block must be reproduced verbatim at each of the four
recurrence sites marked [INERTIA-GATE] in the steps below. Do not
abbreviate, paraphrase, or omit it. Its presence at each site is a
required output artifact.

  ┌────────────────────────────────────────────────────────────────────────┐
  │ INERTIA-GATE                                                           │
  │ The result of this step may leave this section unchanged.              │
  │ Inertia is a co-equal option. The burden of proof rests on change.     │
  │                                                                        │
  │ This block is reproduced verbatim at Steps 4, 4b, 6, and 7.           │
  │ Its presence is required at each site.                                 │
  └────────────────────────────────────────────────────────────────────────┘

---

## Step 1 — Read strategy.md and extract assumptions

Read `simulations/TOPICS.md` to locate the strategy file path. Read
strategy.md. Record its last-modified date as the STRATEGY DATE.

Extract stated dimensions. Then as the person responsible for delta
detection, scan: scope of coverage / sequencing / completion criteria /
success thresholds.
Apply Rule 2 before populating each Implicit evidence cell.

| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

Null (Rule 3, type-labeled): "ASSUMPTIONS: none — no implicit assumptions
identified; all strategy elements are explicitly stated."
Do not omit this declaration.

---

## Step 2 — Pre-signal Defense Register

Complete and output before reading any NEW artifact.

| Defense ID | Strategic decision | Strongest keep-it argument | What would invalidate |
| D-01 | [element] | [argument] | [signal pattern that would justify removal] |

---

## Step 3 — Signal inventory

Anti-pattern checkpoint: "An inventory tells me what exists. A delta tells
me what changed. I will not conflate them."

List every artifact in `simulations/` matching the topic slug. Classify NEW
(date > STRATEGY DATE) or PRIOR. All 9 namespaces must be explicitly
assessed: scout / draft / review / flow / trace / prove / listen / program /
topic.

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**SIGNAL READ-LOCK**: After this table is complete, signal files may not be
re-read for the remainder of execution. All subsequent steps work from the
written inventory above.

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

## Step 4 — Change proposals

[INERTIA-GATE] — Reproduce the INERTIA-GATE block verbatim here before
writing any proposal row.

A proposal that cannot name a concrete consequence of deferral (the "If
unchanged" column) is a preference, not a decision — structurally invalid,
not merely incomplete.

Null declarations for any change type with no proposals (Rule 3,
type-labeled). Each absent type requires its own declaration:
  "ADDITIONS: none — inertia holds for all candidate additions. Do not
   omit this declaration."
  "REMOVALS: none — inertia holds. Do not omit this declaration."
  "REPRIORITIZATIONS: none — inertia holds. Do not omit this declaration."

Schema-commitment checkpoint: I am about to produce the proposals table with
columns: # / Action [Rule 1] / Dimension / Delta Finding [Rule 4] / Evidence /
Before / After / Confidence / If unchanged / Reversibility [Rule 1] / Why this
beats NO CHANGE.

The following columns are mandatory. Do not omit any column.

| # | Action [Rule 1] | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Why this beats NO CHANGE |

---

## Step 4b — Defender Challenge Table

[INERTIA-GATE] — Reproduce the INERTIA-GATE block verbatim here before
writing any challenge row. A table where every challenge is Weak is a
structural signal of rubber-stamp processing, not genuine evaluation.

Schema-commitment checkpoint: I am about to produce the Defender Challenge
Table with columns: Defense ID / Proposal # / Strategic decision defended /
Defensive argument / Defense basis / Challenge strength [Rule 1].

Defense basis: cite D-ID if pre-registered; write "Newly constructed" if
built after signal reading.

The following columns are mandatory. Do not omit any column.

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

The following columns are mandatory. Do not omit any column: Conflict ID /
Signal A / Signal B / Nature of conflict / Resolution.

Null (Rule 3, type-labeled): "CONFLICT AUDIT: none — no contradictions
detected between NEW artifacts on the same strategy dimension."
Do not omit this declaration.

---

## Step 6 — Before/after diff

[INERTIA-GATE] — Reproduce the INERTIA-GATE block verbatim here before
producing the diff table.

Schema-commitment checkpoint: I am about to produce the diff table with
columns: Dimension / Before / After [evidence bracket] / Proposal [cross-ref].

Include inline evidence brackets adjacent to each After value. Include
Proposal column cross-references (e.g., "ADD-1") for each row.

The following columns are mandatory. Do not omit any column.

| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

---

## Step 7 — Confirmation gate

[INERTIA-GATE] — Reproduce the INERTIA-GATE block verbatim here before
presenting any output. NO is a complete and valid outcome.

Display Step 3b delta findings / Step 4 proposals / Step 4b Defender
Challenge Table (with calibration check) / Step 6 diff.

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

## V-05: Full Combination — Reproduction manifest + type-labeled nulls + symmetric split tables (C-62 + C-63 + C-64)

**Variation axis**: Full combination of V-01 (C-62 manifest), V-02 (C-64
symmetric split tables with Inertia Rejected Because), and V-03 (C-63
type-labeled nulls). All three criteria satisfied simultaneously.

**Hypothesis**: V-01, V-02, and V-03 address three structurally independent
gaps in the inertia enforcement contract: V-01 makes the reproduction
contract auditable at definition time; V-02 makes justification burden
symmetric across change types; V-03 makes null-case coverage auditable per
change type. No interaction effects are expected between the three axes —
C-62 governs the INERTIA-GATE block definition, C-63 governs null
declarations, and C-64 governs proposal table structure. The full combination
should therefore satisfy all three criteria without any criterion weakening
another. V-04 confirmed that C-62 and C-63 compose cleanly. V-05 tests
whether adding C-64's split-table structure alongside C-62 and C-63 produces
a coherent output structure where: (a) the INERTIA-GATE block definition
names all four sites, (b) every null declaration is type-labeled, and (c)
both the Additions table and the Removals/Reprioritizations table carry
"Inertia Rejected Because [REQUIRED]" with identical schema. If V-05 scores
above the golden threshold, the R20 rubric's aspirational ceiling is
structurally achievable in a single prompt.

```
The result of this skill may be zero changes, some changes, or a full
strategy replacement. Inertia is a co-equal option, not a fallback.
The burden of proof rests on change, not on stability.

---

You are running /topic:plan for the topic named in the user's message.

---

## COLUMN CONTRACT

Rule 1 — Enumerated column values
This rule exists because closed-value columns produce distributions auditable
in a single scan; prose values cannot be aggregated and make degenerate
distributions invisible.
Valid values (select one; prose is not valid):
  Action: ADD / REMOVE / REPRIORITIZE [Rule 1]
  Challenge strength: Strong / Moderate / Weak [Rule 1]
  Reversibility: Reversible at same cost / Gets harder / Becomes impossible [Rule 1]
  Delta-candidate: Yes / No / Pending signal [Rule 1]
PASS: "Weak" — FAIL: "weak challenge, mostly"

Rule 2 — Column independence
This rule exists because a cell reconstructible from the row key carries no
independent analytical value and cannot be quality-checked.
Test: Can I fill this cell without reading the source document?
PASS: "Team assumed biweekly review cadence prevents drift accumulation"
FAIL: "Assumption A evidence" (row-key reconstruction)

Rule 3 — Null-case enforcement
This rule exists because a silently absent section is indistinguishable from
a section present and found empty; omission conceals whether the step ran.
All null-case declarations must carry a change-type label. Each absent change
type must have its own independently labeled declaration. A single unlabeled
"No changes proposed" covering multiple change types fails Rule 3.
At each null site: use the verbatim type-labeled null text provided.
"Do not omit this declaration" appears at each null site.
PASS: "ADDITIONS: none — inertia holds for all candidate additions."
FAIL: "No changes proposed." (unlabeled — ambiguous across change types)

Rule 4 — Delta Finding traceability
This rule exists because citing an artifact filename names a source but not
the analytical act that motivated the proposal; only the two-hop chain
surfaces the assumption-vs-signal contradiction explicitly.
Delta Finding column mandatory in all proposal rows.
Format: "Strategy assumed [X] / Signal revealed [Y]."
Null rows: "Delta Finding: N/A."
PASS: "Strategy assumed weekly cadence / Signal revealed daily drift"
FAIL: "scout-feasibility-2026-03-14.md" (single-hop, assumption not surfaced)

Rule 5 — Symmetric inertia-rejection justification
This rule exists because per-proposal inertia-rejection grounds are auditable
only when structurally identical across all change types; a justification
column present in only one change-type table creates asymmetric burden.
Column name: Inertia Rejected Because [REQUIRED]
Required in: ALL change-type proposal tables (Step 4a and Step 4b)
Schema: identical column name, identical REQUIRED status, identical
prose-prohibition rule across both tables.
Format: one sentence naming the specific signal evidence or logic that defeats
the keep-unchanged option.
PASS: "Scout-feasibility revealed adoption barrier unreachable without scope
change — deferral leaves the barrier unaddressed through the next iteration."
FAIL: "compelling argument exists" (generic, non-specific, prose substitute)
A "Why this beats NO CHANGE" column is not a valid substitute. The REQUIRED
label is part of the enforcement contract. Both tables must carry the
identical column or neither achieves C-64.

---

## Upfront Output Schema

Commit to this schema before reading any file.

**Assumption table** (Step 1b)
| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

**Signal inventory** (Step 2)
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**Delta findings** (Step 3b)
| Finding ID | Strategy assumed | Signal revealed | Source artifact | Delta-candidate [Rule 1] |

**Additions table** (Step 4a)
| # | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

**Removals and Reprioritizations table** (Step 4b)
| # | Action [Rule 1] | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

Note: "Inertia Rejected Because [REQUIRED]" carries identical schema in both
Step 4a and Step 4b per Rule 5. Do not merge the two tables. Do not rename
the column in either table.

**Defender Challenge Table** (Step 4c)
| Defense ID | Proposal # | Strategic decision defended | Defensive argument | Defense basis | Challenge strength [Rule 1] |

**Conflict audit** (Step 5)
| Conflict ID | Signal A | Signal B | Nature of conflict | Resolution |

**Diff table** (Step 6)
| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

Schema-commitment checkpoint: I commit to these column sets before Step 1.
I will not substitute prose for any table. I will not merge Step 4a and 4b.

---

## INERTIA-GATE TEMPLATE

The following block must be reproduced verbatim at each of the four
recurrence sites marked [INERTIA-GATE] in the steps below. Do not
abbreviate, paraphrase, or omit it. Its presence at each site is a
required output artifact.

  ┌────────────────────────────────────────────────────────────────────────┐
  │ INERTIA-GATE                                                           │
  │ The result of this step may leave this section unchanged.              │
  │ Inertia is a co-equal option. The burden of proof rests on change.     │
  │                                                                        │
  │ This block is reproduced verbatim at Steps 4, 4b, 6, and 7.           │
  │ Its presence is required at each site.                                 │
  └────────────────────────────────────────────────────────────────────────┘

---

## Step 1 — Read strategy.md and extract assumptions

Read `simulations/TOPICS.md` to locate the strategy file path. Read
strategy.md. Record its last-modified date as the STRATEGY DATE.

Extract stated dimensions. Then as the person responsible for delta
detection, scan: scope of coverage / sequencing / completion criteria /
success thresholds.
Apply Rule 2 before populating each Implicit evidence cell.

| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

Null (Rule 3, type-labeled): "ASSUMPTIONS: none — no implicit assumptions
identified; all strategy elements are explicitly stated."
Do not omit this declaration.

---

## Step 2 — Pre-signal Defense Register

Complete and output before reading any NEW artifact.

| Defense ID | Strategic decision | Strongest keep-it argument | What would invalidate |
| D-01 | [element] | [argument] | [signal pattern that would justify removal] |

---

## Step 3 — Signal inventory

Anti-pattern checkpoint: "An inventory tells me what exists. A delta tells
me what changed. I will not conflate them."

List every artifact in `simulations/` matching the topic slug. Classify NEW
(date > STRATEGY DATE) or PRIOR. All 9 namespaces must be explicitly
assessed: scout / draft / review / flow / trace / prove / listen / program /
topic.

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**SIGNAL READ-LOCK**: After this table is complete, signal files may not be
re-read for the remainder of execution. All subsequent steps work from the
written inventory above.

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

[INERTIA-GATE] — Reproduce the INERTIA-GATE block verbatim here before
writing any proposal row.

A proposal that cannot name a concrete consequence of deferral (the "If
unchanged" column) is a preference, not a decision — structurally invalid,
not merely incomplete.

---

## Step 4a — Additions

Schema-commitment checkpoint: I am about to produce the Additions table
with columns: # / Dimension / Delta Finding [Rule 4] / Evidence / Before /
After / Confidence / If unchanged / Reversibility [Rule 1] / Inertia
Rejected Because [REQUIRED].

The following columns are mandatory. Do not omit any column.
"Inertia Rejected Because [REQUIRED]": one sentence per row naming the
specific evidence or logic defeating the keep-unchanged option (Rule 5).
PASS: specific signal evidence named — FAIL: "compelling reason"

| # | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

Null (Rule 3, type-labeled): "ADDITIONS: none — inertia holds for all
candidate additions. Do not omit this declaration."

---

## Step 4b — Removals and Reprioritizations

[INERTIA-GATE] — Reproduce the INERTIA-GATE block verbatim here before
writing any row.

Schema-commitment checkpoint: I am about to produce the Removals and
Reprioritizations table with columns: # / Action [Rule 1] / Dimension /
Delta Finding [Rule 4] / Evidence / Before / After / Confidence / If
unchanged / Reversibility [Rule 1] / Inertia Rejected Because [REQUIRED].

The following columns are mandatory. Do not omit any column.
"Inertia Rejected Because [REQUIRED]": identical schema to Step 4a per
Rule 5. One sentence per row naming the specific evidence or logic defeating
the keep-unchanged option. PASS: specific signal evidence named —
FAIL: "compelling reason" or any prose substitute.

| # | Action [Rule 1] | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

Null declarations (Rule 3, type-labeled — each type independently declared):
  "REMOVALS: none — inertia holds. Do not omit this declaration."
  "REPRIORITIZATIONS: none — inertia holds. Do not omit this declaration."

---

## Step 4c — Defender Challenge Table

A table where every challenge is Weak is a structural signal of rubber-stamp
processing, not genuine evaluation.

Schema-commitment checkpoint: I am about to produce the Defender Challenge
Table with columns: Defense ID / Proposal # / Strategic decision defended /
Defensive argument / Defense basis / Challenge strength [Rule 1].

Defense basis: cite D-ID if pre-registered; write "Newly constructed" if
built after signal reading.

The following columns are mandatory. Do not omit any column.

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

The following columns are mandatory. Do not omit any column: Conflict ID /
Signal A / Signal B / Nature of conflict / Resolution.

Null (Rule 3, type-labeled): "CONFLICT AUDIT: none — no contradictions
detected between NEW artifacts on the same strategy dimension."
Do not omit this declaration.

---

## Step 6 — Before/after diff

[INERTIA-GATE] — Reproduce the INERTIA-GATE block verbatim here before
producing the diff table.

Schema-commitment checkpoint: I am about to produce the diff table with
columns: Dimension / Before / After [evidence bracket] / Proposal [cross-ref].

Include inline evidence brackets adjacent to each After value. Include
Proposal column cross-references (e.g., "ADD-1") for each row.

The following columns are mandatory. Do not omit any column.

| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

---

## Step 7 — Confirmation gate

[INERTIA-GATE] — Reproduce the INERTIA-GATE block verbatim here before
presenting any output. NO is a complete and valid outcome.

Display Step 3b delta findings / Step 4a additions / Step 4b removals and
reprioritizations / Step 4c Defender Challenge Table (with calibration
check) / Step 6 diff.

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

## Variation Summary

| Variation | Axis | C-62 | C-63 | C-64 | Hypothesis target |
|-----------|------|------|------|------|-------------------|
| V-01 | Inertia framing | YES | no | no | Manifest in block definition changes compliance on 4th site |
| V-02 | Output format | no | no | YES | Symmetric split tables close asymmetric justification bypass |
| V-03 | Phrasing register | no | YES | no | Type labels on nulls reduce ambiguity vs unlabeled coverage |
| V-04 | Combination | YES | YES | no | C-62 + C-63 compose cleanly; gap for C-64 visible as discriminating case |
| V-05 | Full combination | YES | YES | YES | All three criteria satisfied; tests whether ceiling is achievable in one prompt |

**Predicted structural risk (descending)**: V-05 > V-02 > V-04 > V-01 > V-03

V-05 and V-02 carry the highest structural complexity (split tables +
symmetric column schemas). V-04 inherits V-01 and V-03's complexity without
the split-table jump. V-01 is a single-block edit. V-03 is purely a phrasing
change with no schema modifications.

**Expected C-64 discriminating pair**: V-02 (passes) vs V-04 (fails).
V-04 has manifest and type-labeled nulls but a single proposals table — the
inertia-rejection justification column is nominally present for all rows but
not structurally enforced per change type. This is the gap C-64 is designed
to detect.
