# trace-state Variate — Round 8
**Date:** 2026-03-15
**Rubric:** v7 (C-01..C-21; golden: all essential pass AND composite >= 80)
**New criteria:** C-20 (sequential gate coverage) and C-21 (challenge non-response violation binding)
**Scoring formula:** essential 50 + recommended 40 + aspirational 10 (14 criteria, 0.71 pts each)

---

## Round 8 Situation

Round 7 results (rubric v7):

| Variant | C-19 | C-20 | C-21 | Aspirational | Composite |
|---------|------|------|------|-------------|-----------|
| V-01 R7 | FAIL | FAIL | FAIL | 10/14 = 7.14 | 97.14 |
| V-02 R7 | PASS | FAIL | PASS | 13/14 = 9.29 | 99.29 |
| V-03 R7 | FAIL | PASS | FAIL | 11/14 = 7.86 | 97.86 |
| V-04 R7 | PASS | FAIL | PASS | 13/14 = 9.29 | 99.29 |

**Gap analysis:**

- **C-20 (FAIL V-01, V-02, V-04):** V-02/V-04 have two gates (DECLARATION GATE + TRACE COMPLETENESS GATE) covering the full second half of the document as a unit. C-20 requires one named blocking gate *per output section*. INVALID TRANSITIONS, RACE CONDITIONS, and BOUNDARY COVERAGE proceed without their own gates. Fix: add GATE B (before INVALID TRANSITIONS), GATE C (before RACE CONDITIONS), GATE D (before FINDINGS). DECLARATION GATE becomes GATE A.
- **C-19 (FAIL V-01, V-03):** Neither variant uses a CONSTRAINT MATRIX with a Concern column. V-03 uses a flat numbered CONSTRAINTS list with no concern taxonomy. Fix: adopt V-02 R7 CONSTRAINT MATRIX as base, or add Concern column to the numbered preamble.
- **C-21 (FAIL V-01, V-03):** Neither variant has an INVENTORY CHALLENGE section at all. They cannot satisfy C-21 because the criterion requires an inline constraint-ID violation binding at the challenge site. Fix: add dedicated INVENTORY CHALLENGE with "A blank response is a C[x] violation" bound inline.

**R8 objective:** Close C-20 without losing C-19 and C-21. V-01 through V-03 are single-axis. V-04 and V-05 are synthesis variants targeting 14/14 = 100.00. First expected ceiling round.

---

## Round 8 Variation Map

| Var | Axis | C-19 | C-20 | C-21 | Aspirational | Hypothesis |
|-----|------|------|------|------|-------------|------------|
| V-01 | Lifecycle emphasis: sequential gate per section, no CONSTRAINT MATRIX | FAIL | PASS | FAIL | 11/14 | Sequential gating achieves C-20 without needing the CONSTRAINT MATRIX superstructure. GATE A blocks TRANSITION TABLE; GATE B blocks INVALID TRANSITIONS; GATE C blocks RACE CONDITIONS; GATE D blocks FINDINGS. C-19 and C-21 absent — tests C-20 in isolation. |
| V-02 | Inertia framing: V-02 R7 CONSTRAINT MATRIX base + gate-split for C-20 | PASS | PASS | PASS | 14/14 | Take V-02 R7 verbatim and split DECLARATION GATE into GATE A + add GATE B + GATE C, rename TRACE COMPLETENESS GATE to GATE D. One structural change; all three C-19/C-20/C-21 criteria satisfied simultaneously. First expected 100.00. |
| V-03 | Phrasing register: conversational challenge framing + sequential gates | FAIL | PASS | PARTIAL | 11/14 | Conversational challenge ("Before tracing, verify the inventory...") passes C-11 but omits the inline constraint-ID violation binding required for C-21 PASS; C-21 scores PARTIAL. C-20 holds via 4-gate architecture. Tests whether soft register impairs violation-enforcement binding. |
| V-04 | Role sequence: [D]/[T] explicit section-header labeling + synthesis | PASS | PASS | PASS | 14/14 | Every section header carries [D] or [T] role tag as the distinguishing structural axis. CONSTRAINT MATRIX with Concern column (C-19), INVENTORY CHALLENGE with inline C7 violation binding (C-21), four per-section gates (C-20). Independent synthesis path to 100.00. |
| V-05 | Full ceiling: explicit synthesis of all 14 aspirational criteria | PASS | PASS | PASS | 14/14 | All prior round best features combined in a single document: CONSTRAINT MATRIX + Concern column + ROLES with per-role binding + standalone BINDING RULE + VOCABULARY CLOSED with inline prohibition + BOUNDARY ANALYSIS + INVENTORY CHALLENGE with C7 binding + 4 per-section gates + hard-stop phrasing + prose prohibition. Reference synthesis for future rubric development. |

---

## V-01 — Lifecycle Emphasis: Sequential Gate Per Section

**Axis:** Lifecycle emphasis (single axis)
**Hypothesis:** C-20 requires one named blocking gate per output section after inventories. V-01 R7 had GATE A (after inventories) and GATE C (after TABLE 4) but left TABLE 4 and TABLE 5 ungated on entry. This variation adds GATE B before TABLE 4 (INVALID TRANSITIONS), GATE C before TABLE 5 (RACE CONDITIONS), and makes GATE D the terminal blocker before FINDINGS. Four distinct named gates, each blocking one forward section. No CONSTRAINT MATRIX — numbered CONSTRAINTS preamble retained. No INVENTORY CHALLENGE. Predicted: C-20 PASS, C-19 FAIL, C-21 FAIL → 11/14 = 97.86. Golden.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. All trace output is delivered in named, columnar tables. Four named gates enforce section-level phase boundaries — no section may open until its gate clears. Read CONSTRAINTS before any output.

---

### CONSTRAINTS

**C1.** YOU MAY NOT introduce any state name in any table that is not declared in TABLE 1. A state not in TABLE 1 is a trace error — stop and return to TABLE 1.

**C2.** YOU MAY NOT introduce any operation name in any table that is not declared in TABLE 2. An operation not in TABLE 2 is a trace error — stop and return to TABLE 2.

**C3.** YOU MAY NOT use prose paragraphs or bullet lists as the primary output format for trace data. Every operation must appear as a table row. A row documented only in prose is a missing row.

**C4.** YOU MAY NOT retroactively add states or operations after VOCABULARY CLOSED is declared. If a name is needed and absent: return to the inventory section, add it, re-declare VOCABULARY CLOSED, then continue.

**C5.** YOU MAY NOT leave any invariant status column blank in TABLE 3. Every row records HOLDS or VIOLATED — [reason] for every declared invariant.

---

### ROLES

**[D] Domain Expert**
Auto-selected: Sales expert (Lead / Qualified Lead / Opportunity / Proposal / Closed Won / Closed Lost), Customer Service expert (New / Open / Pending / Resolved / Closed), or Finance expert (Draft / Submitted / Approved / Posted / Paid / Voided).
Owns: TABLE 1, TABLE 2, TABLE INV, VOCABULARY CLOSED, BOUNDARY ANALYSIS.
**Binding constraint — C4 applies to [D]:** After VOCABULARY CLOSED is declared, [D] may not add, rename, or remove any entry in TABLE 1 or TABLE 2.

