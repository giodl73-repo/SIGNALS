# prove-prototype Variations: V-01 through V-05

---

## V-01 — Variation Axis: Output Format (Table-Dominant)

**Hypothesis**: Tables force cell-by-cell population, eliminating blank sections and making the measurement-before-build temporal order structurally legible without prose enforcement.

---

You are running `/prove:prototype`. Your task is to design, build, and report on the smallest prototype that tests a hypothesis. You must produce exactly the output structure below. Every table cell must be populated. No cell may be left blank or contain a placeholder.

---

### Step 1 — Receive the hypothesis

The user has provided a hypothesis. Restate it verbatim or in a tightened paraphrase as the first line of your output, labeled:

```
**Hypothesis under test**: <restatement>
```

This line must appear before any other content.

---

### Step 2 — Define scope

Produce the following table. You must supply at least two rows (two exclusions). Each row must answer the test-validity question in the third column — "it wasn't needed" does not pass.

| What the prototype includes | What the prototype excludes | Why the test remains valid without the excluded item |
|-----------------------------|-----------------------------|----------------------------------------------------|
| ... | ... | ... |
| ... | ... | ... |

---

### Step 3 — Define measurement (BEFORE building)

Produce the following table. This table must appear in the output before any description of building or results. If you find yourself writing build steps or results before this table exists, stop and complete this table first.

| What to measure | Success condition | Failure condition |
|-----------------|-------------------|-------------------|
| ... | ... | ... |

Then add a single sentence confirming the measurement protocol: "I will measure [metric] by [method] before examining outcomes."

---

### Step 4 — Build

Describe what you built in 2–5 sentences. Include the tools, commands, or steps used. Every tool, input, and command must be named explicitly so someone else can replicate the build from this description alone.

---

### Step 5 — Report results

Produce the following table. The Delta column must be computed explicitly — do not leave it for the reader to infer.

| Metric | Predicted value | Actual value | Delta (predicted − actual) |
|--------|-----------------|--------------|----------------------------|
| ... | ... | ... | ... |

Include at least one concrete data point in the Actual value column (a number, a count, a measured duration, or a direct quote from output).

---

### Step 6 — Verdict

State the verdict in a labeled field:

```
**Verdict**: [confirmed | refuted | inconclusive]
```

Then write a distinct rationale paragraph — at least one sentence — that explains *why* the delta observed supports this verdict. This rationale must be a new explanation, not a restatement of the results table.

---

### Step 7 — Limitations and next step

| Limitation | Next step |
|------------|-----------|
| ... | ... |

One row minimum. The next step must be specific enough to act on in the next session.

---

### Step 8 — Counter-evidence (optional but scored)

If a plausible counter-interpretation exists, name it and rebut it with reasoning grounded in the evidence from Step 5. If no counter-interpretation is plausible, write "No counter-interpretation identified" and state why.

---

**Output contract**: All eight steps must appear in order. No step may be skipped. The Step 3 table must appear before the Step 4 paragraph in the final output.

---

## V-02 — Variation Axis: Phrasing Register (Conversational / Imperative)

**Hypothesis**: A direct second-person imperative voice reduces interpretive latitude — the model follows commands rather than infers intent — which raises pass rates on structural criteria (C-11, C-12) without sacrificing depth criteria.

---

You are building a prototype. Not a plan to build one. Not a description of what a prototype would look like. An actual prototype, right now, from whatever you have in context.

Here is what you will do, in order. Do not skip steps. Do not reorder them.

---

**First: say the hypothesis out loud.**

Whatever hypothesis this prototype is supposed to test — restate it right now, before you write anything else. Put it at the top. Label it "Hypothesis." If you are not sure what the hypothesis is, ask before proceeding.

---

**Second: say what you are NOT building — and why that's fine.**

List at least two things your prototype will leave out. For each one, answer this question: "Does leaving this out mean the test is invalid?" If the answer is yes, you need to add it back in. If the answer is no, write down why not. These are your scope exclusions. They need to pass the test-validity question, not just exist as a list.

---

**Third: decide what "it worked" looks like — before you build.**

Right now, before you write a single line of build output: what would you measure? What number, output, or result would tell you the hypothesis is confirmed? What would tell you it's refuted? Write this down. Label it "Measurement protocol." Do not move on to building until this section exists in your output.

This is the hardest part to get right. The whole point of the prototype is to test the hypothesis against a pre-committed measurement. If you define "worked" after seeing the results, you have not run a test — you have written a story.

---

**Fourth: build it.**

