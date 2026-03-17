---
skill: quest-variate
skill_target: prove-program
date: 2026-03-15
round: 1
rubric: prove-program-rubric-2026-03-15.md
status: DRAFT
---

# prove-program — Variations R1 (V-01 through V-05)

**Single-axis variations:** V-01 (role sequence), V-02 (output format), V-03 (lifecycle emphasis), V-04 (phrasing register)
**Combined variation:** V-05 (role sequence + inertia framing)

---

## V-01 — Role Sequence axis

**Variation axis:** Role sequence
**Hypothesis:** Naming and bounding three sequential roles (PLANNER → EXPERIMENTER → SYNTHESIZER) with hard-modal forbidden clauses and COMPLETE handoff markers produces stronger feed-forward and cleaner hypothesis-to-synthesis traceability than an undifferentiated agent prompt.

---

You are running a research program for: **{{topic}}**

Research question: {{research_question}}

---

### Role Sequence

Three roles execute in strict order. No role may begin before the preceding role completes.

| Role | Writes | Forbidden |
|------|--------|-----------|
| PLANNER | Hypothesis, falsification criteria, experiment plan | Any experiment execution, findings, synthesis |
| EXPERIMENTER | Experiment execution (one at a time, reading prior outputs) | Planning new experiments, writing synthesis |
| SYNTHESIZER | Findings, synthesis, principles | Re-running experiments, introducing new hypotheses |

---

### PLANNER

**Phase 1 — Hypothesis**

State the specific belief the research program will test. Write in positive form: what you believe is true. This hypothesis MUST precede all experiments.

Hypothesis: [one sentence — what you believe is true]

State falsification criteria: what evidence would cause you to reject this hypothesis?

Falsification: [what would prove you wrong]

GATE: Hypothesis and falsification criteria REQUIRED before Phase 2.

**Phase 2 — Experiment Plan**

Select ≥2 distinct experiment types from: websearch, intelligence, analysis, interview, prototype, custom. For each, state:

- Experiment type
- What question it answers
- Why this type was chosen (not a different one)
- What output it produces for downstream experiments

At least one experiment type MUST represent a scope that prove-topic could not handle — cross-namespace lookup, external domain search, custom data analysis, or multi-namespace synthesis.

GATE: Plan with ≥2 typed experiments and rationale REQUIRED before PLANNER COMPLETE.

**PLANNER COMPLETE**
Record: hypothesis (verbatim) | falsification criteria | experiment plan summary (types in execution order)
→ EXPERIMENTER receives: hypothesis, falsification criteria, ordered experiment plan.

---

### EXPERIMENTER

REQUIRED: Confirm PLANNER COMPLETE marker present before executing Experiment 1.

Execute experiments in the order declared in the plan. Before each experiment, state which prior output you are reading and how it informs this experiment's scope or focus.

**Experiment 1 — [Type from plan]**

Entry input: PLANNER hypothesis + plan
[Execute the experiment. Draw on the hypothesis and falsification criteria.]
E-01 output: [labeled finding]

---

**Experiment 2 — [Type from plan]**

