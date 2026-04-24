# trace-state — Round 17 Variations (R17)
# Skill: trace-state | Date: 2026-03-15 | Rubric: v15

Five complete, runnable skill body prompt variations for `trace-state`.
Each variation is a complete prompt body -- not a diff.

---

## R17 Gap Analysis

From R16 under v15 rubric (38 aspirational criteria C-09..C-47):

| Criterion | Status in R16 V-01..V-05 | R17 Path |
|-----------|--------------------------|----------|
| C-45 (defect-entry state-triple decomposition) | ABSENT in all R16 variants | Add structured Pre-Defect State / Triggering Operation / Post-Defect State+Reason block with independent state triples to FINDINGS in all variations |
| C-46 (phase vocabulary declaration before trace) | ABSENT in all R16 variants | Add per-domain PHASE VOCABULARY DECLARATION section before TRANSITION TABLE/TRANSITION STEPS in all variations |
| C-47 (defect-hypothesis confirmation annotation) | ABSENT in all R16 variants (requires C-40+C-41+C-42) | Add per-pass defect confirmation note naming the C-42 defect class and C-41 bridge row in multi-pass variations (V-02, V-04, V-05) |
| C-38/C-39 (step-block format) | FAIL in all R16 variants (tabular format used) | Introduce step-block format in V-04 (combined) and V-05 (synthesis) |

**R16 ceiling under v15:** C-45/C-46/C-47 all absent; C-38/C-39 structurally excluded by tabular format.

**R17 objective:** Hold all prior criteria AND add C-45/C-46 to all five variations as standard; add C-47 to multi-pass variations (V-02, V-04, V-05); introduce step-block format in V-04/V-05 to unlock C-38/C-39.

---

## Variation Axis Map

| Variation | Axis | Domain | Key Probe | C-45 | C-46 | C-47 | C-38/C-39 |
|-----------|------|--------|-----------|------|------|------|-----------|
| V-01 | Phrasing register — IS-negation density in all sections | Sales | Dense IS-negation register throughout: does phrasing carry criteria without structural change? | PASS | PASS | N/A (single-pass) | FAIL (tabular) |
| V-02 | Role sequence — Finance-first multi-pass | Finance/Sales/CS | Finance-first ordering as hypothesis vehicle (C-42); C-47 confirmation annotation closes the circuit | PASS | PASS | PASS | FAIL (tabular) |
| V-03 | Lifecycle emphasis — expanded phase vocabulary | Customer Service | 8-phase CS domain; C-46 declaration covers phases absent from the trace (completeness verifiable) | PASS | PASS | N/A (single-pass) | FAIL (tabular) |
| V-04 | Role sequence x output format — step-block multi-pass | Finance | Step-block format with fused labels (C-38/C-39) + multi-pass (C-47) | PASS | PASS | PASS | PASS |
| V-05 | Full synthesis — all probes + new domain | E-commerce | C-45+C-46+C-47+C-38/C-39 all held; domain portability confirmed | PASS | PASS | PASS | PASS |

---

## V-01 — Phrasing Register: IS-Negation Density (Sales)

**Variation axis:** Phrasing register
**Hypothesis:** Dense IS-negation phrasing throughout all sections (INERTIA BASELINE, ROLES, GATES, FINDINGS) carries all prior criteria AND C-45/C-46 without structural change. The phrasing register itself becomes a structural signal. Single-pass tabular format. C-47 N/A. Predicted ceiling gain: C-45 + C-46.
**Domain:** Sales (Lead / Qualified / Proposed / Negotiating / Closed-Won / Closed-Lost)
**New probes:** C-45 (defect-entry state-triple decomposition in FINDINGS), C-46 (PHASE VOCABULARY DECLARATION before TRANSITION TABLE)

---

### INERTIA BASELINE

The alternative to this trace IS: implement {{topic}} state management without hand-compiling transitions and invariants. The failure mode that alternative creates IS NOT a theoretical gap; it IS a revenue record in an invalid state discovered by a quarterly audit. This trace exists to close that gap before code is written. Every section left blank or abbreviated IS NOT deferred work; it IS the inertia baseline already instantiated.

**PRODUCTION COST DECLARATION.** The production cost of the inertia baseline IS: sales pipeline records enter invalid state sequences -- opportunities advance past qualification gates without approval records, closed-won deals reopen without executive override, lost opportunities appear active in revenue forecasts. The cost IS NOT a misrouted lead; the cost IS a revenue record in a state the system should have blocked. This IS NOT a risk to be accepted; this IS the specific failure this trace exists to prevent.

**IS-NEGATION PAIR.** The inertia baseline IS NOT a process gap; it IS a revenue integrity failure mode in the absence of this artifact. Choosing not to produce this trace IS NOT a risk accepted; it IS the failure mode instantiated before the feature ships. The existence of this document IS NOT documentation; it IS the artifact that converts that certainty into a prevented outcome.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. This trace IS a formal artifact; its governing document IS the CONSTRAINT MATRIX below. A Domain Expert [D] declares the vocabulary phase; a Trace Developer [T] executes the trace phase. [T]'s authorization IS CONTINGENT on [D] completing and executing a HANDOFF DECLARATION. The INERTIA BASELINE above IS the structural frame for this entire document. The CONSTRAINT MATRIX IS authoritative. Read it completely before producing any output.

---

### CONSTRAINT MATRIX

**MATRIX AUTHORITY.** The CONSTRAINT MATRIX IS the governing authority for this trace and IS NOT AMENDABLE by [D] or [T]. A constraint not named in this matrix IS NOT binding. A violation not classifiable by a named constraint IS NOT a violation under this matrix. The scope of this matrix IS total.

| ID | Architectural Fact | Assigned Role | Concern |
|----|--------------------|---------------|---------|
| C1 | A state name not declared in STATE DECLARATIONS IS PROHIBITED in any trace table | [T] | vocabulary |
| C2 | An operation name not declared in OPERATION DECLARATIONS IS PROHIBITED in any trace table | [T] | vocabulary |
| C3 | The TRANSITION TABLE includes an EPOCH column. EPOCH IS informational; IS NOT constrained by C1/C2. EPOCH values ARE drawn from Sales lifecycle phase vocabulary (PIPELINE / ACTIVE / CLOSE-TRACK / RESOLUTION). Prose and bullet lists ARE NOT VALID as primary trace output; every operation IS REQUIRED as a table row. | [T] | format |
| C4 | Any state or operation added after VOCABULARY CLOSED IS declared IS a retroactive violation; such additions ARE PROHIBITED | [D] | ordering |
| C5 | A blank invariant status cell IS NOT PERMITTED; every cell IS REQUIRED to contain HOLDS or VIOLATED | [T] | integrity |
| C6 | TRANSITION TABLE IS BLOCKED until GATE A IS confirmed AND INVARIANT-VIOLATION FORECAST IS complete | [T] | ordering |
| C7 | A blank or non-option response at INVENTORY CHALLENGE IS a C7 violation; GATE A IS BLOCKED in the presence of a C7 violation | [T] | completeness |
| C8 | INVALID TRANSITIONS IS BLOCKED until GATE B IS confirmed | [T] | ordering |
| C9 | RACE CONDITIONS IS BLOCKED until GATE C IS confirmed | [T] | ordering |
| C10 | STATE DIAGRAM [D] IS NOT a substitute for the TRANSITION TABLE; it IS the structural cross-check artifact. [D] IS REQUIRED to declare node count, edge count, and [!] annotation count. A [!] IS REQUIRED on every edge whose operation IS predicted VIOLATED. A forecast row predicting VIOLATED without a corresponding [!] IS a C10 violation. | [D] | integrity |

---

### ROLES

**[D] Domain Expert**
Auto-selected: Sales expert (Lead / Qualified / Proposed / Negotiating / Closed-Won / Closed-Lost).
Sections owned by [D]: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, PHASE VOCABULARY DECLARATION, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION.
Binding constraint: **C4** (vocabulary IS FROZEN after VOCABULARY CLOSED IS declared; retroactive additions ARE PROHIBITED).
INERTIA BASELINE relationship: [D]'s incomplete declarations ARE NOT a deferral; they ARE the inertia baseline instantiated. The specific regression form [D] prevents IS: unvalidated state vocabulary reaching the trace phase. An incomplete PHASE VOCABULARY DECLARATION IS NOT a minor omission; it IS the elimination of completeness-verifiability for all lifecycle-phase annotations in the trace.

**[T] Trace Developer**
Sections owned by [T]: INVENTORY CHALLENGE response, INVARIANT-VIOLATION FORECAST, TRANSITION TABLE, LIFECYCLE EPOCH MAP, FORECAST VALIDATION, INVALID TRANSITIONS, RACE CONDITIONS, FINDINGS.
Binding constraints: **C1, C2, C3, C5, C6, C7, C8, C9, C10**.
Authorization status: [T]'s authorization IS CONTINGENT on HANDOFF DECLARATION. Prior to HANDOFF DECLARATION, [T] IS NOT AUTHORIZED to produce output in any [T]-owned section.
INERTIA BASELINE relationship: A blank [T] section IS NOT an in-progress state; it IS the inertia baseline already chosen. The specific regression form [T] prevents IS: untraced transitions shipping as assumed-valid precondition logic.

---

### STATE DECLARATIONS [D]

Declare all lifecycle states as numbered prose items with inline definitional clauses. Each entry IS REQUIRED to name: (a) conditions causing entry, (b) characterizing field values, (c) terminal status. Generic labels ARE PROHIBITED; Sales vocabulary IS REQUIRED.

**S-01.** [State Name] -- [inline definitional clause]. Terminal: Yes/No.
**S-02.** [State Name] -- [inline definitional clause]. Terminal: Yes/No.
*(continue; Sales typical set: Lead, Qualified, Proposed, Negotiating, Closed-Won, Closed-Lost)*

A STATE DECLARATIONS section without at least one Terminal: Yes entry IS INCOMPLETE.

---

### OPERATION DECLARATIONS [D]

Declare all lifecycle operations as numbered prose items. Each entry IS REQUIRED to name: (a) what the operation does, (b) when triggered, (c) all legal source S-IDs, (d) target S-ID.

**O-01.** [Operation Name] -- [inline definitional clause]. From: S-[N]. To: S-[N]. Actor: [role/system].
*(continue for all lifecycle operations)*

---

### INVARIANT DECLARATIONS [D]

**INV-01.** [Name] -- [boolean assertion]. Authority: [source].
**INV-02.** [Name] -- [boolean assertion]. Authority: [source].
*(minimum two; each IS REQUIRED to include a boolean assertion and authority source)*

---

### PHASE VOCABULARY DECLARATION [D]

**This declaration IS NOT a trace artifact; it IS the vocabulary source that makes lifecycle-phase annotation completeness verifiable. [T]'s use of `[phase: X]` labels in TRANSITION TABLE state cells IS NOT valid unless X appears in this declaration. A phase label absent from this declaration IS NOT a C1 violation; it IS NOT permitted as a `[phase: X]` annotation. The TRANSITION TABLE IS BLOCKED until this declaration IS complete.**

