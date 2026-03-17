# flow-lifecycle -- Round 17 Variations (Rubric v17)

**Rubric**: v17 · 53 criteria (45 aspirational) · Ceiling entering R17: 45/45
(R16 V-05 achieved 45/45 retroactive score under v17; C-51/C-52/C-53 signals implicitly present
via per-direction violation check in Phase->Baseline, PHASE GATE CONTRACT SUMMARY Phase Refs:
instruction prose, and "see architecture above" IM Ref hint anchor.)

**Open criteria entering R17**: C-51, C-52, C-53 -- all three implicitly triggered by R16 V-05
but never promoted to explicit named structural sub-fields in their canonical locations. R17
escalates all three to explicit named instructions: VIOLATION CHECK per direction in DIRECTION
INVENTORY (C-51), `Return instruction:` labeled field in PHASE GATE CONTRACT SUMMARY (C-52),
named architecture back-reference in `IM Ref:` hint (C-53).

**Evidence from R16 excellence (C-51, C-52, C-53):**

- **C-51 signal**: R16 V-05 Phase->Baseline direction in CHAIN STATUS carried an explicit
  consistency violation check: "an IM-ID cited by at least one PHASE ENTRY CONTRACT but carrying
  NONE in `Phase Refs:` is a C-48 consistency violation." This named source field, target field,
  and inconsistency pattern -- the structure C-51 requires -- but only for one direction and
  only in the CHAIN STATUS body, not as a per-direction sub-field of the DIRECTION INVENTORY.
  R17 C-51 promotes this to all PRESENT directions in the DIRECTION INVENTORY.

- **C-52 signal**: R16 V-05 PHASE GATE CONTRACT SUMMARY stated "After all phases are traced,
  INCUMBENT BASELINE `Phase Refs:` back-references close the Baseline->Phase direction
  bidirectionally." This names target table, target sub-field, and trigger condition -- the
  minimum C-52 content -- but as prose inside the orthogonality note, not as a dedicated named
  `Return instruction:` sub-field. R17 C-52 promotes this to a labeled instruction element.

- **C-53 signal**: R16 V-05 `IM Ref:` EX block hint ended with "Namespace: IM-ID (see
  architecture above)." The phrase "architecture" refers to the EXCEPTION BLOCK ARCHITECTURE
  header but by abbreviated label. C-53 requires the full declaration name "EXCEPTION BLOCK
  ARCHITECTURE" to appear in the hint, making the back-reference unambiguously anchored.
  R17 C-53 promotes this to the explicit full name.

**New criteria targeted in R17:**

**C-51 target (V-03, V-05)**: Expand DIRECTION INVENTORY from 3-column to 4-column by adding a
`Violation Check` column. Each PRESENT direction carries a declarative string-comparison condition
naming (a) the source field, (b) the target field, and (c) the exact inconsistency pattern that
would reopen the gate. CHAIN STATUS remains CLOSED only when all violation checks evaluate to
no-conflict. Directions declared NOT-APPLICABLE are exempt.

**C-52 target (V-02, V-05)**: Add an explicit `Return instruction:` labeled sub-field to PHASE
GATE CONTRACT SUMMARY, positioned after the three-field table and orthogonality declaration.
The field names the target table (INCUMBENT BASELINE), the target sub-field (`Phase Refs:`),
and the trigger condition (all PHASE ENTRY CONTRACT blocks authored).

**C-53 target (V-04, V-05)**: Change the `IM Ref:` hint in each EX block template from
"(see architecture above)" to "(see EXCEPTION BLOCK ARCHITECTURE above)" -- using the full
declaration name to make the back-reference traceable to the named block by document position.

**Variation matrix:**

| Variation | Axes | C-51 Violation Checks | C-52 Return Instruction | C-53 Named Back-Ref | Primary hypothesis |
|-----------|------|:---------------------:|:-----------------------:|:-------------------:|-------------------|
| V-01 | Role sequence | NO (implicit) | NO (implicit) | NO (implicit) | R16 V-05 implicit structure -- tests whether retroactive C-51/C-52/C-53 pass holds on fresh topic; establishes R17 floor |
| V-02 | Output format | NO (implicit) | YES (named `Return instruction:`) | NO (implicit) | Explicit Return instruction in PHASE GATE CONTRACT SUMMARY scores C-52 independently |
| V-03 | Lifecycle emphasis | YES (4-column DIRECTION INVENTORY) | NO (implicit) | NO (implicit) | Explicit per-direction violation checks in DIRECTION INVENTORY scores C-51 independently |
| V-04 | Phrasing register | NO (implicit) | NO (implicit) | YES (full name anchor) | Explicit "EXCEPTION BLOCK ARCHITECTURE" name in IM Ref hint scores C-53 independently |
| V-05 | Output format + Lifecycle emphasis + Phrasing register | YES | YES | YES | Maximum density -- all three compose; 45/45 = 10.000 |

**Structural change summary vs R16 V-05:**

| Section | R16 V-05 had | V-01 (unchanged) | V-02 adds | V-03 adds | V-04 adds | V-05 combines |
|---------|-------------|-----------------|----------|----------|----------|--------------|
| PHASE GATE CONTRACT SUMMARY | Prose mention of Phase Refs: after-tracing | Same | `Return instruction:` named field | -- | -- | `Return instruction:` named field |
| DIRECTION INVENTORY | 3-column (Direction / Status / Carried By) | Same | -- | 4-column (+ Violation Check) | -- | 4-column (+ Violation Check) |
| EX block `IM Ref:` hint | "see architecture above" | Same | -- | -- | "see EXCEPTION BLOCK ARCHITECTURE above" | "see EXCEPTION BLOCK ARCHITECTURE above" |

---

## V-01 -- Axis: Role Sequence (Full R16 V-05 Structure, Baseline)

**Variation axis**: Role sequence -- default domain-natural role ordering (Sales/Procurement/
Finance/Operations sequence determined by process type). Full R16 V-05 structure intact with all
C-48, C-49, C-50 explicit elements: `Phase Refs:` per IM-ID in INCUMBENT BASELINE, EXCEPTION
BLOCK ARCHITECTURE header in SECTION A, DIRECTION INVENTORY block at CHAIN STATUS opening.
C-51 violation checks not explicitly added to DIRECTION INVENTORY. C-52 Return instruction
not added as named field. C-53 IM Ref hint uses "see architecture above" (partial name).

**Hypothesis**: R16 V-05 structure retroactively scored 45/45 under v17 because: (1) the
Phase->Baseline CHAIN STATUS entry carried an explicit violation check naming source, target,
and inconsistency pattern (implicit C-51); (2) PHASE GATE CONTRACT SUMMARY mentioned Phase Refs:
annotation as an after-tracing step (implicit C-52); (3) "see architecture above" in IM Ref hint
references the EXCEPTION BLOCK ARCHITECTURE declaration by abbreviated name (implicit C-53). V-01
tests whether these implicit structures produce reliable compliance on a fresh topic run. If V-01
scores 45/45, single-axis variations confirm zero-regression tolerance. If V-01 scores 42/45,
single-axis variations isolate which explicit additions are necessary. Expected: 42/45 or 45/45.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must satisfy both Dual-Cite
> Fail Conditions. Quantified metric must appear before PHASE 1 in document order.
> This section is the inertia reference: IM-IDs assigned here are anchor identifiers for
> (1) `IM Reference:` in every PHASE ENTRY CONTRACT, (2) `IM Ref:` in every SECTION A EX block,
> and (3) `Phase Refs:` back-references declared at the end of this section after all PHASE ENTRY
> CONTRACT blocks are complete. Every exception trace and bottleneck must be traceable back to a
> named IM-ID. The `Phase Refs:` back-references close the Baseline->Phase direction (C-46)
> bidirectionally at the source-row level.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle -- auto-detect from {Topic}]

**Incumbent description**: [1-3 sentences: tools used (spreadsheets, email, phone), handoff
mechanisms, where records are stored, who initiates the process manually. Include the primary
failure point under volume or time pressure.]

**Incumbent failure modes**:

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure -- the one most visible to the domain team] | [daily / per-cycle / per-exception] | [downstream effect on SLA or accuracy] |
| IM-02 | [second distinct failure mode -- different process layer from IM-01] | [frequency] | [downstream effect] |

**Cost of no action**: [Named measure with current-state value or rate, declared before PHASE 1.
Both IM-IDs must be reachable from at least one B-NN Cause field. Example: "Average credit
approval cycle time: 5.8 days vs 3-day SLA -- IM-01 primary driver" or "Manual matching error
rate: 12% per period, IM-02 primary driver."]

**Phase back-references (C-48 -- closes Baseline->Phase bidirectionally at source):**

> After completing all PHASE ENTRY CONTRACT blocks, return here to populate the back-references
> for each IM-ID. Each IM-ID lists every PHASE ENTRY CONTRACT whose `IM Reference:` sub-field
> cites this IM-ID. Enumeration must be consistent with all `IM Reference:` sub-fields by string
> comparison: if a PHASE ENTRY CONTRACT `IM Reference:` cites IM-01, then IM-01 `Phase Refs:`
> must list that phase's literal identifier; if it does not cite IM-01, `Phase Refs:` must not
> list it. IM-IDs with no phase citations carry explicit NONE sentinel. String comparison only --
> no inference. These back-references make each IM-ID row a navigable lookup for Baseline->Phase
> traceability, complementing the `IM Reference:` sub-fields in PHASE ENTRY CONTRACT blocks.
> CHAIN STATUS `Phase->Baseline` direction verifies consistency.

- IM-01 Phase Refs: [List every PHASE ENTRY CONTRACT by literal phase block identifier whose
  `IM Reference:` sub-field cites IM-01 (e.g., "PHASE 1 -- Initiation; PHASE 3 -- Approval").
  If no PHASE ENTRY CONTRACT `IM Reference:` cites IM-01, write NONE. String comparison only.]
- IM-02 Phase Refs: [List every PHASE ENTRY CONTRACT whose `IM Reference:` cites IM-02, or NONE.
  Same rules as IM-01 above.]

---

### Role Registry Gate

> GATE BLOCK: Complete before the Role Sequence Schedule and before tracing any state.
> All four anti-generic checks must clear before proceeding.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [domain-specific role] | [named responsibility] |
| R-02 | [domain-specific role] | [named responsibility] |
| R-03 | [domain-specific role] | [named responsibility] |

Anti-generic validation (all four must clear before proceeding):
- [ ] No R-ID entry uses "Approver" without a domain qualifier
- [ ] No R-ID entry uses "Owner" without a named responsibility
- [ ] Each R-ID is referenced by at least one Decision Supplement block, the Role Sequence
      Schedule, and at least one PHASE EXIT GATE Exit verification or Blocked bottleneck field
- [ ] Each declared R-ID appears in at least one EX block's `Role Ref:` sub-field -- R-IDs
      with no observable EX trace are "dark" roles and constitute a gate violation

Role set by process type:
- L2O --> Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P --> Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close --> Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle --> Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Role Sequence Schedule

> Declared after Role Registry Gate and before PHASE 1. Maps each R-ID to owned phases with
> activation triggers, handoff triggers, and parallel windows. B-NN Cause fields must cite
> the blocking R-ID from this schedule (Dual-Cite Fail Condition B). R-IDs in EX block
> `Role Ref:` must match the schedule entry for the enclosing phase. Every declared R-ID
> must appear in at least one EX block Role Ref -- the Role Registry Gate fourth check enforces this.

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior-process artifact -- not "Start"] | [specific completion condition] | R-[ID] or NONE | [concurrent window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1 -- name the artifact] | [completion condition] | R-[ID] or NONE | [concurrent activity or NONE] |

Rules: Every phase has a Primary Owner. Activation Trigger for Phase 1 must name an external
event or prior-process artifact. Every R-ID here must match a Role Registry Gate entry.

---

### Phase Gate Contract Summary

> **DECLARED UNIT: THREE-FIELD PHASE GATE CONTRACT**
>
> This document uses a three-field phase gate contract. All three fields are named here as a
> declared unit before PHASE 1 is traced. Every phase block must carry all three fields in
> their designated structural locations. A fourth field (`IM Reference:`) augments PHASE ENTRY
> CONTRACTs with Baseline->Phase traceability; it is not part of the three-field gate contract
> but is required in every PHASE ENTRY CONTRACT block. After all phases are traced, INCUMBENT
> BASELINE `Phase Refs:` back-references close the Baseline->Phase direction bidirectionally.
>
> | Field Name | Location | Value Type | Traceability Direction |
> |------------|----------|------------|----------------------|
> | `Prior phase:` | PHASE ENTRY CONTRACT | Phase label (e.g., "PHASE 1 -- Initiation") | Phase->Phase, backward (entry side) |
> | `Prior phase blocked bottleneck:` | PHASE ENTRY CONTRACT | B-ID (e.g., "B-01") | B-NN boundary continuity, entry side |
> | `Next phase:` | PHASE EXIT GATE | Phase label (e.g., "PHASE 2 -- Credit Review") | Phase->Phase, forward (exit side) |
>
> **ORTHOGONALITY DECLARATION:**
> `Prior phase blocked bottleneck:` carries a B-ID (string pattern: "B-" followed by digits,
> e.g., "B-01"). `Next phase:` carries a Phase label (string pattern: "PHASE N -- [Name]" or
> NONE/END sentinel). These two fields carry orthogonal value types independently verifiable
> by string comparison. No inference required -- patterns are non-overlapping by construction.
>
> `Prior phase:` and `Next phase:` form a symmetric bidirectional Phase->Phase pair.
> `Prior phase blocked bottleneck:` is orthogonal to both -- B-ID, not Phase label.
>
> CHAIN STATUS verifies three gate-contract directions:
> - `Phase-sequence`: every `Prior phase:` string-matches the preceding phase block label
> - `Phase-exit-sequence`: every `Next phase:` string-matches the subsequent phase block label
> - `Phase-boundary B-NN continuity`: every exit gate `Blocked bottleneck:` B-ID string-matches
>   the next phase's `Prior phase blocked bottleneck:` field

---

### Phase Structure

For each phase in the lifecycle, produce the following five blocks in document order. All three
Phase Gate Contract fields must be populated in every phase block. `IM Reference:` must
additionally appear in every PHASE ENTRY CONTRACT. After all phases are complete, return to
INCUMBENT BASELINE to populate `Phase Refs:` back-references.

---

