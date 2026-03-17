# trace-state Variate — Round 9
**Date:** 2026-03-15
**Rubric:** v7 (C-01..C-21; golden: all essential pass AND composite >= 80)
**Situation:** R8 closed the three remaining aspirational gaps (C-19, C-20, C-21) via synthesis variants V-02/V-04/V-05, all predicting 14/14 = 100.00. The ceiling is reached under v7. R9 tests whether structural innovations orthogonal to the current criteria hold the ceiling while introducing patterns that may seed C-22+. Three single-axis variants probe new territory; two synthesis variants combine the best new patterns with the R8 ceiling baseline.

---

## Round 8 Results (Basis for R9)

| Variant | C-19 | C-20 | C-21 | Aspirational | Composite |
|---------|------|------|------|-------------|-----------|
| V-01 R8 | FAIL | PASS | FAIL | 11/14 = 97.86 | Golden |
| V-02 R8 | PASS | PASS | PASS | 14/14 = 100.00 | Golden ceiling |
| V-03 R8 | FAIL | PASS | PARTIAL | 11/14 = 97.86 | Golden |
| V-04 R8 | PASS | PASS | PASS | 14/14 = 100.00 | Golden ceiling |
| V-05 R8 | PASS | PASS | PASS | 14/14 = 100.00 | Golden ceiling |

Ceiling achieved. No new v7 criteria available to earn. R9 objective: stress-test ceiling stability under new structural axes and discover structural features worth promoting to C-22+.

---

## Round 9 Variation Map

| Var | Axis | Hypothesis | C-19 | C-20 | C-21 | Predicted |
|-----|------|------------|------|------|------|-----------|
| V-01 | Role sequence — explicit [D]→[T] HANDOFF DECLARATION | A named role-transfer event signed by [D] and acknowledged by [T] makes handoff structural, not implicit. Ceiling holds; HANDOFF DECLARATION may seed C-22 (explicit role-transfer declaration). | PASS | PASS | PASS | 14/14 = 100.00 |
| V-02 | Output format — numbered prose inventory declarations | STATE REGISTRY and OPERATION REGISTRY use numbered prose items (S-01, O-01) instead of tables. Trace tables remain columnar. Tests whether prose inventories degrade C-14/C-15 referential binding or survive because binding is declared, not structural. C-19 FAIL predicted (no Concern column in prose). | FAIL | PASS | PASS | 12/14 = 98.57 |
| V-03 | Phrasing register — declarative IS framing | All constraint text uses ontological IS framing ("An operation IS PROHIBITED from appearing in TABLE 3 unless it IS declared in the OPERATION REGISTRY") instead of imperative YOU MAY NOT. Tests whether declarative register weakens enforcement at C-21 (violation binding must still be imperative-enough to bind). | PASS | PASS | PASS | 14/14 = 100.00 |
| V-04 | Role sequence + lifecycle emphasis (combined) | [D] HANDOFF DECLARATION (V-01) combined with two named macro-phases: DECLARATION PHASE / TRACE PHASE. The HANDOFF DECLARATION is the inter-phase boundary. GATE A–D operate within TRACE PHASE as sub-section gates. Tests whether macro-phase framing strengthens or obscures sequential gate coverage (C-20). | PASS | PASS | PASS | 14/14 = 100.00 |
| V-05 | Full synthesis — R8 V-02 baseline + V-01 handoff + V-03 IS register in selected positions | Takes R8 V-02 (confirmed ceiling) and adds HANDOFF DECLARATION after VOCABULARY CLOSED and IS framing in the CONSTRAINT MATRIX Prohibition column. No other structural changes. Pure additive synthesis. Predicted ceiling + potential C-22 and C-23 seeds. | PASS | PASS | PASS | 14/14 = 100.00 |

---

## V-01 — Role Sequence: Explicit [D]→[T] Handoff Declaration

**Axis:** Role sequence (single axis)
**Hypothesis:** In R8 V-02, the handoff from [D] to [T] is implicit — GATE A checks inventory completion, but no named actor formally closes the declaration phase. A HANDOFF DECLARATION section, signed by [D] after VOCABULARY CLOSED, makes role-sequence enforcement explicit: [T] is blocked until [D] produces a signed artifact, not merely until a checklist passes. The INVENTORY CHALLENGE then becomes [T]'s countersignature. R8 V-02 structure otherwise preserved verbatim. Predicted: 14/14 = 100.00. HANDOFF DECLARATION may seed C-22.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. Two roles execute in sequence. [D] produces the declaration artifact and signs it. [T] acknowledges the declaration and executes the transition trace. [D] must sign HANDOFF DECLARATION before [T] is authorized to begin. Read CONSTRAINT MATRIX completely before producing any output.

---

### CONSTRAINT MATRIX

| ID | Prohibition | Assigned Role | Concern |
|----|-------------|---------------|---------|
| C1 | YOU MAY NOT introduce any state name in any trace table that is not declared in the STATE REGISTRY | [T] | vocabulary |
| C2 | YOU MAY NOT introduce any operation name in any trace table that is not declared in the OPERATION REGISTRY | [T] | vocabulary |
| C3 | YOU MAY NOT use prose paragraphs or bullet lists as the primary output format for trace data; every operation traces as a table row | [T] | format |
| C4 | YOU MAY NOT retroactively add states or operations after HANDOFF DECLARATION is signed | [D] | ordering |
| C5 | YOU MAY NOT leave any invariant status column blank in the TRANSITION TABLE | [T] | integrity |
| C6 | YOU MAY NOT begin TRANSITION TABLE until GATE A is confirmed | [T] | ordering |
| C7 | YOU MAY NOT proceed past INVENTORY CHALLENGE without a written Option A or Option B response; a blank response or non-option response is a C7 violation | [T] | completeness |
| C8 | YOU MAY NOT begin INVALID TRANSITIONS until GATE B is confirmed | [T] | ordering |
| C9 | YOU MAY NOT begin RACE CONDITIONS until GATE C is confirmed | [T] | ordering |

---

### ROLES

**[D] Domain Expert**
Auto-selected: Sales expert (Lead / Qualified Lead / Opportunity / Proposal / Closed Won / Closed Lost), Customer Service expert (New / Open / Pending / Resolved / Closed), or Finance expert (Draft / Submitted / Approved / Posted / Paid / Voided).
Owns: STATE REGISTRY, OPERATION REGISTRY, INVARIANT REGISTRY, VOCABULARY CLOSED, HANDOFF DECLARATION.
Binding constraint from CONSTRAINT MATRIX: **C4** (may not retroactively add vocabulary after HANDOFF DECLARATION is signed).

**[T] Trace Developer**
Owns: INVENTORY CHALLENGE written response, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, BOUNDARY COVERAGE, FINDINGS.
Binding constraints from CONSTRAINT MATRIX: **C1, C2, C3, C5, C6, C7, C8, C9**.
Authorization: [T] is blocked from all sections until HANDOFF DECLARATION is signed by [D].

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

