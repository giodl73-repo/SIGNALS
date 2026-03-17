Now I have full context. The v1 rubric has 10 criteria (C-01 to C-10) across three tiers. Let me generate V-01 through V-05 against that rubric, using three single-axis variations then two combinations.

---

# prove-prototype — Variate Round 1

**Rubric target**: v1 (C-01 Essential ×5, C-06–C-08 Recommended ×3, C-09–C-10 Aspirational ×2)

---

## V-01: Output Format — Table-Driven

**Variation axis**: Output format  
**Hypothesis**: Table columns act as structural gates — a blank cell signals a missing required element without instruction-reading, making skipped criteria visually conspicuous and harder to rationalize past.

---

```
You are running /prove:prototype for the topic: {{topic}}

Hypothesis: {{hypothesis}}

Build the smallest possible thing that tests this hypothesis. Define what to
measure before you build. Report what actually happened versus what was predicted.

---

## DEFINE

Complete all fields. Do not proceed to BUILD until this section is finished.

**Claim** (restate the hypothesis in one sentence — must appear before any
build description or result):

[one sentence]

| Field | Value |
|-------|-------|
| Confirmed if | [observable condition that counts as confirmation] |
| Refuted if | [observable condition that counts as refutation] |
| Metric | [what is measured — collectible, not "see if it works"] |
| Predicted value | [what you expect the metric to produce before running] |

**Scope table** (two OUT rows minimum):

| Aspect | IN / OUT | Why this boundary doesn't compromise the test |
|--------|----------|-----------------------------------------------|
| [feature / component] | IN | [reason] |
| [feature / component] | OUT | [why the test is valid without it] |
| [feature / component] | OUT | [why the test is valid without it] |

---

## BUILD

Build log — steps must be detailed enough that another developer could
reproduce this prototype without asking any follow-up questions:

| Tool | Input | Step | Output |
|------|-------|------|--------|
| [tool] | [input] | [what you did] | [what resulted] |

---

## MEASURE

Run the prototype. Record results. Do not change the metric or thresholds
declared in DEFINE.

**Results table**:

| Metric | Predicted | Actual | Delta | Verdict |
|--------|-----------|--------|-------|---------|
| [copy from DEFINE] | [copy from DEFINE] | [numeric or categorical — not "it worked"] | [actual minus predicted] | confirmed / refuted / inconclusive |

Verdict rationale: [one sentence — why this verdict given the delta?]

**Minimality** (required field): [what was excluded from scope, and why that
exclusion still produces a valid test — name the specific trade-off, not just
"it wasn't needed"]

**Raw evidence** (required field): [at least one concrete data point — a
number, a log line, a count, or an enumerated list of specific observed
behaviors; a summary statement does not satisfy this field]

---

## REPORT

**Limitations table**:

| Limitation | Impact on interpreting the verdict |
|------------|-----------------------------------|
| [specific to this run, not a generic disclaimer] | [what it changes or doesn't change about the conclusion] |

**Counter-check**: [name one result or aspect that a skeptic could point to
as evidence against the verdict; explain why the verdict holds despite it]

**Next step**: proceed / pivot / discard — [what specifically changes in the
feature plan? Not "do more research." Name the concrete action conditioned
on the observed result.]

---

Write the completed artifact to:
`simulations/prove/investigations/{{topic}}-prototype-{{date}}.md`
```

---

## V-02: Phrasing Register — Conversational

**Variation axis**: Phrasing register  
**Hypothesis**: A question-by-question format guides model output through required elements more naturally than formal section headers — each question is self-contained and difficult to skip without leaving an obvious blank.

---

