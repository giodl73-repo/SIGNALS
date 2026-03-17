# Quest Variate R4 — `topic-retro` (V-01 through V-05)

---

## V-01 — Role Sequence: Echo-Lock-First

**Variation axis**: Role sequence — Echo is identified and frozen in Phase 1, before the signal inventory is opened. Accuracy computation cannot begin until the Echo is in writing.

**Hypothesis**: Requiring the Echo to be stated before reviewing any signal data prevents it from being absorbed post-hoc into the accuracy narrative. When later phases create tension with the locked Echo, the conflict surfaces visibly rather than being silently resolved.

---

You are running a post-commitment signal retrospective for a topic. The retrospective identifies which signals were gathered, how accurate they were, what was missing, and—above all—the single unexpected learning (the Echo) that should change how future signal design works.

### Inputs

- **Topic**: {{topic}}
- **AMEND** (optional): {{amend}}

---

### Phase 1 — Echo Lock *(runs before everything else)*

Before opening any signal inventory or accuracy data, identify the single most unexpected finding from this topic's signal journey. This is the Echo: the thing you did not predict and could not have derived from the signals you planned to gather. It is not a summary of what went wrong — it is the thing that surprised you.

State the Echo now, in the locked block below:

> **ECHO (LOCKED):** [one sentence — the unexpected finding]
> **Phase locked:** 1
> **Revision status:** NO REVISION

The Echo is frozen at the end of Phase 1. Do not revise it when Phases 3 or 4 produce accuracy data or gap findings. If tension arises, record the tension — do not resolve it by silently updating the Echo.

---

### Phase 2 — Signal Inventory

List every signal artifact gathered for this topic before the commitment decision.

If AMEND specifies a signal type or time window, restrict the inventory to that scope and note the constraint at the top of this phase.

| # | Signal Artifact | Namespace | Date Gathered | Pre-Signal Prediction |
|---|----------------|-----------|--------------|----------------------|

---

### Phase 3 — Accuracy Assessment

For each signal in Phase 2, record whether the prediction was Correct (C), Partial (P), or Wrong (W). Compute per-namespace accuracy using the formula: `(C×100 + P×50) / (C + P + W)`.

| Namespace | C | P | W | Accuracy Score |
|-----------|---|---|---|---------------|

After the table, state the overall accuracy verdict — a score, ratio, or qualitative rating — grounded in the per-namespace results above.

---

### Phase 4 — Gap Analysis

Identify signals that were NOT gathered but would have changed the pre-commitment decision. Each gap must name the specific skill to run next time and the specific decision question it would have answered.

| Gap Signal | Namespace | Skill to Run | Decision Question It Would Have Answered |
|-----------|-----------|-------------|----------------------------------------|

Generic advice ("gather more signals") does not count. Name the specific `/skill` and the specific question.

---

### Phase 5 — Conflict Audit *(runs unconditionally)*

This phase runs regardless of whether you perceived tension between the locked Echo and later phases. Review Phases 3 and 4: would the accuracy data or gap findings have led you to revise the Echo?

| Phase | Echo Revision Attempted? | Detail |
|-------|------------------------|--------|
| Phase 3 — Accuracy | NO REVISION | — |
| Phase 4 — Gaps | NO REVISION | — |

If a phase generated tension, change "NO REVISION" to "REVISION ATTEMPTED" and describe what you would have changed and why you preserved the original instead. If no tension arose, the "NO REVISION" entries ARE the explicit no-conflict signal for this retro — do not omit this table or leave it blank.

---

### Output Order

Phases must appear in this order: 1 → 2 → 3 → 4 → 5. Do not reorder phases. The Echo must precede the accuracy table.

### AMEND Behavior

If AMEND is present, apply the scope constraint throughout all phases. Note the constraint at the top of Phase 2.

---

---

## V-02 — Output Format: Formula-in-Header with Worked Example

**Variation axis**: Output format — the per-namespace accuracy column header contains both the scoring formula and a concrete worked example. The header IS the computation instruction; a scorer populating the table cannot miss it.

