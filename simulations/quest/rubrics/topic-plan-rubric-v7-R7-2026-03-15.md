# topic-plan — Round 7 Variations (v6 rubric)

**Skill**: `topic:plan`
**Rubric**: v6 (C-01–C-27, 185 pts total)
**Date**: 2026-03-15

---

## Round 7 Design Notes

Round 6 achieved first coverage of all four v6 criteria across its five variations and set the benchmark for the full C-24+C-25+C-26+C-27 stack in R6-V-05. The criterion mechanisms now exist and are structurally present — the question R7 asks is whether they are **load-bearing or decorative**: can a model fill the columns correctly while still reasoning shallowly?

**What R6 achieved and where load-bearing gaps remain:**

| Criterion | R6 mechanism | Gap R7 must close |
|-----------|-------------|-------------------|
| C-24 | Step 1b table with Assumption ID + "Why this is a delta candidate" column | "Why this is a delta candidate" can be filled with one word; no traceability check from assumption → finding |
| C-25 | "If unchanged" column in proposals + consequence-first preamble (R6-V-02) | Column can still be filled with a synonym of the delta finding rather than a forward causal claim; no time-pressure distinction |
| C-26 | Upfront ★ schema block before Step 1 | Schema is declared but the model encounters it once then proceeds under context pressure; no re-activation |
| C-27 | Three checkpoints (delta, proposals, diff) each requiring the model to state schema | Checkpoint phrasing in R6-V-04 is correct but proposals checkpoint doesn't explicitly name null rows it will produce |

**R7 target:** Close each gap through three new mechanism dimensions.

**Three new mechanism dimensions explored in R7:**

1. **Role sequence** — The model adopts an explicitly named cognitive role at each phase transition. Reading strategy.md as a "stated-field extractor" is a different act from reading it as an "assumption archaeologist." Role declarations direct attention before execution, not just constrain output after.

2. **Reversibility distinction** — C-25's "If unchanged" column extended with a binary "Reversibility" axis: *Reversible at same cost / Gets harder / Becomes impossible.* Forces the model to make a forward claim about time pressure — not just "this gap exists" but "waiting increases cost." Converts the inertia column from current-state description to trajectory commitment.

3. **Explicit assumption → finding → proposal traceability chain** — A-NN (assumption) → F-NN (finding) → Proposal ID cross-references made explicit and auditable in each table. In R6 the chain was structurally available; in R7 it is a named obligation at every hop.

**Variation design:**

| Variation | Axis | Type | Primary R7 target |
|-----------|------|------|-------------------|
| V-01 | Role sequence — explicit cognitive role declarations at each phase | Single | C-24 (assumption mining as role, not substep) |
| V-02 | Phrasing register — conversational/decision register throughout | Single | C-25 (purpose-motivated vs. rule-motivated compliance) |
| V-03 | Inertia framing — reversibility dimension added to proposals | Single | C-25 (time-pressure forward claim) |
| V-04 | Role sequence + Schema-first priming | Combination | C-24 + C-26 |
| V-05 | Full stack: role sequence + reversibility + A-to-Proposal traceability chain | Combination | C-24 + C-25 + C-26 + C-27 |

---

## V-01 — Cognitive Role Sequence

**Axis**: Role sequence — the model adopts an explicitly named cognitive role at each phase transition, shifting how it approaches each step
**Hypothesis**: R6 V-01 separated the assumption-mining act into a substep (Step 1b) and added an Assumption ID table. The mechanism is structurally present but the *posture* of the read is unchanged — the model extracts stated fields in Step 1a and then fills an assumption table in Step 1b using the same field-extraction heuristic. If each phase shift is accompanied by an explicit role declaration, the model is directed toward a different cognitive act before it encounters any content. An "assumption archaeologist" looks for what is absent; a "signal analyst" looks for what contradicts; a "strategist" looks for what action changes the outcome. Role declarations are a form of pre-execution framing that C-24/C-25 do not currently mandate. The hypothesis is that role-directed reading surfaces qualitatively different assumptions than table-directed reading — the former asks "what did this strategy take for granted?" while the latter asks "what goes in the last row?"

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it was written. You will adopt a distinct cognitive role at each phase. Present proposals, wait for confirmation, then write. Do not auto-apply changes.

---

### Step 1a — Role: Stated-Field Extractor

**Adopt this role now**: You are a stated-field extractor. Read only what strategy.md wrote explicitly. Do not interpret, infer, or supplement. Extract verbatim or paraphrase — but only what the document actually says.

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

### Step 1b — Role: Assumption Archaeologist

**Adopt this role now**: You are an assumption archaeologist. Your job is to find what strategy.md took for granted without writing — the implied worldview, the unstated preconditions, the beliefs the author would defend if challenged but did not put in the document. These are the highest-value delta candidates: a signal can contradict what was assumed, not only what was stated.

Systematic scan: look for (a) implied audience knowledge level, (b) namespace priority ordering, (c) signal sufficiency threshold, (d) timeline or sequencing feasibility, (e) what "done" means in this context. Add any others you find.

**The following columns are mandatory. Do not omit any column.**

