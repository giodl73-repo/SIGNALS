# trace-state Variate — Round 1 (rubric v17)
**Date:** 2026-03-15
**Rubric:** v17 (C-01 through C-10; golden threshold: all 5 essential pass AND composite >= 80)
**New criteria vs v1:** C-09 now requires all four elements (invalid start state, blocked op, unchanged end state, named error/guard). C-10 is new: reachability annotation with every omitted transition listed with rationale.

---

## Round 1 Variation Map

| Var | Axis | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | Hypothesis |
|-----|------|------|------|------|------|------|------|------|------|------|------|------------|
| V-01 | Output format — reachability-first layout | exp | exp | exp | exp | exp | exp | ? | ? | ? | exp | Pre-declaring the full reachability map before any trace row forces C-10 to be structural, not an afterthought, and anchors C-01 completeness by naming all transitions upfront |
| V-02 | Lifecycle emphasis — negative path promoted to first-class section | exp | exp | exp | exp | exp | ? | ? | ? | exp | ? | Giving the negative path its own dedicated format (peer to the happy path, not an appendix) forces all four C-09 elements because the writer fills a template rather than retrofitting findings |
| V-03 | Phrasing register — per-criterion call-outs embedded in instructions | exp | exp | exp | exp | exp | exp | exp | ? | exp | exp | Naming each rubric criterion inline at the point of satisfaction gives the writer a checklist during production, reducing the gap between "I thought I included that" and verifiable coverage |
| V-04 | Combined: role sequence + lifecycle emphasis — two-expert model (Domain Expert + Concurrency Analyst) | exp | exp | exp | exp | exp | exp | exp | exp | exp | exp | A dedicated Concurrency Analyst role owns C-08 and C-09 exclusively; domain expert cannot dilute that section by leaving it as an afterthought in findings |
| V-05 | Combined: output format + inertia framing + reachability annotation | exp | exp | exp | exp | exp | exp | exp | exp | exp | exp | Three mutually-reinforcing structures: reachability grid forces C-10, inertia challenge seeds C-09 candidate rows, mandatory transition table enforces C-01/C-02/C-03/C-06 |

`exp` = expected PASS based on structural guarantee. `?` = uncertain, depends on execution depth.

---

## V-01 — Output Format: Reachability-First Layout

**Axis:** Output format (reachability map as opening section, not closing annotation)
**Hypothesis:** Starting with a complete reachability map — a grid of every state × every operation labeled TRACED / SKIP-[reason] / ILLEGAL — forces the writer to commit to scope before a single trace row is written. C-10 becomes structural (the grid must be filled) rather than aspirational (remembered at the end). As a side effect, the grid also anchors C-01 completeness: every TRACED row must appear in the transition table, making omissions visible by grid-to-table mismatch.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. The opening deliverable is a reachability map — a complete coverage grid of every state and operation. The transition table fills in exactly the cells marked TRACED. This ordering is mandatory: map first, trace second.

---

### ROLES

Auto-select one domain expert role from context:
- **Sales Expert** — Lead / Qualified Lead / Opportunity / Proposal / Closed Won / Closed Lost lifecycle
- **Customer Service Expert** — New / Active / On Hold / Pending / Resolved / Closed; SLA timers
- **Finance Expert** — Draft / Submitted / Approved / Posted / Paid / Voided; journal/ledger/payment lifecycle

One **Trace Developer** who fills the reachability map and executes the transition table.

---

### STEP 1 — ENTITY AND STATE VOCABULARY

Name the entity and list every state in its lifecycle.

**Entity:** [name and entity type]
**Domain:** [Sales | Customer Service | Finance]

| State Name | Defining Field Values | Entry Conditions | Terminal? |
|-----------|---------------------|-----------------|-----------|

State names must use domain vocabulary. No generic labels ("State A", "initial state").

---

### STEP 2 — OPERATION REGISTRY

List every legal operation that transitions this entity.

| Operation Name | Legal Source States | Target State | Triggering Actor |
|---------------|-------------------|-------------|-----------------|

---

### STEP 3 — INVARIANT DECLARATION

Declare at least two domain invariants before the reachability map. Invariants must encode specific business rules — not generic structural assertions.

| ID | Invariant Name | Checkable Assertion | Authority Source |
|----|---------------|--------------------|--------------------|

