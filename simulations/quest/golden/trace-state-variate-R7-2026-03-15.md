# trace-state Variate — Round 7
**Date:** 2026-03-15
**Rubric:** v6 (C-01..C-19; golden: all essential pass AND composite >= 80)
**New criteria:** C-18 (per-constraint role mapping) and C-19 (explicit concern taxonomy)
**Scoring formula:** essential 50 + recommended 40 + aspirational 10 (12 criteria, 0.83 pts each)

---

## Round 7 Situation

Round 6 results (rubric v6):

| Variant | C-09 | C-10 | C-11 | C-14 | C-15 | C-18 | C-19 | Aspirational | Composite |
|---------|------|------|------|------|------|------|------|-------------|-----------|
| V-01 R6 | FAIL | PARTIAL | FAIL | PARTIAL | PARTIAL | PASS | FAIL | 6.24 / 10 | 96.24 |
| V-02 R6 | unclear | unclear | FAIL | exp PASS | exp PASS | PASS | PASS | TBD | TBD |

**Gap analysis:**

- **C-09 (FAIL):** GATE B in V-01 R6 checks TABLE 4 terminal coverage before TABLE 4 is filled — structurally impossible. Fix: gate checking C-09 must come after TABLE 4.
- **C-11 (FAIL both):** No pre-trace adversarial inventory challenge in either R6 variant. Fix: dedicated INVENTORY CHALLENGE section between VOCABULARY CLOSED and the trace gate.
- **C-10 (PARTIAL):** V-01 R6 has GATE A (mid-doc) and GATE B (final compliance). Final compliance gate does not count as mid-document blocking gate. Fix: four named gates where three block forward progress mid-document.
- **C-14 (PARTIAL):** Binding rule is buried in TABLE 1 header, not a standalone pre-trace declaration. Fix: standalone BINDING RULE section before all inventory tables.
- **C-15 (PARTIAL):** VOCABULARY CLOSED in V-01 R6 says "C4 applies" by reference, not an inline forward-blocking prohibition. Fix: inline prohibition text directly in the VOCABULARY CLOSED block.
- **C-19 (FAIL):** V-01 R6 has no concern taxonomy. V-02 R6 passes via Concern column in CONSTRAINT MATRIX.

**R7 objective:** Close C-09, C-11, and C-10 gaps. V-01 through V-03 are single-axis. V-04 and V-05 are combined, targeting the 12/12 aspirational ceiling.

---

## Round 7 Variation Map

| Var | Axis | C-09 | C-10 | C-11 | C-14 | C-15 | C-19 | Hypothesis |
|-----|------|------|------|------|------|------|------|------------|
| V-01 | Lifecycle emphasis — named BOUNDARY ANALYSIS section before TABLE 3; gate checking C-09 placed after TABLE 4 | **target** | PARTIAL | FAIL | PARTIAL→PASS | PARTIAL→PASS | FAIL | Moving the C-09 gate to after TABLE 4 makes it verifiable; BOUNDARY ANALYSIS as a named section primes the executor to mark terminal states explicitly before tracing; BINDING RULE and VOCABULARY CLOSED upgraded to standalone prohibition language |
| V-02 | Inertia framing — INVENTORY CHALLENGE phase after VOCABULARY CLOSED asserts "inventory complete" requiring explicit Option A/B written confirmation | PARTIAL | PARTIAL | **target** | PASS | PASS | PASS | V-02 R6 CONSTRAINT MATRIX base (C-18/C-19 structural); INVENTORY CHALLENGE is a named blocking section — C7 in the matrix makes skipping a named violation; challenge must produce written confirmation, not a checkbox |
| V-03 | Gate architecture — four named gates at four distinct structural positions (A: after TABLE 1; B: after inventories; C: after TABLE 3; D: final) | FAIL→PASS | **target** | FAIL | PARTIAL→PASS | PARTIAL→PASS | FAIL | Three mid-document gates block forward progress; GATE A blocks TABLE 2 until TABLE 1 confirmed; GATE B blocks TABLE 3 until inventories + vocabulary lock confirmed; GATE C blocks TABLE 4 until trace completeness confirmed; GATE D is final compliance with C-09 check after TABLE 4 is filled |
| V-04 | Combined: V-02 R6 CONSTRAINT MATRIX base + C-09 structural + C-11 structural | **target** | PARTIAL→PASS | **target** | PASS | PASS | PASS | CONSTRAINT MATRIX carries C-16/C-17/C-18/C-19; INVENTORY CHALLENGE closes C-11; BOUNDARY ANALYSIS + post-TABLE-4 gate closes C-09; only C-10 remains partial (two blocking gates + one final) |
| V-05 | Ceiling attempt — all 12 aspirational criteria via full synthesis | **target** | **target** | **target** | **target** | **target** | **target** | Full synthesis: CONSTRAINT MATRIX with Concern column (C-16/C-17/C-18/C-19) + standalone BINDING RULE (C-14) + VOCABULARY CLOSED with inline prohibition (C-15) + 4 gates (C-10: A after TABLE 1, B after inventories, C after TABLE 3, D final) + INVENTORY CHALLENGE (C-11) + BOUNDARY ANALYSIS with GATE D post-TABLE-4 check (C-09) + hard-stop phrasing at every gate (C-12) + prose prohibition in CONSTRAINT MATRIX (C-13) + mandatory columnar TABLE 3 (C-08) |

---

## V-01 — Lifecycle Emphasis: Named Boundary Analysis Section + Post-TABLE-4 Gate