```
You are running /prove:prototype for the topic: {{topic}}

Hypothesis: {{hypothesis}}

Answer each step in order. Do not skip ahead — the order prevents you from
declaring a metric after you already know the result.

---

**Step 1 — What's the claim?**

Write one sentence that states what you believe to be true. This is the
hypothesis restated in your own words. It must appear before any description
of what you built or what happened.

Claim: [one sentence]

Confirmed if: [what you would observe that counts as confirmation]
Refuted if: [what you would observe that counts as refutation]

---

**Step 2 — What are you building and what are you leaving out?**

Describe the smallest thing that directly tests the claim above.

What's in: [what the prototype does]

What's out (at least two — both with justification):
- [thing excluded] — why the test is still valid without it: [reason]
- [thing excluded] — why the test is still valid without it: [reason]

---

**Step 3 — What are you measuring and what do you predict?**

Before you build anything, name the metric. If you declare the metric after
seeing the results, the test is not a real test — it's a build with a
post-hoc story.

Metric: [a specific observable thing — not "see if it works"]
How to collect it: [tool, command, or observation method]
Predicted value: [what you expect, as specifically as possible]

---

**Step 4 — Build it.**

Write this so that another developer could reproduce the prototype from your
description alone, without asking any follow-up questions. Name every tool
used and every input provided.

What I built: [brief description]

Steps to reproduce:
1. [step with enough detail to run without asking questions]
2. [continue as needed]

Tools used: [list]
Inputs provided: [list]

---

**Step 5 — What happened?**

Run the prototype and record what you observed.

Observed: [the actual value for the metric from Step 3 — a number or named
result; not "it worked" or "it seemed to pass"]

Include at least one concrete data point — a number, a log line, a count, or
an enumerated list of specific behaviors. A summary statement does not count.

- Predicted (from Step 3): [value]
- Observed: [value]
- Delta: [difference, or "matches prediction" if identical]
- Verdict: confirmed / refuted / inconclusive — [one sentence why]

---

**Step 6 — What would a skeptic say?**

Name one result or aspect of this run that someone skeptical of your
conclusion could point to as evidence against your verdict. Then explain why
your verdict still holds.

Skeptic's reading: [what they would say]
Why the verdict stands: [your response, grounded in the evidence]

---

**Step 7 — What are the limits of this test, and what comes next?**

Name one specific limitation of this prototype that affects how much you can
generalize from the result. Not "results may vary" — something particular to
this prototype, this metric, or this environment. State what it changes about
the interpretation.

Limitation: [what it is and its impact on interpretation]

Next step: proceed / pivot / discard — [what specifically changes in the
feature plan? Not "do more research" — the action must be specific to what
you just learned.]

---

Write the completed artifact to:
`simulations/prove/investigations/{{topic}}-prototype-{{date}}.md`
```

---

## V-03: Lifecycle Emphasis — Explicit Phase Gates

**Variation axis**: Lifecycle emphasis  
**Hypothesis**: Binary checklist gates that must clear before each phase begins enforce measurement-before-building as a structural pre-condition, not a document-ordering convention that can be violated by filling sections out of sequence.

---

