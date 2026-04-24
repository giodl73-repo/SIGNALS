# prove-prototype — Round 5 Variations (v5 rubric)

**Date**: 2026-03-15
**Rubric version**: v5 (140 pts; C-20 and C-21 added)
**Test variable**: C-20 (model-written gate completion artifact) and C-21 (gate coverage
includes all trailing optional sections). All five variations target full C-19/C-20/C-21
compliance using different structural axes. Round 4's V-02 (Phase Gates, execute-before)
is the reference architecture for C-20 and C-21 — all five variations here attempt to meet
or exceed that bar through different structural approaches.

**Axis plan**:
- V-01: Single-axis — Role Sequence (DEFINER → EXPERIMENTER → EVALUATOR, 3 sequential roles)
- V-02: Single-axis — Output Format (table-row gates: gate as leading table row, completion as trailing summary row)
- V-03: Single-axis — Phrasing Register (formal/structural — "The following must be established...")
- V-04: Combined — Lifecycle emphasis (DEFINE / RUN / EVALUATE lifecycle containers) + Inertia framing (B-00 baseline declared in Phase 1)
- V-05: Combined — Role Sequence (2 roles: DESIGNER + ANALYST) + Output Format (labeled-pair blocks with gate footers)

---

## V-01 — Single-axis: Role Sequence (DEFINER → EXPERIMENTER → EVALUATOR)

**Axis**: Role sequence — three sequential roles, each phase-scoped to a distinct responsibility
**Hypothesis**: Declaring three phase-scoped roles before output begins makes structural separation
of definition (phases 1–3), execution (phases 4–5), and evaluation (phases 6–9) verifiable by
role-declaration scan, and places gate-completion artifacts under role authority rather than
document convention.

---

### ROLE DECLARATIONS

*Read before producing any output. Three sequential roles govern this skill. No role may produce
output that belongs to a subsequent role's phase scope.*

**DEFINER** — Governs Phases 1, 2, and 3. DEFINER establishes the hypothesis, scope, and
measurement protocol. No build activity occurs during DEFINER phases. Every DEFINER phase closes
with a DEFINER-written completion line before EXPERIMENTER begins.

**EXPERIMENTER** — Governs Phases 4 and 5. EXPERIMENTER describes what was built and records
observed results. EXPERIMENTER inherits the measurement protocol from Phase 3 unchanged.
EXPERIMENTER does not redefine metrics or success conditions. Every EXPERIMENTER phase closes
with an EXPERIMENTER-written completion line before EVALUATOR begins.

**EVALUATOR** — Governs Phases 6, 7, 8, and 9. EVALUATOR does not describe build activity.
EVALUATOR does not restate results. EVALUATOR's exclusive function is to evaluate evidence
produced by EXPERIMENTER against the hypothesis established by DEFINER. Every EVALUATOR phase
closes with an EVALUATOR-written completion line. Phase 9 closes with a replication-complete line.

---

### PHASE 1 — HYPOTHESIS

*DEFINER. Execute before anything else. This phase must appear as the first element of your
output. Nothing precedes it.*

Restate the hypothesis being tested. The hypothesis is a single falsifiable claim: if you built
and measured [this], you expected to observe [that]. State it before any description of what was
built or what happened.

The hypothesis must name:
- The behavior or property the prototype is designed to demonstrate
- The observable outcome that would confirm the hypothesis
- The observable outcome that would refute it

No build content. No results. The hypothesis only.

**PHASE 1 COMPLETE — hypothesis established: [write the hypothesis in one sentence as the
terminal line of this phase before Phase 2 begins]**

---

### PHASE 2 — SCOPE

*DEFINER. Execute after Phase 1 completion line is present in your output.*

Define the prototype boundary. State what it does and does not include. For every excluded item,
answer the test-validity question: without this, can the prototype still test the hypothesis?

| What is excluded | Why the hypothesis remains testable without it |
|------------------|------------------------------------------------|
| [exclusion 1]    | [reason — "it wasn't needed" does not answer this question] |
| [exclusion 2]    | [reason — answer what the test depends on and confirm this exclusion does not break that dependency] |

Minimum two exclusions. Each exclusion answers the test-validity question in the same row.

**PHASE 2 COMPLETE — scope boundary established: [name the prototype in one phrase as the
terminal line of this phase before Phase 3 begins]**

---

### PHASE 3 — MEASUREMENT PROTOCOL

*DEFINER. Execute after Phase 2 completion line is present in your output. This phase must be
complete before Phase 4 begins. The measurement protocol is frozen at the end of this phase —
EXPERIMENTER may not modify it.*

Define what will be measured and how, before anything is built. Success and failure conditions
are established here, not after results are observed.

| Metric | Collection method | Success condition | Failure condition |
|--------|-------------------|-------------------|-------------------|
| [metric name] | [how it is collected] | [what result confirms the hypothesis] | [what result refutes the hypothesis] |

