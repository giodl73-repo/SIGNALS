---
skill: quest-variate
skill_target: prove-program
date: 2026-03-15
round: 7
rubric: prove-program-rubric-v6-2026-03-15.md
status: DRAFT
---

# prove-program -- Variations R7 (V-01 through V-05)

**Context**: R6 confirmed 160/160 ceiling across role sequence (4-role), numbered-step output format, conversational phrasing register, lifecycle+inertia combined, and triple combined (role+phrasing+inertia). v6 rubric unchanged.
**R7 purpose**: Verify ceiling stability across structural axes not yet explored: 2-role consolidation, pure-prose output (no tables), formal specification register (RFC MUST/SHALL), and new combinatorial pressure.
**R7 single-axis**: V-01 (2-role model), V-02 (pure-prose output, no tables), V-03 (formal spec register: MUST/SHALL/PROHIBITED).
**R7 combined**: V-04 (pure-prose format + maximum gate density), V-05 (3-role model + formal spec register + inertia framing).
**Prediction**: All five score 160/160, demonstrating that C-20/C-21/C-22 survive 2-role consolidation, tableless formatting, formal register, and new combinatorial axes.

---

## V-01 -- Role sequence axis: 2-role model (ARCHITECT -> EXECUTOR)

**Variation axis:** Role sequence -- extreme consolidation from the R6 4-role model to 2 roles. ARCHITECT owns phases 0 through 1B (inertia gap, hypothesis, GATE-1, experiment plan). EXECUTOR owns phases 2 through 5 (all experiments, GATE-CAL, synthesis, principles, artifact). The single inter-role handoff is the only mandatory boundary. GATE-1 (atomic conjunction) is the only gate that separates the two roles, making it structurally the sole architectural checkpoint.
**Hypothesis:** Collapsing from 4 roles to 2 -- with GATE-1 as the single role handoff -- does not weaken C-20 compliance; instead, GATE-1 becomes a harder structural invariant because it is the only allowed path by which EXECUTOR receives inputs. A 2-role model with one hard gate is structurally equivalent to a 4-role model with 4 gates for C-20 purposes.

---

You are running a research program for: **{{topic}}**

Research question: {{research_question}}

Two roles execute in strict sequence: ARCHITECT then EXECUTOR. ARCHITECT must produce a COMPLETE handoff before EXECUTOR may begin. No role may write outside its designated sections.

| Role | Writes | May not write |
|------|--------|---------------|
| ARCHITECT | Inertia gap, hypothesis, falsification, GATE-1 evaluation, experiment plan | Experiments, findings, synthesis, principles |
| EXECUTOR | All experiments, feed-forward ledger, findings, GATE-CAL, synthesis, principles, artifact | Hypothesis, inertia gap, experiment plan |

---

### ARCHITECT

#### Phase 0 -- Inertia Gap

The inertia competitor is **prove-topic**: single-topic intelligence -> analysis -> interview -> synthesis scoped to one Signal topic. prove-program is required only when the research question exceeds prove-topic's capability.

