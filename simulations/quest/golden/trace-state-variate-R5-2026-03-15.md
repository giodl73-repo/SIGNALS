# trace-state Variate — Round 5
**Date:** 2026-03-15
**Rubric:** v4 (C-01..C-15; golden threshold: all essential pass AND composite >= 80)
**New criteria:** C-14 (cross-table referential integrity) and C-15 (vocabulary lock)
**Scoring formula:** essential 50 + recommended 40 + aspirational 10 (8 criteria, 1.25 pts each)

---

## Round 5 Situation

R1-R4 best scorers all addressed C-08 through C-13. No prior variation directly targets C-14 or C-15 — they were extracted from R4 variation patterns post-hoc and formalized in v4.

C-14 requires an **explicit forward-declared binding rule** ("a state not in Table 1 may not appear in Table 3"). The rule must be stated before tracing begins, not inferred from structure.

C-15 requires an **explicit vocabulary-lock prohibition** ("you may not add any state or operation after this marker"). Implicit ordering does not satisfy it; the prohibition must be written.

**R5 objective:** Structural guarantee for C-14 and C-15. All variations inherit the V-04 R2 baseline (four phases, GATE enforcement, inertia, mandatory tables) — the question is which axis produces the strongest C-14 + C-15 signal without sacrificing C-01 through C-13.

---

## Round 5 Variation Map

| Var | Axis | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | Hypothesis |
|-----|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------------|
| V-01 | Output format — referential binding tables | exp | exp | exp | exp | exp | exp | exp | exp | exp | exp | exp | exp | exp | **exp** | ? | Naming inventory tables "T1" and "T2" and stating the binding rule "a name not in T1 may not appear in T3, T4, T5" makes C-14 structural; C-15 uncertain without explicit closure prohibition |
| V-02 | Lifecycle emphasis — vocabulary lock with hard closure | exp | exp | exp | exp | exp | exp | exp | exp | exp | exp | exp | exp | exp | ? | **exp** | Hard "VOCABULARY CLOSED" marker stated as prohibition after inventory phases makes C-15 structural; C-14 uncertain without explicit binding rule |
| V-03 | Phrasing register — prohibitive constraint framing | exp | exp | exp | exp | exp | exp | exp | exp | exp | exp | exp | exp | exp | **exp** | **exp** | Both constraints stated as explicit YOU MAY NOT prohibitions; C-14 and C-15 are structural because they appear as named rules before any table is filled — but phrasing alone without structure may be fragile |
| V-04 | Combined: output format + vocabulary lock + gate | exp | exp | exp | exp | exp | exp | exp | exp | exp | exp | exp | exp | exp | **exp** | **exp** | Binding rule in T1 header + VOCABULARY CLOSED gate item + GATE C checks C-14 and C-15 by ID — both structural; strongest guarantee of any R5 variation |
| V-05 | Combined: lifecycle emphasis + inertia + vocabulary lock | exp | exp | exp | exp | exp | exp | exp | exp | exp | exp | exp | exp | exp | ? | **exp** | Inertia PHASE B precedes vocabulary closure; after inertia assumptions are named, Domain Expert signs vocabulary closed — C-15 structural via the sign-off; C-14 uncertain unless binding rule is implied by structure |

`exp` = expected PASS based on structural guarantee. `?` = uncertain, depends on execution depth.

---

## V-01 — Output Format: Referential Binding Tables

**Axis:** Output format (single axis)
**Hypothesis:** In R4, the C-14 pattern emerged organically when a variation named its inventory tables and then stated "every state transition in Table 3 must have a named operation in this table." V-01 makes that binding rule explicit, front-declared, and applied to all subsequent tables. The rule appears in the preamble before any table is filled — not as a guideline but as a referential constraint: "T1 is the authoritative state registry. T2 is the authoritative operation registry. Any row in T3, T4, or T5 that names a state or operation not declared in T1 or T2 is invalid output." C-14 is structural because the rule is stated before tracing begins. C-15 remains uncertain: no explicit closure prohibition appears, though the binding rule implies the vocabulary is fixed.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. All trace output is delivered in named tables. Table 1 and Table 2 are the authoritative inventories; all later tables bind to them.

**Referential binding rule — read before filling any table:**

> A state name that does not appear in **Table 1** may not appear in any row of **Table 3**, **Table 4**, or **Table 5**. An operation name that does not appear in **Table 2** may not appear in any row of **Table 3**, **Table 4**, or **Table 5**. A row that introduces an undeclared state or operation is an error in the trace, not a finding.

---

### ROLES

**[D] Domain Expert**
Auto-selected from context: Sales expert (Lead / Qualified Lead / Opportunity / Proposal / Closed Won / Closed Lost), Customer Service expert (New / Active / On Hold / Pending / Resolved / Closed), Finance expert (Draft / Submitted / Approved / Posted / Paid / Voided).
Owns: TABLE 1, TABLE 2, TABLE INV.

**[T] Trace Developer**
Owns: TABLE 3, TABLE 4, TABLE 5, FINDINGS.
Must verify referential binding rule before writing any row: if a state or operation name is not in T1 or T2, stop and flag the gap rather than introducing the term.

---

### TABLE 1 — STATE REGISTRY [D]

This table is the complete state vocabulary for {{topic}}. It is authoritative. No state may appear in any later table that is not declared here.

