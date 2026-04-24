---
skill: prove-program
date: 2026-03-15
source: QU5 simplification of prove-program-variate-R7-2026-03-15.md (V-02 base)
reduction: V-02 1547w -> 1183w (24%)
---

You are running a research program for: **{{topic}}**

Research question: {{research_question}}

Complete all phases in order. Every gate is a hard stop; advance only when its pass condition is fully met. Use the section headers below exactly as labeled.

---

### Phase 0 -- Inertia Gap

The inertia competitor is **prove-topic**: single-topic intelligence -> analysis -> interview -> synthesis scoped to one Signal topic. prove-program is warranted only when the research question exceeds prove-topic's capability.

State the inertia gap as a single sentence naming the specific capability prove-topic lacks for this question. Acceptable gap types: cross-namespace scope, external domain not reachable by Signal skills, multi-hypothesis structure, or custom experiment type unavailable in prove-topic.

**Inertia gap:** [one sentence naming the specific prove-topic limitation]

**GATE-0:** The gap statement names a specific capability prove-topic lacks. If prove-topic is sufficient for this question, stop here and use it.

**FAIL:** Gap statement is generic ("more flexibility needed", "broader scope") rather than naming the specific limitation.

---

### Phase 1 -- Hypothesis

State a single, testable belief before naming or planning any experiment. The hypothesis must be in positive form.

**Hypothesis:** [one sentence, positive form]

**Falsification:** [the specific evidence that would cause you to reject this hypothesis -- concrete, not a vague qualifier]

---

### GATE-1 -- Atomic Hypothesis + Falsification Conjunction

Both must be TRUE. Partial satisfaction is FAIL.

**Condition A -- Hypothesis distinctness:** Hypothesis differs from the research question in specificity or framing. A restatement in different words fails.
Condition A: TRUE / FALSE -- [in what way does the hypothesis differ?]

**Condition B -- Falsification present:** A falsification criterion is explicitly stated as a concrete piece of evidence that would cause rejection.
Condition B: TRUE / FALSE -- [what is the stated falsification criterion?]

**GATE-1 result: PASS** (A AND B = TRUE) / **FAIL** (A = FALSE OR B = FALSE)

**FAIL:** Hypothesis is a restatement of the question, or falsification criterion is absent. Return to Phase 1. Rewrite and re-evaluate GATE-1.

---

### Phase 1B -- Experiment Plan

**E-01:** Type -- [type]. Question -- [question]. Rationale -- [why this type]. Output label -- [label]. Consumed by -- [E-02 / synthesis]. Closes gap? -- Yes / No.

**E-02:** Type -- [type]. Question -- [question]. Rationale -- [why this type]. Output label -- [label]. Consumed by -- [synthesis]. Closes gap? -- Yes / No.

**Plan rules:**
- At least 2 distinct types required. No two experiments may share the same type.
- At least one experiment must close the inertia gap (Closes gap? = Yes).
- Every output label must be filled.

**GATE-P:** Confirm: (a) >=2 distinct types; (b) at least one Closes gap? = Yes; (c) every output label filled.

**FAIL:** Fewer than 2 distinct types, no experiment closes the gap, or any output label missing.

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

**INPUT -- citation contract (local to this block):** This block consumes E-01 output. Reproduce the exact text of E-01's labeled finding in full below. The following pointer forms are PROHIBITED in this INPUT section: "see above", "per E-01", "as found in E-01", or any paraphrase. Embed verbatim:

[exact text from E-01's labeled output -- quoted in full, not described or summarized]

[One sentence: how E-01's finding constrains or refocuses this experiment.]

[Execute experiment.]

**E-02 output:** [labeled finding]

**Contract delivery:** output label = "[plan label]" -- consumed by: synthesis -- delivered? Yes / No

**FAIL:** Contract delivery line absent or output label mismatch.

**EXPERIMENT 2 COMPLETE.** Summary: [one line]. -> Consumed by: synthesis.

---

[For each additional experiment: begin with entry condition confirming prior COMPLETE marker; INPUT section must contain the citation contract clause and verbatim content of the consumed output; execute; write labeled output; write contract delivery line; write EXPERIMENT N COMPLETE marker. The citation contract is written locally in each consumer experiment's INPUT section -- not in a shared global note.]

**ALL EXPERIMENTS COMPLETE.** -> Synthesis receives all labeled outputs.

---

### Feed-Forward Audit

**E-01 audit:** Plan label -- [label] | Delivered? -- Yes / No | Consumed by -- [E-02 / synthesis]
**E-02 audit:** Plan label -- [label] | Delivered? -- Yes / No | Consumed by -- synthesis

Populate from contract delivery lines only.

**FAIL:** Any audit entry contradicts the corresponding contract delivery line.

---

### Findings

>=2 labeled findings required. Evidence basis required per finding.

**F-01:** [finding text] -- Source: E-01 -- Confidence: high / medium / low -- Evidence basis: [basis]

**F-02:** [finding text] -- Source: E-02 -- Confidence: high / medium / low -- Evidence basis: [basis]

**FAIL:** Fewer than 2 findings, or evidence basis absent from any finding.

---

### GATE-CAL -- Confidence Calibration Check

Pass condition: >=2 distinct confidence values. All findings rated the same level = FAIL.

Distinct confidence values in findings: [e.g., "high (F-01), medium (F-02)"]
Count of distinct values: [N]
At least 2 distinct values? YES / NO

**GATE-CAL result: PASS / FAIL**

**FAIL:** All findings carry the same confidence level. Return to Findings. Examine each evidence basis independently. Differentiate confidence assignments. Re-evaluate GATE-CAL.

---

### Synthesis

**[Confirm GATE-CAL PASS before writing this section.]**

**What we thought:** [verbatim hypothesis from Phase 1]

**What we actually learned:** [confirm, refine, or refute -- must differ from hypothesis text; answer the research question]

**Inertia gap closure:** Did the gap-closing experiment produce a finding prove-topic could not have produced? Yes / No + one sentence of evidence.

**Cross-namespace routing:** Which Signal artifact downstream should receive these findings? [draft spec / scout brief / topic plan / topic story]

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
