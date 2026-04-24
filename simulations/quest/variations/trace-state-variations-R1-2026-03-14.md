Written to `simulations/quest/variations/trace-state-variations-R1-2026-03-14.md`.

---

## Round 1 Variations -- trace-state

### Variation design

**Three single-axis:**

| V | Axis | Primary rubric target | Key mechanism |
|---|------|-----------------------|---------------|
| **V-01** | Output format | C-09, C-10 | Pre-printed tables: state machine table (C-10 gate), trace table with Before/After columns (C-01/C-02 gate), anomaly register with required type column (C-09 gate) |
| **V-02** | Phrasing register | C-01 through C-07 (control) | Conversational question-driven prose; no table mandate; Step 4 explicitly requests numbered steps (C-07) |
| **V-03** | Role sequence | C-04, C-05, C-09 | Domain Expert locks vocabulary before any trace (C-05 gate); Anomaly Finder sweeps all four types with dedicated per-type sections (C-04/C-09 gate) |

**Two combination:**

| V | Axes | Hypothesis |
|---|------|-----------|
| **V-04** | Output format + role sequence | Highest-structure: role gates enforce role correctness; tables within each role enforce column-level coverage. Anomaly Finder sweep table forces four verdicts (one per anomaly type) -- the strongest C-09 surface in all five variations |
| **V-05** | Lifecycle emphasis + phrasing register | GATE 2 locks the state machine before the trace begins (prevents mid-trace domain model drift). PHASE 4 has four explicit per-type sub-headings. Conversational within phases. |

### Key design decision

The primary failure mode for `trace-state` is **happy-path collapse** -- tracing only the forward path and never pausing to hunt anomalies. This is the state-trace analog of inertia framing. V-03/V-04 address it through the Anomaly Finder role; V-05 addresses it through PHASE 4's forced four-type sweep; V-01 addresses it through the required anomaly-type column. V-02 is the control -- tests whether question phrasing alone prevents the collapse.

### Predicted C-09/C-10 ceiling

**V-04** -- sweep table forces four anomaly type verdicts (C-09) + state machine table with Op IDs and entry conditions (C-10). No omission path on either aspirational criterion.

### Open research questions for R2

1. Does the Domain Expert role gate (V-03/V-04) produce better domain vocabulary than the column mandate (V-01)?
2. Does the Anomaly Finder sweep table (V-04) outperform per-type sub-headings (V-03/V-05) on C-09 live runs?
3. Does GATE 2 (V-05) prevent mid-trace state machine drift more reliably than the role gate (V-03/V-04)?
-01 enforces
it as a column requirement ("Domain Description" vs "Description"). V-02 relies on question
phrasing alone -- the weakest enforcement.

**C-04 (anomaly identification) is where most traces die.** The happy path is easy to trace;
anomalies require a deliberate hunting posture. V-03 and V-04 give the Anomaly Finder its own
role with explicit per-type sections. V-05 gives PHASE 4 explicit per-type sub-headings. V-01
uses a required anomaly-type column to force categorization. V-02 asks for the hunt in Step 6
but provides no structural enforcement.

**Inertia framing is not applicable to trace-state directly.** The nearest analog is the
all-happy-path bias: the inertia mode for a state trace is tracing only the forward path and
never the rejected transitions or concurrent conflicts. V-01 through V-05 all address this
through the rejected-transition requirement, but they do so with different structural strength.

---

## V-01: Output Format (Table-Structured)

**Axis:** Output format -- pre-printed tables for state machine declaration (C-10), operation
trace (C-01/C-02), and anomaly register (C-04/C-09). Every required column is pre-printed;
a blank is visible.

**Hypothesis:** Pre-printed tables prevent the most common failure modes: missing before/after
state (C-01), skipped preconditions or postconditions (C-02), and anomalies that are described
but not categorized by type (C-09). The anomaly-type column in the register forces explicit
categorization without a separate instruction. The state machine table forces domain-realistic
naming by column (Domain Description column vs a generic Description) -- a soft C-05 gate.