| State ID | State Name | Defining Field Values | Entry Conditions | Terminal? |
|---------|-----------|----------------------|-----------------|-----------|

**Domain vocabulary required.** No generic labels ("State A", "initial", "final"). At least one row must have Terminal = Yes.

---

### TABLE 2 — OPERATION REGISTRY [D]

This table is the complete operation inventory. It is authoritative. No operation may appear in any later table that is not declared here.

| Operation ID | Operation Name | Legal Source State IDs | Target State ID | Triggering Actor |
|-------------|---------------|----------------------|----------------|-----------------|

**State IDs in columns 3 and 4 must reference TABLE 1 IDs.** An operation that references a state not in Table 1 must not be added — resolve the discrepancy in Table 1 first.

---

### TABLE INV — INVARIANT REGISTRY [D]

| INV ID | Name | Checkable Assertion | Authority Source |
|--------|------|--------------------|--------------------|

Minimum two invariants. Authority source: business rule name, SLA contract clause, accounting regulation, or policy.

---

### GATE A

Before filling TABLE 3: confirm all items.

- [ ] **[C-01]** TABLE 1 contains all states in the lifecycle; no state is implied only by prose
- [ ] **[C-02]** TABLE 2 contains all operations; every legal transition has a named operation
- [ ] **[C-05]** TABLE INV has at least two invariants with checkable assertions
- [ ] **[C-14]** Referential binding rule has been read; Trace Developer confirms: "I will not introduce any state or operation name not declared in T1 or T2"

**Any item unconfirmed → return to relevant table.**

---

### TABLE 3 — TRANSITION TRACE [T]

Scenario setup: [entity instance, starting state, actor, date/time context]

**Every state and operation name in this table must reference T1 or T2. If a needed name is missing from T1 or T2, stop. Do not add it here.**

| # | From State (T1 ID) | Operation (T2 ID) | Preconditions | To State (T1 ID) | Postconditions | INV-01 | INV-02 | Side Effects |
|---|--------------------|-------------------|---------------|-----------------|----------------|--------|--------|--------------|

