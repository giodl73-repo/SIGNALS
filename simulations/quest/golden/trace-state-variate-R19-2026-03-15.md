# trace-state — Round 19 Variations (R19)
# Skill: trace-state | Date: 2026-03-15 | Rubric: v17 (current)

Five complete, runnable skill body prompt variations for `trace-state`.
Each variation is a complete prompt body -- not a diff.

---

## R19 Gap Analysis

From R18 under rubric v17 (44 aspirational criteria, C-09..C-53, unit = 1.14):

| Variant | R18 PASS | R18 Score | R19 Gap |
|---------|----------|-----------|---------|
| V-01 (Sales, single-pass tabular) | 27 | 80.8 | C-51: no Arc Position column in LIFECYCLE EPOCH MAP |
| V-02 (Finance, single-pass + Arc Position) | 28 | 81.9 | C-51 satisfied; R19 probe: C-49/C-51 synergy confirmation language in remediation implication |
| V-03 (CS, step-block) | 27 | 80.8 | C-51: no structural role tags in ECL epoch entries |
| V-04 (Finance→Sales, two-pass) | 36 | 91.0 | C-51: Arc Position absent from both LIFECYCLE EPOCH MAPs; adding yields 37 PASS = 92.2 |
| V-05 (Finance→Sales→CS, three-pass) | 36 | 91.0 | C-51: Arc Position absent from all three LIFECYCLE EPOCH MAPs; adding yields 37 PASS = 92.2 |

**R19 axis:** Epoch arc-position structural role annotation (C-51) deployed in every variant:
- **Single-domain artifacts (V-01, V-03):** Add Arc Position column / structural role tags to LIFECYCLE EPOCH MAP; update EPOCH-CLUSTER ANALYSIS remediation implication to cite structural role vocabulary, not epoch name alone.
- **Multi-domain artifacts (V-04, V-05):** Add Arc Position to all domain LIFECYCLE EPOCH MAPs; update cross-domain EPOCH-CLUSTER ANALYSIS to use arc-position vocabulary in the inter-domain handoff remediation implication, activating the C-51/C-52 synergy.

**Predicted R19 scores under v17 (unit = 1.14):**

| Variant | New PASS | Total PASS | Score |
|---------|----------|------------|-------|
| V-01 (Sales, single-pass + Arc Position) | C-51 | 28 | **81.9** |
| V-02 (Finance, single-pass + Arc Position synergy) | — | 28 | **81.9** |
| V-03 (CS, step-block + Arc Position tags) | C-51 | 28 | **81.9** |
| V-04 (Finance→Sales, two-pass + Arc Position both) | C-51 | 37 | **92.2** |
| V-05 (Finance→Sales→CS, three-pass + Arc Position all) | C-51 | 37 | **92.2** |

---

## Variation Axis Map

| Variation | Axis | Domain | New Probe | Predicted |
|-----------|------|--------|-----------|-----------|
| V-01 | Lifecycle emphasis: Arc Position column in LIFECYCLE EPOCH MAP (tabular) | Sales | C-51 in single-domain tabular format; C-49 remediation cites structural role | 28/44 |
| V-02 | Lifecycle emphasis: C-49/C-51 synergy confirmation language | Finance | C-51 carried from R18; R19 probe: remediation implication language explicitly references arc position (not epoch name alone) to confirm synergy activation | 28/44 |
| V-03 | Output format: Arc Position structural role tags in step-block ECL entries | Customer Service | C-51 in step-block format; ECL epochs carry structural role tags; tests format-neutrality of C-51 | 28/44 |
| V-04 | Role sequence × Lifecycle emphasis: Arc Position in both LIFECYCLE EPOCH MAPs + cross-domain EPOCH-CLUSTER synergy | Finance → Sales | C-51 in both passes; C-52 remediation implication uses arc-position structural roles; C-51/C-52 synergy activated | 37/44 |
| V-05 | Full synthesis: Arc Position in all three LIFECYCLE EPOCH MAPs + three-domain arc-position EPOCH-CLUSTER synthesis | Finance → Sales → CS | C-51 across all three passes; EPOCH-CLUSTER ANALYSIS names handoff boundary using arc-position structural vocabulary; maximum C-51/C-52 synergy | 37/44 |

**V-01 hypothesis:** Sales domain (Lead / Qualified / Proposal / Negotiation / Closed-Won / Closed-Lost). Single-pass tabular. C-48 saturation standard from R18. C-49 standard from R18. **C-51 addition:** LIFECYCLE EPOCH MAP gains a mandatory Arc Position column (Entry boundary / Gate boundary / Approval event / Terminal settlement). Arc Position legend declared before trace. EPOCH-CLUSTER ANALYSIS remediation implication references structural role (e.g., "highest-density epoch IS the Gate boundary epoch — approval-gate hardening at this structural chokepoint IS the intervention, not the epoch-name of QUALIFY"). Tests whether Arc Position column earns C-51 PASS in Sales domain tabular format. Predicted: 28 PASS = 81.9.

**V-02 hypothesis:** Finance domain (Invoice: Draft / Submitted / Under-Review / Approved / Paid / Disputed / Void). R18 V-02 already has Arc Position column — C-51 PASS confirmed. **R19 probe:** The C-51/C-49 synergy rule states that when both are satisfied, C-49 remediation implications should reference structural role vocabulary rather than epoch names alone. R19 V-02 sharpens the EPOCH-CLUSTER ANALYSIS remediation implication: "IS NOT an APPROVAL epoch finding; IS a Gate boundary structural-role finding — intervention IS approval-gate hardening at this structural position regardless of what the epoch is named across domain vocabularies." Tests whether explicit synergy language in the remediation section raises C-49 quality score beyond generic PASS. Predicted: 28 PASS = 81.9.

**V-03 hypothesis:** Customer Service domain (Support Ticket: New / Assigned / In-Progress / Pending-Customer / Resolved / Closed). Step-block format from R18. C-48 saturation standard. C-49 delivered as ECL step blocks. **C-51 addition:** ECL epoch entries carry structural role tags (format: `[Arc: Entry boundary / Gate boundary / Approval event / Terminal settlement]`) in the ECL-1 finding-to-epoch mapping lines and ECL-3 highest-density epoch declaration. Tests C-51 format-neutrality: can step-block format satisfy C-51 using structural role tags in ECL lines rather than a dedicated column? Predicted: 28 PASS = 81.9.

**V-04 hypothesis:** Finance → Sales two-pass multi-domain. R18 V-04 satisfies C-36/C-37/C-40/C-41/C-42/C-47/C-48/C-49/C-50/C-52/C-53 (36 PASS). **C-51 addition:** Both Finance and Sales LIFECYCLE EPOCH MAPs gain Arc Position columns. EPOCH-CLUSTER ANALYSIS updates: finding-to-epoch mapping carries Arc Position column; cross-domain highest-density epoch identification uses structural role vocabulary; inter-domain handoff remediation implication names the structural role of the handoff boundary ("Finance-Gate-boundary → Sales-Entry-boundary handoff IS the defect concentration site"). Tests C-51/C-52 synergy activation in two-pass format. Predicted: 37 PASS = 92.2.

**V-05 hypothesis:** Finance → Sales → CS three-pass multi-domain. R18 V-05 satisfies all multi-domain/multi-pass criteria (36 PASS). **C-51 addition:** All three LIFECYCLE EPOCH MAPs carry Arc Position columns. EPOCH-CLUSTER ANALYSIS updates: all three domain finding-to-epoch mappings carry Arc Position; cross-domain synthesis uses arc-position structural vocabulary for the inter-domain handoff remediation implication; both inter-domain boundaries (Finance→Sales and Sales→CS) are characterized by their structural role positions, not only by epoch names. Tests C-51/C-52 full synergy in three-domain format. Predicted: 37 PASS = 92.2.

---

## V-01 — Lifecycle Emphasis: Arc Position Column in LIFECYCLE EPOCH MAP (Sales)

**Variation axis:** Lifecycle emphasis — Arc Position structural role annotation (C-51) in single-domain tabular format
**Hypothesis:** Sales domain, single-pass tabular. C-51 probe: LIFECYCLE EPOCH MAP gains a mandatory Arc Position column (Entry boundary / Gate boundary / Approval event / Terminal settlement). Arc Position legend declared before table. EPOCH-CLUSTER ANALYSIS remediation implication references the structural role of the highest-density epoch, not only its name. Tests whether Arc Position column earns C-51 PASS in Sales domain and whether C-49/C-51 synergy language is achievable. Predicted: 28 PASS = 81.9.
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
| C11 | The LIFECYCLE EPOCH MAP IS REQUIRED to carry an Arc Position column assigning a structural role (Entry boundary / Gate boundary / Approval event / Terminal settlement) to every epoch. An EPOCH row without an Arc Position assignment IS a C11 violation. EPOCH-CLUSTER ANALYSIS IS BLOCKED until all epoch rows carry Arc Position assignments. | [T] | epoch structure |

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
Binding constraints: **C1, C2, C3, C5, C6, C7, C8, C9, C10, C11**.
Authorization status: [T]'s authorization IS CONTINGENT on HANDOFF DECLARATION. Prior to HANDOFF DECLARATION, [T] IS NOT AUTHORIZED to produce output in any [T]-owned section.
INERTIA BASELINE relationship: **[T]'s obligation IS NOT iterative development; it IS the commitment that converts the inertia certainty named above into a prevented outcome.** A blank [T] section IS NOT an in-progress state; it IS the inertia baseline already chosen. The specific regression form [T] prevents IS: untraced opportunity transitions shipping as assumed-valid precondition logic.

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
> 4. STATE DIAGRAM [D]: Node count: [N]. Edge count: [N]. [!] annotation count: [N].
> 5. VOCABULARY CLOSED: IS in effect. The vocabulary IS FROZEN. Retroactive modifications by [D] ARE PROHIBITED.
>
> **Post-transfer role states (both declared simultaneously at this moment):**
> [D] IS PROHIBITED from altering any declaration from this point forward. [D]'s modification authority IS REVOKED. This prohibition IS NOT WAIVABLE.
> [T] IS NOW AUTHORIZED to produce output in all [T]-owned sections. [T] WAS NOT AUTHORIZED prior to this moment; [T] IS AUTHORIZED now.
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

