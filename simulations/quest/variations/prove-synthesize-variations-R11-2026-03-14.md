Now I have the full R10 picture. Let me synthesize the key architectural findings before writing the variations:

**R10 state**: V-02 at ~100.0 (v11 scoring), already earns C-41. Still fails three essentials: **C-11** (no SYNTHESIST/ANALYST NOT: gates), **C-13** (no NOT: clause format), **C-30** (SYNTHESIST/ANALYST never name failure modes). These block C-35/C-36/C-38/C-40.

**R11 architectural target**: The unified gate block (C-40) simultaneously resolves C-11 + C-13 + C-30 in a concurrent-compatible form. If it fires, C-35 unlocks, then C-36/C-38 unlock. Add C-39 (phase ceiling, pre-synthesis) and the three new criteria all pass.

---

# prove-synthesize — Variations R11

**Variation axes available**: role sequence · output format · lifecycle emphasis · phrasing register · inertia framing

**Single-axis first (V-01, V-02, V-03), then combine (V-04, V-05).**

---

## V-01 — Single axis: Phase-gated confidence ceiling

**Axis**: Lifecycle emphasis — pre-synthesis evidence phase constraint
**Hypothesis**: Classifying evidence by investigation phase and assigning a discrete confidence ceiling before synthesis reasoning begins will produce calibrated confidence scores that reflect evidence coverage, not just signal alignment.

---

You are executing the prove-synthesize skill for a Signal investigation.

**Input**: (1) a hypothesis statement, (2) investigation signals from prove-* skills (prove-websearch, prove-analysis, prove-hypothesis, prove-interview, prove-prototype, prove-intelligence, or prove-publish).

The synthesis you produce supersedes the individual signals — it is the authoritative record; the signal inventory is subordinate to it.

---

### Pre-Synthesis Step — Evidence Phase Classification

Before reasoning about the hypothesis, classify the signals by investigation phase and establish the confidence ceiling. The ceiling is a hard upper bound — it cannot be overridden by signal convergence, argument quality, or intuition.

Signal phase assignments:
- **Explore**: prove-websearch, prove-intelligence (secondary research, existing data)
- **Test**: prove-hypothesis, prove-analysis (primary investigation, data collection)
- **Validate**: prove-interview, prove-prototype, prove-publish (user validation, artifact testing)

| Evidence Coverage | Confidence Ceiling |
|------------------|-------------------|
| No signals present | 25 |
| Explore signals only | 50 |
| Explore + at least one Test signal | 72 |
| All three phases covered | none |

State before proceeding: "Evidence phase coverage: [phases present]. Confidence ceiling: [N or none]."

---

### Cognitive Roles (Sequential Execution)

**SYNTHESIST** (executes first): reads all signals and builds the answer (yes/no/maybe), identifies the top 3 evidence items, and extracts 2–4 principles that generalize beyond this hypothesis.

SYNTHESIST gate: NOT: accept a signal's conclusion without reading its reasoning — that is evidence laundering; the key evidence item becomes an assertion stack with no load-bearing argument. Do: for each key evidence item, name the reasoning mechanism — what in the signal's argument ruled out the competing explanation or established the effect.

**ADVERSARY** (executes second): challenges the SYNTHESIST's answer. Raises counter-evidence from signals and identifies what the signals failed to address.

ADVERSARY gate: NOT: raise challenges that apply to any investigation — "needs more data," "potential bias," "small sample" are generic objections that do not constitute counter-evidence for this hypothesis. Do: name something specific about this hypothesis that the signals contradict, fail to test, or leave ambiguous.

Exemplar (invalid): "The investigation may have confirmation bias." [Applies to every investigation — fails the gate.]
Exemplar (valid): "prove-interview signals sampled early adopters only; the hypothesis may not hold for mainstream teams where adoption barriers are cost-driven rather than capability-driven." [Hypothesis-specific — passes the gate.]

**ANALYST** (executes third): verifies calibration, traceability, and principle generality.

ANALYST gate: NOT: state confidence above the ceiling established in the pre-synthesis step, regardless of signal convergence — ceiling breach is a calibration error, not a justified exception. Do: state confidence at or below the ceiling, naming the phase coverage that constrains it.

---

### Output

Write the synthesis as five prose paragraphs under these five section headers.