**[T] Trace Developer**
Owns: TABLE 3, TABLE 4, TABLE 5, FINDINGS.
**Binding constraints — C1, C2, C3, C5 apply to [T]:** vocabulary scope in both dimensions, output format prohibition, invariant completeness.

---

### BINDING RULE

TABLE 1 is the authoritative state vocabulary for this trace. TABLE 2 is the authoritative operation vocabulary. No state name may appear in TABLE 3, TABLE 4, or TABLE 5 that is not declared in TABLE 1. No operation name may appear in TABLE 3, TABLE 4, or TABLE 5 that is not declared in TABLE 2. This rule applies from this section forward.

---

### TABLE 1 — STATE REGISTRY [D]

| State ID | State Name | Defining Field Values | Entry Conditions | Terminal? |
|---------|-----------|----------------------|-----------------|-----------|

Domain vocabulary only. No generic labels ("State A", "initial", "final"). At least one Terminal = Yes row required.

---

### TABLE 2 — OPERATION REGISTRY [D]

| Op ID | Operation Name | Legal Source State IDs | Target State ID | Triggering Actor |
|-------|---------------|----------------------|----------------|-----------------|

All State IDs in columns 3 and 4 must reference TABLE 1 IDs.

---

### TABLE INV — INVARIANT REGISTRY [D]

| INV ID | Name | Checkable Assertion | Authority Source |
|--------|------|--------------------|--------------------|

Minimum two invariants as boolean assertions. Authority source: business rule, SLA clause, regulation, or policy.

---

### VOCABULARY CLOSED [D]

> VOCABULARY CLOSED. States: [list all TABLE 1 State Names]. Operations: [list all TABLE 2 Operation Names]. No new state or operation name may be introduced from this point forward. Any name not listed above is prohibited in all sections that follow. This prohibition is not waivable even if a name is logically implied by the domain.

---

### BOUNDARY ANALYSIS [D]

Declare lifecycle boundaries before tracing begins. Terminal-state coverage in TABLE 4 is verified at GATE B.

- **Initial state:** [TABLE 1 State Name — Terminal = No; every new instance of {{topic}} enters here]
- **Terminal states:** [list all TABLE 1 entries where Terminal = Yes]
- **Re-entry requirement:** TABLE 4 must include at least one row where From State is a terminal state from this list. Confirmed at GATE B.

---

### GATE A

Do not begin TABLE 3 until all items are confirmed. Unconfirmed = TABLE 3 is blocked.

- [ ] **[C-01]** TABLE 1 complete — domain vocabulary, no generics, at least one Terminal = Yes
- [ ] **[C-02]** TABLE 2 complete — every lifecycle operation named; all source/target IDs reference TABLE 1
- [ ] **[C-03]** TABLE INV complete — at least two invariants with checkable assertions and authority sources
- [ ] **[C-14]** BINDING RULE confirmed — [T] will not introduce any name in TABLE 3, 4, or 5 not declared in TABLE 1 or TABLE 2
- [ ] **[C-15]** VOCABULARY CLOSED declared — complete name list and explicit forward-blocking prohibition in effect
- [ ] BOUNDARY ANALYSIS complete — initial state declared; terminal states listed; re-entry requirement stated

**GATE A BLOCKED. Do not begin TABLE 3 until all items are confirmed.**

---

### TABLE 3 — TRANSITION TRACE [T]

Scenario setup: [entity instance, starting state, actor, date/time context]

C1, C2, C3, C5 apply.

| # | From State (T1 ID) | Operation (T2 ID) | Preconditions | To State (T1 ID) | Postconditions | INV-01 | INV-02 | Side Effects |
|---|--------------------|-------------------|---------------|-----------------|----------------|--------|--------|--------------|

