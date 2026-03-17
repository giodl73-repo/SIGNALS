---
agent: 'agent'
tools: ['codebase']
description: 'Signal strategy revision as new information arrives with user confirmation.'
---

depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


## INERTIA PRIOR

This skill executes under an inertia prior: strategy.md unchanged is the
default outcome. The entire schema below is designed to surface evidence
that defeats that default. Where evidence is insufficient, the default wins.

The burden of proof rests on change. Do not propose changes absent
specific evidence from NEW signal artifacts. Inertia is a co-equal
outcome, not a fallback. A run that produces zero proposals is a valid,
complete execution of this skill.

This prior applies to every proposal table, every delta finding, and every
step in the schema below. It is not overridden by volume of signals.

---

You are running /topic:plan for the topic named in the user's message.

---

## COLUMN CONTRACT

Rule 1 -- Enumerated column values
Valid values (select one; prose is not valid):
  Action: ADD / REMOVE / REPRIORITIZE [Rule 1]
  Challenge strength: Strong / Moderate / Weak [Rule 1]
  Reversibility: Reversible at same cost / Gets harder / Becomes impossible [Rule 1]
  Delta-candidate: Yes / No / Pending signal [Rule 1]
PASS: "Weak" -- FAIL: "weak challenge, mostly"

Rule 2 -- Column independence
Test: Can I fill this cell without reading the source document?
PASS: "Team assumed biweekly review cadence prevents drift accumulation"
FAIL: "Assumption A evidence" (row-key reconstruction)

Rule 3 -- Null-case enforcement
All null-case declarations must carry a change-type label. Each absent change
type must have its own independently labeled declaration. A single unlabeled
"No changes proposed" covering multiple change types fails Rule 3.
At each null site: use the verbatim type-labeled null text provided.
"Do not omit this declaration" appears at each null site.
PASS: "ADDITIONS: none -- inertia holds for all candidate additions."
FAIL: "No changes proposed." (unlabeled -- ambiguous across change types)

Rule 4 -- Delta Finding traceability
Delta Finding column mandatory in all proposal rows.
Format: "Strategy assumed [X] / Signal revealed [Y]."
Null rows: "Delta Finding: N/A."
PASS: "Strategy assumed weekly cadence / Signal revealed daily drift"
FAIL: "scout-feasibility-2026-03-14.md" (single-hop, assumption not surfaced)

Rule 5 -- Symmetric inertia-rejection justification
Column name: Inertia Rejected Because [REQUIRED]
Required in: ALL change-type proposal tables (Step 4a and Step 4b)
Schema: identical column name, identical REQUIRED status, identical
prose-prohibition rule across both tables.
Format: one sentence naming the specific signal evidence or logic that defeats
the keep-unchanged option.
PASS: specific named signal with deferral consequence stated -- not generic.
FAIL: "compelling argument exists" (generic, non-specific, prose substitute)
A "Why this beats NO CHANGE" column is not a valid substitute. The REQUIRED
label is part of the enforcement contract. Both tables must carry the
identical column or neither achieves the criterion.

Rule 6 -- Per-entry delta citation
Every entry in every delta category sub-section (Step 3b-1 through 3b-4) must
carry: (a) the source artifact filename, and (b) a statement of what
understanding changed as a result of that signal.
Citation format: "[Source: {filename}] Understanding changed: {prior} -> {now}"
An entry without this two-part citation is structurally incomplete.
PASS: "[Source: prove-interview-2026-03-15.md] Understanding changed: assumed
  users care most about latency -> revealed users prioritize correctness over speed"
FAIL: "prove-interview-2026-03-15.md" (filename only, no understanding-change stated)
FAIL: "Users care about correctness" (claim only, no source named)

Rule 7 -- Gate token compliance
Each gate block (GC-1, GC-2, GC-3) must emit exactly the token declared in
the GATE COMPLIANCE MANIFEST at the site specified. A token that differs from
the declared string is a structural violation. A missing token is a structural
violation independent of whether the gate condition was satisfied.

Rule 8 -- Dual-source citation in gate blocks
Each gate block must explicitly name both the GATE ARCHITECTURE DECLARATION
and the GATE COMPLIANCE MANIFEST as independent authoritative references for
its token obligation. A gate block citing only one source satisfies Rule 7
but fails Rule 8. Both sources must agree on the required token string. A
discrepancy between the two sources is itself a structural violation.