**Column rules:**
- **From State / To State:** T1 IDs or T1 state names only. Never introduce a name not in T1.
- **Operation:** T2 operation names only. Never introduce an operation name not in T2.
- **Preconditions:** Minimum two testable assertions per row (e.g., `status == Active`, `owner != null`).
- **Postconditions:** Minimum one assertion distinct from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED — [reason]`; never blank.

---

### TABLE 4 — INVALID TRANSITIONS [T]

| # | Attempted Operation (T2 ID) | From State (T1 ID) | Blocking Condition | INV Reference | Risk if Bypassed |
|---|----------------------------|-------------------|--------------------|--------------|-----------------|

**All operation and state references must use T1/T2 IDs.** Minimum one row.

---

### TABLE 5 — RACE CONDITIONS [T]

| Operation A (T2 ID) | Operation B (T2 ID) | Unsafe Interleaving | Outcome |
|--------------------|---------------------|---------------------|---------|

If no concurrent access is possible: "No concurrent access — [reason]."

---

### GATE B

Before writing FINDINGS: confirm all items.

- [ ] **[C-03]** Every TABLE 3 row has at least two preconditions as testable assertions
- [ ] **[C-06]** Every TABLE 3 row has at least one postcondition distinct from the To State name
- [ ] **[C-04]** TABLE 4 has at least three (operation, state) pairs with blocking conditions
- [ ] **[C-07]** TABLE 5 addressed — at least one row OR explicit clearance with reason
- [ ] **[C-08]** TABLE 3 is complete and columnar; no operation exists only in prose
- [ ] **[C-09]** At least one T1 terminal state appears in TABLE 3 as a To State; at least one TABLE 4 row covers a terminal state attempt
- [ ] **[C-14]** All state and operation names in TABLE 3, 4, 5 reference T1 or T2; no undeclared term was introduced

**Any item unconfirmed → return to relevant table.**

---

### BOUNDARY COVERAGE [T]

- **Initial state:** [T1 state name; confirm Terminal = No]
- **Terminal states:** [list all T1 entries with Terminal = Yes]
- **Re-entry blocked:** One attempt to operate from a terminal state. Blocking condition.

---

### FINDINGS

Priority order. Reference table number and row.

- **P[N]:** [title] — [description, T-table row reference]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: TABLE 1 (state registry), TABLE 2 (operation registry), TABLE INV (invariants), GATE A, TABLE 3 (transition trace), TABLE 4 (invalid transitions), TABLE 5 (race conditions), GATE B, BOUNDARY COVERAGE, FINDINGS.

---

## V-02 — Lifecycle Emphasis: Vocabulary Lock with Hard Closure

**Axis:** Lifecycle emphasis (single axis)
**Hypothesis:** In R4, the C-15 pattern emerged from a variation that declared "you may not add operations after Phase 2 closes." V-02 makes that closure a named, standalone lifecycle event — the "VOCABULARY CLOSED" declaration — positioned between the inventory phase and the trace phase. The declaration is stated as a prohibition, not a recommendation: "From this point forward, you may not introduce any new state name or operation name. If a state or operation name needed for the trace is not in the current inventory, stop. Return to the inventory phase, add it there, and then re-close vocabulary before tracing." C-15 is structural because the prohibition is explicit and is placed at a mandatory lifecycle boundary. C-14 is uncertain: no explicit binding rule between tables is stated.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace in strict lifecycle order. Each lifecycle phase must complete before the next begins. The VOCABULARY CLOSED declaration is a mandatory lifecycle event — vocabulary is frozen after inventory and may not expand during tracing.

---

### ROLES

**[D] Domain Expert**
Auto-selected: Sales expert (Lead / Opportunity / Proposal / Closed Won / Closed Lost), CS expert (New / Active / On Hold / Pending / Resolved / Closed), Finance expert (Draft / Submitted / Approved / Posted / Paid / Voided).
Owns: PHASE 1 (state inventory), PHASE 2 (operation and invariant inventory), VOCABULARY CLOSED declaration.

**[T] Trace Developer**
Owns: PHASE 3 (transition trace), PHASE 4 (adversarial review).
May not add any state or operation name not present in PHASE 1 or PHASE 2. If a name is missing, stop and flag to Domain Expert for inventory update before VOCABULARY CLOSED is re-issued.

---

### PHASE 1 — STATE INVENTORY [D]

**Entity:** [name and entity type]
**Domain:** [Sales | Customer Service | Finance]

Every state in this entity's lifecycle, named before any operation is traced.

| State Name | Defining Field Values | Entry Conditions | Terminal? |
|-----------|----------------------|-----------------|-----------|

Domain vocabulary only. No "State A", "initial", "final". At least one terminal state required.

---

### PHASE 1 COMPLETE

Do not begin PHASE 2 until PHASE 1 is complete.

- [ ] All lifecycle states are named with domain vocabulary
- [ ] At least one terminal state is marked Terminal = Yes
- [ ] No state is implied only by prose

**If any item fails → return to PHASE 1.**

---

### PHASE 2 — OPERATION AND INVARIANT INVENTORY [D]

**Operations** — every legal operation that transitions this entity:

| Operation Name | Legal Source States | Target State | Triggering Actor |
|---------------|-------------------|-------------|-----------------|

Source states and target states must use names declared in PHASE 1. No new state names.

**Invariants** — conditions that must hold throughout this entity's lifecycle:

| INV ID | Name | Checkable Assertion | Authority Source |
|--------|------|--------------------|-----------------|

Minimum two invariants. Authority source: business rule name, SLA contract clause, accounting regulation, or policy.

---

### PHASE 2 COMPLETE

Do not issue the VOCABULARY CLOSED declaration until PHASE 2 is complete.

- [ ] **[C-02]** Every operation has enumerated legal source states and a single target state
- [ ] **[C-05]** At least two invariants with checkable assertions and authority sources
- [ ] **[C-12]** All states referenced in the operation table appear in PHASE 1; no new states introduced

**If any item fails → return to PHASE 2.**

---

## VOCABULARY CLOSED

> **Prohibition:** From this point forward, you may not introduce any new state name or operation name. The state vocabulary declared in PHASE 1 and the operation inventory declared in PHASE 2 are now closed.
>
> If a state or operation name needed for PHASE 3 or PHASE 4 is not currently in the inventory, **stop**. Do not proceed. Return to Domain Expert, add the name to the appropriate inventory phase, and re-issue the VOCABULARY CLOSED declaration before tracing resumes.
>
> This prohibition applies to PHASE 3 (transition trace), PHASE 4 (adversarial review), and all findings output.

**Domain Expert confirmation:** [Explicitly state: "Vocabulary is closed. PHASE 1 contains N states. PHASE 2 contains M operations and K invariants. No new states or operations will be introduced in PHASES 3 or 4."]

---

### PHASE 3 — TRANSITION TRACE [T]

Scenario setup: [entity instance, starting state, actor, date/time context]

**State and operation names in this table must come from PHASE 1 and PHASE 2 inventories. VOCABULARY IS CLOSED.**

| # | From State | Operation | Preconditions | To State | Postconditions | INV-01 | INV-02 | Side Effects |
|---|-----------|-----------|---------------|---------|----------------|--------|--------|--------------|

**Column rules:**
- **From State / To State:** PHASE 1 vocabulary only. If you encounter a needed state name not in PHASE 1, stop and follow the VOCABULARY CLOSED protocol above.
- **Operation:** PHASE 2 operation names only. Same stop-and-flag protocol.
- **Preconditions:** Minimum two testable assertions per row.
- **Postconditions:** Minimum one assertion distinct from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED — [reason]`; never blank.
- **Side Effects:** Triggered plugins, business rules, related record changes, notifications.

---

### PHASE 3 COMPLETE

Do not begin PHASE 4 until PHASE 3 is complete.

- [ ] **[C-01]** Every row has a From State and To State from PHASE 1
- [ ] **[C-03]** Every row has at least two preconditions as testable assertions
- [ ] **[C-06]** Every row has at least one postcondition distinct from the To State name
- [ ] **[C-05]** Every INV column checked (HOLDS or VIOLATED) per row
- [ ] **[C-08]** Table is complete and columnar; no operation exists only in prose
- [ ] **[C-15]** No state or operation name in PHASE 3 is absent from PHASE 1 or PHASE 2

**If any item fails → return to PHASE 3.**

---

### PHASE 4 — ADVERSARIAL REVIEW [T]

**VOCABULARY IS CLOSED. All names below must come from PHASE 1 and PHASE 2.**

#### Invalid Transitions

| Attempted Operation | From State | Blocking Condition | INV or Precondition Reference | Risk if Bypassed |
|--------------------|------------|-------------------|-----------------------------|-----------------|

