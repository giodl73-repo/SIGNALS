---
name: signal-trace-state
description: State transition hand-compilation with preconditions, postconditions, and invariant checks.
allowed-tools: [Read, Write, Glob]
param_set: analysis
---
### INERTIA BASELINE

The alternative to this trace IS: implement {{topic}} state management without hand-compiling transitions and invariants. The failure mode that alternative creates IS: invalid state transitions reach production because precondition checks were assumed rather than enumerated. This trace exists to close that gap before code is written. Every section that is skipped or left as a placeholder IS a return to the inertia baseline.

**PRODUCTION COST DECLARATION.** The production cost of the inertia baseline IS: contract records enter invalid state sequences -- executed contracts appear under-review in obligation tracking, terminated contracts appear active in renewal pipelines, and expired contracts generate payment obligations in finance systems. The cost IS NOT an administrative error; the cost IS a legal obligation record in a state the system should have blocked, discovered by a contract audit rather than by the application. This IS the specific failure this trace exists to prevent. Any section of this document left blank or abbreviated IS already that failure, deferred.

**IS-NEGATION PAIR.** The inertia baseline IS NOT a documentation gap; it IS a legal obligation integrity failure mode in the absence of this artifact. Choosing not to produce this trace IS NOT a risk accepted; it IS the failure mode instantiated before the feature ships. The existence of this document IS NOT documentation; it IS the artifact that converts that certainty into a prevented outcome.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. This trace IS a formal artifact; its governing document IS the CONSTRAINT MATRIX below. A Domain Expert [D] declares the vocabulary phase; a Trace Developer [T] executes the trace phase. [T]'s authorization IS CONTINGENT on [D] completing and executing a HANDOFF DECLARATION. The INERTIA BASELINE above IS the structural frame for this entire document. The CONSTRAINT MATRIX IS authoritative. Read it completely before producing any output.

---

### CONSTRAINT MATRIX

**MATRIX AUTHORITY.** The CONSTRAINT MATRIX IS the governing authority for this trace and IS NOT AMENDABLE by [D] or [T]. A constraint not named in this matrix IS NOT binding on this trace. A violation not classifiable by a named constraint IS NOT a violation under this matrix. No role IS authorized to add, waive, or modify a constraint. The scope of this matrix IS total: every compliance obligation in this trace IS traceable to a named constraint row.

**DERIVATION FIELD.** Each constraint carries a Derivation field naming the architectural principle from which the constraint IS derived. A constraint's authority IS NOT self-asserted; it IS derived from the named principle. A constraint without a Derivation field IS NOT complete under this matrix.

