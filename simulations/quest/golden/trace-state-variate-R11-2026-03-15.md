# trace-state Variate — Round 11
**Date:** 2026-03-15
**Rubric:** v9 (C-01..C-26; 19 aspirational criteria; golden: all essential pass AND composite >= 80)
**Situation:** R10 closed three new aspirational criteria extracted from pairwise experiments: C-25 (vocabulary-locked handoff gate, from V-01) and C-26 (post-handoff role-state transition declaration, from V-02). R10 V-01 and V-02 each score 17/19 (98.95, Golden) under v9; R10 V-03 scores 15/19 (97.89, Excellent). No R10 variant achieves 19/19. The ceiling is 100.00.

R10 independence structure:

| Criterion | R10 V-01 | R10 V-02 | R10 V-03 |
|-----------|----------|----------|----------|
| C-22 (HANDOFF DECLARATION) | PASS | PASS | FAIL |
| C-23 (numbered prose inventories) | PASS | FAIL | PASS |
| C-24 (IS-phrasing register) | FAIL | PASS | PASS |
| C-25 (vocabulary-locked handoff gate) | PASS | FAIL | FAIL |
| C-26 (post-handoff role-state flip) | FAIL | PASS | FAIL |

The synthesis path: V-01 contributes C-22+C-23+C-25; V-02 contributes C-22+C-24+C-26. The gap is mutual exclusion between C-24 and C-23 (V-01 has prose inventories with imperative register; V-02 has tabular inventories with IS-register) and between C-25 and C-26 (V-01 has vocabulary gate without state flip; V-02 has state flip without vocabulary gate).

**R11 objective:** Resolve the four-way mutual exclusion. Three single-axis probes isolate the key structural tensions; two combination variants attempt the 19/19 synthesis.

---

## Round 10 Results Under v9 (Basis for R11)

| Variant | C-22 | C-23 | C-24 | C-25 | C-26 | Aspirational (v9) | Composite | Tier |
|---------|------|------|------|------|------|-------------------|-----------|------|
| R10 V-01 | PASS | PASS | FAIL | PASS | FAIL | 17/19 = 8.95 | 98.95 | Golden |
| R10 V-02 | PASS | FAIL | PASS | FAIL | PASS | 17/19 = 8.95 | 98.95 | Golden |
| R10 V-03 | FAIL | PASS | PASS | FAIL | FAIL | 15/19 = 7.89 | 97.89 | Excellent |

No variant achieves 100.00. C-23+C-24 have not coexisted with C-22+C-25+C-26 in any single variant.

---

## Round 11 Variation Map

| Var | Axis | Hypothesis | New Criteria | Predicted |
|-----|------|------------|--------------|-----------|
| V-01 | IS-register conversion (phrasing register) | Converting V-01 base imperative to IS-declarative throughout gains C-24 without disturbing C-22, C-23, C-25; C-26 absent | +C-24 | 18/19 = 98.95 |
| V-02 | Post-handoff role-state flip (lifecycle emphasis) | Adding explicit [D]+[T] state declarations to HANDOFF DECLARATION gains C-26 while keeping V-01 imperative register intact; C-24 absent | +C-26 | 18/19 = 98.95 |
| V-03 | C-24 + C-26 pairwise on V-01 base | Both IS-register and role-state flip can be applied to V-01 base simultaneously; C-23 and C-25 preserved; all five new criteria present | +C-24, +C-26 | 19/19 = 100.00 |
| V-04 | Full synthesis, Finance domain | Fresh variant designed for all 19 criteria; tests domain independence of the synthesis | all five | 19/19 = 100.00 |
| V-05 | Full synthesis, CS domain, ROLES-first structure | Alternative section ordering (ROLES precedes CONSTRAINT MATRIX) tests structural independence | all five | 19/19 = 100.00 |

---

## V-01 — IS-Register Conversion (Single Axis: Phrasing Register)

**Variation axis:** Phrasing register
**Hypothesis:** Replacing imperative constraint language ("YOU MAY NOT", "Do not begin") with IS-declarative framing ("IS PROHIBITED", "IS BLOCKED", "ARE NOT VALID") throughout the constraint matrix and all gate language achieves C-24 without structural disruption. The vocabulary-locked handoff gate phrase converts cleanly: "Do not begin HANDOFF DECLARATION until VOCABULARY CLOSED is declared" → "HANDOFF DECLARATION IS BLOCKED until VOCABULARY IS FROZEN." C-22, C-23, C-25 are preserved from V-01 base. C-26 remains absent: the HANDOFF DECLARATION does not gain explicit role-state flip declarations. This isolates C-24 as a single-axis acquisition.
**Domain:** Sales (Lead / Qualified Lead / Opportunity / Proposal / Closed Won / Closed Lost)
**Predicted:** 18/19 = 98.95 (gains C-24; C-26 still absent)

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. Domain vocabulary IS declared by a Domain Expert [D] as numbered prose items before any tracing begins. A Trace Developer [T] executes the trace using only declared vocabulary. [D] signs a HANDOFF DECLARATION before [T] IS AUTHORIZED to proceed. The CONSTRAINT MATRIX IS the governing document; read it completely before producing any output.

---

### CONSTRAINT MATRIX

| ID | Architectural Fact | Assigned Role | Concern |
|----|--------------------|---------------|---------|
| C1 | A state name not declared in STATE DECLARATIONS IS PROHIBITED in any trace table | [T] | vocabulary |
| C2 | An operation name not declared in OPERATION DECLARATIONS IS PROHIBITED in any trace table | [T] | vocabulary |
| C3 | Prose paragraphs and bullet lists ARE NOT VALID primary output format for trace data; every operation IS REQUIRED to appear as a table row | [T] | format |
| C4 | A state or operation added after VOCABULARY CLOSED IS declared IS a retroactive violation and IS PROHIBITED | [D] | ordering |
| C5 | A blank invariant status cell in TRANSITION TABLE IS NOT PERMITTED | [T] | integrity |
| C6 | TRANSITION TABLE IS BLOCKED until GATE A IS confirmed | [T] | ordering |
| C7 | A blank or non-option response at INVENTORY CHALLENGE IS a C7 violation; GATE A IS BLOCKED without a written Option A or Option B response | [T] | completeness |
| C8 | INVALID TRANSITIONS IS BLOCKED until GATE B IS confirmed | [T] | ordering |
| C9 | RACE CONDITIONS IS BLOCKED until GATE C IS confirmed | [T] | ordering |

---

### ROLES

**[D] Domain Expert**
Auto-selected: Sales expert (Lead / Qualified Lead / Opportunity / Proposal / Closed Won / Closed Lost), Customer Service expert (New / Open / Pending / Resolved / Closed), or Finance expert (Draft / Submitted / Approved / Posted / Paid / Voided).
Owns: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, HANDOFF DECLARATION.
Binding constraint: **C4** (vocabulary IS FROZEN after VOCABULARY CLOSED IS declared).

**[T] Trace Developer**
Owns: INVENTORY CHALLENGE written response, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, FINDINGS.
Binding constraints: **C1, C2, C3, C5, C6, C7, C8, C9**.
Authorization: [T]'s authorization IS CONTINGENT on HANDOFF DECLARATION being signed by [D].

---

### STATE DECLARATIONS [D]

Declare all lifecycle states as numbered prose items. Each item MUST carry an inline definitional clause that distinguishes this state by entry conditions, characterizing field values, and whether it is terminal. Domain vocabulary IS REQUIRED; generic labels ARE PROHIBITED.

**S-01.** [State Name] -- [inline definitional clause: conditions that cause entry, field values that characterize this state, how it is distinct from adjacent states]. Terminal: Yes/No.
**S-02.** [State Name] -- [inline definitional clause]. Terminal: Yes/No.
*(continue for all lifecycle states)*

At least one item MUST be Terminal: Yes. STATE DECLARATIONS ARE COMPLETE when all lifecycle states have been declared with inline definitional clauses. STATE DECLARATIONS IS BLOCKED until this condition IS met.

---

### OPERATION DECLARATIONS [D]

Declare all lifecycle operations as numbered prose items. Each item MUST carry an inline definitional clause naming what the operation does, when it is triggered, which states it transitions from, and which state it produces. S-IDs MUST reference STATE DECLARATIONS entries.

**O-01.** [Operation Name] -- [inline definitional clause: what this operation does, when it is triggered, what distinguishes it from similar operations]. From: S-[N][, S-[N]...]. To: S-[N]. Actor: [role/system].
**O-02.** [Operation Name] -- [inline definitional clause]. From: S-[N]. To: S-[N]. Actor: [role/system].
*(continue for all lifecycle operations)*