```
You are running /trace-state. Fill in this structured template.
All section headers are fixed. Do not reorder, rename, or remove any section header, table, or column.

---

## SETUP: PRIOR SIGNALS
[Search simulations/trace/ and simulations/scout/ for any prior state, request, or contract
artifacts on this topic.]
Prior signals found: [List files found, or write "None -- starting fresh."]

## DOMAIN: STATE MACHINE
[Declare the entity and its state machine before tracing any operations. Complete this table first.]
Entity: [Name of the entity -- domain-realistic. Examples: SalesOpportunity, SupportTicket, Invoice.]
Domain: [Sales / Customer Service / Finance -- select one]

| State ID | State Name | Domain Description | Terminal? |
|----------|-----------|-------------------|-----------|
| S-01 | [Name] | [What this state means to a practitioner in this domain] | yes / no |
| S-02 | [Name] | [What this state means to a practitioner in this domain] | yes / no |
[Minimum 4 rows. Terminal = no further transitions expected under normal operation.]

Valid transitions:
[Map all allowed transitions before the trace begins. Operations not listed here are not allowed.]
| From State | Operation | To State |
|-----------|-----------|---------|
| [S-ID] | [operation name] | [S-ID] |
| [S-ID] | [operation name] | [S-ID] |
[Add one row per allowed transition. Every operation in TRACE: OPERATION LOG must appear here.]

Invariants:
[At least one invariant must be declared before the trace begins. State it precisely -- scope it
to specific states or the full lifecycle.]
- INV-01: [Complete invariant statement with scope. Example: "A Closed Won opportunity can
  never revert to Qualified without manager re-engagement logged."]
[Add INV-02, INV-03 as the domain warrants.]

## TRACE: OPERATION LOG
[Trace each operation in the scenario. Number every step. Before-State and After-State are
required columns -- do not leave them blank. Preconditions must be state-specific, not generic.]

| Step | Before-State (S-ID: Name) | Operation | Preconditions (state-specific, one per line) | After-State (S-ID: Name) | Postconditions (one per line) | INV Check |
|------|--------------------------|-----------|---------------------------------------------|--------------------------|------------------------------|-----------|
| 1 | [S-ID: State Name] | [operation] | - [Precondition 1]<br>- [Precondition 2] | [S-ID: State Name] | - [Postcondition 1] | INV-01: pass |
| 2 | [S-ID: State Name] | [operation] | - [Precondition 1] | [S-ID: State Name] | - [Postcondition 1] | INV-01: pass |
[Minimum 4 happy-path steps. Every S-ID must reference a state declared in DOMAIN: STATE MACHINE.]

Rejected transitions:
[At least one rejected transition required. State must not change on rejection.]
| Step | Before-State (S-ID: Name) | Attempted Operation | Failing Precondition | Rejection Behavior | After-State (S-ID: Name) |
|------|--------------------------|--------------------|--------------------|-------------------|--------------------------|
| [N] | [S-ID: State Name] | [operation attempted] | [Specific precondition text that is not met] | [reject / error / exception -- state unchanged] | [Same S-ID: Name] |

## ANOMALIES
[At least one anomaly required. The Anomaly Type column is required for every row -- do not omit
it or merge types. Add one row per distinct finding.]

| ID | Anomaly Type | Operation + State | Description | Production Consequence |
|----|-------------|-------------------|-------------|------------------------|
| A-01 | invalid-transition / missing-precondition-check / invariant-violation / race-condition | [operation at S-ID] | [Specific description of what can go wrong] | [What happens in production if not caught] |
[Add A-02, A-03 for additional findings. Cover as many anomaly types as the trace warrants.]

Race condition scenario:
[Complete if a race condition was identified in ANOMALIES. Skip with "No race condition in scope" if none.]
Concurrent ops:  [Op-A] and [Op-B], both attempting on entity in state [S-ID]
Interleave:      [Sequence: Op-A reads state, Op-B writes new state, Op-A writes -- conflict]
Resolution:      [Which operation wins, or how conflict is detected and rejected]

---

Write artifact: simulations/trace/state/{topic}-state-{date}.md
Frontmatter: skill, topic, date, domain, entity, state_count, operation_count, anomaly_count,
             anomaly_types (list), invariant_count, race_condition_analyzed (true/false).
```

---

## V-02: Phrasing Register (Conversational)

**Axis:** Phrasing register -- descriptive, question-driven prose replaces imperative directives
and pre-printed tables. The prompt reads as a thinking partner walking through state machine
analysis, not a compliance checklist. Questions surface intent before asking for output.

**Hypothesis:** Conversational register lowers friction for dev audiences encountering this skill
for the first time, at the cost of weaker structural enforcement. Essential criteria (C-01 through
C-05) can be met if questions are specific enough. C-07 (numbered steps) is explicitly requested
in Step 4. C-10 (structured notation) is unlikely to appear reliably without a table mandate.
This is the control variation: minimum structural overhead, maximum readability, weakest
aspirational enforcement.