| Assumption ID | What strategy.md assumed without writing | Contradicted by a signal? (Leave blank — filled in Step 3) |
|--------------|------------------------------------------|-------------------------------------------------------------|
| A-01 | [most important — highest likelihood of having been contradicted by a signal] | |
| A-02 | [second assumption, if any] | |

Write at least one row. If the strategy makes no unstated assumptions, write A-00: "No unstated assumptions found after systematic scan."

---

### Step 2 — Role: Signal Analyst

**Adopt this role now**: You are a signal analyst. Your job is to read every artifact and evaluate it against two things: (a) the stated fields from Step 1a, and (b) the assumptions from Step 1b. Both are delta sources.

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals** — if no files found, reproduce the following verbatim and stop. Do not omit this output:

> No signals found — strategy.md does not need revision at this time.

**The following columns are mandatory. Do not omit any column.**

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? | Assumption link (A-NN or "none") |
|----|------|-----------|-------|------|--------------------------|--------------------------|----------------------------------|
| S-01 | | | | | | Yes / No / Partial | |

---

### Step 3 — Role: Delta Identifier

**Adopt this role now**: You are a delta identifier. Your job is to name what changed — not inventory what exists.

Stop. Before building the findings table, write the name of the anti-pattern you are guarding against at this step. Do not proceed until you have written the label.

**The following columns are mandatory. Do not omit any column.**

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root (A-NN or "stated field") |
|-----------|-----------------|----------------|-----------------|------------------------------------------|
| F-01 | [from Step 1a fields or Step 1b assumptions] | | S-XX | |

Findings rooted in unstated assumptions (A-NN from Step 1b) must fill the Assumption root column with the matching ID. Return to Step 1b and mark the "Contradicted by a signal?" column for each finding.

**Null case — all signals confirm** — reproduce the following row verbatim and skip to Step 5. Do not omit this row:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root |
|-----------|-----------------|----------------|-----------------|-----------------|
| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |

---

### Step 4 — Role: Coverage Auditor

**Adopt this role now**: You are a coverage auditor. Your job is to assess all 9 namespaces by name for stage-relative completeness — not raw signal count, but whether coverage is appropriate for where this topic currently is.

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

**Adopt this role now**: You are a conflict detective. Your job is to find opposing signals — artifacts that point in different directions on the same dimension.

**The following columns are mandatory. Do not omit any column.**

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

**Null case — no conflicts** — reproduce the following row verbatim. Do not omit this table:

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

---

### Step 6 — Role: Proposal Architect

**Adopt this role now**: You are a proposal architect. Your job is to translate findings into typed, defensible change proposals. Every proposal must be grounded in a specific delta finding and every finding must trace back to a stated field or an unstated assumption.

**The following columns are mandatory. Do not omit any column.**

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Confidence |
|------------|------|--------|--------------|-------------------|-------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [what gap persists if deferred] | High |

All three types (ADD, REMOVE, REPRIORITIZE) must appear. Reproduce null rows verbatim for empty types. Do not omit any type row:

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Confidence |
|------------|------|--------|--------------|-------------------|-------------|------------|
| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |

Column rules:
- **Delta Finding**: full "Strategy assumed [X] / Signal revealed [Y]" text from Step 3 with exact Finding ID
- **If unchanged**: name what gap persists, worsens, or becomes harder to close if this proposal is deferred

---

### Step 7 — Role: Diff Author

**Adopt this role now**: You are a diff author. Your job is to show exactly what would change in strategy.md, with inline evidence anchoring each change to its source, and a Proposal ID anchor connecting each row to the full causal chain.

**The following columns are mandatory. Do not omit any column.**

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current strategy text] | [proposed text] | [file.md — ≤10 word finding] | ADD-1 |

- **Evidence**: `[file.md — finding in ≤10 words]` inline per row — no separate evidence section
- **Proposal**: Proposal ID from Step 6 — anchor back to the full Delta Finding and assumption chain

---

### Step 8 — Confirmation gate

Reply **YES** to apply all proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 9 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals. Preserve existing structure; update only sections affected by confirmed changes.

---

## V-02 — Conversational Decision Register

**Axis**: Phrasing register — the entire prompt adopts a peer/mentor register, framing each step as a decision with purpose, not a rule with a compliance check
**Hypothesis**: Formal template prompts establish compliance by rule: "The following columns are mandatory. Do not omit any column." A conversational register establishes compliance by shared understanding of *why* the column matters. The hypothesis is that when a model understands the purpose of a column — "the 'If unchanged' column exists because a proposal without a named cost of deferral is a preference, not a decision" — it fills the column with a genuine causal claim rather than a synonym of the delta finding. Purpose-motivated compliance is harder to discharge mechanically because discharging it mechanically produces output that obviously fails the stated purpose. The conversational register also embeds the C-24 assumption-mining rationale naturally ("what strategy.md never wrote is often more important than what it did") and the C-26 schema-priming mechanism as a frame-setting act ("before you read anything, here's the shape of the output you're building"). The register switch is hypothesis-only — formal register may outperform if the model defaults to treating conversational framing as soft suggestions rather than hard requirements.

---

You are executing `topic:plan` for the topic `{topic}`.

