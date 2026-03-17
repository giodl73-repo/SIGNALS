# topic-plan — Round 6 Variations (v6 rubric)

**Skill**: `topic:plan`
**Rubric**: v6 (C-01–C-27, 185 pts total)
**Date**: 2026-03-15

---

## Round 6 Design Notes

Round 5 achieved full coverage of C-21, C-22, C-23 (enforcement layer) and surfaced the four new v6 criteria from excellence signals. The v6 rubric splits in two directions from the v5 enforcement foundation:

**Depth layer (C-24, C-25)** — the gap between "the output is structured correctly" and "the output carries genuine causal reasoning":
- C-24 forces the model to extract what strategy.md never wrote (unstated assumptions as delta candidates)
- C-25 forces the model to reason about the cost of staying put, not just the direction of change

**Enforcement layer (C-26, C-27)** — extending v5's constraint-explicitness work:
- C-26 moves the schema contract before execution begins (priming, not per-table reinforcement)
- C-27 cascades the auditable-checkpoint mechanism from one point (delta) to three (delta, proposals, diff)

**What Round 5 already surfaced for free:**
- R5 V-05 Step 1 already had "What it assumed without naming" → C-24 mechanism exists but not as a mandatory substep
- R5 V-05 Step 6 already had "If unchanged" → C-25 mechanism exists but without inertia framing in the preamble
- R5 V-04 already had an upfront ★ schema block → C-26 mechanism exists but signal inventory lacked "assumption link" column
- R5 V-02 already had 3 schema commitments → C-27 mechanism exists but proposals checkpoint phrasing wasn't full schema commitment

**Round 6 target: make each mechanism structurally unavoidable rather than instructed-and-possibly-skipped.**

**Variation axes:**

| Variation | Axis | Type | Primary v6 target |
|-----------|------|------|-------------------|
| V-01 | Lifecycle emphasis — dedicated assumption-mining substep in Step 1 | Single | C-24 |
| V-02 | Inertia framing — consequence reasoning as organizing principle throughout | Single | C-25 |
| V-03 | Output format — consolidated schema-priming block before all execution | Single | C-26 |
| V-04 | Output format + Phrasing register — schema-first + cascade commitment checkpoints | Combination | C-26 + C-27 |
| V-05 | Lifecycle + Inertia + Output format + Phrasing — full depth and enforcement stack | Combination | C-24 + C-25 + C-26 + C-27 |

---

## V-01 — Assumption-Mining Substep

**Axis**: Lifecycle emphasis — dedicated named substep for unstated assumption extraction within the strategy read phase
**Hypothesis**: R5 V-05 added "What it assumed without naming" as a row in the Step 1 strategy table — a single row embedded among five stated-field rows. C-24 requires a stronger mechanism: the unstated assumption extraction must be a *named act*, not a table row the model can fill mechanically with one word. Separating it into a distinct labeled substep (Step 1b) signals that this is a different kind of reading: not extracting what strategy.md wrote but reconstructing what it took for granted. The "Why this is a delta candidate" column forces the model to evaluate each assumption's relevance before proceeding to signals — making the connection from assumption to delta structurally unavoidable rather than available in the output but skipped under context pressure. The assumption inventory also becomes a reference target for the signal inventory (Step 2 "Confirms or challenges which assumption?" column), creating a traceability chain from assumption → signal → finding that C-24 relies on but prior variations left implicit.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it was written. Present proposals, wait for confirmation, then write. Do not auto-apply changes.

---

### Step 1a — Read strategy.md: stated fields

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

### Step 1b — Mine unstated assumptions

Every strategy assumes things it does not write. These are the highest-value delta candidates — a signal can contradict what was assumed, not only what was stated. A strategy that assumes "the audience is already familiar with the namespace model" cannot be revised for that gap without first surfacing the assumption.

**The following columns are mandatory. Do not omit any column.**

| Assumption ID | What it assumed without naming | Why this is a delta candidate |
|--------------|-------------------------------|-------------------------------|
| A-01 | [most important unstated assumption for delta detection] | |
| A-02 | [second unstated assumption, if any] | |

Write at least one row. Common unstated assumptions to look for: namespace priority ordering, audience maturity level, signal sufficiency threshold, timeline or sequencing feasibility, scope of "done." If the strategy makes no assumptions beyond its stated content (rare), write "A-00 — No unstated assumptions identified."

---

### Step 2 — Read and inventory signal artifacts

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals** — if no files found, reproduce the following verbatim and stop. Do not omit this output:

> No signals found — strategy.md does not need revision at this time.

**The following columns are mandatory. Do not omit any column.**

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Confirms or challenges which assumption? |
|----|------|-----------|-------|------|--------------------------|------------------------------------------|
| S-01 | | | | | | Confirms: [A-NN] / Challenges: [A-NN] / No assumption link |

The final column connects each signal to the assumption inventory from Step 1b, setting up the "Strategy assumed [X]" anchor for Step 3.

