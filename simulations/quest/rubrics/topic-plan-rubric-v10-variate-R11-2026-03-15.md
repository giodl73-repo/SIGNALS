# topic-plan — Round 11 Variations (v10 rubric)

**Skill**: `topic:plan`
**Rubric**: v10 (C-01–C-37, 235 pts total)
**Date**: 2026-03-15

---

## Round 11 Design Notes

R10 V-03 achieved the first perfect 27/27 aspirational pass (225/225 against v9). The two
new v10 criteria promote what V-03 introduced:

- **C-36** — Named pre-schema rule block (COLUMN CONTRACT) with numbered rules and
  rule-reference linkage at commitment checkpoints. V-03 satisfies this with Rule 1 + Rule 2.
- **C-37** — Operationalized independence test procedure with explicit pass/fail examples
  embedded in the column definition. V-03 satisfies this with the decision-question
  ("Can I fill this without reading the source document?") and fail examples inline.

**What V-03 from R10 achieved and where gaps may remain:**

| Criterion | V-03 R10 mechanism | Possible R11 gap |
|-----------|-------------------|------------------|
| C-36 | COLUMN CONTRACT with Rule 1/Rule 2, numbered, cited at checkpoints as "Rule 1"/"Rule 2" | Only two rules — Rule 3 (evidence provenance) and Rule 4 (null completeness) are undeclared; their constraints appear per-step rather than in the pre-schema contract |
| C-37 | Decision-question embedded in column header + fail examples in step annotation | Pass examples are only implicit in the column description ("phrase from strategy.md"); explicit symmetric PASS/FAIL exhibits are absent from the column header definition |

**Three single-axis dimensions explored in R11:**

1. **Role sequence**: Add a Step 0 "Hypothesis Generator" — before reading any file, commit
   to predictions about assumptions, signal directions, and expected deltas. Delta Findings
   table gains a "Hypothesis match" column (confirmed / surprise). Surprise findings are
   flagged as highest-value discoveries.

2. **Inertia framing**: Foreground the status-quo competitor. Open with a "Status-quo
   defender framing" block. Rename "If unchanged" as "Status quo retains" and present it
   as a challenger test: a proposal that cannot name what the status quo retains is not
   a competitor. Add a pre-proposal "Inertia cost audit" table before Step 6.

3. **Output format — symmetric pass/fail exhibits**: For EVERY operationalized test in
   the CONTRACT and in each column header, include explicit PASS and FAIL examples
   as labeled exhibit rows (not just implied by the description). Applied to: Implicit
   evidence column (Rule 2), Type column (Rule 1), Reversibility column (Rule 1), and
   the anti-pattern checkpoint at the delta step.

**Variation design:**

| Variation | Axis | Type | Primary R11 target |
|-----------|------|------|--------------------|
| V-01 | Role sequence — pre-read hypothesis commitment | Single | Delta quality via pre-commitment |
| V-02 | Inertia framing — status-quo competitor prominence | Single | C-25, C-31, C-32 load-bearing quality |
| V-03 | Output format — symmetric PASS/FAIL exhibits throughout | Single | C-37 completeness |
| V-04 | Role sequence + Output format (V-01 + V-03 combined) | Combination | Delta quality + C-37 completeness |
| V-05 | Full ceiling — 4-rule CONTRACT + V-01 + V-02 + V-03 | Combination | All C-36/C-37 mechanisms at maximum specificity |

---

## V-01 — Pre-Read Hypothesis Commitment

**Axis**: Role sequence — a new Step 0 ("Hypothesis Generator") runs before any file
is read. The model commits to predictions: what assumptions the strategy probably makes,
what direction signals probably take, what delta likely emerges. These hypotheses are
scored against Step 4 findings. A finding that matches a hypothesis is "confirmed"; a
finding with no matching hypothesis is a "surprise" — flagged as highest-value discovery.

**Hypothesis**: The current structure reads → extracts → back-fills. The delta step
can confabulate alignment between assumptions and signals after the fact because the
model holds both simultaneously. A pre-read hypothesis commitment makes the delta
step falsifiable: if Step 4 finding F-01 has no matching Step 0 hypothesis, the model
cannot claim it "expected" the gap. Surprise findings reveal the model's actual blindspots.
The hypothesis table also activates the Assumption Archaeologist before the document
creates confirmation bias — the model generates what the strategy "probably" assumes
before reading what it actually says.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it
was written. The assumption table is a two-phase artifact: extract at Step 2 (before
signal reading), back-fill at Step 3b (after). Present proposals, wait for confirmation,
then write. Do not auto-apply changes.

---

### COLUMN CONTRACT (binding before reading any file)

Two rules govern every table you produce. Read before the Output Schema.

**Rule 1 — Enumerated columns**: Any column using a closed value set must declare those
values at every point where the column is named. Select from the declared set only; prose
is not a valid value. Applies to: `Delta candidate?` [yes / no / yes — F-NN],
`Consistent with strategy?` [Yes / No / Partial], `Type` [ADD / REMOVE / REPRIORITIZE],
`Reversibility` [(1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible].

**Rule 2 — Column independence**: Before filling any cell, apply this test: *"Can I fill
this cell without reading the source document?"* If yes, the cell is a structural alias
and is treated as empty regardless of content. Applies especially to `Implicit evidence` —
the cell must contain text traceable to a specific location in strategy.md.

Example: A cell containing "A-01" (the row key), "signals gather evidence" (restatement),
or "see rationale" (pointer) cannot pass the Rule 2 test and is treated as absent.

---

### Output Schema (read before proceeding to Step 0)

Every table you produce must conform to this schema. Columns marked ★ are mandatory —
do not omit any ★ column. Both Contract Rules apply to every ★ column.

**Hypothesis Table** (Step 0 only — 4 columns mandatory)
| ★ Hypothesis ID | ★ Predicted assumption | ★ Expected signal direction | ★ Expected delta (if signals contradict) |

**Assumption Table** (5 columns — all independently populated per Rule 2)
| ★ Assumption | ★ Implicit evidence [text from strategy.md — Rule 2 applies; test: "Can I fill this without reading strategy.md?" — if yes, this fails] | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? [Rule 1: yes / no; update to yes — F-NN after Step 4] |

**Signal Inventory**
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? [Rule 1: Yes / No / Partial] | ★ Assumption link (A-NN / "stated field" / "none") |

**Delta Findings**
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) | ★ Assumption root (A-NN / "stated field") | ★ Hypothesis match (H-N confirmed / Surprise — not hypothesized) |

**Namespace Audit**
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |

**Conflict Audit**
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals** (Rule 1 applies to Type and Reversibility)
| ★ Proposal ID | ★ Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | ★ Change | ★ Delta Finding | ★ Evidence | ★ If unchanged | ★ Reversibility [Rule 1: (1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible] | ★ Confidence |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

Do not omit any ★ column.

---

### Step 0 — Role: Hypothesis Generator

**Adopt this role**: Before reading any file, commit to predictions about what you will
find. What does this strategy probably assume? What do signals probably reveal? What is
the most likely delta?

These predictions are scored in Step 4. A delta finding that matches a Step 0 hypothesis
is confirmed — expected. A finding with no matching hypothesis is a **surprise** — the
highest-value discovery, revealing a genuine blindspot.

**The following columns are mandatory. Do not omit any column.**

| Hypothesis ID | Predicted assumption | Expected signal direction | Expected delta (if signals contradict) |
|--------------|---------------------|---------------------------|----------------------------------------|
| H-01 | [most likely unstated assumption given the topic + skill phase] | [signals probably confirm / probably contradict] | [predicted delta if contradicted] |
| H-02 | [second prediction, if any] | | |

Write at least one hypothesis. **Do not read any files before completing this step.**

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

### Step 2 — Role: Assumption Archaeologist — Extract phase

**Adopt this role**: Find what strategy.md took for granted without writing. These are
the implied preconditions, the unstated beliefs, the worldview the author would defend
if challenged but never put in the document.

Systematic scan — cover each dimension:
- (a) Implied audience knowledge level
- (b) Namespace priority ordering assumed without justification
- (c) Signal sufficiency threshold — what "enough signals" means here
- (d) Timeline or sequencing feasibility
- (e) Definition of "done" for this topic

Per schema (Assumption Table) — all five columns are mandatory. Apply Rule 2 to
`Implicit evidence` before completing each row.

Column rules:
- **"Contradicted by a signal?"**: Write `[pending]` now. Fill after Step 3a.
- **"Why this matters"**: Fill now. Name the failure mode if this assumption is wrong.
- **"Delta candidate?"**: Rule 1 — select `yes` or `no`. After Step 4, update to `yes — F-NN`.

| Assumption | Implicit evidence [text from strategy.md — Rule 2 test: "Can I fill this without reading strategy.md?"; fail if row key, restatement, or pointer] | Contradicted by a signal? | Why this matters for delta detection | Delta candidate? [yes / no] |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|--------------------------------------|------------------------------|
| [most important — highest likelihood of signal contradiction] | [phrase from strategy.md — fails test if it is the assumption ID, a restatement, or a pointer] | [pending] | [failure mode if wrong] | yes |

Write at least one row. Null case:

| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |

---

### Step 3a — Role: Signal Analyst — Read phase

**Adopt this role**: Read every artifact against two reference points: (a) stated fields
from Step 1, and (b) assumptions from Step 2.

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals found** — reproduce the following verbatim and stop. Do not omit:

> No signals found — strategy.md does not need revision at this time.

Per schema (Signal Inventory) — the following columns are mandatory. Do not omit any column.
Rule 1 applies to `Consistent with strategy?` — select Yes / No / Partial; prose not valid:

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? [Yes / No / Partial] | Assumption link (A-NN / "stated field" / "none") |
|----|------|-----------|-------|------|--------------------------|------------------------------------------------|--------------------------------------------------|
| S-01 | | | | | | | |

---

### Step 3b — Role: Assumption Archaeologist — Back-fill phase

**Return to this role**: Adjudicate every assumption against the full signal set.

For each A-NN row, replace `[pending]` with exactly one verdict:
- **Contradicted — S-NN**: Signal challenges this assumption. Cite ID, one sentence.
- **Supported — S-NN**: Signal confirms this assumption. Cite ID.
- **No signal coverage**: No signal speaks to this assumption.

Reproduce the full updated Assumption Table (all 5 columns). Every row must have a verdict.

After completing Step 4, return here and update `yes` rows in "Delta candidate?" to `yes — F-NN`.

---

### Step 4 — Role: Delta Identifier

**Adopt this role**: Name the gap between strategy beliefs and signal evidence.

Stop. Before building the findings table, write the name of the anti-pattern you are
guarding against at this step.

For each finding, check your Step 0 hypotheses:
- If a Step 0 hypothesis matches, note **"H-N confirmed"**
- If no hypothesis matches, note **"Surprise — not hypothesized"** (flag as highest-value)

Per schema (Delta Findings) — the following columns are mandatory. Do not omit any column:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root (A-NN / "stated field") | Hypothesis match |
|-----------|-----------------|----------------|-----------------|----------------------------------------|-----------------|
| F-01 | [from Step 1 or Step 2] | | S-XX | | H-N confirmed / Surprise — not hypothesized |

After building findings, return to Step 3b and update `yes` rows to `yes — F-NN`.

**Null case — all signals confirm** — reproduce verbatim and skip to Step 6:

| F-00 | Strategy confirmed | No gaps detected | All signals | N/A | All confirmed |

---

### Step 5 — Role: Coverage Auditor

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
> revealed [Y]' text from Step 4 with exact ID), Evidence ★, If unchanged ★ (specific
> degradation — a row that cannot name a specific degradation is a preference, not a
> decision), Reversibility ★ [Rule 1: (1) Reversible at same cost / (2) Gets harder /
> (3) Becomes impossible; prose not valid], Confidence ★. All three types present.
> Empty types use null rows."

**The following columns are mandatory. Do not omit any column.**