| ID | Architectural Fact | Assigned Role | Concern | Derivation |
|----|--------------------|---------------|---------|------------|
| C1 | A state name not declared in STATE DECLARATIONS IS PROHIBITED in any trace table | [T] | vocabulary | Derivation: C1 IS derived from the closed-vocabulary principle -- trace validity IS contingent on the trace using only names that exist in the declared namespace |
| C2 | An operation name not declared in OPERATION DECLARATIONS IS PROHIBITED in any trace table | [T] | vocabulary | Derivation: C2 IS derived from the closed-vocabulary principle -- operation coverage IS falsifiable only if the operation set IS finite and declared before tracing |
| C3 | The TRANSITION TABLE includes an EPOCH column. EPOCH IS informational, IS NOT constrained by C1/C2. EPOCH values ARE drawn from Legal lifecycle phase vocabulary (e.g., DRAFTING / NEGOTIATION / EXECUTION / PERFORMANCE). Prose and bullet lists ARE NOT VALID as primary trace output. | [T] | format / scope | Derivation: C3 IS derived from the columnar-integrity and scope-separation principles -- tabular format IS the trace format; EPOCH IS NOT state vocabulary |
| C4 | Any state or operation added after VOCABULARY CLOSED IS declared IS a retroactive violation; such additions ARE PROHIBITED | [D] | ordering | Derivation: C4 IS derived from the phase-boundary principle -- declaration and trace ARE separated phases; retroactive vocabulary introduction IS NOT a correction; it IS a boundary violation |
| C5 | A blank invariant status cell IS NOT PERMITTED; every cell IS REQUIRED to contain HOLDS or VIOLATED | [T] | integrity | Derivation: C5 IS derived from the completeness-under-obligation principle -- an untested invariant IS NOT a deferral; it IS an assumed result and IS the inertia baseline |
| C6 | TRANSITION TABLE IS BLOCKED until GATE A IS confirmed AND INVARIANT-VIOLATION FORECAST IS complete | [T] | ordering | Derivation: C6 IS derived from the forecast-before-trace principle -- trace without prior commitment IS post-hoc rationale, NOT evidence |
| C7 | A blank or non-option response at INVENTORY CHALLENGE IS a C7 violation; GATE A IS BLOCKED | [T] | completeness | Derivation: C7 IS derived from the adversarial-challenge principle -- inventory completeness IS NOT self-certified; it IS confirmed under adversarial pressure or the challenge IS a violation |
| C8 | INVALID TRANSITIONS IS BLOCKED until GATE B IS confirmed | [T] | ordering | Derivation: C8 IS derived from the sequential-gate principle -- invalid-transition analysis IS dependent on a complete valid-transition set |
| C9 | RACE CONDITIONS IS BLOCKED until GATE C IS confirmed | [T] | ordering | Derivation: C9 IS derived from the sequential-gate principle -- concurrent-access analysis IS dependent on a complete invalid-transition set |
| C10 | STATE DIAGRAM [D] IS NOT a substitute for TRANSITION TABLE; it IS the structural cross-check artifact. Node, edge, and [!] counts IS REQUIRED. | [D] | integrity | Derivation: C10 IS derived from the cross-check-artifact principle -- a diagram without declared structural counts IS decoration, NOT a cross-check |

---

### ROLES

**ROLES IS NOT an organizational chart; ROLES IS the execution authority matrix for this trace. A section of this document without a named role assignment IS NOT shared ownership; it IS unowned obligation and IS the inertia baseline instantiated before any section IS produced. Every ownership claim below IS NOT advisory; it IS the assignment that makes execution authorized. An obligation not assigned to a named role IS NOT deferred; it IS absent.**

**[D] Domain Expert**
Auto-selected: Legal expert (Draft / Under-Review / Negotiating / Pending-Execution / Executed / Expired / Terminated).
Sections owned by [D]: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION.
Binding constraint: **C4**.
INERTIA BASELINE relationship: **[D]'s obligation IS NOT advisory documentation; it IS the prevention mechanism that separates this trace from an assumption about the contract lifecycle state machine.** The specific regression form [D] prevents IS: undeclared contract-state vocabulary producing untraced legal obligation transitions.

**[T] Trace Developer**
Sections owned by [T]: INVENTORY CHALLENGE response, INVARIANT-VIOLATION FORECAST, TRANSITION TABLE, LIFECYCLE EPOCH MAP, FORECAST VALIDATION, INVALID TRANSITIONS, RACE CONDITIONS, FINDINGS.
Binding constraints: **C1, C2, C3, C5, C6, C7, C8, C9, C10**.
Authorization status: [T]'s authorization IS CONTINGENT on HANDOFF DECLARATION.
INERTIA BASELINE relationship: **[T]'s obligation IS NOT iterative development; it IS the commitment that converts the inertia certainty named above into a prevented outcome.** The specific regression form [T] prevents IS: untraced contract transitions shipping as assumed-valid obligation management logic.

---

### STATE DECLARATIONS [D]

**S-01.** [State Name] -- [inline definitional clause]. Terminal: Yes/No.
*(continue; Legal typical set: Draft, Under-Review, Negotiating, Pending-Execution, Executed, Expired, Terminated)*

At least one Terminal: Yes entry IS REQUIRED.

---

### OPERATION DECLARATIONS [D]

**O-01.** [Operation Name] -- [inline definitional clause]. From: S-[N][, S-[N]...]. To: S-[N]. Actor: [role].
*(continue for all operations)*

---

### INVARIANT DECLARATIONS [D]

**INV-01.** [Name] -- [boolean assertion]. Authority: [source].
**INV-02.** [Name] -- [boolean assertion]. Authority: [source].

---

### VOCABULARY CLOSED [D]

