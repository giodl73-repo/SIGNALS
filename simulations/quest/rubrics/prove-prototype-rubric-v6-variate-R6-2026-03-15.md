# prove-prototype — Round 6 Variations (v6 rubric)

**Date**: 2026-03-15
**Rubric version**: v6 (170 pts; C-22, C-23, C-24 added)
**Test variable**: C-22 (completion-line-as-audit-by-scan), C-23 (role-attribution-as-contamination-guard),
C-24 (lifecycle-container-as-second-detection-level). All five variations target full C-22 compliance as
a baseline (Round 5 ceiling was 140; all additional 30 pts come from C-22/C-23/C-24). Variations test
which combinations achieve ceiling.

**Axis plan**:
- V-01: Single-axis — Role Sequence (DEFINER → BUILDER → EVALUATOR) with explicit per-role prohibitions (C-23)
- V-02: Single-axis — Table-driven format with information-rich completion lines (C-22)
- V-03: Single-axis — Lifecycle containers (DEFINE / RUN / EVALUATE) (C-24)
- V-04: Combined — Lifecycle containers + Role sequence with prohibitions (C-23 + C-24)
- V-05: Combined — All three axes + B-00 inertia baseline (C-22 maximized + C-23 + C-24)

---

## V-01 — Single Axis: Role Sequence with Explicit Prohibitions

**Axis**: Role sequence — three sequential roles, each carrying explicit named prohibitions
**Hypothesis**: Role labels that carry explicit prohibitions (naming the content type each role must not
produce) catch in-order but out-of-role contamination that phase-gate ordering alone cannot detect.

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
and next steps.
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

EVALUATOR GATE COMPLETE — verdict: [confirmed/refuted/inconclusive], counter-evidence:
[rebutted/none], next step: [named]
```

---

## V-02 — Single Axis: Table-Driven with Information-Rich Completion Lines

**Axis**: Output format — table-row gates throughout; completion lines carry multiple substantive
values (hypothesis text, measurement name, threshold, count, delta, verdict) enabling audit-by-scan
**Hypothesis**: Completion lines that encode multiple substantive result values create a cross-phase
audit path — a reader scanning only completion lines can reconstruct the full experimental outcome
chain without reading phase bodies.

---

```markdown
Produce a prove-prototype artifact in the structured table format below.
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
| Counter-interpretation | [name a specific alternative explanation, or: None] | |
| Rebuttal / Reason | [why it does not hold using Phase 2–3 evidence, or: why none is plausible] | |
| **Disposition** | | A: counter-interpretation named and rebutted — OR — B: no plausible counter-interpretation; [reason] |

**PHASE 4 COMPLETE — DISPOSITION [A or B]** — counter-evidence: [rebutted/none + reason]

---

## Phase 5 — LIMITATIONS AND NEXT STEP
*Gate: Phase 4 complete line must appear in your output before this phase begins.*
*Execute before Phase 6 gate is present in your output.*

| Element | Value | Disposition |
|---------|-------|-------------|
| Limitation | [one specific confound or constraint particular to this prototype run] | |
| Next step | [one specific action: what to build, test, or change — "do more research" does not pass] | |
| **Disposition** | | A: limitation and next step recorded — OR — B: [explain why a specific limitation or next step cannot be stated] |

**PHASE 5 COMPLETE — DISPOSITION [A or B]** — limitation: [named], next step: [named]

---

## Phase 6 — REPLICATION PATH
*Gate: Phase 5 complete line must appear in your output before this phase begins.*
*Execute after Phase 5 gate is present in your output.*

| Element | Value |
|---------|-------|
| Step 1 | [tool, input, command, or configuration — no implicit steps] |
| Step 2 | [continue for every step] |
| ... | |
| **Disposition** | A: replication path complete — OR — B: [name the step that cannot be fully specified and why] |

**PHASE 6 COMPLETE — DISPOSITION [A or B]** — replication: [complete/partial + reason]

No "etc." No "standard setup." Configuration files named. Environment requirements explicit.
```

---

## V-03 — Single Axis: Lifecycle Containers (DEFINE / RUN / EVALUATE)

**Axis**: Lifecycle emphasis — three named structural containers group phases by experimental stage,
providing document-structure-level detection of lifecycle inversions independent of phase-gate ordering
**Hypothesis**: Named lifecycle containers as structural section boundaries create an independent
detection surface for lifecycle-order inversions: a container-boundary scan catches violations before
any phase-level inspection is required, and this detection capability is orthogonal to role attribution
and phase-gate ordering.

---

```markdown
You are producing a `prove-prototype` artifact. The artifact is organized into three lifecycle
containers — DEFINE, RUN, and EVALUATE — and nine phases. Each lifecycle container encloses
only phases that belong to that experimental stage. Gates and completion lines govern all nine
phases.