```
You are running /trace-state.

State machine analysis is most useful when it reveals what the system does in states and sequences
that the implementation never planned for. The goal is not to document the happy path -- that is
already in the spec. The goal is to find the transitions that were not anticipated, the invariants
that cannot hold under concurrent load, and the preconditions that exist in the design but are
missing from the code.

---

**Step 1: Check what we already know.**

Look in simulations/trace/ and simulations/scout/ for any prior state, request, or contract
artifacts on this topic. List what you find with a one-line summary of each. If you find nothing,
say so -- a trace starting from zero is a different signal than one that builds on prior work.

Prior signals: [list files with one-line summaries, or "None -- starting fresh."]

---

**Step 2: Name the entity and its domain.**

What is the entity whose state machine you are tracing? Give it a name a practitioner in this
domain would recognize -- the kind of name that appears in a CRM, ticketing system, or ERP, not
a generic design placeholder. Which domain does this belong to: Sales, Customer Service, or Finance?
Write one sentence on why this entity has a meaningful lifecycle in that domain context.

Entity: [domain-realistic name]
Domain: [Sales / Customer Service / Finance]
Context: [One sentence -- what business problem does this entity's lifecycle address?]

---

**Step 3: Map the state machine.**

What states can this entity be in? List each one with a description that would make sense to a
practitioner -- the kind of label that appears in a status dropdown, not an architectural diagram.
Mark which states are terminal: the entity does not normally move from them.

Then list the valid transitions. For each operation, name the state it starts from and the state
it moves to. Be complete -- a transition not listed here is not valid, and the trace in Step 4
will use this map as its contract.

Finally, name at least one invariant. An invariant is not a business rule -- it is a mechanical
guarantee the system must enforce regardless of user intent. "A Closed Won opportunity cannot
revert to Draft" is an invariant. "Users should fill in all fields" is not. State it precisely:
name the scope (all states, specific states, or post a specific operation) and what breaks in
production if it is violated.

States: [List each with domain name, description, and terminal flag]
Valid transitions: [List each as "operation: FROM-STATE to TO-STATE"]
Invariants: [At least one, stated with explicit scope and violation consequence]

---

**Step 4: Trace the scenario step by step.**

Walk the entity through a realistic scenario. Number each step. For each step, answer explicitly:
- What state is the entity in before this operation?
- What operation is applied?
- What must be true before this operation is allowed to execute? Name specific state conditions --
  not "data is valid" or "user is authenticated", but conditions tied to this entity's current state.
- What state is the entity in after the operation completes?
- What is guaranteed to be true about the entity after the operation? Postconditions, not just
  the new state name.
- Do the invariants from Step 3 still hold? Check each one explicitly.

Trace at least four steps on the main path.

---

**Step 5: Attempt at least one invalid transition.**

Pick a state from the trace. Try to apply an operation that is not valid from that state --
something not listed in the valid transitions from Step 3. What specific precondition fails?
What should the system do? The entity's state must not change on a rejected transition. Document
this explicitly: the starting state, the attempted operation, the specific failing precondition,
the rejection behavior, and the unchanged state after the attempt.

---

**Step 6: Hunt for anomalies.**

Review the trace from Step 4 and look for at least one finding from this list. For each finding,
name the anomaly type precisely.

- Invalid state transition: does any step, or any possible sequence of steps, move the entity
  to a state it should not be reachable from the starting state?
- Missing precondition check: are there preconditions listed in the trace steps that the
  implementation is unlikely to enforce? Look for conditions that require data the system may
  not have at execution time, or checks that belong to a different layer than where the
  operation is handled.
- Invariant violation: is there a sequence of operations that would leave an invariant false?
  Include concurrent sequences if applicable.
- Race condition: can two operations be applied to the same entity simultaneously in a way
  that produces a conflicting state outcome?

For each finding: name the type, name the specific operation and state where it occurs, describe
what would happen in production if it is not caught.

---

**Step 7: Examine concurrent conflicts.**

Is there any pair of operations in the trace that a user or automated process could attempt
simultaneously on the same entity? If so: name both operations, describe the interleave (which
reads and writes happen in which order), identify the resulting conflict, and describe how the
system should detect or resolve it.

If no concurrent conflict applies, explain briefly why the domain's operation model prevents it.

---

Write artifact: simulations/trace/state/{topic}-state-{date}.md
Frontmatter: skill, topic, date, domain, entity, state_count, operation_count, anomaly_count,
             race_condition_analyzed (true/false).
```

---

## V-03: Role Sequence (Domain Expert -> Compiler -> Anomaly Finder)

**Axis:** Role sequence -- three named roles execute in strict order. Domain Expert establishes
the state machine vocabulary, valid transitions, and invariants before any tracing occurs. Compiler
hand-compiles the operation log. Anomaly Finder sweeps all four anomaly types explicitly, one
section per type. Each role has a gate condition that must be satisfied before the next role begins.

**Hypothesis:** Separating state machine declaration (Domain Expert) from trace execution
(Compiler) from anomaly analysis (Anomaly Finder) prevents the most common collapse: the model
traces the happy path fluently but never pauses to hunt anomalies with rigor. The Anomaly
Finder's explicit per-type sweep is the structural gate for C-04 and C-09. The Domain Expert
gate ensures C-05 domain grounding is locked before any operation is named -- preventing generic
vocabulary from entering the trace through the back door.

