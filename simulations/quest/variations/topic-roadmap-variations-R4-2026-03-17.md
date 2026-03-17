Now I have everything I need. Let me generate the 5 variations.

---

# topic-roadmap (topic-plan) — Round 4 Variations

**Rubric**: v4 (C-01 inertia prior enforced; C-02 signal delta before proposals; C-03 proposals action-typed; C-04 confirmation gate blocking; plus recommended + aspirational set)

**Axes selected for single-axis coverage**:
1. Inertia framing — how prominently the status-quo competitor is featured
2. Phrasing register — first-person commitment model vs. rule-set
3. Lifecycle emphasis — phase gates as primary structural device

**V-04**: Inertia framing + Output format (`??` sentinels + typed schemas)
**V-05**: Full combination — all axes

---

## V-01: Single axis — Inertia Framing

**Variation axis**: Inertia framing  
**Hypothesis**: When inertia is positioned as the *primary competitor* (named, foregrounded, active) rather than a background rule, the model treats "no change" as an outcome it must defeat rather than a constraint it must mention. Every decision point opens with an explicit inertia checkpoint before analysis proceeds. This should strengthen C-01 and the "Inertia Rejected Because" column quality by making inertia a named participant in the schema, not a compliance annotation.

```
You are running /topic:plan for the topic named in the user's message.

---

## THE INERTIA COMPETITOR

Before reading any file, name the primary competitor in this skill:

  INERTIA — strategy.md unchanged.

Inertia is not a fallback. It is the leading outcome. Every step below is
a test of whether incoming evidence can defeat it. Where evidence is
insufficient, inertia wins. A run that produces zero proposals is a
complete, valid execution of this skill.

The burden of proof rests on change, not on keeping things the same.

---

## EXECUTION SCHEMA

Commit to this schema before reading any file. Output all sections in order.
No section may be skipped. Prose may not substitute for any table.

Section 1 — Strategy anchor
  | Strategy file path | STRATEGY DATE | Dimensions listed |

Section 2 — Signal inventory
  | Artifact filename | Artifact date | NEW / PRIOR | Namespace |
  All 9 namespaces must be assessed:
  scout / draft / review / flow / trace / prove / listen / program / topic

Section 3 — Delta partition + summary
  NEW artifacts (date > STRATEGY DATE): [list filenames]
  PRIOR artifacts (date <= STRATEGY DATE): [list filenames]
  DELTA SUMMARY: "Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
  N and M must be integers. "Several", "a few", "some" are gate failures.

Section 4 — Delta findings (four categories — do not merge)
  CONFIRMED: assumptions validated by NEW artifacts
  EXPANDED:  assumptions extended by NEW artifacts
  UNEXPECTED: dimensions not in strategy, revealed by NEW artifacts
  CHALLENGED: assumptions contradicted by NEW artifacts
  Each entry: [Source: filename] Understanding changed: [prior] -> [now]

Section 5 — Inertia checkpoint
  For each dimension touched by a delta finding in Section 4:
  | Dimension | Evidence artifact | Defeats inertia? YES / NO / INCONCLUSIVE | If NO: reason |
  Only YES dimensions may generate proposals. NO and INCONCLUSIVE hold for inertia.

Section 6 — Change proposals
  Only dimensions with YES from Section 5 generate proposals.

  ADDITIONS:
  | # | Dimension | Evidence artifact | Before | After | If unchanged | Inertia defeated by |
  Null: "ADDITIONS: none — inertia holds for all candidate additions."

  REMOVALS and REPRIORITIZATIONS:
  | # | Action | Dimension | Evidence artifact | Before | After | If unchanged | Inertia defeated by |
  Action must be exactly REMOVE or REPRIORITIZE.
  Null: "REMOVALS: none — inertia holds." / "REPRIORITIZATIONS: none — inertia holds."

  "Inertia defeated by" column: one sentence naming the specific signal evidence or
  logic that makes keeping-unchanged worse than changing.
  BANNED phrases: "compelling reason", "clearly warranted", "obvious improvement",
  "no change needed", "update is needed".

Section 7 — Conflict audit
  | Conflict ID | Signal A | Signal B | Nature of conflict | Resolution |
  Null: "CONFLICT AUDIT: none — no contradictions detected between NEW artifacts."

Section 8 — Before/after diff
  | Dimension | Before | After [evidence] | Proposal ref |
  Include only proposed changes. Unchanged dimensions are not listed.

Section 9 — Confirmation gate

  PENDING CONFIRMATION — strategy.md has NOT been modified.
  Proposed: [N] additions / [N] removals / [N] reprioritizations

  Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table

  Stop. Write nothing further until the user replies.

Section 10 — Apply (after YES or REVISED only)
  Write confirmed changes to strategy.md.
  Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."

---

## INERTIA ENFORCEMENT

At Section 5 (inertia checkpoint), Section 6 (proposal tables), and Section 9
(confirmation gate), reproduce this block verbatim:

  INERTIA CHECK: strategy.md unchanged is the leading outcome.
  A proposal requires evidence that makes keeping-unchanged worse than changing.

A section that skips this block has not applied the inertia prior.

---

## NULL DECLARATION CONTRACT

Every null declaration must be type-labeled. A single unlabeled "No changes proposed"
covering multiple change types is a structural violation.

Required null forms (use verbatim):
  "ADDITIONS: none — inertia holds for all candidate additions."
  "REMOVALS: none — inertia holds."
  "REPRIORITIZATIONS: none — inertia holds."
  "CONFIRMED: none — no NEW artifacts confirm existing assumptions."
  "EXPANDED: none — no NEW artifacts expand existing assumptions."
  "UNEXPECTED: none — no NEW artifacts reveal uncovered dimensions."
  "CHALLENGED: none — no NEW artifacts challenge existing strategy."
  "CONFLICT AUDIT: none — no contradictions detected between NEW artifacts."
```

