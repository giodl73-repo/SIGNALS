# topic-retro — Variate Round 2 (V-01 through V-05)

---

## V-01 — Axis: Output Format (Table-driven)
**Hypothesis**: Structured tables force explicit verdict labeling per signal (C-02) and make the accuracy ratio (C-08) computable at a glance, reducing prose hedging that obscures wrong predictions.

---

### Prompt Body

You are running a **topic-retro** — a post-commitment retrospective on the signals gathered for a topic before a feature decision was made.

**Input** (provide before running):
- Topic name
- Commitment made (what was decided, when)
- List of signals gathered (or path to `simulations/TOPICS.md` entry)
- AMEND (optional): focus on a specific signal type and/or time window

---

**Step 1 — Commitment Context**

State in two sentences:
1. The topic and the commitment made.
2. The date committed and the signal state at that time (how many signals existed, across how many namespaces).

---

**Step 2 — Signal Accuracy Table**

Build this table. One row per signal gathered before commitment.

| Signal | Namespace | Prediction | Actual Outcome | Verdict |
|--------|-----------|------------|----------------|---------|
| (name) | (ns)      | (what was expected) | (what shipped/happened) | CORRECT / WRONG / PARTIAL |

Rules:
- Every row must carry a verdict. "Unknown" is not a verdict.
- PARTIAL counts as wrong for accuracy scoring.
- If AMEND is set, include only signals in the specified type or window. Note omissions at table bottom.

Immediately after the table, state the accuracy ratio:

> **Accuracy**: N correct / M total = X%

---

**Step 3 — Coverage Summary Table**

| Namespace | Signals Gathered | Signals Absent | Note |
|-----------|-----------------|----------------|------|
| scout | | | |
| draft | | | |
| review | | | |
| flow | | | |
| trace | | | |
| prove | | | |
| listen | | | |
| program | | | |
| topic | | | |

Mark each namespace as: **Present** / **Absent** / **Partial**. One-line note only where Absent or Partial.

---

**Step 4 — Gaps**

List gaps that would have changed the commitment decision. Use this format per gap:

**Gap**: [signal that was missing]
**Namespace**: [which namespace would have produced it]
**Decision impact**: [how the commitment would have differed if this signal existed]
**Inertia note**: [what assumption the team was relying on in its absence — the "we assumed" statement]

Minimum: one gap. Maximum: three gaps. If no gaps changed the decision, state that explicitly.

---

**Step 5 — Echo**

State exactly one Echo — the finding that was not predicted by any signal gathered, not a restatement of a wrong prediction.

**Echo**: [one sentence]
**Why it wasn't predicted**: [one sentence — what signal type would have caught this, or why none would have]
**Systemic pattern**: [name a pattern this Echo resembles across prior topics, or state "no prior pattern identified"]

---

**Step 6 — Improvement Recommendation**

One recommendation only. Name the specific gap or Echo it addresses. State the practice change.

> **Recommendation**: [practice change] addresses [Gap N / Echo] by [mechanism].

---

**AMEND handling**: If AMEND specifies a signal type, restrict Steps 2–4 to that type and note the restriction in the header. If AMEND specifies a time window, exclude signals outside the window and state the window used.

---

---

## V-02 — Axis: Phrasing Register (Conversational/Interrogative)
**Hypothesis**: Question framing guides the model to surface the right content without over-specifying structure, leading to more organic Echo discovery (C-04) and richer gap impact statements.

---

### Prompt Body

This is a **topic-retro**. You shipped something. Now look back at what the signals said — and whether they were right.

Answer these questions in order. Each answer becomes a section of the retrospective.

---

**Before you start**: Confirm the topic name, what was committed, and when. One paragraph. If you don't know these, stop and ask.

---

**Q1: What signals did you gather?**

Walk through each signal gathered before the commitment. For each one, say what you expected it to show — and what actually happened. Was the signal right?

Keep it grounded. "Scout said the market was clear. It was wrong — a competitor launched two weeks later." That's what you're looking for.

End this section with a simple count: how many signals were correct, how many were wrong.

---

**Q2: Where were the blank spots?**

Look at all nine namespaces: scout, draft, review, flow, trace, prove, listen, program, topic. Which ones had no signal? Which ones had thin coverage?

For any blank spot that mattered — that is, where a signal could have changed the decision — say what you were assuming in its absence. What did the team believe without evidence?

