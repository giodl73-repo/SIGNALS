---

# prove-program — Variations R2 (V-01 through V-05)

**Single-axis:** V-01 (inertia framing), V-02 (output format — double contract ledger), V-03 (phrasing register — telegraphic minimal)
**Combined:** V-04 (output format + inertia framing), V-05 (role sequence + ledger + inertia gap)

---

## V-01 — Inertia Framing axis

**Variation axis:** Inertia framing
**Hypothesis:** Standalone inertia gap bookending — without role sequence machinery — is sufficient to achieve C-13 and C-12 while reducing structural overhead, because the gap lifecycle (declare → mark → close) provides natural section anchors that substitute for role transitions.

---

```
You are running a research program for: **{{topic}}**

Research question: {{research_question}}

---

### Inertia Check

prove-topic runs intelligence, analysis, interview, and synthesis on a **single Signal topic**
in sequence. If this question is about one topic, one namespace, one thread — prove-topic is
the right tool. Stop and use it.

Before planning, declare why this question requires prove-program. Name the specific
characteristic that falls outside prove-topic's capability: cross-namespace scope, external
domain lookup, custom data experiment, multi-hypothesis structure, or span across multiple
threads.

Inertia gap: [what prove-topic cannot do for this question — one sentence]

GATE: Inertia gap REQUIRED before any section below executes. If prove-topic is sufficient,
stop.

---

### Hypothesis

State the specific belief you are testing. Must appear before any experiment is described.

Hypothesis: [what you believe is true — positive form, one sentence]
Falsification: [what evidence would cause you to reject this hypothesis]

GATE: Hypothesis and falsification REQUIRED before Experiment Plan.

---

### Experiment Plan

Select ≥2 distinct experiment types (websearch, intelligence, analysis, interview, prototype,
custom). For each, state:
- Type
- Question it answers
- Why this type over alternatives
- Output label for downstream use
- Closes inertia gap? (Yes/No — at least one must be Yes)

The gap-closing experiment MUST exist and be marked.

---

### Experiment Execution

Each experiment block must follow this structure:

**E-NN — [Type]**

Entry input: [prior output label — quote specific content. For E-01, cite hypothesis + plan.]
Scope: [one sentence — how the prior input scopes this experiment's focus]
[Execute]
E-NN output ([output label from plan]): [labeled finding]
→ Consumed by: [next experiment label or "Findings" or "Synthesis"]

"Entry input" and "→ Consumed by:" are REQUIRED for each block.

---

### Findings

For each major finding:
- Finding text
- Source: E-NN
- Confidence: high / medium / low — [one sentence qualifier]

Minimum 2 findings with distinct confidence annotations.

---

### Synthesis

What we thought: [hypothesis verbatim from Hypothesis section]
What we actually learned: [confirm, refine, or refute — must differ from hypothesis text]

**Inertia gap closure:** Did the gap-closing experiment produce findings prove-topic could not
have produced? Yes or No — one sentence of evidence.

Cross-namespace note: Name any downstream Signal artifact this research should update — draft
spec, scout brief, flow diagram, topic plan, or topic story. State what it receives.

---

### Principles

≥2 principles. Label P-01, P-02, ... Imperative or conditional form: "When X, do Y" or
"Always Z." No generic truisms.

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
```

---

## V-02 — Output Format axis (double contract ledger)

**Variation axis:** Output format — two-phase ledger (plan contract + synthesis audit)
**Hypothesis:** A two-phase ledger — a contract table declared in the plan before execution, and an audit table in synthesis that verifies every contract was honored — produces the strongest evidence for C-11 and C-03 compliance by making contract violations visible without reading experiment prose.

---

