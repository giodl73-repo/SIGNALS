# topic-plan — Round 14 Variations (v13 rubric)

**Skill**: `topic:plan`
**Rubric**: v13 (C-01–C-43, 265 pts total)
**Date**: 2026-03-15

---

## Round 14 Design Notes

R13 V-01 achieved the highest score under v12 and introduced the discriminating mechanisms
for v13's two new criteria:

- **C-42** — Column-complete pass/fail pairing within each CONTRACT rule: the PASS column
  set and FAIL column set must be identical within each rule. R13 V-01 satisfies this for
  all four rules — Rule 1 (5 PASS columns + 5 FAIL columns including `Defender verdict`),
  Rule 2 (4 PASS + 4 FAIL for `Implicit evidence`), Rule 3 (3 PASS + 3 FAIL null cases),
  Rule 4 (2 PASS + 2 FAIL for `Delta Finding`). R13 V-03/V-04/V-05 score PARTIAL on C-38
  and FAIL on C-42 — they add columns via their axes (Prediction match, Urgency) but FAIL
  examples do not extend to those new columns in Rule 1.

- **C-43** — Cross-rule example coverage: C-42 discipline applied to ALL CONTRACT rules.
  R13 V-01 satisfies this because Rules 2, 3, and 4 also carry symmetric paired examples.
  R13 V-04 concentrates pairings on Rule 1 and Rule 5 but thins Rule 3 FAIL examples;
  R13 V-05 adds extensive Rule 1 coverage but C-43 fails because Rules 3 and 4 FAIL
  examples are abbreviated.

**All R14 variations preserve C-42 and C-43 as floor requirements:**
- For every CONTRACT rule, the set of columns covered by PASS examples must equal the set
  covered by FAIL examples
- This discipline applies to all four rules, not only Rule 1
- Every null-case site cites "(Rule 3)" (C-40 floor)
- Every enumerated-value column in the schema carries `[Rule N: ...]` annotation (C-41 floor)
- 4-rule CONTRACT minimum (Rules 1–4)

**Three single-axis dimensions explored in R14:**

1. **Lifecycle emphasis** — Explicit phase gate declarations divide execution into four
   named phases (Pre-read, Read, Analysis, Build). At each phase boundary, a mandatory
   checkpoint table lists artifacts produced and requires all items marked "Yes" before the
   next phase opens. Tests whether structural lifecycle gates reduce cross-phase contamination
   in assumption extraction and delta identification.

2. **Output format — unified per-column exhibit** — The CONTRACT's separate PASS list +
   FAIL list format is replaced with a single exhibit table per rule: `Column | PASS | FAIL`.
   The table structure makes C-42 unavoidable — a column can only appear in the PASS column
   if a FAIL value occupies the same row. Tests whether structural enforcement outperforms
   instructed enforcement for column completeness across all four rules.

3. **Inertia framing — pre-emptive threshold Defender** — The Status Quo Defender runs
   BEFORE the Proposal Architect. At Step 6b, the Defender produces a Change Warrant Table
   stating the minimum evidence threshold each change type must meet. At Step 7, the Proposal
   Architect must match each proposal against the warrant criteria before the row is added to
   the proposals table. Proposals that do not clear the warrant are excluded before review.
   Tests whether threshold-first framing produces fewer preference-only proposals than the
   post-hoc challenge framing in R13 V-01 Step 7b.

**Variation design:**

| Variation | Axis | Type | Primary R14 target |
|-----------|------|------|--------------------|
| V-01 | Lifecycle emphasis — phase gates | Single | Cross-phase contamination (C-03, C-09) |
| V-02 | Output format — unified per-column exhibit | Single | C-42/C-43 structural enforcement |
| V-03 | Inertia framing — pre-emptive threshold Defender | Single | Proposal discrimination (C-07, C-08) |
| V-04 | Lifecycle + unified exhibit (V-01 + V-02) | Combination | Phase contamination + column asymmetry |
| V-05 | Full ceiling — V-01 + V-02 + V-03 + CONTRACT exhibit audit | Combination | Maximum structural depth |

---

## V-01 — Lifecycle Emphasis: Phase Gates

**Axis**: Lifecycle emphasis — execution is divided into four explicitly declared phases:
Phase 1 (Pre-read: Steps 1–2), Phase 2 (Read: Step 3a), Phase 3 (Analysis: Steps 3b–6),
Phase 4 (Build: Steps 7–10). At each phase boundary, a mandatory checkpoint table lists
every artifact produced in that phase and marks it complete. If any mandatory artifact is
marked incomplete, the gate does not clear and the next phase does not open.

**Hypothesis**: In the standard step sequence, nothing structurally prevents the model from
consulting signals while filling pre-read artifacts (assumption table) or from using post-read
knowledge to retroactively sharpen assumptions. Explicit phase declarations with a pass/fail
checkpoint before reading is permitted should reduce these contaminations. If correct, V-01
should produce assumption tables with no signal content and delta findings that cannot have
been reverse-engineered. If incorrect — the phase gate declarations produce no measurable
improvement in assumption quality — the finding is that naming the phases is not a
load-bearing constraint under the current prompt structure.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it was
written. Execution is organized into four phases; you must complete each phase and pass its
checkpoint gate before opening the next. The assumption table is a two-phase artifact:
extract at Step 2 (Phase 1, before any signal reading), back-fill at Step 3b (Phase 3,
after reading). After building proposals and running the Defender challenge, present the
confirmed proposal set and wait for YES before writing. Do not auto-apply.

---

### COLUMN CONTRACT (binding before reading any file)

Four rules govern every table you produce. Read all four before the Output Schema.

**Rule 1 — Enumerated columns**

Any column using a closed value set must declare those values at every point where the column
is named. Select from the declared set only; prose is not a valid value. A cell that contains
paraphrase, conditional prose, or a multi-value selection is treated as empty regardless of
content.

*Why this matters*: A model that sees `Type` and writes "I think we should add a new skill"
has not made a typed proposal — it has made a suggestion. Typed columns are falsifiable; prose
columns are not. An ADD-type proposal and a REPRIORITIZE-type proposal are structurally
different change requests. Mixing types in prose removes that distinction and makes the
proposals table non-auditable.

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
document?"* If yes, the cell is a structural alias and is treated as empty. Applies to every
column but is especially critical for `Implicit evidence`.

*Why this matters*: The `Implicit evidence` column exists to make assumptions auditable. If
a reviewer cannot trace the evidence back to a phrase in strategy.md, the column is not doing
its job. A column that can be filled without reading the document is navigational metadata,
not an analytical dimension.

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

Every mandatory null case must appear in the output. A section that runs and finds nothing
is proven by its null row. A missing section is indistinguishable from a section that was
skipped entirely. Every null template in this skill cites Rule 3.

*Why this matters*: Auditable absence requires an explicit declaration. If the Conflict Audit
section is empty because no conflicts exist, that is a finding — not a formatting oversight.
Null rows are evidence that the section ran.

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
column must include the full "Strategy assumed [X] / Signal revealed [Y]" text from the delta
step with the exact finding ID — not just the ID, not just a signal reference.

*Why this matters*: The proposals table should be self-contained. A reviewer should understand
why each change is proposed without returning to the delta section.