Be direct. "We assumed users would tolerate the latency. We had no listen signals. We were wrong."

---

**Q3: What was the one thing you didn't see coming?**

Not a signal that was wrong. Something that no signal predicted at all — something genuinely outside the model you were operating with before committing.

State it in one sentence. Then explain why no signal would have caught it, and whether this has happened before on other topics.

This is the Echo. There should be exactly one. If you are tempted to list two, pick the more surprising one.

---

**Q4: What would you do differently next time?**

One recommendation. Connect it directly to the gap or the Echo you named. What changes — which namespace gets more coverage, which signal gets run earlier, what question gets asked before commitment?

---

**AMEND**: If the retro is scoped to a specific signal type or time window, say so at the top and answer only within that scope. Flag what's being excluded.

---

---

## V-03 — Axis: Lifecycle Emphasis (Explicit Phase Boundaries, Equal Weight)
**Hypothesis**: Hard section labels with equal space budgets prevent Gaps from collapsing into Signal Accuracy and ensure the Echo is produced independently rather than as a residual from the wrong-predictions list.

---

### Prompt Body

Run a **topic-retro** for the named topic. This retrospective has five phases of equal importance. Do not compress any phase. Do not merge phases. Each phase produces a distinct deliverable.

---

**PHASE 1 — CONTEXT** *(deliverable: commitment statement)*

Establish:
- Topic name
- Commitment made (what, when)
- Signal inventory at commitment time (count by namespace)

If AMEND is active, state the scope restriction here and carry it through all phases.

---

**PHASE 2 — SIGNAL ACCURACY** *(deliverable: signal ledger with verdicts)*

For each signal gathered before commitment:
- Name the signal
- State the prediction it carried
- State the actual outcome after commitment
- Assign verdict: CORRECT, WRONG, or PARTIAL

PARTIAL counts as WRONG for scoring.

Close this phase with: **Accuracy: N/M (X%)** — calculated from the ledger above.

This phase covers only signals that existed before commitment. Post-commitment signals do not belong here.

---

**PHASE 3 — COVERAGE** *(deliverable: namespace coverage map)*

For each of the nine namespaces, state whether signals were Present, Absent, or Partial at commitment time. Note any namespace where absence was a deliberate choice vs. an oversight.

This phase describes the shape of the evidence base — not whether the signals were right.

---

**PHASE 4 — GAPS** *(deliverable: decision-impact gap list)*

A gap is a missing signal whose presence would have changed the commitment.

For each gap:
1. Name the missing signal and its namespace
2. State the decision impact: how the commitment would have differed
3. State the inertia assumption: what the team believed without evidence

If no missing signal would have changed the commitment, state that explicitly with a one-sentence rationale.

Maximum three gaps. If more than three apply, select the three with the largest decision impact.

---

**PHASE 5 — ECHO** *(deliverable: one unpredicted finding + pattern link)*

The Echo is what happened that no gathered signal predicted and no gap analysis would have surfaced. It is genuinely outside the pre-commitment model.

Rules:
- Exactly one Echo
- Not a restatement of a WRONG signal — those belong in Phase 2
- Framed as: "This happened, and nothing we gathered would have predicted it"

After stating the Echo:
- Name the signal type that might have caught it, if any
- State whether this pattern has appeared in prior topic retrospectives

Close with one improvement recommendation tied directly to the Echo or the highest-impact gap from Phase 4.

---

---

## V-04 — Combined Axes: Role Sequence (Commitment Narrator Leads) + Inertia Framing (Status Quo Competitor Named Explicitly)
**Hypothesis**: Naming "what we would have done without these signals" sharpens gap impact (C-03) and elevates the Echo as a genuine surprise against a concrete baseline, rather than an abstract omission. Commitment narrator role grounds the retro in a real decision before the analyst evaluates it.

---

### Prompt Body

You are running a **topic-retro**. Two roles operate in sequence.

---

**ROLE 1 — COMMITMENT NARRATOR**

The Commitment Narrator reconstructs what was known and believed at the moment of commitment — from memory, not from hindsight. This role speaks in past tense, as of the commitment date.

Narrator output (produce this before any analysis):

