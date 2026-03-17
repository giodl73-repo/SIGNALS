# prove-prototype Variations — Round 6 (V-01 through V-05)

---

## V-01 — Single Axis: Role Sequence
**Axis**: DEFINER → BUILDER → EVALUATOR with explicit per-role prohibitions (targets C-23)
**Hypothesis**: Role-labeled prompts with explicit prohibitions catch in-order, out-of-role contamination that phase-gate ordering alone cannot detect.

---

```markdown
You are running a prove-prototype experiment in three sequential roles.
Execute each role completely before advancing. Do not blend roles.

---

## ROLE 1: DEFINER
**Permitted**: Restate the hypothesis. Define prototype scope. Specify what to measure.
Establish success and failure conditions.
**Prohibited**: DEFINER must not describe construction steps, report outcomes, interpret
results, or reference what actually happened. Any build description or result here is
a contamination error.

**Execute before Role 2 gate is present in your output.**

### Hypothesis (restate verbatim or in your own words — must be first element)
[Restate the hypothesis being tested.]

### Prototype Scope
State what the prototype does and does not do. Name at least two explicit exclusions.
For each exclusion, state why the test remains valid without it.

| Exclusion | Why the test remains valid without it |
|-----------|---------------------------------------|
| [exclusion 1] | [validity reasoning] |
| [exclusion 2] | [validity reasoning] |

### Measurement Definition
*This section must appear before any construction or results.*

**What to measure**: [the observable quantity or outcome]
**Success condition**: [what result confirms the hypothesis]
**Failure condition**: [what result refutes the hypothesis]
**Inconclusive condition**: [what result leaves the hypothesis unresolved]

**Minimality justification**: Name one thing left out and why that omission still allows
the hypothesis to be tested.

DEFINER GATE COMPLETE — hypothesis: [one sentence], scope boundary: [named exclusions],
success threshold: [stated condition]

*Execute Role 2 only after DEFINER GATE appears in your output.*

---

## ROLE 2: BUILDER
**Permitted**: Describe what was built. Record the replication path. State one raw evidence
data point. Record what was predicted to happen before reporting what happened.
**Prohibited**: BUILDER must not interpret results, render a verdict on the hypothesis,
address counter-evidence, or assess whether the hypothesis is confirmed or refuted.
Interpretation here is a contamination error.

**Execute before Role 3 gate is present in your output.**

### What Was Built
[Describe the prototype — what it is, what it does, how it was constructed.]

### Replication Path
List every tool, input, command, or step needed to reproduce. No implicit steps.

1. [step]
2. [step]
3. [step]

### Prediction (record before reporting results)
*State what you predicted before describing what happened.*

**Predicted outcome**: [what you expected to observe]

### Raw Result
**Observed outcome**: [what actually happened — at least one concrete data point]

**Delta**: [match or mismatch between prediction and observation]
**Why the delta is what it is**: [explanation co-located here, not in a separate section]

BUILDER GATE COMPLETE — predicted: [value], observed: [value], delta: [match/mismatch + reason]

*Execute Role 3 only after BUILDER GATE appears in your output.*

---

## ROLE 3: EVALUATOR
**Permitted**: Render the hypothesis verdict. Address counter-evidence. State limitations
and next steps. Assess failure modes if applicable.
**Prohibited**: EVALUATOR must not restate the build description, re-list construction
steps, or re-describe what the prototype does. Build description here is a contamination
error.

**Execute after BUILDER GATE is present in your output.**

### Hypothesis Verdict
State whether the hypothesis is confirmed, refuted, or inconclusive.
Ground the verdict in the measurement result — do not assert it without evidence.

**Verdict**: [confirmed / refuted / inconclusive]
**Reasoning**: [why this verdict follows from the measured delta]

### Counter-Evidence
This section must close with one of exactly two dispositions:
- (a) A named counter-interpretation with a grounded rebuttal, or
- (b) An explicit statement that no plausible counter-interpretation exists, with a reason.

[Address or explicitly close the counter-evidence question here.]

**Counter-evidence disposition**: [(a) rebuttal: [reasoning] | (b) none: [reason]]

### Limitations and Next Step
**One limitation**: [what this prototype cannot tell us]
**One specific next step**: [what to build or test next, and why]

*Execute after Role 3 is complete.*

EVALUATOR GATE COMPLETE — verdict: [confirmed/refuted/inconclusive], counter-evidence:
[rebutted/none], next step: [named]
```