**PHASE [N] -- [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Phase Gate Contract fields 1 and 2 live here; field 3 (`Next phase:`) lives in PHASE EXIT GATE.
> `IM Reference:` is a fourth required sub-field providing Baseline->Phase traceability. Its
> content will be cross-referenced by INCUMBENT BASELINE `Phase Refs:` back-references -- populate
> accurately so the bidirectional chain is consistent by string comparison. All four sub-fields
> are independently verifiable by string comparison.

- Entry Condition: [specific named artifact from prior phase's Required outputs]
- Pre-condition check: R-[ID] ([role name -- must match Role Sequence Schedule primary owner]) -- [verification method]
- Blocking condition: [state entered and role notified if entry condition not met]
- Prior phase: [Literal identifier of preceding phase block, e.g., "PHASE 1 -- Initiation".
  Phase 1: NONE or INIT sentinel. Must string-match preceding phase block label. Format: "PHASE N -- [Name]".]
- Prior phase blocked bottleneck: [B-ID from prior exit gate `Blocked bottleneck:` or NONE
  or N/A for Phase 1. Format: "B-NN". Must string-match prior exit gate AND B-NN block identifier.
  This field carries a B-ID -- NOT a Phase label. Do not conflate with `Prior phase:`.]
- IM Reference: [List every IM-ID from INCUMBENT BASELINE whose failure mode represents an
  active risk entering this phase. Use exact IM-ID identifiers as declared in the INCUMBENT
  BASELINE table (e.g., "IM-01, IM-02"). If no incumbent failure mode is an active risk at
  this phase's entry point, write NONE. IM-IDs must literal-match INCUMBENT BASELINE table
  identifiers -- string comparison only, no inference. INCUMBENT BASELINE `Phase Refs:` for
  each cited IM-ID will list this phase's literal identifier -- ensure phase block label is
  consistent with `Phase Refs:` entries. Example: "IM-01 (manual reconciliation gap -- active
  entry risk: pre-condition artifact produced manually and vulnerable to IM-01 failure mode
  before this phase begins)."]

**SECTION A -- EXCEPTION TRACES**

> **EXCEPTION BLOCK ARCHITECTURE:**
> Each EX block in this document carries three independent citation sub-fields, declared here
> as a named unit. All three sub-fields must appear in every EX block across all phases.
> Missing any sub-field in any EX block is a detectable format violation verifiable from this
> declaration without per-block traversal.
>
> | Sub-field | Namespace | ID Pattern | Traceability Direction |
> |-----------|-----------|------------|----------------------|
> | `Role Ref:` | R-ID namespace | "R-" followed by digits (e.g., "R-01") | Role->Exception (C-40): cites the phase's ROLE SEQUENCE SCHEDULE primary owner |
> | `Bottleneck Ref:` | B-ID namespace | "B-" followed by digits (e.g., "B-01") | B-NN->Exception (C-42): cites the bottleneck that enabled this exception |
> | `IM Ref:` | IM-ID namespace | "IM-" followed by digits (e.g., "IM-01") | Baseline->Exception (C-47): cites the INCUMBENT BASELINE failure mode this exception traces |
>
> **ORTHOGONALITY DECLARATION:** The three ID namespaces are distinct and independently
> verifiable by string comparison. "R-[digits]", "B-[digits]", and "IM-[digits]" are
> non-overlapping string patterns by construction: no R-ID can be mistaken for a B-ID or
> IM-ID; no B-ID can be mistaken for an R-ID or IM-ID; no IM-ID can be mistaken for an
> R-ID or B-ID. The three citation directions are orthogonal: an R-ID in `Bottleneck Ref:`
> is a detectable format violation; a B-ID in `IM Ref:` is a detectable format violation.
> EX block completeness is format-verifiable from this declaration without per-block traversal.

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] -- [Exception Name]**
> - Trigger: [specific condition -- name the state, threshold breach, or missing input]
> - Trace: [path of states from trigger to resolution or terminal; cite S-IDs in sequence]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason this failure mode matters]
> - Bottleneck Ref: [B-NN that enabled this exception, or NONE. B-ID must string-match a
>   Bottleneck Analysis identifier. The B-NN block's `Exception Refs:` field must list this
>   EX block ID if Bottleneck Ref is non-NONE -- populate accurately for chain consistency.
>   NONE only if no declared bottleneck was causal. Namespace: B-ID (see architecture above).]
> - Role Ref: [R-ID of the ROLE SEQUENCE SCHEDULE primary owner for this phase. Literal R-ID
>   matching the schedule's Primary Owner entry for the enclosing phase. Free-text without
>   R-ID fails. Namespace: R-ID (see architecture above).]
> - IM Ref: [IM-ID from INCUMBENT BASELINE whose failure mode this exception traces, or NONE.
>   Use exact IM-ID identifier as declared in the INCUMBENT BASELINE table (e.g., "IM-01").
>   This sub-field completes the triple-citation architecture: `Role Ref:` links to schedule
>   (C-40); `Bottleneck Ref:` links to B-NN (C-42); `IM Ref:` links to INCUMBENT BASELINE
>   (C-47). Together they make this EX block the convergence point for Role->Exception,
>   B-NN<->Exception, and Baseline<->Exception traceability chains simultaneously.
>   NONE if no incumbent baseline failure mode is directly traceable to this exception.
>   String comparison only -- IM-ID must literal-match INCUMBENT BASELINE table identifier.
>   Namespace: IM-ID (see architecture above).
>   Example: "IM-01 -- this exception is the process-visible manifestation of the incumbent
>   manual reconciliation failure mode entering Phase 2."]

Minimum 1 exception trace per phase; 3 total minimum.
Every declared R-ID in the Role Registry Gate must appear in at least one EX block Role Ref.
Role Ref, Bottleneck Ref, and IM Ref are independent sub-fields; populate all three for every EX block.

**SECTION B -- STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules:
- Every state must have a named Entry Condition. "Ready" or "Previous step complete" fails.
- Every Exit must reference a destination S-ID or carry the label TERMINAL.
- Type values: NORMAL / DECISION / PARALLEL-FORK / PARALLEL-JOIN / EXCEPTION / TERMINAL

**Decision Supplement Blocks** (one per DECISION-type state in this phase):

> **DS-[S-ID] -- [State Name]**
> - Condition: [rule or threshold evaluated]; Owner: R-[ID]; Branch A: --> S-[ID];
>   Branch B: --> S-[ID] or TERMINAL; Fallback: [action if condition cannot be evaluated]

**PHASE EXIT GATE**

> Phase Gate Contract field 3 lives here: `Next phase:` (Phase label, forward).
> `Blocked bottleneck:` carries a B-ID. These two sub-fields are orthogonal -- see PHASE GATE
> CONTRACT SUMMARY above.

- Exit Condition: [what the phase must produce to be complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name -- must match Role Sequence Schedule primary owner]) confirms all outputs present
- Blocking condition: [re-entry path or escalation if outputs absent]
- Blocked bottleneck: [B-NN or NONE. Must string-match Bottleneck Analysis identifier AND
  next phase's `Prior phase blocked bottleneck:`. Format: "B-NN" -- a B-ID, not a Phase label.]
- Next phase: [Literal identifier of the subsequent phase block. Last phase: NONE or END.
  Format: "PHASE N -- [Name]". This field carries a Phase label -- not a B-ID. See PHASE GATE
  CONTRACT SUMMARY orthogonality declaration.]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID] ([state name])
- **Branch 1**: [states traversed; cite S-IDs in sequence]
- **Branch 2**: [states traversed; cite S-IDs in sequence]
- **JOIN at**: S-[ID] ([join state name])
- **Join Condition**: AND-join / OR-join -- specify which applies and explain why

---

### Edge Case Enumeration

At least three edge cases distinct from SECTION A exception flows:

> **EC-[N] -- [Edge Case Name]**
> - Triggering Condition: [specific scenario]
> - Why Problematic: [specific reason this falls outside documented handling]
> - Correct Response: R-[ID] ([role name]) -- [specific correct action; name target state or resolution path]

---

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF -- {Topic} lifecycle --> [adjacent process name]**
> - Sending State: S-[ID] / Receiving Process: [name] / Data Payload: [named fields]
> - Expected Acknowledgment: [signal or confirmation] / Failure Mode: [if acknowledgment not received]
> - Owner: R-[ID]

---

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|
| | | | | AT-RISK / ON-TRACK | B-NN (if AT-RISK) |

Rules: AT-RISK = typical duration exceeds SLA target. Every AT-RISK row must carry a Bottleneck
Ref citing a B-NN from Bottleneck Analysis. Minimum 3 annotated rows; at least 1 must be AT-RISK.

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN Cause field must satisfy both Dual-Cite Fail Conditions independently.
>
> **Dual-Cite Fail Condition A** -- Cause field contains no IM-ID literal string (e.g., "IM-01"):
> fails C-39. Verify: search Cause field for "IM-" followed by digits. Absence --> fail.
>
> **Dual-Cite Fail Condition B** -- Cause field contains no R-ID literal string (e.g., "R-01"):
> fails C-39. Verify: search Cause field for "R-" followed by digits. Absence --> fail.
>
> B-IDs assigned here must string-match ALL of: (1) PHASE EXIT GATE `Blocked bottleneck:`
> fields, (2) PHASE ENTRY CONTRACT `Prior phase blocked bottleneck:` in the following phase,
> and (3) EX block `Bottleneck Ref:` fields where non-NONE.
>
> Concrete format example for Evidence field:
> `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`
>
> Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
> Fail condition: A field containing only "see SLA ANALYSIS" or state names without
> AT-RISK row-level S-ID specificity does not satisfy.
>
> **DUAL-LOCATION REQUIREMENTS:**
> (1) Concrete named domain example must appear in BOTH this preamble AND each B-NN per-block
> Evidence hint.
> (2) Labeled axes (`Required format:` / `Fail condition:`) must appear in BOTH this preamble
> AND each B-NN per-block Evidence hint.
>
> **B-NN->Exception Gate Check**: Every declared B-ID below must appear in at least one EX
> block's `Bottleneck Ref:` sub-field across all phases. A B-ID absent from all EX blocks is
> a "dark bottleneck" -- declared failure mode with no exception-phase trace. Dark bottlenecks
> are gate violations. Report result in CHAIN STATUS `B-NN->Exception` direction.
>
> Anti-embedding: Declare CHAIN STATUS in its own dedicated top-level section after SLA ANALYSIS.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field AND an Exception Refs field.**

---

**B-01 -- [Bottleneck Name]**

- Cause: [Required: IM-ID literal string (Condition A) AND R-ID literal string (Condition B).
  Example: "IM-01 (manual reconciliation gap) combined with R-02 (GL Manager) period-close
  unavailability -- approval queue at S-05. 'IM-01' satisfies A; 'R-02' satisfies B."]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string --> fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string --> fails C-39
- Impact: [downstream state, SLA node, or adjacent process affected]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-01. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]
- Exception Refs:
  - Required format: `EX-[Phase#][Letter] (Phase [N] -- [Exception Name])`
  - Fail condition: NONE declared here means this is a dark bottleneck -- declared process
    failure mode with no exception-phase trace. Dark bottleneck = gate violation for the
    B-NN->Exception direction. A listed EX block ID that has no matching `Bottleneck Ref:
    B-01` in the cited EX block fails the CHAIN STATUS B-NN->Exception consistency check.
  - [List each EX block identifier whose `Bottleneck Ref:` cites B-01, or NONE.]

---

**B-02 -- [Bottleneck Name]**

- Cause: [Required: IM-ID literal string AND R-ID literal string.]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string --> fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string --> fails C-39
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: [same as B-01]
  - [List each AT-RISK SLA row citing B-02. Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]
- Exception Refs:
  - Required format: `EX-[Phase#][Letter] (Phase [N] -- [Exception Name])`
  - Fail condition: NONE = dark bottleneck (gate violation). Listed EX block ID without
    matching `Bottleneck Ref: B-02` in the cited EX block fails consistency check.
  - [List each EX block identifier whose `Bottleneck Ref:` cites B-02, or NONE.]

---

**Gap Identification**

> MISSING: [step name] -- [rationale: why it belongs; failure mode enabled; which phase;
> which IM-ID it would reduce if present]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

**DIRECTION INVENTORY:**

> The four established traceability directions are enumerated below as a named index declared
> before the direction-level verification entries. Each direction is declared PRESENT or ABSENT
> with a citation to the section or sub-field carrying it. Completeness of chain coverage is
> format-verifiable from this inventory by string comparison alone, without traversing the full
> document. A direction declared NOT-APPLICABLE must carry an explicit rationale. An absent
> DIRECTION INVENTORY block is a FAIL regardless of direction content below. A DIRECTION
> INVENTORY missing any of the four established directions is a FAIL.

| Direction | Status | Carried By |
|-----------|--------|-----------|
| B-NN->Exception | [PRESENT / ABSENT] | [B-NN block `Exception Refs:` field listing EX block IDs; EX block `Bottleneck Ref:` field citing B-ID; verified in CHAIN STATUS `B-NN->Exception` direction below] |
| Phase-exit-sequence | [PRESENT / ABSENT] | [PHASE EXIT GATE `Next phase:` sub-field; string-match to subsequent phase block label; verified in CHAIN STATUS `Phase-exit-sequence` direction below] |
| Baseline->Phase | [PRESENT / ABSENT] | [PHASE ENTRY CONTRACT `IM Reference:` sub-field; string-match to INCUMBENT BASELINE IM-IDs; back-referenced by INCUMBENT BASELINE `Phase Refs:` annotations; verified in CHAIN STATUS `Baseline->Phase` direction below] |
| Baseline->Exception | [PRESENT / ABSENT] | [SECTION A EX block `IM Ref:` sub-field; string-match to INCUMBENT BASELINE IM-IDs; verified in CHAIN STATUS `Baseline->Exception` direction below] |

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA->B): [every AT-RISK SLA row cites a B-ID; enumerate pairs or name gap]
- Backward (B->SLA): [every B-NN Evidence field lists AT-RISK SLA rows; enumerate or name gap]
- Exit gate consistency: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID matches a declared B-NN; name any mismatch]
- Phase-boundary B-NN continuity: [every exit gate B-ID matches next phase's `Prior phase blocked bottleneck:`; list pairs or name break]
- Phase-sequence: [every PHASE ENTRY CONTRACT `Prior phase:` matches preceding phase block label; PHASE 1 carries NONE/INIT; list pairs or name mismatch]
- Phase-exit-sequence: [every PHASE EXIT GATE `Next phase:` matches subsequent phase block label; last phase carries NONE/END; list pairs or name mismatch -- DIRECTION INVENTORY declares PRESENT]
- Exception->B: [every EX block `Bottleneck Ref:` B-ID (non-NONE) matches a declared B-NN; list EX->B-NN pairs or name unresolved block]
- B-NN->Exception: [every declared B-ID has at least one non-NONE entry in its `Exception Refs:` field; each listed EX block ID string-matches an EX block with `Bottleneck Ref:` citing this B-ID; enumerate B-ID->EX pairs; name any B-ID with NONE in Exception Refs (dark bottleneck) or any listed ID whose EX block does not carry matching Bottleneck Ref (consistency failure) -- DIRECTION INVENTORY declares PRESENT]
- Exception->Role: [every EX block `Role Ref:` R-ID matches ROLE SEQUENCE SCHEDULE primary owner; list EX->R-ID pairs or name mismatch]
- Role->Exception: [every declared R-ID appears in at least one EX block `Role Ref:`; list R-ID->EX pairs; name dark roles]
- Dual-cite status: [every B-NN Cause has both IM-ID and R-ID; name any block missing either]
- Baseline->Phase: [every PHASE ENTRY CONTRACT `IM Reference:` field contains only IM-IDs declared in INCUMBENT BASELINE; list phase->IM-ID pairs; phases with NONE sentinel are CLOSED for this direction; name any phase whose IM Reference contains a non-declared IM-ID or is absent -- DIRECTION INVENTORY declares PRESENT]
- Baseline->Exception: [every SECTION A EX block `IM Ref:` field contains only IM-IDs declared in INCUMBENT BASELINE or NONE sentinel; list EX->IM-ID pairs; name any EX block whose IM Ref contains a non-declared IM-ID or is absent (dark exception); EX blocks with NONE sentinel are CLOSED -- DIRECTION INVENTORY declares PRESENT]
- Phase->Baseline: [bidirectional complement to Baseline->Phase; for each IM-ID cited in any
  PHASE ENTRY CONTRACT `IM Reference:` field, verify INCUMBENT BASELINE `Phase Refs:` for that
  IM-ID includes this phase by literal phase block identifier; enumerate IM-ID->Phase Refs pairs;
  name any phase whose `IM Reference:` cites an IM-ID whose `Phase Refs:` does not list that
  phase (consistency failure); verify all NONE sentinels are accurate -- an IM-ID with NONE in
  `Phase Refs:` must not be cited by any PHASE ENTRY CONTRACT `IM Reference:` field; an IM-ID
  cited by at least one PHASE ENTRY CONTRACT but carrying NONE in `Phase Refs:` is a C-48
  consistency violation that reopens the gate]
- Gap (if OPEN): [unresolved direction and unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal name] | SUCCESS | [branch or state that reaches it] |
| [failure terminal name] | FAILURE | [branch or state that reaches it] |
| [cancel terminal name] | CANCEL | [branch or state that reaches it] |

> Completeness check: Every exit branch in every SECTION B state table must reach one of the
> declared terminals. No branch may end at a non-terminal state without `continues-via: S-[ID]`.

---
---

## V-02 -- Axis: Output Format (PHASE GATE CONTRACT SUMMARY Return Instruction, C-52 Target)

**Variation axis**: Output format -- an explicit `Return instruction:` labeled sub-field is added
to PHASE GATE CONTRACT SUMMARY immediately after the orthogonality declaration. The field names the
target table (INCUMBENT BASELINE), the target sub-field (`Phase Refs:`), and the trigger condition
(all PHASE ENTRY CONTRACT blocks authored). This converts the C-48 back-annotation workflow step
from prose embedded inside the orthogonality note into a dedicated, positionally verifiable
named instruction. Parallel to how EXCEPTION BLOCK ARCHITECTURE made EX block field requirements
format-verifiable from the preamble: PHASE GATE CONTRACT SUMMARY now makes the Phase Refs:
back-annotation workflow step format-verifiable from the phase gate section.

**Hypothesis**: C-52 requires "a named `Return instruction:` sub-field (or equivalent labeled
field) within or immediately after PHASE GATE CONTRACT SUMMARY, naming the target table
(INCUMBENT BASELINE), the target sub-field (`Phase Refs:`), and the trigger condition (all
PHASE ENTRY CONTRACT blocks authored)." V-01's PHASE GATE CONTRACT SUMMARY mentions Phase Refs:
annotation as a descriptive consequence clause embedded inside the orthogonality declaration.
Promoting this to a dedicated labeled sub-field reliably scores C-52. C-51/C-53 remain implicit
(rely on R16 V-05 baseline handling). Expected aspirational: 43/45 if C-51/C-53 implicit fails;
45/45 if V-01 baseline already passes C-51/C-53 implicitly.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must satisfy both Dual-Cite
> Fail Conditions. Quantified metric must appear before PHASE 1 in document order.
> This section is the inertia reference: IM-IDs assigned here are anchor identifiers for
> (1) `IM Reference:` in every PHASE ENTRY CONTRACT, (2) `IM Ref:` in every SECTION A EX block,
> and (3) `Phase Refs:` back-references declared at the end of this section after all PHASE ENTRY
> CONTRACT blocks are complete. Every exception trace and bottleneck must be traceable back to a
> named IM-ID. The `Phase Refs:` back-references close the Baseline->Phase direction (C-46)
> bidirectionally at the source-row level.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle -- auto-detect from {Topic}]