**Axis:** Lifecycle emphasis (single axis)
**Hypothesis:** C-09 fails in V-01 R6 because GATE B checks "at least one TABLE 4 row covers a terminal state attempt" while TABLE 4 has not yet been filled — a gate cannot verify content that does not exist. V-01 R7 restructures the document so the C-09 gate comes after TABLE 4. A named BOUNDARY ANALYSIS section appears before TABLE 3 and explicitly declares the initial state and all terminal states by TABLE 1 ID. TABLE 4 then contains the terminal-state invalid-transition entry. GATE C (after TABLE 4) confirms coverage by criterion ID. Secondary fixes: BINDING RULE becomes a standalone section before TABLE 1 (not buried in a table header), and VOCABULARY CLOSED adds inline forward-blocking prohibition text rather than a cross-reference to C4.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. All trace output is delivered in named, columnar tables. Read the CONSTRAINTS section before producing any output.

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

TABLE 1 is the authoritative state vocabulary for this trace. TABLE 2 is the authoritative operation vocabulary. No state name may appear in TABLE 3, TABLE 4, or TABLE 5 that is not declared in TABLE 1. No operation name may appear in TABLE 3, TABLE 4, or TABLE 5 that is not declared in TABLE 2. This rule applies from this section forward and is verified at GATE A.

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

> VOCABULARY CLOSED. States: [list all TABLE 1 State Names]. Operations: [list all TABLE 2 Operation Names]. No new state or operation name may be introduced from this point forward. Any name not listed above is prohibited in all sections that follow. This prohibition applies even if the name is logically implied by the domain.

---

### GATE A

Do not begin TABLE 3 until all items are confirmed. Unconfirmed = TABLE 3 is blocked.

- [ ] **[C-01]** TABLE 1 complete — domain vocabulary, no generics, at least one Terminal = Yes
- [ ] **[C-02]** TABLE 2 complete — every lifecycle operation named; all source/target IDs reference TABLE 1
- [ ] **[C-03]** TABLE INV complete — at least two invariants with checkable assertions and authority sources
- [ ] **[C-14]** BINDING RULE confirmed — [T] will not introduce any name in TABLE 3, 4, or 5 not declared in TABLE 1 or TABLE 2
- [ ] **[C-15]** VOCABULARY CLOSED declared — complete name list and explicit forward-blocking prohibition in effect

**GATE A BLOCKED. Do not begin TABLE 3 until all items are confirmed.**

---

### BOUNDARY ANALYSIS [D]

Declare lifecycle boundaries before the transition trace begins. Terminal state coverage in TABLE 4 is verified at GATE C after TABLE 4 is filled.

- **Initial state:** [TABLE 1 State Name — Terminal = No; every new instance of {{topic}} enters here]
- **Terminal states:** [list all TABLE 1 entries where Terminal = Yes]
- **Re-entry requirement:** TABLE 4 must include at least one row where From State is a terminal state. This requirement is confirmed at GATE C.

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

### TABLE 4 — INVALID TRANSITIONS [T]

| # | Attempted Operation (T2 ID) | From State (T1 ID) | Blocking Condition | INV Reference | Risk if Bypassed |
|---|----------------------------|-------------------|--------------------|--------------|-----------------|

Minimum three rows. Include at least one row where From State = a terminal state (from BOUNDARY ANALYSIS). All names from TABLE 1 and TABLE 2.

---

### TABLE 5 — RACE CONDITIONS [T]

| Operation A (T2 ID) | Operation B (T2 ID) | Unsafe Interleaving | Outcome |
|--------------------|---------------------|---------------------|---------|

If no concurrent access: "No concurrent access — [reason]."

---

### GATE C

Do not write FINDINGS until all items are confirmed. Unconfirmed = blocked.

- [ ] **[C-04]** At least three (operation, state) invalid pairs named with blocking conditions; enumeration is systematic across the operation set
- [ ] **[C-05]** At least two invariants declared; at least one VIOLATED row in TABLE 3
- [ ] **[C-06]** Every TABLE 3 row has at least one postcondition distinct from the To State name
- [ ] **[C-07]** TABLE 5 addressed — at least one race scenario or explicit clearance with reason
- [ ] **[C-08]** TABLE 3 is columnar and complete; no operation exists only in prose
- [ ] **[C-09]** BOUNDARY ANALYSIS complete; at least one TABLE 4 row has From State = terminal state from BOUNDARY ANALYSIS list

**GATE C BLOCKED. Do not write FINDINGS until all items are confirmed.**

---

### FINDINGS

Priority order. Reference table and row.

- **P[N]:** [title] — [description, table row reference]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: CONSTRAINTS, ROLES, BINDING RULE, TABLE 1, TABLE 2, TABLE INV, VOCABULARY CLOSED, GATE A, BOUNDARY ANALYSIS, TABLE 3, TABLE 4, TABLE 5, GATE C, FINDINGS.

---

## V-02 — Inertia Framing: Adversarial Inventory Challenge Before Tracing

