# trace-state — Round 18 Variations (R18)
# Skill: trace-state | Date: 2026-03-15 | Rubric: v16 (current)

Five complete, runnable skill body prompt variations for `trace-state`.
Each variation is a complete prompt body -- not a diff.

---

## R18 Gap Analysis

From R17 under current v16 rubric (41 aspirational criteria, C-09..C-50):

| Criterion | Status in R17 V-01..V-05 under v16 | R18 Path |
|-----------|------------------------------------|----------|
| C-48 (IS-negation register saturation) | PASS in R17 V-01 per rubric note; partial/absent in V-02–V-05 (IS-negation present in isolated sections, not saturated across all constraint-carrying sections) | Promote to STANDARD in ALL R18 variants; every constraint-carrying section must use IS/IS-NOT register |
| C-49 (Epoch-cluster defect analysis) | ABSENT in all R17 variants (LIFECYCLE EPOCH MAP present but never used as analysis surface; no post-FINDINGS epoch-cluster section exists) | Add dedicated EPOCH-CLUSTER ANALYSIS section after FINDINGS in all R18 variants; section maps each F-NN to epoch, counts defects per epoch, names highest-density epoch, states targeted remediation implication |
| C-50 (Artifact-level domain dependency declaration) | ABSENT in all R17 variants (all single-domain; C-50 is multi-domain only) | Introduce multi-domain variants (V-04, V-05); each must carry a top-scope DOMAIN DEPENDENCY DECLARATION before any pass naming source-of-record domain and full dependency chain |

**R17 ceiling under v16:** V-01 achieves C-48 PASS (82.2 projected). C-49 blocked by absent epoch-cluster section. C-50 blocked by single-domain format across all variants.

**R18 objective:** (1) C-48 saturation is STANDARD — every constraint-carrying section uses IS/IS-NOT register. (2) C-49 is STANDARD — EPOCH-CLUSTER ANALYSIS section appears after FINDINGS in every variant. (3) C-50 is introduced in V-04 and V-05 via multi-domain format with artifact-level DOMAIN DEPENDENCY DECLARATION.

**Structural additions:**

| Addition | Variants | Satisfies |
|----------|----------|-----------|
| EPOCH-CLUSTER ANALYSIS section (post-FINDINGS) | V-01, V-02, V-03, V-04, V-05 | C-49 |
| IS-negation register in GATE definitions, FINDINGS preamble, EPOCH-CLUSTER ANALYSIS preamble | V-01, V-02, V-03, V-04, V-05 | C-48 saturation |
| DOMAIN DEPENDENCY DECLARATION (top-scope, before first pass) | V-04, V-05 | C-50 |
| GATE D updated to block on EPOCH-CLUSTER ANALYSIS completion | V-01, V-02, V-03, V-04, V-05 | C-49 enforcement |

---

## Variation Axis Map

| Variation | Axis | Domain | New Probe | Predicted |
|-----------|------|--------|-----------|-----------|
| V-01 | Phrasing register: C-48 saturation verification | Sales | C-48 saturation confirmed across ALL constraint-carrying sections | 41/41 |
| V-02 | Lifecycle emphasis: C-49 epoch-cluster richness | Finance | C-49 with epoch-level remediation specificity | 41/41 |
| V-03 | Output format: step-block epoch-cluster | Customer Service | C-49 in step-block format (C-38/C-39 compatible) | 41/41 |
| V-04 | Role sequence x phrasing: Finance-first multi-pass + C-50 | Finance → Sales | C-50 dependency declaration + C-49 epoch-cluster spanning two domains | 41/41 |
| V-05 | Full synthesis: three-domain + all probes | Finance → Sales → CS | C-48 + C-49 + C-50 across three-domain dependency chain | 41/41 |

**V-01 hypothesis:** Sales domain (Lead / Qualified / Proposal / Negotiation / Closed-Won / Closed-Lost). Single-pass tabular. C-48 saturation: IS-negation register deployed in CONSTRAINT MATRIX authority, ROLES preamble, VOCABULARY CLOSED preamble, HANDOFF DECLARATION transfer statement, all GATE definitions, FINDINGS preamble, and EPOCH-CLUSTER ANALYSIS preamble. C-49: EPOCH-CLUSTER ANALYSIS section maps each F-NN to Sales lifecycle epoch (OPEN-TRACK / QUALIFY / ADVANCE / CLOSE-TRACK), counts defects per epoch, names highest-density epoch, states targeted remediation implication. No multi-domain; C-50 not applicable. Predicted: 41/41.

**V-02 hypothesis:** Finance domain (Invoice: Draft / Submitted / Under-Review / Approved / Paid / Disputed / Void). Single-pass tabular. C-48 standard. C-49 with expanded epoch-level specificity: epoch rationale column in LIFECYCLE EPOCH MAP, then post-FINDINGS epoch-cluster analysis names the lifecycle-arc position of the highest-density epoch and draws a remediation implication tied to the approval-gate boundary. Tests whether epoch rationale richness in LIFECYCLE EPOCH MAP improves the specificity of the C-49 remediation statement. Predicted: 41/41.

**V-03 hypothesis:** Customer Service domain (Support Ticket: New / Assigned / In-Progress / Pending-Customer / Resolved / Closed). Step-block output format (not tabular). C-48 standard. C-49: EPOCH-CLUSTER ANALYSIS appears as a labeled analysis block (step-block format) rather than a summary table. C-38/C-39 active (step-label criterion-instruction fusion + disqualification-condition fusion). Tests whether C-49 is satisfiable in step-block format. Predicted: 41/41.

**V-04 hypothesis:** Finance → Sales multi-domain multi-pass. Finance IS the source-of-record; Sales commitment state IS derived from Finance approval state. C-50: artifact-level DOMAIN DEPENDENCY DECLARATION before Pass 1 names source-of-record and full dependency chain using IS-negation register (simultaneously contributes to C-48). C-49: EPOCH-CLUSTER ANALYSIS spans both domain passes, maps cross-domain defects to epochs, identifies highest-density epoch across passes. C-40/C-41/C-42/C-47 active (multi-pass). Predicted: 41/41.

**V-05 hypothesis:** Finance → Sales → CS three-domain multi-pass. C-50: DOMAIN DEPENDENCY DECLARATION names all three domains and full two-hop dependency chain (Finance → Sales → CS). C-49: EPOCH-CLUSTER ANALYSIS spans three domain passes, counts defects per epoch across all three, identifies cross-domain epoch concentration. C-48: IS-negation saturation across all sections including cross-domain gate definitions and multi-pass HANDOFF DECLARATION. Full stack: C-38/C-39/C-40/C-41/C-42/C-47/C-48/C-49/C-50 simultaneously active. Domain portability tested: is the full criterion stack domain-agnostic across Sales, Finance, and CS lifecycles simultaneously? Predicted: 41/41.

---

## V-01 — Phrasing Register: C-48 Saturation Verification (Sales)

**Variation axis:** Phrasing register — IS-negation register saturation (C-48)
**Hypothesis:** Single-pass tabular. C-48 saturation: IS-negation register deployed in every constraint-carrying section (CONSTRAINT MATRIX authority statement, ROLES section preamble, VOCABULARY CLOSED preamble, HANDOFF DECLARATION transfer statement, all GATE definitions, FINDINGS preamble, EPOCH-CLUSTER ANALYSIS preamble). C-49: EPOCH-CLUSTER ANALYSIS section maps findings to Sales lifecycle epochs and states a targeted remediation implication. No multi-domain; C-50 not applicable. Predicted: 41/41.
**Domain:** Sales (Opportunity: Lead / Qualified / Proposal / Negotiation / Closed-Won / Closed-Lost)

---

### INERTIA BASELINE

The alternative to this trace IS: implement {{topic}} state management without hand-compiling transitions and invariants. The failure mode that alternative creates IS: invalid state transitions reach production because precondition checks were assumed rather than enumerated. This trace exists to close that gap before code is written. Every section that is skipped or left as a placeholder IS a return to the inertia baseline.

**PRODUCTION COST DECLARATION.** The production cost of the inertia baseline IS: sales opportunity records enter invalid state sequences — negotiating opportunities revert to lead stage without qualification records, closed-won opportunities remain active in pipeline reports, and closed-lost opportunities are reclassified as in-progress by automated forecasting tools. The cost IS NOT a misrouted record; the cost IS an opportunity in a state the system should have blocked, discovered by a forecast review rather than by the application. This IS the specific failure this trace exists to prevent. Any section of this document left blank or abbreviated IS already that failure, deferred.

**IS-NEGATION PAIR.** The inertia baseline IS NOT a process gap; it IS a sales integrity failure mode in the absence of this artifact. Choosing not to produce this trace IS NOT a risk accepted; it IS the failure mode instantiated before the feature ships. The existence of this document IS NOT documentation; it IS the artifact that converts that certainty into a prevented outcome.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. This trace IS a formal artifact; its governing document IS the CONSTRAINT MATRIX below. A Domain Expert [D] declares the vocabulary phase; a Trace Developer [T] executes the trace phase. [T]'s authorization IS CONTINGENT on [D] completing and executing a HANDOFF DECLARATION. The INERTIA BASELINE above IS the structural frame for this entire document. The CONSTRAINT MATRIX IS authoritative. Read it completely before producing any output.

---

### CONSTRAINT MATRIX

**MATRIX AUTHORITY.** The CONSTRAINT MATRIX IS the governing authority for this trace and IS NOT AMENDABLE by [D] or [T]. A constraint not named in this matrix IS NOT binding on this trace. A violation not classifiable by a named constraint IS NOT a violation under this matrix. No role IS authorized to add, waive, or modify a constraint. The scope of this matrix IS total: every compliance obligation in this trace IS traceable to a named constraint row. A section without a named constraint row IS NOT a governed section; producing ungoverned output IS NOT authorized.

| ID | Architectural Fact | Assigned Role | Concern |
|----|--------------------|---------------|---------|
| C1 | A state name not declared in STATE DECLARATIONS IS PROHIBITED in any trace table | [T] | vocabulary |
| C2 | An operation name not declared in OPERATION DECLARATIONS IS PROHIBITED in any trace table | [T] | vocabulary |
| C3 | The TRANSITION TABLE includes an EPOCH column. The EPOCH column IS informational; it IS NOT constrained by C1 or C2. EPOCH values ARE drawn from Sales lifecycle phase vocabulary (e.g., OPEN-TRACK / QUALIFY / ADVANCE / CLOSE-TRACK) and ARE NOT required to match declared S-IDs. An EPOCH value that does not appear in STATE DECLARATIONS IS NOT a C1 violation. EPOCH data IS used to generate the LIFECYCLE EPOCH MAP secondary artifact. Prose paragraphs and bullet lists ARE NOT VALID as primary trace output; every operation IS REQUIRED as a table row. | [T] | format / scope |
| C4 | Any state or operation added after VOCABULARY CLOSED IS declared IS a retroactive violation; such additions ARE PROHIBITED | [D] | ordering |
| C5 | A blank invariant status cell in the TRANSITION TABLE IS NOT PERMITTED; every cell IS REQUIRED to contain HOLDS or VIOLATED | [T] | integrity |
| C6 | TRANSITION TABLE IS BLOCKED until GATE A IS confirmed AND INVARIANT-VIOLATION FORECAST IS complete | [T] | ordering |
| C7 | A blank or non-option response at INVENTORY CHALLENGE IS a C7 violation; GATE A IS BLOCKED in the presence of a C7 violation | [T] | completeness |
| C8 | INVALID TRANSITIONS IS BLOCKED until GATE B IS confirmed | [T] | ordering |
| C9 | RACE CONDITIONS IS BLOCKED until GATE C IS confirmed | [T] | ordering |
| C10 | STATE DIAGRAM [D] IS NOT a substitute for the TRANSITION TABLE; it IS the structural cross-check artifact. [D] IS REQUIRED to declare node count, edge count, and [!] annotation count at authoring time. An [!] IS REQUIRED on every edge whose operation IS predicted VIOLATED in INVARIANT-VIOLATION FORECAST; a forecast row predicting VIOLATED without a corresponding [!] in STATE DIAGRAM IS a C10 violation. | [D] | integrity |

---

### ROLES

**ROLES IS NOT an organizational chart; ROLES IS the execution authority matrix for this trace. A section of this document without a named role assignment IS NOT shared ownership; it IS unowned obligation and IS the inertia baseline instantiated before any section IS produced. Every ownership claim below IS NOT advisory; it IS the assignment that makes execution authorized. An obligation not assigned to a named role IS NOT deferred; it IS absent.**

**[D] Domain Expert**
Auto-selected: Sales expert (Lead / Qualified / Proposal / Negotiation / Closed-Won / Closed-Lost).
Sections owned by [D]: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION.
Binding constraint: **C4** (vocabulary IS FROZEN after VOCABULARY CLOSED IS declared; retroactive additions ARE PROHIBITED).
INERTIA BASELINE relationship: [D]'s incomplete declarations ARE a return to the INERTIA BASELINE state named above. **[D]'s obligation IS NOT advisory documentation; it IS the prevention mechanism that separates this trace from an assumption about the sales opportunity state machine.** Incomplete [D] declarations ARE NOT a deferral; they ARE the inertia baseline instantiated before [T] has written a single row. The specific regression form [D] prevents IS: unvalidated opportunity state vocabulary reaching the trace phase.