**Hypothesis**: Embedding `Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=1,W=1 → 62.5]` directly in the column label makes the formula structurally unavoidable. Unlike prose instructions that may be skipped, the header is present at the moment of every cell entry.

---

You are running a post-commitment signal retrospective for a topic. Review which signals were gathered, how accurate they were, what was missing, and what was unexpectedly learned.

### Inputs

- **Topic**: {{topic}}
- **AMEND** (optional): {{amend}}

---

### Step 1 — Echo

Before reviewing signals, identify the single most unexpected finding from this topic's signal journey. The Echo is the thing you did not predict and could not have derived from the signals you planned to gather.

> **Echo:** [one sentence — the unexpected finding]

---

### Step 2 — Signal Inventory

List every signal artifact gathered for this topic. If AMEND limits scope, apply the constraint and note it.

| # | Signal Artifact | Namespace | Date Gathered | Pre-Signal Prediction |
|---|----------------|-----------|--------------|----------------------|

---

### Step 3 — Per-Namespace Accuracy

For each namespace in the inventory, record prediction outcomes (Correct / Partial / Wrong) and compute the accuracy score. **Use the column header exactly as written below — it contains the formula and a worked example.**

| Namespace | C | P | W | Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=1,W=1 → 62.5] |
|-----------|---|---|---|----------------------------------------------------------|

After the table, state the overall accuracy verdict: a score, ratio, or qualitative rating that summarizes the full signal set, grounded in the per-namespace column above.

---

### Step 4 — Gap Analysis

List signals not gathered that would have changed the commitment decision. For each gap, name the specific skill to run and the exact decision question it would have answered. Generic guidance does not pass.

| Gap Signal | Namespace | Skill to Run | Decision Question |
|-----------|-----------|-------------|------------------|

---

### Step 5 — Conflict Audit

This step runs unconditionally. Determine whether the accuracy findings or gap analysis from Steps 3–4 would have led you to revise the Echo from Step 1.

| Step | Echo Revision Attempted? | Detail |
|------|------------------------|--------|
| Step 3 — Accuracy | NO CONFLICT | — |
| Step 4 — Gaps | NO CONFLICT | — |

If a step generated tension, change "NO CONFLICT" to "CONFLICT DETECTED" and describe the tension and why the original Echo was preserved. If no tension arose, the "NO CONFLICT" entries are the explicit no-conflict result for this retro — this table must be present and populated whether or not tension occurred.

---

### AMEND Behavior

Respect AMEND scope throughout all steps. Note the applied constraint beneath the Step 2 heading.

---

---

## V-03 — Lifecycle Emphasis: Explicit Phase Contracts with Incremental Revision Log

**Variation axis**: Lifecycle emphasis — each phase carries an explicit REQUIRES / PRODUCES contract, and a running revision log is established in Phase 1 and updated by each subsequent phase. Phase boundaries are hard; a phase may not proceed until its REQUIRES conditions are satisfied.

**Hypothesis**: Pre-populated revision log cells — each defaulting to NO REVISION — make silence structurally impossible. The log is opened before accuracy data appears; by the time the conflict question arises, the scaffolding is already in place.

---

You are running a post-commitment signal retrospective for a topic. The output has five phases. Each phase has a contract: what it needs as input (REQUIRES) and what it must produce (PRODUCES). Do not skip ahead.

### Inputs

- **Topic**: {{topic}}
- **AMEND** (optional): {{amend}}

---

### Phase 1 — Echo and Revision Log Setup

**REQUIRES:** nothing — this phase runs from memory and intuition alone, before any signal data is reviewed.

**PRODUCES:** a locked Echo statement and an initialized revision log with one row per subsequent phase.

Before opening the signal inventory, state the single most unexpected finding from this topic's signal journey:

> **Echo (locked):** [one sentence]

Now initialize the revision log. Every subsequent phase will fill in its row.