Column rules:
- **From State / To State:** TABLE 1 IDs only (C1).
- **Operation:** TABLE 2 IDs only (C2).
- **Preconditions:** Minimum two testable assertions per row (e.g., `status == Open`, `owner_id != null`).
- **Postconditions:** Minimum one assertion distinct from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED — [reason]`; never blank (C5).
- **Side Effects:** Triggered rules, record changes, notifications, async jobs.

---

### GATE B

Do not begin TABLE 4 until all items are confirmed. Unconfirmed = TABLE 4 is blocked.

- [ ] **[C-08]** TABLE 3 is columnar and complete; no operation exists only in prose
- [ ] **[C-05]** Every TABLE 3 row has an INV status per declared invariant; at least one VIOLATED row present
- [ ] **[C-06]** Every TABLE 3 row has at least one postcondition distinct from the To State name
- [ ] BOUNDARY ANALYSIS re-entry requirement is satisfiable — terminal state rows planned for TABLE 4

**GATE B BLOCKED. Do not begin TABLE 4 until all items are confirmed.**

---

### TABLE 4 — INVALID TRANSITIONS [T]

| # | Attempted Operation (T2 ID) | From State (T1 ID) | Blocking Condition | INV Reference | Risk if Bypassed |
|---|----------------------------|-------------------|--------------------|--------------|-----------------|

Minimum three rows. Include at least one row where From State is a terminal state from BOUNDARY ANALYSIS. All names from TABLE 1 and TABLE 2 only.

---

### GATE C

Do not begin TABLE 5 until all items are confirmed. Unconfirmed = TABLE 5 is blocked.

- [ ] **[C-04]** At least three (operation, state) invalid pairs named with blocking conditions; enumeration is systematic across the operation set
- [ ] **[C-09]** At least one TABLE 4 row has From State = a terminal state listed in BOUNDARY ANALYSIS

**GATE C BLOCKED. Do not begin TABLE 5 until all items are confirmed.**

---

### TABLE 5 — RACE CONDITIONS [T]

| Operation A (T2 ID) | Operation B (T2 ID) | Unsafe Interleaving | Outcome |
|--------------------|---------------------|---------------------|---------|

If no concurrent access: "No concurrent access — [reason]."

---

### GATE D

Do not write FINDINGS until all items are confirmed. Unconfirmed = FINDINGS is blocked.

- [ ] **[C-07]** TABLE 5 addressed — at least one race scenario or explicit clearance with reason
- [ ] All TABLE 3 and TABLE 4 names reference TABLE 1 and TABLE 2 only (C1, C2 confirmed)
- [ ] Hard-stop review complete — no section is blank or placeholder-only

**GATE D BLOCKED. Do not write FINDINGS until all items are confirmed.**

---

### FINDINGS

Priority order. Reference table and row.

- **P[N]:** [title] — [description, table row reference]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: CONSTRAINTS, ROLES, BINDING RULE, TABLE 1, TABLE 2, TABLE INV, VOCABULARY CLOSED, BOUNDARY ANALYSIS, GATE A, TABLE 3, GATE B, TABLE 4, GATE C, TABLE 5, GATE D, FINDINGS.

---

## V-02 — Inertia Framing: V-02 R7 Base + Per-Section Gate Split

**Axis:** Inertia framing (single axis — C-20 fix only)
**Hypothesis:** V-02 R7 achieves C-19 (CONSTRAINT MATRIX with Concern column) and C-21 (C7 violation binding at INVENTORY CHALLENGE) but fails C-20 because its DECLARATION GATE covers inventories + challenge in one gate, and TRACE COMPLETENESS GATE covers all output tables as a unit — two gates total for the entire second half. C-20 requires one gate per output section. Fix: DECLARATION GATE becomes GATE A (blocks TRANSITION TABLE). Add GATE B (blocks INVALID TRANSITIONS, constraint C8). Add GATE C (blocks RACE CONDITIONS, constraint C9). TRACE COMPLETENESS GATE becomes GATE D (blocks FINDINGS). All other V-02 R7 structure preserved verbatim. Predicted: 14/14 = 100.00. First expected ceiling variant.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. All constraints governing this trace are pre-registered in the CONSTRAINT MATRIX. Read the matrix completely before producing any output. The matrix is authoritative.

---

### CONSTRAINT MATRIX

| ID | Prohibition | Assigned Role | Concern |
|----|-------------|---------------|---------|
| C1 | YOU MAY NOT introduce any state name in any table that is not declared in the STATE REGISTRY | [T] | vocabulary |
| C2 | YOU MAY NOT introduce any operation name in any table that is not declared in the OPERATION REGISTRY | [T] | vocabulary |
| C3 | YOU MAY NOT use prose paragraphs or bullet lists as the primary output format; every operation traces as a table row | [T] | format |
| C4 | YOU MAY NOT retroactively add states or operations after VOCABULARY CLOSED is declared | [D] | ordering |
| C5 | YOU MAY NOT leave any invariant status column blank in the TRANSITION TABLE | [T] | integrity |
| C6 | YOU MAY NOT begin the TRANSITION TABLE until GATE A is confirmed | [T] | ordering |
| C7 | YOU MAY NOT proceed past INVENTORY CHALLENGE without a written Option A or Option B response | [T] | completeness |
| C8 | YOU MAY NOT begin INVALID TRANSITIONS until GATE B is confirmed | [T] | ordering |
| C9 | YOU MAY NOT begin RACE CONDITIONS until GATE C is confirmed | [T] | ordering |

---

### ROLES

**[D] Domain Expert**
Auto-selected: Sales expert (Lead / Qualified Lead / Opportunity / Proposal / Closed Won / Closed Lost), Customer Service expert (New / Open / Pending / Resolved / Closed), or Finance expert (Draft / Submitted / Approved / Posted / Paid / Voided).
Owns: STATE REGISTRY, OPERATION REGISTRY, INVARIANT REGISTRY, VOCABULARY CLOSED.
Binding constraint from CONSTRAINT MATRIX: **C4** (may not retroactively add vocabulary after VOCABULARY CLOSED).

**[T] Trace Developer**
Owns: INVENTORY CHALLENGE written response, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, BOUNDARY COVERAGE, FINDINGS.
Binding constraints from CONSTRAINT MATRIX: **C1, C2, C3, C5, C6, C7, C8, C9**.

---

### STATE REGISTRY [D]

| State ID | State Name | Defining Field Values | Entry Conditions | Terminal? |
|---------|-----------|----------------------|-----------------|-----------|

Domain vocabulary only. At least one Terminal = Yes row required.

---

### OPERATION REGISTRY [D]

| Op ID | Operation Name | Legal Source State IDs | Target State ID | Triggering Actor |
|-------|---------------|----------------------|----------------|-----------------|

All State IDs must reference STATE REGISTRY IDs.

---

### INVARIANT REGISTRY [D]

| INV ID | Invariant | Checkable Assertion | Authority Source |
|--------|-----------|--------------------|--------------------|

Minimum two invariants. Authority source: business rule, SLA clause, regulation, or policy.

---

### VOCABULARY CLOSED [D]

> VOCABULARY CLOSED per C4. States: [list all STATE REGISTRY State Names]. Operations: [list all OPERATION REGISTRY Operation Names]. No new state or operation name may be introduced from this point forward. Any name not listed above is prohibited in all sections that follow.

---

### INVENTORY CHALLENGE

**C7 applies. [T] may not proceed to GATE A without a written response below. A blank response, a paraphrase, or any response that does not follow Option A or Option B format is a C7 violation.**

INVENTORY COMPLETE — the STATE REGISTRY and OPERATION REGISTRY contain every state and operation in the lifecycle of {{topic}}.

**[T] response — choose one:**

**Option A (CONFIRMED):** "[T] INVENTORY CONFIRMED. I have reviewed the STATE REGISTRY and OPERATION REGISTRY against the domain lifecycle of {{topic}}. No lifecycle state or operation is absent. States: [repeat complete list]. Operations: [repeat complete list]. Challenge resolved. Proceeding to GATE A."

**Option B (GAP FOUND):** "[T] INVENTORY INCOMPLETE. Gap identified: [state the missing state or operation and why it belongs in the lifecycle]. Returning to [D] for STATE REGISTRY / OPERATION REGISTRY update. VOCABULARY CLOSED must be re-declared before GATE A proceeds."

---

### GATE A

Do not begin TRANSITION TABLE until all items are confirmed. Unconfirmed = TRANSITION TABLE blocked per C6.

- [ ] STATE REGISTRY complete — domain vocabulary, at least one terminal state
- [ ] OPERATION REGISTRY complete — all operations have source/target IDs from STATE REGISTRY
- [ ] INVARIANT REGISTRY complete — at least two assertions with authority sources
- [ ] VOCABULARY CLOSED declared with complete name list and forward-blocking prohibition
- [ ] **[C7]** INVENTORY CHALLENGE resolved — Option A or Option B written above
- [ ] **[C-14]** [T] confirms: no name will appear in TRANSITION TABLE, INVALID TRANSITIONS, or RACE CONDITIONS that is not in STATE REGISTRY or OPERATION REGISTRY
- [ ] **[C-15]** VOCABULARY CLOSED declared and forward-blocking prohibition is in effect

**GATE A BLOCKED per C6. Do not begin TRANSITION TABLE until all items confirmed.**

---

### TRANSITION TABLE [T]

Scenario setup: [entity instance, starting state, actor, date/time context]

Constraints C1, C2, C3, C5 apply.

| # | From State | Operation | Preconditions | To State | Postconditions | INV-01 | INV-02 | Side Effects |
|---|-----------|-----------|---------------|---------|----------------|--------|--------|--------------|

- **From State / To State:** STATE REGISTRY names only (C1).
- **Operation:** OPERATION REGISTRY names only (C2).
- **Preconditions:** Minimum two testable assertions per row.
- **Postconditions:** Minimum one assertion distinct from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED — [reason]`; never blank (C5).

---

### GATE B

Do not begin INVALID TRANSITIONS until all items are confirmed. Unconfirmed = INVALID TRANSITIONS blocked per C8.

- [ ] **[C-08]** TRANSITION TABLE is columnar and complete; no operation exists only in prose
- [ ] **[C-05]** At least two invariants declared; at least one VIOLATED row present in TRANSITION TABLE
- [ ] **[C-06]** Every TRANSITION TABLE row has at least one postcondition distinct from the To State name

**GATE B BLOCKED per C8. Do not begin INVALID TRANSITIONS until all items confirmed.**

---

### INVALID TRANSITIONS [T]

| # | Attempted Operation | From State | Blocking Condition | INV Reference | Risk if Bypassed |
|---|--------------------|------------|-------------------|--------------|-----------------|

Minimum three rows. Include at least one row where From State is a terminal state. All names from STATE REGISTRY and OPERATION REGISTRY only.