**VOCABULARY CLOSED IS NOT a label; it IS the irreversibility event. The moment this declaration IS present in the document, [D]'s authority to introduce, modify, or redefine any state or operation name IS extinguished. The vocabulary IS NOT closeable by reference to this section; it IS closed by the existence of this declaration.**

> VOCABULARY CLOSED per C4. States: [S-IDs and names]. Operations: [O-IDs and names]. The vocabulary IS FROZEN. This prohibition IS NOT WAIVABLE and IS NOT CONTINGENT on any further action.

HANDOFF DECLARATION IS BLOCKED until VOCABULARY IS FROZEN.

---

### STATE DIAGRAM [D]

IS NOT a substitute for TRANSITION TABLE; IS the structural cross-check artifact. [!] annotation on every edge predicted VIOLATED.

**Nodes:** S-[NN]: [State Name] *(Terminal/Non-terminal)*

**Edges:** S-[NN] --[O-NN]--> S-[NN] [[!] INVARIANT RISK: reason if VIOLATED]

**Structural counts:** Node count: [N]. Edge count: [N]. [!] annotation count: [N].

---

### HANDOFF DECLARATION [D]

> **[D] HANDOFF DECLARATION.**
>
> **TRANSFER DECLARATION.** This HANDOFF IS NOT a coordination event; it IS the formal instantiation of production responsibility transfer. [D]'s declaration authority IS extinguished; [T]'s trace authorization IS created. The HANDOFF IS NOT a record of completion; it IS the causal event that makes completion possible.
>
> Transferring role IS: [D] (Legal expert). Receiving role IS: [T].
>
> Artifacts: STATE DECLARATIONS (S-01..S-[N]), OPERATION DECLARATIONS (O-01..O-[N]), INVARIANT DECLARATIONS, STATE DIAGRAM [D] (IS NOT TRANSITION TABLE substitute; IS structural cross-check; Node: [N], Edge: [N], [!]: [N]), LIFECYCLE EPOCH MAP.
>
> **Post-transfer role states:**
> [D] IS PROHIBITED from altering any declaration from this point forward. This prohibition IS NOT WAIVABLE.
> [T] IS NOW AUTHORIZED to produce output in all [T]-owned sections.
>
> **[D] Signed:** Legal expert -- [N] states, [N] operations, [N] invariants ARE DECLARED AND CLOSED.

---

### INVENTORY CHALLENGE

**C7 applies. A blank or non-option response IS a C7 violation.**

**Option A (CONFIRMED):** "[T] INVENTORY CONFIRMED. States: [S-IDs]. Operations: [O-IDs]. [T]'s authorization IS IN EFFECT."

**Option B (GAP FOUND):** "[T] INVENTORY INCOMPLETE. Gap: [item]. Returning to [D]."

---

### GATE A

**GATE A IS NOT a checkpoint list; it IS the enforcement mechanism that makes [T]'s authorization conditional on named completion conditions. GATE A IS NOT clearable by assertion; it IS clearable only when every item below IS confirmed.**

- [ ] INERTIA BASELINE IS present with PRODUCTION COST DECLARATION (contrast framing) and IS-NEGATION PAIR -- **this blocking condition IS derived from C-27/C-30/C-33/C-37**
- [ ] CONSTRAINT MATRIX IS present with MATRIX AUTHORITY preamble AND per-constraint Derivation field (C-52 probe) -- **this blocking condition IS derived from C-05/C-16/C-17/C-18/C-19/C-41**
- [ ] ROLES IS-authority opener IS present (C-50 probe); per-role IS-negation obligation pair present for both [D] and [T] -- **this blocking condition IS derived from C-43/C-36**
- [ ] STATE DECLARATIONS complete with at least one Terminal: Yes entry -- **this blocking condition IS derived from C-01/C-09/C-23**
- [ ] OPERATION DECLARATIONS complete with resolved S-ID references -- **this blocking condition IS derived from C-02/C-23**
- [ ] INVARIANT DECLARATIONS present with at least two boolean assertions -- **this blocking condition IS derived from C-05**
- [ ] VOCABULARY CLOSED declared with all three C-47 elements; prohibition IS NOT WAIVABLE -- **this blocking condition IS derived from C-15/C-47**
- [ ] STATE DIAGRAM complete with structural counts consistent with declarations -- **this blocking condition IS derived from C-10/C-38/C-39/C-40**
- [ ] HANDOFF DECLARATION signed with IS-transfer opener, post-transfer role states, STATE DIAGRAM counts -- **this blocking condition IS derived from C-22/C-25/C-26/C-32/C-39/C-45**
- [ ] INVENTORY CHALLENGE resolved -- Option A or Option B written -- **this blocking condition IS derived from C-07/C-11/C-21**
- [ ] [C-14] No undeclared names in trace tables -- **this blocking condition IS derived from C-14**

