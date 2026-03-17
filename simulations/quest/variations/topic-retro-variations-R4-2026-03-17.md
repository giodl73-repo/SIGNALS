# topic-retro Skill Variations — Round 4

---

## V-01 — Single Axis: Output Format (Table-Heavy)

**Axis**: Output format — structured tables dominate over prose  
**Hypothesis**: Forcing tabular output for signals, coverage, and gaps will mechanically satisfy C-02 (verdict labels), C-15 (accuracy ratio), C-16 (namespace coverage table), and C-17 (recommendation template) without requiring extra instruction, because the column headers themselves enforce the required fields.

---

```
You are running /topic-retro for the topic: {{topic}}.

A commitment was made on this topic. Now that the feature has shipped (or a milestone was reached), run a structured retrospective over the signals that were gathered before the commitment.

## Context

Topic: {{topic}}
Commitment: {{commitment_description}}
Signals directory: simulations/ (check all namespace subdirectories)
Date of commitment: {{commitment_date}}
Date of retro: {{retro_date}}

---

## Step 1 — Locate and Inventory Signals

Scan simulations/ for all artifact files associated with {{topic}}. List every signal found, organized by namespace.

The 9 namespaces are: scout, draft, review, flow, trace, prove, listen, program, topic.

Produce a namespace coverage table:

| Namespace | Signal File(s) | Gathered? |
|-----------|---------------|-----------|
| scout     | ...           | Yes / No  |
| draft     | ...           | Yes / No  |
| review    | ...           | Yes / No  |
| flow      | ...           | Yes / No  |
| trace     | ...           | Yes / No  |
| prove     | ...           | Yes / No  |
| listen    | ...           | Yes / No  |
| program   | ...           | Yes / No  |
| topic     | ...           | Yes / No  |

Count: X of 9 namespaces covered.

---

## Step 2 — Signal Accuracy Table

For each signal found, extract what the signal predicted and compare it to what actually happened after the commitment.

Produce this table:

| Signal | Namespace | Prediction | Actual Outcome | Verdict |
|--------|-----------|------------|----------------|---------|
| ...    | ...       | ...        | ...            | CORRECT / WRONG / PARTIAL |

Below the table, state the accuracy ratio:
**Accuracy: N/M = X%** (correct or partial / total signals assessed)

---

## Step 3 — Gaps

Gaps are signals that were absent before the commitment AND whose absence mattered — meaning having them would likely have changed the decision or the approach.

Produce a gaps table:

| Gap | Missing Namespace | What It Would Have Revealed | Decision Impact |
|-----|------------------|-----------------------------|-----------------|
| ... | ...              | ...                         | Would have changed X / Would have changed timing / Would have added condition |

If no gaps apply, write: **No decision-relevant gaps identified.**

---

## Step 4 — Echo

The Echo is the single most unexpected finding from post-commitment reality — something not predicted by any signal, not a restatement of a wrong prediction, but a genuinely new learning.

Write exactly one Echo:

**Echo**: [one-sentence statement of the unexpected finding]

Then explain in 2–4 sentences: why it was unpredicted, what it reveals about signal quality, and whether it points to a systemic gap in how signals were gathered for this topic.

---

## Step 5 — Improvement Recommendation

Write one recommendation that directly addresses the most significant gap or the Echo.

Use this template:
**This recommendation addresses [name the Gap or Echo] by [specific practice change].**

Then write 2–3 sentences elaborating on the change and when to apply it.

---

## Output Format

Produce the full retro as a Markdown document with these top-level sections:

1. Topic and Commitment Context
2. Namespace Coverage Table
3. Signal Accuracy Table + Accuracy Ratio
4. Gaps Table
5. Echo
6. Improvement Recommendation

Do not add sections. Do not omit sections.
```

---

## V-02 — Single Axis: Phrasing Register (Conversational + Imperative)

**Axis**: Phrasing register — direct, plain-English imperatives throughout  
**Hypothesis**: Stripping formal structure in favor of short imperative commands ("Do X. Then do Y.") reduces friction for the AI and produces more natural, readable output while still hitting the structural criteria — the rubric criteria are embedded as action verbs, not described as requirements.

---