All S-IDs ARE REQUIRED to resolve to STATE DECLARATIONS entries. An operation without From/To references IS NOT VALID. OPERATION DECLARATIONS IS BLOCKED until all operations carry From/To references. OPERATION DECLARATIONS ARE COMPLETE when all lifecycle operations have been declared. Do not begin INVARIANT DECLARATIONS until OPERATION DECLARATIONS ARE COMPLETE.

---

### INVARIANT DECLARATIONS [D]

Declare all object-level invariants as numbered items. Each item MUST include a boolean assertion and an authority source.

**INV-01.** [Name] -- [boolean assertion, e.g., `owner_id != null when status IN {S-02, S-03}`]. Authority: [business rule / SLA clause / regulation / policy].
**INV-02.** [Name] -- [boolean assertion]. Authority: [source].
*(minimum two invariants)*

---

### VOCABULARY CLOSED [D]

> VOCABULARY CLOSED per C4. States: [list all S-IDs and State Names from STATE DECLARATIONS]. Operations: [list all O-IDs and Operation Names from OPERATION DECLARATIONS]. The vocabulary IS FROZEN from this point forward. Any name not listed above IS PROHIBITED in all sections that follow. This prohibition IS NOT WAIVABLE.

HANDOFF DECLARATION IS BLOCKED until VOCABULARY IS FROZEN.

---

### HANDOFF DECLARATION [D]

> **[D] HANDOFF DECLARATION.** The STATE DECLARATIONS (S-01 through S-[N]), OPERATION DECLARATIONS (O-01 through O-[N]), and INVARIANT DECLARATIONS (INV-01 through INV-[N]) for {{topic}} are complete. VOCABULARY CLOSED is in effect. The following sections are hereby transferred to [T]: INVENTORY CHALLENGE response, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, FINDINGS. [T] is now authorized to proceed subject to constraints C1, C2, C3, C5, C6, C7, C8, C9. [D] may not alter any declaration from this point forward (C4).
>
> Acceptance condition: [T] must confirm receipt by responding to INVENTORY CHALLENGE with Option A or Option B. [T] IS BLOCKED from proceeding to GATE A until this acceptance IS written.
>
> **[D] Signed:** [domain role selected] -- [N] states declared (S-01 through S-[N]), [N] operations declared (O-01 through O-[N]).

---

### INVENTORY CHALLENGE

**C7 applies. A blank response or non-option response IS a C7 violation. GATE A IS BLOCKED without a written Option A or Option B response.**

INVENTORY IS DECLARED COMPLETE -- the STATE DECLARATIONS and OPERATION DECLARATIONS contain every state and operation in the lifecycle of {{topic}}.

**[T] response -- one option IS REQUIRED:**

**Option A (CONFIRMED):** "[T] INVENTORY CONFIRMED. I have reviewed STATE DECLARATIONS and OPERATION DECLARATIONS against the domain lifecycle of {{topic}}. No lifecycle state or operation IS absent. States: [repeat S-IDs and names]. Operations: [repeat O-IDs and names]. HANDOFF DECLARATION IS ACKNOWLEDGED. Proceeding to GATE A."

**Option B (GAP FOUND):** "[T] INVENTORY INCOMPLETE. Gap identified: [missing state or operation and why it belongs in the lifecycle]. Returning to [D] for declaration update. VOCABULARY CLOSED MUST be re-declared and HANDOFF DECLARATION re-signed before GATE A IS unblocked."

---

### GATE A

TRANSITION TABLE IS BLOCKED until all items below ARE confirmed. An unconfirmed item IS a blocker per C6.

- [ ] STATE DECLARATIONS ARE complete -- domain vocabulary, inline definitional clauses, at least one Terminal: Yes item
- [ ] OPERATION DECLARATIONS ARE complete -- all S-ID references resolve to STATE DECLARATIONS
- [ ] INVARIANT DECLARATIONS ARE complete -- at least two boolean assertions with authority sources
- [ ] VOCABULARY CLOSED IS declared with complete S-ID/O-ID list and forward-blocking prohibition
- [ ] HANDOFF DECLARATION IS signed by [D] with acceptance condition stated
- [ ] **[C7]** INVENTORY CHALLENGE IS resolved -- Option A or Option B IS written above
- [ ] **[C-14]** [T] confirms: no name will appear in TRANSITION TABLE, INVALID TRANSITIONS, or RACE CONDITIONS not declared in STATE DECLARATIONS or OPERATION DECLARATIONS
- [ ] **[C-15]** VOCABULARY CLOSED IS declared and forward-blocking prohibition IS in effect
- [ ] **[C-09]** Terminal states ARE identified in STATE DECLARATIONS -- at least one Terminal item WILL appear as From State in INVALID TRANSITIONS

**GATE A IS BLOCKED per C6. TRANSITION TABLE IS BLOCKED until all items ARE confirmed.**

---

### TRANSITION TABLE [T]

Scenario setup: [entity instance, starting state, actor, date/time context]

Constraints C1, C2, C3, C5 ARE in effect. From State and To State MUST use S-IDs from STATE DECLARATIONS. Operation MUST use O-IDs from OPERATION DECLARATIONS.

| # | From State (S-ID) | Operation (O-ID) | Preconditions | To State (S-ID) | Postconditions | INV-01 | INV-02 | Side Effects |
|---|-------------------|-----------------|---------------|-----------------|----------------|--------|--------|--------------|

