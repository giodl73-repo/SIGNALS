# trace-state Variate — Round 10
**Date:** 2026-03-15
**Rubric:** v8 (C-01..C-24; golden: all essential pass AND composite >= 80)
**Situation:** R9 closed three new aspirational criteria: C-22 (HANDOFF DECLARATION, from V-01), C-23 (numbered prose inventory declarations, from V-02), C-24 (uniform IS-phrasing register, from V-03). Each R9 variant contributes exactly one of the three and fails the other two; all score 15/17 (98.82, Golden). The new ceiling is 100.00, requiring all three simultaneously alongside the 14 prior aspirational criteria. R10 objective: synthesize C-22 + C-23 + C-24 in a single variant. Three pairwise combinations probe structural coexistence; V-04 is the full synthesis target; V-05 adds inertia framing as a new axis to seed C-25+.

---

## Round 9 Results (Basis for R10)

| Variant | C-22 | C-23 | C-24 | Aspirational (v8) | Composite |
|---------|------|------|------|-------------------|-----------|
| V-01 R9 | PASS | FAIL | FAIL | 15/17 = 98.82 | Golden |
| V-02 R9 | FAIL | PASS | FAIL | 15/17 = 98.82 | Golden |
| V-03 R9 | FAIL | FAIL | PASS | 15/17 = 98.82 | Golden |

No R9 variant achieves 100.00. The synthesis of all three has not been attempted.

---

## Round 10 Variation Map

| Var | Axis | Hypothesis | C-22 | C-23 | C-24 | Predicted |
|-----|------|------------|------|------|------|-----------|
| V-01 | C-22 + C-23 pairwise (HANDOFF + Numbered Prose, imperative) | HANDOFF DECLARATION and numbered prose inventories coexist; the formal transfer event references artifacts by S-ID/O-ID rather than table rows; imperative phrasing preserved; C-24 FAIL | PASS | PASS | FAIL | 16/17 = 99.41 |
| V-02 | C-22 + C-24 pairwise (HANDOFF + IS-phrasing, tabular inventories) | HANDOFF DECLARATION is expressible in IS register without losing the structural specificity C-22 requires; tabular inventories preserved; C-23 FAIL | PASS | FAIL | PASS | 16/17 = 99.41 |
| V-03 | C-23 + C-24 pairwise (Numbered Prose + IS-phrasing, no HANDOFF) | Numbered prose inventories and IS-phrasing coexist; IS register applies naturally in inline definitional clauses; no HANDOFF DECLARATION; C-22 FAIL | FAIL | PASS | PASS | 16/17 = 99.41 |
| V-04 | Full synthesis: C-22 + C-23 + C-24 | All three R9 innovations are simultaneously compatible; IS register works in HANDOFF DECLARATION body; numbered prose inventories work with IS-phrasing in definitional clauses; HANDOFF DECLARATION references artifacts by S-ID/O-ID; first predicted ceiling hit | PASS | PASS | PASS | 17/17 = 100.00 |
| V-05 | Full synthesis + inertia framing | V-04 synthesis holds; INERTIA BASELINE section names the status-quo alternative and the failure mode; tests whether explicit inertia declaration seeds C-25; 17/17 under v8, potential new criterion | PASS | PASS | PASS | 17/17 = 100.00 |

---

## V-01 — C-22 + C-23 Pairwise Synthesis: HANDOFF DECLARATION + Numbered Prose Inventories

**Axis:** Role sequence + output format (two-axis pairwise, single-new-combination)
**Hypothesis:** C-22 (HANDOFF DECLARATION) and C-23 (numbered prose inventories) coexist without structural tension. The [D]->[T] role transfer can name prose-declared artifacts by S-ID/O-ID rather than table rows. Imperative phrasing preserved throughout -- C-24 is NOT targeted. All 14 prior aspirational criteria hold. Pairwise score predicts 16/17 (99.41, Golden). Structural test: does the HANDOFF DECLARATION's specificity requirement (name artifacts transferred) work when inventories are prose items rather than table sections?

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. Domain vocabulary is declared by a Domain Expert [D] as numbered prose items before any tracing begins. A Trace Developer [T] executes the trace using only declared vocabulary. [D] signs a HANDOFF DECLARATION before [T] may proceed. Read the CONSTRAINT MATRIX completely before producing any output.

---

### CONSTRAINT MATRIX

| ID | Prohibition | Assigned Role | Concern |
|----|-------------|---------------|---------|
| C1 | YOU MAY NOT introduce any state name in any trace table not declared in STATE DECLARATIONS | [T] | vocabulary |
| C2 | YOU MAY NOT introduce any operation name in any trace table not declared in OPERATION DECLARATIONS | [T] | vocabulary |
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
Auto-selected: Sales expert (Lead / Qualified Lead / Opportunity / Proposal / Closed Won / Closed Lost), Customer Service expert (New / Open / Pending / Resolved / Closed), or Finance expert (Draft / Submitted / Approved / Posted / Paid / Voided).
Owns: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, HANDOFF DECLARATION.
Binding constraint from CONSTRAINT MATRIX: **C4** (may not retroactively add vocabulary after VOCABULARY CLOSED is declared).

**[T] Trace Developer**
Owns: INVENTORY CHALLENGE written response, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, FINDINGS.
Binding constraints from CONSTRAINT MATRIX: **C1, C2, C3, C5, C6, C7, C8, C9**.
Authorization: [T] is blocked from all trace sections until HANDOFF DECLARATION is signed by [D].

---

### STATE DECLARATIONS [D]

Declare all lifecycle states as numbered prose items. Each item must include an inline definitional clause that distinguishes this state from all others by meaning -- what conditions cause entry, what field values characterize it, and whether it is terminal. Use domain vocabulary only; generic labels (State A, initial, final) are prohibited.

**S-01.** [State Name] -- [inline definitional clause: the conditions that cause entry into this state, the field values that characterize it, and how it is distinct from adjacent states]. Terminal: Yes/No.
**S-02.** [State Name] -- [inline definitional clause]. Terminal: Yes/No.
*(continue for all lifecycle states)*

At least one item must be Terminal: Yes. Do not begin OPERATION DECLARATIONS until STATE DECLARATIONS are complete.

---

### OPERATION DECLARATIONS [D]

Declare all lifecycle operations as numbered prose items. Each item must include an inline definitional clause naming what the operation does, when it is triggered, which states it transitions from, and which state it produces. Use S-IDs to reference STATE DECLARATIONS entries.

**O-01.** [Operation Name] -- [inline definitional clause: what this operation does, when it is triggered, and what distinguishes it from similar operations in the lifecycle]. From: S-[N][, S-[N]...]. To: S-[N]. Actor: [role/system].
**O-02.** [Operation Name] -- [inline definitional clause]. From: S-[N]. To: S-[N]. Actor: [role/system].
*(continue for all lifecycle operations)*

All S-IDs must reference STATE DECLARATIONS entries. No operation may be declared without From and To references. Do not begin INVARIANT DECLARATIONS until OPERATION DECLARATIONS are complete.

---

### INVARIANT DECLARATIONS [D]

Declare all object-level invariants as numbered items. Each item must include a boolean assertion and an authority source.

**INV-01.** [Name] -- [boolean assertion, e.g., `owner_id != null when status IN {S-02, S-03}`]. Authority: [business rule / SLA clause / regulation / policy].
**INV-02.** [Name] -- [boolean assertion]. Authority: [source].
*(minimum two invariants)*

---

### VOCABULARY CLOSED [D]

> VOCABULARY CLOSED per C4. States: [list all S-IDs and State Names from STATE DECLARATIONS]. Operations: [list all O-IDs and Operation Names from OPERATION DECLARATIONS]. No new state or operation name may be introduced from this point forward. Any name not listed above is prohibited in all sections that follow.

Do not begin HANDOFF DECLARATION until VOCABULARY CLOSED is declared.

---

### HANDOFF DECLARATION [D]

