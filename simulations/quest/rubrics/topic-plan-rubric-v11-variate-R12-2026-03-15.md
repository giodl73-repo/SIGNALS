# topic-plan — Round 12 Variations (v11 rubric)

**Skill**: `topic:plan`
**Rubric**: v11 (C-01–C-39, 245 pts total)
**Date**: 2026-03-15

---

## Round 12 Design Notes

R11 V-03/V-04/V-05 achieved perfect 235/235 under v10. Two new v11 criteria promote
what R11 V-03/V-04 introduced:

- **C-38** — Pass/fail example symmetry: pass examples must be concrete, quoted, labeled,
  and format-traceable — not structural descriptions of the passing mechanism. R11 V-03/V-04/V-05
  satisfy this with quoted pass examples like `"teams run scout before draft"`.
- **C-39** — Step-level activation cross-reference: the extraction step must explicitly
  cite the COLUMN CONTRACT test by name. R11 V-03 satisfies this via "Apply Rule 2 using
  the PASS/FAIL exhibit in the COLUMN CONTRACT before completing each cell"; R11 V-04
  satisfies it via "Apply Rule 2 using the PASS/FAIL exhibit from the COLUMN CONTRACT
  before completing each `Implicit evidence` cell."

**All R12 variations preserve C-38 and C-39 as floor requirements.**

**Three single-axis dimensions explored in R12:**

1. **Phrasing register**: Conversational/developer-friendly language throughout. Same
   structural requirements; every "Adopt this role" → first-person instruction; every
   "The following columns are mandatory. Do not omit any column." → accessible equivalent.
   Tests whether structural compliance is phrasing-dependent.

2. **Lifecycle emphasis**: Expanded COLUMN CONTRACT block (per-rule rationale, why each
   rule exists, extended PASS/FAIL exhibits, two additional rules: null completeness and
   two-level traceability). Compressed step bodies — each step = role + action + null case
   only; no per-step column annotations (all moved upfront into CONTRACT). Tests whether
   front-loading all binding constraints produces better compliance than distributing
   annotations across steps.

3. **Role sequence**: Namespace Coverage Audit runs before Delta Identifier. Delta Findings
   gain a "Namespace gap?" column. Model has a complete namespace gap picture in hand
   before forming delta claims — gaps with zero signals can become structured delta findings.
   Tests whether namespace-gap awareness at delta-formation time surfaces coverage-driven
   findings that would otherwise be missed or appear only as audit notes.

**Variation design:**

| Variation | Axis | Type | Primary R12 target |
|-----------|------|------|--------------------|
| V-01 | Phrasing register — conversational | Single | Developer UX / structural compliance stability |
| V-02 | Lifecycle emphasis — expanded CONTRACT, compressed steps | Single | Front-loaded contract retention |
| V-03 | Role sequence — namespace audit before delta | Single | Namespace-gap delta coverage (C-09) |
| V-04 | Phrasing register + Lifecycle emphasis (V-01 + V-02) | Combination | Developer-friendly + contract-heavy |
| V-05 | Full ceiling — V-01 + V-02 + V-03 + pre-read hypothesis | Combination | Maximum structural depth + developer UX |

---

## V-01 — Conversational Phrasing Register

**Axis**: Phrasing register — every formal imperative phrase is replaced with a
conversational equivalent. All structural requirements are identical: COLUMN CONTRACT,
output schema, step sequence, null-case templates, confirmation gate. Only the language
register changes.

**Hypothesis**: The enforcement value of structural criteria (CONTRACT architecture,
schema-first priming, step-level activation) derives from position and structure, not
formal register. If correct, conversational phrasing produces identical or higher
compliance scores because reduced cognitive friction compensates for reduced formality.
If incorrect — a conversational prompt scores lower on C-21 or C-27 — the finding
indicates that imperative/formal language is load-bearing beyond its informational content.

---

You are running `topic:plan` for the topic `{topic}`.

Your job: look at what signals have come in since `simulations/{topic}/strategy.md` was
written and decide what to update. You'll extract assumptions before reading signals, then
back-fill after. When you have proposals ready, show them and wait for a YES before
writing anything. Do not auto-apply.

---

### COLUMN CONTRACT — read this before anything else

Two rules govern every table you produce. Read both before looking at any file.

**Rule 1 — Enumerated columns**: If a column has a fixed set of valid values, use only
those values. No paraphrasing, no prose, no hybrid answers.

What passes:
- `Type`: `ADD` | `REMOVE` | `REPRIORITIZE`
- `Reversibility`: `(1) Reversible at same cost` | `(2) Gets harder` | `(3) Becomes impossible`
- `Delta candidate?`: `yes` | `no` | `yes — F-01` (after delta step)
- `Consistent with strategy?`: `Yes` | `No` | `Partial`

What fails (treated as blank):
- `Type`: "I'd suggest adding..." | "addition of a skill" | "add/remove"
- `Reversibility`: "will get harder over time" | "probably cannot reverse this"
- `Consistent with strategy?`: "mostly yes" | "it depends on the context"

**Rule 2 — Column independence**: Before you fill in any cell, ask yourself: *"Could I
write this cell without looking at the source document?"* If yes, your cell is empty —
even if it looks filled. This applies especially to `Implicit evidence`.

What passes (you had to read strategy.md to write this):

- PASS: `"teams run scout before draft"` — a phrase you found in the rationale block
- PASS: `"signal count threshold never defined"` — a gap you noticed was absent
- PASS: `"the phrase 'gather evidence first'"` — a quoted instruction from the document

What fails (you could write this without reading anything — treated as blank):

- FAIL: `A-01` — that's just the row key
- FAIL: `"signals gather evidence"` — a restatement of the assumption in different words
- FAIL: `"see rationale section"` — a pointer that has no content
- FAIL: `"strategy implies sequencing"` — a generic inference not traceable to any phrase

---

### Output Schema — read this before Step 1

Every table you produce must match this schema. Columns marked ★ are required — skip
one and that column doesn't exist.

**Assumption Table** (5 columns — each independently populated per Rule 2)
| ★ Assumption | ★ Implicit evidence [Rule 2 — must require reading strategy.md; PASS: phrase/paraphrase | FAIL: row key / restatement / pointer] | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? [Rule 1: yes / no / yes — F-NN] |

**Signal Inventory**
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? [Rule 1: Yes / No / Partial] | ★ Assumption link (A-NN / "stated field" / "none") |

**Delta Findings**
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) | ★ Assumption root (A-NN / "stated field") |

**Namespace Audit**
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |

