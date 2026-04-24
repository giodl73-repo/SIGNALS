# topic-plan — Round 5 Variations (v5 rubric)

**Skill**: `topic:plan`
**Rubric**: v5 (C-01–C-23, 165 pts total)
**Date**: 2026-03-15

---

## Round 5 Design Notes

Round 4 achieved 150/150 (v4 rubric) across all 5 variations. The v4 meta-assessment predicted this outcome ("full-round convergence") and recommended Round 5 either move to execution fidelity or target the three new v5 criteria. This round targets the three new criteria.

**What changed in v5:**

| Criterion | Layer | What Round 4 missed |
|-----------|-------|---------------------|
| C-21 | Enforcement: column completeness as named rule | V-02 had the declaration before proposals+diff only; delta findings, namespace, conflict, and signal inventory tables had no adjacent declaration |
| C-22 | Enforcement: anti-pattern awareness as verifiable output | All R4 variations named the anti-pattern in the prompt (C-14 pass); none required the *model* to produce the label before proceeding |
| C-23 | Enforcement: null-case form as copy-paste act | V-02 pre-reproduced the conflict null row; no variation pre-reproduced the three proposal-type null rows |

**Variation axes:**

| Variation | Axis | Type | Primary v5 target |
|-----------|------|------|-------------------|
| V-01 | Output format — column-completeness declaration on every template | Single | C-21 exhaustive |
| V-02 | Phrasing register — stop-and-produce checkpoints at every compliance gate | Single | C-22 cascade |
| V-03 | Lifecycle emphasis — pre-reproduced null template library | Single | C-23 exhaustive |
| V-04 | Role sequence + Output format — upfront schema contract + checkpoint at delta | Combination | C-21 + C-22 |
| V-05 | Output format + Lifecycle emphasis + Inertia framing — full enforcement stack | Combination | C-21 + C-22 + C-23 + depth |

---

## V-01 — All-Templates Column Declaration

**Axis**: Output format — column-completeness declaration adjacent to every structured template
**Hypothesis**: Round 4's V-02 placed "The following columns are mandatory. Do not omit any column." before proposals and diff tables — the two tables where C-19/C-20 column elision would be most costly. C-21 extends this obligation to every template. Placing the declaration adjacent to all six structured outputs (signal inventory, delta findings, namespace audit, conflict table, proposals, diff) creates a uniform schema contract: the model never encounters a table template without an adjacent prohibition on column omission. The absence of the declaration becomes the exception, making partial compliance structurally visible.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it was written. Present proposals, wait for confirmation, then write. Do not auto-apply changes.

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

---

### Step 2 — Read and inventory signal artifacts

Glob `simulations/{topic}/` recursively. Read every file found.

If no signal artifacts exist, reproduce the following verbatim and stop. Do not omit this output:

> No signals found — strategy.md does not need revision at this time.

**The following columns are mandatory. Do not omit any column.**

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? |
|----|------|-----------|-------|------|--------------------------|--------------------------|
| S-01 | | | | | | Yes / No / Partial |

---

### Step 3 — Identify the delta (not an inventory)

Stop here. Write the name of the anti-pattern you are guarding against at this step. Then proceed to the findings table.

**The following columns are mandatory. Do not omit any column.**

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) |
|-----------|-----------------|----------------|-----------------|
| F-01 | | | |

Stop condition: If all signals confirm the strategy, reproduce the following row verbatim and skip to Step 5. Do not omit this row:

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

## V-02 — Active Checkpoint Cascade

**Axis**: Phrasing register — imperative stop-and-produce checkpoints at every compliance-critical transition
**Hypothesis**: C-22 requires the model to produce the anti-pattern label as verifiable output at the delta step. If a single stop-and-produce checkpoint reduces the most common failure mode (silent inventory substituting for delta), cascading the pattern to all compliance-critical structural transitions should produce a similar constraint at each boundary. Before the delta table the model names the anti-pattern; before the proposals table it commits to the column schema in prose; before the diff table it commits to inline evidence format. Each commitment is auditable in the output independently — a reviewer can confirm compliance at any step without reading the full prompt. The anti-pattern checkpoint remains the primary C-22 gate; the proposals and diff checkpoints are structural satellites.

---

