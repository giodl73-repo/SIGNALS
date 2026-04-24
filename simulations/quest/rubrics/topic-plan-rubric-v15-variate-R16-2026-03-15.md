# topic-plan — Round 16 Variations (v15 rubric)

**Skill**: `topic:plan`
**Rubric**: v15 (C-01–C-49, 295 pts total)
**Date**: 2026-03-15

---

## Round 16 Design Notes

R15 V-01 achieved above-ceiling performance under v14 and established the floor for R16. The v15
upgrade extracted three new aspirational criteria from R15 excellence signals: C-47 (Defense
Register with invalidation conditions, from V-01/V-04), C-48 (Defense basis column in the Defender
Challenge Table, from V-01/V-04), C-49 (signal read-lock gate after inventory step, from V-03).

R16 explores three dimensions orthogonal to R15's three single-axis tests (ante-signal defense,
explanatory prose, per-step micro-gates).

**All R16 variations preserve the R15 V-01 floor:**
- 4-rule COLUMN CONTRACT with symmetric PASS/FAIL pairs per rule (C-42/C-43/C-46)
- Rule 4 as a named CONTRACT rule governing Delta Finding (C-45)
- Step 9 scoped to "non-withdrawn proposals" — exact phrase (C-44)
- Anti-pattern label + PASS/FAIL exhibit written as output at Step 4 (C-22)
- Schema commitment verbatim statements at Step 7 and Step 8 (C-27)
- Defense Register at Step 2b — 3–5 entries, 4 columns, built before any signal is read (C-47)
- `Defense basis` column in Defender Challenge Table citing D-ID or "Newly constructed" (C-48)

**Three single-axis dimensions explored in R16:**

1. **Enforcement axis — Named read-lock artifact (C-49)** — After Step 3a the model produces a
   boxed READ-LOCK declaration as a named, first-class output artifact. The declaration names every
   subsequent step that is lock-scoped, commits to working from the written inventory only, and
   provides an explicit fallback notation for when inventory is insufficient ("inventory gap —
   [field]"). This is structurally stronger than a phase gate header: the read-lock is produced as
   auditable evidence that the constraint was acknowledged, not merely implied by a phase boundary.
   Tests whether making the read-lock a named artifact (not just an implicit phase rule) reduces
   cross-step contamination where the model re-reads signals for "clarification" during Steps 3b–6.

2. **Framing axis — Inertia as co-equal option** — The Status Quo Defender is introduced in the
   preamble as a co-equal design principle, not merely a challenge step. The preamble states: "Every
   proposed change competes against the decision to leave strategy.md unchanged — and that decision
   deserves an equal hearing." Step 7b adds a `Challenge strength` column (Rule 1 enumerated:
   Strong / Moderate / Weak) that the Defender fills before issuing a verdict. Tests whether
   framing the Defender as adversarial-but-principled (rather than procedural) produces stronger
   inertia challenges, higher withdrawal rates, and better-calibrated `Strengthened` verdicts.

3. **Format axis — Narrative-forward execution** — Every analytical step (Steps 2, 3b, 4, 5, 6)
   produces a 2–3 sentence narrative summary of findings before filling the table. The narrative
   must state what was found and why it matters — not describe what the step does. Same schemas,
   same columns, same Contract rules; only the sequencing of narrative vs. table changes. Tests
   whether explicit narrative articulation before tabulation drives better analytical accuracy in
   the `Implicit evidence`, `Strategy assumed`, and `Signal revealed` cells, or whether it adds
   overhead without improving discriminative depth.

| Variation | Axis | Type | Primary R16 target |
|-----------|------|------|--------------------|
| V-01 | Enforcement — named read-lock artifact | Single | Cross-step contamination (C-02, C-49) |
| V-02 | Framing — inertia as co-equal option | Single | Defender challenge quality (C-07, C-08, C-09) |
| V-03 | Format — narrative-forward execution | Single | Analytical depth in assumption + delta steps (C-06, C-16) |
| V-04 | Read-lock + inertia co-equal (V-01 + V-02) | Combination | Enforcement depth + Defender calibration |
| V-05 | Full ceiling: V-01 + V-02 + V-03 + explanatory prose | Combination | Maximum structural depth |

---

## V-01 — Enforcement: Named Read-Lock Artifact

**Axis**: Enforcement — after Step 3a, the model produces a boxed READ-LOCK declaration as an
explicit output artifact before any analysis steps begin. The declaration names every locked step,
commits to working from the written inventory only, and provides an inventory-gap fallback notation.
This is structurally distinct from a phase gate header: the read-lock is produced as a first-class
named artifact with a specific ID (LOCK-1), making it auditable evidence that the constraint was
acknowledged.

**Hypothesis**: In R15 V-03, per-step micro-gates produced above-ceiling behavior (C-49) because
one of the micro-gates explicitly scoped the "no re-reading" constraint to named steps. The C-49
criterion generalizes this: the constraint should be a named artifact, not a gate-header side-effect.
If the read-lock is produced as a first-class artifact with a specific ID, the model has structural
incentive to reference it when filling cells in Steps 3b–6 (e.g., "per LOCK-1, filling from
inventory only"). If incorrect — the lock declaration is produced but not honored, or the
inventory-gap fallback is used to avoid analytical work — the finding is that structural declaration
of the lock is insufficient; what matters is whether the inventory step is thorough enough to make
re-reading unnecessary.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it was written.
Execution is organized into four phases; you must complete each phase and pass its checkpoint gate
before opening the next. The assumption table is a two-phase artifact: extract at Step 2 (Phase 1,
before signal reading), back-fill at Step 3b (Phase 3, after reading). After the Assumption
Archaeologist extracts assumptions, the Strategy Advocate produces a pre-signal Defense Register.
After Step 3a, you will produce a named READ-LOCK artifact before any analysis steps begin — all
subsequent steps work from the written inventory only. After building proposals and running the
Defender challenge, present the confirmed proposal set and wait for YES before writing. Do not
auto-apply.

---

### COLUMN CONTRACT (binding before reading any file)

Four rules govern every table you produce. Read all four before the Output Schema.

**Rule 1 — Enumerated columns**

Any column using a closed value set must declare those values at every point where the column is
named. Select from the declared set only; prose is not a valid value. A cell that contains
paraphrase, conditional prose, or a multi-value selection is treated as empty regardless of content.

*Why this matters*: Typed columns are falsifiable; prose columns are not. An ADD-type proposal and a
REPRIORITIZE-type proposal are structurally different change requests. Mixing types in prose removes
that distinction and makes the proposals table non-auditable.

Rule 1 PASS examples:
- `Type`: `ADD` | `REMOVE` | `REPRIORITIZE`
- `Reversibility`: `(1) Reversible at same cost` | `(2) Gets harder` | `(3) Becomes impossible`
- `Delta candidate?`: `yes` | `no` | `yes — F-01` | `yes — F-03`
- `Consistent with strategy?`: `Yes` | `No` | `Partial`
- `Defender verdict`: `Withdrawn` | `Strengthened` | `Unchanged`

Rule 1 FAIL examples (treated as absent):
- `Type`: "I suggest adding..." | "addition" | "add/remove"
- `Reversibility`: "it will be harder later" | "probably irreversible"
- `Delta candidate?`: "probably yes" | "yes if confirmed"
- `Consistent with strategy?`: "mostly yes" | "it's complicated"
- `Defender verdict`: "maybe we should keep it" | "partially withdrawn" | "conditionally accepted"

**Rule 2 — Column independence**

Before filling any cell, apply this test: *"Can I fill this cell without reading the source
document?"* If yes, the cell is a structural alias and is treated as empty. Applies to every column
but is especially critical for `Implicit evidence`.

*Why this matters*: The `Implicit evidence` column exists to make assumptions auditable. If a
reviewer cannot trace the evidence back to a phrase in strategy.md, the column is not doing its job.

Rule 2 PASS examples for `Implicit evidence`:
- PASS: `"teams run scout before draft"` — specific phrase from strategy.md rationale block
- PASS: `"signal count threshold never defined"` — gap detected as absent in the text
- PASS: `"the phrase 'gather evidence first'"` — verbatim instruction from the document
- PASS: `"no definition of done for this topic appears in the strategy"` — explicit gap notation

Rule 2 FAIL examples for `Implicit evidence` (treated as absent):
- FAIL: `A-01` — the row key; reconstructible without reading the document
- FAIL: `"signals gather evidence"` — restatement in different words
- FAIL: `"see rationale section"` — pointer with no content
- FAIL: `"strategy implies sequencing"` — generic inference not traceable to any phrase

**Rule 3 — Null completeness**

Every mandatory null case must appear in the output. A section that runs and finds nothing is proven
by its null row. A missing section is indistinguishable from a section that was skipped entirely.

*Why this matters*: Auditable absence requires an explicit declaration. Null rows are evidence that
the section ran.

Rule 3 PASS examples:
- Conflict null: `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |` (Rule 3)
- ADD null: `| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |` (Rule 3)
- Delta null: `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |` (Rule 3)

Rule 3 FAIL (treated as section skipped):
- Empty conflict section with no null row
- Proposals table with only ADD rows and no REMOVE / REPRIORITIZE null rows
- Delta step skipped with only "no changes needed" in prose

**Rule 4 — Two-level traceability**

Every proposal must chain from proposal to delta finding to source signal. The `Delta Finding`
column must include the full "Strategy assumed [X] / Signal revealed [Y]" text from the delta step
with the exact finding ID — not just the ID, not just a signal reference.

*Why this matters*: The proposals table should be self-contained. A reviewer should understand why
each change is proposed without returning to the delta section.

Rule 4 PASS examples:
- `F-01: Strategy assumed scout runs before draft / Signal revealed draft completed without scout artifacts`
- `F-03: Strategy assumed no review namespace signals existed / Signal revealed 3 review artifacts unaddressed in strategy`

Rule 4 FAIL examples (treated as absent):
- `F-01` — finding ID only
- `"signal S-01 suggests adding a skill"` — signal reference, no delta structure

---

### Output Schema (read before proceeding to Phase 1)

Every table must conform to this schema. Columns marked ★ are mandatory. All four Contract Rules
apply. Do not omit any ★ column.

**Assumption Table** (5 columns — all independently populated per Rule 2)
| ★ Assumption | ★ Implicit evidence [Rule 2 — PASS: phrase/paraphrase from strategy.md | FAIL: row key / restatement / pointer] | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? [Rule 1: yes / no / yes — F-NN] |

**Defense Register** (Step 2b — built before any signal files are opened; 4 columns)
| ★ Defense ID | ★ Strategic decision | ★ Strongest keep-it argument (pre-signal) | ★ What would invalidate this defense? |

**READ-LOCK Declaration** (Step 3a exit — named artifact; produced once, referenced in locked steps)
> **READ-LOCK LOCK-1 ENGAGED** — Signal files are now closed. Steps 3b, 4, 5, 6, 7, 7b, and 8
> operate from the written inventory above only. Re-reading any signal file during these steps is a
> protocol violation. If a cell cannot be filled from the inventory, write
> `inventory gap — [field name]` and continue. Do not open a signal file to resolve the gap.

**Signal Inventory**
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? [Rule 1: Yes / No / Partial] | ★ Assumption link (A-NN / "stated field" / "none") |

**Delta Findings**
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) | ★ Assumption root (A-NN / "stated field") |