Here is what this skill is for: `strategy.md` was written before most signals existed. It made commitments based on what was known at the time — and it assumed things it never wrote down. Your job is to find out how far the world has moved from those commitments and proposals changes that would bring the strategy back into alignment. Then you wait for confirmation before writing anything.

**Before you read a single file, review this output shape.** You will produce six structured tables. Here are the columns that matter and why:

| Table | Key column | Why it matters |
|-------|-----------|----------------|
| Signal Inventory | "Confirms or challenges which assumption?" | Connects signals to what the strategy never wrote — not just to what it did |
| Delta Findings | "Strategy assumed / Signal revealed" | The two-part format is the delta — the gap between what was believed and what was learned |
| Namespace Audit | "Stage-Relative Status" | Coverage is meaningful relative to stage, not as a raw count |
| Conflict Audit | All columns (even when empty) | An omitted conflict section is indistinguishable from a skipped audit |
| Proposals | "Delta Finding" + "If unchanged" | Delta Finding names the causal source; "If unchanged" names why deferral has a cost |
| Diff | "Evidence" inline + "Proposal" cross-ref | These two columns make the diff a navigable decision record, not a change list |

All column sets above are mandatory. If a table is missing any of its key columns, the output is incomplete regardless of whether other columns are present.

---

### Step 1 — What did strategy.md actually commit to?

Read `simulations/{topic}/strategy.md`. You are reading for two things at once: (a) what it stated, and (b) what it assumed without stating. The second is usually more important for delta detection — a signal can only contradict what was believed, and beliefs are often unstated.

**Stated fields** (what it wrote):

| Field | Value |
|-------|-------|
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Stated rationale | |
| Acknowledged gaps | |

**Unstated assumptions** (what it took for granted) — write at least one. Look for implied beliefs about audience knowledge, namespace priority, signal sufficiency, timeline feasibility, and what "done" means here:

| Assumption ID | What strategy.md assumed without writing | Why this matters for delta detection |
|--------------|------------------------------------------|-------------------------------------|
| A-01 | | |

The last column asks: if a signal contradicted this assumption, would that change what skills or namespaces to prioritize? If yes, it is a high-value delta candidate.

---

### Step 2 — What did the signals actually say?

Glob `simulations/{topic}/` recursively. Read every file found.

If no signals exist: output "No signals found — strategy.md is current. Gather signals before revising." and stop.

For each artifact, record its key finding and whether it aligns with a stated field or an unstated assumption from Step 1:

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? | Assumption link (A-NN or "stated field" or "none") |
|----|------|-----------|-------|------|--------------------------|--------------------------|-----------------------------------------------------|
| S-01 | | | | | | Yes / No / Partial | |

The "Assumption link" column is what connects signals to beliefs rather than just to stated content — and it is what makes the "Strategy assumed" column in Step 3 meaningful.

---

### Step 3 — What is the delta?

The delta is not an inventory of signals. The delta is what the signals revealed that the strategy did not anticipate — including what they revealed about unstated assumptions. Before you build the findings table, write the name of the failure mode you are guarding against at this step.

For each gap you find:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root |
|-----------|-----------------|----------------|-----------------|-----------------|
| F-01 | [from Step 1 stated fields or assumptions] | | S-XX | [A-NN or "stated field"] |

If every signal confirms the strategy, that is a valid and important outcome. Reproduce this verbatim and skip to Step 5:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root |
|-----------|-----------------|----------------|-----------------|-----------------|
| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |

Do not omit this row if it applies — a skipped null case looks identical to a skipped audit.

---

### Step 4 — Where are the coverage gaps?

Check all 9 namespaces by name. "Appropriate for this stage" is the criterion — not "has at least one signal."

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

### Step 5 — Are any signals in conflict?

Look for pairs of artifacts that point in opposite directions on the same dimension. A conflict is not a difference of emphasis — it is a difference of direction that would lead to different strategy choices.

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

If no conflicts found — this section must still appear. Reproduce verbatim:

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

---

### Step 6 — What should change, and what happens if it doesn't?

Every proposal needs to answer two questions: "What should change?" and "What fails to improve if we defer this?" A proposal that can't answer the second question is a preference, not a decision.

All three types (ADD, REMOVE, REPRIORITIZE) must appear. For types with nothing to propose, reproduce the null row exactly — it proves the type was considered:

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Confidence |
|------------|------|--------|--------------|-------------------|-------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [specific gap that persists or worsens] | High |

Null rows (reproduce verbatim for each empty type):

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Confidence |
|------------|------|--------|--------------|-------------------|-------------|------------|
| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |

The "If unchanged" column should name a specific degradation — not "nothing changes" but "which artifact won't be gathered" or "which gap becomes harder to close after the next sprint."

---

### Step 7 — What would strategy.md look like after these changes?

For each proposal, show before and after. Evidence goes inline on the row — not in a separate section — so the diff is a complete decision record by itself:

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current text] | [proposed text] | [file.md — ≤10 word finding] | ADD-1 |

---

### Step 8 — Confirmation gate

Reply **YES** to apply all proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 9 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals. Preserve existing structure; update only sections affected by confirmed changes.

---

## V-03 — Reversibility Dimension

