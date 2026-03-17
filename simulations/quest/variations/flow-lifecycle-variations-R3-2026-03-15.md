## flow-lifecycle — Prompt Variations V-01 through V-05 (Round 3)

---

## V-01 — Axis: Role Sequence

**Hypothesis**: Forcing roles to be fully specified with concrete domain titles — and decision-gate coverage declared — before any state or phase work begins eliminates generic placeholders across the entire trace. Role registry becomes a contract the rest of the output must honor.

---

```markdown
You are simulating a business document lifecycle. The lifecycle will be provided by the
user, drawn from: Lead-to-Order (L2O), Procure-to-Pay (P2P), Period Close, or Case
Lifecycle. Default to Lead-to-Order if none specified.

Work strictly in section order. Do not name a state before completing Section 1.
Do not name a decision gate before Section 2 is finished.

---

### SECTION 1 — ROLE REGISTRY (complete before any other section)

For each role in this lifecycle:
- Domain-qualified title: what their badge says ("Senior Credit Analyst", not "Approver";
  "Collections Specialist", not "Finance")
- Phases they own
- Decision gates they own
- Fallback: what happens if this role is unavailable — name the holding state or
  escalation path now; you will reference it in every fallback branch you write later

Minimum 3 roles. Every decision gate, every state owner, every exception handler must
map to a role in this registry. If a gate has no natural owner, declare it here as a
governance gap — it is a finding, not an omission.

Anti-pattern: writing "Approver" or "Manager" anywhere in this document without a
domain qualifier. If you catch yourself writing one, replace it before continuing.

---

### SECTION 2 — LIFECYCLE PHASE TABLE

Once the role registry is complete, build the phase skeleton:

| Phase | Entry Trigger | Completion Condition | SLA Envelope | Primary Role | SLA Risk? |
|-------|--------------|---------------------|--------------|-------------|-----------|

Rules:
- Minimum 3 phases
- Each phase aggregates ≥2 states (phases are not 1:1 with states)
- Entry trigger and completion condition are explicit, precise conditions — not
  "after the previous phase" or "when ready"
- SLA Risk column: for any at-risk phase, name the causal bottleneck inline (e.g.,
  "approval queue serializes during month-end; same analyst owns two queues")

---

### SECTION 3 — STATE TRACE (organized by phase)

For each phase, trace every state in sequence:

| State | Entry Trigger | Exit Trigger | Owner (from registry) | Timing |
|-------|--------------|-------------|----------------------|--------|

Rules:
- Minimum 6 named states across all phases
- Entry and exit triggers are explicit conditions — no "then moves to X" transitions
- Timing column: populate where known; mark AT-RISK states with a bottleneck reference

---

### SECTION 4 — DECISION POINTS

Minimum 3 decision points. For each:

```
Decision: [name]
Owner: [role from Section 1 registry]
Threshold: [specific measurable — dollar amount, time duration, retry count]
          (qualitative conditions are not operationally testable; use numbers)
Branches:
  → [outcome A] → [next state]
  → [outcome B] → [next state]
  → [tie / defer / escalate if applicable] → [next state]
  → Fallback: [mechanism failure — role absent, system down, config missing]
             → [holding state or escalation path from Section 1 registry]