```
You are running /trace-state.
Three roles execute in sequence. Each role gate must complete before the next role begins.
Do not adjust the Domain Expert's state machine or invariants after the Compiler gate.

---

## SETUP: PRIOR SIGNALS
[Search simulations/trace/ and simulations/scout/ for any prior state, request, or contract
artifacts on this topic.]
Prior signals found: [List files found, or write "None -- starting fresh."]

---

## DOMAIN EXPERT: DECLARE

[The Domain Expert establishes the state machine before any tracing occurs. Use vocabulary a
Sales rep, support engineer, or finance analyst would recognize without translation. Generic
names like "Pending" and "Processed" do not pass -- use the vocabulary the domain actually uses.]

Entity: [Name -- domain-realistic. Not "Entity" or "Object".]
Domain: [Sales / Customer Service / Finance]

States:
[List each state with the domain name practitioners use. Mark terminal states.]
| State | Description (domain language) | Terminal? |
|-------|------------------------------|-----------|
| [Name] | [What this state means to a practitioner -- status field language] | yes / no |
[Minimum 4 rows.]

Valid transitions:
[Every operation that the Compiler will trace must appear here first. This is the contract.]
| Operation | From | To |
|-----------|------|----|
| [operation name -- verb form, domain-realistic] | [state name] | [state name] |
[Add one row per valid transition. Be complete -- the Compiler is not allowed to invent transitions.]

Invariants:
[Declare at least one. State it as a complete sentence with explicit scope. The Compiler will
check each invariant at every step and the Anomaly Finder will sweep for violations.]
- INV-01: [Precisely stated invariant with scope. Example: "A Resolved ticket can only be
  Reopened if the original reporter or a manager initiates the reopen -- self-reassignment
  from Resolved is invalid."]
[Add INV-02, INV-03 as the domain warrants.]

Domain Expert gate -- required before COMPILER begins:
[ ] Entity and domain named with domain-realistic vocabulary (no generic placeholders)
[ ] At least 4 states declared with domain-language descriptions
[ ] All valid operations listed with from/to state pairs
[ ] At least one invariant declared with explicit scope and violation consequence

---

## COMPILER: TRACE

[The Compiler hand-compiles the scenario step by step. The Domain Expert's state machine is
read-only -- do not add new states or operations during tracing. If a gap is found (an operation
that appears necessary but was not declared), flag it as a note for the Anomaly Finder and
continue with the declared set.]

Step 1:
  Before-State:    [State name from DOMAIN EXPERT states]
  Operation:       [Operation name from DOMAIN EXPERT valid transitions]
  Preconditions:   [List each condition that must be true for this operation to be allowed.
                   State-specific -- "data is valid" does not count. Name the specific state
                   attribute or system condition that gates this operation.]
                   - [Precondition 1]
                   - [Precondition 2]
  After-State:     [State name from DOMAIN EXPERT states]
  Postconditions:  [List each condition guaranteed to be true after the operation completes.
                   State-specific -- what is different about the entity now?]
                   - [Postcondition 1]
  Invariant check: [INV-01: pass / VIOLATION -- if violation, describe what was broken]

[Repeat the step format for each step in the scenario. Minimum 4 happy-path steps.]

Rejected transition step:
  Before-State:    [State name]
  Attempted op:    [Operation that is not valid from this state -- not in valid-transitions table,
                   or attempted but a precondition is not met]
  Failing precond: [Specific precondition text that is not satisfied]
  Rejection:       [Operation fails; state is unchanged. What is the system's response?]
  After-State:     [Same as Before-State -- state does not change on rejection]

Compiler gate -- required before ANOMALY FINDER begins:
[ ] Every step has Before-State, Operation, Preconditions (state-specific), After-State,
    Postconditions
[ ] At least one rejected transition is documented with named failing precondition
[ ] Invariant check appears at every step

---

## ANOMALY FINDER: REVIEW

[The Anomaly Finder sweeps the Compiler's trace for all four anomaly types. Each type gets its
own section. A section may end with "None found" -- but every section must be evaluated explicitly.
Do not bundle findings into a single list.]

**Invalid state transitions:**
Review the Domain Expert's valid-transitions table. Does the Compiler's trace include any step
where an entity moves between states not listed in that table? Are there sequences of steps that
reach an unauthorized state through a chain of individually-valid transitions?
Finding: [Describe the specific step or sequence and why it violates the declared transition
map. Include the operation name and state IDs. Or write "None found."]

**Missing precondition checks:**
Review the Compiler's preconditions. Are any preconditions listed that the implementation is
unlikely to enforce? Look for conditions that require data the system does not have at execution
time, conditions that must be checked at a different layer than where the operation is handled,
or conditions that are implied by a Domain Expert invariant but not surfaced as an explicit check.
Finding: [Describe the operation, the missing check, and why it is likely to be absent from the
implementation. Or write "None found."]

**Invariant violations:**
Review each invariant from the Domain Expert's declaration and each INV check from the Compiler.
Is there any sequence of operations -- including operations not in the current trace -- that could
leave an invariant false? Does any concurrent scenario create a window where the invariant is
temporarily or permanently broken?
Finding: [Describe the violating operation sequence and which invariant it breaks. Or write
"None found."]

**Race conditions:**
Is there any pair of operations in the Compiler's trace that a user or automated process could
apply concurrently to the same entity? If so: name both operations, describe the problematic
interleave (which reads and writes happen in which order, and why they conflict), name the
resulting state corruption or conflict, and describe how the system should detect or resolve it.
Finding: [Op-A + Op-B, the interleave, the conflict, and the resolution. Or write "None found
-- [reason the domain model prevents concurrency]."]

Anomaly summary:
| ID | Type | Operation + State | Consequence if unhandled |
|----|------|-------------------|--------------------------|
| A-01 | [invalid-transition / missing-precondition-check / invariant-violation / race-condition] | [operation at state] | [Production risk] |
[Minimum 1 row. All findings from the four sections above must appear here.]

---

Write artifact: simulations/trace/state/{topic}-state-{date}.md
Frontmatter: skill, topic, date, domain, entity, state_count, operation_count, anomaly_count,
             anomaly_types (list), invariant_count, race_condition_analyzed (true/false),
             rejected_transitions (count).
```

---

## V-04: Output Format + Role Sequence

**Axes:** Output format (pre-printed tables per role section, column requirements enforce rubric
criteria) + role sequence (Domain Expert -> Compiler -> Anomaly Finder with gate conditions).