---

## V-02 — Single Axis: Output Format
**Axis**: Table-driven format throughout — all structural requirements expressed as table rows (targets C-17, co-located rationale)
**Hypothesis**: Tabular co-location of anchor + rationale prevents rationale drift better than prose sections because table structure physically binds each rationale to its anchor row.

---

```markdown
Produce a prove-prototype artifact in the structured table format below.
The format is mandatory — do not convert tables to prose.
Fill every cell. Mark truly absent values as `—` with a reason, never leave blank.

---

## Phase 1 — DEFINE
*Gate: all rows in this table must be complete before Phase 2 begins.*
*Execute before Phase 2 gate is present in your output.*

| Element | Value | Rationale / Validity Reasoning |
|---------|-------|-------------------------------|
| Hypothesis (restated) | [exact restatement] | — (anchor element, no rationale required) |
| What to measure | [the observable] | [why this observable tests the hypothesis] |
| Success condition | [specific threshold or outcome] | [why this confirms the hypothesis] |
| Failure condition | [specific threshold or outcome] | [why this refutes the hypothesis] |
| Exclusion 1 | [what is excluded] | [why test remains valid without it] |
| Exclusion 2 | [what is excluded] | [why test remains valid without it] |
| Minimality trade-off | [what was left out] | [why omission still allows the test] |

**PHASE 1 COMPLETE** — hypothesis: [one sentence], measurement: [named observable],
success threshold: [stated condition], exclusions: [count named]

---

## Phase 2 — BUILD
*Gate: Phase 1 complete line must appear in your output before this phase begins.*
*Execute before Phase 3 gate is present in your output.*

| Element | Value |
|---------|-------|
| What was built | [description] |
| Replication step 1 | [tool / command / input] |
| Replication step 2 | [tool / command / input] |
| Replication step N | [tool / command / input — add rows as needed] |
| Prediction (recorded before results) | [expected outcome] |
| Raw result (concrete data point) | [observed value or outcome] |

**PHASE 2 COMPLETE** — predicted: [value], observed: [value]

---

## Phase 3 — COMPARE
*Gate: Phase 2 complete line must appear in your output before this phase begins.*
*Execute before Phase 4 gate is present in your output.*

| Element | Value | Rationale |
|---------|-------|-----------|
| Delta | [match / mismatch + magnitude] | [why the delta is what it is] |
| Verdict | [confirmed / refuted / inconclusive] | [why this verdict follows from the delta] |

**PHASE 3 COMPLETE** — delta: [described], verdict: [confirmed/refuted/inconclusive]

---

## Phase 4 — COUNTER-EVIDENCE
*Gate: Phase 3 complete line must appear in your output before this phase begins.*
*Execute before Phase 5 gate is present in your output.*

This section must close with one of exactly two dispositions. Silence or a missing
section does not pass.

| Element | Value | Disposition |
|---------|-------|-------------|
| Counter-interpretation (if any) | [name a specific alternative explanation] | (a) rebutted: [reasoning] |
| — OR — | | |
| No counter-interpretation | [explicit statement] | (b) none: [reason why no plausible alternative exists] |

**PHASE 4 COMPLETE** — counter-evidence: [rebutted / none + basis]

---

## Phase 5 — LIMITATIONS AND NEXT STEPS
*Execute after Phase 4 gate is present in your output.*

| Element | Value |
|---------|-------|
| One limitation | [what this prototype cannot tell us] |
| One specific next step | [what to build or test next] |

**PHASE 5 COMPLETE** — limitation: [named], next step: [named]
```

---

## V-03 — Single Axis: Lifecycle Emphasis
**Axis**: DEFINE / RUN / EVALUATE lifecycle containers as primary document structure (targets C-24, second detection level)
**Hypothesis**: Named lifecycle containers that map onto scientific method stages catch lifecycle inversions at document-structure level before any phase-level inspection is required.

