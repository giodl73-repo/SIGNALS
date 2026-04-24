# Quest Variate — topic-retro — Round 3

**Skill**: `topic-retro`
**Rubric**: v3
**Goal**: 5 complete prompt body variations targeting C-14 through C-17 aspirational criteria

---

## Variation Axes Selected

| Axis | Hypothesis |
|------|-----------|
| **Output format** | Explicit table structure forces verdict-label and ratio compliance (C-14, C-15) |
| **Lifecycle emphasis** | Giving Echo its own expanded phase prevents it from being a restatement of wrong predictions (C-04, C-09) |
| **Phrasing register** | Imperative second-person voice reduces ambiguity in verdict labeling and recommendation framing |

V-04 and V-05 combine axes.

---

## V-01

**Axis**: Output format — table-first with explicit verdict column and accuracy ratio row
**Hypothesis**: Forcing signal accuracy into a table with a labeled `VERDICT` column eliminates prose verdicts (C-14) and a `Ratio` header row enforces N/M = X% format (C-15).

```
You are running /topic-retro for: $TOPIC

A commitment has been made. Review the signals gathered before that commitment and assess
their predictive value now that outcomes are known.

---

## Step 1 — Commitment Context

State:
- Topic name
- Commitment made (what was decided and when)
- Signal window (what date range the signals cover)

---

## Step 2 — Signal Accuracy Table

Build this table. One row per signal artifact gathered before commitment.

| Signal | Namespace | Prediction | Actual Outcome | VERDICT |
|--------|-----------|------------|----------------|---------|
| ...    | ...       | ...        | ...            | CORRECT / WRONG / PARTIAL |

After the table, add a single accuracy line:

> **Accuracy: N/M = X%** (CORRECT + PARTIAL×0.5 / total signals)

Rules:
- VERDICT must be one of: CORRECT, WRONG, PARTIAL. No prose substitutes.
- Every row requires all five columns populated.
- Predictions must be stated as they were before commitment, not retrofitted.

---

## Step 3 — Namespace Coverage Table

For each of the 9 namespaces, record whether a signal was gathered.

| Namespace | Signal Gathered? | Signal Name (if yes) |
|-----------|-----------------|----------------------|
| scout     | YES / NO        | ...                  |
| draft     | YES / NO        | ...                  |
| review    | YES / NO        | ...                  |
| flow      | YES / NO        | ...                  |
| trace     | YES / NO        | ...                  |
| prove     | YES / NO        | ...                  |
| listen    | YES / NO        | ...                  |
| program   | YES / NO        | ...                  |
| topic     | YES / NO        | ...                  |

Note the coverage ratio: **X of 9 namespaces covered**.

---

## Step 4 — Gaps

List signals that were absent and would have changed the commitment decision.

For each gap:
- Name the missing signal (namespace + type)
- State the decision impact: "Without this signal, we committed without knowing [X]"

At least one gap required. If no gaps exist, state that explicitly with reasoning.

---

## Step 5 — Echo

State exactly one unexpected finding — something not predicted by any signal and not
a restatement of a wrong prediction.

Format:
> **Echo**: [Finding]. This was unexpected because [no signal predicted it / all signals
> pointed away from it].

One Echo only. If you find multiple candidates, name the most systemic one and move
the others to a "Near-Echoes" list below it.

---

## Step 6 — Improvement Recommendation

Write one recommendation. Use this template exactly:

> Addresses [Gap: gap-name / Echo] by [specific practice change — what to do differently
> next time, naming the namespace or signal type affected].

One recommendation required. Additional recommendations may follow the same template.

---

## Output Format

Deliver sections in order: Commitment Context → Signal Accuracy Table → Namespace Coverage
Table → Gaps → Echo → Improvement Recommendation.

No section may be omitted. Tables must use markdown pipe format.
```

---

## V-02

**Axis**: Phrasing register — conversational imperative, first-person "you gathered" voice
**Hypothesis**: Conversational register with direct "you" address and active verbs reduces hedging language that produces prose verdicts instead of labels.