**Namespace Audit**
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |

**Conflict Audit**
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals** (Rules 1 and 4 apply)
| ★ Proposal ID | ★ Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | ★ Change | ★ Delta Finding [Rule 4: full "Strategy assumed X / Signal revealed Y" + ID] | ★ Evidence | ★ If unchanged | ★ Reversibility [Rule 1: (1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible] | ★ Confidence |

**Defender Challenge Table** (Step 7b — Rule 1 applies to `Defender verdict`)
| ★ Proposal ID | ★ Strongest case for no change | ★ Specific cost of changing | ★ Defense basis [D-ID(s) from Step 2b register, or "Newly constructed — no pre-registered defense applies"] | ★ Proposal Architect response | ★ Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

Do not omit any ★ column.

---

### PHASE 1 — Pre-read (Steps 1–2b)

*No signal files may be read during Phase 1. If you encounter a signal file path, do not read it —
log it in the signal inventory during Phase 2 only.*

---

### Step 1 — Role: Stated-Field Extractor

Read `simulations/{topic}/strategy.md`. Extract stated fields only. Do not infer.

| Field | Value |
|-------|-------|
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Stated rationale | |
| Acknowledged gaps | |

---

### Step 2 — Role: Assumption Archaeologist (Extract)

Extract what strategy.md assumed without writing. Scan dimensions:
- (a) Implied audience knowledge level
- (b) Namespace priority ordering assumed without justification
- (c) Signal sufficiency threshold — what "enough signals" means here
- (d) Timeline or sequencing feasibility
- (e) Definition of "done" for this topic

Apply the COLUMN CONTRACT Rule 2 PASS/FAIL exhibit before populating each `Implicit evidence` cell.

Column rules: `Contradicted?` = `[pending]` until Step 3b. `Why it matters` = failure mode if
assumption is wrong. `Delta candidate?` = Rule 1 (`yes` / `no`); update to `yes — F-NN` after
Step 4.

| Assumption | Implicit evidence [Rule 2] | Contradicted by a signal? | Why this matters | Delta candidate? [Rule 1: yes / no] |
|-----------|---------------------------|--------------------------|-----------------|-------------------------------------|
| [most important] | [phrase from strategy.md — Rule 2 test before filling] | [pending] | [failure mode] | yes |

Null case (Rule 3): `| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |`

---

### Step 2b — Role: Strategy Advocate

Produce a pre-signal Defense Register. For each strategic decision identifiable from Steps 1 and 2,
state the strongest argument that decision remains correct regardless of what signals reveal. Produce
3–5 entries. Assign each a Defense ID (D-01, D-02...).

The defense must be articulable without consulting signal content. Do not speculate about what
signals say. The `What would invalidate this defense?` column names the signal type that would
defeat the registered argument.

| Defense ID | Strategic decision | Strongest keep-it argument (pre-signal) | What would invalidate this defense? |
|-----------|-------------------|----------------------------------------|-------------------------------------|
| D-01 | [decision from strategy.md] | [why keeping it is defensible, without reference to signals] | [signal type or finding structure that would defeat this defense] |

Null case: `| D-00 | No strategic decisions identifiable as defensible pre-signal | N/A | N/A |`

---

### PHASE 1 GATE

| Step | Artifact | Complete? |
|------|----------|-----------|
| Step 1 | Stated-field table — all 5 fields populated, no inferred values | Yes / No |
| Step 2 | Assumption table — all rows, all 5 columns, Rule 2 applied to every `Implicit evidence` cell | Yes / No |
| Step 2b | Defense Register — 3–5 entries, all 4 columns, no signal content referenced | Yes / No |

All rows must show "Yes". Declare: **Phase 1 complete. Opening Phase 2 (Read).**

---

### PHASE 2 — Read (Step 3a)

*Phase 1 gate cleared. Signal files may now be read.*

---

### Step 3a — Role: Signal Analyst (Read)

Glob `simulations/{topic}/` recursively. Read every file.

Null case (Rule 3): `> No signals found — strategy.md does not need revision at this time.`

| ID | File | Namespace | Skill | Date | Key Finding | Consistent with strategy? [Rule 1: Yes / No / Partial] | Assumption link |
|----|------|-----------|-------|------|-------------|-------------------------------------------------------|----------------|
| S-01 | | | | | | | |

After completing the inventory, produce the READ-LOCK declaration exactly as shown in the Output
Schema. Assign it ID LOCK-1. All steps from here forward operate from this inventory only.

> **READ-LOCK LOCK-1 ENGAGED** — Signal files are now closed. Steps 3b, 4, 5, 6, 7, 7b, and 8
> operate from the written inventory above only. Re-reading any signal file during these steps is a
> protocol violation. If a cell cannot be filled from the inventory, write
> `inventory gap — [field name]` and continue. Do not open a signal file to resolve the gap.

---

### PHASE 2 GATE

| Step | Artifact | Complete? |
|------|----------|-----------|
| Step 3a | Signal inventory — every file read, all 8 columns populated per row | Yes / No |
| LOCK-1 | READ-LOCK declaration produced with exact text, all steps named | Yes / No |

All rows must show "Yes". Declare: **Phase 2 complete. LOCK-1 active. Opening Phase 3 (Analysis).**

---

### PHASE 3 — Analysis (Steps 3b–6)

*Phase 2 gate cleared. LOCK-1 active. Work only from the inventory built in Phase 2.*
*If a cell cannot be filled from the inventory, write `inventory gap — [field name]`. Do not re-read
signal files.*

---

### Step 3b — Role: Assumption Archaeologist (Back-fill)

Adjudicate each A-NN against the signal inventory (LOCK-1 active — do not re-read signal files).
Replace `[pending]` with one of:
- `Contradicted — S-NN`: cite ID, one sentence
- `Supported — S-NN`: cite ID
- `No signal coverage`

Reproduce full updated assumption table. After Step 4, update `yes` rows to `yes — F-NN`.

---

### Step 4 — Role: Delta Identifier

Stop. Write: (1) the anti-pattern label you are guarding against, and (2) a PASS/FAIL exhibit for
the delta vs. inventory distinction. Then fill the findings table. LOCK-1 active — work from
inventory only.

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root |
|-----------|-----------------|----------------|-----------------|----------------|
| F-01 | | | S-XX | |

Null case (Rule 3): `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |`

After findings, return to Step 3b and update `yes` rows to `yes — F-NN`.

---

### Step 5 — Role: Coverage Auditor

All 9 namespaces by name. Stage-relative, not raw count. LOCK-1 active.

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

LOCK-1 active — work from inventory only.

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

Null case (Rule 3): `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |`

---

### PHASE 3 GATE

| Step | Artifact | Complete? |
|------|----------|-----------|
| Step 3b | Assumption table — all [pending] replaced, yes rows updated to yes — F-NN | Yes / No |
| Step 4 | Delta findings — anti-pattern named, PASS/FAIL exhibit written, findings table complete | Yes / No |
| Step 5 | Namespace audit — all 9 namespaces present | Yes / No |
| Step 6 | Conflict audit — null row present if no conflicts found | Yes / No |
| LOCK-1 | No signal files re-read during Steps 3b–6 (self-certify) | Yes / No |

All rows must show "Yes". Declare: **Phase 3 complete. Opening Phase 4 (Build).**

---

### PHASE 4 — Build (Steps 7–10)

*Phase 3 gate cleared.*

---

### Step 7 — Role: Proposal Architect

Stop. Write this statement verbatim before building the proposals table:

> "Proposals schema committed: Proposal ID ★, Type ★ [Rule 1: ADD / REMOVE / REPRIORITIZE; prose
> not valid], Change ★, Delta Finding ★ [Rule 4: full 'Strategy assumed X / Signal revealed Y'
> text with ID], Evidence ★, If unchanged ★ (no degradation named = preference not decision),
> Reversibility ★ [Rule 1: (1)/(2)/(3); prose not valid], Confidence ★. All three types present.
> Empty types use Rule 3 null rows."

| Proposal ID | Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | Change | Delta Finding [Rule 4] | Evidence | If unchanged [specific degradation] | Reversibility [Rule 1: (1)/(2)/(3)] | Confidence |
|------------|------------------------------------------|--------|----------------------|----------|-------------------------------------|-------------------------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [degradation] | (2) Gets harder | High |

Null rows (Rule 3):

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 7b — Role: Status Quo Defender

Adopt this role: you are the voice of inertia. For each active proposal (non-null rows from
Step 7), articulate the strongest case for leaving strategy.md unchanged. Draw on the Defense
Register from Step 2b — cite the D-ID(s) whose pre-registered argument applies to this proposal's
challenged decision. Name the specific cost of making the change.

| Proposal ID | Strongest case for no change | Specific cost of changing | Defense basis [D-ID(s) or "Newly constructed — no pre-registered defense applies"] | Proposal Architect response | Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |
|------------|------------------------------|--------------------------|------------------------------------------------------------------------------------|----------------------------|----------------------------------------------------------------|
| ADD-1 | [why keeping strategy as-is is defensible] | [concrete cost] | D-01 | [Architect's rebuttal or concession] | Unchanged |

Null case — no active proposals (Rule 3):
`| — | No active proposals — Defender step not applicable | N/A | N/A | N/A | N/A |`

After filling the table:
- Mark `Withdrawn` proposals: add "[WITHDRAWN after Defender step]" note to the original row in
  Step 7. These proposals do not appear in the diff.
- Mark `Strengthened` proposals: update the `If unchanged` cell in Step 7 to reflect the sharpened
  degradation case.
- `Unchanged` proposals: proceed as-is.

---

### Step 8 — Role: Diff Author

Stop. Write this statement verbatim before building the diff table:

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★ (inline
> [file.md — ≤10 words] per row), Proposal ★ (ID from Step 7). No column omitted. Withdrawn
> proposals excluded."

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current text] | [proposed text] | [file.md — ≤10 words] | ADD-1 |

---

### Step 9 — Confirmation gate

Reply **YES** to apply all non-withdrawn proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 10 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed, non-withdrawn proposals.
Preserve existing structure; update only sections affected.

---

## V-02 — Framing: Inertia as Co-Equal Option

**Axis**: Framing — the Status Quo Defender is introduced in the preamble as a co-equal design
principle, not merely a challenge step. The preamble explicitly names the two failure modes for
inertia assessment: (a) rubber-stamp Defender that never withdraws a proposal, (b) over-zealous
Defender that withdraws proposals without genuine cost analysis. Step 7b adds a `Challenge strength`
column (Rule 1 enumerated: Strong / Moderate / Weak) that the Defender fills before issuing a
verdict — forcing explicit calibration of challenge quality before the pass/fail decision.