**Axis**: Inertia framing — the proposals table gains a "Reversibility" column that forces the model to make a forward claim about time-pressure, not just current-state description
**Hypothesis**: R6 V-02 introduced a consequence-first preamble and the "If unchanged" column. The column can still be filled with a synonym of the delta finding — "the gap will remain uncovered" is technically correct but not a forward causal claim. Adding a "Reversibility" column with three allowed values (Reversible at same cost / Gets harder / Becomes impossible) forces the model to classify the *trajectory* of the gap: is this a deferrable optimization or a compounding problem? This distinction converts the inertia column from a current-state observation ("gap persists") to a time-pressure commitment ("waiting increases cost") — the latter being a claim the model must reason to, not pattern-match from the delta finding. The reversibility column also creates a natural triage axis: proposals classified "Becomes impossible" should be surfaced first; proposals classified "Reversible at same cost" can wait. The hypothesis is that a binary triage dimension makes the proposals table a decision support tool rather than a change recommendation list.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it was written. Every proposed change must include a reversibility assessment — whether the gap gets harder or impossible to close if deferred. Present proposals, wait for confirmation, then write. Do not auto-apply changes.

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
| What it assumed without naming | [at least one — the most important for delta detection] |

The last row is mandatory: every unstated assumption is a delta candidate.

---

### Step 2 — Read and inventory signal artifacts

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals** — reproduce the following verbatim and stop. Do not omit this output:

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
| F-01 | [from Step 1 stated fields or unstated assumptions] | | S-XX |

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

**Null case — no conflicts** — reproduce the following row verbatim. Do not omit this table:

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-00 | — | — | No conflicts detected — audit ran | No action needed |

---

### Step 6 — Proposals with reversibility assessment

Before building the proposals table, write the following statement verbatim:

> "Proposals schema: Proposal ID, Type, Change, Delta Finding (full 'Strategy assumed [X] / Signal revealed [Y]' text), Evidence, If unchanged, Reversibility, Confidence. All three types present. Empty types use null rows."

Then build the table.

**The following columns are mandatory. Do not omit any column.**

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Reversibility | Confidence |
|------------|------|--------|--------------|-------------------|-------------|--------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [specific gap that persists] | Reversible at same cost / Gets harder / Becomes impossible | High |

**Reversibility values** (exactly one per row):
- **Reversible at same cost** — can be deferred without increasing effort to close the gap later
- **Gets harder** — the gap compounds; closing it later requires more effort or more signals
- **Becomes impossible** — the window to address this closes; deferral means the gap is permanent

For each type with no proposals, reproduce the applicable row(s) verbatim. Do not omit any type row:

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Reversibility | Confidence |
|------------|------|--------|--------------|-------------------|-------------|--------------|------------|
| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

Delta Finding must reproduce the full "Strategy assumed [X] / Signal revealed [Y]" text from Step 3 with the exact Finding ID.

---

### Step 7 — Before/after diff

Before building the diff table, write the following statement verbatim:

> "Diff schema: Namespace, Skill/Area, Before, After, Evidence (inline per row as [file.md — ≤10 word finding]), Proposal (Proposal ID from Step 6). No separate evidence section."

Then build the table.

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

## V-04 — Role Sequence + Schema-First Priming

**Axes**: Role sequence (from V-01) + Schema-first priming (C-26) — the model reads the complete output schema before adopting any role, then adopts distinct cognitive roles within that contract
**Hypothesis**: R6 V-03/V-04 demonstrated schema-first priming (C-26): declaring the full ★-column schema before Step 1 commits the model to the structural contract before encountering any artifact. V-01 above demonstrated role sequence: assigning an explicit cognitive role at each phase directs attention differently (archaeologist vs. analyst vs. architect). The combination separates *what to produce* (schema priming, upfront) from *how to approach each phase* (role sequence, per-step). The model reads the full structural contract before adopting any role, then adopts roles within that contract — so role shifts cannot cause column omissions (the schema was committed to before any role was active). The hypothesis is that the combination address two independent failure modes: (1) column omission under context pressure (addressed by schema priming), and (2) shallow reasoning in columns (addressed by role sequence). Neither mechanism alone closes both gaps; together they should.

---

You are executing `topic:plan` for the topic `{topic}`.

**Before reading any files, review the complete output schema below.** Every table you produce must conform to this schema. Columns marked ★ are mandatory — do not omit any ★ column. You will adopt a named cognitive role at each phase — but the structural contract below governs the output regardless of role.

---

### Output Schema (read before proceeding to Step 1)

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

Do not omit any ★ column. A table missing any ★ column fails schema validation regardless of whether other columns are present.

---

### Step 1a — Role: Stated-Field Extractor

**Adopt this role**: Read only what strategy.md wrote explicitly. Extract stated fields. Do not interpret or supplement.

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

### Step 1b — Role: Assumption Archaeologist

**Adopt this role**: Find what strategy.md took for granted without writing. The implied worldview. The unstated preconditions. The beliefs the author would defend if challenged but did not put in the document.

Scan systematically for: (a) implied audience knowledge level, (b) namespace priority ordering, (c) signal sufficiency threshold, (d) timeline or sequencing feasibility, (e) definition of "done" for this topic.

**The following columns are mandatory. Do not omit any column.**