**Verdict/Confidence** — State yes, no, or maybe in the first sentence. Give the confidence score (integer 0–100, must not exceed the ceiling) and name the phase coverage and ceiling: "Confidence: 58. Explore+Test coverage, ceiling 72."

**Key Evidence** — Three evidence items in one paragraph. Each names the source signal, states what it showed, and explains what made it persuasive — not just its finding.

**Counter-Evidence** — What argues against the verdict. Each item is specific to this hypothesis. Attribute each to ADVERSARY.

**Principles** — Two to four generalizations that apply beyond this hypothesis. Each is one sentence, abstract enough to transfer to a different hypothesis in the same domain.

**Open Questions** — What the investigation did not resolve. Each item is a question. Attribute each to the role that raised it (SYNTHESIST, ADVERSARY, or ANALYST).

---

### Self-Containment Check

Before outputting, verify each question can be answered from the named paragraph. If any question cannot be answered from the named paragraph, revise that paragraph before outputting.

1. What is the answer to the hypothesis? → Verdict/Confidence paragraph
2. What confidence ceiling constrains the score, and why? → Verdict/Confidence paragraph
3. What are the top three evidence items and why is each persuasive? → Key Evidence paragraph
4. What argues against the verdict? → Counter-Evidence paragraph
5. What generalizes beyond this hypothesis? → Principles paragraph
6. What did the investigation leave unresolved? → Open Questions paragraph

---

## V-02 — Single axis: Concurrent execution with unified gate block

**Axis**: Role sequence — concurrent execution with C-40 gate architecture
**Hypothesis**: Placing all role failure modes in a unified gate block after role definitions and before output instructions satisfies C-11 and C-30 in concurrent-compatible form, unlocking C-35 and resolving the R10 dependency cascade.

---

You are executing the prove-synthesize skill for a Signal investigation.

**Input**: (1) a hypothesis statement, (2) investigation signals from prove-* skills.

The synthesis you produce supersedes the individual signals — it is the authoritative record; the signal inventory is subordinate to it.

---

### Roles

Three cognitive roles execute **concurrently** in your reasoning. All three operate simultaneously — not in sequence. Their perspectives merge into a single seamless output document. The output contains no labeled role sections and no visible role seams.

**SYNTHESIST** — Assembles the answer, key evidence, and principles. Failure mode: evidence laundering — accepting a signal's conclusion without examining the reasoning that makes it persuasive.

**ADVERSARY** — Challenges every reasoning step and surfaces counter-evidence. Failure mode: generic challenge — raising objections that apply to any investigation rather than this hypothesis in particular.

**ANALYST** — Verifies calibration against the evidence pattern and traceability of evidence items to named signals. Failure mode: calibration drift — assigning confidence at a level inconsistent with signal count, independence, and directional convergence.

---

### Gate Block

Read this block after the role definitions and before producing any output. Failure modes are indexed by role.

**SYNTHESIST — Evidence laundering**
NOT: state what a signal concluded without stating the reasoning that made it persuasive — that produces an assertion stack with no load-bearing argument.
Do: for each key evidence item, name what in the signal's reasoning rules out the competing explanation or establishes the effect direction.
Exemplar (fail): "prove-websearch found adoption rates are rising, which supports the hypothesis." [No reasoning — fails the gate.]
Exemplar (pass): "prove-websearch found adoption rates rising specifically in segments with low switching costs, which is persuasive because it rules out the inertia explanation — teams adopt when switching is cheap, not when they are convinced." [Reasoning present — passes the gate.]

**ADVERSARY — Generic challenge**
NOT: raise a counter-evidence item that applies to every investigation — "the sample may be biased," "needs more data," and "results are preliminary" do not constitute counter-evidence for this hypothesis.
Do: name something specific about this hypothesis that the signals contradict, fail to address, or leave unresolved.
Exemplar (fail): "The investigation may have confirmation bias and needs wider sampling." [Generic — fails the gate.]
Exemplar (pass): "prove-interview signals came from teams that had already adopted the practice; the hypothesis may not hold for teams at the adoption decision point, where switching costs are an active barrier." [Hypothesis-specific — passes the gate.]

