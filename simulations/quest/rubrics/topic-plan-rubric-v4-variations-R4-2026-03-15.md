# topic-plan — Round 4 Variations (v4 rubric)

**Skill**: `topic:plan`
**Rubric**: v4 (C-01–C-20, 150 pts total)
**Date**: 2026-03-15

---

## Round 4 Design Notes

Round 3 established two universal gaps that v4 now formalizes as C-19 and C-20:

- **C-13** (inline evidence in diff): failed all 5 variations — evidence lived in the proposal table, not in the diff
- **C-16** (two-level traceability): all 5 were PARTIAL — conflict-driven proposals got two-level tracing, non-conflict proposals stayed single-hop

C-19 and C-20 are the structural fixes:
- **C-19**: a Proposal ID cross-reference column in the diff table creates a two-hop navigational path without requiring full inline duplication
- **C-20**: a Delta Finding column in the proposal table generalizes two-level tracing to all change types, making C-16 mechanically achievable

**Variation axes selected:**

| Variation | Axis | Type |
|-----------|------|------|
| V-01 | Role sequence — signals read before strategy | Single |
| V-02 | Output format — template-driven with explicit column schemas | Single |
| V-03 | Phrasing register — first-person conversational | Single |
| V-04 | Role sequence + Output format — hypothesis-first + unified table | Combination |
| V-05 | Lifecycle emphasis + Inertia framing — strategy assumptions foregrounded | Combination |

---

## V-01 — Signals-First

**Axis**: Role sequence — signals read before strategy
**Hypothesis**: Reading signals before strategy primes contrast-based delta detection. The strategy becomes the "what they thought" document encountered after evidence is already in memory, sharpening the "Strategy assumed X" anchor that C-18 requires and that C-20's Delta Finding column depends on. Evidence is loaded before the diff is built, making C-13/C-19 inline evidence natural rather than a retrofitted annotation.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it was written. You do **not** auto-apply changes. You present proposals, wait for confirmation, then write.

---

### Step 1 — Read and inventory signal artifacts

Glob `simulations/{topic}/` recursively. Read every file found. For each file, record: filename, namespace, skill, date, key finding in one sentence.

| ID | File | Namespace | Skill | Date | Key Finding | Consistent with strategy? |
|----|------|-----------|-------|------|-------------|--------------------------|
| S-01 | ... | ... | ... | ... | ... | Yes / No / Partial |

If no signal artifacts exist: output "No signals found — strategy.md does not need revision at this time." Stop.

---

### Step 2 — Read strategy.md

Read `simulations/{topic}/strategy.md`. Extract and record:

| Field | Value |
|-------|-------|
| Declared stage | ... |
| Namespaces covered | ... |
| Skills planned | ... |
| Stated rationale | ... |
| Acknowledged gaps | ... |

This gives you the "what the strategy assumed" side for every delta finding you will name next.

---

### Step 3 — Identify the delta (not an inventory)

**Anti-pattern warning**: A plain inventory of signal files is not the delta. The delta names what the signals revealed that the strategy did not anticipate. If signals only confirm what the strategy already said, the delta is empty.

For each finding where a signal diverges from or extends the strategy:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) |
|-----------|-----------------|----------------|-----------------|
| F-01 | [what strategy said or implicitly committed to] | [what S-XX showed instead] | S-01 |

Stop condition: If no findings diverge, write one row: `| F-00 | Strategy confirmed | No gaps detected | All |` and stop before proposals.

---

### Step 4 — Namespace coverage audit

Assess all 9 namespaces by name. "Stage-relative" means: is this coverage level appropriate for the topic's current stage?

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

Look for signals pointing in opposite directions (e.g., one says feasible, another says blocked). For each conflict, name the files and state the implication.

**Mandatory null case**: If no conflicts found, write:

> No conflicts detected — audit ran, no opposing signals found.

Do not omit this section. An absent conflict section is indistinguishable from a skipped audit regardless of whether your format is tabular or inline.

---

### Step 6 — Proposals table

Build the proposals table. **Every row must include a Delta Finding column** naming the specific Finding #N from Step 3 that motivated this change — reproduce the full "Strategy assumed [X] / Signal revealed [Y]" text. Every row must also carry a **Proposal ID** (e.g., ADD-1, REPRIORITIZE-2) so the diff table can cross-reference it.

