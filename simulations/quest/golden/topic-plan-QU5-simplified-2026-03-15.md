The result of this skill may be zero changes, some changes, or a full
strategy replacement. Inertia is a co-equal option, not a fallback.
The burden of proof rests on change, not on stability.

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
PASS: "Strategy assumed weekly cadence / Signal revealed daily drift"
FAIL: "scout-feasibility-2026-03-14.md" (single-hop, assumption not surfaced)

Rule 5 — Symmetric inertia-rejection justification
Column name: Inertia Rejected Because [REQUIRED]
Required in: ALL change-type proposal tables (Step 4a and Step 4b)
Schema: identical column name, identical REQUIRED status, identical
prose-prohibition rule across both tables.
Format: one sentence naming the specific signal evidence or logic that defeats
the keep-unchanged option.
PASS: specific named signal with deferral consequence stated — not generic.
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

Pre-read commitment: columns above are fixed. No prose substitutes.
No table merges. I will not merge Step 4a and 4b.

---

## INERTIA-GATE TEMPLATE

Reproduce this block verbatim at each [INERTIA-GATE] site below.
Do not abbreviate, paraphrase, or omit. Its presence at each site is required.

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

[INERTIA-GATE] — Reproduce verbatim here before writing any proposal row.

A proposal that cannot name a concrete consequence of deferral (the "If
unchanged" column) is a preference, not a decision — structurally invalid,
not merely incomplete.

---

## Step 4a — Additions

The following columns are mandatory. Do not omit any column.
"Inertia Rejected Because [REQUIRED]": one sentence per row naming the
specific evidence or logic defeating the keep-unchanged option (Rule 5).
PASS: specific signal evidence named — FAIL: "compelling reason"

| # | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

Null (Rule 3, type-labeled): "ADDITIONS: none — inertia holds.
Do not omit this declaration."

---

## Step 4b — Removals and Reprioritizations

[INERTIA-GATE] — Reproduce verbatim here before writing any row.

The following columns are mandatory. Do not omit any column.
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

[INERTIA-GATE] — Reproduce verbatim here before producing the diff table.

Include [evidence brackets] in each After cell and Proposal cross-refs
(e.g., "ADD-1") per row.

The following columns are mandatory. Do not omit any column.

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
