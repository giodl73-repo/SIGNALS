# flow-lifecycle -- Round 16 Variations (Rubric v16)

**Rubric**: v16 · 50 criteria (42 aspirational) · Ceiling entering R16: 42/42
(R15 V-05 achieved 42/42 retroactive score under v16; C-48/C-49/C-50 signals implicitly present
via `Phase Refs:` inference from `IM Reference:` sub-fields, triple-citation co-presence, and
multi-direction CHAIN STATUS content.)

**Open criteria entering R16**: C-48, C-49, C-50 -- all three implicitly triggered by R15 V-05
but never explicitly named as required structural sub-fields in their canonical locations. R16
escalates all three to explicit named instructions: `Phase Refs:` in INCUMBENT BASELINE rows
(C-48), EXCEPTION BLOCK ARCHITECTURE header in SECTION A (C-49), DIRECTION INVENTORY block at
CHAIN STATUS opening (C-50).

**Evidence from R15 excellence (C-48, C-49, C-50):**

- **C-48 signal**: R15 V-05 placed `IM Reference:` in every PHASE ENTRY CONTRACT (C-46). The
  implicit inference path for C-48 existed: a reader could cross-reference from each PHASE ENTRY
  CONTRACT `IM Reference:` back to the INCUMBENT BASELINE row. But no `Phase Refs:` sub-field
  was declared at the baseline-row level. R16 V-04 promotes the back-reference to an explicit
  named annotation on each IM-ID row, closing the Baseline->Phase direction bidirectionally at
  the source table.

- **C-49 signal**: R15 V-05 carried `Role Ref:`, `Bottleneck Ref:`, and `IM Ref:` in every EX
  block (C-40, C-42, C-47). The three sub-fields co-existed but their architectural status was
  implicit -- no preamble declared them as a named unit. C-49 requires an explicit EXCEPTION
  BLOCK ARCHITECTURE header naming all three namespaces with orthogonality assertion, making EX
  block completeness format-verifiable from the preamble alone. R16 V-02 adds this header.

- **C-50 signal**: R15 V-05 listed 13 CHAIN STATUS directions in a flat bullet list. The four
  directions named by C-50 were all present but discoverable only by traversal. C-50 requires
  an indexed DIRECTION INVENTORY block at CHAIN STATUS opening that declares each direction
  PRESENT or ABSENT with a section citation. R16 V-03 adds this inventory.

**New criteria targeted in R16:**

**C-48 target (V-04, V-05)**: Add named `Phase Refs:` back-reference annotations to INCUMBENT
BASELINE, one per IM-ID row. Each annotation lists every PHASE ENTRY CONTRACT whose
`IM Reference:` sub-field cites this IM-ID. NONE sentinel for IM-IDs with no phase citations.
String comparison only. CHAIN STATUS gains a `Phase->Baseline` direction.

**C-49 target (V-02, V-05)**: Add explicit EXCEPTION BLOCK ARCHITECTURE header to SECTION A
preamble. The header names all three citation sub-fields as a declared unit (`Role Ref:` / R-ID
namespace, `Bottleneck Ref:` / B-ID namespace, `IM Ref:` / IM-ID namespace) with an explicit
orthogonality assertion that the three string patterns are non-overlapping and independently
verifiable by string comparison.

**C-50 target (V-03, V-05)**: Add DIRECTION INVENTORY block as the first structural element of
CHAIN STATUS. The inventory enumerates all four established traceability directions by canonical
name, declares each PRESENT or ABSENT, and cites the section or sub-field carrying it.

**Variation matrix:**

| Variation | Axes | C-48 Phase Refs | C-49 EX Architecture | C-50 Direction Inventory | Primary hypothesis |
|-----------|------|:---------------:|:--------------------:|:------------------------:|-------------------|
| V-01 | Role sequence | NO | NO | NO | R15 V-05 implicit structure -- tests whether retroactive C-48/C-49/C-50 pass holds reliably without explicit instructions; establishes R16 floor |
| V-02 | Output format | NO | YES (named header, namespace table, orthogonality) | NO | Explicit EXCEPTION BLOCK ARCHITECTURE header scores C-49 independently; C-48/C-50 remain FAIL |
| V-03 | Lifecycle emphasis | NO | NO | YES (indexed DIRECTION INVENTORY) | Explicit DIRECTION INVENTORY at CHAIN STATUS opening scores C-50 independently; C-48/C-49 remain FAIL |
| V-04 | Inertia framing | YES (Phase Refs per IM-ID, NONE sentinel) | NO | NO | Explicit Phase Refs back-reference in INCUMBENT BASELINE rows scores C-48 independently; C-49/C-50 remain FAIL |
| V-05 | Output format + Lifecycle emphasis + Inertia framing | YES | YES | YES | Maximum density -- all three compose; 42/42 = 10.000 |

**Structural change summary vs R15 V-05:**

| Section | R15 V-05 had | V-01 (unchanged) | V-02 adds | V-03 adds | V-04 adds | V-05 combines |
|---------|-------------|-----------------|----------|----------|----------|--------------|
| INCUMBENT BASELINE | Table + Cost of no action | Same | -- | -- | `Phase Refs:` per IM-ID annotation | `Phase Refs:` per IM-ID |
| SECTION A preamble | EX block template with three sub-fields | Same | EXCEPTION BLOCK ARCHITECTURE header | -- | -- | EXCEPTION BLOCK ARCHITECTURE header |
| CHAIN STATUS | 13 directions flat list | Same | -- | DIRECTION INVENTORY block at opening | + `Phase->Baseline` direction (14 total) | DIRECTION INVENTORY + `Phase->Baseline` (14 total) |

---

## V-01 -- Axis: Role Sequence (Full R15 V-05 Structure, Baseline)