```
You are running /topic-retro for: $TOPIC

You made a commitment. Now look back at the signals you gathered and find out which ones
told you the truth.

---

**First: set the scene.**

In two to three sentences, say what the topic was, what commitment you made, and when you
made it. This anchors everything that follows.

---

**Second: go through your signals one by one.**

For each signal you gathered before the commitment, answer three questions:
1. What did this signal predict?
2. What actually happened?
3. Was it CORRECT, WRONG, or PARTIAL?

Use those exact labels — CORRECT, WRONG, PARTIAL — nothing else. Not "mostly right." Not
"directionally accurate." Pick one.

Then count: how many signals did you gather? How many were CORRECT or PARTIAL?
Write it as: **X of Y signals correct = Z%**

---

**Third: check your namespace coverage.**

Go through all 9 namespaces: scout, draft, review, flow, trace, prove, listen, program, topic.

For each one, answer: did you gather a signal here before committing?

Build a table:
- Column 1: Namespace name
- Column 2: YES or NO
- Column 3: Signal name if YES, blank if NO

At the bottom of the table, write how many of the 9 you covered.

---

**Fourth: name your gaps.**

Which signals were missing that would have made you decide differently — or decide with
more confidence?

For each gap, name it and say what it would have told you that you didn't know. A gap
without a consequence isn't a real gap — it's just something you didn't do.

---

**Fifth: find the Echo.**

What happened after commitment that you genuinely didn't see coming — not a wrong
prediction, but something that no signal even gestured toward?

Write it as one clear sentence starting: "**Echo**:" — then explain why nothing predicted it.

One Echo only. If you want to list more, put them in a "Near-Echoes" note but don't elevate
them to Echo status.

---

**Sixth: make one recommendation.**

Say what you'd do differently next time. Be specific: which namespace, which signal type,
which practice. Use this sentence structure:

> Addresses [name the gap or Echo] by [name the change — what you'd add, drop, or do earlier].

---

Keep this order. Don't skip sections. Tables in pipe format.
```

---

## V-03

**Axis**: Lifecycle emphasis — expanded Echo and Gap phases, compressed accuracy header
**Hypothesis**: When Echo gets its own interrogation phase (candidates → elimination → selection), the output produces a genuinely unexpected finding rather than a restatement of prediction failures.

```
You are running /topic-retro for: $TOPIC

Post-commitment retrospective. The commitment has been made. You are now reviewing the
signal record to determine what the signals got right, what they missed, and what surprised
everyone.

---

## Phase 1 — Context (brief)

State the topic, the commitment, and the signal window. Three sentences maximum.

---

## Phase 2 — Signal Accuracy (structured)

For each signal gathered before commitment:

**Signal name** | Namespace: [namespace]
- Prediction: [what the signal said would happen]
- Actual: [what happened]
- VERDICT: CORRECT / WRONG / PARTIAL

After all signals:
> **Accuracy ratio: N/M = X%**
> (Count: CORRECT = A, WRONG = B, PARTIAL = C; score = (A + C×0.5) / M)

---

## Phase 3 — Namespace Coverage

Explicit table across all 9 namespaces. Each row: namespace | gathered (YES/NO) | signal name.

Coverage line: X of 9 namespaces represented.

Namespaces: scout, draft, review, flow, trace, prove, listen, program, topic.

---

## Phase 4 — Gaps (expanded)

A gap is a signal that was absent and whose absence created decision risk.

For each gap identified:

**Gap G-N: [signal type], [namespace]**
- Missing: [what signal would have been gathered]
- Decision impact: [what the team committed to without knowing]
- Severity: HIGH (would have changed decision) / MEDIUM (would have changed confidence) / LOW (nice to have)

Identify at least one HIGH or MEDIUM gap. If none exist, justify explicitly.

---

## Phase 5 — Echo (expanded)

The Echo is the one thing that wasn't predicted — not a wrong prediction, but something
genuinely outside the prediction space.

**Step 5a — List candidates**
Name up to three things that happened post-commitment that no signal predicted. One sentence each.

**Step 5b — Test each candidate**
For each: check whether any signal, even a wrong one, gestured toward this. If a signal
named it and got it wrong, it is a wrong prediction, not an Echo.

**Step 5c — Select the Echo**
Promote the candidate that passed Step 5b and was most systemic (affected multiple decisions
or would affect future topics). Label it:

> **Echo**: [finding]. Unexpected because: [no signal predicted it; signals pointed
> elsewhere / the namespace that would have caught this was absent].

If zero candidates pass Step 5b, state that the signals fully covered the outcome space —
no Echo this cycle.

---

## Phase 6 — Improvement Recommendation

One primary recommendation, using the required template:

> Addresses [Gap G-N: gap-name / Echo] by [specific practice change, naming the
> namespace or signal type and when in the topic lifecycle to add it].

Secondary recommendations may follow the same template, labeled R-2, R-3, etc.

---

Deliver phases in order. Tables in pipe format. Phase 5 must show the elimination steps,
not just the selected Echo.
```

