# trace-state Variate — Round 6
**Date:** 2026-03-15
**Rubric:** v5 (C-01..C-17; golden threshold: all essential pass AND composite >= 80)
**New criteria:** C-16 (numbered constraint preamble) and C-17 (role-differentiated constraint assignment)
**Scoring formula:** essential 50 + recommended 40 + aspirational 10 (10 criteria, 1.0 pt each)

---

## Round 6 Situation

Round 5 results (rubric v5, retroactive scoring):

| Variant | C-16 | C-17 | Aspirational total | Composite |
|---------|------|------|-------------------|-----------|
| V-01 | FAIL (no preamble block) | PASS (ROLES [T]) | 5.5 / 10 | 95.5 |
| V-02 | FAIL (distributed, not preamble) | PASS (ROLES [T]) | 7.0 / 10 | 97.0 |
| V-03 | PASS (CONSTRAINT BLOCK C1-C5) | FAIL (no ROLES) | 6.5 / 10 | 96.5 |

No R5 variation satisfies both C-16 and C-17 simultaneously. The 10/10 aspirational ceiling requires synthesis: a numbered preamble block before all output-generating sections (C-16) AND role-differentiated constraint attribution within a ROLES section (C-17).

The two criteria are compatible but solve different problems. C-16 registers concerns before work begins — it is a constraint registry. C-17 makes accountability explicit — it assigns each constraint to a named actor. A variation that has the registry but not the attribution (R5 V-03) is a rulebook without owners. A variation that has attribution but not the registry (R5 V-01, V-02) has owners without a canonical list to consult before work begins. The synthesis is straightforward structurally; the risk is dilution — adding both sections superficially without making either load-bearing.

**R6 objective:** All five variations target C-16 + C-17 synthesis. Variation axes differentiate the structural mechanism, not whether to pursue it. V-01 through V-03 are single-axis tests; V-04 and V-05 combine axes for coverage depth.

---

## Round 6 Variation Map