All three types (ADD, REMOVE, REPRIORITIZE) must have at least one row. For empty types, use "None proposed" with Delta Finding: N/A.

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | Confidence |
|------------|------|--------|--------------|-------------------|------------|
| ADD-1 | ADD | ... | F-01: Strategy assumed ... / Signal revealed ... | file.md | High |
| REMOVE-1 | REMOVE | None proposed | Delta Finding: N/A | — | — |
| REPRIORITIZE-1 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | — |

A missing type row is an incomplete review.

---

### Step 7 — Before/after diff

For every item in the proposals table, produce a diff row. Every diff row must carry:
- **Evidence** inline: `[file.md — key finding in ≤10 words]`
- **Proposal** column: the Proposal ID from Step 6 — navigational anchor back to the full traceability chain without requiring the user to rescan the proposals table

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| ... | ... | [current] | [proposed] | [file.md — finding] | ADD-1 |

---

### Step 8 — Confirmation gate

Reply **YES** to apply all proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 9 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals. Preserve existing structure; update only the sections affected by confirmed changes.

---

## V-02 — Template-Driven

**Axis**: Output format — explicit table templates with named columns
**Hypothesis**: When the output template names "Delta Finding" and "Proposal ID" as literal column headers that the model must fill, compliance becomes mechanical fill-in-the-blank rather than inferred from instructions. C-19 and C-20 pass without requiring the model to reason about navigability — the columns exist by template structure, not by reasoning about the reviewer's needs.

---

You are executing `topic:plan` for the topic `{topic}`.

Read the strategy, read the signals, find the delta, propose typed changes with full traceability, confirm, then write. Every section below contains an output template. Fill every cell.

---

### Phase A — Read strategy.md

Read `simulations/{topic}/strategy.md`.

**Strategy Baseline** — fill every cell:

| Field | Value |
|-------|-------|
| Topic | {topic} |
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Stated rationale | |
| Acknowledged gaps | |

---

### Phase B — Read and inventory signals

Glob `simulations/{topic}/` recursively. Read every file found.

If no files: output "No signals gathered — strategy.md requires no revision." Stop.

**Signal Inventory** — fill every cell:

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? |
|----|------|-----------|-------|------|--------------------------|--------------------------|
| S-01 | | | | | | Yes / No / Partial |
| S-02 | | | | | | |

---

### Phase C — Delta identification

**Stop here and name the anti-pattern you are guarding against**: A plain inventory of signal files is not the delta. The delta names what the signals revealed that the strategy did not anticipate — the gap between what the strategy assumed and what signals proved.

**Delta Findings** — fill every cell, one row per diverging finding:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) |
|-----------|-----------------|----------------|-----------------|
| F-01 | | | |
| F-02 | | | |

Stop condition: If no findings diverge, write:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) |
|-----------|-----------------|----------------|-----------------|
| F-00 | Strategy confirmed | No gaps detected | All signals |

Then skip Phases D–F.

---

### Phase D — Namespace coverage audit

**Namespace Coverage** — check all 9 namespaces; fill every cell:

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

### Phase E — Conflict audit

Review the Signal Inventory (Phase B). Find rows where "Consistent with strategy?" is No or Partial AND two signals point in opposite directions.

**Conflict Table** — fill every cell:

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

**Mandatory null case** — if no conflicts, reproduce this exact row:

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-00 | — | — | No conflicts detected | No action needed |

Do not omit this table. An absent conflict table is indistinguishable from a skipped audit.

---

### Phase F — Change proposals

**The following columns are mandatory. Do not omit any column.**

**Proposals** — fill every cell:

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | Confidence |
|------------|------|--------|--------------|-------------------|------------|
| ADD-1 | ADD | | F-XX: Strategy assumed ... / Signal revealed ... | | High/Medium/Low |
| REMOVE-1 | REMOVE | | F-XX: ... | | |
| REPRIORITIZE-1 | REPRIORITIZE | | F-XX: ... | | |

Rules:
- All three types (ADD, REMOVE, REPRIORITIZE) must have at least one row
- Empty types: write "None proposed" in Change; write "Delta Finding: N/A" in Delta Finding
- Delta Finding must reproduce the full "Strategy assumed [X] / Signal revealed [Y]" text from Phase C using the exact Finding ID

