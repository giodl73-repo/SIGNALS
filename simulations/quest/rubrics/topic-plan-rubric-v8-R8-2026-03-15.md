# topic-plan — Round 8 Variations (v7 rubric)

**Skill**: `topic:plan`
**Rubric**: v7 (C-01–C-31, 205 pts total)
**Date**: 2026-03-15

---

## Round 8 Design Notes

R7 set the ceiling at V-05 with the full C-24+C-25+C-26+C-27 stack, role sequence, and reversibility. The four new v7 criteria split across two layers:

- **Role-scoped enforcement** (C-28, C-31): named role + scan dimensions; inertia column as decision gate
- **Assumption traceability** (C-29, C-30): closing the assumption table's backward and forward arcs

**What R7 achieved and where gaps remain:**

| Criterion | Best R7 mechanism | Gap R8 must close |
|-----------|-------------------|-------------------|
| C-28 | Assumption Archaeologist + scan (a-e) in V-01, V-04, V-05 | Role present, scan present — but not declared in upfront schema; back-fill step was column annotation, not role return |
| C-29 | "Contradicted?" col with "fill after Step 3" in V-05 | Back-fill is a column annotation, not a named lifecycle event; model fills a header instruction rather than executing a distinct revisit act |
| C-30 | "Why this matters" col in V-02 (partial), "Contradicted?" col in V-05 (partial) | Neither variation had BOTH delta-relevance AND delta-candidate designation simultaneously — C-30 was never met in R7 |
| C-31 | "A proposal that can't answer the second question is a preference, not a decision" in V-03 preamble | Disqualification sentence appeared before the column template, not adjacent to it — C-31 requires adjacency to the column definition |

**R8 target**: First full coverage of C-28 + C-29 + C-30 + C-31, with C-30 as the primary new discriminator.

**Three single-axis dimensions explored in R8:**

1. **Output format** — the assumption table is redesigned as a 5-column bidirectional schema (ID + assumed + back-fill + delta-relevance + delta-candidate), declared at extraction time, making C-29 and C-30 structurally inevitable rather than instructed additions.

2. **Inertia framing** — the "If unchanged" column definition includes the disqualification rule as a column-adjacent annotation, satisfying C-31's adjacency requirement and converting the column from a format cell to a structural gate.

3. **Lifecycle emphasis** — back-fill is promoted from a deferred column annotation to a named sub-step with its own role return obligation, satisfying C-29's "revisit" requirement and making each phase of the assumption table a verifiable act.

**Variation design:**

| Variation | Axis | Type | Primary R8 target |
|-----------|------|------|-------------------|
| V-01 | Output format — complete assumption table schema at extraction time | Single | C-29 + C-30 |
| V-02 | Inertia framing — decision-gate rule adjacent to column definition | Single | C-31 |
| V-03 | Lifecycle emphasis — back-fill as a named lifecycle sub-step | Single | C-29 |
| V-04 | Output format + Role sequence — assumption lifecycle schema + Archaeologist role + schema-first | Combination | C-28 + C-29 + C-30 |
| V-05 | Full stack: all four new criteria + R7 ceiling mechanisms | Combination | C-28 + C-29 + C-30 + C-31 |

---

## V-01 — Complete Assumption Table Schema

**Axis**: Output format — the assumption table is declared as a 5-column bidirectional bridge at extraction time, making C-29 and C-30 structurally inevitable

**Hypothesis**: R7 introduced "Contradicted?" as a column annotation ("fill after Step 3") and the "Why this matters for delta detection" column appeared only in V-02. Neither variation declared both the back-fill column and the forward-reasoning columns simultaneously at extraction time. The gap is that columns added as deferred-fill annotations are treated as lower-priority under context pressure — the model sees the column heading but treats the deferred fill as optional. If the assumption table is declared upfront as a 5-column schema — ID + assumed + back-fill (placeholder now, filled after Step 2) + delta-relevance + delta-candidate designation — the model cannot produce a complete Step 1b without all five columns present. The hypothesis is that declaring the full assumption schema at extraction time prevents selective omission of the C-30 columns, because partial completion is structurally visible rather than silently skipped. Note: this variation intentionally omits the named "Assumption Archaeologist" role (C-28) to isolate whether output format alone achieves C-29/C-30 without role-scoping.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it was written. The assumption table you build in Step 1b is a complete two-way bridge — it links from strategy beliefs backward to signal evidence (back-fill after Step 2), and forward to delta findings and proposals (candidate designation after Step 3). Present proposals, wait for confirmation, then write. Do not auto-apply changes.

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

Your job is to find what strategy.md took for granted without writing. These are the highest-value delta candidates — a signal can contradict what was assumed, not only what was stated.

Scan across at least five dimensions: (a) implied audience knowledge level, (b) namespace priority ordering, (c) signal sufficiency threshold, (d) timeline or sequencing feasibility, (e) what "done" means in this context. Add others if found.

**The assumption table has five mandatory columns. Do not omit any column.**

Column rules:
- **"Contradicted by a signal?"**: Write `[fill after Step 2]` as placeholder now. Return here after Step 2 and populate with a signal-grounded verdict.
- **"Why this matters for delta detection"**: Fill now. Name the specific failure mode if this assumption is wrong — which skills or namespaces would change priority.
- **"Delta candidate?"**: Fill now. Write `yes` if contradicting this assumption would change strategy direction; `no` if it would not. After Step 3, update `yes` rows to `yes — F-NN` with the actual Finding ID.

| Assumption ID | What strategy.md assumed without writing | Contradicted by a signal? | Why this matters for delta detection | Delta candidate? |
|--------------|------------------------------------------|--------------------------|-------------------------------------|-----------------|
| A-01 | [most important — highest likelihood of signal contradiction] | [fill after Step 2] | [specific failure mode if this assumption is wrong] | yes / no |
| A-02 | [second assumption, if any] | [fill after Step 2] | | yes / no |

