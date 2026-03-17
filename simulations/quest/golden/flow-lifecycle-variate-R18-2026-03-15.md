# flow-lifecycle -- Round 18 Variations (Rubric v18)

**Rubric version**: v18
**Criteria count**: 48 (C-39 through C-56, plus inherited C-01 through C-38 structure)
**Ceiling**: 48/48 = 10.000
**New v18 criteria**: C-54 (CHAIN STATUS Closed Derivation Claim), C-55 (Phase-to-Baseline Violation Check Return Instruction Cross-Reference), C-56 (EX Block All-Citation-Hints Architecture Back-Reference)
**Baseline**: R17 V-05 scores 42/48 under v18 (C-54/C-55/C-56 all fail)

### R17 Retrospective -- Expected Scores Under v18

| Variation | Axis | C-54 | C-55 | C-56 | Expected Score (v18) |
|-----------|------|:----:|:----:|:----:|----------------------|
| V-01 | Role Sequence (R17 V-05 baseline floor, no R18 additions) | FAIL | FAIL | FAIL | 42/48 = 8.750 |
| V-02 | Output Format (adds C-54 Derivation Claim only) | PASS | FAIL | FAIL | 43/48 = 8.958 |
| V-03 | Lifecycle Emphasis (adds C-55 Return instruction cross-ref only) | FAIL | PASS | FAIL | 43/48 = 8.958 |
| V-04 | Phrasing Register (adds C-56 all-hints full-name back-ref only) | FAIL | FAIL | PASS | 43/48 = 8.958 |
| V-05 | Output Format + Lifecycle Emphasis + Phrasing Register (all three) | PASS | PASS | PASS | 48/48 = 10.000 |

---

## V-01 -- Axis: Role Sequence (R17 V-05 Baseline, R18 Floor)

**Variation axis**: Role sequence -- reproduces R17 V-05 prompt body verbatim with no R18 additions. Establishes the 42/48 floor under v18 rubric. C-54, C-55, and C-56 all fail because (a) no DERIVATION CLAIM block in CHAIN STATUS, (b) no Return instruction cross-reference in Baseline->Phase Violation Check, and (c) `Bottleneck Ref:` and `Role Ref:` hints say "see architecture above" rather than "see EXCEPTION BLOCK ARCHITECTURE above".
**Hypothesis**: 42/48 = 8.750 under v18. All criteria through C-53 pass (same as R17 V-05 golden). C-54 fails (no derivation claim). C-55 fails (no Return instruction citation in Baseline->Phase Violation Check). C-56 fails (two of three hints use abbreviated back-reference).

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
---
## V-02 -- Axis: Output Format (CHAIN STATUS Derivation Claim, C-54 Target)

**Variation axis**: Output format -- adds the DERIVATION CLAIM block immediately before the `CHAIN STATUS: [CLOSED / OPEN]` declaration. All other content is byte-for-byte identical to V-01. C-54 now passes; C-55 and C-56 still fail.
**Hypothesis**: 43/48 = 8.958 under v18. C-54 passes (explicit DERIVATION CLAIM block enumerates all four PRESENT directions with Violation Check evaluation results and derives CLOSED from the complete record). C-55 fails (Baseline->Phase Violation Check still lacks Return instruction cross-reference). C-56 fails (Bottleneck Ref and Role Ref hints still use abbreviated "see architecture above").

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

**DERIVATION CLAIM:**
> For CHAIN STATUS: CLOSED to be asserted, each direction declared PRESENT in DIRECTION
> INVENTORY must evaluate to NO CONFLICT through its Violation Check. The enumeration below
> lists every PRESENT direction, its Violation Check evaluation result, and derives CLOSED
> from the complete per-direction record. Absent derivation claim is a fail even when
> per-direction Violation Checks are well-formed and CHAIN STATUS: CLOSED is declared.
> A derivation claim omitting any PRESENT direction is a fail. NOT-APPLICABLE directions exempt.

- B-NN->Exception: Violation Check evaluated -- [NO CONFLICT / CONFLICT: describe mismatch]
- Phase-exit-sequence: Violation Check evaluated -- [NO CONFLICT / CONFLICT: describe mismatch]
- Baseline->Phase: Violation Check evaluated -- [NO CONFLICT / CONFLICT: describe mismatch]
- Baseline->Exception: Violation Check evaluated -- [NO CONFLICT / CONFLICT: describe mismatch]