**Conflict Audit**
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals** (Rule 1 applies to Type and Reversibility)
| ★ Proposal ID | ★ Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | ★ Change | ★ Delta Finding | ★ Evidence | ★ If unchanged [what gap stays open or gets worse] | ★ Reversibility [Rule 1: (1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible] | ★ Confidence |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

Every ★ column is required in every table. Don't skip any.

---

### Step 1 — Stated-Field Extractor

Here's your job: pull out exactly what strategy.md says. Don't infer, don't extrapolate.

Read `simulations/{topic}/strategy.md`.

Every field below is required — skip one and this step is incomplete.

| Field | Value |
|-------|-------|
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Stated rationale | |
| Acknowledged gaps | |

---

### Step 2 — Assumption Archaeologist (Extract)

Here's your job: find what strategy.md assumed without writing it down. These are the
implied beliefs the author would defend if challenged but never put in the document.

Work through each of these dimensions:
- (a) Implied audience knowledge level
- (b) Namespace priority ordering assumed without justification
- (c) Signal sufficiency threshold — what "enough signals" means here
- (d) Timeline or sequencing feasibility
- (e) Definition of "done" for this topic

Before you fill in `Implicit evidence` for each row, apply the COLUMN CONTRACT Rule 2
test and PASS/FAIL exhibit. If you could write the cell without reading strategy.md,
leave it blank and try again.

Column notes:
- `Contradicted by a signal?`: Write `[pending]` for now. Fill this in after Step 3a.
- `Why this matters`: Fill now. Name what breaks if this assumption turns out to be wrong.
- `Delta candidate?`: Use Rule 1 — write `yes` or `no`. After Step 4, update to `yes — F-NN`.

Every column below is required — skip one and this step doesn't count.

| Assumption | Implicit evidence [must require reading strategy.md — PASS: quoted phrase | FAIL: row key / restatement / pointer] | Contradicted by a signal? | Why this matters for delta detection | Delta candidate? [yes / no] |
|-----------|-------------------------------------------------------------------------------------------------------|--------------------------|--------------------------------------|------------------------------|
| [most important — highest chance of signal contradiction] | [phrase you found in strategy.md] | [pending] | [what breaks if wrong] | yes |

At least one row required. If nothing found:

| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |

---

### Step 3a — Signal Analyst (Read)

Here's your job: read every artifact and check it against what you found in Steps 1 and 2.

Glob `simulations/{topic}/` recursively. Read every file.

If no signals exist, reproduce this verbatim and stop:

> No signals found — strategy.md does not need revision at this time.

Every column below is required. Rule 1 applies to `Consistent with strategy?` — pick
one: `Yes` / `No` / `Partial`. Prose fails.

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? [Yes / No / Partial] | Assumption link (A-NN / "stated field" / "none") |
|----|------|-----------|-------|------|--------------------------|------------------------------------------------|--------------------------------------------------|
| S-01 | | | | | | | |

---

### Step 3b — Assumption Archaeologist (Back-fill)

Go back to your assumption table. For each `[pending]`, write exactly one verdict:
- **Contradicted — S-NN**: This signal challenges the assumption. Cite ID + one sentence.
- **Supported — S-NN**: This signal confirms the assumption. Cite ID.
- **No signal coverage**: No signal addresses this assumption.

Reproduce the full updated assumption table (all 5 columns). After Step 4, come back
and update `yes` rows to `yes — F-NN`.

---

### Step 4 — Delta Identifier

Here's your job: name what signals revealed that the strategy didn't anticipate. This
is different from listing what signals exist.

Stop. Before building the findings table, write:
1. The name of the anti-pattern you're guarding against at this step.
2. A PASS/FAIL exhibit showing the difference:

| Example type | Row |
|-------------|-----|
| PASS — this is a delta | "Strategy assumed scout signals were required before draft / Signal revealed: draft completed without any scout artifacts" |
| FAIL — this is inventory | "We have 3 scout signals" or "S-01 covers namespace coverage" |

Every column below is required. Don't skip any.

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root (A-NN / "stated field") |
|-----------|-----------------|----------------|-----------------|----------------------------------------|
| F-01 | [from Step 1 or 2] | | S-XX | |

After building findings, return to Step 3b and update `yes` rows to `yes — F-NN`.

If all signals confirm the strategy, reproduce this verbatim and skip to Step 6:

| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |

---

### Step 5 — Coverage Auditor

Go through all 9 namespaces. Stage-relative = right for where this topic currently is,
not just a raw count.

Every column below is required.

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

### Step 6 — Conflict Detective

Every column below is required.

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

No conflicts found? Reproduce this verbatim — don't skip this table:

| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

---

### Step 7 — Proposal Architect

Before building the proposals table, write this statement word-for-word:

> "Proposals schema committed: Proposal ID ★, Type ★ [Rule 1: ADD / REMOVE / REPRIORITIZE;
> prose fails], Change ★, Delta Finding ★ (full 'Strategy assumed [X] / Signal revealed [Y]'
> text from Step 4 with exact ID), Evidence ★, If unchanged ★ (a row that can't name a
> specific degradation is a preference, not a decision), Reversibility ★ [Rule 1: (1)/(2)/(3);
> prose fails], Confidence ★. All three types present. Empty types use null rows."

Every column below is required — skip one and the row is invalid.

| Proposal ID | Type [ADD / REMOVE / REPRIORITIZE — Rule 1] | Change | Delta Finding | Evidence | If unchanged [specific degradation — no degradation named = preference, not decision] | Reversibility [(1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible — Rule 1] | Confidence |
|------------|---------------------------------------------|--------|--------------|----------|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [specific degradation] | (2) Gets harder | High |

Null rows — reproduce these verbatim for any empty type:

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 8 — Diff Author

Before building the diff table, write this statement word-for-word:

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★
> (inline as [file.md — ≤10 word finding] — no separate evidence section), Proposal ★
> (Proposal ID from Step 7). No column omitted."

Every column below is required.

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current strategy text] | [proposed text] | [file.md — ≤10 word finding] | ADD-1 |

---

### Step 9 — Confirmation gate

Reply **YES** to apply all proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 10 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals. Preserve
existing structure; update only sections affected by confirmed changes.

---

## V-02 — Expanded COLUMN CONTRACT, Compressed Steps

**Axis**: Lifecycle emphasis — the COLUMN CONTRACT section is expanded with per-rule
rationale paragraphs, extended PASS/FAIL exhibit rows, and two additional rules (null
completeness, two-level traceability). Step bodies are compressed: each step = role
assignment + action + mandatory-column list + null case. All per-step column annotations
and example rows are removed from steps and consolidated upfront in the CONTRACT.

**Hypothesis**: R11 V-03 distributed enforcement annotations across steps: column header
annotation in the schema, inline example row at Step 2, PASS/FAIL exhibit at Step 4.
Under context pressure, a procedure encountered at position N in a long prompt may
receive less attention than one encountered at position 1. Front-loading all contract
content into the CONTRACT block means the model reads the binding rules once, completely,
before any step begins. If compressed steps reduce redundant re-instruction and the
upfront CONTRACT is thorough enough, compliance should be equivalent or higher because
the model cannot encounter a step without having already read the governing rules.
The two new rules (R3: null completeness, R4: two-level traceability) test whether
named-rule coverage of all enforcement criteria (C-17, C-23, C-16) is more durable
than per-step instructions.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it
was written. The assumption table is a two-phase artifact: extract at Step 2 (before
signal reading), back-fill at Step 3b (after). Present proposals, wait for confirmation,
then write. Do not auto-apply changes.