Entry input: E-01 — [cite specific finding by content, not "see above"]
[How does E-01's output change or focus this experiment?]
[Execute the experiment.]
E-02 output: [labeled finding]

---

[Add Experiment 3+ if plan requires. Each block MUST have an explicit entry input citation.]

**EXPERIMENTER COMPLETE**
Record: [Experiment label → type → output produced] for each experiment.
→ SYNTHESIZER receives: all labeled experiment outputs.

---

### SYNTHESIZER

REQUIRED: Confirm EXPERIMENTER COMPLETE marker present before executing.

**Phase 3 — Findings**

For each major finding, state:
- Finding text
- Source experiment (which E-NN)
- Confidence: high / medium / low — [brief qualifier, e.g., "based on 2 consistent sources" or "single source, not replicated"]

Minimum 2 findings with distinct confidence annotations.

**Phase 4 — Synthesis**

What we thought (hypothesis restatement): [verbatim from PLANNER Phase 1]
What we actually learned: [answer the research question based on experiment outputs — confirm, refine, or refute the hypothesis. Do not repeat the hypothesis verbatim.]

**Phase 5 — Principles**

Extract ≥2 reusable, actionable principles from the findings. Label P-01, P-02, ... State each in imperative or conditional form ("When X, do Y" or "Always Z"). No generic truisms.

Cross-namespace note: If any finding should flow to a downstream Signal artifact (draft spec, scout brief, topic plan), name the artifact explicitly.

---

### Artifact

Write: `simulations/prove/research/{{topic}}-research-{{date}}.md`

Frontmatter: `skill: prove-program | topic: {{topic}} | date: {{date}} | hypothesis: [one line] | experiment_count: [N] | principles_count: [N]`

---

---

## V-02 — Output Format axis

**Variation axis:** Output format (table-first)
**Hypothesis:** Structuring every major section as a table — experiment plan, feed-forward ledger, findings with confidence column, synthesis table — makes rubric compliance easier to verify by inspection and forces explicit feed-forward entries that prose-heavy variants often omit.

---

You are running a research program for: **{{topic}}**

Research question: {{research_question}}

Read all sections before filling in any. Complete in order written. Do not skip forward.

---

### Section 1 — Hypothesis

State a specific, testable belief in positive form. This section MUST appear before Section 2.

Hypothesis: [one sentence — what you believe is true]
Falsification: [what evidence would refute this hypothesis]

GATE: Section 1 REQUIRED before Section 2.

---

### Section 2 — Experiment Plan

Produce this table before executing any experiment.

| # | Experiment type | Question answered | Why this type | Output label for downstream |
|---|----------------|------------------|---------------|-----------------------------|
| E-01 | [type] | [question] | [rationale] | [what downstream receives] |
| E-02 | [type] | [question] | [rationale] | [what downstream receives] |
| ... | | | | |

Rules:
- Select ≥2 distinct experiment types (websearch, intelligence, analysis, interview, prototype, custom).
- At least one row MUST represent a scope that prove-topic could not handle (cross-namespace, external domain, custom experiment, or multi-namespace span). Mark that row with an asterisk (*).
- The "Output label" column locks the feed-forward contract for Section 3.

GATE: Plan table REQUIRED before Section 3.

---

### Section 3 — Experiment Execution

Execute experiments in the order listed in Section 2. Complete each block before starting the next.

#### E-01 — [Experiment Type]

Input from prior: PLANNER (hypothesis + plan from Sections 1 and 2)
[Execute experiment.]
E-01 output: [labeled finding — used by: E-02, Section 4]

---

#### E-02 — [Experiment Type]

Input from prior: E-01 — [quote the specific finding text from E-01 that constrains this experiment's scope]
[How does E-01's output change or focus this experiment? One sentence before executing.]
[Execute experiment.]
E-02 output: [labeled finding — used by: Section 4]

---

[Add E-03+ as needed. Every block MUST have an explicit "Input from prior" citation with content, not just "see above".]

---

### Section 4 — Findings

| # | Finding | Source experiment | Confidence | Evidence qualifier |
|---|---------|-----------------|------------|--------------------|
| F-01 | [finding text] | E-01 | high / medium / low | [basis: e.g., "2 consistent sources", "single source", "inconclusive"] |
| F-02 | [finding text] | E-02 | high / medium / low | [basis] |

Minimum 2 findings. Each MUST have a distinct confidence annotation. Identical confidence across all rows does not pass.

---

### Section 5 — Synthesis

**Feed-forward ledger** — verify all plan outputs were consumed:

| Experiment | Output produced | Consumed by |
|-----------|-----------------|-------------|
| E-01 | [output label from Section 2] | [E-02 / Section 4 / Section 5] |
| E-02 | [output label from Section 2] | [Section 4 / Section 5] |

**What we thought:** [hypothesis verbatim from Section 1]
**What we actually learned:** [confirm, refine, or refute — must differ from hypothesis text. Answer the research question.]

Cross-namespace note: [If any finding should flow to a named downstream Signal artifact (draft spec, scout brief, topic plan), state it here.]

---

### Section 6 — Principles

| Label | Principle | Basis finding |
|-------|-----------|--------------|
| P-01 | [imperative or conditional rule: "When X, do Y" or "Always Z"] | [F-NN] |
| P-02 | [imperative or conditional rule] | [F-NN] |

Minimum 2 principles. Generic truisms do not pass.

---

### Artifact

Write: `simulations/prove/research/{{topic}}-research-{{date}}.md`

Frontmatter: `skill: prove-program | topic | date | hypothesis | experiment_count | findings_count | principles_count`

---

---

## V-03 — Lifecycle Emphasis axis

**Variation axis:** Lifecycle emphasis
**Hypothesis:** Requiring an entry contract and a COMPLETE record at every phase boundary — not just at container transitions — prevents phases from bleeding into each other and makes feed-forward obligations independently verifiable by scanning rather than by reading prose.

---

You are running a research program for: **{{topic}}**

Research question: {{research_question}}

Every phase has an entry contract and a COMPLETE record. Do not begin a phase until its entry contract is satisfied. Do not leave a phase without writing its COMPLETE record.

---

### PHASE 1: HYPOTHESIS
**Entry contract:** Nothing precedes this phase. It executes first.

State the specific belief you are testing. Must appear before any experiment is named or planned.

Hypothesis: [what you believe is true — one sentence, positive form]
Falsification: [what evidence would cause you to reject this hypothesis]

**PHASE 1 COMPLETE**
Hypothesis locked: [verbatim]
Falsification locked: [verbatim]

---

### PHASE 2: EXPERIMENT PLAN
**Entry contract:** PHASE 1 COMPLETE marker present. Hypothesis locked.

Select ≥2 distinct experiment types (websearch, intelligence, analysis, interview, prototype, custom). For each, state type, the question it answers, rationale for this type over alternatives, and the output label it produces for downstream phases.

Explicitly name at least one experiment scope that prove-topic — which operates on a single Signal topic — could not execute: cross-namespace lookup, external domain search, custom data analysis, or multi-namespace synthesis.

**PHASE 2 COMPLETE**
Experiment plan locked: [list types in execution order]
Flexibility marker: [name the experiment that exceeds prove-topic scope, and why]

---

### PHASE 3: EXPERIMENT EXECUTION
**Entry contract:** PHASE 2 COMPLETE marker present. Experiment plan locked.

Execute in plan order. Each experiment block must:
1. State entry inputs explicitly — which prior phase or experiment output is consumed, and how it scopes or focuses this experiment.
2. Execute the experiment.
3. Record its output with a label.

#### EXPERIMENT 1 — [Type]
**Entry contract:** PHASE 2 COMPLETE present.
Entry input: PHASE 1 hypothesis + PHASE 2 plan
[Execute]
E-01 output: [labeled finding]

**EXPERIMENT 1 COMPLETE**
Produced: E-01 — [one-line summary]
→ Consumed by: [EXPERIMENT 2 / PHASE 4]

---

#### EXPERIMENT 2 — [Type]
**Entry contract:** EXPERIMENT 1 COMPLETE marker present.
Entry input: E-01 — [cite specific content from E-01 output, not "see above"]
[How does E-01 constrain or focus this experiment? One sentence.]
[Execute]
E-02 output: [labeled finding]

**EXPERIMENT 2 COMPLETE**
Produced: E-02 — [one-line summary]
→ Consumed by: [PHASE 4]

---

[Add EXPERIMENT 3+ as needed. Entry contract and COMPLETE record REQUIRED for each.]

**PHASE 3 COMPLETE**
All experiments executed. Outputs: [E-01 type, E-02 type, ...]

---

### PHASE 4: FINDINGS
**Entry contract:** PHASE 3 COMPLETE marker present. All experiment outputs labeled.

State each major finding. For each: finding text, source experiment, confidence level (high / medium / low + brief qualifier).

Minimum 2 findings with distinct confidence annotations.

**PHASE 4 COMPLETE**
Findings locked: [count] findings. Confidence annotations present: yes.

---

### PHASE 5: SYNTHESIS
**Entry contract:** PHASE 4 COMPLETE marker present.

What we thought: [hypothesis verbatim from PHASE 1]
What we actually learned: [confirm, refine, or refute — must differ from hypothesis text. Answer the research question.]

Cross-namespace note: Does any finding cross namespace boundaries or require a downstream Signal artifact update? Name the artifact explicitly.

**PHASE 5 COMPLETE**

---

### PHASE 6: PRINCIPLES
**Entry contract:** PHASE 5 COMPLETE marker present.

Extract ≥2 principles from the findings. Label P-01, P-02, ... State each in imperative or conditional form ("When X, do Y" or "Always Z"). No generic truisms.

**PHASE 6 COMPLETE**
Principles locked: [count]

---

### Artifact

Write: `simulations/prove/research/{{topic}}-research-{{date}}.md`

Frontmatter: `skill: prove-program | topic | date | hypothesis | experiment_types | findings_count | principles_count`

---

---

## V-04 — Phrasing Register axis

**Variation axis:** Phrasing register (conversational/imperative)
**Hypothesis:** Replacing formal entry-contract / COMPLETE-marker language with short, direct numbered steps and plain imperatives reduces cognitive overhead without losing structural compliance — producing equally valid feed-forward and synthesis at lower prompt word count.

---

You are running a research program on: **{{topic}}**

Research question: {{research_question}}

Work through these steps in order. Don't skip ahead.

---

**Step 1 — State your hypothesis**

What do you believe is true about this research question? Write one clear sentence before you think about how to test it.

Hypothesis: [your claim — positive form, one sentence]

Now write: what would change your mind? Give a specific piece of evidence that would refute this hypothesis.

Falsification: [what would prove you wrong]

Don't proceed until you've written both.

---

**Step 2 — Plan your experiments**

Choose at least two experiment types. Good options: websearch, intelligence review, data analysis, expert interview, prototype, custom. For each one, write:
- Type
- What specific question does it answer?
- Why this type, not a different one?
- What does it hand off to the next experiment?

Make at least one experiment cross-namespace or external-scope — something a single-topic prove run couldn't do. Note which one that is.

Write the plan as a numbered list. You'll execute in this order.

---

**Step 3 — Run experiment 1**

Before you start, write: "Starting from: [hypothesis text + plan summary]"

Run it. Write what you found. Label the output: "E-01 output: [finding]"

---

**Step 4 — Run experiment 2 (and any others)**

Before you start each new experiment, write: "Reading E-[prior N] output — [quote the specific finding that matters here]"

Say in one sentence how that prior finding changes what you're looking for. Then run the experiment.

Label each output: "E-02 output: [finding]", "E-03 output: [finding]", etc.

Keep going until all planned experiments are done.

---

**Step 5 — State your findings**

List each major finding. For each one, say:
- What you found
- Which experiment it came from (E-NN)
- How confident you are: high / medium / low — and one sentence saying why (e.g., "two independent sources agree" or "single source, not cross-checked")

Give at least 2 findings with different confidence levels.

---

**Step 6 — Write your synthesis**

Two parts, in this order:

What you thought before: [paste your hypothesis from Step 1 — verbatim]

What you actually learned: [answer the research question based on what the experiments showed — confirm, refine, or refute your hypothesis. Don't just copy it.]

If any finding should update a Signal artifact outside the prove namespace (a draft spec, a scout brief, a topic plan), name it here.

---

**Step 7 — Extract principles**

Pull out at least 2 principles from what you learned. Label them P-01, P-02, etc. Write each as a rule: "When X, do Y" or "Always Z." Don't write generic advice.

---

Write the result to: `simulations/prove/research/{{topic}}-research-{{date}}.md`

Include frontmatter: `skill: prove-program | topic | date | hypothesis | experiment_count | principles_count`

---

---

## V-05 — Combined: Role Sequence + Inertia Framing

**Variation axes:** Role sequence + inertia framing
**Hypothesis:** Combining explicit role boundaries (PLANNER → EXPERIMENTER → SYNTHESIZER) with a required inertia-gap declaration forces the researcher to articulate why prove-program was the right tool before executing any role — and produces an explicit "inertia gap closure" finding that validates prove-program's differentiation claim.

---

You are running a research program for: **{{topic}}**

Research question: {{research_question}}

---

### Inertia Competitor Declaration

The inertia competitor for prove-program is **prove-topic**: a single-topic, sequential prove campaign that runs intelligence, analysis, interview, and synthesis experiments on one Signal topic. Any research question that a prove-topic run could fully answer does not require prove-program.

Before any role executes, state why this research question requires prove-program. Name at least one characteristic of the question that falls outside prove-topic's capability: cross-namespace scope, external domain, multi-hypothesis structure, or custom experiment type.

Inertia gap: [one sentence — what prove-topic cannot do here]

GATE: Inertia gap REQUIRED before any role executes. If prove-topic is sufficient, stop and use it instead.

---

### Role Declarations

| Role | Writes | May not |
|------|--------|---------|
| PLANNER | Hypothesis, falsification criteria, experiment plan | Run any experiment, write findings or synthesis |
| EXPERIMENTER | Experiment execution in sequence, each reading prior outputs | Change the plan, write synthesis, introduce new hypotheses |
| SYNTHESIZER | Findings, synthesis, inertia gap closure, principles | Re-run experiments, retroactively change hypothesis |

---

### PLANNER

**Phase 1 — Hypothesis**

State a specific, testable belief. Must appear before any experiment is named.

Hypothesis: [positive claim — what you believe is true]
Falsification: [what evidence would refute this]

GATE: Hypothesis and falsification REQUIRED before Phase 2.

**Phase 2 — Experiment Plan**

Select ≥2 distinct experiment types (websearch, intelligence, analysis, interview, prototype, custom). For each:
- Type
- Question it answers
- Why this type (not a different one)
- Output label for downstream consumption

At least one experiment MUST directly address the inertia gap declared above — an experiment type or scope that prove-topic could not handle. Mark it.

**PLANNER COMPLETE**
Hypothesis (verbatim): [text]
Inertia gap addressed by: [experiment label + type]
Plan order: [E-01 type → E-02 type → ...]
→ EXPERIMENTER receives: hypothesis, falsification criteria, ordered experiment plan.

---

### EXPERIMENTER

REQUIRED: Confirm PLANNER COMPLETE before executing.

For each experiment, state the entry input explicitly — which prior output you are reading and what specific content informs this experiment's scope.

**E-01 — [Type]**

Entry input: PLANNER hypothesis + plan
[Execute]
E-01 output: [labeled finding]
→ Consumed by: [E-02 / SYNTHESIZER]

---

**E-02 — [Type]**

Entry input: E-01 — [cite specific finding content from E-01, not "see above"]
[One sentence: how E-01 constrains or focuses this experiment's scope.]
[Execute]
E-02 output: [labeled finding]
→ Consumed by: [SYNTHESIZER]

---

[Add E-03+ as needed. Explicit entry input citation REQUIRED for each.]

**EXPERIMENTER COMPLETE**
All outputs: E-01 [type], E-02 [type], ...
→ SYNTHESIZER receives: all labeled experiment outputs.

---

### SYNTHESIZER

REQUIRED: Confirm EXPERIMENTER COMPLETE before executing.

**Findings**

| # | Finding | Source | Confidence | Evidence quality |
|---|---------|--------|------------|-----------------|
| F-01 | [finding text] | E-01 | high / medium / low | [qualifier] |
| F-02 | [finding text] | E-02 | high / medium / low | [qualifier] |

Minimum 2 findings with distinct confidence annotations.

**Synthesis**

What we thought: [hypothesis verbatim from PLANNER Phase 1]
What we actually learned: [confirm, refine, or refute — do not copy hypothesis verbatim. Answer the research question.]

**Inertia gap closure:** Did the experiment that addressed the inertia gap produce findings that prove-topic could not have produced? State yes or no with one sentence of evidence.

**Cross-namespace note:** Name any downstream Signal artifact that should receive these findings (draft spec, scout brief, topic plan, topic story).

**Principles**

P-01: [imperative or conditional rule — "When X, do Y" or "Always Z"]
P-02: [imperative or conditional rule]

---

### Artifact

Write: `simulations/prove/research/{{topic}}-research-{{date}}.md`

Frontmatter: `skill: prove-program | topic | date | hypothesis | inertia_gap | experiment_types | findings_count | principles_count | inertia_gap_closed: true/false`

---

---

## Rubric coverage summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 hypothesis-first | PLANNER Phase 1 gate | Section 1 gate | PHASE 1 gate | Step 1 "don't proceed" | PLANNER Phase 1 gate |
| C-02 plan ≥2 types + rationale | Phase 2 table + rationale | Section 2 table | PHASE 2 with type+rationale | Step 2 list + "why this type" | PLANNER Phase 2 |
| C-03 feed-forward | Entry input citation per experiment | Section 3 "Input from prior" + ledger table | Entry contract cites prior output | Step 4 "Reading E-N — [quote]" | Entry input citation per experiment |
| C-04 thought vs learned | SYNTHESIZER Phase 4 | Section 5 two-field | PHASE 5 two-field | Step 6 two-part | Synthesis two-field |
| C-05 Qx.md format at path | Artifact instruction | Artifact instruction | Artifact instruction | Artifact instruction | Artifact instruction |
| C-06 labeled principles ≥2 | SYNTHESIZER Phase 5 | Section 6 table | PHASE 6 | Step 7 | Principles block |
| C-07 confidence per finding | SYNTHESIZER Phase 3 | Section 4 table column | PHASE 4 | Step 5 per-finding | Findings table column |
| C-08 flexibility beyond prove-topic | "at least one experiment MUST" | asterisk marker in plan | "explicitly name" | "cross-namespace or external-scope" | Inertia gap declaration + gap marker |
| C-09 falsification criteria | PLANNER Phase 1 | Section 1 field | PHASE 1 field | Step 1 field | PLANNER Phase 1 |
| C-10 cross-namespace artifact | SYNTHESIZER Phase 5 note | Section 5 note | PHASE 5 note | Step 6 note | Cross-namespace note |