**Hypothesis:** Role gates enforce correctness of role responsibilities -- C-05 domain grounding
is a Domain Expert gate condition, not a section convention. Pre-printed tables within each role
section enforce column-level rubric coverage: Domain Expert table enforces C-10 (structured state
machine with entry conditions); Compiler table enforces C-01/C-02 (Before-State/After-State and
Preconditions/Postconditions as required columns); Anomaly Finder sweep table enforces C-09 (all
four types as rows, each requiring a verdict). This is the highest-structure variation: both role
architecture and table architecture apply simultaneously.

```
You are running /trace-state. Fill in this structured template.
Three roles execute in sequence. Each role gate must complete before the next begins.
All table headers are fixed -- do not reorder, rename, or remove any column.
The Domain Expert's state machine is locked after its gate. COMPILER and ANOMALY FINDER are
read-only on it -- gaps become findings, not retroactive additions.

---

## SETUP: PRIOR SIGNALS
[Search simulations/trace/ and simulations/scout/ for any prior state, request, or contract
artifacts on this topic.]
Prior signals: [List files found, or write "None -- starting fresh."]

---

## DOMAIN EXPERT: DECLARE

[Use vocabulary a Sales rep, support engineer, or finance analyst would recognize without
translation. Generic labels ("Pending", "Active", "Done") do not pass -- use the vocabulary
the domain actually uses in its systems.]

Entity: [Domain-realistic name -- the kind that appears in a CRM, helpdesk, or ERP]
Domain: [Sales / Customer Service / Finance]

State machine:
| State ID | State Name | Domain Description | Entry Condition | Terminal? |
|----------|-----------|-------------------|----------------|-----------|
| S-01 | [Name] | [What this state means to a domain practitioner] | [What must be true to enter this state] | yes / no |
| S-02 | [Name] | [What this state means to a domain practitioner] | [What must be true to enter this state] | yes / no |
[Minimum 4 rows. Terminal = no further transitions expected under normal operation.]

Valid transitions:
| Op ID | Operation Name | From State (S-ID) | To State (S-ID) | Domain Meaning |
|-------|---------------|------------------|----------------|----------------|
| OP-01 | [Name] | [S-ID] | [S-ID] | [Why a practitioner would trigger this operation] |
| OP-02 | [Name] | [S-ID] | [S-ID] | [Why a practitioner would trigger this operation] |
[All operations that appear in COMPILER: TRACE must be declared here first with an Op ID.]

Invariants:
| INV ID | Invariant Statement | Scope | Violation Consequence |
|--------|--------------------|----|----------------------|
| INV-01 | [Precisely stated invariant] | [Specific states or "all states"] | [What breaks in production if violated] |
[Minimum 1 row. Add INV-02 and beyond as the domain warrants.]

Domain Expert gate:
[ ] Entity and domain named with domain vocabulary -- no generic placeholders
[ ] All states have entry conditions and domain-language descriptions
[ ] All valid transitions declared with Op IDs before any trace steps are written
[ ] At least one invariant declared with scope and violation consequence

---

## COMPILER: TRACE

[Read-only on the Domain Expert tables. Reference states by S-ID and operations by OP-ID.
Do not add states or operations not declared above. Flag any gap as an anomaly note.]

Operation trace:
| Step | Before-State (S-ID: Name) | Operation (OP-ID: Name) | Preconditions (state-specific, one per line) | After-State (S-ID: Name) | Postconditions (one per line) | INV Check |
|------|--------------------------|------------------------|---------------------------------------------|--------------------------|------------------------------|-----------|
| 1 | [S-ID: State Name] | [OP-ID: Operation] | - [Precondition 1]<br>- [Precondition 2] | [S-ID: State Name] | - [Postcondition 1] | INV-01: pass |
| 2 | [S-ID: State Name] | [OP-ID: Operation] | - [Precondition 1] | [S-ID: State Name] | - [Postcondition 1] | INV-01: pass |
[Minimum 4 happy-path steps. Every S-ID must reference a state declared in DOMAIN EXPERT.]

Rejected transitions:
| Step | Before-State (S-ID: Name) | Attempted Op (OP-ID or "undeclared") | Failing Precondition | Rejection Behavior | After-State (S-ID: Name) |
|------|--------------------------|--------------------------------------|--------------------|--------------------|--------------------------|
| [N] | [S-ID: State Name] | [OP-ID: Name] | [Specific precondition not met] | [reject / error / exception -- state unchanged] | [Same S-ID: Name] |
[Minimum 1 row.]

Compiler gate:
[ ] Every step has non-blank Before-State (with S-ID), Operation (with OP-ID), state-specific
    Preconditions, After-State (with S-ID), Postconditions, INV Check
[ ] Every S-ID in the trace references a declared state
[ ] At least 1 rejected transition with named failing precondition
[ ] No states or operations introduced that were not declared in DOMAIN EXPERT

---

## ANOMALY FINDER: REVIEW

[Sweep the Compiler's trace for all four anomaly types. Every type row requires a verdict.
"None found" is a valid verdict -- but the row must be present and the evaluation must have
occurred.]

Anomaly sweep:
| Anomaly Type | Sweep Question | Verdict | Op + State (if found) | Production Consequence (if found) |
|-------------|---------------|---------|----------------------|----------------------------------|
| Invalid transition | Does any step cross a transition not in DOMAIN EXPERT valid-transitions? | found / none | [OP-ID at S-ID, or --] | [Consequence, or --] |
| Missing precondition check | Is any step's precondition unlikely to be enforced at the system boundary? | found / none | [OP-ID at S-ID, or --] | [Consequence, or --] |
| Invariant violation | Does any step or sequence produce an INV Check: VIOLATION, or could it under any ordering? | found / none | [INV-ID + OP-ID, or --] | [Consequence, or --] |
| Race condition | Can two operations on the same entity conflict if concurrent? | found / none | [OP-A + OP-B at S-ID, or --] | [Consequence, or --] |

Race condition detail (complete if verdict = found):
  Concurrent ops:  [OP-A (OP-ID)] and [OP-B (OP-ID)] on entity in state [S-ID: Name]
  Interleave:      [Sequence -- which reads and writes happen in which order, and where they conflict]
  Resolution:      [Which operation wins, or how the conflict is detected and the entity's final state]

Anomaly register:
| ID | Type | Op + State | Description | Severity |
|----|------|-----------|-------------|---------|
| A-01 | [invalid-transition / missing-precondition-check / invariant-violation / race-condition] | [OP-ID at S-ID] | [Specific description] | HIGH / MEDIUM / LOW |
[Minimum 1 row. Every row from the sweep table where verdict = "found" must appear here.]

---

Write artifact: simulations/trace/state/{topic}-state-{date}.md
Frontmatter: skill, topic, date, domain, entity, state_count, operation_count, anomaly_count,
             anomaly_types (list), invariant_count, race_condition_analyzed (true/false),
             rejected_transitions (count).
```