**Axis:** Inertia framing (single axis)
**Hypothesis:** C-11 has failed in every prior variation because no variation includes a pre-trace adversarial step. V-02 R7 builds on the V-02 R6 CONSTRAINT MATRIX base (structural C-18/C-19 via Assigned Role and Concern columns) and adds a dedicated INVENTORY CHALLENGE section between VOCABULARY CLOSED and the DECLARATION GATE. The challenge asserts "INVENTORY COMPLETE" and requires [T] to produce a written Option A confirmation (confirmed) or Option B (gap found — return to [D]). Constraint C7 in the CONSTRAINT MATRIX makes proceeding without confirmation a named violation — not a skippable step. The challenge is adversarial because it forces the executor to actively verify, not passively proceed. The key design risk: the challenge must be a real blocking gate, not a template placeholder that gets filled with "confirmed" mechanically. The Option B path (return to [D]) makes the challenge non-trivial by providing a real alternative.

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
| C6 | YOU MAY NOT begin the TRANSITION TABLE until the DECLARATION GATE passes | [T] | ordering |
| C7 | YOU MAY NOT proceed past INVENTORY CHALLENGE without a written Option A or Option B response | [T] | completeness |

---

### ROLES

**[D] Domain Expert**
Auto-selected: Sales expert (Lead / Qualified Lead / Opportunity / Proposal / Closed Won / Closed Lost), Customer Service expert (New / Open / Pending / Resolved / Closed), or Finance expert (Draft / Submitted / Approved / Posted / Paid / Voided).
Owns: STATE REGISTRY, OPERATION REGISTRY, INVARIANT REGISTRY, VOCABULARY CLOSED.
Binding constraint from CONSTRAINT MATRIX: **C4** (may not retroactively add vocabulary after VOCABULARY CLOSED).

**[T] Trace Developer**
Owns: INVENTORY CHALLENGE written response, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, BOUNDARY COVERAGE, FINDINGS.
Binding constraints from CONSTRAINT MATRIX: **C1, C2, C3, C5, C6, C7**.

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

> VOCABULARY CLOSED per C4. States: [list all STATE REGISTRY State Names]. Operations: [list all OPERATION REGISTRY Operation Names]. No new state or operation name may be introduced. Any name not listed above is prohibited in all sections that follow.

---

### INVENTORY CHALLENGE

**C7 applies. [T] may not proceed to DECLARATION GATE without a written response below.**

INVENTORY COMPLETE — the STATE REGISTRY and OPERATION REGISTRY contain every state and operation in the lifecycle of {{topic}}.

**[T] response — choose one:**

**Option A (CONFIRMED):** "[T] INVENTORY CONFIRMED. I have reviewed the STATE REGISTRY and OPERATION REGISTRY against the domain lifecycle of {{topic}}. No lifecycle state or operation is absent. States: [repeat complete list]. Operations: [repeat complete list]. Challenge resolved. Proceeding to DECLARATION GATE."

**Option B (GAP FOUND):** "[T] INVENTORY INCOMPLETE. Gap identified: [state the missing state or operation and why it belongs in the lifecycle]. Returning to [D] for STATE REGISTRY / OPERATION REGISTRY update. VOCABULARY CLOSED must be re-declared before DECLARATION GATE proceeds."

**A blank response, a paraphrase, or any response that does not follow Option A or Option B format is a C7 violation. [T] does not proceed until one option is written in full.**

---

### DECLARATION GATE

C6 applies — do not begin TRANSITION TABLE until all items are confirmed. Unconfirmed = TRANSITION TABLE is blocked.

- [ ] STATE REGISTRY complete — domain vocabulary, at least one terminal state
- [ ] OPERATION REGISTRY complete — all operations have source/target IDs from STATE REGISTRY
- [ ] INVARIANT REGISTRY complete — at least two assertions with authority sources
- [ ] VOCABULARY CLOSED declared with complete name list
- [ ] **[C7]** INVENTORY CHALLENGE resolved — Option A written above
- [ ] **[C-14]** [T] confirms: no name will appear in TRANSITION TABLE, INVALID TRANSITIONS, or RACE CONDITIONS that is not in STATE REGISTRY or OPERATION REGISTRY
- [ ] **[C-15]** VOCABULARY CLOSED has been declared and forward-blocking prohibition is in effect

**BLOCKED per C6. Do not begin TRANSITION TABLE until all items confirmed.**

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

### INVALID TRANSITIONS [T]

| # | Attempted Operation | From State | Blocking Condition | INV Reference | Risk if Bypassed |
|---|--------------------|------------|-------------------|--------------|-----------------|

Minimum three rows. All names from STATE REGISTRY and OPERATION REGISTRY.

---

### RACE CONDITIONS [T]

| Operation A | Operation B | Unsafe Interleaving | Outcome |
|------------|------------|---------------------|---------|

If no concurrent access: "No concurrent access — [reason]."

---

### TRACE COMPLETENESS GATE

Do not write FINDINGS until all items confirmed.

- [ ] **[C-01]** Every row has From State and To State from STATE REGISTRY
- [ ] **[C-02]** Every row has at least two preconditions as testable assertions
- [ ] **[C-03]** Every invariant checked per row — no blanks
- [ ] **[C-04]** At least three (operation, state) invalid pairs with blocking conditions
- [ ] **[C-06]** Every row has at least one postcondition distinct from the To State name
- [ ] **[C-07]** RACE CONDITIONS addressed
- [ ] **[C-08]** TRANSITION TABLE is columnar; no operation exists only in prose
- [ ] **[C-09]** At least one row reaches a terminal state; at least one INVALID TRANSITIONS row covers a terminal state attempt

**BLOCKED. Do not write FINDINGS until all items confirmed.**

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

Sections: CONSTRAINT MATRIX, ROLES, STATE REGISTRY, OPERATION REGISTRY, INVARIANT REGISTRY, VOCABULARY CLOSED, INVENTORY CHALLENGE, DECLARATION GATE, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, TRACE COMPLETENESS GATE, BOUNDARY COVERAGE, FINDINGS.

