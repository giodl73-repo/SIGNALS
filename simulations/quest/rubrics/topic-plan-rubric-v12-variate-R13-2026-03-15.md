# topic-plan — Round 13 Variations (v12 rubric)

**Skill**: `topic:plan`
**Rubric**: v12 (C-01–C-41, 255 pts total)
**Date**: 2026-03-15

---

## Round 13 Design Notes

R12 V-02 achieved the highest scores under v11 and introduced the discriminating mechanisms
for v12's two new criteria:

- **C-40** — Null-case enforcement consolidated in COLUMN CONTRACT rule: Rule 3 in CONTRACT
  + every null-case site cites "(Rule 3)" inline. R12 V-02 satisfies this via "Null case
  (Rule 3):" label before every null template. R12 V-01/V-03 score PARTIAL — the null
  template appears without the "(Rule 3)" citation at Steps 3a/4/7.
- **C-41** — Schema column definitions carry inline rule-reference annotations: every
  enumerated-value column carries `[Rule N: ...]` in the schema header. R12 V-02 satisfies
  this for Type, Reversibility, Delta candidate?, Consistent with strategy?. R12 V-01/V-03
  pass C-36 without inline annotations, leaving the governing rule implicit at column level.

**All R13 variations preserve C-40 and C-41 as floor requirements:**
- 4-rule CONTRACT is the minimum CONTRACT structure (Rules 1-4)
- Every null-case site must have "(Rule 3)" inline
- Every enumerated-value column in the schema must carry `[Rule N: ...]` annotation

**Three single-axis dimensions explored in R13:**

1. **Inertia framing**: A "Status Quo Defender" role is inserted after the Proposal
   Architect step. The Defender articulates the strongest case for leaving the strategy
   unchanged, challenge by challenge, before the diff is built. Tests whether forcing
   explicit counter-argument before writing reduces preference-only proposals.

2. **Output format — scoring scale**: The proposals table gains an `★ Urgency [Rule 5:
   U-1 to U-5]` column, defined by a five-level scale in the CONTRACT. The signal
   inventory gains a `★ Signal quality [Rule 5: H / M / L]` column. Tests whether
   quantified urgency forces proposal discrimination that confidence alone does not.

3. **Role sequence — prediction-first**: After the Assumption Archaeologist extracts
   assumptions (Step 2) and before any signal reading (Step 3a), a Step 2b "Delta
   Predictor" requires the model to commit to specific predicted delta findings. After
   Step 4 (Delta Identifier), a Step 4b "Prediction Accuracy Audit" scores each
   prediction against actual findings. Tests whether pre-commitment reduces
   reverse-engineered delta claims.

**Variation design:**

| Variation | Axis | Type | Primary R13 target |
|-----------|------|------|--------------------|
| V-01 | Inertia framing — Status Quo Defender | Single | Proposal discrimination (C-07, C-08) |
| V-02 | Output format — scoring scale (U-1 to U-5) | Single | Proposal urgency calibration |
| V-03 | Role sequence — prediction-first before signal reading | Single | Delta fabrication prevention (C-03, C-09) |
| V-04 | Inertia framing + scoring scale (V-01 + V-02) | Combination | Challenged proposals + quantified urgency |
| V-05 | Full ceiling — V-01 + V-02 + V-03 + expanded CONTRACT + pre-read hypothesis | Combination | Maximum structural depth |

---

## V-01 — Inertia Framing: Status Quo Defender

**Axis**: Inertia framing — after the Proposal Architect builds proposals (Step 7), a
Status Quo Defender role (Step 7b) generates the strongest case for leaving strategy
unchanged, one objection per proposal. The Proposal Architect (Step 7c) responds to each
objection before the Diff Author proceeds.

**Hypothesis**: Without an explicit counter-argument step, proposals can survive on
preference alone — an `ADD` proposal backed by weak evidence passes if no competing
force challenges it. Inserting a Defender that articulates the cost of change (migration
effort, strategy coherence, signal thinness) forces the Proposal Architect to either
sharpen the `If unchanged` degradation case or retract the proposal. If correct, V-01
should produce fewer low-confidence proposals and sharper `If unchanged` cells. If
incorrect — the Defender step produces no retractions and `If unchanged` cells remain
generic — the finding is that counter-argument pressure is not load-bearing for proposal
quality.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it
was written. The assumption table is a two-phase artifact: extract at Step 2 (before
signal reading), back-fill at Step 3b (after). After building proposals, a Status Quo
Defender will challenge each one — address every objection before the diff is built.
Present the confirmed proposal set, then wait for YES before writing. Do not auto-apply.

---

### COLUMN CONTRACT (binding before reading any file)

Four rules govern every table you produce. Read all four before the Output Schema.

**Rule 1 — Enumerated columns**

Any column using a closed value set must declare those values at every point where the
column is named. Select from the declared set only; prose is not a valid value. A cell
that contains paraphrase, conditional prose, or a multi-value selection is treated as
empty regardless of content.

*Why this matters*: A model that sees `Type` and writes "I think we should add a new
skill" has not made a typed proposal — it has made a suggestion. Typed columns are
falsifiable; prose columns are not. An ADD-type proposal and a REPRIORITIZE-type proposal
are structurally different change requests. Mixing types in prose removes that distinction
and makes the proposals table non-auditable.

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

Before filling any cell, apply this test: *"Can I fill this cell without reading the
source document?"* If yes, the cell is a structural alias and is treated as empty.
Applies to every column but is especially critical for `Implicit evidence`.

*Why this matters*: The `Implicit evidence` column exists to make assumptions auditable.
If a reviewer cannot trace the evidence back to a phrase in strategy.md, the column is
not doing its job. A column that can be filled without reading the document is navigational
metadata, not an analytical dimension.

Rule 2 PASS examples for `Implicit evidence`:
- PASS: `"teams run scout before draft"` — specific phrase from strategy.md rationale block
- PASS: `"signal count threshold never defined"` — gap detected as absent in the text
- PASS: `"the phrase 'gather evidence first'"` — verbatim instruction from the document
- PASS: `"no definition of done for this topic appears in the strategy"` — explicit gap notation

Rule 2 FAIL examples (treated as absent):
- FAIL: `A-01` — the row key; reconstructible without reading the document
- FAIL: `"signals gather evidence"` — restatement in different words
- FAIL: `"see rationale section"` — pointer with no content
- FAIL: `"strategy implies sequencing"` — generic inference not traceable to any phrase

**Rule 3 — Null completeness**

Every mandatory null case must appear in the output. A section that runs and finds nothing
is proven by its null row. A missing section is indistinguishable from a section that was
skipped entirely. Every null template in this skill cites Rule 3.

*Why this matters*: Auditable absence requires an explicit declaration. If the Conflict
Audit section is empty because no conflicts exist, that is a finding — not a formatting
oversight. Null rows are evidence that the section ran.

Rule 3 PASS examples:
- Conflict null: `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |` (Rule 3)
- ADD null: `| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |` (Rule 3)
- Delta null: `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |` (Rule 3)

Rule 3 FAIL (treated as section skipped):
- Empty conflict section with no null row
- Proposals table with only ADD rows and no REMOVE / REPRIORITIZE null rows
- Delta step skipped with only "no changes needed" in prose

**Rule 4 — Two-level traceability**