> **[D] HANDOFF DECLARATION.** The STATE DECLARATIONS (S-01 through S-[N]), OPERATION DECLARATIONS (O-01 through O-[N]), and INVARIANT DECLARATIONS (INV-01 through INV-[N]) for {{topic}} are complete. VOCABULARY CLOSED is in effect. The following sections are hereby transferred to [T]: INVENTORY CHALLENGE response, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, FINDINGS. [T] is now authorized to proceed subject to constraints C1, C2, C3, C5, C6, C7, C8, C9. [D] may not alter any declaration from this point forward (C4).
>
> Acceptance condition: [T] must confirm receipt by responding to INVENTORY CHALLENGE with Option A or Option B. [T] may not proceed to GATE A until this acceptance is written.
>
> **[D] Signed:** [domain role selected] -- [N] states declared (S-01 through S-[N]), [N] operations declared (O-01 through O-[N]).

---

### INVENTORY CHALLENGE

**C7 applies. [T] may not proceed to GATE A without a written response below. A blank response or non-option response is a C7 violation.**

INVENTORY COMPLETE -- the STATE DECLARATIONS and OPERATION DECLARATIONS contain every state and operation in the lifecycle of {{topic}}.

**[T] response -- choose one:**

**Option A (CONFIRMED):** "[T] INVENTORY CONFIRMED. I have reviewed STATE DECLARATIONS and OPERATION DECLARATIONS against the domain lifecycle of {{topic}}. No lifecycle state or operation is absent. States: [repeat S-IDs and names]. Operations: [repeat O-IDs and names]. HANDOFF DECLARATION acknowledged. Proceeding to GATE A."

**Option B (GAP FOUND):** "[T] INVENTORY INCOMPLETE. Gap identified: [missing state or operation and why it belongs in the lifecycle]. Returning to [D] for declaration update. VOCABULARY CLOSED must be re-declared and HANDOFF DECLARATION re-signed before GATE A proceeds."

---

### GATE A

Do not begin TRANSITION TABLE until all items are confirmed. Unconfirmed = TRANSITION TABLE blocked per C6.

- [ ] STATE DECLARATIONS complete -- domain vocabulary, inline definitional clauses, at least one Terminal item
- [ ] OPERATION DECLARATIONS complete -- all S-ID references resolve to STATE DECLARATIONS
- [ ] INVARIANT DECLARATIONS complete -- at least two boolean assertions with authority sources
- [ ] VOCABULARY CLOSED declared with complete S-ID/O-ID list and forward-blocking prohibition
- [ ] HANDOFF DECLARATION signed by [D] with acceptance condition stated
- [ ] **[C7]** INVENTORY CHALLENGE resolved -- Option A or Option B written above
- [ ] **[C-14]** [T] confirms: no name will appear in TRANSITION TABLE, INVALID TRANSITIONS, or RACE CONDITIONS not declared in STATE DECLARATIONS or OPERATION DECLARATIONS
- [ ] **[C-15]** VOCABULARY CLOSED declared and forward-blocking prohibition is in effect
- [ ] **[C-09]** Terminal states identified in STATE DECLARATIONS -- at least one Terminal item will appear as From State in INVALID TRANSITIONS

**GATE A BLOCKED per C6. Do not begin TRANSITION TABLE until all items confirmed.**

---

### TRANSITION TABLE [T]

Scenario setup: [entity instance, starting state, actor, date/time context]

Constraints C1, C2, C3, C5 apply. From State and To State must use S-IDs from STATE DECLARATIONS. Operation must use O-IDs from OPERATION DECLARATIONS.

| # | From State (S-ID) | Operation (O-ID) | Preconditions | To State (S-ID) | Postconditions | INV-01 | INV-02 | Side Effects |
|---|-------------------|-----------------|---------------|-----------------|----------------|--------|--------|--------------|