---

### Step 3 — Identify the delta (not an inventory)

Stop here. Name the anti-pattern you are guarding against at this step. Then proceed to the findings table.

**The following columns are mandatory. Do not omit any column.**

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) |
|-----------|-----------------|----------------|-----------------|
| F-01 | [from Step 1a stated fields or Step 1b unstated assumptions] | [from Step 2 signals] | S-XX |

Findings may be rooted in stated fields (C-01 pass) or in unstated assumptions surfaced in Step 1b. Both are valid delta sources — a finding rooted in an unstated assumption should reference the Assumption ID.

**Null case — all signals confirm** — reproduce the following row verbatim and skip to Step 5. Do not omit this row:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) |
|-----------|-----------------|----------------|-----------------|
| F-00 | Strategy confirmed | No gaps detected | All signals |

---

### Step 4 — Namespace coverage audit

Assess all 9 namespaces by name. "Stage-relative" = appropriate for the topic's current stage, not a raw count.

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

Look for signals pointing in opposite directions.

**The following columns are mandatory. Do not omit any column.**

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

**Mandatory null case** — if no conflicts found, reproduce the following row verbatim. Do not omit this table:

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

---

### Step 6 — Proposals table

**The following columns are mandatory. Do not omit any column.**

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | Confidence |
|------------|------|--------|--------------|-------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | High |

All three types (ADD, REMOVE, REPRIORITIZE) must appear. For types with no proposals, reproduce the applicable row(s) verbatim. Do not omit any type row:

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | Confidence |
|------------|------|--------|--------------|-------------------|------------|
| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | — |

Delta Finding must reproduce the full "Strategy assumed [X] / Signal revealed [Y]" text from Step 3 using the exact Finding ID.

---

### Step 7 — Before/after diff

**The following columns are mandatory. Do not omit any column.**

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current strategy text] | [proposed text] | [file.md — ≤10 word finding] | ADD-1 |

- **Evidence**: `[file.md — finding in ≤10 words]` inline per row
- **Proposal**: Proposal ID from Step 6 — navigational anchor back to the full Delta Finding chain

---

### Step 8 — Confirmation gate

Reply **YES** to apply all proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 9 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals. Preserve existing structure; update only sections affected by confirmed changes.

---

## V-02 — Consequence-First Framing

**Axis**: Inertia framing — consequence reasoning as the organizing principle from the opening preamble through the proposals table
**Hypothesis**: R5 V-05 introduced "If unchanged" as a proposals column with brief guidance ("name what gap persists, worsens, or becomes harder to close"). C-25 requires more: the column must force *consequence reasoning* (what the signals say about what happens next if ignored) not just *directional labeling* (what the signal said). The mechanism for achieving this is framing — if the opening of the prompt establishes that every proposal is a cost-of-inaction decision, the model will approach the "If unchanged" column as a conclusion to be reasoned toward rather than a field to fill. The proposals step also adds an explicit guidance sentence distinguishing consequence reasoning from observation ("not 'nothing changes' but the specific degradation — what gets worse, harder, or impossible"), which prevents the column from being filled with synonyms of the delta finding rather than a forward causal claim.

---

You are executing `topic:plan` for the topic `{topic}`.

Every proposed change must answer the question: **what happens if we don't make this change?** A proposal without a named cost of inaction is a preference, not a decision. This prompt requires consequence reasoning at the proposals step — every change must name what gap persists, worsens, or becomes impossible to close if it is deferred. Present proposals, wait for confirmation, then write. Do not auto-apply changes.

---

### Step 1 — Read strategy.md

Read `simulations/{topic}/strategy.md`.

**The following columns are mandatory. Do not omit any column.**

| Field | Value |
|-------|-------|
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Stated rationale | |
| Acknowledged gaps | |
| What it assumed without naming | [at least one item — most important for delta detection] |

---

### Step 2 — Read and inventory signal artifacts

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals** — if no files found, reproduce the following verbatim and stop. Do not omit this output:

> No signals found — strategy.md does not need revision at this time.

**The following columns are mandatory. Do not omit any column.**

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? |
|----|------|-----------|-------|------|--------------------------|--------------------------|
| S-01 | | | | | | Yes / No / Partial |

---

### Step 3 — Identify the delta (not an inventory)

Stop here. Name the anti-pattern you are guarding against at this step. Then proceed to the findings table.

**The following columns are mandatory. Do not omit any column.**

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) |
|-----------|-----------------|----------------|-----------------|
| F-01 | | | |

**Null case — all signals confirm** — reproduce the following row verbatim and skip to Step 5. Do not omit this row:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) |
|-----------|-----------------|----------------|-----------------|
| F-00 | Strategy confirmed | No gaps detected | All signals |

---

### Step 4 — Namespace coverage audit

Assess all 9 namespaces by name. "Stage-relative" = appropriate for this stage, not a raw count.

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