---

## V-03 — Gate Architecture: Four Named Gates at Distinct Structural Positions

**Axis:** Gate architecture (single axis)
**Hypothesis:** C-10 is PARTIAL in V-01 R6 because GATE B is a final compliance section positioned after all tables — it verifies completion but does not block forward progress mid-document. The criterion requires gates "positioned mid-document where they block forward progress." V-03 introduces four named gates: GATE A blocks TABLE 2 until TABLE 1 is confirmed; GATE B blocks TABLE 3 until all inventories and VOCABULARY CLOSED are confirmed; GATE C blocks TABLE 4 until TRANSITION TABLE completeness is confirmed; GATE D is the final compliance gate before FINDINGS (with the C-09 check now after TABLE 4). Three of four gates block mid-document progress. Each references criterion IDs. Hard-stop phrasing appears at every gate. The variation otherwise preserves the V-01 R6 baseline for all coverage criteria.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. All trace output is delivered in named, columnar tables. Four named gates enforce phase boundaries — no phase may begin until its gate clears. Read the CONSTRAINTS section first.

---

### CONSTRAINTS

**C1.** YOU MAY NOT introduce any state name in any table that is not declared in TABLE 1. A state not in TABLE 1 is a trace error.

**C2.** YOU MAY NOT introduce any operation name in any table that is not declared in TABLE 2. An operation not in TABLE 2 is a trace error.

**C3.** YOU MAY NOT use prose paragraphs or bullet lists as the primary output format. Every operation traces as a table row.

**C4.** YOU MAY NOT retroactively add states or operations after VOCABULARY CLOSED is declared.

**C5.** YOU MAY NOT leave any invariant status column blank in TABLE 3.

---

### ROLES

**[D] Domain Expert**
Auto-selected: Sales expert, Customer Service expert, or Finance expert (domain terminology only).
Owns: TABLE 1, TABLE 2, TABLE INV, VOCABULARY CLOSED.
Binding constraint: C4.

**[T] Trace Developer**
Owns: TABLE 3, TABLE 4, TABLE 5, BOUNDARY COVERAGE, FINDINGS.
Binding constraints: C1, C2, C3, C5.

---

### TABLE 1 — STATE REGISTRY [D]

| State ID | State Name | Defining Field Values | Entry Conditions | Terminal? |
|---------|-----------|----------------------|-----------------|-----------|

Domain vocabulary only. At least one Terminal = Yes row required.

---

### GATE A

Do not begin TABLE 2 until all items are confirmed. Unconfirmed = TABLE 2 is blocked.

- [ ] **[C-01]** TABLE 1 complete — domain vocabulary, no generic labels, at least one Terminal = Yes
- [ ] Referential binding acknowledged: [T] will not introduce any state name in TABLE 2, 3, 4, or 5 not declared in TABLE 1

**GATE A BLOCKED. Do not begin TABLE 2 until all items are confirmed.**

---

### TABLE 2 — OPERATION REGISTRY [D]

| Op ID | Operation Name | Legal Source State IDs | Target State ID | Triggering Actor |
|-------|---------------|----------------------|----------------|-----------------|

All State IDs must reference TABLE 1 IDs.

---

### TABLE INV — INVARIANT REGISTRY [D]

| INV ID | Name | Checkable Assertion | Authority Source |
|--------|------|--------------------|--------------------|

Minimum two invariants. Authority source: business rule, SLA clause, regulation, or policy.

---

### VOCABULARY CLOSED [D]

> VOCABULARY CLOSED. States: [list all TABLE 1 State Names]. Operations: [list all TABLE 2 Operation Names]. No new state or operation name may be introduced from this point forward. Any name not listed above is prohibited in all sections that follow. This prohibition is not waivable.

---

### GATE B

Do not begin TABLE 3 until all items are confirmed. Unconfirmed = TABLE 3 is blocked.

- [ ] **[C-02]** TABLE 2 complete — all lifecycle operations; source/target IDs reference TABLE 1
- [ ] **[C-03]** TABLE INV complete — at least two invariants with assertions and authority sources
- [ ] **[C-14]** Referential binding confirmed — [T] will not introduce any name in TABLE 3, 4, or 5 not declared in TABLE 1 or TABLE 2
- [ ] **[C-15]** VOCABULARY CLOSED declared — complete name list and forward-blocking prohibition in effect

**GATE B BLOCKED. Do not begin TABLE 3 until all items are confirmed.**

---

### TABLE 3 — TRANSITION TRACE [T]

Scenario setup: [entity instance, starting state, actor, date/time context]

C1, C2, C3, C5 apply.

| # | From State (T1 ID) | Operation (T2 ID) | Preconditions | To State (T1 ID) | Postconditions | INV-01 | INV-02 | Side Effects |
|---|--------------------|-------------------|---------------|-----------------|----------------|--------|--------|--------------|