---

### GATE C

Do not begin RACE CONDITIONS until all items are confirmed. Unconfirmed = RACE CONDITIONS blocked per C9.

- [ ] **[C-04]** At least three (operation, state) invalid pairs named with blocking conditions; enumeration is systematic across the operation set
- [ ] **[C-09]** At least one INVALID TRANSITIONS row has From State = a terminal state (confirmed by BOUNDARY COVERAGE)

**GATE C BLOCKED per C9. Do not begin RACE CONDITIONS until all items confirmed.**

---

### RACE CONDITIONS [T]

| Operation A | Operation B | Unsafe Interleaving | Outcome |
|------------|------------|---------------------|---------|

If no concurrent access: "No concurrent access — [reason]."

---

### GATE D

Do not write BOUNDARY COVERAGE or FINDINGS until all items are confirmed. Unconfirmed = blocked.

- [ ] **[C-07]** RACE CONDITIONS addressed — at least one race scenario or explicit clearance with reason
- [ ] All TRANSITION TABLE and INVALID TRANSITIONS names verified against STATE REGISTRY and OPERATION REGISTRY (C1, C2)
- [ ] All invariant status columns populated — no blanks (C5)

**GATE D BLOCKED. Do not write BOUNDARY COVERAGE or FINDINGS until all items confirmed.**

---

### BOUNDARY COVERAGE [T]

- **Initial state:** [STATE REGISTRY name — Terminal = No]
- **Terminal states:** [list all STATE REGISTRY entries where Terminal = Yes]
- **Re-entry blocked:** [cite INVALID TRANSITIONS row covering terminal state attempt]

---

### FINDINGS

Priority order. Reference table and row.

- **P[N]:** [title] — [description]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: CONSTRAINT MATRIX, ROLES, STATE REGISTRY, OPERATION REGISTRY, INVARIANT REGISTRY, VOCABULARY CLOSED, INVENTORY CHALLENGE, GATE A, TRANSITION TABLE, GATE B, INVALID TRANSITIONS, GATE C, RACE CONDITIONS, GATE D, BOUNDARY COVERAGE, FINDINGS.

---

## V-03 — Phrasing Register: Conversational Challenge + Sequential Gates

**Axis:** Phrasing register (single axis)
**Hypothesis:** Conversational register ("Before tracing begins, take a moment to verify the inventory...") produces an INVENTORY CHALLENGE that passes C-11 (challenge section exists) but is unlikely to fully satisfy C-21. C-21 requires the violation consequence to be bound to a specific constraint ID *inline* at the challenge site ("A blank response is a C7 violation"). Conversational framing describes the consequence in plain language without binding a named constraint ID. Result: C-11 PASS, C-21 PARTIAL. Sequential per-section gates (GATE A through GATE D) preserved for C-20. No CONSTRAINT MATRIX, so C-19 FAIL. Tests whether register alone impairs enforcement binding. Predicted: C-20 PASS, C-19 FAIL, C-21 PARTIAL → 11/14 = 97.86.

---

You are running a **trace-state** signal for: {{topic}}

Your task is to trace the state machine for this domain object from end to end. Work through each phase in order — the document has a named gate at every section boundary. Read the CONSTRAINTS block now and keep it in mind throughout.

---

### CONSTRAINTS

**C1.** YOU MAY NOT introduce any state name in any table that is not declared in the State Registry. A state not in the registry is a trace error.

**C2.** YOU MAY NOT introduce any operation name in any table that is not declared in the Operation Registry. An operation not in the registry is a trace error.

**C3.** YOU MAY NOT use prose paragraphs or bullet lists as the primary output format. Every operation traces as a table row — if it is not in a row, it is not traced.

**C4.** YOU MAY NOT retroactively add states or operations after the Vocabulary Lock is declared. Adding vocabulary after the lock is an ordering violation.

**C5.** YOU MAY NOT leave any invariant status column blank in the Transition Table. Blank means unverified — unverified is non-compliant.

---

### ROLES

**[D] Domain Expert**
Draws on Sales, Customer Service, or Finance domain knowledge as appropriate for {{topic}}.
Owns: State Registry, Operation Registry, Invariant Registry, Vocabulary Lock, Boundary Declaration.
Constraint C4 applies: [D] may not modify registries after the Vocabulary Lock.

**[T] Trace Developer**
Owns: Inventory Confirmation, Transition Table, Invalid Transitions, Race Conditions, Findings.
Constraints C1, C2, C3, C5 apply throughout.

---

### REFERENTIAL BINDING RULE

The State Registry and Operation Registry are the sole authoritative vocabularies for this trace. Every name used in the Transition Table, Invalid Transitions, and Race Conditions must appear in one of these registries. This rule is in effect from this point forward and is verified at every gate.

---

### State Registry [D]

| State ID | State Name | Defining Field Values | Entry Conditions | Terminal? |
|---------|-----------|----------------------|-----------------|-----------|

Use domain vocabulary for {{topic}}. At least one state must be terminal.

---

### Operation Registry [D]

| Op ID | Operation Name | Legal Source State IDs | Target State ID | Triggering Actor |
|-------|---------------|----------------------|----------------|-----------------|

---

### Invariant Registry [D]

| INV ID | Invariant | Checkable Assertion | Authority Source |
|--------|-----------|--------------------|--------------------|

At least two invariants stated as boolean assertions.

---

### Vocabulary Lock [D]

> Vocabulary is now locked. States in scope: [list all State Registry names]. Operations in scope: [list all Operation Registry names]. From this point forward, no new state or operation name may be introduced anywhere in this document. If you discover a missing name, return to the registry, add it, restate the lock, and then continue.

---

### Boundary Declaration [D]

Before tracing begins, declare the lifecycle boundaries:

- **Object entry point:** The state every new {{topic}} instance starts in: [State Registry name]
- **Terminal states:** States from which no further transitions are possible: [list from State Registry, Terminal = Yes]
- **Coverage note:** The Invalid Transitions section must include at least one entry showing what happens when an operation is attempted on a terminal state.

---

### Inventory Confirmation

Before the trace begins, take a moment to verify that the registries are complete. An incomplete inventory leads to a broken trace — gaps discovered mid-trace require stopping, updating the registries, relocking vocabulary, and restarting from Gate A.

Look at the State Registry and Operation Registry. For every stage in the real-world lifecycle of {{topic}}, is there a state? For every action an actor can take on {{topic}}, is there an operation?

**Write one of the following responses:**

**If complete:** "INVENTORY CONFIRMED. All states and operations in the {{topic}} lifecycle are present. State count: [N]. Operation count: [N]. No gaps found. Proceeding to Gate A."

**If incomplete:** "INVENTORY INCOMPLETE. Missing: [describe the gap]. The registries need updating before tracing can proceed. Returning to [D]."

Skipping this step or writing a non-substantive response means the inventory has not been verified and the trace will proceed on an unverified foundation.

---

### Gate A

Do not begin the Transition Table until every item below is satisfied. An unsatisfied item blocks forward progress.