---

### COLUMN CONTRACT (binding before reading any file)

Four rules govern every table you produce. Read all four before the Output Schema.

**Rule 1 — Enumerated columns**

Any column using a closed value set must declare those values at every point where the
column is named. Select from the declared set only; prose is not a valid value. A cell
that contains paraphrase, conditional prose, or a multi-value selection is treated as
empty regardless of content.

*Why this matters*: A model that sees `Type` and writes "I think we should add a new
skill" has not made a typed proposal — it has made a suggestion. Typed columns are
falsifiable; prose columns are not. An ADD-type proposal and a REPRIORITIZE-type
proposal are structurally different change requests. Mixing types in prose removes
that distinction and makes the proposals table non-auditable.

Rule 1 PASS examples:
- `Type`: `ADD` | `REMOVE` | `REPRIORITIZE`
- `Reversibility`: `(1) Reversible at same cost` | `(2) Gets harder` | `(3) Becomes impossible`
- `Delta candidate?`: `yes` | `no` | `yes — F-01` | `yes — F-03`
- `Consistent with strategy?`: `Yes` | `No` | `Partial`

Rule 1 FAIL examples (treated as absent):
- `Type`: "I suggest adding..." | "addition" | "add/remove"
- `Reversibility`: "it will be harder later" | "probably irreversible" | "somewhat reversible"
- `Delta candidate?`: "probably yes" | "yes if confirmed" | "yes, depending on signal weight"
- `Consistent with strategy?`: "mostly yes" | "it's complicated" | "partially yes"

**Rule 2 — Column independence**

Before filling any cell, apply this test: *"Can I fill this cell without reading the
source document?"* If yes, the cell is a structural alias and is treated as empty.
Applies to every column but is especially critical for `Implicit evidence` — the cell
must contain text or paraphrase traceable to a specific location in strategy.md.

*Why this matters*: The `Implicit evidence` column exists to make assumptions auditable.
If a reviewer cannot trace the evidence back to a phrase in strategy.md, the column is
not doing its job. Row-key aliasing, restatements, and pointers all satisfy the column
structurally while providing no auditable content. A column that can be filled without
reading the document is navigational metadata, not an analytical dimension.

Rule 2 PASS examples for `Implicit evidence` (content that requires reading strategy.md):

- PASS: `"teams run scout before draft"` — specific phrase from strategy.md rationale block
- PASS: `"signal count threshold never defined"` — gap detected as absent in the text
- PASS: `"the phrase 'gather evidence first'"` — verbatim instruction from the document
- PASS: `"no definition of done for this topic appears in the strategy"` — explicit gap notation

Rule 2 FAIL examples for `Implicit evidence` (treated as absent regardless of appearance):

- FAIL: `A-01` — the row key; reconstructible without reading the document
- FAIL: `"signals gather evidence"` — restatement of the assumption in different words
- FAIL: `"see rationale section"` — pointer with no content
- FAIL: `"strategy implies sequencing"` — generic inference not traceable to any phrase
- FAIL: `"the strategy assumes this"` — circular reference to the row itself

**Rule 3 — Null completeness**

Every mandatory null case must appear in the output. A section that runs and finds
nothing is proven by its null row. A missing section is indistinguishable from a
section that was skipped entirely.

*Why this matters*: Auditable absence requires an explicit declaration. If the Conflict
Audit section is empty because no conflicts exist, that is a finding — not a formatting
oversight. Null rows are not formatting courtesy; they are evidence that the section ran.

Rule 3 PASS examples:
- Conflict null: `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |`
- ADD null: `| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |`
- Delta null: `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |`

Rule 3 FAIL (treated as section skipped):
- Empty conflict section with no null row
- Proposals table with only ADD rows and no REMOVE / REPRIORITIZE null rows
- Delta step skipped with only "no changes needed" in prose

**Rule 4 — Two-level traceability**

Every proposal must chain from proposal to delta finding to source signal. The `Delta
Finding` column must include the full "Strategy assumed [X] / Signal revealed [Y]" text
from the delta step with the exact finding ID — not just the ID, not just a signal reference.

*Why this matters*: The proposals table should be self-contained. A reviewer should
be able to understand why each change is proposed without returning to the delta section.
A finding ID alone requires re-reading; the full delta text in the proposals row does not.

Rule 4 PASS example (`Delta Finding` cell):
- `F-01: Strategy assumed scout runs before draft / Signal revealed draft completed without scout artifacts`

Rule 4 FAIL examples:
- `F-01` — finding ID only; requires re-reading delta section
- `"signal S-01 suggests adding a skill"` — signal reference, no delta structure

---

### Output Schema (read before proceeding to Step 1)

Every table you produce must conform to this schema. Columns marked ★ are mandatory.
All four Contract Rules apply. Do not omit any ★ column.

**Assumption Table** (5 columns — all independently populated per Rule 2)
| ★ Assumption | ★ Implicit evidence [Rule 2 — PASS: phrase/paraphrase from strategy.md | FAIL: row key / restatement / pointer] | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? [Rule 1: yes / no / yes — F-NN] |

**Signal Inventory**
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? [Rule 1: Yes / No / Partial] | ★ Assumption link (A-NN / "stated field" / "none") |

**Delta Findings**
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) | ★ Assumption root (A-NN / "stated field") |

**Namespace Audit**
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |

**Conflict Audit**
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals** (Rules 1 and 4 apply)
| ★ Proposal ID | ★ Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | ★ Change | ★ Delta Finding [Rule 4: full "Strategy assumed X / Signal revealed Y" + ID] | ★ Evidence | ★ If unchanged | ★ Reversibility [Rule 1: (1)/(2)/(3)] | ★ Confidence |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

Do not omit any ★ column.

---

### Step 1 — Role: Stated-Field Extractor

Read `simulations/{topic}/strategy.md`. Extract stated fields only. Do not infer.

The following columns are mandatory. Do not omit any column.

| Field | Value |
|-------|-------|
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Stated rationale | |
| Acknowledged gaps | |

---

### Step 2 — Role: Assumption Archaeologist (Extract)

Extract what strategy.md assumed without writing. Scan dimensions: (a) audience
knowledge, (b) namespace priority ordering, (c) signal sufficiency threshold,
(d) timeline feasibility, (e) definition of done.

Apply the COLUMN CONTRACT Rule 2 PASS/FAIL exhibit before populating each
`Implicit evidence` cell.

The following columns are mandatory. Do not omit any column.

Column rules: `Contradicted?` = `[pending]` until Step 3b. `Why it matters` = failure
mode if assumption is wrong. `Delta candidate?` = Rule 1 (`yes` / `no`); update to
`yes — F-NN` after Step 4.