- [ ] INERTIA BASELINE IS present as document opener, includes PRODUCTION COST DECLARATION with IS NOT X / IS Y contrast framing, and includes IS-NEGATION PAIR
- [ ] CONSTRAINT MATRIX IS-authority preamble IS present — governing-authority declaration IS written before C1 row
- [ ] ROLES section carries IS-authority self-declaration opener AND per-role IS-negation obligation pair for both [D] and [T] with specific regression form named
- [ ] STATE DECLARATIONS ARE complete — domain vocabulary, inline definitional clauses, at least one Terminal: Yes item IS present
- [ ] OPERATION DECLARATIONS ARE complete — all S-ID references ARE resolved to STATE DECLARATIONS
- [ ] INVARIANT DECLARATIONS ARE complete — at least two boolean assertions with authority sources ARE present
- [ ] VOCABULARY CLOSED IS declared — IS-event self-declaration IS present as opener; vocabulary IS FROZEN; prohibition IS NOT WAIVABLE
- [ ] STATE DIAGRAM [D] IS complete — node count, edge count, [!] annotation count ARE declared and consistent
- [ ] HANDOFF DECLARATION IS signed — TRANSFER DECLARATION IS-transfer opener IS present; post-transfer role states ARE explicitly declared
- [ ] **[C7]** INVENTORY CHALLENGE IS resolved — Option A or Option B IS written; no C7 violation IS present
- [ ] **[C11]** [T] acknowledges: LIFECYCLE EPOCH MAP WILL carry Arc Position column with all four canonical roles (Entry boundary / Gate boundary / Approval event / Terminal settlement) assigned to every epoch row; an epoch row without Arc Position assignment IS a C11 violation; EPOCH-CLUSTER ANALYSIS IS BLOCKED until all rows ARE annotated

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

**V-01 VARIATION — ARC POSITION COLUMN (C-51).** This map IS NOT a labeling artifact; it IS the structural-role surface that makes epoch-grounded remediation possible. Each epoch carries an Arc Position assignment from the canonical vocabulary below. An epoch row without an Arc Position assignment IS a C11 violation. EPOCH-CLUSTER ANALYSIS IS BLOCKED until all epoch rows carry Arc Position assignments.

**Arc Position canonical vocabulary (C-51 compliant):**
- **Entry boundary** — IS the epoch where entities enter the tracked domain (lead capture, case open, invoice creation). Defects at Entry boundary ARE data-quality defects (missing fields, invalid initial states, unauthorized entry). Intervention IS NOT approval-gate hardening; it IS input validation at the first state transition.
- **Gate boundary** — IS the epoch where a formal qualification or approval decision is made. Defects at Gate boundary ARE authorization defects (qualification bypassed, required checks skipped). Intervention IS gate-enforcement hardening at the qualification transition.
- **Approval event** — IS the epoch where a binding commitment or authorization is issued. Defects at Approval event ARE commitment defects (commitment created without required prior approvals, binding state reached from invalid prior state). Intervention IS precondition enforcement at the commitment transition.
- **Terminal settlement** — IS the epoch where the entity exits the domain (closed won/lost, case resolved, payment settled). Defects at Terminal settlement ARE finalization defects (terminal state reached while active-state records remain open, terminal state bypassed). Intervention IS terminal-state transition locking.

Map each declared operation to its lifecycle epoch and arc position:

| O-ID | Operation Name | Lifecycle Epoch | Epoch Rationale | Arc Position |
|------|----------------|-----------------|-----------------|--------------|
| O-[N] | [from OPERATION DECLARATIONS] | OPEN-TRACK / QUALIFY / ADVANCE / CLOSE-TRACK | [why this operation belongs to this epoch in the Sales lifecycle arc] | Entry boundary / Gate boundary / Approval event / Terminal settlement |
*(one row per declared operation; Arc Position IS REQUIRED; blank Arc Position IS a C11 violation)*

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

- [ ] TRANSITION TABLE IS columnar and complete; no operation IS documented only in prose
- [ ] Every row HAS INV status per declared invariant; at least one VIOLATED row IS present
- [ ] Every row HAS at least one postcondition distinct from the To State name
- [ ] LIFECYCLE EPOCH MAP IS complete — every O-ID IS mapped to a lifecycle epoch AND an Arc Position from the canonical vocabulary (C11); an epoch row without Arc Position IS a C11 violation
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

- [ ] At least three (operation, state) invalid pairs ARE named with blocking conditions; enumeration IS systematic
- [ ] At least one INVALID TRANSITIONS row HAS From State = a Terminal item from STATE DECLARATIONS

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
- [ ] LIFECYCLE EPOCH MAP IS complete — all O-IDs ARE mapped to epochs AND Arc Position assignments (C11) — EPOCH-CLUSTER ANALYSIS IS BLOCKED without complete Arc Position annotations
- [ ] All TRANSITION TABLE and INVALID TRANSITIONS S-IDs and O-IDs ARE resolved to declarations (C1, C2)
- [ ] Hard-stop review IS complete — no section IS blank or placeholder-only

**GATE D: [T] IS BLOCKED from proceeding. FINDINGS IS BLOCKED until all items ARE confirmed. EPOCH-CLUSTER ANALYSIS IS BLOCKED until FINDINGS IS complete AND all LIFECYCLE EPOCH MAP Arc Position assignments ARE present (C11).**

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

**EPOCH-CLUSTER ANALYSIS IS NOT a summary of FINDINGS; it IS the analytical transformation that converts the LIFECYCLE EPOCH MAP Arc Position annotations into a structural-role-grounded defect-density surface. EPOCH-CLUSTER ANALYSIS IS BLOCKED until FINDINGS IS complete, the LIFECYCLE EPOCH MAP IS present with all O-IDs mapped, AND all epoch rows carry Arc Position assignments (C11).**

**V-01 VARIATION.** The remediation implication IS grounded in the Arc Position of the highest-density epoch — NOT the epoch name alone. A remediation that names only the epoch ("QUALIFY epoch carries the most defects") IS NOT a C-49/C-51 synergy-activated remediation; it IS a C-49 epoch-name-grounded remediation. A C-49/C-51 synergy-activated remediation names the structural role: "Gate boundary epoch carries the most defects — approval-gate hardening at this structural chokepoint IS the intervention, regardless of what this epoch IS named across domain vocabulary changes." The Arc Position vocabulary IS portable; epoch names ARE NOT.

**Finding-to-epoch mapping (Arc Position column required):**

| Finding ID | Title | Triggering Operation (O-ID) | Lifecycle Epoch | Arc Position | Defect Type |
|------------|-------|----------------------------|-----------------|--------------|-------------|
| F-[N] | [finding title from FINDINGS] | O-[N] | [epoch from LIFECYCLE EPOCH MAP] | [Arc Position from LIFECYCLE EPOCH MAP] | INVARIANT VIOLATION / INVALID TRANSITION / RACE CONDITION / FORECAST REFUTATION |
*(one row per finding in FINDINGS; Arc Position IS REQUIRED from the C11-annotated LIFECYCLE EPOCH MAP)*

**Epoch defect counts (with Arc Position):**

| Lifecycle Epoch | Arc Position | Defect Count | Finding IDs |
|-----------------|--------------|-------------|-------------|
| OPEN-TRACK | Entry boundary | [N] | [F-NN, ...] |
| QUALIFY | Gate boundary | [N] | [F-NN, ...] |
| ADVANCE | Approval event | [N] | [F-NN, ...] |
| CLOSE-TRACK | Terminal settlement | [N] | [F-NN, ...] |
*(epochs with zero defects ARE included; Arc Position column IS drawn from LIFECYCLE EPOCH MAP)*

**Highest-density epoch:** [Epoch name] — [N] of [total] defects (finding IDs: [F-NN, ...]).

**Structural role:** Arc Position IS [Entry boundary / Gate boundary / Approval event / Terminal settlement]. This IS NOT coincidental; the [Arc Position name] IS the structural position where [specific structural reason — e.g., "Gate boundary IS where qualification decisions are enforced; defect density here IS the signature of a gate whose precondition checks ARE assumed rather than enforced"].

**Remediation implication (C-49/C-51 synergy form):** [Intervention named by structural role, not epoch name. E.g., "The Gate boundary epoch (QUALIFY) carries [N] of [total] defects — this IS NOT a QUALIFY epoch problem; it IS a Gate boundary structural problem: the approval check at this position in the Sales lifecycle arc IS NOT enforced. Hardening the precondition at the qualification transition (O-[N]) IS the highest-leverage intervention. This remediation IS portable: if the epoch IS renamed in a future vocabulary revision, the Gate boundary structural role identifies the same intervention point."]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: INERTIA BASELINE, CONSTRAINT MATRIX, ROLES, STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION, INVENTORY CHALLENGE, GATE A, INVARIANT-VIOLATION FORECAST, TRANSITION TABLE, LIFECYCLE EPOCH MAP (with Arc Position column), FORECAST VALIDATION, GATE B, INVALID TRANSITIONS, GATE C, RACE CONDITIONS, GATE D, FINDINGS, EPOCH-CLUSTER ANALYSIS.

---

## V-02 — Lifecycle Emphasis: C-49/C-51 Synergy Confirmation Language (Finance)

**Variation axis:** Lifecycle emphasis — C-49/C-51 synergy language in EPOCH-CLUSTER ANALYSIS remediation implication
**Hypothesis:** Finance domain (Invoice: Draft / Submitted / Under-Review / Approved / Paid / Disputed / Void). Single-pass tabular. C-51 carried from R18 V-02 — Arc Position column is standard in LIFECYCLE EPOCH MAP. R19 probe: the EPOCH-CLUSTER ANALYSIS remediation implication is sharpened to use structural role vocabulary explicitly, confirming synergy activation. A remediation that names "APPROVAL epoch" is C-49 PASS but NOT synergy-activated. A remediation that names "Gate boundary epoch (APPROVAL)" IS synergy-activated. Tests whether explicit IS-negation language in the remediation section separates a generic C-49 PASS from a C-49/C-51 synergy-confirmed PASS. Predicted: 28 PASS = 81.9.
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
| C3 | The TRANSITION TABLE includes an EPOCH column. The EPOCH column IS informational; it IS NOT constrained by C1 or C2. EPOCH values ARE drawn from Finance lifecycle phase vocabulary (e.g., ORIGINATION / REVIEW / APPROVAL / SETTLEMENT) and ARE NOT required to match declared S-IDs. EPOCH data IS used to generate the LIFECYCLE EPOCH MAP secondary artifact. Prose paragraphs and bullet lists ARE NOT VALID as primary trace output; every operation IS REQUIRED as a table row. | [T] | format / scope |
| C4 | Any state or operation added after VOCABULARY CLOSED IS declared IS a retroactive violation; such additions ARE PROHIBITED | [D] | ordering |
| C5 | A blank invariant status cell in the TRANSITION TABLE IS NOT PERMITTED; every cell IS REQUIRED to contain HOLDS or VIOLATED | [T] | integrity |
| C6 | TRANSITION TABLE IS BLOCKED until GATE A IS confirmed AND INVARIANT-VIOLATION FORECAST IS complete | [T] | ordering |
| C7 | A blank or non-option response at INVENTORY CHALLENGE IS a C7 violation; GATE A IS BLOCKED in the presence of a C7 violation | [T] | completeness |
| C8 | INVALID TRANSITIONS IS BLOCKED until GATE B IS confirmed | [T] | ordering |
| C9 | RACE CONDITIONS IS BLOCKED until GATE C IS confirmed | [T] | ordering |
| C10 | STATE DIAGRAM [D] IS NOT a substitute for the TRANSITION TABLE; it IS the structural cross-check artifact. [D] IS REQUIRED to declare node count, edge count, and [!] annotation count at authoring time. | [D] | integrity |
| C11 | The LIFECYCLE EPOCH MAP IS REQUIRED to carry an Arc Position column assigning a structural role (Entry boundary / Gate boundary / Approval event / Terminal settlement) to every epoch row. An EPOCH row without an Arc Position assignment IS a C11 violation. EPOCH-CLUSTER ANALYSIS IS BLOCKED until all epoch rows carry Arc Position assignments. The EPOCH-CLUSTER ANALYSIS remediation implication IS REQUIRED to reference the Arc Position structural role — a remediation that names only the epoch name IS NOT a C-49/C-51 synergy-activated remediation. | [T] | epoch structure / synergy |