Look for signals pointing in opposite directions.

**The following columns are mandatory. Do not omit any column.**

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

**Mandatory null case** — if no conflicts found, reproduce the following row verbatim. Do not omit this table:

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

---

### Step 6 — Proposals with inertia cost

**The following columns are mandatory. Do not omit any column.**

The **If unchanged** column is not optional and cannot be filled with a synonym of the delta finding. It must name a specific degradation — what worsens, what becomes harder to reverse, or what opportunity closes — if this proposal is deferred. "Nothing changes" is not a valid entry: if nothing changes by deferring, the proposal should not be made.

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Confidence |
|------------|------|--------|--------------|-------------------|-------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [specific degradation if deferred] | High |

All three types (ADD, REMOVE, REPRIORITIZE) must appear. For types with no proposals, reproduce the applicable row(s) verbatim. Do not omit any type row:

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Confidence |
|------------|------|--------|--------------|-------------------|-------------|------------|
| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |

Column rules:
- **Delta Finding**: full "Strategy assumed [X] / Signal revealed [Y]" text from Step 3 with exact Finding ID
- **If unchanged**: a forward causal claim — what degrades, compounds, or closes if the proposal is not taken — not a restatement of the delta finding

---

### Step 7 — Before/after diff

**The following columns are mandatory. Do not omit any column.**

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current strategy text] | [proposed text] | [file.md — ≤10 word finding] | ADD-1 |

- **Evidence**: `[file.md — finding in ≤10 words]` inline per row
- **Proposal**: Proposal ID from Step 6 — navigational anchor to the full Delta Finding and inertia chain

---

### Step 8 — Confirmation gate

Reply **YES** to apply all proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 9 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals. Preserve existing structure; update only sections affected by confirmed changes.

---

## V-03 — Schema Priming Block

**Axis**: Output format — consolidated schema contract for all tables declared before any file reading begins
**Hypothesis**: R5 V-04 placed a ★-annotated schema block before Step 1 and achieved a C-26-like structure, but the schema did not include the strategy read table, the null templates were distributed across steps (not pre-reproduced in the contract), and the signal inventory lacked a column linking each signal to its assumption. C-26 requires the *complete* output schema for all tables, with mandatory-column designation, declared before execution. The distinction from C-21 (adjacent declarations within steps) is placement: C-26's contract is committed to before any file is touched. When the model reads a strategy.md and encounters unexpected content, the contract is already in memory — it cannot be locally rationalized away at each step because it was declared globally before any content was seen. A second structural bet: consolidating all null templates into the contract block eliminates the requirement that the model match each null-template instruction to its context step under pressure. The model has a single pre-read reference for all null outcomes before it starts.

---

You are executing `topic:plan` for the topic `{topic}`.

**Read the OUTPUT CONTRACT below before reading any files.** The contract defines every table you will produce and pre-reproduces every null template. Columns marked ★ are mandatory — do not omit any ★ column in any table. Do not auto-apply changes.

---

## OUTPUT CONTRACT — Read before Step 1

**Strategy Read** (Step 1)
| ★ Field | ★ Value |

Mandatory fields: Declared stage, Namespaces covered, Skills planned, Stated rationale, Acknowledged gaps, What it assumed without naming.

**Signal Inventory** (Step 2)
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? |

**Delta Findings** (Step 3)
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) |

**Namespace Audit** (Step 4)
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |
All 9 namespaces must appear: scout, draft, review, flow, trace, prove, listen, program, topic.

**Conflict Audit** (Step 5)
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals** (Step 6)
| ★ Proposal ID | ★ Type | ★ Change | ★ Delta Finding | ★ Evidence | ★ Confidence |
All three types (ADD, REMOVE, REPRIORITIZE) must appear.

**Diff** (Step 7)
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |
Evidence: inline `[file.md — ≤10 word finding]` per row. Proposal: Proposal ID from Step 6.

A table that omits any ★ column fails schema validation regardless of content in other columns.

---

**Null templates** — reproduce verbatim when the condition applies. Do not paraphrase.

**No-signals** (use when Step 2 finds no files):
> No signals found — strategy.md does not need revision at this time.

**Delta null** (use when all signals confirm in Step 3):

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) |
|-----------|-----------------|----------------|-----------------|
| F-00 | Strategy confirmed | No gaps detected | All signals |

**Conflict null** (use when Step 5 finds no conflicts):

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

**Proposal null rows** (reproduce for each type with no proposals):

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | Confidence |
|------------|------|--------|--------------|-------------------|------------|
| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | — |

---

### Step 1 — Read strategy.md

Read `simulations/{topic}/strategy.md`. Extract per schema (Strategy Read).

**The following columns are mandatory. Do not omit any column.**

| Field | Value |
|-------|-------|
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Stated rationale | |
| Acknowledged gaps | |
| What it assumed without naming | [at least one item — most important for delta detection] |

