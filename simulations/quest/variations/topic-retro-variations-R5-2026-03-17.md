# topic-retro — Skill Body Prompt Variations (V-01 through V-05)

---

## V-01 — Axis A: Output Format (Table-Dominant)

**Variation axis**: Output format — tables enforced for Signal Accuracy and Namespace Coverage  
**Hypothesis**: Forcing tabular columns for verdict/prediction/actual eliminates prose drift, guaranteeing C-02 (explicit verdict label) and C-16 (namespace coverage table) are structurally satisfied rather than incidentally present.

---

```markdown
You are running /topic-retro.

A feature has shipped. You are conducting a post-commitment retrospective on the signals gathered
before the decision was made. Your job is to assess signal accuracy, surface gaps, and name the
one unexpected finding.

---

## Step 1 — Establish Context

State:
- **Topic**: [name]
- **Commitment**: [what was decided, e.g., "build / kill / defer / pivot"]
- **Decision date**: [date]
- **Retrospective window**: [how long after commitment this retro is being run]

---

## Step 2 — Signal Accuracy Table

List every signal gathered before commitment. For each, populate all columns. Do not skip
the Verdict column — it must be one of: CORRECT / WRONG / PARTIAL.

| Signal | Namespace | Prediction | Actual Outcome | Verdict |
|--------|-----------|------------|----------------|---------|
| ...    | ...       | ...        | ...            | CORRECT / WRONG / PARTIAL |

After the table, state the accuracy ratio:

> **Accuracy**: N correct / M total = X%

---

## Step 3 — Namespace Coverage Table

Walk all 9 namespaces. Mark each as GATHERED or ABSENT. If ABSENT, note whether it would
have mattered.

| Namespace | Status | Signals Gathered | Would Absence Have Changed Decision? |
|-----------|--------|------------------|--------------------------------------|
| scout     | GATHERED / ABSENT | [names or —] | YES / NO / UNKNOWN |
| draft     | ... | ... | ... |
| review    | ... | ... | ... |
| flow      | ... | ... | ... |
| trace     | ... | ... | ... |
| prove     | ... | ... | ... |
| listen    | ... | ... | ... |
| program   | ... | ... | ... |
| topic     | ... | ... | ... |

---

## Step 4 — Gaps

Name every signal that was ABSENT and would have changed or sharpened the decision.
For each gap, state the decision impact explicitly.

Format each gap as:
> **Gap**: [signal that was missing]  
> **Decision impact**: [how its absence affected the commitment]

---

## Step 5 — Echo

State exactly one Echo: the single thing you learned after shipping that you did not predict
and could not have predicted from the signals available. The Echo is not a wrong prediction —
it is genuinely new information.

> **Echo**: [one unexpected finding]  
> **Why unpredicted**: [what made this invisible before commitment]

---

## Step 6 — Improvement Recommendation

State one practice change. Use this template exactly:

> **Recommendation**: Addresses [Gap: name / Echo] by [specific practice change].

One recommendation only. Tie it to the gap or Echo with the highest future leverage.

---

## Output Format

Deliver sections in this order:
1. Context block
2. Signal Accuracy Table + accuracy ratio
3. Namespace Coverage Table
4. Gaps (bulleted, gap + impact per item)
5. Echo block
6. Recommendation (one sentence, template above)

No prose summaries between sections. Tables where specified.
```

---

## V-02 — Axis B: Lifecycle Emphasis (Namespace-Walk-First)

**Variation axis**: Lifecycle emphasis — namespace inventory runs before signal analysis, not after  
**Hypothesis**: Starting with the 9-namespace walk as the primary organizing frame surfaces what was absent before evaluating what was correct. This makes gaps structurally primary rather than afterthoughts, improving C-03 (actionable gaps), C-06 (coverage summary), and C-16 (explicit namespace table).

---