Rule 4 PASS examples:
- `F-01: Strategy assumed scout runs before draft / Signal revealed draft completed without scout artifacts`
- `F-03: Strategy assumed no review namespace signals existed / Signal revealed 3 review artifacts unaddressed in strategy`

Rule 4 FAIL examples (treated as absent):
- `F-01` — finding ID only
- `"signal S-01 suggests adding a skill"` — signal reference, no delta structure

---

### Output Schema (read before proceeding to Phase 1)

Every table must conform to this schema. Columns marked ★ are mandatory. All four Contract
Rules apply. Do not omit any ★ column.

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

**Defender Challenge Table** (Step 7b — Rule 1 applies to Defender verdict)
| ★ Proposal ID | ★ Strongest case for no change | ★ Specific cost of changing | ★ Proposal Architect response | ★ Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

Do not omit any ★ column.

---

### PHASE 1 — Pre-read (Steps 1–2)

*No signal files may be read during Phase 1. If you encounter a signal file path, do not
read it — log it in the signal inventory during Phase 2 only.*

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

Apply the COLUMN CONTRACT Rule 2 PASS/FAIL exhibit before populating each
`Implicit evidence` cell.

Column rules: `Contradicted?` = `[pending]` until Step 3b. `Why it matters` = failure
mode if assumption is wrong. `Delta candidate?` = Rule 1 (`yes` / `no`); update to
`yes — F-NN` after Step 4.

The following columns are mandatory. Do not omit any column.

| Assumption | Implicit evidence [Rule 2] | Contradicted by a signal? | Why this matters | Delta candidate? [Rule 1: yes / no] |
|-----------|---------------------------|--------------------------|-----------------|-------------------------------------|
| [most important] | [phrase from strategy.md — Rule 2 test before filling] | [pending] | [failure mode] | yes |

Null case (Rule 3): `| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |`

---

### PHASE 1 GATE

Produce this checkpoint before advancing to Phase 2. If any item is incomplete, stop and
complete it before the gate clears.

| Step | Artifact | Complete? |
|------|----------|-----------|
| Step 1 | Stated-field table — all 5 fields populated, no inferred values | Yes / No |
| Step 2 | Assumption table — all rows, all 5 columns, Rule 2 applied to every `Implicit evidence` cell | Yes / No |

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

*Phase 2 gate cleared. Work only from the signal inventory built in Phase 2 — do not
re-read signal files during this phase.*

---

### Step 3b — Role: Assumption Archaeologist (Back-fill)

Adjudicate each A-NN against all signals. Replace `[pending]` with one of:
- `Contradicted — S-NN`: cite ID, one sentence
- `Supported — S-NN`: cite ID
- `No signal coverage`

Reproduce full updated assumption table. After Step 4, update `yes` rows to `yes — F-NN`.

---

### Step 4 — Role: Delta Identifier

Stop. Write: (1) the anti-pattern label you are guarding against, and (2) a PASS/FAIL
exhibit for the delta vs. inventory distinction. Then fill the findings table.

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

> "Proposals schema committed: Proposal ID ★, Type ★ [Rule 1: ADD / REMOVE / REPRIORITIZE;
> prose not valid], Change ★, Delta Finding ★ [Rule 4: full 'Strategy assumed X / Signal
> revealed Y' text with ID], Evidence ★, If unchanged ★ (no degradation named = preference
> not decision), Reversibility ★ [Rule 1: (1)/(2)/(3); prose not valid], Confidence ★.
> All three types present. Empty types use Rule 3 null rows."

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

Adopt this role: you are the voice of inertia. For each active proposal (non-null rows from
Step 7), articulate the strongest case for leaving strategy.md unchanged. Name the specific
cost of making the change — migration effort, coherence risk, signal thinness, or premature
commitment. Do not argue that the strategy is perfect; argue that this specific change is not
worth the cost at this time.

The following columns are mandatory. Do not omit any column. Rule 1 applies to
`Defender verdict`.

