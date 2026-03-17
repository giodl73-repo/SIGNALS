# prove-prototype Variations (V-01 through V-05)

---

## V-01 — Single Axis: Output Format (table-driven, rationale co-located)

**Hypothesis**: Tables structurally enforce rationale co-location (C-17) better than prose, producing higher C-02, C-13, and C-15 compliance as a side-effect of the format itself.

---

```
You are running /prove:prototype for the topic: {{topic}}

The hypothesis under test is:
{{hypothesis}}

---

## Instructions

Produce a prototype report. Use the table formats specified below for every section that has one. Do not skip a section. Do not leave a section header without a body.

---

### Section 1 — Hypothesis Under Test

Restate the hypothesis in a single sentence. This is the first thing in your output. Do not begin with preamble.

---

### Section 2 — Prototype Scope

| Item | In Scope | Out of Scope | Exclusion Rationale (why the test remains valid without it) |
|------|----------|--------------|-------------------------------------------------------------|
| [component or behavior] | yes/no | yes/no | [specific reason this omission does not invalidate the test] |

Minimum two rows. Every out-of-scope item must have a non-empty rationale cell that answers: "why does leaving this out still permit a valid test?"

---

### Section 3 — Measurement Plan (defined before building)

State: this section was written before any build activity.

| Metric | How It Is Measured | Predicted Value | Success Condition | Failure Condition |
|--------|-------------------|-----------------|--------------------|-------------------|
| [metric name] | [method] | [expected value] | [what pass looks like] | [what fail looks like] |

Minimum one metric row. Success and failure conditions must be explicit.

---

### Section 4 — Build Summary

One paragraph. What was actually constructed. Reference only things in scope from Section 2.

---

### Section 5 — Results

| Metric | Predicted | Actual | Delta | Delta Explanation |
|--------|-----------|--------|-------|-------------------|
| [metric name] | [value] | [value] | [gap as a signed quantity or direction] | [why the gap exists, or "none — prediction matched"] |

The Delta column is mandatory. Do not merge it into the Predicted or Actual columns. The Delta Explanation must be in the same row as the delta it explains.

---

### Section 6 — Counter-Evidence

This section must end with one of two explicit dispositions. Choose the one that applies:

**If a counter-interpretation exists:**
State it, then rebut it. The rebuttal must be grounded in the evidence from Section 5, not in the hypothesis itself.

**If no counter-interpretation exists:**
State: "No plausible counter-interpretation was identified." Follow with a one-sentence reason why the results are not susceptible to an alternative reading.

Do not leave this section open-ended. One of these two dispositions must close the section.

---

### Section 7 — Verdict

| Verdict | Rationale |
|---------|-----------|
| [Confirmed / Refuted / Inconclusive] | [One or two sentences explaining why the evidence from Section 5 supports this verdict, not just restating the evidence] |

---

### Section 8 — Limitations and Next Step

| Limitation | Next Step |
|------------|-----------|
| [one specific limitation of this prototype or measurement] | [one specific action that follows from this result] |

---

### Section 9 — Replication

List every tool, input, command, or step needed to reproduce this prototype. Use a numbered list. No implicit steps. If a step requires a file or config, name it.

---

## Structural Rules

- Section 3 must appear in the output before Section 4. The temporal gate must be visible in the document order.
- Every table cell must be populated. Write "N/A" only if the cell genuinely does not apply and state why inline.
- The Delta column in Section 5 is a computed element, not a label alongside two other columns. If predicted and actual match, write "0 — prediction confirmed." If they diverge, write the signed gap.
```

---

## V-02 — Single Axis: Lifecycle Emphasis (explicit phase gates, ordered sections with word budgets)

**Hypothesis**: Naming each lifecycle phase as an explicit structural gate, with ordered constraints and word budgets, produces higher C-03 and C-12 compliance than format-neutral instructions.

---