You are executing `topic:plan` for the topic `{topic}`.

Revise `simulations/{topic}/strategy.md` based on signals gathered since it was written. This prompt uses stop-and-declare checkpoints at compliance-critical steps. At each checkpoint, produce the named output before proceeding. Do not auto-apply changes.

---

### Step 1 — Read strategy.md

Read `simulations/{topic}/strategy.md`. Extract:

| Field | Value |
|-------|-------|
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Stated rationale | |
| Acknowledged gaps | |

---

### Step 2 — Read and inventory signal artifacts

Glob `simulations/{topic}/` recursively. Read every file found.

If no files found: output "No signals found — strategy.md requires no revision." and stop.

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? |
|----|------|-----------|-------|------|--------------------------|--------------------------|
| S-01 | | | | | | Yes / No / Partial |

---

### Step 3 — Delta checkpoint (produce before building table)

**Stop. Before building the findings table, produce the following two outputs:**

1. **Anti-pattern label**: Name the anti-pattern you are guarding against at this step. Write the label. Do not omit this output.
2. **Delta definition**: Write one sentence stating what the delta IS, contrasted with what it IS NOT.

Then proceed to the findings table.

For each finding where a signal diverges from or extends the strategy:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) |
|-----------|-----------------|----------------|-----------------|
| F-01 | | | |

Stop condition: If all signals confirm the strategy, reproduce the following verbatim and skip to Step 5. Do not omit this row:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) |
|-----------|-----------------|----------------|-----------------|
| F-00 | Strategy confirmed | No gaps detected | All signals |

---

### Step 4 — Namespace coverage audit

List all 9 namespaces by name. "Stage-relative" = appropriate for this stage, not a raw count.

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

Review all signals. Name opposing pairs.

**Mandatory null case** — if no conflicts found, reproduce the following verbatim. Do not omit this section:

> No conflicts detected — audit ran, no opposing signals found.

---

### Step 6 — Proposals checkpoint (produce before building table)

**Stop. Before building the proposals table, write the following statement verbatim:**

> "Proposals schema: Proposal ID, Type, Change, Delta Finding (full 'Strategy assumed [X] / Signal revealed [Y]' text from Step 3), Evidence, Confidence. All three types (ADD, REMOVE, REPRIORITIZE) will have at least one row. Empty types will have a null row."

Write that statement, then build the table.

**The following columns are mandatory. Do not omit any column.**

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | Confidence |
|------------|------|--------|--------------|-------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | High |

For empty types, reproduce the applicable row(s) verbatim. Do not omit any type row:

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | Confidence |
|------------|------|--------|--------------|-------------------|------------|
| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | — |

---

### Step 7 — Diff checkpoint (produce before building table)

**Stop. Before building the diff table, write the following statement verbatim:**

> "Diff schema: Namespace, Skill/Area, Before, After, Evidence (inline per row as [file.md — ≤10 word finding]), Proposal (Proposal ID from Step 6). No separate evidence section."

Write that statement, then build the table.

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

## V-03 — Null Template Library

**Axis**: Lifecycle emphasis — pre-reproduced verbatim templates for every null outcome with "Do not omit" instruction
**Hypothesis**: C-23 requires pre-reproduced null templates + "Do not omit" for all mandatory null sections. Round 4's V-02 pre-reproduced only the conflict null row (CF-00). The full null-outcome space has six branches: (1) no signals, (2) all signals confirm (delta null), (3) no conflicts, (4) no ADD proposals, (5) no REMOVE proposals, (6) no REPRIORITIZE proposals. Providing verbatim copy-paste text for all six eliminates model discretion at every stop condition. The model has nothing to decide about null-case form — it either adds content rows or reproduces the pre-written template. Structural consistency is achieved by copy, not by inference.

---

You are executing `topic:plan` for the topic `{topic}`.

Revise `simulations/{topic}/strategy.md` based on signals. Every section provides verbatim null-case text for when the condition is empty. Reproduce null templates exactly when the condition applies. Do not paraphrase, abbreviate, or omit null sections. Do not auto-apply changes.

---

### Step 1 — Read strategy.md

Read `simulations/{topic}/strategy.md`. Extract:

| Field | Value |
|-------|-------|
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Stated rationale | |
| Acknowledged gaps | |