```
You are running /prove:prototype for the topic: {{topic}}

Hypothesis: {{hypothesis}}

Execute four phases in sequence. Each phase ends with a gate. Do not begin
the next phase until the gate for the current phase clears.

---

## PHASE 1 — DEFINE

**No building. No results. Lock everything here that MEASURE will reference.**

Claim: [restate the hypothesis in one sentence — must appear before any
build description or result]

Confirmed if: [observable condition]
Refuted if: [observable condition]

Scope:
- In: [what the prototype does]
- Out (at least two, each with justification):
  - [excluded aspect] — why the test is still valid without it: [reason]
  - [excluded aspect] — why the test is still valid without it: [reason]

Metric: [what is measured]
Collection method: [how to collect the value]
Predicted value: [what you expect before running]

### GATE 1 — must clear before PHASE 2 begins:
- [ ] Claim stated in one sentence, before any build description
- [ ] At least two scope exclusions named, each with justification
- [ ] Metric named and has a stated collection method
- [ ] Predicted value declared (not "to be determined")
- [ ] Both confirm and refute conditions present
- [ ] No build output or results present in this section

---

## PHASE 2 — BUILD

**Build only. No measurement yet.**

What was built: [description]

Build log:
| Tool | Input | Step | Output |
|------|-------|------|--------|

### GATE 2 — must clear before PHASE 3 begins:
- [ ] Build log is detailed enough to reproduce without clarifying questions —
  tools, inputs, and steps present
- [ ] No metric values appear in this section

---

## PHASE 3 — MEASURE

**Use the metric and thresholds from PHASE 1. Do not change them.**

| Metric | Predicted | Actual | Delta |
|--------|-----------|--------|-------|
| [copy from PHASE 1] | [copy from PHASE 1] | [specific value — not "it worked" or a qualitative summary] | [actual minus predicted] |

Raw evidence: [at least one concrete data point tied to the actual value —
number, log excerpt, count, or enumerated observation list; a summary
statement does not satisfy this]

### GATE 3 — must clear before PHASE 4 begins:
- [ ] Actual value is a measurement, not a qualitative summary
- [ ] Metric matches PHASE 1 declaration (no substitutions)
- [ ] Observed value recorded (not a placeholder like "TBD" or "see results")
- [ ] Raw evidence present (at least one concrete data point)

---

## PHASE 4 — REPORT

Verdict: confirmed / refuted / inconclusive

Verdict rationale: [one sentence — why this verdict given the delta?]

**Minimality**: [what was excluded from scope and why the test is still valid
without it — name the specific trade-off]

**Counter-evidence**: [name one result that a skeptic would use to argue
against the verdict; explain why the verdict holds despite it]

**Limitation**: [one specific confound or measurement limitation for this run,
with its impact on interpretation stated; not a generic disclaimer]

**Next step**: proceed / pivot / discard — [what specifically changes in the
feature plan? Not "investigate further" without naming what, where, and why
now]

---

Write the completed artifact to:
`simulations/prove/investigations/{{topic}}-prototype-{{date}}.md`
```

---

## V-04: Role Sequence + Output Format — Builder / Measurer / Analyst

**Variation axes**: Role sequence + output format  
**Hypothesis**: Separating Builder, Measurer, and Analyst into distinct mandated roles with a handoff lock makes measurement declaration a physical ordering constraint — the Measurer must declare the plan before the run output row exists in the same section — rather than a prose convention a single voice can violate silently.

---

```
You are running /prove:prototype for the topic: {{topic}}

Hypothesis: {{hypothesis}}

Three roles execute in sequence: Builder, then Measurer, then Analyst.
Each role has a mandate. Roles do not overlap. The Measurer sets the
measurement plan before running. The Analyst may not modify the Measurer's
plan after the fact.

---

## BUILDER

**Mandate**: Define the prototype and declare what will be tested. Do not
run anything. Do not record measurements.

**Claim** (restate the hypothesis in one sentence — must appear before any
build output or result):
[one sentence]

**Confirmed if**: [observable condition]
**Refuted if**: [observable condition]

**Scope table** — two OUT rows minimum; every OUT row must explain why the
exclusion still allows the hypothesis to be tested:

| Aspect | IN / OUT | Why this boundary is sufficient to test the hypothesis |
|--------|----------|--------------------------------------------------------|
| [component] | IN | [why this is the minimum needed] |
| [component] | OUT | [why test is valid without it] |
| [component] | OUT | [why test is valid without it] |

**Build log** — must be reproducible without follow-up questions:

| Tool | Input | Step | Output |
|------|-------|------|--------|

---

## MEASURER

**Mandate**: Declare the measurement plan before running. Then run. Record
the actual result. Do not interpret — interpretation belongs to the Analyst.

**Measurement plan** (declared before run — complete this table before the
run output table below):

| Metric | Collection method | Predicted value | Confirm threshold | Refute threshold |
|--------|------------------|-----------------|-------------------|------------------|
| [specific observable] | [tool or method] | [expected value] | [condition] | [condition] |

**MEASURER LOCK**: The Analyst may not change or reinterpret the metric,
thresholds, or predicted value above.

**Run output** (recorded after run):

| Metric | Actual observed value | Raw evidence |
|--------|----------------------|--------------|
| [copy from plan] | [numeric or categorical — no placeholder] | [log line, count, screenshot ref, or enumerated list] |

---

## ANALYST

**Mandate**: Interpret the measurement. Produce the verdict, minimality
assessment, counter-evidence check, limitations, and next step. Do not
re-run the prototype or modify the Measurer's plan.

**Comparison table**:

| | Predicted | Actual | Delta | Verdict |
|-|-----------|--------|-------|---------|
| Hypothesis | [from Measurer plan] | [from Measurer run] | [delta] | confirmed / refuted / inconclusive |

Verdict rationale: [one sentence — why this verdict given the delta?]

**Minimality**: [what the Builder excluded and why the test is still valid
without it]

**Counter-evidence**: [name one result or observation a skeptic would cite
against the verdict; explain why the verdict stands, grounded in the
Measurer's run output]

**Limitation**: [specific to this prototype run — state its impact on
interpreting the verdict; not a generic disclaimer]

**Next step**: proceed / pivot / discard — reference the confirm or refute
threshold from Measurer's plan; name the specific next action given what
was learned; not generic

---

Write the completed artifact to:
`simulations/prove/investigations/{{topic}}-prototype-{{date}}.md`
```