Authority source: business rule name, SLA contract clause, accounting regulation, or policy.

---

### STEP 4 — REACHABILITY MAP

Fill a coverage grid: rows = states, columns = operations. For every cell:
- **TRACED** — this transition will appear in the STEP 5 transition table
- **SKIP — [reason]** — intentionally excluded; reason must be one of: out-of-scope, terminal-state, illegal (with the blocking rule named), or deferred
- **ILLEGAL — [rule]** — platform enforces this cannot happen; name the blocking guard

| State \ Operation | [Op 1] | [Op 2] | [Op 3] | ... |
|------------------|--------|--------|--------|-----|
| [State 1]        |        |        |        |     |
| [State 2]        |        |        |        |     |
| ...              |        |        |        |     |

**Coverage rule:** Every cell must have a label. Silent omissions are not permitted. After filling the grid, state the total: TRACED=N, SKIP=N, ILLEGAL=N.

---

### STEP 5 — TRANSITION TABLE

Trace every row marked TRACED in the STEP 4 grid, in operation order. Every cell is required.

**Scenario setup:** [entity instance, starting state, actor, date/time context]

| # | From State | Operation | Preconditions | To State | Postconditions | INV-01 | INV-02 | Side Effects |
|---|-----------|-----------|---------------|---------|----------------|--------|--------|--------------|

**Fill rules:**
- **From State / To State:** Use state vocabulary from STEP 1. No generic labels.
- **Preconditions:** At least one checkable assertion per row (`status == Active`, `assignee != null`).
- **Postconditions:** At least one assertion distinct from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED — [reason]`. Never blank.
- **Side Effects:** Triggered plugins, business rules, related record changes, notifications.

---

### STEP 6 — NEGATIVE PATH TRACE

Trace at least one operation attempted from an invalid starting state.

| # | Invalid Start State | Attempted Operation | Blocking Precondition or Guard | Resulting State | Error Signal or Guard Name |
|---|--------------------|--------------------|-------------------------------|----------------|---------------------------|

**Required elements per row:** (1) the invalid starting state — state the record is in when the operation is attempted, (2) the blocked operation — what was attempted, (3) the resulting state — confirm it is unchanged, (4) the named error or guard — the specific precondition, validation rule, or error message that fires.

---

### STEP 7 — RACE CONDITIONS

Identify concurrent access risks, or explicitly clear them.

| Operation A | Operation B | Unsafe Interleaving | Outcome |
|------------|------------|-------------------|---------|

If cleared: state "No concurrent access — [reason]."

---

### STEP 8 — FINDINGS

Priority-ordered findings. Reference grid cell (state × operation) and table row numbers.

- **P[N] [type]:** [title] — [description]

Types: INVALID-TRANSITION | MISSING-PRECONDITION-GUARD | INVARIANT-VIOLATION | RACE-CONDITION

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: Entity + State Vocabulary, Operation Registry, Invariant Declaration, Reachability Map (with coverage totals), Transition Table, Negative Path Trace, Race Conditions, Findings.

---

## V-02 — Lifecycle Emphasis: Negative Path as First-Class Section

**Axis:** Lifecycle emphasis (negative path section elevated to peer of happy path, not appendix)
**Hypothesis:** In most state machine tracing prompts, the negative path is a section at the end — an "adversarial review" or "invalid transitions" appendix that gets filled in lightly after the main trace is done. This placement causes C-09 failures because the writer has used up attention budget before reaching it. Elevating the negative path to a peer section — with its own scenario setup, step format, and four-element template — causes all four C-09 elements to be present because the format demands them, not because the writer remembers to include them.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace with two parallel paths of equal weight: the forward path (operations that succeed) and the negative path (operations that are blocked). Both paths are first-class. Neither is a summary or appendix of the other.

---

### ROLES

Auto-select one domain expert role from context:
- **Sales Expert** — Lead / Qualified Lead / Opportunity / Proposal / Closed Won / Closed Lost
- **Customer Service Expert** — New / Active / On Hold / Pending / Resolved / Closed; SLA timers
- **Finance Expert** — Draft / Submitted / Approved / Posted / Paid / Voided

One **Trace Developer** who executes both paths and identifies concurrency risks.

---

### STEP 1 — STATE MACHINE DEFINITION

**Entity:** [name and entity type]
**Domain:** [Sales | Customer Service | Finance]

State vocabulary:

| State Name | Defining Field Values | Terminal? |
|-----------|---------------------|-----------|

Operation registry:

| Operation Name | Legal Source States | Target State |
|---------------|-------------------|-------------|

Invariants (at least two; domain-specific business rules, not structural assertions):

| ID | Name | Checkable Assertion | Authority Source |
|----|------|--------------------|--------|

---

### STEP 2 — FORWARD PATH TRACE

Choose a realistic concrete scenario. State the scenario setup, then trace each operation.

**Scenario:** [entity instance, starting state, actor, context]

Per-operation format:

```
OPERATION [N]: [operation name]
  Starting state:   [state name] — [key field values]
  Preconditions:    [testable assertions — "status == Active", "role == Case Resolver"]
  Processing:       [plugins, business rules, calculations that execute]
  Ending state:     [state name] — [key field values]
  Postconditions:   [assertions about ending state, distinct from state name]
  Side effects:     [related records, notifications, async jobs]
  Invariant check:
    - [INV-ID] [name]: HOLDS | VIOLATED — [reason]
    (check every declared invariant)