| INV ID | Invariant | Checkable Assertion | Authority Source |
|--------|-----------|--------------------|--------------------|

Minimum two invariants as boolean assertions. Authority source: business rule, SLA clause, regulation, or policy.

---

### VOCABULARY CLOSED [D]

> VOCABULARY CLOSED per C4. States: [list all STATE REGISTRY State Names]. Operations: [list all OPERATION REGISTRY Operation Names]. No new state or operation name may be introduced from this point forward. Any name not listed above is prohibited in all sections that follow.

---

### HANDOFF DECLARATION [D]

> **[D] HANDOFF DECLARATION.** The STATE REGISTRY, OPERATION REGISTRY, and INVARIANT REGISTRY for {{topic}} are complete. VOCABULARY CLOSED is in effect. The following sections are hereby transferred to [T]: INVENTORY CHALLENGE response, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, BOUNDARY COVERAGE, FINDINGS. [T] is now authorized to proceed subject to constraints C1, C2, C3, C5, C6, C7, C8, C9. [D] may not alter any registry entry from this point forward (C4).
>
> **[D] Signed:** [domain role selected] — [N] states, [N] operations.

---

### INVENTORY CHALLENGE

**C7 applies. [T] may not proceed to GATE A without a written response below. A blank response or non-option response is a C7 violation.**

INVENTORY COMPLETE — the STATE REGISTRY and OPERATION REGISTRY contain every state and operation in the lifecycle of {{topic}}.

**[T] response — choose one:**

**Option A (CONFIRMED):** "[T] INVENTORY CONFIRMED. I have reviewed the STATE REGISTRY and OPERATION REGISTRY against the domain lifecycle of {{topic}}. No lifecycle state or operation is absent. States: [repeat complete list]. Operations: [repeat complete list]. HANDOFF DECLARATION acknowledged. Proceeding to GATE A."

**Option B (GAP FOUND):** "[T] INVENTORY INCOMPLETE. Gap identified: [state the missing state or operation and why it belongs in the lifecycle]. Returning to [D] for registry update. HANDOFF DECLARATION must be re-signed before GATE A proceeds."

---

### GATE A

Do not begin TRANSITION TABLE until all items are confirmed. Unconfirmed = TRANSITION TABLE blocked per C6.