**Variation axis**: Role sequence -- default domain-natural role ordering (Sales/Procurement/
Finance/Operations sequence determined by process type). Full R15 V-05 structure intact: per-block
`Exception Refs:` in B-NN blocks (C-44), dedicated PHASE GATE CONTRACT SUMMARY (C-45), named
`IM Reference:` sub-field in every PHASE ENTRY CONTRACT (C-46), named `IM Ref:` sub-field in
every SECTION A EX block (C-47). No explicit `Phase Refs:` back-reference in INCUMBENT BASELINE
(C-48 not targeted). No EXCEPTION BLOCK ARCHITECTURE header in SECTION A (C-49 not targeted). No
DIRECTION INVENTORY block in CHAIN STATUS (C-50 not targeted).

**Hypothesis**: The R15 V-05 structure implicitly satisfied C-48/C-49/C-50 retroactively because
the prerequisite sub-fields were all present. V-01 tests whether implicit inference produces
reliable compliance on a fresh topic run. If V-01 scores 42/42, single-axis variations confirm
zero-regression tolerance. If V-01 scores 39/42, the single-axis variations isolate which
explicit additions are necessary. Expected aspirational: 39/42 or 42/42.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must satisfy both Dual-Cite
> Fail Conditions. Quantified metric must appear before PHASE 1 in document order.
> This section is the inertia reference: IM-IDs assigned here are anchor identifiers for
> (1) `IM Reference:` in every PHASE ENTRY CONTRACT and (2) `IM Ref:` in every SECTION A EX
> block. Every exception trace and bottleneck must be traceable back to a named IM-ID.

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
> by string comparison: a B-ID in `Next phase:` is a detectable format violation; a Phase
> label in `Prior phase blocked bottleneck:` is a detectable format violation. No inference
> required -- the patterns are non-overlapping by construction.
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

For each phase in the lifecycle, produce the following five blocks in document order. All
three Phase Gate Contract fields must be populated in every phase block per the PHASE GATE
CONTRACT SUMMARY above. `IM Reference:` must additionally appear in every PHASE ENTRY CONTRACT.

---

**PHASE [N] -- [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Phase Gate Contract fields 1 and 2 live here; field 3 (`Next phase:`) lives in PHASE EXIT GATE.
> `IM Reference:` is a fourth required sub-field providing Baseline->Phase traceability.
> Entry Condition must reference the prior phase's PHASE EXIT GATE "Required outputs" by name.
> All four sub-fields are independently verifiable by string comparison.

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
  identifiers -- string comparison only, no inference. This sub-field opens the Baseline->Phase
  traceability direction: a reader can navigate directly from this phase's entry contract to
  the INCUMBENT BASELINE rows whose failure modes motivated the entry controls for this phase.
  Example: "IM-01 (manual reconciliation gap -- active entry risk: pre-condition artifact
  produced manually and vulnerable to IM-01 failure mode before this phase begins)."]

**SECTION A -- EXCEPTION TRACES**

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
>   NONE only if no declared bottleneck was causal.]
> - Role Ref: [R-ID of the ROLE SEQUENCE SCHEDULE primary owner for this phase. Literal R-ID
>   matching the schedule's Primary Owner entry for the enclosing phase. Free-text without
>   R-ID fails. R-ID absent from schedule fails.]
> - IM Ref: [IM-ID from INCUMBENT BASELINE whose failure mode this exception traces, or NONE.
>   Use exact IM-ID identifier as declared in the INCUMBENT BASELINE table (e.g., "IM-01").
>   This sub-field completes the dual-citation architecture: `Bottleneck Ref:` links this EX
>   block to a B-NN (C-42); `IM Ref:` links this EX block directly to the INCUMBENT BASELINE
>   failure mode (C-47). NONE if no incumbent baseline failure mode is directly traceable.
>   String comparison only -- IM-ID must literal-match INCUMBENT BASELINE table identifier.
>   Example: "IM-01 -- this exception is the process-visible manifestation of the incumbent
>   manual reconciliation failure mode entering Phase 2."]

Minimum 1 exception trace per phase; 3 total minimum.
Every declared R-ID in the Role Registry Gate must appear in at least one EX block Role Ref.
Bottleneck Ref, Role Ref, and IM Ref are independent sub-fields; populate all three for every EX block.

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

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA->B): [every AT-RISK SLA row cites a B-ID; enumerate pairs or name gap]
- Backward (B->SLA): [every B-NN Evidence field lists AT-RISK SLA rows; enumerate or name gap]
- Exit gate consistency: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID matches a declared B-NN; name any mismatch]
- Phase-boundary B-NN continuity: [every exit gate B-ID matches next phase's `Prior phase blocked bottleneck:`; list pairs or name break]
- Phase-sequence: [every PHASE ENTRY CONTRACT `Prior phase:` matches preceding phase block label; PHASE 1 carries NONE/INIT; list pairs or name mismatch]
- Phase-exit-sequence: [every PHASE EXIT GATE `Next phase:` matches subsequent phase block label; last phase carries NONE/END; list pairs or name mismatch]
- Exception->B: [every EX block `Bottleneck Ref:` B-ID (non-NONE) matches a declared B-NN; list EX->B-NN pairs or name unresolved block]
- B-NN->Exception: [every declared B-ID has at least one non-NONE entry in its `Exception Refs:` field; each listed EX block ID string-matches an EX block with `Bottleneck Ref:` citing this B-ID; enumerate B-ID->EX pairs; name any B-ID with NONE in Exception Refs (dark bottleneck) or any listed ID whose EX block does not carry matching Bottleneck Ref (consistency failure)]
- Exception->Role: [every EX block `Role Ref:` R-ID matches ROLE SEQUENCE SCHEDULE primary owner; list EX->R-ID pairs or name mismatch]
- Role->Exception: [every declared R-ID appears in at least one EX block `Role Ref:`; list R-ID->EX pairs; name dark roles]
- Dual-cite status: [every B-NN Cause has both IM-ID and R-ID; name any block missing either]
- Baseline->Phase: [every PHASE ENTRY CONTRACT `IM Reference:` field contains only IM-IDs declared in INCUMBENT BASELINE; list phase->IM-ID pairs; phases with NONE sentinel are CLOSED for this direction; name any phase whose IM Reference contains a non-declared IM-ID or is absent]
- Baseline->Exception: [every SECTION A EX block `IM Ref:` field contains only IM-IDs declared in INCUMBENT BASELINE or NONE sentinel; list EX->IM-ID pairs; name any EX block whose IM Ref contains a non-declared IM-ID or is absent (dark exception); EX blocks with NONE sentinel are CLOSED for this direction]
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

## V-02 -- Axis: Output Format (EXCEPTION BLOCK ARCHITECTURE Declaration, C-49 Target)

**Variation axis**: Output format -- an explicit EXCEPTION BLOCK ARCHITECTURE header is added to
the SECTION A preamble before the first EX block template. The header names all three EX block
citation sub-fields as a declared unit (`Role Ref:` / R-ID namespace, `Bottleneck Ref:` / B-ID
namespace, `IM Ref:` / IM-ID namespace) with an explicit orthogonality assertion that the three
string patterns are non-overlapping and independently verifiable by string comparison. This header
is parallel to the PHASE GATE CONTRACT SUMMARY: both are pre-phase architectural declarations that
bind independently established sub-fields into a named unit. No `Phase Refs:` in INCUMBENT
BASELINE (C-48 not targeted). No DIRECTION INVENTORY in CHAIN STATUS (C-50 not targeted).

**Hypothesis**: C-49 requires "an explicit SECTION A preamble or EXCEPTION BLOCK ARCHITECTURE
header that names all three citation sub-fields as a declared unit" with orthogonality assertion.
The V-01 baseline has all three sub-fields co-present in every EX block but no preamble that
declares them as a named architectural unit with namespace labels. Promoting the implicit
co-presence to an explicit EXCEPTION BLOCK ARCHITECTURE header reliably scores C-49. C-48/C-50
remain FAIL. Expected: 40/42.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must satisfy both Dual-Cite
> Fail Conditions. Quantified metric must appear before PHASE 1 in document order.
> This section is the inertia reference: IM-IDs assigned here are anchor identifiers for
> (1) `IM Reference:` in every PHASE ENTRY CONTRACT and (2) `IM Ref:` in every SECTION A EX
> block. Every exception trace and bottleneck must be traceable back to a named IM-ID.

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
approval cycle time: 5.8 days vs 3-day SLA -- IM-01 primary driver."]

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
> `Role Ref:` must match the schedule entry for the enclosing phase.

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior-process artifact -- not "Start"] | [specific completion condition] | R-[ID] or NONE | [concurrent window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1 -- name the artifact] | [completion condition] | R-[ID] or NONE | [concurrent activity or NONE] |