```
You are running a research program for: **{{topic}}**

Research question: {{research_question}}

Read all sections before filling in any. Complete in order. Do not skip forward.

---

### Section 1 — Hypothesis

Hypothesis: [what you believe is true — one sentence, positive form]
Falsification: [what evidence would refute this hypothesis]

GATE: Section 1 REQUIRED before Section 2.

---

### Section 2 — Experiment Plan + Feed-Forward Contract Table

Fill this table completely before running any experiment. The "Output label" and "Consumed by"
columns are a binding contract that Section 3 and Section 5 must honor.

| # | Type | Question answered | Rationale | Output label | Consumed by | Scope note |
|---|------|------------------|-----------|-------------|-------------|------------|
| E-01 | [type] | [question] | [why this type] | [label] | [E-02 / Section 4] | — |
| E-02 | [type] | [question] | [why this type] | [label] | [Section 4/5] | — |

Rules:
- ≥2 distinct types (websearch, intelligence, analysis, interview, prototype, custom).
- At least one row must represent scope prove-topic cannot execute. Mark that row "(*)" in
  Scope note.
- "Output label" and "Consumed by" values are contracts. Reference exact labels in Sections 3,
  4, and 5.

GATE: Contract table complete before Section 3.

---

### Section 3 — Experiment Execution

Execute in Section 2 order. Each block:

#### E-01 — [Experiment Type]

Input: Section 1 hypothesis + Section 2 contract table
[Execute]
E-01 output ([label from contract]): [finding]
**Contract delivery:** output label = "[label]", consumed by = "[per Section 2]" — delivered? Yes

---

#### E-02 — [Experiment Type]

Input: E-01 — "[quote the specific finding from E-01 that scopes this experiment]"
Scope adjustment: [one sentence — how E-01 changes this experiment's focus]
[Execute]
E-02 output ([label from contract]): [finding]
**Contract delivery:** output label = "[label]", consumed by = "[per Section 2]" — delivered? Yes

---

[Add E-03+ as needed. "Input:" citation and "Contract delivery:" line REQUIRED for each block.]

---

### Section 4 — Findings

| # | Finding | Source | Confidence | Evidence basis |
|---|---------|--------|------------|----------------|
| F-01 | [finding text] | E-01 | high/med/low | [qualifier] |
| F-02 | [finding text] | E-02 | high/med/low | [qualifier] |

Minimum 2 findings with distinct confidence annotations.

---

### Section 5 — Synthesis + Feed-Forward Audit Table

**Feed-forward audit** — verify every Section 2 contract:

| Experiment | Output label (contracted) | Output label (delivered) | Consumed by (contracted) | Consumed by (actual) | Met? |
|-----------|--------------------------|--------------------------|--------------------------|----------------------|------|
| E-01 | [from Section 2] | [from Section 3] | [from Section 2] | [cite section] | Yes/No |
| E-02 | [from Section 2] | [from Section 3] | [from Section 2] | [cite section] | Yes/No |

All rows must show "Yes." A "No" row means the program has an open feed-forward gap.

**What we thought:** [hypothesis verbatim from Section 1]
**What we actually learned:** [confirm, refine, or refute — must differ. Answer the research
question.]

Cross-namespace note: [Name downstream Signal artifact and what finding it receives. Not
generic.]

---

### Section 6 — Principles

| Label | Principle | Source finding |
|-------|-----------|----------------|
| P-01 | [When X, do Y / Always Z] | [F-NN] |
| P-02 | [imperative or conditional] | [F-NN] |

Minimum 2 principles. No generic truisms.

---

### Artifact

Write: `simulations/prove/research/{{topic}}-research-{{date}}.md`

Frontmatter: skill: prove-program | topic | date | hypothesis | experiment_count |
             findings_count | principles_count | contracts_met: true/false
```

---

## V-03 — Phrasing Register axis (telegraphic minimal)

**Variation axis:** Phrasing register — telegraphic / minimal
**Hypothesis:** Telegraphic imperatives with an explicit output document structure specification produces full rubric compliance at ~50% of the word count of role-sequence variants, because compliance is enforced by the section order requirement at the tail, not by instructional prose.

---

```
Research program: **{{topic}}**
Research question: {{research_question}}

Complete each item in order. Do not skip forward.

---

**1. Hypothesis**

Write one sentence: what you believe is true.
Write one sentence: what evidence would prove you wrong.

---

**2. Plan** (complete before running any experiment)

List ≥2 experiments. For each, one line each:
- Type (websearch / intelligence / analysis / interview / prototype / custom)
- Question it answers
- Why this type, not another
- What it hands off to the next step

Mark at least one experiment "(*)" — one that prove-topic (single Signal topic, sequential
prove run) could not execute.

---

**3. Experiments**

Run in plan order.

Before each: write "Input: [prior output or hypothesis — quote the relevant content]"
After each: write "E-NN output: [labeled finding]" and "Feeds to: [next experiment or
Findings]"

---

**4. Findings**

Each finding on one row: finding text | source (E-NN) | confidence (high/medium/low) |
one-sentence basis

At least 2 findings with different confidence levels.

---

**5. Synthesis**

Line 1 — What you thought: [hypothesis verbatim from item 1]
Line 2 — What you learned: [confirm, refine, or refute — answer the research question, do not
copy hypothesis]
Line 3 — Downstream: [name the Signal artifact this should update and what it receives]

---

**6. Principles**

At least 2. Each as: "P-NN: When X, do Y" or "P-NN: Always Z." No generic advice.

---

**Output document**

Write to: `simulations/prove/research/{{topic}}-research-{{date}}.md`

Document must contain these labeled sections in order:
1. Hypothesis (with falsification)
2. Experiment Plan (≥2 typed experiments with rationale)
3. Experiment Results (each with labeled output and downstream routing)
4. Findings (with confidence annotations)
5. Synthesis (what-we-thought / what-we-learned / downstream note)
6. Principles (labeled P-NN, imperative or conditional)

Frontmatter: skill: prove-program | topic | date | hypothesis | experiment_count |
             principles_count
```