Write at least one row. If no unstated assumptions found after systematic scan:

| A-00 | No unstated assumptions found after systematic scan | N/A | N/A | no |

---

### Step 2 — Read signal artifacts

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals found** — reproduce the following verbatim and stop. Do not omit this output:

> No signals found — strategy.md does not need revision at this time.

**The following columns are mandatory. Do not omit any column.**

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? | Assumption link (A-NN / "stated field" / "none") |
|----|------|-----------|-------|------|--------------------------|--------------------------|--------------------------------------------------|
| S-01 | | | | | | Yes / No / Partial | |

**After building this table, return to Step 1b and fill the "Contradicted by a signal?" column for each A-NN row.** For each assumption contradicted, cite the S-NN ID and write one sentence describing the contradiction. For assumptions not contradicted, write "Not contradicted — assumption stands." For assumptions with no signal coverage, write "No signal coverage."

---

### Step 3 — Identify the delta

Stop. Before building the findings table, write the name of the anti-pattern you are guarding against at this step.

**The following columns are mandatory. Do not omit any column.**

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root (A-NN / "stated field") |
|-----------|-----------------|----------------|-----------------|----------------------------------------|
| F-01 | [from Step 1a stated fields or Step 1b assumptions] | | S-XX | |

After building findings, return to Step 1b and update "Delta candidate?" — change `yes` to `yes — F-NN` for rows that produced a finding.

**Null case — all signals confirm** — reproduce verbatim and skip to Step 5. Do not omit this row:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root |
|-----------|-----------------|----------------|-----------------|-----------------|
| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |

---

### Step 4 — Namespace coverage audit

Assess all 9 namespaces by name. "Stage-relative" = appropriate for this topic's current stage, not a raw count.

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

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Confidence |
|------------|------|--------|--------------|-------------------|-------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [specific gap that persists or worsens if deferred] | High |

All three types (ADD, REMOVE, REPRIORITIZE) must appear. Reproduce null rows verbatim for empty types:

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Confidence |
|------------|------|--------|--------------|-------------------|-------------|------------|
| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |

Delta Finding must reproduce the full "Strategy assumed [X] / Signal revealed [Y]" text from Step 3 with exact Finding ID. Every Proposal ID must trace back through its Delta Finding to an Assumption root (A-NN or "stated field") in the Step 1b table.

---

### Step 7 — Before/after diff

Before building the diff table, write the following statement verbatim:

> "Diff schema: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★ (inline as [file.md — ≤10 word finding]), Proposal ★ (Proposal ID from Step 6). No separate evidence section."

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

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals. Preserve existing structure; update only sections affected by confirmed changes.

---

## V-02 — Decision-Gate Framing

**Axis**: Inertia framing — the "If unchanged" column definition includes an adjacent disqualification rule, converting the column from a format requirement to a structural proposal-validity gate

**Hypothesis**: R7 V-03 included "A proposal that can't answer the second question is a preference, not a decision" as a Step 6 preamble. C-31 requires the disqualification statement to appear "adjacent to the column definition." The R7 V-03 mechanism fails C-31 because the sentence appeared 3-4 lines above the column template — the adjacency requirement was not met. If the disqualification rule is placed directly inside the column header — as a parenthetical within the column heading text itself — the model cannot fill the cell without confronting the gate. The hypothesis is that adjacency converts C-31 from an instructional requirement (rule stated somewhere) to a structural requirement (rule present at the moment of fill). When the disqualification sentence is in the column header, a model writing "gap will remain" in that cell is writing it immediately next to a statement that labels such an answer as disqualifying. This variation carries the full R7 V-05 enforcement stack (schema-first + cascade checkpoints) to isolate the C-31 adjacency mechanism as the single discriminating axis.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it was written. Present proposals, wait for confirmation, then write. Do not auto-apply changes.

**Before reading any files, review the complete output schema below.** Every table you produce must conform to this schema. Columns marked ★ are mandatory — do not omit any ★ column.

---

### Output Schema (read before proceeding to Step 1)

**Signal Inventory**
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? | ★ Assumption link |

**Assumption Table**
| ★ Assumption ID | ★ What assumed | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? |

**Delta Findings**
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) | ★ Assumption root |

**Namespace Audit**
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |

**Conflict Audit**
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals**
| ★ Proposal ID | ★ Type | ★ Change | ★ Delta Finding | ★ Evidence | ★ If unchanged | ★ Confidence |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

Do not omit any ★ column. A table missing any ★ column fails schema validation.

---

### Step 1 — Read strategy.md

Read `simulations/{topic}/strategy.md`. Extract stated fields and unstated assumptions.

**Stated fields** (mandatory columns):

| Field | Value |
|-------|-------|
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Stated rationale | |
| Acknowledged gaps | |

**Unstated assumptions** — per schema (Assumption Table). The following columns are mandatory. Do not omit any column. "Contradicted?" is filled after Step 2 — write `[fill after Step 2]` as placeholder:

| Assumption ID | What strategy.md assumed without writing | Contradicted by a signal? | Why this matters for delta detection | Delta candidate? |
|--------------|------------------------------------------|--------------------------|-------------------------------------|-----------------|
| A-01 | [most important for delta detection] | [fill after Step 2] | | yes / no |

Write at least one row.

---

### Step 2 — Read signal artifacts

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals found** — reproduce the following verbatim and stop. Do not omit this output:

> No signals found — strategy.md does not need revision at this time.