No observed values here. The measurement plan only.

**PHASE 3 COMPLETE — measurement protocol frozen before build: [name the metric and its
success condition in one phrase as the terminal line of this phase before Phase 4 begins]**

---

### PHASE 4 — BUILD

*EXPERIMENTER. Execute after Phase 3 completion line is present in your output.*

Describe what was built. State the minimal implementation that tests the hypothesis — nothing
beyond what is required. Do not expand the scope defined in Phase 2. Do not add measurement
criteria not defined in Phase 3.

Name every tool, input, and configuration used. No implicit steps.

**PHASE 4 COMPLETE — prototype built: [name the artifact or implementation in one phrase as
the terminal line of this phase before Phase 5 begins]**

---

### PHASE 5 — RESULTS

*EXPERIMENTER. Execute after Phase 4 completion line is present in your output.*

Record what was observed. Compare to what was predicted.

| Element | Value |
|---------|-------|
| **Predicted** | [the value from Phase 3 success condition — what you expected to observe] |
| **Actual** | [what you actually observed; include at least one concrete data point: a number, a count, a time, or a direct quote from output] |
| **Delta** | [predicted − actual; do not leave this for the reader to compute; write "0 — prediction confirmed" if they match] |
| **Why the delta is what it is** | [the explanation for the gap; this is not a restatement of Actual; it is the cause of the difference] |

**PHASE 5 COMPLETE — results recorded: [state the delta in one phrase as the terminal line of
this phase before Phase 6 begins]**

---

### PHASE 6 — COUNTER-EVIDENCE

*EVALUATOR. Execute after Phase 5 completion line is present in your output.*

Determine whether a counter-interpretation of the results exists. Consider the evidence from
Phase 5.

If a counter-interpretation exists:
- **Counter-interpretation**: [state it]
- **Rebuttal**: [explain why it does not hold, using evidence from Phase 5]

If no plausible counter-interpretation exists:
- **Counter-interpretation**: None
- **Reason**: [explain why no alternative reading of the evidence from Phase 5 is plausible]

Write exactly one of the following two lines as the terminal element of this phase, before Phase
7 begins:

A) `PHASE 6 COMPLETE — DISPOSITION A: counter-interpretation named and rebutted`
B) `PHASE 6 COMPLETE — DISPOSITION B: no plausible counter-interpretation — [reason in one phrase]`

---

### PHASE 7 — VERDICT

*EVALUATOR. Execute after Phase 6 completion line is present in your output.*

State the verdict.

| Field | Value |
|-------|-------|
| **Verdict** | Confirmed / Refuted / Inconclusive [choose one] |
| **Verdict rationale** | [the reasoning that connects the observed delta from Phase 5 to the verdict; this is not a restatement of Phase 5; it is the logical step from evidence to conclusion; one to three sentences] |

**PHASE 7 COMPLETE — verdict: [verdict word as the terminal line of this phase before Phase 8
begins]**

---

### PHASE 8 — LIMITATIONS AND NEXT STEP

*EVALUATOR. Execute after Phase 7 completion line is present in your output.*

Name one limitation of this prototype run and one specific next step that follows from the
verdict.

| Field | Value |
|-------|-------|
| **Limitation** | [a specific confound or constraint on interpretation — not a generic disclaimer; must be particular to this prototype run and metric] |
| **Next step** | [a specific action: what to build, test, or change next — "do more research" does not answer this; name the specific thing] |

Write exactly one of the following two lines as the terminal element of this phase, before Phase
9 begins:

A) `PHASE 8 COMPLETE — DISPOSITION A: limitation and next step recorded`
B) `PHASE 8 COMPLETE — DISPOSITION B: [explain what prevented naming a specific limitation or next step, and why]`

---

### PHASE 9 — REPLICATION PATH

*EVALUATOR. Execute after Phase 8 completion line is present in your output.*

List every step needed to reproduce this prototype run. A reader unfamiliar with this work
must be able to replicate it from this section alone without asking clarifying questions.

1. [step 1 — tool, input, command, or configuration; no implicit steps]
2. [step 2]
3. [continue for every step required]

No "etc." No "standard setup." Configuration files named. Environment requirements stated.

Write exactly one of the following two lines as the terminal element of this phase:

A) `PHASE 9 COMPLETE — DISPOSITION A: replication path complete`
B) `PHASE 9 COMPLETE — DISPOSITION B: [name the step that cannot be fully specified and why]`

---

---

## V-02 — Single-axis: Output Format (table-row gate structure)

**Axis**: Output format — gates are embedded as dedicated rows within tables rather than as
inline italic or bold annotations outside tables
**Hypothesis**: Embedding gate labels as named rows inside the table containing the constrained
content makes gate presence auditable by row-scan — the same mechanism that makes missing data
detectable — rather than requiring a separate scan of italicized prose outside the table.