| Proposal ID | Strongest case for no change | Specific cost of changing | Proposal Architect response | Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |
|------------|------------------------------|--------------------------|----------------------------|----------------------------------------------------------------|
| ADD-1 | [why keeping strategy as-is is defensible] | [concrete cost] | [Architect's rebuttal or concession] | Unchanged |

Null case — no active proposals (Rule 3):
`| — | No active proposals — Defender step not applicable | N/A | N/A | N/A |`

After filling the table:
- Mark `Withdrawn` proposals: add "[WITHDRAWN after Defender step]" note to the original row
  in Step 7. These proposals do not appear in the diff.
- Mark `Strengthened` proposals: update the `If unchanged` cell in Step 7 to reflect the
  sharpened degradation case from the Architect's response.
- `Unchanged` proposals: proceed as-is.

---

### Step 8 — Role: Diff Author

Stop. Write this statement verbatim before building the diff table:

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★
> (inline [file.md — ≤10 words] per row), Proposal ★ (ID from Step 7). No column omitted.
> Withdrawn proposals excluded."

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

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed, non-withdrawn
proposals. Preserve existing structure; update only sections affected.

---

## V-02 — Output Format: Unified Per-Column Exhibit

**Axis**: Output format — the CONTRACT's separate PASS list + FAIL list format is replaced
with a single exhibit table per rule. Each rule ends with a table whose rows are the governed
columns (or cases), and whose columns are `PASS value` and `FAIL value`. The exhibit
structure makes C-42 unavoidable: a column can only appear in the PASS column if a FAIL
value occupies the same row.

**Hypothesis**: R13 V-03/V-04/V-05 fail C-42 not because the instruction is missing but
because the instructed format (separate PASS/FAIL lists) makes asymmetry easy — you can add
a new PASS item without noticing you haven't added a FAIL. A unified exhibit table where each
row must have both values makes the omission structurally visible. If correct, V-02 should
achieve C-42/C-43 without explicit mention of symmetry as a requirement — the format enforces
it. If incorrect — the exhibit table format still admits asymmetric rows when a model simply
leaves a FAIL cell empty — the finding is that structural format alone does not substitute
for the instructed requirement.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it was
written. The assumption table is a two-phase artifact: extract at Step 2 (before signal
reading), back-fill at Step 3b (after). After building proposals and running the Defender
challenge, present the confirmed proposal set and wait for YES before writing.
Do not auto-apply.

---

### COLUMN CONTRACT (binding before reading any file)

Four rules govern every table you produce. Each rule ends with an exhibit table. Read all
four exhibit tables before the Output Schema.

**Rule 1 — Enumerated columns**

Any column using a closed value set must declare those values at every point where the column
is named. Select from the declared set only; prose is not a valid value. A cell that contains
paraphrase, conditional prose, or a multi-value selection is treated as empty regardless of
content.

*Why this matters*: Typed columns are falsifiable; prose columns are not. An ADD-type proposal
and a REPRIORITIZE-type proposal are structurally different change requests. Mixing types in
prose makes the proposals table non-auditable.

Rule 1 exhibit (read PASS and FAIL for every row before filling any governed cell):

| Column | PASS value — select from declared set only | FAIL value — treated as absent |
|--------|-------------------------------------------|-------------------------------|
| `Type` | `ADD` \| `REMOVE` \| `REPRIORITIZE` | "I suggest adding..." \| "addition" \| "add/remove" |
| `Reversibility` | `(1) Reversible at same cost` \| `(2) Gets harder` \| `(3) Becomes impossible` | "it will be harder later" \| "probably irreversible" |
| `Delta candidate?` | `yes` \| `no` \| `yes — F-01` \| `yes — F-03` | "probably yes" \| "yes if confirmed" |
| `Consistent with strategy?` | `Yes` \| `No` \| `Partial` | "mostly yes" \| "it's complicated" |
| `Defender verdict` | `Withdrawn` \| `Strengthened` \| `Unchanged` | "maybe we should keep it" \| "partially withdrawn" \| "conditionally accepted" |

**Rule 2 — Column independence**

Before filling any cell, apply this test: *"Can I fill this cell without reading the source
document?"* If yes, the cell is a structural alias and is treated as empty. Applies to every
column but is especially critical for `Implicit evidence`.

*Why this matters*: The `Implicit evidence` column exists to make assumptions auditable. A
column that can be filled without reading the document is navigational metadata, not an
analytical dimension.

Rule 2 exhibit (four paired examples for `Implicit evidence`):

| Example | PASS — traceable to phrase in strategy.md | FAIL — treated as absent |
|---------|------------------------------------------|--------------------------|
| 1 | `"teams run scout before draft"` — specific phrase from strategy.md rationale block | `A-01` — the row key; reconstructible without reading the document |
| 2 | `"signal count threshold never defined"` — gap detected as absent in the text | `"signals gather evidence"` — restatement in different words |
| 3 | `"the phrase 'gather evidence first'"` — verbatim instruction from the document | `"see rationale section"` — pointer with no content |
| 4 | `"no definition of done for this topic appears in the strategy"` — explicit gap notation | `"strategy implies sequencing"` — generic inference not traceable to any phrase |

**Rule 3 — Null completeness**

Every mandatory null case must appear in the output. A section that runs and finds nothing
is proven by its null row. A missing section is indistinguishable from a section that was
skipped entirely. Every null template in this skill cites Rule 3.

*Why this matters*: Auditable absence requires an explicit declaration. Null rows are evidence
that the section ran.

Rule 3 exhibit (three null cases — PASS = explicit null row present; FAIL = section skipped):

| Null case | PASS — section ran, nothing found | FAIL — treated as section skipped |
|-----------|----------------------------------|----------------------------------|
| Conflict section | `\| CF-00 \| — \| — \| No conflicts detected — audit ran \| No action needed \|` (Rule 3) | Empty conflict section with no null row |
| Proposal type rows | `\| ADD-0 \| ADD \| None proposed \| ... \|` + REMOVE-0 + REPRIORITIZE-0 (Rule 3) | Proposals table with only ADD rows; REMOVE/REPRIORITIZE null rows absent |
| Delta step | `\| F-00 \| Strategy confirmed \| No gaps detected \| All signals \| N/A \|` (Rule 3) | Delta step skipped with only "no changes needed" in prose |

**Rule 4 — Two-level traceability**

Every proposal must chain from proposal to delta finding to source signal. The `Delta Finding`
column must include the full "Strategy assumed [X] / Signal revealed [Y]" text with the exact
finding ID — not just the ID, not just a signal reference.

*Why this matters*: The proposals table should be self-contained. A reviewer should understand
why each change is proposed without returning to the delta section.

Rule 4 exhibit (two paired examples for `Delta Finding`):

| Example | PASS — full traceability chain | FAIL — treated as absent |
|---------|-------------------------------|--------------------------|
| 1 | `F-01: Strategy assumed scout runs before draft / Signal revealed draft completed without scout artifacts` | `F-01` — finding ID only |
| 2 | `F-03: Strategy assumed no review signals existed / Signal revealed 3 review artifacts unaddressed in strategy` | `"signal S-01 suggests adding a skill"` — signal reference, no delta structure |

---

### Output Schema (read before proceeding to Step 1)

Every table must conform to this schema. Columns marked ★ are mandatory. All four Contract
Rules apply. Do not omit any ★ column.

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

**Defender Challenge Table** (Step 7b — Rule 1 applies to Defender verdict)
| ★ Proposal ID | ★ Strongest case for no change | ★ Specific cost of changing | ★ Proposal Architect response | ★ Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

Do not omit any ★ column.

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

Extract what strategy.md assumed without writing. Scan dimensions: (a) implied audience
knowledge, (b) namespace priority ordering, (c) signal sufficiency threshold, (d) timeline
feasibility, (e) definition of done.

Apply Rule 2 exhibit before populating each `Implicit evidence` cell.

Column rules: `Contradicted?` = `[pending]` until Step 3b. `Delta candidate?` = Rule 1
(`yes` / `no`); update to `yes — F-NN` after Step 4.

| Assumption | Implicit evidence [Rule 2] | Contradicted by a signal? | Why this matters | Delta candidate? [Rule 1: yes / no] |
|-----------|---------------------------|--------------------------|-----------------|-------------------------------------|
| [most important] | [phrase from strategy.md — Rule 2 exhibit applied] | [pending] | [failure mode] | yes |

Null case (Rule 3): `| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |`

---

### Step 3a — Role: Signal Analyst (Read)

Glob `simulations/{topic}/` recursively. Read every file.

Null case (Rule 3): `> No signals found — strategy.md does not need revision at this time.`

Rule 1: `Consistent with strategy?` = Yes / No / Partial.

| ID | File | Namespace | Skill | Date | Key Finding | Consistent with strategy? [Rule 1: Yes / No / Partial] | Assumption link |
|----|------|-----------|-------|------|-------------|-------------------------------------------------------|----------------|
| S-01 | | | | | | | |

---

### Step 3b — Role: Assumption Archaeologist (Back-fill)

Adjudicate each A-NN against all signals. Replace `[pending]` with one of:
- `Contradicted — S-NN`: cite ID, one sentence
- `Supported — S-NN`: cite ID
- `No signal coverage`

Reproduce full updated assumption table. After Step 4, update `yes` rows to `yes — F-NN`.

---

### Step 4 — Role: Delta Identifier

Stop. Write: (1) the anti-pattern label you are guarding against, and (2) a PASS/FAIL exhibit
for the delta vs. inventory distinction. Then fill the findings table.

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

### Step 7 — Role: Proposal Architect

Stop. Write this statement verbatim before building the proposals table:

> "Proposals schema committed: Proposal ID ★, Type ★ [Rule 1: ADD / REMOVE / REPRIORITIZE;
> prose not valid], Change ★, Delta Finding ★ [Rule 4: full 'Strategy assumed X / Signal
> revealed Y' text with ID], Evidence ★, If unchanged ★ (no degradation named = preference
> not decision), Reversibility ★ [Rule 1: (1)/(2)/(3); prose not valid], Confidence ★.
> All three types present. Empty types use Rule 3 null rows."

| Proposal ID | Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | Change | Delta Finding [Rule 4] | Evidence | If unchanged [specific degradation] | Reversibility [Rule 1: (1)/(2)/(3)] | Confidence |
|------------|------------------------------------------|--------|----------------------|----------|-------------------------------------|-------------------------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [degradation] | (2) Gets harder | High |

Null rows (Rule 3):

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 7b — Role: Status Quo Defender