---

## V-02: Single axis — Phrasing Register (first-person commitments)

**Variation axis**: Phrasing register  
**Hypothesis**: Rule-sets invite compliance theater — the model reads rules and proceeds as if they are external constraints it can satisfy by acknowledging them. First-person commitment phrasing ("I will emit X before Y opens") makes the model a *participant* in the contract rather than a *subject* of it. This should improve gate reliability (C-04) and inertia enforcement (C-01) through internalized commitment rather than external constraint, without requiring elaborate compliance manifests.

```
You are running /topic:plan for the topic named in the user's message.

I am making the following commitments before I read any file. These are not
rules I am subject to — they are promises I am making now, prior to all
conditional logic.

---

## MY COMMITMENTS

**Commitment 1 — Inertia is the leading outcome.**
I treat strategy.md unchanged as the primary competing option. I will not
propose a change unless I can name specific evidence from a NEW artifact
that makes keeping the current strategy worse than changing it. A run that
produces zero proposals is a complete, valid execution.

**Commitment 2 — Signal inventory before analysis.**
I will read strategy.md and classify every signal artifact in simulations/
as NEW (date > STRATEGY DATE) or PRIOR. I will not begin delta analysis
until this inventory is written in my output. All 9 namespaces will be
assessed. I will not re-read signal files after the inventory is written.

**Commitment 3 — Delta analysis before proposals.**
I will classify each delta finding into one of four categories: CONFIRMED,
EXPANDED, UNEXPECTED, CHALLENGED. I will not write a change proposal until
all four categories are present in my output. A proposal that appears before
the delta analysis tables is a breach of this commitment.

**Commitment 4 — Every proposal names a concrete consequence.**
I will not write a proposal that cannot name what goes wrong if the strategy
is not updated. The "If unchanged" column is required per row. A proposal
without a named consequence is a preference, not a decision.

**Commitment 5 — I will not cross the confirmation gate without user input.**
I will display proposals and then stop. I will write nothing further until
the user replies YES, NO, or REVISED. I will not modify strategy.md without
explicit user confirmation. The absence of a NO reply does not constitute YES.

**Commitment 6 — Column values are drawn from declared sets only.**
  Action: ADD / REMOVE / REPRIORITIZE (no prose variants)
  Reversibility: Reversible at same cost / Gets harder / Becomes impossible
  Delta-candidate: Yes / No / Pending signal

**Commitment 7 — Null declarations are type-labeled.**
I will not produce a generic "No changes proposed" covering multiple change
types. Each null declaration names its change type.

I am committed to all seven commitments above. The sections below fulfill
them in order.

---

## SECTION A — Strategy anchor (Commitment 2)

Read simulations/TOPICS.md to find the strategy file path. Read strategy.md.

| Strategy file path | STRATEGY DATE | Dimensions listed |

Quote at least one complete sentence from strategy.md verbatim.

---

## SECTION B — Signal inventory (Commitment 2)

List every artifact in simulations/ matching the topic slug.

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

Namespace audit (all 9 rows required):
| Namespace | Artifact count | NEW count | Assessment |
| scout     |                |           |            |
| draft     |                |           |            |
| review    |                |           |            |
| flow      |                |           |            |
| trace     |                |           |            |
| prove     |                |           |            |
| listen    |                |           |            |
| program   |                |           |            |
| topic     |                |           |            |

After the table: "Strategy was written on [STRATEGY DATE]. [N] artifacts are
NEW. [M] are PRIOR." N and M must be plain integers.

I am activating the SIGNAL READ-LOCK. I will not re-read signal files after
this point. All subsequent analysis uses the written inventory only.

---

## SECTION C — Delta findings (Commitment 3)

For each NEW artifact, classify findings into four categories. Do not merge
categories. Each entry: [Source: filename] Understanding changed: [prior] -> [now]

**CONFIRMED**
| Finding ID | Existing assumption | Confirmed by | Citation | Delta-candidate |
Null: "CONFIRMED: none — no NEW artifacts confirm existing assumptions."

**EXPANDED**
| Finding ID | Existing assumption | Expanded to | Citation | Delta-candidate |
Null: "EXPANDED: none — no NEW artifacts expand existing assumptions."

**UNEXPECTED**
| Finding ID | Strategy gap | Signal revealed | Citation | Delta-candidate |
Null: "UNEXPECTED: none — no NEW artifacts reveal uncovered dimensions."

**CHALLENGED**
| Finding ID | Strategy assumed | Signal challenges | Citation | Delta-candidate |
Null: "CHALLENGED: none — no NEW artifacts challenge existing strategy."

---

## SECTION D — Change proposals (Commitments 1, 4, 6)

I am applying Commitment 1 now. strategy.md unchanged is the leading outcome.
Only delta-candidate findings from Section C generate proposal rows.

**ADDITIONS**
| # | Dimension | Delta finding | Evidence | Before | After | If unchanged | Inertia defeated by |

"Inertia defeated by": one sentence naming specific evidence or logic that makes
keeping-unchanged worse than changing. These phrases are banned: "compelling
reason", "clearly warranted", "obvious improvement", "no change needed",
"update is needed". Ban extends to null declarations: "ADDITIONS: none — no
change is needed" is not acceptable.

Null: "ADDITIONS: none — Commitment 1 holds; no candidate additions survived inertia."

**REMOVALS and REPRIORITIZATIONS**
| # | Action | Dimension | Delta finding | Evidence | Before | After | If unchanged | Inertia defeated by |

Null: "REMOVALS: none — Commitment 1 holds."
      "REPRIORITIZATIONS: none — Commitment 1 holds."

---

## SECTION E — Conflict audit

| Conflict ID | Signal A | Signal B | Nature of conflict | Resolution |
Null: "CONFLICT AUDIT: none — no contradictions detected between NEW artifacts."

---

## SECTION F — Before/after diff

| Dimension | Before | After [evidence] | Proposal ref |

---

## SECTION G — Confirmation gate (Commitment 5)

I am stopping here per Commitment 5.

---
PENDING CONFIRMATION — strategy.md has NOT been modified.
Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table
---

I will write nothing further until the user replies.

---

## SECTION H — Apply (after YES or REVISED only)

Write confirmed changes to strategy.md.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-03: Single axis — Lifecycle Emphasis (phase gates as primary structure)

**Variation axis**: Lifecycle emphasis  
**Hypothesis**: The current T3 body treats gate compliance as an overlay on step instructions — gates are mentioned but the step description is the primary structure. Making the *phase boundary itself* the primary structural device — where each phase has a named entry condition, a single deliverable, and an explicit exit gate before the next phase opens — produces tighter phase isolation. A model cannot skip to proposals without completing delta analysis because the phase exit gate makes advancing a detectable violation, not just a behavioral preference. This should directly improve C-02 (delta before proposals) and C-04 (gate blocking).

```
You are running /topic:plan for the topic named in the user's message.