---

### Phase Gate Contract Summary

> **DECLARED UNIT: THREE-FIELD PHASE GATE CONTRACT**
>
> | Field Name | Location | Value Type | Traceability Direction |
> |------------|----------|------------|----------------------|
> | `Prior phase:` | PHASE ENTRY CONTRACT | Phase label (e.g., "PHASE 1 -- Initiation") | Phase->Phase, backward |
> | `Prior phase blocked bottleneck:` | PHASE ENTRY CONTRACT | B-ID (e.g., "B-01") | B-NN boundary continuity |
> | `Next phase:` | PHASE EXIT GATE | Phase label (e.g., "PHASE 2 -- Review") | Phase->Phase, forward |
>
> **ORTHOGONALITY DECLARATION:** `Prior phase blocked bottleneck:` carries a B-ID;
> `Next phase:` carries a Phase label. Non-overlapping by construction; independently verifiable.
> `IM Reference:` is a fourth required sub-field in PHASE ENTRY CONTRACT (Baseline->Phase
> traceability); it is not part of the three-field gate contract but required in every entry block.

---

### Phase Structure

For each phase in the lifecycle, produce the following five blocks in document order. All three
Phase Gate Contract fields required in every phase block. `IM Reference:` additionally required
in every PHASE ENTRY CONTRACT.

---

**PHASE [N] -- [PHASE NAME]**

**PHASE ENTRY CONTRACT**

- Entry Condition: [specific named artifact from prior phase's Required outputs]
- Pre-condition check: R-[ID] ([role name -- must match Role Sequence Schedule primary owner]) -- [verification method]
- Blocking condition: [state entered and role notified if entry condition not met]
- Prior phase: [Literal identifier of preceding phase block. Phase 1: NONE or INIT. Format: "PHASE N -- [Name]".]
- Prior phase blocked bottleneck: [B-ID from prior exit gate or NONE or N/A for Phase 1. B-ID format, NOT Phase label.]
- IM Reference: [List every IM-ID from INCUMBENT BASELINE whose failure mode is an active risk
  entering this phase. Exact IM-IDs from INCUMBENT BASELINE table. NONE if no active risk.
  String comparison only. Example: "IM-01 (manual reconciliation gap -- active entry risk)."]

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
> R-ID or B-ID. EX block completeness is format-verifiable from this declaration without
> per-block traversal: an EX block missing any of the three sub-fields is a detectable
> format violation regardless of prose content.

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] -- [Exception Name]**
> - Trigger: [specific condition -- name the state, threshold breach, or missing input]
> - Trace: [states traversed; cite S-IDs in sequence]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason]
> - Bottleneck Ref: [B-NN or NONE. B-ID must string-match a Bottleneck Analysis identifier.
>   B-NN block's `Exception Refs:` must list this EX block ID if non-NONE.
>   Namespace: B-ID (see EXCEPTION BLOCK ARCHITECTURE above).]
> - Role Ref: [R-ID of ROLE SEQUENCE SCHEDULE primary owner for this phase. Literal R-ID.
>   Namespace: R-ID (see EXCEPTION BLOCK ARCHITECTURE above).]
> - IM Ref: [IM-ID from INCUMBENT BASELINE or NONE. String comparison only.
>   Namespace: IM-ID (see EXCEPTION BLOCK ARCHITECTURE above).
>   Example: "IM-01 -- manifestation of incumbent manual reconciliation failure mode."]