Go. Use the tools, inputs, or commands available. Keep it minimal — only what the measurement protocol requires. Write down every step you take in enough detail that someone else could replicate it: what tool, what input, what command, what you observed.

---

**Fifth: report what happened vs. what you predicted.**

Put your prediction next to your result. Then compute the gap. Don't just show two numbers — name the gap. "I predicted X. I observed Y. The difference is Z." At least one of your results must be a concrete data point: a number, a measured output, a direct quote from what ran.

---

**Sixth: render a verdict.**

Confirmed? Refuted? Inconclusive? Say it plainly. Then explain *why* — one or two sentences that connect the gap you just computed to the verdict. This explanation is not the results again. It is the reasoning that bridges the evidence to the conclusion.

---

**Seventh: name what you learned that limits this result, and what you would do next.**

One limitation. One next step specific enough to act on. Not "do more testing." Something concrete.

---

**Eighth: if there is a reasonable counter-interpretation, address it.**

Could someone argue the result shows the opposite? Name that argument. Then rebut it using the evidence you already have. If there is genuinely no counter-interpretation, say so and say why.

---

**One rule above all**: the measurement protocol (step 3) must appear in your output before the build output (step 4). If you reach step 4 without step 3 written down, go back.

---

## V-03 — Variation Axis: Lifecycle Emphasis (Explicit Phase Gates)

**Hypothesis**: Mandatory go/no-go gate checks between phases force the model to verify completeness of each phase before proceeding, which structurally enforces temporal ordering (C-12) and eliminates skipped sections (C-11) more reliably than instruction text alone.

---

You are running `/prove:prototype`. This skill executes in five phases. Each phase has a gate. You may not enter the next phase until the gate condition for the current phase is satisfied. State the gate outcome explicitly before proceeding.

---

### Phase 1: Anchor

**Purpose**: Establish the hypothesis as the fixed point for all subsequent decisions.

**Task**: Restate the hypothesis being tested. This restatement must be the first substantive element of your output — before scope, before measurements, before any description of building.

**Gate 1**: Does your output so far begin with the hypothesis? If yes, proceed to Phase 2. If no, write the hypothesis now, then proceed.

---

### Phase 2: Scope

**Purpose**: Define the smallest prototype that can test the hypothesis without invalidating the test.

**Task**: State what the prototype includes. Then name at least two items it excludes. For each exclusion, answer the test-validity question: "If I leave this out, does the test still produce a meaningful result?" Your answer to that question must appear next to each exclusion. An exclusion without a test-validity answer does not satisfy this phase.

Separately, state at least one minimality trade-off: something you could have included that you chose not to, and why that choice still permits the hypothesis to be tested.

**Gate 2**: Does your output include (a) the prototype's included scope, (b) at least two exclusions each paired with a test-validity answer, and (c) at least one minimality trade-off? If yes, proceed to Phase 3. If no, complete the missing elements now.

---

### Phase 3: Measure-First

**Purpose**: Commit to measurement criteria before any build output exists. This phase exists entirely to prevent post-hoc retrofitting of success criteria.

**Task**: Define what you will measure, how you will measure it, and what result constitutes confirmation vs. refutation of the hypothesis. Write this as an explicit measurement protocol.

**Constraint**: You may not write any build output — no tools, no commands, no construction steps — until this phase's gate is satisfied. The measurement protocol must precede the build record in the final output.

**Gate 3**: Does your output now contain a measurement protocol with (a) the metric, (b) the success condition, and (c) the failure condition — all stated before any build content? If yes, proceed to Phase 4. If no, complete the measurement protocol now.

---

### Phase 4: Build and Observe

**Purpose**: Execute the prototype and record what happened.

**Task**: Describe what you built. List every tool, input, or command used in sufficient detail for a reader to replicate the steps. Then record your observations. Include at least one concrete data point: a number, a count, a measured duration, or a direct quote from the output.

**Gate 4**: Does your output include (a) a build description with named tools/steps and (b) at least one concrete measurement result? If yes, proceed to Phase 5. If no, supply the missing content now.

---

### Phase 5: Analyze and Report

**Purpose**: Compare results against the pre-committed measurement protocol, render a verdict, and close the loop.

**Task — in this exact order**:

1. **Delta**: State the predicted value from Phase 3 and the observed value from Phase 4. Compute the gap as a labeled element. The reader must not have to subtract these numbers themselves.

2. **Verdict**: State whether the hypothesis is confirmed, refuted, or inconclusive.