- **From State / To State:** S-IDs from STATE DECLARATIONS only (C1).
- **Operation:** O-IDs from OPERATION DECLARATIONS only (C2).
- **Preconditions:** Minimum two testable assertions per row (e.g., `status == S-02`, `owner_id != null`).
- **Postconditions:** Minimum one assertion distinct from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED -- [reason]`; never blank (C5).
- **Side Effects:** Triggered rules, notifications, async jobs, record changes.

---

### GATE B

Do not begin INVALID TRANSITIONS until all items are confirmed. Unconfirmed = INVALID TRANSITIONS blocked per C8.

- [ ] **[C-08]** TRANSITION TABLE is columnar and complete; no operation documented only in prose
- [ ] **[C-05]** Every row has INV status per declared invariant; at least one VIOLATED row present
- [ ] **[C-06]** Every row has at least one postcondition distinct from the To State name
- [ ] Boundary coverage planned -- at least one terminal-state S-ID targeted for INVALID TRANSITIONS

**GATE B BLOCKED per C8. Do not begin INVALID TRANSITIONS until all items confirmed.**

---

### INVALID TRANSITIONS [T]

| # | Attempted Operation (O-ID) | From State (S-ID) | Blocking Condition | INV Reference | Risk if Bypassed |
|---|---------------------------|------------------|--------------------|--------------|-----------------|

Minimum three rows. Include at least one row where From State is a Terminal item from STATE DECLARATIONS. S-IDs and O-IDs only (C1, C2).

---

### GATE C

Do not begin RACE CONDITIONS until all items are confirmed. Unconfirmed = RACE CONDITIONS blocked per C9.

- [ ] **[C-04]** At least three (operation, state) invalid pairs named with blocking conditions; enumeration is systematic
- [ ] **[C-09]** At least one INVALID TRANSITIONS row has From State = a Terminal item from STATE DECLARATIONS

**GATE C BLOCKED per C9. Do not begin RACE CONDITIONS until all items confirmed.**

---

### RACE CONDITIONS [T]

| Operation A (O-ID) | Operation B (O-ID) | Unsafe Interleaving | Outcome | Mitigation |
|--------------------|---------------------|---------------------|---------|-----------|

If no concurrent access: "No concurrent access -- [reason]."

---

### GATE D

Do not write FINDINGS until all items are confirmed. Unconfirmed = FINDINGS blocked.

- [ ] **[C-07]** RACE CONDITIONS addressed -- at least one race scenario or explicit clearance with reason
- [ ] All TRANSITION TABLE and INVALID TRANSITIONS S-IDs and O-IDs resolve to STATE DECLARATIONS and OPERATION DECLARATIONS (C1, C2)
- [ ] Hard-stop review complete -- no section is blank or placeholder-only

**GATE D BLOCKED. Do not write FINDINGS until all items confirmed.**

---

### FINDINGS

Priority order. Reference section and item.

- **P[N]:** [title] -- [description, section/item reference]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: CONSTRAINT MATRIX, ROLES, STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, HANDOFF DECLARATION, INVENTORY CHALLENGE, GATE A, TRANSITION TABLE, GATE B, INVALID TRANSITIONS, GATE C, RACE CONDITIONS, GATE D, FINDINGS.

---

## V-02 -- C-22 + C-24 Pairwise Synthesis: HANDOFF DECLARATION + IS-Phrasing Register

**Axis:** Role sequence + phrasing register (two-axis pairwise, single-new-combination)
**Hypothesis:** C-22 (HANDOFF DECLARATION) and C-24 (IS-phrasing register) coexist. The formal transfer-of-ownership event is expressible in IS register without losing the structural specificity C-22 requires -- it can still name transferring role, receiving role, artifacts transferred, and acceptance condition, all in declarative IS register. Tabular inventories preserved (C-23 NOT targeted). Predicts 16/17 (99.41, Golden). Structural test: does IS-phrasing in the HANDOFF DECLARATION body ("OWNERSHIP IS TRANSFERRED", "vocabulary IS FROZEN", "[T] IS AUTHORIZED") satisfy C-22's pass condition while also satisfying C-24's uniform-register requirement?

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. The state machine IS governed by an ontological constraint registry in which each entry names an architectural fact about this trace. A Domain Expert [D] owns the vocabulary phase; a Trace Developer [T] owns the trace phase. [T]'s authorization IS CONTINGENT on [D] completing and signing HANDOFF DECLARATION. Read the CONSTRAINT MATRIX completely before producing any output. The matrix IS authoritative.

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
Owns: STATE REGISTRY, OPERATION REGISTRY, INVARIANT REGISTRY, VOCABULARY CLOSED, HANDOFF DECLARATION.
Binding constraint from CONSTRAINT MATRIX: **C4** (vocabulary IS FROZEN after VOCABULARY CLOSED IS declared).

**[T] Trace Developer**
Owns: INVENTORY CHALLENGE written response, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, FINDINGS.
Binding constraints from CONSTRAINT MATRIX: **C1, C2, C3, C5, C6, C7, C8, C9**.
Authorization: [T]'s authorization to begin any trace section IS CONTINGENT on HANDOFF DECLARATION being signed by [D].

---

### STATE REGISTRY [D]

| State ID | State Name | Defining Field Values | Entry Conditions | Terminal? |
|---------|-----------|----------------------|-----------------|-----------|

Domain vocabulary IS REQUIRED throughout. At least one Terminal = Yes row IS REQUIRED. Generic labels (State A, initial, final) ARE NOT VALID.

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

> **[D] HANDOFF IS DECLARED.**
>
> Transferring role IS: [D] (Domain Expert -- [auto-selected domain] expert).
> Receiving role IS: [T] (Trace Developer).
>
> Artifacts transferred ARE: STATE REGISTRY, OPERATION REGISTRY, INVARIANT REGISTRY, VOCABULARY CLOSED.
>
> Acceptance condition: [T]'s authorization IS CONTINGENT on an explicit written response to INVENTORY CHALLENGE. Option A or Option B IS REQUIRED. INVENTORY CHALLENGE IS the formal acceptance mechanism; [T] IS NOT AUTHORIZED to begin GATE A until Option A or Option B IS written.
>
> [D] IS PROHIBITED from altering any registry entry from this point forward (C4). The vocabulary IS FROZEN. [T] IS NOW AUTHORIZED to proceed to INVENTORY CHALLENGE.
>
> **[D] Signed:** [domain role selected] -- [N] states, [N] operations, [N] invariants ARE DECLARED.

---

### INVENTORY CHALLENGE

**C7 applies. INVENTORY CHALLENGE IS a required checkpoint. A blank response or non-option response IS a C7 violation.**

INVENTORY IS DECLARED COMPLETE -- the STATE REGISTRY and OPERATION REGISTRY contain every state and operation in the lifecycle of {{topic}}.

**[T] response -- one option IS REQUIRED:**

**Option A (CONFIRMED):** "[T] INVENTORY CONFIRMED. The STATE REGISTRY and OPERATION REGISTRY ARE the complete lifecycle vocabulary for {{topic}}. No lifecycle state or operation IS absent. States: [repeat complete list]. Operations: [repeat complete list]. HANDOFF DECLARATION IS ACKNOWLEDGED. Proceeding to GATE A."

**Option B (GAP FOUND):** "[T] INVENTORY INCOMPLETE. The following IS absent from the registry: [missing state or operation and why it IS required by the lifecycle]. Returning to [D] for STATE REGISTRY / OPERATION REGISTRY update. VOCABULARY CLOSED IS REQUIRED to be re-declared and HANDOFF DECLARATION IS REQUIRED to be re-signed before GATE A proceeds."

---

### GATE A

TRANSITION TABLE IS BLOCKED until all items ARE confirmed. Unconfirmed IS a C6 violation.

- [ ] STATE REGISTRY IS COMPLETE -- domain vocabulary, at least one terminal state present
- [ ] OPERATION REGISTRY IS COMPLETE -- all operations have source/target IDs from STATE REGISTRY
- [ ] INVARIANT REGISTRY IS COMPLETE -- at least two assertions with authority sources
- [ ] VOCABULARY CLOSED IS DECLARED with complete name list and forward-blocking prohibition
- [ ] HANDOFF DECLARATION IS SIGNED by [D] -- transferring role, receiving role, artifacts, and acceptance condition ARE NAMED
- [ ] **[C7]** INVENTORY CHALLENGE IS RESOLVED -- Option A or Option B IS written above
- [ ] **[C-14]** [T] CONFIRMS: no name IS PRESENT in TRANSITION TABLE, INVALID TRANSITIONS, or RACE CONDITIONS that IS NOT in STATE REGISTRY or OPERATION REGISTRY
- [ ] **[C-15]** VOCABULARY CLOSED IS DECLARED and the forward-blocking prohibition IS IN EFFECT
- [ ] **[C-09]** Terminal states ARE IDENTIFIED in STATE REGISTRY -- at least one IS TARGETED for INVALID TRANSITIONS

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
- **INV columns:** `HOLDS` or `VIOLATED -- [reason]`; blank IS a C5 violation.

---

### GATE B

INVALID TRANSITIONS IS BLOCKED until all items ARE confirmed. Unconfirmed IS a C8 violation.

- [ ] **[C-08]** TRANSITION TABLE IS COLUMNAR and COMPLETE; no operation IS documented only in prose
- [ ] **[C-05]** Every row HAS an INV status per declared invariant; at least one VIOLATED row IS PRESENT
- [ ] **[C-06]** Every row HAS at least one postcondition that IS DISTINCT from the To State name
- [ ] Boundary coverage IS PLANNED -- at least one terminal-state row IS TARGETED for INVALID TRANSITIONS

**GATE B IS BLOCKED per C8. INVALID TRANSITIONS IS NOT REACHABLE until all items ARE confirmed.**

---

### INVALID TRANSITIONS [T]

| # | Attempted Operation | From State | Blocking Condition | INV Reference | Risk if Bypassed |
|---|---------------------|-----------|--------------------|--------------|--------------------|

Minimum three rows. At least one row IS REQUIRED where From State IS a terminal state from STATE REGISTRY. All names ARE FROM STATE REGISTRY and OPERATION REGISTRY.

---

### GATE C

RACE CONDITIONS IS BLOCKED until all items ARE confirmed. Unconfirmed IS a C9 violation.

- [ ] **[C-04]** At least three (operation, state) invalid pairs ARE NAMED with blocking conditions; enumeration IS SYSTEMATIC
- [ ] **[C-09]** At least one INVALID TRANSITIONS row HAS From State that IS a terminal state from STATE REGISTRY

**GATE C IS BLOCKED per C9. RACE CONDITIONS IS NOT REACHABLE until all items ARE confirmed.**

---

### RACE CONDITIONS [T]

| Operation A | Operation B | Unsafe Interleaving | Outcome | Mitigation |
|-------------|-------------|---------------------|---------|-----------|

If no concurrent access: "No concurrent access -- [reason explaining why concurrent access IS NOT POSSIBLE]."

---

### GATE D

FINDINGS IS BLOCKED until all items ARE confirmed.

- [ ] **[C-07]** RACE CONDITIONS IS ADDRESSED -- at least one race scenario or explicit clearance with reason IS PRESENT
- [ ] All TRANSITION TABLE and INVALID TRANSITIONS names ARE FROM STATE REGISTRY and OPERATION REGISTRY (C1, C2)
- [ ] Hard-stop review IS COMPLETE -- no section IS blank or placeholder-only

**GATE D IS BLOCKED. FINDINGS IS NOT REACHABLE until all items ARE confirmed.**

---

### FINDINGS

Priority order. Reference table and row.

- **P[N]:** [title] -- [description, table/row reference]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: CONSTRAINT MATRIX, ROLES, STATE REGISTRY, OPERATION REGISTRY, INVARIANT REGISTRY, VOCABULARY CLOSED, HANDOFF DECLARATION, INVENTORY CHALLENGE, GATE A, TRANSITION TABLE, GATE B, INVALID TRANSITIONS, GATE C, RACE CONDITIONS, GATE D, FINDINGS.

---

## V-03 -- C-23 + C-24 Pairwise Synthesis: Numbered Prose Inventories + IS-Phrasing Register

**Axis:** Output format + phrasing register (two-axis pairwise, single-new-combination)
**Hypothesis:** C-23 (numbered prose inventories) and C-24 (IS-phrasing register) coexist. The IS register applies naturally within numbered prose definitional clauses -- "This state IS entered when...", "This operation IS triggered by...", "This transition IS NOT VALID when...". No HANDOFF DECLARATION section (C-22 NOT targeted); vocabulary transfer is implicit via VOCABULARY CLOSED. Predicts 16/17 (99.41, Golden). Structural test: does IS-phrasing within S-01/O-01 entries cause any friction with the prose format, or does the declarative register fit naturally into definitional clauses?

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. The state machine IS governed by an ontological constraint registry. Domain vocabulary IS DECLARED as numbered prose items; each item IS a self-contained declaration with an inline definitional clause. All transition data IS delivered in columnar tables. Read the CONSTRAINT MATRIX completely before producing any output. The matrix IS authoritative.

---

### CONSTRAINT MATRIX

| ID | Architectural Fact | Assigned Role | Concern |
|----|-------------------|---------------|---------|
| C1 | A state name IS NOT REACHABLE in any trace table unless it IS declared in STATE DECLARATIONS | [T] | vocabulary |
| C2 | An operation name IS NOT REACHABLE in any trace table unless it IS declared in OPERATION DECLARATIONS | [T] | vocabulary |
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
Owns: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED.
Binding constraint from CONSTRAINT MATRIX: **C4** (vocabulary IS FROZEN after VOCABULARY CLOSED IS declared).

**[T] Trace Developer**
Owns: INVENTORY CHALLENGE written response, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, FINDINGS.
Binding constraints from CONSTRAINT MATRIX: **C1, C2, C3, C5, C6, C7, C8, C9**.

---

### STATE DECLARATIONS [D]

Declare all lifecycle states as numbered prose items. Each item IS a self-contained declaration with an inline definitional clause. The clause IS REQUIRED to distinguish this state from all others by meaning. Generic labels ARE NOT VALID.

**S-01.** [State Name] -- This state IS entered when [entry conditions]. It IS characterized by [defining field values / attributes]. It IS [terminal / non-terminal]. Terminal: Yes/No.
**S-02.** [State Name] -- This state IS entered when [entry conditions]. [Additional inline definition distinguishing this state from S-01]. Terminal: Yes/No.
*(continue for all lifecycle states)*

At least one item IS REQUIRED to be Terminal: Yes. STATE DECLARATIONS IS NOT COMPLETE until all lifecycle states ARE declared with inline clauses.

---

### OPERATION DECLARATIONS [D]

Declare all lifecycle operations as numbered prose items. Each item IS a self-contained declaration with an inline definitional clause naming what the operation does, from which states it IS APPLICABLE, and to which state it transitions. Use S-IDs to reference STATE DECLARATIONS entries.

**O-01.** [Operation Name] -- This operation IS triggered when [conditions]. It IS APPLICABLE only from [S-N, S-N]. The target state IS [S-N]. The triggering actor IS [role/system]. From: S-[N]. To: S-[N].
**O-02.** [Operation Name] -- This operation IS triggered when [conditions]. [Additional definitional clause]. From: S-[N]. To: S-[N]. Actor IS [role/system].
*(continue for all lifecycle operations)*

OPERATION DECLARATIONS IS NOT COMPLETE until every lifecycle operation IS declared with an inline clause and From/To S-ID references.

---

### INVARIANT DECLARATIONS [D]

Declare all object-level invariants as numbered items. Each assertion IS a boolean expression. Authority source IS one of: business rule, SLA clause, regulation, or policy.

**INV-01.** [Name] -- The condition `[boolean assertion, e.g., owner_id IS NOT NULL when status IS IN {S-02, S-03}]` IS REQUIRED to hold throughout the lifecycle. Authority IS: [source].
**INV-02.** [Name] -- The condition `[boolean assertion]` IS REQUIRED to hold throughout the lifecycle. Authority IS: [source].
*(minimum two invariants)*

---

### VOCABULARY CLOSED [D]

> VOCABULARY CLOSED per C4. States: [list all S-IDs and State Names from STATE DECLARATIONS]. Operations: [list all O-IDs and Operation Names from OPERATION DECLARATIONS]. The vocabulary IS FROZEN from this point forward. Any name not listed above IS PROHIBITED in all sections that follow. This prohibition IS NOT WAIVABLE.

---

### INVENTORY CHALLENGE

**C7 applies. INVENTORY CHALLENGE IS a required checkpoint. A blank response or non-option response IS a C7 violation.**

INVENTORY IS DECLARED COMPLETE -- the STATE DECLARATIONS and OPERATION DECLARATIONS contain every state and operation in the lifecycle of {{topic}}.

**[T] response -- one option IS REQUIRED:**

**Option A (CONFIRMED):** "[T] INVENTORY CONFIRMED. The STATE DECLARATIONS and OPERATION DECLARATIONS ARE the complete lifecycle vocabulary for {{topic}}. No lifecycle state or operation IS absent. States: [repeat S-IDs and names]. Operations: [repeat O-IDs and names]. Challenge IS RESOLVED. Proceeding to GATE A."

**Option B (GAP FOUND):** "[T] INVENTORY INCOMPLETE. The following IS absent from declarations: [missing item and why it IS required by the lifecycle]. Returning to [D] for declaration update. VOCABULARY CLOSED IS REQUIRED to be re-declared before GATE A proceeds."

---

### GATE A

TRANSITION TABLE IS BLOCKED until all items ARE confirmed. Unconfirmed IS a C6 violation.

- [ ] STATE DECLARATIONS IS COMPLETE -- domain vocabulary, inline definitional clauses, at least one Terminal item
- [ ] OPERATION DECLARATIONS IS COMPLETE -- all S-ID references resolve to STATE DECLARATIONS
- [ ] INVARIANT DECLARATIONS IS COMPLETE -- at least two boolean assertions with authority sources
- [ ] VOCABULARY CLOSED IS DECLARED with complete S-ID/O-ID list and forward-blocking prohibition
- [ ] **[C7]** INVENTORY CHALLENGE IS RESOLVED -- Option A or Option B IS written above
- [ ] **[C-14]** [T] CONFIRMS: no name IS PRESENT in TRANSITION TABLE, INVALID TRANSITIONS, or RACE CONDITIONS that IS NOT in STATE DECLARATIONS or OPERATION DECLARATIONS
- [ ] **[C-15]** VOCABULARY CLOSED IS DECLARED and the forward-blocking prohibition IS IN EFFECT
- [ ] **[C-09]** Terminal states ARE IDENTIFIED in STATE DECLARATIONS -- at least one IS TARGETED for INVALID TRANSITIONS

**GATE A IS BLOCKED per C6. TRANSITION TABLE IS NOT REACHABLE until all items ARE confirmed.**

---

### TRANSITION TABLE [T]

Scenario setup: [entity instance, starting state, actor, date/time context]

C1, C2, C3, C5 ARE IN EFFECT.

| # | From State (S-ID) | Operation (O-ID) | Preconditions | To State (S-ID) | Postconditions | INV-01 | INV-02 | Side Effects |
|---|-------------------|-----------------|---------------|-----------------|----------------|--------|--------|--------------|

- **From State / To State:** S-IDs from STATE DECLARATIONS IS REQUIRED; unlisted names ARE violations (C1).
- **Operation:** O-IDs from OPERATION DECLARATIONS IS REQUIRED; unlisted names ARE violations (C2).
- **Preconditions:** Minimum two testable assertions per row.
- **Postconditions:** Minimum one assertion that IS DISTINCT from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED -- [reason]`; blank IS a C5 violation.

