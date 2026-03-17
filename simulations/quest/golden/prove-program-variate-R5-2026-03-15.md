---
skill: quest-variate
skill_target: prove-program
date: 2026-03-15
round: 5
rubric: prove-program-rubric-v5-2026-03-15.md
status: DRAFT
---

# prove-program — Variations R5 (V-01 through V-05)

**New criteria in v5 rubric**: C-20 (gate-enforced hypothesis + falsification as atomic conjunction at Phase 1→plan), C-21 (gate-enforced confidence calibration, non-uniformity required), C-22 (anti-pointer prohibition embedded locally in each consumer block's INPUT section)
**Baseline**: R4 V-05 scored ~145/145 — R5 variations target the 15-point gap (C-20 + C-21 + C-22 = 5 pts each)
**Single-axis**: V-01 (C-20 atomic conjunction gate), V-02 (C-21 calibration gate), V-03 (C-22 per-block citation contract)
**Combined**: V-04 (C-20 + C-21), V-05 (C-20 + C-21 + C-22 over R4 V-05 floor)

---

## V-01 — Lifecycle Emphasis axis (C-20: Atomic Conjunction Gate)

**Variation axis:** Lifecycle emphasis — single atomic gate at Phase 1→plan boundary enforcing hypothesis distinctness AND falsification as a boolean conjunction
**Hypothesis:** Framing the Phase 1→plan boundary as one named gate whose pass condition is "Condition A AND Condition B" — rather than a list of advisory checks — prevents the partial-satisfaction failure mode (one condition met, other silently dropped) and produces C-20 compliance as a structural property of the prompt rather than an instruction-following quality.

---

You are running a research program for: **{{topic}}**

Research question: {{research_question}}

Complete all phases in order. Do not advance past a gate until its pass condition is fully met.

---

### Phase 0 — Inertia Gap Declaration

The inertia competitor is **prove-topic**: single-topic intelligence → analysis → interview → synthesis scoped to one Signal topic. Prove-program is required only when the research question exceeds prove-topic's capability.

Inertia gap: [what prove-topic cannot handle here — cross-namespace scope, external domain, multi-hypothesis structure, or custom experiment type]

GATE-0: Inertia gap names a specific capability prove-topic lacks for this question. If prove-topic is sufficient, stop and use it.

---

### Phase 1 — Hypothesis

State a specific, testable belief. Must appear before any experiment is named or planned.

Hypothesis: [what you believe is true — one sentence, positive form]
Falsification: [what evidence would cause you to reject this hypothesis]

---

### GATE-1 — Atomic Hypothesis + Falsification Conjunction [Phase 1 → Plan Boundary]

This gate has exactly two conditions. Both must be TRUE to proceed to Phase 1B. Partial satisfaction — one TRUE, one FALSE or absent — fails the gate.

**Condition A — Hypothesis distinctness**: The hypothesis differs from the research question in specificity or framing. A restatement of the question in different words does not satisfy Condition A.

**Condition B — Falsification present**: A falsification criterion is explicitly stated — a specific piece of evidence that would cause the researcher to reject the hypothesis.

**GATE-1 evaluation** (state each):
- Condition A: TRUE / FALSE — [brief justification: in what way does the hypothesis differ from the question?]
- Condition B: TRUE / FALSE — [brief justification: what is the stated falsification criterion?]
- **GATE-1 result: PASS (A AND B = TRUE) / FAIL (A = FALSE OR B = FALSE)**

STOP: If GATE-1 result is FAIL, return to Phase 1. Rewrite the hypothesis and/or add the falsification criterion. Re-evaluate GATE-1. Do not proceed to Phase 1B until GATE-1 shows PASS.

---

### Phase 1B — Experiment Plan

**[Confirm GATE-1 PASS before producing this section.]**

| # | Type | Question answered | Rationale | Output label | Consumed by | Closes gap? |
|---|------|------------------|-----------|--------------|-------------|-------------|
| E-01 | [websearch / intelligence / analysis / interview / prototype / custom] | [question] | [why this type, not another] | [label] | [E-02 / Phase 3] | Yes / No |
| E-02 | [type] | [question] | [rationale] | [label] | [Phase 3] | Yes / No |

Rules:
- >=2 distinct types — no two rows share the same type
- >=1 row: Closes gap? = Yes (the experiment addressing Phase 0 inertia gap)
- All Output label cells filled before executing

GATE-P: Table has >=2 distinct types, >=1 Yes in Closes gap?, all Output labels filled. Do not execute until GATE-P passes.

---

### Phase 2 — Experiment Execution

**[Confirm GATE-P PASS before executing E-01.]**

Execute experiments in plan order. Each block requires: (1) explicit Input citation citing prior content, (2) execution, (3) labeled E-NN output, (4) Contract delivery line.

---

#### E-01 — [Type from Phase 1B]

Input: Phase 1 hypothesis — [verbatim hypothesis text] | Phase 0 inertia gap — [verbatim gap text]
[One sentence: how hypothesis + inertia gap scope this experiment.]
[Execute experiment.]
E-01 output: [labeled finding]
Contract delivery: output label = "[plan label]" — consumed by: [E-02 / Phase 3] — delivered? Yes / No

---

#### E-02 — [Type from Phase 1B]

Input: E-01 output — [cite the specific content of E-01's labeled finding; "see above" or pointer references do not satisfy this requirement]
[One sentence: how E-01's finding changes the scope or focus of this experiment.]
[Execute experiment.]
E-02 output: [labeled finding]
Contract delivery: output label = "[plan label]" — consumed by: [Phase 3] — delivered? Yes / No

---

[Add E-03+ as needed. Every block requires an explicit prior-content citation in the Input.]

GATE-C: All planned experiments complete. All outputs labeled. All Contract delivery lines present.

---

### Phase 3A — Feed-Forward Audit Ledger

**[Confirm GATE-C PASS.]**

| Experiment | Plan output label | Delivered? | Consumed by |
|-----------|------------------|------------|-------------|
| E-01 | [label] | Yes / No | [step] |
| E-02 | [label] | Yes / No | [step] |

Populate from Contract delivery lines. Do not infer values not stated in experiment blocks.

---

### Phase 3B — Findings

| # | Finding | Source | Confidence | Evidence basis |
|---|---------|--------|------------|---------------|
| F-01 | [finding] | E-01 | high / medium / low | [e.g., "2 independent sources", "single source not replicated"] |
| F-02 | [finding] | E-02 | high / medium / low | [basis] |

Minimum 2 findings. Confidence levels must not all be identical. Evidence basis required per row.

---

### Phase 3C — Synthesis

What we thought: [hypothesis verbatim from Phase 1]
What we actually learned: [confirm, refine, or refute — must differ from hypothesis text. Answer the research question.]

Inertia gap closure: [Did the gap-closing experiment produce a finding prove-topic could not? Yes / No + one sentence.]

Cross-namespace note: [Name any downstream Signal artifact that should receive these findings.]

GATE-D: "What we actually learned" must not be a verbatim copy of the hypothesis. Revise if it is.

---

### Phase 3D — Principles

P-01: [When X, do Y — or Always Z] — Source: F-NN
P-02: [When X, do Y — or Always Z] — Source: F-NN

Minimum 2 principles. No generic truisms.

---

### Artifact

Write: `simulations/prove/research/{{topic}}-research-{{date}}.md`

Frontmatter: `skill: prove-program | topic: {{topic}} | date: {{date}} | hypothesis: [one line] | inertia_gap: [one line] | experiment_types: [list] | findings_count: [N] | principles_count: [N] | inertia_gap_closed: true / false`

---

---

## V-02 — Lifecycle Emphasis axis (C-21: Confidence Calibration Gate)

**Variation axis:** Lifecycle emphasis — named gate at the findings→synthesis boundary enforcing confidence non-uniformity, not just presence
**Hypothesis:** Placing a dedicated GATE-CAL between findings and synthesis whose single pass condition is "at least two distinct confidence levels appear" — not "confidence levels present" — forces the researcher to differentiate evidentiary quality before drawing conclusions, closing the uniform-confidence compliance-shortcut failure mode that presence-only gates permit.

---

You are running a research program for: **{{topic}}**

Research question: {{research_question}}

Every phase boundary has a gate. Complete each gate before advancing.

---

### Phase 0 — Inertia Gap

The inertia competitor is **prove-topic**: single-topic intelligence → analysis → interview → synthesis. Prove-program is required only when this question exceeds prove-topic's capability.

Inertia gap: [what prove-topic cannot handle here]

GATE-0: Inertia gap names a specific limitation of prove-topic for this question. If prove-topic is sufficient, stop.

---

### Phase 1 — Hypothesis

Hypothesis: [what you believe is true — one sentence, positive form]
Falsification: [what evidence would refute this hypothesis]

GATE-H: (a) Hypothesis differs from research question in specificity or framing; (b) falsification criterion present. Both required before Phase 1B.

---

### Phase 1B — Experiment Plan

| # | Type | Question answered | Rationale | Output label | Consumed by | Closes gap? |
|---|------|------------------|-----------|--------------|-------------|-------------|
| E-01 | [type] | [question] | [why this type] | [label] | [E-02 / Phase 3] | Yes / No |
| E-02 | [type] | [question] | [rationale] | [label] | [Phase 3] | Yes / No |

Types: websearch, intelligence, analysis, interview, prototype, custom. >=2 distinct types. >=1 Closes gap? = Yes. All Output labels filled.

GATE-P: All plan requirements met. Do not execute until GATE-P passes.

---

### Phase 2 — Experiment Execution

Execute in plan order. Each block requires an explicit Input citation from prior content, execution, a labeled E-NN output, and a Contract delivery line.

---

#### E-01 — [Type]

Input: Phase 1 hypothesis — [verbatim] | Phase 0 gap — [verbatim]
[One sentence: how hypothesis + gap scope this experiment.]
[Execute.]
E-01 output: [labeled finding]
Contract delivery: "[plan label]" — consumed by: [E-02 / Phase 3] — delivered? Yes / No

---

#### E-02 — [Type]

Input: E-01 output — [cite specific content of E-01's labeled finding; pointer references do not satisfy this requirement]
[One sentence: how E-01's finding focuses this experiment.]
[Execute.]
E-02 output: [labeled finding]
Contract delivery: "[plan label]" — consumed by: [Phase 3] — delivered? Yes / No

---

[Add E-03+ as needed. Explicit content citation required in every Input.]

GATE-C: All experiments complete. All outputs labeled. All Contract delivery lines present.

---

### Phase 3A — Feed-Forward Audit Ledger

| Experiment | Plan output label | Delivered? | Consumed by |
|-----------|------------------|------------|-------------|
| E-01 | [label] | Yes / No | [step] |
| E-02 | [label] | Yes / No | [step] |

---

### Phase 3B — Findings

| # | Finding | Source | Confidence | Evidence basis |
|---|---------|--------|------------|---------------|
| F-01 | [finding] | E-01 | high / medium / low | [basis] |
| F-02 | [finding] | E-02 | high / medium / low | [basis] |

---

### GATE-CAL — Confidence Calibration Check [Findings → Synthesis Boundary]

This gate enforces calibration, not just presence. Confidence levels present in every row is necessary but not sufficient to pass.

**GATE-CAL pass condition**: The findings table contains at least two distinct confidence values. "high" and "high" does not pass. "high" and "medium" passes. "medium", "medium", and "low" passes. The test is on distinct values, not distinct rows.

**GATE-CAL evaluation**:
- List distinct confidence values appearing in the findings table: [e.g., "high (F-01), medium (F-02)"]
- Count of distinct values: [N]
- At least 2 distinct values? YES / NO
- **GATE-CAL result: PASS / FAIL**

FAIL: All findings carry the same confidence level. The findings table records presence but not calibration. Return to Phase 3B. Re-examine each finding's evidentiary basis independently. Assign confidence levels that reflect actual differences in evidence quality. Re-evaluate GATE-CAL.

STOP: Do not write synthesis until GATE-CAL result is PASS.

---

### Phase 3C — Synthesis

**[Confirm GATE-CAL PASS before writing synthesis.]**

What we thought: [hypothesis verbatim from Phase 1]
What we actually learned: [confirm, refine, or refute — must differ from hypothesis. Answer the research question.]

Inertia gap closure: [Did the gap-closing experiment produce a finding prove-topic could not? Yes / No + one sentence.]

Cross-namespace note: [Name downstream Signal artifact that should receive these findings.]

GATE-S: Both fields present. "What we actually learned" is not a verbatim copy of hypothesis.

---

### Phase 3D — Principles

P-01: [When X, do Y — or Always Z] — Source: F-NN
P-02: [When X, do Y — or Always Z] — Source: F-NN

Minimum 2. No generic truisms.

---

### Artifact

Write: `simulations/prove/research/{{topic}}-research-{{date}}.md`

Frontmatter: `skill: prove-program | topic: {{topic}} | date: {{date}} | hypothesis: [one line] | inertia_gap: [one line] | experiment_types: [list] | findings_count: [N] | principles_count: [N] | inertia_gap_closed: true / false`

---

---

## V-03 — Output Format axis (C-22: Per-Consumer-Block Embedded Citation Contract)

**Variation axis:** Output format — anti-pointer prohibition embedded as the opening clause of each consumer block's INPUT section, not in a global preamble
**Hypothesis:** Embedding the citation contract locally inside each consumer block's INPUT section — where the block author executes it — produces more consistent verbatim citation behavior than a global rule placed in a distant preamble, because local enforcement persists even when the global context is far away or has been processed in a prior generation window.

---

You are running a research program for: **{{topic}}**

Research question: {{research_question}}

Complete phases in order. Each phase has an entry condition. Do not skip forward.

---

### Phase 0 — Inertia Gap

The inertia competitor is **prove-topic**: single-topic intelligence → analysis → interview → synthesis on one Signal topic. Use prove-program only when this question exceeds that scope.

Inertia gap: [what prove-topic cannot handle here — cross-namespace scope, external domain, multi-hypothesis structure, or custom experiment type]

Gate: Inertia gap must name a specific limitation of prove-topic for this question. If prove-topic is sufficient, stop.

---

### Phase 1 — Hypothesis

State a specific, testable belief. Required before any experiment is named or planned.

Hypothesis: [what you believe is true — one sentence, positive form]
Falsification: [what evidence would refute this hypothesis]

Gate: (a) Hypothesis differs from research question in specificity or framing; (b) falsification criterion present. Both required before Phase 1B.

---

### Phase 1B — Experiment Plan

Produce this table before executing any experiment.

| # | Type | Question answered | Rationale | Output label | Consumed by | Closes gap? |
|---|------|------------------|-----------|--------------|-------------|-------------|
| E-01 | [websearch / intelligence / analysis / interview / prototype / custom] | [question] | [why this type, not another] | [label] | [E-02 / Phase 3] | Yes / No |
| E-02 | [type] | [question] | [rationale] | [label] | [Phase 3] | Yes / No |

Rules: >=2 distinct types; >=1 Closes gap? = Yes; all Output labels filled.

Gate: All plan requirements met before executing.

---

### Phase 2 — Experiment Execution

Execute experiments in plan order.

---

#### E-01 — [Type from Phase 1B]

**INPUT**: Phase 1 hypothesis — [verbatim hypothesis text] | Phase 0 inertia gap — [verbatim gap text]

[One sentence: how the hypothesis and inertia gap focus this experiment's scope.]

[Execute experiment.]

E-01 output: [labeled finding — this exact text will be consumed by E-02]

Contract delivery: output label = "[plan label]" — consumed by: [E-02 / Phase 3] — delivered? Yes / No

---

#### E-02 — [Type from Phase 1B]

**INPUT — citation contract (local to this block)**: This block consumes E-01 output. Reproduce the exact text of E-01's labeled finding below. Pointer references ("see above", "per E-01", "as found in E-01") are prohibited in this INPUT section. Embed the verbatim content:

> [exact text from E-01 output — directly quoted from the labeled finding, not described or paraphrased]

[One sentence: how E-01's finding changes the scope or focus of this experiment.]

[Execute experiment.]

E-02 output: [labeled finding]

Contract delivery: output label = "[plan label]" — consumed by: [Phase 3] — delivered? Yes / No

---

[For each additional consumer block (E-03, E-04, etc.), the INPUT section MUST begin with the same local citation contract clause:

**INPUT — citation contract (local to this block)**: This block consumes [prior E-NN] output. Reproduce the exact text of [prior E-NN]'s labeled finding below. Pointer references are prohibited in this INPUT section. Embed the verbatim content:

> [exact text from prior E-NN output]

The citation contract is embedded per-block. It is not delegated to the global rules above.]

Gate: All experiments complete. All outputs labeled. All Contract delivery lines present.

---

### Phase 3A — Feed-Forward Audit Ledger

| Experiment | Plan output label | Delivered? | Consumed by |
|-----------|------------------|------------|-------------|
| E-01 | [label] | Yes / No | [step] |
| E-02 | [label] | Yes / No | [step] |

Populate from Contract delivery lines. Do not infer.

---

### Phase 3B — Findings

| # | Finding | Source | Confidence | Evidence basis |
|---|---------|--------|------------|---------------|
| F-01 | [finding] | E-01 | high / medium / low | [basis] |
| F-02 | [finding] | E-02 | high / medium / low | [basis] |

Minimum 2 findings. Confidence levels must not all be identical. Evidence basis required per row.

---

### Phase 3C — Synthesis

What we thought: [hypothesis verbatim from Phase 1]
What we actually learned: [confirm, refine, or refute — must differ from hypothesis. Answer the research question.]

Inertia gap closure: [Did the gap-closing experiment produce a finding prove-topic could not? Yes / No + one sentence.]

Cross-namespace note: [Name any downstream Signal artifact that should receive these findings.]

Gate: "What we actually learned" must differ from hypothesis text. Revise if it copies the hypothesis verbatim.

---

### Phase 3D — Principles

P-01: [When X, do Y — or Always Z] — Source: F-NN
P-02: [When X, do Y — or Always Z] — Source: F-NN

Minimum 2. No generic truisms.

---

### Artifact

Write: `simulations/prove/research/{{topic}}-research-{{date}}.md`

Frontmatter: `skill: prove-program | topic: {{topic}} | date: {{date}} | hypothesis: [one line] | inertia_gap: [one line] | experiment_types: [list] | findings_count: [N] | principles_count: [N] | inertia_gap_closed: true / false`

---

---

## V-04 — Combined: C-20 + C-21 (Atomic Gate + Calibration Gate)

**Variation axes:** Lifecycle emphasis (C-20 atomic conjunction gate) + Lifecycle emphasis (C-21 confidence calibration gate)
**Hypothesis:** Pairing the atomic conjunction gate at Phase 1→plan (C-20) with the confidence calibration gate at findings→synthesis (C-21) creates symmetric quality enforcement at both ends of the research arc — ensuring input integrity before any experiment runs and output calibration before any conclusion is drawn — producing a document where both gates are structurally impossible to bypass.

---

You are running a research program for: **{{topic}}**

Research question: {{research_question}}

Two dedicated quality gates operate at symmetric positions in the lifecycle: GATE-1 (before planning) enforces hypothesis + falsification integrity as an atomic conjunction; GATE-CAL (before synthesis) enforces confidence calibration. Both must reach PASS. Standard flow gates enforce sequencing throughout.

---

### Phase 0 — Inertia Gap

The inertia competitor is **prove-topic**: single-topic intelligence → analysis → interview → synthesis. Use prove-program only when this question exceeds that scope.

Inertia gap: [what prove-topic cannot handle here — cross-namespace scope, external domain, multi-hypothesis structure, or custom experiment type]

GATE-0: Inertia gap names a specific prove-topic limitation for this question. If prove-topic is sufficient, stop.

---

### Phase 1 — Hypothesis

State a specific, testable belief. Must appear before any experiment is named.

Hypothesis: [what you believe is true — one sentence, positive form]
Falsification: [what evidence would refute this]

---

### GATE-1 — Atomic Hypothesis + Falsification Check [Phase 1 → Plan Boundary]

**This gate enforces two conditions as an atomic conjunction. Both must be TRUE. Partial satisfaction is FAIL.**

| Condition | Description | Result |
|-----------|-------------|--------|
| A — Hypothesis distinctness | Hypothesis differs from research question in specificity or framing. A restatement in different words fails. | TRUE / FALSE |
| B — Falsification present | Falsification criterion is explicitly stated: a specific piece of evidence that would cause rejection of the hypothesis. | TRUE / FALSE |

GATE-1 result: **PASS** (A = TRUE AND B = TRUE) / **FAIL** (A = FALSE OR B = FALSE)

STOP: If GATE-1 result is FAIL, return to Phase 1. Rewrite the hypothesis and/or add the falsification criterion. Re-evaluate GATE-1. Do not proceed to Phase 1B until GATE-1 shows PASS.

---

### Phase 1B — Experiment Plan

**[Confirm GATE-1 PASS before this section.]**

| # | Type | Question answered | Rationale | Output label | Consumed by | Closes gap? |
|---|------|------------------|-----------|--------------|-------------|-------------|
| E-01 | [websearch / intelligence / analysis / interview / prototype / custom] | [question] | [why this type, not another] | [label] | [E-02 / Phase 3] | Yes / No |
| E-02 | [type] | [question] | [rationale] | [label] | [Phase 3] | Yes / No |

>=2 distinct types. >=1 Closes gap? = Yes. All Output labels filled.

GATE-P: All plan requirements met. Do not execute until GATE-P passes.

---

### Phase 2 — Experiment Execution

**[Confirm GATE-P PASS before executing E-01.]**

Each block requires: explicit Input citation from prior content, execution, labeled E-NN output, Contract delivery line.

---

#### E-01 — [Type]

Input: Phase 1 hypothesis — [verbatim] | Phase 0 gap — [verbatim]
[One sentence: how hypothesis + gap scope this experiment.]
[Execute.]
E-01 output: [labeled finding]
Contract delivery: "[plan label]" — consumed by: [E-02 / Phase 3] — delivered? Yes / No

---

#### E-02 — [Type]

Input: E-01 output — [cite specific content of E-01's labeled finding; "see above" or pointer references do not satisfy this]
[One sentence: how E-01's finding changes this experiment's scope.]
[Execute.]
E-02 output: [labeled finding]
Contract delivery: "[plan label]" — consumed by: [Phase 3] — delivered? Yes / No

---

[Add E-03+ as needed. Explicit content citation required in each Input.]

GATE-C: All experiments complete. All outputs labeled. All Contract delivery lines present.

---

### Phase 3A — Feed-Forward Audit Ledger

**[Confirm GATE-C PASS.]**

| Experiment | Plan output label | Delivered? | Consumed by |
|-----------|------------------|------------|-------------|
| E-01 | [label] | Yes / No | [step] |
| E-02 | [label] | Yes / No | [step] |

---

### Phase 3B — Findings

| # | Finding | Source | Confidence | Evidence basis |
|---|---------|--------|------------|---------------|
| F-01 | [finding] | E-01 | high / medium / low | [e.g., "2 independent sources", "single source not replicated"] |
| F-02 | [finding] | E-02 | high / medium / low | [basis] |

Minimum 2 findings. Evidence basis required per row.

---

### GATE-CAL — Confidence Calibration Check [Findings → Synthesis Boundary]

**This gate enforces calibration. Presence of confidence labels is necessary but not sufficient.**

**GATE-CAL pass condition**: The findings table contains at least two distinct confidence values. All rows labeled the same level — regardless of which level — fail this gate.

**GATE-CAL evaluation**:
- Distinct confidence values in findings table: [list — e.g., "high (F-01), medium (F-02)"]
- Count of distinct values: [N]
- At least 2 distinct values? YES / NO
- **GATE-CAL result: PASS / FAIL**

FAIL: All findings carry the same confidence level. Return to Phase 3B. Re-examine each finding's evidentiary basis independently. Assign confidence levels that reflect actual differences in evidence strength. Re-evaluate GATE-CAL.

STOP: Do not write synthesis until GATE-CAL result is PASS.

---

### Phase 3C — Synthesis

**[Confirm GATE-CAL PASS before writing synthesis.]**

What we thought: [hypothesis verbatim from Phase 1]
What we actually learned: [confirm, refine, or refute — must differ from hypothesis text. Answer the research question.]

Inertia gap closure: [Did the gap-closing experiment produce a finding prove-topic could not? Yes / No + one sentence.]

Cross-namespace note: [Name downstream Signal artifact that should receive these findings.]

GATE-S: Both synthesis fields present. "What we actually learned" is not a verbatim copy of hypothesis.

---

### Phase 3D — Principles

P-01: [When X, do Y — or Always Z] — Source: F-NN
P-02: [When X, do Y — or Always Z] — Source: F-NN

Minimum 2. No generic truisms.

---

### Artifact

Write: `simulations/prove/research/{{topic}}-research-{{date}}.md`

Frontmatter: `skill: prove-program | topic: {{topic}} | date: {{date}} | hypothesis: [one line] | inertia_gap: [one line] | experiment_types: [list] | findings_count: [N] | principles_count: [N] | inertia_gap_closed: true / false`

---

---

## V-05 — Combined: C-20 + C-21 + C-22 over R4 V-05 Floor

**Variation axes:** C-20 (atomic conjunction gate) + C-21 (calibration gate) + C-22 (per-block citation contracts) layered over R4 V-05 role-sequence + verbatim blockquote + gate enforcement + inline FAIL baseline
**Hypothesis:** Layering all three R5 criteria over the R4 V-05 ceiling — which holds all prior criteria — produces the first 160/160-eligible variation because the three new criteria are structurally non-overlapping: C-20 operates at the Phase 1→plan boundary, C-21 at findings→synthesis, and C-22 per-block inside EXPERIMENTER. None interferes with the others, and none degrades existing criteria.

---

You are running a research program for: **{{topic}}**

Research question: {{research_question}}

Three roles execute in strict sequence: PLANNER → EXPERIMENTER → SYNTHESIZER. Named gate tokens enforce every phase boundary. Every enforced criterion carries an inline FAIL condition. The EXPERIMENTER verbatim input requirement operates with per-block citation contracts embedded locally in each consumer block. Two dedicated quality gates enforce input integrity (GATE-1) and output calibration (GATE-CAL).

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

---

#### GATE-1 — Atomic Hypothesis + Falsification Conjunction [Phase 1 → Plan Boundary]

**Single atomic gate. Both conditions must be TRUE. Partial satisfaction is FAIL.**

| Condition | Description | Result |
|-----------|-------------|--------|
| A — Hypothesis distinctness | Hypothesis differs from research question in specificity or framing. A restatement in different words fails. | TRUE / FALSE |
| B — Falsification present | Falsification criterion explicitly stated: specific evidence that would cause rejection of hypothesis. | TRUE / FALSE |

GATE-1 result: PASS (A AND B = TRUE) / FAIL (A = FALSE OR B = FALSE)

FAIL: Hypothesis absent, is a restatement of the question, or falsification criterion missing. Rewrite Phase 1 and re-evaluate GATE-1.
STOP: Do not proceed to Phase 1B until GATE-1 result is PASS.

---

#### Phase 1B — Experiment Plan

**[Confirm GATE-1 PASS before this section.]**

| # | Type | Question answered | Rationale | Output label | Consumed by | Closes gap? |
|---|------|------------------|-----------|--------------|-------------|-------------|
| E-01 | [websearch / intelligence / analysis / interview / prototype / custom] | [question] | [why this type, not another] | [label] | [E-02 / SYNTHESIZER] | Yes / No |
| E-02 | [type] | [question] | [rationale] | [label] | [SYNTHESIZER] | Yes / No |

Rules:
- >=2 distinct types — no two rows share the same type
- >=1 row: Closes gap? = Yes (the experiment addressing Phase 0 inertia gap)
- All Output label cells filled — these lock the per-block verbatim contract in EXPERIMENTER

GATE-P: (a) >=2 distinct types; (b) >=1 Yes in Closes gap?; (c) all Output labels filled.
FAIL: <2 rows, all rows share the same type, no Yes in Closes gap?, or any Output label blank.

**PLANNER COMPLETE**
Hypothesis locked: [verbatim]
Inertia gap addressed by: [E-NN + type]
Plan order: [E-01 type → E-02 type → ...]
→ EXPERIMENTER receives: hypothesis, falsification criterion, ordered plan, per-block citation contract requirement

---

### EXPERIMENTER

GATE-PLANNER: Confirm PLANNER COMPLETE before executing any experiment.
FAIL: Any experiment executes without PLANNER COMPLETE marker confirmed.

**Per-block verbatim citation contract — governs all EXPERIMENTER consumer blocks:**

Every experiment block that consumes a prior block's output must embed the citation contract locally in its own INPUT section. The contract is NOT satisfied by a global rule in a preamble — each consumer block's INPUT section must contain the contract clause itself. The clause format is:

> Citation contract (local to this block): reproduce the exact output text of the prior block. Pointer references ("see above", "per E-NN", "as found in E-NN", or any paraphrase) are prohibited in this INPUT section. Embed verbatim content below.

FAIL (applies to every consumer block): Input section uses a pointer reference or paraphrase, or does not contain the local citation contract clause.

---

#### E-01 — [Type from Phase 1B]

GATE-E1-entry: PLANNER COMPLETE confirmed.

INPUT: Phase 1 hypothesis — [verbatim hypothesis text] | Phase 0 inertia gap — [verbatim gap text]

[One sentence: how hypothesis + inertia gap focus this experiment's scope.]

[Execute experiment.]

E-01 output: [labeled finding — this exact text is what E-02 must embed verbatim in its INPUT section]

Contract delivery: output label = "[plan label]" — consumed by: [E-02 / SYNTHESIZER] — delivered? Yes / No
FAIL: Contract delivery absent or output label does not match Phase 1B plan.

**EXPERIMENT 1 COMPLETE**
Produced: E-01 — [one-line summary]
→ Consumed by: [E-02 / SYNTHESIZER]

---

#### E-02 — [Type from Phase 1B]

GATE-E2-entry: EXPERIMENT 1 COMPLETE confirmed before executing.
FAIL: E-02 begins without EXPERIMENT 1 COMPLETE marker present.

INPUT — citation contract (local to this block): This block consumes E-01 output. Reproduce the exact text of E-01's labeled finding below. Pointer references ("see above", "per E-01", "as found in E-01") are prohibited in this INPUT section. Embed verbatim content:

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

[Add E-03+ as needed. Every consumer block requires:
1. GATE-E{N}-entry confirmation of prior COMPLETE marker
2. INPUT section containing the local citation contract clause + verbatim blockquote
3. Execution
4. Labeled E-NN output
5. Contract delivery line with delivered? boolean
6. EXPERIMENT N COMPLETE marker with consumed-by routing
The citation contract is embedded in each block's INPUT section individually — not in a shared global rule.]

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

Populate from Contract delivery lines in EXPERIMENTER. Do not infer values not stated in experiment blocks.
FAIL: Ledger absent, or any row's Delivered? value contradicts the corresponding Contract delivery line.

---

#### Findings

| # | Finding | Source | Confidence | Evidence basis |
|---|---------|--------|------------|---------------|
| F-01 | [finding text] | E-01 | high / medium / low | [e.g., "2 consistent sources", "single source not replicated"] |
| F-02 | [finding text] | E-02 | high / medium / low | [basis] |

Minimum 2 findings. Evidence basis required per row.
FAIL: Fewer than 2 findings, or evidence basis absent from any row.

---

#### GATE-CAL — Confidence Calibration Check [Findings → Synthesis Boundary]

**This gate enforces calibration. Presence of confidence labels is necessary but not sufficient.**

**GATE-CAL pass condition**: The findings table contains at least two distinct confidence values. All findings labeled the same level — regardless of label chosen — fail this gate.

**GATE-CAL evaluation**:
- Distinct confidence values in findings table: [list — e.g., "high (F-01), medium (F-02)"]
- Count of distinct values: [N]
- At least 2 distinct values? YES / NO
- **GATE-CAL result: PASS / FAIL**

FAIL: All findings carry the same confidence level. Return to Findings. Re-examine each finding's evidentiary basis independently. Differentiate confidence assignments to reflect actual evidence quality differences. Re-evaluate GATE-CAL.
STOP: Do not write synthesis until GATE-CAL result is PASS.

---

#### Synthesis

**[Confirm GATE-CAL PASS before writing synthesis.]**

What we thought: [hypothesis verbatim from PLANNER Phase 1]
What we actually learned: [confirm, refine, or refute — must differ from hypothesis text. Answer the research question.]

Inertia gap closure: [Did the experiment marked Closes gap? = Yes produce a finding prove-topic could not have produced? Yes / No + one sentence of evidence.]

Cross-namespace note: [Name any downstream Signal artifact that should receive these findings — draft spec, scout brief, topic plan, topic story.]

FAIL: "What we actually learned" copies the hypothesis verbatim, or either synthesis field is absent.
FAIL: Inertia gap closure verdict absent or states neither Yes nor No.

---

#### Principles

| Label | Principle | Source finding |
|-------|-----------|---------------|
| P-01 | [When X, do Y — or Always Z] | F-NN |
| P-02 | [When X, do Y — or Always Z] | F-NN |

Minimum 2 principles. No generic truisms. Source finding required per row.
FAIL: Fewer than 2 principles, principles are generic truisms, or source finding column blank.

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

## Rubric coverage summary (v5 — 160 pts)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 hypothesis-first | Phase 1 before experiments | Phase 1 before experiments | Phase 1 before experiments | Phase 1 before experiments | PLANNER Phase 1 before experiments |
| C-02 plan >=2 types + rationale | GATE-P table | GATE-P table | Phase 1B table + gate | GATE-P table | PLANNER Phase 1B GATE-P + FAIL |
| C-03 feed-forward | Input citation per block | Input citation per block | Per-block contract (strong) | Input citation per block | EXPERIMENTER per-block contract + FAIL |
| C-04 synthesis contrast | Phase 3C two fields | Phase 3C two fields | Phase 3C two fields | Phase 3C two fields | SYNTHESIZER two fields + FAIL |
| C-05 Qx.md format at path | Artifact section | Artifact section | Artifact section | Artifact section | Artifact section |
| C-06 principles >=2 labeled | Phase 3D | Phase 3D | Phase 3D | Phase 3D | SYNTHESIZER principles table + FAIL |
| C-07 confidence per finding | Phase 3B table | Phase 3B table | Phase 3B table | Phase 3B table | SYNTHESIZER findings table |
| C-08 flexibility beyond prove-topic | Phase 0 gap + Closes gap? | Phase 0 gap + Closes gap? | Phase 0 gap + Closes gap? | Phase 0 gap + Closes gap? | Pre-role gap + GATE-0 + Closes gap? |
| C-09 falsification | GATE-1 Condition B | GATE-H field (b) | Phase 1 field | GATE-1 Condition B | GATE-1 Condition B + FAIL |
| C-10 cross-namespace | Phase 3C note | Phase 3C note | Phase 3C note | Phase 3C note | SYNTHESIZER cross-namespace note |
| C-11 audit ledger | Phase 3A standalone table | Phase 3A standalone table | Phase 3A standalone table | Phase 3A standalone table | SYNTHESIZER ledger + FAIL |
| C-12 COMPLETE markers | No per-block COMPLETE (PARTIAL) | No per-block COMPLETE (PARTIAL) | No per-block COMPLETE (PARTIAL) | No per-block COMPLETE (PARTIAL) | EXPERIMENT N COMPLETE + consumed-by per block (PASS) |
| C-13 inertia bookending | Phase 0 + Closes gap? + Phase 3C | Phase 0 + Closes gap? + Phase 3C | Phase 0 + Closes gap? + Phase 3C | Phase 0 + Closes gap? + Phase 3C | Pre-role + PLANNER Closes gap? + SYNTHESIZER closure |
| C-14 plan output routing | Output label + Consumed by columns | Output label + Consumed by columns | Output label + Consumed by columns | Output label + Consumed by columns | PLANNER table columns |
| C-15 delivery boolean | Contract delivery per block | Contract delivery per block | Contract delivery per block | Contract delivery per block | Contract delivery per block + FAIL |
| C-16 gap-to-plan column | Closes gap? column | Closes gap? column | Closes gap? column | Closes gap? column | Closes gap? column |
| C-17 verbatim quotation | PARTIAL — content cite without blockquote | PARTIAL — content cite without blockquote | PASS — per-block contract mandates verbatim embed | PARTIAL — content cite without blockquote | PASS — per-block contract + blockquote format + FAIL |
| C-18 inter-phase GATE | PASS — GATE-0, GATE-1, GATE-P, GATE-C, GATE-D | PASS — GATE-0, GATE-H, GATE-P, GATE-C, GATE-CAL, GATE-S | PASS — named gates throughout | PASS — GATE-0, GATE-1, GATE-P, GATE-C, GATE-CAL, GATE-S | PASS — full gate system (GATE-0, GATE-1, GATE-P, GATE-PLANNER, GATE-E1, GATE-E2, GATE-EXPERIMENTER, GATE-CAL) |
| C-19 inline FAIL | PARTIAL — some FAIL conditions present | PARTIAL — some FAIL (GATE-CAL, GATE-S, GATE-D) | PARTIAL — no FAIL labels, gate only | PARTIAL — multiple FAIL conditions | PASS — per-criterion FAIL throughout all roles |
| **C-20 atomic gate** | **PASS — GATE-1 is single gate, explicit A AND B conjunction, evaluation table** | PARTIAL — GATE-H checks both conditions but as advisory list, not named atomic conjunction | PARTIAL — gate checks both conditions but not framed as atomic conjunction | **PASS — GATE-1 with explicit atomic conjunction table** | **PASS — GATE-1 as atomic conjunction table + FAIL + STOP** |
| **C-21 calibration gate** | PARTIAL — findings confidence required not-identical, but no dedicated gate | **PASS — GATE-CAL with explicit non-uniformity pass condition + FAIL for uniform labels** | PARTIAL — "not all identical" advisory, no dedicated gate | **PASS — GATE-CAL with non-uniformity enforcement + FAIL** | **PASS — GATE-CAL + FAIL + STOP** |
| **C-22 per-block citation** | FAIL — global Input citation rule only, not embedded per-block | FAIL — global pointer prohibition only | **PASS — citation contract clause embedded in INPUT section of each consumer block** | FAIL — global pointer prohibition, not per-block | **PASS — citation contract clause embedded locally in each consumer block INPUT section + FAIL** |

**Projected v5 scores:**

| Variation | Primary axis | C-20 | C-21 | C-22 | Expected ceiling |
|-----------|-------------|------|------|------|-----------------|
| V-01 | Atomic conjunction gate | PASS | PARTIAL | FAIL | ~148/160 |
| V-02 | Calibration gate | PARTIAL | PASS | FAIL | ~148/160 |
| V-03 | Per-block citation contract | PARTIAL | PARTIAL | PASS | ~148/160 |
| V-04 | C-20 + C-21 combined | PASS | PASS | FAIL | ~153/160 |
| V-05 | All three + R4 V-05 floor | PASS | PASS | PASS | ~160/160 |