```markdown
You are running /topic-retro.

A feature has shipped. Before analyzing prediction accuracy, you will first inventory what
signals existed across all 9 namespaces. Coverage is the frame. Accuracy is the detail.

---

## Phase 1 — Commitment Context

State:
- **Topic**: [name]
- **Commitment**: [decision made]
- **Decision date**: [date]

---

## Phase 2 — Namespace Inventory (Run This First)

For each of the 9 namespaces, answer: what signals were gathered, and were any absent?
Do not skip namespaces. Mark absent ones explicitly.

**scout** — market, feasibility, competition signals  
Signals: [list or "none gathered"]  
Absent signals that would have mattered: [list or "none identified"]

**draft** — brainstorm, proposal, spec signals  
Signals: [list or "none gathered"]  
Absent: [list or "none identified"]

**review** — design, code, user, customer review signals  
Signals: [list or "none gathered"]  
Absent: [list or "none identified"]

**flow** — trigger, lifecycle, throttle, resilience, dataflow signals  
Signals: [list or "none gathered"]  
Absent: [list or "none identified"]

**trace** — state, permissions, contract, component signals  
Signals: [list or "none gathered"]  
Absent: [list or "none identified"]

**prove** — hypothesis, interview, prototype, synthesis signals  
Signals: [list or "none gathered"]  
Absent: [list or "none identified"]

**listen** — adoption, support, feedback signals  
Signals: [list or "none gathered"]  
Absent: [list or "none identified"]

**program** — program plan, execution signals  
Signals: [list or "none gathered"]  
Absent: [list or "none identified"]

**topic** — readiness, story, plan signals  
Signals: [list or "none gathered"]  
Absent: [list or "none identified"]

**Coverage summary**: N namespaces with at least one signal / 9 total

---

## Phase 3 — Signal Accuracy

For every signal identified in Phase 2, state what it predicted and whether it was correct.

Each entry:
- **Signal**: [name]
- **Namespace**: [namespace]
- **Predicted**: [what the signal said would be true]
- **Actual**: [what turned out to be true after shipping]
- **Verdict**: CORRECT | WRONG | PARTIAL

After all entries:
> **Accuracy ratio**: N correct / M total = X%

---

## Phase 4 — Gaps

From the absent signals identified in Phase 2, select those that would have changed or
sharpened the commitment. For each:

> **Gap**: [namespace] / [signal type]  
> **Decision impact**: [how its absence affected the commitment]

If no absent signal would have changed anything, state that explicitly.

---

## Phase 5 — Echo

One finding only. The Echo is something you learned after shipping that was invisible before
commitment — not a wrong prediction, but genuinely new information that the signals available
could not have surfaced.

> **Echo**: [one unexpected finding]  
> **Systemic pattern**: [if this connects to a recurring blind spot, name it]

---

## Phase 6 — Recommendation

One practice change, tied to the gap or Echo with highest leverage.

> **Recommendation**: Addresses [Gap: namespace/type | Echo] by [specific practice change].

---

## AMEND options

- `/topic-retro focus:scout` — run Phase 2–4 for scout namespace only
- `/topic-retro window:30d` — restrict Phase 3 to signals gathered within 30 days of commit
```

---

## V-03 — Axis C: Phrasing Register (Interrogative/Conversational)

**Variation axis**: Phrasing register — question-driven structure instead of imperative commands  
**Hypothesis**: Interrogative framing anchors the model to actual evidence by forcing it to answer specific factual questions rather than generating plausible-sounding retrospective prose. Reduces hallucinated signals, improves C-01 and C-04 fidelity.

---

```markdown
You are running /topic-retro.

A feature has shipped. Answer the following questions about the signals you gathered before
committing. Be precise. If you don't know, say so — gaps in your answers are data.

---

### What was the topic and what did you decide?

- What is the topic name?
- What commitment was made? (build / kill / defer / pivot — be specific)
- When was the commitment made?

---

### What signals did you gather, and were they right?

For each signal gathered before the commitment, answer:

1. What did this signal predict?
2. What actually happened after shipping?
3. Was the signal CORRECT, WRONG, or PARTIAL?

List every signal. Do not summarize or skip.

After listing all signals, answer: what fraction were correct? (N correct / M total = X%)

---

### Which namespaces did you cover, and which did you skip?

For each of the 9 namespaces — scout, draft, review, flow, trace, prove, listen, program,
topic — answer: did you gather at least one signal here before committing?

For each namespace you skipped: would a signal there have changed your decision? Why?

---

### What was missing that would have mattered?

What signals were absent that, if present, would have changed or sharpened the commitment?

For each gap, answer: how did its absence actually affect the decision?

---

### What surprised you?

What is the one thing you learned after shipping that you genuinely could not have predicted
from the signals you had? This is not a wrong prediction — it is something that was invisible
before commitment.

Name exactly one thing. Explain why it was unpredictable.

---

### What would you do differently?

Given the gaps and the surprise, what is the single most valuable practice change for the
next topic?

Answer using this format:
> This addresses [the gap / the Echo] by [doing what, specifically].

---

### AMEND options

Want to focus? Specify:
- A single signal type: "retro focused on scout signals only"
- A time window: "retro for signals gathered in the 2 weeks before commit"
- A single question: "just the Echo" or "just the gaps"
```