**Incumbent description**: [1-3 sentences: tools used (spreadsheets, email, phone), handoff
mechanisms, where records are stored, who initiates the process manually. Include the primary
failure point under volume or time pressure.]

**Incumbent failure modes**:

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure -- the one most visible to the domain team] | [daily / per-cycle / per-exception] | [downstream effect on SLA or accuracy] |
| IM-02 | [second distinct failure mode -- different process layer from IM-01] | [frequency] | [downstream effect] |

**Cost of no action**: [Named measure with current-state value or rate, declared before PHASE 1.
Both IM-IDs must be reachable from at least one B-NN Cause field. Example: "Average credit
approval cycle time: 5.8 days vs 3-day SLA -- IM-01 primary driver" or "Manual matching error
rate: 12% per period, IM-02 primary driver."]

**Phase back-references (C-48 -- closes Baseline->Phase bidirectionally at source):**

> After completing all PHASE ENTRY CONTRACT blocks, return here to populate the back-references
> for each IM-ID. Each IM-ID lists every PHASE ENTRY CONTRACT whose `IM Reference:` sub-field
> cites this IM-ID. Enumeration must be consistent with all `IM Reference:` sub-fields by string
> comparison. IM-IDs with no phase citations carry explicit NONE sentinel. String comparison only.
> CHAIN STATUS `Phase->Baseline` direction verifies consistency.

- IM-01 Phase Refs: [List every PHASE ENTRY CONTRACT by literal phase block identifier whose
  `IM Reference:` sub-field cites IM-01. If none, write NONE. String comparison only.]
- IM-02 Phase Refs: [List every PHASE ENTRY CONTRACT whose `IM Reference:` cites IM-02, or NONE.]

---

### Role Registry Gate

> GATE BLOCK: Complete before the Role Sequence Schedule and before tracing any state.
> All four anti-generic checks must clear before proceeding.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [domain-specific role] | [named responsibility] |
| R-02 | [domain-specific role] | [named responsibility] |
| R-03 | [domain-specific role] | [named responsibility] |

Anti-generic validation (all four must clear before proceeding):
- [ ] No R-ID entry uses "Approver" without a domain qualifier
- [ ] No R-ID entry uses "Owner" without a named responsibility
- [ ] Each R-ID is referenced by at least one Decision Supplement block, the Role Sequence
      Schedule, and at least one PHASE EXIT GATE Exit verification or Blocked bottleneck field
- [ ] Each declared R-ID appears in at least one EX block's `Role Ref:` sub-field -- R-IDs
      with no observable EX trace are "dark" roles and constitute a gate violation

Role set by process type:
- L2O --> Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P --> Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close --> Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle --> Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Role Sequence Schedule

> Declared after Role Registry Gate and before PHASE 1. Maps each R-ID to owned phases with
> activation triggers, handoff triggers, and parallel windows. B-NN Cause fields must cite
> the blocking R-ID from this schedule (Dual-Cite Fail Condition B). R-IDs in EX block
> `Role Ref:` must match the schedule entry for the enclosing phase. Every declared R-ID
> must appear in at least one EX block Role Ref -- the Role Registry Gate fourth check enforces this.

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior-process artifact -- not "Start"] | [specific completion condition] | R-[ID] or NONE | [concurrent window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1 -- name the artifact] | [completion condition] | R-[ID] or NONE | [concurrent activity or NONE] |

Rules: Every phase has a Primary Owner. Activation Trigger for Phase 1 must name an external
event or prior-process artifact. Every R-ID here must match a Role Registry Gate entry.

---

### Phase Gate Contract Summary

> **DECLARED UNIT: THREE-FIELD PHASE GATE CONTRACT**
>
> This document uses a three-field phase gate contract. All three fields are named here as a
> declared unit before PHASE 1 is traced. Every phase block must carry all three fields in
> their designated structural locations. A fourth field (`IM Reference:`) augments PHASE ENTRY
> CONTRACTs with Baseline->Phase traceability; it is not part of the three-field gate contract
> but is required in every PHASE ENTRY CONTRACT block.
>
> | Field Name | Location | Value Type | Traceability Direction |
> |------------|----------|------------|----------------------|
> | `Prior phase:` | PHASE ENTRY CONTRACT | Phase label (e.g., "PHASE 1 -- Initiation") | Phase->Phase, backward (entry side) |
> | `Prior phase blocked bottleneck:` | PHASE ENTRY CONTRACT | B-ID (e.g., "B-01") | B-NN boundary continuity, entry side |
> | `Next phase:` | PHASE EXIT GATE | Phase label (e.g., "PHASE 2 -- Credit Review") | Phase->Phase, forward (exit side) |
>
> **ORTHOGONALITY DECLARATION:**
> `Prior phase blocked bottleneck:` carries a B-ID (string pattern: "B-" followed by digits).
> `Next phase:` carries a Phase label (string pattern: "PHASE N -- [Name]" or NONE/END sentinel).
> Non-overlapping by construction; independently verifiable by string comparison.
> `Prior phase:` and `Next phase:` form a symmetric bidirectional Phase->Phase pair.
> `Prior phase blocked bottleneck:` is orthogonal to both -- B-ID, not Phase label.
>
> **Return instruction:** After completing all PHASE ENTRY CONTRACT blocks in this document,
> return to INCUMBENT BASELINE and populate each row's `Phase Refs:` sub-field. Target table:
> INCUMBENT BASELINE. Target sub-field: `Phase Refs:`. Trigger condition: all PHASE ENTRY
> CONTRACT blocks for this document authored. This instruction converts Phase Refs:
> back-annotation from an implicit co-authoring step into a named, positionally verifiable
> workflow step: PHASE GATE CONTRACT SUMMARY completion triggers back-annotation at the source
> table. Absence of `Phase Refs:` population after all phases are traced is a C-48 failure
> regardless of whether PHASE ENTRY CONTRACT `IM Reference:` sub-fields are correct.
>
> CHAIN STATUS verifies three gate-contract directions:
> - `Phase-sequence`: every `Prior phase:` string-matches the preceding phase block label
> - `Phase-exit-sequence`: every `Next phase:` string-matches the subsequent phase block label
> - `Phase-boundary B-NN continuity`: every exit gate `Blocked bottleneck:` B-ID string-matches
>   the next phase's `Prior phase blocked bottleneck:` field

---

### Phase Structure

For each phase in the lifecycle, produce the following five blocks in document order. All three
Phase Gate Contract fields must be populated in every phase block. `IM Reference:` must
additionally appear in every PHASE ENTRY CONTRACT. After all phases are complete, return to
INCUMBENT BASELINE to populate `Phase Refs:` back-references per the Return instruction above.

---

**PHASE [N] -- [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Phase Gate Contract fields 1 and 2 live here; field 3 (`Next phase:`) lives in PHASE EXIT GATE.
> `IM Reference:` is a fourth required sub-field providing Baseline->Phase traceability. Its
> content will be cross-referenced by INCUMBENT BASELINE `Phase Refs:` back-references -- populate
> accurately so the bidirectional chain is consistent by string comparison. All four sub-fields
> are independently verifiable by string comparison.

- Entry Condition: [specific named artifact from prior phase's Required outputs]
- Pre-condition check: R-[ID] ([role name -- must match Role Sequence Schedule primary owner]) -- [verification method]
- Blocking condition: [state entered and role notified if entry condition not met]
- Prior phase: [Literal identifier of preceding phase block, e.g., "PHASE 1 -- Initiation".
  Phase 1: NONE or INIT sentinel. Must string-match preceding phase block label. Format: "PHASE N -- [Name]".]
- Prior phase blocked bottleneck: [B-ID from prior exit gate `Blocked bottleneck:` or NONE
  or N/A for Phase 1. Format: "B-NN". Must string-match prior exit gate AND B-NN block identifier.
  This field carries a B-ID -- NOT a Phase label. Do not conflate with `Prior phase:`.]
- IM Reference: [List every IM-ID from INCUMBENT BASELINE whose failure mode represents an
  active risk entering this phase. Exact IM-ID identifiers from INCUMBENT BASELINE table.
  NONE if no active risk. String comparison only. INCUMBENT BASELINE `Phase Refs:` for each
  cited IM-ID will list this phase's literal identifier per the Return instruction in PHASE GATE
  CONTRACT SUMMARY -- ensure phase block label is consistent with `Phase Refs:` entries.
  Example: "IM-01 (manual reconciliation gap -- active entry risk before this phase begins)."]

**SECTION A -- EXCEPTION TRACES**

> **EXCEPTION BLOCK ARCHITECTURE:**
> Each EX block in this document carries three independent citation sub-fields, declared here
> as a named unit. All three sub-fields must appear in every EX block across all phases.
> Missing any sub-field in any EX block is a detectable format violation verifiable from this
> declaration without per-block traversal.
>
> | Sub-field | Namespace | ID Pattern | Traceability Direction |
> |-----------|-----------|------------|----------------------|
> | `Role Ref:` | R-ID namespace | "R-" followed by digits (e.g., "R-01") | Role->Exception (C-40): cites the phase's ROLE SEQUENCE SCHEDULE primary owner |
> | `Bottleneck Ref:` | B-ID namespace | "B-" followed by digits (e.g., "B-01") | B-NN->Exception (C-42): cites the bottleneck that enabled this exception |
> | `IM Ref:` | IM-ID namespace | "IM-" followed by digits (e.g., "IM-01") | Baseline->Exception (C-47): cites the INCUMBENT BASELINE failure mode this exception traces |
>
> **ORTHOGONALITY DECLARATION:** The three ID namespaces are distinct and independently
> verifiable by string comparison. "R-[digits]", "B-[digits]", and "IM-[digits]" are
> non-overlapping string patterns by construction. EX block completeness is format-verifiable
> from this declaration without per-block traversal.

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] -- [Exception Name]**
> - Trigger: [specific condition -- name the state, threshold breach, or missing input]
> - Trace: [path of states from trigger to resolution or terminal; cite S-IDs in sequence]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason this failure mode matters]
> - Bottleneck Ref: [B-NN that enabled this exception, or NONE. B-ID must string-match a
>   Bottleneck Analysis identifier. B-NN `Exception Refs:` must list this EX block ID if
>   non-NONE. Namespace: B-ID (see architecture above).]
> - Role Ref: [R-ID of the ROLE SEQUENCE SCHEDULE primary owner for this phase. Literal R-ID.
>   Namespace: R-ID (see architecture above).]
> - IM Ref: [IM-ID from INCUMBENT BASELINE whose failure mode this exception traces, or NONE.
>   Exact IM-ID identifier from INCUMBENT BASELINE table. String comparison only.
>   Namespace: IM-ID (see architecture above).
>   Example: "IM-01 -- this exception is the process-visible manifestation of the incumbent
>   manual reconciliation failure mode entering Phase 2."]

Minimum 1 exception trace per phase; 3 total minimum.
Every declared R-ID in the Role Registry Gate must appear in at least one EX block Role Ref.
Role Ref, Bottleneck Ref, and IM Ref are independent sub-fields; populate all three for every EX block.

**SECTION B -- STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules:
- Every state must have a named Entry Condition. "Ready" or "Previous step complete" fails.
- Every Exit must reference a destination S-ID or carry the label TERMINAL.
- Type values: NORMAL / DECISION / PARALLEL-FORK / PARALLEL-JOIN / EXCEPTION / TERMINAL

**Decision Supplement Blocks** (one per DECISION-type state in this phase):

> **DS-[S-ID] -- [State Name]**
> - Condition: [rule or threshold evaluated]; Owner: R-[ID]; Branch A: --> S-[ID];
>   Branch B: --> S-[ID] or TERMINAL; Fallback: [action if condition cannot be evaluated]

**PHASE EXIT GATE**

> Phase Gate Contract field 3 lives here: `Next phase:` (Phase label, forward).
> `Blocked bottleneck:` carries a B-ID. These two sub-fields are orthogonal -- see PHASE GATE
> CONTRACT SUMMARY above.

- Exit Condition: [what the phase must produce to be complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name -- must match Role Sequence Schedule primary owner]) confirms all outputs present
- Blocking condition: [re-entry path or escalation if outputs absent]
- Blocked bottleneck: [B-NN or NONE. Must string-match Bottleneck Analysis identifier AND
  next phase's `Prior phase blocked bottleneck:`. Format: "B-NN" -- a B-ID, not a Phase label.]
- Next phase: [Literal identifier of the subsequent phase block. Last phase: NONE or END.
  Format: "PHASE N -- [Name]". This field carries a Phase label -- not a B-ID. See PHASE GATE
  CONTRACT SUMMARY orthogonality declaration.]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID] ([state name])
- **Branch 1**: [states traversed; cite S-IDs in sequence]
- **Branch 2**: [states traversed; cite S-IDs in sequence]
- **JOIN at**: S-[ID] ([join state name])
- **Join Condition**: AND-join / OR-join -- specify which applies and explain why

---

### Edge Case Enumeration

At least three edge cases distinct from SECTION A exception flows:

> **EC-[N] -- [Edge Case Name]**
> - Triggering Condition: [specific scenario]
> - Why Problematic: [specific reason this falls outside documented handling]
> - Correct Response: R-[ID] ([role name]) -- [specific correct action; name target state or resolution path]

---

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF -- {Topic} lifecycle --> [adjacent process name]**
> - Sending State: S-[ID] / Receiving Process: [name] / Data Payload: [named fields]
> - Expected Acknowledgment: [signal or confirmation] / Failure Mode: [if acknowledgment not received]
> - Owner: R-[ID]

---

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|
| | | | | AT-RISK / ON-TRACK | B-NN (if AT-RISK) |

