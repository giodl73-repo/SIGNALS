# flow-lifecycle — Round 12 Variations (Rubric v12)

**Rubric**: v12 · 41 criteria (33 aspirational) · Ceiling entering R12: 33/33
(R11 V-04 cracked C-40 minimum; R11 V-05 confirmed C-40 + cracked C-41 minimum)

**Open criteria entering R12**: None — C-40 and C-41 both signaled. All five R12 variations carry
the full architecture needed to pass C-01 through C-39. Variation axes probe C-40 + C-41 at
structural precision and bidirectional closure.

**Evidence from R11 excellence (C-40, C-41):**

- **C-40 signal (Exception→Role)**: R11 V-04 established `Bottleneck Ref: B-NN` in EX blocks as
  the Exception→Artifact cross-reference pattern. C-40 specializes this to Exception→Role: each
  EX block carries `Role Ref: R-ID` naming the ROLE SEQUENCE SCHEDULE owner for the enclosing
  phase. Additionally, the registry gate gains a bidirectional closure check: each declared R-ID
  must appear in at least one EX block's Role Ref field, making "dark" roles detectable.
- **C-41 signal (Phase→Phase sequential linkage)**: R11 V-05 established `Prior phase blocked
  bottleneck: B-ID` in PHASE ENTRY CONTRACT for B-NN inheritance across phase boundaries. C-41
  is orthogonal: a `Prior phase:` sub-field naming the predecessor phase by its literal identifier
  (e.g., "PHASE 1 — Initiation"). PHASE 1 carries NONE/INIT sentinel. Together with C-37's exit
  gate B-ID forward reference, C-41 completes gate-to-gate phase linkage: entry declares which
  phase this follows (backward); exit declares which bottleneck may block the exit (forward).

**Distinction from R11 probes:**

| R11 field | C-40/C-41 target | What R12 adds |
|-----------|-----------------|---------------|
| `Bottleneck Ref: B-NN` in EX block | Precursor — Exception→B-NN direction | `Role Ref: R-ID` in EX block — Exception→Role direction |
| `Prior phase blocked bottleneck: B-ID` in ENTRY CONTRACT | Precursor — B-NN boundary continuity | `Prior phase: PHASE N` in ENTRY CONTRACT — Phase→Phase sequence declaration |

Both new fields are **distinct sub-fields** alongside the existing R11 fields — not replacements.

**Variation axes chosen:**

- **Axis D — EX-Block Role-Ref (single direction)**: Each EX block gains `Role Ref: R-ID` citing
  the ROLE SEQUENCE SCHEDULE owner for the enclosing phase. One new sub-field only; no registry
  gate change. Probes whether Exception→Role direction alone is sufficient to surface C-40.
- **Axis E — Registry Gate Bidirectional Closure**: The Role Registry Gate anti-generic
  validation gains a fourth check: each declared R-ID must appear in at least one EX block's
  `Role Ref:` sub-field. CHAIN STATUS gains a `Role→Exception` direction. Probes whether
  bidirectional closure (Role→Exception in gate; Exception→Role in block) adds independent
  discriminating power over single-direction alone.
- **Axis F — Prior-Phase Sequential Sub-Field**: Each PHASE ENTRY CONTRACT gains `Prior phase:
  PHASE N` as a named sub-field distinct from `Prior phase blocked bottleneck:`. PHASE 1 carries
  NONE/INIT. CHAIN STATUS gains a `Phase-sequence` direction. Probes C-41 in isolation.

| Variation | Axis | Hypothesis |
|-----------|------|-----------|
| V-01 | D only: EX-block Role-Ref (single direction) | Adding `Role Ref: R-ID` to every EX block creates the Exception→Role traceability direction: EX-2A cites R-02; R-02 owns Phase 2 in the ROLE SEQUENCE SCHEDULE — verifiable by string comparison. If the single-direction sub-field is sufficient for C-40, V-01 is the minimal architecture |
| V-02 | D + E: Role-Ref + Registry Gate bidirectional closure | The bidirectional requirement — each declared R-ID must appear in at least one EX block — gates the Role Registry on observable exception-phase activity. "Dark" roles become structural violations rather than silent omissions. If C-40 requires both the EX→Role sub-field AND the Role→Exception gate check, V-02 is the minimum |
| V-03 | F only: Prior-Phase sequential sub-field | A `Prior phase: PHASE N` field in PHASE ENTRY CONTRACT declares phase sequence as a named structural property, making out-of-order rendering detectable as an identifier mismatch. Probes C-41 in isolation without the Exception→Role change, verifying whether phase-sequence linkage surfaces independently |
| V-04 | D + F: Role-Ref + Prior-Phase | The two new single-direction criteria compose without shared state: Role Ref in EX blocks does not interact with Prior phase in entry contracts. If C-40 and C-41 are independent, V-04 is the minimum for both to pass simultaneously — tests whether single-direction D plus single-direction F is architecturally coherent |
| V-05 | D + E + F: Full bidirectional Role-Ref + Prior-Phase | Maximum traceability density for the two new criteria: bidirectional Role-Ref (EX→Role in block + Role→Exception in gate) plus Prior-Phase phase sequence declaration. CHAIN STATUS verifies both new directions. If C-40 requires bidirectional closure and C-41 is independent, V-05 is the only configuration where both criteria can simultaneously pass at their strongest form |

---

## V-01 — Axis D: EX-Block Role-Ref (Single Direction)

**Variation axis**: Role sequence — each EX block names the owning R-ID from the ROLE SEQUENCE
SCHEDULE, establishing the Exception→Role traceability direction as a single sub-field addition.
The registry gate is not updated; no gate check verifies that every declared R-ID appears in at
least one EX block. The chain runs one way: exception trace → role owner.

**Hypothesis**: C-40 requires each EX block to carry a named R-ID sub-field matching the ROLE
SEQUENCE SCHEDULE entry for the enclosing phase. If the single-direction chain (Exception→Role)
is sufficient — the EX block declares the owning role, and a reviewer can navigate from the EX
block to the schedule entry by string comparison — then V-01 is the minimum architecture. The
bidirectional closure (registry gate validating Role→Exception) may be an escalation criterion
rather than a baseline requirement. V-01 isolates the EX-block sub-field change from the gate
change, allowing the round to determine whether single-direction presence satisfies C-40.

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
| IM-01 | [specific recurring failure in the manual process] | [daily / per-cycle / per-exception] | [what breaks downstream when this occurs] |
| IM-02 | [second distinct failure mode] | [frequency] | [downstream effect] |

**Cost of no action**: [Named measure with current-state value or rate, declared before PHASE 1.
Example: "Average rejection cycle time: 3.2 days per rejected invoice" or
"Credit approval rework rate: 18% per period." Both IM-IDs above must be reachable from at least
one B-NN Cause field in Bottleneck Analysis below.]

---

### Role Registry Gate

> GATE BLOCK: Complete before the Role Sequence Schedule and before tracing any state.
> Do not begin any phase until all R-ID entries are filled and all three anti-generic checks pass.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [domain-specific role] | [named responsibility] |
| R-02 | [domain-specific role] | [named responsibility] |
| R-03 | [domain-specific role] | [named responsibility] |

Anti-generic validation (all three must clear before proceeding):
- [ ] No R-ID entry uses "Approver" without a domain qualifier
- [ ] No R-ID entry uses "Owner" without a named responsibility
- [ ] Each R-ID is referenced by at least one Decision Supplement block, the Role Sequence
      Schedule, and at least one PHASE EXIT GATE Exit verification or Blocked bottleneck field

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
> `Role Ref:` sub-fields must appear in this schedule as the phase owner for the enclosing phase.

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