---

### GATE B

INVALID TRANSITIONS IS BLOCKED until all items ARE confirmed. Unconfirmed IS a C8 violation.

- [ ] **[C-08]** TRANSITION TABLE IS COLUMNAR and COMPLETE; no operation IS documented only in prose
- [ ] **[C-05]** Every row HAS an INV status per declared invariant; at least one VIOLATED row IS PRESENT
- [ ] **[C-06]** Every row HAS at least one postcondition that IS DISTINCT from the To State name
- [ ] Boundary coverage IS PLANNED -- at least one terminal-state S-ID IS TARGETED for INVALID TRANSITIONS

**GATE B IS BLOCKED per C8. INVALID TRANSITIONS IS NOT REACHABLE until all items ARE confirmed.**

---

### INVALID TRANSITIONS [T]

| # | Attempted Operation (O-ID) | From State (S-ID) | Blocking Condition | INV Reference | Risk if Bypassed |
|---|---------------------------|------------------|--------------------|--------------|-----------------|

Minimum three rows. At least one row IS REQUIRED where From State IS a Terminal item from STATE DECLARATIONS. S-IDs and O-IDs IS REQUIRED in all name cells.

---

### GATE C

RACE CONDITIONS IS BLOCKED until all items ARE confirmed. Unconfirmed IS a C9 violation.