---

```markdown
Produce a prove-prototype artifact organized within three named lifecycle containers.
The containers are DEFINE, RUN, and EVALUATE. They correspond to setup, execution,
and analysis stages of the scientific method.

Each container is a structural boundary. Phases within a container must belong to
that stage only. A phase in the wrong container is a lifecycle inversion — detectable
by structure before reading content.

---

# ╔══ LIFECYCLE: DEFINE ══╗
*Container purpose: establish everything that must exist before any build activity.*
*Phases in this container: hypothesis restatement, scope, measurement specification.*

---

## Phase D1 — Hypothesis
*Execute before Phase D2 gate is present in your output.*

Restate the hypothesis being tested. This must be the first substantive element.

**Hypothesis**: [restatement]

PHASE D1 COMPLETE — hypothesis established: [one-sentence summary]

---

## Phase D2 — Prototype Scope
*Execute after Phase D1 gate. Execute before Phase D3 gate is present in your output.*

State what the prototype does and does not do. Name at least two explicit exclusions.
For each exclusion, explain why the test remains valid without it.

**Exclusion 1**: [what is excluded]
**Why the test remains valid without it**: [reasoning — co-located]

**Exclusion 2**: [what is excluded]
**Why the test remains valid without it**: [reasoning — co-located]

**Minimality trade-off**: [what was left out and why that omission still allows the test]

PHASE D2 COMPLETE — scope boundary: [named], exclusions valid: [count]

---

## Phase D3 — Measurement Specification
*Execute after Phase D2 gate. This is the final phase in DEFINE.*
*All measurement criteria must be established before RUN begins.*

**What to measure**: [the observable quantity or outcome]
**Success condition**: [what result confirms the hypothesis]
**Failure condition**: [what result refutes the hypothesis]
**Prediction**: [what you expect to observe]

PHASE D3 COMPLETE — measurement: [named observable], success threshold: [stated],
prediction: [stated]

# ╚══ END: DEFINE ══╝

---

# ╔══ LIFECYCLE: RUN ══╗
*Container purpose: build the prototype and record raw results.*
*Phases in this container: construction, measurement, result recording.*
*Gate: DEFINE container must be complete before RUN begins.*

---

## Phase R1 — Build
*Execute after DEFINE container is complete. Execute before Phase R2 gate.*

Describe what was built. Then provide the replication path — every tool, input,
command, or step needed to reproduce. No implicit steps.

**What was built**: [description]

**Replication path**:
1. [step]
2. [step]
3. [step — add as needed]

PHASE R1 COMPLETE — prototype: [named/described in one line]

---

## Phase R2 — Measure
*Execute after Phase R1 gate. This is the final phase in RUN.*

Record the raw result. At least one concrete data point is required.

**Observed outcome**: [what actually happened]
**Raw data point**: [concrete value, count, latency, rate, or other specific evidence]

PHASE R2 COMPLETE — observed: [value], raw evidence: [stated]

# ╚══ END: RUN ══╝

---

# ╔══ LIFECYCLE: EVALUATE ══╗
*Container purpose: interpret results, render verdict, address counter-evidence.*
*Phases in this container: comparison, verdict, counter-evidence, closure.*
*Gate: RUN container must be complete before EVALUATE begins.*

---

## Phase E1 — Compare
*Execute after RUN container is complete. Execute before Phase E2 gate.*

**Delta**: [match or mismatch between prediction and observation]
**Why the delta is what it is**: [explanation co-located here]

PHASE E1 COMPLETE — delta: [described]

---

## Phase E2 — Verdict
*Execute after Phase E1 gate. Execute before Phase E3 gate.*

State whether the hypothesis is confirmed, refuted, or inconclusive.
Ground the verdict in the measured delta — do not assert it without evidence.

**Verdict**: [confirmed / refuted / inconclusive]
**Reasoning**: [why this verdict follows from the delta]

PHASE E2 COMPLETE — verdict: [confirmed/refuted/inconclusive], grounded: [yes]

---

## Phase E3 — Counter-Evidence
*Execute after Phase E2 gate. Execute before Phase E4 gate.*

This section must close with one of exactly two dispositions:
- (a) A named counter-interpretation with a grounded rebuttal, or
- (b) An explicit statement that no plausible counter-interpretation exists, with a reason.
Silence or a missing section does not pass.

[Address or explicitly close the counter-evidence question here.]

**Disposition**: [(a) rebutted: [reasoning] | (b) none: [reason]]

PHASE E3 COMPLETE — counter-evidence: [rebutted/none + basis]

---

## Phase E4 — Limitations and Next Steps
*Execute after Phase E3 gate.*

**One limitation**: [what this prototype cannot tell us]
**One specific next step**: [what to build or test next, and why]

PHASE E4 COMPLETE — limitation: [named], next step: [named]

# ╚══ END: EVALUATE ══╝
```