Minimum 1 per phase; 3 total minimum. All three sub-fields independent; populate all three.

**SECTION B -- STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules: Named Entry Condition required; Exits --> S-ID or TERMINAL; standard Type values.

**Decision Supplement Blocks** (one per DECISION-type state):

> **DS-[S-ID] -- [State Name]**: Condition / Owner R-[ID] / Branch A / Branch B / Fallback

**PHASE EXIT GATE**

- Exit Condition: [what the phase must produce to be complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name]) confirms all outputs present
- Blocking condition: [re-entry path or escalation if outputs absent]
- Blocked bottleneck: [B-NN or NONE. Must string-match Bottleneck Analysis AND next phase `Prior phase blocked bottleneck:`.]
- Next phase: [Literal identifier of subsequent phase. Last phase: NONE or END. Phase label -- not a B-ID.]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID]; **Branch 1**: [S-IDs]; **Branch 2**: [S-IDs]
- **JOIN at**: S-[ID]; **Join Condition**: AND-join / OR-join -- specify and explain

### Edge Case Enumeration

Three or more, distinct from SECTION A:

> **EC-[N] -- [Edge Case Name]**: Triggering Condition / Why Problematic / Correct Response: R-[ID] -- [action]

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF**: Sending State S-[ID] / Receiving Process / Data Payload /
> Expected Acknowledgment / Failure Mode / Owner R-[ID]

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|

Minimum 3 rows; at least 1 AT-RISK citing a B-NN.

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN Cause field must satisfy both Dual-Cite Fail Conditions independently.
>
> **Dual-Cite Fail Condition A** -- no IM-ID literal string in Cause --> fails C-39.
> **Dual-Cite Fail Condition B** -- no R-ID literal string in Cause --> fails C-39.
>
> B-IDs must string-match: (1) PHASE EXIT GATE `Blocked bottleneck:`, (2) PHASE ENTRY CONTRACT
> `Prior phase blocked bottleneck:` in following phase, (3) EX block `Bottleneck Ref:` non-NONE.
>
> Concrete format example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`
> Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
> Fail condition: Field with no AT-RISK row-level S-ID specificity does not satisfy.
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
  - [List each AT-RISK SLA row citing B-02. Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]
- Exception Refs:
  - Required format: `EX-[Phase#][Letter] (Phase [N] -- [Exception Name])`
  - Fail condition: NONE = dark bottleneck (gate violation).
  - [List each EX block identifier whose `Bottleneck Ref:` cites B-02, or NONE.]

---

**Gap Identification**

> MISSING: [step name] -- [why it belongs; failure mode enabled; which phase; which IM-ID reduced]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA->B): [enumerate pairs or name gap]
- Backward (B->SLA): [enumerate or name gap]
- Exit gate consistency: [every exit gate B-ID matches a declared B-NN; name mismatch]
- Phase-boundary B-NN continuity: [exit gate B-ID matches next entry contract; list pairs]
- Phase-sequence: [every `Prior phase:` matches preceding block label; PHASE 1 NONE/INIT]
- Phase-exit-sequence: [every `Next phase:` matches subsequent block label; last phase NONE/END]
- Exception->B: [every EX `Bottleneck Ref:` B-ID matches a declared B-NN; list pairs]
- B-NN->Exception: [every declared B-ID has at least one non-NONE entry in its `Exception Refs:`; each listed EX block ID string-matches an EX block with matching `Bottleneck Ref:`; enumerate B-ID->EX pairs; name dark bottlenecks]
- Exception->Role: [every EX `Role Ref:` R-ID matches schedule primary owner; list pairs]
- Role->Exception: [every declared R-ID in at least one EX `Role Ref:`; list pairs; name dark roles]
- Dual-cite status: [every B-NN Cause has both IM-ID and R-ID; name missing]
- Baseline->Phase: [every PHASE ENTRY CONTRACT `IM Reference:` contains only declared IM-IDs; list phase->IM-ID pairs; NONE sentinels CLOSED]
- Baseline->Exception: [every EX block `IM Ref:` contains only declared IM-IDs or NONE; list EX->IM-ID pairs; name dark exceptions]
- Gap (if OPEN): [unresolved direction and unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal name] | SUCCESS | [branch or state] |
| [failure terminal name] | FAILURE | [branch or state] |
| [cancel terminal name] | CANCEL | [branch or state] |

> Completeness check: Every exit branch must reach a declared terminal.

---
---

## V-03 -- Axis: Lifecycle Emphasis (CHAIN STATUS Direction Inventory, C-50 Target)

**Variation axis**: Lifecycle emphasis -- the CHAIN STATUS section opens with an explicit
DIRECTION INVENTORY block that enumerates all four established traceability directions by
canonical name, declares each PRESENT or ABSENT, and cites the section or sub-field carrying it.
Converts the implicit multi-directional CHAIN STATUS from a traversal-dependent flat list into
an indexed direction register verifiable by string comparison alone. No `Phase Refs:` in
INCUMBENT BASELINE (C-48 not targeted). No EXCEPTION BLOCK ARCHITECTURE header (C-49 not targeted).