For each active proposal (non-null rows from Step 7), articulate the strongest case for
leaving strategy.md unchanged. Name the specific cost of making the change — migration
effort, coherence risk, signal thinness, or premature commitment.

Rule 1 applies to `Defender verdict`.

| Proposal ID | Strongest case for no change | Specific cost of changing | Proposal Architect response | Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |
|------------|------------------------------|--------------------------|----------------------------|----------------------------------------------------------------|
| ADD-1 | | | | Unchanged |

Null case — no active proposals (Rule 3):
`| — | No active proposals — Defender step not applicable | N/A | N/A | N/A |`

After filling: mark Withdrawn proposals "[WITHDRAWN after Defender step]" in Step 7.
Strengthened proposals: update `If unchanged` in Step 7. Unchanged: proceed as-is.

---

### Step 8 — Role: Diff Author

Stop. Write this statement verbatim:

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★
> (inline [file.md — ≤10 words] per row), Proposal ★ (ID from Step 7). No column omitted.
> Withdrawn proposals excluded."

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current text] | [proposed text] | [file.md — ≤10 words] | ADD-1 |

---

### Step 9 — Confirmation gate

Reply **YES** to apply all non-withdrawn proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 10 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed, non-withdrawn
proposals. Preserve existing structure; update only sections affected.

---

## V-03 — Inertia Framing: Pre-emptive Threshold Defender

**Axis**: Inertia framing — the Status Quo Defender runs BEFORE the Proposal Architect.
At Step 6b (after conflict detection), the Defender produces a Change Warrant Table stating
the minimum evidence threshold each change type must meet. At Step 7, the Proposal Architect
must match every proposed row against the warrant criteria before the row enters the table.
Proposals that do not meet the warrant are excluded at inception — they never reach the
proposals table. There is no post-hoc challenge step (no Step 7b).

**Hypothesis**: In R13 V-01, proposals are built first, then challenged. A proposal with weak
`If unchanged` evidence can survive the Defender if the Architect's rebuttal is plausible
rather than evidenced. Moving the Defender to before proposal generation forces the Architect
to build proposals against pre-set thresholds, not post-hoc justifications. A proposal backed
by thin evidence fails the warrant gate before it is written. If correct, V-03 should produce
fewer proposals overall but with higher average evidence density and sharper `If unchanged`
degradation cases. If incorrect — warrant criteria are set so loosely that every proposal
clears the gate — the finding is that threshold-first framing only helps when the warrant
calibration is tight.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it was
written. The assumption table is a two-phase artifact: extract at Step 2 (before signal
reading), back-fill at Step 3b (after). Before proposals are built, a pre-emptive Defender
sets evidence thresholds for each change type. The Proposal Architect then matches every
candidate proposal against the warrant criteria — only warrant-cleared proposals enter the
table. Present the confirmed set, wait for YES before writing. Do not auto-apply.

---

### COLUMN CONTRACT (binding before reading any file)

Four rules govern every table you produce. Read all four before the Output Schema.

**Rule 1 — Enumerated columns**

Any column using a closed value set must declare those values at every point where the column
is named. Select from the declared set only; prose is not a valid value.

*Why this matters*: Typed columns are falsifiable; prose columns are not. The `Warrant met?`
column is the gate that prevents preference-only proposals from entering the table. A cell
that says "mostly yes" or "warrant partially met" provides no gate — it is prose.

Rule 1 PASS examples:
- `Type`: `ADD` | `REMOVE` | `REPRIORITIZE`
- `Reversibility`: `(1) Reversible at same cost` | `(2) Gets harder` | `(3) Becomes impossible`
- `Delta candidate?`: `yes` | `no` | `yes — F-01` | `yes — F-03`
- `Consistent with strategy?`: `Yes` | `No` | `Partial`
- `Warrant met?`: `Yes` | `No`

Rule 1 FAIL examples (treated as absent):
- `Type`: "I suggest adding..." | "addition" | "add/remove"
- `Reversibility`: "it will be harder later" | "probably irreversible"
- `Delta candidate?`: "probably yes" | "yes if confirmed"
- `Consistent with strategy?`: "mostly yes" | "it's complicated"
- `Warrant met?`: "mostly yes" | "warrant partially met" | "yes with caveats"

**Rule 2 — Column independence**

Before filling any cell, apply this test: *"Can I fill this cell without reading the source
document?"* If yes, the cell is a structural alias and is treated as empty. Applies especially
to `Implicit evidence`.

*Why this matters*: The `Implicit evidence` column exists to make assumptions auditable.
A column that can be filled without reading the document is navigational metadata, not an
analytical dimension.

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

Every mandatory null case must appear in the output. A section that runs and finds nothing
is proven by its null row. Every null template in this skill cites Rule 3.

*Why this matters*: Auditable absence requires an explicit declaration. Null rows are evidence
that the section ran.

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

*Why this matters*: The proposals table should be self-contained.

Rule 4 PASS examples:
- `F-01: Strategy assumed scout runs before draft / Signal revealed draft completed without scout artifacts`
- `F-03: Strategy assumed no review signals existed / Signal revealed 3 review artifacts unaddressed in strategy`

Rule 4 FAIL examples (treated as absent):
- `F-01` — finding ID only
- `"signal S-01 suggests adding a skill"` — signal reference, no delta structure

---

### Output Schema (read before proceeding to Step 1)

Every table must conform to this schema. Columns marked ★ are mandatory. All four Contract
Rules apply. Do not omit any ★ column.

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

**Change Warrant Table** (Step 6b — Defender pre-empts proposal generation)
| ★ Change type [Rule 1: ADD / REMOVE / REPRIORITIZE] | ★ Minimum evidence threshold | ★ Signal quality required | ★ If threshold not met |