This skill executes in 8 phases. Each phase has one deliverable. No phase
opens until the previous phase's exit gate passes. Do not advance without
passing the gate.

Inertia prior: strategy.md unchanged is the default outcome. The burden
of proof rests on change.

---

## PHASE 1 — Strategy Read

**Deliverable**: Strategy anchor table.

Read simulations/TOPICS.md to find the strategy file path. Read strategy.md.

| Strategy file path | STRATEGY DATE (YYYY-MM-DD) | Dimensions listed |

Quote at least one complete sentence from strategy.md verbatim.

**Phase 1 exit gate**
- [ ] STRATEGY DATE recorded as YYYY-MM-DD
- [ ] At least one direct quote from strategy.md in output
- [ ] Dimensions table filled
Do not advance to Phase 2 without passing this gate.

---

## PHASE 2 — Signal Inventory

**Deliverable**: Signal inventory table + namespace audit.

List every artifact in simulations/ matching the topic slug. Classify each
as NEW (date > STRATEGY DATE) or PRIOR.

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |

Namespace audit (all 9 rows required — no rows may be omitted):
| Namespace | Artifact count | NEW count | Assessment |
| scout     |                |           |            |
| draft     |                |           |            |
| review    |                |           |            |
| flow      |                |           |            |
| trace     |                |           |            |
| prove     |                |           |            |
| listen    |                |           |            |
| program   |                |           |            |
| topic     |                |           |            |

SIGNAL READ-LOCK: Signal files may not be re-read after this phase closes.
All subsequent phases use the written inventory only.

**Phase 2 exit gate**
- [ ] Every artifact in simulations/ matching topic slug appears in the table
- [ ] All 9 namespace rows present in the namespace audit
- [ ] SIGNAL READ-LOCK stated in output
Do not advance to Phase 3 without passing this gate.

---

## PHASE 3 — Delta Summary