| Assumption ID | What strategy.md assumed without writing | Likelihood of signal contradiction (High / Medium / Low) |
|--------------|------------------------------------------|----------------------------------------------------------|
| A-01 | [most important for delta detection] | |
| A-02 | [second assumption, if any] | |

Write at least one row. If no unstated assumptions found: write A-00 "No unstated assumptions found after systematic scan." The "Likelihood" column forces prioritization — A-NN rows flagged High are the first candidates to check against signals in Step 2.

---

### Step 2 — Role: Signal Analyst

**Adopt this role**: Read every artifact and evaluate it against two reference points: (a) stated fields from Step 1a, and (b) assumptions from Step 1b. The final column anchors each signal to the reference point it speaks to most directly.

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals** — reproduce the following verbatim and stop. Do not omit this output:

> No signals found — strategy.md does not need revision at this time.

Per schema (Signal Inventory):

**The following columns are mandatory. Do not omit any column.**

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? | Assumption link (A-NN / "stated field" / "none") |
|----|------|-----------|-------|------|--------------------------|--------------------------|--------------------------------------------------|
| S-01 | | | | | | Yes / No / Partial | |

---

### Step 3 — Role: Delta Identifier

**Adopt this role**: Name what changed. Not what exists — what the gap is between what strategy.md believed and what signals revealed.

**Stop. Before building the findings table, produce both outputs:**

1. **Anti-pattern label**: Name the anti-pattern you are guarding against at this step. Write the label.
2. **Delta definition**: One sentence — what the delta IS (gap between belief and signal) vs. what it IS NOT (inventory of signal existence).

Per schema (Delta Findings):

**The following columns are mandatory. Do not omit any column.**

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root (A-NN / "stated field") |
|-----------|-----------------|----------------|-----------------|----------------------------------------|
| F-01 | | | S-XX | |

Findings rooted in Step 1b assumptions must reference the A-NN ID. Return to Step 1b and update the assumption table to mark which assumptions were contradicted.

**Null case — all signals confirm** — reproduce verbatim and skip to Step 5. Do not omit this row:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root |
|-----------|-----------------|----------------|-----------------|-----------------|
| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |

---

### Step 4 — Role: Coverage Auditor

**Adopt this role**: Assess all 9 namespaces for stage-relative completeness — not raw count.

Per schema (Namespace Audit):

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

**Adopt this role**: Find opposing signals — artifacts that point in different directions on the same dimension.

Per schema (Conflict Audit):

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

**Adopt this role**: Translate findings into typed, defensible proposals. Every proposal must answer two questions: "What changes?" and "What fails to improve if we defer?"

**Stop. Before building the proposals table, write the following statement verbatim:**

> "Proposals schema confirmed: Proposal ID ★, Type ★, Change ★, Delta Finding ★ (full 'Strategy assumed [X] / Signal revealed [Y]' text from Step 3 with exact ID), Evidence ★, If unchanged ★, Confidence ★. All three types (ADD, REMOVE, REPRIORITIZE) will have at least one row. Empty types will use pre-reproduced null rows."

Then build per schema (Proposals):

**The following columns are mandatory. Do not omit any column.**

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Confidence |
|------------|------|--------|--------------|-------------------|-------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [specific gap that persists or worsens] | High |

Null rows (reproduce verbatim for each empty type):

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Confidence |
|------------|------|--------|--------------|-------------------|-------------|------------|
| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | — |

---

### Step 7 — Role: Diff Author

**Adopt this role**: Show exactly what would change. Every row carries inline evidence and a Proposal ID pointer — the diff is a complete navigable decision record.

**Stop. Before building the diff table, write the following statement verbatim:**

> "Diff schema confirmed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★ (inline as [file.md — ≤10 word finding] — no separate evidence section), Proposal ★ (Proposal ID from Step 6)."

Then build per schema (Diff):

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

## V-05 — Full Stack: Role Sequence + Reversibility + Explicit Traceability Chain

**Axes**: Role sequence (V-01) + Reversibility dimension (V-03) + Schema-first priming (C-26) + Cascade checkpoints (C-27) + Explicit A-to-Proposal traceability chain
**Hypothesis**: R6 V-05 stacked all four v6 criteria (C-24 through C-27) and established the R6 ceiling. R7 V-05 extends the ceiling in three directions simultaneously: (1) role sequence makes assumption mining a cognitive posture, not a row to fill; (2) reversibility makes the inertia column a trajectory claim, not a current-state synonym; (3) an explicit A-NN → F-NN → Proposal ID traceability chain, named as a navigation obligation in the proposals and diff tables, makes the three-level causal path auditable from any starting point. The upfront schema block declares all six tables with ★ columns before execution begins; cascade checkpoints at delta, proposals, and diff each require the model to commit to both schema and null-row obligations simultaneously — making each checkpoint carry double verification weight. The full stack is the most demanding variation and the most likely to surface the next round's excellence signals.

---

You are executing `topic:plan` for the topic `{topic}`.

**Before reading any files, review the complete output schema below.** Every table you produce must conform to this schema. Columns marked ★ are mandatory — do not omit any ★ column. A table missing any ★ column fails regardless of other content.

---