Per schema (Signal Inventory) — the following columns are mandatory. Do not omit any column:

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? | Assumption link (A-NN / "stated field" / "none") |
|----|------|-----------|-------|------|--------------------------|--------------------------|--------------------------------------------------|
| S-01 | | | | | | Yes / No / Partial | |

After building this table, return to Step 1 and fill the "Contradicted by a signal?" column for each assumption row.

---

### Step 3 — Identify the delta

Stop. Before building the findings table, write the name of the anti-pattern you are guarding against at this step. Then write one sentence: what the delta IS vs. what it IS NOT.

Per schema (Delta Findings) — the following columns are mandatory. Do not omit any column:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root (A-NN / "stated field") |
|-----------|-----------------|----------------|-----------------|----------------------------------------|
| F-01 | | | S-XX | |

**Null case — all signals confirm** — reproduce verbatim and skip to Step 5. Do not omit this row:

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

> "Proposals schema committed: Proposal ID ★, Type ★, Change ★, Delta Finding ★ (full 'Strategy assumed [X] / Signal revealed [Y]' text from Step 3 with exact ID), Evidence ★, If unchanged ★ (specific degradation — not a synonym of the delta finding), Confidence ★. All three types present. Empty types use null rows."

Per schema (Proposals) — the following columns are mandatory. Do not omit any column.

**Column rule for "If unchanged"**: Name the specific artifact that won't be gathered, the decision that becomes harder, or the gap that compounds — not a restatement of the delta finding.

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged [a row that cannot name a specific degradation here is a preference, not a decision] | Confidence |
|------------|------|--------|--------------|-------------------|----------------------------------------------------------------------------------------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [which artifact won't be gathered / which decision becomes harder to close] | High |

Null rows (reproduce verbatim for each empty type):

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Confidence |
|------------|------|--------|--------------|-------------------|-------------|------------|
| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |

---

### Step 7 — Before/after diff

Before building the diff table, write the following statement verbatim:

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★ (inline per row as [file.md — ≤10 word finding] — no separate evidence section), Proposal ★ (Proposal ID from Step 6)."

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

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals. Preserve existing structure; update only sections affected by confirmed changes.

---

## V-03 — Back-fill as Named Lifecycle Phase

**Axis**: Lifecycle emphasis — back-fill is promoted from a deferred column annotation to an explicit named sub-step with its own role return obligation

**Hypothesis**: R7 V-05 used "fill after Step 3" as a column header annotation, with a post-findings instruction embedded in the Step 3 body. C-29 requires the model to "revisit the assumption table and populate a back-fill column for each extracted assumption, indicating whether a signal contradicts it and citing the contradicting artifact when applicable." The gap is that a column annotation or a post-step instruction is discharged minimally — the model fills a binary "contradicted / not contradicted" flag rather than executing a citation-grounded adjudication. If back-fill is a named step — "Step 2b: Back-fill Phase — return to the assumption table as a signal adjudicator and produce a verdict-per-row with signal citation" — the model treats it as a first-class execution act with verifiable output. The lifecycle distinction matters because C-29's pass condition is an adjudication, not a flag. This variation intentionally omits the forward-reasoning columns (C-30) and the adjacent decision-gate rule (C-31) to isolate whether the named lifecycle phase alone achieves C-29.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it was written. The assumption table has a two-phase lifecycle: extraction (Step 1b) and back-fill (Step 2b). Each phase is a distinct cognitive act — do not conflate them. Present proposals, wait for confirmation, then write. Do not auto-apply changes.

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

**Adopt this role**: You are an assumption archaeologist. Your job is to find what strategy.md took for granted without writing — the implied worldview, the unstated preconditions, the beliefs the author would defend if challenged but never put in the document.

Systematic scan — cover each dimension:
- (a) Implied audience knowledge level
- (b) Namespace priority ordering assumed without justification
- (c) Signal sufficiency threshold — what "enough signals" means here
- (d) Timeline or sequencing feasibility
- (e) Definition of "done" for this topic

**The following columns are mandatory. Do not omit any column. The "Contradicted?" column is filled in Step 2b — not now. Write `[pending]` as placeholder.**

| Assumption ID | What strategy.md assumed without writing | Contradicted? [pending — filled in Step 2b] |
|--------------|------------------------------------------|---------------------------------------------|
| A-01 | [most important for delta detection — highest likelihood of signal contradiction] | pending |
| A-02 | [second assumption, if any] | pending |

Write at least one row. If no unstated assumptions found: write A-00 "No unstated assumptions found after systematic scan."

---

### Step 2a — Role: Signal Analyst — Read phase

**Adopt this role**: You are a signal analyst. Read every artifact and evaluate it against two reference points: (a) stated fields from Step 1a, and (b) assumptions from Step 1b. The "Assumption link" column maps each signal to the reference point it speaks to most directly.

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals found** — reproduce the following verbatim and stop. Do not omit this output:

> No signals found — strategy.md does not need revision at this time.

**The following columns are mandatory. Do not omit any column.**

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? | Assumption link (A-NN / "stated field" / "none") |
|----|------|-----------|-------|------|--------------------------|--------------------------|--------------------------------------------------|
| S-01 | | | | | | Yes / No / Partial | |

---

### Step 2b — Role: Assumption Archaeologist — Back-fill phase

**Return to this role**: You are back as the assumption archaeologist. Now that you have read all signals, adjudicate every assumption from Step 1b against the signal evidence.

For each A-NN row, replace `pending` with exactly one of the following verdicts. Do not leave any row as `pending`:

- **Contradicted — S-NN**: A signal directly challenges this assumption. Cite the signal ID. Write one sentence on the contradiction.
- **Supported — S-NN**: A signal confirms this assumption. Cite the signal ID.
- **No signal coverage**: No artifact in the current set speaks to this assumption.

Reproduce the full updated assumption table:

| Assumption ID | What strategy.md assumed without writing | Contradicted? [verdict from signal evidence] |
|--------------|------------------------------------------|----------------------------------------------|
| A-01 | [copied from Step 1b] | [Contradicted — S-XX / Supported — S-XX / No signal coverage] |

Every row must have a verdict. A row left as `pending` fails this step.

---

### Step 3 — Role: Delta Identifier

**Adopt this role**: Name the gap between strategy beliefs and signal evidence — not an inventory, a finding for each contradicted belief.

Stop. Before building the findings table, write the name of the anti-pattern you are guarding against at this step.

**The following columns are mandatory. Do not omit any column.**

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root (A-NN / "stated field") |
|-----------|-----------------|----------------|-----------------|----------------------------------------|
| F-01 | [from Step 1a stated fields or Step 1b assumptions marked Contradicted] | | S-XX | |

**Null case — all signals confirm** — reproduce verbatim and skip to Step 5:

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

**Adopt this role**: Find pairs of artifacts pointing in opposite directions on the same dimension.

**The following columns are mandatory. Do not omit any column.**

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

**Null case — no conflicts** — reproduce verbatim. Do not omit this table:

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

---

### Step 6 — Role: Proposal Architect

**Adopt this role**: Translate each finding into a typed, defensible proposal.

**The following columns are mandatory. Do not omit any column.**

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Confidence |
|------------|------|--------|--------------|-------------------|-------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [specific gap that persists or worsens if deferred] | High |

All three types (ADD, REMOVE, REPRIORITIZE) must appear. Reproduce null rows verbatim for empty types:

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Confidence |
|------------|------|--------|--------------|-------------------|-------------|------------|
| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |

---

### Step 7 — Role: Diff Author

**Adopt this role**: Show the exact before/after change for every confirmed proposal.

Before building the diff table, write the following statement verbatim:

> "Diff schema confirmed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★ (inline per row as [file.md — ≤10 word finding] — no separate evidence section), Proposal ★ (Proposal ID from Step 6)."

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

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals. Preserve existing structure; update only sections affected by confirmed changes.

---

## V-04 — Assumption Lifecycle Schema + Role Sequence

**Axes**: Output format (V-01 complete assumption table schema) + Role sequence (Assumption Archaeologist + scan dimensions) + Schema-first priming (C-26) + Cascade checkpoints (C-27)

**Hypothesis**: V-01 introduces the complete 5-column assumption table at extraction time, making C-29 and C-30 structurally inevitable. But without schema-first priming (C-26), the column declarations appear only at Step 1b — the model has not committed to the full assumption table schema before reading strategy.md. If the upfront ★ schema block includes the assumption table with all five columns declared before Step 1, the model commits to the bidirectional bridge schema before encountering any content. Role sequence then ensures the extraction act (Assumption Archaeologist, scan dimensions) and the back-fill act (Archaeologist returns, signal adjudication) are cognitively distinct. The combination separates three independent failure modes: column omission under context pressure (C-26 addresses), shallow extraction (role sequence addresses), and missing back-fill lifecycle (explicit sub-step addresses). C-28 is met by the Archaeologist role + scan dimensions. C-29 is met by the back-fill sub-step. C-30 is met by the delta-relevance and delta-candidate columns in upfront schema and Step 1b. C-31 is intentionally excluded to isolate C-28+C-29+C-30 in combination.

---

You are executing `topic:plan` for the topic `{topic}`.

**Before reading any files, review the complete output schema below.** Every table you produce must conform to this schema. Columns marked ★ are mandatory — do not omit any ★ column. You will adopt a named cognitive role at each phase. The structural contract below governs output regardless of role.

---

### Output Schema (read before proceeding to Step 1)

**Assumption Table** (full bidirectional bridge — all 5 columns mandatory)
| ★ Assumption ID | ★ What assumed | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? |

**Signal Inventory**
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? | ★ Assumption link |

**Delta Findings**
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) | ★ Assumption root |