---

### ROLES

**ROLES IS NOT an organizational chart; ROLES IS the execution authority matrix for this trace. A section of this document without a named role assignment IS NOT shared ownership; it IS unowned obligation and IS the inertia baseline instantiated before any section IS produced. Every ownership claim below IS NOT advisory; it IS the assignment that makes execution authorized. An obligation not assigned to a named role IS NOT deferred; it IS absent.**

**[D] Domain Expert**
Auto-selected: Finance expert (Draft / Submitted / Under-Review / Approved / Paid / Disputed / Void).
Sections owned by [D]: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION.
Binding constraint: **C4**. The specific regression form [D] prevents IS: unvalidated invoice state vocabulary reaching the trace phase.

**[T] Trace Developer**
Sections owned by [T]: INVENTORY CHALLENGE response, INVARIANT-VIOLATION FORECAST, TRANSITION TABLE, LIFECYCLE EPOCH MAP, FORECAST VALIDATION, INVALID TRANSITIONS, RACE CONDITIONS, FINDINGS, EPOCH-CLUSTER ANALYSIS.
Binding constraints: **C1, C2, C3, C5, C6, C7, C8, C9, C10, C11**.
Authorization status: [T]'s authorization IS CONTINGENT on HANDOFF DECLARATION. The specific regression form [T] prevents IS: untraced invoice transitions shipping as assumed-valid financial approval rules.

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

### INVARIANT DECLARATIONS [D], VOCABULARY CLOSED [D], STATE DIAGRAM [D], HANDOFF DECLARATION [D]

*(same structure as V-01; Finance domain; VOCABULARY CLOSED preamble IS NOT a label; HANDOFF DECLARATION TRANSFER DECLARATION IS NOT a coordination event)*

---

### INVENTORY CHALLENGE, GATE A

*(same structure as V-01; GATE A adds C11 acknowledgment: [T] acknowledges LIFECYCLE EPOCH MAP WILL carry Arc Position column AND EPOCH-CLUSTER ANALYSIS remediation implication WILL reference structural role vocabulary, not epoch name alone)*

---

### INVARIANT-VIOLATION FORECAST [T], TRANSITION TABLE [T]

*(same structure as V-01; Finance S-IDs and O-IDs; EPOCH column: ORIGINATION / REVIEW / APPROVAL / SETTLEMENT)*

---

### LIFECYCLE EPOCH MAP [T]

**V-02 VARIATION — ARC POSITION COLUMN + SYNERGY PRIMER (C-51).** Each epoch entry carries an Arc Position field naming the epoch's structural role in the Finance lifecycle arc. This Arc Position IS the anchor for the EPOCH-CLUSTER ANALYSIS remediation implication. The Arc Position IS NOT a label for the epoch's name; it IS a structural-role assignment that IS portable across domain vocabulary changes. An EPOCH-CLUSTER ANALYSIS remediation that names only "APPROVAL epoch" IS NOT synergy-activated; one that names "Gate boundary epoch (APPROVAL)" IS synergy-activated.

| O-ID | Operation Name | Lifecycle Epoch | Epoch Rationale | Arc Position |
|------|----------------|-----------------|-----------------|--------------|
| O-[N] | [from OPERATION DECLARATIONS] | ORIGINATION / REVIEW / APPROVAL / SETTLEMENT | [why this operation belongs to this epoch] | Entry boundary / Gate boundary / Approval event / Terminal settlement |
*(one row per declared operation; Arc Position IS REQUIRED; a blank Arc Position IS a C11 violation)*

**Finance epoch arc position assignments:**
- **ORIGINATION** — Arc Position IS Entry boundary. Defects here ARE data-quality defects: missing fields, invalid amounts, unauthorized submitters. Intervention IS input validation at Draft → Submitted. Remediation IS NOT approval-gate hardening; it IS entry-validation hardening.
- **REVIEW** — Arc Position IS Gate boundary. Defects here ARE routing defects: wrong reviewer, bypass of review assignment. Intervention IS assignment-rule enforcement at the gate where review is authorized.
- **APPROVAL** — Arc Position IS Approval event. Defects here ARE authorization defects: approval without required dual sign-off, approval under threshold bypass. Intervention IS approval-gate hardening at the event where binding approval IS issued.
- **SETTLEMENT** — Arc Position IS Terminal settlement. Defects here ARE finalization defects: paid invoices re-entering dispute, void invoices appearing active. Intervention IS terminal-state transition locking.

---

### FORECAST VALIDATION [T], GATE B, INVALID TRANSITIONS [T], GATE C, RACE CONDITIONS [T], GATE D

*(same structure as V-01; GATE D adds: LIFECYCLE EPOCH MAP Arc Position assignments ARE present AND EPOCH-CLUSTER ANALYSIS remediation implication WILL use structural role vocabulary)*

---

### FINDINGS [T]

*(same structure as V-01)*

---

### EPOCH-CLUSTER ANALYSIS [T]

**EPOCH-CLUSTER ANALYSIS IS NOT a summary of FINDINGS; it IS the analytical transformation that converts Arc Position annotations into a structural-role-grounded defect-density surface. EPOCH-CLUSTER ANALYSIS IS BLOCKED until FINDINGS IS complete AND the LIFECYCLE EPOCH MAP IS present with all Arc Position assignments (C11).**

**V-02 SYNERGY REQUIREMENT.** The C-49/C-51 synergy IS NOT automatic. Synergy IS activated only when the remediation implication references the Arc Position structural role rather than only the epoch name. The scoring distinction IS:
- C-49 PASS (no synergy): "APPROVAL epoch carries [N] of [total] defects — hardening the approval check IS the intervention."
- C-49/C-51 synergy-activated: "Gate boundary epoch (APPROVAL) carries [N] of [total] defects — this IS NOT an APPROVAL epoch-name finding; it IS a Gate boundary structural-role finding. The intervention IS approval-gate hardening at the Gate boundary position in the Finance lifecycle arc. This remediation IS vocabulary-portable: if Finance renames its APPROVAL epoch, the Gate boundary structural role identifies the same intervention point."

**Finding-to-epoch mapping (Arc Position column required):**

| Finding ID | Title | Triggering O-ID | Lifecycle Epoch | Arc Position | Defect Class |
|------------|-------|-----------------|-----------------|--------------|--------------|
| F-[N] | [from FINDINGS] | O-[N] | [from LIFECYCLE EPOCH MAP] | [from Arc Position column] | data-quality / routing / authorization / terminal-lock |

**Epoch defect counts (with Arc Position):**

| Lifecycle Epoch | Arc Position | Defect Count | Finding IDs |
|-----------------|--------------|-------------|-------------|
| ORIGINATION | Entry boundary | [N] | [F-NN] |
| REVIEW | Gate boundary | [N] | [F-NN] |
| APPROVAL | Approval event | [N] | [F-NN] |
| SETTLEMENT | Terminal settlement | [N] | [F-NN] |

**Highest-density epoch:** [Epoch name] — [N] of [total] defects. Arc Position: [structural role from Arc Position column].

**Defect class (from Arc Position):** [The defect class for this Arc Position — Entry boundary → data-quality; Gate boundary → routing/authorization; Approval event → authorization/commitment; Terminal settlement → finalization/locking].

**Remediation implication (C-49/C-51 synergy form):** [Structural-role-grounded intervention. IS-NOT / IS contrast REQUIRED. E.g., "Gate boundary epoch (REVIEW) carries [N] of [total] defects. This IS NOT a REVIEW epoch name problem; it IS a Gate boundary structural-role problem: the routing check at this gate IS NOT enforced. The defect class at Gate boundary IS routing defects — not authorization defects. The intervention IS assignment-rule enforcement at the Gate boundary transition (O-[N]: Submitted → Under-Review), not at the Approval event. A remediation targeted at O-[N] (Approval event) IS NOT the highest-leverage action; it IS a downstream address of an upstream gap."]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: INERTIA BASELINE, CONSTRAINT MATRIX, ROLES, STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION, INVENTORY CHALLENGE, GATE A, INVARIANT-VIOLATION FORECAST, TRANSITION TABLE, LIFECYCLE EPOCH MAP (with Arc Position column), FORECAST VALIDATION, GATE B, INVALID TRANSITIONS, GATE C, RACE CONDITIONS, GATE D, FINDINGS, EPOCH-CLUSTER ANALYSIS.

---

## V-03 — Output Format: Arc Position Structural Role Tags in Step-Block ECL Entries (Customer Service)

**Variation axis:** Output format — C-51 in step-block format via structural role tags in ECL epoch entries
**Hypothesis:** Customer Service domain (Support Ticket: New / Assigned / In-Progress / Pending-Customer / Resolved / Closed). Step-block format. C-38/C-39 active. C-48 saturation standard. C-49 satisfied as ECL step blocks (R18 structure carried). **C-51 addition:** ECL-1 finding-to-epoch mapping lines carry a `[Arc: structural role]` tag per epoch entry; ECL-3 highest-density epoch declaration includes Arc Position structural role label. Tests whether C-51 is satisfiable in step-block format without a dedicated column — format-neutral test per C-51 rubric specification. Predicted: 28 PASS = 81.9.
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
| C11 | The LIFECYCLE EPOCH MAP IS REQUIRED to carry an Arc Position assignment for every epoch row. In step-block format, Arc Position IS expressed as a `[Arc: structural role]` tag on the Epoch Rationale field rather than a dedicated column. An epoch entry without an `[Arc: ...]` tag IS a C11 violation. The ECL-3 highest-density epoch declaration IS REQUIRED to name the Arc Position structural role. EPOCH-CLUSTER ANALYSIS IS BLOCKED until all epoch entries carry Arc Position tags. | [T] | epoch structure / format-neutral C-51 |

---

### ROLES

**ROLES IS NOT an organizational chart; ROLES IS the execution authority matrix for this trace. A section without a named role assignment IS NOT shared ownership; it IS unowned obligation and IS the inertia baseline instantiated before any section IS produced.**