---

## V-04 — Combined: Output Format + Inertia Framing

**Variation axes:** Output format (table-first) + inertia framing
**Hypothesis:** Combining table-first format with inertia gap bookending — without role sequence — achieves C-11 + C-12 + C-13 simultaneously and produces the most scannable artifact for cross-namespace consumers, because every compliance point is visible in a named table cell or field rather than buried in prose.

---

```
You are running a research program for: **{{topic}}**

Research question: {{research_question}}

---

### Inertia Declaration

prove-topic executes intelligence, analysis, interview, and synthesis on a **single Signal
topic** in sequence. Before planning, name what this question requires that prove-topic cannot
provide.

Inertia gap: [cross-namespace / external domain / custom experiment / multi-hypothesis —
specify, one sentence]

If prove-topic is sufficient, stop and run that instead.

GATE: Inertia gap required before any section below.

---

### Section 1 — Hypothesis

Hypothesis: [what you believe is true — one sentence, positive form]
Falsification: [what evidence would refute this hypothesis]

GATE: Section 1 required before Section 2.

---

### Section 2 — Experiment Plan + Gap Contract Table

Produce this table before running any experiment. "Output label," "Consumed by," and "Closes
gap?" are a binding contract.

| # | Type | Question | Rationale | Output label | Consumed by | Closes gap? |
|---|------|----------|-----------|-------------|-------------|-------------|
| E-01 | | | | | | Yes / No |
| E-02 | | | | | | Yes / No |

Rules:
- ≥2 distinct types (websearch, intelligence, analysis, interview, prototype, custom)
- ≥1 row "Closes gap? = Yes" — must directly address the inertia gap declared above
- "Consumed by" values are commitments Section 3 must honor

GATE: Contract table with ≥1 gap-closing experiment required before Section 3.

---

### Section 3 — Experiment Execution

Run in Section 2 order. Each block:

**E-NN — [Type]**
Input: [prior output label — quote specific content. E-01: hypothesis + plan summary.]
Adjustment: [one sentence — how prior input scopes this experiment]
[Execute]
E-NN output ([label from contract]): [finding]
→ Consumed by: [experiment label or section, per contract table]

[Add E-03+ as needed. "Input:" citation and "→ Consumed by:" required for each block.]

---

### Section 4 — Findings

| # | Finding | Source | Confidence | Evidence basis |
|---|---------|--------|------------|----------------|
| F-01 | | E-01 | high/med/low | |
| F-02 | | E-02 | high/med/low | |

≥2 findings, distinct confidence annotations.

---

### Section 5 — Synthesis

**Feed-forward audit** — verify every Section 2 contract:

| Experiment | Output (planned) | Output (delivered) | Consumed by (planned) | Consumed by (actual) | Met? |
|-----------|-----------------|-------------------|----------------------|----------------------|------|
| E-01 | | | | | Yes/No |
| E-02 | | | | | Yes/No |

All rows must show "Yes."

**What we thought:** [hypothesis verbatim from Section 1]
**What we actually learned:** [confirm, refine, or refute — must differ. Answer the research
question.]

**Inertia gap closure:** Did the gap-closing experiment produce findings prove-topic could not
have produced? Yes or No — one sentence of evidence.

Cross-namespace note: [Name downstream Signal artifact and what finding it receives.]

---

### Section 6 — Principles

| Label | Principle | Source finding |
|-------|-----------|----------------|
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
  experiment_count: N
  findings_count: N
  principles_count: N
```

---

## V-05 — Combined: Role Sequence + Ledger + Inertia Gap (max aspirational)