- **From State / To State:** S-IDs from STATE DECLARATIONS only (C1).
- **Operation:** O-IDs from OPERATION DECLARATIONS only (C2).
- **Preconditions:** Minimum two testable assertions per row (e.g., `status == S-02`, `owner_id != null`).
- **Postconditions:** Minimum one assertion distinct from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED -- [reason]`; blank IS NOT PERMITTED (C5).
- **Side Effects:** Triggered rules, notifications, async jobs, record changes.

---

### GATE B

INVALID TRANSITIONS IS BLOCKED until all items below ARE confirmed. An unconfirmed item IS a blocker per C8.

- [ ] **[C-08]** TRANSITION TABLE IS columnar and complete; no operation IS documented only in prose
- [ ] **[C-05]** Every row HAS INV status per declared invariant; at least one VIOLATED row IS present
- [ ] **[C-06]** Every row HAS at least one postcondition distinct from the To State name
- [ ] Boundary coverage IS planned -- at least one terminal-state S-ID IS targeted for INVALID TRANSITIONS

**GATE B IS BLOCKED per C8. INVALID TRANSITIONS IS BLOCKED until all items ARE confirmed.**

---

### INVALID TRANSITIONS [T]

| # | Attempted Operation (O-ID) | From State (S-ID) | Blocking Condition | INV Reference | Risk if Bypassed |
|---|---------------------------|------------------|--------------------|--------------|-----------------|

Minimum three rows. At least one row WHERE From State IS a Terminal item from STATE DECLARATIONS IS REQUIRED. S-IDs and O-IDs only (C1, C2).

---

### GATE C

RACE CONDITIONS IS BLOCKED until all items below ARE confirmed. An unconfirmed item IS a blocker per C9.

- [ ] **[C-04]** At least three (operation, state) invalid pairs ARE named with blocking conditions; enumeration IS systematic
- [ ] **[C-09]** At least one INVALID TRANSITIONS row HAS From State = a Terminal item from STATE DECLARATIONS

**GATE C IS BLOCKED per C9. RACE CONDITIONS IS BLOCKED until all items ARE confirmed.**

---

### RACE CONDITIONS [T]

| Operation A (O-ID) | Operation B (O-ID) | Unsafe Interleaving | Outcome | Mitigation |
|--------------------|---------------------|---------------------|---------|-----------|

If no concurrent access: "No concurrent access -- [reason explaining why concurrent access IS NOT POSSIBLE for this object type]."

---

### GATE D

FINDINGS IS BLOCKED until all items below ARE confirmed.

- [ ] **[C-07]** RACE CONDITIONS ARE addressed -- at least one race scenario or explicit clearance with reason IS present
- [ ] All TRANSITION TABLE and INVALID TRANSITIONS S-IDs and O-IDs ARE resolved to STATE DECLARATIONS and OPERATION DECLARATIONS (C1, C2)
- [ ] Hard-stop review IS complete -- no section IS blank or placeholder-only

**GATE D IS BLOCKED. FINDINGS IS BLOCKED until all items ARE confirmed.**

---

### FINDINGS

Priority order. Reference section and item.

- **P[N]:** [title] -- [description, section/item reference]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: CONSTRAINT MATRIX, ROLES, STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, HANDOFF DECLARATION, INVENTORY CHALLENGE, GATE A, TRANSITION TABLE, GATE B, INVALID TRANSITIONS, GATE C, RACE CONDITIONS, GATE D, FINDINGS.

---

## V-02 — Post-Handoff Role-State Flip (Single Axis: Lifecycle Emphasis)

**Variation axis:** Lifecycle emphasis (how explicitly the HANDOFF DECLARATION marks the role-state transition)
**Hypothesis:** Augmenting the V-01 base HANDOFF DECLARATION with explicit simultaneous role-state declarations -- "[D] IS PROHIBITED from altering any declaration" and "[T] IS NOW AUTHORIZED" both appearing within the HANDOFF DECLARATION block itself -- achieves C-26 without requiring IS-register conversion throughout the rest of the document. The constraint matrix and gate language remain imperative ("YOU MAY NOT", "Do not begin"), so C-24 IS absent. C-22, C-23, C-25 are preserved. C-24 remains absent. This isolates C-26 as a single-axis acquisition.
**Domain:** Customer Service (New / Open / Pending / Resolved / Closed)
**Predicted:** 18/19 = 98.95 (gains C-26; C-24 still absent)

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

**INV-01.** [Name] -- [boolean assertion, e.g., `assignee_id != null when status IN {S-02, S-03, S-04}`]. Authority: [business rule / SLA clause / regulation / policy].
**INV-02.** [Name] -- [boolean assertion]. Authority: [source].
*(minimum two invariants)*

---

### VOCABULARY CLOSED [D]

> VOCABULARY CLOSED per C4. States: [list all S-IDs and State Names from STATE DECLARATIONS]. Operations: [list all O-IDs and Operation Names from OPERATION DECLARATIONS]. No new state or operation name may be introduced from this point forward. Any name not listed above is prohibited in all sections that follow.

Do not begin HANDOFF DECLARATION until VOCABULARY CLOSED is declared.

---

### HANDOFF DECLARATION [D]

> **[D] HANDOFF DECLARATION.** The STATE DECLARATIONS (S-01 through S-[N]), OPERATION DECLARATIONS (O-01 through O-[N]), and INVARIANT DECLARATIONS (INV-01 through INV-[N]) for {{topic}} are complete. VOCABULARY CLOSED is in effect. The following artifacts are hereby transferred to [T]: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS.
>
> **Post-transfer role states (declared simultaneously upon execution of this HANDOFF DECLARATION):**
> [D] IS PROHIBITED from altering any declaration, registry entry, or vocabulary item from this point forward. [D]'s authoring authority over STATE DECLARATIONS, OPERATION DECLARATIONS, and INVARIANT DECLARATIONS IS REVOKED at this moment. This prohibition IS NOT WAIVABLE and IS NOT CONTINGENT on [T]'s acceptance.
> [T] IS NOW AUTHORIZED to proceed to INVENTORY CHALLENGE, GATE A, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, and FINDINGS. [T]'s authorization IS CONTINGENT on this HANDOFF DECLARATION having been executed. [T] was not authorized before this declaration; [T] IS authorized now.
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
- [ ] HANDOFF DECLARATION signed by [D] -- post-transfer role states ([D] PROHIBITED, [T] AUTHORIZED) explicitly declared
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
- **Preconditions:** Minimum two testable assertions per row.
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

## V-03 — C-24 + C-26 Pairwise Synthesis on V-01 Base

**Variation axis:** Phrasing register × post-handoff role-state (two axes combined)
**Hypothesis:** Both IS-register conversion (C-24) and explicit role-state flip in HANDOFF DECLARATION (C-26) can be applied to the V-01 base simultaneously without structural conflict. C-23 (numbered prose inventories) and C-25 (vocabulary-locked handoff gate) are preserved from V-01. The vocabulary-locked handoff gate phrase converts to IS-register: "HANDOFF DECLARATION IS BLOCKED until VOCABULARY IS FROZEN." The HANDOFF DECLARATION gains the role-state flip block. All five new aspirational criteria are present. Structural test: IS-register throughout + role-state flip in HANDOFF + numbered prose inventories + vocabulary-locked gate all coexist in a single variant.
**Domain:** Finance (Draft / Submitted / Approved / Posted / Paid / Voided)
**Predicted:** 19/19 = 100.00

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. Domain vocabulary IS declared by a Domain Expert [D] as numbered prose items before any tracing begins. A Trace Developer [T] executes the trace using only declared vocabulary. [D] signs a HANDOFF DECLARATION before [T] IS AUTHORIZED to proceed. The CONSTRAINT MATRIX IS the governing document; every constraint IS a structural fact, not an instruction. Read the CONSTRAINT MATRIX completely before producing any output.

---

### CONSTRAINT MATRIX

| ID | Architectural Fact | Assigned Role | Concern |
|----|--------------------|---------------|---------|
| C1 | A state name not declared in STATE DECLARATIONS IS PROHIBITED in any trace table | [T] | vocabulary |
| C2 | An operation name not declared in OPERATION DECLARATIONS IS PROHIBITED in any trace table | [T] | vocabulary |
| C3 | Prose paragraphs and bullet lists ARE NOT VALID primary output format for trace data; every operation IS REQUIRED to appear as a table row | [T] | format |
| C4 | A state or operation added after VOCABULARY CLOSED IS declared IS a retroactive violation and IS PROHIBITED | [D] | ordering |
| C5 | A blank invariant status cell in TRANSITION TABLE IS NOT PERMITTED | [T] | integrity |
| C6 | TRANSITION TABLE IS BLOCKED until GATE A IS confirmed | [T] | ordering |
| C7 | A blank or non-option response at INVENTORY CHALLENGE IS a C7 violation; GATE A IS BLOCKED without a written Option A or Option B response | [T] | completeness |
| C8 | INVALID TRANSITIONS IS BLOCKED until GATE B IS confirmed | [T] | ordering |
| C9 | RACE CONDITIONS IS BLOCKED until GATE C IS confirmed | [T] | ordering |

---

### ROLES

**[D] Domain Expert**
Auto-selected: Sales expert (Lead / Qualified Lead / Opportunity / Proposal / Closed Won / Closed Lost), Customer Service expert (New / Open / Pending / Resolved / Closed), or Finance expert (Draft / Submitted / Approved / Posted / Paid / Voided).
Owns: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, HANDOFF DECLARATION.
Binding constraint: **C4** (vocabulary IS FROZEN after VOCABULARY CLOSED IS declared).

**[T] Trace Developer**
Owns: INVENTORY CHALLENGE written response, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, FINDINGS.
Binding constraints: **C1, C2, C3, C5, C6, C7, C8, C9**.
Authorization: [T]'s authorization IS CONTINGENT on HANDOFF DECLARATION being signed by [D].

---

### STATE DECLARATIONS [D]

Declare all lifecycle states as numbered prose items. Each item MUST carry an inline definitional clause distinguishing this state by entry conditions, characterizing field values, and terminal status. Domain vocabulary IS REQUIRED; generic labels ARE PROHIBITED.

**S-01.** [State Name] -- [inline definitional clause: conditions that cause entry, field values that characterize this state, how it is distinct from adjacent states]. Terminal: Yes/No.
**S-02.** [State Name] -- [inline definitional clause]. Terminal: Yes/No.
*(continue for all lifecycle states)*

At least one item MUST be Terminal: Yes. STATE DECLARATIONS IS BLOCKED until this condition IS met. Do not begin OPERATION DECLARATIONS until STATE DECLARATIONS ARE COMPLETE.

---

### OPERATION DECLARATIONS [D]

Declare all lifecycle operations as numbered prose items. Each item MUST carry an inline definitional clause naming what the operation does, when it is triggered, which states it transitions from, and which state it produces. S-IDs MUST reference STATE DECLARATIONS entries.

**O-01.** [Operation Name] -- [inline definitional clause: what this operation does, when it is triggered, what distinguishes it from similar operations]. From: S-[N][, S-[N]...]. To: S-[N]. Actor: [role/system].
**O-02.** [Operation Name] -- [inline definitional clause]. From: S-[N]. To: S-[N]. Actor: [role/system].
*(continue for all lifecycle operations)*

All S-IDs ARE REQUIRED to resolve to STATE DECLARATIONS entries. An operation without From/To references IS NOT VALID. Do not begin INVARIANT DECLARATIONS until OPERATION DECLARATIONS ARE COMPLETE.

---

### INVARIANT DECLARATIONS [D]

Declare all object-level invariants as numbered items. Each item MUST include a boolean assertion and an authority source.

**INV-01.** [Name] -- [boolean assertion, e.g., `approver_id != null when status IN {S-03, S-04, S-05}`]. Authority: [business rule / SLA clause / regulation / policy].
**INV-02.** [Name] -- [boolean assertion]. Authority: [source].
*(minimum two invariants)*

---

### VOCABULARY CLOSED [D]

> VOCABULARY CLOSED per C4. States: [list all S-IDs and State Names from STATE DECLARATIONS]. Operations: [list all O-IDs and Operation Names from OPERATION DECLARATIONS]. The vocabulary IS FROZEN from this point forward. Any name not listed above IS PROHIBITED in all sections that follow. This prohibition IS NOT WAIVABLE.

HANDOFF DECLARATION IS BLOCKED until VOCABULARY IS FROZEN.

---

### HANDOFF DECLARATION [D]

> **[D] HANDOFF DECLARATION.** The STATE DECLARATIONS (S-01 through S-[N]), OPERATION DECLARATIONS (O-01 through O-[N]), and INVARIANT DECLARATIONS (INV-01 through INV-[N]) for {{topic}} ARE COMPLETE. VOCABULARY CLOSED IS in effect. The following artifacts ARE hereby transferred to [T]: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS.
>
> **Post-transfer role states (declared simultaneously upon execution of this HANDOFF DECLARATION):**
> [D] IS PROHIBITED from altering any declaration, registry entry, or vocabulary item from this point forward. [D]'s authoring authority over STATE DECLARATIONS, OPERATION DECLARATIONS, and INVARIANT DECLARATIONS IS REVOKED at this moment. This prohibition IS NOT WAIVABLE.
> [T] IS NOW AUTHORIZED to proceed to INVENTORY CHALLENGE, GATE A, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, and FINDINGS. [T]'s authorization IS CONTINGENT on this HANDOFF DECLARATION having been executed. [T] WAS NOT AUTHORIZED before this declaration; [T] IS AUTHORIZED now.
>
> Acceptance condition: [T] IS REQUIRED to confirm receipt by responding to INVENTORY CHALLENGE with Option A or Option B. GATE A IS BLOCKED until this acceptance IS written.
>
> **[D] Signed:** [domain role selected] -- [N] states declared (S-01 through S-[N]), [N] operations declared (O-01 through O-[N]).

---

### INVENTORY CHALLENGE

**C7 applies. A blank or non-option response IS a C7 violation. GATE A IS BLOCKED without a written Option A or Option B response.**

INVENTORY IS DECLARED COMPLETE -- the STATE DECLARATIONS and OPERATION DECLARATIONS ARE the complete lifecycle vocabulary for {{topic}}.

**[T] response -- one option IS REQUIRED:**

**Option A (CONFIRMED):** "[T] INVENTORY CONFIRMED. The STATE DECLARATIONS and OPERATION DECLARATIONS ARE the complete lifecycle vocabulary for {{topic}}. No lifecycle state or operation IS absent. States: [repeat S-IDs and names]. Operations: [repeat O-IDs and names]. HANDOFF DECLARATION IS ACKNOWLEDGED. Proceeding to GATE A."

**Option B (GAP FOUND):** "[T] INVENTORY INCOMPLETE. Gap identified: [missing state or operation and why it belongs in the lifecycle]. Returning to [D] for declaration update. VOCABULARY CLOSED MUST be re-declared and HANDOFF DECLARATION re-signed before GATE A IS unblocked."

---

### GATE A

TRANSITION TABLE IS BLOCKED until all items below ARE confirmed. An unconfirmed item IS a blocker per C6.

- [ ] STATE DECLARATIONS ARE complete -- domain vocabulary, inline definitional clauses, at least one Terminal: Yes item
- [ ] OPERATION DECLARATIONS ARE complete -- all S-ID references resolve to STATE DECLARATIONS
- [ ] INVARIANT DECLARATIONS ARE complete -- at least two boolean assertions with authority sources
- [ ] VOCABULARY CLOSED IS declared -- vocabulary IS FROZEN; prohibition IS in effect
- [ ] HANDOFF DECLARATION IS signed by [D] -- post-transfer role states ([D] IS PROHIBITED, [T] IS AUTHORIZED) ARE explicitly declared within the HANDOFF DECLARATION block
- [ ] **[C7]** INVENTORY CHALLENGE IS resolved -- Option A or Option B IS written above
- [ ] **[C-14]** [T] confirms: no name WILL appear in TRANSITION TABLE, INVALID TRANSITIONS, or RACE CONDITIONS that IS NOT declared in STATE DECLARATIONS or OPERATION DECLARATIONS
- [ ] **[C-15]** VOCABULARY CLOSED IS declared and forward-blocking prohibition IS in effect
- [ ] **[C-09]** Terminal states ARE identified in STATE DECLARATIONS -- at least one Terminal item WILL appear as From State in INVALID TRANSITIONS

**GATE A IS BLOCKED per C6. TRANSITION TABLE IS BLOCKED until all items ARE confirmed.**

---

### TRANSITION TABLE [T]

Scenario setup: [entity instance, starting state, actor, date/time context]

Constraints C1, C2, C3, C5 ARE in effect. From State and To State MUST use S-IDs from STATE DECLARATIONS. Operation MUST use O-IDs from OPERATION DECLARATIONS.

| # | From State (S-ID) | Operation (O-ID) | Preconditions | To State (S-ID) | Postconditions | INV-01 | INV-02 | Side Effects |
|---|-------------------|-----------------|---------------|-----------------|----------------|--------|--------|--------------|

- **From State / To State:** S-IDs from STATE DECLARATIONS only (C1).
- **Operation:** O-IDs from OPERATION DECLARATIONS only (C2).
- **Preconditions:** Minimum two testable assertions per row.
- **Postconditions:** Minimum one assertion distinct from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED -- [reason]`; blank IS NOT PERMITTED (C5).
- **Side Effects:** Triggered rules, notifications, async jobs, record changes.