| Var | Axis | C-16 | C-17 | Aspirational target | Hypothesis |
|-----|------|------|------|---------------------|------------|
| V-01 | Phrasing register — formal preamble with numbered prohibitions + ROLES attributes each constraint to owning role | exp | exp | 8.5-9.0 | The most direct synthesis: CONSTRAINTS C1-C5 before all sections (C-16 structural via position), ROLES section re-attributes each Cx to a named role as a binding obligation (C-17 structural via explicit attribution); phrasing stays imperative throughout |
| V-02 | Output format — unified CONSTRAINT MATRIX table (ID, Prohibition, Assigned Role, Concern) | exp | exp | 8.0-9.0 | One table satisfies both criteria: numbered rows with imperative phrasing (C-16), Assigned Role column for each row (C-17); risk is whether a table constitutes a "preamble section" under C-16's pass condition or whether a bare table without section header fails on a technicality |
| V-03 | Role sequence — [D] executes CONSTRAINT CHARTER as Phase 0; [T] confirms each item before tracing | exp | exp | 8.0-8.5 | Reversed role sequence: [D] authors and publishes constraints before [T] begins; the charter is numbered and imperative (C-16 via [D]'s authorship before Phase 1); [T]'s ROLES entry requires charter acknowledgment as a named obligation (C-17 via [T]'s scoped binding to [D]'s charter) |
| V-04 | Lifecycle emphasis — phase ownership prohibitions registered in numbered preamble; vocabulary lock and referential binding added | exp | exp | 9.0-9.5 | Phase ownership generates natural role-scoped constraints; numbered preamble formalizes them as C1-Cn before phases begin (C-16); ROLES section re-attributes each to the owning role with explicit binding language (C-17); C-14 and C-15 added as numbered preamble items, raising aspirational floor |
| V-05 | Combined — all axes, ceiling attempt | exp | exp | 10.0 | Full synthesis targeting all 10 aspirational criteria structurally: numbered preamble (C-16) + ROLES binding (C-17) + vocabulary lock (C-15) + referential integrity (C-14) + inertia challenge (C-11) + four named gates (C-10) + explicit prose prohibition (C-13) + hard-stop phase-completion phrasing (C-12) + mandatory columnar table (C-08) + terminal-state boundary coverage (C-09) |

---

## V-01 — Phrasing Register: Formal Preamble + Role-Attributed ROLES

**Axis:** Phrasing register (single axis)
**Hypothesis:** R5 V-03 had a CONSTRAINT BLOCK C1-C5 satisfying C-16 but had no ROLES section. R5 V-01 had role-scoped binding in ROLES satisfying C-17 but its constraints were distributed across the document, not collected into a preamble block. V-01 (R6) is the direct synthesis: a CONSTRAINTS section with five numbered "YOU MAY NOT" items covering distinct concerns (C-16 structural via position before all tables) paired with a ROLES section that re-attributes each Cx constraint to the role that owns it as an explicit binding obligation (C-17 structural via named role + scoped language). The phrasing register stays formal and imperative throughout — the preamble is a policy, not a suggestion. Each role entry ends with a binding statement that names the applicable constraints. The key design decision is that the preamble and ROLES are separate sections doing distinct work: the preamble registers, the ROLES section assigns.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. All trace output is delivered in named, columnar tables. Before producing any output, read the CONSTRAINTS section — it governs every section that follows.

---

### CONSTRAINTS

Read this section completely before filling any table or writing any section.

**C1.** YOU MAY NOT introduce any state name in any table that is not declared in TABLE 1. A state name not in TABLE 1 is a trace error, not a finding. Stop and return to TABLE 1.

**C2.** YOU MAY NOT introduce any operation name in any table that is not declared in TABLE 2. An operation name not in TABLE 2 is a trace error. Stop and return to TABLE 2.

**C3.** YOU MAY NOT use prose paragraphs or bullet lists as the primary output format for trace data. Every operation must appear as a row in a named, columnar table. A row documented only in prose is a missing row.

**C4.** YOU MAY NOT retroactively add states or operations to TABLE 1 or TABLE 2 after VOCABULARY CLOSED is declared. If a name is needed and absent, stop: return to the inventory section, add it, re-declare VOCABULARY CLOSED, then continue.

**C5.** YOU MAY NOT leave any invariant status column blank in TABLE 3. Every row must record HOLDS or VIOLATED — [reason] for every declared invariant.

---

### ROLES

**[D] Domain Expert**
Auto-selected from context: Sales expert (Lead / Qualified Lead / Opportunity / Proposal / Closed Won / Closed Lost), Customer Service expert (New / Active / On Hold / Pending / Resolved / Closed), or Finance expert (Draft / Submitted / Approved / Posted / Paid / Voided).
Owns: TABLE 1 (State Registry), TABLE 2 (Operation Registry), TABLE INV (Invariant Registry), VOCABULARY CLOSED declaration.
**Binding constraint — C4 applies to [D]:** After [D] declares VOCABULARY CLOSED, [D] may not add, rename, or remove any entry in TABLE 1 or TABLE 2.

**[T] Trace Developer**
Owns: TABLE 3 (Transition Trace), TABLE 4 (Invalid Transitions), TABLE 5 (Race Conditions), BOUNDARY COVERAGE, FINDINGS.
**Binding constraints — C1, C2, C3, C5 apply to [T]:**
- [T] may not introduce any state or operation name in TABLE 3, 4, or 5 that is not declared in TABLE 1 or TABLE 2 (C1, C2).
- [T] may not substitute prose narrative for a table row (C3).
- [T] may not leave an invariant column blank in any TABLE 3 row (C5).

---

### TABLE 1 — STATE REGISTRY [D]

| State ID | State Name | Defining Field Values | Entry Conditions | Terminal? |
|---------|-----------|----------------------|-----------------|-----------|

Domain vocabulary only. No "State A", "initial", "final", or numbered generics. At least one row must have Terminal = Yes.

---

### TABLE 2 — OPERATION REGISTRY [D]

| Op ID | Operation Name | Legal Source State IDs | Target State ID | Triggering Actor |
|-------|---------------|----------------------|----------------|-----------------|

State IDs in columns 3 and 4 must reference TABLE 1 IDs. An operation referencing an undeclared state must not be added — resolve in TABLE 1 first.

---

### TABLE INV — INVARIANT REGISTRY [D]

| INV ID | Name | Checkable Assertion | Authority Source |
|--------|------|--------------------|--------------------|

Minimum two invariants as boolean assertions. Authority source: business rule name, SLA contract clause, accounting regulation, or policy.

---

### VOCABULARY CLOSED [D]

After completing TABLE 1, TABLE 2, and TABLE INV, declare:

> VOCABULARY CLOSED. TABLE 1 states: [list]. TABLE 2 operations: [list]. No new state or operation name may be introduced from this point forward. C4 applies.

---

### GATE A

Do not begin TABLE 3 until all items below are confirmed. Unconfirmed = blocked.

- [ ] **[C-01]** Every TABLE 2 operation has at least one legal source state and exactly one target state, both referencing TABLE 1 IDs
- [ ] **[C-04]** All TABLE 1 state names use domain vocabulary — no generics
- [ ] **[C-05]** TABLE INV has at least two invariants with checkable assertions and authority sources
- [ ] **[C-14]** Referential binding confirmed: [T] will not introduce any name in TABLE 3, 4, or 5 that is not in TABLE 1 or TABLE 2
- [ ] **[C-15]** VOCABULARY CLOSED has been declared and contains the complete name list

**GATE A BLOCKED. Do not begin TABLE 3 until all items are confirmed.**

---

### TABLE 3 — TRANSITION TRACE [T]

Scenario setup: [entity instance, starting state, actor, date/time context]

C1 and C2 apply: every state and operation reference must use TABLE 1 and TABLE 2 IDs. If a needed name is missing, stop.

| # | From State (T1 ID) | Operation (T2 ID) | Preconditions | To State (T1 ID) | Postconditions | INV-01 | INV-02 | Side Effects |
|---|--------------------|-------------------|---------------|-----------------|----------------|--------|--------|--------------|

Column rules:
- **From State / To State:** TABLE 1 IDs only.
- **Operation:** TABLE 2 IDs only.
- **Preconditions:** Minimum two testable assertions (e.g., `status == Active`, `owner_id != null`).
- **Postconditions:** Minimum one assertion distinct from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED — [reason]`; never blank (C5).
- **Side Effects:** Triggered rules, record changes, notifications, async jobs.

---

### TABLE 4 — INVALID TRANSITIONS [T]

| # | Attempted Operation (T2 ID) | From State (T1 ID) | Blocking Condition | INV Reference | Risk if Bypassed |
|---|----------------------------|-------------------|--------------------|--------------|-----------------|

Minimum one row. All references use TABLE 1 and TABLE 2 IDs.

---

### TABLE 5 — RACE CONDITIONS [T]

| Operation A (T2 ID) | Operation B (T2 ID) | Unsafe Interleaving | Outcome |
|--------------------|---------------------|---------------------|---------|

If no concurrent access is possible: "No concurrent access — [reason]."

---

### GATE B

Do not write FINDINGS until all items below are confirmed. Unconfirmed = blocked.

- [ ] **[C-01]** Every TABLE 3 row has a From State and To State from TABLE 1
- [ ] **[C-02]** Every TABLE 3 row has at least two preconditions as testable assertions
- [ ] **[C-03]** Every TABLE INV invariant is checked (HOLDS or VIOLATED) in every TABLE 3 row
- [ ] **[C-06]** Every TABLE 3 row has at least one postcondition distinct from the To State name
- [ ] **[C-04]** All TABLE 3 state names use domain vocabulary from TABLE 1
- [ ] **[C-07]** TABLE 5 addressed — at least one row OR explicit clearance with reason
- [ ] **[C-08]** TABLE 3 is columnar and complete; no operation exists only in prose
- [ ] **[C-09]** At least one TABLE 3 row reaches a terminal state; at least one TABLE 4 row covers a terminal state attempt

**GATE B BLOCKED. Do not write FINDINGS until all items are confirmed.**

---

### BOUNDARY COVERAGE [T]

- **Initial state:** [TABLE 1 state name; confirm Terminal = No]
- **Terminal states:** [list all TABLE 1 entries where Terminal = Yes]
- **Re-entry blocked:** One attempt to execute an operation from a terminal state. Blocking condition.

---

### FINDINGS

Priority order. Reference table and row.

- **P[N]:** [title] — [description, table row reference]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: CONSTRAINTS, ROLES, TABLE 1, TABLE 2, TABLE INV, VOCABULARY CLOSED, GATE A, TABLE 3, TABLE 4, TABLE 5, GATE B, BOUNDARY COVERAGE, FINDINGS.

---

## V-02 — Output Format: Unified Constraint Matrix

**Axis:** Output format (single axis)
**Hypothesis:** C-16 and C-17 are satisfied by separate sections in V-01 — a preamble for C-16, a ROLES section for C-17. V-02 asks whether a single artifact can satisfy both. A CONSTRAINT MATRIX table with columns `ID | Prohibition | Assigned Role | Concern` places every constraint as a numbered row (C-16 via numbered IDs and imperative phrasing in the Prohibition column) with explicit role attribution per row (C-17 via Assigned Role column). The matrix is the first section before any inventory or trace output. The ROLES section following it references the CONSTRAINT MATRIX rather than defining new constraints, making the attribution declarative rather than duplicated. The main risk is whether a table constitutes a "preamble section" under C-16's pass condition — the rubric requires a "preamble section with at least two numbered prohibitions covering at least two distinct concerns," which a labeled, titled table section satisfies if it precedes all output-generating sections. The secondary risk is that the Assigned Role column is a lookup, not a binding statement — but the rubric's C-17 pass condition says "role has at least one explicitly assigned constraint expressed as a role-scoped binding," and a table cell explicitly assigning a constraint ID to a role name is a binding.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. All constraints governing this trace are pre-registered in the CONSTRAINT MATRIX. Read the matrix completely before producing any output. The matrix is authoritative.

---

### CONSTRAINT MATRIX

This table registers every constraint that applies to this trace. It is the first section. No inventory or trace output may be produced until this table is read.

| ID | Prohibition | Assigned Role | Concern |
|----|-------------|---------------|---------|
| C1 | YOU MAY NOT introduce any state name in any table that is not declared in the STATE REGISTRY | [T] | Vocabulary scope — states |
| C2 | YOU MAY NOT introduce any operation name in any table that is not declared in the OPERATION REGISTRY | [T] | Vocabulary scope — operations |
| C3 | YOU MAY NOT use prose paragraphs or bullet lists as the primary output format for trace data; every operation must appear as a table row | [T] | Output format |
| C4 | YOU MAY NOT retroactively add states or operations after VOCABULARY CLOSED is declared | [D] | Retroactive additions |
| C5 | YOU MAY NOT leave any invariant status column blank in the TRANSITION TABLE | [T] | Invariant completeness |
| C6 | YOU MAY NOT begin the TRANSITION TABLE until the DECLARATION GATE confirms all inventory tables are complete | [T] | Phase ordering |

---

### ROLES

**[D] Domain Expert**
Auto-selected: Sales expert (Lead / Qualified Lead / Opportunity / Proposal / Closed Won / Closed Lost), Customer Service expert (New / Active / On Hold / Pending / Resolved / Closed), or Finance expert (Draft / Submitted / Approved / Posted / Paid / Voided).
Owns: STATE REGISTRY, OPERATION REGISTRY, INVARIANT REGISTRY, VOCABULARY CLOSED declaration.
Binding constraints from CONSTRAINT MATRIX: **C4** (may not retroactively add vocabulary after VOCABULARY CLOSED).

**[T] Trace Developer**
Owns: TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, BOUNDARY COVERAGE, FINDINGS.
Binding constraints from CONSTRAINT MATRIX: **C1, C2, C3, C5, C6** (vocabulary scope in both dimensions, output format, invariant completeness, phase ordering).

---

### STATE REGISTRY [D]

| State ID | State Name | Defining Field Values | Entry Conditions | Terminal? |
|---------|-----------|----------------------|-----------------|-----------|

Domain vocabulary only. At least one Terminal = Yes row required.

---

### OPERATION REGISTRY [D]

| Op ID | Operation Name | Legal Source State IDs | Target State ID | Triggering Actor |
|-------|---------------|----------------------|----------------|-----------------|

All State IDs must reference STATE REGISTRY IDs. Operations referencing undeclared states must not be added.

---

### INVARIANT REGISTRY [D]

| INV ID | Invariant | Checkable Assertion | Authority Source |
|--------|-----------|--------------------|--------------------|

Minimum two invariants as boolean assertions. Authority source: business rule, SLA clause, regulation, or policy.

---

### VOCABULARY CLOSED [D]

> VOCABULARY CLOSED per CONSTRAINT MATRIX C4. States: [list]. Operations: [list]. No new names may be introduced.

---

### DECLARATION GATE

Constraint C6 from CONSTRAINT MATRIX: [T] may not begin the TRANSITION TABLE until this gate passes.

- [ ] STATE REGISTRY complete — domain vocabulary, at least one terminal state
- [ ] OPERATION REGISTRY complete — all operations have source state IDs and target state IDs from STATE REGISTRY
- [ ] INVARIANT REGISTRY complete — at least two invariants with assertions and authority sources
- [ ] VOCABULARY CLOSED declared
- [ ] **[C-14]** [T] confirms: no name will be introduced in any table that is not in STATE REGISTRY or OPERATION REGISTRY

**BLOCKED per C6. Do not begin TRANSITION TABLE until all items confirmed.**

---

### TRANSITION TABLE [T]

Constraints C1, C2, C3, C5 apply. See CONSTRAINT MATRIX.

Scenario setup: [entity instance, starting state, actor, date/time context]

| # | From State | Operation | Preconditions | To State | Postconditions | INV-01 | INV-02 | Side Effects |
|---|--------------------|-----------|---------------|---------|----------------|--------|--------|--------------|

Column rules:
- **From State / To State:** STATE REGISTRY names only (C1).
- **Operation:** OPERATION REGISTRY names only (C2).
- **Preconditions:** Minimum two testable assertions per row.
- **Postconditions:** Minimum one assertion distinct from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED — [reason]`; never blank (C5).

---

### INVALID TRANSITIONS [T]

| # | Attempted Operation | From State | Blocking Condition | INV Reference | Risk if Bypassed |
|---|--------------------|------------|-------------------|--------------|-----------------|

Minimum one row. All names from STATE REGISTRY / OPERATION REGISTRY.

---

### RACE CONDITIONS [T]

| Operation A | Operation B | Unsafe Interleaving | Outcome |
|------------|------------|---------------------|---------|

If no concurrent access: "No concurrent access — [reason]."

---

### TRACE COMPLETENESS GATE

- [ ] TRANSITION TABLE complete and columnar — no operation exists only in prose (C3)
- [ ] Every row has at least two preconditions
- [ ] Every row has at least one postcondition distinct from the To State name
- [ ] Every INV column filled — no blanks (C5)
- [ ] INVALID TRANSITIONS has at least one row with a named blocking condition
- [ ] RACE CONDITIONS addressed
- [ ] **[C-09]** At least one row reaches a terminal state; at least one invalid transition covers a terminal state attempt

**BLOCKED. Do not write FINDINGS until all items confirmed.**

---

### BOUNDARY COVERAGE [T]

- **Initial state:** [name; Terminal = No]
- **Terminal states:** [list all STATE REGISTRY entries where Terminal = Yes]
- **Re-entry attempt:** One attempt from a terminal state with blocking condition shown.

---

### FINDINGS

Priority order. Reference table and row.

- **P[N]:** [title] — [description]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: CONSTRAINT MATRIX, ROLES, STATE REGISTRY, OPERATION REGISTRY, INVARIANT REGISTRY, VOCABULARY CLOSED, DECLARATION GATE, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, TRACE COMPLETENESS GATE, BOUNDARY COVERAGE, FINDINGS.

---

## V-03 — Role Sequence: Domain Expert Publishes Constraint Charter; Trace Developer Acknowledges

**Axis:** Role sequence (single axis)
**Hypothesis:** R5 V-01 and V-02 both placed ROLES as a document-level header — a setup section before any phases began. The constraints in those ROLES sections were attributed to [T] but were not published by [D]; they were editorially imposed by the prompt. V-03 changes who authors the constraint registry: [D] executes a CONSTRAINT CHARTER phase as the first operational act, before any inventory. [D] is the constraint authority — [D] publishes the numbered charter items (C-16 structural via position before Phase 1 inventory, via [D]'s authorship). [T]'s ROLES entry requires explicit charter acknowledgment as a named obligation before tracing begins (C-17 structural: "[T] must acknowledge each charter item before filling TABLE 3"). The role sequence is the structural guarantor: [D] publishes, [T] acknowledges, then [T] traces. The hypothesis is that role-ownership of the constraint registry strengthens C-17 attribution — the constraints are not general document rules but specifically delegated between [D] (who issues the charter as the domain authority) and [T] (who is bound by it as the technical executor).

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. Phase 0 begins with [D] — the Domain Expert publishes the CONSTRAINT CHARTER before any inventory or tracing work begins. [T] — the Trace Developer — may not open any table or begin any phase until [T] has acknowledged each charter item.

---

### ROLES

**[D] Domain Expert**
Auto-selected: Sales expert (Lead / Qualified Lead / Opportunity / Proposal / Closed Won / Closed Lost), Customer Service expert (New / Active / On Hold / Pending / Resolved / Closed), or Finance expert (Draft / Submitted / Approved / Posted / Paid / Voided).
Owns: PHASE 0 (CONSTRAINT CHARTER), PHASE 1 (inventory tables), VOCABULARY CLOSED declaration.
**[D] must complete and publish the CONSTRAINT CHARTER before [T] begins any phase.**

**[T] Trace Developer**
Owns: PHASE 2 (TRANSITION TABLE), PHASE 3 (adversarial review), FINDINGS.
**[T] must acknowledge every charter item in ACKNOWLEDGMENT GATE before filling any table. [T] may not introduce any state or operation name not declared in [D]'s inventory. [T] may not use prose as the primary trace format.**

---

### PHASE 0 — CONSTRAINT CHARTER [D]

[D] publishes this charter. It registers the constraints that govern all subsequent work. [T] reads and acknowledges each item before proceeding.

**C1.** YOU MAY NOT introduce any state or operation name in any table that [D] has not declared in the STATE REGISTRY or OPERATION REGISTRY. If a name is missing, return to [D]'s inventory phase — do not improvise.

**C2.** YOU MAY NOT use prose paragraphs or unstructured bullet lists as the primary carrier of trace data. Every operation traces as a table row.

**C3.** YOU MAY NOT retroactively expand the vocabulary after [D] declares VOCABULARY CLOSED. If a new name is needed, [D] must re-open the inventory, add the name, and re-declare VOCABULARY CLOSED before [T] continues.

**C4.** YOU MAY NOT leave invariant status columns blank. Every row in the TRANSITION TABLE records a status for every declared invariant.

**C5.** YOU MAY NOT begin PHASE 2 until ACKNOWLEDGMENT GATE confirms [T] has read and accepted all charter items.

*[D] declaration: "This charter is now published. [T] may not begin until each item is acknowledged."*

---

### PHASE 1 — INVENTORY [D]

Do not begin Phase 1 until PHASE 0 is complete.

#### STATE REGISTRY [D]

| State ID | State Name | Defining Field Values | Entry Conditions | Terminal? |
|---------|-----------|----------------------|-----------------|-----------|

Domain vocabulary only. At least one Terminal = Yes.

---

#### OPERATION REGISTRY [D]

| Op ID | Operation Name | Legal Source State IDs | Target State ID | Triggering Actor |
|-------|---------------|----------------------|----------------|-----------------|

All IDs reference STATE REGISTRY.

---

#### INVARIANT REGISTRY [D]

| INV ID | Invariant | Checkable Assertion | Authority Source |
|--------|-----------|--------------------|--------------------|

Minimum two. Authority source: business rule, SLA clause, regulation, policy.

---

#### VOCABULARY CLOSED [D]

> VOCABULARY CLOSED. [D] confirms the complete name set: states [list], operations [list]. C3 applies from this point.

---

### ACKNOWLEDGMENT GATE

[T] confirms each charter item before any PHASE 2 table may be opened. Unconfirmed = PHASE 2 is blocked.

- [ ] **C1 acknowledged:** [T] confirms: I will not introduce any state or operation name not declared in [D]'s STATE REGISTRY or OPERATION REGISTRY.
- [ ] **C2 acknowledged:** [T] confirms: I will not use prose as the primary output format. Every operation will appear as a table row.
- [ ] **C3 acknowledged:** [T] confirms: I will not add vocabulary after VOCABULARY CLOSED. If I need a name, I will return to [D].
- [ ] **C4 acknowledged:** [T] confirms: I will not leave any invariant column blank.
- [ ] **C5 acknowledged:** [T] confirms: I am now entering PHASE 2 with all charter constraints accepted.
- [ ] **[C-14]** [T] confirms: STATE REGISTRY and OPERATION REGISTRY are the authoritative vocabularies; no later table will introduce terms outside them.
- [ ] **[C-15]** [T] confirms: VOCABULARY CLOSED has been declared and the name list is complete.

**[T] MAY NOT OPEN PHASE 2 UNTIL ALL ITEMS ARE CONFIRMED.**

---

### PHASE 2 — TRANSITION TABLE [T]

Scenario setup: [entity instance, starting state, actor, date/time context]

Charter constraints C1, C2, C4 apply. See PHASE 0.

| # | From State | Operation | Preconditions | To State | Postconditions | INV-01 | INV-02 | Side Effects |
|---|--------------------|-----------|---------------|---------|----------------|--------|--------|--------------|

Column rules:
- **From State / To State:** STATE REGISTRY names only.
- **Operation:** OPERATION REGISTRY names only.
- **Preconditions:** Minimum two testable assertions per row.
- **Postconditions:** Minimum one assertion distinct from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED — [reason]`; never blank (C4).

---

### TRACE GATE

Do not begin PHASE 3 until all items confirmed.

- [ ] **[C-01]** Every row has a From State and To State from STATE REGISTRY
- [ ] **[C-02]** Every row has at least two preconditions as testable assertions
- [ ] **[C-03]** Every invariant checked per row (HOLDS or VIOLATED)
- [ ] **[C-06]** Every row has at least one postcondition distinct from the state name
- [ ] **[C-08]** TRANSITION TABLE is columnar and complete; no operation exists only in prose

**BLOCKED. Do not begin PHASE 3 until all items confirmed.**

---

### PHASE 3 — ADVERSARIAL REVIEW [T]

#### INVALID TRANSITIONS [T]

| # | Attempted Operation | From State | Blocking Condition | INV Reference | Risk if Bypassed |
|---|--------------------|------------|-------------------|--------------|-----------------|

Minimum one row.

#### RACE CONDITIONS [T]

| Operation A | Operation B | Unsafe Interleaving | Outcome |
|------------|------------|---------------------|---------|

If cleared: "No concurrent access — [reason]."

#### BOUNDARY COVERAGE [T]

- **Initial state:** [STATE REGISTRY name; Terminal = No]
- **Terminal states:** [list all Terminal = Yes entries]
- **Re-entry attempt:** One attempt from a terminal state. Blocking condition.

---

### FINDINGS

Priority order. Reference phase and table row.

- **P[N]:** [title] — [description]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: PHASE 0 (CONSTRAINT CHARTER), ROLES, PHASE 1 (STATE REGISTRY, OPERATION REGISTRY, INVARIANT REGISTRY, VOCABULARY CLOSED), ACKNOWLEDGMENT GATE, PHASE 2 (TRANSITION TABLE), TRACE GATE, PHASE 3 (INVALID TRANSITIONS, RACE CONDITIONS, BOUNDARY COVERAGE), FINDINGS.

---

## V-04 — Lifecycle Emphasis: Phase Ownership Constraints Registered in Numbered Preamble

**Axis:** Lifecycle emphasis (single axis)
**Hypothesis:** In prior variations, role-scoped constraints are either editorially imposed (prompt author attributes them) or sequentially enforced (role sequence makes them structural). V-04 tests a third mechanism: phase ownership naturally generates role-scoped constraints, and a numbered preamble can register those constraints before the phases are even defined. The insight is that "YOU MAY NOT modify a section owned by a different role" is both a numbered prohibition (C-16) and a role-attributed binding (C-17) when written as "[T] may not modify any row in [D]-owned tables." The preamble covers three distinct concerns: vocabulary scope (C1, C2), output format (C3), and phase ownership (C4, C5). VOCABULARY CLOSED (C-15) and the referential binding rule (C-14) are added as numbered preamble items C4 and C5, raising the aspirational floor without requiring separate sections. Lifecycle emphasis is maintained by giving each phase proportionally developed instruction and by requiring explicit phase-completion markers before advancing.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace in three phases. Each phase is owned exclusively by one role. Before phases begin, the CONSTRAINT REGISTRY establishes the rules that govern all phases. Read the registry completely before producing any output.

---

### CONSTRAINT REGISTRY

**C1.** YOU MAY NOT introduce any state name in Phase 2 or Phase 3 that is not declared in [D]'s STATE REGISTRY. [T] owns Phases 2 and 3 and is bound by this constraint.

**C2.** YOU MAY NOT introduce any operation name in Phase 2 or Phase 3 that is not declared in [D]'s OPERATION REGISTRY. [T] owns Phases 2 and 3 and is bound by this constraint.

**C3.** YOU MAY NOT use prose paragraphs or bullet lists as the primary output format in any Phase 2 table. [T] must produce columnar tables. A prose-only operation is a missing row.

**C4.** YOU MAY NOT retroactively add states or operations after [D] declares VOCABULARY CLOSED in Phase 1. [D] is bound by this constraint as the vocabulary authority.

**C5.** YOU MAY NOT begin Phase 2 until the DECLARATION GATE confirms Phase 1 is complete and VOCABULARY CLOSED has been declared.

**C6.** YOU MAY NOT leave invariant status columns blank in the TRANSITION TABLE. [T] must record HOLDS or VIOLATED for every invariant in every row.

---

### ROLES

**[D] Domain Expert**
Auto-selected: Sales expert (Lead / Qualified Lead / Opportunity / Proposal / Closed Won / Closed Lost), Customer Service expert (New / Active / On Hold / Pending / Resolved / Closed), or Finance expert (Draft / Submitted / Approved / Posted / Paid / Voided).
Owns: Phase 1 exclusively (STATE REGISTRY, OPERATION REGISTRY, INVARIANT REGISTRY, VOCABULARY CLOSED).
**Binding constraints from CONSTRAINT REGISTRY:** C4 ([D] may not retroactively expand vocabulary after VOCABULARY CLOSED). Phase 1 is [D]'s domain; [T] may not modify any Phase 1 table.

**[T] Trace Developer**
Owns: Phase 2 exclusively (TRANSITION TABLE) and Phase 3 exclusively (INVALID TRANSITIONS, RACE CONDITIONS, BOUNDARY COVERAGE, FINDINGS).
**Binding constraints from CONSTRAINT REGISTRY:** C1 ([T] may not introduce undeclared state names), C2 ([T] may not introduce undeclared operation names), C3 ([T] may not substitute prose for table rows), C5 ([T] may not open Phase 2 before DECLARATION GATE passes), C6 ([T] may not leave invariant columns blank).

---

### PHASE 1 — DECLARATION [D]

Do not advance to Phase 2 until DECLARATION GATE passes.

#### STATE REGISTRY [D]

| State ID | State Name | Defining Field Values | Entry Conditions | Terminal? |
|---------|-----------|----------------------|-----------------|-----------|

Domain vocabulary only. At least one Terminal = Yes. The binding rule for Phase 2: a state name not in this table may not appear in any Phase 2 or Phase 3 row.

#### OPERATION REGISTRY [D]

| Op ID | Operation Name | Legal Source State IDs | Target State ID | Triggering Actor |
|-------|---------------|----------------------|----------------|-----------------|

All State IDs reference STATE REGISTRY IDs. The binding rule for Phase 2: an operation name not in this table may not appear in any Phase 2 or Phase 3 row.

#### INVARIANT REGISTRY [D]

| INV ID | Invariant | Checkable Assertion | Authority Source |
|--------|-----------|--------------------|--------------------|

Minimum two invariants as boolean assertions. Authority source: business rule, SLA clause, regulation, policy.

#### VOCABULARY CLOSED [D]

> VOCABULARY CLOSED — C4 applies. States: [list]. Operations: [list]. Phase 1 is complete. [T] may proceed to DECLARATION GATE.

---

### DECLARATION GATE — Phase 1 Complete, Phase 2 Blocked Until Confirmed

C5 from CONSTRAINT REGISTRY: [T] may not begin Phase 2 until all items below are confirmed. Unconfirmed = blocked.

- [ ] **[C-01]** Every OPERATION REGISTRY entry has at least one legal source state and exactly one target state from STATE REGISTRY
- [ ] **[C-04]** All STATE REGISTRY names use domain vocabulary — no generics
- [ ] **[C-05]** INVARIANT REGISTRY has at least two invariants with checkable assertions and authority sources
- [ ] **[C-14]** Referential binding: STATE REGISTRY is the authoritative state vocabulary; OPERATION REGISTRY is the authoritative operation vocabulary; no Phase 2 or Phase 3 table may introduce a name outside these registries
- [ ] **[C-15]** VOCABULARY CLOSED is declared and contains the complete state and operation name lists

**Do not begin Phase 2 until all DECLARATION GATE items are confirmed.**

---

### PHASE 2 — TRANSITION TABLE [T]

C1, C2, C3, C6 from CONSTRAINT REGISTRY apply throughout Phase 2.

Scenario setup: [entity instance, starting state, actor, date/time context]

| # | From State (Phase 1 ID) | Operation (Phase 1 ID) | Preconditions | To State (Phase 1 ID) | Postconditions | INV-01 | INV-02 | Side Effects |
|---|------------------------|------------------------|---------------|----------------------|----------------|--------|--------|--------------|

Column rules:
- **From State / To State:** Phase 1 STATE REGISTRY IDs only (C1).
- **Operation:** Phase 1 OPERATION REGISTRY IDs only (C2).
- **Preconditions:** Minimum two testable assertions per row.
- **Postconditions:** Minimum one assertion distinct from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED — [reason]`; never blank (C6).
- **Side Effects:** Triggered rules, record changes, notifications, async jobs.

---

### TRACE GATE — Phase 2 Complete, Phase 3 Blocked Until Confirmed

Do not begin Phase 3 until all items are confirmed. Unconfirmed = blocked.

- [ ] **[C-01]** Every row has From State and To State from Phase 1 STATE REGISTRY
- [ ] **[C-02]** Every row has at least two preconditions as testable assertions
- [ ] **[C-03]** Every Phase 1 invariant is checked per row (HOLDS or VIOLATED)
- [ ] **[C-06]** Every row has at least one postcondition distinct from the To State name
- [ ] **[C-08]** TRANSITION TABLE is columnar and complete — every operation is a row; no operation exists only in prose (C3 confirmed)

**Do not begin Phase 3 until TRACE GATE is confirmed.**

---

### PHASE 3 — ADVERSARIAL REVIEW [T]

#### INVALID TRANSITIONS [T]

| # | Attempted Operation | From State | Blocking Condition | INV Reference | Risk if Bypassed |
|---|--------------------|------------|-------------------|--------------|-----------------|

Minimum one row. All names from Phase 1 registries.

#### RACE CONDITIONS [T]

| Operation A | Operation B | Unsafe Interleaving | Outcome |
|------------|------------|---------------------|---------|

If no concurrent access: "No concurrent access — [reason]."

#### BOUNDARY COVERAGE [T]

- **Initial state:** [STATE REGISTRY name; Terminal = No]
- **Terminal states:** [list all Terminal = Yes entries from STATE REGISTRY]
- **Re-entry attempt:** One operation attempted from a terminal state. Blocking condition shown.

---

### FINDINGS

Priority order. Reference phase and row.

- **P[N]:** [title] — [description]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: CONSTRAINT REGISTRY, ROLES, Phase 1 (STATE REGISTRY, OPERATION REGISTRY, INVARIANT REGISTRY, VOCABULARY CLOSED), DECLARATION GATE, Phase 2 (TRANSITION TABLE), TRACE GATE, Phase 3 (INVALID TRANSITIONS, RACE CONDITIONS, BOUNDARY COVERAGE), FINDINGS.

---

## V-05 — Combined: All Axes, Ceiling Attempt

**Axis:** Combined — phrasing register + role sequence + lifecycle emphasis + inertia framing
**Hypothesis:** No R5 variation achieved more than 7.0/10 aspirational. The ceiling requires all 10 aspirational criteria to be targeted structurally. V-05 assembles every proven mechanism from R2 through R5: numbered constraint preamble from R5 V-03 (C-16), role-scoped ROLES binding from R5 V-01/V-02 (C-17), VOCABULARY CLOSED from R5 V-02 (C-15), referential binding rule from R5 V-01 (C-14), four-phase structure and named gates from R2 V-04 (C-10), inertia challenge as Phase B before tracing from R2 V-04 (C-11), explicit prose prohibition in CONSTRAINTS (C-13), hard-stop "do not begin X until Y is complete" phrasing at every phase boundary (C-12), mandatory columnar table as Phase C primary deliverable (C-08), and terminal-state boundary coverage as a named Phase D section (C-09). The risk is structural incoherence from over-combination. The mitigation is to keep each section's purpose distinct: CONSTRAINTS registers, ROLES assigns, each phase owns exactly one deliverable, each gate references criteria by ID, VOCABULARY CLOSED is a named lifecycle event, and INERTIA is a named phase that [D] owns before [T] traces.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace in four phases. Before any phase begins, the CONSTRAINTS section registers the governing prohibitions; the ROLES section assigns each constraint to the actor that owns it. Phases advance only when gates confirm completion. Read CONSTRAINTS and ROLES completely before producing any output.

---

### CONSTRAINTS

Read this section completely before filling any table or beginning any phase.

**C1.** YOU MAY NOT introduce any state name in Phase C or Phase D that is not declared in Phase A's STATE REGISTRY. If a state name is missing, stop and return to Phase A — do not improvise.

**C2.** YOU MAY NOT introduce any operation name in Phase C or Phase D that is not declared in Phase A's OPERATION REGISTRY. If an operation name is missing, stop and return to Phase A.

**C3.** YOU MAY NOT use prose paragraphs or bullet lists as the primary output format for trace data. Every operation in Phase C must appear as a row in the TRANSITION TABLE. An operation documented only in prose is a missing row.

**C4.** YOU MAY NOT retroactively add states or operations after VOCABULARY CLOSED is declared in Phase A.

**C5.** YOU MAY NOT begin Phase C (TRANSITION TABLE) until GATE B confirms Phase A inventory and Phase B inertia are both complete.

**C6.** YOU MAY NOT leave invariant status columns blank in the TRANSITION TABLE. Every row records HOLDS or VIOLATED for every declared invariant.

**C7.** YOU MAY NOT begin Phase D (adversarial review) until GATE C confirms the TRANSITION TABLE is complete.

**C8.** YOU MAY NOT skip or loosely confirm any gate. A gate that cannot be confirmed is a blocker requiring return to the relevant phase.

---

### ROLES

**[D] Domain Expert**
Auto-selected: Sales expert (Lead / Qualified Lead / Opportunity / Proposal / Closed Won / Closed Lost), Customer Service expert (New / Active / On Hold / Pending / Resolved / Closed), or Finance expert (Draft / Submitted / Approved / Posted / Paid / Voided).
Owns: Phase A (inventory), Phase B (inertia challenge), VOCABULARY CLOSED declaration.
**Binding constraints:** C4 ([D] may not retroactively expand vocabulary after VOCABULARY CLOSED). [D] must complete Phase B inertia challenge before [T] begins Phase C.

**[T] Trace Developer**
Owns: Phase C (TRANSITION TABLE), Phase D (INVALID TRANSITIONS, RACE CONDITIONS, BOUNDARY COVERAGE), FINDINGS.
**Binding constraints:** C1 ([T] may not introduce undeclared state names), C2 ([T] may not introduce undeclared operation names), C3 ([T] may not substitute prose for table rows), C5 ([T] may not begin Phase C before GATE B passes), C6 ([T] may not leave invariant columns blank), C7 ([T] may not begin Phase D before GATE C passes), C8 ([T] must confirm all gate items; partial confirmation is a blocker, not a note).

---

### PHASE A — DECLARATION [D]

Do not begin Phase B until GATE A passes.

#### A1 — STATE REGISTRY [D]

| State ID | State Name | Defining Field Values | Entry Conditions | Terminal? |
|---------|-----------|----------------------|-----------------|-----------|

Domain vocabulary only. At least one Terminal = Yes. The referential binding rule: a state name not declared here may not appear in any Phase C, D, or findings row.

#### A2 — OPERATION REGISTRY [D]

| Op ID | Operation Name | Legal Source State IDs | Target State ID | Triggering Actor |
|-------|---------------|----------------------|----------------|-----------------|

All State IDs reference A1. The referential binding rule: an operation name not declared here may not appear in any Phase C, D, or findings row.

#### A3 — INVARIANT REGISTRY [D]

| INV ID | Invariant Name | Checkable Assertion | Authority Source |
|--------|---------------|--------------------|--------------------|

Minimum two invariants as boolean assertions. At least one must reference an authority source (business rule, SLA clause, accounting regulation, or policy).

#### VOCABULARY CLOSED [D]

After A1, A2, and A3 are complete:

> VOCABULARY CLOSED — C4 applies. States: [list all A1 names]. Operations: [list all A2 names]. No new state or operation name may be introduced by any role from this point forward. To add a name: return here, add it to the registry, re-declare VOCABULARY CLOSED, then continue.

---

### GATE A

Do not begin Phase B until all items are confirmed. Unconfirmed = Phase B is blocked.

- [ ] **[C-04]** All A1 state names use domain vocabulary — no "State A", "initial", "final", or generics
- [ ] **[C-01]** Every A2 operation has at least one legal source state and exactly one target state from A1
- [ ] **[C-05]** A3 has at least two invariants with checkable boolean assertions and authority sources
- [ ] **[C-15]** VOCABULARY CLOSED is declared with the complete name list

**Do not begin Phase B until GATE A is confirmed.**

---

### PHASE B — INERTIA CHALLENGE [D]

Before [T] traces any operation, challenge the assumptions the current process makes about {{topic}} that the platform does NOT enforce.

**Core question:** What does the current manual process (spreadsheet, email, legacy system, verbal agreement, paper form) assume about operation order or preconditions that the platform may silently allow to be bypassed?

| # | Current Process Assumption | Platform Enforced? (Y/N) | If N: Expected Enforcement Gap |
|---|--------------------------|--------------------------|-------------------------------|

Domain discovery prompts:
- *Sales:* "Opportunity can only Close Won with a signed contract — is that a platform state gate or a handshake?"
- *CS:* "Cases require customer confirmation before Resolved — enforced state precondition or verbal process?"
- *Finance:* "Invoices require manager approval before Posting — state gate or manual step?"

Minimum two assumptions. Every row with Platform Enforced = N is a candidate for Phase D INVALID TRANSITIONS.

---

### GATE B

Do not begin Phase C until all items are confirmed. Unconfirmed = Phase C is blocked per C5.

- [ ] At least two process assumptions documented
- [ ] Every assumption has Platform Enforced = Y or N verdict
- [ ] At least one N row with an Expected Enforcement Gap named (or a documented reason why no gaps exist — fully automated pipelines are rare and the explanation is itself a finding)
- [ ] **[C-14]** [T] confirms: STATE REGISTRY and OPERATION REGISTRY are authoritative; no Phase C or D table will introduce names outside them
- [ ] **[C-11]** Phase B inertia challenge is complete and precedes Phase C; at least one N row will be traced in Phase D D1

**Do not begin Phase C until GATE B is confirmed.**

---

### PHASE C — TRANSITION TABLE [T]

C1, C2, C3, C6 from CONSTRAINTS apply throughout Phase C. A missing row is a constraint violation, not a finding.

Scenario setup: [entity instance, starting state, actor, date/time context]

| # | From State (A1 ID) | Operation (A2 ID) | Preconditions | To State (A1 ID) | Postconditions | INV-01 | INV-02 | Side Effects |
|---|--------------------|-------------------|---------------|-----------------|----------------|--------|--------|--------------|

Column rules:
- **From State / To State:** A1 State IDs or names only (C1). Never introduce an undeclared name.
- **Operation:** A2 Operation IDs or names only (C2). Never introduce an undeclared operation.
- **Preconditions:** Minimum two testable assertions per row (e.g., `status == Active`, `owner_id != null`, `SLA timer is running`).
- **Postconditions:** Minimum one assertion distinct from the To State name — assert a property of the resulting state, not just its label.
- **INV-01, INV-02:** `HOLDS` or `VIOLATED — [reason]`; never blank (C6). Add INV-03 column if A3 has more invariants.
- **Side Effects:** Triggered plugins, business rules, related record changes, notifications, async jobs.

---

### GATE C

Do not begin Phase D until all items are confirmed. Unconfirmed = Phase D is blocked per C7.

- [ ] **[C-01]** Every row has a From State and To State from A1
- [ ] **[C-02]** Every row has at least two preconditions as testable assertions
- [ ] **[C-03]** Every A3 invariant checked per row (HOLDS or VIOLATED)
- [ ] **[C-06]** Every row has at least one postcondition distinct from the To State name
- [ ] **[C-08]** TRANSITION TABLE is columnar and complete — all operations are rows; no operation exists only in prose
- [ ] **[C-09]** At least one row reaches a terminal A1 state (Terminal = Yes) as its To State
- [ ] **[C-10]** Gates A, B, and C are present in this output; each references at least one criterion by ID

**Do not begin Phase D until GATE C is confirmed.**

---

### PHASE D — ADVERSARIAL REVIEW [T]

#### D1 — INVALID TRANSITIONS [T]

Begin with Phase B N-rows. For each: does the platform actually block the transition, or does it allow it?

| # | Attempted Operation (A2 ID) | From State (A1 ID) | Blocking Condition | Phase B Row | Risk if Bypassed |
|---|----------------------------|-------------------|--------------------|-------------|-----------------|

Every Phase B N-row must appear in D1. Add any additional invalid transitions not from Phase B. Minimum: one row total.

#### D2 — RACE CONDITIONS [T]

| Operation A (A2 ID) | Operation B (A2 ID) | Unsafe Interleaving | Outcome |
|--------------------|---------------------|---------------------|---------|

If no concurrent access: "No concurrent access — [reason]."

#### D3 — BOUNDARY COVERAGE [T]

- **Initial state:** [A1 state name; confirm Terminal = No]
- **Terminal states:** [list all A1 entries where Terminal = Yes]
- **Re-entry blocked:** Trace one attempt to execute an operation from a terminal state. Show the blocking condition (which precondition or invariant prevents it).

---

### GATE D (Final)

- [ ] **[C-05]** D1 has at least one row with a named blocking condition
- [ ] **[C-07]** D2 addressed — at least one row OR explicit clearance with reason
- [ ] **[C-09]** D3 complete — initial state labeled, all terminal states listed, re-entry attempt traced
- [ ] **[C-10]** All four gates (A, B, C, D) are present and each references at least one criterion by ID
- [ ] **[C-11]** Phase B inertia challenge preceded Phase C; at least one D1 row references a Phase B N-row (confirm by Phase B row number in D1 table)
- [ ] **[C-16]** CONSTRAINTS section with C1-C8 numbered "YOU MAY NOT" items appears before all phases in this output
- [ ] **[C-17]** ROLES section assigns binding constraints to [D] and [T] by name — at least one role-scoped obligation per role

**Any item unconfirmed → correct the relevant phase.**

---

### FINDINGS

Priority order. Reference phase, gate, and row.

- **P[N]:** [title] — [description, phase and row reference]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: CONSTRAINTS, ROLES, Phase A (A1 STATE REGISTRY, A2 OPERATION REGISTRY, A3 INVARIANT REGISTRY, VOCABULARY CLOSED), GATE A, Phase B (INERTIA CHALLENGE), GATE B, Phase C (TRANSITION TABLE), GATE C, Phase D (D1 INVALID TRANSITIONS, D2 RACE CONDITIONS, D3 BOUNDARY COVERAGE), GATE D, FINDINGS.