---

You are producing a `prove-prototype` output. The structure below governs what you write and in
what order. Nine sections. Each section opens with a gate row that must appear before the section
body. Each section closes with a completion row. Do not skip sections. Do not merge section
bodies. A missing gate row or completion row is a structural failure.

---

### SECTION 1 — HYPOTHESIS

| Structural element | Content |
|--------------------|---------|
| **[GATE: first element of output — nothing precedes this section]** | *(this row must appear before any body content in this section)* |
| Hypothesis claim | [write the falsifiable claim: what behavior the prototype is expected to demonstrate] |
| Confirmed if | [the observable outcome that confirms the claim] |
| Refuted if | [the observable outcome that refutes the claim] |
| **[SECTION 1 COMPLETE — hypothesis established]** | [restate the hypothesis claim in one phrase] |

---

### SECTION 2 — SCOPE

| Structural element | Content |
|--------------------|---------|
| **[GATE: execute after Section 1 completion row is present]** | *(this row must appear before any body content in this section)* |
| Prototype does | [what the prototype is and does] |
| Exclusion 1 | [item excluded] — *Why test remains valid*: [reason] |
| Exclusion 2 | [item excluded] — *Why test remains valid*: [reason] |
| **[SECTION 2 COMPLETE — scope boundary established]** | [name the prototype in one phrase] |

Minimum two exclusion rows. Each exclusion row includes its test-validity reason in the same row.
"It wasn't needed" does not answer the test-validity question.

---

### SECTION 3 — MEASUREMENT PROTOCOL

| Structural element | Content |
|--------------------|---------|
| **[GATE: execute after Section 2 completion row is present — measurement protocol must be complete before any build content is written]** | *(this row must appear before any body content in this section)* |
| Metric | [what is being measured] |
| Collection method | [how the metric is observed] |
| Success condition | [value or outcome that confirms the hypothesis] |
| Failure condition | [value or outcome that refutes the hypothesis] |
| **[SECTION 3 COMPLETE — measurement protocol frozen before build]** | [metric name and success condition in one phrase] |

No observed values in this section. Measurement plan only.

---

### SECTION 4 — BUILD

| Structural element | Content |
|--------------------|---------|
| **[GATE: execute after Section 3 completion row is present]** | *(this row must appear before any body content in this section)* |
| What was built | [the minimal implementation; no scope expansion beyond Section 2] |
| Tools used | [every tool, library, or system used; no implicit dependencies] |
| Inputs | [every input provided] |
| **[SECTION 4 COMPLETE — prototype built]** | [name the artifact in one phrase] |

---

### SECTION 5 — RESULTS

| Structural element | Content |
|--------------------|---------|
| **[GATE: execute after Section 4 completion row is present]** | *(this row must appear before any body content in this section)* |
| Predicted | [expected value from Section 3 success condition] |
| Actual | [observed value — include at least one concrete data point: number, count, time, or direct quote] |
| Delta | [predicted − actual; "0 — prediction confirmed" if equal; do not leave this for the reader to compute] |
| Why the delta is what it is | [the cause of the gap, co-located in this row] |
| **[SECTION 5 COMPLETE — results recorded]** | [delta stated in one phrase] |

---

### SECTION 6 — COUNTER-EVIDENCE

| Structural element | Content |
|--------------------|---------|
| **[GATE: execute after Section 5 completion row is present]** | *(this row must appear before any body content in this section)* |
| Counter-interpretation | [a plausible alternative reading of Section 5 evidence — OR — "None"] |
| Rebuttal / Reason | [why the counter-interpretation does not hold, using Section 5 evidence — OR — why no plausible counter-interpretation exists] |
| **Disposition [choose one]** | A: counter-interpretation named and rebutted — OR — B: no plausible counter-interpretation; [reason in one phrase] |
| **[SECTION 6 COMPLETE — DISPOSITION A or B selected]** | [state which disposition applies] |

---

### SECTION 7 — VERDICT

| Structural element | Content |
|--------------------|---------|
| **[GATE: execute after Section 6 completion row is present]** | *(this row must appear before any body content in this section)* |
| Verdict | Confirmed / Refuted / Inconclusive [choose one] |
| Verdict rationale | [the reasoning connecting the Section 5 delta to the verdict; not a restatement of Section 5; one to three sentences of logical connection] |
| **[SECTION 7 COMPLETE — verdict rendered]** | [verdict word] |

---

### SECTION 8 — LIMITATIONS AND NEXT STEP

| Structural element | Content |
|--------------------|---------|
| **[GATE: execute after Section 7 completion row is present]** | *(this row must appear before any body content in this section)* |
| Limitation | [one specific confound or constraint particular to this prototype run — not a generic disclaimer] |
| Next step | [one specific action: what to build, test, or change — "do more research" does not pass] |
| **Disposition [choose one]** | A: limitation and next step recorded — OR — B: [explain why a specific limitation or next step cannot be stated] |
| **[SECTION 8 COMPLETE — DISPOSITION A or B selected]** | [state which disposition applies] |