---

### GATE B

INVALID TRANSITIONS IS BLOCKED until all items below ARE confirmed. An unconfirmed item IS a blocker per C8.

- [ ] **[C-08]** TRANSITION TABLE IS columnar and complete; no operation IS documented only in prose
- [ ] **[C-05]** Every row HAS INV status per declared invariant; at least one VIOLATED row IS present
- [ ] **[C-06]** Every row HAS at least one postcondition distinct from the To State name
- [ ] Boundary coverage IS planned -- at least one terminal-state S-ID IS targeted for INVALID TRANSITIONS

**GATE B IS BLOCKED per C8. INVALID TRANSITIONS IS BLOCKED until all items ARE confirmed.**

---

### INVALID TRANSITIONS [T]

| # | Attempted Operation (O-ID) | From State (S-ID) | Blocking Condition | INV Reference | Risk if Bypassed |
|---|---------------------------|------------------|--------------------|--------------|-----------------|

Minimum three rows. At least one row WHERE From State IS a Terminal item from STATE DECLARATIONS IS REQUIRED. S-IDs and O-IDs only (C1, C2).

---

### GATE C

RACE CONDITIONS IS BLOCKED until all items below ARE confirmed. An unconfirmed item IS a blocker per C9.

- [ ] **[C-04]** At least three (operation, state) invalid pairs ARE named with blocking conditions; enumeration IS systematic
- [ ] **[C-09]** At least one INVALID TRANSITIONS row HAS From State = a Terminal item from STATE DECLARATIONS

**GATE C IS BLOCKED per C9. RACE CONDITIONS IS BLOCKED until all items ARE confirmed.**

---

### RACE CONDITIONS [T]

| Operation A (O-ID) | Operation B (O-ID) | Unsafe Interleaving | Outcome | Mitigation |
|--------------------|---------------------|---------------------|---------|-----------|

If no concurrent access: "No concurrent access -- [reason explaining why concurrent access IS NOT POSSIBLE for this object type]."

---

### GATE D

FINDINGS IS BLOCKED until all items below ARE confirmed.

- [ ] **[C-07]** RACE CONDITIONS ARE addressed -- at least one race scenario or explicit clearance with reason IS present
- [ ] All TRANSITION TABLE and INVALID TRANSITIONS S-IDs and O-IDs ARE resolved to STATE DECLARATIONS and OPERATION DECLARATIONS (C1, C2)
- [ ] Hard-stop review IS complete -- no section IS blank or placeholder-only