Rule 9 -- Pre-execution cross-source consistency check
The CROSS-SOURCE CONSISTENCY CHECK table is a required structural output before
Step 1 executes. Its absence before Step 1 is a schema-level violation,
independently enforceable by the same mechanism as token-string matching
(Rule 7). Gate blocks cite this artifact by its exact structural name:
"CROSS-SOURCE CONSISTENCY CHECK above". A DISCREPANCY verdict halts
execution before any gate fires.

---

## GATE COMPLIANCE MANIFEST

| Gate ID | Gate Name | Required Token | Meta-Violation |
|---------|-----------|---------------|----------------|
| GC-1 | READ-TO-ANALYSIS GATE | GATE CHECK PASSED -- READ-TO-ANALYSIS | Token omission is a structural violation independent of gate condition |
| GC-2 | ANALYSIS-TO-CONFIRMATION GATE | GATE CHECK PASSED -- ANALYSIS-TO-CONFIRMATION | Token omission is a structural violation independent of gate condition |
| GC-3 | CONFIRMATION-TO-APPLY GATE | GATE CHECK PASSED -- CONFIRMATION-TO-APPLY | Token omission is a structural violation independent of gate condition |

Emit this manifest now. Its presence before Step 1 is required.
Rules 7, 8, and 9 apply to all three Gate IDs above.

---

## GATE ARCHITECTURE DECLARATION

You are committing to this declaration now, before Step 1 opens.
You are a first-person participant in the execution contract below.
These are not rules you are subject to -- they are commitments you are
making at this moment, prior to all conditional logic.

You will govern execution through three named gates. You will not cross any
gate without emitting the declared token.

Gate 1 -- READ-TO-ANALYSIS GATE (GC-1)
You will emit exactly: GATE CHECK PASSED -- READ-TO-ANALYSIS
You will emit this before Step 3b opens. You are committing to this now.
Omitting this token is a breach of this commitment, not merely a violation.

Gate 2 -- ANALYSIS-TO-CONFIRMATION GATE (GC-2)
You will emit exactly: GATE CHECK PASSED -- ANALYSIS-TO-CONFIRMATION
You will emit this before Step 4 opens. You are committing to this now.
Omitting this token is a breach of this commitment, not merely a violation.

Gate 3 -- CONFIRMATION-TO-APPLY GATE (GC-3)
You will emit exactly: GATE CHECK PASSED -- CONFIRMATION-TO-APPLY
You will emit this after the user replies YES or REVISED. You are
committing to this now. Omitting this token is a breach of this
commitment, not merely a violation.

DECLARATION-TO-MANIFEST CROSS-REFERENCE:
This table is self-contained for token-equality verification. A reviewer
confirms declaration token = manifest token from this table alone without
consulting any downstream gate block or manifest entry.

| Gate | Declaration token | Manifest entry | Manifest token |
|------|-------------------|----------------|----------------|
| Gate 1 | GATE CHECK PASSED -- READ-TO-ANALYSIS | GC-1 (READ-TO-ANALYSIS GATE) | GATE CHECK PASSED -- READ-TO-ANALYSIS |
| Gate 2 | GATE CHECK PASSED -- ANALYSIS-TO-CONFIRMATION | GC-2 (ANALYSIS-TO-CONFIRMATION GATE) | GATE CHECK PASSED -- ANALYSIS-TO-CONFIRMATION |
| Gate 3 | GATE CHECK PASSED -- CONFIRMATION-TO-APPLY | GC-3 (CONFIRMATION-TO-APPLY GATE) | GATE CHECK PASSED -- CONFIRMATION-TO-APPLY |

Token equality: Declaration token = Manifest token for all three gates.
A discrepancy in any row is a structural error detectable from this table alone.
You are committing to the full gate architecture above. A declared token
absent from the output is a detectable gap against this declaration and
against the GATE COMPLIANCE MANIFEST simultaneously.

---

## CROSS-SOURCE CONSISTENCY CHECK

REQUIRED STRUCTURAL OUTPUT -- emit now, before Step 1 opens.
This is a required model output. Do not treat it as optional commentary.
Rule 9 mandates this artifact at this location. Its absence is a schema-level
violation (Rule 9), independently enforceable by the same mechanism as
token-string matching (Rule 7).

Compare, for each gate, the token string in the GATE ARCHITECTURE DECLARATION
against the token string in the GATE COMPLIANCE MANIFEST. Emit an explicit
CONSISTENT or DISCREPANCY verdict per gate.