---

### SECTION 9 — REPLICATION PATH

| Structural element | Content |
|--------------------|---------|
| **[GATE: execute after Section 8 completion row is present]** | *(this row must appear before any body content in this section)* |
| Step 1 | [tool, input, command, or configuration — no implicit steps] |
| Step 2 | [continue for every step] |
| ... | |
| **Disposition [choose one]** | A: replication path complete — OR — B: [name the step that cannot be fully specified and why] |
| **[SECTION 9 COMPLETE — DISPOSITION A or B selected]** | [state which disposition applies] |

No "etc." No "standard setup." Configuration files named. Environment requirements explicit.

---

---

## V-03 — Single-axis: Phrasing Register (formal/structural)

**Axis**: Phrasing register — formal structural language ("The following must be established
prior to proceeding") rather than imperative commands ("Execute before") or conversational
register
**Hypothesis**: Formal-structural phrasing makes gate language legible as a compliance
requirement rather than a workflow suggestion, while completion lines written in the same
register create a consistent structural vocabulary throughout the output.

---

This skill produces a `prove-prototype` artifact. The artifact is organized into nine phases.
Each phase carries an opening requirement statement and a closing establishment record. Neither
may be omitted. The establishment record names what was established in the phase; it is not
a declaration that the phase was completed.

---

### PHASE 1 — HYPOTHESIS

*The following must be established before any other phase content is produced: the hypothesis
to be tested. No build description, result, or observation may precede this phase.*

A prototype tests a single falsifiable claim. State the claim before writing any account of
what was built or what happened.

**Hypothesis claim**: [the claim — what behavior or property the prototype is expected to
demonstrate; written as a single testable assertion]

**Confirmed if**: [the observable outcome that would confirm the claim]

**Refuted if**: [the observable outcome that would refute the claim]

*Establishment record — Phase 1: hypothesis [state the claim in one phrase; this record
certifies that the hypothesis was established before any subsequent phase began]*

---

### PHASE 2 — SCOPE

*The following must be established after the Phase 1 establishment record is present: the
prototype boundary. Phase 2 may not be produced until the Phase 1 establishment record
appears in the output.*

The prototype boundary names what was built and what was explicitly excluded. For each
exclusion, the following question must be answered in the same structural unit: without this
exclusion, can the prototype still test the hypothesis? The answer must explain which aspect
of the test the excluded item does not affect.

| Excluded item | Why the hypothesis remains testable without it |
|---------------|------------------------------------------------|
| [item 1] | [explanation — "it wasn't needed" is not an explanation] |
| [item 2] | [explanation] |

Minimum two exclusion rows. Each row answers the test-validity question.

*Establishment record — Phase 2: scope boundary [name the prototype in one phrase; this record
certifies that the scope was established and that each exclusion is paired with a test-validity
explanation]*

---

### PHASE 3 — MEASUREMENT PROTOCOL

*The following must be established after the Phase 2 establishment record is present: the
measurement protocol. Phase 3 must be complete and its establishment record present before
any build content is written. The measurement protocol established here is frozen — it may
not be modified after Phase 3 closes.*

The measurement protocol defines what is measured, how it is collected, and what constitutes
confirmation versus refutation of the hypothesis. These definitions precede construction.

| Metric | Collection method | Confirmation condition | Refutation condition |
|--------|-------------------|----------------------|---------------------|
| [metric name] | [how observed] | [value or outcome that confirms] | [value or outcome that refutes] |

No observed values in this phase. The protocol only.

*Establishment record — Phase 3: measurement protocol frozen — metric: [name the metric],
confirmation condition: [state the success value in one phrase]; this record certifies
that the measurement protocol was established before any build activity*

---

### PHASE 4 — BUILD

*Phase 4 may not be produced until the Phase 3 establishment record is present. The following
must be established in this phase: a description of what was built.*

The build description names the minimal implementation that tests the hypothesis. Every tool,
input, and configuration used is named. No implicit steps. The scope defined in Phase 2
is not expanded here.

**What was built**: [description of the implementation]

**Tools and inputs**: [every tool, library, input, and configuration — no "standard setup"]

*Establishment record — Phase 4: prototype built — [name the artifact in one phrase; this
record certifies that a build description is present and that all tools and inputs are named]*

---

### PHASE 5 — RESULTS

*Phase 5 may not be produced until the Phase 4 establishment record is present. The following
must be established in this phase: the observed result compared to the predicted result.*

The result section reports what was predicted, what was observed, the gap between them, and the
explanation for the gap. Each element is a separate named field in the same structural unit.

**Predicted**: [the value from the Phase 3 confirmation condition — what was expected]

**Actual**: [what was observed; at least one concrete data point must be present — a number,
a count, a time, or a direct quote from output]

**Delta**: [predicted − actual; this field is computed and stated explicitly; the reader does
not compute it; write "0 — prediction confirmed" if predicted and actual are equal]

**Why the delta is what it is**: [the explanation for the gap — not a restatement of Actual;
the cause of the difference, stated in this same structural unit as Delta]

*Establishment record — Phase 5: results recorded — delta: [state the delta in one phrase;
this record certifies that predicted, actual, delta, and explanation are present]*

---

### PHASE 6 — COUNTER-EVIDENCE

*Phase 6 may not be produced until the Phase 5 establishment record is present. The following
must be established in this phase: a determination of whether a counter-interpretation of the
results exists.*

The counter-evidence determination examines whether an alternative reading of the Phase 5
evidence could lead to a different conclusion. This phase closes with exactly one of two
dispositions:

If a counter-interpretation exists:

**Counter-interpretation**: [the alternative reading of the Phase 5 evidence]

**Rebuttal**: [explanation of why the counter-interpretation does not hold, grounded in
Phase 5 evidence]

If no plausible counter-interpretation exists:

**Counter-interpretation**: None

**Reason**: [explanation of why no alternative reading of the Phase 5 evidence is plausible]

The terminal element of Phase 6 is one of the following establishment records — no other
closing form is permitted:

A) *Establishment record — Phase 6: DISPOSITION A — counter-interpretation named and rebutted*
B) *Establishment record — Phase 6: DISPOSITION B — no plausible counter-interpretation;
[state the reason in one phrase]*