---

### Step 2 — Read and inventory signal artifacts

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals** — if no files found, reproduce the following verbatim and stop. Do not omit this output:

> No signals found — strategy.md does not need revision at this time. Run signal-gathering skills before attempting revision.

If signals found, continue:

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? |
|----|------|-----------|-------|------|--------------------------|--------------------------|
| S-01 | | | | | | Yes / No / Partial |

---

### Step 3 — Identify the delta (not an inventory)

**Anti-pattern**: A plain inventory of signal files is not the delta. The delta names what the signals revealed that the strategy did not anticipate.

Stop here. Name the anti-pattern you are guarding against. Then proceed to the findings table.

For each finding where a signal diverges from or extends the strategy:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) |
|-----------|-----------------|----------------|-----------------|
| F-01 | | | |

**Null case — all signals confirm** — if no diverging findings, reproduce the following row verbatim and skip to Step 5. Do not omit this row:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) |
|-----------|-----------------|----------------|-----------------|
| F-00 | Strategy confirmed | No gaps detected | All signals |

---

### Step 4 — Namespace coverage audit

List all 9 namespaces by name. "Stage-relative" = appropriate for this stage, not a raw count.

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

Check for signals pointing in opposite directions. Name each opposing pair and its implication.

**Null case — no conflicts** — if no conflicts found, reproduce the following verbatim. Do not omit this table:

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

---

### Step 6 — Proposals table

Propose changes typed as ADD, REMOVE, or REPRIORITIZE. All three types must appear.

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | Confidence |
|------------|------|--------|--------------|-------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | High |

**Null cases — empty types** — for each type with no proposals, reproduce the corresponding row verbatim. Do not omit any type row:

**ADD null case:**

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | Confidence |
|------------|------|--------|--------------|-------------------|------------|
| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | — |

**REMOVE null case:**

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | Confidence |
|------------|------|--------|--------------|-------------------|------------|
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | — |

**REPRIORITIZE null case:**

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | Confidence |
|------------|------|--------|--------------|-------------------|------------|
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | — |

Delta Finding must reproduce the full "Strategy assumed [X] / Signal revealed [Y]" text from Step 3.

---

### Step 7 — Before/after diff

For every confirmed proposal, produce one diff row carrying inline evidence and a Proposal ID pointer.

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current text] | [proposed text] | [file.md — ≤10 word finding] | ADD-1 |

- **Evidence**: `[file.md — ≤10 word finding]` inline per row — no separate evidence section
- **Proposal**: Proposal ID from Step 6 — navigational anchor to the full Delta Finding chain

---

### Step 8 — Confirmation gate

Reply **YES** to apply all proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 9 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals.

---

## V-04 — Schema-First + Active Checkpoints

**Axes**: Role sequence + Output format — upfront schema declaration before reading; active stop-and-produce at delta and proposals
**Hypothesis**: (1) Declaring the complete output schema before any file-reading begins primes the model with the full structural contract upfront. The model knows before touching any artifact what every table must look like and which columns are mandatory — the contract is not revealed progressively but committed to before execution starts. The ★ mandatory-column notation is compact enough to survive context pressure. (2) Active stop-and-produce checkpoints at the delta step (C-22) and the proposals step create two independent verifiable compliance signals. A reviewer can audit C-22 compliance at the delta output without reading the proposal table, and can audit proposals schema compliance without re-reading the upfront schema. Dual checkpoints are harder to fail silently than a single one.

---

You are executing `topic:plan` for the topic `{topic}`.

**Before reading any files, review the complete output schema below.** Every table you produce must conform to this schema. Columns marked ★ are mandatory — do not omit any ★ column.

---

### Output Schema (read before proceeding to Step 1)

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

Do not omit any ★ column. If a column is absent from your output, that table fails schema validation regardless of whether content is present in other columns.

---

### Step 1 — Read strategy.md

Read `simulations/{topic}/strategy.md`. Extract:

| Field | Value |
|-------|-------|
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Stated rationale | |
| Acknowledged gaps | |

---

### Step 2 — Read and inventory signal artifacts

Glob `simulations/{topic}/` recursively. Read every file found.

If no files: output "No signals found — strategy.md requires no revision." and stop.