Inertia gap: [what prove-topic cannot handle here -- name a specific capability limitation: cross-namespace scope, external domain not in Signal, multi-hypothesis structure, or custom experiment type not in prove-topic's set]

GATE-0: Inertia gap must name a specific capability prove-topic lacks for this question.
FAIL: Gap statement is generic ("more flexibility", "broader scope") rather than naming the specific limitation.
STOP: If prove-topic is sufficient for this question, stop here and use it.

---

#### Phase 1 -- Hypothesis Pre-Commitment

State a specific, testable belief before any experiment is named or designed.

Hypothesis: [what you believe is true -- one sentence, positive form]
Falsification: [what specific evidence would cause you to reject this hypothesis]

---

#### GATE-1 -- Atomic Hypothesis + Falsification Conjunction [ARCHITECT -> EXECUTOR Boundary]

This is the single inter-role gate. Both conditions must be TRUE. Partial satisfaction is FAIL.

| Condition | Description | Result |
|-----------|-------------|--------|
| A -- Hypothesis distinctness | The hypothesis differs from the research question in specificity or framing. A restatement of the question in different words does not satisfy Condition A. | TRUE / FALSE |
| B -- Falsification present | A falsification criterion is explicitly stated: a specific piece of evidence that would cause the researcher to reject the hypothesis. A vague qualifier ("if evidence doesn't support it") does not satisfy Condition B. | TRUE / FALSE |

GATE-1 result: **PASS** (A AND B = TRUE) / **FAIL** (A = FALSE OR B = FALSE)

FAIL: Hypothesis is a restatement of the question, or falsification criterion is absent or vague. Return to Phase 1. Rewrite and re-evaluate GATE-1.
STOP: ARCHITECT COMPLETE requires GATE-1 PASS. Do not emit ARCHITECT COMPLETE until GATE-1 result is PASS.

---

#### Phase 1B -- Experiment Plan

| # | Type | Question answered | Rationale | Output label | Consumed by | Closes gap? |
|---|------|------------------|-----------|--------------|-------------|-------------|
| E-01 | [websearch / intelligence / analysis / interview / prototype / custom] | [question] | [why this type, not another] | [label] | [E-02 / EXECUTOR synthesis] | Yes / No |
| E-02 | [type] | [question] | [rationale] | [label] | [EXECUTOR synthesis] | Yes / No |

Rules:
- >=2 distinct types -- no two rows share the same type
- >=1 row: Closes gap? = Yes
- All Output label cells filled -- EXECUTOR uses these to enforce per-block citation contracts

GATE-P: (a) >=2 distinct types confirmed; (b) >=1 Closes gap? = Yes; (c) all Output labels filled.
FAIL: <2 distinct types, no Yes in Closes gap?, or any Output label blank.
STOP: Do not emit ARCHITECT COMPLETE until GATE-P also PASS.

---

**ARCHITECT COMPLETE**
GATE-1 result: PASS
GATE-P result: PASS
Hypothesis (locked): [verbatim]
Falsification criterion (locked): [verbatim]
Inertia gap (locked): [verbatim]
Experiment plan: [E-01 type -> E-02 type -> ...]
Gap-closing experiment: [E-NN]
-> EXECUTOR receives: hypothesis, falsification, inertia gap, ordered experiment plan, output labels

---

### EXECUTOR

GATE-ARCHITECT: Confirm ARCHITECT COMPLETE before executing any experiment.
FAIL: Any EXECUTOR content written without ARCHITECT COMPLETE marker present.

**Per-block citation contract -- governs all consumer experiment blocks:**

Every experiment that consumes a prior experiment's output MUST embed the citation contract locally in its own INPUT section. A global preamble does not satisfy this requirement; each consumer block's INPUT section must carry the contract clause and verbatim content independently.

Format for every consumer INPUT section:
> Citation contract (local to this block): reproduce the exact output text of [upstream label]. Pointer references ("see above", "per E-NN", "as found above", or any paraphrase of the prior finding) are PROHIBITED in this INPUT section. Embed verbatim:

---

#### E-01 -- [Type from plan]

GATE-E01: ARCHITECT COMPLETE confirmed.

INPUT: Hypothesis -- [verbatim hypothesis from ARCHITECT Phase 1] | Inertia gap -- [verbatim gap from ARCHITECT Phase 0]

[One sentence: how hypothesis + inertia gap scope this experiment's focus.]

[Execute experiment.]

E-01 output: [labeled finding -- write this precisely; E-02 must embed this verbatim]

Contract delivery: output label = "[plan label]" -- consumed by: [E-02 / synthesis] -- delivered? Yes / No
FAIL: Contract delivery line absent or output label does not match ARCHITECT plan.

**EXPERIMENT 1 COMPLETE**
Produced: E-01 -- [one-line summary]
-> Consumed by: [E-02 / synthesis]

---

#### E-02 -- [Type from plan]

GATE-E02: EXPERIMENT 1 COMPLETE confirmed before executing.
FAIL: E-02 begins without EXPERIMENT 1 COMPLETE marker present.

INPUT -- citation contract (local to this block): This block consumes E-01 output. Reproduce the exact text of E-01's labeled finding below. Pointer references ("see above", "per E-01", "as found in E-01") are PROHIBITED in this INPUT section. Embed verbatim:

> [exact text from E-01 output -- the labeled finding quoted directly]

[One sentence: how E-01's finding constrains or refocuses this experiment.]

[Execute experiment.]

E-02 output: [labeled finding]

Contract delivery: output label = "[plan label]" -- consumed by: [synthesis] -- delivered? Yes / No
FAIL: Contract delivery line absent or output label mismatch.

**EXPERIMENT 2 COMPLETE**
Produced: E-02 -- [one-line summary]
-> Consumed by: synthesis

---

[Add E-03+ as needed. Every consumer block requires: (1) GATE-E{N} confirming prior COMPLETE marker; (2) INPUT section with local citation contract clause + verbatim blockquote; (3) execution; (4) labeled output; (5) contract delivery line; (6) EXPERIMENT N COMPLETE marker. The citation contract travels with each consuming block's INPUT section, not in a shared global rule.]

**EXECUTOR -- ALL EXPERIMENTS COMPLETE**
All outputs: E-01 [type], E-02 [type], ...
-> Synthesize from labeled outputs

---

#### Feed-Forward Audit Ledger

| Experiment | Plan output label | Delivered? | Consumed by |
|-----------|------------------|------------|-------------|
| E-01 | [plan label] | Yes / No | [E-02 / synthesis] |
| E-02 | [plan label] | Yes / No | [synthesis] |

Populate from Contract delivery lines in experiments. Do not infer values not stated in experiment blocks.
FAIL: Ledger absent, or any row contradicts the corresponding Contract delivery line.

---

#### Findings

| # | Finding | Source | Confidence | Evidence basis |
|---|---------|--------|------------|----------------|
| F-01 | [finding text] | E-01 | high / medium / low | [basis] |
| F-02 | [finding text] | E-02 | high / medium / low | [basis] |

Minimum 2 findings. Evidence basis required per row.
FAIL: Fewer than 2 findings, or any evidence basis cell blank.

---

#### GATE-CAL -- Confidence Calibration Check [Findings -> Synthesis Boundary]

This gate enforces calibration. Presence of confidence labels is necessary but not sufficient.

**GATE-CAL pass condition**: The findings table contains at least two distinct confidence values. All findings labeled the same level -- regardless of which level -- fail this gate.

GATE-CAL evaluation:
- Distinct confidence values present: [list -- e.g., "high (F-01), medium (F-02)"]
- Count of distinct values: [N]
- At least 2 distinct values? YES / NO
- **GATE-CAL result: PASS / FAIL**

FAIL: All findings carry the same confidence level (all HIGH, all MEDIUM, or all LOW). Return to Findings. Re-examine each finding's evidence basis independently. Differentiate confidence assignments. Re-evaluate GATE-CAL.
STOP: Do not write synthesis until GATE-CAL result is PASS.

---

#### Synthesis

**[Confirm GATE-CAL PASS before writing synthesis.]**

What we thought: [hypothesis verbatim from ARCHITECT Phase 1]
What we actually learned: [confirm, refine, or refute -- must differ from hypothesis text; answer the research question]

Inertia gap closure: Did the gap-closing experiment produce a finding prove-topic could not have produced? Yes / No + one sentence of evidence.

Cross-namespace routing: Which Signal artifact downstream should receive these findings? [draft spec / scout brief / topic plan / topic story -- name it]

FAIL: "What we actually learned" copies the hypothesis verbatim, or inertia gap closure verdict absent.

---

#### Principles

| Label | Principle | Source finding |
|-------|-----------|----------------|
| P-01 | [When X, do Y -- or Always Z] | F-NN |
| P-02 | [When X, do Y -- or Always Z] | F-NN |

Minimum 2 principles. No generic truisms. Source finding required per row.
FAIL: Fewer than 2, principles are generic truisms, or any source finding cell blank.

---

#### Artifact

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

## V-02 -- Output format axis: pure prose (no tables anywhere)

**Variation axis:** Output format -- zero tables. All structured information is expressed as flowing paragraphs with bolded labels, inline notation, and section headers. Findings are labeled prose blocks. Principles are labeled prose statements. The plan is an ordered prose list. Gates are prose blocks with bold pass/fail lines. This tests whether the 160/160 ceiling is achievable when the tabular scaffolding common to R1-R6 is entirely absent.
**Hypothesis:** The ceiling is format-agnostic at the element level: prose formatting with consistently applied labels produces the same criterion coverage as tabular formatting, because the rubric tests for structural properties (gate enforcement, per-block contracts, calibration non-uniformity) not for the presence of markdown tables.

---

You are running a research program for: **{{topic}}**

Research question: {{research_question}}

Complete all phases in order. Every gate is a hard stop; advance only when its pass condition is fully met. Use the section headers below exactly as labeled.

---

### Phase 0 -- Inertia Gap

The inertia competitor is **prove-topic**: single-topic intelligence -> analysis -> interview -> synthesis scoped to one Signal topic. prove-program is warranted only when the research question exceeds prove-topic's capability.

State the inertia gap as a single sentence that names the specific capability prove-topic lacks for this question. Acceptable gap types: cross-namespace scope, external domain not reachable by Signal skills, multi-hypothesis structure, or custom experiment type unavailable in prove-topic.

**Inertia gap:** [one sentence naming the specific prove-topic limitation]

**GATE-0:** The gap statement names a specific capability prove-topic lacks. If prove-topic is sufficient for this question, stop here and use it.

**FAIL:** Gap statement is generic ("more flexibility needed", "broader scope") rather than naming the specific limitation.

---

### Phase 1 -- Hypothesis

State a single, specific, testable belief before naming or planning any experiment. The hypothesis must be in positive form (what you believe is true, not what you suspect is false).

**Hypothesis:** [one sentence, positive form -- what you believe is true]

**Falsification:** [what specific evidence would cause you to reject this hypothesis -- not a vague qualifier, but a concrete piece of evidence]

---

### GATE-1 -- Atomic Hypothesis + Falsification Conjunction

This gate has exactly two conditions. Both must be TRUE. One TRUE and one absent or FALSE is FAIL -- the gate is conjunctive, not a checklist.

**Condition A -- Hypothesis distinctness:** The hypothesis differs from the research question in specificity or framing. A restatement of the question in different words fails Condition A.

Condition A result: TRUE / FALSE -- [brief justification: in what way does the hypothesis differ?]

**Condition B -- Falsification present:** A falsification criterion is explicitly stated as a concrete piece of evidence that would cause rejection of the hypothesis.

Condition B result: TRUE / FALSE -- [brief justification: what is the stated falsification criterion?]

**GATE-1 result: PASS** (A AND B = TRUE) / **FAIL** (A = FALSE OR B = FALSE)

**FAIL:** Hypothesis is a restatement of the question, or falsification criterion is absent. Return to Phase 1. Rewrite and re-evaluate GATE-1.

**STOP:** Do not proceed to Phase 1B until GATE-1 result is PASS.

---

### Phase 1B -- Experiment Plan

**[Confirm GATE-1 PASS before writing this section.]**

List all experiments in execution order. For each experiment, state: its sequence number (E-NN), the experiment type (websearch / intelligence / analysis / interview / prototype / custom), the question it will answer, the rationale for that type over alternatives, the output label that uniquely names its finding, what downstream step consumes it, and whether it closes the inertia gap.

**E-01:** Type -- [type]. Question -- [question]. Rationale -- [why this type]. Output label -- [label]. Consumed by -- [E-02 / synthesis]. Closes gap? -- Yes / No.

**E-02:** Type -- [type]. Question -- [question]. Rationale -- [why this type]. Output label -- [label]. Consumed by -- [synthesis]. Closes gap? -- Yes / No.

**Plan rules:**
- At least 2 distinct types are required. No two experiments may share the same type.
- At least one experiment must close the inertia gap (Closes gap? = Yes).
- Every output label must be filled; EXECUTOR uses these in per-block citation contracts.

**GATE-P:** Confirm: (a) >=2 distinct types; (b) at least one Closes gap? = Yes; (c) every output label filled.

**FAIL:** Fewer than 2 distinct types, no experiment closes the gap, or any output label missing.

**STOP:** Do not execute any experiment until GATE-P PASS.

---

### Experiment E-01 -- [Type]

**Entry condition:** GATE-P PASS confirmed.

**INPUT:** Hypothesis -- [verbatim hypothesis from Phase 1] | Inertia gap -- [verbatim gap from Phase 0]

[One sentence: how hypothesis and inertia gap together scope what this experiment seeks.]

[Execute experiment.]

**E-01 output:** [labeled finding -- write this precisely; E-02 will embed it verbatim]

**Contract delivery:** output label = "[plan label]" -- consumed by: [E-02 / synthesis] -- delivered? Yes / No

**FAIL:** Contract delivery line absent or output label does not match Phase 1B plan.

**EXPERIMENT 1 COMPLETE.** Summary: [one line]. -> Consumed by: [E-02 / synthesis].

---

### Experiment E-02 -- [Type]

**Entry condition:** EXPERIMENT 1 COMPLETE confirmed.

**FAIL:** E-02 content written without EXPERIMENT 1 COMPLETE marker present.

**INPUT -- citation contract (local to this block):** This block consumes E-01 output. Reproduce the exact text of E-01's labeled finding in full below. The following pointer forms are PROHIBITED in this INPUT section: "see above", "per E-01", "as found in E-01", or any paraphrase of the prior finding. Embed verbatim content:

[exact text from E-01's labeled output -- quoted in full, not described or summarized]

[One sentence: how E-01's finding constrains or refocuses this experiment.]

[Execute experiment.]

**E-02 output:** [labeled finding]

**Contract delivery:** output label = "[plan label]" -- consumed by: [synthesis] -- delivered? Yes / No

**FAIL:** Contract delivery line absent or output label mismatch.

**EXPERIMENT 2 COMPLETE.** Summary: [one line]. -> Consumed by: synthesis.

---

[For each additional experiment: begin with entry condition confirming prior COMPLETE marker; INPUT section must contain the citation contract clause and verbatim content of the consumed output; execute; write labeled output; write contract delivery line; write EXPERIMENT N COMPLETE marker. The citation contract is written locally in each consumer experiment's INPUT section -- not in a shared global note.]

**ALL EXPERIMENTS COMPLETE.** -> Synthesis receives all labeled outputs.

---

### Feed-Forward Audit

For each experiment, record: what output label was promised in the plan, whether delivery was confirmed in the experiment's contract delivery line, and what step consumed it.

**E-01 audit:** Plan label -- [label] | Delivered? -- Yes / No | Consumed by -- [E-02 / synthesis]
**E-02 audit:** Plan label -- [label] | Delivered? -- Yes / No | Consumed by -- [synthesis]

Populate from contract delivery lines only. Do not infer.

**FAIL:** Any audit entry contradicts the corresponding contract delivery line.

---

### Findings

Write at least 2 labeled findings. For each finding, state: the finding text, which experiment produced it, a confidence level (high / medium / low), and the evidence basis for that confidence level.

**F-01:** [finding text] -- Source: E-01 -- Confidence: high / medium / low -- Evidence basis: [basis]

**F-02:** [finding text] -- Source: E-02 -- Confidence: high / medium / low -- Evidence basis: [basis]

**FAIL:** Fewer than 2 findings, or evidence basis absent from any finding.

---

### GATE-CAL -- Confidence Calibration Check

**[This gate runs before synthesis. Do not write synthesis until GATE-CAL PASS.]**

State every distinct confidence value present in your findings. Count them. Confirm that at least 2 distinct values are present.

**The pass condition is differentiation, not presence.** Assigning HIGH to every finding is not calibration -- it is uniform assertion. FAIL condition: all findings rated HIGH (or all MEDIUM, or all LOW).

Distinct confidence values in findings: [e.g., "high (F-01), medium (F-02)"]
Count of distinct values: [N]
At least 2 distinct values? YES / NO

**GATE-CAL result: PASS / FAIL**

**FAIL:** All findings carry the same confidence level. Return to findings. Examine each evidence basis independently. Differentiate confidence assignments. Re-evaluate GATE-CAL.

**STOP:** Do not write synthesis until GATE-CAL result is PASS.

---

### Synthesis

**[Confirm GATE-CAL PASS before writing this section.]**

**What we thought:** [verbatim hypothesis from Phase 1]

**What we actually learned:** [confirm, refine, or refute the hypothesis -- must differ from the hypothesis text; answer the research question with the findings]

**Inertia gap closure:** Did the gap-closing experiment produce a finding prove-topic could not have produced? Yes / No + one sentence of evidence.

**Cross-namespace routing:** Which Signal artifact downstream should receive these findings? [draft spec / scout brief / topic plan / topic story -- name it]

**FAIL:** "What we actually learned" copies the hypothesis verbatim, or inertia gap closure verdict absent.

---

### Principles

Write at least 2 labeled, actionable principles abstracted from the findings. Each must state a specific guideline (when X, do Y -- or always Z). No generic truisms. Each must cite its source finding.

**P-01:** [When X, do Y] -- Source: F-NN

**P-02:** [When X, do Y] -- Source: F-NN

**FAIL:** Fewer than 2 principles, any principle is a generic truism, or any source finding missing.

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

## V-03 -- Phrasing register axis: formal specification language (RFC MUST/SHALL/PROHIBITED)

**Variation axis:** Phrasing register -- the entire skill is written in formal specification language using RFC 2119-style normative terms: MUST, MUST NOT, SHALL, SHALL NOT, SHOULD, PROHIBITED. The executor is referred to as "the executor" (third person), not "you" or a named role. Gates are specification constraints, not procedural instructions. This tests whether the ceiling is achievable with a register at the opposite pole from the conversational second-person used in R6 V-03.
**Hypothesis:** Formal specification register does not weaken C-20 or C-22 compliance; the normative terms MUST and PROHIBITED express the same structural invariants as imperative or conversational phrasings, and the atomic conjunction structure of C-20 is preserved identically by requiring "Condition A MUST be TRUE AND Condition B MUST be TRUE."

---

**SPECIFICATION: prove-program skill execution**

**Subject**: {{topic}}
**Research question**: {{research_question}}

The executor MUST complete all phases in the order specified. A gate SHALL be treated as a hard constraint, not an advisory check. The executor MUST NOT advance past a gate until its pass condition is fully satisfied.

---

### Section 1 -- Inertia Gap Declaration

**1.1** The inertia competitor is **prove-topic**: single-topic intelligence -> analysis -> interview -> synthesis scoped to one Signal topic. The executor MUST declare a specific capability limitation of prove-topic before proceeding.

**1.2** Inertia gap declaration:

> Inertia gap: [one sentence naming the specific capability prove-topic cannot provide for this research question]

**GATE-0 (Section 1 -> Section 2 constraint):**
- The inertia gap declaration MUST name a specific capability limitation.
- FAIL condition: the gap statement is generic (e.g., "more flexibility", "broader scope") rather than naming the specific limitation.
- The executor MUST NOT proceed to Section 2 if GATE-0 is not satisfied.
- Alternative path: if prove-topic is sufficient for the research question, the executor SHALL stop and use prove-topic instead.

---

### Section 2 -- Hypothesis Pre-Commitment

**2.1** The executor MUST state a single testable hypothesis before any experiment is named or designed. The hypothesis SHALL be expressed in positive form (what is believed to be true, not what is suspected to be false).

**2.2** Hypothesis:

> Hypothesis: [one sentence, positive form]
> Falsification criterion: [the specific evidence that would cause rejection of this hypothesis]

---

### GATE-1 -- Atomic Hypothesis + Falsification Conjunction (Section 2 -> Section 3 Constraint)

**GATE-1 is an atomic conjunction. Both conditions MUST be TRUE. Partial satisfaction is PROHIBITED.**

| Condition | Specification | Result |
|-----------|---------------|--------|
| A -- Hypothesis distinctness | The hypothesis MUST differ from the research question in specificity or framing. A restatement of the question in different words SHALL NOT satisfy Condition A. | TRUE / FALSE |
| B -- Falsification present | A falsification criterion MUST be explicitly stated as a specific piece of evidence that would cause rejection of the hypothesis. A vague qualifier (e.g., "if evidence does not support it") SHALL NOT satisfy Condition B. | TRUE / FALSE |

**GATE-1 evaluation:**
- Condition A result: TRUE / FALSE -- [justification]
- Condition B result: TRUE / FALSE -- [justification]
- **GATE-1 result: PASS** (A AND B = TRUE) / **FAIL** (A = FALSE OR B = FALSE or absent)

**FAIL condition:** hypothesis is a restatement of the research question, or falsification criterion is absent or vague. The executor MUST return to Section 2, rewrite the hypothesis and/or falsification criterion, and re-evaluate GATE-1.

**The executor SHALL NOT proceed to Section 3 until GATE-1 result is PASS.**

---

### Section 3 -- Experiment Plan

**3.1** The executor MUST produce a complete experiment plan before executing any experiment.

**3.2** [Confirm GATE-1 PASS before producing this section.]

| # | Type | Question answered | Rationale | Output label | Consumed by | Closes gap? |
|---|------|------------------|-----------|--------------|-------------|-------------|
| E-01 | [websearch / intelligence / analysis / interview / prototype / custom] | [question] | [why this type, not another] | [label] | [E-02 / Section 5] | Yes / No |
| E-02 | [type] | [question] | [rationale] | [label] | [Section 5] | Yes / No |

**3.3 Plan constraints (all MUST be satisfied):**
- The plan MUST contain experiments of >=2 distinct types. No two plan rows SHALL share the same type.
- At least one experiment MUST close the inertia gap (Closes gap? = Yes).
- Every Output label cell MUST be filled. These labels SHALL govern the per-block citation contracts in Section 4.

**GATE-P (Section 3 -> Section 4 constraint):**
- FAIL condition: fewer than 2 distinct types, no experiment closes the gap, or any Output label cell is blank.
- The executor SHALL NOT execute any experiment until GATE-P is satisfied.

---

### Section 4 -- Experiment Execution

**4.1 Per-block citation contract (applies to all consumer experiment blocks):**

Every experiment block that consumes a prior experiment's output MUST embed the citation contract locally in its own INPUT subsection. A global preamble SHALL NOT satisfy this requirement. The citation contract MUST travel with the consuming block's INPUT subsection, not with a shared global rule.

PROHIBITED in any consumer INPUT subsection: pointer references of the form "see above", "per E-NN", "as found in E-NN", or any paraphrase of the upstream finding. The verbatim text of the upstream output MUST be reproduced in full.

---

#### 4.1 -- Experiment E-01

**Entry constraint:** GATE-P PASS MUST be confirmed before E-01 executes.

**INPUT:**
- Hypothesis (verbatim): [verbatim hypothesis from Section 2]
- Inertia gap (verbatim): [verbatim gap from Section 1]
- [One sentence: how hypothesis and inertia gap constrain the scope of this experiment.]

[Execute experiment.]

**E-01 output:** [labeled finding -- the executor SHALL write this precisely; it is the upstream content for any consumer block]

**Contract delivery:** output label = "[plan label]" -- consumed by: [E-02 / Section 5] -- delivered? Yes / No

FAIL condition: contract delivery line absent or output label does not match Section 3 plan.

**E-01 COMPLETE.** Output produced: [one-line summary]. Consumed by: [E-02 / Section 5].

---

#### 4.2 -- Experiment E-02

**Entry constraint:** E-01 COMPLETE MUST be confirmed before E-02 executes.

FAIL condition: E-02 content produced without E-01 COMPLETE marker confirmed.

**INPUT -- citation contract (local to this block):**

This block consumes E-01 output. The executor MUST reproduce the exact text of E-01's labeled finding below. The following forms are PROHIBITED in this INPUT subsection: "see above", "per E-01", "as found in E-01", or any paraphrase.

> [exact text from E-01 output -- the labeled finding reproduced verbatim in full]

[One sentence: how E-01's finding constrains the scope of E-02.]

[Execute experiment.]

**E-02 output:** [labeled finding]

**Contract delivery:** output label = "[plan label]" -- consumed by: [Section 5] -- delivered? Yes / No

FAIL condition: contract delivery line absent or output label mismatch with Section 3 plan.

**E-02 COMPLETE.** Output produced: [one-line summary]. Consumed by: Section 5.

---

[Each additional experiment MUST: confirm prior COMPLETE marker as entry constraint; embed the citation contract in its INPUT subsection with verbatim upstream content; execute; produce a labeled output; write a contract delivery line; emit a COMPLETE marker. The citation contract SHALL be embedded locally per consuming block, not in a shared global rule.]

**ALL EXPERIMENTS COMPLETE.** Section 5 receives all labeled outputs.

---

### Section 5 -- Findings and Synthesis

#### 5.1 -- Feed-Forward Audit Ledger

| Experiment | Plan output label | Delivered? | Consumed by |
|-----------|------------------|------------|-------------|
| E-01 | [plan label] | Yes / No | [E-02 / Section 5] |
| E-02 | [plan label] | Yes / No | [Section 5] |

The executor MUST populate this ledger from contract delivery lines in Section 4. Values MUST NOT be inferred.

FAIL condition: ledger absent, or any Delivered? value contradicts the corresponding contract delivery line.

---

#### 5.2 -- Findings

| # | Finding | Source | Confidence | Evidence basis |
|---|---------|--------|------------|----------------|
| F-01 | [finding text] | E-01 | high / medium / low | [basis] |
| F-02 | [finding text] | E-02 | high / medium / low | [basis] |

The findings table MUST contain at least 2 findings. The evidence basis cell MUST be populated for every row.

FAIL condition: fewer than 2 findings, or any evidence basis cell blank.

---

#### GATE-CAL -- Confidence Calibration Constraint (Section 5.2 -> Section 5.3)

**GATE-CAL enforces calibration. Presence of confidence labels is necessary but SHALL NOT be treated as sufficient.**

**GATE-CAL pass condition:** The findings table MUST contain at least two distinct confidence values. All findings labeled the same level SHALL NOT satisfy this gate.

**FAIL condition: all findings rated HIGH (or all MEDIUM, or all LOW).** The uniform-label pattern explicitly fails this gate regardless of which level is applied uniformly.

**GATE-CAL evaluation:**
- Distinct confidence values present: [list -- e.g., "high (F-01), medium (F-02)"]
- Count of distinct values: [N]
- At least 2 distinct values: YES / NO
- **GATE-CAL result: PASS / FAIL**

**FAIL:** The executor MUST return to Section 5.2. Each finding's evidence basis MUST be re-examined independently. Confidence assignments MUST be differentiated to reflect real differences in evidence strength. GATE-CAL MUST be re-evaluated.

**The executor SHALL NOT produce Section 5.3 until GATE-CAL result is PASS.**

---

#### 5.3 -- Synthesis

**[GATE-CAL PASS MUST be confirmed before this subsection is produced.]**

**What the executor believed going in:** [hypothesis verbatim from Section 2]

**What was actually learned:** [confirm, refine, or refute the hypothesis -- MUST differ from hypothesis text; MUST answer the research question]

**Inertia gap closure:** Did the gap-closing experiment produce a finding prove-topic could not have produced? Yes / No + one sentence of evidence.

**Cross-namespace routing:** Which Signal artifact SHALL receive these findings downstream? [draft spec / scout brief / topic plan / topic story]

FAIL condition: "What was actually learned" reproduces the hypothesis verbatim, or inertia gap closure verdict absent.

---

#### 5.4 -- Principles

| Label | Principle | Source finding |
|-------|-----------|----------------|
| P-01 | [When X, do Y -- or Always Z] | F-NN |
| P-02 | [When X, do Y -- or Always Z] | F-NN |

The principles table MUST contain at least 2 principles. Principles SHALL be specific and actionable; generic truisms SHALL NOT satisfy this requirement. The source finding cell MUST be populated per row.

FAIL condition: fewer than 2 principles, any principle is a generic truism, or any source finding cell blank.

---

### Section 6 -- Artifact

The executor SHALL write: `simulations/prove/research/{{topic}}-research-{{date}}.md`

Frontmatter SHALL be present:
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

## V-04 -- Combined: Pure-prose format + maximum gate density (output format + lifecycle emphasis)

**Variation axes:** Output format (pure prose, no tables) + Lifecycle emphasis (maximum gate density: every phase transition has a named gate; GATE-0, GATE-1, GATE-P, GATE-E{N}, GATE-CAL each receives a prose block with named FAIL condition). This tests whether gate-dense lifecycle enforcement survives tableless formatting -- the two constraints pull in opposite directions (tables support rapid gate evaluation; prose forces gate logic into flowing blocks).
**Hypothesis:** Gate density and prose format are independently compatible with the 160/160 ceiling; when combined, the absence of tables forces gate conditions to be stated more verbosely in prose, which increases rather than decreases rubric compliance because every FAIL condition must be named explicitly in full sentences rather than abbreviated in table cells.

---

You are running a research program for: **{{topic}}**

Research question: {{research_question}}

Complete all phases in order. Every labeled gate is a hard stop. You may not cross a phase boundary until the gate at that boundary passes. Write all output in prose with labeled sections -- no markdown tables appear in this document.

---

### Phase 0 -- Inertia Gap

The inertia competitor for this skill is **prove-topic**: single-topic intelligence -> analysis -> interview -> synthesis scoped to one Signal topic. prove-program is warranted only when your research question requires capabilities prove-topic cannot provide.

Declare the inertia gap now as a single sentence that names the specific capability prove-topic lacks for this research question. The gap must be a named limitation -- cross-namespace scope, external domain, multi-hypothesis structure, or a custom experiment type unavailable in prove-topic. A generic statement ("more flexibility", "broader scope") does not name a specific limitation.

**Inertia gap:** [one sentence naming the specific prove-topic limitation for this question]

**GATE-0 -- Inertia Gap Validity:** The inertia gap statement names a specific prove-topic capability limitation for this research question. **FAIL:** Gap statement is generic and does not name the specific limitation. If prove-topic is sufficient for this question, stop here and use it instead.

---

### Phase 1 -- Hypothesis

State your hypothesis now, before naming or planning any experiment. Your hypothesis is a single specific, testable belief expressed in positive form -- what you believe is true, not what you fear might be false.

**Hypothesis:** [one sentence, positive form -- what you believe is true]

**Falsification criterion:** [the specific piece of evidence that would cause you to reject this hypothesis -- name it concretely, not as a vague qualifier like "if evidence doesn't support it"]

**GATE-1 -- Atomic Hypothesis + Falsification Conjunction [Phase 1 -> Phase 1B boundary]:** This gate enforces two conditions simultaneously as a single conjunction -- both must be true. Condition A: your hypothesis differs from the research question in specificity or framing (a restatement in different words fails). Condition B: your falsification criterion is explicitly stated as a concrete piece of evidence. **FAIL:** hypothesis is a restatement of the question, or falsification criterion is absent or vague. The gate is conjunctive: one condition TRUE and one FALSE is FAIL, not partial credit. State both conditions and the result: Condition A -- TRUE / FALSE; Condition B -- TRUE / FALSE; GATE-1 result -- PASS / FAIL. Do not proceed to Phase 1B until GATE-1 PASS.

---

### Phase 1B -- Experiment Plan

**[GATE-1 PASS confirmed before writing this section.]**

List your experiments in execution order. For each experiment, write a labeled block stating: the sequence label (E-NN), the experiment type (websearch / intelligence / analysis / interview / prototype / custom), the specific question the experiment will answer, the rationale for choosing that type over available alternatives, a unique output label that names the finding this experiment will produce, what step will consume that output, and whether this experiment closes the inertia gap.

**E-01:** Type -- [type]. Question -- [question]. Rationale -- [why this type]. Output label -- [label]. Consumed by -- [E-02 or synthesis]. Closes gap? -- Yes / No.

**E-02:** Type -- [type]. Question -- [question]. Rationale -- [why this type]. Output label -- [label]. Consumed by -- [synthesis]. Closes gap? -- Yes / No.

Your plan must satisfy three requirements: (1) at least 2 distinct experiment types -- no two experiments may share the same type; (2) at least one experiment closes the inertia gap; (3) every output label is filled in before execution begins.

**GATE-P -- Plan Completeness [Phase 1B -> Phase 2 boundary]:** The plan satisfies all three requirements. **FAIL:** fewer than 2 distinct types, no experiment closes the gap, or any output label blank. Re-examine and rewrite before proceeding. Do not execute any experiment until GATE-P PASS.

---

### Phase 2 -- Experiments

**Phase 2 entry condition:** GATE-P PASS confirmed.

Every experiment block that consumes an earlier experiment's output must embed the citation contract locally in its own INPUT paragraph. You may not satisfy this requirement with a global note above the experiments; the contract clause and verbatim content must appear in each consumer block's INPUT paragraph individually.

---

**Experiment E-01 -- [Type]**

GATE-E01 entry: GATE-P PASS confirmed before executing.

INPUT: Your hypothesis (verbatim) -- [verbatim hypothesis from Phase 1]. Your inertia gap (verbatim) -- [verbatim gap from Phase 0]. Write one sentence: how do hypothesis and inertia gap scope what this experiment seeks?

[Execute experiment.]

E-01 output: [labeled finding -- write this precisely; E-02 will embed it verbatim]

Contract delivery: output label = "[plan label]" -- consumed by: [E-02 / synthesis] -- delivered? Yes / No

**FAIL:** Contract delivery absent or output label does not match Phase 1B plan.

**E-01 COMPLETE.** Summary: [one line]. -> Consumed by: [E-02 / synthesis].

---

**Experiment E-02 -- [Type]**

GATE-E02 entry: E-01 COMPLETE confirmed before executing. **FAIL:** E-02 begins without E-01 COMPLETE marker present.

INPUT -- citation contract (local to this block): This block consumes E-01 output. Reproduce the exact text of E-01's labeled finding in full below. The following forms are prohibited in this INPUT paragraph: "see above", "per E-01", "as found in E-01", or any paraphrase. The verbatim content must appear here:

[exact text from E-01's labeled output -- reproduced in full, not described or paraphrased]

Write one sentence: how does E-01's finding change what you are looking for in this experiment?

[Execute experiment.]

E-02 output: [labeled finding]

Contract delivery: output label = "[plan label]" -- consumed by: [synthesis] -- delivered? Yes / No

**FAIL:** Contract delivery absent or output label mismatch.

**E-02 COMPLETE.** Summary: [one line]. -> Consumed by: synthesis.

---

[For each additional experiment: confirm prior COMPLETE as GATE-E{N} entry; write the citation contract clause and verbatim prior output in the INPUT paragraph; execute; produce labeled output; write contract delivery; write COMPLETE marker. The contract clause is embedded per consuming block's INPUT paragraph, not in a shared preamble.]

**ALL EXPERIMENTS COMPLETE.** Synthesis receives all labeled outputs.

---

### Phase 3 -- Findings

Write at least 2 labeled findings. For each finding, state the finding in a complete sentence, identify which experiment produced it, assign a confidence level (high, medium, or low), and explain the evidence basis for that confidence level in one sentence.

**F-01:** [finding statement]. Source: E-01. Confidence: high / medium / low. Evidence basis: [basis].

**F-02:** [finding statement]. Source: E-02. Confidence: high / medium / low. Evidence basis: [basis].

**FAIL:** fewer than 2 findings, or evidence basis absent from any finding.

---

**GATE-CAL -- Confidence Calibration [Phase 3 -> Phase 4 boundary]:** This gate enforces differentiation. Listing confidence levels is not the same as calibrating them. The pass condition requires at least 2 distinct confidence values across all findings. **FAIL condition: all findings rated HIGH (or all MEDIUM, or all LOW).** State the distinct values present (e.g., "high for F-01, medium for F-02"), count them, confirm at least 2 distinct values, and state the GATE-CAL result: PASS or FAIL. If FAIL, return to Phase 3 and re-examine each evidence basis independently to produce differentiated confidence assignments. Do not proceed to Phase 4 until GATE-CAL PASS.

---

### Phase 4 -- Synthesis

**[GATE-CAL PASS confirmed before writing this section.]**

**What we thought:** [hypothesis verbatim from Phase 1]

**What we actually learned:** [confirm, refine, or refute the hypothesis -- must differ from hypothesis text and answer the research question using your findings]

**Inertia gap closure:** Did the gap-closing experiment produce a finding prove-topic could not have produced? Yes or No, plus one sentence of evidence.

**Cross-namespace routing:** Which Signal artifact downstream should receive these findings? Name it: draft spec, scout brief, topic plan, or topic story.

**FAIL:** "What we actually learned" copies the hypothesis verbatim, or inertia gap closure verdict absent.

---

### Phase 5 -- Principles

Write at least 2 labeled, actionable principles drawn from the findings. Each principle must state a specific guideline. Cite the source finding for each.

**P-01:** [When X, do Y -- or Always Z]. Source: F-NN.

**P-02:** [When X, do Y -- or Always Z]. Source: F-NN.

**FAIL:** fewer than 2 principles, any principle is a generic truism, or any source finding missing.

---

### Phase 6 -- Artifact

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

## V-05 -- Combined: 3-role model + formal spec register + inertia framing (role sequence + phrasing register + inertia framing)

**Variation axes:** Role sequence (3-role model: STRATEGIST, INVESTIGATOR, JUDGE) + Phrasing register (formal spec: MUST/SHALL/PROHIBITED) + Inertia framing (prove-topic named as benchmark at every phase boundary, not only Phase 0). prove-topic appears in three places: the initial capability map, the GATE-1 handoff (hypothesis must address a gap prove-topic cannot close), and the synthesis inertia gap closure verdict. This is the deepest combinatorial pressure in R7.
**Hypothesis:** The 160/160 ceiling survives maximum combinatorial pressure (3 axes simultaneously) because the atomic conjunction gate (C-20), calibration gate (C-21), and per-block citation contracts (C-22) are structural properties independent of role granularity, register formality, and inertia framing depth. Each axis operates on orthogonal dimensions; stacking three axes produces additive formatting variation without removing any structural invariant required for C-20/C-21/C-22.

---

**SPECIFICATION: prove-program execution -- 3-role model**

**Subject**: {{topic}}
**Research question**: {{research_question}}

Three roles execute in strict sequence: STRATEGIST -> INVESTIGATOR -> JUDGE. Each role MUST confirm the prior role's COMPLETE marker before beginning. Role boundaries are enforced by hard gates. The inertia competitor **prove-topic** is consulted at every role boundary as a named benchmark.

---

### Role Declarations

| Role | Sections owned | MUST NOT write |
|------|---------------|----------------|
| STRATEGIST | Inertia gap, capability map, hypothesis, GATE-1, experiment plan | Experiments, findings, synthesis, principles |
| INVESTIGATOR | All experiments and contract delivery lines | Hypothesis, plan, findings table, synthesis, principles |
| JUDGE | Feed-forward ledger, findings, GATE-CAL, synthesis, principles, artifact | Hypothesis, plan, experiments |

---

### STRATEGIST

#### S-1 -- Inertia Gap and Capability Map

**S-1.1** The inertia competitor is **prove-topic**. The STRATEGIST MUST produce both an inertia gap declaration and a capability map before committing to a hypothesis.

**S-1.2** prove-topic capability map:

| prove-topic can | prove-topic cannot |
|-----------------|-------------------|
| Run intelligence, analysis, interview, synthesis on a named Signal topic | Span multiple namespaces in a single research run |
| Draw on scout, draft, flow, trace artifacts for a topic | Query external domains not covered by Signal skills |
| Chain analysis -> interview -> synthesis within one topic | Support multi-hypothesis programs |
| | Execute custom experiment types outside its fixed set |

**S-1.3** Inertia gap: [one sentence naming the specific row in the "cannot" column that applies to this research question]

**GATE-S0:** The inertia gap names a specific row from the "cannot" column. **FAIL:** gap statement is generic or references a "can" row. The STRATEGIST MUST NOT advance if prove-topic is sufficient for this question.

---

#### S-2 -- Hypothesis Pre-Commitment

**S-2.1** The STRATEGIST MUST state a single testable hypothesis before naming any experiment. The hypothesis SHALL be in positive form.

**S-2.2** The hypothesis MUST address the inertia gap: it must assert something that prove-topic's "cannot" constraint prevents prove-topic from confirming or refuting alone.

> **Hypothesis:** [one sentence, positive form -- addresses the named inertia gap]
> **Falsification criterion:** [specific evidence that would cause rejection of this hypothesis]

---

#### GATE-1 -- Atomic Hypothesis + Falsification Conjunction [STRATEGIST -> INVESTIGATOR boundary]

**GATE-1 is an atomic conjunction. Both conditions MUST be TRUE. The gate MUST NOT be treated as two independent advisory checks.**

| Condition | Specification | Result |
|-----------|---------------|--------|
| A -- Hypothesis distinctness | The hypothesis MUST differ from the research question in specificity or framing. A restatement of the question SHALL NOT satisfy Condition A. | TRUE / FALSE |
| B -- Falsification present | A falsification criterion MUST be explicitly stated as a specific piece of evidence. A vague qualifier SHALL NOT satisfy Condition B. | TRUE / FALSE |

**GATE-1 evaluation:**
- Condition A: TRUE / FALSE -- [how does the hypothesis differ from the question?]
- Condition B: TRUE / FALSE -- [what is the stated falsification criterion?]
- **GATE-1 result: PASS** (A AND B = TRUE) / **FAIL** (A = FALSE OR B = FALSE or absent)

**FAIL:** STRATEGIST MUST return to S-2, rewrite, and re-evaluate GATE-1. STRATEGIST MUST NOT emit STRATEGIST COMPLETE until GATE-1 PASS.

---

#### S-3 -- Experiment Plan

**[Confirm GATE-1 PASS before producing this section.]**

| # | Type | Question answered | Rationale | Output label | Consumed by | Closes gap? | prove-topic could run? |
|---|------|------------------|-----------|--------------|-------------|-------------|----------------------|
| E-01 | [websearch / intelligence / analysis / interview / prototype / custom] | [question] | [why this type, not another] | [label] | [E-02 / JUDGE] | Yes / No | Yes / No |
| E-02 | [type] | [question] | [rationale] | [label] | [JUDGE] | Yes / No | Yes / No |

The "prove-topic could run?" column names whether prove-topic could have executed this experiment type for a single-topic question. At least one row MUST show No.

**Plan constraints (all MUST be satisfied):**
- >=2 distinct types; no two rows SHALL share the same type
- >=1 row: Closes gap? = Yes (the experiment addressing S-1 inertia gap)
- All Output label cells MUST be filled
- >=1 row: prove-topic could run? = No

**GATE-P:** All four constraints satisfied. **FAIL:** any constraint not met.

---

**STRATEGIST COMPLETE**
GATE-1 result: PASS | GATE-P result: PASS
Hypothesis (locked): [verbatim]
Falsification criterion (locked): [verbatim]
Inertia gap (locked): [verbatim]
Experiment plan: [E-01 type -> E-02 type -> ...]
Gap-closing experiment: [E-NN]
prove-topic benchmark: [verbatim row from "cannot" column]
-> INVESTIGATOR receives: hypothesis, falsification, inertia gap, experiment plan, output labels, prove-topic benchmark

---

### INVESTIGATOR

**GATE-STRATEGIST:** STRATEGIST COMPLETE MUST be confirmed before INVESTIGATOR executes any experiment. **FAIL:** Any experiment executed without STRATEGIST COMPLETE confirmed.

**Per-block citation contract (governs all INVESTIGATOR consumer experiment blocks):**

Every experiment that consumes a prior experiment's output MUST embed the citation contract locally in its own INPUT subsection. A global preamble SHALL NOT satisfy this requirement. The contract clause and verbatim content MUST appear in each consuming experiment's INPUT subsection independently. The following forms are PROHIBITED in any consumer INPUT subsection: "see above", "per E-NN", "as found in E-NN", or any paraphrase of the upstream finding.

---

#### I-1 -- Experiment E-01

**Entry constraint:** STRATEGIST COMPLETE confirmed. GATE-P PASS confirmed.

**INPUT:**
- Hypothesis (verbatim): [verbatim from STRATEGIST S-2]
- Inertia gap (verbatim): [verbatim from STRATEGIST S-1]
- prove-topic benchmark: [verbatim "cannot" row from STRATEGIST S-1]
- Scope note: [one sentence: how hypothesis, gap, and benchmark together focus this experiment]

[Execute experiment.]

**E-01 output:** [labeled finding -- the INVESTIGATOR SHALL write this precisely; it is the upstream content for any consuming block]

**Contract delivery:** output label = "[plan label]" -- consumed by: [E-02 / JUDGE] -- delivered? Yes / No

FAIL condition: contract delivery absent or output label does not match STRATEGIST plan.

**I-1 COMPLETE.** Output: E-01 -- [one-line summary]. -> Consumed by: [E-02 / JUDGE].

---

#### I-2 -- Experiment E-02

**Entry constraint:** I-1 COMPLETE MUST be confirmed before I-2 executes.

FAIL condition: I-2 begins without I-1 COMPLETE marker confirmed.

**INPUT -- citation contract (local to this block):**

This block consumes E-01 output. The INVESTIGATOR MUST reproduce the exact text of E-01's labeled finding below. The following forms are PROHIBITED in this INPUT subsection: "see above", "per E-01", "as found in E-01", or any paraphrase.

> [exact text from E-01 output -- the labeled finding reproduced verbatim]

prove-topic benchmark (verbatim): [verbatim "cannot" row from STRATEGIST S-1]

[One sentence: how E-01's finding and the prove-topic benchmark together scope this experiment.]

[Execute experiment.]

**E-02 output:** [labeled finding]

**Contract delivery:** output label = "[plan label]" -- consumed by: [JUDGE] -- delivered? Yes / No

FAIL condition: contract delivery absent or output label mismatch.

**I-2 COMPLETE.** Output: E-02 -- [one-line summary]. -> Consumed by: JUDGE.

---

[Each additional experiment MUST: confirm prior COMPLETE as entry constraint; embed citation contract in INPUT subsection with verbatim prior output AND verbatim prove-topic benchmark; execute; produce labeled output; write contract delivery line; write COMPLETE marker. The citation contract SHALL be embedded per consuming block, not in a global rule.]

**INVESTIGATOR COMPLETE**
All outputs: E-01 [type], E-02 [type], ...
-> JUDGE receives: all labeled outputs, hypothesis verbatim, prove-topic benchmark

---

### JUDGE

**GATE-INVESTIGATOR:** INVESTIGATOR COMPLETE MUST be confirmed before JUDGE executes. **FAIL:** Any JUDGE section produced without INVESTIGATOR COMPLETE confirmed.

#### J-1 -- Feed-Forward Audit Ledger

| Experiment | Plan output label | Delivered? | Consumed by |
|-----------|------------------|------------|-------------|
| E-01 | [plan label] | Yes / No | [E-02 / JUDGE] |
| E-02 | [plan label] | Yes / No | [JUDGE] |

The JUDGE MUST populate this ledger from contract delivery lines in INVESTIGATOR blocks. Values MUST NOT be inferred.

FAIL condition: ledger absent, or any Delivered? value contradicts the corresponding contract delivery line.

---

#### J-2 -- Findings

| # | Finding | Source | Confidence | Evidence basis |
|---|---------|--------|------------|----------------|
| F-01 | [finding text] | E-01 | high / medium / low | [basis] |
| F-02 | [finding text] | E-02 | high / medium / low | [basis] |

The findings table MUST contain at least 2 findings. The evidence basis cell MUST be populated per row.

FAIL condition: fewer than 2 findings, or any evidence basis cell blank.

---

#### GATE-CAL -- Confidence Calibration Constraint [J-2 -> J-3 boundary]

**GATE-CAL enforces calibration. Presence of confidence labels SHALL NOT be treated as sufficient.**

**GATE-CAL pass condition:** The findings table MUST contain at least 2 distinct confidence values. All findings labeled the same level -- regardless of which level -- SHALL NOT pass this gate. **FAIL condition: all findings rated HIGH (or all MEDIUM, or all LOW).**

GATE-CAL evaluation:
- Distinct confidence values present: [list]
- Count of distinct values: [N]
- At least 2 distinct values: YES / NO
- **GATE-CAL result: PASS / FAIL**

**FAIL:** The JUDGE MUST return to J-2. Each finding's evidence basis MUST be re-examined independently. Confidence assignments MUST be differentiated. GATE-CAL MUST be re-evaluated. The JUDGE SHALL NOT produce J-3 until GATE-CAL PASS.

---

#### J-3 -- Synthesis

**[GATE-CAL PASS MUST be confirmed before this section is produced.]**

**What we believed going in:** [hypothesis verbatim from STRATEGIST S-2]

**What we actually learned:** [confirm, refine, or refute the hypothesis -- MUST differ from hypothesis text; MUST answer the research question]

**prove-topic benchmark verdict:** The gap-closing experiment was [E-NN]. It produced the following finding: [finding text]. Could prove-topic have produced this finding for a single-topic question? Yes / No. One sentence of evidence: [evidence].

**Cross-namespace routing:** Which Signal artifact downstream SHALL receive these findings? [draft spec / scout brief / topic plan / topic story]

FAIL condition: "What we actually learned" reproduces the hypothesis verbatim; or benchmark verdict absent.

---

#### J-4 -- Principles

| Label | Principle | Source finding |
|-------|-----------|----------------|
| P-01 | [When X, do Y -- or Always Z] | F-NN |
| P-02 | [When X, do Y -- or Always Z] | F-NN |

The JUDGE MUST produce at least 2 principles. Principles SHALL be specific and actionable. Generic truisms SHALL NOT satisfy this requirement. The source finding cell MUST be populated per row.

FAIL condition: fewer than 2 principles, any principle is a generic truism, or any source finding cell blank.

---

#### J-5 -- Artifact

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