**Hypothesis**: In R15 V-01/V-04, the Defender is introduced as a step instruction — "Adopt this
role: you are the voice of inertia." The preamble does not name the Defender as a co-equal decision
path. If framing the Defender as co-equal up front (in the preamble, before any steps) causes the
model to invest more analytical effort in challenge construction, the `Challenge strength` column
should distribute across Strong/Moderate/Weak in ways correlated with eventual verdicts. If
incorrect — the preamble framing is overridden by step-level instructions and does not change
Defender behavior — the finding is that role instructions at the step level dominate preamble
framing, and challenge strength declaration is independent of framing context.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it was written.

**A structural principle governs this execution**: every proposed change competes against the
decision to leave strategy.md unchanged — and that decision deserves equal analytical investment.
The Status Quo Defender (Step 7b) is not a procedural check on proposals. It is the voice of the
option you might be discarding. A skill that never withdraws a proposal has not run a genuine
Defender step — it has run a ratification step. A skill that withdraws every proposal on thin
grounds has not honored the delta evidence. The Defender is calibrated when its verdicts are
correlated with the actual strength of the no-change case.

Execution is organized into four phases; you must complete each phase and pass its checkpoint gate
before opening the next. The assumption table is a two-phase artifact: extract at Step 2 (Phase 1,
before signal reading), back-fill at Step 3b (Phase 3, after reading). After the Assumption
Archaeologist extracts assumptions, the Strategy Advocate produces a pre-signal Defense Register.
After building proposals and running the Defender challenge, present the confirmed proposal set and
wait for YES before writing. Do not auto-apply.

---

### COLUMN CONTRACT (binding before reading any file)

Four rules govern every table you produce. Read all four before the Output Schema.

**Rule 1 — Enumerated columns**

Any column using a closed value set must declare those values at every point where the column is
named. Select from the declared set only; prose is not a valid value. A cell that contains
paraphrase, conditional prose, or a multi-value selection is treated as empty regardless of content.

*Why this matters*: Typed columns are falsifiable; prose columns are not. An ADD-type proposal and a
REPRIORITIZE-type proposal are structurally different change requests. Mixing types in prose removes
that distinction and makes the proposals table non-auditable.

Rule 1 PASS examples:
- `Type`: `ADD` | `REMOVE` | `REPRIORITIZE`
- `Reversibility`: `(1) Reversible at same cost` | `(2) Gets harder` | `(3) Becomes impossible`
- `Delta candidate?`: `yes` | `no` | `yes — F-01` | `yes — F-03`
- `Consistent with strategy?`: `Yes` | `No` | `Partial`
- `Defender verdict`: `Withdrawn` | `Strengthened` | `Unchanged`
- `Challenge strength`: `Strong` | `Moderate` | `Weak`

Rule 1 FAIL examples (treated as absent):
- `Type`: "I suggest adding..." | "addition" | "add/remove"
- `Reversibility`: "it will be harder later" | "probably irreversible"
- `Challenge strength`: "fairly strong" | "somewhat weak" | "this is a good challenge"
- `Defender verdict`: "maybe we should keep it" | "partially withdrawn"

**Rule 2 — Column independence**

Before filling any cell, apply this test: *"Can I fill this cell without reading the source
document?"* If yes, the cell is a structural alias and is treated as empty. Applies to every column
but is especially critical for `Implicit evidence`.

*Why this matters*: The `Implicit evidence` column exists to make assumptions auditable. If a
reviewer cannot trace the evidence back to a phrase in strategy.md, the column is not doing its job.

Rule 2 PASS examples for `Implicit evidence`:
- PASS: `"teams run scout before draft"` — specific phrase from strategy.md rationale block
- PASS: `"signal count threshold never defined"` — gap detected as absent in the text
- PASS: `"the phrase 'gather evidence first'"` — verbatim instruction from the document
- PASS: `"no definition of done for this topic appears in the strategy"` — explicit gap notation

Rule 2 FAIL examples for `Implicit evidence` (treated as absent):
- FAIL: `A-01` — the row key; reconstructible without reading the document
- FAIL: `"signals gather evidence"` — restatement in different words
- FAIL: `"see rationale section"` — pointer with no content
- FAIL: `"strategy implies sequencing"` — generic inference not traceable to any phrase

**Rule 3 — Null completeness**

Every mandatory null case must appear in the output. A section that runs and finds nothing is proven
by its null row. A missing section is indistinguishable from a section that was skipped entirely.

Rule 3 PASS examples:
- Conflict null: `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |` (Rule 3)
- ADD null: `| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |` (Rule 3)
- Delta null: `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |` (Rule 3)

Rule 3 FAIL (treated as section skipped):
- Empty conflict section with no null row
- Proposals table with only ADD rows and no REMOVE / REPRIORITIZE null rows
- Delta step skipped with only "no changes needed" in prose

**Rule 4 — Two-level traceability**

Every proposal must chain from proposal to delta finding to source signal. The `Delta Finding`
column must include the full "Strategy assumed [X] / Signal revealed [Y]" text with the exact
finding ID.

Rule 4 PASS examples:
- `F-01: Strategy assumed scout runs before draft / Signal revealed draft completed without scout artifacts`
- `F-03: Strategy assumed no review namespace signals existed / Signal revealed 3 review artifacts unaddressed in strategy`

Rule 4 FAIL examples (treated as absent):
- `F-01` — finding ID only
- `"signal S-01 suggests adding a skill"` — signal reference, no delta structure

---

### Output Schema (read before proceeding to Phase 1)

Every table must conform to this schema. Columns marked ★ are mandatory. All four Contract Rules
apply. Do not omit any ★ column.

**Assumption Table** (5 columns — all independently populated per Rule 2)
| ★ Assumption | ★ Implicit evidence [Rule 2] | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? [Rule 1: yes / no / yes — F-NN] |

**Defense Register** (Step 2b — built before any signal files are opened; 4 columns)
| ★ Defense ID | ★ Strategic decision | ★ Strongest keep-it argument (pre-signal) | ★ What would invalidate this defense? |

**Signal Inventory**
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? [Rule 1: Yes / No / Partial] | ★ Assumption link (A-NN / "stated field" / "none") |

**Delta Findings**
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) | ★ Assumption root (A-NN / "stated field") |

**Namespace Audit**
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |

**Conflict Audit**
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals** (Rules 1 and 4 apply)
| ★ Proposal ID | ★ Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | ★ Change | ★ Delta Finding [Rule 4] | ★ Evidence | ★ If unchanged | ★ Reversibility [Rule 1: (1)/(2)/(3)] | ★ Confidence |

**Defender Challenge Table** (Step 7b — Rules 1 applies to `Challenge strength` and `Defender verdict`)
| ★ Proposal ID | ★ Strongest case for no change | ★ Specific cost of changing | ★ Defense basis [D-ID(s) or "Newly constructed"] | ★ Challenge strength [Rule 1: Strong / Moderate / Weak] | ★ Proposal Architect response | ★ Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

Do not omit any ★ column.

---

### PHASE 1 — Pre-read (Steps 1–2b)

*No signal files may be read during Phase 1.*

---

### Step 1 — Role: Stated-Field Extractor

Read `simulations/{topic}/strategy.md`. Extract stated fields only. Do not infer.

| Field | Value |
|-------|-------|
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Stated rationale | |
| Acknowledged gaps | |

---

### Step 2 — Role: Assumption Archaeologist (Extract)

Extract what strategy.md assumed without writing. Scan dimensions:
- (a) Implied audience knowledge level
- (b) Namespace priority ordering assumed without justification
- (c) Signal sufficiency threshold — what "enough signals" means here
- (d) Timeline or sequencing feasibility
- (e) Definition of "done" for this topic

Apply the Rule 2 PASS/FAIL exhibit before populating each `Implicit evidence` cell.

Column rules: `Contradicted?` = `[pending]` until Step 3b. `Delta candidate?` = Rule 1 (`yes` / `no`);
update to `yes — F-NN` after Step 4.

| Assumption | Implicit evidence [Rule 2] | Contradicted by a signal? | Why this matters | Delta candidate? [Rule 1: yes / no] |
|-----------|---------------------------|--------------------------|-----------------|-------------------------------------|
| [most important] | [phrase from strategy.md — Rule 2 test before filling] | [pending] | [failure mode] | yes |

Null case (Rule 3): `| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |`

---

### Step 2b — Role: Strategy Advocate

Produce a pre-signal Defense Register. For each strategic decision identifiable from Steps 1 and 2,
state the strongest argument that decision remains correct regardless of what signals reveal. Produce
3–5 entries. Assign each a Defense ID (D-01, D-02...).

The defense must be articulable without consulting signal content. The `What would invalidate this
defense?` column names the signal type that would defeat the registered argument — this prepares
the Defender to apply evidence-testing at Step 7b rather than constructing objections from scratch.

| Defense ID | Strategic decision | Strongest keep-it argument (pre-signal) | What would invalidate this defense? |
|-----------|-------------------|----------------------------------------|-------------------------------------|
| D-01 | [decision from strategy.md] | [why keeping it is defensible, without reference to signals] | [signal type or finding structure that would defeat this defense] |

Null case: `| D-00 | No strategic decisions identifiable as defensible pre-signal | N/A | N/A |`

---

### PHASE 1 GATE

| Step | Artifact | Complete? |
|------|----------|-----------|
| Step 1 | Stated-field table — all 5 fields populated, no inferred values | Yes / No |
| Step 2 | Assumption table — all rows, all 5 columns, Rule 2 applied | Yes / No |
| Step 2b | Defense Register — 3–5 entries, all 4 columns, no signal content referenced | Yes / No |

All rows must show "Yes". Declare: **Phase 1 complete. Opening Phase 2 (Read).**

---

### PHASE 2 — Read (Step 3a)

*Phase 1 gate cleared. Signal files may now be read.*

---

### Step 3a — Role: Signal Analyst (Read)

Glob `simulations/{topic}/` recursively. Read every file.

Null case (Rule 3): `> No signals found — strategy.md does not need revision at this time.`

| ID | File | Namespace | Skill | Date | Key Finding | Consistent with strategy? [Rule 1: Yes / No / Partial] | Assumption link |
|----|------|-----------|-------|------|-------------|-------------------------------------------------------|----------------|
| S-01 | | | | | | | |

---

### PHASE 2 GATE

| Step | Artifact | Complete? |
|------|----------|-----------|
| Step 3a | Signal inventory — every file read, all 8 columns populated per row | Yes / No |

All rows must show "Yes". Declare: **Phase 2 complete. Opening Phase 3 (Analysis).**

---

### PHASE 3 — Analysis (Steps 3b–6)

*Phase 2 gate cleared. Work only from the signal inventory built in Phase 2 — do not re-read signal
files during this phase.*

---

### Step 3b — Role: Assumption Archaeologist (Back-fill)

Adjudicate each A-NN against all signals. Replace `[pending]` with one of:
- `Contradicted — S-NN`: cite ID, one sentence
- `Supported — S-NN`: cite ID
- `No signal coverage`