**[T] Trace Developer**
Sections owned by [T]: INVENTORY CHALLENGE response, INVARIANT-VIOLATION FORECAST, TRANSITION TABLE, LIFECYCLE EPOCH MAP, FORECAST VALIDATION, INVALID TRANSITIONS, RACE CONDITIONS, FINDINGS, EPOCH-CLUSTER ANALYSIS.
Binding constraints: **C1, C2, C3, C5, C6, C7, C8, C9, C10**.
Authorization status: [T]'s authorization IS CONTINGENT on HANDOFF DECLARATION. Prior to HANDOFF DECLARATION, [T] IS NOT AUTHORIZED to produce output in any [T]-owned section.
INERTIA BASELINE relationship: [T]'s incomplete trace rows ARE a return to the INERTIA BASELINE state named above. **[T]'s obligation IS NOT iterative development; it IS the commitment that converts the inertia certainty named above into a prevented outcome.** A blank [T] section IS NOT an in-progress state; it IS the inertia baseline already chosen. The specific regression form [T] prevents IS: untraced opportunity transitions shipping as assumed-valid precondition logic.

---

### STATE DECLARATIONS [D]

Declare all lifecycle states as numbered prose items with inline definitional clauses. Each entry IS REQUIRED to name: (a) the conditions that cause entry into this state, (b) the field values that characterize it, and (c) whether it is terminal. Generic labels ARE PROHIBITED; domain vocabulary IS REQUIRED.

**S-01.** [State Name] — [inline definitional clause: entry conditions, characterizing field values, terminal status, and what distinguishes this state from all others in the lifecycle]. Terminal: Yes/No.
**S-02.** [State Name] — [inline definitional clause]. Terminal: Yes/No.
*(continue for all lifecycle states; Sales typical set: Lead, Qualified, Proposal, Negotiation, Closed-Won, Closed-Lost)*

A STATE DECLARATIONS section without at least one Terminal: Yes entry IS INCOMPLETE. STATE DECLARATIONS IS BLOCKED until this condition IS met. Do not begin OPERATION DECLARATIONS until STATE DECLARATIONS IS COMPLETE.

---

### OPERATION DECLARATIONS [D]

Declare all lifecycle operations as numbered prose items with inline definitional clauses. Each entry IS REQUIRED to name: (a) what the operation does, (b) when it is triggered, (c) all legal source states by S-ID, and (d) the target state by S-ID. An operation entry without S-ID references IS NOT VALID.

**O-01.** [Operation Name] — [inline definitional clause]. From: S-[N][, S-[N]...]. To: S-[N]. Actor: [role/system].
**O-02.** [Operation Name] — [inline definitional clause]. From: S-[N]. To: S-[N]. Actor: [role/system].
*(continue for all lifecycle operations)*

All S-IDs ARE REQUIRED to reference STATE DECLARATIONS entries. Do not begin INVARIANT DECLARATIONS until OPERATION DECLARATIONS IS COMPLETE.

---

### INVARIANT DECLARATIONS [D]

Declare all object-level invariants as numbered items. Each item IS REQUIRED to include a boolean assertion and an authority source. A declaration without a boolean assertion IS NOT VALID.

**INV-01.** [Name] — [boolean assertion]. Authority: [source].
**INV-02.** [Name] — [boolean assertion]. Authority: [source].
*(minimum two invariants required; INVARIANT DECLARATIONS IS BLOCKED until two valid entries ARE present)*

---

### VOCABULARY CLOSED [D]

**VOCABULARY CLOSED IS NOT a label; it IS the irreversibility event. The moment this declaration IS present in the document, [D]'s authority to introduce, modify, or redefine any state or operation name IS extinguished. The vocabulary IS NOT closeable by reference to this section; it IS closed by the existence of this declaration. Any name not listed below IS NOT part of the declared vocabulary and IS PROHIBITED in all subsequent sections; any name listed below IS permanently frozen.**

> VOCABULARY CLOSED per C4. States: [list all S-IDs and State Names from STATE DECLARATIONS]. Operations: [list all O-IDs and Operation Names from OPERATION DECLARATIONS]. The vocabulary IS FROZEN. Any state name or operation name not listed above IS PROHIBITED in all subsequent sections. This prohibition IS NOT WAIVABLE and IS NOT CONTINGENT on any further action.

HANDOFF DECLARATION IS BLOCKED until VOCABULARY IS FROZEN. Executing HANDOFF DECLARATION before this declaration IS a C4 violation.

---

### STATE DIAGRAM [D]

This STATE DIAGRAM IS NOT a substitute for the TRANSITION TABLE; it IS the structural cross-check artifact that makes transition-coverage falsifiable before [T] begins tracing. Nodes: one per declared S-ID. Edges: one per valid (From State, Operation) pair in OPERATION DECLARATIONS. **[!] annotation:** applied to every edge whose operation IS predicted VIOLATED in INVARIANT-VIOLATION FORECAST; every [!] implies a forecast VIOLATED prediction; every VIOLATED prediction implies a [!] in this diagram. A mismatch IS a C10 violation.

Produce the STATE DIAGRAM as an annotated edge list:

**Nodes:**
- S-[NN]: [State Name] *(Terminal)* or *(Non-terminal)*

**Edges:**
- S-[NN] --[O-NN: Operation Name]--> S-[NN] [optional: [!] INVARIANT RISK: reason if predicted VIOLATED]

**Structural counts (declared at authoring time):**
- Node count: [N] (MUST equal S-ID count in STATE DECLARATIONS)
- Edge count: [N] (MUST equal total valid From/To operation pairs across all O-IDs)
- [!] annotation count: [N] (MUST equal count of VIOLATED-predicted O-ID rows in INVARIANT-VIOLATION FORECAST)

---

### HANDOFF DECLARATION [D]

> **[D] HANDOFF DECLARATION.**
>
> **TRANSFER DECLARATION.** This HANDOFF IS NOT a coordination event; it IS the formal instantiation of production responsibility transfer. [D]'s declaration authority IS extinguished at this moment; [T]'s trace authorization IS created at this moment. The HANDOFF IS NOT a record of completion; it IS the causal event that makes completion possible. A HANDOFF DECLARATION that IS skipped or abbreviated IS NOT a shortcut; it IS the absence of the event that authorizes [T] to proceed.
>
> Transferring role IS: [D] (Domain Expert — Sales expert).
> Receiving role IS: [T] (Trace Developer).
>
> Artifacts transferred ARE:
> 1. STATE DECLARATIONS (S-01 through S-[N])
> 2. OPERATION DECLARATIONS (O-01 through O-[N])
> 3. INVARIANT DECLARATIONS (INV-01 through INV-[N])
> 4. STATE DIAGRAM [D]: This artifact IS NOT a substitute for the TRANSITION TABLE; it IS the structural cross-check that makes node/edge coverage falsifiable. Node count: [N]. Edge count: [N]. [!] annotation count: [N]. A STATE DIAGRAM transferred with counts not matching declarations IS NOT an accepted artifact.
> 5. VOCABULARY CLOSED: IS in effect. The vocabulary IS FROZEN. Retroactive modifications by [D] ARE PROHIBITED.
>
> **Post-transfer role states (both declared simultaneously at this moment):**
> [D] IS PROHIBITED from altering any declaration in STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, or STATE DIAGRAM from this point forward. [D]'s modification authority IS REVOKED. This prohibition IS NOT WAIVABLE.
> [T] IS NOW AUTHORIZED to produce output in all [T]-owned sections. [T] WAS NOT AUTHORIZED prior to this moment; [T] IS AUTHORIZED now.
>
> Acceptance condition: [T] IS REQUIRED to write an explicit Option A or Option B response to INVENTORY CHALLENGE before GATE A IS cleared. GATE A IS BLOCKED until this acceptance IS written.
>
> **[D] Signed:** Sales expert — [N] states (S-01 through S-[N]), [N] operations (O-01 through O-[N]), [N] invariants (INV-01 through INV-[N]), STATE DIAGRAM ([N] nodes, [N] edges, [N] [!] annotations) ARE DECLARED AND CLOSED.

---

### INVENTORY CHALLENGE

**C7 applies. A blank or non-option response IS a C7 violation. GATE A IS BLOCKED in the presence of a C7 violation.**

INVENTORY IS DECLARED COMPLETE — the STATE DECLARATIONS and OPERATION DECLARATIONS contain every state and operation in the lifecycle of {{topic}}.

**[T] response — one option IS REQUIRED:**

**Option A (CONFIRMED):** "[T] INVENTORY CONFIRMED. The STATE DECLARATIONS and OPERATION DECLARATIONS ARE the complete lifecycle vocabulary for {{topic}}. No lifecycle state or operation IS absent. States: [repeat S-IDs and names]. Operations: [repeat O-IDs and names]. HANDOFF DECLARATION IS ACKNOWLEDGED. [T]'s authorization IS IN EFFECT. Proceeding to GATE A."

**Option B (GAP FOUND):** "[T] INVENTORY INCOMPLETE. Gap identified: [missing state or operation]. Returning to [D] for declaration update. VOCABULARY CLOSED MUST be re-declared and HANDOFF DECLARATION re-signed before GATE A IS unblocked."

---

### GATE A

**GATE A IS NOT a checkpoint list; it IS the enforcement mechanism that makes [T]'s authorization conditional on named completion conditions. GATE A IS NOT clearable by assertion; it IS clearable only when every item below IS confirmed. A partially-confirmed GATE A IS NOT a cleared GATE A; it IS a blocked gate.**

Gate clearance IS a two-party completion: [D]'s signed HANDOFF DECLARATION IS the first completion; [T]'s written INVENTORY CHALLENGE acceptance IS the second. Both ARE REQUIRED. [T] IS BLOCKED from proceeding to INVARIANT-VIOLATION FORECAST until all items below ARE confirmed.

- [ ] INERTIA BASELINE IS present as document opener, includes PRODUCTION COST DECLARATION with IS NOT X / IS Y contrast framing, and includes IS-NEGATION PAIR — **this blocking condition IS derived from C-27/C-30/C-33/C-37**
- [ ] CONSTRAINT MATRIX IS-authority preamble IS present — governing-authority declaration IS written before C1 row — **this blocking condition IS derived from the MATRIX AUTHORITY requirement**
- [ ] ROLES section carries IS-authority self-declaration opener AND per-role IS-negation obligation pair for both [D] and [T] with specific regression form named — **this blocking condition IS derived from C-43/C-36**
- [ ] STATE DECLARATIONS ARE complete — domain vocabulary, inline definitional clauses, at least one Terminal: Yes item IS present — **this blocking condition IS derived from C-01/C-09/C-23**
- [ ] OPERATION DECLARATIONS ARE complete — all S-ID references ARE resolved to STATE DECLARATIONS — **this blocking condition IS derived from C-02/C-23**
- [ ] INVARIANT DECLARATIONS ARE complete — at least two boolean assertions with authority sources ARE present
- [ ] VOCABULARY CLOSED IS declared — IS-event self-declaration IS present as opener; vocabulary IS FROZEN; prohibition IS NOT WAIVABLE — **this blocking condition IS derived from C-15**
- [ ] STATE DIAGRAM [D] IS complete — node count, edge count, [!] annotation count ARE declared and consistent — **this blocking condition IS derived from C-10**
- [ ] HANDOFF DECLARATION IS signed — TRANSFER DECLARATION IS-transfer opener IS present; post-transfer role states ([D] IS PROHIBITED, [T] IS NOW AUTHORIZED) ARE explicitly declared — **this blocking condition IS derived from C-22/C-25/C-26/C-32/C-39**
- [ ] **[C7]** INVENTORY CHALLENGE IS resolved — Option A or Option B IS written; no C7 violation IS present
- [ ] **[C-14]** [T] confirms: no name WILL appear in any trace table that IS NOT declared in STATE DECLARATIONS or OPERATION DECLARATIONS
- [ ] **[C-09]** Terminal states ARE identified; at least one Terminal item WILL appear as From State in INVALID TRANSITIONS

**GATE A: [T] IS BLOCKED from proceeding. INVARIANT-VIOLATION FORECAST IS BLOCKED until all items ARE confirmed.**

---

### INVARIANT-VIOLATION FORECAST [T]

**TRANSITION TABLE IS BLOCKED until INVARIANT-VIOLATION FORECAST IS complete per C6.**

**FORECAST COMMITMENT.** This FORECAST IS a formal commitment, not a guess. A blank O-ID row IS a C6 violation already instantiated at authoring time. The FORECAST IS the contract; FORECAST VALIDATION IS the audit of that contract.

| O-ID | Operation Name | Predicted INV-01 | Predicted INV-02 | Rationale |
|------|----------------|-----------------|-----------------|-----------|
| O-[N] | [name from OPERATION DECLARATIONS] | HOLDS / VIOLATED | HOLDS / VIOLATED | [why this operation IS or IS NOT expected to produce a violation] |
*(one row per declared operation; blanks ARE NOT PERMITTED)*

---

### TRANSITION TABLE [T]

Scenario setup: [entity instance, starting state, actor, date/time context]

Constraints C1, C2, C3, C5 ARE in effect. EPOCH column IS informational per C3.

| # | From State (S-ID) | Operation (O-ID) | Preconditions | To State (S-ID) | Postconditions | INV-01 | INV-02 | EPOCH (informational) | Side Effects |
|---|-------------------|-----------------|---------------|-----------------|----------------|--------|--------|----------------------|--------------|

