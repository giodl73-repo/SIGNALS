# flow-lifecycle — Round 13 Variations (Rubric v13)

**Rubric**: v13 · 43 criteria (35 aspirational) · Ceiling entering R13: 35/35
(R12 V-02 cracked C-40 bidirectional; R12 V-05 confirmed C-40 + C-41 simultaneously —
all prior aspirationals signaled; v13 adds C-42 + C-43, raising ceiling from 33 to 35)

**Open criteria entering R13**: C-42 and C-43 — both new in rubric v13.

**Evidence from R12 excellence (C-40, C-41):**

- **C-40 signal**: R12 V-02 established that bidirectional closure — EX block `Role Ref: R-ID`
  PLUS Role Registry Gate fourth check (every declared R-ID appears in at least one EX block)
  — is required. Single-direction (R12 V-01 EX block only) was insufficient. The gate check
  is the discriminating property that closes the Role→Exception reverse direction.
- **C-41 signal**: R12 V-03 established that `Prior phase:` in PHASE ENTRY CONTRACT creates
  Phase→Phase backward sequential traceability as a named structural property. R12 V-05
  confirmed C-40 + C-41 compose without structural conflict.

**New criteria for R13:**

**C-42 — Exception Block Bottleneck Cross-Reference** (`depth`, C-42→C-04+C-13)