Every proposal must chain from proposal to delta finding to source signal. The `Delta
Finding` column must include the full "Strategy assumed [X] / Signal revealed [Y]" text
from the delta step with the exact finding ID — not just the ID, not just a signal reference.

*Why this matters*: The proposals table should be self-contained. A reviewer should
understand why each change is proposed without returning to the delta section.

Rule 4 PASS example:
- `F-01: Strategy assumed scout runs before draft / Signal revealed draft completed without scout artifacts`

Rule 4 FAIL examples:
- `F-01` — finding ID only
- `"signal S-01 suggests adding a skill"` — signal reference, no delta structure

---

### Output Schema (read before proceeding to Step 1)

Every table must conform to this schema. Columns marked ★ are mandatory. All four
Contract Rules apply. Do not omit any ★ column.

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

### Step 3a — Role: Signal Analyst (Read)

Glob `simulations/{topic}/` recursively. Read every file.

Null case (Rule 3): `> No signals found — strategy.md does not need revision at this time.`

The following columns are mandatory. Rule 1: `Consistent with strategy?` = Yes / No / Partial.

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

Adopt this role: you are the voice of inertia. For each active proposal (non-null rows
from Step 7), articulate the strongest case for leaving strategy.md unchanged. Name the
specific cost of making the change — migration effort, coherence risk, signal thinness,
or premature commitment. Do not argue that the strategy is perfect; argue that this
specific change is not worth the cost at this time.

The following columns are mandatory. Do not omit any column. Rule 1 applies to
`Defender verdict`.

| Proposal ID | Strongest case for no change | Specific cost of changing | Proposal Architect response | Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |
|------------|------------------------------|--------------------------|----------------------------|----------------------------------------------------------------|
| ADD-1 | [why keeping strategy as-is is defensible] | [concrete cost: e.g., "removes current scout-first ordering, requiring 3 skill resequences"] | [Architect's rebuttal or concession] | Unchanged |

Null case — no active proposals (Rule 3):
`| — | No active proposals — Defender step not applicable | N/A | N/A | N/A |`

After filling the table:
- Mark `Withdrawn` proposals: add a note to the original proposal row in Step 7 as
  "[WITHDRAWN after Defender step]". These proposals do not appear in the diff.
- Mark `Strengthened` proposals: update the `If unchanged` cell in Step 7 to reflect
  the sharpened degradation case from the Architect's response.
- `Unchanged` proposals: proceed as-is.

---

### Step 8 — Role: Diff Author

Stop. Write this statement verbatim before building the diff table:

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★
> (inline [file.md — ≤10 words] per row), Proposal ★ (ID from Step 7). No column
> omitted. Withdrawn proposals excluded."

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

## V-02 — Output Format: Scoring Scale

**Axis**: Output format — the proposals table gains a mandatory `★ Urgency [Rule 5:
U-1 to U-5]` column defined by a five-level scale in the CONTRACT (Rule 5). The signal
inventory gains a `★ Signal quality [Rule 5: H / M / L]` column. A fifth rule is added
to the CONTRACT defining both scales.

**Hypothesis**: R12 V-02's `Confidence` column (High/Med/Low) captures epistemic
certainty about whether a finding is real. `Urgency` captures a distinct dimension:
how costly it is to defer the proposal. A strategy proposal backed by a strong signal
but low urgency is appropriate to defer; a weak signal with high urgency warrants
provisional action. Separating these dimensions should force the model to distinguish
"I'm confident this is right" from "this gets worse if we wait." If correct, urgency
scores should correlate with Reversibility values — U-4/U-5 proposals should have (2)
or (3) Reversibility. Signal quality forces discrimination at the inventory step rather
than the proposal step, earlier in the chain.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it
was written. The assumption table is a two-phase artifact: extract at Step 2 (before
signal reading), back-fill at Step 3b (after). Present proposals, wait for confirmation,
then write. Do not auto-apply changes.

---

### COLUMN CONTRACT (binding before reading any file)

Five rules govern every table you produce. Read all five before the Output Schema.

**Rule 1 — Enumerated columns**

Any column using a closed value set must declare those values at every point where the
column is named. Select from the declared set only; prose is not a valid value.

Rule 1 PASS examples:
- `Type`: `ADD` | `REMOVE` | `REPRIORITIZE`
- `Reversibility`: `(1) Reversible at same cost` | `(2) Gets harder` | `(3) Becomes impossible`
- `Delta candidate?`: `yes` | `no` | `yes — F-01`
- `Consistent with strategy?`: `Yes` | `No` | `Partial`

Rule 1 FAIL examples (treated as absent):
- `Type`: "I suggest adding..." | "addition" | "add/remove"
- `Reversibility`: "gets harder over time" | "might be irreversible"
- `Delta candidate?`: "probably yes" | "yes if confirmed"
- `Consistent with strategy?`: "mostly yes" | "it's complicated"

**Rule 2 — Column independence**

Before filling any cell, apply this test: *"Can I fill this cell without reading the
source document?"* If yes, the cell is a structural alias and is treated as empty.
Applies especially to `Implicit evidence`.

*Why this matters*: The `Implicit evidence` column exists to make assumptions auditable.
If a reviewer cannot trace the evidence back to a phrase in strategy.md, the column is
not doing its job.

Rule 2 PASS examples for `Implicit evidence`:
- PASS: `"teams run scout before draft"` — phrase from strategy.md rationale block
- PASS: `"signal count threshold never defined"` — gap detected as absent in the text
- PASS: `"the phrase 'gather evidence first'"` — verbatim instruction from the document

Rule 2 FAIL examples (treated as absent):
- FAIL: `A-01` — the row key
- FAIL: `"signals gather evidence"` — restatement in different words
- FAIL: `"see rationale section"` — pointer with no content
- FAIL: `"strategy implies sequencing"` — generic inference

**Rule 3 — Null completeness**

Every mandatory null case must appear in the output. A section that runs and finds nothing
is proven by its null row. A missing section is indistinguishable from a section that was
skipped entirely. Every null template in this skill cites Rule 3.

Rule 3 PASS examples:
- Conflict null: `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |` (Rule 3)
- ADD null: `| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | U-0 | — |` (Rule 3)
- Delta null: `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |` (Rule 3)

Rule 3 FAIL: empty sections with no null row; missing change types with no null row.

**Rule 4 — Two-level traceability**

Every proposal must chain from proposal to delta finding to source signal. The `Delta
Finding` column must include the full "Strategy assumed [X] / Signal revealed [Y]" text
with the exact finding ID — not just the ID.

Rule 4 PASS: `F-01: Strategy assumed scout runs before draft / Signal revealed draft completed without scout artifacts`
Rule 4 FAIL: `F-01` alone | `"signal S-01 suggests adding a skill"`

**Rule 5 — Scoring scales**

Two scoring scales apply to specific columns. Select from the defined levels only;
prose is not a valid value. Intermediate values are not valid.

*Urgency scale* — applies to the `Urgency` column in the Proposals table:

| Level | Meaning |
|-------|---------|
| U-1 | Cosmetic — deferring has no compounding cost |
| U-2 | Low — strategy still works without this, but gaps grow slowly |
| U-3 | Medium — a cohort of signals will be misclassified until addressed |
| U-4 | High — each sprint without this change actively misdirects signal gathering |
| U-5 | Critical — the strategy is structurally incorrect; continued use causes harm |

*Signal quality scale* — applies to the `Signal quality` column in the Signal Inventory:

| Level | Meaning |
|-------|---------|
| H | High — artifact is complete, dated, namespace-and-skill-tagged, finding is specific |
| M | Medium — artifact exists but is partial, undated, or finding is generic |
| L | Low — artifact is a stub, draft, or finding is not extractable |

Rule 5 FAIL examples (treated as absent):
- `Urgency`: "high-ish" | "medium to high" | "urgent" | "3.5"
- `Signal quality`: "pretty good" | "okay" | "high/medium" | "HM"

---

### Output Schema (read before proceeding to Step 1)

Every table must conform to this schema. Columns marked ★ are mandatory. All five
Contract Rules apply. Do not omit any ★ column.

**Assumption Table** (5 columns — all independently populated per Rule 2)
| ★ Assumption | ★ Implicit evidence [Rule 2 — PASS: phrase/paraphrase from strategy.md | FAIL: row key / restatement / pointer] | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? [Rule 1: yes / no / yes — F-NN] |

**Signal Inventory** (Rule 5 applies to Signal quality)
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? [Rule 1: Yes / No / Partial] | ★ Assumption link (A-NN / "stated field" / "none") | ★ Signal quality [Rule 5: H / M / L] |

**Delta Findings**
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) | ★ Assumption root (A-NN / "stated field") |