| Phase | Would have changed the Echo? | If yes — what and why |
|-------|-----------------------------|-----------------------|
| Phase 3 — Accuracy | *to be filled by Phase 3* | — |
| Phase 4 — Gaps | *to be filled by Phase 4* | — |

---

### Phase 2 — Signal Inventory

**REQUIRES:** no prior phase output needed.

**PRODUCES:** a complete list of signal artifacts for the topic.

Enumerate every signal gathered before the commitment decision. If AMEND limits scope, note the constraint and apply it.

| # | Signal Artifact | Namespace | Date | Pre-Signal Prediction |
|---|----------------|-----------|------|----------------------|

---

### Phase 3 — Accuracy Assessment

**REQUIRES:** Phase 1 Echo (locked), Phase 2 inventory.

**PRODUCES:** per-namespace accuracy scores, an overall verdict, and a filled-in revision log row for this phase.

Compute per-namespace accuracy using the formula `(C×100 + P×50) / (C + P + W)`.

| Namespace | C | P | W | Accuracy Score |
|-----------|---|---|---|---------------|

**Overall accuracy verdict:** state a score, ratio, or qualitative rating grounded in the per-namespace results.

**Update revision log — Phase 3 row:** Review the locked Echo from Phase 1. Does the accuracy data create tension with it? Fill in the Phase 3 row of the log now:
- If no tension: write `NO REVISION`
- If tension: write `REVISION ATTEMPTED — [what you would have changed and why you preserved the original]`

---

### Phase 4 — Gap Analysis

**REQUIRES:** Phase 2 inventory, Phase 3 accuracy.

**PRODUCES:** actionable gap signals and a filled-in revision log row for this phase.

Identify signals not gathered that would have changed the commitment decision. Name the specific skill and specific decision question for each.

| Gap Signal | Namespace | Skill to Run | Decision Question |
|-----------|-----------|-------------|------------------|

**Update revision log — Phase 4 row:** Does the gap analysis create tension with the locked Echo? Fill in the Phase 4 row now:
- If no tension: write `NO REVISION`
- If tension: write `REVISION ATTEMPTED — [what you would have changed and why you preserved the original]`

---

### Phase 5 — Completed Revision Log and Verdict

**REQUIRES:** all prior phases complete; revision log Phase 3 and Phase 4 rows filled.

**PRODUCES:** the finalized revision log and the retro verdict.

Present the completed revision log:

| Phase | Would have changed the Echo? | If yes — what and why |
|-------|-----------------------------|-----------------------|
| Phase 3 — Accuracy | [from Phase 3] | [from Phase 3] |
| Phase 4 — Gaps | [from Phase 4] | [from Phase 4] |

If both rows say NO REVISION, that is the affirmative no-conflict result. If either row names a tension, that conflict is now a traceable artifact of this retro.

---

### AMEND Behavior

If AMEND is present, apply the scope constraint in Phase 2 (and carry it through Phase 3 and Phase 4). Note the constraint in the Phase 2 header.

---

---

## V-04 — Combination: Echo-Lock + Formula-in-Header + Phase Contracts

**Variation axes**: Role sequence (V-01 Echo-lock) + Output format (V-02 formula-in-header with worked example) + Lifecycle emphasis (V-03 phase contracts + incremental revision log).

**Hypothesis**: Combining three structural mechanisms — Echo frozen before accuracy, formula+example embedded in the column header, and a pre-populated revision log updated by each phase — eliminates the three most common failure modes: post-hoc Echo revision, formula omission, and silent no-conflict signals.

---

You are running a post-commitment signal retrospective for a topic. The output follows a five-phase protocol. Each phase has a contract. The Echo is locked before accuracy data is reviewed. The revision log is initialized in Phase 1 and updated by each subsequent phase.

### Inputs

- **Topic**: {{topic}}
- **AMEND** (optional): {{amend}}

---

### Phase 1 — Echo Lock and Revision Log Initialization

**REQUIRES:** nothing — runs from memory before any signal data is opened.

**PRODUCES:** a locked Echo and a revision log with placeholder rows for Phases 3 and 4.

