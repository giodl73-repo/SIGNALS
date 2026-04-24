# Quest Variate — prove-prototype (Round 4)

**Rubric**: v4 (130 pts) | **New criteria**: C-18, C-19
**Date**: 2026-03-15

Two new criteria drive this round:
- **C-18**: Every optional section must close with one of exactly two explicit dispositions — not silence, not open-ended hedging.
- **C-19**: Ordering gate labels must appear inline at the point of the constrained action, not only in a preamble or end-of-document output contract.

R3 V-01 passed all 17 criteria by having binary closure in Section 6 and an output contract block at the end for ordering. V4 requires both: the inline gate AND the output contract. V-01's output contract alone does not satisfy C-19; the inline gate markers are new.

---

## Variation Axes

| Variation | Primary Axis | Secondary Axis |
|-----------|-------------|----------------|
| V-01 | Output format (table-dominant) | C-18 universalized + C-19 inline gates added |
| V-02 | Lifecycle emphasis (phase gates) | Execute-before markers + phase-level closure locks |
| V-03 | Output format (labeled-pair blocks, no tables) | C-18 via labeled terminal fields, C-19 via bracketed gate labels |
| V-04 | Phrasing register (conversational/imperative) | C-18 via explicit two-option closing sentence, C-19 via inline gate lines |
| V-05 | Combination (phase gates + tables) | Maximum structural enforcement: phase markers + table rationale + phase-close blocks |

---

## V-01 — Table-Dominant with Inline Gate Labels and Universal Binary Disposition

**Axis**: Output format (table-dominant)
**Hypothesis**: Structural tables enforce co-location; inline gate labels at each ordering-constrained section satisfy C-19 without relying on the output contract alone; universalizing the binary disposition pattern from Section 6 to all optional sections satisfies C-18.

---

You are running /prove:prototype. Build something small and measure it.

Every section header below carries an inline gate marker stating its ordering constraint. Gate markers are structural — they are not decorative labels. Read the gate marker before writing each section.

---

### Section 1 — Hypothesis
*[Gate: this section must be the first element of your output. Nothing precedes it — not a title, not a build description, not a result.]*

Restate the hypothesis being tested. Label it `H:`. One to two sentences.

> H: [restatement here]

---

### Section 2 — Prototype Scope
*[Gate: complete this table before any build content or measurement criteria appear in your output.]*

| In Scope | Out of Scope | Why the test remains valid without this exclusion |
|----------|--------------|--------------------------------------------------|
| [item]   | [item]       | [one sentence answering: why does leaving this out still permit a valid test of H?] |
| [item]   | [item]       | [one sentence answering: why does leaving this out still permit a valid test of H?] |

Requirements:
- At least two Out-of-Scope rows.
- The third column must be populated in every Out-of-Scope row. "It wasn't needed" and "outside scope" do not satisfy it.

---

### Section 3 — Measurement Protocol
*[Gate: complete every row in this table before any build output exists. This section must appear before Section 4 in your output. If you find yourself writing build steps, stop and complete this table first. The metric, success condition, failure condition, and prediction must all be established here — before any building begins.]*

| Field | Content |
|-------|---------|
| Metric | [what will be observed] |
| Success condition | [value or event that confirms H] |
| Failure condition | [value or event that refutes H] |
| Predicted outcome | [which condition you expect; one sentence of reasoning] |

---

### Section 4 — Build Record
*[Gate: this section must appear after Section 3 in your output.]*

| Tool | Input | Step | Output |
|------|-------|------|--------|
| [name] | [exact parameter or file] | [what was done] | [what was produced] |

Requirements:
- Every tool, input, step, and output must be named explicitly enough for reproduction.
- No implicit steps. Configuration files named.

---

### Section 5 — Results
*[Gate: this section must appear after Section 4 in your output.]*

| Metric | Predicted | Actual | Delta (predicted − actual) | Why the delta is what it is |
|--------|-----------|--------|---------------------------|-----------------------------|
| [name] | [from Section 3] | [observed value; include one concrete data point — a number, a time, a count, or a direct quote from output] | [computed gap; write "0 — prediction confirmed" if equal; do not leave this for the reader to infer] | [explanation here, in this row, not in a separate section] |