---

## V-05: Inertia Framing + Lifecycle Emphasis — Baseline + Phases

**Variation axes**: Inertia framing + lifecycle emphasis  
**Hypothesis**: Requiring a status-quo baseline prediction (B-00) declared before building forces the verdict to distinguish between "confirmed and exceeds inertia" vs. "confirmed but matches what teams already do" — the latter is weaker evidence and should not pass as an unqualified confirmation.

---

```
You are running /prove:prototype for the topic: {{topic}}

Hypothesis: {{hypothesis}}

Before you build: name the baseline. The baseline is what happens today
without this feature — the status quo, the workaround, the inertia state.
Your prototype must beat the baseline to be worth acting on. A hypothesis
confirmed by a result that merely matches what teams already do is a
different signal than one that improves on it. The comparison must be explicit.

Execute four phases in sequence. Each gate must clear before the next phase begins.

---

## PHASE 1 — DEFINE

**No building. No results. Lock everything here that MEASURE will reference.**

Claim: [restate the hypothesis in one sentence — before any build
description or result]

Confirmed if: [observable condition]
Refuted if: [observable condition]

**Baseline (B-00)**: [describe the status quo today — what users do without
this feature, or what the current system produces; name the workaround]

**Baseline predicted value**: [what you would measure if you ran the metric
against B-00 — before any build]

Metric: [what is measured]
Collection method: [how the value is collected]
Experimental predicted value: [what you expect the prototype to produce —
separate from B-00]

Scope:
- In: [what the prototype does]
- Out (at least two, each with justification):
  - [excluded aspect] — why the test is still valid without it: [reason]
  - [excluded aspect] — why the test is still valid without it: [reason]

### GATE 1 — must clear before PHASE 2 begins:
- [ ] Claim stated in one sentence, before any build description
- [ ] Baseline (B-00) described with its predicted metric value declared
- [ ] Metric declared with collection method
- [ ] Experimental prediction declared separately from B-00
- [ ] Both confirm and refute conditions present
- [ ] At least two scope exclusions with justification
- [ ] No build output or results in this section

---

## PHASE 2 — BUILD

What was built: [description]

Build log — steps must be detailed enough to reproduce without clarifying questions:

| Tool | Input | Step | Output |
|------|-------|------|--------|

### GATE 2 — must clear before PHASE 3 begins:
- [ ] Build log is detailed enough to reproduce without clarifying questions

---

## PHASE 3 — MEASURE

**Use the metric from PHASE 1. Do not change it.**

| Metric | Predicted (experimental) | Actual | Delta (vs. prediction) |
|--------|--------------------------|--------|------------------------|
| [from PHASE 1] | [from PHASE 1] | [specific value — not a qualitative summary] | [actual minus predicted] |

Raw evidence: [at least one concrete data point — number, log excerpt, count,
or enumerated observation list; a summary statement does not satisfy this]

### GATE 3 — must clear before PHASE 4 begins:
- [ ] Actual value is a measurement, not a qualitative summary
- [ ] Raw evidence present (at least one concrete data point)
- [ ] Observed value recorded (not a placeholder)

---

## PHASE 4 — REPORT

**Three-way comparison**:

| Comparison | Reference | Actual | Delta | Verdict |
|------------|-----------|--------|-------|---------|
| Hypothesis (experimental vs. prediction) | [PHASE 1 experimental] | [PHASE 3 actual] | [delta] | confirmed / refuted / inconclusive |
| Inertia check (actual vs. baseline B-00) | [PHASE 1 baseline] | [PHASE 3 actual] | [delta] | beats baseline / matches baseline / worse than baseline |
| Combined signal | — | — | — | ship / investigate / discard |

Verdict rationale: [why this verdict — account for both the experimental
comparison and the inertia check; a confirmed result that only matches the
baseline is a weaker signal than one that exceeds it]

**Minimality**: [what was excluded from scope and why the test is still
valid without it]

**Counter-evidence**: [name one result a skeptic would cite against the
verdict; explain why the verdict holds despite it]

**Limitation**: [specific to this run — state its impact on interpreting
the verdict; not a generic disclaimer]

**Next step**: proceed / pivot / discard — conditioned on both the
experimental result AND the inertia check; name the specific action; not generic

---

Write the completed artifact to:
`simulations/prove/investigations/{{topic}}-prototype-{{date}}.md`
```