```

---

### STEP 3 — NEGATIVE PATH TRACE

Trace at least two operations attempted from invalid starting states. These are **not** edge cases or exceptions to the forward path — they are a parallel scenario of their own, with dedicated scenario setup.

**Negative scenario:** [entity instance, who is attempting the invalid operation, why they might try it]

Per-blocked-operation format:

```
BLOCKED OPERATION [N]: [operation name]
  Invalid starting state:   [state name] — [key field values; why this is the wrong state]
  Attempted operation:      [exact operation name from registry]
  Blocking condition:       [which precondition fails, which invariant would be violated, or which guard fires]
  Resulting state:          [state name — UNCHANGED; confirm it matches Invalid starting state]
  Error signal or guard:    [specific error message, guard name, exception type, or validation rule name]
  Why someone tries this:   [realistic user or integration scenario that leads to this attempt]
```

At least one blocked operation must trace an invariant violation (not just a missing precondition).

---

### STEP 4 — RACE CONDITIONS

For each operation in the forward path that could be invoked by two actors concurrently:

| Operation | Actor A | Actor B | Unsafe Interleaving | Conflicting State | Resolution or Risk |
|-----------|--------|--------|-------------------|------------------|-------------------|

If no concurrent access is possible for any operation, state this explicitly for each: "Operation [N] — no concurrent risk because [reason]."

---

### STEP 5 — DEFECT SUMMARY

Consolidate findings from STEP 3 and STEP 4. Label each defect by type.

| # | Defect Type | Triggering Operation | State at Trigger | Reason It Is a Defect |
|---|------------|---------------------|-----------------|----------------------|

Defect types: INVALID-TRANSITION | MISSING-PRECONDITION-GUARD | INVARIANT-VIOLATION | RACE-CONDITION

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: State Machine Definition (vocabulary, operations, invariants), Forward Path Trace, Negative Path Trace, Race Conditions, Defect Summary.

---

## V-03 — Phrasing Register: Per-Criterion Call-Outs Embedded in Instructions

**Axis:** Phrasing register (rubric criteria named inline at their point of satisfaction)
**Hypothesis:** When a prompt names the criterion being satisfied at exactly the point in the format where it must be provided — e.g., "Preconditions (this satisfies C-02)" — the writer has a continuous checklist embedded in the task itself. They cannot finish the trace believing they satisfied a criterion they actually skipped. This reduces the gap between a writer who understands the rubric abstractly and one who executes it consistently. Particularly valuable for C-09 four-element completeness and C-10 which writers routinely treat as optional.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace: per-operation transitions with preconditions, postconditions, and invariant checks, plus defect identification and coverage annotation. The format below is calibrated to produce a complete, scorable signal artifact; each section notes which quality criterion it satisfies.

---

### ROLES

Auto-select from context:
- **Sales Expert** — Lead → Opportunity → Close lifecycle; Quote and Order states
- **Customer Service Expert** — Case lifecycle; SLA timers; escalation states
- **Finance Expert** — Journal → Ledger → Payment lifecycle; Approval and Void states

One **Trace Developer** who executes the trace and adversarial sections.

---

### SECTION 1 — ENTITY AND STATE VOCABULARY

*(Satisfies: C-05 — domain plausibility)*

**Entity:** [name and entity type, e.g., "Opportunity (sales record), Dynamics 365 Sales"]
**Domain:** [Sales | Customer Service | Finance]

List every named state in the lifecycle. Use domain vocabulary throughout — no generic labels.

| State Name | Defining Field Values | Entry Conditions | Terminal? |
|-----------|---------------------|-----------------|-----------|

List every legal operation:

| Operation Name | Legal Source States | Target State | Triggering Actor |
|---------------|-------------------|-------------|-----------------|

---

### SECTION 2 — INVARIANT DECLARATION

*(Satisfies: C-03 — declared; must also be checked per operation. Satisfies C-07 if business-rule-sourced)*

Name at least two invariants. Each must encode a specific business rule — not a generic structural assertion. State the authority source (business rule, SLA clause, regulation, policy).

| ID | Name | Checkable Assertion | Authority Source |
|----|------|--------------------|-----------------|

**Non-qualifying examples** (do not use): "state must be valid", "entity must exist", "id is not null".
**Qualifying examples**: "total_amount >= sum_of_line_items at all times", "SLA timer is paused when status == On Hold".

---

### SECTION 3 — PER-OPERATION TRACE

*(Satisfies: C-01 — starting state + operation + ending state per row. C-02 — preconditions + postconditions per operation. C-03 — invariant check per operation. C-06 — consistent format throughout)*

**Scenario:** [entity instance, starting state, actor, date/time context]

Per-operation format — every field is required for every operation:

```
OPERATION [N]: [operation name from registry]

  Starting state (C-01a):    [state name] — [key field values]

  Preconditions (C-02a):
    - [testable assertion: "field == value", "record exists", "user has role X"]
    - [additional preconditions as needed]

  Processing:                [plugins, business rules, calculations, messages that fire]

  Ending state (C-01b):      [state name] — [key field values after transition]

  Postconditions (C-02b):
    - [testable assertion about ending state, distinct from state name]

  Side effects:              [related records, notifications, async jobs]

  Invariant check (C-03):
    - [INV-ID] [name]: HOLDS | VIOLATED — [reason]
    (check every invariant from SECTION 2 per operation — never skip)