Declare all lifecycle phases per domain in sequence. Phases not appearing in the trace ARE still required here; their absence from the trace IS a coverage note, not a gap.

**Sales lifecycle arc:** Lead-Identification → Qualification → Solution-Development → Negotiation → Close → Post-Close
*(Terminal phases: Closed-Won, Closed-Lost)*

> [D] declares: Sales lifecycle phases in sequence as above. Every `[phase: X]` label in [T]'s TRANSITION TABLE state cells IS traceable to this declaration. A phase not listed IS NOT usable as a `[phase: X]` annotation.

---

### VOCABULARY CLOSED [D]

> VOCABULARY CLOSED per C4. States: [list all S-IDs and State Names]. Operations: [list all O-IDs and Operation Names]. The vocabulary IS FROZEN. Any state or operation name not listed above IS PROHIBITED in all subsequent sections. This prohibition IS NOT WAIVABLE.

HANDOFF DECLARATION IS BLOCKED until VOCABULARY IS FROZEN.

---

### STATE DIAGRAM [D]

This STATE DIAGRAM IS NOT a substitute for the TRANSITION TABLE; it IS the structural cross-check artifact. Nodes: one per S-ID. Edges: one per valid (From, Operation) pair. **[!] annotation:** on every edge whose operation IS predicted VIOLATED in INVARIANT-VIOLATION FORECAST.

**Nodes:**
- S-[NN]: [State Name] *(Terminal)* or *(Non-terminal)*

**Edges:**
- S-[NN] --[O-NN: Operation Name]--> S-[NN] [optional: [!] INVARIANT RISK: reason]

**Structural counts:**
- Node count: [N] (MUST equal S-ID count)
- Edge count: [N] (MUST equal total valid From/To pairs)
- [!] annotation count: [N] (MUST equal count of VIOLATED-predicted rows in INVARIANT-VIOLATION FORECAST)

---

### HANDOFF DECLARATION [D]

> **[D] HANDOFF DECLARATION.**
>
> **TRANSFER DECLARATION.** This HANDOFF IS NOT a coordination event; it IS the formal instantiation of production responsibility transfer. [D]'s declaration authority IS extinguished at this moment; [T]'s trace authorization IS created at this moment.
>
> Transferring role IS: [D] (Domain Expert -- Sales expert).
> Receiving role IS: [T] (Trace Developer).
>
> Artifacts transferred ARE:
> 1. STATE DECLARATIONS (S-01 through S-[N])
> 2. OPERATION DECLARATIONS (O-01 through O-[N])
> 3. INVARIANT DECLARATIONS (INV-01 through INV-[N])
> 4. PHASE VOCABULARY DECLARATION: Sales lifecycle arc declared. [T]'s `[phase: X]` labels ARE constrained to this declaration. A `[phase: X]` label not traceable to this declaration IS NOT PERMITTED.
> 5. STATE DIAGRAM [D]: Node count: [N]. Edge count: [N]. [!] annotation count: [N]. This IS NOT a substitute for the TRANSITION TABLE; it IS the structural cross-check.
>
> **Post-transfer role states:**
> [D] IS PROHIBITED from altering any declaration from this point forward. [D]'s modification authority IS REVOKED. This prohibition IS NOT WAIVABLE.
> [T] IS NOW AUTHORIZED to produce output in all [T]-owned sections. [T] WAS NOT AUTHORIZED prior to this moment.
>
> Acceptance condition: [T] IS REQUIRED to write an explicit Option A or Option B response to INVENTORY CHALLENGE before GATE A IS cleared.
>
> **[D] Signed:** Sales expert -- [N] states, [N] operations, [N] invariants, PHASE VOCABULARY DECLARATION (Sales arc declared), STATE DIAGRAM ([N] nodes, [N] edges, [N] [!] annotations) ARE DECLARED AND CLOSED.

---

### INVENTORY CHALLENGE

**C7 applies. A blank or non-option response IS a C7 violation. GATE A IS BLOCKED in the presence of a C7 violation.**

INVENTORY IS DECLARED COMPLETE -- the STATE DECLARATIONS and OPERATION DECLARATIONS contain every state and operation in the lifecycle of {{topic}}.

**[T] response -- one option IS REQUIRED:**

**Option A (CONFIRMED):** "[T] INVENTORY CONFIRMED. States: [S-IDs and names]. Operations: [O-IDs and names]. HANDOFF DECLARATION IS ACKNOWLEDGED. Proceeding to GATE A."

**Option B (GAP FOUND):** "[T] INVENTORY INCOMPLETE. Gap identified: [missing state or operation]. Returning to [D] for declaration update."

---

### GATE A

- [ ] INERTIA BASELINE IS present -- PRODUCTION COST DECLARATION and IS-NEGATION PAIR both present
- [ ] CONSTRAINT MATRIX IS-authority preamble IS present
- [ ] ROLES section carries per-role IS-negation obligation pair with specific regression form named
- [ ] STATE DECLARATIONS ARE complete -- domain vocabulary, inline definitional clauses, Terminal: Yes present
- [ ] OPERATION DECLARATIONS ARE complete -- all S-ID references resolved
- [ ] INVARIANT DECLARATIONS ARE complete -- minimum two boolean assertions with authority sources
- [ ] PHASE VOCABULARY DECLARATION IS complete -- Sales lifecycle arc declared in sequence before trace; all phases named including those not appearing in trace rows
- [ ] VOCABULARY CLOSED IS declared -- vocabulary IS FROZEN; prohibition IS NOT WAIVABLE
- [ ] STATE DIAGRAM IS complete -- node count, edge count, [!] annotation count declared and consistent
- [ ] HANDOFF DECLARATION IS signed -- TRANSFER DECLARATION present; PHASE VOCABULARY DECLARATION named as transferred artifact; post-transfer role states explicitly declared
- [ ] **[C7]** INVENTORY CHALLENGE IS resolved -- Option A or B written
- [ ] [T] confirms: no name WILL appear in any trace table not declared in STATE DECLARATIONS or OPERATION DECLARATIONS

**GATE A: [T] IS BLOCKED. INVARIANT-VIOLATION FORECAST IS BLOCKED until all items ARE confirmed.**

---

### INVARIANT-VIOLATION FORECAST [T]

**TRANSITION TABLE IS BLOCKED until this forecast IS complete per C6.**

| O-ID | Operation Name | Predicted INV-01 | Predicted INV-02 | Rationale |
|------|----------------|-----------------|-----------------|-----------|
| O-[N] | [name] | HOLDS / VIOLATED | HOLDS / VIOLATED | [why] |
*(one row per declared operation; blanks ARE NOT PERMITTED)*

---

### TRANSITION TABLE [T]

Scenario setup: [entity instance, starting state, actor, date/time context]

Constraints C1, C2, C3, C5 ARE in effect. EPOCH column IS informational per C3. State cells carry `[phase: X]` annotations traceable to PHASE VOCABULARY DECLARATION.

| # | From State (S-ID) [phase: X] | Operation (O-ID) | Preconditions | To State (S-ID) [phase: X] | Postconditions | INV-01 | INV-02 | EPOCH | Side Effects |
|---|------------------------------|-----------------|---------------|---------------------------|----------------|--------|--------|-------|--------------|