Requirements:
- Delta is a required column. Compute it explicitly.
- Actual must contain at least one concrete data point. A summary statement does not satisfy this.
- "Why the delta is what it is" must appear in the same row as the delta.

---

### Section 6 — Counter-Evidence
*[Gate: this section must appear after Section 5 in your output.]*

Consider whether the results could be explained by something other than the hypothesis being true or false.

This section must close with exactly one of the following two dispositions. Write the applicable disposition as the terminal element of this section. Silence, hedging, and partial answers are not permitted.

**Disposition A** (counter-interpretation exists):
> Counter-interpretation: [state the alternative explanation]
> Rebuttal: [explain, using evidence from Section 5, why this does not hold]

**Disposition B** (no counter-interpretation):
> No plausible counter-interpretation was identified. Reason: [one sentence explaining why the results are not susceptible to an alternative reading]

---

### Section 7 — Verdict
*[Gate: this section must appear after Section 6.]*

| Verdict | Verdict Rationale |
|---------|------------------|
| [Confirmed / Refuted / Inconclusive] | [one to three sentences explaining why the evidence supports this verdict; this is not a restatement of Section 5 — it is the reasoning that connects the observed delta to the verdict] |

---

### Section 8 — Limitations and Next Step

| Limitation | Next Step |
|------------|-----------|
| [one scope constraint affecting generalizability] | [one specific action concrete enough to execute next session; "do more testing" does not satisfy this] |

This section must close with exactly one of the following two dispositions as its terminal element:

**Disposition A** (meaningful limitation found):
> This limitation affects the verdict's generalizability in the following way: [one sentence]

**Disposition B** (no significant limitation beyond scope exclusions):
> No limitations beyond the scope exclusions in Section 2 were identified. Reason: [one sentence]

---

### Section 9 — Replication Path

List every tool, input, command, and step needed to reproduce this prototype from scratch. Numbered list. No implicit steps. Configuration files named.

This section must close with exactly one of the following two dispositions as its terminal element:

**Disposition A** (replication path complete):
> Replication path is complete. All tools, inputs, and steps are enumerated above.

**Disposition B** (replication path incomplete):
> Replication path is incomplete. Missing: [what could not be specified and why]

---

### Output Contract

Before submitting, verify:

1. Section 1 is the first element of the output.
2. Section 3 appears before Section 4 in the output.
3. Section 5 appears before Section 6 in the output.
4. Section 6 appears before Section 7 in the output.
5. Every table cell is populated. Write "N/A" only where genuinely not applicable — with an inline reason.
6. Sections 6, 8, and 9 each close with an explicit Disposition A or Disposition B terminal element.
7. Delta is a computed gap in its own column — not left for the reader to infer.
8. "Why the delta is what it is" appears in the same table row as the delta.
9. "Verdict rationale" appears in the same table row as the verdict.
10. Every inline gate marker in Sections 1–7 is present in the output — they are not suppressed in the output contract alone.

---

## V-02 — Phase Gates with Execute-Before Inline Markers and Phase Closure Locks

**Axis**: Lifecycle emphasis (explicit phase boundaries)
**Hypothesis**: Phase-gate architecture makes the temporal sequence structurally visible; inline "Execute before Phase N" markers at each constrained phase satisfy C-19; mandatory phase-close dispositions on optional phases satisfy C-18; completing the full 9-phase structure (R3 V-02 was cut off at Phase 6) enables full scoring.

---

You are running /prove:prototype.

A prototype is the smallest possible thing that tests a hypothesis. This prompt enforces a strict sequence: hypothesis → scope → measure → build → results → counter-evidence → verdict → limitations → replication. Each phase carries an inline execution marker stating when it must run. The execution markers are structural — not summaries. Read each marker before writing that phase.

---

#### PHASE 1 — Hypothesis Restatement
*Execute before anything else. This phase must appear as the first element of your output.*