**Namespace Audit**
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |

**Conflict Audit**
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals** (Rules 1, 4, and 5 apply)
| ★ Proposal ID | ★ Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | ★ Change | ★ Delta Finding [Rule 4: full "Strategy assumed X / Signal revealed Y" + ID] | ★ Evidence | ★ If unchanged | ★ Reversibility [Rule 1: (1)/(2)/(3)] | ★ Urgency [Rule 5: U-1 / U-2 / U-3 / U-4 / U-5] | ★ Confidence |

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

---

### Step 2 — Role: Assumption Archaeologist (Extract)

Extract what strategy.md assumed without writing. Scan dimensions: (a) audience
knowledge, (b) namespace priority ordering, (c) signal sufficiency threshold,
(d) timeline feasibility, (e) definition of done.

Apply the COLUMN CONTRACT Rule 2 PASS/FAIL exhibit before populating each
`Implicit evidence` cell.

Column rules: `Contradicted?` = `[pending]` until Step 3b. `Why it matters` = failure
mode if wrong. `Delta candidate?` = Rule 1 (`yes` / `no`); update to `yes — F-NN`
after Step 4.

The following columns are mandatory. Do not omit any column.

| Assumption | Implicit evidence [Rule 2] | Contradicted by a signal? | Why this matters | Delta candidate? [Rule 1: yes / no] |
|-----------|---------------------------|--------------------------|-----------------|-------------------------------------|
| [most important] | [phrase from strategy.md] | [pending] | [failure mode] | yes |

Null case (Rule 3): `| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |`

---

### Step 3a — Role: Signal Analyst (Read)

Glob `simulations/{topic}/` recursively. Read every file.

Null case (Rule 3): `> No signals found — strategy.md does not need revision at this time.`

Rule 1: `Consistent with strategy?` = Yes / No / Partial. Rule 5: `Signal quality` = H / M / L.

The following columns are mandatory.

| ID | File | Namespace | Skill | Date | Key Finding | Consistent with strategy? [Rule 1] | Assumption link | Signal quality [Rule 5: H / M / L] |
|----|------|-----------|-------|------|-------------|-----------------------------------|----------------|-------------------------------------|
| S-01 | | | | | | | | |

---

### Step 3b — Role: Assumption Archaeologist (Back-fill)

Adjudicate each A-NN. Replace `[pending]`:
- `Contradicted — S-NN`: cite ID, one sentence
- `Supported — S-NN`: cite ID
- `No signal coverage`

Reproduce full updated assumption table. After Step 4, update `yes` rows to `yes — F-NN`.

---

### Step 4 — Role: Delta Identifier

Stop. Write: (1) the anti-pattern label you are guarding against, (2) a PASS/FAIL
exhibit. Then fill the findings table.

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

### Step 7 — Role: Proposal Architect

Stop. Write this statement verbatim before building the proposals table:

> "Proposals schema committed: Proposal ID ★, Type ★ [Rule 1: ADD / REMOVE / REPRIORITIZE;
> prose not valid], Change ★, Delta Finding ★ [Rule 4: full 'Strategy assumed X / Signal
> revealed Y' text with ID], Evidence ★, If unchanged ★ (no degradation named = preference
> not decision), Reversibility ★ [Rule 1: (1)/(2)/(3); prose not valid], Urgency ★ [Rule 5:
> U-1 to U-5; prose not valid], Confidence ★. All three types present. Empty types use
> Rule 3 null rows."

Before assigning `Urgency`, apply the Rule 5 scale: U-5 = structural harm now; U-4 =
misdirects signal gathering each sprint; U-3 = some signals misclassified; U-2 = slow
gap growth; U-1 = cosmetic. U-4 or U-5 proposals must have Reversibility (2) or (3) —
if they do not, revisit Reversibility before proceeding.

The following columns are mandatory. Do not omit any column.

| Proposal ID | Type [Rule 1] | Change | Delta Finding [Rule 4] | Evidence | If unchanged | Reversibility [Rule 1] | Urgency [Rule 5: U-1/U-2/U-3/U-4/U-5] | Confidence |
|------------|--------------|--------|----------------------|----------|-------------|----------------------|----------------------------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [degradation] | (2) Gets harder | U-3 | High |

Null rows (Rule 3):

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | U-0 | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | U-0 | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | U-0 | — |

---

### Step 8 — Role: Diff Author

Stop. Write this statement verbatim before building the diff table:

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★
> (inline [file.md — ≤10 words] per row), Proposal ★ (ID from Step 7). No column omitted."

The following columns are mandatory.

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current text] | [proposed text] | [file.md — ≤10 words] | ADD-1 |

---

### Step 9 — Confirmation gate

Reply **YES** to apply all proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 10 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals. Preserve
existing structure; update only sections affected.

---

## V-03 — Role Sequence: Prediction-First

**Axis**: Role sequence — after the Assumption Archaeologist extracts assumptions at
Step 2 but before any signal is read (Step 3a), a Step 2b "Delta Predictor" requires
the model to commit to specific predicted delta findings. After Step 4 (Delta Identifier),
a Step 4b "Prediction Accuracy Audit" compares each prediction against actual findings
and labels each delta finding as `Predicted — P-NN` or `Surprise`.

**Hypothesis**: In the standard sequence, the model reads signals before identifying
deltas. A model that commits to "Strategy assumed X / Signal will likely reveal Y"
before reading cannot easily reverse-engineer a finding from the signal it just read.
The prediction step makes the delta identification falsifiable: a finding that matches a
prediction is evidence of genuine assumption-based reasoning; a finding with no matching
prediction is a surprise (valuable) or reverse-engineered (suspect). If correct, V-03
should produce higher-quality delta claims traceable to specific pre-committed assumptions.
If incorrect — predictions are vague or the accuracy audit fails to discriminate —
the finding is that pre-commitment does not reduce reverse-engineering under the current
prompt structure.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it
was written. The assumption table is a two-phase artifact: extract at Step 2 (before
signal reading), back-fill at Step 3b (after). Before reading signals, you will commit
to specific predicted delta findings. After identifying actual deltas, you will audit
prediction accuracy. Present proposals, wait for confirmation, then write.
Do not auto-apply changes.