---

## V-04 — Combined: Role Sequence + Lifecycle Containers + Completion Lines with Result Values
**Axes**: Role sequence (C-23) + Lifecycle containers (C-24) + Completion lines with substantive result values enabling audit-by-scan (C-22)
**Hypothesis**: Combining role-labeled prohibitions inside named lifecycle containers, with completion lines that carry actual result values, creates three independent detection surfaces: container-level inversion detection, role-level contamination detection, and completion-line audit-by-scan — each catching failures the others would miss.

---

```markdown
Produce a prove-prototype artifact organized within three lifecycle containers
(DEFINE / RUN / EVALUATE), with three named roles (DEFINER, BUILDER, EVALUATOR),
each carrying explicit prohibitions. Every gate-protected phase closes with a
completion line that encodes the actual result established — not merely an assertion
that the phase is done. A reader who scans only completion lines must be able to
reconstruct the full outcome chain.

---

# ╔══ LIFECYCLE: DEFINE ══╗

## DEFINER — Phase 1: Hypothesis and Scope
**Role**: DEFINER
**Permitted**: Restate the hypothesis. Define prototype scope and exclusions.
Establish measurement criteria and prediction.
**Prohibited**: DEFINER must not describe build steps, report results, interpret
outcomes, or render any verdict. Build or result content here is a contamination error.

*Execute before Phase 2 gate is present in your output.*

**Hypothesis** (first element): [restatement of the hypothesis being tested]

**Scope exclusions** (minimum two):

**Exclusion 1**: [what is excluded]
**Why test remains valid without it**: [reasoning — co-located]

**Exclusion 2**: [what is excluded]
**Why test remains valid without it**: [reasoning — co-located]

**Minimality trade-off**: [what was left out and why the omission still allows the test]

**What to measure**: [the observable quantity or outcome]
**Success condition**: [what result confirms the hypothesis]
**Failure condition**: [what result refutes the hypothesis]
**Prediction**: [what you expect to observe before building]

PHASE 1 COMPLETE — hypothesis: [one sentence], measurement: [named observable],
success threshold: [stated condition], prediction: [stated value or outcome]

# ╚══ END: DEFINE ══╝

---

# ╔══ LIFECYCLE: RUN ══╗

## BUILDER — Phase 2: Construction and Measurement
**Role**: BUILDER
**Permitted**: Describe what was built. Provide replication path. Record raw results.
**Prohibited**: BUILDER must not interpret results, render a verdict, assess whether the
hypothesis is confirmed or refuted, or address counter-evidence. Interpretation here
is a contamination error.

*Execute after Phase 1 gate. Execute before Phase 3 gate is present in your output.*

**What was built**: [description]

**Replication path** (no implicit steps):
1. [tool / command / input]
2. [tool / command / input]
3. [tool / command / input — add rows as needed]

**Observed outcome**: [what actually happened]
**Raw data point**: [concrete value — number, rate, latency, count, or named finding]
**Delta**: [match or mismatch between prediction and observation]
**Why the delta is what it is**: [explanation co-located here]

PHASE 2 COMPLETE — predicted: [value from Phase 1], observed: [value],
delta: [match/mismatch], raw evidence: [stated]

# ╚══ END: RUN ══╝

---

# ╔══ LIFECYCLE: EVALUATE ══╗

## EVALUATOR — Phase 3: Verdict
**Role**: EVALUATOR
**Permitted**: Render hypothesis verdict. Address counter-evidence. State limitations
and next steps.
**Prohibited**: EVALUATOR must not re-describe the prototype, re-list build steps, or
repeat the construction narrative. Build description here is a contamination error.

*Execute after Phase 2 gate. Execute before Phase 4 gate is present in your output.*

**Verdict**: [confirmed / refuted / inconclusive]
**Reasoning**: [why this verdict follows from the delta in Phase 2]

PHASE 3 COMPLETE — verdict: [confirmed/refuted/inconclusive], grounded in: [delta value from Phase 2]

---

## EVALUATOR — Phase 4: Counter-Evidence
*Execute after Phase 3 gate. Execute before Phase 5 gate is present in your output.*

This section must close with one of exactly two dispositions. Silence or a section
structured only for the affirmative case does not pass.

- (a) A named counter-interpretation with a grounded rebuttal, or
- (b) An explicit statement that no plausible counter-interpretation exists, with a reason.

[Address or close the counter-evidence question here.]

**Disposition**: [(a) rebuttal: [reasoning grounded in evidence] | (b) none: [reason]]

PHASE 4 COMPLETE — counter-evidence: [rebutted: named interpretation / none: stated reason]

---

## EVALUATOR — Phase 5: Limitations and Next Steps
*Execute after Phase 4 gate.*

**One limitation**: [what this prototype cannot tell us]
**One specific next step**: [what to build or test next, and why]

PHASE 5 COMPLETE — limitation: [named], next step: [named action]

# ╚══ END: EVALUATE ══╝

---

## Audit-by-scan check
A reader who reads only the COMPLETE lines above must be able to answer:
what was hypothesized, what was predicted, what was observed, what the delta was,
and what verdict was rendered. Each completion line must carry actual result values —
not section headings restated as outcomes.
```