```
Run a post-commitment retrospective on topic: {{topic}}.

The feature shipped. Now look back. Did the signals tell the truth?

---

**What you need to know going in:**
- Topic: {{topic}}
- Commitment made: {{commitment_description}}
- Commitment date: {{commitment_date}}
- Today: {{retro_date}}
- Where signals live: simulations/ subdirectories, organized by namespace

---

**Section 1 — What happened**

Open with one paragraph: what the topic was, what was committed to, and what actually shipped. Keep it to 3–5 sentences. This is context for a reader who wasn't in the room.

---

**Section 2 — What signals existed**

Go through all 9 namespaces (scout, draft, review, flow, trace, prove, listen, program, topic). For each one, say whether a signal exists for this topic. Show this as a table — namespace, file name or "none", and gathered yes/no.

After the table: how many of 9 namespaces had coverage?

---

**Section 3 — Were they right?**

For every signal you found, say what it predicted and what actually happened. Give each signal a verdict: CORRECT, WRONG, or PARTIAL. Be blunt — vague verdicts like "mostly right" don't count.

Then state the accuracy ratio plainly: "X out of M signals were correct or partially correct (X/M = Y%)."

---

**Section 4 — What was missing**

Name any gaps — signals that weren't gathered but would have mattered. For each gap, say what it would have told you and how it would have affected the decision. If nothing was missing that mattered, say so.

---

**Section 5 — The one surprise**

Pick the single most unexpected thing you learned after the commitment. Not a wrong prediction — something genuinely new that no signal anticipated. Call it the Echo.

Write one sentence stating it. Then explain in a short paragraph why it wasn't predicted and what it tells you about how signals were gathered.

---

**Section 6 — One thing to do differently**

Write one concrete recommendation. Name the specific gap or Echo it responds to. Use this sentence structure: "This recommendation addresses [gap or echo name] by [what you'd do differently]." Then add 2–3 sentences on how to apply it.

---

Keep the whole document tight. No bullet lists in the accuracy and gap sections — use tables. No more than one Echo.
```

---

## V-03 — Single Axis: Lifecycle Emphasis (Explicit Phase Boundaries with Word Budgets)

**Axis**: Lifecycle emphasis — each retrospective phase has a named stage, explicit entry/exit conditions, and a word budget  
**Hypothesis**: Treating the retro as a multi-phase lifecycle with explicit phase gates (not just sections) will prevent the AI from collapsing phases together, which is the most common failure mode — especially conflating "wrong predictions" with the Echo.

---

```
/topic-retro — Post-Commitment Signal Retrospective

Topic: {{topic}}
Commitment: {{commitment_description}}

This skill runs in five phases. Each phase has an entry condition and an exit condition. Do not proceed to the next phase until the current one is complete. Budget guidance is approximate — substance over length.

---

## Phase 1: ORIENT
**Entry**: Begin here.
**Task**: Establish context for a reader new to this topic.
  - State the topic name and what problem it addresses (1–2 sentences).
  - State the nature of the commitment: what was decided, by whom, and when.
  - State the retrospective date and what triggered it (shipped feature, milestone, cutoff).
**Exit**: Context is clear. A reader knows what was committed and why.
**Budget**: ~100 words.

---

## Phase 2: AUDIT
**Entry**: Phase 1 complete.
**Task**: Take inventory of all signals gathered before the commitment.
  - Scan simulations/ for all artifacts tagged to {{topic}}.
  - Classify each artifact by namespace. The 9 namespaces: scout, draft, review, flow, trace, prove, listen, program, topic.
  - Produce an explicit namespace coverage table: namespace | artifact filename | gathered (Y/N).
  - After the table, state coverage count: "X of 9 namespaces covered."
**Exit**: Every namespace is accounted for. No namespace is left ambiguous.
**Budget**: Table + 1 summary sentence. No prose substitutes for the table.

---

## Phase 3: SCORE
**Entry**: Phase 2 complete. You know exactly which signals existed.
**Task**: Evaluate prediction accuracy for each signal.
  - For each gathered signal, identify what it predicted pre-commitment.
  - Compare prediction to post-commitment actuals.
  - Assign a verdict: CORRECT, WRONG, or PARTIAL. Each verdict must be a column value — not embedded in prose.
  - Produce a signal accuracy table: signal name | namespace | prediction | actual outcome | verdict.
  - Below the table, state the accuracy ratio: "N/M signals correct or partial = X%."
**Exit**: Every signal has a verdict. Accuracy ratio is computed.
**Budget**: Table + 1 ratio line. No narrative verdicts.

---

## Phase 4: GAP + ECHO
**Entry**: Phase 3 complete.

This phase has two distinct outputs. Do not merge them.

**4a — Gaps**
  - Identify signals that were absent AND that would have changed the decision or approach.
  - For each gap: name it, identify which namespace it belongs to, state what it would have revealed, state the decision impact.
  - If no decision-relevant gaps exist, state: "No decision-altering gaps identified." Do not skip this section.

**4b — Echo**
  - Identify the single most unexpected post-commitment finding — something no signal predicted and not a restatement of a wrong prediction.
  - Write exactly one Echo statement (one sentence).
  - Explain in 2–4 sentences: what made it unpredicted, what it reveals about signal coverage for this topic, and whether it points to a systemic pattern across future topics.
  - If multiple surprises exist, select only the most significant. Label it Echo.

**Exit**: At least one gap assessed (even if none found). Exactly one Echo written.
**Budget**: Gap table or statement (~50–100 words). Echo statement + explanation (~75–100 words). Keep them visually separate.

---

## Phase 5: IMPROVE
**Entry**: Phase 4 complete.
**Task**: Write one improvement recommendation.
  - Name the specific gap or Echo it responds to.
  - Use the template: "This recommendation addresses [gap or echo] by [mechanism / practice change]."
  - Extend with 2–3 sentences: what changes in practice, when to apply it, and what signal improvement is expected.
**Exit**: One recommendation, one named anchor (gap or echo), one mechanism.
**Budget**: ~75–100 words.

---

## Final Output

Assemble all five phases into a single Markdown document. Use phase names as top-level headers:

- ORIENT
- AUDIT
- SCORE
- GAP + ECHO
- IMPROVE

Do not add phases. Do not combine phases.
```