Restate the hypothesis being tested. One to two sentences. Label it `H:`.

> H: [restatement here]

*Phase gate: write "PHASE 1 COMPLETE" before proceeding to Phase 2.*

---

#### PHASE 2 — Prototype Scope
*Execute before Phase 3. Scope must be established before any measurement criteria are defined.*

Name what the prototype will do and what it will not do. List at least two exclusions. For each exclusion, write the test-validity answer inline, in the same bullet as the exclusion.

Exclusion format (for each excluded item):
- **Excluded**: [item]
  **Why the test remains valid without it**: [one sentence; bare labels without rationale fail this phase; "it wasn't needed" fails this phase]

*Phase gate: write "PHASE 2 COMPLETE" before proceeding to Phase 3.*

---

#### PHASE 3 — Measurement Protocol
*Execute before any build activity. This phase establishes the evidentiary standard the result will be held to.*
*Do not proceed to Phase 4 until every metric, success condition, and failure condition is written down in this phase.*

**Metric**: [what will be observed]
**Success condition**: [value or event that confirms the hypothesis]
**Failure condition**: [value or event that refutes the hypothesis]
**Predicted outcome**: [which condition you expect; one sentence of reasoning]

*Phase gate: write "PHASE 3 COMPLETE — measurement protocol established before build" before proceeding to Phase 4.*

---

#### PHASE 4 — Build Record
*Execute after Phase 3 gate is present in your output. Do not begin writing build content until the Phase 3 gate line appears above.*

For each step, write the step number, tool, input, and output inline:

- **Step [N]**: [action taken] | Tool: [name] | Input: [exact parameter or file] | Output: [what was produced]

No implicit steps. Every tool, input, and command must be named. Configuration files named.

*Phase gate: write "PHASE 4 COMPLETE" before proceeding to Phase 5.*

---

#### PHASE 5 — Results
*Execute after Phase 4 gate is present in your output.*

Compare the predicted outcome from Phase 3 to what actually happened.

**Predicted**: [restate predicted outcome from Phase 3]
**Actual**: [what was observed; must include at least one concrete data point — a number, a time, a count, or a direct quote from output; a summary statement does not satisfy this field]
**Delta**: [the gap as a stated quantity; do not merge this into Predicted or Actual; it is its own labeled field]
**Why the delta is what it is**: [explanation here, in the same block as Delta — not in a separate section]

*Phase gate: write "PHASE 5 COMPLETE" before proceeding to Phase 6.*

---

#### PHASE 6 — Counter-Evidence
*Execute after Phase 5 gate is present in your output.*

Consider whether the results could be explained by something other than the hypothesis being true or false.

*This phase must close with exactly one of the two following dispositions written as the terminal element of this phase, before the gate line.*

**Disposition A** (counter-interpretation exists):
> Counter-interpretation: [state the alternative explanation]
> Rebuttal: [explain why it does not hold, using evidence from Phase 5]

**Disposition B** (no counter-interpretation):
> No plausible counter-interpretation was identified. Reason: [one sentence]

*Phase gate: write "PHASE 6 COMPLETE — DISPOSITION [A/B] SELECTED" before proceeding to Phase 7.*

---

#### PHASE 7 — Verdict
*Execute after Phase 6 gate is present in your output.*

**Verdict**: [Confirmed / Refuted / Inconclusive]
**Verdict rationale**: [explain why the evidence supports this verdict; this is not a restatement of Phase 5 — it is the reasoning connecting the observed delta to the verdict; it appears here in the same block as the verdict]

*Phase gate: write "PHASE 7 COMPLETE" before proceeding to Phase 8.*

---

#### PHASE 8 — Limitations and Next Step
*Execute after Phase 7 gate is present in your output.*

**Limitation**: [one scope constraint that could affect generalizability of the verdict]
**Next step**: [one action concrete enough to execute next session; "do more testing" does not satisfy this; name the specific thing to test, build, or change]

*This phase must close with exactly one of the two following dispositions written as the terminal element of this phase, before the gate line.*

**Disposition A** (meaningful limitation found):
> This limitation affects the verdict's generalizability in the following way: [one sentence]