- **From/To State:** S-IDs only (C1). `[phase: X]` label IS REQUIRED; X MUST appear in PHASE VOCABULARY DECLARATION (C-46).
- **Operation:** O-IDs only (C2).
- **EPOCH:** Sales phase label per C3; IS NOT constrained by C1/C2.
- **Preconditions:** Minimum two testable assertions per row.
- **Postconditions:** Minimum one assertion distinct from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED -- [reason]`; blank IS NOT PERMITTED (C5).

---

### LIFECYCLE EPOCH MAP [T]

| O-ID | Operation Name | Lifecycle Epoch | Epoch Rationale |
|------|----------------|-----------------|-----------------|
| O-[N] | [from OPERATION DECLARATIONS] | PIPELINE / ACTIVE / CLOSE-TRACK / RESOLUTION | [why] |

---

### FORECAST VALIDATION [T]

| O-ID | Predicted INV-01 | Actual INV-01 | Predicted INV-02 | Actual INV-02 | Forecast Status |
|------|-----------------|--------------|-----------------|--------------|-----------------|
| O-[N] | [forecast] | [actual] | [forecast] | [actual] | CONFIRMED / REFUTED -- [explanation] |

A REFUTED forecast IS a required finding in FINDINGS.

---

### GATE B

- [ ] TRANSITION TABLE IS columnar and complete; no operation documented only in prose
- [ ] Every row HAS INV status per declared invariant; at least one VIOLATED row IS present
- [ ] Every row HAS at least one postcondition distinct from the To State name
- [ ] All `[phase: X]` labels in state cells ARE traceable to PHASE VOCABULARY DECLARATION
- [ ] LIFECYCLE EPOCH MAP IS complete
- [ ] FORECAST VALIDATION IS complete; REFUTED rows flagged as findings
- [ ] Boundary coverage IS planned -- at least one terminal S-ID targeted for INVALID TRANSITIONS

**GATE B: [T] IS BLOCKED. INVALID TRANSITIONS IS BLOCKED until all items ARE confirmed.**

---

### INVALID TRANSITIONS [T]

| # | Attempted Operation (O-ID) | From State (S-ID) | Blocking Condition | INV Reference | Risk if Bypassed |
|---|---------------------------|------------------|--------------------|--------------|-----------------|

Minimum three rows. At least one row WHERE From State IS a Terminal item IS REQUIRED.

---

### GATE C

- [ ] At least three (operation, state) invalid pairs ARE named with blocking conditions
- [ ] At least one INVALID TRANSITIONS row HAS From State = a Terminal item

**GATE C: [T] IS BLOCKED. RACE CONDITIONS IS BLOCKED until all items ARE confirmed.**

---

### RACE CONDITIONS [T]

| Operation A (O-ID) | Operation B (O-ID) | Unsafe Interleaving | Outcome | Mitigation |
|--------------------|---------------------|---------------------|---------|-----------|

If no concurrent access: "No concurrent access -- [reason why concurrent access IS NOT POSSIBLE for this object type]."

---

### GATE D

- [ ] RACE CONDITIONS ARE addressed
- [ ] FORECAST VALIDATION IS included; REFUTED forecasts flagged
- [ ] LIFECYCLE EPOCH MAP IS included
- [ ] All S-IDs and O-IDs resolved to declarations
- [ ] No section IS blank or placeholder-only

**GATE D: [T] IS BLOCKED. FINDINGS IS BLOCKED until all items ARE confirmed.**

---

### FINDINGS [T]

**FINDINGS IS NOT an observation log; it IS the derivation layer.** A finding IS NOT valid unless traceable to a named record in TRANSITION TABLE, INVALID TRANSITIONS, FORECAST VALIDATION, or RACE CONDITIONS.

**Defect-entry format IS REQUIRED (C-45).** Each finding MUST decompose into three sub-steps each carrying an independent state triple. A finding without this decomposition IS NOT a valid finding entry.

Priority order. REFUTED forecast rows ARE required findings.

- **P[N]: [title]**
  **Pre-Defect State:** `[S-ID: state name | phase: X | key fields: field=value, field=value]`
  **Triggering Operation:** `[O-ID: operation name]` -- [which precondition was absent or bypassed; why the operation was permitted when invariant conditions were unmet]
  **Post-Defect State+Reason:** `[S-ID: resulting state name | phase: X | INV-NN: VIOLATED because reason]`
  State-triple: Before=[S-ID] --[O-ID]--> After=[S-ID] (invariant VIOLATED)
  Source: [TRANSITION TABLE row N / INVALID TRANSITIONS row N / FORECAST VALIDATION O-[N]]
  Inertia connection: [how this finding traces to the INERTIA BASELINE failure mode; a finding without this field IS background noise]
  Severity: FATAL / DEGRADED / COSMETIC.

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: INERTIA BASELINE, CONSTRAINT MATRIX, ROLES, STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, PHASE VOCABULARY DECLARATION, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION, INVENTORY CHALLENGE, GATE A, INVARIANT-VIOLATION FORECAST, TRANSITION TABLE, LIFECYCLE EPOCH MAP, FORECAST VALIDATION, GATE B, INVALID TRANSITIONS, GATE C, RACE CONDITIONS, GATE D, FINDINGS.

---

## V-02 — Role Sequence: Finance-First Multi-Pass with C-47 Confirmation (Finance/Sales/CS)

**Variation axis:** Role sequence (which domain runs first, multi-pass ordering as hypothesis vehicle)
**Hypothesis:** Finance-first ordering targets revenue-leak defect class in Pass 1; Sales in Pass 2 surfaces commitment-gap defects; CS in Pass 3 surfaces service-state defects. C-42 pass headings annotate WHY each domain occupies its position. C-47 confirmation annotations in each pass defect entry close the hypothesis circuit by naming the C-42 predicted class and citing the C-41 bridge row. C-45 and C-46 standard. Predicted: all prior + C-45 + C-46 + C-47.
**Domain:** Finance (Draft/Pending-Approval/Approved/Posted/Archived) leading; Sales handoff; CS resolution
**New probes:** C-47 (defect-hypothesis confirmation annotation with C-40+C-41+C-42 prerequisites)

---

### INERTIA BASELINE

The alternative to this trace IS: implement {{topic}} state management without hand-compiling cross-domain transitions and invariants. The failure mode that alternative creates IS: Finance approves a record that Sales has already marked committed, or CS resolves a case whose Finance record IS still pending -- the cross-domain precondition chain IS assumed rather than enumerated. This trace exists to close that gap before code is written.

**PRODUCTION COST DECLARATION.** The production cost of the inertia baseline IS: Finance records transition to Posted while Sales commitment records are absent; CS closure records appear resolved while Finance approval records are still Draft. The cost IS NOT a reporting inconsistency; the cost IS a revenue record in a state that another domain's invariant should have blocked, discovered by a reconciliation run rather than by the application.

**IS-NEGATION PAIR.** The inertia baseline IS NOT a workflow gap; it IS a cross-domain state integrity failure mode. Choosing not to produce this trace IS NOT a risk accepted; it IS the failure mode instantiated before the feature ships.

---

You are running a **trace-state** signal for: {{topic}}

Produce a multi-pass state machine trace. Three domain passes run in sequence: **Pass 1 (Finance)**, **Pass 2 (Sales)**, **Pass 3 (CS)**. The pass ordering IS the hypothesis vehicle: Finance runs first because Finance-first ordering IS predicted to surface revenue-leak defects before commitment-gap defects. A Domain Expert [D] declares the vocabulary phase; a Trace Developer [T] executes all three passes. The CONSTRAINT MATRIX IS authoritative. Read it completely before producing any output.

---

### CONSTRAINT MATRIX

**MATRIX AUTHORITY.** The CONSTRAINT MATRIX IS the governing authority for this trace and IS NOT AMENDABLE by [D] or [T].

| ID | Architectural Fact | Assigned Role | Concern |
|----|--------------------|---------------|---------|
| C1 | A state name not declared in STATE DECLARATIONS IS PROHIBITED in any trace table | [T] | vocabulary |
| C2 | An operation name not declared in OPERATION DECLARATIONS IS PROHIBITED in any trace table | [T] | vocabulary |
| C3 | EPOCH columns ARE informational per domain (FINANCE-PHASE / SALES-PHASE / CS-PHASE); IS NOT constrained by C1/C2. Every operation IS REQUIRED as a table row in its domain pass table. | [T] | format |
| C4 | Any state or operation added after VOCABULARY CLOSED IS declared IS a retroactive violation | [D] | ordering |
| C5 | A blank invariant status cell IS NOT PERMITTED; every cell IS REQUIRED to contain HOLDS or VIOLATED | [T] | integrity |
| C6 | Each pass TRANSITION TABLE IS BLOCKED until its pass GATE A IS confirmed | [T] | ordering |
| C7 | A blank or non-option response at INVENTORY CHALLENGE IS a C7 violation | [T] | completeness |
| C8 | INVALID TRANSITIONS IS BLOCKED until GATE B IS confirmed | [T] | ordering |
| C9 | RACE CONDITIONS IS BLOCKED until GATE C IS confirmed | [T] | ordering |
| C10 | STATE DIAGRAM IS the structural cross-check artifact; [!] IS REQUIRED on every edge predicted VIOLATED | [D] | integrity |
| C11 | A cross-domain BRIDGE TABLE IS REQUIRED between each adjacent pass. Pass 2 IS BLOCKED until Pass 1 BRIDGE TABLE IS written. Pass 3 IS BLOCKED until Pass 2 BRIDGE TABLE IS written. A bridge row IS REQUIRED for every postcondition in Pass N that IS a precondition in Pass N+1. | [T] | ordering |

---

### ROLES

**[D] Domain Expert**
Auto-selected: Finance expert (primary), Sales expert (secondary), CS expert (tertiary).
Sections owned by [D]: STATE DECLARATIONS (all three domains), OPERATION DECLARATIONS (all three domains), INVARIANT DECLARATIONS, PHASE VOCABULARY DECLARATION (all three domains), VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION.
Binding constraint: **C4**. The specific regression form [D] prevents IS: undeclared cross-domain state vocabulary producing untraceable pass transitions.

**[T] Trace Developer**
Sections owned by [T]: INVENTORY CHALLENGE, Pass 1 trace (INVARIANT-VIOLATION FORECAST, TRANSITION TABLE, FINDINGS), BRIDGE TABLE 1→2, Pass 2 trace, BRIDGE TABLE 2→3, Pass 3 trace, INVALID TRANSITIONS, RACE CONDITIONS, AGGREGATE FINDINGS.
Authorization status: [T]'s authorization IS CONTINGENT on HANDOFF DECLARATION.

---

### STATE DECLARATIONS [D]

Declare states for all three domains. Use domain prefixes (F-NN for Finance, S-NN for Sales, C-NN for CS).

**Finance states:**
**F-01.** [State Name] -- [inline definitional clause]. Terminal: Yes/No.
*(Finance typical: Draft, Pending-Approval, Approved, Posted, Archived)*

**Sales states:**
**S-01.** [State Name] -- [inline definitional clause]. Terminal: Yes/No.
*(Sales typical: Lead, Qualified, Proposed, Negotiating, Closed-Won, Closed-Lost)*

**CS states:**
**C-01.** [State Name] -- [inline definitional clause]. Terminal: Yes/No.
*(CS typical: New, Assigned, In-Progress, Resolved, Closed)*

Each domain MUST have at least one Terminal: Yes entry.

---

### OPERATION DECLARATIONS [D]

Declare operations for all three domains with domain prefixes (FO-NN, SO-NN, CO-NN).

**Finance operations:**
**FO-01.** [Operation Name] -- [clause]. From: F-[N]. To: F-[N]. Actor: [role].

**Sales operations:**
**SO-01.** [Operation Name] -- [clause]. From: S-[N]. To: S-[N]. Actor: [role].

**CS operations:**
**CO-01.** [Operation Name] -- [clause]. From: C-[N]. To: C-[N]. Actor: [role].

---

### INVARIANT DECLARATIONS [D]

Declare invariants per domain. Cross-domain invariants ARE permitted and ENCOURAGED.

**INV-F-01.** [Finance invariant] -- [boolean assertion]. Authority: [source].
**INV-S-01.** [Sales invariant] -- [boolean assertion]. Authority: [source].
**INV-C-01.** [CS invariant] -- [boolean assertion]. Authority: [source].
**INV-X-01.** [Cross-domain invariant] -- [boolean assertion]. Authority: [source].
*(minimum two per domain plus at least one cross-domain)*

---

### PHASE VOCABULARY DECLARATION [D]

**This declaration IS the vocabulary source for all `[phase: X]` labels across all three domain pass tables. A phase label not declared here IS NOT usable as a `[phase: X]` annotation in any pass table. The Pass 1 TRANSITION TABLE IS BLOCKED until this declaration IS complete.**

**Finance lifecycle arc:** Draft → Pending-Approval → Approved → Posted → Archived
*(Terminal: Archived)*

**Sales lifecycle arc:** Lead-Identification → Qualification → Solution-Development → Negotiation → Close → Post-Close
*(Terminal: Closed-Won, Closed-Lost)*

**Customer Service lifecycle arc:** Intake → Assignment → Investigation → Resolution → Verification → Closure
*(Terminal: Closed)*

> [D] declares: all three domain lifecycle arcs above. Every `[phase: X]` label in [T]'s pass TRANSITION TABLES IS traceable to this declaration. Phases declared but absent from a pass table ARE a coverage note, not a gap.

---

### VOCABULARY CLOSED [D]

> VOCABULARY CLOSED per C4. Finance states: [F-IDs and names]. Sales states: [S-IDs and names]. CS states: [C-IDs and names]. Finance operations: [FO-IDs and names]. Sales operations: [SO-IDs and names]. CS operations: [CO-IDs and names]. The vocabulary IS FROZEN. Any name not listed IS PROHIBITED. This prohibition IS NOT WAIVABLE.

---

### STATE DIAGRAM [D]

Produce three domain sub-diagrams (Finance, Sales, CS) each as annotated edge lists with structural counts. Cross-domain dependency edges (Finance.Approved → Sales.Commit trigger) ARE documented as BRIDGE EDGES and ARE annotated with the downstream domain they feed.

*(structure same as V-01 STATE DIAGRAM; [!] annotations per INVARIANT-VIOLATION FORECAST for each domain)*

---

### HANDOFF DECLARATION [D]

> **[D] HANDOFF DECLARATION.**
>
> **TRANSFER DECLARATION.** This HANDOFF IS NOT a coordination event; it IS the formal instantiation of production responsibility transfer across three domains.
>
> Artifacts transferred ARE:
> 1. STATE DECLARATIONS (F-01..F-[N], S-01..S-[N], C-01..C-[N])
> 2. OPERATION DECLARATIONS (FO-01..FO-[N], SO-01..SO-[N], CO-01..CO-[N])
> 3. INVARIANT DECLARATIONS (INV-F-NN, INV-S-NN, INV-C-NN, INV-X-NN)
> 4. PHASE VOCABULARY DECLARATION: Finance arc, Sales arc, CS arc -- all phases declared. [T]'s `[phase: X]` labels ARE constrained to this declaration.
> 5. STATE DIAGRAM: Three domain sub-diagrams with structural counts and cross-domain BRIDGE EDGES.
>
> **Post-transfer role states:**
> [D] IS PROHIBITED from altering any declaration from this point forward.
> [T] IS NOW AUTHORIZED to produce Pass 1, BRIDGE TABLE 1→2, Pass 2, BRIDGE TABLE 2→3, Pass 3, INVALID TRANSITIONS, RACE CONDITIONS, AGGREGATE FINDINGS.
>
> **[D] Signed:** Finance/Sales/CS expert -- [N]+[N]+[N] states, [N]+[N]+[N] operations, [N] invariants, PHASE VOCABULARY DECLARATION (three domain arcs declared), STATE DIAGRAM (three sub-diagrams) ARE DECLARED AND CLOSED.

---

### INVENTORY CHALLENGE

*(same structure as V-01; [T] confirms all three domain state/operation sets are complete)*

---

### GATE A (Multi-Pass)

- [ ] INERTIA BASELINE IS present with PRODUCTION COST DECLARATION and IS-NEGATION PAIR
- [ ] CONSTRAINT MATRIX with C11 (cross-domain BRIDGE TABLE requirement) IS present
- [ ] ROLES section IS present with per-role obligation pair
- [ ] STATE DECLARATIONS complete for all three domains -- domain prefixes used, Terminal: Yes per domain
- [ ] OPERATION DECLARATIONS complete for all three domains -- S-ID references resolved within domain
- [ ] INVARIANT DECLARATIONS complete -- per-domain + cross-domain invariants present
- [ ] PHASE VOCABULARY DECLARATION IS complete -- all three domain lifecycle arcs declared in sequence
- [ ] VOCABULARY CLOSED IS declared
- [ ] STATE DIAGRAM IS complete -- three sub-diagrams with structural counts and BRIDGE EDGES
- [ ] HANDOFF DECLARATION IS signed -- PHASE VOCABULARY DECLARATION named as transferred artifact; post-transfer role states declared
- [ ] **[C7]** INVENTORY CHALLENGE IS resolved
- [ ] Pass ordering IS declared as hypothesis vehicle: Finance-first IS predicted to surface revenue-leak defect class (C-42)

**GATE A: [T] IS BLOCKED. Pass 1 TRANSITION TABLE IS BLOCKED until all items ARE confirmed.**

---

### PASS 1: Finance

**Pass 1 Heading [C-42 ordering annotation]:** Finance runs first because Finance-first ordering IS the hypothesis vehicle for revenue-leak defect class. Predicted defect class: **revenue-state integrity failure** -- a Finance state advance occurring without a corresponding Sales commitment record. Finance transition data IS the precondition source for Sales Pass 2 via BRIDGE TABLE 1→2.

#### Pass 1 Invariant-Violation Forecast [T]

| FO-ID | Operation Name | Predicted INV-F-01 | Predicted INV-X-01 | Rationale |
|-------|----------------|-------------------|-------------------|-----------|
| FO-[N] | [name] | HOLDS / VIOLATED | HOLDS / VIOLATED | [why] |

#### Pass 1 Transition Table [T]

| # | From State (F-ID) [phase: X] | Operation (FO-ID) | Preconditions | To State (F-ID) [phase: X] | Postconditions | INV-F-01 | INV-X-01 | EPOCH | Side Effects |
|---|------------------------------|-------------------|---------------|---------------------------|----------------|----------|----------|-------|--------------|

State cells: `[phase: X]` traceable to PHASE VOCABULARY DECLARATION Finance arc.

#### Pass 1 Forecast Validation [T]

*(same structure as V-01 FORECAST VALIDATION, Finance operations only)*

#### Pass 1 Findings [T]

**Defect-entry format IS REQUIRED (C-45).**

- **F-P[N]: [title]**
  **Pre-Defect State:** `[F-ID: state name | phase: X | key fields: field=value]`
  **Triggering Operation:** `[FO-ID: operation name]` -- [precondition absent/bypassed]
  **Post-Defect State+Reason:** `[F-ID: resulting state | phase: X | INV-F-NN: VIOLATED because reason]`
  State-triple: Before=[F-ID] --[FO-ID]--> After=[F-ID] (invariant VIOLATED)
  **Defect-hypothesis confirmation (C-47):** Confirms [exact defect class quoted from Pass 1 heading C-42 annotation: "revenue-state integrity failure"] (C-42 prediction: Pass 1 heading) -- exposed by bridge row [specific Finance.field → Sales.field dependency from BRIDGE TABLE 1→2 row reference] from C-11 cross-domain bridge table.
  Source: [Pass 1 TRANSITION TABLE row N]
  Inertia connection: [how this finding traces to the INERTIA BASELINE failure mode]
  Severity: FATAL / DEGRADED / COSMETIC.

---

### BRIDGE TABLE 1→2 [T] (C-41)

**BRIDGE TABLE IS NOT a summary; it IS the formal cross-domain precondition transfer record. Pass 2 IS BLOCKED per C11 until this table IS complete. A postcondition in Pass 1 that seeds a precondition in Pass 2 MUST appear as a bridge row. An implicit dependency IS NOT a bridge row; it MUST be explicit.**

| Bridge Row | Pass 1 Postcondition (FO-ID, field) | Feeds Pass 2 Precondition | Dependency type |
|------------|-------------------------------------|--------------------------|-----------------|
| BR-1 | [FO-ID]: [postcondition field=value] | [SO-ID]: [precondition that requires this field] | Sequential / Conditional |
*(one row per cross-domain dependency; bridge rows ARE referenced by C-47 confirmation annotations in Pass 2 FINDINGS)*

---

### PASS 2: Sales

**Pass 2 Heading [C-42 ordering annotation]:** Sales runs second because Sales-second ordering IS the hypothesis vehicle for commitment-gap defect class. Predicted defect class: **commitment-record gap** -- a Sales state advance occurring without a Finance approval record in the state required by BRIDGE TABLE 1→2. Sales precondition data IS the source for CS Pass 3 via BRIDGE TABLE 2→3.

*(Pass 2 structure mirrors Pass 1: Forecast, Transition Table [phase: X] labels traceable to Sales arc, Forecast Validation, Pass 2 Findings with C-45 defect-entry decomposition and C-47 confirmation citing BRIDGE TABLE 1→2 row)*

---

### BRIDGE TABLE 2→3 [T] (C-41)

*(same structure as BRIDGE TABLE 1→2; bridges Sales postconditions to CS preconditions; bridge rows referenced by C-47 in Pass 3 FINDINGS)*

---

### PASS 3: CS

**Pass 3 Heading [C-42 ordering annotation]:** CS runs third because CS-third ordering IS the hypothesis vehicle for service-closure premature defect class. Predicted defect class: **premature-closure** -- a CS case closed while the Finance/Sales chain has unresolved records. CS is the downstream recipient of both bridge tables.

*(Pass 3 structure mirrors Pass 1/2)*

---

### GATE B

*(same as V-01; add: all three pass TRANSITION TABLES complete; both BRIDGE TABLES complete)*

---

### INVALID TRANSITIONS [T]

*(same structure as V-01; entries drawn from all three domain pass tables; at least one terminal state per domain)*

---

### GATE C / RACE CONDITIONS [T]

*(same as V-01)*

---

### GATE D / AGGREGATE FINDINGS [T]

**AGGREGATE FINDINGS IS the synthesis layer across all three passes.** A finding appearing in only one pass finding section IS a pass-level finding. A finding that spans multiple bridge rows IS an aggregate finding and IS REQUIRED to appear here.

**Defect-entry format IS REQUIRED (C-45) for all aggregate findings.**

*(same defect-entry format as Pass Findings; C-47 confirmation annotation required; cite specific bridge row from specific BRIDGE TABLE)*

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections (in order): INERTIA BASELINE, CONSTRAINT MATRIX, ROLES, STATE DECLARATIONS (all three domains), OPERATION DECLARATIONS (all three domains), INVARIANT DECLARATIONS, PHASE VOCABULARY DECLARATION, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION, INVENTORY CHALLENGE, GATE A, PASS 1 (Forecast + Table + Validation + Findings), BRIDGE TABLE 1→2, PASS 2, BRIDGE TABLE 2→3, PASS 3, GATE B, INVALID TRANSITIONS, GATE C, RACE CONDITIONS, GATE D, AGGREGATE FINDINGS.

---

## V-03 — Lifecycle Emphasis: Expanded Phase Vocabulary / Large CS Domain

**Variation axis:** Lifecycle emphasis (how explicitly phase boundaries are declared; phase vocabulary covers phases not appearing in the trace)
**Hypothesis:** An 8-phase CS domain forces C-46 to declare phases that will NOT appear in the trace. This makes C-46's completeness-verifiability property observable: the trace covers 5 phases; the declaration covers 8; the 3 absent phases ARE a documented coverage note, not a gap. C-46 without this structure IS satisfiable by listing only trace-present phases -- defeating the completeness intent. C-45 standard. Single-pass tabular. Predicted: all prior + C-45 + C-46 (with completeness-verifiable phase arc).
**Domain:** Customer Service / Support (New / Assigned / In-Progress / Pending-Customer / Escalated / Resolved / Verification-Pending / Closed)
**New probes:** C-46 completeness-verifiability: phases declared beyond those in trace; coverage gap IS a declared note.

---

### INERTIA BASELINE

The alternative to this trace IS: implement {{topic}} case lifecycle management without hand-compiling state transitions. The failure mode IS: cases enter invalid state sequences -- escalated cases resolve without resolution records, closed cases reopen without supervisor override, pending-customer cases auto-close without customer confirmation. This trace exists to close that gap.

**PRODUCTION COST DECLARATION.** The cost IS NOT a delayed response; the cost IS a support record in a state the system should have blocked, discovered by a support audit rather than by the application.

**IS-NEGATION PAIR.** The inertia baseline IS NOT a support workflow gap; it IS a case integrity failure mode. Choosing not to produce this trace IS NOT a risk accepted; it IS the failure mode instantiated.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. A Domain Expert [D] declares the CS lifecycle vocabulary including all 8 phases of the support case lifecycle. [D]'s PHASE VOCABULARY DECLARATION IS the completeness anchor: it names all phases in sequence, including those that will not appear in this specific trace scenario. [T] traces the scenario. The CONSTRAINT MATRIX IS authoritative.

---

### CONSTRAINT MATRIX

*(same structure as V-01; EPOCH vocabulary: INTAKE / ACTIVE-SUPPORT / ESCALATION / RESOLUTION)*

---

### ROLES

**[D] Domain Expert**
Auto-selected: Customer Service expert (New / Assigned / In-Progress / Pending-Customer / Escalated / Resolved / Verification-Pending / Closed).
Sections owned by [D]: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, PHASE VOCABULARY DECLARATION, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION.
**PHASE VOCABULARY DECLARATION obligation:** [D]'s declaration IS REQUIRED to name all 8 lifecycle phases in sequence including Verification-Pending, which IS a phase that may not appear in a standard happy-path trace. An incomplete declaration that lists only trace-present phases IS NOT a valid C-46 artifact; it IS a declaration that eliminates completeness-verifiability.

**[T] Trace Developer**
*(same as V-01)*

---

### STATE DECLARATIONS [D]

**S-01.** New -- case record created on customer contact; case_id assigned, channel and priority set, no agent assigned yet. Terminal: No.
**S-02.** Assigned -- first-response agent assigned; SLA clock started; initial acknowledgment sent. Terminal: No.
**S-03.** In-Progress -- active investigation underway; agent working the case; internal notes accumulating. Terminal: No.
**S-04.** Pending-Customer -- case blocked on customer input; SLA clock paused per policy; auto-close timer started. Terminal: No.
**S-05.** Escalated -- case transferred to Tier-2 or specialist; original agent notified; escalation reason recorded. Terminal: No.
**S-06.** Resolved -- solution delivered; resolution_code set; customer notified; verification window open. Terminal: No.
**S-07.** Verification-Pending -- resolution sent; awaiting customer confirmation within verification window; auto-confirm timer active. Terminal: No.
**S-08.** Closed -- case confirmed resolved or auto-closed; case_status = CLOSED; no further state transitions permitted. Terminal: Yes.

---

### OPERATION DECLARATIONS [D]

**O-01.** Assign -- routes case to available agent matching skill profile. From: S-01. To: S-02. Actor: routing-engine.
**O-02.** Begin-Investigation -- agent accepts case and begins active work. From: S-02. To: S-03. Actor: agent.
**O-03.** Request-Customer-Input -- agent determines customer input required; SLA paused. From: S-03. To: S-04. Actor: agent.
**O-04.** Resume-Investigation -- customer response received; SLA resumed. From: S-04. To: S-03. Actor: system on customer-response.
**O-05.** Escalate -- agent determines Tier-2 required; escalation_reason required. From: S-03, S-04. To: S-05. Actor: agent.
**O-06.** Resolve -- solution confirmed; resolution_code set; customer notified. From: S-03, S-05. To: S-06. Actor: agent.
**O-07.** Enter-Verification -- resolution delivered; verification window opened. From: S-06. To: S-07. Actor: system.
**O-08.** Confirm-Closed -- customer confirms resolution or auto-close timer expires. From: S-07. To: S-08. Actor: customer or system.
**O-09.** Reopen -- customer reports unresolved after closure; requires supervisor_override. From: S-08. To: S-03. Actor: supervisor.

---

### INVARIANT DECLARATIONS [D]

**INV-01.** SLA-Clock Integrity -- IF case.status IN (S-01, S-02, S-03, S-05, S-06, S-07) THEN sla_clock.status = RUNNING; IF case.status = S-04 THEN sla_clock.status = PAUSED. Authority: SLA Policy v3.2.
**INV-02.** Escalation-Record Completeness -- IF case transitioned via O-05 THEN escalation_reason IS NOT NULL AND escalation_timestamp IS NOT NULL. Authority: Support Operations Handbook §4.1.
**INV-03.** Closed-State Immutability -- IF case.status = S-08 AND actor != supervisor THEN no operation IS permitted except O-09 with supervisor_override. Authority: Compliance Policy §7.
*(minimum two; INV-03 recommended for terminal state coverage)*

---

### PHASE VOCABULARY DECLARATION [D]

**This declaration IS NOT a summary of phases that appear in the trace; it IS the complete CS lifecycle arc. Phases appearing in this declaration but absent from the scenario trace ARE documented-but-untested paths. Their absence IS NOT a trace gap; it IS a coverage note that IS verifiable because this declaration exists. A PHASE VOCABULARY DECLARATION that lists only trace-present phases eliminates this verifiability and IS NOT a valid C-46 artifact.**

**Customer Service lifecycle arc (all 8 phases in sequence):**

| Phase # | Phase Name | Lifecycle Position | Note |
|---------|-----------|-------------------|------|
| 1 | Intake | Entry | Case created; no agent yet |
| 2 | Initial-Response | Early | Agent assigned; SLA started |
| 3 | Active-Investigation | Mid | Agent working; notes accumulating |
| 4 | Customer-Pending | Mid | Blocked on customer; SLA paused |
| 5 | Escalation | Mid-Late | Tier-2 engaged |
| 6 | Resolution-Delivered | Late | Solution sent; verification window open |
| 7 | Verification | Late | Awaiting customer confirmation |
| 8 | Closure | Terminal | Case permanently closed |

*(Terminal phase: Closure / S-08)*

> [D] declares: all 8 phases above. This scenario trace covers phases 1-5 and 8. **Phases 6 (Resolution-Delivered) and 7 (Verification) ARE declared but untested in this scenario.** Their absence from the trace IS a documented coverage note. A trace reviewer MAY verify that all 8 phases have been exercised across the trace suite by comparing this declaration against trace-present phases across all runs.

---

### VOCABULARY CLOSED [D]

> VOCABULARY CLOSED per C4. States: S-01 (New), S-02 (Assigned), S-03 (In-Progress), S-04 (Pending-Customer), S-05 (Escalated), S-06 (Resolved), S-07 (Verification-Pending), S-08 (Closed). Operations: O-01 (Assign) through O-09 (Reopen). The vocabulary IS FROZEN. This prohibition IS NOT WAIVABLE.

---

### STATE DIAGRAM [D]

*(Annotated edge list; 8 nodes; edges per OPERATION DECLARATIONS; [!] on VIOLATED-predicted edges)*

**Nodes:**
- S-01: New *(Non-terminal)*
- S-02: Assigned *(Non-terminal)*
- S-03: In-Progress *(Non-terminal)*
- S-04: Pending-Customer *(Non-terminal)*
- S-05: Escalated *(Non-terminal)*
- S-06: Resolved *(Non-terminal)*
- S-07: Verification-Pending *(Non-terminal)*
- S-08: Closed *(Terminal)*

**Edges:** *(per OPERATION DECLARATIONS; [!] added by [D] for operations predicted VIOLATED)*
- S-01 --[O-01: Assign]--> S-02
- S-02 --[O-02: Begin-Investigation]--> S-03
- *(continue for all O-IDs)*

**Structural counts:**
- Node count: 8
- Edge count: [N] (per OPERATION DECLARATIONS)
- [!] annotation count: [N] (per INVARIANT-VIOLATION FORECAST)

---

### HANDOFF DECLARATION [D]

> **[D] HANDOFF DECLARATION.**
>
> Artifacts transferred ARE:
> 1. STATE DECLARATIONS (S-01 through S-08, 8 states, 1 terminal)
> 2. OPERATION DECLARATIONS (O-01 through O-09)
> 3. INVARIANT DECLARATIONS (INV-01 through INV-03)
> 4. PHASE VOCABULARY DECLARATION: CS lifecycle arc, all 8 phases declared in sequence. Phases 6 (Resolution-Delivered) and 7 (Verification) ARE declared-but-untested in this scenario -- coverage note documented in declaration. [T]'s `[phase: X]` labels ARE constrained to these 8 phases.
> 5. STATE DIAGRAM: 8 nodes, [N] edges, [N] [!] annotations.
>
> [D] IS PROHIBITED from altering any declaration from this point forward.
> [T] IS NOW AUTHORIZED.
>
> **[D] Signed:** CS expert -- 8 states (1 terminal), 9 operations, 3 invariants, PHASE VOCABULARY DECLARATION (8 phases, 2 declared-untested noted), STATE DIAGRAM (8 nodes, [N] edges, [N] [!] annotations) ARE DECLARED AND CLOSED.

---

### INVENTORY CHALLENGE / GATE A / INVARIANT-VIOLATION FORECAST / TRANSITION TABLE [T]

*(same structure as V-01; TRANSITION TABLE state cells carry `[phase: X]` labels traceable to the 8-phase PHASE VOCABULARY DECLARATION; GATE A checklist adds: PHASE VOCABULARY DECLARATION lists all 8 phases including Verification-Pending and Closure; declared-but-untested phases documented)*

---

### TRANSITION TABLE [T]

| # | From State (S-ID) [phase: X] | Operation (O-ID) | Preconditions | To State (S-ID) [phase: X] | Postconditions | INV-01 | INV-02 | EPOCH | Side Effects |
|---|------------------------------|-----------------|---------------|---------------------------|----------------|--------|--------|-------|--------------|

`[phase: X]` labels MUST reference phases from the 8-phase PHASE VOCABULARY DECLARATION. A phase label not in the declaration IS NOT PERMITTED.

---

### LIFECYCLE EPOCH MAP / FORECAST VALIDATION / GATE B / INVALID TRANSITIONS / GATE C / RACE CONDITIONS / GATE D

*(same structure as V-01)*

---

### FINDINGS [T]

**Defect-entry format IS REQUIRED (C-45). Phase coverage note IS REQUIRED in each finding that involves a declared-but-untested phase path.**

- **P[N]: [title]**
  **Pre-Defect State:** `[S-ID: state name | phase: X | key fields: field=value]`
  **Triggering Operation:** `[O-ID: operation name]` -- [precondition absent/bypassed]
  **Post-Defect State+Reason:** `[S-ID: resulting state | phase: X | INV-NN: VIOLATED because reason]`
  State-triple: Before=[S-ID] --[O-ID]--> After=[S-ID] (invariant VIOLATED)
  **Phase coverage note (if applicable):** [if this defect involves a transition through a declared-but-untested phase (e.g., Verification-Pending), note which phase was bypassed and cite the PHASE VOCABULARY DECLARATION entry]
  Source: [record reference]
  Inertia connection: [INERTIA BASELINE trace]
  Severity: FATAL / DEGRADED / COSMETIC.

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

*(same section list as V-01)*

---

## V-04 — Role Sequence x Output Format: Step-Block Multi-Pass (Finance/Sales)

**Variation axis:** Role sequence x output format (combined axis)
**Hypothesis:** Step-block format with fused step labels (`[C-38: directive -- FAILS if: pattern]`) combined with two-pass multi-pass structure enables C-38/C-39 (step-block only) AND C-40/C-41/C-42/C-47 (multi-pass only) simultaneously. C-44 via sub-step decomposition within a Finance operation block. C-45/C-46 standard. This is the first variation to probe C-38/C-39 + C-47 together. Predicted: all prior + C-45 + C-46 + C-47 + C-38 + C-39.
**Domain:** Finance (Pass 1) → Sales (Pass 2)
**Format:** Step-block (numbered steps with fused criterion labels, not tabular rows)

---

### INERTIA BASELINE

*(same structure as V-02; Finance/Sales cross-domain failure mode)*

---

You are running a **trace-state** signal for: {{topic}}

Produce a **step-block** state machine trace. Each operation IS documented as a numbered step block, not a table row. Step labels carry criterion-instruction fusions. Two domain passes run: **Pass 1 (Finance)**, **Pass 2 (Sales)**. The CONSTRAINT MATRIX IS authoritative. Read it completely before producing any output.

---

### CONSTRAINT MATRIX

**MATRIX AUTHORITY.** The CONSTRAINT MATRIX IS the governing authority for this trace and IS NOT AMENDABLE.

| ID | Architectural Fact | Assigned Role | Concern |
|----|--------------------|---------------|---------|
| C1 | A state name not declared in STATE DECLARATIONS IS PROHIBITED | [T] | vocabulary |
| C2 | An operation name not declared in OPERATION DECLARATIONS IS PROHIBITED | [T] | vocabulary |
| C3 | Primary trace output IS step-block format. Each operation IS a numbered step block. Tables ARE NOT VALID as primary trace output. Step labels carry fused criterion annotations. | [T] | format |
| C4 | Any state or operation added after VOCABULARY CLOSED IS declared IS a retroactive violation | [D] | ordering |
| C5 | A blank invariant status block within a step IS NOT PERMITTED | [T] | integrity |
| C6 | Pass 1 TRANSITION STEPS ARE BLOCKED until GATE A IS confirmed | [T] | ordering |
| C7 | A blank INVENTORY CHALLENGE IS a C7 violation | [T] | completeness |
| C8 | INVALID TRANSITIONS IS BLOCKED until GATE B IS confirmed | [T] | ordering |
| C9 | RACE CONDITIONS IS BLOCKED until GATE C IS confirmed | [T] | ordering |
| C10 | STATE DIAGRAM IS the structural cross-check; [!] required on VIOLATED-predicted edges | [D] | integrity |
| C11 | BRIDGE TABLE IS REQUIRED between Pass 1 and Pass 2 per C-41; Pass 2 IS BLOCKED until BRIDGE TABLE IS complete | [T] | ordering |

---

### ROLES

*(same role structure as V-02 but with step-block format language)*

---

### STATE DECLARATIONS / OPERATION DECLARATIONS / INVARIANT DECLARATIONS [D]

*(same as V-02 Finance + Sales sections)*

---

### PHASE VOCABULARY DECLARATION [D]

**Finance lifecycle arc:** Draft → Pending-Approval → Approved → Posted → Archived *(Terminal: Archived)*
**Sales lifecycle arc:** Lead-Identification → Qualification → Solution-Development → Negotiation → Close → Post-Close *(Terminal: Closed-Won, Closed-Lost)*

> [D] declares: both domain lifecycle arcs. [T]'s `[phase: X]` annotations in step blocks ARE constrained to these declarations.

---

### VOCABULARY CLOSED [D]

*(same as V-02)*

---

### STATE DIAGRAM [D]

*(same as V-02; two domain sub-diagrams with [!] annotations)*

---

### HANDOFF DECLARATION [D]

*(same as V-02 with step-block format references; PHASE VOCABULARY DECLARATION named as transferred artifact)*

---

### INVENTORY CHALLENGE / GATE A [T]

GATE A checklist adds for step-block format:
- [ ] PHASE VOCABULARY DECLARATION IS complete -- Finance and Sales arcs declared in sequence
- [ ] Step-block format IS declared: each operation WILL be a numbered step block with fused criterion label
- [ ] Pass ordering IS declared as hypothesis vehicle (C-42 annotation in pass headings)

---

### PASS 1: Finance — Step-Block Trace

**Pass 1 Heading [C-42 ordering annotation]:** Finance runs first because Finance-first ordering IS the hypothesis vehicle for **revenue-state integrity failure** defect class. A Finance state advancing to Posted without a Sales commitment record IS the predicted invariant violation pattern. Finance postconditions ARE the precondition source for Sales via BRIDGE TABLE.

#### Pass 1 Invariant-Violation Forecast [T]

*(same structure as V-02 Pass 1 Forecast)*

#### Pass 1 Transition Steps [T]

Each operation IS documented as a numbered step block with fused criterion label per C3.

---

**Step 1 [C-38: each step block carries Before/Operation/After state triple -- FAILS if: state fields are described in prose without explicit S-ID annotation] [C-39: FAILS if: invariant check is omitted or labeled "N/A" without explicit clearance reason]**

- **Before State:** `[F-ID: state name | phase: X | key fields: field=value, field=value]`
  `[phase: X]` IS traceable to PHASE VOCABULARY DECLARATION Finance arc.
- **Operation:** `[FO-ID: operation name]`
- **Preconditions:**
  1. [testable assertion]
  2. [testable assertion]
- **After State:** `[F-ID: state name | phase: X | key fields: field=value, field=value]`
- **Postconditions:**
  1. [assertion distinct from After State name]
- **INV-F-01 check:** HOLDS / VIOLATED -- [reason if violated]
- **INV-X-01 check:** HOLDS / VIOLATED -- [reason if violated]
- **Side Effects:** [triggered rules, notifications, async jobs]

---

**Step 2 [C-38: each step block carries Before/Operation/After state triple -- FAILS if: state fields described in prose without S-ID] [C-39: FAILS if: invariant check omitted]**

*(structure repeats for all Finance operations)*

---

**Step [N] [C-44 sub-step decomposition: this operation IS decomposed into 3+ sub-steps each carrying independent Before/Op/After annotation -- FAILS if: fewer than 3 sub-steps present or any sub-step omits state triple]**

*[This step is designated for C-44 sub-step decomposition. Choose one Finance operation with compound precondition logic for decomposition.]*

- **Sub-step 1 of 3:**
  - Before: `[F-ID: state | phase: X | fields]`
  - Operation: `[FO-ID sub-action: first atomic action within compound operation]`
  - After: `[F-ID: intermediate state | phase: X | fields reflecting sub-step completion]`

- **Sub-step 2 of 3:**
  - Before: `[F-ID: intermediate state from sub-step 1]`
  - Operation: `[FO-ID sub-action: second atomic action]`
  - After: `[F-ID: further intermediate state]`

- **Sub-step 3 of 3:**
  - Before: `[F-ID: intermediate state from sub-step 2]`
  - Operation: `[FO-ID sub-action: final atomic action completing the operation]`
  - After: `[F-ID: final state after complete operation]`

- **INV-F-01 check (after all sub-steps):** HOLDS / VIOLATED -- [reason]
- **INV-X-01 check:** HOLDS / VIOLATED -- [reason]

---

#### Pass 1 Findings [T]

**Defect-entry format IS REQUIRED (C-45).**

- **F-P[N]: [title]**
  **Pre-Defect State:** `[F-ID: state name | phase: X | key fields: field=value]`
  **Triggering Operation:** `[FO-ID: operation name]` -- [precondition absent/bypassed]
  **Post-Defect State+Reason:** `[F-ID: resulting state | phase: X | INV-F-NN: VIOLATED because reason]`
  State-triple: Before=[F-ID] --[FO-ID]--> After=[F-ID] (invariant VIOLATED)
  **Defect-hypothesis confirmation (C-47):** Confirms [exact defect class from Pass 1 heading C-42 annotation: "revenue-state integrity failure"] (C-42 prediction: Pass 1 heading) -- exposed by bridge row [specific Finance.field → Sales.field from BRIDGE TABLE row BR-[N]] from C-11 BRIDGE TABLE.
  Source: [Step N of Pass 1]
  Inertia connection: [INERTIA BASELINE trace]
  Severity: FATAL / DEGRADED / COSMETIC.

---

### BRIDGE TABLE 1→2 [T] (C-41)

**Pass 2 IS BLOCKED until this table IS complete per C11.**

| Bridge Row | Pass 1 Step N Postcondition | Feeds Pass 2 Precondition | Dependency type |
|------------|----------------------------|--------------------------|-----------------|
| BR-1 | [Step N]: [FO-ID postcondition field=value] | [SO-ID]: [Sales precondition requiring this value] | Sequential |

---

### PASS 2: Sales — Step-Block Trace

**Pass 2 Heading [C-42 ordering annotation]:** Sales runs second because Sales-second ordering IS the hypothesis vehicle for **commitment-record gap** defect class. A Sales state advancing without the Finance approval postcondition from BR-[N] IS the predicted violation pattern.

*(Step blocks mirror Pass 1 format; `[phase: X]` labels traceable to PHASE VOCABULARY DECLARATION Sales arc; Pass 2 Findings include C-45 defect-entry decomposition and C-47 confirmation citing BRIDGE TABLE 1→2 BR-[N])*

---

### GATE B / INVALID TRANSITIONS / GATE C / RACE CONDITIONS / GATE D

*(same structure as V-02; step-block artifacts referenced instead of table rows)*

---

### AGGREGATE FINDINGS [T]

*(same structure as V-02; C-45 defect-entry format required; C-47 confirmation required)*

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: INERTIA BASELINE, CONSTRAINT MATRIX, ROLES, STATE DECLARATIONS (Finance + Sales), OPERATION DECLARATIONS, INVARIANT DECLARATIONS, PHASE VOCABULARY DECLARATION, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION, INVENTORY CHALLENGE, GATE A, PASS 1 (Forecast + Steps + Findings), BRIDGE TABLE 1→2, PASS 2 (Forecast + Steps + Findings), GATE B, INVALID TRANSITIONS, GATE C, RACE CONDITIONS, GATE D, AGGREGATE FINDINGS.

---

## V-05 — Full Synthesis: All Probes + New Domain (E-Commerce Order)

**Variation axis:** Full synthesis (all three new criteria + step-block format + new domain)
**Hypothesis:** E-commerce order domain (Pending / Confirmed / Processing / Shipped / Delivered / Cancelled / Returned) exercises C-45/C-46/C-47/C-38/C-39/C-44 simultaneously and confirms domain portability of all new v15 criteria. Three-pass: Payment (Pass 1) → Fulfillment (Pass 2) → Returns (Pass 3). C-47 confirmation in each pass. Phase vocabulary declaration for all three sub-domains. Step-block format throughout. Predicted: all prior + C-45 + C-46 + C-47 + C-38 + C-39 + C-44.
**Domain:** E-commerce Order (Pending/Confirmed/Processing/Shipped/Delivered/Cancelled/Returned)
**Format:** Step-block multi-pass
**New probes:** Domain portability confirmation for all R17 criteria

---

### INERTIA BASELINE

The alternative to this trace IS: implement {{topic}} order lifecycle management without hand-compiling payment, fulfillment, and returns state transitions. The failure mode IS: orders ship without payment confirmation, returns process against delivered records that are still in-transit in fulfillment state, and cancelled orders appear as active in warehouse queues. The cost IS NOT an inventory discrepancy; the cost IS an order record in a state that the payment or fulfillment system should have blocked, discovered by a warehouse audit rather than by the application.

**PRODUCTION COST DECLARATION.** The cost IS: fulfilled orders whose payment records ARE still Pending; Returned orders whose Delivered records ARE still Processing; Cancelled orders whose warehouse picks ARE still active. This IS NOT a reporting lag; this IS a state machine defect in the absence of this trace.

**IS-NEGATION PAIR.** The inertia baseline IS NOT an order management gap; it IS a cross-domain state integrity failure mode. Choosing not to produce this trace IS NOT acceptable risk; it IS the failure mode instantiated before the feature ships.

---

You are running a **trace-state** signal for: {{topic}}

Produce a **step-block multi-pass** state machine trace. Format IS step-block (not tabular). Three domain passes: **Pass 1 (Payment)**, **Pass 2 (Fulfillment)**, **Pass 3 (Returns)**. Step labels carry fused criterion annotations. The CONSTRAINT MATRIX IS authoritative.

---

### CONSTRAINT MATRIX

*(same as V-04 with E-commerce epoch vocabulary: PAYMENT-PHASE / FULFILLMENT-PHASE / RETURNS-PHASE)*

---

### ROLES

*(same as V-04; [D] IS E-commerce expert across Payment, Fulfillment, Returns sub-domains)*

---

### STATE DECLARATIONS [D]

**Order states (shared across passes; access governed by pass scope):**
**S-01.** Pending -- order created; payment not yet authorized; inventory not reserved. Terminal: No.
**S-02.** Confirmed -- payment authorized; inventory reserved; fulfillment queue entry created. Terminal: No.
**S-03.** Processing -- warehouse pick initiated; items staged for packing. Terminal: No.
**S-04.** Shipped -- carrier handoff completed; tracking number assigned; estimated delivery set. Terminal: No.
**S-05.** Delivered -- carrier confirmed delivery; delivery_timestamp set; return window opens. Terminal: No.
**S-06.** Cancelled -- order voided; payment reversal initiated; inventory reservation released. Terminal: Yes.
**S-07.** Return-Requested -- customer initiated return within return window; RMA issued. Terminal: No.
**S-08.** Returned -- physical goods received; return_receipt confirmed; refund initiated. Terminal: Yes.

---

### OPERATION DECLARATIONS [D]

**Payment operations (PO-NN):**
**PO-01.** Authorize-Payment -- payment gateway approval received; payment_auth_code assigned. From: S-01. To: S-02. Actor: payment-gateway.
**PO-02.** Cancel-Payment -- order voided before fulfillment; payment_reversal initiated. From: S-01, S-02. To: S-06. Actor: customer or admin.

**Fulfillment operations (FLO-NN):**
**FLO-01.** Begin-Pick -- warehouse pick list generated; items staged. From: S-02. To: S-03. Actor: warehouse-system.
**FLO-02.** Ship -- carrier handoff completed; tracking assigned. From: S-03. To: S-04. Actor: fulfillment-ops.
**FLO-03.** Confirm-Delivery -- carrier delivery scan received. From: S-04. To: S-05. Actor: carrier-api.
**FLO-04.** Cancel-Fulfillment -- cancellation received while in Processing; pick reversed. From: S-03. To: S-06. Actor: admin.

**Returns operations (RTO-NN):**
**RTO-01.** Request-Return -- customer initiates return; RMA issued. From: S-05. To: S-07. Actor: customer.
**RTO-02.** Receive-Return -- goods received at warehouse; return_receipt confirmed. From: S-07. To: S-08. Actor: warehouse-ops.

---

### INVARIANT DECLARATIONS [D]

**INV-01.** Payment-Before-Fulfillment -- IF order.status IN (S-03, S-04, S-05) THEN payment_auth_code IS NOT NULL AND payment_status = AUTHORIZED. Authority: Financial Controls Policy §2.1.
**INV-02.** Inventory-Reservation Integrity -- IF order.status = S-02 THEN inventory_reservation_id IS NOT NULL AND reservation_qty = order_qty. Authority: Warehouse Operations §3.4.
**INV-03.** Return-Window Compliance -- IF order.status = S-07 THEN return_requested_at <= delivered_at + return_window_days. Authority: Customer Policy §5.2.
**INV-04.** Terminal-State Immutability -- IF order.status IN (S-06, S-08) THEN no transition IS permitted except by admin with override_reason. Authority: Order Lifecycle Policy §1.1.

---

### PHASE VOCABULARY DECLARATION [D]

**All three sub-domain lifecycle arcs ARE declared in sequence. Phases declared but not exercised in this trace scenario ARE documented-but-untested paths. Their absence IS a coverage note verifiable against this declaration.**

**Payment lifecycle arc:** Authorization-Pending → Payment-Authorized → Payment-Captured → Payment-Reversed
*(Terminal: Payment-Captured for successful orders; Payment-Reversed for cancelled)*

**Fulfillment lifecycle arc:** Fulfillment-Queued → Picking → Packing → Carrier-Handoff → In-Transit → Delivered
*(Terminal: Delivered)*

**Returns lifecycle arc:** Return-Window-Open → Return-Requested → Return-In-Transit → Return-Received → Refund-Processing → Refund-Complete
*(Terminal: Refund-Complete)*

> [D] declares: all three sub-domain lifecycle arcs above. [T]'s `[phase: X]` step annotations ARE constrained to these arcs. Phases not appearing in the trace (e.g., Packing in Fulfillment, Refund-Processing in Returns) ARE declared-but-untested; their absence IS documented here as a coverage note.

---

### VOCABULARY CLOSED [D]

> VOCABULARY CLOSED per C4. States: S-01 (Pending) through S-08 (Returned). Operations: PO-01 (Authorize-Payment), PO-02 (Cancel-Payment), FLO-01 (Begin-Pick), FLO-02 (Ship), FLO-03 (Confirm-Delivery), FLO-04 (Cancel-Fulfillment), RTO-01 (Request-Return), RTO-02 (Receive-Return). The vocabulary IS FROZEN. This prohibition IS NOT WAIVABLE.

---

### STATE DIAGRAM [D]

**Nodes:**
- S-01: Pending *(Non-terminal)*
- S-02: Confirmed *(Non-terminal)*
- S-03: Processing *(Non-terminal)*
- S-04: Shipped *(Non-terminal)*
- S-05: Delivered *(Non-terminal)*
- S-06: Cancelled *(Terminal)*
- S-07: Return-Requested *(Non-terminal)*
- S-08: Returned *(Terminal)*

**Edges:** *(per OPERATION DECLARATIONS; [!] on VIOLATED-predicted operations)*
- S-01 --[PO-01: Authorize-Payment]--> S-02
- S-01 --[PO-02: Cancel-Payment]--> S-06
- S-02 --[PO-02: Cancel-Payment]--> S-06
- S-02 --[FLO-01: Begin-Pick]--> S-03
- S-03 --[FLO-02: Ship]--> S-04
- S-03 --[FLO-04: Cancel-Fulfillment]--> S-06 [!] INVARIANT RISK: inventory reservation may remain active if reservation release IS not atomic with state transition
- S-04 --[FLO-03: Confirm-Delivery]--> S-05
- S-05 --[RTO-01: Request-Return]--> S-07
- S-07 --[RTO-02: Receive-Return]--> S-08

**Structural counts:**
- Node count: 8
- Edge count: 9
- [!] annotation count: [N] (per INVARIANT-VIOLATION FORECAST)

---

### HANDOFF DECLARATION [D]

> **[D] HANDOFF DECLARATION.**
>
> Artifacts transferred ARE:
> 1. STATE DECLARATIONS (S-01 through S-08; 2 terminal: S-06, S-08)
> 2. OPERATION DECLARATIONS (PO-01, PO-02, FLO-01..FLO-04, RTO-01, RTO-02)
> 3. INVARIANT DECLARATIONS (INV-01 through INV-04)
> 4. PHASE VOCABULARY DECLARATION: Payment arc (4 phases), Fulfillment arc (6 phases), Returns arc (6 phases) -- all arcs declared. Declared-but-untested phases: Packing (Fulfillment), Refund-Processing and Refund-Complete (Returns). [T]'s `[phase: X]` annotations ARE constrained to these three arcs.
> 5. STATE DIAGRAM: 8 nodes, 9 edges, [N] [!] annotations.
>
> [D] IS PROHIBITED from altering any declaration from this point forward.
> [T] IS NOW AUTHORIZED for Pass 1, BRIDGE TABLE 1→2, Pass 2, BRIDGE TABLE 2→3, Pass 3, INVALID TRANSITIONS, RACE CONDITIONS, AGGREGATE FINDINGS.
>
> **[D] Signed:** E-commerce expert -- 8 states (2 terminal), 8 operations, 4 invariants, PHASE VOCABULARY DECLARATION (3 sub-domain arcs, 16 total phases, declared-but-untested phases documented), STATE DIAGRAM (8 nodes, 9 edges, [N] [!] annotations) ARE DECLARED AND CLOSED.

---

### INVENTORY CHALLENGE / GATE A [T]

*(same as V-04; add: PHASE VOCABULARY DECLARATION lists all three sub-domain arcs; pass ordering declared as hypothesis vehicle per C-42)*

---

### PASS 1: Payment — Step-Block Trace

**Pass 1 Heading [C-42 ordering annotation]:** Payment runs first because Payment-first ordering IS the hypothesis vehicle for **pre-authorization fulfillment** defect class. A Fulfillment state advancing before payment_auth_code IS set IS the predicted invariant violation (INV-01). Payment postconditions ARE the precondition source for Fulfillment via BRIDGE TABLE 1→2.

#### Pass 1 Invariant-Violation Forecast [T]

| Op-ID | Operation Name | Predicted INV-01 | Predicted INV-02 | Rationale |
|-------|----------------|-----------------|-----------------|-----------|
| PO-01 | Authorize-Payment | HOLDS | HOLDS | authorization sets payment_auth_code; INV-01 satisfied after transition |
| PO-02 | Cancel-Payment | HOLDS | VIOLATED | cancellation releases inventory reservation; if reservation release IS not atomic, INV-02 may hold stale reservation_id |

#### Pass 1 Transition Steps [T]

---

**Step 1 [C-38: each step block carries Before/Operation/After state triple -- FAILS if: state fields described in prose without explicit S-ID] [C-39: FAILS if: invariant check omitted or labeled "N/A" without explicit clearance reason]**

- **Before State:** `[S-01: Pending | phase: Authorization-Pending | payment_auth_code=NULL, inventory_reservation_id=NULL]`
- **Operation:** `[PO-01: Authorize-Payment]`
- **Preconditions:**
  1. payment_gateway.status = READY
  2. order.total_amount > 0 AND card.on_file = TRUE
- **After State:** `[S-02: Confirmed | phase: Payment-Authorized | payment_auth_code=AUTH-XXXXXX, inventory_reservation_id=RES-YYYYYYY]`
- **Postconditions:**
  1. payment_auth_code IS NOT NULL
  2. inventory_reservation_id IS NOT NULL AND reservation_qty = order_qty
- **INV-01 check:** HOLDS -- payment_auth_code IS NOT NULL and payment_status = AUTHORIZED after transition
- **INV-02 check:** HOLDS -- inventory_reservation_id IS NOT NULL, reservation_qty matches order_qty

---

**Step 2 [C-38: Before/Operation/After triple required -- FAILS if: state fields in prose] [C-39: FAILS if: INV check absent]**
**[C-44 sub-step decomposition: PO-02 (Cancel-Payment) IS decomposed into 3 sub-steps -- FAILS if: fewer than 3 sub-steps OR any sub-step omits independent state triple]**

*PO-02 (Cancel-Payment) IS designated for C-44 sub-step decomposition due to compound atomic requirements (payment reversal + inventory release + order void must be independently traceable).*

- **Sub-step 1 of 3: Payment Reversal Initiation**
  - Before: `[S-02: Confirmed | phase: Payment-Authorized | payment_auth_code=AUTH-XXXXXX, reversal_initiated=FALSE]`
  - Operation: `[PO-02 sub-action: Initiate-Payment-Reversal]`
  - After: `[S-02: Confirmed | phase: Payment-Authorized | payment_auth_code=AUTH-XXXXXX, reversal_initiated=TRUE, reversal_ref=REV-ZZZZZZ]`

- **Sub-step 2 of 3: Inventory Reservation Release**
  - Before: `[S-02: Confirmed | phase: Payment-Authorized | inventory_reservation_id=RES-YYYYYYY]`
  - Operation: `[PO-02 sub-action: Release-Inventory-Reservation]`
  - After: `[S-02: Confirmed | phase: Payment-Authorized | inventory_reservation_id=NULL, reservation_qty=0]`

- **Sub-step 3 of 3: Order State Transition to Cancelled**
  - Before: `[S-02: Confirmed | phase: Payment-Authorized | reversal_initiated=TRUE, inventory_reservation_id=NULL]`
  - Operation: `[PO-02 sub-action: Void-Order]`
  - After: `[S-06: Cancelled | phase: Payment-Reversed | payment_auth_code=NULL, inventory_reservation_id=NULL, void_timestamp=NOW]`

- **INV-01 check (post all sub-steps):** HOLDS -- S-06 (Cancelled) does not require payment_auth_code; invariant applies only to S-03/S-04/S-05
- **INV-02 check:** VIOLATED -- if sub-step 2 IS NOT atomic with sub-step 3, a window exists where inventory_reservation_id=NULL but order IS still Confirmed (S-02); INV-02 requires reservation IS NOT NULL while in S-02

---

#### Pass 1 Findings [T]

**Defect-entry format IS REQUIRED (C-45).**

- **P1-01: Inventory-Release Race Window in Cancel-Payment**
  **Pre-Defect State:** `[S-02: Confirmed | phase: Payment-Authorized | inventory_reservation_id=RES-YYYYYYY, reversal_initiated=TRUE]`
  **Triggering Operation:** `[PO-02 sub-action: Release-Inventory-Reservation]` -- inventory release IS NOT atomic with order state transition; INV-02 requires reservation IS NOT NULL while in S-02, but Release-Inventory-Reservation sets reservation_id=NULL before Void-Order transitions to S-06
  **Post-Defect State+Reason:** `[S-02: Confirmed | phase: Payment-Authorized | inventory_reservation_id=NULL | INV-02: VIOLATED because reservation IS NULL while order IS still Confirmed]`
  State-triple: Before=[S-02] --[PO-02: Release-Inventory-Reservation]--> After=[S-02] (INV-02 VIOLATED in intermediate window)
  **Defect-hypothesis confirmation (C-47):** Confirms **pre-authorization fulfillment** defect class (C-42 prediction: Pass 1 heading -- "pre-authorization fulfillment defect class...Payment postconditions ARE the precondition source for Fulfillment via BRIDGE TABLE 1→2") -- exposed by bridge row BR-1 [S-02.payment_auth_code=AUTHORIZED → FLO-01 precondition: payment_auth_code IS NOT NULL] from C-11 BRIDGE TABLE 1→2. Without BR-1, the PO-02 sub-step 2 race window IS invisible to the Fulfillment pass.
  Source: Pass 1 Step 2, Sub-step 2 of 3
  Inertia connection: This defect IS the INERTIA BASELINE failure mode instantiated -- a Fulfillment pass that does not receive the payment precondition chain from BRIDGE TABLE 1→2 WILL process Begin-Pick against an order whose inventory reservation IS transiently NULL.
  Severity: FATAL.

---

### BRIDGE TABLE 1→2 [T] (C-41)

**Pass 2 IS BLOCKED until this table IS complete per C11.**

| Bridge Row | Pass 1 Step N Postcondition | Feeds Pass 2 Precondition | Dependency type |
|------------|----------------------------|--------------------------|-----------------|
| BR-1 | Step 1 (PO-01): payment_auth_code=AUTH-XXXXXX AND payment_status=AUTHORIZED | FLO-01 precondition 1: payment_auth_code IS NOT NULL (INV-01 must hold before Begin-Pick) | Sequential-Required |
| BR-2 | Step 1 (PO-01): inventory_reservation_id=RES-YYYYYYY AND reservation_qty=order_qty | FLO-01 precondition 2: inventory_reservation_id IS NOT NULL AND reservation_qty >= pick_qty | Sequential-Required |

---

### PASS 2: Fulfillment — Step-Block Trace

**Pass 2 Heading [C-42 ordering annotation]:** Fulfillment runs second because Fulfillment-second ordering IS the hypothesis vehicle for **inventory-state desync** defect class. A Fulfillment operation advancing after PO-02's inventory release window (identified in Pass 1 P1-01) IS the predicted compound defect. Fulfillment pass receives preconditions from BR-1 and BR-2.

*(Step blocks: same format as Pass 1; `[phase: X]` labels traceable to PHASE VOCABULARY DECLARATION Fulfillment arc; C-44 sub-step decomposition on FLO-01 or FLO-02; C-45 defect-entry decomposition in Pass 2 Findings; C-47 confirmation citing BRIDGE TABLE 1→2 specific rows)*

---

### BRIDGE TABLE 2→3 [T] (C-41)

| Bridge Row | Pass 2 Step N Postcondition | Feeds Pass 3 Precondition | Dependency type |
|------------|----------------------------|--------------------------|-----------------|
| BR-3 | [FLO-03 step]: delivered_at=TIMESTAMP AND delivery_confirmed=TRUE | RTO-01 precondition: order.status=S-05 (Delivered) AND return_window_open=TRUE | Sequential-Required |

---

### PASS 3: Returns — Step-Block Trace

**Pass 3 Heading [C-42 ordering annotation]:** Returns runs third because Returns-third ordering IS the hypothesis vehicle for **return-window bypass** defect class. An RTO-01 (Request-Return) operation where delivered_at IS not set (from BR-3) IS the predicted invariant violation (INV-03 -- return_requested_at <= delivered_at + window). Returns pass receives preconditions from BR-3.

*(Step blocks: same format; `[phase: X]` labels traceable to PHASE VOCABULARY DECLARATION Returns arc; C-45 defect-entry decomposition in Pass 3 Findings; C-47 confirmation citing BRIDGE TABLE 2→3 BR-3)*

---

### GATE B / INVALID TRANSITIONS [T]

*(same as V-04; minimum three invalid operation/state pairs; at least one from each of the two Terminal states S-06, S-08)*

---

### GATE C / RACE CONDITIONS [T]

Concurrent scenario IS REQUIRED: PO-01 (Authorize-Payment) and FLO-01 (Begin-Pick) initiated simultaneously -- payment gateway slow; fulfillment system begins pick before auth_code IS committed. Document unsafe interleaving, outcome (INV-01 VIOLATED), and mitigation (distributed lock on order_id; FLO-01 IS BLOCKED until payment_auth_code IS NOT NULL).

---

### GATE D / AGGREGATE FINDINGS [T]

**Defect-entry format IS REQUIRED (C-45) for all aggregate findings. C-47 confirmation IS REQUIRED for each aggregate finding that spans a bridge row.**

*(each finding: Pre-Defect State / Triggering Operation / Post-Defect State+Reason state-triple decomposition; C-47 confirmation naming the C-42 predicted class from the relevant pass heading and the specific bridge row from the relevant BRIDGE TABLE)*

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: INERTIA BASELINE, CONSTRAINT MATRIX, ROLES, STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, PHASE VOCABULARY DECLARATION, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION, INVENTORY CHALLENGE, GATE A, PASS 1 (Forecast + Steps + Findings), BRIDGE TABLE 1→2, PASS 2 (Forecast + Steps + Findings), BRIDGE TABLE 2→3, PASS 3 (Forecast + Steps + Findings), GATE B, INVALID TRANSITIONS, GATE C, RACE CONDITIONS, GATE D, AGGREGATE FINDINGS.

---

## Criterion Coverage Summary (R17)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-45 (defect-entry state-triple decomposition) | PASS | PASS | PASS | PASS | PASS |
| C-46 (phase vocabulary declaration before trace) | PASS | PASS | PASS | PASS | PASS |
| C-47 (defect-hypothesis confirmation annotation) | N/A (single-pass) | PASS | N/A (single-pass) | PASS | PASS |
| C-38 (step-block criterion-instruction fusion) | FAIL (tabular) | FAIL (tabular) | FAIL (tabular) | PASS | PASS |
| C-39 (step-block disqualification-condition fusion) | FAIL (tabular) | FAIL (tabular) | FAIL (tabular) | PASS | PASS |
| C-44 (sub-step decomposition within operation) | PARTIAL | PARTIAL | PARTIAL | PASS | PASS |
| C-40/C-41/C-42 (multi-pass prerequisites for C-47) | N/A | PASS | N/A | PASS | PASS |
| C-43 (lifecycle-phase state annotation) | PASS | PASS | PASS | PASS | PASS |

*C-47 requires C-40+C-41+C-42 all satisfied. V-01 and V-03 are single-pass and cannot satisfy C-47.*
*C-38/C-39 are step-block only; V-01 through V-03 use tabular format and cannot satisfy these.*