- **From State / To State:** TABLE 1 IDs only (C1).
- **Operation:** TABLE 2 IDs only (C2).
- **Preconditions:** Minimum two testable assertions per row.
- **Postconditions:** Minimum one assertion distinct from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED — [reason]`; never blank (C5).

---

### GATE C

Do not begin TABLE 4 until all items are confirmed. Unconfirmed = TABLE 4 is blocked.

- [ ] **[C-06]** Every TABLE 3 row has at least one postcondition distinct from the To State name
- [ ] **[C-08]** TABLE 3 is columnar and complete; no operation exists only in prose
- [ ] **[C-05]** At least two invariants declared; at least one VIOLATED row present in TABLE 3

**GATE C BLOCKED. Do not begin TABLE 4 until all items are confirmed.**

---

### TABLE 4 — INVALID TRANSITIONS [T]

| # | Attempted Operation (T2 ID) | From State (T1 ID) | Blocking Condition | INV Reference | Risk if Bypassed |
|---|----------------------------|-------------------|--------------------|--------------|-----------------|

Minimum three rows. Include at least one row where From State = a terminal state. All names from TABLE 1 and TABLE 2.

---

### TABLE 5 — RACE CONDITIONS [T]

| Operation A (T2 ID) | Operation B (T2 ID) | Unsafe Interleaving | Outcome |
|--------------------|---------------------|---------------------|---------|

If no concurrent access: "No concurrent access — [reason]."

---

### GATE D — FINAL COMPLIANCE

Do not write BOUNDARY COVERAGE or FINDINGS until all items are confirmed. Unconfirmed = blocked.

- [ ] **[C-04]** At least three (operation, state) invalid pairs named with blocking conditions
- [ ] **[C-07]** TABLE 5 addressed — at least one race scenario or explicit clearance
- [ ] **[C-09]** Initial state declared; terminal states listed; at least one TABLE 4 row covers an attempt on a terminal state [cite row]

**GATE D BLOCKED. Do not write BOUNDARY COVERAGE or FINDINGS until all items are confirmed.**

---

### BOUNDARY COVERAGE [T]

- **Initial state:** [TABLE 1 — Terminal = No]
- **Terminal states:** [list all TABLE 1 entries where Terminal = Yes]
- **Re-entry blocked:** [cite TABLE 4 row covering terminal state attempt]

---

### FINDINGS

Priority order. Reference table and row.

- **P[N]:** [title] — [description]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: CONSTRAINTS, ROLES, TABLE 1, GATE A, TABLE 2, TABLE INV, VOCABULARY CLOSED, GATE B, TABLE 3, GATE C, TABLE 4, TABLE 5, GATE D, BOUNDARY COVERAGE, FINDINGS.

---

## V-04 — Combined: CONSTRAINT MATRIX Base + C-09 Structural + C-11 Structural

**Axis:** Combined (output format + lifecycle emphasis + inertia framing)
**Hypothesis:** V-02 R6 established the CONSTRAINT MATRIX (ID | Prohibition | Assigned Role | Concern) as the structural foundation for C-16, C-17, C-18, and C-19 simultaneously. V-04 R7 adds the two largest structural gaps to that base without disrupting the matrix. INVENTORY CHALLENGE closes C-11 — it is a dedicated section after VOCABULARY CLOSED; C7 in the matrix makes skipping it a named violation. Named BOUNDARY ANALYSIS before TABLE 3 + a post-TABLE-4 TRACE COMPLETENESS GATE confirming C-09 by ID closes the terminal boundary gap. Expected result: all 12 aspirational criteria pass except possibly C-10 (two blocking gates mid-document, not four — DECLARATION GATE and TRACE COMPLETENESS GATE are present, which may be PARTIAL under the four-gate reading).

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. All constraints governing this trace are pre-registered in the CONSTRAINT MATRIX. Read the matrix completely before producing any output.

---

### CONSTRAINT MATRIX

| ID | Prohibition | Assigned Role | Concern |
|----|-------------|---------------|---------|
| C1 | YOU MAY NOT introduce any state name in any table that is not declared in the STATE REGISTRY | [T] | vocabulary |
| C2 | YOU MAY NOT introduce any operation name in any table that is not declared in the OPERATION REGISTRY | [T] | vocabulary |
| C3 | YOU MAY NOT use prose paragraphs or bullet lists as the primary output format; every operation traces as a table row | [T] | format |
| C4 | YOU MAY NOT retroactively add states or operations after VOCABULARY CLOSED is declared | [D] | ordering |
| C5 | YOU MAY NOT leave any invariant status column blank in the TRANSITION TABLE | [T] | integrity |
| C6 | YOU MAY NOT begin the TRANSITION TABLE until the DECLARATION GATE passes | [T] | ordering |
| C7 | YOU MAY NOT proceed past INVENTORY CHALLENGE without a written Option A or Option B response | [T] | completeness |

---

### ROLES

**[D] Domain Expert**
Auto-selected: Sales expert (Lead / Qualified Lead / Opportunity / Proposal / Closed Won / Closed Lost), Customer Service expert (New / Open / Pending / Resolved / Closed), or Finance expert (Draft / Submitted / Approved / Posted / Paid / Voided).
Owns: STATE REGISTRY, OPERATION REGISTRY, INVARIANT REGISTRY, VOCABULARY CLOSED, BOUNDARY ANALYSIS.
Binding constraint from CONSTRAINT MATRIX: **C4**.

**[T] Trace Developer**
Owns: INVENTORY CHALLENGE written response, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, FINDINGS.
Binding constraints from CONSTRAINT MATRIX: **C1, C2, C3, C5, C6, C7**.

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

> VOCABULARY CLOSED per C4. States: [list all STATE REGISTRY State Names]. Operations: [list all OPERATION REGISTRY Operation Names]. No new state or operation name may be introduced. Any name not listed above is prohibited in all sections that follow.

---

### INVENTORY CHALLENGE

**C7 applies — [T] may not proceed to BOUNDARY ANALYSIS or DECLARATION GATE until this challenge is resolved in writing.**

INVENTORY COMPLETE — the STATE REGISTRY and OPERATION REGISTRY contain every state and operation in the lifecycle of {{topic}}.

**[T] response — choose one:**

**Option A (CONFIRMED):** "[T] INVENTORY CONFIRMED. States: [repeat complete list]. Operations: [repeat complete list]. No lifecycle state or operation is absent. Challenge resolved. Proceeding to DECLARATION GATE."

**Option B (GAP FOUND):** "[T] INVENTORY INCOMPLETE. Gap: [name and reason]. Returning to [D] for STATE REGISTRY / OPERATION REGISTRY update. VOCABULARY CLOSED must be re-declared before DECLARATION GATE."

**A blank response or non-option response is a C7 violation.**

---

### BOUNDARY ANALYSIS [D]

- **Initial state:** [STATE REGISTRY name — Terminal = No; every new {{topic}} instance enters here]
- **Terminal states:** [list all STATE REGISTRY entries where Terminal = Yes]
- **Re-entry requirement:** INVALID TRANSITIONS must include at least one row where From State is a terminal state. Confirmed at TRACE COMPLETENESS GATE after INVALID TRANSITIONS is filled.

---

### DECLARATION GATE

C6 applies — do not begin TRANSITION TABLE until all items confirmed.

- [ ] STATE REGISTRY complete — domain vocabulary, at least one terminal state
- [ ] OPERATION REGISTRY complete — all operations have source/target IDs from STATE REGISTRY
- [ ] INVARIANT REGISTRY complete — at least two assertions with authority sources
- [ ] VOCABULARY CLOSED declared with complete name list
- [ ] **[C7]** INVENTORY CHALLENGE resolved — Option A written above
- [ ] **[C-14]** [T] confirms: no name will appear in TRANSITION TABLE, INVALID TRANSITIONS, or RACE CONDITIONS that is not in STATE REGISTRY or OPERATION REGISTRY
- [ ] **[C-15]** VOCABULARY CLOSED declared — forward-blocking prohibition in effect

**BLOCKED per C6. Do not begin TRANSITION TABLE until all items confirmed.**

---

### TRANSITION TABLE [T]

Scenario setup: [entity instance, starting state, actor, date/time context]

Constraints C1, C2, C3, C5 apply. See CONSTRAINT MATRIX.

| # | From State | Operation | Preconditions | To State | Postconditions | INV-01 | INV-02 | Side Effects |
|---|-----------|-----------|---------------|---------|----------------|--------|--------|--------------|

- **From State / To State:** STATE REGISTRY names only (C1).
- **Operation:** OPERATION REGISTRY names only (C2).
- **Preconditions:** Minimum two testable assertions per row.
- **Postconditions:** Minimum one assertion distinct from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED — [reason]`; never blank (C5).