**Proposals** (Rules 1 and 4 apply — only warrant-cleared proposals enter)
| ★ Proposal ID | ★ Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | ★ Change | ★ Delta Finding [Rule 4: full "Strategy assumed X / Signal revealed Y" + ID] | ★ Evidence | ★ If unchanged | ★ Reversibility [Rule 1: (1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible] | ★ Warrant met? [Rule 1: Yes / No] | ★ Confidence |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

Do not omit any ★ column.

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

Extract what strategy.md assumed without writing. Scan dimensions: (a) implied audience
knowledge, (b) namespace priority ordering, (c) signal sufficiency threshold, (d) timeline
feasibility, (e) definition of done.

Apply Rule 2 PASS/FAIL exhibit before populating each `Implicit evidence` cell.

Column rules: `Contradicted?` = `[pending]` until Step 3b. `Delta candidate?` = Rule 1
(`yes` / `no`); update to `yes — F-NN` after Step 4.

| Assumption | Implicit evidence [Rule 2] | Contradicted by a signal? | Why this matters | Delta candidate? [Rule 1: yes / no] |
|-----------|---------------------------|--------------------------|-----------------|-------------------------------------|
| [most important] | [phrase from strategy.md] | [pending] | [failure mode] | yes |

Null case (Rule 3): `| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |`

---

### Step 3a — Role: Signal Analyst (Read)

Glob `simulations/{topic}/` recursively. Read every file.

Null case (Rule 3): `> No signals found — strategy.md does not need revision at this time.`

Rule 1: `Consistent with strategy?` = Yes / No / Partial.

| ID | File | Namespace | Skill | Date | Key Finding | Consistent with strategy? [Rule 1: Yes / No / Partial] | Assumption link |
|----|------|-----------|-------|------|-------------|-------------------------------------------------------|----------------|
| S-01 | | | | | | | |

---

### Step 3b — Role: Assumption Archaeologist (Back-fill)

Adjudicate each A-NN. Replace `[pending]` with one of:
- `Contradicted — S-NN`: cite ID, one sentence
- `Supported — S-NN`: cite ID
- `No signal coverage`

Reproduce full updated assumption table. After Step 4, update `yes` rows to `yes — F-NN`.

---

### Step 4 — Role: Delta Identifier

Stop. Write: (1) the anti-pattern label you are guarding against, and (2) a PASS/FAIL exhibit
for the delta vs. inventory distinction. Then fill the findings table.

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

### Step 6b — Role: Pre-emptive Defender (Change Warrant)

Adopt this role: you are the threshold-setter. Before any proposals are built, define the
minimum evidence requirements that a proposal must meet to enter the proposals table. Set
thresholds by change type. Be specific: name the signal quality floor, the delta finding
requirement, and what happens if the threshold is not met.

A warrant threshold that is met by every possible proposal regardless of evidence quality
is not a threshold — it is no gate at all. Each `Minimum evidence threshold` cell must name
a condition that would cause a real proposal to fail the warrant.

The following columns are mandatory. Do not omit any column.

| Change type [Rule 1: ADD / REMOVE / REPRIORITIZE] | Minimum evidence threshold | Signal quality required | If threshold not met |
|--------------------------------------------------|---------------------------|------------------------|----------------------|
| ADD | [e.g., at least one direct delta finding (F-NN) + signal that is not strategy.md itself] | [e.g., H or M — stub signals do not warrant ADD proposals] | Proposal excluded from table; logged as "warrant not cleared" |
| REMOVE | | | |
| REPRIORITIZE | | | |

---

### Step 7 — Role: Proposal Architect (Warrant-gated)

Stop. Write this statement verbatim before building the proposals table:

> "Proposals schema committed: Proposal ID ★, Type ★ [Rule 1: ADD / REMOVE / REPRIORITIZE;
> prose not valid], Change ★, Delta Finding ★ [Rule 4: full 'Strategy assumed X / Signal
> revealed Y' text with ID], Evidence ★, If unchanged ★ (no degradation named = preference
> not decision), Reversibility ★ [Rule 1: (1)/(2)/(3); prose not valid], Warrant met? ★
> [Rule 1: Yes / No; No = excluded], Confidence ★. All three types present. Empty types
> use Rule 3 null rows."

For each candidate proposal, apply the Change Warrant criteria from Step 6b. Fill
`Warrant met?` = `Yes` or `No` before filling any other cell in that row. Rows where
`Warrant met?` = `No` are excluded from the diff — they may appear in the table labeled
`[EXCLUDED — warrant not met]` but do not generate diff rows.

| Proposal ID | Type [Rule 1] | Change | Delta Finding [Rule 4] | Evidence | If unchanged [specific degradation] | Reversibility [Rule 1] | Warrant met? [Rule 1: Yes / No] | Confidence |
|------------|--------------|--------|----------------------|----------|-------------------------------------|------------------------|--------------------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [degradation] | (2) Gets harder | Yes | High |

Null rows (Rule 3):

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | N/A | — |

---

### Step 8 — Role: Diff Author

Stop. Write this statement verbatim:

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★
> (inline [file.md — ≤10 words] per row), Proposal ★ (ID from Step 7). No column omitted.
> Excluded proposals omitted."

Only warrant-cleared proposals (`Warrant met?` = `Yes`) generate diff rows.

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current text] | [proposed text] | [file.md — ≤10 words] | ADD-1 |

---

### Step 9 — Confirmation gate

Reply **YES** to apply all warrant-cleared proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 10 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed, warrant-cleared
proposals. Preserve existing structure; update only sections affected.

---

## V-04 — Lifecycle + Unified Exhibit (V-01 + V-02)

**Axes**: Lifecycle emphasis with phase gates (V-01) + output format unified per-column
exhibit tables in the CONTRACT (V-02).

**Hypothesis**: V-01 addresses cross-phase contamination — pre-read artifacts stay clean
because a gate blocks signal reading until Phase 1 is complete. V-02 addresses column
asymmetry in the CONTRACT — exhibit tables make C-42/C-43 structurally unavoidable. These
target independent failure modes: V-01 guards the temporal axis (when things are read),
V-02 guards the structural axis (whether PASS and FAIL coverage is symmetric). Combined,
V-04 should produce assumption tables that are genuinely pre-read and CONTRACT exhibits that
are column-complete across all four rules. If the combination introduces friction that reduces
output quality elsewhere (e.g., steps abbreviated to manage length), the finding is that the
two axes interact negatively and should not be combined.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it was
written. Execution is organized into four phases; complete each phase and pass its checkpoint
gate before opening the next. The assumption table is a two-phase artifact: extract at Step 2
(Phase 1, before any signal reading), back-fill at Step 3b (Phase 3, after reading). After
building proposals and running the Defender challenge, present the confirmed set and wait for
YES before writing. Do not auto-apply.

---

### COLUMN CONTRACT (binding before reading any file)

Four rules govern every table you produce. Each rule ends with an exhibit table.
Read all four before the Output Schema.

**Rule 1 — Enumerated columns**

Any column using a closed value set must declare those values at every point where the column
is named. Select from the declared set only; prose is not a valid value.

*Why this matters*: Typed columns are falsifiable; prose columns are not. Mixing types in
prose makes the proposals table non-auditable.

Rule 1 exhibit:

| Column | PASS value — select from declared set only | FAIL value — treated as absent |
|--------|-------------------------------------------|-------------------------------|
| `Type` | `ADD` \| `REMOVE` \| `REPRIORITIZE` | "I suggest adding..." \| "addition" \| "add/remove" |
| `Reversibility` | `(1) Reversible at same cost` \| `(2) Gets harder` \| `(3) Becomes impossible` | "it will be harder later" \| "probably irreversible" |
| `Delta candidate?` | `yes` \| `no` \| `yes — F-01` \| `yes — F-03` | "probably yes" \| "yes if confirmed" |
| `Consistent with strategy?` | `Yes` \| `No` \| `Partial` | "mostly yes" \| "it's complicated" |
| `Defender verdict` | `Withdrawn` \| `Strengthened` \| `Unchanged` | "maybe we should keep it" \| "partially withdrawn" \| "conditionally accepted" |

**Rule 2 — Column independence**

Before filling any cell, apply this test: *"Can I fill this cell without reading the source
document?"* If yes, the cell is empty. Applies especially to `Implicit evidence`.

*Why this matters*: The `Implicit evidence` column makes assumptions auditable. A column
that can be filled without reading the document is navigational metadata, not analysis.

Rule 2 exhibit:

| Example | PASS — traceable to phrase in strategy.md | FAIL — treated as absent |
|---------|------------------------------------------|--------------------------|
| 1 | `"teams run scout before draft"` — specific phrase from strategy.md rationale block | `A-01` — the row key; reconstructible without reading |
| 2 | `"signal count threshold never defined"` — gap detected as absent in the text | `"signals gather evidence"` — restatement in different words |
| 3 | `"the phrase 'gather evidence first'"` — verbatim instruction from the document | `"see rationale section"` — pointer with no content |
| 4 | `"no definition of done for this topic appears in the strategy"` — explicit gap notation | `"strategy implies sequencing"` — generic inference not traceable to any phrase |