- [ ] STATE REGISTRY complete — domain vocabulary, at least one terminal state
- [ ] OPERATION REGISTRY complete — all operations have source/target IDs from STATE REGISTRY
- [ ] INVARIANT REGISTRY complete — at least two assertions with authority sources
- [ ] VOCABULARY CLOSED declared with complete name list and forward-blocking prohibition
- [ ] HANDOFF DECLARATION signed by [D]
- [ ] **[C7]** INVENTORY CHALLENGE resolved — Option A or Option B written above
- [ ] **[C-14]** [T] confirms: no name will appear in TRANSITION TABLE, INVALID TRANSITIONS, or RACE CONDITIONS not in STATE REGISTRY or OPERATION REGISTRY
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
- **Preconditions:** Minimum two testable assertions per row (e.g., `status == Open`, `owner_id != null`).
- **Postconditions:** Minimum one assertion distinct from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED — [reason]`; never blank (C5).
- **Side Effects:** Triggered rules, record changes, notifications, async jobs.

---

### GATE B

Do not begin INVALID TRANSITIONS until all items are confirmed. Unconfirmed = INVALID TRANSITIONS blocked per C8.

- [ ] **[C-08]** TRANSITION TABLE is columnar and complete; no operation documented only in prose
- [ ] **[C-05]** Every row has INV status per declared invariant; at least one VIOLATED row present
- [ ] **[C-06]** Every row has at least one postcondition distinct from the To State name
- [ ] Boundary coverage planned — at least one terminal-state row targeted for INVALID TRANSITIONS

**GATE B BLOCKED per C8. Do not begin INVALID TRANSITIONS until all items confirmed.**

---

### INVALID TRANSITIONS [T]

| # | Attempted Operation | From State | Blocking Condition | INV Reference | Risk if Bypassed |
|---|---------------------|-----------|--------------------|--------------|--------------------|

Minimum three rows. Include at least one row where From State is a terminal state. All names from STATE REGISTRY and OPERATION REGISTRY only.

---

### GATE C

Do not begin RACE CONDITIONS until all items are confirmed. Unconfirmed = RACE CONDITIONS blocked per C9.

- [ ] **[C-04]** At least three (operation, state) invalid pairs named with blocking conditions; enumeration is systematic
- [ ] **[C-09]** At least one INVALID TRANSITIONS row has From State = a terminal state

**GATE C BLOCKED per C9. Do not begin RACE CONDITIONS until all items confirmed.**

---

### RACE CONDITIONS [T]

| Operation A | Operation B | Unsafe Interleaving | Outcome | Mitigation |
|-------------|-------------|---------------------|---------|-----------|

If no concurrent access: "No concurrent access — [reason]."

---

### GATE D

Do not write FINDINGS until all items are confirmed. Unconfirmed = FINDINGS blocked.

- [ ] **[C-07]** RACE CONDITIONS addressed — at least one race scenario or explicit clearance with reason
- [ ] All TRANSITION TABLE and INVALID TRANSITIONS names reference STATE REGISTRY and OPERATION REGISTRY only (C1, C2)
- [ ] Hard-stop review complete — no section is blank or placeholder-only

**GATE D BLOCKED. Do not write FINDINGS until all items confirmed.**

---

### FINDINGS

Priority order. Reference table and row.

- **P[N]:** [title] — [description, table row reference]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: CONSTRAINT MATRIX, ROLES, STATE REGISTRY, OPERATION REGISTRY, INVARIANT REGISTRY, VOCABULARY CLOSED, HANDOFF DECLARATION, INVENTORY CHALLENGE, GATE A, TRANSITION TABLE, GATE B, INVALID TRANSITIONS, GATE C, RACE CONDITIONS, GATE D, FINDINGS.

---

## V-02 — Output Format: Numbered Prose Inventory Declarations

**Axis:** Output format (single axis)
**Hypothesis:** The R8 ceiling requires STATE REGISTRY and OPERATION REGISTRY as columnar tables. V-02 tests whether numbered prose declarations (S-01 / O-01 style) survive the referential binding requirements of C-14 and C-15 without a table structure to anchor them. The CONSTRAINT MATRIX retains its columnar form — only the inventory sections change format. C-19 predicted FAIL (no Concern column possible in prose CONSTRAINT block if CONSTRAINT MATRIX is dropped; if CONSTRAINT MATRIX is kept, C-19 survives). Final decision: keep CONSTRAINT MATRIX in table form; change only STATE REGISTRY and OPERATION REGISTRY to numbered prose. Predicted: C-19 PASS (matrix kept), C-20 PASS, C-21 PASS, but a new formatting risk may emerge around C-14 if prose declarations are ambiguous. Composite predicted 14/14 = 100.00, with a stress test on whether prose inventory weakens referential integrity.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. Inventories are declared as numbered items. All transition data is delivered in columnar tables. Read CONSTRAINT MATRIX completely before producing any output.

---

### CONSTRAINT MATRIX

| ID | Prohibition | Assigned Role | Concern |
|----|-------------|---------------|---------|
| C1 | YOU MAY NOT introduce any state name in any trace table that is not declared in the STATE DECLARATIONS section | [T] | vocabulary |
| C2 | YOU MAY NOT introduce any operation name in any trace table that is not declared in the OPERATION DECLARATIONS section | [T] | vocabulary |
| C3 | YOU MAY NOT use prose paragraphs or bullet lists as the primary output format for trace data; every operation traces as a table row | [T] | format |
| C4 | YOU MAY NOT retroactively add states or operations after VOCABULARY CLOSED is declared | [D] | ordering |
| C5 | YOU MAY NOT leave any invariant status column blank in the TRANSITION TABLE | [T] | integrity |
| C6 | YOU MAY NOT begin TRANSITION TABLE until GATE A is confirmed | [T] | ordering |
| C7 | YOU MAY NOT proceed past INVENTORY CHALLENGE without a written Option A or Option B response; a blank response or non-option response is a C7 violation | [T] | completeness |
| C8 | YOU MAY NOT begin INVALID TRANSITIONS until GATE B is confirmed | [T] | ordering |
| C9 | YOU MAY NOT begin RACE CONDITIONS until GATE C is confirmed | [T] | ordering |

---

### ROLES

**[D] Domain Expert**
Auto-selected: Sales expert, Customer Service expert, or Finance expert.
Owns: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED.
Binding constraint from CONSTRAINT MATRIX: **C4**.

**[T] Trace Developer**
Owns: INVENTORY CHALLENGE response, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, BOUNDARY COVERAGE, FINDINGS.
Binding constraints from CONSTRAINT MATRIX: **C1, C2, C3, C5, C6, C7, C8, C9**.

---

### STATE DECLARATIONS [D]

Declare all lifecycle states as numbered items. Each item includes: ID, name, entry conditions, terminal status. Use domain vocabulary only.

**S-01.** [State Name] | Entry: [condition] | Terminal: Yes/No
**S-02.** [State Name] | Entry: [condition] | Terminal: Yes/No
...

At least one item must be Terminal: Yes. Generic labels (State A, initial, final) are prohibited.

---

### OPERATION DECLARATIONS [D]

Declare all lifecycle operations as numbered items. Each item includes: ID, name, legal source states (by S-ID), target state (by S-ID), triggering actor.

**O-01.** [Operation Name] | From: S-[N] | To: S-[N] | Actor: [role/system]
**O-02.** [Operation Name] | From: S-[N] | To: S-[N] | Actor: [role/system]
...

All S-IDs must reference STATE DECLARATIONS entries.

---

### INVARIANT DECLARATIONS [D]

Declare all invariants as numbered items. Each item includes: ID, name, checkable assertion, authority source.

**INV-01.** [Name]: [boolean assertion, e.g., `owner_id != null when status IN {Open, Pending}`] | Authority: [business rule / SLA / regulation]
**INV-02.** [Name]: [boolean assertion] | Authority: [source]

Minimum two invariants.

---

### VOCABULARY CLOSED [D]

> VOCABULARY CLOSED per C4. States: [list all S-IDs and State Names from STATE DECLARATIONS]. Operations: [list all O-IDs and Operation Names from OPERATION DECLARATIONS]. No new state or operation name may be introduced from this point forward. Any name not listed above is prohibited in all sections that follow.

---

### INVENTORY CHALLENGE

**C7 applies. [T] may not proceed to GATE A without a written response below. A blank response or non-option response is a C7 violation.**

INVENTORY COMPLETE — the STATE DECLARATIONS and OPERATION DECLARATIONS contain every state and operation in the lifecycle of {{topic}}.

**[T] response — choose one:**

**Option A (CONFIRMED):** "[T] INVENTORY CONFIRMED. I have reviewed STATE DECLARATIONS and OPERATION DECLARATIONS against the domain lifecycle of {{topic}}. No lifecycle state or operation is absent. States: [repeat S-IDs and names]. Operations: [repeat O-IDs and names]. Challenge resolved. Proceeding to GATE A."

**Option B (GAP FOUND):** "[T] INVENTORY INCOMPLETE. Gap identified: [missing item and reason it belongs in the lifecycle]. Returning to [D] for declaration update. VOCABULARY CLOSED must be re-declared before GATE A proceeds."

---

### GATE A

Do not begin TRANSITION TABLE until all items are confirmed. Unconfirmed = TRANSITION TABLE blocked per C6.

- [ ] STATE DECLARATIONS complete — domain vocabulary, at least one Terminal item
- [ ] OPERATION DECLARATIONS complete — all S-ID references resolve to STATE DECLARATIONS
- [ ] INVARIANT DECLARATIONS complete — at least two boolean assertions with authority sources
- [ ] VOCABULARY CLOSED declared with complete item list and forward-blocking prohibition
- [ ] **[C7]** INVENTORY CHALLENGE resolved — Option A or Option B written above
- [ ] **[C-14]** [T] confirms: no name will appear in TRANSITION TABLE, INVALID TRANSITIONS, or RACE CONDITIONS not declared in STATE DECLARATIONS or OPERATION DECLARATIONS
- [ ] **[C-15]** VOCABULARY CLOSED declared and forward-blocking prohibition is in effect

**GATE A BLOCKED per C6. Do not begin TRANSITION TABLE until all items confirmed.**

---

### TRANSITION TABLE [T]

Scenario setup: [entity instance, starting state, actor, date/time context]

Constraints C1, C2, C3, C5 apply.

| # | From State (S-ID) | Operation (O-ID) | Preconditions | To State (S-ID) | Postconditions | INV-01 | INV-02 | Side Effects |
|---|-------------------|-----------------|---------------|-----------------|----------------|--------|--------|--------------|

- **From State / To State:** S-IDs from STATE DECLARATIONS only (C1).
- **Operation:** O-IDs from OPERATION DECLARATIONS only (C2).
- **Preconditions:** Minimum two testable assertions per row.
- **Postconditions:** Minimum one assertion distinct from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED — [reason]`; never blank (C5).

---

### GATE B

Do not begin INVALID TRANSITIONS until all items are confirmed. Unconfirmed = INVALID TRANSITIONS blocked per C8.

- [ ] **[C-08]** TRANSITION TABLE is columnar and complete; no operation documented only in prose
- [ ] **[C-05]** Every row has INV status per declared invariant; at least one VIOLATED row present
- [ ] **[C-06]** Every row has at least one postcondition distinct from the To State name
- [ ] Boundary coverage planned — at least one terminal-state row targeted for INVALID TRANSITIONS

**GATE B BLOCKED per C8. Do not begin INVALID TRANSITIONS until all items confirmed.**

---

### INVALID TRANSITIONS [T]

