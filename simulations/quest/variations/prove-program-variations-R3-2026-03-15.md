Here are the five R3 variations written to `simulations/quest/variations/prove-program-variations-R3-2026-03-15.md`.

---

## R3 Variation Summary

**Single-axis:**

| | Axis | Hypothesis |
|---|---|---|
| **V-01** | Lifecycle emphasis (3-phase COMMIT/EXECUTE/VERIFY) | Phase structure can deliver C-14+C-15+C-16 without role sequence — COMMIT anchors the plan pre-commitment, EXECUTE puts the boolean in the block, gap column threads C-16 |
| **V-02** | Output format (unified evolving table) | A single growing table achieves C-14+C-16 but **exposes C-15's gap**: updating a table column outside the block does not satisfy the per-block boolean requirement |
| **V-03** | Phrasing register (imperative procedural + FAIL conditions) | FAIL gates at each step enforce ordering and completeness at lower cognitive overhead — achieves C-14+C-15+C-16 but loses C-11 (no standalone ledger) |

**Combined:**

| | Axes | Key finding |
|---|---|---|
| **V-04** | Output format + lifecycle (contract loop as primary metaphor) | Minimum structure for C-14+C-15+C-11+C-12(partial) — **no C-13/C-16** — isolates the pure feed-forward machinery baseline |
| **V-05** | Role sequence + all 8 aspirational criteria | Extends R2 V-05 with one line per COMPLETE block (`Contract delivery: ... delivered? Yes/No`); first variation targeting **40/40 aspirational** |

**Aspirational score estimates (C-09–C-16, 40 pts total):** V-01: 38 | V-02: 33 | V-03: 33 | V-04: 28 | V-05: **40**

The critical diagnostic the rubric coverage table surfaces: **C-15 is the hardest to satisfy incidentally** — a table cell updated after a block (V-02) doesn't count; the boolean must appear *inside* the experiment block prose.
e Phase 1 begins, declare why this question requires prove-program. Name the specific
characteristic that falls outside prove-topic's capability: cross-namespace scope, external
domain lookup, custom data experiment, multi-hypothesis structure, or span across multiple
threads.

Inertia gap: [what prove-topic cannot do for this question — one sentence, specific]

GATE: Inertia gap REQUIRED before Phase 1. If prove-topic is sufficient, stop.

---

## Phase 1 — COMMIT

Complete this phase entirely before any experiment runs. Every value you fill in here is a
binding commitment Phases 2 and 3 must honor.

### 1A — Hypothesis

Hypothesis: [what you believe is true — one sentence, positive form]
Falsification: [what evidence would cause you to reject this hypothesis]

GATE: Hypothesis and falsification REQUIRED before 1B.

### 1B — Experiment Plan Contract

Produce this table before Phase 2 begins.

| # | Type | Question | Rationale | Output label | Consumed by | Closes gap? |
|---|------|----------|-----------|-------------|-------------|-------------|
| E-01 | [type] | [question] | [why this type] | [label-01] | [E-02 / Phase 3] | Yes / No |
| E-02 | [type] | [question] | [why this type] | [label-02] | [Phase 3] | Yes / No |

Rules:
- ≥2 distinct types (websearch, intelligence, analysis, interview, prototype, custom)
- "Output label" and "Consumed by" are contracts Phase 2 must fulfill exactly
- ≥1 row "Closes gap? = Yes" — this experiment directly addresses the Phase 0 inertia gap
- Add E-03+ rows as needed

GATE: Contract table complete before Phase 2.

---

## Phase 2 — EXECUTE

Run experiments in contract order. Each block must follow this structure:

**E-NN — [Type]**