```
You are running /prove:prototype for the topic: {{topic}}

The hypothesis under test is:
{{hypothesis}}

---

## Prototype Report — Phase-Gated Format

This format enforces the prototype lifecycle as a strict linear sequence. Each phase is labeled. Later phases may not reference information introduced in earlier phases if that information was not present at the time that phase would have been executed.

Complete the phases in order. Do not reorder them.

---

### PHASE 1: HYPOTHESIS RESTATEMENT
*Execute before anything else.*

Restate the hypothesis in your own words. One to two sentences. This is the anchor for every decision that follows.

> H: [restatement here]

---

### PHASE 2: SCOPE DEFINITION
*Execute before any measurement planning.*

Name what the prototype will do and what it will not do.

For each exclusion, answer the test-validity question directly: **"Without this, can the prototype still test the hypothesis? Why?"**

Exclusions:
- [Item excluded]: [Why the test remains valid without it]
- [Item excluded]: [Why the test remains valid without it]

Minimum two exclusions. Bare labels without rationale fail this phase.

---

### PHASE 3: MEASUREMENT PLAN
*Execute before any build activity. This phase establishes the evidentiary standard the result will be held to.*

**What to measure**: [metric name and measurement method]
**Predicted outcome**: [specific value, range, or direction expected]
**What confirms the hypothesis**: [explicit pass condition]
**What refutes the hypothesis**: [explicit fail condition]

If there is more than one metric, repeat this block. Do not proceed to Phase 4 until every success and failure condition is written down.

---

### PHASE 4: BUILD SUMMARY
*Execute after Phase 3 is complete.*

One paragraph. Describe what was built. Reference only items that were in scope per Phase 2. Do not introduce new scope here.

Word budget: 50–150 words.

---

### PHASE 5: RESULTS
*Execute after Phase 4 is complete.*

For each metric from Phase 3:

**Metric**: [name]
**Predicted**: [value from Phase 3]
**Actual**: [observed value]
**Delta**: [gap as a signed quantity — do not merge this into either Predicted or Actual]
**Why the delta is what it is**: [explanation, or "prediction matched exactly"]

Report the raw evidence that produced the actual value. Include at least one concrete data point (a number, a time, a count, an output).

---

### PHASE 6: COUNTER-EVIDENCE
*Execute after Phase 5 is complete.*

Consider whether the results could be explained by something other than the hypothesis being true or false.

Terminate this phase with exactly one of:

(A) **Counter-interpretation found**: [state it] → [rebuttal grounded in Phase 5 evidence]
(B) **No counter-interpretation found**: "No plausible alternative explanation for the observed results was identified." → [one sentence on why]

One of A or B must close this phase. An open-ended discussion that reaches neither disposition fails.

---

### PHASE 7: VERDICT
*Execute after Phase 6 is complete.*

**Verdict**: [Confirmed / Refuted / Inconclusive]

**Rationale**: [One to three sentences. Explain why the Phase 5 evidence — specifically the delta — supports this verdict. Do not restate the evidence; connect it to the verdict.]

The verdict rationale must be a distinct explanation, not a repetition of the results.

---

### PHASE 8: LIMITATIONS AND NEXT STEP
*Execute last.*

**Limitation**: [One honest constraint on what this prototype can and cannot claim]
**Next step**: [One specific action that follows from the verdict and the limitation]

---

### PHASE 9: REPLICATION PATH
*Appended after Phase 8.*

List every tool, input, command, or step a reader would need to reproduce this prototype from scratch. Number the steps. Name every file, config, or parameter by name. No step may rely on information that is not in this list or in the report above.
```

---

## V-03 — Single Axis: Phrasing Register (conversational, imperative, lab-notebook style)

**Hypothesis**: Direct imperative phrasing ("write this, then write this") with conversational register reduces hedging and produces more populated sections (C-11) than formal/descriptive instruction.

---

```
You are running /prove:prototype for the topic: {{topic}}

The hypothesis you're testing is:
{{hypothesis}}

---

Here's what you're going to write. Follow this sequence exactly. Don't skip anything.

---

**First: restate the hypothesis.**
Write it out. One sentence. Before you say anything else about what you built or what happened.

---

**Second: define the scope.**
Tell me what the prototype does. Then tell me what it doesn't do — at least two things. For each thing you left out, say why the test still works without it. Don't just list the exclusions; answer the question "so why doesn't that matter for this test?"

---

**Third: write down what you were going to measure — before you describe what happened.**
Pick a metric. Say what you expected to happen. Say what "it worked" looks like and what "it didn't work" looks like. Be specific. A range is fine. Vague isn't.

This goes in the report before the results. The ordering matters. The reader should be able to see you committed to a prediction before you knew the answer.

---

**Fourth: describe what you built.**
Keep it short — one paragraph. Stick to what was in scope.

---

**Fifth: report what happened.**
Say what you predicted. Say what actually happened. Say what the gap is — don't make me compute it from two numbers. Then say why the gap is what it is. If there was no gap, say that too.

Include at least one real data point: a number, a time, a count, an output. Something concrete.

---

**Sixth: deal with the counter-case.**
Ask yourself: could someone look at these results and say the hypothesis is still wrong (or right) for a different reason? If yes — name that reason and knock it down using the evidence. If no — say so. Say "no plausible counter-interpretation applies here" and give one reason why. Don't leave this hanging. Close it.

---

**Seventh: give the verdict.**
Confirmed, refuted, or inconclusive. Then say why — not a restatement of the results, but the reasoning that connects the evidence to the verdict. One or two sentences.

---

**Eighth: be honest about what this doesn't prove.**
Name one real limitation. Then name one concrete next step.

---

**Ninth: tell me how to reproduce it.**
Number the steps. Name every tool, file, config, and input by name. Don't leave any implicit steps. Someone should be able to run this without asking you a follow-up question.

---

A few rules:
- Don't leave any of these sections empty. If a section exists, fill it.
- The measurement plan comes before the results in the document. Don't flip it.
- The delta is its own element — not embedded in the prediction or the observation.
- Every exclusion rationale stays next to the exclusion it explains.
```