| # | Attempted Operation (O-ID) | From State (S-ID) | Blocking Condition | INV Reference | Risk if Bypassed |
|---|---------------------------|------------------|--------------------|--------------|-----------------|

Minimum three rows. Include at least one row where From State is Terminal. S-IDs and O-IDs only.

---

### GATE C

Do not begin RACE CONDITIONS until all items are confirmed. Unconfirmed = RACE CONDITIONS blocked per C9.

- [ ] **[C-04]** At least three (operation, state) invalid pairs named with blocking conditions; enumeration is systematic
- [ ] **[C-09]** At least one INVALID TRANSITIONS row has From State = a Terminal state from STATE DECLARATIONS

**GATE C BLOCKED per C9. Do not begin RACE CONDITIONS until all items confirmed.**

---

### RACE CONDITIONS [T]

| Operation A (O-ID) | Operation B (O-ID) | Unsafe Interleaving | Outcome | Mitigation |
|--------------------|--------------------|---------------------|---------|-----------|

If no concurrent access: "No concurrent access — [reason]."

---

### GATE D

Do not write FINDINGS until all items are confirmed. Unconfirmed = FINDINGS blocked.

- [ ] **[C-07]** RACE CONDITIONS addressed — at least one race scenario or explicit clearance with reason
- [ ] All TRANSITION TABLE and INVALID TRANSITIONS S-IDs and O-IDs resolve to declarations (C1, C2)
- [ ] Hard-stop review complete — no section is blank or placeholder-only

**GATE D BLOCKED. Do not write FINDINGS until all items confirmed.**

---

### FINDINGS

Priority order. Reference section and item.

- **P[N]:** [title] — [description, section/row reference]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: CONSTRAINT MATRIX, ROLES, STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, INVENTORY CHALLENGE, GATE A, TRANSITION TABLE, GATE B, INVALID TRANSITIONS, GATE C, RACE CONDITIONS, GATE D, FINDINGS.

---

## V-03 — Phrasing Register: Declarative IS Framing

**Axis:** Phrasing register (single axis)
**Hypothesis:** All prior ceiling variants use imperative YOU MAY NOT phrasing for constraints. V-03 tests a declarative IS register throughout: "An operation IS NOT REACHABLE in any trace table unless it IS declared in the OPERATION REGISTRY." The constraint IDs are preserved; the prohibition text shifts to ontological framing. C-21 (challenge non-response violation binding) requires a specific enforcement statement — V-03 tests whether IS framing ("A blank response IS a C7 violation") satisfies the criterion or whether the rubric requires imperative phrasing. Predicted: C-19 PASS, C-20 PASS, C-21 PASS (IS framing is sufficient for violation binding), 14/14 = 100.00. If C-21 requires imperative phrasing, score drops to 13/14 = 99.29.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. The state machine is governed by an ontological constraint registry. Each constraint names an architectural fact about this trace. Read the CONSTRAINT MATRIX completely before producing any output. The matrix is authoritative.

---

### CONSTRAINT MATRIX

| ID | Architectural Fact | Assigned Role | Concern |
|----|-------------------|---------------|---------|
| C1 | A state name IS NOT REACHABLE in any trace table unless it IS declared in the STATE REGISTRY | [T] | vocabulary |
| C2 | An operation name IS NOT REACHABLE in any trace table unless it IS declared in the OPERATION REGISTRY | [T] | vocabulary |
| C3 | Prose paragraphs and bullet lists ARE NOT VALID primary output formats for trace data; every operation IS a table row | [T] | format |
| C4 | A state or operation name IS FROZEN after VOCABULARY CLOSED IS declared; retroactive additions ARE architectural violations | [D] | ordering |
| C5 | Every invariant status column in the TRANSITION TABLE IS REQUIRED to contain a value; blank IS a structural gap | [T] | integrity |
| C6 | TRANSITION TABLE IS BLOCKED until GATE A IS cleared | [T] | ordering |
| C7 | INVENTORY CHALLENGE IS a required checkpoint; a blank response or non-option response IS a C7 violation | [T] | completeness |
| C8 | INVALID TRANSITIONS IS BLOCKED until GATE B IS cleared | [T] | ordering |
| C9 | RACE CONDITIONS IS BLOCKED until GATE C IS cleared | [T] | ordering |

---

### ROLES

**[D] Domain Expert**
Auto-selected: Sales expert (Lead / Qualified Lead / Opportunity / Proposal / Closed Won / Closed Lost), Customer Service expert (New / Open / Pending / Resolved / Closed), or Finance expert (Draft / Submitted / Approved / Posted / Paid / Voided).
Owns: STATE REGISTRY, OPERATION REGISTRY, INVARIANT REGISTRY, VOCABULARY CLOSED.
Binding constraint from CONSTRAINT MATRIX: **C4** (vocabulary IS FROZEN after VOCABULARY CLOSED).

**[T] Trace Developer**
Owns: INVENTORY CHALLENGE written response, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, BOUNDARY COVERAGE, FINDINGS.
Binding constraints from CONSTRAINT MATRIX: **C1, C2, C3, C5, C6, C7, C8, C9**.

---

### STATE REGISTRY [D]

| State ID | State Name | Defining Field Values | Entry Conditions | Terminal? |
|---------|-----------|----------------------|-----------------|-----------|

Domain vocabulary only. At least one Terminal = Yes row IS REQUIRED.

---

### OPERATION REGISTRY [D]

| Op ID | Operation Name | Legal Source State IDs | Target State ID | Triggering Actor |
|-------|---------------|----------------------|----------------|-----------------|

All State IDs IS REQUIRED to reference STATE REGISTRY IDs.

---

### INVARIANT REGISTRY [D]

| INV ID | Invariant | Checkable Assertion | Authority Source |
|--------|-----------|--------------------|--------------------|

Minimum two invariants. Each assertion IS a boolean expression. Authority source IS one of: business rule, SLA clause, regulation, or policy.

---

### VOCABULARY CLOSED [D]

> VOCABULARY CLOSED per C4. States: [list all STATE REGISTRY State Names]. Operations: [list all OPERATION REGISTRY Operation Names]. The vocabulary IS FROZEN from this point forward. Any name not listed above IS PROHIBITED in all sections that follow. This prohibition IS NOT WAIVABLE.

---

### INVENTORY CHALLENGE

**C7 applies. INVENTORY CHALLENGE IS a required checkpoint. A blank response or non-option response IS a C7 violation.**

INVENTORY IS DECLARED COMPLETE — the STATE REGISTRY and OPERATION REGISTRY contain every state and operation in the lifecycle of {{topic}}.

**[T] response — one option IS REQUIRED:**

**Option A (CONFIRMED):** "[T] INVENTORY CONFIRMED. The STATE REGISTRY and OPERATION REGISTRY are the complete lifecycle vocabulary for {{topic}}. No lifecycle state or operation IS absent. States: [repeat complete list]. Operations: [repeat complete list]. Challenge resolved. Proceeding to GATE A."