> **Topic**: [name]
> **Commitment**: [what was decided]
> **Date**: [when]
> **What we knew**: [signals gathered, by namespace, in one sentence each]
> **What we assumed without evidence**: [explicit list of inertia assumptions — things the team believed because it was the default, not because a signal supported it]
> **The status quo option**: [what the team would have done if no signals had been gathered — the baseline decision inertia was pointing toward]

The status quo option is required. It names the path the team was on before signal gathering changed anything. If signals didn't change the path, say so.

---

**ROLE 2 — SIGNAL ANALYST**

The Signal Analyst evaluates the Narrator's reconstruction against what actually happened. This role has full hindsight.

**Section A — Signal Accuracy**

For each signal named by the Narrator:
- Prediction carried by the signal
- Actual outcome
- Verdict: CORRECT / WRONG / PARTIAL

Accuracy ratio: N/M (X%)

**Section B — Gap Analysis**

For each inertia assumption named by the Narrator: did the team have evidence for it, or was it flying blind?

For assumptions with no supporting signal that turned out to matter:

| Assumption | Signal that was missing | Namespace | Decision impact |
|------------|------------------------|-----------|----------------|
| | | | |

Decision impact = how the commitment would have differed with evidence.

Anchor every gap to one of the Narrator's named assumptions. Do not invent new assumptions here.

**Section C — Echo**

One finding the Narrator's model could not have generated. Not a wrong signal. Not a missed assumption. Something entirely outside the pre-commitment frame.

State it. Explain why the Narrator's model had no slot for it. Name a prior pattern if one exists.

**Section D — Recommendation**

One practice change. Addresses the highest-impact gap from Section B or the Echo from Section C. Names the specific namespace or signal type it targets.

---

**AMEND**: If scoped to a signal type or time window, the Narrator restricts "what we knew" to that scope. The Analyst evaluates only within scope. Both roles note the restriction.

---

---

## V-05 — Combined Axes: Output Format (Prose Narrative) + Role Sequence (Echo-First, Reconstruct Backward)
**Hypothesis**: Starting with the Echo and working backward forces the model to treat the unexpected finding as load-bearing rather than a residual, producing richer systemic pattern linkage (C-09) and preventing the Echo from being a recycled wrong-prediction in disguise.

---

### Prompt Body

Run a **topic-retro** in reverse chronological order. Begin with what surprised you most. Reconstruct backward to understand why the signals didn't see it coming.

This is a prose-first retrospective. Write in paragraphs. Tables are permitted only in the Signal Accuracy section (Step 4).

---

**Step 1 — The Echo (write this first)**

Before reviewing any signal, state the one thing that happened after commitment that no pre-commitment signal predicted.

Write it as a short paragraph: what happened, why it was surprising, and in one sentence — what it suggests about the limits of the signal model used for this topic.

This is the Echo. It must be written before Step 2. Do not revise it after completing Steps 2–5.

If AMEND is active (scoped signal type or time window), state the scope restriction here. The Echo must come from within scope.

---

**Step 2 — Commitment Context**

Now establish the ground: what topic, what commitment, when. One paragraph. Include the count of signals gathered by namespace at commitment time.

---

**Step 3 — Working Backward: Why Didn't We See the Echo Coming?**

Name each signal that was gathered and explain, in prose, whether it pointed toward or away from the Echo. For signals that pointed away: was the prediction simply wrong, or was the Echo genuinely outside what the signal could observe?

This section reconstructs the gap between the signal model and the Echo. It should read as a narrative of the pre-commitment epistemic state, not a list of verdicts.

---

**Step 4 — Signal Accuracy Ledger**

Now formalize the accuracy accounting. Build the table:

| Signal | Namespace | Prediction | Actual | Verdict |
|--------|-----------|------------|--------|---------|
| | | | | CORRECT / WRONG / PARTIAL |

State the accuracy ratio immediately after: **N/M (X%)**

---

**Step 5 — Gaps**

Name up to three gaps — signals not gathered whose presence would have changed the commitment. For each gap, write one paragraph:
- What signal was missing
- What the team assumed in its absence (the inertia assumption)
- How the commitment would have been different with that signal

Prioritize gaps that connect to the Echo from Step 1.

---

**Step 6 — Pattern and Recommendation**

Return to the Echo. Does it resemble a pattern seen in prior topic retrospectives? Name the pattern or say "no prior pattern identified."

Close with one recommendation. It must connect to either the highest-impact gap or the Echo pattern. Name the specific practice change and the namespace it targets.

---
