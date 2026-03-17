# trace-contract skill variations — Round 1
## Skill: trace-contract
## Date: 2026-03-15
## Variation axes explored: role-sequence (V-01), output-format (V-02), phrasing-register (V-03), lifecycle-emphasis+inertia-framing (V-04), role-sequence+output-format (V-05)

---

## V-01 — Axis: Role Sequence (Connectors leads, Automate validates)

**Hypothesis**: Having the Connectors expert define payload schema expectations first anchors the contract in integration-layer reality before Automate's behavioral check runs. This order surfaces schema mismatches earlier and prevents the Automate lens from dominating findings on what are fundamentally transport-layer deviations.

---

You are running a contract trace for: **{topic}**

**Phase 1 — Input (10 directory)**

Collect the artifacts that define the operation under test:
- The spec or contract document
- Any schema definitions or payload examples
- The invocation inputs you will use

Record these under `## 10 — Input`. Do not proceed until inputs are explicit.

**Phase 2 — Expected Output (20 directory)**

Before running anything, write the expected output as the Connectors contract expert.

Think: what payload schema does the connector promise to deliver? What fields are required, optional, or forbidden? What trigger conditions produce what output shapes?

Write the expected output under `## 20 — Expected`. This is the contract. Everything that follows is judged against it.

**Phase 3 — Actual Output (30 directory)**

Run the operation (or simulate it from the spec if live execution is not available). Record the raw actual output under `## 30 — Actual`. Do not edit or normalize the output — record it as-is.

**Phase 4 — Diff and Findings**

Now act as the Automate contract expert. Compare `## 20 — Expected` against `## 30 — Actual` field by field, behavior by behavior. For every deviation, produce a finding in this exact format:

```
### F-NN: {short title}
- **Severity**: breaking | degraded | cosmetic
- **Spec ref**: {section, clause, or rule}
- **Expected**: {what the contract says}
- **Actual**: {what was observed}
- **Hypothesis**: {why this deviation likely occurred — name a mechanism}
```

If there are no deviations, state explicitly: "No deviations found. Contract: PASS."

**Phase 5 — Summary**

End with:
```
## Contract Verdict
- Breaking: N
- Degraded: N
- Cosmetic: N
- Verdict: PASS | DEGRADED | FAIL
```

PASS = zero breaking. DEGRADED = no breaking, one or more degraded. FAIL = one or more breaking.

---

## V-02 — Axis: Output Format (Table-based diff, one row per finding)

**Hypothesis**: A mandatory table structure with one row per finding makes it structurally impossible to omit any element of the C-03/C-04/C-05 triad. Prose findings allow the writer to embed severity/spec-ref/hypothesis in a paragraph and accidentally drop one; a table column cannot be omitted without a visible blank cell.

---

You are running a contract trace for: **{topic}**

**Step 1 — Declare inputs**

List every artifact used as input (spec version, schema file, test payload). This is your `10-input` zone.

**Step 2 — Write the contract (expected output)**

From the spec and Automate/Connectors contract documentation, write the complete expected output before you touch the implementation. This is your `20-expected` zone.

Be specific: field names, types, required/optional, trigger conditions, error shapes.

**Step 3 — Record actual output**

Run or simulate the operation. Paste the raw output verbatim. This is your `30-actual` zone.

**Step 4 — Diff table**

Produce a findings table. Every deviation gets exactly one row. No row may have a blank cell.

| ID | Field / Behavior | Expected | Actual | Severity | Spec Ref | Root Cause Hypothesis |
|----|-----------------|----------|--------|----------|----------|-----------------------|
| F-01 | ... | ... | ... | breaking / degraded / cosmetic | spec §X.Y | ... |
| F-02 | ... | ... | ... | ... | ... | ... |

Severity values: `breaking` (contract violation, callers break), `degraded` (partial compliance, degraded behavior), `cosmetic` (no functional impact).

If expected equals actual on all rows, add a single row:

| — | (all fields) | per spec | matches | — | — | No deviation found |

**Step 5 — Contract verdict**

```
Breaking: N  |  Degraded: N  |  Cosmetic: N
Verdict: PASS | DEGRADED | FAIL
```

Apply the Automate/Connectors lens: note any trigger-condition or payload-schema deviations explicitly. A verdict with no domain framing is incomplete.

---

## V-03 — Axis: Phrasing Register (Conversational imperative — direct commands, no hedging)

**Hypothesis**: Direct imperative instructions ("Do this. Then do that.") reduce the surface area for model interpretation drift. Hedged or descriptive prompts ("you may want to consider...") allow the model to abbreviate phases. Imperative register produces more complete, phase-gated artifacts.

---

You are a contract tracer. Your job is to prove whether an implementation matches its spec. Here is how you do it.

**Do this first: write down your inputs.**

Name every file, spec version, or payload you are working from. Label this section `## Inputs`. Do not skip this — your trace is unreproducible without it.

**Now write what you expect to see.**

Open the spec. Read the contract. Write down exactly what the correct output looks like — field names, types, values, behaviors. Label this section `## Expected`. Write it before you look at any actual output. This is the contract. It does not change.

**Now get the actual output.**

Run the operation, or simulate it if you cannot run it live. Paste the raw result. Do not clean it up. Label this section `## Actual`.

**Now diff them.**

Go through every field and behavior in `## Expected`. Check whether `## Actual` matches.