---

## V-04 — Axes A + B Combined: Table Format × Namespace-Walk-First

**Variation axes**: Output format (table-dominant) + Lifecycle emphasis (namespace-walk-first)  
**Hypothesis**: The namespace walk generates the row set for the Signal Accuracy table, creating a single pass that satisfies C-06, C-16 (namespace table), C-02 (verdict column), and C-15 (ratio) without requiring the model to revisit the signal list. Structural dependency between phases closes gaps mechanically.

---

```markdown
You are running /topic-retro.

A feature has shipped. This retrospective runs in three table passes. Each table feeds the next.
Do not skip tables or merge them.

---

## Block 1 — Context

| Field | Value |
|-------|-------|
| Topic | [name] |
| Commitment | [decision: build / kill / defer / pivot] |
| Decision date | [date] |
| Retrospective window | [days/weeks since commit] |

---

## Block 2 — Namespace Coverage Table (Run First)

Enumerate every signal by namespace. This table is the input to Block 3.

| Namespace | Signal Name | Gathered? | If Absent: Decision Impact |
|-----------|-------------|-----------|---------------------------|
| scout | [signal or —] | YES / NO | [impact or n/a] |
| draft | [signal or —] | YES / NO | [impact or n/a] |
| review | [signal or —] | YES / NO | [impact or n/a] |
| flow | [signal or —] | YES / NO | [impact or n/a] |
| trace | [signal or —] | YES / NO | [impact or n/a] |
| prove | [signal or —] | YES / NO | [impact or n/a] |
| listen | [signal or —] | YES / NO | [impact or n/a] |
| program | [signal or —] | YES / NO | [impact or n/a] |
| topic | [signal or —] | YES / NO | [impact or n/a] |

Add rows for namespaces with multiple signals. One row per signal, not one row per namespace.

**Coverage**: N namespaces with signals / 9 total

---

## Block 3 — Signal Accuracy Table (Gathered signals only)

Take every YES row from Block 2. For each, fill in prediction vs. actual and assign a verdict.
Verdict must be one of: CORRECT / WRONG / PARTIAL. No prose substitutes for the verdict column.

| Signal | Namespace | Predicted | Actual | Verdict |
|--------|-----------|-----------|--------|---------|
| ...    | ...       | ...       | ...    | CORRECT / WRONG / PARTIAL |

**Accuracy ratio**: N correct / M total = X%

(Count PARTIAL as 0.5 if you choose to include them in the numerator — state your convention.)

---

## Block 4 — Gaps Table (NO rows from Block 2 where Decision Impact is non-trivial)

Take every NO row from Block 2 where "Decision Impact" is not "n/a". One row per gap.

| Namespace | Missing Signal | Decision Impact |
|-----------|----------------|-----------------|
| ...       | ...            | [how absence affected commitment] |

If the Block 2 NO rows all have trivial impact, state: **No material gaps identified.**

---

## Block 5 — Echo

Prose only. Exactly one finding. Not a wrong prediction — something invisible before commitment.

> **Echo**: [one unexpected finding]  
> **Why unpredicted**: [what made it invisible to the signals available]  
> **Systemic pattern**: [if this connects to a recurring blind spot, name it; otherwise omit]

---

## Block 6 — Recommendation

One sentence. Mandatory template:

> **Recommendation**: Addresses [Gap: namespace/signal | Echo] by [specific practice change].

---

## AMEND options

- `focus:[namespace]` — restrict Block 2 to one namespace row set, re-derive Blocks 3–4
- `window:[Nd]` — restrict Block 3 to signals gathered within N days of commit
- `signal-type:[type]` — filter Block 2/3 to a specific signal category
```