**Namespace Audit**
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |

**Conflict Audit**
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals**
| ★ Proposal ID | ★ Type | ★ Change | ★ Delta Finding | ★ Evidence | ★ If unchanged | ★ Confidence |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

**Traceability obligation**: Every Proposal row must trace: Diff (Proposal ID) → Proposals (Delta Finding) → Delta Findings (Finding ID) → Assumption Table (Assumption root). Every chain hop must be filled.

Do not omit any ★ column.

---

### Step 1a — Role: Stated-Field Extractor

**Adopt this role**: Extract only what strategy.md wrote explicitly. Verbatim or paraphrase — but only what the document actually says. Do not interpret or supplement.

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

**Adopt this role**: You are an assumption archaeologist. Find what strategy.md took for granted without writing — the implied worldview, the unstated preconditions, the beliefs the author would defend if challenged but never put in the document. These are the highest-value delta candidates.

Systematic scan — cover each dimension explicitly:
- (a) Implied audience knowledge level
- (b) Namespace priority ordering assumed without justification
- (c) Signal sufficiency threshold — what "enough signals" means here
- (d) Timeline or sequencing feasibility
- (e) Definition of "done" for this topic

Per schema (Assumption Table) — all five columns are mandatory. Do not omit any column.

Column rules:
- **"Contradicted by a signal?"**: Write `[pending]` now. Filled in Step 2b.
- **"Why this matters for delta detection"**: Fill now. Which skills or namespaces would change priority if this assumption is wrong?
- **"Delta candidate?"**: Fill now. `yes` if contradicting this would change strategy direction; `no` if not. After Step 3, update `yes` to `yes — F-NN`.

