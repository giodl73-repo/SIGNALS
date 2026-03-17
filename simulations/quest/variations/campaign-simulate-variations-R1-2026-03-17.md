Now I have the baseline skill body, rubric, and sub-skill catalog. Generating all five variations.

---

# `campaign-simulate` — Quest Variate R1

Five complete, runnable prompt body variations. Single-axis first (V-01 through V-04), combination last (V-05).

---

## V-01 — Axis: Role Sequence (trace-first)

**Hypothesis**: Running the platform-layer trace skills (state, contract, permissions) *before* the domain flow skills surfaces contract violations and state machine anomalies with more precision — the flow sims can then reference known violations as context rather than discovering them redundantly.

```
Simulate the technical behavior of: {{topic}}

You are running the pre-implementation simulation campaign. The goal is a
single ranked findings report that tells implementors what breaks before they
write a line of code. Do not produce five separate outputs — produce one
synthesized document.

Run all five sub-skills in this order. Each produces findings that feed the next:

**Phase 1 — Platform mechanics first**

1. **trace-state** — Hand-compile every state transition for {{topic}}.
   For each transition: precondition, postcondition, invariant check.
   Flag unreachable states, invalid transitions, missing guards.

2. **trace-contract** — Using the three-directory pattern (input / expected /
   actual), verify the spec contract for {{topic}}. Surface every expected-vs-
   actual mismatch with severity: CRITICAL / HIGH / MEDIUM / LOW.

3. **trace-permissions** — Walk the permission model for {{topic}}.
   Every actor, every action, every guard. Flag privilege escalation paths
   and missing deny conditions.

**Phase 2 — Domain flows, informed by Phase 1 findings**

4. **flow-lifecycle** — Trace the complete business process lifecycle.
   Phase contracts, exception flows, and dead-end states. Reference any
   state machine anomalies or contract violations found in Phase 1.

5. **flow-conversation** — Simulate multi-turn conversational flows.
   Include at least one exception path (dead-end, loop risk, or failed
   branch) per topic area.

**Synthesis**

Collect all findings across all five sub-skills. Assign each finding:
- An F-NN identifier
- The sub-skill that surfaced it (e.g., [trace-state])
- The system boundary where it was detected
- A severity: CRITICAL / HIGH / MEDIUM / LOW
- A blast radius: what is the scope of impact if this is not fixed?

Rank the final findings list by blast radius (highest first).

Write the synthesized report to:
  simulations/{{topic}}/simulate-{{date}}.md

The report must include:
1. Findings table (ranked, with F-NN, sub-skill, boundary, severity, blast radius)
2. Spec gaps and contract violations section (any finding classified as missing
   precondition, underspecified behavior, or expected/actual mismatch)
3. State machine anomalies section (sourced from trace-state)
4. Test scenario baseline — one named scenario per HIGH or CRITICAL finding
```

---

## V-02 — Axis: Output Format (table-first, mandatory columns)

**Hypothesis**: A mandatory findings table with explicit column definitions forces every finding to carry boundary + severity labels (C-03 pass) and eliminates the most common failure mode — findings without attribution.

```
Simulate the technical behavior of: {{topic}}

Run the full simulation campaign across five sub-skills. Your output is one
synthesized report — not a concatenation of five sub-outputs.

**Sub-skills to run (in any order, all five required):**
- flow-lifecycle
- flow-conversation
- trace-state
- trace-contract
- trace-permissions

For each sub-skill: read the spec and design artifacts for {{topic}}, run
the simulation, and collect findings. Every finding must be captured in the
findings table below.

---

**Required output structure:**

### Findings Table

| F-ID | Sub-Skill | System Boundary | Severity | Blast Radius | Finding Summary |
|------|-----------|-----------------|----------|--------------|-----------------|
| F-01 | [trace-state] | state machine | HIGH | ... | ... |
| ... | ... | ... | ... | ... | ... |

Rules:
- Every row must have all six columns filled. No blank cells.
- Severity: CRITICAL / HIGH / MEDIUM / LOW
- Blast Radius: scope description (e.g., "all permission checks", "single flow branch")
- Rows sorted by Blast Radius descending (CRITICAL first, LOW last)
- Minimum: 1 finding from each of the five sub-skills

### Spec Gaps and Contract Violations

List every finding classified as:
- Missing precondition or postcondition
- Underspecified behavior (what happens when X is undefined?)
- Expected vs. actual mismatch from trace-contract

At least one is required. If none are found, that is itself a finding — explain why.

### State Machine Anomalies

From trace-state specifically: unreachable states, invalid transitions,
invariant violations, missing guards. "No anomalies" is valid only with rationale.

### Exception Paths

At least two exception flows identified across the campaign:
dead-ends, loop risks, failed branches, or out-of-sequence events.

### Test Scenario Baseline

Derive one named test scenario per HIGH or CRITICAL finding.
Format:
  - **TS-NN** (links to F-NN): [scenario name] — what to exercise, expected pass condition

---

Write the final report to:
  simulations/{{topic}}/simulate-{{date}}.md
```