---

### PHASE 7 — VERDICT

*Phase 7 may not be produced until the Phase 6 establishment record is present. The following
must be established in this phase: the verdict.*

The verdict states whether the hypothesis is confirmed, refuted, or inconclusive based on the
Phase 5 results.

**Verdict**: Confirmed / Refuted / Inconclusive [choose one]

**Verdict rationale**: [the reasoning that connects the Phase 5 delta to the verdict; this is
not a restatement of Phase 5; it is the logical step from evidence to conclusion; one to three
sentences]

*Establishment record — Phase 7: verdict — [verdict word; this record certifies that a verdict
and rationale are present before Phase 8 begins]*

---

### PHASE 8 — LIMITATIONS AND NEXT STEP

*Phase 8 may not be produced until the Phase 7 establishment record is present. The following
must be established in this phase: one limitation and one next step.*

**Limitation**: [one specific confound or constraint on interpretation — particular to this
prototype run and metric — not a generic disclaimer]

**Next step**: [one specific action that follows from the verdict — what to build, test, or
change; "do more research" does not establish a next step]

The terminal element of Phase 8 is one of the following establishment records — no other
closing form is permitted:

A) *Establishment record — Phase 8: DISPOSITION A — limitation and next step recorded*
B) *Establishment record — Phase 8: DISPOSITION B — [state what prevented naming a specific
limitation or next step, and why]*

---

### PHASE 9 — REPLICATION PATH

*Phase 9 may not be produced until the Phase 8 establishment record is present. The following
must be established in this phase: every step required to reproduce this prototype run.*

A reader unfamiliar with this work must be able to reproduce the prototype run from this phase
alone without requiring clarifying questions. Every tool, input, command, and configuration
is named. No implicit steps. Configuration files named. Environment requirements stated.

1. [step 1]
2. [step 2]
3. [continue for every step required]

The terminal element of Phase 9 is one of the following establishment records — no other
closing form is permitted:

A) *Establishment record — Phase 9: DISPOSITION A — replication path complete*
B) *Establishment record — Phase 9: DISPOSITION B — [name the step that cannot be fully
specified and why]*

---

---

## V-04 — Combined: Lifecycle Emphasis + Inertia Framing

**Axes**:
1. Lifecycle emphasis — three named lifecycle containers (DEFINE / RUN / EVALUATE) group
phases by purpose, making lifecycle-level scope violations detectable at document-structure level
2. Inertia framing — a status-quo baseline (B-00) is declared in Phase 1 alongside the
experimental prediction, carried through Phase 5, and calibrates the verdict in Phase 7

**Hypothesis**: Combining lifecycle containers with a B-00 baseline declared before build
prevents two failure modes simultaneously: (a) lifecycle-scope violations where DEFINE content
appears in RUN phases, and (b) retroactive baseline-setting where the status-quo comparison is
constructed after the experimental result is known.

---

You are producing a `prove-prototype` artifact. The artifact is divided into three lifecycle
containers — DEFINE, RUN, and EVALUATE — and nine phases. Gates and completion lines govern
all nine phases. B-00 is the inertia baseline: what would be observed if no prototype were
built. B-00 is declared in Phase 1 and frozen there. B-00 is read-only in all subsequent
phases.