| Assumption ID | What strategy.md assumed without writing | Contradicted by a signal? | Why this matters for delta detection | Delta candidate? |
|--------------|------------------------------------------|--------------------------|-------------------------------------|-----------------|
| A-01 | [most important for delta detection] | [pending] | [failure mode if wrong] | yes / no |
| A-02 | [second assumption, if any] | [pending] | | yes / no |

Write at least one row. Null case: A-00 "No unstated assumptions found after systematic scan."

---

### Step 2a — Role: Signal Analyst — Read phase

**Adopt this role**: Read every artifact against two reference points: (a) stated fields from Step 1a, and (b) assumptions from Step 1b. Map each signal to its reference point.

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals found** — reproduce the following verbatim and stop. Do not omit this output:

> No signals found — strategy.md does not need revision at this time.

Per schema (Signal Inventory) — the following columns are mandatory. Do not omit any column:

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? | Assumption link (A-NN / "stated field" / "none") |
|----|------|-----------|-------|------|--------------------------|--------------------------|--------------------------------------------------|
| S-01 | | | | | | Yes / No / Partial | |

---

### Step 2b — Role: Assumption Archaeologist — Back-fill phase

**Return to this role**: Adjudicate every assumption from Step 1b against the full signal set.

For each A-NN row, replace `[pending]` with a signal-grounded verdict — exactly one per row:
- **Contradicted — S-NN**: Signal challenges this assumption. Cite ID, one sentence on the contradiction.
- **Supported — S-NN**: Signal confirms this assumption. Cite ID.
- **No signal coverage**: No signal speaks to this assumption.

Reproduce the full updated Assumption Table (5 columns). Every row must have a verdict — no row remains `[pending]`.

After completing Step 3, return to this table and update "Delta candidate?" — change `yes` to `yes — F-NN` for rows that produced a finding.

---

### Step 3 — Role: Delta Identifier

**Adopt this role**: Name the gap between strategy beliefs and signal evidence.

**Stop. Before building the findings table, produce both:**

1. **Anti-pattern label**: Name the anti-pattern you are guarding against. Write the label.
2. **Delta definition**: Delta IS: [gap between belief and signal]. Delta IS NOT: [inventory of signal existence].

Per schema (Delta Findings) — the following columns are mandatory. Do not omit any column:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root (A-NN / "stated field") |
|-----------|-----------------|----------------|-----------------|----------------------------------------|
| F-01 | | | S-XX | |

After completing findings, return to Step 2b and update all `yes` entries in "Delta candidate?" with actual F-NN IDs.

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

**Adopt this role**: Find pairs of artifacts pointing in opposite directions on the same dimension.

Per schema (Conflict Audit) — the following columns are mandatory. Do not omit any column:

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

**Null case** — reproduce verbatim:

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

---

### Step 6 — Role: Proposal Architect

**Adopt this role**: Translate each finding into a typed, defensible proposal. Every Proposal ID must trace to a Finding ID (via Delta Finding) and from there to an Assumption root.

**Stop. Before building the proposals table, write the following statement verbatim:**

> "Proposals schema committed: Proposal ID ★, Type ★, Change ★, Delta Finding ★ (full 'Strategy assumed [X] / Signal revealed [Y]' text from Step 3 with exact Finding ID), Evidence ★, If unchanged ★ (specific degradation — not a synonym of the delta finding), Confidence ★. All three types present. Empty types use null rows. Traceability: each Proposal ID traces to a Finding ID via Delta Finding, and from there to an Assumption root."

Per schema (Proposals) — the following columns are mandatory. Do not omit any column:

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Confidence |
|------------|------|--------|--------------|-------------------|-------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [specific gap that persists or worsens if deferred] | High |

Null rows (reproduce verbatim for each empty type):

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Confidence |
|------------|------|--------|--------------|-------------------|-------------|------------|
| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |

---

### Step 7 — Role: Diff Author

**Adopt this role**: Show the exact before/after for every confirmed proposal. Every Proposal ID is the entry point into the full traceability chain.

**Stop. Before building the diff table, write the following statement verbatim:**

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★ (inline per row as [file.md — ≤10 word finding] — no separate evidence section), Proposal ★ (Proposal ID from Step 6 — entry point into Proposal → Delta Finding → Assumption root chain)."

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

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals. Preserve existing structure; update only sections affected by confirmed changes.

---

## V-05 — Full Stack: All Four New Criteria + R7 Ceiling

**Axes**: Complete assumption table lifecycle (V-01) + Decision-gate framing adjacent to column (V-02) + Named back-fill lifecycle phase (V-03) + Schema-first priming (C-26) + Cascade checkpoints (C-27) + Reversibility dimension (R7 V-03) + Explicit traceability chain (R7 V-05)

**Hypothesis**: R7 V-05 set the ceiling at C-24+C-25+C-26+C-27 with role sequence and reversibility. R8 V-05 extends to close all four v7 criteria simultaneously. C-28: Assumption Archaeologist role + explicit scan dimensions (a-f) declared in upfront schema. C-29: Back-fill as a named lifecycle phase (Step 2b) with verdict-per-row obligation — not a column annotation. C-30: Full 5-column assumption table (extraction + back-fill + delta-relevance + delta-candidate designation) declared in upfront schema and executed in Step 1b, updated in Step 3. C-31: Decision-gate rule placed adjacent to the "If unchanged" column header in the proposals table template — not in the step preamble. The reversibility column is retained from R7 V-03. The A-NN → F-NN → Proposal ID traceability chain is named as a navigation obligation in the upfront schema. The Step 6 checkpoint carries triple weight: schema commitment + null-row obligation + traceability chain declaration. V-05 is the R8 ceiling and the most demanding variation. The primary test is whether C-30's forward-reasoning columns (delta-relevance + candidate designation) at extraction time change what findings the model surfaces in Step 3, compared to C-24+C-29 alone.