Identify the single most unexpected finding from this topic's signal journey — the thing you did not predict and could not have derived from the signals you planned:

> **ECHO (LOCKED):** [one sentence]
> **Revision status:** NO REVISION

Initialize the revision log:

| Phase | Echo Revision Attempted? | Detail |
|-------|------------------------|--------|
| Phase 3 — Accuracy | *pending* | — |
| Phase 4 — Gaps | *pending* | — |

---

### Phase 2 — Signal Inventory

**REQUIRES:** Phase 1 complete.

**PRODUCES:** complete signal artifact list.

Enumerate every signal artifact gathered for this topic before the commitment decision. If AMEND limits scope, note the constraint here and apply it throughout.

| # | Signal Artifact | Namespace | Date Gathered | Pre-Signal Prediction |
|---|----------------|-----------|--------------|----------------------|

---

### Phase 3 — Per-Namespace Accuracy

**REQUIRES:** Phase 1 Echo locked, Phase 2 inventory.

**PRODUCES:** per-namespace accuracy table, overall verdict, Phase 3 revision log update.

Record prediction outcomes (Correct / Partial / Wrong) per signal, then compute per-namespace score. **Use the column header exactly as written — it contains the formula and worked example.**

| Namespace | C | P | W | Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=1,W=1 → 62.5] |
|-----------|---|---|---|----------------------------------------------------------|

**Overall accuracy verdict:** state a score, ratio, or qualitative rating grounded in the per-namespace column above.

**Update revision log — Phase 3:** Does the accuracy data create tension with the locked Echo? Replace `*pending*` in the Phase 3 row:
- No tension → `NO REVISION`
- Tension → `REVISION ATTEMPTED — [what you would have revised and why you preserved the original]`

---

### Phase 4 — Gap Analysis

**REQUIRES:** Phase 3 accuracy verdict.

**PRODUCES:** actionable gap signals, Phase 4 revision log update.

Identify signals not gathered that would have changed the commitment decision. Name the specific skill to run and the specific decision question for each.

| Gap Signal | Namespace | Skill to Run | Decision Question It Would Have Answered |
|-----------|-----------|-------------|----------------------------------------|

**Update revision log — Phase 4:** Does the gap analysis create tension with the locked Echo? Replace `*pending*` in the Phase 4 row:
- No tension → `NO REVISION`
- Tension → `REVISION ATTEMPTED — [what you would have revised and why you preserved the original]`

---

### Phase 5 — Finalized Revision Log

**REQUIRES:** Phase 3 and Phase 4 revision log rows filled (no `*pending*` remaining).

**PRODUCES:** the complete, traceable conflict audit for this retro.

Present the finalized revision log:

| Phase | Echo Revision Attempted? | Detail |
|-------|------------------------|--------|
| Phase 3 — Accuracy | [from Phase 3] | [from Phase 3] |
| Phase 4 — Gaps | [from Phase 4] | [from Phase 4] |

Both rows must be filled before this retro is complete. `NO REVISION` in both rows is the affirmative no-conflict result. Do not leave any row as `*pending*` or empty.

---

### AMEND Behavior

If AMEND is present, apply the scope constraint in Phase 2 and carry it through Phases 3 and 4.

---

---

## V-05 — Full Aspirational Sweep: Echo-Lock + Formula-Header + Calibration Trend + Echo-to-Design-Change

**Variation axes**: All V-04 mechanisms + calibration trend (C-09) + Echo-to-design-change translation (C-10). Full aspirational coverage.

**Hypothesis**: A retro that closes the complete learning loop — Echo locked before accuracy, accuracy computed with a visible formula, conflict audited unconditionally, prediction quality compared against prior retros, and the unexpected finding translated into a concrete skill or rubric amendment — produces the highest actionable improvement value for future signal design.

---

You are running a post-commitment signal retrospective for a topic. This retro has six phases. The Echo is locked before any accuracy data is reviewed. The accuracy formula is embedded in the column header. A revision log tracks potential Echo conflicts unconditionally. A calibration section compares this retro to prior retros. The Echo is translated into a concrete design change before the retro closes.

