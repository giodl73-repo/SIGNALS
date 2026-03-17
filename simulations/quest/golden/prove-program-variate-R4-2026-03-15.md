---
skill: quest-variate
skill_target: prove-program
date: 2026-03-15
round: 4
rubric: prove-program-rubric-v4-2026-03-15.md
status: DRAFT
---

# prove-program — Variations R4 (V-01 through V-05)

**New criteria in v4 rubric**: C-17 (verbatim feed-forward quotation), C-18 (inter-phase GATE enforcement), C-19 (per-criterion FAIL conditions inline)
**Baseline**: R3 V-05 scored 130/130 on all prior criteria — R4 variations build on that floor and target the 15-point gap (C-17 + C-18 + C-19 = 5 pts each)
**Single-axis**: V-01 (C-17 verbatim quotation), V-02 (C-18 gate enforcement), V-03 (C-19 inline FAIL conditions)
**Combined**: V-04 (C-17 + C-18), V-05 (C-17 + C-18 + C-19 over full R3 V-05 role-sequence baseline)

---

## V-01 — Output Format axis (C-17 Verbatim Quotation)

**Variation axis:** Output format — verbatim blockquote extraction in every experiment Input section
**Hypothesis:** Mandating `> [exact text]` blockquote format in every experiment Input section — with a precise FAIL condition prohibiting paraphrase and pointer references — eliminates interpretive drift across the feed-forward chain and produces C-17 compliance on every artifact without relying on advisory phrasing.

---

You are running a research program for: **{{topic}}**

Research question: {{research_question}}

Complete all phases in order. Do not advance past a gate until its condition is fully met.

---

### Phase 0 — Inertia Gap Declaration

The inertia competitor is **prove-topic**: a single-topic sequential prove campaign (intelligence → analysis → interview → synthesis) scoped to one Signal topic. Use prove-program only when the research question exceeds that capability.

Inertia gap: [one sentence — what prove-topic cannot handle here: cross-namespace scope, external domain, multi-hypothesis structure, or custom experiment type]

GATE-0: Inertia gap required before Phase 1. If prove-topic is sufficient for this question, stop and use it.

---

### Phase 1 — Hypothesis

State the specific belief you are testing. Must precede all experiments.

Hypothesis: [what you believe is true — one sentence, positive form]
Falsification: [what specific evidence would cause you to reject this hypothesis]

GATE-A: Hypothesis must differ from the research question in specificity or framing, and falsification criterion must be present. Do not proceed to Phase 1B until both conditions are met.

---

### Phase 1B — Experiment Plan

Produce this table before executing any experiment.

| # | Type | Question answered | Rationale | Output label | Consumed by | Closes gap? |
|---|------|------------------|-----------|--------------|-------------|-------------|
| E-01 | [websearch / intelligence / analysis / interview / prototype / custom] | [question] | [why this type, not another] | [label] | [E-02 / Phase 3] | Yes / No |
| E-02 | [type] | [question] | [rationale] | [label] | [Phase 3] | Yes / No |

Rules:
- Select >=2 distinct types — no two rows may share the same type
- At least one row: Closes gap? = Yes — the experiment that addresses the Phase 0 inertia gap
- Output labels in this table lock the verbatim-quotation contract for Phase 2

GATE-B: Table requires >=2 distinct types, >=1 Yes in Closes gap?, all Output label cells filled. Revise until all conditions met before Phase 2.

---

### Phase 2 — Experiment Execution

**Verbatim input format — required for every block in this phase:**

Each experiment block MUST reproduce the exact text of the upstream output it consumes using blockquote format:

> [exact text — directly quoted from the prior block, not paraphrased, summarized, or pointed to]

FAIL: Input section uses "see above", "per E-01", "as found in E-01", "based on E-01's finding that...", or any paraphrase or pointer reference instead of directly quoted text. Rephrase is not verbatim. Rewrite the Input section before executing if this condition triggers.

---

#### E-01 — [Type from Phase 1B]

Input (verbatim):
> Hypothesis: [verbatim hypothesis text from Phase 1] | Inertia gap: [verbatim gap text from Phase 0]