---

You are executing `topic:plan` for the topic `{topic}`.

**Before reading any files, review the complete output schema below.** Every table you produce must conform to this schema. Columns marked ★ are mandatory — do not omit any ★ column. A table missing any ★ column fails schema validation regardless of other content.

---

### Output Schema (read before proceeding to Step 1)

**Assumption Table** (full bidirectional bridge — 5 columns mandatory)
| ★ Assumption ID | ★ What assumed | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? |

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

**Traceability obligation**: Every Proposal row must be traceable backward — Diff (Proposal ID) → Proposals (Delta Finding) → Delta Findings (Finding ID) → Assumption Table (Assumption root). Every chain hop must be filled. Schema compliance alone is insufficient — the chain must be walkable.

Do not omit any ★ column.

---

### Step 1a — Role: Stated-Field Extractor

**Adopt this role**: Extract only what strategy.md wrote explicitly. Do not interpret, infer, or supplement.

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

**Adopt this role**: You are an assumption archaeologist. Find what strategy.md took for granted without writing — the implied worldview, the unstated preconditions, the beliefs the author would defend if challenged but never put in the document. These are the highest-value delta candidates.

Systematic scan — cover each dimension. Do not skip dimensions:
- (a) Implied audience knowledge level
- (b) Namespace priority ordering assumed without justification
- (c) Signal sufficiency threshold — what "enough signals" means here
- (d) Timeline or sequencing feasibility
- (e) Definition of "done" for this topic
- (f) Any additional dimension this strategy reveals

Per schema (Assumption Table) — all five columns are mandatory. Do not omit any column.

Column rules:
- **"Contradicted by a signal?"**: Write `[pending]` now. Filled in Step 2b.
- **"Why this matters for delta detection"**: Fill now. If a signal contradicts this, which skill priorities or namespace ordering would change?
- **"Delta candidate?"**: Fill now. `yes` if contradicting would change strategy direction; `no` if not. After Step 3, update `yes` rows to `yes — F-NN`.

| Assumption ID | What strategy.md assumed without writing | Contradicted by a signal? | Why this matters for delta detection | Delta candidate? |
|--------------|------------------------------------------|--------------------------|-------------------------------------|-----------------|
| A-01 | [most important — highest likelihood of signal contradiction] | [pending] | [specific failure mode: which priorities would shift?] | yes / no |
| A-02 | [second assumption, if any] | [pending] | | yes / no |

Write at least one row. Null case: A-00 "No unstated assumptions found after systematic scan."

---

### Step 2a — Role: Signal Analyst — Read phase

**Adopt this role**: Read every artifact against two reference points: (a) stated fields from Step 1a, and (b) assumptions from Step 1b. Map each signal to its reference point.

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals found** — reproduce the following verbatim and stop. Do not omit this output:

> No signals found — strategy.md remains current. Run signal-gathering skills before attempting revision.

Per schema (Signal Inventory) — the following columns are mandatory. Do not omit any column:

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? | Assumption link (A-NN / "stated field" / "none") |
|----|------|-----------|-------|------|--------------------------|--------------------------|--------------------------------------------------|
| S-01 | | | | | | Yes / No / Partial | |

---

### Step 2b — Role: Assumption Archaeologist — Back-fill phase

**Return to this role**: Adjudicate every assumption from Step 1b against the full signal set.

For each A-NN row, replace `[pending]` with a signal-grounded verdict — exactly one per row. Do not leave any row as `[pending]`:

- **Contradicted — S-NN**: A signal directly challenges this assumption. Cite the signal ID. Write one sentence on the contradiction.
- **Supported — S-NN**: A signal confirms this assumption. Cite the signal ID.
- **No signal coverage**: No signal in the current set speaks to this assumption.

Reproduce the full updated Assumption Table (all 5 columns). Every row must have a verdict.

After completing Step 3, return here and update "Delta candidate?" — change `yes` to `yes — F-NN` for rows where a finding was generated.

---

### Step 3 — Role: Delta Identifier

**Adopt this role**: Name the gap between strategy beliefs and signal evidence.

**Stop. Before building the findings table, produce both outputs:**

1. **Anti-pattern label**: Name the anti-pattern you are guarding against. Write the label.
2. **Delta definition**: Delta IS: [gap between belief and signal]. Delta IS NOT: [inventory of signal existence].

Per schema (Delta Findings) — the following columns are mandatory. Do not omit any column:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root (A-NN / "stated field") |
|-----------|-----------------|----------------|-----------------|----------------------------------------|
| F-01 | [from Step 1a stated fields or Step 1b assumptions marked Contradicted] | | S-XX | |

After completing findings, return to Step 2b and update all `yes` entries in "Delta candidate?" with actual F-NN IDs.

**Null case** — reproduce verbatim and skip to Step 5:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root |
|-----------|-----------------|----------------|-----------------|-----------------|
| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |

---

### Step 4 — Role: Coverage Auditor

**Adopt this role**: Assess all 9 namespaces by name for stage-relative completeness — not raw count.

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

**Adopt this role**: Find pairs of artifacts pointing in opposite directions on the same dimension.

Per schema (Conflict Audit) — the following columns are mandatory. Do not omit any column:

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

**Null case** — reproduce verbatim. Do not omit this table:

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

---

### Step 6 — Role: Proposal Architect

**Adopt this role**: Translate each finding into a typed, defensible proposal. Every proposal must answer three questions: "What changes?", "What is the reversibility of deferral?", and "What fails to improve if we defer?"

**Stop. Before building the proposals table, write the following statement verbatim:**