Rules: AT-RISK = typical duration exceeds SLA target. Every AT-RISK row must carry a Bottleneck
Ref citing a B-NN from Bottleneck Analysis. Minimum 3 annotated rows; at least 1 must be AT-RISK.

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN Cause field must satisfy both Dual-Cite Fail Conditions independently.
>
> **Dual-Cite Fail Condition A** -- no IM-ID literal string in Cause --> fails C-39.
> **Dual-Cite Fail Condition B** -- no R-ID literal string in Cause --> fails C-39.
>
> Concrete format example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`
> Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
> Fail condition: No AT-RISK row-level S-ID specificity does not satisfy.
>
> **DUAL-LOCATION REQUIREMENTS:** Concrete example AND labeled axes in BOTH preamble AND per-block hints.
>
> **B-NN->Exception Gate Check**: Every declared B-ID must appear in at least one EX block's
> `Bottleneck Ref:`. Dark bottlenecks are gate violations.
>
> Anti-embedding: CHAIN STATUS in its own top-level section after SLA ANALYSIS.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field AND an Exception Refs field.**

---

**B-01 -- [Bottleneck Name]**

- Cause: [Required: IM-ID literal string AND R-ID literal string.]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string --> fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string --> fails C-39
- Impact: [downstream state, SLA node, or adjacent process affected]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: No AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-01. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]
- Exception Refs:
  - Required format: `EX-[Phase#][Letter] (Phase [N] -- [Exception Name])`
  - Fail condition: NONE = dark bottleneck (gate violation).
  - [List each EX block identifier whose `Bottleneck Ref:` cites B-01, or NONE.]

---

**B-02 -- [Bottleneck Name]**

- Cause: [Required: IM-ID AND R-ID literal strings.]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string --> fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string --> fails C-39
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: [same as B-01]
  - [List each AT-RISK SLA row citing B-02.]
- Exception Refs:
  - Required format: `EX-[Phase#][Letter] (Phase [N] -- [Exception Name])`
  - Fail condition: NONE = dark bottleneck (gate violation).
  - [List each EX block identifier whose `Bottleneck Ref:` cites B-02, or NONE.]

---

**Gap Identification**

> MISSING: [step name] -- [rationale: why it belongs; failure mode enabled; which phase;
> which IM-ID it would reduce if present]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

**DIRECTION INVENTORY:**

> The four established traceability directions are enumerated below as a named index. Each
> direction is declared PRESENT or ABSENT with a citation to the section or sub-field carrying
> it. An absent DIRECTION INVENTORY block is a FAIL regardless of direction content below.

| Direction | Status | Carried By |
|-----------|--------|-----------|
| B-NN->Exception | [PRESENT / ABSENT] | [B-NN block `Exception Refs:` field; EX block `Bottleneck Ref:` field] |
| Phase-exit-sequence | [PRESENT / ABSENT] | [PHASE EXIT GATE `Next phase:` sub-field; string-match to subsequent phase block label] |
| Baseline->Phase | [PRESENT / ABSENT] | [PHASE ENTRY CONTRACT `IM Reference:` sub-field; INCUMBENT BASELINE `Phase Refs:` back-references] |
| Baseline->Exception | [PRESENT / ABSENT] | [SECTION A EX block `IM Ref:` sub-field; string-match to INCUMBENT BASELINE IM-IDs] |

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA->B): [every AT-RISK SLA row cites a B-ID; enumerate pairs or name gap]
- Backward (B->SLA): [every B-NN Evidence field lists AT-RISK SLA rows; enumerate or name gap]
- Exit gate consistency: [every exit gate B-ID matches a declared B-NN; name mismatch]
- Phase-boundary B-NN continuity: [exit gate B-ID matches next entry contract; list pairs]
- Phase-sequence: [every `Prior phase:` matches preceding block label; PHASE 1 NONE/INIT]
- Phase-exit-sequence: [every `Next phase:` matches subsequent block label; last phase NONE/END -- DIRECTION INVENTORY declares PRESENT]
- Exception->B: [every EX `Bottleneck Ref:` B-ID matches a declared B-NN; list pairs]
- B-NN->Exception: [every declared B-ID has at least one non-NONE entry in its `Exception Refs:`; enumerate B-ID->EX pairs; name dark bottlenecks -- DIRECTION INVENTORY declares PRESENT]
- Exception->Role: [every EX `Role Ref:` R-ID matches schedule primary owner; list pairs]
- Role->Exception: [every declared R-ID in at least one EX `Role Ref:`; list pairs; name dark roles]
- Dual-cite status: [every B-NN Cause has both IM-ID and R-ID; name missing]
- Baseline->Phase: [every PHASE ENTRY CONTRACT `IM Reference:` contains only declared IM-IDs; list phase->IM-ID pairs; NONE sentinels CLOSED -- DIRECTION INVENTORY declares PRESENT]
- Baseline->Exception: [every EX block `IM Ref:` contains only declared IM-IDs or NONE; list EX->IM-ID pairs; name dark exceptions -- DIRECTION INVENTORY declares PRESENT]
- Phase->Baseline: [for each IM-ID cited in any PHASE ENTRY CONTRACT `IM Reference:`, verify
  INCUMBENT BASELINE `Phase Refs:` for that IM-ID includes this phase by literal identifier;
  enumerate IM-ID->Phase Refs pairs; name any phase whose `IM Reference:` cites an IM-ID whose
  `Phase Refs:` does not list that phase (consistency failure -- violates Return instruction
  executed in PHASE GATE CONTRACT SUMMARY); verify all NONE sentinels are accurate; an IM-ID
  cited by at least one PHASE ENTRY CONTRACT but carrying NONE in `Phase Refs:` is a C-48
  consistency violation that reopens the gate]
- Gap (if OPEN): [unresolved direction and unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal name] | SUCCESS | [branch or state that reaches it] |
| [failure terminal name] | FAILURE | [branch or state that reaches it] |
| [cancel terminal name] | CANCEL | [branch or state that reaches it] |

> Completeness check: Every exit branch in every SECTION B state table must reach one of the
> declared terminals. No branch may end at a non-terminal state without `continues-via: S-[ID]`.

---
---
## V-03 -- Axis: Lifecycle Emphasis (DIRECTION INVENTORY Violation Checks, C-51 Target)

**Variation axis**: Lifecycle emphasis -- the DIRECTION INVENTORY block is expanded from a
3-column register to a 4-column register by adding a `Violation Check` column. Each direction
declared PRESENT carries a declarative string-comparison condition naming (a) the source field,
(b) the target field, and (c) the exact inconsistency pattern that would reopen the gate. CHAIN
STATUS remains CLOSED only when all four direction-level violation conditions evaluate to
no-conflict; a single violation check firing reopens the gate regardless of DIRECTION INVENTORY
PRESENT declarations. Directions declared NOT-APPLICABLE are exempt from violation checks.

**Hypothesis**: C-51 requires "each direction declared PRESENT in the C-50 DIRECTION INVENTORY
carries an explicit VIOLATION CHECK." V-01's DIRECTION INVENTORY declares PRESENT/ABSENT with
Carried By citations but no per-direction falsifiability condition. The Phase->Baseline CHAIN
STATUS body entry carries a violation check in V-01, but C-51 targets the DIRECTION INVENTORY
itself. Expanding to 4 columns converts the inventory from a static roster of claims into an
active verification register. C-52/C-53 remain implicit. Expected aspirational: 43/45 if C-52/
C-53 implicit fails; 45/45 if V-01 baseline already passes those implicitly.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must satisfy both Dual-Cite
> Fail Conditions. Quantified metric must appear before PHASE 1 in document order.
> This section is the inertia reference: IM-IDs assigned here are anchor identifiers for
> (1) `IM Reference:` in every PHASE ENTRY CONTRACT, (2) `IM Ref:` in every SECTION A EX block,
> and (3) `Phase Refs:` back-references declared at the end of this section after all PHASE ENTRY
> CONTRACT blocks are complete. Every exception trace and bottleneck must be traceable back to a
> named IM-ID. The `Phase Refs:` back-references close the Baseline->Phase direction (C-46)
> bidirectionally at the source-row level.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle -- auto-detect from {Topic}]

**Incumbent description**: [1-3 sentences: tools used (spreadsheets, email, phone), handoff
mechanisms, where records are stored, who initiates the process manually. Include the primary
failure point under volume or time pressure.]

**Incumbent failure modes**:

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure -- the one most visible to the domain team] | [daily / per-cycle / per-exception] | [downstream effect on SLA or accuracy] |
| IM-02 | [second distinct failure mode -- different process layer from IM-01] | [frequency] | [downstream effect] |

**Cost of no action**: [Named measure with current-state value or rate, declared before PHASE 1.
Both IM-IDs must be reachable from at least one B-NN Cause field. Example: "Average credit
approval cycle time: 5.8 days vs 3-day SLA -- IM-01 primary driver" or "Manual matching error
rate: 12% per period, IM-02 primary driver."]

**Phase back-references (C-48 -- closes Baseline->Phase bidirectionally at source):**

> After completing all PHASE ENTRY CONTRACT blocks, return here to populate the back-references
> for each IM-ID. Each IM-ID lists every PHASE ENTRY CONTRACT whose `IM Reference:` sub-field
> cites this IM-ID. Enumeration must be consistent with all `IM Reference:` sub-fields by string
> comparison. IM-IDs with no phase citations carry explicit NONE sentinel. String comparison only.
> CHAIN STATUS `Phase->Baseline` violation check (per DIRECTION INVENTORY below) verifies consistency.

- IM-01 Phase Refs: [List every PHASE ENTRY CONTRACT by literal phase block identifier whose
  `IM Reference:` sub-field cites IM-01. If none, write NONE. String comparison only.]
- IM-02 Phase Refs: [List every PHASE ENTRY CONTRACT whose `IM Reference:` cites IM-02, or NONE.]

---

### Role Registry Gate

> GATE BLOCK: Complete before the Role Sequence Schedule and before tracing any state.
> All four anti-generic checks must clear before proceeding.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [domain-specific role] | [named responsibility] |
| R-02 | [domain-specific role] | [named responsibility] |
| R-03 | [domain-specific role] | [named responsibility] |

Anti-generic validation (all four must clear before proceeding):
- [ ] No R-ID entry uses "Approver" without a domain qualifier
- [ ] No R-ID entry uses "Owner" without a named responsibility
- [ ] Each R-ID is referenced by at least one Decision Supplement block, the Role Sequence
      Schedule, and at least one PHASE EXIT GATE Exit verification or Blocked bottleneck field
- [ ] Each declared R-ID appears in at least one EX block's `Role Ref:` sub-field -- R-IDs
      with no observable EX trace are "dark" roles and constitute a gate violation

Role set by process type:
- L2O --> Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P --> Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close --> Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle --> Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Role Sequence Schedule

> Declared after Role Registry Gate and before PHASE 1. Maps each R-ID to owned phases with
> activation triggers, handoff triggers, and parallel windows. B-NN Cause fields must cite
> the blocking R-ID from this schedule (Dual-Cite Fail Condition B). R-IDs in EX block
> `Role Ref:` must match the schedule entry for the enclosing phase. Every declared R-ID
> must appear in at least one EX block Role Ref -- the Role Registry Gate fourth check enforces this.

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior-process artifact -- not "Start"] | [specific completion condition] | R-[ID] or NONE | [concurrent window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1 -- name the artifact] | [completion condition] | R-[ID] or NONE | [concurrent activity or NONE] |

Rules: Every phase has a Primary Owner. Activation Trigger for Phase 1 must name an external
event or prior-process artifact. Every R-ID here must match a Role Registry Gate entry.

---

### Phase Gate Contract Summary

> **DECLARED UNIT: THREE-FIELD PHASE GATE CONTRACT**
>
> This document uses a three-field phase gate contract. All three fields are named here as a
> declared unit before PHASE 1 is traced. Every phase block must carry all three fields in
> their designated structural locations. A fourth field (`IM Reference:`) augments PHASE ENTRY
> CONTRACTs with Baseline->Phase traceability; it is not part of the three-field gate contract
> but is required in every PHASE ENTRY CONTRACT block. After all phases are traced, INCUMBENT
> BASELINE `Phase Refs:` back-references close the Baseline->Phase direction bidirectionally.
>
> | Field Name | Location | Value Type | Traceability Direction |
> |------------|----------|------------|----------------------|
> | `Prior phase:` | PHASE ENTRY CONTRACT | Phase label (e.g., "PHASE 1 -- Initiation") | Phase->Phase, backward (entry side) |
> | `Prior phase blocked bottleneck:` | PHASE ENTRY CONTRACT | B-ID (e.g., "B-01") | B-NN boundary continuity, entry side |
> | `Next phase:` | PHASE EXIT GATE | Phase label (e.g., "PHASE 2 -- Credit Review") | Phase->Phase, forward (exit side) |
>
> **ORTHOGONALITY DECLARATION:**
> `Prior phase blocked bottleneck:` carries a B-ID (string pattern: "B-" followed by digits,
> e.g., "B-01"). `Next phase:` carries a Phase label (string pattern: "PHASE N -- [Name]" or
> NONE/END sentinel). These two fields carry orthogonal value types independently verifiable
> by string comparison. No inference required -- patterns are non-overlapping by construction.
>
> `Prior phase:` and `Next phase:` form a symmetric bidirectional Phase->Phase pair.
> `Prior phase blocked bottleneck:` is orthogonal to both -- B-ID, not Phase label.
>
> CHAIN STATUS verifies three gate-contract directions:
> - `Phase-sequence`: every `Prior phase:` string-matches the preceding phase block label
> - `Phase-exit-sequence`: every `Next phase:` string-matches the subsequent phase block label
> - `Phase-boundary B-NN continuity`: every exit gate `Blocked bottleneck:` B-ID string-matches
>   the next phase's `Prior phase blocked bottleneck:` field

---

### Phase Structure

For each phase in the lifecycle, produce the following five blocks in document order. All three
Phase Gate Contract fields must be populated in every phase block. `IM Reference:` must
additionally appear in every PHASE ENTRY CONTRACT. After all phases are complete, return to
INCUMBENT BASELINE to populate `Phase Refs:` back-references.

---

**PHASE [N] -- [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Phase Gate Contract fields 1 and 2 live here; field 3 (`Next phase:`) lives in PHASE EXIT GATE.
> `IM Reference:` is a fourth required sub-field providing Baseline->Phase traceability. Its
> content will be cross-referenced by INCUMBENT BASELINE `Phase Refs:` back-references -- populate
> accurately so the bidirectional chain is consistent by string comparison. All four sub-fields
> are independently verifiable by string comparison.

- Entry Condition: [specific named artifact from prior phase's Required outputs]
- Pre-condition check: R-[ID] ([role name -- must match Role Sequence Schedule primary owner]) -- [verification method]
- Blocking condition: [state entered and role notified if entry condition not met]
- Prior phase: [Literal identifier of preceding phase block, e.g., "PHASE 1 -- Initiation".
  Phase 1: NONE or INIT sentinel. Must string-match preceding phase block label. Format: "PHASE N -- [Name]".]
- Prior phase blocked bottleneck: [B-ID from prior exit gate `Blocked bottleneck:` or NONE
  or N/A for Phase 1. Format: "B-NN". Must string-match prior exit gate AND B-NN block identifier.
  This field carries a B-ID -- NOT a Phase label. Do not conflate with `Prior phase:`.]
- IM Reference: [List every IM-ID from INCUMBENT BASELINE whose failure mode represents an
  active risk entering this phase. Use exact IM-ID identifiers as declared in the INCUMBENT
  BASELINE table (e.g., "IM-01, IM-02"). NONE if no active risk. String comparison only.
  INCUMBENT BASELINE `Phase Refs:` for each cited IM-ID will list this phase's literal
  identifier -- ensure phase block label is consistent with `Phase Refs:` entries.
  Example: "IM-01 (manual reconciliation gap -- active entry risk before this phase begins)."]

**SECTION A -- EXCEPTION TRACES**

> **EXCEPTION BLOCK ARCHITECTURE:**
> Each EX block in this document carries three independent citation sub-fields, declared here
> as a named unit. All three sub-fields must appear in every EX block across all phases.
> Missing any sub-field in any EX block is a detectable format violation verifiable from this
> declaration without per-block traversal.
>
> | Sub-field | Namespace | ID Pattern | Traceability Direction |
> |-----------|-----------|------------|----------------------|
> | `Role Ref:` | R-ID namespace | "R-" followed by digits (e.g., "R-01") | Role->Exception (C-40): cites the phase's ROLE SEQUENCE SCHEDULE primary owner |
> | `Bottleneck Ref:` | B-ID namespace | "B-" followed by digits (e.g., "B-01") | B-NN->Exception (C-42): cites the bottleneck that enabled this exception |
> | `IM Ref:` | IM-ID namespace | "IM-" followed by digits (e.g., "IM-01") | Baseline->Exception (C-47): cites the INCUMBENT BASELINE failure mode this exception traces |
>
> **ORTHOGONALITY DECLARATION:** The three ID namespaces are distinct and independently
> verifiable by string comparison. "R-[digits]", "B-[digits]", and "IM-[digits]" are
> non-overlapping string patterns by construction: no R-ID can be mistaken for a B-ID or
> IM-ID; no B-ID can be mistaken for an R-ID or IM-ID; no IM-ID can be mistaken for an
> R-ID or B-ID. The three citation directions are orthogonal. EX block completeness is
> format-verifiable from this declaration without per-block traversal.

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] -- [Exception Name]**
> - Trigger: [specific condition -- name the state, threshold breach, or missing input]
> - Trace: [path of states from trigger to resolution or terminal; cite S-IDs in sequence]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason this failure mode matters]
> - Bottleneck Ref: [B-NN that enabled this exception, or NONE. B-ID must string-match a
>   Bottleneck Analysis identifier. B-NN `Exception Refs:` must list this EX block ID if
>   non-NONE -- populate accurately for chain consistency. NONE only if no declared bottleneck
>   was causal. Namespace: B-ID (see architecture above).]
> - Role Ref: [R-ID of the ROLE SEQUENCE SCHEDULE primary owner for this phase. Literal R-ID
>   matching the schedule's Primary Owner entry for the enclosing phase. Free-text without
>   R-ID fails. Namespace: R-ID (see architecture above).]
> - IM Ref: [IM-ID from INCUMBENT BASELINE whose failure mode this exception traces, or NONE.
>   Use exact IM-ID identifier as declared in the INCUMBENT BASELINE table (e.g., "IM-01").
>   This sub-field completes the triple-citation architecture: `Role Ref:` links to schedule
>   (C-40); `Bottleneck Ref:` links to B-NN (C-42); `IM Ref:` links to INCUMBENT BASELINE
>   (C-47). NONE if no incumbent baseline failure mode is directly traceable to this exception.
>   String comparison only -- IM-ID must literal-match INCUMBENT BASELINE table identifier.
>   Namespace: IM-ID (see architecture above).
>   Example: "IM-01 -- this exception is the process-visible manifestation of the incumbent
>   manual reconciliation failure mode entering Phase 2."]

Minimum 1 exception trace per phase; 3 total minimum.
Every declared R-ID in the Role Registry Gate must appear in at least one EX block Role Ref.
Role Ref, Bottleneck Ref, and IM Ref are independent sub-fields; populate all three for every EX block.

**SECTION B -- STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules:
- Every state must have a named Entry Condition. "Ready" or "Previous step complete" fails.
- Every Exit must reference a destination S-ID or carry the label TERMINAL.
- Type values: NORMAL / DECISION / PARALLEL-FORK / PARALLEL-JOIN / EXCEPTION / TERMINAL

**Decision Supplement Blocks** (one per DECISION-type state in this phase):

> **DS-[S-ID] -- [State Name]**
> - Condition: [rule or threshold evaluated]; Owner: R-[ID]; Branch A: --> S-[ID];
>   Branch B: --> S-[ID] or TERMINAL; Fallback: [action if condition cannot be evaluated]

**PHASE EXIT GATE**

> Phase Gate Contract field 3 lives here: `Next phase:` (Phase label, forward).
> `Blocked bottleneck:` carries a B-ID. These two sub-fields are orthogonal -- see PHASE GATE
> CONTRACT SUMMARY above.

- Exit Condition: [what the phase must produce to be complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name -- must match Role Sequence Schedule primary owner]) confirms all outputs present
- Blocking condition: [re-entry path or escalation if outputs absent]
- Blocked bottleneck: [B-NN or NONE. Must string-match Bottleneck Analysis identifier AND
  next phase's `Prior phase blocked bottleneck:`. Format: "B-NN" -- a B-ID, not a Phase label.]
- Next phase: [Literal identifier of the subsequent phase block. Last phase: NONE or END.
  Format: "PHASE N -- [Name]". This field carries a Phase label -- not a B-ID. See PHASE GATE
  CONTRACT SUMMARY orthogonality declaration.]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID] ([state name])