**GATE D IS BLOCKED. FINDINGS IS BLOCKED until all items ARE confirmed.**

---

### FINDINGS

Priority order. Reference section and item.

- **P[N]:** [title] -- [description, section/item reference]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: CONSTRAINT MATRIX, ROLES, STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, HANDOFF DECLARATION, INVENTORY CHALLENGE, GATE A, TRANSITION TABLE, GATE B, INVALID TRANSITIONS, GATE C, RACE CONDITIONS, GATE D, FINDINGS.

---

## V-04 — Full Synthesis, Fresh Build (Sales Domain)

**Variation axis:** Full synthesis (all five new criteria: C-22 + C-23 + C-24 + C-25 + C-26)
**Hypothesis:** A freshly structured variant that designs for all 19 aspirational criteria simultaneously -- without inheriting the V-01 base's structural baggage -- produces the 19/19 ceiling. Key structural decisions: (1) CONSTRAINT MATRIX uses IS/IS NOT declarative framing throughout (C-24); (2) STATE DECLARATIONS and OPERATION DECLARATIONS use numbered prose items with inline definitional clauses (C-23); (3) VOCABULARY CLOSED carries an explicit "HANDOFF DECLARATION IS BLOCKED until VOCABULARY IS FROZEN" gate phrase (C-25); (4) HANDOFF DECLARATION carries simultaneous [D] IS PROHIBITED + [T] IS NOW AUTHORIZED declarations (C-26); (5) HANDOFF DECLARATION structure, roles, artifacts, and acceptance condition all present (C-22). Inertia framing added: an INERTIA BASELINE section names the status-quo alternative and the failure mode the trace exists to prevent. Tests whether fresh architecture is cleaner than base conversion.
**Domain:** Sales (Lead / Qualified Lead / Opportunity / Proposal / Closed Won / Closed Lost)
**Predicted:** 19/19 = 100.00

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. This trace IS a formal artifact; its governing document IS the CONSTRAINT MATRIX below. A Domain Expert [D] declares the vocabulary phase; a Trace Developer [T] executes the trace phase. [T]'s authorization IS CONTINGENT on [D] completing and executing a HANDOFF DECLARATION. The CONSTRAINT MATRIX IS authoritative. Read it completely before producing any output.

---

### INERTIA BASELINE

The alternative to this trace IS: implement {{topic}} state management without hand-compiling transitions and invariants. The failure mode that alternative creates IS: invalid state transitions reach production because precondition checks were assumed rather than enumerated. This trace exists to close that gap before code is written. Every section that is skipped or left as a placeholder IS a return to the inertia baseline.

---

### CONSTRAINT MATRIX

| ID | Architectural Fact | Assigned Role | Concern |
|----|--------------------|---------------|---------|
| C1 | A state name not declared in STATE DECLARATIONS IS PROHIBITED in any trace table | [T] | vocabulary |
| C2 | An operation name not declared in OPERATION DECLARATIONS IS PROHIBITED in any trace table | [T] | vocabulary |
| C3 | Prose paragraphs and bullet lists ARE NOT VALID as primary trace output; every operation IS REQUIRED as a table row | [T] | format |
| C4 | Any state or operation added after VOCABULARY CLOSED IS declared IS a retroactive violation; such additions ARE PROHIBITED | [D] | ordering |
| C5 | A blank invariant status cell in the TRANSITION TABLE IS NOT PERMITTED; every cell IS REQUIRED to contain HOLDS or VIOLATED | [T] | integrity |
| C6 | TRANSITION TABLE IS BLOCKED until GATE A IS confirmed | [T] | ordering |
| C7 | A blank or non-option response at INVENTORY CHALLENGE IS a C7 violation; GATE A IS BLOCKED in the presence of a C7 violation | [T] | completeness |
| C8 | INVALID TRANSITIONS IS BLOCKED until GATE B IS confirmed | [T] | ordering |
| C9 | RACE CONDITIONS IS BLOCKED until GATE C IS confirmed | [T] | ordering |

---

### ROLES

**[D] Domain Expert**
Auto-selected: Sales expert (Lead / Qualified Lead / Opportunity / Proposal / Closed Won / Closed Lost), Customer Service expert (New / Open / Pending / Resolved / Closed), or Finance expert (Draft / Submitted / Approved / Posted / Paid / Voided).
Sections owned by [D]: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, HANDOFF DECLARATION.
Binding constraint: **C4** (vocabulary IS FROZEN after VOCABULARY CLOSED IS declared; retroactive additions ARE PROHIBITED).

**[T] Trace Developer**
Sections owned by [T]: INVENTORY CHALLENGE response, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, FINDINGS.
Binding constraints: **C1, C2, C3, C5, C6, C7, C8, C9**.
Authorization status: [T]'s authorization IS CONTINGENT on HANDOFF DECLARATION. Prior to HANDOFF DECLARATION, [T] IS NOT AUTHORIZED to produce output in any [T]-owned section.

---

### STATE DECLARATIONS [D]

Declare all lifecycle states as numbered prose items with inline definitional clauses. Each entry IS REQUIRED to name: (a) the conditions that cause entry into this state, (b) the field values that characterize it, and (c) whether it is terminal. Generic labels ARE PROHIBITED; domain vocabulary IS REQUIRED.

**S-01.** [State Name] -- [inline definitional clause: entry conditions, characterizing field values, terminal status, and what distinguishes this state from all other states in the lifecycle]. Terminal: Yes/No.
**S-02.** [State Name] -- [inline definitional clause]. Terminal: Yes/No.
*(continue for all lifecycle states)*

A STATE DECLARATIONS section without at least one Terminal: Yes entry IS INCOMPLETE. STATE DECLARATIONS IS BLOCKED until this condition IS met. Do not begin OPERATION DECLARATIONS until STATE DECLARATIONS IS COMPLETE.

---

### OPERATION DECLARATIONS [D]

Declare all lifecycle operations as numbered prose items with inline definitional clauses. Each entry IS REQUIRED to name: (a) what the operation does, (b) when it is triggered, (c) all legal source states by S-ID, and (d) the target state by S-ID. An operation entry without S-ID references IS NOT VALID.

**O-01.** [Operation Name] -- [inline definitional clause: what this operation does, when it is triggered, and what distinguishes it from adjacent operations in the lifecycle]. From: S-[N][, S-[N]...]. To: S-[N]. Actor: [role/system].
**O-02.** [Operation Name] -- [inline definitional clause]. From: S-[N]. To: S-[N]. Actor: [role/system].
*(continue for all lifecycle operations)*

All S-IDs ARE REQUIRED to reference STATE DECLARATIONS entries. Do not begin INVARIANT DECLARATIONS until OPERATION DECLARATIONS IS COMPLETE.

---

### INVARIANT DECLARATIONS [D]

Declare all object-level invariants as numbered items. Each item IS REQUIRED to include a boolean assertion and an authority source. A declaration without a boolean assertion IS NOT VALID.

**INV-01.** [Name] -- [boolean assertion, e.g., `owner_id != null when status IN {S-02, S-03, S-04}`]. Authority: [business rule / SLA clause / regulation / policy].
**INV-02.** [Name] -- [boolean assertion]. Authority: [source].
*(minimum two invariants required; INVARIANT DECLARATIONS IS BLOCKED until two valid entries ARE present)*

---

### VOCABULARY CLOSED [D]

> VOCABULARY CLOSED per C4. States: [list all S-IDs and State Names from STATE DECLARATIONS]. Operations: [list all O-IDs and Operation Names from OPERATION DECLARATIONS]. The vocabulary IS FROZEN. Any state name or operation name not listed above IS PROHIBITED in all subsequent sections. This prohibition IS NOT WAIVABLE and IS NOT CONTINGENT on any further action.

HANDOFF DECLARATION IS BLOCKED until VOCABULARY IS FROZEN. Executing HANDOFF DECLARATION before this declaration IS a C4 violation.

---

### HANDOFF DECLARATION [D]