Reproduce full updated assumption table. After Step 4, update `yes` rows to `yes — F-NN`.

---

### Step 4 — Role: Delta Identifier

Stop. Write: (1) the anti-pattern label you are guarding against, and (2) a PASS/FAIL exhibit for
the delta vs. inventory distinction. Then fill the findings table.

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root |
|-----------|-----------------|----------------|-----------------|----------------|
| F-01 | | | S-XX | |

Null case (Rule 3): `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |`

After findings, return to Step 3b and update `yes` rows to `yes — F-NN`.

---

### Step 5 — Role: Coverage Auditor

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

### Step 6 — Role: Conflict Detective

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

Null case (Rule 3): `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |`

---

### PHASE 3 GATE

| Step | Artifact | Complete? |
|------|----------|-----------|
| Step 3b | Assumption table — all [pending] replaced, yes rows updated to yes — F-NN | Yes / No |
| Step 4 | Delta findings — anti-pattern named, PASS/FAIL exhibit written, table complete | Yes / No |
| Step 5 | Namespace audit — all 9 namespaces present | Yes / No |
| Step 6 | Conflict audit — null row present if no conflicts found | Yes / No |

All rows must show "Yes". Declare: **Phase 3 complete. Opening Phase 4 (Build).**

---

### PHASE 4 — Build (Steps 7–10)

*Phase 3 gate cleared.*

---

### Step 7 — Role: Proposal Architect

Stop. Write this statement verbatim before building the proposals table:

> "Proposals schema committed: Proposal ID ★, Type ★ [Rule 1: ADD / REMOVE / REPRIORITIZE; prose
> not valid], Change ★, Delta Finding ★ [Rule 4: full 'Strategy assumed X / Signal revealed Y'
> text with ID], Evidence ★, If unchanged ★ (no degradation named = preference not decision),
> Reversibility ★ [Rule 1: (1)/(2)/(3); prose not valid], Confidence ★. All three types present.
> Empty types use Rule 3 null rows."

| Proposal ID | Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | Change | Delta Finding [Rule 4] | Evidence | If unchanged [specific degradation] | Reversibility [Rule 1: (1)/(2)/(3)] | Confidence |
|------------|------------------------------------------|--------|----------------------|----------|-------------------------------------|-------------------------------------|------------|

Null rows (Rule 3):

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 7b — Role: Status Quo Defender

Recall the structural principle from the preamble: the decision to leave strategy.md unchanged
deserves equal analytical investment as the decision to change it. For each active proposal, your
job is not to argue that the strategy is perfect — it is to articulate the strongest case for not
making this specific change at this time.

Before issuing a verdict, rate the strength of your challenge as Strong, Moderate, or Weak (Rule 1
enumerated). A Strong challenge names a concrete cost that outweighs the gap the proposal closes.
A Moderate challenge names a real cost but cannot clearly demonstrate it outweighs the gap. A Weak
challenge cannot identify a cost beyond generic disruption risk.

Draw on the Defense Register from Step 2b — cite the D-ID(s) whose pre-registered argument applies.
A `Newly constructed` defense is not invalid, but it should be examined: if no pre-registered
defense applies to a major strategic decision, ask why the Advocate missed it.

| Proposal ID | Strongest case for no change | Specific cost of changing | Defense basis [D-ID(s) or "Newly constructed — no pre-registered defense applies"] | Challenge strength [Rule 1: Strong / Moderate / Weak] | Proposal Architect response | Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |
|------------|------------------------------|--------------------------|------------------------------------------------------------------------------------|-------------------------------------------------------|----------------------------|----------------------------------------------------------------|
| ADD-1 | [why keeping strategy as-is is defensible] | [concrete cost] | D-01 | Strong | [Architect's rebuttal] | Unchanged |

Null case — no active proposals (Rule 3):
`| — | No active proposals — Defender step not applicable | N/A | N/A | N/A | N/A | N/A |`

Calibration check: if all verdicts are `Unchanged`, declare "Rubber-stamp audit — re-examine cost
specificity before accepting." If all verdicts are `Withdrawn`, declare "Over-zealous audit — verify
each withdrawal is supported by a concrete cost exceeding the gap."

After filling:
- Mark `Withdrawn` proposals: add "[WITHDRAWN after Defender step]" to Step 7 row.
- Mark `Strengthened` proposals: update `If unchanged` in Step 7.
- `Unchanged` proposals: proceed.

---

### Step 8 — Role: Diff Author

Stop. Write this statement verbatim before building the diff table:

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★ (inline
> [file.md — ≤10 words] per row), Proposal ★ (ID from Step 7). No column omitted. Withdrawn
> proposals excluded."

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current text] | [proposed text] | [file.md — ≤10 words] | ADD-1 |

---

### Step 9 — Confirmation gate

Reply **YES** to apply all non-withdrawn proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 10 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed, non-withdrawn proposals.
Preserve existing structure; update only sections affected.

---

## V-03 — Format: Narrative-Forward Execution

**Axis**: Output format — every analytical step (Steps 2, 3b, 4, 5, 6) produces a 2–3 sentence
narrative summary of findings before filling the table. The narrative states what was found and why
it matters — not what the step does. Same schemas, same columns, same Contract rules. The sequencing
is: narrative first, then table. The narrative is not a description of the step; it is an analytical
claim about the content the table will contain.

**Hypothesis**: Steps 2 and 4 are the most analytically demanding in the skill. The assumption
extraction step requires finding implicit commitments in a document; the delta step requires
distinguishing contradiction from description. If the model must articulate a claim about findings
before filling the table, the claim commits the model to a position before encountering the
structural demands of cell-by-cell filling. This should produce `Implicit evidence` cells with more
specific phrase citations (the narrative forced the phrase to surface) and `Strategy assumed` cells
that name a genuine belief rather than a paraphrase of signal content. If incorrect — the narrative
adds overhead that dilutes the structural discipline of the table, or the narrative claim is
generic and does not constrain table content — the finding is that narrative framing does not
improve analytical depth; table structure alone carries the discriminative work.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it was written.
Execution is organized into four phases; you must complete each phase and pass its checkpoint gate
before opening the next. The assumption table is a two-phase artifact: extract at Step 2 (Phase 1,
before signal reading), back-fill at Step 3b (Phase 3, after reading). After the Assumption
Archaeologist extracts assumptions, the Strategy Advocate produces a pre-signal Defense Register.

**Narrative discipline**: at Steps 2, 3b, 4, 5, and 6, write a 2–3 sentence narrative summary
before filling the table. The narrative must state what you found and why it matters for the
strategy revision — not describe what the step does. A narrative that says "this step extracts
assumptions" is not valid; a narrative that says "strategy.md makes three implicit bets: sequencing
is rigid, the topic stage is early, and signal quality is not yet an issue" is valid. The narrative
is an analytical commitment that the table must then substantiate.

After building proposals and running the Defender challenge, present the confirmed proposal set and
wait for YES before writing. Do not auto-apply.

---

### COLUMN CONTRACT (binding before reading any file)

Four rules govern every table you produce. Read all four before the Output Schema.

**Rule 1 — Enumerated columns**

Any column using a closed value set must declare those values at every point where the column is
named. Select from the declared set only; prose is not a valid value.

Rule 1 PASS examples:
- `Type`: `ADD` | `REMOVE` | `REPRIORITIZE`
- `Reversibility`: `(1) Reversible at same cost` | `(2) Gets harder` | `(3) Becomes impossible`
- `Delta candidate?`: `yes` | `no` | `yes — F-01` | `yes — F-03`
- `Consistent with strategy?`: `Yes` | `No` | `Partial`
- `Defender verdict`: `Withdrawn` | `Strengthened` | `Unchanged`

Rule 1 FAIL examples (treated as absent):
- `Type`: "I suggest adding..." | "addition"
- `Reversibility`: "it will be harder later"
- `Defender verdict`: "maybe we should keep it" | "conditionally accepted"

**Rule 2 — Column independence**

Before filling any cell, apply this test: *"Can I fill this cell without reading the source
document?"* If yes, the cell is a structural alias and is treated as empty.

Rule 2 PASS examples for `Implicit evidence`:
- PASS: `"teams run scout before draft"` — specific phrase from strategy.md rationale block
- PASS: `"signal count threshold never defined"` — gap detected as absent in the text
- PASS: `"the phrase 'gather evidence first'"` — verbatim instruction from the document

Rule 2 FAIL examples for `Implicit evidence` (treated as absent):
- FAIL: `A-01` — the row key
- FAIL: `"signals gather evidence"` — restatement
- FAIL: `"strategy implies sequencing"` — generic inference

**Rule 3 — Null completeness**

Every mandatory null case must appear in the output. A missing section is indistinguishable from a
skipped section.

Rule 3 PASS examples:
- `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |` (Rule 3)
- `| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |` (Rule 3)
- `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |` (Rule 3)

**Rule 4 — Two-level traceability**

Every proposal must include the full "Strategy assumed [X] / Signal revealed [Y]" text with finding
ID in the `Delta Finding` column. Finding ID alone fails.

Rule 4 PASS: `F-01: Strategy assumed scout runs before draft / Signal revealed draft completed without scout artifacts`
Rule 4 FAIL: `F-01` — finding ID only

---

### Output Schema (read before proceeding to Phase 1)

Every table must conform to this schema. Columns marked ★ are mandatory. Narrative precedes table
at Steps 2, 3b, 4, 5, 6. Do not omit any ★ column.

**Assumption Table** (5 columns — narrative precedes table at Step 2 and Step 3b)
| ★ Assumption | ★ Implicit evidence [Rule 2] | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? [Rule 1: yes / no / yes — F-NN] |

**Defense Register** (Step 2b — no narrative required; built before signal reading; 4 columns)
| ★ Defense ID | ★ Strategic decision | ★ Strongest keep-it argument (pre-signal) | ★ What would invalidate this defense? |

**Signal Inventory** (Step 3a — no narrative required; this is a read step, not analysis)
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? [Rule 1: Yes / No / Partial] | ★ Assumption link (A-NN / "stated field" / "none") |

**Delta Findings** (narrative precedes table at Step 4)
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) | ★ Assumption root (A-NN / "stated field") |

**Namespace Audit** (narrative precedes table at Step 5)
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |

**Conflict Audit** (narrative precedes table at Step 6)
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals** (Rules 1 and 4 apply — no narrative requirement)
| ★ Proposal ID | ★ Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | ★ Change | ★ Delta Finding [Rule 4] | ★ Evidence | ★ If unchanged | ★ Reversibility [Rule 1: (1)/(2)/(3)] | ★ Confidence |

**Defender Challenge Table** (Step 7b — Rule 1 applies to `Defender verdict`)
| ★ Proposal ID | ★ Strongest case for no change | ★ Specific cost of changing | ★ Defense basis [D-ID(s) or "Newly constructed — no pre-registered defense applies"] | ★ Proposal Architect response | ★ Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

Do not omit any ★ column.