- **Branch 1**: [states traversed; cite S-IDs in sequence]
- **Branch 2**: [states traversed; cite S-IDs in sequence]
- **JOIN at**: S-[ID] ([join state name])
- **Join Condition**: AND-join / OR-join -- specify which applies and explain why

---

### Edge Case Enumeration

At least three edge cases distinct from SECTION A exception flows:

> **EC-[N] -- [Edge Case Name]**
> - Triggering Condition: [specific scenario]
> - Why Problematic: [specific reason this falls outside documented handling]
> - Correct Response: R-[ID] ([role name]) -- [specific correct action; name target state or resolution path]

---

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF -- {Topic} lifecycle --> [adjacent process name]**
> - Sending State: S-[ID] / Receiving Process: [name] / Data Payload: [named fields]
> - Expected Acknowledgment: [signal or confirmation] / Failure Mode: [if acknowledgment not received]
> - Owner: R-[ID]

---

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|
| | | | | AT-RISK / ON-TRACK | B-NN (if AT-RISK) |

Rules: AT-RISK = typical duration exceeds SLA target. Every AT-RISK row must carry a Bottleneck
Ref citing a B-NN from Bottleneck Analysis. Minimum 3 annotated rows; at least 1 must be AT-RISK.

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN Cause field must satisfy both Dual-Cite Fail Conditions independently.
>
> **Dual-Cite Fail Condition A** -- Cause field contains no IM-ID literal string (e.g., "IM-01"):
> fails C-39. Verify: search Cause field for "IM-" followed by digits. Absence --> fail.
>
> **Dual-Cite Fail Condition B** -- Cause field contains no R-ID literal string (e.g., "R-01"):
> fails C-39. Verify: search Cause field for "R-" followed by digits. Absence --> fail.
>
> B-IDs assigned here must string-match ALL of: (1) PHASE EXIT GATE `Blocked bottleneck:`
> fields, (2) PHASE ENTRY CONTRACT `Prior phase blocked bottleneck:` in the following phase,
> and (3) EX block `Bottleneck Ref:` fields where non-NONE.
>
> Concrete format example for Evidence field:
> `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`
>
> Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
> Fail condition: A field containing only "see SLA ANALYSIS" or state names without
> AT-RISK row-level S-ID specificity does not satisfy.
>
> **DUAL-LOCATION REQUIREMENTS:**
> (1) Concrete named domain example must appear in BOTH this preamble AND each B-NN per-block
> Evidence hint.
> (2) Labeled axes (`Required format:` / `Fail condition:`) must appear in BOTH this preamble
> AND each B-NN per-block Evidence hint.
>
> **B-NN->Exception Gate Check**: Every declared B-ID below must appear in at least one EX
> block's `Bottleneck Ref:` sub-field across all phases. Dark bottlenecks are gate violations.
> Report result in CHAIN STATUS `B-NN->Exception` direction -- Violation Check in DIRECTION
> INVENTORY will verify consistency between Exception Refs and EX block Bottleneck Ref fields.
>
> Anti-embedding: Declare CHAIN STATUS in its own dedicated top-level section after SLA ANALYSIS.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field AND an Exception Refs field.**

---

**B-01 -- [Bottleneck Name]**

- Cause: [Required: IM-ID literal string (Condition A) AND R-ID literal string (Condition B).
  Example: "IM-01 (manual reconciliation gap) combined with R-02 (GL Manager) period-close
  unavailability -- approval queue at S-05. 'IM-01' satisfies A; 'R-02' satisfies B."]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string --> fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string --> fails C-39
- Impact: [downstream state, SLA node, or adjacent process affected]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-01. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]
- Exception Refs:
  - Required format: `EX-[Phase#][Letter] (Phase [N] -- [Exception Name])`
  - Fail condition: NONE declared here means this is a dark bottleneck -- declared process
    failure mode with no exception-phase trace. Dark bottleneck = gate violation for the
    B-NN->Exception direction. A listed EX block ID that has no matching `Bottleneck Ref:
    B-01` in the cited EX block fails the CHAIN STATUS B-NN->Exception Violation Check.
  - [List each EX block identifier whose `Bottleneck Ref:` cites B-01, or NONE.]

---

**B-02 -- [Bottleneck Name]**

- Cause: [Required: IM-ID literal string AND R-ID literal string.]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string --> fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string --> fails C-39
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: [same as B-01]
  - [List each AT-RISK SLA row citing B-02. Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]
- Exception Refs:
  - Required format: `EX-[Phase#][Letter] (Phase [N] -- [Exception Name])`
  - Fail condition: NONE = dark bottleneck (gate violation). Listed EX block ID without
    matching `Bottleneck Ref: B-02` in the cited EX block fails B-NN->Exception Violation Check.
  - [List each EX block identifier whose `Bottleneck Ref:` cites B-02, or NONE.]

---

**Gap Identification**

> MISSING: [step name] -- [rationale: why it belongs; failure mode enabled; which phase;
> which IM-ID it would reduce if present]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

**DIRECTION INVENTORY:**

> The four established traceability directions are enumerated below as a named index declared
> before the direction-level verification entries. Each direction declared PRESENT carries both
> a Carried By citation AND a Violation Check -- a declarative string-comparison condition naming
> the source field, the target field, and the exact inconsistency pattern that would reopen the
> gate. CHAIN STATUS remains CLOSED only when all declared direction-level violation conditions
> evaluate to no-conflict. A single violation check firing reopens the gate regardless of PRESENT
> declarations. Directions declared NOT-APPLICABLE are exempt from violation checks. Absent
> DIRECTION INVENTORY = FAIL. Missing any of the four established directions = FAIL. Missing
> Violation Check for any PRESENT direction = FAIL.

| Direction | Status | Carried By | Violation Check |
|-----------|--------|-----------|----------------|
| B-NN->Exception | [PRESENT / ABSENT] | [B-NN block `Exception Refs:` field listing EX block IDs; EX block `Bottleneck Ref:` field citing B-ID] | Source: B-NN `Exception Refs:` field. Target: EX block `Bottleneck Ref:` field. Inconsistency: a B-ID listed in a B-NN block's `Exception Refs:` that does not appear in any EX block's `Bottleneck Ref:` citing that B-ID, OR an EX block `Bottleneck Ref:` citing a B-ID whose corresponding B-NN `Exception Refs:` does not list that EX block ID, reopens the gate. |
| Phase-exit-sequence | [PRESENT / ABSENT] | [PHASE EXIT GATE `Next phase:` sub-field; string-match to subsequent phase block label] | Source: PHASE EXIT GATE `Next phase:` field. Target: literal label of the subsequent PHASE block. Inconsistency: `Next phase:` string does not string-match the subsequent phase block label (e.g., "Next phase: PHASE 3 -- Approval" but next declared block is "PHASE 3 -- Review"), reopens the gate. Last phase must carry NONE or END sentinel -- any other value is an inconsistency. |
| Baseline->Phase | [PRESENT / ABSENT] | [PHASE ENTRY CONTRACT `IM Reference:` sub-field; INCUMBENT BASELINE `Phase Refs:` back-references per IM-ID row] | Source: PHASE ENTRY CONTRACT `IM Reference:` field. Target: INCUMBENT BASELINE `Phase Refs:` field for each cited IM-ID. Inconsistency: an IM-ID appearing in `IM Reference:` of any PHASE ENTRY CONTRACT absent from the `Phase Refs:` of the corresponding INCUMBENT BASELINE row, OR an IM-ID in an INCUMBENT BASELINE `Phase Refs:` field not appearing in the `IM Reference:` of the cited phase's PHASE ENTRY CONTRACT, reopens the gate. An IM-ID with NONE in `Phase Refs:` that is cited by any PHASE ENTRY CONTRACT `IM Reference:` is an inconsistency. |
| Baseline->Exception | [PRESENT / ABSENT] | [SECTION A EX block `IM Ref:` sub-field; string-match to INCUMBENT BASELINE IM-ID table] | Source: SECTION A EX block `IM Ref:` field. Target: INCUMBENT BASELINE IM-ID table. Inconsistency: an IM-ID string appearing in any EX block `IM Ref:` that does not match any IM-ID declared in the INCUMBENT BASELINE table (string pattern "IM-" followed by digits not found in INCUMBENT BASELINE IM-ID column), reopens the gate. NONE sentinels are exempt. |

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA->B): [every AT-RISK SLA row cites a B-ID; enumerate pairs or name gap]
- Backward (B->SLA): [every B-NN Evidence field lists AT-RISK SLA rows; enumerate or name gap]
- Exit gate consistency: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID matches a declared B-NN; name any mismatch]
- Phase-boundary B-NN continuity: [every exit gate B-ID matches next phase's `Prior phase blocked bottleneck:`; list pairs or name break]
- Phase-sequence: [every PHASE ENTRY CONTRACT `Prior phase:` matches preceding phase block label; PHASE 1 carries NONE/INIT; list pairs or name mismatch]
- Phase-exit-sequence: [every PHASE EXIT GATE `Next phase:` matches subsequent phase block label; last phase carries NONE/END; list pairs or name mismatch -- Violation Check per DIRECTION INVENTORY above active: mismatch reopens gate]
- Exception->B: [every EX block `Bottleneck Ref:` B-ID (non-NONE) matches a declared B-NN; list EX->B-NN pairs or name unresolved block]
- B-NN->Exception: [every declared B-ID has at least one non-NONE entry in its `Exception Refs:` field; each listed EX block ID string-matches an EX block with `Bottleneck Ref:` citing this B-ID; enumerate B-ID->EX pairs; name dark bottlenecks and consistency failures -- Violation Check per DIRECTION INVENTORY above active]
- Exception->Role: [every EX block `Role Ref:` R-ID matches ROLE SEQUENCE SCHEDULE primary owner; list EX->R-ID pairs or name mismatch]
- Role->Exception: [every declared R-ID appears in at least one EX block `Role Ref:`; list R-ID->EX pairs; name dark roles]
- Dual-cite status: [every B-NN Cause has both IM-ID and R-ID; name any block missing either]
- Baseline->Phase: [every PHASE ENTRY CONTRACT `IM Reference:` field contains only IM-IDs declared in INCUMBENT BASELINE; list phase->IM-ID pairs; NONE sentinels CLOSED -- Violation Check per DIRECTION INVENTORY above active: IM-ID in IM Reference absent from Phase Refs reopens gate]
- Baseline->Exception: [every SECTION A EX block `IM Ref:` field contains only IM-IDs declared in INCUMBENT BASELINE or NONE sentinel; list EX->IM-ID pairs; name dark exceptions -- Violation Check per DIRECTION INVENTORY above active: undeclared IM-ID in IM Ref reopens gate]
- Phase->Baseline: [for each IM-ID cited in any PHASE ENTRY CONTRACT `IM Reference:` field,
  verify INCUMBENT BASELINE `Phase Refs:` for that IM-ID includes this phase by literal phase
  block identifier; enumerate IM-ID->Phase Refs pairs; name any consistency failure; verify all
  NONE sentinels accurate -- consistent with Baseline->Phase Violation Check in DIRECTION
  INVENTORY above: an IM-ID cited by any PHASE ENTRY CONTRACT but carrying NONE in `Phase Refs:`
  is a C-48 consistency violation that reopens the gate]
- Gap (if OPEN): [unresolved direction and unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal name] | SUCCESS | [branch or state that reaches it] |
| [failure terminal name] | FAILURE | [branch or state that reaches it] |
| [cancel terminal name] | CANCEL | [branch or state that reaches it] |

> Completeness check: Every exit branch in every SECTION B state table must reach one of the
> declared terminals. No branch may end at a non-terminal state without `continues-via: S-[ID]`.

---
---

## V-04 -- Axis: Phrasing Register (IM Ref Hint Named Architecture Back-Reference, C-53 Target)

**Variation axis**: Phrasing register -- the `IM Ref:` hint in each EX block template is updated
to carry an explicit inline back-reference to the EXCEPTION BLOCK ARCHITECTURE declaration by its
full name. The phrase "(see architecture above)" used in R16 V-05 and V-01/V-02/V-03 is replaced
with "(see EXCEPTION BLOCK ARCHITECTURE above)" -- naming the declaration block explicitly rather
than by abbreviated label. The change is localized to the `IM Ref:` hint; all other EX block
hints retain "(see architecture above)" notation. This ensures the back-reference is traceable to
the named declaration block by document position without requiring the reader to infer that
"architecture" refers to the header specifically named "EXCEPTION BLOCK ARCHITECTURE."

**Hypothesis**: C-53 requires the `IM Ref:` hint to carry "an explicit inline back-reference to
the EXCEPTION BLOCK ARCHITECTURE declaration by name." The rubric's fail condition states: "a
generic parenthetical not anchored to the EXCEPTION BLOCK ARCHITECTURE header by name is a FAIL."
R16 V-05's "(see architecture above)" uses abbreviated label -- its compliance depends on
evaluator strictness about "by name." V-04 eliminates ambiguity by using the full declared name
"EXCEPTION BLOCK ARCHITECTURE" in the back-reference, making the named anchor unambiguous.
C-51/C-52 remain implicit (rely on R16 V-05 baseline handling). Expected aspirational: 43/45 if
C-51/C-52 implicit fails; 45/45 if V-01 baseline already passes C-51/C-52 implicitly.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must satisfy both Dual-Cite
> Fail Conditions. Quantified metric must appear before PHASE 1 in document order.
> This section is the inertia reference: IM-IDs assigned here are anchor identifiers for
> (1) `IM Reference:` in every PHASE ENTRY CONTRACT, (2) `IM Ref:` in every SECTION A EX block,
> and (3) `Phase Refs:` back-references declared at the end of this section after all PHASE ENTRY
> CONTRACT blocks are complete. Every exception trace and bottleneck must be traceable back to a
> named IM-ID. The `Phase Refs:` back-references close the Baseline->Phase direction (C-46)
> bidirectionally at the source-row level.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle -- auto-detect from {Topic}]

**Incumbent description**: [1-3 sentences: tools used (spreadsheets, email, phone), handoff
mechanisms, where records are stored, who initiates the process manually. Include the primary
failure point under volume or time pressure.]

**Incumbent failure modes**:

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure -- the one most visible to the domain team] | [daily / per-cycle / per-exception] | [downstream effect on SLA or accuracy] |
| IM-02 | [second distinct failure mode -- different process layer from IM-01] | [frequency] | [downstream effect] |