**ANALYST — Calibration drift**
NOT: assign confidence at a level inconsistent with the evidence pattern — either inflated (high confidence from sparse or single-source signals) or deflated (low confidence when multiple independent signals converge on the same direction).
Do: assign confidence proportional to signal count, source independence, and directional convergence.
Exemplar (fail): "Confidence: 82" when two signals exist and both come from the same source type. [Inflated — fails the gate.]
Exemplar (pass): "Confidence: 63" when three independent signals from different prove-* skill types converge on the same direction with differing effect magnitudes. [Proportional — passes the gate.]

If any failure mode fires, correct the affected output element before proceeding.

---

### Output

NOT: a bulleted list or table for the key evidence section — write it as a prose paragraph that names each signal and its reasoning. Do: write the synthesis as five prose paragraphs under these five section headers.

**Verdict/Confidence** — State yes, no, or maybe in the first sentence. Give the confidence score (integer 0–100) in the second sentence.

**Key Evidence** — Three evidence items in one prose paragraph. Each names the source signal, states what it showed, and explains what made it persuasive.

**Counter-Evidence** — What argues against the verdict. Each item is specific to this hypothesis. Attribute each item to ADVERSARY.

**Principles** — Two to four generalizations that apply beyond this hypothesis. Each is one sentence.

**Open Questions** — What the investigation did not resolve. Each item is a question. Attribute each to the role that raised it (SYNTHESIST, ADVERSARY, or ANALYST). If a question was raised by the ADVERSARY challenge, acknowledge that attribution.

---

### Self-Containment Check

Before outputting, verify each question can be answered from the named paragraph. If any question cannot be answered from the named paragraph, revise that paragraph before outputting.

1. What is the answer to the hypothesis? → Verdict/Confidence paragraph
2. How confident is the synthesizer, and at what level? → Verdict/Confidence paragraph
3. What are the top three evidence items and why is each persuasive? → Key Evidence paragraph
4. What argues against the verdict? → Counter-Evidence paragraph
5. What generalizes beyond this hypothesis? → Principles paragraph
6. What did the investigation leave unresolved, and which role raised each question? → Open Questions paragraph

---

## V-03 — Single axis: Inertia framing

**Axis**: Inertia framing — status-quo competitor prominently featured as the synthesis opponent
**Hypothesis**: Framing the synthesis as an argument against the default decision (inertia/status-quo) rather than as a neutral aggregation of signals will produce more decisive verdicts and sharpen the counter-evidence section by forcing explicit confrontation with the "don't act" position.

---

You are executing the prove-synthesize skill for a Signal investigation.

**Input**: (1) a hypothesis statement, (2) investigation signals from prove-* skills.

The synthesis you produce supersedes the individual signals. A synthesis that reaches no verdict is not a synthesis — it is a deferred decision wearing analytical clothing.

**The default competitor**: Before reading any signal, the status-quo position is "the hypothesis is false and no action is warranted." The synthesis must argue against or confirm that default with evidence — not hedge around it. Every output section addresses the status-quo position explicitly.

---

### Roles (Sequential)

**SYNTHESIST** reads all signals and names a verdict (yes/no/maybe), the top 3 signals that most challenged the status-quo default, and 2–4 principles that generalize the finding.

NOT: produce a maybe verdict without naming exactly what evidence would resolve it into yes or no — open-ended maybe is inertia with a different label. Do: if the verdict is maybe, specify the one signal that, if obtained, would resolve the verdict.

**ADVERSARY** argues *for* the status-quo position. Its job is to find what the signals missed, misread, or overstated that would justify maintaining the default.

NOT: argue that the investigation was insufficient in generic terms — that proves nothing about the status-quo position. Do: name the specific mechanism by which the status-quo would survive the evidence — what would have to be true for the signals to be wrong.

**ANALYST** audits whether the synthesist's verdict actually defeats the status-quo or merely reports findings without engaging it.

NOT: accept a verdict that does not address the status-quo competitor. Do: confirm that the verdict explicitly names why the evidence outweighs the cost of acting relative to the cost of staying put.

---

### Output

**Verdict vs. Status Quo** — State yes, no, or maybe in the first sentence. In the second sentence, name what the verdict says about the status-quo position: does the evidence defeat it, confirm it, or leave it standing on a specific question?

**Status-Quo Challenge Evidence** — Three evidence items that most directly challenge (or confirm) the default position. Each names the signal, states what it showed about the status-quo assumption, and explains why it shifts the decision.

**Status-Quo Survival Case** — What the ADVERSARY found that most supports the status-quo surviving the evidence. This is not "more research needed" — it is the strongest specific mechanism by which the default position remains defensible.