---

### COLUMN CONTRACT (binding before reading any file)

Four rules govern every table you produce. Read all four before the Output Schema.

**Rule 1 — Enumerated columns**

Any column using a closed value set must declare those values at every point where the
column is named. Select from the declared set only; prose is not a valid value.

Rule 1 PASS examples:
- `Type`: `ADD` | `REMOVE` | `REPRIORITIZE`
- `Reversibility`: `(1) Reversible at same cost` | `(2) Gets harder` | `(3) Becomes impossible`
- `Delta candidate?`: `yes` | `no` | `yes — F-01`
- `Consistent with strategy?`: `Yes` | `No` | `Partial`
- `Prediction match`: `Predicted — P-NN` | `Surprise`

Rule 1 FAIL examples (treated as absent):
- `Type`: "add a skill" | "addition" | "add/remove"
- `Reversibility`: "gets harder later" | "might be irreversible"
- `Delta candidate?`: "probably yes" | "yes if confirmed"
- `Prediction match`: "mostly predicted" | "close to P-01" | "partially predicted"

**Rule 2 — Column independence**

Before filling any cell, apply this test: *"Can I fill this cell without reading the
source document?"* If yes, the cell is a structural alias and is treated as empty.

Rule 2 PASS examples for `Implicit evidence`:
- PASS: `"teams run scout before draft"` — phrase from strategy.md rationale block
- PASS: `"signal count threshold never defined"` — gap detected as absent in the text
- PASS: `"the phrase 'gather evidence first'"` — verbatim instruction

Rule 2 FAIL examples (treated as absent):
- FAIL: `A-01` — the row key
- FAIL: `"signals gather evidence"` — restatement
- FAIL: `"see rationale section"` — pointer without content
- FAIL: `"strategy implies sequencing"` — generic inference

**Rule 3 — Null completeness**

Every mandatory null case must appear in the output. A section that runs and finds nothing
is proven by its null row. A missing section is indistinguishable from a section that
was skipped entirely. Every null template in this skill cites Rule 3.

Rule 3 PASS examples:
- Conflict null: `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |` (Rule 3)
- ADD null: `| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |` (Rule 3)
- Delta null: `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A | Surprise |` (Rule 3)
- Prediction null: `| P-00 | No predictions committed — assumptions insufficient for prediction | N/A |` (Rule 3)

Rule 3 FAIL: empty sections with no null row; missing change types with no null row.

**Rule 4 — Two-level traceability**

Every proposal must chain from proposal to delta finding to source signal. The `Delta
Finding` column must include the full "Strategy assumed [X] / Signal revealed [Y]" text
with the exact finding ID.

Rule 4 PASS: `F-01: Strategy assumed scout runs before draft / Signal revealed draft completed without scout artifacts`
Rule 4 FAIL: `F-01` alone | `"S-01 suggests adding a skill"`

---

### Output Schema (read before proceeding to Step 1)

Every table must conform to this schema. Columns marked ★ are mandatory. All four
Contract Rules apply. Do not omit any ★ column.

**Assumption Table** (5 columns — all independently populated per Rule 2)
| ★ Assumption | ★ Implicit evidence [Rule 2 — PASS: phrase/paraphrase from strategy.md | FAIL: row key / restatement / pointer] | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? [Rule 1: yes / no / yes — F-NN] |

**Prediction Table** (Step 2b — committed before signal reading)
| ★ Prediction ID | ★ Assumption source (A-NN) | ★ Predicted: Strategy assumed [X] | ★ Predicted: Signal will reveal [Y] | ★ Confidence before reading |

**Signal Inventory**
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? [Rule 1: Yes / No / Partial] | ★ Assumption link (A-NN / "stated field" / "none") |

**Delta Findings** (Rule 1 applies to Prediction match)
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) | ★ Assumption root (A-NN / "stated field") | ★ Prediction match [Rule 1: Predicted — P-NN / Surprise] |

**Prediction Accuracy Audit** (Step 4b)
| ★ Prediction ID | ★ Predicted delta | ★ Actual finding (F-NN / "No match") | ★ Verdict | ★ Implication |

**Namespace Audit**
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |

**Conflict Audit**
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals** (Rules 1 and 4 apply)
| ★ Proposal ID | ★ Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | ★ Change | ★ Delta Finding [Rule 4: full "Strategy assumed X / Signal revealed Y" + ID] | ★ Evidence | ★ If unchanged | ★ Reversibility [Rule 1: (1)/(2)/(3)] | ★ Confidence |

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

---

### Step 2 — Role: Assumption Archaeologist (Extract)

Extract what strategy.md assumed without writing. Scan dimensions: (a) audience
knowledge, (b) namespace priority ordering, (c) signal sufficiency threshold,
(d) timeline feasibility, (e) definition of done.

Apply the COLUMN CONTRACT Rule 2 PASS/FAIL exhibit before populating each
`Implicit evidence` cell.

Column rules: `Contradicted?` = `[pending]` until Step 3b. `Delta candidate?` = Rule 1.

The following columns are mandatory. Do not omit any column.

| Assumption | Implicit evidence [Rule 2] | Contradicted by a signal? | Why this matters | Delta candidate? [Rule 1: yes / no] |
|-----------|---------------------------|--------------------------|-----------------|-------------------------------------|
| [most important] | [phrase from strategy.md] | [pending] | [failure mode] | yes |

Null case (Rule 3): `| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |`

---

### Step 2b — Role: Delta Predictor

Stop. You have not yet read any signal files. Based solely on what strategy.md stated
(Step 1) and the assumptions you extracted (Step 2), commit to specific predicted delta
findings now.

A valid prediction has this form:
- `Predicted: Strategy assumed [exact claim from Step 1 or A-NN] / Signal will likely reveal [specific contradiction or gap]`

A prediction that could be written without reading strategy.md is not a prediction — it
is a generic concern. Apply the Rule 2 test: could you write this prediction without having
read strategy.md? If yes, sharpen it until the answer is no.

PASS predictions (tied to specific strategy content):
- PASS: `A-02: Strategy assumed scout signals were required before draft / Signal will likely reveal: draft skills have run without scout coverage`
- PASS: `Stated field: no acknowledgment of prove coverage / Signal will likely reveal: prove namespace has zero artifacts despite stated stage`

FAIL predictions (treated as absent — too generic to be falsifiable):
- FAIL: `"Some signals may contradict the strategy"` — applicable to any skill invocation
- FAIL: `"The strategy may need updating"` — not a prediction
- FAIL: `P-01: Signal may reveal gaps"` — not tied to any stated assumption

The following columns are mandatory. Do not omit any column.

| Prediction ID | Assumption source (A-NN / "stated field") | Predicted: Strategy assumed [X] | Predicted: Signal will reveal [Y] | Confidence before reading |
|--------------|------------------------------------------|--------------------------------|-----------------------------------|--------------------------|
| P-01 | A-NN | [from Step 1 or 2] | [specific contradiction] | High / Med / Low |

Null case (Rule 3): `| P-00 | No predictions committed — assumptions insufficient for prediction | N/A | N/A | N/A |`

Do not read any signal files until this table is complete.

---

### Step 3a — Role: Signal Analyst (Read)

Predictions are committed. Now read signals.

Glob `simulations/{topic}/` recursively. Read every file.