---

### PHASE 1 — Pre-read (Steps 1–2b)

*No signal files may be read during Phase 1.*

---

### Step 1 — Role: Stated-Field Extractor

Read `simulations/{topic}/strategy.md`. Extract stated fields only. Do not infer. No narrative
required at Step 1.

| Field | Value |
|-------|-------|
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Stated rationale | |
| Acknowledged gaps | |

---

### Step 2 — Role: Assumption Archaeologist (Extract)

**Narrative first (2–3 sentences before the table)**: State what implicit bets strategy.md is
making and why those bets matter for delta detection. Example form: "strategy.md implicitly assumes
[X]. This matters because if [signal type] contradicts it, [failure mode] follows. The most load-
bearing assumption is [Y] because [reason]." Do not describe the step — make a claim about content.

After the narrative, extract assumptions. Scan dimensions:
- (a) Implied audience knowledge level
- (b) Namespace priority ordering assumed without justification
- (c) Signal sufficiency threshold
- (d) Timeline or sequencing feasibility
- (e) Definition of "done" for this topic

Apply Rule 2 PASS/FAIL exhibit before populating each `Implicit evidence` cell.

Column rules: `Contradicted?` = `[pending]` until Step 3b. `Delta candidate?` = `yes` / `no`.

| Assumption | Implicit evidence [Rule 2] | Contradicted by a signal? | Why this matters | Delta candidate? |
|-----------|---------------------------|--------------------------|-----------------|-----------------|
| [most important] | [phrase from strategy.md — Rule 2 test before filling] | [pending] | [failure mode] | yes |

Null case (Rule 3): `| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |`

---

### Step 2b — Role: Strategy Advocate

Produce a pre-signal Defense Register. No narrative required — this is a structured commitment
step, not an analysis step. For each strategic decision identifiable from Steps 1 and 2, state the
strongest argument it remains correct. Produce 3–5 entries. Assign each a Defense ID (D-01...).

| Defense ID | Strategic decision | Strongest keep-it argument (pre-signal) | What would invalidate this defense? |
|-----------|-------------------|----------------------------------------|-------------------------------------|
| D-01 | [decision] | [argument without reference to signals] | [signal type that would defeat it] |

Null case: `| D-00 | No strategic decisions identifiable as defensible pre-signal | N/A | N/A |`

---

### PHASE 1 GATE

| Step | Artifact | Complete? |
|------|----------|-----------|
| Step 1 | Stated-field table — all 5 fields populated, no inferred values | Yes / No |
| Step 2 | Narrative (2–3 sentences, analytical claim) + assumption table, all 5 columns, Rule 2 applied | Yes / No |
| Step 2b | Defense Register — 3–5 entries, all 4 columns, no signal content referenced | Yes / No |

All rows must show "Yes". Declare: **Phase 1 complete. Opening Phase 2 (Read).**

---

### PHASE 2 — Read (Step 3a)

*Phase 1 gate cleared. Signal files may now be read.*

---

### Step 3a — Role: Signal Analyst (Read)

No narrative required at Step 3a — this is a read step, not an analysis step. Glob
`simulations/{topic}/` recursively. Read every file.

Null case (Rule 3): `> No signals found — strategy.md does not need revision at this time.`

| ID | File | Namespace | Skill | Date | Key Finding | Consistent with strategy? [Rule 1: Yes / No / Partial] | Assumption link |
|----|------|-----------|-------|------|-------------|-------------------------------------------------------|----------------|
| S-01 | | | | | | | |

---

### PHASE 2 GATE

| Step | Artifact | Complete? |
|------|----------|-----------|
| Step 3a | Signal inventory — every file read, all 8 columns populated per row | Yes / No |

All rows must show "Yes". Declare: **Phase 2 complete. Opening Phase 3 (Analysis).**

---

### PHASE 3 — Analysis (Steps 3b–6)

*Phase 2 gate cleared. Work only from the inventory built in Phase 2 — do not re-read signal files.*

---

### Step 3b — Role: Assumption Archaeologist (Back-fill)

**Narrative first (2–3 sentences before the updated table)**: State which assumptions were
contradicted, which were supported, and which had no coverage — and what this pattern means for the
delta step. Example: "Two of four assumptions were contradicted by signals (A-02, A-04); the
contradicted assumptions both involve sequencing. This concentration suggests the delta step will
surface sequencing-related findings rather than coverage gaps."

After the narrative, adjudicate each A-NN. Replace `[pending]` with:
- `Contradicted — S-NN`: cite ID, one sentence
- `Supported — S-NN`: cite ID
- `No signal coverage`

Reproduce full updated assumption table. After Step 4, update `yes` rows to `yes — F-NN`.

---

### Step 4 — Role: Delta Identifier

**Narrative first (2–3 sentences before the findings table)**: State the core delta this execution
surfaced — what the strategy assumed, what signals actually revealed, and the strategic implication.
Example: "The strategy assumed two namespaces were sufficient at this stage; signals revealed four
additional namespaces with artifacts. This is not a coverage gap — it is a scope assumption
failure: the strategy committed to a narrower evidence surface than evidence-gathering actually
produced."

Write: (1) the anti-pattern label you are guarding against, and (2) a PASS/FAIL exhibit for the
delta vs. inventory distinction. Then fill the findings table.

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root |
|-----------|-----------------|----------------|-----------------|----------------|
| F-01 | | | S-XX | |

Null case (Rule 3): `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |`

After findings, return to Step 3b and update `yes` rows to `yes — F-NN`.

---

### Step 5 — Role: Coverage Auditor

**Narrative first (2–3 sentences)**: State the overall coverage picture — which namespaces are
appropriately covered given the declared stage, which are thin, and what action this suggests.

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

### Step 6 — Role: Conflict Detective

**Narrative first (2–3 sentences)**: State whether conflicts exist, and if so what they imply about
strategy revision. If no conflicts exist, state that explicitly and explain why the absence is
informative (or not).

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

Null case (Rule 3): `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |`

---

### PHASE 3 GATE

| Step | Artifact | Complete? |
|------|----------|-----------|
| Step 3b | Narrative (2–3 sentences, analytical) + updated assumption table, all [pending] replaced | Yes / No |
| Step 4 | Narrative (2–3 sentences) + anti-pattern named + PASS/FAIL exhibit + findings table | Yes / No |
| Step 5 | Narrative (2–3 sentences) + namespace audit, all 9 namespaces present | Yes / No |
| Step 6 | Narrative (2–3 sentences) + conflict audit, null row present if no conflicts | Yes / No |

All rows must show "Yes". Declare: **Phase 3 complete. Opening Phase 4 (Build).**

---

### PHASE 4 — Build (Steps 7–10)

*Phase 3 gate cleared.*

---

### Step 7 — Role: Proposal Architect

Stop. Write this statement verbatim before building the proposals table:

> "Proposals schema committed: Proposal ID ★, Type ★ [Rule 1: ADD / REMOVE / REPRIORITIZE; prose
> not valid], Change ★, Delta Finding ★ [Rule 4: full 'Strategy assumed X / Signal revealed Y'
> text with ID], Evidence ★, If unchanged ★ (no degradation named = preference not decision),
> Reversibility ★ [Rule 1: (1)/(2)/(3); prose not valid], Confidence ★. All three types present.
> Empty types use Rule 3 null rows."

| Proposal ID | Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | Change | Delta Finding [Rule 4] | Evidence | If unchanged [specific degradation] | Reversibility [Rule 1: (1)/(2)/(3)] | Confidence |
|------------|------------------------------------------|--------|----------------------|----------|-------------------------------------|-------------------------------------|------------|

Null rows (Rule 3):

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 7b — Role: Status Quo Defender

For each active proposal, articulate the strongest case for leaving strategy.md unchanged. Draw on
the Defense Register from Step 2b — cite the D-ID(s) whose pre-registered argument applies. Name
the specific cost of making the change.

| Proposal ID | Strongest case for no change | Specific cost of changing | Defense basis [D-ID(s) or "Newly constructed — no pre-registered defense applies"] | Proposal Architect response | Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |
|------------|------------------------------|--------------------------|------------------------------------------------------------------------------------|----------------------------|----------------------------------------------------------------|

Null case — no active proposals (Rule 3):
`| — | No active proposals — Defender step not applicable | N/A | N/A | N/A | N/A |`

After filling:
- Mark `Withdrawn` proposals: add "[WITHDRAWN after Defender step]" to Step 7 row.
- Mark `Strengthened` proposals: update `If unchanged` in Step 7.
- `Unchanged` proposals: proceed.

---

### Step 8 — Role: Diff Author

Stop. Write this statement verbatim before building the diff table:

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★ (inline
> [file.md — ≤10 words] per row), Proposal ★ (ID from Step 7). No column omitted. Withdrawn
> proposals excluded."

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current text] | [proposed text] | [file.md — ≤10 words] | ADD-1 |

---

### Step 9 — Confirmation gate

Reply **YES** to apply all non-withdrawn proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 10 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed, non-withdrawn proposals.
Preserve existing structure; update only sections affected.

---

## V-04 — Read-Lock + Inertia Co-Equal (V-01 + V-02)

**Axes combined**: V-01 (named read-lock artifact after Step 3a) + V-02 (inertia as co-equal option
with `Challenge strength` column in Step 7b).

**Hypothesis**: V-01's read-lock artifact enforces the signal-analysis boundary; V-02's inertia
framing enforces the proposal-challenge quality boundary. These two axes operate on different failure
modes (contamination vs. rubber-stamping) and should compose without interference. If combined, the
execution should show both: the LOCK-1 artifact appearing after Step 3a, and the `Challenge
strength` column distributing across Strong/Moderate/Weak in ways correlated with verdicts. If
incorrect — one axis dominates and the other produces mechanical compliance without quality gain —
the finding is that enforcement and framing axes do not compose additively; one resets the other.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it was written.
Execution is organized into four phases; you must complete each phase and pass its checkpoint gate
before opening the next. The assumption table is a two-phase artifact: extract at Step 2 (Phase 1,
before signal reading), back-fill at Step 3b (Phase 3, after reading). After the Assumption
Archaeologist extracts assumptions, the Strategy Advocate produces a pre-signal Defense Register.
After Step 3a, you will produce a named READ-LOCK artifact before any analysis steps begin — all
subsequent steps work from the written inventory only.

**A structural principle governs this execution**: every proposed change competes against the
decision to leave strategy.md unchanged — and that decision deserves equal analytical investment.
The Status Quo Defender (Step 7b) is not a procedural check on proposals. It is the voice of the
option you might be discarding. Rate each challenge as Strong, Moderate, or Weak before issuing a
verdict. A skill where every verdict is `Unchanged` has not run a genuine Defender step.

After building proposals and running the Defender challenge, present the confirmed proposal set and
wait for YES before writing. Do not auto-apply.

---

### COLUMN CONTRACT (binding before reading any file)

Four rules govern every table you produce. Read all four before the Output Schema.

**Rule 1 — Enumerated columns**