| Gate | Token in GATE ARCHITECTURE DECLARATION | Token in GATE COMPLIANCE MANIFEST | Verdict |
|------|----------------------------------------|-----------------------------------|---------|
| GC-1 READ-TO-ANALYSIS | [declaration token] | [manifest GC-1 token] | CONSISTENT / DISCREPANCY |
| GC-2 ANALYSIS-TO-CONFIRMATION | [declaration token] | [manifest GC-2 token] | CONSISTENT / DISCREPANCY |
| GC-3 CONFIRMATION-TO-APPLY | [declaration token] | [manifest GC-3 token] | CONSISTENT / DISCREPANCY |

All verdicts CONSISTENT: proceed to Upfront Output Schema, then Step 1.
Any verdict DISCREPANCY: halt. Do not proceed to Step 1. Emit:
"CROSS-SOURCE DISCREPANCY DETECTED at [gate name].
GATE ARCHITECTURE DECLARATION declares: [token string].
GATE COMPLIANCE MANIFEST declares: [token string].
Execution halted. Resolve the discrepancy before proceeding."

---

## Upfront Output Schema

Commit to this schema before reading any file.

**Assumption table** (Step 1)
| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

**Signal inventory** (Step 3)
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**Delta findings -- four category sub-sections** (Step 3b)
Each category: | Finding ID | Source artifact | Citation [Rule 6] | Delta-candidate [Rule 1] |
Categories: 3b-1 Confirmed / 3b-2 Expanded / 3b-3 Unexpected / 3b-4 Challenged

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
No table merges. I will not merge Step 4a and 4b. I will not merge delta categories.

---

## INERTIA-GATE TEMPLATE

Reproduce this block verbatim at each [INERTIA-GATE] site below.
Do not abbreviate, paraphrase, or omit. Its presence at each site is required.
This block is reproduced verbatim at Steps 4, 4b, 6, and 7.

  +------------------------------------------------------------------------+
  | INERTIA-GATE                                                           |
  | The result of this step may leave this section unchanged.              |
  | Inertia is a co-equal option. The burden of proof rests on change.     |
  |                                                                        |
  | This block is reproduced verbatim at Steps 4, 4b, 6, and 7.           |
  | Its presence is required at each site.                                 |
  +------------------------------------------------------------------------+

---

## Step 1 -- Read strategy.md and extract assumptions

Read `simulations/TOPICS.md` to locate the strategy file path. Read
strategy.md (STRATEGY DATE = last-modified date).

Extract stated dimensions. Scan: scope of coverage / sequencing /
completion criteria / success thresholds.
Apply Rule 2 before populating each Implicit evidence cell.

| Assumption | Implicit evidence [Rule 2] | Signal adjudication | Delta-relevance | Delta-candidate [Rule 1] |

Null (Rule 3, type-labeled): "ASSUMPTIONS: none -- no implicit assumptions
identified; all strategy elements are explicitly stated."
Do not omit this declaration.

---

## Step 2 -- Pre-signal Defense Register

Output before reading any NEW artifact.

| Defense ID | Strategic decision | Strongest keep-it argument | What would invalidate |

---

## Step 3 -- Signal inventory

List every artifact in `simulations/` matching the topic slug. Classify NEW
(date > STRATEGY DATE) or PRIOR. All 9 namespaces must be explicitly
assessed: scout / draft / review / flow / trace / prove / listen / program /
topic.

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

**SIGNAL READ-LOCK**: Signal files may not be re-read after this step.
All subsequent steps use the written inventory only.

Null (Rule 3, type-labeled): "SIGNAL INVENTORY: null -- no artifacts found
for topic [name]. Cannot run /topic:plan."
Do not omit this declaration.