**Hypothesis**: C-50 requires "an explicit DIRECTION INVENTORY block enumerating all four
established traceability directions by canonical name" at CHAIN STATUS opening. The V-01 baseline
lists all 13 directions as a flat bullet list with no indexed inventory that declares each
direction PRESENT or ABSENT with a section citation. A dedicated DIRECTION INVENTORY block --
naming `B-NN->Exception`, `Phase-exit-sequence`, `Baseline->Phase`, `Baseline->Exception` with
PRESENT declarations and sub-field citations -- reliably scores C-50. An absent inventory block
fails regardless of direction content in the body. C-48/C-49 remain FAIL. Expected: 40/42.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must satisfy both Dual-Cite
> Fail Conditions. Quantified metric must appear before PHASE 1 in document order.
> This section is the inertia reference: IM-IDs assigned here are anchor identifiers for
> (1) `IM Reference:` in every PHASE ENTRY CONTRACT and (2) `IM Ref:` in every SECTION A EX
> block. Every exception trace and bottleneck must be traceable back to a named IM-ID.

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
Both IM-IDs must be reachable from at least one B-NN Cause field.]

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
> the blocking R-ID from this schedule (Dual-Cite Fail Condition B).

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior-process artifact -- not "Start"] | [specific completion condition] | R-[ID] or NONE | [concurrent window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1 -- name the artifact] | [completion condition] | R-[ID] or NONE | [concurrent activity or NONE] |

---

### Phase Gate Contract Summary

> **DECLARED UNIT: THREE-FIELD PHASE GATE CONTRACT**
>
> | Field Name | Location | Value Type | Traceability Direction |
> |------------|----------|------------|----------------------|
> | `Prior phase:` | PHASE ENTRY CONTRACT | Phase label (e.g., "PHASE 1 -- Initiation") | Phase->Phase, backward |
> | `Prior phase blocked bottleneck:` | PHASE ENTRY CONTRACT | B-ID (e.g., "B-01") | B-NN boundary continuity |
> | `Next phase:` | PHASE EXIT GATE | Phase label (e.g., "PHASE 2 -- Review") | Phase->Phase, forward |
>
> **ORTHOGONALITY DECLARATION:** `Prior phase blocked bottleneck:` carries a B-ID; `Next phase:`
> carries a Phase label. Non-overlapping by construction; independently verifiable by string
> comparison. `IM Reference:` is a fourth required sub-field in PHASE ENTRY CONTRACT
> (Baseline->Phase traceability); not part of the three-field gate contract but required in
> every entry block. CHAIN STATUS verifies: `Phase-sequence`, `Phase-exit-sequence`,
> `Phase-boundary B-NN continuity`.

---

### Phase Structure

For each phase, produce five blocks in document order. All three Phase Gate Contract fields
required in every phase block. `IM Reference:` additionally required in every PHASE ENTRY CONTRACT.

---

**PHASE [N] -- [PHASE NAME]**

**PHASE ENTRY CONTRACT**

- Entry Condition: [specific named artifact from prior phase's Required outputs]
- Pre-condition check: R-[ID] ([role name -- must match Role Sequence Schedule primary owner]) -- [verification method]
- Blocking condition: [state entered and role notified if entry condition not met]
- Prior phase: [Literal identifier of preceding phase block. Phase 1: NONE or INIT. Format: "PHASE N -- [Name]".]
- Prior phase blocked bottleneck: [B-ID from prior exit gate or NONE or N/A for Phase 1. B-ID format, NOT Phase label.]
- IM Reference: [List every IM-ID from INCUMBENT BASELINE whose failure mode is an active risk
  entering this phase. Exact IM-IDs from INCUMBENT BASELINE table. NONE if no active risk.
  String comparison only. Example: "IM-01 (manual reconciliation gap -- active entry risk)."]

**SECTION A -- EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] -- [Exception Name]**
> - Trigger: [specific condition -- name the state, threshold breach, or missing input]
> - Trace: [states traversed; cite S-IDs in sequence]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason]
> - Bottleneck Ref: [B-NN or NONE. B-ID must string-match a Bottleneck Analysis identifier.
>   B-NN block's `Exception Refs:` must list this EX block ID if non-NONE.]
> - Role Ref: [R-ID of ROLE SEQUENCE SCHEDULE primary owner for this phase. Literal R-ID.]
> - IM Ref: [IM-ID from INCUMBENT BASELINE or NONE. String comparison only.
>   Example: "IM-01 -- manifestation of incumbent manual failure mode in this phase."]

Minimum 1 per phase; 3 total minimum. All three sub-fields independent; populate all three.

**SECTION B -- STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules: Named Entry Condition required; Exits --> S-ID or TERMINAL; standard Type values.

**Decision Supplement Blocks** (one per DECISION-type state):

> **DS-[S-ID] -- [State Name]**: Condition / Owner R-[ID] / Branch A / Branch B / Fallback

**PHASE EXIT GATE**

- Exit Condition: [what the phase must produce to be complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name]) confirms all outputs present
- Blocking condition: [re-entry path or escalation if outputs absent]
- Blocked bottleneck: [B-NN or NONE. Must string-match Bottleneck Analysis AND next phase `Prior phase blocked bottleneck:`.]
- Next phase: [Literal identifier of subsequent phase. Last phase: NONE or END. Phase label -- not a B-ID.]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID]; **Branch 1**: [S-IDs]; **Branch 2**: [S-IDs]
- **JOIN at**: S-[ID]; **Join Condition**: AND-join / OR-join -- specify and explain

### Edge Case Enumeration

Three or more, distinct from SECTION A:

> **EC-[N] -- [Edge Case Name]**: Triggering Condition / Why Problematic / Correct Response: R-[ID] -- [action]

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF**: Sending State S-[ID] / Receiving Process / Data Payload /
> Expected Acknowledgment / Failure Mode / Owner R-[ID]

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|

