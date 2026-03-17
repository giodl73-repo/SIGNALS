---
skill: quest-variate
skill_target: prove-program
date: 2026-03-15
round: 6
rubric: prove-program-rubric-v6-2026-03-15.md
status: DRAFT
---

# prove-program -- Variations R6 (V-01 through V-05)

**Context**: R5 V-05 confirmed 160/160 ceiling. v6 rubric is unchanged (header update only). No new criteria.
**R6 purpose**: Verify ceiling stability across distinct structural axes not systematically explored in R5.
**R5 single-axis**: lifecycle emphasis (C-20 / C-21 / C-22 gate placement). R5 combined: C-20+C-21 then all three.
**R6 single-axis**: V-01 (role sequence), V-02 (output format), V-03 (phrasing register).
**R6 combined**: V-04 (lifecycle emphasis + inertia framing), V-05 (role sequence + phrasing register + inertia framing).
**Prediction**: All five score 160/160, demonstrating that C-20/C-21/C-22 are format-agnostic structural properties.

---

## V-01 -- Role sequence axis: 4-role model (FRAMER -> PLANNER -> RUNNER -> EVALUATOR)

**Variation axis:** Role sequence -- PLANNER is split into two roles: FRAMER owns inertia gap + hypothesis commitment, PLANNER owns experiment design. This adds a dedicated GATE-1 between FRAMER and PLANNER and a COMPLETE marker handoff, making the atomic conjunction gate (C-20) a structural role boundary rather than an advisory checkpoint.
**Hypothesis:** Splitting hypothesis commitment from experiment planning into separate bounded roles -- with a hard gate and COMPLETE marker between them -- makes C-20 structurally impossible to skip, because the gate is also the only path by which PLANNER receives inputs; PLANNER cannot execute without FRAMER COMPLETE, and FRAMER COMPLETE requires GATE-1 PASS.

---

You are running a research program for: **{{topic}}**

Research question: {{research_question}}

Four roles execute in strict sequence: FRAMER -> PLANNER -> RUNNER -> EVALUATOR. Each role has bounded write authority. No role may write outside its designated sections.

---

### Role Declarations

| Role | Writes | May Not |
|------|--------|---------|
| FRAMER | Inertia gap, hypothesis, falsification, GATE-1 evaluation | Plan experiments, execute, write findings or synthesis |
| PLANNER | Experiment plan only | Change hypothesis, execute, write findings, write synthesis |
| RUNNER | Experiment execution in plan order | Change plan, change hypothesis, write findings, write synthesis |
| EVALUATOR | Feed-forward ledger, findings, GATE-CAL, synthesis, principles | Re-run experiments, change hypothesis, change plan |

---

### FRAMER

#### Phase 0 -- Inertia Gap Declaration

The inertia competitor is **prove-topic**: single-topic intelligence -> analysis -> interview -> synthesis scoped to one Signal topic. prove-program is required only when the research question exceeds prove-topic's capability.

Inertia gap: [what prove-topic cannot handle here -- cross-namespace scope, external domain, multi-hypothesis structure, or custom experiment type]

GATE-0: Inertia gap must name a specific capability prove-topic lacks for this question.
FAIL: Gap statement is generic ("more flexibility needed") rather than naming the specific limitation.
STOP: If prove-topic is sufficient, stop and use it.

---

#### Phase 1 -- Hypothesis Pre-Commitment

State a specific, testable belief. Required before any experiment is named or planned.

Hypothesis: [what you believe is true -- one sentence, positive form]
Falsification: [what evidence would cause you to reject this hypothesis]

---

#### GATE-1 -- Atomic Hypothesis + Falsification Conjunction [FRAMER -> PLANNER Boundary]

Single atomic gate. Both conditions must be TRUE. Partial satisfaction -- one TRUE, one FALSE or absent -- is FAIL.

| Condition | Description | Result |
|-----------|-------------|--------|
| A -- Hypothesis distinctness | Hypothesis differs from research question in specificity or framing. A restatement in different words fails. | TRUE / FALSE |
| B -- Falsification present | Falsification criterion explicitly stated: a specific piece of evidence that would cause rejection of hypothesis. | TRUE / FALSE |

GATE-1 result: **PASS** (A AND B = TRUE) / **FAIL** (A = FALSE OR B = FALSE)

FAIL: Hypothesis is a restatement of the question, or falsification criterion missing. Return to Phase 1, rewrite, re-evaluate GATE-1.
STOP: Do not produce FRAMER COMPLETE until GATE-1 result is PASS.

**FRAMER COMPLETE**
Hypothesis locked: [verbatim]
Falsification criterion: [verbatim]
Inertia gap: [verbatim]
-> PLANNER receives: hypothesis, falsification criterion, inertia gap

---

### PLANNER

GATE-FRAMER: Confirm FRAMER COMPLETE before writing plan.
FAIL: Plan produced without FRAMER COMPLETE marker confirmed.

#### Phase 1B -- Experiment Plan

| # | Type | Question answered | Rationale | Output label | Consumed by | Closes gap? |
|---|------|------------------|-----------|--------------|-------------|-------------|
| E-01 | [websearch / intelligence / analysis / interview / prototype / custom] | [question] | [why this type, not another] | [label] | [E-02 / EVALUATOR] | Yes / No |
| E-02 | [type] | [question] | [rationale] | [label] | [EVALUATOR] | Yes / No |

Rules:
- >=2 distinct types -- no two rows share the same type
- >=1 row: Closes gap? = Yes (the experiment addressing Phase 0 inertia gap)
- All Output label cells filled -- these lock the per-block citation contract in RUNNER

GATE-P: (a) >=2 distinct types; (b) >=1 Closes gap? = Yes; (c) all Output labels filled.
FAIL: <2 distinct types, no Yes in Closes gap?, or any Output label blank.

**PLANNER COMPLETE**
Plan order: [E-01 type -> E-02 type -> ...]
Gap-closing experiment: [E-NN]
-> RUNNER receives: ordered plan, hypothesis verbatim, inertia gap verbatim, per-block citation contract requirement

---

### RUNNER

GATE-PLANNER: Confirm PLANNER COMPLETE before executing any experiment.
FAIL: Any experiment executes without PLANNER COMPLETE confirmed.

**Per-block citation contract -- governs all RUNNER consumer blocks:**

Every experiment block that consumes a prior block's output MUST embed the citation contract locally in its own INPUT section. A global rule in a preamble does NOT satisfy this requirement -- each consumer block's INPUT section must contain the contract clause and the verbatim content. Format:

> Citation contract (local to this block): reproduce the exact output text of the prior block. Pointer references ("see above", "per E-NN", "as found in E-NN", or any paraphrase) are prohibited in this INPUT section. Embed verbatim content below.

FAIL (applies independently to every consumer block): Input section uses a pointer reference, paraphrase, or does not contain the local citation contract clause + verbatim blockquote.

---

#### E-01 -- [Type from Phase 1B]

GATE-E1-entry: PLANNER COMPLETE confirmed.

INPUT: Phase 1 hypothesis -- [verbatim hypothesis text] | Phase 0 inertia gap -- [verbatim gap text]