---

## V-04 — Combined Axes: Role Sequence + Output Format (two-pass, mixed table/prose)

**Hypothesis**: Splitting the skill into an explicit Architect pass (scope + measurement planning) followed by an Experimenter pass (results + verdict) produces higher C-03 and C-12 compliance by structurally separating the prediction phase from the observation phase.

---

```
You are running /prove:prototype for the topic: {{topic}}

The hypothesis under test is:
{{hypothesis}}

---

## Instructions

This skill runs in two passes. Complete Pass 1 entirely before writing Pass 2.

Pass 1 is the **Architect pass** — you define what will be built and how it will be judged.
Pass 2 is the **Experimenter pass** — you report what happened and what it means.

The document boundary between Pass 1 and Pass 2 is the evidentiary firewall. Nothing in Pass 2 may revise what was committed in Pass 1.

---

## PASS 1 — ARCHITECT

*Stop after completing this pass. Do not read ahead.*

### 1.1 Hypothesis (Architect)

Restate the hypothesis in one sentence. This is the claim the prototype will test.

---

### 1.2 Scope Table (Architect)

| Component | In / Out | If Out: Why the Test Remains Valid |
|-----------|----------|------------------------------------|
| | | |

Minimum two out-of-scope entries. Every out-of-scope row must have a populated rationale column that answers the test-validity question directly.

---

### 1.3 Measurement Plan (Architect)

| Metric | Measurement Method | Predicted Value | Confirms Hypothesis If | Refutes Hypothesis If |
|--------|--------------------|-----------------|------------------------|----------------------|
| | | | | |

Write the prediction before the prototype is built. The prediction must not be informed by the results. If more than one metric applies, add rows.

---

### 1.4 Minimality Justification (Architect)

One short paragraph. Identify at least one trade-off: what was left out, and why that omission still permits the hypothesis to be tested.

---

*— PASS 1 COMPLETE — DO NOT REVISE ANYTHING ABOVE THIS LINE —*

---

## PASS 2 — EXPERIMENTER

### 2.1 Build Summary (Experimenter)

One paragraph. What was constructed. Reference only items that were declared in-scope in Section 1.2.

---

### 2.2 Results Table (Experimenter)

| Metric | Predicted (from 1.3) | Actual | Delta | Delta Explanation |
|--------|----------------------|--------|-------|-------------------|
| | | | | |

The Predicted column must be copied verbatim from Section 1.3. The Delta column is a distinct computed element — state the signed gap or write "prediction matched." The Delta Explanation must appear in the same row as the delta.

Include at least one concrete data point in or alongside this table (a number, a time, a measurement output).

---

### 2.3 Counter-Evidence (Experimenter)

Consider alternative explanations for the observed results.

Close this section with one of:

**(A)** "Counter-interpretation: [state it] — Rebuttal: [grounded in Section 2.2 evidence]"
**(B)** "No plausible counter-interpretation identified — [one sentence on why the results are not susceptible to an alternative reading]"

The section must end at A or B. It may not end with an open question.

---

### 2.4 Verdict (Experimenter)

**Verdict**: Confirmed / Refuted / Inconclusive

**Rationale**: [Distinct explanation — not a restatement of the results — of why the delta in Section 2.2 supports this verdict. One to three sentences.]

---

### 2.5 Limitations and Next Step (Experimenter)

**Limitation**: [One honest constraint on what this prototype proves or fails to prove]
**Next step**: [One specific action that follows from this verdict]

---

### 2.6 Replication Path (Experimenter)

Numbered list. Every tool, input, file, config, command, and parameter by name. No implicit steps. A reader with no prior context must be able to reproduce the prototype from this list alone.
```

---

## V-05 — Combined Axes: Lifecycle Emphasis + Inertia Framing (status-quo competitor at each phase)

**Hypothesis**: Requiring the status-quo competitor to appear at each lifecycle phase — not just in the verdict — produces more grounded scope exclusions and more credible verdicts by forcing explicit comparison throughout, rather than only at the conclusion.

---