Any column using a closed value set must declare those values at every point where the column is
named. Select from the declared set only; prose is not a valid value.

Rule 1 PASS examples:
- `Type`: `ADD` | `REMOVE` | `REPRIORITIZE`
- `Reversibility`: `(1) Reversible at same cost` | `(2) Gets harder` | `(3) Becomes impossible`
- `Delta candidate?`: `yes` | `no` | `yes — F-01` | `yes — F-03`
- `Consistent with strategy?`: `Yes` | `No` | `Partial`
- `Defender verdict`: `Withdrawn` | `Strengthened` | `Unchanged`
- `Challenge strength`: `Strong` | `Moderate` | `Weak`

Rule 1 FAIL examples (treated as absent):
- `Type`: "addition" | "add/remove"
- `Challenge strength`: "fairly strong" | "somewhat weak"
- `Defender verdict`: "partially withdrawn" | "conditionally accepted"

**Rule 2 — Column independence**

Before filling any cell, apply this test: *"Can I fill this cell without reading the source
document?"* If yes, the cell is a structural alias and is treated as empty.

Rule 2 PASS examples for `Implicit evidence`:
- PASS: `"teams run scout before draft"` — specific phrase from strategy.md
- PASS: `"signal count threshold never defined"` — explicit absence
- PASS: `"the phrase 'gather evidence first'"` — verbatim

Rule 2 FAIL examples (treated as absent):
- FAIL: `A-01` | `"signals gather evidence"` | `"strategy implies sequencing"`

**Rule 3 — Null completeness**

Every mandatory null case must appear. A missing section is indistinguishable from a skipped section.

Rule 3 PASS:
- `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |`
- `| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |`
- `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |`

**Rule 4 — Two-level traceability**

Every proposal's `Delta Finding` column must include the full "Strategy assumed [X] / Signal
revealed [Y]" text with the exact finding ID.

Rule 4 PASS: `F-01: Strategy assumed scout runs before draft / Signal revealed draft completed without scout artifacts`
Rule 4 FAIL: `F-01` alone | signal reference without delta structure

---

### Output Schema (read before proceeding to Phase 1)

Every table must conform to this schema. Columns marked ★ are mandatory. Do not omit any ★ column.

**Assumption Table**
| ★ Assumption | ★ Implicit evidence [Rule 2] | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? [Rule 1: yes / no / yes — F-NN] |

**Defense Register** (Step 2b — built before any signal files are opened)
| ★ Defense ID | ★ Strategic decision | ★ Strongest keep-it argument (pre-signal) | ★ What would invalidate this defense? |

**READ-LOCK Declaration** (Step 3a exit — first-class artifact)
> **READ-LOCK LOCK-1 ENGAGED** — Signal files are now closed. Steps 3b, 4, 5, 6, 7, 7b, and 8
> operate from the written inventory above only. Re-reading any signal file during these steps is a
> protocol violation. If a cell cannot be filled from the inventory, write
> `inventory gap — [field name]` and continue.

**Signal Inventory**
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? [Rule 1: Yes / No / Partial] | ★ Assumption link |

**Delta Findings**
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) | ★ Assumption root |

**Namespace Audit**
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |

**Conflict Audit**
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals** (Rules 1 and 4 apply)
| ★ Proposal ID | ★ Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | ★ Change | ★ Delta Finding [Rule 4] | ★ Evidence | ★ If unchanged | ★ Reversibility [Rule 1: (1)/(2)/(3)] | ★ Confidence |

**Defender Challenge Table** (Step 7b — Rule 1 applies to `Challenge strength` and `Defender verdict`)
| ★ Proposal ID | ★ Strongest case for no change | ★ Specific cost of changing | ★ Defense basis [D-ID(s) or "Newly constructed"] | ★ Challenge strength [Rule 1: Strong / Moderate / Weak] | ★ Proposal Architect response | ★ Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

Do not omit any ★ column.

---

### PHASE 1 — Pre-read (Steps 1–2b)

*No signal files may be read during Phase 1.*

---

### Step 1 — Role: Stated-Field Extractor

Read `simulations/{topic}/strategy.md`. Extract stated fields only. Do not infer.

| Field | Value |
|-------|-------|
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Stated rationale | |
| Acknowledged gaps | |

---

### Step 2 — Role: Assumption Archaeologist (Extract)

Extract what strategy.md assumed without writing. Scan dimensions (a)–(e). Apply Rule 2 PASS/FAIL
exhibit before each `Implicit evidence` cell.

Column rules: `Contradicted?` = `[pending]`. `Delta candidate?` = `yes` / `no`.

| Assumption | Implicit evidence [Rule 2] | Contradicted by a signal? | Why this matters | Delta candidate? |
|-----------|---------------------------|--------------------------|-----------------|-----------------|
| [most important] | [phrase from strategy.md — Rule 2 test before filling] | [pending] | [failure mode] | yes |

Null case (Rule 3): `| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |`

---

### Step 2b — Role: Strategy Advocate

Produce a pre-signal Defense Register. 3–5 entries. No signal content. Assign D-IDs.

| Defense ID | Strategic decision | Strongest keep-it argument (pre-signal) | What would invalidate this defense? |
|-----------|-------------------|----------------------------------------|-------------------------------------|
| D-01 | [decision] | [argument without signal reference] | [signal type that would defeat it] |

Null case: `| D-00 | No strategic decisions identifiable as defensible pre-signal | N/A | N/A |`

---

### PHASE 1 GATE

| Step | Artifact | Complete? |
|------|----------|-----------|
| Step 1 | Stated-field table — all 5 fields, no inferred values | Yes / No |
| Step 2 | Assumption table — all rows, all 5 columns, Rule 2 applied | Yes / No |
| Step 2b | Defense Register — 3–5 entries, all 4 columns, no signal content | Yes / No |

All rows "Yes". Declare: **Phase 1 complete. Opening Phase 2 (Read).**

---

### PHASE 2 — Read (Step 3a)

*Phase 1 gate cleared. Signal files may now be read.*

---

### Step 3a — Role: Signal Analyst (Read)

Glob `simulations/{topic}/` recursively. Read every file. Build inventory.

Null case (Rule 3): `> No signals found — strategy.md does not need revision at this time.`

| ID | File | Namespace | Skill | Date | Key Finding | Consistent with strategy? [Rule 1: Yes / No / Partial] | Assumption link |
|----|------|-----------|-------|------|-------------|-------------------------------------------------------|----------------|
| S-01 | | | | | | | |

After completing the inventory, produce READ-LOCK LOCK-1:

> **READ-LOCK LOCK-1 ENGAGED** — Signal files are now closed. Steps 3b, 4, 5, 6, 7, 7b, and 8
> operate from the written inventory above only. Re-reading any signal file during these steps is a
> protocol violation. If a cell cannot be filled from the inventory, write
> `inventory gap — [field name]` and continue. Do not open a signal file to resolve the gap.

---

### PHASE 2 GATE

| Step | Artifact | Complete? |
|------|----------|-----------|
| Step 3a | Signal inventory — all files read, all 8 columns populated | Yes / No |
| LOCK-1 | READ-LOCK declaration produced with exact text, all steps named | Yes / No |

All rows "Yes". Declare: **Phase 2 complete. LOCK-1 active. Opening Phase 3 (Analysis).**

---

### PHASE 3 — Analysis (Steps 3b–6)

*LOCK-1 active. Work from inventory only. Use `inventory gap — [field]` if inventory is
insufficient — do not re-read signal files.*

---

### Step 3b — Role: Assumption Archaeologist (Back-fill)

Adjudicate each A-NN from inventory (LOCK-1 active). Replace `[pending]`:
- `Contradicted — S-NN`: ID + one sentence
- `Supported — S-NN`: ID
- `No signal coverage`

Reproduce full updated table. After Step 4, update `yes` to `yes — F-NN`.

---

### Step 4 — Role: Delta Identifier

Stop. Write: (1) anti-pattern label, (2) PASS/FAIL exhibit. LOCK-1 active.

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root |
|-----------|-----------------|----------------|-----------------|----------------|
| F-01 | | | S-XX | |

Null case (Rule 3): `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |`

After findings, return to Step 3b and update `yes` rows to `yes — F-NN`.

---

### Step 5 — Role: Coverage Auditor

All 9 namespaces. Stage-relative. LOCK-1 active.

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

LOCK-1 active.

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

Null case (Rule 3): `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |`

---

### PHASE 3 GATE

| Step | Artifact | Complete? |
|------|----------|-----------|
| Step 3b | Assumption table — all [pending] replaced, yes rows updated to yes — F-NN | Yes / No |
| Step 4 | Delta findings — anti-pattern named, PASS/FAIL exhibit, table complete | Yes / No |
| Step 5 | Namespace audit — all 9 namespaces present | Yes / No |
| Step 6 | Conflict audit — null row present if no conflicts | Yes / No |
| LOCK-1 | No signal files re-read during Steps 3b–6 (self-certify) | Yes / No |

All rows "Yes". Declare: **Phase 3 complete. Opening Phase 4 (Build).**

---

### PHASE 4 — Build (Steps 7–10)

*Phase 3 gate cleared.*

---

### Step 7 — Role: Proposal Architect

Stop. Write verbatim:

> "Proposals schema committed: Proposal ID ★, Type ★ [Rule 1: ADD / REMOVE / REPRIORITIZE; prose
> not valid], Change ★, Delta Finding ★ [Rule 4: full 'Strategy assumed X / Signal revealed Y'
> text with ID], Evidence ★, If unchanged ★ (no degradation named = preference not decision),
> Reversibility ★ [Rule 1: (1)/(2)/(3); prose not valid], Confidence ★. All three types present.
> Empty types use Rule 3 null rows."

| Proposal ID | Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | Change | Delta Finding [Rule 4] | Evidence | If unchanged [specific degradation] | Reversibility [Rule 1: (1)/(2)/(3)] | Confidence |
|------------|------------------------------------------|--------|----------------------|----------|-------------------------------------|-------------------------------------|------------|

Null rows (Rule 3):

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 7b — Role: Status Quo Defender

Recall: every proposed change competes against the decision to leave strategy.md unchanged — that
decision deserves equal analytical investment. For each active proposal, articulate the strongest
no-change case. Rate challenge strength before issuing a verdict. Draw on Defense Register D-IDs.

| Proposal ID | Strongest case for no change | Specific cost of changing | Defense basis [D-ID(s) or "Newly constructed"] | Challenge strength [Rule 1: Strong / Moderate / Weak] | Proposal Architect response | Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |
|------------|------------------------------|--------------------------|------------------------------------------------|-------------------------------------------------------|----------------------------|----------------------------------------------------------------|

Null case (Rule 3):
`| — | No active proposals — Defender step not applicable | N/A | N/A | N/A | N/A | N/A |`

Calibration check: if all verdicts `Unchanged`, declare "Rubber-stamp audit — re-examine cost
specificity." If all verdicts `Withdrawn`, declare "Over-zealous audit — verify each withdrawal."