- [ ] **[C-04]** At least three (operation, state) invalid pairs ARE NAMED with blocking conditions; enumeration IS SYSTEMATIC
- [ ] **[C-09]** At least one INVALID TRANSITIONS row HAS From State that IS a Terminal item from STATE DECLARATIONS

**GATE C IS BLOCKED per C9. RACE CONDITIONS IS NOT REACHABLE until all items ARE confirmed.**

---

### RACE CONDITIONS [T]

| Operation A (O-ID) | Operation B (O-ID) | Unsafe Interleaving | Outcome | Mitigation |
|--------------------|---------------------|---------------------|---------|-----------|

If no concurrent access: "No concurrent access -- [reason explaining why concurrent access IS NOT POSSIBLE]."

---

### GATE D

FINDINGS IS BLOCKED until all items ARE confirmed.

- [ ] **[C-07]** RACE CONDITIONS IS ADDRESSED -- at least one race scenario or explicit clearance with reason IS PRESENT
- [ ] All TRANSITION TABLE and INVALID TRANSITIONS S-IDs and O-IDs ARE FROM STATE DECLARATIONS and OPERATION DECLARATIONS (C1, C2)
- [ ] Hard-stop review IS COMPLETE -- no section IS blank or placeholder-only

**GATE D IS BLOCKED. FINDINGS IS NOT REACHABLE until all items ARE confirmed.**

---

### FINDINGS

Priority order. Reference section and item.

- **P[N]:** [title] -- [description, section/item reference]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: CONSTRAINT MATRIX, ROLES, STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, INVENTORY CHALLENGE, GATE A, TRANSITION TABLE, GATE B, INVALID TRANSITIONS, GATE C, RACE CONDITIONS, GATE D, FINDINGS.

---

## V-04 -- Full Synthesis: C-22 + C-23 + C-24

**Axis:** All three R9 innovations combined (synthesis target)
**Hypothesis:** All three R9 innovations are simultaneously compatible. The IS register applies naturally in the HANDOFF DECLARATION body ("OWNERSHIP IS TRANSFERRED", "[T] IS AUTHORIZED", "[D] IS PROHIBITED"). Numbered prose inventories work with IS-phrasing within their definitional clauses ("This state IS entered when..."). The HANDOFF DECLARATION references prose-declared artifacts by ID (S-01 through S-N, O-01 through O-N), making the transfer concrete without depending on table structure. This is the first variant predicted to achieve all 17 aspirational criteria simultaneously. Predicted: 17/17 = 100.00 -- the new ceiling.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. Domain vocabulary IS DECLARED by a Domain Expert [D] as numbered prose items -- each item IS a self-contained declaration with an inline definitional clause. A Trace Developer [T] executes the trace using only declared vocabulary. [T]'s authorization IS CONTINGENT on [D] completing VOCABULARY CLOSED and signing HANDOFF DECLARATION. The state machine IS governed by an ontological constraint registry; each entry names an architectural fact about this trace. Read the CONSTRAINT MATRIX completely before producing any output. The matrix IS authoritative.

---

### CONSTRAINT MATRIX

| ID | Architectural Fact | Assigned Role | Concern |
|----|-------------------|---------------|---------|
| C1 | A state name IS NOT REACHABLE in any trace table unless it IS declared in STATE DECLARATIONS | [T] | vocabulary |
| C2 | An operation name IS NOT REACHABLE in any trace table unless it IS declared in OPERATION DECLARATIONS | [T] | vocabulary |
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
Owns: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, HANDOFF DECLARATION.
Binding constraint from CONSTRAINT MATRIX: **C4** (vocabulary IS FROZEN after VOCABULARY CLOSED IS declared).

**[T] Trace Developer**
Owns: INVENTORY CHALLENGE written response, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, FINDINGS.
Binding constraints from CONSTRAINT MATRIX: **C1, C2, C3, C5, C6, C7, C8, C9**.
Authorization: [T]'s authorization to begin any trace section IS CONTINGENT on HANDOFF DECLARATION being signed by [D].

---

### STATE DECLARATIONS [D]

Declare all lifecycle states as numbered prose items. Each item IS a self-contained declaration with an inline definitional clause. The clause IS REQUIRED to distinguish this state from all others by meaning -- what conditions cause entry, what field values characterize it, and whether it IS terminal. Generic labels ARE NOT VALID.

**S-01.** [State Name] -- This state IS entered when [entry conditions]. It IS characterized by [defining field values / attributes]. It IS [terminal / the origin of transitions to S-N and S-N]. Terminal: Yes/No.
**S-02.** [State Name] -- This state IS entered when [entry conditions]. [Additional definitional clause distinguishing this state from S-01]. Terminal: Yes/No.
*(continue for all lifecycle states)*

At least one item IS REQUIRED to be Terminal: Yes. STATE DECLARATIONS IS NOT COMPLETE until every lifecycle state IS declared with an inline clause. STATE DECLARATIONS IS NOT COMPLETE if any generic label IS present.

---

### OPERATION DECLARATIONS [D]

Declare all lifecycle operations as numbered prose items. Each item IS a self-contained declaration with an inline definitional clause naming what the operation does, from which states it IS APPLICABLE, and to which state it transitions. All S-IDs IS REQUIRED to reference STATE DECLARATIONS entries.

**O-01.** [Operation Name] -- This operation IS triggered when [conditions]. It IS APPLICABLE only from [S-N, S-N]. The target state IS [S-N]. The triggering actor IS [role/system]. From: S-[N]. To: S-[N].
**O-02.** [Operation Name] -- This operation IS triggered when [conditions]. [Additional definitional clause]. From: S-[N]. To: S-[N]. Actor IS [role/system].
*(continue for all lifecycle operations)*

OPERATION DECLARATIONS IS NOT COMPLETE until every lifecycle operation IS declared with an inline clause and From/To S-ID references.

---

### INVARIANT DECLARATIONS [D]

Declare all object-level invariants as numbered items. Each assertion IS a boolean expression. Authority source IS one of: business rule, SLA clause, regulation, or policy.

**INV-01.** [Name] -- The condition `[boolean assertion, e.g., owner_id IS NOT NULL when status IS IN {S-02, S-03}]` IS REQUIRED to hold throughout the lifecycle. Authority IS: [source].
**INV-02.** [Name] -- The condition `[boolean assertion]` IS REQUIRED to hold throughout the lifecycle. Authority IS: [source].
*(minimum two invariants)*

---

### VOCABULARY CLOSED [D]