The EX block `Bottleneck Ref: B-ID` sub-field (established in R11) provides the
Exception→Bottleneck direction: each exception trace declares which bottleneck enabled it.
C-42 closes the reverse — Bottleneck→Exception — by adding a gate check to the Bottleneck
Analysis PREAMBLE: every declared B-ID must appear in at least one EX block's `Bottleneck
Ref:` field. B-IDs absent from all EX blocks are "dark bottlenecks": declared process failure
modes with no exception-phase trace. CHAIN STATUS gains a `B-NN→Exception` direction.
The analog to C-40: C-40 closed Role↔Exception; C-42 closes B-NN↔Exception.

**C-43 — Phase Exit Gate Forward Phase Sequential Linkage** (`format`, C-43→C-37+C-41)

C-41 added `Prior phase:` to PHASE ENTRY CONTRACT (backward: "which phase preceded me?").
C-43 adds `Next phase:` to PHASE EXIT GATE (forward: "which phase follows me?"). Last phase
carries NONE/END sentinel. Together C-41+C-43 complete bidirectional Phase→Phase gate-to-gate
linkage: out-of-order rendering detectable in both directions by identifier mismatch.
`Next phase:` is orthogonal to `Blocked bottleneck:` (C-37): one is a Phase label, one is a
B-ID. CHAIN STATUS gains a `Phase-exit-sequence` direction.

**Variation matrix:**

| Variation | Axes | B-NN→Exception gate check | Exception Refs in B-NN block | Next phase in exit gate | Primary hypothesis |
|-----------|------|---------------------------|------------------------------|-------------------------|--------------------|
| V-01 | G1 | YES (preamble gate only) | NO | NO | Gate check alone is the minimum for C-42; per-block listing is not required |
| V-02 | G1+G2 | YES (preamble gate) | YES (explicit per-B-NN field) | NO | C-42 requires bidirectional explicit listing — symmetric to C-40's Role Ref pattern |
| V-03 | H | NO | NO | YES | Phase exit Next phase sub-field alone surfaces C-43 independently of C-42 |
| V-04 | G1+H | YES (gate only) | NO | YES | C-42 minimum + C-43 compose without structural conflict |
| V-05 | G1+G2+H | YES (gate) | YES | YES | Maximum density: full bidirectional B↔Exception + Phase→Phase forward linkage |

**Structural change summary vs R12 V-05:**

| Section | R12 V-05 had | V-01 adds | V-02 adds | V-03 adds | V-04 adds | V-05 adds |
|---------|-------------|-----------|-----------|-----------|-----------|-----------|
| Bottleneck Analysis PREAMBLE | Dual-cite + Evidence format | B-NN→Exception gate check | B-NN→Exception gate + Exception Refs requirement | — | B-NN→Exception gate | B-NN→Exception gate + Exception Refs |
| B-NN blocks | Cause + Impact + Evidence | — | `Exception Refs:` sub-field | — | — | `Exception Refs:` sub-field |
| PHASE EXIT GATE | Exit Condition + Required outputs + Blocked bottleneck | — | — | `Next phase:` sub-field | `Next phase:` sub-field | `Next phase:` sub-field |
| CHAIN STATUS | 9 directions (through Role→Exception) | +`B-NN→Exception` | +`B-NN→Exception` (enhanced) | +`Phase-exit-sequence` | +both | +both (enhanced) |

---

## V-01 — Axis G1: B→Exception Gate Check (Single Direction)

**Variation axis**: Lifecycle emphasis — the Bottleneck Analysis PREAMBLE gains a gate check
verifying that every declared B-ID appears in at least one EX block's `Bottleneck Ref:`
sub-field across all phases. B-IDs present in the Bottleneck Analysis but absent from all EX
block `Bottleneck Ref:` fields are flagged as "dark bottlenecks" and constitute a gate
violation. The B-NN blocks themselves do not gain an `Exception Refs:` field; the gate check
is preamble-level only, requiring a forward scan after all phases are generated. CHAIN STATUS
gains a `B-NN→Exception` direction. No `Next phase:` sub-field is added to PHASE EXIT GATE.

**Hypothesis**: C-42 probes the B-NN→Exception gate check. If the minimum architecture is a
preamble-level verification that every declared B-ID is cited by at least one EX block —
symmetric to the Role Registry Gate's fourth check which verifies Role→Exception — then V-01
is the minimum to pass C-42. The B-NN block does not need an explicit `Exception Refs:` field
if the preamble performs the scan and names dark bottlenecks. If C-42 requires per-block
explicit listing (symmetric to Role Ref within EX blocks), then V-01 is insufficient and
V-02 is the minimum.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must satisfy both Dual-Cite
> Fail Conditions (IM-ID literal string and R-ID literal string). Quantified metric must appear
> before PHASE 1 in document order. A metric declared after PHASE 1 begins fails C-35.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: tools used (spreadsheets, email, phone), handoff
mechanisms, where records are stored, who initiates the process manually]

**Incumbent failure modes** (assign IM-ID to each):

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure in the manual process] | [daily / per-cycle / per-exception] | [what breaks downstream] |
| IM-02 | [second distinct failure mode] | [frequency] | [downstream effect] |

**Cost of no action**: [Named measure with current-state value or rate, declared before PHASE 1.
Example: "Average credit approval cycle time: 5.8 days vs 3-day SLA" or "Manual matching
error rate: 12% per period, generating 40+ exception tickets." Both IM-IDs above must be
reachable from at least one B-NN Cause field in Bottleneck Analysis below.]

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
- [ ] Each declared R-ID appears in at least one EX block's `Role Ref:` sub-field — R-IDs
      with no observable EX trace are "dark" roles and constitute a gate violation; identify
      any dark R-IDs before proceeding to phase content generation

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Role Sequence Schedule

> Declared after Role Registry Gate and before PHASE 1. Maps each R-ID to its active phases,
> activation trigger, handoff trigger, and any parallel windows. B-NN Cause fields must cite
> the blocking R-ID from this schedule (Dual-Cite Fail Condition B). R-IDs cited in EX block
> `Role Ref:` sub-fields must appear in this schedule as the phase owner for the enclosing
> phase. Every R-ID declared in the registry must appear in at least one EX block Role Ref —
> the Role Registry Gate fourth check is the structural enforcement of this property.

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior-process artifact — not "Start"] | [specific completion condition] | R-[ID] or NONE | [concurrent activity window or NONE] |
| Phase 2 | R-[ID] | [handoff received from phase 1 — name the artifact] | [completion condition] | R-[ID] or NONE | [concurrent activity or NONE] |

Rules:
- Every phase must have a Primary Owner.
- Activation Trigger for Phase 1 must name an external event or prior-process artifact.
- Handoff Trigger must be specific enough that a reviewer can determine the exact moment of transfer.
- Parallel windows must declare start/end states (S-IDs) when known.
- Every R-ID in this schedule must match an entry in the Role Registry Gate.

---

### Phase Structure

For each phase in the lifecycle, produce the following five blocks in document order:

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> This gate must be completed before SECTION A or SECTION B for this phase.
> Entry Condition must reference the prior phase's PHASE EXIT GATE "Required outputs" field
> by name — "previous phase complete" fails.
> Two sequential-linkage sub-fields are required and must not be conflated:
> `Prior phase:` carries the literal phase identifier (Phase→Phase backward linkage, C-41).
> `Prior phase blocked bottleneck:` carries the B-ID from the prior exit gate (B-NN boundary
> continuity). Both are independently verifiable by string comparison.

- Entry Condition: [specific named artifact or state record from prior phase's Required outputs]
- Pre-condition check: R-[ID] ([role name — must match Role Sequence Schedule primary owner for this phase]) — [verification method]
- Blocking condition: [if entry condition not met: which state is entered, which role notified, re-entry path]
- Prior phase: [Literal identifier of the preceding phase block, e.g., "PHASE 1 — Initiation".
  Phase 1 carries NONE or INIT as sentinel. A non-first phase carrying sentinel fails.
  A first phase carrying a phase identifier instead of sentinel fails.
  Must string-match the label of the preceding phase block in document order.]
- Prior phase blocked bottleneck: [B-ID from prior phase PHASE EXIT GATE `Blocked bottleneck:`
  or NONE if that field was NONE, or N/A for Phase 1. Must string-match prior exit gate field
  AND B-NN block identifier. Example: "B-01 (inherited from Phase 1 exit gate — manual
  reconciliation delay still active at phase boundary; R-02 blocking per Role Sequence Schedule)."]

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition — name the state, threshold breach, or missing input]
> - Trace: [path of states traversed from trigger to resolution or terminal; cite S-IDs in sequence]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason this failure mode matters]
> - Bottleneck Ref: [B-NN that enabled this exception, or NONE. B-ID must string-match a
>   Bottleneck Analysis identifier. Example: "B-01 — manual reconciliation backlog created the
>   missing-approval condition that triggered this exception." NONE if no declared bottleneck
>   was causal. This sub-field is the Exception→Bottleneck traceability artifact; the preamble
>   gate check in Bottleneck Analysis will verify the reverse direction (B-NN→Exception)
>   by checking that every declared B-ID appears in at least one block here.]
> - Role Ref: [R-ID of the ROLE SEQUENCE SCHEDULE primary owner for this phase. Must be a
>   literal R-ID matching the schedule entry for the enclosing phase. Example: "R-02 — GL
>   Manager owns Phase 2 per Role Sequence Schedule; exception escalates through their approval
>   queue." Free-text role name without R-ID fails. R-ID absent from schedule fails.]

Minimum 1 exception trace per phase. Minimum 3 exception traces total across all phases.
Every declared R-ID in the Role Registry Gate must appear in at least one EX block Role Ref.
Bottleneck Ref and Role Ref are independent; populate both for every EX block.

**SECTION B — STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules:
- Every state must have a named Entry Condition. "Ready" or "Previous step complete" fails.
- Every Exit must reference a destination S-ID or carry the label TERMINAL.
- Type values: NORMAL / DECISION / PARALLEL-FORK / PARALLEL-JOIN / EXCEPTION / TERMINAL

**Decision Supplement Blocks** (one per DECISION-type state in this phase):

> **DS-[S-ID] — [State Name]**
> - Condition: [the rule or threshold evaluated at this decision point]
> - Owner: R-[ID] ([role name from Role Registry])
> - Branch A ([condition outcome]): → S-[ID] ([state name])
> - Branch B ([condition outcome]): → S-[ID] ([state name]) or TERMINAL
> - Fallback: [action if condition cannot be evaluated — who is notified, what state is entered]

**PHASE EXIT GATE**

> `Blocked bottleneck:` names the B-ID that can delay this phase's exit, or NONE. The B-ID
> must string-match both: (1) the identifier declared in Bottleneck Analysis below, and (2)
> the next phase's PHASE ENTRY CONTRACT `Prior phase blocked bottleneck:` field.

- Exit Condition: [what the phase must have produced to be considered complete]
- Required outputs: [named artifacts, decisions, or state records that must exist]
- Exit verification: R-[ID] ([role name — must match Role Sequence Schedule primary owner]) confirms all required outputs are present
- Blocking condition: [if required outputs absent: re-entry path or escalation]
- Blocked bottleneck: [B-NN or NONE. B-ID declared here must appear in Bottleneck Analysis
  AND be mirrored in the next phase's PHASE ENTRY CONTRACT `Prior phase blocked bottleneck:`
  field. Example: "B-01 — manual spreadsheet reconciliation by R-02 delays GL approval exit;
  inherited by Phase 2 entry contract as prior-phase blocker."]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID] ([state name])
- **Branch 1**: [states traversed; cite S-IDs in sequence]
- **Branch 2**: [states traversed; cite S-IDs in sequence]
- **JOIN at**: S-[ID] ([join state name])
- **Join Condition**: AND-join (both branches must complete) / OR-join (first branch sufficient) — specify which applies and explain why this process requires that join type

---

### Edge Case Enumeration

At least three edge cases distinct from SECTION A exception flows:

> **EC-[N] — [Edge Case Name]**
> - Triggering Condition: [specific scenario that produces this edge case]
> - Why Problematic: [specific reason this falls outside documented handling]
> - Correct Response: R-[ID] ([role name]) — [specific correct action; name target state or resolution path]

---

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF — {Topic} lifecycle → [adjacent process name]**
> - Sending State: S-[ID] ([state name])
> - Receiving Process: [adjacent process name]
> - Data Payload: [named fields or record types transferred]
> - Expected Acknowledgment: [signal or confirmation message from receiving process]
> - Failure Mode: [what happens if acknowledgment not received within SLA]
> - Owner: R-[ID] ([role name])

---

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|
| | | | | AT-RISK / ON-TRACK | B-NN (if AT-RISK) |

Rules:
- AT-RISK = typical duration exceeds SLA target
- Every AT-RISK row must carry a Bottleneck Ref citing a B-NN from Bottleneck Analysis
- Minimum 3 annotated rows; at least 1 must be AT-RISK

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN Cause field must satisfy both of the following independent conditions.
>
> **Dual-Cite Fail Condition A** — Cause field contains no IM-ID literal string (e.g., "IM-01"):
> fails C-39. Verify: search Cause field text for "IM-" followed by digits. Absence → fail.
>
> **Dual-Cite Fail Condition B** — Cause field contains no R-ID literal string (e.g., "R-02"):
> fails C-39. Verify: search Cause field text for "R-" followed by digits. Absence → fail.
>
> B-IDs assigned here must string-match ALL of: (1) PHASE EXIT GATE `Blocked bottleneck:`
> fields, (2) PHASE ENTRY CONTRACT `Prior phase blocked bottleneck:` fields in the following
> phase, and (3) EX block `Bottleneck Ref:` fields where non-NONE.
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
> **B-NN→Exception Gate Check**: Every declared B-ID below must appear in at least one EX
> block's `Bottleneck Ref:` sub-field across all phases. A B-ID present in this section but
> absent from all EX block `Bottleneck Ref:` fields is a "dark bottleneck" — a declared
> process failure mode with no exception-phase trace, leaving the causal chain from bottleneck
> to observable exception unverifiable. Dark bottlenecks are gate violations. Verify after all
> phases are generated: for each declared B-ID, scan all EX blocks for a `Bottleneck Ref:`
> field containing that B-ID literal string. Absence → dark bottleneck gate violation. Report
> results in CHAIN STATUS `B-NN→Exception` direction.
>
> Anti-embedding: Do not embed CHAIN STATUS inside the SLA ANALYSIS section.
> Declare CHAIN STATUS in its own dedicated top-level section after SLA ANALYSIS.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field.**

---

**B-01 — [Bottleneck Name]**

- Cause: [specific cause. Required: cite IM-ID literal string (Fail Condition A) AND R-ID
  literal string (Fail Condition B). Example: "IM-01 (manual spreadsheet GL reconciliation)
  combined with R-02 (GL Manager) unavailable during period-close peak — causes queue
  accumulation at S-05. Dual-cite: 'IM-01' satisfies Condition A; 'R-02' satisfies Condition B."]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string → fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string → fails C-39
- Impact: [downstream state, SLA node, or adjacent process affected]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-01. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]

---

**B-02 — [Bottleneck Name]**

- Cause: [Required: IM-ID literal string (Condition A) AND R-ID literal string (Condition B).
  Example: "IM-02 (email approval routing without timestamp) combined with R-03 (Finance
  Controller) same-day unavailability — invoice matching queue at S-07."]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string → fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string → fails C-39
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-02. Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]

---

**Gap Identification**

> MISSING: [step name] — [rationale: why it belongs in this process model; what failure mode
> its absence enables; which phase it belongs in; which IM-ID it would reduce if present]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [every AT-RISK SLA row cites a B-ID; enumerate pairs or name gap]
- Backward (B→SLA): [every B-NN Evidence field lists AT-RISK SLA rows citing it; enumerate or name gap]
- Exit gate consistency: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID string-matches a declared B-NN; name any mismatch]
- Phase-boundary B-NN continuity: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID string-matches the next phase's PHASE ENTRY CONTRACT `Prior phase blocked bottleneck:`; list phase pairs or name break]
- Phase-sequence: [every PHASE ENTRY CONTRACT `Prior phase:` identifier string-matches the label of the preceding phase block; PHASE 1 carries NONE/INIT sentinel; list pairs or name mismatch]
- Exception→B: [every EX block `Bottleneck Ref:` B-ID (where non-NONE) matches a declared B-NN; list EX→B-NN pairs or name unresolved block]
- B-NN→Exception: [every declared B-ID appears in at least one EX block's `Bottleneck Ref:` sub-field; enumerate B-ID→EX block pairs; name any B-ID with no EX trace (dark bottleneck — gate violation)]
- Exception→Role: [every EX block `Role Ref:` R-ID matches the ROLE SEQUENCE SCHEDULE primary owner for the enclosing phase; list EX→R-ID pairs or name mismatch]
- Role→Exception: [every declared R-ID in the Role Registry Gate appears in at least one EX block's `Role Ref:` sub-field; list R-ID→EX pairs; name any R-ID with no EX trace (dark role)]
- Dual-cite status: [every B-NN Cause field contains both IM-ID and R-ID string; name any block missing either]
- Gap (if OPEN): [name the unresolved direction and the unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal name] | SUCCESS | [branch or state that reaches it] |
| [failure terminal name] | FAILURE | [branch or state that reaches it] |
| [cancel terminal name] | CANCEL | [branch or state that reaches it] |

> Completeness check: Every exit branch in every SECTION B state table must reach one of the
> declared terminals above. No branch may end at a non-terminal state without an explicit
> `continues-via: S-[ID]` pointer.

---
---

## V-02 — Axes G1+G2: B→Exception Gate Check + Explicit Exception Refs per B-NN Block

**Variation axis**: Output format — in addition to the preamble gate check (Axis G1), each
B-NN block gains an explicit `Exception Refs:` sub-field listing the EX block identifiers
whose `Bottleneck Ref:` cites this B-ID. The chain is closed bidirectionally from within the
B-NN block itself: a reviewer can navigate from any B-NN block directly to the exception
traces it underlies without scanning all EX blocks. Dark bottlenecks — B-IDs with an empty
or NONE `Exception Refs:` — are visible at the block level, not only at the preamble gate.
CHAIN STATUS `B-NN→Exception` direction verifies the explicit per-block refs against EX block
`Bottleneck Ref:` fields for string-comparison consistency.

**Hypothesis**: C-42 requires each B-NN block to carry an explicit `Exception Refs:` field
listing which EX blocks cite it — symmetric to how C-40 required each EX block to carry
`Role Ref: R-ID` naming the phase owner. If C-42 requires this structural symmetry (not just
a preamble gate check), then V-01 (preamble gate only) is insufficient and V-02 is the
minimum. The per-block field makes the B-NN→Exception direction string-comparable at the
block level, analogous to `Role Ref:` making the Exception→Role direction string-comparable
at the EX block level. If C-42 only requires the gate check without per-block explicit refs,
V-02 does not surface the criterion over V-01 — allowing the round to determine whether
per-block explicitness is discriminating.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must satisfy both Dual-Cite
> Fail Conditions. Quantified metric must appear before PHASE 1 in document order.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: tools used, handoff mechanisms, storage, initiator]

**Incumbent failure modes**:

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure] | [frequency] | [downstream effect] |
| IM-02 | [second distinct failure mode] | [frequency] | [downstream effect] |

**Cost of no action**: [Named quantified measure before PHASE 1. Both IM-IDs must be reachable
from at least one B-NN Cause field. Example: "Purchase order cycle time: 8.1 days against
5-day target" or "Manual matching error rate: 12% per period."]

---

### Role Registry Gate

> GATE BLOCK: Complete before Role Sequence Schedule and before tracing any state.
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
- [ ] Each declared R-ID appears in at least one EX block's `Role Ref:` sub-field — R-IDs
      with no observable EX trace are "dark" roles and constitute a gate violation

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Role Sequence Schedule

> Declared after Role Registry Gate and before PHASE 1. Maps each R-ID to active phases,
> activation trigger, handoff trigger, and parallel windows. B-NN Cause fields must cite
> the blocking R-ID (Dual-Cite Fail Condition B). R-IDs in EX block `Role Ref:` must match
> the schedule entry for the enclosing phase. Every declared R-ID must appear in at least
> one EX block Role Ref — the Role Registry Gate fourth check enforces this property.

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior-process artifact] | [specific completion condition] | R-[ID] or NONE | [concurrent window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1 — name the artifact] | [completion condition] | R-[ID] or NONE | [concurrent activity or NONE] |

Rules: Every phase must have a Primary Owner. Triggers must be specific. Parallel windows
must state start/end states (S-IDs). Every R-ID must match a Role Registry Gate entry.

---

### Phase Structure

For each phase, produce the following five blocks in document order:

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Entry Condition must reference the prior phase's PHASE EXIT GATE "Required outputs" by name.
> Two sequential-linkage sub-fields required and must not be conflated:
> `Prior phase:` = literal phase identifier (Phase→Phase backward linkage).
> `Prior phase blocked bottleneck:` = B-ID from prior exit gate (B-NN boundary continuity).

- Entry Condition: [specific named artifact from prior phase's Required outputs]
- Pre-condition check: R-[ID] ([role name — must match Role Sequence Schedule primary owner]) — [verification method]
- Blocking condition: [state entered and role notified if entry condition not met]
- Prior phase: [Literal identifier of preceding phase block, e.g., "PHASE 1 — Initiation".
  Phase 1 carries NONE or INIT as sentinel. Must string-match preceding phase block label.]
- Prior phase blocked bottleneck: [B-ID from prior exit gate `Blocked bottleneck:` or NONE
  or N/A for Phase 1. Must string-match prior exit gate AND B-NN block identifier.]

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition — name state, threshold breach, or missing input]
> - Trace: [states traversed from trigger to resolution or terminal; cite S-IDs]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason]
> - Bottleneck Ref: [B-NN that enabled this exception, or NONE. B-ID must string-match a
>   Bottleneck Analysis identifier. This sub-field is the Exception→Bottleneck artifact.
>   The reverse direction (B-NN→Exception) is closed by the per-B-NN `Exception Refs:` field
>   in Bottleneck Analysis — that field must list this EX block ID if Bottleneck Ref is
>   non-NONE. A non-NONE Bottleneck Ref here must have a corresponding `Exception Refs:`
>   entry in the cited B-NN block for the bidirectional chain to close.]
> - Role Ref: [R-ID of the ROLE SEQUENCE SCHEDULE primary owner for this phase. Must be a
>   literal R-ID matching the schedule entry for the enclosing phase.]

Minimum 1 per phase; 3 total minimum. Bottleneck Ref and Role Ref independent; populate both.

**SECTION B — STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules: Named Entry Condition required; Exits → S-ID or TERMINAL; standard Type values.

**Decision Supplement Blocks** (one per DECISION-type state):

> **DS-[S-ID] — [State Name]**
> - Condition: [rule or threshold]; Owner: R-[ID]; Branch A: → S-[ID]; Branch B: → S-[ID] or TERMINAL; Fallback: [action if undecidable]

**PHASE EXIT GATE**

> `Blocked bottleneck:` names the B-ID delaying this exit, or NONE. Must string-match:
> (1) Bottleneck Analysis identifier, (2) next phase's `Prior phase blocked bottleneck:`.

- Exit Condition: [what the phase must produce to be complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name — must match Role Sequence Schedule primary owner]) confirms all outputs present
- Blocking condition: [re-entry path or escalation if outputs absent]
- Blocked bottleneck: [B-NN or NONE. Must appear in Bottleneck Analysis AND in next phase's
  `Prior phase blocked bottleneck:`. Example: "B-01 — manual reconciliation by R-02 delays
  GL approval exit; carries forward to Phase 2 entry contract."]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID]; **Branch 1**: [S-IDs in sequence]; **Branch 2**: [S-IDs in sequence]
- **JOIN at**: S-[ID]; **Join Condition**: AND-join / OR-join — specify and explain

### Edge Case Enumeration

Three or more, distinct from SECTION A:

> **EC-[N]**: Triggering Condition / Why Problematic / Correct Response: R-[ID] — [action]

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
> **Dual-Cite Fail Condition A** — no IM-ID literal string in Cause → fails C-39.
> **Dual-Cite Fail Condition B** — no R-ID literal string in Cause → fails C-39.
>
> B-IDs here must string-match ALL of: (1) PHASE EXIT GATE `Blocked bottleneck:` fields,
> (2) PHASE ENTRY CONTRACT `Prior phase blocked bottleneck:` in the following phase, and
> (3) EX block `Bottleneck Ref:` fields where non-NONE.
>
> Concrete format example for Evidence field:
> `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`
>
> Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
> Fail condition: A field containing only "see SLA ANALYSIS" or state names without
> AT-RISK row-level S-ID specificity does not satisfy.
>
> **DUAL-LOCATION REQUIREMENTS:**
> (1) Concrete named domain example in BOTH preamble AND each B-NN per-block Evidence hint.
> (2) Labeled axes (`Required format:` / `Fail condition:`) in BOTH preamble AND each hint.
>
> **B-NN→Exception Gate Check + Explicit Refs**: Every declared B-ID must appear in at least
> one EX block's `Bottleneck Ref:` sub-field. Each B-NN block carries an explicit `Exception
> Refs:` sub-field listing the EX block identifiers that cite this B-ID. `Exception Refs: NONE`
> declares a dark bottleneck explicitly — any B-NN block with NONE fails the gate check.
> The `Exception Refs:` field makes the B-NN→Exception direction string-comparable at the
> block level without requiring a full EX block scan: verify each listed EX block ID has a
> `Bottleneck Ref:` field citing this B-ID by string comparison. CHAIN STATUS `B-NN→Exception`
> direction verifies both the field population and cross-reference consistency.
>
> Anti-embedding: Declare CHAIN STATUS in its own dedicated top-level section after SLA ANALYSIS.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field.**

---

**B-01 — [Bottleneck Name]**

- Cause: [Required: IM-ID literal string (Condition A) AND R-ID literal string (Condition B).
  Example: "IM-01 (manual spreadsheet GL reconciliation) combined with R-02 (GL Manager)
  period-close peak unavailability — queue accumulation at S-05. 'IM-01' satisfies A; 'R-02'
  satisfies B."]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string → fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string → fails C-39
- Impact: [downstream state, SLA node, or adjacent process affected]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-01. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]
- Exception Refs: [list EX block identifiers whose `Bottleneck Ref:` cites B-01. Format:
  "EX-1A (Phase 1 — [Exception Name]), EX-2B (Phase 2 — [Exception Name])". NONE if no EX
  block cites B-01 — this is a dark bottleneck and constitutes a gate violation. Each listed
  EX block ID must string-match an EX block where `Bottleneck Ref:` contains "B-01". A listed
  ID with no matching EX block entry fails the consistency check in CHAIN STATUS B-NN→Exception.]

---

**B-02 — [Bottleneck Name]**

- Cause: [Required: IM-ID literal string AND R-ID literal string.]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string → fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string → fails C-39
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-02. Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]
- Exception Refs: [list EX block identifiers whose `Bottleneck Ref:` cites B-02, or NONE
  (dark bottleneck — gate violation). Each listed ID must string-match an EX block with
  `Bottleneck Ref: B-02`.]

---

**Gap Identification**

> MISSING: [step name] — [why it belongs; failure mode enabled; which phase; which IM-ID reduced]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [every AT-RISK SLA row cites a B-ID; enumerate pairs or name gap]
- Backward (B→SLA): [every B-NN Evidence field lists AT-RISK SLA rows; enumerate or name gap]
- Exit gate consistency: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID matches a declared B-NN; name any mismatch]
- Phase-boundary B-NN continuity: [every exit gate B-ID matches next phase's `Prior phase blocked bottleneck:`; list pairs or name break]
- Phase-sequence: [every PHASE ENTRY CONTRACT `Prior phase:` matches preceding phase block label; PHASE 1 carries NONE/INIT; list pairs or name mismatch]
- Exception→B: [every EX block `Bottleneck Ref:` B-ID (non-NONE) matches a declared B-NN; list EX→B-NN pairs or name unresolved block]
- B-NN→Exception: [every declared B-ID has at least one entry in its `Exception Refs:` field (no NONE values); each listed EX block ID string-matches an EX block with `Bottleneck Ref:` citing this B-ID; enumerate B-ID→EX pairs; name any B-ID with NONE in Exception Refs (dark bottleneck) or any Exception Refs entry whose Bottleneck Ref does not match]
- Exception→Role: [every EX block `Role Ref:` R-ID matches ROLE SEQUENCE SCHEDULE primary owner; list EX→R-ID pairs or name mismatch]
- Role→Exception: [every declared R-ID appears in at least one EX block `Role Ref:`; list R-ID→EX pairs; name dark roles]
- Dual-cite status: [every B-NN Cause has both IM-ID and R-ID; name any block missing either]
- Gap (if OPEN): [unresolved direction and unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal name] | SUCCESS | [branch or state] |
| [failure terminal name] | FAILURE | [branch or state] |
| [cancel terminal name] | CANCEL | [branch or state] |

> Every exit branch must reach a declared terminal. No mid-flow endings without `continues-via:`.

---
---

## V-03 — Axis H: Phase Exit Gate Forward Phase Sequential Linkage

**Variation axis**: Lifecycle emphasis — each PHASE EXIT GATE gains a named `Next phase:`
sub-field carrying the literal identifier of the subsequent phase (e.g., "PHASE 2 — Credit
Review"). The last phase carries NONE or END as a sentinel. This is structurally distinct
from `Blocked bottleneck:` (C-37): that field carries a B-ID; `Next phase:` carries a Phase
identifier. Both sub-fields coexist in PHASE EXIT GATE independently. CHAIN STATUS gains a
`Phase-exit-sequence` direction verifying that every exit gate's `Next phase:` identifier
string-matches the subsequent phase's block label in document order. No B-NN→Exception gate
check is added to the Bottleneck Analysis (C-42 architecture is absent).

**Hypothesis**: C-43 requires the exit gate's Phase→Phase forward sequential linkage as a
named structural property, symmetric to C-41's `Prior phase:` in PHASE ENTRY CONTRACT.
When PHASE 1's exit gate declares `Next phase: PHASE 2 — Credit Review`, a reviewer can
verify phase sequence from the exit side by comparing the string to the label of the
subsequent phase block in document order, without inferred reading order. The last phase
sentinel (NONE/END) makes the terminal boundary explicit. V-03 isolates the `Next phase:`
addition from the C-42 B-NN→Exception gate check, verifying that phase-exit-sequence
traceability surfaces as an independent criterion. If C-43 requires both the `Next phase:`
field AND the `Prior phase:` field in a symmetric pair, C-41 is already in the base
architecture and V-03 carries both, making the pair visible.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must satisfy both Dual-Cite
> Fail Conditions. Quantified metric must appear before PHASE 1 in document order.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: tools used, handoff mechanisms, storage, initiator]

**Incumbent failure modes**:

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure] | [frequency] | [downstream effect] |
| IM-02 | [second distinct failure mode] | [frequency] | [downstream effect] |

**Cost of no action**: [Named quantified measure before PHASE 1. Both IM-IDs reachable from
at least one B-NN Cause field. Example: "Support case mean-time-to-resolve: 11.4 days vs
7-day SLA target" or "Duplicate payment rate: 4.7% per period."]

---

### Role Registry Gate

> GATE BLOCK: Complete before Role Sequence Schedule and before tracing any state.
> All four anti-generic checks must clear before proceeding.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [domain-specific role] | [named responsibility] |
| R-02 | [domain-specific role] | [named responsibility] |
| R-03 | [domain-specific role] | [named responsibility] |

Anti-generic validation (all four must clear):
- [ ] No R-ID entry uses "Approver" without a domain qualifier
- [ ] No R-ID entry uses "Owner" without a named responsibility
- [ ] Each R-ID referenced by at least one Decision Supplement block, Role Sequence Schedule,
      and at least one PHASE EXIT GATE Exit verification or Blocked bottleneck field
- [ ] Each declared R-ID appears in at least one EX block's `Role Ref:` sub-field

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Role Sequence Schedule

> Declared after Role Registry Gate and before PHASE 1. Maps each R-ID to active phases,
> activation trigger, handoff trigger, and parallel windows. B-NN Cause fields must cite
> the blocking R-ID (Dual-Cite Fail Condition B). R-IDs in EX block `Role Ref:` must match
> the schedule entry for the enclosing phase.

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior-process artifact] | [specific completion condition] | R-[ID] or NONE | [concurrent window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1] | [completion condition] | R-[ID] or NONE | [concurrent activity or NONE] |

Rules: Every phase must have a Primary Owner. Triggers must be specific. Every R-ID here
must match a Role Registry Gate entry.

---

### Phase Structure

For each phase, produce the following five blocks in document order:

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Entry Condition must reference the prior phase's PHASE EXIT GATE "Required outputs" by name.
> `Prior phase:` carries the literal phase identifier (Phase→Phase backward linkage, C-41).
> `Prior phase blocked bottleneck:` carries the B-ID from the prior exit gate.
> Both are independently verifiable by string comparison.

- Entry Condition: [specific named artifact from prior phase's Required outputs]
- Pre-condition check: R-[ID] ([role name]) — [verification method]
- Blocking condition: [state entered and role notified if entry condition not met]
- Prior phase: [Literal identifier of preceding phase block. Phase 1: NONE or INIT sentinel.
  Must string-match preceding phase block label in document order.]
- Prior phase blocked bottleneck: [B-ID from prior exit gate or NONE or N/A for Phase 1.
  Must string-match prior exit gate AND B-NN block identifier.]

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition]
> - Trace: [states traversed; cite S-IDs]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason]
> - Bottleneck Ref: [B-NN or NONE. B-ID must string-match a Bottleneck Analysis identifier.]
> - Role Ref: [R-ID of ROLE SEQUENCE SCHEDULE primary owner for this phase. Literal R-ID
>   matching the schedule entry for the enclosing phase.]

Minimum 1 per phase; 3 total minimum. Bottleneck Ref and Role Ref independent; populate both.

**SECTION B — STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules: Named Entry Condition required; Exits → S-ID or TERMINAL; standard Type values.

**Decision Supplement Blocks** (one per DECISION-type state):

> **DS-[S-ID]**: Condition / Owner R-[ID] / Branch A → S-[ID] / Branch B → S-[ID] or TERMINAL / Fallback

**PHASE EXIT GATE**

> `Blocked bottleneck:` names the B-ID that can delay this exit, or NONE. Must string-match
> Bottleneck Analysis identifier AND next phase's `Prior phase blocked bottleneck:`.
> `Next phase:` is a SEPARATE sub-field carrying the Phase identifier of the subsequent phase
> — not a B-ID. These two sub-fields are orthogonal and must not be conflated:
> `Blocked bottleneck:` carries a B-ID; `Next phase:` carries a Phase label.

- Exit Condition: [what the phase must produce to be complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name — must match Role Sequence Schedule primary owner]) confirms all outputs present
- Blocking condition: [re-entry path or escalation if outputs absent]
- Blocked bottleneck: [B-NN or NONE. Must appear in Bottleneck Analysis AND in next phase's
  `Prior phase blocked bottleneck:`. Example: "B-01 — manual reconciliation by R-02 delays
  GL approval exit; inherited by Phase 2 as prior-phase blocker."]
- Next phase: [Literal identifier of the subsequent phase block, e.g., "PHASE 2 — Credit
  Review". Last phase carries NONE or END as sentinel. Must string-match the label of the
  next phase block in document order. A non-last phase carrying sentinel fails. A last phase
  carrying a phase identifier instead of sentinel fails. Together with the next phase's
  PHASE ENTRY CONTRACT `Prior phase:` field (C-41), this completes bidirectional Phase→Phase
  gate-to-gate linkage: entry contracts declare backward (which phase preceded); exit gates
  declare forward (which phase follows). Out-of-order rendering is detectable from both
  directions by identifier mismatch, independent of document position.]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID]; **Branch 1**: [S-IDs]; **Branch 2**: [S-IDs]
- **JOIN at**: S-[ID]; **Join Condition**: AND-join / OR-join — specify and explain

### Edge Case Enumeration

Three or more, distinct from SECTION A:

> **EC-[N]**: Triggering Condition / Why Problematic / Correct Response: R-[ID] — [action]

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
> **Dual-Cite Fail Condition A** — no IM-ID literal string in Cause → fails C-39.
> **Dual-Cite Fail Condition B** — no R-ID literal string in Cause → fails C-39.
>
> B-IDs here must string-match ALL of: (1) PHASE EXIT GATE `Blocked bottleneck:` fields,
> (2) PHASE ENTRY CONTRACT `Prior phase blocked bottleneck:` in the following phase, and
> (3) EX block `Bottleneck Ref:` fields where non-NONE.
>
> Concrete format example for Evidence field:
> `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`
>
> Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
> Fail condition: A field containing only "see SLA ANALYSIS" or state names without
> AT-RISK row-level S-ID specificity does not satisfy.
>
> **DUAL-LOCATION REQUIREMENTS:**
> (1) Concrete named domain example in BOTH preamble AND each B-NN per-block Evidence hint.
> (2) Labeled axes (`Required format:` / `Fail condition:`) in BOTH preamble AND each hint.
>
> Anti-embedding: Declare CHAIN STATUS in its own dedicated top-level section after SLA ANALYSIS.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field.**

---

**B-01 — [Bottleneck Name]**

- Cause: [Required: IM-ID literal string (Condition A) AND R-ID literal string (Condition B).
  Example: "IM-01 (manual spreadsheet GL reconciliation) combined with R-02 (GL Manager)
  unavailable during period-close peak — queue accumulation at S-05."]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string → fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string → fails C-39
- Impact: [downstream state, SLA node, or adjacent process]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-01. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]

---

**B-02 — [Bottleneck Name]**

- Cause: [Required: IM-ID AND R-ID literal strings.]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string → fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string → fails C-39
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: [same as B-01]
  - [List each AT-RISK SLA row citing B-02.]

---

**Gap Identification**

> MISSING: [step name] — [why it belongs; failure mode enabled; which phase; which IM-ID reduced]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [every AT-RISK SLA row cites a B-ID; enumerate pairs or name gap]
- Backward (B→SLA): [every B-NN Evidence field lists AT-RISK SLA rows; enumerate or name gap]
- Exit gate consistency: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID matches a declared B-NN; name any mismatch]
- Phase-boundary B-NN continuity: [every exit gate B-ID matches next phase's `Prior phase blocked bottleneck:`; list pairs or name break]
- Phase-sequence: [every PHASE ENTRY CONTRACT `Prior phase:` matches preceding phase block label; PHASE 1 carries NONE/INIT; list pairs or name mismatch]
- Phase-exit-sequence: [every PHASE EXIT GATE `Next phase:` identifier string-matches the label of the subsequent phase block in document order; last phase carries NONE/END sentinel; list exit gate→next phase pairs or name any mismatch, non-last phase with sentinel, or last phase without sentinel]
- Exception→B: [every EX block `Bottleneck Ref:` B-ID (non-NONE) matches a declared B-NN; list EX→B-NN pairs or name unresolved block]
- Exception→Role: [every EX block `Role Ref:` R-ID matches ROLE SEQUENCE SCHEDULE primary owner; list EX→R-ID pairs or name mismatch]
- Role→Exception: [every declared R-ID appears in at least one EX block `Role Ref:`; list R-ID→EX pairs; name dark roles]
- Dual-cite status: [every B-NN Cause has both IM-ID and R-ID; name any block missing either]
- Gap (if OPEN): [unresolved direction and unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal name] | SUCCESS | [branch or state] |
| [failure terminal name] | FAILURE | [branch or state] |
| [cancel terminal name] | CANCEL | [branch or state] |

> Every exit branch must reach a declared terminal. No mid-flow endings without `continues-via:`.

---
---

## V-04 — Axes G1+H: B→Exception Gate Check + Phase Exit Forward Linkage

**Variation axis**: Role sequence + lifecycle emphasis — two orthogonal new sub-fields added
simultaneously: the Bottleneck Analysis PREAMBLE gains the B-NN→Exception gate check (Axis
G1), and each PHASE EXIT GATE gains a `Next phase:` sub-field (Axis H). No `Exception Refs:`
field is added to B-NN blocks (Axis G2 is absent). Tests whether C-42 minimum (gate check
only) and C-43 (exit gate `Next phase:`) compose without structural ambiguity or requiring
cross-field coordination.

**Hypothesis**: C-42 and C-43 probe independent traceability directions with no shared state:
the B-NN→Exception gate check operates on the bottleneck-to-exception axis; `Next phase:`
in exit gates operates on the phase-sequence axis. When both are active simultaneously, each
should remain independently evaluable. If both can be populated without conflicting with
existing fields (`Blocked bottleneck:`, `Prior phase blocked bottleneck:`), V-04 demonstrates
architectural composability and may be the minimum for both C-42 and C-43 to be simultaneously
detectable. Absence of Axis G2 means if C-42 requires per-block explicit refs, V-04 would fail
C-42 while passing C-43 — allowing the round to isolate the discriminating property.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must satisfy both Dual-Cite
> Fail Conditions. Quantified metric must appear before PHASE 1 in document order.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: tools used, handoff mechanisms, storage, initiator]

**Incumbent failure modes**:

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure] | [frequency] | [downstream effect] |
| IM-02 | [second distinct failure mode] | [frequency] | [downstream effect] |

**Cost of no action**: [Named quantified measure before PHASE 1. Both IM-IDs reachable from
at least one B-NN Cause field. Example: "Average credit approval cycle time: 5.8 days vs
3-day SLA" or "Goods receipt discrepancy rate: 8.4% per period."]

---

### Role Registry Gate

> GATE BLOCK: All four anti-generic checks must clear before proceeding.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [domain-specific role] | [named responsibility] |
| R-02 | [domain-specific role] | [named responsibility] |
| R-03 | [domain-specific role] | [named responsibility] |

Anti-generic validation (all four must clear):
- [ ] No R-ID entry uses "Approver" without a domain qualifier
- [ ] No R-ID entry uses "Owner" without a named responsibility
- [ ] Each R-ID referenced by at least one Decision Supplement block, Role Sequence Schedule,
      and at least one PHASE EXIT GATE Exit verification or Blocked bottleneck field
- [ ] Each declared R-ID appears in at least one EX block's `Role Ref:` sub-field

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Role Sequence Schedule

> Declared after Role Registry Gate and before PHASE 1. B-NN Cause fields must cite the
> blocking R-ID (Dual-Cite Fail Condition B). R-IDs in EX block `Role Ref:` must match the
> schedule entry for the enclosing phase.

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior-process artifact] | [specific completion condition] | R-[ID] or NONE | [concurrent window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1] | [completion condition] | R-[ID] or NONE | [concurrent activity or NONE] |

---

### Phase Structure

For each phase, produce the following five blocks in document order:

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Entry Condition references prior phase's PHASE EXIT GATE "Required outputs" by name.
> `Prior phase:` = literal phase identifier (backward Phase→Phase linkage, C-41).
> `Prior phase blocked bottleneck:` = B-ID from prior exit gate (B-NN continuity).

- Entry Condition: [specific named artifact from prior phase's Required outputs]
- Pre-condition check: R-[ID] ([role name]) — [verification method]
- Blocking condition: [state entered and role notified if entry condition not met]
- Prior phase: [Literal identifier of preceding phase block. Phase 1: NONE or INIT sentinel.]
- Prior phase blocked bottleneck: [B-ID from prior exit gate or NONE or N/A for Phase 1.]

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition]; Trace: [S-IDs]; Handling Role: R-[ID]; Terminal: [state or continues-via]
> - Why Problematic: [specific reason]
> - Bottleneck Ref: [B-NN or NONE. B-ID string-matches a Bottleneck Analysis identifier.
>   The preamble gate check will verify that this B-ID appears here to close the B-NN→Exception
>   direction — populate accurately.]
> - Role Ref: [R-ID of ROLE SEQUENCE SCHEDULE primary owner for this phase. Literal R-ID.]

Minimum 1 per phase; 3 total minimum. Bottleneck Ref and Role Ref independent; populate both.

**SECTION B — STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules: Named Entry Condition required; Exits → S-ID or TERMINAL; standard Type values.

**Decision Supplement Blocks** (one per DECISION-type state):

> **DS-[S-ID]**: Condition / Owner R-[ID] / Branch A → S-[ID] / Branch B → S-[ID] or TERMINAL / Fallback

**PHASE EXIT GATE**

> Two sub-fields carry independent traceability directions and must not be conflated:
> `Blocked bottleneck:` carries a B-ID (phase→B-NN forward reference, C-37).
> `Next phase:` carries a Phase identifier (phase→phase forward linkage, C-43).
> The B-ID from `Blocked bottleneck:` is inherited by the next phase's PHASE ENTRY CONTRACT
> `Prior phase blocked bottleneck:`. The Phase label from `Next phase:` is the string target
> for the next phase's block label — verifiable by string comparison from the exit gate side.

- Exit Condition: [what the phase must produce to be complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name — must match Role Sequence Schedule primary owner]) confirms all outputs present
- Blocking condition: [re-entry path or escalation if outputs absent]
- Blocked bottleneck: [B-NN or NONE. Must appear in Bottleneck Analysis AND in next phase's
  `Prior phase blocked bottleneck:`.]
- Next phase: [Literal identifier of the subsequent phase block, e.g., "PHASE 2 — Credit
  Review". Last phase carries NONE or END sentinel. Must string-match next phase block label.
  Non-last phase with sentinel fails. Last phase with phase identifier fails.]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID]; **Branch 1**: [S-IDs]; **Branch 2**: [S-IDs]
- **JOIN at**: S-[ID]; **Join Condition**: AND-join / OR-join — specify and explain

### Edge Case Enumeration

Three or more, distinct from SECTION A:

> **EC-[N]**: Triggering Condition / Why Problematic / Correct Response: R-[ID] — [action]

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
> **Dual-Cite Fail Condition A** — no IM-ID literal string in Cause → fails C-39.
> **Dual-Cite Fail Condition B** — no R-ID literal string in Cause → fails C-39.
>
> B-IDs here must string-match ALL of: (1) PHASE EXIT GATE `Blocked bottleneck:` fields,
> (2) PHASE ENTRY CONTRACT `Prior phase blocked bottleneck:` in the following phase, and
> (3) EX block `Bottleneck Ref:` fields where non-NONE.
>
> Concrete format example for Evidence field:
> `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`
>
> Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
> Fail condition: A field containing only "see SLA ANALYSIS" or state names without
> AT-RISK row-level S-ID specificity does not satisfy.
>
> **DUAL-LOCATION REQUIREMENTS:**
> (1) Concrete named domain example in BOTH preamble AND each B-NN per-block Evidence hint.
> (2) Labeled axes (`Required format:` / `Fail condition:`) in BOTH preamble AND each hint.
>
> **B-NN→Exception Gate Check**: Every declared B-ID below must appear in at least one EX
> block's `Bottleneck Ref:` sub-field across all phases. A B-ID absent from all EX blocks is
> a "dark bottleneck" — declared failure mode with no exception-phase trace. Dark bottlenecks
> are gate violations. Verify after all phases: for each declared B-ID, scan EX blocks for
> `Bottleneck Ref:` containing that B-ID literal string. Absence → dark bottleneck violation.
> Report in CHAIN STATUS `B-NN→Exception` direction.
>
> Anti-embedding: Declare CHAIN STATUS in its own dedicated top-level section after SLA ANALYSIS.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field.**

---

**B-01 — [Bottleneck Name]**

- Cause: [Required: IM-ID literal string (Condition A) AND R-ID literal string (Condition B).]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string → fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string → fails C-39
- Impact: [downstream state, SLA node, or adjacent process]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-01. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]

---

**B-02 — [Bottleneck Name]**

- Cause: [Required: IM-ID AND R-ID literal strings.]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string → fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string → fails C-39
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: [same as B-01]
  - [List each AT-RISK SLA row citing B-02.]

---

**Gap Identification**

> MISSING: [step name] — [why it belongs; failure mode enabled; which phase; which IM-ID reduced]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [every AT-RISK SLA row cites a B-ID; enumerate pairs or name gap]
- Backward (B→SLA): [every B-NN Evidence field lists AT-RISK SLA rows; enumerate or name gap]
- Exit gate consistency: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID matches a declared B-NN; name any mismatch]
- Phase-boundary B-NN continuity: [every exit gate B-ID matches next phase's `Prior phase blocked bottleneck:`; list pairs or name break]
- Phase-sequence: [every PHASE ENTRY CONTRACT `Prior phase:` matches preceding phase block label; PHASE 1 carries NONE/INIT; list pairs or name mismatch]
- Phase-exit-sequence: [every PHASE EXIT GATE `Next phase:` identifier string-matches the label of the subsequent phase block; last phase carries NONE/END sentinel; list exit gate→next phase pairs or name any mismatch or missing sentinel]
- Exception→B: [every EX block `Bottleneck Ref:` B-ID (non-NONE) matches a declared B-NN; list EX→B-NN pairs or name unresolved]
- B-NN→Exception: [every declared B-ID appears in at least one EX block's `Bottleneck Ref:` sub-field; enumerate B-ID→EX pairs; name any B-ID with no EX trace (dark bottleneck — gate violation)]
- Exception→Role: [every EX block `Role Ref:` R-ID matches ROLE SEQUENCE SCHEDULE primary owner; list EX→R-ID pairs or name mismatch]
- Role→Exception: [every declared R-ID appears in at least one EX block `Role Ref:`; list R-ID→EX pairs; name dark roles]
- Dual-cite status: [every B-NN Cause has both IM-ID and R-ID; name any block missing either]
- Gap (if OPEN): [unresolved direction and unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal name] | SUCCESS | [branch or state] |
| [failure terminal name] | FAILURE | [branch or state] |
| [cancel terminal name] | CANCEL | [branch or state] |

> Every exit branch must reach a declared terminal. No mid-flow endings without `continues-via:`.

---
---

## V-05 — Axes G1+G2+H: Full Bidirectional B↔Exception + Phase Exit Forward Linkage

**Variation axis**: Phrasing register (imperative + descriptive) — maximum traceability
density for the two new criteria: full bidirectional B-NN↔Exception (preamble gate check
plus explicit `Exception Refs:` field in each B-NN block, Axes G1+G2) plus Phase Exit
`Next phase:` sub-field (Axis H). CHAIN STATUS verifies all new directions. If C-42 requires
the per-block explicit `Exception Refs:` field AND C-43 requires the exit gate `Next phase:`
field, V-05 is the only configuration where both criteria can simultaneously pass at their
strongest form. The variation also surfaces whether the three additions create structural
conflicts or unexpected interactions in the generating model's output.

**Hypothesis**: If C-42 requires per-block explicit listing (symmetric to C-40's Role Ref
pattern) AND C-43 requires exit gate `Next phase:` (symmetric to C-41's entry contract
`Prior phase:` pattern), then V-05 is the minimum for both to pass simultaneously at full
strength. V-02 would pass C-42 without C-43; V-03 would pass C-43 without C-42; V-04 would
pass C-43 and possibly C-42 at gate-only level; only V-05 can pass both at maximum fidelity.
The combination also tests structural independence: `Exception Refs:` in B-NN blocks operates
on the bottleneck axis; `Next phase:` in exit gates operates on the phase-sequence axis — no
shared state is expected, but generating both simultaneously may surface unexpected coupling.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must satisfy both Dual-Cite
> Fail Conditions. Quantified metric must appear before PHASE 1 in document order.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: tools used, handoff mechanisms, storage, initiator]

**Incumbent failure modes**:

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure] | [frequency] | [downstream effect] |
| IM-02 | [second distinct failure mode] | [frequency] | [downstream effect] |

**Cost of no action**: [Named quantified measure before PHASE 1. Both IM-IDs reachable from
at least one B-NN Cause field. Example: "Manual GL reconciliation error rate: 6.3% per
period" or "Average case escalation lag: 4.2 days beyond SLA."]

---

### Role Registry Gate

> GATE BLOCK: Complete before Role Sequence Schedule and before tracing any state.
> All four anti-generic checks must clear before proceeding.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [domain-specific role] | [named responsibility] |
| R-02 | [domain-specific role] | [named responsibility] |
| R-03 | [domain-specific role] | [named responsibility] |

Anti-generic validation (all four must clear):
- [ ] No R-ID entry uses "Approver" without a domain qualifier
- [ ] No R-ID entry uses "Owner" without a named responsibility
- [ ] Each R-ID referenced by at least one Decision Supplement block, Role Sequence Schedule,
      and at least one PHASE EXIT GATE Exit verification or Blocked bottleneck field
- [ ] Each declared R-ID appears in at least one EX block's `Role Ref:` sub-field — R-IDs
      with no observable EX trace are "dark" roles and constitute a gate violation

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Role Sequence Schedule

> Declared after Role Registry Gate and before PHASE 1. Maps each R-ID to active phases,
> activation trigger, handoff trigger, and parallel windows. B-NN Cause fields must cite
> the blocking R-ID (Dual-Cite Fail Condition B). R-IDs cited in EX block `Role Ref:` must
> match the schedule entry for the enclosing phase. Every declared R-ID must appear in at
> least one EX block Role Ref — the Role Registry Gate fourth check enforces this property.

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior-process artifact — not "Start"] | [specific completion condition] | R-[ID] or NONE | [concurrent window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1 — name the artifact] | [completion condition] | R-[ID] or NONE | [concurrent activity or NONE] |

Rules: Every phase must have a Primary Owner. Triggers must be specific. Every R-ID here
must match a Role Registry Gate entry. Parallel windows must state start/end S-IDs when known.

---

### Phase Structure

For each phase in the lifecycle, produce the following five blocks in document order:

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Entry Condition must reference the prior phase's PHASE EXIT GATE "Required outputs" by name.
> Three sequential-linkage sub-fields are in play across ENTRY CONTRACT and EXIT GATE:
> ENTRY CONTRACT `Prior phase:` = backward Phase→Phase linkage (C-41, this block).
> ENTRY CONTRACT `Prior phase blocked bottleneck:` = B-NN boundary continuity (C-37 inheritance).
> EXIT GATE `Next phase:` = forward Phase→Phase linkage (C-43, exit gate below).
> `Prior phase:` and `Next phase:` form a bidirectional pair; `Prior phase blocked bottleneck:`
> is orthogonal — it carries a B-ID, not a Phase label. Do not conflate any of the three.

- Entry Condition: [specific named artifact from prior phase's Required outputs]
- Pre-condition check: R-[ID] ([role name — must match Role Sequence Schedule primary owner for this phase]) — [verification method]
- Blocking condition: [state entered and role notified if entry condition not met]
- Prior phase: [Literal identifier of preceding phase block, e.g., "PHASE 1 — Initiation".
  Phase 1 carries NONE or INIT as sentinel. Must string-match preceding phase block label.
  Fails if: non-first phase carries sentinel; first phase carries a phase identifier; identifier
  does not match preceding phase block label in document order.]
- Prior phase blocked bottleneck: [B-ID from prior exit gate `Blocked bottleneck:` or NONE
  or N/A for Phase 1. Must string-match prior exit gate AND B-NN block identifier. Example:
  "B-01 (inherited from Phase 1 exit gate — manual reconciliation delay still active at phase
  boundary; R-02 is the blocking role per Role Sequence Schedule)."]

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition — name state, threshold breach, or missing input]
> - Trace: [path of states from trigger to resolution or terminal; cite S-IDs in sequence]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason this failure mode matters]
> - Bottleneck Ref: [B-NN that enabled this exception, or NONE. B-ID must string-match a
>   Bottleneck Analysis identifier. This is the Exception→Bottleneck direction. The reverse
>   direction (B-NN→Exception) is closed by the `Exception Refs:` field in each B-NN block —
>   that field must list this EX block ID if Bottleneck Ref is non-NONE. Accurate population
>   is required: if B-01 is cited here, B-01's `Exception Refs:` must list this EX block ID.
>   Inconsistency between Bottleneck Ref here and Exception Refs in the B-NN block produces
>   an OPEN CHAIN STATUS B-NN→Exception direction.]
> - Role Ref: [R-ID of the ROLE SEQUENCE SCHEDULE primary owner for this phase. Must be a
>   literal R-ID matching the schedule's Primary Owner entry for the phase containing this
>   exception. This field is required for the Role Registry Gate fourth check: every declared
>   R-ID must appear here in at least one EX block. Example: "R-02 — GL Manager owns Phase 2
>   per Role Sequence Schedule; this exception escalates through their approval queue."
>   Free-text role name without R-ID fails. R-ID absent from schedule fails.]

Minimum 1 exception trace per phase; 3 total minimum. Every declared R-ID in the Role
Registry Gate must appear in at least one EX block Role Ref. Bottleneck Ref and Role Ref
are independent sub-fields; populate both for every EX block.

**SECTION B — STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules:
- Every state must have a named Entry Condition. "Ready" or "Previous step complete" fails.
- Every Exit must reference a destination S-ID or carry the label TERMINAL.
- Type values: NORMAL / DECISION / PARALLEL-FORK / PARALLEL-JOIN / EXCEPTION / TERMINAL

**Decision Supplement Blocks** (one per DECISION-type state in this phase):

> **DS-[S-ID] — [State Name]**
> - Condition: [rule or threshold evaluated]
> - Owner: R-[ID] ([role name from Role Registry])
> - Branch A ([outcome]): → S-[ID] ([state name])
> - Branch B ([outcome]): → S-[ID] ([state name]) or TERMINAL
> - Fallback: [action if condition cannot be evaluated]

**PHASE EXIT GATE**

> This gate carries three distinct sub-fields. Two must not be conflated:
> `Blocked bottleneck:` = B-ID that can delay this exit (Phase→B-NN forward reference, C-37).
>   Must string-match Bottleneck Analysis AND next phase's `Prior phase blocked bottleneck:`.
> `Next phase:` = Phase identifier of the subsequent phase (Phase→Phase forward linkage, C-43).
>   Must string-match the label of the next phase block in document order.
> These fields operate on independent axes: one carries a B-ID; one carries a Phase label.
> The bidirectional Phase→Phase pair is now complete: `Prior phase:` in ENTRY CONTRACT
> (backward: "who preceded me?") and `Next phase:` in EXIT GATE (forward: "who follows me?").

- Exit Condition: [what the phase must have produced to be considered complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name — must match Role Sequence Schedule primary owner]) confirms all required outputs present
- Blocking condition: [if required outputs absent: re-entry path or escalation]
- Blocked bottleneck: [B-NN or NONE. Must appear in Bottleneck Analysis AND in next phase's
  `Prior phase blocked bottleneck:`. Example: "B-01 — manual spreadsheet reconciliation by
  R-02 delays GL approval exit; carries forward to Phase 2 entry contract as prior-phase
  blocker. Also: if EX blocks cite B-01, this B-ID appears in their `Exception Refs:` field
  in the Bottleneck Analysis to close the bidirectional chain."]
- Next phase: [Literal identifier of the subsequent phase block, e.g., "PHASE 2 — Credit
  Review". Last phase carries NONE or END as sentinel. Must string-match the label of the
  next phase block in document order. Non-last phase with sentinel fails. Last phase with
  phase identifier instead of sentinel fails. Together with this phase's PHASE ENTRY CONTRACT
  `Prior phase:` field (C-41) and the next phase's PHASE ENTRY CONTRACT `Prior phase:` field,
  bidirectional Phase→Phase linkage is complete: exit gate looks forward; entry contract looks
  backward. CHAIN STATUS `Phase-exit-sequence` verifies this direction.]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID] ([state name])
- **Branch 1**: [states traversed; cite S-IDs in sequence]
- **Branch 2**: [states traversed; cite S-IDs in sequence]
- **JOIN at**: S-[ID] ([join state name])
- **Join Condition**: AND-join (both branches must complete) / OR-join (first branch sufficient) — specify which applies and explain why this process requires that join type

---

### Edge Case Enumeration

At least three edge cases distinct from SECTION A exception flows:

> **EC-[N] — [Edge Case Name]**
> - Triggering Condition: [specific scenario]
> - Why Problematic: [specific reason outside documented handling]
> - Correct Response: R-[ID] ([role name]) — [specific correct action; name target state or resolution path]

---

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF — {Topic} lifecycle → [adjacent process name]**
> - Sending State: S-[ID] ([state name])
> - Receiving Process: [adjacent process name]
> - Data Payload: [named fields or record types transferred]
> - Expected Acknowledgment: [signal or confirmation message from receiving process]
> - Failure Mode: [what happens if acknowledgment not received within SLA]
> - Owner: R-[ID] ([role name])

---

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|
| | | | | AT-RISK / ON-TRACK | B-NN (if AT-RISK) |

Rules:
- AT-RISK = typical duration exceeds SLA target
- Every AT-RISK row must carry a Bottleneck Ref citing a B-NN from Bottleneck Analysis
- Minimum 3 annotated rows; at least 1 must be AT-RISK

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN Cause field must satisfy both of the following independent conditions.
>
> **Dual-Cite Fail Condition A** — Cause field contains no IM-ID literal string (e.g., "IM-01"):
> fails C-39. Verify: search Cause field text for "IM-" followed by digits. Absence → fail.
>
> **Dual-Cite Fail Condition B** — Cause field contains no R-ID literal string (e.g., "R-02"):
> fails C-39. Verify: search Cause field text for "R-" followed by digits. Absence → fail.
>
> B-IDs assigned here must string-match ALL of: (1) PHASE EXIT GATE `Blocked bottleneck:`
> fields, (2) PHASE ENTRY CONTRACT `Prior phase blocked bottleneck:` fields in the following
> phase, and (3) EX block `Bottleneck Ref:` fields where non-NONE. All four contexts must
> be consistent.
>
> Concrete format example for Evidence field:
> `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`
>
> Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
> Fail condition: A field containing only "see SLA ANALYSIS" or state names without
> AT-RISK row-level S-ID specificity does not satisfy.
>
> **DUAL-LOCATION REQUIREMENTS:**
> (1) Concrete named domain example (`"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`)
> must appear in BOTH this preamble AND each B-NN per-block Evidence hint.
> (2) Labeled axes (`Required format:` / `Fail condition:`) must appear in BOTH this preamble
> AND each B-NN per-block Evidence hint.
>
> **B-NN→Exception Gate Check + Explicit Refs**: Every declared B-ID must appear in at least
> one EX block's `Bottleneck Ref:` sub-field. Each B-NN block carries an explicit `Exception
> Refs:` sub-field listing the EX block identifiers whose `Bottleneck Ref:` cites this B-ID.
> `Exception Refs: NONE` declares a dark bottleneck — any B-NN block with NONE fails the gate
> check and produces an OPEN CHAIN STATUS B-NN→Exception direction. Verify each listed EX
> block ID by string comparison to EX blocks with matching `Bottleneck Ref:` field. This closes
> the B-NN↔Exception chain bidirectionally: Exception→B is carried in EX block `Bottleneck
> Ref:`; B-NN→Exception is carried in B-NN block `Exception Refs:`. Both directions are
> string-comparable without scanning.
>
> Anti-embedding: Do not embed CHAIN STATUS inside the SLA ANALYSIS section.
> Declare CHAIN STATUS in its own dedicated top-level section after SLA ANALYSIS.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field.**

---

**B-01 — [Bottleneck Name]**

- Cause: [Required: IM-ID literal string (Condition A) AND R-ID literal string (Condition B).
  Example: "IM-01 (manual spreadsheet GL reconciliation) combined with R-02 (GL Manager)
  period-close peak unavailability — causes queue accumulation at S-05. R-02 is Phase 2
  primary owner per Role Sequence Schedule. This B-ID appears in: Phase 1 exit gate
  `Blocked bottleneck:`, Phase 2 entry contract `Prior phase blocked bottleneck:`, and any
  EX block with `Bottleneck Ref: B-01` listed in Exception Refs below.
  Dual-cite: 'IM-01' satisfies Condition A; 'R-02' satisfies Condition B."]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string → fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string → fails C-39
- Impact: [downstream state, SLA node, or adjacent process affected]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-01. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]
- Exception Refs: [list EX block identifiers whose `Bottleneck Ref:` cites B-01. Format:
  "EX-1A (Phase 1 — [Exception Name]), EX-2B (Phase 2 — [Exception Name])". NONE if no EX
  block cites B-01 (dark bottleneck — gate violation). Each listed ID must string-match an
  EX block where `Bottleneck Ref:` contains "B-01". A listed ID with no matching EX block
  entry fails the CHAIN STATUS B-NN→Exception consistency check.]

---

**B-02 — [Bottleneck Name]**

- Cause: [Required: IM-ID literal string AND R-ID literal string. Example: "IM-02 (email
  approval routing without SLA timestamp) combined with R-03 (Finance Controller) same-day
  unavailability — invoice matching queue at S-07. Dual-cite: 'IM-02' satisfies Condition A;
  'R-03' satisfies Condition B."]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string → fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string → fails C-39
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-02. Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]
- Exception Refs: [list EX block identifiers whose `Bottleneck Ref:` cites B-02, or NONE
  (dark bottleneck — gate violation). Each listed ID must string-match an EX block with
  `Bottleneck Ref: B-02`.]

---

**Gap Identification**

> MISSING: [step name] — [rationale: why it belongs; failure mode enabled; which phase;
> which IM-ID it would reduce if present]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [every AT-RISK SLA row cites a B-ID; enumerate pairs or name gap]
- Backward (B→SLA): [every B-NN Evidence field lists AT-RISK SLA rows citing it; enumerate or name gap]
- Exit gate consistency: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID string-matches a declared B-NN block; name any mismatch]
- Phase-boundary B-NN continuity: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID string-matches the next phase's PHASE ENTRY CONTRACT `Prior phase blocked bottleneck:`; list phase pairs or name break]
- Phase-sequence: [every PHASE ENTRY CONTRACT `Prior phase:` identifier string-matches the label of the preceding phase block; PHASE 1 carries NONE/INIT sentinel; list pairs or name any mismatch or missing sentinel]
- Phase-exit-sequence: [every PHASE EXIT GATE `Next phase:` identifier string-matches the label of the subsequent phase block in document order; last phase carries NONE/END sentinel; list exit gate→next phase pairs or name any mismatch, non-last phase with sentinel, or last phase without sentinel]
- Exception→B: [every EX block `Bottleneck Ref:` B-ID (where non-NONE) matches a declared B-NN; list EX→B-NN pairs or name unresolved block]
- B-NN→Exception: [every declared B-ID has at least one entry in its `Exception Refs:` field (no NONE values); each listed EX block ID string-matches an EX block with `Bottleneck Ref:` citing this B-ID; enumerate B-ID→EX block pairs from Exception Refs; name any B-ID with NONE in Exception Refs (dark bottleneck — gate violation) or any Exception Refs entry whose referenced EX block does not have a matching Bottleneck Ref]
- Exception→Role: [every EX block `Role Ref:` R-ID matches the ROLE SEQUENCE SCHEDULE primary owner for the enclosing phase; list EX→R-ID pairs or name mismatch]
- Role→Exception: [every declared R-ID in the Role Registry Gate appears in at least one EX block's `Role Ref:` sub-field; list R-ID→EX block pairs; name any R-ID with no EX trace (dark role)]
- Dual-cite status: [every B-NN Cause field contains both IM-ID and R-ID string; name any block missing either]
- Gap (if OPEN): [name the unresolved direction and the unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal name] | SUCCESS | [branch or state that reaches it] |
| [failure terminal name] | FAILURE | [branch or state that reaches it] |
| [cancel terminal name] | CANCEL | [branch or state that reaches it] |

> Completeness check: Every exit branch in every SECTION B state table must reach one of the
> declared terminals above. No branch may end at a non-terminal state without an explicit
> `continues-via: S-[ID]` pointer.