---

### INVALID TRANSITIONS [T]

| # | Attempted Operation | From State | Blocking Condition | INV Reference | Risk if Bypassed |
|---|--------------------|------------|-------------------|--------------|-----------------|

Minimum three rows. Include at least one where From State = terminal state (from BOUNDARY ANALYSIS). All names from STATE REGISTRY and OPERATION REGISTRY.

---

### RACE CONDITIONS [T]

| Operation A | Operation B | Unsafe Interleaving | Outcome |
|------------|------------|---------------------|---------|

If no concurrent access: "No concurrent access — [reason]."

---

### TRACE COMPLETENESS GATE

Do not write FINDINGS until all items confirmed. Unconfirmed = blocked.

- [ ] **[C-01]** Every row has From State and To State from STATE REGISTRY
- [ ] **[C-02]** Every row has at least two preconditions as testable assertions
- [ ] **[C-03]** Every invariant checked per row — no blanks
- [ ] **[C-04]** At least three (operation, state) invalid pairs with blocking conditions
- [ ] **[C-06]** Every row has at least one postcondition distinct from the To State name
- [ ] **[C-07]** RACE CONDITIONS addressed
- [ ] **[C-08]** TRANSITION TABLE is columnar; no operation exists only in prose
- [ ] **[C-09]** BOUNDARY ANALYSIS declared; at least one INVALID TRANSITIONS row covers a terminal state attempt [cite row]

**BLOCKED. Do not write FINDINGS until all items confirmed.**

---

### FINDINGS

Priority order. Reference table and row.

- **P[N]:** [title] — [description]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: CONSTRAINT MATRIX, ROLES, STATE REGISTRY, OPERATION REGISTRY, INVARIANT REGISTRY, VOCABULARY CLOSED, INVENTORY CHALLENGE, BOUNDARY ANALYSIS, DECLARATION GATE, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, TRACE COMPLETENESS GATE, FINDINGS.

---

## V-05 — Ceiling Attempt: All 12 Aspirational Criteria via Full Synthesis

**Axis:** Combined — all axes
**Hypothesis:** Full synthesis targeting all 12 aspirational criteria simultaneously.