---

### Phase G — Before/after diff

**The following columns are mandatory. Do not omit any column.**

**Change Diff** — fill every cell:

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current strategy text] | [proposed new text] | [file.md — ≤10 word finding] | ADD-1 |

Rules:
- **Evidence**: `[file.md — finding in ≤10 words]` inline per row — no separate evidence section required
- **Proposal**: the Proposal ID from Phase F (e.g., "ADD-1") — this column is the navigational pointer from the diff to the evidence and traceability chain in Phase F; it makes confirmation single-pass without requiring the user to rescan Phase F

---

### Phase H — Confirmation gate

Reply **YES** to apply all proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Phase I — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` with all confirmed proposals applied.

---

## V-03 — Conversational Register

**Axis**: Phrasing register — first-person conversational
**Hypothesis**: First-person register ("I'll build the proposals table, making sure each row has its Delta Finding column...") creates a natural self-monitoring channel where the model names what it's about to produce before producing it. This should reduce structural omissions (especially the Delta Finding and Proposal ID columns) without requiring a separate enforcement pass — the narration commits the model to the structure before the table is built.

---

You are executing `topic:plan` for `{topic}`. I'll run this as a structured walk-through: read signals, read strategy, find the delta, propose changes with full traceability, and wait for your confirmation before writing anything.

---

### Step 1 — I'll read the signal artifacts first

I'll glob `simulations/{topic}/` and read every file I find. For each one, I'll record the filename, namespace, skill, date, and key finding. I'll also note whether each signal is consistent with what the strategy says — this sets up the contrast I need for the delta step.

If I find no signal files, I'll stop and tell you: the strategy needs no revision yet.

| ID | File | Namespace | Skill | Date | Key Finding | Consistent with strategy? |
|----|------|-----------|-------|------|-------------|--------------------------|
| S-01 | | | | | | Yes / No / Partial |

---

### Step 2 — I'll read strategy.md and record what it committed to

I'll read `simulations/{topic}/strategy.md` and note everything the strategy explicitly or implicitly assumed. This "what the strategy believed" record is what makes the delta step honest — I can't name "Strategy assumed X" without having actually read and internalized what X was.

| Field | Value |
|-------|-------|
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Rationale | |
| Acknowledged gaps | |

---

### Step 3 — I'll find the delta — not an inventory

I'm guarding against a specific failure mode: **a plain inventory of signal files is not the delta**. What I'm looking for is what signals revealed that the strategy did not anticipate — where the evidence diverged from the commitments I recorded in Step 2.

For each diverging finding, I'll write one structured entry:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) |
|-----------|-----------------|----------------|-----------------|
| F-01 | | | |

If all signals confirm the strategy, I'll write: "Finding: Signals confirmed — no gaps detected." and stop before proposals.

---

### Step 4 — I'll audit all 9 namespaces by name

I'll check every namespace — `scout`, `draft`, `review`, `flow`, `trace`, `prove`, `listen`, `program`, `topic` — and assess whether the signal coverage is appropriate for the topic's current stage. Stage-relative means I'm not just counting signals; I'm asking whether *this much* coverage is right for *this stage*.

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

### Step 5 — I'll check for conflicting signals

I'll look for signals pointing in opposite directions. For each conflict I find, I'll name the files and say what it means for the strategy.

If I find no conflicts, I'll say so explicitly — I'll write "No conflicts detected." rather than leaving this section blank or omitting it. An absent section looks the same as a skipped audit; an explicit null result is evidence the audit ran. This applies whether I'm using a table or inline annotation.

---

### Step 6 — I'll build the proposals table with full traceability

I'll propose changes typed as ADD, REMOVE, or REPRIORITIZE. Each row will carry:
- A **Proposal ID** (ADD-1, REMOVE-2, REPRIORITIZE-1, etc.) so the diff table can reference it directly
- A **Delta Finding** column: the specific Finding #N from Step 3, with the full "Strategy assumed [X] / Signal revealed [Y]" text reproduced — not just the Finding ID

All three types must appear. Empty types get a "None proposed" row with "Delta Finding: N/A" so the column is structurally consistent.

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | Confidence |
|------------|------|--------|--------------|-------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | High |
| REMOVE-1 | REMOVE | None proposed | Delta Finding: N/A | — | — |
| REPRIORITIZE-1 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | — |

---

### Step 7 — I'll build the before/after diff with inline evidence and proposal pointers

Each diff row will carry two navigational aids:
- **Evidence** inline: `[file.md — key finding in ≤10 words]` — no cross-referencing to a separate section
- **Proposal** column: the Proposal ID from Step 6 — links this diff row back to the full Delta Finding and evidence chain without duplicating the full text

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | | | [file.md — finding] | ADD-1 |

---

### Step 8 — I'll wait for your confirmation

Here are all proposed changes. Reply **YES** to apply them to `simulations/{topic}/strategy.md`.

I will not write anything until you confirm.

Waiting.

---

### Step 9 — Apply (only after YES)

I'll rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals.

---

## V-04 — Hypothesis-First + Unified Table

**Axis**: Role sequence + Output format — hypothesis formed before reading; proposals and diff merged into one table
**Hypothesis**: (1) Forming a gap hypothesis before reading forces the model to approach files as evidence for or against specific predictions, sharpening delta detection and making the "Strategy assumed X" anchor easier to fill honestly. (2) A unified table that merges proposals, evidence, and diff into one structure eliminates the C-13/C-19/C-20 navigation problem entirely — there is no separate sections to cross-reference when all information is on one row.

---

You are executing `topic:plan` for `{topic}`.

---

### Step 1 — State a gap hypothesis (before reading any files)

Before reading anything: based on the topic name and the 9-namespace model (`scout`, `draft`, `review`, `flow`, `trace`, `prove`, `listen`, `program`, `topic`), name 2–3 types of gaps you would expect to find if signals have been gathered but the strategy has not been revised.

These are predictions — you will confirm, revise, or discard them after reading.

| # | Predicted gap type | Namespace(s) most likely affected |
|---|-------------------|------------------------------------|
| H-1 | | |
| H-2 | | |
| H-3 | | |

---

### Step 2 — Read signal artifacts

Glob `simulations/{topic}/` recursively. Read every file found. Note whether each signal confirms a hypothesis, contradicts it, or reveals something unexpected.

If no files found: "No signals gathered — no revision needed." Stop.

| ID | File | Namespace | Skill | Date | Key Finding | Confirms hypothesis? |
|----|------|-----------|-------|------|-------------|----------------------|
| S-01 | | | | | | H-N / Unexpected / Confirms strategy |

---

### Step 3 — Read strategy.md; revise hypothesis

Read `simulations/{topic}/strategy.md`. Extract stage, namespaces covered, skills planned, rationale, acknowledged gaps.

Update your hypothesis table:

| Hypothesis | Status | Notes |
|-----------|--------|-------|
| H-1 | Confirmed / Revised / Discarded | |
| H-2 | | |
| H-3 | | |

---

### Step 4 — Delta identification

**Anti-pattern check**: A plain inventory of signal files is not the delta. The delta names what the signals revealed that the strategy did not anticipate.

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) |
|-----------|-----------------|----------------|-----------------|
| F-01 | | | |

Stop condition: If all signals confirm, write: `| F-00 | Strategy confirmed | No gaps detected | All |` and stop.

---

### Step 5 — Namespace audit + conflict check

**9-namespace audit** (all by name):

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

**Conflict audit** — mandatory, do not omit:

| Conflict ID | Signal A | Signal B | Implication for strategy |
|------------|---------|---------|--------------------------|
| CF-01 | | | |

Null case (required when no conflicts found):

| Conflict ID | Signal A | Signal B | Implication for strategy |
|------------|---------|---------|--------------------------|
| CF-00 | — | — | No conflicts detected — audit ran, none found |

---

### Step 6 — Unified change table

This single table is both the proposals record AND the diff. It replaces separate "proposals" and "before/after" sections. Every column is mandatory — do not omit any.

| Proposal ID | Type | Namespace | Before | After | Delta Finding | Evidence | Confidence |
|------------|------|-----------|--------|-------|--------------|---------|------------|
| ADD-1 | ADD | | [current text or "—"] | [proposed text] | F-XX: Strategy assumed ... / Signal revealed ... | [file.md — ≤10 word finding] | High |
| REMOVE-1 | REMOVE | None proposed | — | — | Delta Finding: N/A | — | — |
| REPRIORITIZE-1 | REPRIORITIZE | None proposed | — | — | Delta Finding: N/A | — | — |

Column rules:
- **Delta Finding**: Finding ID + full "Strategy assumed / Signal revealed" text from Step 4
- **Evidence**: inline per row — `[file.md — ≤10 word finding]`
- **Before/After**: this IS the diff — the table makes a separate diff section unnecessary
- All three types must appear; "None proposed" rows require "Delta Finding: N/A"

---

### Step 7 — Confirmation gate

Reply **YES** to apply all proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 8 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals.

---

## V-05 — Inertia-Foregrounded

**Axis**: Lifecycle emphasis + Inertia framing — strategy's original assumptions made explicit; every proposal names cost of inaction
**Hypothesis**: When the strategy's commitments are fully reconstructed before signals are read, and every proposal row must name "If unchanged: [cost]", the model produces richer Delta Finding entries naturally — it has already committed to what the strategy believed, so the "Strategy assumed X" anchor is easier to fill honestly and harder to fabricate. The inertia framing also makes C-16/C-20 self-enforcing: naming the cost of not changing forces the model to have traced the causal path from assumption to proposal.

---

You are executing `topic:plan` for `{topic}`.

This revision starts from the strategy's original intent, then measures how far signals have moved from it. Every proposed change names what the strategy would leave unaddressed if no change is made.

---

### Step 1 — Fully reconstruct strategy.md's commitments

Read `simulations/{topic}/strategy.md`. Reconstruct its commitments in detail — including what it assumed without naming explicitly.

| Strategy commitment | Detail |
|---------------------|--------|
| Declared stage | |
| Core belief about the topic | |
| Namespaces it covers | |
| Namespaces it explicitly defers | |
| Skills it planned | |
| Risks it acknowledged | |
| What it assumed without naming | [at least one item — the most important for delta detection] |

The last row is the most important. Every unstated assumption is a delta candidate.

---

### Step 2 — Read and inventory signal artifacts

Glob `simulations/{topic}/` recursively. Read every file found. For each signal, note whether it confirms a strategy assumption or challenges one — and if challenging, name which assumption.

If no files: "No signals gathered — strategy remains current." Stop.

| ID | File | Namespace | Skill | Date | Key Finding | Confirms or challenges which assumption? |
|----|------|-----------|-------|------|-------------|------------------------------------------|
| S-01 | | | | | | Confirms: [which] / Challenges: [which] |

---

### Step 3 — Identify the delta (not an inventory)

**Anti-pattern warning**: A plain inventory of signal files is not the delta. The delta names what signals revealed that the strategy did not anticipate — where evidence diverged from the commitments and assumptions you recorded in Step 1.

For each diverging finding:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) |
|-----------|-----------------|----------------|-----------------|
| F-01 | [what strategy said or implicitly committed to — from Step 1] | [what S-XX showed instead] | S-01 |

Stop condition: "Finding: Signals confirmed — strategy assumptions remain valid."

---

### Step 4 — Namespace coverage audit

Audit all 9 namespaces by name. "Expected at this stage?" means: should this namespace be covered given the topic's current stage, not just whether any signal exists.

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

For every signal pair pointing in opposite directions, name the conflict and its implication for strategy.

**Mandatory null case**: If no conflicts found, write the following — do not omit this section regardless of whether your format is tabular or inline:

> No conflicts detected — audit ran, no opposing signals found.

An absent section is indistinguishable from a skipped audit.

---

### Step 6 — Proposals with inertia cost

Build the proposals table. Every row must include:
- **Proposal ID** (ADD-1, REMOVE-2, REPRIORITIZE-1) for diff cross-referencing
- **Delta Finding**: the specific Finding #N from Step 3, with full "Strategy assumed [X] / Signal revealed [Y]" text
- **If unchanged**: what gap persists, worsens, or becomes harder to fix if this proposal is deferred

All three types must appear. "None proposed" rows require "Delta Finding: N/A" and "If unchanged: N/A".

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Confidence |
|------------|------|--------|--------------|-------------------|-------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | file.md | [what persists if skipped] | High |
| REMOVE-1 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |
| REPRIORITIZE-1 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |

---

### Step 7 — Before/after diff with navigational anchors

For each changed item, produce a diff row carrying:
- **Evidence** inline: `[file.md — ≤10 word finding]` — no cross-referencing needed
- **Proposal** column: the Proposal ID from Step 6 — navigational anchor from this diff row to the full Delta Finding and evidence chain in Step 6

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current strategy text] | [proposed new text] | [file.md — finding] | ADD-1 |

---

### Step 8 — Confirmation gate

Reply **YES** to apply all proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 9 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals.

---

## Criterion Coverage Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Read strategy | Step 2 | Phase A | Step 2 | Step 3 | Step 1 |
| C-02 Read signals | Step 1 | Phase B | Step 1 | Step 2 | Step 2 |
| C-03 Delta not inventory | Step 3 warning | Phase C warning | Step 3 warning | Step 4 warning | Step 3 warning |
| C-04 Typed proposals | Step 6 table | Phase F table | Step 6 table | Step 6 table | Step 6 table |
| C-05 Confirm gate | Step 8 | Phase H | Step 8 | Step 7 | Step 8 |
| C-06 Evidence per change | Step 6 Evidence col | Phase F Evidence col | Step 6 Evidence col | Step 6 Evidence col | Step 6 Evidence col |
| C-07 Before/after diff | Step 7 | Phase G | Step 7 | Step 6 (unified) | Step 7 |
| C-08 All three types | Step 6 + no-change rule | Phase F + no-change rule | Step 6 + no-change rule | Step 6 + no-change rule | Step 6 + no-change rule |
| C-09 Namespace gaps | Step 4 | Phase D | Step 4 | Step 5 | Step 4 |
| C-10 Conflicting signals | Step 5 | Phase E | Step 5 | Step 5 | Step 5 |
| C-11 Typed confirmation verb | Step 8 YES | Phase H YES | Step 8 YES | Step 7 YES | Step 8 YES |
| C-12 No-change rows | Step 6 rule | Phase F rule | Step 6 rule | Step 6 rule | Step 6 rule |
| C-13 Inline evidence in diff | Step 7 Evidence col | Phase G Evidence col | Step 7 Evidence col | Step 6 unified (inline) | Step 7 Evidence col |
| C-14 Anti-inventory warning | Step 3 verbatim | Phase C verbatim | Step 3 verbatim | Step 4 verbatim | Step 3 verbatim |
| C-15 All 9 namespaces named | Step 4 table | Phase D table | Step 4 table | Step 5 table | Step 4 table |
| C-16 Two-level traceability | Step 6: Delta Finding + Evidence | Phase F: Delta Finding + Evidence | Step 6: Delta Finding + Evidence | Step 6: Delta Finding + Evidence | Step 6: Delta Finding + Evidence |
| C-17 Explicit no-conflicts | Step 5 mandatory rule (format-agnostic) | Phase E null row | Step 5 mandatory rule (format-agnostic) | Step 5 null row | Step 5 mandatory rule (format-agnostic) |
| C-18 Structured delta format | Step 3 template | Phase C template | Step 3 template | Step 4 template | Step 3 template |
| C-19 Diff Proposal ID column | Step 7 Proposal col | Phase G Proposal col | Step 7 Proposal col | Step 6 unified (Proposal ID col) | Step 7 Proposal col |
| C-20 Delta Finding column in proposals | Step 6 mandatory | Phase F mandatory | Step 6 narrated then mandatory | Step 6 mandatory | Step 6 mandatory |

**Key structural bets:**

| Criterion | V-01 mechanism | V-02 mechanism | V-03 mechanism | V-04 mechanism | V-05 mechanism |
|-----------|----------------|----------------|----------------|----------------|----------------|
| C-13 + C-19 | Separate table columns | Separate table columns (template-forced) | Separate table columns (narrated) | Unified table — inline + Proposal ID | Separate table columns |
| C-16 + C-20 | Delta Finding col in proposals | Delta Finding col (template-forced) | Delta Finding col (narrated) | Delta Finding col in unified table | Delta Finding col + inertia framing makes causal path natural |
| C-17 | "format-agnostic" rule (closes V-01/V-04 R3 gap) | Null row in table | "format-agnostic" rule | Null row in table | "format-agnostic" rule |
| C-14 | Verbatim anti-inventory label | Verbatim anti-inventory label | Verbatim anti-inventory label | Verbatim anti-inventory label | Verbatim anti-inventory label |