[One sentence: how the hypothesis focuses this experiment's scope.]

[Execute experiment.]

E-01 output: [labeled finding — this exact text is the verbatim source for E-02's Input section]

Contract delivery: output label = "[label from Phase 1B]" — consumed by: [E-02 / Phase 3] — delivered? Yes / No

---

#### E-02 — [Type from Phase 1B]

Input (verbatim):
> [exact text from E-01 output — quote the labeled finding directly, not a description of it]

[One sentence: how E-01's finding constrains or refocuses this experiment's scope.]

[Execute experiment.]

E-02 output: [labeled finding]

Contract delivery: output label = "[label from Phase 1B]" — consumed by: [Phase 3] — delivered? Yes / No

---

[Add E-03+ as needed. Every block MUST have a verbatim blockquote Input and a Contract delivery line.]

GATE-C: All planned experiments complete. Every block has a verbatim blockquote Input and a Contract delivery line with a delivered? Yes/No.

---

### Phase 3A — Feed-Forward Audit

| Experiment | Plan output label | Delivered? | Consumed by |
|-----------|------------------|------------|-------------|
| E-01 | [label] | Yes / No | [step] |
| E-02 | [label] | Yes / No | [step] |

Populate from Phase 2 Contract delivery lines. Do not infer values not stated in the experiment blocks.

---

### Phase 3B — Findings

| # | Finding | Source | Confidence | Evidence basis |
|---|---------|--------|------------|---------------|
| F-01 | [finding text] | E-01 | high / medium / low | [e.g., "2 independent sources", "single source not replicated"] |
| F-02 | [finding text] | E-02 | high / medium / low | [basis] |

Minimum 2 findings. Confidence levels must not all be identical. Evidence basis required per row.

---

### Phase 3C — Synthesis

What we thought: [hypothesis verbatim from Phase 1]
What we actually learned: [confirm, refine, or refute — must differ from hypothesis text. Answer the research question.]

Inertia gap closure: [Did the experiment marked Closes gap? = Yes produce a finding that prove-topic could not have produced? Yes / No + one sentence of evidence.]

Cross-namespace note: [Name any downstream Signal artifact that should receive these findings — draft spec, scout brief, topic plan, topic story.]

GATE-D: "What we actually learned" must differ from the hypothesis. If it copies the hypothesis verbatim, revise before writing principles.

---

### Phase 3D — Principles

| Label | Principle | Source finding |
|-------|-----------|---------------|
| P-01 | [When X, do Y — or Always Z] | F-NN |
| P-02 | [When X, do Y — or Always Z] | F-NN |

Minimum 2 principles. Generic truisms do not pass. Source finding required per row.

---

### Artifact

Write: `simulations/prove/research/{{topic}}-research-{{date}}.md`

Frontmatter: `skill: prove-program | topic: {{topic}} | date: {{date}} | hypothesis: [one line] | inertia_gap: [one line] | experiment_types: [list] | findings_count: [N] | principles_count: [N] | inertia_gap_closed: true / false`

---

---

## V-02 — Lifecycle Emphasis axis (C-18 Gate Enforcement)

**Variation axis:** Lifecycle emphasis — dense named GATE tokens at every phase boundary, each with a pass condition and a STOP instruction
**Hypothesis:** Placing named GATE-α through GATE-ζ tokens at every major phase boundary — each gate blocking forward progress with a specific unmet-condition STOP instruction — converts the research lifecycle from advisory to enforcing and achieves C-18 compliance regardless of model capability variance.

---

You are running a research program for: **{{topic}}**

Research question: {{research_question}}

This document uses a named gate system. Every major phase boundary carries a GATE checkpoint with a pass condition and a STOP instruction. Do not advance past any gate until its pass condition is fully satisfied.

---

### GATE-α — Inertia Check

The inertia competitor is **prove-topic**: single-topic intelligence → analysis → interview → synthesis. Prove-program is warranted only when the research question exceeds prove-topic's capability.

Inertia gap: [what prove-topic cannot handle here]

**GATE-α PASS condition**: Inertia gap names a specific capability prove-topic lacks for this question — not a generic preference.
**GATE-α STOP**: If prove-topic is sufficient, stop and use it instead.

---

### Phase 1 — Hypothesis

Hypothesis: [what you believe is true — one sentence, positive form]
Falsification: [what evidence would refute this]

**GATE-β PASS condition**: (a) Hypothesis is in positive form; (b) differs from the research question in specificity or framing; (c) falsification criterion is stated.
**GATE-β STOP**: If any condition is unmet, rewrite the hypothesis before Phase 1B begins. Do not proceed.

---

### Phase 1B — Experiment Plan

Produce this table before any experiment executes.

| # | Type | Question answered | Rationale | Output label | Consumed by | Closes gap? |
|---|------|------------------|-----------|--------------|-------------|-------------|
| E-01 | [type] | [question] | [why this type] | [label] | [E-02 / Phase 3] | Yes / No |
| E-02 | [type] | [question] | [rationale] | [label] | [Phase 3] | Yes / No |

Types: websearch, intelligence, analysis, interview, prototype, custom.

**GATE-γ PASS condition**: (a) >=2 distinct types by name; (b) >=1 row has Closes gap? = Yes; (c) all Output label cells are filled; (d) no experiment has been executed yet.
**GATE-γ STOP**: Revise the table until all four conditions are met. Do not execute any experiment until GATE-γ passes.

---

### Phase 2 — Experiment Execution

**[Confirm GATE-γ PASS before executing E-01]**

Each experiment block must include: (1) an Input section citing prior content specifically, (2) execution, (3) a labeled E-NN output, and (4) a Contract delivery line.

---

#### E-01 — [Type]

Input from prior: Phase 1 hypothesis + Phase 0 inertia gap — [state the specific content of each that scopes this experiment]
[Execute.]
E-01 output: [labeled finding]
Contract delivery: output label = "[plan label]" — consumed by: [E-02 / Phase 3] — delivered? Yes / No

**GATE-δ1 PASS condition**: E-01 output is labeled and Contract delivery line is present with a delivered? boolean.
**GATE-δ1 STOP**: Do not begin E-02 until GATE-δ1 passes.

---

#### E-02 — [Type]

**[Confirm GATE-δ1 PASS before executing E-02]**

Input from prior: E-01 output — [cite the specific finding content from E-01, not a pointer such as "see above" or "per E-01"]
[One sentence: how E-01's finding changes what you're looking for in this experiment.]
[Execute.]
E-02 output: [labeled finding]
Contract delivery: output label = "[plan label]" — consumed by: [Phase 3] — delivered? Yes / No

**GATE-δ2 PASS condition**: E-02 output labeled and Contract delivery present.
**GATE-δ2 STOP**: Do not proceed to Phase 3 until all planned experiments have a GATE-δN PASS.

---

[Add E-03+ following the same GATE-δN pattern. Each block requires a preceding confirmation of the prior GATE-δN, and a new GATE-δN PASS condition after execution.]

---

### Phase 3A — Feed-Forward Audit

**[Confirm all GATE-δN PASS before Phase 3]**

| Experiment | Plan output label | Delivered? | Consumed by |
|-----------|------------------|------------|-------------|
| E-01 | [label] | Yes / No | [step] |
| E-02 | [label] | Yes / No | [step] |

Populate directly from Contract delivery lines in Phase 2. Do not invent values.

---

### Phase 3B — Findings

| # | Finding | Source | Confidence | Evidence basis |
|---|---------|--------|------------|---------------|
| F-01 | [finding] | E-01 | high / medium / low | [basis] |
| F-02 | [finding] | E-02 | high / medium / low | [basis] |

**GATE-ε PASS condition**: >=2 findings, confidence annotations present and not all identical, evidence basis per row.
**GATE-ε STOP**: Add findings until all conditions are met. Do not write synthesis until GATE-ε passes.

---

### Phase 3C — Synthesis

**[Confirm GATE-ε PASS before synthesis]**

What we thought: [hypothesis verbatim from Phase 1]
What we actually learned: [confirm, refine, or refute — must differ from hypothesis text. Answer the research question.]

Inertia gap closure: [Did the Closes gap? experiment produce a finding prove-topic could not? Yes / No + one sentence.]

Cross-namespace note: [Name downstream Signal artifact that should receive these findings.]

**GATE-ζ PASS condition**: Both synthesis fields present; "what we actually learned" is not a verbatim copy of the hypothesis.
**GATE-ζ STOP**: Revise before writing principles.

---

### Phase 3D — Principles

**[Confirm GATE-ζ PASS before principles]**

P-01: [When X, do Y — or Always Z] — Source: F-NN
P-02: [When X, do Y — or Always Z] — Source: F-NN

Minimum 2 principles. No generic truisms.

---

### Artifact

Write: `simulations/prove/research/{{topic}}-research-{{date}}.md`

Frontmatter: `skill: prove-program | topic: {{topic}} | date: {{date}} | hypothesis: [one line] | inertia_gap: [one line] | experiment_types: [list] | findings_count: [N] | principles_count: [N] | inertia_gap_closed: true / false`

---

---

## V-03 — Phrasing Register axis (C-19 Inline FAIL Conditions)

**Variation axis:** Phrasing register — every enforced criterion is immediately followed by an inline FAIL condition naming the specific failure mode
**Hypothesis:** Pairing each enforced criterion with an inline FAIL condition (precise failure mode, embedded immediately at the enforcement point) produces self-correcting behavior at generation time, satisfies C-19, and fixes the C-11 audit-ledger loss seen in R3 V-03 by keeping the ledger as a distinct section alongside the FAIL gates.

---

You are running a research program for: **{{topic}}**

Research question: {{research_question}}

Every requirement in this document includes an inline FAIL condition. Check each FAIL condition before moving to the next section — do not proceed if the FAIL condition is triggered.

---

### 1. Inertia Gap

The inertia competitor is **prove-topic**: single-topic intelligence → analysis → interview → synthesis on one Signal topic. State why this question requires prove-program.

Inertia gap: [what prove-topic cannot handle here — cross-namespace scope, external domain, multi-hypothesis structure, or custom experiment type]

FAIL: Gap statement is generic ("I need more flexibility" or similar) rather than naming the specific capability prove-topic lacks for this research question.

---

### 2. Hypothesis

State a specific, testable belief. Must appear before any experiment is named or planned.

Hypothesis: [what you believe is true — one sentence, positive form]
Falsification: [what evidence would refute this hypothesis]

FAIL: Hypothesis is absent, is a restatement of the research question, or falsification criterion is missing.

---

### 3. Experiment Plan

Produce this table before any experiment executes.

| # | Type | Question answered | Rationale | Output label | Consumed by | Closes gap? |
|---|------|------------------|-----------|--------------|-------------|-------------|
| E-01 | [websearch / intelligence / analysis / interview / prototype / custom] | [question] | [why this type, not another] | [label] | [E-02 / Section 5] | Yes / No |
| E-02 | [type] | [question] | [rationale] | [label] | [Section 5] | Yes / No |

FAIL: Plan has fewer than 2 rows, all rows use the same type, no row has Closes gap? = Yes, or any Output label cell is blank.

---

### 4. Experiment Execution

Execute experiments in plan order.

Each block must include:
- **Input**: cite the specific prior output you're reading and its content — not a pointer
- **Execution**: run the experiment; use hypothesis and prior output to focus scope
- **Output**: label the finding as E-NN output: [finding]
- **Contract delivery**: `Contract delivery: output label = "[plan label]" — consumed by: [step] — delivered? Yes / No`

FAIL (applies to every block): Block lacks an explicit Input citation naming the prior content, or Contract delivery line is absent, or the output label in Contract delivery does not match the Section 3 plan.

---

#### E-01 — [Type]

Input: Phase 2 hypothesis — "[verbatim hypothesis text]" + Phase 0 inertia gap — "[verbatim gap text]"
[Execute.]
E-01 output: [labeled finding]
Contract delivery: output label = "[plan label]" — consumed by: [E-02 / Section 5] — delivered? Yes

FAIL: E-01 output is unlabeled, or Contract delivery is absent.

---

#### E-02 — [Type]

Input: E-01 output — [cite the specific content of E-01's labeled finding; "see above" or "per E-01" do not satisfy this requirement]
[One sentence: how E-01's finding changes the scope or focus of this experiment.]
[Execute.]
E-02 output: [labeled finding]
Contract delivery: output label = "[plan label]" — consumed by: [Section 5] — delivered? Yes

FAIL: Input section uses a pointer reference without citing content, or Contract delivery is absent.

---

[Add E-03+ as needed. Repeat FAIL conditions per block.]

---

### 5. Feed-Forward Audit Ledger

| Experiment | Plan output label | Delivered? | Consumed by |
|-----------|------------------|------------|-------------|
| E-01 | [label] | Yes / No | [step] |
| E-02 | [label] | Yes / No | [step] |

FAIL: Ledger is absent, or any row's Delivered? value contradicts the Contract delivery line in the corresponding experiment block.

---

### 6. Findings

| # | Finding | Source | Confidence | Evidence basis |
|---|---------|--------|------------|---------------|
| F-01 | [finding text] | E-01 | high / medium / low | [e.g., "2 independent sources", "single source not replicated"] |
| F-02 | [finding text] | E-02 | high / medium / low | [basis] |

FAIL: Fewer than 2 findings, all confidence levels are identical, or evidence basis is absent from any row.

---

### 7. Synthesis

What we thought: [hypothesis verbatim from Section 2]
What we actually learned: [confirm, refine, or refute — must differ from hypothesis text. Answer the research question.]

Inertia gap closure: [Did the Closes gap? experiment produce a finding prove-topic could not have produced? Yes / No + one sentence of evidence.]

Cross-namespace note: [Name any downstream Signal artifact that should receive these findings — draft spec, scout brief, topic plan, topic story.]

FAIL: "What we actually learned" copies the hypothesis verbatim, or either synthesis field is absent.
FAIL: Inertia gap closure verdict is absent or states neither Yes nor No.

---

### 8. Principles

P-01: [When X, do Y — or Always Z] — Source: F-NN
P-02: [When X, do Y — or Always Z] — Source: F-NN

FAIL: Fewer than 2 principles, or any principle is a generic truism without a specific source finding citation.

---

### Artifact

Write: `simulations/prove/research/{{topic}}-research-{{date}}.md`

Frontmatter: `skill: prove-program | topic: {{topic}} | date: {{date}} | hypothesis: [one line] | inertia_gap: [one line] | experiment_types: [list] | findings_count: [N] | principles_count: [N] | inertia_gap_closed: true / false`

---

---

## V-04 — Combined: Output Format + Lifecycle (C-17 + C-18)

**Variation axes:** Verbatim quotation + gate enforcement
**Hypothesis:** Combining mandatory blockquote verbatim extraction (C-17) with named GATE tokens at every phase boundary (C-18) creates mutually reinforcing enforcement — gates prevent experiment blocks from executing without a verbatim Input, and the verbatim Input provides concrete traceability for the feed-forward audit — together achieving both new R4 criteria without adding FAIL conditions.

---

You are running a research program for: **{{topic}}**

Research question: {{research_question}}

Two enforcement mechanisms operate simultaneously:

1. **Named GATE tokens** — every major phase boundary carries a named GATE with a pass condition and a STOP instruction. Do not advance past a gate until its condition is fully met.
2. **Verbatim input quotation** — every experiment block MUST reproduce the exact text of the upstream output it consumes using blockquote notation (`> [exact text]`). Paraphrase and pointer references are prohibited.

---

### GATE-0 — Inertia Check

The inertia competitor is **prove-topic**: single-topic intelligence → analysis → interview → synthesis. State why this question requires prove-program.

Inertia gap: [what prove-topic cannot handle here]

**GATE-0 PASS**: Inertia gap names a specific prove-topic limitation for this question.
**GATE-0 STOP**: If prove-topic is sufficient, stop and use it.

---

### Phase 1 — Hypothesis

Hypothesis: [what you believe is true — one sentence, positive form]
Falsification: [what would refute this]

**GATE-H PASS**: Hypothesis (a) is in positive form, (b) differs from the research question, (c) has a falsification criterion.
**GATE-H STOP**: Rewrite until all three conditions are met. Do not produce the experiment plan until GATE-H passes.

---

### Phase 1B — Experiment Plan

| # | Type | Question answered | Rationale | Output label | Consumed by | Closes gap? |
|---|------|------------------|-----------|--------------|-------------|-------------|
| E-01 | [type] | [question] | [why this type] | [label] | [E-02 / Phase 3] | Yes / No |
| E-02 | [type] | [question] | [rationale] | [label] | [Phase 3] | Yes / No |

Types: websearch, intelligence, analysis, interview, prototype, custom.

**GATE-P PASS**: (a) >=2 distinct types; (b) >=1 Yes in Closes gap?; (c) all Output labels filled.
**GATE-P STOP**: Revise until all conditions met. Do not execute any experiment until GATE-P passes.

---

### Phase 2 — Experiment Execution

**[Confirm GATE-P PASS — verbatim input requirement now active for all blocks]**

Each experiment block:
1. **Input (verbatim)** — blockquote the exact text of the upstream output consumed
2. **Execution** — run the experiment
3. **Output** — E-NN output: [labeled finding]
4. **Contract delivery** — `Contract delivery: "[plan label]" — consumed by: [step] — delivered? Yes / No`

The blockquote in the Input section MUST be the actual output content of the prior block. Do not write "see above", "per E-01", or any paraphrase. Use verbatim extracted text.

---

#### E-01 — [Type]

Input (verbatim):
> Hypothesis: [verbatim hypothesis text from Phase 1] | Inertia gap: [verbatim gap text from Phase 0]

[One sentence: how hypothesis + inertia gap scope this experiment.]
[Execute.]
E-01 output: [labeled finding — this exact text is what E-02 must blockquote]
Contract delivery: "[label]" — consumed by: [E-02 / Phase 3] — delivered? Yes

**GATE-E1 PASS**: E-01 output labeled, verbatim blockquote present in Input, Contract delivery present.
**GATE-E1 STOP**: Do not begin E-02 until GATE-E1 passes.

---

#### E-02 — [Type]

**[Confirm GATE-E1 PASS]**

Input (verbatim):
> [exact text from E-01 output — directly quoted, not a description of what E-01 found]

[One sentence: how E-01's finding constrains this experiment's scope.]
[Execute.]
E-02 output: [labeled finding]
Contract delivery: "[label]" — consumed by: [Phase 3] — delivered? Yes

**GATE-E2 PASS**: E-02 output labeled, verbatim blockquote present, Contract delivery present.

---

[Add E-03+ following the same pattern. Each block requires a preceding GATE confirmation, a verbatim blockquote Input, and a Contract delivery line with a GATE-EN PASS at the end.]

**GATE-X PASS** [after all experiments complete]: All outputs labeled, all verbatim blockquotes verified, all Contract delivery lines present.

---

### Phase 3A — Feed-Forward Audit

**[Confirm GATE-X PASS]**

| Experiment | Plan output label | Delivered? | Consumed by |
|-----------|------------------|------------|-------------|
| E-01 | [label] | Yes / No | [step] |
| E-02 | [label] | Yes / No | [step] |

Populate from Contract delivery lines. No new information.

---

### Phase 3B — Findings

| # | Finding | Source | Confidence | Evidence basis |
|---|---------|--------|------------|---------------|
| F-01 | [finding] | E-01 | high / medium / low | [basis] |
| F-02 | [finding] | E-02 | high / medium / low | [basis] |

**GATE-F PASS**: >=2 findings, distinct confidence levels, evidence basis per row.
**GATE-F STOP**: Add or revise findings until all conditions met.

---

### Phase 3C — Synthesis

**[Confirm GATE-F PASS]**

What we thought: [hypothesis verbatim from Phase 1]
What we actually learned: [confirm, refine, or refute — must differ from hypothesis text. Answer the research question.]

Inertia gap closure: [Did the gap-closing experiment produce a finding prove-topic could not? Yes / No + one sentence.]

Cross-namespace note: [Name downstream Signal artifact that should receive these findings.]

**GATE-S PASS**: Both synthesis fields present; learned field is not a verbatim copy of hypothesis.
**GATE-S STOP**: Revise before writing principles.

---

### Phase 3D — Principles

**[Confirm GATE-S PASS]**

P-01: [When X, do Y — or Always Z] — Source: F-NN
P-02: [When X, do Y — or Always Z] — Source: F-NN

Minimum 2 principles. No generic truisms.

---

### Artifact

Write: `simulations/prove/research/{{topic}}-research-{{date}}.md`

Frontmatter: `skill: prove-program | topic: {{topic}} | date: {{date}} | hypothesis: [one line] | inertia_gap: [one line] | experiment_types: [list] | findings_count: [N] | principles_count: [N] | inertia_gap_closed: true / false`

---

---

## V-05 — Combined: Role Sequence + C-17 + C-18 + C-19 (Full R4 Ceiling)

**Variation axes:** Role sequence + verbatim quotation + gate enforcement + inline FAIL conditions
**Hypothesis:** Layering verbatim blockquote quotation (C-17), dense named GATE tokens (C-18), and inline per-criterion FAIL conditions (C-19) over the R3 V-05 role-sequence baseline — which already earned 130/130 on all prior criteria — produces the first 145/145-eligible variation by closing all three R4 aspirational gaps without degrading any essential or recommended criterion.

---

You are running a research program for: **{{topic}}**

Research question: {{research_question}}

Three roles execute in strict sequence. Each role operates within a named GATE system blocking forward progress until pass conditions are met. Every enforced requirement carries an inline FAIL condition. Every experiment block must reproduce upstream outputs in verbatim blockquote format.

---

### Pre-Role — Inertia Gap Declaration

The inertia competitor is **prove-topic**: a single-topic sequential prove campaign (intelligence → analysis → interview → synthesis) scoped to one Signal topic. Prove-program is required only when the research question exceeds prove-topic's capability.

Inertia gap: [what prove-topic cannot handle here — cross-namespace scope, external domain, multi-hypothesis structure, or custom experiment type]

GATE-0: Inertia gap required before any role executes.
FAIL: Gap statement is generic ("I need more flexibility") rather than naming the specific capability prove-topic lacks for this question.
STOP: If prove-topic is sufficient, stop and use it.

---

### Role Declarations

| Role | Writes | May Not |
|------|--------|---------|
| PLANNER | Hypothesis, falsification, experiment plan | Execute experiments, write findings or synthesis |
| EXPERIMENTER | Experiment execution in sequence | Change the plan, write synthesis, introduce new hypotheses |
| SYNTHESIZER | Findings, synthesis, inertia gap closure, principles | Re-run experiments, retroactively change hypothesis |

---

### PLANNER

#### Phase 1 — Hypothesis

State a specific, testable belief. Must appear before any experiment is named.

Hypothesis: [what you believe is true — one sentence, positive form]
Falsification: [what evidence would refute this]

GATE-H: Hypothesis must (a) be in positive form, (b) differ from the research question in specificity, and (c) include a falsification criterion.
FAIL: Hypothesis is absent, is a restatement of the question in different words, or falsification criterion is missing. Rewrite before Phase 1B.

---

#### Phase 1B — Experiment Plan

Produce this table before executing any experiment.

| # | Type | Question answered | Rationale | Output label | Consumed by | Closes gap? |
|---|------|------------------|-----------|--------------|-------------|-------------|
| E-01 | [websearch / intelligence / analysis / interview / prototype / custom] | [question] | [why this type, not another] | [label] | [E-02 / SYNTHESIZER] | Yes / No |
| E-02 | [type] | [question] | [rationale] | [label] | [SYNTHESIZER] | Yes / No |

Rules:
- >=2 distinct types — no two rows may share the same type
- At least one row: Closes gap? = Yes — the experiment that addresses the Phase 0 inertia gap
- Output labels lock the verbatim-quotation contract for EXPERIMENTER blocks

GATE-P: Table requires (a) >=2 distinct types, (b) >=1 Yes in Closes gap?, (c) all Output label cells filled.
FAIL: Table has <2 rows, all rows share the same type, no row is marked Yes in Closes gap?, or any Output label is blank.

**PLANNER COMPLETE**
Hypothesis locked: [verbatim]
Inertia gap addressed by: [E-NN + type]
Plan order: [E-01 type → E-02 type → ...]
→ EXPERIMENTER receives: hypothesis, falsification criterion, ordered plan, verbatim-quotation contract

---

### EXPERIMENTER

GATE-PLANNER: Confirm PLANNER COMPLETE before executing any experiment.
FAIL: Any experiment executes without PLANNER COMPLETE marker confirmed.

**Verbatim input requirement — active for all EXPERIMENTER blocks:**

Every experiment block MUST reproduce the exact text of the upstream output it consumes using blockquote format:

> [exact text — directly quoted from the prior block, not paraphrased, summarized, or pointer-referenced]

FAIL (applies to every block): Input section uses "see above", "per E-01", "as found in E-01", "based on E-01's finding that...", or any form of paraphrase instead of directly quoted text. Rewrite the Input section if this condition triggers.

---

#### E-01 — [Type from Phase 1B]

GATE-E1-entry: PLANNER COMPLETE confirmed. Verbatim input required.

Input (verbatim):
> Hypothesis: [verbatim hypothesis from Phase 1] | Inertia gap: [verbatim gap from Phase 0]

[One sentence: how hypothesis + inertia gap focus this experiment's scope.]

[Execute experiment.]

E-01 output: [labeled finding — this exact text is the verbatim source for E-02's Input section]

Contract delivery: output label = "[plan label]" — consumed by: [E-02 / SYNTHESIZER] — delivered? Yes / No
FAIL: Contract delivery line absent or its output label does not match the Phase 1B plan.

**EXPERIMENT 1 COMPLETE**
Produced: E-01 — [one-line summary]
→ Consumed by: [E-02 / SYNTHESIZER]

---

#### E-02 — [Type from Phase 1B]

GATE-E2-entry: EXPERIMENT 1 COMPLETE confirmed before executing.
FAIL: E-02 begins without EXPERIMENT 1 COMPLETE marker present.

Input (verbatim):
> [exact text from E-01 output — the labeled finding quoted directly, not described or paraphrased]

[One sentence: how E-01's finding constrains or refocuses this experiment's scope.]

[Execute experiment.]

E-02 output: [labeled finding]

Contract delivery: output label = "[plan label]" — consumed by: [SYNTHESIZER] — delivered? Yes / No
FAIL: Contract delivery absent or output label mismatch with Phase 1B plan.

**EXPERIMENT 2 COMPLETE**
Produced: E-02 — [one-line summary]
→ Consumed by: SYNTHESIZER

---

[Add E-03+ as needed. Every block requires:
1. A GATE-E{N}-entry confirmation
2. A verbatim blockquote Input section
3. Execution
4. A labeled E-NN output
5. A Contract delivery line with a delivered? boolean
6. An EXPERIMENT N COMPLETE marker with consumed-by routing]

**EXPERIMENTER COMPLETE**
All outputs: E-01 [type], E-02 [type], ...
→ SYNTHESIZER receives: all labeled experiment outputs

---

### SYNTHESIZER

GATE-EXPERIMENTER: Confirm EXPERIMENTER COMPLETE before executing.
FAIL: Any SYNTHESIZER section begins without EXPERIMENTER COMPLETE confirmed.

---

#### Feed-Forward Audit Ledger

| Experiment | Plan output label | Delivered? | Consumed by |
|-----------|------------------|------------|-------------|
| E-01 | [plan label] | Yes / No | [step] |
| E-02 | [plan label] | Yes / No | [step] |

Populate from Contract delivery lines in EXPERIMENTER. Do not infer values not stated in the experiment blocks.
FAIL: Ledger is absent, or any row's Delivered? value contradicts the Contract delivery line in the corresponding EXPERIMENTER block.

---

#### Findings

| # | Finding | Source | Confidence | Evidence basis |
|---|---------|--------|------------|---------------|
| F-01 | [finding text] | E-01 | high / medium / low | [e.g., "2 consistent sources", "single source not replicated"] |
| F-02 | [finding text] | E-02 | high / medium / low | [basis] |

Minimum 2 findings with distinct confidence levels.
FAIL: Fewer than 2 findings, all confidence levels are identical, or evidence basis is absent from any row.

---

#### Synthesis

What we thought: [hypothesis verbatim from PLANNER Phase 1]
What we actually learned: [confirm, refine, or refute — must differ from hypothesis text. Answer the research question.]

Inertia gap closure: [Did the experiment marked Closes gap? = Yes produce a finding that prove-topic could not have produced? Yes / No + one sentence of evidence.]

Cross-namespace note: [Name any downstream Signal artifact that should receive these findings — draft spec, scout brief, topic plan, topic story.]

FAIL: "What we actually learned" copies the hypothesis verbatim, or either synthesis field is absent.
FAIL: Inertia gap closure verdict is absent or states neither Yes nor No.

---

#### Principles

| Label | Principle | Source finding |
|-------|-----------|---------------|
| P-01 | [When X, do Y — or Always Z] | F-NN |
| P-02 | [When X, do Y — or Always Z] | F-NN |

Minimum 2 principles. No generic truisms.
FAIL: Fewer than 2 principles, principles are generic truisms without a specific finding origin, or source finding column is blank.

---

### Artifact

Write: `simulations/prove/research/{{topic}}-research-{{date}}.md`

Frontmatter:
```
skill: prove-program
topic: {{topic}}
date: {{date}}
hypothesis: [one line]
inertia_gap: [one line]
experiment_types: [list]
findings_count: [N]
principles_count: [N]
inertia_gap_closed: true / false
```

---

---

## Rubric coverage summary (v4 — 145 pts)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 hypothesis-first | Phase 1 before experiments, GATE-A | GATE-β blocks Phase 1B | Section 2, FAIL gate | GATE-H blocks Phase 1B | PLANNER Phase 1, GATE-H + FAIL |
| C-02 plan >=2 types + rationale | Phase 1B table, GATE-B | Phase 1B table, GATE-γ | Section 3 table, FAIL | Phase 1B table, GATE-P | PLANNER Phase 1B, GATE-P + FAIL |
| C-03 feed-forward | Verbatim blockquote (C-17 PASS auto-satisfies C-03) | Input citation per block | Section 4 Input citation + FAIL | Verbatim blockquote | EXPERIMENTER verbatim blockquote + FAIL |
| C-04 synthesis contrast | Phase 3C two fields, GATE-D | Phase 3C two fields, GATE-ζ | Section 7 two fields, FAIL | Phase 3C two fields, GATE-S | SYNTHESIZER synthesis two fields + FAIL |
| C-05 Qx.md format + path | Artifact section | Artifact section | Artifact section | Artifact section | Artifact section |
| C-06 principles >=2 | Phase 3D table | Phase 3D | Section 8 + FAIL | Phase 3D | SYNTHESIZER principles table + FAIL |
| C-07 confidence per finding | Phase 3B table | Phase 3B table, GATE-ε | Section 6 + FAIL | Phase 3B table, GATE-F | SYNTHESIZER findings table + FAIL |
| C-08 flexibility beyond prove-topic | Phase 0 inertia gap, Closes gap? column | GATE-0 inertia gap, Closes gap? column | Section 1 inertia gap + FAIL, Closes gap? column | GATE-0 + Closes gap? column | Pre-role inertia gap + GATE-0 + FAIL, Closes gap? |
| C-09 falsification | Phase 1 Falsification field | Phase 1 Falsification field | Section 2 Falsification + FAIL | Phase 1 Falsification | PLANNER Phase 1 Falsification + FAIL |
| C-10 cross-namespace | Phase 3C note | Phase 3C note | Section 7 note | Phase 3C note | SYNTHESIZER cross-namespace note |
| C-11 audit ledger | Phase 3A standalone table | Phase 3A standalone table | Section 5 standalone ledger + FAIL | Phase 3A standalone table | SYNTHESIZER audit ledger + FAIL |
| C-12 COMPLETE markers | No COMPLETE token per block (PARTIAL) | GATE-δN PASS but no COMPLETE token (PARTIAL) | No COMPLETE token (PARTIAL) | GATE-EN PASS but no COMPLETE token (PARTIAL) | EXPERIMENT N COMPLETE + consumed-by per block (PASS) |
| C-13 inertia gap bookending | Phase 0 + Closes gap? + Phase 3C closure | GATE-0 + Closes gap? + Phase 3C closure | Section 1 + Closes gap? + Section 7 closure | GATE-0 + Closes gap? + Phase 3C closure | Pre-role + PLANNER Closes gap? + SYNTHESIZER closure |
| C-14 plan output routing | Phase 1B: Output label + Consumed by columns | Phase 1B table Output label + Consumed by | Section 3 table Output label + Consumed by | Phase 1B table Output label + Consumed by | PLANNER Phase 1B table columns |
| C-15 delivery boolean | Contract delivery per block with boolean | Contract delivery per block with boolean | Contract delivery per block with boolean | Contract delivery per block with boolean | Contract delivery per block with boolean + FAIL |
| C-16 gap-to-plan column | Closes gap? column in Phase 1B | Closes gap? column in Phase 1B | Closes gap? column in Section 3 | Closes gap? column in Phase 1B | Closes gap? column in PLANNER Phase 1B |
| **C-17 verbatim quotation** | **PASS — blockquote required + FAIL for paraphrase** | PARTIAL — input citation but no blockquote format | PARTIAL — input citation without verbatim requirement | **PASS — blockquote required + prohibition stated** | **PASS — blockquote required + FAIL conditions** |
| **C-18 inter-phase GATE** | **PASS — GATE-A, GATE-B, GATE-C, GATE-D (4 gates beyond GATE-0)** | **PASS — GATE-β through GATE-ζ (5 gates beyond GATE-α)** | FAIL — no named GATE tokens, advisory structure only | **PASS — GATE-H, GATE-P, GATE-E1, GATE-E2, GATE-X, GATE-F, GATE-S (7 gates beyond GATE-0)** | **PASS — GATE-H, GATE-P, GATE-PLANNER, GATE-E1-entry, GATE-E2-entry, GATE-EXPERIMENTER (6 gates beyond GATE-0)** |
| **C-19 inline FAIL conditions** | PASS — >=3 precise FAIL conditions (Phase 0, Phase 1 GATE-A, Phase 1B, Phase 2 verbatim×2, Phase 3C, Phase 3D) | PARTIAL — GATE STOP conditions present but not labeled FAIL; >=3 conditions present but form differs from C-19 requirement | **PASS — >=3 precise inline FAIL conditions per criterion throughout** | PASS — >=3 FAIL conditions (GATE-0 FAIL, GATE-H FAIL, Phase 2 verbatim FAIL, GATE-E1 FAIL, GATE-E2 FAIL) | **PASS — >=3 per-criterion FAIL conditions throughout all roles** |

**Projected v4 scores (aspirational tier gaps noted):**

| Variation | Primary axis | C-17 | C-18 | C-19 | Expected ceiling |
|-----------|-------------|------|------|------|-----------------|
| V-01 | Verbatim quotation | PASS | PASS | PASS | ~143/145 (C-12 PARTIAL) |
| V-02 | Gate enforcement | PARTIAL | PASS | PARTIAL | ~128/145 |
| V-03 | Inline FAIL conditions | PARTIAL | FAIL | PASS | ~125/145 |
| V-04 | C-17 + C-18 combined | PASS | PASS | PASS | ~143/145 (C-12 PARTIAL) |
| V-05 | All three + role sequence | PASS | PASS | PASS | ~145/145 |