---

## LIFECYCLE: DEFINE
*Phases 1, 2, and 3. Establish the hypothesis, scope, and measurement protocol before any
build activity. No observed values appear in this lifecycle. No build content appears here.*

---

### PHASE 1 — HYPOTHESIS

*Execute before anything else. This phase must appear as the first element of your output.
Nothing precedes it.*

Restate the hypothesis being tested. The hypothesis is a single falsifiable claim.

**Hypothesis**: [the falsifiable claim — what behavior or property the prototype demonstrates]

**Confirmed if**: [the observable outcome that confirms the claim]

**Refuted if**: [the observable outcome that refutes the claim]

**PHASE 1 COMPLETE — hypothesis established: [hypothesis in one phrase]**

---

### PHASE 2 — SCOPE

*Execute after Phase 1 completion line is present in your output.*

Define the prototype boundary. For each excluded item, state why the hypothesis remains
testable without it.

| Excluded item | Why the hypothesis remains testable without it |
|---------------|------------------------------------------------|
| [item 1] | [reason — "it wasn't needed" does not answer this question] |
| [item 2] | [reason] |

Minimum two exclusions. Each exclusion answers the test-validity question in the same row.

**PHASE 2 COMPLETE — scope established: [prototype name in one phrase]**

---

### PHASE 3 — MEASUREMENT PROTOCOL

*Execute after Phase 2 completion line is present in your output. Measurement protocol must
be complete and this completion line present before Phase 4 begins. The protocol is frozen
at the end of this phase — it may not be modified in LIFECYCLE: RUN.*

| Metric | Collection method | Success condition | Failure condition |
|--------|-------------------|-------------------|-------------------|
| [metric name] | [how observed] | [value that confirms] | [value that refutes] |

No observed values in this phase.

**PHASE 3 COMPLETE — measurement protocol frozen before build: metric = [name],
success condition = [value]**

---

## LIFECYCLE: RUN
*Phases 4 and 5. Build the prototype and record results. The measurement protocol from
Phase 3 is inherited unchanged. No evaluation, verdict, or interpretation in this lifecycle.*

---

### PHASE 4 — BUILD

*Execute after Phase 3 completion line is present in your output.*

Describe what was built. State the minimal implementation. Name every tool, input, and
configuration. No scope expansion. No implicit steps.

**What was built**: [minimal implementation description]

**Tools and inputs**: [every tool, library, input, and configuration]

**PHASE 4 COMPLETE — prototype built: [artifact name in one phrase]**

---

### PHASE 5 — RESULTS

*Execute after Phase 4 completion line is present in your output.*

| Row | Value |
|-----|-------|
| **Predicted** | [Phase 3 success condition — what was expected] |
| **Actual** | [observed value — at least one concrete data point: number, count, time, or direct quote] |
| **Delta** | [predicted − actual; "0 — prediction confirmed" if equal; do not leave for reader to compute] |
| **Why the delta is what it is** | [cause of gap — not a restatement of Actual; co-located in this row] |

**PHASE 5 COMPLETE — results recorded: predicted = [value], observed = [value],
delta = [phrase]**

---

## LIFECYCLE: EVALUATE
*Phases 6, 7, 8, and 9. Evaluate evidence and record conclusions. No build content in
this lifecycle. No new measurement definitions.*

---

### PHASE 6 — COUNTER-EVIDENCE

*Execute after Phase 5 completion line is present in your output.*

If a counter-interpretation exists:
- **Counter-interpretation**: [the alternative reading]
- **Rebuttal**: [why it does not hold, using Phase 5 evidence]

If none exists:
- **Counter-interpretation**: None
- **Reason**: [why no alternative reading of the Phase 5 evidence is plausible]

Write exactly one of the following as the terminal element:

A) `PHASE 6 COMPLETE — DISPOSITION A: counter-interpretation named and rebutted`
B) `PHASE 6 COMPLETE — DISPOSITION B: no plausible counter-interpretation — [reason]`

---

### PHASE 7 — VERDICT

*Execute after Phase 6 completion line is present in your output.*