Minimum three (operation, state) pairs.

#### Race Conditions

| Operation A | Operation B | Unsafe Interleaving | Outcome |
|------------|------------|-------------------|---------|

If no concurrent access: "No concurrent access — [reason]."

#### Boundary Coverage

- **Initial state:** [PHASE 1 name; confirm Terminal = No]
- **Terminal states:** [all PHASE 1 entries with Terminal = Yes]
- **Re-entry blocked:** One operation attempted from a terminal state; blocking condition named.

---

### PHASE 4 COMPLETE

- [ ] **[C-04]** At least three invalid (operation, state) pairs with blocking conditions
- [ ] **[C-07]** Race conditions addressed — at least one row OR explicit clearance with reason
- [ ] **[C-09]** Boundary coverage complete: initial state, all terminal states, re-entry blocked
- [ ] **[C-10]** All phase-complete gates present and referencing criterion IDs
- [ ] **[C-15]** No state or operation name in PHASE 4 is absent from PHASE 1 or PHASE 2

**If any item fails → return to relevant phase.**

---

### FINDINGS

Priority order. Reference phase and row.

- **P[N]:** [title] — [description]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: PHASE 1 (state inventory), PHASE 2 (operation and invariant inventory), VOCABULARY CLOSED declaration, PHASE 3 (transition trace), PHASE 4 (invalid transitions, race conditions, boundary coverage), FINDINGS.

---

## V-03 — Phrasing Register: Prohibitive Constraint Declaration

**Axis:** Phrasing register (single axis — prohibitive imperative vs explanatory guidance)
**Hypothesis:** V-01 uses binding rules stated descriptively ("a state not in T1 may not appear in T3"). V-02 uses a named lifecycle event with a prohibition block. V-03 tests whether the *phrasing register alone* — switching all structural constraints to YOU MAY NOT imperatives in a condensed preamble — produces both C-14 and C-15 without the overhead of a four-phase gate structure. The hypothesis is that explicit prohibition language ("YOU MAY NOT introduce a state not declared in the inventory"; "YOU MAY NOT add operations after the inventory is closed") is itself sufficient structure if the writer reads and internalizes the preamble. This is more fragile than V-01 or V-02 — there is no enforcement gate — but it tests whether phrasing alone carries the constraint.

---

You are running a **trace-state** signal for: {{topic}}

Hand-compile the state machine for a domain object. Before you fill any table, read the constraint block below. These constraints govern every table you fill. They are not guidelines — they are rules.

---

### CONSTRAINT BLOCK — READ BEFORE FILLING ANY TABLE

**C1 — State vocabulary is declared once.**
Declare all states in the State Inventory table. Once that table is complete, the state vocabulary is closed.
**YOU MAY NOT introduce a state name in any later table that does not appear in the State Inventory.**

**C2 — Operation vocabulary is declared once.**
Declare all operations in the Operation Inventory table. Once that table is complete, the operation vocabulary is closed.
**YOU MAY NOT introduce an operation name in any later table that does not appear in the Operation Inventory.**

**C3 — Inventory tables are authoritative.**
The State Inventory and Operation Inventory tables are the reference source for all later tables. Later tables bind to them.
**YOU MAY NOT add states or operations to the inventory retroactively.** If a trace row requires a name that is not in the inventory, stop. Identify the missing name, add it to the inventory before any trace rows reference it, and note the addition as a finding.

**C4 — Generic labels are invalid.**
State names such as "State A", "State 1", "initial", "final" are not acceptable.
**YOU MAY NOT use generic labels in any table.** Domain vocabulary from your assigned role is required in every state name.

**C5 — Prose is not a valid trace format.**
Operations may not be described only in prose paragraphs or bullet lists.
**YOU MAY NOT deliver trace output as prose.** Every operation must appear as a table row.

---

### ROLES

**[D] Domain Expert**
Auto-selected: Sales expert (Lead / Opportunity / Proposal / Closed Won / Closed Lost), CS expert (New / Active / On Hold / Pending / Resolved / Closed), Finance expert (Draft / Submitted / Approved / Posted / Paid / Voided).
Owns: STATE INVENTORY, OPERATION INVENTORY, INVARIANT REGISTRY.

**[T] Trace Developer**
Owns: TRANSITION TABLE, INVALID TRANSITIONS TABLE, RACE CONDITIONS TABLE, BOUNDARY COVERAGE, FINDINGS.
Before filling any table: re-read the CONSTRAINT BLOCK. Confirm compliance with C1–C5 per row.

---

### STATE INVENTORY [D]

All states in this entity's lifecycle. This table is the authoritative state vocabulary. Once complete, it is closed per CONSTRAINT C1 and C2.

| State Name | Defining Field Values | Entry Conditions | Terminal? |
|-----------|----------------------|-----------------|-----------|

---

### OPERATION INVENTORY [D]

All operations that can execute on this entity. This table is the authoritative operation vocabulary.

| Operation Name | Legal Source States | Target State | Triggering Actor |
|---------------|-------------------|-------------|-----------------|

States referenced here must appear in STATE INVENTORY. Adding a state here that is not in the STATE INVENTORY violates CONSTRAINT C3.

---

### INVENTORY CONFIRMED — VOCABULARY CLOSED