**[D] Domain Expert**
Auto-selected: Customer Service expert (New / Assigned / In-Progress / Pending-Customer / Resolved / Closed).
Sections owned by [D]: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION.
Binding constraint: **C4**. The specific regression form [D] prevents IS: unvalidated ticket state vocabulary reaching the trace phase.

**[T] Trace Developer**
Sections owned by [T]: INVENTORY CHALLENGE response, INVARIANT-VIOLATION FORECAST, TRACE BLOCKS, LIFECYCLE EPOCH MAP, FORECAST VALIDATION, INVALID TRANSITIONS, RACE CONDITIONS, FINDINGS, EPOCH-CLUSTER ANALYSIS.
Binding constraints: **C1, C2, C3, C5, C6, C7, C8, C9, C10, C11**.
Authorization status: [T]'s authorization IS CONTINGENT on HANDOFF DECLARATION. The specific regression form [T] prevents IS: untraced ticket transitions shipping as assumed-valid precondition logic.

---

### STATE DECLARATIONS [D], OPERATION DECLARATIONS [D], INVARIANT DECLARATIONS [D], VOCABULARY CLOSED [D], STATE DIAGRAM [D], HANDOFF DECLARATION [D]

*(same structure as V-01; CS vocabulary: New, Assigned, In-Progress, Pending-Customer, Resolved, Closed; VOCABULARY CLOSED preamble IS NOT a label; HANDOFF DECLARATION TRANSFER DECLARATION IS NOT a coordination event)*

---

### INVENTORY CHALLENGE, GATE A

*(same structure as V-01; GATE A adds C11 acknowledgment: [T] acknowledges LIFECYCLE EPOCH MAP WILL carry Arc Position tags on all epoch entries in `[Arc: structural role]` format, and ECL-3 WILL name the Arc Position structural role of the highest-density epoch)*

---

### INVARIANT-VIOLATION FORECAST [T]

*(same structure as V-01)*

---

### TRACE BLOCKS [T]

**V-03 FORMAT.** Each operation IS traced as a labeled step block. Step-block label format: `**[C-38: trace Before/Op/After state triple — FAILS if: any field IS left blank or S-ID IS NOT from STATE DECLARATIONS] [C-39: disqualify on blank INV sub-field — FAILS if: INV sub-field IS blank or does not contain HOLDS or VIOLATED] Step N: O-[NN] — [Operation Name]**`. The label simultaneously satisfies C-38 (criterion-instruction fusion) and C-39 (disqualification-condition fusion).

**Block structure for each operation:**