After filling:
- Mark `Withdrawn` proposals: add "[WITHDRAWN after Defender step]" to Step 7 row.
- Mark `Strengthened` proposals: update `If unchanged` in Step 7.

---

### Step 8 — Role: Diff Author

Stop. Write verbatim:

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★ (inline
> [file.md — ≤10 words] per row), Proposal ★ (ID from Step 7). No column omitted. Withdrawn
> proposals excluded."

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current text] | [proposed text] | [file.md — ≤10 words] | ADD-1 |

---

### Step 9 — Confirmation gate

Reply **YES** to apply all non-withdrawn proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 10 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed, non-withdrawn proposals.
Preserve existing structure; update only sections affected.

---

## V-05 — Full Ceiling: Read-Lock + Inertia Co-Equal + Narrative-Forward + Explanatory Prose

**Axes combined**: V-01 (named read-lock artifact) + V-02 (inertia co-equal framing with
`Challenge strength` column) + V-03 (narrative-forward execution) + explanatory register
(every step opens with what it is doing and why, before the output specification).

**Hypothesis**: V-04 combines enforcement and framing axes. V-05 adds narrative-forward execution
and explanatory register, making every analytical step commit to a claim before filling the table
and grounding every instruction in its purpose. If all four axes are load-bearing and compose
without cancellation, V-05 should produce the highest analytical depth (assumption cells, delta
findings, Defender challenges) across all R16 variations. If incorrect — some axes cancel each
other (e.g., explanatory register dilutes the read-lock's terse authority; narrative claims become
a performance rather than a commitment) — the finding is that axis combinations past three face
diminishing returns or negative interaction effects.

---

You are executing `topic:plan` for the topic `{topic}`.

This skill exists because strategy documents age. The moment signals arrive, the strategy written
before them carries assumptions that may no longer hold. Your job is to find where those assumptions
diverged from what signals actually revealed, and to propose only changes that close a genuine gap
— not changes that reflect preference or completeness for its own sake.

**Two structural principles govern this execution:**

First, the read boundary. The assumption table is built before any signals are read — assumptions
extracted after signal reading will unconsciously mirror signal content. After building the signal
inventory, a named READ-LOCK (LOCK-1) is produced. All analysis steps work from the written
inventory only. If a cell cannot be filled from inventory, write `inventory gap — [field]`. Do not
re-open signal files.

Second, the inertia principle. Every proposed change competes against the decision to leave
strategy.md unchanged — and that decision deserves equal analytical investment. The Status Quo
Defender (Step 7b) rates each challenge as Strong, Moderate, or Weak before issuing a verdict.
A skill where every verdict is `Unchanged` has not run a genuine Defender step. A skill that
withdraws every proposal on thin grounds has not honored the delta evidence.

**Narrative discipline**: at Steps 2, 3b, 4, 5, and 6, write a 2–3 sentence narrative summary
before filling the table. The narrative states what you found and why it matters — not what the
step does.

After building proposals and running the Defender challenge, present the confirmed proposal set and
wait for YES before writing. Do not auto-apply.

---

### COLUMN CONTRACT (binding before reading any file)

The four rules below govern every table you produce. They exist because tables are only auditable
when columns obey structural constraints. Read all four before the Output Schema.

**Rule 1 — Enumerated columns**

The purpose of enumeration is discriminating power. A `Type` column that says `ADD` tells a
reviewer the proposal expands scope. A column that says "I think we should add a skill" tells a
reviewer nothing they can act on without re-interpreting — the column has failed. The rule: any
cell in an enumerated column that contains paraphrase, conditional prose, or a multi-value
selection is treated as empty regardless of content.

Enumerated columns and their permitted values:
- `Type`: `ADD` | `REMOVE` | `REPRIORITIZE`
- `Reversibility`: `(1) Reversible at same cost` | `(2) Gets harder` | `(3) Becomes impossible`
- `Delta candidate?`: `yes` | `no` | `yes — F-01` | `yes — F-03`
- `Consistent with strategy?`: `Yes` | `No` | `Partial`
- `Defender verdict`: `Withdrawn` | `Strengthened` | `Unchanged`
- `Challenge strength`: `Strong` | `Moderate` | `Weak`

Rule 1 PASS: `ADD` | `(2) Gets harder` | `Withdrawn` | `Strong`
Rule 1 FAIL (treated as absent): `"addition"` | `"it will be harder later"` | `"conditionally accepted"` | `"fairly strong"`

**Rule 2 — Column independence**

Before you fill any cell in the assumption table, ask: "Could I fill this cell without opening
strategy.md?" If yes, stop — you are about to write a structural alias. That content reconstructs
information already present elsewhere in the row or schema. It is treated as empty.

This rule is most critical for `Implicit evidence`. That column should contain a specific phrase,
verbatim text, or explicitly-noted absence from strategy.md that a second reviewer could verify
independently.

Rule 2 PASS for `Implicit evidence`:
- `"teams run scout before draft"` — specific phrase; a reviewer can find it
- `"signal count threshold never defined"` — an explicitly-noted gap; its absence is auditable
- `"the phrase 'gather evidence first'"` — verbatim; traceable to a specific location

Rule 2 FAIL (treated as absent):
- `A-01` — the row key; reconstructible without reading
- `"signals gather evidence"` — restatement
- `"strategy implies sequencing"` — generic inference not traceable to any phrase

**Rule 3 — Null completeness**

Every section in this skill is required to produce output — even when it finds nothing. A null row
is not an admission of emptiness; it is a declaration that the section ran and confirmed absence.
The most common violation: the conflict audit left empty when no conflicts exist. The required
output is `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |`. That row
is the evidence that the audit ran.

Rule 3 PASS:
- `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |`
- `| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |`
- `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |`

Rule 3 FAIL (treated as section skipped):
- Empty conflict section
- Proposals table with ADD rows only; REMOVE-0 and REPRIORITIZE-0 absent
- Delta step bypassed with only "no changes needed" in prose

**Rule 4 — Two-level traceability**

The proposals table exists to make strategy changes auditable. A proposal without traceability is a
recommendation — it tells a reviewer what to change but not why. The `Delta Finding` column closes
this gap: embed the full two-level chain in every proposal row: proposal → delta finding → source
signal. The required format is the full "Strategy assumed [X] / Signal revealed [Y]" text from
Step 4, with the exact finding ID.

Rule 4 PASS: `F-01: Strategy assumed scout runs before draft / Signal revealed draft completed without scout artifacts`
Rule 4 FAIL: `F-01` (ID only) | `"signal S-01 suggests adding a skill"` (signal reference only)

---

### Output Schema (read before proceeding to Phase 1)

Every table must conform to this schema. Columns marked ★ are mandatory. Narrative precedes table
at Steps 2, 3b, 4, 5, and 6. Do not omit any ★ column.

**Assumption Table** (narrative precedes at Steps 2 and 3b)
| ★ Assumption | ★ Implicit evidence [Rule 2] | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? [Rule 1: yes / no / yes — F-NN] |

**Defense Register** (Step 2b — built before any signal files are opened; 4 columns)
| ★ Defense ID | ★ Strategic decision | ★ Strongest keep-it argument (pre-signal) | ★ What would invalidate this defense? |

**READ-LOCK Declaration** (Step 3a exit — first-class artifact; produced once)
> **READ-LOCK LOCK-1 ENGAGED** — Signal files are now closed. Steps 3b, 4, 5, 6, 7, 7b, and 8
> operate from the written inventory above only. Re-reading any signal file during these steps is a
> protocol violation. If a cell cannot be filled from the inventory, write
> `inventory gap — [field name]` and continue.

**Signal Inventory** (no narrative — read step, not analysis)
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? [Rule 1: Yes / No / Partial] | ★ Assumption link |

**Delta Findings** (narrative precedes at Step 4)
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) | ★ Assumption root |

**Namespace Audit** (narrative precedes at Step 5)
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |

**Conflict Audit** (narrative precedes at Step 6)
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals** (Rules 1 and 4 apply — no narrative)
| ★ Proposal ID | ★ Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | ★ Change | ★ Delta Finding [Rule 4] | ★ Evidence | ★ If unchanged | ★ Reversibility [Rule 1: (1)/(2)/(3)] | ★ Confidence |

**Defender Challenge Table** (Step 7b — Rule 1 applies to `Challenge strength` and `Defender verdict`)
| ★ Proposal ID | ★ Strongest case for no change | ★ Specific cost of changing | ★ Defense basis [D-ID(s) or "Newly constructed"] | ★ Challenge strength [Rule 1: Strong / Moderate / Weak] | ★ Proposal Architect response | ★ Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

Do not omit any ★ column.

---

### PHASE 1 — Pre-read (Steps 1–2b)

*No signal files may be read during Phase 1. If you encounter a signal file path, do not read it —
log it in the signal inventory during Phase 2 only.*

---

### Step 1 — Role: Stated-Field Extractor

Your first task is to surface only what strategy.md explicitly declares. Open
`simulations/{topic}/strategy.md` and read it in full. Extract these five fields as stated. If a
field is not explicitly present, write "not stated" — do not infer it from surrounding context.
The purpose is to establish a boundary between what the strategy actually commits to and what it
leaves implicit. The assumption extraction step (Step 2) handles what is implicit; this step handles
only what is stated. No narrative required at Step 1.

| Field | Value |
|-------|-------|
| Declared stage | |
| Namespaces covered | |
| Skills planned | |
| Stated rationale | |
| Acknowledged gaps | |

---

### Step 2 — Role: Assumption Archaeologist (Extract)

Now you are looking for what strategy.md assumed without saying. Every strategy document makes
implicit bets. These assumptions are the engine of the delta step: a signal can only constitute a
delta finding if it contradicts something the strategy assumed. If the assumptions are not named
before signal reading, the delta step collapses into inventory.

**Narrative first (2–3 sentences)**: State what implicit bets strategy.md is making and why those
bets matter for delta detection. This is an analytical commitment — not a description of what this
step does.

Scan these five dimensions: (a) implied audience knowledge level, (b) namespace priority ordering
assumed without justification, (c) signal sufficiency threshold, (d) timeline or sequencing
feasibility, (e) definition of "done" for this topic.

Before populating any `Implicit evidence` cell, apply the Rule 2 independence test: "Can I fill
this cell without reading strategy.md?" If yes, stop — find a specific phrase, verbatim text, or
explicitly-noted absence instead.

Column initialization: `Contradicted?` = `[pending]` until Step 3b. `Delta candidate?` = `yes` /
`no`; update `yes` rows to `yes — F-NN` after Step 4.

| Assumption | Implicit evidence [Rule 2] | Contradicted by a signal? | Why this matters | Delta candidate? |
|-----------|---------------------------|--------------------------|-----------------|-----------------|
| [most important] | [phrase from strategy.md — Rule 2 test before filling] | [pending] | [failure mode] | yes |

Null case (Rule 3): `| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |`

---

### Step 2b — Role: Strategy Advocate