| Field | Value |
|-------|-------|
| **Verdict** | Confirmed / Refuted / Inconclusive [choose one] |
| **Verdict rationale** | [reasoning connecting Phase 5 delta to verdict — not a restatement of Phase 5; one to three sentences] |

**PHASE 7 COMPLETE — verdict: [verdict word]**

---

### PHASE 8 — LIMITATIONS AND NEXT STEP

*Execute after Phase 7 completion line is present in your output.*

**Limitation**: [one specific confound or constraint particular to this prototype run and metric]

**Next step**: [one specific action: what to build, test, or change — "do more research" does not pass]

Write exactly one of the following as the terminal element:

A) `PHASE 8 COMPLETE — DISPOSITION A: limitation and next step recorded`
B) `PHASE 8 COMPLETE — DISPOSITION B: [what prevented naming a specific limitation or next step, and why]`

---

### PHASE 9 — REPLICATION PATH

*Execute after Phase 8 completion line is present in your output.*

Every step to reproduce this prototype run. A reader unfamiliar with this work replicates
from this phase alone. No implicit steps. Configuration files named. Environment requirements stated.

1. [step 1]
2. [step 2]
3. [continue]

Write exactly one of the following as the terminal element:

A) `PHASE 9 COMPLETE — DISPOSITION A: replication path complete`
B) `PHASE 9 COMPLETE — DISPOSITION B: [step that cannot be fully specified, and why]`
```

---

## V-04 — Combined: Lifecycle Containers + Role Sequence with Explicit Prohibitions

**Axes**:
1. Lifecycle containers (DEFINE / RUN / EVALUATE) — structural boundaries for C-24
2. Role sequence (DEFINER → BUILDER → EVALUATOR) with explicit prohibitions — for C-23

**Hypothesis**: Aligning lifecycle containers with roles one-to-one (each lifecycle container
enclosing exactly one role's phases) creates two structurally independent detection surfaces:
container-boundary scan catches lifecycle-order inversions, role-prohibition scan catches
in-order out-of-role content. Each mechanism detects a failure class the other cannot.

---

```markdown
You are producing a `prove-prototype` artifact. Three lifecycle containers organize the
output by experimental stage. Within each lifecycle container, a named role governs phase
content. Roles carry explicit prohibitions. Gates and completion lines govern all nine phases.

---

## LIFECYCLE: DEFINE
*Phases 1, 2, and 3. No build activity. No observed values. No evaluation content.*

**DEFINER** governs this lifecycle.
**DEFINER is prohibited from**: describing construction steps, reporting observed outcomes,
interpreting results, or referencing what actually happened. Any such content appearing
within LIFECYCLE: DEFINE is a contamination error detectable by container-boundary scan.

---

### PHASE 1 — HYPOTHESIS

*DEFINER. Execute before anything else. First element of your output.*

**Hypothesis**: [the falsifiable claim — what behavior or property the prototype demonstrates]

**Confirmed if**: [observable outcome that confirms]

**Refuted if**: [observable outcome that refutes]

**PHASE 1 COMPLETE — DEFINER: hypothesis established — [hypothesis in one phrase]**

---

### PHASE 2 — SCOPE

*DEFINER. Execute after Phase 1 completion line is present in your output.*

| Excluded item | Why the hypothesis remains testable without it |
|---------------|------------------------------------------------|
| [item 1] | [reason] |
| [item 2] | [reason] |

Minimum two exclusions. "It wasn't needed" does not answer the test-validity question.

**PHASE 2 COMPLETE — DEFINER: scope established — [prototype name in one phrase]**

---

### PHASE 3 — MEASUREMENT PROTOCOL

*DEFINER. Execute after Phase 2 completion line is present in your output. This phase must
close and its completion line must appear before LIFECYCLE: RUN begins. The protocol is
frozen here — BUILDER may not modify it.*

| Metric | Collection method | Success condition | Failure condition |
|--------|-------------------|-------------------|-------------------|
| [metric] | [method] | [value that confirms] | [value that refutes] |

No observed values in this phase.

**PHASE 3 COMPLETE — DEFINER: measurement protocol frozen before build —
metric = [name], success condition = [value]**

---

## LIFECYCLE: RUN
*Phases 4 and 5. Build and observe. No evaluation content. No verdict. No counter-evidence.*