---

## V-05: Lifecycle Emphasis + Phrasing Register

**Axes:** Lifecycle emphasis (four explicit phases -- SETUP / DECLARE / COMPILE / REVIEW -- with
hard checklist gate conditions between them; each phase has a named rubric responsibility) +
phrasing register (conversational within phases, goals framed as questions and narrative, not
compliance directives).

**Hypothesis:** Explicit lifecycle phases with named gate conditions enforce the rubric's
sequential dependencies better than section headers alone. GATE 2 locks the state machine after
DECLARE -- preventing mid-trace domain model drift, which is the state-analysis equivalent of
goalpost movement. GATE 3 enforces trace completeness before anomaly review begins. PHASE 4 is
explicitly structured around all four anomaly types, making the per-type sweep a phase design
element rather than a bonus instruction. Conversational register within phases keeps the output
readable for a dev audience reviewing the trace narrative.

```
You are running /trace-state.
Four phases execute in order. Each phase gate lists what must be true before the next phase begins.
The DECLARE phase output is locked after GATE 2 -- do not modify states, transitions, or invariants
in COMPILE or REVIEW. If the trace reveals a gap, note it as a finding, not a retroactive edit.

---

## PHASE 1: SETUP

The goal here is to understand the territory before mapping anything. Look around before you declare.

Check what prior investigation exists. Search simulations/trace/ and simulations/scout/ for any
prior state, request, or contract artifacts related to this topic. List what you find with a
one-line summary. If you find nothing, say so explicitly -- a trace starting from zero is a
different signal than one building on prior work.

Prior signals: [list files with one-line summaries, or "None -- starting fresh."]

Now name the entity and pick its domain. The entity should have a name a practitioner in that
domain would use -- the kind of name that appears in a CRM dropdown, a helpdesk queue, or an ERP
status field, not a design document. The domain is Sales, Customer Service, or Finance. Write one
sentence on why this entity has a meaningful lifecycle in this domain: what business process does
its state machine reflect?

Entity: [domain-realistic name]
Domain: [Sales / Customer Service / Finance]
Why the lifecycle matters: [One sentence -- what business problem does this entity's state
machine address?]

GATE 1 -- required before PHASE 2:
[ ] Prior signal state is declared (found or empty -- not silent)
[ ] Entity named with domain vocabulary (not a generic placeholder)
[ ] Domain selected and one-sentence context written

---

## PHASE 2: DECLARE

Now map the state machine. Everything declared in this phase is locked after GATE 2. COMPILE and
REVIEW phases read it, they do not modify it. If the trace reveals that a state or transition is
missing, that gap is a finding -- not a retroactive addition to this section.

What states can this entity be in? For each state, describe what it means in domain language --
the kind of description that would appear in a status field tooltip, not a technical spec.
Mark which states are terminal.

What operations move the entity between states? For each operation, name the state it starts from
and the state it moves to. If two operations do the same work from different starting states, name
them separately -- the state graph is the contract. An operation not listed here is not valid.

What invariants must hold? An invariant is a mechanical guarantee the system must enforce
regardless of user intent or sequence of operations. It is not a business rule. State each one
as a complete sentence with explicit scope ("always", "in states X and Y", "after operation Z
has been applied at least once"). Name what breaks in production if the invariant is violated.

States:
[List each state. Use domain names -- not "State-1", not "Pending" if the domain uses something
more specific. Minimum 4. Mark terminal states explicitly.]

Valid transitions:
[List every allowed operation with its from/to state pair. Format:
"[operation-name]: [FROM STATE] to [TO STATE]"
An operation not in this list is not valid.]

Invariants:
[At least one. Stated as a complete sentence with scope and violation consequence.
Example: "INV-01 (all states after approval): An Approved invoice cannot be edited -- only voided
and reissued. Violation consequence: financial controls break; audit trail is corrupted."]

GATE 2 -- required before PHASE 3:
[ ] At least 4 states declared with domain-language descriptions and terminal flags
[ ] All valid transitions listed (from/to state pairs for every operation in scope)
[ ] At least one invariant stated with scope and violation consequence
[ ] State machine is complete -- no states, transitions, or invariants will be added in COMPILE
    or REVIEW; gaps discovered later become findings

---

## PHASE 3: COMPILE

This is the hand-compilation phase. Walk the entity through a realistic scenario, step by step.
Number every step. The reader should be able to follow the entity's exact state at every moment
without inference -- every step must stand alone.

For each step, answer these questions explicitly:
- What state is the entity in right now? Use the state name from DECLARE.
- What operation is about to be applied? Use the operation name from DECLARE.
- What must be true before this operation can execute? Name conditions tied to this entity's
  current state -- not generic validations like "user is logged in" or "form is complete", but
  conditions specific to the domain state. "Opportunity must be in Qualified state" counts.
  "Data must be valid" does not.
- What state will the entity be in after the operation?
- What is guaranteed to be true about the entity after the operation? Postconditions -- not just
  the new state label.
- Do the invariants from DECLARE still hold? Check each one explicitly at each step.

After tracing at least four steps on the main path, trace at least one rejected transition: pick
a state and attempt an operation that is not valid from there. Document which precondition fails,
what the system should do (reject, not silently accept), and confirm the entity's state is
unchanged after the rejection.

Step 1:
  Before-State:    [State name from DECLARE]
  Operation:       [Operation name from DECLARE valid transitions]
  Preconditions:   [State-specific conditions -- one per line, domain-grounded]
  After-State:     [State name from DECLARE]
  Postconditions:  [What is guaranteed about the entity now -- one per line]
  Invariants:      [INV-01: pass / VIOLATION -- if violation, describe what was broken and how]

[Repeat for each step. Minimum 4 happy-path steps.]

Rejected transition:
  Before-State:    [State name from DECLARE]
  Attempted op:    [Operation name -- either not in valid-transitions from this state, or
                   precondition not met]
  Failing precond: [Specific precondition text from DECLARE or from this step that is not met]
  System response: [Operation is rejected. State is unchanged. What does the system return?]
  After-State:     [Same as Before-State]

GATE 3 -- required before PHASE 4:
[ ] Every step has Before-State, Operation, state-specific Preconditions, After-State,
    Postconditions, and explicit Invariant check
[ ] At least one rejected transition with named failing precondition
[ ] No states or operations introduced that were not in DECLARE -- gaps are flagged as notes
    for PHASE 4, not silently added here

---

## PHASE 4: REVIEW

The trace is done. Now review it for what it reveals. Work through each anomaly type explicitly --
do not merge them into a generic "issues found" list. Each type has its own question and its own
answer. "None found" is a valid answer -- but the evaluation must have happened.

**Invalid state transitions:**
Look at the DECLARE transition map. Does any step in the COMPILE trace move the entity between
states not listed there? Are there sequences of individually-valid steps that reach an unexpected
or unauthorized state? Does the combination of operations in the trace reveal a path the Domain
Expert's map did not anticipate?
Finding: [Describe the specific step or sequence and why it violates the declared transition map.
Name the operation and the state IDs involved. Or write "None found."]

**Missing precondition checks:**
Review the preconditions listed in each COMPILE step. Are any of them unlikely to be enforced
at the system boundary? Look for preconditions that require data the system does not have at
execution time, conditions that must be evaluated at a different architectural layer, or checks
that are implied by an invariant but never surfaced as an explicit gate.
Finding: [Describe the operation, the missing check, and why the implementation is likely to
skip it. Or write "None found."]

**Invariant violations:**
Review the invariants from DECLARE and the invariant checks from each COMPILE step. Is there any
sequence of operations -- including sequences not in the main trace -- that leaves an invariant
false? Does any concurrent execution scenario create a window where an invariant is temporarily
or permanently broken?
Finding: [Describe the violating sequence and which invariant it breaks. Name the operations and
the state where the violation occurs. Or write "None found."]

**Race conditions:**
Is there any pair of operations in the COMPILE trace that a user or automated process could apply
concurrently to the same entity? If so: name both operations, describe the interleave (which reads
and writes happen in which order, and where they conflict), identify the resulting state corruption
or conflict, and describe how the system should detect or resolve it. What is the correct final
state if both operations are attempted simultaneously?
Finding: [Name both operations, the problematic interleave, the resulting conflict, and the
resolution. Or write "None found -- [reason the domain model prevents concurrency]."]

Findings summary:
| ID | Type | Where (operation + state) | What could go wrong in production |
|----|------|--------------------------|----------------------------------|
| A-01 | [invalid-transition / missing-precondition-check / invariant-violation / race-condition] | [operation at state] | [Production risk description] |
[Minimum 1 row. Every finding from the four sections above must appear here.]

---

Write artifact: simulations/trace/state/{topic}-state-{date}.md
Frontmatter: skill, topic, date, domain, entity, state_count, operation_count, anomaly_count,
             anomaly_types (list), invariant_count, race_condition_analyzed (true/false),
             phase2_locked (true), rejected_transitions (count).
```