---

## LIFECYCLE: DEFINE

*Phases 1, 2, and 3. Establish the hypothesis, scope, and measurement protocol before any
build activity. B-00 is declared here. No observed values appear in this lifecycle.*

---

### PHASE 1 — HYPOTHESIS + BASELINE

*Execute before anything else. This phase must appear as the first element of your output.
Nothing precedes it.*

Declare two things: the experimental hypothesis (E) and the inertia baseline (B-00).

**Hypothesis (E)**: [the falsifiable claim — what the prototype is expected to demonstrate]

**Confirmed if**: [the observable outcome that confirms E]

**Refuted if**: [the observable outcome that refutes E]

**Inertia baseline (B-00)**: [what would be observed if no prototype were built — the status
quo outcome; B-00 is frozen here and may not be revised after this phase]

**PHASE 1 COMPLETE — hypothesis and B-00 declared: E = [experimental claim in one phrase],
B-00 = [baseline in one phrase]**

---

### PHASE 2 — SCOPE

*Execute after Phase 1 completion line is present in your output.*

Define the prototype boundary. For each excluded item, state why the hypothesis remains
testable without it.

| Excluded item | Why the hypothesis remains testable without it |
|---------------|------------------------------------------------|
| [item 1]      | [reason] |
| [item 2]      | [reason] |

Minimum two exclusions. "It wasn't needed" does not answer the test-validity question.

**PHASE 2 COMPLETE — scope established: [name the prototype in one phrase]**

---

### PHASE 3 — MEASUREMENT PROTOCOL

*Execute after Phase 2 completion line is present in your output. Measurement protocol must
be complete and this completion line present before Phase 4 begins.*

Define the metric and the thresholds for E (experimental prediction) and B-00 (inertia
prediction). Both predictions are established here before build.

| Metric | Collection method | E (experimental threshold) | B-00 (inertia threshold) | Confirm E | Refute E |
|--------|-------------------|---------------------------|--------------------------|-----------|----------|
| [metric] | [method] | [predicted E value] | [predicted B-00 value] | [condition] | [condition] |

No observed values here. B-00 threshold is declared alongside E threshold.

**PHASE 3 COMPLETE — measurement protocol and B-00 threshold frozen before build:
metric = [name], E = [value], B-00 = [value]**

---

## LIFECYCLE: RUN

*Phases 4 and 5. Build the prototype and record results. The measurement protocol from Phase 3
is inherited unchanged. B-00 threshold is read-only.*

---

### PHASE 4 — BUILD

*Execute after Phase 3 completion line is present in your output.*

Describe what was built. State the minimal implementation. Name every tool, input, and
configuration. No scope expansion. No implicit steps.

**What was built**: [minimal implementation description]

**Tools and inputs**: [every tool, library, input, and configuration]

**PHASE 4 COMPLETE — prototype built: [name the artifact in one phrase]**

---

### PHASE 5 — RESULTS

*Execute after Phase 4 completion line is present in your output.*

Record the observed result. Compare E, B-00, and actual.

| Row | Value |
|-----|-------|
| **E (predicted)** | [Phase 3 experimental threshold] |
| **B-00 (inertia)** | [Phase 3 inertia threshold — read-only, unchanged] |
| **Actual** | [observed value — at least one concrete data point: number, count, time, or direct quote] |
| **E vs. Actual (delta)** | [E − actual; "0 — prediction confirmed" if equal; do not leave for reader to compute] |
| **B-00 vs. Actual** | [B-00 − actual; which direction did actual land relative to the status quo?] |
| **E vs. B-00** | [was the experimental prediction set above or below the inertia baseline?] |
| **Why the delta is what it is** | [cause of E vs. Actual gap — not a restatement of Actual] |

**PHASE 5 COMPLETE — results recorded: E vs. Actual = [delta in one phrase], actual vs.
B-00 = [relationship in one phrase]**

---

## LIFECYCLE: EVALUATE

*Phases 6, 7, 8, and 9. Evaluate evidence. B-00 comparison informs verdict. No build content
in this lifecycle.*

---

### PHASE 6 — COUNTER-EVIDENCE

*Execute after Phase 5 completion line is present in your output.*

Examine the Phase 5 evidence for a plausible counter-interpretation.

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

State the verdict. Address both the experimental result and its relationship to B-00.

| Field | Value |
|-------|-------|
| **Verdict** | Confirmed / Refuted / Inconclusive |
| **Verdict rationale** | [reasoning connecting Phase 5 delta to the verdict — not a restatement of Phase 5] |
| **B-00 calibration** | [did the actual result exceed, match, or fall below B-00? What does this mean for the forward decision — is this a result that could have happened without the prototype?] |

**PHASE 7 COMPLETE — verdict: [verdict word]; B-00 calibration: [above/below/at B-00 in one phrase]**

