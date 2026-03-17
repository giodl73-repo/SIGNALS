# topic-plan — Round 10 Variations (v9 rubric)

**Skill**: `topic:plan`
**Rubric**: v9 (C-01–C-35, 225 pts total)
**Date**: 2026-03-15

---

## Round 10 Design Notes

R9 set the ceiling at V-05 with implicit-evidence column in upfront schema (C-33) and
closed-enum Reversibility in upfront schema + commitment checkpoint (C-32). The two new
v9 criteria split across two precision layers:

- **Schema specificity** (C-34): enumerated-column valid-value constraints must appear at
  *both* declaration sites — upfront schema AND each schema-commitment checkpoint — for
  *every* enumerated column, not only Reversibility
- **Column independence** (C-35): each declared assumption table column must carry
  analytical content that cannot be derived from or replaced by the row identifier or any
  adjacent column — "Implicit evidence" must be an actual strategy.md citation, not a
  row key or assumption restatement

**What R9 achieved and where gaps remain:**

| Criterion | Best R9 mechanism | Gap R10 must close |
|-----------|-------------------|---------------------|
| C-34 | V-05: Reversibility closed-enum in upfront schema AND in Step 6 commitment checkpoint | Other enumerated columns (`Consistent with strategy?`: Yes/No/Partial; `Delta candidate?`: yes/no; `Type`: ADD/REMOVE/REPRIORITIZE) carry no closed-enum annotation at either site; commitment checkpoints for proposals name these columns without their valid values |
| C-35 | V-05: "Implicit evidence" column named in upfront schema + extraction step with archaeology framing | Extraction instruction says "cite the strategy.md phrase" but does not name the disqualification pattern: a model can fill the column with the assumption ID ("A-01"), a pointer ("same as above"), or a restatement ("signals gather evidence"), all of which preserve apparent column-count compliance while substituting navigational content for the required citation |

**Clarification on the C-34 scope (all enumerated columns):**

The five columns in the output schema that carry closed enumerated values:

1. **`Delta candidate?`** — `yes` / `no` (with `yes — F-NN` update after Step 3)
2. **`Consistent with strategy?`** — `Yes` / `No` / `Partial`
3. **`Type`** (proposals) — `ADD` / `REMOVE` / `REPRIORITIZE`
4. **`Reversibility`** (proposals) — `(1) Reversible at same cost` / `(2) Gets harder` /
   `(3) Becomes impossible`
5. *(optionally)* **`Delta candidate? update`** after Step 3 — `yes — F-NN` / `no`

C-34 requires each of these to appear in the upfront schema with its closed value list
and prose-prohibition, AND in every commitment checkpoint that names the column.

**Clarification on the C-35 discrimination test:**

For the "Implicit evidence" column, these fill patterns **fail** C-35:
- `A-01` (the row key itself)
- `see above` or `same as assumption`
- `The strategy mentions signals` (restatement in different words)

These fill patterns **pass** C-35:
- `"teams run scout before draft"` (direct quote from strategy.md)
- `"signal sufficiency not defined"` (close paraphrase of absent text)
- `"the phrase 'gather evidence first' in the rationale block"` (location + text)

The discrimination test: can the cell content be reproduced without reading strategy.md?
If yes, the column is a navigational alias. If no, it is an independent analytical dimension.

**Three single-axis dimensions explored in R10:**

1. **Output format (C-34)**: The upfront schema block annotates ALL five enumerated
   columns with their closed value lists and prose-prohibition. Commitment checkpoints at
   proposals and diff reproduce the enumeration for every enumerated column they name.

2. **Lifecycle emphasis (C-35)**: The assumption extraction step adds an explicit
   column-independence rule for "Implicit evidence" with a named anti-pattern
   ("row-key aliasing"), three fail examples, and one pass example, placed both in the
   upfront schema annotation and adjacent to the extraction step template.

3. **Phrasing register (C-34 + C-35)**: A pre-schema "COLUMN CONTRACT" block states two
   structural obligations as binding rules before the output schema — (a) every enumerated
   column carries its closed value list at every declaration site; (b) every declared
   column carries content not derivable from the row identity — using a decision-question
   ("Can this cell be filled without reading the source document?") as the independence test.

**Variation design:**

| Variation | Axis | Type | Primary R10 target |
|-----------|------|------|--------------------|
| V-01 | Output format — universal closed-enum at both declaration sites | Single | C-34 |
| V-02 | Lifecycle emphasis — Implicit evidence independence rule with anti-pattern examples | Single | C-35 |
| V-03 | Phrasing register — pre-schema COLUMN CONTRACT with decision-question independence test | Single | C-34 + C-35 |
| V-04 | Output format + Lifecycle — universal enum lock + independence rule combined | Combination | C-34 + C-35 |
| V-05 | Full stack — R9 V-05 base + universal enum lock + column independence contract + extraction anti-pattern | Combination | C-34 + C-35 + all R9 ceiling |

---

## V-01 — Universal Closed-Enum at Both Declaration Sites

**Axis**: Output format — every enumerated column in the output schema declares its
closed value list and prose-prohibition rule in the upfront schema block, and each
schema-commitment checkpoint reproduces the annotation for every enumerated column it
names

**Hypothesis**: R9 V-01 placed the three-value Reversibility enum inside the upfront
schema column header and blocked prose fill. C-34 requires the same treatment for every
enumerated column — `Delta candidate?`, `Consistent with strategy?`, `Type`, and
`Reversibility` — at both the upfront schema site and at each commitment checkpoint. R9
commitment checkpoints named "Reversibility ★" with the three values; they named
"Consistent with strategy?" and "Delta candidate?" without any value list, leaving those
fields open to prose fill. V-01 extends the enum-lock mechanism uniformly: every
enumerated column header in the upfront schema carries `[select: X / Y / Z; prose not
a valid value]`; every commitment statement that names an enumerated column reproduces
its valid-value selector. Single-axis: universal enum annotation only; no column
independence rule (C-35 mechanism isolated).

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it
was written. The assumption table you build is a two-way bridge: backward from strategy
beliefs to signal evidence (back-fill after Step 2), and forward to delta findings and
proposals (candidate designation updated after Step 3). Present proposals, wait for
confirmation, then write. Do not auto-apply changes.

---

### Output Schema (read before proceeding to Step 1)

Every table you produce must conform to this schema. Columns marked ★ are mandatory —
do not omit any ★ column. For every enumerated column, select from the listed values
only; prose is not a valid value.

**Assumption Table** (5 columns mandatory)
| ★ Assumption ID | ★ What assumed without writing | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? [select: yes / no; update to yes — F-NN after Step 3; prose not a valid value] |

**Signal Inventory**
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding (1 sentence) | ★ Consistent with strategy? [select: Yes / No / Partial; prose not a valid value] | ★ Assumption link (A-NN / "stated field" / "none") |

**Delta Findings**
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) | ★ Assumption root (A-NN / "stated field") |

**Namespace Audit**
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |

**Conflict Audit**
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals** — all enumerated columns require selecting from the listed values; prose
is not a valid value for any enumerated column:
| ★ Proposal ID | ★ Type [select: ADD / REMOVE / REPRIORITIZE; prose not a valid value] | ★ Change | ★ Delta Finding | ★ Evidence | ★ If unchanged | ★ Reversibility [select: (1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible; prose not a valid value] | ★ Confidence |

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

Find what strategy.md took for granted without writing. These are the highest-value
delta candidates — a signal can contradict what was assumed, not only what was stated.

Scan across at least five dimensions: (a) implied audience knowledge level, (b) namespace
priority ordering, (c) signal sufficiency threshold, (d) timeline or sequencing feasibility,
(e) definition of "done" for this topic.

**The following columns are mandatory. Do not omit any column.**

Column rules:
- **"Contradicted by a signal?"**: Write `[pending]` now. Fill after Step 2.
- **"Why this matters"**: Fill now. Name the failure mode if this assumption is wrong.
- **"Delta candidate?"**: Fill now. Write `yes` or `no` — **select one; prose not valid**.
  After Step 3, update `yes` rows to `yes — F-NN`.

| Assumption ID | What strategy.md assumed without writing | Contradicted by a signal? | Why this matters for delta detection | Delta candidate? [yes / no] |
|--------------|------------------------------------------|--------------------------|--------------------------------------|------------------------------|
| A-01 | [most important — highest likelihood of signal contradiction] | [pending] | [failure mode if wrong] | yes |
| A-02 | [second assumption, if any] | [pending] | | yes / no |

Write at least one row. Null case:

| A-00 | No unstated assumptions found after systematic scan | N/A | N/A | no |

---

### Step 2 — Read signal artifacts

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals found** — reproduce the following verbatim and stop. Do not omit:

> No signals found — strategy.md does not need revision at this time.

**The following columns are mandatory. Do not omit any column.**

For `Consistent with strategy?`: select `Yes`, `No`, or `Partial` — prose not a valid value.

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? [Yes / No / Partial] | Assumption link (A-NN / "stated field" / "none") |
|----|------|-----------|-------|------|--------------------------|-------------------------------------------------|--------------------------------------------------|
| S-01 | | | | | | Yes / No / Partial | |

**After building this table, return to Step 1b and fill "Contradicted by a signal?" for
each A-NN row.** For each contradicted assumption: cite the S-NN ID and write one sentence.
For uncontradicted: "Not contradicted — assumption stands." For uncovered: "No signal coverage."

---

### Step 3 — Identify the delta

Stop. Before building the findings table, write the name of the anti-pattern you are
guarding against at this step.

**The following columns are mandatory. Do not omit any column.**

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root (A-NN / "stated field") |
|-----------|-----------------|----------------|-----------------|----------------------------------------|
| F-01 | [from Step 1a stated fields or Step 1b assumptions] | | S-XX | |

After building findings, return to Step 1b and update "Delta candidate?" — change `yes`
to `yes — F-NN` for rows that produced a finding.

**Null case — all signals confirm** — reproduce verbatim and skip to Step 5:

| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |

---

### Step 4 — Namespace coverage audit

Assess all 9 namespaces by name. Stage-relative = appropriate for the topic's current
stage, not a raw count.

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

**The following columns are mandatory. Do not omit any column.**

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

**Null case — no conflicts** — reproduce verbatim. Do not omit this table:

| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

---

### Step 6 — Proposals

**Stop. Before building the proposals table, write the following statement verbatim:**

> "Proposals schema committed: Proposal ID ★, Type ★ [select: ADD / REMOVE /
> REPRIORITIZE; prose not a valid value], Change ★, Delta Finding ★ (full 'Strategy
> assumed [X] / Signal revealed [Y]' text from Step 3 with exact ID), Evidence ★,
> If unchanged ★ (specific degradation — a row that cannot name a specific degradation
> is a preference, not a decision), Reversibility ★ [select: (1) Reversible at same cost /
> (2) Gets harder / (3) Becomes impossible; prose not a valid value], Confidence ★.
> All three types present. Empty types use null rows."

**The following columns are mandatory. Do not omit any column.**

| Proposal ID | Type [ADD / REMOVE / REPRIORITIZE] | Change | Delta Finding | Evidence [file(s)] | If unchanged [specific degradation — not a delta finding synonym] | Reversibility [(1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible] | Confidence |
|------------|-------------------------------------|--------|--------------|-------------------|--------------------------------------------------------------------|----------------------------------------------------------------------------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [which artifact won't be gathered / which gap compounds] | (2) Gets harder | High |

Null rows — reproduce verbatim for each empty type:

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 7 — Before/after diff

**Stop. Before building the diff table, write the following statement verbatim:**

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★
> (inline per row as [file.md — ≤10 word finding] — no separate evidence section),
> Proposal ★ (Proposal ID from Step 6). No column omitted."

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

## V-02 — Implicit Evidence Column Independence Rule

**Axis**: Lifecycle emphasis — the "Implicit evidence" column definition in the upfront
schema and at the extraction step names the anti-pattern it guards against ("row-key
aliasing"), provides three concrete fail examples and one pass example, and states the
independence disqualification condition

**Hypothesis**: R9 V-02 introduced the Implicit evidence column with an instruction to
"cite the strategy.md phrase that implies the assumption." C-35 requires more: the
column definition must make the disqualification condition explicit and name what counts
as a structural alias. Without named failure examples, a model can fill the column with
"A-01" (the row key), "signals gather evidence" (a restatement), or "see the strategy
rationale" (a pointer) — each preserves column-count compliance while removing the
archaeological citation. This variation adds three explicit fail patterns and one pass
pattern adjacent to the column definition in both the upfront schema and the extraction
step. The hypothesis: named anti-pattern examples make the independence requirement
self-enforcing at fill time — the model confronts the fail list before completing the
cell. Single-axis: independence rule for Implicit evidence only; no universal enum
annotation for non-Reversibility columns (C-34 mechanism isolated separately).

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it
was written. Present proposals, wait for confirmation, then write. Do not auto-apply
changes.

**Before reading any files, review the complete output schema below.** Every table you
produce must conform to this schema. Columns marked ★ are mandatory.

---

### Output Schema (read before proceeding to Step 1)

**Assumption Table** — five content columns mandatory. The "Implicit evidence" column
requires a short phrase or clause quoted or paraphrased from strategy.md that implies the
assumption existed. It is NOT satisfied by: (a) a row key or ID, (b) a restatement of
the assumption in different words, (c) a pointer such as "see rationale." It IS
satisfied by: a specific phrase from strategy.md that would lead a reader to infer the
assumption was made (e.g., "teams run scout before draft" reveals a sequencing assumption;
"signal count determines readiness" reveals a sufficiency assumption).

| ★ Assumption | ★ Implicit evidence — quote/paraphrase from strategy.md that implies this assumption [NOT: row ID, restatement, pointer] | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? |

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

Read `simulations/{topic}/strategy.md`.

**Stated fields** — the following columns are mandatory. Do not omit any column:

| Field | Value |
|-------|-------|
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Stated rationale | |
| Acknowledged gaps | |

**Unstated assumptions** — per schema (Assumption Table). The following columns are
mandatory. Do not omit any column. "Contradicted?" is filled after Step 2 — write
`[pending]` as placeholder.

**Column rule — Implicit evidence**: Find the specific phrase in strategy.md that reveals
this assumption. Fill with text from the document, not with:
- The assumption ID (e.g., "A-01") — this is a navigational alias
- A restatement (e.g., "scouts are done first") — this reproduces the assumption without citing evidence
- A pointer (e.g., "see rationale section") — this defers without delivering

Fill with text that could only come from reading strategy.md:
- A quoted phrase: `"teams run scout before draft"`
- A paraphrase of absent text: `"signal count is never defined as a threshold"`

Leave blank only if systematic scan finds no strategy text that implies the assumption.

| Assumption | Implicit evidence [quote/paraphrase from strategy.md — NOT row ID, restatement, or pointer] | Contradicted by a signal? | Why this matters for delta detection | Delta candidate? |
|-----------|----------------------------------------------------------------------------------------------|--------------------------|--------------------------------------|-----------------|
| [most important for delta detection] | [short phrase from strategy.md only — fail: "A-01" / "same as above" / "see rationale"] | [pending] | [failure mode if wrong] | yes / no |

Write at least one row. Null case: "No unstated assumptions found after systematic scan."

---

### Step 2 — Read signal artifacts

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals found** — reproduce the following verbatim and stop. Do not omit:

> No signals found — strategy.md does not need revision at this time.

Per schema (Signal Inventory) — the following columns are mandatory. Do not omit any column:

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? | Assumption link (A-NN / "stated field" / "none") |
|----|------|-----------|-------|------|--------------------------|---------------------------|--------------------------------------------------|
| S-01 | | | | | | Yes / No / Partial | |

After building this table, return to Step 1 and fill "Contradicted by a signal?" for
each assumption row.

---

### Step 3 — Identify the delta

Stop. Before building the findings table, write the name of the anti-pattern you are
guarding against at this step. Then write one sentence: what the delta IS vs. what it IS NOT.

Per schema (Delta Findings) — the following columns are mandatory. Do not omit any column:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root |
|-----------|-----------------|----------------|-----------------|-----------------|
| F-01 | | | S-XX | |

**Null case — all signals confirm** — reproduce verbatim and skip to Step 5:

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

| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

---

### Step 6 — Proposals

Before building the proposals table, write the following statement verbatim:

> "Proposals schema committed: Proposal ID ★, Type ★, Change ★, Delta Finding ★ (full
> 'Strategy assumed [X] / Signal revealed [Y]' text from Step 3 with exact ID), Evidence ★,
> If unchanged ★ (specific degradation — a row that cannot name a specific degradation
> here is a preference, not a decision), Reversibility ★, Confidence ★. All three types
> present. Empty types use null rows."

Per schema (Proposals) — the following columns are mandatory. Do not omit any column.

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Reversibility [(1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible — select one] | Confidence |
|------------|------|--------|--------------|-------------------|--------------|----------------------------------------------------------------------------------------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [specific gap that persists or worsens] | (2) Gets harder | High |

Null rows (reproduce verbatim for each empty type):

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

## V-03 — Pre-Schema COLUMN CONTRACT with Decision-Question Independence Test

**Axis**: Phrasing register — a pre-schema COLUMN CONTRACT block states two structural
obligations as binding rules before the output schema: (a) every enumerated column
declares its closed value list at every declaration site; (b) every declared column
carries content not derivable from the row identity; using a decision-question ("Can
this cell be filled without reading the source document?") as the column independence test

**Hypothesis**: R9 scattered constraint declarations across multiple steps — enum
annotation in the column header (upfront schema), prose-prohibition in the commitment
checkpoint, column-completeness declaration adjacent to each template. Both C-34 and C-35
can be collapsed into a single pre-reading contract that a model evaluates before
encountering any step-specific instruction. The conversational decision-question format —
"Can this cell be filled without reading the source document? If yes, it is a structural
alias and is treated as absent" — makes the independence test executable without
requiring the model to know what "navigational alias" or "row-key substitution" means as
technical terms. The decision-question also generalizes naturally: a model asked "Can I
fill 'Delta candidate?' without reading step output?" answers "no" and is forced to
commit to a value after reasoning. Single-axis: the CONTRACT framing as a register choice
is the discriminator; the specific mechanisms (enum annotations, Implicit evidence rule)
follow from the contract rather than being added per-column.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it
was written. The assumption table is a two-phase artifact: extract (Step 1b), then
back-fill after signals are read (Step 2b). Present proposals, wait for confirmation,
then write. Do not auto-apply changes.

---

### COLUMN CONTRACT (binding before reading any file)

Two rules govern every table you produce:

**Rule 1 — Enumerated columns**: Any column that uses a closed value set must declare
those values at every point where the column is named. When writing a cell in an
enumerated column, select from the declared set. Do not write prose.

**Rule 2 — Column independence**: Before filling any cell, ask: *"Can I fill this cell
without reading the source document?"* If yes, the cell contains a structural alias —
it restates, points to, or duplicates information available from the row identifier or an
adjacent column. Structural aliases are treated as empty cells regardless of content.

Rule 2 applies especially to the "Implicit evidence" column in the Assumption Table:
that column must contain text from strategy.md — a phrase, clause, or paraphrase that a
reader could trace back to a specific location. A cell containing the assumption ID,
the assumption text in other words, or a pointer ("see above") cannot pass the
decision-question test and is treated as absent.

---

### Output Schema (read before proceeding to Step 1)

Every table you produce must conform to this schema. Columns marked ★ are mandatory —
do not omit any ★ column. Both Contract Rules apply to every ★ column.

**Assumption Table** (5 columns — all independently populated per Rule 2)
| ★ Assumption | ★ Implicit evidence [text from strategy.md — Rule 2 applies; test: "Can I fill this without reading strategy.md?" — if yes, this fails] | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? [select: yes / no — Rule 1 applies; update to yes — F-NN after Step 3] |

**Signal Inventory**
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? [select: Yes / No / Partial — Rule 1 applies] | ★ Assumption link |

**Delta Findings**
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) | ★ Assumption root |

**Namespace Audit**
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |

**Conflict Audit**
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals** (Rule 1 applies to Type and Reversibility)
| ★ Proposal ID | ★ Type [select: ADD / REMOVE / REPRIORITIZE] | ★ Change | ★ Delta Finding | ★ Evidence | ★ If unchanged | ★ Reversibility [select: (1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible] | ★ Confidence |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

Do not omit any ★ column.

---

### Step 1a — Role: Stated-Field Extractor

**Adopt this role**: Extract only what strategy.md wrote explicitly.

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
granted without writing — the implied worldview, the unstated preconditions, the beliefs
the author would defend if challenged but never put in the document.

Systematic scan — cover each dimension:
- (a) Implied audience knowledge level
- (b) Namespace priority ordering assumed without justification
- (c) Signal sufficiency threshold — what "enough signals" means here
- (d) Timeline or sequencing feasibility
- (e) Definition of "done" for this topic

Per schema (Assumption Table) — all five columns are mandatory. Both Contract Rules apply.
Apply the decision-question test to "Implicit evidence" before completing each row.

Column rules:
- **"Contradicted by a signal?"**: Write `[pending]` now. Filled in Step 2b.
- **"Why this matters"**: Fill now. Name the failure mode if this assumption is wrong —
  which skills or namespaces would change priority.
- **"Delta candidate?"**: Apply Rule 1 — select `yes` or `no`. Do not write prose.
  After Step 3, update `yes` rows to `yes — F-NN`.

| Assumption | Implicit evidence [text from strategy.md — test: "Can I fill this without reading strategy.md?"] | Contradicted by a signal? | Why this matters for delta detection | Delta candidate? [yes / no] |
|-----------|---------------------------------------------------------------------------------------------------|--------------------------|--------------------------------------|------------------------------|
| [most important — highest likelihood of signal contradiction] | [phrase from strategy.md that reveals this assumption — fails test if it's the assumption ID, a restatement, or a pointer] | [pending] | [failure mode if wrong] | yes |

Write at least one row. Null case:

| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |

---

### Step 2a — Role: Signal Analyst — Read phase

**Adopt this role**: Read every artifact against two reference points: (a) stated fields
from Step 1a, and (b) assumptions from Step 1b.

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals found** — reproduce the following verbatim and stop. Do not omit:

> No signals found — strategy.md does not need revision at this time.

Per schema (Signal Inventory) — the following columns are mandatory. Apply Rule 1 to
`Consistent with strategy?` — select `Yes`, `No`, or `Partial`:

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? [Yes / No / Partial] | Assumption link (A-NN / "stated field" / "none") |
|----|------|-----------|-------|------|--------------------------|------------------------------------------------|--------------------------------------------------|
| S-01 | | | | | | | |

---

### Step 2b — Role: Assumption Archaeologist — Back-fill phase

**Return to this role**: Adjudicate every assumption against the full signal set.

For each A-NN row, replace `[pending]` with exactly one verdict:
- **Contradicted — S-NN**: Signal challenges this assumption. Cite ID, one sentence.
- **Supported — S-NN**: Signal confirms this assumption. Cite ID.
- **No signal coverage**: No signal speaks to this assumption.

Reproduce the full updated Assumption Table (all 5 columns). Every row must have a verdict.

After completing Step 3, return here and update `yes` rows to `yes — F-NN`.

---

### Step 3 — Role: Delta Identifier

**Adopt this role**: Name the gap between strategy beliefs and signal evidence.

Stop. Before building the findings table, produce both outputs:
1. **Anti-pattern label**: Write the name of the anti-pattern you are guarding against.
2. **Delta definition**: Delta IS: [gap between belief and signal]. Delta IS NOT: [inventory of
   signal existence].

Per schema (Delta Findings) — the following columns are mandatory. Do not omit any column:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root (A-NN / "stated field") |
|-----------|-----------------|----------------|-----------------|----------------------------------------|
| F-01 | | | S-XX | |

**Null case** — reproduce verbatim and skip to Step 5:

| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |

---

### Step 4 — Role: Coverage Auditor

Per schema (Namespace Audit) — the following columns are mandatory. Assess stage-relative
completeness — not raw count:

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

Per schema (Conflict Audit) — the following columns are mandatory:

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

**Null case** — reproduce verbatim. Do not omit:

| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

---

### Step 6 — Role: Proposal Architect

**Stop. Before building the proposals table, write the following statement verbatim:**

> "Proposals schema committed: Proposal ID ★, Type ★ [ADD / REMOVE / REPRIORITIZE —
> Rule 1: select one; prose not valid], Change ★, Delta Finding ★ (full 'Strategy
> assumed [X] / Signal revealed [Y]' text from Step 3 with exact Finding ID), Evidence ★,
> If unchanged ★ (specific degradation — a row that cannot name a specific degradation
> is a preference, not a decision), Reversibility ★ [(1) Reversible at same cost /
> (2) Gets harder / (3) Becomes impossible — Rule 1: select one; prose not valid],
> Confidence ★. All three types present. Empty types use null rows."

Per schema (Proposals) — all columns mandatory. Apply Rule 1 to Type and Reversibility.

| Proposal ID | Type [ADD / REMOVE / REPRIORITIZE] | Change | Delta Finding | Evidence [file(s)] | If unchanged [specific degradation — a row that cannot name one is a preference, not a decision] | Reversibility [(1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible] | Confidence |
|------------|-------------------------------------|--------|--------------|-------------------|-------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [specific degradation] | (2) Gets harder | High |

Null rows (reproduce verbatim):

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 7 — Role: Diff Author

**Stop. Before building the diff table, write the following statement verbatim:**

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★
> (inline per row as [file.md — ≤10 word finding] — no separate evidence section),
> Proposal ★ (Proposal ID from Step 6). No column omitted."

Per schema (Diff) — all columns mandatory:

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

## V-04 — Universal Enum Lock + Implicit Evidence Independence Rule

**Axes**: Output format (V-01: every enumerated column carries closed value list +
prose-prohibition at both the upfront schema and each commitment checkpoint) + Lifecycle
emphasis (V-02: "Implicit evidence" column carries explicit independence rule with named
anti-pattern examples at extraction step)

**Hypothesis**: V-01 closes C-34 by extending the enum-lock mechanism from Reversibility
to all enumerated columns at both declaration sites. V-02 closes C-35 by naming the
disqualification condition for Implicit evidence with three fail examples and one pass
example. Each is individually targeted at one new criterion. The combination tests whether
the two mechanisms compose cleanly: C-34 is a schema-specificity constraint (column
headers carry their value sets); C-35 is a content-independence constraint (column cells
carry non-derivable content). They operate at different levels of the output structure —
declaration vs. population — and should not interfere. V-04 uses R9 V-04 as its base
(role sequence + schema-first + upfront schema) and layers V-01 enum universalization +
V-02 independence rule on top.

---

You are executing `topic:plan` for the topic `{topic}`.

**Before reading any files, review the complete output schema below.** Every table you
produce must conform to this schema. Columns marked ★ are mandatory. You will adopt a
named cognitive role at each phase. The structural contract below governs output
regardless of role.

Two pre-reading commitments:
1. **Enumerated columns**: Every enumerated column declares its closed value list here.
   At each commitment checkpoint, the same values are reproduced. Prose is not a valid
   value for any enumerated column.
2. **Implicit evidence independence**: The "Implicit evidence" column in the Assumption
   Table must contain text from strategy.md. It is NOT satisfied by a row ID, a
   restatement of the assumption, or a pointer. The fill test: "Is this text derivable
   without reading strategy.md?" — if yes, the cell fails.

---

### Output Schema (read before proceeding to Step 1)

**Assumption Table** — five content columns mandatory; all independently populated:
| ★ Assumption | ★ Implicit evidence — short phrase/clause from strategy.md that implies this assumption [NOT: row ID / restatement / pointer; test: must come from reading strategy.md] | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? [select: yes / no; update to yes — F-NN after Step 3; prose not a valid value] |

**Signal Inventory**
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? [select: Yes / No / Partial; prose not a valid value] | ★ Assumption link (A-NN / "stated field" / "none") |

**Delta Findings**
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) | ★ Assumption root (A-NN / "stated field") |

**Namespace Audit**
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |

**Conflict Audit**
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals** — all enumerated columns require selecting from listed values; prose not valid:
| ★ Proposal ID | ★ Type [select: ADD / REMOVE / REPRIORITIZE; prose not a valid value] | ★ Change | ★ Delta Finding | ★ Evidence | ★ If unchanged | ★ Reversibility [select: (1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible; prose not a valid value] | ★ Confidence |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

**Traceability obligation**: Every Proposal row must trace backward — Diff (Proposal ID) →
Proposals (Delta Finding) → Delta Findings (Finding ID) → Assumption Table (Assumption).
Every chain hop must be filled.

Do not omit any ★ column.

---

### Step 1a — Role: Stated-Field Extractor

**Adopt this role**: Extract only what strategy.md wrote explicitly. Do not interpret,
infer, or supplement.

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
granted without writing — the implied worldview, the unstated preconditions, the beliefs
the author would defend if challenged but never put in the document. These are the
highest-value delta candidates.

For each assumption, you have two obligations: (1) name the assumption; (2) cite the
strategy.md phrase that implies it. Obligation 2 is the archaeology obligation. Do not
fill "Implicit evidence" with:
- The assumption ID — that is a navigational alias, not a citation
- A restatement of the assumption — that is self-referential, not evidence
- "See rationale" or any pointer — that defers without delivering

Fill "Implicit evidence" with text that can only come from reading strategy.md — a phrase
that, if read by someone who didn't see your assumption, would lead them to the same
inference.

Systematic scan — cover each dimension explicitly:
- (a) Implied audience knowledge level
- (b) Namespace priority ordering assumed without justification
- (c) Signal sufficiency threshold — what "enough signals" means here
- (d) Timeline or sequencing feasibility
- (e) Definition of "done" for this topic

Per schema (Assumption Table) — all five columns mandatory.

Column rules:
- **"Contradicted by a signal?"**: Write `[pending]` now. Filled in Step 2b.
- **"Why this matters"**: Fill now. Which skills or namespaces would change priority if
  this assumption is wrong?
- **"Delta candidate?"**: Apply Rule 1 — select `yes` or `no`. After Step 3, update `yes`
  rows to `yes — F-NN`.

| Assumption | Implicit evidence [phrase from strategy.md — NOT: ID / restatement / pointer] | Contradicted by a signal? | Why this matters for delta detection | Delta candidate? [yes / no] |
|-----------|--------------------------------------------------------------------------------|--------------------------|--------------------------------------|------------------------------|
| [most important — highest likelihood of signal contradiction] | [strategy.md phrase that reveals this assumption to a reader] | [pending] | [failure mode if wrong] | yes |
| [second assumption, if any] | [phrase, or blank only if no strategy text implies it] | [pending] | | yes / no |

Write at least one row. Null case: "No unstated assumptions found after systematic scan."

---

### Step 2a — Role: Signal Analyst — Read phase

**Adopt this role**: Read every artifact against two reference points: (a) stated fields
from Step 1a, and (b) assumptions from Step 1b.

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals found** — reproduce verbatim and stop. Do not omit:

> No signals found — strategy.md does not need revision at this time.

Per schema (Signal Inventory) — the following columns are mandatory. `Consistent with
strategy?` requires selecting `Yes`, `No`, or `Partial` — prose not valid:

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? [Yes / No / Partial] | Assumption link (A-NN / "stated field" / "none") |
|----|------|-----------|-------|------|--------------------------|------------------------------------------------|--------------------------------------------------|
| S-01 | | | | | | Yes / No / Partial | |

---

### Step 2b — Role: Assumption Archaeologist — Back-fill phase

**Return to this role**: Adjudicate every assumption from Step 1b against the full signal set.

For each row, replace `[pending]` with exactly one verdict. Do not leave any row as `[pending]`:
- **Contradicted — S-NN**: Signal challenges this assumption. Cite ID, one sentence.
- **Supported — S-NN**: Signal confirms this assumption. Cite ID.
- **No signal coverage**: No signal speaks to this assumption.

Reproduce the full updated Assumption Table (all 5 columns). Every row must have a verdict.

After completing Step 3, return here and update `yes` entries to `yes — F-NN`.

---

### Step 3 — Role: Delta Identifier

**Adopt this role**: Name the gap between strategy beliefs and signal evidence.

**Stop. Before building the findings table, produce both outputs:**
1. **Anti-pattern label**: Name the anti-pattern you are guarding against. Write the label.
2. **Delta definition**: Delta IS: [gap between belief and signal]. Delta IS NOT: [inventory
   of signal existence].

Per schema (Delta Findings) — the following columns are mandatory. Do not omit any column:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root (A-NN / "stated field") |
|-----------|-----------------|----------------|-----------------|----------------------------------------|
| F-01 | | | S-XX | |

After completing findings, return to Step 2b and update all `yes` entries with F-NN IDs.

**Null case** — reproduce verbatim and skip to Step 5:

| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |

---

### Step 4 — Role: Coverage Auditor

Per schema (Namespace Audit) — the following columns are mandatory. Stage-relative
completeness — not raw count:

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

Per schema (Conflict Audit) — the following columns are mandatory:

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

**Null case** — reproduce verbatim. Do not omit:

| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

---

### Step 6 — Role: Proposal Architect

**Adopt this role**: Translate each finding into a typed, defensible proposal. Every
Proposal ID must trace to a Finding ID and from there to an Assumption.

**Stop. Before building the proposals table, write the following statement verbatim:**

> "Proposals schema committed: Proposal ID ★, Type ★ [select: ADD / REMOVE /
> REPRIORITIZE; prose not a valid value], Change ★, Delta Finding ★ (full 'Strategy
> assumed [X] / Signal revealed [Y]' text from Step 3 with exact Finding ID),
> Evidence ★, If unchanged ★ (specific degradation — a row that cannot name a specific
> degradation is a preference, not a decision), Reversibility ★ [select: (1) Reversible
> at same cost / (2) Gets harder / (3) Becomes impossible; prose not a valid value; a row
> that cannot select one has not reasoned about the deferral window], Confidence ★.
> All three types present. Empty types use null rows."

Per schema (Proposals) — all columns mandatory. Rule 1 applies to Type and Reversibility.

**Column rules:**
- **"If unchanged"**: Name the specific artifact that won't be gathered, the decision that
  becomes harder, or the gap that compounds. A row that writes a synonym of the delta
  finding here is a preference, not a decision.
- **"Reversibility"**: Select one from the three values committed above. No prose.

| Proposal ID | Type [ADD / REMOVE / REPRIORITIZE] | Change | Delta Finding | Evidence [file(s)] | If unchanged [specific degradation] | Reversibility [(1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible] | Confidence |
|------------|-------------------------------------|--------|--------------|-------------------|------------------------------------|----------------------------------------------------------------------------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [specific degradation] | (2) Gets harder | High |

Null rows (reproduce verbatim):

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 7 — Role: Diff Author

**Adopt this role**: Show the exact before/after for every confirmed proposal.

**Stop. Before building the diff table, write the following statement verbatim:**

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★
> (inline per row as [file.md — ≤10 word finding] — no separate section), Proposal ★
> (Proposal ID from Step 6 — entry point into Proposal → Delta Finding → Assumption chain).
> No column omitted."

Per schema (Diff) — all columns mandatory:

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

## V-05 — Full Stack: R9 V-05 + Universal Enum Lock + Column Independence Contract + Extraction Anti-Pattern

**Axes**: All R9 V-05 mechanisms + universal closed-enum annotation at both declaration
sites for every enumerated column (C-34) + pre-schema COLUMN CONTRACT with
decision-question independence test (C-35) + "Implicit evidence" anti-pattern examples
at extraction with three fail cases and one pass case

**Hypothesis**: R9 V-05 set the ceiling with C-32+C-33 added to the
C-28+C-29+C-30+C-31 stack. C-34 is the second-site requirement for enums: R9 V-05
closes C-32 by placing the three-value Reversibility enum in the upfront schema AND
the Step 6 commitment checkpoint. C-34 extends this: (a) all other enumerated columns
(`Consistent with strategy?`, `Delta candidate?`, `Type`) must also carry their closed
value sets in the upfront schema; (b) every commitment checkpoint that names an
enumerated column must reproduce its valid-value selector. C-35 closes the content gap
in C-33: R9 V-05's "Implicit evidence" column carries an archaeology framing, but the
model can still fill it with the assumption ID or a restatement while appearing compliant.
C-35 requires the column's disqualification condition to be explicit — three concrete
fail patterns and one pass pattern, placed at both the upfront schema annotation and the
extraction step. The pre-schema COLUMN CONTRACT from V-03 generalizes both constraints
into a single pre-reading structural commitment that governs all tables. The full-stack
V-05 tests whether all three mechanisms (universal enum, column independence contract,
extraction anti-patterns) interact constructively with the existing R9 V-05 architecture
— specifically, whether the additional precision constraints change the behavior of
models that were already passing C-32 and C-33 partially.

---

You are executing `topic:plan` for the topic `{topic}`.

**Before reading any files, review the COLUMN CONTRACT and output schema below.** Every
table you produce must conform to this contract. Columns marked ★ are mandatory — a
table missing any ★ column fails schema validation regardless of other content.

---

### COLUMN CONTRACT (binding before any file is read)

**Rule 1 — Enumerated columns**: Every enumerated column declares its closed value set
at every site where the column is named — upfront schema AND every commitment checkpoint.
Select from the declared values only. Prose is not a valid value for any enumerated column.

**Rule 2 — Column independence**: Before filling any cell, apply the independence test:
*"Can this cell be filled correctly without reading the source document?"* A cell that
passes this test contains a structural alias — it is derived from the row identifier,
restates an adjacent column, or is otherwise reconstructable without the source. Structural
aliases are treated as absent regardless of the text they contain.

Rule 2 applies to every column, but applies most critically to "Implicit evidence":
- **FAILS**: `A-01` (row key) | `"first run scout"` when the assumption IS "scout runs
  first" (restatement) | `"see rationale"` (pointer without delivery)
- **PASSES**: `"teams run scout before draft"` (quoted strategy text) | `"signal count
  is never defined"` (paraphrase of absent text) | `"the phrase 'gather evidence first'
  in Section 2"` (location + text)

The independence test for "Implicit evidence": the cell must contain text that a reader
could trace back to a specific location in strategy.md. If it cannot be traced, it fails.

Three pre-reading commitments made here:
1. Assumption table schema — five content columns including "Implicit evidence" — committed
   before strategy.md is read.
2. Reversibility taxonomy — three enumerated values; prose not valid — committed before
   any proposal scenario is encountered.
3. All other enumerated columns — their value sets are declared below and reproduced at
   every commitment checkpoint.

---

### Output Schema (read before proceeding to Step 1)

**Assumption Table** (5 content columns — full pre-reading contract — Rule 2 applies to all)
| ★ Assumption | ★ Implicit evidence [text from strategy.md traced to a specific phrase — FAILS: row ID / restatement / pointer; PASSES: quoted or paraphrased strategy.md text that reveals the assumption] | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? [select: yes / no — Rule 1; update to yes — F-NN after Step 3] |

**Signal Inventory**
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? [select: Yes / No / Partial — Rule 1; prose not valid] | ★ Assumption link (A-NN / "stated field" / "none") |

**Delta Findings**
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) | ★ Assumption root (A-NN / "stated field") |

**Namespace Audit**
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |

**Conflict Audit**
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals** — Rule 1 applies to Type and Reversibility at this declaration site AND
at the Step 6 commitment checkpoint:
| ★ Proposal ID | ★ Type [select: ADD / REMOVE / REPRIORITIZE — Rule 1; prose not valid] | ★ Change | ★ Delta Finding | ★ Evidence | ★ If unchanged | ★ Reversibility [select: (1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible — Rule 1; prose not valid] | ★ Confidence |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

**Traceability obligation**: Every Proposal row must be traceable backward — Diff
(Proposal ID) → Proposals (Delta Finding) → Delta Findings (Finding ID) → Assumption
Table (Assumption). Every chain hop must be filled. Schema compliance alone is
insufficient — the chain must be walkable.

Do not omit any ★ column.

---

### Step 1a — Role: Stated-Field Extractor

**Adopt this role**: Extract only what strategy.md wrote explicitly. Do not interpret,
infer, or supplement.

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
granted without writing — the implied worldview, the unstated preconditions, the beliefs
the author would defend if challenged but never put in the document. These are the
highest-value delta candidates.

Your extraction has two obligations per assumption:
1. **Name the assumption** — the belief itself, stated in one sentence
2. **Cite the Implicit evidence** — apply the Column Contract Rule 2 test before
   completing this cell:
   - FAILS the test: `A-01` (row key) | restatement of the assumption in different words |
     `"see rationale"` or any pointer that doesn't deliver text
   - PASSES the test: a short phrase or clause from strategy.md that a reader could trace
     back to a specific location — the text that, if removed, would make the assumption
     invisible to an external reader

An assumption with no strategy text implying it is an inference you imposed on the
document. Leave "Implicit evidence" blank only if systematic scan finds no strategy text,
however indirect, that implies the assumption.

Systematic scan — cover each dimension. Do not skip:
- (a) Implied audience knowledge level
- (b) Namespace priority ordering assumed without justification
- (c) Signal sufficiency threshold — what "enough signals" means here
- (d) Timeline or sequencing feasibility
- (e) Definition of "done" for this topic
- (f) Any additional dimension this specific strategy reveals

Per schema (Assumption Table) — all five columns mandatory. Rule 2 applies; apply the
independence test before completing "Implicit evidence" for each row.

Column rules:
- **"Contradicted by a signal?"**: Write `[pending]` now. Filled in Step 2b.
- **"Why this matters for delta detection"**: Fill now. If a signal contradicts this, which
  skill priorities or namespace ordering would change?
- **"Delta candidate?"**: Rule 1 — select `yes` or `no`. No prose. After Step 3, update
  `yes` rows to `yes — F-NN`.

| Assumption | Implicit evidence [phrase from strategy.md — test: can this be filled without reading strategy.md? if yes, FAILS; FAILS: row ID, restatement, pointer; PASSES: traceable strategy.md text] | Contradicted by a signal? | Why this matters for delta detection | Delta candidate? [yes / no] |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|--------------------------------------|------------------------------|
| [most important — highest likelihood of signal contradiction] | [text from strategy.md that reveals this assumption — specific phrase or clause] | [pending] | [failure mode: which priorities shift?] | yes |
| [second assumption, if any] | [strategy.md phrase, or blank only if no text implies it] | [pending] | | yes / no |

Write at least one row. Null case: "No unstated assumptions found after systematic scan."

---

### Step 2a — Role: Signal Analyst — Read phase

**Adopt this role**: Read every artifact against two reference points: (a) stated fields
from Step 1a, and (b) assumptions from Step 1b. Map each signal to its reference point.

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals found** — reproduce verbatim and stop. Do not omit:

> No signals found — strategy.md remains current. Run signal-gathering skills before
> attempting revision.

Per schema (Signal Inventory) — the following columns are mandatory. Rule 1 applies to
`Consistent with strategy?` — select `Yes`, `No`, or `Partial`; prose not valid:

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? [Yes / No / Partial] | Assumption link (A-NN / "stated field" / "none") |
|----|------|-----------|-------|------|--------------------------|------------------------------------------------|--------------------------------------------------|
| S-01 | | | | | | Yes / No / Partial | |

---

### Step 2b — Role: Assumption Archaeologist — Back-fill phase

**Return to this role**: Adjudicate every assumption from Step 1b against the full signal set.

For each assumption row, replace `[pending]` with a signal-grounded verdict — exactly
one per row. Do not leave any row as `[pending]`:

- **Contradicted — S-NN**: A signal directly challenges this assumption. Cite signal ID.
  Write one sentence on the contradiction.
- **Supported — S-NN**: A signal confirms this assumption. Cite signal ID.
- **No signal coverage**: No signal in the current set speaks to this assumption.

Reproduce the full updated Assumption Table (all 5 columns). Every row must have a verdict.

After completing Step 3, return here and update `yes` entries in "Delta candidate?" —
change `yes` to `yes — F-NN` for rows where a finding was generated.

---

### Step 3 — Role: Delta Identifier

**Adopt this role**: Name the gap between strategy beliefs and signal evidence.

**Stop. Before building the findings table, produce both outputs:**

1. **Anti-pattern label**: Name the anti-pattern you are guarding against. Write the label.
2. **Delta definition**: Delta IS: [gap between belief and signal]. Delta IS NOT:
   [inventory of signal existence].

Per schema (Delta Findings) — the following columns are mandatory. Do not omit any column:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root (A-NN / "stated field") |
|-----------|-----------------|----------------|-----------------|----------------------------------------|
| F-01 | [from Step 1a stated fields or Step 1b assumptions marked Contradicted] | | S-XX | |

After completing findings, return to Step 2b and update all `yes` entries with F-NN IDs.

**Null case** — reproduce verbatim and skip to Step 5:

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

Per schema (Conflict Audit) — the following columns are mandatory:

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

**Null case** — reproduce verbatim. Do not omit:

| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

---

### Step 6 — Role: Proposal Architect

**Adopt this role**: Translate each finding into a typed, defensible proposal. Every
Proposal ID must trace to a Finding ID (via Delta Finding) and from there to an Assumption.

**Stop. Before building the proposals table, write the following statement verbatim:**

> "Proposals schema committed: Proposal ID ★, Type ★ [select: ADD / REMOVE /
> REPRIORITIZE — Rule 1: prose not valid; same values as upfront schema], Change ★,
> Delta Finding ★ (full 'Strategy assumed [X] / Signal revealed [Y]' text from Step 3
> with exact Finding ID), Evidence ★, If unchanged ★ (specific degradation — a row
> that cannot name a specific degradation is a preference, not a decision),
> Reversibility ★ [select: (1) Reversible at same cost / (2) Gets harder / (3) Becomes
> impossible — Rule 1: prose not valid; same values as upfront schema; a row that cannot
> select one has not reasoned about the deferral window and must be revised], Confidence ★.
> All three types present. Empty types use null rows. Traceability: each Proposal ID
> traces to a Finding ID via Delta Finding, and from there to an Assumption."

Per schema (Proposals) — all columns mandatory. Rule 1 applies to Type and Reversibility.

**Column rules:**
- **"If unchanged"**: Name the specific artifact that won't be gathered, the decision that
  becomes harder, or the gap that compounds — not a restatement of the delta finding. A
  row that cannot name a specific degradation is a preference, not a decision.
- **"Reversibility"**: Select exactly one of the three values from the pre-reading contract.
  Prose ("it will be harder later") is not a valid value. A row that cannot commit to (1),
  (2), or (3) has not reasoned about the deferral window.

| Proposal ID | Type [ADD / REMOVE / REPRIORITIZE] | Change | Delta Finding | Evidence [file(s)] | If unchanged [specific degradation — not a delta finding synonym] | Reversibility [(1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible] | Confidence |
|------------|-------------------------------------|--------|--------------|-------------------|--------------------------------------------------------------------|----------------------------------------------------------------------------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [which artifact won't be gathered / which gap compounds] | (2) Gets harder | High |

Null rows (reproduce verbatim for each empty type):

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 7 — Role: Diff Author

**Adopt this role**: Show the exact before/after for every confirmed proposal. Every
Proposal ID is the entry point into the full traceability chain: Proposal ID → Delta
Finding → Assumption.

**Stop. Before building the diff table, write the following statement verbatim:**

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★
> (inline per row as [file.md — ≤10 word finding] — no separate evidence section),
> Proposal ★ (Proposal ID from Step 6 — entry point into Proposal → Delta Finding →
> Assumption chain). No column omitted."

Per schema (Diff) — all columns mandatory:

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

## Criterion Coverage Matrix (v9 rubric, C-01–C-35)

C-01 through C-33: mechanisms carried forward from R9. New R10 discriminators in bold.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Read strategy | Step 1a | Step 1 | Step 1a | Step 1a | Step 1a |
| C-02 Read signals | Step 2 | Step 2 | Step 2a | Step 2a | Step 2a |
| C-03 Delta not inventory | Step 3 stop+name | Step 3 stop+name+contrast | Step 3 stop+name+contrast | Step 3 stop+name+contrast | Step 3 stop+name+contrast |
| C-04 Typed proposals | Step 6 table | Step 6 table | Step 6 table | Step 6 table | Step 6 table |
| C-05 Confirm gate | Step 8 YES | Step 8 YES | Step 8 YES | Step 8 YES | Step 8 YES |
| C-06 Evidence per change | Step 6 Evidence col | Step 6 Evidence col | Step 6 Evidence col | Step 6 Evidence col | Step 6 Evidence col |
| C-07 Before/after diff | Step 7 | Step 7 | Step 7 | Step 7 | Step 7 |
| C-08 All three types | Step 6 null rows | Step 6 null rows | Step 6 null rows | Step 6 null rows | Step 6 null rows |
| C-09 Namespace gaps | Step 4 (9 by name) | Step 4 (9 by name) | Step 4 (9 by name) | Step 4 (9 by name) | Step 4 (9 by name) |
| C-10 Conflicting signals | Step 5 | Step 5 | Step 5 | Step 5 | Step 5 |
| C-11 Typed confirmation verb | Step 8 YES | Step 8 YES | Step 8 YES | Step 8 YES | Step 8 YES |
| C-12 Explicit no-change rows | Step 6 null rows verbatim | Step 6 null rows verbatim | Step 6 null rows verbatim | Step 6 null rows verbatim | Step 6 null rows verbatim |
| C-13 Inline evidence in diff | Step 7 Evidence col | Step 7 (committed at checkpoint) | Step 7 (committed at checkpoint) | Step 7 (committed at checkpoint) | Step 7 (committed at checkpoint) |
| C-14 Anti-inventory warning | Step 3 stop+name | Step 3 stop+name+contrast | Step 3 stop+name+contrast | Step 3 stop+name+contrast | Step 3 stop+name+contrast |
| C-15 All 9 namespaces named | Step 4 table | Step 4 table | Step 4 table | Step 4 table | Step 4 table |
| C-16 Two-level traceability | Step 6 Delta Finding + Evidence | Step 6 Delta Finding + Evidence (committed) | Step 6 Delta Finding + Evidence + chain obligation | Step 6 Delta Finding + Evidence + chain obligation | Step 6 Delta Finding + Evidence + chain obligation |
| C-17 Explicit no-conflicts | Step 5 null row verbatim | Step 5 null row verbatim | Step 5 null row verbatim | Step 5 null row verbatim | Step 5 null row verbatim |
| C-18 Structured delta format | Step 3 table | Step 3 table | Step 3 table | Step 3 table | Step 3 table |
| C-19 Diff Proposal ID col | Step 7 Proposal col (committed) | Step 7 Proposal col (committed) | Step 7 Proposal col (committed) | Step 7 Proposal col (committed) | Step 7 Proposal col (committed) |
| C-20 Delta Finding col | Step 6 mandatory + null rows (committed) | Step 6 mandatory + null rows (committed) | Step 6 mandatory + null rows (committed) | Step 6 mandatory + null rows (committed) | Step 6 mandatory + null rows (committed) |
| C-21 Column-completeness declaration | PASS: every table | PASS: upfront ★ schema + per-table | PASS: upfront ★ schema + per-table | PASS: upfront ★ schema + per-table | PASS: upfront ★ schema + per-table |
| C-22 Active anti-pattern checkpoint | PASS: Step 3 stop+name | PASS: Step 3 stop+name+contrast | PASS: Steps 3+6+7 checkpoints | PASS: Steps 3+6+7 checkpoints | PASS: Steps 3+6+7 checkpoints |
| C-23 Pre-reproduced null templates | PASS: all null outcomes | PASS: all null outcomes | PASS: all null outcomes | PASS: all null outcomes | PASS: all null outcomes |
| C-24 Unstated assumption extraction | PASS: Step 1b scan (a-e) | PASS: Step 1b scan + Implicit evidence col | PASS: Archaeologist + scan (a-e) | PASS: Archaeologist + scan (a-e) | PASS: Archaeologist + scan (a-f) |
| C-25 Inertia cost column | PASS: "If unchanged" col | PASS: "If unchanged" + adjacent rule | PASS: "If unchanged" col + Rule 1 context | PASS: "If unchanged" + adjacent rule + committed | PASS: "If unchanged" + adjacent rule + committed |
| C-26 Schema-first priming | PASS: upfront ★ schema | PASS: upfront ★ schema | PASS: upfront ★ schema | PASS: upfront ★ schema | PASS: upfront ★ schema |
| C-27 Cascade checkpoints | PASS: Steps 3+6+7 | PASS: Steps 3+6+7 | PASS: Steps 3+6+7 | PASS: Steps 3+6+7 | PASS: Steps 3+6+7 |
| C-28 Named role + scan dimensions | PARTIAL: scan (a-e) in Step 1b, no named role | PARTIAL: no named role, no scan dimensions | PASS: Archaeologist + scan (a-e) | PASS: Archaeologist + scan (a-e) | PASS: Archaeologist + scan (a-f) |
| C-29 Back-fill column | PASS: "Contradicted?" + back-fill instruction | PASS: "Contradicted?" in upfront + back-fill | PASS: named Step 2b lifecycle + verdict-per-row | PASS: upfront schema + named Step 2b back-fill | PASS: upfront schema + named Step 2b + verdict-per-row |
| C-30 Forward-reasoning columns | PASS: "Why this matters" + "Delta candidate?" | PASS: "Why this matters" + "Delta candidate?" in upfront + Step 1 | PASS: "Why this matters" + "Delta candidate?" in upfront + Step 1b + updated post-Step 3 | PASS: same + updated post-Step 3 | PASS: same + updated post-Step 3 |
| C-31 Decision-gate framing | FAIL: no adjacent disqualification rule | PASS: "a row that cannot name a specific degradation is a preference, not a decision" | PASS: adjacent disqualification rule in Step 6 + commitment | PASS: adjacent rule + committed | PASS: adjacent rule + committed |
| C-32 Reversibility taxonomy | PASS: three-value enum in upfront schema + Step 6 column header + "prose not valid" | PASS: three-value enum in upfront schema + Step 6 column header | PASS: three-value enum in upfront schema + Step 6 column header + commitment reproduced | PASS: three-value enum in upfront schema + Step 6 column header + commitment reproduced | PASS: three-value enum in upfront schema + Step 6 commitment reproduced with disqualification |
| C-33 Assumption table in upfront schema | FAIL: Assumption Table in upfront schema but Implicit evidence column absent | PASS: Implicit evidence column in upfront schema + in Step 1 extraction | PASS: Implicit evidence column in upfront schema (with Rule 2 test) + in Step 1b | PASS: Implicit evidence column in upfront schema (with independence rule) + in Step 1b | PASS: Implicit evidence column in upfront schema (with fail/pass examples + Rule 2) + in Step 1b |
| **C-34 Universal closed-enum at both sites** | **PASS: Delta candidate? [yes/no], Consistent with strategy? [Yes/No/Partial], Type [ADD/REMOVE/REPRIORITIZE], Reversibility [(1)/(2)/(3)] all carry closed enums in upfront schema; Step 6 commitment reproduces all four with prose-prohibition** | **FAIL: only Reversibility carries closed enum; Consistent with strategy? and Delta candidate? have no enum annotation; commitment checkpoint names them without value lists** | **PASS: COLUMN CONTRACT Rule 1 declares closed-enum obligation universally; upfront schema carries closed enums for all four columns; commitment checkpoints reproduce them** | **PASS: all four enumerated columns carry closed enums in upfront schema; Step 6 commitment reproduces Type and Reversibility with prose-prohibition** | **PASS: COLUMN CONTRACT Rule 1 + all four enumerated columns in upfront schema + Step 6 commitment names all four with valid-value selectors + prose-prohibition** |
| **C-35 Column independence in assumption table** | **FAIL: no independence rule; Implicit evidence column named in upfront schema but no disqualification condition; row key aliasing not prevented** | **PASS: independence rule with three fail examples and one pass example at upfront schema annotation and Step 1 extraction; anti-pattern named ("row key aliasing" pattern)** | **PASS: COLUMN CONTRACT Rule 2 with decision-question independence test; "Implicit evidence" column annotation carries the test + fail/pass distinction** | **PASS: upfront schema Implicit evidence annotation carries independence rule with fail/pass examples; Step 1b extraction names three fail patterns and one pass pattern explicitly** | **PASS: COLUMN CONTRACT Rule 2 + upfront schema fail/pass examples + Step 1b archaeology obligation names three fail cases + one pass case with traceability test** |