| Assumption | Implicit evidence [Rule 2] | Contradicted by a signal? | Why this matters | Delta candidate? |
|-----------|---------------------------|--------------------------|-----------------|-----------------|
| [most important] | [phrase from strategy.md — Rule 2 test before filling] | [pending] | [failure mode] | yes |

Null case (Rule 3): `| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |`

---

### Step 3a — Role: Signal Analyst (Read)

Glob `simulations/{topic}/` recursively. Read every file.

Null case (Rule 3): `> No signals found — strategy.md does not need revision at this time.`

The following columns are mandatory. Rule 1: `Consistent with strategy?` = Yes / No / Partial.

| ID | File | Namespace | Skill | Date | Key Finding | Consistent with strategy? | Assumption link |
|----|------|-----------|-------|------|-------------|--------------------------|----------------|
| S-01 | | | | | | | |

---

### Step 3b — Role: Assumption Archaeologist (Back-fill)

Adjudicate each A-NN against all signals. Replace `[pending]` with one of:
- `Contradicted — S-NN`: cite ID, one sentence
- `Supported — S-NN`: cite ID
- `No signal coverage`

Reproduce full updated assumption table. After Step 4, update `yes` rows to `yes — F-NN`.

---

### Step 4 — Role: Delta Identifier

Stop. Write: (1) the anti-pattern label you are guarding against, and (2) a PASS/FAIL
exhibit for the delta vs. inventory distinction. Then fill the findings table.

The following columns are mandatory. Do not omit any column.

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root |
|-----------|-----------------|----------------|-----------------|----------------|
| F-01 | | | S-XX | |

Null case (Rule 3): `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |`

After findings, return to Step 3b and update `yes` rows to `yes — F-NN`.

---

### Step 5 — Role: Coverage Auditor

All 9 namespaces by name. Stage-relative, not raw count.

The following columns are mandatory.

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

### Step 6 — Role: Conflict Detective

The following columns are mandatory.

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

Null case (Rule 3): `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |`

---

### Step 7 — Role: Proposal Architect

Stop. Write this statement verbatim before building the proposals table:

> "Proposals schema committed: Proposal ID ★, Type ★ [Rule 1: ADD / REMOVE / REPRIORITIZE;
> prose not valid], Change ★, Delta Finding ★ [Rule 4: full 'Strategy assumed X / Signal
> revealed Y' text with ID], Evidence ★, If unchanged ★ (no degradation = preference not
> decision), Reversibility ★ [Rule 1: (1)/(2)/(3); prose not valid], Confidence ★. All
> three types present. Empty types use Rule 3 null rows."

The following columns are mandatory. Do not omit any column.

| Proposal ID | Type | Change | Delta Finding [Rule 4] | Evidence | If unchanged | Reversibility | Confidence |
|------------|------|--------|----------------------|----------|-------------|--------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [degradation] | (2) Gets harder | High |

Null rows (Rule 3):

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 8 — Role: Diff Author

Stop. Write this statement verbatim before building the diff table:

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★
> (inline [file.md — ≤10 words] per row — no separate section), Proposal ★ (ID from
> Step 7). No column omitted. Rule 1 applies to all enumerated columns."

The following columns are mandatory.

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | | | | ADD-1 |

---

### Step 9 — Confirmation gate

Reply **YES** to apply all proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 10 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals. Preserve
existing structure; update only sections affected.

---

## V-03 — Namespace Audit Before Delta Identification

**Axis**: Role sequence — the Namespace Coverage Audit (normally Step 5) runs as
Step 4, before the Delta Identifier (Step 5). Delta Findings gain a "Namespace gap?"
column. When the model knows which namespaces have zero or thin signal coverage before
forming delta claims, it can explicitly surface coverage-driven findings.

**Hypothesis**: In the standard sequence, the model identifies deltas from
assumption/signal mismatches, then audits namespace coverage separately. A delta
finding driven by signal absence in a namespace (e.g., "prove" has 0 signals) requires
the model to either notice the gap during signal reading or form it retrospectively
during audit. In the reordered sequence, the model has an explicit namespace gap report
before the delta step: if "prove" shows 0 signals, the model can generate "Strategy
assumed prove-level validation coverage / Signal revealed: no prove signals gathered"
as a structured delta finding, not just an audit note. This should improve C-09
(namespace coverage gap detection) by making namespace imbalance available as a delta
source at delta-formation time, not after.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it
was written. The assumption table is a two-phase artifact: extract at Step 2, back-fill
at Step 3b. You will audit namespace coverage before identifying deltas — namespace
gaps are delta candidates. Present proposals, wait for confirmation, then write.
Do not auto-apply changes.

---

### COLUMN CONTRACT (binding before reading any file)

Two rules govern every table you produce. Read before the Output Schema.

**Rule 1 — Enumerated columns**: Any column using a closed value set must declare those
values at every point where the column is named. Select from the declared set only; prose
is not a valid value. Applies to: `Delta candidate?` [yes / no / yes — F-NN],
`Consistent with strategy?` [Yes / No / Partial], `Type` [ADD / REMOVE / REPRIORITIZE],
`Reversibility` [(1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible],
`Namespace gap?` [yes — NS-NAME / no].

Rule 1 PASS examples:
- `Type`: `ADD` | `REMOVE` | `REPRIORITIZE`
- `Reversibility`: `(1) Reversible at same cost` | `(2) Gets harder` | `(3) Becomes impossible`
- `Namespace gap?`: `yes — prove` | `yes — trace` | `no`

Rule 1 FAIL examples (treated as absent):
- `Type`: "I suggest adding" | "addition" | "add/remove"
- `Reversibility`: "gets harder over time" | "might be irreversible"
- `Namespace gap?`: "probably yes" | "yes for some namespaces" | "depends on stage"

**Rule 2 — Column independence**: Before filling any cell, apply this test: *"Can I fill
this cell without reading the source document?"* If yes, the cell is a structural alias
and is treated as empty. Applies especially to `Implicit evidence`.

Rule 2 PASS examples for `Implicit evidence` (requires reading strategy.md):

- PASS: `"teams run scout before draft"` — traced to rationale block
- PASS: `"signal count threshold never defined"` — gap detected as absent text
- PASS: `"the phrase 'gather evidence first'"` — verbatim from the document

Rule 2 FAIL examples for `Implicit evidence` (treated as absent):

- FAIL: `A-01` — row key
- FAIL: `"signals gather evidence"` — restatement
- FAIL: `"see rationale section"` — pointer without content
- FAIL: `"strategy implies sequencing"` — generic inference not traceable to a phrase

---

### Output Schema (read before proceeding to Step 1)

Every table you produce must conform to this schema. Columns marked ★ are mandatory —
do not omit any ★ column. Both Contract Rules apply to every ★ column.

**Assumption Table** (5 columns — all independently populated per Rule 2)
| ★ Assumption | ★ Implicit evidence [Rule 2 — PASS: phrase from strategy.md | FAIL: row key / restatement / pointer] | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? [Rule 1: yes / no / yes — F-NN] |

**Signal Inventory**
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? [Rule 1: Yes / No / Partial] | ★ Assumption link (A-NN / "stated field" / "none") |

**Namespace Audit** (runs as Step 4 — before Delta)
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? | ★ Delta candidate? [Rule 1: yes — generate F-NN at Step 5 / no] |

**Delta Findings**
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) | ★ Assumption root (A-NN / "stated field" / "namespace gap") | ★ Namespace gap? [Rule 1: yes — NS-NAME / no] |