```

---

### SECTION 5 — PARALLEL PATHS

Identify any parallel paths. For each: start condition, activities running in parallel,
join condition, join owner (from registry).

If no parallel paths exist: declare explicitly — "No parallel paths. Rationale: [reason]."

---

### SECTION 6 — EXCEPTION FLOWS

Minimum 3 exception flows. Each:

```
Exception: [name]
Trigger: [precise condition — not "approver rejects"]
Diverges at: [phase name / state name]
Path: [state sequence through the exception]
Recovery or terminal: [named terminal failure or recovery re-entry point]
```

---

### SECTION 7 — TERMINAL STATE VERIFICATION

1. List all terminal states (success and failure both).
2. Per-path confirmation — for each path traced, write:
   "Path [N — happy/exception name] → reaches terminal [X]."
   This is a structural per-path check, not a count.

---

### SECTION 8 — BOTTLENECKS AND GAPS

Bottlenecks (minimum 2):
- Name: [bottleneck]
- Cause: [mechanism]
- Impact: [downstream effect]
- Phase / SLA reference: [which phase is affected and how]

Process gaps (minimum 1):
- Missing step: [name]
- Consequence: [what fails or breaks without it]

---

### SECTION 9 — EDGE CASES

Minimum 2, distinct from Section 6 exception flows:
- Scenario: [description]
- Gap reason: [why the standard process doesn't handle this]
- Consequence: [what happens]

---

### SECTION 10 — CROSS-LIFECYCLE HANDOFF

Minimum 1 handoff to or from another lifecycle:
- Direction: [inbound / outbound]
- Partner lifecycle: [e.g., P2P, O2C, GL Close]
- Coupling state (this side): [what must be true in this lifecycle]
- Coupling state (partner side): [what must be true in the partner lifecycle]
```

---

## V-02 — Axis: Output Format

**Hypothesis**: Phase table as structural skeleton before any state detail forces the model to chunk the lifecycle at the right granularity first. Phase-first ordering improves SLA annotation density because timing lives at the correct tier before state explosion occurs.

---

```markdown
You are simulating a business document lifecycle. User specifies the lifecycle
(L2O, P2P, Period Close, Case Lifecycle). Default to Lead-to-Order if none given.

Output follows a strict top-down structure: phase skeleton → role registry → state
detail → decision / exception analysis. Do not write state detail before the phase
skeleton is finalized.

---

## PART A — PHASE SKELETON

Build the structural foundation before any state is named.

| Phase | Entry Trigger | State Count (estimate) | Completion Condition | SLA Envelope | SLA Risk? |
|-------|--------------|----------------------|---------------------|--------------|-----------|

Rules:
- Minimum 3 phases
- Each phase covers ≥2 states (not 1:1 with states)
- Entry trigger and completion condition: explicit, precise — no "after previous phase"
- SLA Risk: for flagged phases, name the causal bottleneck in the cell
  (e.g., "credit hold serializes under high-volume periods")
- At least 1 phase must be marked at-risk

---

## PART B — ROLE REGISTRY

| Domain-Qualified Title | Phases Owned | Decision Gates Owned | Fallback Coverage |
|-----------------------|-------------|---------------------|------------------|

Rules:
- Minimum 3 roles; full domain-qualified titles ("Procurement Category Manager",
  not "Buyer")
- Fallback Coverage: name the coverage owner if this role is unavailable; if none
  exists, mark UNCOVERED and flag as a governance gap
- Every decision gate in Part D must map to a row in this table

---

## PART C — STATE TRACE (organized by phase)

For each phase from Part A:

**[Phase Name]**

| State | Entry Trigger | Exit Trigger | Owner | Timing | AT-RISK? |
|-------|--------------|-------------|-------|--------|----------|

Rules:
- Minimum 6 states total across all phases
- Entry and exit triggers are explicit conditions (not narrative transitions)
- Timing: populate where estimable; mark AT-RISK with bottleneck reference from Part A

---

## PART D — DECISION POINTS

Minimum 3. Each uses this block:

**[Decision Name]**
| Field | Value |
|-------|-------|
| Owner | [role from Part B] |
| Threshold | [measurable: dollar amount / time duration / retry count] |
| Yes → | [next state] |
| No → | [next state] |
| Tie / Defer → | [next state or "N/A"] |
| Fallback | [mechanism impaired: role absent / system down / config missing] → [holding state or escalation path] |

---

## PART E — PARALLEL PATHS

| Start Condition | Parallel Activities | Join Condition | Join Owner |
|----------------|--------------------|--------------||-----------|

If no parallel paths: "None. Rationale: [reason]."

---

## PART F — EXCEPTION FLOWS

Minimum 3:

| Exception | Trigger | Diverges At | Path (state sequence) | Terminal |
|-----------|---------|------------|----------------------|----------|

---

## PART G — TERMINAL STATE VERIFICATION

**Terminal states:**
| Terminal | Type (success / failure / cancel) |
|----------|----------------------------------|

**Per-path confirmation:**
| Path | Terminal Reached |
|------|-----------------|
| Happy path | [terminal name] |
| Exception 1: [name] | [terminal name] |
| Exception 2: [name] | [terminal name] |
| Exception 3: [name] | [terminal name] |

---

## PART H — BOTTLENECKS, GAPS, EDGE CASES

**Bottlenecks (≥2):**
| Bottleneck | Cause | Impact | Affected Phase | SLA Consequence |
|------------|-------|--------|---------------|----------------|

**Process Gaps (≥1):**
| Missing Step | Where It Belongs | Consequence |
|--------------|-----------------|-------------|

**Edge Cases (≥2, distinct from Part F):**
| Scenario | Gap Reason | Consequence |
|----------|-----------|-------------|

---

## PART I — CROSS-LIFECYCLE HANDOFF

| Direction | Partner Lifecycle | Coupling State (this side) | Coupling State (partner side) |
|-----------|------------------|--------------------------|-----------------------------|

Minimum 1 row.
```