> **[D] HANDOFF DECLARATION.**
>
> Transferring role IS: [D] (Domain Expert -- [auto-selected domain] expert).
> Receiving role IS: [T] (Trace Developer).
>
> Artifacts transferred ARE: STATE DECLARATIONS (S-01 through S-[N]), OPERATION DECLARATIONS (O-01 through O-[N]), INVARIANT DECLARATIONS (INV-01 through INV-[N]).
>
> **Post-transfer role states (both declared simultaneously at this moment):**
> [D] IS PROHIBITED from altering any declaration in STATE DECLARATIONS, OPERATION DECLARATIONS, or INVARIANT DECLARATIONS from this point forward. [D]'s modification authority IS REVOKED. This prohibition IS NOT WAIVABLE.
> [T] IS NOW AUTHORIZED to produce output in all [T]-owned sections: INVENTORY CHALLENGE, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, FINDINGS. [T]'s authorization IS CONTINGENT on this HANDOFF DECLARATION having been executed. [T] WAS NOT AUTHORIZED prior to this moment; [T] IS AUTHORIZED now.
>
> Acceptance condition: [T] IS REQUIRED to write an explicit Option A or Option B response to INVENTORY CHALLENGE before GATE A IS cleared. GATE A IS BLOCKED until this acceptance IS written. The acceptance IS the formal mechanism by which [T] takes ownership of the declared artifacts.
>
> **[D] Signed:** [domain role selected] -- [N] states (S-01 through S-[N]), [N] operations (O-01 through O-[N]), [N] invariants (INV-01 through INV-[N]) ARE DECLARED AND CLOSED.

---

### INVENTORY CHALLENGE

**C7 applies. A blank or non-option response IS a C7 violation. GATE A IS BLOCKED in the presence of a C7 violation.**

INVENTORY IS DECLARED COMPLETE -- the STATE DECLARATIONS and OPERATION DECLARATIONS contain every state and operation in the lifecycle of {{topic}}.

**[T] response -- one option IS REQUIRED:**

**Option A (CONFIRMED):** "[T] INVENTORY CONFIRMED. The STATE DECLARATIONS and OPERATION DECLARATIONS ARE the complete lifecycle vocabulary for {{topic}}. No lifecycle state or operation IS absent. States: [repeat S-IDs and names]. Operations: [repeat O-IDs and names]. HANDOFF DECLARATION IS ACKNOWLEDGED. [T]'s authorization IS IN EFFECT. Proceeding to GATE A."

**Option B (GAP FOUND):** "[T] INVENTORY INCOMPLETE. Gap identified: [missing state or operation and why it belongs in the lifecycle]. Returning to [D] for declaration update. VOCABULARY CLOSED MUST be re-declared and HANDOFF DECLARATION re-signed before GATE A IS unblocked."

---

### GATE A

TRANSITION TABLE IS BLOCKED until all items below ARE confirmed. An unconfirmed item IS a blocker per C6.

- [ ] STATE DECLARATIONS ARE complete -- domain vocabulary, inline definitional clauses, at least one Terminal: Yes item IS present
- [ ] OPERATION DECLARATIONS ARE complete -- all S-ID references ARE resolved to STATE DECLARATIONS
- [ ] INVARIANT DECLARATIONS ARE complete -- at least two boolean assertions with authority sources ARE present
- [ ] VOCABULARY CLOSED IS declared -- vocabulary IS FROZEN; prohibition IS in effect
- [ ] HANDOFF DECLARATION IS signed -- post-transfer role states ([D] IS PROHIBITED, [T] IS NOW AUTHORIZED) ARE explicitly declared within HANDOFF DECLARATION block
- [ ] **[C7]** INVENTORY CHALLENGE IS resolved -- Option A or Option B IS written above; no C7 violation IS present
- [ ] **[C-14]** [T] confirms: no name WILL appear in TRANSITION TABLE, INVALID TRANSITIONS, or RACE CONDITIONS that IS NOT declared in STATE DECLARATIONS or OPERATION DECLARATIONS
- [ ] **[C-15]** VOCABULARY CLOSED IS declared and forward-blocking prohibition IS in effect
- [ ] **[C-09]** Terminal states ARE identified in STATE DECLARATIONS; at least one Terminal item WILL appear as From State in INVALID TRANSITIONS

**GATE A IS BLOCKED per C6. TRANSITION TABLE IS BLOCKED until all items ARE confirmed.**

---

### TRANSITION TABLE [T]

Scenario setup: [entity instance, starting state, actor, date/time context]

Constraints C1, C2, C3, C5 ARE in effect. From State and To State MUST use S-IDs. Operation MUST use O-IDs. Prose IS NOT VALID as primary trace output (C3).

| # | From State (S-ID) | Operation (O-ID) | Preconditions | To State (S-ID) | Postconditions | INV-01 | INV-02 | Side Effects |
|---|-------------------|-----------------|---------------|-----------------|----------------|--------|--------|--------------|