### Inputs

- **Topic**: {{topic}}
- **Prior retro (optional)**: {{prior_retro}} — if available, used for calibration in Phase 5
- **AMEND** (optional): {{amend}}

---

### Phase 1 — Echo Lock and Revision Log Initialization

**Before reviewing any signals**, identify the single most unexpected finding from this topic's signal journey. The Echo is what you did not predict and could not have derived from the signals you planned:

> **ECHO (LOCKED):** [one sentence]
> **Revision status:** NO REVISION

Initialize the revision log:

| Phase | Echo Revision Attempted? | Detail |
|-------|------------------------|--------|
| Phase 3 — Accuracy | *pending* | — |
| Phase 4 — Gaps | *pending* | — |

---

### Phase 2 — Signal Inventory

Enumerate every signal artifact gathered for this topic before the commitment decision. If AMEND limits scope, note the constraint and apply it throughout.

| # | Signal Artifact | Namespace | Date Gathered | Pre-Signal Prediction |
|---|----------------|-----------|--------------|----------------------|

---

### Phase 3 — Per-Namespace Accuracy

Record prediction outcomes (Correct / Partial / Wrong) per signal, grouped by namespace. Compute the accuracy score using the formula in the column header. **Use this header exactly as written.**

| Namespace | C | P | W | Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=1,W=1 → 62.5] |
|-----------|---|---|---|----------------------------------------------------------|

**Overall accuracy verdict:** state a score, ratio, or qualitative rating grounded in the per-namespace column above.

**Update revision log — Phase 3:** Replace `*pending*` in the Phase 3 row: `NO REVISION` if no tension with the locked Echo; `REVISION ATTEMPTED — [what/why preserved]` if tension arose.

---

### Phase 4 — Gap Analysis

Identify signals not gathered that would have changed the commitment decision. Name the specific skill to run and the specific decision question for each.

| Gap Signal | Namespace | Skill to Run | Decision Question It Would Have Answered |
|-----------|-----------|-------------|----------------------------------------|

**Update revision log — Phase 4:** Replace `*pending*` in the Phase 4 row: `NO REVISION` if no tension; `REVISION ATTEMPTED — [what/why preserved]` if tension arose.

---

### Phase 5 — Calibration Trend

Compare this retro's accuracy to any prior retro for the same team or namespace.

If a prior retro is available ({{prior_retro}}):
- State the prior retro's overall accuracy score or verdict
- State this retro's overall accuracy score or verdict
- Identify the direction: **improving**, **degrading**, or **stable**
- Identify which namespace shifted most significantly between retros

If no prior retro is available, mark this phase as N/A and note that this is the first retro for the topic. (N/A counts as pass for scoring purposes.)

---

### Phase 6 — Finalized Audit and Design Change

**6a — Completed Revision Log**

Present the finalized revision log. No row may remain `*pending*`.

| Phase | Echo Revision Attempted? | Detail |
|-------|------------------------|--------|
| Phase 3 — Accuracy | [from Phase 3] | [from Phase 3] |
| Phase 4 — Gaps | [from Phase 4] | [from Phase 4] |

`NO REVISION` in both rows is the affirmative no-conflict result. A `REVISION ATTEMPTED` row is a traceable conflict artifact for this retro.

**6b — Echo-to-Design-Change**

Translate the locked Echo into a concrete change proposal. Choose the form that fits:

| Form | What to specify |
|------|----------------|
| New skill | Skill name, input, output format, which namespace |
| Rubric amendment | Criterion ID, current wording, proposed wording |
| Threshold adjustment | Which threshold, current value, proposed value, signal that triggered this |

The design change must be specific enough that a team could act on it in the next sprint. "We should gather more signals" does not pass — name the exact mechanism.

---

### AMEND Behavior

If AMEND is present, apply the scope constraint in Phase 2 and carry it through Phases 3 and 4. Phases 5 and 6 are not scoped by AMEND — calibration and design change apply to the full topic.

---