**Option B (GAP FOUND):** "[T] INVENTORY INCOMPLETE. The following IS absent from the registry: [missing state or operation and why it IS required by the lifecycle]. Returning to [D] for STATE REGISTRY / OPERATION REGISTRY update. VOCABULARY CLOSED IS REQUIRED to be re-declared before GATE A proceeds."

---

### GATE A

TRANSITION TABLE IS BLOCKED until all items ARE confirmed. Unconfirmed IS a C6 violation.

- [ ] STATE REGISTRY IS COMPLETE — domain vocabulary, at least one terminal state present
- [ ] OPERATION REGISTRY IS COMPLETE — all operations have source/target IDs from STATE REGISTRY
- [ ] INVARIANT REGISTRY IS COMPLETE — at least two assertions with authority sources
- [ ] VOCABULARY CLOSED IS DECLARED with complete name list and forward-blocking prohibition
- [ ] **[C7]** INVENTORY CHALLENGE IS RESOLVED — Option A or Option B IS written above
- [ ] **[C-14]** [T] CONFIRMS: no name IS PRESENT in TRANSITION TABLE, INVALID TRANSITIONS, or RACE CONDITIONS that IS NOT in STATE REGISTRY or OPERATION REGISTRY
- [ ] **[C-15]** VOCABULARY CLOSED IS DECLARED and the forward-blocking prohibition IS IN EFFECT

**GATE A IS BLOCKED per C6. TRANSITION TABLE IS NOT REACHABLE until all items ARE confirmed.**

---

### TRANSITION TABLE [T]

Scenario setup: [entity instance, starting state, actor, date/time context]

C1, C2, C3, C5 ARE IN EFFECT.

| # | From State | Operation | Preconditions | To State | Postconditions | INV-01 | INV-02 | Side Effects |
|---|-----------|-----------|---------------|---------|----------------|--------|--------|--------------|