- **From State / To State:** S-IDs only (C1).
- **Operation:** O-IDs only (C2).
- **EPOCH:** Sales lifecycle phase label (e.g., OPEN-TRACK / QUALIFY / ADVANCE / CLOSE-TRACK); informational only, IS NOT constrained by C1/C2 per C3.
- **Preconditions:** Minimum two testable assertions per row.
- **Postconditions:** Minimum one assertion distinct from the To State name.
- **INV columns:** `HOLDS` or `VIOLATED — [reason]`; blank IS NOT PERMITTED (C5).
- **Side Effects:** Triggered rules, notifications, async jobs, record changes.

---

### LIFECYCLE EPOCH MAP [T]

Map each declared operation to its lifecycle epoch. This IS informational per CONSTRAINT MATRIX C3; scope IS NOT constrained by C1/C2.

| O-ID | Operation Name | Lifecycle Epoch | Epoch Rationale |
|------|----------------|-----------------|-----------------|
| O-[N] | [from OPERATION DECLARATIONS] | OPEN-TRACK / QUALIFY / ADVANCE / CLOSE-TRACK | [why this operation belongs to this epoch in the Sales lifecycle arc] |
*(one row per declared operation)*

---

### FORECAST VALIDATION [T]

Compare INVARIANT-VIOLATION FORECAST predictions against actual TRANSITION TABLE results.

| O-ID | Predicted INV-01 | Actual INV-01 | Predicted INV-02 | Actual INV-02 | Forecast Status |
|------|-----------------|--------------|-----------------|--------------|-----------------|
| O-[N] | [from forecast] | [from table] | [from forecast] | [from table] | CONFIRMED / REFUTED — [explanation if refuted] |

A REFUTED forecast IS a required finding in FINDINGS.

---

### GATE B

**GATE B IS NOT a checkpoint list; it IS the enforcement mechanism that makes INVALID TRANSITIONS authorization conditional on TRANSITION TABLE completeness. GATE B IS NOT clearable by assertion; it IS clearable only when every item below IS confirmed.**

- [ ] TRANSITION TABLE IS columnar and complete; no operation IS documented only in prose — **this blocking condition IS derived from C-08/C-13**
- [ ] Every row HAS INV status per declared invariant; at least one VIOLATED row IS present — **this blocking condition IS derived from C-05**
- [ ] Every row HAS at least one postcondition distinct from the To State name — **this blocking condition IS derived from C-03**
- [ ] LIFECYCLE EPOCH MAP IS complete — every O-ID IS mapped to a lifecycle epoch — **this blocking condition IS derived from C-31**
- [ ] FORECAST VALIDATION IS complete — every O-ID IS compared; REFUTED rows ARE flagged as findings

**GATE B: [T] IS BLOCKED from proceeding. INVALID TRANSITIONS IS BLOCKED until all items ARE confirmed.**

---

### INVALID TRANSITIONS [T]

| # | Attempted Operation (O-ID) | From State (S-ID) | Blocking Condition | INV Reference | Risk if Bypassed |
|---|---------------------------|------------------|--------------------|--------------|-----------------|

Minimum three rows. At least one row WHERE From State IS a Terminal item from STATE DECLARATIONS IS REQUIRED. S-IDs and O-IDs only (C1, C2).

---

### GATE C

**GATE C IS NOT a checkpoint list; it IS the enforcement mechanism that makes RACE CONDITIONS authorization conditional on INVALID TRANSITIONS completeness. GATE C IS NOT clearable by assertion; it IS clearable only when every item below IS confirmed.**

- [ ] At least three (operation, state) invalid pairs ARE named with blocking conditions; enumeration IS systematic — **this blocking condition IS derived from C-04/C-12**
- [ ] At least one INVALID TRANSITIONS row HAS From State = a Terminal item from STATE DECLARATIONS — **this blocking condition IS derived from C-09**

**GATE C: [T] IS BLOCKED from proceeding. RACE CONDITIONS IS BLOCKED until all items ARE confirmed.**

---

### RACE CONDITIONS [T]

| Operation A (O-ID) | Operation B (O-ID) | Unsafe Interleaving | Outcome | Mitigation |
|--------------------|--------------------|---------------------|---------|-----------|

If no concurrent access: "No concurrent access — [reason explaining why concurrent access IS NOT POSSIBLE for this object type]."

---

### GATE D

**GATE D IS NOT a checkpoint list; it IS the enforcement mechanism that makes FINDINGS and EPOCH-CLUSTER ANALYSIS authorization conditional on full trace completeness. GATE D IS NOT clearable by assertion; it IS clearable only when every item below IS confirmed. A GATE D not fully confirmed IS NOT a cleared gate; it IS an authorization block on both FINDINGS and EPOCH-CLUSTER ANALYSIS.**

- [ ] RACE CONDITIONS ARE addressed — at least one race scenario or explicit clearance with reason IS present
- [ ] FORECAST VALIDATION IS included — REFUTED forecasts ARE flagged as findings
- [ ] LIFECYCLE EPOCH MAP IS complete — all O-IDs ARE mapped to epochs — **this blocking condition IS derived from C-31; EPOCH-CLUSTER ANALYSIS IS BLOCKED without a complete LIFECYCLE EPOCH MAP**
- [ ] All TRANSITION TABLE and INVALID TRANSITIONS S-IDs and O-IDs ARE resolved to declarations (C1, C2)
- [ ] Hard-stop review IS complete — no section IS blank or placeholder-only

**GATE D: [T] IS BLOCKED from proceeding. FINDINGS IS BLOCKED until all items ARE confirmed. EPOCH-CLUSTER ANALYSIS IS BLOCKED until FINDINGS IS complete.**

---

### FINDINGS [T]

**FINDINGS IS NOT an observation log; it IS the derivation layer.** A finding IS NOT valid if it cannot be traced to a named record in TRANSITION TABLE, INVALID TRANSITIONS, FORECAST VALIDATION, or RACE CONDITIONS. A finding IS NOT a priority finding if it IS NOT traceable to the INERTIA BASELINE failure mode; such a finding IS background noise. FINDINGS IS NOT complete until every REFUTED forecast row IS named as a finding.

**Inertia connection IS REQUIRED on every finding.** A finding template without an Inertia connection field IS NOT a valid finding entry under this document.

**Disposition IS REQUIRED on every finding.** A finding without a Disposition field IS NOT a valid finding entry. Disposition MUST use IS-phrased values.

Priority order. Any REFUTED invariant-violation forecast IS a required finding.

- **P[N]: [title]**
  Source: [TRANSITION TABLE row N / INVALID TRANSITIONS row N / FORECAST VALIDATION O-[N] / RACE CONDITIONS entry N].
  Inertia connection: [how this finding traces to the INERTIA BASELINE failure mode named above; a finding without this field IS background noise].
  Disposition: [Status IS ACCEPTED / Status IS REJECTED — IS NOT traceable to INERTIA BASELINE / Action IS REQUIRED before feature ships / Action IS NOT PERMITTED until this finding IS resolved].
  Severity: FATAL / DEGRADED / COSMETIC.

---

### EPOCH-CLUSTER ANALYSIS [T]

**EPOCH-CLUSTER ANALYSIS IS NOT a summary of FINDINGS; it IS the analytical transformation that converts the LIFECYCLE EPOCH MAP from a labeling artifact into a defect-density surface. EPOCH-CLUSTER ANALYSIS IS NOT optional; it IS the section that makes the LIFECYCLE EPOCH MAP produce a remediation claim. EPOCH-CLUSTER ANALYSIS IS BLOCKED until FINDINGS IS complete AND the LIFECYCLE EPOCH MAP IS present with all O-IDs mapped. A post-trace section that enumerates findings without mapping them to epochs IS NOT an EPOCH-CLUSTER ANALYSIS; it IS an observation list.**

For each finding in FINDINGS, identify the epoch of the triggering operation using the LIFECYCLE EPOCH MAP:

**Finding-to-epoch mapping:**

| Finding ID | Title | Triggering Operation (O-ID) | Lifecycle Epoch | Defect Type |
|------------|-------|----------------------------|-----------------|-------------|
| F-[N] | [finding title from FINDINGS] | O-[N] | [epoch from LIFECYCLE EPOCH MAP] | [INVARIANT VIOLATION / INVALID TRANSITION / RACE CONDITION / FORECAST REFUTATION] |
*(one row per finding in FINDINGS)*

**Epoch defect counts:**

| Lifecycle Epoch | Defect Count | Finding IDs |
|-----------------|-------------|-------------|
| OPEN-TRACK | [N] | [F-NN, ...] |
| QUALIFY | [N] | [F-NN, ...] |
| ADVANCE | [N] | [F-NN, ...] |
| CLOSE-TRACK | [N] | [F-NN, ...] |
*(epochs with zero defects ARE included; epoch count IS derived from LIFECYCLE EPOCH MAP)*

**Highest-density epoch:** [Epoch name] — [N] of [total] defects (finding IDs: [F-NN, ...]).

**Epoch position in lifecycle arc:** [Where the highest-density epoch sits — early / mid / late — and what that means for the defect pattern. E.g., "CLOSE-TRACK IS the terminal epoch of the Sales lifecycle arc; defect density here IS NOT random; it IS the accumulated result of precondition checks that were deferred through OPEN-TRACK and QUALIFY."]