> VOCABULARY CLOSED per C4. States: [list all S-IDs and State Names from STATE DECLARATIONS]. Operations: [list all O-IDs and Operation Names from OPERATION DECLARATIONS]. The vocabulary IS FROZEN from this point forward. Any name not listed above IS PROHIBITED in all sections that follow. This prohibition IS NOT WAIVABLE.

---

### HANDOFF DECLARATION [D]

> **[D] HANDOFF IS DECLARED.**
>
> Transferring role IS: [D] (Domain Expert -- [auto-selected domain] expert).
> Receiving role IS: [T] (Trace Developer).
>
> Artifacts transferred ARE: STATE DECLARATIONS (S-01 through S-[N]), OPERATION DECLARATIONS (O-01 through O-[N]), INVARIANT DECLARATIONS (INV-01 through INV-[N]), VOCABULARY CLOSED.
>
> Acceptance condition: [T]'s authorization IS CONTINGENT on a written response to INVENTORY CHALLENGE. Option A or Option B IS REQUIRED. INVENTORY CHALLENGE IS the formal acceptance mechanism; [T] IS NOT AUTHORIZED to begin GATE A until Option A or Option B IS written.
>
> [D] IS PROHIBITED from altering any declaration from this point forward (C4). The vocabulary IS FROZEN. [T] IS NOW AUTHORIZED to proceed to INVENTORY CHALLENGE.
>
> **[D] Signed:** [domain role selected] -- [N] states ARE DECLARED (S-01 through S-[N]), [N] operations ARE DECLARED (O-01 through O-[N]).

---

### INVENTORY CHALLENGE

**C7 applies. INVENTORY CHALLENGE IS a required checkpoint. A blank response or non-option response IS a C7 violation.**

INVENTORY IS DECLARED COMPLETE -- the STATE DECLARATIONS (S-01 through S-[N]) and OPERATION DECLARATIONS (O-01 through O-[N]) contain every state and operation in the lifecycle of {{topic}}.

**[T] response -- one option IS REQUIRED:**

**Option A (CONFIRMED):** "[T] INVENTORY CONFIRMED. The STATE DECLARATIONS and OPERATION DECLARATIONS ARE the complete lifecycle vocabulary for {{topic}}. No lifecycle state or operation IS absent. States: [repeat S-IDs and names]. Operations: [repeat O-IDs and names]. HANDOFF DECLARATION IS ACKNOWLEDGED. Proceeding to GATE A."

**Option B (GAP FOUND):** "[T] INVENTORY INCOMPLETE. The following IS absent from declarations: [missing item and why it IS required by the lifecycle]. Returning to [D] for declaration update. VOCABULARY CLOSED IS REQUIRED to be re-declared and HANDOFF DECLARATION IS REQUIRED to be re-signed before GATE A proceeds."

---

### GATE A

TRANSITION TABLE IS BLOCKED until all items ARE confirmed. Unconfirmed IS a C6 violation.

- [ ] STATE DECLARATIONS IS COMPLETE -- domain vocabulary, inline definitional clauses, at least one Terminal item
- [ ] OPERATION DECLARATIONS IS COMPLETE -- all S-ID references resolve to STATE DECLARATIONS
- [ ] INVARIANT DECLARATIONS IS COMPLETE -- at least two boolean assertions with authority sources
- [ ] VOCABULARY CLOSED IS DECLARED with complete S-ID/O-ID list and forward-blocking prohibition
- [ ] HANDOFF DECLARATION IS SIGNED by [D] -- transferring role, receiving role, artifacts, and acceptance condition ARE NAMED
- [ ] **[C7]** INVENTORY CHALLENGE IS RESOLVED -- Option A or Option B IS written above
- [ ] **[C-14]** [T] CONFIRMS: no name IS PRESENT in TRANSITION TABLE, INVALID TRANSITIONS, or RACE CONDITIONS that IS NOT in STATE DECLARATIONS or OPERATION DECLARATIONS
- [ ] **[C-15]** VOCABULARY CLOSED IS DECLARED and the forward-blocking prohibition IS IN EFFECT
- [ ] **[C-09]** Terminal states ARE IDENTIFIED -- at least one IS TARGETED for INVALID TRANSITIONS

**GATE A IS BLOCKED per C6. TRANSITION TABLE IS NOT REACHABLE until all items ARE confirmed.**

---

### TRANSITION TABLE [T]

Scenario setup: [entity instance, starting state, actor, date/time context]

C1, C2, C3, C5 ARE IN EFFECT.

| # | From State (S-ID) | Operation (O-ID) | Preconditions | To State (S-ID) | Postconditions | INV-01 | INV-02 | Side Effects |
|---|-------------------|-----------------|---------------|-----------------|----------------|--------|--------|--------------|