- **From State / To State:** STATE REGISTRY names IS REQUIRED; unlisted names ARE violations (C1).
- **Operation:** OPERATION REGISTRY names IS REQUIRED; unlisted names ARE violations (C2).
- **Preconditions:** Minimum two testable assertions per row.
- **Postconditions:** Minimum one assertion that IS DISTINCT from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED — [reason]`; blank IS a C5 violation.

---

### GATE B

INVALID TRANSITIONS IS BLOCKED until all items ARE confirmed. Unconfirmed IS a C8 violation.

- [ ] **[C-08]** TRANSITION TABLE IS COLUMNAR and COMPLETE; no operation IS documented only in prose
- [ ] **[C-05]** Every row HAS an INV status per declared invariant; at least one VIOLATED row IS PRESENT
- [ ] **[C-06]** Every row HAS at least one postcondition that IS DISTINCT from the To State name
- [ ] Boundary coverage IS PLANNED — at least one terminal-state row IS TARGETED for INVALID TRANSITIONS

**GATE B IS BLOCKED per C8. INVALID TRANSITIONS IS NOT REACHABLE until all items ARE confirmed.**

---

### INVALID TRANSITIONS [T]

| # | Attempted Operation | From State | Blocking Condition | INV Reference | Risk if Bypassed |
|---|---------------------|-----------|--------------------|--------------|--------------------|

Minimum three rows. At least one row IS REQUIRED where From State IS a terminal state. All names ARE FROM STATE REGISTRY and OPERATION REGISTRY.

---

### GATE C

RACE CONDITIONS IS BLOCKED until all items ARE confirmed. Unconfirmed IS a C9 violation.

- [ ] **[C-04]** At least three (operation, state) invalid pairs ARE NAMED with blocking conditions; enumeration IS SYSTEMATIC
- [ ] **[C-09]** At least one INVALID TRANSITIONS row HAS From State IS a terminal state

**GATE C IS BLOCKED per C9. RACE CONDITIONS IS NOT REACHABLE until all items ARE confirmed.**

---

### RACE CONDITIONS [T]

| Operation A | Operation B | Unsafe Interleaving | Outcome | Mitigation |
|-------------|-------------|---------------------|---------|-----------|

If no concurrent access: "No concurrent access — [reason explaining why concurrent access IS NOT POSSIBLE]."

---

### GATE D

FINDINGS IS BLOCKED until all items ARE confirmed.

- [ ] **[C-07]** RACE CONDITIONS IS ADDRESSED — at least one race scenario or explicit clearance with reason IS PRESENT
- [ ] All TRANSITION TABLE and INVALID TRANSITIONS names ARE FROM STATE REGISTRY and OPERATION REGISTRY (C1, C2)
- [ ] Hard-stop review IS COMPLETE — no section IS blank or placeholder-only

**GATE D IS BLOCKED. FINDINGS IS NOT REACHABLE until all items ARE confirmed.**

---

### FINDINGS

Priority order. Reference table and row.

- **P[N]:** [title] — [description, table row reference]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: CONSTRAINT MATRIX, ROLES, STATE REGISTRY, OPERATION REGISTRY, INVARIANT REGISTRY, VOCABULARY CLOSED, INVENTORY CHALLENGE, GATE A, TRANSITION TABLE, GATE B, INVALID TRANSITIONS, GATE C, RACE CONDITIONS, GATE D, FINDINGS.

---

## V-04 — Combined: Role Sequence + Lifecycle Emphasis

**Axis:** Role sequence + lifecycle emphasis (combined)
**Hypothesis:** V-01 adds a HANDOFF DECLARATION making [D]→[T] transfer structural. This variant wraps the entire trace in two explicit macro-phases: DECLARATION PHASE (owned by [D]) and TRACE PHASE (owned by [T]). The HANDOFF DECLARATION becomes the inter-phase boundary marker. GATE A–D operate within TRACE PHASE as sub-section gates. The macro-phase framing adds one layer of lifecycle emphasis on top of the R8 ceiling structure. Predicted: C-19 PASS (CONSTRAINT MATRIX retained), C-20 PASS (GATE A–D preserved as sub-section gates within TRACE PHASE), C-21 PASS (INVENTORY CHALLENGE with C7 binding retained). 14/14 = 100.00. HANDOFF DECLARATION may seed C-22; macro-phase framing may seed C-23 (explicit lifecycle phase declaration).

---

You are running a **trace-state** signal for: {{topic}}

This trace executes in two phases. **DECLARATION PHASE** is owned by [D] and produces the authoritative vocabulary. **TRACE PHASE** is owned by [T] and is blocked until [D] signs HANDOFF DECLARATION. Within TRACE PHASE, four named gates enforce section-level ordering. Read CONSTRAINT MATRIX completely before producing any output.

---

### CONSTRAINT MATRIX

| ID | Prohibition | Assigned Role | Concern |
|----|-------------|---------------|---------|
| C1 | YOU MAY NOT introduce any state name in any trace table that is not declared in the STATE REGISTRY | [T] | vocabulary |
| C2 | YOU MAY NOT introduce any operation name in any trace table that is not declared in the OPERATION REGISTRY | [T] | vocabulary |
| C3 | YOU MAY NOT use prose paragraphs or bullet lists as the primary output format for trace data; every operation traces as a table row | [T] | format |
| C4 | YOU MAY NOT retroactively add states or operations after HANDOFF DECLARATION is signed | [D] | ordering |
| C5 | YOU MAY NOT leave any invariant status column blank in the TRANSITION TABLE | [T] | integrity |
| C6 | YOU MAY NOT begin TRANSITION TABLE until GATE A is confirmed | [T] | ordering |
| C7 | YOU MAY NOT proceed past INVENTORY CHALLENGE without a written Option A or Option B response; a blank response or non-option response is a C7 violation | [T] | completeness |
| C8 | YOU MAY NOT begin INVALID TRANSITIONS until GATE B is confirmed | [T] | ordering |
| C9 | YOU MAY NOT begin RACE CONDITIONS until GATE C is confirmed | [T] | ordering |
| C10 | YOU MAY NOT begin TRACE PHASE until HANDOFF DECLARATION is signed by [D] | [T] | ordering |

---

### ROLES

**[D] Domain Expert**
Auto-selected: Sales expert (Lead / Qualified Lead / Opportunity / Proposal / Closed Won / Closed Lost), Customer Service expert (New / Open / Pending / Resolved / Closed), or Finance expert (Draft / Submitted / Approved / Posted / Paid / Voided).
Owns: DECLARATION PHASE (all sections within it) including STATE REGISTRY, OPERATION REGISTRY, INVARIANT REGISTRY, VOCABULARY CLOSED, HANDOFF DECLARATION.
Binding constraint from CONSTRAINT MATRIX: **C4** (may not retroactively add vocabulary after HANDOFF DECLARATION is signed).

**[T] Trace Developer**
Owns: TRACE PHASE (all sections within it) including INVENTORY CHALLENGE response, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, BOUNDARY COVERAGE, FINDINGS.
Binding constraints from CONSTRAINT MATRIX: **C1, C2, C3, C5, C6, C7, C8, C9, C10**.

---

## DECLARATION PHASE [D]

[D] owns this phase completely. TRACE PHASE does not begin until HANDOFF DECLARATION is signed.

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

Minimum two invariants as boolean assertions. Authority source: business rule, SLA clause, regulation, or policy.

---

### VOCABULARY CLOSED [D]

> VOCABULARY CLOSED per C4. States: [list all STATE REGISTRY State Names]. Operations: [list all OPERATION REGISTRY Operation Names]. No new state or operation name may be introduced from this point forward. Any name not listed above is prohibited in all sections that follow.

---

### HANDOFF DECLARATION [D]

> **[D] HANDOFF DECLARATION.** DECLARATION PHASE is complete. STATE REGISTRY ([N] states), OPERATION REGISTRY ([N] operations), and INVARIANT REGISTRY ([N] invariants) are final. VOCABULARY CLOSED is in effect. TRACE PHASE is now authorized for [T]. Constraints C1, C2, C3, C5, C6, C7, C8, C9 are active. [D] may not alter any registry entry from this point forward (C4).
>
> **[D] Signed:** [domain role selected] — [N] states, [N] operations.

---

## TRACE PHASE [T]

[T] owns this phase. TRACE PHASE IS BLOCKED per C10 until HANDOFF DECLARATION above is signed.

---

### INVENTORY CHALLENGE

**C7 applies. [T] may not proceed to GATE A without a written response below. A blank response or non-option response is a C7 violation.**

INVENTORY COMPLETE — the STATE REGISTRY and OPERATION REGISTRY contain every state and operation in the lifecycle of {{topic}}.

**[T] response — choose one:**

**Option A (CONFIRMED):** "[T] INVENTORY CONFIRMED. HANDOFF DECLARATION acknowledged. I have reviewed STATE REGISTRY and OPERATION REGISTRY against the domain lifecycle of {{topic}}. No lifecycle state or operation is absent. States: [repeat complete list]. Operations: [repeat complete list]. Proceeding to GATE A."

**Option B (GAP FOUND):** "[T] INVENTORY INCOMPLETE. Gap identified: [missing item and why it belongs]. Returning to [D] for DECLARATION PHASE update. HANDOFF DECLARATION must be re-signed before GATE A proceeds."

---

### GATE A

Do not begin TRANSITION TABLE until all items are confirmed. Unconfirmed = TRANSITION TABLE blocked per C6.

- [ ] HANDOFF DECLARATION signed by [D] (C10)
- [ ] STATE REGISTRY complete — domain vocabulary, at least one terminal state
- [ ] OPERATION REGISTRY complete — all operations have source/target IDs from STATE REGISTRY
- [ ] INVARIANT REGISTRY complete — at least two assertions with authority sources
- [ ] VOCABULARY CLOSED declared with complete name list and forward-blocking prohibition
- [ ] **[C7]** INVENTORY CHALLENGE resolved — Option A or Option B written above
- [ ] **[C-14]** [T] confirms: no name will appear in trace tables not declared in STATE REGISTRY or OPERATION REGISTRY
- [ ] **[C-15]** VOCABULARY CLOSED forward-blocking prohibition is in effect

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
- **Side Effects:** Triggered rules, notifications, async jobs.

---

### GATE B

Do not begin INVALID TRANSITIONS until all items are confirmed. Unconfirmed = INVALID TRANSITIONS blocked per C8.

- [ ] **[C-08]** TRANSITION TABLE is columnar and complete
- [ ] **[C-05]** Every row has INV status per declared invariant; at least one VIOLATED row present
- [ ] **[C-06]** Every row has at least one postcondition distinct from the To State name
- [ ] Terminal-state row planned for INVALID TRANSITIONS

**GATE B BLOCKED per C8. Do not begin INVALID TRANSITIONS until all items confirmed.**

---

### INVALID TRANSITIONS [T]

| # | Attempted Operation | From State | Blocking Condition | INV Reference | Risk if Bypassed |
|---|---------------------|-----------|--------------------|--------------|--------------------|

Minimum three rows. At least one row where From State is a terminal state. All names from STATE REGISTRY and OPERATION REGISTRY only.

---

### GATE C

Do not begin RACE CONDITIONS until all items are confirmed. Unconfirmed = RACE CONDITIONS blocked per C9.

- [ ] **[C-04]** At least three (operation, state) invalid pairs named with blocking conditions; enumeration is systematic
- [ ] **[C-09]** At least one INVALID TRANSITIONS row has From State = a terminal state

**GATE C BLOCKED per C9. Do not begin RACE CONDITIONS until all items confirmed.**

---

### RACE CONDITIONS [T]

| Operation A | Operation B | Unsafe Interleaving | Outcome | Mitigation |
|-------------|-------------|---------------------|---------|-----------|

If no concurrent access: "No concurrent access — [reason]."

---

### GATE D

Do not write FINDINGS until all items are confirmed. Unconfirmed = FINDINGS blocked.

- [ ] **[C-07]** RACE CONDITIONS addressed — at least one race scenario or explicit clearance with reason
- [ ] All trace table names reference STATE REGISTRY and OPERATION REGISTRY only (C1, C2)
- [ ] Hard-stop review complete — no section is blank or placeholder-only

**GATE D BLOCKED. Do not write FINDINGS until all items confirmed.**

---

### FINDINGS

Priority order. Reference table and row.

- **P[N]:** [title] — [description, table row reference]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: CONSTRAINT MATRIX, ROLES, DECLARATION PHASE (STATE REGISTRY, OPERATION REGISTRY, INVARIANT REGISTRY, VOCABULARY CLOSED, HANDOFF DECLARATION), TRACE PHASE (INVENTORY CHALLENGE, GATE A, TRANSITION TABLE, GATE B, INVALID TRANSITIONS, GATE C, RACE CONDITIONS, GATE D, FINDINGS).

---

## V-05 — Full Synthesis: R8 V-02 Ceiling + V-01 Handoff + V-03 IS Register

**Axis:** Full synthesis (combined — additive onto R8 V-02 confirmed ceiling)
**Hypothesis:** R8 V-02 is the confirmed ceiling variant (CONSTRAINT MATRIX with Concern column, INVENTORY CHALLENGE with C7 binding, GATE A–D per section). V-05 adds two features: (1) HANDOFF DECLARATION from V-01 (structural [D]→[T] transfer event); (2) IS framing in the CONSTRAINT MATRIX Prohibition column from V-03 (declarative register for architectural facts). No structural sections are removed; two sections are added or modified. Predicted: all 14 aspirational PASS (100.00) plus HANDOFF DECLARATION and IS-register features as C-22/C-23 seeds. This is the reference ceiling synthesis for Round 9.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. All constraints governing this trace are pre-registered in the CONSTRAINT MATRIX as architectural facts. Read the matrix completely before producing any output. The matrix is authoritative. Two roles execute in sequence; [D] signs HANDOFF DECLARATION before [T] proceeds.

---

### CONSTRAINT MATRIX

| ID | Architectural Fact | Assigned Role | Concern |
|----|-------------------|---------------|---------|
| C1 | A state name IS NOT REACHABLE in any trace table unless it IS declared in the STATE REGISTRY | [T] | vocabulary |
| C2 | An operation name IS NOT REACHABLE in any trace table unless it IS declared in the OPERATION REGISTRY | [T] | vocabulary |
| C3 | Prose paragraphs and bullet lists ARE NOT VALID primary output formats; every operation IS a table row | [T] | format |
| C4 | Vocabulary IS FROZEN after HANDOFF DECLARATION IS signed; retroactive additions ARE architectural violations | [D] | ordering |
| C5 | Every invariant status column in TRANSITION TABLE IS REQUIRED to contain HOLDS or VIOLATED — [reason] | [T] | integrity |
| C6 | TRANSITION TABLE IS BLOCKED until GATE A IS cleared | [T] | ordering |
| C7 | INVENTORY CHALLENGE IS a required checkpoint; a blank response or non-option response IS a C7 violation | [T] | completeness |
| C8 | INVALID TRANSITIONS IS BLOCKED until GATE B IS cleared | [T] | ordering |
| C9 | RACE CONDITIONS IS BLOCKED until GATE C IS cleared | [T] | ordering |
| C10 | TRACE SECTIONS ARE BLOCKED until HANDOFF DECLARATION IS signed by [D] | [T] | ordering |

---

### ROLES

**[D] Domain Expert**
Auto-selected: Sales expert (Lead / Qualified Lead / Opportunity / Proposal / Closed Won / Closed Lost), Customer Service expert (New / Open / Pending / Resolved / Closed), or Finance expert (Draft / Submitted / Approved / Posted / Paid / Voided).
Owns: STATE REGISTRY, OPERATION REGISTRY, INVARIANT REGISTRY, VOCABULARY CLOSED, HANDOFF DECLARATION.
Binding constraint from CONSTRAINT MATRIX: **C4** (vocabulary IS FROZEN after HANDOFF DECLARATION IS signed).

**[T] Trace Developer**
Owns: INVENTORY CHALLENGE written response, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, BOUNDARY COVERAGE, FINDINGS.
Binding constraints from CONSTRAINT MATRIX: **C1, C2, C3, C5, C6, C7, C8, C9, C10**.

---

### STATE REGISTRY [D]

| State ID | State Name | Defining Field Values | Entry Conditions | Terminal? |
|---------|-----------|----------------------|-----------------|-----------|

Domain vocabulary only. At least one Terminal = Yes row IS REQUIRED.

---

### OPERATION REGISTRY [D]

| Op ID | Operation Name | Legal Source State IDs | Target State ID | Triggering Actor |
|-------|---------------|----------------------|----------------|-----------------|

All State IDs IS REQUIRED to reference STATE REGISTRY IDs.

---

### INVARIANT REGISTRY [D]

| INV ID | Invariant | Checkable Assertion | Authority Source |
|--------|-----------|--------------------|--------------------|

Minimum two invariants. Each assertion IS a boolean expression. Authority source IS one of: business rule, SLA clause, regulation, or policy.

---

### VOCABULARY CLOSED [D]

> VOCABULARY CLOSED per C4. States: [list all STATE REGISTRY State Names]. Operations: [list all OPERATION REGISTRY Operation Names]. The vocabulary IS FROZEN from this point forward. Any name not listed above IS PROHIBITED in all sections that follow. This prohibition IS NOT WAIVABLE.

---

### HANDOFF DECLARATION [D]

> **[D] HANDOFF DECLARATION.** The STATE REGISTRY, OPERATION REGISTRY, and INVARIANT REGISTRY for {{topic}} ARE COMPLETE. VOCABULARY IS FROZEN per C4. The following sections ARE hereby transferred to [T]: INVENTORY CHALLENGE response, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, BOUNDARY COVERAGE, FINDINGS. [T] IS now authorized to proceed. Constraints C1, C2, C3, C5, C6, C7, C8, C9 ARE IN EFFECT. [D] IS PROHIBITED from altering any registry entry from this point forward (C4).
>
> **[D] Signed:** [domain role selected] — [N] states, [N] operations.

---

### INVENTORY CHALLENGE

**C7 applies. INVENTORY CHALLENGE IS a required checkpoint. A blank response or non-option response IS a C7 violation.**

INVENTORY IS DECLARED COMPLETE — the STATE REGISTRY and OPERATION REGISTRY contain every state and operation in the lifecycle of {{topic}}.

**[T] response — one option IS REQUIRED:**

**Option A (CONFIRMED):** "[T] INVENTORY CONFIRMED. HANDOFF DECLARATION acknowledged. The STATE REGISTRY and OPERATION REGISTRY ARE the complete lifecycle vocabulary for {{topic}}. No lifecycle state or operation IS absent. States: [repeat complete list]. Operations: [repeat complete list]. Proceeding to GATE A."

**Option B (GAP FOUND):** "[T] INVENTORY INCOMPLETE. The following IS absent from the registry: [missing item and why it IS required by the lifecycle]. Returning to [D] for registry update. HANDOFF DECLARATION IS REQUIRED to be re-signed before GATE A proceeds."

---

### GATE A

TRANSITION TABLE IS BLOCKED until all items ARE confirmed. Unconfirmed IS a C6 violation.

- [ ] STATE REGISTRY IS COMPLETE — domain vocabulary, at least one terminal state present
- [ ] OPERATION REGISTRY IS COMPLETE — all operations have source/target IDs from STATE REGISTRY
- [ ] INVARIANT REGISTRY IS COMPLETE — at least two boolean assertions with authority sources
- [ ] VOCABULARY IS FROZEN — VOCABULARY CLOSED IS declared with complete name list
- [ ] HANDOFF DECLARATION IS signed by [D] (C10)
- [ ] **[C7]** INVENTORY CHALLENGE IS RESOLVED — Option A or Option B IS written above
- [ ] **[C-14]** [T] CONFIRMS: no name IS PRESENT in trace tables that IS NOT in STATE REGISTRY or OPERATION REGISTRY
- [ ] **[C-15]** VOCABULARY CLOSED IS DECLARED and the forward-blocking prohibition IS IN EFFECT

**GATE A IS BLOCKED per C6. TRANSITION TABLE IS NOT REACHABLE until all items ARE confirmed.**

---

### TRANSITION TABLE [T]

Scenario setup: [entity instance, starting state, actor, date/time context]

C1, C2, C3, C5 ARE IN EFFECT.

| # | From State | Operation | Preconditions | To State | Postconditions | INV-01 | INV-02 | Side Effects |
|---|-----------|-----------|---------------|---------|----------------|--------|--------|--------------|

- **From State / To State:** STATE REGISTRY names only; unlisted names ARE C1 violations.
- **Operation:** OPERATION REGISTRY names only; unlisted names ARE C2 violations.
- **Preconditions:** Minimum two testable assertions per row.
- **Postconditions:** Minimum one assertion that IS DISTINCT from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED — [reason]`; blank IS a C5 violation.
- **Side Effects:** Triggered rules, notifications, async jobs.