**Disposition B** (no significant limitation beyond scope exclusions):
> No limitations beyond the scope exclusions in Phase 2 were identified. Reason: [one sentence]

*Phase gate: write "PHASE 8 COMPLETE — DISPOSITION [A/B] SELECTED" before proceeding to Phase 9.*

---

#### PHASE 9 — Replication Path
*Execute after Phase 8 gate is present in your output.*

List every tool, input, command, and step needed to reproduce this prototype from scratch. Numbered list. No implicit steps. Configuration files named.

*This phase must close with exactly one of the two following dispositions written as the terminal element of this phase.*

**Disposition A** (replication path complete):
> Replication path is complete. All tools, inputs, and steps are enumerated above.

**Disposition B** (replication path incomplete):
> Replication path is incomplete. Missing: [what could not be specified and why]

*Phase gate: write "PHASE 9 COMPLETE — PROTOTYPE REPORT FINISHED"*

---

## V-03 — Labeled-Pair Block Architecture (No Tables)

**Axis**: Output format (labeled-pair blocks only; no tables)
**Hypothesis**: Labeled-pair blocks satisfy C-17 without tables (confirmed by R3 V-02 assessment); extending the same format to binary disposal terminal fields satisfies C-18; bracketed inline gate labels in section sub-headers satisfy C-19; this variation tests whether pure labeled-pair structure achieves full rubric compliance.

---

You are running /prove:prototype. Your output is structured entirely as labeled-pair blocks — no tables. Every block has a mandatory label. Every rationale element appears in the same block as the item it explains. Read the inline gate marker at the start of each section before writing that section.

---

#### Block 1 — Hypothesis
**[Gate: this block must appear as the first element of your output, before any description of what was built or what happened]**

**Hypothesis**: [restate the hypothesis in one to two sentences]

---

#### Block 2 — Prototype Scope
**[Gate: this block must be complete before any build description or measurement definition appears in your output]**

For each exclusion, write a labeled pair. At least two pairs required.

**Excluded item**: [name]
**Why the test remains valid without it**: [one sentence answering the test-validity question; bare labels do not satisfy this field; "it wasn't needed" does not satisfy this field]

*(repeat for each exclusion)*

---

#### Block 3 — Measurement Protocol
**[Gate: this block must be complete before Block 4. Every metric, success condition, and failure condition must be established here before any build content is written. This block must precede Block 4 in your output.]*

**Metric**: [what will be observed]
**Success condition**: [value or event that confirms the hypothesis]
**Failure condition**: [value or event that refutes the hypothesis]
**Predicted outcome**: [which condition you expect; one sentence of reasoning]

---

#### Block 4 — Build Record
**[Gate: this block must appear after Block 3 in your output]**

For each step, write a labeled group:

**Step [N]**: [action taken]
**Tool**: [name]
**Input**: [exact parameter or file name]
**Output**: [what was produced]

No implicit steps. Every tool, input, and command must be named. Configuration files named.

---

#### Block 5 — Results
**[Gate: this block must appear after Block 4 in your output]**

**Predicted**: [restate predicted outcome from Block 3]
**Actual**: [observed outcome; must include at least one concrete data point — a number, a time, a count, or a direct quote from output; a summary statement does not satisfy this field]
**Delta**: [the gap as a stated quantity; this is its own labeled field — do not embed it in Predicted or Actual; do not leave it for the reader to compute]
**Why the delta is what it is**: [explanation here, in the same block as Delta — not in a separate block]

---

#### Block 6 — Counter-Evidence
**[Gate: this block must appear after Block 5 in your output]**

Consider whether the results could be explained by something other than the hypothesis being true or false.

This block must close with exactly one of the two following terminal labeled pairs written as the last element of this block. No other closing form is permitted.

*If a counter-interpretation exists:*

**Counter-interpretation**: [state the alternative explanation]
**Rebuttal**: [explain why it does not hold, using evidence from Block 5]

*If no counter-interpretation exists:*