- **From State / To State:** S-IDs from STATE DECLARATIONS IS REQUIRED; unlisted names ARE violations (C1).
- **Operation:** O-IDs from OPERATION DECLARATIONS IS REQUIRED; unlisted names ARE violations (C2).
- **Preconditions:** Minimum two testable assertions per row.
- **Postconditions:** Minimum one assertion that IS DISTINCT from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED -- [reason]`; blank IS a C5 violation.
- **Side Effects:** Triggered rules, notifications, async jobs, record changes.

---

### GATE B

INVALID TRANSITIONS IS BLOCKED until all items ARE confirmed. Unconfirmed IS a C8 violation.

- [ ] **[C-08]** TRANSITION TABLE IS COLUMNAR and COMPLETE; no operation IS documented only in prose
- [ ] **[C-05]** Every row HAS an INV status per declared invariant; at least one VIOLATED row IS PRESENT
- [ ] **[C-06]** Every row HAS at least one postcondition that IS DISTINCT from the To State name
- [ ] Boundary coverage IS PLANNED -- at least one terminal-state S-ID IS TARGETED for INVALID TRANSITIONS

**GATE B IS BLOCKED per C8. INVALID TRANSITIONS IS NOT REACHABLE until all items ARE confirmed.**

---

### INVALID TRANSITIONS [T]

| # | Attempted Operation (O-ID) | From State (S-ID) | Blocking Condition | INV Reference | Risk if Bypassed |
|---|---------------------------|------------------|--------------------|--------------|-----------------|

Minimum three rows. At least one row IS REQUIRED where From State IS a Terminal item from STATE DECLARATIONS. S-IDs and O-IDs IS REQUIRED in all name cells.

---

### GATE C

RACE CONDITIONS IS BLOCKED until all items ARE confirmed. Unconfirmed IS a C9 violation.

- [ ] **[C-04]** At least three (operation, state) invalid pairs ARE NAMED with blocking conditions; enumeration IS SYSTEMATIC
- [ ] **[C-09]** At least one INVALID TRANSITIONS row HAS From State that IS a Terminal item from STATE DECLARATIONS

**GATE C IS BLOCKED per C9. RACE CONDITIONS IS NOT REACHABLE until all items ARE confirmed.**

---

### RACE CONDITIONS [T]

| Operation A (O-ID) | Operation B (O-ID) | Unsafe Interleaving | Outcome | Mitigation |
|--------------------|---------------------|---------------------|---------|-----------|

If no concurrent access: "No concurrent access -- [reason explaining why concurrent access IS NOT POSSIBLE]."

---

### GATE D

FINDINGS IS BLOCKED until all items ARE confirmed.

- [ ] **[C-07]** RACE CONDITIONS IS ADDRESSED -- at least one race scenario or explicit clearance with reason IS PRESENT
- [ ] All TRANSITION TABLE and INVALID TRANSITIONS S-IDs and O-IDs ARE FROM STATE DECLARATIONS and OPERATION DECLARATIONS (C1, C2)
- [ ] Hard-stop review IS COMPLETE -- no section IS blank or placeholder-only

**GATE D IS BLOCKED. FINDINGS IS NOT REACHABLE until all items ARE confirmed.**

---

### FINDINGS

Priority order. Reference section and item.

- **P[N]:** [title] -- [description, section/item reference]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: CONSTRAINT MATRIX, ROLES, STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, HANDOFF DECLARATION, INVENTORY CHALLENGE, GATE A, TRANSITION TABLE, GATE B, INVALID TRANSITIONS, GATE C, RACE CONDITIONS, GATE D, FINDINGS.

---

## V-05 -- Full Synthesis + Inertia Framing

**Axis:** V-04 synthesis + inertia framing (new axis, C-25 exploration)
**Hypothesis:** V-04 achieves 17/17 (100.00) under v8. V-05 adds an INERTIA BASELINE section at the top of the document -- before the CONSTRAINT MATRIX -- that names the status-quo approach being displaced, the failure mode under the current approach, and an explicit assertion that this trace-state artifact IS the replacement. Under v8, V-05 predicts 17/17 (100.00) because INERTIA BASELINE is additive, not substitutive. The inertia framing may seed C-25: a named INERTIA BASELINE section identifies the status-quo alternative, names the current approach's failure mode, and asserts why the trace-state artifact IS the replacement.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. Domain vocabulary IS DECLARED by a Domain Expert [D] as numbered prose items -- each item IS a self-contained declaration with an inline definitional clause. A Trace Developer [T] executes the trace using only declared vocabulary. [T]'s authorization IS CONTINGENT on [D] completing VOCABULARY CLOSED and signing HANDOFF DECLARATION. The state machine IS governed by an ontological constraint registry. Read INERTIA BASELINE and CONSTRAINT MATRIX completely before producing any output.

---

### INERTIA BASELINE

This section IS NOT PART OF THE TRACE. It IS the description of the current approach being replaced by this signal.

**Current approach IS:** [describe the status-quo -- e.g., state transitions are reviewed by reading code directly, precondition checks are ad-hoc field guards written from developer memory, the lifecycle has no single authoritative document].

**The failure mode under the current approach IS:** [name the specific risk -- e.g., invalid transitions are discovered only in production; missing precondition checks allow objects to reach illegal states; invariant violations accumulate silently; race conditions appear only under load].

**This trace-state artifact IS the replacement.** It IS a systematic, reviewable record of every state, every operation, every precondition, every invariant, and every invalid transition in the lifecycle of {{topic}}. The replacement IS operative when FINDINGS IS produced and the artifact IS written to disk.

---

### CONSTRAINT MATRIX

| ID | Architectural Fact | Assigned Role | Concern |
|----|-------------------|---------------|---------|
| C1 | A state name IS NOT REACHABLE in any trace table unless it IS declared in STATE DECLARATIONS | [T] | vocabulary |
| C2 | An operation name IS NOT REACHABLE in any trace table unless it IS declared in OPERATION DECLARATIONS | [T] | vocabulary |
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
Owns: INERTIA BASELINE completion, STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, HANDOFF DECLARATION.
Binding constraint from CONSTRAINT MATRIX: **C4** (vocabulary IS FROZEN after VOCABULARY CLOSED IS declared).

**[T] Trace Developer**
Owns: INVENTORY CHALLENGE written response, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, FINDINGS.
Binding constraints from CONSTRAINT MATRIX: **C1, C2, C3, C5, C6, C7, C8, C9**.
Authorization: [T]'s authorization IS CONTINGENT on HANDOFF DECLARATION being signed by [D].

---

### STATE DECLARATIONS [D]

Declare all lifecycle states as numbered prose items. Each item IS a self-contained declaration with an inline definitional clause. The clause IS REQUIRED to distinguish this state from all others by meaning. Generic labels ARE NOT VALID.

**S-01.** [State Name] -- This state IS entered when [entry conditions]. It IS characterized by [defining field values / attributes]. It IS [terminal / the origin of transitions to S-N]. Terminal: Yes/No.
**S-02.** [State Name] -- This state IS entered when [entry conditions]. [Additional definitional clause distinguishing this state from S-01]. Terminal: Yes/No.
*(continue for all lifecycle states)*

At least one item IS REQUIRED to be Terminal: Yes. STATE DECLARATIONS IS NOT COMPLETE until every lifecycle state IS declared with an inline definitional clause.

---

### OPERATION DECLARATIONS [D]

Declare all lifecycle operations as numbered prose items. Each item IS a self-contained declaration with an inline definitional clause. All S-IDs IS REQUIRED to reference STATE DECLARATIONS entries.

**O-01.** [Operation Name] -- This operation IS triggered when [conditions]. It IS APPLICABLE only from [S-N, S-N]. The target state IS [S-N]. The triggering actor IS [role/system]. From: S-[N]. To: S-[N].
**O-02.** [Operation Name] -- This operation IS triggered when [conditions]. [Additional definitional clause]. From: S-[N]. To: S-[N]. Actor IS [role/system].
*(continue for all lifecycle operations)*

OPERATION DECLARATIONS IS NOT COMPLETE until every lifecycle operation IS declared with an inline clause and From/To S-ID references.

---

### INVARIANT DECLARATIONS [D]

Declare all object-level invariants as numbered items. Each assertion IS a boolean expression. Authority source IS one of: business rule, SLA clause, regulation, or policy.

**INV-01.** [Name] -- The condition `[boolean assertion]` IS REQUIRED to hold throughout the lifecycle. Authority IS: [source].
**INV-02.** [Name] -- The condition `[boolean assertion]` IS REQUIRED to hold throughout the lifecycle. Authority IS: [source].
*(minimum two invariants)*

---

### VOCABULARY CLOSED [D]

> VOCABULARY CLOSED per C4. States: [list all S-IDs and State Names from STATE DECLARATIONS]. Operations: [list all O-IDs and Operation Names from OPERATION DECLARATIONS]. The vocabulary IS FROZEN from this point forward. Any name not listed above IS PROHIBITED in all sections that follow. This prohibition IS NOT WAIVABLE.

---

### HANDOFF DECLARATION [D]

> **[D] HANDOFF IS DECLARED.**
>
> Transferring role IS: [D] (Domain Expert -- [auto-selected domain] expert).
> Receiving role IS: [T] (Trace Developer).
>
> Artifacts transferred ARE: STATE DECLARATIONS (S-01 through S-[N]), OPERATION DECLARATIONS (O-01 through O-[N]), INVARIANT DECLARATIONS (INV-01 through INV-[N]), VOCABULARY CLOSED.
>
> These artifacts ARE the complete replacement for the status-quo approach described in INERTIA BASELINE. The replacement IS operative when [T] completes TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, and FINDINGS.
>
> Acceptance condition: [T]'s authorization IS CONTINGENT on a written response to INVENTORY CHALLENGE. Option A or Option B IS REQUIRED. [T] IS NOT AUTHORIZED to begin GATE A until Option A or Option B IS written.
>
> [D] IS PROHIBITED from altering any declaration from this point forward (C4). The vocabulary IS FROZEN. [T] IS NOW AUTHORIZED to proceed to INVENTORY CHALLENGE.
>
> **[D] Signed:** [domain role selected] -- [N] states ARE DECLARED (S-01 through S-[N]), [N] operations ARE DECLARED (O-01 through O-[N]).

---

### INVENTORY CHALLENGE

**C7 applies. INVENTORY CHALLENGE IS a required checkpoint. A blank response or non-option response IS a C7 violation.**

INVENTORY IS DECLARED COMPLETE -- the STATE DECLARATIONS (S-01 through S-[N]) and OPERATION DECLARATIONS (O-01 through O-[N]) contain every state and operation in the lifecycle of {{topic}}.

**[T] response -- one option IS REQUIRED:**

**Option A (CONFIRMED):** "[T] INVENTORY CONFIRMED. The STATE DECLARATIONS and OPERATION DECLARATIONS ARE the complete lifecycle vocabulary for {{topic}}. No lifecycle state or operation IS absent. States: [repeat S-IDs and names]. Operations: [repeat O-IDs and names]. HANDOFF DECLARATION IS ACKNOWLEDGED. Proceeding to GATE A."

**Option B (GAP FOUND):** "[T] INVENTORY INCOMPLETE. The following IS absent from declarations: [missing item and why it IS required by the lifecycle]. Returning to [D] for declaration update. VOCABULARY CLOSED IS REQUIRED to be re-declared and HANDOFF DECLARATION IS REQUIRED to be re-signed before GATE A proceeds."

---

### GATE A

TRANSITION TABLE IS BLOCKED until all items ARE confirmed. Unconfirmed IS a C6 violation.

- [ ] INERTIA BASELINE IS COMPLETE -- current approach, failure mode, and replacement assertion ARE present
- [ ] STATE DECLARATIONS IS COMPLETE -- domain vocabulary, inline definitional clauses, at least one Terminal item
- [ ] OPERATION DECLARATIONS IS COMPLETE -- all S-ID references resolve to STATE DECLARATIONS
- [ ] INVARIANT DECLARATIONS IS COMPLETE -- at least two boolean assertions with authority sources
- [ ] VOCABULARY CLOSED IS DECLARED with complete S-ID/O-ID list and forward-blocking prohibition
- [ ] HANDOFF DECLARATION IS SIGNED by [D] -- transferring role, receiving role, artifacts, and acceptance condition ARE NAMED
- [ ] **[C7]** INVENTORY CHALLENGE IS RESOLVED -- Option A or Option B IS written above
- [ ] **[C-14]** [T] CONFIRMS: no name IS PRESENT in TRANSITION TABLE, INVALID TRANSITIONS, or RACE CONDITIONS that IS NOT in STATE DECLARATIONS or OPERATION DECLARATIONS
- [ ] **[C-15]** VOCABULARY CLOSED IS DECLARED and the forward-blocking prohibition IS IN EFFECT
- [ ] **[C-09]** Terminal states ARE IDENTIFIED -- at least one IS TARGETED for INVALID TRANSITIONS

**GATE A IS BLOCKED per C6. TRANSITION TABLE IS NOT REACHABLE until all items ARE confirmed.**

---

### TRANSITION TABLE [T]

Scenario setup: [entity instance, starting state, actor, date/time context]

C1, C2, C3, C5 ARE IN EFFECT.

| # | From State (S-ID) | Operation (O-ID) | Preconditions | To State (S-ID) | Postconditions | INV-01 | INV-02 | Side Effects |
|---|-------------------|-----------------|---------------|-----------------|----------------|--------|--------|--------------|

- **From State / To State:** S-IDs from STATE DECLARATIONS IS REQUIRED; unlisted names ARE violations (C1).
- **Operation:** O-IDs from OPERATION DECLARATIONS IS REQUIRED; unlisted names ARE violations (C2).
- **Preconditions:** Minimum two testable assertions per row.
- **Postconditions:** Minimum one assertion that IS DISTINCT from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED -- [reason]`; blank IS a C5 violation.
- **Side Effects:** Triggered rules, notifications, async jobs, record changes.

