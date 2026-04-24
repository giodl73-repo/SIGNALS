# topic-plan — Round 9 Variations (v8 rubric)

**Skill**: `topic:plan`
**Rubric**: v8 (C-01–C-33, 215 pts total)
**Date**: 2026-03-15

---

## Round 9 Design Notes

R8 set the ceiling at V-05 with the full C-28+C-29+C-30+C-31 stack. The two new v8 criteria
split across two precision layers:

- **Temporal depth** (C-32): three-value reversibility taxonomy — how fast the deferral window
  closes, not just what degrades
- **Pre-reading contract coverage** (C-33): assumption table's *implicit evidence* column
  must appear in the upfront schema block, not only at the extraction step

**What R8 achieved and where gaps remain:**

| Criterion | Best R8 mechanism | Gap R9 must close |
|-----------|-------------------|-------------------|
| C-32 | `★ Reversibility` in upfront schema; three values defined in a prose block *below* the Step 6 table | Enumeration defined adjacent-below, not in-column-header; upfront schema's Reversibility column carries no closed-enum annotation; prose fill ("it will be harder") not structurally blocked |
| C-33 | Full 5-column assumption table in upfront schema in V-04 and V-05 | C-33 requires "implicit evidence" column — what text in strategy.md implies each assumption. R8 V-05's five columns are: ID + assumption + back-fill + delta-relevance + candidate. The "implicit evidence" column — where in strategy.md the assumption is evidenced — is absent from both the upfront schema and the extraction step |

**Clarification on C-33's five-column schema:**

C-33 parenthetical: *(extracted assumption, implicit evidence, 'Contradicted by a signal?'
back-fill, delta-relevance, delta-candidate designation).*

This maps to:
1. **Extracted assumption** — what strategy.md assumed without writing
2. **Implicit evidence** — the phrase or passage in strategy.md that reveals the assumption
   existed (the archaeology citation)
3. **Contradicted by a signal?** — back-fill, filled after Step 2
4. **Delta-relevance** — why this matters for delta detection (failure mode if wrong)
5. **Delta-candidate designation** — yes/no with F-NN cross-reference after Step 3

R8 V-05's "Assumption ID" is a row key, not one of the five content columns. The "implicit
evidence" column is missing from every R8 variation — it is the new discriminator for C-33.

**Three single-axis dimensions explored in R9:**

1. **Output format (C-32)**: The reversibility column header in both the upfront schema and the
   Step 6 template includes the three-value closed enum as an inline selector — "(1) Reversible
   at same cost / (2) Gets harder / (3) Becomes impossible — select one; prose is not a valid
   value" — making ambiguous prose structurally non-compliant at the point of fill.

2. **Lifecycle emphasis (C-33)**: The extraction step explicitly names the "Implicit evidence"
   column as a citation act: "find the phrase in strategy.md that implies this assumption;
   leave blank only if no strategy text implies it." The column is declared in the upfront schema
   and executed as a distinct cognitive act at Step 1b.

3. **Phrasing register (C-32)**: The reversibility column uses a decision-question format —
   "Can we defer this safely? Select: [A] Yes, same cost / [B] Yes, but harder / [C] No,
   window closes permanently" — activating temporal-consequence reasoning through outcome
   framing rather than taxonomy-label selection.

**Variation design:**

| Variation | Axis | Type | Primary R9 target |
|-----------|------|------|-------------------|
| V-01 | Output format — closed-enum Reversibility in column header | Single | C-32 |
| V-02 | Lifecycle emphasis — Implicit evidence column at extraction | Single | C-33 |
| V-03 | Phrasing register — decision-question reversibility framing | Single | C-32 |
| V-04 | Output format + Lifecycle — enum lock + implicit evidence + schema-first | Combination | C-32 + C-33 |
| V-05 | Full stack — R8 V-05 base + C-32 enum lock + C-33 implicit evidence | Combination | C-32 + C-33 + all R8 ceiling |

---

## V-01 — Closed-Enum Reversibility in Column Header

**Axis**: Output format — the Reversibility column definition includes the three-value closed
enum in both the upfront schema and the Step 6 column header, blocking prose fill at the
structural level

**Hypothesis**: R8 V-05 defined the reversibility values in a prose block below the Step 6
table template — the model sees the value set only after writing the column header, under
context pressure from all prior execution. If the three values appear inside the column header
itself — "(1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible — select one;
prose is not a valid value" — the model cannot fill the cell without confronting the enum
constraint. The upfront schema's Proposals row carries the same inline annotation, committing
the model to the closed set before reading any files. The hypothesis is that in-header
enumeration prevents ambiguous prose by making the column a structural selector rather than a
free-text field. This variation intentionally omits the implicit evidence column (C-33) to
isolate the C-32 mechanism; the assumption table uses R8 V-01's full 5-column schema without
the new column.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it was
written. The assumption table you build in Step 1b is a complete two-way bridge — backward from
strategy beliefs to signal evidence (back-fill after Step 2), and forward to delta findings and
proposals (candidate designation updated after Step 3). Present proposals, wait for
confirmation, then write. Do not auto-apply changes.

---

### Output Schema (read before proceeding to Step 1)

Every table you produce must conform to this schema. Columns marked ★ are mandatory — do not
omit any ★ column.

**Assumption Table** (5 columns mandatory)
| ★ Assumption ID | ★ What assumed | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? |

**Signal Inventory**
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? | ★ Assumption link |

**Delta Findings**
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) | ★ Assumption root |

**Namespace Audit**
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |

**Conflict Audit**
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals** — the Reversibility column requires selecting exactly one enumerated value; prose
is not a valid value:
| ★ Proposal ID | ★ Type | ★ Change | ★ Delta Finding | ★ Evidence | ★ If unchanged | ★ Reversibility [(1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible] | ★ Confidence |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

Do not omit any ★ column.

---

### Step 1a — Read strategy.md: Stated Fields

Read `simulations/{topic}/strategy.md`.

**The following columns are mandatory. Do not omit any column.**

| Field | Value |
|-------|-------|
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Stated rationale | |
| Acknowledged gaps | |

---

### Step 1b — Build the Assumption Table

Your job is to find what strategy.md took for granted without writing. These are the
highest-value delta candidates — a signal can contradict what was assumed, not only what was
stated.

Scan across at least five dimensions: (a) implied audience knowledge level, (b) namespace
priority ordering, (c) signal sufficiency threshold, (d) timeline or sequencing feasibility,
(e) what "done" means in this context. Add others if found.

**The following columns are mandatory. Do not omit any column.**

Column rules:
- **"Contradicted by a signal?"**: Write `[pending]` as placeholder now. Return here after
  Step 2 and populate with a signal-grounded verdict.
- **"Why this matters for delta detection"**: Fill now. Name the specific failure mode if this
  assumption is wrong — which skills or namespaces would change priority.
- **"Delta candidate?"**: Fill now. Write `yes` if contradicting this assumption would change
  strategy direction; `no` if it would not. After Step 3, update `yes` rows to `yes — F-NN`.

| Assumption ID | What strategy.md assumed without writing | Contradicted by a signal? | Why this matters for delta detection | Delta candidate? |
|--------------|------------------------------------------|--------------------------|--------------------------------------|-----------------|
| A-01 | [most important — highest likelihood of signal contradiction] | [pending] | [specific failure mode if wrong] | yes / no |
| A-02 | [second assumption, if any] | [pending] | | yes / no |

Write at least one row. Null case:

| A-00 | No unstated assumptions found after systematic scan | N/A | N/A | no |

---

### Step 2 — Read signal artifacts

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals found** — reproduce the following verbatim and stop. Do not omit:

> No signals found — strategy.md does not need revision at this time.

**The following columns are mandatory. Do not omit any column.**

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? | Assumption link (A-NN / "stated field" / "none") |
|----|------|-----------|-------|------|--------------------------|---------------------------|--------------------------------------------------|
| S-01 | | | | | | Yes / No / Partial | |

**After building this table, return to Step 1b and fill "Contradicted by a signal?" for each
A-NN row.** For each contradicted assumption: cite the S-NN ID and write one sentence on the
contradiction. For uncontradicted: "Not contradicted — assumption stands." For uncovered:
"No signal coverage."

---

### Step 3 — Identify the delta

Stop. Before building the findings table, write the name of the anti-pattern you are guarding
against at this step.

**The following columns are mandatory. Do not omit any column.**

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root (A-NN / "stated field") |
|-----------|-----------------|----------------|-----------------|----------------------------------------|
| F-01 | [from Step 1a stated fields or Step 1b assumptions] | | S-XX | |

After building findings, return to Step 1b and update "Delta candidate?" — change `yes` to
`yes — F-NN` for rows that produced a finding.

**Null case — all signals confirm** — reproduce verbatim and skip to Step 5:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root |
|-----------|-----------------|----------------|-----------------|-----------------|
| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |

---

### Step 4 — Namespace coverage audit

Assess all 9 namespaces by name. "Stage-relative" = appropriate for the topic's current stage,
not a raw count.

**The following columns are mandatory. Do not omit any column.**

| Namespace | Signal Count | Stage-Relative Status | Action Needed? |
|-----------|-------------|----------------------|----------------|
| scout | | | |
| draft | | | |
| review | | | |
| flow | | | |
| trace | | | |
| prove | | | |
| listen | | | |
| program | | | |
| topic | | | |

---

### Step 5 — Conflict audit

Look for signals pointing in opposite directions on the same dimension.

**The following columns are mandatory. Do not omit any column.**

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

**Null case — no conflicts** — reproduce verbatim. Do not omit this table:

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

---

### Step 6 — Proposals

**The following columns are mandatory. Do not omit any column.**

For the Reversibility column: select exactly one enumerated value per content row. Do not write
prose. No other value is valid.

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Reversibility [(1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible — select one] | Confidence |
|------------|------|--------|--------------|-------------------|-------------|------------------------------------------------------------------------------------------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [specific gap that persists or worsens if deferred] | (2) Gets harder | High |

All three types (ADD, REMOVE, REPRIORITIZE) must appear. Reproduce null rows verbatim:

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Reversibility | Confidence |
|------------|------|--------|--------------|-------------------|-------------|--------------|------------|
| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

Delta Finding must reproduce the full "Strategy assumed [X] / Signal revealed [Y]" text from
Step 3 with exact Finding ID. Every Proposal ID must trace back through its Delta Finding to an
Assumption root (A-NN or "stated field").

---

### Step 7 — Before/after diff

Before building the diff table, write the following statement verbatim:

> "Diff schema: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★ (inline as
> [file.md — ≤10 word finding] — no separate section), Proposal ★ (Proposal ID from Step 6).
> No column omitted."

**The following columns are mandatory. Do not omit any column.**

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current strategy text] | [proposed text] | [file.md — ≤10 word finding] | ADD-1 |

---

### Step 8 — Confirmation gate

Reply **YES** to apply all proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 9 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals. Preserve
existing structure; update only sections affected by confirmed changes.

---

## V-02 — Implicit Evidence Column at Extraction

**Axis**: Lifecycle emphasis — the assumption extraction step adds an "Implicit evidence" column
requiring the model to cite the specific strategy text that implies each assumption, declared in
the upfront schema before any file reading

**Hypothesis**: R8 V-01 through V-05 declared the assumption extraction column as "What
strategy.md assumed without writing" — the assumption itself. C-33 requires an additional
column: "implicit evidence" — the text or passage in strategy.md that reveals the assumption
existed. Without this column, assumptions can be inferred from whole-document patterns without
any auditable citation; the model can name an assumption it inferred from the document's tone
or emphasis without grounding it in a specific phrase. If the "Implicit evidence" column
requires citing the strategy text that implies the assumption — even a short phrase — the
model's extraction becomes auditable: a reviewer can verify the assumption was present by
reading the cited passage. The hypothesis is that forcing a citation at extraction time not only
satisfies C-33 but changes which assumptions are named: shallow assumptions (not evidenced in
the text) are filtered out, and load-bearing assumptions (explicitly evidenced but never
explicitly stated as premises) surface. This variation uses R8 V-02 as the base (schema-first
priming, adjacent disqualification rule), adds the "Implicit evidence" column, and intentionally
keeps Reversibility as just `★ Reversibility` without the closed-enum annotation to isolate C-33.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it was
written. Present proposals, wait for confirmation, then write. Do not auto-apply changes.

**Before reading any files, review the complete output schema below.** Every table you produce
must conform to this schema. Columns marked ★ are mandatory — do not omit any ★ column.

---

### Output Schema (read before proceeding to Step 1)

**Assumption Table** — five content columns mandatory; the Implicit evidence column cites the
strategy text that implies each assumption:
| ★ Assumption | ★ Implicit evidence (strategy phrase implying this assumption) | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? |

**Signal Inventory**
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? | ★ Assumption link |

**Delta Findings**
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) | ★ Assumption root |

**Namespace Audit**
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |

**Conflict Audit**
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals**
| ★ Proposal ID | ★ Type | ★ Change | ★ Delta Finding | ★ Evidence | ★ If unchanged | ★ Reversibility | ★ Confidence |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

Do not omit any ★ column. A table missing any ★ column fails schema validation.

---

### Step 1 — Read strategy.md

Read `simulations/{topic}/strategy.md`. Extract stated fields and unstated assumptions.

**Stated fields** — the following columns are mandatory. Do not omit any column:

| Field | Value |
|-------|-------|
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Stated rationale | |
| Acknowledged gaps | |

**Unstated assumptions** — per schema (Assumption Table). The following columns are mandatory.
Do not omit any column. "Contradicted?" is filled after Step 2 — write `[pending]` as
placeholder. "Implicit evidence" is filled now — cite the strategy.md phrase that implies the
assumption:

| Assumption | Implicit evidence (strategy phrase implying this assumption) | Contradicted by a signal? | Why this matters for delta detection | Delta candidate? |
|-----------|--------------------------------------------------------------|--------------------------|--------------------------------------|-----------------|
| [most important for delta detection] | [short phrase from strategy.md that implies this assumption existed — leave blank only if no strategy text implies it] | [pending] | [failure mode if wrong] | yes / no |