Null case (Rule 3): `> No signals found — strategy.md does not need revision at this time.`

Rule 1: `Consistent with strategy?` = Yes / No / Partial.

The following columns are mandatory.

| ID | File | Namespace | Skill | Date | Key Finding | Consistent with strategy? [Rule 1] | Assumption link |
|----|------|-----------|-------|------|-------------|-----------------------------------|----------------|
| S-01 | | | | | | | |

---

### Step 3b — Role: Assumption Archaeologist (Back-fill)

Adjudicate each A-NN. Replace `[pending]`:
- `Contradicted — S-NN`: cite ID, one sentence
- `Supported — S-NN`: cite ID
- `No signal coverage`

Reproduce full updated assumption table. After Step 4, update `yes` rows to `yes — F-NN`.

---

### Step 4 — Role: Delta Identifier

Stop. Write: (1) the anti-pattern label you are guarding against, (2) a PASS/FAIL exhibit.
Then fill the findings table.

For each finding, check your prediction table (Step 2b): does this finding match a
prediction? If yes, mark `Predicted — P-NN`. If no, mark `Surprise`.

The following columns are mandatory. Do not omit any column. Rule 1 applies to
`Prediction match`.

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root | Prediction match [Rule 1: Predicted — P-NN / Surprise] |
|-----------|-----------------|----------------|-----------------|----------------|--------------------------------------------------------|
| F-01 | | | S-XX | | Predicted — P-01 |

Null case (Rule 3): `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A | Surprise |`

After findings, return to Step 3b and update `yes` rows to `yes — F-NN`.

---

### Step 4b — Role: Prediction Accuracy Auditor

For each prediction (P-01, P-02, ...) from Step 2b, find its matching delta finding.
If no actual finding matches the prediction, record "No match."

After auditing, write one sentence: what the prediction accuracy implies about the
quality of the assumption extraction at Step 2.

The following columns are mandatory. Do not omit any column.

| Prediction ID | Predicted delta | Actual finding (F-NN / "No match") | Verdict | Implication |
|--------------|-----------------|-------------------------------------|---------|-------------|
| P-01 | [prediction text] | F-01 | Confirmed | [what this reveals about assumption quality] |

Null case (Rule 3): `| P-00 | No predictions to audit | N/A | N/A | N/A |`

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

### Step 7 — Role: Proposal Architect

Stop. Write this statement verbatim before building the proposals table:

> "Proposals schema committed: Proposal ID ★, Type ★ [Rule 1: ADD / REMOVE / REPRIORITIZE;
> prose not valid], Change ★, Delta Finding ★ [Rule 4: full 'Strategy assumed X / Signal
> revealed Y' text with ID], Evidence ★, If unchanged ★ (no degradation named = preference
> not decision), Reversibility ★ [Rule 1: (1)/(2)/(3); prose not valid], Confidence ★.
> All three types present. Empty types use Rule 3 null rows."

The following columns are mandatory. Do not omit any column.

| Proposal ID | Type [Rule 1] | Change | Delta Finding [Rule 4] | Evidence | If unchanged | Reversibility [Rule 1] | Confidence |
|------------|--------------|--------|----------------------|----------|-------------|----------------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [degradation] | (2) Gets harder | High |

Null rows (Rule 3):

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | — |

---

### Step 8 — Role: Diff Author

Stop. Write this statement verbatim before building the diff table:

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★
> (inline [file.md — ≤10 words] per row), Proposal ★ (ID from Step 7). No column omitted."

The following columns are mandatory.

| Namespace | Skill/Area | Before | After | Evidence | Proposal |
|-----------|-----------|--------|-------|----------|---------|
| | | [current text] | [proposed text] | [file.md — ≤10 words] | ADD-1 |

---

### Step 9 — Confirmation gate

Reply **YES** to apply all proposals to `simulations/{topic}/strategy.md`.

Waiting.

---

### Step 10 — Apply (only after YES)

Rewrite `simulations/{topic}/strategy.md` incorporating all confirmed proposals. Preserve
existing structure; update only sections affected.

---

## V-04 — Inertia Framing + Scoring Scale (V-01 + V-02)

**Axes**: Inertia framing (Status Quo Defender challenges each proposal — V-01) +
Output format scoring scale (Urgency U-1 to U-5, Signal quality H/M/L — V-02).

**Hypothesis**: V-01 tests whether counter-argument pressure sharpens proposals. V-02
tests whether quantified urgency forces discrimination. V-04 combines them: proposals
that survive the Defender's challenge must also carry a calibrated urgency score. The
hypothesis is that the combination produces a ratchet — only proposals worth the change
cost AND worth acting on now survive both filters. If correct, V-04 should produce a
smaller proposal set with higher average urgency scores and sharper degradation cases.
If incorrect — the Defender step and the urgency score are redundant — the finding is
that one of the two mechanisms is doing the discriminating work while the other adds
noise.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it
was written. The assumption table is a two-phase artifact: extract at Step 2 (before
signal reading), back-fill at Step 3b (after). After building proposals, a Status Quo
Defender challenges each one before the diff is built. Proposals carry urgency scores.
Present the confirmed set, wait for YES before writing. Do not auto-apply.

---

### COLUMN CONTRACT (binding before reading any file)

Five rules govern every table you produce. Read all five before the Output Schema.

**Rule 1 — Enumerated columns**

Any column using a closed value set must declare those values at every point where the
column is named. Select from the declared set only; prose is not a valid value.

Rule 1 PASS examples:
- `Type`: `ADD` | `REMOVE` | `REPRIORITIZE`
- `Reversibility`: `(1) Reversible at same cost` | `(2) Gets harder` | `(3) Becomes impossible`
- `Delta candidate?`: `yes` | `no` | `yes — F-01`
- `Consistent with strategy?`: `Yes` | `No` | `Partial`
- `Defender verdict`: `Withdrawn` | `Strengthened` | `Unchanged`

Rule 1 FAIL (treated as absent):
- `Type`: "add a skill" | "addition" | "add/remove"
- `Reversibility`: "gets harder" | "probably irreversible"
- `Defender verdict`: "maybe withdrawn" | "conditionally kept" | "partially withdrawn"

**Rule 2 — Column independence**

Before filling any cell: *"Can I fill this without reading the source document?"* If yes,
the cell is empty. Applies especially to `Implicit evidence`.

Rule 2 PASS: `"teams run scout before draft"` | `"signal count threshold never defined"`
Rule 2 FAIL: `A-01` | `"signals gather evidence"` | `"see rationale"` | `"strategy implies sequencing"`

**Rule 3 — Null completeness**

Every section that runs must show its result. Absence is a finding. Every null template
in this skill cites Rule 3.

Rule 3 PASS:
- `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |` (Rule 3)
- `| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | U-0 | — |` (Rule 3)
- `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |` (Rule 3)
- `| — | No active proposals — Defender step not applicable | N/A | N/A | N/A |` (Rule 3)

Rule 3 FAIL: empty sections with no null row; missing type rows without null rows.

**Rule 4 — Two-level traceability**

Every proposal must chain: proposal → delta finding (full text + ID) → source signal.
`Delta Finding` column = full "Strategy assumed [X] / Signal revealed [Y]" + finding ID.

Rule 4 PASS: `F-01: Strategy assumed scout runs before draft / Signal revealed draft completed without scout artifacts`
Rule 4 FAIL: `F-01` | `"S-01 suggests adding a skill"`