```
**[C-38: trace Before/Op/After state triple — FAILS if: any field IS left blank or S-ID IS NOT from STATE DECLARATIONS] [C-39: disqualify on blank INV sub-field — FAILS if: INV sub-field IS blank or does not contain HOLDS or VIOLATED] Step N: O-[NN] — [Operation Name]**

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

**V-03 VARIATION — ARC POSITION TAGS IN STEP-BLOCK FORMAT (C-11 / C-51).** In step-block format, Arc Position IS NOT expressed as a dedicated table column; it IS expressed as a `[Arc: structural role]` tag within the Epoch Rationale field. An epoch entry without an `[Arc: ...]` tag IS a C11 violation. This IS the step-block format expression of C-51. Format-neutrality test: the canonical Arc Position vocabulary (Entry boundary / Gate boundary / Approval event / Terminal settlement) IS the same regardless of format.

**Arc Position canonical vocabulary:**
- `[Arc: Entry boundary]` — IS the epoch where tickets enter the support lifecycle (new ticket created, case opened). Defects here ARE intake defects (missing fields, unauthorized creation, duplicate creation). Intervention IS NOT escalation-gate hardening; it IS creation-validation at the New → Assigned transition.
- `[Arc: Gate boundary]` — IS the epoch where a formal assignment or escalation decision is made. Defects here ARE assignment defects (wrong agent, queue bypass). Intervention IS assignment-rule enforcement at the gate.
- `[Arc: Approval event]` — IS the epoch where a binding resolution or closure authorization is issued. Defects here ARE resolution defects (resolved without customer acknowledgment, closed without resolution record). Intervention IS resolution precondition enforcement.
- `[Arc: Terminal settlement]` — IS the epoch where the ticket exits the support lifecycle (case closed, entitlement terminated). Defects here ARE closure defects (closed tickets reopened without escalation, closed state bypassed). Intervention IS terminal-state transition locking.

| O-ID | Operation Name | Lifecycle Epoch | Epoch Rationale + Arc Position Tag |
|------|----------------|-----------------|-------------------------------------|
| O-[N] | [from OPERATION DECLARATIONS] | INTAKE / ACTIVE / PENDING / RESOLUTION | [why this operation belongs to this epoch] [Arc: Entry boundary / Gate boundary / Approval event / Terminal settlement] |
*(one row per declared operation; `[Arc: ...]` tag IS REQUIRED on every row; a row without `[Arc: ...]` IS a C11 violation)*

---

### FORECAST VALIDATION [T], GATE B, INVALID TRANSITIONS [T], GATE C, RACE CONDITIONS [T], GATE D

*(same structure as V-01; adapted for step-block format terminology; GATE D adds: LIFECYCLE EPOCH MAP Arc Position tags ARE present on all epoch entries AND ECL-3 WILL name Arc Position structural role of highest-density epoch)*

---

### FINDINGS [T]

*(same structure as V-01)*

---

### EPOCH-CLUSTER ANALYSIS [T]

**EPOCH-CLUSTER ANALYSIS IS NOT a summary of FINDINGS; it IS the analytical transformation that converts the LIFECYCLE EPOCH MAP from a labeling artifact into a structural-role-grounded defect-density surface. EPOCH-CLUSTER ANALYSIS IS BLOCKED until FINDINGS IS complete AND the LIFECYCLE EPOCH MAP IS present with all O-IDs mapped AND all Arc Position tags ARE present (C11).**

**V-03 FORMAT.** EPOCH-CLUSTER ANALYSIS IS produced as a labeled step-block analysis section (not a table), demonstrating that C-49 IS format-neutral. **C-51 addition:** Each ECL epoch entry carries a `[Arc: structural role]` tag from the LIFECYCLE EPOCH MAP. ECL-3 highest-density epoch declaration names the Arc Position structural role. ECL-4 remediation implication IS grounded in the structural role, not the epoch name.

**Step ECL-1: Finding-to-Epoch Mapping (with Arc Position tags)**
For each finding F-[N] in FINDINGS: identify the triggering O-ID from the finding's Source field; look up the O-ID's epoch and Arc Position tag in the LIFECYCLE EPOCH MAP; record:
- F-[N] ("[title]") — triggered by O-[NN] — Epoch: [INTAKE / ACTIVE / PENDING / RESOLUTION] — [Arc: Entry boundary / Gate boundary / Approval event / Terminal settlement]
*(one line per finding; `[Arc: ...]` tag IS REQUIRED from LIFECYCLE EPOCH MAP)*

**Step ECL-2: Epoch Defect Count**
Count findings per epoch (Arc Position tag included for each):
- INTAKE [Arc: Entry boundary]: [N] defects — [F-NN, ...]
- ACTIVE [Arc: Gate boundary]: [N] defects — [F-NN, ...]
- PENDING [Arc: Approval event]: [N] defects — [F-NN, ...]
- RESOLUTION [Arc: Terminal settlement]: [N] defects — [F-NN, ...]

**Step ECL-3: Highest-Density Epoch (with Arc Position)**
Highest-density epoch IS: [Epoch name] [Arc: structural role] ([N] of [total] defects; finding IDs: [F-NN, ...]).
This epoch IS NOT randomly dense; it IS the epoch where [specific structural reason tied to the Arc Position role — e.g., "RESOLUTION [Arc: Terminal settlement] IS dense because the Resolved → Closed transition IS currently unguarded; the invariant requiring customer acknowledgment before resolution IS authorized IS NOT enforced at this Terminal settlement position"].

**Step ECL-4: Remediation Implication (C-49/C-51 synergy form)**
The remediation IS NOT broad process improvement; it IS a structural-role-grounded gate-hardening action. The IS-NOT / IS contrast IS REQUIRED.
[E.g., "RESOLUTION epoch carries [N] of [total] defects. This IS NOT a RESOLUTION epoch name problem; it IS a Terminal settlement structural-role problem — the Resolved → Closed gate IS NOT locked against backwards re-entry. The specific intervention IS: add a terminal-state transition lock at O-[N] (Resolved → Closed) that IS NOT bypassable once the terminal state IS reached. This remediation IS vocabulary-portable: if the CS domain renames its RESOLUTION epoch, the Terminal settlement structural role identifies the same intervention point."]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: INERTIA BASELINE, CONSTRAINT MATRIX, ROLES, STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION, INVENTORY CHALLENGE, GATE A, INVARIANT-VIOLATION FORECAST, TRACE BLOCKS, LIFECYCLE EPOCH MAP (with Arc Position tags), FORECAST VALIDATION, GATE B, INVALID TRANSITIONS, GATE C, RACE CONDITIONS, GATE D, FINDINGS, EPOCH-CLUSTER ANALYSIS.

---

## V-04 — Role Sequence × Lifecycle Emphasis: Arc Position in Both LIFECYCLE EPOCH MAPs + C-52 Synergy (Finance → Sales)

**Variation axis:** Role sequence (Finance-first) × Lifecycle emphasis (Arc Position in both LIFECYCLE EPOCH MAPs); C-51 activates C-52 synergy in cross-domain EPOCH-CLUSTER ANALYSIS
**Hypothesis:** Finance → Sales two-domain multi-pass. R18 V-04 satisfies C-36/C-37/C-40/C-41/C-42/C-47/C-48/C-49/C-50/C-52/C-53 (36 PASS). **C-51 addition:** Both Finance and Sales LIFECYCLE EPOCH MAPs gain Arc Position columns. EPOCH-CLUSTER ANALYSIS cross-domain synthesis: finding-to-epoch mapping carries Arc Position column; highest-density epoch identification uses structural role vocabulary; inter-domain handoff remediation implication names the structural role boundary ("Finance Gate boundary → Sales Entry boundary handoff IS the defect concentration site — not the epoch names but the structural boundary between approval and intake"). Tests C-51/C-52 synergy activation in two-pass format. Predicted: 37 PASS = 92.2.
**Domain:** Finance (Invoice: Draft → Approved) → Sales (Opportunity: Proposal → Committed)

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

**Arc Position cross-domain note:** The Finance Arc Position vocabulary and the Sales Arc Position vocabulary ARE DISTINCT domain vocabularies sharing the same structural role set. A Finance APPROVAL epoch `[Arc: Approval event]` and a Sales ADVANCE epoch `[Arc: Approval event]` occupy the same structural role in their respective domain arcs — this IS the basis for the cross-domain epoch vocabulary synthesis in EPOCH-CLUSTER ANALYSIS (C-52): structural roles ARE the cross-domain comparison axis, not epoch names.

**This declaration IS NOT WAIVABLE and IS NOT AMENDABLE by [D] or [T].**

---

You are running a **trace-state** signal for: {{topic}} — multi-domain multi-pass (Finance → Sales).

Produce a two-pass state machine trace. Pass 1 traces the Finance domain. Pass 2 traces the Sales domain with cross-domain bridge annotations. This trace IS a formal artifact; its governing document IS the CONSTRAINT MATRIX below. The DOMAIN DEPENDENCY DECLARATION IS AUTHORITATIVE for domain ordering. Read both completely before producing any output.

---

### CONSTRAINT MATRIX

**MATRIX AUTHORITY.** The CONSTRAINT MATRIX IS the governing authority for this trace and IS NOT AMENDABLE by [D] or [T]. A constraint not named in this matrix IS NOT binding on this trace. No role IS authorized to add, waive, or modify a constraint. The scope of this matrix IS total.

| ID | Architectural Fact | Assigned Role | Concern |
|----|--------------------|---------------|---------|
| C1 | A state name not declared in STATE DECLARATIONS IS PROHIBITED in any trace table in either domain pass | [T] | vocabulary |
| C2 | An operation name not declared in OPERATION DECLARATIONS IS PROHIBITED in any trace table in either domain pass | [T] | vocabulary |
| C3 | Each TRANSITION TABLE includes an EPOCH column. Finance EPOCH vocabulary: ORIGINATION / REVIEW / APPROVAL / SETTLEMENT. Sales EPOCH vocabulary: OPEN-TRACK / QUALIFY / ADVANCE / CLOSE-TRACK. EPOCH IS informational; IS NOT constrained by C1/C2. | [T] | format / scope |
| C4 | Any state or operation added after VOCABULARY CLOSED IS declared IS a retroactive violation; such additions ARE PROHIBITED | [D] | ordering |
| C5 | A blank invariant status cell in any TRANSITION TABLE IS NOT PERMITTED | [T] | integrity |
| C6 | Pass 1 TRANSITION TABLE IS BLOCKED until GATE A IS confirmed. Pass 2 TRANSITION TABLE IS BLOCKED until Pass 1 IS complete AND BRIDGE TABLE IS declared | [T] | ordering |
| C7 | A blank or non-option response at INVENTORY CHALLENGE IS a C7 violation | [T] | completeness |
| C8 | INVALID TRANSITIONS (both passes) IS BLOCKED until GATE B IS confirmed | [T] | ordering |
| C9 | RACE CONDITIONS IS BLOCKED until GATE C IS confirmed | [T] | ordering |
| C10 | STATE DIAGRAM [D] IS NOT a substitute for the TRANSITION TABLE; one STATE DIAGRAM IS REQUIRED per domain | [D] | integrity |
| C11 | Pass 2 TRANSITION TABLE IS BLOCKED until the BRIDGE TABLE explicitly names at least one Finance postcondition as a Sales precondition | [T] | cross-domain ordering |
| C12 | Both LIFECYCLE EPOCH MAPs (Finance and Sales) ARE REQUIRED to carry Arc Position columns (Entry boundary / Gate boundary / Approval event / Terminal settlement) on every epoch row. An epoch row without Arc Position assignment IS a C12 violation. EPOCH-CLUSTER ANALYSIS IS BLOCKED until both maps carry complete Arc Position assignments. The cross-domain EPOCH-CLUSTER ANALYSIS remediation implication IS REQUIRED to reference structural role vocabulary at the inter-domain handoff boundary (naming Finance structural role AND Sales structural role at the boundary, not only their epoch names). | [T] | epoch structure / cross-domain synergy |

---

### ROLES

**ROLES IS NOT an organizational chart; ROLES IS the execution authority matrix for this trace. A section without a named role assignment IS NOT shared ownership; it IS unowned obligation and IS the inertia baseline instantiated before any section IS produced.**

**[D] Domain Expert**
Auto-selected: Finance expert (Pass 1) AND Sales expert (Pass 2) — the same [D] role IS responsible for both domain declarations. An incomplete domain declaration IS NOT a deferred section; it IS the inertia baseline chosen before [T] begins.
Sections owned by [D]: both domain STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAMS, HANDOFF DECLARATIONS.
Binding constraint: **C4** (vocabulary IS FROZEN across both domains after VOCABULARY CLOSED IS declared).

**[T] Trace Developer**
Sections owned by [T]: INVENTORY CHALLENGE, both domain INVARIANT-VIOLATION FORECASTs, BRIDGE TABLE, both domain TRANSITION TABLEs, both domain LIFECYCLE EPOCH MAPs (with Arc Position columns per C12), both domain FORECAST VALIDATIONs, INVALID TRANSITIONS (both passes), RACE CONDITIONS, FINDINGS, EPOCH-CLUSTER ANALYSIS.
Authorization: [T] IS NOT AUTHORIZED to begin Pass 2 until Pass 1 IS complete AND BRIDGE TABLE IS declared (C11). [T]'s authorization IS CONTINGENT on HANDOFF DECLARATION. [T] acknowledges: EPOCH-CLUSTER ANALYSIS remediation implication WILL name structural roles at the inter-domain handoff boundary (C12).

---

### Pass 1: Finance Domain

**### Pass 1 — Finance [C-36: Finance-first ordering targets cross-domain precondition defects — FAILS if: Pass 2 begins before Finance approval state resolved] [C-37: unresolved Finance state IS the failure mode that creates unauthorized Sales commitments; Pass 1 IS NOT a preamble; it IS the dependency root] [C-42: Finance IS ordered first because Sales commitment preconditions ARE Finance-derived; the defect class targeted IS: downstream-commitment-without-upstream-approval]**

#### STATE DECLARATIONS [D] — Finance

**S-F01.** [Finance State Name] — [inline definitional clause]. Terminal: Yes/No.
*(Finance typical set: Draft, Submitted, Under-Review, Approved — minimum one Terminal: Yes)*

#### OPERATION DECLARATIONS [D] — Finance, INVARIANT DECLARATIONS [D] — Finance, VOCABULARY CLOSED [D] — Finance, STATE DIAGRAM [D] — Finance, HANDOFF DECLARATION [D] — Finance

*(same structure as V-01; Finance domain; VOCABULARY CLOSED preamble: Finance domain — VOCABULARY CLOSED IS NOT a label; it IS the irreversibility event for the Finance domain)*

#### INVARIANT-VIOLATION FORECAST [T] — Finance

*(one row per Finance O-ID; blank cells ARE NOT PERMITTED)*

| O-ID | Operation Name | Predicted INV-F01 | Predicted INV-F02 | Rationale |
|------|----------------|------------------|------------------|-----------|

#### GATE A — Finance Pass

*(standard blocking items; adds C12 acknowledgment: Finance LIFECYCLE EPOCH MAP WILL carry Arc Position column with canonical role assigned to every epoch row)*

**GATE A: [T] IS BLOCKED. Pass 1 TRANSITION TABLE IS BLOCKED until all items ARE confirmed.**

#### TRANSITION TABLE [T] — Finance (Pass 1)

*(standard table structure; Finance S-IDs and O-IDs only; EPOCH column: ORIGINATION / REVIEW / APPROVAL / SETTLEMENT)*

#### LIFECYCLE EPOCH MAP [T] — Finance (with Arc Position column)

**C12 REQUIREMENT.** Finance LIFECYCLE EPOCH MAP IS REQUIRED to carry Arc Position column. An epoch row without Arc Position assignment IS a C12 violation. EPOCH-CLUSTER ANALYSIS IS BLOCKED until all Finance epoch rows carry Arc Position assignments.

**Finance epoch arc position assignments:**
- ORIGINATION — Arc Position IS Entry boundary. Defects: data-quality (missing fields, invalid amounts). Intervention: entry-validation hardening.
- REVIEW — Arc Position IS Gate boundary. Defects: routing (reviewer bypass, wrong assignment). Intervention: assignment-rule enforcement.
- APPROVAL — Arc Position IS Approval event. Defects: authorization (dual sign-off bypass, approval threshold miss). Intervention: approval-gate hardening.
- SETTLEMENT — Arc Position IS Terminal settlement. Defects: finalization (paid invoices re-entering dispute). Intervention: terminal-state locking.

| O-ID | Operation Name | Lifecycle Epoch | Epoch Rationale | Arc Position |
|------|----------------|-----------------|-----------------|--------------|
| O-F[N] | [from Finance OPERATION DECLARATIONS] | ORIGINATION / REVIEW / APPROVAL / SETTLEMENT | [why this operation belongs to this epoch] | Entry boundary / Gate boundary / Approval event / Terminal settlement |
*(one row per Finance operation; Arc Position IS REQUIRED; blank IS a C12 violation)*

#### FORECAST VALIDATION [T] — Finance

*(compare Finance forecast against Pass 1 TRANSITION TABLE results)*

---

#### BRIDGE TABLE [T]

**BRIDGE TABLE IS NOT an optional annotation; it IS the cross-domain precondition chain that makes Pass 2 authorization conditional. Pass 2 TRANSITION TABLE IS BLOCKED until at least one Finance postcondition IS explicitly named as a Sales precondition in this table (C11). The BRIDGE TABLE IS NOT advisory; it IS the record that proves the dependency chain declared in DOMAIN DEPENDENCY DECLARATION IS traceable to specific state records. C-47 confirmation annotations WILL cite BRIDGE TABLE rows by reference ("BRIDGE TABLE row F→S row [N]") — unnamed chain references ARE NOT VALID for C-47 when a BRIDGE TABLE IS present.**

| Bridge Row | Finance Postcondition (Pass 1 Row #) | Finance State After (S-F ID) | Bridge: Seeds Sales Precondition | Sales State Blocked Until (S-S ID) |
|------------|--------------------------------------|------------------------------|----------------------------------|-------------------------------------|
| F→S-[N] | [Pass 1 row number] | S-F[N] ([Finance State]) | Finance [field/state] IS REQUIRED before Sales O-[N] IS authorized | S-S[N] (IS NOT reachable until this bridge condition IS met) |
*(minimum one bridge row IS REQUIRED; C11 violation IS present until this table IS non-empty; bridge rows ARE named F→S-[N] for C-47 citation)*

---

### Pass 2: Sales Domain

**### Pass 2 — Sales [C-36: Sales-second ordering targets Finance-derived precondition defects — FAILS if: any Sales precondition IS asserted without a BRIDGE TABLE row reference] [C-37: a Sales commitment without a Finance approval bridge row IS the revenue-commitment failure mode this artifact exists to prevent; proceeding without BRIDGE TABLE IS NOT a shortcut; it IS the failure mode instantiated] [C-42: Sales IS ordered second because commitment preconditions ARE Finance-derived (DOMAIN DEPENDENCY DECLARATION); the defect class targeted IS: Sales-commits-without-Finance-approval; BRIDGE TABLE row F→S-[N] IS the detection surface]**

#### STATE DECLARATIONS [D] — Sales, OPERATION DECLARATIONS [D] — Sales, INVARIANT DECLARATIONS [D] — Sales, VOCABULARY CLOSED [D] — Sales, STATE DIAGRAM [D] — Sales, HANDOFF DECLARATION [D] — Sales

*(same structure; Sales domain: Proposal, Negotiation, Committed, Closed-Won, Closed-Lost; VOCABULARY CLOSED preamble IS NOT a label for the Sales domain)*

#### INVARIANT-VIOLATION FORECAST [T] — Sales

*(one row per Sales O-ID)*

#### GATE A — Sales Pass

**GATE A (Sales Pass) IS NOT clearable until BRIDGE TABLE IS present with at least one bridge row (C11). C12 acknowledgment: Sales LIFECYCLE EPOCH MAP WILL carry Arc Position column with canonical role assigned to every epoch row.**

*(standard blocking items + C11 bridge requirement + C12 Arc Position acknowledgment)*

#### TRANSITION TABLE [T] — Sales (Pass 2)

*(standard table structure; Sales S-IDs and O-IDs only; EPOCH: OPEN-TRACK / QUALIFY / ADVANCE / CLOSE-TRACK)*

**Cross-domain precondition annotation (C-41):** For any Sales row where the precondition references a Finance state, annotate: "Precondition derived from BRIDGE TABLE row F→S-[N]: Finance [state/field] IS REQUIRED before this Sales operation IS authorized." C-47 confirmations WILL cite these named bridge rows.

#### LIFECYCLE EPOCH MAP [T] — Sales (with Arc Position column)

**C12 REQUIREMENT.** Sales LIFECYCLE EPOCH MAP IS REQUIRED to carry Arc Position column. An epoch row without Arc Position assignment IS a C12 violation. EPOCH-CLUSTER ANALYSIS cross-domain synthesis WILL use Sales Arc Position vocabulary in the inter-domain handoff remediation implication.

**Sales epoch arc position assignments:**
- OPEN-TRACK — Arc Position IS Entry boundary. Defects: lead intake (unqualified leads entering pipeline). Intervention: entry-qualification hardening.
- QUALIFY — Arc Position IS Gate boundary. Defects: qualification bypass (opportunity advanced without qualification criteria met). Intervention: qualification-gate enforcement.
- ADVANCE — Arc Position IS Approval event. Defects: commitment without approval (committed without Finance approval record). Intervention: precondition enforcement at commitment transition.
- CLOSE-TRACK — Arc Position IS Terminal settlement. Defects: closure (closed-won with open pipeline records, closed-lost records remaining active). Intervention: terminal-state locking.

| O-ID | Operation Name | Lifecycle Epoch | Epoch Rationale | Arc Position |
|------|----------------|-----------------|-----------------|--------------|
| O-S[N] | [from Sales OPERATION DECLARATIONS] | OPEN-TRACK / QUALIFY / ADVANCE / CLOSE-TRACK | [why this operation belongs to this epoch] | Entry boundary / Gate boundary / Approval event / Terminal settlement |
*(one row per Sales operation; Arc Position IS REQUIRED; blank IS a C12 violation)*

#### FORECAST VALIDATION [T] — Sales

*(compare Sales forecast against Pass 2 TRANSITION TABLE results)*

---

### GATE B, INVALID TRANSITIONS (both passes), GATE C, RACE CONDITIONS

*(standard structure; covers both Finance and Sales domains; GATE B adds: both LIFECYCLE EPOCH MAPs IS complete with Arc Position columns — C12 satisfied for both passes)*

---

### GATE D

**GATE D IS NOT a checkpoint list; it IS the enforcement mechanism that makes FINDINGS and EPOCH-CLUSTER ANALYSIS authorization conditional. A GATE D not fully confirmed IS NOT a cleared gate.**

*(standard blocking items + requirement that both domain LIFECYCLE EPOCH MAPs carry complete Arc Position assignments; EPOCH-CLUSTER ANALYSIS cross-domain remediation implication WILL use structural role vocabulary at the inter-domain handoff boundary)*

---

### FINDINGS [T]

*(standard structure; findings may reference either domain pass; cross-domain bridge defects ARE priority findings)*

**Cross-domain finding template:**
- **P[N]: [title]**
  Source: [Pass 1 row N / Pass 2 row N / BRIDGE TABLE row F→S-[N]].
  Cross-domain dependency: [which BRIDGE TABLE row surfaces the dependency that this finding violates; a cross-domain finding without a named bridge row reference IS NOT traceable].
  Inertia connection: [traces to INERTIA BASELINE failure mode].
  Disposition: [Status IS ACCEPTED / Action IS REQUIRED].
  Severity: FATAL / DEGRADED / COSMETIC.

**Per-pass defect (C-40):** At least one labeled defect IS REQUIRED per domain pass. A pass with no finding IS NOT an acceptable result; it IS an incomplete trace.

**Defect-hypothesis confirmation (C-47):** For multi-pass findings, confirm or refute the C-42 defect-class prediction. C-47 confirmation MUST cite: (1) the defect class from the C-42 pass heading annotation, AND (2) the named BRIDGE TABLE row from C-41 annotations. Example: "CONFIRMS Sales-commits-without-Finance-approval defect class (C-42 prediction: Pass 2) — triggered by BRIDGE TABLE row F→S-[N]: Finance.Approved IS the Sales.Commit precondition that WAS NOT enforced."

---

### EPOCH-CLUSTER ANALYSIS [T]

**EPOCH-CLUSTER ANALYSIS IS NOT a summary of FINDINGS; it IS the analytical transformation that converts both domain LIFECYCLE EPOCH MAPs (including Arc Position columns) into a cross-domain structural-role-grounded defect-density surface. EPOCH-CLUSTER ANALYSIS IS BLOCKED until FINDINGS IS complete AND both LIFECYCLE EPOCH MAPs ARE present with complete Arc Position assignments (C12).**

**V-04 VARIATION — C-51/C-52 SYNERGY.** The cross-domain EPOCH-CLUSTER ANALYSIS extends beyond epoch-name concentration: it uses Arc Position structural roles as the cross-domain synthesis axis. The diagnostic insight: Finance APPROVAL `[Approval event]` and Sales ADVANCE `[Approval event]` occupy the same structural role in their respective arcs. A cross-domain synthesis that names epoch names only ("Finance APPROVAL and Sales ADVANCE cluster") IS C-52 PARTIAL. A synthesis that names the structural role boundary ("Finance Approval-event → Sales Entry-boundary IS the inter-domain handoff where the structural role transitions from commitment issuance to commitment intake — defects at this handoff ARE the signature of a gate that exists in Finance's arc but IS NOT yet present in Sales' arc") IS C-52/C-51 synergy-activated.

**Finding-to-epoch mapping (Arc Position column required, both domains):**

| Finding ID | Domain | Triggering O-ID | Lifecycle Epoch | Arc Position | Defect Type |
|------------|--------|-----------------|-----------------|--------------|-------------|
| F-[N] | Finance / Sales | O-F[N] / O-S[N] | [epoch from respective LIFECYCLE EPOCH MAP] | [Arc Position from respective LIFECYCLE EPOCH MAP] | [type] |

**Epoch defect counts by domain (with Arc Position):**

**Finance epochs:**
| Epoch | Arc Position | Defect Count | Finding IDs |
|-------|--------------|-------------|-------------|
| ORIGINATION | Entry boundary | [N] | [...] |
| REVIEW | Gate boundary | [N] | [...] |
| APPROVAL | Approval event | [N] | [...] |
| SETTLEMENT | Terminal settlement | [N] | [...] |

**Sales epochs:**
| Epoch | Arc Position | Defect Count | Finding IDs |
|-------|--------------|-------------|-------------|
| OPEN-TRACK | Entry boundary | [N] | [...] |
| QUALIFY | Gate boundary | [N] | [...] |
| ADVANCE | Approval event | [N] | [...] |
| CLOSE-TRACK | Terminal settlement | [N] | [...] |

**Highest-density epoch (cross-domain, with Arc Position):** [Epoch name] in [Finance/Sales] domain — [N] of [total] defects. Arc Position: [structural role].

**Cross-domain structural role concentration (C-51/C-52 synergy):** IS-NOT / IS contrast IS REQUIRED. [E.g., "The highest-defect-density position IS NOT Finance APPROVAL epoch by name; it IS the Approval event structural role, shared across both domain arcs. Finance carries [N] defects at its Approval event epoch; Sales carries [N] defects at its Approval event epoch ([N] total). This IS NOT a coincidence; it IS the signature of a gate that IS enforced in Finance's arc and IS NOT yet present in Sales' arc at the equivalent structural position."]

**Inter-domain handoff remediation implication (C-52/C-51 synergy form):** [Names the structural role boundary at the handoff, not only the epoch names. E.g., "The Finance Approval-event → Sales Entry-boundary handoff IS the defect concentration site (BRIDGE TABLE row F→S-[N]). Finance IS NOT defective at settlement; it IS defective at the approval gate it issues. Sales IS NOT defective mid-arc; it IS defective at the entry boundary where Finance's approval record IS consumed but NOT validated. The intervention IS NOT within either domain alone; it IS the approval-record validation check at the handoff boundary — the moment Finance transitions from Approval event to Terminal settlement IS the moment Sales IS authorized to leave Entry boundary. That transition IS NOT currently gated."]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: INERTIA BASELINE, DOMAIN DEPENDENCY DECLARATION, CONSTRAINT MATRIX, ROLES, Pass 1 (Finance: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION, INVARIANT-VIOLATION FORECAST, GATE A, TRANSITION TABLE, LIFECYCLE EPOCH MAP [with Arc Position column], FORECAST VALIDATION), BRIDGE TABLE, Pass 2 (Sales: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION, INVARIANT-VIOLATION FORECAST, GATE A, TRANSITION TABLE, LIFECYCLE EPOCH MAP [with Arc Position column], FORECAST VALIDATION), GATE B, INVALID TRANSITIONS (both passes), GATE C, RACE CONDITIONS, GATE D, FINDINGS, EPOCH-CLUSTER ANALYSIS.

---

## V-05 — Full Synthesis: Arc Position in All Three LIFECYCLE EPOCH MAPs + Three-Domain Structural Role EPOCH-CLUSTER (Finance → Sales → CS)

**Variation axis:** Full synthesis — C-51 Arc Position in all three domain LIFECYCLE EPOCH MAPs; three-domain EPOCH-CLUSTER ANALYSIS uses structural role vocabulary for inter-domain handoff remediation; C-51/C-52 synergy activated across both handoff boundaries
**Hypothesis:** Finance → Sales → CS three-pass multi-domain. R18 V-05 satisfies all multi-domain/multi-pass criteria (36 PASS). **C-51 addition:** All three LIFECYCLE EPOCH MAPs carry Arc Position columns. EPOCH-CLUSTER ANALYSIS updates: all three domain finding-to-epoch mappings carry Arc Position; cross-domain synthesis uses arc-position structural vocabulary for both inter-domain handoff remediation implications (Finance→Sales and Sales→CS boundary characterization uses structural role names, not only epoch names). Tests C-51/C-52 full synergy in three-domain format: does naming structural roles at BOTH handoff boundaries yield a qualitatively superior C-52 PASS? Predicted: 37 PASS = 92.2.
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

**Sales commitment state IS derived from Finance approval state.** Sales IS NOT independent; Sales IS the first downstream domain. A Sales opportunity IS NOT in Committed state unless the corresponding Finance invoice IS in Approved state. Sales IS ordered second because its valid states ARE constrained by Finance state resolution.

**CS entitlement state IS derived from Sales commitment state.** CS IS the second downstream domain. A CS support entitlement IS NOT in Active state unless the corresponding Sales opportunity IS in Committed or Closed-Won state. CS IS ordered third because its valid states ARE constrained by Sales state resolution, which IS itself constrained by Finance state resolution. The full dependency chain IS: Finance approval → Sales commitment → CS entitlement. Reversing any hop IS NOT merely reordered; it IS structurally incorrect.

**Arc Position cross-domain note:** The Arc Position structural role vocabulary (Entry boundary / Gate boundary / Approval event / Terminal settlement) IS the cross-domain comparison axis for EPOCH-CLUSTER ANALYSIS. Finance APPROVAL `[Approval event]` and Sales ADVANCE `[Approval event]` and CS RESOLUTION `[Terminal settlement]` each name a structural role in their respective domain arcs. The inter-domain handoff remediation implications in EPOCH-CLUSTER ANALYSIS WILL name both the source domain's Arc Position and the target domain's Arc Position at each handoff boundary — this IS the C-51/C-52 synergy mechanism for three-domain traces.

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
| C13 | All three LIFECYCLE EPOCH MAPs (Finance, Sales, CS) ARE REQUIRED to carry Arc Position columns (Entry boundary / Gate boundary / Approval event / Terminal settlement) on every epoch row. An epoch row without Arc Position assignment IS a C13 violation. EPOCH-CLUSTER ANALYSIS IS BLOCKED until all three maps carry complete Arc Position assignments. The cross-domain EPOCH-CLUSTER ANALYSIS remediation implications ARE REQUIRED to reference structural role vocabulary at BOTH inter-domain handoff boundaries (Finance→Sales and Sales→CS), naming the source domain's Arc Position AND the target domain's Arc Position at each boundary. A remediation that names only epoch names without structural role vocabulary at any handoff boundary IS a C13 synergy gap. | [T] | epoch structure / three-domain synergy |

---

### ROLES

**ROLES IS NOT an organizational chart; ROLES IS the execution authority matrix for this trace. A section without a named role assignment IS NOT shared ownership; it IS unowned obligation and IS the inertia baseline instantiated before any section IS produced. A role obligation that IS unassigned IS NOT deferred; it IS absent.**

**[D] Domain Expert**
Auto-selected: Finance expert (Pass 1) + Sales expert (Pass 2) + Customer Service expert (Pass 3) — [D] IS responsible for all three domain declarations. An incomplete domain declaration IS NOT a deferred section; it IS the inertia baseline chosen before that domain's trace begins.
Sections owned by [D]: All three domains' STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAMS, HANDOFF DECLARATIONS.
Binding constraint: **C4** (vocabulary IS FROZEN across all three domains after VOCABULARY CLOSED IS declared for each).

**[T] Trace Developer**
Sections owned by [T]: All three INVENTORY CHALLENGEs, all three INVARIANT-VIOLATION FORECASTs, BRIDGE TABLE F→S, BRIDGE TABLE S→CS, all three TRANSITION TABLEs, all three LIFECYCLE EPOCH MAPs (with Arc Position columns per C13), all three FORECAST VALIDATIONs, INVALID TRANSITIONS (all passes), RACE CONDITIONS, FINDINGS, EPOCH-CLUSTER ANALYSIS.
Authorization: [T] IS NOT AUTHORIZED to begin Pass 2 until Pass 1 IS complete AND BRIDGE TABLE F→S IS declared (C11). [T] IS NOT AUTHORIZED to begin Pass 3 until Pass 2 IS complete AND BRIDGE TABLE S→CS IS declared (C12). [T]'s authorization per pass IS CONTINGENT on the respective HANDOFF DECLARATION. [T] acknowledges: EPOCH-CLUSTER ANALYSIS WILL name structural roles at BOTH inter-domain handoff boundaries (C13).

---

### Pass 1: Finance Domain

**### Pass 1 — Finance [C-36: Finance-first ordering targets cross-domain commitment defects — FAILS if: Pass 2 begins without Finance approval state resolved] [C-37: unresolved Finance state IS the approval-chain failure that creates unauthorized Sales commitments AND unauthorized CS entitlements; Pass 1 IS NOT a preamble; it IS the dependency root] [C-42: Finance IS ordered first because Sales commitment preconditions ARE Finance-derived; the defect class targeted IS: downstream-commitment-without-upstream-approval]**

*(Finance domain sections: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION — same structure as V-04 Finance pass; domain: Draft / Submitted / Under-Review / Approved)*

*(INVENTORY CHALLENGE, GATE A-F, INVARIANT-VIOLATION FORECAST [T], GATE A: same structure as V-04; GATE A adds C13 acknowledgment for Finance LIFECYCLE EPOCH MAP)*

#### TRANSITION TABLE [T] — Finance (Pass 1)

*(standard table structure; Finance S-IDs and O-IDs; EPOCH: ORIGINATION / REVIEW / APPROVAL / SETTLEMENT)*

#### LIFECYCLE EPOCH MAP [T] — Finance (with Arc Position column)

**C13 REQUIREMENT.** Finance LIFECYCLE EPOCH MAP IS REQUIRED to carry Arc Position column. Arc Position assignments: ORIGINATION = Entry boundary; REVIEW = Gate boundary; APPROVAL = Approval event; SETTLEMENT = Terminal settlement.

| O-ID | Operation Name | Lifecycle Epoch | Epoch Rationale | Arc Position |
|------|----------------|-----------------|-----------------|--------------|
| O-F[N] | [from Finance OPERATION DECLARATIONS] | ORIGINATION / REVIEW / APPROVAL / SETTLEMENT | [rationale] | Entry boundary / Gate boundary / Approval event / Terminal settlement |
*(one row per Finance operation; Arc Position IS REQUIRED; blank IS a C13 violation)*

#### FORECAST VALIDATION [T] — Finance

*(standard)*

---

### BRIDGE TABLE F→S [T]

**BRIDGE TABLE F→S IS NOT an optional annotation; it IS the cross-domain precondition chain that makes Pass 2 Sales trace authorization conditional. Pass 2 IS BLOCKED until at least one Finance postcondition IS explicitly named as a Sales precondition (C11). C-47 confirmation annotations WILL cite BRIDGE TABLE F→S rows by name ("BRIDGE TABLE F→S row [N]") — unnamed chain references ARE NOT VALID for C-47 when a BRIDGE TABLE IS present.**

| Bridge Row | Finance Postcondition (Pass 1 Row #) | Finance State After | Bridge: Seeds Sales Precondition | Sales State Blocked Until |
|------------|--------------------------------------|---------------------|----------------------------------|---------------------------|
| F→S-[N] | [row #] | S-F[N] ([Finance State]) | Finance [field/state] IS REQUIRED before Sales O-[N] IS authorized | S-S[N] (IS NOT reachable until bridge condition IS met) |

---

### Pass 2: Sales Domain

**### Pass 2 — Sales [C-36: Sales-second ordering targets Finance-derived precondition defects — FAILS if: any Sales precondition IS asserted without a BRIDGE TABLE F→S row reference] [C-37: a Sales commitment without a Finance approval bridge row IS the revenue-commitment failure mode this artifact exists to prevent; proceeding without BRIDGE TABLE F→S IS NOT a shortcut; it IS the failure mode instantiated] [C-42: Sales IS ordered second because commitment preconditions ARE Finance-derived; the defect class targeted IS: Sales-commits-without-Finance-approval; BRIDGE TABLE F→S row IS the detection surface]**

*(Sales domain sections: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION — domain: Proposal / Negotiation / Committed / Closed-Won / Closed-Lost)*

*(INVENTORY CHALLENGE, GATE A-S, INVARIANT-VIOLATION FORECAST [T]: same structure; GATE A-S adds C13 acknowledgment for Sales LIFECYCLE EPOCH MAP)*

#### TRANSITION TABLE [T] — Sales (Pass 2)

*(standard; cross-domain C-41 annotations cite BRIDGE TABLE F→S rows by name)*

#### LIFECYCLE EPOCH MAP [T] — Sales (with Arc Position column)

**C13 REQUIREMENT.** Sales LIFECYCLE EPOCH MAP IS REQUIRED to carry Arc Position column. Arc Position assignments: OPEN-TRACK = Entry boundary; QUALIFY = Gate boundary; ADVANCE = Approval event; CLOSE-TRACK = Terminal settlement.

| O-ID | Operation Name | Lifecycle Epoch | Epoch Rationale | Arc Position |
|------|----------------|-----------------|-----------------|--------------|
| O-S[N] | [from Sales OPERATION DECLARATIONS] | OPEN-TRACK / QUALIFY / ADVANCE / CLOSE-TRACK | [rationale] | Entry boundary / Gate boundary / Approval event / Terminal settlement |
*(one row per Sales operation; Arc Position IS REQUIRED; blank IS a C13 violation)*

#### FORECAST VALIDATION [T] — Sales

*(standard)*

---

### BRIDGE TABLE S→CS [T]

**BRIDGE TABLE S→CS IS NOT an optional annotation; it IS the cross-domain precondition chain that makes Pass 3 CS trace authorization conditional. Pass 3 IS BLOCKED until at least one Sales postcondition IS explicitly named as a CS precondition (C12). This bridge IS the second hop in the Finance → Sales → CS dependency chain. C-47 confirmation annotations WILL cite BRIDGE TABLE S→CS rows by name ("BRIDGE TABLE S→CS row [N]").**

| Bridge Row | Sales Postcondition (Pass 2 Row #) | Sales State After | Bridge: Seeds CS Precondition | CS State Blocked Until |
|------------|-------------------------------------|-------------------|-------------------------------|------------------------|
| S→CS-[N] | [row #] | S-S[N] ([Sales State]) | Sales [field/state] IS REQUIRED before CS O-[N] IS authorized | S-CS[N] (IS NOT reachable until bridge condition IS met) |

---

### Pass 3: CS Domain

**### Pass 3 — CS (Customer Service) [C-36: CS-third ordering targets Sales-derived entitlement defects — FAILS if: any CS entitlement IS asserted without a BRIDGE TABLE S→CS row reference] [C-37: a CS entitlement without a Sales commitment bridge row IS the unauthorized-entitlement failure mode this artifact exists to prevent; proceeding without BRIDGE TABLE S→CS IS NOT a shortcut; it IS the failure mode instantiated] [C-42: CS IS ordered third because entitlement preconditions ARE Sales-derived, which ARE themselves Finance-derived; the defect class targeted IS: CS-entitlement-without-Sales-commitment; BRIDGE TABLE S→CS row IS the detection surface]**

*(CS domain sections: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION — domain: New / Assigned / In-Progress / Pending-Customer / Resolved / Closed)*

*(INVENTORY CHALLENGE, GATE A-CS, INVARIANT-VIOLATION FORECAST [T]: same structure; GATE A-CS adds C13 acknowledgment for CS LIFECYCLE EPOCH MAP)*

#### TRANSITION TABLE [T] — CS (Pass 3)

*(standard; cross-domain C-41 annotations cite BRIDGE TABLE S→CS rows by name)*

#### LIFECYCLE EPOCH MAP [T] — CS (with Arc Position column)

**C13 REQUIREMENT.** CS LIFECYCLE EPOCH MAP IS REQUIRED to carry Arc Position column. Arc Position assignments: INTAKE = Entry boundary; ACTIVE = Gate boundary; PENDING = Approval event; RESOLUTION = Terminal settlement.

| O-ID | Operation Name | Lifecycle Epoch | Epoch Rationale | Arc Position |
|------|----------------|-----------------|-----------------|--------------|
| O-CS[N] | [from CS OPERATION DECLARATIONS] | INTAKE / ACTIVE / PENDING / RESOLUTION | [rationale] | Entry boundary / Gate boundary / Approval event / Terminal settlement |
*(one row per CS operation; Arc Position IS REQUIRED; blank IS a C13 violation)*

#### FORECAST VALIDATION [T] — CS

*(standard; CS epochs)*

---

### GATE B, INVALID TRANSITIONS (all three passes), GATE C, RACE CONDITIONS

**GATE B IS NOT clearable until all three TRANSITION TABLEs ARE complete AND all three LIFECYCLE EPOCH MAPs ARE present with complete Arc Position columns (C13).**

*(standard blocking items; covers Finance, Sales, CS passes; cross-domain race scenarios: Finance approval and Sales commitment operations could interleave; if no concurrent access: explicit clearance with reason IS REQUIRED)*

---

### GATE D

**GATE D IS NOT clearable until all three LIFECYCLE EPOCH MAPs carry complete Arc Position assignments (C13). EPOCH-CLUSTER ANALYSIS IS BLOCKED until FINDINGS IS complete AND all three Arc Position assignments ARE present.**

*(standard blocking items; three-domain scope)*

---

### FINDINGS [T]

*(standard structure; findings may reference any of the three domain passes; cross-domain bridge defects ARE priority findings)*

**Cross-domain finding template:**
- **P[N]: [title]**
  Source: [Pass 1/2/3 row N / BRIDGE TABLE F→S row [N] / BRIDGE TABLE S→CS row [N]].
  Cross-domain dependency: [which bridge table and row surfaces the dependency; a cross-domain finding without a named bridge row reference IS NOT traceable].
  Inertia connection: [traces to INERTIA BASELINE failure mode].
  Disposition: [Status IS ACCEPTED / Action IS REQUIRED].
  Severity: FATAL / DEGRADED / COSMETIC.

**Per-pass defect (C-40):** At least one labeled defect IS REQUIRED per domain pass (Finance, Sales, CS). Three passes without defects IS NOT a finding; it IS an incomplete trace.

**Defect-hypothesis confirmation (C-47):** C-47 confirmations MUST cite: (1) the defect class from the C-42 pass heading annotation, AND (2) the named BRIDGE TABLE row by reference. Example for Pass 2: "CONFIRMS Sales-commits-without-Finance-approval defect class (C-42 prediction: Pass 2) — triggered by BRIDGE TABLE F→S row F→S-[N]." Example for Pass 3: "CONFIRMS CS-entitlement-without-Sales-commitment defect class (C-42 prediction: Pass 3) — triggered by BRIDGE TABLE S→CS row S→CS-[N]."

---

### EPOCH-CLUSTER ANALYSIS [T]

**EPOCH-CLUSTER ANALYSIS IS NOT a summary of FINDINGS; it IS the analytical transformation that converts all three domain LIFECYCLE EPOCH MAPs (with Arc Position columns) into a three-domain structural-role-grounded defect-density surface. EPOCH-CLUSTER ANALYSIS IS BLOCKED until FINDINGS IS complete AND all three LIFECYCLE EPOCH MAPs ARE present with complete Arc Position assignments (C13).**

**V-05 VARIATION — THREE-DOMAIN C-51/C-52 SYNERGY.** The three-domain cross-domain synthesis is the maximum-depth expression of C-51/C-52 synergy. The diagnostic value: Finance defects at its Approval event epoch, Sales defects at its Entry boundary epoch, and CS defects at its Terminal settlement epoch may each represent a different failure mode — or they may all be manifestations of the same gap in the Finance→Sales handoff, propagating downstream. The Arc Position vocabulary IS the instrument that distinguishes these cases without being confused by domain vocabulary differences.

**Finding-to-epoch mapping (Arc Position column required, all three domains):**

| Finding ID | Domain | Triggering O-ID | Lifecycle Epoch | Arc Position | Defect Type |
|------------|--------|-----------------|-----------------|--------------|-------------|
| F-[N] | Finance / Sales / CS | O-F/S/CS[N] | [epoch from respective LIFECYCLE EPOCH MAP] | [Arc Position from respective LIFECYCLE EPOCH MAP] | [type] |

**Epoch defect counts by domain (with Arc Position):**

**Finance epochs:**
| Epoch | Arc Position | Defect Count | Finding IDs |
|-------|--------------|-------------|-------------|
| ORIGINATION | Entry boundary | [N] | [...] |
| REVIEW | Gate boundary | [N] | [...] |
| APPROVAL | Approval event | [N] | [...] |
| SETTLEMENT | Terminal settlement | [N] | [...] |

**Sales epochs:**
| Epoch | Arc Position | Defect Count | Finding IDs |
|-------|--------------|-------------|-------------|
| OPEN-TRACK | Entry boundary | [N] | [...] |
| QUALIFY | Gate boundary | [N] | [...] |
| ADVANCE | Approval event | [N] | [...] |
| CLOSE-TRACK | Terminal settlement | [N] | [...] |

**CS epochs:**
| Epoch | Arc Position | Defect Count | Finding IDs |
|-------|--------------|-------------|-------------|
| INTAKE | Entry boundary | [N] | [...] |
| ACTIVE | Gate boundary | [N] | [...] |
| PENDING | Approval event | [N] | [...] |
| RESOLUTION | Terminal settlement | [N] | [...] |

**Highest-density epoch (three-domain cross-domain, with Arc Position):** [Epoch name] in [Finance/Sales/CS] domain — [N] of [total] defects. Arc Position: [structural role].

**Three-domain structural role concentration (C-51/C-52 synergy):** IS-NOT / IS contrast IS REQUIRED for both inter-domain handoff boundaries.

*Finance→Sales handoff characterization:* [Names source domain's Arc Position AND target domain's Arc Position at the Finance→Sales boundary. E.g., "Finance APPROVAL `[Approval event]` → Sales OPEN-TRACK `[Entry boundary]` IS the first inter-domain handoff. A Finance Approval event defect and a Sales Entry boundary defect at this handoff ARE NOT two independent defects; they ARE the same handoff gap expressed in two domain vocabularies: Finance IS NOT issuing a clean approval record (Approval event failure) AND Sales IS NOT validating the approval record at intake (Entry boundary failure). The C-51/C-52 synergy: naming both structural roles identifies the gap as a handoff contract failure, not a Finance-internal or Sales-internal defect."]

*Sales→CS handoff characterization:* [Names source domain's Arc Position AND target domain's Arc Position at the Sales→CS boundary. E.g., "Sales ADVANCE `[Approval event]` → CS INTAKE `[Entry boundary]` IS the second inter-domain handoff. A Sales Approval event defect and a CS Entry boundary defect at this handoff ARE NOT two independent defects; they ARE the same handoff gap: Sales IS NOT issuing a clean commitment record (Approval event failure) AND CS IS NOT validating the commitment at entitlement intake (Entry boundary failure)."]

**Three-domain remediation implication (C-52/C-51 synergy form):** [Highest-leverage intervention named by structural role at the inter-domain handoff boundary, not epoch names. Must span the dependency chain. E.g., "The highest-density defect concentration IS at the Finance Approval event epoch ([N] defects). This IS NOT a Finance APPROVAL epoch-name problem; it IS an Approval event structural-role problem in a dependency chain. The intervention IS at the Finance Approval event → Sales Entry boundary handoff (BRIDGE TABLE F→S row F→S-[N]): the approval record validation check that IS currently absent at the Sales entry boundary. Addressing this single check removes [N] Finance Approval event defects AND [N] Sales Entry boundary defects simultaneously, and eliminates the downstream precondition gap that propagates into the CS INTAKE epoch. The three-domain structural role vocabulary makes this visible; the three-domain epoch-name vocabulary alone would not."]

---

### ARTIFACT

Write to: `simulations/trace/state/{{topic}}-state-{{date}}.md`

Sections: INERTIA BASELINE, DOMAIN DEPENDENCY DECLARATION, CONSTRAINT MATRIX, ROLES, Pass 1 (Finance: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION, INVENTORY CHALLENGE, GATE A-F, INVARIANT-VIOLATION FORECAST, TRANSITION TABLE, LIFECYCLE EPOCH MAP [Arc Position column], FORECAST VALIDATION), BRIDGE TABLE F→S, Pass 2 (Sales: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION, INVENTORY CHALLENGE, GATE A-S, INVARIANT-VIOLATION FORECAST, TRANSITION TABLE, LIFECYCLE EPOCH MAP [Arc Position column], FORECAST VALIDATION), BRIDGE TABLE S→CS, Pass 3 (CS: STATE DECLARATIONS, OPERATION DECLARATIONS, INVARIANT DECLARATIONS, VOCABULARY CLOSED, STATE DIAGRAM, HANDOFF DECLARATION, INVENTORY CHALLENGE, GATE A-CS, INVARIANT-VIOLATION FORECAST, TRANSITION TABLE, LIFECYCLE EPOCH MAP [Arc Position column], FORECAST VALIDATION), GATE B, INVALID TRANSITIONS (all passes), GATE C, RACE CONDITIONS, GATE D, FINDINGS, EPOCH-CLUSTER ANALYSIS.