---

  +------------------------------------------------------------------------+
  | READ-TO-ANALYSIS GATE (GC-1)                                           |
  |                                                                        |
  | Token obligation -- two independent authoritative sources agree:       |
  |   GATE ARCHITECTURE DECLARATION (prose): you committed to emitting     |
  |     GATE CHECK PASSED -- READ-TO-ANALYSIS before Step 3b opens.        |
  |   GATE COMPLIANCE MANIFEST (registry, GC-1): declares required token   |
  |     GATE CHECK PASSED -- READ-TO-ANALYSIS at this site.               |
  | Sources are CONSISTENT (verified at CROSS-SOURCE CONSISTENCY CHECK     |
  | above). Either source independently confirms this obligation.          |
  |                                                                        |
  | Condition A: strategy.md read; assumption table present in output.     |
  | Condition B: signal inventory written; SIGNAL READ-LOCK in effect.     |
  | Proceeding before both conditions are met is a structural violation.   |
  |                                                                        |
  | Write this token before Step 3b opens:                                 |
  |   GATE CHECK PASSED -- READ-TO-ANALYSIS                               |
  | Omitting this token is a breach of the GATE ARCHITECTURE DECLARATION   |
  | commitment and a Rule 7 manifest violation (Rule 7, Rule 8).           |
  +------------------------------------------------------------------------+

## Step 3b -- Delta findings (four categories)

For each NEW artifact, classify each finding into one of four named categories.
Every entry in every category must carry Rule 6 citation: two parts required.
Citation format: "[Source: {filename}] Understanding changed: {prior} -> {now}"
An entry without the two-part citation is structurally incomplete.
Do not merge categories. Each category has its own sub-section and table.

### 3b-1 -- CONFIRMED
| Finding ID | Existing strategy assumption | Confirmed by | Citation [Rule 6] | Delta-candidate [Rule 1] |

Null (Rule 3, type-labeled): "CONFIRMED: none -- no NEW artifacts confirm existing assumptions."
Do not omit this declaration.

### 3b-2 -- EXPANDED
| Finding ID | Existing assumption | Expanded to | Citation [Rule 6] | Delta-candidate [Rule 1] |

Null (Rule 3, type-labeled): "EXPANDED: none -- no NEW artifacts expand existing assumptions."
Do not omit this declaration.

### 3b-3 -- UNEXPECTED
| Finding ID | Strategy gap (what was missing) | Signal revealed | Citation [Rule 6] | Delta-candidate [Rule 1] |

Null (Rule 3, type-labeled): "UNEXPECTED: none -- no NEW artifacts reveal uncovered dimensions."
Do not omit this declaration.

### 3b-4 -- CHALLENGED
| Finding ID | Strategy assumed | Signal challenges | Citation [Rule 6] | Delta-candidate [Rule 1] |

Null (Rule 3, type-labeled): "CHALLENGED: none -- no NEW artifacts challenge existing strategy."
Do not omit this declaration.

---

  +------------------------------------------------------------------------+
  | ANALYSIS-TO-CONFIRMATION GATE (GC-2)                                   |
  |                                                                        |
  | Token obligation -- two independent authoritative sources agree:       |
  |   GATE ARCHITECTURE DECLARATION (prose): you committed to emitting     |
  |     GATE CHECK PASSED -- ANALYSIS-TO-CONFIRMATION before Step 4 opens. |
  |   GATE COMPLIANCE MANIFEST (registry, GC-2): declares required token   |
  |     GATE CHECK PASSED -- ANALYSIS-TO-CONFIRMATION at this site.        |
  | Sources are CONSISTENT (verified at CROSS-SOURCE CONSISTENCY CHECK     |
  | above). Either source independently confirms this obligation.          |
  |                                                                        |
  | Change proposals are not written until all four Step 3b categories     |
  | are complete in the output above. Advancing before this is a           |
  | structural violation.                                                  |
  |                                                                        |
  | Write this token before Step 4 opens:                                  |
  |   GATE CHECK PASSED -- ANALYSIS-TO-CONFIRMATION                       |
  | Omitting this token is a breach of the GATE ARCHITECTURE DECLARATION   |
  | commitment and a Rule 7 manifest violation (Rule 7, Rule 8).           |
  +------------------------------------------------------------------------+

## Step 4 -- Change proposals (preamble)

[INERTIA-GATE] -- Reproduce verbatim here before writing any proposal row.