Per schema (Signal Inventory):

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? |
|----|------|-----------|-------|------|--------------------------|--------------------------|
| S-01 | | | | | | Yes / No / Partial |

---

### Step 3 — Delta step: produce checkpoint outputs before building table

**Stop. Produce these two outputs before building the findings table:**

1. **Anti-pattern label**: Name the anti-pattern you are guarding against at this step. (Write the label — do not skip.)
2. **Corrective statement**: One sentence: what the delta IS versus what it IS NOT.

Then build per schema (Delta Findings):

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

Per schema (Conflict Audit). Null case — reproduce verbatim, do not omit this table:

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

---

### Step 6 — Proposals: confirm schema before building

**Stop. Before building the proposals table, write:**

> "Proposals schema confirmed: Proposal ID ★, Type ★, Change ★, Delta Finding ★ (full 'Strategy assumed [X] / Signal revealed [Y]' text from Step 3), Evidence ★, Confidence ★. All three types present. Empty types will use null rows."

Then build per schema (Proposals). Null rows for empty types — reproduce verbatim, do not omit any type:

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | Confidence |
|------------|------|--------|--------------|-------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | High |
| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | — |

---

### Step 7 — Before/after diff

Per schema (Diff). Evidence inline per row. Proposal = Proposal ID from Step 6.

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

## V-05 — Full Enforcement Stack

**Axes**: Output format + Lifecycle emphasis + Inertia framing — column declarations on every template; full null template library; inertia cost column in proposals
**Hypothesis**: C-21, C-22, and C-23 all address the enforcement layer — the gap between "the instruction is present" and "the model cannot deviate from it." A variation that stacks all three enforcement mechanisms (column declarations on every table, active anti-pattern checkpoint, full null template library) should achieve maximal structural compliance. The inertia framing — an "If unchanged" column in proposals naming the cost of not changing — forces causal depth in Delta Finding entries: the model must trace assumption → gap → consequence, making "Strategy assumed X / Signal revealed Y" substantive rather than a mechanical label fill. V-05 from Round 4 had the inertia framing but not the full C-21/C-22/C-23 stack. This variation combines both.

---

You are executing `topic:plan` for the topic `{topic}`.

This revision starts from the strategy's original commitments, measures how far signals have moved from them, and names the cost of inaction for every proposed change. Every table carries a column-completeness declaration. Every null outcome has a pre-reproduced template — reproduce it verbatim when the condition applies. Do not auto-apply changes.

---

### Step 1 — Reconstruct strategy.md's commitments

Read `simulations/{topic}/strategy.md`. Reconstruct all commitments, including what the strategy assumed without naming explicitly.

**The following columns are mandatory. Do not omit any column.**

| Strategy commitment | Detail |
|---------------------|--------|
| Declared stage | |
| Core belief about the topic | |
| Namespaces covered | |
| Namespaces explicitly deferred | |
| Skills planned | |
| Risks acknowledged | |
| What it assumed without naming | [at least one item — the most important for delta detection] |

The last row is the most important: every unstated assumption is a delta candidate.

---

### Step 2 — Read and inventory signal artifacts

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals** — if no files found, reproduce the following verbatim and stop. Do not omit this output:

> No signals found — strategy.md remains current. Run signal-gathering skills before attempting revision.

**The following columns are mandatory. Do not omit any column.**

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Confirms or challenges which assumption? |
|----|------|-----------|-------|------|--------------------------|------------------------------------------|
| S-01 | | | | | | Confirms: [which] / Challenges: [which] |

---

### Step 3 — Identify the delta (not an inventory)

Stop here. Name the anti-pattern you are guarding against at this step. Then proceed to the findings table.

**The following columns are mandatory. Do not omit any column.**

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) |
|-----------|-----------------|----------------|-----------------|
| F-01 | [from Step 1 commitments] | [from Step 2 signals] | S-XX |

**Null case — all signals confirm** — reproduce the following row verbatim and skip to Step 5. Do not omit this row:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) |
|-----------|-----------------|----------------|-----------------|
| F-00 | Strategy confirmed | No gaps detected | All signals |

---

### Step 4 — Namespace coverage audit

**The following columns are mandatory. Do not omit any column.**