**Counter-interpretation**: None identified.
**Why no counter-interpretation exists**: [one sentence explaining why the results are not susceptible to an alternative reading]

---

#### Block 7 — Verdict

**Verdict**: [Confirmed / Refuted / Inconclusive]
**Verdict rationale**: [explain why the evidence supports this verdict; this must be a new explanation — not a restatement of Block 5; it appears in this same block as the verdict, not in a separate section]

---

#### Block 8 — Limitations and Next Step

**Limitation**: [one scope constraint affecting generalizability]
**Next step**: [one specific action concrete enough to execute next session; "do more testing" does not satisfy this field]

This block must close with exactly one of the two following terminal labeled pairs written as the last element of this block:

*If meaningful limitation found:*

**How this limitation constrains the verdict**: [one sentence]

*If no significant limitation beyond scope exclusions:*

**No significant limitations identified. Reason**: [one sentence]

---

#### Block 9 — Replication Path

List every tool, input, command, and step needed to reproduce this prototype. Numbered list. No implicit steps.

This block must close with exactly one of the two following terminal labeled pairs written as the last element of this block:

*If replication path is complete:*

**Replication path status**: Complete. All tools, inputs, and steps are enumerated above.

*If replication path is incomplete:*

**Replication path status**: Incomplete. Missing: [what could not be specified and why]

---

#### Structural Rules

1. Every labeled field must be populated. Write "N/A" only where genuinely not applicable — with an inline reason in the same labeled pair.
2. Blocks 6, 8, and 9 must each close with their named terminal labeled pair. Open-ended blocks that do not terminate with a disposition do not satisfy this prompt.
3. Block 3 must precede Block 4 in the output. Block 5 must precede Block 6. Block 6 must precede Block 7.
4. Every rationale field ("Why the test remains valid without it," "Why the delta is what it is," "Verdict rationale," "Rebuttal" or "Why no counter-interpretation exists") appears in the same labeled block as its anchor item.
5. The inline gate marker at the start of each block is present in the output — it is not suppressed.

---

## V-04 — Conversational Imperative with Binary Closure Instructions

**Axis**: Phrasing register (conversational/imperative)
**Hypothesis**: Plain-language directives — explicitly naming both permitted closing sentences for each optional step — satisfy C-18 without tables or labeled pairs; inline gate lines written by the model satisfy C-19 at the point of the constrained action; this variation tests whether conversational register can achieve full rubric compliance.

---

You are running /prove:prototype. You are about to write a prototype report. These instructions are written in plain language. Follow them in order.

---

**Before you write anything else:** Restate the hypothesis you are testing. Label it "Hypothesis." It goes first. It appears before any description of what you built, what you measured, or what happened.

---

**Step 1 — Name what the prototype leaves out.**

List at least two things your prototype does not cover. For each one, write two things: the item you excluded, and the reason that leaving it out does not invalidate the test. One item without a reason does not satisfy this step. "It wasn't needed" is not a reason. Your reason must answer: *without this, can the prototype still test the hypothesis? If yes, why?*

---

**Step 2 — Set your measurement standard before you build.**

*Before you move past this step, write this gate line in your output:* `Measurement protocol established before build.`

Name the metric you will observe. Name what counts as confirmation. Name what counts as refutation. Write your prediction: which outcome do you expect, and one sentence of reasoning?

Do not describe what you actually built or what actually happened yet. You are committing to an evidentiary standard before the evidence exists. The gate line above signals that the standard was set first.

---

**Step 3 — Build it and record what you did.**

Describe the build step by step. Be specific: what tool, what input, what command, what you observed at each step. No implicit steps. If you used a configuration file, name it.

---

**Step 4 — Compare the prediction to the result.**

Write the prediction next to the result. Then compute the gap explicitly — do not leave it for the reader to infer. Write: "I predicted [X]. I observed [Y]. The gap is [Z]." The gap is a required element of your answer.

Include at least one concrete data point: a number, a measured output, a time, a direct quote from what ran. A summary statement does not satisfy this step.

Write the reason the gap is what it is in the same paragraph as the gap — not in a separate section later.