- **From State / To State:** S-IDs from STATE DECLARATIONS only (C1).
- **Operation:** O-IDs from OPERATION DECLARATIONS only (C2).
- **Preconditions:** Minimum two testable assertions per row (e.g., `status == S-02`, `owner_id != null`).
- **Postconditions:** Minimum one assertion distinct from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED -- [reason]`; blank IS NOT PERMITTED (C5).
- **Side Effects:** Triggered rules, notifications, async jobs, record changes.

---

### GATE B

INVALID TRANSITIONS IS BLOCKED until all items below ARE confirmed. An unconfirmed item IS a blocker per C8.

- [ ] **[C-08]** TRANSITION TABLE IS columnar and complete; no operation IS documented only in prose
- [ ] **[C-05]** Every row HAS INV status per declared invariant; at least one VIOLATED row IS present
- [ ] **[C-06]** Every row HAS at least one postcondition distinct from the To State name
- [ ] Boundary coverage IS planned -- at least one terminal-state S-ID IS targeted for INVALID TRANSITIONS

**GATE B IS BLOCKED per C8. INVALID TRANSITIONS IS BLOCKED until all items ARE confirmed.**

---

### INVALID TRANSITIONS [T]

| # | Attempted Operation (O-ID) | From State (S-ID) | Blocking Condition | INV Reference | Risk if Bypassed |
|---|---------------------------|------------------|--------------------|--------------|-----------------|

Minimum three rows. At least one row WHERE From State IS a Terminal item from STATE DECLARATIONS IS REQUIRED. S-IDs and O-IDs only (C1, C2).

---

### GATE C

RACE CONDITIONS IS BLOCKED until all items below ARE confirmed. An unconfirmed item IS a blocker per C9.

- [ ] **[C-04]** At least three (operation, state) invalid pairs ARE named with blocking conditions; enumeration IS systematic
- [ ] **[C-09]** At least one INVALID TRANSITIONS row HAS From State = a Terminal item from STATE DECLARATIONS

**GATE C IS BLOCKED per C9. RACE CONDITIONS IS BLOCKED until all items ARE confirmed.**

---

### RACE CONDITIONS [T]

| Operation A (O-ID) | Operation B (O-ID) | Unsafe Interleaving | Outcome | Mitigation |
|--------------------|---------------------|---------------------|---------|-----------|

If no concurrent access: "No concurrent access -- [reason explaining why concurrent access IS NOT POSSIBLE for this object type]."

---

### GATE D

FINDINGS IS BLOCKED until all items below ARE confirmed.

- [ ] **[C-07]** RACE CONDITIONS ARE addressed -- at least one race scenario or explicit clearance with reason IS present
- [ ] All TRANSITION TABLE and INVALID TRANSITIONS S-IDs and O-IDs ARE resolved to STATE DECLARATIONS and OPERATION DECLARATIONS (C1, C2)
- [ ] Hard-stop review IS complete -- no section IS blank or placeholder-only

**GATE D IS BLOCKED. FINDINGS IS BLOCKED until all items ARE confirmed.**

---

### FINDINGS

Priority order. Reference section and item.

- **P[N]:** [title] -- [description, section/item reference]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: INERTIA BASELINE, CONSTRAINT MATRIX, ROLES, STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, HANDOFF DECLARATION, INVENTORY CHALLENGE, GATE A, TRANSITION TABLE, GATE B, INVALID TRANSITIONS, GATE C, RACE CONDITIONS, GATE D, FINDINGS.

---

## V-05 — Full Synthesis, ROLES-First Structure (Customer Service Domain)

**Variation axis:** Role sequence × full synthesis (all five new criteria)
**Hypothesis:** Reordering the preamble so ROLES precedes CONSTRAINT MATRIX tests whether the synthesis is structurally independent of section ordering. The ROLES block establishes [D] and [T] with their IS-register authority statements before the constraint registry formalizes individual prohibitions. This "authority-first" ordering emphasizes that each constraint IS owned before it IS enumerated -- a structural framing distinct from V-03 and V-04 where constraints precede roles. All 19 aspirational criteria remain achievable under this ordering: C-22 through C-26 are fully compatible with ROLES-first structure. Tests structural generalizability of the R11 synthesis.
**Domain:** Customer Service (New / Open / Pending / Resolved / Closed)
**Predicted:** 19/19 = 100.00

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. This trace IS a formal artifact governed by role assignments and constraints declared below. A Domain Expert [D] IS responsible for the vocabulary phase; a Trace Developer [T] IS responsible for the trace execution phase. [T]'s authorization IS CONTINGENT on [D] executing a HANDOFF DECLARATION. Read ROLES and CONSTRAINT MATRIX completely before producing any output.

---

### ROLES

**[D] Domain Expert**
[D] IS the authority for vocabulary. [D]'s sections ARE: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, HANDOFF DECLARATION.
[D]'s binding constraint IS: vocabulary IS FROZEN after VOCABULARY CLOSED IS declared; retroactive additions ARE PROHIBITED ([D] IS bound by C4).
[D]'s authorization IS revoked at HANDOFF DECLARATION: after executing HANDOFF DECLARATION, [D] IS PROHIBITED from altering any declaration in any [D]-owned section.

**[T] Trace Developer**
[T] IS the authority for trace execution. [T]'s sections ARE: INVENTORY CHALLENGE response, TRANSITION TABLE, INVALID TRANSITIONS, RACE CONDITIONS, FINDINGS.
[T]'s binding constraints ARE: C1, C2, C3, C5, C6, C7, C8, C9.
[T]'s authorization IS CONTINGENT on HANDOFF DECLARATION. Prior to HANDOFF DECLARATION, [T] IS NOT AUTHORIZED to produce output in any [T]-owned section.

Auto-select domain: Sales expert (Lead / Qualified Lead / Opportunity / Proposal / Closed Won / Closed Lost), Customer Service expert (New / Open / Pending / Resolved / Closed), or Finance expert (Draft / Submitted / Approved / Posted / Paid / Voided).

---

### CONSTRAINT MATRIX

| ID | Architectural Fact | Assigned Role | Concern |
|----|--------------------|---------------|---------|
| C1 | A state name not declared in STATE DECLARATIONS IS PROHIBITED in any trace table | [T] | vocabulary |
| C2 | An operation name not declared in OPERATION DECLARATIONS IS PROHIBITED in any trace table | [T] | vocabulary |
| C3 | Prose paragraphs and bullet lists ARE NOT VALID as primary trace output; every operation IS REQUIRED as a table row | [T] | format |
| C4 | Any state or operation added after VOCABULARY CLOSED IS declared IS a retroactive violation and IS PROHIBITED | [D] | ordering |
| C5 | A blank invariant status cell in the TRANSITION TABLE IS NOT PERMITTED; HOLDS or VIOLATED IS REQUIRED per cell | [T] | integrity |
| C6 | TRANSITION TABLE IS BLOCKED until GATE A IS confirmed | [T] | ordering |
| C7 | A blank or non-option response at INVENTORY CHALLENGE IS a C7 violation; GATE A IS BLOCKED in the presence of a C7 violation | [T] | completeness |
| C8 | INVALID TRANSITIONS IS BLOCKED until GATE B IS confirmed | [T] | ordering |
| C9 | RACE CONDITIONS IS BLOCKED until GATE C IS confirmed | [T] | ordering |

---

### STATE DECLARATIONS [D]

Declare all lifecycle states as numbered prose items. Each entry IS REQUIRED to carry an inline definitional clause distinguishing this state by: (a) entry conditions, (b) characterizing field values, and (c) terminal status. Domain vocabulary IS REQUIRED; generic labels (State A, initial) ARE PROHIBITED.

**S-01.** [State Name] -- [inline definitional clause: conditions that cause entry, field values that characterize this state, how it is distinct from adjacent states]. Terminal: Yes/No.
**S-02.** [State Name] -- [inline definitional clause]. Terminal: Yes/No.
*(continue for all lifecycle states)*

A STATE DECLARATIONS section without at least one Terminal: Yes entry IS INCOMPLETE; STATE DECLARATIONS IS BLOCKED until this condition IS met. Do not begin OPERATION DECLARATIONS until STATE DECLARATIONS IS COMPLETE.

---

### OPERATION DECLARATIONS [D]

Declare all lifecycle operations as numbered prose items. Each entry IS REQUIRED to carry an inline definitional clause naming: (a) what the operation does, (b) when it is triggered, (c) all legal source states by S-ID, and (d) the target state by S-ID.

**O-01.** [Operation Name] -- [inline definitional clause: what this operation does, when it is triggered, what distinguishes it from similar operations]. From: S-[N][, S-[N]...]. To: S-[N]. Actor: [role/system].
**O-02.** [Operation Name] -- [inline definitional clause]. From: S-[N]. To: S-[N]. Actor: [role/system].
*(continue for all lifecycle operations)*

An operation entry without S-ID references IS NOT VALID. All S-IDs ARE REQUIRED to resolve to STATE DECLARATIONS entries. Do not begin INVARIANT DECLARATIONS until OPERATION DECLARATIONS IS COMPLETE.

---

### INVARIANT DECLARATIONS [D]

Declare all object-level invariants as numbered items. Each item IS REQUIRED to include a boolean assertion and an authority source.

**INV-01.** [Name] -- [boolean assertion, e.g., `assignee_id != null when status IN {S-02, S-03}`]. Authority: [business rule / SLA clause / regulation / policy].
**INV-02.** [Name] -- [boolean assertion]. Authority: [source].
*(minimum two; INVARIANT DECLARATIONS IS BLOCKED until two valid entries ARE present)*

---

### VOCABULARY CLOSED [D]

> VOCABULARY CLOSED per C4. States: [list all S-IDs and State Names from STATE DECLARATIONS]. Operations: [list all O-IDs and Operation Names from OPERATION DECLARATIONS]. The vocabulary IS FROZEN. Any state name or operation name not listed above IS PROHIBITED in all subsequent sections. This prohibition IS NOT WAIVABLE.

HANDOFF DECLARATION IS BLOCKED until VOCABULARY IS FROZEN. Any attempt to execute HANDOFF DECLARATION before this declaration IS a C4 violation.

---

### HANDOFF DECLARATION [D]

> **[D] HANDOFF DECLARATION.**
>
> Transferring role IS: [D] (Domain Expert -- [auto-selected domain] expert).
> Receiving role IS: [T] (Trace Developer).
>
> Artifacts transferred ARE: STATE DECLARATIONS (S-01 through S-[N]), OPERATION DECLARATIONS (O-01 through O-[N]), INVARIANT DECLARATIONS (INV-01 through INV-[N]). VOCABULARY IS FROZEN.
>
> **Post-transfer role states (both declared simultaneously upon execution of this HANDOFF DECLARATION):**
> [D] IS PROHIBITED from altering any entry in STATE DECLARATIONS, OPERATION DECLARATIONS, or INVARIANT DECLARATIONS from this point forward. [D]'s modification authority IS REVOKED. This prohibition IS NOT WAIVABLE and IS NOT CONTINGENT on any subsequent action by [T].
> [T] IS NOW AUTHORIZED to produce output in all [T]-owned sections. [T]'s authorization IS CONTINGENT on this HANDOFF DECLARATION having been executed. [T] WAS NOT AUTHORIZED prior to this moment; [T] IS AUTHORIZED now.
>
> Acceptance condition: [T] IS REQUIRED to confirm receipt by writing an explicit Option A or Option B response to INVENTORY CHALLENGE. GATE A IS BLOCKED until this acceptance IS written.
>
> **[D] Signed:** [domain role selected] -- [N] states (S-01 through S-[N]), [N] operations (O-01 through O-[N]), [N] invariants (INV-01 through INV-[N]) ARE DECLARED AND CLOSED.

---

### INVENTORY CHALLENGE

**C7 applies. A blank or non-option response IS a C7 violation. GATE A IS BLOCKED in the presence of a C7 violation.**

INVENTORY IS DECLARED COMPLETE -- the STATE DECLARATIONS and OPERATION DECLARATIONS ARE the complete lifecycle vocabulary for {{topic}}.

**[T] response -- one option IS REQUIRED:**

**Option A (CONFIRMED):** "[T] INVENTORY CONFIRMED. The STATE DECLARATIONS and OPERATION DECLARATIONS ARE the complete lifecycle vocabulary for {{topic}}. No lifecycle state or operation IS absent. States: [repeat S-IDs and names]. Operations: [repeat O-IDs and names]. HANDOFF DECLARATION IS ACKNOWLEDGED. [T]'s authorization IS IN EFFECT. Proceeding to GATE A."

**Option B (GAP FOUND):** "[T] INVENTORY INCOMPLETE. Gap identified: [missing state or operation and why it belongs in the lifecycle]. Returning to [D] for declaration update. VOCABULARY CLOSED MUST be re-declared and HANDOFF DECLARATION re-signed before GATE A IS unblocked."

---

### GATE A

TRANSITION TABLE IS BLOCKED until all items below ARE confirmed. An unconfirmed item IS a blocker per C6.

- [ ] STATE DECLARATIONS ARE complete -- domain vocabulary, inline definitional clauses, at least one Terminal: Yes item IS present
- [ ] OPERATION DECLARATIONS ARE complete -- all S-ID references ARE resolved to STATE DECLARATIONS
- [ ] INVARIANT DECLARATIONS ARE complete -- at least two boolean assertions with authority sources ARE present
- [ ] VOCABULARY CLOSED IS declared -- vocabulary IS FROZEN; prohibition IS in effect
- [ ] HANDOFF DECLARATION IS signed -- post-transfer role states ([D] IS PROHIBITED, [T] IS NOW AUTHORIZED) ARE explicitly declared within the HANDOFF DECLARATION block itself
- [ ] **[C7]** INVENTORY CHALLENGE IS resolved -- Option A or Option B IS written above; no C7 violation IS present
- [ ] **[C-14]** [T] confirms: no name WILL appear in TRANSITION TABLE, INVALID TRANSITIONS, or RACE CONDITIONS that IS NOT declared in STATE DECLARATIONS or OPERATION DECLARATIONS
- [ ] **[C-15]** VOCABULARY CLOSED IS declared and forward-blocking prohibition IS in effect
- [ ] **[C-09]** Terminal states ARE identified in STATE DECLARATIONS; at least one Terminal item WILL appear as From State in INVALID TRANSITIONS

**GATE A IS BLOCKED per C6. TRANSITION TABLE IS BLOCKED until all items ARE confirmed.**

---

### TRANSITION TABLE [T]

Scenario setup: [entity instance, starting state, actor, date/time context]

Constraints C1, C2, C3, C5 ARE in effect. From State and To State MUST use S-IDs. Operation MUST use O-IDs. Prose IS NOT VALID as primary trace output (C3).

| # | From State (S-ID) | Operation (O-ID) | Preconditions | To State (S-ID) | Postconditions | INV-01 | INV-02 | Side Effects |
|---|-------------------|-----------------|---------------|-----------------|----------------|--------|--------|--------------|

- **From State / To State:** S-IDs from STATE DECLARATIONS only (C1).
- **Operation:** O-IDs from OPERATION DECLARATIONS only (C2).
- **Preconditions:** Minimum two testable assertions per row.
- **Postconditions:** Minimum one assertion distinct from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED -- [reason]`; blank IS NOT PERMITTED (C5).
- **Side Effects:** Triggered rules, notifications, async jobs, record changes.