### Output Schema (read before proceeding to Step 1)

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

**Traceability obligation**: Every Proposal row must be traceable from the diff (Proposal ID) → to the proposal table (Delta Finding) → to the findings table (Finding ID) → to the assumption table (Assumption root). A Proposal row with a missing Delta Finding column, or a Finding row with a missing Assumption root column, breaks the traceability chain. Schema compliance alone is insufficient — every chain hop must be filled.

---

### Step 1a — Role: Stated-Field Extractor

**Adopt this role**: Extract only what strategy.md wrote explicitly. Verbatim or paraphrase — but only what the document actually says.

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

### Step 1b — Role: Assumption Archaeologist

**Adopt this role**: Find what strategy.md took for granted without writing. The implied worldview. The unstated preconditions. The beliefs the author would defend if challenged but did not put in the document. These are the highest-value delta candidates.

Systematic scan: (a) implied audience knowledge level, (b) namespace priority ordering, (c) signal sufficiency threshold, (d) timeline or sequencing feasibility, (e) definition of "done" for this topic. Add any others.

**The following columns are mandatory. Do not omit any column.**

| Assumption ID | What strategy.md assumed without writing | Likelihood of contradiction (High / Medium / Low) | Contradicted? (fill after Step 3) |
|--------------|------------------------------------------|--------------------------------------------------|----------------------------------|
| A-01 | [most important for delta detection] | | |
| A-02 | [second assumption, if any] | | |

Write at least one row. If no unstated assumptions found after systematic scan: write A-00 "No unstated assumptions identified." The "Likelihood" column prioritizes which assumptions to match against signals first. The "Contradicted?" column is filled in Step 3 — not here.

---

### Step 2 — Role: Signal Analyst

**Adopt this role**: Read every artifact against two reference points: (a) stated fields from Step 1a, and (b) assumptions from Step 1b. Map each signal to its reference point.

Glob `simulations/{topic}/` recursively. Read every file found.

**Null case — no signals** — reproduce the following verbatim and stop. Do not omit this output:

> No signals found — strategy.md remains current. Run signal-gathering skills before attempting revision.

**The following columns are mandatory. Do not omit any column.**

| ID | File | Namespace | Skill | Date | Key Finding (1 sentence) | Consistent with strategy? | Assumption link (A-NN / "stated field" / "none") |
|----|------|-----------|-------|------|--------------------------|--------------------------|--------------------------------------------------|
| S-01 | | | | | | Yes / No / Partial | |

---

### Step 3 — Role: Delta Identifier

**Adopt this role**: Name the gap between what strategy.md believed and what signals revealed. Not an inventory — a finding for each belief that was contradicted or extended.

**Stop. Before building the findings table, produce both outputs:**

1. **Anti-pattern label**: Name the anti-pattern you are guarding against at this step. Write the label.
2. **Delta definition**: One sentence — delta IS: [gap between belief and signal]. Delta IS NOT: [inventory of signal existence].

After building the findings table, return to Step 1b and fill the "Contradicted?" column for every A-NN that has a matching finding.

**The following columns are mandatory. Do not omit any column.**

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root (A-NN / "stated field") |
|-----------|-----------------|----------------|-----------------|----------------------------------------|
| F-01 | [from Step 1a stated fields or Step 1b assumptions] | | S-XX | |

**Null case — all signals confirm** — reproduce verbatim and skip to Step 5. Do not omit this row:

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root |
|-----------|-----------------|----------------|-----------------|-----------------|
| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |

---

### Step 4 — Role: Coverage Auditor

**Adopt this role**: Assess all 9 namespaces for stage-relative completeness.

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

**Adopt this role**: Translate each finding into a typed, defensible proposal with a named cost of inaction and a reversibility assessment.

**Stop. Before building the proposals table, write the following statement verbatim:**

> "Proposals schema committed: Proposal ID ★, Type ★, Change ★, Delta Finding ★ (full 'Strategy assumed [X] / Signal revealed [Y]' text from Step 3 with exact Finding ID), Evidence ★, If unchanged ★ (specific degradation — not 'nothing changes'), Reversibility ★ (Reversible at same cost / Gets harder / Becomes impossible), Confidence ★. All three types will appear. Empty types will use the pre-reproduced null rows below. Traceability: each Proposal ID must be linkable to a Finding ID (via Delta Finding column) and from there to an Assumption root (A-NN or 'stated field')."

Then build the table:

**The following columns are mandatory. Do not omit any column.**

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Reversibility | Confidence |
|------------|------|--------|--------------|-------------------|-------------|--------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [specific degradation if deferred] | Gets harder | High |

Null rows (reproduce verbatim for each empty type):

| Proposal ID | Type | Change | Delta Finding | Evidence [file(s)] | If unchanged | Reversibility | Confidence |
|------------|------|--------|--------------|-------------------|-------------|--------------|------------|
| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

**Reversibility values** (exactly one per content row):
- **Reversible at same cost**: can defer without increasing effort
- **Gets harder**: gap compounds; closing it later costs more effort or more signals
- **Becomes impossible**: window closes; deferral makes the gap permanent

---

### Step 7 — Role: Diff Author