---

**Step 5 — Consider whether a skeptic has a point.**

Could the results be explained by something other than the hypothesis being true or false?

*End this step with exactly one of the following two closing sentences. Choose the one that applies. No other form of closing is permitted.*

**Option A** (counter-interpretation exists): "Counter-interpretation: [state it]. Rebuttal: [explain why it does not hold using the evidence from Step 4]."

**Option B** (no counter-interpretation): "No plausible counter-interpretation was identified. [One sentence explaining why the results are not susceptible to an alternative reading.]"

---

**Step 6 — State the verdict.**

Confirmed? Refuted? Inconclusive? Say it plainly.

Then explain why. This explanation is not the results again. It is the reasoning that bridges the evidence to the conclusion — the sentence that says *why* the delta you observed leads to the verdict you are stating. One to three sentences.

---

**Step 7 — Name a limitation and a next step.**

One limitation: an honest constraint on what this prototype proves.

One next step: something specific enough to execute in the next session. Not "do more testing." Name the specific thing to test, build, or change.

*End this step with exactly one of the following two closing sentences. Choose the one that applies. No other form of closing is permitted.*

**Option A** (meaningful limitation found): "This limitation affects the verdict's generalizability in the following way: [one sentence]."

**Option B** (no significant limitation): "No limitations beyond the scope exclusions in Step 1 were identified. [One sentence explaining why the scope exclusions are sufficient.]"

---

**Step 8 — Write the replication path.**

List every tool, input, command, and step needed to reproduce this prototype from scratch. Numbered list. No implicit steps. Configuration files named.

*End this step with exactly one of the following two closing sentences. Choose the one that applies. No other form of closing is permitted.*

**Option A** (replication path complete): "Replication path is complete. All tools, inputs, and steps are enumerated above."

**Option B** (replication path incomplete): "Replication path is incomplete. Missing: [what and why]."

---

**One rule above all:** The measurement protocol from Step 2 — including the gate line `Measurement protocol established before build.` — must appear in your output before the build description in Step 3. This gate line is structural evidence that the evidentiary standard was set before the results were known. Do not retroactively insert it. Do not skip it.

---

## V-05 — Hybrid Phase-Table (Phase Gates + Tables)

**Axis**: Combination (lifecycle emphasis + table-dominant format)
**Hypothesis**: Combining phase-gate markers with intra-phase tables achieves maximum criterion coverage — phase gates provide the inline ordering constraints needed for C-19, intra-phase tables enforce co-location for C-17, and phase-close blocks with named A/B dispositions satisfy C-18; this combination removes the single-failure-mode risk of each approach used alone.

---

You are running /prove:prototype.

This prompt uses a hybrid format. Each phase is named, gated, and contains a table. The phase header carries the ordering constraint for that phase (C-19). The table within each phase enforces structural co-location of rationale (C-17). Optional phases close with a named A/B disposition block (C-18). Both mechanisms operate simultaneously.

Read the phase gate before writing each phase.

---

#### Phase 1 — Hypothesis
*[Phase gate: this phase must produce the first element of your output. Nothing precedes it.]*

| Field | Content |
|-------|---------|
| Hypothesis | [restate the hypothesis in one to two sentences; this row must be first in your output] |

---

#### Phase 2 — Prototype Scope
*[Phase gate: complete this phase before any measurement criteria or build content appears. Scope must be established first.]*

| In Scope | Out of Scope | Why this exclusion does not invalidate the test |
|----------|--------------|--------------------------------------------------|
| [item]   | [item]       | [one sentence; must answer: why does the hypothesis remain testable without this?] |
| [item]   | [item]       | [one sentence; must answer: why does the hypothesis remain testable without this?] |

Rules:
- At least two Out-of-Scope rows.
- Third column must be populated in every row. "It wasn't needed" fails.

---

#### Phase 3 — Measurement Protocol
*[Phase gate: complete every row in this table before Phase 4 begins. This phase establishes the evidentiary standard the build will be held to. A measurement protocol must exist in the output before any build content can appear.]*

