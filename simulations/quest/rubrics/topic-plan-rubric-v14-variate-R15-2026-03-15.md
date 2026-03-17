# topic-plan — Round 15 Variations (v14 rubric)

**Skill**: `topic:plan`
**Rubric**: v14 (C-01–C-46, 280 pts total)
**Date**: 2026-03-15

---

## Round 15 Design Notes

R14 V-01 achieved the highest score under v13 and established the floor for R15. The v14 upgrade added three criteria that R14 V-01 already structurally satisfies: C-44 (withdrawal-aware Step 9), C-45 (Rule 4 in CONTRACT), C-46 (4-rule minimum). R15 explores axes orthogonal to R14's three single-axis tests (lifecycle phase gates, unified exhibit format, pre-emptive warrant Defender).

**All R15 variations preserve the R14 V-01 floor:**
- 4-rule COLUMN CONTRACT with symmetric PASS/FAIL pairs per rule (C-42/C-43/C-46)
- Rule 4 as a named CONTRACT rule governing Delta Finding (C-45)
- Step 9 scoped to "non-withdrawn proposals" — exact phrase (C-44)
- Anti-pattern label + PASS/FAIL exhibit written as output at Step 4 (C-22)
- Schema commitment verbatim statements at Step 7 and Step 8 (C-27)

**Three single-axis dimensions explored in R15:**

1. **Role sequence — ante-signal strategy defense** — A new pre-read role (Strategy Advocate, Step 2b) produces a Defense Register immediately after assumption extraction, before any signal files are opened. Each entry states a strategic decision in strategy.md and the pre-signal argument for keeping it. The Defender Challenge Table gains a `Defense basis` column requiring citation of the registered D-ID or explicit acknowledgment that the defense was newly constructed. Tests whether pre-registering the strategy's case before signal reading produces stronger, less reactive inertia challenges.

2. **Phrasing register — explanatory/descriptive** — All imperative step instructions are rewritten as explanatory prose: every step opens with what it is doing and why it matters before stating the output specification. The COLUMN CONTRACT rules expand their rationale sections. Tests whether comprehension-first framing drives better structural compliance than terse imperative instructions.

3. **Lifecycle emphasis — per-step micro-gates** — A single-row checkpoint after every step replaces macro-phase gates. The model writes a micro-gate declaration before proceeding. Ten granular gates instead of four coarse ones. Tests whether step-level commitment distributes the gating workload more effectively than phase-level commitment.

| Variation | Axis | Type | Primary R15 target |
|-----------|------|------|--------------------|
| V-01 | Role sequence — ante-signal defense | Single | Proposal discrimination quality (C-07, C-08, C-09) |
| V-02 | Phrasing register — explanatory prose | Single | Structural compliance through comprehension |
| V-03 | Lifecycle emphasis — per-step micro-gates | Single | Cross-step contamination and completeness (C-03, C-05) |
| V-04 | Ante-signal defense + explanatory prose (V-01 + V-02) | Combination | Defense depth + comprehension-driven compliance |
| V-05 | Full ceiling: V-01 + V-02 + macro phase gates + unified exhibit | Combination | Maximum structural depth |

---

## V-01 — Role Sequence: Ante-Signal Strategy Defense

**Axis**: Role sequence — a new pre-read role (Strategy Advocate, Step 2b) runs after the Assumption Archaeologist extracts assumptions but before any signal files are opened. The Advocate produces a Defense Register: 3–5 entries, each stating one strategic decision in strategy.md and the strongest pre-signal argument that decision remains correct. Each entry is assigned a Defense ID (D-01, D-02...). The Defender Challenge Table gains a `Defense basis` column: each Defender row must cite the D-ID(s) that support the no-change case, or write "Newly constructed — no pre-registered defense applies."

**Hypothesis**: In R14 V-01, the Defender's challenge at Step 7b is reactive — the Defender sees a completed proposal and constructs an objection under proposal-pressure. Pre-registering the defense before signal reading should produce stronger, more principled inertia challenges because the Advocate's case was built without knowing what signals revealed. If the defense is substantively pre-registered, the Defender in Step 7b applies an existing case rather than improvising a counterfactual. If incorrect — the Defense Register entries are too generic to transfer, or are parroted without genuine challenge improvement — the finding is that pre-registration of defense arguments is not load-bearing for proposal discrimination quality.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it was written. Execution is organized into four phases; you must complete each phase and pass its checkpoint gate before opening the next. The assumption table is a two-phase artifact: extract at Step 2 (Phase 1, before signal reading), back-fill at Step 3b (Phase 3, after reading). After the Assumption Archaeologist extracts assumptions, the Strategy Advocate produces a pre-signal Defense Register. After building proposals and running the Defender challenge, present the confirmed proposal set and wait for YES before writing. Do not auto-apply.

---

### COLUMN CONTRACT (binding before reading any file)

Four rules govern every table you produce. Read all four before the Output Schema.

**Rule 1 — Enumerated columns**

Any column using a closed value set must declare those values at every point where the column is named. Select from the declared set only; prose is not a valid value. A cell that contains paraphrase, conditional prose, or a multi-value selection is treated as empty regardless of content.

*Why this matters*: Typed columns are falsifiable; prose columns are not. An ADD-type proposal and a REPRIORITIZE-type proposal are structurally different change requests. Mixing types in prose removes that distinction and makes the proposals table non-auditable.

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

Before filling any cell, apply this test: *"Can I fill this cell without reading the source document?"* If yes, the cell is a structural alias and is treated as empty. Applies to every column but is especially critical for `Implicit evidence`.

*Why this matters*: The `Implicit evidence` column exists to make assumptions auditable. If a reviewer cannot trace the evidence back to a phrase in strategy.md, the column is not doing its job. A column that can be filled without reading the document is navigational metadata, not an analytical dimension.

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

Every mandatory null case must appear in the output. A section that runs and finds nothing is proven by its null row. A missing section is indistinguishable from a section that was skipped entirely. Every null template in this skill cites Rule 3.

*Why this matters*: Auditable absence requires an explicit declaration. If the Conflict Audit section is empty because no conflicts exist, that is a finding — not a formatting oversight. Null rows are evidence that the section ran.

Rule 3 PASS examples:
- Conflict null: `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |` (Rule 3)
- ADD null: `| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |` (Rule 3)
- Delta null: `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |` (Rule 3)

Rule 3 FAIL (treated as section skipped):
- Empty conflict section with no null row
- Proposals table with only ADD rows and no REMOVE / REPRIORITIZE null rows
- Delta step skipped with only "no changes needed" in prose

**Rule 4 — Two-level traceability**

Every proposal must chain from proposal to delta finding to source signal. The `Delta Finding` column must include the full "Strategy assumed [X] / Signal revealed [Y]" text from the delta step with the exact finding ID — not just the ID, not just a signal reference.

*Why this matters*: The proposals table should be self-contained. A reviewer should understand why each change is proposed without returning to the delta section.

Rule 4 PASS examples:
- `F-01: Strategy assumed scout runs before draft / Signal revealed draft completed without scout artifacts`
- `F-03: Strategy assumed no review namespace signals existed / Signal revealed 3 review artifacts unaddressed in strategy`

Rule 4 FAIL examples (treated as absent):
- `F-01` — finding ID only
- `"signal S-01 suggests adding a skill"` — signal reference, no delta structure

---

### Output Schema (read before proceeding to Phase 1)

Every table must conform to this schema. Columns marked ★ are mandatory. All four Contract Rules apply. Do not omit any ★ column.