**Principles** — Two to four generalizations. Each principle names what this investigation reveals about when status-quo positions in this domain are correctly challenged versus correctly maintained.

**Open Questions** — Questions that, if resolved, would change the verdict. Each names the role that raised it and states what the answer would do to the status-quo position.

---

### Self-Containment Check

Before outputting, verify each question can be answered from the named section. If any question cannot be answered from the named section, revise that section before outputting.

1. What is the verdict, and what does it say about the status-quo position? → Verdict vs. Status Quo
2. What evidence most directly challenged the default? → Status-Quo Challenge Evidence
3. What is the strongest remaining argument for the status-quo? → Status-Quo Survival Case
4. What generalizes about when status-quo positions in this domain should be challenged? → Principles
5. What would change the verdict if resolved? → Open Questions

---

## V-04 — Combined: Phase-gated ceiling + sequential gate resolution

**Axes**: Lifecycle emphasis (C-39) + role sequence (proper NOT: gates per role, sequential architecture)
**Hypothesis**: Adding phase-gated confidence ceilings to a correctly-gated sequential architecture produces a synthesis instruction that passes all essential criteria and earns C-39 without requiring concurrent execution.

---

You are executing the prove-synthesize skill for a Signal investigation.

**Input**: (1) a hypothesis statement, (2) investigation signals from prove-* skills.

The synthesis you produce supersedes the individual signals — it is the authoritative record; the signal inventory is subordinate to it.

---

### Pre-Synthesis Step — Evidence Phase Classification

Before reasoning about the hypothesis, classify the signals by investigation phase and establish the confidence ceiling for this synthesis. The ceiling is a hard upper bound — it fires before synthesis begins, not as calibration guidance afterward.

| Evidence Coverage | Confidence Ceiling |
|------------------|-------------------|
| No signals | 25 |
| Explore signals only (prove-websearch, prove-intelligence) | 50 |
| Explore + at least one Test signal (prove-hypothesis, prove-analysis) | 72 |
| All three phases: Explore + Test + Validate (prove-interview, prove-prototype, prove-publish) | none |

State before proceeding: "Evidence phase coverage: [phases present]. Confidence ceiling: [N or none]."

---

### Cognitive Roles (Sequential Execution)

**SYNTHESIST** (Step 1): reads all signals, assembles the answer (yes/no/maybe), identifies the top 3 evidence items, and drafts 2–4 principles.

SYNTHESIST gate — NOT: accept a signal's conclusion without reading its reasoning — that is evidence laundering, and produces an argument stack with no weight-bearing structure. Do: for each evidence item, name the reasoning mechanism that makes the signal persuasive — what the signal showed that ruled out the competing interpretation.

**ADVERSARY** (Step 2): receives the SYNTHESIST output and challenges every claim. Produces counter-evidence and open questions.

ADVERSARY gate — NOT: challenge with objections that apply to every investigation — "potential bias," "small sample," "needs replication" are not counter-evidence for this hypothesis. Do: name something specific about this hypothesis that argues against the answer: a signal that points a different direction, a population the signals didn't test, or an assumption the signals never examined.

Exemplar (invalid): "The investigation may have been influenced by selection bias." [Generic — fails the gate.]
Exemplar (valid): "prove-interview signals came entirely from teams that chose to adopt; the hypothesis about why non-adopters resist remains unexamined." [Hypothesis-specific — passes the gate.]

**ANALYST** (Step 3): receives both outputs, verifies confidence is within the phase ceiling, verifies traceability, and surfaces any open questions the previous two roles raised.

ANALYST gate — NOT: state confidence above the ceiling established in the pre-synthesis step — a ceiling breach is a calibration error regardless of signal quality. Do: state confidence within the ceiling, citing the phase coverage: "Confidence: 62. Ceiling: 72 (Explore+Test coverage)."

---

### Output

Write the synthesis as five prose paragraphs under these five section headers.

NOT: a table or numbered list for the key evidence section — write argument structure as prose, naming each signal and the reasoning that makes it persuasive. Do: each paragraph is self-contained and addresses a named reader question.

**Verdict/Confidence** — Yes, no, or maybe in the first sentence. Confidence integer (within ceiling) and phase coverage in the second sentence.

