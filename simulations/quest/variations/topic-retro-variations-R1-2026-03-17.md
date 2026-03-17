# topic-retro Variations — V-01 through V-05

---

## V-01 — Axis: Output Format (Table-First)

**Hypothesis:** Structured tables force completeness and make accuracy ratios scannable, preventing narrative drift that buries wrong predictions inside "nuanced" prose.

---

```markdown
You are running /topic-retro for topic: $TOPIC

A commitment was made. Now you review the signals that led to it.

---

## Step 1 — Anchor

State the topic name, the commitment made, and the date range covered.
One sentence each. No elaboration yet.

---

## Step 2 — Signal Accuracy Table

For every signal gathered before commitment, produce a row in this table:

| Signal | Namespace | Prediction | Actual Outcome | Verdict |
|--------|-----------|------------|----------------|---------|
| ...    | ...       | ...        | ...            | ✓ Correct / ✗ Wrong / ~ Partial |

Rules:
- Every signal artifact referenced in TOPICS.md for this topic gets a row.
- Prediction = what the signal said would be true post-ship.
- Actual Outcome = what happened.
- Verdict = Correct / Wrong / Partial. No other values.
- If a namespace has no signal row, explicitly add: `(none gathered)` as a row.
- State the accuracy ratio at the bottom: `X of Y signals correct (Z%)`.

---

## Step 3 — Gaps Table

Gaps are signals NOT gathered that, if gathered, would have changed the decision.

| Missing Signal | Namespace | What It Would Have Revealed | Decision Impact |
|----------------|-----------|----------------------------|-----------------|
| ...            | ...       | ...                         | Would have blocked / changed scope / confirmed faster |

Rules:
- Only include signals where the decision impact is concrete.
- "Would have been nice to know" does not qualify. "Would have changed X" does.
- If no gaps exist, state that explicitly with a one-sentence justification.

---

## Step 4 — Echo

The Echo is the one thing that actually happened that no signal predicted.

Write it as: **Echo:** [finding] — [why no signal would have caught this]

Rules:
- Echo is NOT a wrong prediction. Wrong predictions belong in Step 2.
- Echo is a thing that happened outside the prediction surface entirely.
- If there is no Echo, state "No Echo detected" and explain why the prediction surface was complete.
- Do not list multiple Echos. If you have more than one candidate, pick the one with highest surprise value.

---

## Step 5 — Improvement

State one concrete improvement to future signal gathering for this topic type.
Tie it to a specific Gap row (by namespace) or to the Echo.
Format: **Improve:** [what to do differently] — tied to [Gap: namespace / Echo]

---

## AMEND Instructions

If an AMEND scope is active:
- If AMEND specifies a signal type: restrict Step 2 and Step 3 to that namespace only.
  Re-state the accuracy ratio for that namespace alone.
- If AMEND specifies a time window: restrict all steps to signals gathered within that window.
  Note signals outside the window as "out of scope" rather than omitting them.
- Always preserve Echo (Step 4) — it is never scoped away.
```

---

## V-02 — Axis: Phrasing Register (Conversational/Interrogative)

**Hypothesis:** Question-driven prompts produce more honest self-assessment. Imperative prompts encourage performing completeness; questions expose what the model actually knows vs. what it's constructing.

---