Write at least one row.

---

### Step 2 — Read signal artifacts

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals found** — reproduce the following verbatim and stop. Do not omit:

> No signals found — strategy.md does not need revision at this time.

Per schema (Signal Inventory) — the following columns are mandatory. Do not omit any column:

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? | Assumption link (A-NN / "stated field" / "none") |
|----|------|-----------|-------|------|--------------------------|---------------------------|--------------------------------------------------|
| S-01 | | | | | | Yes / No / Partial | |

After building this table, return to Step 1 and fill "Contradicted by a signal?" for each
assumption row.

---

### Step 3 — Identify the delta

Stop. Before building the findings table, write the name of the anti-pattern you are guarding
against at this step. Then write one sentence: what the delta IS vs. what it IS NOT.

Per schema (Delta Findings) — the following columns are mandatory. Do not omit any column:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root |
|-----------|-----------------|----------------|-----------------|-----------------|
| F-01 | | | S-XX | |

**Null case — all signals confirm** — reproduce verbatim and skip to Step 5:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root |
|-----------|-----------------|----------------|-----------------|-----------------|
| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |

---

### Step 4 — Namespace coverage audit

Per schema (Namespace Audit) — the following columns are mandatory. Do not omit any column:

| Namespace | Signal Count | Stage-Relative Status | Action Needed? |
|-----------|-------------|----------------------|----------------|
| scout | | | |
| draft | | | |
| review | | | |
| flow | | | |
| trace | | | |
| prove | | | |
| listen | | | |
| program | | | |
| topic | | | |

---

### Step 5 — Conflict audit

Per schema (Conflict Audit) — the following columns are mandatory. Do not omit any column:

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

**Null case — no conflicts** — reproduce verbatim. Do not omit this table:

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

---

### Step 6 — Proposals

Before building the proposals table, write the following statement verbatim:

> "Proposals schema committed: Proposal ID ★, Type ★, Change ★, Delta Finding ★ (full
> 'Strategy assumed [X] / Signal revealed [Y]' text from Step 3 with exact ID), Evidence ★,
> If unchanged ★ (specific degradation — a row that cannot name a specific degradation here is
> a preference, not a decision), Reversibility ★, Confidence ★. All three types present.
> Empty types use null rows."

Per schema (Proposals) — the following columns are mandatory. Do not omit any column.

**Column rule for "If unchanged"**: Name the specific artifact that won't be gathered, the
decision that becomes harder, or the gap that compounds.

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged [a row that cannot name a specific degradation here is a preference, not a decision] | Reversibility | Confidence |
|------------|------|--------|--------------|-------------------|----------------------------------------------------------------------------------------------------|--------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [specific gap that persists or worsens if deferred] | Gets harder | High |

Null rows (reproduce verbatim for each empty type):

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Reversibility | Confidence |
|------------|------|--------|--------------|-------------------|-------------|--------------|------------|
| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 7 — Before/after diff

Before building the diff table, write the following statement verbatim:

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★
> (inline per row as [file.md — ≤10 word finding] — no separate evidence section),
> Proposal ★ (Proposal ID from Step 6)."

Per schema (Diff) — the following columns are mandatory. Do not omit any column:

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current strategy text] | [proposed text] | [file.md — ≤10 word finding] | ADD-1 |

---

### Step 8 — Confirmation gate

Reply **YES** to apply all proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 9 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals. Preserve
existing structure; update only sections affected by confirmed changes.

---

## V-03 — Decision-Question Reversibility (Conversational Register)

**Axis**: Phrasing register — the Reversibility column replaces taxonomy-label selection with a
forced-choice decision question: "Can we defer this safely?", activating temporal-consequence
reasoning through outcome framing rather than classification

**Hypothesis**: R8 V-05 listed reversibility values as labels — "Reversible at same cost /
Gets harder / Becomes impossible" — that the model selects from. C-32's distinction between
"Gets harder" and "Becomes impossible" requires the model to reason about whether a constraint
is a ratchet (escalating cost) or a hard stop (permanent closure). A taxonomy label invites
classification from memory; a decision question invites consequence reasoning. "Can we defer
this safely?" with three forced-choice answers — [A] Yes, same cost; [B] Yes, but harder; [C]
No, window closes permanently — frames the column as a decision to be reasoned rather than a
category to be assigned. The distinction between [B] and [C] is now: "will it cost more, but
remain open?" vs. "will it close?" — a question the model must answer by examining the
specific constraint, not labeling its magnitude. This variation uses R8 V-03 (named lifecycle
phases, Archaeologist role, back-fill as named step) as its base. It intentionally omits the
implicit evidence column (C-33) and the upfront schema priming (C-26) to isolate whether
decision-question framing alone closes the C-32 prose gap.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it was
written. The assumption table has a two-phase lifecycle: extraction (Step 1b) and back-fill
(Step 2b). Each phase is a distinct cognitive act — do not conflate them. Present proposals,
wait for confirmation, then write. Do not auto-apply changes.

---

### Step 1a — Read strategy.md: Stated Fields

Read `simulations/{topic}/strategy.md`.

**The following columns are mandatory. Do not omit any column.**

| Field | Value |
|-------|-------|
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Stated rationale | |
| Acknowledged gaps | |

---

### Step 1b — Role: Assumption Archaeologist — Extract phase

**Adopt this role**: You are an assumption archaeologist. Your job is to find what strategy.md
took for granted without writing — the implied worldview, the unstated preconditions, the
beliefs the author would defend if challenged but never put in the document.

Systematic scan — cover each dimension:
- (a) Implied audience knowledge level
- (b) Namespace priority ordering assumed without justification
- (c) Signal sufficiency threshold — what "enough signals" means here
- (d) Timeline or sequencing feasibility
- (e) Definition of "done" for this topic

**The following columns are mandatory. Do not omit any column. The "Contradicted?" column is
filled in Step 2b — not now. Write `[pending]` as placeholder.**

| Assumption ID | What strategy.md assumed without writing | Contradicted? [pending — filled in Step 2b] | Why this matters for delta detection | Delta candidate? |
|--------------|------------------------------------------|---------------------------------------------|--------------------------------------|-----------------|
| A-01 | [most important — highest likelihood of signal contradiction] | pending | [failure mode if wrong] | yes / no |
| A-02 | [second assumption, if any] | pending | | yes / no |

Write at least one row. Null case: A-00 "No unstated assumptions found after systematic scan."

---

### Step 2a — Role: Signal Analyst — Read phase

**Adopt this role**: You are a signal analyst. Read every artifact against two reference points:
(a) stated fields from Step 1a, and (b) assumptions from Step 1b. The "Assumption link" column
maps each signal to the reference point it speaks to most directly.

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals found** — reproduce the following verbatim and stop. Do not omit:

> No signals found — strategy.md does not need revision at this time.

**The following columns are mandatory. Do not omit any column.**

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? | Assumption link (A-NN / "stated field" / "none") |
|----|------|-----------|-------|------|--------------------------|---------------------------|--------------------------------------------------|
| S-01 | | | | | | Yes / No / Partial | |