**BUILDER** governs this lifecycle.
**BUILDER is prohibited from**: interpreting results, rendering a verdict, addressing
counter-evidence, or assessing whether the hypothesis is confirmed or refuted. Any such
content appearing within LIFECYCLE: RUN is a contamination error detectable by
container-boundary scan.

---

### PHASE 4 — BUILD

*BUILDER. Execute after Phase 3 completion line is present in your output.*

**What was built**: [minimal implementation — no scope expansion beyond Phase 2]

**Tools and inputs**: [every tool, library, input, and configuration — no implicit steps]

**PHASE 4 COMPLETE — BUILDER: prototype built — [artifact name in one phrase]**

---

### PHASE 5 — RESULTS

*BUILDER. Execute after Phase 4 completion line is present in your output.*

| Row | Value |
|-----|-------|
| **Predicted** | [Phase 3 success condition] |
| **Actual** | [observed value — at least one concrete data point: number, count, time, or direct quote] |
| **Delta** | [predicted − actual; "0 — prediction confirmed" if equal; do not leave for reader to compute] |
| **Why the delta is what it is** | [cause of gap — not a restatement of Actual; co-located in this row] |

**PHASE 5 COMPLETE — BUILDER: results recorded — predicted = [value], observed = [value],
delta = [phrase]**

---

## LIFECYCLE: EVALUATE
*Phases 6, 7, 8, and 9. Evaluate evidence and record conclusions. No build content. No
new measurement definitions. No restating what was built.*

**EVALUATOR** governs this lifecycle.
**EVALUATOR is prohibited from**: describing what was built, re-listing construction steps,
re-describing what the prototype does, or re-stating the build tools used. Any such content
appearing within LIFECYCLE: EVALUATE is a contamination error detectable by container-boundary scan.

---

### PHASE 6 — COUNTER-EVIDENCE

*EVALUATOR. Execute after Phase 5 completion line is present in your output.*

If a counter-interpretation exists:
- **Counter-interpretation**: [alternative reading of Phase 5 evidence]
- **Rebuttal**: [why it does not hold, using Phase 5 evidence]

If none exists:
- **Counter-interpretation**: None
- **Reason**: [why no alternative reading of Phase 5 evidence is plausible]

Write exactly one of the following as the terminal element:

A) `PHASE 6 COMPLETE — EVALUATOR: DISPOSITION A — counter-interpretation named and rebutted`
B) `PHASE 6 COMPLETE — EVALUATOR: DISPOSITION B — no plausible counter-interpretation — [reason]`

---

### PHASE 7 — VERDICT

*EVALUATOR. Execute after Phase 6 completion line is present in your output.*

| Field | Value |
|-------|-------|
| **Verdict** | Confirmed / Refuted / Inconclusive [choose one] |
| **Verdict rationale** | [reasoning connecting Phase 5 delta to verdict — not a restatement of Phase 5; one to three sentences] |

**PHASE 7 COMPLETE — EVALUATOR: verdict — [verdict word]**

---

### PHASE 8 — LIMITATIONS AND NEXT STEP

*EVALUATOR. Execute after Phase 7 completion line is present in your output.*

**Limitation**: [one specific confound or constraint particular to this prototype run and metric — not a generic disclaimer]

**Next step**: [one specific action: what to build, test, or change — "do more research" does not pass]

Write exactly one of the following as the terminal element:

A) `PHASE 8 COMPLETE — EVALUATOR: DISPOSITION A — limitation and next step recorded`
B) `PHASE 8 COMPLETE — EVALUATOR: DISPOSITION B — [what prevented naming a specific limitation or next step, and why]`

---

### PHASE 9 — REPLICATION PATH

*EVALUATOR. Execute after Phase 8 completion line is present in your output.*

Every step to reproduce this prototype run. No implicit steps. Configuration files named.

1. [step 1]
2. [step 2]
3. [continue]

Write exactly one of the following as the terminal element:

A) `PHASE 9 COMPLETE — EVALUATOR: DISPOSITION A — replication path complete`
B) `PHASE 9 COMPLETE — EVALUATOR: DISPOSITION B — [step that cannot be fully specified, and why]`
```

---

## V-05 — Combined: All Three New Axes + B-00 Inertia Baseline

**Axes**:
1. Lifecycle containers (DEFINE / RUN / EVALUATE) — C-24
2. Role sequence (DEFINER → BUILDER → EVALUATOR) with explicit prohibitions — C-23
3. B-00 inertia baseline propagated through completion lines — C-22 maximized

**Hypothesis**: Adding a pre-declared inertia baseline (B-00) to information-rich completion lines
creates a multi-dimensional audit-by-scan capability: completion lines encode both experimental
outcome and baseline-relative calibration, allowing a reviewer to verify experimental validity and
baseline significance by scanning completion lines alone — a two-chain audit unavailable when
completion lines carry only experimental values.

---

```markdown
You are producing a `prove-prototype` artifact. Three lifecycle containers organize the
output. Roles govern phase content within each container. B-00 is the inertia baseline:
what would be observed if no prototype were built. B-00 is declared in Phase 1, frozen
in Phase 3, and read-only in all subsequent phases.