**Rule 5 — Scoring scales**

Two scoring scales apply to specific columns. Select from defined levels only.

*Urgency scale* (applies to `Urgency` column in Proposals):

| Level | Meaning |
|-------|---------|
| U-1 | Cosmetic — deferring has no compounding cost |
| U-2 | Low — strategy still works, gaps grow slowly |
| U-3 | Medium — a cohort of signals will be misclassified until addressed |
| U-4 | High — each sprint without this change actively misdirects signal gathering |
| U-5 | Critical — strategy is structurally incorrect; continued use causes harm |

*Signal quality scale* (applies to `Signal quality` column in Signal Inventory):

| Level | Meaning |
|-------|---------|
| H | High — complete, dated, namespace+skill-tagged, specific finding |
| M | Medium — partial, undated, or finding is generic |
| L | Low — stub, draft, or finding not extractable |

Rule 5 FAIL: `"high-ish"` | `"medium to high"` | `"3.5"` | `"HM"` | `"urgent"`

---

### Output Schema (read before proceeding to Step 1)

Every table must conform to this schema. ★ columns are mandatory. All five Contract Rules
apply. Do not omit any ★ column.

**Assumption Table** (5 columns — independently populated per Rule 2)
| ★ Assumption | ★ Implicit evidence [Rule 2 — PASS: phrase from strategy.md | FAIL: row key / restatement / pointer] | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? [Rule 1: yes / no / yes — F-NN] |

**Signal Inventory** (Rule 5: Signal quality)
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? [Rule 1: Yes / No / Partial] | ★ Assumption link | ★ Signal quality [Rule 5: H / M / L] |

**Delta Findings**
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) | ★ Assumption root |

**Namespace Audit**
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |

**Conflict Audit**
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals** (Rules 1, 4, 5 apply)
| ★ Proposal ID | ★ Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | ★ Change | ★ Delta Finding [Rule 4] | ★ Evidence | ★ If unchanged | ★ Reversibility [Rule 1: (1)/(2)/(3)] | ★ Urgency [Rule 5: U-1/U-2/U-3/U-4/U-5] | ★ Confidence |

**Defender Challenge Table** (Step 7b — Rule 1: Defender verdict)
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

Extract what strategy.md assumed without writing. Scan: (a) audience knowledge,
(b) namespace priority ordering, (c) signal sufficiency, (d) timeline, (e) definition of done.

Apply Rule 2 PASS/FAIL before each `Implicit evidence` cell.

| Assumption | Implicit evidence [Rule 2] | Contradicted? | Why this matters | Delta candidate? [Rule 1] |
|-----------|---------------------------|--------------|-----------------|--------------------------|
| [most important] | [phrase from strategy.md] | [pending] | [failure mode] | yes |

Null case (Rule 3): `| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |`

---

### Step 3a — Role: Signal Analyst (Read)

Glob `simulations/{topic}/` recursively. Read every file.

Null case (Rule 3): `> No signals found — strategy.md does not need revision at this time.`

Rules 1 and 5 apply.

| ID | File | Namespace | Skill | Date | Key Finding | Consistent with strategy? [Rule 1] | Assumption link | Signal quality [Rule 5: H / M / L] |
|----|------|-----------|-------|------|-------------|-----------------------------------|----------------|-------------------------------------|
| S-01 | | | | | | | | |

---

### Step 3b — Role: Assumption Archaeologist (Back-fill)

Replace each `[pending]`: `Contradicted — S-NN` | `Supported — S-NN` | `No signal coverage`

Reproduce full updated assumption table. After Step 4, update `yes` rows to `yes — F-NN`.

---

### Step 4 — Role: Delta Identifier

Write: (1) the anti-pattern label, (2) PASS/FAIL exhibit. Then build findings table.

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root |
|-----------|-----------------|----------------|-----------------|----------------|
| F-01 | | | S-XX | |

Null case (Rule 3): `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A |`

After findings, return to Step 3b and update `yes` rows to `yes — F-NN`.

---

### Step 5 — Role: Coverage Auditor

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

Stop. Write verbatim before building:

> "Proposals schema committed: Proposal ID ★, Type ★ [Rule 1], Change ★, Delta Finding ★
> [Rule 4], Evidence ★, If unchanged ★, Reversibility ★ [Rule 1], Urgency ★ [Rule 5:
> U-1 to U-5; prose not valid], Confidence ★. All three types present. Empty types use
> Rule 3 null rows."

Before assigning `Urgency`: apply Rule 5 scale. U-4/U-5 must have Reversibility (2) or (3).

| Proposal ID | Type [Rule 1] | Change | Delta Finding [Rule 4] | Evidence | If unchanged | Reversibility [Rule 1] | Urgency [Rule 5] | Confidence |
|------------|--------------|--------|----------------------|----------|-------------|----------------------|-----------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [degradation] | (2) | U-3 | High |

Null rows (Rule 3):

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | U-0 | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | U-0 | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | U-0 | — |

---

### Step 7b — Role: Status Quo Defender

For each active proposal (non-null rows from Step 7), articulate the strongest case for
leaving strategy.md unchanged. Name the specific cost of changing. Then the Proposal
Architect responds. Rule 1 applies to `Defender verdict`.

After filling the table:
- `Withdrawn` proposals: mark "[WITHDRAWN after Defender step]" in Step 7. Exclude from diff.
- `Strengthened` proposals: update `If unchanged` in Step 7 with the sharpened case.
- `Unchanged` proposals: proceed as-is.

| Proposal ID | Strongest case for no change | Specific cost of changing | Proposal Architect response | Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |
|------------|------------------------------|--------------------------|----------------------------|----------------------------------------------------------------|
| ADD-1 | | | | Unchanged |

Null case (Rule 3): `| — | No active proposals — Defender step not applicable | N/A | N/A | N/A |`

---

### Step 8 — Role: Diff Author

Stop. Write verbatim:

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★
> (inline [file.md — ≤10 words] per row), Proposal ★ (ID from Step 7). No column
> omitted. Withdrawn proposals excluded."

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

## V-05 — Full Ceiling (V-01 + V-02 + V-03 + Expanded CONTRACT)

**Axes**: All R13 axes combined (Status Quo Defender, urgency scoring scale, prediction-first
role sequence) plus the expanded CONTRACT rationale from R12 V-02.

**Hypothesis**: Each axis contributes a distinct mechanism:
- Prediction-first (V-03): makes delta identification falsifiable via pre-commitment;
  surprise findings surface genuine blindspots rather than reverse-engineered ones.
- Inertia framing (V-01): forces explicit justification of change over status quo;
  only proposals that survive counter-argument proceed.
- Scoring scale (V-02): forces urgency discrimination distinct from confidence; U-4/U-5
  proposals must have matching Reversibility.
- Expanded CONTRACT with per-rule rationale (R12 V-02): front-loads binding constraints
  with explanatory context; model has full rule intent before any step.

The full ceiling tests whether all four mechanisms compose without interference. The
prediction step is extended to include urgency predictions: "I predict delta F-01 at
urgency U-4." The Defender step applies to post-urgency proposals only, ensuring urgency
calibration happens before counter-argument pressure.

---

You are executing `topic:plan` for the topic `{topic}`.