---

## V-04 — Combined Axes: Output Format (Table-Heavy) + Role Sequence

**Axes combined**: Structured table output (V-01) + explicit role sequence (auditor → scorer → analyst → synthesizer)  
**Hypothesis**: Assigning distinct cognitive roles in sequence — each one consuming the previous role's table output — will produce cleaner signal-by-signal analysis than a single undifferentiated pass, because each role has narrower scope and a constrained output format it must fill before handing off.

---

```
/topic-retro — Post-Commitment Signal Retrospective

Topic: {{topic}}
Commitment: {{commitment_description}}
Commitment date: {{commitment_date}}
Retro date: {{retro_date}}

This skill runs through four sequential roles. Each role produces a structured artifact that the next role consumes. Complete each role fully before moving to the next.

---

## Role 1: Signal Auditor

**Task**: Locate and inventory all signals associated with {{topic}}.

Scan simulations/ across all 9 namespaces: scout, draft, review, flow, trace, prove, listen, program, topic.

Produce the Signal Inventory Table:

| Namespace | Signal File | Signal Type | Gathered? | Has Prediction? |
|-----------|-------------|-------------|-----------|-----------------|
| scout     | ...         | ...         | Yes / No  | Yes / No        |
| draft     | ...         | ...         | Yes / No  | Yes / No        |
| review    | ...         | ...         | Yes / No  | Yes / No        |
| flow      | ...         | ...         | Yes / No  | Yes / No        |
| trace     | ...         | ...         | Yes / No  | Yes / No        |
| prove     | ...         | ...         | Yes / No  | Yes / No        |
| listen    | ...         | ...         | Yes / No  | Yes / No        |
| program   | ...         | ...         | Yes / No  | Yes / No        |
| topic     | ...         | ...         | Yes / No  | Yes / No        |

Summary line: "X of 9 namespaces covered. Y signals with extractable predictions."

Hand off to Role 2.

---

## Role 2: Accuracy Scorer

**Input**: Signal Inventory Table from Role 1.
**Task**: For every signal that has a prediction (Role 1, "Has Prediction?" = Yes), compare the prediction to post-commitment actuals.

Produce the Signal Accuracy Table:

| Signal | Namespace | Prediction (pre-commitment) | Actual Outcome (post-commitment) | Verdict |
|--------|-----------|----------------------------|----------------------------------|---------|
| ...    | ...       | ...                        | ...                              | CORRECT / WRONG / PARTIAL |

Verdict rule: CORRECT = outcome matched prediction. WRONG = outcome contradicted prediction. PARTIAL = outcome partially matched. Do not use any other verdict values.

Accuracy summary line: "N/M signals assessed. X correct, Y partial, Z wrong. Accuracy ratio: (X + Y)/M = P%."

Hand off to Role 3.

---

## Role 3: Gap and Echo Analyst

**Input**: Signal Inventory Table (Role 1) + Signal Accuracy Table (Role 2).
**Task**: Two outputs. Produce both. Do not merge.

**Output A — Gap Table**

Identify namespaces or signal types that were absent (Role 1, "Gathered?" = No) and whose absence had decision impact — meaning gathering them would have changed the commitment or its conditions.

| Gap | Missing Namespace | What It Would Have Revealed | Decision Impact |
|-----|------------------|-----------------------------|-----------------|
| ... | ...              | ...                         | Changed decision / Changed scope / Added condition / No impact |

If no gaps had decision impact, write one row: "No decision-altering gaps identified" across all columns.

**Output B — Echo**

Review the post-commitment actuals in Role 2's table. Identify the single finding that was not predicted by any signal and is not simply a restatement of a WRONG verdict — it is genuinely new information.

Write:
**Echo**: [one sentence]
**Why unpredicted**: [2–3 sentences explaining why no signal pointed here]
**Systemic signal**: [1 sentence — does this suggest a recurring gap pattern, or is it a one-off?]

If multiple surprises exist, select the single most significant and label it Echo.

Hand off to Role 4.

---

## Role 4: Retrospective Synthesizer

**Input**: All outputs from Roles 1–3.
**Task**: Produce the final retrospective document.

**4a — Topic and Commitment Context**

Write 2–4 sentences: topic name, problem it addresses, commitment made, and retrospective date. This is the document header for readers who weren't present.

**4b — Namespace Coverage Table**

Copy the coverage columns from Role 1's Signal Inventory Table (Namespace | Gathered? only).

**4c — Signal Accuracy Table**

Copy Role 2's Signal Accuracy Table verbatim. Append the accuracy summary line.

**4d — Gaps**

Copy Role 3's Gap Table verbatim.

**4e — Echo**

Copy Role 3's Echo block verbatim.

**4f — Improvement Recommendation**

Write one recommendation that directly addresses the most significant gap from 4d or the Echo from 4e.

Required template: "This recommendation addresses [gap name or Echo] by [specific practice change]."

Then add 2–3 sentences: what changes in practice, when to apply it, expected signal improvement.

---

## Final Document Structure

1. Topic and Commitment Context
2. Namespace Coverage Table
3. Signal Accuracy Table + Accuracy Ratio
4. Gaps Table
5. Echo
6. Improvement Recommendation

Sections must appear in this order. Do not add or remove sections.
```