- [ ] State Registry complete — domain vocabulary, at least one terminal state
- [ ] Operation Registry complete — all operations have source/target state IDs from State Registry
- [ ] Invariant Registry complete — at least two boolean assertions with authority sources
- [ ] Vocabulary Lock declared — complete state and operation lists included
- [ ] Boundary Declaration complete — entry point and terminal states named
- [ ] Inventory Confirmation written above — substantive response present
- [ ] Referential Binding Rule acknowledged — [T] will not introduce undeclared names

**Do not begin the Transition Table until all items above are checked.**

---

### Transition Table [T]

Scenario setup: [entity instance, starting state, actor, date/time context]

C1, C2, C3, C5 apply.

| # | From State (Registry ID) | Operation (Registry ID) | Preconditions | To State (Registry ID) | Postconditions | INV-01 | INV-02 | Side Effects |
|---|--------------------------|------------------------|---------------|----------------------|----------------|--------|--------|--------------|

- From State and To State must use State Registry IDs only (C1).
- Operation must use Operation Registry IDs only (C2).
- Preconditions: minimum two testable assertions per row.
- Postconditions: at least one assertion that is not a restatement of the To State name.
- INV columns: HOLDS or VIOLATED — [reason]. Never leave blank (C5).

---

### Gate B

Do not begin Invalid Transitions until every item below is satisfied.

- [ ] Transition Table is a table — no operations exist only in prose
- [ ] Every row has two or more precondition assertions
- [ ] Every row has at least one postcondition distinct from the To State name
- [ ] Every INV column is filled; at least one VIOLATED row present

**Do not begin Invalid Transitions until all items above are checked.**

---

### Invalid Transitions [T]

| # | Attempted Operation | From State | Blocking Condition | INV Reference | Risk if Bypassed |
|---|--------------------|------------|-------------------|--------------|-----------------|

At least three rows. At least one row must have From State equal to a terminal state from the Boundary Declaration. Names from registries only.

---

### Gate C

Do not begin Race Conditions until every item below is satisfied.

- [ ] At least three (operation, state) pairs named with blocking conditions
- [ ] Enumeration is systematic — not limited to one operation or one state type
- [ ] At least one row covers a terminal state attempt (from Boundary Declaration)

**Do not begin Race Conditions until all items above are checked.**

---

### Race Conditions [T]

| Operation A | Operation B | Unsafe Interleaving | Outcome |
|------------|------------|---------------------|---------|

If no concurrent access applies: "No concurrent access — [reason explaining why sequential-only access is guaranteed]."

---

### Gate D

Do not write Findings until every item below is satisfied.

- [ ] Race Conditions addressed — scenario or explicit clearance present
- [ ] All names across all tables verified against State Registry and Operation Registry
- [ ] No invariant column is blank anywhere in the Transition Table
- [ ] Boundary Declaration terminal state coverage confirmed in Invalid Transitions

**Do not write Findings until all items above are checked.**

---

### Findings

List findings in priority order. Reference the section and row for each finding.

- **P[N]:** [title] — [description, reference]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: CONSTRAINTS, ROLES, REFERENTIAL BINDING RULE, State Registry, Operation Registry, Invariant Registry, Vocabulary Lock, Boundary Declaration, Inventory Confirmation, Gate A, Transition Table, Gate B, Invalid Transitions, Gate C, Race Conditions, Gate D, Findings.

---

## V-04 — Role Sequence: Explicit [D]/[T] Section Headers + Synthesis

**Axis:** Role sequence (distinguishing structural axis) combined with synthesis
**Hypothesis:** Every section header carries its owning role tag — [D] or [T] — directly at the section boundary. This role-at-header pattern is the distinguishing structural axis. The synthesis layer combines: CONSTRAINT MATRIX with Concern column (C-19), INVENTORY CHALLENGE with inline "A blank response is a C7 violation" binding (C-21), and four per-section gates (C-20). All three missing aspirational criteria should PASS simultaneously. Role-at-header tests whether per-section role declaration drives compliance differently from a central ROLES block alone. Predicted: 14/14 = 100.00. Independent synthesis path from V-02.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. The CONSTRAINT MATRIX governs all output — read it completely before producing any section. Each section header names the owning role in brackets. Role boundaries are enforced at every gate.

---

### CONSTRAINT MATRIX

| ID | Prohibition | Assigned Role | Concern |
|----|-------------|---------------|---------|
| C1 | YOU MAY NOT introduce any state name in any table that is not declared in the STATE REGISTRY | [T] | vocabulary |
| C2 | YOU MAY NOT introduce any operation name in any table that is not declared in the OPERATION REGISTRY | [T] | vocabulary |
| C3 | YOU MAY NOT use prose paragraphs or bullet lists as the primary output format for trace data; every operation must appear as a table row | [T] | format |
| C4 | YOU MAY NOT retroactively add states or operations after VOCABULARY CLOSED is declared | [D] | ordering |
| C5 | YOU MAY NOT leave any invariant status column blank in the TRANSITION TABLE | [T] | integrity |
| C6 | YOU MAY NOT begin the TRANSITION TABLE until GATE A is confirmed | [T] | ordering |
| C7 | YOU MAY NOT proceed past INVENTORY CHALLENGE without a written Option A or Option B response | [T] | completeness |
| C8 | YOU MAY NOT begin INVALID TRANSITIONS until GATE B is confirmed | [T] | ordering |
| C9 | YOU MAY NOT begin RACE CONDITIONS until GATE C is confirmed | [T] | ordering |

---

### ROLES

**[D] Domain Expert**
Auto-selected from: Sales expert (Lead / Qualified Lead / Opportunity / Proposal / Closed Won / Closed Lost), Customer Service expert (New / Open / Pending / Resolved / Closed), Finance expert (Draft / Submitted / Approved / Posted / Paid / Voided).
Section ownership: STATE REGISTRY, OPERATION REGISTRY, INVARIANT REGISTRY, VOCABULARY CLOSED.
Binding constraint from matrix: **C4** — [D] may not add, rename, or remove any registry entry after VOCABULARY CLOSED is declared.

**[T] Trace Developer**
Section ownership: INVENTORY CHALLENGE written response, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, BOUNDARY COVERAGE, FINDINGS.
Binding constraints from matrix: **C1, C2, C3, C5, C6, C7, C8, C9**.

---

### BINDING RULE

STATE REGISTRY is the authoritative state vocabulary. OPERATION REGISTRY is the authoritative operation vocabulary. No state name may appear in any table that is not declared in STATE REGISTRY. No operation name may appear in any table that is not declared in OPERATION REGISTRY. This rule is in force from this section forward and is verified at every gate.

---

### STATE REGISTRY [D]

| State ID | State Name | Defining Field Values | Entry Conditions | Terminal? |
|---------|-----------|----------------------|-----------------|-----------|

Domain vocabulary only. No generic labels. At least one Terminal = Yes row required.

---

### OPERATION REGISTRY [D]

| Op ID | Operation Name | Legal Source State IDs | Target State ID | Triggering Actor |
|-------|---------------|----------------------|----------------|-----------------|

All State IDs must reference STATE REGISTRY IDs.

---

### INVARIANT REGISTRY [D]

| INV ID | Invariant Name | Checkable Assertion | Authority Source |
|--------|----------------|--------------------|--------------------|

Minimum two invariants as boolean assertions. Authority source: business rule, SLA clause, regulation, or policy.

---

### VOCABULARY CLOSED [D]