| Namespace | Signal Count | Expected at this stage? | Status | Gap? |
|-----------|-------------|------------------------|--------|------|
| scout | | Yes/No | Covered/Thin/Missing | |
| draft | | | | |
| review | | | | |
| flow | | | | |
| trace | | | | |
| prove | | | | |
| listen | | | | |
| program | | | | |
| topic | | | | |

---

### Step 5 — Conflict audit

**The following columns are mandatory. Do not omit any column.**

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

**Null case — no conflicts** — reproduce the following row verbatim. Do not omit this table:

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

---

### Step 6 — Proposals with inertia cost

**The following columns are mandatory. Do not omit any column.**

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Confidence |
|------------|------|--------|--------------|-------------------|-------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | file.md | [what gap persists if deferred] | High |

All three types must appear. For empty types, reproduce the applicable row(s) verbatim. Do not omit any type row:

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Confidence |
|------------|------|--------|--------------|-------------------|-------------|------------|
| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |

Column rules:
- **Delta Finding**: full "Strategy assumed [X] / Signal revealed [Y]" text from Step 3 with exact Finding ID
- **If unchanged**: name what gap persists, worsens, or becomes harder to close if this proposal is deferred

---

### Step 7 — Before/after diff

**The following columns are mandatory. Do not omit any column.**

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current strategy text] | [proposed text] | [file.md — ≤10 word finding] | ADD-1 |

- **Evidence**: `[file.md — ≤10 word finding]` inline per row
- **Proposal**: Proposal ID from Step 6 — navigational anchor to the full Delta Finding and inertia chain

---

### Step 8 — Confirmation gate

Reply **YES** to apply all proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 9 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals.

---

## Criterion Coverage Matrix

Coverage assessed against v5 rubric (C-01–C-23). C-01–C-20 are carried forward from Round 4 (all PASS in all variations; mechanisms unchanged unless noted). New criteria C-21/C-22/C-23 are the discriminators.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Read strategy | Step 1 | Step 1 | Step 1 | Step 1 | Step 1 |
| C-02 Read signals | Step 2 | Step 2 | Step 2 | Step 2 | Step 2 |
| C-03 Delta not inventory | Step 3 checkpoint | Step 3 checkpoint | Step 3 warning | Step 3 checkpoint | Step 3 checkpoint |
| C-04 Typed proposals | Step 6 table | Step 6 table | Step 6 table | Step 6 table | Step 6 table |
| C-05 Confirm gate | Step 8 YES | Step 8 YES | Step 8 YES | Step 8 YES | Step 8 YES |
| C-06 Evidence per change | Step 6 Evidence col | Step 6 Evidence col | Step 6 Evidence col | Step 6 Evidence col | Step 6 Evidence col |
| C-07 Before/after diff | Step 7 | Step 7 | Step 7 | Step 7 | Step 7 |
| C-08 All three types | Step 6 null rows | Step 6 null rows | Step 6 null rows | Step 6 null rows | Step 6 null rows |
| C-09 Namespace gaps | Step 4 (9 by name) | Step 4 (9 by name) | Step 4 (9 by name) | Step 4 (9 by name) | Step 4 (9 by name) |
| C-10 Conflicting signals | Step 5 | Step 5 | Step 5 | Step 5 | Step 5 |
| C-11 Typed confirmation verb | Step 8 YES | Step 8 YES | Step 8 YES | Step 8 YES | Step 8 YES |
| C-12 Explicit no-change rows | Step 6 null rows verbatim | Step 6 null rows verbatim | Step 6 null rows verbatim | Step 6 null rows verbatim | Step 6 null rows verbatim |
| C-13 Inline evidence in diff | Step 7 Evidence col | Step 7 checkpoint + col | Step 7 Evidence col | Step 7 Evidence col | Step 7 Evidence col |
| C-14 Anti-inventory warning | Step 3 (stop + name) | Step 3 (stop + name + contrast) | Step 3 verbatim label | Step 3 (stop + name + contrast) | Step 3 (stop + name) |
| C-15 All 9 namespaces named | Step 4 table | Step 4 table | Step 4 table | Step 4 table | Step 4 table |
| C-16 Two-level traceability | Step 6: Delta Finding + Evidence | Step 6: Delta Finding + Evidence | Step 6: Delta Finding + Evidence | Step 6: Delta Finding + Evidence | Step 6: Delta Finding + Evidence |
| C-17 Explicit no-conflicts | Step 5 null row verbatim | Step 5 verbatim statement | Step 5 null row verbatim | Step 5 null row verbatim | Step 5 null row verbatim |
| C-18 Structured delta format | Step 3 table | Step 3 table | Step 3 table | Step 3 table | Step 3 table |
| C-19 Diff Proposal ID col | Step 7 Proposal col | Step 7 Proposal col (committed in checkpoint) | Step 7 Proposal col | Step 7 Proposal col | Step 7 Proposal col |
| C-20 Delta Finding col in proposals | Step 6 mandatory + null rows | Step 6 (committed in checkpoint) | Step 6 mandatory + null rows | Step 6 (committed in checkpoint) | Step 6 mandatory + null rows |
| **C-21 Column-completeness declaration** | **PASS: every table** | **PASS: proposals + diff (checkpoint replaces declaration on others)** | **PARTIAL: proposals + diff only** | **PASS: upfront schema + proposals checkpoint** | **PASS: every table** |
| **C-22 Active anti-pattern checkpoint** | **PASS: Step 3 stop+name** | **PASS: Step 3 stop+name+contrast; cascade to Steps 6+7** | **PASS: Step 3 stop+name** | **PASS: Step 3 stop+name+contrast** | **PASS: Step 3 stop+name** |
| **C-23 Pre-reproduced null templates** | **PASS: all 6 null outcomes** | **PASS: all 6 null outcomes** | **PASS: all 6 null outcomes (labeled individually)** | **PASS: all 6 null outcomes** | **PASS: all 6 null outcomes** |