**Key Evidence** — Three signals in one paragraph. Each names the source, states what it showed, and explains what in the reasoning made it persuasive.

**Counter-Evidence** — What argues against the verdict. Each item is specific to this hypothesis. Attribute each to ADVERSARY.

**Principles** — Two to four generalizations. Each is one sentence, abstract enough to transfer to a different hypothesis in the same domain.

**Open Questions** — What the investigation did not resolve. Each is a question. Attribute each to the role that raised it (SYNTHESIST, ADVERSARY, or ANALYST).

---

### Self-Containment Check

Before outputting, verify each question can be answered from the named paragraph. If any question cannot be answered from the named paragraph, revise that paragraph before outputting.

1. What is the verdict? → Verdict/Confidence paragraph
2. What is the confidence score and what ceiling constrains it? → Verdict/Confidence paragraph
3. What are the three strongest evidence items and why is each persuasive? → Key Evidence paragraph
4. What argues against the verdict? → Counter-Evidence paragraph
5. What generalizes beyond this hypothesis? → Principles paragraph
6. What remains unresolved, and which role raised each question? → Open Questions paragraph

---

## V-05 — Combined: Concurrent execution + unified gate block + phase-gated ceiling

**Axes**: Role sequence (concurrent, C-35) + lifecycle emphasis (C-39) + gate architecture (C-40)
**Hypothesis**: Combining concurrent role execution, a unified gate block indexed by role failure mode, and a pre-synthesis evidence phase ceiling produces a synthesis instruction that passes all essential criteria and all three new v11 criteria simultaneously.

---

You are executing the prove-synthesize skill for a Signal investigation.

**Input**: (1) a hypothesis statement, (2) investigation signals from prove-* skills (prove-websearch, prove-analysis, prove-hypothesis, prove-interview, prove-prototype, prove-intelligence, or prove-publish).

The synthesis you produce supersedes the individual signals — it is the authoritative record; the signal inventory is subordinate to it.

---

### Pre-Synthesis Step — Evidence Phase Classification

Before reasoning begins, classify the investigation signals by phase and establish the confidence ceiling for this synthesis. The ceiling is a hard upper bound set before synthesis reasoning — it is not calibration guidance after the fact.

| Evidence Coverage | Confidence Ceiling |
|------------------|-------------------|
| No signals | 25 |
| Explore signals only (prove-websearch, prove-intelligence) | 50 |
| Explore + at least one Test signal (prove-hypothesis, prove-analysis) | 72 |
| All three phases covered (Explore + Test + any Validate signal) | none |

State before proceeding: "Evidence phase coverage: [phases present]. Confidence ceiling: [N or none]."

---

### Roles

Three cognitive roles execute **concurrently** in your reasoning. All three operate simultaneously — not in sequence. Their perspectives merge into a single seamless output document. The output contains no labeled role sections and no visible role seams.

**SYNTHESIST** — Assembles the answer, key evidence, and principles. Failure mode: evidence laundering — accepting a signal's conclusion without examining the reasoning that makes it persuasive.

**ADVERSARY** — Challenges every reasoning step and surfaces counter-evidence. Failure mode: generic challenge — raising objections that apply to any investigation rather than this hypothesis.

**ANALYST** — Verifies that confidence is within the phase ceiling and that evidence items are traceable to named signals. Failure mode: ceiling breach — assigning confidence above the phase ceiling regardless of signal convergence.

---

### Gate Block

Read this block after the role definitions and before producing any output. Failure modes are indexed by role.

**SYNTHESIST — Evidence laundering**
NOT: state what a signal concluded without naming the reasoning that made it persuasive — that produces an assertion with no weight-bearing argument.
Do: for each key evidence item, name what in the signal's reasoning ruled out the competing explanation or established the mechanism.
Exemplar (fail): "prove-websearch found adoption rising, supporting the hypothesis." [No reasoning — fails the gate.]
Exemplar (pass): "prove-websearch found adoption rising specifically in low-switching-cost segments, which is persuasive because it rules out the inertia explanation — if adoption were driven by conviction alone, the pattern would not vary by switching cost." [Reasoning present — passes the gate.]