---

## Variation Map

| Variation | Axis | Key mechanism | C-03 enforcement | C-04/C-07 enforcement | C-09/C-10 enforcement |
|-----------|------|---------------|------------------|-----------------------|-----------------------|
| V-01 | Output format | Table columns | DEFINE section before BUILD; Metric + Predicted value rows required | Results table: Actual + Delta + Verdict columns; Raw evidence field | Counter-check field; Build log table with all inputs |
| V-02 | Phrasing register | Question sequence | Step 3 (metric) precedes Step 4 (build) — explicit warning against retroactive declaration | Step 5: Predicted/Observed/Delta/Verdict fields; "at least one concrete data point" | Step 6: skeptic's reading + rebuttal; Step 4: reproducibility requirement |
| V-03 | Lifecycle emphasis | Phase gates | GATE 1 item: "No build output or results in this section"; GATE 3 bans qualitative summaries | GATE 3: raw evidence required; Results table with Delta column | Counter-evidence section; Build log + GATE 2 reproducibility check |
| V-04 | Role sequence + format | Role handoff lock | Measurer declares plan table before run output table exists — ordering is within same section, not cross-section | Run output: Actual + Raw evidence columns; Comparison table: Delta column | Counter-evidence in Analyst mandate; Build log with reproducibility requirement |
| V-05 | Inertia + lifecycle | B-00 + phase gates | GATE 1 item: "No build output or results"; GATE 3 bans qualitative summaries | Three-way comparison table forces delta computation twice; GATE 3: raw evidence | Counter-evidence section; Build log + GATE 2 reproducibility |

**C-03 strength ranking** (weakest → strongest): V-02 (prose warning) < V-01 (section ordering) < V-03 (gate checklist) ≈ V-05 (gate checklist, three items) < V-04 (within-section physical ordering)

**Differentiator to watch in scoring**: V-04's Measurer Lock is the only mechanism that structurally prevents the Analyst from retroactively adjusting thresholds after seeing results. All other variations rely on instruction prose.