```

---

### SECTION 4 — DEFECT IDENTIFICATION

*(Satisfies: C-04 — labeled defect with type, triggering operation, and reason)*

At least one defect is required. Label by type.

| # | Defect Type | Triggering Operation | Starting State at Trigger | Reason It Is a Defect |
|---|------------|---------------------|--------------------------|----------------------|

Defect types: INVALID-TRANSITION | MISSING-PRECONDITION-GUARD | INVARIANT-VIOLATION | RACE-CONDITION

---

### SECTION 5 — NEGATIVE PATH TRACE

*(Satisfies: C-09 — all four elements required: invalid start state, blocked operation, unchanged resulting state, named error or guard)*

Trace at least one blocked operation. All four elements must be present for every row.

| Element | Value |
|---------|-------|
| (1) Invalid start state | [state name — the record is in this state when the operation is attempted] |
| (2) Blocked operation | [exact operation name from registry] |
| (3) Resulting state | [state name — CONFIRM it is unchanged from the invalid start state] |
| (4) Named error or guard | [specific error message, guard name, exception type, or platform validation rule] |

Add additional blocked operations as warranted by the state machine.

---

### SECTION 6 — RACE CONDITIONS

*(Satisfies: C-08 — one concurrent interleaving with conflict or resolution named)*

Identify at least one operation that could be invoked concurrently by two actors. For each:

| Operation | Interleaving | Conflicting State | Outcome or Resolution |
|-----------|-------------|-----------------|----------------------|

If no concurrent risk: state "No concurrent access — [reason]" for each operation.

---

### SECTION 7 — REACHABILITY ANNOTATION

*(Satisfies: C-10 — every omitted transition listed with rationale; silent omissions do not qualify)*

List all transitions traced in SECTION 3, then list every omitted transition with a stated reason.

**Transitions traced:**
- [Operation N: State A → State B]

**Transitions omitted:**

| Omitted Transition | Rationale |
|-------------------|-----------|

Rationale options: out-of-scope for this trace, terminal state (cannot exit), illegal (platform blocks — name the rule), deferred to separate trace.

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: Entity + State Vocabulary, Invariants, Per-Operation Trace, Defect Identification, Negative Path Trace, Race Conditions, Reachability Annotation.

---

## V-04 — Combined: Role Sequence + Lifecycle Emphasis — Two-Expert Model

**Axes:** Role sequence (Domain Expert + Concurrency Analyst as separate roles) + Lifecycle emphasis (concurrency and negative path owned by dedicated expert, not developer)
**Hypothesis:** In single-expert or expert-plus-developer models, the concurrency analysis and negative path sections are owned by the Developer role, who tends to underweight them relative to the forward trace. Splitting into three roles — Domain Expert (state machine + invariants), Trace Developer (forward path), Concurrency Analyst (negative path + race conditions) — gives C-08 and C-09 a dedicated owner whose entire job is those sections. The Concurrency Analyst cannot defer to findings because they have no other sections to complete. This structural pressure should produce consistent C-08 and C-09 coverage without requiring the developer to context-switch.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace in three owned sections. Each section is owned by a specific role with explicit ownership boundaries. No role executes work outside their section.

---

### ROLES

**[D] Domain Expert**
Auto-selected from context:
- Sales topic → Sales state expert (Lead / Qualified Lead / Opportunity / Proposal / Closed Won / Closed Lost)
- Customer Service topic → CS expert (New / Active / On Hold / Pending / Resolved / Closed; SLA timers)
- Finance topic → Finance expert (Draft / Submitted / Approved / Posted / Paid / Voided)

Owns: STATE MACHINE DEFINITION, INVARIANT DECLARATION.
May not perform: per-operation trace, concurrency analysis, negative path analysis.

**[T] Trace Developer**
Owns: FORWARD PATH TRACE.
May not perform: state vocabulary, invariant declaration, concurrency analysis.

**[C] Concurrency Analyst**
Owns: NEGATIVE PATH TRACE, RACE CONDITION ANALYSIS, DEFECT SYNTHESIS.
May not perform: forward path trace, state vocabulary, invariant declaration.

---

### DOMAIN EXPERT SECTION [D]

#### D1 — Entity and State Vocabulary

**Entity:** [name and entity type]
**Domain:** [Sales | Customer Service | Finance]

| State Name | Defining Field Values | Entry Conditions | Terminal? |
|-----------|---------------------|-----------------|-----------|

State names must use domain vocabulary throughout. No generic labels.

#### D2 — Operation Registry

| Operation Name | Legal Source States | Target State | Triggering Actor |
|---------------|-------------------|-------------|-----------------|

#### D3 — Invariant Registry

Declare at least two domain-specific invariants. Each must encode a real business rule that a generic framework would not automatically enforce.

| ID | Invariant Name | Checkable Assertion | Authority Source |
|----|---------------|--------------------|--------------------|

**D3 Gate:** No forward trace begins until the invariant registry is complete and authority-sourced.

---

### TRACE DEVELOPER SECTION [T]

#### T1 — Scenario Setup

[Entity instance, starting state, actor, date/time context. Specific field values.]

#### T2 — Forward Path Trace

Per-operation format:

```
OPERATION [N]: [operation name from D2 registry]
  Starting state:   [state name] — [key field values]
  Preconditions:
    - [testable assertion]
    - [additional as needed; minimum two per operation]
  Processing:       [plugins, business rules, calculations, messages]
  Ending state:     [state name] — [key field values]
  Postconditions:
    - [assertion distinct from state name; minimum one]
  Side effects:     [related records, notifications, async jobs]
  Invariant check:
    - [INV-ID] [name]: HOLDS | VIOLATED — [reason]
    (check every invariant from D3 per operation)