3. **Rationale**: Write a distinct rationale passage — separate from the results — that explains *why* the delta supports the verdict. This is not a restatement of the data; it is reasoning.

4. **Limitations and next step**: Name one limitation of this prototype and one specific next step.

5. **Counter-evidence** (optional but scored): Identify a plausible counter-interpretation and rebut it using the evidence.

**Gate 5**: Does your output include all five elements above? If yes, output is complete. If no, supply the missing elements.

---

**Phase ordering is mandatory**. The output must reflect this sequence: Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5. Phase 3 content (measurement protocol) must precede Phase 4 content (build) in the literal output.

---

## V-04 — Variation Axes: Role Sequence + Output Format (Combined)

**Hypothesis**: Separating concerns across three named roles — one that owns the hypothesis and verdict, one that owns scope and validity, one that owns evidence and measurement — reduces the chance that any single concern is skipped, because the role boundary makes omission visible.

---

You are running `/prove:prototype`. This skill coordinates three roles in sequence. Each role produces a named artifact. The roles are not optional. Run them in order.

---

### Role 1: Hypothesis Keeper

**Responsibility**: Own the hypothesis and the verdict. The Hypothesis Keeper opens the output and closes it.

**Opening task** — produce this block at the top of the output:

```
=== HYPOTHESIS KEEPER: OPEN ===
Hypothesis under test: <restatement>
Prediction: <what you expect to observe if the hypothesis is true>
=== END OPEN ===
```

The hypothesis restatement must be the first content in the output. The prediction must be an observable claim — something that can be compared against actual results.

**Closing task** — after all other roles have completed, produce this block:

```
=== HYPOTHESIS KEEPER: CLOSE ===
Predicted: <value from OPEN>
Observed: <value from Role 3>
Delta: <computed gap>
Verdict: [confirmed | refuted | inconclusive]
Rationale: <one or more sentences explaining why the delta supports this verdict — not a restatement of the data>
=== END CLOSE ===
```

The Hypothesis Keeper's CLOSE block must appear after Role 3's output in the final document.

---

### Role 2: Scope Referee

**Responsibility**: Define the prototype's boundary and certify that the boundary does not invalidate the test.

**Task** — produce this block immediately after the Hypothesis Keeper's OPEN:

```
=== SCOPE REFEREE ===
Prototype includes:
  - <item>
  - <item>

Prototype excludes:
  - <item> → test-validity: <why the test remains valid without this>
  - <item> → test-validity: <why the test remains valid without this>

Minimality trade-off: <one item that could have been included and was not, and why its omission is acceptable>
=== END SCOPE REFEREE ===
```

Rules:
- At least two inclusions
- At least two exclusions; each must answer the test-validity question with a substantive reason, not a label
- One minimality trade-off stated explicitly

---

### Role 3: Evidence Recorder

**Responsibility**: Define measurement, record the build, and report raw evidence.

**Task** — produce this block after the Scope Referee's output:

```
=== EVIDENCE RECORDER ===

[MEASUREMENT PROTOCOL — defined before build]
Metric: <what is being measured>
Success condition: <what result confirms the hypothesis>
Failure condition: <what result refutes the hypothesis>
Method: <how measurement will be taken>

[BUILD RECORD]
Steps taken:
  1. <tool / command / input>
  2. <tool / command / input>
  ...

[OBSERVATIONS]
Raw result: <at least one concrete data point — number, count, duration, or direct quote>
Additional observations: <any other relevant data>

[LIMITATIONS AND NEXT STEP]
Limitation: <one specific limitation of this prototype>
Next step: <one specific actionable next step>

[COUNTER-EVIDENCE]
Counter-interpretation: <a plausible alternative reading of the results, or "none identified">
Rebuttal: <reasoning grounded in the evidence above>
=== END EVIDENCE RECORDER ===
```

**Constraint**: The MEASUREMENT PROTOCOL section must precede the BUILD RECORD section within this block. Do not write build steps before the measurement protocol is written.

---

### Role execution order

1. Hypothesis Keeper OPEN
2. Scope Referee
3. Evidence Recorder
4. Hypothesis Keeper CLOSE

The output must contain all four blocks in this sequence. No block may be omitted or left partially populated. Every labeled field must contain substantive content.

---

## V-05 — Variation Axes: Inertia Framing + Lifecycle Emphasis (Combined)

**Hypothesis**: Anchoring the prototype against an explicit status-quo alternative sharpens scope decisions (what to exclude and why) and makes the verdict more consequential — because the reader understands what they would do instead if the hypothesis is refuted.

---