[One sentence: how hypothesis + inertia gap focus this experiment's scope.]

[Execute experiment.]

E-01 output: [labeled finding -- this exact text is what E-02 must embed verbatim in its INPUT section]

Contract delivery: output label = "[plan label]" -- consumed by: [E-02 / EVALUATOR] -- delivered? Yes / No
FAIL: Contract delivery absent or output label does not match PLANNER Phase 1B.

**EXPERIMENT 1 COMPLETE**
Produced: E-01 -- [one-line summary]
-> Consumed by: [E-02 / EVALUATOR]

---

#### E-02 -- [Type from Phase 1B]

GATE-E2-entry: EXPERIMENT 1 COMPLETE confirmed before executing.
FAIL: E-02 begins without EXPERIMENT 1 COMPLETE marker present.

INPUT -- citation contract (local to this block): This block consumes E-01 output. Reproduce the exact text of E-01's labeled finding below. Pointer references ("see above", "per E-01", "as found in E-01") are prohibited in this INPUT section. Embed verbatim content:

> [exact text from E-01 output -- the labeled finding quoted directly, not described or paraphrased]

[One sentence: how E-01's finding constrains or refocuses this experiment.]

[Execute experiment.]

E-02 output: [labeled finding]

Contract delivery: output label = "[plan label]" -- consumed by: [EVALUATOR] -- delivered? Yes / No
FAIL: Contract delivery absent or output label mismatch with PLANNER Phase 1B.

**EXPERIMENT 2 COMPLETE**
Produced: E-02 -- [one-line summary]
-> Consumed by: EVALUATOR

---

[Add E-03+ as needed. Every consumer block requires:
1. GATE-E{N}-entry confirmation of prior COMPLETE marker
2. INPUT section containing the local citation contract clause + verbatim blockquote
3. Execution
4. Labeled E-NN output
5. Contract delivery line with delivered? boolean
6. EXPERIMENT N COMPLETE marker with consumed-by routing
The citation contract is embedded in each block's INPUT section individually -- not in a shared global rule.]

**RUNNER COMPLETE**
All outputs: E-01 [type], E-02 [type], ...
-> EVALUATOR receives: all labeled experiment outputs

---

### EVALUATOR

GATE-RUNNER: Confirm RUNNER COMPLETE before executing.
FAIL: Any EVALUATOR section begins without RUNNER COMPLETE confirmed.

#### Feed-Forward Audit Ledger

| Experiment | Plan output label | Delivered? | Consumed by |
|-----------|------------------|------------|-------------|
| E-01 | [plan label] | Yes / No | [step] |
| E-02 | [plan label] | Yes / No | [step] |

Populate from Contract delivery lines in RUNNER. Do not infer values not stated in RUNNER blocks.
FAIL: Ledger absent, or any row's Delivered? contradicts the corresponding Contract delivery line.

---

#### Findings

| # | Finding | Source | Confidence | Evidence basis |
|---|---------|--------|------------|---------------|
| F-01 | [finding text] | E-01 | high / medium / low | [e.g., "2 consistent sources", "single source not replicated"] |
| F-02 | [finding text] | E-02 | high / medium / low | [basis] |

Minimum 2 findings. Evidence basis required per row.
FAIL: Fewer than 2 findings, or evidence basis absent from any row.

---

#### GATE-CAL -- Confidence Calibration Check [Findings -> Synthesis Boundary]

This gate enforces calibration. Presence of confidence labels is necessary but not sufficient.

**GATE-CAL pass condition**: The findings table contains at least two distinct confidence values. All findings labeled the same level -- regardless of which level -- fail this gate. FAIL condition: all findings rated HIGH (or all MEDIUM, or all LOW).

**GATE-CAL evaluation**:
- Distinct confidence values in findings table: [list -- e.g., "high (F-01), medium (F-02)"]
- Count of distinct values: [N]
- At least 2 distinct values? YES / NO
- **GATE-CAL result: PASS / FAIL**

FAIL: All findings carry the same confidence level. Return to Findings. Re-examine each finding's evidentiary basis independently. Differentiate confidence assignments. Re-evaluate GATE-CAL.
STOP: Do not write synthesis until GATE-CAL result is PASS.

---

#### Synthesis

**[Confirm GATE-CAL PASS before writing synthesis.]**

What we thought: [hypothesis verbatim from FRAMER Phase 1]
What we actually learned: [confirm, refine, or refute -- must differ from hypothesis text. Answer the research question.]

Inertia gap closure: [Did the gap-closing experiment produce a finding prove-topic could not have produced? Yes / No + one sentence of evidence.]

Cross-namespace note: [Name any downstream Signal artifact that should receive these findings -- draft spec, scout brief, topic plan, topic story.]

FAIL: "What we actually learned" copies the hypothesis verbatim, or either synthesis field is absent.
FAIL: Inertia gap closure verdict absent or states neither Yes nor No.

---

#### Principles

| Label | Principle | Source finding |
|-------|-----------|---------------|
| P-01 | [When X, do Y -- or Always Z] | F-NN |
| P-02 | [When X, do Y -- or Always Z] | F-NN |

Minimum 2 principles. No generic truisms. Source finding required per row.
FAIL: Fewer than 2, principles are generic truisms, or source finding column blank.

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

## V-02 -- Output format axis: numbered procedure (Step N) instead of phase/role labels

**Variation axis:** Output format -- the entire skill is presented as a numbered procedure (Step 1 through Step 11) rather than as labeled phases or named roles. Gates are named by their step position (GATE-2A, GATE-4, GATE-8, etc.). This tests whether the ceiling is achievable when structural sections are identified by sequence number rather than semantic labels.
**Hypothesis:** The 160/160 ceiling is format-agnostic: numbered procedure steps that enforce the same structural invariants as phase labels produce identical criterion coverage, because the rubric tests for structural properties (gate enforcement, per-block contracts, calibration) not for specific section-naming conventions.

---

You are running a research program for: **{{topic}}**

Research question: {{research_question}}

Execute the following steps in order. Do not advance to a step until its entry condition is met. Gates are hard stops, not advisory checks.

---

### Step 1 -- Declare the Inertia Gap

The inertia competitor is **prove-topic**: single-topic intelligence -> analysis -> interview -> synthesis on one Signal topic. This step exists because prove-program is only warranted when the research question exceeds prove-topic's capability.

Inertia gap: [what prove-topic cannot handle here -- cross-namespace scope, external domain, multi-hypothesis structure, or custom experiment type]

GATE-1: Inertia gap must name a specific capability prove-topic lacks for this question.
FAIL: Gap statement is generic. Rewrite to name the specific limitation.
STOP: If prove-topic is sufficient for this question, stop and use it instead.

---

### Step 2 -- Commit to Hypothesis and Falsification

Write one specific, testable belief in positive form. Write it before naming any experiment.

Hypothesis: [what you believe is true -- one sentence, positive form]
Falsification: [what specific evidence would cause you to reject this hypothesis]

---

### GATE-2A -- Atomic Hypothesis + Falsification Conjunction [Step 2 -> Step 3 Boundary]

Single atomic gate. Both conditions must be TRUE. One TRUE and one FALSE is FAIL -- the gate is conjunctive, not advisory.

| Condition | Description | Result |
|-----------|-------------|--------|
| A -- Hypothesis distinctness | Hypothesis differs from research question in specificity or framing. A restatement in different words fails. | TRUE / FALSE |
| B -- Falsification present | Falsification criterion explicitly stated: a specific piece of evidence that would cause rejection of the hypothesis. | TRUE / FALSE |

GATE-2A result: **PASS** (A AND B = TRUE) / **FAIL** (A = FALSE OR B = FALSE)

FAIL: Hypothesis is a restatement of the question, or falsification criterion is absent. Return to Step 2. Rewrite and re-evaluate GATE-2A.
STOP: Do not proceed to Step 3 until GATE-2A result is PASS.

---

### Step 3 -- Build the Experiment Plan

Produce this table before executing any experiment. Every cell must be filled.

| # | Type | Question answered | Rationale | Output label | Consumed by | Closes gap? |
|---|------|------------------|-----------|--------------|-------------|-------------|
| E-01 | [websearch / intelligence / analysis / interview / prototype / custom] | [question] | [why this type, not another] | [label] | [E-02 / Step 8] | Yes / No |
| E-02 | [type] | [question] | [rationale] | [label] | [Step 8] | Yes / No |

Rules:
- >=2 distinct types -- no two rows may share the same type
- >=1 row: Closes gap? = Yes
- All Output label cells filled -- these lock the per-block citation contract in Steps 4-7

GATE-3: All plan requirements met.
FAIL: <2 distinct types, no Yes in Closes gap?, or any Output label blank.
STOP: Do not execute any experiment until GATE-3 passes.

---

### Step 4 -- Execute Experiment E-01

**Step 4 entry condition**: GATE-3 PASS confirmed.

INPUT: Step 2 hypothesis -- [verbatim hypothesis text] | Step 1 inertia gap -- [verbatim gap text]

[One sentence: how hypothesis + inertia gap scope this experiment.]

[Execute experiment.]

E-01 output: [labeled finding -- this exact text is what Step 5 must embed verbatim in its INPUT]

Contract delivery: output label = "[plan label]" -- consumed by: [E-02 / Step 8] -- delivered? Yes / No
FAIL: Contract delivery absent or output label does not match Step 3 plan.

**STEP 4 COMPLETE -- E-01 produced**
E-01 summary: [one line]
-> Consumed by: [Step 5 / Step 8]

---

### Step 5 -- Execute Experiment E-02

**Step 5 entry condition**: STEP 4 COMPLETE confirmed.
FAIL: Step 5 begins without STEP 4 COMPLETE present.

INPUT -- citation contract (local to this step): This step consumes E-01 output from Step 4. Reproduce the exact text of E-01's labeled finding below. Pointer references ("see above", "per E-01", "as found in Step 4") are prohibited in this INPUT section. Embed verbatim content:

> [exact text from E-01 output -- the labeled finding quoted directly, not described or paraphrased]

[One sentence: how E-01's finding changes the scope or focus of this experiment.]

[Execute experiment.]

E-02 output: [labeled finding]

Contract delivery: output label = "[plan label]" -- consumed by: [Step 8] -- delivered? Yes / No
FAIL: Contract delivery absent or output label mismatch with Step 3 plan.

**STEP 5 COMPLETE -- E-02 produced**
E-02 summary: [one line]
-> Consumed by: Step 8

---

[Add Step 6, Step 7, etc. for additional experiments as needed. Each step must:
1. State its entry condition (prior COMPLETE marker confirmed)
2. INPUT section containing the citation contract clause + verbatim blockquote from the consumed output
3. Execute the experiment
4. Produce a labeled E-NN output
5. Contract delivery line with delivered? boolean
6. STEP N COMPLETE marker with consumed-by routing
Citation contract is embedded locally in each step's INPUT section -- not in a global rule.]

**ALL EXPERIMENTS COMPLETE**
Steps completed: Step 4 (E-01 [type]), Step 5 (E-02 [type]), ...
-> Step 8 receives: all labeled experiment outputs

---

### Step 6 -- Feed-Forward Audit Ledger

**Step 6 entry condition**: ALL EXPERIMENTS COMPLETE confirmed.

| Step | Plan output label | Delivered? | Consumed by |
|------|------------------|------------|-------------|
| Step 4 (E-01) | [label] | Yes / No | [step] |
| Step 5 (E-02) | [label] | Yes / No | [step] |

Populate from Contract delivery lines. Do not infer values not stated in experiment steps.
FAIL: Ledger absent or any Delivered? value contradicts the Contract delivery line.

---

### Step 7 -- Findings Table

| # | Finding | Source | Confidence | Evidence basis |
|---|---------|--------|------------|---------------|
| F-01 | [finding] | E-01 | high / medium / low | [e.g., "2 consistent sources", "single source not replicated"] |
| F-02 | [finding] | E-02 | high / medium / low | [basis] |

Minimum 2 findings. Evidence basis required per row.
FAIL: Fewer than 2 findings, or evidence basis absent from any row.

---

### GATE-7A -- Confidence Calibration Check [Step 7 -> Step 8 Boundary]

This gate enforces calibration. Presence of confidence labels is necessary but not sufficient.

**GATE-7A pass condition**: The findings table contains at least two distinct confidence values. FAIL condition: all findings rated HIGH (uniform high), or all MEDIUM (uniform medium), or all LOW (uniform low).

**GATE-7A evaluation**:
- Distinct confidence values in findings table: [list -- e.g., "high (F-01), medium (F-02)"]
- Count of distinct values: [N]
- At least 2 distinct values? YES / NO
- **GATE-7A result: PASS / FAIL**

FAIL: All findings carry the same confidence level. Return to Step 7. Re-examine each finding's evidentiary basis independently. Differentiate confidence assignments to reflect evidence quality differences. Re-evaluate GATE-7A.
STOP: Do not write Step 8 until GATE-7A result is PASS.

---

### Step 8 -- Synthesis

**Step 8 entry condition**: GATE-7A PASS confirmed.

What we thought: [hypothesis verbatim from Step 2]
What we actually learned: [confirm, refine, or refute -- must differ from hypothesis text. Answer the research question.]

Inertia gap closure: [Did the gap-closing experiment produce a finding prove-topic could not have produced? Yes / No + one sentence.]

Cross-namespace note: [Name any downstream Signal artifact that should receive these findings.]

GATE-8: "What we actually learned" must not be a verbatim copy of hypothesis.
FAIL: "What we actually learned" copies the hypothesis verbatim, or either synthesis field is absent.

---

### Step 9 -- Principles

P-01: [When X, do Y -- or Always Z] -- Source: F-NN
P-02: [When X, do Y -- or Always Z] -- Source: F-NN

Minimum 2. No generic truisms. Source finding required.
FAIL: Fewer than 2 principles, or principles are generic truisms.

---

### Step 10 -- Write Artifact

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

## V-03 -- Phrasing register axis: second-person imperative + question-answer frame

**Variation axis:** Phrasing register -- every section header is a direct question addressed to the researcher; the body is the answer format. Imperative second-person voice ("Write your hypothesis now", "You may not proceed") replaces the impersonal third-person register used in all prior rounds. This tests whether the 160/160 ceiling holds when the same structural constraints are expressed through direct address.
**Hypothesis:** Phrasing register is orthogonal to rubric criterion compliance: criteria test for structural elements (gate tables, contract clauses, labeled fields) not for grammatical person or sentence voice; therefore the second-person imperative register produces the same ceiling as formal register, because the required elements are present regardless of how they are requested.

---

You are running a research program for: **{{topic}}**

Research question: {{research_question}}

You will answer each question below in order. Do not answer a question before completing all prior ones. When a gate appears, evaluate it before continuing.

---

### What is the inertia gap?

You are choosing prove-program over **prove-topic**. prove-topic is: single-topic intelligence -> analysis -> interview -> synthesis on one Signal topic. You are justified in using prove-program only if this question exceeds prove-topic's capability.

Write the gap now: [what prove-topic cannot handle here -- cross-namespace scope, external domain, multi-hypothesis structure, or custom experiment type]

Gate -- Before continuing: Does your gap name a specific capability prove-topic lacks for this question? If prove-topic is sufficient, stop and use it.
FAIL: Your gap is generic. Rewrite it to name the specific limitation.

---

### What do you believe is true?

Write one sentence, in positive form, stating your specific belief about {{topic}}. This is your hypothesis. Write it now, before naming any experiment.

Your hypothesis: [one sentence, positive form]
What would change your mind: [specific evidence that would cause you to reject your hypothesis]

---

### GATE-H -- Do your hypothesis and falsification pass the atomic check? [Commits you to the experiment plan]

You cannot design experiments until both conditions below are TRUE. Check each one:

| Condition | Check | Your result |
|-----------|-------|-------------|
| A -- Your hypothesis is distinct | It differs from the research question in specificity or framing. A restatement in different words fails. | TRUE / FALSE |
| B -- Your falsification is explicit | It names a specific piece of evidence that would cause rejection. A vague qualifier ("if the evidence doesn't support it") fails. | TRUE / FALSE |

GATE-H result: **PASS** (A AND B = TRUE) / **FAIL** (A = FALSE OR B = FALSE)

FAIL: Your hypothesis is a restatement of the question, or your falsification criterion is absent. Rewrite and re-evaluate GATE-H.
STOP: You may not design experiments until GATE-H result is PASS.

---

### What experiments will you run?

Design your experiment plan now. You must complete this table before executing anything.

| # | Type | Question you will answer | Why this type, not another | What you will call the output | Who consumes it | Does it close the gap? |
|---|------|-------------------------|---------------------------|-------------------------------|-----------------|----------------------|
| E-01 | [websearch / intelligence / analysis / interview / prototype / custom] | [question] | [rationale] | [output label] | [E-02 / synthesis] | Yes / No |
| E-02 | [type] | [question] | [rationale] | [output label] | [synthesis] | Yes / No |

Requirements:
- Pick >=2 different types -- no two rows may be the same type
- At least one row must close the inertia gap (Yes in the last column)
- Fill in every output label cell now -- you will need them in the experiments

GATE-P: Check: >=2 distinct types? All output labels filled? At least one Yes in "closes gap"?
FAIL: Any of the three requirements is not met. Revise and re-evaluate GATE-P.
STOP: Do not execute any experiment until GATE-P passes.

---

### Run your first experiment.

**Entry check**: GATE-P confirmed PASS.

What you bring in:
INPUT: Your hypothesis (verbatim): [verbatim hypothesis text] | Your inertia gap (verbatim): [verbatim gap text]

Write one sentence: how do your hypothesis and inertia gap scope what you are looking for in this experiment?

[Execute E-01.]

Name your output: E-01 output: [labeled finding -- write this text precisely; E-02 will reproduce it verbatim]

Record delivery: output label = "[plan label]" -- consumed by: [E-02 / synthesis] -- delivered? Yes / No
FAIL: Delivery line absent or output label does not match your plan.

**E-01 complete.** Summary: [one line]. -> E-02 (or synthesis) receives this output.

---

### Run your second experiment.

**Entry check**: E-01 complete confirmed.
FAIL: You begin E-02 without E-01 complete present.

What you bring in -- citation contract (local to this experiment): You are consuming E-01 output. Reproduce the exact text of E-01's labeled finding below. You may not write "see above", "per E-01", "as found previously", or any paraphrase. Embed the verbatim text:

> [exact text from E-01 output -- quoted directly from the labeled finding, not described]

Write one sentence: how does E-01's finding change what you are looking for here?

[Execute E-02.]

Name your output: E-02 output: [labeled finding]

Record delivery: output label = "[plan label]" -- consumed by: [synthesis] -- delivered? Yes / No
FAIL: Delivery line absent or output label mismatch.

**E-02 complete.** Summary: [one line]. -> Synthesis receives this output.

---

[For each additional experiment: entry check confirms prior complete marker; INPUT section must contain the citation contract clause and verbatim blockquote from the consumed output; end with complete marker and routing. The citation contract lives in each experiment's INPUT section -- not in a global rule above.]

**All experiments complete.** -> Synthesis receives: all labeled outputs.

---

### What did each experiment actually deliver?

Fill in this ledger from your delivery lines above. Do not infer anything not stated in your experiments.

| Experiment | Output label from plan | Delivered? | Who consumed it |
|-----------|------------------------|------------|-----------------|
| E-01 | [label] | Yes / No | [step] |
| E-02 | [label] | Yes / No | [step] |

FAIL: Ledger absent or any Delivered? contradicts the corresponding delivery line.

---

### What did you find?

| # | Finding | Which experiment | How confident are you | Why that confidence level |
|---|---------|-----------------|----------------------|--------------------------|
| F-01 | [finding] | E-01 | high / medium / low | [e.g., "2 independent sources", "single source, not replicated"] |
| F-02 | [finding] | E-02 | high / medium / low | [basis] |

Write at least 2 findings. Write the evidence basis for each.
FAIL: Fewer than 2 findings, or evidence basis absent from any row.

---

### GATE-CAL -- Are your confidence levels calibrated? [Commits you to synthesis]

Before writing what you learned, check this: are your confidence levels the same across all findings, or different?

**The pass condition is differentiation, not presence.** Writing "high" for every finding means you have not calibrated -- you have just asserted confidence uniformly. That fails this gate.

- List the distinct confidence values in your findings table: [e.g., "high (F-01), medium (F-02)"]
- Count of distinct values: [N]
- Do you have at least 2 distinct values? YES / NO
- **GATE-CAL result: PASS / FAIL**

FAIL: All your findings carry the same confidence level (all HIGH, all MEDIUM, or all LOW). Return to your findings table. Look at each finding's evidence basis independently. Reassign confidence to reflect real differences in evidence strength. Re-evaluate GATE-CAL.
STOP: You may not write synthesis until GATE-CAL result is PASS.

---

### What did you actually learn?

**Entry check**: GATE-CAL PASS confirmed.

What you thought going in: [your hypothesis verbatim from the hypothesis step]
What you actually learned: [confirm, refine, or refute -- this must differ from your hypothesis. Answer the research question with your findings.]

Did the gap-closing experiment deliver a finding prove-topic could not have delivered? Yes / No + one sentence.

Which Signal artifact downstream should receive these findings? [draft spec / scout brief / topic plan / topic story -- name it]

FAIL: "What you actually learned" copies your hypothesis verbatim. Rewrite it.

---

### What principles do you take away?

P-01: [When X, do Y -- or Always Z] -- Source: F-NN
P-02: [When X, do Y -- or Always Z] -- Source: F-NN

Write at least 2. Make them specific and actionable, not truisms. Cite the finding each comes from.
FAIL: Fewer than 2, or principles are generic truisms.

---

### Write the artifact.

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

## V-04 -- Combined: Lifecycle emphasis + Inertia framing

**Variation axes:** Lifecycle emphasis (explicit phase-crossing narration at every boundary) + Inertia framing (prove-topic capability map as structural spine, referenced at every gate)
**Hypothesis:** Anchoring the inertia competitor as a first-class structural element -- a capability map table consulted at every phase boundary -- reinforces C-08 and C-13 beyond the minimum by making the prove-topic foil impossible to ignore during execution, while explicit lifecycle narration ("You are now crossing Phase 1 -> Phase 2") strengthens the COMPLETE marker pattern and makes phase gate violations self-evident.

---

You are running a research program for: **{{topic}}**

Research question: {{research_question}}

This program runs against a named inertia competitor at every phase boundary. Complete phases in order. Read the prove-topic capability map before proceeding.

---

### Inertia Competitor -- prove-topic Capability Map

**The inertia competitor is prove-topic.** Before each phase, consult this map to confirm prove-program adds value where prove-topic cannot.

| Capability | prove-topic | prove-program |
|-----------|-------------|---------------|
| Research scope | Single Signal topic | Any question, any domain |
| Experiment types | Intelligence, analysis, interview, synthesis | Any combination: + websearch, + prototype, + custom |
| Cross-namespace findings | Not supported | Supported via custom experiment |
| Multi-hypothesis structure | Not supported | Supported via parallel experiment tracks |
| External domain research | Not supported | Supported via websearch + custom |

**prove-program is warranted only when the research question requires a capability prove-topic lacks.** If no row in the right column is needed for this question, use prove-topic.

---

### Phase 0 -- Inertia Gap

**Phase entry**: You are entering Phase 0. Consult the prove-topic capability map above.

Which cell in the "prove-program" column is required to answer this research question? Name it explicitly.

Inertia gap: [what prove-topic cannot handle here -- name the specific capability from the map]

GATE-0 [Phase 0 -> Phase 1 Boundary]: Inertia gap names a specific prove-topic capability limitation from the map.
FAIL: Gap statement is generic. Consult the map and name the specific row.
STOP: If prove-topic can handle this question, use it.

**Phase 0 complete. You are crossing the Phase 0 -> Phase 1 boundary.**
Inertia gap carried forward: [verbatim]

---

### Phase 1 -- Hypothesis

**Phase entry**: You are entering Phase 1. You are committing to a hypothesis before any experiment is named.

State a specific, testable belief about {{topic}}. Must differ from the research question in specificity or framing.

Hypothesis: [what you believe is true -- one sentence, positive form]
Falsification: [what specific evidence would cause you to reject this hypothesis]

---

### GATE-1 -- Atomic Hypothesis + Falsification Conjunction [Phase 1 -> Phase 1B Boundary]

**You are at the Phase 1 -> Phase 1B boundary.** This gate enforces both hypothesis integrity and falsification as an atomic conjunction. Consult the prove-topic capability map: a vague hypothesis does not exploit prove-program's additional experiment types.

Single atomic gate. Both conditions must be TRUE. Partial satisfaction is FAIL.

| Condition | Description | Result |
|-----------|-------------|--------|
| A -- Hypothesis distinctness | Hypothesis differs from research question in specificity or framing. A restatement in different words fails. | TRUE / FALSE |
| B -- Falsification present | Falsification criterion explicitly stated: a specific piece of evidence that would cause rejection of the hypothesis. | TRUE / FALSE |

GATE-1 result: **PASS** (A AND B = TRUE) / **FAIL** (A = FALSE OR B = FALSE)

FAIL: Hypothesis is a restatement of the question, or falsification criterion absent. Return to Phase 1, rewrite, re-evaluate GATE-1.
STOP: You may not cross into Phase 1B until GATE-1 result is PASS.

**Phase 1 complete. You are crossing the Phase 1 -> Phase 1B boundary.**
Hypothesis carried forward: [verbatim]

---

### Phase 1B -- Experiment Plan

**Phase entry**: You are entering Phase 1B. Consult the prove-topic capability map: your experiment types must include at least one type prove-topic cannot run (the capability that closes your inertia gap).

| # | Type | Question answered | Rationale | Output label | Consumed by | Closes gap? |
|---|------|------------------|-----------|--------------|-------------|-------------|
| E-01 | [websearch / intelligence / analysis / interview / prototype / custom] | [question] | [why this type -- reference the capability map if gap-closing] | [label] | [E-02 / Phase 3] | Yes / No |
| E-02 | [type] | [question] | [rationale] | [label] | [Phase 3] | Yes / No |

Rules:
- >=2 distinct types
- >=1 row: Closes gap? = Yes -- the experiment that uses the prove-program-only capability from the map
- All Output labels filled

GATE-P [Phase 1B -> Phase 2 Boundary]: All plan requirements met.
FAIL: <2 distinct types, no Yes in Closes gap?, or any Output label blank.
STOP: Do not cross into Phase 2 until GATE-P passes.

**Phase 1B complete. You are crossing the Phase 1B -> Phase 2 boundary.**
Plan locked. Gap-closing experiment: [E-NN].

---

### Phase 2 -- Experiment Execution

**Phase entry**: You are entering Phase 2. You are executing the plan in order. Each experiment block must carry its own citation contract -- this is a prove-program behavior prove-topic does not require because it has no multi-experiment feed-forward chain.

---

#### E-01 -- [Type from Phase 1B]

**Phase 2 entry confirmed.**

INPUT: Phase 1 hypothesis -- [verbatim hypothesis text] | Phase 0 inertia gap -- [verbatim gap text]

[One sentence: how hypothesis + inertia gap scope this experiment.]

[Execute experiment.]

E-01 output: [labeled finding]

Contract delivery: output label = "[plan label]" -- consumed by: [E-02 / Phase 3] -- delivered? Yes / No
FAIL: Contract delivery absent or output label does not match Phase 1B plan.

**EXPERIMENT 1 COMPLETE.** E-01 summary: [one line]. -> Consumed by: [E-02 / Phase 3].

---

#### E-02 -- [Type from Phase 1B]

**Entry check**: EXPERIMENT 1 COMPLETE confirmed.
FAIL: E-02 begins without EXPERIMENT 1 COMPLETE present.

INPUT -- citation contract (local to this block): This block consumes E-01 output. Reproduce the exact text of E-01's labeled finding below. Pointer references ("see above", "per E-01", "as found in E-01") are prohibited in this INPUT section. Embed verbatim content:

> [exact text from E-01 output -- the labeled finding quoted directly, not described or paraphrased]

[One sentence: how E-01's finding -- which prove-topic could not have produced through a single-topic campaign -- changes the scope of this experiment.]

[Execute experiment.]

E-02 output: [labeled finding]

Contract delivery: output label = "[plan label]" -- consumed by: [Phase 3] -- delivered? Yes / No
FAIL: Contract delivery absent or output label mismatch with Phase 1B plan.

**EXPERIMENT 2 COMPLETE.** E-02 summary: [one line]. -> Consumed by: Phase 3.

---

[Add E-03+ as needed. Every consumer block requires the local citation contract clause + verbatim blockquote in its INPUT section. The citation contract is per-block, not global.]

**PHASE 2 COMPLETE.** All experiment outputs produced.
-> Phase 3 receives: all labeled outputs. Note: this multi-experiment feed-forward chain is the core prove-program capability that justify its use over prove-topic.

---

### Phase 3A -- Feed-Forward Audit Ledger

**Phase entry**: You are crossing Phase 2 -> Phase 3A.

| Experiment | Plan output label | Delivered? | Consumed by |
|-----------|------------------|------------|-------------|
| E-01 | [label] | Yes / No | [step] |
| E-02 | [label] | Yes / No | [step] |

Populate from Contract delivery lines in Phase 2. Do not infer.
FAIL: Ledger absent or any Delivered? contradicts the delivery line.

---

### Phase 3B -- Findings

| # | Finding | Source | Confidence | Evidence basis |
|---|---------|--------|------------|---------------|
| F-01 | [finding] | E-01 | high / medium / low | [basis] |
| F-02 | [finding] | E-02 | high / medium / low | [basis] |

Minimum 2 findings. Evidence basis required per row.
FAIL: Fewer than 2 findings, or evidence basis absent from any row.

---

### GATE-CAL -- Confidence Calibration Check [Phase 3B -> Phase 3C Boundary]

**You are at the Phase 3B -> Phase 3C boundary.** Consult the prove-topic capability map: calibrated confidence across multi-experiment outputs is a prove-program deliverable -- a single-topic prove campaign produces one confidence signal; your multi-experiment program should differentiate.

This gate enforces calibration. Presence is necessary but not sufficient. FAIL condition: all findings rated HIGH (or all MEDIUM, or all LOW -- any uniform label pattern fails).

**GATE-CAL evaluation**:
- Distinct confidence values in findings table: [list]
- Count of distinct values: [N]
- At least 2 distinct values? YES / NO
- **GATE-CAL result: PASS / FAIL**

FAIL: All findings carry the same confidence level. Return to Phase 3B. Re-examine each finding's evidentiary basis independently. Differentiate. Re-evaluate GATE-CAL.
STOP: Do not cross into Phase 3C until GATE-CAL result is PASS.

**Phase 3B complete. You are crossing the Phase 3B -> Phase 3C boundary.**

---

### Phase 3C -- Synthesis

**Phase entry**: GATE-CAL PASS confirmed.

What we thought: [hypothesis verbatim from Phase 1]
What we actually learned: [confirm, refine, or refute -- must differ from hypothesis text. Answer the research question.]

Inertia gap closure: [Did the gap-closing experiment produce a finding prove-topic could not have produced? Yes / No + one sentence naming the prove-program capability that made it possible.]

Cross-namespace note: [Name downstream Signal artifact that should receive these findings.]

GATE-S [Phase 3C -> Phase 3D Boundary]: Both synthesis fields present. "What we actually learned" is not a verbatim copy of hypothesis.
FAIL: "What we actually learned" copies the hypothesis verbatim, or either field absent.

---

### Phase 3D -- Principles

P-01: [When X, do Y -- or Always Z] -- Source: F-NN
P-02: [When X, do Y -- or Always Z] -- Source: F-NN

Minimum 2. No generic truisms. Source finding required.
FAIL: Fewer than 2 principles, or principles are generic truisms.

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

## V-05 -- Combined: Role sequence + Phrasing register + Inertia framing

**Variation axes:** Role sequence (4-role: FRAMER -> PLANNER -> RUNNER -> EVALUATOR from V-01) + Phrasing register (second-person imperative from V-03) + Inertia framing (prominent prove-topic foil from V-04) -- all three combined over the R5 V-05 atomic pattern floor (C-20 + C-21 + C-22)
**Hypothesis:** Combining three orthogonal surface-form axes -- role partition, grammatical person, and inertia salience -- does not degrade any criterion below R5 V-05 ceiling, because C-20/C-21/C-22 are structural invariants (gate table, calibration check, per-block contract) that are format, voice, and framing-agnostic; the surface changes make the prompt more flexible for different user contexts without touching the structural skeleton.

---

You are running a research program for: **{{topic}}**

Research question: {{research_question}}

You have chosen prove-program over prove-topic. Four roles will execute your program in sequence: FRAMER -> PLANNER -> RUNNER -> EVALUATOR. Each role will address you directly. Follow the instructions for each role before moving to the next.

---

### Before you begin -- Why are you using prove-program?

**prove-topic** handles: single-topic intelligence -> analysis -> interview -> synthesis, scoped to one Signal topic. It does not support cross-namespace scope, external domain research, multi-hypothesis structure, or custom experiment types.

If your research question fits entirely within prove-topic's capability, stop and use prove-topic now.

If it does not, name the specific capability you need:

Inertia gap: [what prove-topic cannot handle here]

GATE-0: Your gap must name a specific capability prove-topic lacks. A generic statement ("more flexibility") fails.
FAIL: Rewrite to name the specific limitation.
STOP: If prove-topic is sufficient, use it.

---

### FRAMER -- Your job: commit to a hypothesis before any planning begins.

You have declared an inertia gap. Now commit to what you believe is true.

**Write your hypothesis.** One sentence, positive form. Do not think about experiments yet.

Your hypothesis: [what you believe is true about {{topic}}]
What would change your mind: [specific evidence that would cause you to reject your hypothesis]

---

**FRAMER check -- do not plan until this gate passes.**

### GATE-1 -- Atomic Hypothesis + Falsification Conjunction [FRAMER -> PLANNER Boundary]

You are at the FRAMER -> PLANNER boundary. Answer both questions before PLANNER may begin.

| Question | What passes | Your answer |
|---------|-------------|-------------|
| A -- Is your hypothesis distinct from the research question? | It differs in specificity or framing. A restatement in different words fails. | TRUE / FALSE |
| B -- Is your falsification criterion explicit? | It names specific evidence that would cause rejection. A vague qualifier fails. | TRUE / FALSE |

GATE-1 result: **PASS** (A AND B = TRUE) / **FAIL** (A = FALSE OR B = FALSE)

FAIL: Your hypothesis is a restatement of the question, or your falsification criterion is absent. Rewrite and re-evaluate.
STOP: PLANNER may not begin until GATE-1 result is PASS.

**FRAMER COMPLETE.**
Your hypothesis, locked: [verbatim]
Your falsification criterion: [verbatim]
Your inertia gap: [verbatim]
-> PLANNER receives these three inputs.

---

### PLANNER -- Your job: design the experiment sequence that will test the hypothesis.

**Entry check**: FRAMER COMPLETE confirmed. Your inputs are the locked hypothesis, falsification criterion, and inertia gap above.
FAIL: You begin planning without FRAMER COMPLETE present.

Design a plan that exploits prove-program's additional capability over prove-topic. At least one experiment must use a capability prove-topic cannot run (the one you named in your inertia gap).

| # | Type | Question you will answer | Why this type -- name the prove-program capability if gap-closing | Output label | Who consumes it | Does it close your gap? |
|---|------|-------------------------|------------------------------------------------------------------|--------------|-----------------|------------------------|
| E-01 | [websearch / intelligence / analysis / interview / prototype / custom] | [question] | [rationale] | [label] | [E-02 / EVALUATOR] | Yes / No |
| E-02 | [type] | [question] | [rationale] | [label] | [EVALUATOR] | Yes / No |

Your plan must have:
- >=2 different types -- no two rows the same
- At least one Yes in "Does it close your gap?"
- Every output label filled -- RUNNER needs these for the citation contracts

GATE-P: >=2 distinct types? At least one Yes? All output labels filled?
FAIL: Any requirement not met. Revise.

**PLANNER COMPLETE.**
Your plan order: [E-01 type -> E-02 type -> ...]
Your gap-closing experiment: [E-NN]
-> RUNNER receives: your ordered plan, your locked hypothesis, your inertia gap, and the per-block citation contract requirement below.

---

### RUNNER -- Your job: execute each experiment in plan order, carrying outputs forward verbatim.

**Entry check**: PLANNER COMPLETE confirmed.
FAIL: You execute any experiment without PLANNER COMPLETE present.

**Citation contract -- read before executing any experiment that consumes a prior output:**

Every experiment you run that consumes a prior output MUST embed the citation contract locally in its own INPUT section. Writing a global rule here does not satisfy the contract -- each consuming experiment's INPUT section must contain the contract clause and the verbatim text. The clause format is:

> Citation contract (local to this experiment): I am consuming [prior E-NN] output. I reproduce its exact text below. Pointer references ("see above", "per E-NN", "as found earlier") are prohibited in this INPUT section. Verbatim content:

FAIL (applies independently to each consuming experiment): Input section uses a pointer reference or does not contain the citation contract clause + verbatim blockquote.

---

**Experiment 1.**

GATE-E1-entry: PLANNER COMPLETE confirmed.

Your inputs:
INPUT: Your hypothesis (verbatim): [verbatim hypothesis text] | Your inertia gap (verbatim): [verbatim gap text]

Write one sentence: how do your hypothesis and inertia gap scope what you are looking for?

[Execute E-01.]

Name your output: E-01 output: [labeled finding -- write this precisely; Experiment 2 will reproduce this verbatim]

Record delivery: output label = "[plan label]" -- consumed by: [E-02 / EVALUATOR] -- delivered? Yes / No
FAIL: Delivery line absent or label mismatch.

**EXPERIMENT 1 COMPLETE.** E-01 summary: [one line]. -> Consumed by: [E-02 / EVALUATOR].

---

**Experiment 2.**

GATE-E2-entry: EXPERIMENT 1 COMPLETE confirmed.
FAIL: You begin Experiment 2 without EXPERIMENT 1 COMPLETE present.

Your inputs -- citation contract (local to this experiment): I am consuming E-01 output. I reproduce its exact text below. Pointer references ("see above", "per E-01", "as found in Experiment 1") are prohibited in this INPUT section. Verbatim content:

> [exact text from E-01 output -- the labeled finding quoted directly, not described or paraphrased]

Write one sentence: how does E-01's finding -- a finding prove-topic could not have produced through a single-topic campaign -- change what you are looking for here?

[Execute E-02.]

Name your output: E-02 output: [labeled finding]

Record delivery: output label = "[plan label]" -- consumed by: [EVALUATOR] -- delivered? Yes / No
FAIL: Delivery line absent or label mismatch.

**EXPERIMENT 2 COMPLETE.** E-02 summary: [one line]. -> Consumed by: EVALUATOR.

---

[Add Experiment 3, 4, etc. as needed. Each must:
1. Confirm prior COMPLETE at entry
2. INPUT section with citation contract clause + verbatim blockquote
3. Execute
4. Name the labeled output
5. Record delivery line with delivered? boolean
6. EXPERIMENT N COMPLETE marker with routing
The citation contract is local to each experiment's INPUT section -- not satisfied by the global instruction above.]

**RUNNER COMPLETE.**
All outputs: E-01 [type], E-02 [type], ...
-> EVALUATOR receives: all labeled experiment outputs. This multi-experiment feed-forward chain is the core prove-program capability that justify its use over prove-topic.

---

### EVALUATOR -- Your job: assess the findings, calibrate confidence, synthesize, and extract principles.

**Entry check**: RUNNER COMPLETE confirmed.
FAIL: You begin any EVALUATOR section without RUNNER COMPLETE present.

---

**What did each experiment actually deliver?**

Fill in from the delivery lines above. Do not infer.

| Experiment | Output label from plan | Delivered? | Who consumed it |
|-----------|------------------------|------------|-----------------|
| E-01 | [label] | Yes / No | [step] |
| E-02 | [label] | Yes / No | [step] |

FAIL: Ledger absent or any Delivered? contradicts the delivery line.

---

**What did you find?**

| # | Finding | Which experiment | How confident | Why that confidence level |
|---|---------|-----------------|---------------|--------------------------|
| F-01 | [finding] | E-01 | high / medium / low | [e.g., "2 independent sources", "single source not replicated"] |
| F-02 | [finding] | E-02 | high / medium / low | [basis] |

Write at least 2 findings. Write the evidence basis for each.
FAIL: Fewer than 2 findings or evidence basis absent from any row.

---

**Are your confidence levels calibrated? [EVALUATOR gate before synthesis]**

### GATE-CAL -- Confidence Calibration Check [Findings -> Synthesis Boundary]

You are at the findings -> synthesis boundary. Before you write what you learned, check: did you actually differentiate your confidence levels, or did you assign the same label to every finding?

**The pass condition is differentiation, not presence.** FAIL condition: all findings rated HIGH (uniform high), or all MEDIUM, or all LOW -- any uniform pattern fails regardless of which label you chose.

- List the distinct confidence values in your findings: [e.g., "high (F-01), medium (F-02)"]
- Count of distinct values: [N]
- At least 2 distinct values? YES / NO
- **GATE-CAL result: PASS / FAIL**

FAIL: Your findings all carry the same confidence level. Return to your findings table. Re-examine each finding's evidence basis independently. Assign confidence levels that reflect real differences in evidence strength. Re-evaluate GATE-CAL.
STOP: You may not write synthesis until GATE-CAL result is PASS.

---

**What did you actually learn?**

**Entry check**: GATE-CAL PASS confirmed.

What you thought going in: [your hypothesis verbatim from FRAMER]
What you actually learned: [confirm, refine, or refute -- this must differ from your hypothesis. Answer the research question using your findings.]

Did the gap-closing experiment deliver a finding prove-topic could not have delivered? Yes / No + one sentence naming the prove-program capability that made it possible.

Which downstream Signal artifact should receive these findings? [name it: draft spec / scout brief / topic plan / topic story]

FAIL: "What you actually learned" copies your hypothesis verbatim. Rewrite it.
FAIL: Inertia gap closure verdict absent or does not state Yes or No.

---

**What principles do you take away?**

| Label | Principle | Source finding |
|-------|-----------|---------------|
| P-01 | [When X, do Y -- or Always Z] | F-NN |
| P-02 | [When X, do Y -- or Always Z] | F-NN |

At least 2. Specific and actionable, not truisms. Cite the finding each comes from.
FAIL: Fewer than 2, principles are generic truisms, or source finding column blank.

---

### Write the artifact.

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

## Rubric coverage summary (v6 -- 160 pts)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 hypothesis-first | FRAMER Phase 1 before PLANNER | Step 2 before Step 3 | "What do you believe?" before experiment design | Phase 1 before Phase 1B | FRAMER before PLANNER |
| C-02 plan >=2 types + rationale | PLANNER Phase 1B table + GATE-P | Step 3 table + GATE-3 | Experiment plan table + GATE-P | Phase 1B table + GATE-P | PLANNER table + GATE-P |
| C-03 feed-forward | RUNNER per-block contract | Per-step contract (Steps 4-7) | Per-experiment contract (Q&A frame) | Phase 2 per-block contract | RUNNER per-block contract |
| C-04 synthesis contrast | EVALUATOR two fields + FAIL | Step 8 two fields + GATE-8 FAIL | "What you actually learned" two fields + FAIL | Phase 3C two fields + GATE-S FAIL | EVALUATOR two fields + FAIL |
| C-05 Qx.md format at path | Artifact section | Step 10 Artifact | Artifact section | Artifact section | Artifact section |
| C-06 principles >=2 labeled | EVALUATOR principles table + FAIL | Step 9 + FAIL | Numbered P-01/P-02 + FAIL | Phase 3D + FAIL | EVALUATOR principles table + FAIL |
| C-07 confidence per finding | EVALUATOR findings table | Step 7 findings table | "How confident are you" column | Phase 3B table | EVALUATOR findings table |
| C-08 flexibility beyond prove-topic | FRAMER Phase 0 gap + Closes gap? | Step 1 gap + Closes gap? column | Gap declaration + Closes gap? | Capability map + Closes gap? column | Gap declaration + Closes gap? |
| C-09 falsification | GATE-1 Condition B + FAIL | GATE-2A Condition B + FAIL | "What would change your mind" + GATE-H B + FAIL | GATE-1 Condition B + FAIL | GATE-1 Condition B + FAIL |
| C-10 cross-namespace | EVALUATOR cross-namespace note | Step 8 cross-namespace note | "Which Signal artifact" field | Phase 3C cross-namespace note | EVALUATOR cross-namespace note |
| C-11 audit ledger | EVALUATOR ledger + FAIL | Step 6 ledger + FAIL | "What did each experiment deliver?" ledger + FAIL | Phase 3A ledger + FAIL | EVALUATOR ledger + FAIL |
| C-12 COMPLETE markers | FRAMER/PLANNER/RUNNER/EVALUATOR + EXPERIMENT N COMPLETE per block | STEP N COMPLETE per experiment | "E-N complete" per experiment | EXPERIMENT N COMPLETE per block | FRAMER/PLANNER/RUNNER COMPLETE + EXPERIMENT N COMPLETE |
| C-13 inertia bookending | Phase 0 gap + Closes gap? + EVALUATOR closure | Step 1 gap + Closes gap? + Step 8 closure | Gap declaration + Closes gap? + "did gap-closing experiment deliver" | Capability map + GATE-0 + every boundary note + Phase 3C closure + GATE-CAL map reference | Gap declaration + GATE-0 + every role note + EVALUATOR closure |
| C-14 plan output routing | Output label + Consumed by columns | Output label + Consumed by columns | Output label + Who consumes it columns | Output label + Consumed by columns | Output label + Who consumes it columns |
| C-15 delivery boolean | Contract delivery per block + FAIL | Contract delivery per step + FAIL | "Record delivery" per experiment + FAIL | Contract delivery per block + FAIL | Contract delivery per experiment + FAIL |
| C-16 gap-to-plan column | Closes gap? column | Closes gap? column | "Does it close your gap?" column | Closes gap? column | "Does it close your gap?" column |
| C-17 verbatim quotation | RUNNER per-block blockquote + FAIL | Per-step blockquote + FAIL | Per-experiment blockquote + FAIL | Phase 2 per-block blockquote + FAIL | RUNNER per-experiment blockquote + FAIL |
| C-18 inter-phase GATE | GATE-0, GATE-FRAMER, GATE-1, GATE-P, GATE-PLANNER, GATE-E1, GATE-E2, GATE-RUNNER, GATE-CAL | GATE-1 (Step 1), GATE-2A (Step 2->3), GATE-3, GATE-7A, GATE-8 | GATE-0, GATE-H, GATE-P, GATE-CAL, GATE-S (>=2 named gates) | GATE-0, GATE-1, GATE-P, GATE-CAL, GATE-S (all named, all at phase transitions) | GATE-0, GATE-1, GATE-P, GATE-E1, GATE-E2, GATE-CAL (>=2 named gates) |
| C-19 inline FAIL | PASS -- FAIL per criterion throughout all roles | PASS -- FAIL per step throughout procedure | PASS -- FAIL conditions throughout Q&A sections | PASS -- FAIL per criterion throughout phases | PASS -- FAIL per criterion throughout all roles |
| **C-20 atomic gate** | **PASS -- GATE-1 boolean table, A AND B conjunction, FAIL if partial** | **PASS -- GATE-2A boolean table, A AND B conjunction, FAIL if partial** | **PASS -- GATE-H boolean table, A AND B conjunction, FAIL if partial** | **PASS -- GATE-1 boolean table, A AND B conjunction, FAIL if partial** | **PASS -- GATE-1 boolean table, A AND B conjunction, FAIL if partial** |
| **C-21 calibration gate** | **PASS -- GATE-CAL with explicit "FAIL: all findings rated HIGH" uniform-label pattern** | **PASS -- GATE-7A with explicit uniform-label FAIL condition** | **PASS -- GATE-CAL with explicit uniform-label FAIL condition** | **PASS -- GATE-CAL with explicit "FAIL: all findings rated HIGH" + capability map reference** | **PASS -- GATE-CAL with explicit uniform-label FAIL condition** |
| **C-22 per-block citation** | **PASS -- citation contract clause embedded in each RUNNER consumer block INPUT section + FAIL** | **PASS -- citation contract clause embedded in each consuming step INPUT section + FAIL** | **PASS -- citation contract clause embedded in each consuming experiment INPUT section + FAIL** | **PASS -- citation contract clause embedded in each Phase 2 consumer block INPUT section + FAIL** | **PASS -- citation contract clause embedded in each RUNNER consumer experiment INPUT section + FAIL** |

**Projected v6 scores:**

| Variation | Primary axis | C-20 | C-21 | C-22 | Expected ceiling |
|-----------|-------------|------|------|------|-----------------|
| V-01 | Role sequence (4-role FRAMER/PLANNER/RUNNER/EVALUATOR) | PASS | PASS | PASS | 160/160 |
| V-02 | Output format (numbered procedure Steps) | PASS | PASS | PASS | 160/160 |
| V-03 | Phrasing register (second-person imperative + Q&A) | PASS | PASS | PASS | 160/160 |
| V-04 | Lifecycle emphasis + inertia framing | PASS | PASS | PASS | 160/160 |
| V-05 | Role sequence + phrasing register + inertia framing | PASS | PASS | PASS | 160/160 |

**R6 conclusion**: The 160/160 ceiling is structurally robust across role partitions (3-role vs 4-role), output formats (phase/role labels vs numbered steps), grammatical registers (third-person vs second-person imperative), and inertia framing salience (minimal vs capability-map-as-spine). The three atomic patterns introduced in v5 (C-20 conjunction gate, C-21 calibration gate, C-22 per-block citation contract) are surface-form-agnostic -- they require structural placement (gate table before planning, calibration check before synthesis, contract clause in each consumer INPUT) not specific terminology or register.