---

## V-03 — Axis: Lifecycle Emphasis (explicit exception budgets per sub-skill)

**Hypothesis**: Giving each sub-skill an explicit "exception budget" — a named obligation to find at least one non-happy-path case — increases C-06 pass rate and makes edge cases first-class rather than afterthoughts.

```
Simulate the technical behavior of: {{topic}}

This is the pre-implementation simulation campaign. You are hunting for what
breaks, not confirming what works. Every sub-skill has a happy-path component
AND an exception budget — both must be satisfied.

Run all five sub-skills. Do not skip any. Produce one unified findings report.

---

**1. flow-lifecycle** — Business process lifecycle

Happy path: trace each phase of the lifecycle from initiation to completion.
Identify phase contracts (entry condition, work done, exit condition).

Exception budget (required):
- At least one lifecycle exception: what happens if a phase is entered without
  meeting its entry condition?
- At least one dead-end: a state from which the process cannot progress.
- At least one rollback or compensating path.

---

**2. flow-conversation** — Multi-turn conversational flows

Happy path: trace the canonical conversation from opening to resolution.
Map each turn: intent, expected response, state change.

Exception budget (required):
- At least one dead-end turn: where does the conversation break down?
- At least one loop risk: where might the conversation cycle without progress?
- At least one failed branch: an intent that the system cannot handle.

---

**3. trace-state** — State machine transitions

Happy path: enumerate all valid states and transitions for {{topic}}.
For each transition: precondition → action → postcondition → invariant check.

Exception budget (required):
- At least one unreachable state (exists in spec, cannot be entered).
- At least one invalid transition (allowed by spec but breaks an invariant).
- At least one missing guard (transition possible without a required check).

---

**4. trace-contract** — Spec contract verification

Happy path: for each contract surface, compare expected output to spec-defined
actual output. Confirm or disconfirm.

Exception budget (required):
- At least one CRITICAL or HIGH mismatch between expected and actual.
- At least one underspecified behavior (input defined, output undefined or ambiguous).

---

**5. trace-permissions** — Permission model walk-through

Happy path: confirm that each actor can perform their authorized actions.

Exception budget (required):
- At least one privilege escalation path (actor reaches resource without
  explicit grant).
- At least one missing deny (action not permitted but not explicitly blocked).

---

**Synthesis**

Combine all findings from all five sub-skills into one document.
Label each finding with:
- F-NN identifier
- Source sub-skill in brackets: [flow-lifecycle], [trace-state], etc.
- System boundary
- Severity: CRITICAL / HIGH / MEDIUM / LOW
- Blast radius (scope of impact)

Sort findings by blast radius, highest first.

Highlight:
- All spec gaps and contract violations in a dedicated section
- State machine anomalies from trace-state in a dedicated section

Write to: simulations/{{topic}}/simulate-{{date}}.md
```

---

## V-04 — Axis: Phrasing Register (descriptive / intent-first)

**Hypothesis**: Describing the purpose and intent of each sub-skill in first-person outcome language ("your job is to find X") reduces silent skipping — the model understands *why* it is running each sub-skill, not just *that* it should.

```
Simulate the technical behavior of: {{topic}}

Your job is to act as a simulation analyst running a pre-implementation
technical audit. You will exercise five distinct simulation lenses against
{{topic}} and then synthesize everything into a single findings report that
a developer can act on.

The reason this campaign exists: writing code against an unexamined spec is
how you discover broken contracts and missing states in production. This
campaign finds them now.

---

**What you're doing for each sub-skill:**

With **flow-lifecycle**, your job is to walk the business document or process
lifecycle for {{topic}} from start to finish — including every phase boundary,
every exception that could derail progression, and every dead-end state. You
want to know: where does this process break?

With **flow-conversation**, your job is to simulate how a multi-turn
conversation about {{topic}} plays out — tracing each exchange, identifying
where conversations dead-end, where they loop, and where the system fails to
handle a turn gracefully.

With **trace-state**, your job is to hand-compile the state machine for
{{topic}} — every state, every transition, every precondition and
postcondition. You want anomalies: states that can't be reached, transitions
that violate invariants, guards that are missing.

With **trace-contract**, your job is to verify that the spec says what it
means. For each contract surface, ask: if I implement exactly what the spec
says, do I get what it promises? Surface every mismatch between expected and
actual, especially where behavior is undefined or ambiguous.

With **trace-permissions**, your job is to walk the permission model and find
the holes. Who can do what? Are there paths to privileged resources that don't
require explicit grants? Are there actions not covered by any deny rule?

---

**What you're producing:**

One document — not five sub-outputs concatenated. The document should read as
if a senior engineer synthesized all five simulation passes into a coherent
risk assessment.

Structure:
- **Ranked findings list** — sorted by blast radius (widest impact first).
  Every finding: an F-NN ID, the sub-skill that found it in brackets, the
  system boundary it lives in, a severity (CRITICAL / HIGH / MEDIUM / LOW),
  and a one-line blast radius statement.
- **Spec gaps and contract violations** — a separate callout for findings
  that require a spec change before implementation can proceed.
- **State machine anomalies** — a separate callout for trace-state findings
  specifically.
- **Exception paths found** — a brief summary of all non-happy-path flows
  discovered (at least two across the campaign).

Write the final report to:
  simulations/{{topic}}/simulate-{{date}}.md
```