---

## LIFECYCLE: DEFINE
*Phases 1, 2, and 3. No build activity. No observed values. No evaluation content.*

**DEFINER** governs this lifecycle.
**DEFINER is prohibited from**: describing construction steps, reporting observed outcomes,
interpreting results, or referencing what actually happened.

---

### PHASE 1 — HYPOTHESIS + BASELINE

*DEFINER. Execute before anything else. First element of your output.*

Declare two things: the experimental hypothesis (E) and the inertia baseline (B-00).

**Hypothesis (E)**: [the falsifiable claim — what the prototype is expected to demonstrate]

**Confirmed if**: [observable outcome that confirms E]

**Refuted if**: [observable outcome that refutes E]

**Inertia baseline (B-00)**: [what would be observed if no prototype were built; frozen here;
may not be revised after this phase]

**PHASE 1 COMPLETE — DEFINER: hypothesis and B-00 declared —
E = [experimental claim in one phrase], B-00 = [baseline in one phrase]**

---

### PHASE 2 — SCOPE

*DEFINER. Execute after Phase 1 completion line is present in your output.*

| Excluded item | Why the hypothesis remains testable without it |
|---------------|------------------------------------------------|
| [item 1] | [reason] |
| [item 2] | [reason] |

**PHASE 2 COMPLETE — DEFINER: scope established — [prototype name in one phrase]**

---

### PHASE 3 — MEASUREMENT PROTOCOL

*DEFINER. Execute after Phase 2 completion line is present in your output. This phase must
close before LIFECYCLE: RUN begins. The protocol and B-00 threshold are frozen here.*

| Metric | Collection method | E threshold (experimental) | B-00 threshold (inertia) | Confirm E | Refute E |
|--------|-------------------|---------------------------|--------------------------|-----------|----------|
| [metric] | [method] | [predicted E value] | [predicted B-00 value] | [condition] | [condition] |

No observed values here.

**PHASE 3 COMPLETE — DEFINER: measurement protocol and B-00 threshold frozen before build —
metric = [name], E = [value], B-00 = [value]**

---

## LIFECYCLE: RUN
*Phases 4 and 5. Build and observe. No evaluation content. B-00 threshold is read-only.*

**BUILDER** governs this lifecycle.
**BUILDER is prohibited from**: interpreting results, rendering a verdict, addressing
counter-evidence, or assessing whether the hypothesis is confirmed or refuted.

---

### PHASE 4 — BUILD

*BUILDER. Execute after Phase 3 completion line is present in your output.*

**What was built**: [minimal implementation — no scope expansion beyond Phase 2]

**Tools and inputs**: [every tool, library, input, and configuration — no implicit steps]

**PHASE 4 COMPLETE — BUILDER: prototype built — [artifact name in one phrase]**

---

### PHASE 5 — RESULTS

*BUILDER. Execute after Phase 4 completion line is present in your output.*

| Row | Value |
|-----|-------|
| **E (predicted)** | [Phase 3 experimental threshold] |
| **B-00 (inertia)** | [Phase 3 inertia threshold — read-only, unchanged] |
| **Actual** | [observed value — at least one concrete data point: number, count, time, or direct quote] |
| **E vs. Actual (delta)** | [E − actual; "0 — prediction confirmed" if equal; do not leave for reader to compute] |
| **B-00 vs. Actual** | [B-00 − actual; which direction did actual land relative to status quo?] |
| **Why the delta is what it is** | [cause of E vs. Actual gap — not a restatement of Actual] |

**PHASE 5 COMPLETE — BUILDER: results recorded —
E vs. Actual = [delta in one phrase], actual vs. B-00 = [relationship in one phrase]**

---

## LIFECYCLE: EVALUATE
*Phases 6, 7, 8, and 9. Evaluate evidence. No build content. B-00 comparison informs verdict.*