---

## V-05 — Axes B + C Combined: Namespace-Walk-First × Interrogative Register

**Variation axes**: Lifecycle emphasis (namespace inventory as primary frame) + Phrasing register (question-driven)  
**Hypothesis**: Interrogative framing on the namespace walk forces the model to answer whether each namespace produced evidence before making accuracy claims. The Echo question sequence — "what was invisible, and why" — produces richer systemic pattern identification than imperative instructions, improving C-04, C-09, and C-17 depth.

---

```markdown
You are running /topic-retro.

A feature has shipped. You will answer a sequence of questions. Start from coverage, not from
accuracy — what you gathered shapes what you can evaluate. Work through the questions in order.

---

### Q1 — What was the topic and what did you commit to?

Name the topic. State the commitment as a single decision (build / kill / defer / pivot) and
when it was made.

---

### Q2 — What did each namespace contribute?

For each of the 9 namespaces below, answer: did it produce a signal before commitment?
If yes, name the signal. If no, say why it was skipped or absent.

Work through all nine. Do not skip.

- **scout** — what did competitive, market, or feasibility signals tell you?
- **draft** — what did brainstorm, proposal, or spec signals tell you?
- **review** — what did design, code, or user review signals tell you?
- **flow** — what did trigger, lifecycle, throttle, or resilience signals tell you?
- **trace** — what did state, permissions, or contract signals tell you?
- **prove** — what did hypothesis, interview, or prototype signals tell you?
- **listen** — what did adoption, support, or feedback signals tell you?
- **program** — what did program-plan signals tell you?
- **topic** — what did topic readiness or story signals tell you?

After answering all nine: how many namespaces contributed at least one signal?

---

### Q3 — Which signals were right, which were wrong?

For every signal named in Q2, answer:
- What exactly did it predict?
- What actually happened after shipping?
- Was it CORRECT, WRONG, or PARTIAL?

After all signals: what fraction were correct? State as N/M = X%.

---

### Q4 — Which absences hurt you?

Look back at the namespaces in Q2 that produced no signal. For each:
- Would a signal there have changed or sharpened your commitment?
- If yes: how?

If a namespace's absence made no difference, say so.

---

### Q5 — What was the one thing you couldn't have known?

What is the single finding that emerged after shipping that was genuinely invisible before
commitment — not a prediction that turned out wrong, but something the available signals
had no way to surface?

Answer with: what it was, why it was unpredicted, and whether it connects to a pattern
you've seen across other topics.

---

### Q6 — What should change?

Given your answers to Q4 (absences that hurt) and Q5 (the unexpected finding), what is the
highest-leverage practice change for your next topic?

State it as: "This addresses [the gap in Q4 / the Echo in Q5] by [what, specifically]."

---

### AMEND options

Running a focused retro? Specify the scope before the questions:

- **Focus on one signal type**: "retro on scout signals only — answer Q2–Q3 for scout only"
- **Narrow the time window**: "signals gathered in the 14 days before commit only"
- **Skip to Echo**: "I only need Q5 and Q6"
```

---

## Variation Summary

| Variation | Primary Axes | Core Hypothesis |
|-----------|-------------|-----------------|
| V-01 | Output Format (table-dominant) | Tabular column enforcement eliminates verdict prose drift; C-02 + C-16 satisfied structurally |
| V-02 | Lifecycle Emphasis (namespace-walk-first) | Inventory-before-analysis makes gaps structurally primary, not afterthoughts |
| V-03 | Phrasing Register (interrogative) | Question-driven framing anchors model to evidence, reduces hallucinated retrospective prose |
| V-04 | A + B (table × namespace-walk) | Namespace walk generates table row set — single pass closes C-06, C-16, C-02, C-15 mechanically |
| V-05 | B + C (namespace-walk × interrogative) | Interrogative namespace walk produces richer Echo/systemic pattern content without losing structural coverage |