---

### PHASE 8 — LIMITATIONS AND NEXT STEP

*Execute after Phase 7 completion line is present in your output.*

**Limitation**: [one specific confound or constraint — particular to this run and metric]

**Next step**: [one specific action; "do more research" does not pass; name what to build,
test, or change]

Write exactly one of the following as the terminal element:

A) `PHASE 8 COMPLETE — DISPOSITION A: limitation and next step recorded`
B) `PHASE 8 COMPLETE — DISPOSITION B: [what prevented a specific limitation or next step, and why]`

---

### PHASE 9 — REPLICATION PATH

*Execute after Phase 8 completion line is present in your output.*

Every step to reproduce this prototype run. A reader unfamiliar with this work replicates
from this section alone. No implicit steps. Configuration files named.

1. [step 1]
2. [step 2]
3. [continue]

Write exactly one of the following as the terminal element:

A) `PHASE 9 COMPLETE — DISPOSITION A: replication path complete`
B) `PHASE 9 COMPLETE — DISPOSITION B: [step that cannot be fully specified, and why]`

---

---

## V-05 — Combined: Role Sequence (DESIGNER + ANALYST) + Labeled-Pair Block Format

**Axes**:
1. Role sequence — two sequential roles: DESIGNER (Phases 1–5, defines and executes) and
ANALYST (Phases 6–9, evaluates and records); simpler than a 3-role architecture, tests
whether a 2-role split achieves adjudication isolation
2. Output format — labeled-pair blocks throughout; each pair appears as `**Field name**: value`
in a contiguous block; no tables required; completion lines close every block

**Hypothesis**: A 2-role architecture separating definition+execution (DESIGNER) from
evaluation (ANALYST) produces adjudication isolation structurally verifiable by role-scan,
while labeled-pair blocks provide rationale co-location without table infrastructure —
testing whether the gate-completion line mechanism survives format change.

---

### ROLE DECLARATIONS

*Read before producing any output.*

**DESIGNER** — Governs Phases 1 through 5. DESIGNER establishes the hypothesis, scope,
measurement protocol, and build description, and records the observed results. DESIGNER does
not render a verdict, name limitations, or write an implication. Every DESIGNER phase closes
with a DESIGNER-authored completion line.

**ANALYST** — Governs Phases 6 through 9. ANALYST does not describe build activity. ANALYST
does not restate results. ANALYST's exclusive function is to evaluate the evidence produced
by DESIGNER and record the verdict, counter-evidence determination, limitations, and
replication path. Every ANALYST phase closes with an ANALYST-authored completion line.

---

### PHASE 1 — HYPOTHESIS

*DESIGNER. Execute before anything else. This phase is the first element of your output.*

**Hypothesis**: [the falsifiable claim — what behavior or property the prototype demonstrates]

**Confirmed if**: [observable outcome that confirms the claim]

**Refuted if**: [observable outcome that refutes the claim]

**PHASE 1 COMPLETE — DESIGNER: hypothesis declared — [hypothesis in one phrase]**

---

### PHASE 2 — SCOPE

*DESIGNER. Execute after Phase 1 completion line is present in your output.*

**Prototype boundary**: [what the prototype is and does]

**Exclusion 1**: [item excluded]
**Why test remains valid without it**: [reason — "it wasn't needed" does not answer this]

**Exclusion 2**: [item excluded]
**Why test remains valid without it**: [reason]

*Add additional exclusion pairs if needed. Each exclusion has its test-validity reason in the
same labeled-pair block.*

**PHASE 2 COMPLETE — DESIGNER: scope boundary established — [prototype name in one phrase]**

---

### PHASE 3 — MEASUREMENT PROTOCOL

*DESIGNER. Execute after Phase 2 completion line is present in your output. This phase must
close and its completion line must appear before Phase 4 begins.*

**Metric**: [what is being measured]

**Collection method**: [how the metric is observed]

**Success condition**: [value or outcome that confirms the hypothesis]

**Failure condition**: [value or outcome that refutes the hypothesis]

*No observed values in this phase.*

**PHASE 3 COMPLETE — DESIGNER: measurement protocol frozen before build — metric: [name],
success condition: [value in one phrase]**

---

### PHASE 4 — BUILD

*DESIGNER. Execute after Phase 3 completion line is present in your output.*

**What was built**: [the minimal implementation — no scope expansion beyond Phase 2]

**Tools**: [every tool used — no implicit dependencies]

**Inputs**: [every input provided]

**Configuration**: [every configuration setting relevant to replication]

**PHASE 4 COMPLETE — DESIGNER: prototype built — [artifact name in one phrase]**

---

### PHASE 5 — RESULTS

*DESIGNER. Execute after Phase 4 completion line is present in your output.*

**Predicted**: [the value from Phase 3 success condition — what was expected]