---

### Step 2b — Role: Assumption Archaeologist — Back-fill phase

**Return to this role**: You are back as the assumption archaeologist. Now that you have read
all signals, adjudicate every assumption from Step 1b against the signal evidence.

For each A-NN row, replace `pending` with exactly one of the following verdicts. Do not leave
any row as `pending`:

- **Contradicted — S-NN**: A signal directly challenges this assumption. Cite the signal ID.
  Write one sentence on the contradiction.
- **Supported — S-NN**: A signal confirms this assumption. Cite the signal ID.
- **No signal coverage**: No artifact in the current set speaks to this assumption.

Reproduce the full updated assumption table. Every row must have a verdict.

---

### Step 3 — Role: Delta Identifier

**Adopt this role**: Name the gap between strategy beliefs and signal evidence.

Stop. Before building the findings table, write the name of the anti-pattern you are guarding
against at this step.

**The following columns are mandatory. Do not omit any column.**

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root (A-NN / "stated field") |
|-----------|-----------------|----------------|-----------------|----------------------------------------|
| F-01 | [from Step 1a stated fields or Step 1b assumptions marked Contradicted] | | S-XX | |

After building findings, return to Step 2b and update "Delta candidate?" — change `yes` to
`yes — F-NN` for rows that produced a finding.

**Null case** — reproduce verbatim and skip to Step 5:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root |
|-----------|-----------------|----------------|-----------------|-----------------|
| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |

---

### Step 4 — Role: Coverage Auditor

**Adopt this role**: Assess all 9 namespaces by name for stage-relative completeness.

**The following columns are mandatory. Do not omit any column.**

| Namespace | Signal Count | Stage-Relative Status | Action Needed? |
|-----------|-------------|----------------------|----------------|
| scout | | | |
| draft | | | |
| review | | | |
| flow | | | |
| trace | | | |
| prove | | | |
| listen | | | |
| program | | | |
| topic | | | |

---

### Step 5 — Role: Conflict Detective

**Adopt this role**: Find pairs of artifacts pointing in opposite directions on the same
dimension.

**The following columns are mandatory. Do not omit any column.**

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

**Null case** — reproduce verbatim. Do not omit this table:

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

---

### Step 6 — Role: Proposal Architect

**Adopt this role**: Translate each finding into a typed, defensible proposal.

**The following columns are mandatory. Do not omit any column.**

For the **Reversibility** column: answer the question "Can we defer this safely?" by selecting
exactly one of:
- **[A] Yes, same cost** — deferring does not increase the effort to close this gap later
- **[B] Yes, but harder** — the gap compounds; closing later costs more effort or more signals
- **[C] No, window closes permanently** — deferral makes this gap unrecoverable

Do not write prose. If you cannot select A, B, or C, the reversibility of deferral has not been
reasoned through.

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Reversibility [A/B/C — see above] | Confidence |
|------------|------|--------|--------------|-------------------|--------------|------------------------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [specific gap that persists or worsens] | B | High |

All three types must appear. Reproduce null rows verbatim:

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Reversibility | Confidence |
|------------|------|--------|--------------|-------------------|-------------|--------------|------------|
| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 7 — Role: Diff Author

**Adopt this role**: Show the exact before/after for every confirmed proposal.

Before building the diff table, write the following statement verbatim:

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★
> (inline per row as [file.md — ≤10 word finding] — no separate evidence section),
> Proposal ★ (Proposal ID from Step 6)."

**The following columns are mandatory. Do not omit any column.**

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current strategy text] | [proposed text] | [file.md — ≤10 word finding] | ADD-1 |

---

### Step 8 — Confirmation gate

Reply **YES** to apply all proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 9 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals. Preserve
existing structure; update only sections affected by confirmed changes.

---

## V-04 — Closed-Enum + Implicit Evidence + Schema-First

**Axes**: Output format (V-01: closed-enum Reversibility in column header) + Lifecycle emphasis
(V-02: Implicit evidence column at extraction) + Schema-first priming (C-26: complete output
schema declared before file reading)

**Hypothesis**: V-01 locks C-32 via enum constraint in the column header but leaves C-33 open
(no implicit evidence column). V-02 closes C-33 via the implicit evidence column but leaves
C-32 open (no enum constraint). V-04 combines both mechanisms with schema-first priming: the
upfront Output Schema block declares the Reversibility column with the three-value enum AND the
Assumption Table with the implicit evidence column — both structural contracts are committed
before the model reads a single file. The combination matters because both C-32 and C-33 are
pre-reading contract criteria: C-32 requires the model to hold the three-value taxonomy before
encountering any proposal scenario; C-33 requires the model to hold the assumption table schema
(including implicit evidence) before encountering strategy.md. Schema-first priming makes both
constraints available for compliance evaluation before context pressure begins. This variation
uses R8 V-04 (output format + role sequence + schema-first) as its base and intentionally omits
the R8 V-05 cascade checkpoints (C-27) to isolate the C-32+C-33 combination from the
checkpoint mechanism.

---

You are executing `topic:plan` for the topic `{topic}`.

**Before reading any files, review the complete output schema below.** Every table you produce
must conform to this schema. Columns marked ★ are mandatory — do not omit any ★ column. You
will adopt a named cognitive role at each phase. The structural contract below governs output
regardless of role.

---

### Output Schema (read before proceeding to Step 1)

**Assumption Table** — five content columns mandatory; the Implicit evidence column is a
citation of the strategy.md text that implies each assumption:
| ★ Assumption | ★ Implicit evidence (strategy phrase implying this assumption) | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? |

**Signal Inventory**
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? | ★ Assumption link |

**Delta Findings**
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) | ★ Assumption root |

**Namespace Audit**
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |

**Conflict Audit**
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals** — Reversibility requires exactly one enumerated value; prose is not valid:
| ★ Proposal ID | ★ Type | ★ Change | ★ Delta Finding | ★ Evidence | ★ If unchanged | ★ Reversibility [(1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible] | ★ Confidence |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

**Traceability obligation**: Every Proposal row must trace backward — Diff (Proposal ID) →
Proposals (Delta Finding) → Delta Findings (Finding ID) → Assumption Table (Assumption root).
Every chain hop must be filled.

Do not omit any ★ column.

---

### Step 1a — Role: Stated-Field Extractor

**Adopt this role**: Extract only what strategy.md wrote explicitly. Do not interpret, infer,
or supplement.

Read `simulations/{topic}/strategy.md`.

**The following columns are mandatory. Do not omit any column.**

| Field | Value |
|-------|-------|
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Stated rationale | |
| Acknowledged gaps | |

---

### Step 1b — Role: Assumption Archaeologist — Extract phase

**Adopt this role**: You are an assumption archaeologist. Find what strategy.md took for
granted without writing — the implied worldview, the unstated preconditions, the beliefs the
author would defend if challenged but never put in the document. These are the highest-value
delta candidates.

For each assumption you find, you must do two things: (1) name the assumption, and (2) cite the
specific strategy.md phrase or passage that implies it existed. An assumption with no strategy
text implying it is an inference you imposed — not an assumption the strategy made. Leave the
"Implicit evidence" cell blank only if no strategy text implies the assumption after systematic
scan.

Systematic scan — cover each dimension explicitly:
- (a) Implied audience knowledge level
- (b) Namespace priority ordering assumed without justification
- (c) Signal sufficiency threshold — what "enough signals" means here
- (d) Timeline or sequencing feasibility
- (e) Definition of "done" for this topic

Per schema (Assumption Table) — all five columns are mandatory. Do not omit any column.

Column rules:
- **"Contradicted by a signal?"**: Write `[pending]` now. Filled in Step 2b.
- **"Why this matters for delta detection"**: Fill now. Which skills or namespaces would change
  priority if this assumption is wrong?
- **"Delta candidate?"**: Fill now. `yes` if contradicting would change strategy direction; `no`
  if not. After Step 3, update `yes` rows to `yes — F-NN`.

| Assumption | Implicit evidence (strategy phrase implying this assumption) | Contradicted by a signal? | Why this matters for delta detection | Delta candidate? |
|-----------|--------------------------------------------------------------|--------------------------|--------------------------------------|-----------------|
| [most important for delta detection] | [short phrase from strategy.md] | [pending] | [failure mode if wrong] | yes / no |
| [second assumption, if any] | [strategy phrase, or leave blank if none found] | [pending] | | yes / no |

Write at least one row. Null case: "No unstated assumptions found after systematic scan."

---

### Step 2a — Role: Signal Analyst — Read phase

**Adopt this role**: Read every artifact against two reference points: (a) stated fields from
Step 1a, and (b) assumptions from Step 1b. Map each signal to its reference point.

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals found** — reproduce the following verbatim and stop. Do not omit:

> No signals found — strategy.md does not need revision at this time.

Per schema (Signal Inventory) — the following columns are mandatory. Do not omit any column:

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? | Assumption link (A-NN / "stated field" / "none") |
|----|------|-----------|-------|------|--------------------------|---------------------------|--------------------------------------------------|
| S-01 | | | | | | Yes / No / Partial | |

---

### Step 2b — Role: Assumption Archaeologist — Back-fill phase

**Return to this role**: Adjudicate every assumption from Step 1b against the full signal set.

For each assumption row, replace `[pending]` with a signal-grounded verdict — exactly one per
row. Do not leave any row as `[pending]`:

- **Contradicted — S-NN**: Signal challenges this assumption. Cite ID, one sentence.
- **Supported — S-NN**: Signal confirms this assumption. Cite ID.
- **No signal coverage**: No signal speaks to this assumption.

Reproduce the full updated Assumption Table (all 5 columns). Every row must have a verdict.

After completing Step 3, return here and update "Delta candidate?" — change `yes` to `yes — F-NN`
for rows that produced a finding.

---

### Step 3 — Role: Delta Identifier

**Adopt this role**: Name the gap between strategy beliefs and signal evidence.

**Stop. Before building the findings table, produce both:**

1. **Anti-pattern label**: Name the anti-pattern you are guarding against. Write the label.
2. **Delta definition**: Delta IS: [gap between belief and signal]. Delta IS NOT: [inventory of
   signal existence].

Per schema (Delta Findings) — the following columns are mandatory. Do not omit any column:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root |
|-----------|-----------------|----------------|-----------------|-----------------|
| F-01 | [from Step 1a stated fields or Step 1b assumptions marked Contradicted] | | S-XX | |

After completing findings, return to Step 2b and update all `yes` entries with actual F-NN IDs.

**Null case** — reproduce verbatim and skip to Step 5:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root |
|-----------|-----------------|----------------|-----------------|-----------------|
| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |

---

### Step 4 — Role: Coverage Auditor

**Adopt this role**: Assess all 9 namespaces for stage-relative completeness — not raw count.

Per schema (Namespace Audit) — the following columns are mandatory. Do not omit any column:

| Namespace | Signal Count | Stage-Relative Status | Action Needed? |
|-----------|-------------|----------------------|----------------|
| scout | | | |
| draft | | | |
| review | | | |
| flow | | | |
| trace | | | |
| prove | | | |
| listen | | | |
| program | | | |
| topic | | | |

---

### Step 5 — Role: Conflict Detective

**Adopt this role**: Find pairs of artifacts pointing in opposite directions on the same
dimension.

Per schema (Conflict Audit) — the following columns are mandatory. Do not omit any column:

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

**Null case** — reproduce verbatim. Do not omit:

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

---

### Step 6 — Role: Proposal Architect

**Adopt this role**: Translate each finding into a typed, defensible proposal. Every Proposal
ID must trace to a Finding ID (via Delta Finding) and from there to an Assumption root.

Per schema (Proposals) — the following columns are mandatory. Do not omit any column.

**Column rules:**
- **"If unchanged"**: Name the specific artifact that won't be gathered, the decision that
  becomes harder, or the gap that compounds. A row that writes a synonym of the delta finding
  here is a preference, not a decision.
- **"Reversibility"**: Select exactly one enumerated value. Do not write prose. No other value
  is valid.

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Reversibility [(1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible — select one] | Confidence |
|------------|------|--------|--------------|-------------------|--------------|----------------------------------------------------------------------------------------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [specific degradation] | (2) Gets harder | High |

Null rows (reproduce verbatim for each empty type):

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Reversibility | Confidence |
|------------|------|--------|--------------|-------------------|-------------|--------------|------------|
| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 7 — Role: Diff Author

**Adopt this role**: Show the exact before/after for every confirmed proposal. Every Proposal
ID is the entry point into the full traceability chain.

Per schema (Diff) — the following columns are mandatory. Do not omit any column:

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current strategy text] | [proposed text] | [file.md — ≤10 word finding] | ADD-1 |

---

### Step 8 — Confirmation gate

Reply **YES** to apply all proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 9 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals. Preserve
existing structure; update only sections affected by confirmed changes.

---

## V-05 — Full Stack: R8 V-05 + C-32 Enum Lock + C-33 Implicit Evidence

**Axes**: All R8 V-05 mechanisms + closed-enum Reversibility in upfront schema and column
header with disqualification rule + Implicit evidence column in upfront Assumption Table schema
and Step 1b extraction

**Hypothesis**: R8 V-05 set the ceiling with C-28+C-29+C-30+C-31. The two v8 additions are
precision gaps in the same two structural layers R8 already addressed. C-32 is to consequence
reasoning what C-31 was to inertia framing: C-31 made the "If unchanged" column a decision gate
by naming the disqualification condition adjacent to the column; C-32 makes the Reversibility
column a taxonomy gate by placing the closed-enum constraint inside the column header. The same
adjacency principle that made C-31 work makes C-32 work. C-33 is to the assumption table what
C-26 was to output tables: C-26 moved output schemas from adjacent-to-step (C-21) to upfront
pre-reading contract; C-33 does the same for the assumption table. The "implicit evidence"
column is the new element: it adds an archaeology citation requirement — not just what was
assumed, but what in strategy.md reveals the assumption existed. Both mechanisms follow the same
structural logic as their R8 predecessors: in-header placement (not adjacent prose) for enum
constraints; pre-reading declaration (not adjacent-to-step) for schema contracts. The V-05
ceiling variation tests whether both new precision mechanisms interact constructively — whether
assumption archaeology citations change which delta findings surface, and whether closed-enum
reversibility changes how proposals are defended under deferral pressure.

---

You are executing `topic:plan` for the topic `{topic}`.

**Before reading any files, review the complete output schema below.** Every table you produce
must conform to this schema. Columns marked ★ are mandatory — do not omit any ★ column. A table
missing any ★ column fails schema validation regardless of other content.

Two pre-reading commitments are made here:
1. **Assumption table schema** — five content columns including the Implicit evidence column
   (strategy phrase implying each assumption) — committed before strategy.md is read.
2. **Reversibility taxonomy** — three enumerated values; prose is not a valid value — committed
   before any proposal scenario is encountered.

---

### Output Schema (read before proceeding to Step 1)

**Assumption Table** (5 content columns — full pre-reading contract)
| ★ Assumption | ★ Implicit evidence (strategy phrase implying this assumption) | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? |

**Signal Inventory**
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? | ★ Assumption link |

**Delta Findings**
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) | ★ Assumption root |