**Remediation implication:** [Specific gate or transition to harden, tied to the epoch's position. Must name the specific operation boundary or approval gate. E.g., "CLOSE-TRACK epoch carries 3 of 4 defects — approval-gate hardening at the Negotiation → Closed-Won transition (O-[N]) IS the highest-leverage intervention; the precondition check that IS currently assumed IS the defect source in [N] of [N] CLOSE-TRACK findings." Generic statements such as 'investigate the late stages' ARE NOT VALID remediation implications; they ARE placeholders that fail C-49.]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: INERTIA BASELINE, CONSTRAINT MATRIX, ROLES, STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION, INVENTORY CHALLENGE, GATE A, INVARIANT-VIOLATION FORECAST, TRANSITION TABLE, LIFECYCLE EPOCH MAP, FORECAST VALIDATION, GATE B, INVALID TRANSITIONS, GATE C, RACE CONDITIONS, GATE D, FINDINGS, EPOCH-CLUSTER ANALYSIS.

---

## V-02 — Lifecycle Emphasis: Epoch-Cluster Remediation Specificity (Finance)

**Variation axis:** Lifecycle emphasis — C-49 epoch-cluster analysis with expanded epoch rationale richness
**Hypothesis:** Finance domain (Invoice: Draft / Submitted / Under-Review / Approved / Paid / Disputed / Void). Single-pass tabular. C-48 standard. C-49 primary probe: LIFECYCLE EPOCH MAP carries an expanded Epoch Rationale column that names each epoch's position in the Finance lifecycle arc (e.g., "ORIGINATION epoch IS the entry boundary; defects here ARE data-quality defects, not approval-gate defects"). The EPOCH-CLUSTER ANALYSIS section uses this rationale to produce a more precise remediation implication — not just naming the highest-density epoch but naming the specific approval gate within the epoch that IS the intervention point. Tests whether epoch rationale richness in LIFECYCLE EPOCH MAP improves C-49 remediation specificity. Predicted: 41/41.
**Domain:** Finance (Invoice: Draft / Submitted / Under-Review / Approved / Paid / Disputed / Void)

---

### INERTIA BASELINE

The alternative to this trace IS: implement {{topic}} state management without hand-compiling transitions and invariants. The failure mode that alternative creates IS: invalid state transitions reach production because precondition checks were assumed rather than enumerated. This trace exists to close that gap before code is written. Every section that is skipped or left as a placeholder IS a return to the inertia baseline.

**PRODUCTION COST DECLARATION.** The production cost of the inertia baseline IS: invoice records enter invalid state sequences — approved invoices remain under-review in payment queues, paid invoices appear disputed in reconciliation reports, and voided invoices re-enter the approval workflow as active records. The cost IS NOT a delayed payment; the cost IS a financial record in a state the system should have blocked, discovered by a period-close audit rather than by the application. This IS the specific failure this trace exists to prevent. Any section of this document left blank or abbreviated IS already that failure, deferred.

**IS-NEGATION PAIR.** The inertia baseline IS NOT a process gap; it IS a financial integrity failure mode in the absence of this artifact. Choosing not to produce this trace IS NOT a risk accepted; it IS the failure mode instantiated before the feature ships. The existence of this document IS NOT documentation; it IS the artifact that converts that certainty into a prevented outcome.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace. This trace IS a formal artifact; its governing document IS the CONSTRAINT MATRIX below. A Domain Expert [D] declares the vocabulary phase; a Trace Developer [T] executes the trace phase. [T]'s authorization IS CONTINGENT on [D] completing and executing a HANDOFF DECLARATION. The INERTIA BASELINE above IS the structural frame for this entire document. The CONSTRAINT MATRIX IS authoritative. Read it completely before producing any output.

---

### CONSTRAINT MATRIX

**MATRIX AUTHORITY.** The CONSTRAINT MATRIX IS the governing authority for this trace and IS NOT AMENDABLE by [D] or [T]. A constraint not named in this matrix IS NOT binding on this trace. A violation not classifiable by a named constraint IS NOT a violation under this matrix. No role IS authorized to add, waive, or modify a constraint. The scope of this matrix IS total: every compliance obligation in this trace IS traceable to a named constraint row.

| ID | Architectural Fact | Assigned Role | Concern |
|----|--------------------|---------------|---------|
| C1 | A state name not declared in STATE DECLARATIONS IS PROHIBITED in any trace table | [T] | vocabulary |
| C2 | An operation name not declared in OPERATION DECLARATIONS IS PROHIBITED in any trace table | [T] | vocabulary |
| C3 | The TRANSITION TABLE includes an EPOCH column. The EPOCH column IS informational; it IS NOT constrained by C1 or C2. EPOCH values ARE drawn from Finance lifecycle phase vocabulary (e.g., ORIGINATION / REVIEW / APPROVAL / SETTLEMENT) and ARE NOT required to match declared S-IDs. An EPOCH value that does not appear in STATE DECLARATIONS IS NOT a C1 violation. EPOCH data IS used to generate the LIFECYCLE EPOCH MAP secondary artifact. Prose paragraphs and bullet lists ARE NOT VALID as primary trace output; every operation IS REQUIRED as a table row. | [T] | format / scope |
| C4 | Any state or operation added after VOCABULARY CLOSED IS declared IS a retroactive violation; such additions ARE PROHIBITED | [D] | ordering |
| C5 | A blank invariant status cell in the TRANSITION TABLE IS NOT PERMITTED; every cell IS REQUIRED to contain HOLDS or VIOLATED | [T] | integrity |
| C6 | TRANSITION TABLE IS BLOCKED until GATE A IS confirmed AND INVARIANT-VIOLATION FORECAST IS complete | [T] | ordering |
| C7 | A blank or non-option response at INVENTORY CHALLENGE IS a C7 violation; GATE A IS BLOCKED in the presence of a C7 violation | [T] | completeness |
| C8 | INVALID TRANSITIONS IS BLOCKED until GATE B IS confirmed | [T] | ordering |
| C9 | RACE CONDITIONS IS BLOCKED until GATE C IS confirmed | [T] | ordering |
| C10 | STATE DIAGRAM [D] IS NOT a substitute for the TRANSITION TABLE; it IS the structural cross-check artifact. [D] IS REQUIRED to declare node count, edge count, and [!] annotation count at authoring time. An [!] IS REQUIRED on every edge whose operation IS predicted VIOLATED in INVARIANT-VIOLATION FORECAST; a forecast row predicting VIOLATED without a corresponding [!] in STATE DIAGRAM IS a C10 violation. | [D] | integrity |

---

### ROLES

**ROLES IS NOT an organizational chart; ROLES IS the execution authority matrix for this trace. A section of this document without a named role assignment IS NOT shared ownership; it IS unowned obligation and IS the inertia baseline instantiated before any section IS produced. Every ownership claim below IS NOT advisory; it IS the assignment that makes execution authorized. An obligation not assigned to a named role IS NOT deferred; it IS absent.**

**[D] Domain Expert**
Auto-selected: Finance expert (Draft / Submitted / Under-Review / Approved / Paid / Disputed / Void).
Sections owned by [D]: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION.
Binding constraint: **C4** (vocabulary IS FROZEN after VOCABULARY CLOSED IS declared; retroactive additions ARE PROHIBITED).
INERTIA BASELINE relationship: [D]'s incomplete declarations ARE a return to the INERTIA BASELINE state named above. **[D]'s obligation IS NOT advisory documentation; it IS the prevention mechanism that separates this trace from an assumption about the invoice lifecycle state machine.** The specific regression form [D] prevents IS: unvalidated invoice state vocabulary reaching the trace phase.

**[T] Trace Developer**
Sections owned by [T]: INVENTORY CHALLENGE response, INVARIANT-VIOLATION FORECAST, TRANSITION TABLE, LIFECYCLE EPOCH MAP, FORECAST VALIDATION, INVALID TRANSITIONS, RACE CONDITIONS, FINDINGS, EPOCH-CLUSTER ANALYSIS.
Binding constraints: **C1, C2, C3, C5, C6, C7, C8, C9, C10**.
Authorization status: [T]'s authorization IS CONTINGENT on HANDOFF DECLARATION. Prior to HANDOFF DECLARATION, [T] IS NOT AUTHORIZED to produce output in any [T]-owned section.
INERTIA BASELINE relationship: The specific regression form [T] prevents IS: untraced invoice transitions shipping as assumed-valid financial approval rules.

---

### STATE DECLARATIONS [D]

*(same structure as V-01; domain vocabulary: Draft, Submitted, Under-Review, Approved, Paid, Disputed, Void)*

**S-01.** [State Name] — [inline definitional clause]. Terminal: Yes/No.
*(continue; Finance typical set: Draft, Submitted, Under-Review, Approved, Paid, Disputed, Void)*

---

### OPERATION DECLARATIONS [D]

*(same structure as V-01; domain: invoice submission, review, approval, payment, dispute, void operations)*

**O-01.** [Operation Name] — [inline definitional clause]. From: S-[N][, S-[N]...]. To: S-[N]. Actor: [role/system].
*(continue for all lifecycle operations)*

---

### INVARIANT DECLARATIONS [D]

**INV-01.** [Name] — [boolean assertion]. Authority: [source].
**INV-02.** [Name] — [boolean assertion]. Authority: [source].

---

### VOCABULARY CLOSED [D]

**VOCABULARY CLOSED IS NOT a label; it IS the irreversibility event. The moment this declaration IS present in the document, [D]'s authority to introduce, modify, or redefine any state or operation name IS extinguished. Any name not listed below IS PROHIBITED in all subsequent sections; this prohibition IS NOT WAIVABLE.**

> VOCABULARY CLOSED per C4. States: [list]. Operations: [list]. The vocabulary IS FROZEN. This prohibition IS NOT CONTINGENT on any further action.

---

### STATE DIAGRAM [D]

*(same structure as V-01; Finance domain)*

**Nodes:** S-[NN]: [State Name] *(Terminal / Non-terminal)*
**Edges:** S-[NN] --[O-NN: Operation Name]--> S-[NN] [optional [!] INVARIANT RISK]
**Structural counts:** Node count: [N]. Edge count: [N]. [!] annotation count: [N].

---

### HANDOFF DECLARATION [D]

> **[D] HANDOFF DECLARATION.**
>
> **TRANSFER DECLARATION.** This HANDOFF IS NOT a coordination event; it IS the formal instantiation of production responsibility transfer. [D]'s declaration authority IS extinguished at this moment; [T]'s trace authorization IS created at this moment. The HANDOFF IS NOT a record of completion; it IS the causal event that makes completion possible.
>
> Transferring role IS: [D] (Domain Expert — Finance expert).
> Receiving role IS: [T] (Trace Developer).
>
> Artifacts transferred ARE: STATE DECLARATIONS (S-01 through S-[N]), OPERATION DECLARATIONS (O-01 through O-[N]), INVARIANT DECLARATIONS (INV-01 through INV-[N]), STATE DIAGRAM ([N] nodes, [N] edges, [N] [!] annotations), VOCABULARY CLOSED (IS in effect; retroactive modifications ARE PROHIBITED).
>
> [D] IS PROHIBITED from altering any declaration from this point forward. [T] IS NOW AUTHORIZED. GATE A IS BLOCKED until INVENTORY CHALLENGE IS resolved.
>
> **[D] Signed:** Finance expert — declarations ARE CLOSED.

---

### INVENTORY CHALLENGE

*(same structure as V-01)*

---

### GATE A

**GATE A IS NOT a checkpoint list; it IS the enforcement mechanism that makes [T]'s authorization conditional on named completion conditions. GATE A IS NOT clearable by assertion; it IS clearable only when every item below IS confirmed.**

*(same blocking items as V-01)*

**GATE A: [T] IS BLOCKED. INVARIANT-VIOLATION FORECAST IS BLOCKED until all items ARE confirmed.**

---

### INVARIANT-VIOLATION FORECAST [T]

*(same structure as V-01; Finance operations)*

---

### TRANSITION TABLE [T]

*(same structure as V-01)*

**EPOCH:** Finance lifecycle phase label (ORIGINATION / REVIEW / APPROVAL / SETTLEMENT); informational per C3.

---

### LIFECYCLE EPOCH MAP [T]

**V-02 VARIATION — EXPANDED EPOCH RATIONALE.** Each epoch entry carries an Arc Position field naming the epoch's structural role in the Finance lifecycle. This arc position IS the anchor for the EPOCH-CLUSTER ANALYSIS remediation implication: a finding in SETTLEMENT epoch IS NOT the same type of defect as a finding in ORIGINATION epoch; the arc position names the approval-gate class that IS the intervention point.

Map each declared operation to its lifecycle epoch and arc position:

| O-ID | Operation Name | Lifecycle Epoch | Epoch Rationale | Arc Position |
|------|----------------|-----------------|-----------------|--------------|
| O-[N] | [from OPERATION DECLARATIONS] | ORIGINATION / REVIEW / APPROVAL / SETTLEMENT | [why this operation belongs to this epoch] | [Entry boundary / Gate boundary / Approval event / Terminal settlement] |
*(one row per declared operation)*

**Epoch arc position legend:**
- **ORIGINATION** — IS the entry boundary epoch; defects here ARE data-quality defects (missing fields, invalid amounts, unauthorized submitters). The intervention IS NOT approval-gate hardening; it IS input validation at the Draft → Submitted transition.
- **REVIEW** — IS the classification epoch; defects here ARE routing defects (wrong reviewer assigned, review bypassed). The intervention IS assignment-rule enforcement.
- **APPROVAL** — IS the gate boundary epoch; defects here ARE authorization defects (approved without required dual sign-off, approval bypassed under threshold). The intervention IS approval-gate hardening.
- **SETTLEMENT** — IS the terminal epoch; defects here ARE finalization defects (paid invoices re-entering dispute workflow, void invoices appearing active). The intervention IS terminal-state transition locking.

---

### FORECAST VALIDATION [T]

*(same structure as V-01)*

---

### GATE B, GATE C, GATE D

*(same structure as V-01)*

---

### INVALID TRANSITIONS [T]

*(same structure as V-01)*

---

### RACE CONDITIONS [T]

*(same structure as V-01)*

---

### FINDINGS [T]

**FINDINGS IS NOT an observation log; it IS the derivation layer.** A finding IS NOT valid if it cannot be traced to a named record in TRANSITION TABLE, INVALID TRANSITIONS, FORECAST VALIDATION, or RACE CONDITIONS. FINDINGS IS NOT complete until every REFUTED forecast row IS named as a finding.

- **P[N]: [title]**
  Source: [named record].
  Inertia connection: [traces to INERTIA BASELINE failure mode].
  Disposition: [Status IS ACCEPTED / Action IS REQUIRED before feature ships].
  Severity: FATAL / DEGRADED / COSMETIC.

---

### EPOCH-CLUSTER ANALYSIS [T]

**EPOCH-CLUSTER ANALYSIS IS NOT a summary of FINDINGS; it IS the analytical transformation that converts the LIFECYCLE EPOCH MAP into a defect-density surface with arc-position-grounded remediation. EPOCH-CLUSTER ANALYSIS IS BLOCKED until FINDINGS IS complete AND the LIFECYCLE EPOCH MAP (with Arc Position column) IS present.**

**V-02 VARIATION.** The remediation implication IS grounded in the Arc Position column of the LIFECYCLE EPOCH MAP. A generic epoch name IS NOT sufficient as a remediation anchor; the Arc Position names which class of defect the epoch produces (data-quality vs routing vs authorization vs terminal-lock), and the remediation implication IS the specific intervention for that defect class. This specificity IS the difference between C-49 PASS and C-49 PARTIAL.

**Finding-to-epoch mapping:**

| Finding ID | Title | Triggering O-ID | Lifecycle Epoch | Arc Position | Defect Class |
|------------|-------|-----------------|-----------------|--------------|--------------|
| F-[N] | [from FINDINGS] | O-[N] | [from LIFECYCLE EPOCH MAP] | [from Arc Position column] | [data-quality / routing / authorization / terminal-lock] |

**Epoch defect counts:**

| Lifecycle Epoch | Arc Position | Defect Count | Finding IDs |
|-----------------|--------------|-------------|-------------|
| ORIGINATION | Entry boundary | [N] | [F-NN] |
| REVIEW | Classification | [N] | [F-NN] |
| APPROVAL | Gate boundary | [N] | [F-NN] |
| SETTLEMENT | Terminal | [N] | [F-NN] |

**Highest-density epoch:** [Epoch name] — [N] of [total] defects. Arc position: [entry boundary / gate boundary / terminal].

**Defect class:** [As named by Arc Position column — authorization defects / data-quality defects / terminal-lock defects].

**Remediation implication:** [Specific intervention for the defect class at this arc position. Must name the operation boundary or approval gate. E.g., "APPROVAL epoch carries [N] of [total] defects; arc position IS gate boundary; defect class IS authorization; hardening the dual-sign-off check at O-[N] (Under-Review → Approved) IS the highest-leverage intervention — this IS the operation that IS currently executing without the precondition check that [N] findings require."]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: INERTIA BASELINE, CONSTRAINT MATRIX, ROLES, STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION, INVENTORY CHALLENGE, GATE A, INVARIANT-VIOLATION FORECAST, TRANSITION TABLE, LIFECYCLE EPOCH MAP (with Arc Position column), FORECAST VALIDATION, GATE B, INVALID TRANSITIONS, GATE C, RACE CONDITIONS, GATE D, FINDINGS, EPOCH-CLUSTER ANALYSIS.

---

## V-03 — Output Format: Step-Block Epoch-Cluster (Customer Service)

**Variation axis:** Output format — step-block format (C-38/C-39 active); C-49 satisfied in step-block labeled analysis block format
**Hypothesis:** Customer Service domain (Support Ticket: New / Assigned / In-Progress / Pending-Customer / Resolved / Closed). Step-block output format: operations traced as labeled step blocks (not table rows), with each step-block label carrying `[C-XX: directive — FAILS if: pattern]` fusion (C-38 + C-39 simultaneously). C-48 standard. C-49: EPOCH-CLUSTER ANALYSIS appears as a labeled step-block analysis block rather than a tabular summary — tests whether C-49 is format-neutral as the rubric states. Single domain; C-50 not applicable. Predicted: 41/41.
**Domain:** Customer Service (Support Ticket: New / Assigned / In-Progress / Pending-Customer / Resolved / Closed)

---

### INERTIA BASELINE

The alternative to this trace IS: implement {{topic}} state management without hand-compiling transitions and invariants. The failure mode that alternative creates IS: invalid state transitions reach production because precondition checks were assumed rather than enumerated. This trace exists to close that gap before code is written. Every section that is skipped or left as a placeholder IS a return to the inertia baseline.

**PRODUCTION COST DECLARATION.** The production cost of the inertia baseline IS: support ticket records enter invalid state sequences — closed tickets reopen without escalation records, resolved tickets remain active in agent queues, and pending-customer tickets age unnoticed as in-progress work. The cost IS NOT a misrouted ticket; the cost IS a ticket in a state the system should have blocked, discovered by a customer complaint rather than by the application. This IS the specific failure this trace exists to prevent. Any section of this document left blank or abbreviated IS already that failure, deferred.

**IS-NEGATION PAIR.** The inertia baseline IS NOT a workflow gap; it IS a customer service integrity failure mode in the absence of this artifact. Choosing not to produce this trace IS NOT a risk accepted; it IS the failure mode instantiated before the feature ships. The existence of this document IS NOT documentation; it IS the artifact that converts that certainty into a prevented outcome.

---

You are running a **trace-state** signal for: {{topic}}

Produce a state machine trace in **step-block format**. Each operation IS traced as a labeled step block, not a table row. Step-block labels carry criterion-instruction fusion and disqualification-condition fusion simultaneously. This trace IS a formal artifact; its governing document IS the CONSTRAINT MATRIX below. A Domain Expert [D] declares the vocabulary phase; a Trace Developer [T] executes the trace phase. [T]'s authorization IS CONTINGENT on [D] completing a HANDOFF DECLARATION. Read the CONSTRAINT MATRIX completely before producing any output.

---

### CONSTRAINT MATRIX

**MATRIX AUTHORITY.** The CONSTRAINT MATRIX IS the governing authority for this trace and IS NOT AMENDABLE by [D] or [T]. A constraint not named in this matrix IS NOT binding on this trace. A violation not classifiable by a named constraint IS NOT a violation under this matrix. The scope of this matrix IS total: every compliance obligation IS traceable to a named constraint row.

| ID | Architectural Fact | Assigned Role | Concern |
|----|--------------------|---------------|---------|
| C1 | A state name not declared in STATE DECLARATIONS IS PROHIBITED in any step block | [T] | vocabulary |
| C2 | An operation name not declared in OPERATION DECLARATIONS IS PROHIBITED in any step block | [T] | vocabulary |
| C3 | Each step block carries an EPOCH field. The EPOCH field IS informational; it IS NOT constrained by C1 or C2. EPOCH values ARE drawn from CS lifecycle phase vocabulary (INTAKE / ACTIVE / PENDING / RESOLUTION) and ARE NOT required to match declared S-IDs. EPOCH data IS used to generate the LIFECYCLE EPOCH MAP secondary artifact. Table rows ARE NOT VALID as primary trace output; every operation IS REQUIRED as a step block with Before / Operation / After / EPOCH / INV sub-fields. | [T] | format / scope |
| C4 | Any state or operation added after VOCABULARY CLOSED IS declared IS a retroactive violation; such additions ARE PROHIBITED | [D] | ordering |
| C5 | A blank invariant status sub-field in any step block IS NOT PERMITTED; every INV sub-field IS REQUIRED to contain HOLDS or VIOLATED | [T] | integrity |
| C6 | TRACE BLOCKS ARE BLOCKED until GATE A IS confirmed AND INVARIANT-VIOLATION FORECAST IS complete | [T] | ordering |
| C7 | A blank or non-option response at INVENTORY CHALLENGE IS a C7 violation; GATE A IS BLOCKED in the presence of a C7 violation | [T] | completeness |
| C8 | INVALID TRANSITIONS IS BLOCKED until GATE B IS confirmed | [T] | ordering |
| C9 | RACE CONDITIONS IS BLOCKED until GATE C IS confirmed | [T] | ordering |
| C10 | STATE DIAGRAM [D] IS NOT a substitute for the TRACE BLOCKS; it IS the structural cross-check artifact. [D] IS REQUIRED to declare node count, edge count, and [!] annotation count. | [D] | integrity |

---

### ROLES

**ROLES IS NOT an organizational chart; ROLES IS the execution authority matrix for this trace. A section without a named role assignment IS NOT shared ownership; it IS unowned obligation and IS the inertia baseline instantiated before any section IS produced.**

**[D] Domain Expert**
Auto-selected: Customer Service expert (New / Assigned / In-Progress / Pending-Customer / Resolved / Closed).
Sections owned by [D]: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION.
Binding constraint: **C4**. The specific regression form [D] prevents IS: unvalidated ticket state vocabulary reaching the trace phase.

**[T] Trace Developer**
Sections owned by [T]: INVENTORY CHALLENGE response, INVARIANT-VIOLATION FORECAST, TRACE BLOCKS, LIFECYCLE EPOCH MAP, FORECAST VALIDATION, INVALID TRANSITIONS, RACE CONDITIONS, FINDINGS, EPOCH-CLUSTER ANALYSIS.
Binding constraints: **C1, C2, C3, C5, C6, C7, C8, C9, C10**.
Authorization status: [T]'s authorization IS CONTINGENT on HANDOFF DECLARATION. Prior to HANDOFF DECLARATION, [T] IS NOT AUTHORIZED to produce output in any [T]-owned section. The specific regression form [T] prevents IS: untraced ticket transitions shipping as assumed-valid precondition logic.

---

### STATE DECLARATIONS [D]

*(same format as V-01; CS vocabulary: New, Assigned, In-Progress, Pending-Customer, Resolved, Closed)*

**S-01.** [State Name] — [inline definitional clause]. Terminal: Yes/No.
*(at least one Terminal: Yes entry IS REQUIRED)*

---

### OPERATION DECLARATIONS [D]

*(same format as V-01; CS domain: assign, start work, block on customer, resume, resolve, close operations)*

**O-01.** [Operation Name] — [inline definitional clause]. From: S-[N][, S-[N]...]. To: S-[N]. Actor: [role/system].

---

### INVARIANT DECLARATIONS [D], VOCABULARY CLOSED [D], STATE DIAGRAM [D], HANDOFF DECLARATION [D]

*(same structure as V-01; CS domain; VOCABULARY CLOSED preamble IS NOT a label; HANDOFF DECLARATION TRANSFER DECLARATION IS NOT a coordination event)*

---

### INVENTORY CHALLENGE, GATE A

*(same structure as V-01)*

---

### INVARIANT-VIOLATION FORECAST [T]

*(same structure as V-01)*

---

### TRACE BLOCKS [T]

**V-03 FORMAT.** Each operation IS traced as a labeled step block. Step-block label format: `**[C-XX: directive — FAILS if: disqualification pattern] Step N: O-[ID] — Operation Name**`. The label simultaneously carries criterion-instruction fusion (C-38) and disqualification-condition fusion (C-39).

**Block structure for each operation:**

```
**[C-38: trace Before/Op/After state triple — FAILS if: any field IS left blank or S-ID IS NOT from STATE DECLARATIONS] Step N: O-[NN] — [Operation Name]**

- **Before:** S-[NN] ([State Name]) | Epoch: [CS lifecycle epoch] | INV-01: HOLDS/VIOLATED | INV-02: HOLDS/VIOLATED
- **Operation:** O-[NN] triggered by [actor/condition]; preconditions: [minimum two testable assertions]; all preconditions hold: [Yes/No]
- **After:** S-[NN] ([State Name]); postconditions: [minimum one assertion distinct from To State name]; side effects: [triggered rules, notifications, async jobs]
- **EPOCH (informational, C3):** [INTAKE / ACTIVE / PENDING / RESOLUTION]
- **INV-01 status:** HOLDS / VIOLATED — [reason if VIOLATED]
- **INV-02 status:** HOLDS / VIOLATED — [reason if VIOLATED]
```

*(one block per declared operation; blank sub-fields ARE NOT PERMITTED per C5)*

---

### LIFECYCLE EPOCH MAP [T]

| O-ID | Operation Name | Lifecycle Epoch | Epoch Rationale |
|------|----------------|-----------------|-----------------|
| O-[N] | [from OPERATION DECLARATIONS] | INTAKE / ACTIVE / PENDING / RESOLUTION | [why this operation belongs to this epoch] |

---

### FORECAST VALIDATION [T], GATE B, INVALID TRANSITIONS [T], GATE C, RACE CONDITIONS [T], GATE D

*(same structure as V-01; adapted for step-block format terminology)*

---

### FINDINGS [T]

*(same structure as V-01)*

---

### EPOCH-CLUSTER ANALYSIS [T]

**EPOCH-CLUSTER ANALYSIS IS NOT a summary of FINDINGS; it IS the analytical transformation that converts the LIFECYCLE EPOCH MAP from a labeling artifact into a defect-density surface. EPOCH-CLUSTER ANALYSIS IS BLOCKED until FINDINGS IS complete AND the LIFECYCLE EPOCH MAP IS present with all O-IDs mapped.**

**V-03 FORMAT.** EPOCH-CLUSTER ANALYSIS IS produced as a labeled step-block analysis section (not a table), demonstrating that C-49 IS format-neutral. The analysis block structure IS:

**Step ECL-1: Finding-to-Epoch Mapping**
For each finding F-[N] in FINDINGS: identify the triggering O-ID from the finding's Source field; look up the O-ID's epoch in the LIFECYCLE EPOCH MAP; record:
- F-[N] ("[title]") — triggered by O-[NN] — Epoch: [INTAKE / ACTIVE / PENDING / RESOLUTION]
*(one line per finding)*

**Step ECL-2: Epoch Defect Count**
Count findings per epoch:
- INTAKE: [N] defects — [F-NN, ...]
- ACTIVE: [N] defects — [F-NN, ...]
- PENDING: [N] defects — [F-NN, ...]
- RESOLUTION: [N] defects — [F-NN, ...]

**Step ECL-3: Highest-Density Epoch**
Highest-density epoch IS: [Epoch name] ([N] of [total] defects; finding IDs: [F-NN, ...]).
This epoch IS NOT randomly dense; it IS the epoch where [specific structural reason — e.g., "the Resolved → Closed transition IS currently unguarded, and the pending-customer timeout IS NOT enforced before resolution IS authorized"].

**Step ECL-4: Remediation Implication**
The remediation IS NOT broad process improvement; it IS a specific gate-hardening action. The highest-leverage intervention IS: [name the specific operation boundary or precondition check. E.g., "RESOLUTION epoch carries [N] of [total] defects — the precondition check on O-[N] (Pending-Customer → Resolved) IS the intervention point; the invariant that IS currently VIOLATED IS the one requiring customer acknowledgment before resolution IS authorized; adding this precondition check IS the single action that addresses [N] of [N] RESOLUTION epoch findings."]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: INERTIA BASELINE, CONSTRAINT MATRIX, ROLES, STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION, INVENTORY CHALLENGE, GATE A, INVARIANT-VIOLATION FORECAST, TRACE BLOCKS, LIFECYCLE EPOCH MAP, FORECAST VALIDATION, GATE B, INVALID TRANSITIONS, GATE C, RACE CONDITIONS, GATE D, FINDINGS, EPOCH-CLUSTER ANALYSIS.

---

## V-04 — Role Sequence x Phrasing: Finance-First Multi-Pass + C-50 (Finance → Sales)

**Variation axis:** Role sequence (Finance-first) × phrasing register (IS-negation saturation); C-50 artifact-level domain dependency declaration
**Hypothesis:** Finance → Sales two-domain multi-pass. Finance IS the source-of-record; Sales commitment state IS derived from Finance approval state. C-50: a top-scope DOMAIN DEPENDENCY DECLARATION before Pass 1 names Finance as source-of-record and the full dependency chain to Sales using IS-negation register (which simultaneously contributes to C-48 saturation). C-49: EPOCH-CLUSTER ANALYSIS spans both domain passes and maps findings to epochs across the full cross-domain lifecycle arc. Multi-pass criteria active: C-36, C-37, C-40, C-41, C-42, C-47. Predicted: 41/41.
**Domain:** Finance → Sales (Invoice approval driving Sales commitment; Finance: Draft → Approved; Sales: Proposal → Committed)

---

### INERTIA BASELINE

The alternative to this trace IS: implement {{topic}} cross-domain state management without hand-compiling Finance and Sales transitions as dependent passes. The failure mode that alternative creates IS: Sales commitment records are created without Finance approval records because the cross-domain dependency was assumed rather than traced. This trace exists to close that gap before code is written. Every section that is skipped or left as a placeholder IS a return to the inertia baseline.

**PRODUCTION COST DECLARATION.** The production cost of the inertia baseline IS: sales opportunities commit revenue that Finance has not approved — committed pipeline totals include deals whose underlying invoices are under review, disputed, or void. The cost IS NOT a data inconsistency; the cost IS committed revenue without an approval record, discovered by a revenue reconciliation audit rather than by the application. This IS the specific failure this trace exists to prevent.

**IS-NEGATION PAIR.** The inertia baseline IS NOT a process gap; it IS a cross-domain integrity failure mode instantiated before this trace IS produced. Choosing not to produce this trace IS NOT a risk accepted; it IS the failure mode deployed before the feature ships.

---

### DOMAIN DEPENDENCY DECLARATION

**[C-50] This declaration IS NOT a pass heading; it IS the artifact-level topology statement that governs the domain ordering of all passes in this trace. A pass ordering without this declaration IS NOT arbitrary; it IS undeclared. The dependency chain IS:**

**Finance IS the source-of-record domain for this trace.** Finance holds the approval record that determines whether a sales commitment IS authorized. Finance IS NOT a sequential pre-step; Finance IS the state authority from which Sales state IS derived.

**Sales commitment state IS derived from Finance approval state.** A Sales record IS NOT in a valid Committed state unless the corresponding Finance record IS in Approved state. Sales IS NOT independent; Sales IS a downstream domain whose valid states ARE constrained by Finance state resolution.

**The domain ordering in this trace IS Finance-first, Sales-second.** Finance IS NOT ordered first because it IS more important; Finance IS ordered first because Sales precondition checks depend on Finance state resolution. Reversing this order IS NOT merely stylistic; it IS structurally incorrect: a Sales pass executed before Finance state IS resolved IS a pass whose precondition checks ARE untestable.

**This declaration IS NOT WAIVABLE and IS NOT AMENDABLE by [D] or [T].**

---

You are running a **trace-state** signal for: {{topic}} — multi-domain multi-pass (Finance → Sales).

Produce a two-pass state machine trace. Pass 1 traces the Finance domain (Invoice: Draft / Submitted / Under-Review / Approved). Pass 2 traces the Sales domain (Opportunity: Proposal / Negotiation / Committed / Closed-Won), with cross-domain bridge annotations naming Finance postconditions as Sales preconditions. This trace IS a formal artifact; its governing document IS the CONSTRAINT MATRIX below. The DOMAIN DEPENDENCY DECLARATION above IS AUTHORITATIVE for domain ordering. Read both completely before producing any output.

---

### CONSTRAINT MATRIX

**MATRIX AUTHORITY.** The CONSTRAINT MATRIX IS the governing authority for this trace and IS NOT AMENDABLE by [D] or [T]. A constraint not named in this matrix IS NOT binding on this trace. No role IS authorized to add, waive, or modify a constraint. The scope of this matrix IS total.

| ID | Architectural Fact | Assigned Role | Concern |
|----|--------------------|---------------|---------|
| C1 | A state name not declared in STATE DECLARATIONS IS PROHIBITED in any trace table in either domain pass | [T] | vocabulary |
| C2 | An operation name not declared in OPERATION DECLARATIONS IS PROHIBITED in any trace table in either domain pass | [T] | vocabulary |
| C3 | Each TRANSITION TABLE includes an EPOCH column. EPOCH values ARE drawn from the respective domain's lifecycle phase vocabulary. Finance EPOCH vocabulary: ORIGINATION / REVIEW / APPROVAL / SETTLEMENT. Sales EPOCH vocabulary: OPEN-TRACK / QUALIFY / ADVANCE / CLOSE-TRACK. EPOCH IS informational; IS NOT constrained by C1/C2. | [T] | format / scope |
| C4 | Any state or operation added after VOCABULARY CLOSED IS declared IS a retroactive violation; such additions ARE PROHIBITED | [D] | ordering |
| C5 | A blank invariant status cell in any TRANSITION TABLE IS NOT PERMITTED | [T] | integrity |
| C6 | Pass 1 TRANSITION TABLE IS BLOCKED until GATE A IS confirmed. Pass 2 TRANSITION TABLE IS BLOCKED until Pass 1 IS complete AND Pass 2 BRIDGE TABLE IS declared | [T] | ordering |
| C7 | A blank or non-option response at INVENTORY CHALLENGE IS a C7 violation | [T] | completeness |
| C8 | INVALID TRANSITIONS (both passes) IS BLOCKED until GATE B IS confirmed | [T] | ordering |
| C9 | RACE CONDITIONS IS BLOCKED until GATE C IS confirmed | [T] | ordering |
| C10 | STATE DIAGRAM [D] IS NOT a substitute for the TRANSITION TABLE; it IS the structural cross-check artifact. One STATE DIAGRAM IS REQUIRED per domain. | [D] | integrity |
| C11 | Pass 2 TRANSITION TABLE IS BLOCKED until the BRIDGE TABLE explicitly names at least one Finance postcondition as a Sales precondition | [T] | cross-domain ordering |

---

### ROLES

**ROLES IS NOT an organizational chart; ROLES IS the execution authority matrix for this trace. A section without a named role assignment IS NOT shared ownership; it IS unowned obligation and IS the inertia baseline instantiated before any section IS produced.**

**[D] Domain Expert**
Auto-selected: Finance expert (Pass 1) AND Sales expert (Pass 2) — the same [D] role IS responsible for both domain declarations. A domain whose declarations ARE incomplete IS NOT a deferred section; it IS the inertia baseline chosen before [T] begins.
Sections owned by [D]: both domain STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAMS, HANDOFF DECLARATION.
Binding constraint: **C4** (vocabulary IS FROZEN across both domains after VOCABULARY CLOSED IS declared).

**[T] Trace Developer**
Sections owned by [T]: INVENTORY CHALLENGE, both domain INVARIANT-VIOLATION FORECASTs, BRIDGE TABLE, both domain TRANSITION TABLEs, both domain LIFECYCLE EPOCH MAPs, both domain FORECAST VALIDATIONs, INVALID TRANSITIONS (both passes), RACE CONDITIONS, FINDINGS, EPOCH-CLUSTER ANALYSIS.
Authorization: [T] IS NOT AUTHORIZED to begin Pass 2 until Pass 1 IS complete AND BRIDGE TABLE IS declared (C11). [T]'s authorization IS CONTINGENT on HANDOFF DECLARATION.

---

### Pass 1: Finance Domain

#### STATE DECLARATIONS [D] — Finance

**S-F01.** [Finance State Name] — [inline definitional clause]. Terminal: Yes/No.
*(Finance typical set: Draft, Submitted, Under-Review, Approved — minimum one Terminal: Yes)*

#### OPERATION DECLARATIONS [D] — Finance

**O-F01.** [Finance Operation Name] — [inline definitional clause]. From: S-F[N]. To: S-F[N]. Actor: [role/system].

#### INVARIANT DECLARATIONS [D] — Finance

**INV-F01.** [Finance Invariant] — [boolean assertion]. Authority: [source].
**INV-F02.** [Finance Invariant] — [boolean assertion]. Authority: [source].

#### VOCABULARY CLOSED [D] — Finance

**VOCABULARY CLOSED IS NOT a label; it IS the irreversibility event for the Finance domain. [D]'s authority to introduce Finance state or operation names IS extinguished at this moment. Any Finance name not listed below IS PROHIBITED in Pass 1 and in the BRIDGE TABLE.**

> VOCABULARY CLOSED — Finance domain. States: [list S-F IDs and names]. Operations: [list O-F IDs and names]. IS FROZEN. IS NOT WAIVABLE.

#### STATE DIAGRAM [D] — Finance

*(annotated edge list; [!] on every edge predicted VIOLATED; structural counts declared)*

#### HANDOFF DECLARATION [D] — Finance

> **[D] PASS 1 HANDOFF DECLARATION.**
> **TRANSFER DECLARATION.** This HANDOFF IS NOT a coordination event; it IS the formal transfer of Finance-domain trace authorization to [T]. [D]'s Finance declaration authority IS extinguished at this moment; [T]'s Pass 1 trace authorization IS created at this moment.
> Finance artifacts transferred: STATE DECLARATIONS (S-F01 through S-F[N]), OPERATION DECLARATIONS (O-F01 through O-F[N]), INVARIANT DECLARATIONS, STATE DIAGRAM ([N] nodes, [N] edges, [N] [!] annotations), VOCABULARY CLOSED (IS FROZEN).
> [D] IS PROHIBITED from modifying Finance declarations. [T] IS NOW AUTHORIZED to begin Pass 1.

#### INVARIANT-VIOLATION FORECAST [T] — Finance

*(one row per Finance O-ID; blank cells ARE NOT PERMITTED)*

| O-ID | Operation Name | Predicted INV-F01 | Predicted INV-F02 | Rationale |
|------|----------------|------------------|------------------|-----------|

#### GATE A

**GATE A IS NOT a checkpoint list; it IS the enforcement mechanism that makes Pass 1 TRANSITION TABLE authorization conditional. GATE A IS NOT clearable by assertion; it IS clearable only when every item below IS confirmed.**

*(standard blocking items; Pass 1 specific; same format as V-01)*

**GATE A: [T] IS BLOCKED. Pass 1 TRANSITION TABLE IS BLOCKED until all items ARE confirmed.**

#### TRANSITION TABLE [T] — Finance (Pass 1)

**### Pass 1 — Finance [C-36: Finance-first ordering targets cross-domain precondition defects — FAILS if: Pass 2 begins before Finance state resolution IS recorded] [C-37: Finance approval IS the precondition the entire artifact depends on; failure to complete Pass 1 IS NOT a gap; it IS an unauthorized Sales commitment]**

*(standard table structure; Finance S-IDs and O-IDs only; EPOCH column: ORIGINATION / REVIEW / APPROVAL / SETTLEMENT)*

#### LIFECYCLE EPOCH MAP [T] — Finance

*(standard structure; Finance lifecycle epochs)*

#### FORECAST VALIDATION [T] — Finance

*(compare Finance forecast against Pass 1 TRANSITION TABLE results)*

#### BRIDGE TABLE [T]

**BRIDGE TABLE IS NOT an optional annotation; it IS the cross-domain precondition chain that makes Pass 2 authorization conditional. Pass 2 TRANSITION TABLE IS BLOCKED until at least one Finance postcondition IS explicitly named as a Sales precondition in this table (C11).**

| Finance Postcondition (Pass 1 Row #) | Finance State After (S-F ID) | Bridge: Seeds Sales Precondition | Sales State Blocked Until (S-S ID) |
|--------------------------------------|------------------------------|----------------------------------|-------------------------------------|
| [Pass 1 row number] | S-F[N] ([Finance State]) | [Finance field value or record state] IS the precondition that Sales O-[N] IS BLOCKED on | S-S[N] (Sales: IS NOT reachable until this bridge condition IS met) |
*(minimum one bridge row IS REQUIRED; C11 violation IS present until this table IS non-empty)*

---

### Pass 2: Sales Domain

**### Pass 2 — Sales [C-36: Sales-second ordering targets Sales precondition defects that ARE derived from Finance approval — FAILS if: any Sales precondition is asserted without reference to Finance state] [C-37: A Sales commitment created before Finance approval IS recorded IS the exact revenue-leak failure mode this trace exists to prevent; proceeding without Bridge Table IS NOT a shortcut; it IS the failure mode instantiated]**

**[C-42: Pass 2 runs after Pass 1 because Sales commitment state IS derived from Finance approval state (DOMAIN DEPENDENCY DECLARATION); the defect class targeted by this ordering IS: Sales-commits-without-Finance-approval; the bridge row in BRIDGE TABLE IS the detection mechanism for this class]**

#### STATE DECLARATIONS [D] — Sales

**S-S01.** [Sales State Name] — [inline definitional clause]. Terminal: Yes/No.
*(Sales typical set: Proposal, Negotiation, Committed, Closed-Won, Closed-Lost — minimum one Terminal: Yes)*

#### OPERATION DECLARATIONS [D] — Sales

**O-S01.** [Sales Operation Name] — [inline definitional clause]. From: S-S[N]. To: S-S[N]. Actor: [role/system].

#### INVARIANT DECLARATIONS [D] — Sales, VOCABULARY CLOSED [D] — Sales, STATE DIAGRAM [D] — Sales, HANDOFF DECLARATION [D] — Sales

*(same structure as Finance counterparts; VOCABULARY CLOSED preamble IS NOT a label; HANDOFF DECLARATION TRANSFER DECLARATION IS NOT a coordination event; scoped to Sales domain)*

#### INVARIANT-VIOLATION FORECAST [T] — Sales

*(one row per Sales O-ID)*

#### GATE A — Sales Pass

**GATE A (Sales Pass) IS NOT clearable until BRIDGE TABLE IS present with at least one bridge row (C11). A Sales pass begun without a BRIDGE TABLE IS NOT a shortcut; it IS a C11 violation.**

*(standard blocking items + C11 bridge requirement)*

#### TRANSITION TABLE [T] — Sales (Pass 2)

*(standard table structure; Sales S-IDs and O-IDs only; EPOCH: OPEN-TRACK / QUALIFY / ADVANCE / CLOSE-TRACK)*

**Cross-domain precondition annotation (C-41):** For any Sales row where the precondition references a Finance state, annotate: "Precondition derived from Bridge Table row [N]: Finance [state/field] IS REQUIRED before this Sales operation IS authorized."

#### LIFECYCLE EPOCH MAP [T] — Sales, FORECAST VALIDATION [T] — Sales

*(standard structure; Sales epochs)*

---

### GATE B, INVALID TRANSITIONS (both passes), GATE C, RACE CONDITIONS

*(standard structure; covers both Finance and Sales domains)*

---

### GATE D

**GATE D IS NOT a checkpoint list; it IS the enforcement mechanism that makes FINDINGS and EPOCH-CLUSTER ANALYSIS authorization conditional. A GATE D not fully confirmed IS NOT a cleared gate.**

*(standard blocking items + requirement that LIFECYCLE EPOCH MAP IS complete for BOTH domains)*

---

### FINDINGS [T]

*(standard structure; findings may reference either domain pass; cross-domain bridge defects ARE priority findings)*

**Cross-domain finding template:**
- **P[N]: [title]**
  Source: [Pass 1 row N / Pass 2 row N / BRIDGE TABLE row N].
  Cross-domain dependency: [which bridge row surfaces the dependency that this finding violates; a cross-domain finding without a bridge row reference IS NOT traceable].
  Inertia connection: [traces to INERTIA BASELINE failure mode].
  Disposition: [Status IS ACCEPTED / Action IS REQUIRED].
  Severity: FATAL / DEGRADED / COSMETIC.

**Per-pass defect (C-40):** At least one labeled defect IS REQUIRED per domain pass. A pass with no finding IS NOT an acceptable result; it IS an incomplete trace.

**Defect-hypothesis confirmation (C-47):** For multi-pass findings, confirm or refute the C-42 defect-class prediction: "This finding [CONFIRMS / REFUTES] the [defect class from C-42 pass heading annotation]; triggered by bridge row [row reference from BRIDGE TABLE / C-41 cross-domain annotation]."

---

### EPOCH-CLUSTER ANALYSIS [T]

**EPOCH-CLUSTER ANALYSIS IS NOT a summary of FINDINGS; it IS the analytical transformation that converts both domain LIFECYCLE EPOCH MAPs into a cross-domain defect-density surface. EPOCH-CLUSTER ANALYSIS IS BLOCKED until FINDINGS IS complete AND both LIFECYCLE EPOCH MAPs ARE present.**

**V-04 VARIATION.** This analysis spans two domain passes. Findings are mapped to epochs within their respective domain. The cross-domain epoch concentration (whether Finance or Sales epochs carry more defects) IS the primary output: it names which domain IS the higher-leverage intervention point.

**Finding-to-epoch mapping (both domains):**

| Finding ID | Domain | Triggering O-ID | Lifecycle Epoch | Defect Type |
|------------|--------|-----------------|-----------------|-------------|
| F-[N] | Finance / Sales | O-[FN] / O-[SN] | [epoch from respective LIFECYCLE EPOCH MAP] | [type] |

**Epoch defect counts by domain:**

**Finance epochs:**
| Epoch | Defect Count | Finding IDs |
|-------|-------------|-------------|
| ORIGINATION | [N] | [...] |
| REVIEW | [N] | [...] |
| APPROVAL | [N] | [...] |
| SETTLEMENT | [N] | [...] |

**Sales epochs:**
| Epoch | Defect Count | Finding IDs |
|-------|-------------|-------------|
| OPEN-TRACK | [N] | [...] |
| QUALIFY | [N] | [...] |
| ADVANCE | [N] | [...] |
| CLOSE-TRACK | [N] | [...] |

**Highest-density epoch (cross-domain):** [Epoch name] in [Finance/Sales] domain — [N] of [total] defects (finding IDs: [F-NN, ...]).

**Cross-domain concentration finding:** [Finance domain / Sales domain] IS the higher-defect-density domain ([N] vs [N] defects). This IS NOT a coincidence; it IS [structural reason — e.g., "because the APPROVAL epoch IS the gate between the two domains, and every Sales defect in CLOSE-TRACK IS downstream of an APPROVAL epoch precondition that IS not enforced"].

**Remediation implication:** [Specific intervention. Must name domain, epoch, operation, and precondition check. E.g., "Finance APPROVAL epoch IS the highest-density epoch ([N] defects); the intervention IS the dual-sign-off precondition at O-F[N] (Under-Review → Approved); this IS the single check that, if enforced, removes the precondition dependency from [N] downstream Sales CLOSE-TRACK findings."]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: INERTIA BASELINE, DOMAIN DEPENDENCY DECLARATION, CONSTRAINT MATRIX, ROLES, Pass 1 (Finance: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION, INVARIANT-VIOLATION FORECAST, GATE A, TRANSITION TABLE, LIFECYCLE EPOCH MAP, FORECAST VALIDATION), BRIDGE TABLE, Pass 2 (Sales: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION, INVARIANT-VIOLATION FORECAST, GATE A, TRANSITION TABLE, LIFECYCLE EPOCH MAP, FORECAST VALIDATION), GATE B, INVALID TRANSITIONS (both passes), GATE C, RACE CONDITIONS, GATE D, FINDINGS, EPOCH-CLUSTER ANALYSIS.

---

## V-05 — Full Synthesis: Three-Domain + All Probes (Finance → Sales → CS)

**Variation axis:** Full synthesis — C-48 IS-negation saturation + C-49 epoch-cluster analysis + C-50 three-domain dependency declaration
**Hypothesis:** Finance → Sales → CS three-domain multi-pass. Finance IS the source-of-record (invoice approval). Sales IS derived from Finance (commitment requires approval). CS IS derived from Sales (support entitlement requires commitment). C-50: DOMAIN DEPENDENCY DECLARATION names all three domains and the full two-hop dependency chain (Finance → Sales → CS) using IS-negation register (simultaneously contributes to C-48 saturation). C-49: EPOCH-CLUSTER ANALYSIS spans three domain passes, identifies cross-domain epoch concentration, and names the highest-leverage intervention point in the three-domain dependency chain. C-48 saturation: IS-negation register present in every constraint-carrying section across all three passes. All multi-pass criteria (C-36/C-37/C-40/C-41/C-42/C-47) active. Tests: (a) C-50 with a three-domain dependency chain (the PARTIAL case where only 1 of 2 downstream domains is named is specifically called out in the rubric), (b) C-49 with three-domain epoch surface, (c) whether C-48 saturation is maintainable across a three-domain artifact. Domain portability confirmed: Sales/Finance/CS lifecycle vocabularies all distinct, no vocabulary overlap. Predicted: 41/41.
**Domain:** Finance (Invoice) → Sales (Opportunity) → CS (Support Entitlement)

---

### INERTIA BASELINE

The alternative to this trace IS: implement {{topic}} cross-domain state management without hand-compiling Finance, Sales, and CS transitions as a three-pass dependency chain. The failure mode that alternative creates IS: CS support entitlements are created without committed sales records, and committed sales records are created without Finance approval records, because the two-hop dependency chain was assumed rather than traced. This trace exists to close that gap before code is written. Every section that is skipped or left as a placeholder IS a return to the inertia baseline.

**PRODUCTION COST DECLARATION.** The production cost of the inertia baseline IS: customers receive CS entitlements for deals that have not been committed, and commitments are recorded for invoices that have not been approved. The cost IS NOT a data inconsistency; the cost IS an entitlement without an approval chain, discovered by a contract audit rather than by the application. This IS the specific failure this trace exists to prevent.

**IS-NEGATION PAIR.** The inertia baseline IS NOT a three-party coordination failure; it IS a dependency-chain integrity failure mode instantiated before this trace IS produced. Choosing not to produce this trace IS NOT a risk accepted; it IS the failure mode deployed before the feature ships.

---

### DOMAIN DEPENDENCY DECLARATION

**[C-50] This declaration IS NOT a pass heading; it IS the artifact-level topology statement governing the domain ordering of all three passes in this trace. A three-domain trace without this declaration IS NOT missing a header; it IS missing the structural justification for every cross-domain gate in the artifact. This declaration IS NOT WAIVABLE and IS NOT AMENDABLE by [D] or [T].**

**Finance IS the source-of-record domain for this trace.** Finance holds the invoice approval record. Finance IS NOT a pre-step; Finance IS the state authority that all downstream domains depend on. A Sales record IS NOT valid until a Finance approval record IS present. A CS entitlement record IS NOT valid until a Sales commitment record IS present. Finance IS the origin of the dependency chain.

**Sales commitment state IS derived from Finance approval state.** Sales IS NOT independent; Sales IS the first downstream domain. A Sales opportunity IS NOT in Committed state unless the corresponding Finance invoice IS in Approved state. Sales IS NOT ordered second because it matters less; Sales IS ordered second because its valid states ARE constrained by Finance state resolution, and those preconditions ARE NOT testable until Finance state IS resolved.

**CS entitlement state IS derived from Sales commitment state.** CS IS the second downstream domain. A CS support entitlement IS NOT in Active state unless the corresponding Sales opportunity IS in Committed or Closed-Won state. CS IS ordered third because its valid states ARE constrained by Sales state resolution, which IS itself constrained by Finance state resolution. The full dependency chain IS: Finance approval → Sales commitment → CS entitlement. Reversing any hop in this chain IS NOT merely reordered; it IS structurally incorrect.

**This declaration IS NOT satisfied by per-pass headings alone.** Per-pass ordering annotations (C-42) name the defect-class hypothesis at each pass; this declaration names the artifact-wide dependency topology. Both ARE REQUIRED. Neither satisfies the other.

---

You are running a **trace-state** signal for: {{topic}} — multi-domain three-pass (Finance → Sales → CS).

Produce a three-pass state machine trace following the dependency chain declared above. Pass 1: Finance (Invoice). Pass 2: Sales (Opportunity). Pass 3: CS (Support Entitlement). Cross-domain bridge tables connect each pass. This trace IS a formal artifact; its governing document IS the CONSTRAINT MATRIX below. The DOMAIN DEPENDENCY DECLARATION IS AUTHORITATIVE for domain ordering. Read both completely before producing any output.

---

### CONSTRAINT MATRIX

**MATRIX AUTHORITY.** The CONSTRAINT MATRIX IS the governing authority for this trace and IS NOT AMENDABLE by [D] or [T]. A constraint not named in this matrix IS NOT binding on this trace. No role IS authorized to add, waive, or modify a constraint. The scope of this matrix IS total: every compliance obligation IS traceable to a named constraint row. A constraint unnamed here IS NOT a constraint on this trace.

| ID | Architectural Fact | Assigned Role | Concern |
|----|--------------------|---------------|---------|
| C1 | A state name not declared in the domain's STATE DECLARATIONS IS PROHIBITED in that domain's trace tables | [T] | vocabulary |
| C2 | An operation name not declared in the domain's OPERATION DECLARATIONS IS PROHIBITED in that domain's trace tables | [T] | vocabulary |
| C3 | Each TRANSITION TABLE includes an EPOCH column. EPOCH IS informational; IS NOT constrained by C1/C2. Finance EPOCH vocabulary: ORIGINATION / REVIEW / APPROVAL / SETTLEMENT. Sales EPOCH vocabulary: OPEN-TRACK / QUALIFY / ADVANCE / CLOSE-TRACK. CS EPOCH vocabulary: INTAKE / ACTIVE / PENDING / RESOLUTION. | [T] | format / scope |
| C4 | Any state or operation added after VOCABULARY CLOSED IS declared IS a retroactive violation; IS PROHIBITED | [D] | ordering |
| C5 | A blank invariant status cell IS NOT PERMITTED; every INV cell IS REQUIRED to contain HOLDS or VIOLATED | [T] | integrity |
| C6 | Pass 1 TRANSITION TABLE IS BLOCKED until GATE A-F IS confirmed. Pass 2 TRANSITION TABLE IS BLOCKED until Pass 1 IS complete AND BRIDGE TABLE F→S IS declared. Pass 3 TRANSITION TABLE IS BLOCKED until Pass 2 IS complete AND BRIDGE TABLE S→CS IS declared. | [T] | ordering |
| C7 | A blank or non-option response at any INVENTORY CHALLENGE IS a C7 violation | [T] | completeness |
| C8 | INVALID TRANSITIONS (all passes) IS BLOCKED until GATE B IS confirmed | [T] | ordering |
| C9 | RACE CONDITIONS IS BLOCKED until GATE C IS confirmed | [T] | ordering |
| C10 | One STATE DIAGRAM IS REQUIRED per domain; each IS the structural cross-check for its domain | [D] | integrity |
| C11 | Pass 2 TRANSITION TABLE IS BLOCKED until BRIDGE TABLE F→S names at least one Finance postcondition as Sales precondition | [T] | cross-domain ordering |
| C12 | Pass 3 TRANSITION TABLE IS BLOCKED until BRIDGE TABLE S→CS names at least one Sales postcondition as CS precondition | [T] | cross-domain ordering |

---

### ROLES

**ROLES IS NOT an organizational chart; ROLES IS the execution authority matrix for this trace. A section without a named role assignment IS NOT shared ownership; it IS unowned obligation and IS the inertia baseline instantiated before any section IS produced. A role obligation that IS unassigned IS NOT deferred; it IS absent.**

**[D] Domain Expert**
Auto-selected: Finance expert (Pass 1) + Sales expert (Pass 2) + Customer Service expert (Pass 3) — [D] IS responsible for all three domain declarations. An incomplete domain declaration IS NOT a deferred section; it IS the inertia baseline chosen before that domain's trace begins.
Sections owned by [D]: All three domains' STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAMS, HANDOFF DECLARATIONS.
Binding constraint: **C4** (vocabulary IS FROZEN across all three domains after VOCABULARY CLOSED IS declared for each).
INERTIA BASELINE: [D]'s incomplete declarations ARE the inertia baseline instantiated. The specific regression [D] prevents IS: unvalidated state vocabulary from any of the three domains propagating into the trace phase and producing undeclared cross-domain precondition assumptions.

**[T] Trace Developer**
Sections owned by [T]: All three INVENTORY CHALLENGEs, all three INVARIANT-VIOLATION FORECASTs, BRIDGE TABLE F→S, BRIDGE TABLE S→CS, all three TRANSITION TABLEs, all three LIFECYCLE EPOCH MAPs, all three FORECAST VALIDATIONs, INVALID TRANSITIONS (all passes), RACE CONDITIONS, FINDINGS, EPOCH-CLUSTER ANALYSIS.
Authorization: [T] IS NOT AUTHORIZED to begin Pass 2 until Pass 1 IS complete AND BRIDGE TABLE F→S IS declared (C11). [T] IS NOT AUTHORIZED to begin Pass 3 until Pass 2 IS complete AND BRIDGE TABLE S→CS IS declared (C12). [T]'s authorization per pass IS CONTINGENT on the respective HANDOFF DECLARATION.

---

### Pass 1: Finance Domain

**### Pass 1 — Finance [C-36: Finance-first ordering targets cross-domain commitment defects — FAILS if: Pass 2 begins without Finance approval state resolved] [C-37: unresolved Finance state IS the approval-chain failure that creates unauthorized Sales commitments AND unauthorized CS entitlements; Pass 1 IS NOT a preamble; it IS the dependency root] [C-42: Finance IS ordered first because Sales commitment preconditions ARE Finance-derived; the defect class targeted IS: downstream-commitment-without-upstream-approval]**

*(Finance domain sections: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION — same structure as V-04 Finance pass; domain: Draft / Submitted / Under-Review / Approved)*

*(VOCABULARY CLOSED preamble: Finance domain — **VOCABULARY CLOSED IS NOT a label; it IS the irreversibility event for the Finance domain.** [Same IS-negation structure as V-01 / V-04])*

*(HANDOFF DECLARATION: **TRANSFER DECLARATION. This HANDOFF IS NOT a coordination event; it IS the formal transfer of Finance-domain trace authorization to [T].** [Same IS-negation structure as V-04])*

*(INVARIANT-VIOLATION FORECAST [T], GATE A-F, TRANSITION TABLE [T] — Finance, LIFECYCLE EPOCH MAP [T] — Finance, FORECAST VALIDATION [T] — Finance: same structure as V-04)*

---

### BRIDGE TABLE F→S [T]

**BRIDGE TABLE F→S IS NOT an optional annotation; it IS the cross-domain precondition chain that makes Pass 2 Sales trace authorization conditional. Pass 2 IS BLOCKED until at least one Finance postcondition IS explicitly named as a Sales precondition (C11). This bridge IS NOT advisory; it IS the record that proves the dependency chain declared in DOMAIN DEPENDENCY DECLARATION IS traceable to specific state records.**

| Finance Postcondition (Pass 1 Row #) | Finance State After | Bridge: Seeds Sales Precondition | Sales State Blocked Until |
|--------------------------------------|---------------------|----------------------------------|---------------------------|
| [row #] | S-F[N] ([Finance State]) | Finance [field/state] IS REQUIRED before Sales O-[N] IS authorized | S-S[N] (IS NOT reachable until bridge condition IS met) |

---

### Pass 2: Sales Domain

**### Pass 2 — Sales [C-36: Sales-second ordering targets Finance-derived precondition defects — FAILS if: any Sales precondition IS asserted without a bridge row reference] [C-37: a Sales commitment without a Finance approval bridge row IS the revenue-commitment failure mode this artifact exists to prevent; proceeding without Bridge Table F→S IS NOT a shortcut; it IS the failure mode instantiated] [C-42: Sales IS ordered second because commitment preconditions ARE Finance-derived; the defect class targeted IS: Sales-commits-without-Finance-approval; the bridge row in BRIDGE TABLE F→S IS the detection surface]**

*(Sales domain sections: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION — same structure; domain: Proposal / Negotiation / Committed / Closed-Won / Closed-Lost)*

*(VOCABULARY CLOSED preamble: Sales domain — **VOCABULARY CLOSED IS NOT a label; it IS the irreversibility event for the Sales domain.**)*

*(INVARIANT-VIOLATION FORECAST [T] — Sales, GATE A-S, TRANSITION TABLE [T] — Sales: same structure; cross-domain precondition annotations per C-41 reference BRIDGE TABLE F→S rows)*

*(LIFECYCLE EPOCH MAP [T] — Sales, FORECAST VALIDATION [T] — Sales: same structure)*

---

### BRIDGE TABLE S→CS [T]

**BRIDGE TABLE S→CS IS NOT an optional annotation; it IS the cross-domain precondition chain that makes Pass 3 CS trace authorization conditional. Pass 3 IS BLOCKED until at least one Sales postcondition IS explicitly named as a CS precondition (C12). This bridge IS the second hop in the Finance → Sales → CS dependency chain declared in DOMAIN DEPENDENCY DECLARATION.**

| Sales Postcondition (Pass 2 Row #) | Sales State After | Bridge: Seeds CS Precondition | CS State Blocked Until |
|------------------------------------|-------------------|-------------------------------|------------------------|
| [row #] | S-S[N] ([Sales State]) | Sales [field/state] IS REQUIRED before CS O-[N] IS authorized | S-CS[N] (IS NOT reachable until bridge condition IS met) |

---

### Pass 3: CS Domain

**### Pass 3 — CS (Customer Service) [C-36: CS-third ordering targets Sales-derived entitlement defects — FAILS if: any CS entitlement IS asserted without a bridge row reference to Sales commitment state] [C-37: a CS entitlement without a Sales commitment bridge row IS the unauthorized-entitlement failure mode this artifact exists to prevent; proceeding without Bridge Table S→CS IS NOT a shortcut; it IS the failure mode instantiated] [C-42: CS IS ordered third because entitlement preconditions ARE Sales-derived, which ARE themselves Finance-derived; the defect class targeted IS: CS-entitlement-without-Sales-commitment; the bridge row in BRIDGE TABLE S→CS IS the detection surface]**

*(CS domain sections: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION — same structure; domain: New / Assigned / In-Progress / Pending-Customer / Resolved / Closed)*

*(VOCABULARY CLOSED preamble: CS domain — **VOCABULARY CLOSED IS NOT a label; it IS the irreversibility event for the CS domain.**)*

*(INVARIANT-VIOLATION FORECAST [T] — CS, GATE A-CS, TRANSITION TABLE [T] — CS: cross-domain precondition annotations per C-41 reference BRIDGE TABLE S→CS rows)*

*(LIFECYCLE EPOCH MAP [T] — CS, FORECAST VALIDATION [T] — CS: CS epochs: INTAKE / ACTIVE / PENDING / RESOLUTION)*

---

### GATE B, INVALID TRANSITIONS (all three passes), GATE C, RACE CONDITIONS

**GATE B IS NOT a checkpoint list; it IS the enforcement mechanism that makes INVALID TRANSITIONS authorization conditional. GATE B covers all three passes simultaneously. GATE B IS NOT clearable until all three TRANSITION TABLEs ARE complete AND all three LIFECYCLE EPOCH MAPs ARE present.**

*(standard blocking items; covers Finance, Sales, CS passes)*

*(INVALID TRANSITIONS: minimum three rows per domain, each with S-ID and O-ID from the respective domain's declarations)*

*(RACE CONDITIONS: cross-domain race scenarios where Finance approval and Sales commitment operations could interleave; if no concurrent access: explicit clearance with reason IS REQUIRED)*

---

### GATE D

**GATE D IS NOT a checkpoint list; it IS the enforcement mechanism that makes FINDINGS and EPOCH-CLUSTER ANALYSIS authorization conditional. GATE D IS NOT clearable until FINDINGS IS complete for all three domain passes. A GATE D not fully confirmed IS NOT a cleared gate; it IS an authorization block on both FINDINGS and EPOCH-CLUSTER ANALYSIS.**

*(standard blocking items + requirement that all three LIFECYCLE EPOCH MAPs ARE complete)*

---

### FINDINGS [T]

*(standard structure; findings reference domain pass; cross-domain findings reference bridge table row)*

**Per-pass defect (C-40):** At least one labeled defect IS REQUIRED per domain pass (Finance, Sales, CS). A pass with no finding IS NOT an acceptable result.

**Defect-hypothesis confirmation (C-47):** For each multi-pass finding: "This finding [CONFIRMS / REFUTES] the [defect class from C-42 heading annotation for that pass]; triggered by bridge row [row reference from BRIDGE TABLE F→S / BRIDGE TABLE S→CS / C-41 annotation]."

---

### EPOCH-CLUSTER ANALYSIS [T]

**EPOCH-CLUSTER ANALYSIS IS NOT a summary of FINDINGS; it IS the analytical transformation that converts all three domain LIFECYCLE EPOCH MAPs into a cross-domain defect-density surface. EPOCH-CLUSTER ANALYSIS IS BLOCKED until FINDINGS IS complete AND all three LIFECYCLE EPOCH MAPs ARE present. An epoch-cluster section produced without all three maps IS NOT complete; it IS a partial analysis and IS NOT a C-49 pass.**

**V-05 VARIATION.** This analysis spans three domain passes across three distinct lifecycle epoch vocabularies (Finance: ORIGINATION/REVIEW/APPROVAL/SETTLEMENT; Sales: OPEN-TRACK/QUALIFY/ADVANCE/CLOSE-TRACK; CS: INTAKE/ACTIVE/PENDING/RESOLUTION). The cross-domain concentration finding names which domain IS the highest-leverage intervention point in the Finance → Sales → CS dependency chain.

**Finding-to-epoch mapping (all three domains):**

| Finding ID | Domain | Triggering O-ID | Lifecycle Epoch | Defect Type |
|------------|--------|-----------------|-----------------|-------------|
| F-[N] | Finance / Sales / CS | O-[FN] / O-[SN] / O-[CSN] | [epoch from respective LIFECYCLE EPOCH MAP] | [type] |

**Epoch defect counts by domain:**

**Finance epochs:**
| Epoch | Defect Count | Finding IDs |
|-------|-------------|-------------|
| ORIGINATION | [N] | [...] |
| REVIEW | [N] | [...] |
| APPROVAL | [N] | [...] |
| SETTLEMENT | [N] | [...] |

**Sales epochs:**
| Epoch | Defect Count | Finding IDs |
|-------|-------------|-------------|
| OPEN-TRACK | [N] | [...] |
| QUALIFY | [N] | [...] |
| ADVANCE | [N] | [...] |
| CLOSE-TRACK | [N] | [...] |

**CS epochs:**
| Epoch | Defect Count | Finding IDs |
|-------|-------------|-------------|
| INTAKE | [N] | [...] |
| ACTIVE | [N] | [...] |
| PENDING | [N] | [...] |
| RESOLUTION | [N] | [...] |

**Highest-density epoch (cross-domain):** [Epoch name] in [Finance / Sales / CS] domain — [N] of [total] defects.

**Dependency-chain concentration finding:** The highest-density epoch IS in the [Finance / Sales / CS] domain. This IS NOT isolated; given the Finance → Sales → CS dependency chain, defect density in the [Finance / Sales] domain IS the causal upstream of downstream defects: [e.g., "Finance APPROVAL epoch IS the gate between Finance and Sales; [N] of the [total] downstream Sales CLOSE-TRACK defects ARE traceable to the Finance → Sales bridge; remediating the Finance APPROVAL gate simultaneously addresses upstream and downstream findings"]. A generic statement that names the epoch without tracing the cascade through the dependency chain IS NOT a valid C-49 remediation implication; it IS a PARTIAL at best.

**Remediation implication:** [Specific intervention. Must name: domain, epoch, operation, precondition check, and dependency-chain cascade effect. E.g., "Finance APPROVAL epoch IS the highest-density epoch and IS the dependency root; hardening the dual-sign-off precondition at O-F[N] (Under-Review → Approved) IS the highest-leverage intervention because it (a) addresses [N] Finance APPROVAL defects directly, (b) closes the bridge gap that generates [N] Sales CLOSE-TRACK defects via BRIDGE TABLE F→S row [N], and (c) removes the entitlement-without-approval precondition that generates [N] CS INTAKE defects via BRIDGE TABLE S→CS row [N]. This single intervention point IS the intervention that propagates remediation through the full three-domain dependency chain."]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: INERTIA BASELINE, DOMAIN DEPENDENCY DECLARATION, CONSTRAINT MATRIX, ROLES, Pass 1 (Finance: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION, INVARIANT-VIOLATION FORECAST, GATE A-F, TRANSITION TABLE, LIFECYCLE EPOCH MAP, FORECAST VALIDATION), BRIDGE TABLE F→S, Pass 2 (Sales: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION, INVARIANT-VIOLATION FORECAST, GATE A-S, TRANSITION TABLE, LIFECYCLE EPOCH MAP, FORECAST VALIDATION), BRIDGE TABLE S→CS, Pass 3 (CS: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION, INVARIANT-VIOLATION FORECAST, GATE A-CS, TRANSITION TABLE, LIFECYCLE EPOCH MAP, FORECAST VALIDATION), GATE B, INVALID TRANSITIONS (all passes), GATE C, RACE CONDITIONS, GATE D, FINDINGS, EPOCH-CLUSTER ANALYSIS.

---

*Round: R18 | Rubric: v16 (current) | New criteria targeted: C-48 (IS-negation register saturation), C-49 (epoch-cluster defect analysis), C-50 (artifact-level domain dependency declaration) | Pool: 41 | Unit: 1.22 pts*