---

### GATE B

INVALID TRANSITIONS IS BLOCKED until all items ARE confirmed. Unconfirmed IS a C8 violation.

- [ ] **[C-08]** TRANSITION TABLE IS COLUMNAR and COMPLETE; no operation IS documented only in prose
- [ ] **[C-05]** Every row HAS an INV status per declared invariant; at least one VIOLATED row IS PRESENT
- [ ] **[C-06]** Every row HAS at least one postcondition that IS DISTINCT from the To State name
- [ ] Terminal-state coverage IS PLANNED — at least one terminal-state row IS TARGETED for INVALID TRANSITIONS

**GATE B IS BLOCKED per C8. INVALID TRANSITIONS IS NOT REACHABLE until all items ARE confirmed.**

---

### INVALID TRANSITIONS [T]

| # | Attempted Operation | From State | Blocking Condition | INV Reference | Risk if Bypassed |
|---|---------------------|-----------|--------------------|--------------|--------------------|

Minimum three rows. At least one row IS REQUIRED where From State IS a terminal state. All names ARE FROM STATE REGISTRY and OPERATION REGISTRY.

---

### GATE C

RACE CONDITIONS IS BLOCKED until all items ARE confirmed. Unconfirmed IS a C9 violation.

- [ ] **[C-04]** At least three (operation, state) invalid pairs ARE NAMED with blocking conditions; enumeration IS SYSTEMATIC
- [ ] **[C-09]** At least one INVALID TRANSITIONS row HAS From State IS a terminal state