```markdown
You are running /topic-retro for topic: $TOPIC

You committed to this feature. It shipped. Now look back.

---

**What was the commitment?**

Describe the topic and the decision that was made. What did the team agree to build or ship?
Keep it to two or three sentences — just enough so someone reading this cold knows what happened.

---

**What did your signals say would happen?**

Go through each signal gathered before the commitment. For each one:
- What did it predict?
- Was it right?

Be honest about the "wrong" ones. Wrong predictions are not failures — they're the most valuable
part of this retrospective. Label each signal: Correct, Wrong, or Partial.

Cover all nine signal types: scout, draft, review, flow, trace, prove, listen, program, topic.
If you didn't gather a signal in a namespace, say so — that's information too.

At the end, give yourself a score: how many signals called it correctly out of how many you gathered?

---

**What did you wish you'd asked before committing?**

Think about what you learned after the fact. Now work backward: what question, if asked earlier,
would have surfaced that learning? What signal would have answered it?

For each gap: which namespace would it have lived in, and would it have changed the decision or
just the confidence level?

Be specific. "More research" doesn't count. "A scout-competitors signal on X would have revealed Y,
which would have changed Z" does.

---

**What happened that no signal could have predicted?**

This is the Echo. Not a wrong prediction — wrong predictions are things you got wrong.
The Echo is something that happened completely outside what you were measuring.

If everything that happened was inside your prediction surface, say so and explain why.
If there's an Echo, describe it clearly and explain why the signal system didn't have a way to
catch it in advance.

One Echo only. If you have multiple candidates, pick the one that was most surprising.

---

**What would you do differently next time?**

One thing. Connect it either to a specific gap (which namespace was missing?) or to the Echo
(what type of signal would have seen this coming?). Make it actionable — a future team should
be able to read this and know what to add to their signal gathering plan.

---

**AMEND**

If a scope constraint is active:
- Namespace scope: work only within that signal type for the accuracy and gaps sections,
  but keep the Echo unrestricted.
- Time window scope: only consider signals gathered in that window; note anything outside it.
```

---

## V-03 — Axis: Lifecycle Emphasis (Explicit Phase Gates with Isolation Enforcement)

**Hypothesis:** Hard "do not proceed" gates between phases prevent the model from importing downstream reasoning backward — specifically, preventing Echo contamination of the Signal Accuracy phase and preventing Gaps from being rationalized as Echo.

---

```markdown
You are running /topic-retro for topic: $TOPIC

This retrospective has four phases. Complete each phase fully before reading the next.
Each phase has an isolation rule — do not violate it.

---

### PHASE 1 — Commitment Anchor
*Isolation: No evaluation yet. Anchor only.*

State:
1. Topic name
2. The commitment made (one sentence: what was decided)
3. The date or milestone the commitment was made
4. The date or milestone the feature shipped

Do not begin evaluating signals. Do not mention outcomes yet. Anchor only.

---

### PHASE 2 — Signal Accuracy
*Isolation: Only use information available at commitment time. Do not import post-ship knowledge.*

List every signal gathered for this topic before commitment. For each signal:

- **Signal name / artifact**
- **Namespace** (scout / draft / review / flow / trace / prove / listen / program / topic)
- **What the signal predicted** (as understood at commitment time)
- **What actually happened** (post-ship)
- **Verdict**: `Correct` | `Wrong` | `Partial`

Include all nine namespaces. If a namespace has no signal: `[namespace]: no signal gathered`.

After the list: state the accuracy ratio. Example: `7 of 9 signals correct (78%)`.

**Phase gate:** Do not proceed to Phase 3 until every namespace is accounted for.

---

### PHASE 3 — Gaps
*Isolation: Gaps are counterfactuals — signals not gathered. Do not re-evaluate signals from Phase 2 here.*

A Gap is a signal that was not gathered but would have changed the decision or its confidence level
if it had been gathered.

For each Gap:
- **What signal was missing**
- **Which namespace it would belong to**
- **What it would have revealed**
- **Decision impact**: `Would have blocked` | `Would have changed scope` | `Would have accelerated` | `Would have confirmed`

Do not include signals that were gathered in Phase 2 — those belong there, even if they were Wrong.
Do not include vague gaps. Counterfactual must be specific.

**Phase gate:** Do not proceed to Phase 4 until each gap has a concrete decision impact.

---

### PHASE 4 — Echo and Improvement
*Isolation: Echo must be genuinely outside the prediction surface. Check: if you could describe it as a wrong prediction, it belongs in Phase 2, not here.*

**Echo**

The Echo is one finding that occurred post-ship that no signal could have predicted — not because
the signals were wrong, but because the phenomenon was outside the measurement surface.

State:
- **Echo:** [what happened]
- **Why it was unpredictable:** [why no signal type covers this]
- **Systemic pattern (if identifiable):** [is this a class of thing that retrospectives routinely miss?]

If no Echo exists: state "No Echo" and explain what made the prediction surface complete.
One Echo only.

**Improvement**

One concrete recommendation. Must be tied to either:
- A specific Gap from Phase 3 (cite the namespace), or
- The Echo from this phase (cite what signal type would have approached it)

---

### AMEND
If AMEND is active with a namespace scope: restrict Phase 2 and Phase 3 to that namespace.
Restate the accuracy ratio for that namespace only. Phase 4 is never scoped.
If AMEND is active with a time window: note out-of-window signals but exclude them from the ratio.
```