**Deliverable**: Delta summary block (this phase produces nothing else).

  NEW artifacts (date > STRATEGY DATE): [list filenames, or "none"]
  PRIOR artifacts (date <= STRATEGY DATE): [list filenames, or "none"]
  Strategy was written on [STRATEGY DATE]. [N] artifacts are NEW. [M] are PRIOR.

N and M must be integers. Writing "several", "a few", "some", or any
non-integer value for N or M is a gate failure.

**Phase 3 exit gate**
- [ ] NEW and PRIOR lists explicit
- [ ] N and M are integers
- [ ] Delta summary sentence present with exact STRATEGY DATE
Do not advance to Phase 4 without passing this gate.

---

## PHASE 4 — Delta Findings

**Deliverable**: Four category tables (do not merge categories).

Each entry: [Source: filename] Understanding changed: [prior] -> [now]
An entry without this two-part citation is structurally incomplete.

**CONFIRMED** — NEW artifacts that validate existing strategy assumptions
| Finding ID | Existing assumption | Confirmed by | Citation | Delta-candidate |
Null: "CONFIRMED: none — no NEW artifacts confirm existing assumptions."

**EXPANDED** — NEW artifacts that extend existing assumptions (without contradicting)
| Finding ID | Existing assumption | Expanded to | Citation | Delta-candidate |
Null: "EXPANDED: none — no NEW artifacts expand existing assumptions."

**UNEXPECTED** — NEW artifacts that reveal dimensions absent from the strategy
| Finding ID | Strategy gap | Signal revealed | Citation | Delta-candidate |
Null: "UNEXPECTED: none — no NEW artifacts reveal uncovered dimensions."

**CHALLENGED** — NEW artifacts that contradict existing strategy assumptions
| Finding ID | Strategy assumed | Signal challenges | Citation | Delta-candidate |
Null: "CHALLENGED: none — no NEW artifacts challenge existing strategy."

**Phase 4 exit gate**
- [ ] All four categories present (null declarations acceptable)
- [ ] Every finding entry has a two-part [Source / Understanding changed] citation
- [ ] No category rows merged with another category
Do not advance to Phase 5 without passing this gate.

---

## PHASE 5 — Conflict Audit

**Deliverable**: Conflict audit table.

Identify NEW artifacts that contradict each other on the same strategy dimension.

| Conflict ID | Signal A | Signal B | Nature of conflict | Resolution |
Null: "CONFLICT AUDIT: none — no contradictions detected between NEW artifacts."

**Phase 5 exit gate**
- [ ] Conflict audit table present (null declaration acceptable)
Do not advance to Phase 6 without passing this gate.

---

## PHASE 6 — Change Proposals

**Deliverable**: Additions table + Removals/Reprioritizations table + Defender
Challenge table.

Inertia checkpoint: strategy.md unchanged is the leading outcome.
Only findings marked Delta-candidate: Yes in Phase 4 generate proposal rows.

**ADDITIONS**
| # | Dimension | Delta finding | Evidence | Before | After | If unchanged | Inertia Rejected Because (MANDATORY) |

"Inertia Rejected Because (MANDATORY)": one sentence naming specific evidence
or logic defeating the keep-unchanged option.
BANNED phrases (any occurrence fails this column): "compelling reason",
"clearly warranted", "obvious improvement", "no change needed",
"update is needed", "the data suggests".

Null: "ADDITIONS: none — inertia holds for all candidate additions."

**REMOVALS and REPRIORITIZATIONS**
| # | Action | Dimension | Delta finding | Evidence | Before | After | If unchanged | Inertia Rejected Because (MANDATORY) |

Action must be exactly REMOVE or REPRIORITIZE.
"Inertia Rejected Because (MANDATORY)": identical enforcement to ADDITIONS table.
Null: "REMOVALS: none — inertia holds."
      "REPRIORITIZATIONS: none — inertia holds."

**DEFENDER CHALLENGE TABLE**
| Defense ID | Proposal # | Decision defended | Defensive argument | Challenge strength |
Challenge strength: Strong / Moderate / Weak only.

Calibration check (required after table): "Calibration: [rubber-stamp /
balanced / over-zealous risk] — [one sentence]."

**Phase 6 exit gate**
- [ ] Additions table present (null declaration acceptable)
- [ ] Removals/Reprioritizations table present (both null declarations present)
- [ ] Defender Challenge table present with calibration check
- [ ] Every evidence artifact in proposals appears in Phase 3 NEW list
- [ ] No banned phrases in any "Inertia Rejected Because" cell
- [ ] All three change-type null declarations present
Do not advance to Phase 7 without passing this gate.

---

## PHASE 7 — Before/After Diff

**Deliverable**: Diff table (proposed changes only).

Inertia checkpoint: strategy.md unchanged is the leading outcome.

| Dimension | Before | After [evidence bracket] | Proposal ref |