**Rule 3 — Null completeness**

Every mandatory null case must appear in the output. Every null template cites Rule 3.

*Why this matters*: Auditable absence requires explicit declaration. Null rows are evidence
that the section ran.

Rule 3 exhibit:

| Null case | PASS — section ran, nothing found | FAIL — treated as section skipped |
|-----------|----------------------------------|----------------------------------|
| Conflict section | `\| CF-00 \| — \| — \| No conflicts detected — audit ran \| No action needed \|` (Rule 3) | Empty conflict section with no null row |
| Proposal type rows | `\| ADD-0 \| ADD \| None proposed \| ... \|` + REMOVE-0 + REPRIORITIZE-0 (Rule 3) | Proposals table with only ADD rows; REMOVE/REPRIORITIZE null rows absent |
| Delta step | `\| F-00 \| Strategy confirmed \| No gaps detected \| All signals \| N/A \|` (Rule 3) | Delta step skipped with only "no changes needed" in prose |

**Rule 4 — Two-level traceability**

Every proposal must chain: proposal → delta finding (full text + ID) → source signal. The
`Delta Finding` column = full "Strategy assumed [X] / Signal revealed [Y]" + ID.

*Why this matters*: The proposals table should be self-contained.

Rule 4 exhibit:

| Example | PASS — full traceability chain | FAIL — treated as absent |
|---------|-------------------------------|--------------------------|
| 1 | `F-01: Strategy assumed scout runs before draft / Signal revealed draft completed without scout artifacts` | `F-01` — finding ID only |
| 2 | `F-03: Strategy assumed no review signals existed / Signal revealed 3 review artifacts unaddressed in strategy` | `"signal S-01 suggests adding a skill"` — no delta structure |

---

### Output Schema (read before proceeding to Phase 1)

Every table must conform to this schema. Columns marked ★ are mandatory. All four Contract
Rules apply. Do not omit any ★ column.

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

**Defender Challenge Table** (Step 7b — Rule 1: Defender verdict)
| ★ Proposal ID | ★ Strongest case for no change | ★ Specific cost of changing | ★ Proposal Architect response | ★ Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

Do not omit any ★ column.

---

### PHASE 1 — Pre-read (Steps 1–2)

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

Extract what strategy.md assumed without writing. Scan: (a) audience knowledge, (b) namespace
priority ordering, (c) signal sufficiency, (d) timeline feasibility, (e) definition of done.

Apply Rule 2 exhibit before each `Implicit evidence` cell.

`Contradicted?` = `[pending]` until Step 3b. `Delta candidate?` = Rule 1 (`yes` / `no`).

| Assumption | Implicit evidence [Rule 2] | Contradicted by a signal? | Why this matters | Delta candidate? [Rule 1: yes / no] |
|-----------|---------------------------|--------------------------|-----------------|-------------------------------------|
| [most important] | [phrase from strategy.md — Rule 2 exhibit applied] | [pending] | [failure mode] | yes |

Null case (Rule 3): `| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |`

---

### PHASE 1 GATE

| Step | Artifact | Complete? |
|------|----------|-----------|
| Step 1 | Stated-field table — all 5 fields, no inferred values | Yes / No |
| Step 2 | Assumption table — all rows, all 5 columns, Rule 2 exhibit applied to each `Implicit evidence` cell | Yes / No |

All rows "Yes". Declare: **Phase 1 complete. Opening Phase 2 (Read).**

---

### PHASE 2 — Read (Step 3a)

*Phase 1 gate cleared. Signal files may now be read.*

---

### Step 3a — Role: Signal Analyst (Read)

Glob `simulations/{topic}/` recursively. Read every file.

Null case (Rule 3): `> No signals found — strategy.md does not need revision at this time.`

Rule 1: `Consistent with strategy?` = Yes / No / Partial.

| ID | File | Namespace | Skill | Date | Key Finding | Consistent with strategy? [Rule 1: Yes / No / Partial] | Assumption link |
|----|------|-----------|-------|------|-------------|-------------------------------------------------------|----------------|
| S-01 | | | | | | | |

---

### PHASE 2 GATE

| Step | Artifact | Complete? |
|------|----------|-----------|
| Step 3a | Signal inventory — all files read, all 8 columns populated | Yes / No |

All rows "Yes". Declare: **Phase 2 complete. Opening Phase 3 (Analysis).**

---

### PHASE 3 — Analysis (Steps 3b–6)

*Phase 2 gate cleared. Work from signal inventory only — do not re-read signal files.*

---

### Step 3b — Role: Assumption Archaeologist (Back-fill)

Replace `[pending]`: `Contradicted — S-NN` | `Supported — S-NN` | `No signal coverage`

Reproduce full updated assumption table. After Step 4, update `yes` rows to `yes — F-NN`.

---

### Step 4 — Role: Delta Identifier

Stop. Write: (1) anti-pattern label, (2) PASS/FAIL exhibit. Then fill findings table.

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
| Step 3b | Assumption table back-filled — all [pending] replaced, yes rows updated to yes — F-NN | Yes / No |
| Step 4 | Delta findings — anti-pattern named, PASS/FAIL exhibit written | Yes / No |
| Step 5 | Namespace audit — all 9 namespaces present | Yes / No |
| Step 6 | Conflict audit — null row present if no conflicts | Yes / No |

All rows "Yes". Declare: **Phase 3 complete. Opening Phase 4 (Build).**

---

### PHASE 4 — Build (Steps 7–10)

*Phase 3 gate cleared.*

---

### Step 7 — Role: Proposal Architect

Stop. Write this statement verbatim before building the proposals table:

> "Proposals schema committed: Proposal ID ★, Type ★ [Rule 1: ADD / REMOVE / REPRIORITIZE;
> prose not valid], Change ★, Delta Finding ★ [Rule 4: full 'Strategy assumed X / Signal
> revealed Y' text with ID], Evidence ★, If unchanged ★ (no degradation named = preference
> not decision), Reversibility ★ [Rule 1: (1)/(2)/(3); prose not valid], Confidence ★.
> All three types present. Empty types use Rule 3 null rows."

| Proposal ID | Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | Change | Delta Finding [Rule 4] | Evidence | If unchanged [specific degradation] | Reversibility [Rule 1: (1)/(2)/(3)] | Confidence |
|------------|------------------------------------------|--------|----------------------|----------|-------------------------------------|-------------------------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [degradation] | (2) Gets harder | High |

Null rows (Rule 3):

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 7b — Role: Status Quo Defender

For each active proposal, articulate the strongest case for leaving strategy.md unchanged.
Name the specific cost of the change. Rule 1 applies to `Defender verdict`.

| Proposal ID | Strongest case for no change | Specific cost of changing | Proposal Architect response | Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |
|------------|------------------------------|--------------------------|----------------------------|----------------------------------------------------------------|
| ADD-1 | | | | Unchanged |

Null case — no active proposals (Rule 3):
`| — | No active proposals — Defender step not applicable | N/A | N/A | N/A |`