Your task: revise `simulations/{topic}/strategy.md` based on signals gathered since it
was written. Before reading anything, commit to specific predicted delta findings and
their urgency levels. Extract assumptions, read signals, identify deltas (marking each
as predicted or surprise), check conflicts, build proposals with urgency scores, challenge
each proposal with the Status Quo Defender, then wait for YES before writing.
Do not auto-apply changes.

---

### COLUMN CONTRACT (binding before reading any file)

Five rules govern every table you produce. Read all five before starting.

**Rule 1 — Enumerated columns**

Any column using a closed value set must declare those values at every point where the
column is named. Select from the declared set only; prose is not a valid value. A cell
that contains paraphrase, conditional prose, or multi-value selection is treated as
empty regardless of content.

*Why this matters*: Typed columns are falsifiable; prose columns are not. An ADD-type
proposal and a REPRIORITIZE-type proposal are structurally different change requests.
Mixing types in prose removes that distinction and makes the proposals table non-auditable.
The same principle applies to urgency: "high-ish" is not a decision — U-4 is.

Rule 1 PASS:
- `Type`: `ADD` | `REMOVE` | `REPRIORITIZE`
- `Reversibility`: `(1) Reversible at same cost` | `(2) Gets harder` | `(3) Becomes impossible`
- `Delta candidate?`: `yes` | `no` | `yes — F-01`
- `Consistent with strategy?`: `Yes` | `No` | `Partial`
- `Prediction match`: `Predicted — P-NN` | `Surprise`
- `Defender verdict`: `Withdrawn` | `Strengthened` | `Unchanged`

Rule 1 FAIL (treated as absent):
- `Type`: "add a skill" | "addition" | "add/remove"
- `Prediction match`: "mostly predicted" | "close to P-01" | "partially predicted"
- `Defender verdict`: "conditionally kept" | "partially withdrawn"

**Rule 2 — Column independence**

Before filling any cell, apply this test: *"Can I fill this cell without reading the
source document?"* If yes, the cell is a structural alias and is treated as empty.
Applies especially to `Implicit evidence`.

*Why this matters*: The `Implicit evidence` column makes assumptions auditable. If a
reviewer cannot trace evidence back to a phrase in strategy.md, the column is decorative.
A column that can be filled without reading the document is navigational metadata, not
analysis.

Rule 2 PASS (requires reading strategy.md):
- `"teams run scout before draft"` — specific phrase from rationale block
- `"signal count threshold never defined"` — gap detected as absent in text
- `"the phrase 'gather evidence first'"` — verbatim instruction

Rule 2 FAIL (treated as absent):
- `A-01` — row key
- `"signals gather evidence"` — restatement in different words
- `"see rationale section"` — pointer with no content
- `"strategy implies sequencing"` — generic inference not traceable to any phrase

**Rule 3 — Null completeness**

Every mandatory null case must appear in the output. A section that runs and finds
nothing is proven by its null row. A missing section is indistinguishable from a
section that was skipped entirely. Every null template in this skill cites Rule 3.

*Why this matters*: Auditable absence requires an explicit declaration. A missing null
row tells a reviewer nothing about whether the section ran.

Rule 3 PASS:
- `| CF-00 | — | — | No conflicts detected — audit ran | No action needed |` (Rule 3)
- `| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | U-0 | — |` (Rule 3)
- `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A | Surprise |` (Rule 3)
- `| P-00 | No predictions committed | N/A | N/A | N/A |` (Rule 3)
- `| — | No active proposals — Defender step not applicable | N/A | N/A | N/A |` (Rule 3)

Rule 3 FAIL: missing null rows; missing change type rows without null rows.

**Rule 4 — Two-level traceability**

Every proposal must chain from proposal to delta finding to source signal. The `Delta
Finding` column must include the full "Strategy assumed [X] / Signal revealed [Y]" text
with the exact finding ID — not just the ID.

*Why this matters*: The proposals table should be self-contained. A reviewer who reads
only the proposals table must understand why each change is proposed without returning
to the delta section.

Rule 4 PASS: `F-01: Strategy assumed scout runs before draft / Signal revealed draft completed without scout artifacts`
Rule 4 FAIL: `F-01` | `"S-01 suggests adding a skill"`

**Rule 5 — Scoring scales**

Two scales apply to specific columns. Select from defined levels only.

*Urgency scale* — `Urgency` column in Proposals and `Predicted urgency` in Predictions:

| Level | Meaning |
|-------|---------|
| U-1 | Cosmetic — deferring has no compounding cost |
| U-2 | Low — strategy still works, gaps grow slowly |
| U-3 | Medium — a cohort of signals will be misclassified until addressed |
| U-4 | High — each sprint without this change actively misdirects signal gathering |
| U-5 | Critical — strategy is structurally incorrect; continued use causes harm |

Calibration constraint: U-4/U-5 proposals must have Reversibility (2) or (3). Mismatches
must be resolved before proceeding.

*Signal quality scale* — `Signal quality` column in Signal Inventory:

| Level | Meaning |
|-------|---------|
| H | High — complete, dated, namespace+skill-tagged, finding specific |
| M | Medium — partial, undated, or finding generic |
| L | Low — stub, draft, or finding not extractable |

Rule 5 FAIL: `"high-ish"` | `"urgent"` | `"HM"` | `3.5` | `"medium to high"`

---

### Output Schema (read before proceeding to Step 1)

Every table must conform to this schema. ★ columns are mandatory. All five Contract Rules
apply. Do not omit any ★ column.

**Assumption Table** (5 columns — all independently populated per Rule 2)
| ★ Assumption | ★ Implicit evidence [Rule 2 — PASS: phrase from strategy.md | FAIL: row key / restatement / pointer] | ★ Contradicted by a signal? | ★ Why this matters for delta detection | ★ Delta candidate? [Rule 1: yes / no / yes — F-NN] |

**Prediction Table** (committed before signal reading — Rule 5 applies to Predicted urgency)
| ★ Prediction ID | ★ Assumption source (A-NN / "stated field") | ★ Predicted: Strategy assumed [X] | ★ Predicted: Signal will reveal [Y] | ★ Predicted urgency [Rule 5: U-1/U-2/U-3/U-4/U-5] | ★ Confidence before reading |

**Signal Inventory** (Rule 5: Signal quality)
| ★ ID | ★ File | ★ Namespace | ★ Skill | ★ Date | ★ Key Finding | ★ Consistent with strategy? [Rule 1: Yes / No / Partial] | ★ Assumption link | ★ Signal quality [Rule 5: H / M / L] |

**Delta Findings** (Rule 1: Prediction match)
| ★ Finding ID | ★ Strategy assumed | ★ Signal revealed | ★ Source signal(s) | ★ Assumption root | ★ Prediction match [Rule 1: Predicted — P-NN / Surprise] |

**Prediction Accuracy Audit** (Step 4b)
| ★ Prediction ID | ★ Predicted delta | ★ Actual finding (F-NN / "No match") | ★ Urgency: predicted vs actual | ★ Verdict | ★ Implication |

**Namespace Audit**
| ★ Namespace | ★ Signal Count | ★ Stage-Relative Status | ★ Action Needed? |

**Conflict Audit**
| ★ Conflict ID | ★ Signal A | ★ Signal B | ★ Description | ★ Implication for strategy |