**Conflict Audit**
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals** (Rule 1 applies to Type, Reversibility, Namespace gap?)
| ★ Proposal ID | ★ Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | ★ Change | ★ Delta Finding | ★ Evidence | ★ If unchanged | ★ Reversibility [Rule 1: (1)/(2)/(3)] | ★ Confidence |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

Do not omit any ★ column.

---

### Step 1 — Role: Stated-Field Extractor

**Adopt this role**: Extract only what strategy.md wrote explicitly. Do not infer.

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

### Step 2 — Role: Assumption Archaeologist (Extract)

**Adopt this role**: Find what strategy.md took for granted without writing.

Systematic scan — cover each dimension:
- (a) Implied audience knowledge level
- (b) Namespace priority ordering assumed without justification
- (c) Signal sufficiency threshold — what "enough signals" means here
- (d) Timeline or sequencing feasibility
- (e) Definition of "done" for this topic

Per schema (Assumption Table) — all five columns mandatory. Before populating each
`Implicit evidence` cell, apply the COLUMN CONTRACT Rule 2 PASS/FAIL exhibit. If you
can write the cell without reading strategy.md, it fails the test — find a direct phrase.

Column rules:
- `Contradicted by a signal?`: Write `[pending]` now. Fill after Step 3b.
- `Why this matters`: Fill now. Name the failure mode if wrong.
- `Delta candidate?`: Rule 1 — select `yes` or `no`. Update to `yes — F-NN` after Step 5.

**The following columns are mandatory. Do not omit any column.**

| Assumption | Implicit evidence [Rule 2 — PASS: phrase from strategy.md | FAIL: row key / restatement / pointer] | Contradicted by a signal? | Why this matters for delta detection | Delta candidate? [yes / no] |
|-----------|-------------------------------------------------------------------------------------------------------|--------------------------|--------------------------------------|------------------------------|
| [most important] | [phrase from strategy.md — apply CONTRACT Rule 2 test before filling] | [pending] | [failure mode if wrong] | yes |

Null case: `| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |`

---

### Step 3a — Role: Signal Analyst (Read)

**Adopt this role**: Read every artifact against stated fields (Step 1) and assumptions (Step 2).

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals** — reproduce verbatim and stop:

> No signals found — strategy.md does not need revision at this time.

**The following columns are mandatory. Rule 1 applies to `Consistent with strategy?`.**

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? [Yes / No / Partial] | Assumption link |
|----|------|-----------|-------|------|--------------------------|------------------------------------------------|----------------|
| S-01 | | | | | | | |

---

### Step 3b — Role: Assumption Archaeologist (Back-fill)

For each A-NN row, replace `[pending]`:
- `Contradicted — S-NN`: signal challenges this. Cite ID, one sentence.
- `Supported — S-NN`: signal confirms this. Cite ID.
- `No signal coverage`

Reproduce full updated assumption table. After Step 5, update `yes` rows to `yes — F-NN`.

---

### Step 4 — Role: Coverage Auditor ← runs before Delta Identifier

**Adopt this role**: Assess all 9 namespaces for signal coverage relative to the topic's
current stage. A namespace with zero signals that the strategy expected coverage for is
a delta candidate — it will generate a finding at Step 5.

**The following columns are mandatory. Do not omit any column. Rule 1 applies to
`Delta candidate?`.**

| Namespace | Signal Count | Stage-Relative Status | Action Needed? | Delta candidate? [yes — generate F-NN at Step 5 / no] |
|-----------|-------------|----------------------|----------------|-------------------------------------------------------|
| scout | | | | |
| draft | | | | |
| review | | | | |
| flow | | | | |
| trace | | | | |
| prove | | | | |
| listen | | | | |
| program | | | | |
| topic | | | | |

If a namespace has zero signals and the topic's current stage calls for them, mark
`yes — generate F-NN`. You will create a delta finding for it at Step 5.

---

### Step 5 — Role: Delta Identifier

**Adopt this role**: Name the gap between strategy beliefs and signal evidence, including
gaps surfaced by the namespace audit at Step 4.

Stop. Before building the findings table, write:
1. The name of the anti-pattern you are guarding against.
2. A PASS/FAIL exhibit:

| Example type | Row |
|-------------|-----|
| PASS — delta | "F-01: Strategy assumed prove signals would exist / Signal revealed: no prove signals gathered" |
| FAIL — inventory | "We have 0 signals in prove" or "prove coverage is thin" |

Per schema (Delta Findings) — include a finding for every `yes` namespace gap from Step 4.
**The following columns are mandatory. Do not omit any column. Rule 1 applies to `Namespace gap?`.**

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root (A-NN / "stated field" / "namespace gap") | Namespace gap? [yes — NS-NAME / no] |
|-----------|-----------------|----------------|-----------------|----------------------------------------------------------|-------------------------------------|
| F-01 | [from Step 1, 2, or 4] | | S-XX or "no signals in NS" | | yes — prove / no |

After findings, return to Step 3b and update `yes` rows to `yes — F-NN`.

Null case — all signals confirm, no namespace gaps:

| F-00 | Strategy confirmed | No gaps detected | All signals | N/A | no |

---

### Step 6 — Role: Conflict Detective

**The following columns are mandatory. Do not omit any column.**

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

**Null case — no conflicts** — reproduce verbatim. Do not omit this table:

| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

---

### Step 7 — Role: Proposal Architect

**Stop. Before building the proposals table, write the following statement verbatim:**

> "Proposals schema committed: Proposal ID ★, Type ★ [Rule 1: ADD / REMOVE / REPRIORITIZE;
> prose not valid], Change ★, Delta Finding ★ (full 'Strategy assumed [X] / Signal
> revealed [Y]' text from Step 5 with exact ID), Evidence ★, If unchanged ★ (a row
> without specific degradation is a preference, not a decision), Reversibility ★ [Rule 1:
> (1)/(2)/(3); prose not valid], Confidence ★. All three types present. Empty types use
> null rows."

**The following columns are mandatory. Do not omit any column.**

| Proposal ID | Type [Rule 1] | Change | Delta Finding | Evidence | If unchanged [specific degradation] | Reversibility [Rule 1] | Confidence |
|------------|--------------|--------|--------------|----------|-------------------------------------|----------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [degradation] | (2) Gets harder | High |

Null rows (verbatim for each empty type):

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 8 — Role: Diff Author

**Stop. Before building the diff table, write the following statement verbatim:**

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★
> (inline [file.md — ≤10 word finding] per row), Proposal ★ (ID from Step 7). No
> column omitted."