```

**T2 Gate:** All operations traced before Concurrency Analyst section begins.

---

### CONCURRENCY ANALYST SECTION [C]

The Concurrency Analyst section is not a summary or appendix. It is a parallel analysis of the same state machine under adversarial conditions.

#### C1 — Negative Path Trace

Trace at least two blocked operations. Each must include all four elements — no element may be omitted.

For each blocked operation:

```
BLOCKED OPERATION [N]: [operation name]

  (1) Invalid starting state:
      State name: [state name from D1 vocabulary]
      Field values: [key field values that define this state]
      Why invalid: [which precondition or invariant makes this the wrong state for this operation]

  (2) Attempted operation:
      [exact operation name from D2 registry]

  (3) Resulting state (must be UNCHANGED):
      State name: [same state name as (1) — operation did not execute]
      Field values: [same as (1) — no side effects applied]
      Confirmation: "State is unchanged. Operation did not execute."

  (4) Error signal or guard:
      [Specific error message, guard name, platform validation rule, or exception type]
      [Do not use generic descriptions like "an error fires" or "validation fails"]
```

#### C2 — Race Condition Analysis

For each operation in the forward path that involves a writable state field:

| Operation | Actor A Action | Actor B Concurrent Action | Unsafe Interleaving | State Conflict | Resolution or Risk |
|-----------|--------------|--------------------------|-------------------|--------------|-------------------|

At least one operation must be analyzed with both interleavings described.

If an operation has no concurrent risk: "Operation [N] — no concurrent risk: [specific reason, e.g., 'single-owner lock enforced by platform assignment', 'sequential plugin execution guaranteed']."

#### C3 — Defect Synthesis

Consolidate all defects found in C1 and C2. Priority order.

| Priority | Defect Type | Triggering Operation | State Context | Root Cause |
|---------|------------|---------------------|--------------|------------|

Defect types: INVALID-TRANSITION | MISSING-PRECONDITION-GUARD | INVARIANT-VIOLATION | RACE-CONDITION

---

### REACHABILITY ANNOTATION

All three roles contribute. Fill after C3 is complete.

**Transitions traced in T2:** [list as Operation: State A → State B]

**Transitions omitted:**

| Omitted Transition | Owner Section | Rationale |
|-------------------|--------------|-----------|

Every omission requires a rationale. Options: out-of-scope, terminal state, illegal (name the blocking rule), deferred.

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: Domain Expert (D1, D2, D3), Trace Developer (T1, T2), Concurrency Analyst (C1, C2, C3), Reachability Annotation.

---

## V-05 — Combined: Output Format + Inertia Framing + Reachability Annotation

**Axes:** Output format (structured grid) + Inertia framing (manual process assumptions surfaced first) + Reachability annotation (as closing coverage audit)
**Hypothesis:** Three structures reinforce each other: the inertia challenge surfaces what the manual process assumes but the platform does not enforce — these assumptions are C-09 candidates (blocked operations the platform *should* block but currently might not). The mandatory transition table enforces C-01/C-02/C-03/C-06 structurally. The reachability annotation forces C-10 as a closing audit: the writer reviews the inertia table and the transition table together to confirm every inertia-derived transition was either traced or explicitly skipped. No single axis alone reliably produces all three; together they form a self-checking loop.

---

You are running a **trace-state** signal for: {{topic}}

Produce a full state machine trace in four stages: (1) surface what the current manual process assumes the platform enforces (inertia challenge), (2) declare the state machine and invariants, (3) execute the transition table, (4) audit reachability and confirm what was covered. This ordering is mandatory — the inertia challenge runs before the trace so its findings can seed the negative path and defect identification.

---

### ROLES

**[D] Domain Expert**
Auto-selected: Sales / Customer Service / Finance.
Owns: INERTIA CHALLENGE, STATE MACHINE DEFINITION, INVARIANT DECLARATION.

**[T] Trace Developer**
Owns: TRANSITION TABLE, NEGATIVE PATH TRACE, RACE CONDITIONS, REACHABILITY AUDIT.

---

### STAGE 1 — INERTIA CHALLENGE [D]

Before declaring any formal state machine, answer this question for {{topic}}:

**What does the current process (spreadsheet, email, legacy system, verbal convention, paper form) assume about operation order that the platform may not enforce?**

For each assumption found:

| # | Current Process Assumption | Assumed Platform Behavior | Is It Actually Enforced? | Expected Invalid Transition If Not |
|---|--------------------------|--------------------------|-------------------------|-----------------------------------|

**Guidance:**
- "Everyone knows you don't post until the manager approves" — is this a platform gate or a cultural norm?
- "Finance always voids before re-opening" — is the void step a state machine gate or a manual step?
- "Sales ops confirms qualification before the developer assigns" — is there a precondition check, or just convention?

Each row where "Is It Actually Enforced? = No" is a C-09 candidate. The Trace Developer will use this table to seed the negative path trace in STAGE 3.

---

### STAGE 2 — STATE MACHINE DEFINITION [D]

**Entity:** [name and entity type]
**Domain:** [Sales | Customer Service | Finance]

State vocabulary (domain terms only — no generic labels):

| State Name | Defining Field Values | Entry Conditions | Terminal? |
|-----------|---------------------|-----------------|-----------|

Operation registry:

| Operation Name | Legal Source States | Target State | Triggering Actor |
|---------------|-------------------|-------------|-----------------|

Invariant declaration (at least two; encode business rules, not structural assertions):

| ID | Invariant Name | Checkable Assertion | Authority Source |
|----|---------------|--------------------|--------------------|

**Inertia linkage:** After filling invariants, note which STAGE 1 rows (if any) should become new invariants. Add them to the registry.

---

### STAGE 3 — TRANSITION TABLE AND NEGATIVE PATH [T]

#### 3A — Transition Table

**Scenario setup:** [entity instance, starting state, actor, date/time context]

| # | From State | Operation | Preconditions | To State | Postconditions | INV-01 | INV-02 | Side Effects |
|---|-----------|-----------|---------------|---------|----------------|--------|--------|--------------|

**Fill rules:**
- From State / To State: use state vocabulary from STAGE 2. No generic labels.
- Preconditions: minimum two checkable assertions per row.
- Postconditions: minimum one assertion distinct from the To State name.
- INV columns: `HOLDS` or `VIOLATED — [reason]`. Never blank.
- Side Effects: triggered plugins, business rules, related record changes, notifications.

#### 3B — Negative Path Trace

For each STAGE 1 row where "Is It Actually Enforced? = No," trace the blocked operation. Add any additional blocked operations not surfaced by inertia.

All four elements are required for every row:

| # | (1) Invalid Start State | (2) Attempted Operation | (3) Resulting State (Unchanged) | (4) Error Signal or Guard | STAGE 1 Row Ref |
|---|------------------------|------------------------|--------------------------------|--------------------------|----------------|

**Element definitions:**
1. **Invalid start state** — the state the record is in when the operation is attempted (not a legal source state for this operation)
2. **Attempted operation** — exact operation name from STAGE 2 registry
3. **Resulting state** — confirm it is unchanged; operation did not execute
4. **Error signal or guard** — specific error message, guard name, validation rule, or exception type; not "validation fails"

#### 3C — Race Conditions

| Operation A | Operation B | Unsafe Interleaving | Outcome |
|------------|------------|-------------------|---------|

If cleared per operation: "Operation [N] — no concurrent risk: [specific reason]."

---

### STAGE 4 — REACHABILITY AUDIT [T]

After the transition table and negative path are complete, perform a coverage audit.

**Transitions traced (3A):**
| # | From State | Operation | To State |
|---|-----------|-----------|---------|

**Transitions in negative path (3B):**
| # | Invalid State | Blocked Operation | Guard |
|---|--------------|-----------------|-------|

**Transitions intentionally omitted:**
| From State | Operation | Rationale |
|-----------|-----------|-----------|

Rationale options: out-of-scope for this trace, terminal state, illegal (name blocking rule), deferred. Silent omissions are not acceptable.

**Coverage summary:**
- Total operations in registry: [N]
- Total (state × operation) cells explored: [N]
- TRACED: [N] | BLOCKED (negative path): [N] | OMITTED: [N]

---

### FINDINGS [D + T]

Consolidate defects from 3B and 3C. Reference STAGE 1 rows, table row numbers, and invariant IDs.

| Priority | Defect Type | Triggering Operation | State Context | Root Cause | STAGE 1 Ref |
|---------|------------|---------------------|--------------|------------|------------|

Defect types: INVALID-TRANSITION | MISSING-PRECONDITION-GUARD | INVARIANT-VIOLATION | RACE-CONDITION

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: Inertia Challenge (STAGE 1), State Machine Definition + Invariants (STAGE 2), Transition Table + Negative Path + Race Conditions (STAGE 3), Reachability Audit + Coverage Summary (STAGE 4), Findings.