Derivation: All four PRESENT directions evaluate to NO CONFLICT per Violation Checks above.
CHAIN STATUS: CLOSED is logically derived from this complete per-direction evaluation record.
A single CONFLICT in any direction above produces CHAIN STATUS: OPEN regardless of other declarations.

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
---
## V-03 -- Axis: Lifecycle Emphasis (Phase->Baseline Violation Check Cross-Reference, C-55 Target)

**Variation axis**: Lifecycle emphasis -- appends the Return instruction cross-reference sentence to the Baseline->Phase Violation Check cell in DIRECTION INVENTORY. All other content is byte-for-byte identical to V-01. C-55 now passes; C-54 and C-56 still fail.
**Hypothesis**: 43/48 = 8.958 under v18. C-55 passes (Baseline->Phase Violation Check now explicitly cites `Return instruction:` sub-field in PHASE GATE CONTRACT SUMMARY as the authoring mechanism that maintains consistency). C-54 fails (no DERIVATION CLAIM block). C-56 fails (two of three hints use abbreviated back-reference).

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
| Baseline->Phase | [PRESENT / ABSENT] | [PHASE ENTRY CONTRACT `IM Reference:` sub-field; INCUMBENT BASELINE `Phase Refs:` back-references per IM-ID row (populated per Return instruction in PHASE GATE CONTRACT SUMMARY); verified in CHAIN STATUS `Baseline->Phase` direction below] | Source: PHASE ENTRY CONTRACT `IM Reference:` field. Target: INCUMBENT BASELINE `Phase Refs:` field for each cited IM-ID. Inconsistency: an IM-ID appearing in `IM Reference:` of any PHASE ENTRY CONTRACT absent from the `Phase Refs:` of the corresponding INCUMBENT BASELINE row (Return instruction executed but Phase Refs not populated for this IM-ID), OR an IM-ID in an INCUMBENT BASELINE `Phase Refs:` field not appearing in the `IM Reference:` of the cited phase's PHASE ENTRY CONTRACT, reopens the gate. An IM-ID with NONE in `Phase Refs:` cited by any PHASE ENTRY CONTRACT `IM Reference:` is an inconsistency. Consistency maintained by `Return instruction:` sub-field in PHASE GATE CONTRACT SUMMARY -- that labeled instruction triggers the `Phase Refs:` back-annotation workflow step; correct execution of the Return instruction prevents the IM-ID/Phase Refs inconsistency pattern from arising. |
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
---
## V-04 -- Axis: Phrasing Register (All-Hints Architecture Back-Reference, C-56 Target)

**Variation axis**: Phrasing register -- changes `Bottleneck Ref:` and `Role Ref:` hint suffix from "see architecture above" to "see EXCEPTION BLOCK ARCHITECTURE above". `IM Ref:` hint already had the full name (C-53 pass, unchanged). All other content is byte-for-byte identical to V-01. C-56 now passes; C-54 and C-55 still fail.
**Hypothesis**: 43/48 = 8.958 under v18. C-56 passes (all three citation hints -- Role Ref, Bottleneck Ref, IM Ref -- now carry explicit inline back-reference to "EXCEPTION BLOCK ARCHITECTURE" by full name). C-54 fails (no DERIVATION CLAIM block). C-55 fails (no Return instruction citation in Baseline->Phase Violation Check).

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
>   NONE only if no declared bottleneck was causal. Namespace: B-ID (see EXCEPTION BLOCK ARCHITECTURE above).]
> - Role Ref: [R-ID of the ROLE SEQUENCE SCHEDULE primary owner for this phase. Literal R-ID
>   matching the schedule's Primary Owner entry for the enclosing phase. Free-text without
>   R-ID fails. Namespace: R-ID (see EXCEPTION BLOCK ARCHITECTURE above).]
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
---
## V-05 -- Axis: Combination: Output Format + Lifecycle Emphasis + Phrasing Register (C-54 + C-55 + C-56)