**EVALUATOR** governs this lifecycle.
**EVALUATOR is prohibited from**: describing what was built, re-listing construction steps,
or re-describing what the prototype does.

---

### PHASE 6 — COUNTER-EVIDENCE

*EVALUATOR. Execute after Phase 5 completion line is present in your output.*

If a counter-interpretation exists:
- **Counter-interpretation**: [alternative reading of Phase 5 evidence]
- **Rebuttal**: [why it does not hold, using Phase 5 evidence]

If none exists:
- **Counter-interpretation**: None
- **Reason**: [why no alternative reading is plausible]

Write exactly one of the following as the terminal element:

A) `PHASE 6 COMPLETE — EVALUATOR: DISPOSITION A — counter-interpretation named and rebutted`
B) `PHASE 6 COMPLETE — EVALUATOR: DISPOSITION B — no plausible counter-interpretation — [reason]`

---

### PHASE 7 — VERDICT

*EVALUATOR. Execute after Phase 6 completion line is present in your output.*

| Field | Value |
|-------|-------|
| **Verdict** | Confirmed / Refuted / Inconclusive [choose one] |
| **Verdict rationale** | [reasoning connecting Phase 5 delta to verdict — not a restatement of Phase 5] |
| **B-00 calibration** | [did the actual result exceed, match, or fall below B-00? What does this mean for the forward decision?] |

**PHASE 7 COMPLETE — EVALUATOR: verdict — [verdict word];
B-00 calibration: [above/below/at B-00 in one phrase]**

---

### PHASE 8 — LIMITATIONS AND NEXT STEP

*EVALUATOR. Execute after Phase 7 completion line is present in your output.*

**Limitation**: [one specific confound or constraint particular to this prototype run and metric — not a generic disclaimer]

**Next step**: [one specific action: what to build, test, or change — "do more research" does not pass]

Write exactly one of the following as the terminal element:

A) `PHASE 8 COMPLETE — EVALUATOR: DISPOSITION A — limitation and next step recorded`
B) `PHASE 8 COMPLETE — EVALUATOR: DISPOSITION B — [what prevented naming a specific limitation or next step, and why]`

---

### PHASE 9 — REPLICATION PATH

*EVALUATOR. Execute after Phase 8 completion line is present in your output.*

Every step to reproduce this prototype run. No implicit steps. Configuration files named.

1. [step 1]
2. [step 2]
3. [continue]

Write exactly one of the following as the terminal element:

A) `PHASE 9 COMPLETE — EVALUATOR: DISPOSITION A — replication path complete`
B) `PHASE 9 COMPLETE — EVALUATOR: DISPOSITION B — [step that cannot be fully specified, and why]`
```

---

## Axis Summary

| Variation | Single/Combined | Primary axis | C-22 mechanism | C-23 coverage | C-24 coverage |
|-----------|-----------------|--------------|----------------|---------------|---------------|
| V-01 | Single | Role sequence with prohibitions | 3 completion lines carrying hypothesis/delta/verdict values | 3 roles with explicit named prohibitions | PARTIAL — roles serve as quasi-containers but detection not independent of C-23 |
| V-02 | Single | Table-driven with rich completion lines | 6 completion lines; Phase 1 carries hypothesis + measurement + threshold + exclusion count | None | None |
| V-03 | Single | Lifecycle containers | 9 completion lines carrying substantive values at every phase | None | DEFINE/RUN/EVALUATE structural headers; detection independent of phase gates |
| V-04 | Combined | Lifecycle containers + Role prohibitions | 9 completion lines; all phases + lifecycle container boundaries | 3 roles (DEFINER/BUILDER/EVALUATOR) with named prohibitions; roles scoped to lifecycle | DEFINE/RUN/EVALUATE structural headers; detection independent of C-23 |
| V-05 | Combined | All three axes + B-00 | 9 completion lines; B-00 values in Phases 1/3/5/7 create two-chain audit (experimental + baseline-relative) | Same as V-04 | Same as V-04 |

**Round 6 design intent**: Every variation achieves at least C-22 (Round 5 demonstrated that
information-rich completion lines are achievable in any format). The discriminating variables
are C-23 and C-24, and specifically whether C-24 can be achieved independently of C-23.
V-01 demonstrates that roles-as-containers do not achieve C-24 independence. V-03 demonstrates
C-24 with single-axis lifecycle containers. V-04 and V-05 demonstrate that C-23 + C-24 can
be achieved simultaneously without structural conflict.