- Entry Condition: [specific named artifact or state record from prior phase's Required outputs field]
- Pre-condition check: R-[ID] ([role name — must match Role Sequence Schedule primary owner for this phase]) — [how they verify the entry condition is met]
- Blocking condition: [if entry condition is not met: which state is entered, which role is notified, what re-entry path applies]

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition that causes deviation — name the state, threshold breach, or missing input]
> - Trace: [path of states traversed from trigger to resolution or terminal; cite S-IDs in sequence]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason this failure mode matters for this process type]
> - Bottleneck Ref: [B-NN that enabled this exception, or NONE. B-ID must string-match a
>   Bottleneck Analysis identifier. Example: "B-01 — manual reconciliation backlog created the
>   missing-approval condition that triggered this exception." NONE if no declared bottleneck
>   was causal for this specific trigger.]
> - Role Ref: [R-ID of the ROLE SEQUENCE SCHEDULE primary owner for this phase. Must be a
>   literal R-ID matching the schedule entry for the phase containing this exception trace.
>   Example: "R-02 — GL Manager owns this phase per Role Sequence Schedule; exception
>   escalation routes through their approval queue." A free-text role name without an R-ID
>   identifier fails. An R-ID absent from the ROLE SEQUENCE SCHEDULE fails. An R-ID whose
>   schedule phase-ownership mapping does not include this exception's enclosing phase fails.]

Minimum 1 exception trace per phase. Minimum 3 exception traces total across all phases.
For each EX block with a non-NONE Bottleneck Ref: B-ID must string-match a declared B-NN block.
For every Role Ref: R-ID must string-match the Primary Owner entry in the ROLE SEQUENCE SCHEDULE
for the enclosing phase.

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
> must string-match the identifier declared in Bottleneck Analysis below — assign the B-ID now
> and use the same string in that section. This is a forward reference.

- Exit Condition: [what the phase must have produced to be considered complete]
- Required outputs: [named artifacts, decisions, or state records that must exist]
- Exit verification: R-[ID] ([role name — must match Role Sequence Schedule primary owner]) confirms all required outputs are present
- Blocking condition: [if required outputs are absent: re-entry path or escalation]
- Blocked bottleneck: [B-NN that can delay this phase's exit, or NONE. Example: "B-01 — manual spreadsheet reconciliation by R-02 blocks invoice approval exit until GL entries are verified."]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

Identify at least one fork/join with labeled join condition:

- **FORK at**: S-[ID] ([state name])
- **Branch 1**: [path — states traversed in sequence; cite S-IDs]
- **Branch 2**: [path — states traversed in sequence; cite S-IDs]
- **JOIN at**: S-[ID] ([join state name])
- **Join Condition**: AND-join (both branches must complete) / OR-join (first branch sufficient) — specify which applies and explain why this process requires that join type

---

### Edge Case Enumeration

Identify at least three edge cases distinct from SECTION A exception flows:

> **EC-[N] — [Edge Case Name]**
> - Triggering Condition: [specific scenario that produces this edge case]
> - Why Problematic: [specific reason this falls outside documented handling]
> - Correct Response: R-[ID] ([role name]) — [specific correct action; name the target state or resolution path]

---

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF — {Topic} lifecycle → [adjacent process name]**
> - Sending State: S-[ID] ([state name])
> - Receiving Process: [adjacent process name]
> - Data Payload: [named fields or record types transferred]
> - Expected Acknowledgment: [signal or confirmation message from receiving process]
> - Failure Mode: [what happens if acknowledgment is not received within SLA]
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
> Each condition is verifiable by a single string-presence check against the Cause field text.
>
> **Dual-Cite Fail Condition A** — Cause field contains no IM-ID literal string (e.g., "IM-01"):
> fails C-39. Verify: search the Cause field text for "IM-" followed by digits. Absence → fail.
>
> **Dual-Cite Fail Condition B** — Cause field contains no R-ID literal string (e.g., "R-02"):
> fails C-39. Verify: search the Cause field text for "R-" followed by digits. Absence → fail.
>
> A Cause field that cites IM-01 but not an R-ID satisfies Condition A but fails Condition B.
> Both conditions must pass independently.
>
> B-IDs assigned here must string-match: (1) PHASE EXIT GATE `Blocked bottleneck:` fields, and
> (2) EX block `Bottleneck Ref:` fields where non-NONE.
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
> (2) Labeled axes (`` `Required format:` `` / `` `Fail condition:` ``) must appear in BOTH
> this preamble AND each B-NN per-block Evidence hint.
>
> Anti-embedding: Do not embed CHAIN STATUS inside the SLA ANALYSIS section.
> Declare CHAIN STATUS in its own dedicated top-level section after SLA ANALYSIS.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field.**

---

**B-01 — [Bottleneck Name]**

- Cause: [specific cause. Required: cite IM-ID literal string (Fail Condition A) AND R-ID literal
  string (Fail Condition B). Example: "IM-01 (manual spreadsheet GL reconciliation) combined with
  R-02 (GL Manager) unavailable during period-close peak — causes queue accumulation at S-05.
  Dual-cite check: 'IM-01' satisfies Condition A; 'R-02' satisfies Condition B."]
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

- Cause: [specific cause — cite IM-ID literal string (Condition A) AND R-ID literal string
  (Condition B). Example: "IM-02 (email-based approval routing without timestamp) combined with
  R-03 (Finance Controller) not available for same-day review — delays invoice matching at S-07.
  Dual-cite: 'IM-02' satisfies A; 'R-03' satisfies B."]
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

> MISSING: [step name] — [rationale: why it belongs in this process model; what failure mode its
> absence enables; which phase it belongs in; which IM-ID it would reduce if present]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [every AT-RISK SLA row cites a B-ID; enumerate pairs or name the unlinked row]
- Backward (B→SLA): [every B-NN names affected SLA nodes; enumerate or name the gap]
- Exit gate consistency: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID string-matches a declared B-NN block; name any mismatch]
- Exception→B: [every EX block `Bottleneck Ref:` B-ID (where non-NONE) matches a declared B-NN; list EX→B-NN pairs or name the unresolved EX block]
- Exception→Role: [every EX block `Role Ref:` R-ID matches the ROLE SEQUENCE SCHEDULE primary owner for the enclosing phase; list EX→R-ID pairs or name any mismatch]
- Dual-cite status: [every B-NN Cause field contains both an IM-ID string and an R-ID string; name any block where either is absent]
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

## V-02 — Axes D + E: Role-Ref + Registry Gate Bidirectional Closure

**Variation axes**: Output format — the Role Registry Gate anti-generic validation gains a fourth
structural check: each declared R-ID must appear in at least one EX block's `Role Ref:` sub-field.
This closes the chain bidirectionally: EX block → Role (Exception→Role in the block, per Axis D)
and Role → EX block (Role→Exception in the gate, Axis E). CHAIN STATUS gains a `Role→Exception`
direction. "Dark" roles — registry-declared but with no observable EX trace — become gate
violations detectable by name.

**Hypothesis**: C-40 requires both directions: (a) the EX block carries `Role Ref: R-ID` making
the Exception→Role linkage explicit, AND (b) the registry gate validates that every declared R-ID
appears in at least one EX block. If the bidirectional closure is the discriminating property —
a registry-declared role with no EX trace is a structural gap, not merely a missing annotation —
then V-01's single-direction chain is insufficient and V-02 is the minimum for C-40. The gate
check converts an implicit expectation (every declared role should be observable in exceptions)
into a named structural violation. If both (a) and (b) are required, V-02 surfaces C-40 and
V-01 does not.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must satisfy both Dual-Cite
> Fail Conditions. Quantified metric must appear before PHASE 1.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: tools, handoff mechanisms, storage, initiator]

**Incumbent failure modes**:

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure] | [frequency] | [downstream effect] |
| IM-02 | [second distinct failure mode] | [frequency] | [downstream effect] |

**Cost of no action**: [Named measure with current-state value or rate, declared before PHASE 1.
Example: "Purchase order cycle time: 8.1 days against 5-day target" or
"Manual matching error rate: 12% per period, generating 40+ exception tickets."]

---

### Role Registry Gate

> GATE BLOCK: Complete before Role Sequence Schedule and before tracing any state.
> All four anti-generic checks must clear before proceeding to the Role Sequence Schedule.

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
- [ ] Each declared R-ID appears in at least one EX block's `Role Ref:` sub-field — R-IDs with
      no observable EX block trace are "dark" roles and constitute a gate violation; identify any
      dark R-IDs before proceeding to phase content generation

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Role Sequence Schedule

> Declared after Role Registry Gate and before PHASE 1. Maps each R-ID to active phases,
> activation trigger, handoff trigger, and parallel windows. B-NN Cause fields must cite
> the blocking R-ID from this schedule (Dual-Cite Fail Condition B). R-IDs cited in EX block
> `Role Ref:` sub-fields must match the schedule entry for the enclosing phase. Every R-ID
> declared in the registry must appear in at least one EX block Role Ref — the gate check
> above is the structural enforcement of this property.

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior-process artifact — not "Start"] | [specific completion condition] | R-[ID] or NONE | [concurrent window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1] | [completion condition] | R-[ID] or NONE | [concurrent window or NONE] |