**Variation axes:** Role sequence + feed-forward contract ledger + inertia gap bookending
**Hypothesis:** The only combination that reliably targets all five aspirational criteria (C-09 through C-13) simultaneously is role sequence + contract table + per-experiment COMPLETE markers + inertia gap bookend, because each structural layer closes a distinct failure mode the others leave open: roles prevent phase bleed, the contract table makes C-11 auditable, COMPLETE markers make C-12 traceable at block level, and the inertia bookend makes C-13 a closed proof rather than an instruction.

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
| PLANNER | Hypothesis, falsification, experiment plan, feed-forward contract table | Experiment results, findings, synthesis, principles |
| EXPERIMENTER | Experiment execution (one block at a time, each reading prior outputs) | New plan items, synthesis, hypothesis revisions |
| SYNTHESIZER | Feed-forward audit table, findings, synthesis, inertia gap closure verdict, principles | New experiments, retroactive hypothesis changes |

---

### PLANNER

**Phase 1 — Hypothesis**

Hypothesis: [what you believe is true — one sentence, positive form]
Falsification: [what evidence would cause you to reject this hypothesis]

GATE: Hypothesis and falsification required before Phase 2.

**Phase 2 — Experiment Plan + Feed-Forward Contract Table**

Produce this table before any experiment runs. It is the binding contract EXPERIMENTER must
execute and SYNTHESIZER must audit.

| # | Type | Question | Rationale | Output label | Consumed by | Closes inertia gap? |
|---|------|----------|-----------|-------------|-------------|---------------------|
| E-01 | | | | | | Yes / No |
| E-02 | | | | | | Yes / No |

Rules:
- ≥2 distinct types (websearch, intelligence, analysis, interview, prototype, custom)
- ≥1 row "Closes inertia gap? = Yes" — directly addresses the declared gap
- "Consumed by" values are commitments EXPERIMENTER must honor

**PLANNER COMPLETE**
Hypothesis (verbatim): [text]
Falsification (verbatim): [text]
Inertia gap addressed by: E-NN — [type]
Contract table: [N experiments, types in execution order]
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
→ Consumed by: [experiment label or role — must match "Consumed by" in contract table]

---

**E-02 — [Type]**
Entry input: E-01 — "[quote the specific finding content from E-01 that scopes this experiment
— not 'see above']"
Scope adjustment: [one sentence — how E-01's output changes this experiment's focus]
[Execute]
E-02 output ([label from contract]): [labeled finding]

**E-02 COMPLETE**
Produced: [one-line output summary]
→ Consumed by: [SYNTHESIZER — must match contract table]

---

[Add E-03+ as needed. Entry input citation and COMPLETE record required for each block.]

**EXPERIMENTER COMPLETE**
All outputs delivered: E-01 ([type]), E-02 ([type]), ...
Contract delivery check: all "Consumed by" values honored? [Yes — list any gaps]
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

All rows must show "Yes." A "No" row means an open feed-forward gap.

**Findings**

| # | Finding | Source | Confidence | Evidence basis |
|---|---------|--------|------------|----------------|
| F-01 | | E-01 | high/med/low | |
| F-02 | | E-02 | high/med/low | |

≥2 findings with distinct confidence levels.

**Synthesis**

What we thought: [hypothesis verbatim from PLANNER Phase 1]
What we actually learned: [confirm, refine, or refute — must differ from hypothesis. Answer the
research question directly.]

**Inertia gap closure:** Did the gap-closing experiment (E-NN per contract) produce findings
prove-topic could not have produced? Yes or No — one sentence of evidence.

Cross-namespace note: [Name the downstream Signal artifact and what finding it receives —
draft spec, scout brief, flow diagram, topic plan, topic story. Substantive, not generic.]

**Principles**

P-01: [When X, do Y / Always Z — specific, actionable]
P-02: [...]

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