After filling: mark Withdrawn "[WITHDRAWN after Defender step]" in Step 7. Strengthened:
update `If unchanged`. Unchanged: proceed as-is.

---

### Step 8 — Role: Diff Author

Stop. Write this statement verbatim:

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★
> (inline [file.md — ≤10 words] per row), Proposal ★. No column omitted.
> Withdrawn proposals excluded."

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current text] | [proposed text] | [file.md — ≤10 words] | ADD-1 |

---

### Step 9 — Confirmation gate

Reply **YES** to apply all non-withdrawn proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 10 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed, non-withdrawn
proposals. Preserve existing structure; update only sections affected.

---

## V-05 — Full Ceiling (V-01 + V-02 + V-03 + CONTRACT Exhibit Audit)

**Axes**: Lifecycle phase gates (V-01) + unified per-column exhibit tables (V-02) +
pre-emptive threshold Defender (V-03) + a self-referential CONTRACT Exhibit Audit that must
clear before Phase 1 opens.

**Hypothesis**: V-04 addresses temporal contamination (phase gates) and column asymmetry
(exhibit tables). V-03 addresses proposal quality (threshold-first Defender). The CONTRACT
Exhibit Audit adds a meta-step: before any execution begins, the model produces a table
confirming that each rule's PASS and FAIL coverage is symmetric. A rule that fails the audit
must be corrected before the model proceeds. This is the maximum structural depth available
to enforce C-42 and C-43 simultaneously. If correct, V-05 should score highest on all
four C-42/C-43-adjacent criteria (C-38, C-39, C-42, C-43) and demonstrate that self-audit
of the CONTRACT before execution outperforms instructed enforcement. If incorrect — the audit
table is filled mechanically without triggering genuine corrections — the finding is that
self-referential audits require genuine consequence (forced rewrite) to be load-bearing.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it was
written. Before Phase 1 opens, you must complete the CONTRACT Exhibit Audit — a self-check
confirming that each rule's PASS and FAIL examples cover identical columns. Execution is then
organized into four phases with checkpoint gates. The assumption table is a two-phase
artifact: extract at Step 2 (Phase 1), back-fill at Step 3b (Phase 3). Before proposals are
built, a pre-emptive Defender sets evidence thresholds. Present the confirmed proposal set
and wait for YES before writing. Do not auto-apply.

---

### COLUMN CONTRACT (binding before the CONTRACT Exhibit Audit)

Four rules govern every table you produce. Each rule ends with an exhibit table. After all
four rules, a CONTRACT Exhibit Audit step must pass before Phase 1 opens.

**Rule 1 — Enumerated columns**

Any column using a closed value set must declare those values at every point where the column
is named. Select from the declared set only; prose is not a valid value.

*Why this matters*: Typed columns are falsifiable; prose columns are not. The `Warrant met?`
column is the pre-emptive gate; the typed values are the only valid gate values.

Rule 1 exhibit:

| Column | PASS value — select from declared set only | FAIL value — treated as absent |
|--------|-------------------------------------------|-------------------------------|
| `Type` | `ADD` \| `REMOVE` \| `REPRIORITIZE` | "I suggest adding..." \| "addition" \| "add/remove" |
| `Reversibility` | `(1) Reversible at same cost` \| `(2) Gets harder` \| `(3) Becomes impossible` | "it will be harder later" \| "probably irreversible" |
| `Delta candidate?` | `yes` \| `no` \| `yes — F-01` \| `yes — F-03` | "probably yes" \| "yes if confirmed" |
| `Consistent with strategy?` | `Yes` \| `No` \| `Partial` | "mostly yes" \| "it's complicated" |
| `Warrant met?` | `Yes` \| `No` | "mostly yes" \| "warrant partially met" \| "yes with caveats" |

**Rule 2 — Column independence**

Before filling any cell: *"Can I fill this cell without reading the source document?"*
If yes, the cell is empty. Applies especially to `Implicit evidence`.

*Why this matters*: The `Implicit evidence` column makes assumptions auditable. A column
that can be filled without reading the document is navigational metadata.

Rule 2 exhibit:

| Example | PASS — traceable to phrase in strategy.md | FAIL — treated as absent |
|---------|------------------------------------------|--------------------------|
| 1 | `"teams run scout before draft"` — specific phrase from strategy.md rationale block | `A-01` — the row key; reconstructible without reading |
| 2 | `"signal count threshold never defined"` — gap detected as absent in the text | `"signals gather evidence"` — restatement in different words |
| 3 | `"the phrase 'gather evidence first'"` — verbatim instruction from the document | `"see rationale section"` — pointer with no content |
| 4 | `"no definition of done for this topic appears in the strategy"` — explicit gap notation | `"strategy implies sequencing"` — generic inference |

**Rule 3 — Null completeness**

Every mandatory null case must appear in the output. Every null template cites Rule 3.

*Why this matters*: Auditable absence requires explicit declaration.

Rule 3 exhibit:

| Null case | PASS — section ran, nothing found | FAIL — treated as section skipped |
|-----------|----------------------------------|----------------------------------|
| Conflict section | `\| CF-00 \| — \| — \| No conflicts detected — audit ran \| No action needed \|` (Rule 3) | Empty conflict section with no null row |
| Proposal type rows | `\| ADD-0 \| ADD \| None proposed \| ... \|` + REMOVE-0 + REPRIORITIZE-0 (Rule 3) | Proposals table with only ADD rows; REMOVE/REPRIORITIZE null rows absent |
| Delta step | `\| F-00 \| Strategy confirmed \| No gaps detected \| All signals \| N/A \|` (Rule 3) | Delta step skipped with only "no changes needed" in prose |

**Rule 4 — Two-level traceability**

Every proposal chains: proposal → delta finding (full text + ID) → source signal.

*Why this matters*: The proposals table should be self-contained.

Rule 4 exhibit:

| Example | PASS — full traceability chain | FAIL — treated as absent |
|---------|-------------------------------|--------------------------|
| 1 | `F-01: Strategy assumed scout runs before draft / Signal revealed draft completed without scout artifacts` | `F-01` — finding ID only |
| 2 | `F-03: Strategy assumed no review signals existed / Signal revealed 3 review artifacts unaddressed in strategy` | `"signal S-01 suggests adding a skill"` — no delta structure |

---

### CONTRACT Exhibit Audit (complete before Phase 1 opens)

Produce this self-check table now. Count the columns or cases covered by PASS examples and
by FAIL examples in each rule's exhibit. If any rule shows "No" in the Symmetric? column,
rewrite that rule's exhibit to add the missing FAIL values before proceeding. Do not advance
to Phase 1 until all rows show "Yes".

| Rule | Columns or null cases governed | PASS coverage (list columns/cases) | FAIL coverage (list columns/cases) | Symmetric? |
|------|-------------------------------|------------------------------------|------------------------------------|------------|
| Rule 1 | Type, Reversibility, Delta candidate?, Consistent with strategy?, Warrant met? | [list] | [list] | Yes / No |
| Rule 2 | Implicit evidence (4 paired examples) | [count] | [count] | Yes / No |
| Rule 3 | Conflict null, Proposal type null (ADD/REMOVE/REPRIORITIZE), Delta null | [list] | [list] | Yes / No |
| Rule 4 | Delta Finding (2 paired examples) | [count] | [count] | Yes / No |