[Domain Expert explicitly states: "State inventory is complete: [list state names]. Operation inventory is complete: [list operation names]. Per CONSTRAINT C1 and C2, these vocabularies are now closed. No new state or operation names will be introduced in subsequent tables."]

---

### INVARIANT REGISTRY [D]

| INV ID | Name | Checkable Assertion | Authority Source |
|--------|------|--------------------|-----------------|

Minimum two invariants. Express each as a boolean assertion checkable in a test. Authority source: business rule name, SLA contract clause, regulation, or policy.

---

### TRANSITION TABLE [T]

**All names in this table must appear in STATE INVENTORY or OPERATION INVENTORY. Per CONSTRAINT C1 and C2, you may not introduce new state or operation names here.**

Scenario setup: [entity instance, starting state, actor, date/time context]

| # | From State | Operation | Preconditions | To State | Postconditions | INV-01 | INV-02 | Side Effects |
|---|-----------|-----------|---------------|---------|----------------|--------|--------|--------------|

**Column rules:**
- **From State / To State:** STATE INVENTORY names only. Any other name violates CONSTRAINT C1.
- **Operation:** OPERATION INVENTORY names only. Any other name violates CONSTRAINT C2.
- **Preconditions:** Minimum two testable assertions per row.
- **Postconditions:** Minimum one assertion distinct from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED — [reason]`; never blank.

---

### INVALID TRANSITIONS TABLE [T]

**All names must reference STATE INVENTORY and OPERATION INVENTORY. No new vocabulary.**

| # | Attempted Operation | From State | Blocking Condition | INV Reference | Risk if Bypassed |
|---|--------------------|-----------|--------------------|--------------|-----------------|

Minimum three (operation, state) pairs.

---

### RACE CONDITIONS TABLE [T]

| Operation A | Operation B | Unsafe Interleaving | Outcome |
|------------|------------|-------------------|---------|

If no concurrent access: "No concurrent access — [reason]."

---

### BOUNDARY COVERAGE [T]

- **Initial state:** [STATE INVENTORY name; confirm Terminal = No]
- **Terminal states:** [list all STATE INVENTORY entries with Terminal = Yes]
- **Re-entry blocked:** One operation attempted from a terminal state. Which precondition or invariant blocks it?

---

### COMPLIANCE REVIEW [T]

Before writing FINDINGS, confirm compliance with the CONSTRAINT BLOCK:

- [ ] **[C-14]** No state name in TRANSITION TABLE, INVALID TRANSITIONS TABLE, or BOUNDARY COVERAGE is absent from STATE INVENTORY
- [ ] **[C-14]** No operation name in any table is absent from OPERATION INVENTORY
- [ ] **[C-15]** INVENTORY CONFIRMED marker is present; no state or operation was added retroactively after that marker
- [ ] **[C-13]** No operation appears only in prose — all operations are table rows
- [ ] **[C-09]** At least one terminal state appears as a To State in TRANSITION TABLE; at least one INVALID TRANSITIONS row covers a terminal state

**Any item not confirmed → identify the violation and correct before writing FINDINGS.**

---

### FINDINGS

Priority order. Reference table and row. Include any C1–C5 violations found during COMPLIANCE REVIEW.

- **P[N]:** [title] — [description]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: CONSTRAINT BLOCK (reproduced), STATE INVENTORY, OPERATION INVENTORY, INVENTORY CONFIRMED marker, INVARIANT REGISTRY, TRANSITION TABLE, INVALID TRANSITIONS TABLE, RACE CONDITIONS TABLE, BOUNDARY COVERAGE, COMPLIANCE REVIEW, FINDINGS.

---

## V-04 — Combined: Referential Binding + Vocabulary Lock + Gate

**Axis:** Combined — output format (referential binding tables, C-14) + lifecycle emphasis (vocabulary lock, C-15) + gate enforcement (C-10, C-12)
**Hypothesis:** V-01 achieves C-14 structurally but leaves C-15 uncertain. V-02 achieves C-15 structurally but leaves C-14 uncertain. V-04 combines both by: (1) naming inventory tables with IDs (T1, T2) and stating the binding rule forward, (2) placing an explicit VOCABULARY CLOSED prohibition after T1 and T2 are complete, and (3) adding GATE A item that checks C-14 by ID and GATE C item that checks C-15 by ID. The two constraints reinforce each other: the binding rule makes C-14 operational (every later row references a T1/T2 ID), and the vocabulary lock prevents new vocabulary from being added that would require retroactive T1/T2 updates. Both structural guarantees are active simultaneously, and both are referenced by gate checkpoint items.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. Table 1 (states) and Table 2 (operations) are the authoritative inventories; all later tables reference them and may not introduce vocabulary not declared in them. Vocabulary is explicitly locked after the inventory phase; no new state or operation names may be added during trace phases.

---

### ROLES

**[D] Domain Expert**
Auto-selected: Sales expert (Lead / Opportunity / Proposal / Closed Won / Closed Lost), CS expert (New / Active / On Hold / Pending / Resolved / Closed), Finance expert (Draft / Submitted / Approved / Posted / Paid / Voided).
Owns: TABLE 1, TABLE 2, TABLE INV, VOCABULARY CLOSED declaration.

**[T] Trace Developer**
Owns: TABLE 3, TABLE 4, TABLE 5, BOUNDARY COVERAGE, FINDINGS.
Before writing any row in TABLE 3, 4, or 5: confirm the state and operation names in that row are present in T1 and T2 respectively. If a name is missing, stop and flag it to Domain Expert — do not introduce new vocabulary.

---

### TABLE 1 — STATE REGISTRY [D]

| State ID | State Name | Defining Field Values | Entry Conditions | Terminal? |
|---------|-----------|----------------------|-----------------|-----------|

**This table is the authoritative state vocabulary.** No state may appear in TABLE 3, 4, or 5 that is not declared here. Domain vocabulary only; no generic labels.

---

### TABLE 2 — OPERATION REGISTRY [D]

| Operation ID | Operation Name | Legal Source State IDs | Target State ID | Triggering Actor |
|-------------|---------------|----------------------|----------------|-----------------|

**This table is the authoritative operation vocabulary.** No operation may appear in TABLE 3, 4, or 5 that is not declared here. State IDs must reference TABLE 1 IDs.

---

### TABLE INV — INVARIANT REGISTRY [D]

| INV ID | Name | Checkable Assertion | Authority Source |
|--------|------|--------------------|-----------------|

Minimum two invariants. Authority source: business rule name, SLA contract clause, accounting regulation, or policy.

---

### GATE A

Before issuing VOCABULARY CLOSED: confirm all items.

- [ ] **[C-01]** TABLE 1 contains all lifecycle states with domain vocabulary; no generic labels
- [ ] **[C-02]** TABLE 2 contains all operations; every legal transition has a named operation; all state references in T2 use T1 IDs
- [ ] **[C-05]** TABLE INV has at least two invariants with checkable assertions and authority sources
- [ ] **[C-14]** Cross-table binding rule is understood: a state name not in TABLE 1 may not appear in TABLE 3, 4, or 5; an operation name not in TABLE 2 may not appear in TABLE 3, 4, or 5

**Any item unconfirmed → return to relevant table.**

---

### VOCABULARY CLOSED

> **Prohibition — Domain Expert declaration:**
> TABLE 1 is complete: [list state names]. TABLE 2 is complete: [list operation names].
>
> **You may not introduce any new state name or operation name after this point.** Tables 3, 4, and 5 may only reference names declared in TABLE 1 and TABLE 2. If a name needed for the trace is absent from the inventories, stop, return to Domain Expert, update the appropriate inventory table, re-confirm GATE A, and re-issue this declaration before tracing resumes.

---

### TABLE 3 — TRANSITION TRACE [T]

**All state and operation names must reference TABLE 1 and TABLE 2. VOCABULARY IS CLOSED.**

Scenario setup: [entity instance, starting state, actor, date/time context]

| # | From State (T1 ID) | Operation (T2 ID) | Preconditions | To State (T1 ID) | Postconditions | INV-01 | INV-02 | Side Effects |
|---|--------------------|-------------------|---------------|-----------------|----------------|--------|--------|--------------|

**Column rules:**
- **From State / To State:** T1 State IDs or State Names only. No undeclared name.
- **Operation:** T2 Operation IDs or Operation Names only. No undeclared name.
- **Preconditions:** Minimum two testable assertions per row.
- **Postconditions:** Minimum one assertion distinct from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED — [reason]`; never blank. Add columns for INV-03+ if TABLE INV has more invariants.