---

## V-04 — Combination: Output Format (Hybrid Table+Prose) + Role Sequence (Critic-First)

**Hypothesis:** Running a skeptic role before the narrator role forces the retrospective to surface weaknesses before they can be rationalized. The hybrid format then gives the critic's findings structured capture while allowing the narrator to provide context prose only where tables cannot carry meaning.

---

```markdown
You are running /topic-retro for topic: $TOPIC

This retrospective runs two roles in sequence. Complete Role A before starting Role B.

---

## ROLE A — The Critic
*Your job: find what failed, what was missing, and what surprised the team. No advocacy.*

---

**A1. What went wrong in the signals?**

Scan all signals gathered for this topic. For each signal where the prediction was Wrong or
only Partial: list it, state what was predicted, state what happened.

| Signal | Namespace | Predicted | Actual | Verdict |
|--------|-----------|-----------|--------|---------|
| ...    | ...       | ...       | ...    | Wrong / Partial |

If there are no Wrong/Partial signals: state that and proceed. Do not invent failures.

---

**A2. What was missing?**

State the gaps — signals not gathered that would have sharpened or changed the decision.

| Missing Signal | Namespace | What It Would Have Revealed | Impact If Gathered |
|----------------|-----------|----------------------------|--------------------|
| ...            | ...       | ...                        | ...                |

---

**A3. What surprised the team?**

State the Echo candidate: one thing that happened post-ship that the signal system did not predict.
One sentence. Do not explain it yet — just name it.

---

## ROLE B — The Narrator
*Your job: complete the record, contextualize, and produce the final artifact.*

---

**B1. Commitment Anchor**

State the topic, the commitment, and the ship date. One sentence each.

---

**B2. Full Signal Accuracy**

Extend the Critic's table (A1) to include all signals, not just the failures.
Add Correct signals. Compute the accuracy ratio.

| Signal | Namespace | Predicted | Actual | Verdict |
|--------|-----------|-----------|--------|---------|
| ...    | ...       | ...       | ...    | ✓ / ✗ / ~ |

Accuracy ratio: `X of Y correct (Z%)`

If any namespace has no signal: mark it explicitly.

---

**B3. Gaps (from Critic's A2)**

Keep the Critic's gaps table. Add one sentence per row explaining the decision context —
why was this signal not gathered at the time? (Without excusing the gap.)

---

**B4. Echo (from Critic's A3)**

Take the Critic's Echo candidate. Now explain it fully:
- Why it was outside the prediction surface (not just wrong, but unmeasured)
- Whether it represents a systemic class of thing that signal systems routinely miss

If the Critic's Echo candidate is actually a wrong prediction (covered in B2): reclassify it
there and state "No Echo detected" with justification.

---

**B5. Improvement**

One recommendation. Tied to the most impactful gap (cite namespace) or to the Echo.
State it as a concrete addition to future signal-gathering plans for this topic type.

---

## AMEND
Namespace scope: restrict A1, A2, B2, B3 to that namespace. B4 (Echo) is never scoped.
Time window scope: flag out-of-window signals in the table with `[out of scope]` but include them
in the table for record completeness; exclude from ratio calculation.
```

---

## V-05 — Combination: Phrasing Register (Formal/Imperative) + Inertia Framing (Prominent)

**Hypothesis:** Foregrounding "what the team was already doing before signals" vs. "what signals changed" creates a sharper counterfactual frame. The inertia framing makes the Gaps section more honest: a gap is not just "missing data" but specifically "a signal that would have overcome the team's prior assumption."

---