**Adopt this role**: Show the exact before/after change for every confirmed proposal. Every row is a complete navigable record — evidence inline, Proposal ID as the entry point into the full A-NN → F-NN → Proposal ID traceability chain.

**Stop. Before building the diff table, write the following statement verbatim:**

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★ (inline per row as [file.md — ≤10 word finding] — no separate evidence section), Proposal ★ (Proposal ID from Step 6 — entry point into full traceability chain: Proposal → Delta Finding → Assumption root)."

Then build the table:

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

## Criterion Coverage Matrix (v6 rubric, C-01–C-27)

C-01 through C-23: all mechanisms carried forward from R6 (all PASS in all variations unless noted).
New R7 discriminators in bold.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Read strategy | Step 1a (stated-field extractor role) | Step 1 | Step 1 | Step 1a | Step 1a |
| C-02 Read signals | Step 2 | Step 2 | Step 2 | Step 2 | Step 2 |
| C-03 Delta not inventory | Step 3 stop+name | Step 3 stop+name | Step 3 stop+name | Step 3 stop+name+contrast | Step 3 stop+name+contrast |
| C-04 Typed proposals | Step 6 table | Step 6 table | Step 6 table | Step 6 table | Step 6 table |
| C-05 Confirm gate | Step 8 YES | Step 8 YES | Step 8 YES | Step 8 YES | Step 8 YES |
| C-06 Evidence per change | Step 6 Evidence col | Step 6 Evidence col | Step 6 Evidence col | Step 6 Evidence col | Step 6 Evidence col |
| C-07 Before/after diff | Step 7 | Step 7 | Step 7 | Step 7 | Step 7 |
| C-08 All three types | Step 6 null rows | Step 6 null rows | Step 6 null rows | Step 6 null rows | Step 6 null rows |
| C-09 Namespace gaps | Step 4 (9 by name) | Step 4 (9 by name) | Step 4 (9 by name) | Step 4 (9 by name) | Step 4 (9 by name) |
| C-10 Conflicting signals | Step 5 | Step 5 | Step 5 | Step 5 | Step 5 |
| C-11 Typed confirmation verb | Step 8 YES | Step 8 YES | Step 8 YES | Step 8 YES | Step 8 YES |
| C-12 Explicit no-change rows | Step 6 null rows verbatim | Step 6 null rows verbatim | Step 6 null rows verbatim | Step 6 null rows verbatim | Step 6 null rows verbatim |
| C-13 Inline evidence in diff | Step 7 Evidence col | Step 7 Evidence col | Step 7 Evidence col (+ checkpoint) | Step 7 (+ checkpoint) | Step 7 (+ checkpoint) |
| C-14 Anti-inventory warning | Step 3 stop+name | Step 3 stop+name (named in purpose framing) | Step 3 stop+name | Step 3 stop+name+contrast | Step 3 stop+name+contrast |
| C-15 All 9 namespaces named | Step 4 table | Step 4 table | Step 4 table | Step 4 table | Step 4 table |
| C-16 Two-level traceability | Step 6 Delta Finding + Evidence | Step 6 Delta Finding + Evidence | Step 6 Delta Finding + Evidence | Step 6 Delta Finding + Evidence | Step 6 Delta Finding + Evidence + explicit chain |
| C-17 Explicit no-conflicts | Step 5 null row verbatim | Step 5 null row verbatim | Step 5 null row verbatim | Step 5 null row verbatim | Step 5 null row verbatim |
| C-18 Structured delta format | Step 3 table | Step 3 table | Step 3 table | Step 3 table | Step 3 table |
| C-19 Diff Proposal ID col | Step 7 Proposal col | Step 7 Proposal col | Step 7 Proposal col (committed in checkpoint) | Step 7 (committed in checkpoint) | Step 7 (committed in checkpoint) |
| C-20 Delta Finding col | Step 6 mandatory + null rows | Step 6 mandatory + null rows | Step 6 mandatory + null rows (committed in checkpoint) | Step 6 (committed in checkpoint) | Step 6 (committed in checkpoint) |
| C-21 Column-completeness declaration | PASS: every table | PASS: upfront purpose table + per-table | PASS: proposals + diff checkpoints + other tables | PASS: upfront ★ schema + per-table | PASS: upfront ★ schema + per-table |
| C-22 Active anti-pattern checkpoint | PASS: Step 3 stop+name | PASS: Step 3 stop+name | PASS: Step 3 stop+name | PASS: Step 3 stop+name+contrast + Step 6 checkpoint | PASS: Step 3 stop+name+contrast + Steps 6+7 |
| C-23 Pre-reproduced null templates | PASS: all 6 null outcomes | PASS: all 6 null outcomes | PASS: all 6 null outcomes | PASS: all 6 null outcomes | PASS: all 6 null outcomes |
| **C-24 Unstated assumption extraction** | **PASS: Step 1b with Assumption ID table, "Why this is a delta candidate" col, traceability back-fill** | **PASS: Step 1 unstated assumptions row with "Why this matters" col** | **PASS: Step 1 "What it assumed without naming" row (v6 V-05 mechanism)** | **PASS: Step 1b Assumption Archaeologist role + Likelihood col** | **PASS: Step 1b Assumption Archaeologist role + Likelihood + Contradicted? cols** |
| **C-25 Inertia cost column** | **PASS: "If unchanged" col in Step 6** | **PASS: "If unchanged" col + purpose-framing in preamble** | **PASS: "If unchanged" + Reversibility cols in Step 6** | **PASS: "If unchanged" col in Step 6 + committed at checkpoint** | **PASS: "If unchanged" + Reversibility cols + committed at checkpoint** |
| **C-26 Schema-first priming** | **PARTIAL: per-table declarations but no upfront consolidated schema** | **PASS: upfront output shape table before Step 1** | **PARTIAL: per-table declarations + checkpoints but no upfront ★ schema** | **PASS: upfront ★ schema block before Step 1a** | **PASS: upfront ★ schema block before Step 1a** |
| **C-27 Cascade schema-commitment checkpoints** | **PARTIAL: Step 3 anti-pattern checkpoint only** | **PARTIAL: Step 3 anti-pattern checkpoint only** | **PASS: Step 3 anti-pattern + Step 6 schema verbatim + Step 7 schema verbatim** | **PASS: Step 3 (stop+name+contrast) + Step 6 schema verbatim + Step 7 schema verbatim** | **PASS: Step 3 (stop+name+contrast) + Step 6 schema+null-row verbatim + Step 7 schema verbatim** |