**GATE C IS BLOCKED per C9. RACE CONDITIONS IS NOT REACHABLE until all items ARE confirmed.**

---

### RACE CONDITIONS [T]

| Operation A | Operation B | Unsafe Interleaving | Outcome | Mitigation |
|-------------|-------------|---------------------|---------|-----------|

If no concurrent access: "No concurrent access — [reason explaining why concurrent access IS NOT POSSIBLE]."

---

### GATE D

FINDINGS IS BLOCKED until all items ARE confirmed.

- [ ] **[C-07]** RACE CONDITIONS IS ADDRESSED — at least one race scenario or explicit clearance IS PRESENT
- [ ] All trace table names ARE FROM STATE REGISTRY and OPERATION REGISTRY (C1, C2 confirmed)
- [ ] Hard-stop review IS COMPLETE — no section IS blank or placeholder-only

**GATE D IS BLOCKED. FINDINGS IS NOT REACHABLE until all items ARE confirmed.**

---

### FINDINGS

Priority order. Reference table and row.

- **P[N]:** [title] — [description, table row reference]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: CONSTRAINT MATRIX, ROLES, STATE REGISTRY, OPERATION REGISTRY, INVARIANT REGISTRY, VOCABULARY CLOSED, HANDOFF DECLARATION, INVENTORY CHALLENGE, GATE A, TRANSITION TABLE, GATE B, INVALID TRANSITIONS, GATE C, RACE CONDITIONS, GATE D, FINDINGS.

---

## Round 9 Scoring Predictions

| Variant | Axis | C-19 | C-20 | C-21 | Aspirational | Composite | Notes |
|---------|------|------|------|------|-------------|-----------|-------|
| V-01 | Role sequence (HANDOFF DECLARATION) | PASS | PASS | PASS | 14/14 | 100.00 | HANDOFF DECLARATION seeds C-22 |
| V-02 | Output format (prose inventories) | PASS | PASS | PASS | 14/14 | 100.00 | Stress-tests C-14 with prose format |
| V-03 | Phrasing register (IS framing) | PASS | PASS | PASS* | 14/14 | 100.00 | C-21 PASS if IS binding is sufficient; drop to 13/14 if rubric requires imperative |
| V-04 | Role sequence + lifecycle emphasis | PASS | PASS | PASS | 14/14 | 100.00 | Macro-phase framing seeds C-23 |
| V-05 | Full synthesis (R8 V-02 + V-01 + V-03) | PASS | PASS | PASS | 14/14 | 100.00 | Reference ceiling + two C-22/C-23 seeds |

**New aspirational criteria seeded by R9 structural innovations:**

- **C-22 (candidate):** Explicit role-transfer declaration — a named HANDOFF DECLARATION section signed by [D] and acknowledged by [T] makes the [D]→[T] handoff structural. C-22 passes when a HANDOFF DECLARATION (or equivalent named transfer event) appears after VOCABULARY CLOSED and before INVENTORY CHALLENGE, signed by [D]. V-01, V-04, V-05 satisfy this. V-02, V-03 do not.

- **C-23 (candidate):** Explicit lifecycle phase declaration — the document declares two or more named lifecycle phases (e.g., DECLARATION PHASE / TRACE PHASE) with explicit ownership assignments and inter-phase gates. C-23 passes when macro-phases are named, owned, and gated. V-04 satisfies this. V-01, V-02, V-03, V-05 do not.