Minimum 3 rows; at least 1 AT-RISK citing a B-NN.

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN Cause field must satisfy both Dual-Cite Fail Conditions independently.
>
> **Dual-Cite Fail Condition A** -- no IM-ID literal string in Cause --> fails C-39.
> **Dual-Cite Fail Condition B** -- no R-ID literal string in Cause --> fails C-39.
>
> B-IDs must string-match: (1) PHASE EXIT GATE `Blocked bottleneck:`, (2) PHASE ENTRY CONTRACT
> `Prior phase blocked bottleneck:` in following phase, (3) EX block `Bottleneck Ref:` non-NONE.
>
> Concrete format example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`
> Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
> Fail condition: Field with no AT-RISK row-level S-ID specificity does not satisfy.
>
> **DUAL-LOCATION REQUIREMENTS:** Concrete example AND labeled axes in BOTH preamble AND per-block hints.
>
> **B-NN->Exception Gate Check**: Every declared B-ID must appear in at least one EX block's
> `Bottleneck Ref:`. Dark bottlenecks are gate violations. Report in CHAIN STATUS.
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
  - [List each AT-RISK SLA row citing B-02. Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]
- Exception Refs:
  - Required format: `EX-[Phase#][Letter] (Phase [N] -- [Exception Name])`
  - Fail condition: NONE = dark bottleneck (gate violation).
  - [List each EX block identifier whose `Bottleneck Ref:` cites B-02, or NONE.]

---

**Gap Identification**

> MISSING: [step name] -- [why it belongs; failure mode enabled; which phase; which IM-ID reduced]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

**DIRECTION INVENTORY:**

> The four established traceability directions are enumerated below as a named index. Each
> direction is declared PRESENT or ABSENT with a citation to the section or sub-field carrying
> it. Completeness of chain coverage is format-verifiable from this inventory by string
> comparison alone, without traversing the full document. A direction declared NOT-APPLICABLE
> must carry an explicit rationale. An absent DIRECTION INVENTORY block is a FAIL regardless
> of direction content in the body below. A DIRECTION INVENTORY missing any of the four
> established directions is a FAIL.

| Direction | Status | Carried By |
|-----------|--------|-----------|
| B-NN->Exception | [PRESENT / ABSENT] | [B-NN block `Exception Refs:` field listing EX block IDs; EX block `Bottleneck Ref:` field citing B-ID] |
| Phase-exit-sequence | [PRESENT / ABSENT] | [PHASE EXIT GATE `Next phase:` sub-field; string-match to subsequent phase block label] |
| Baseline->Phase | [PRESENT / ABSENT] | [PHASE ENTRY CONTRACT `IM Reference:` sub-field; string-match to INCUMBENT BASELINE IM-IDs] |
| Baseline->Exception | [PRESENT / ABSENT] | [SECTION A EX block `IM Ref:` sub-field; string-match to INCUMBENT BASELINE IM-IDs] |

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA->B): [every AT-RISK SLA row cites a B-ID; enumerate pairs or name gap]
- Backward (B->SLA): [every B-NN Evidence field lists AT-RISK SLA rows; enumerate or name gap]
- Exit gate consistency: [every exit gate B-ID matches a declared B-NN; name mismatch]
- Phase-boundary B-NN continuity: [exit gate B-ID matches next entry contract; list pairs]
- Phase-sequence: [every `Prior phase:` matches preceding block label; PHASE 1 NONE/INIT]
- Phase-exit-sequence: [every `Next phase:` matches subsequent block label; last phase NONE/END -- consistent with DIRECTION INVENTORY declaration above]
- Exception->B: [every EX `Bottleneck Ref:` B-ID matches a declared B-NN; list pairs]
- B-NN->Exception: [every declared B-ID has at least one non-NONE entry in its `Exception Refs:`; enumerate B-ID->EX pairs; name dark bottlenecks -- consistent with DIRECTION INVENTORY declaration above]
- Exception->Role: [every EX `Role Ref:` R-ID matches schedule primary owner; list pairs]
- Role->Exception: [every declared R-ID in at least one EX `Role Ref:`; list pairs; name dark roles]
- Dual-cite status: [every B-NN Cause has both IM-ID and R-ID; name missing]
- Baseline->Phase: [every PHASE ENTRY CONTRACT `IM Reference:` contains only declared IM-IDs; list phase->IM-ID pairs; NONE sentinels CLOSED -- consistent with DIRECTION INVENTORY declaration above]
- Baseline->Exception: [every EX block `IM Ref:` contains only declared IM-IDs or NONE; list EX->IM-ID pairs; name dark exceptions -- consistent with DIRECTION INVENTORY declaration above]
- Gap (if OPEN): [unresolved direction and unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal name] | SUCCESS | [branch or state] |
| [failure terminal name] | FAILURE | [branch or state] |
| [cancel terminal name] | CANCEL | [branch or state] |

> Completeness check: Every exit branch must reach a declared terminal.

---
---

## V-04 -- Axis: Inertia Framing (Phase Refs Back-Reference in INCUMBENT BASELINE, C-48 Target)

**Variation axis**: Inertia framing -- each IM-ID row in INCUMBENT BASELINE carries an explicit
`Phase Refs:` back-reference annotation listing every PHASE ENTRY CONTRACT whose `IM Reference:`
sub-field cites this IM-ID. This closes the Baseline->Phase direction (C-46) bidirectionally at
the source-table level: the INCUMBENT BASELINE becomes navigable in both directions -- outward
(IM-ID -> which phases cite it, via `Phase Refs:`) and inward (phase -> which IM-IDs are active,
via `IM Reference:`). IM-IDs with no phase citations carry explicit NONE sentinel. CHAIN STATUS
gains a `Phase->Baseline` direction as the bidirectional complement to `Baseline->Phase`.
No EXCEPTION BLOCK ARCHITECTURE header (C-49 not targeted). No DIRECTION INVENTORY block
(C-50 not targeted).