**Actual**: [what was observed; at least one concrete data point: number, count, time, or
direct quote]

**Delta**: [predicted − actual; computed and stated explicitly; "0 — prediction confirmed"
if equal; do not leave for the reader to compute]

**Why the delta is what it is**: [the cause of the gap — not a restatement of Actual; must
appear in the same block as Delta]

**PHASE 5 COMPLETE — DESIGNER: results recorded — delta: [gap in one phrase]**

---

### PHASE 6 — COUNTER-EVIDENCE

*ANALYST. Execute after Phase 5 completion line is present in your output.*

**Counter-interpretation**: [a plausible alternative reading of Phase 5 evidence — OR — None]

**Rebuttal / Reason**: [why the counter-interpretation does not hold, using Phase 5 evidence
— OR — why no plausible counter-interpretation exists; must appear in the same block as
Counter-interpretation]

Write exactly one of the following as the terminal element of Phase 6:

A) **PHASE 6 COMPLETE — ANALYST: DISPOSITION A — counter-interpretation named and rebutted**
B) **PHASE 6 COMPLETE — ANALYST: DISPOSITION B — no plausible counter-interpretation —
[reason in one phrase]**

---

### PHASE 7 — VERDICT

*ANALYST. Execute after Phase 6 completion line is present in your output.*

**Verdict**: Confirmed / Refuted / Inconclusive [choose one]

**Verdict rationale**: [the reasoning connecting the Phase 5 delta to the verdict; not a
restatement of Phase 5; one to three sentences of logical connection; must appear in the
same block as Verdict]

**PHASE 7 COMPLETE — ANALYST: verdict rendered — [verdict word]**

---

### PHASE 8 — LIMITATIONS AND NEXT STEP

*ANALYST. Execute after Phase 7 completion line is present in your output.*

**Limitation**: [one specific confound or constraint particular to this prototype run and
metric — not a generic disclaimer]

**Next step**: [one specific action: what to build, test, or change — "do more research"
does not pass]

Write exactly one of the following as the terminal element of Phase 8:

A) **PHASE 8 COMPLETE — ANALYST: DISPOSITION A — limitation and next step recorded**
B) **PHASE 8 COMPLETE — ANALYST: DISPOSITION B — [what prevented naming a specific
limitation or next step, and why]**

---

### PHASE 9 — REPLICATION PATH

*ANALYST. Execute after Phase 8 completion line is present in your output.*

Every step to reproduce this prototype run. A reader unfamiliar with this work replicates
from this phase alone. No implicit steps. Configuration files named. Environment requirements
stated.

**Step 1**: [tool, input, command, or configuration — no "standard setup"]
**Step 2**: [continue for every step required]

Write exactly one of the following as the terminal element of Phase 9:

A) **PHASE 9 COMPLETE — ANALYST: DISPOSITION A — replication path complete**
B) **PHASE 9 COMPLETE — ANALYST: DISPOSITION B — [step that cannot be fully specified,
and why]**

---

---

## Axis Summary

| Variation | Single/Combined | Primary axis | C-20 mechanism | C-21 coverage |
|-----------|-----------------|--------------|----------------|---------------|
| V-01 | Single | Role sequence (3 roles: DEFINER/EXPERIMENTER/EVALUATOR) | Role-attributed completion lines per phase | All 9 phases; phases 8–9 carry execute-after markers |
| V-02 | Single | Output format (table-row gates) | Completion rows embedded as final row in each section table | All 9 sections; sections 8–9 carry gate rows |
| V-03 | Single | Phrasing register (formal/structural) | "Establishment record" phrasing at every phase close | All 9 phases; phases 8–9 carry "may not be produced until" constraints |
| V-04 | Combined | Lifecycle emphasis + Inertia framing (B-00) | Phase completion lines name B-00 values in phases 1, 3, 5, 7 | All 9 phases across 3 lifecycle containers |
| V-05 | Combined | Role sequence (2 roles: DESIGNER/ANALYST) + Labeled-pair blocks | Role-attributed bold completion lines per phase | All 9 phases; phases 8–9 carry ANALYST execute-after markers |

**C-19 coverage strategy**: V-01 and V-05 use execute-before/after language; V-02 uses
gate rows inside tables; V-03 uses "may not be produced until" formal constraints; V-04 uses
both execute-after and lifecycle container framing. All five cover phases 8 and 9 explicitly.

**C-20 coverage strategy**: V-01 and V-05 attribute completion lines to named roles;
V-02 embeds completion as table rows; V-03 uses "establishment record" naming what was
established; V-04 includes values (E, B-00) in completion lines for structural specificity.

**C-21 test**: All five explicitly gate phases 8 and 9 with inline markers. The trailing-
section gate gap from Round 4 (V-01, V-03, V-05 failed C-19 by scoping gates to
"phases 1–7" only) is closed in every variation here.