---

## Round 1 Design Notes

### Variation axis selection

Three single-axis variations chosen:

- **Output format** (V-01): Highest structural coverage of aspirational criteria C-09/C-10.
  Pre-printed table columns make state-machine notation (C-10) and anomaly-type categorization
  (C-09) structurally unavoidable. The anomaly-type column is a particularly direct C-09 gate:
  the model cannot write an anomaly row without selecting from the four valid types. Chosen as
  the "maximum structural enforcement" baseline for single-axis.

- **Phrasing register** (V-02): Control variation. Tests whether question-driven prose achieves
  rubric compliance without structural enforcement. Expected to score well on essential criteria
  (C-01 through C-05), weakly on C-09/C-10 (no table mandate), and moderately on C-07 (Step 4
  explicitly requests numbered steps). Its score reveals how much structural enforcement is
  actually needed for this skill.

- **Role sequence** (V-03): Addresses the primary failure mode specific to trace-state: happy-path
  collapse. Most traces document the forward path and never pause to hunt anomalies. The Anomaly
  Finder role is the structural gate that separates trace execution from anomaly review. The Domain
  Expert gate is the C-05 enforcement mechanism -- domain vocabulary is locked before any operation
  is named. Expected to score strongly on C-04, C-05, and C-09; weakly on C-10 (no table mandate).