**Cost of no action**: [Named measure with current-state value or rate, declared before PHASE 1.
Both IM-IDs must be reachable from at least one B-NN Cause field. Example: "Average credit
approval cycle time: 5.8 days vs 3-day SLA -- IM-01 primary driver" or "Manual matching error
rate: 12% per period, IM-02 primary driver."]

**Phase back-references (C-48 -- closes Baseline->Phase bidirectionally at source):**

> After completing all PHASE ENTRY CONTRACT blocks, return here to populate the back-references
> for each IM-ID. Each IM-ID lists every PHASE ENTRY CONTRACT whose `IM Reference:` sub-field
> cites this IM-ID. Enumeration must be consistent with all `IM Reference:` sub-fields by string
> comparison. IM-IDs with no phase citations carry explicit NONE sentinel. String comparison only.
> CHAIN STATUS `Phase->Baseline` direction verifies consistency.

- IM-01 Phase Refs: [List every PHASE ENTRY CONTRACT by literal phase block identifier whose
  `IM Reference:` sub-field cites IM-01. If none, write NONE. String comparison only.]
- IM-02 Phase Refs: [List every PHASE ENTRY CONTRACT whose `IM Reference:` cites IM-02, or NONE.]

---

### Role Registry Gate

> GATE BLOCK: Complete before the Role Sequence Schedule and before tracing any state.
> All four anti-generic checks must clear before proceeding.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [domain-specific role] | [named responsibility] |
| R-02 | [domain-specific role] | [named responsibility] |
| R-03 | [domain-specific role] | [named responsibility] |

Anti-generic validation (all four must clear before proceeding):
- [ ] No R-ID entry uses "Approver" without a domain qualifier
- [ ] No R-ID entry uses "Owner" without a named responsibility
- [ ] Each R-ID is referenced by at least one Decision Supplement block, the Role Sequence
      Schedule, and at least one PHASE EXIT GATE Exit verification or Blocked bottleneck field
- [ ] Each declared R-ID appears in at least one EX block's `Role Ref:` sub-field -- R-IDs
      with no observable EX trace are "dark" roles and constitute a gate violation

Role set by process type:
- L2O --> Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P --> Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close --> Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle --> Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Role Sequence Schedule

> Declared after Role Registry Gate and before PHASE 1. Maps each R-ID to owned phases with
> activation triggers, handoff triggers, and parallel windows. B-NN Cause fields must cite
> the blocking R-ID from this schedule (Dual-Cite Fail Condition B). R-IDs in EX block
> `Role Ref:` must match the schedule entry for the enclosing phase. Every declared R-ID
> must appear in at least one EX block Role Ref -- the Role Registry Gate fourth check enforces this.

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior-process artifact -- not "Start"] | [specific completion condition] | R-[ID] or NONE | [concurrent window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1 -- name the artifact] | [completion condition] | R-[ID] or NONE | [concurrent activity or NONE] |

Rules: Every phase has a Primary Owner. Activation Trigger for Phase 1 must name an external
event or prior-process artifact. Every R-ID here must match a Role Registry Gate entry.

---

### Phase Gate Contract Summary

> **DECLARED UNIT: THREE-FIELD PHASE GATE CONTRACT**
>
> This document uses a three-field phase gate contract. All three fields are named here as a
> declared unit before PHASE 1 is traced. Every phase block must carry all three fields in
> their designated structural locations. A fourth field (`IM Reference:`) augments PHASE ENTRY
> CONTRACTs with Baseline->Phase traceability; it is not part of the three-field gate contract
> but is required in every PHASE ENTRY CONTRACT block. After all phases are traced, INCUMBENT
> BASELINE `Phase Refs:` back-references close the Baseline->Phase direction bidirectionally.
>
> | Field Name | Location | Value Type | Traceability Direction |
> |------------|----------|------------|----------------------|
> | `Prior phase:` | PHASE ENTRY CONTRACT | Phase label (e.g., "PHASE 1 -- Initiation") | Phase->Phase, backward (entry side) |
> | `Prior phase blocked bottleneck:` | PHASE ENTRY CONTRACT | B-ID (e.g., "B-01") | B-NN boundary continuity, entry side |
> | `Next phase:` | PHASE EXIT GATE | Phase label (e.g., "PHASE 2 -- Credit Review") | Phase->Phase, forward (exit side) |
>
> **ORTHOGONALITY DECLARATION:**
> `Prior phase blocked bottleneck:` carries a B-ID (string pattern: "B-" followed by digits,
> e.g., "B-01"). `Next phase:` carries a Phase label (string pattern: "PHASE N -- [Name]" or
> NONE/END sentinel). These two fields carry orthogonal value types independently verifiable
> by string comparison. No inference required -- patterns are non-overlapping by construction.
>
> `Prior phase:` and `Next phase:` form a symmetric bidirectional Phase->Phase pair.
> `Prior phase blocked bottleneck:` is orthogonal to both -- B-ID, not Phase label.
>
> CHAIN STATUS verifies three gate-contract directions:
> - `Phase-sequence`: every `Prior phase:` string-matches the preceding phase block label
> - `Phase-exit-sequence`: every `Next phase:` string-matches the subsequent phase block label
> - `Phase-boundary B-NN continuity`: every exit gate `Blocked bottleneck:` B-ID string-matches
>   the next phase's `Prior phase blocked bottleneck:` field

---

### Phase Structure

For each phase in the lifecycle, produce the following five blocks in document order. All three
Phase Gate Contract fields must be populated in every phase block. `IM Reference:` must
additionally appear in every PHASE ENTRY CONTRACT. After all phases are complete, return to
INCUMBENT BASELINE to populate `Phase Refs:` back-references.

---

**PHASE [N] -- [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Phase Gate Contract fields 1 and 2 live here; field 3 (`Next phase:`) lives in PHASE EXIT GATE.
> `IM Reference:` is a fourth required sub-field providing Baseline->Phase traceability. Its
> content will be cross-referenced by INCUMBENT BASELINE `Phase Refs:` back-references -- populate
> accurately so the bidirectional chain is consistent by string comparison. All four sub-fields
> are independently verifiable by string comparison.

- Entry Condition: [specific named artifact from prior phase's Required outputs]
- Pre-condition check: R-[ID] ([role name -- must match Role Sequence Schedule primary owner]) -- [verification method]
- Blocking condition: [state entered and role notified if entry condition not met]
- Prior phase: [Literal identifier of preceding phase block, e.g., "PHASE 1 -- Initiation".
  Phase 1: NONE or INIT sentinel. Must string-match preceding phase block label. Format: "PHASE N -- [Name]".]
- Prior phase blocked bottleneck: [B-ID from prior exit gate `Blocked bottleneck:` or NONE
  or N/A for Phase 1. Format: "B-NN". Must string-match prior exit gate AND B-NN block identifier.
  This field carries a B-ID -- NOT a Phase label. Do not conflate with `Prior phase:`.]
- IM Reference: [List every IM-ID from INCUMBENT BASELINE whose failure mode represents an
  active risk entering this phase. Use exact IM-ID identifiers as declared in the INCUMBENT
  BASELINE table (e.g., "IM-01, IM-02"). NONE if no active risk. String comparison only.
  INCUMBENT BASELINE `Phase Refs:` for each cited IM-ID will list this phase's literal
  identifier -- ensure phase block label is consistent with `Phase Refs:` entries.
  Example: "IM-01 (manual reconciliation gap -- active entry risk before this phase begins)."]

**SECTION A -- EXCEPTION TRACES**

> **EXCEPTION BLOCK ARCHITECTURE:**
> Each EX block in this document carries three independent citation sub-fields, declared here
> as a named unit. All three sub-fields must appear in every EX block across all phases.
> Missing any sub-field in any EX block is a detectable format violation verifiable from this
> declaration without per-block traversal.
>
> | Sub-field | Namespace | ID Pattern | Traceability Direction |
> |-----------|-----------|------------|----------------------|
> | `Role Ref:` | R-ID namespace | "R-" followed by digits (e.g., "R-01") | Role->Exception (C-40): cites the phase's ROLE SEQUENCE SCHEDULE primary owner |
> | `Bottleneck Ref:` | B-ID namespace | "B-" followed by digits (e.g., "B-01") | B-NN->Exception (C-42): cites the bottleneck that enabled this exception |
> | `IM Ref:` | IM-ID namespace | "IM-" followed by digits (e.g., "IM-01") | Baseline->Exception (C-47): cites the INCUMBENT BASELINE failure mode this exception traces |
>
> **ORTHOGONALITY DECLARATION:** The three ID namespaces are distinct and independently
> verifiable by string comparison. "R-[digits]", "B-[digits]", and "IM-[digits]" are
> non-overlapping string patterns by construction: no R-ID can be mistaken for a B-ID or
> IM-ID; no B-ID can be mistaken for an R-ID or IM-ID; no IM-ID can be mistaken for an
> R-ID or B-ID. The three citation directions are orthogonal: an R-ID in `Bottleneck Ref:`
> is a detectable format violation; a B-ID in `IM Ref:` is a detectable format violation.
> EX block completeness is format-verifiable from this declaration without per-block traversal.

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] -- [Exception Name]**
> - Trigger: [specific condition -- name the state, threshold breach, or missing input]
> - Trace: [path of states from trigger to resolution or terminal; cite S-IDs in sequence]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason this failure mode matters]
> - Bottleneck Ref: [B-NN that enabled this exception, or NONE. B-ID must string-match a
>   Bottleneck Analysis identifier. The B-NN block's `Exception Refs:` field must list this
>   EX block ID if Bottleneck Ref is non-NONE -- populate accurately for chain consistency.
>   NONE only if no declared bottleneck was causal. Namespace: B-ID (see architecture above).]
> - Role Ref: [R-ID of the ROLE SEQUENCE SCHEDULE primary owner for this phase. Literal R-ID
>   matching the schedule's Primary Owner entry for the enclosing phase. Free-text without
>   R-ID fails. Namespace: R-ID (see architecture above).]
> - IM Ref: [IM-ID from INCUMBENT BASELINE whose failure mode this exception traces, or NONE.
>   Use exact IM-ID identifier as declared in the INCUMBENT BASELINE table (e.g., "IM-01").
>   This sub-field completes the triple-citation architecture: `Role Ref:` links to schedule
>   (C-40); `Bottleneck Ref:` links to B-NN (C-42); `IM Ref:` links to INCUMBENT BASELINE
>   (C-47). Together they make this EX block the convergence point for Role->Exception,
>   B-NN<->Exception, and Baseline<->Exception traceability chains simultaneously.
>   NONE if no incumbent baseline failure mode is directly traceable to this exception.
>   String comparison only -- IM-ID must literal-match INCUMBENT BASELINE table identifier.
>   Namespace: IM-ID (see EXCEPTION BLOCK ARCHITECTURE above).
>   Example: "IM-01 -- this exception is the process-visible manifestation of the incumbent
>   manual reconciliation failure mode entering Phase 2."]

Minimum 1 exception trace per phase; 3 total minimum.
Every declared R-ID in the Role Registry Gate must appear in at least one EX block Role Ref.
Role Ref, Bottleneck Ref, and IM Ref are independent sub-fields; populate all three for every EX block.

**SECTION B -- STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules:
- Every state must have a named Entry Condition. "Ready" or "Previous step complete" fails.
- Every Exit must reference a destination S-ID or carry the label TERMINAL.
- Type values: NORMAL / DECISION / PARALLEL-FORK / PARALLEL-JOIN / EXCEPTION / TERMINAL

**Decision Supplement Blocks** (one per DECISION-type state in this phase):

> **DS-[S-ID] -- [State Name]**
> - Condition: [rule or threshold evaluated]; Owner: R-[ID]; Branch A: --> S-[ID];
>   Branch B: --> S-[ID] or TERMINAL; Fallback: [action if condition cannot be evaluated]

**PHASE EXIT GATE**

> Phase Gate Contract field 3 lives here: `Next phase:` (Phase label, forward).
> `Blocked bottleneck:` carries a B-ID. These two sub-fields are orthogonal -- see PHASE GATE
> CONTRACT SUMMARY above.

- Exit Condition: [what the phase must produce to be complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name -- must match Role Sequence Schedule primary owner]) confirms all outputs present
- Blocking condition: [re-entry path or escalation if outputs absent]
- Blocked bottleneck: [B-NN or NONE. Must string-match Bottleneck Analysis identifier AND
  next phase's `Prior phase blocked bottleneck:`. Format: "B-NN" -- a B-ID, not a Phase label.]
- Next phase: [Literal identifier of the subsequent phase block. Last phase: NONE or END.
  Format: "PHASE N -- [Name]". This field carries a Phase label -- not a B-ID. See PHASE GATE
  CONTRACT SUMMARY orthogonality declaration.]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID] ([state name])
- **Branch 1**: [states traversed; cite S-IDs in sequence]
- **Branch 2**: [states traversed; cite S-IDs in sequence]
- **JOIN at**: S-[ID] ([join state name])
- **Join Condition**: AND-join / OR-join -- specify which applies and explain why

---

### Edge Case Enumeration

At least three edge cases distinct from SECTION A exception flows:

> **EC-[N] -- [Edge Case Name]**
> - Triggering Condition: [specific scenario]
> - Why Problematic: [specific reason this falls outside documented handling]
> - Correct Response: R-[ID] ([role name]) -- [specific correct action; name target state or resolution path]

---

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF -- {Topic} lifecycle --> [adjacent process name]**
> - Sending State: S-[ID] / Receiving Process: [name] / Data Payload: [named fields]
> - Expected Acknowledgment: [signal or confirmation] / Failure Mode: [if acknowledgment not received]
> - Owner: R-[ID]

---

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|
| | | | | AT-RISK / ON-TRACK | B-NN (if AT-RISK) |

Rules: AT-RISK = typical duration exceeds SLA target. Every AT-RISK row must carry a Bottleneck
Ref citing a B-NN from Bottleneck Analysis. Minimum 3 annotated rows; at least 1 must be AT-RISK.

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN Cause field must satisfy both Dual-Cite Fail Conditions independently.
>
> **Dual-Cite Fail Condition A** -- Cause field contains no IM-ID literal string (e.g., "IM-01"):
> fails C-39. Verify: search Cause field for "IM-" followed by digits. Absence --> fail.
>
> **Dual-Cite Fail Condition B** -- Cause field contains no R-ID literal string (e.g., "R-01"):
> fails C-39. Verify: search Cause field for "R-" followed by digits. Absence --> fail.
>
> B-IDs assigned here must string-match ALL of: (1) PHASE EXIT GATE `Blocked bottleneck:`
> fields, (2) PHASE ENTRY CONTRACT `Prior phase blocked bottleneck:` in the following phase,
> and (3) EX block `Bottleneck Ref:` fields where non-NONE.
>
> Concrete format example for Evidence field:
> `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`
>
> Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
> Fail condition: A field containing only "see SLA ANALYSIS" or state names without
> AT-RISK row-level S-ID specificity does not satisfy.
>
> **DUAL-LOCATION REQUIREMENTS:**
> (1) Concrete named domain example must appear in BOTH this preamble AND each B-NN per-block
> Evidence hint.
> (2) Labeled axes (`Required format:` / `Fail condition:`) must appear in BOTH this preamble
> AND each B-NN per-block Evidence hint.
>
> **B-NN->Exception Gate Check**: Every declared B-ID below must appear in at least one EX
> block's `Bottleneck Ref:` sub-field across all phases. Dark bottlenecks are gate violations.
>
> Anti-embedding: Declare CHAIN STATUS in its own dedicated top-level section after SLA ANALYSIS.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field AND an Exception Refs field.**

---

**B-01 -- [Bottleneck Name]**

- Cause: [Required: IM-ID literal string (Condition A) AND R-ID literal string (Condition B).
  Example: "IM-01 (manual reconciliation gap) combined with R-02 (GL Manager) period-close
  unavailability -- approval queue at S-05. 'IM-01' satisfies A; 'R-02' satisfies B."]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string --> fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string --> fails C-39
- Impact: [downstream state, SLA node, or adjacent process affected]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-01. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]
- Exception Refs:
  - Required format: `EX-[Phase#][Letter] (Phase [N] -- [Exception Name])`
  - Fail condition: NONE declared here means this is a dark bottleneck -- declared process
    failure mode with no exception-phase trace. Dark bottleneck = gate violation for the
    B-NN->Exception direction. A listed EX block ID that has no matching `Bottleneck Ref:
    B-01` in the cited EX block fails the CHAIN STATUS B-NN->Exception consistency check.
  - [List each EX block identifier whose `Bottleneck Ref:` cites B-01, or NONE.]

---

**B-02 -- [Bottleneck Name]**

- Cause: [Required: IM-ID literal string AND R-ID literal string.]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string --> fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string --> fails C-39
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: [same as B-01]
  - [List each AT-RISK SLA row citing B-02. Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]
- Exception Refs:
  - Required format: `EX-[Phase#][Letter] (Phase [N] -- [Exception Name])`
  - Fail condition: NONE = dark bottleneck (gate violation). Listed EX block ID without
    matching `Bottleneck Ref: B-02` in the cited EX block fails consistency check.
  - [List each EX block identifier whose `Bottleneck Ref:` cites B-02, or NONE.]

---

**Gap Identification**

> MISSING: [step name] -- [rationale: why it belongs; failure mode enabled; which phase;
> which IM-ID it would reduce if present]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

**DIRECTION INVENTORY:**

> The four established traceability directions are enumerated below as a named index declared
> before the direction-level verification entries. Each direction is declared PRESENT or ABSENT
> with a citation to the section or sub-field carrying it. An absent DIRECTION INVENTORY block
> is a FAIL regardless of direction content below. A DIRECTION INVENTORY missing any of the four
> established directions is a FAIL.