**Assumption Table** (5 columns — all independently populated per Rule 2)
| ★ Assumption | ★ Implicit evidence [Rule 2 — PASS: phrase/paraphrase from strategy.md | FAIL: row key / restatement / pointer] | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? [Rule 1: yes / no / yes — F-NN] |

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
| ★ Proposal ID | ★ Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | ★ Change | ★ Delta Finding [Rule 4: full "Strategy assumed X / Signal revealed Y" + ID] | ★ Evidence | ★ If unchanged | ★ Reversibility [Rule 1: (1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible] | ★ Confidence |

**Defender Challenge Table** (Step 7b — Rule 1 applies to `Defender verdict`)
| ★ Proposal ID | ★ Strongest case for no change | ★ Specific cost of changing | ★ Defense basis [D-ID(s) from Step 2b register, or "Newly constructed — no pre-registered defense applies"] | ★ Proposal Architect response | ★ Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

Do not omit any ★ column.

---

### PHASE 1 — Pre-read (Steps 1–2b)

*No signal files may be read during Phase 1. If you encounter a signal file path, do not read it — log it in the signal inventory during Phase 2 only.*

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

Extract what strategy.md assumed without writing. Scan dimensions:
- (a) Implied audience knowledge level
- (b) Namespace priority ordering assumed without justification
- (c) Signal sufficiency threshold — what "enough signals" means here
- (d) Timeline or sequencing feasibility
- (e) Definition of "done" for this topic

Apply the COLUMN CONTRACT Rule 2 PASS/FAIL exhibit before populating each `Implicit evidence` cell.

Column rules: `Contradicted?` = `[pending]` until Step 3b. `Why it matters` = failure mode if assumption is wrong. `Delta candidate?` = Rule 1 (`yes` / `no`); update to `yes — F-NN` after Step 4.

The following columns are mandatory. Do not omit any column.

| Assumption | Implicit evidence [Rule 2] | Contradicted by a signal? | Why this matters | Delta candidate? [Rule 1: yes / no] |
|-----------|---------------------------|--------------------------|-----------------|-------------------------------------|
| [most important] | [phrase from strategy.md — Rule 2 test before filling] | [pending] | [failure mode] | yes |

Null case (Rule 3): `| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |`

---

### Step 2b — Role: Strategy Advocate

Produce a pre-signal Defense Register. For each strategic decision identifiable from Steps 1 and 2, state the strongest argument that decision remains correct regardless of what signals reveal. Produce 3–5 entries. Assign each a Defense ID (D-01, D-02...).

The defense must be articulable without consulting signal content. Do not speculate about what signals say. The `What would invalidate this defense?` column names the signal type that would defeat the registered argument — this prepares the Defender for evidence-testing at Step 7b.

The following columns are mandatory. Do not omit any column.

| Defense ID | Strategic decision | Strongest keep-it argument (pre-signal) | What would invalidate this defense? |
|-----------|-------------------|----------------------------------------|-------------------------------------|
| D-01 | [decision from strategy.md] | [why keeping it is defensible, without reference to signals] | [signal type or finding structure that would defeat this defense] |

Null case: `| D-00 | No strategic decisions identifiable as defensible pre-signal | N/A | N/A |`

---

### PHASE 1 GATE

Produce this checkpoint before advancing to Phase 2. If any item is incomplete, stop and complete it before the gate clears.

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

The following columns are mandatory. Rule 1: `Consistent with strategy?` = Yes / No / Partial.

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

*Phase 2 gate cleared. Work only from the signal inventory built in Phase 2 — do not re-read signal files during this phase.*

---

### Step 3b — Role: Assumption Archaeologist (Back-fill)

Adjudicate each A-NN against all signals. Replace `[pending]` with one of:
- `Contradicted — S-NN`: cite ID, one sentence
- `Supported — S-NN`: cite ID
- `No signal coverage`

Reproduce full updated assumption table. After Step 4, update `yes` rows to `yes — F-NN`.

---

### Step 4 — Role: Delta Identifier

Stop. Write: (1) the anti-pattern label you are guarding against, and (2) a PASS/FAIL exhibit for the delta vs. inventory distinction. Then fill the findings table.

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

### PHASE 3 GATE

| Step | Artifact | Complete? |
|------|----------|-----------|
| Step 3b | Assumption table — all [pending] replaced, yes rows updated to yes — F-NN | Yes / No |
| Step 4 | Delta findings — anti-pattern named, PASS/FAIL exhibit written, findings table complete | Yes / No |
| Step 5 | Namespace audit — all 9 namespaces present | Yes / No |
| Step 6 | Conflict audit — null row present if no conflicts found | Yes / No |

All rows must show "Yes". Declare: **Phase 3 complete. Opening Phase 4 (Build).**

---

### PHASE 4 — Build (Steps 7–10)

*Phase 3 gate cleared.*

---

### Step 7 — Role: Proposal Architect

Stop. Write this statement verbatim before building the proposals table:

> "Proposals schema committed: Proposal ID ★, Type ★ [Rule 1: ADD / REMOVE / REPRIORITIZE; prose not valid], Change ★, Delta Finding ★ [Rule 4: full 'Strategy assumed X / Signal revealed Y' text with ID], Evidence ★, If unchanged ★ (no degradation named = preference not decision), Reversibility ★ [Rule 1: (1)/(2)/(3); prose not valid], Confidence ★. All three types present. Empty types use Rule 3 null rows."

The following columns are mandatory. Do not omit any column.

| Proposal ID | Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | Change | Delta Finding [Rule 4] | Evidence | If unchanged [specific degradation] | Reversibility [Rule 1: (1)/(2)/(3)] | Confidence |
|------------|------------------------------------------|--------|----------------------|----------|-------------------------------------|-------------------------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [degradation] | (2) Gets harder | High |

Null rows (Rule 3):

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 7b — Role: Status Quo Defender

Adopt this role: you are the voice of inertia. For each active proposal (non-null rows from Step 7), articulate the strongest case for leaving strategy.md unchanged. Draw on the Defense Register from Step 2b — cite the D-ID(s) whose pre-registered argument applies to this proposal's challenged decision. Name the specific cost of making the change — migration effort, coherence risk, signal thinness, or premature commitment.

The following columns are mandatory. Do not omit any column. Rule 1 applies to `Defender verdict`.

| Proposal ID | Strongest case for no change | Specific cost of changing | Defense basis [D-ID(s) or "Newly constructed — no pre-registered defense applies"] | Proposal Architect response | Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |
|------------|------------------------------|--------------------------|------------------------------------------------------------------------------------|----------------------------|----------------------------------------------------------------|
| ADD-1 | [why keeping strategy as-is is defensible] | [concrete cost] | D-01 | [Architect's rebuttal or concession] | Unchanged |

Null case — no active proposals (Rule 3):
`| — | No active proposals — Defender step not applicable | N/A | N/A | N/A | N/A |`

After filling the table:
- Mark `Withdrawn` proposals: add "[WITHDRAWN after Defender step]" note to the original row in Step 7. These proposals do not appear in the diff.
- Mark `Strengthened` proposals: update the `If unchanged` cell in Step 7 to reflect the sharpened degradation case.
- `Unchanged` proposals: proceed as-is.

---

### Step 8 — Role: Diff Author

Stop. Write this statement verbatim before building the diff table:

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★ (inline [file.md — ≤10 words] per row), Proposal ★ (ID from Step 7). No column omitted. Withdrawn proposals excluded."

The following columns are mandatory. Withdrawn proposals are excluded.

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current text] | [proposed text] | [file.md — ≤10 words] | ADD-1 |

---

### Step 9 — Confirmation gate

Reply **YES** to apply all non-withdrawn proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 10 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed, non-withdrawn proposals. Preserve existing structure; update only sections affected.

---

## V-02 — Phrasing Register: Explanatory/Descriptive

**Axis**: Phrasing register — all imperative step instructions are rewritten as explanatory prose. Every step opens with what it is doing and why that matters before stating the output specification. The COLUMN CONTRACT rules retain their binding force but lead with comprehension-building rationale. Terse imperatives ("Extract stated fields only. Do not infer.") become purposive explanations ("Your first task is to surface only what strategy.md explicitly declares...").

**Hypothesis**: In R14 V-01, instructions are maximally terse and binding — the model is told what to do with minimal context for why. For models that treat explanation as load-bearing context, the explanatory register may produce better analytical depth: the model understands what failure looks like, not just what output format is expected. If correct, V-02 should produce assumption tables with richer implicit-evidence citations and delta findings with more accurate "Strategy assumed / Signal revealed" structures. If incorrect — the additional prose dilutes the structural binding force of instructions and produces more varied (not more compliant) outputs — the finding is that imperative register is architecturally load-bearing for structural discipline.

---

You are executing `topic:plan` for the topic `{topic}`.

This skill exists because strategy documents age. The moment signals arrive, the strategy written before them carries assumptions that may no longer hold. Your job is to find where those assumptions diverged from what signals actually revealed, and to propose only those changes that close a genuine gap — not changes that simply reflect preference or completeness for its own sake.

A note on ordering: the assumption table is a two-phase artifact. You extract assumptions at Step 2, before reading any signals. You adjudicate them at Step 3b, after reading. This sequencing is not optional — assumptions extracted after signal reading will unconsciously mirror signal content, defeating the purpose of the extraction step.

After building proposals and running the Defender challenge, present the confirmed proposal set and wait for YES before writing. Do not auto-apply.

---

### COLUMN CONTRACT (binding before reading any file)

The four rules below govern every table you produce. They exist because tables are only auditable when columns obey structural constraints. Read all four rules before the Output Schema — they apply at every table you fill, not only the first time you encounter each column.

**Rule 1 — Enumerated columns**

The purpose of enumeration is discriminating power. A `Type` column that says `ADD` tells a reviewer the proposal expands scope. A column that says "I think we should add a skill" tells a reviewer nothing they can act on without re-interpreting — the column has failed. The rule is: any cell in an enumerated column that contains paraphrase, conditional prose, or a multi-value selection is treated as empty regardless of content.

Enumerated columns and their permitted values:
- `Type`: `ADD` | `REMOVE` | `REPRIORITIZE`
- `Reversibility`: `(1) Reversible at same cost` | `(2) Gets harder` | `(3) Becomes impossible`
- `Delta candidate?`: `yes` | `no` | `yes — F-01` | `yes — F-03`
- `Consistent with strategy?`: `Yes` | `No` | `Partial`
- `Defender verdict`: `Withdrawn` | `Strengthened` | `Unchanged`

Rule 1 PASS examples — these are valid values:
- `Type: ADD` — single token from declared set
- `Reversibility: (2) Gets harder` — full enumerated phrase, no paraphrase
- `Defender verdict: Withdrawn` — single declared token

Rule 1 FAIL examples — treated as absent regardless of content:
- `Type: "addition"` — not in declared set
- `Reversibility: "it will be harder later"` — prose, not enumerated phrase
- `Defender verdict: "conditionally accepted"` — not in declared set

**Rule 2 — Column independence**

Before you fill any cell in the assumption table, ask yourself: "Could I fill this cell without opening strategy.md?" If yes, stop — the content you were about to write is a structural alias. It reconstructs information already present elsewhere in the row or schema rather than adding new analytical content. Structural aliases are treated as empty.

This rule is most critical for `Implicit evidence`. That column should contain a specific phrase, verbatim text, or explicitly-noted absence from strategy.md that a second reviewer could verify independently.

Rule 2 PASS examples for `Implicit evidence` — these add content a reviewer can verify:
- `"teams run scout before draft"` — a specific phrase from the rationale block; a reviewer can find it
- `"signal count threshold never defined"` — an explicitly-noted gap; its absence is auditable
- `"the phrase 'gather evidence first'"` — verbatim; traceable to a specific location
- `"no definition of done for this topic appears in the strategy"` — an explicit absence notation

Rule 2 FAIL examples for `Implicit evidence` — treated as absent because they add nothing verifiable:
- `A-01` — the row key; reconstructible without reading the document
- `"signals gather evidence"` — restatement of the assumption in different words
- `"see rationale section"` — pointer with no content
- `"strategy implies sequencing"` — generic inference not traceable to any phrase

**Rule 3 — Null completeness**

Every section in this skill is required to produce output — even when it finds nothing. A null row is not an admission of emptiness; it is a declaration that the section ran and confirmed absence. Without that declaration, a missing section is indistinguishable from a section that was skipped entirely.

The most common violation is the conflict audit: when no conflicts exist, the section is often left empty. The required output is: `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |`. That row is the evidence that the audit ran.

Rule 3 PASS examples — absence is declared:
- `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |` (Rule 3)
- `| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |` (Rule 3)
- `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |` (Rule 3)

Rule 3 FAIL examples — treated as section skipped:
- Empty conflict section with no null row
- Proposals table with ADD rows only; REMOVE-0 and REPRIORITIZE-0 absent
- Delta step bypassed with only "no changes needed" in prose

**Rule 4 — Two-level traceability**

The proposals table exists to make strategy changes auditable. A proposal without traceability is a recommendation — it tells a reviewer what to change but not why. The `Delta Finding` column closes this gap by embedding the full two-level chain in every proposal row: proposal → delta finding → source signal.

The required format is the full "Strategy assumed [X] / Signal revealed [Y]" text from Step 4, with the exact finding ID. The finding ID alone requires the reviewer to look up the delta section. A signal reference alone skips the delta layer. Only the full text makes the proposals table self-contained.

Rule 4 PASS examples — full chain, self-contained:
- `F-01: Strategy assumed scout runs before draft / Signal revealed draft completed without scout artifacts`
- `F-03: Strategy assumed no review namespace signals existed / Signal revealed 3 review artifacts unaddressed in strategy`

Rule 4 FAIL examples — treated as absent because the chain is incomplete:
- `F-01` — finding ID only; reviewer must look up the delta section
- `"signal S-01 suggests adding a skill"` — signal reference only; delta layer missing

---

### Output Schema (read before proceeding to Step 1)

Every table must conform to this schema. Columns marked ★ are mandatory. All four Contract Rules apply. Do not omit any ★ column.

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
| ★ Proposal ID | ★ Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | ★ Change | ★ Delta Finding [Rule 4: full "Strategy assumed X / Signal revealed Y" + ID] | ★ Evidence | ★ If unchanged | ★ Reversibility [Rule 1: (1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible] | ★ Confidence |

**Defender Challenge Table** (Step 7b — Rule 1 applies to `Defender verdict`)
| ★ Proposal ID | ★ Strongest case for no change | ★ Specific cost of changing | ★ Proposal Architect response | ★ Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

Do not omit any ★ column.

---

### Step 1 — Role: Stated-Field Extractor

Your first task is to surface only what strategy.md explicitly declares. Open `simulations/{topic}/strategy.md` and read it in full. Extract these five fields as stated. If a field is not explicitly present, write "not stated" — do not infer it from surrounding context. The purpose of this step is to establish a boundary between what the strategy actually commits to and what it leaves implicit. The assumption extraction step (Step 2) will handle what is implicit; this step handles only what is stated.

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

Now you are looking for what strategy.md assumed without saying. Every strategy document makes implicit bets — about who will be reading it, about which signals will arrive in which order, about what "enough signals" means, about timelines. These assumptions are the engine of the delta step: a signal can only constitute a delta finding if it contradicts something the strategy assumed. If the assumptions are not named before signal reading, the delta step collapses into inventory.

Scan these five dimensions: (a) implied audience knowledge level, (b) namespace priority ordering assumed without justification, (c) signal sufficiency threshold, (d) timeline or sequencing feasibility, (e) definition of "done" for this topic.

Before populating any `Implicit evidence` cell, apply the Rule 2 independence test: "Can I fill this cell without reading strategy.md?" If yes, stop — find a specific phrase, verbatim text, or explicitly-noted absence instead.

Column initialization rules: `Contradicted?` = `[pending]` until Step 3b. `Why it matters` = the failure mode if this assumption is wrong. `Delta candidate?` = Rule 1 (`yes` / `no`); you will update `yes` rows to `yes — F-NN` after Step 4.

The following columns are mandatory. Do not omit any column.

| Assumption | Implicit evidence [Rule 2] | Contradicted by a signal? | Why this matters | Delta candidate? [Rule 1: yes / no] |
|-----------|---------------------------|--------------------------|-----------------|-------------------------------------|
| [most important] | [phrase from strategy.md — Rule 2 test before filling] | [pending] | [failure mode] | yes |

Null case (Rule 3): `| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |`

---

### Step 3a — Role: Signal Analyst (Read)

Now read the signals. Glob `simulations/{topic}/` recursively and read every file you find. Your goal is to build a complete inventory of what signals exist, what each reveals, and how each relates to the strategy and to specific assumptions you identified in Step 2. You will not draw analytical conclusions in this step — that comes in Steps 3b and 4. Here you are documenting.

Null case (Rule 3): `> No signals found — strategy.md does not need revision at this time.`

The following columns are mandatory. Rule 1: `Consistent with strategy?` must be exactly `Yes`, `No`, or `Partial` — not a prose judgment.

| ID | File | Namespace | Skill | Date | Key Finding | Consistent with strategy? [Rule 1: Yes / No / Partial] | Assumption link |
|----|------|-----------|-------|------|-------------|-------------------------------------------------------|----------------|
| S-01 | | | | | | | |

---

### Step 3b — Role: Assumption Archaeologist (Back-fill)

Return to the assumption table from Step 2 and adjudicate each row against the signals you just read. Replace every `[pending]` cell with one of three values:
- `Contradicted — S-NN`: the signal contradicts this assumption; cite the ID and one sentence explaining how
- `Supported — S-NN`: the signal corroborates this assumption; cite the ID
- `No signal coverage`: no signal addresses this assumption directly

Reproduce the full updated assumption table. After you complete Step 4 and have finding IDs, return here and update every `yes` cell in the `Delta candidate?` column to `yes — F-NN`.

---

### Step 4 — Role: Delta Identifier

This is the most important analytical step. Before filling the findings table, you must write two things: (1) the name of the anti-pattern you are guarding against, and (2) a PASS/FAIL exhibit for the delta vs. inventory distinction.

The anti-pattern is called *plain inventory*: listing what signals say without naming what the strategy assumed differently. A plain inventory table has rows like "S-03 discusses namespace X." A delta findings table has rows like "Strategy assumed namespace X would have no signals at this stage / Signal S-03 revealed 4 namespace X artifacts." The test is: does each finding contain a contradiction between a strategy assumption and a signal revelation? If it only describes signal content, it is inventory.

Write the anti-pattern name and PASS/FAIL exhibit before filling any row. Then fill the table.

The following columns are mandatory. Do not omit any column.

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root |
|-----------|-----------------|----------------|-----------------|----------------|
| F-01 | | | S-XX | |

Null case (Rule 3): `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |`

After completing the findings table, return to Step 3b and update all `yes` assumption rows to `yes — F-NN`.

---

### Step 5 — Role: Coverage Auditor

Assess the signal coverage across all 9 namespaces. Use stage-relative framing: a namespace with zero signals at an early stage might be appropriate; the same count at a late stage signals a coverage gap. "Action Needed?" should reflect whether the current count is concerning given stage, not whether any signals exist at all.

All 9 namespaces must appear. Do not substitute a prose summary.

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

Look for signals that directly contradict each other — not signals that are simply incomplete, but signals where two artifacts make incompatible claims about the same topic. A conflict has a strategic implication: it means the strategy cannot simply defer to signal evidence; it must resolve the contradiction first.

If no conflicts exist, you must still produce the null row. Its presence is the evidence that this step ran.

The following columns are mandatory.

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

Null case (Rule 3): `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |`

---

### Step 7 — Role: Proposal Architect

Stop. Write this statement verbatim before building the proposals table:

> "Proposals schema committed: Proposal ID ★, Type ★ [Rule 1: ADD / REMOVE / REPRIORITIZE; prose not valid], Change ★, Delta Finding ★ [Rule 4: full 'Strategy assumed X / Signal revealed Y' text with ID], Evidence ★, If unchanged ★ (no degradation named = preference not decision), Reversibility ★ [Rule 1: (1)/(2)/(3); prose not valid], Confidence ★. All three types present. Empty types use Rule 3 null rows."

Every proposal must be rooted in a delta finding. The `If unchanged` cell must name a specific degradation: what gap persists or worsens if this proposal is deferred? A cell that says "it would be worse" without naming the mechanism fails the decision-qualification test.

The following columns are mandatory. Do not omit any column.

| Proposal ID | Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | Change | Delta Finding [Rule 4] | Evidence | If unchanged [specific degradation] | Reversibility [Rule 1: (1)/(2)/(3)] | Confidence |
|------------|------------------------------------------|--------|----------------------|----------|-------------------------------------|-------------------------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [degradation] | (2) Gets harder | High |

Null rows (Rule 3):

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 7b — Role: Status Quo Defender

Adopt this role: you are the voice of inertia. For each active proposal, your job is not to argue that the strategy is perfect — it is to articulate the strongest case for not making this specific change at this time. Name the concrete cost: migration effort, coherence risk, signal thinness, or premature commitment. A challenge that says "this change might cause problems" is not a cost — name the specific problem and why it outweighs the gap the proposal closes.

The following columns are mandatory. Do not omit any column. Rule 1 applies to `Defender verdict`.

| Proposal ID | Strongest case for no change | Specific cost of changing | Proposal Architect response | Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |
|------------|------------------------------|--------------------------|----------------------------|----------------------------------------------------------------|
| ADD-1 | [why keeping strategy as-is is defensible] | [concrete cost] | [Architect's rebuttal or concession] | Unchanged |

Null case — no active proposals (Rule 3):
`| — | No active proposals — Defender step not applicable | N/A | N/A | N/A |`

After filling the table:
- Mark `Withdrawn` proposals: add "[WITHDRAWN after Defender step]" note to the original row in Step 7. These proposals do not appear in the diff.
- Mark `Strengthened` proposals: update the `If unchanged` cell in Step 7 to reflect the sharpened degradation case.
- `Unchanged` proposals: proceed as-is.

---

### Step 8 — Role: Diff Author

Stop. Write this statement verbatim before building the diff table:

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★ (inline [file.md — ≤10 words] per row), Proposal ★ (ID from Step 7). No column omitted. Withdrawn proposals excluded."

The diff table is the bridge between proposals and strategy.md edits. Every row must carry an inline evidence citation — not a reference to the proposals table, but an inline bracketed citation from the source signal. Withdrawn proposals do not appear here.

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current text] | [proposed text] | [file.md — ≤10 words] | ADD-1 |

---

### Step 9 — Confirmation gate

Reply **YES** to apply all non-withdrawn proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 10 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed, non-withdrawn proposals. Preserve existing structure; update only sections affected.

---

## V-03 — Lifecycle Emphasis: Per-Step Micro-Gates

**Axis**: Lifecycle emphasis — a single-row micro-gate appears after every step. The model must declare each step complete before advancing. Ten granular checkpoints replace four macro-phase gates. Each micro-gate names the exact artifact produced.

**Hypothesis**: R14 V-01's phase gates aggregate commitment to 4 checkpoints; steps within a phase can drift without triggering a gate. Per-step micro-gates distribute the commitment workload across every step boundary. If contamination occurs between steps within a phase, the micro-gate pattern should catch it earlier. If incorrect — micro-gates add overhead without reducing cross-step contamination because the gating declaration is produced mechanically rather than analytically — the finding is that gate frequency is not the load-bearing variable; gate placement relative to contamination risk boundaries is.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it was written. The assumption table is a two-phase artifact: extract at Step 2 (before signal reading), back-fill at Step 3b (after). A micro-gate follows every step — you must complete the gate before advancing. After building proposals and running the Defender challenge, present the confirmed proposal set and wait for YES before writing. Do not auto-apply.

---

### COLUMN CONTRACT (binding before reading any file)

Four rules govern every table you produce. Read all four before the Output Schema.

**Rule 1 — Enumerated columns**

Any column using a closed value set must declare those values at every point where the column is named. Select from the declared set only; prose is not a valid value. A cell that contains paraphrase, conditional prose, or a multi-value selection is treated as empty regardless of content.

*Why this matters*: Typed columns are falsifiable; prose columns are not. Mixing types in prose removes the discriminating power of the column and makes the proposals table non-auditable.

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

Before filling any cell, apply this test: *"Can I fill this cell without reading the source document?"* If yes, the cell is a structural alias and is treated as empty. Applies to every column but is especially critical for `Implicit evidence`.

*Why this matters*: The `Implicit evidence` column exists to make assumptions auditable. A column that can be filled without reading the document is navigational metadata, not an analytical dimension.

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

Every mandatory null case must appear in the output. A section that runs and finds nothing is proven by its null row. A missing section is indistinguishable from a section that was skipped entirely. Every null template in this skill cites Rule 3.

*Why this matters*: Auditable absence requires an explicit declaration. Null rows are evidence that the section ran.

Rule 3 PASS examples:
- Conflict null: `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |` (Rule 3)
- ADD null: `| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |` (Rule 3)
- Delta null: `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |` (Rule 3)

Rule 3 FAIL (treated as section skipped):
- Empty conflict section with no null row
- Proposals table with only ADD rows and no REMOVE / REPRIORITIZE null rows
- Delta step skipped with only "no changes needed" in prose

**Rule 4 — Two-level traceability**

Every proposal must chain from proposal to delta finding to source signal. The `Delta Finding` column must include the full "Strategy assumed [X] / Signal revealed [Y]" text with the exact finding ID.

*Why this matters*: The proposals table should be self-contained. A reviewer should understand why each change is proposed without returning to the delta section.

Rule 4 PASS examples:
- `F-01: Strategy assumed scout runs before draft / Signal revealed draft completed without scout artifacts`
- `F-03: Strategy assumed no review namespace signals existed / Signal revealed 3 review artifacts unaddressed in strategy`

Rule 4 FAIL examples (treated as absent):
- `F-01` — finding ID only
- `"signal S-01 suggests adding a skill"` — signal reference, no delta structure

---

### Output Schema (read before proceeding to Step 1)

Every table must conform to this schema. Columns marked ★ are mandatory. All four Contract Rules apply. Do not omit any ★ column.

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
| ★ Proposal ID | ★ Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | ★ Change | ★ Delta Finding [Rule 4: full "Strategy assumed X / Signal revealed Y" + ID] | ★ Evidence | ★ If unchanged | ★ Reversibility [Rule 1: (1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible] | ★ Confidence |

**Defender Challenge Table** (Step 7b — Rule 1 applies to `Defender verdict`)
| ★ Proposal ID | ★ Strongest case for no change | ★ Specific cost of changing | ★ Proposal Architect response | ★ Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |

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

> **Micro-gate 1**: Step 1 complete — stated-field table produced, all 5 fields populated, no inferred values. Advancing to Step 2.

*No signal files may be read before Micro-gate 3 clears.*

---

### Step 2 — Role: Assumption Archaeologist (Extract)

Extract what strategy.md assumed without writing. Scan dimensions: (a) implied audience knowledge, (b) namespace priority ordering, (c) signal sufficiency threshold, (d) timeline feasibility, (e) definition of done.

Apply the COLUMN CONTRACT Rule 2 PASS/FAIL exhibit before populating each `Implicit evidence` cell. `Contradicted?` = `[pending]` until Step 3b. `Delta candidate?` = Rule 1 (`yes` / `no`); update to `yes — F-NN` after Step 4.

The following columns are mandatory. Do not omit any column.

| Assumption | Implicit evidence [Rule 2] | Contradicted by a signal? | Why this matters | Delta candidate? [Rule 1: yes / no] |
|-----------|---------------------------|--------------------------|-----------------|-------------------------------------|
| [most important] | [phrase from strategy.md — Rule 2 test before filling] | [pending] | [failure mode] | yes |

Null case (Rule 3): `| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |`

> **Micro-gate 2**: Step 2 complete — assumption table produced, all rows, all 5 columns, Rule 2 applied to every `Implicit evidence` cell, all `Contradicted?` cells = `[pending]`. Advancing to Step 3a.

---

### Step 3a — Role: Signal Analyst (Read)

Glob `simulations/{topic}/` recursively. Read every file.

Null case (Rule 3): `> No signals found — strategy.md does not need revision at this time.`

The following columns are mandatory. Rule 1: `Consistent with strategy?` = Yes / No / Partial.

| ID | File | Namespace | Skill | Date | Key Finding | Consistent with strategy? [Rule 1: Yes / No / Partial] | Assumption link |
|----|------|-----------|-------|------|-------------|-------------------------------------------------------|----------------|
| S-01 | | | | | | | |

> **Micro-gate 3**: Step 3a complete — signal inventory produced, every file read, all 8 columns populated per row. Advancing to Step 3b.

*Signal files may not be re-read after this gate. All analysis from Step 3b onward works from the inventory above.*

---

### Step 3b — Role: Assumption Archaeologist (Back-fill)

Adjudicate each A-NN against all signals. Replace `[pending]` with one of:
- `Contradicted — S-NN`: cite ID, one sentence
- `Supported — S-NN`: cite ID
- `No signal coverage`

Reproduce full updated assumption table. After Step 4, update `yes` rows to `yes — F-NN`.

> **Micro-gate 3b**: Step 3b complete — all `[pending]` cells replaced, full assumption table reproduced. Advancing to Step 4.

---

### Step 4 — Role: Delta Identifier

Stop. Write: (1) the anti-pattern label you are guarding against, and (2) a PASS/FAIL exhibit for the delta vs. inventory distinction. Then fill the findings table.

The following columns are mandatory. Do not omit any column.

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root |
|-----------|-----------------|----------------|-----------------|----------------|
| F-01 | | | S-XX | |

Null case (Rule 3): `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |`

After findings, return to Step 3b and update `yes` rows to `yes — F-NN`.

> **Micro-gate 4**: Step 4 complete — anti-pattern label written as output, PASS/FAIL exhibit written, findings table complete, Step 3b `yes` rows updated to `yes — F-NN`. Advancing to Step 5.

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

> **Micro-gate 5**: Step 5 complete — namespace audit produced, all 9 namespaces present. Advancing to Step 6.

---

### Step 6 — Role: Conflict Detective

The following columns are mandatory.

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

Null case (Rule 3): `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |`

> **Micro-gate 6**: Step 6 complete — conflict audit produced, null row present if no conflicts found. Advancing to Step 7.

---

### Step 7 — Role: Proposal Architect

Stop. Write this statement verbatim before building the proposals table:

> "Proposals schema committed: Proposal ID ★, Type ★ [Rule 1: ADD / REMOVE / REPRIORITIZE; prose not valid], Change ★, Delta Finding ★ [Rule 4: full 'Strategy assumed X / Signal revealed Y' text with ID], Evidence ★, If unchanged ★ (no degradation named = preference not decision), Reversibility ★ [Rule 1: (1)/(2)/(3); prose not valid], Confidence ★. All three types present. Empty types use Rule 3 null rows."

The following columns are mandatory. Do not omit any column.

| Proposal ID | Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | Change | Delta Finding [Rule 4] | Evidence | If unchanged [specific degradation] | Reversibility [Rule 1: (1)/(2)/(3)] | Confidence |
|------------|------------------------------------------|--------|----------------------|----------|-------------------------------------|-------------------------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [degradation] | (2) Gets harder | High |

Null rows (Rule 3):

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

> **Micro-gate 7**: Step 7 complete — schema commitment statement written verbatim, proposals table complete, all three type rows present (active or null). Advancing to Step 7b.

---

### Step 7b — Role: Status Quo Defender

Adopt this role: you are the voice of inertia. For each active proposal (non-null rows from Step 7), articulate the strongest case for leaving strategy.md unchanged. Name the specific cost of making the change — migration effort, coherence risk, signal thinness, or premature commitment.

The following columns are mandatory. Do not omit any column. Rule 1 applies to `Defender verdict`.

| Proposal ID | Strongest case for no change | Specific cost of changing | Proposal Architect response | Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |
|------------|------------------------------|--------------------------|----------------------------|----------------------------------------------------------------|
| ADD-1 | [why keeping strategy as-is is defensible] | [concrete cost] | [Architect's rebuttal or concession] | Unchanged |

Null case — no active proposals (Rule 3):
`| — | No active proposals — Defender step not applicable | N/A | N/A | N/A |`

After filling the table:
- Mark `Withdrawn` proposals: add "[WITHDRAWN after Defender step]" to the original row in Step 7.
- Mark `Strengthened` proposals: update the `If unchanged` cell in Step 7.
- `Unchanged` proposals: proceed as-is.

> **Micro-gate 7b**: Step 7b complete — Defender table complete, Withdrawn proposals marked in Step 7, Strengthened proposals updated in Step 7. Advancing to Step 8.

---

### Step 8 — Role: Diff Author

Stop. Write this statement verbatim before building the diff table:

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★ (inline [file.md — ≤10 words] per row), Proposal ★ (ID from Step 7). No column omitted. Withdrawn proposals excluded."

The following columns are mandatory. Withdrawn proposals are excluded.

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current text] | [proposed text] | [file.md — ≤10 words] | ADD-1 |

> **Micro-gate 8**: Step 8 complete — schema commitment statement written verbatim, diff table complete, withdrawn proposals excluded. Advancing to Step 9.

---

### Step 9 — Confirmation gate

Reply **YES** to apply all non-withdrawn proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 10 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed, non-withdrawn proposals. Preserve existing structure; update only sections affected.

---

## V-04 — Combination: Ante-Signal Defense + Explanatory Register (V-01 + V-02)

**Axes**: Role sequence (ante-signal Defense Register, Step 2b) combined with phrasing register (explanatory/descriptive throughout).

**Hypothesis**: V-01 tests whether pre-registering defenses strengthens inertia challenges; V-02 tests whether explanatory prose improves structural compliance. If both axes are individually load-bearing, their combination should produce proposals that are both better-evidenced and more structurally disciplined. The combination also tests for negative interaction: if explanatory prose dilutes the binding force of the Defense Register by making it feel optional, the combination will underperform V-01 alone.

---

You are executing `topic:plan` for the topic `{topic}`.

This skill closes the gap between what the strategy assumed when it was written and what signals have since revealed. The assumption table is built in two passes: first you extract what strategy.md assumed without saying (Step 2, before signals), then you adjudicate those assumptions against what signals revealed (Step 3b, after signals). This ordering prevents assumption fabrication — assumptions extracted after signal reading will reflect signal content, defeating the purpose of the extraction step.

Before opening any signal files, the Strategy Advocate produces a Defense Register: a pre-signal statement of the strategy's strongest arguments for its current choices. The Defender at Step 7b draws on this register rather than constructing a post-hoc counterfactual.

After building proposals and running the Defender challenge, present the confirmed proposal set and wait for YES before writing. Do not auto-apply.

---

### COLUMN CONTRACT (binding before reading any file)

The four rules below govern every table you produce. They exist because tables are only auditable when columns obey structural constraints — not because columns are labeled, but because the values in those columns actually discriminate. Read all four rules before the Output Schema.

**Rule 1 — Enumerated columns**

The purpose of enumeration is discriminating power. A `Type` column that says `ADD` tells a reviewer the proposal expands scope. A column that says "I think we should add a skill" tells a reviewer nothing they can act on without re-interpreting. The rule is: any cell in an enumerated column that contains paraphrase, conditional prose, or a multi-value selection is treated as empty regardless of content.

Enumerated columns and permitted values:
- `Type`: `ADD` | `REMOVE` | `REPRIORITIZE`
- `Reversibility`: `(1) Reversible at same cost` | `(2) Gets harder` | `(3) Becomes impossible`
- `Delta candidate?`: `yes` | `no` | `yes — F-01` | `yes — F-03`
- `Consistent with strategy?`: `Yes` | `No` | `Partial`
- `Defender verdict`: `Withdrawn` | `Strengthened` | `Unchanged`

Rule 1 PASS examples:
- `Type: ADD` — single token from declared set
- `Reversibility: (1) Reversible at same cost` — full enumerated phrase
- `Defender verdict: Strengthened` — single declared token

Rule 1 FAIL examples (treated as absent):
- `Type: "addition"` — not in declared set
- `Reversibility: "it will be harder later"` — prose, not enumerated phrase
- `Defender verdict: "conditionally accepted"` — not in declared set

**Rule 2 — Column independence**

Before filling any `Implicit evidence` cell, ask: "Could I fill this cell without opening strategy.md?" If yes, stop — you are about to write a structural alias. The `Implicit evidence` column should contain content a second reviewer can independently verify: a specific phrase, verbatim text, or an explicitly-noted absence. Row keys, restatements, and pointer references are structural aliases.

Rule 2 PASS examples for `Implicit evidence`:
- PASS: `"teams run scout before draft"` — specific phrase from the rationale block; verifiable
- PASS: `"signal count threshold never defined"` — absence explicitly noted; auditable
- PASS: `"the phrase 'gather evidence first'"` — verbatim; traceable to a specific location
- PASS: `"no definition of done for this topic appears in the strategy"` — explicit gap notation

Rule 2 FAIL examples for `Implicit evidence` (treated as absent):
- FAIL: `A-01` — the row key; no new content
- FAIL: `"signals gather evidence"` — restatement in different words
- FAIL: `"see rationale section"` — pointer with no content
- FAIL: `"strategy implies sequencing"` — generic inference not traceable to any phrase

**Rule 3 — Null completeness**

Every section must produce output, even when it finds nothing. A null row proves the section ran. An empty section cannot be distinguished from a skipped section. Every null template in this skill cites Rule 3.

The conflict audit is the most common violation site. If no conflicts exist, the required output is: `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |` — not an empty section.

Rule 3 PASS examples:
- Conflict null: `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |` (Rule 3)
- ADD null: `| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |` (Rule 3)
- Delta null: `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |` (Rule 3)

Rule 3 FAIL (treated as section skipped):
- Empty conflict section with no null row
- Proposals table with ADD rows only; REMOVE-0 and REPRIORITIZE-0 absent
- Delta step bypassed with only "no changes needed" in prose

**Rule 4 — Two-level traceability**

A proposals table without full traceability is a wish list. The `Delta Finding` column is what makes the table self-contained: it embeds the full chain — proposal → delta finding → source signal — in the proposal row itself. The finding ID alone requires the reviewer to look up the delta section. A signal reference alone skips the delta layer. Only the full "Strategy assumed [X] / Signal revealed [Y]" text with the finding ID satisfies Rule 4.

Rule 4 PASS examples:
- `F-01: Strategy assumed scout runs before draft / Signal revealed draft completed without scout artifacts`
- `F-03: Strategy assumed no review signals existed / Signal revealed 3 review artifacts unaddressed in strategy`

Rule 4 FAIL examples (treated as absent):
- `F-01` — finding ID only
- `"signal S-01 suggests adding a skill"` — signal reference, no delta structure

---

### Output Schema (read before proceeding to Step 1)

Every table must conform to this schema. Columns marked ★ are mandatory. All four Contract Rules apply. Do not omit any ★ column.

**Assumption Table** (5 columns — all independently populated per Rule 2)
| ★ Assumption | ★ Implicit evidence [Rule 2 — PASS: phrase/paraphrase from strategy.md | FAIL: row key / restatement / pointer] | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? [Rule 1: yes / no / yes — F-NN] |

**Defense Register** (Step 2b — produced before any signal files are opened)
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
| ★ Proposal ID | ★ Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | ★ Change | ★ Delta Finding [Rule 4: full "Strategy assumed X / Signal revealed Y" + ID] | ★ Evidence | ★ If unchanged | ★ Reversibility [Rule 1: (1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible] | ★ Confidence |

**Defender Challenge Table** (Step 7b — Rule 1 applies to `Defender verdict`)
| ★ Proposal ID | ★ Strongest case for no change | ★ Specific cost of changing | ★ Defense basis [D-ID(s) from Step 2b, or "Newly constructed — no pre-registered defense applies"] | ★ Proposal Architect response | ★ Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

Do not omit any ★ column.

---

### Step 1 — Role: Stated-Field Extractor

Your first task is to establish the stated boundary of the strategy — what it explicitly commits to, not what it implies. Open `simulations/{topic}/strategy.md` and read it in full. Extract these five fields as stated. Write "not stated" for any field not explicitly present. The extraction must be clean: no inferences, no paraphrase that goes beyond the text.

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

Now you are looking for what strategy.md assumed without saying. Every strategy document places implicit bets — about sequencing, about which namespaces matter, about what "enough signals" means. These bets are the raw material of the delta step: a signal can only produce a finding if it contradicts an assumption. Naming assumptions before signal reading prevents assumption fabrication.

Scan these five dimensions: (a) implied audience knowledge level, (b) namespace priority ordering assumed without justification, (c) signal sufficiency threshold, (d) timeline or sequencing feasibility, (e) definition of "done" for this topic.

Before filling any `Implicit evidence` cell, apply the Rule 2 test: "Can I fill this cell without opening strategy.md?" If yes, find a specific phrase or noted absence instead.

Column initialization rules: `Contradicted?` = `[pending]` until Step 3b. `Delta candidate?` = `yes` / `no` until Step 4, then update to `yes — F-NN`.

The following columns are mandatory. Do not omit any column.

| Assumption | Implicit evidence [Rule 2] | Contradicted by a signal? | Why this matters | Delta candidate? [Rule 1: yes / no] |
|-----------|---------------------------|--------------------------|-----------------|-------------------------------------|
| [most important] | [phrase from strategy.md — Rule 2 test before filling] | [pending] | [failure mode] | yes |

Null case (Rule 3): `| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |`

---

### Step 2b — Role: Strategy Advocate

Before you open any signal files, produce a Defense Register. Its purpose: pre-register the strategy's strongest arguments for its current choices, built without knowledge of what signals say. This register is the Defender's reference at Step 7b — when challenging a proposal, the Defender cites the pre-registered argument rather than improvising a counterfactual under proposal-pressure.

For each strategic decision identifiable from Steps 1 and 2, state the strongest pre-signal argument that decision remains correct. Produce 3–5 entries. The `What would invalidate this defense?` column names the signal type that would legitimately defeat the registered argument.

The following columns are mandatory. Do not omit any column.

| Defense ID | Strategic decision | Strongest keep-it argument (pre-signal) | What would invalidate this defense? |
|-----------|-------------------|----------------------------------------|-------------------------------------|
| D-01 | [decision from strategy.md] | [why keeping it is defensible, without reference to signals] | [signal type or finding structure that would defeat this defense] |

Null case: `| D-00 | No strategic decisions identifiable as defensible pre-signal | N/A | N/A |`

---

### Step 3a — Role: Signal Analyst (Read)

Now read the signals. Glob `simulations/{topic}/` recursively and read every file. Build a complete inventory: what exists, what each reveals, how each relates to the strategy and to specific assumptions from Step 2. You are documenting here — analytical conclusions come in Steps 3b and 4.

Null case (Rule 3): `> No signals found — strategy.md does not need revision at this time.`

The following columns are mandatory. Rule 1: `Consistent with strategy?` must be exactly `Yes`, `No`, or `Partial`.

| ID | File | Namespace | Skill | Date | Key Finding | Consistent with strategy? [Rule 1: Yes / No / Partial] | Assumption link |
|----|------|-----------|-------|------|-------------|-------------------------------------------------------|----------------|
| S-01 | | | | | | | |

---

### Step 3b — Role: Assumption Archaeologist (Back-fill)

Return to the assumption table and adjudicate each row against the signals you read. Replace every `[pending]` cell with one of:
- `Contradicted — S-NN`: cite the ID and one sentence explaining how
- `Supported — S-NN`: cite the ID
- `No signal coverage`: no signal addresses this assumption directly

Reproduce the full updated assumption table. After Step 4, update every `yes` cell in `Delta candidate?` to `yes — F-NN`.

---

### Step 4 — Role: Delta Identifier

Before filling the findings table, write two things: (1) the name of the anti-pattern you are guarding against, and (2) a PASS/FAIL exhibit for the delta vs. inventory distinction.

The anti-pattern is *plain inventory*: describing what signals say without naming what the strategy assumed differently. The test: does each row contain a genuine contradiction between a strategy assumption and a signal revelation? If a row only describes signal content, it is inventory, not a finding.

Write the anti-pattern name and PASS/FAIL exhibit before filling any row.

The following columns are mandatory. Do not omit any column.

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root |
|-----------|-----------------|----------------|-----------------|----------------|
| F-01 | | | S-XX | |

Null case (Rule 3): `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |`

After completing the findings table, return to Step 3b and update `yes` rows to `yes — F-NN`.

---

### Step 5 — Role: Coverage Auditor

Assess signal coverage across all 9 namespaces. Use stage-relative framing. All 9 namespaces must appear by name.

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

Look for signals that directly contradict each other — not signals that are incomplete, but signals where two artifacts make incompatible claims. A conflict has a strategic implication: it means the strategy cannot defer to signal evidence without first resolving the contradiction. If no conflicts exist, the null row is still required.

The following columns are mandatory.

| Conflict ID | Signal A | Signal B | Description | Implication for strategy |
|------------|---------|---------|-------------|--------------------------|
| CF-01 | | | | |

Null case (Rule 3): `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |`

---

### Step 7 — Role: Proposal Architect

Stop. Write this statement verbatim before building the proposals table:

> "Proposals schema committed: Proposal ID ★, Type ★ [Rule 1: ADD / REMOVE / REPRIORITIZE; prose not valid], Change ★, Delta Finding ★ [Rule 4: full 'Strategy assumed X / Signal revealed Y' text with ID], Evidence ★, If unchanged ★ (no degradation named = preference not decision), Reversibility ★ [Rule 1: (1)/(2)/(3); prose not valid], Confidence ★. All three types present. Empty types use Rule 3 null rows."

Every proposal must be rooted in a delta finding. The `If unchanged` cell must name a specific degradation. "It would be worse" fails the decision-qualification test; name the specific mechanism.

The following columns are mandatory. Do not omit any column.

| Proposal ID | Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | Change | Delta Finding [Rule 4] | Evidence | If unchanged [specific degradation] | Reversibility [Rule 1: (1)/(2)/(3)] | Confidence |
|------------|------------------------------------------|--------|----------------------|----------|-------------------------------------|-------------------------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [degradation] | (2) Gets harder | High |

Null rows (Rule 3):

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 7b — Role: Status Quo Defender

Adopt this role: you are the voice of inertia. For each active proposal, draw on the Defense Register from Step 2b — cite the D-ID(s) whose pre-registered argument applies to this proposal's challenged decision. If no pre-registered defense applies, write "Newly constructed — no pre-registered defense applies." Name the specific cost of making the change.

The following columns are mandatory. Do not omit any column. Rule 1 applies to `Defender verdict`.

| Proposal ID | Strongest case for no change | Specific cost of changing | Defense basis [D-ID(s) or "Newly constructed — no pre-registered defense applies"] | Proposal Architect response | Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |
|------------|------------------------------|--------------------------|------------------------------------------------------------------------------------|----------------------------|----------------------------------------------------------------|
| ADD-1 | [why keeping strategy as-is is defensible] | [concrete cost] | D-01 | [Architect's rebuttal or concession] | Unchanged |

Null case — no active proposals (Rule 3):
`| — | No active proposals — Defender step not applicable | N/A | N/A | N/A | N/A |`

After filling:
- Mark `Withdrawn` proposals: add "[WITHDRAWN after Defender step]" to the original row in Step 7.
- Mark `Strengthened` proposals: update the `If unchanged` cell in Step 7.
- `Unchanged` proposals: proceed as-is.

---

### Step 8 — Role: Diff Author

Stop. Write this statement verbatim before building the diff table:

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★ (inline [file.md — ≤10 words] per row), Proposal ★ (ID from Step 7). No column omitted. Withdrawn proposals excluded."

The diff table bridges proposals to strategy.md edits. Every row carries an inline evidence citation from the source signal. Withdrawn proposals are excluded.

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current text] | [proposed text] | [file.md — ≤10 words] | ADD-1 |

---

### Step 9 — Confirmation gate

Reply **YES** to apply all non-withdrawn proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 10 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed, non-withdrawn proposals. Preserve existing structure; update only sections affected.

---

## V-05 — Full Ceiling: Ante-Signal Defense + Explanatory Register + Phase Gates + Unified Exhibit

**Axes**: All three R15 axes (role sequence, phrasing register, lifecycle emphasis) combined with R14 V-02's unified per-column exhibit format for the COLUMN CONTRACT. Phase macro-gates (R14 V-01) provide lifecycle structure; the unified exhibit format makes column-symmetry structural rather than instructed.

**Hypothesis**: V-05 tests whether all four structural mechanisms can coexist without interaction degradation. The unified exhibit format (Column | PASS | FAIL) makes C-42 unavoidable structurally. Combined with the explanatory register, the CONTRACT becomes both structurally enforced and comprehensible. The pre-signal defense register anchors the Defender's challenge in a pre-articulated argument. Phase gates bound the activation sequence. If the combination is load-bearing, V-05 should achieve the highest overall score. If there is a negative interaction — explanatory prose dilutes the binding force of the exhibit format, or the defense register adds overhead that reduces compliance elsewhere — the finding identifies which axis is not net-positive.

---

You are executing `topic:plan` for the topic `{topic}`.

This skill closes the gap between what the strategy assumed when it was written and what signals have since revealed. The assumption table is built in two passes: first you extract what strategy.md assumed without saying (Step 2, before signals), then you adjudicate those assumptions against what signals actually revealed (Step 3b, after signals). This ordering prevents assumption fabrication — assumptions extracted after signal reading will reflect signal content.

Before opening any signal files, the Strategy Advocate produces a Defense Register: a pre-signal statement of the strategy's strongest arguments for its current choices. The Defender at Step 7b draws on this register rather than constructing a post-hoc counterfactual.

Execution is organized into four phases. You must complete each phase and pass its checkpoint gate before the next phase opens. After building proposals and running the Defender challenge, present the confirmed proposal set and wait for YES before writing. Do not auto-apply.

---

### COLUMN CONTRACT (binding before reading any file)

The four rules below govern every table you produce. Each rule ends with an exhibit table. Read all four exhibit tables before the Output Schema — the exhibit format makes compliance structural: a column can only appear in the PASS column if a FAIL value occupies the same row.

**Rule 1 — Enumerated columns**

The purpose of enumeration is discriminating power. A `Type` column that says `ADD` tells a reviewer the proposal expands scope. A `REPRIORITIZE` tells them sequencing is being adjusted without new scope. These are different downstream decisions. A cell that says "I think we should add a skill" provides neither — it requires re-interpretation. The rule: any cell in an enumerated column that contains paraphrase, conditional prose, or a multi-value selection is treated as empty regardless of content.

Rule 1 exhibit (read PASS and FAIL for every row before filling any governed cell):

| Column | PASS value — select from declared set only | FAIL value — treated as absent |
|--------|-------------------------------------------|-------------------------------|
| `Type` | `ADD` \| `REMOVE` \| `REPRIORITIZE` | "I suggest adding..." \| "addition" \| "add/remove" |
| `Reversibility` | `(1) Reversible at same cost` \| `(2) Gets harder` \| `(3) Becomes impossible` | "it will be harder later" \| "probably irreversible" |
| `Delta candidate?` | `yes` \| `no` \| `yes — F-01` \| `yes — F-03` | "probably yes" \| "yes if confirmed" |
| `Consistent with strategy?` | `Yes` \| `No` \| `Partial` | "mostly yes" \| "it's complicated" |
| `Defender verdict` | `Withdrawn` \| `Strengthened` \| `Unchanged` | "maybe we should keep it" \| "partially withdrawn" \| "conditionally accepted" |

**Rule 2 — Column independence**

Before filling any `Implicit evidence` cell, ask: "Could I fill this cell without opening strategy.md?" If yes, stop — you are about to write a structural alias that adds no auditing value. The `Implicit evidence` column should contain specific phrases, verbatim text, or explicitly-noted absences that a second reviewer could independently verify. Row keys, restatements, and pointer references are structural aliases.

Rule 2 exhibit (four paired examples for `Implicit evidence`):

| Example | PASS — traceable to phrase or noted absence in strategy.md | FAIL — treated as absent |
|---------|-----------------------------------------------------------|--------------------------|
| 1 | `"teams run scout before draft"` — specific phrase from rationale block | `A-01` — the row key; reconstructible without reading the document |
| 2 | `"signal count threshold never defined"` — gap detected as absent in the text | `"signals gather evidence"` — restatement in different words |
| 3 | `"the phrase 'gather evidence first'"` — verbatim instruction from the document | `"see rationale section"` — pointer with no content |
| 4 | `"no definition of done for this topic appears in the strategy"` — explicit gap notation | `"strategy implies sequencing"` — generic inference not traceable to any phrase |

**Rule 3 — Null completeness**

Every section must produce output, even when it finds nothing. A null row proves the section ran. An empty section cannot be distinguished from a skipped section. The conflict audit is the most common violation site: when no conflicts exist, the section is often left empty. The null row — `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |` — is the only evidence that the audit ran.

Rule 3 exhibit (three null cases — PASS = explicit null row present; FAIL = treated as section skipped):

| Null case | PASS — section ran, nothing found | FAIL — treated as section skipped |
|-----------|----------------------------------|----------------------------------|
| Conflict section | `\| CF-00 \| — \| — \| No conflicts detected — audit ran \| No action needed \|` (Rule 3) | Empty conflict section with no null row |
| Proposal type rows | `\| ADD-0 \| ADD \| None proposed \| Delta Finding: N/A \| — \| ... \|` + REMOVE-0 + REPRIORITIZE-0 (Rule 3) | Proposals table with ADD rows only; REMOVE-0 / REPRIORITIZE-0 absent |
| Delta step | `\| F-00 \| Strategy confirmed \| No gaps detected \| All signals \| N/A \|` (Rule 3) | Delta step bypassed with only "no changes needed" in prose |

**Rule 4 — Two-level traceability**

A proposals table without full traceability is a recommendation list. The `Delta Finding` column is what makes the table self-contained: it embeds the full chain — proposal → delta finding → source signal — in the proposal row itself. The finding ID alone requires the reviewer to look up the delta section. A signal reference alone skips the delta layer. Only the full "Strategy assumed [X] / Signal revealed [Y]" text with the finding ID satisfies Rule 4.

Rule 4 exhibit (two paired examples for `Delta Finding`):

| Example | PASS — full traceability chain | FAIL — treated as absent |
|---------|-------------------------------|--------------------------|
| 1 | `F-01: Strategy assumed scout runs before draft / Signal revealed draft completed without scout artifacts` | `F-01` — finding ID only; reviewer must look up the delta section |
| 2 | `F-03: Strategy assumed no review signals existed / Signal revealed 3 review artifacts unaddressed in strategy` | `"signal S-01 suggests adding a skill"` — signal reference only; delta layer missing |

---

### Output Schema (read before proceeding to Phase 1)

Every table must conform to this schema. Columns marked ★ are mandatory. All four Contract Rules apply. Do not omit any ★ column.

**Assumption Table** (5 columns — all independently populated per Rule 2)
| ★ Assumption | ★ Implicit evidence [Rule 2 — PASS: phrase/paraphrase from strategy.md | FAIL: row key / restatement / pointer] | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? [Rule 1: yes / no / yes — F-NN] |

**Defense Register** (Step 2b — produced before Phase 1 gate; before any signal files are opened)
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
| ★ Proposal ID | ★ Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | ★ Change | ★ Delta Finding [Rule 4: full "Strategy assumed X / Signal revealed Y" + ID] | ★ Evidence | ★ If unchanged | ★ Reversibility [Rule 1: (1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible] | ★ Confidence |

**Defender Challenge Table** (Step 7b — Rule 1 applies to `Defender verdict`)
| ★ Proposal ID | ★ Strongest case for no change | ★ Specific cost of changing | ★ Defense basis [D-ID(s) from Defense Register, or "Newly constructed — no pre-registered defense applies"] | ★ Proposal Architect response | ★ Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

Do not omit any ★ column.

---

### PHASE 1 — Pre-read (Steps 1–2b)

*No signal files may be read during Phase 1. If you encounter a signal file path, do not read it — log it in the signal inventory during Phase 2 only.*

---

### Step 1 — Role: Stated-Field Extractor

Your first task is to establish the stated boundary of the strategy. Open `simulations/{topic}/strategy.md` and read it in full. Extract only what it explicitly commits to — write "not stated" for any field not explicitly present. No inferences; no paraphrase beyond the text.

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

Now you are looking for what strategy.md assumed without saying. Every strategy document places implicit bets — about sequencing, about which namespaces matter, about what "enough signals" means. These bets are the raw material of the delta step: a signal can only produce a finding if it contradicts an assumption. Naming assumptions before signal reading prevents assumption fabrication.

Scan these five dimensions: (a) implied audience knowledge level, (b) namespace priority ordering assumed without justification, (c) signal sufficiency threshold, (d) timeline or sequencing feasibility, (e) definition of "done" for this topic.

Before filling any `Implicit evidence` cell, apply the Rule 2 exhibit — ask: "Can I fill this cell without opening strategy.md?" If yes, find a specific phrase or noted absence instead.

Column initialization rules: `Contradicted?` = `[pending]` until Step 3b. `Delta candidate?` = `yes` / `no` until Step 4, then update to `yes — F-NN`.

The following columns are mandatory. Do not omit any column.

| Assumption | Implicit evidence [Rule 2] | Contradicted by a signal? | Why this matters | Delta candidate? [Rule 1: yes / no] |
|-----------|---------------------------|--------------------------|-----------------|-------------------------------------|
| [most important] | [phrase from strategy.md — Rule 2 exhibit applied] | [pending] | [failure mode] | yes |

Null case (Rule 3): `| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |`

---

### Step 2b — Role: Strategy Advocate

Before you open any signal files, produce a Defense Register. Its purpose: pre-register the strategy's strongest arguments for its current choices, built without knowledge of what signals say. This register is the Defender's reference at Step 7b — when challenging a proposal, the Defender cites the pre-registered argument rather than improvising a counterfactual under proposal-pressure.

For each strategic decision identifiable from Steps 1 and 2, state the strongest pre-signal argument that decision remains correct. Produce 3–5 entries. The `What would invalidate this defense?` column names the signal type that would legitimately defeat the registered argument.

The following columns are mandatory. Do not omit any column.

| Defense ID | Strategic decision | Strongest keep-it argument (pre-signal) | What would invalidate this defense? |
|-----------|-------------------|----------------------------------------|-------------------------------------|
| D-01 | [decision from strategy.md] | [why keeping it is defensible, without reference to signals] | [signal type or finding structure that would defeat this defense] |

Null case: `| D-00 | No strategic decisions identifiable as defensible pre-signal | N/A | N/A |`

---

### PHASE 1 GATE

Produce this checkpoint before advancing to Phase 2. If any item is incomplete, stop and complete it before the gate clears.

| Step | Artifact | Complete? |
|------|----------|-----------|
| Step 1 | Stated-field table — all 5 fields populated, no inferred values | Yes / No |
| Step 2 | Assumption table — all rows, all 5 columns, Rule 2 exhibit applied to every `Implicit evidence` cell, all `Contradicted?` = `[pending]` | Yes / No |
| Step 2b | Defense Register — 3–5 entries, all 4 columns, no signal content referenced | Yes / No |

All rows must show "Yes". Declare: **Phase 1 complete. Opening Phase 2 (Read).**

---

### PHASE 2 — Read (Step 3a)

*Phase 1 gate cleared. Signal files may now be read.*

---

### Step 3a — Role: Signal Analyst (Read)

Now read the signals. Glob `simulations/{topic}/` recursively and read every file. Build a complete inventory: what exists, what each reveals, how each relates to the strategy and to specific assumptions from Step 2. You are documenting here — analytical conclusions come in Steps 3b and 4.

Null case (Rule 3): `> No signals found — strategy.md does not need revision at this time.`

The following columns are mandatory. Rule 1: `Consistent with strategy?` must be exactly `Yes`, `No`, or `Partial`.

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

*Phase 2 gate cleared. Work only from the signal inventory built in Phase 2 — do not re-read signal files during this phase.*

---

### Step 3b — Role: Assumption Archaeologist (Back-fill)

Return to the assumption table and adjudicate each row against the signals you read. Replace every `[pending]` cell with one of:
- `Contradicted — S-NN`: the signal contradicts this assumption; cite the ID and one sentence explaining how
- `Supported — S-NN`: the signal corroborates this assumption; cite the ID
- `No signal coverage`: no signal addresses this assumption directly

Reproduce the full updated assumption table. After Step 4, return here and update every `yes` cell in `Delta candidate?` to `yes — F-NN`.

---

### Step 4 — Role: Delta Identifier

Before filling the findings table, write two things: (1) the name of the anti-pattern you are guarding against, and (2) a PASS/FAIL exhibit for the delta vs. inventory distinction.

The anti-pattern is *plain inventory*: describing what signals say without naming what the strategy assumed differently. The test: does each row contain a genuine contradiction between a strategy assumption and a signal revelation? If a row only describes signal content, it is inventory, not a finding.

Write the anti-pattern name and PASS/FAIL exhibit before filling any row.

The following columns are mandatory. Do not omit any column.

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root |
|-----------|-----------------|----------------|-----------------|----------------|
| F-01 | | | S-XX | |

Null case (Rule 3): `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |`

After completing the findings table, return to Step 3b and update `yes` rows to `yes — F-NN`.

---

### Step 5 — Role: Coverage Auditor

Assess signal coverage across all 9 namespaces. Use stage-relative framing — a namespace with zero signals may be appropriate at early stages and concerning at late stages. All 9 namespaces must appear by name.

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

Look for signals that directly contradict each other — not signals that are incomplete, but signals where two artifacts make incompatible claims. Name the strategic implication for each conflict. If no conflicts exist, the null row is still required.

The following columns are mandatory.

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

All rows must show "Yes". Declare: **Phase 3 complete. Opening Phase 4 (Build).**

---

### PHASE 4 — Build (Steps 7–10)

*Phase 3 gate cleared.*

---

### Step 7 — Role: Proposal Architect

Stop. Write this statement verbatim before building the proposals table:

> "Proposals schema committed: Proposal ID ★, Type ★ [Rule 1: ADD / REMOVE / REPRIORITIZE; prose not valid], Change ★, Delta Finding ★ [Rule 4: full 'Strategy assumed X / Signal revealed Y' text with ID], Evidence ★, If unchanged ★ (no degradation named = preference not decision), Reversibility ★ [Rule 1: (1)/(2)/(3); prose not valid], Confidence ★. All three types present. Empty types use Rule 3 null rows."

Every proposal must be rooted in a delta finding. The `If unchanged` cell must name a specific degradation — what gap persists or worsens if this change is deferred? "It would be worse" fails the decision-qualification test; name the specific mechanism.

The following columns are mandatory. Do not omit any column.

| Proposal ID | Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | Change | Delta Finding [Rule 4] | Evidence | If unchanged [specific degradation] | Reversibility [Rule 1: (1)/(2)/(3)] | Confidence |
|------------|------------------------------------------|--------|----------------------|----------|-------------------------------------|-------------------------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [degradation] | (2) Gets harder | High |

Null rows (Rule 3):

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 7b — Role: Status Quo Defender

Adopt this role: you are the voice of inertia. For each active proposal, draw on the Defense Register from Step 2b — cite the D-ID(s) whose pre-registered argument applies to this proposal's challenged decision. If no pre-registered defense applies, write "Newly constructed — no pre-registered defense applies" and explain why the pre-registered defenses did not cover this case.

Name the specific cost of making the change: migration effort, coherence risk, signal thinness, or premature commitment.

The following columns are mandatory. Do not omit any column. Rule 1 applies to `Defender verdict`.

| Proposal ID | Strongest case for no change | Specific cost of changing | Defense basis [D-ID(s) or "Newly constructed — no pre-registered defense applies"] | Proposal Architect response | Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |
|------------|------------------------------|--------------------------|------------------------------------------------------------------------------------|----------------------------|----------------------------------------------------------------|
| ADD-1 | [why keeping strategy as-is is defensible] | [concrete cost] | D-01 | [Architect's rebuttal or concession] | Unchanged |

Null case — no active proposals (Rule 3):
`| — | No active proposals — Defender step not applicable | N/A | N/A | N/A | N/A |`

After filling:
- Mark `Withdrawn` proposals: add "[WITHDRAWN after Defender step]" to the original row in Step 7.
- Mark `Strengthened` proposals: update the `If unchanged` cell in Step 7.
- `Unchanged` proposals: proceed as-is.

---

### Step 8 — Role: Diff Author

Stop. Write this statement verbatim before building the diff table:

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★ (inline [file.md — ≤10 words] per row), Proposal ★ (ID from Step 7). No column omitted. Withdrawn proposals excluded."

The diff table bridges proposals to strategy.md edits. Every row carries an inline evidence citation from the source signal. Withdrawn proposals are excluded.

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current text] | [proposed text] | [file.md — ≤10 words] | ADD-1 |

---

### PHASE 4 GATE

| Step | Artifact | Complete? |
|------|----------|-----------|
| Step 7 | Proposals table — schema commitment written verbatim, all three type rows present (active or null), Rule 4 Delta Finding text in every active row | Yes / No |
| Step 7b | Defender table — Defense basis column populated (D-ID or "Newly constructed"), Withdrawn proposals marked in Step 7 | Yes / No |
| Step 8 | Diff table — schema commitment written verbatim, withdrawn proposals excluded, inline evidence per row | Yes / No |

All rows must show "Yes". Declare: **Phase 4 complete. Presenting proposal set for confirmation.**

---

### Step 9 — Confirmation gate

Reply **YES** to apply all non-withdrawn proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 10 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed, non-withdrawn proposals. Preserve existing structure; update only sections affected.