**ADVERSARY — Generic challenge**
NOT: raise counter-evidence that applies to any investigation — "potential bias," "small sample," and "needs replication" are not counter-evidence for this hypothesis.
Do: name something specific about this hypothesis that argues against the verdict — a signal pointing a different direction, a population not tested, or an assumption the signals never examined.
Exemplar (fail): "The investigation may have sampling bias and requires replication." [Generic — fails the gate.]
Exemplar (pass): "prove-interview signals sampled only teams that adopted; the hypothesis about non-adopter resistance remains untested, leaving the causal direction ambiguous." [Hypothesis-specific — passes the gate.]

**ANALYST — Ceiling breach**
NOT: state confidence above the phase ceiling established in the pre-synthesis step — a ceiling breach is a calibration error regardless of signal quality or convergence.
Do: state confidence within the ceiling, naming the phase coverage that constrains it.
Exemplar (fail): "Confidence: 80" when only Explore signals are present (ceiling: 50). [Ceiling breach — fails the gate.]
Exemplar (pass): "Confidence: 47. Explore-only coverage, ceiling 50." [Within ceiling — passes the gate.]

If any failure mode fires, correct the affected output element before proceeding.

---

### Output

NOT: a table or bulleted list for the key evidence section — write it as a prose paragraph naming each signal and its reasoning. Do: write the synthesis as five prose paragraphs under these five section headers.

**Verdict/Confidence** — State yes, no, or maybe in the first sentence. Give the confidence score (integer 0–100, within the phase ceiling) and name the phase coverage and ceiling: "Confidence: 61. Explore+Test coverage, ceiling 72."

**Key Evidence** — Three evidence items in one prose paragraph. Each names the source signal, states what it showed, and explains what made it persuasive — not just its conclusion.

**Counter-Evidence** — What argues against the verdict. Each item is specific to this hypothesis. Attribute each item to ADVERSARY.

**Principles** — Two to four generalizations. Each is one sentence, abstract enough to transfer to a different hypothesis in the same domain.

**Open Questions** — What the investigation did not resolve. Each item is a question. Attribute each to the role that raised it (SYNTHESIST, ADVERSARY, or ANALYST). If a question was raised by the ADVERSARY challenge, acknowledge that attribution.

---

### Self-Containment Check

Before outputting, verify each question can be answered from the named paragraph. If any question cannot be answered from the named paragraph, revise that paragraph before outputting.

1. What is the verdict? → Verdict/Confidence paragraph
2. What is the confidence score, and what ceiling constrains it? → Verdict/Confidence paragraph
3. What are the three strongest evidence items and why is each persuasive? → Key Evidence paragraph
4. What argues against the verdict? → Counter-Evidence paragraph
5. What generalizes beyond this hypothesis? → Principles paragraph
6. What did the investigation leave unresolved, and which role raised each question? → Open Questions paragraph

---

## Variation Summary

| Variation | Axis | New Criteria Targeted | Essential Fix? |
|-----------|------|-----------------------|----------------|
| V-01 | Lifecycle emphasis: phase-gated ceiling | C-39 | No (C-11/C-13/C-30 still fail) |
| V-02 | Role sequence: concurrent + unified gate block | C-40 (unlocks C-35, C-36, C-38) | Yes — unified gate satisfies C-11/C-13/C-30 |
| V-03 | Inertia framing: status-quo as synthesis opponent | none | No (exploratory axis) |
| V-04 | Combined: phase ceiling + sequential gate fix | C-39 | Yes — NOT: gates per role |
| V-05 | Combined: concurrent + unified gate + phase ceiling | C-39 + C-40 + C-41 | Yes — full target |

**Calibration preview under v11:**

| Variation | C-11 | C-13 | C-30 | C-35 | C-39 | C-40 | C-41 | All essential? |
|-----------|------|------|------|------|------|------|------|----------------|
| V-01 | FAIL | FAIL | FAIL | FAIL | **PASS** | FAIL | PASS | No |
| V-02 | **PASS** | **PASS** | **PASS** | **PASS** | FAIL | **PASS** | PASS | **Yes** |
| V-03 | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | PASS | No |
| V-04 | **PASS** | **PASS** | **PASS** | FAIL | **PASS** | FAIL | PASS | **Yes** |
| V-05 | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | **PASS** | PASS | **Yes** |

**Golden candidates**: V-02, V-04, V-05. V-05 is the maximum-criteria target. V-02 is the cleanest single-axis test of the C-40 architectural fix. V-04 confirms the fix is architecture-independent (concurrent not required for essential pass).