---

### GATE B

INVALID TRANSITIONS IS BLOCKED until all items below ARE confirmed. An unconfirmed item IS a blocker per C8.

- [ ] **[C-08]** TRANSITION TABLE IS columnar and complete; no operation IS documented only in prose
- [ ] **[C-05]** Every row HAS INV status per declared invariant; at least one VIOLATED row IS present
- [ ] **[C-06]** Every row HAS at least one postcondition distinct from the To State name
- [ ] Boundary coverage IS planned -- at least one terminal-state S-ID IS targeted for INVALID TRANSITIONS

**GATE B IS BLOCKED per C8. INVALID TRANSITIONS IS BLOCKED until all items ARE confirmed.**

---

### INVALID TRANSITIONS [T]

| # | Attempted Operation (O-ID) | From State (S-ID) | Blocking Condition | INV Reference | Risk if Bypassed |
|---|---------------------------|------------------|--------------------|--------------|-----------------|

Minimum three rows. At least one row WHERE From State IS a Terminal item from STATE DECLARATIONS IS REQUIRED. S-IDs and O-IDs only (C1, C2).

---

### GATE C

RACE CONDITIONS IS BLOCKED until all items below ARE confirmed. An unconfirmed item IS a blocker per C9.

- [ ] **[C-04]** At least three (operation, state) invalid pairs ARE named with blocking conditions; enumeration IS systematic
- [ ] **[C-09]** At least one INVALID TRANSITIONS row HAS From State = a Terminal item from STATE DECLARATIONS

**GATE C IS BLOCKED per C9. RACE CONDITIONS IS BLOCKED until all items ARE confirmed.**

---

### RACE CONDITIONS [T]

| Operation A (O-ID) | Operation B (O-ID) | Unsafe Interleaving | Outcome | Mitigation |
|--------------------|---------------------|---------------------|---------|-----------|

If no concurrent access: "No concurrent access -- [reason explaining why concurrent access IS NOT POSSIBLE for this object type]."

---

### GATE D

FINDINGS IS BLOCKED until all items below ARE confirmed.

- [ ] **[C-07]** RACE CONDITIONS ARE addressed -- at least one race scenario or explicit clearance with reason IS present
- [ ] All TRANSITION TABLE and INVALID TRANSITIONS S-IDs and O-IDs ARE resolved to STATE DECLARATIONS and OPERATION DECLARATIONS (C1, C2)
- [ ] Hard-stop review IS complete -- no section IS blank or placeholder-only

**GATE D IS BLOCKED. FINDINGS IS BLOCKED until all items ARE confirmed.**

---

### FINDINGS

Priority order. Reference section and item.

- **P[N]:** [title] -- [description, section/item reference]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: ROLES, CONSTRAINT MATRIX, STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, HANDOFF DECLARATION, INVENTORY CHALLENGE, GATE A, TRANSITION TABLE, GATE B, INVALID TRANSITIONS, GATE C, RACE CONDITIONS, GATE D, FINDINGS.

---

## Criterion Coverage Matrix (Predicted)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-08 Columnar table | PASS | PASS | PASS | PASS | PASS |
| C-09 Terminal-state boundary | PASS | PASS | PASS | PASS | PASS |
| C-10 Two mid-doc gates | PASS | PASS | PASS | PASS | PASS |
| C-11 Adversarial challenge | PASS | PASS | PASS | PASS | PASS |
| C-12 Hard-stop phrasing | PASS | PASS | PASS | PASS | PASS |
| C-13 Prose prohibition | PASS | PASS | PASS | PASS | PASS |
| C-14 Referential binding | PASS | PASS | PASS | PASS | PASS |
| C-15 Vocabulary lock | PASS | PASS | PASS | PASS | PASS |
| C-16 Numbered constraint preamble | PASS | PASS | PASS | PASS | PASS |
| C-17 Role-differentiated constraints | PASS | PASS | PASS | PASS | PASS |
| C-18 Per-constraint role mapping | PASS | PASS | PASS | PASS | PASS |
| C-19 Explicit concern taxonomy | PASS | PASS | PASS | PASS | PASS |
| C-20 Sequential gate coverage | PASS | PASS | PASS | PASS | PASS |
| C-21 Challenge non-response violation | PASS | PASS | PASS | PASS | PASS |
| C-22 Explicit handoff declaration | PASS | PASS | PASS | PASS | PASS |
| C-23 Numbered prose inventories | PASS | PASS | PASS | PASS | PASS |
| C-24 IS-phrasing register | **PASS** | FAIL | **PASS** | **PASS** | **PASS** |
| C-25 Vocabulary-locked handoff gate | PASS | PASS | PASS | PASS | PASS |
| C-26 Post-handoff role-state flip | FAIL | **PASS** | **PASS** | **PASS** | **PASS** |
| **Aspirational (v9)** | 18/19 | 18/19 | **19/19** | **19/19** | **19/19** |
| **Composite** | 98.95 | 98.95 | **100.00** | **100.00** | **100.00** |
| **Tier** | Golden | Golden | **Ceiling** | **Ceiling** | **Ceiling** |

**V-01 and V-02:** Single-axis probes confirming C-24 and C-26 are independently achievable on the V-01 base. Golden.
**V-03:** Pairwise synthesis of C-24 + C-26 on V-01 base. First predicted 100.00 using minimal modification from a known Golden variant. Ceiling candidate.
**V-04:** Fresh synthesis with inertia framing. Ceiling candidate via independent architectural path.
**V-05:** ROLES-first structure synthesis. Ceiling candidate testing section-ordering independence of the synthesis.