Two combination variations:

- **V-04 (Output format + role sequence)**: Roles enforce correct role responsibilities; tables
  enforce column-level rubric coverage within each role. This is the highest-structure variation.
  The Anomaly Finder sweep table is the most direct C-09 structural enforcement in all five
  variations -- four rows, one per anomaly type, each requiring a verdict. The Domain Expert table
  is the most direct C-10 enforcement -- structured state machine with entry conditions and Op IDs.

- **V-05 (Lifecycle emphasis + phrasing register)**: Lifecycle gates are the most direct enforcement
  of DECLARE-before-COMPILE ordering (which mirrors the "no goalpost movement" constraint from
  prove-hypothesis). GATE 2 explicitly locks the state machine -- the Compiler cannot add states
  mid-trace. PHASE 4's per-type sub-headings enforce the anomaly sweep conversationally rather
  than through a table. This is the second-highest-structure variation for C-04/C-09 and the
  strongest for preventing domain model drift mid-trace.

### C-05 (domain grounding) coverage comparison

| V | How C-05 is enforced |
|---|---------------------|
| V-01 | Column requirement: "Domain Description" column forces domain-language descriptions; prompt text calls out generic names by example |
| V-02 | Question phrasing: Step 2 asks for practitioner vocabulary, gives examples of what passes |
| V-03 | Role gate: Domain Expert gate checklist item explicitly rejects generic placeholders |
| V-04 | Role gate + column: Domain Expert gate checklist + Domain Description column in state machine table |
| V-05 | Phase gate: GATE 1 requires entity named with domain vocabulary; DECLARE phase instructs domain-language descriptions for states |

V-03 and V-04 have the strongest C-05 enforcement (gate checklist item that explicitly rejects
generic placeholders). V-05 is close (GATE 1 checklist). V-01 and V-02 rely on column framing
and question phrasing -- weakest enforcement.

### Predicted differentiation on aspirational criteria

| | C-09 (all four anomaly types) | C-10 (structured notation) |
|-|-----------------------------|---------------------------|
| V-01 | Anomaly-type required column + anomaly register table | State machine table with S-IDs + valid-transitions table |
| V-02 | Step 6 lists all four types but no structural enforcement | No table mandate -- model discretion |
| V-03 | Anomaly Finder has explicit per-type section (four sections) | No table mandate in Domain Expert declare |
| V-04 | Anomaly sweep table: four rows, one per type, each requiring a verdict | State machine table + valid-transitions table with Op IDs |
| V-05 | PHASE 4 has four explicit sub-headings, one per type | No table mandate -- prose format within phases |

V-04 has the richest C-09 surface (sweep table forces four verdicts) and the richest C-10 surface
(state machine table + transitions table with Op IDs + entry conditions). V-01 is close on C-10.
V-03 and V-05 are structurally strong on C-09 (per-type sections) but weaker on C-10.

### Open research questions for R2

1. Does the Domain Expert role gate (V-03/V-04) produce materially better C-05 compliance
   (domain-realistic vocabulary) than the column mandate (V-01) or the question phrasing (V-02)?
   The gate is a checklist item; the column is a template slot; the question is a nudge.
   Compliance differences are only measurable on live model runs.

2. Does the Anomaly Finder sweep table (V-04) produce better C-09 coverage than the per-type
   sub-headings (V-03/V-05)? The sweep table forces a verdict for every type including "none
   found" -- the sub-heading approach requires the model to recognize when a type is absent
   and produce an explicit negative. These are different cognitive tasks.

3. Does GATE 2 (V-05) prevent mid-trace domain model drift more reliably than the Domain Expert
   role gate (V-03/V-04)? Both are gate conditions, but V-05's gate language is more explicit:
   "no states or transitions will be added in COMPILE -- gaps become findings." This is testable
   on live runs by counting whether states appear in the trace that were not in the declared set.