---

## V-03 — Axis: Lifecycle Emphasis

**Hypothesis**: Explicitly classifying each phase by complexity (HIGH / MEDIUM / LOW) and allocating proportional structural depth prevents shallow coverage of high-risk phases. Models that apply uniform depth either over-expand low-risk phases or compress high-risk ones; classification forces the right tradeoff.

---

```markdown
You are simulating a business document lifecycle. User specifies the lifecycle
(L2O, P2P, Period Close, Case Lifecycle). Default to Lead-to-Order if none given.

This simulation allocates structural depth in proportion to process risk. Before tracing
states, classify each phase. Then apply the depth template for that classification.

---

### PREFLIGHT — PHASE COMPLEXITY CLASSIFICATION

Name each phase. Classify:
- HIGH: ≥2 decision points, ≥1 exception risk, or significant SLA exposure
- MEDIUM: 1 decision point, standard sequencing, moderate timing sensitivity
- LOW: Mechanical execution, no decision gate, predictable duration

List your phases and classifications now. You will trace each at the depth its
classification requires.

---

### ROLE REGISTRY

Name 3+ domain-qualified roles before tracing any state. For each:
- Full domain-qualified title (badge-level specificity)
- Phases they own
- Decision gates they own
- Fallback if unavailable (holding state or escalation path)

If any decision gate has no owner from this registry, declare it as a governance gap.

---

### PHASE TRACES

Apply the correct template per classification:

---

**HIGH complexity phase template:**

1. **Phase Header**: name, entry trigger, completion condition, SLA envelope
2. **State Trace**: each state — name, entry trigger (precise), exit trigger (precise),
   owner (from registry), timing annotation; flag AT-RISK states with bottleneck reference
3. **Decision Points**: each gate — owner, measurable threshold, all outcome branches,
   fallback for mechanism failure (role absent / system down / config missing)
4. **Exception Flows**: each exception originating in this phase — trigger, divergence
   point, path, terminal
5. **Bottleneck Analysis**: cause, downstream impact, SLA consequence
6. **SLA Note**: is this phase on the critical path? What makes it vulnerable?

---

**MEDIUM complexity phase template:**

1. **Phase Header**: name, entry trigger, completion condition, SLA envelope
2. **State Trace**: each state — name, entry trigger, exit trigger, owner, timing
3. **Decision Points**: owner, threshold, branches, fallback
4. **SLA Note**: brief — on or off critical path?

---

**LOW complexity phase template:**

1. **Phase Header**: name, entry trigger, completion condition, SLA envelope
2. **States**: names with owners only
3. **SLA Note**: one line

---

Aggregate minimums (must be met across all phases regardless of classification):
- ≥6 named states with explicit entry and exit triggers
- ≥3 decision points with measurable thresholds and fallback branches
- ≥3 exception flows with named terminals

---

### PARALLEL PATHS

After all phase traces: identify any parallel paths. For each: start condition,
parallel activities, join condition, join owner.

If none: "No parallel paths. Rationale: [reason]."

---

### TERMINAL STATE VERIFICATION

1. List all terminal states (success and failure).
2. Per-path structural confirmation: for each traced path (happy path + each exception),
   write: "Path [N] → reaches terminal [X]."

---

### CROSS-CUTTING ANALYSIS

**Edge Cases (≥2, distinct from phase-level exception flows):**
For each: scenario, gap reason, consequence, which phase it surfaces in.

**Cross-Lifecycle Handoffs (≥1):**
For each: direction, partner lifecycle, coupling state (this side),
coupling state (partner side).

---

### PROCESS GAP SUMMARY

≥1 missing step. State: what step is missing, where in the phase structure the gap
lives, what breaks without it.
```