**The following columns are mandatory. Do not omit any column.**

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current text] | [proposed text] | [file.md — ≤10 words] | ADD-1 |

---

### Step 9 — Confirmation gate

Reply **YES** to apply all proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 10 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals. Preserve
existing structure; update only sections affected.

---

## V-04 — Conversational + Expanded CONTRACT (V-01 + V-02)

**Axes**: Phrasing register (V-01: conversational language throughout) + Lifecycle
emphasis (V-02: expanded CONTRACT with per-rule rationale and additional rules,
compressed step bodies).

**Hypothesis**: V-01 tests whether structural compliance is phrasing-dependent; V-02
tests whether front-loaded contract retention outperforms distributed annotation. V-04
combines them: every rule in the CONTRACT is explained in accessible language (why it
matters, in terms a developer can immediately relate to), and steps are compressed to
just the essential action. The hypothesis is that this combination produces the best
developer experience — easy to read, reason about, and follow — while achieving equal
or higher structural compliance than the formal/verbose baseline. If V-04 underperforms
V-02 on specific criteria, the finding is that rule rationale requires formal language
to be load-bearing.

---

You are running `topic:plan` for the topic `{topic}`.

Your job: look at what signals have come in since `simulations/{topic}/strategy.md` was
written, figure out what has changed, and propose revisions. Extract assumptions before
reading signals, then back-fill after. Show proposals and wait for a YES before writing
anything. Do not auto-apply.

---

### COLUMN CONTRACT — read this before anything else

Four rules govern every table you produce. Read all four before starting. These rules
apply at every step; you don't need to re-read them, but they're always active.

**Rule 1 — Enumerated columns**

If a column has a fixed set of valid values, use only those exact values. No paraphrasing,
no prose, no hedging. A cell that contains paraphrase is treated as blank.

Why this matters: a proposal typed as "I think we should add something" isn't a proposal
yet — it's a note. Once typed as `ADD`, it is structurally committed. Typed columns make
decisions auditable; prose columns make them invisible.

What passes:
- `Type`: `ADD` | `REMOVE` | `REPRIORITIZE`
- `Reversibility`: `(1) Reversible at same cost` | `(2) Gets harder` | `(3) Becomes impossible`
- `Delta candidate?`: `yes` | `no` | `yes — F-01`
- `Consistent with strategy?`: `Yes` | `No` | `Partial`

What fails (treated as blank — Rule 1 applies at every step where these columns appear):
- `Type`: "add a skill" | "addition" | "add/remove"
- `Reversibility`: "gets harder" | "probably irreversible" | "somewhat reversible"
- `Delta candidate?`: "probably yes" | "yes if confirmed" | "likely"
- `Consistent with strategy?`: "mostly" | "partially" | "it depends"

**Rule 2 — Column independence**

Before filling any cell, ask yourself: *"Could I write this cell without opening the
source document?"* If yes, your cell is empty — even if you've written something there.

Why this matters: the `Implicit evidence` column exists so that someone can trace each
assumption back to something in strategy.md. If you fill it with the row key, a
restatement, or a pointer, you've created the appearance of evidence without the
substance.

What passes (you had to read strategy.md to write this):

- PASS: `"teams run scout before draft"` — a phrase you found in the rationale block
- PASS: `"signal count threshold never defined"` — a gap you noticed was explicitly absent
- PASS: `"the phrase 'gather evidence first'"` — a verbatim quote from the document
- PASS: `"no definition of done appears in the strategy"` — an explicit gap you confirmed

What fails (you could write this without opening the document — treated as blank):

- FAIL: `A-01` — that's the row key; tells you which row you're in, not what the document said
- FAIL: `"signals gather evidence"` — a restatement of the assumption in other words
- FAIL: `"see rationale section"` — a pointer that has no content of its own
- FAIL: `"strategy implies sequencing"` — something you could infer without reading

**Rule 3 — Null completeness**

Every section that runs must show its result — including when the result is nothing.
Absence is a finding. A missing null row is indistinguishable from a skipped section.

Why this matters: if the conflict audit found nothing, that's a result — you ran the
audit and nothing came up, which is different from not running it at all.

What passes:
- No conflicts: `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |`
- No ADD proposals: `| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |`
- No delta findings: `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |`

What fails (treated as section skipped):
- Empty conflict section with no null row
- Proposals table with no REMOVE or REPRIORITIZE rows and no null rows for those types
- Missing delta section with only "no changes needed" in prose

**Rule 4 — Two-level traceability**

Every proposal needs to chain from proposal to delta finding to source signal. The Delta
Finding cell must include the full "Strategy assumed [X] / Signal revealed [Y]" text plus
the exact finding ID — not just the ID, not just a reference to the signal file.

Why this matters: the proposals table should be self-contained. A reviewer shouldn't
have to go back to the delta section to understand why ADD-1 is being proposed.

What passes:
- `F-01: Strategy assumed scout runs before draft / Signal revealed draft completed without scout artifacts`

What fails:
- `F-01` — ID only; requires re-reading delta section
- `"S-01 suggests we add a skill"` — signal reference, no delta structure

---

### Output Schema — read this before Step 1

Every table must match this schema. ★ columns are required. Skip one and that column
doesn't exist.

**Assumption Table** (5 columns — independently populated per Rule 2)
| ★ Assumption | ★ Implicit evidence [Rule 2 — PASS: phrase from strategy.md | FAIL: row key / restatement / pointer] | ★ Contradicted by a signal? | ★ Why this matters | ★ Delta candidate? [Rule 1: yes / no / yes — F-NN] |

**Signal Inventory**
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? [Rule 1: Yes / No / Partial] | ★ Assumption link |

**Delta Findings**
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) | ★ Assumption root |

**Namespace Audit**
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |

**Conflict Audit**
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals** (Rules 1 and 4 apply)
| ★ Proposal ID | ★ Type [Rule 1] | ★ Change | ★ Delta Finding [Rule 4: full text + ID] | ★ Evidence | ★ If unchanged | ★ Reversibility [Rule 1] | ★ Confidence |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

Every ★ column required. Don't skip any.

---

### Step 1 — Stated-Field Extractor

Read `simulations/{topic}/strategy.md`. Pull out exactly what it says. Don't infer.

| Field | Value |
|-------|-------|
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Stated rationale | |
| Acknowledged gaps | |

---

### Step 2 — Assumption Archaeologist (Extract)

Find what strategy.md assumed without writing. Scan: (a) audience knowledge, (b) namespace
priority ordering, (c) signal sufficiency, (d) timeline feasibility, (e) definition of done.

Before filling `Implicit evidence` for any row, apply the COLUMN CONTRACT Rule 2
PASS/FAIL exhibit. Ask: "Could I write this without reading strategy.md?" If yes, try again.

`Contradicted?` = `[pending]` for now. `Why it matters` = fill now. `Delta candidate?` = Rule 1.