Rules:
- Every phase must have a Primary Owner. Triggers must be specific.
- Every R-ID here must match an entry in the Role Registry Gate.
- Parallel windows must state start/end states (S-IDs) when known.

---

### Phase Structure

For each phase, produce the following five blocks in document order:

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Entry Condition must reference the prior phase's PHASE EXIT GATE "Required outputs" by name.

- Entry Condition: [specific named artifact or state record from prior phase's Required outputs]
- Pre-condition check: R-[ID] ([role name — must match Role Sequence Schedule primary owner for this phase]) — [verification method]
- Blocking condition: [state entered and role notified if entry condition not met]

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition — name the state, threshold breach, or missing input]
> - Trace: [path of states traversed from trigger to resolution or terminal; cite S-IDs]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason]
> - Bottleneck Ref: [B-NN that enabled this exception, or NONE. B-ID must string-match a
>   Bottleneck Analysis identifier. NONE if no declared bottleneck was causal.]
> - Role Ref: [R-ID of the ROLE SEQUENCE SCHEDULE primary owner for this phase. Must be a
>   literal R-ID matching the schedule entry for the enclosing phase. This sub-field is
>   the Exception→Role traceability artifact — the Role Registry Gate fourth check will
>   verify that this R-ID appears here before the gate passes. Example: "R-02 — GL Manager
>   is Phase 2 primary owner per Role Sequence Schedule; this exception escalates through
>   their review queue." Fails if: free-text role name without R-ID; R-ID absent from schedule;
>   R-ID whose schedule phase mapping does not include this phase.]

Minimum 1 per phase; 3 total minimum. Every declared R-ID must appear in at least one EX block's
Role Ref sub-field — the Role Registry Gate fourth check is validated against this population.
CHAIN STATUS Role→Exception direction will enumerate R-ID → EX block pairs.

**SECTION B — STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules: Named Entry Condition required; Exits → S-ID or TERMINAL; standard Type values.

**Decision Supplement Blocks** (one per DECISION-type state):

> **DS-[S-ID] — [State Name]**
> - Condition: [rule or threshold]
> - Owner: R-[ID] ([role name from Role Registry])
> - Branch A ([outcome]): → S-[ID]
> - Branch B ([outcome]): → S-[ID] or TERMINAL
> - Fallback: [action if condition cannot be evaluated]

**PHASE EXIT GATE**

> `Blocked bottleneck:` names the B-ID that can delay this exit, or NONE. B-ID must
> string-match the Bottleneck Analysis identifier below.

- Exit Condition: [what the phase must produce to be complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name — must match Role Sequence Schedule primary owner]) confirms all required outputs are present
- Blocking condition: [re-entry path or escalation if outputs absent]
- Blocked bottleneck: [B-NN or NONE. Example: "B-01 — manual spreadsheet reconciliation by R-02 blocks approval exit."]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID] ([state name])
- **Branch 1**: [states traversed; cite S-IDs]
- **Branch 2**: [states traversed; cite S-IDs]
- **JOIN at**: S-[ID] ([join state name])
- **Join Condition**: AND-join / OR-join — specify which and explain why

---

### Edge Case Enumeration

At least three, distinct from SECTION A exception flows:

> **EC-[N] — [Edge Case Name]**
> - Triggering Condition: [specific scenario]
> - Why Problematic: [specific reason outside documented handling]
> - Correct Response: R-[ID] ([role name]) — [specific correct action]

---

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF — {Topic} lifecycle → [adjacent process name]**
> - Sending State: S-[ID]; Receiving Process: [name]; Data Payload: [fields]
> - Expected Acknowledgment: [signal]; Failure Mode: [if no acknowledgment]; Owner: R-[ID]

---

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|
| | | | | AT-RISK / ON-TRACK | B-NN (if AT-RISK) |

Minimum 3 rows; at least 1 AT-RISK citing a B-NN.

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN Cause field must satisfy both of the following conditions independently.
>
> **Dual-Cite Fail Condition A** — Cause field contains no IM-ID literal string (e.g., "IM-01"):
> fails C-39. Test: search Cause text for "IM-" followed by digits. Absence → fail.
>
> **Dual-Cite Fail Condition B** — Cause field contains no R-ID literal string (e.g., "R-02"):
> fails C-39. Test: search Cause text for "R-" followed by digits. Absence → fail.
>
> Partial citation (one present, one absent) satisfies one condition and fails the other.
> B-IDs here must string-match: (1) PHASE EXIT GATE `Blocked bottleneck:` fields, and
> (2) EX block `Bottleneck Ref:` fields where non-NONE.
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
> (2) Labeled axes (`` `Required format:` `` / `` `Fail condition:` ``) must appear in BOTH
> this preamble AND each B-NN per-block Evidence hint.
>
> Anti-embedding: Do not embed CHAIN STATUS inside the SLA ANALYSIS section.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field.**

---

**B-01 — [Bottleneck Name]**