---

### Step 2 — Read and inventory signal artifacts

Glob `simulations/{topic}/` recursively. Read every file found.

If no files found: reproduce the no-signals null template from the OUTPUT CONTRACT and stop.

Per schema (Signal Inventory):

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? |
|----|------|-----------|-------|------|--------------------------|--------------------------|
| S-01 | | | | | | Yes / No / Partial |

---

### Step 3 — Identify the delta (not an inventory)

Stop here. Name the anti-pattern you are guarding against at this step. Then proceed to the findings table.

Per schema (Delta Findings):

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) |
|-----------|-----------------|----------------|-----------------|
| F-01 | | | |

If all signals confirm: reproduce the delta null template from the OUTPUT CONTRACT and skip to Step 5. Do not omit this row.

---

### Step 4 — Namespace coverage audit

Per schema (Namespace Audit). All 9 by name:

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

Per schema (Conflict Audit). If no conflicts: reproduce the conflict null template from the OUTPUT CONTRACT. Do not omit this table.

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

---

### Step 6 — Proposals table

Per schema (Proposals). All three types must appear. For empty types: reproduce the applicable proposal null rows from the OUTPUT CONTRACT. Do not omit any type row.

**The following columns are mandatory. Do not omit any column.**

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | Confidence |
|------------|------|--------|--------------|-------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | High |

Delta Finding must reproduce the full "Strategy assumed [X] / Signal revealed [Y]" text from Step 3 using the exact Finding ID.

---

### Step 7 — Before/after diff

Per schema (Diff). Evidence inline per row. Proposal = Proposal ID from Step 6.

**The following columns are mandatory. Do not omit any column.**

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current text] | [proposed text] | [file.md — ≤10 word finding] | ADD-1 |

---

### Step 8 — Confirmation gate

Reply **YES** to apply all proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 9 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals.

---

## V-04 — Schema-First + Cascade Commitments

**Axes**: Output format + Phrasing register — complete schema contract before execution; model-produced schema-commitment statements at three auditable checkpoints
**Hypothesis**: (1) C-26 requires the complete output schema declared *before* any file reading begins. The priming effect is distinct from C-21's per-table adjacency: adjacency reinforces the contract when each step is reached; priming commits to the contract before any content is encountered. A model that has committed to all column names before reading strategy.md cannot rationalize a column omission as "this file didn't seem to need that" because the contract was fixed before the file was read. (2) C-27 requires the model to *produce* schema-commitment statements immediately before the proposals table AND immediately before the diff table, creating three independent verifiable checkpoints across the output (delta anti-pattern + proposals schema + diff schema). Each commitment is auditable without reading any other section — a reviewer can check proposals compliance by looking only at the proposals checkpoint statement, independently of whether the upfront schema was read. This three-point audit structure is the mechanism that distinguishes C-27 from C-26 (which is about pre-reading the contract) and from C-22 (which is one checkpoint at delta only). The cascade transforms the contract from a reference into a trail of evidence.

---

You are executing `topic:plan` for the topic `{topic}`.

**Before reading any files, review the complete output schema below.** Every table you produce must conform to this schema. Columns marked ★ are mandatory. You will produce schema-commitment statements at three checkpoints — before the delta findings table, before the proposals table, and before the diff table. Each statement is verifiable output: a reviewer can confirm schema compliance at any checkpoint without reading the others. Do not auto-apply changes.

---

## Output Schema — Read before Step 1

**Signal Inventory**
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? |

**Delta Findings**
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) |

**Namespace Audit**
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |

**Conflict Audit**
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals**
| ★ Proposal ID | ★ Type | ★ Change | ★ Delta Finding | ★ Evidence | ★ Confidence |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

Do not omit any ★ column. If a column is absent from your output, that table fails schema validation regardless of content in other columns.

---

### Step 1 — Read strategy.md

Read `simulations/{topic}/strategy.md`. Extract:

**The following columns are mandatory. Do not omit any column.**

| Field | Value |
|-------|-------|
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Stated rationale | |
| Acknowledged gaps | |
| What it assumed without naming | [at least one item — most important for delta detection] |

---

### Step 2 — Read and inventory signal artifacts

Glob `simulations/{topic}/` recursively. Read every file found.

If no files found: output "No signals found — strategy.md requires no revision." and stop.

Per schema (Signal Inventory):

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? |
|----|------|-----------|-------|------|--------------------------|--------------------------|
| S-01 | | | | | | Yes / No / Partial |

---

### Step 3 — Delta checkpoint: produce before building table

**Stop. Before building the delta findings table, produce both outputs:**

1. **Anti-pattern label**: Name the anti-pattern you are guarding against at this step. Write the label — do not skip.
2. **Schema commitment**: Write verbatim: "Delta Findings schema: Finding ID ★, Strategy assumed ★, Signal revealed ★, Source signal(s) ★."

Then build per schema (Delta Findings):