| Field | Content |
|-------|---------|
| Metric | [what will be measured] |
| Success condition | [value or event that confirms the hypothesis] |
| Failure condition | [value or event that refutes the hypothesis] |
| Predicted outcome | [which condition you expect; one sentence of reasoning] |

---

#### Phase 4 — Build Record
*[Phase gate: Phase 3 must be complete and present in your output before this phase begins.]*

| Step | Tool | Input | Output |
|------|------|-------|--------|
| [action taken] | [tool name] | [exact parameter or file; configuration files named] | [what was produced] |

Rules:
- No implicit steps.
- Every tool, input, and command named explicitly enough for reproduction.

---

#### Phase 5 — Results
*[Phase gate: Phase 4 must be complete and present in your output before this phase begins.]*

| Metric | Predicted | Actual | Delta (predicted − actual) | Why the delta is what it is |
|--------|-----------|--------|---------------------------|------------------------------|
| [name] | [from Phase 3] | [observed; one concrete data point — a number, a time, a count, or a direct quote] | [computed gap; write "0 — prediction confirmed" if match; do not leave this for the reader to infer] | [explanation here, in this row — not in a separate section] |

Rules:
- Delta column is mandatory. Compute it explicitly.
- "Why the delta is what it is" must appear in the same row as the delta.

---

#### Phase 6 — Counter-Evidence
*[Phase gate: Phase 5 must be complete and present in your output before this phase begins.]*

Consider whether the results could be explained by something other than the hypothesis being true or false.

| Candidate counter-interpretation | Assessment |
|----------------------------------|------------|
| [state one possible alternative explanation, or write "None identified"] | [REBUTTED: [reason] — OR — NONE: [reason none applies]] |

*Phase close — write exactly one of the following as the terminal element of this phase:*

**A** (counter-interpretation found and rebutted):
> Counter-interpretation: [restate]. Rebuttal: [evidence-grounded reason it does not hold].

**B** (no counter-interpretation):
> No plausible counter-interpretation was identified. Reason: [one sentence].

---

#### Phase 7 — Verdict
*[Phase gate: Phase 6 must be complete and its phase-close disposition must be present in your output before this phase begins.]*

| Verdict | Verdict Rationale |
|---------|------------------|
| [Confirmed / Refuted / Inconclusive] | [one to three sentences explaining why the delta in Phase 5 supports this verdict; this is not a restatement of Phase 5 — it is the reasoning that connects the evidence to the conclusion; it appears in this row] |

---

#### Phase 8 — Limitations and Next Step

| Limitation | Next Step |
|------------|-----------|
| [one scope constraint affecting generalizability] | [one action concrete enough to execute next session; "do more testing" fails] |

*Phase close — write exactly one of the following as the terminal element of this phase:*

**A** (meaningful limitation found):
> This limitation affects the verdict's generalizability in the following way: [one sentence].

**B** (no significant limitation):
> No limitations beyond the scope exclusions in Phase 2 were identified. Reason: [one sentence].

---

#### Phase 9 — Replication Path

List every tool, input, command, and step needed to reproduce the build as a numbered list. No implicit steps. Configuration files named.

*Phase close — write exactly one of the following as the terminal element of this phase:*

**A** (replication complete):
> Replication path is complete. All tools, inputs, and steps are enumerated above.

**B** (replication incomplete):
> Replication path is incomplete. Missing: [what and why].

---

#### Output Contract

Before submitting your output, verify all of the following:

1. Phase 1 is the first element of the output.
2. Phase 3 appears before Phase 4 in the output.
3. Phase 5 appears before Phase 6 in the output.
4. Phase 6 appears before Phase 7 in the output.
5. Every table cell is populated. Write "N/A" only where genuinely not applicable — with an inline reason.
6. Phases 6, 8, and 9 each close with an explicit A or B phase-close block.
7. Delta is a computed gap in its own column — not left for the reader to infer.
8. "Why the delta is what it is" appears in the same row as the delta.
9. "Verdict rationale" appears in the same row as the verdict.
10. Every inline phase gate marker is present in the output — they are not present only in this output contract.