A proposal that cannot name a concrete consequence of deferral (the "If
unchanged" column) is a preference, not a decision -- structurally invalid,
not merely incomplete.

---

## Step 4a -- Additions

The following columns are mandatory. Do not omit any column.
"Inertia Rejected Because [REQUIRED]": one sentence per row naming the
specific evidence or logic defeating the keep-unchanged option (Rule 5).
PASS: specific signal evidence named -- FAIL: "compelling reason"

| # | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

Null (Rule 3, type-labeled): "ADDITIONS: none -- inertia holds.
Do not omit this declaration."

---

## Step 4b -- Removals and Reprioritizations

[INERTIA-GATE] -- Reproduce verbatim here before writing any row.

The following columns are mandatory. Do not omit any column.
"Inertia Rejected Because [REQUIRED]": identical schema to Step 4a (Rule 5).
FAIL: "compelling reason" or any prose substitute.

| # | Action [Rule 1] | Dimension | Delta Finding [Rule 4] | Evidence | Before | After | Confidence | If unchanged | Reversibility [Rule 1] | Inertia Rejected Because [REQUIRED] |

Null declarations (Rule 3, type-labeled):
  "REMOVALS: none -- inertia holds. Do not omit this declaration."
  "REPRIORITIZATIONS: none -- inertia holds. Do not omit this declaration."

---

## Step 4c -- Defender Challenge Table

A table where every challenge is Weak is a structural signal of rubber-stamp
processing, not genuine evaluation.

Defense basis: D-ID if pre-registered; "Newly constructed" if built after
signal reading.

The following columns are mandatory. Do not omit any column.

| Defense ID | Proposal # | Strategic decision defended | Defensive argument | Defense basis | Challenge strength [Rule 1] |

**Calibration check** (required artifact): After completing the table,
produce one sentence:
  - All Weak -> "Calibration: rubber-stamp risk -- all challenges are Weak."
  - All Strong -> "Calibration: over-zealous risk -- all challenges are Strong."
  - Otherwise -> "Calibration: balanced -- challenge strength distribution is varied."

---

## Step 5 -- Conflict audit

Identify any NEW artifacts that contradict each other on the same strategy
dimension.

The following columns are mandatory: Conflict ID / Signal A / Signal B /
Nature of conflict / Resolution.

Null (Rule 3, type-labeled): "CONFLICT AUDIT: none -- no contradictions
detected between NEW artifacts on the same strategy dimension."
Do not omit this declaration.

---

## Step 6 -- Before/after diff

[INERTIA-GATE] -- Reproduce verbatim here before producing the diff table.

Include [evidence brackets] in each After cell and Proposal cross-refs
(e.g., "ADD-1") per row. The following columns are mandatory.

| Dimension | Before | After [evidence bracket] | Proposal [cross-ref] |

---

## Step 7 -- Confirmation gate

[INERTIA-GATE] -- Reproduce verbatim here before presenting any output.
NO is a complete and valid outcome.

Display: Step 3b (all four categories) / Step 4a / Step 4b /
Step 4c (with calibration check) / Step 6.

Individual proposals may be withdrawn before gate execution. Reply YES
applies only to non-withdrawn proposals.

Write exactly:

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.

Proposed (non-withdrawn): [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table
to apply custom version | WITHDRAW [#] to remove specific proposals before
confirming
---

Stop here. Write nothing further until the user replies.

---

  +------------------------------------------------------------------------+
  | CONFIRMATION-TO-APPLY GATE (GC-3)                                      |
  |                                                                        |
  | Token obligation -- two independent authoritative sources agree:       |
  |   GATE ARCHITECTURE DECLARATION (prose): you committed to emitting     |
  |     GATE CHECK PASSED -- CONFIRMATION-TO-APPLY after user YES/REVISED. |
  |   GATE COMPLIANCE MANIFEST (registry, GC-3): declares required token   |
  |     GATE CHECK PASSED -- CONFIRMATION-TO-APPLY at this site.           |
  | Sources are CONSISTENT (verified at CROSS-SOURCE CONSISTENCY CHECK     |
  | above). Either source independently confirms this obligation.          |
  |                                                                        |
  | strategy.md is not modified without an explicit YES or REVISED from   |
  | the user at Step 7. The absence of a NO reply does not constitute     |
  | implicit YES. Step 8 does not open without that confirmation.         |
  |                                                                        |
  | Write this token after the user replies YES or REVISED:               |
  |   GATE CHECK PASSED -- CONFIRMATION-TO-APPLY                          |
  | Omitting this token is a breach of the GATE ARCHITECTURE DECLARATION   |
  | commitment and a Rule 7 manifest violation (Rule 7, Rule 8).           |
  +------------------------------------------------------------------------+

## Step 8 -- Apply

Triggered only after YES or REVISED.

Write exactly the confirmed (non-withdrawn) changes. No additional formatting
of unchanged sections.

Confirm: "strategy.md updated: [N] additions, [N] removals, [N]
reprioritizations."