## Rubric coverage summary (v2 rubric — 115 points)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 hypothesis-first | Hypothesis gate before plan | Section 1 gate | "Complete in order" | Section 1 gate | PLANNER Phase 1 gate |
| C-02 plan ≥2 types + rationale | Plan section w/ gap marker | Section 2 contract table | Step 2 list + why | Section 2 contract table | PLANNER Phase 2 contract |
| C-03 feed-forward | `→ Consumed by:` per block | Input citation + audit table | `Feeds to:` per block | `→ Consumed by:` + audit | Entry citation + COMPLETE + audit |
| C-04 thought vs learned | Synthesis two-field | Section 5 two-field | Line 1/Line 2 | Section 5 two-field | Synthesis two-field |
| C-05 Qx.md format | Named sections + path | 6 sections + path | Explicit section list + path | 6 sections + path | Role blocks + path |
| C-06 principles ≥2 | P-NN imperative | Section 6 table + basis | P-NN per-line | Section 6 table | P-NN in SYNTHESIZER |
| C-07 confidence per finding | Distinct annotations | Section 4 confidence column | Different levels | Section 4 confidence column | Findings table confidence |
| C-08 beyond prove-topic | Gap-closing experiment marked | `(*)` in Scope note | `(*)` marker | Closes gap? column | Closes gap? + inertia gate |
| C-09 falsification | Falsification field | Section 1 field | Step 1 sentence 2 | Section 1 field | PLANNER Phase 1 field |
| C-10 cross-namespace | Cross-namespace note | Section 5 note | Step 5 Line 3 | Section 5 note | SYNTHESIZER note |
| **C-11** feed-forward ledger | **No** | **Yes** — audit table | **No** | **Yes** — audit table | **Yes** — audit table |
| **C-12** per-exp COMPLETE + consumed-by | Partial (`→ Consumed by:` but no COMPLETE marker) | Partial (`Contract delivery:` inline) | Partial (`Feeds to:`) | Partial (`→ Consumed by:`) | **Yes** — E-NN COMPLETE + routing |
| **C-13** inertia gap bookend | **Yes** — declare + mark + close | **No** | **No** | **Yes** — declare + mark + close | **Yes** — Pre-Program + contract + verdict |
| **Est. aspirational pts** | **17** | **17** | **10** | **22** | **25** |

**Key distinctions from R1:**
- V-01 isolates C-13 without role sequence — tests whether the bookend can stand alone
- V-02 introduces the double-ledger (contract declared before execution, audited after) — strongest C-11 signal
- V-03 fixes R1 V-04's C-05 gap via explicit output-document section list at tail
- V-04 is the first combination without role sequence to target both C-11 and C-13
- V-05 is the first variation designed to score all 25 aspirational points
ction 3 "Input:" citation + Section 5 audit table | "Feeds to:" per experiment | Section 3 "→ Consumed by:" + Section 5 audit | Entry input citation + COMPLETE routing + audit table |
| C-04 thought vs learned | Synthesis two-field | Section 5 two-field | "Line 1 / Line 2" synthesis | Section 5 two-field | Synthesis two-field |
| C-05 Qx.md format | Named sections + artifact path | 6 labeled sections + artifact path | Explicit output document section list | 6 labeled sections + artifact path | PLANNER + EXPERIMENTER + SYNTHESIZER blocks + artifact path |
| C-06 labeled principles ≥2 | P-NN, imperative/conditional | Section 6 table with Basis column | P-NN per-line format | Section 6 table | P-01 / P-02 in SYNTHESIZER |
| C-07 confidence per finding | "distinct confidence annotations" | Section 4 table confidence column | "different confidence levels" | Section 4 table confidence column | Findings table confidence column |
| C-08 flexibility beyond prove-topic | Gap-closing experiment marked in plan | "(*)" row in contract table | "(*)" marker | "Closes gap? = Yes" in contract | "Closes inertia gap? = Yes" in contract |
| C-09 falsification | Falsification field in Hypothesis | Section 1 Falsification field | Step 1 second sentence | Section 1 Falsification field | PLANNER Phase 1 Falsification field |
| C-10 cross-namespace artifact | Cross-namespace note with "substantive connection" | Section 5 cross-namespace note | Step 5 Line 3 downstream | Section 5 cross-namespace note | SYNTHESIZER cross-namespace note |
| C-11 feed-forward ledger | No standalone ledger | Section 5 audit table (contracted vs delivered vs actual) | No | Section 5 audit table | Feed-Forward Audit Table in SYNTHESIZER |
| C-12 per-experiment COMPLETE + consumed-by | "→ Consumed by:" per block (partial: no COMPLETE marker) | "Contract delivery:" per block (partial: inline, not formal COMPLETE) | "Feeds to:" per block (partial) | "→ Consumed by:" per block (partial) | E-NN COMPLETE with "→ Consumed by:" — full |
| C-13 inertia gap bookend | Full: declare + mark (plan) + close (synthesis) | No | No | Full: declare + mark + close | Full: Pre-Program + contract mark + SYNTHESIZER verdict |

**Aspirational coverage per variation:**

| | C-09 | C-10 | C-11 | C-12 | C-13 | Est. aspirational pts |
|---|---|---|---|---|---|---|
| V-01 | Yes | Yes | No | Partial | Yes | 15–17 |
| V-02 | Yes | Yes | Yes | Partial | No | 15–17 |
| V-03 | Yes | Yes | No | Partial | No | 10–12 |
| V-04 | Yes | Yes | Yes | Partial | Yes | 20–22 |
| V-05 | Yes | Yes | Yes | Yes | Yes | 25 |