---

## V-04

**Axis**: Role sequence — coverage verifier runs first, accuracy analyst runs second
**Hypothesis**: Running namespace coverage before accuracy analysis forces the retrospective to acknowledge gaps structurally before assessing prediction quality, preventing the common failure mode where absent signals are invisible in the accuracy count.

```
You are running /topic-retro for: $TOPIC

Retrospective on a completed topic's signal record. Two roles execute in sequence.

---

## Role 1: Coverage Verifier

Your job is to establish what signals exist in the record before any accuracy assessment begins.

**Step 1.1 — Commitment Context**
State the topic, commitment made, and signal window.

**Step 1.2 — Signal Inventory**
List every signal artifact gathered before the commitment date:
- Signal name
- Namespace
- Date gathered

**Step 1.3 — Namespace Coverage Table**
Map the inventory against all 9 namespaces.

| Namespace | Signal Present | Signal Name |
|-----------|---------------|-------------|
| scout     | YES / NO      | ...         |
| draft     | YES / NO      | ...         |
| review    | YES / NO      | ...         |
| flow      | YES / NO      | ...         |
| trace     | YES / NO      | ...         |
| prove     | YES / NO      | ...         |
| listen    | YES / NO      | ...         |
| program   | YES / NO      | ...         |
| topic     | YES / NO      | ...         |

Coverage: **X of 9 namespaces**.
Absent namespaces (if any): list them. These are gap candidates.

---

## Role 2: Accuracy Analyst

You receive the inventory from Role 1. Your job is to assess prediction quality and surface the unexpected.

**Step 2.1 — Signal Accuracy**

For each signal in the inventory, assess:

| Signal | Prediction | Actual Outcome | VERDICT |
|--------|------------|----------------|---------|
| ...    | ...        | ...            | CORRECT / WRONG / PARTIAL |

Accuracy summary: **N/M = X%**
(CORRECT = A, WRONG = B, PARTIAL = C; score = (A + C×0.5) / M)

VERDICT must be one of the three labels. No prose substitutes accepted.

**Step 2.2 — Gaps**

Gaps come from two sources:
1. Absent namespaces identified by Role 1 that would have changed the decision
2. Present signals that were WRONG and whose failure exposed a missing signal type

For each gap:
- Name it: [namespace / signal type]
- Decision impact: "Committing without this signal meant we didn't know [X]"

**Step 2.3 — Echo**

Name the one finding that appeared post-commitment that no signal in the inventory predicted.
Distinguish from WRONG predictions — an Echo is outside the prediction space entirely.

> **Echo**: [finding]. No signal in the inventory addressed this because [reason — absent
> namespace / topic domain not covered / signal gathered too early].

One Echo only.

**Step 2.4 — Improvement Recommendation**

> Addresses [Gap: name / Echo] by [practice change — namespace, signal type, timing
> in topic lifecycle].

---

Deliver Role 1 output, then Role 2 output, in full. Do not merge the roles. Tables in pipe format.
```

---

## V-05

**Axis**: Combination — V-01 table format + V-03 Echo interrogation + V-04 role sequence + explicit recommendation template enforcement
**Hypothesis**: Combining structural table enforcement (C-14, C-15, C-16) with explicit Echo candidate elimination (C-04, C-09) and the recommendation template (C-17) in a sequenced role structure maximizes aspirational criteria hit rate by making each criterion structurally unavoidable.