```markdown
You are running /topic-retro for topic: $TOPIC

---

## 1. Commitment Record

Establish the retrospective anchor:

- **Topic:** [topic name]
- **Commitment:** [one sentence — what was decided and when]
- **Prior state (inertia):** [one sentence — what the team was doing or assumed before signals were gathered]

The prior state matters. Every signal either confirmed the inertia, disrupted it, or failed to
address it. This framing will govern the Gap analysis in Section 3.

---

## 2. Signal Accuracy — Measured Against Inertia

For each signal gathered before commitment, evaluate it against two axes:
(a) Was the prediction correct?
(b) Did it confirm or challenge the team's prior assumption (inertia)?

Format:

**[Signal Name]**
- Namespace: [namespace]
- Prediction: [what the signal said would be true]
- Actual: [what happened]
- Verdict: Correct | Wrong | Partial
- Inertia relationship: Confirmed prior assumption | Challenged prior assumption | Orthogonal to prior assumption

Cover all nine namespaces: scout, draft, review, flow, trace, prove, listen, program, topic.
For any namespace with no signal: state `[namespace]: not sampled`.

Compute and state the accuracy ratio: `X / Y signals correct (Z%)`.
Compute and state the inertia breakdown: how many signals confirmed vs. challenged the prior assumption.

---

## 3. Gaps — Signals That Would Have Overcome Inertia

A Gap is a signal that was not gathered. Gaps are evaluated against the inertia frame:
the most important gaps are those that, if gathered, would have challenged or confirmed the prior
assumption in a way that would have changed the commitment.

For each Gap:

**[Gap description]**
- Namespace: [which signal type would have carried this]
- Inertia target: [which aspect of the prior assumption this signal would have addressed]
- Predicted finding: [what the signal would likely have shown]
- Decision impact: Blocked | Changed scope | Accelerated confirmation | Unchanged (explain why listed)

Omit gaps with "Unchanged" impact unless they recur across multiple retrospectives (systemic gap).

---

## 4. Echo — Outside the Inertia Model

The Echo is a finding that occurred post-ship which was not predicted by any signal and was not
addressed by the inertia frame. It is not a wrong prediction (those belong in Section 2). It is
not a gap (those belong in Section 3). It is an event that the signal system — even if fully
executed — would not have surfaced.

State the Echo:

**Echo:** [what happened]
**Why signals couldn't reach it:** [what was structurally outside the measurement surface]
**Inertia relationship:** [did the prior assumption make this more or less likely to be invisible?]
**Systemic class:** [is this a category of thing that retrospectives routinely fail to catch?
If yes, name the category.]

If no Echo exists: state so explicitly. Explain what made the signal + inertia coverage complete.
One Echo. If multiple candidates, select the one most outside both the signal surface and the
prior assumption.

---

## 5. Improvement Directive

Issue one improvement directive. It must be tied to either:

(a) The highest-impact Gap in Section 3 — specify namespace and inertia target, or
(b) The Echo — specify what signal type or what change to inertia framing would have approached it.

Format: **Directive:** [specific, actionable change to future signal-gathering for this topic type]

Do not issue general process advice. The directive must be specific enough that a team can add it
to a checklist.

---

## AMEND Handling

If a namespace scope is active: restrict Sections 2 and 3 to that namespace. Restate accuracy
ratio for that namespace only. Section 4 (Echo) is never namespace-scoped.

If a time window is active: include all signals in the record but mark out-of-window signals as
`[outside window]`. Exclude them from the accuracy ratio. Include them in the inertia analysis
if they influenced the prior assumption.
```

---

## Variation Summary

| ID | Axis | Hypothesis |
|----|------|------------|
| V-01 | Output format — table-first | Tables force row-level completeness; accuracy ratio becomes unavoidable |
| V-02 | Phrasing register — conversational/interrogative | Questions surface honest unknowns; imperatives surface performed completeness |
| V-03 | Lifecycle emphasis — hard phase gates | Phase isolation prevents Echo contamination of Signal Accuracy and backward rationalization |
| V-04 | Format (hybrid) + Role sequence (critic-first) | Critic role surfaces weaknesses before narrator can rationalize them away |
| V-05 | Register (formal/imperative) + Inertia framing | Prior-assumption frame sharpens Gaps from "missing data" to "what would have overcome inertia" |

**C-04 compliance note across all five:** Every variation explicitly defines Echo as *outside the prediction surface entirely*, not a wrong prediction — the wrong-prediction/Echo boundary is enforced structurally (V-01, V-03, V-04) or through explicit rule text (V-02, V-05). The strictest enforcement is V-03 (phase gate + reclassification check) and V-04 (Narrator must reclassify Critic's Echo candidate if it turns out to be a wrong prediction).