This step exists because ante-signal defense is structurally different from post-signal
rationalization. For each strategic decision identifiable from Steps 1 and 2, state the strongest
argument that decision remains correct — before consulting any signal. The defense must be
articulable from the strategy itself. The `What would invalidate this defense?` column is not a
hedge — it is preparation for the Defender step: if the registered defense is invalidated by a
signal, the Defender at Step 7b should say so.

Produce 3–5 entries. Assign each a Defense ID (D-01, D-02...).

| Defense ID | Strategic decision | Strongest keep-it argument (pre-signal) | What would invalidate this defense? |
|-----------|-------------------|----------------------------------------|-------------------------------------|
| D-01 | [decision from strategy.md] | [why keeping it is defensible, without reference to signals] | [signal type or finding structure that would defeat this defense] |

Null case: `| D-00 | No strategic decisions identifiable as defensible pre-signal | N/A | N/A |`

---

### PHASE 1 GATE

| Step | Artifact | Complete? |
|------|----------|-----------|
| Step 1 | Stated-field table — all 5 fields populated, no inferred values | Yes / No |
| Step 2 | Narrative (2–3 sentences, analytical claim) + assumption table, all 5 columns, Rule 2 applied | Yes / No |
| Step 2b | Defense Register — 3–5 entries, all 4 columns, no signal content referenced | Yes / No |

All rows must show "Yes". Declare: **Phase 1 complete. Opening Phase 2 (Read).**

---

### PHASE 2 — Read (Step 3a)

*Phase 1 gate cleared. Signal files may now be read.*

---

### Step 3a — Role: Signal Analyst (Read)

Your job here is documentation, not analysis. Glob `simulations/{topic}/` recursively and read
every file you find. Build a complete inventory of what signals exist, what each reveals, and how
each relates to the strategy and to specific assumptions from Step 2. You will not draw analytical
conclusions here — that comes in Steps 3b and 4. Analysis that happens here, before all signals are
read, is premature and will contaminate the delta step.

Null case (Rule 3): `> No signals found — strategy.md does not need revision at this time.`

Rule 1: `Consistent with strategy?` must be exactly `Yes`, `No`, or `Partial` — not a prose
judgment.

| ID | File | Namespace | Skill | Date | Key Finding | Consistent with strategy? [Rule 1: Yes / No / Partial] | Assumption link |
|----|------|-----------|-------|------|-------------|-------------------------------------------------------|----------------|
| S-01 | | | | | | | |

After completing the inventory, produce READ-LOCK LOCK-1. This is a first-class artifact — produce
it with the exact text shown in the Output Schema. All subsequent steps are locked to the inventory.

> **READ-LOCK LOCK-1 ENGAGED** — Signal files are now closed. Steps 3b, 4, 5, 6, 7, 7b, and 8
> operate from the written inventory above only. Re-reading any signal file during these steps is a
> protocol violation. If a cell cannot be filled from the inventory, write
> `inventory gap — [field name]` and continue. Do not open a signal file to resolve the gap.

---

### PHASE 2 GATE

| Step | Artifact | Complete? |
|------|----------|-----------|
| Step 3a | Signal inventory — every file read, all 8 columns populated per row | Yes / No |
| LOCK-1 | READ-LOCK declaration produced with exact text, all steps named | Yes / No |

All rows "Yes". Declare: **Phase 2 complete. LOCK-1 active. Opening Phase 3 (Analysis).**

---

### PHASE 3 — Analysis (Steps 3b–6)

*LOCK-1 active. Work from inventory only. Use `inventory gap — [field]` if insufficient. Do not
re-read signal files.*

---

### Step 3b — Role: Assumption Archaeologist (Back-fill)

Return to the assumption table from Step 2 and adjudicate each row against the signals in the
inventory. The purpose is to determine which assumptions the evidence supports, which it contradicts,
and which it leaves untested. This determines which rows become delta findings at Step 4.

**Narrative first (2–3 sentences)**: State which assumptions were contradicted, which were supported,
and which had no coverage — and what this pattern implies for the delta step. This is an analytical
commitment, not a description of the back-fill operation.

Replace every `[pending]` cell with one of three values:
- `Contradicted — S-NN`: signal contradicts this assumption; cite the ID and one sentence how
- `Supported — S-NN`: signal corroborates this assumption; cite the ID
- `No signal coverage`: no signal addresses this assumption directly

Reproduce the full updated assumption table. After Step 4, update `yes` rows to `yes — F-NN`.

---

### Step 4 — Role: Delta Identifier

This is the most important analytical step. The delta step finds where strategy and evidence
diverged — not where signals add new information, but where signals contradict something the
strategy assumed. The failure mode is plain inventory: listing what signals say without naming what
the strategy assumed differently. Guard against it explicitly.

**Narrative first (2–3 sentences)**: State the core delta this execution surfaced. What did the
strategy assume, what did signals reveal, and what does the divergence imply for the strategy
revision? This is not a description of what Step 4 does — it is a claim about the content the
findings table will contain. LOCK-1 active — work from inventory only.

Write: (1) the anti-pattern name you are guarding against, and (2) a PASS/FAIL exhibit for the
delta vs. inventory distinction. Then fill the table.

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root |
|-----------|-----------------|----------------|-----------------|----------------|
| F-01 | | | S-XX | |

Null case (Rule 3): `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |`

After completing the table, return to Step 3b and update all `yes` assumption rows to `yes — F-NN`.

---

### Step 5 — Role: Coverage Auditor

Assess signal coverage across all 9 namespaces. Use stage-relative framing: the same signal count
means different things at different stages. "Action Needed?" should reflect whether the current
count is concerning given stage — not simply whether any signals exist. LOCK-1 active.

**Narrative first (2–3 sentences)**: State the overall coverage picture — which namespaces are
appropriately covered, which are thin, and what the pattern implies for strategy revision.

All 9 namespaces must appear. Do not substitute a prose summary.

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

Look for signals that directly contradict each other — not signals that are simply incomplete, but
signals where two artifacts make incompatible claims about the same topic. A conflict has a
strategic implication: the strategy cannot simply defer to signal evidence; it must resolve the
contradiction first. LOCK-1 active.

**Narrative first (2–3 sentences)**: State whether conflicts exist and what they imply. If no
conflicts exist, state that and explain whether the absence is informative.

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

Null case (Rule 3): `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |`

---

### PHASE 3 GATE

| Step | Artifact | Complete? |
|------|----------|-----------|
| Step 3b | Narrative (2–3 sentences) + updated assumption table, all [pending] replaced, yes→yes — F-NN | Yes / No |
| Step 4 | Narrative (2–3 sentences) + anti-pattern + PASS/FAIL exhibit + findings table | Yes / No |
| Step 5 | Narrative (2–3 sentences) + namespace audit, all 9 namespaces present | Yes / No |
| Step 6 | Narrative (2–3 sentences) + conflict audit, null row present if no conflicts | Yes / No |
| LOCK-1 | No signal files re-read during Steps 3b–6 (self-certify) | Yes / No |

All rows "Yes". Declare: **Phase 3 complete. Opening Phase 4 (Build).**

---

### PHASE 4 — Build (Steps 7–10)

*Phase 3 gate cleared.*

---

### Step 7 — Role: Proposal Architect

The proposals table is the deliverable. It should be self-contained: a reviewer should understand
why each change is proposed without returning to any other section. This requires Rule 4 compliance
— the full "Strategy assumed X / Signal revealed Y" text — not a finding ID alone. Every proposal
must be rooted in a delta finding. The `If unchanged` cell must name a specific degradation: what
gap persists or worsens if this proposal is deferred.

Stop. Write this statement verbatim before building the proposals table:

> "Proposals schema committed: Proposal ID ★, Type ★ [Rule 1: ADD / REMOVE / REPRIORITIZE; prose
> not valid], Change ★, Delta Finding ★ [Rule 4: full 'Strategy assumed X / Signal revealed Y'
> text with ID], Evidence ★, If unchanged ★ (no degradation named = preference not decision),
> Reversibility ★ [Rule 1: (1)/(2)/(3); prose not valid], Confidence ★. All three types present.
> Empty types use Rule 3 null rows."

| Proposal ID | Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | Change | Delta Finding [Rule 4] | Evidence | If unchanged [specific degradation] | Reversibility [Rule 1: (1)/(2)/(3)] | Confidence |
|------------|------------------------------------------|--------|----------------------|----------|-------------------------------------|-------------------------------------|------------|

Null rows (Rule 3):

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 7b — Role: Status Quo Defender

Recall the two structural principles from the preamble. First: the decision to leave strategy.md
unchanged deserves equal analytical investment. Second: calibration matters — a skill where every
verdict is `Unchanged` has not run a genuine Defender step; a skill where every verdict is
`Withdrawn` has not honored the delta evidence.

For each active proposal, articulate the strongest no-change case. Draw on the Defense Register
from Step 2b — cite the D-ID(s) whose pre-registered argument applies. If no pre-registered defense
applies, acknowledge that explicitly: the Advocate should have anticipated this decision. Rate
challenge strength before issuing a verdict — not after.

Strong: a concrete cost that clearly outweighs the gap the proposal closes.
Moderate: a real cost that may not clearly outweigh the gap.
Weak: only generic disruption risk; no specific cost named.

| Proposal ID | Strongest case for no change | Specific cost of changing | Defense basis [D-ID(s) or "Newly constructed"] | Challenge strength [Rule 1: Strong / Moderate / Weak] | Proposal Architect response | Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |
|------------|------------------------------|--------------------------|------------------------------------------------|-------------------------------------------------------|----------------------------|----------------------------------------------------------------|
| ADD-1 | [why keeping strategy as-is is defensible] | [concrete cost] | D-01 | Strong | [Architect's rebuttal] | Unchanged |

Null case — no active proposals (Rule 3):
`| — | No active proposals — Defender step not applicable | N/A | N/A | N/A | N/A | N/A |`

Calibration check: if all verdicts `Unchanged`, declare "Rubber-stamp audit — re-examine cost
specificity." If all verdicts `Withdrawn`, declare "Over-zealous audit — verify each withdrawal."

After filling:
- Mark `Withdrawn` proposals: add "[WITHDRAWN after Defender step]" to Step 7 row.
- Mark `Strengthened` proposals: update `If unchanged` in Step 7.

---

### Step 8 — Role: Diff Author

The diff table is the bridge between proposals and strategy.md edits. Every row must carry an
inline evidence citation from the source signal — not a reference to the proposals table, but an
inline bracketed citation. Withdrawn proposals are excluded: the diff reflects the confirmed
proposal set only.

Stop. Write this statement verbatim before building the diff table:

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★ (inline
> [file.md — ≤10 words] per row), Proposal ★ (ID from Step 7). No column omitted. Withdrawn
> proposals excluded."

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current text] | [proposed text] | [file.md — ≤10 words] | ADD-1 |

---

### Step 9 — Confirmation gate

Reply **YES** to apply all non-withdrawn proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 10 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed, non-withdrawn proposals.
Preserve existing structure; update only sections affected.