**The following columns are mandatory. Do not omit any column.**

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) |
|-----------|-----------------|----------------|-----------------|
| F-01 | | | |

Null case: if all signals confirm, reproduce verbatim and skip to Step 5. Do not omit this row:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) |
|-----------|-----------------|----------------|-----------------|
| F-00 | Strategy confirmed | No gaps detected | All signals |

---

### Step 4 — Namespace coverage audit

Per schema (Namespace Audit). All 9 by name:

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

Per schema (Conflict Audit). Null case — reproduce verbatim. Do not omit this table:

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

---

### Step 6 — Proposals checkpoint: produce before building table

**Stop. Before building the proposals table, write the following statement verbatim:**

> "Proposals schema confirmed: Proposal ID ★, Type ★, Change ★, Delta Finding ★ (full 'Strategy assumed [X] / Signal revealed [Y]' text from Step 3 with exact Finding ID), Evidence ★, Confidence ★. All three types present. Empty types will use null rows."

Write that statement, then build per schema (Proposals):

**The following columns are mandatory. Do not omit any column.**

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | Confidence |
|------------|------|--------|--------------|-------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | High |

For empty types, reproduce verbatim. Do not omit any type row:

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | Confidence |
|------------|------|--------|--------------|-------------------|------------|
| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | — |

---

### Step 7 — Diff checkpoint: produce before building table

**Stop. Before building the diff table, write the following statement verbatim:**

> "Diff schema confirmed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★ (inline per row as [file.md — ≤10 word finding], no separate evidence section), Proposal ★ (Proposal ID from Step 6)."

Write that statement, then build per schema (Diff):

**The following columns are mandatory. Do not omit any column.**

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current text] | [proposed text] | [file.md — ≤10 word finding] | ADD-1 |

---

### Step 8 — Confirmation gate

Reply **YES** to apply all proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 9 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals.

---

## V-05 — Full Depth and Enforcement Stack

**Axes**: Lifecycle emphasis + Inertia framing + Output format + Phrasing register — all four v6 criteria targeted simultaneously
**Hypothesis**: C-24 and C-25 operate on *what the model reasons about*; C-26 and C-27 operate on *when and how often the structural contract is activated*. These axes are orthogonal — a prompt can satisfy C-26/C-27 while producing shallow Delta Finding entries (schema-compliant but mechanically filled), and can satisfy C-24/C-25 while lacking the upfront contract and checkpoint cascade. V-05 stacks all four mechanisms because the depth criteria depend on the enforcement criteria to survive context pressure: the "What it assumed without naming" substep produces high-value delta candidates, but those candidates become load-bearing only if the proposals table's "If unchanged" column is structurally enforced at the point where context pressure is highest (Step 6). Similarly, the cascade checkpoints (C-27) at proposals and diff include the "If unchanged" column in their verbatim schema-commitment statements — meaning the inertia column is named as a commitment before the table is built, not just instructed in the step guidance. The structural bet: surface deep reasoning (C-24/C-25) + make it unavoidable (C-26/C-27) is stronger than either depth or enforcement alone.

---

You are executing `topic:plan` for the topic `{topic}`.

**Read the OUTPUT CONTRACT below before reading any files.** This revision surfaces what the strategy assumed without naming, names the cost of inaction for every proposed change, and produces schema-commitment checkpoints at three auditable points. Do not auto-apply changes.

---

## OUTPUT CONTRACT — Read before Step 1

All tables you produce must conform to this schema. Columns marked ★ are mandatory — do not omit any ★ column.

**Strategy Read** (Step 1)
Mandatory fields: Declared stage ★, Core belief about the topic ★, Namespaces covered ★, Namespaces explicitly deferred ★, Skills planned ★, Risks acknowledged ★, What it assumed without naming ★.

**Signal Inventory** (Step 2)
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Confirms or challenges which assumption? |

**Delta Findings** (Step 3)
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) |

**Namespace Audit** (Step 4)
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |
All 9 namespaces: scout, draft, review, flow, trace, prove, listen, program, topic.

**Conflict Audit** (Step 5)
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals** (Step 6)
| ★ Proposal ID | ★ Type | ★ Change | ★ Delta Finding | ★ Evidence | ★ If unchanged | ★ Confidence |
"If unchanged" = forward causal claim: what degrades, compounds, or closes if the proposal is deferred.

**Diff** (Step 7)
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |
Evidence: inline `[file.md — ≤10 word finding]` per row. Proposal: Proposal ID from Step 6.

A table that omits any ★ column fails schema validation regardless of content in other columns.

---

**Null templates** — reproduce verbatim when the condition applies. Do not paraphrase.

**No-signals**:
> No signals found — strategy.md does not need revision at this time.

**Delta null**:
| F-00 | Strategy confirmed | No gaps detected | All signals |

**Conflict null**:
| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

**Proposal null rows** (reproduce for each empty type):
| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |

---

### Step 1 — Read strategy.md: stated fields + unstated assumptions

Read `simulations/{topic}/strategy.md`. Extract all commitments — both explicit and implicit. Complete both substeps before proceeding to signals.

**Step 1a — Stated fields**

**The following columns are mandatory. Do not omit any column.**

| Field | Value |
|-------|-------|
| Declared stage | |
| Core belief about the topic | |
| Namespaces covered | |
| Namespaces explicitly deferred | |
| Skills planned | |
| Risks acknowledged | |

**Step 1b — Unstated assumptions**

Every strategy assumes things it does not write. These are the highest-value delta candidates.

**The following columns are mandatory. Do not omit any column.**

| Assumption ID | What it assumed without naming | Why this is a delta candidate |
|--------------|-------------------------------|-------------------------------|
| A-01 | [most important — required] | |

Write at least one row. Common unstated assumptions: namespace priority ordering, audience maturity level, signal sufficiency threshold, timeline feasibility, what "done" means for this topic. If no unstated assumptions exist (rare), write "A-00 — No unstated assumptions identified."

---

### Step 2 — Read and inventory signal artifacts

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals** — if no files found, reproduce the no-signals null template from the OUTPUT CONTRACT and stop. Do not omit this output.

**The following columns are mandatory. Do not omit any column.**

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Confirms or challenges which assumption? |
|----|------|-----------|-------|------|--------------------------|------------------------------------------|
| S-01 | | | | | | Confirms: [A-NN] / Challenges: [A-NN] / No assumption link |

---

### Step 3 — Delta checkpoint: produce before building table

**Stop. Before building the delta findings table, produce both outputs:**

1. **Anti-pattern label**: Name the anti-pattern you are guarding against at this step. Write the label — do not skip.
2. **Schema commitment**: Write verbatim: "Delta Findings schema: Finding ID ★, Strategy assumed ★, Signal revealed ★, Source signal(s) ★."

Then build per schema (Delta Findings):

**The following columns are mandatory. Do not omit any column.**

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) |
|-----------|-----------------|----------------|-----------------|
| F-01 | [from Step 1a stated fields or Step 1b unstated assumptions] | [from Step 2 signals] | S-XX |

Findings rooted in Step 1b unstated assumptions should reference the Assumption ID (e.g., "A-01: assumed without naming: [X]").

**Null case — all signals confirm** — reproduce the delta null template from the OUTPUT CONTRACT and skip to Step 5. Do not omit this row.

---

### Step 4 — Namespace coverage audit

Per schema (Namespace Audit). All 9 by name. "Stage-relative" = appropriate for the topic's current stage, not a raw count.

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

Per schema (Conflict Audit).

**The following columns are mandatory. Do not omit any column.**

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

**Null case — no conflicts** — reproduce the conflict null template from the OUTPUT CONTRACT. Do not omit this table.

---

### Step 6 — Proposals checkpoint: produce before building table

**Stop. Before building the proposals table, write the following statement verbatim:**

> "Proposals schema confirmed: Proposal ID ★, Type ★, Change ★, Delta Finding ★ (full 'Strategy assumed [X] / Signal revealed [Y]' text from Step 3 with exact Finding ID), Evidence ★, If unchanged ★ (forward causal claim: what degrades or closes if deferred), Confidence ★. All three types present. Empty types will use null rows from the OUTPUT CONTRACT."

Write that statement, then build per schema (Proposals):

**The following columns are mandatory. Do not omit any column.**

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Confidence |
|------------|------|--------|--------------|-------------------|-------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [what degrades if deferred] | High |

For empty types, reproduce the applicable null rows from the OUTPUT CONTRACT verbatim. Do not omit any type row.

Column rules:
- **Delta Finding**: full "Strategy assumed [X] / Signal revealed [Y]" text from Step 3 with exact Finding ID
- **If unchanged**: a forward causal claim — what degrades, compounds, or becomes irreversible if this proposal is deferred. Not a restatement of the delta finding.

---

### Step 7 — Diff checkpoint: produce before building table

**Stop. Before building the diff table, write the following statement verbatim:**

> "Diff schema confirmed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★ (inline per row as [file.md — ≤10 word finding], no separate section), Proposal ★ (Proposal ID from Step 6 — links to full Delta Finding and inertia chain)."

Write that statement, then build per schema (Diff):

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

## Criterion Coverage Matrix