---

## v5 Discriminator Analysis

| Variation | C-21 mechanism | C-22 mechanism | C-23 mechanism | Structural bet |
|-----------|----------------|----------------|----------------|----------------|
| V-01 | Declaration on every table — uniformity means no table is ambiguous | Stop+name at delta only | All 6 null outcomes with verbatim text | C-21 exhaustiveness reduces variance across all tables |
| V-02 | Declaration before proposals+diff; cascade of schema-commitment statements replaces declaration on upstream tables | Stop+name+contrast at delta; schema commitments at proposals and diff — 3 auditable checkpoints | All 6 null outcomes with verbatim text | C-22 cascade creates multiple independent verification points |
| V-03 | Declaration before proposals+diff only — C-21 partial | Stop+name at delta | All 6 null outcomes labeled individually with separate headers | C-23 exhaustiveness with labeled null cases is clearest for model scanning |
| V-04 | Upfront ★ schema + "do not omit" per table — priming before execution | Stop+name+contrast at delta; schema confirmation at proposals | All 6 null outcomes | Schema-first priming should reduce C-21/C-23 omissions via commitment before reading |
| V-05 | Declaration on every table (same as V-01) | Stop+name at delta | All 6 null outcomes (same as V-01) | Inertia column enriches C-20 Delta Finding entries; full stack on all new criteria |

**Key structural distinctions:**

- **V-01 vs V-05**: Same C-21/C-22/C-23 mechanisms; V-05 adds "If unchanged" inertia column and "unstated assumption" extraction in Step 1. V-05 should produce richer Delta Finding entries at the cost of a longer Step 1 and Step 6.
- **V-02 uniqueness**: The cascade of stop-and-produce checkpoints at three steps is the only variation where compliance is verifiable at three independent points — delta, proposals, and diff. Reviewer can audit each step independently.
- **V-03 uniqueness**: The only variation that labels each null case with its own section header ("NULL CASE — no ADD proposals:"). This makes it impossible to miss which null template applies — they are not interleaved with positive-case instructions but separated into labeled blocks.
- **V-04 uniqueness**: The only variation where the model reads the schema before reading any content. This separates the structural contract from execution: the model has committed to the full column schema before it encounters any artifact.

**Where V-03 is the weakest on C-21**: V-03 places the column declaration only before proposals and diff (the critical two), not before the delta findings table or signal inventory. This is intentional — V-03's single axis is C-23 (null templates), and adding full C-21 declarations everywhere would make the variation ambiguous. Round 5 scoring will show whether C-23 exhaustiveness compensates for partial C-21 coverage.