---

## V-05 — Combined Axes: Phrasing Register (Formal/Technical) + Inertia Framing (Prominent)

**Axes combined**: Formal/technical register (structured specification language) + prominent inertia framing (explicit comparison to what status-quo signal gathering would have produced)  
**Hypothesis**: Making the status-quo competitor explicit — "what would have happened with no structured signal gathering" — gives the Echo and Gap sections a concrete counterfactual anchor, sharpening both the accuracy assessment and the improvement recommendation by grounding them in a real alternative rather than an abstract standard.

---

```
/topic-retro

## Invocation Context

skill: topic-retro
topic: {{topic}}
commitment_description: {{commitment_description}}
commitment_date: {{commitment_date}}
retro_date: {{retro_date}}
signal_root: simulations/

---

## Preamble: Signal Gathering vs. Intuition-First

Before executing the retrospective, establish the baseline counterfactual. Signal gathering exists because intuition-first development produces predictable failure modes: wrong-direction effort, late-discovery surprises, and unactionable hindsight. The value of this retrospective is not to assign blame but to measure signal fidelity against that alternative — to determine whether the signals gathered were more accurate than informed guesswork would have been, and to identify where they were not.

---

## Section 1: Commitment Context

State the following:
1. **Topic**: {{topic}} — one sentence on the problem domain.
2. **Commitment**: {{commitment_description}} — what was formally decided and its scope.
3. **Commitment date**: {{commitment_date}}.
4. **Retrospective date**: {{retro_date}}.
5. **Counterfactual baseline**: In one sentence, characterize what the intuition-first approach to this commitment would have been — what would the team have done without structured signal gathering?

This section establishes the decision context and the comparison basis for all subsequent assessment.

---

## Section 2: Signal Coverage Audit

Enumerate all signal artifacts found in signal_root for topic {{topic}}, organized by namespace.

The 9 namespaces are: scout, draft, review, flow, trace, prove, listen, program, topic.

Produce the following table:

| Namespace | Signal File | Prediction Extractable | Coverage Status |
|-----------|-------------|----------------------|-----------------|
| scout     | ...         | Yes / No             | Gathered / Absent |
| draft     | ...         | ...                  | ...               |
| review    | ...         | ...                  | ...               |
| flow      | ...         | ...                  | ...               |
| trace     | ...         | ...                  | ...               |
| prove     | ...         | ...                  | ...               |
| listen    | ...         | ...                  | ...               |
| program   | ...         | ...                  | ...               |
| topic     | ...         | ...                  | ...               |

Coverage summary: "X of 9 namespaces covered. Y signals contain extractable predictions."

**Inertia note**: For each absent namespace, indicate in one clause whether intuition-first development would have addressed that dimension at all, partially (ad hoc), or not at all.

---

## Section 3: Prediction Accuracy Assessment

For each signal with an extractable prediction, assess fidelity against post-commitment actuals.

Produce the following table:

| Signal | Namespace | Pre-Commitment Prediction | Post-Commitment Actual | Verdict | Advantage Over Intuition |
|--------|-----------|--------------------------|----------------------|---------|--------------------------|
| ...    | ...       | ...                      | ...                  | CORRECT / WRONG / PARTIAL | Superior / Equivalent / Inferior |

**Verdict definitions**:
- CORRECT: Prediction matched actual outcome within acceptable tolerance.
- WRONG: Prediction contradicted actual outcome in a materially relevant way.
- PARTIAL: Prediction was directionally correct but missed scope, timing, or magnitude.

**Advantage Over Intuition definitions**:
- Superior: Signal produced a better-calibrated prediction than informed guesswork would have.
- Equivalent: Signal produced a prediction consistent with what experienced intuition would have yielded.
- Inferior: Signal produced a worse prediction than intuition would have — introduced false confidence.

Accuracy summary: "N/M signals assessed (Y correct, Z partial, W wrong). Accuracy ratio: (Y + Z)/N = P%. Superior-to-intuition signals: S/N."

---

## Section 4: Gap Analysis

Gaps are signal absences that were decision-relevant — where intuition-first development would have operated on assumption, and structured signal gathering would have replaced assumption with evidence.

For each identified gap:

| Gap | Missing Namespace | Intuition-First Assumption | What Signal Would Have Revealed | Decision Impact |
|-----|------------------|---------------------------|--------------------------------|-----------------|
| ... | ...              | ...                       | ...                            | Changed decision / Modified scope / Added safeguard / No impact |

If no decision-relevant gaps are identified, state: "No decision-altering signal gaps identified. Intuition-first assumptions were sufficient for this commitment."

---

## Section 5: Echo

The Echo is the single post-commitment finding that was not predicted by any gathered signal and represents genuinely new information — not a wrong prediction restated, but an unknown unknown that surfaced only after the commitment.

Write:

**Echo**: [One sentence stating the unexpected finding.]

**Why no signal predicted this**: [2–3 sentences. Identify which namespace would have been responsible for this signal had it been gathered. Was this a coverage gap, a prediction failure, or an unknowable at commitment time?]

**Inertia comparison**: [1 sentence. Would intuition-first development have predicted this finding, or would it have been equally surprised?]

**Systemic pattern**: [1 sentence. Is this Echo indicative of a recurring blind spot in signal gathering methodology, or a one-time anomaly?]

Select exactly one Echo. If multiple candidates exist, select the one with the highest potential to change future signal gathering strategy.

---

## Section 6: Improvement Recommendation

Write one recommendation derived from the most significant gap in Section 4 or the Echo in Section 5.

**Required structure**:

> This recommendation addresses [name the specific Gap or Echo] by [specific, implementable practice change].

Follow with:
1. **What changes**: Name the practice or process modification in concrete terms.
2. **When to apply**: Specify the point in the signal gathering workflow where this applies.
3. **Expected improvement**: State what fidelity gain or coverage improvement is expected relative to current practice.
4. **Inertia displacement**: State what assumption or intuition-first behavior this recommendation replaces.

---

## Output Specification

Produce a single Markdown document. Required sections in order:

1. Commitment Context
2. Signal Coverage Audit
3. Prediction Accuracy Assessment
4. Gap Analysis
5. Echo
6. Improvement Recommendation

Each section must be a top-level header (`##`). Tables are required for sections 2, 3, and 4. No section may be omitted. No additional sections may be added.
```

---

## Variation Summary

| Version | Axis (Primary) | Axis (Secondary) | Key Hypothesis |
|---------|---------------|-----------------|----------------|
| V-01 | Output format (table-heavy) | — | Column headers enforce rubric criteria mechanically |
| V-02 | Phrasing register (conversational/imperative) | — | Short imperatives reduce structural collapse risk |
| V-03 | Lifecycle emphasis (phase gates + budgets) | — | Explicit entry/exit conditions prevent phase merging |
| V-04 | Output format (tables) | Role sequence (4 roles) | Role handoffs narrow scope and prevent cross-contamination |
| V-05 | Phrasing register (formal/technical) | Inertia framing (prominent) | Counterfactual baseline sharpens Echo and Gap anchoring |