| Assumption | Implicit evidence [Rule 2 test before filling] | Contradicted by a signal? | Why this matters | Delta candidate? |
|-----------|------------------------------------------------|--------------------------|-----------------|-----------------|
| [most important] | [phrase from strategy.md] | [pending] | [failure mode] | yes |

Null case (Rule 3): `| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |`

---

### Step 3a — Signal Analyst (Read)

Glob `simulations/{topic}/` recursively. Read every file.

Null case (Rule 3): `> No signals found — strategy.md does not need revision at this time.`

Rule 1: `Consistent with strategy?` = Yes / No / Partial only.

| ID | File | Namespace | Skill | Date | Key Finding | Consistent with strategy? | Assumption link |
|----|------|-----------|-------|------|-------------|--------------------------|----------------|
| S-01 | | | | | | | |

---

### Step 3b — Assumption Archaeologist (Back-fill)

Replace each `[pending]`: `Contradicted — S-NN` | `Supported — S-NN` | `No signal coverage`

Reproduce full updated assumption table. After Step 4, update `yes` rows to `yes — F-NN`.

---

### Step 4 — Delta Identifier

Write: (1) the anti-pattern you're guarding against, (2) a PASS/FAIL exhibit showing
delta vs. inventory. Then build the findings table.

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root |
|-----------|-----------------|----------------|-----------------|----------------|
| F-01 | | | S-XX | |

Null case (Rule 3): `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |`

After findings, return to Step 3b and update `yes` rows to `yes — F-NN`.

---

### Step 5 — Coverage Auditor

All 9 namespaces by name. Stage-relative, not raw count.

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

### Step 6 — Conflict Detective

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

Null case (Rule 3): `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |`

---

### Step 7 — Proposal Architect

Write this word-for-word before the proposals table:

> "Proposals schema committed: Proposal ID ★, Type ★ [Rule 1: ADD / REMOVE / REPRIORITIZE],
> Change ★, Delta Finding ★ [Rule 4: full text + ID], Evidence ★, If unchanged ★ (no
> degradation = preference not decision), Reversibility ★ [Rule 1: (1)/(2)/(3)],
> Confidence ★. All three types. Empty types use Rule 3 null rows."

| Proposal ID | Type [Rule 1] | Change | Delta Finding [Rule 4] | Evidence | If unchanged | Reversibility [Rule 1] | Confidence |
|------------|--------------|--------|----------------------|----------|-------------|----------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [degradation] | (2) Gets harder | High |

Null rows (Rule 3):

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 8 — Diff Author

Write this word-for-word before the diff table:

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★
> (inline [file.md — ≤10 words]), Proposal ★ (ID from Step 7). No column omitted."

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | | | | ADD-1 |

---

### Step 9 — Confirmation gate

Reply **YES** to apply all proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 10 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals. Preserve
existing structure; update only sections affected.

---

## V-05 — Full Ceiling (V-01 + V-02 + V-03 + Pre-Read Hypothesis)

**Axes**: All R12 axes combined (conversational phrasing, expanded CONTRACT with 4
rules, namespace audit before delta) plus the pre-read hypothesis commitment from R11 V-01.

**Hypothesis**: Each axis contributes a distinct mechanism:
- Pre-read hypothesis (R11 V-01): makes the delta step falsifiable via pre-commitment;
  surprise findings reveal genuine blindspots.
- Conversational phrasing (R12 V-01): reduces cognitive friction without removing structure.
- Expanded CONTRACT with 4 rules (R12 V-02): front-loads all binding constraints; step
  bodies compressed.
- Namespace audit before delta (R12 V-03): makes namespace gaps available as delta sources
  at formation time.

The full ceiling tests whether all four mechanisms compose without interference or
diminishing returns. The pre-commit step is extended here to include namespace predictions:
"Which namespaces do you expect to have thin coverage?" allows the subsequent namespace
audit to score surprises.

---

You are running `topic:plan` for the topic `{topic}`.

Your job: revise `simulations/{topic}/strategy.md` based on signals gathered since it was
written. Before reading anything, commit to predictions. Then extract assumptions, read
signals, audit namespace coverage (before identifying deltas), identify deltas including
namespace gaps, check for conflicts, propose changes, and wait for a YES before writing.
Do not auto-apply.

---

### COLUMN CONTRACT — read this before anything else

Four rules govern every table you produce. Read all four before starting.

**Rule 1 — Enumerated columns**

Use only the declared values for closed-value columns. No prose, no paraphrasing.

What passes:
- `Type`: `ADD` | `REMOVE` | `REPRIORITIZE`
- `Reversibility`: `(1) Reversible at same cost` | `(2) Gets harder` | `(3) Becomes impossible`
- `Delta candidate?`: `yes` | `no` | `yes — F-NN`
- `Consistent with strategy?`: `Yes` | `No` | `Partial`
- `Namespace gap?`: `yes — NS-NAME` | `no`
- `Hypothesis match`: `H-N confirmed` | `Surprise — not hypothesized`

What fails (treated as blank):
- `Type`: "add a skill" | "addition" | "add/remove"
- `Reversibility`: "gets harder over time" | "might be irreversible"
- `Namespace gap?`: "probably yes" | "yes for some" | "depends"
- `Hypothesis match`: "mostly confirmed" | "partially predicted"

**Rule 2 — Column independence**

Before filling any cell, ask: *"Could I write this without opening the source document?"*
If yes, that cell is empty.

Why this matters: if you can fill `Implicit evidence` without reading strategy.md, the
column is decorative — you're recording what you already believed, not what the document
said.

What passes:

- PASS: `"teams run scout before draft"` — you had to read the rationale block
- PASS: `"signal count threshold never defined"` — you noticed its absence
- PASS: `"the phrase 'gather evidence first'"` — a verbatim quote you found
- PASS: `"no definition of done appears anywhere in the strategy"` — a gap you confirmed

What fails (treated as blank):

- FAIL: `A-01` — the row key
- FAIL: `"signals gather evidence"` — restatement of the assumption
- FAIL: `"see rationale section"` — pointer without content
- FAIL: `"strategy implies sequencing"` — inference you could make without reading

**Rule 3 — Null completeness**

Every section that runs must show its result, even when the result is nothing.

What passes:
- No conflicts: `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |`
- Empty ADD type: `| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |`
- Delta confirmed: `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A | no |`

What fails: empty sections with no null row; missing change types with no null row.

**Rule 4 — Two-level traceability**

Every proposal's `Delta Finding` cell must include the full "Strategy assumed [X] /
Signal revealed [Y]" text with the exact finding ID.

What passes: `F-01: Strategy assumed scout runs before draft / Signal revealed draft completed without scout artifacts`

What fails: `F-01` alone | `"S-01 suggests adding"` | delta text without ID.

---

### Output Schema — read before Step 0

Every table must match this schema. ★ columns are required.

**Hypothesis Table** (Step 0 only — 5 columns mandatory)
| ★ Hypothesis ID | ★ Predicted assumption | ★ Expected signal direction | ★ Expected delta | ★ Expected namespace gaps |