**Hypothesis**: C-48 requires source-end enumeration: "each row in the INCUMBENT BASELINE table
carries a named `Phase Refs:` sub-field enumerating every PHASE ENTRY CONTRACT where this IM-ID
appears in its `IM Reference:` field." The V-01 baseline has C-46 (`IM Reference:` in PHASE ENTRY
CONTRACT) but no back-reference from the baseline row to the phases that cite it. Adding explicit
`Phase Refs:` annotations per IM-ID row -- with NONE sentinel and a consistency instruction
linking to C-46 sub-fields -- reliably scores C-48 as a source-end navigable lookup. CHAIN STATUS
`Phase->Baseline` direction verifies consistency. C-49/C-50 remain FAIL. Expected: 40/42.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must satisfy both Dual-Cite
> Fail Conditions. Quantified metric must appear before PHASE 1 in document order.
> This section is the inertia reference: IM-IDs assigned here are anchor identifiers for
> (1) `IM Reference:` in every PHASE ENTRY CONTRACT, (2) `IM Ref:` in every SECTION A EX block.
> After all PHASE ENTRY CONTRACT blocks are complete, return here to populate `Phase Refs:`
> back-references for each IM-ID, closing the Baseline->Phase direction bidirectionally.

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
Both IM-IDs must be reachable from at least one B-NN Cause field.]

**Phase back-references (C-48 -- closes Baseline->Phase bidirectionally at source):**

> After completing all PHASE ENTRY CONTRACT blocks, populate the back-references below.
> Each IM-ID lists every PHASE ENTRY CONTRACT whose `IM Reference:` sub-field cites this IM-ID.
> Enumeration must be consistent with all `IM Reference:` sub-fields by string comparison --
> if a PHASE ENTRY CONTRACT `IM Reference:` cites IM-01, then IM-01 `Phase Refs:` must include
> that phase's literal identifier; if it does not cite IM-01, IM-01 `Phase Refs:` must not list
> it. IM-IDs with no phase citations carry explicit NONE sentinel. String comparison only.

- IM-01 Phase Refs: [List every PHASE ENTRY CONTRACT by literal phase block identifier whose
  `IM Reference:` sub-field cites IM-01 (e.g., "PHASE 1 -- Initiation; PHASE 3 -- Approval").
  If no PHASE ENTRY CONTRACT `IM Reference:` cites IM-01, write NONE. String comparison only --
  match the literal phase block label as it appears in the document.]
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
> the blocking R-ID from this schedule (Dual-Cite Fail Condition B).

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior-process artifact -- not "Start"] | [specific completion condition] | R-[ID] or NONE | [concurrent window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1 -- name the artifact] | [completion condition] | R-[ID] or NONE | [concurrent activity or NONE] |

---

### Phase Gate Contract Summary

> **DECLARED UNIT: THREE-FIELD PHASE GATE CONTRACT**
>
> | Field Name | Location | Value Type | Traceability Direction |
> |------------|----------|------------|----------------------|
> | `Prior phase:` | PHASE ENTRY CONTRACT | Phase label (e.g., "PHASE 1 -- Initiation") | Phase->Phase, backward |
> | `Prior phase blocked bottleneck:` | PHASE ENTRY CONTRACT | B-ID (e.g., "B-01") | B-NN boundary continuity |
> | `Next phase:` | PHASE EXIT GATE | Phase label (e.g., "PHASE 2 -- Review") | Phase->Phase, forward |
>
> **ORTHOGONALITY DECLARATION:** `Prior phase blocked bottleneck:` carries a B-ID; `Next phase:`
> carries a Phase label. Non-overlapping by construction; independently verifiable. `IM Reference:`
> is a fourth required sub-field in PHASE ENTRY CONTRACT (Baseline->Phase traceability).
> After all phases are traced, INCUMBENT BASELINE `Phase Refs:` back-references close the
> Baseline->Phase direction bidirectionally at the source-row level.

---

### Phase Structure

For each phase, produce five blocks in document order. All three Phase Gate Contract fields
required in every phase block. `IM Reference:` additionally required in every PHASE ENTRY
CONTRACT. After all phases are complete, return to INCUMBENT BASELINE to populate `Phase Refs:`.

---

**PHASE [N] -- [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> `IM Reference:` content will be cross-referenced by INCUMBENT BASELINE `Phase Refs:`
> back-references -- populate accurately so the bidirectional chain is consistent by string
> comparison.

- Entry Condition: [specific named artifact from prior phase's Required outputs]
- Pre-condition check: R-[ID] ([role name -- must match Role Sequence Schedule primary owner]) -- [verification method]
- Blocking condition: [state entered and role notified if entry condition not met]
- Prior phase: [Literal identifier of preceding phase block. Phase 1: NONE or INIT. Format: "PHASE N -- [Name]".]
- Prior phase blocked bottleneck: [B-ID from prior exit gate or NONE or N/A for Phase 1. B-ID format, NOT Phase label.]
- IM Reference: [List every IM-ID from INCUMBENT BASELINE whose failure mode is an active risk
  entering this phase. Exact IM-IDs from INCUMBENT BASELINE table. NONE if no active risk.
  INCUMBENT BASELINE `Phase Refs:` for each cited IM-ID will list this phase's literal
  identifier -- ensure phase block label here is consistent with `Phase Refs:` entries.
  Example: "IM-01 (manual reconciliation gap -- active entry risk at this phase)."]

**SECTION A -- EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] -- [Exception Name]**
> - Trigger: [specific condition -- name the state, threshold breach, or missing input]
> - Trace: [states traversed; cite S-IDs in sequence]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason]
> - Bottleneck Ref: [B-NN or NONE. B-ID must string-match a Bottleneck Analysis identifier.
>   B-NN block's `Exception Refs:` must list this EX block ID if non-NONE.]
> - Role Ref: [R-ID of ROLE SEQUENCE SCHEDULE primary owner for this phase. Literal R-ID.]
> - IM Ref: [IM-ID from INCUMBENT BASELINE or NONE. String comparison only.
>   Example: "IM-01 -- manifestation of incumbent manual failure mode."]

Minimum 1 per phase; 3 total minimum. All three sub-fields independent; populate all three.

**SECTION B -- STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules: Named Entry Condition required; Exits --> S-ID or TERMINAL; standard Type values.

**Decision Supplement Blocks** (one per DECISION-type state):

> **DS-[S-ID] -- [State Name]**: Condition / Owner R-[ID] / Branch A / Branch B / Fallback

**PHASE EXIT GATE**

- Exit Condition: [what the phase must produce to be complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name]) confirms all outputs present
- Blocking condition: [re-entry path or escalation if outputs absent]
- Blocked bottleneck: [B-NN or NONE. Must string-match Bottleneck Analysis AND next phase `Prior phase blocked bottleneck:`.]
- Next phase: [Literal identifier of subsequent phase. Last phase: NONE or END. Phase label -- not a B-ID.]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID]; **Branch 1**: [S-IDs]; **Branch 2**: [S-IDs]
- **JOIN at**: S-[ID]; **Join Condition**: AND-join / OR-join -- specify and explain