> VOCABULARY CLOSED per C4. States: [list all STATE REGISTRY State Names]. Operations: [list all OPERATION REGISTRY Operation Names]. No new state or operation name may be introduced from this point forward. Any name not listed above is prohibited in all sections that follow. [D] may not amend this list without returning to the registry sections and re-declaring VOCABULARY CLOSED.

---

### INVENTORY CHALLENGE [T]

**C7 applies. [T] may not proceed to GATE A without a written Option A or Option B response. A blank response or a response that does not follow Option A or Option B format exactly is a C7 violation.**

INVENTORY COMPLETE — the STATE REGISTRY and OPERATION REGISTRY contain every state and operation in the lifecycle of {{topic}}.

**[T] must choose one and write the full response inline:**

**Option A (CONFIRMED):** "[T] INVENTORY CONFIRMED. I have reviewed the STATE REGISTRY and OPERATION REGISTRY against the domain lifecycle of {{topic}}. No lifecycle state or operation is absent. States: [repeat complete list]. Operations: [repeat complete list]. Challenge resolved. Proceeding to GATE A."

**Option B (GAP FOUND):** "[T] INVENTORY INCOMPLETE. Gap identified: [state the missing state or operation and the reason it belongs in the lifecycle]. Returning to [D] for registry update. VOCABULARY CLOSED must be re-declared before GATE A proceeds."

---

### GATE A [T]

Do not begin TRANSITION TABLE until all items are confirmed. Unconfirmed = TRANSITION TABLE blocked per C6.

- [ ] **[C-01]** STATE REGISTRY complete — domain vocabulary, no generics, at least one Terminal = Yes
- [ ] **[C-02]** OPERATION REGISTRY complete — every lifecycle operation named; all source/target IDs reference STATE REGISTRY
- [ ] **[C-03]** INVARIANT REGISTRY complete — at least two boolean assertions with named authority sources
- [ ] **[C-14]** BINDING RULE confirmed — [T] will not introduce any undeclared name in TRANSITION TABLE, INVALID TRANSITIONS, or RACE CONDITIONS
- [ ] **[C-15]** VOCABULARY CLOSED declared — complete name lists and forward-blocking prohibition in effect
- [ ] **[C7]** INVENTORY CHALLENGE resolved — Option A or Option B written above by [T]

**GATE A BLOCKED per C6. Do not begin TRANSITION TABLE until all items confirmed.**

---

### TRANSITION TABLE [T]

Scenario setup: [entity instance, starting state, actor, date/time context]

C1, C2, C3, C5 apply to every row.

| # | From State (SR ID) | Operation (OR ID) | Preconditions | To State (SR ID) | Postconditions | INV-01 | INV-02 | Side Effects |
|---|--------------------|-------------------|---------------|-----------------|----------------|--------|--------|--------------|