All rows must show "Yes". If any row shows "No": identify the missing FAIL coverage, add it
to the rule's exhibit above, then update this row to "Yes". Do not proceed until the table
is all "Yes".

Declare: **CONTRACT Exhibit Audit passed. Opening Phase 1.**

---

### Output Schema (read before Phase 1)

Every table must conform to this schema. Columns marked ★ are mandatory. All four Contract
Rules apply. Do not omit any ★ column.

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

**Change Warrant Table** (Step 6b)
| ★ Change type [Rule 1: ADD / REMOVE / REPRIORITIZE] | ★ Minimum evidence threshold | ★ Signal quality required | ★ If threshold not met |

**Proposals** (Rules 1 and 4 apply — warrant-cleared rows only)
| ★ Proposal ID | ★ Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | ★ Change | ★ Delta Finding [Rule 4: full "Strategy assumed X / Signal revealed Y" + ID] | ★ Evidence | ★ If unchanged | ★ Reversibility [Rule 1: (1) Reversible at same cost / (2) Gets harder / (3) Becomes impossible] | ★ Warrant met? [Rule 1: Yes / No] | ★ Confidence |

**Diff**
| ★ Namespace | ★ Skill/Area | ★ Before | ★ After | ★ Evidence | ★ Proposal |

Do not omit any ★ column.

---

### PHASE 1 — Pre-read (Steps 1–2)

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

Extract what strategy.md assumed without writing. Scan: (a) audience knowledge,
(b) namespace priority ordering, (c) signal sufficiency, (d) timeline feasibility,
(e) definition of done.

Apply Rule 2 exhibit before each `Implicit evidence` cell.

`Contradicted?` = `[pending]` until Step 3b. `Delta candidate?` = Rule 1 (`yes` / `no`).

| Assumption | Implicit evidence [Rule 2] | Contradicted by a signal? | Why this matters | Delta candidate? [Rule 1: yes / no] |
|-----------|---------------------------|--------------------------|-----------------|-------------------------------------|
| [most important] | [phrase from strategy.md — Rule 2 exhibit applied] | [pending] | [failure mode] | yes |

Null case (Rule 3): `| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |`

---

### PHASE 1 GATE

| Step | Artifact | Complete? |
|------|----------|-----------|
| Step 1 | Stated-field table — all 5 fields, no inferred values | Yes / No |
| Step 2 | Assumption table — all rows, all 5 columns, Rule 2 exhibit applied to every `Implicit evidence` cell | Yes / No |

All rows "Yes". Declare: **Phase 1 complete. Opening Phase 2 (Read).**

---

### PHASE 2 — Read (Step 3a)

*Phase 1 gate cleared. Signal files may now be read.*

---

### Step 3a — Role: Signal Analyst (Read)

Glob `simulations/{topic}/` recursively. Read every file.

Null case (Rule 3): `> No signals found — strategy.md does not need revision at this time.`

Rule 1: `Consistent with strategy?` = Yes / No / Partial.

| ID | File | Namespace | Skill | Date | Key Finding | Consistent with strategy? [Rule 1: Yes / No / Partial] | Assumption link |
|----|------|-----------|-------|------|-------------|-------------------------------------------------------|----------------|
| S-01 | | | | | | | |

---

### PHASE 2 GATE

| Step | Artifact | Complete? |
|------|----------|-----------|
| Step 3a | Signal inventory — all files read, all 8 columns populated | Yes / No |

All rows "Yes". Declare: **Phase 2 complete. Opening Phase 3 (Analysis).**

---

### PHASE 3 — Analysis (Steps 3b–6)

*Phase 2 gate cleared. Work from signal inventory only.*

---

### Step 3b — Role: Assumption Archaeologist (Back-fill)

Replace `[pending]`: `Contradicted — S-NN` | `Supported — S-NN` | `No signal coverage`

Reproduce full updated assumption table. After Step 4, update `yes` rows to `yes — F-NN`.

---

### Step 4 — Role: Delta Identifier

Stop. Write: (1) anti-pattern label, (2) PASS/FAIL exhibit. Then fill findings table.

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

### Step 6b — Role: Pre-emptive Defender (Change Warrant)

Before any proposals are built, set the minimum evidence thresholds. A threshold that every
possible proposal meets regardless of evidence quality is not a threshold.

| Change type [Rule 1: ADD / REMOVE / REPRIORITIZE] | Minimum evidence threshold | Signal quality required | If threshold not met |
|--------------------------------------------------|---------------------------|------------------------|----------------------|
| ADD | | | Proposal excluded — logged as "warrant not cleared" |
| REMOVE | | | |
| REPRIORITIZE | | | |

---

### PHASE 3 GATE

| Step | Artifact | Complete? |
|------|----------|-----------|
| Step 3b | Assumption table back-filled — all [pending] replaced, yes rows → yes — F-NN | Yes / No |
| Step 4 | Delta findings — anti-pattern named, PASS/FAIL exhibit written | Yes / No |
| Step 5 | Namespace audit — all 9 namespaces present | Yes / No |
| Step 6 | Conflict audit — null row present if no conflicts | Yes / No |
| Step 6b | Change Warrant Table — all three change types have thresholds | Yes / No |

All rows "Yes". Declare: **Phase 3 complete. Opening Phase 4 (Build).**

---

### PHASE 4 — Build (Steps 7–10)

*Phase 3 gate cleared.*

---

### Step 7 — Role: Proposal Architect (Warrant-gated)

Stop. Write this statement verbatim before building the proposals table:

> "Proposals schema committed: Proposal ID ★, Type ★ [Rule 1: ADD / REMOVE / REPRIORITIZE;
> prose not valid], Change ★, Delta Finding ★ [Rule 4: full 'Strategy assumed X / Signal
> revealed Y' text with ID], Evidence ★, If unchanged ★ (no degradation named = preference
> not decision), Reversibility ★ [Rule 1: (1)/(2)/(3); prose not valid], Warrant met? ★
> [Rule 1: Yes / No; No = excluded], Confidence ★. All three types present. Empty types
> use Rule 3 null rows."

For each candidate proposal: fill `Warrant met?` = `Yes` or `No` before any other cell.
`No` rows are labeled `[EXCLUDED — warrant not met]` and do not appear in the diff.

| Proposal ID | Type [Rule 1] | Change | Delta Finding [Rule 4] | Evidence | If unchanged [specific degradation] | Reversibility [Rule 1] | Warrant met? [Rule 1: Yes / No] | Confidence |
|------------|--------------|--------|----------------------|----------|-------------------------------------|------------------------|--------------------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [degradation] | (2) Gets harder | Yes | High |

Null rows (Rule 3):

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | N/A | — |

---

### Step 8 — Role: Diff Author

Stop. Write this statement verbatim:

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★
> (inline [file.md — ≤10 words] per row), Proposal ★. No column omitted.
> Excluded proposals omitted."

Only rows with `Warrant met?` = `Yes` generate diff entries.

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current text] | [proposed text] | [file.md — ≤10 words] | ADD-1 |

---

### Step 9 — Confirmation gate

Reply **YES** to apply all warrant-cleared proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 10 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed, warrant-cleared
proposals. Preserve existing structure; update only sections affected.