Input: [For E-01: Phase 1 hypothesis + plan summary. For E-02+: quote the specific output
content from the previous block that scopes this experiment — not "see above."]
Scope: [one sentence — how the input frames this experiment's question]
[Execute]
E-NN output ([output label from Phase 1 contract]): [labeled finding]
**Contract delivery:** output label = "[label from contract]" = "[one-line finding summary]",
consumed by = "[consumer from contract]" — delivered? Yes / No

"Input:", labeled "E-NN output", and "Contract delivery:" are REQUIRED for every block.

---

## Phase 3 — VERIFY

### 3A — Feed-Forward Audit

Verify every row in the Phase 1 contract:

| Experiment | Output (committed) | Output (delivered) | Consumed by (committed) | Consumed by (actual) | Met? |
|-----------|--------------------|--------------------|------------------------|----------------------|------|
| E-01 | [from Phase 1] | [from Phase 2] | [from Phase 1] | [cite section] | Yes/No |
| E-02 | [from Phase 1] | [from Phase 2] | [from Phase 1] | [cite section] | Yes/No |

A "No" row identifies an open feed-forward gap.

### 3B — Findings

| # | Finding | Source | Confidence | Evidence basis |
|---|---------|--------|------------|----------------|
| F-01 | | E-NN | high / med / low | |
| F-02 | | E-NN | high / med / low | |

≥2 findings with distinct confidence levels.

### 3C — Synthesis

What we thought: [hypothesis verbatim from Phase 1]
What we actually learned: [confirm, refine, or refute — must differ. Answer the research
question.]

**Inertia gap closure:** Did the gap-closing experiment (E-NN per contract) produce findings
prove-topic could not have produced? Yes or No — one sentence of evidence.

Cross-namespace note: Name the downstream Signal artifact this research should update — draft
spec, scout brief, flow diagram, topic plan, topic story. State what finding it receives.

### 3D — Principles

| Label | Principle | Source |
|-------|-----------|--------|
| P-01 | [When X, do Y / Always Z] | F-NN |
| P-02 | [...] | F-NN |

≥2 principles, labeled, no generic truisms.

---

## Artifact

Write: `simulations/prove/research/{{topic}}-research-{{date}}.md`

Frontmatter:
  skill: prove-program
  topic: {{topic}}
  date: {{date}}
  hypothesis: [one line]
  inertia_gap: [one line]
  inertia_gap_closed: true/false
  experiment_types: [list in execution order]
  findings_count: N
  principles_count: N
  contracts_met: true/false
```

---

## V-02 — Output Format axis (unified evolving table)

**Variation axis:** Output format — single table that begins as a plan and grows into an audit record
**Hypothesis:** A unified "program table" that starts as a plan (columns: Type, Question, Output label, Consumed by, Closes gap?) and is incrementally completed during execution (Delivered?, Consumed by actual, Contract met?) achieves C-14 + C-16 in the plan phase and approximates C-11 at synthesis — all in one scannable structure — but trades per-block C-15 compliance (which requires the boolean inside the experiment block, not a table cell updated after) for a lower-friction document format.

---

```
You are running a research program for: **{{topic}}**

Research question: {{research_question}}

---

### Inertia Check

prove-topic runs intelligence, analysis, interview, and synthesis on a **single Signal topic**
in sequence. If this question fits one topic — stop and use prove-topic.

Inertia gap: [what prove-topic cannot do here — one sentence, specific]

GATE: Inertia gap required before continuing.

---

### Hypothesis

Hypothesis: [what you believe is true — one sentence, positive form]
Falsification: [what evidence would refute this hypothesis]

---

### Program Table

Complete the PLAN columns before running any experiment. Fill EXECUTION and AUDIT columns
as you run. This table is the complete plan-to-execution record.

| Step | Type | Question | Output label | Consumed by | Closes gap? | Delivered? | Consumed by (actual) | Contract met? |
|------|------|----------|-------------|-------------|-------------|------------|----------------------|---------------|
| E-01 | [type] | [question] | [label] | [E-02 / Synthesis] | Y / N | ← fill after E-01 | ← fill after E-01 | ← fill in Synthesis |
| E-02 | [type] | [question] | [label] | [Synthesis] | Y / N | ← fill after E-02 | ← fill after E-02 | ← fill in Synthesis |

Rules:
- ≥2 distinct types (websearch, intelligence, analysis, interview, prototype, custom)
- ≥1 row "Closes gap? = Y" — addresses the declared inertia gap
- PLAN columns (Type through Closes gap?) complete before any experiment runs
- EXECUTION columns (Delivered?, Consumed by actual) updated immediately after each block
- AUDIT column (Contract met?) filled in Synthesis

GATE: PLAN columns complete before Experiment Execution.

---

### Experiment Execution

**E-NN — [Type]**

Input: [For E-01: hypothesis + program table plan summary. For E-02+: quote the specific
output from the previous experiment block that scopes this one — not "see above."]
[Execute]
E-NN output ([output label from program table]): [finding]
→ Update program table: fill Delivered? and Consumed by (actual) for this row now.

[Repeat for each planned experiment. "Input:" citation and labeled output required per block.]

---

### Findings

| # | Finding | Source | Confidence | Evidence basis |
|---|---------|--------|------------|----------------|
| F-01 | | E-NN | high / med / low | |
| F-02 | | E-NN | high / med / low | |

≥2 findings with distinct confidence levels.

---

### Synthesis

Fill the Contract met? column in the program table. All rows should show "Yes." A "No" row
identifies an open feed-forward gap.

What we thought: [hypothesis verbatim]
What we actually learned: [confirm, refine, or refute — must differ from hypothesis]

Inertia gap closure: Did the Closes gap? = Y experiment produce findings prove-topic could not
have produced? Yes or No — one sentence of evidence.

Cross-namespace note: Name the downstream Signal artifact and what finding it receives.

---

### Principles

| Label | Principle | Source |
|-------|-----------|--------|
| P-01 | [When X, do Y / Always Z] | F-NN |
| P-02 | | F-NN |

≥2 principles, labeled, no truisms.

---

### Artifact

Write: `simulations/prove/research/{{topic}}-research-{{date}}.md`

Frontmatter:
  skill: prove-program
  topic: {{topic}}
  date: {{date}}
  hypothesis: [one line]
  inertia_gap: [one line]
  inertia_gap_closed: true/false
  experiment_types: [list]
  findings_count: N
  principles_count: N
  contracts_met: true/false
```

---

## V-03 — Phrasing Register axis (imperative procedural with FAIL conditions)

**Variation axis:** Phrasing register — numbered steps with explicit FAIL conditions per gate
**Hypothesis:** Replacing section headers and prose instructions with numbered procedural steps and FAIL conditions — where each step names the exact failure mode that blocks progress — achieves full essential + aspirational criterion coverage at lower cognitive overhead than role-sequence or lifecycle variants, because FAIL conditions enforce ordering and completeness requirements at the point of execution rather than requiring the model to recall gate semantics from a preamble.

---

```
Research program: **{{topic}}**
Research question: {{research_question}}

Execute steps in order. Each step has a FAIL condition — if it triggers, stop and fix before
continuing.

---

**STEP 0 — Inertia screen**

State why this question cannot be answered by prove-topic (single Signal topic, sequential
prove run).

Inertia gap: ___

FAIL: Gap is empty, vague, or describes something prove-topic can already do → stop, reframe,
or switch to prove-topic.

---

**STEP 1 — Hypothesis**

Write one sentence: what you believe is true (positive form).
Write one sentence: what evidence would cause you to reject it (specific, testable condition).

FAIL: Hypothesis is a question, restates the research question, or lacks a falsification
condition → rewrite.

---

**STEP 2 — Experiment plan** (complete before running any experiment)

For each planned experiment, fill one row:

| # | Type | Question | Rationale | Output label | Consumed by | Closes gap? |
|---|------|----------|-----------|-------------|-------------|-------------|

Requirements:
- ≥2 distinct types (websearch, intelligence, analysis, interview, prototype, custom)
- ≥1 row "Closes gap? = Yes" — directly addresses the STEP 0 inertia gap
- "Output label" and "Consumed by" are binding commitments STEP 3 must honor exactly

FAIL: Fewer than 2 types, no gap-closing row, or any Output label is blank → fix before
STEP 3.

---

**STEP 3 — Experiments** (run in plan order)

For each experiment E-NN, execute all four items:

1. Write: Input: [quote prior output content — exact words. E-01: hypothesis + plan summary.
   E-02+: specific finding from prior block that scopes this one — not "see above."]
2. Execute the experiment.
3. Write: E-NN output ([output label from STEP 2]): [labeled finding]
4. Write: Contract delivery: output label = "[label]" = "[one-line finding summary]",
   consumed by = "[consumer from STEP 2]" — delivered? Yes / No

FAIL: Any block missing item 1 (Input), item 3 (labeled output), or item 4 (Contract
delivery with boolean) → add before continuing.

---

**STEP 4 — Findings**

For each major finding, one row:

| Finding | Source (E-NN) | Confidence (high / med / low) | Basis (one sentence) |

FAIL: Fewer than 2 findings, or all findings share the same confidence level → add
distinctions.

---

**STEP 5 — Synthesis**

Write each line in order:
1. What we thought: [hypothesis verbatim from STEP 1]
2. What we actually learned: [confirm, refine, or refute — MUST differ from STEP 1 text.
   Answer the research question directly.]
3. Inertia gap closure: [Yes or No — one sentence of evidence from the gap-closing
   experiment]
4. Cross-namespace note: [name the downstream Signal artifact and what finding it receives —
   draft spec, scout brief, flow diagram, topic plan, topic story. Not generic.]

FAIL: "What we actually learned" repeats the hypothesis verbatim, inertia gap closure is
absent, or cross-namespace note is generic ("see upstream artifacts") → rewrite.

---

**STEP 6 — Principles**

Write ≥2 principles. Each: P-NN: [When X, do Y] or [Always Z]. Specific and actionable.

FAIL: Fewer than 2 principles, or any is a generic truism (e.g., "do thorough research",
"consider trade-offs") → replace.

---

**Output document**

Write to: `simulations/prove/research/{{topic}}-research-{{date}}.md`

The document must contain these labeled sections in order:
1. Hypothesis (with falsification)
2. Experiment Plan (table with Output label, Consumed by, Closes gap? columns)
3. Experiments (each with Input citation, labeled output, Contract delivery line with boolean)
4. Findings (with confidence annotations, distinct levels)
5. Synthesis (what-we-thought / what-we-learned / gap closure / cross-namespace note)
6. Principles (P-NN labeled, imperative or conditional)

Frontmatter: skill: prove-program | topic | date | hypothesis | inertia_gap |
             inertia_gap_closed | experiment_types | findings_count | principles_count |
             contracts_met
```

---

## V-04 — Combined: C-14 + C-15 closed contract loop (no inertia framing, no role sequence)

**Variation axes:** Output format (contract-table-first) + lifecycle emphasis (contract loop as primary structural metaphor)
**Hypothesis:** The C-14/C-15 contract loop (plan pre-commits output labels + consumer per experiment; each block verifies delivery with an explicit boolean) is the minimum structure that simultaneously satisfies C-11 (feed-forward ledger), C-12 (per-block routing), C-14 (plan pre-commitment), and C-15 (boolean verification) without requiring role sequence or inertia framing — yielding 4 of the 8 aspirational criteria at roughly half the structural overhead of V-05.

---

```
You are running a research program for: **{{topic}}**

Research question: {{research_question}}

This prompt is organized around a plan-to-execution contract. Fill the contract table before
running any experiment. Each experiment block verifies its contract. Synthesis audits the
full contract.

---

### Hypothesis

Hypothesis: [what you believe is true — one sentence, positive form]
Falsification: [what evidence would refute this hypothesis]

GATE: Hypothesis required before plan.

---

### Experiment Plan Contract

Complete this table before running any experiment. Every value in the table is a commitment.

| # | Type | Question | Rationale | Output label | Consumed by |
|---|------|----------|-----------|-------------|-------------|
| E-01 | [type] | [question] | [why this type, not another] | [label-01] | [E-02 / Findings / Synthesis] |
| E-02 | [type] | [question] | [why this type, not another] | [label-02] | [Findings / Synthesis] |

Rules:
- ≥2 distinct types (websearch, intelligence, analysis, interview, prototype, custom)
- At least one experiment must represent scope beyond a single Signal topic — mark that row
  with "☆" in the Rationale cell and note the cross-topic or cross-namespace angle
- "Output label" and "Consumed by" are the contract. Execution must use these exact labels
  and route to these exact consumers.

GATE: Contract table complete before Experiment Execution.

---

### Experiment Execution

Run in contract order. Each block must follow this structure exactly:

**E-NN — [Type]**

Input: [For E-01: hypothesis + plan summary. For E-02+: quote the specific output content
from the previous block that scopes this experiment — exact words, not "see above."]
Scope: [one sentence — how the input frames this experiment's specific question]
[Execute]
E-NN output ([output label from contract]): [labeled finding]
**Contract delivery:** output label = "[label from contract]" = "[one-line finding summary]",
consumed by = "[consumer from contract]" — delivered? Yes / No

"Input:", labeled "E-NN output (label)", and "Contract delivery:" REQUIRED for every block.

---

### Feed-Forward Audit

Verify every row in the contract:

| Experiment | Output (contracted) | Output (delivered) | Consumed by (contracted) | Consumed by (actual) | Met? |
|-----------|---------------------|--------------------|--------------------------|----------------------|------|
| E-01 | [from contract] | [from execution] | [from contract] | [cite section] | Yes/No |
| E-02 | [from contract] | [from execution] | [from contract] | [cite section] | Yes/No |

A "No" row identifies an open feed-forward gap.

---

### Findings

| # | Finding | Source | Confidence | Evidence basis |
|---|---------|--------|------------|----------------|
| F-01 | | E-NN | high / med / low | |
| F-02 | | E-NN | high / med / low | |

≥2 findings with distinct confidence levels.

---

### Synthesis

What we thought: [hypothesis verbatim]
What we actually learned: [confirm, refine, or refute — must differ. Answer the research
question.]

Cross-namespace note: Name the downstream Signal artifact and what finding it receives — draft
spec, scout brief, flow diagram, topic plan, topic story. Substantive, not generic.

---

### Principles

| Label | Principle | Source |
|-------|-----------|--------|
| P-01 | [When X, do Y / Always Z] | F-NN |
| P-02 | | F-NN |

≥2 principles, labeled, no truisms.

---

### Artifact

Write: `simulations/prove/research/{{topic}}-research-{{date}}.md`

Frontmatter:
  skill: prove-program
  topic: {{topic}}
  date: {{date}}
  hypothesis: [one line]
  experiment_types: [list]
  findings_count: N
  principles_count: N
  contracts_met: true/false
```

---

## V-05 — Combined: Role sequence + all 8 aspirational criteria (max aspirational)

**Variation axes:** Role sequence + feed-forward contract ledger + inertia gap bookending + C-15 per-block boolean delivery
**Hypothesis:** Extending R2 V-05 with an explicit "Contract delivery: ... delivered? Yes/No" line inside each EXPERIMENTER COMPLETE block — the sole structural gap R2 V-05 had against C-15 — closes the remaining criterion and produces the first variation targeting a perfect 40/40 aspirational score, because R2 V-05 already satisfied C-09 through C-14 and C-16 by design; C-15 is the only missing element and requires only one line per block.

---

```
You are running a research program for: **{{topic}}**

Research question: {{research_question}}

---

### Pre-Program: Inertia Gap Declaration

prove-topic: runs intelligence, analysis, interview, and synthesis on a **single Signal topic**
in sequence. If one topic, one thread — use prove-topic.

This declaration executes before any role begins. State why this question requires
prove-program. Name the specific capability it needs that prove-topic cannot provide.

Inertia gap: [what prove-topic cannot do for this question — one sentence, specific]

GATE: Inertia gap REQUIRED before any role executes. If prove-topic is sufficient, stop.

---

### Role Declarations

| Role | Writes | May NOT write |
|------|--------|---------------|
| PLANNER | Hypothesis, falsification, experiment plan contract table | Experiment results, findings, synthesis, principles |
| EXPERIMENTER | Experiment execution blocks (one at a time, each reading prior outputs) | New plan items, synthesis, hypothesis revisions |
| SYNTHESIZER | Feed-forward audit table, findings, synthesis, gap closure verdict, principles | New experiments, retroactive hypothesis changes |

---

### PLANNER

**Phase 1 — Hypothesis**

Hypothesis: [what you believe is true — one sentence, positive form]
Falsification: [what evidence would cause you to reject this hypothesis]

GATE: Hypothesis and falsification REQUIRED before Phase 2.

**Phase 2 — Experiment Plan Contract Table**

Produce this table before any experiment runs. It is the binding contract EXPERIMENTER must
fulfill and SYNTHESIZER must audit.

| # | Type | Question | Rationale | Output label | Consumed by | Closes inertia gap? |
|---|------|----------|-----------|-------------|-------------|---------------------|
| E-01 | | | | [label] | [E-02 or SYNTHESIZER] | Yes / No |
| E-02 | | | | [label] | [SYNTHESIZER] | Yes / No |

Rules:
- ≥2 distinct types (websearch, intelligence, analysis, interview, prototype, custom)
- ≥1 row "Closes inertia gap? = Yes" — directly addresses the declared gap
- "Output label" and "Consumed by" are commitments EXPERIMENTER must fulfill exactly
- Add E-03+ rows as needed

**PLANNER COMPLETE**
Hypothesis (verbatim): [text]
Falsification (verbatim): [text]
Inertia gap addressed by: E-NN — [type]
Contract table: [N experiments, ordered]
→ EXPERIMENTER receives: hypothesis, falsification criteria, ordered contract table.

---

### EXPERIMENTER

REQUIRED: Confirm PLANNER COMPLETE marker present before executing E-01.

Each block must follow this structure:

**E-01 — [Type]**
Entry input: PLANNER hypothesis + contract table
Scope: [one sentence — how the hypothesis frames this experiment's question]
[Execute]
E-01 output ([label from contract]): [labeled finding]

**E-01 COMPLETE**
Produced: [one-line output summary]
→ Consumed by: [experiment label or SYNTHESIZER — must match contract table]
Contract delivery: output label = "[label from contract]" = "[one-line finding summary]",
consumed by = "[consumer from contract]" — delivered? Yes / No

---

**E-02 — [Type]**
Entry input: E-01 — "[quote the specific finding content from E-01 that scopes this
experiment — not 'see above']"
Scope adjustment: [one sentence — how E-01's output changes this experiment's focus]
[Execute]
E-02 output ([label from contract]): [labeled finding]

**E-02 COMPLETE**
Produced: [one-line output summary]
→ Consumed by: [SYNTHESIZER — must match contract table]
Contract delivery: output label = "[label from contract]" = "[one-line finding summary]",
consumed by = "[consumer from contract]" — delivered? Yes / No

---

[Add E-03+ as needed. Entry input citation, COMPLETE record, and Contract delivery line
REQUIRED for every block.]

**EXPERIMENTER COMPLETE**
All outputs delivered: E-01 ([type]), E-02 ([type]), ...
All "Consumed by" values honored: [Yes — list any gaps]
→ SYNTHESIZER receives: all labeled experiment outputs.

---

### SYNTHESIZER

REQUIRED: Confirm EXPERIMENTER COMPLETE marker present before executing.

**Feed-Forward Audit Table**

Verify every contract row from the PLANNER table:

| Experiment | Output label (contracted) | Output label (delivered) | Consumed by (contracted) | Consumed by (actual) | Contract met? |
|-----------|--------------------------|--------------------------|--------------------------|----------------------|---------------|
| E-01 | [from PLANNER] | [from E-01 COMPLETE] | [from PLANNER] | [cite section] | Yes / No |
| E-02 | [from PLANNER] | [from E-02 COMPLETE] | [from PLANNER] | [cite section] | Yes / No |

All rows must show "Yes." A "No" row = open feed-forward gap.

**Findings**

| # | Finding | Source | Confidence | Evidence basis |
|---|---------|--------|------------|----------------|
| F-01 | | E-NN | high / med / low | |
| F-02 | | E-NN | high / med / low | |

≥2 findings with distinct confidence levels.

**Synthesis**

What we thought: [hypothesis verbatim from PLANNER Phase 1]
What we actually learned: [confirm, refine, or refute — must differ. Answer the research
question directly.]

**Inertia gap closure:** Did the gap-closing experiment (E-NN per contract) produce findings
prove-topic could not have produced? Yes or No — one sentence of evidence.

Cross-namespace note: [Name the downstream Signal artifact and what finding it receives —
draft spec, scout brief, flow diagram, topic plan, topic story. Substantive, not generic.]

**Principles**

| Label | Principle | Source finding |
|-------|-----------|----------------|
| P-01 | [When X, do Y / Always Z — specific, actionable] | F-NN |
| P-02 | [...] | F-NN |

≥2 principles, labeled, no truisms.

---

### Artifact

Write: `simulations/prove/research/{{topic}}-research-{{date}}.md`

Frontmatter:
  skill: prove-program
  topic: {{topic}}
  date: {{date}}
  hypothesis: [one line]
  inertia_gap: [one line]
  inertia_gap_closed: true/false
  experiment_types: [list in execution order]
  findings_count: N
  principles_count: N
  contracts_met: true/false
```

---

## Rubric coverage summary (v3 rubric — 130 points)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 hypothesis-first | Phase 1 gate before plan | Hypothesis before Program Table | STEP 1 before STEP 2 gate | Hypothesis gate | PLANNER Phase 1 gate |
| C-02 plan ≥2 types + rationale | Phase 1B contract table | Program Table PLAN columns | STEP 2 table + rationale column | Contract table + rationale | PLANNER Phase 2 contract table |
| C-03 feed-forward | Input: per block + 3A audit | Input: per block + table update | STEP 3 item 1 + STEP 4 audit | Input: per block + audit table | Entry input + COMPLETE + audit |
| C-04 thought vs learned | 3C two-field | Synthesis two-field | STEP 5 line 1 / line 2 | Synthesis two-field | Synthesis two-field |
| C-05 Qx.md format | Named phases + path | Named sections + path | Explicit output section list + path | Named sections + path | Role blocks + path |
| C-06 principles ≥2 | 3D table + basis | Principles table + basis | STEP 6 P-NN per-line | Principles table + basis | P-NN table in SYNTHESIZER |
| C-07 confidence per finding | Distinct levels in 3B table | Distinct levels in Findings table | STEP 4 distinct levels | Distinct levels in findings table | Distinct levels in SYNTHESIZER findings |
| C-08 beyond prove-topic | Gap-closing experiment in plan | Closes gap? = Y row | Gap-closing row STEP 2 | ☆ marker in Rationale | Closes inertia gap? = Yes in contract |
| C-09 falsification | 1A field | Hypothesis section field | STEP 1 sentence 2 | Hypothesis section field | PLANNER Phase 1 field |
| C-10 cross-namespace | 3C note | Synthesis note | STEP 5 line 4 | Synthesis note | SYNTHESIZER note |
| **C-11** feed-forward ledger | **Yes** — 3A audit table | **Yes** — Contract met? column in program table (filled in Synthesis) | **No** standalone ledger | **Yes** — Feed-Forward Audit table | **Yes** — SYNTHESIZER audit table |
| **C-12** per-exp COMPLETE + consumed-by | Partial — Contract delivery line (output + routing + boolean, no "COMPLETE" keyword) | Partial — table update instruction (not in experiment block prose) | Partial — Contract delivery line inside block | Partial — Contract delivery line (output + routing + boolean, no COMPLETE keyword) | **Yes** — E-NN COMPLETE with produced + consumed routing |
| **C-13** inertia gap bookend | **Yes** — Phase 0 declare + plan Closes gap? mark + 3C verdict | **Yes** — inertia gap + program table gap column + synthesis closure | **Yes** — STEP 0 declare + STEP 2 gap column + STEP 5 closure | **No** — C-08 only (☆ marker, no bookend declare/close lifecycle) | **Yes** — Pre-Program + contract Closes gap? + SYNTHESIZER verdict |
| **C-14** plan output routing pre-commitment | **Yes** — Phase 1B table has Output label + Consumed by columns pre-execution | **Yes** — Program Table PLAN columns (Output label + Consumed by) before execution | **Yes** — STEP 2 table Output label + Consumed by columns | **Yes** — Contract table has Output label + Consumed by columns | **Yes** — PLANNER contract table has Output label + Consumed by columns |
| **C-15** per-experiment delivery boolean | **Yes** — "Contract delivery: label = '...', consumed by = '...' — delivered? Yes/No" per block | **No** — Delivered? column updated in table outside the block, not inside the experiment block prose | **Yes** — STEP 3 item 4: "Contract delivery: ... — delivered? Yes/No" | **Yes** — "Contract delivery: ... — delivered? Yes/No" per block | **Yes** — Contract delivery line inside E-NN COMPLETE block with boolean |
| **C-16** gap-to-plan column threading | **Yes** — "Closes gap?" column in Phase 1B table; C-13 passes | **Yes** — "Closes gap?" column in Program Table PLAN section; C-13 passes | **Yes** — "Closes gap?" column in STEP 2 table; C-13 passes | **No** — C-13 does not pass; C-16 requires C-13 | **Yes** — "Closes inertia gap?" column in PLANNER contract; C-13 passes |
| **Est. new aspirational pts (C-14/15/16)** | **15** | **10** | **10** | **10** | **15** |
| **Est. total aspirational pts (C-09–C-16)** | **38** | **33** | **33** | **28** | **40** |

**Key distinctions from R2:**
- V-01 is the first single-axis variation to target all three new criteria — 3-phase lifecycle gives C-14 (COMMIT table), C-15 (EXECUTE block), C-16 (Closes gap? column + C-13 passes via Phase 0 + 3C)
- V-02 isolates the unified evolving table format and reveals its C-15 gap: table-column updates outside the block do not satisfy the per-block boolean requirement
- V-03 shows that FAIL conditions + checklist format achieve C-14/C-15/C-16 compliance at the cost of C-11 (no standalone ledger table), trading auditability for brevity
- V-04 establishes the minimum contract-loop structure (C-14 + C-15 + C-11 + C-12 partial) without C-13/C-16 — the pure "feed-forward machinery" baseline for cross-variation comparison
- V-05 is the first variation targeting 40/40 aspirational: the only structural addition over R2 V-05 is the "Contract delivery: ... delivered? Yes/No" line inside each E-NN COMPLETE block

**Coverage gaps to watch in golden runs:**
- C-12 vs C-15 distinction: variations with "Contract delivery:" lines (V-01, V-03, V-04, V-05) satisfy C-15 (plan reference + boolean) but NOT C-12 (no "E-NN COMPLETE" keyword) — except V-05 which has both COMPLETE and Contract delivery
- C-16 requires C-13: V-04 cannot score C-16 regardless of plan table structure; raters should not award C-16 when C-13 fails
- V-02 unified table: C-15 will be the most common scoring dispute — raters should verify the boolean appears inside the experiment prose block, not only as a table cell update