For operations with significant branching or plugin firing sequences, add a detail block beneath the row:
```
OPERATION [N] detail:
  Processing:   [what executes — plugin name, business rule, calculation, message]
  Branching:    [conditions that alter processing path]
```

---

### GATE B

Before filling TABLE 4: confirm all items.

- [ ] **[C-03]** Every TABLE 3 row has at least two preconditions as testable assertions
- [ ] **[C-06]** Every TABLE 3 row has at least one postcondition distinct from the To State name
- [ ] **[C-05]** Every invariant from TABLE INV is checked (HOLDS or VIOLATED) in every TABLE 3 row
- [ ] **[C-08]** TABLE 3 is complete and columnar; no operation exists only in prose
- [ ] **[C-15]** No state or operation name in TABLE 3 is absent from TABLE 1 or TABLE 2 respectively

**Any item unconfirmed → return to TABLE 3.**

---

### TABLE 4 — INVALID TRANSITIONS [T]

**All names must reference TABLE 1 and TABLE 2. VOCABULARY IS CLOSED.**

| # | Attempted Operation (T2 ID) | From State (T1 ID) | Blocking Condition | INV Reference | Risk if Bypassed |
|---|----------------------------|-------------------|--------------------|--------------|-----------------|

Minimum three (operation, state) pairs. Include at least one attempt on a terminal state from TABLE 1.

---

### TABLE 5 — RACE CONDITIONS [T]

| Operation A (T2 ID) | Operation B (T2 ID) | Unsafe Interleaving | Outcome |
|--------------------|---------------------|---------------------|---------|

If no concurrent access: "No concurrent access — [reason]."

---

### BOUNDARY COVERAGE [T]

- **Initial state:** [T1 State Name; confirm Terminal = No]
- **Terminal states:** [list all T1 entries with Terminal = Yes]
- **Re-entry blocked:** [T1 terminal state name] — attempted operation: [T2 operation name]. Blocking condition: [assertion].

---

### GATE C (Final)