**Variation axis**: Combination -- applies all three structural changes (C-54 DERIVATION CLAIM + C-55 Return instruction cross-reference + C-56 all-hints full-name back-reference) simultaneously. Everything else is byte-for-byte identical to V-01. All three new v18 criteria pass.
**Hypothesis**: 48/48 = 10.000 under v18. C-54 passes (DERIVATION CLAIM block present, enumerates all four PRESENT directions). C-55 passes (Baseline->Phase Violation Check cites `Return instruction:` in PHASE GATE CONTRACT SUMMARY). C-56 passes (all three EX block citation hints carry full "EXCEPTION BLOCK ARCHITECTURE" back-reference). All prior criteria through C-53 continue to pass unchanged.

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
>   NONE only if no declared bottleneck was causal. Namespace: B-ID (see EXCEPTION BLOCK ARCHITECTURE above).]
> - Role Ref: [R-ID of the ROLE SEQUENCE SCHEDULE primary owner for this phase. Literal R-ID
>   matching the schedule's Primary Owner entry for the enclosing phase. Free-text without
>   R-ID fails. Namespace: R-ID (see EXCEPTION BLOCK ARCHITECTURE above).]
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
| Baseline->Phase | [PRESENT / ABSENT] | [PHASE ENTRY CONTRACT `IM Reference:` sub-field; INCUMBENT BASELINE `Phase Refs:` back-references per IM-ID row (populated per Return instruction in PHASE GATE CONTRACT SUMMARY); verified in CHAIN STATUS `Baseline->Phase` direction below] | Source: PHASE ENTRY CONTRACT `IM Reference:` field. Target: INCUMBENT BASELINE `Phase Refs:` field for each cited IM-ID. Inconsistency: an IM-ID appearing in `IM Reference:` of any PHASE ENTRY CONTRACT absent from the `Phase Refs:` of the corresponding INCUMBENT BASELINE row (Return instruction executed but Phase Refs not populated for this IM-ID), OR an IM-ID in an INCUMBENT BASELINE `Phase Refs:` field not appearing in the `IM Reference:` of the cited phase's PHASE ENTRY CONTRACT, reopens the gate. An IM-ID with NONE in `Phase Refs:` cited by any PHASE ENTRY CONTRACT `IM Reference:` is an inconsistency. Consistency maintained by `Return instruction:` sub-field in PHASE GATE CONTRACT SUMMARY -- that labeled instruction triggers the `Phase Refs:` back-annotation workflow step; correct execution of the Return instruction prevents the IM-ID/Phase Refs inconsistency pattern from arising. |
| Baseline->Exception | [PRESENT / ABSENT] | [SECTION A EX block `IM Ref:` sub-field (per EXCEPTION BLOCK ARCHITECTURE IM-ID namespace; each EX block hint anchored with "see EXCEPTION BLOCK ARCHITECTURE above"); string-match to INCUMBENT BASELINE IM-IDs; verified in CHAIN STATUS `Baseline->Exception` direction below] | Source: SECTION A EX block `IM Ref:` field. Target: INCUMBENT BASELINE IM-ID table. Inconsistency: an IM-ID string appearing in any EX block `IM Ref:` that does not match any IM-ID declared in the INCUMBENT BASELINE table (string pattern "IM-" followed by digits not found in INCUMBENT BASELINE IM-ID column), reopens the gate. NONE sentinels are exempt. |

**DERIVATION CLAIM:**
> For CHAIN STATUS: CLOSED to be asserted, each direction declared PRESENT in DIRECTION
> INVENTORY must evaluate to NO CONFLICT through its Violation Check. The enumeration below
> lists every PRESENT direction, its Violation Check evaluation result, and derives CLOSED
> from the complete per-direction record. Absent derivation claim is a fail even when
> per-direction Violation Checks are well-formed and CHAIN STATUS: CLOSED is declared.
> A derivation claim omitting any PRESENT direction is a fail. NOT-APPLICABLE directions exempt.

- B-NN->Exception: Violation Check evaluated -- [NO CONFLICT / CONFLICT: describe mismatch]
- Phase-exit-sequence: Violation Check evaluated -- [NO CONFLICT / CONFLICT: describe mismatch]
- Baseline->Phase: Violation Check evaluated -- [NO CONFLICT / CONFLICT: describe mismatch]
- Baseline->Exception: Violation Check evaluated -- [NO CONFLICT / CONFLICT: describe mismatch]

Derivation: All four PRESENT directions evaluate to NO CONFLICT per Violation Checks above.
CHAIN STATUS: CLOSED is logically derived from this complete per-direction evaluation record.
A single CONFLICT in any direction above produces CHAIN STATUS: OPEN regardless of other declarations.

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
---