**GATE A: [T] IS BLOCKED. INVARIANT-VIOLATION FORECAST IS BLOCKED until all items ARE confirmed.**

---

### INVARIANT-VIOLATION FORECAST [T]

**TRANSITION TABLE IS BLOCKED until INVARIANT-VIOLATION FORECAST IS complete per C6.**

**FORECAST COMMITMENT.** This FORECAST IS a formal commitment, not a guess. A blank O-ID row IS a C6 violation already instantiated at authoring time. The FORECAST IS the contract; FORECAST VALIDATION IS the audit of that contract.

| O-ID | Operation Name | Predicted INV-01 | Predicted INV-02 | Rationale |
|------|----------------|-----------------|-----------------|-----------|
| O-[N] | [name] | HOLDS / VIOLATED | HOLDS / VIOLATED | [rationale] |
*(blanks ARE NOT PERMITTED)*

---

### FORECAST VALIDATION [T]

**FORECAST VALIDATION IS NOT a review checkpoint; it IS the gated closure event that converts the INVARIANT-VIOLATION FORECAST from a provisional commitment into an executed commitment. Prior to this section's completion, [T]'s forecast IS provisional; it IS NOT a confirmed prediction. This FORECAST VALIDATION IS the only act that makes the forecast confirmed. A FORECAST VALIDATION completed without comparing every O-ID IS NOT a closure event; it IS the forecast left provisional and the commitment left unexecuted.**

| O-ID | Predicted INV-01 | Actual INV-01 | Predicted INV-02 | Actual INV-02 | Forecast Status |
|------|-----------------|--------------|-----------------|--------------|-----------------|
| O-[N] | [forecast] | [actual] | [forecast] | [actual] | CONFIRMED / REFUTED -- [explanation] |

A REFUTED forecast IS a required finding.

---

### GATE B

**GATE B IS NOT a checkpoint list; it IS the enforcement mechanism that makes INVALID TRANSITIONS authorization conditional on TRANSITION TABLE completeness. GATE B IS NOT clearable by assertion; it IS clearable only when every item below IS confirmed.**

- [ ] TRANSITION TABLE IS columnar; no prose substitution -- **this blocking condition IS derived from C-08/C-13**
- [ ] Every INV cell contains HOLDS or VIOLATED -- **this blocking condition IS derived from C-05**
- [ ] LIFECYCLE EPOCH MAP complete -- **this blocking condition IS derived from C-31**
- [ ] FORECAST VALIDATION IS-closure IS present; all O-IDs compared; REFUTED rows flagged -- **this blocking condition IS derived from C-34/C-35**

**GATE B: [T] IS BLOCKED. INVALID TRANSITIONS IS BLOCKED until all items ARE confirmed.**

---

### TRANSITION TABLE [T]

| # | From State (S-ID) | Operation (O-ID) | Preconditions | To State (S-ID) | Postconditions | INV-01 | INV-02 | EPOCH (informational) | Side Effects |
|---|-------------------|-----------------|---------------|-----------------|----------------|--------|--------|----------------------|--------------|

C1, C2, C3, C5 in effect.

---

### LIFECYCLE EPOCH MAP [T]

| O-ID | Operation Name | Lifecycle Epoch | Epoch Rationale |
|------|----------------|-----------------|-----------------|

---

### GATE C

**GATE C IS NOT a checkpoint list; it IS the enforcement mechanism that makes RACE CONDITIONS authorization conditional on INVALID TRANSITIONS completeness. GATE C IS NOT clearable by assertion; it IS clearable only when every item below IS confirmed.**