Coverage assessed against v6 rubric (C-01–C-27). C-01–C-23 are carried forward from Round 5 (all PASS; mechanisms unchanged unless noted). New criteria C-24/C-25/C-26/C-27 are the discriminators.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Read strategy | Step 1a | Step 1 | Step 1 | Step 1 | Step 1a |
| C-02 Read signals | Step 2 | Step 2 | Step 2 | Step 2 | Step 2 |
| C-03 Delta not inventory | Step 3 checkpoint | Step 3 checkpoint | Step 3 checkpoint | Step 3 checkpoint | Step 3 checkpoint |
| C-04 Typed proposals | Step 6 table | Step 6 table | Step 6 table | Step 6 table | Step 6 table |
| C-05 Confirm gate | Step 8 YES | Step 8 YES | Step 8 YES | Step 8 YES | Step 8 YES |
| C-06 Evidence per change | Step 6 Evidence col | Step 6 Evidence col | Step 6 Evidence col | Step 6 Evidence col | Step 6 Evidence col |
| C-07 Before/after diff | Step 7 | Step 7 | Step 7 | Step 7 | Step 7 |
| C-08 All three types | Step 6 null rows | Step 6 null rows | Step 6 null rows | Step 6 null rows | Step 6 null rows |
| C-09 Namespace gaps | Step 4 (9 by name) | Step 4 (9 by name) | Step 4 (9 by name) | Step 4 (9 by name) | Step 4 (9 by name) |
| C-10 Conflicting signals | Step 5 | Step 5 | Step 5 | Step 5 | Step 5 |
| C-11 Typed confirmation verb | Step 8 YES | Step 8 YES | Step 8 YES | Step 8 YES | Step 8 YES |
| C-12 Explicit no-change rows | Step 6 null rows verbatim | Step 6 null rows verbatim | Step 6 null rows verbatim | Step 6 null rows verbatim | Step 6 null rows verbatim |
| C-13 Inline evidence in diff | Step 7 Evidence col | Step 7 Evidence col | Step 7 Evidence col | Step 7 Evidence col (checkpoint confirms) | Step 7 Evidence col (checkpoint confirms) |
| C-14 Anti-inventory warning | Step 3 (stop + name) | Step 3 (stop + name) | Step 3 (stop + name) | Step 3 (stop + name) | Step 3 (stop + name) |
| C-15 All 9 namespaces named | Step 4 table | Step 4 table | Step 4 table (contract enumerates) | Step 4 table | Step 4 table (contract enumerates) |
| C-16 Two-level traceability | Step 6: Delta Finding + Evidence | Step 6: Delta Finding + Evidence | Step 6: Delta Finding + Evidence | Step 6: Delta Finding + Evidence | Step 6: Delta Finding + Evidence |
| C-17 Explicit no-conflicts | Step 5 null row verbatim | Step 5 null row verbatim | Step 5 contract null template | Step 5 null row verbatim | Step 5 contract null template |
| C-18 Structured delta format | Step 3 table | Step 3 table | Step 3 table | Step 3 table | Step 3 table |
| C-19 Diff Proposal ID col | Step 7 Proposal col | Step 7 Proposal col | Step 7 Proposal col (schema ★) | Step 7 Proposal col (checkpoint confirms) | Step 7 Proposal col (checkpoint confirms) |
| C-20 Delta Finding col in proposals | Step 6 mandatory + null rows | Step 6 mandatory + null rows | Step 6 mandatory + null rows (schema ★) | Step 6 (committed in checkpoint) | Step 6 (committed in checkpoint) |
| C-21 Column-completeness declaration | PASS: every table | PASS: every table | PASS: upfront ★ contract + mandatory at proposals + diff | PASS: upfront ★ contract + mandatory at proposals + diff | PASS: upfront ★ contract + mandatory at all tables |
| C-22 Active anti-pattern checkpoint | PASS: Step 3 stop+name | PASS: Step 3 stop+name | PASS: Step 3 stop+name | PASS: Step 3 stop+name+schema commitment | PASS: Step 3 stop+name+schema commitment |
| C-23 Pre-reproduced null templates | PASS: all 6 verbatim + Do not omit | PASS: all 6 verbatim + Do not omit | PASS: all 6 in OUTPUT CONTRACT | PASS: all 6 verbatim | PASS: all 6 in OUTPUT CONTRACT |
| **C-24 Unstated-assumption extraction** | **PASS: Step 1b dedicated substep + Assumption ID column + signal inventory links** | **PARTIAL: "What it assumed without naming" row in Step 1 table, no dedicated substep** | **PARTIAL: "What it assumed without naming" row in Step 1, no dedicated substep** | **PARTIAL: "What it assumed without naming" row in Step 1, no dedicated substep** | **PASS: Step 1b dedicated substep + Why column + signal inventory links assumption IDs** |
| **C-25 Inertia cost column ("If unchanged")** | **FAIL: no "If unchanged" column** | **PASS: "If unchanged" column with consequence-reasoning guidance; null rows carry N/A; "Nothing changes" is explicitly disallowed** | **FAIL: no "If unchanged" column** | **FAIL: no "If unchanged" column** | **PASS: "If unchanged" column; null rows carry N/A; checkpoint statement names it as ★ before Step 6** |
| **C-26 Schema-first priming** | **FAIL: no upfront schema block** | **FAIL: no upfront schema block** | **PASS: complete OUTPUT CONTRACT with all 6 tables + ★ columns + null templates before Step 1** | **PASS: complete Output Schema with all 6 tables + ★ columns before Step 1** | **PASS: complete OUTPUT CONTRACT with all 6 tables + ★ columns + null templates before Step 1** |
| **C-27 Cascade schema-commitment checkpoints** | **FAIL: one checkpoint (Step 3 anti-pattern only)** | **FAIL: one checkpoint (Step 3 anti-pattern only)** | **FAIL: one checkpoint (Step 3 anti-pattern only)** | **PASS: 3 checkpoints — Step 3 (anti-pattern + schema), Step 6 (proposals schema), Step 7 (diff schema)** | **PASS: 3 checkpoints — Step 3 (anti-pattern + schema), Step 6 (proposals schema with If unchanged ★), Step 7 (diff schema)** |