| Direction | Status | Carried By |
|-----------|--------|-----------|
| B-NN->Exception | [PRESENT / ABSENT] | [B-NN block `Exception Refs:` field listing EX block IDs; EX block `Bottleneck Ref:` field citing B-ID; verified in CHAIN STATUS `B-NN->Exception` direction below] |
| Phase-exit-sequence | [PRESENT / ABSENT] | [PHASE EXIT GATE `Next phase:` sub-field; string-match to subsequent phase block label; verified in CHAIN STATUS `Phase-exit-sequence` direction below] |
| Baseline->Phase | [PRESENT / ABSENT] | [PHASE ENTRY CONTRACT `IM Reference:` sub-field; INCUMBENT BASELINE `Phase Refs:` back-references per IM-ID row; verified in CHAIN STATUS `Baseline->Phase` direction below] |
| Baseline->Exception | [PRESENT / ABSENT] | [SECTION A EX block `IM Ref:` sub-field citing EXCEPTION BLOCK ARCHITECTURE IM-ID namespace; string-match to INCUMBENT BASELINE IM-IDs; verified in CHAIN STATUS `Baseline->Exception` direction below] |

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA->B): [every AT-RISK SLA row cites a B-ID; enumerate pairs or name gap]
- Backward (B->SLA): [every B-NN Evidence field lists AT-RISK SLA rows; enumerate or name gap]
- Exit gate consistency: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID matches a declared B-NN; name any mismatch]
- Phase-boundary B-NN continuity: [every exit gate B-ID matches next phase's `Prior phase blocked bottleneck:`; list pairs or name break]
- Phase-sequence: [every PHASE ENTRY CONTRACT `Prior phase:` matches preceding phase block label; PHASE 1 carries NONE/INIT; list pairs or name mismatch]
- Phase-exit-sequence: [every PHASE EXIT GATE `Next phase:` matches subsequent phase block label; last phase carries NONE/END; list pairs or name mismatch -- DIRECTION INVENTORY declares PRESENT]
- Exception->B: [every EX block `Bottleneck Ref:` B-ID (non-NONE) matches a declared B-NN; list EX->B-NN pairs or name unresolved block]
- B-NN->Exception: [every declared B-ID has at least one non-NONE entry in its `Exception Refs:` field; each listed EX block ID string-matches an EX block with `Bottleneck Ref:` citing this B-ID; enumerate B-ID->EX pairs; name dark bottlenecks -- DIRECTION INVENTORY declares PRESENT]
- Exception->Role: [every EX block `Role Ref:` R-ID matches ROLE SEQUENCE SCHEDULE primary owner; list EX->R-ID pairs or name mismatch]
- Role->Exception: [every declared R-ID appears in at least one EX block `Role Ref:`; list R-ID->EX pairs; name dark roles]
- Dual-cite status: [every B-NN Cause has both IM-ID and R-ID; name any block missing either]
- Baseline->Phase: [every PHASE ENTRY CONTRACT `IM Reference:` field contains only IM-IDs declared in INCUMBENT BASELINE; list phase->IM-ID pairs; NONE sentinels CLOSED -- DIRECTION INVENTORY declares PRESENT]
- Baseline->Exception: [every SECTION A EX block `IM Ref:` field (per EXCEPTION BLOCK ARCHITECTURE IM-ID namespace, anchored by "see EXCEPTION BLOCK ARCHITECTURE above" hint in each block) contains only IM-IDs declared in INCUMBENT BASELINE or NONE sentinel; list EX->IM-ID pairs; name dark exceptions -- DIRECTION INVENTORY declares PRESENT]
- Phase->Baseline: [for each IM-ID cited in any PHASE ENTRY CONTRACT `IM Reference:` field,
  verify INCUMBENT BASELINE `Phase Refs:` for that IM-ID includes this phase by literal phase
  block identifier; enumerate IM-ID->Phase Refs pairs; name consistency failures; verify all
  NONE sentinels accurate; an IM-ID cited by at least one PHASE ENTRY CONTRACT but carrying NONE
  in `Phase Refs:` is a C-48 consistency violation that reopens the gate]
- Gap (if OPEN): [unresolved direction and unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal name] | SUCCESS | [branch or state that reaches it] |
| [failure terminal name] | FAILURE | [branch or state that reaches it] |
| [cancel terminal name] | CANCEL | [branch or state that reaches it] |

> Completeness check: Every exit branch in every SECTION B state table must reach one of the
> declared terminals. No branch may end at a non-terminal state without `continues-via: S-[ID]`.

---
---

## V-05 -- Combination: Output Format + Lifecycle Emphasis + Phrasing Register (C-51 + C-52 + C-53)

**Variation axis**: Output format + Lifecycle emphasis + Phrasing register -- maximum structural
density for all three R17 criteria. (1) `Return instruction:` labeled sub-field in PHASE GATE
CONTRACT SUMMARY (V-02 axis, C-52). (2) 4-column DIRECTION INVENTORY with per-direction Violation
Check (V-03 axis, C-51). (3) "see EXCEPTION BLOCK ARCHITECTURE above" by full name in `IM Ref:`
hint of every EX block template (V-04 axis, C-53). All three additions are architecturally
independent: C-52 lives in PHASE GATE CONTRACT SUMMARY, C-51 lives in the DIRECTION INVENTORY,
C-53 lives in each EX block `IM Ref:` hint. The additions do not interact structurally.

**Hypothesis**: V-05 is the minimum R17 configuration to achieve C-51, C-52, and C-53
simultaneously with maximum explicitness. Each structural addition is independently necessary
and sufficient for its target criterion: Return instruction scores C-52, per-direction Violation
Check scores C-51, full-name IM Ref back-reference scores C-53. If all three pass and V-01 also
scores 45/45, single-axis results confirm each criterion is independently sufficient via the
baseline's implicit handling. If V-01 scores 42/45, V-05 confirms three-way composition with
45/45 and single-axis variations isolate the missing threshold. Expected: 45/45 = 10.000.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must satisfy both Dual-Cite
> Fail Conditions. Quantified metric must appear before PHASE 1 in document order.
> This section is the inertia reference: IM-IDs assigned here are anchor identifiers for
> (1) `IM Reference:` in every PHASE ENTRY CONTRACT, (2) `IM Ref:` in every SECTION A EX block,
> and (3) `Phase Refs:` back-references declared at the end of this section after all PHASE ENTRY
> CONTRACT blocks are complete. Every exception trace and bottleneck must be traceable back to a
> named IM-ID. The `Phase Refs:` back-references close the Baseline->Phase direction (C-46)
> bidirectionally at the source-row level.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle -- auto-detect from {Topic}]

**Incumbent description**: [1-3 sentences: tools used (spreadsheets, email, phone), handoff
mechanisms, where records are stored, who initiates the process manually. Include the primary
failure point under volume or time pressure.]

**Incumbent failure modes**:

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure -- the one most visible to the domain team] | [daily / per-cycle / per-exception] | [downstream effect on SLA or accuracy] |
| IM-02 | [second distinct failure mode -- different process layer from IM-01] | [frequency] | [downstream effect] |

**Cost of no action**: [Named measure with current-state value or rate, declared before PHASE 1.
Both IM-IDs must be reachable from at least one B-NN Cause field. Example: "Average credit
approval cycle time: 5.8 days vs 3-day SLA -- IM-01 primary driver" or "Manual matching error
rate: 12% per period, IM-02 primary driver."]

**Phase back-references (C-48 -- closes Baseline->Phase bidirectionally at source):**

> After completing all PHASE ENTRY CONTRACT blocks, return here to populate the back-references
> for each IM-ID. Each IM-ID lists every PHASE ENTRY CONTRACT whose `IM Reference:` sub-field
> cites this IM-ID. Enumeration must be consistent with all `IM Reference:` sub-fields by string
> comparison: if a PHASE ENTRY CONTRACT `IM Reference:` cites IM-01, then IM-01 `Phase Refs:`
> must list that phase's literal identifier; if it does not cite IM-01, `Phase Refs:` must not
> list it. IM-IDs with no phase citations carry explicit NONE sentinel. String comparison only --
> no inference. These back-references make each IM-ID row a navigable lookup for Baseline->Phase
> traceability. CHAIN STATUS `Phase->Baseline` direction (Violation Check active per DIRECTION
> INVENTORY) verifies consistency.

- IM-01 Phase Refs: [List every PHASE ENTRY CONTRACT by literal phase block identifier whose
  `IM Reference:` sub-field cites IM-01 (e.g., "PHASE 1 -- Initiation; PHASE 3 -- Approval").
  If no PHASE ENTRY CONTRACT `IM Reference:` cites IM-01, write NONE. String comparison only.]
- IM-02 Phase Refs: [List every PHASE ENTRY CONTRACT whose `IM Reference:` cites IM-02, or NONE.
  Same rules as IM-01 above.]

---

### Role Registry Gate

> GATE BLOCK: Complete before the Role Sequence Schedule and before tracing any state.
> All four anti-generic checks must clear before proceeding.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [domain-specific role] | [named responsibility] |
| R-02 | [domain-specific role] | [named responsibility] |
| R-03 | [domain-specific role] | [named responsibility] |

Anti-generic validation (all four must clear before proceeding):
- [ ] No R-ID entry uses "Approver" without a domain qualifier
- [ ] No R-ID entry uses "Owner" without a named responsibility
- [ ] Each R-ID is referenced by at least one Decision Supplement block, the Role Sequence
      Schedule, and at least one PHASE EXIT GATE Exit verification or Blocked bottleneck field
- [ ] Each declared R-ID appears in at least one EX block's `Role Ref:` sub-field -- R-IDs
      with no observable EX trace are "dark" roles and constitute a gate violation

Role set by process type:
- L2O --> Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P --> Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close --> Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle --> Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Role Sequence Schedule

> Declared after Role Registry Gate and before PHASE 1. Maps each R-ID to owned phases with
> activation triggers, handoff triggers, and parallel windows. B-NN Cause fields must cite
> the blocking R-ID from this schedule (Dual-Cite Fail Condition B). R-IDs in EX block
> `Role Ref:` must match the schedule entry for the enclosing phase. Every declared R-ID
> must appear in at least one EX block Role Ref -- the Role Registry Gate fourth check enforces this.

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior-process artifact -- not "Start"] | [specific completion condition] | R-[ID] or NONE | [concurrent window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1 -- name the artifact] | [completion condition] | R-[ID] or NONE | [concurrent activity or NONE] |

Rules: Every phase has a Primary Owner. Activation Trigger for Phase 1 must name an external
event or prior-process artifact. Every R-ID here must match a Role Registry Gate entry.

---

### Phase Gate Contract Summary

> **DECLARED UNIT: THREE-FIELD PHASE GATE CONTRACT**
>
> This document uses a three-field phase gate contract. All three fields are named here as a
> declared unit before PHASE 1 is traced. Every phase block must carry all three fields in
> their designated structural locations. A fourth field (`IM Reference:`) augments PHASE ENTRY
> CONTRACTs with Baseline->Phase traceability; it is not part of the three-field gate contract
> but is required in every PHASE ENTRY CONTRACT block.
>
> | Field Name | Location | Value Type | Traceability Direction |
> |------------|----------|------------|----------------------|
> | `Prior phase:` | PHASE ENTRY CONTRACT | Phase label (e.g., "PHASE 1 -- Initiation") | Phase->Phase, backward (entry side) |
> | `Prior phase blocked bottleneck:` | PHASE ENTRY CONTRACT | B-ID (e.g., "B-01") | B-NN boundary continuity, entry side |
> | `Next phase:` | PHASE EXIT GATE | Phase label (e.g., "PHASE 2 -- Credit Review") | Phase->Phase, forward (exit side) |
>
> **ORTHOGONALITY DECLARATION:**
> `Prior phase blocked bottleneck:` carries a B-ID (string pattern: "B-" followed by digits,
> e.g., "B-01"). `Next phase:` carries a Phase label (string pattern: "PHASE N -- [Name]" or
> NONE/END sentinel). These two fields carry orthogonal value types independently verifiable
> by string comparison. No inference required -- patterns are non-overlapping by construction.
>
> `Prior phase:` and `Next phase:` form a symmetric bidirectional Phase->Phase pair.
> `Prior phase blocked bottleneck:` is orthogonal to both -- B-ID, not Phase label.
>
> **Return instruction:** After completing all PHASE ENTRY CONTRACT blocks in this document,
> return to INCUMBENT BASELINE and populate each row's `Phase Refs:` sub-field. Target table:
> INCUMBENT BASELINE. Target sub-field: `Phase Refs:`. Trigger condition: all PHASE ENTRY
> CONTRACT blocks for this document authored. This instruction converts Phase Refs:
> back-annotation from an implicit co-authoring step into a named, positionally verifiable
> workflow step: PHASE GATE CONTRACT SUMMARY completion triggers back-annotation at the source
> table. Absence of `Phase Refs:` population after all phases are traced is a C-48 failure
> regardless of whether PHASE ENTRY CONTRACT `IM Reference:` sub-fields are correct.
>
> CHAIN STATUS verifies three gate-contract directions:
> - `Phase-sequence`: every `Prior phase:` string-matches the preceding phase block label
> - `Phase-exit-sequence`: every `Next phase:` string-matches the subsequent phase block label
> - `Phase-boundary B-NN continuity`: every exit gate `Blocked bottleneck:` B-ID string-matches
>   the next phase's `Prior phase blocked bottleneck:` field

---

### Phase Structure

For each phase in the lifecycle, produce the following five blocks in document order. All three
Phase Gate Contract fields must be populated in every phase block. `IM Reference:` must
additionally appear in every PHASE ENTRY CONTRACT. After all phases are complete, return to
INCUMBENT BASELINE to populate `Phase Refs:` back-references per the Return instruction above.

---