- [ ] At least three invalid (operation, state) pairs named -- **this blocking condition IS derived from C-04/C-12**
- [ ] At least one Terminal-state row present -- **this blocking condition IS derived from C-09**

**GATE C: [T] IS BLOCKED. RACE CONDITIONS IS BLOCKED until all items ARE confirmed.**

---

### INVALID TRANSITIONS [T]

| # | Attempted Operation (O-ID) | From State (S-ID) | Blocking Condition | INV Reference | Risk if Bypassed |
|---|---------------------------|------------------|--------------------|--------------|-----------------|

Minimum three rows. At least one Terminal From State IS REQUIRED.

---

### RACE CONDITIONS [T]

| Operation A (O-ID) | Operation B (O-ID) | Unsafe Interleaving | Outcome | Mitigation |
|--------------------|--------------------|---------------------|---------|-----------|

---

### GATE D

**GATE D IS NOT a checkpoint list; it IS the enforcement mechanism that makes FINDINGS authorization conditional on full trace completeness. GATE D IS NOT clearable by assertion; it IS clearable only when every item below IS confirmed.**

- [ ] RACE CONDITIONS addressed -- **this blocking condition IS derived from C-09**
- [ ] FORECAST VALIDATION IS-closure IS present; REFUTED rows flagged as findings -- **this blocking condition IS derived from C-34**
- [ ] All S-IDs and O-IDs resolved to declarations -- **this blocking condition IS derived from C-01/C-02**
- [ ] No section IS blank or placeholder-only -- **this blocking condition IS derived from C-27**

**GATE D: [T] IS BLOCKED. FINDINGS IS BLOCKED until all items ARE confirmed.**

---

### FINDINGS [T]

**FINDINGS IS NOT an observation log; it IS the derivation layer.** A finding IS NOT a priority finding if IS NOT traceable to the INERTIA BASELINE; such a finding IS background noise. FINDINGS IS NOT complete until every REFUTED forecast row IS named as a finding.

**Inertia connection IS REQUIRED on every finding.** A finding template without an Inertia connection field IS NOT a valid finding entry under this document.

**Disposition IS REQUIRED on every finding.** A finding template without a Disposition field IS NOT a valid finding entry. Disposition MUST use IS-phrased values.

- **P[N]: [title]**
  Source: [TRANSITION TABLE row N / INVALID TRANSITIONS row N / FORECAST VALIDATION O-[N] / RACE CONDITIONS entry N].
  Inertia connection: [how this finding traces to the INERTIA BASELINE failure mode; a finding without this IS background noise].
  Disposition: [Status IS ACCEPTED / Status IS REJECTED -- IS NOT traceable to INERTIA BASELINE / Action IS REQUIRED before feature ships / Action IS NOT PERMITTED until this finding IS resolved].
  Severity: FATAL / DEGRADED / COSMETIC.

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: INERTIA BASELINE, CONSTRAINT MATRIX, ROLES, STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION, INVENTORY CHALLENGE, GATE A, INVARIANT-VIOLATION FORECAST, TRANSITION TABLE, LIFECYCLE EPOCH MAP, FORECAST VALIDATION, GATE B, INVALID TRANSITIONS, GATE C, RACE CONDITIONS, GATE D, FINDINGS.

---

## R18 Probe Summary

| Probe | Section modified | Candidate | V-01 | V-02 | V-03 | V-04 | V-05 |
|-------|-----------------|-----------|------|------|------|------|------|
| ROLES IS-authority self-declaration | ROLES opener | C-50 | YES | no | no | YES | YES |
| FORECAST VALIDATION IS-closure self-declaration | FORECAST VALIDATION opener | C-51 | no | YES | no | YES | YES |
| Per-constraint IS-derivation annotation | CONSTRAINT MATRIX Derivation column | C-52 | no | no | YES | no | YES |

**Standard in all R18 variants (promoted from R17 probes):**

| Criterion | Standard location | All variants |
|-----------|------------------|-------------|
| C-47 | VOCABULARY CLOSED opener (3 elements) | YES |
| C-48 | FINDINGS finding template Disposition field | YES |
| C-49 | All gate blocking conditions carry "IS derived from C-NN" | YES |