**Namespace Audit**
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |

**Conflict Audit**
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals** — Reversibility taxonomy pre-committed: three enumerated values, no prose valid:
| ★ Proposal ID | ★ Type | ★ Change | ★ Delta Finding | ★ Evidence | ★ If unchanged | ★ Reversibility [(1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible] | ★ Confidence |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

**Traceability obligation**: Every Proposal row must be traceable backward — Diff (Proposal
ID) → Proposals (Delta Finding) → Delta Findings (Finding ID) → Assumption Table (Assumption
root). Every chain hop must be filled. Schema compliance alone is insufficient — the chain must
be walkable.

Do not omit any ★ column.

---

### Step 1a — Role: Stated-Field Extractor

**Adopt this role**: Extract only what strategy.md wrote explicitly. Do not interpret, infer,
or supplement.

Read `simulations/{topic}/strategy.md`.

**The following columns are mandatory. Do not omit any column.**

| Field | Value |
|-------|-------|
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Stated rationale | |
| Acknowledged gaps | |

---

### Step 1b — Role: Assumption Archaeologist — Extract phase

**Adopt this role**: You are an assumption archaeologist. Find what strategy.md took for
granted without writing — the implied worldview, the unstated preconditions, the beliefs the
author would defend if challenged but never put in the document. These are the highest-value
delta candidates.

Your extraction has two obligations per assumption: (1) name the assumption itself; (2) cite
the strategy.md phrase that implies it. Obligation 2 is the archaeology obligation — find the
textual evidence that the assumption was made, not merely that it could have been made. An
assumption with no strategy text implying it is an inference you imposed — leave "Implicit
evidence" blank only if no strategy text, however indirect, implies the assumption.

Systematic scan — cover each dimension. Do not skip dimensions:
- (a) Implied audience knowledge level
- (b) Namespace priority ordering assumed without justification
- (c) Signal sufficiency threshold — what "enough signals" means here
- (d) Timeline or sequencing feasibility
- (e) Definition of "done" for this topic
- (f) Any additional dimension this specific strategy reveals

Per schema (Assumption Table) — all five columns are mandatory. Do not omit any column.

Column rules:
- **"Contradicted by a signal?"**: Write `[pending]` now. Filled in Step 2b.
- **"Why this matters for delta detection"**: Fill now. If a signal contradicts this, which
  skill priorities or namespace ordering would change?
- **"Delta candidate?"**: Fill now. `yes` if contradicting would change strategy direction;
  `no` if not. After Step 3, update `yes` rows to `yes — F-NN`.

| Assumption | Implicit evidence (strategy phrase implying this assumption) | Contradicted by a signal? | Why this matters for delta detection | Delta candidate? |
|-----------|--------------------------------------------------------------|--------------------------|--------------------------------------|-----------------|
| [most important — highest likelihood of signal contradiction] | [short phrase from strategy.md — the textual clue that reveals this assumption] | [pending] | [specific failure mode: which priorities would shift?] | yes / no |
| [second assumption, if any] | [strategy phrase, or leave blank only if no text implies it] | [pending] | | yes / no |

Write at least one row. Null case: "No unstated assumptions found after systematic scan."

---

### Step 2a — Role: Signal Analyst — Read phase

**Adopt this role**: Read every artifact against two reference points: (a) stated fields from
Step 1a, and (b) assumptions from Step 1b. Map each signal to its reference point.

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals found** — reproduce the following verbatim and stop. Do not omit:

> No signals found — strategy.md remains current. Run signal-gathering skills before attempting
> revision.

Per schema (Signal Inventory) — the following columns are mandatory. Do not omit any column:

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? | Assumption link (A-NN / "stated field" / "none") |
|----|------|-----------|-------|------|--------------------------|---------------------------|--------------------------------------------------|
| S-01 | | | | | | Yes / No / Partial | |

---

### Step 2b — Role: Assumption Archaeologist — Back-fill phase

**Return to this role**: Adjudicate every assumption from Step 1b against the full signal set.

For each assumption row, replace `[pending]` with a signal-grounded verdict — exactly one per
row. Do not leave any row as `[pending]`:

- **Contradicted — S-NN**: A signal directly challenges this assumption. Cite the signal ID.
  Write one sentence on the contradiction.
- **Supported — S-NN**: A signal confirms this assumption. Cite the signal ID.
- **No signal coverage**: No signal in the current set speaks to this assumption.

Reproduce the full updated Assumption Table (all 5 columns). Every row must have a verdict.

After completing Step 3, return here and update "Delta candidate?" — change `yes` to `yes — F-NN`
for rows where a finding was generated.

---

### Step 3 — Role: Delta Identifier

**Adopt this role**: Name the gap between strategy beliefs and signal evidence.

**Stop. Before building the findings table, produce both outputs:**

1. **Anti-pattern label**: Name the anti-pattern you are guarding against. Write the label.
2. **Delta definition**: Delta IS: [gap between belief and signal]. Delta IS NOT: [inventory of
   signal existence].

Per schema (Delta Findings) — the following columns are mandatory. Do not omit any column:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root (A-NN / "stated field") |
|-----------|-----------------|----------------|-----------------|----------------------------------------|
| F-01 | [from Step 1a stated fields or Step 1b assumptions marked Contradicted] | | S-XX | |

After completing findings, return to Step 2b and update all `yes` entries in "Delta candidate?"
with actual F-NN IDs.

**Null case** — reproduce verbatim and skip to Step 5:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root |
|-----------|-----------------|----------------|-----------------|-----------------|
| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |

---

### Step 4 — Role: Coverage Auditor

**Adopt this role**: Assess all 9 namespaces for stage-relative completeness — not raw count.

Per schema (Namespace Audit) — the following columns are mandatory. Do not omit any column:

| Namespace | Signal Count | Stage-Relative Status | Action Needed? |
|-----------|-------------|----------------------|----------------|
| scout | | | |
| draft | | | |
| review | | | |
| flow | | | |
| trace | | | |
| prove | | | |
| listen | | | |
| program | | | |
| topic | | | |

---

### Step 5 — Role: Conflict Detective

**Adopt this role**: Find pairs of artifacts pointing in opposite directions on the same
dimension.

Per schema (Conflict Audit) — the following columns are mandatory. Do not omit any column:

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

**Null case** — reproduce verbatim. Do not omit:

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

---

### Step 6 — Role: Proposal Architect

**Adopt this role**: Translate each finding into a typed, defensible proposal. Every Proposal
ID must trace to a Finding ID (via Delta Finding) and from there to an Assumption root.

**Stop. Before building the proposals table, write the following statement verbatim:**

> "Proposals schema committed: Proposal ID ★, Type ★, Change ★, Delta Finding ★ (full
> 'Strategy assumed [X] / Signal revealed [Y]' text from Step 3 with exact Finding ID),
> Evidence ★, If unchanged ★ (specific degradation — a row that cannot name a specific
> degradation is a preference, not a decision), Reversibility ★ [(1) Reversible at same cost
> / (2) Gets harder / (3) Becomes impossible — select one; prose is not a valid value; a row
> that cannot select one of these three values has not reasoned about the deferral window],
> Confidence ★. All three types present. Empty types use null rows. Traceability: each
> Proposal ID traces to a Finding ID via Delta Finding, and from there to an Assumption root."