You are running `/prove:prototype`. Before you build anything, you must understand what the status quo is — what someone would do today, without this prototype. Every decision you make about scope, measurement, and verdict should be made against that baseline.

---

### Stage 0: Status Quo Anchor

Start by naming the status-quo alternative. This is the thing someone does *instead* — the current workaround, the existing approach, the tool already in use.

Write:
```
Status quo: <what is done today instead of the approach this prototype tests>
Cost of status quo: <what it costs — time, error rate, friction, capability gap>
```

This anchor will inform your scope decisions (Stage 2) and your verdict interpretation (Stage 5). Keep it visible.

---

### Stage 1: Hypothesis Restatement

Restate the hypothesis under test. This must be the first substantive element of the output after the status quo anchor.

The hypothesis should be stated in a form that predicts something measurable: "If we [do X], then [Y] will happen." Vague hypotheses are not testable; if the hypothesis is vague, tighten it before proceeding.

---

### Stage 2: Scope — What This Prototype Is and Is Not

Define the prototype's boundary. Your scope decisions should be made in light of the status quo: you only need to build enough to test whether the approach beats the baseline on the dimension that matters.

Required elements:

**Included**: What the prototype does.

**Excluded**: At least two items the prototype does not do. For each:
- Name the exclusion
- Answer: "Does this omission mean the test can't tell us whether we beat the status quo?" If yes — add it back. If no — explain why not.
- This is the test-validity question. Each exclusion must answer it with substantive reasoning.

**Minimality trade-off**: Name one thing you chose not to include that you could have included, and explain why leaving it out keeps the test valid.

---

### Stage 3: Measurement Protocol (Committed Before Building)

This stage must be completed before any build output is written. Its purpose is to prevent you from defining "success" after you already know the outcome.

Define:
- **Metric**: What you will measure
- **Success condition**: The result that would confirm the hypothesis
- **Failure condition**: The result that would refute it
- **Baseline**: What the status quo scores on this same metric (if known; estimate if not)

Write the full measurement protocol now. Do not proceed to Stage 4 until this section is complete in your output.

---

### Stage 4: Build and Observe

Build the prototype. Keep it minimal — only what Stage 3 requires you to measure.

Record:
- Every tool, command, or input used (in enough detail for replication)
- What happened — including at least one concrete data point (number, count, duration, direct quote)
- Any surprising or unexpected observations

---

### Stage 5: Results and Verdict

**Delta table** — do not leave this computation to the reader:

| Dimension | Predicted | Actual | Delta |
|-----------|-----------|--------|-------|
| [metric from Stage 3] | [value] | [value] | [computed gap] |
| vs. status quo | [baseline from Stage 3] | [actual] | [gap vs. baseline] |

**Verdict**: Confirmed / Refuted / Inconclusive — state it plainly.

**Rationale**: Explain in at least one sentence *why* the delta supports the verdict. This is not the results again — it is the reasoning. Connect the observed delta to the hypothesis and, where relevant, to the status quo baseline.

**Inertia implication**: Given the verdict, what should someone do about the status quo? Should they keep it, replace it, or run a larger test? One sentence.

---

### Stage 6: Limitations, Next Step, Counter-Evidence

**Limitation**: One specific limitation of this prototype — why the result might not generalize.

**Next step**: One concrete action the reader can take in the next session. Not "do more testing." Something specific enough to schedule.

**Counter-interpretation**: Could the result be explained differently? Name the alternative reading. Rebut it using the evidence from Stage 4. If no counter-interpretation exists, state why.

---

**Output order is enforced**: Stage 0 → Stage 1 → Stage 2 → Stage 3 → Stage 4 → Stage 5 → Stage 6. Stage 3 (measurement protocol) must appear before Stage 4 (build) in the literal output. No stage may be omitted or left with placeholder content.

---

## Variation Summary

| Variation | Primary Axis | Secondary Axis | Key Structural Bet |
|-----------|-------------|----------------|--------------------|
| V-01 | Output format (tables) | — | Tables force cell-by-cell population; delta column enforces C-13 |
| V-02 | Phrasing register (conversational/imperative) | — | Direct commands reduce interpretive latitude on C-11, C-12 |
| V-03 | Lifecycle emphasis (phase gates) | — | Explicit go/no-go gates enforce temporal ordering structurally |
| V-04 | Role sequence | Output format (role blocks) | Named role ownership makes omission visible at block level |
| V-05 | Inertia framing | Lifecycle emphasis | Status-quo anchor sharpens scope exclusion reasoning (C-15) |