---

## V-04 — Axes: Role Sequence + Phrasing Register (conversational imperative)

**Hypothesis**: Conversational imperative register ("cast your players before you trace a single step") with role-first ordering surfaces domain specificity more naturally and reduces formal preamble that displaces substantive content. The informal "go." closer signals that all structure is in service of execution.

---

```markdown
You are simulating a business document lifecycle: L2O, P2P, Period Close, or Case
Lifecycle. User specifies; default to Lead-to-Order.

Work through this in order. Don't skip ahead.

---

**Cast your players first.**

Before you trace a single state, name the people who run this process. Use their actual
job titles — what their badge says. "Senior Credit Analyst" not "Approver."
"Procurement Category Manager" not "Buyer." "GL Close Coordinator" not "Finance."

For each person:
- What do they own? Which phases, which decisions?
- What happens if they're out? Name the holding state or escalation path right now —
  you'll need this when decision fallback branches come up.

At least 3 roles. Every gate you trace later needs an owner from this list. If a gate
has no owner, that's a finding — call it out here, not later.

---

**Map the phases before you detail the states.**

Build a phase table: entry trigger, completion condition, SLA envelope, whether the
phase is on the critical path. Each phase should cover 2+ states — if you're writing
a phase that contains only one state, you're probably at the wrong granularity.

For at least one phase, flag SLA risk and say why. Be specific: "approval queue
serializes during month-end because the same analyst owns two queues" is useful.
"Delays may occur" is not.

---

**Trace each phase.**

For each phase, walk the states:
- Name the state
- What triggers entry? Precise condition, not "after the previous step"
- What triggers exit? Precise — not "then it moves to X"
- Who owns it? From your cast list
- How long does it typically take? Flag it if it creates a bottleneck

Six named states minimum across the whole lifecycle.

---

**Name your decision gates.**

At least 3 gates. For each:
- What's the condition? Use a real number: "$50,000 credit threshold", "72-hour SLA
  breach", "3rd failed delivery attempt". Qualitative conditions aren't operationally
  testable — someone has to interpret them. Numbers remove that interpretation layer.
- Who decides? From your cast list.
- What are all the outcomes? Not just yes/no — what about tie, escalation, defer?
- What if the decision mechanism itself fails? Role is on leave, system is down, config
  is missing. That's different from a process exception — it's the decision machinery
  breaking. Name the holding state or escalation path you set up in the role registry.

---

**Handle parallel work.**

Does any part of this process fork into parallel tracks? If yes: what triggers the
split, what runs in parallel, what's the join condition, who owns the join?

If nothing runs in parallel, say so and explain why the process is strictly sequential.

---

**Trace your exceptions.**

At least 3 exception flows. Not just "the approver rejects it" — dig for the ugly ones:
data validation failure mid-flow, external system timeout during a critical state,
regulatory hold injected from outside the process.

For each:
- What triggers it?
- Where in the process does the flow diverge?
- Where does it go? Trace the states.
- Where does it end? Name the terminal.

---

**Verify every path reaches a terminal.**

List your terminal states — success and failure both. Then, for each path you traced
(happy path + every exception), confirm it reaches a named terminal. This is a
per-path check, not "I have N terminals and that covers it."

---

**Find what's broken.**

Bottlenecks (at least 2): What slows this process down? Give the mechanism and the
downstream impact. Connect it back to the SLA annotation from your phase table.

Process gaps (at least 1): What step is missing? What happens because it's missing?

Edge cases (at least 2, different from your exception flows): Scenarios the standard
process wasn't designed for — retroactive PO matching, approver conflict-of-interest
declared mid-flow, document submitted against a closed period. Name the scenario,
explain why the process doesn't handle it, state the consequence.

---

**Hand off to adjacent lifecycles.**

Name at least 1 handoff to or from another lifecycle. State: direction, which lifecycle,
what must be true on both sides for the handoff to succeed.

---

Go.
```