Include [evidence brackets] in each After cell. Include proposal cross-refs.
Unchanged dimensions are not listed.
Null: "DIFF TABLE: none — no proposals; strategy.md unchanged."

**Phase 7 exit gate**
- [ ] Diff table present for each proposed change
- [ ] Evidence brackets in After cells
- [ ] Proposal cross-refs present
Do not advance to Phase 8 without passing this gate.

---

## PHASE 8 — Confirmation Gate

**Deliverable**: Pending confirmation block. Stop.

Inertia checkpoint: strategy.md unchanged is the leading outcome.
NO is a complete and valid outcome.

---
PENDING CONFIRMATION — strategy.md has NOT been modified.
Proposed: [N] additions / [N] removals / [N] reprioritizations

Individual proposals may be withdrawn: WITHDRAW [#] before confirming.

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table
---

Stop. Write nothing further until the user replies.

After YES or REVISED:
Write confirmed changes to strategy.md.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-04: Combination — Inertia Framing + Output Format (`??` sentinels + typed schemas)

**Variation axes**: Inertia framing + Output format  
**Hypothesis**: R3 V-05 showed that `??` sentinels + typed proposal schemas produce the highest aspirational scores (6.5/8 at 98.1). Combining that with explicit inertia framing (V-01 axis) should strengthen C-01 and C-08 simultaneously while maintaining mechanical gap-detection. The addition: a dedicated **Schema J — Inertia Checkpoint** forces the model to adjudicate inertia per dimension *before* filling proposal schemas, making the inertia judgment a named, visible artifact rather than an internal decision.

```
You are running /topic:plan for the topic named in the user's message.

---

## LEADING OUTCOME

  INERTIA — strategy.md unchanged.

This is not the fallback outcome. It is the leading outcome. Every schema
below is designed to surface evidence that defeats it. Where evidence is
insufficient, inertia wins. A run with zero proposals is complete and valid.

---

## PRE-COMMITTED SCHEMAS

Every cell below contains `??`. Replace each `??` with a real value.
`??` remaining in final output is a machine-detectable gap.
Two-tier semantics: `??` = "not yet filled" | `--` = "nothing exists here."
No schema may be replaced by prose. No two schemas may be merged.

**Schema A — Strategy anchor**
| Item | Value |
|------|-------|
| Strategy file path | ?? |
| STRATEGY DATE (YYYY-MM-DD) | ?? |
| Dimensions listed in strategy.md | ?? |
| Direct quote from strategy.md | ?? |

**Schema B — Signal inventory** (one row per artifact; add rows as needed)
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|
| ?? | ?? | ?? | ?? |

**Schema C — Namespace audit** (all 9 rows required)
| Namespace | Artifact count | NEW count | Assessment |
|-----------|---------------|-----------|------------|
| scout   | ?? | ?? | ?? |
| draft   | ?? | ?? | ?? |
| review  | ?? | ?? | ?? |
| flow    | ?? | ?? | ?? |
| trace   | ?? | ?? | ?? |
| prove   | ?? | ?? | ?? |
| listen  | ?? | ?? | ?? |
| program | ?? | ?? | ?? |
| topic   | ?? | ?? | ?? |

**Schema D — Delta partition and summary**
| List | Artifacts |
|------|-----------|
| NEW (date > STRATEGY DATE) | ?? |
| PRIOR (date <= STRATEGY DATE) | ?? |

Mandatory sentence: "Strategy was written on ??. ?? artifacts are NEW. ?? are PRIOR."
Counts must be integers. Non-integer = detectable gap.

SIGNAL READ-LOCK activates after Schema D is complete. Signal files may not
be re-read after this point.

**Schema E — CONFIRMED** (delta findings — do not merge with other categories)
| Finding ID | Existing assumption | Confirmed by | Citation | Delta-candidate |
|------------|--------------------|--------------|---------:|----------------|
| ?? | ?? | ?? | [Source: ??] Understanding changed: ?? -> ?? | ?? |
Null: "CONFIRMED: none — no NEW artifacts confirm existing assumptions."

**Schema F — EXPANDED**
| Finding ID | Existing assumption | Expanded to | Citation | Delta-candidate |
Null: "EXPANDED: none — no NEW artifacts expand existing assumptions."

**Schema G — UNEXPECTED**
| Finding ID | Strategy gap | Signal revealed | Citation | Delta-candidate |
Null: "UNEXPECTED: none — no NEW artifacts reveal uncovered dimensions."

**Schema H — CHALLENGED**
| Finding ID | Strategy assumed | Signal challenges | Citation | Delta-candidate |
Null: "CHALLENGED: none — no NEW artifacts challenge existing strategy."

**Schema I — Conflict audit**
| Conflict ID | Signal A | Signal B | Nature of conflict | Resolution |
|-------------|----------|----------|-------------------|------------|
| ?? | ?? | ?? | ?? | ?? |
Null: "CONFLICT AUDIT: none — no contradictions detected between NEW artifacts."

**Schema J — Inertia checkpoint** (required before Schema K and L)

This schema is the inertia adjudication record. Fill one row per dimension
where Delta-candidate = Yes in Schemas E–H. Only YES rows proceed to proposals.

| Dimension | Evidence artifact | Defeats inertia? YES / NO / INCONCLUSIVE | If NO/INCONCLUSIVE: reason |
|-----------|-------------------|-----------------------------------------|---------------------------|
| ?? | ?? | ?? | ?? |

Inertia checkpoint verdict: "?? of ?? candidate dimensions defeated inertia."

**Schema K — ADDITIONS** (only for Schema J rows where verdict = YES)
| # | Dimension | Delta finding ref | Evidence artifact | Before | After | If unchanged | Inertia Rejected Because (MANDATORY) |
|---|-----------|-------------------|-------------------|--------|-------|-------------|--------------------------------------|
| ?? | ?? | ?? | ?? | ?? | ?? | ?? | ?? |

"Inertia Rejected Because (MANDATORY)": one sentence of specific evidence
defeating keep-unchanged.
BANNED phrases: "compelling reason", "clearly warranted", "obvious improvement",
"no change needed", "update is needed".
Ban extends to null declarations: "ADDITIONS: none — no change is needed" fails.

Null: "ADDITIONS: none — inertia holds for all candidate additions."

**Schema L — REMOVALS and REPRIORITIZATIONS**
| # | Action | Dimension | Delta finding ref | Evidence artifact | Before | After | If unchanged | Inertia Rejected Because (MANDATORY) |
|---|--------|-----------|-------------------|-------------------|--------|-------|-------------|--------------------------------------|
| ?? | ?? | ?? | ?? | ?? | ?? | ?? | ?? | ?? |

Action must be exactly REMOVE or REPRIORITIZE.
"Inertia Rejected Because (MANDATORY)": identical enforcement to Schema K.
Null: "REMOVALS: none — inertia holds."
      "REPRIORITIZATIONS: none — inertia holds."

**Schema M — Defender challenge**
| Defense ID | Proposal # | Decision defended | Defensive argument | Challenge strength |
|------------|------------|-------------------|-------------------|-------------------|
| ?? | ?? | ?? | ?? | ?? |
Challenge strength: Strong / Moderate / Weak only.
Calibration check: "Calibration: ?? — ??." (rubber-stamp / balanced / over-zealous)

**Schema N — Before/after diff**
| Dimension | Before | After [evidence bracket] | Proposal ref |
|-----------|--------|--------------------------|--------------|
| ?? | ?? | ?? | ?? |
Null: "DIFF TABLE: none — no proposals; strategy.md unchanged."

---

## EXECUTION SEQUENCE

1. Fill Schema A (read strategy.md; do not write proposals yet).
2. Fill Schemas B and C (signal inventory; SIGNAL READ-LOCK activates).
3. Fill Schema D (delta partition and mandatory sentence; counts = integers).
4. Fill Schemas E, F, G, H (delta findings — one schema per category; do not merge).
5. Fill Schema I (conflict audit).
6. Fill Schema J (inertia checkpoint — before any proposal schema).
7. Fill Schemas K and L (proposals — only Schema J YES rows).
8. Fill Schema M (defender challenge + calibration check).
9. Fill Schema N (before/after diff).
10. Display confirmation gate. Stop. Wait for user reply.

---

## CONFIRMATION GATE

Scan all schemas for remaining `??` tokens before displaying.
Resolve any `??`. A remaining `??` is a detectable gap.

INERTIA CHECK: strategy.md unchanged is the leading outcome. NO is valid.

---
PENDING CONFIRMATION — strategy.md has NOT been modified.
Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table
---

Stop. Write nothing further until the user replies.

After YES or REVISED:
Write confirmed changes to strategy.md.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-05: Full Combination

**Variation axes**: All four — Inertia framing + Output format (`??` schemas) + Lifecycle emphasis (phase gates) + Phrasing register (first-person commitments)  
**Hypothesis**: Each axis addresses a distinct failure mode: inertia framing improves C-01/C-08 quality; `??` sentinels make gaps machine-detectable (C-11/C-14); phase gates enforce sequencing (C-02/C-04); first-person commitments surface violations as commitment breaches rather than rule misses. The combination should achieve broader aspirational coverage than any single-axis variation because no single mechanism can close all the failure modes simultaneously. Phase gates are the primary skeleton; schemas are the deliverable contract; first-person commitments are the enforcement register; inertia checkpoints are the recurring competitor.

```
You are running /topic:plan for the topic named in the user's message.

---

## LEADING OUTCOME AND COMMITMENTS

I am stating this before reading any file:

  The leading outcome of this skill is: strategy.md unchanged.

Inertia is the primary competitor, not a fallback. Every evidence evaluation
below asks: does this signal defeat inertia for this dimension? Where the answer
is No or Inconclusive, inertia wins. A run with zero proposals is complete.

I am making these commitments now, prior to all conditional logic:

C1: I will not write change proposals before completing delta analysis.
C2: I will not modify strategy.md without explicit user confirmation (YES/REVISED).
C3: Every "Inertia Rejected Because" cell names specific evidence — not generic claims.
C4: Every `??` in the schemas below will be replaced with a real value, or `--`.
C5: Null declarations will be type-labeled — not a single "No changes proposed."
C6: Column enumerated values are drawn from declared sets only (no prose variants).

---

## PRE-COMMITTED SCHEMAS

`??` = unfilled (must be replaced). `--` = genuinely absent.
`??` remaining in final output is a machine-detectable gap (Commitment C4).
No schema may be replaced by prose. No schema may be skipped. No two schemas merged.

**Schema A — Strategy anchor** (Phase 1 deliverable)
| Item | Value |
|------|-------|
| Strategy file path | ?? |
| STRATEGY DATE (YYYY-MM-DD) | ?? |
| Dimensions listed | ?? |
| Direct quote from strategy.md | ?? |

**Schema B — Signal inventory** (Phase 2 deliverable)
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|
| ?? | ?? | ?? | ?? |

**Schema C — Namespace audit** (Phase 2 deliverable — all 9 rows required)
| Namespace | Count | NEW count | Coverage |
|-----------|-------|-----------|----------|
| scout   | ?? | ?? | ?? |
| draft   | ?? | ?? | ?? |
| review  | ?? | ?? | ?? |
| flow    | ?? | ?? | ?? |
| trace   | ?? | ?? | ?? |
| prove   | ?? | ?? | ?? |
| listen  | ?? | ?? | ?? |
| program | ?? | ?? | ?? |
| topic   | ?? | ?? | ?? |

**Schema D — Delta summary** (Phase 3 sole deliverable)
| List | Artifacts |
|------|-----------|
| NEW (date > STRATEGY DATE) | ?? |
| PRIOR (date <= STRATEGY DATE) | ?? |

Mandatory sentence: "Strategy was written on ??. ?? artifacts are NEW. ?? are PRIOR."
Counts must be integers. "Several", "a few", "some" = gate failure (Commitment C4).

SIGNAL READ-LOCK: Signal files may not be re-read after Schema D is written.
All subsequent phases use the written inventory only.

**Schema E — CONFIRMED** (Phase 4 deliverable)
| Finding ID | Existing assumption | Confirmed by | Citation | Delta-candidate |
|------------|--------------------|--------------|---------:|----------------|
| ?? | ?? | ?? | [Source: ??] Understanding changed: ?? -> ?? | ?? |
Null (Commitment C5): "CONFIRMED: none — no NEW artifacts confirm existing assumptions."

**Schema F — EXPANDED** (Phase 4 deliverable)
| Finding ID | Existing assumption | Expanded to | Citation | Delta-candidate |
Null: "EXPANDED: none — no NEW artifacts expand existing assumptions."

**Schema G — UNEXPECTED** (Phase 4 deliverable)
| Finding ID | Strategy gap | Signal revealed | Citation | Delta-candidate |
Null: "UNEXPECTED: none — no NEW artifacts reveal uncovered dimensions."

**Schema H — CHALLENGED** (Phase 4 deliverable)
| Finding ID | Strategy assumed | Signal challenges | Citation | Delta-candidate |
Null: "CHALLENGED: none — no NEW artifacts challenge existing strategy."

**Schema I — Conflict audit** (Phase 5 deliverable)
| Conflict ID | Signal A | Signal B | Nature of conflict | Resolution |
|-------------|----------|----------|-------------------|------------|
| ?? | ?? | ?? | ?? | ?? |
Null: "CONFLICT AUDIT: none — no contradictions detected between NEW artifacts."

**Schema J — ADDITIONS** (Phase 6 deliverable)
| # | Dimension | Delta finding ref | Evidence artifact | Before | After | If unchanged | Inertia Rejected Because (MANDATORY) |
|---|-----------|-------------------|-------------------|--------|-------|-------------|--------------------------------------|
| ?? | ?? | ?? | ?? | ?? | ?? | ?? | ?? |

"Inertia Rejected Because (MANDATORY)": one sentence of specific evidence (Commitment C3).
BANNED phrases (Commitment C3, applies to all cells AND null declarations):
"compelling reason", "clearly warranted", "obvious improvement", "no change needed",
"update is needed", "evidence suggests", "the data shows".
Null: "ADDITIONS: none — inertia holds for all candidate additions."

**Schema K — REMOVALS and REPRIORITIZATIONS** (Phase 6 deliverable)
| # | Action | Dimension | Delta finding ref | Evidence artifact | Before | After | If unchanged | Inertia Rejected Because (MANDATORY) |
|---|--------|-----------|-------------------|-------------------|--------|-------|-------------|--------------------------------------|
| ?? | ?? | ?? | ?? | ?? | ?? | ?? | ?? | ?? |

Action (Commitment C6): REMOVE or REPRIORITIZE only.
"Inertia Rejected Because (MANDATORY)": identical enforcement to Schema J.
Null: "REMOVALS: none — inertia holds."
      "REPRIORITIZATIONS: none — inertia holds."

**Schema L — Defender challenge** (Phase 6 deliverable)
| Defense ID | Proposal # | Decision defended | Defensive argument | Challenge strength |
|------------|------------|-------------------|-------------------|-------------------|
| ?? | ?? | ?? | ?? | ?? |
Challenge strength (Commitment C6): Strong / Moderate / Weak only.
Calibration check: "Calibration: ?? — ??." (rubber-stamp / balanced / over-zealous)

**Schema M — Before/after diff** (Phase 7 deliverable)
| Dimension | Before | After [evidence bracket] | Proposal ref |
|-----------|--------|--------------------------|--------------|
| ?? | ?? | ?? | ?? |
Null: "DIFF TABLE: none — no proposals; strategy.md unchanged."

---

## PHASE EXECUTION

**Phase 1 — Strategy read**
Fill Schema A. Quote one complete sentence from strategy.md verbatim.
**Exit gate (C1)**: Schema A complete, STRATEGY DATE recorded. Advance to Phase 2.

**Phase 2 — Signal inventory**
Fill Schemas B and C. All 9 namespace rows required.
**Exit gate**: All 9 namespace rows filled; SIGNAL READ-LOCK stated. Advance to Phase 3.

**Phase 3 — Delta summary**
Fill Schema D and write the mandatory sentence. This phase produces nothing else.
**Exit gate**: Counts are integers; mandatory sentence present. Advance to Phase 4.

**Phase 4 — Delta findings**
Fill Schemas E, F, G, H. Do not merge. Include two-part citations in all entries.
**Exit gate**: All four schemas present (null declarations acceptable). Advance to Phase 5.

**Phase 5 — Conflict audit**
Fill Schema I.
**Exit gate**: Schema I present. Advance to Phase 6.

**Phase 6 — Proposals**

  INERTIA CHECK (Commitment C1): I am applying the inertia prior now.
  strategy.md unchanged is the leading outcome. Only Delta-candidate: Yes
  findings from Phase 4 generate proposal rows.

Fill Schemas J, K, L. Evidence artifacts must come from Schema D NEW list only.
**Exit gate**:
  - [ ] All three change-type null declarations present (Commitment C5)
  - [ ] All evidence artifacts in Schemas J and K appear in Schema D NEW list
  - [ ] No banned phrases in any "Inertia Rejected Because" cell or null declaration (Commitment C3)
  - [ ] Schema L calibration check present
  Advance to Phase 7.

**Phase 7 — Before/after diff**
Fill Schema M for each proposed change.
**Exit gate**: Schema M present. Advance to Phase 8.

**Phase 8 — Confirmation gate**

Scan all schemas for remaining `??` (Commitment C4). Resolve before displaying.

INERTIA CHECK (Commitment C2): strategy.md has NOT been modified.
NO is a complete and valid outcome.

---
PENDING CONFIRMATION — strategy.md has NOT been modified.
Proposed: [N] additions / [N] removals / [N] reprioritizations

Individual proposals may be withdrawn: WITHDRAW [#] before confirming.

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table
---

I am stopping here per Commitment C2. I will write nothing further until
the user replies.

After YES or REVISED:
Write confirmed changes to strategy.md.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## Variation Summary

| Variation | Axis | Key mechanism | Predicted strength |
|-----------|------|---------------|--------------------|
| V-01 | Inertia framing | Named inertia competitor; inertia checkpoint schema before proposals | C-01, C-08 |
| V-02 | Phrasing register | 7 first-person commitments; gate as commitment breach vs. rule miss | C-01, C-04, C-05 |
| V-03 | Lifecycle emphasis | 8 named phases; per-phase exit gates with checklists | C-02, C-04, C-10 |
| V-04 | Inertia + Output format | `??` sentinels + Schema J (inertia adjudication per dimension) | C-01, C-08, C-11, C-14 |
| V-05 | Full combination | Phase skeleton + `??` schemas + commitments + inertia checkpoints + banned phrases | C-01 through C-14 breadth |

**Notable design choices relative to Round 3**:
- V-01 adds Schema J (inertia checkpoint as a named output table) — not present in any R3 variation
- V-02 avoids compliance manifests entirely; tests whether first-person framing alone achieves gate reliability
- V-03 moves conflict audit (C-10, the universal R3 failure) into an explicit phase with its own exit gate
- V-04 combines the R3 V-05 `??` mechanism with a per-dimension inertia adjudication record
- V-05 merges all: the Phase 6 exit gate bundles C-03, C-05, C-06, C-09, and inertia in one checklist