| Proposal ID | Type [ADD / REMOVE / REPRIORITIZE — Rule 1] | Change | Delta Finding | Evidence [file(s)] | If unchanged [specific degradation — a row without one is a preference, not a decision] | Reversibility [(1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible — Rule 1] | Confidence |
|------------|---------------------------------------------|--------|--------------|-------------------|---------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [specific degradation named] | (2) Gets harder | High |

Null rows — reproduce verbatim for each empty type:

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 8 — Role: Diff Author

**Stop. Before building the diff table, write the following statement verbatim:**

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★
> (inline per row as [file.md — ≤10 word finding] — no separate evidence section),
> Proposal ★ (Proposal ID from Step 7). No column omitted. Rule 1 applies to all
> enumerated columns."

**The following columns are mandatory. Do not omit any column.**

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

## V-02 — Status-Quo Competitor Framing

**Axis**: Inertia framing — the current strategy is the status quo, and every proposal
is a challenger. The prompt opens with this framing explicitly. The "If unchanged" column
is presented as the "Status quo case" — what the current strategy retains if this proposal
loses. A pre-proposal Inertia Cost Audit table forces the model to evaluate all signals
against the current strategy before generating proposals. The reversibility classification
is prominently introduced at the framing level (not only at the commitment checkpoint).

**Hypothesis**: Burying the status-quo cost in a column header creates a formatting
compliance path — the model names a degradation because the column requires it, not
because it has argued the full status-quo position. Foregrounding the status-quo framing
at the start of proposals makes every proposal a written argument for why the challenger
wins. A model that cannot articulate "what the status quo retains" and "how fast that
retention erodes" has not made a proposal — it has made an observation. The inertia cost
audit table surfaces this distinction before the proposal table is built.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it
was written. The current strategy is the status quo. Each proposed change is a challenger:
it must defeat the status quo by naming what degrades if the current approach is retained
and how fast that window closes. Present proposals, wait for confirmation, then write.
Do not auto-apply changes.

---

### COLUMN CONTRACT (binding before reading any file)

Two rules govern every table you produce. Read before the Output Schema.

**Rule 1 — Enumerated columns**: Any column using a closed value set must declare those
values at every point where the column is named. Select from the declared set only; prose
is not a valid value. Applies to: `Delta candidate?` [yes / no / yes — F-NN],
`Consistent with strategy?` [Yes / No / Partial], `Type` [ADD / REMOVE / REPRIORITIZE],
`Reversibility` [(1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible].

**Rule 2 — Column independence**: Before filling any cell, apply this test: *"Can I fill
this cell without reading the source document?"* If yes, the cell is a structural alias
and is treated as empty. Applies especially to `Implicit evidence` — the cell must contain
text traceable to a specific location in strategy.md.

Example: A cell containing "A-01" (the row key), "signals gather evidence" (restatement),
or "see rationale" (pointer) cannot pass the Rule 2 test and is treated as absent.

---

### Output Schema (read before proceeding to Step 1)

Every table you produce must conform to this schema. Columns marked ★ are mandatory —
do not omit any ★ column. Both Contract Rules apply to every ★ column.

**Assumption Table** (5 columns — all independently populated per Rule 2)
| ★ Assumption | ★ Implicit evidence [text from strategy.md — Rule 2 applies; test: "Can I fill this without reading strategy.md?" — if yes, this fails] | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? [Rule 1: yes / no; update to yes — F-NN after Step 4] |

**Signal Inventory**
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? [Rule 1: Yes / No / Partial] | ★ Assumption link (A-NN / "stated field" / "none") |

**Delta Findings**
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) | ★ Assumption root (A-NN / "stated field") |

**Namespace Audit**
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |

**Conflict Audit**
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Inertia Cost Audit** (pre-proposal — all signals ranked by status-quo cost)
| ★ Signal ID | ★ Status quo position | ★ Cost if status quo retained | ★ Reversibility window [Rule 1: (1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible] |

**Proposals** (Rule 1 applies to Type and Reversibility)
| ★ Proposal ID | ★ Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | ★ Change | ★ Delta Finding | ★ Evidence | ★ Status quo retains [what the current strategy keeps if this proposal is deferred — a proposal that cannot answer this is not a competitor, it is a preference] | ★ Reversibility [Rule 1: (1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible] | ★ Confidence |

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

### Step 2 — Role: Assumption Archaeologist — Extract phase

**Adopt this role**: Find what strategy.md took for granted without writing. These are
the implied preconditions, the unstated beliefs, the worldview the author would defend
if challenged but never put in the document.

Systematic scan — cover each dimension:
- (a) Implied audience knowledge level
- (b) Namespace priority ordering assumed without justification
- (c) Signal sufficiency threshold — what "enough signals" means here
- (d) Timeline or sequencing feasibility
- (e) Definition of "done" for this topic

Per schema (Assumption Table) — all five columns mandatory. Apply Rule 2 to `Implicit evidence`.

Column rules:
- **"Contradicted by a signal?"**: Write `[pending]` now. Fill after Step 3a.
- **"Why this matters"**: Fill now. Name the failure mode if this assumption is wrong.
- **"Delta candidate?"**: Rule 1 — select `yes` or `no`. After Step 4, update to `yes — F-NN`.

| Assumption | Implicit evidence [text from strategy.md — Rule 2 test: "Can I fill this without reading strategy.md?"] | Contradicted by a signal? | Why this matters for delta detection | Delta candidate? [yes / no] |
|-----------|----------------------------------------------------------------------------------------------------------|--------------------------|--------------------------------------|------------------------------|
| [most important] | [phrase from strategy.md — fails if row key, restatement, pointer] | [pending] | [failure mode if wrong] | yes |

Write at least one row. Null case:

| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |

---

### Step 3a — Role: Signal Analyst — Read phase

**Adopt this role**: Read every artifact against two reference points: (a) stated fields
from Step 1, and (b) assumptions from Step 2.

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals found** — reproduce the following verbatim and stop. Do not omit:

> No signals found — strategy.md does not need revision at this time.

Per schema (Signal Inventory) — the following columns are mandatory. Do not omit any column.
Rule 1 applies to `Consistent with strategy?` — select Yes / No / Partial; prose not valid:

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? [Yes / No / Partial] | Assumption link (A-NN / "stated field" / "none") |
|----|------|-----------|-------|------|--------------------------|------------------------------------------------|--------------------------------------------------|
| S-01 | | | | | | | |

---

### Step 3b — Role: Assumption Archaeologist — Back-fill phase

For each A-NN row, replace `[pending]` with exactly one verdict:
- **Contradicted — S-NN**: Signal challenges this assumption. Cite ID, one sentence.
- **Supported — S-NN**: Signal confirms this assumption. Cite ID.
- **No signal coverage**: No signal speaks to this assumption.

Reproduce the full updated Assumption Table. After Step 4, update `yes` rows to `yes — F-NN`.

---

### Step 4 — Role: Delta Identifier

Stop. Before building the findings table, write the name of the anti-pattern you are
guarding against at this step.

Per schema (Delta Findings) — the following columns are mandatory. Do not omit any column:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root (A-NN / "stated field") |
|-----------|-----------------|----------------|-----------------|----------------------------------------|
| F-01 | [from Step 1 or Step 2] | | S-XX | |

After building findings, return to Step 3b and update `yes` rows to `yes — F-NN`.

**Null case — all signals confirm** — reproduce verbatim and skip to Step 6:

| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |

---

### Step 5 — Namespace Coverage Audit

Assess all 9 namespaces by name. Stage-relative = appropriate for current stage.

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

### Step 6 — Conflict Audit

**The following columns are mandatory. Do not omit any column.**

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

**Null case — no conflicts** — reproduce verbatim. Do not omit this table:

| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

---

### Step 7a — Inertia Cost Audit

**Before building proposals, audit every signal against the current strategy.** The
current strategy is the status quo. For each signal, name what the status quo position
is and what it costs to retain it.

Per schema (Inertia Cost Audit) — the following columns are mandatory. Do not omit any column.
Rule 1 applies to `Reversibility window` — select one; prose not valid:

| Signal ID | Status quo position [what the current strategy does re this signal] | Cost if status quo retained [specific degradation named] | Reversibility window [(1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible] |
|-----------|---------------------------------------------------------------------|----------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| S-01 | | | |

**Null case — all signals confirm status quo** — reproduce verbatim and proceed to Step 7b:

| SC-00 | All signals confirm current strategy | No degradation identified | (1) Reversible at same cost |

---

### Step 7b — Role: Proposal Architect

**Stop. Before building the proposals table, write the following statement verbatim:**

> "Proposals schema committed: Proposal ID ★, Type ★ [Rule 1: ADD / REMOVE / REPRIORITIZE;
> prose not valid], Change ★, Delta Finding ★ (full 'Strategy assumed [X] / Signal
> revealed [Y]' text from Step 4 with exact ID), Evidence ★, Status quo retains ★
> (what the current strategy keeps if this proposal is deferred — a proposal that cannot
> answer this is not a competitor, it is a preference), Reversibility ★ [Rule 1:
> (1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible; prose not valid],
> Confidence ★. All three types present. Empty types use null rows."

**The following columns are mandatory. Do not omit any column.**

| Proposal ID | Type [ADD / REMOVE / REPRIORITIZE — Rule 1] | Change | Delta Finding | Evidence [file(s)] | Status quo retains [specific — a proposal that cannot name this is a preference, not a decision] | Reversibility [(1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible — Rule 1] | Confidence |
|------------|---------------------------------------------|--------|--------------|-------------------|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [what the current approach retains if deferred — and why that retention eventually fails] | (2) Gets harder | High |

Null rows — reproduce verbatim for each empty type:

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | Status quo retains: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | Status quo retains: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | Status quo retains: N/A | N/A | — |

---

### Step 8 — Before/after diff

**Stop. Before building the diff table, write the following statement verbatim:**

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★
> (inline per row as [file.md — ≤10 word finding] — no separate evidence section),
> Proposal ★ (Proposal ID from Step 7b). No column omitted."

**The following columns are mandatory. Do not omit any column.**

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

## V-03 — Symmetric PASS/FAIL Exhibits in All Column Definitions

**Axis**: Output format — every operationalized test in the COLUMN CONTRACT and in
each column definition carries a symmetric exhibit with explicit PASS and FAIL examples
as labeled rows (not just descriptive prose). This applies to: `Implicit evidence`
(Rule 2 decision-question), `Type` and `Reversibility` (Rule 1 enum), and the
anti-pattern checkpoint at the delta step.

**Hypothesis**: R10 V-03 embedded the decision-question in the column header and named
fail examples in the step annotation. C-37 requires "explicit pass/fail examples
demonstrating the test's discriminating power embedded in the column definition." V-03
from R10 provides fail examples but the pass examples are only implicit ("phrase from
strategy.md"). Symmetric exhibits make the discrimination test bidirectional: the model
confronts both what correct and incorrect cells look like before filling. For Rule 1
columns (Type, Reversibility), fail examples show what prose looks like; pass examples
show what a valid selection looks like. The anti-pattern checkpoint gains a symmetric
exhibit: PASS shows what a delta finding looks like, FAIL shows what an inventory
item looks like. Single-axis: exhibit symmetry is the only change; no pre-hypothesis
step, no inertia framing restructure.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it
was written. The assumption table is a two-phase artifact: extract at Step 2, back-fill
at Step 3b. Present proposals, wait for confirmation, then write. Do not auto-apply changes.

---

### COLUMN CONTRACT (binding before reading any file)

Two rules govern every table you produce. Read before the Output Schema.

**Rule 1 — Enumerated columns**: Any column using a closed value set must declare those
values at every point where the column is named. Select from the declared set only; prose
is not a valid value.

Rule 1 PASS examples (correct cell content):
- `Type`: `ADD` | `REMOVE` | `REPRIORITIZE`
- `Reversibility`: `(1) Reversible at same cost` | `(2) Gets harder` | `(3) Becomes impossible`
- `Delta candidate?`: `yes` | `no` | `yes — F-01`
- `Consistent with strategy?`: `Yes` | `No` | `Partial`

Rule 1 FAIL examples (invalid cell content — treated as absent):
- `Type`: "I suggest adding a new skill" (prose) | "addition" (paraphrase) | "add/remove" (multi-value)
- `Reversibility`: "it will be harder later" (prose) | "maybe irreversible" (hedged prose)
- `Delta candidate?`: "probably yes" (hedged) | "yes, depending on signals" (conditional prose)

**Rule 2 — Column independence**: Before filling any cell, apply this test: *"Can I fill
this cell without reading the source document?"* If yes, the cell is a structural alias
and is treated as empty.

Rule 2 PASS examples for `Implicit evidence` (content that requires reading strategy.md):
- `"teams run scout before draft"` — traced to rationale block
- `"signal count threshold never defined"` — paraphrase of absent text
- `"the phrase 'gather evidence first'"` — location + text

Rule 2 FAIL examples for `Implicit evidence` (treated as absent):
- `A-01` — the row key
- `"signals gather evidence"` — restatement of assumption in other words
- `"see rationale section"` — pointer without content
- `"strategy implies sequencing"` — generic inference not traceable to a phrase

---

### Output Schema (read before proceeding to Step 1)

Every table you produce must conform to this schema. Columns marked ★ are mandatory —
do not omit any ★ column. Both Contract Rules apply to every ★ column.

**Assumption Table** (5 columns — all independently populated per Rule 2)
| ★ Assumption | ★ Implicit evidence [Rule 2 test: "Can I fill this without reading strategy.md?" — PASS: specific phrase/paraphrase from strategy.md only | FAIL: row key / restatement / pointer] | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? [Rule 1 — PASS: yes / no / yes — F-NN | FAIL: prose] |

**Signal Inventory**
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? [Rule 1 — PASS: Yes / No / Partial | FAIL: prose or multi-value] | ★ Assumption link (A-NN / "stated field" / "none") |

**Delta Findings**
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) | ★ Assumption root (A-NN / "stated field") |

**Namespace Audit**
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |

**Conflict Audit**
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals** (Rule 1 applies to Type and Reversibility)
| ★ Proposal ID | ★ Type [Rule 1 — PASS: ADD / REMOVE / REPRIORITIZE | FAIL: prose or multi-value] | ★ Change | ★ Delta Finding | ★ Evidence | ★ If unchanged | ★ Reversibility [Rule 1 — PASS: (1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible | FAIL: prose] | ★ Confidence |

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

### Step 2 — Role: Assumption Archaeologist — Extract phase

**Adopt this role**: Find what strategy.md took for granted without writing.

Systematic scan — cover each dimension:
- (a) Implied audience knowledge level
- (b) Namespace priority ordering assumed without justification
- (c) Signal sufficiency threshold — what "enough signals" means here
- (d) Timeline or sequencing feasibility
- (e) Definition of "done" for this topic

Per schema (Assumption Table) — all five columns mandatory. Apply Rule 2 to `Implicit evidence`
using the PASS/FAIL exhibit in the COLUMN CONTRACT before completing each cell.

Column rules:
- **"Contradicted by a signal?"**: Write `[pending]` now. Fill after Step 3a.
- **"Why this matters"**: Fill now. Name the failure mode if this assumption is wrong.
- **"Delta candidate?"**: Rule 1 — select `yes` or `no`. After Step 4, update to `yes — F-NN`.

Example row showing PASS cell for `Implicit evidence` (required format):

| Assumption | Implicit evidence | Contradicted? | Why it matters | Delta candidate? |
|-----------|-------------------|---------------|----------------|-----------------|
| "scout before draft is assumed" | "teams run scout before draft" — from rationale block | [pending] | If wrong: draft could precede scout, invalidating sequencing skills | yes |

Example row showing FAIL cell for `Implicit evidence` (rejected format — treated as absent):

| Assumption | Implicit evidence | ... |
|-----------|-------------------|-----|
| "scout before draft is assumed" | A-01 | ... | ← FAIL: row key |
| "scout before draft is assumed" | "sequencing is assumed" | ... | ← FAIL: restatement |

**The following columns are mandatory. Do not omit any column.**

| Assumption | Implicit evidence [PASS: phrase from strategy.md only — FAIL: row key / restatement / pointer] | Contradicted by a signal? | Why this matters for delta detection | Delta candidate? [PASS: yes / no — FAIL: prose] |
|-----------|------------------------------------------------------------------------------------------------|--------------------------|--------------------------------------|------------------------------------------------|
| [most important] | [phrase from strategy.md that reveals this assumption — test: "Can I fill this without reading strategy.md?"] | [pending] | [failure mode if wrong] | yes |

Write at least one row. Null case:

| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |

---

### Step 3a — Role: Signal Analyst — Read phase

**Adopt this role**: Read every artifact against two reference points: (a) stated fields
from Step 1, and (b) assumptions from Step 2.

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals found** — reproduce the following verbatim and stop. Do not omit:

> No signals found — strategy.md does not need revision at this time.

Per schema (Signal Inventory) — the following columns are mandatory. Do not omit any column.
Rule 1 applies to `Consistent with strategy?` — PASS: `Yes` / `No` / `Partial`. FAIL: prose:

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? [Yes / No / Partial] | Assumption link (A-NN / "stated field" / "none") |
|----|------|-----------|-------|------|--------------------------|------------------------------------------------|--------------------------------------------------|
| S-01 | | | | | | | |

---

### Step 3b — Role: Assumption Archaeologist — Back-fill phase

For each A-NN row, replace `[pending]` with exactly one verdict:
- **Contradicted — S-NN**: Signal challenges this assumption. Cite ID, one sentence.
- **Supported — S-NN**: Signal confirms this assumption. Cite ID.
- **No signal coverage**: No signal speaks to this assumption.

Reproduce the full updated Assumption Table (all 5 columns). After Step 4, update `yes` rows
to `yes — F-NN`.

---

### Step 4 — Role: Delta Identifier

Stop. Before building the findings table, produce two outputs:

1. **Anti-pattern label**: Write the name of the anti-pattern you are guarding against.
2. **PASS/FAIL exhibit** for the delta vs. inventory distinction:

| Example type | Example row |
|-------------|-------------|
| PASS — this is a delta | "F-01: Strategy assumed scout signals suffice before draft / Signal revealed draft can complete without scout artifacts" |
| FAIL — this is inventory | "S-01 covers namespace coverage" or "we have 3 signals in scout" |

Per schema (Delta Findings) — the following columns are mandatory. Do not omit any column:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root (A-NN / "stated field") |
|-----------|-----------------|----------------|-----------------|----------------------------------------|
| F-01 | [from Step 1 or Step 2] | | S-XX | |

After building findings, return to Step 3b and update `yes` rows to `yes — F-NN`.

**Null case — all signals confirm** — reproduce verbatim and skip to Step 6:

| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |

---

### Step 5 — Namespace Coverage Audit

Assess all 9 namespaces by name. Stage-relative = appropriate for current stage.

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

### Step 6 — Conflict Audit

**The following columns are mandatory. Do not omit any column.**

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

**Null case — no conflicts** — reproduce verbatim. Do not omit this table:

| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

---

### Step 7 — Role: Proposal Architect

**Stop. Before building the proposals table, write the following statement verbatim:**

> "Proposals schema committed: Proposal ID ★, Type ★ [Rule 1 — PASS: ADD / REMOVE /
> REPRIORITIZE | FAIL: prose], Change ★, Delta Finding ★ (full 'Strategy assumed [X] /
> Signal revealed [Y]' text from Step 4 with exact ID), Evidence ★, If unchanged ★
> (specific degradation — a row that cannot name one is a preference, not a decision),
> Reversibility ★ [Rule 1 — PASS: (1) Reversible at same cost / (2) Gets harder /
> (3) Becomes impossible | FAIL: prose], Confidence ★. All three types present.
> Empty types use null rows."

**The following columns are mandatory. Do not omit any column.**

| Proposal ID | Type [PASS: ADD / REMOVE / REPRIORITIZE — FAIL: prose] | Change | Delta Finding | Evidence [file(s)] | If unchanged [specific degradation — a row without one is a preference, not a decision] | Reversibility [PASS: (1)/(2)/(3) from list — FAIL: prose] | Confidence |
|------------|-------------------------------------------------------|--------|--------------|-------------------|---------------------------------------------------------------------------------------|----------------------------------------------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [specific degradation named] | (2) Gets harder | High |

Null rows — reproduce verbatim for each empty type:

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 8 — Before/after diff

**Stop. Before building the diff table, write the following statement verbatim:**

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★
> (inline per row as [file.md — ≤10 word finding] — no separate evidence section),
> Proposal ★ (Proposal ID from Step 7). No column omitted."

**The following columns are mandatory. Do not omit any column.**

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

## V-04 — Pre-Hypothesis + Symmetric PASS/FAIL Exhibits

**Axes**: Role sequence (V-01: pre-read hypothesis commitment) + Output format
(V-03: symmetric PASS/FAIL exhibits for all operationalized tests)

**Hypothesis**: V-01's hypothesis step forces pre-commitment to predictions before reading,
making the delta step falsifiable (surprise findings = blindspots). V-03's symmetric
exhibits make the discrimination tests bidirectional — the model confronts both correct
and incorrect cell content before filling. These two mechanisms operate at different
layers (pre-execution commitment vs. cell-level execution precision) and should compose
without interference. The combination tests whether pre-commitment combined with
exhibit-based discrimination guidance produces higher-quality delta findings than either
mechanism alone: the hypothesis primes for surprise detection; the exhibits ensure
structural compliance at fill time. V-04 uses R10 V-03 as base, adds Step 0
hypothesis table and symmetric exhibits throughout, and retains the full COLUMN CONTRACT.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it
was written. Before reading any files, commit to predictions about what you expect to
find. The assumption table is a two-phase artifact: extract at Step 2, back-fill at
Step 3b. Present proposals, wait for confirmation, then write. Do not auto-apply changes.

---

### COLUMN CONTRACT (binding before reading any file)

Two rules govern every table you produce. Read before the Output Schema.

**Rule 1 — Enumerated columns**: Any column using a closed value set must declare those
values at every point where the column is named. Select from the declared set only; prose
is not a valid value.

Rule 1 PASS examples:
- `Type`: `ADD` | `REMOVE` | `REPRIORITIZE`
- `Reversibility`: `(1) Reversible at same cost` | `(2) Gets harder` | `(3) Becomes impossible`
- `Delta candidate?`: `yes` | `no` | `yes — F-01`
- `Consistent with strategy?`: `Yes` | `No` | `Partial`

Rule 1 FAIL examples (treated as absent):
- `Type`: "I suggest adding" | "addition" | "add or remove"
- `Reversibility`: "it will be harder later" | "probably irreversible"
- `Consistent with strategy?`: "mostly yes" | "it depends"

**Rule 2 — Column independence**: Before filling any cell, apply this test: *"Can I fill
this cell without reading the source document?"* If yes, the cell is a structural alias
and is treated as empty.

Rule 2 PASS examples for `Implicit evidence`:
- `"teams run scout before draft"` — specific phrase from strategy.md
- `"signal count threshold never defined"` — paraphrase of absent text

Rule 2 FAIL examples for `Implicit evidence` (treated as absent):
- `A-01` — row key
- `"signals gather evidence"` — restatement
- `"see rationale"` — pointer

---

### Output Schema (read before proceeding to Step 0)

Every table you produce must conform to this schema. Columns marked ★ are mandatory —
do not omit any ★ column. Both Contract Rules apply to every ★ column.

**Hypothesis Table** (Step 0 only — 4 columns mandatory)
| ★ Hypothesis ID | ★ Predicted assumption | ★ Expected signal direction | ★ Expected delta (if signals contradict) |

**Assumption Table** (5 columns — all independently populated per Rule 2)
| ★ Assumption | ★ Implicit evidence [Rule 2 — PASS: phrase from strategy.md | FAIL: row key / restatement / pointer] | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? [Rule 1 — PASS: yes / no / yes — F-NN | FAIL: prose] |

**Signal Inventory**
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? [Rule 1 — PASS: Yes / No / Partial | FAIL: prose] | ★ Assumption link |

**Delta Findings**
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) | ★ Assumption root | ★ Hypothesis match (H-N confirmed / Surprise — not hypothesized) |

**Namespace Audit**
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |

**Conflict Audit**
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals** (Rule 1 applies to Type and Reversibility)
| ★ Proposal ID | ★ Type [Rule 1 — PASS: ADD / REMOVE / REPRIORITIZE | FAIL: prose] | ★ Change | ★ Delta Finding | ★ Evidence | ★ If unchanged | ★ Reversibility [Rule 1 — PASS: (1)/(2)/(3) | FAIL: prose] | ★ Confidence |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

Do not omit any ★ column.

---

### Step 0 — Role: Hypothesis Generator

**Adopt this role**: Before reading any file, commit to predictions. What does this
strategy probably assume? What do signals probably reveal? What is the most likely delta?

These predictions are scored in Step 4. A finding that matches a Step 0 hypothesis is
**confirmed**. A finding with no matching hypothesis is a **surprise** — flagged as highest-value.

**The following columns are mandatory. Do not omit any column.**

| Hypothesis ID | Predicted assumption | Expected signal direction | Expected delta (if signals contradict) |
|--------------|---------------------|---------------------------|----------------------------------------|
| H-01 | [most likely unstated assumption given topic + skill phase] | [signals probably confirm / contradict] | [predicted delta text] |

Write at least one hypothesis. **Do not read any files before completing this step.**

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

### Step 2 — Role: Assumption Archaeologist — Extract phase

**Adopt this role**: Find what strategy.md took for granted without writing.

Systematic scan — cover each dimension:
- (a) Implied audience knowledge level
- (b) Namespace priority ordering assumed without justification
- (c) Signal sufficiency threshold — what "enough signals" means here
- (d) Timeline or sequencing feasibility
- (e) Definition of "done" for this topic

Per schema (Assumption Table) — all five columns mandatory. Apply Rule 2 using the
PASS/FAIL exhibit from the COLUMN CONTRACT before completing each `Implicit evidence` cell.

Column rules:
- **"Contradicted by a signal?"**: Write `[pending]` now. Fill after Step 3a.
- **"Why this matters"**: Fill now. Name the failure mode if wrong.
- **"Delta candidate?"**: Rule 1 — PASS: `yes` or `no`. After Step 4, update to `yes — F-NN`.

| Assumption | Implicit evidence [Rule 2 — PASS: phrase from strategy.md | FAIL: row key / restatement / pointer] | Contradicted by a signal? | Why this matters for delta detection | Delta candidate? [PASS: yes / no | FAIL: prose] |
|-----------|-------------------------------------------------------------------------------------------------------|--------------------------|--------------------------------------|----------------------------------------------|
| [most important] | [phrase from strategy.md — decision-question test before filling] | [pending] | [failure mode if wrong] | yes |

Write at least one row. Null case:

| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |

---

### Step 3a — Role: Signal Analyst — Read phase

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals found** — reproduce verbatim and stop. Do not omit:

> No signals found — strategy.md does not need revision at this time.

Per schema (Signal Inventory) — the following columns mandatory. Rule 1: `Consistent with
strategy?` — PASS: `Yes` / `No` / `Partial`. FAIL: prose:

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? [Yes / No / Partial] | Assumption link (A-NN / "stated field" / "none") |
|----|------|-----------|-------|------|--------------------------|------------------------------------------------|--------------------------------------------------|
| S-01 | | | | | | | |

---

### Step 3b — Role: Assumption Archaeologist — Back-fill phase

For each A-NN row, replace `[pending]` with one verdict:
- **Contradicted — S-NN**: Signal challenges this. Cite ID, one sentence.
- **Supported — S-NN**: Signal confirms this. Cite ID.
- **No signal coverage**: No signal speaks to this.

Reproduce full updated Assumption Table. After Step 4, update `yes` rows to `yes — F-NN`.

---

### Step 4 — Role: Delta Identifier

Stop. Before building the findings table, produce two outputs:

1. **Anti-pattern label**: Name the anti-pattern you are guarding against.
2. **PASS/FAIL exhibit** for the delta vs. inventory distinction:

| Example type | Example |
|-------------|---------|
| PASS — delta | "F-01: Strategy assumed scout signals suffice before draft / S-01 revealed draft can complete without scout artifacts" |
| FAIL — inventory | "S-01 exists and covers namespace coverage" |

For each finding, check Step 0 hypotheses: **H-N confirmed** or **Surprise — not hypothesized**.

Per schema (Delta Findings) — all columns mandatory:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root (A-NN / "stated field") | Hypothesis match |
|-----------|-----------------|----------------|-----------------|----------------------------------------|-----------------|
| F-01 | | | S-XX | | H-N confirmed / Surprise |

After findings, return to Step 3b and update `yes` → `yes — F-NN`.

**Null case** — reproduce verbatim and skip to Step 6:

| F-00 | Strategy confirmed | No gaps detected | All signals | N/A | All confirmed |

---

### Step 5 — Namespace Coverage Audit

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

### Step 6 — Conflict Audit

**The following columns are mandatory. Do not omit any column.**

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

**Null case** — reproduce verbatim. Do not omit:

| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

---

### Step 7 — Role: Proposal Architect

**Stop. Before building the proposals table, write the following statement verbatim:**

> "Proposals schema committed: Proposal ID ★, Type ★ [Rule 1 — PASS: ADD / REMOVE /
> REPRIORITIZE | FAIL: prose], Change ★, Delta Finding ★ (full 'Strategy assumed [X] /
> Signal revealed [Y]' text from Step 4 with exact ID), Evidence ★, If unchanged ★
> (specific degradation — a row without one is a preference, not a decision),
> Reversibility ★ [Rule 1 — PASS: (1) Reversible at same cost / (2) Gets harder /
> (3) Becomes impossible | FAIL: prose], Confidence ★. All three types present.
> Empty types use null rows."

**The following columns are mandatory. Do not omit any column.**

| Proposal ID | Type [PASS: ADD / REMOVE / REPRIORITIZE | FAIL: prose] | Change | Delta Finding | Evidence [file(s)] | If unchanged [specific — no named degradation = preference, not decision] | Reversibility [PASS: (1)/(2)/(3) | FAIL: prose] | Confidence |
|------------|---------------------------------------------------------------|--------|--------------|-------------------|---------------------------------------------------------------------------|-------------------------------------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [specific degradation] | (2) Gets harder | High |

Null rows — reproduce verbatim:

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 8 — Before/after diff

**Stop. Write the following verbatim:**

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★
> (inline [file.md — ≤10 word finding]), Proposal ★ (ID from Step 7). No column omitted."

**The following columns are mandatory. Do not omit any column.**

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current] | [proposed] | [file.md — ≤10 words] | ADD-1 |

---

### Step 9 — Confirmation gate

Reply **YES** to apply all proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 10 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals.
Preserve existing structure; update only sections affected by confirmed changes.

---

## V-05 — Full Ceiling: 4-Rule COLUMN CONTRACT + All Three Mechanisms

**Axes**: Role sequence (V-01) + Inertia framing (V-02) + Symmetric PASS/FAIL exhibits
(V-03) + expanded COLUMN CONTRACT with 4 rules

**Hypothesis**: The R10 V-03 COLUMN CONTRACT with 2 rules covers enumerated columns
(Rule 1) and column independence (Rule 2). Rules 3 and 4 capture two constraints that
currently appear per-step: evidence provenance (every evidence cell traces to a signal
artifact, not to another output column) and null-case completeness (every mandatory
section has a verbatim null template and a "Do not omit" instruction). Elevating these
from per-step instructions to pre-schema CONTRACT rules makes them part of the binding
contract read before any file — the same architectural elevation C-36 applies to Rules 1
and 2. The combination: 4-rule CONTRACT provides the architectural foundation; V-01's
hypothesis step provides pre-commitment; V-02's inertia framing makes proposals load-bearing
arguments rather than signal translations; V-03's symmetric exhibits make every
discrimination test bidirectional. Together they represent the maximum structural
specificity achievable from the five available axes.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it
was written. The current strategy is the status quo. Each proposal must defeat the
current approach by naming what degrades if it is retained and how fast that window
closes. Before reading any files, commit to predictions. Present proposals, wait for
confirmation, then write. Do not auto-apply changes.

---

### COLUMN CONTRACT (binding before reading any file)

Four rules govern every table you produce. Read before the Output Schema.

**Rule 1 — Enumerated columns**: Any column using a closed value set must declare those
values at every point where the column is named. Select from the declared set only; prose
is not a valid value.

Rule 1 PASS examples:
- `Type`: `ADD` | `REMOVE` | `REPRIORITIZE`
- `Reversibility`: `(1) Reversible at same cost` | `(2) Gets harder` | `(3) Becomes impossible`
- `Delta candidate?`: `yes` | `no` | `yes — F-01`
- `Consistent with strategy?`: `Yes` | `No` | `Partial`

Rule 1 FAIL examples (treated as absent):
- `Type`: "I suggest adding" | "addition" | "add or remove"
- `Reversibility`: "will be harder" | "probably can't undo" | "maybe irreversible"
- `Delta candidate?`: "probably yes" | "yes, depending"

**Rule 2 — Column independence**: Before filling any cell, apply this test: *"Can I fill
this cell without reading the source document?"* If yes, the cell is a structural alias
and is treated as empty.

Rule 2 PASS examples for `Implicit evidence`:
- `"teams run scout before draft"` — specific phrase from strategy.md
- `"signal count threshold never defined"` — paraphrase of absent text
- `"the phrase 'gather evidence first' in the rationale block"` — location + text

Rule 2 FAIL examples for `Implicit evidence` (treated as absent):
- `A-01` — row key
- `"signals gather evidence"` — restatement in other words
- `"see rationale section"` — pointer
- `"strategy implies sequencing"` — generic inference

**Rule 3 — Evidence provenance**: Any evidence cell must trace to a specific signal
artifact (filename from `simulations/{topic}/`). It may not trace to another output
column (e.g., "see Delta Finding F-01") or to strategy.md (strategy.md is an input,
not a signal artifact). A pointer to another output column is a navigational alias.

Rule 3 PASS examples: `scout-feasibility-{topic}-2026-03-14.md` | `draft-pitch-{topic}-2026-03-14.md`
Rule 3 FAIL examples: "see F-01" | "per the strategy" | "as noted above"

**Rule 4 — Null-case completeness**: Every mandatory output section has a verbatim null
template. When null conditions are met, reproduce the null template exactly — do not omit
or paraphrase. A section that is skipped when null fails Rule 4 regardless of other output.

Rule 4 null templates are provided in each step below. Each carries a "Do not omit"
instruction. Both the template and the instruction are required.

---

### Output Schema (read before proceeding to Step 0)

Every table you produce must conform to this schema. Columns marked ★ are mandatory.
All four Contract Rules apply to every ★ column.

**Hypothesis Table** (Step 0 only)
| ★ Hypothesis ID | ★ Predicted assumption | ★ Expected signal direction | ★ Expected delta (if contradicted) |

**Assumption Table** (5 columns — all independently populated per Rule 2)
| ★ Assumption | ★ Implicit evidence [Rule 2 — PASS: phrase from strategy.md | FAIL: row key / restatement / pointer] | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? [Rule 1 — PASS: yes / no / yes — F-NN | FAIL: prose] |

**Signal Inventory**
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? [Rule 1 — PASS: Yes / No / Partial | FAIL: prose] | ★ Assumption link (A-NN / "stated field" / "none") |

**Delta Findings**
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) [Rule 3: artifact filename] | ★ Assumption root (A-NN / "stated field") | ★ Hypothesis match (H-N confirmed / Surprise — not hypothesized) |

**Namespace Audit**
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |

**Conflict Audit**
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Inertia Cost Audit**
| ★ Signal ID | ★ Status quo position | ★ Cost if retained [Rule 3: no pointers] | ★ Reversibility window [Rule 1: (1)/(2)/(3)] |

**Proposals** (Rules 1, 3, 4 apply)
| ★ Proposal ID | ★ Type [Rule 1 — PASS: ADD / REMOVE / REPRIORITIZE | FAIL: prose] | ★ Change | ★ Delta Finding | ★ Evidence [Rule 3: artifact filename] | ★ Status quo retains [specific — a proposal that cannot name this is a preference, not a decision] | ★ Reversibility [Rule 1 — PASS: (1)/(2)/(3) | FAIL: prose] | ★ Confidence |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence [Rule 3: artifact inline] | ★ Proposal |

Do not omit any ★ column.

---

### Step 0 — Role: Hypothesis Generator

**Adopt this role**: Before reading any file, commit to predictions. What does this strategy
probably assume? What do signals probably reveal? What delta likely emerges?

Findings that match a Step 0 hypothesis are **confirmed**. Findings with no hypothesis
match are **surprises** — flagged as highest-value discoveries.

**The following columns are mandatory. Do not omit any column.**

| Hypothesis ID | Predicted assumption | Expected signal direction | Expected delta (if contradicted) |
|--------------|---------------------|---------------------------|----------------------------------|
| H-01 | [most likely unstated assumption] | [signals probably confirm / contradict] | [predicted delta] |

Write at least one hypothesis. **Do not read any files before completing this step.**

**Rule 4 null case — no hypotheses possible** — reproduce verbatim. Do not omit:

| H-00 | No pre-read hypotheses generated | N/A | N/A |

---

### Step 1 — Role: Stated-Field Extractor

Read `simulations/{topic}/strategy.md`. Extract only what was written explicitly.

**The following columns are mandatory. Do not omit any column.**

| Field | Value |
|-------|-------|
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Stated rationale | |
| Acknowledged gaps | |

---

### Step 2 — Role: Assumption Archaeologist — Extract phase

**Adopt this role**: Find what strategy.md took for granted without writing. Systematically
check each dimension — a dimension not checked is a dimension that may harbor the highest-value
delta candidate.

Scan dimensions:
- (a) Implied audience knowledge level
- (b) Namespace priority ordering assumed without justification
- (c) Signal sufficiency threshold — what "enough signals" means here
- (d) Timeline or sequencing feasibility
- (e) Definition of "done" for this topic

Per schema (Assumption Table) — all five columns mandatory. Apply Rule 2 to `Implicit evidence`
using the PASS/FAIL exhibit from the COLUMN CONTRACT.

Column rules:
- **"Contradicted by a signal?"**: Write `[pending]` now. Fill after Step 3a.
- **"Why this matters"**: Fill now — name the failure mode if this assumption is wrong.
- **"Delta candidate?"**: Rule 1 — PASS: `yes` or `no`. After Step 4, update to `yes — F-NN`.

| Assumption | Implicit evidence [Rule 2 — PASS: phrase from strategy.md | FAIL: row key / restatement / pointer] | Contradicted by a signal? | Why this matters for delta detection | Delta candidate? [PASS: yes / no | FAIL: prose] |
|-----------|-------------------------------------------------------------------------------------------------------|--------------------------|--------------------------------------|----------------------------------------------|
| [most important] | [phrase from strategy.md — test: "Can I fill this without reading strategy.md?"] | [pending] | [failure mode if wrong] | yes |

Write at least one row. **Rule 4 null case** — reproduce verbatim. Do not omit:

| No unstated assumptions found after systematic scan across all 5 dimensions | N/A | N/A | N/A | no |

---

### Step 3a — Role: Signal Analyst — Read phase

Glob `simulations/{topic}/` recursively. Read every file found.

**Rule 4 null case — no signals found** — reproduce verbatim and stop. Do not omit:

> No signals found — strategy.md does not need revision at this time.

Per schema (Signal Inventory) — all columns mandatory. Rule 1: `Consistent with strategy?`
PASS: `Yes` / `No` / `Partial`. FAIL: prose. Rule 3: `File` must be an artifact filename:

| ID | File [Rule 3: artifact filename] | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? [Yes / No / Partial] | Assumption link (A-NN / "stated field" / "none") |
|----|----------------------------------|-----------|-------|------|--------------------------|------------------------------------------------|--------------------------------------------------|
| S-01 | | | | | | | |

---

### Step 3b — Role: Assumption Archaeologist — Back-fill phase

For each A-NN row, replace `[pending]` with one verdict:
- **Contradicted — S-NN**: Signal challenges this. Cite ID, one sentence.
- **Supported — S-NN**: Signal confirms this. Cite ID.
- **No signal coverage**: No signal speaks to this.

Reproduce full updated Assumption Table. After Step 4, update `yes` → `yes — F-NN`.

---

### Step 4 — Role: Delta Identifier

Stop. Before building findings, produce both outputs:

1. **Anti-pattern label**: Write the name of the anti-pattern you are guarding against.
2. **PASS/FAIL exhibit**:

| Example type | Example |
|-------------|---------|
| PASS — delta | "F-01: Strategy assumed scout signals suffice before draft / S-01 revealed draft can complete without scout artifacts" |
| FAIL — inventory | "S-01 covers namespace coverage" or "we have 3 signals in scout" |

For each finding: check Step 0 hypotheses — **H-N confirmed** or **Surprise — not hypothesized**.

Per schema (Delta Findings) — all columns mandatory. Rule 3 applies to `Source signal(s)`:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) [Rule 3: artifact filename] | Assumption root (A-NN / "stated field") | Hypothesis match |
|-----------|-----------------|----------------|---------------------------------------------|----------------------------------------|-----------------|
| F-01 | | | | | H-N confirmed / Surprise |

After findings, return to Step 3b and update `yes` → `yes — F-NN`.

**Rule 4 null case** — reproduce verbatim and skip to Step 6. Do not omit:

| F-00 | Strategy confirmed | No gaps detected | All signals | N/A | All confirmed |

---

### Step 5 — Namespace Coverage Audit

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

### Step 6 — Conflict Audit

**The following columns are mandatory. Do not omit any column.**

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

**Rule 4 null case** — reproduce verbatim. Do not omit:

| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

---

### Step 7a — Inertia Cost Audit

Before building proposals, rank every signal by the cost to the current strategy if it
is not acted on. The current strategy is the status quo; each signal is a potential
challenger. A signal that costs nothing to ignore should not become a proposal.

Per schema (Inertia Cost Audit) — all columns mandatory. Rule 1 applies to
`Reversibility window` — PASS: `(1)/(2)/(3)`. FAIL: prose:

| Signal ID | Status quo position [what the current strategy does here] | Cost if retained [specific — Rule 3: no pointers] | Reversibility window [(1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible] |
|-----------|----------------------------------------------------------|--------------------------------------------------|-----------------------------------------------------------------------------------------------|
| S-01 | | | |

**Rule 4 null case** — reproduce verbatim. Do not omit:

| SC-00 | All signals confirm current strategy | No degradation | (1) Reversible at same cost |

---

### Step 7b — Role: Proposal Architect

**Stop. Before building the proposals table, write the following statement verbatim:**

> "Proposals schema committed: Proposal ID ★, Type ★ [Rule 1 — PASS: ADD / REMOVE /
> REPRIORITIZE | FAIL: prose], Change ★, Delta Finding ★ (full 'Strategy assumed [X] /
> Signal revealed [Y]' text from Step 4 with exact ID), Evidence ★ [Rule 3: artifact
> filename], Status quo retains ★ (what the current strategy keeps if this proposal is
> deferred — a proposal that cannot name this is a preference, not a decision),
> Reversibility ★ [Rule 1 — PASS: (1)/(2)/(3) | FAIL: prose], Confidence ★.
> All three types present. Empty types use Rule 4 null rows."

**The following columns are mandatory. Do not omit any column.**

| Proposal ID | Type [PASS: ADD / REMOVE / REPRIORITIZE | FAIL: prose] | Change | Delta Finding | Evidence [Rule 3: artifact filename] | Status quo retains [specific — a proposal that cannot name this is a preference, not a decision] | Reversibility [PASS: (1)/(2)/(3) | FAIL: prose] | Confidence |
|------------|---------------------------------------------------------------|--------|--------------|--------------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [specific retention — and why it eventually fails] | (2) Gets harder | High |

**Rule 4 null rows** — reproduce verbatim for each empty type. Do not omit:

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | Status quo retains: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | Status quo retains: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | Status quo retains: N/A | N/A | — |

---

### Step 8 — Role: Diff Author

**Stop. Before building the diff table, write the following statement verbatim:**

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★
> [Rule 3: artifact filename inline as (file.md — ≤10 word finding) — no separate
> evidence section], Proposal ★ (ID from Step 7b). Rule 1 applies to all enumerated
> columns. No column omitted."

**The following columns are mandatory. Do not omit any column.**

| Namespace | Skill/Area | Before | After | Evidence [artifact inline — ≤10 words] | Proposal |
|-----------|-----------|--------|-------|----------------------------------------|---------|
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

## Round 11 Summary

| Variation | Primary axes | COLUMN CONTRACT | Step 0 | Inertia framing | Symmetric exhibits | Key prediction |
|-----------|-------------|-----------------|--------|-----------------|-------------------|----------------|
| V-01 | Role sequence | Rule 1 + Rule 2 | Yes — Hypothesis Generator | No | No | Surprise findings reveal blindspots; confirmed = not discriminating |
| V-02 | Inertia framing | Rule 1 + Rule 2 | No | Yes — status-quo competitor + audit table | No | Proposals as arguments defeat more than formatting compliance |
| V-03 | Output format | Rule 1 + Rule 2 | No | No | Yes — PASS/FAIL for all tests | Bidirectional exhibits prevent novel shortcuts that pass recognition but fail intent |
| V-04 | Role sequence + Output format | Rule 1 + Rule 2 | Yes | No | Yes | Pre-commitment + bidirectional exhibits compose without interference |
| V-05 | All three + expanded contract | 4 rules (+ provenance + null) | Yes | Yes | Yes | 4-rule architectural elevation makes all per-step constraints part of the pre-reading contract |

**The C-36/C-37 mechanisms are maintained in all five variations.** Every variation carries:
- Named COLUMN CONTRACT preceding the output schema (C-36 architecture)
- Decision-question independence test embedded in `Implicit evidence` column definition (C-37 operationalization)
- All enumerated columns with closed value lists at both the upfront schema and commitment checkpoints (C-34)

**The R11 open question**: Do pre-execution commitments (V-01 hypothesis, V-05 extended contract) improve delta quality beyond structural compliance? Do symmetric exhibits reduce novel structural shortcuts that R10 exhibit-only examples cannot anticipate?