- Cause: [Required: IM-ID literal string (Condition A) AND R-ID literal string (Condition B).
  Example: "IM-01 (manual spreadsheet GL reconciliation) combined with R-02 (GL Manager) peak
  unavailability — queue accumulation at S-05. Dual-cite: 'IM-01' satisfies A; 'R-02' satisfies B."]
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

- Cause: [Required: IM-ID literal string AND R-ID literal string.
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

> MISSING: [step name] — [why it belongs; failure mode enabled; which phase; which IM-ID reduced]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [every AT-RISK SLA row cites a B-ID; enumerate pairs or name gap]
- Backward (B→SLA): [every B-NN names affected SLA nodes; enumerate or name gap]
- Exit gate consistency: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID matches a declared B-NN; name any mismatch]
- Exception→B: [every EX block `Bottleneck Ref:` B-ID (where non-NONE) matches a declared B-NN; list EX→B-NN pairs or name unresolved EX block]
- Exception→Role: [every EX block `Role Ref:` R-ID matches ROLE SEQUENCE SCHEDULE primary owner for the enclosing phase; list EX→R-ID pairs or name mismatch]
- Role→Exception: [every declared R-ID in the Role Registry Gate appears in at least one EX block's `Role Ref:` sub-field; list R-ID→EX block pairs; name any R-ID with no EX trace (dark role)]
- Dual-cite status: [every B-NN Cause field contains both IM-ID and R-ID string; name any block missing either]
- Gap (if OPEN): [name the unresolved direction and the unlinked entry]

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

## V-03 — Axis F: Prior-Phase Sequential Sub-Field

**Variation axis**: Lifecycle emphasis — each PHASE ENTRY CONTRACT gains a named `Prior phase:`
sub-field carrying the literal identifier of the preceding phase (e.g., "PHASE 1 — Initiation").
PHASE 1 carries an explicit sentinel (NONE or INIT). This is structurally distinct from the
`Prior phase blocked bottleneck:` field established in R11: that field carries a B-ID; this
field carries a Phase identifier. Both sub-fields coexist in the PHASE ENTRY CONTRACT block.
CHAIN STATUS gains a `Phase-sequence` direction verifying that every entry contract's `Prior
phase:` identifier string-matches the preceding phase's block label in document order.

**Hypothesis**: C-41 requires the entry contract's Phase→Phase sequential linkage as a named
structural property. When PHASE 2's entry contract declares `Prior phase: PHASE 1 — Initiation`,
a reviewer can verify phase sequence by comparing the string in the entry contract to the label
of the preceding phase block in document order, without inferred reading order. C-41 is
orthogonal to C-37 (which provides the Phase→B-NN forward reference): C-37 fills the exit gate's
B-ID slot; C-41 fills the entry contract's phase-sequencing slot. V-03 isolates the Prior-Phase
sub-field from the Role-Ref change, verifying that phase-sequence traceability surfaces as an
independent criterion without the Exception→Role addition.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must satisfy both Dual-Cite
> Fail Conditions. Quantified metric must appear before PHASE 1.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: tools, handoff mechanisms, storage, initiator]

**Incumbent failure modes**:

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure] | [frequency] | [downstream effect] |
| IM-02 | [second distinct failure mode] | [frequency] | [downstream effect] |

**Cost of no action**: [Named quantified measure declared before PHASE 1. Example: "Support case
mean-time-to-resolve: 11.4 days vs 7-day SLA target" or "Duplicate payment rate: 4.7% per period."]

---

### Role Registry Gate

> GATE BLOCK: Complete before Role Sequence Schedule and before tracing any state.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [domain-specific role] | [named responsibility] |
| R-02 | [domain-specific role] | [named responsibility] |
| R-03 | [domain-specific role] | [named responsibility] |

Anti-generic validation (all three must clear before proceeding):
- [ ] No R-ID entry uses "Approver" without a domain qualifier
- [ ] No R-ID entry uses "Owner" without a named responsibility
- [ ] Each R-ID is referenced by at least one Decision Supplement block, the Role Sequence
      Schedule, and at least one PHASE EXIT GATE Exit verification or Blocked bottleneck field

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Role Sequence Schedule

> Declared after Role Registry Gate and before PHASE 1. Maps each R-ID to active phases,
> activation trigger, handoff trigger, and parallel windows. B-NN Cause fields must cite
> the blocking R-ID from this schedule (Dual-Cite Fail Condition B).

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior-process artifact] | [specific completion condition] | R-[ID] or NONE | [concurrent window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1] | [completion condition] | R-[ID] or NONE | [concurrent window or NONE] |

Rules:
- Every phase must have a Primary Owner. Triggers must be specific.
- Every R-ID here must match an entry in the Role Registry Gate.
- Parallel windows must state start/end states (S-IDs) when known.

---

### Phase Structure

For each phase, produce the following five blocks in document order:

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Entry Condition must reference the prior phase's PHASE EXIT GATE "Required outputs" by name.
> `Prior phase:` must carry the literal identifier of the preceding phase block (e.g., "PHASE 1
> — Initiation"). Phase 1 carries sentinel value NONE or INIT — not a phase identifier and not
> blank. The identifier must string-match the label of the preceding phase block in document
> order: if that block is labeled "PHASE 1 — Initiation", the Prior phase: field in Phase 2's
> entry contract must cite "PHASE 1 — Initiation" or "PHASE 1" as a recognizable string match.
> `Prior phase blocked bottleneck:` is a SEPARATE sub-field carrying the B-ID from the prior
> exit gate — do not conflate the two fields.

- Entry Condition: [specific named artifact from prior phase's Required outputs field]
- Pre-condition check: R-[ID] ([role name — must match Role Sequence Schedule primary owner]) — [verification method]
- Blocking condition: [state entered and role notified if entry condition not met]
- Prior phase: [Literal identifier of the preceding phase block, e.g., "PHASE 1 — Initiation".
  Phase 1 carries NONE or INIT as sentinel. A non-first phase carrying sentinel fails.
  A first phase carrying a phase identifier instead of sentinel fails.]
- Prior phase blocked bottleneck: [B-ID from prior phase PHASE EXIT GATE `Blocked bottleneck:`
  or NONE if that field was NONE, or N/A for Phase 1. Must string-match the prior exit gate
  field AND the B-NN block identifier. Example: "B-01 (inherited from Phase 1 exit gate —
  spreadsheet reconciliation delay still active at phase boundary)."]

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition — name the state, threshold breach, or missing input]
> - Trace: [path of states traversed from trigger to resolution or terminal; cite S-IDs]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason]
> - Bottleneck Ref: [B-NN that enabled this exception, or NONE. B-ID must string-match a
>   Bottleneck Analysis identifier. NONE if no declared bottleneck was causal.]

Minimum 1 per phase; 3 total minimum.

**SECTION B — STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules: Named Entry Condition required; Exits → S-ID or TERMINAL; standard Type values.

**Decision Supplement Blocks** (one per DECISION-type state):

> **DS-[S-ID] — [State Name]**
> - Condition: [rule or threshold]
> - Owner: R-[ID] ([role name from Role Registry])
> - Branch A ([outcome]): → S-[ID]
> - Branch B ([outcome]): → S-[ID] or TERMINAL
> - Fallback: [action if undecidable]

**PHASE EXIT GATE**

> `Blocked bottleneck:` names the B-ID that can delay this exit, or NONE. B-ID must
> string-match: (1) Bottleneck Analysis identifier, and (2) the next phase's PHASE ENTRY
> CONTRACT `Prior phase blocked bottleneck:` field. The `Prior phase:` field in the next
> phase's entry contract is a SEPARATE traceability direction — it carries the phase label,
> not the B-ID.

- Exit Condition: [what the phase must produce to be complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name — must match Role Sequence Schedule primary owner]) confirms all outputs present
- Blocking condition: [re-entry path or escalation if outputs absent]
- Blocked bottleneck: [B-NN or NONE. B-ID declared here must appear in Bottleneck Analysis
  AND be mirrored in the next phase's PHASE ENTRY CONTRACT `Prior phase blocked bottleneck:`
  field. Example: "B-01 — manual spreadsheet reconciliation delay blocks GL approval exit;
  inherited by Phase 2 entry contract as prior-phase blocker."]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID] ([state name])
- **Branch 1**: [states traversed; cite S-IDs]
- **Branch 2**: [states traversed; cite S-IDs]
- **JOIN at**: S-[ID] ([join state name])
- **Join Condition**: AND-join / OR-join — specify and explain

---

### Edge Case Enumeration

Three or more, distinct from SECTION A:

> **EC-[N] — [Edge Case Name]**
> - Triggering Condition: [specific scenario]
> - Why Problematic: [specific consequence]
> - Correct Response: R-[ID] ([role name]) — [specific action]

---

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF — {Topic} lifecycle → [adjacent process name]**
> - Sending State: S-[ID]; Receiving Process: [name]; Data Payload: [fields]
> - Expected Acknowledgment: [signal]; Failure Mode: [if no acknowledgment]; Owner: R-[ID]

---

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|
| | | | | AT-RISK / ON-TRACK | B-NN (if AT-RISK) |

Minimum 3 rows; at least 1 AT-RISK citing a B-NN.

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN Cause field must satisfy both of the following conditions independently.
>
> **Dual-Cite Fail Condition A** — Cause field contains no IM-ID literal string (e.g., "IM-01"):
> fails C-39. Test: search Cause text for "IM-" followed by digits. Absence → fail.
>
> **Dual-Cite Fail Condition B** — Cause field contains no R-ID literal string (e.g., "R-02"):
> fails C-39. Test: search Cause text for "R-" followed by digits. Absence → fail.
>
> B-IDs here must string-match: (1) PHASE EXIT GATE `Blocked bottleneck:` fields, (2) PHASE
> ENTRY CONTRACT `Prior phase blocked bottleneck:` fields in the following phase, and (3)
> EX block `Bottleneck Ref:` fields where non-NONE.
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
> (2) Labeled axes must appear in BOTH this preamble AND each B-NN per-block Evidence hint.
>
> Anti-embedding: Do not embed CHAIN STATUS inside the SLA ANALYSIS section.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field.**

---

**B-01 — [Bottleneck Name]**

- Cause: [Required: IM-ID literal string (Condition A) AND R-ID literal string (Condition B).
  Example: "IM-01 (manual spreadsheet reconciliation) combined with R-02 (GL Manager) peak
  unavailability — queue accumulation at S-05. This B-ID appears in Phase 1 exit gate
  `Blocked bottleneck:` and Phase 2 entry contract `Prior phase blocked bottleneck:`."]
  - Dual-Cite Fail Condition A: no IM-ID string in Cause → fails C-39
  - Dual-Cite Fail Condition B: no R-ID string in Cause → fails C-39
- Impact: [downstream state, SLA node, or adjacent process]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List AT-RISK SLA rows citing B-01. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]

---

**B-02 — [Bottleneck Name]**

- Cause: [Required: IM-ID literal string AND R-ID literal string.]
  - Dual-Cite Fail Condition A: no IM-ID string in Cause → fails C-39
  - Dual-Cite Fail Condition B: no R-ID string in Cause → fails C-39
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List AT-RISK SLA rows citing B-02. Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]

---

**Gap Identification**

> MISSING: [step name] — [why it belongs; failure mode enabled; which phase; which IM-ID reduced]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [every AT-RISK SLA row cites a B-ID; enumerate pairs or name gap]
- Backward (B→SLA): [every B-NN names affected SLA nodes; enumerate or name gap]
- Exit gate consistency: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID matches a declared B-NN; name any mismatch]
- Phase-boundary B-NN continuity: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID string-matches the next phase's PHASE ENTRY CONTRACT `Prior phase blocked bottleneck:`; list phase pairs or name break]
- Phase-sequence: [every PHASE ENTRY CONTRACT `Prior phase:` identifier string-matches the label of the preceding phase block in document order; PHASE 1 carries NONE/INIT sentinel; list phase pairs or name any mismatch or missing sentinel]
- Exception→B: [every EX block `Bottleneck Ref:` B-ID (where non-NONE) matches a declared B-NN; list pairs or name unresolved block]
- Dual-cite status: [every B-NN Cause field contains both IM-ID and R-ID string; name any block missing either]
- Gap (if OPEN): [name the unresolved direction and the unlinked entry]

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

## V-04 — Axes D + F: Role-Ref + Prior-Phase Sequential Linkage

**Variation axes**: Role sequence + lifecycle emphasis — two orthogonal new sub-fields added
simultaneously: `Role Ref: R-ID` in EX blocks (Exception→Role direction, Axis D) and
`Prior phase: PHASE N` in PHASE ENTRY CONTRACTs (Phase→Phase sequential linkage, Axis F).
No registry gate bidirectional closure (Axis E is absent). Tests whether the two new
single-direction criteria compose cleanly without creating structural ambiguity or requiring
cross-field coordination.

**Hypothesis**: C-40 and C-41 probe independent traceability directions with no shared state:
Role Ref in EX blocks operates on the exception-to-role axis; Prior phase in entry contracts
operates on the phase-sequence axis. When both are active simultaneously, each should remain
independently evaluable. If both sub-fields can be populated without conflicting with each other
or with the existing R11 fields (`Bottleneck Ref:`, `Prior phase blocked bottleneck:`), V-04
demonstrates architectural composability and may be the minimum for both criteria to be
simultaneously detectable. Absence of the bidirectional gate (Axis E) means C-40's bidirectional
requirement, if it exists, would prevent C-40 from passing here while C-41 passes — allowing
the round to detect whether C-40 requires bidirectional closure or not.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must satisfy both Dual-Cite
> Fail Conditions. Quantified metric must appear before PHASE 1.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: tools, handoff mechanisms, storage, initiator]

**Incumbent failure modes**:

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure] | [frequency] | [downstream effect] |
| IM-02 | [second distinct failure mode] | [frequency] | [downstream effect] |

**Cost of no action**: [Named quantified measure declared before PHASE 1. Both IM-IDs must be
reachable from at least one B-NN Cause field. Example: "Average credit approval cycle time: 5.8
days vs 3-day SLA" or "Goods receipt discrepancy rate: 8.4% per period."]

---

### Role Registry Gate

> GATE BLOCK: Complete before Role Sequence Schedule and before tracing any state.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [domain-specific role] | [named responsibility] |
| R-02 | [domain-specific role] | [named responsibility] |
| R-03 | [domain-specific role] | [named responsibility] |

Anti-generic validation (all three must clear before proceeding):
- [ ] No R-ID entry uses "Approver" without a domain qualifier
- [ ] No R-ID entry uses "Owner" without a named responsibility
- [ ] Each R-ID is referenced by at least one Decision Supplement block, the Role Sequence
      Schedule, and at least one PHASE EXIT GATE Exit verification or Blocked bottleneck field

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Role Sequence Schedule

> Declared after Role Registry Gate and before PHASE 1. Maps each R-ID to active phases,
> activation trigger, handoff trigger, and parallel windows. B-NN Cause fields must cite
> the blocking R-ID from this schedule (Dual-Cite Fail Condition B). R-IDs cited in EX block
> `Role Ref:` sub-fields must match the schedule entry for the enclosing phase.

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior-process artifact — not "Start"] | [specific completion condition] | R-[ID] or NONE | [concurrent window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1] | [completion condition] | R-[ID] or NONE | [concurrent window or NONE] |

Rules:
- Every phase must have a Primary Owner. Triggers must be specific.
- Every R-ID here must match an entry in the Role Registry Gate.
- Parallel windows must state start/end states (S-IDs) when known.

---

### Phase Structure

For each phase, produce the following five blocks in document order:

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Entry Condition must reference the prior phase's PHASE EXIT GATE "Required outputs" by name.
> Two sequential-linkage sub-fields are required and must not be conflated:
> (1) `Prior phase:` carries the literal phase identifier of the preceding phase block.
> (2) `Prior phase blocked bottleneck:` carries the B-ID from the prior exit gate.
> These are independent fields with different traceability directions.

- Entry Condition: [specific named artifact from prior phase's Required outputs field]
- Pre-condition check: R-[ID] ([role name — must match Role Sequence Schedule primary owner]) — [verification method]
- Blocking condition: [state entered and role notified if entry condition not met]
- Prior phase: [Literal identifier of the preceding phase, e.g., "PHASE 1 — Initiation".
  Phase 1 carries NONE or INIT as sentinel value. Must string-match the label of the preceding
  phase block in document order. Fails if: non-first phase carries sentinel; first phase carries
  a phase identifier; identifier does not match preceding phase label.]
- Prior phase blocked bottleneck: [B-ID from prior phase PHASE EXIT GATE `Blocked bottleneck:`
  or NONE or N/A (Phase 1). Must string-match prior exit gate AND B-NN block identifier.
  Example: "B-02 (inherited from Phase 1 exit gate — invoice matching backlog carries into
  Phase 2 until receipt confirmation is issued)."]

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition — name state, threshold breach, or missing input]
> - Trace: [state path; cite S-IDs in sequence]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason]
> - Bottleneck Ref: [B-NN that enabled this exception, or NONE. B-ID must string-match a
>   Bottleneck Analysis identifier. NONE if no declared bottleneck was causal.]
> - Role Ref: [R-ID of the ROLE SEQUENCE SCHEDULE primary owner for this phase. Literal R-ID
>   matching the schedule entry for the enclosing phase. Example: "R-02 — GL Manager owns
>   Phase 2 per Role Sequence Schedule; exception escalates through their approval queue."
>   Free-text role name without R-ID fails. R-ID absent from schedule fails. R-ID whose
>   schedule phase-ownership does not include this phase fails.]

Minimum 1 per phase; 3 total minimum. Role Ref and Bottleneck Ref are independent sub-fields;
populate both independently.

**SECTION B — STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules: Named Entry Condition required; Exits → S-ID or TERMINAL; standard Type values.

**Decision Supplement Blocks** (one per DECISION-type state):

> **DS-[S-ID] — [State Name]**
> - Condition: [rule or threshold]
> - Owner: R-[ID] ([role name from Role Registry])
> - Branch A ([outcome]): → S-[ID]
> - Branch B ([outcome]): → S-[ID] or TERMINAL
> - Fallback: [action if undecidable]

**PHASE EXIT GATE**

> `Blocked bottleneck:` names the B-ID that can delay this exit, or NONE. B-ID must
> string-match: (1) Bottleneck Analysis identifier, and (2) the next phase's PHASE ENTRY
> CONTRACT `Prior phase blocked bottleneck:` field. The next phase's `Prior phase:` field
> carries the phase label, not the B-ID — these are two separate traceability directions.

- Exit Condition: [what the phase must produce to be complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name — must match Role Sequence Schedule primary owner]) confirms all outputs present
- Blocking condition: [re-entry path or escalation if outputs absent]
- Blocked bottleneck: [B-NN or NONE. Example: "B-01 — manual reconciliation delays GL
  approval exit; R-02 is blocking role per Role Sequence Schedule. B-01 will appear in
  Phase 2 entry contract `Prior phase blocked bottleneck:` field."]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID] ([state name])
- **Branch 1**: [states traversed; cite S-IDs]
- **Branch 2**: [states traversed; cite S-IDs]
- **JOIN at**: S-[ID] ([join state name])
- **Join Condition**: AND-join / OR-join — specify and explain

---

### Edge Case Enumeration

Three or more, distinct from SECTION A:

> **EC-[N] — [Edge Case Name]**
> - Triggering Condition: [specific scenario]
> - Why Problematic: [specific consequence]
> - Correct Response: R-[ID] ([role name]) — [specific action]

---

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF — {Topic} lifecycle → [adjacent process name]**
> - Sending State: S-[ID]; Receiving Process: [name]; Data Payload: [fields]
> - Expected Acknowledgment: [signal]; Failure Mode: [if no acknowledgment]; Owner: R-[ID]

---

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|
| | | | | AT-RISK / ON-TRACK | B-NN (if AT-RISK) |

Minimum 3 rows; at least 1 AT-RISK citing a B-NN.

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN Cause field must satisfy both of the following conditions independently.
>
> **Dual-Cite Fail Condition A** — Cause field contains no IM-ID literal string (e.g., "IM-01"):
> fails C-39. Test: search Cause text for "IM-" followed by digits. Absence → fail.
>
> **Dual-Cite Fail Condition B** — Cause field contains no R-ID literal string (e.g., "R-02"):
> fails C-39. Test: search Cause text for "R-" followed by digits. Absence → fail.
>
> Partial citation fails the absent condition. Both must pass. B-IDs here must string-match:
> (1) PHASE EXIT GATE `Blocked bottleneck:` fields, (2) PHASE ENTRY CONTRACT `Prior phase
> blocked bottleneck:` fields in the following phase, and (3) EX block `Bottleneck Ref:`
> fields where non-NONE.
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
> (2) Labeled axes must appear in BOTH this preamble AND each B-NN per-block Evidence hint.
>
> Anti-embedding: Do not embed CHAIN STATUS inside the SLA ANALYSIS section.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field.**

---

**B-01 — [Bottleneck Name]**

- Cause: [Required: IM-ID literal string (Condition A) AND R-ID literal string (Condition B).
  Example: "IM-01 (manual spreadsheet GL reconciliation) combined with R-02 (GL Manager) peak
  unavailability — queue at S-05. Dual-cite: 'IM-01' satisfies A; 'R-02' satisfies B."]
  - Dual-Cite Fail Condition A: no IM-ID string in Cause → fails C-39
  - Dual-Cite Fail Condition B: no R-ID string in Cause → fails C-39
- Impact: [downstream state, SLA node, or adjacent process]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List AT-RISK SLA rows citing B-01. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]

---

**B-02 — [Bottleneck Name]**

- Cause: [Required: IM-ID literal string AND R-ID literal string.
  Example: "IM-02 (email routing without timestamp) combined with R-03 (Finance Controller)
  unavailability — invoice matching queue at S-07."]
  - Dual-Cite Fail Condition A: no IM-ID string in Cause → fails C-39
  - Dual-Cite Fail Condition B: no R-ID string in Cause → fails C-39
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List AT-RISK SLA rows citing B-02. Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]

---

**Gap Identification**

> MISSING: [step name] — [why it belongs; failure mode enabled; which phase; which IM-ID reduced]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [every AT-RISK SLA row cites a B-ID; enumerate pairs or name gap]
- Backward (B→SLA): [every B-NN names affected SLA nodes; enumerate or name gap]
- Exit gate consistency: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID matches a declared B-NN; name any mismatch]
- Phase-boundary B-NN continuity: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID string-matches the next phase's PHASE ENTRY CONTRACT `Prior phase blocked bottleneck:`; list pairs or name break]
- Phase-sequence: [every PHASE ENTRY CONTRACT `Prior phase:` identifier string-matches the label of the preceding phase block; PHASE 1 carries NONE/INIT; list phase pairs or name any mismatch]
- Exception→B: [every EX block `Bottleneck Ref:` B-ID (where non-NONE) matches a declared B-NN; list pairs or name unresolved block]
- Exception→Role: [every EX block `Role Ref:` R-ID matches the ROLE SEQUENCE SCHEDULE primary owner for the enclosing phase; list pairs or name any mismatch]
- Dual-cite status: [every B-NN Cause field contains both IM-ID and R-ID string; name any block missing either]
- Gap (if OPEN): [name the unresolved direction and the unlinked entry]

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

## V-05 — Axes D + E + F: Full Bidirectional Role-Ref + Prior-Phase Sequential Linkage

**Variation axes**: Role sequence + output format + lifecycle emphasis — all three axes active
simultaneously. EX blocks carry `Role Ref: R-ID` (Axis D, Exception→Role direction). The Role
Registry Gate gains a fourth check validating that every declared R-ID appears in at least one
EX block's `Role Ref:` (Axis E, Role→Exception direction, bidirectional closure). PHASE ENTRY
CONTRACTs carry `Prior phase: PHASE N` (Axis F, Phase→Phase sequential linkage). CHAIN STATUS
verifies all directions including both new ones. A seven-artifact cross-reference system:
INCUMBENT BASELINE / ROLE SEQUENCE SCHEDULE / EX blocks (Bottleneck Ref + Role Ref) / PHASE
ENTRY CONTRACT (Prior phase blocked bottleneck + Prior phase) / PHASE EXIT GATE (Blocked
bottleneck) / B-NN blocks (Cause, Evidence). Every declared artifact is reachable from every
other via at most two string comparisons.

**Hypothesis**: If C-40 requires bidirectional closure (both EX→Role in block and Role→Exception
in gate) and C-41 requires phase-sequence declaration (Prior phase: PHASE N in entry contract),
V-05 is the only R12 configuration where both criteria can simultaneously pass at their full
pass condition. V-04 isolates D+F without gate closure; V-02 isolates D+E without prior-phase;
V-05 is the compound test. If C-40 and C-41 are both present in V-05 output, the compound
architecture is confirmed as the minimum sufficient design. If C-40 passes in V-01/V-04 (single
direction) but not V-02 (which adds the gate), the bidirectional requirement is not a factor.
V-05 anchors the maximum-density configuration regardless of which sub-criteria surface.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must satisfy both Dual-Cite
> Fail Conditions. Quantified metric must appear before PHASE 1.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: tools, handoff mechanisms, storage, initiator]

**Incumbent failure modes**:

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure] | [frequency] | [downstream effect] |
| IM-02 | [second distinct failure mode] | [frequency] | [downstream effect] |

**Cost of no action**: [Named quantified measure declared before PHASE 1. Example: "Case
escalation rate: 34% of cases reach senior review vs 15% target" or "Period-close reconciliation
cycle: 6.2 days vs 4-day regulatory deadline."]

---

### Role Registry Gate

> GATE BLOCK: Complete before Role Sequence Schedule and before tracing any state.
> All four anti-generic checks must clear before proceeding. The fourth check requires that
> every declared R-ID appears in at least one EX block's `Role Ref:` sub-field — because
> EX blocks are generated after this gate, the check is a forward-reference constraint:
> declare which R-IDs will appear in EX block Role Ref fields before generating phase content,
> then verify at CHAIN STATUS time.

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
- [ ] Each declared R-ID must appear in at least one EX block's `Role Ref:` sub-field —
      generate phase content such that every R-ID in this registry is traceable to at least
      one exception trace in its owned phase; R-IDs with no EX trace are "dark" roles and
      are a gate violation reportable in CHAIN STATUS

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Role Sequence Schedule

> Declared after Role Registry Gate and before PHASE 1. Maps each R-ID to active phases,
> activation trigger, handoff trigger, and parallel windows. B-NN Cause fields must cite
> the blocking R-ID from this schedule (Dual-Cite Fail Condition B). R-IDs cited in EX block
> `Role Ref:` sub-fields must match the schedule entry for the enclosing phase. Because the
> registry gate requires every R-ID to appear in at least one EX block Role Ref, every row in
> this schedule must correspond to a phase that contains at least one EX block.

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior-process artifact — not "Start"] | [specific completion condition] | R-[ID] or NONE | [concurrent window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1] | [completion condition] | R-[ID] or NONE | [concurrent window or NONE] |

Rules:
- Every phase must have a Primary Owner. Triggers must be specific.
- Every R-ID here must match an entry in the Role Registry Gate.
- Parallel windows must state start/end states (S-IDs) when known.

---

### Phase Structure

For each phase, produce the following five blocks in document order:

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Entry Condition must reference the prior phase's PHASE EXIT GATE "Required outputs" by name.
> Two sequential-linkage sub-fields are required and must not be conflated:
> `Prior phase:` carries the literal phase identifier (Phase→Phase linkage, C-41 direction).
> `Prior phase blocked bottleneck:` carries the B-ID from the prior exit gate (B-NN boundary
> continuity, established in R11). Both are independently verifiable by string comparison.
> Three-way consistency for `Prior phase blocked bottleneck:`: this field, prior exit gate
> `Blocked bottleneck:`, and the B-NN block identifier must all match.

- Entry Condition: [specific named artifact from prior phase's Required outputs field]
- Pre-condition check: R-[ID] ([role name — must match Role Sequence Schedule primary owner for this phase]) — [verification method]
- Blocking condition: [state entered and role notified if entry condition not met]
- Prior phase: [Literal identifier of the preceding phase block, e.g., "PHASE 1 — Initiation".
  Phase 1 carries NONE or INIT as sentinel. Must string-match the label of the preceding phase
  block in document order. Fails if: non-first phase carries sentinel; first phase carries a
  phase identifier; identifier does not match preceding phase block label in document order.]
- Prior phase blocked bottleneck: [B-ID from prior phase PHASE EXIT GATE `Blocked bottleneck:`
  or NONE or N/A (Phase 1). Must string-match prior exit gate AND B-NN block identifier.
  Example: "B-01 (inherited from Phase 1 exit gate — manual reconciliation delay still active
  at phase boundary; R-02 is the blocking role per Role Sequence Schedule)."]

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition — name state, threshold breach, or missing input]
> - Trace: [path of states traversed from trigger to resolution or terminal; cite S-IDs]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason]
> - Bottleneck Ref: [B-NN that enabled this exception, or NONE. B-ID must string-match a
>   Bottleneck Analysis identifier. Example: "B-01 — manual reconciliation backlog created the
>   missing-entry condition that triggered this exception; R-02 was unavailable to resolve it
>   before the deadline." NONE if no declared bottleneck was causal.]
> - Role Ref: [R-ID of the ROLE SEQUENCE SCHEDULE primary owner for this phase. Literal R-ID
>   matching the schedule's Primary Owner entry for the phase containing this exception.
>   This field is required for the Role Registry Gate fourth check: every declared R-ID must
>   appear here in at least one EX block. Example: "R-02 — GL Manager owns Phase 2 per Role
>   Sequence Schedule; this exception escalates through their approval queue and contributes
>   to R-02's EX trace coverage required by the registry gate." Free-text role name without
>   R-ID fails. R-ID absent from schedule fails. R-ID whose schedule phase mapping does not
>   include this phase fails.]

Minimum 1 per phase; 3 total minimum. Each declared R-ID in the Role Registry Gate must appear
in at least one EX block Role Ref sub-field across all phases — CHAIN STATUS Role→Exception
direction verifies this. Bottleneck Ref and Role Ref are independent; populate both.

**SECTION B — STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules: Named Entry Condition required; Exits → S-ID or TERMINAL; standard Type values.

**Decision Supplement Blocks** (one per DECISION-type state):

> **DS-[S-ID] — [State Name]**
> - Condition: [rule or threshold]
> - Owner: R-[ID] ([role name from Role Registry])
> - Branch A ([outcome]): → S-[ID]
> - Branch B ([outcome]): → S-[ID] or TERMINAL
> - Fallback: [action if undecidable]

**PHASE EXIT GATE**

> `Blocked bottleneck:` names the B-ID that can delay this exit, or NONE. B-ID must
> string-match: (1) Bottleneck Analysis identifier, (2) the next phase's PHASE ENTRY CONTRACT
> `Prior phase blocked bottleneck:` field. The next phase's `Prior phase:` field carries the
> phase label — a separate traceability direction with no dependency on this B-ID.

- Exit Condition: [what the phase must produce to be complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name — must match Role Sequence Schedule primary owner]) confirms all outputs present
- Blocking condition: [re-entry path or escalation if outputs absent]
- Blocked bottleneck: [B-NN or NONE. B-ID must appear in Bottleneck Analysis AND be mirrored
  in the next phase's PHASE ENTRY CONTRACT `Prior phase blocked bottleneck:` field.
  Example: "B-01 — manual spreadsheet reconciliation by R-02 delays GL approval exit;
  this blocker carries forward to Phase 2 entry contract as prior-phase inherited bottleneck."]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID] ([state name])
- **Branch 1**: [states traversed; cite S-IDs]
- **Branch 2**: [states traversed; cite S-IDs]
- **JOIN at**: S-[ID] ([join state name])
- **Join Condition**: AND-join / OR-join — specify and explain

---

### Edge Case Enumeration

Three or more, distinct from SECTION A:

> **EC-[N] — [Edge Case Name]**
> - Triggering Condition: [specific scenario]
> - Why Problematic: [specific consequence]
> - Correct Response: R-[ID] ([role name]) — [specific action]

---

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF — {Topic} lifecycle → [adjacent process name]**
> - Sending State: S-[ID]; Receiving Process: [name]; Data Payload: [fields]
> - Expected Acknowledgment: [signal]; Failure Mode: [if no acknowledgment]; Owner: R-[ID]

---

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|
| | | | | AT-RISK / ON-TRACK | B-NN (if AT-RISK) |

Minimum 3 rows; at least 1 AT-RISK citing a B-NN.

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN Cause field must satisfy both of the following conditions independently.
>
> **Dual-Cite Fail Condition A** — Cause field contains no IM-ID literal string (e.g., "IM-01"):
> fails C-39. Test: search Cause text for "IM-" followed by digits. Absence → fail.
>
> **Dual-Cite Fail Condition B** — Cause field contains no R-ID literal string (e.g., "R-02"):
> fails C-39. Test: search Cause text for "R-" followed by digits. Absence → fail.
>
> Partial citation fails the absent condition. Both must pass. B-IDs here must string-match
> ALL of: (1) PHASE EXIT GATE `Blocked bottleneck:` fields, (2) PHASE ENTRY CONTRACT
> `Prior phase blocked bottleneck:` fields in the following phase, and (3) EX block
> `Bottleneck Ref:` fields where non-NONE. All four contexts must be consistent.
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
> (2) Labeled axes (`` `Required format:` `` / `` `Fail condition:` ``) must appear in BOTH
> this preamble AND each B-NN per-block Evidence hint.
>
> Anti-embedding: Do not embed CHAIN STATUS inside the SLA ANALYSIS section.
> Declare CHAIN STATUS in its own dedicated top-level section after SLA ANALYSIS.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field.**

---

**B-01 — [Bottleneck Name]**

- Cause: [Required: IM-ID literal string (Condition A) AND R-ID literal string (Condition B).
  Example: "IM-01 (manual spreadsheet GL reconciliation) combined with R-02 (GL Manager)
  period-close peak unavailability — causes queue accumulation at S-05. R-02 is Phase 2
  primary owner per Role Sequence Schedule. This B-ID appears in Phase 1 exit gate
  `Blocked bottleneck:`, Phase 2 entry contract `Prior phase blocked bottleneck:`, and any
  EX block with `Bottleneck Ref: B-01`. Dual-cite: 'IM-01' satisfies Condition A; 'R-02'
  satisfies Condition B."]
  - Dual-Cite Fail Condition A: no IM-ID string in Cause → fails C-39
  - Dual-Cite Fail Condition B: no R-ID string in Cause → fails C-39
- Impact: [downstream state, SLA node, or adjacent process]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List AT-RISK SLA rows citing B-01. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]

---

**B-02 — [Bottleneck Name]**

- Cause: [Required: IM-ID literal string AND R-ID literal string. Example: "IM-02 (email
  approval routing without SLA timestamp) combined with R-03 (Finance Controller) same-day
  unavailability — invoice matching queue at S-07. Dual-cite: 'IM-02' satisfies Condition A;
  'R-03' satisfies Condition B."]
  - Dual-Cite Fail Condition A: no IM-ID string in Cause → fails C-39
  - Dual-Cite Fail Condition B: no R-ID string in Cause → fails C-39
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List AT-RISK SLA rows citing B-02. Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]

---

**Gap Identification**

> MISSING: [step name] — [why it belongs; failure mode enabled; which phase; which IM-ID reduced]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [every AT-RISK SLA row cites a B-ID; enumerate pairs or name gap]
- Backward (B→SLA): [every B-NN names affected SLA nodes; enumerate or name gap]
- Exit gate consistency: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID matches a declared B-NN; name any mismatch]
- Phase-boundary B-NN continuity: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID string-matches the next phase's PHASE ENTRY CONTRACT `Prior phase blocked bottleneck:`; list phase pairs or name break]
- Phase-sequence: [every PHASE ENTRY CONTRACT `Prior phase:` identifier string-matches the label of the preceding phase block in document order; PHASE 1 carries NONE/INIT sentinel; list phase pairs or name any mismatch or missing sentinel]
- Exception→B: [every EX block `Bottleneck Ref:` B-ID (where non-NONE) matches a declared B-NN; list EX→B-NN pairs or name unresolved block]
- Exception→Role: [every EX block `Role Ref:` R-ID matches the ROLE SEQUENCE SCHEDULE primary owner for the enclosing phase; list EX→R-ID pairs or name any mismatch]
- Role→Exception: [every declared R-ID in the Role Registry Gate appears in at least one EX block's `Role Ref:` sub-field; list R-ID→EX block pairs; name any R-ID with no EX trace (dark role)]
- Dual-cite status: [every B-NN Cause field contains both IM-ID and R-ID string; name any block missing either]
- Gap (if OPEN): [name the unresolved direction and the unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal name] | SUCCESS | [branch or state] |
| [failure terminal name] | FAILURE | [branch or state] |
| [cancel terminal name] | CANCEL | [branch or state] |

> Every exit branch must reach a declared terminal. No mid-flow endings without `continues-via:`.