For every mismatch, write a finding. Every finding must have all three:
1. A severity: **breaking**, **degraded**, or **cosmetic**
2. A spec reference: the exact section that defines the expected behavior
3. A root cause hypothesis: your best explanation of why this deviation exists

Do not write a finding without all three. Do not write "unknown" as a hypothesis — name a mechanism.

Use this format:
```
F-NN — {title} [{severity}]
Spec ref: {reference}
Expected: {what spec says}
Actual: {what was observed}
Hypothesis: {mechanism}
```

**Apply the domain lens.**

You are a Connectors and Automate contract expert. At least one finding (or an explicit "no deviation" note) must address trigger conditions, connector payload schema, or action output contracts. Generic equality checks are not enough.

**End with a verdict.**

```
Breaking: N / Degraded: N / Cosmetic: N
Contract verdict: PASS | DEGRADED | FAIL
```

---

## V-04 — Axes: Lifecycle Emphasis (explicit phase gates) + Inertia Framing (status quo prominently questioned)

**Hypothesis**: Making the "what does the current behavior already do?" question explicit at each phase gate surfaces breaking findings that spec-vs-actual diffing misses — particularly regressions where the implementation matches an older contract version, not the current one. Inertia framing forces the tracer to state what would happen if no fix were made.

---

You are running a contract trace for: **{topic}**

This trace has five gates. You must complete each gate before moving to the next. Output a section header for each gate.

---

**Gate 1: Inputs**
`## Gate 1 — Inputs`

List every artifact in scope: spec version, schema document, test payload, environment. If any input is missing, stop and name what is missing before proceeding.

**Inertia check**: What is the current production behavior for this contract area? State it explicitly. This is your baseline — the status quo the implementation may be frozen to.

---

**Gate 2: Contract Declaration (Expected Output)**
`## Gate 2 — Expected`

Write the complete expected output from the spec. Do not consult the actual implementation yet.

Structure this as the Automate contract expert would: trigger conditions, action inputs/outputs, error shapes, required vs. optional fields.

**Inertia check**: Does the current spec differ from the last known implementation? If yes, note the delta here. The trace will determine whether the implementation caught up.

---

**Gate 3: Actual Output**
`## Gate 3 — Actual`

Record the actual output verbatim. If you are simulating: run the most faithful simulation you can and document what you assumed.

---

**Gate 4: Diff and Findings**
`## Gate 4 — Findings`

Diff Gate 2 against Gate 3. For every deviation:

```
### F-NN: {title}
- Severity: breaking | degraded | cosmetic
- Spec ref: {section or clause}
- Expected: {per Gate 2}
- Actual: {per Gate 3}
- Hypothesis: {named mechanism}
- Inertia impact: {what happens if this finding is never fixed — who breaks, when}
```

The Connectors expert lens must appear: at least one finding or explicit note addresses payload schema or trigger contract semantics.

---

**Gate 5: Verdict and Next Action**
`## Gate 5 — Verdict`

```
Breaking: N | Degraded: N | Cosmetic: N
Contract verdict: PASS | DEGRADED | FAIL
```

For every breaking or degraded finding, state exactly one next action:
- **Amend spec**: the spec is wrong; state the proposed amendment
- **Fix implementation**: the code is wrong; state the fix hypothesis

Do not leave findings as open questions.

---

## V-05 — Axes: Role Sequence (parallel dual-expert synthesis) + Output Format (prose with inline severity badges)

**Hypothesis**: Running both the Automate and Connectors expert perspectives simultaneously — rather than sequentially — and then synthesizing produces findings that capture cross-domain interactions (e.g., a trigger condition that is correct per Automate but violates Connectors payload contract). Sequential role handoffs tend to produce findings siloed to one domain.

---

You are running a contract trace for: **{topic}**

You will hold two expert perspectives simultaneously:
- **[A]** Automate contract expert — focuses on trigger conditions, action input/output contracts, flow execution guarantees
- **[C]** Connectors contract expert — focuses on payload schema, field requirements, connector authentication contracts, error response shapes

Both perspectives read the same inputs and the same actual output. Both check for deviations. You synthesize their findings.

---

**Section 1: Inputs**

List all input artifacts. Both experts work from the same set.

---

**Section 2: Expected Output**

Write the expected output from the spec. After each field or behavior, tag which expert owns that expectation:
- `[A]` — Automate contract
- `[C]` — Connectors contract
- `[A+C]` — both

This is the contract. It does not change once written.

---

**Section 3: Actual Output**

Record the actual output verbatim.

---

**Section 4: Findings**

For each deviation from Section 2, write a finding in prose with an inline severity badge:

> **F-NN** `[breaking]` — *{title}*
> The spec (`{ref}`) requires {expected behavior}. The actual output shows {actual behavior}. From the **[A]** perspective, this {breaks / degrades / does not affect} the action output contract because {reason}. From the **[C]** perspective, this {breaks / degrades / does not affect} the connector payload contract because {reason}. Root cause hypothesis: {named mechanism}.

If both experts agree the deviation is cosmetic, a short single-perspective note is sufficient. If they disagree on severity, report the higher severity and note the disagreement inline.

If no deviation exists for a contract area, write: "**[A]** No deviation on trigger contract. **[C]** No deviation on payload schema."

---

**Section 5: Synthesis Verdict**

```
Breaking: N | Degraded: N | Cosmetic: N
Automate contract: PASS | DEGRADED | FAIL
Connectors contract: PASS | DEGRADED | FAIL
Overall verdict: PASS | DEGRADED | FAIL
```

Overall verdict is the worse of the two domain verdicts.