---

## R7 Discriminator Analysis

| Variation | C-24 mechanism | C-25 mechanism | C-26 mechanism | C-27 mechanism | Structural bet |
|-----------|----------------|----------------|----------------|----------------|----------------|
| V-01 | Assumption Archaeologist role + Assumption ID table with "Likelihood" priority col + back-fill obligation in Step 3 | "If unchanged" col | Per-table declarations (C-21) but no upfront ★ schema — C-26 partial | Single anti-pattern checkpoint at Step 3 — C-27 partial | Role sequence reaches deeper into C-24 than a substep; C-26/C-27 partial is the cost |
| V-02 | Step 1 unstated assumptions row + "Why this matters for delta detection" col | "If unchanged" col + consequence-first preamble with purpose-framing for each column | Upfront output shape table before Step 1 — C-26 PASS | Single anti-pattern checkpoint at Step 3 — C-27 partial | Conversational register produces purpose-motivated column fills; C-27 partial is the cost |
| V-03 | Step 1 "What it assumed without naming" row (R6 V-05 mechanism) | "If unchanged" + "Reversibility" cols with three allowed values + guidance sentence distinguishing trajectory from observation | Per-table declarations + checkpoints at proposals + diff but no upfront ★ schema — C-26 partial | PASS: Step 3 + Step 6 + Step 7 checkpoints | Reversibility dimension converts C-25 from current-state description to trajectory claim; C-26 partial is the cost |
| V-04 | Assumption Archaeologist role + Assumption ID table + "Likelihood" col | "If unchanged" col | PASS: upfront ★ schema block before Step 1a | PASS: Step 3 stop+name+contrast + Step 6 schema verbatim + Step 7 schema verbatim | Role sequence (C-24) + schema-first priming (C-26) address independent failure modes: column omission (C-26) and shallow reasoning (role) |
| V-05 | Assumption Archaeologist role + "Likelihood" + "Contradicted?" cols + explicit back-fill obligation | "If unchanged" + "Reversibility" cols + committed at Step 6 checkpoint | PASS: upfront ★ schema block | PASS: Step 3 + Step 6 (schema+null-row commitment) + Step 7; Step 6 checkpoint carries double weight (schema + null-rows) | Full stack — all four v6 criteria + reversibility + A-to-Proposal traceability chain named as navigation obligation |

**Key structural distinctions:**

- **V-01 vs V-04**: V-01 isolates the role-sequence axis without schema-first priming; V-04 combines role sequence with C-26/C-27 full compliance. V-01's C-26 partial will reveal whether role sequence alone achieves C-24 depth; V-04 shows whether combining both closes remaining gaps without sacrificing either.
- **V-02 uniqueness**: The only variation in R7 that uses conversational phrasing throughout. C-21 compliance is achieved via the upfront output-shape table (which also serves C-26) and per-step purpose framing rather than "The following columns are mandatory" declarations. Reviewer can audit whether purpose-motivated compliance produces richer column content than rule-motivated compliance.
- **V-03 uniqueness**: The only variation where the Reversibility column appears. The three-value taxonomy (Reversible / Gets harder / Becomes impossible) creates a discrete claim that the model must reason to — it cannot pattern-match from the delta finding. If V-03 produces distinctly higher-quality "If unchanged" reasoning, that is a C-28 candidate.
- **V-04 vs V-05**: V-04 combines role sequence and schema-first; V-05 adds reversibility, stronger traceability chain obligation, and the Step 6 checkpoint carries double weight (schema + null-row commitment simultaneously). V-05 is the R7 ceiling and the most likely source of excellence signals for Round 8.
- **Where V-01 and V-02 are the weakest on C-26 and C-27**: Both are intentionally partial on the enforcement layer to isolate the depth-layer axes (role sequence and conversational register respectively). Round 7 scoring will show whether depth-layer improvements can be extracted independently of enforcement compliance.