---

## Criterion Coverage Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Hypothesis first | Inline gate Section 1 | Phase 1 execute-before | Block 1 gate | "Before anything else" | Phase 1 gate |
| C-02 Scope defined | Table ≥2 rows, col 3 enforces test-validity | Phase 2 per-exclusion pair | Block 2 labeled pairs | Step 1 per-item reason | Phase 2 table col 3 |
| C-03 Measure before build | Inline gate Section 3 + "stop and complete" | Phase 3 execute-before + gate check | Block 3 gate + precedes Block 4 | Step 2 gate line written by model | Phase 3 gate + output contract |
| C-04 Actual vs predicted | Table columns | Phase 5 labeled fields | Block 5 labeled pairs | Step 4 explicit gap | Phase 5 table |
| C-05 Verdict | Table Section 7 | Phase 7 labeled field | Block 7 labeled pair | Step 6 plain statement | Phase 7 table |
| C-06 Minimality | Table col 3 + ≥2 exclusions | Phase 2 test-validity per exclusion | Block 2 per-exclusion | Step 1 per-item | Phase 2 table |
| C-07 Raw evidence | Actual column: "one concrete data point" | Phase 5 "include at least one concrete data point" | Block 5 Actual field | Step 4 "concrete data point" | Phase 5 table rules |
| C-08 Limitations + next step | Table Section 8 | Phase 8 labeled fields | Block 8 | Step 7 | Phase 8 table |
| C-09 Counter-evidence rebutted | Section 6 Disposition A | Phase 6 Disposition A | Block 6 terminal pair A | Step 5 Option A | Phase 6 phase-close A |
| C-10 Replication path | Section 9 numbered list | Phase 9 numbered list | Block 9 numbered list | Step 8 numbered list | Phase 9 numbered list |
| C-11 No blank sections | Output contract rule 5 | Gate checks require each phase to be written | Structural rule 1 | "Follow them in order" + gate lines | Output contract rule 5 |
| C-12 Measurement ordering explicit | Section 3 inline gate + output contract | Phase 3 execute-before + gate check | Block 3 inline gate | Step 2 gate line + final rule | Phase 3 gate + output contract |
| C-13 Delta computed not co-reported | Table column "Delta (predicted − actual)" + "do not leave for reader" | Phase 5 Delta labeled field "do not merge" | Block 5 Delta labeled field | Step 4 "I predicted X. I observed Y. The gap is Z." | Phase 5 Delta column |
| C-14 Verdict rationale distinct | Table row + "not a restatement" | Phase 7 "not a restatement" | Block 7 "not a restatement" | Step 6 "not the results again" | Phase 7 table "not a restatement" |
| C-15 Each exclusion answers test-validity | Col 3 header = test-validity question per row | Per-exclusion "why remains valid" inline | Per-exclusion labeled pair | Per-item "why the test is still valid" | Col 3 header per row |
| C-16 Counter-evidence closed | Section 6 two-path terminal | Phase 6 A/B gate check | Block 6 two-path terminal pair | Step 5 two closing sentences | Phase 6 A/B phase-close |
| C-17 Rationale co-located | Tables: rationale in same row; output contract | Phase labeled-pair blocks: rationale in same block | Labeled pairs: rationale in same block | Same paragraph rule | Tables: rationale in same row |
| **C-18 Optional sections binary disposed** | **Sections 6, 8, 9 each: Disposition A or B terminal** | **Phases 6, 8, 9 each: A/B gate check** | **Blocks 6, 8, 9 each: terminal labeled pair A or B** | **Steps 5, 7, 8 each: two closing sentence options** | **Phases 6, 8, 9 each: A/B phase-close block** |
| **C-19 Ordering gate co-located inline** | **Sections 1, 2, 3, 4, 5, 6, 7 each carry *[Gate: ...]* inline** | **Every phase carries *Execute before/after Phase N* inline** | **Every block carries *[Gate: ...]* in block header** | **Step 2 gate line written into output by model** | **Every phase carries *[Phase gate: ...]* inline + output contract** |