> "Proposals schema committed: Proposal ID ★, Type ★, Change ★, Delta Finding ★ (full 'Strategy assumed [X] / Signal revealed [Y]' text from Step 3 with exact Finding ID), Evidence ★, If unchanged ★ (specific degradation — a row that writes a synonym of the delta finding here is a preference, not a decision), Reversibility ★ (Reversible at same cost / Gets harder / Becomes impossible), Confidence ★. All three types present. Empty types use null rows. Traceability: each Proposal ID traces to a Finding ID via Delta Finding, and from there to an Assumption root."

Per schema (Proposals) — the following columns are mandatory. Do not omit any column:

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged [a row that cannot name a specific degradation is a preference, not a decision] | Reversibility | Confidence |
|------------|------|--------|--------------|-------------------|---------------------------------------------------------------------------------------------|--------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [which artifact won't be gathered / which gap compounds / which decision window closes] | Gets harder | High |

**Reversibility values** (exactly one per content row):
- **Reversible at same cost**: can defer without increasing effort to close the gap later
- **Gets harder**: gap compounds; closing later costs more effort or more signals
- **Becomes impossible**: window closes; deferral makes the gap permanent

Null rows (reproduce verbatim for each empty type):

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Reversibility | Confidence |
|------------|------|--------|--------------|-------------------|-------------|--------------|------------|
| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 7 — Role: Diff Author

**Adopt this role**: Show the exact before/after for every confirmed proposal. Every Proposal ID is the entry point into the full traceability chain: Proposal ID → Delta Finding → Assumption root.

**Stop. Before building the diff table, write the following statement verbatim:**

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★ (inline per row as [file.md — ≤10 word finding] — no separate evidence section), Proposal ★ (Proposal ID from Step 6 — entry point into Proposal → Delta Finding → Assumption root chain)."

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

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals. Preserve existing structure; update only sections affected by confirmed changes.

---

## Criterion Coverage Matrix (v7 rubric, C-01–C-31)

C-01 through C-27: all mechanisms carried forward from R7 V-05. New R8 discriminators in bold.

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
| C-13 Inline evidence in diff | Step 7 Evidence col | Step 7 Evidence col (committed at checkpoint) | Step 7 Evidence col (committed at checkpoint) | Step 7 (committed at checkpoint) | Step 7 (committed at checkpoint) |
| C-14 Anti-inventory warning | Step 3 stop+name | Step 3 stop+name+contrast | Step 3 stop+name | Step 3 stop+name+contrast | Step 3 stop+name+contrast |
| C-15 All 9 namespaces named | Step 4 table | Step 4 table | Step 4 table | Step 4 table | Step 4 table |
| C-16 Two-level traceability | Step 6 Delta Finding + Evidence | Step 6 Delta Finding + Evidence (committed at checkpoint) | Step 6 Delta Finding + Evidence | Step 6 Delta Finding + Evidence + chain obligation | Step 6 Delta Finding + Evidence + chain obligation |
| C-17 Explicit no-conflicts | Step 5 null row verbatim | Step 5 null row verbatim | Step 5 null row verbatim | Step 5 null row verbatim | Step 5 null row verbatim |
| C-18 Structured delta format | Step 3 table | Step 3 table | Step 3 table | Step 3 table | Step 3 table |
| C-19 Diff Proposal ID col | Step 7 Proposal col | Step 7 Proposal col (committed at checkpoint) | Step 7 Proposal col (committed at checkpoint) | Step 7 (committed at checkpoint) | Step 7 (committed at checkpoint) |
| C-20 Delta Finding col | Step 6 mandatory + null rows | Step 6 mandatory + null rows (committed at checkpoint) | Step 6 mandatory + null rows | Step 6 (committed at checkpoint) | Step 6 (committed at checkpoint) |
| C-21 Column-completeness declaration | PASS: every table | PASS: upfront ★ schema + per-table | PASS: every table | PASS: upfront ★ schema + per-table | PASS: upfront ★ schema + per-table |
| C-22 Active anti-pattern checkpoint | PASS: Step 3 stop+name | PASS: Step 3 stop+name+contrast + Step 6 checkpoint | PASS: Step 3 stop+name | PASS: Step 3 stop+name+contrast + Step 6 checkpoint | PASS: Step 3 stop+name+contrast + Steps 6+7 |
| C-23 Pre-reproduced null templates | PASS: all null outcomes | PASS: all null outcomes | PASS: all null outcomes | PASS: all null outcomes | PASS: all null outcomes |
| C-24 Unstated assumption extraction | PASS: Step 1b scan (a-e), 5-col table, systematic | PASS: Step 1 unstated assumptions, "Why this matters" col | PASS: Step 1b Archaeologist role, scan (a-e) | PASS: Step 1b Archaeologist role, scan (a-e), full schema | PASS: Step 1b Archaeologist role, scan (a-f), full schema |
| C-25 Inertia cost column | PASS: "If unchanged" col in Step 6 | PASS: "If unchanged" col + adjacent disqualification rule | PASS: "If unchanged" col in Step 6 | PASS: "If unchanged" col + committed at checkpoint | PASS: "If unchanged" + Reversibility cols + adjacent disqualification rule + committed at checkpoint |
| C-26 Schema-first priming | PARTIAL: per-table only, no upfront consolidated schema | PASS: upfront ★ schema block before Step 1 | PARTIAL: per-table only | PASS: upfront ★ schema block including Assumption Table | PASS: upfront ★ schema block including Assumption Table |
| C-27 Cascade schema-commitment checkpoints | PARTIAL: Step 3 anti-pattern + Step 7 diff checkpoint only | PASS: Steps 3+6+7 checkpoints | PASS: Steps 3+7 checkpoints | PASS: Steps 3+6+7 checkpoints | PASS: Steps 3+6+7 (Step 6 carries triple weight: schema+null-rows+traceability) |
| **C-28 Named role + scan dimensions** | **PARTIAL: scan (a-e) present, no named role** | **PARTIAL: no named role, no scan dimensions** | **PASS: Assumption Archaeologist + scan (a-e) in Step 1b** | **PASS: Assumption Archaeologist + scan (a-e) + declared in upfront schema** | **PASS: Assumption Archaeologist + scan (a-f) + declared in upfront schema** |
| **C-29 Back-fill column** | **PASS: "Contradicted?" declared at extraction time + explicit back-fill instruction after Step 2** | **PASS: "Contradicted?" in upfront schema + Step 1 + back-fill instruction after Step 2** | **PASS: "Contradicted?" col + named Step 2b lifecycle phase with verdict-per-row obligation** | **PASS: "Contradicted?" in upfront schema + named Step 2b back-fill phase with verdict-per-row obligation** | **PASS: "Contradicted?" in upfront schema + named Step 2b back-fill phase with verdict-per-row obligation** |
| **C-30 Forward-reasoning columns** | **PASS: "Why this matters for delta detection" col + "Delta candidate?" col — both at Step 1b, updated in Step 3** | **PARTIAL: "Why this matters" col in upfront schema and Step 1 — no "Delta candidate?" designation col** | **FAIL: no delta-relevance col, no delta-candidate col** | **PASS: "Why this matters" + "Delta candidate?" in upfront schema and Step 1b, updated in Step 3** | **PASS: "Why this matters" + "Delta candidate?" in upfront schema and Step 1b, updated after Step 3** |
| **C-31 Decision-gate framing** | **FAIL: no adjacent disqualification rule** | **PASS: disqualification rule in column header: "a row that cannot name a specific degradation here is a preference, not a decision"** | **FAIL: no adjacent disqualification rule** | **PARTIAL: Step 6 checkpoint names "specific degradation — not a synonym" but no column-header rule** | **PASS: disqualification rule in column header + Step 6 checkpoint** |

---

## R8 Discriminator Analysis

| Variation | C-28 mechanism | C-29 mechanism | C-30 mechanism | C-31 mechanism | Structural bet |
|-----------|----------------|----------------|----------------|----------------|----------------|
| V-01 | Scan (a-e) in Step 1b — no named role (C-28 partial) | "Contradicted?" declared at extraction + back-fill instruction post-Step 2 — C-29 pass | Full 5-col table: "Why this matters" + "Delta candidate?" at Step 1b — first R8 variation to achieve C-30 | No adjacent disqualification rule — C-31 fail | Assumption table schema as structural inevitability: five columns at extraction make C-29/C-30 unavoidable |
| V-02 | No named role, no scan dimensions — C-28 partial | "Contradicted?" in upfront schema + back-fill instruction — C-29 pass | "Why this matters" col in upfront schema and Step 1 — no "Delta candidate?" designation — C-30 partial | Disqualification rule in column header: "a row that cannot name a specific degradation here is a preference, not a decision" — first variation across all rounds to achieve C-31 via adjacency | Adjacency as structural gate: disqualification sentence in column header, not preamble |
| V-03 | Assumption Archaeologist + scan (a-e) — C-28 pass | Named Step 2b lifecycle phase with verdict-per-row obligation — strongest C-29 mechanism in any round | No delta-relevance or delta-candidate columns — C-30 fail | No adjacent disqualification rule — C-31 fail | Lifecycle phase as cognitive act: named Step 2b produces richer adjudication than column annotation |
| V-04 | Assumption Archaeologist + scan (a-e) + upfront schema — C-28 pass | Upfront schema + named Step 2b back-fill phase — C-29 pass | Full 5-col table in upfront schema + Step 1b, updated post-Step 3 — C-30 pass | No column-header rule — C-31 partial | First variation to achieve C-28+C-29+C-30 simultaneously; C-31 excluded to isolate the combination |
| V-05 | Assumption Archaeologist + scan (a-f) + upfront schema — C-28 pass | Upfront schema + named Step 2b with verdict-per-row obligation — C-29 pass | Full 5-col table in upfront schema + Step 1b, updated after Step 3 — C-30 pass | Disqualification rule in column header + Step 6 checkpoint — C-31 pass | Full stack: all four new criteria; ceiling variation for R8; most likely source of R9 excellence signals |

**Key structural distinctions:**

- **V-01 C-30 first achievement**: First variation across all eight rounds to declare "Why this matters for delta detection" AND "Delta candidate?" simultaneously at extraction time. Tests whether upfront column declaration alone achieves C-30 without a named role — the result isolates format from role.
- **V-02 C-31 first achievement**: First variation to place the disqualification rule in the column header rather than the step preamble. Tests whether adjacency alone converts the inertia column from format cell to gate — the result isolates adjacency from register.
- **V-03 C-29 strongest mechanism**: Named Step 2b with verdict-per-row obligation is the most explicit C-29 mechanism across all rounds. Tests whether a lifecycle phase with a named role return produces richer back-fill than a column annotation or post-step instruction.
- **V-04 vs V-05**: V-04 achieves C-28+C-29+C-30 and deliberately omits C-31 — scoring gap between V-04 and V-05 isolates the value of the C-31 adjacency mechanism. If V-04 and V-05 score identically on C-30, C-31 was not load-bearing for delta quality; if V-05 produces distinctly more defensible proposals, C-31 adjacency affects proposal reasoning.
- **Where V-01 and V-02 are partial on C-28**: Both are intentionally single-axis isolations — V-01 tests format without role; V-02 tests adjacency without role or scan dimensions. These partial-C-28 variations reveal whether C-29/C-30/C-31 can be achieved independently of the named role.