---

## V-05 — Axis: Combination (trace-first sequence + mandatory table format + explicit exception budgets)

**Hypothesis**: Combining three single-axis strengths — trace-first ordering (V-01), mandatory column-enforced table (V-02), and per-sub-skill exception budgets (V-03) — achieves reliable C-01–C-05 coverage AND pushes into C-09/C-10 by making F-NN IDs and scenario derivation structural requirements rather than optional aspirations.

```
Simulate the technical behavior of: {{topic}}

Run the pre-implementation simulation campaign. Output: one synthesized
findings report. Do not concatenate five sub-outputs — synthesize them.

All five sub-skills are required. Missing any one sub-skill = invalid output.

---

**Execution sequence**

Run platform-layer skills first so their findings inform the domain-flow sims:

**Round 1 — Platform mechanics**

1. **trace-state** — Enumerate all states and transitions for {{topic}}.
   Per transition: precondition, action, postcondition, invariant.
   Exception budget: at least one unreachable state, one invalid transition,
   one missing guard.

2. **trace-contract** — Apply the three-directory pattern against the spec.
   For each contract surface: expected vs. actual, severity rating.
   Exception budget: at least one CRITICAL or HIGH mismatch, at least one
   underspecified behavior.

3. **trace-permissions** — Walk every actor/action/resource path.
   Exception budget: at least one privilege escalation path, one missing deny.

**Round 2 — Domain flows (reference Round 1 findings)**

4. **flow-lifecycle** — Trace the full business process lifecycle.
   Reference any state anomalies or contract violations from Round 1.
   Exception budget: at least one failed phase entry, one dead-end state,
   one rollback path.

5. **flow-conversation** — Simulate multi-turn conversational flows.
   Exception budget: at least one dead-end turn, one loop risk.

---

**Findings collection**

As you complete each sub-skill, add its findings to the master findings table.
Assign IDs incrementally across all sub-skills (F-01, F-02, ...).

**Master Findings Table** (mandatory — no finding exists outside this table):

| F-ID | Sub-Skill | System Boundary | Severity | Blast Radius | Summary |
|------|-----------|-----------------|----------|--------------|---------|
| F-01 | [trace-state] | state machine | HIGH | ... | ... |

Rules:
- All six columns required per row. No blank cells.
- Severity: CRITICAL / HIGH / MEDIUM / LOW
- Blast Radius: scope statement (not just a word — a phrase)
- Sort: CRITICAL first, then HIGH, MEDIUM, LOW

---

**Synthesis sections (required after the table)**

**Spec Gaps and Contract Violations**
Every finding where behavior is underspecified or expected/actual mismatches.
At least one is required. State explicitly if none found and explain why.

**State Machine Anomalies**
Findings from trace-state only. Every unreachable state, invalid transition,
and missing guard found in Round 1.

**Exception Paths Inventory**
Every non-happy-path flow found across all five sub-skills. Minimum two.
Name each one: what sub-skill found it, what triggers it, what breaks.

**Test Scenario Baseline**
Derive one named test scenario per CRITICAL or HIGH finding.
Format:
  TS-NN (from F-NN): [scenario name] — input condition, action, expected pass condition

---

Write the complete report to:
  simulations/{{topic}}/simulate-{{date}}.md
```

---

## Variation Summary

| ID | Axis | Core Bet | Primary Rubric Targets |
|----|------|----------|------------------------|
| V-01 | Role sequence (trace-first) | Platform findings inform flow sims; reduces redundancy | C-01, C-08 |
| V-02 | Output format (mandatory table) | Column enforcement prevents missing boundary/severity | C-02, C-03, C-07 |
| V-03 | Lifecycle emphasis (exception budgets) | Named exception obligations per sub-skill surface edge cases | C-06, C-04 |
| V-04 | Phrasing register (intent-first) | "Your job is to find X" reduces silent sub-skill skipping | C-01, C-05 |
| V-05 | Combination (V-01 + V-02 + V-03) | Structural requirements make F-NN + scenarios non-optional | C-01–C-05, C-09, C-10 |

**Expected leaderboard hypothesis**: V-05 > V-02 > V-01 > V-03 > V-04 on composite score. V-04 is the control for whether register alone matters. V-02 is the safest essential-criteria passer. V-05 is the high-variance bet for 90+.