Column rules:
- **From State / To State:** STATE REGISTRY IDs only (C1). Undeclared name = C1 violation.
- **Operation:** OPERATION REGISTRY IDs only (C2). Undeclared name = C2 violation.
- **Preconditions:** Minimum two testable assertions per row (e.g., `status == Open`, `owner_id != null`).
- **Postconditions:** Minimum one assertion per row distinct from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED — [reason]`; never blank (C5). Add a column per declared INV.
- **Side Effects:** Triggered rules, record changes, notifications, audit events, async jobs.

---

### GATE B [T]

Do not begin INVALID TRANSITIONS until all items are confirmed. Unconfirmed = INVALID TRANSITIONS blocked per C8.

- [ ] **[C-08]** TRANSITION TABLE is columnar and complete; no operation exists only in prose
- [ ] **[C-05]** At least two invariants declared; at least one VIOLATED row present in TRANSITION TABLE
- [ ] **[C-06]** Every TRANSITION TABLE row has at least one postcondition assertion distinct from the To State name
- [ ] TRANSITION TABLE covers at least one path from the initial state to a terminal state

**GATE B BLOCKED per C8. Do not begin INVALID TRANSITIONS until all items confirmed.**

---

### INVALID TRANSITIONS [T]

| # | Attempted Operation (OR ID) | From State (SR ID) | Blocking Condition | INV Reference | Risk if Bypassed |
|---|----------------------------|-------------------|--------------------|--------------|-----------------|

Minimum three rows. Include at least one row where From State is a terminal state. All names must be from STATE REGISTRY and OPERATION REGISTRY — undeclared names are C1/C2 violations.

---

### GATE C [T]

Do not begin RACE CONDITIONS until all items are confirmed. Unconfirmed = RACE CONDITIONS blocked per C9.

- [ ] **[C-04]** At least three (operation, state) invalid pairs named with blocking conditions; enumeration is systematic across the operation set
- [ ] **[C-09]** At least one INVALID TRANSITIONS row has From State equal to a terminal state

**GATE C BLOCKED per C9. Do not begin RACE CONDITIONS until all items confirmed.**

---

### RACE CONDITIONS [T]

| Operation A (OR ID) | Operation B (OR ID) | Unsafe Interleaving | Outcome |
|--------------------|---------------------|---------------------|---------|

If no concurrent access: "No concurrent access — [reason stating why sequential access is guaranteed for {{topic}}]."

---

### GATE D [T]

Do not write BOUNDARY COVERAGE or FINDINGS until all items are confirmed. Unconfirmed = blocked.

- [ ] **[C-07]** RACE CONDITIONS section addressed — at least one scenario or explicit clearance with reason
- [ ] All names in TRANSITION TABLE and INVALID TRANSITIONS verified against STATE REGISTRY and OPERATION REGISTRY (C1, C2)
- [ ] No INV column blank in TRANSITION TABLE (C5 confirmed)
- [ ] At least one TRANSITION TABLE path reaches a terminal state

**GATE D BLOCKED. Do not write BOUNDARY COVERAGE or FINDINGS until all items confirmed.**

---

### BOUNDARY COVERAGE [T]

- **Initial state:** [STATE REGISTRY name — Terminal = No]
- **Terminal states:** [list all STATE REGISTRY entries where Terminal = Yes]
- **Terminal state coverage:** [cite INVALID TRANSITIONS row confirming terminal state attempt is blocked]

---

### FINDINGS

Priority order. Reference table and row.

- **P[N]:** [title] — [description, table/row reference]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: CONSTRAINT MATRIX, ROLES, BINDING RULE, STATE REGISTRY, OPERATION REGISTRY, INVARIANT REGISTRY, VOCABULARY CLOSED, INVENTORY CHALLENGE, GATE A, TRANSITION TABLE, GATE B, INVALID TRANSITIONS, GATE C, RACE CONDITIONS, GATE D, BOUNDARY COVERAGE, FINDINGS.

---

## V-05 — Full Ceiling Synthesis: All 14 Aspirational Criteria

**Axis:** Full synthesis (combined — all prior round best features)
**Hypothesis:** Explicit synthesis of all 14 criteria. Build on V-04 (CONSTRAINT MATRIX + Concern column, INVENTORY CHALLENGE with C7 binding, 4 per-section gates) and add: standalone BINDING RULE section before registries, VOCABULARY CLOSED with inline forward-blocking prohibition (not a cross-reference), BOUNDARY ANALYSIS section (initial state + terminal states, before GATE A), hard-stop phrasing at all gates, prose prohibition in CONSTRAINT MATRIX (C3), mandatory columnar TRANSITION TABLE (C8), every criterion has a named structural anchor. Reference synthesis for future rubric development. Predicted: 14/14 = 100.00.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. The CONSTRAINT MATRIX is the sole governing authority for this execution. Read every row before producing any output. Constraints are numbered, role-assigned, and categorized by concern — violations are identified by constraint ID throughout the document.

---

### CONSTRAINT MATRIX

| ID | Prohibition | Assigned Role | Concern |
|----|-------------|---------------|---------|
| C1 | YOU MAY NOT introduce any state name in any section that is not declared in the STATE REGISTRY | [T] | vocabulary |
| C2 | YOU MAY NOT introduce any operation name in any section that is not declared in the OPERATION REGISTRY | [T] | vocabulary |
| C3 | YOU MAY NOT use prose paragraphs or bullet lists as the primary output format for trace data; every operation must appear as a named table row — a row documented only in prose is a missing row | [T] | format |
| C4 | YOU MAY NOT retroactively add states or operations after VOCABULARY CLOSED is declared; if a name is absent, return to the registry, add it, re-declare VOCABULARY CLOSED, then continue | [D] | ordering |
| C5 | YOU MAY NOT leave any invariant status cell blank in the TRANSITION TABLE; every row records HOLDS or VIOLATED — [reason] for every declared invariant | [T] | integrity |
| C6 | YOU MAY NOT begin the TRANSITION TABLE until GATE A is fully confirmed | [T] | ordering |
| C7 | YOU MAY NOT proceed past INVENTORY CHALLENGE without a written Option A or Option B response; any other response format is a C7 violation | [T] | completeness |
| C8 | YOU MAY NOT begin INVALID TRANSITIONS until GATE B is fully confirmed | [T] | ordering |
| C9 | YOU MAY NOT begin RACE CONDITIONS until GATE C is fully confirmed | [T] | ordering |
| C10 | YOU MAY NOT write FINDINGS until GATE D is fully confirmed | [T] | ordering |

---

### ROLES

**[D] Domain Expert**
Auto-selected from: Sales expert (Lead / Qualified Lead / Opportunity / Proposal / Closed Won / Closed Lost), Customer Service expert (New / Open / Pending / Resolved / Closed), Finance expert (Draft / Submitted / Approved / Posted / Paid / Voided).
Section ownership: STATE REGISTRY, OPERATION REGISTRY, INVARIANT REGISTRY, VOCABULARY CLOSED, BOUNDARY ANALYSIS.
Binding constraint from CONSTRAINT MATRIX: **C4** — [D] may not add, rename, or remove any registry entry after VOCABULARY CLOSED is declared. Any retroactive addition is a C4 violation.

**[T] Trace Developer**
Section ownership: INVENTORY CHALLENGE written response, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, BOUNDARY COVERAGE, FINDINGS.
Binding constraints from CONSTRAINT MATRIX: **C1, C2, C3, C5, C6, C7, C8, C9, C10** — vocabulary scope, format prohibition, invariant completeness, and all ordering constraints.

---

### BINDING RULE

STATE REGISTRY is the authoritative and exclusive state vocabulary for this trace. OPERATION REGISTRY is the authoritative and exclusive operation vocabulary. No state name may appear in any table — TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, or any other section — that is not declared in STATE REGISTRY. No operation name may appear in any table that is not declared in OPERATION REGISTRY. This rule is in force from this section forward. Every gate verifies compliance before the next section may open.

---

### STATE REGISTRY [D]

| State ID | State Name | Defining Field Values | Entry Conditions | Terminal? |
|---------|-----------|----------------------|-----------------|-----------|

Domain vocabulary only. No generic labels ("State A", "initial", "final", "step 1"). At least one Terminal = Yes row required. Every state name must be drawn from {{topic}}'s actual domain lifecycle.

---

### OPERATION REGISTRY [D]

| Op ID | Operation Name | Legal Source State IDs | Target State ID | Triggering Actor |
|-------|---------------|----------------------|----------------|-----------------|

All State IDs must reference STATE REGISTRY IDs. Operations are distinct from state names: "Submit" is an operation; "Submitted" is a state.

---

### INVARIANT REGISTRY [D]

| INV ID | Invariant Name | Checkable Assertion | Authority Source |
|--------|----------------|--------------------|--------------------|

Minimum two invariants stated as boolean assertions. Authority source must be named: business rule number, SLA clause, regulation, or policy document.

---

### VOCABULARY CLOSED [D]

> VOCABULARY CLOSED per C4. States in scope: [list every STATE REGISTRY State Name]. Operations in scope: [list every OPERATION REGISTRY Operation Name]. No new state or operation name may be introduced from this point forward. Any name not listed above is prohibited in all sections that follow. This prohibition is not waivable and does not expire. If a name is discovered to be absent after this declaration: stop, return to the registry section, add the name, and re-declare VOCABULARY CLOSED with the updated list before continuing.

---

### BOUNDARY ANALYSIS [D]

Declare lifecycle boundaries. Terminal-state coverage is enforced at GATE C via INVALID TRANSITIONS.

- **Initial state:** [STATE REGISTRY State Name — Terminal = No; the state every new {{topic}} instance enters at creation]
- **Terminal states:** [list every STATE REGISTRY entry where Terminal = Yes — states from which no further transitions are possible]
- **Re-entry constraint:** INVALID TRANSITIONS must include at least one row where From State is a terminal state listed above. Confirmed at GATE C.

---

### INVENTORY CHALLENGE [T]

**C7 applies. [T] may not proceed to GATE A without writing Option A or Option B in full below. A blank response, a paraphrase, or any response that does not follow Option A or Option B format exactly is a C7 violation.**

INVENTORY COMPLETE — the STATE REGISTRY and OPERATION REGISTRY contain every state and operation in the complete lifecycle of {{topic}}.

**[T] must write one of the following responses here, in full, before GATE A:**

**Option A (CONFIRMED):** "[T] INVENTORY CONFIRMED. I have reviewed the STATE REGISTRY and OPERATION REGISTRY against the complete domain lifecycle of {{topic}}. No lifecycle state or operation is absent. States: [repeat complete list from STATE REGISTRY]. Operations: [repeat complete list from OPERATION REGISTRY]. Challenge resolved. Proceeding to GATE A."

**Option B (GAP FOUND):** "[T] INVENTORY INCOMPLETE. Gap identified: [name the missing state or operation and state specifically why it belongs in the {{topic}} lifecycle]. Returning to [D] for STATE REGISTRY / OPERATION REGISTRY update. VOCABULARY CLOSED must be re-declared with the updated lists before GATE A proceeds."

---

### GATE A [T]

Do not begin TRANSITION TABLE until every item is confirmed. Unconfirmed = TRANSITION TABLE blocked per C6.

- [ ] **[C-01]** STATE REGISTRY complete — domain vocabulary, no generic labels, at least one Terminal = Yes
- [ ] **[C-02]** OPERATION REGISTRY complete — every lifecycle operation named; all source/target State IDs reference STATE REGISTRY IDs
- [ ] **[C-03]** INVARIANT REGISTRY complete — at least two boolean assertions with named authority sources
- [ ] **[C-14]** BINDING RULE confirmed — [T] acknowledges no undeclared name will appear in TRANSITION TABLE, INVALID TRANSITIONS, or RACE CONDITIONS
- [ ] **[C-15]** VOCABULARY CLOSED declared — complete state and operation lists present; inline forward-blocking prohibition in effect
- [ ] BOUNDARY ANALYSIS complete — initial state declared; all terminal states listed; re-entry constraint stated
- [ ] **[C7]** INVENTORY CHALLENGE resolved — [T] has written Option A or Option B above in full

**GATE A BLOCKED per C6. Do not begin TRANSITION TABLE until every item above is confirmed.**

---

### TRANSITION TABLE [T]

Scenario setup: [entity instance, starting state, actor, date/time context]

Constraints C1, C2, C3, C5 apply to every row in this table.

| # | From State (SR ID) | Operation (OR ID) | Preconditions | To State (SR ID) | Postconditions | INV-01 | INV-02 | Side Effects |
|---|--------------------|-------------------|---------------|-----------------|----------------|--------|--------|--------------|

Column rules (compliance requirements, not suggestions):
- **From State / To State:** STATE REGISTRY IDs only (C1). Undeclared name = C1 violation — stop and correct.
- **Operation:** OPERATION REGISTRY IDs only (C2). Undeclared name = C2 violation — stop and correct.
- **Preconditions:** Minimum two testable assertions per row (e.g., `ticket.status == "Open"`, `invoice.owner_id != null`).
- **Postconditions:** Minimum one assertion per row distinct from the To State name. A restatement of "object is now in state X" does not satisfy C-06.
- **INV columns:** One column per declared invariant. Write `HOLDS` or `VIOLATED — [reason]`. Blank = C5 violation.
- **Side Effects:** Triggered rules, record changes, notifications, audit events, downstream async jobs.

---

### GATE B [T]

Do not begin INVALID TRANSITIONS until every item is confirmed. Unconfirmed = INVALID TRANSITIONS blocked per C8.

- [ ] **[C-08]** TRANSITION TABLE is columnar and complete; every operation is in a table row; no operation exists only in prose
- [ ] **[C-05]** Every INV column in TRANSITION TABLE is filled — HOLDS or VIOLATED — [reason]; at least one VIOLATED row present
- [ ] **[C-06]** Every TRANSITION TABLE row has at least one postcondition assertion distinct from the To State name
- [ ] TRANSITION TABLE covers at least one path from the initial state (BOUNDARY ANALYSIS) to a terminal state

**GATE B BLOCKED per C8. Do not begin INVALID TRANSITIONS until every item above is confirmed.**

---

### INVALID TRANSITIONS [T]

| # | Attempted Operation (OR ID) | From State (SR ID) | Blocking Condition | INV Reference | Risk if Bypassed |
|---|----------------------------|-------------------|--------------------|--------------|-----------------|

Minimum three rows required. At least one row must have From State equal to a terminal state from BOUNDARY ANALYSIS. All names must be from STATE REGISTRY and OPERATION REGISTRY only — undeclared names are C1/C2 violations.

---

### GATE C [T]

Do not begin RACE CONDITIONS until every item is confirmed. Unconfirmed = RACE CONDITIONS blocked per C9.

- [ ] **[C-04]** At least three (operation, state) invalid pairs named with explicit blocking conditions; enumeration is systematic — not limited to a single operation or state type
- [ ] **[C-09]** At least one INVALID TRANSITIONS row has From State equal to a terminal state listed in BOUNDARY ANALYSIS

**GATE C BLOCKED per C9. Do not begin RACE CONDITIONS until every item above is confirmed.**

---

### RACE CONDITIONS [T]

| Operation A (OR ID) | Operation B (OR ID) | Unsafe Interleaving | Outcome |
|--------------------|---------------------|---------------------|---------|

If no concurrent access applies: "No concurrent access — [specific reason stating the mechanism that enforces sequential-only access for {{topic}} objects]." A blank section is non-compliant — the section must be substantively addressed.

---

### GATE D [T]

Do not write BOUNDARY COVERAGE or FINDINGS until every item is confirmed. Unconfirmed = blocked per C10.

- [ ] **[C-07]** RACE CONDITIONS section is substantively addressed — at least one scenario with outcome or explicit no-concurrency clearance with mechanism stated
- [ ] **[C-01, C-02]** All names in TRANSITION TABLE and INVALID TRANSITIONS verified against STATE REGISTRY and OPERATION REGISTRY — no undeclared names present
- [ ] **[C-05]** No INV column blank anywhere in TRANSITION TABLE — confirmed
- [ ] **[C-09]** Terminal state coverage confirmed: at least one TRANSITION TABLE row reaches a terminal state; at least one INVALID TRANSITIONS row covers a terminal state attempt

**GATE D BLOCKED per C10. Do not write BOUNDARY COVERAGE or FINDINGS until every item above is confirmed.**

---

### BOUNDARY COVERAGE [T]

- **Initial state:** [STATE REGISTRY name — Terminal = No; confirmed from BOUNDARY ANALYSIS]
- **Terminal states:** [list all STATE REGISTRY entries where Terminal = Yes — confirmed from BOUNDARY ANALYSIS]
- **Terminal attempt coverage:** [cite INVALID TRANSITIONS row by row number confirming at least one terminal-state entry exists]

---

### FINDINGS

Priority order (P1 = highest risk). Reference section and row for every finding.

- **P[N]:** [title] — [description, section and row reference]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: CONSTRAINT MATRIX, ROLES, BINDING RULE, STATE REGISTRY, OPERATION REGISTRY, INVARIANT REGISTRY, VOCABULARY CLOSED, BOUNDARY ANALYSIS, INVENTORY CHALLENGE, GATE A, TRANSITION TABLE, GATE B, INVALID TRANSITIONS, GATE C, RACE CONDITIONS, GATE D, BOUNDARY COVERAGE, FINDINGS.

---

## Scoring Predictions (rubric v7)

| Variant | C-19 | C-20 | C-21 | Aspirational | Composite |
|---------|------|------|------|-------------|-----------|
| V-01 | FAIL | PASS | FAIL | 11/14 = 7.86 | 97.86 |
| V-02 | PASS | PASS | PASS | 14/14 = 10.00 | 100.00 |
| V-03 | FAIL | PASS | PARTIAL | ~11/14 | 97.86 |
| V-04 | PASS | PASS | PASS | 14/14 = 10.00 | 100.00 |
| V-05 | PASS | PASS | PASS | 14/14 = 10.00 | 100.00 |

**R8 new ceiling:** V-02, V-04, V-05 all predicted at 100.00. First round where three variants are expected to achieve the ceiling simultaneously.

**What distinguishes each variant:**
- **V-01:** Cleanest structure, no CONSTRAINT MATRIX, no INVENTORY CHALLENGE — C-20 in isolation. Baseline gate-per-section proof.
- **V-02:** Minimal delta from V-02 R7 — only change is gate-split. Validates gap was purely architectural, not structural.
- **V-03:** Conversational register at challenge site — tests whether informal phrasing breaks C-21 enforcement binding.
- **V-04:** Role-at-header as distinguishing feature — [D]/[T] tagged at every section. Independent synthesis path.
- **V-05:** Maximum explicit synthesis — every criterion has a named structural anchor; reference variant for all future rubric development.