**Proposals** (Rules 1, 4, 5 apply)
| ★ Proposal ID | ★ Type [Rule 1: ADD / REMOVE / REPRIORITIZE] | ★ Change | ★ Delta Finding [Rule 4: full "Strategy assumed X / Signal revealed Y" + ID] | ★ Evidence | ★ If unchanged | ★ Reversibility [Rule 1: (1)/(2)/(3)] | ★ Urgency [Rule 5: U-1/U-2/U-3/U-4/U-5] | ★ Confidence |

**Defender Challenge Table** (Step 7b — Rule 1: Defender verdict)
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

Extract what strategy.md assumed without writing. Scan: (a) audience knowledge,
(b) namespace priority ordering, (c) signal sufficiency, (d) timeline, (e) definition of done.

Apply Rule 2 PASS/FAIL before each `Implicit evidence` cell.
`Contradicted?` = `[pending]`. `Delta candidate?` = Rule 1. Update to `yes — F-NN`
after Step 4.

| Assumption | Implicit evidence [Rule 2] | Contradicted? | Why this matters | Delta candidate? [Rule 1] |
|-----------|---------------------------|--------------|-----------------|--------------------------|
| [most important] | [phrase from strategy.md] | [pending] | [failure mode] | yes |

Null case (Rule 3): `| No unstated assumptions found after systematic scan | N/A | N/A | N/A | no |`

---

### Step 2b — Role: Delta Predictor

You have not yet read any signal files. Based only on Step 1 (stated fields) and
Step 2 (extracted assumptions), commit to specific predicted delta findings with urgency.

Valid prediction form:
`Predicted: Strategy assumed [X from Step 1 or A-NN] / Signal will reveal [Y]`

Apply Rule 2 test to each prediction: could you write it without reading strategy.md? If
yes, sharpen until the answer is no.

Also predict urgency using the Rule 5 scale — what level of urgency do you expect if
this finding is confirmed?

PASS: tied to specific strategy content + specific contradiction + urgency level
FAIL: generic ("some signals may contradict") | not tied to any stated field or assumption

| Prediction ID | Assumption source | Predicted: Strategy assumed [X] | Predicted: Signal will reveal [Y] | Predicted urgency [Rule 5] | Confidence before reading |
|--------------|------------------|---------------------------------|-----------------------------------|-----------------------------|--------------------------|
| P-01 | A-NN | | | U-3 | Med |

Null case (Rule 3): `| P-00 | No predictions committed — assumptions insufficient | N/A | N/A | N/A | N/A |`

Do not read any signal files until this table is complete.

---

### Step 3a — Role: Signal Analyst (Read)

Predictions are committed. Now read signals.

Glob `simulations/{topic}/` recursively. Read every file.

Null case (Rule 3): `> No signals found — strategy.md does not need revision at this time.`

Rules 1 and 5 apply.

| ID | File | Namespace | Skill | Date | Key Finding | Consistent with strategy? [Rule 1] | Assumption link | Signal quality [Rule 5] |
|----|------|-----------|-------|------|-------------|-----------------------------------|----------------|------------------------|
| S-01 | | | | | | | | |

---

### Step 3b — Role: Assumption Archaeologist (Back-fill)

Replace each `[pending]`: `Contradicted — S-NN` | `Supported — S-NN` | `No signal coverage`

Reproduce full updated assumption table. After Step 4, update `yes` rows to `yes — F-NN`.

---

### Step 4 — Role: Delta Identifier

Write: (1) the anti-pattern label, (2) a PASS/FAIL exhibit. Then fill findings.

For each finding, check Step 2b predictions. Mark `Predicted — P-NN` or `Surprise`.
Rule 1 applies to `Prediction match`.

| Finding ID | Strategy assumed | Signal revealed | Source signal(s) | Assumption root | Prediction match [Rule 1: Predicted — P-NN / Surprise] |
|-----------|-----------------|----------------|-----------------|----------------|--------------------------------------------------------|
| F-01 | | | S-XX | | Predicted — P-01 |

Null case (Rule 3): `| F-00 | Strategy confirmed | No gaps detected | All signals | N/A | Surprise |`

After findings, return to Step 3b and update `yes` rows to `yes — F-NN`.

---

### Step 4b — Role: Prediction Accuracy Auditor

For each prediction from Step 2b, find the matching delta finding. Compare predicted
urgency vs actual urgency assigned at Step 7 (if available, annotate after Step 7).
Write one sentence: what prediction accuracy implies about assumption extraction quality.

| Prediction ID | Predicted delta | Actual finding (F-NN / "No match") | Urgency: predicted vs actual | Verdict | Implication |
|--------------|-----------------|--------------------------------------|------------------------------|---------|-------------|
| P-01 | | F-01 | U-3 vs U-4 | Confirmed, underestimated urgency | [what this reveals] |

Null case (Rule 3): `| P-00 | No predictions to audit | N/A | N/A | N/A | N/A |`

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

Stop. Write verbatim before building:

> "Proposals schema committed: Proposal ID ★, Type ★ [Rule 1: ADD / REMOVE / REPRIORITIZE],
> Change ★, Delta Finding ★ [Rule 4], Evidence ★, If unchanged ★, Reversibility ★ [Rule 1:
> (1)/(2)/(3)], Urgency ★ [Rule 5: U-1 to U-5; prose not valid], Confidence ★. All three
> types present. Empty types use Rule 3 null rows. U-4/U-5 must have Reversibility (2) or (3)."

Before assigning `Urgency`: apply Rule 5 scale. Resolve any Reversibility/Urgency mismatches
before proceeding to Step 7b.

After completing this table, return to Step 4b to add `Urgency: predicted vs actual` values.

| Proposal ID | Type [Rule 1] | Change | Delta Finding [Rule 4] | Evidence | If unchanged | Reversibility [Rule 1] | Urgency [Rule 5] | Confidence |
|------------|--------------|--------|----------------------|----------|-------------|----------------------|-----------------|------------|
| ADD-1 | ADD | | F-01: Strategy assumed ... / Signal revealed ... | | [degradation] | (2) | U-3 | High |

Null rows (Rule 3):

| ADD-0 | ADD | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | U-0 | — |
| REMOVE-0 | REMOVE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | U-0 | — |
| REPRIORITIZE-0 | REPRIORITIZE | None proposed | Delta Finding: N/A | — | If unchanged: N/A | N/A | U-0 | — |

---

### Step 7b — Role: Status Quo Defender

For each active proposal, articulate the strongest case for leaving strategy.md unchanged.
Name the specific cost of this change. Proposal Architect responds. Rule 1 applies to
`Defender verdict`.

After filling:
- `Withdrawn`: mark "[WITHDRAWN after Defender step]" in Step 7. Exclude from diff.
- `Strengthened`: update `If unchanged` in Step 7.
- `Unchanged`: proceed as-is.

| Proposal ID | Strongest case for no change | Specific cost of changing | Proposal Architect response | Defender verdict [Rule 1: Withdrawn / Strengthened / Unchanged] |
|------------|------------------------------|--------------------------|----------------------------|----------------------------------------------------------------|
| ADD-1 | | | | Unchanged |

Null case (Rule 3): `| — | No active proposals — Defender step not applicable | N/A | N/A | N/A |`

---

### Step 8 — Role: Diff Author

Stop. Write verbatim:

> "Diff schema committed: Namespace ★, Skill/Area ★, Before ★, After ★, Evidence ★
> (inline [file.md — ≤10 words] per row), Proposal ★ (ID from Step 7). No column
> omitted. Withdrawn proposals excluded."

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