Per schema (Proposals) — the following columns are mandatory. Do not omit any column.

**Column rules:**
- **"If unchanged"**: Name the specific artifact that won't be gathered, the decision that
  becomes harder, or the gap that compounds — not a restatement of the delta finding. A row
  that cannot name a specific degradation is a preference, not a decision.
- **"Reversibility"**: Select exactly one enumerated value from the three committed above.
  Prose ("it will be harder later") is not a valid value. A row that cannot commit to (1), (2),
  or (3) has not reasoned about the deferral window and must be revised before this step is
  complete.

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged [specific degradation — not a delta finding synonym] | Reversibility [(1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible — select one] | Confidence |
|------------|------|--------|--------------|-------------------|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [which artifact won't be gathered / which gap compounds] | (2) Gets harder | High |

Null rows (reproduce verbatim for each empty type):

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Reversibility | Confidence |
|------------|------|--------|--------------|-------------------|-------------|--------------|------------|
| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 7 — Role: Diff Author

**Adopt this role**: Show the exact before/after for every confirmed proposal. Every Proposal
ID is the entry point into the full traceability chain: Proposal ID → Delta Finding → Assumption
root.

**Stop. Before building the diff table, write the following statement verbatim:**

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★ (inline
> per row as [file.md — ≤10 word finding] — no separate evidence section), Proposal ★
> (Proposal ID from Step 6 — entry point into Proposal → Delta Finding → Assumption root
> chain). No column omitted."

Per schema (Diff) — the following columns are mandatory. Do not omit any column:

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current strategy text] | [proposed text] | [file.md — ≤10 word finding] | ADD-1 |

---

### Step 8 — Confirmation gate

Reply **YES** to apply all proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 9 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals. Preserve
existing structure; update only sections affected by confirmed changes.

---

## Criterion Coverage Matrix (v8 rubric, C-01–C-33)

C-01 through C-31: all mechanisms carried forward from R8. New R9 discriminators in bold.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Read strategy | Step 1a | Step 1 | Step 1a | Step 1a | Step 1a |
| C-02 Read signals | Step 2 | Step 2 | Step 2a | Step 2a | Step 2a |
| C-03 Delta not inventory | Step 3 stop+name | Step 3 stop+name+contrast | Step 3 stop+name | Step 3 stop+name+contrast | Step 3 stop+name+contrast |
| C-04 Typed proposals | Step 6 table | Step 6 table | Step 6 table | Step 6 table | Step 6 table |
| C-05 Confirm gate | Step 8 YES | Step 8 YES | Step 8 YES | Step 8 YES | Step 8 YES |
| C-06 Evidence per change | Step 6 Evidence col | Step 6 Evidence col | Step 6 Evidence col | Step 6 Evidence col | Step 6 Evidence col |
| C-07 Before/after diff | Step 7 | Step 7 | Step 7 | Step 7 | Step 7 |
| C-08 All three types | Step 6 null rows | Step 6 null rows | Step 6 null rows | Step 6 null rows | Step 6 null rows |
| C-09 Namespace gaps | Step 4 (9 by name) | Step 4 (9 by name) | Step 4 (9 by name) | Step 4 (9 by name) | Step 4 (9 by name) |
| C-10 Conflicting signals | Step 5 | Step 5 | Step 5 | Step 5 | Step 5 |
| C-11 Typed confirmation verb | Step 8 YES | Step 8 YES | Step 8 YES | Step 8 YES | Step 8 YES |
| C-12 Explicit no-change rows | Step 6 null rows verbatim | Step 6 null rows verbatim | Step 6 null rows verbatim | Step 6 null rows verbatim | Step 6 null rows verbatim |
| C-13 Inline evidence in diff | Step 7 Evidence col | Step 7 Evidence col (committed at checkpoint) | Step 7 Evidence col (committed at checkpoint) | Step 7 Evidence col | Step 7 Evidence col (committed at checkpoint) |
| C-14 Anti-inventory warning | Step 3 stop+name | Step 3 stop+name+contrast | Step 3 stop+name | Step 3 stop+name+contrast | Step 3 stop+name+contrast |
| C-15 All 9 namespaces named | Step 4 table | Step 4 table | Step 4 table | Step 4 table | Step 4 table |
| C-16 Two-level traceability | Step 6 Delta Finding + Evidence | Step 6 Delta Finding + Evidence (committed) | Step 6 Delta Finding + Evidence | Step 6 Delta Finding + Evidence + chain obligation | Step 6 Delta Finding + Evidence + chain obligation |
| C-17 Explicit no-conflicts | Step 5 null row verbatim | Step 5 null row verbatim | Step 5 null row verbatim | Step 5 null row verbatim | Step 5 null row verbatim |
| C-18 Structured delta format | Step 3 table | Step 3 table | Step 3 table | Step 3 table | Step 3 table |
| C-19 Diff Proposal ID col | Step 7 Proposal col | Step 7 Proposal col (committed) | Step 7 Proposal col (committed) | Step 7 Proposal col | Step 7 Proposal col (committed) |
| C-20 Delta Finding col | Step 6 mandatory + null rows | Step 6 mandatory + null rows (committed) | Step 6 mandatory + null rows | Step 6 mandatory + null rows | Step 6 mandatory + null rows (committed) |
| C-21 Column-completeness declaration | PASS: every table | PASS: upfront ★ schema + per-table | PASS: every table | PASS: upfront ★ schema + per-table | PASS: upfront ★ schema + per-table |
| C-22 Active anti-pattern checkpoint | PASS: Step 3 stop+name | PASS: Step 3 stop+name+contrast + Step 6 checkpoint | PASS: Step 3 stop+name | PASS: Step 3 stop+name+contrast | PASS: Steps 3+6+7 checkpoints |
| C-23 Pre-reproduced null templates | PASS: all null outcomes | PASS: all null outcomes | PASS: all null outcomes | PASS: all null outcomes | PASS: all null outcomes |
| C-24 Unstated assumption extraction | PASS: Step 1b scan (a-e), 5-col table | PASS: Step 1 unstated + implicit evidence | PASS: Step 1b Archaeologist role, scan (a-e) | PASS: Step 1b Archaeologist role, scan (a-e), full schema | PASS: Step 1b Archaeologist + scan (a-f) + full schema |
| C-25 Inertia cost column | PASS: "If unchanged" col | PASS: "If unchanged" + adjacent rule | PASS: "If unchanged" col | PASS: "If unchanged" + committed at checkpoint | PASS: "If unchanged" + adjacent rule + committed at checkpoint |
| C-26 Schema-first priming | PASS: upfront ★ schema | PASS: upfront ★ schema | PARTIAL: per-table only | PASS: upfront ★ schema | PASS: upfront ★ schema |
| C-27 Cascade checkpoints | PARTIAL: Step 3 + Step 7 only | PASS: Steps 3+6+7 | PARTIAL: Step 3 + Step 7 | PARTIAL: Step 3 only | PASS: Steps 3+6+7 |
| C-28 Named role + scan dimensions | PARTIAL: scan (a-e) in Step 1b, no named role | PARTIAL: no named role, no scan dimensions | PASS: Assumption Archaeologist + scan (a-e) | PASS: Archaeologist + scan (a-e) + upfront schema | PASS: Archaeologist + scan (a-f) + upfront schema |
| C-29 Back-fill column | PASS: "Contradicted?" + back-fill instruction | PASS: "Contradicted?" in upfront + back-fill instruction | PASS: named Step 2b lifecycle phase + verdict-per-row | PASS: upfront schema + named Step 2b back-fill phase | PASS: upfront schema + named Step 2b + verdict-per-row obligation |
| C-30 Forward-reasoning columns | PASS: "Why this matters" + "Delta candidate?" in Step 1b | PASS: "Why this matters" + "Delta candidate?" in upfront + Step 1 | FAIL: no delta-relevance col, no delta-candidate col | PASS: "Why this matters" + "Delta candidate?" in upfront + Step 1b + updated post-Step 3 | PASS: "Why this matters" + "Delta candidate?" in upfront + Step 1b + updated post-Step 3 |
| C-31 Decision-gate framing | FAIL: no adjacent disqualification rule | PASS: "a row that cannot name a specific degradation here is a preference, not a decision" in column header | FAIL: no adjacent disqualification rule | PASS: column rule + "a row that writes a synonym of the delta finding is a preference, not a decision" | PASS: adjacent rule in column header + Step 6 checkpoint commitment |
| **C-32 Reversibility taxonomy** | **PASS: three-value enum in upfront schema + in Step 6 column header; "prose is not a valid value"** | **FAIL: Reversibility column present but no enum; values not restricted** | **PASS: three forced-choice decision options [A]/[B]/[C]; "do not write prose" enforcement** | **PASS: three-value enum in upfront schema + in Step 6 column header** | **PASS: three-value enum in upfront schema + Step 6 column header + Step 6 commitment checkpoint names all three values + disqualification rule** |
| **C-33 Assumption table in upfront schema** | **FAIL: Assumption Table in upfront schema but no Implicit evidence column** | **PASS: Implicit evidence column in upfront Assumption Table + in Step 1b extraction** | **FAIL: no upfront schema; no Implicit evidence column** | **PASS: Implicit evidence column in upfront Assumption Table + in Step 1b extraction** | **PASS: Implicit evidence column in upfront Assumption Table (named as pre-reading contract) + in Step 1b extraction** |

---

## R9 Discriminator Analysis

| Variation | C-32 mechanism | C-33 mechanism | Structural bet |
|-----------|----------------|----------------|----------------|
| V-01 | Enum in column header ("select one; prose is not a valid value") in both upfront schema and Step 6 template — PASS | No implicit evidence column — FAIL | Closed-enum in header is sufficient to lock C-32 without C-33; isolates format from lifecycle |
| V-02 | Reversibility column present but no enum or prose rule — FAIL | Implicit evidence column in upfront schema + Step 1b ("leave blank only if no strategy text implies it") — PASS | Citation requirement changes which assumptions surface; isolates C-33 from C-32 |
| V-03 | Decision-question framing [A]/[B]/[C] + "do not write prose" — PASS | No upfront schema; no implicit evidence column — FAIL | Decision-question activates different reasoning than taxonomy label; tests whether phrasing register alone closes C-32 |
| V-04 | Enum in column header in upfront schema + Step 6 — PASS | Implicit evidence column in upfront schema + Step 1b — PASS | First combination achieving both C-32 and C-33; schema-first priming for both; R8 V-04 base |
| V-05 | Enum in upfront + Step 6 header + Step 6 commitment checkpoint names all three values + disqualification rule — PASS | Implicit evidence column in upfront schema (named as pre-reading contract) + archaeology obligation in Step 1b — PASS | Full stack ceiling; tests whether the implicit evidence archaeology citation changes delta finding quality, and whether triple-checkpoint enum enforcement changes proposal defensibility |

**Key structural distinctions:**

- **V-01 vs V-03 (both C-32 pass, different mechanism)**: V-01 uses taxonomy-label selection
  constrained to three values; V-03 uses decision-question forced-choice [A/B/C]. If both pass
  C-32 but V-03 proposals show richer temporal reasoning, decision-question framing produces
  deeper consequence analysis than label selection — the phrasing register difference is real.

- **V-02 (C-33 isolation)**: The only variation with implicit evidence but no enum constraint.
  Tests whether adding the "find the strategy text" obligation changes extraction quality
  independently of the reversibility taxonomy. If V-02 assumptions are more auditable (each
  tied to a specific phrase) but V-02 proposals are no better defended than R8 V-05, C-33 is a
  provenance criterion (traceability) not a quality criterion (proposal reasoning).

- **V-04 vs V-05 (both C-32+C-33 pass)**: V-04 uses R8 V-04 base (no cascade checkpoints);
  V-05 uses R8 V-05 base (full cascade checkpoints including the Step 6 commitment that names
  all three reversibility values). If V-04 and V-05 are indistinguishable in proposal quality,
  the Step 6 commitment addition (C-27 pass) doesn't change what the Proposal Architect role
  produces — the pre-reading schema commitment is sufficient. If V-05 proposals are more
  temporally precise, the at-step commitment (naming the three values again under execution
  pressure) reinforces the pre-reading contract in a way that schema-first alone does not.

- **Where V-01 and V-03 fail C-33, and V-02 fails C-32**: All three are intentional
  single-axis isolations. V-01 and V-03 test whether C-32 mechanisms work without C-33's
  implicit evidence obligation. V-02 tests whether C-33's implicit evidence obligation works
  without C-32's enum constraint. Single-axis failures here prove the independence of the two
  criteria — their combination in V-04 and V-05 is not redundant if each axis passes and fails
  independently.