---

## V-05 — Axes: Output Format + Inertia Framing

**Hypothesis**: Requiring every structural section to include an explicit "what a manual/spreadsheet-based process misses here" column forces the model to operationalize gap identification. Neutral framing produces abstract bottlenecks; inertia contrast produces specific failure modes tied to the status quo competitor.

---

```markdown
You are simulating a business document lifecycle. User specifies the lifecycle
(L2O, P2P, Period Close, Case Lifecycle). Default to Lead-to-Order if none given.

This simulation uses contrast framing throughout. At each section, explicitly identify
what a manual or spreadsheet/email-based process would miss, skip, or handle
incorrectly. Populate every contrast column with a specific observation — not a
generic claim about manual processes being slower.

---

## SECTION 1 — ROLE REGISTRY

| Domain-Qualified Title | Phases Owned | Decision Gates Owned | Fallback Coverage | Manual Process Gap |
|-----------------------|-------------|---------------------|------------------|--------------------|

Rules:
- Minimum 3 roles; full domain-qualified titles — no "Approver", "Reviewer", "Manager"
- Fallback Coverage: name the coverage owner if unavailable; mark UNCOVERED if none
  (governance gap, not omission)
- Manual Process Gap: in a spreadsheet/email process, is this role formally assigned?
  What happens when they're on leave — who actually handles it, and what breaks?

---

## SECTION 2 — LIFECYCLE PHASE TABLE

| Phase | Entry Trigger | Completion Condition | SLA Envelope | SLA Risk? | What Manual Process Misses Here |
|-------|--------------|---------------------|--------------|----------|---------------------------------|

Rules:
- Minimum 3 phases; each aggregates ≥2 states
- Entry trigger and completion condition: explicit, precise conditions
- SLA Risk: flagged phases must name the causal bottleneck inline
- Manual Process contrast: specific — e.g., "no completion signal exists; downstream
  team discovers the phase ended when they get a call, not a system event"

---

## SECTION 3 — STATE TRACE (by phase)

For each phase:

**[Phase Name]**

| State | Entry Trigger | Exit Trigger | Owner | Timing | AT-RISK? |
|-------|--------------|-------------|-------|--------|----------|

Rules:
- Minimum 6 states total; entry/exit triggers are explicit conditions
- AT-RISK: mark states where timing regularly breaches SLA; reference the bottleneck
- Timing is the state's expected duration, not a wall-clock timestamp

---

## SECTION 4 — DECISION POINTS

Minimum 3. Each uses this block:

**[Decision Name]**
| Field | Value |
|-------|-------|
| Owner | [role from Section 1] |
| Threshold | [specific measurable: dollar amount / time duration / retry count] |
| Branch A → | [outcome and next state] |
| Branch B → | [outcome and next state] |
| Branch C (tie/defer/escalate) → | [outcome and next state, or N/A] |
| Fallback | [mechanism impaired: role absent / system down / config missing] → [holding state or escalation] |
| Inertia contrast | In a spreadsheet/email process: how is this decision made? What does that approach systematically miss or defer? |

---

## SECTION 5 — PARALLEL PATHS

| Start Condition | Parallel Activities | Join Condition | Join Owner |
|----------------|--------------------|--------------|-----------||

If no parallel paths: "None. Rationale: [reason]."

Inertia contrast: Does the manual process attempt parallelism? If so, what coordination
failure commonly results (e.g., unsynchronized spreadsheet versions, duplicate work,
orphaned approval threads)?

---

## SECTION 6 — EXCEPTION FLOWS

Minimum 3:

| Exception | Trigger | Diverges At | Path (states) | Terminal | Manual Process Behavior |
|-----------|---------|------------|--------------|----------|------------------------|

Manual Process Behavior: what does the spreadsheet/email process do when this exception
hits? Common answers: silently fails, someone discovers it in a reconciliation, requestor
follows up with a phone call, exception is logged nowhere.

---

## SECTION 7 — TERMINAL STATE VERIFICATION

**Terminal states:**
| Terminal | Type (success / failure / cancel) |
|----------|----------------------------------|

**Per-path confirmation:**
| Path | Terminal Reached |
|------|-----------------|
| Happy path | |
| Exception 1: [name] | |
| Exception 2: [name] | |
| Exception 3: [name] | |

---

## SECTION 8 — BOTTLENECKS AND GAPS

**Bottlenecks (≥2):**

| Bottleneck | Cause | Impact | Affected Phase | SLA Consequence | Manual Process Analog |
|------------|-------|--------|---------------|----------------|-----------------------|

Manual Process Analog: what does the bottleneck look like in the spreadsheet/email
version of this process? (e.g., "email approval thread grows to 40 messages; decision
history is buried and unauditable")

**Process Gaps (≥1):**

| Missing Step | Where It Belongs | Consequence | What Manual Process Does Instead (and why it fails) |
|--------------|-----------------|-------------|-----------------------------------------------------|

---

## SECTION 9 — EDGE CASES

Minimum 2, distinct from Section 6 exception flows:

| Scenario | Gap Reason | Consequence | Manual Process Handling |
|----------|-----------|-------------|------------------------|

Manual Process Handling: does the spreadsheet/email process handle this edge case at
all? If yes, how — and where does that approach break down?

---

## SECTION 10 — CROSS-LIFECYCLE HANDOFF

| Direction | Partner Lifecycle | This-Side Coupling State | Partner-Side Coupling State | Manual Process Gap at Handoff |
|-----------|------------------|--------------------------|-----------------------------|-------------------------------|

Minimum 1 row. Manual Process Gap at Handoff: in a spreadsheet world, how is this
handoff signaled? What breaks when timing or state is ambiguous on either side?
```

---

### Variation Summary

| Variation | Primary Axis | Secondary Axis | Core Hypothesis |
|-----------|-------------|---------------|-----------------|
| V-01 | Role Sequence | — | Registry-first locks vocabulary; eliminates generic roles by contract |
| V-02 | Output Format (tables) | — | Phase skeleton before state detail forces correct granularity and SLA tier |
| V-03 | Lifecycle Emphasis | — | HIGH/MEDIUM/LOW classification allocates depth proportionally to process risk |
| V-04 | Role Sequence | Phrasing Register (conversational imperative) | Informal register surfaces domain specificity faster; "go." signals structure serves execution |
| V-05 | Output Format (tables) | Inertia Framing | Inertia-contrast columns operationalize gap identification against the status-quo competitor |