**PHASE [N] -- [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Phase Gate Contract fields 1 and 2 live here; field 3 (`Next phase:`) lives in PHASE EXIT GATE.
> `IM Reference:` is a fourth required sub-field providing Baseline->Phase traceability. Its
> content will be cross-referenced by INCUMBENT BASELINE `Phase Refs:` back-references per the
> Return instruction in PHASE GATE CONTRACT SUMMARY -- populate accurately so the bidirectional
> chain is consistent by string comparison. All four sub-fields are independently verifiable by
> string comparison.

- Entry Condition: [specific named artifact from prior phase's Required outputs]
- Pre-condition check: R-[ID] ([role name -- must match Role Sequence Schedule primary owner]) -- [verification method]
- Blocking condition: [state entered and role notified if entry condition not met]
- Prior phase: [Literal identifier of preceding phase block, e.g., "PHASE 1 -- Initiation".
  Phase 1: NONE or INIT sentinel. Must string-match preceding phase block label. Format: "PHASE N -- [Name]".]
- Prior phase blocked bottleneck: [B-ID from prior exit gate `Blocked bottleneck:` or NONE
  or N/A for Phase 1. Format: "B-NN". Must string-match prior exit gate AND B-NN block identifier.
  This field carries a B-ID -- NOT a Phase label. Do not conflate with `Prior phase:`.]
- IM Reference: [List every IM-ID from INCUMBENT BASELINE whose failure mode represents an
  active risk entering this phase. Use exact IM-ID identifiers as declared in the INCUMBENT
  BASELINE table (e.g., "IM-01, IM-02"). If no incumbent failure mode is an active risk at
  this phase's entry point, write NONE. IM-IDs must literal-match INCUMBENT BASELINE table
  identifiers -- string comparison only, no inference. INCUMBENT BASELINE `Phase Refs:` for
  each cited IM-ID will list this phase's literal identifier per the Return instruction in PHASE
  GATE CONTRACT SUMMARY -- ensure phase block label is consistent with `Phase Refs:` entries.
  Example: "IM-01 (manual reconciliation gap -- active entry risk: pre-condition artifact
  produced manually and vulnerable to IM-01 failure mode before this phase begins)."]

**SECTION A -- EXCEPTION TRACES**

> **EXCEPTION BLOCK ARCHITECTURE:**
> Each EX block in this document carries three independent citation sub-fields, declared here
> as a named unit. All three sub-fields must appear in every EX block across all phases.
> Missing any sub-field in any EX block is a detectable format violation verifiable from this
> declaration without per-block traversal.
>
> | Sub-field | Namespace | ID Pattern | Traceability Direction |
> |-----------|-----------|------------|----------------------|
> | `Role Ref:` | R-ID namespace | "R-" followed by digits (e.g., "R-01") | Role->Exception (C-40): cites the phase's ROLE SEQUENCE SCHEDULE primary owner |
> | `Bottleneck Ref:` | B-ID namespace | "B-" followed by digits (e.g., "B-01") | B-NN->Exception (C-42): cites the bottleneck that enabled this exception |
> | `IM Ref:` | IM-ID namespace | "IM-" followed by digits (e.g., "IM-01") | Baseline->Exception (C-47): cites the INCUMBENT BASELINE failure mode this exception traces |
>
> **ORTHOGONALITY DECLARATION:** The three ID namespaces are distinct and independently
> verifiable by string comparison. "R-[digits]", "B-[digits]", and "IM-[digits]" are
> non-overlapping string patterns by construction: no R-ID can be mistaken for a B-ID or
> IM-ID; no B-ID can be mistaken for an R-ID or IM-ID; no IM-ID can be mistaken for an
> R-ID or B-ID. The three citation directions are orthogonal: an R-ID in `Bottleneck Ref:`
> is a detectable format violation; a B-ID in `IM Ref:` is a detectable format violation.
> EX block completeness is format-verifiable from this declaration without per-block traversal.

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] -- [Exception Name]**
> - Trigger: [specific condition -- name the state, threshold breach, or missing input]
> - Trace: [path of states from trigger to resolution or terminal; cite S-IDs in sequence]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason this failure mode matters]
> - Bottleneck Ref: [B-NN that enabled this exception, or NONE. B-ID must string-match a
>   Bottleneck Analysis identifier. The B-NN block's `Exception Refs:` field must list this
>   EX block ID if Bottleneck Ref is non-NONE -- populate accurately for chain consistency.
>   NONE only if no declared bottleneck was causal. Namespace: B-ID (see architecture above).]
> - Role Ref: [R-ID of the ROLE SEQUENCE SCHEDULE primary owner for this phase. Literal R-ID
>   matching the schedule's Primary Owner entry for the enclosing phase. Free-text without
>   R-ID fails. Namespace: R-ID (see architecture above).]
> - IM Ref: [IM-ID from INCUMBENT BASELINE whose failure mode this exception traces, or NONE.
>   Use exact IM-ID identifier as declared in the INCUMBENT BASELINE table (e.g., "IM-01").
>   This sub-field completes the triple-citation architecture: `Role Ref:` links to schedule
>   (C-40); `Bottleneck Ref:` links to B-NN (C-42); `IM Ref:` links to INCUMBENT BASELINE
>   (C-47). Together they make this EX block the convergence point for Role->Exception,
>   B-NN<->Exception, and Baseline<->Exception traceability chains simultaneously.
>   NONE if no incumbent baseline failure mode is directly traceable to this exception.
>   String comparison only -- IM-ID must literal-match INCUMBENT BASELINE table identifier.
>   Namespace: IM-ID (see EXCEPTION BLOCK ARCHITECTURE above).
>   Example: "IM-01 -- this exception is the process-visible manifestation of the incumbent
>   manual reconciliation failure mode entering Phase 2."]

Minimum 1 exception trace per phase; 3 total minimum.
Every declared R-ID in the Role Registry Gate must appear in at least one EX block Role Ref.
Role Ref, Bottleneck Ref, and IM Ref are independent sub-fields; populate all three for every EX block.

**SECTION B -- STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules:
- Every state must have a named Entry Condition. "Ready" or "Previous step complete" fails.
- Every Exit must reference a destination S-ID or carry the label TERMINAL.
- Type values: NORMAL / DECISION / PARALLEL-FORK / PARALLEL-JOIN / EXCEPTION / TERMINAL

**Decision Supplement Blocks** (one per DECISION-type state in this phase):

> **DS-[S-ID] -- [State Name]**
> - Condition: [rule or threshold evaluated]; Owner: R-[ID]; Branch A: --> S-[ID];
>   Branch B: --> S-[ID] or TERMINAL; Fallback: [action if condition cannot be evaluated]

**PHASE EXIT GATE**

> Phase Gate Contract field 3 lives here: `Next phase:` (Phase label, forward).
> `Blocked bottleneck:` carries a B-ID. These two sub-fields are orthogonal -- see PHASE GATE
> CONTRACT SUMMARY above.

- Exit Condition: [what the phase must produce to be complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name -- must match Role Sequence Schedule primary owner]) confirms all outputs present
- Blocking condition: [re-entry path or escalation if outputs absent]
- Blocked bottleneck: [B-NN or NONE. Must string-match Bottleneck Analysis identifier AND
  next phase's `Prior phase blocked bottleneck:`. Format: "B-NN" -- a B-ID, not a Phase label.]
- Next phase: [Literal identifier of the subsequent phase block. Last phase: NONE or END.
  Format: "PHASE N -- [Name]". This field carries a Phase label -- not a B-ID. See PHASE GATE
  CONTRACT SUMMARY orthogonality declaration.]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID] ([state name])
- **Branch 1**: [states traversed; cite S-IDs in sequence]
- **Branch 2**: [states traversed; cite S-IDs in sequence]
- **JOIN at**: S-[ID] ([join state name])
- **Join Condition**: AND-join / OR-join -- specify which applies and explain why

---

### Edge Case Enumeration

At least three edge cases distinct from SECTION A exception flows:

> **EC-[N] -- [Edge Case Name]**
> - Triggering Condition: [specific scenario]
> - Why Problematic: [specific reason this falls outside documented handling]
> - Correct Response: R-[ID] ([role name]) -- [specific correct action; name target state or resolution path]

---

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF -- {Topic} lifecycle --> [adjacent process name]**
> - Sending State: S-[ID] / Receiving Process: [name] / Data Payload: [named fields]
> - Expected Acknowledgment: [signal or confirmation] / Failure Mode: [if acknowledgment not received]
> - Owner: R-[ID]

---

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|
| | | | | AT-RISK / ON-TRACK | B-NN (if AT-RISK) |

Rules: AT-RISK = typical duration exceeds SLA target. Every AT-RISK row must carry a Bottleneck
Ref citing a B-NN from Bottleneck Analysis. Minimum 3 annotated rows; at least 1 must be AT-RISK.

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN Cause field must satisfy both Dual-Cite Fail Conditions independently.
>
> **Dual-Cite Fail Condition A** -- Cause field contains no IM-ID literal string (e.g., "IM-01"):
> fails C-39. Verify: search Cause field for "IM-" followed by digits. Absence --> fail.
>
> **Dual-Cite Fail Condition B** -- Cause field contains no R-ID literal string (e.g., "R-01"):
> fails C-39. Verify: search Cause field for "R-" followed by digits. Absence --> fail.
>
> B-IDs assigned here must string-match ALL of: (1) PHASE EXIT GATE `Blocked bottleneck:`
> fields, (2) PHASE ENTRY CONTRACT `Prior phase blocked bottleneck:` in the following phase,
> and (3) EX block `Bottleneck Ref:` fields where non-NONE.
>
> Concrete format example for Evidence field:
> `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`
>
> Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
> Fail condition: A field containing only "see SLA ANALYSIS" or state names without
> AT-RISK row-level S-ID specificity does not satisfy.
>
> **DUAL-LOCATION REQUIREMENTS:**
> (1) Concrete named domain example must appear in BOTH this preamble AND each B-NN per-block
> Evidence hint.
> (2) Labeled axes (`Required format:` / `Fail condition:`) must appear in BOTH this preamble
> AND each B-NN per-block Evidence hint.
>
> **B-NN->Exception Gate Check**: Every declared B-ID below must appear in at least one EX
> block's `Bottleneck Ref:` sub-field across all phases. A B-ID absent from all EX blocks is
> a "dark bottleneck" -- declared failure mode with no exception-phase trace. Dark bottlenecks
> are gate violations. Report result in CHAIN STATUS `B-NN->Exception` direction -- Violation
> Check in DIRECTION INVENTORY will verify bidirectional consistency.
>
> Anti-embedding: Declare CHAIN STATUS in its own dedicated top-level section after SLA ANALYSIS.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field AND an Exception Refs field.**

---

**B-01 -- [Bottleneck Name]**

- Cause: [Required: IM-ID literal string (Condition A) AND R-ID literal string (Condition B).
  Example: "IM-01 (manual reconciliation gap) combined with R-02 (GL Manager) period-close
  unavailability -- approval queue at S-05. 'IM-01' satisfies A; 'R-02' satisfies B."]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string --> fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string --> fails C-39
- Impact: [downstream state, SLA node, or adjacent process affected]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-01. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]
- Exception Refs:
  - Required format: `EX-[Phase#][Letter] (Phase [N] -- [Exception Name])`
  - Fail condition: NONE declared here means this is a dark bottleneck -- declared process
    failure mode with no exception-phase trace. Dark bottleneck = gate violation for the
    B-NN->Exception direction (Violation Check in DIRECTION INVENTORY). A listed EX block ID
    that has no matching `Bottleneck Ref: B-01` in the cited EX block fails the consistency check.
  - [List each EX block identifier whose `Bottleneck Ref:` cites B-01, or NONE.]

---

**B-02 -- [Bottleneck Name]**

- Cause: [Required: IM-ID literal string AND R-ID literal string.]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string --> fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string --> fails C-39
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: [same as B-01]
  - [List each AT-RISK SLA row citing B-02. Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]
- Exception Refs:
  - Required format: `EX-[Phase#][Letter] (Phase [N] -- [Exception Name])`
  - Fail condition: NONE = dark bottleneck (gate violation). Listed EX block ID without
    matching `Bottleneck Ref: B-02` in the cited EX block fails consistency check.
  - [List each EX block identifier whose `Bottleneck Ref:` cites B-02, or NONE.]

---

**Gap Identification**

> MISSING: [step name] -- [rationale: why it belongs; failure mode enabled; which phase;
> which IM-ID it would reduce if present]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

**DIRECTION INVENTORY:**

> The four established traceability directions are enumerated below as a named index declared
> before the direction-level verification entries. Each direction declared PRESENT carries both
> a Carried By citation AND a Violation Check -- a declarative string-comparison condition naming
> the source field, the target field, and the exact inconsistency pattern that would reopen the
> gate. CHAIN STATUS remains CLOSED only when all declared direction-level violation conditions
> evaluate to no-conflict. A single violation check firing reopens the gate regardless of PRESENT
> declarations. Directions declared NOT-APPLICABLE are exempt from violation checks. Absent
> DIRECTION INVENTORY = FAIL. Missing any of the four established directions = FAIL. Missing
> Violation Check for any PRESENT direction = FAIL.

| Direction | Status | Carried By | Violation Check |
|-----------|--------|-----------|----------------|
| B-NN->Exception | [PRESENT / ABSENT] | [B-NN block `Exception Refs:` field listing EX block IDs; EX block `Bottleneck Ref:` field citing B-ID; verified in CHAIN STATUS `B-NN->Exception` direction below] | Source: B-NN `Exception Refs:` field. Target: EX block `Bottleneck Ref:` field. Inconsistency: a B-ID listed in a B-NN block's `Exception Refs:` that does not appear in any EX block's `Bottleneck Ref:` citing that B-ID, OR an EX block `Bottleneck Ref:` citing a B-ID whose corresponding B-NN `Exception Refs:` does not list that EX block ID, reopens the gate. |
| Phase-exit-sequence | [PRESENT / ABSENT] | [PHASE EXIT GATE `Next phase:` sub-field; string-match to subsequent phase block label; verified in CHAIN STATUS `Phase-exit-sequence` direction below] | Source: PHASE EXIT GATE `Next phase:` field. Target: literal label of the subsequent PHASE block. Inconsistency: `Next phase:` string does not string-match the subsequent phase block label (e.g., "Next phase: PHASE 3 -- Approval" but next declared block is "PHASE 3 -- Review"), reopens the gate. Last phase must carry NONE or END sentinel -- any other value is an inconsistency. |
| Baseline->Phase | [PRESENT / ABSENT] | [PHASE ENTRY CONTRACT `IM Reference:` sub-field; INCUMBENT BASELINE `Phase Refs:` back-references per IM-ID row (populated per Return instruction in PHASE GATE CONTRACT SUMMARY); verified in CHAIN STATUS `Baseline->Phase` direction below] | Source: PHASE ENTRY CONTRACT `IM Reference:` field. Target: INCUMBENT BASELINE `Phase Refs:` field for each cited IM-ID. Inconsistency: an IM-ID appearing in `IM Reference:` of any PHASE ENTRY CONTRACT absent from the `Phase Refs:` of the corresponding INCUMBENT BASELINE row (Return instruction executed but Phase Refs not populated for this IM-ID), OR an IM-ID in an INCUMBENT BASELINE `Phase Refs:` field not appearing in the `IM Reference:` of the cited phase's PHASE ENTRY CONTRACT, reopens the gate. An IM-ID with NONE in `Phase Refs:` cited by any PHASE ENTRY CONTRACT `IM Reference:` is an inconsistency. |
| Baseline->Exception | [PRESENT / ABSENT] | [SECTION A EX block `IM Ref:` sub-field (per EXCEPTION BLOCK ARCHITECTURE IM-ID namespace; each EX block hint anchored with "see EXCEPTION BLOCK ARCHITECTURE above"); string-match to INCUMBENT BASELINE IM-IDs; verified in CHAIN STATUS `Baseline->Exception` direction below] | Source: SECTION A EX block `IM Ref:` field. Target: INCUMBENT BASELINE IM-ID table. Inconsistency: an IM-ID string appearing in any EX block `IM Ref:` that does not match any IM-ID declared in the INCUMBENT BASELINE table (string pattern "IM-" followed by digits not found in INCUMBENT BASELINE IM-ID column), reopens the gate. NONE sentinels are exempt. |

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA->B): [every AT-RISK SLA row cites a B-ID; enumerate pairs or name gap]
- Backward (B->SLA): [every B-NN Evidence field lists AT-RISK SLA rows; enumerate or name gap]
- Exit gate consistency: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID matches a declared B-NN; name any mismatch]
- Phase-boundary B-NN continuity: [every exit gate B-ID matches next phase's `Prior phase blocked bottleneck:`; list pairs or name break]
- Phase-sequence: [every PHASE ENTRY CONTRACT `Prior phase:` matches preceding phase block label; PHASE 1 carries NONE/INIT; list pairs or name mismatch]
- Phase-exit-sequence: [every PHASE EXIT GATE `Next phase:` matches subsequent phase block label; last phase carries NONE/END; list pairs or name mismatch -- Violation Check per DIRECTION INVENTORY above active: mismatch reopens gate]
- Exception->B: [every EX block `Bottleneck Ref:` B-ID (non-NONE) matches a declared B-NN; list EX->B-NN pairs or name unresolved block]
- B-NN->Exception: [every declared B-ID has at least one non-NONE entry in its `Exception Refs:` field; each listed EX block ID string-matches an EX block with `Bottleneck Ref:` citing this B-ID; enumerate B-ID->EX pairs; name dark bottlenecks and consistency failures -- Violation Check per DIRECTION INVENTORY above active]
- Exception->Role: [every EX block `Role Ref:` R-ID matches ROLE SEQUENCE SCHEDULE primary owner; list EX->R-ID pairs or name mismatch]
- Role->Exception: [every declared R-ID appears in at least one EX block `Role Ref:`; list R-ID->EX pairs; name dark roles]
- Dual-cite status: [every B-NN Cause has both IM-ID and R-ID; name any block missing either]
- Baseline->Phase: [every PHASE ENTRY CONTRACT `IM Reference:` field contains only IM-IDs declared in INCUMBENT BASELINE; list phase->IM-ID pairs; NONE sentinels CLOSED for this direction; name any phase whose IM Reference contains a non-declared IM-ID or is absent -- Violation Check per DIRECTION INVENTORY above active: IM-ID in IM Reference absent from Phase Refs reopens gate]
- Baseline->Exception: [every SECTION A EX block `IM Ref:` field (anchored by "see EXCEPTION BLOCK ARCHITECTURE above" in each EX block hint) contains only IM-IDs declared in INCUMBENT BASELINE or NONE sentinel; list EX->IM-ID pairs; name dark exceptions -- Violation Check per DIRECTION INVENTORY above active: undeclared IM-ID in IM Ref reopens gate]
- Phase->Baseline: [bidirectional complement to Baseline->Phase; for each IM-ID cited in any
  PHASE ENTRY CONTRACT `IM Reference:` field, verify INCUMBENT BASELINE `Phase Refs:` for that
  IM-ID includes this phase by literal phase block identifier; enumerate IM-ID->Phase Refs pairs;
  name any phase whose `IM Reference:` cites an IM-ID whose `Phase Refs:` does not list that
  phase (consistency failure -- violates Baseline->Phase Violation Check and Return instruction);
  verify all NONE sentinels are accurate -- an IM-ID with NONE in `Phase Refs:` must not be
  cited by any PHASE ENTRY CONTRACT `IM Reference:` field; an IM-ID cited by at least one PHASE
  ENTRY CONTRACT but carrying NONE in `Phase Refs:` is a C-48 consistency violation that
  reopens the gate]
- Gap (if OPEN): [unresolved direction and unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal name] | SUCCESS | [branch or state that reaches it] |
| [failure terminal name] | FAILURE | [branch or state that reaches it] |
| [cancel terminal name] | CANCEL | [branch or state that reaches it] |

> Completeness check: Every exit branch in every SECTION B state table must reach one of the
> declared terminals. No branch may end at a non-terminal state without `continues-via: S-[ID]`.

---