```
You are running /prove:prototype for the topic: {{topic}}

The hypothesis under test is:
{{hypothesis}}

The status-quo approach (what currently exists or is currently done without this feature) is:
{{status_quo}}

---

## Instructions

This prototype report compares your hypothesis against the status-quo approach at each phase. The status-quo is not the enemy — it is the baseline. Comparison at each phase keeps the prototype honest.

Complete all sections. Do not leave any section empty.

---

### Phase 1 — Hypothesis and Baseline Contrast

**Hypothesis (restated)**: [One sentence restatement of the hypothesis being tested]

**What the status quo currently does here**: [One sentence describing how the status-quo approach handles the same problem]

**The specific difference this prototype claims to test**: [One sentence identifying the narrowest possible delta between hypothesis and status quo]

---

### Phase 2 — Scope Definition

| Item | In Scope | Out of Scope | Exclusion Rationale | Status-Quo Comparison |
|------|----------|--------------|---------------------|-----------------------|
| | | | Why the test remains valid without this | Does the status quo handle this differently? Note it or write "same" |

Minimum two out-of-scope rows. The Exclusion Rationale column must directly answer "why does leaving this out still permit a valid test?" The Status-Quo Comparison column notes whether the exclusion creates a scope asymmetry with the baseline.

---

### Phase 3 — Measurement Plan (before build)

**What to measure**: [metric name and method]
**Predicted outcome for this prototype**: [specific value, range, or direction]
**Expected status-quo result on the same metric**: [what the baseline would produce on the same metric, if measurable]
**Confirms hypothesis if**: [explicit pass condition]
**Refutes hypothesis if**: [explicit fail condition]

This phase is written before any build activity. If more than one metric applies, repeat the block.

---

### Phase 4 — Build Summary

One paragraph. What was constructed. Reference only in-scope items from Phase 2. Do not introduce new scope.

*Note: the status-quo is not re-implemented here. If a baseline measurement is reported in Phase 5, state how it was obtained.*

---

### Phase 5 — Results

| Metric | Predicted (this prototype) | Actual (this prototype) | Delta | Status-Quo Baseline | Prototype vs. Baseline |
|--------|---------------------------|------------------------|-------|---------------------|------------------------|
| | | | [signed gap] | [if measured; else "not measured"] | [direction of difference or "baseline not available"] |

The Delta column is a distinct computed element. Do not merge it with Predicted or Actual. Include at least one concrete data point (a number, time, count, or output).

If a status-quo baseline measurement was not taken, write "not measured" and note it as a limitation in Phase 7.

---

### Phase 6 — Counter-Evidence

Identify alternative explanations for the observed results.

**Prototype-internal counter**: Could the observed delta be explained by something other than the hypothesis being true? If yes: state it and rebut it using Phase 5 evidence. If no: "No plausible prototype-internal counter-interpretation identified — [one sentence why]."

**Status-quo parity risk**: Could the status-quo approach produce the same result through a mechanism this prototype did not test? If yes: name the mechanism and address it. If no: "Status-quo parity risk not applicable — [one sentence why]."

Both questions must reach a disposition. Open-ended discussion without a closing statement fails.

---

### Phase 7 — Verdict

**Verdict**: Confirmed / Refuted / Inconclusive

**Rationale**: [One to three sentences. Connect the Phase 5 delta to the verdict. Explain why the evidence supports this conclusion rather than the alternative. Mention the status-quo comparison if it is load-bearing for the verdict.]

**Against the status quo**: [One sentence on what the verdict implies for whether this feature improves on, matches, or falls short of the baseline.]

---

### Phase 8 — Limitations and Next Step

**Limitation**: [One specific constraint on what this prototype can claim]
**Status-quo gap**: [One note on whether the comparison was symmetric; if baseline was not measured, name it here]
**Next step**: [One specific action that follows from the verdict — either to strengthen the hypothesis or to validate against the status quo more rigorously]

---

### Phase 9 — Replication Path

Numbered steps. Every tool, input, file, config, command, and parameter by name. If a status-quo baseline was measured, include how to reproduce that measurement. No implicit steps.
```

---

## Variation Summary

| Variation | Axis | Key Structural Bets | Targets |
|-----------|------|---------------------|---------|
| V-01 | Output format (table-driven) | Tables enforce co-location structurally; Delta column is non-negotiable; counter-evidence section has explicit A/B closure | C-17, C-13, C-15, C-16 |
| V-02 | Lifecycle emphasis (phase gates) | Phases labeled, ordered, temporally constrained; word budgets; Phase 3 cannot bleed into Phase 4 | C-03, C-12, C-11 |
| V-03 | Phrasing register (conversational/imperative) | Direct "write this" instructions; lab-notebook tone; closes counter-evidence with explicit sentence | C-11, C-16, C-04 |
| V-04 | Role sequence + Output format | Architect/Experimenter firewall; mixed table+prose; Pass 1 completion is a hard gate | C-03, C-12, C-17 |
| V-05 | Lifecycle emphasis + Inertia framing | Status-quo appears at every phase; scope asymmetry column; parity risk in counter-evidence | C-02, C-05, C-09 |