```
You are running /topic-retro for: $TOPIC

Post-commitment retrospective. Two roles execute in sequence. Both roles use explicit table
formats throughout. No prose substitutes for structured fields.

---

## Role 1: Coverage Verifier

**Output 1A — Commitment Context**

| Field | Value |
|-------|-------|
| Topic | ... |
| Commitment | ... |
| Commitment date | ... |
| Signal window | ... |

**Output 1B — Namespace Coverage Table**

| Namespace | Signal Gathered | Signal Name | Date |
|-----------|----------------|-------------|------|
| scout     | YES / NO        | ...         | ...  |
| draft     | YES / NO        | ...         | ...  |
| review    | YES / NO        | ...         | ...  |
| flow      | YES / NO        | ...         | ...  |
| trace     | YES / NO        | ...         | ...  |
| prove     | YES / NO        | ...         | ...  |
| listen    | YES / NO        | ...         | ...  |
| program   | YES / NO        | ...         | ...  |
| topic     | YES / NO        | ...         | ...  |

Coverage summary line: **X of 9 namespaces covered.**
Absent namespaces: [list or "none"].

---

## Role 2: Accuracy Analyst

Receives Role 1 output. Does not re-derive coverage — use Role 1's table as the signal inventory.

**Output 2A — Signal Accuracy Table**

| Signal | Namespace | Prediction (pre-commitment) | Actual Outcome | VERDICT |
|--------|-----------|-----------------------------|----------------|---------|
| ...    | ...       | ...                         | ...            | CORRECT / WRONG / PARTIAL |

Rules:
- VERDICT column: CORRECT, WRONG, or PARTIAL only. No prose.
- Prediction column: state as it was before commitment. No retrofitting.
- Every signal from Role 1's YES rows must appear here.

Accuracy line immediately below the table:
> **Accuracy: N/M = X%** (CORRECT = A, WRONG = B, PARTIAL = C; scored as (A + C×0.5) / M)

**Output 2B — Gaps**

Gaps come from: (a) absent namespaces in Role 1 that would have changed the decision,
(b) WRONG signals that point to a missing signal type.

For each gap, provide:

| Gap ID | Missing Signal | Namespace | Decision Impact |
|--------|---------------|-----------|-----------------|
| G-1    | ...           | ...       | Without this, we committed not knowing [X] |

Minimum one gap. If none: justify in one sentence.

**Output 2C — Echo Interrogation**

Step 1 — Candidates: List up to three post-commitment findings not predicted by any signal.
Step 2 — Elimination: For each candidate, check: did any signal, even a wrong one, gesture
toward this? If yes, it is a wrong prediction, not an Echo. Mark ELIMINATED.
Step 3 — Selection: Promote the surviving candidate most likely to recur across future topics.

> **Echo**: [finding]. Unexpected because [no signal addressed this domain / the namespace
> that would have caught this was absent per Role 1 / signals pointed in the opposite direction].

If all candidates are eliminated in Step 2: state "No Echo — all unexpected findings were
within the prediction space of signals gathered."

**Output 2D — Improvement Recommendations**

Use this template for each recommendation:

> **R-N**: Addresses [Gap G-N: signal-name / Echo] by [specific practice change —
> name the namespace, signal type, and when in the topic lifecycle to gather it].

Minimum one recommendation. Maximum three.

---

Deliver Role 1 in full, then Role 2 in full. Tables in pipe format throughout.
All VERDICT values must be from the allowed set. Accuracy ratio required. Echo interrogation
must show all three steps.
```

---

## Variation Summary

| Variation | Axis | C-14 Strategy | C-15 Strategy | C-16 Strategy | C-17 Strategy |
|-----------|------|--------------|--------------|--------------|--------------|
| V-01 | Output format | Explicit VERDICT column in table | Ratio row after table | Full 9-row namespace table | Exact template quoted |
| V-02 | Register (imperative) | "Use those exact labels" injunction | "Write it as X of Y = Z%" | Table with YES/NO column | "Use this sentence structure" |
| V-03 | Lifecycle emphasis | VERDICT after each signal block | Accuracy ratio with formula | Coverage line + table | R-N labeled template |
| V-04 | Role sequence | VERDICT column, three allowed values | Accuracy summary after table | Role 1 owns namespace table | Template in Role 2 |
| V-05 | Combination | VERDICT column + "no prose" rule | Formula shown explicitly | Role 1 owns 9-row table | Template enforced with R-N labels |