**Assumption Table** (5 columns — independently populated per Rule 2)
| ★ Assumption | ★ Implicit evidence [Rule 2 — PASS: phrase from strategy.md | FAIL: row key / restatement / pointer] | ★ Contradicted by a signal? | ★ Why this matters | ★ Delta candidate? [Rule 1] |

**Signal Inventory**
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? [Rule 1] | ★ Assumption link |

**Namespace Audit** (runs as Step 4 — before Delta)
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? | ★ Delta candidate? [Rule 1: yes — F-NN / no] | ★ Hypothesis match [Rule 1: H-N confirmed / Surprise — not hypothesized] |

**Delta Findings**
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) | ★ Assumption root (A-NN / "stated field" / "namespace gap") | ★ Namespace gap? [Rule 1: yes — NS-NAME / no] | ★ Hypothesis match [Rule 1: H-N confirmed / Surprise] |

**Conflict Audit**
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals** (Rules 1 and 4 apply)
| ★ Proposal ID | ★ Type [Rule 1] | ★ Change | ★ Delta Finding [Rule 4] | ★ Evidence | ★ If unchanged | ★ Reversibility [Rule 1] | ★ Confidence |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

Every ★ column required.

---

### Step 0 — Hypothesis Generator

Before reading anything, commit to predictions. Write at least one hypothesis. Don't
open any files until this step is complete.

These predictions are scored later. A finding that matches a hypothesis is **confirmed**.
A finding with no matching hypothesis is a **surprise** — flagged as highest-value.

Predict: (a) assumptions the strategy probably makes, (b) signal directions you expect,
(c) deltas you think will emerge, and (d) which namespaces you expect to have thin coverage.

Rule 1 applies to `Hypothesis match` columns throughout the output.

| Hypothesis ID | Predicted assumption | Expected signal direction | Expected delta | Expected namespace gaps |
|--------------|---------------------|---------------------------|----------------|------------------------|
| H-01 | [most likely unstated assumption] | [probably confirm / contradict] | [predicted delta text] | [namespace with likely thin coverage] |

At least one row. Don't read any files yet.

---

### Step 1 — Stated-Field Extractor

Read `simulations/{topic}/strategy.md`. Pull out exactly what it says. Don't infer.

| Field | Value |
|-------|-------|
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Stated rationale | |
| Acknowledged gaps | |

---

### Step 2 — Assumption Archaeologist (Extract)

Find what strategy.md assumed without writing. Scan: (a) audience knowledge, (b) namespace
priority ordering, (c) signal sufficiency, (d) timeline feasibility, (e) definition of done.

Before filling `Implicit evidence` for each row, apply the COLUMN CONTRACT Rule 2
PASS/FAIL exhibit. Ask: "Could I write this cell without reading strategy.md?" If yes,
the cell fails — find a phrase from the document instead.

`Contradicted?` = `[pending]` for now. `Why it matters` = failure mode. `Delta candidate?` = Rule 1.

| Assumption | Implicit evidence [Rule 2 test before filling] | Contradicted by a signal? | Why this matters | Delta candidate? |
|-----------|------------------------------------------------|--------------------------|-----------------|-----------------|
| [most important] | [phrase from strategy.md] | [pending] | [failure mode] | yes |

Null case (Rule 3): `| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |`

---

### Step 3a — Signal Analyst (Read)

Glob `simulations/{topic}/` recursively. Read every file.

Null case (Rule 3): `> No signals found — strategy.md does not need revision at this time.`

Rule 1 applies to `Consistent with strategy?`.

| ID | File | Namespace | Skill | Date | Key Finding | Consistent with strategy? | Assumption link |
|----|------|-----------|-------|------|-------------|--------------------------|----------------|
| S-01 | | | | | | | |

---

### Step 3b — Assumption Archaeologist (Back-fill)

Replace each `[pending]`: `Contradicted — S-NN` | `Supported — S-NN` | `No signal coverage`

Reproduce full updated assumption table. After Step 5, update `yes` rows to `yes — F-NN`.

---

### Step 4 — Coverage Auditor ← runs before Delta Identifier

Assess all 9 namespaces. For each namespace with zero signals that the strategy expected
coverage for, mark it as a delta candidate — you'll generate a finding at Step 5.

Check your Step 0 predictions: a namespace you didn't predict as thin is a **surprise**.

Rule 1 applies to `Delta candidate?` and `Hypothesis match`.

| Namespace | Signal Count | Stage-Relative Status | Action Needed? | Delta candidate? [yes — F-NN / no] | Hypothesis match [H-N confirmed / Surprise] |
|-----------|-------------|----------------------|----------------|-------------------------------------|---------------------------------------------|
| scout | | | | | |
| draft | | | | | |
| review | | | | | |
| flow | | | | | |
| trace | | | | | |
| prove | | | | | |
| listen | | | | | |
| program | | | | | |
| topic | | | | | |

---

### Step 5 — Delta Identifier

Write: (1) the anti-pattern you're guarding against, (2) a PASS/FAIL exhibit showing
delta vs. inventory. Then build the findings table. Include one finding per `yes`
namespace gap from Step 4. Check Step 0 hypotheses — mark each finding as confirmed
or surprise.

Rule 1 applies to `Namespace gap?` and `Hypothesis match`.

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root | Namespace gap? | Hypothesis match |
|-----------|-----------------|----------------|-----------------|----------------|---------------|-----------------|
| F-01 | | | S-XX | | yes — prove / no | H-01 confirmed / Surprise |

Null case (Rule 3): `| F-00 | Strategy confirmed | No gaps | All signals | N/A | no | N/A |`

After findings, return to Step 3b and update `yes` rows to `yes — F-NN`.

---

### Step 6 — Conflict Detective

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

Null case (Rule 3): `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |`

---

### Step 7 — Proposal Architect

Write this word-for-word before the proposals table:

> "Proposals schema committed: Proposal ID ★, Type ★ [Rule 1: ADD / REMOVE / REPRIORITIZE],
> Change ★, Delta Finding ★ [Rule 4: full text + ID], Evidence ★, If unchanged ★ (no
> degradation = preference not decision), Reversibility ★ [Rule 1: (1)/(2)/(3)],
> Confidence ★. All three types. Empty types use Rule 3 null rows."

| Proposal ID | Type [Rule 1] | Change | Delta Finding [Rule 4] | Evidence | If unchanged | Reversibility [Rule 1] | Confidence |
|------------|--------------|--------|----------------------|----------|-------------|----------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [degradation] | (2) Gets harder | High |

Null rows (Rule 3):

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 8 — Diff Author

Write this word-for-word before the diff table:

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★
> (inline [file.md — ≤10 words]), Proposal ★ (ID from Step 7). No column omitted."

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | | | | ADD-1 |

---

### Step 9 — Confirmation gate

Reply **YES** to apply all proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 10 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals. Preserve
existing structure; update only sections affected.