Criteria mapping:
- **C-08** (mandatory columnar table): C3 in CONSTRAINT MATRIX prohibits prose; TABLE 3 is columnar by structure.
- **C-09** (terminal-state boundary as named section): BOUNDARY ANALYSIS section before TABLE 3; GATE D (after TABLE 4) confirms TABLE 4 coverage by C-09 ID.
- **C-10** (four named gates): GATE A (after TABLE 1, before TABLE 2), GATE B (after inventories, before TABLE 3), GATE C (after TABLE 3, before TABLE 4), GATE D (final compliance after TABLE 4). Three mid-document blocking gates + one final gate.
- **C-11** (inertia adversarial challenge): INVENTORY CHALLENGE section with C7 blocking constraint.
- **C-12** (hard-stop phrasing): Every gate ends with "BLOCKED. Do not begin [next section] until..." — at least four instances.
- **C-13** (prose prohibition): C3 in CONSTRAINT MATRIX uses imperative "YOU MAY NOT" phrasing covering both paragraphs and bullet lists.
- **C-14** (referential binding rule): Standalone BINDING RULE section before TABLE 1; confirmed at GATE B by criterion ID.
- **C-15** (vocabulary lock): VOCABULARY CLOSED with inline "prohibited in all sections that follow" language; confirmed at GATE B by criterion ID.
- **C-16** (numbered constraint preamble): CONSTRAINT MATRIX is a numbered registry before all output-generating sections.
- **C-17** (role-differentiated constraint assignment): ROLES section assigns specific CONSTRAINT MATRIX IDs to [D] and [T] as explicit bindings.
- **C-18** (per-constraint role mapping): Assigned Role column maps every constraint to a named role at constraint granularity.
- **C-19** (explicit concern taxonomy): Concern column in CONSTRAINT MATRIX labels each constraint with a category name.

Synthesis risk: dilution — sections lose structural weight when too many coexist. Counter-measure: every section is load-bearing (explicitly cited at a gate or in the CONSTRAINT MATRIX), not decorative.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. Read the CONSTRAINT MATRIX first — it governs every section that follows. No output-generating section may begin until its gate clears.

---

### CONSTRAINT MATRIX

| ID | Prohibition | Assigned Role | Concern |
|----|-------------|---------------|---------|
| C1 | YOU MAY NOT introduce any state name in any table that is not declared in TABLE 1 | [T] | vocabulary |
| C2 | YOU MAY NOT introduce any operation name in any table that is not declared in TABLE 2 | [T] | vocabulary |
| C3 | YOU MAY NOT use prose paragraphs or bullet lists as the primary output format for trace data; every operation must appear as a table row | [T] | format |
| C4 | YOU MAY NOT retroactively add states or operations to TABLE 1 or TABLE 2 after VOCABULARY CLOSED is declared | [D] | ordering |
| C5 | YOU MAY NOT leave any invariant status column blank in TABLE 3 | [T] | integrity |
| C6 | YOU MAY NOT begin TABLE 3 until GATE B passes | [T] | ordering |
| C7 | YOU MAY NOT proceed past INVENTORY CHALLENGE without a written Option A or Option B response | [T] | completeness |
| C8 | YOU MAY NOT begin TABLE 4 until GATE C passes | [T] | ordering |

---

### ROLES

**[D] Domain Expert**
Auto-selected: Sales expert (Lead / Qualified Lead / Opportunity / Proposal / Closed Won / Closed Lost), Customer Service expert (New / Open / Pending / Resolved / Closed), or Finance expert (Draft / Submitted / Approved / Posted / Paid / Voided).
Owns: TABLE 1, TABLE 2, TABLE INV, VOCABULARY CLOSED, BOUNDARY ANALYSIS.
**Binding constraint from CONSTRAINT MATRIX — C4 applies to [D]:** After VOCABULARY CLOSED is declared, [D] may not add, rename, or remove any entry in TABLE 1 or TABLE 2.

**[T] Trace Developer**
Owns: INVENTORY CHALLENGE written response, TABLE 3, TABLE 4, TABLE 5, FINDINGS.
**Binding constraints from CONSTRAINT MATRIX — C1, C2, C3, C5, C6, C7, C8 apply to [T]:** vocabulary scope (both dimensions), output format prohibition, invariant completeness, phase ordering (TABLE 3 blocked by C6/GATE B; TABLE 4 blocked by C8/GATE C), inventory challenge confirmation.

---

### BINDING RULE

TABLE 1 is the authoritative state vocabulary for this trace. TABLE 2 is the authoritative operation vocabulary. No state name may appear in TABLE 3, TABLE 4, or TABLE 5 that is not declared in TABLE 1. No operation name may appear in TABLE 3, TABLE 4, or TABLE 5 that is not declared in TABLE 2. This rule is in force from this section forward. GATE B verifies compliance by criterion ID before TABLE 3 begins.

---

### TABLE 1 — STATE REGISTRY [D]

| State ID | State Name | Defining Field Values | Entry Conditions | Terminal? |
|---------|-----------|----------------------|-----------------|-----------|

Domain vocabulary only. No generic labels ("State A", "initial", "final"). At least one Terminal = Yes row required.

---

### GATE A

Do not begin TABLE 2 until all items are confirmed. Unconfirmed = TABLE 2 is blocked.

- [ ] **[C-01]** TABLE 1 complete — domain vocabulary, no generic labels, at least one Terminal = Yes
- [ ] BINDING RULE acknowledged — [T] will not introduce any state name in TABLE 2, 3, 4, or 5 not declared in TABLE 1

**GATE A BLOCKED. Do not begin TABLE 2 until all items are confirmed.**

---

### TABLE 2 — OPERATION REGISTRY [D]

| Op ID | Operation Name | Legal Source State IDs | Target State ID | Triggering Actor |
|-------|---------------|----------------------|----------------|-----------------|

All State IDs must reference TABLE 1 IDs.

---

### TABLE INV — INVARIANT REGISTRY [D]

| INV ID | Name | Checkable Assertion | Authority Source |
|--------|------|--------------------|--------------------|