- [ ] **[C-04]** TABLE 4 has at least three (operation, state) pairs with named blocking conditions
- [ ] **[C-07]** TABLE 5 addressed — at least one row OR explicit clearance with reason
- [ ] **[C-09]** BOUNDARY COVERAGE complete — initial state declared, all terminal states listed, re-entry blocked
- [ ] **[C-10]** GATE A, GATE B, and GATE C are present in this output and each references at least one criterion by ID
- [ ] **[C-11]** If an inertia challenge or pre-trace adversarial step was performed before TABLE 3, confirm at least one TABLE 4 row is derived from it
- [ ] **[C-12]** Phase-complete boundaries (GATE A, GATE B) are present as hard gates; each was closed before the next phase began
- [ ] **[C-13]** No operation appears only in prose in this output; TABLE 3 is the primary trace carrier
- [ ] **[C-14]** All state and operation names in TABLE 3, 4, 5 reference TABLE 1 and TABLE 2 respectively; no undeclared vocabulary was introduced
- [ ] **[C-15]** VOCABULARY CLOSED declaration is present between inventory phase and TABLE 3; no new state or operation was added after that marker

**Any item unconfirmed → correct the relevant phase.**

---

### FINDINGS

Priority order. Reference table number and gate item.

- **P[N]:** [title] — [description]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: TABLE 1 (state registry), TABLE 2 (operation registry), TABLE INV (invariants), GATE A, VOCABULARY CLOSED, TABLE 3 (transition trace), GATE B, TABLE 4 (invalid transitions), TABLE 5 (race conditions), BOUNDARY COVERAGE, GATE C, FINDINGS.

---

## V-05 — Combined: Vocabulary Lock + Inertia + Phase Sequencing

**Axis:** Combined — lifecycle emphasis (vocabulary lock, C-15) + inertia framing (C-11) + phase-completion sequencing (C-12)
**Hypothesis:** V-02 achieves C-15 via an explicit VOCABULARY CLOSED declaration placed after inventory. V-05 adds a new causal chain: the inertia challenge (PHASE B) forces the Domain Expert to surface process assumptions *before* declaring vocabulary closed, because process assumptions often reveal states or operations the initial inventory missed. Once the inertia assumptions are documented, the Domain Expert reviews the inventory one more time — then issues VOCABULARY CLOSED. This two-step closure (inertia first, then lock) is structurally sounder than locking after inventory alone: it reduces the probability of the Developer discovering missing vocabulary mid-trace and needing to return to the Domain Expert. C-14 is uncertain — no explicit binding rule between tables is stated — but C-15, C-11, and C-12 are all structural by design.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace in four phases. Vocabulary is locked between PHASE 2 and PHASE 3 — after the Domain Expert has inventoried states and operations AND challenged the current-process assumptions. Locking after inertia ensures that process-assumption discoveries (which often reveal missing states and operations) are incorporated before the trace begins.

---

### ROLES

**[D] Domain Expert**
Auto-selected: Sales expert (Lead / Opportunity / Proposal / Closed Won / Closed Lost), CS expert (New / Active / On Hold / Pending / Resolved / Closed), Finance expert (Draft / Submitted / Approved / Posted / Paid / Voided).
Owns: PHASE 1 (inventory), PHASE 2 (inertia challenge), VOCABULARY CLOSED declaration.

**[T] Trace Developer**
Owns: PHASE 3 (transition trace), PHASE 4 (adversarial review).
May not introduce any state or operation name not present in the inventories at the time VOCABULARY CLOSED was issued. If a name is needed, stop, flag to Domain Expert, and await an updated VOCABULARY CLOSED declaration.

---

### PHASE 1 — INVENTORY [D]

**Entity:** [name and entity type]
**Domain:** [Sales | Customer Service | Finance]

#### State Inventory

| State Name | Defining Field Values | Entry Conditions | Terminal? |
|-----------|----------------------|-----------------|-----------|

Domain vocabulary only. At least one terminal state required.

#### Operation Inventory

| Operation Name | Legal Source States | Target State | Triggering Actor |
|---------------|-------------------|-------------|-----------------|

Source and target states must use names from the State Inventory above.

#### Invariant Registry

| INV ID | Name | Checkable Assertion | Authority Source |
|--------|------|--------------------|-----------------|

Minimum two invariants. Authority source: business rule, SLA clause, regulation, policy.

---

### PHASE 1 COMPLETE

Do not begin PHASE 2 until PHASE 1 is complete.

- [ ] **[C-01]** All lifecycle states named with domain vocabulary; no generic labels
- [ ] **[C-02]** All operations named; every legal transition has a named operation
- [ ] **[C-05]** At least two invariants with checkable assertions and authority sources
- [ ] **[C-12]** PHASE 1 is complete before PHASE 2 begins

**Any item unconfirmed → return to PHASE 1.**

---

### PHASE 2 — INERTIA CHALLENGE [D]

Before locking vocabulary, challenge the process assumptions for {{topic}}.

**Core question:** What does the current manual process (spreadsheet, email, legacy system, verbal convention, paper form) assume about operation order or preconditions that the platform may NOT enforce as a state gate?

| # | Current Process Assumption | Platform Enforced? (Y/N) | Expected Enforcement Gap |
|---|--------------------------|--------------------------|--------------------------|

*Discovery prompts by domain:*
- *Sales:* "Deal can only close with a signed contract — is that a state gate or a convention?"
- *CS:* "Agents must escalate before Resolving a Priority 1 case — platform rule or manager rule?"
- *Finance:* "Finance approves before anyone posts — enforced as a state precondition or manual?"

