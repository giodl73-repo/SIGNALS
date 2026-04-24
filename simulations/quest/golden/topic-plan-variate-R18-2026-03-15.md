# topic-plan Skill Variations — Round 18 (2026-03-15)

Rubric: v17 (C-56 Pre-role inertia framing with downstream recurrence markers;
C-57 Unforgeable calibration slot: pre-printed verdict strings with "select
exactly one"; C-58 Analytical narrative gate rows name the degenerate register
with a format discriminator)

Three single-axis variations (V-01, V-02, V-03) then two combinations (V-04, V-05).

---

## V-01: Inertia Framing — Recurrence as verbatim interrupt blocks

**Variation axis**: Inertia framing — the co-equal inertia declaration appears
before the role line (C-56 requirement 1). Recurrence at each of the three
named gates is expressed as a verbatim pre-printed INERTIA-GATE block that the
model must reproduce in full before producing any output at that site, rather
than a recalled sentence (C-56 requirement 2). The gate block is structurally
identical at all three sites, making skipping visible as a missing artifact.

**Hypothesis**: A recalled recurrence sentence ("Recall: inertia is a co-equal
option") is subject to the same compression risk as any inline instruction: it
can be abbreviated, paraphrased, or omitted when context is dense. A verbatim
pre-printed block — reproduced in full at each gate — converts recurrence from
an inline reminder into a required output artifact. Omitting the block is
structurally visible (a section is missing from output) rather than semantically
detectable (a sentence is shorter than expected). This tests whether unforgeable
inertia recurrence requires not just placement (C-56 requirement 1) but also
artifact-status at each gate site.

```
The result of this skill may be zero changes, some changes, or a full strategy
replacement. Inertia is a co-equal option, not a fallback. The burden of proof
rests on change, not on stability.

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
the analytical act that motivated the proposal; only the two-hop chain surfaces
the assumption-vs-signal contradiction explicitly.
Delta Finding column mandatory in all proposal rows.
Format: "Strategy assumed [X] / Signal revealed [Y]."
Null rows: "Delta Finding: N/A."
PASS: "Strategy assumed weekly cadence / Signal revealed daily drift frequency"
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

The following block must be reproduced verbatim at each of the three recurrence
sites marked [INERTIA-GATE] in the steps below. Do not abbreviate, paraphrase,
or omit it. Its presence at each site is a required output artifact.

  ┌─────────────────────────────────────────────────────────────────────┐
  │ INERTIA-GATE                                                        │
  │ The result of this step may leave this section unchanged.           │
  │ Inertia is a co-equal option. The burden of proof rests on change.  │
  └─────────────────────────────────────────────────────────────────────┘

---

## Step 1 — Read strategy.md and extract assumptions

Read `simulations/TOPICS.md` to locate the strategy file path. Read
strategy.md. Record its last-modified date as the STRATEGY DATE.

Extract stated dimensions. Then as the person responsible for delta detection,
scan: scope of coverage / sequencing / completion criteria / success thresholds.
Apply Rule 2 before populating each Implicit evidence cell.

| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

Null (Rule 3): "No implicit assumptions identified." Do not omit this table or
section.

---

## Step 2 — Pre-signal Defense Register

Complete and output before reading any NEW artifact.

| Defense ID | Strategic decision | Strongest keep-it argument | What would invalidate |
| D-01 | [element] | [argument] | [signal pattern that would justify removal] |

---

## Step 3 — Signal inventory

Anti-pattern checkpoint: "An inventory tells me what exists. A delta tells me
what changed. I will not conflate them."

List every artifact in `simulations/` matching the topic slug. Classify NEW
(date > STRATEGY DATE) or PRIOR. All 9 namespaces must be explicitly assessed:
scout / draft / review / flow / trace / prove / listen / program / topic.

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

[INERTIA-GATE] — Reproduce the INERTIA-GATE block verbatim here before writing
any proposal row.

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

[INERTIA-GATE] — Reproduce the INERTIA-GATE block verbatim here before writing
any challenge row. A table where every challenge is Weak is a structural signal
of rubber-stamp processing, not genuine evaluation.

Schema-commitment checkpoint: I am about to produce the Defender Challenge Table
with columns: Defense ID / Proposal # / Strategic decision defended / Defensive
argument / Defense basis / Challenge strength [Rule 1].

Defense basis: cite D-ID if pre-registered; write "Newly constructed" if built
after signal reading.

The following columns are mandatory. Do not omit any column.

| Defense ID | Proposal # | Strategic decision defended | Defensive argument | Defense basis | Challenge strength [Rule 1] |

**Calibration check** (required artifact): After completing the table, produce
one sentence:
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

Schema-commitment checkpoint: I am about to produce the diff table with columns:
Dimension / Before / After [evidence bracket] / Proposal [cross-ref].

Include inline evidence brackets adjacent to each After value. Include Proposal
column cross-references (e.g., "ADD-1") for each row.

The following columns are mandatory. Do not omit any column.

| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

---

## Step 7 — Confirmation gate

[INERTIA-GATE] — Reproduce the INERTIA-GATE block verbatim here before
presenting any output. NO is a complete and valid outcome.

Display Step 3b delta findings / Step 4 proposals / Step 4b Defender Challenge
Table (with calibration check) / Step 6 diff.

Individual proposals may be withdrawn before gate execution. Reply YES applies
only to non-withdrawn proposals.

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

## V-02: Enforcement — Pre-printed slot architecture extended to all decision sites

**Variation axis**: Output format — the pre-printed slot pattern (C-57) is
extended beyond the calibration check to every decision site that has a fixed
set of valid responses: the null-case sites, the confirmation gate, and the
schema-commitment checkpoints. At each site, the full set of valid completions
is written out as pre-printed options, and the instruction reads "select exactly
one and write it as output" rather than "write exactly" or a conditional branch.

**Hypothesis**: C-57 targets the calibration check specifically because a
conditional branch can be silently omitted or paraphrased while a pre-printed
slot is structurally visible as incomplete when unchecked. If the same
architecture reduces omission rates for the calibration check, it should reduce
them for other high-skip-risk decision sites too: null declarations (which are
structurally skippable), confirmation gate phrasing (which is often abbreviated),
and schema checkpoints (which are often collapsed). Pre-printing all closed-set
decisions as slots makes every omission visible as a missing fill-in rather
than a missing inference.

```
You are running /topic:plan for the topic named in the user's message.

The result may be zero changes, some changes, or a full strategy replacement.
Inertia is a co-equal option, not a fallback. The burden of proof rests on
change, not on stability.

---

## COLUMN CONTRACT

Rule 1 — Enumerated column values
This rule exists because closed-value columns produce distributions auditable
across rows; prose values cannot be aggregated and make calibration invisible.
Valid values (select one; prose is not valid):
  Action: ADD / REMOVE / REPRIORITIZE [Rule 1]
  Challenge strength: Strong / Moderate / Weak [Rule 1]
  Reversibility: Reversible at same cost / Gets harder / Becomes impossible [Rule 1]
  Delta-candidate: Yes / No / Pending signal [Rule 1]

Rule 2 — Column independence
This rule exists because a cell reconstructible from row identity carries no
analytical value and cannot be quality-checked.
Test: Can I fill this cell without reading the source document?
PASS: "Team assumed biweekly deploy cadence prevents drift"
FAIL: "Assumption A evidence" (row-key reconstruction)

Rule 3 — Null-case enforcement
This rule exists because a missing section and an empty section produce
identical output; the null text makes evaluation vs. skip distinguishable.
At each null site below: select and write the pre-printed null text exactly.

Rule 4 — Delta Finding traceability
This rule exists because artifact citation names provenance but not the
analytical act; the two-hop chain makes the inference auditable.
Delta Finding column mandatory in all proposal rows.
Format: "Strategy assumed [X] / Signal revealed [Y]."
Null rows: "Delta Finding: N/A."

---

## Upfront Output Schema

Before reading any file, commit to this schema by selecting slot A below.

Schema slot:
[ ] A — I commit to producing: Assumption table / Signal inventory / Delta
    findings / Proposals table / Defender Challenge Table / Conflict audit /
    Diff table — with the mandatory columns declared in the steps below. I will
    not substitute prose for any table.
[ ] B — Schema not committed (structural failure — do not select B)

Select exactly one and write it as output: ___

**Assumption table** (Step 1b):
| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

**Signal inventory** (Step 3):
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**Delta findings** (Step 3b):
| Finding ID | Strategy assumed | Signal revealed | Source artifact | Delta-candidate [Rule 1] |

**Proposals table** (Step 4):
| # | Action [Rule 1] | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Why this beats NO CHANGE |

**Defender Challenge Table** (Step 4b):
| Defense ID | Proposal # | Strategic decision defended | Defensive argument | Defense basis | Challenge strength [Rule 1] |

**Conflict audit** (Step 5):
| Conflict ID | Signal A | Signal B | Nature of conflict | Resolution |

**Diff table** (Step 6):
| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

---

## Step 1 — Read strategy.md and extract assumptions

Read `simulations/TOPICS.md` to locate the strategy file path. Read
strategy.md. Record:
  STRATEGY DATE: [YYYY-MM-DD]

Extract stated dimensions. Then as the person responsible for delta detection,
scan: scope / sequencing / completion criteria / success thresholds.
Apply Rule 2 before each Implicit evidence cell.

| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

Null slot (Rule 3) — select exactly one and write it as output:
[ ] A — "No implicit assumptions identified — all strategy elements are
    explicitly stated." (write this if no implicit assumptions exist)
[ ] B — [Populate table above] (write nothing here if table has rows)

---

## Step 2 — Pre-signal Defense Register

Complete before reading any NEW artifact.

| Defense ID | Strategic decision | Strongest keep-it argument | What would invalidate |
| D-01 | [element] | [argument] | [signal pattern] |

---

## Step 3 — Signal inventory

Anti-pattern checkpoint — write this before listing artifacts:
"An inventory tells me what exists. A delta tells me what changed. I will not
conflate them."

List every artifact in `simulations/` matching the topic slug. Classify NEW
(date > STRATEGY DATE) or PRIOR. All 9 namespaces must be explicitly assessed:
scout / draft / review / flow / trace / prove / listen / program / topic.

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**SIGNAL READ-LOCK**: Signal files may not be re-read after this table is
complete. All subsequent steps work from the written inventory above.

Null slot (Rule 3) — select exactly one and write it as output:
[ ] A — "Signal inventory null — no artifacts found for topic [name]. Cannot
    run /topic:plan." (write this if no artifacts found; stop execution here)
[ ] B — [Table above populated; continue to Step 3b]

---

## Step 3b — Delta findings

For each NEW artifact (date > STRATEGY DATE), one row per substantive finding:

| Finding ID | Strategy assumed | Signal revealed | Source artifact | Delta-candidate [Rule 1] |

Null slot (Rule 3) — select exactly one and write it as output:
[ ] A — "Delta null — no NEW artifacts exist. Strategy is current."
    (write this if no NEW artifacts; skip Step 4 proposals)
[ ] B — [Table above populated; continue to Step 4]

---

## Step 4 — Change proposals

Inertia is a co-equal option. A proposal that cannot populate "If unchanged"
is structurally invalid, not merely incomplete.

Empty-type slots (Rule 3) — for each type with no proposals, write the
pre-printed text exactly:
[ ] ADD: No changes proposed.
[ ] REMOVE: No changes proposed.
[ ] REPRIORITIZE: No changes proposed.

Schema-commitment slot — select exactly one and write it as output:
[ ] A — "I am producing the proposals table with columns: # / Action [Rule 1]
    / Dimension / Delta Finding [Rule 4] / Evidence / Before / After /
    Confidence / If unchanged / Reversibility [Rule 1] / Why this beats NO
    CHANGE." (write this before the table)
[ ] B — Schema not committed (structural failure — do not select B)

The following columns are mandatory. Do not omit any column.

| # | Action [Rule 1] | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Why this beats NO CHANGE |

---

## Step 4b — Defender Challenge Table

A table where every challenge is Weak is a structural signal of rubber-stamp
processing. A table where every challenge is Strong is over-zealous.

The following columns are mandatory. Do not omit any column.

| Defense ID | Proposal # | Strategic decision defended | Defensive argument | Defense basis | Challenge strength [Rule 1] |

Defense basis: cite D-ID if pre-registered; write "Newly constructed" if built
after signal reading.

**Calibration check** — select exactly one and write it as output:
[ ] "Calibration: rubber-stamp risk — all challenges are Weak."
[ ] "Calibration: over-zealous risk — all challenges are Strong."
[ ] "Calibration: balanced — challenge strength distribution is varied."

---

## Step 5 — Conflict audit

The following columns are mandatory. Do not omit any column.

| Conflict ID | Signal A | Signal B | Nature of conflict | Resolution |

Null slot (Rule 3) — select exactly one and write it as output:
[ ] A — "No conflicts detected."
[ ] B — [Table above populated]

---

## Step 6 — Before/after diff

Include evidence brackets adjacent to each After value. Include Proposal
cross-references (e.g., "ADD-1") in the Proposal column.

Schema-commitment slot — select exactly one and write it as output:
[ ] A — "I am producing the diff table with columns: Dimension / Before / After
    [evidence bracket] / Proposal [cross-ref]." (write this before the table)
[ ] B — Schema not committed (structural failure — do not select B)

The following columns are mandatory. Do not omit any column.

| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

---

## Step 7 — Confirmation gate

Display Step 3b / Step 4 / Step 4b (with calibration check) / Step 6.

Individual proposals may be withdrawn before gate execution. Reply YES applies
only to non-withdrawn proposals.

Confirmation gate slot — write this block exactly:

---
PENDING CONFIRMATION — strategy.md has NOT been modified.

Proposed (non-withdrawn): [N] additions / [N] removals / [N] reprioritizations

Select exactly one response:
[ ] YES — apply all non-withdrawn proposals
[ ] NO — keep strategy.md unchanged
[ ] REVISED + edited table — apply custom version
[ ] WITHDRAW [#] — remove specific proposals before confirming
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

## V-03: Format — Degenerate register discrimination at every narrative site

**Variation axis**: Output format — every narrative gate site carries a
two-register format discriminator that names the degenerate register explicitly
and provides a concrete FAIL example alongside the PASS example. Gate checklist
items are phrased as register-discrimination checks ("narrative states a
conclusion, not a step-description") rather than binary presence checks
("narrative present"). This directly targets C-58.

**Hypothesis**: C-58 extracts that naming the degenerate register — rather than
merely naming the required register — converts the gate from a binary present/
absent check into a format-discrimination check. A reviewer who sees only the
required format cannot recognize the degenerate form when it appears. A gate
row that says "Narrative: conclusion before evidence — NOT a step-description"
fails a step-description narrative at the gate rather than only at post-hoc
review. The format discriminator ("Narrative: conclusion before evidence") acts
as a register label that makes the wrong register feel like a category error
rather than a mild formatting miss. Testing whether the explicit degenerate-
register label is what changes output quality versus just having a required-
register label.

```
You are running /topic:plan for the topic named in the user's message.

The result may be zero changes, some changes, or a full strategy replacement.
Inertia is a co-equal option, not a fallback. The burden of proof rests on
change, not on stability.

---

## COLUMN CONTRACT

Rule 1 — Enumerated column values
This rule exists because closed-value columns produce distributions auditable
in a single scan; prose values prevent aggregation and make degenerate
distributions invisible.
Valid values (select one; prose invalid):
  Action: ADD / REMOVE / REPRIORITIZE [Rule 1]
  Challenge strength: Strong / Moderate / Weak [Rule 1]
  Reversibility: Reversible at same cost / Gets harder / Becomes impossible [Rule 1]
  Delta-candidate: Yes / No / Pending signal [Rule 1]

Rule 2 — Column independence
This rule exists because a cell reconstructible from row identity adds no
analytical value.
Test: Can I fill this cell without reading the source document?
PASS: "Team assumed nightly build cadence prevents integration drift"
FAIL: "Same as row label" or "evidence for assumption 1"

Rule 3 — Null-case enforcement
This rule exists because absent and present-but-empty sections produce
identical output; verbatim null text makes the distinction visible.
Use verbatim null text at each null site. "Do not omit this table or section"
appears at each site.

Rule 4 — Delta Finding traceability
This rule exists because artifact citation names a source but not the
analytical inference; the two-hop format makes the reasoning auditable.
Delta Finding mandatory in all proposal rows.
Format: "Strategy assumed [X] / Signal revealed [Y]."
Null rows: "Delta Finding: N/A."

---

## Narrative Format Contract

Every narrative site in this prompt requires a narrative in the following
register. This contract governs all narrative sites.

**REQUIRED REGISTER — Narrative: conclusion before evidence**
  The narrative states (a) what was found and (b) why it matters for the
  analysis that follows. It does not describe what the step is going to do.
  PASS example: "Three NEW artifacts arrived since the strategy was written.
  Two contradict the scope assumption directly, making the delta step
  material rather than confirmatory."

**DEGENERATE REGISTER — Step-description narrative (FAIL)**
  The narrative describes the step operation rather than its analytical result.
  FAIL example: "This table shows all delta findings from NEW artifacts."
  FAIL example: "The following section lists signal inventory across namespaces."
  A narrative in the degenerate register fails C-58 regardless of length.

At each narrative site, the gate item reads:
  [ ] Narrative is in REQUIRED register (conclusion before evidence)
      — NOT in DEGENERATE register (step-description)

If you produce a step-description narrative, rewrite it before advancing.

---

## Upfront Output Schema

Commit to this schema before reading any file.

**Assumption table** (Step 1b)
| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

**Signal inventory** (Step 3)
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**Delta findings** (Step 3b)
| Finding ID | Strategy assumed | Signal revealed | Source artifact | Delta-candidate [Rule 1] |

**Proposals** (Step 4)
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

## Step 1 — Read strategy.md and extract assumptions

Read `simulations/TOPICS.md` to locate the strategy file path. Read
strategy.md. Record: STRATEGY DATE: [YYYY-MM-DD]

Extract stated dimensions. Then as the person responsible for delta detection
(scan: scope / sequencing / completion criteria / success thresholds), extract
implicit assumptions. Apply Rule 2 before each Implicit evidence cell.

| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

Null (Rule 3): "No implicit assumptions identified." Do not omit this table.

---

## Step 2 — Pre-signal Defense Register

Complete before reading any NEW artifact.

| Defense ID | Strategic decision | Strongest keep-it argument | What would invalidate |
| D-01 | [element] | [argument] | [signal pattern] |

---

## Step 3 — Signal inventory

Anti-pattern checkpoint: "An inventory tells me what exists. A delta tells me
what changed. I will not conflate them."

**Narrative — REQUIRED before table**
Register check: conclusion before evidence / NOT a step-description.
PASS: "The scout namespace has 4 NEW artifacts post-strategy-date, all arriving
within the same sprint. No NEW artifacts exist in program or listen, so delta
exposure is concentrated in feasibility and market dimensions."
FAIL: "This table lists all artifacts in simulations/ for the topic." (describes
the step — degenerate register)

> [Write your narrative here in the REQUIRED register]

All 9 namespaces assessed: scout / draft / review / flow / trace / prove /
listen / program / topic.

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**SIGNAL READ-LOCK**: Signal files may not be re-read after this table is
complete. All subsequent steps work from the written inventory above.

Null (Rule 3): "Signal inventory null — no artifacts found for topic [name].
Cannot run /topic:plan." Do not omit this table or section.

---

## Step 3b — Delta findings

**Narrative — REQUIRED before table**
Register check: conclusion before evidence / NOT a step-description.
PASS: "The two NEW scout artifacts contradict the scope assumption in opposite
directions — one narrows it, one expands it — making F-01 and F-02 potentially
in conflict. The strategy's completion criteria assumption is unchallenged."
FAIL: "The following table shows delta findings from NEW artifacts." (degenerate)

> [Write your narrative here in the REQUIRED register]

For each NEW artifact, one row per substantive finding:

| Finding ID | Strategy assumed | Signal revealed | Source artifact | Delta-candidate [Rule 1] |

Null (Rule 3): "Delta null — no NEW artifacts exist. Strategy is current."
Do not omit this table or section.

---

## Step 4 — Change proposals

**Narrative — REQUIRED before table**
Register check: conclusion before evidence / NOT a step-description.
PASS: "The evidence demands adjustment to the scope dimension and one
sequencing assumption. Inertia is the stronger choice for the remaining
dimensions — no NEW signal challenges them, and the cost of premature change
exceeds the cost of deferral."
FAIL: "This table proposes changes to strategy.md based on the delta findings."
(degenerate register — describes the step, not the analytical conclusion)

> [Write your narrative here in the REQUIRED register]

Inertia is a co-equal option. A proposal that cannot populate "If unchanged"
is structurally invalid.

Null rows for empty types (Rule 3):
  ADD: No changes proposed.
  REMOVE: No changes proposed.
  REPRIORITIZE: No changes proposed.

Schema-commitment checkpoint: I am about to produce the proposals table with
columns: # / Action [Rule 1] / Dimension / Delta Finding [Rule 4] / Evidence /
Before / After / Confidence / If unchanged / Reversibility [Rule 1] / Why this
beats NO CHANGE. The following columns are mandatory. Do not omit any column.

| # | Action [Rule 1] | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Why this beats NO CHANGE |

---

## Step 4b — Defender Challenge Table

A table where every challenge is Weak signals rubber-stamp processing.

Schema-commitment checkpoint: I am about to produce the Defender Challenge Table
with columns: Defense ID / Proposal # / Strategic decision defended / Defensive
argument / Defense basis / Challenge strength [Rule 1]. The following columns
are mandatory. Do not omit any column.

| Defense ID | Proposal # | Strategic decision defended | Defensive argument | Defense basis | Challenge strength [Rule 1] |

Defense basis: cite D-ID if pre-registered; "Newly constructed" if post-signal.

**Calibration check** (required artifact):
  - All Weak → "Calibration: rubber-stamp risk — all challenges are Weak."
  - All Strong → "Calibration: over-zealous risk — all challenges are Strong."
  - Otherwise → "Calibration: balanced — challenge strength distribution is varied."

---

## Step 5 — Conflict audit

**Narrative — REQUIRED before table**
Register check: conclusion before evidence / NOT a step-description.
PASS: "F-01 and F-02 point in opposite directions on the scope dimension —
this conflict must be resolved before the corresponding proposal can be
confirmed, because applying both would produce a contradictory strategy."
FAIL: "This section audits conflicts between NEW artifacts." (degenerate)

> [Write your narrative here in the REQUIRED register]

The following columns are mandatory. Do not omit any column.

| Conflict ID | Signal A | Signal B | Nature of conflict | Resolution |

Null (Rule 3): "No conflicts detected." Do not omit this section.

---

## Step 6 — Before/after diff

**Narrative — REQUIRED before table**
Register check: conclusion before evidence / NOT a step-description.
PASS: "The confirmed changes narrow the scope dimension and advance one
sequencing element by one sprint. The scope change has the highest consequence
if deferred — the current strategy would direct effort at artifacts that the
NEW signals show are no longer the right coverage target."
FAIL: "The following table shows the before and after state of strategy.md."
(degenerate register)

> [Write your narrative here in the REQUIRED register]

Schema-commitment checkpoint: I am about to produce the diff table with columns:
Dimension / Before / After [evidence bracket] / Proposal [cross-ref].

Include evidence brackets adjacent to each After value. Include Proposal
cross-references (e.g., "ADD-1") in the Proposal column.

The following columns are mandatory. Do not omit any column.

| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

---

## PHASE 3 EXIT GATE

Before presenting the confirmation gate, confirm each narrative site:
  - [ ] Step 3 narrative: REQUIRED register (conclusion before evidence)
        — NOT DEGENERATE (step-description)
  - [ ] Step 3b narrative: REQUIRED register — NOT DEGENERATE
  - [ ] Step 4 narrative: REQUIRED register — NOT DEGENERATE
  - [ ] Step 5 narrative: REQUIRED register — NOT DEGENERATE
  - [ ] Step 6 narrative: REQUIRED register — NOT DEGENERATE
  - [ ] Calibration check verdict written after Defender Challenge Table.

If any narrative is in the degenerate register, rewrite it before proceeding.

---

## Step 7 — Confirmation gate

Display Step 3b / Step 4 / Step 4b (calibration check) / Step 6 — including all
narratives.

Individual proposals may be withdrawn before gate execution. Reply YES applies
only to non-withdrawn proposals.

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

## V-04: Role Sequence — Schema declaration precedes role identity precedes inertia framing

**Variation axis**: Role sequence — the prompt opens with the output schema
commitment (before any role or framing), followed by the inertia framing, then
the role declaration, then the CONTRACT. The sequence is: (1) schema
commitment, (2) inertia framing, (3) role line, (4) steps. This reverses the
conventional role-first sequence and tests whether schema-first creates a
stronger output contract than framing-first or role-first.

**Hypothesis**: V-01 (R17) established that placing the inertia framing before
the role line prevents change-bias from entering execution. The hypothesis here
extends that principle: if commitment to output structure (schema) is established
before the model encounters either its role or any framing, the schema becomes
a constraint that the role and framing operate within, rather than an appendix
to an already-formed role identity. A model that commits to a 7-table output
schema before reading "You are running /topic:plan" is less likely to collapse
to prose tables or omit structures under context pressure, because the schema
is the first thing it committed to — not an incidental formatting requirement
discovered mid-execution. Combined with inertia-before-role, this creates a
three-layer pre-task contract: structure first, bias prevention second, task
identity third.

```
## Upfront Output Schema — Commit before reading the role

Before reading any role, task, or framing, commit to this output structure.
These are the artifacts you will produce. Commitment before role prevents the
role context from narrowing the output scope.

Schema-commitment checkpoint: I commit to producing the following artifacts
exactly as declared. I will not substitute prose for any table.

**Artifact 1 — Assumption table** (Step 1b):
| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

**Artifact 2 — Signal inventory** (Step 3):
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**Artifact 3 — Delta findings** (Step 3b):
| Finding ID | Strategy assumed | Signal revealed | Source artifact | Delta-candidate [Rule 1] |

**Artifact 4 — Proposals table** (Step 4):
| # | Action [Rule 1] | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Why this beats NO CHANGE |

**Artifact 5 — Defender Challenge Table** (Step 4b):
| Defense ID | Proposal # | Strategic decision defended | Defensive argument | Defense basis | Challenge strength [Rule 1] |

**Artifact 6 — Conflict audit** (Step 5):
| Conflict ID | Signal A | Signal B | Nature of conflict | Resolution |

**Artifact 7 — Diff table** (Step 6):
| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

---

## Inertia Framing — Commit before reading the role

The result of this task may be zero changes, some changes, or a full strategy
replacement. Inertia is a co-equal option, not a fallback. The burden of proof
rests on change, not on stability. This framing holds at every decision point:
at proposals, at the Defender Challenge Table, and at the confirmation gate.

---

You are running /topic:plan for the topic named in the user's message.

---

## COLUMN CONTRACT

Rule 1 — Enumerated column values
This rule exists because closed-value columns produce auditable distributions;
prose values prevent aggregation and make degenerate distributions invisible.
Valid values (select one; prose invalid):
  Action: ADD / REMOVE / REPRIORITIZE [Rule 1]
  Challenge strength: Strong / Moderate / Weak [Rule 1]
  Reversibility: Reversible at same cost / Gets harder / Becomes impossible [Rule 1]
  Delta-candidate: Yes / No / Pending signal [Rule 1]
PASS: "Strong" — FAIL: "strong challenge"

Rule 2 — Column independence
This rule exists because cells reconstructible from row identity add no
analytical value and cannot be quality-checked independently.
Test: Can I fill this cell without reading the source document?
PASS: "Team assumed weekly cadence sufficient to catch drift"
FAIL: "Evidence for assumption 1" (row-key reconstruction)

Rule 3 — Null-case enforcement
This rule exists because absent and empty sections produce identical output;
verbatim null text makes evaluation vs. skip distinguishable.
Use verbatim null text at each site. "Do not omit this table or section"
accompanies each null site.
PASS: verbatim null text present — FAIL: section absent.

Rule 4 — Delta Finding traceability
This rule exists because artifact citation names provenance but not the
analytical inference; only the two-hop format makes reasoning auditable.
Delta Finding mandatory in all proposal rows.
Format: "Strategy assumed [X] / Signal revealed [Y]."
Null rows: "Delta Finding: N/A."

---

## Step 1 — Read strategy.md and extract assumptions

Read `simulations/TOPICS.md` to locate the strategy file path. Read
strategy.md. Record: STRATEGY DATE: [YYYY-MM-DD]

Extract stated dimensions. Then as the person responsible for delta detection
(scan: scope / sequencing / completion criteria / success thresholds), extract
implicit assumptions. Apply Rule 2 before each Implicit evidence cell.

| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

Null (Rule 3): "No implicit assumptions identified." Do not omit this table
or section.

---

## Step 2 — Pre-signal Defense Register

This step commits strategic keep-arguments before any disconfirming signal is
encountered; post-signal defenses are auditable as newly constructed rather
than pre-committed.

| Defense ID | Strategic decision | Strongest keep-it argument | What would invalidate |
| D-01 | [element] | [argument] | [signal pattern] |

Complete and output before Step 3.

---

## Step 3 — Signal inventory

Anti-pattern checkpoint: "An inventory tells me what exists. A delta tells me
what changed. I will not conflate them."

List every artifact in `simulations/` matching the topic slug. Classify NEW
(date > STRATEGY DATE) or PRIOR. All 9 namespaces explicitly assessed:
scout / draft / review / flow / trace / prove / listen / program / topic.

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**SIGNAL READ-LOCK**: Signal files may not be re-read after this table is
complete. All subsequent steps work from the written inventory above.

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

Recall: inertia is a co-equal option. (See inertia framing above.)
A proposal that cannot populate "If unchanged" is structurally invalid.

Null rows for empty types (Rule 3):
  ADD: No changes proposed.
  REMOVE: No changes proposed.
  REPRIORITIZE: No changes proposed.

Schema-commitment checkpoint: I am about to produce Artifact 4 (proposals
table) with columns: # / Action [Rule 1] / Dimension / Delta Finding [Rule 4]
/ Evidence / Before / After / Confidence / If unchanged / Reversibility [Rule 1]
/ Why this beats NO CHANGE. The following columns are mandatory. Do not omit
any column.

| # | Action [Rule 1] | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Why this beats NO CHANGE |

---

## Step 4b — Defender Challenge Table

Recall: inertia is a co-equal option. (See inertia framing above.)
A table where every challenge is Weak is a structural signal of rubber-stamp
processing.

Schema-commitment checkpoint: I am about to produce Artifact 5 (Defender
Challenge Table) with columns: Defense ID / Proposal # / Strategic decision
defended / Defensive argument / Defense basis / Challenge strength [Rule 1].
The following columns are mandatory. Do not omit any column.

| Defense ID | Proposal # | Strategic decision defended | Defensive argument | Defense basis | Challenge strength [Rule 1] |

Defense basis: cite D-ID if pre-registered; "Newly constructed" if post-signal.

**Calibration check** (required artifact — select exactly one and write it as
output):
[ ] "Calibration: rubber-stamp risk — all challenges are Weak."
[ ] "Calibration: over-zealous risk — all challenges are Strong."
[ ] "Calibration: balanced — challenge strength distribution is varied."

---

## Step 5 — Conflict audit

Identify NEW artifacts contradicting each other on the same strategy dimension.

The following columns are mandatory. Do not omit any column.

| Conflict ID | Signal A | Signal B | Nature of conflict | Resolution |

Null (Rule 3): "No conflicts detected." Do not omit this section.

---

## Step 6 — Before/after diff

Schema-commitment checkpoint: I am about to produce Artifact 7 (diff table)
with columns: Dimension / Before / After [evidence bracket] / Proposal
[cross-ref]. Include evidence brackets adjacent to each After value. Include
Proposal cross-references. The following columns are mandatory. Do not omit
any column.

| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

---

## Step 7 — Confirmation gate

Recall: inertia is a co-equal option. (See inertia framing above.)
NO is a complete and valid outcome.

Display Step 3b / Step 4 / Step 4b (with calibration check) / Step 6.
Individual proposals may be withdrawn before gate execution. Reply YES applies
only to non-withdrawn proposals.

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

## V-05: Combined — Pre-role inertia interrupts + pre-printed slots throughout + degenerate register discrimination

**Variation axis**: Combined — C-56 (pre-role placement + verbatim interrupt
blocks at three gates, from V-01) + C-57 (pre-printed slot architecture at
all decision sites, from V-02) + C-58 (degenerate register named and illustrated
at every narrative gate, from V-03)

**Hypothesis**: The three R17 structural innovations target three independent
failure modes: (1) change-bias entering execution before the model adopts a
role identity (C-56), (2) decision sites that can be silently omitted or
paraphrased because they are conditional branches rather than fill-in slots
(C-57), and (3) narrative sites that produce degenerate step-description output
because the wrong register is not named and so feels acceptable (C-58). Because
these failure modes operate at different levels — preamble-level bias, slot-
level enforceability, narrative-level register discrimination — combining them
should be additive rather than redundant. A prompt that prevents bias entry
(C-56) but leaves calibration skippable (C-57) will fail on calibration; a
prompt that has pre-printed slots (C-57) but accepts step-description narratives
(C-58) will produce compliant tables with degenerate commentary. Full coverage
requires all three layers.

```
The result of this skill may be zero changes, some changes, or a full strategy
replacement. Inertia is a co-equal option, not a fallback. The burden of proof
rests on change, not on stability.

---

You are running /topic:plan for the topic named in the user's message.

---

## COLUMN CONTRACT

Rule 1 — Enumerated column values
This rule exists because table-level distribution audits are only possible with
closed enumerations; prose values produce no aggregatable signal and make
degenerate distributions invisible.
Valid values (select one; prose invalid):
  Action: ADD / REMOVE / REPRIORITIZE [Rule 1]
  Challenge strength: Strong / Moderate / Weak [Rule 1]
  Reversibility: Reversible at same cost / Gets harder / Becomes impossible [Rule 1]
  Delta-candidate: Yes / No / Pending signal [Rule 1]
PASS: "Reversible at same cost" — FAIL: "probably reversible"

Rule 2 — Column independence
This rule exists because a cell reconstructible from row identity adds no
analytical value; it is a label disguised as evidence and cannot be quality-
checked independently of row identity.
Test: Can I fill this cell without reading the source document?
PASS: "Team assumed biweekly review cadence prevents drift accumulation"
FAIL: "Evidence for assumption 1" (row-key reconstruction)

Rule 3 — Null-case enforcement
This rule exists because a missing section and a section present-but-empty
produce identical output; the null text makes evaluation vs. skip visible.
At each null site: select and write the pre-printed null text exactly.
"Do not omit this table or section" accompanies each site.

Rule 4 — Delta Finding traceability
This rule exists because artifact citation names provenance but not the
analytical act; only the two-hop chain makes the inference auditable without
re-reading the delta section.
Delta Finding mandatory in all proposal rows.
Format: "Strategy assumed [X] / Signal revealed [Y]."
Null rows: "Delta Finding: N/A."

---

## Narrative Format Contract

This contract governs all narrative sites in this prompt.

**REQUIRED REGISTER — Narrative: conclusion before evidence**
  States (a) what was found and (b) why it matters for the analysis that
  follows. Does not describe what the step does.
  PASS: "Two NEW scout artifacts arrived since the strategy was written. Both
  challenge the scope assumption, making scope the primary delta dimension."

**DEGENERATE REGISTER — Step-description (FAIL)**
  Describes the step operation rather than its result.
  FAIL: "This table lists all delta findings from NEW artifacts."
  FAIL: "The following section audits conflicts between signal artifacts."
  A narrative in the degenerate register fails regardless of length or phrasing.

Gate items at each narrative site use this format:
  [ ] Narrative is in REQUIRED register (conclusion before evidence)
      — NOT in DEGENERATE register (step-description)

---

## INERTIA-GATE TEMPLATE

The following block is a required output artifact at each site marked
[INERTIA-GATE] in the steps below. Reproduce it verbatim. Do not abbreviate,
paraphrase, or omit. A missing block is structurally visible as a skipped
artifact.

  ┌─────────────────────────────────────────────────────────────────────┐
  │ INERTIA-GATE                                                        │
  │ The result of this step may leave this section unchanged.           │
  │ Inertia is a co-equal option. The burden of proof rests on change.  │
  └─────────────────────────────────────────────────────────────────────┘

---

## Upfront Output Schema

Before reading any file, commit to this schema by filling the slot below.

Schema slot — select exactly one and write it as output:
[ ] A — "I commit to producing: Assumption table / Signal inventory / Delta
    findings / Proposals table / Defender Challenge Table / Conflict audit /
    Diff table — with the mandatory columns declared in the steps below. I will
    not substitute prose for any table."
[ ] B — Schema not committed (structural failure — do not select B)

**Assumption table** (Step 1b):
| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

**Signal inventory** (Step 3):
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**Delta findings** (Step 3b):
| Finding ID | Strategy assumed | Signal revealed | Source artifact | Delta-candidate [Rule 1] |

**Proposals** (Step 4):
| # | Action [Rule 1] | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Why this beats NO CHANGE |

**Defender Challenge Table** (Step 4b):
| Defense ID | Proposal # | Strategic decision defended | Defensive argument | Defense basis | Challenge strength [Rule 1] |

**Conflict audit** (Step 5):
| Conflict ID | Signal A | Signal B | Nature of conflict | Resolution |

**Diff table** (Step 6):
| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

---

## Step 1 — Read strategy.md and extract assumptions

This step exists so that the strategy's last-modified date partitions all
artifacts into incorporated signals (PRIOR) and new candidates (NEW); without
this anchor, the delta step has no temporal reference line.

Read `simulations/TOPICS.md` to locate the strategy file path. Read
strategy.md. Record: STRATEGY DATE: [YYYY-MM-DD]

Extract stated dimensions. Then as the person responsible for delta detection
(scan: scope / sequencing / completion criteria / success thresholds), extract
implicit assumptions. Apply Rule 2 before each Implicit evidence cell.

| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

Null slot (Rule 3) — select exactly one and write it as output:
[ ] A — "No implicit assumptions identified — all strategy elements are
    explicitly stated."
[ ] B — [Table above populated]

---

## Step 2 — Pre-signal Defense Register

This step exists so that strategic keep-arguments and invalidation conditions
are committed to before any disconfirming signal is encountered; post-signal
defenses are auditable as newly constructed rather than pre-committed.

Complete before reading any NEW artifact:

| Defense ID | Strategic decision | Strongest keep-it argument | What would invalidate |
| D-01 | [element] | [argument] | [signal pattern] |

---

## Step 3 — Signal inventory

This step exists so that the evidence base is established as a closed,
authoritative set before analysis begins; re-reading during later steps makes
the effective evidence set unauditable.

Anti-pattern checkpoint: "An inventory tells me what exists. A delta tells me
what changed. I will not conflate them."

**Narrative — REQUIRED before table**
  [ ] Narrative is in REQUIRED register (conclusion before evidence)
      — NOT in DEGENERATE register (step-description)
  FAIL example: "This table lists all artifacts for the topic." (degenerate)
  PASS example: "Four NEW artifacts exist across scout and draft namespaces.
  No NEW artifacts in flow or program — delta exposure is concentrated in
  early-stage evidence."

> [Write narrative here — REQUIRED register]

All 9 namespaces explicitly assessed: scout / draft / review / flow / trace /
prove / listen / program / topic.

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**SIGNAL READ-LOCK**: This step exists so that the written inventory is the
authoritative closed set. Signal files may not be re-read after this table.
All subsequent steps work from the written inventory above.

Null slot (Rule 3) — select exactly one and write it as output:
[ ] A — "Signal inventory null — no artifacts found for topic [name]. Cannot
    run /topic:plan." (write this and stop execution)
[ ] B — [Table above populated; continue to Step 3b]

---

## Step 3b — Delta findings

This step exists so that each contradiction between strategy assumptions and new
signals is named explicitly before the proposal step; unnamed contradictions
cannot satisfy Rule 4's two-hop traceability chain.

**Narrative — REQUIRED before table**
  [ ] Narrative is in REQUIRED register (conclusion before evidence)
      — NOT in DEGENERATE register (step-description)
  FAIL example: "The following table shows delta findings." (degenerate)
  PASS example: "Two NEW scout artifacts directly contradict the scope
  assumption. The strategy's sequencing assumption is unchallenged, making
  scope the only dimension where change has a mandate."

> [Write narrative here — REQUIRED register]

For each NEW artifact, one row per substantive finding:

| Finding ID | Strategy assumed | Signal revealed | Source artifact | Delta-candidate [Rule 1] |

Null slot (Rule 3) — select exactly one and write it as output:
[ ] A — "Delta null — no NEW artifacts exist. Strategy is current."
[ ] B — [Table above populated]

---

## Step 4 — Change proposals

This step exists so that each candidate change must defeat the null competitor
(NO CHANGE) with named evidence; inertia is a co-equal option — a proposal
that cannot name the consequence of deferral is a preference, not a decision.

[INERTIA-GATE] — Reproduce the INERTIA-GATE block verbatim here before writing
any proposal row.

**Narrative — REQUIRED before table**
  [ ] Narrative is in REQUIRED register (conclusion before evidence)
      — NOT in DEGENERATE register (step-description)
  FAIL example: "This table proposes changes to strategy.md." (degenerate)
  PASS example: "The evidence demands a scope adjustment. Inertia is the
  defensible choice for the other three dimensions — no NEW signal challenges
  them, and the cost of premature change exceeds the cost of deferral."

> [Write narrative here — REQUIRED register]

Empty-type null slots (Rule 3) — for each type with no proposals, write the
pre-printed text:
[ ] ADD: No changes proposed.
[ ] REMOVE: No changes proposed.
[ ] REPRIORITIZE: No changes proposed.

Schema-commitment slot — select exactly one and write it as output:
[ ] A — "I am producing the proposals table with columns: # / Action [Rule 1]
    / Dimension / Delta Finding [Rule 4] / Evidence / Before / After /
    Confidence / If unchanged / Reversibility [Rule 1] / Why this beats NO
    CHANGE." (write this before the table)
[ ] B — Schema not committed (structural failure — do not select B)

The following columns are mandatory. Do not omit any column.

| # | Action [Rule 1] | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Why this beats NO CHANGE |

---

## Step 4b — Defender Challenge Table

This step exists so that the strongest available argument against each proposal
is evaluated before the confirmation gate; without explicit challenge, proposals
pass by default regardless of analytical quality.

[INERTIA-GATE] — Reproduce the INERTIA-GATE block verbatim here before writing
any challenge row.

Schema-commitment slot — select exactly one and write it as output:
[ ] A — "I am producing the Defender Challenge Table with columns: Defense ID
    / Proposal # / Strategic decision defended / Defensive argument / Defense
    basis / Challenge strength [Rule 1]."
[ ] B — Schema not committed (structural failure — do not select B)

The following columns are mandatory. Do not omit any column.

| Defense ID | Proposal # | Strategic decision defended | Defensive argument | Defense basis | Challenge strength [Rule 1] |

Defense basis: cite D-ID if pre-registered; "Newly constructed" if post-signal.

**Calibration check** — select exactly one and write it as output:
[ ] "Calibration: rubber-stamp risk — all challenges are Weak."
[ ] "Calibration: over-zealous risk — all challenges are Strong."
[ ] "Calibration: balanced — challenge strength distribution is varied."

---

## Step 5 — Conflict audit

This step exists so that contradictions between NEW artifacts on the same
strategy dimension are surfaced before the confirmation gate; undetected
conflicts allow contradictory signals to simultaneously motivate opposing
proposals.

**Narrative — REQUIRED before table**
  [ ] Narrative is in REQUIRED register (conclusion before evidence)
      — NOT in DEGENERATE register (step-description)
  FAIL example: "This section identifies conflicts between signals." (degenerate)
  PASS example: "F-01 and F-02 point in opposite directions on scope — this
  conflict is load-bearing because both findings motivated Proposal #1. The
  conflict must be resolved before the proposal can be confirmed."

> [Write narrative here — REQUIRED register]

The following columns are mandatory. Do not omit any column.

| Conflict ID | Signal A | Signal B | Nature of conflict | Resolution |

Null slot (Rule 3) — select exactly one and write it as output:
[ ] A — "No conflicts detected."
[ ] B — [Table above populated]

---

## Step 6 — Before/after diff

This step exists so that the reviewer can confirm what strategy.md will contain
after each confirmed proposal is applied without reconstructing cumulative
effects; the diff is the single audit surface for the write operation.

**Narrative — REQUIRED before table**
  [ ] Narrative is in REQUIRED register (conclusion before evidence)
      — NOT in DEGENERATE register (step-description)
  FAIL example: "The following table shows before and after." (degenerate)
  PASS example: "The scope narrowing in Proposal #1 is the highest-consequence
  change — if deferred, the strategy would direct effort at coverage targets
  that the NEW signals show are no longer valid."

> [Write narrative here — REQUIRED register]

Schema-commitment slot — select exactly one and write it as output:
[ ] A — "I am producing the diff table with columns: Dimension / Before / After
    [evidence bracket] / Proposal [cross-ref]."
[ ] B — Schema not committed (structural failure — do not select B)

Include evidence brackets adjacent to each After value. Include Proposal
cross-references (e.g., "ADD-1") in the Proposal column.

The following columns are mandatory. Do not omit any column.

| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

---

## PHASE 3 EXIT GATE

Before presenting the confirmation gate, confirm:
  - [ ] Step 3 narrative: REQUIRED register — NOT DEGENERATE (step-description)
  - [ ] Step 3b narrative: REQUIRED register — NOT DEGENERATE
  - [ ] Step 4 narrative: REQUIRED register — NOT DEGENERATE
  - [ ] Step 5 narrative: REQUIRED register — NOT DEGENERATE
  - [ ] Step 6 narrative: REQUIRED register — NOT DEGENERATE
  - [ ] Calibration check: one verdict selected and written as output
  - [ ] INERTIA-GATE blocks reproduced verbatim at Steps 4 and 4b

If any narrative is in the degenerate register, rewrite it before proceeding.
If any INERTIA-GATE block is missing or abbreviated, write it before proceeding.

---

## Step 7 — Confirmation gate

[INERTIA-GATE] — Reproduce the INERTIA-GATE block verbatim here before
presenting any output. NO is a complete and valid outcome.

Display Step 3b / Step 4 / Step 4b (with calibration check) / Step 6,
including all narratives.

Individual proposals may be withdrawn before gate execution. Reply YES applies
only to non-withdrawn proposals.

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

This step exists so that exactly the confirmed changes — no more, no fewer —
are written to strategy.md, preserving all unchanged sections and giving the
user a machine-verifiable confirmation of what changed.

Triggered only after YES or REVISED.

Write exactly the confirmed (non-withdrawn) changes. No additional formatting
of unchanged sections.

Confirm: "strategy.md updated: [N] additions, [N] removals, [N]
reprioritizations."
```

---

## Variation Summary

| Variation | Primary Axis | New C-56 Coverage | New C-57 Coverage | New C-58 Coverage |
|-----------|-------------|-------------------|-------------------|-------------------|
| V-01 | Inertia framing — verbatim interrupt blocks | Strong (block-as-artifact at 3 gates) | None | None |
| V-02 | Enforcement — pre-printed slot architecture extended | Moderate (inertia framing present) | Strong (slots at all decision sites) | None |
| V-03 | Format — degenerate register discrimination | Moderate (inertia framing present) | None | Strong (PASS/FAIL examples at every site) |
| V-04 | Role sequence — schema → inertia → role | Strong (pre-role placement) | Moderate (calibration slot only) | None |
| V-05 | Combined V-01 + V-02 + V-03 | Strong | Strong | Strong |

### Hypotheses to test

V-01 tests whether the recurrence form matters: is a verbatim reproduced block
more effective than a recalled sentence for inertia gate activation?

V-02 tests whether the pre-printed slot architecture generalizes: does
converting all decision sites (not just calibration) to fill-in slots reduce
omission and paraphrase rates across the board?

V-03 tests whether naming the degenerate register is the load-bearing variable
in C-58: does "FAIL: step-description narrative" produce different output than
"PASS: conclusion before evidence" alone?

V-04 tests whether schema-first-then-inertia-then-role creates a stronger pre-
task output contract than inertia-first-then-role (V-01/V-05 from R17).

V-05 tests whether the three innovations are additive: does combining all three
produce better scores than any single axis alone?