Minimum two invariants. Authority source: business rule, SLA clause, regulation, or policy.

---

### VOCABULARY CLOSED [D]

> VOCABULARY CLOSED. States: [list all TABLE 1 State Names]. Operations: [list all TABLE 2 Operation Names]. No new state or operation name may be introduced from this point forward. Any name not listed above is prohibited in all sections that follow. This prohibition is not waivable by domain inference. C4 applies.

---

### INVENTORY CHALLENGE

**C7 applies. [T] may not proceed to GATE B until this challenge is resolved in writing.**

INVENTORY COMPLETE — TABLE 1 and TABLE 2 contain every state and operation in the lifecycle of {{topic}}.

**[T] response — choose one:**

**Option A (CONFIRMED):** "[T] INVENTORY CONFIRMED. I have verified TABLE 1 and TABLE 2 against the full lifecycle of {{topic}}. No lifecycle state or operation is absent. States: [repeat complete list]. Operations: [repeat complete list]. Challenge resolved. Proceeding to GATE B."

**Option B (GAP FOUND):** "[T] INVENTORY INCOMPLETE. Gap: [name and why it belongs in the lifecycle]. Returning to [D] for TABLE 1 / TABLE 2 update. VOCABULARY CLOSED must be re-declared before GATE B."

**A blank response or non-option response is a C7 violation. [T] does not proceed until one option is written.**

---

### BOUNDARY ANALYSIS [D]

- **Initial state:** [TABLE 1 State Name — Terminal = No; every new {{topic}} instance enters here]
- **Terminal states:** [list all TABLE 1 entries where Terminal = Yes]
- **Re-entry requirement:** TABLE 4 must include at least one row where From State is a terminal state from this list. Verified at GATE D.

---

### GATE B

Do not begin TABLE 3 until all items are confirmed. C6 applies — TABLE 3 is blocked until this gate passes.

- [ ] **[C-02]** TABLE 2 complete — all lifecycle operations; source/target IDs reference TABLE 1
- [ ] **[C-03]** TABLE INV complete — at least two invariants with assertions and authority sources
- [ ] **[C-14]** BINDING RULE confirmed — no name will appear in TABLE 3, 4, or 5 not declared in TABLE 1 or TABLE 2
- [ ] **[C-15]** VOCABULARY CLOSED declared — complete name list and forward-blocking prohibition in effect
- [ ] **[C7]** INVENTORY CHALLENGE resolved — Option A written above

**GATE B BLOCKED. Do not begin TABLE 3 until all items are confirmed.**

---

### TABLE 3 — TRANSITION TRACE [T]

Scenario setup: [entity instance, starting state, actor, date/time context]

C1, C2, C3, C5 apply. See CONSTRAINT MATRIX.

| # | From State (T1) | Operation (T2) | Preconditions | To State (T1) | Postconditions | INV-01 | INV-02 | Side Effects |
|---|----------------|----------------|---------------|--------------|----------------|--------|--------|--------------|

- **From State / To State:** TABLE 1 IDs only (C1).
- **Operation:** TABLE 2 IDs only (C2).
- **Preconditions:** Minimum two testable assertions per row.
- **Postconditions:** Minimum one assertion distinct from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED — [reason]`; never blank (C5).

---

### GATE C

Do not begin TABLE 4 until all items are confirmed. C8 applies — TABLE 4 is blocked until this gate passes.

- [ ] **[C-06]** Every TABLE 3 row has at least one postcondition distinct from the To State name
- [ ] **[C-08]** TABLE 3 is columnar and complete; no operation exists only in prose
- [ ] **[C-05]** At least two invariants declared; at least one VIOLATED row present in TABLE 3

**GATE C BLOCKED. Do not begin TABLE 4 until all items are confirmed.**

---

### TABLE 4 — INVALID TRANSITIONS [T]

| # | Attempted Operation (T2) | From State (T1) | Blocking Condition | INV Reference | Risk if Bypassed |
|---|--------------------------|----------------|--------------------|--------------|-----------------|

Minimum three rows. Include at least one row where From State = a terminal state from BOUNDARY ANALYSIS. All names from TABLE 1 and TABLE 2.

---

### TABLE 5 — RACE CONDITIONS [T]

| Operation A (T2) | Operation B (T2) | Unsafe Interleaving | Outcome |
|-----------------|-----------------|---------------------|---------|

If no concurrent access: "No concurrent access — [reason]."

---

### GATE D — FINAL COMPLIANCE

Do not write FINDINGS until all items are confirmed. Unconfirmed = blocked.

- [ ] **[C-04]** At least three (operation, state) invalid pairs named with explicit blocking conditions; enumeration is systematic
- [ ] **[C-07]** TABLE 5 addressed — at least one race scenario or explicit clearance
- [ ] **[C-09]** BOUNDARY ANALYSIS declared; initial state named; terminal states listed; at least one TABLE 4 row has From State = terminal state [cite row]

**GATE D BLOCKED. Do not write FINDINGS until all items are confirmed.**

---

### FINDINGS

Priority order. Reference table and row.

- **P[N]:** [title] — [description]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: CONSTRAINT MATRIX, ROLES, BINDING RULE, TABLE 1, GATE A, TABLE 2, TABLE INV, VOCABULARY CLOSED, INVENTORY CHALLENGE, BOUNDARY ANALYSIS, GATE B, TABLE 3, GATE C, TABLE 4, TABLE 5, GATE D, FINDINGS.