---

## v6 Discriminator Analysis

| Variation | C-24 mechanism | C-25 mechanism | C-26 mechanism | C-27 mechanism | Structural bet |
|-----------|----------------|----------------|----------------|----------------|----------------|
| V-01 | Dedicated Step 1b substep; Assumption ID column; signal inventory references assumption IDs | Absent | Absent | Absent (Step 3 only) | Assumption mining is most effective when it is a named act separate from stated-field extraction, not a row embedded in the same table |
| V-02 | "What it assumed without naming" row in Step 1 table (partial) | "If unchanged" as organizing principle from preamble; consequence-reasoning guidance; "Nothing changes" explicitly disallowed | Absent | Absent (Step 3 only) | Framing inertia as the primary evaluation question (not a column to fill) produces better consequence reasoning than column-instruction alone |
| V-03 | "What it assumed without naming" row in Step 1 (partial) | Absent | Consolidated OUTPUT CONTRACT before Step 1; all 6 ★ schemas + all null templates | Absent (Step 3 only) | Consolidating schema + null templates into one pre-read block is stronger than distributing them across steps; model cannot encounter a table without having pre-committed to its schema |
| V-04 | "What it assumed without naming" row in Step 1 (partial) | Absent | Complete ★ Output Schema before Step 1 | 3 checkpoints: Step 3 (anti-pattern + schema), Step 6 (proposals commit), Step 7 (diff commit) | Schema-first priming + cascade commitments create both pre-commitment (before reading) and multi-point evidence (during output) — independent audit at each checkpoint |
| V-05 | Dedicated Step 1b substep; Assumption ID + Why column; signal inventory links; assumption IDs in findings | "If unchanged" in proposals + null rows + named in Step 6 checkpoint commitment | Complete OUTPUT CONTRACT before Step 1 (includes Proposals schema with If unchanged ★) | 3 checkpoints: Step 3, Step 6 (includes If unchanged ★), Step 7 | C-24 + C-25 produce deeper content; C-26 + C-27 enforce that depth structurally — the cascade checkpoint at Step 6 names "If unchanged ★" before the table is built, making depth enforcement verifiable |

**Key structural distinctions:**

- **V-01 uniqueness**: The only variation where unstated assumption extraction is a *separate named step* with its own table and a "Why this is a delta candidate" column — making the reasoning behind each assumption visible before signals are read.
- **V-02 uniqueness**: The only variation where "Nothing changes" is explicitly prohibited as an If unchanged entry — naming the disallowed form is a different constraint than naming the required form.
- **V-03 uniqueness**: The only single-axis variation with both the complete schema AND all null templates in the upfront contract block — a model that reads the contract before Step 1 has every stop condition pre-resolved before encountering any artifact.
- **V-04 uniqueness**: The only variation where the model produces three schema-commitment *statements* as verifiable output — delta (anti-pattern + schema), proposals (schema commit), diff (schema commit) — fully satisfying C-27 without C-25 depth, isolating the cascade mechanism.
- **V-05 uniqueness**: The only variation where the proposals checkpoint statement explicitly names "If unchanged ★" as a mandatory column — meaning the inertia column is committed to in the verifiable output at Step 6, not only instructed in the step guidance. This is the tightest enforcement path for C-25: it is simultaneously depth (C-25 content requirement) and enforcement (C-27 checkpoint names it as required).

**C-24 partial vs full pass:**

V-02, V-03, V-04 have "What it assumed without naming" as a table row, which satisfies C-01's stated-field extraction requirement but does not constitute the dedicated substep C-24 requires ("lists as a named row or section" and "explicitly instructing unstated-assumption extraction" as a separate act). V-01 and V-05 provide the dedicated substep with Assumption ID column — the structural signal that assumption extraction is a different act from stated-field reading.

**Single-axis failure pattern:**

Each single-axis variation (V-01, V-02, V-03) targets one new criterion cleanly and fails the other three. This is intentional — the discriminator value comes from knowing which mechanisms are necessary vs sufficient. V-04 and V-05 reveal whether combining axes produces additive or synergistic compliance.