---

### GATE B

INVALID TRANSITIONS IS BLOCKED until all items ARE confirmed. Unconfirmed IS a C8 violation.

- [ ] **[C-08]** TRANSITION TABLE IS COLUMNAR and COMPLETE; no operation IS documented only in prose
- [ ] **[C-05]** Every row HAS an INV status per declared invariant; at least one VIOLATED row IS PRESENT
- [ ] **[C-06]** Every row HAS at least one postcondition that IS DISTINCT from the To State name
- [ ] Boundary coverage IS PLANNED -- at least one terminal-state S-ID IS TARGETED for INVALID TRANSITIONS

**GATE B IS BLOCKED per C8. INVALID TRANSITIONS IS NOT REACHABLE until all items ARE confirmed.**

---

### INVALID TRANSITIONS [T]

| # | Attempted Operation (O-ID) | From State (S-ID) | Blocking Condition | INV Reference | Risk if Bypassed |
|---|---------------------------|------------------|--------------------|--------------|-----------------|

Minimum three rows. At least one row IS REQUIRED where From State IS a Terminal item from STATE DECLARATIONS. S-IDs and O-IDs IS REQUIRED in all name cells.

---

### GATE C

RACE CONDITIONS IS BLOCKED until all items ARE confirmed. Unconfirmed IS a C9 violation.

- [ ] **[C-04]** At least three (operation, state) invalid pairs ARE NAMED with blocking conditions; enumeration IS SYSTEMATIC
- [ ] **[C-09]** At least one INVALID TRANSITIONS row HAS From State that IS a Terminal item from STATE DECLARATIONS

**GATE C IS BLOCKED per C9. RACE CONDITIONS IS NOT REACHABLE until all items ARE confirmed.**

---

### RACE CONDITIONS [T]

| Operation A (O-ID) | Operation B (O-ID) | Unsafe Interleaving | Outcome | Mitigation |
|--------------------|---------------------|---------------------|---------|-----------|

If no concurrent access: "No concurrent access -- [reason explaining why concurrent access IS NOT POSSIBLE]."

---

### GATE D

FINDINGS IS BLOCKED until all items ARE confirmed.

- [ ] **[C-07]** RACE CONDITIONS IS ADDRESSED -- at least one race scenario or explicit clearance with reason IS PRESENT
- [ ] All TRANSITION TABLE and INVALID TRANSITIONS S-IDs and O-IDs ARE FROM STATE DECLARATIONS and OPERATION DECLARATIONS (C1, C2)
- [ ] Hard-stop review IS COMPLETE -- no section IS blank or placeholder-only

**GATE D IS BLOCKED. FINDINGS IS NOT REACHABLE until all items ARE confirmed.**

---

### FINDINGS

Priority order. Reference section and item.

- **P[N]:** [title] -- [description, section/item reference]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: INERTIA BASELINE, CONSTRAINT MATRIX, ROLES, STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, HANDOFF DECLARATION, INVENTORY CHALLENGE, GATE A, TRANSITION TABLE, GATE B, INVALID TRANSITIONS, GATE C, RACE CONDITIONS, GATE D, FINDINGS.

---

## Scoring Predictions (v8)

| Variant | C-22 | C-23 | C-24 | Aspirational | Composite | Status |
|---------|------|------|------|-------------|-----------|--------|
| V-01 | PASS | PASS | FAIL | 16/17 x 10 = 9.41 | 99.41 | Golden |
| V-02 | PASS | FAIL | PASS | 16/17 x 10 = 9.41 | 99.41 | Golden |
| V-03 | FAIL | PASS | PASS | 16/17 x 10 = 9.41 | 99.41 | Golden |
| V-04 | PASS | PASS | PASS | 17/17 x 10 = 10.00 | 100.00 | Golden ceiling |
| V-05 | PASS | PASS | PASS | 17/17 x 10 = 10.00 | 100.00 | Golden ceiling |

**V-04 and V-05 are the first variants predicted to achieve 100.00.**

V-05's INERTIA BASELINE is additive and does not displace any existing criterion. It does not interfere with C-22/C-23/C-24. Under v8 it scores identically to V-04.

### C-25 candidate (seeded by V-05)

**Name:** Explicit inertia declaration
**Mechanism:** A named INERTIA BASELINE section (or equivalently named block) appears before the CONSTRAINT MATRIX. It names: (a) the current approach being replaced, (b) the failure mode under the current approach, and (c) an explicit assertion that this trace-state artifact IS the replacement. The section IS NOT PART OF THE TRACE -- it IS context for why the trace exists. This makes the analytical value of the trace explicit at the outset rather than implicit in the artifact's existence.
**Pass condition:** An INERTIA BASELINE section (or equivalent) is present before CONSTRAINT MATRIX. It names the current approach, names a specific failure mode, and contains an explicit "this artifact IS the replacement" assertion. A section that merely describes the domain without naming the status-quo alternative and its failure mode does not satisfy this criterion.