### Edge Case Enumeration

Three or more, distinct from SECTION A:

> **EC-[N] -- [Edge Case Name]**: Triggering Condition / Why Problematic / Correct Response: R-[ID] -- [action]

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF**: Sending State S-[ID] / Receiving Process / Data Payload /
> Expected Acknowledgment / Failure Mode / Owner R-[ID]

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|

Minimum 3 rows; at least 1 AT-RISK citing a B-NN.

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN Cause field must satisfy both Dual-Cite Fail Conditions independently.
>
> **Dual-Cite Fail Condition A** -- no IM-ID literal string in Cause --> fails C-39.
> **Dual-Cite Fail Condition B** -- no R-ID literal string in Cause --> fails C-39.
>
> B-IDs must string-match: (1) PHASE EXIT GATE `Blocked bottleneck:`, (2) PHASE ENTRY CONTRACT
> `Prior phase blocked bottleneck:` in following phase, (3) EX block `Bottleneck Ref:` non-NONE.
>
> Concrete format example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`
> Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
> Fail condition: Field with no AT-RISK row-level S-ID specificity does not satisfy.
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
  - [List each AT-RISK SLA row citing B-02. Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]
- Exception Refs:
  - Required format: `EX-[Phase#][Letter] (Phase [N] -- [Exception Name])`
  - Fail condition: NONE = dark bottleneck (gate violation).
  - [List each EX block identifier whose `Bottleneck Ref:` cites B-02, or NONE.]

---

**Gap Identification**

> MISSING: [step name] -- [why it belongs; failure mode enabled; which phase; which IM-ID reduced]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA->B): [enumerate pairs or name gap]
- Backward (B->SLA): [enumerate or name gap]
- Exit gate consistency: [every exit gate B-ID matches a declared B-NN; name mismatch]
- Phase-boundary B-NN continuity: [exit gate B-ID matches next entry contract; list pairs]
- Phase-sequence: [every `Prior phase:` matches preceding block label; PHASE 1 NONE/INIT]
- Phase-exit-sequence: [every `Next phase:` matches subsequent block label; last phase NONE/END]
- Exception->B: [every EX `Bottleneck Ref:` B-ID matches a declared B-NN; list pairs]
- B-NN->Exception: [every declared B-ID has at least one non-NONE entry in its `Exception Refs:`; enumerate B-ID->EX pairs; name dark bottlenecks]
- Exception->Role: [every EX `Role Ref:` R-ID matches schedule primary owner; list pairs]
- Role->Exception: [every declared R-ID in at least one EX `Role Ref:`; list pairs; name dark roles]
- Dual-cite status: [every B-NN Cause has both IM-ID and R-ID; name missing]
- Baseline->Phase: [every PHASE ENTRY CONTRACT `IM Reference:` contains only declared IM-IDs; list phase->IM-ID pairs; NONE sentinels CLOSED]
- Baseline->Exception: [every EX block `IM Ref:` contains only declared IM-IDs or NONE; list EX->IM-ID pairs; name dark exceptions]
- Phase->Baseline: [bidirectional complement to Baseline->Phase; for each IM-ID cited in any
  PHASE ENTRY CONTRACT `IM Reference:` field, verify INCUMBENT BASELINE `Phase Refs:` for that
  IM-ID includes this phase by literal identifier; enumerate IM-ID->Phase Refs pairs; name any
  phase whose `IM Reference:` cites an IM-ID whose `Phase Refs:` does not list that phase
  (consistency failure); verify all NONE sentinels are accurate -- an IM-ID with NONE in
  `Phase Refs:` must not be cited by any PHASE ENTRY CONTRACT `IM Reference:` field]
- Gap (if OPEN): [unresolved direction and unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal name] | SUCCESS | [branch or state] |
| [failure terminal name] | FAILURE | [branch or state] |
| [cancel terminal name] | CANCEL | [branch or state] |

> Completeness check: Every exit branch must reach a declared terminal.

---
---

## V-05 -- Combination: Output Format + Lifecycle Emphasis + Inertia Framing (C-48 + C-49 + C-50)

**Variation axis**: Output format + Lifecycle emphasis + Inertia framing -- maximum structural
density for all three R16 criteria. (1) `Phase Refs:` back-reference annotations per IM-ID row
in INCUMBENT BASELINE (V-04 axis, C-48). (2) EXCEPTION BLOCK ARCHITECTURE header in SECTION A
preamble (V-02 axis, C-49). (3) DIRECTION INVENTORY block at CHAIN STATUS opening (V-03 axis,
C-50). CHAIN STATUS gains a `Phase->Baseline` direction (from C-48), bringing the total to 14
named directions. The DIRECTION INVENTORY enumerates the four canonical directions as an indexed
register at the section opening.

**Hypothesis**: V-05 is the minimum R16 configuration to achieve C-48, C-49, and C-50
simultaneously. Each structural addition is architecturally independent: C-48 lives in INCUMBENT
BASELINE rows and one CHAIN STATUS direction, C-49 lives in the SECTION A preamble, C-50 lives
at the CHAIN STATUS opening. The three additions do not interact structurally. If all three pass,
single-axis results from V-02/V-03/V-04 confirm each criterion is independently sufficient.
Expected: 42/42 = 10.000.

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
  consistency violation]
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