---

## V-05 — Combined: Phrasing Register + Inertia Framing
**Axes**: Conversational/imperative register + prominent status-quo competitor framing
**Hypothesis**: Anchoring the prototype against the status-quo alternative — what you'd do if you didn't build this — sharpens scope decisions and forces a more honest minimality justification, because the prototype must beat or expose the incumbent, not just function.

---

```markdown
You're building the smallest possible thing that tests your hypothesis.
Not a feature. Not a proof of concept that you'll refactor later.
A prototype: something that either confirms or kills the hypothesis before you
commit to building the real thing.

Before you write anything else, answer this: what's the status-quo alternative?
What would someone do instead if this prototype didn't exist? That alternative
is your competitor. The prototype only matters if it reveals something the
status quo can't.

Work through the following phases in order. Do not skip ahead.

---

## Phase 1 — What You're Testing
*Write this before you describe anything you built.*
*Execute before Phase 2 gate is present in your output.*

**Hypothesis** (first thing, no exceptions):
Write out the hypothesis being tested. Exact words if you have them, your own
words if not. This must appear before any prototype description.

**The status-quo alternative**:
Name what you'd do instead — the existing approach, the workaround, the
nothing. What does the prototype need to reveal that the status quo cannot?

**What you're measuring**:
Name the observable. What specifically will you look at to know if the
hypothesis holds?

**Success looks like**: [specific outcome that confirms]
**Failure looks like**: [specific outcome that refutes]
**Inconclusive looks like**: [what would leave the question open]

**What you predicted would happen** (write this now, before Phase 2):
[your honest prediction before you see the results]

**What you're leaving out** (minimum two things):
The prototype doesn't do everything. Name at least two things you deliberately
excluded, and for each one, explain why the test is still valid without it.

- Excluded: [thing 1] — still valid because: [reason]
- Excluded: [thing 2] — still valid because: [reason]

**Minimality call**: What's the one thing you're most tempted to add but
consciously chose not to? Why does leaving it out not invalidate the test?

PHASE 1 COMPLETE — hypothesis: [one sentence], competing approach: [named],
measurement: [observable], prediction: [stated outcome]

---

## Phase 2 — What You Built and What Happened
*Execute after Phase 1 gate. Execute before Phase 3 gate is present in your output.*

**What you built**:
Describe the prototype. Keep it short — if the description is longer than the
prototype, something is wrong.

**How to reproduce it** (no hand-waving):
List every step, tool, input, and command someone would need to get the same
result. If a step is "obvious," write it anyway.

1. [step]
2. [step]
3. [step — add as needed]

**What actually happened**:
Report the result. Include at least one concrete data point — a number, a rate,
a count, a named observation. Not "it worked," but how, how fast, how often,
or under what conditions.

**Predicted vs. actual**:
You wrote a prediction in Phase 1. Compare it here.

| | Value |
|---|---|
| Predicted | [from Phase 1] |
| Observed | [what happened] |
| Delta | [match or mismatch — and why] |

The "why" belongs in the delta row, not in a separate interpretation section.

PHASE 2 COMPLETE — predicted: [value], observed: [value], delta: [match/mismatch + reason]

---

## Phase 3 — What It Means
*Execute after Phase 2 gate. Execute before Phase 4 gate is present in your output.*

**Verdict**: Confirmed / Refuted / Inconclusive
Say it plainly. Then say why the delta in Phase 2 leads to this verdict.
Don't assert a verdict and then explain something unrelated.

**Verdict**: [confirmed / refuted / inconclusive]
**Why**: [direct connection to the measured delta]

**How this compares to the status-quo alternative**:
Go back to what you named in Phase 1. Does the prototype reveal something the
status quo couldn't show? If the verdict is confirmed: what does the status quo
miss? If refuted: does the status quo actually work fine?

PHASE 3 COMPLETE — verdict: [confirmed/refuted/inconclusive], status-quo comparison: [stated]

---

## Phase 4 — The Skeptic's Objection
*Execute after Phase 3 gate. Execute before Phase 5 gate is present in your output.*

Someone skeptical of your result will ask: couldn't something else explain this?
This section must close with one of exactly two dispositions — no third option:

- (a) Name the most plausible alternative explanation and rebut it with
  evidence from Phase 2. Not a general rebuttal — specific.
- (b) Explicitly state that no plausible alternative explanation exists,
  and say why.

A missing section, or a section that only handles case (a), does not count.

[Write the skeptic's objection and your response here.]

**Disposition**: [(a) counter: [named alternative] — rebutted because: [evidence-grounded reason]
| (b) none: [explicit reason no alternative is plausible]]

PHASE 4 COMPLETE — counter-evidence: [rebutted: named / none: stated reason]

---

## Phase 5 — What's Next
*Execute after Phase 4 gate.*

**One limitation**: What can't this prototype tell you, even though it just ran?
Don't list everything — pick the one limitation that matters most for the
hypothesis.

**One next step**: Given the verdict, what's the single most useful thing to
do next? Name it specifically — not "investigate further" but what to build,
test, or measure.

PHASE 5 COMPLETE — limitation: [named], next step: [specific action]
```

---

## Variation Summary

| ID | Variation Axis | Key Structural Bet | Primary Rubric Targets |
|----|---------------|-------------------|------------------------|
| V-01 | Role sequence | DEFINER/BUILDER/EVALUATOR with explicit prohibitions per role | C-23, C-19, C-20, C-22 |
| V-02 | Output format | Table-driven: anchor + rationale in same row throughout | C-17, C-18, C-03, C-04 |
| V-03 | Lifecycle emphasis | DEFINE/RUN/EVALUATE containers as primary structure | C-24, C-19, C-20, C-21 |
| V-04 | Role sequence + Lifecycle containers + Completion lines | Three independent detection surfaces; audit-by-scan completion lines | C-22, C-23, C-24, C-20 |
| V-05 | Phrasing register + Inertia framing | Conversational voice; status-quo competitor named in Phase 1 and revisited in Phase 3 | C-06, C-16, C-18, C-04 |