Minimum two assumptions. Every N row is a candidate invalid transition for PHASE 4.

**After completing the inertia table:** Review the PHASE 1 State Inventory and Operation Inventory. Did the inertia challenge reveal any states or operations that were omitted? If yes, add them to PHASE 1 now, before issuing VOCABULARY CLOSED. This is the last opportunity to expand the inventory.

---

### PHASE 2 COMPLETE

Do not issue VOCABULARY CLOSED until PHASE 2 is complete.

- [ ] At least two inertia assumptions documented with Platform Enforced verdict
- [ ] At least one assumption marked N
- [ ] PHASE 1 inventories reviewed in light of PHASE 2 findings; any missing states or operations added to PHASE 1 before this marker
- [ ] **[C-11]** Inertia challenge is complete and precedes the VOCABULARY CLOSED declaration; PHASE 3 has not yet begun

**Any item unconfirmed → return to PHASE 2.**

---

### VOCABULARY CLOSED

> **Prohibition — Domain Expert declaration:**
> PHASE 2 inertia challenge is complete. All process assumptions have been documented. I have reviewed the PHASE 1 inventories in light of the inertia findings.
>
> **Final inventory:**
> - States: [list all state names from PHASE 1]
> - Operations: [list all operation names from PHASE 1]
>
> **This vocabulary is now closed. You may not introduce any new state name or operation name in PHASE 3 or PHASE 4.** If the Trace Developer encounters a state or operation needed for a trace row that is not in this list, they must stop and request a vocabulary update from the Domain Expert. Any such update requires a new VOCABULARY CLOSED declaration before tracing resumes.

---

### PHASE 3 — TRANSITION TRACE [T]

**VOCABULARY IS CLOSED. All names must appear in the PHASE 1 inventories as declared at VOCABULARY CLOSED.**

Scenario setup: [entity instance, starting state, actor, date/time context]

| # | From State | Operation | Preconditions | To State | Postconditions | INV-01 | INV-02 | Side Effects |
|---|-----------|-----------|---------------|---------|----------------|--------|--------|--------------|

**Column rules:**
- **From State / To State:** PHASE 1 state names only. No undeclared names.
- **Operation:** PHASE 1 operation names only. No undeclared names.
- **Preconditions:** Minimum two testable assertions per row.
- **Postconditions:** Minimum one assertion distinct from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED — [reason]`; never blank.
- **Side Effects:** Triggered plugins, business rules, related records, notifications, async jobs.

---

### PHASE 3 COMPLETE

Do not begin PHASE 4 until PHASE 3 is complete.

- [ ] **[C-03]** Every row has at least two preconditions as testable assertions
- [ ] **[C-06]** Every row has at least one postcondition distinct from the To State name
- [ ] **[C-05]** Every invariant from PHASE 1 is checked (HOLDS or VIOLATED) per row
- [ ] **[C-08]** Table is complete and columnar; no operation exists only in prose
- [ ] **[C-15]** No state or operation name in PHASE 3 table is absent from the VOCABULARY CLOSED list

**Any item unconfirmed → return to PHASE 3.**

---

### PHASE 4 — ADVERSARIAL REVIEW [T]

**VOCABULARY IS CLOSED.**

#### Invalid Transitions

Start with PHASE 2 N-rows. For each: does the platform actually block the transition?

| # | Attempted Operation | From State | Blocking Condition | PHASE 2 Row | Risk if Bypassed |
|---|--------------------|-----------|--------------------|-----------|-----------------|

Every PHASE 2 N-row must appear here. Add any additional invalid transitions not from PHASE 2. Minimum three total (operation, state) pairs.

#### Race Conditions

| Operation A | Operation B | Unsafe Interleaving | Outcome |
|------------|------------|-------------------|---------|

If no concurrent access: "No concurrent access — [reason]."

#### Boundary Coverage

- **Initial state:** [PHASE 1 state name; confirm Terminal = No]
- **Terminal states:** [list all PHASE 1 states with Terminal = Yes]
- **Re-entry blocked:** One terminal state, one attempted operation, one blocking condition.

---

### PHASE 4 COMPLETE

- [ ] **[C-04]** At least three (operation, state) pairs in invalid transitions with blocking conditions
- [ ] **[C-07]** Race conditions addressed — at least one row OR explicit clearance with reason
- [ ] **[C-09]** Boundary coverage complete — initial state, all terminal states, re-entry blocked
- [ ] **[C-10]** All four phase-complete gates are present and reference criterion IDs
- [ ] **[C-11]** PHASE 2 inertia challenge preceded PHASE 3; at least one PHASE 4 invalid-transition row is derived from a PHASE 2 N-row (confirm by PHASE 2 row reference in the table)
- [ ] **[C-12]** PHASE 1, 2, and 3 complete markers are present as hard gates; each was closed before the next phase began
- [ ] **[C-15]** VOCABULARY CLOSED declaration is present between PHASE 2 and PHASE 3; no new state or operation was added after that marker

**Any item unconfirmed → correct the relevant phase.**

---

### FINDINGS

Priority order. Reference phase and row.

- **P[N]:** [title] — [description]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: PHASE 1 (state inventory, operation inventory, invariant registry), PHASE 2 (inertia challenge table + inventory review note), VOCABULARY CLOSED declaration, PHASE 3 (transition trace), PHASE 4 (invalid transitions, race conditions, boundary coverage), FINDINGS.
